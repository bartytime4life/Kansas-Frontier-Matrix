<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/encyclopedia/chapters/08-cross-domain-systems
title: "Cross-domain systems"
type: planning-reference
version: v1.0
status: draft; repository-grounded; non-authoritative; placement-hold
owners: ["@bartytime4life via CODEOWNERS; domain review remains pending"]
created: 2026-10-08
created_note: Metadata records substantive draft authorship; the existing path predates this edition.
updated: 2026-10-08
policy_label: public; planning-reference
owning_root: docs/
responsibility: "Explain cross-domain systems and route readers to the owning KFM sources."
truth_posture: PROPOSED guidance; repository-grounded draft at ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe; not ADR acceptance, source admission, release or publication.
related:
  - docs/encyclopedia/INDEX.md
  - docs/KFM-encyclopedia.md
[/KFM_META_BLOCK_V2] -->

# Cross-domain systems

Evidence snapshot: `main@ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe`. Draft reference; formal lane acceptance remains pending.

Cross-domain work is strongest when each input retains its original meaning. This chapter describes investigation patterns and the checks needed before combining them.

| Investigation | Inputs kept distinct | Main join risk | Usable output |
|---|---|---|---|
| Watershed change | Gauge observations, watershed geometry, land-cover edition and precipitation | Incompatible periods or extending point values along a network | Source-labeled comparison with aligned windows |
| Groundwater context | Well identity, logged intervals, aquifer boundary and water-level record | Invented continuity or treating depth as elevation | Bounded cross-section with missing coverage visible |
| Environmental events | Radar, lightning, thermal detections, smoke and official alerts | Mixing observation/forecast times or inferring cause | Timeline with each product's role and coverage |
| Settlement history | Census vintage, place names, historic maps and transport records | Back-projecting present boundaries or identities | Edition-specific map comparison with provenance |
| Habitat context | Occurrences, sampling effort, land cover and soil | Treating absence of records as absence of species | Descriptive context with privacy and effort caveats |

## Assembly procedure

1. State the claim and intended audience.
2. Pin each input's source, product, edition, spatial support and time interval.
3. Describe the join key or spatial operation and its tolerance.
4. Account for missing, excluded and unmatched records.
5. Label derived output and retain the contributing sources.
6. Validate the output against the intended claim, including counterexamples.

## Display examples

The [underground workspace](../../../apps/site/source/docs/underground-explorer.md) and [subsurface data notes](../../../apps/site/source/docs/subsurface-data.md) explain recorded observations versus display geometry. The [water-flow path notes](../../../apps/site/source/docs/water-flow-paths.md) describe network display. [History comparison](../../../apps/site/source/docs/history-comparison.md) covers temporal comparison controls.

These are source-specific feature records. Reusing their visual components does not supply missing evidence in another domain. Preserve source labels and the consumer's ability to inspect uncertainty throughout a combined view.

[Chapter index](../INDEX.md) · [Reader guide](01-cover.md)
