#!/usr/bin/env python3
"""Minimal workflow entry point."""

from pathlib import Path


BASE_DIR = Path(__file__).parent
OUTPUTS_DIR = BASE_DIR / "outputs"


def main() -> None:
    OUTPUTS_DIR.mkdir(exist_ok=True)
    output = OUTPUTS_DIR / "example.txt"
    output.write_text("workflow ran\n", encoding="utf-8")
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()
