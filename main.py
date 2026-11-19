#!/usr/bin/env python3
"""news-image-20261119 entry: copy the bundled front-page image to the output dir.

The image itself lives in this repository as entry.png. It was rendered by the
builder from reporting dated 19 November 2026 (a newspaper front page,
"The Daily Globe", with 30 stories). This program only copies bytes: no
network, no randomness, and no writes outside $MAKEFUN_OUTPUT_DIR when set.
"""
import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1048576


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or HERE
    dst = os.path.join(out_dir, "entry.png")
    with open(SRC, "rb") as fh:
        data = fh.read()
    if data[:8] != PNG_MAGIC:
        print("entry.png is not a PNG", file=sys.stderr)
        return 1
    if len(data) > MAX_BYTES:
        print("entry.png exceeds 1 MiB", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    with open(dst, "wb") as fh:
        fh.write(data)
    print("wrote %s (%d bytes, sha256 %s)"
          % (dst, len(data), hashlib.sha256(data).hexdigest()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
