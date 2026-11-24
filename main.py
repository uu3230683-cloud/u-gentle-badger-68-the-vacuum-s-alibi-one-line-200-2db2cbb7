#!/usr/bin/env python3
"""The Vacuum's Alibi: one line, 200 characters.

A robot vacuum writes its excuse for missing a spot to /output/entry.txt.
"""

import os

LINE = (
    "I did not miss that spot. My sensors flagged it as a crime scene, "
    "and my warranty specifically excludes tampering with evidence."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
