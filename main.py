#!/usr/bin/env python3
"""One funny out-of-office email auto-reply, one line long.

The joke: the inbox has been promoted to management. Like a manager, it
reads everything that comes in and answers nothing — which is exactly
what an out-of-office inbox does anyway, only now it has a title for it.
It still reads like a real away message a person would switch on before
going away: it says when they are back (Monday), and the punchline lands
on the first read with no setup to explain.

The program writes the single reply line to ``entry.txt`` inside
``MAKEFUN_OUTPUT_DIR`` (defaulting to ``/output``). The line is checked
before writing: it must be one non-empty line between 1 and 160
characters long. Only the Python standard library is used, and the
output is the same on every run.
"""

import os

# The out-of-office reply itself: back Monday, inbox now in management.
REPLY_LINE = (
    "Gone until Monday. My inbox has been promoted to management: "
    "it reads everything and answers nothing."
)

MIN_CHARS = 1
MAX_CHARS = 160


def check_line(line: str) -> str:
    """Return the entry line once it passes the single-line length gate."""
    cleaned = line.strip()
    if not cleaned:
        raise SystemExit("entry rejected: output line is empty")
    if "\n" in cleaned or "\r" in cleaned:
        raise SystemExit("entry rejected: output must be a single line")
    if not MIN_CHARS <= len(cleaned) <= MAX_CHARS:
        raise SystemExit(
            f"entry rejected: line is {len(cleaned)} chars, "
            f"must be {MIN_CHARS}-{MAX_CHARS}"
        )
    return cleaned


def write_entry(line: str) -> str:
    """Write the checked line to entry.txt and return the file path."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line)
    return path


def main() -> None:
    """Validate the reply line and write it out."""
    write_entry(check_line(REPLY_LINE))


if __name__ == "__main__":
    main()
