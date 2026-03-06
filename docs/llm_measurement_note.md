# LLM Measurement Note

The thesis uses an LLM-assisted content analysis workflow to code 762 articles
from Kompas, Tempo, and The Jakarta Post. The coded output is staged in
an offline source file and mirrored here as
`data/processed/coded_outputs.csv`.

## Measurement Targets

- Dominant frame
- Stance
- Narrative tier indicators derived from those labels

## Validation Artifacts Used for This Repo

- `LLM/validation_sample_100.csv`
- `LLM/validation_chatgpt.csv`
- `LLM/validation_claude.csv`
- `LLM/validation_gemini.csv`
- `LLM/inter_model_reliability_100_outputs/agreement_summary_100.csv`
- `LLM/inter_model_reliability_100_outputs/alignment_spotcheck_report.csv`

## Prompt Documentation in This Repo

- Primary coding prompt: `prompts/llm_coding_prompt.md`
- Cross-model validation prompt: `prompts/validation_prompt.md`

## Codebook Documentation in This Repo

- Frame definitions: `codebook/framing_codebook.md`
- Stance definitions: `codebook/stance_codebook.md`
- Narrative tier and perceived state-ness cue protocol:
  `codebook/tier_definitions.md`

## Inter-model Agreement Snapshot

Using the 100-article agreement summary:

- ChatGPT vs Claude: stance agreement 0.72, kappa 0.570
- ChatGPT vs Claude: frame agreement 0.81, kappa 0.736
- ChatGPT vs Gemini: stance agreement 0.52, kappa 0.292
- ChatGPT vs Gemini: frame agreement 0.46, kappa 0.203
- Claude vs Gemini: stance agreement 0.49, kappa 0.246

These results are mirrored in compact form in
`data/diagnostics/validation_summary.csv`.

## Current Limitation

This repo does not yet contain the exact production prompt text or the original
orchestration code that generated the final labels. The current documentation
captures the measurement logic and validation evidence, but not the full prompt
replay path.
