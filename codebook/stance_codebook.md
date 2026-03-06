# Stance Codebook

Source: reconstructed from Sections 4.4.3, 4.4.4, and Appendix E of the
submitted thesis appendices.

## Allowed Labels

- `Supportive`
- `Neutral`
- `Opposed`

Assign exactly one stance label per article.

## Definitions

- `Supportive`: the article's overall evaluation is positive toward the
  Chinese-linked project or capital, or it primarily emphasizes benefits,
  defenses, or achievements.
- `Neutral`: the article is mainly descriptive, balanced, process-oriented, or
  explicitly non-committal.
- `Opposed`: the article's overall evaluation is negative, or it primarily
  emphasizes risks, criticism, failures, or harmful consequences.

## Coding Rule

Use the article's dominant evaluative direction rather than isolated phrases. If
an article includes both positive and negative elements, choose the stance that
best reflects the main takeaway.

The LLM workflow required one stance label only, using:

- only the provided `full_text` and basic metadata
- no outside knowledge
- one sentence of reasoning that justifies both the frame and the stance

## Why `Neutral` Is Substantive

`Neutral` is not a residual catch-all category. In this project it is treated as
substantively meaningful because elite economic reporting often defaults to a
descriptive or process-oriented register. Movement away from neutrality is part
of the outcome being explained.

## Boundary Guidance

- `Neutral` versus `Opposed` is a known hard boundary in this thesis.
- Process reporting on delays, negotiations, or administrative hurdles can still
  be `Neutral` if the article remains mainly descriptive.
- Use `Opposed` only when criticism, failure, or risk is clearly foregrounded as
  the article's main evaluative thrust.
- Do not infer stance from background knowledge about a project; use only the
  evaluative content present in the text.

## Output Constraint

The production and validation prompts permit only these exact strings:

```text
Supportive
Neutral
Opposed
```

No other labels, blanks, or qualifiers should be used.
