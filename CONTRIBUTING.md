# Contributing to ai-quiz-trivia-generator

Thanks for wanting to make trivia generation better. This is a hobbyist
project — Python 3.11+, Windows-first, but the core engine runs anywhere
CPython runs.

## Ground rules

1. **One feature, one PR.** Small diffs land fast. Mega-PRs rot in review.
2. **Tests before merge.** `pytest -q` must be green. New generator
   backends need a fixture bank in `tests/fixtures/`.
3. **Type hints on public functions.** The engine is typed with
   `from __future__ import annotations`; mypy strict is enforced in CI.
4. **No network calls in core.** All remote LLM backends live behind
   `services/llm_backends/` and must be mockable.
5. **Determinism matters.** Every generator accepts a `seed` argument.
   If your backend can't be seeded, document why in the docstring.

## Dev setup

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e ".[dev]"
pre-commit install
pytest -q
```

## Adding a new question source

1. Subclass `QuestionSource` in `quizgen/services/sources/base.py`.
2. Register it in `quizgen/services/sources/__init__.py`.
3. Add a fixture JSON bank under `tests/fixtures/sources/`.
4. Add an integration test in `tests/test_sources.py`.

## Style

- `ruff` for lint + format. Line length 100.
- `black`-compatible output. No tabs.
- Docstrings in Google style for public modules.

## Reporting bugs

Open an issue with:
- Windows version + Python version
- The exact CLI invocation or GUI action
- The generated bank (redact if it contains private content)
- Full traceback from `logs/quizgen.log`

## Code of conduct

Be decent. Trivia is supposed to be fun, not a battleground.