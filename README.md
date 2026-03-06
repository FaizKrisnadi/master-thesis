# master-thesis

Repository scaffold for a master's thesis workflow covering corpus construction,
LLM-assisted coding, validation, and output generation.

## Structure

- `config/`: local path examples and run parameters
- `data/`: raw, external, processed, and diagnostics datasets
- `docs/`: thesis-facing notes and project documentation
- `codebook/`: coding definitions for framing, stance, and case tiers
- `prompts/`: reusable prompts for coding and validation
- `scripts/`: numbered analysis pipeline scripts
- `outputs/`: generated figures, tables, and logs
- `interviews/`: interview handling notes and metadata policy

## Public-Safe Repository

This repository is sanitized for public release. It intentionally excludes:

- raw corpus exports
- full article text
- proprietary figure exports
- sensitive interview materials

## Current Repo State

- `data/raw/` is intentionally empty in the public-safe version except for a
  placeholder file.
- `data/processed/corpus_metadata.csv` is a metadata-only public table with no
  article text.
- `data/processed/` has been populated from the thesis corpus and coded output files.
- `data/diagnostics/` has been populated from cue-hit, unmatched-ID, and
  inter-model agreement artifacts.
- `docs/poster.pdf` contains the thesis poster.
- `docs/thesis_submitted_draft.pdf` contains the submitted thesis draft.

## Quick Start

1. Create a local copy of `config/paths.example.yml` as `config/paths.yml`.
2. Update local filesystem paths and API credentials as needed.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run scripts in numeric order from the repository root.

## Notes

- The current processed tables were derived from an offline source archive.
- `project_universe.csv` is derived from the coded corpus because no separate
  canonical universe table is distributed in this public-safe repo.
- Key thesis documents: `docs/thesis_abstract.md` and
  `docs/thesis_submitted_draft.pdf`.
