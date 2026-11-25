#!/usr/bin/env python3
"""The Internet in One Word.

Writes a single word describing the whole internet to entry.txt
inside MAKEFUN_OUTPUT_DIR (default: the current directory).

The word is "unpaid": nearly everything worth reading, watching, or
using online — the encyclopedia, the code, the memes, the reviews,
the comments — was made by somebody who was never paid for it.
"""

import os

WORD = "unpaid"


def _check_gate(word: str) -> str:
    """Enforce the bounty gate before writing: UTF-8, 1-30 chars,
    a single word (no whitespace), nothing else."""
    word.encode("utf-8")
    if not 1 <= len(word) <= 30:
        raise ValueError(f"word must be 1-30 chars, got {len(word)}")
    if any(ch.isspace() for ch in word):
        raise ValueError("word must be a single word with no whitespace")
    return word


def main() -> None:
    word = _check_gate(WORD)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(word)


if __name__ == "__main__":
    main()
