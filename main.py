#!/usr/bin/env python3
"""Make the AI Judge Laugh: Cat Reviews Its Human — make.fun entry.

Writes one funny single-line one-star review from a house cat about
its human to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os

ENTRY = "One star: the human moved my sunbeam, feeds me late, and types on MY keyboard \u2014 so I knocked his coffee off the desk. Twice."
# Gate: a single line, 1-200 chars of UTF-8 text, not only whitespace.
assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
