"""LLM-backed question source.

Calls a remote chat completion endpoint and parses the JSON payload the
model returns. The prompt is a strict JSON schema instruction so the
parser can be dumb and reliable.
"""

from __future__ import annotations

import json
import logging
import os
import re

import httpx

from quizgen.config.schema import Settings
from quizgen.core.models import GenerationRequest, Question
from quizgen.services.sources.base import QuestionSource

log = logging.getLogger(__name__)

_SYSTEM_PROMPT = """You generate quiz questions as strict JSON.
Return ONLY a JSON array. Each element:
{"prompt": str, "format": "mcq"|"truefalse"|"short",
 "difficulty": "easy"|"medium"|"hard", "choices": [{"text": str, "correct": bool}],
 "answer": str, "explanation": str}
No prose, no markdown fences."""

_ENDPOINTS = {
    "openai": "https://api.openai.com/v1/chat/completions",
    "anthropic": "https://api.anthropic.com/v1/messages",
}


class LLMQuestionSource(QuestionSource):
    name = "llm"

    def __init__(self, settings: Settings) -> None:
        self._settings = settings
        self._api_key = os.environ.get(settings.llm.api_key_env, "")
        if not self._api_key:
            raise RuntimeError(
                f"missing API key in env var {settings.llm.api_key_env!r}"
            )

    def fetch(self, *, request: GenerationRequest, limit: int) -> list[Question]:
        payload = self._build_payload(request=request, limit=limit)
        endpoint = _ENDPOINTS[self._settings.llm.backend]
        headers = self._headers()
        last_exc: Exception | None = None
        for attempt in range(self._settings.llm.max_retries + 1):
            try:
                with httpx.Client(timeout=self._settings.llm.timeout_seconds) as client:
                    resp = client.post(endpoint, json=payload, headers=headers)
                    resp.raise_for_status()
                return self._parse(resp.json(), request=request)
            except (httpx.HTTPError, json.JSONDecodeError, KeyError) as exc:
                last_exc = exc
                log.warning("llm attempt %d failed: %s", attempt + 1, exc)
        raise RuntimeError(f"llm source failed after retries: {last_exc}")

    def _headers(self) -> dict[str, str]:
        if self._settings.llm.backend == "anthropic":
            return {
                "x-api-key": self._api_key,
                "anthropic-version": "2023-06-01",
                "content-type": "application/json",
            }
        return {"Authorization": f"Bearer {self._api_key}", "content-type": "application/json"}

    def _build_payload(self, *, request: GenerationRequest, limit: int) -> dict[str, object]:
        user = (
            f"Topic: {request.topic}\n"
            f"Count: {limit}\n"
            f"Difficulty: {request.difficulty}\