"""Entry for make.fun news-image-20261124 (Python 3.13, standard library only).

The entry is one image, stored beside this file as base64 text in
entry.png.b64, summing up the world's news of Tuesday 24 November 2026.
The program decodes it to the output directory as entry.png. It writes
the same bytes on every run.
"""

import base64
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
_SRC = os.path.join(_HERE, "entry.png.b64")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(_SRC, "rb") as f:
        data = base64.b64decode(f.read())
    with open(os.path.join(out_dir, "entry.png"), "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
