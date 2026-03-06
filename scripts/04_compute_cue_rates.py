#!/usr/bin/env python3
"""Compute aggregate stance and framing summaries."""

from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
STANCE_OUTPUT = ROOT / "data" / "processed" / "stance_summary.csv"
FRAME_OUTPUT = ROOT / "data" / "processed" / "framing_summary.csv"


def main() -> None:
    pd.DataFrame(columns=["project_id", "stance_category", "document_count", "share"]).to_csv(
        STANCE_OUTPUT, index=False
    )
    pd.DataFrame(columns=["project_id", "frame_code", "document_count", "share"]).to_csv(
        FRAME_OUTPUT, index=False
    )
    print(f"Wrote {STANCE_OUTPUT}")
    print(f"Wrote {FRAME_OUTPUT}")


if __name__ == "__main__":
    main()
