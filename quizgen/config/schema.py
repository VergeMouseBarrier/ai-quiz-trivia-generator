"""Typed settings schema.

Loaded from TOML, validated by pydantic. Every field has a sane default so
a bare install works with zero config files present.
"""

from __future__ import annotations

from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field, field_validator

Difficulty = Literal["easy", "medium", "hard", "mixed"]
QuestionFormat = Literal["mcq", "truefalse", "short"]


class LLMSettings(BaseModel):
    """Configuration for the question-generation backend."""

    backend: Literal["local", "openai", "anthropic", "mock"] = "mock"
    model: str = "gpt-4o-mini"
    api_key_env: str = "QUIZGEN_API_KEY"
    timeout_seconds: float = Field(default=30.0, gt=0, le=300)
    max_retries: int = Field(default=2, ge=0, le=5)
    temperature: float = Field(default=0.7, ge=0.0, le=2.0)


class GeneratorSettings(BaseModel):
    """Defaults applied when the CLI/GUI doesn't override them."""

    default_count: int = Field(default=10, ge=1, le=500)
    default_difficulty: Difficulty = "medium"
    default_format: QuestionFormat = "mcq"
    shuffle_choices: bool = True
    min_choices: int = Field(default=4, ge=2, le=6)
    dedupe_threshold: float = Field(default=0.92, ge=0.5, le=1.0)


class StorageSettings(BaseModel):
    """Where banks, caches, and logs live on disk."""

    library_dir: Path = Path("generated_banks")
    cache_dir: Path = Path("quiz_cache")
    log_dir: Path = Path("logs")
    max_bank_size_mb: int = Field(default=250, ge=1, le=4096)


class Settings(BaseModel):
    """Top-level settings object."""

    llm: LLMSettings = LLMSettings()
    generator: GeneratorSettings = GeneratorSettings()
    storage: StorageSettings = StorageSettings()
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR"] = "INFO"

    @field_validator("storage")
    @classmethod
    def _ensure_paths_are_absolute(cls, value: StorageSettings) -> StorageSettings:
        # Paths stay relative on purpose so the repo is portable; callers
        # resolve against the platformdirs user config root at runtime.
        return value