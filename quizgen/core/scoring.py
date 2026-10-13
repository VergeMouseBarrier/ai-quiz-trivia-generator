"""Scoring for a completed quiz session.

Kept separate from generation so the GUI can score without re-importing
the engine. Pure functions, no I/O.
"""

from __future__ import annotations

from dataclasses import dataclass

from quizgen.core.models import Question


@dataclass(slots=True, frozen=True)
class Score:
    correct: int
    total: int
    accuracy: float
    by_difficulty: dict[str, float]


def score_answers(
    questions: list[Question],
    answers: dict[str, str],
) -> Score:
    """Score a mapping of question_id -> chosen answer text.

    Missing answers count as incorrect. Difficulty breakdown reports the
    accuracy per difficulty bucket so the GUI can show a heatmap.
    """
    correct = 0
    buckets: dict[str, list[bool]] = {}
    for question in questions:
        given = answers.get(question.id, "").strip().lower()
        expected = _expected_answer(question).strip().lower()
        hit = given == expected and given != ""
        correct += int(hit)
        buckets.setdefault(question.difficulty, []).append(hit)

    total = len(questions)
    return Score(
        correct=correct,
        total=total,
        accuracy=(correct / total) if total else 0.0,
        by_difficulty={
            diff: (sum(hits) / len(hits)) if hits else 0.0
            for diff, hits in buckets.items()
        },
    )


def _expected_answer(question: Question) -> str:
    if question.format == "mcq":
        for choice in question.choices:
            if choice.correct:
                return choice.text
        return ""
    return question.answer