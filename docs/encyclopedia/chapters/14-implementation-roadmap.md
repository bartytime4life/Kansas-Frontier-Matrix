<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/encyclopedia/chapters/14-implementation-roadmap
title: "Implementation roadmap"
type: planning-reference
version: v1.0
status: draft; repository-grounded; non-authoritative; placement-hold
owners: ["@bartytime4life via CODEOWNERS; domain review remains pending"]
created: 2026-10-08
created_note: Metadata records substantive draft authorship; the existing path predates this edition.
updated: 2026-10-08
policy_label: public; planning-reference
owning_root: docs/
responsibility: "Explain implementation roadmap and route readers to the owning KFM sources."
truth_posture: PROPOSED guidance; repository-grounded draft at ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe; not ADR acceptance, source admission, release or publication.
related:
  - docs/encyclopedia/INDEX.md
  - docs/KFM-encyclopedia.md
[/KFM_META_BLOCK_V2] -->

# Implementation roadmap

Evidence snapshot: `main@ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe`. Draft reference; formal lane acceptance remains pending.

This roadmap orders work by dependency. It is a proposed execution guide without invented dates, assigned stewards or automatic lifecycle approvals.

| Stage | Concrete deliverable | Exit evidence | What remains separate |
|---|---|---|---|
| 1. Orient | One question, source identity and owning paths | Current source readback and bounded scope | Product suitability and admission |
| 2. Specify | Meaning, shape, units, time and failure states | Reviewed contract/profile and examples | Executable behavior |
| 3. Implement | Small complete behavior in the owning component | Source diff and focused tests | Runtime access and operational acceptance |
| 4. Exercise | Representative valid/invalid/partial cases | Exact-version results and exclusions | Independent human review |
| 5. Review | Candidate and evidence packet | Scoped reviewer disposition | Release/publication decision |
| 6. Deliver | Authorized release or exact saved Site version | Relevant release/deployment evidence | Browser/accessibility acceptance where pending |
| 7. Maintain | Currentness, correction and rollback procedure | Reproducible inventory and recovery evidence | Future source changes |

## First practical increments

For an existing Explorer feature, begin with its source guide and a reproducible interaction. For local data, start with inventory and a bounded transfer plan. For a domain with only schemas or empty tests, implement one meaningful validator slice before claiming readiness.

For the encyclopedia itself, review these draft chapters for accuracy and duplication. Proposed [ADR-0036](../../adr/ADR-0036-planning-encyclopedia-carrier-single-writer-and-scaffold-disposition.md) still owns the unresolved carrier/single-writer decision. A generated assembly requires an accepted relationship and deterministic tooling; the draft chapters do not create either.

## Scheduling and progress

Estimate only after the smallest slice and dependencies are known. Track completed evidence, unresolved decisions and user-visible outcomes instead of counting folders or generated pages. Revisit scope when a provider changes, a dependency is blocked, or the intended audience expands. Record a successor decision when an earlier plan becomes stale rather than silently rewriting its history.

[Chapter index](../INDEX.md) · [Reader guide](01-cover.md)
