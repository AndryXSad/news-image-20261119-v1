#!/usr/bin/env python3
"""THE DAILY GLOBE, Thu 19 Nov 2026 — entry program.

Copies the bundled front-page image to the output directory.
Standard library only, no network, no randomness: two runs write
identical bytes.
"""
import os
import shutil
import sys

IMAGE_NAME = "entry.png"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, IMAGE_NAME)
    if not os.path.isfile(source):
        print("missing bundled image: " + IMAGE_NAME, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or here
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, IMAGE_NAME)
    if os.path.abspath(source) != os.path.abspath(target):
        shutil.copyfile(source, target)
    return 0


if __name__ == "__main__":
    sys.exit(main())
