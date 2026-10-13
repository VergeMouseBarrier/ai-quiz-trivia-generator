"""CLI entry point for the quizgen desktop tool.

Subcommands map 1:1 onto the feature handlers in `quizgen.handlers`.
The CLI is the headless surface; the GUI wraps the same handlers.
"""

from __future__ import annotations

import logging
import sys
from pathlib import Path

import typer
from rich.console import Console

from quizgen import __version__
from quizgen.config.loader import load_settings
from quizgen.handlers.generate import run_generate
from quizgen.handlers.export import run_export
from quizgen.handlers.import_bank import run_import
from quizgen.utils.logging import configure_logging

app = typer.Typer(
    name="quizgen",
    help="AI-powered quiz and trivia generator.",
    no_args_is_help=True,
    add_completion=False,
)
console = Console()


@app.command()
def generate(
    topic: str = typer.Argument(..., help="Subject for the quiz, e.g. 'cold war espionage'."),
    count: int = typer.Option(10, "--count", "-n", min=1, max=500),
    difficulty: str = typer.Option("medium", "--difficulty", "-d"),
    fmt: str = typer.Option("mcq", "--format", "-f", help="mcq | truefalse | short"),
    seed: int | None = typer.Option(None, "--seed"),
    out: Path = typer.Option(Path("generated_banks"), "--out", "-o"),
) -> None:
    """Generate a fresh quiz bank for a topic."""
    settings = load_settings()
    configure_logging(settings.log_level)
    bank_path = run_generate(
        topic=topic,
        count=count,
        difficulty=difficulty,
        fmt=fmt,
        seed=seed,
        out_dir=out,
        settings=settings,
    )
    console.print(f"[green]wrote[/green] {bank_path}")


@app.command("import")
def import_cmd(
    source: Path = typer.Argument(..., exists=True, readable=True),
    name: str = typer.Option(..., "--name"),
) -> None:
    """Import an external question bank into the local library."""
    settings = load_settings()
    configure_logging(settings.log_level)
    dest = run_import(source=source, name=name, settings=settings)
    console.print(f"[green]imported[/green] {dest}")


@app.command()
def export(
    bank: Path = typer.Argument(..., exists=True, readable=True),
    fmt: str = typer.Option("json", "--format", "-f", help="json | csv | anki"),
    out: Path = typer.Option(Path("exports"), "--out", "-o"),
) -> None:
    """Export a bank to a portable format."""
    settings = load_settings()
    configure_logging(settings.log_level)
    dest = run_export(bank=bank, fmt=fmt, out_dir=out, settings=settings)
    console.print(f"[green]exported[/green] {dest}")


@app.command()
def version() -> None:
    """Print the tool version."""
    console.print(f"quizgen {__version__}")


def main() -> int:
    try:
        app()
        return 0
    except KeyboardInterrupt:
        console.print("[yellow]interrupted[/yellow]")
        return 130
    except Exception as exc:  # noqa: BLE001 — top-level guard
        logging.getLogger("quizgen").exception("fatal: %s", exc)
        return 1


if __name__ == "__main__":
    sys.exit(main())