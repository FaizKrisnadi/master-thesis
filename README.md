# Does the Label Matter?

This repository is the public replication companion for the master's thesis:

**Does the Label Matter? Explaining When Chinese Development Finance and FDI Blur in Indonesian Elite Narratives**

The project studies how Indonesian elite media narrate Chinese-linked capital. It asks why some cases stay in a routine diplomatic register, while others shift into technocratic scrutiny or polarized contestation. The empirical core of the repository is a coded media corpus, article-level metadata, derived summary tables, and documentation for the LLM-assisted measurement workflow used in the thesis.

Follow-on work: [nlp-thesis](https://github.com/FaizKrisnadi/nlp-thesis) fine-tunes multilingual BERT and XLM-R on these labels, with a TF-IDF baseline.

## Methods at a glance
- Corpus: 762 unique articles, 2013 to 2024, from Kompas, Tempo, and The Jakarta Post
- Task: assign one dominant frame, F1 to F5, and one stance, Supportive, Neutral, or Opposed, per article, with a one-sentence reasoning naming the key cues
- Validation: fixed 100-article set, fixed random seed 20260206, replicated across ChatGPT, Claude, and Gemini
- Agreement: ChatGPT vs Claude, stance 72% with kappa 0.570, frame 81% with kappa 0.736; Gemini pairs lower, 46% to 52%
- Human audit: manual review of 20 high-disagreement cases, focused on F5 vs F1 and Neutral vs Opposed
- Details: docs/llm_measurement_note.md, codebook in codebook/, prompts in prompts/

## What this repository contains

- public-safe article metadata in `data/processed/corpus_metadata.csv`
- coded article-level outputs in `data/processed/coded_outputs.csv`
- derived summaries for stance, framing, and case-level patterns
- the coding prompts, frame codebook, stance codebook, and tier definitions
- the thesis abstract and poster

## What this repository does not contain

This repository was sanitized before publication. It does **not** include:

- raw corpus export files
- full article text
- proprietary analytics exports or third-party screenshots
- sensitive interview materials
- offline source archives used during thesis assembly
- the full submitted thesis manuscript

The aim is to make the workflow legible without redistributing material that should not be public.

## Read this first

- Thesis abstract: [`docs/thesis_abstract.md`](docs/thesis_abstract.md)
- Full thesis manuscript: available on request
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
Krisnadi, Muhammad Faiz. 2026. Does the Label Matter? master-thesis repository. GitHub repository. https://github.com/FaizKrisnadi/master-thesis
```

If you are citing the thesis itself rather than the repository, use the thesis title and submitted manuscript metadata.

## License

This repository is released under the [`MIT License`](LICENSE). That license applies to the code and public-safe repository materials here, not to the full thesis manuscript, third-party source materials held offline, or other restricted materials described in the documentation.
