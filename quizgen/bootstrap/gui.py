"""Optional PySide6 GUI entry point.

Kept thin on purpose — all real work lives in `quizgen.handlers`. The GUI
is a view over the same handler functions the CLI calls, so behaviour
stays identical between the two surfaces.
"""

from __future__ import annotations

import sys

from quizgen.config.loader import load_settings
from quizgen.utils.logging import configure_logging


def main() -> int:
    settings = load_settings()
    configure_logging(settings.log_level)

    try:
        from PySide6.QtWidgets import QApplication
    except ImportError:
        print(
            "PySide6 not installed. Install the GUI extras:\n"
            '  pip install -e ".[gui]"',
            file=sys.stderr,
        )
        return 2

    from quizgen.gui.main_window import MainWindow

    app = QApplication(sys.argv)
    app.setApplicationName("quizgen")
    window = MainWindow(settings=settings)
    window.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())