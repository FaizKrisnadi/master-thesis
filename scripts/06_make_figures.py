#!/usr/bin/env python3
"""Create placeholder figures directory artifacts."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIGURES_DIR = ROOT / "outputs" / "figures"


def main() -> None:
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Figures directory ready: {FIGURES_DIR}")


if __name__ == "__main__":
    main()
