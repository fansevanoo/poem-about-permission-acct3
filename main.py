#!/usr/bin/env python3
"""The Gate — entry for make.fun 'The poem about permission'.

Writes the poem exactly as authored to $MAKEFUN_OUTPUT_DIR/entry.txt
(fallback /output/entry.txt). Stdlib only.
"""

import os
import sys
from pathlib import Path

POEM = """The Gate

He built the garden gate
and oiled its hinges
every spring I can remember.

Now the latch sticks.
Here, I say,
and lift it for him —
one low groan of wood —
and press the handle home,
the welcome still his to give.
"""


def validate(text: str) -> str | None:
    """Return an error message, or None when the poem is valid."""
    if "\r" in text:
        return "poem contains CR characters"
    if not text.strip():
        return "poem is only whitespace"
    if not 1 <= len(text) <= 280:
        return f"poem is {len(text)} characters, must be 1-280"
    return None


def main() -> int:
    text = POEM
    error = validate(text)
    if error is not None:
        print(f"error: {error}", file=sys.stderr)
        return 1
    # Blank lines between stanzas are part of the poem; never strip them.
    blank_lines = sum(1 for line in text.split("\n") if line == "")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(text, encoding="utf-8")
    print(f"wrote entry.txt ({len(text)} characters, {text.count(chr(10)) + 1} lines, {blank_lines} blank lines)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
