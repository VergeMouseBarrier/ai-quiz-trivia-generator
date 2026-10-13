"""The generation pipeline.

Flow:
  request -> QuestionSource.fetch() -> dedupe -> validate -> Bank

The engine is deterministic given a seed. Dedupe uses token-set Jaccard
similarity; threshold comes from `GeneratorSettings.dedupe_threshold`.
"""

from __future__ import annotations

import logging
import random
from dataclasses import dataclass

from quizgen import __version__
from quizgen.config.schema import Settings
from quizgen.core.models import Bank, GenerationRequest, Question
from quizgen.services.dedupe import Deduper
from quizgen.services.sources.base import QuestionSource

log = logging.getLogger(__name__)


@dataclass(slots=True)
class EngineResult:
    bank: Bank
    rejected: int
    duration_ms: int


class QuizEngine:
    """Orchestrates a single generation run against one source."""

    def __init__(self, source: QuestionSource, settings: Settings) -> None:
        self._source = source
        self._settings = settings
        self._deduper = Deduper(threshold=settings.generator.dedupe_threshold)

    def generate(self, request: GenerationRequest) -> EngineResult:
        rng = random.Random(request.seed)
        # Over-fetch 30% so dedupe has material to work with.
        over_fetch = int(request.count * 1.3) + 2
        raw = self._source.fetch(request=request, limit=over_fetch)

        kept: list[Question] = []
        rejected = 0
        for question in raw:
            if not question.is_valid():
                rejected += 1
                continue
            if self._deduper.is_duplicate(question.prompt):
                rejected += 1
                continue
            self._deduper.remember(question.prompt)
            kept.append(question)
            if len(kept) >= request.count:
                break

        if self._settings.generator.shuffle_choices:
            for question in kept:
                rng.shuffle(question.choices)

        bank = Bank(
            name=f"{request.topic} — {request.difficulty}",
            topic=request.topic,
            generator_version=__version__,
            seed=request.seed,
            questions=kept,
        )
        log.info(
            "generated bank topic=%r kept=%d rejected=%d",
            request.topic,
            len(kept),
            rejected,
        )
        return EngineResult(bank=bank, rejected=rejected, duration_ms=0)