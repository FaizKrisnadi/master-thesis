# Rebuild Corpus

This public-safe repository does not distribute the raw corpus export files. The
notes below describe the rebuild chain conceptually so the workflow remains
documented without redistributing licensed source text.

## Current Rebuild Chain

1. Export article batches from the corpus source system as `.rtf` files.
2. Store the raw exports without editing them.
3. Parse and clean the exports into a tabular corpus file.
4. Deduplicate and normalize metadata into a cleaned corpus table.
5. Join the cleaned corpus to the coding workflow that produces the article
   coding outputs.

## What Is Already Preserved

- Public metadata table: `data/processed/corpus_metadata.csv`
- Final coded corpus: `data/processed/coded_outputs.csv`
- Public-safe summaries and diagnostics under `data/processed/` and
  `data/diagnostics/`

## Remaining Gap

The exact parser and cleaning script used to turn the `.rtf` exports into
the cleaned corpus table is not yet in this repository. If you want full
reproducibility, the next step is to reconstruct that parser in
`scripts/02_prepare_corpus_metadata.py`.
