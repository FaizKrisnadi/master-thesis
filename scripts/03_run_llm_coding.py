#!/usr/bin/env python3
"""Stub entrypoint for LLM-assisted document coding."""

from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "data" / "processed" / "coded_outputs.csv"


def main() -> None:
    df = pd.DataFrame(
        columns=["document_id", "project_id", "frame_code", "stance_code", "coder", "model_name", "run_id"]
    )
    df.to_csv(OUTPUT, index=False)
    print("LLM coding stub completed.")
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
