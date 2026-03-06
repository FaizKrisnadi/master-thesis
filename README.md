# Does the Label Matter?

This repository is the public-safe research companion for the master's thesis:

**Does the Label Matter? Explaining When Chinese Development Finance and FDI Blur in Indonesian Elite Narratives**

The project studies how Indonesian elite media narrate Chinese-linked capital. It asks why some cases stay in a routine diplomatic register, while others shift into technocratic scrutiny or polarized contestation. The empirical core of the repository is a coded media corpus, article-level metadata, derived summary tables, and documentation for the LLM-assisted measurement workflow used in the thesis.

## What this repository contains

- public-safe article metadata in `data/processed/corpus_metadata.csv`
- coded article-level outputs in `data/processed/coded_outputs.csv`
- derived summaries for stance, framing, and case-level patterns
- the coding prompts, frame codebook, stance codebook, and tier definitions
- the submitted thesis draft, abstract, and poster

## What this repository does not contain

This repository was sanitized before publication. It does **not** include:

- raw corpus export files
- full article text
- proprietary analytics exports or third-party screenshots
- sensitive interview materials
- offline source archives used during thesis assembly

The aim is to make the workflow legible without redistributing material that should not be public.

## Read this first

- Thesis abstract: [`docs/thesis_abstract.md`](docs/thesis_abstract.md)
- Submitted draft: [`docs/thesis_submitted_draft.pdf`](docs/thesis_submitted_draft.pdf)
- Poster: [`docs/poster.pdf`](docs/poster.pdf)
- Data access and provenance notes: [`docs/data_access.md`](docs/data_access.md)

## Repository map

- [`codebook/`](codebook/) defines frames, stance labels, narrative tiers, and perceived state-ness cues.
- [`prompts/`](prompts/) documents the production coding prompt and the fixed-subset validation prompt.
- [`data/processed/`](data/processed/) contains the public metadata table, coded outputs, and derived summaries.
- [`data/diagnostics/`](data/diagnostics/) contains compact validation and cue-hit diagnostics.
- [`docs/`](docs/) contains the thesis-facing write-up materials.
- [`scripts/`](scripts/) contains the numbered pipeline skeleton used to organize the workflow.

## Public data structure

The public metadata table has this schema:

```text
document_id, project_id, project_name, publish_date, outlet, title, author
```

The coded output table adds the analytic labels:

```text
document_id, project_id, project_name, publish_date, outlet, stance_code, frame_code, reasoning, coder, model_name
```

## Reproducing the workflow

1. Copy `config/paths.example.yml` to `config/paths.yml`.
2. Point the local paths to your own offline source archive.
3. Install dependencies with `pip install -r requirements.txt`.
4. Run the numbered scripts in `scripts/` from the repository root.

The current public repo preserves the structure of the workflow, but not every private or licensed upstream source file needed for a full rerun. See [`docs/rebuild_corpus.md`](docs/rebuild_corpus.md) and [`docs/data_access.md`](docs/data_access.md) for the missing pieces.

## Citation

If you use this repository, cite the repository metadata in [`CITATION.cff`](CITATION.cff).

Suggested citation:

```text
Krisnadi, Faiz. 2026. Does the Label Matter? master-thesis repository. GitHub repository. https://github.com/FaizKrisnadi/master-thesis
```

If you are citing the thesis itself rather than the repository, use the submitted draft and thesis title in [`docs/thesis_submitted_draft.pdf`](docs/thesis_submitted_draft.pdf).

## License

This repository is released under the [`MIT License`](LICENSE). That license applies to the repository contents here, not necessarily to third-party source materials held offline and described in the documentation.
