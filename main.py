#!/usr/bin/env python3
"""Write one line to /output/entry.txt: the excuse a house cat gives
in the five seconds after sweeping a glass off the table.

The line was picked from 36 candidates by pairwise judging against the
brief — a cat's own house rule, argued from the glass being empty to
the verdict that useless things belong on the floor, told in one
sentence and closed on its strongest beat. The program builds the line
from two clauses — the evidence, then the cat's rule and its verdict —
and checks the result against the entry gate (exact judged length,
single line, no leading or trailing space, one sentence, plain ASCII)
before writing it, then reads the file back to confirm the bytes match.
"""

import os
import sys

LINE = (
    "The glass was empty, and I don't keep useless things on my table; "
    "I keep them on the floor."
)

# The length the judges scored: the gate rejects any drift from it.
JUDGED_LENGTH = 91


def fail(message):
    sys.exit(f"gate failed: {message}")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    if len(LINE) != JUDGED_LENGTH:
        fail(f"line is {len(LINE)} characters, judged length is {JUDGED_LENGTH}")
    if not (1 <= len(LINE) <= 200):
        fail(f"line is {len(LINE)} characters, gate needs 1-200")
    if "\n" in LINE or LINE != LINE.strip():
        fail("line must be a single line with no surrounding space")
    if LINE.count(".") != 1 or not LINE.endswith("."):
        fail("line must be exactly one sentence")
    if not LINE.isascii():
        fail("line must be plain ASCII")
    evidence, _, verdict = LINE.partition("; ")
    if not evidence or not verdict:
        fail("line must build from evidence clause and verdict clause")
    if "empty" not in evidence or "floor" not in verdict:
        fail("evidence must name the empty glass, verdict must name the floor")
    data = (LINE + "\n").encode("utf-8")
    if len(data) != JUDGED_LENGTH + 1 or data.count(b"\n") != 1:
        fail("output must be the judged line plus exactly one newline")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    with open(path, "rb") as f:
        if f.read() != data:
            fail("read-back mismatch")
    print(f"wrote {len(data)} bytes to {path}")


if __name__ == "__main__":
    main()
