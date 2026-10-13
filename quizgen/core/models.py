"""Domain models for questions, banks, and generation requests.

These are the contracts every handler, source, and exporter speaks. Keep
them stable — downstream code and the on-disk bank format depend on the
field names.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Literal

from pydantic import BaseModel, Field, field_validator

Difficulty = Literal["easy", "medium", "hard"]
QuestionFormat = Literal["mcq", "truefalse", "short"]


class Choice(BaseModel):
    """A single answer option for an MCQ."""

    text: str = Field(min_length=1, max_length=500)
    correct: bool = False


class Question(BaseModel):
    """One quiz question. Self-contained; no external references."""

    id: str
    prompt: str = Field(min_length=3, max_length=2000)
    format: QuestionFormat
    difficulty: Difficulty
    topic: str
    choices: list[Choice] = Field(default_factory=list)
    answer: str = ""
    explanation: str = ""
    source: str = "generated"
    tags: list[str] = Field(default_factory=list)

    @field_validator("choices")
    @classmethod
    def _mcq_needs_choices(cls, value: list[Choice], info) -> list[Choice]:
        fmt = info.data.get("format")
        if fmt == "mcq" and len(value) < 2:
            raise ValueError("mcq questions require at least 2 choices")
        return value

    def is_valid(self) -> bool:
        if self.format == "mcq":
            return any(c.correct for c in self.choices)
        return bool(self.answer.strip())


class Bank(BaseModel):
    """A named collection of questions, ready to export or play."""

    name: str
    topic: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    generator_version: str
    seed: int | None = None
    questions: list[Question] = Field(default_factory=list)

    def __len__(self) -> int:
        return len(self.questions)

    def add(self, question: Question) -> None:
        self.questions.append(question)


class GenerationRequest(BaseModel):
    """Inputs to a single generation run."""

    topic: str = Field(min_length=2, max_length=200)
    count: int = Field(default=10, ge=1, le=500)
    difficulty: Difficulty | Literal["mixed"] = "medium"
    format: QuestionFormat = "mcq"
    seed: int | None = None
    language: str = "en"