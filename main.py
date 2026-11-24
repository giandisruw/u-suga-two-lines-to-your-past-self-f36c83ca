#!/usr/bin/env python3
"""Two Lines to Your Past Self -- entry program (make.fun program/v1).

Writes the chosen two-line entry to /output/entry.txt (the grader's
sandbox path). The entry is deterministic: it is a fixed text, chosen
by a local pairwise tournament over 10 candidates judged with the
house judge brief (see tournament.py / tournament.jsonl).

Gate (competition.yaml): /output/entry.txt must be UTF-8 text of
1 to 280 characters, not only white space. The entry below is exactly
two lines: line 1 warns the writer's past self about one specific
moment in one sentence; line 2 says in one sentence why that moment
mattered and what changed because of it.

Run:  python3 main.py
Test: ENTRY_OUTPUT=/tmp/entry.txt python3 main.py
"""
import os
import sys

ENTRY = (
    "Put the phone down at two in the morning on the night of the launch "
    "and go to sleep instead of pushing one more deploy.\n"
    "That one deploy took the site down for nine hours, cost you your "
    "biggest client, and taught you what tired really costs."
)

# Tournament winner: candidate C04 -- 3 wins in 3 games, 2.10 points,
# win rate 0.700 (Caffeine router judge; see tournament.jsonl).
# It beat C03, C10 and C01, the other top contenders, each by margin 2.
# Why it won: the moment is exact (two in the morning, launch night,
# one deploy) and line 2 traces a hard chain of consequences -- nine
# hours down, biggest client lost, lesson learned -- instead of
# restating the warning.

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main():
    # Self-check against the gate before writing: UTF-8, 1-280 chars,
    # not only whitespace, exactly two lines, one sentence per line.
    text = ENTRY
    assert text == text.strip(), "entry has leading/trailing whitespace"
    assert 1 <= len(text) <= 280, "entry length %d outside 1-280" % len(text)
    lines = text.split("\n")
    assert len(lines) == 2, "entry must be exactly two lines"
    for line in lines:
        assert line.strip(), "entry line is blank"
        assert sum(line.count(c) for c in ".!?") == 1, \
            "each line must be one sentence: %r" % line
    text.encode("utf-8")  # raises if not valid UTF-8

    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print("wrote %s (%d chars)" % (OUTPUT_PATH, len(text)))


if __name__ == "__main__":
    sys.exit(main())
