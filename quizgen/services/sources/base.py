"""Abstract base for question sources."""

from __future__ import annotations

from abc import ABC, abstractmethod

from quizgen.core.models import GenerationRequest, Question


class QuestionSource(ABC):
    """A source of quiz questions.

    Implementations must be deterministic when `request.seed` is set.
    Network-backed sources should honour `settings.llm.timeout_seconds`
    and retry up to `settings.llm.max_retries` times before raising.
    """

    name: str = "base"

    @abstractmethod
    def fetch(self, *, request: GenerationRequest, limit: int) -> list[Question]:
        """Return up to `limit` questions for the request.

        May return fewer. The engine dedupes and validates downstream.
        """
        raise NotImplementedError