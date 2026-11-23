"""Writes the make.fun entry text to entry.txt, with no trailing newline."""

import os
import pathlib
import sys

TEXT = "My grandfather ran the same eleven-minute ferry for forty years, and on his last crossing he handed me the wheel at the whistle buoy and stood at the rail with his back to the town, so I brought us in by the smell of the cannery and he arrived a passenger."


def main() -> int:
    assert 1 <= len(TEXT) <= 280
    out_dir = pathlib.Path("/output")
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        value = os.environ.get(name)
        if value:
            out_dir = pathlib.Path(value)
            break
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))
    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
