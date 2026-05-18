<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/domains/hydrology/verification-backlog
title: Hydrology — Verification Backlog
type: standard
subtype: register
version: v1
status: draft
owners: <hydrology-domain-steward — TODO>; <release-manager — TODO>; <policy-admin — TODO>
created: 2026-05-18
updated: 2026-05-18
policy_label: public
related:
  - docs/domains/hydrology/README.md
  - docs/registers/VERIFICATION_BACKLOG.md
  - docs/registers/DRIFT_REGISTER.md
  - docs/registers/AUTHORITY_LADDER.md
  - docs/adr/ADR-0001-schema-home.md
  - directory-rules.md
tags: [kfm, hydrology, register, verification, governance, backlog]
notes:
  - "Domain-scoped backlog; rolls up into docs/registers/VERIFICATION_BACKLOG.md."
  - "All implementation-layer claims are PROPOSED until the repo is mounted and inspected."
  - "Cite-or-abstain applies; this file MUST NOT be cited as proof of implementation."
[/KFM_META_BLOCK_V2] -->

# Hydrology — Verification Backlog

Working register of unresolved and checkable items inside the hydrology domain lane. CONFIRMED doctrine, PROPOSED implementation. This is a backlog, not a release artifact.

![status](https://img.shields.io/badge/status-draft-yellow)
![type](https://img.shields.io/badge/type-register-blue)
![domain](https://img.shields.io/badge/domain-hydrology-1f6feb)
![authority](https://img.shields.io/badge/authority-implementation--bearing-lightgrey)
![policy](https://img.shields.io/badge/policy-public-brightgreen)
![truth](https://img.shields.io/badge/truth-CONFIRMED%20doctrine%20%2F%20PROPOSED%20impl-orange)
![updated](https://img.shields.io/badge/updated-2026--05--18-informational)

> **Status:** draft &middot; **Owners:** `<hydrology-domain-steward — TODO>` &middot; **Last reviewed:** `2026-05-18`

> [!NOTE]
> This register tracks **what would need to be true** for hydrology claims to advance through `RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED`. It records open verification items, not decisions. Decisions live in ADRs; receipts and proofs live in `data/receipts/` and `data/proofs/`. This page is a working list, not authority.

---

## Quick jump

- [1. Purpose & scope](#1-purpose--scope)
- [2. How to use this register](#2-how-to-use-this-register)
- [3. Verification-flow diagram](#3-verification-flow-diagram)
- [4. Status legend & priority scale](#4-status-legend--priority-scale)
- [5. Verification items](#5-verification-items)
  - [5.1 Source rights, terms, and freshness](#51-source-rights-terms-and-freshness)
  - [5.2 Identity, geometry, and crosswalk](#52-identity-geometry-and-crosswalk)
  - [5.3 Source-role separation](#53-source-role-separation)
  - [5.4 Catalog and proof closure](#54-catalog-and-proof-closure)
  - [5.5 Schema home and contracts](#55-schema-home-and-contracts)
  - [5.6 Policy, sensitivity, and life-safety boundary](#56-policy-sensitivity-and-life-safety-boundary)
  - [5.7 Governed API and renderer boundary](#57-governed-api-and-renderer-boundary)
  - [5.8 CI, validators, and rollback](#58-ci-validators-and-rollback)
  - [5.9 Watchers and delta detection](#59-watchers-and-delta-detection)
- [6. Negative fixtures expected (reference set)](#6-negative-fixtures-expected-reference-set)
- [7. Resolution paths](#7-resolution-paths)
- [8. Cross-references](#8-cross-references)
- [9. Change log](#9-change-log)

---

## 1. Purpose & scope

### Purpose

This file is the **hydrology lane's open-verification register**. It enumerates items that are `NEEDS VERIFICATION`, `UNKNOWN`, or `PROPOSED` for the hydrology domain, the evidence that would settle each, and which downstream gate or invariant the item unblocks. It feeds the global `docs/registers/VERIFICATION_BACKLOG.md` and is consumed by hydrology PRs as a checklist of "what's still open."

### What this register tracks

- Verification items specific to the **hydrology** lane (watersheds, HUC units, hydro features, reaches, gauges, flow/level observations, water quality, groundwater context, NFHL regulatory flood context, observed flood evidence). [CONFIRMED doctrine] [DOM-HYD] [ENCY]
- The evidence each item needs to be closed.
- The lifecycle gate, invariant, or release surface each item unblocks.

### What this register does **not** track

| Out of scope here | Lives in |
|---|---|
| Cross-domain backlog (non-hydrology) | `docs/registers/VERIFICATION_BACKLOG.md` |
| Cross-cutting doctrine drift | `docs/registers/DRIFT_REGISTER.md` |
| Final authority decisions | `docs/adr/` |
| Per-source rights, terms, cadence | `data/registry/sources/hydrology/` (PROPOSED) |
| Emitted run/release receipts | `data/receipts/`, `data/proofs/`, `release/` |
| Operational steps | `docs/runbooks/hydrology/` (PROPOSED) |

> [!IMPORTANT]
> This register is **not** the source of truth for whether something is implemented. The repository, its tests, workflows, and emitted receipts are. When this register and the repository disagree, the repository wins and a `DRIFT_REGISTER` entry is filed.

---

## 2. How to use this register

### Adding an item

1. Confirm the item is **hydrology-scoped**. Cross-domain items belong in the global backlog.
2. Pick the smallest narrowing of the claim that would settle it. "Verify hydrology" is too broad; "Verify `ReachIdentity` stability across NHDPlus refreshes" is the right size.
3. Assign one of: `NEEDS VERIFICATION`, `UNKNOWN`, `PROPOSED`. Never `CONFIRMED` (closed items are removed, not labeled closed).
4. State the evidence that would settle it (a file, a test, a manifest, a receipt, a workflow run, an ADR).
5. Link the gate, invariant, or release surface it unblocks.
6. Open a PR; reviewers check the placement and the resolution path.

### Closing an item

An item closes only when **all four** are present:

1. The named evidence is actually mounted or produced.
2. A reviewer with the relevant role has confirmed it.
3. Either an ADR or a PR (or both, for structural changes) carries the resolution.
4. Any released artifact that depended on the item has been re-validated.

When an item closes, remove it from §5 and add a one-line entry to §9 (Change log).

> [!TIP]
> If an item turns out to be unanswerable without an ADR, escalate it: file the ADR, link it here, and keep the item open until the ADR is `accepted`.

---

## 3. Verification-flow diagram

```mermaid
flowchart LR
    A["Open verification item<br/>NEEDS VERIFICATION / UNKNOWN / PROPOSED"]
    B{"Evidence available?"}
    C["Inspect repo / tests / workflows"]
    D["File ADR if structural"]
    E["Open PR with fixtures + validator + tests"]
    F{"All four closure conditions met?"}
    G["Remove from §5<br/>Log in §9"]
    H["Stays open; revisit at next review"]

    A --> B
    B -- "Yes" --> C
    B -- "No"  --> D
    C --> E
    D --> E
    E --> F
    F -- "Yes" --> G
    F -- "No"  --> H
    H --> B
```

> [!NOTE]
> **PROPOSED**. The diagram describes the intended workflow. Actual closure mechanics depend on repo conventions, CODEOWNERS, and ADR practice that are `NEEDS VERIFICATION` until the repository is mounted and inspected.

[Back to top](#hydrology--verification-backlog)

---

## 4. Status legend & priority scale

### Status labels (KFM truth posture)

| Label | Meaning |
|---|---|
| `CONFIRMED` | Verified this session from attached doctrine, repo evidence, tests, or receipts. Closed items are removed, not labeled `CONFIRMED` here. |
| `INFERRED` | Reasonably derivable from visible evidence but not directly stated. |
| `PROPOSED` | A design, path, or placement not yet verified in implementation. |
| `UNKNOWN` | Not resolvable without more evidence. |
| `NEEDS VERIFICATION` | Checkable, but not yet checked strongly enough to act as fact. |
| `EXTERNAL` | Sourced from authoritative external research; never applies to KFM-internal claims. |

Defined in the KFM truth posture; see `directory-rules.md` and the project doctrine. [CONFIRMED]

### Priority scale

| Priority | Meaning |
|---|---|
| **P0** | Blocks the first hydrology proof slice (Phase 1: `HydroFeature` + `GaugeObservation` + layer + drawer). [DOC-ENC §12; ENCY] |
| **P1** | Blocks publication of any hydrology layer or correction-bearing artifact. |
| **P2** | Important for lane health but does not block first publication. |
| **P3** | Hygiene, documentation, or future-proofing. |

---

## 5. Verification items

> [!NOTE]
> Every "Affects / unblocks" column links to a downstream gate or invariant that the item gates. IDs are stable within the hydrology lane; do not renumber on remove — leave gaps.

### 5.1 Source rights, terms, and freshness

| ID | Item | Evidence that would settle it | Status | Priority | Affects / unblocks |
|---|---|---|---|---|---|
| `HYD-VB-001` | Verify USGS WBD / HUC12 rights, license, and current terms. | `data/registry/sources/hydrology/wbd.source.yaml` (PROPOSED) with license, terms-of-use URL, cadence, and last-checked date. | NEEDS VERIFICATION | P0 | `SourceDescriptor` admission; RAW lane gate. |
| `HYD-VB-002` | Verify NHDPlus HR / 3DHP-oriented hydrography rights and terms. | `data/registry/sources/hydrology/nhdplus_hr.source.yaml` (PROPOSED). | NEEDS VERIFICATION | P0 | Crosswalk admission (§5.2). |
| `HYD-VB-003` | Verify USGS Water Data API (`api.waterdata.usgs.gov`) terms and confirm the legacy `waterservices.usgs.gov` phase-out window. | Current USGS Water Data API documentation; cutover date captured in source descriptor. The phase-out is referenced in project material as `2026 / 2027` but the exact cutover date is `NEEDS VERIFICATION`. | NEEDS VERIFICATION | P0 | Observation normalization (§5.3); endpoint stability. |
| `HYD-VB-004` | Verify FEMA NFHL / MSC rights and the strict requirement that NFHL stays **regulatory context**, not observed inundation. | Source descriptor + policy fixture asserting the role distinction; release-time validation refuses any release that collapses the two. | NEEDS VERIFICATION | P0 | Source-role anti-collapse invariant (§5.3). |
| `HYD-VB-005` | Verify 3DEP terrain rights and terrain-derived hydrology context handling. | Source descriptor; documented derivative posture. | NEEDS VERIFICATION | P1 | Terrain-derived hydrology layer publication. |
| `HYD-VB-006` | Verify state water office / KGS / groundwater well source rights and cadence. | Per-source descriptors under `data/registry/sources/hydrology/` (PROPOSED). | NEEDS VERIFICATION | P2 | `Groundwater Well` family release. |
| `HYD-VB-007` | Verify water-quality program rights (WQX / state programs). | Source descriptor + redaction posture for sensitive joins. | NEEDS VERIFICATION | P2 | `Water Quality Observation` release. |
| `HYD-VB-008` | Verify historical observed-flood evidence rights and provenance posture. | Source descriptor + review record for historical sources. | NEEDS VERIFICATION | P2 | `Observed Flood Event` release. |

### 5.2 Identity, geometry, and crosswalk

| ID | Item | Evidence that would settle it | Status | Priority | Affects / unblocks |
|---|---|---|---|---|---|
| `HYD-VB-010` | Verify the Kansas HUC12 fixture exists, validates, and carries `geometry_valid` + canonical digest. | A passing `tests/domains/hydrology/` fixture under `fixtures/domains/hydrology/valid/` (PROPOSED). | NEEDS VERIFICATION | P0 | Phase-1 hydrology thin slice. [ENCY] |
| `HYD-VB-011` | Verify COMID ↔ HUC12 crosswalk handling, including `ABSTAIN` behavior on ambiguous reach identity. | Crosswalk validator + valid/invalid fixtures + `decision_reason` enumeration (`official_crosswalk` / `area_weighted_overlay` / `centroid_in_polygon` / `snap_to_pour_point`). | NEEDS VERIFICATION | P0 | Phase-1 hydrology thin slice; ABSTAIN on ambiguity is the documented finite outcome. |
| `HYD-VB-012` | Verify NHDPlus version-drift handling (`v2.1` vs `HR`) is not silently mixed. | Manifest fields `nhdplus_version` and `wbd_snapshot` present and validator-enforced. | NEEDS VERIFICATION | P1 | Crosswalk reproducibility. |
| `HYD-VB-013` | Verify WBD snapshot lineage is carried on every crosswalk row. | Validator gate failing on missing `wbd_snapshot`. | NEEDS VERIFICATION | P1 | Cross-snapshot reproducibility. |
| `HYD-VB-014` | Verify `ReachIdentity` stability across upstream refreshes. | Identity rule test: same source + role + temporal scope + normalized digest → same identity. | NEEDS VERIFICATION | P1 | Identity invariant; promotion across refreshes. |
| `HYD-VB-015` | Define and verify the geometry-fingerprint canonicalization rule for hydrology geometries. | A documented canonicalization rule (likely JCS-canonicalized WKB digest); validator coverage; cross-lane parity with Spatial Foundation. | UNKNOWN | P1 | Cross-domain geometry comparison. |
| `HYD-VB-016` | Verify `coverage_scope` enforcement (e.g., `CONUS` vs non-CONUS) for the crosswalk validator. | Validator gate failing closed outside declared support. | NEEDS VERIFICATION | P2 | Out-of-scope publication denial. |
| `HYD-VB-017` | Verify multi-HUC candidate handling (`multi_huc_candidate: true` + ranked candidates) for coastal / braided systems. | Schema field + validator test. | NEEDS VERIFICATION | P2 | Edge-case correctness. |

### 5.3 Source-role separation

> [!IMPORTANT]
> The hydrology lane **MUST NOT** collapse: (a) NFHL regulatory flood zones, (b) observed inundation, (c) forecasts, and (d) emergency warnings into one truth class. This is a core doctrine constraint and a publication gate. [CONFIRMED] [DOM-HYD] [ENCY]

| ID | Item | Evidence that would settle it | Status | Priority | Affects / unblocks |
|---|---|---|---|---|---|
| `HYD-VB-020` | Verify NFHL regulatory zone vs observed inundation **role separation** at validator level. | Negative fixture: a record asserting NFHL is observed inundation MUST fail closed. | NEEDS VERIFICATION | P0 | Anti-collapse invariant. |
| `HYD-VB-021` | Verify forecast / observation / warning role distinction. | Source descriptor role field + validator + release-time refusal for cross-role asserts. | NEEDS VERIFICATION | P0 | Anti-collapse invariant; hazards boundary (§5.6). |
| `HYD-VB-022` | Verify the USGS Water normalizer preserves source role on every emitted observation. | Normalizer test on `FlowObservation` and `WaterLevelObservation`. | NEEDS VERIFICATION | P1 | `FlowObservation` / `WaterLevelObservation` release. |

### 5.4 Catalog and proof closure

| ID | Item | Evidence that would settle it | Status | Priority | Affects / unblocks |
|---|---|---|---|---|---|
| `HYD-VB-030` | Verify `EvidenceBundle` resolution for at least one `HydroFeature` claim. | A round-trip: `EvidenceRef` → `EvidenceBundle` → citation validation pass. | NEEDS VERIFICATION | P0 | Catalog closure; renderer boundary. |
| `HYD-VB-031` | Verify `ValidationReport` emission for one hydrology fixture run. | Emitted report under `data/proofs/` (PROPOSED) with required fields. | NEEDS VERIFICATION | P0 | Promotion gate. |
| `HYD-VB-032` | Verify `ReleaseManifest` closure for one published hydrology layer (HUC12 demo). | Manifest under `release/candidates/hydrology/` (PROPOSED) referencing `EvidenceBundle`, `PolicyDecision`, `PromotionDecision`, rollback target. | NEEDS VERIFICATION | P0 | First publication. |
| `HYD-VB-033` | Verify `RunReceipt` emission for a hydrology pipeline run. | Receipt under `data/receipts/` (PROPOSED) with input digests, config hash, transform, output artifacts, source roles, timestamp. | NEEDS VERIFICATION | P1 | Reproducibility audit. |
| `HYD-VB-034` | Verify rollback target is reachable for a hydrology release. | Rollback drill receipt; prior `MapReleaseManifest` restored. | NEEDS VERIFICATION | P1 | Reversibility invariant. |

### 5.5 Schema home and contracts

| ID | Item | Evidence that would settle it | Status | Priority | Affects / unblocks |
|---|---|---|---|---|---|
| `HYD-VB-040` | Resolve hydrology schema home: `schemas/contracts/v1/domains/hydrology/` (canonical per ADR-0001 default) vs `contracts/domains/hydrology/` (semantic Markdown only). | Live `ADR-0001` (or successor) accepted; schemas present at the canonical path. Per `directory-rules.md` §13.1, `schemas/contracts/v1/...` is the default canonical home; `contracts/` retains semantic Markdown. The hydrology realization remains PROPOSED until inspected. | PROPOSED | P0 | All hydrology contracts; cross-domain joins. |
| `HYD-VB-041` | Verify `HydroCrosswalkManifest` schema is reviewed, fingerprinted, and used by the crosswalk validator. | Schema file at canonical path + positive/negative fixtures. | NEEDS VERIFICATION | P1 | §5.2. |
| `HYD-VB-042` | Verify the canonical object-family schemas exist: `Watershed`, `HUCUnit`, `HydroFeature`, `ReachIdentity`, `GaugeSite`, `FlowObservation`, `WaterLevelObservation`, `Water Quality Observation`, `Groundwater Well`, `NFHLZone`, `Observed Flood Event`. | Schema files at the canonical home + fixture coverage. The 11 family names are CONFIRMED doctrine; their schema realizations are PROPOSED. [DOM-HYD] [ENCY] | NEEDS VERIFICATION | P1 | Catalog closure. |
| `HYD-VB-043` | Verify deterministic-identity rule (`source id + object role + temporal scope + normalized digest`) is implemented and tested for hydrology objects. | Identity test suite. The identity basis is CONFIRMED doctrine; the field-level realization is PROPOSED. | NEEDS VERIFICATION | P1 | Identity invariant. |
| `HYD-VB-044` | Verify temporal model carries source / observed / valid / retrieval / release / correction times distinctly where material. | Schema field presence + temporal-validation fixture. | NEEDS VERIFICATION | P1 | Time-aware UI; correction lineage. |

### 5.6 Policy, sensitivity, and life-safety boundary

> [!WARNING]
> KFM is **never** an alert authority. Emergency / life-safety warnings are hazards / official-source concerns, not hydrology outputs. Any hydrology release path that could be confused with an emergency channel must fail closed. [CONFIRMED] [DOM-HYD] [DOM-HAZ] [ENCY]

| ID | Item | Evidence that would settle it | Status | Priority | Affects / unblocks |
|---|---|---|---|---|---|
| `HYD-VB-050` | Verify sensitive-join handling (e.g., rare-species locations × hydrology) fails closed at the policy layer. | Policy fixture + `PolicyDecision` denial under `policy/domains/hydrology/` (PROPOSED). | NEEDS VERIFICATION | P0 | Cross-domain sensitivity invariant. |
| `HYD-VB-051` | Verify the life-safety / emergency-alert boundary is explicit in hydrology policy and release language. | Policy bundle + UI copy + release-time refusal of emergency-style framing. | NEEDS VERIFICATION | P0 | Life-safety invariant. |
| `HYD-VB-052` | Verify stale-state and freshness markers are surfaced for live hydrology layers (e.g., gauge offline → stale badge → ABSTAIN). | UI fixture + governed-API stale flag + tests. | NEEDS VERIFICATION | P1 | Trust-state UI. |

### 5.7 Governed API and renderer boundary

| ID | Item | Evidence that would settle it | Status | Priority | Affects / unblocks |
|---|---|---|---|---|---|
| `HYD-VB-060` | Verify hydrology routes flow through `apps/governed-api/` and not directly to canonical stores. | Route map + static check: no browser code imports raw-store / canonical-store clients. | NEEDS VERIFICATION | P0 | Trust-membrane invariant. [directory-rules.md §13] |
| `HYD-VB-061` | Verify the MapLibre hydrology `LayerManifest` adapter binds released layers only. | Layer manifest under `data/published/layers/hydrology/` (PROPOSED) + adapter test refusing unreleased layers. | NEEDS VERIFICATION | P0 | Renderer boundary; PR-06 in roadmap. |
| `HYD-VB-062` | Verify Evidence Drawer click-resolution for a hydrology feature returns a real `EvidenceBundle`. | Click → governed API → `EvidenceDrawerPayload` → `EvidenceBundle`; fixture test. | NEEDS VERIFICATION | P0 | Drawer behavior. |
| `HYD-VB-063` | Verify no-RAW / no-WORK / no-QUARANTINE load test passes for hydrology layers. | Static check + browser test. | NEEDS VERIFICATION | P0 | Trust membrane. |
| `HYD-VB-064` | Verify no-unreleased-tile-load test passes for hydrology. | Static check on `addSource` / `addLayer` artifact references; release-state validation. | NEEDS VERIFICATION | P0 | Release-state invariant. |
| `HYD-VB-065` | Verify time-aware behavior: source / retrieval / processing / release time fields distinguished in the time slider. | UI test with mixed time fields. | NEEDS VERIFICATION | P2 | Time slider correctness. |

### 5.8 CI, validators, and rollback

| ID | Item | Evidence that would settle it | Status | Priority | Affects / unblocks |
|---|---|---|---|---|---|
| `HYD-VB-070` | Verify negative fixtures exist for the hydrology validator (invalid HUC12 length, low alignment, missing provenance). | Fixtures under `fixtures/domains/hydrology/invalid/` (PROPOSED) + failing tests; see §6 for the reference set. | NEEDS VERIFICATION | P0 | Fail-closed posture. |
| `HYD-VB-071` | Verify `tools/validators/hydro/` exists, is invoked by CI, and emits machine-readable output. | Validator package + CI workflow + sample run on a fixture. | NEEDS VERIFICATION | P0 | All hydrology gates. |
| `HYD-VB-072` | Verify the hydrology rollback drill produces a `release/rollback/` card (PROPOSED) and restores the prior manifest. | Drill receipt; prior `ReleaseManifest` restored; cache invalidation recorded. | NEEDS VERIFICATION | P1 | Reversibility invariant. |
| `HYD-VB-073` | Verify hydrology `policy/domains/hydrology/*.rego` (PROPOSED) is mirrored from canonical policy authority and not divergent. | Policy parity check (CI = runtime). | NEEDS VERIFICATION | P1 | Policy invariant. |

### 5.9 Watchers and delta detection

| ID | Item | Evidence that would settle it | Status | Priority | Affects / unblocks |
|---|---|---|---|---|---|
| `HYD-VB-080` | Verify streamflow-anomaly watcher gates (e.g., sustained anomaly `>3×` 7-day median, consecutive days above site historic 95th percentile) emit **observations / candidate decisions only** — never publish. | Watcher contract + receipt schema + negative test asserting watcher cannot mutate catalog. | NEEDS VERIFICATION | P2 | Watcher-as-non-publisher invariant. |
| `HYD-VB-081` | Verify NHD / WBD delta watcher behavior (additions, deletions, geometry shifts) emits proposed-work records, not direct catalog edits. | Delta-watcher contract + drift test. | NEEDS VERIFICATION | P2 | Lifecycle integrity. |
| `HYD-VB-082` | Verify thresholds and seeds are documented and not silently tunable (anti silent-threshold-drift). | Threshold file under version control + change-discipline tests. | NEEDS VERIFICATION | P2 | Reproducibility. |

[Back to top](#hydrology--verification-backlog)

---

## 6. Negative fixtures expected (reference set)

The crosswalk validator's fail-closed posture requires negative fixtures. The set below is **PROPOSED** and serves as a reference for §5.2 and §5.8 items. Final fixture content depends on schema realization.

<details>
<summary><strong>Reference negative-fixture set (PROPOSED)</strong></summary>

| Fixture | Trigger | Expected outcome |
|---|---|---|
| `missing_huc12_field` | Row omits `huc12`. | `FAIL_MISSING_HUC12` |
| `invalid_huc12_length` | `huc12` is not 12 digits (e.g., `"10270101"`). | `FAIL_INVALID_HUC12` |
| `low_alignment_heuristic` | `decision_reason: area_weighted_overlay` with `alignment_score < 0.75`. | `FAIL_LOW_ALIGNMENT` |
| `missing_provenance` | No `source_head` / `algorithm_version`. | `FAIL_MISSING_PROVENANCE` |
| `missing_spec_hash` | No `spec_hash`. | `FAIL_MISSING_SPEC_HASH` |
| `unstable_identity` | Different output for same input across runs. | `FAIL_IDENTITY_DRIFT` |
| `nfhl_as_observed` | NFHL record asserted as observed inundation. | `FAIL_ROLE_COLLAPSE` |
| `mixed_nhdplus_versions` | `v2.1` and `HR` rows merged with no version field. | `FAIL_VERSION_DRIFT` |
| `out_of_scope_coverage` | Row asserts non-`CONUS` without explicit support. | `FAIL_OUT_OF_SCOPE` |
| `unreleased_layer_load` | Browser/test attempts to load a layer without `ReleaseManifest`. | `FAIL_NO_RELEASE_MANIFEST` |
| `raw_path_access` | Code path reads from `data/raw/hydrology/` directly. | `FAIL_TRUST_MEMBRANE` |

Negative fixtures are essential, not optional. Validators that pass every positive case but fail closed on no negative case do not prove the trust spine.

</details>

> [!CAUTION]
> Validator behavior described above is **PROPOSED**. Until the validator package and its CI integration are inspected in a mounted repo, outcomes (`FAIL_*` codes, finite-outcome enumeration) are illustrative and `NEEDS VERIFICATION`.

[Back to top](#hydrology--verification-backlog)

---

## 7. Resolution paths

| Item type | Smallest reversible resolution |
|---|---|
| Source rights / terms / freshness (§5.1) | Author a `SourceDescriptor` under `data/registry/sources/hydrology/` (PROPOSED), link it from the hydrology README. |
| Identity / crosswalk (§5.2) | Add a positive fixture, a negative fixture, and a validator gate; link both from the validator README. |
| Source-role separation (§5.3) | Add a negative fixture asserting the collapse case; tests must fail closed before validator emits ANSWER. |
| Catalog / proof closure (§5.4) | Run the no-network fixture chain end-to-end; produce `RunReceipt`, `ValidationReport`, `EvidenceBundle`, `PromotionDecision`, `ReleaseManifest`. |
| Schema home (§5.5) | Resolve via ADR (default per `directory-rules.md` §13.1 is `schemas/contracts/v1/`); add a drift entry if the repo disagrees. |
| Policy / sensitivity (§5.6) | Add policy fixture + `PolicyDecision` deny case under `policy/domains/hydrology/` (PROPOSED). |
| Governed API / renderer (§5.7) | Add a static check that browser code does not import canonical-store clients; add a test that `addSource`/`addLayer` refuses unreleased artifacts. |
| CI / validators / rollback (§5.8) | Add the validator under `tools/validators/hydro/`, wire it into CI, run a rollback drill. |
| Watchers / deltas (§5.9) | Define watcher contract; assert watcher emits receipts and candidate decisions only. |

> [!NOTE]
> "Smallest reversible resolution" reflects the change-discipline default: contracts, schemas, adapters, validators, registries, receipts, ADRs, tests, and docs tied to behavior. Broad rewrites are acceptable when explicitly requested.

[Back to top](#hydrology--verification-backlog)

---

## 8. Cross-references

### Within hydrology

- `docs/domains/hydrology/README.md` — domain landing page (PROPOSED).
- `docs/domains/hydrology/CROSSWALK_RULES.md` — COMID ↔ HUC12 rules (PROPOSED).
- `docs/runbooks/hydrology/SOURCE_REFRESH_RUNBOOK.md` — source refresh lifecycle (PROPOSED; pattern mirrors the fauna runbook).
- `tools/validators/hydro/README.md` — validator package README (PROPOSED).
- `contracts/domains/hydrology/` — semantic Markdown (PROPOSED).
- `schemas/contracts/v1/domains/hydrology/` — canonical schemas (PROPOSED, pending ADR-0001 confirmation).

### Cross-cutting registers

- `docs/registers/VERIFICATION_BACKLOG.md` — global rollup; this file is its hydrology slice.
- `docs/registers/DRIFT_REGISTER.md` — file an entry when this register and the repo disagree.
- `docs/registers/AUTHORITY_LADDER.md` — authority order.
- `docs/registers/CANONICAL_LINEAGE_EXPLORATORY.md` — canon vs lineage classification.

### ADRs likely to touch this lane

- `ADR-0001` — schema home (`schemas/contracts/v1/...` canonical).
- `ADR-<TODO>` — hydrology source-role anti-collapse (PROPOSED, name pending).
- `ADR-<TODO>` — NHDPlus version-pinning policy (PROPOSED).

### Directory Rules basis

- `directory-rules.md` §4 (Placement Protocol), §12 (Domain Placement Law), §13 (Anti-Patterns), §15 (README Contract), §18 (Open Questions). [CONFIRMED]

### Doctrine / source citations

- `[DOM-HYD]` — Hydrology dossier (KFM Domains Culmination Atlas v1.1).
- `[ENCY]` — KFM Domain and Capability Encyclopedia.
- `[MAP-MASTER]` — Master MapLibre Components / Functions / Features.
- `[UNIFIED]` — KFM Unified Implementation Architecture Build Manual.
- `[DOC-DIR]` — `directory-rules.md`.

[Back to top](#hydrology--verification-backlog)

---

## 9. Change log

| Date | Item | Change | Reviewer |
|---|---|---|---|
| 2026-05-18 | n/a | Initial draft; all items opened in `NEEDS VERIFICATION` / `UNKNOWN` / `PROPOSED` state. | `<TODO>` |

---

<sub>**Related docs:** [`docs/domains/hydrology/README.md`](README.md) · [`docs/registers/VERIFICATION_BACKLOG.md`](../../registers/VERIFICATION_BACKLOG.md) · [`docs/registers/DRIFT_REGISTER.md`](../../registers/DRIFT_REGISTER.md) · [`directory-rules.md`](../../../directory-rules.md) · [`docs/adr/`](../../adr/)</sub>

<sub>**Last updated:** 2026-05-18 &middot; **Authority:** implementation-bearing register, not an ADR &middot; **Truth posture:** CONFIRMED doctrine / PROPOSED implementation &middot; [Back to top](#hydrology--verification-backlog)</sub>
