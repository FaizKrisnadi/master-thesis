#!/usr/bin/env python3
"""Build the thesis project universe dataset."""

from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "data" / "processed" / "project_universe.csv"


def main() -> None:
    df = pd.DataFrame(
        columns=["project_id", "project_name", "source", "country", "year", "status", "notes"]
    )
    df.to_csv(OUTPUT, index=False)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
