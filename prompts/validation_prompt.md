# Validation Prompt

Source: reconstructed from Appendix E of the submitted thesis appendices.

## Purpose

This is the fixed-subset validation prompt used for cross-model replication on a
100-article sample. It is stricter than the production coding prompt because it
forces a machine-readable CSV output and includes an explicit silent self-check.

## Validation Setup

- Validation subset size: `N = 100`
- Fixed random seed reported in the thesis: `20260206`
- Same label space as the main coding workflow
- Same rule: use only the provided text and metadata
- Output must be CSV only, with no explanatory text

## Expected Output Schema

```text
Doc_ID,Date,Outlet,Project_Name,Stance,Frame_ID,Reasoning
```

## Canonical Prompt Text

```text
ROLE
You are an expert political analyst doing systematic content analysis. Follow the codebook and output schema strictly. No extra commentary.

DATA
I will provide up to 100 rows from a CSV corpus of Indonesian news articles (2013-2024). Each row includes: Doc_ID, Date, Outlet, full_text

TASK (FOR EACH ROW)
Assign:

1. Exactly ONE dominant Frame_ID (F1-F5).
2. Exactly ONE Stance (Supportive / Neutral / Opposed).
3. Exactly ONE Project_Name:
   - Use a specific named Chinese-linked project ONLY if it is clearly dominant in the article.
   - If no single specific project dominates, output "General".
   - Do NOT invent names not present in the text.

CODEBOOK (STRICT)
Frames (choose ONE):
F1 Economic Pragmatism: growth/jobs/connectivity/industrial upgrading; "win-win", competitiveness, technology transfer.
F2 Sovereignty & Debt: autonomy/APBN burden, debt trap, national security/sovereignty, loss of control.
F3 Social & Identity Friction: labor/ethnicity/community displacement; TKA/Chinese workers, local vs foreign labor, anti-China sentiment.
F4 Governance & Environmental Justice: corruption, weak safeguards, permits (AMDAL), land conflict, pollution, transparency, worker safety.
F5 Geopolitics & Alignment: foreign policy alignment, US-China rivalry, ASEAN centrality, bebas aktif, Natuna, Indo-Pacific, hedging.

Stance (choose ONE):
Supportive: predominantly emphasizes benefits/defends.
Neutral: mainly factual/balanced or mixed with no clear tilt.
Opposed: predominantly emphasizes risks/criticisms/failures.

DECISION RULES (MANDATORY)

* Use ONLY the provided full_text; no outside knowledge.
* If multiple frames appear, choose the ONE that dominates the article's main thrust.
* If the text is descriptive with no clear evaluation, choose Neutral.
* Reasoning must be exactly ONE sentence and must name the key cue(s) that justify BOTH frame and stance (e.g., "AMDAL permit violations and pollution allegations" or "APBN debt burden concerns" or "US-China rivalry/ASEAN").

OUTPUT FORMAT (STRICT, MACHINE-READABLE)
Return ONLY a CSV block with exactly these columns and this header:

Doc_ID,Date,Outlet,Project_Name,Stance,Frame_ID,Reasoning

Constraints:

* One output row per input row, same order as input.
* No blank cells. If unknown, use "General" for Project_Name and choose the best-fitting Frame_ID and Stance based on text.
* Use ONLY these stance labels: Supportive, Neutral, Opposed.
* Use ONLY these frame labels: F1, F2, F3, F4, F5.
* If Reasoning contains commas, wrap Reasoning in double quotes.
* Do not output Markdown. Do not add explanations before/after the CSV.

VALIDATION SELF-CHECK (SILENT)
Before you output, internally verify:

* Row count in output equals row count in input.
* Every Frame_ID is one of F1-F5 and every Stance is one of the three allowed labels.
* No extra columns, no missing header.

NOW PROCESS THE 100 ROWS ATTACHED IN CSV
```

## Repo Notes

- The resulting validation artifacts are summarized in
  `data/diagnostics/validation_summary.csv`.
- The thesis reports agreement checks across ChatGPT, Claude, and Gemini using
  this fixed-subset validation design.
