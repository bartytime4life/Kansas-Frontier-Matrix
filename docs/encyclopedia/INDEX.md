<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/encyclopedia-scaffold-index
title: KFM Encyclopedia Scaffold Index
type: reference-index
version: v1.0
status: draft; repository-grounded; scaffold-inventory; placement-hold; non-authoritative
owners:
  - "@bartytime4life via the current CODEOWNERS review route"
created: 2026-05-15
updated: 2026-08-14
policy_label: public; planning-reference; no-sensitive-detail
owning_root: docs/
responsibility: >-
  Inventory the tracked encyclopedia scaffold, identify the current planning and
  doctrine surfaces, preserve chapter order and status, and prevent placeholder or
  generated targets from being mistaken for canonical content.
placement_outcome: HOLD
related:
  - README.md
  - CHANGELOG.md
  - encyclopedia.md
  - ../KFM-encyclopedia.md
  - ../doctrine/encyclopedia.md
  - ../adr/ADR-0036-planning-encyclopedia-carrier-single-writer-and-scaffold-disposition.md
  - ../doctrine/directory-rules.md
  - ../adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, encyclopedia, index, scaffold, planning, hold]
notes:
  - "This index is an inventory and navigation surface. It grants no lane admission, chapter authority, generation authority, release, or publication."
  - "ADR-0036 is proposed. Until explicitly accepted, the chapter files and encyclopedia.md remain non-substantive scaffolds."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KFM Encyclopedia Scaffold Index

> **Purpose.** Inventory the current `docs/encyclopedia/` scaffold and route readers to the strongest available source without turning placeholder paths into authority.

[![placement](https://img.shields.io/badge/placement-HOLD-b42318?style=flat-square)](./README.md#repo-fit)
[![ADR](https://img.shields.io/badge/ADR--0036-proposed-d4a72c?style=flat-square)](../adr/ADR-0036-planning-encyclopedia-carrier-single-writer-and-scaffold-disposition.md)
[![chapters](https://img.shields.io/badge/structural%20chapters-16-0969da?style=flat-square)](#ordered-structural-spine)
[![publication](https://img.shields.io/badge/publication-none-6e7781?style=flat-square)](#authority-boundary)

> [!IMPORTANT]
> The current planning orientation is [`docs/KFM-encyclopedia.md`](../KFM-encyclopedia.md). The doctrine-vocabulary surface is [`docs/doctrine/encyclopedia.md`](../doctrine/encyclopedia.md). The files indexed below are scaffolds until a reviewed decision and implementation packet establish a single writer.

## Authority boundary

This index may record paths, status, order, lineage, and review needs. It does not:

- accept ADR-0036;
- make a placeholder substantive;
- authorize chapter population or source-PDF placement;
- define doctrine, contracts, schemas, policy, source authority, evidence, release, or publication;
- select a generator or validate a generated assembly;
- authorize a move, rename, deletion, or compatibility retirement.

## Current surfaces

| Surface | Current role | Status |
|---|---|---|
| [`README.md`](./README.md) | Lane boundary, evidence snapshot, contributor contract, and placement hold | Repository-grounded draft |
| [`INDEX.md`](./INDEX.md) | This scaffold inventory and navigation surface | Repository-grounded draft |
| [`CHANGELOG.md`](./CHANGELOG.md) | Scaffold, decision, migration, and future edition history | Repository-grounded draft |
| [`encyclopedia.md`](./encyclopedia.md) | Reserved assembly target; no manuscript body established | Placeholder / HOLD |
| [`chapters/`](./chapters/) | Sixteen structural placeholders plus one extra domain scaffold | Placeholder / HOLD |
| [`assets/`](./assets/) | Empty conditional encyclopedia-only asset lane | Inactive |
| [`lineage/`](./lineage/) | Empty conditional source/edition lineage lane | Inactive |
| [`../KFM-encyclopedia.md`](../KFM-encyclopedia.md) | Current repository-grounded planning index and source-manuscript crosswalk | Draft planning reference |
| [`../doctrine/encyclopedia.md`](../doctrine/encyclopedia.md) | Separate doctrine-vocabulary surface | Draft doctrine surface |

## Ordered structural spine

The source manuscript uses a sixteen-section structure. These paths preserve that order, but they do not yet contain the manuscript.

| Order | File | Source-manuscript section | Current status |
|---:|---|---|---|
| 01 | [`01-cover.md`](./chapters/01-cover.md) | Cover Page | Generic placeholder |
| 02 | [`02-executive-summary.md`](./chapters/02-executive-summary.md) | Executive Summary | Generic placeholder |
| 03 | [`03-source-ledger.md`](./chapters/03-source-ledger.md) | Source Ledger and Evidence Method | Generic placeholder |
| 04 | [`04-operating-law.md`](./chapters/04-operating-law.md) | KFM Operating Law | Generic placeholder |
| 05 | [`05-master-domain-atlas.md`](./chapters/05-master-domain-atlas.md) | Master Domain Atlas | Generic placeholder |
| 06 | [`06-cross-domain-capability-taxonomy.md`](./chapters/06-cross-domain-capability-taxonomy.md) | Cross-Domain Capability Taxonomy | Generic placeholder |
| 07 | [`07-domain-chapters.md`](./chapters/07-domain-chapters.md) | Domain Chapters | Generic placeholder |
| 08 | [`08-cross-domain-systems.md`](./chapters/08-cross-domain-systems.md) | Cross-Domain Systems Chapters | Generic placeholder |
| 09 | [`09-master-feature-matrix.md`](./chapters/09-master-feature-matrix.md) | Master Feature Matrix | Generic placeholder |
| 10 | [`10-master-action-matrix.md`](./chapters/10-master-action-matrix.md) | Master Action Matrix | Generic placeholder |
| 11 | [`11-master-viewing-mode-atlas.md`](./chapters/11-master-viewing-mode-atlas.md) | Master Viewing Mode Atlas | Generic placeholder |
| 12 | [`12-programming-possibilities-backlog.md`](./chapters/12-programming-possibilities-backlog.md) | Programming Possibilities Backlog | Generic placeholder |
| 13 | [`13-sensitive-deny-by-default-register.md`](./chapters/13-sensitive-deny-by-default-register.md) | Sensitive / Deny-by-Default Register | Generic placeholder |
| 14 | [`14-implementation-roadmap.md`](./chapters/14-implementation-roadmap.md) | Implementation Roadmap | Generic placeholder |
| 15 | [`15-validation-and-acceptance-plan.md`](./chapters/15-validation-and-acceptance-plan.md) | Validation and Acceptance Plan | Generic placeholder |
| 16 | [`16-appendices.md`](./chapters/16-appendices.md) | Appendices and Self-Check | Generic placeholder |

## Extra scaffold outside the ordered spine

| File | Current classification | Required disposition |
|---|---|---|
| [`11-settlements-infrastructure.md`](./chapters/11-settlements-infrastructure.md) | Bounded scaffold sourced from a domain expansion backlog; duplicate `11-` ordinal | Inventory links and unique content; compare with `docs/domains/settlements-infrastructure/`; migrate or retire only through a reviewed compatibility change |

## Proposed single-writer model

Proposed [`ADR-0036`](../adr/ADR-0036-planning-encyclopedia-carrier-single-writer-and-scaffold-disposition.md) selects:

- the ordered `chapters/` set as the writable manuscript source;
- `encyclopedia.md` as a deterministic generated assembly;
- `docs/KFM-encyclopedia.md` as a temporary compatibility index;
- `docs/doctrine/encyclopedia.md` as a separate doctrine-vocabulary surface.

That model is not binding until the ADR is accepted.

## Contributor rules while on HOLD

- Do not populate the structural chapters as a broad campaign.
- Do not hand-edit `encyclopedia.md` into a competing manuscript.
- Do not copy the source PDF into the repository.
- Do not renumber or delete the duplicate `11-` scaffold.
- Do not treat a chapter or matrix as doctrine, implementation proof, or publication.
- Link to current authority and preserve truth labels.
- Record material changes in [`CHANGELOG.md`](./CHANGELOG.md).

## Validation

For a documentation-only change in this lane, use the smallest applicable repository-native set covering:

- metadata;
- Markdown structure;
- relative links, path case, and fragments;
- stable anchors and inbound links;
- document graph and staleness;
- duplicate chapter ordinals;
- sensitive-content and secret scans;
- generated parity after generation tooling exists.

A green check does not accept the lane, prove manuscript completeness, or publish KFM content.

## Open decisions

- Explicit acceptance or rejection of ADR-0036.
- Source PDF repository-carrier and rights posture.
- Generator and generation-manifest shape.
- Domain-review assignment.
- Compatibility window for `docs/KFM-encyclopedia.md`.
- Disposition of the extra settlements/infrastructure scaffold.
- Activation or retirement of `assets/` and `lineage/`.

[Back to top](#top)
