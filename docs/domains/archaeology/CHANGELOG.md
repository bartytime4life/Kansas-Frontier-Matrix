<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-domains-archaeology-changelog
title: Archaeology and Cultural Heritage — Changelog
type: standard
version: v1.0.2
status: draft
owners: <archaeology-domain-steward> + <docs-steward> (PLACEHOLDER — confirm)
created: 2026-05-28
updated: 2026-10-11
policy_label: public
owning_root: docs/
responsibility: "Record the versioned history and repository-evidence posture of human-facing Archaeology lane documentation without granting policy, runtime, release, or publication authority."
truth_posture: "Current path, tracked document presence, and listed metadata versions are confirmed at the observed main revision; document content remains draft and independently governed."
related:
  - docs/domains/archaeology/README.md
  - docs/domains/archaeology/ubiquitous-language.md
  - docs/domains/archaeology/source-families.md
  - docs/domains/archaeology/sensitivity-and-publication-posture.md
  - docs/domains/archaeology/pipeline-shape.md
  - docs/domains/archaeology/cross-lane-relations.md
  - docs/domains/archaeology/governed-ai-behavior.md
  - docs/domains/archaeology/verification-backlog.md
  - docs/doctrine/ai-build-operating-contract.md
  - docs/registers/DRIFT_REGISTER.md
tags: [kfm, domains, archaeology, changelog, versioning, lineage]
notes:
  - CONTRACT_VERSION = "3.0.0" pinned; versioning follows operating contract §37 (MAJOR/MINOR/PATCH).
  - Repository history and current document metadata were inspected on 2026-08-28; tracked presence and listed versions are confirmed at the observed main revision.
  - Tracked presence is not review, acceptance, policy activation, release, promotion, or publication evidence.
  - "2026-10-11: RAW placement wording aligned to accepted DIR-SOURCE-001 across thirteen lane docs; physical source-first placement is HOLD and data/raw/archaeology/ is a compatibility/reference lane; documentation only."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# 🏺 Archaeology and Cultural Heritage — Changelog

> The version history of the Archaeology lane documentation, classified by change type under operating contract §37, with no silent edits.

![status](https://img.shields.io/badge/status-draft-orange)
![policy](https://img.shields.io/badge/policy-public_doc-blue)
![versioning](https://img.shields.io/badge/versioning-§37_MAJOR%2FMINOR%2FPATCH-blue)
![contract](https://img.shields.io/badge/CONTRACT__VERSION-3.0.0-informational)
![repo--state](https://img.shields.io/badge/repository_evidence-CONFIRMED-green)

**Status:** `draft` · **Owners:** `<archaeology-domain-steward>` + `<docs-steward>` (PLACEHOLDER) · **Updated:** 2026-10-11

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
> **Truth labels in this doc.** The §37 versioning model is `CONFIRMED` doctrine. Current repository inspection confirms this path, the tracked lane-document paths in §4, and their listed metadata versions. Their content remains `draft`; repository presence does not establish review, acceptance, semantic correctness, policy activation, release, promotion, or publication.

[↑ Back to top](#top)

---

## 2. Repo fit

| Aspect | Value | Status |
|---|---|---|
| Current path | `docs/domains/archaeology/CHANGELOG.md` | `CONFIRMED` at observed main |
| Owning responsibility root | `docs/` (explains something to humans) | `CONFIRMED` rule |
| Scope | Archaeology lane docs only | `CONFIRMED` |
| Versioning authority | `docs/doctrine/ai-build-operating-contract.md` §37 | `CONFIRMED` rule and path |
| Drift counterpart | `docs/registers/DRIFT_REGISTER.md` | `CONFIRMED` path; entry relevance remains case-specific |

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

The documents this changelog tracks, with versions read from their current metadata blocks. `Tracked on main` proves repository presence only; every document remains `draft` until its own governed transition.

| Document | Current version | Repository state |
|---|---|---|
| `README.md` | v2.2.4 | `CONFIRMED` tracked · content `draft` |
| `ubiquitous-language.md` | v1.0.1 | `CONFIRMED` tracked · content `draft` |
| `source-families.md` | v1.0.1 | `CONFIRMED` tracked · content `draft` |
| `sensitivity-and-publication-posture.md` | v1.0.1 | `CONFIRMED` tracked · content `draft` |
| `pipeline-shape.md` | v1 | `CONFIRMED` tracked · content `draft` |
| `cross-lane-relations.md` | v1 | `CONFIRMED` tracked · content `draft` |
| `governed-ai-behavior.md` | v1 | `CONFIRMED` tracked · content `draft` |
| `verification-backlog.md` | v2.1.1 | `CONFIRMED` tracked · content `draft` |
| `CHANGELOG.md` (this file) | v1.0.2 | `PROPOSED` in this change · content `draft` |

[↑ Back to top](#top)

---

## 5. Changelog entries

Entries are newest-first. Each names the document, version delta, §37 type, and reason. KFM casing and terminology are preserved.

### 2026-10-11 — Source-registry path reconciliation — PATCH

Aligned source-registry paths to accepted Directory Rules `DIR-SOURCE-002`–`004` (ADR-0029): `data/registry/sources/archaeology/` is the canonical `SourceDescriptor` writer, and `data/registry/archaeology/sources/` is a read-only compatibility view that must never become an independent writer. Three unmigrated descriptors remain in the compatibility view (`ahgp.yaml`, `khri_archaeology.yaml`, `tribal_consultation_register.yaml`); this entry records them and moves no registry record.

| Document | Version delta | §37 type | Change |
|---|---|---|---|
| `PIPELINE.md` | v1.0.1 → v1.0.2 | PATCH | Scope list, §6 and §17 path trees, verification item, and `related` name the canonical lane; the domain-first parent is labelled compatibility-only. |
| `OBJECT_FAMILIES.md` | v1 → v1.0.1 | PATCH | Out-of-scope list and path tree name the canonical lane; visible dates synced. |
| `SOURCES.md` | v1.0.1 → v1.0.2 | PATCH | Doctrine-surface callout, §11 tree, KHRI open question, verification item, review trigger, and `related` name the canonical lane; the v1 changelog row that adopted the domain-first path is superseded. |
| `SOURCE_REGISTRY.md` | v0.2.1 → v0.2.2 | PATCH | `OQ-ARCH-SR-08` resolved by `DIR-SOURCE-003`/`004`. |
| `RELEASE_INDEX.md` | v2.0.1 → v2.0.2 | PATCH | `SourceDescriptor` supersession row points at the canonical lane. |
| `PUBLICATION_AND_POLICY.md` | v1 → v1.0.1 | PATCH | Same supersession-row fix; visible dates synced. |

### 2026-10-11 — Header sync and ledger evidence correction — PATCH

Follow-up to the RAW placement reconciliation below, from review of that change.

| Document | Version delta | §37 type | Change |
|---|---|---|---|
| `MISSING_OR_PLANNED_FILES.md` | v1.2.1 → v1.2.3 | PATCH | The `data/raw/archaeology/README.md` row moves to `❓ UNKNOWN` / `❓` / `NEEDS VERIFICATION` (tracked on `main` since #5040; v1.2.2 briefly used `🟡 PLANNED`, which wrongly implied it was unimplemented), because this ledger's evidence rules forbid `🟢 PRESENT` without a mounted-repo verification pass. The version badge now matches the metadata. |
| `API_CONTRACTS.md`, `ARCHITECTURE.md`, `CANONICAL_PATHS.md`, `SOURCE_REGISTRY.md`, `README.md` | none (same edition) | PATCH | Visible badges, status rows, and "Last updated" fields now match the metadata-block version and `updated` date from the reconciliation. |

### 2026-10-11 — RAW placement reconciliation (lane-wide) — PATCH / MINOR

Aligned RAW placement wording to accepted Directory Rules `DIR-SOURCE-001`–`004` (`docs/doctrine/directory-rules.md` §12.3): RAW capture identity is source-first under a `source_id` registered once in `data/registry/sources/`; one capture may support several domains without duplicated RAW bytes. Physical source-first RAW placement is **HOLD** (no accepted placement decision), and `data/raw/archaeology/` is a compatibility/reference lane (`data/raw/archaeology/README.md` v0.2.0) that receives no payloads. Connector rules now read "emit only to the accepted source-first RAW home or QUARANTINE; never to processed, catalog, or published." Every deny-by-default, exact-location, sovereignty, cultural-review, and consent rule is preserved unchanged. Documentation only; no payload, path, writer, policy, or release state changed.

| Document | Version delta | §37 type | Change |
|---|---|---|---|
| `CANONICAL_PATHS.md` | v1.1 → v1.2 | MINOR | Normative §3 placement table: `data/raw/` row now CONFIRMED rule / HOLD path; connector row and anti-pattern A7 retargeted; tree, diagram, and no-public-surface WARNING generalized. |
| `API_CONTRACTS.md` | v0.3.1 → v0.3.2 | PATCH | Trust-membrane check covers RAW as source-first capture or the legacy lane. |
| `ARCHITECTURE.md` | v1.2 → v1.2.1 | PATCH | Lane map, path list, and watcher-as-non-publisher callout. |
| `CONTINUITY_INVENTORY.md` | v1.1 → v1.1.2 | PATCH | Watcher row, lifecycle-skip rule, backlog item 14; required metadata added. |
| `DATA_LIFECYCLE.md` | v2.1 → v2.1.1 | PATCH | §2 `Data — raw` row set to HOLD. |
| `EXPANSION_PLAN.md` | v0.3 → v0.3.1 | PATCH | Scaffolding tree and diagram. |
| `FILE_SYSTEM_PLAN.md` | v1.2 → v1.2.1 | PATCH | Lane-map rows 11 and 19, diagram and NOTE, §5.3/§5.4, Appendix A; required metadata added. |
| `MISSING_OR_PLANNED_FILES.md` | v1.2 → v1.2.1 | PATCH | `data/raw/archaeology/README.md` now PRESENT; per-run payload-tree row HOLD (retained); `⏸ HOLD` legend added. |
| `PIPELINE.md` | v1 → v1.0.1 | PATCH | §6 RAW placement uses a HOLD placeholder; §5 anti-pattern generalized; §17 tree; required metadata added. |
| `README.md` | v2.2.3 → v2.2.4 | PATCH | Repo-fit tree and source-first RAW note. |
| `RELEASE_INDEX.md` | v2 → v2.0.1 | PATCH | Diagram node; index-consistency rule 8 generalized. |
| `SOURCES.md` | v1 → v1.0.1 | PATCH | Admission diagram RAW node. |
| `SOURCE_REGISTRY.md` | v0.2 → v0.2.1 | PATCH | Admission-flow connector node. |
| `CHANGELOG.md` (this file) | v1.0.1 → v1.0.2 | PATCH | This entry; inventory version refresh. |

### `CHANGELOG.md` v1 → v1.0.1 — PATCH

| Change | §37 type | Reason |
|---|---|---|
| Replaced the stale repository-unavailable posture with an exact current-main inventory. | status-table refresh (PATCH) | Current Git history and metadata prove the tracked paths and listed versions. |
| Added responsibility metadata and corrected the operating-contract path. | metadata/link repair (PATCH) | Align with current documentation validation without changing authority. |
| Kept every tracked document `draft` and separated presence from review, acceptance, release, and publication. | truth-posture clarification (PATCH) | Prevent repository evidence from being misread as governance approval. |

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
> Current Git history confirms that all v0 → v1 documents listed above are tracked. This resolves repository-presence uncertainty only; their authored claims and `draft` status remain governed independently.

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
| OQ-ARCH-CL-03 | `RESOLVED 2026-08-28`: current Git history settles tracked presence; content acceptance remains outside this changelog. | docs steward | current repository history + per-document metadata |
| OQ-ARCH-CL-04 | Does a merged doc change require a `GENERATED_RECEIPT.json` entry linked from this changelog? | docs steward + governed-ai steward | ADR / contract §34 |

## Definition of done

This changelog is done enough to enter the repository when:

- it is placed according to Directory Rules (`docs/domains/archaeology/`);
- a docs steward and the archaeology domain steward review it;
- it is linked from the lane `README.md` and `docs/domains/README.md`;
- the changelog convention (OQ-ARCH-CL-01) is confirmed or logged in `docs/registers/DRIFT_REGISTER.md`;
- the v0 → v1 entries remain reconciled against current Git history without treating presence as acceptance;
- the `GENERATED_RECEIPT.json` planned in Section 2 (Notes) is wired into CI;
- future changes follow the operating contract's §37 lifecycle.

---

## Related docs

- [`docs/domains/archaeology/README.md`](./README.md) — lane landing page
- [`docs/domains/archaeology/verification-backlog.md`](./verification-backlog.md) — open verification items
- [`docs/domains/archaeology/sensitivity-and-publication-posture.md`](./sensitivity-and-publication-posture.md) — tiers + CARE
- `docs/doctrine/ai-build-operating-contract.md` — §37 versioning, §52 contract changelog (canonical)
- `docs/registers/DRIFT_REGISTER.md` — divergence log (`PROPOSED`)

**Last updated:** 2026-10-11 · `CONTRACT_VERSION = "3.0.0"`

[↑ Back to top](#top)
