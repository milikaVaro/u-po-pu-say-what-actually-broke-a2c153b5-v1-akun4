#!/usr/bin/env python3
"""Say What Actually Broke — one-line entry.

Writes a single line of software error copy (at most 200 characters)
to /output/entry.txt: it tells the user the brutal truth about what
went wrong and makes them laugh on the way.

Stdlib only, offline, deterministic: every run writes the same bytes.
"""

import os
from pathlib import Path

# The error: the database is down, and so is the team. Brutal,
# specific, and shippable in a real dialog.
# Counted at 96 characters — inside the 1..200 window.
LINE = (
    "The database is down. We know. We are also down. Please try "
    "again after we have both had coffee."
)


def output_dir() -> Path:
    """Where the grader expects the entry file.

    The grader runs the program from /bot with output at /output and
    no environment variables set, so the fallback is absolute.
    """
    return Path(os.environ.get("OUTPUT_DIR", "/output"))


def main() -> None:
    """Write the error line to entry.txt."""
    out = output_dir()
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(LINE, encoding="utf-8")


# Guard: only run when executed directly.
if __name__ == "__main__":
    main()
