"""Handler for the `quizgen import` action.

Imports run through `quizgen.utils.sanitize.sanitize_bank` before the
JSON is parsed, so a malicious bank can't smuggle a `__proto__`-style
payload into the pydantic model.
"""

from __future__ import annotations

import json
import logging
from pathlib import Path

from quizgen.config.schema import Settings
from quizgen.core.models import Bank
from quizgen.utils.paths import ensure_dir
from quizgen.utils.sanitize import sanitize_bank

log = logging.getLogger(__name__)


def run_import(*, source: Path, name: str, settings: Settings) -> Path:
    """Import an external bank into the local library. Returns destination."""
    raw = source.read_text(encoding="utf-8")
    if len(raw.encode("utf-8")) > settings.storage.max_bank_size_mb * 1024 * 1024:
        raise ValueError("bank exceeds max_bank_size_mb")
    cleaned = sanitize_bank(raw)
    data = json.loads(cleaned)
    data.setdefault("name", name)
    bank = Bank.model_validate(data)

    dest_dir = ensure_dir(settings.storage.library_dir)
    dest = dest_dir / f"{name}.json"
    dest.write_text(bank.model_dump_json(indent=2), encoding="utf-8")
    log.info("imported bank name=%r questions=%d", name, len(bank))
    return dest