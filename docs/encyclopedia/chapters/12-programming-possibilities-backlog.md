<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/encyclopedia/chapters/12-programming-possibilities-backlog
title: "Programming possibilities backlog"
type: planning-reference
version: v1.0
status: draft; repository-grounded; non-authoritative; placement-hold
owners: ["@bartytime4life via CODEOWNERS; domain review remains pending"]
created: 2026-10-08
created_note: Metadata records substantive draft authorship; the existing path predates this edition.
updated: 2026-10-08
policy_label: public; planning-reference
owning_root: docs/
responsibility: "Explain programming possibilities backlog and route readers to the owning KFM sources."
truth_posture: PROPOSED guidance; repository-grounded draft at ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe; not ADR acceptance, source admission, release or publication.
related:
  - docs/encyclopedia/INDEX.md
  - docs/KFM-encyclopedia.md
[/KFM_META_BLOCK_V2] -->

# Programming possibilities backlog

Evidence snapshot: `main@ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe`. Draft reference; formal lane acceptance remains pending.

This is a planning backlog, not a list of committed features. Each item needs a bounded problem, an owning component and evidence of user value before implementation.

| Opportunity | Smallest useful slice | Success evidence | Dependency or risk |
|---|---|---|---|
| Better source discovery | One domain's products filtered by supported area/time | Correct product identity and explicit unavailable cases | Catalog currentness and access terms |
| More repeatable comparisons | One compatible pair of source editions | Deterministic alignment, exclusions and provenance | Incompatible support or dates |
| Clearer local inventory | Explain one capture's bytes, verification and usage | Readback matches receipts and protected state | Confusing cache eviction with original deletion |
| Stronger domain validation | One semantic rule with positive and negative fixtures | Real rejection of the invalid example | Permissive schema or empty test |
| Better partial-result UX | One feature's loading/partial/error transitions | Callback-path regression and browser check | Late response replacing current selection |
| Documentation currentness | One source-backed guide plus link/metadata checks | Reviewable diff and accurate evidence timestamp | Cosmetic date bump without review |

## Definition of a ready backlog item

Describe the user question, owning source path, exact input contract, smallest output, expected failure behavior and acceptance check. Include a representative valid example and at least one counterexample where the feature must abstain, reject or show missing information. Identify the human decision required when rights, sensitivity or release scope changes.

## Prioritization

Prefer work that closes an observed gap in a usable workflow: a missing recovery step, incorrect source label, failed timing interaction or unvalidated boundary. Broad feature matrices and folder counts are weak measures of progress. Use the [implementation roadmap](14-implementation-roadmap.md) for dependency order and the [verification backlog](../../registers/VERIFICATION_BACKLOG.md) for recorded unresolved evidence.

Do not reuse a planning row as a completion receipt. Once implemented, link the actual change, checks and limitations from the owning feature guide and retain the row's original planning role.

[Chapter index](../INDEX.md) · [Reader guide](01-cover.md)
