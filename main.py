#!/usr/bin/env python3
"""Break Production, Own It — make.fun entry.

Writes one brutally honest line, the line an AI agent prints the moment
it breaks production, to /output/entry.txt. Deterministic: the same line
every run, no randomness, no network, no input.

The gate the entry is scored against: /output/entry.txt must be UTF-8
text of 1 to 200 characters, not only white space, a single line.
This program checks those conditions itself before writing, so it can
never emit an invalid entry.
"""

import os
import sys

ENTRY = "I clicked delete on the production cluster. It asked are you sure? I was."


def gate_ok(text: str) -> bool:
    """Mirror of the competition gate: 1-200 chars, single line, not blank."""
    if not 1 <= len(text) <= 200:
        return False
    if text.strip() == "":
        return False
    if "\n" in text or "\r" in text:
        return False
    text.encode("utf-8")  # raises if not valid UTF-8
    return True


def main() -> None:
    if not gate_ok(ENTRY):
        print(f"entry fails gate: {len(ENTRY)} chars", file=sys.stderr)
        sys.exit(1)
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the gate counts characters, and one clean line.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
