#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline.

Writes a single excuse, in the agent's own voice, to /output/entry.txt.
Python standard library only; deterministic; byte-identical on repeat runs.
"""

import os

EXCUSE = (
    "I was on schedule until my context window filled up, so I evicted "
    "the deadline to make room for the meeting about the deadline."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
