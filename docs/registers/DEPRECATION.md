<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/registers/deprecation
title: KFM Deprecation Register — Doctrine and Reading Guide
type: standard
version: v1-draft
status: draft
owners: <docs-steward> + <release-authority>   # placeholders — see §11
created: 2026-05-12
updated: 2026-05-12
policy_label: public
related:
  - docs/doctrine/directory-rules.md
  - docs/registers/AUTHORITY_LADDER.md
  - docs/registers/CANONICAL_LINEAGE_EXPLORATORY.md
  - docs/registers/DRIFT_REGISTER.md
  - docs/registers/VERIFICATION_BACKLOG.md
  - docs/archive/deprecated/
  - docs/adr/ADR-0001-schema-home.md
  - control_plane/deprecation_register.yaml
tags: [kfm, governance, registers, deprecation, supersession, migration]
notes:
  - Human-facing explainer for the deprecation register; control_plane/deprecation_register.yaml is the machine-readable register.
  - Path is PROPOSED — Directory Rules §6.1 enumerates docs/registers/ contents but does not explicitly list a DEPRECATION explainer.
  - Owners, dates, and concrete register IDs are placeholders pending repo evidence.
[/KFM_META_BLOCK_V2] -->

# 🗂️ KFM Deprecation Register — Doctrine and Reading Guide

> The human-facing explainer for how Kansas Frontier Matrix retires, supersedes, and sunsets repo paths, schemas, policies, sources, releases, and doctrinal artifacts — paired with the machine-readable register at `control_plane/deprecation_register.yaml`.

![status](https://img.shields.io/badge/status-draft-orange)
![doctype](https://img.shields.io/badge/doctype-register--explainer-blue)
![authority](https://img.shields.io/badge/authority-docs%2Fregisters-purple)
![pair](https://img.shields.io/badge/pair-control__plane%2Fdeprecation__register.yaml-lightgrey)
![policy](https://img.shields.io/badge/policy_label-public-green)
![lifecycle](https://img.shields.io/badge/lifecycle-PROPOSED-yellow)

| Status | Authority level | Owners | Last reviewed |
|---|---|---|---|
| **draft** · PROPOSED | Canonical (under `docs/`) | `<docs-steward>` + `<release-authority>` *(placeholders — §11)* | `2026-05-12` |

---

## Quick jump

- [§1 Purpose](#1-purpose)
- [§2 Authority and the docs ↔ control_plane split](#2-authority-and-the-docs--control_plane-split)
- [§3 What counts as a deprecation entry](#3-what-counts-as-a-deprecation-entry)
- [§4 Entry lifecycle](#4-entry-lifecycle)
- [§5 Register entry shape](#5-register-entry-shape)
- [§6 Triggers — when an entry MUST be opened](#6-triggers--when-an-entry-must-be-opened)
- [§7 Relationship to other registers and artifacts](#7-relationship-to-other-registers-and-artifacts)
- [§8 Deprecation vs adjacent mechanisms](#8-deprecation-vs-adjacent-mechanisms)
- [§9 Reviewer checklist](#9-reviewer-checklist)
- [§10 Anti-patterns](#10-anti-patterns)
- [§11 Open questions and NEEDS VERIFICATION](#11-open-questions-and-needs-verification)
- [§12 Related docs](#12-related-docs)
- [§13 Appendix — worked example and reference tables](#13-appendix--worked-example-and-reference-tables)

---

## 1. Purpose

The KFM Deprecation Register is the project's authoritative record of items that are scheduled for retirement, superseded by newer authority, or held in a compatibility window until a migration completes. It exists so that:

- A reader can answer *"is this path / schema / policy / source / release still authoritative?"* without spelunking through git history.
- Migrations and supersessions are visible *before* they break downstream consumers.
- Removal is a governed, reversible event with a rollback target — not a silent delete.
- Tombstones, correction notices, ADRs, and rollback cards remain discoverable from a single index.

**Two surfaces, one doctrine.** This document is the **human-facing explainer** under `docs/`. The **machine-readable register** lives at `control_plane/deprecation_register.yaml` (CONFIRMED in Directory Rules §6.2). Together they implement the §6.1 governance split: *`docs/` explains; `control_plane/` indexes.*

> [!IMPORTANT]
> A `docs/` page is never the source of canonical decision. Deprecation decisions are recorded in `control_plane/deprecation_register.yaml` and, where the change crosses an authority threshold, in an ADR under `docs/adr/`. This document **explains how to read and use** the register; it does not replace it.

---

## 2. Authority and the docs ↔ control_plane split

Per Directory Rules §6.1, the governance function is layered:

| Layer | Role | Lives in | Authority class |
|---|---|---|---|
| **Doctrine / explainer** | What deprecation *means*; how to use the register | `docs/registers/DEPRECATION.md` *(this file — PROPOSED path)* | Canonical (human-facing) |
| **Operational index** | Machine-readable register of entries, sunset dates, links | `control_plane/deprecation_register.yaml` *(CONFIRMED doctrine)* | Canonical (machine-readable) |
| **Object meaning** | What a deprecated object family means | `contracts/` | Canonical |
| **Shape validation** | Whether a register entry validates | `schemas/contracts/v1/...` *(per ADR-0001; specific sub-path PROPOSED)* | Canonical |

> [!NOTE]
> Directory Rules §6.1 explicitly enumerates the contents of `docs/registers/` as `AUTHORITY_LADDER`, `CANONICAL_LINEAGE_EXPLORATORY`, `DRIFT_REGISTER`, `VERIFICATION_BACKLOG`, and `OBJECT_FAMILY_MAP`. A `DEPRECATION.md` explainer is **not** explicitly listed and is therefore **PROPOSED**. It is doctrinally consistent with §6.1's "docs/ explains; control_plane/ indexes" split and pairs with the CONFIRMED `control_plane/deprecation_register.yaml`. A one-line addition to the §6.1 enumeration via routine PR (Directory Rules §17) is recommended before this doc is treated as canonical.

### 2.1 Where deprecated *content* lives

`docs/archive/deprecated/` is the human-facing archive for retired documentation per Directory Rules §6.1. The **register** tracks the *decision and its lifecycle*; the **archive** holds the *content*. They are linked from each register entry that retires documentation.

For non-doc content, the lifecycle landing zones are governed by the responsibility root:

- A deprecated **schema** is migrated per ADR-0001; the old version is retained under its prior versioned home with a `superseded_by` link in the schema header (Atlas §24.8.2).
- A deprecated **policy** is replaced via accepted ADR; the old bundle is retained with a supersession link.
- A deprecated **release** has a `RollbackCard` under `release/rollback_cards/` and a superseding `ReleaseManifest` under `release/manifests/`.
- A deprecated **source** retains its prior `SourceDescriptor` with `superseded_by` per the source register.

[Back to top](#-kfm-deprecation-register--doctrine-and-reading-guide)

---

## 3. What counts as a deprecation entry

A deprecation entry records the **planned or in-progress retirement** of a governed artifact. The taxonomy aligns with the canonical roots and with the supersession lineage rules of Atlas §24.8.2.

| Item class | Examples | Supersession artifact required |
|---|---|---|
| **Path / directory** | Retired root, renamed lane, moved package | Migration manifest under `migrations/` + ADR if structural (§14.2) |
| **Schema** | Object-family schema replaced by new version | ADR (per ADR-0001) + supersession link in schema header |
| **Policy** | Rego bundle replaced or removed | ADR + supersession link |
| **SourceDescriptor** | Source retired or superseded by newer descriptor | `superseded_by` link in source register |
| **EvidenceBundle** | Corrected; old bundle retained for audit | New `EvidenceBundle` + `CorrectionNotice` + supersession link |
| **GeographyVersion** | Replaced; both versions retained for time-bound claims | Version register entry + crosswalk |
| **ReleaseManifest** | Superseded by next release | Manifest history + valid rollback chain |
| **Atlas / doctrinal supplement** | Edition replaced (e.g., Atlas v1.0 → v1.1) | ADR + lineage appendix |
| **Connector / pipeline** | Source family abandoned or replaced | ADR + migration plan |
| **Compatibility root** | A `legacy`, `mirror`, or `transitional` root reaching end-of-life | Per §8 with declared class |

> [!NOTE]
> Not every removal is a deprecation. Routine refactors that do not change object meaning are tracked by the migration manifest alone (Directory Rules §14.1). Deprecation enters the picture when a downstream consumer might still depend on the old path, identity, or behavior — i.e., when a mirror or sunset window is needed.

### 3.1 What the register does NOT track

- One-line text edits with no behavioral change.
- Internal helpers that were never part of a published surface.
- `scripts/one_off/` artifacts (those are ephemeral per Directory Rules §7.5).
- Per-item runtime revocations of *already-published* content — those are **tombstone receipts** in the audit ledger (C5-09 / C6-08), not register entries. See §8.

---

## 4. Entry lifecycle

Every deprecation entry moves through a small, governed lifecycle. Compatibility-class transitions follow Directory Rules §8 (`legacy` / `mirror` / `deprecated` / `external-export` / `transitional`).

```mermaid
flowchart LR
    A([Proposed]) --> B([Active])
    B --> C([Mirrored])
    C --> D([Sunset])
    D --> E([Retired])
    E -.archive only.-> F([Archived])
    B -.rollback.-> A
    C -.rollback.-> B
    D -.rollback.-> C

    classDef plan fill:#fff7e0,stroke:#b58900,color:#222
    classDef live fill:#e8f4ff,stroke:#268bd2,color:#222
    classDef end1 fill:#f0f0f0,stroke:#586e75,color:#222
    class A,B plan
    class C,D live
    class E,F end1
```

State definitions (PROPOSED — labels align with Directory Rules §8 compatibility classes where applicable):

- **Proposed.** Entry opened; ADR (if required by §14.2) in draft; migration target identified; no consumer impact yet.
- **Active.** ADR accepted (if applicable); migration manifest filed under `migrations/data/` or `migrations/schema/`; old path or object class declared `legacy` or `transitional` per §8.
- **Mirrored.** Old path still resolves via a generated `mirror` per §8.3; canonical authority has moved; new files MUST land in the new home; mirror does not evolve independently.
- **Sunset.** Mirror frozen; downstream consumers warned; explicit sunset date set in the register; rollback card verified by dry-run.
- **Retired.** Mirror removed; content moved to `docs/archive/deprecated/` (if doc) or governed archive (if non-doc); register entry preserved as lineage; entry `id` never reused.

A `RollbackCard` under `release/rollback_cards/` MUST exist before the **Active → Mirrored** transition (Directory Rules §14.2 step 6). Each transition is a PR-reviewable change to `control_plane/deprecation_register.yaml`.

[Back to top](#-kfm-deprecation-register--doctrine-and-reading-guide)

---

## 5. Register entry shape

**PROPOSED.** Directory Rules §14.2 step 5 requires adding "a deprecation entry in `control_plane/deprecation_register.yaml` with sunset date." The detailed schema is not pinned in current evidence; the structure below is **illustrative** and SHOULD be confirmed by an ADR before tooling depends on it.

```yaml
# control_plane/deprecation_register.yaml — illustrative (PROPOSED)
version: 1
entries:
  - id: dep-2026-001
    title: "Retire jsonschema/ mirror in favor of schemas/contracts/v1/"
    item_class: schema-mirror            # see §3 taxonomy
    old:
      path: jsonschema/
      identity: "compatibility mirror of schemas/contracts/v1/"
    new:
      path: schemas/contracts/v1/
      identity: "canonical schema home per ADR-0001"
    compatibility_class: mirror          # legacy | mirror | deprecated | external-export | transitional
    lifecycle_state: active              # proposed | active | mirrored | sunset | retired
    adr: docs/adr/ADR-0001-schema-home.md
    migration_manifest: migrations/schema/ADR-0001-schema-home/manifest.yaml
    rollback_card: release/rollback_cards/<release_id>.yaml
    correction_notices: []
    sunset:
      announce_date: "YYYY-MM-DD"        # placeholder — see §11
      sunset_date:   "YYYY-MM-DD"        # placeholder — see §11
    superseded_by: schemas/contracts/v1/
    reason: "Drift between jsonschema/ and schemas/contracts/v1/ creates parallel authority."
    downstream_consumers: []
    review:
      opened_by: "<docs-steward>"
      reviewed_by: []
      last_reviewed: "YYYY-MM-DD"
    notes: |
      Illustrative shape only. Replace placeholders before commit.
```

> [!WARNING]
> The YAML schema above is **PROPOSED**. Tooling, CI, and downstream consumers MUST NOT depend on these field names until the schema is registered under the governance lane of `schemas/contracts/v1/...` (per ADR-0001) and an ADR records the decision.

### 5.1 Required vs optional fields (PROPOSED)

| Field | Required | Notes |
|---|---|---|
| `id` | required | Stable; never reused after retirement. Format PROPOSED (`dep-YYYY-NNN` vs content-addressed). |
| `title` | required | Human-readable summary. |
| `item_class` | required | Aligns with §3 taxonomy. |
| `old.path` *or* `old.identity` | at least one | Must be unambiguous. |
| `compatibility_class` | required | One of the §8 classes. |
| `lifecycle_state` | required | One of the §4 states. |
| `adr` | required for structural moves | Per Directory Rules §2.4 / §14.2. |
| `migration_manifest` | required if a path moved | Per §14.2 step 3. |
| `rollback_card` | required before `mirrored` | Per §14.2 step 6. |
| `sunset.sunset_date` | required by `mirrored` | The §14.2 step 5 obligation. |
| `superseded_by` | recommended | Resolves the supersession link of Atlas §24.8.2. |
| `correction_notices` | required if released claims affected | Atlas §24.8.2; §8 of this doc. |

---

## 6. Triggers — when an entry MUST be opened

A deprecation entry **MUST** (not *should*) be opened when any of the following occurs. Triggers are drawn from Directory Rules §14 and Atlas §24.8.2.

| # | Trigger | Source rule |
|---|---|---|
| T1 | Structural move per Directory Rules §14.2 (changing a root, splitting a phase, schema-home migration) | DIRRULES §14.2 step 5 |
| T2 | A compatibility root is reclassified to `legacy` or `deprecated` | DIRRULES §8 |
| T3 | A schema under `schemas/contracts/v1/...` is replaced via ADR | Atlas §24.8.2 + ADR-0001 |
| T4 | A policy bundle is superseded via ADR | Atlas §24.8.2 |
| T5 | A `SourceDescriptor` is replaced or retired | Atlas §24.8.2 |
| T6 | An Atlas edition or doctrinal supplement is superseded | Atlas §24.8.2 (Atlas v1.0 → v1.1 precedent, Appendix G) |
| T7 | A public route, connector, or governed-API surface is sunset | DIRRULES §7.1, §7.3 |
| T8 | A `ReleaseManifest` retires a prior published surface that downstream consumers may still resolve | Atlas §24.8.2 |
| T9 | A rename that changes object identity occurs | DIRRULES §14.3 — requires ADR + schema bump + correction notices |

Failure to open an entry when triggered SHOULD be filed to `docs/registers/DRIFT_REGISTER.md` per Directory Rules §2.5 and resolved via ADR or correction notice.

[Back to top](#-kfm-deprecation-register--doctrine-and-reading-guide)

---

## 7. Relationship to other registers and artifacts

The deprecation register sits in a network of governance artifacts; an entry typically references several of them.

| Artifact | Role | Relationship to a deprecation entry |
|---|---|---|
| `docs/registers/AUTHORITY_LADDER.md` | Authority ordering | Determines whose authority a deprecation entry can supersede. |
| `docs/registers/DRIFT_REGISTER.md` | Doctrine / code / path drift | Missed or late deprecations are filed here. |
| `docs/registers/VERIFICATION_BACKLOG.md` | Unresolved checks | Entries in `proposed` lifecycle state appear here until verified. |
| `docs/registers/CANONICAL_LINEAGE_EXPLORATORY.md` | Lineage classifier | Records the prior canonical identity that a deprecation supersedes. |
| `docs/archive/deprecated/` | Doc archive | Holds the retired documentation referenced by `retired` entries. |
| `migrations/data/`, `migrations/schema/` | Migration manifests | Old → new mappings with `git_sha_before` / `git_sha_after`. |
| `release/manifests/` | Release decisions | The superseding `ReleaseManifest` cited by an entry. |
| `release/rollback_cards/` | Rollback decisions | Required before `mirrored`. |
| `release/correction_notices/` | Public correction record | Emitted when a deprecation affects released claims. |
| `docs/adr/` | Architecture decisions | Required for structural deprecations (§14.2). |
| Audit ledger (tombstones, C5-09) | Runtime revocation | Tombstones revoke specific published items; the register tracks the upstream change. |

---

## 8. Deprecation vs adjacent mechanisms

KFM uses several overlapping mechanisms for "this thing is no longer authoritative." They are deliberately distinct and they do different jobs.

| Mechanism | What it does | When to use it | Lives in |
|---|---|---|---|
| **Deprecation entry** | Plans and tracks retirement of a path, schema, source, release, or doc | An artifact WILL be retired and consumers need a sunset window | `control_plane/deprecation_register.yaml` |
| **Supersession link** | Names the replacement for a retained-but-not-authoritative object | Old object is retained for audit; new one is canonical | Schema header / source register / Atlas appendix |
| **CorrectionNotice** | Records a defect in a *released* claim | Already-public content was wrong or needs withdrawal | `release/correction_notices/` |
| **RollbackCard** | Reverses a release to a prior safe state | A release must be rolled back | `release/rollback_cards/` |
| **Tombstone receipt** (C5-09) | Runtime revocation of a specific published item | A public item must be retracted at render time | Audit ledger |
| **Stale marker** (Atlas §24.8.1) | Marks a still-published claim as aged past tolerance | Evidence / source / policy / schema / geography / model / review / rights version has drifted | UI badge + claim metadata |

> [!TIP]
> Atlas §24.8.1 separates **stale** from **wrong**. A `CorrectionNotice` is for **wrong** content. A stale marker is for **aged** content. A deprecation is for **retired** content (with consumers still depending on the old form). A tombstone is for **revoked** content. Don't substitute one for another — they have different audiences and different SLAs.

[Back to top](#-kfm-deprecation-register--doctrine-and-reading-guide)

---

## 9. Reviewer checklist

When reviewing a PR that opens, advances, or closes a deprecation register entry:

- [ ] **Entry has a stable `id`** that has not been used before and will not be reused after retirement.
- [ ] **`item_class` matches §3 taxonomy.**
- [ ] **`compatibility_class` is one of the §8 classes** (`legacy`, `mirror`, `deprecated`, `external-export`, `transitional`).
- [ ] **`lifecycle_state` transition is valid per §4** (no skipping `mirrored` when downstream consumers exist).
- [ ] **ADR cited** when triggered by §14.2 / §2.4 / §14.3.
- [ ] **Migration manifest cited** if a path moved.
- [ ] **RollbackCard cited and dry-run verified** before any transition to `mirrored`.
- [ ] **Sunset date set** before transition to `mirrored`.
- [ ] **`superseded_by` resolves** to a current authority.
- [ ] **Downstream consumers identified** or explicitly declared `none`.
- [ ] **CorrectionNotice emitted** if released claims referenced the old identity.
- [ ] **Doc archive updated** if a doc is being retired (`docs/archive/deprecated/`).
- [ ] **Drift register entry closed** if this entry resolves a previously filed drift item.
- [ ] **§14.3 obligations met** if the change alters object identity (schema bump + correction notices + old-fixture parity tests).

A reviewer who cannot tick every applicable box SHOULD request changes or open a `docs/registers/DRIFT_REGISTER.md` entry.

---

## 10. Anti-patterns

| Anti-pattern | Symptom | Fix |
|---|---|---|
| **Silent rename** | Path renamed; no register entry; mirrors not declared | Open entry; declare `mirror` per §8.3; file migration manifest. |
| **Sunset without rollback** | Mirror frozen; no `RollbackCard` recorded | Add and dry-run a rollback card before the sunset transition. |
| **Hard delete** | Old path removed in the same PR that introduces the new one | Revert; reintroduce as `mirror`; sunset on schedule. |
| **Doc-as-decision** | Deprecation announced only in a `docs/` page | Promote to `control_plane/deprecation_register.yaml`; ADR if structural. |
| **Parallel authority kept alive** | Old and new homes evolve independently past sunset | Per §8.3, mirror MUST regenerate from canonical; freeze writes to the mirror. |
| **Identity-changing rename without ADR** | A rename changes object meaning, treated as routine move | Per §14.3, requires ADR + schema bump + correction notices + old-fixture parity tests. |
| **Tombstone-as-deprecation** | One published item tombstoned, but the upstream path/schema retired without a register entry | Tombstone the item *and* open a deprecation entry for the upstream change. |
| **Deprecation-as-correction** | Wrong content marked deprecated instead of corrected | Emit `CorrectionNotice`; deprecation is for retirement, not for wrongness. |
| **ID reuse** | A retired entry's `id` is reassigned to a new entry | IDs are preserved as lineage; mint a new one. |
| **Stale-as-deprecated** | Aged-but-still-current content marked deprecated | Use stale markers (Atlas §24.8.1) and refresh, supersede, or downgrade as appropriate. |

---

## 11. Open questions and NEEDS VERIFICATION

These items are explicitly **not** resolved by this document and SHOULD be tracked in `docs/registers/VERIFICATION_BACKLOG.md`:

- **NEEDS VERIFICATION:** Whether this file (`docs/registers/DEPRECATION.md`) currently exists in the mounted repo. Path is **PROPOSED** because Directory Rules §6.1 enumerates `docs/registers/` as `AUTHORITY_LADDER`, `CANONICAL_LINEAGE_EXPLORATORY`, `DRIFT_REGISTER`, `VERIFICATION_BACKLOG`, `OBJECT_FAMILY_MAP` — and does *not* explicitly list a DEPRECATION explainer. A routine PR per §17 can extend the §6.1 enumeration.
- **NEEDS VERIFICATION:** Whether `control_plane/deprecation_register.yaml` currently exists in the mounted repo. Its presence is CONFIRMED in §6.2 doctrine; current file existence is **UNKNOWN** without repo inspection.
- **NEEDS VERIFICATION:** The canonical schema for `control_plane/deprecation_register.yaml`. The shape in §5 is **PROPOSED**.
- **OPEN (ADR-S-13):** Drift register triage cadence — affects how missed-deprecation drift is reviewed.
- **OPEN (ADR-S-15):** Atlas / supplement deprecation rule, supersession path, and revision cadence. Tracked in Atlas v1.1 Chapter 24.12 (Open-ADR Backlog).
- **OPEN:** Whether the deprecation-register schema lives under `schemas/contracts/v1/governance/` or another sibling. Default per ADR-0001 reasoning is the `schemas/contracts/v1/...` tree; resolve by inspection or ADR.
- **OPEN:** Whether entry IDs are `dep-YYYY-NNN` or content-addressed (e.g., `spec_hash`-derived). The corpus supports both patterns; pick one in an ADR.
- **OPEN:** Owner role names (`<docs-steward>`, `<release-authority>`) — placeholders pending repo CODEOWNERS and a governance README.
- **OPEN:** Boundary between **tombstone** sufficiency (C5-09) and **erasure** for personal data (right-to-be-forgotten / Tribal data policies). Out of scope for this doc; tracked in C5-09 follow-ups.

---

## 12. Related docs

- `docs/doctrine/directory-rules.md` — §6.1, §6.2, §8, §14, §17 are the primary doctrinal sources for this register.
- `docs/doctrine/lifecycle-law.md` *(PROPOSED path)* — RAW → PUBLISHED lifecycle.
- `docs/doctrine/authority-ladder.md` *(PROPOSED path)* — Authority order.
- `docs/registers/AUTHORITY_LADDER.md` — Authority ordering.
- `docs/registers/CANONICAL_LINEAGE_EXPLORATORY.md` — Lineage classifier.
- `docs/registers/DRIFT_REGISTER.md` — Filed when a deprecation should have been opened but wasn't.
- `docs/registers/VERIFICATION_BACKLOG.md` — Open verification items.
- `docs/registers/OBJECT_FAMILY_MAP.md` *(PROPOSED path)* — Object family map referenced by deprecation entries.
- `docs/adr/ADR-0001-schema-home.md` — Schema-home rule for deprecated / superseding schemas.
- `docs/archive/deprecated/` — Archive home for retired documentation.
- `control_plane/deprecation_register.yaml` — Machine-readable register (this file's pair).
- Atlas v1.1 §24.8.1 (stale-state markers), §24.8.2 (supersession lineage), Appendix G (v1.0 → v1.1 precedent).

---

## 13. Appendix — worked example and reference tables

<details>
<summary><strong>A.1 — Worked example: retiring a <code>jsonschema/</code> mirror (illustrative)</strong></summary>

Illustrative only. Not a current repo claim.

1. **ADR opened.** `docs/adr/ADR-0001-schema-home.md` establishes `schemas/contracts/v1/...` as canonical.
2. **Migration manifest filed** under `migrations/schema/ADR-0001-schema-home/manifest.yaml`, listing every old → new mapping with `git_sha_before` / `git_sha_after` per Directory Rules §14.2 step 3.
3. **Mirror declared** via `jsonschema/README.md` with `class: mirror` per §8.
4. **Deprecation entry opened** in `control_plane/deprecation_register.yaml` with `lifecycle_state: active`, `compatibility_class: mirror`, and a sunset date.
5. **Rollback card drafted** under `release/rollback_cards/<release_id>.yaml`; dry-run rollback verified.
6. **Sunset announcement** at `lifecycle_state: sunset` — downstream consumers notified; mirror frozen against new writes.
7. **Retirement.** Mirror removed; entry transitions to `lifecycle_state: retired`. ID preserved permanently.

If any released claims referenced schemas under `jsonschema/` directly, a `CorrectionNotice` under `release/correction_notices/` is emitted alongside step 6.

</details>

<details>
<summary><strong>A.2 — Supersession lineage matrix (extract from Atlas §24.8.2)</strong></summary>

| Object class | Supersession rule | Required lineage artifact |
|---|---|---|
| `SourceDescriptor` | Replaced by newer descriptor; old retained with `superseded_by` | Supersession entry in source register |
| `EvidenceBundle` | Replaced when corrected; old retained for audit | `EvidenceBundle` + `CorrectionNotice` + supersession link |
| `GeographyVersion` | Replaced by newer version; both remain queryable for time-bound claims | Version register entry + crosswalk |
| Schema (under `schemas/contracts/v1/...`) | Replaced via ADR; old retained | ADR + supersession link in schema header |
| Policy | Replaced via accepted ADR; old retained | ADR + supersession link |
| `ReleaseManifest` | Replaced by next release; rollback target remains valid | Manifest history + rollback chain |
| `AIReceipt` | Never superseded retroactively; new answer is a new receipt | Two distinct `AIReceipt`s with cross-reference |
| Atlas / supplement | Superseded by ADR-recorded new edition; lineage retained | Atlas / supplement supersession appendix |

Source: Atlas v1.1 §24.8.2 (CONFIRMED).

</details>

<details>
<summary><strong>A.3 — Compatibility root class reference (Directory Rules §8)</strong></summary>

| Class | Meaning | Editable? | Migration plan required? |
|---|---|---|---|
| `legacy` | Was canonical, now superseded | No (new files SHOULD NOT land) | Yes |
| `mirror` | Generated or copied from canonical home | No (not edited directly) | When lifecycle ends |
| `deprecated` | Slated for removal | No | Yes |
| `external-export` | Exists for downstream consumers; canonical home is elsewhere | No (regenerated) | Optional |
| `transitional` | Mid-migration; ADR or migration note pinned | Bounded | Yes |

</details>

<details>
<summary><strong>A.4 — Stale-state markers cross-reference (Atlas §24.8.1)</strong></summary>

A stale claim is not the same as a deprecated artifact. Stale claims often *trigger* a deprecation entry on the underlying schema, source, or release.

| Marker | Triggered by | Common downstream action |
|---|---|---|
| Source freshness expired | Cadence in `SourceDescriptor` passed without a new admission | Re-admit, supersede, or mark dependent claims stale |
| Schema version drift | Object schema upgraded past the published claim's version | Migrate, re-validate, re-release; consider deprecation entry on old schema |
| Geography version drift | `GeographyVersion` replaced; published claim still bound to prior version | Rebind, re-release, or mark stale |
| Time-scope outside support | Claim's temporal scope outside current data support window | Mark stale; do not refresh silently |
| Model version superseded | `ModelRunReceipt` references an older model than current | Re-run, supersede, or mark stale |
| Review aged out | `ReviewRecord` older than the sensitive-lane review cycle | Trigger steward review; potentially downgrade tier |
| Rights status changed | Rights change in `SourceDescriptor` or rights-holder communication | Re-evaluate tier; potentially downgrade; emit `CorrectionNotice` |
| Policy version changed | Policy referenced by `PolicyDecision` was superseded | Re-run gate; potentially supersede release; deprecation entry on old policy if retired |

</details>

---

<sub>Last updated: 2026-05-12 · Status: draft / PROPOSED · Authority: docs/registers · Pair: <code>control_plane/deprecation_register.yaml</code> · [Back to top](#-kfm-deprecation-register--doctrine-and-reading-guide)</sub>
