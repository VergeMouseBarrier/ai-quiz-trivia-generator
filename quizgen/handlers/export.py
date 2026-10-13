"""Handler for the `quizgen export` action."""

from __future__ import annotations

import csv
import json
import logging
from pathlib import Path

from quizgen.config.schema import Settings
from quizgen.core.models import Bank
from quizgen.utils.paths import ensure_dir

log = logging.getLogger(__name__)


def run_export(*, bank: Path, fmt: str, out_dir: Path, settings: Settings) -> Path:
    """Export a bank to json, csv, or anki (tab-separated)."""
    data = json.loads(bank.read_text(encoding="utf-8"))
    model = Bank.model_validate(data)
    ensure_dir(out_dir)
    stem = bank.stem

    if fmt == "json":
        dest = out_dir / f"{stem}.json"
        dest.write_text(model.model_dump_json(indent=2), encoding="utf-8")
    elif fmt == "csv":
        dest = out_dir / f"{stem}.csv"
        with dest.open("w", encoding="utf-8", newline="") as fh:
            writer = csv.writer(fh)
            writer.writerow(["id", "prompt", "format", "difficulty", "answer", "explanation"])
            for q in model.questions:
                answer = q.answer or next((c.text for c in q.choices if c.correct), "")
                writer.writerow([q.id, q.prompt, q.format, q.difficulty, answer, q.explanation])
    elif fmt == "anki":
        dest = out_dir / f"{stem}.txt"
        with dest.open("w", encoding="utf-8") as fh:
            for q in model.questions:
                answer = q.answer or next((c.text for c in q.choices if c.correct), "")
                fh.write(f"{q.prompt}\t{answer}\n")
    else:
        raise ValueError(f"unknown export format: {fmt!r}")

    log.info("exported bank=%s fmt=%s dest=%s", stem, fmt, dest)
    return dest