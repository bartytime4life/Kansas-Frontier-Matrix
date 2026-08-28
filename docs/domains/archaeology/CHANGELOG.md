<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-domains-archaeology-changelog
title: Archaeology and Cultural Heritage — Changelog
type: standard
version: v1
status: draft
owners: <archaeology-domain-steward> + <docs-steward> (PLACEHOLDER — confirm)
created: 2026-05-28
updated: 2026-05-28
policy_label: public
related:
  - docs/domains/archaeology/README.md
  - docs/domains/archaeology/ubiquitous-language.md
  - docs/domains/archaeology/source-families.md
  - docs/domains/archaeology/sensitivity-and-publication-posture.md
  - docs/domains/archaeology/pipeline-shape.md
  - docs/domains/archaeology/cross-lane-relations.md
  - docs/domains/archaeology/governed-ai-behavior.md
  - docs/domains/archaeology/verification-backlog.md
  - ai-build-operating-contract.md
  - docs/registers/DRIFT_REGISTER.md
tags: [kfm, domains, archaeology, changelog, versioning, lineage]
notes:
  - CONTRACT_VERSION = "3.0.0" pinned; versioning follows operating contract §37 (MAJOR/MINOR/PATCH).
  - Entries record draft authoring in this session; "merged" status is PROPOSED until verified against a mounted repo.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# 🏺 Archaeology and Cultural Heritage — Changelog

> The version history of the Archaeology lane documentation, classified by change type under operating contract §37, with no silent edits.

![status](https://img.shields.io/badge/status-draft-orange)
![policy](https://img.shields.io/badge/policy-public_doc-blue)
![versioning](https://img.shields.io/badge/versioning-§37_MAJOR%2FMINOR%2FPATCH-blue)
![contract](https://img.shields.io/badge/CONTRACT__VERSION-3.0.0-informational)
![repo--state](https://img.shields.io/badge/merge_status-PROPOSED-lightgrey)

**Status:** `draft` · **Owners:** `<archaeology-domain-steward>` + `<docs-steward>` (PLACEHOLDER) · **Updated:** 2026-05-28

> [!NOTE]
> This changelog tracks the **Archaeology lane documentation** under `docs/domains/archaeology/`. It does not track the canonical operating contract (see `ai-build-operating-contract.md` §52) or repo-wide doctrine. Each entry records a documentation change classified by the contract's §37 MAJOR / MINOR / PATCH model.

---

## Quick jump

- [1. Scope](#1-scope)
- [2. Repo fit](#2-repo-fit)
- [3. How versions are classified](#3-how-versions-are-classified)
- [4. Lane document inventory](#4-lane-document-inventory)
- [5. Changelog entries](#5-changelog-entries)
- [6. Unreleased / pending](#6-unreleased--pending)
- [7. Supersession and lineage](#7-supersession-and-lineage)
- [8. Open questions register](#open-questions-register)
- [9. Definition of done](#definition-of-done)
- [Related docs](#related-docs)

---

## 1. Scope

This document is the **changelog** for the Archaeology / Cultural Heritage documentation lane. It records, per lane document, what changed, the §37 change type, and why — so that doctrine evolution is auditable and no edit is silent.

> [!IMPORTANT]
> **No silent edits.** Per the corrections-are-first-class posture, a material change to any lane doc is recorded here (or in the doc's own changelog section) and, where it diverges from repo convention, in `docs/registers/DRIFT_REGISTER.md`. A changelog entry is not a substitute for the doc's own version bump or for a `GENERATED_RECEIPT.json` when the change is merged.

> [!NOTE]
> **Truth labels in this doc.** The §37 versioning model is `CONFIRMED` doctrine. The "merged" status of each entry below is `PROPOSED` — these documents were authored as drafts in-session; whether they are committed to a mounted repository is `NEEDS VERIFICATION`. All repo paths are `PROPOSED`.

[↑ Back to top](#top)

---

## 2. Repo fit

| Aspect | Value | Status |
|---|---|---|
| Proposed path | `docs/domains/archaeology/CHANGELOG.md` | `PROPOSED` |
| Owning responsibility root | `docs/` (explains something to humans) | `CONFIRMED` rule |
| Scope | Archaeology lane docs only | `CONFIRMED` |
| Versioning authority | `ai-build-operating-contract.md` §37 | `CONFIRMED` rule / `PROPOSED` presence |
| Drift counterpart | `docs/registers/DRIFT_REGISTER.md` | `PROPOSED` |

**Directory Rules basis.** A doc that *explains to humans* lives under `docs/`; a changelog is human-facing history of the lane it sits in. Per-document version bumps live in each doc's own KFM Meta Block and changelog section; this file aggregates the lane view.

[↑ Back to top](#top)

---

## 3. How versions are classified

`CONFIRMED` doctrine — operating contract §37.1. Each lane document is independently semantically versioned. Change types:

| Type | Trigger | Example in this lane |
|---|---|---|
| **MAJOR** | A change to operating-law-level content, or any change requiring re-issue of existing receipts (e.g., a field rename in an emitted artifact). | Renaming a published `SourceDescriptor` field used in archaeology receipts. |
| **MINOR** | A new section, companion artifact, gate, table, or RFC 2119 clarification; additive content. | Adding the API/governed-AI backlog to `verification-backlog.md`. |
| **PATCH** | Typo fixes, link repair, example clarification, status-table refresh. | Fixing a relative link or a badge date. |

> [!IMPORTANT]
> **ADR triggers (§37.2).** An ADR is required before changes that amend a §1 rule, add/remove a truth label, introduce/retire an object family, change the `GENERATED_RECEIPT` schema, change §23 sensitive-domain defaults, change the separation-of-duties matrix, or bump MAJOR. Several archaeology items wait on ADRs — see the lane `verification-backlog.md` and `README.md` ADR section (ADR-S-04, -05, -09, -11, -12).

> [!NOTE]
> **Drift is not silent (§37.3).** If a lane doc and the mounted repo diverge, the divergence is logged in `docs/registers/DRIFT_REGISTER.md`. **Supersession (§37.5):** a superseded version is preserved as `LINEAGE`, never deleted; this changelog enumerates the delta.

[↑ Back to top](#top)

---

## 4. Lane document inventory

The documents this changelog tracks, with their current version. All `merged` states are `PROPOSED` (no mounted repo).

| Document | Current version | Status |
|---|---|---|
| `README.md` | v2 | `draft` · merge `PROPOSED` |
| `ubiquitous-language.md` | v1 | `draft` · merge `PROPOSED` |
| `source-families.md` | v1 | `draft` · merge `PROPOSED` |
| `sensitivity-and-publication-posture.md` | v1 | `draft` · merge `PROPOSED` |
| `pipeline-shape.md` | v1 | `draft` · merge `PROPOSED` |
| `cross-lane-relations.md` | v1 | `draft` · merge `PROPOSED` |
| `governed-ai-behavior.md` | v1 | `draft` · merge `PROPOSED` |
| `verification-backlog.md` | v2 | `draft` · merge `PROPOSED` |
| `CHANGELOG.md` (this file) | v1 | `draft` · merge `PROPOSED` |

[↑ Back to top](#top)

---

## 5. Changelog entries

Entries are newest-first. Each names the document, version delta, §37 type, and reason. KFM casing and terminology are preserved.

### `verification-backlog.md` v1 → v2 — MINOR

| Change | §37 type | Reason |
|---|---|---|
| Added API / governed-AI / map-surface backlog (VS-ARCH-01…06) | new (MINOR) | §15.J/§15.L/§15.G surfaces were unrepresented. |
| Added source-rights and tier backlog (VR-ARCH-01…03) + §24.5.2 tier rows | gap closure (MINOR) | Settles the prior "§24.5 tier assignments" open item. |
| Added verification-flow Mermaid diagram | clarification (MINOR) | Visualize the NEEDS VERIFICATION → CONFIRMED path. |
| Extended OQ register (OQ-06/07) and ADR table (ADR-S-09) | gap closure (MINOR) | Cover anomaly review and governed-AI adapter. |

> Backward compatibility: all v1 anchors preserved; additive only.

### `README.md` v1 → v2 — MINOR

| Change | §37 type | Reason |
|---|---|---|
| Pinned `CONTRACT_VERSION = "3.0.0"`; added badge/field | clarification (MINOR) | Doctrine-adjacent doc requirement. |
| Reconciled sibling filenames to lowercase-hyphenated; linked siblings | reconciliation (MINOR) | Match the lane's actual sibling docs. |
| Relabeled per-source tiers as `INFERRED` (not §15.D doctrine) | reconciliation (MINOR) | Atlas §15.D assigns no per-family tiers; avoid overclaiming. |
| Marked Flora / People-Land cross-lane rows `INFERRED` (not §15.F) | reconciliation (MINOR) | §15.F has four CONFIRMED rows only. |
| Surfaced Directory Rules path and §15.B↔§15.C naming as open/`CONFLICTED` | reconciliation (MINOR) | Do not smooth over unresolved naming. |
| Added Open questions register, Changelog, Definition of done | gap closure (MINOR) | Doctrine companion sections. |

> Backward compatibility: all v1 heading text preserved; new sections inserted before FAQ/Appendix.

### Lane initial drafts v0 → v1 — MINOR (new documents)

| Document | §37 type | Reason |
|---|---|---|
| `cross-lane-relations.md` | new (MINOR) | Synthesizes Atlas §15.F four-relation table + shared constraint. |
| `governed-ai-behavior.md` | new (MINOR) | Synthesizes Atlas §15.L + §15.J + contract §1.8/§8/§21. |
| `pipeline-shape.md` | new (MINOR) | Synthesizes Atlas §15.H + §24.6.1 master gate reference. |
| `sensitivity-and-publication-posture.md` | new (MINOR) | Synthesizes Atlas §15.I, §15.M, §20.5, §24.6.1–.3, contract §23.2. |
| `source-families.md` | new (MINOR) | Synthesizes Atlas §15.D + §24.1.1–.3 source-role doctrine. |
| `ubiquitous-language.md` | new (MINOR) | Synthesizes Atlas §15.B–C + §15.E identity/temporal rules. |
| `verification-backlog.md` | new (MINOR) | Consolidates Atlas §15.N + §15.K + ADR-S items. |
| `README.md` | new (MINOR) | Lane landing page synthesizing Atlas §15 + §24.5. |
| `CHANGELOG.md` (this file) | new (MINOR) | Establishes the lane changelog. |

> [!NOTE]
> All v0 → v1 entries are **`PROPOSED` as merged**. They record documents authored in-session against the KFM corpus. Whether each is committed to a mounted repository is `NEEDS VERIFICATION`.

[↑ Back to top](#top)

---

## 6. Unreleased / pending

Changes anticipated but not yet authored, gated on verification or ADR resolution:

- **Pending VB/VR resolution** — once the repo is mounted and the §15.N items (steward authority, geometry thresholds, oral-history protocol, disablement drill) are settled, the affected docs move from `draft` toward `published` and a PATCH/MINOR entry is recorded here.
- **Pending ADR-S-05** — ratification of the T0–T4 tier scheme will let `sensitivity-and-publication-posture.md` and `README.md` drop the "defaults PROPOSED" caveat (MINOR, reconciliation).
- **Pending ADR-S-11** — cross-lane join policy ratification will let `cross-lane-relations.md` promote join guidance from PROPOSED to CONFIRMED (MINOR).
- **Pending OQ-ARCH-RM-01** — resolution of the Directory Rules canonical path will update `related` links across the lane (PATCH).
- **Pending filename-convention confirmation (OQ-ARCH-RM-02)** — may rename docs; if so, a MINOR entry plus a `DRIFT_REGISTER.md` note records the anchor/link impact.

[↑ Back to top](#top)

---

## 7. Supersession and lineage

`CONFIRMED` doctrine (contract §37.5). When a lane document supersedes a prior edition:

- the prior edition is preserved as `LINEAGE`, **not deleted**;
- this changelog enumerates the delta (the entries in §5);
- any open compatibility seam is noted in `docs/registers/DRIFT_REGISTER.md`.

| Superseded | Superseded by | Lineage status |
|---|---|---|
| `README.md` v1 | `README.md` v2 | `LINEAGE` — retained in version control history |
| `verification-backlog.md` v1 | `verification-backlog.md` v2 | `LINEAGE` — retained in version control history |

> [!TIP]
> Lineage is reversible by construction: to roll a doc back, restore the prior version from history and record a downgrade entry here. Rollback does not delete the superseding version's history.

[↑ Back to top](#top)

---

## Open questions register

| ID | Question | Owner role | Resolution path |
|---|---|---|---|
| OQ-ARCH-CL-01 | Is there a repo-wide changelog convention (e.g., "Keep a Changelog" format) this lane file must conform to? | docs steward | repo inspection / ADR |
| OQ-ARCH-CL-02 | Should per-document changelog sections be the source of truth, with this file an aggregate view, or vice versa? | docs steward | ADR |
| OQ-ARCH-CL-03 | At what point do the v0 → v1 "PROPOSED as merged" entries become CONFIRMED (i.e., what commit evidence settles them)? | docs steward | repo inspection |
| OQ-ARCH-CL-04 | Does a merged doc change require a `GENERATED_RECEIPT.json` entry linked from this changelog? | docs steward + governed-ai steward | ADR / contract §34 |

## Definition of done

This changelog is done enough to enter the repository when:

- it is placed according to Directory Rules (`docs/domains/archaeology/`);
- a docs steward and the archaeology domain steward review it;
- it is linked from the lane `README.md` and `docs/domains/README.md`;
- the changelog convention (OQ-ARCH-CL-01) is confirmed or logged in `docs/registers/DRIFT_REGISTER.md`;
- the v0 → v1 "PROPOSED as merged" entries are reconciled against actual commit history once the repo is mounted;
- the `GENERATED_RECEIPT.json` planned in Section 2 (Notes) is wired into CI;
- future changes follow the operating contract's §37 lifecycle.

---

## Related docs

- [`docs/domains/archaeology/README.md`](./README.md) — lane landing page
- [`docs/domains/archaeology/verification-backlog.md`](./verification-backlog.md) — open verification items
- [`docs/domains/archaeology/sensitivity-and-publication-posture.md`](./sensitivity-and-publication-posture.md) — tiers + CARE
- `ai-build-operating-contract.md` — §37 versioning, §52 contract changelog (canonical)
- `docs/registers/DRIFT_REGISTER.md` — divergence log (`PROPOSED`)

**Last updated:** 2026-05-28 · `CONTRACT_VERSION = "3.0.0"`

[↑ Back to top](#top)
