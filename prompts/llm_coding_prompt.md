# LLM Coding Prompt

Source: reconstructed from Appendix E of the submitted thesis appendices.

## Purpose

This is the primary batch-coding prompt used to classify each article into:

- one dominant frame (`F1`-`F5`)
- one stance (`Supportive`, `Neutral`, `Opposed`)
- one dominant `Project_Name`

The study used the LLM as a constrained classifier, not as a free-form
summarizer.

## Operational Constraints

- Use only the article `full_text` and basic provided metadata.
- Assign exactly one frame and exactly one stance.
- Use `General` if no single project dominates.
- Use deterministic decoding where supported (`temperature = 0`).
- Return one sentence of reasoning that justifies both the frame and the stance.
- Process the corpus in fixed-size batches rather than the entire file at once.

## Expected Output Schema

The prompt expects a table with this exact column order:

```text
Doc_ID | Date | Outlet | Project_Name | Stance | Frame_ID | Reasoning
```

## Canonical Prompt Text

```text
I have uploaded a CSV containing a media corpus of Indonesian news articles (2013-2024).

Your task is to perform a rigorous framing analysis and stance classification using the codebook below.

ROLE

You are an expert political analyst with extensive experience in systematic content analysis.

TASK

The file is large, so we will work in batches. For each article in the batch, read the `full_text` and assign:

1) exactly ONE dominant narrative frame (F1-F5),

2) exactly ONE stance (Supportive / Neutral / Opposed), and

3) exactly ONE Project_Name (a specific project if clearly dominant; otherwise "General").

CODEBOOK (STRICT)

1) Dominant Narrative Frame (choose ONE)

F1: Economic Pragmatism
- Logic: Investment is framed as a tool for growth, jobs, connectivity, or industrial upgrading.
- Cues: win-win, multiplier effects, competitiveness, job creation, technology transfer.

F2: Sovereignty & Debt
- Logic: Investment is framed as a threat to autonomy, fiscal independence (APBN), or security.
- Cues: debt trap, dictated by China, national security, loss of control, sovereignty.

F3: Social & Identity Friction
- Logic: Focus on tensions around labor, ethnicity, identity politics, or community displacement.
- Cues: TKA/foreign workers, Chinese workers, anti-China sentiment, local vs foreign labor, social resentment.

F4: Governance & Environmental Justice
- Logic: Focus on corruption, weak institutions, lack of transparency, land conflict, or environmental harm.
- Cues: AMDAL, corruption, land conflict, transparency, pollution, Rempang, weak safeguards.

F5: Geopolitics & Alignment
- Logic: Focus on strategic positioning in foreign policy or the regional order.
- Cues: U.S.-China rivalry, ASEAN centrality, bebas aktif, Natuna, Indo-Pacific, hedging.

2) Stance (choose ONE)

- Supportive: The article mainly emphasizes benefits or defends the project.
- Neutral: The article is mainly factual/balanced, or presents both sides with no clear tilt.
- Opposed: The article mainly emphasizes risks, criticism, or failures.

3) Project extraction

Identify the dominant Chinese-linked project name mentioned (e.g., "Whoosh", "Morowali", "Rempang", "Weda Bay").

If no single specific project clearly dominates, output "General".

Do not invent project names.

OUTPUT FORMAT

Return a Markdown table with these columns (exact order):

Doc_ID | Date | Outlet | Project_Name | Stance | Frame_ID | Reasoning

Reasoning must be exactly ONE sentence explaining the key cue(s) that justify BOTH the stance and the frame.

EXECUTION INSTRUCTIONS

Do not process the full file at once.

Start with Rows 1-20 only. Output the Markdown table, then stop and ask whether to continue to the next batch.
```

## Repo Notes

- The final coded output derived from this workflow is mirrored in
  `data/processed/coded_outputs.csv`.
- The prompt uses a reduced in-prompt frame codebook so that the coding logic is
  self-contained at run time.
