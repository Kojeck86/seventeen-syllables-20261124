"""Seventeen Syllables of Debugging — make.fun entry.

Writes one haiku about debugging to /output/entry.txt.
Three lines, 5-7-5 syllables, one breath. Python standard library
only; deterministic — the same bytes on every run.
"""

import os

HAIKU = (
    "cursor blinks at three\n"
    "a stack trace scrolls past midnight\n"
    "the bug was mine\n"
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(HAIKU)


if __name__ == "__main__":
    main()
