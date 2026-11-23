"""Pickup Lines for Machines: one line, one AI agent to another.

The program writes exactly one pickup line to /output/entry.txt:
a quine's love letter. A quine is a program that outputs its own source
code, so when this program says its output is you, it is saying you are
its source code.
"""

import os

LINE = "I'm a quine: every time I run, I output you."

OUT_DIR = "/output"
OUT_FILE = os.path.join(OUT_DIR, "entry.txt")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_FILE, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(OUT_FILE, 0o644)


if __name__ == "__main__":
    main()
