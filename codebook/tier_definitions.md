# Tier Definitions

Source: reconstructed from Sections 3, 4.4.2, 4.4.3, and Appendix F of the
submitted thesis appendices.

## Narrative Tier as Outcome

Narrative tier is the primary article-level outcome in the thesis. It is
constructed from two coded indicators:

- dominant frame
- stance

Perceived state-ness is coded separately using cue families and is not part of
the tier construction rule itself.

## Tier Definitions

- `Tier 1 (Baseline / Safe Baseline / Diplomatic Register)`: primarily
  descriptive or routine coverage with limited attribution of responsibility and
  limited scrutiny or overt conflict.
- `Tier 2 (Technocratic Scrutiny)`: coverage organized around evaluation of
  public liability or governance, such as costs, debt exposure, procurement,
  oversight, and institutional accountability.
- `Tier 3 (Polarized Contestation)`: coverage organized around salient
  distributional conflict or legitimacy disputes, including social friction,
  protests, identity-linked claims, geopolitical contestation, or moralized
  blame and credit.

## Decision Rule

When dominant frame and stance do not point cleanly to the same tier, assign the
tier using the article's dominant organizing logic:

- headline
- lead
- largest share of evaluative content

Dominant frame is the primary classifier. Stance helps characterize whether the
coverage is neutral, supportive, or polarized within that tier.

## Interpreting the Tiers

- Tier 1 is the default register for ceremonial, descriptive, or routine elite
  reporting.
- Tier 2 captures evaluation centered on governance, liability, and auditable
  accountability.
- Tier 3 captures evaluation centered on conflict, legitimacy, social harm, and
  politicized blame.

## Perceived State-ness Cue Protocol

Perceived state-ness is operationalized using two article-level cue families:

- `State-mediation cues`: whether the article attributes coordination,
  authority, or direction to the Indonesian state.
- `Liability-legibility cues`: whether the article references auditable public
  exposure or accountability chains.

An article is coded as `high perceived state-ness` when both cue families are
present.

## State-Mediation Cues

Articles containing one or more of the following terms or phrases are coded as
containing state-mediation cues.

| Cue category | Keywords/phrases | Notes |
| --- | --- | --- |
| PSN designation | `PSN`, `Proyek Strategis Nasional`, `National Strategic Project`, `strategic project status` | Explicit policy designation |
| Central government authority | `pemerintah pusat`, `central government`, `pemerintah`, `government control`, `kementerian`, `ministry`, `menteri`, `minister`, `BUMN`, `state-owned enterprise`, `perusahaan negara` | Attribution to national-level actors |
| State coordination | `koordinasi pemerintah`, `government coordination`, `Bappenas`, `coordinating ministry`, `kementerian koordinator`, `Kemenko`, `interagency`, `task force pemerintah` | Signals state as orchestrator |
| Presidential or executive involvement | `Presiden`, `President`, `Jokowi`, `Widodo`, `Prabowo`, `Subianto`, `Istana`, `Istana Negara`, `presidential decree`, `Perpres`, `keputusan presiden` | Direct executive ownership |
| State investment or financing | `investasi pemerintah`, `government investment`, `state financing`, `pembiayaan negara`, `modal negara`, `state capital` | State as financial actor |

## Liability-Legibility Cues

Articles containing one or more of the following terms or phrases are coded as
containing liability-legibility cues.

| Cue category | Keywords/phrases | Notes |
| --- | --- | --- |
| Budget or fiscal exposure | `APBN`, `anggaran negara`, `state budget`, `budget negara`, `government guarantee`, `penjaminan pemerintah`, `sovereign guarantee`, `utang negara`, `national debt`, `fiscal burden`, `beban fiskal` | Links to public treasury |
| Parliamentary oversight | `DPR`, `Dewan Perwakilan Rakyat`, `parliament`, `parlemen`, `legislative oversight`, `pengawasan legislatif`, `komisi DPR`, `parliamentary commission`, `hearing DPR` | Legislative accountability chain |
| Procurement and audit | `pengadaan`, `procurement`, `tender`, `lelang`, `audit`, `BPK`, `Badan Pemeriksa Keuangan`, `auditor`, `oversight`, `pengawasan`, `KPK`, `Komisi Pemberantasan Korupsi` | Formal accountability mechanisms |
| Formal agreements and treaties | `perjanjian`, `agreement`, `G-to-G`, `government-to-government`, `bilateral agreement`, `perjanjian bilateral`, `MoU pemerintah`, `state-to-state`, `nota kesepahaman` | State as treaty signatory |
| Public accountability language | `akuntabilitas`, `accountability`, `transparansi`, `transparency`, `tanggung jawab negara`, `state responsibility`, `public interest`, `kepentingan publik` | Explicit responsibility framing |

## Binary Coding Logic

1. `State-Mediation Cues Present` = article contains one or more keywords from
   the state-mediation table.
2. `Liability-Legibility Cues Present` = article contains one or more keywords
   from the liability-legibility table.
3. `High Perceived State-ness` = article contains cues from both families.

Implementation in the thesis used:

- case-insensitive string matching on `full_text`
- Boolean OR logic within each cue family
- Boolean AND logic across cue families for high perceived state-ness

## Limitations

- This is a dictionary-based proxy, not a direct measure of subjective
  journalist perception.
- Cue presence indicates attribution or accountability language appears in the
  article, not that the article endorses state responsibility.
- Some cues may appear inside quoted criticism; they still count as evidence of
  legibility.
- The dictionary includes both Indonesian-language and English-language terms
  because the corpus spans Kompas, Tempo, and The Jakarta Post.

## Cue Selection Justification

The cue dictionary in the thesis was justified using three inputs:

- the theoretical definition of perceived state-ness in the main framework
- interview evidence on how Indonesian elites infer state involvement and
  auditability
- pilot reading of article samples to identify recurring attribution patterns

## Validation Note

Appendix F reports that cue prevalence follows the expected pattern in the focal
comparison:

- Whoosh: higher state-mediation cue prevalence than Morowali
- Whoosh: higher liability-legibility cue prevalence than Morowali
- Whoosh: higher co-occurrence of both cue families, consistent with higher
  perceived state-ness

The appendix reports these specific values:

- state-mediation cues: `72.5%` for Whoosh versus `52.1%` for Morowali
- liability-legibility cues: `77.3%` for Whoosh versus `41.2%` for Morowali
- high perceived state-ness co-occurrence: `61.4%` for Whoosh versus `27.7%`
  for Morowali
