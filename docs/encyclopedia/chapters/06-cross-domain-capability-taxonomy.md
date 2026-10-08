<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/encyclopedia/chapters/06-cross-domain-capability-taxonomy
title: "Cross-domain capability taxonomy"
type: planning-reference
version: v1.0
status: draft; repository-grounded; non-authoritative; placement-hold
owners: ["@bartytime4life via CODEOWNERS; domain review remains pending"]
created: 2026-10-08
created_note: Metadata records substantive draft authorship; the existing path predates this edition.
updated: 2026-10-08
policy_label: public; planning-reference
owning_root: docs/
responsibility: "Explain cross-domain capability taxonomy and route readers to the owning KFM sources."
truth_posture: PROPOSED guidance; repository-grounded draft at ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe; not ADR acceptance, source admission, release or publication.
related:
  - docs/encyclopedia/INDEX.md
  - docs/KFM-encyclopedia.md
[/KFM_META_BLOCK_V2] -->

# Cross-domain capability taxonomy

Evidence snapshot: `main@ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe`. Draft reference; formal lane acceptance remains pending.

A capability describes a repeatable operation across domains. It is useful only when its inputs, outputs and limitations are known. Domain-specific contracts still control the meaning of the data.

| Capability | Input | Output | Evidence to inspect |
|---|---|---|---|
| Discover | Question, area and source catalog | Candidate products and declared coverage | Provider/product identity and access requirements |
| Capture | Selected object/date interval and bounded plan | Original bytes plus manifest/receipt | Hashes, size limits and partial-transfer state |
| Normalize | Captured bytes and declared mapping | Derived records with original identifiers | Transformation version, units, CRS and exclusions |
| Validate | Candidate plus contract/schema/profile | Scoped findings | Positive and negative fixtures and actual checker |
| Compare | Compatible units, times and spatial support | Difference or side-by-side result | Baselines, missing data and alignment method |
| Explain | Evidence links and explicit question | Cited interpretation or abstention | Source role, uncertainty and claim traceability |
| Review | Exact candidate and evidence packet | Recorded human disposition | Reviewer scope and candidate identity |
| Release | Accepted candidate and release controls | Versioned released artifact | Release manifest, correction and rollback target |

## Implementation classification

Use separate labels for a documented idea, a schema contract, a deterministic fixture implementation, a source-specific local operator, and a runtime feature. A placeholder module cannot satisfy a capability because it imports successfully. A passing synthetic example cannot establish general source coverage.

The [readiness lanes](../../readiness-lanes.md) and [gap tools](../../../tools/qa/gap_scan.py) help identify the distinction. Their reports are review aids, not a substitute for source admission or operational acceptance.

## Extending a capability

Reuse existing object identities and responsibility roots. Start with one bounded question and one explicit candidate profile. Add both admissible and rejected examples. Define what the consumer sees when data are unavailable, stale, partial or denied. Only then broaden coverage. Record new capability evidence in the owning domain and feature documentation, with this taxonomy serving as a shared vocabulary rather than another implementation registry.

[Chapter index](../INDEX.md) · [Reader guide](01-cover.md)
