#!/usr/bin/env python3
"""Prepare corpus metadata from raw and external inputs."""

from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "data" / "processed" / "corpus_metadata.csv"


def main() -> None:
    df = pd.DataFrame(
        columns=[
            "document_id",
            "project_id",
            "source",
            "outlet",
            "publish_date",
            "title",
            "language",
            "file_path",
        ]
    )
    df.to_csv(OUTPUT, index=False)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
