"""Question sources. Each source implements `QuestionSource.fetch`."""

from __future__ import annotations

from quizgen.config.schema import Settings
from quizgen.services.sources.base import QuestionSource
from quizgen.services.sources.llm_source import LLMQuestionSource
from quizgen.services.sources.static_source import StaticBankSource


def build_source(*, settings: Settings) -> QuestionSource:
    """Pick a source based on settings.llm.backend.

    `mock` and `local` both fall through to the static bank so the tool
    works offline out of the box. `openai` and `anthropic` route through
    the LLM source.
    """
    if settings.llm.backend in {"openai", "anthropic"}:
        return LLMQuestionSource(settings=settings)
    return StaticBankSource(settings=settings)


__all__ = ["QuestionSource", "LLMQuestionSource", "StaticBankSource", "build_source"]