#!/usr/bin/env python3
"""Generate case-level metrics and thesis-ready tabular outputs."""

from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "data" / "processed" / "case_metrics.csv"


def main() -> None:
    df = pd.DataFrame(
        columns=["project_id", "total_documents", "avg_stance_score", "avg_frame_hits", "notes"]
    )
    df.to_csv(OUTPUT, index=False)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
