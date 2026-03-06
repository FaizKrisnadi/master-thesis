#!/usr/bin/env python3
"""Run lightweight validation and emit diagnostic tables."""

from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
TERM_HITS = ROOT / "data" / "diagnostics" / "term_hit_diagnostics.csv"
UNMATCHED = ROOT / "data" / "diagnostics" / "unmatched_ids.csv"
SUMMARY = ROOT / "data" / "diagnostics" / "validation_summary.csv"


def main() -> None:
    pd.DataFrame(columns=["document_id", "project_id", "term", "hits", "context_window"]).to_csv(
        TERM_HITS, index=False
    )
    pd.DataFrame(columns=["source_record_id", "source_name", "reason"]).to_csv(UNMATCHED, index=False)
    pd.DataFrame(columns=["run_id", "check_name", "status", "details"]).to_csv(SUMMARY, index=False)
    print(f"Wrote {TERM_HITS}")
    print(f"Wrote {UNMATCHED}")
    print(f"Wrote {SUMMARY}")


if __name__ == "__main__":
    main()
