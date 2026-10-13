"""TOML settings loader with layered overrides.

Resolution order (later wins):
  1. Built-in defaults from `quizgen.config.schema`
  2. `%APPDATA%/quizgen/config.toml` (or platformdirs equivalent)
  3. `./quizgen.toml` in the current working directory
  4. `QUIZGEN_*` environment variables
"""

from __future__ import annotations

import os
import tomllib
from functools import lru_cache
from pathlib import Path

from platformdirs import user_config_dir

from quizgen.config.schema import Settings

_ENV_PREFIX = "QUIZGEN_"


def _user_config_path() -> Path:
    return Path(user_config_dir("quizgen", "quizgen")) / "config.toml"


def _read_toml(path: Path) -> dict[str, object]:
    if not path.is_file():
        return {}
    with path.open("rb") as fh:
        return tomllib.load(fh)


def _apply_env_overrides(data: dict[str, object]) -> dict[str, object]:
    """Fold `QUIZGEN_LLM__BACKEND=openai` style vars into the config tree."""
    merged = dict(data)
    for key, raw in os.environ.items():
        if not key.startswith(_ENV_PREFIX):
            continue
        path = key[len(_ENV_PREFIX) :].lower().split("__")
        cursor: dict[str, object] = merged
        for part in path[:-1]:
            cursor = cursor.setdefault(part, {})  # type: ignore[assignment]
        cursor[path[-1]] = raw
    return merged


@lru_cache(maxsize=1)
def load_settings() -> Settings:
    """Load and validate settings. Cached for the process lifetime."""
    merged: dict[str, object] = {}
    for source in (_user_config_path(), Path.cwd() / "quizgen.toml"):
        merged.update(_read_toml(source))
    merged = _apply_env_overrides(merged)
    return Settings.model_validate(merged)


def reset_settings_cache() -> None:
    """Clear the settings cache. Used by tests and the GUI's reload action."""
    load_settings.cache_clear()