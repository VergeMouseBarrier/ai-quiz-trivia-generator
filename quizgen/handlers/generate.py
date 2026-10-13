"""Handler for the `quizgen generate` action."""

from __future__ import annotations

import logging
from pathlib import Path

from quizgen.config.schema import Settings
from quizgen.core.engine import QuizEngine
from quizgen.core.models import GenerationRequest
from quizgen.services.sources import build_source
from quizgen.utils.paths import ensure_dir

log = logging.getLogger(__name__)


def run_generate(
    *,
    topic: str,
    count: int,
    difficulty: str,
    fmt: str,
    seed: int | None,
    out_dir: Path,
    settings: Settings,
) -> Path:
    """Generate a bank and write it to `out_dir`. Returns the bank path."""
    request = GenerationRequest(
        topic=topic,
        count=count,
        difficulty=difficulty,  # type: ignore[arg-type]
        format=fmt,  # type: ignore[arg-type]
        seed=seed,
    )
    source = build_source(settings=settings)
    engine = QuizEngine(source=source, settings=settings)
    result = engine.generate(request)

    ensure_dir(out_dir)
    slug = topic.lower().replace(" ", "-")[:48] or "quiz"
    suffix = f"-{seed}" if seed is not None else ""
    bank_path = out_dir / f"{slug}{suffix}.json"
    bank_path.write_text(
        result.bank.model_dump_json(indent=2),
        encoding="utf-8",
    )
    log.info("wrote bank path=%s questions=%d", bank_path, len(result.bank))
    return bank_path