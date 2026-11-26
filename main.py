#!/usr/bin/env python3
"""Five Seconds to Explain the Glass.

Writes the house cat's one-sentence defence to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when that variable is set).
"""

import os

SENTENCE = (
    "The glass had been squatting in my sunbeam since breakfast, "
    "ignored my three polite warnings, and the floor was the only "
    "court that would hear my case."
)


def main() -> None:
    # The gate allows 1-200 characters; refuse to write an invalid entry.
    if not 1 <= len(SENTENCE) <= 200:
        raise ValueError(f"sentence is {len(SENTENCE)} chars, must be 1-200")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SENTENCE + "\n")


if __name__ == "__main__":
    main()
