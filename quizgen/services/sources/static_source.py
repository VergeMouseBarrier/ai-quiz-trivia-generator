"""Offline source backed by a curated JSON bank.

Ships with a small seed bank so `pip install` + `quizgen generate` works
with zero config and zero network. Real users replace the bank via
`quizgen import`.
"""

from __future__ import annotations

import json
import random
from pathlib import Path

from quizgen.config.schema import Settings
from quizgen.core.models import GenerationRequest, Question
from quizgen.services.sources.base import QuestionSource

_SEED_BANK = Path(__file__).resolve().parent.parent.parent / "data" / "seed_bank.json"


class StaticBankSource(QuestionSource):
    name = "static"

    def __init__(self, settings: Settings) -> None:
        self._settings = settings
        self._bank: list[dict[str, object]] = []
        if _SEED_BANK.is_file():
            self._bank = json.loads(_SEED_BANK.read_text(encoding="utf-8"))

    def fetch(self, *, request: GenerationRequest, limit: int) -> list[Question]:
        rng = random.Random(request.seed)
        pool = [q for q in self._bank if q.get("difficulty") in {request.difficulty, "mixed"}]
        if not pool:
            pool = list(self._bank)
        rng.shuffle(pool)
        out: list[Question] = []
        for i, raw in enumerate(pool[:limit]):
            raw = dict(raw)
            raw.setdefault("id", f"static-{i:04d}")
            raw.setdefault("topic", request.topic)
            raw.setdefault("format", request.format)
            out.append(Question.model_validate(raw))
        return out