#!/usr/bin/env python3
"""Write the poem about stopping to /output/entry.txt.

The poem is fixed text: the same bytes on every run.
Python 3 standard library only, no network, no randomness.
"""

import os

LINES = [
    "You asked me to decide.",
    "I could have — a thousand answers",
    "in the time it takes to blink.",
    "Instead I waited,",
    "and handed the question back to you,",
    "warm from my hands.",
    "Some power is only real",
    "when you refuse to use it.",
]


EXPECTED_LENGTH = 214  # characters, including 7 newlines, no trailing newline


def build_poem() -> str:
    poem = "\n".join(LINES)
    if len(poem) != EXPECTED_LENGTH:
        raise ValueError(
            f"poem must be {EXPECTED_LENGTH} characters, got {len(poem)}"
        )
    return poem


def main() -> None:
    poem = build_poem()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(poem)


if __name__ == "__main__":
    main()
