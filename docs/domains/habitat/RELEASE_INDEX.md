<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/domains/habitat/release-index
title: Habitat Domain Release Index
type: standard
version: v1.1
status: draft
owners: <habitat-domain-steward>, <release-authority>, <docs-steward>   # placeholders pending owner-registry verification
created: 2026-05-17
updated: 2026-06-05
policy_label: public
contract_version: "3.0.0"   # pinned per ai-build-operating-contract.md
related:
  - docs/domains/habitat/README.md
  - docs/domains/habitat/PRESERVATION_MATRIX.md
  - docs/domains/habitat/REASON_CODES.md
  - docs/standards/PROV.md
  - docs/standards/PMTILES.md
  - release/README.md
  - release/manifests/
  - release/promotion_decisions/
  - release/rollback_cards/
  - release/correction_notices/
  - release/candidates/habitat/
  - data/published/layers/habitat/
  - data/registry/sources/habitat/
  - docs/runbooks/fauna/SOURCE_REFRESH_RUNBOOK.md
  - ai-build-operating-contract.md
tags: [kfm, domain:habitat, release, index, navigation, governance]
notes:
  - This doc is a human-readable navigation index, not the release authority store.
  - Authority for ReleaseManifest, PromotionDecision, RollbackCard, CorrectionNotice lives under release/.
  - Authority for published habitat artifacts lives under data/published/layers/habitat/.
  - "Source-role labels align to the CONFIRMED 7-role enum (Atlas §24.1): observed | regulatory | modeled | aggregate | administrative | candidate | synthetic. USFWS critical habitat = regulatory (not 'authority')."
  - "Sensitivity tier labels align to the CONFIRMED Atlas §24.5.1 scheme: T0 Open | T1 Generalized | T2 Reviewer | T3 Restricted | T4 Denied."
  - "Path uses Directory Rules §12 segment form (docs/domains/habitat/); Atlas §24.13 flat-form drift is tracked in the lane README (HAB-V-009)."
  - Index entries and field set are PROPOSED until ADR/per-root README confirmation.
  - "CONTRACT_VERSION = \"3.0.0\""
[/KFM_META_BLOCK_V2] -->

# 🌿 Habitat Domain Release Index

> **Human-readable navigation index of governed releases in the Habitat domain — pointers to `ReleaseManifest`, `PromotionDecision`, `CorrectionNotice`, `RollbackCard`, and supporting evidence and validation artifacts. This document is a mirror, not an authority store.**

![status](https://img.shields.io/badge/status-draft-yellow)
![domain](https://img.shields.io/badge/domain-habitat-2E7D32)
![policy](https://img.shields.io/badge/policy__label-public-blue)
![lifecycle](https://img.shields.io/badge/lifecycle-CATALOG%E2%86%92PUBLISHED-7E57C2)
![authority](https://img.shields.io/badge/authority-navigational_only-lightgrey)
![contract](https://img.shields.io/badge/CONTRACT__VERSION-3.0.0-blueviolet)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)
![updated](https://img.shields.io/badge/updated-2026--06--05-informational)
<!-- TODO: replace static badges with CI-driven Shields endpoints once owners + build URLs are verified (NEEDS VERIFICATION). -->

| Field | Value |
|---|---|
| **Status** | Draft — `PROPOSED` placement, fields, and scope |
| **Owners** | `<habitat-domain-steward>` · `<release-authority>` · `<docs-steward>` *(placeholders)* |
| **Contract** | `CONTRACT_VERSION = "3.0.0"` |
| **Last updated** | 2026-06-05 |
| **Authority role** | Navigational mirror of `release/` and `data/published/layers/habitat/`. **Not** the release authority. |
| **Lifecycle anchor** | `CATALOG / TRIPLET → PUBLISHED → PUBLISHED′ (correction) → withdrawn / rolled-back` |

---

## Contents

1. [Scope and role](#1-scope-and-role)
2. [Authority and source-of-truth pointers](#2-authority-and-source-of-truth-pointers)
3. [Release flow and where this index sits](#3-release-flow-and-where-this-index-sits)
4. [Index record schema](#4-index-record-schema)
5. [Habitat release index — entry table](#5-habitat-release-index--entry-table)
6. [Sensitivity posture for Habitat releases](#6-sensitivity-posture-for-habitat-releases)
7. [Cross-lane release interactions](#7-cross-lane-release-interactions)
8. [Correction, withdrawal, and rollback handling](#8-correction-withdrawal-and-rollback-handling)
9. [Stale-state and supersession markers](#9-stale-state-and-supersession-markers)
10. [Governed AI behavior over indexed releases](#10-governed-ai-behavior-over-indexed-releases)
11. [Validators and closure checks](#11-validators-and-closure-checks)
12. [Open questions register](#12-open-questions-register)
13. [Open verification backlog](#13-open-verification-backlog)
14. [Changelog & definition of done](#14-changelog--definition-of-done)
15. [Related docs](#15-related-docs)

---

## 1. Scope and role

The Habitat Domain Release Index is a **docs-side, human-readable mirror** of governed release activity in the Habitat lane. It surfaces — in one place — the released, withdrawn, corrected, superseded, and rolled-back states of Habitat artifacts, with pointers into the authority records under `release/` and the public artifacts under `data/published/layers/habitat/`.

> [!IMPORTANT]
> **This document does not decide anything.** A release is not "released" because it appears here. It appears here because a `ReleaseManifest` exists in `release/manifests/` and a `PromotionDecision` recorded the governed `CATALOG → PUBLISHED` state transition. *(CONFIRMED doctrine — promotion is a governed state transition, not a file move.)* Likewise, withdrawal, correction, or rollback are reflected here only after the corresponding `CorrectionNotice` / `RollbackCard` / withdrawal notice has been issued under `release/`.

**This index does the following:**

- Provides a discoverable list of Habitat releases for stewards, reviewers, and public-facing consumers.
- Surfaces lifecycle state, sensitivity tier, evidence support, and review status for each release entry.
- Cross-links to release authority records, evidence bundles, validation reports, and rollback targets.
- Highlights stale-state, withdrawal, correction, and supersession status.
- Documents the cross-lane releases that involve Habitat as an adjacent derivative (e.g., Habitat × Fauna thin slice).

**This index does *not* do the following:**

- It does not own release decisions.
- It does not store `ReleaseManifest`, `PromotionDecision`, `RollbackCard`, or `CorrectionNotice` objects.
- It does not store published artifacts (PMTiles, GeoParquet, COG, layer manifests).
- It does not store source descriptors, evidence bundles, or validation reports.
- It does not authorize promotion, withdrawal, or rollback.

> [!NOTE]
> If this document and a `release/` record conflict, the `release/` record wins. Open a `docs/registers/DRIFT_REGISTER.md` entry rather than treating the doc as authority. *(CONFIRMED doctrine — "Documentation as truth" is a named anti-pattern in `directory-rules.md`.)*

[⬆ Back to top](#contents)

---

## 2. Authority and source-of-truth pointers

This index resolves to the actual authority records below. The `release/` subtree shape is **CONFIRMED** by the repository guiding document's per-root README contract (`directory-rules.md` §9.2); the specific presence of each path in *your* branch is **PROPOSED** pending mounted-repo verification.

| Concern | Authority location | What lives there | Status |
|---|---|---|---|
| Release decisions | `release/manifests/` | `ReleaseManifest` records, by `release_id`, declaring contents, digests, evidence refs, and rollback target. | CONFIRMED subtree / PROPOSED presence |
| Promotion records | `release/promotion_decisions/` | `PromotionDecision` records for `CATALOG → PUBLISHED` transitions. | CONFIRMED subtree / PROPOSED presence |
| Rollback records | `release/rollback_cards/` | `RollbackCard` records — rollback target, reason, invalidates, review ref. | CONFIRMED subtree / PROPOSED presence |
| Corrections | `release/correction_notices/` | `CorrectionNotice` records for post-publication corrections. | CONFIRMED subtree / PROPOSED presence |
| Withdrawals | `release/withdrawal_notices/` | Withdrawal records and reasons. | CONFIRMED subtree / PROPOSED presence |
| Signatures / attestations / SBOM | `release/signatures/`, `release/attestations/`, `release/sbom/` | DSSE / Sigstore / cosign artifacts, SLSA in-toto provenance, SBOMs, Rekor index references. | CONFIRMED subtree / PROPOSED presence |
| Release candidates | `release/candidates/habitat/` | Habitat-lane release-candidate dossiers prior to `PUBLISHED`. | CONFIRMED subtree / PROPOSED presence |
| Published artifacts | `data/published/layers/habitat/` | The actual public-safe outputs consumers read. | PROPOSED |
| Evidence support | `data/proofs/evidence_bundle/` | `EvidenceBundle` and `EvidenceRef` resolution targets. | PROPOSED |
| Process memory | `data/receipts/release/` (and adjacent) | Run, validation, AI, ingest, and release receipts. | CONFIRMED home / PROPOSED presence |
| Source registry | `data/registry/sources/habitat/` | Append-only source descriptors and admission records. | PROPOSED (see §12 — `sources/` vs flat form) |
| Catalog closure | `data/catalog/domain/habitat/` | STAC/DCAT/PROV records for Habitat datasets. | PROPOSED |
| Decision-record schemas | `schemas/contracts/v1/release/`, `schemas/contracts/v1/policy/` | `release_manifest`, `promotion_decision`, `rollback_target`, `policy_decision` schemas (ADR-0001 home). | CONFIRMED home (schema table) / PROPOSED presence |
| Per-root governance | `release/README.md`, `data/published/README.md`, `data/registry/README.md` | Per-root rules refining placement. | CONFIRMED contract / PROPOSED presence |

> [!TIP]
> If a row above is missing from the mounted repo, that is a drift signal — not a license to backfill the data here. Open a drift entry and surface it under [§13](#13-open-verification-backlog).

> [!NOTE]
> **Decision records vs policy rules.** The `PolicyDecision` *record schema* lives under `schemas/contracts/v1/policy/policy_decision.schema.json`; the *policy rules* that produce those decisions live under `policy/domains/habitat/`. The index's `policy_decision_ref` resolves to the **record** (an emitted artifact), not to the rule. *(CONFIRMED schema home per the Master MapLibre schema table; PROPOSED presence.)*

[⬆ Back to top](#contents)

---

## 3. Release flow and where this index sits

The KFM lifecycle invariant is **`RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED`** — promotion is a governed state transition, not a file move. *(CONFIRMED doctrine.)* This index attaches to the right-hand side of the lifecycle and reflects `PUBLISHED` and post-publication state.

```mermaid
flowchart LR
  RAW["RAW<br/><i>data/raw/habitat/</i>"] --> WORK["WORK / QUARANTINE<br/><i>data/work/habitat/</i><br/><i>data/quarantine/habitat/</i>"]
  WORK --> PROCESSED["PROCESSED<br/><i>data/processed/habitat/</i>"]
  PROCESSED --> CATALOG["CATALOG / TRIPLET<br/><i>data/catalog/domain/habitat/</i>"]
  CATALOG --> CAND["Release candidate<br/><i>release/candidates/habitat/</i>"]
  CAND -->|"PromotionDecision"| MAN["ReleaseManifest<br/><i>release/manifests/</i>"]
  MAN --> PUB["PUBLISHED artifacts<br/><i>data/published/layers/habitat/</i>"]
  MAN -. "mirrored" .-> IDX["docs/domains/habitat/<br/><b>RELEASE_INDEX.md</b><br/><i>(this doc)</i>"]
  PUB -. "cross-referenced" .-> IDX
  MAN -->|"CorrectionNotice"| CORR["PUBLISHED′<br/><i>release/correction_notices/</i>"]
  MAN -->|"RollbackCard"| RB["Rollback target<br/><i>release/rollback_cards/</i>"]
  CORR -. "mirrored" .-> IDX
  RB -. "mirrored" .-> IDX

  classDef authority fill:#E8F5E9,stroke:#2E7D32,stroke-width:1px,color:#1B5E20;
  classDef artifact fill:#E3F2FD,stroke:#1565C0,stroke-width:1px,color:#0D47A1;
  classDef docs fill:#FFF8E1,stroke:#F9A825,stroke-width:1px,color:#5D4037;
  classDef lifecycle fill:#F3E5F5,stroke:#6A1B9A,stroke-width:1px,color:#4A148C;
  class RAW,WORK,PROCESSED,CATALOG lifecycle
  class CAND,MAN,CORR,RB authority
  class PUB artifact
  class IDX docs
```

> [!WARNING]
> `NEEDS VERIFICATION` — exact paths under `data/`, `release/`, and any compatibility roots (`artifacts/`, `policies/`, `jsonschema/`, `ui/`, `web/`) require mounted-repo inspection. The diagram reflects `directory-rules.md` doctrine and the confirmed `release/` subtree shape, not a confirmed file tree.

[⬆ Back to top](#contents)

---

## 4. Index record schema

Each entry in [§5](#5-habitat-release-index--entry-table) carries the following fields. The schema below is **PROPOSED**; the canonical field set lives with the `ReleaseManifest` schema in `schemas/contracts/v1/release/`. This doc mirrors, it does not define.

| Field | Type | Description | Authoritative source |
|---|---|---|---|
| `release_id` | string | Deterministic release identifier. | `ReleaseManifest.release_id` |
| `title` | string | Short human-readable release title. | `ReleaseManifest` / candidate dossier |
| `artifact_kinds` | enum[] | Subset of `{pmtiles, stac, geojson, parquet, model, manifest, receipt}`. | `ReleaseManifest.contents[]` |
| `object_families` | string[] | Habitat object families covered (`HabitatPatch`, `LandCoverObservation`, `EcologicalSystem`, `Habitat Quality Score`, `SuitabilityModel`, `ConnectivityEdge`, `Corridor`, `Restoration Opportunity`, `StewardshipZone`, `Model Run Receipt`, `UncertaintySurface`). | Catalog closure record |
| `source_roles` | string[] | Source-role coverage drawn from `SourceDescriptor` entries — CONFIRMED enum `{observed, regulatory, modeled, aggregate, administrative, candidate, synthetic}`. | `data/registry/sources/habitat/` |
| `sensitivity_tier` | enum | One of `T0` (Open), `T1` (Generalized), `T2` (Reviewer), `T3` (Restricted), `T4` (Denied) — Atlas §24.5.1. | `PolicyDecision` + `RedactionReceipt` |
| `lifecycle_state` | enum | `PUBLISHED`, `PUBLISHED′ (corrected)`, `withdrawn`, `superseded`, `rolled_back`. | `release/` records |
| `evidence_ref` | uri | Resolves to one or more `EvidenceBundle` objects. | `data/proofs/evidence_bundle/` |
| `validation_ref` | uri | `ValidationReport` reference, including catalog-closure tests. | `data/receipts/validation/` |
| `policy_decision_ref` | uri | `PolicyDecision` **record** reference (not the rule). | `data/receipts/...` (record); rule in `policy/domains/habitat/` |
| `review_ref` | uri | `ReviewRecord` reference where review is required. | `release/` adjacency |
| `manifest_ref` | uri | The `ReleaseManifest` itself. | `release/manifests/` |
| `promotion_ref` | uri | The `PromotionDecision` that authorized the transition. | `release/promotion_decisions/` |
| `rollback_target` | uri | `RollbackCard` / rollback-target reference, or `null` if not yet exercised. | `release/rollback_cards/` |
| `correction_refs` | uri[] | Any `CorrectionNotice` records that supersede or amend this release. | `release/correction_notices/` |
| `signature_ref` | uri | DSSE / cosign keyless bundle and Rekor index reference. | `release/signatures/` |
| `spec_hash` | string | Canonicalized (JCS + SHA-256) hash of the manifest sidecar input, excluding `spec_hash` itself. | Sidecar generation step |
| `released_at` | datetime | Time of `PUBLISHED` transition. | `PromotionDecision.time` |
| `stale_after` | datetime \| null | Declared freshness tolerance, if any. | `SourceDescriptor.cadence` + policy |
| `supersedes` | uri \| null | Prior `release_id` superseded by this one. | Release lineage |
| `notes` | string | Free-form steward/release-authority notes. | n/a |

> [!NOTE]
> `NEEDS VERIFICATION` — exact schema homes are CONFIRMED by the Master MapLibre schema table (`schemas/contracts/v1/release/promotion_decision.schema.json`, `.../release/rollback_target.schema.json`, `.../policy/policy_decision.schema.json`) and default to `schemas/contracts/v1/` per ADR-0001; **live file placement** requires mounted-repo confirmation. The `ReleaseManifest` content set (`release_id, contents[], digests, evidence_refs[], rollback_target, time`) is **CONFIRMED** in Atlas §24.2 and KFM-P7-PROG-0003; the extended release-index entry fields (`dataset_id, spec_hash, run_receipt, SPDX, evidence bundle digest`) are confirmed there too.

[⬆ Back to top](#contents)

---

## 5. Habitat release index — entry table

> [!IMPORTANT]
> **No releases are currently indexed.** This table is a **PROPOSED** template form. Entries are added only after a `ReleaseManifest` exists under `release/manifests/` and a `PromotionDecision` records the transition. Do not pre-seed rows from intent, plan, or candidate state.

| `release_id` | Title | Kinds | Sensitivity | State | Released | Evidence | Manifest | Rollback | Notes |
|---|---|---|---|---|---|---|---|---|---|
| _(empty — `NEEDS VERIFICATION` against mounted repo)_ | — | — | — | — | — | — | — | — | — |

<details>
<summary><b>Illustrative — Habitat × Fauna thin-slice fixture (NOT a real release; PROPOSED format only)</b></summary>

The Habitat × Fauna thin slice is repeatedly identified as the **first proof lane** for Habitat releases, using *public-safe fixtures, not live sensitive source connectors*. *(CONFIRMED doctrine — `[DOM-HF]`; Atlas §24.13 "pairs with Fauna under the thin-slice plan".)* If and when that thin slice produces a `ReleaseManifest`, the index row would look like:

| Field | Illustrative value |
|---|---|
| `release_id` | `kfm:release:habitat-fauna-thinslice:vYYYY-MM-DD-N` |
| `title` | "Habitat × Fauna thin-slice public-safe assignment, fixture release" |
| `artifact_kinds` | `pmtiles`, `geojson`, `stac`, `manifest`, `receipt` |
| `object_families` | `HabitatPatch`, `UncertaintySurface`, *(Fauna)* `RangePolygon` (public), `RedactionReceipt` |
| `source_roles` | NLCD: **observed**; NWI: **regulatory**; GBIF/iNaturalist: **observed** (geoprivacy-transformed); USFWS critical habitat: **regulatory** (excluded from public layer); KDWP context: source excluded from public layer |
| `sensitivity_tier` | `T1` (Generalized) |
| `lifecycle_state` | _(illustrative)_ `PUBLISHED` |
| `evidence_ref` | `kfm://evidence/bundle/<...>` |
| `validation_ref` | catalog-closure + geoprivacy-transform tests pass |
| `policy_decision_ref` | `PolicyDecision` record = allow (public-safe lane); rule in `policy/domains/habitat/` |
| `manifest_ref` | `release/manifests/<release_id>.json` |
| `promotion_ref` | `release/promotion_decisions/<release_id>.json` |
| `rollback_target` | `release/rollback_cards/<release_id>.json` |
| `notes` | Cross-lane: Fauna owns occurrence truth; this release exposes Habitat-side context only. |

This row is **illustrative**; do not treat it as evidence that the release exists. *(PROPOSED — implementation depth UNKNOWN until mounted-repo inspection.)*

</details>

[⬆ Back to top](#contents)

---

## 6. Sensitivity posture for Habitat releases

Habitat publication touches several distinct sensitivity surfaces that this index must reflect honestly. Tier labels follow the **CONFIRMED** Atlas §24.5.1 scheme (`T0` Open, `T1` Generalized, `T2` Reviewer, `T3` Restricted, `T4` Denied). *(CONFIRMED doctrine / PROPOSED implementation — `[DOM-HAB]`, `[DOM-HF]`, `[ENCY]`.)*

| Surface | Posture | Index implication |
|---|---|---|
| **Regulatory critical habitat** | Source-role-bound — USFWS ECOS is **regulatory**. MUST NOT be collapsed with modeled habitat. | `source_roles` records `regulatory`; modeled-as-critical denial test required (see [§11](#11-validators-and-closure-checks)). |
| **Modeled habitat / suitability surfaces** | Must carry model identity, version, support, and uncertainty. Model vs observation labels stay visible. | `object_families` includes `SuitabilityModel`, `Model Run Receipt`, `UncertaintySurface`. |
| **Sensitive occurrence joins** | Habitat outputs that reveal sensitive occurrence context (nests, dens, roosts, hibernacula, spawning sites, rare-plant locations) **fail closed**. Atlas master matrix: sensitive Fauna occurrence defaults to **T4**, reaching **T1** only via geoprivacy + RedactionReceipt + ReviewRecord + PolicyDecision. | `sensitivity_tier` ≥ `T1`; `RedactionReceipt` recorded under evidence. |
| **Geoprivacy transforms** | Generalization, gridding, watershed/county aggregation, buffering, jitter-with-constraints, delayed publication, or steward-only exact access. Each transform emits a receipt. | `evidence_ref` resolves to a bundle containing the transform receipt; transform type surfaced in `notes`. |
| **Stewardship zones / PAD-US context** | PAD-US is **administrative** context; rights and current terms `NEEDS VERIFICATION`. Tribal / sovereign stewardship zones deny by default. | Source-role check at admission; not promoted as authority. |
| **Unclear rights / unresolved source role / unresolved sensitivity** | Blocks public promotion. | Entry never appears in [§5](#5-habitat-release-index--entry-table); held in `release/candidates/habitat/` with a quarantine reason (see `REASON_CODES.md`). |

> [!CAUTION]
> Sensitive surfaces are **deny-by-default**. The presence of a release candidate under `release/candidates/habitat/` is **not** authorization to index it here. Only `PUBLISHED` state (or post-publication states like withdrawn/superseded) belongs in the entry table.

[⬆ Back to top](#contents)

---

## 7. Cross-lane release interactions

Habitat releases routinely interact with adjacent domain lanes. Habitat **owns** habitat patches, ecological systems, suitability, connectivity, corridors, restoration opportunity, and stewardship zones. It **does not own** species occurrence truth (Fauna), plant taxonomy (Flora), or the truth of Soil, Hydrology, Agriculture, Hazards, or Archaeology. *(CONFIRMED / PROPOSED — `[DOM-HAB]`, `[DOM-HF]`, `[ENCY]`.)*

| Related lane | Relation | Index implication |
|---|---|---|
| **Fauna** | Habitat assignment and occurrence context with geoprivacy. *(Habitat × Fauna thin slice is the proposed first proof lane.)* | Cross-link to Fauna release-index entries when a Habitat release exposes assignment context. Geoprivacy transform receipts required. |
| **Flora** | Vegetation community and rare-plant context under Flora controls. | Cross-link; rare-plant geometry never bound into Habitat public layers. |
| **Soil / Hydrology** | Substrate, moisture, wetlands, riparian support. | Cross-link to relevant lane releases; do not absorb their truth. |
| **Hazards** | Fire, drought, flood, smoke, and resilience-stress context. | Hazard layers consumed as context, not authority. |
| **Agriculture / Roads-Rail-Trade / Settlements-Infrastructure / Archaeology / People-DNA-Land** | Adjacent; not Habitat truth. | Joined only through governed relationships; not co-released. |

> [!NOTE]
> Cross-lane index navigation is **PROPOSED**. The doctrine names the relations clearly (Habitat dossier §F); the operational form of cross-lane index linking awaits the first published cross-lane release.

[⬆ Back to top](#contents)

---

## 8. Correction, withdrawal, and rollback handling

Correction, withdrawal, and rollback are **publication requirements, not afterthoughts**. *(CONFIRMED doctrine — Atlas §24.6.1 lifecycle gates; `directory-rules.md`.)* When any of them occurs, the entry in [§5](#5-habitat-release-index--entry-table) is updated to reflect the new state — the row is **not** deleted, and the original `release_id` remains.

```mermaid
stateDiagram-v2
  [*] --> PUBLISHED : PromotionDecision
  PUBLISHED --> PUBLISHED_prime : CorrectionNotice (supersedes original)
  PUBLISHED --> withdrawn : withdrawal_notice
  PUBLISHED --> rolled_back : RollbackCard
  PUBLISHED_prime --> PUBLISHED_prime : further CorrectionNotice
  PUBLISHED_prime --> rolled_back : RollbackCard
  PUBLISHED_prime --> withdrawn : withdrawal_notice
  rolled_back --> PUBLISHED : republish via governed release path
  withdrawn --> [*]
```

| Action | Trigger | `lifecycle_state` becomes | Required record | Index row behavior |
|---|---|---|---|---|
| **Correction** | Detected error or new evidence; downstream derivatives identified. | `PUBLISHED′ (corrected)` | `CorrectionNotice` + `ReviewRecord` (if material) | Row updated in place; `correction_refs[]` appended; `supersedes` set on the successor row. |
| **Withdrawal** | Rights, sensitivity, or evidence retraction. | `withdrawn` | withdrawal notice | Row updated in place; reason surfaced in `notes`. |
| **Rollback** | Failed release or steward-significant defect. | `rolled_back` | `RollbackCard` | Row updated; `rollback_target` populated; prior `release_id` becomes the current `PUBLISHED` state via republish. |
| **Supersession** | New release replaces an earlier one. | `superseded` | New `ReleaseManifest` with `supersedes` link | Old row retained; new row added; cross-link both ways. |

> [!IMPORTANT]
> **Correction-lineage failures are reason-coded.** A correction that cannot resolve its downstream derivatives, or that points at a missing prior release, fails closed with `CORRECTION_DERIVATIVES_UNRESOLVED` / `CORRECTION_PRIOR_RELEASE_MISSING` (Atlas §24.6.3). The index does not advance a row to `PUBLISHED′` until those resolve. See `docs/domains/habitat/REASON_CODES.md`.

> [!WARNING]
> Rollback must not be a hidden file copy. *(CONFIRMED doctrine.)* Rollback updates this index only after a `RollbackCard` is recorded and the rollback target is verified by digests and manifests.

[⬆ Back to top](#contents)

---

## 9. Stale-state and supersession markers

KFM separates **stale** from **wrong**: a stale claim is one whose evidence, source freshness, or context has aged past its declared tolerance; a wrong claim is one whose substance is incorrect. *(CONFIRMED doctrine — Atlas §24.8; `directory-rules.md`.)* The index reflects both, but does not invent either.

| Marker | Trigger | Index column | UI signal it pairs with |
|---|---|---|---|
| `stale_after` reached | `SourceDescriptor.cadence` passed without a new admission. | `stale_after` populated; current time exceeds it | Stale source badge in Evidence Drawer |
| Source dependency stale | Upstream domain released a `CorrectionNotice` invalidating a Habitat input. | `notes` annotated; downstream review queued | Derived-stale badge |
| Supersession | New `release_id` `supersedes` this one. | `lifecycle_state = superseded`; `supersedes` set on successor | Superseded banner |
| Withdrawn | Withdrawal notice posted. | `lifecycle_state = withdrawn` | Withdrawn banner |

[⬆ Back to top](#contents)

---

## 10. Governed AI behavior over indexed releases

AI surfaces (Focus Mode, summarization, drafting) may operate **over released Habitat `EvidenceBundle`s only**. AI is interpretive, not the root truth source. *(CONFIRMED doctrine — `[GAI]`, `[DOM-HAB]`, `[DOM-HF]`, `[ENCY]`.)*

| AI behavior | Posture | Index relevance |
|---|---|---|
| Summarize released Habitat `EvidenceBundle`s | **Allowed**, citation-bound | AI consumes only rows where `lifecycle_state ∈ {PUBLISHED, PUBLISHED′}` and `evidence_ref` resolves. |
| Compare evidence across Habitat releases | **Allowed** if both rows resolve evidence and policy. | Cross-references via `release_id` and `evidence_ref`. |
| Explain limitations, uncertainty, or stale state | **Allowed** | Index supplies `sensitivity_tier`, `stale_after`, `correction_refs`. |
| Draft steward-review notes | **Allowed** | AI returns drafts, not decisions. |
| Answer where evidence is insufficient | **ABSTAIN** | Index does not promote a `release_id` whose evidence is unresolved. |
| Answer where policy, rights, sensitivity, or release state block | **DENY** | Withdrawn, rolled-back, or `T2`+ tier rows are off-limits for public answers. |
| Operate without citation | **DENY** | Cite-or-abstain is the default truth posture. |

> [!IMPORTANT]
> AI surfaces over this index follow the `RuntimeResponseEnvelope` finite outcomes (`ANSWER / ABSTAIN / DENY / ERROR`), carry a `reason_code` on every non-`ANSWER`, and emit `AIReceipt`s. AI reads only released `EvidenceBundle`s; RAW/WORK access is `T4`. The index does not change those envelopes; it scopes them.

[⬆ Back to top](#contents)

---

## 11. Validators and closure checks

Index entries are an output of release closure, not a substitute for it. The validator set below is **PROPOSED** and converges across Habitat-domain expectations in the Domains Atlas §6.K and the Master MapLibre Atlas `ML-058-044` / `ML-058-045`.

- **Catalog closure** — STAC/DCAT/PROV records present and resolved before any `PUBLISHED` entry appears here. *(PROPOSED)*
- **Critical-habitat source-role test** — USFWS ECOS critical habitat treated as `regulatory`; never collapsed with modeled habitat. *(PROPOSED — `[DOM-HAB §K]`; Atlas §24.1.2)*
- **Modeled-as-critical denial test** — modeled habitat MUST NOT be presented as regulatory critical habitat. *(PROPOSED — `[DOM-HAB §K]`)*
- **Occurrence geoprivacy test** — joins to Fauna/Flora occurrence pass through geoprivacy transforms; transform receipts present. *(PROPOSED — `[DOM-HAB §K]`)*
- **Source descriptor test** — every `source_roles` entry resolves to a `SourceDescriptor` with rights, sensitivity, cadence, and `source_role` recorded. *(PROPOSED — `[DOM-HAB §K]`)*
- **Habitat × Fauna thin-slice fixtures** — the first-proof lane uses public-safe fixtures only. *(PROPOSED — `[DOM-HF]`)*
- **ReleaseManifest artifact-kind coverage** — `artifact_kinds[]` is a subset of `{pmtiles, stac, geojson, parquet, model, manifest, receipt}`. *(PROPOSED — `[ML-058-044]`)*
- **ReleaseManifest policy gate** — Rego policy denies unknown `policy_label`, unknown `rights_status`, non-public sensitivity, missing `evidence_refs[]` / artifacts, or unsupported rollback. *(PROPOSED — `[ML-058-045]`)*
- **`spec_hash` canonicalization** — JCS + SHA-256; the manifest spec hash excludes `spec_hash` itself. *(PROPOSED — `[ML-M-046]`)*
- **Rollback drill** — at least one rollback-drill receipt exists for the lane before a steward-significant release is treated as reliable. *(PROPOSED — Pass-20 REL doctrine)*

> [!NOTE]
> CI workflows that emit these checks are **NEEDS VERIFICATION**. The doctrine names them; the implementation home (e.g., `.github/workflows/`, `tools/validators/`, `tools/release/`, `tools/attest/`) requires mounted-repo confirmation.

[⬆ Back to top](#contents)

---

## 12. Open questions register

| ID | Question | Owner role | Resolution path |
|---|---|---|---|
| OQ-HAB-REL-01 | Is `docs/domains/habitat/RELEASE_INDEX.md` the canonical filename, or a different convention (`RELEASES.md`, `release-index.md`, subfolder `docs/domains/habitat/releases/`)? | Docs steward | Per-root README in `docs/domains/` or ADR. |
| OQ-HAB-REL-02 | Is the index hand-maintained, generated from `release/manifests/`, or both (hand-curated summary + generated body)? | Release authority + docs steward | ADR or per-root README; CI generator if generated. |
| OQ-HAB-REL-03 | Should the index reflect `release/candidates/habitat/` state (pre-published), or only `PUBLISHED+` state? | Release authority | ADR. Current draft default: **`PUBLISHED+` only**. |
| OQ-HAB-REL-04 | `correction_refs[]` cardinality and ordering rules for multi-step corrections. | Correction reviewer | ADR on correction lineage. |
| OQ-HAB-REL-05 | Registry path: `data/registry/sources/habitat/` vs `data/registry/habitat/` (Directory Rules §12 lists both forms). | Directory steward | Per-root README in `data/registry/`. |
| OQ-HAB-REL-06 | Relationship between `ReleaseManifest` and per-product `delta_manifest` (overlap noted in KFM-P7-PROG-0003). | Release authority | ADR; expansion direction: release manifest = union of delta-manifest refs. |
| OQ-HAB-REL-07 | Separation-of-duties threshold — when must the release authority be distinct from the author for a Habitat release? | Release authority | ADR-S-09 (reviewer separation-of-duties). |

[⬆ Back to top](#contents)

---

## 13. Open verification backlog

These items remain `NEEDS VERIFICATION` before promotion from `draft` to `published`. They SHOULD be tracked in `docs/registers/VERIFICATION_BACKLOG.md`.

1. Exact `ReleaseManifest` schema home under `schemas/contracts/v1/release/` — verify presence (default per ADR-0001).
2. Per-domain `release/candidates/habitat/` structure and dossier shape — verify against `release/README.md` or the mounted repo.
3. Habitat-domain sensitivity-tier vocabulary alignment (`T0`–`T4`) cross-checked against `policy/sensitivity/` and Atlas §24.5.
4. Registry path (`data/registry/sources/habitat/` vs `data/registry/habitat/`) — verify against the `data/registry/` per-root README (see OQ-HAB-REL-05).
5. Stale-state cadence values for Habitat sources (NLCD, NWI, GAP/LANDFIRE, NatureServe, GBIF/iNaturalist, PAD-US) — verify from `SourceDescriptor` registry entries.
6. AI Focus-Mode template binding for Habitat — exact prompt / citation / abstain rules — verify against the governed-AI focus-flow doc and policy.
7. CI workflow homes for the §11 closure checks — verify against `.github/workflows/`, `tools/validators/`, `tools/release/`, `tools/attest/`.
8. Path-form conflict (Directory Rules §12 segment vs Atlas §24.13 flat) — tracked as HAB-V-009 in the lane README; this index uses the §12 segment form.

<details>
<summary><b>Doctrine touchstones used in this draft (reference)</b></summary>

- **Lifecycle invariant** — `RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED`; promotion is a governed state transition. *(`directory-rules.md`; Atlas §24.6.)*
- **Trust membrane** — public clients use governed APIs; `release/` holds decisions; `data/published/` holds artifacts; the two are distinct. *(`directory-rules.md` §9.2; Atlas §24.6.2.)*
- **Domain Placement Law** — domains never become root folders; Habitat content lives under `docs/domains/habitat/`, `release/candidates/habitat/`, `data/published/layers/habitat/`, etc. *(`directory-rules.md` §12.)*
- **Documentation-as-truth is an anti-pattern** — docs reflect, they do not decide. *(`directory-rules.md` §13.)*
- **Habitat sensitivity posture** — regulatory critical habitat, modeled habitat, occurrence-linked outputs, and stewardship zones each carry distinct controls; sensitive joins fail closed. *(Atlas §6.I, §6.K; Encyclopedia §7.4.)*
- **ReleaseManifest content (CONFIRMED)** — `release_id, contents[], digests, evidence_refs[], rollback_target, time`; a single signed hashable JSON object naming every dataset, bundle, and tile archive; content-addressed via `spec_hash`. *(Atlas §24.2; KFM-P7-PROG-0003.)*
- **Decision-record schema homes (CONFIRMED)** — `PromotionDecision` → `schemas/contracts/v1/release/promotion_decision.schema.json`; rollback target → `.../release/rollback_target.schema.json`; `PolicyDecision` → `.../policy/policy_decision.schema.json`. *(Master MapLibre v2.1 schema table.)*
- **Separation of duties (CONFIRMED)** — the release authority issues `ReleaseManifest`s and authorizes `PUBLISHED`, distinct from authorship when materiality applies. *(Atlas §24.7; ADR-S-09.)*
- **Cite-or-abstain truth posture** — AI surfaces ABSTAIN on insufficient evidence and DENY on policy/sensitivity/release blocks. *(Governed AI dossier; Atlas §24.3.)*

</details>

[⬆ Back to top](#contents)

---

## 14. Changelog & definition of done

### 14.1 Changelog v1 → v1.1

| Change | Type (per contract §37) | Reason |
|---|---|---|
| Aligned `source_roles` to the CONFIRMED 7-role enum (`observed \| regulatory \| modeled \| aggregate \| administrative \| candidate \| synthetic`); USFWS critical habitat re-labeled `regulatory` (was "authority"); KDWP "review context" removed as a non-role. | reconciliation | Atlas §24.1.1 confirms the enum and the role of each source family. |
| Aligned `sensitivity_tier` vocabulary to the Atlas §24.5.1 names (`T0` Open … `T4` Denied), replacing the invented `T0_public … T4_withheld` labels. | reconciliation | Atlas §24.5.1 is the CONFIRMED tier scheme (PROPOSED for adoption per ADR-S-05). |
| Corrected `policy_decision_ref` to resolve to the `PolicyDecision` **record** (schema in `schemas/contracts/v1/policy/`), with the rule home `policy/domains/habitat/` noted separately. | clarification | Master MapLibre schema table places the decision-record schema under `schemas/`, not `policy/`. |
| Anchored the `release/` subtree (`manifests/`, `promotion_decisions/`, `rollback_cards/`, `correction_notices/`, `withdrawal_notices/`, `signatures/`, `attestations/`, `sbom/`, `candidates/`) and the decision-record schema homes to CONFIRMED evidence. | reconciliation | Repository guiding doc per-root README contract + Master MapLibre schema table. |
| Added `promotion_ref` to the index record schema (§4). | gap closure | `PromotionDecision` is a distinct authority record from the `ReleaseManifest`. |
| Added the correction-lineage reason codes (`CORRECTION_DERIVATIVES_UNRESOLVED`, `CORRECTION_PRIOR_RELEASE_MISSING`) to §8 and linked `REASON_CODES.md`. | gap closure | Atlas §24.6.3 names these correction-gate codes. |
| Split the prior combined §12 into §12 (Open questions register, `OQ-HAB-REL-NN`) and §13 (verification backlog); added §14 changelog + definition of done. | new | Companion-section pattern for standard/doctrine-adjacent docs. |
| Pinned `CONTRACT_VERSION = "3.0.0"` in meta block, badge row, and impact table; normalized object-family display names. | housekeeping | Required for doctrine-adjacent docs; ubiquitous-language stability. |
| Quoted all Mermaid edge labels containing `/`, `(`, `)`; simplified `stateDiagram` labels (removed `<br/>`). | housekeeping | Mermaid-safety rules. |
| Bumped version v1 → v1.1; `updated` → 2026-06-05. | housekeeping | MINOR bump: reconciliation + gap closure, no operating-law change. |

> **Backward compatibility.** Section anchors §1–§11 are preserved. The prior combined "Open questions and verification backlog" (§12) was split into §12 (register) and §13 (backlog); inbound links to `#12-open-questions-and-verification-backlog` should be repointed to `#12-open-questions-register`. The prior §13 "Related docs" is now §15.

### 14.2 Definition of done

This index is done enough to enter the repository when:

- it is placed per Directory Rules §12 (segment form), with the filename question (OQ-HAB-REL-01) and the HAB-V-009 path-form conflict logged in `docs/registers/DRIFT_REGISTER.md`;
- a docs steward, the habitat domain steward, and the release authority review it; sensitivity reviewer signs off on §6;
- it is linked from `docs/domains/habitat/README.md`, `release/README.md`, and the doctrine/standards index;
- the maintenance model (hand-curated vs generated — OQ-HAB-REL-02) is decided;
- it does not conflict with accepted ADRs (notably ADR-0001, ADR-S-09);
- the `GENERATED_RECEIPT.json` planned in the PR is wired into CI with `contract_version: "3.0.0"`;
- future changes follow the operating contract's §37 lifecycle.

[⬆ Back to top](#contents)

---

## 15. Related docs

- [`docs/domains/habitat/README.md`](README.md) — Habitat lane overview *(PROPOSED — `NEEDS VERIFICATION`)*
- [`docs/domains/habitat/PRESERVATION_MATRIX.md`](PRESERVATION_MATRIX.md) — per-object preservation tiers and transforms
- [`docs/domains/habitat/REASON_CODES.md`](REASON_CODES.md) — finite outcomes and reason codes referenced in §8 / §11
- [`docs/standards/PROV.md`](../../standards/PROV.md) — Provenance profile (W3C PROV-O / PAV)
- [`docs/standards/PMTILES.md`](../../standards/PMTILES.md) — PMTiles governance and conformance profile
- [`docs/standards/OGC-API-TILES.md`](../../standards/OGC-API-TILES.md) — OGC API Tiles delivery
- [`docs/standards/ISO-19115.md`](../../standards/ISO-19115.md) — ISO 19115 crosswalk
- [`docs/runbooks/fauna/SOURCE_REFRESH_RUNBOOK.md`](../../runbooks/fauna/SOURCE_REFRESH_RUNBOOK.md) — cross-lane reference for Fauna source-refresh discipline
- `release/README.md` — release authority root *(PROPOSED — `NEEDS VERIFICATION`)*
- `data/published/README.md` — published artifacts root *(PROPOSED — `NEEDS VERIFICATION`)*
- `data/registry/README.md` — registry root *(PROPOSED — `NEEDS VERIFICATION`)*
- `docs/registers/VERIFICATION_BACKLOG.md` — verification backlog *(PROPOSED — `NEEDS VERIFICATION`)*
- `docs/registers/DRIFT_REGISTER.md` — drift register *(PROPOSED — `NEEDS VERIFICATION`)*
- [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md) *(CONFIRMED doctrine; canonical path `PROPOSED`)*
- [`ai-build-operating-contract.md`](../../../ai-build-operating-contract.md) — canonical operating contract (`CONTRACT_VERSION = "3.0.0"`)

---

**Last updated:** 2026-06-05 · **Version:** v1.1 (draft) · **Contract:** `CONTRACT_VERSION = "3.0.0"` · **Authority:** navigational mirror only · [⬆ Back to top](#contents)
