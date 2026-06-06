<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs/domains/hazards/release_index
title: Hazards Release Index
type: standard
version: v2
status: draft
owners: <docs-steward> · <hazards-domain-steward> · <release-manager>
created: 2026-05-17
updated: 2026-06-05
policy_label: public
related:
  - ai-build-operating-contract.md
  - docs/domains/hazards/README.md
  - docs/domains/hazards/PUBLICATION_AND_BOUNDARY.md
  - docs/domains/hazards/PRESERVATION_MATRIX.md
  - docs/domains/hazards/MISSING_OR_PLANNED_FILES.md
  - docs/doctrine/directory-rules.md
  - docs/standards/PROV.md
  - docs/standards/PMTILES.md
  - docs/standards/OGC-API-TILES.md
  - docs/standards/ISO-19115.md
  - release/README.md
  - release/candidates/hazards/
  - release/manifests/
  - release/rollback_cards/
  - release/correction_notices/
  - release/withdrawal_notices/
  - data/published/layers/hazards/
  - data/catalog/domain/hazards/
tags: [kfm, hazards, release, index, lifecycle, governance, not-for-life-safety]
notes:
  # CONTRACT_VERSION = "3.0.0" (ai-build-operating-contract.md v3.0)
  # Docs-side index — NOT a canonical release decision artifact.
  # Hazards is contextual / planning — NOT a life-safety alerting surface; alert authority is T4 forever (Atlas 24.5.2).
  # Most implementation claims are PROPOSED until repo evidence confirms them.
  # v2 aligns source-role vocabulary to the canonical seven-class enum (Atlas 24.1.1) and reconciles the lane tree to Directory Rules 9.1.
[/KFM_META_BLOCK_V2] -->

# 🌪️ Hazards Release Index

> Navigation hub and audit-friendly registry for **Hazards domain releases** — candidates, published, corrected, withdrawn, and superseded — and the `ReleaseManifest`, `PromotionDecision`, `RollbackCard`, `CorrectionNotice`, and `WithdrawalNotice` artifacts that govern them.

![status](https://img.shields.io/badge/status-draft-orange)
![doc--type](https://img.shields.io/badge/doc--type-standard-blue)
![domain](https://img.shields.io/badge/domain-hazards-7E2F2F)
![contract](https://img.shields.io/badge/CONTRACT__VERSION-3.0.0-blueviolet)
![lifecycle](https://img.shields.io/badge/lifecycle-RAW%E2%86%92PUBLISHED-2C7A7B)
![policy](https://img.shields.io/badge/policy-public--safe%20default-2F855A)
![life--safety](https://img.shields.io/badge/life--safety-NOT%20FOR%20ALERTING-B91C1C)
![build](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** `draft` · **Owners:** `<docs-steward>` · `<hazards-domain-steward>` · `<release-manager>` · **Last updated:** `2026-06-05` · **Pins:** `CONTRACT_VERSION = "3.0.0"`

> [!CAUTION]
> **KFM Hazards is *not* an emergency-alerting system and *not* a regulatory authority.** Released hazards layers are historical, regulatory-context, modeled, or planning-context evidence — never current life-safety guidance. Direct life-safety needs to official sources (NWS, FEMA, state emergency management, local 911). This boundary is doctrine — pinned at the strongest tier (**alert authority = T4 forever, no transform**, Atlas §24.5.2) — and every release listed below MUST carry the *"planning context, not alerting"* label on every public surface.

---

## Contents

- [1. Purpose & scope](#1-purpose--scope)
- [2. What this index is — and is not](#2-what-this-index-is--and-is-not)
- [3. Repo fit & where artifacts actually live](#3-repo-fit--where-artifacts-actually-live)
- [4. Hazards release scope — artifact families](#4-hazards-release-scope--artifact-families)
- [5. Hazards release lifecycle](#5-hazards-release-lifecycle)
- [6. Release state vocabulary](#6-release-state-vocabulary)
- [7. Active releases registry](#7-active-releases-registry)
- [8. Candidate releases registry](#8-candidate-releases-registry)
- [9. Corrected, withdrawn, and superseded releases](#9-corrected-withdrawn-and-superseded-releases)
- [10. Per-layer release lineage](#10-per-layer-release-lineage)
- [11. Catalog / proof / release closure for Hazards](#11-catalog--proof--release-closure-for-hazards)
- [12. Sensitivity, rights, and the life-safety boundary](#12-sensitivity-rights-and-the-life-safety-boundary)
- [13. Promotion gates and decisions](#13-promotion-gates-and-decisions)
- [14. Correction and rollback path](#14-correction-and-rollback-path)
- [15. Source drift, watchers, and freshness](#15-source-drift-watchers-and-freshness)
- [16. Validators, tests, and fixtures](#16-validators-tests-and-fixtures)
- [17. Open questions & verification backlog](#17-open-questions--verification-backlog)
- [Related docs](#related-docs)

---

## 1. Purpose & scope

**CONFIRMED doctrine / PROPOSED implementation.** This index is the **human-facing entry point** for Hazards domain releases. It indexes — but never replaces — the canonical decision artifacts that live under `release/` and the released artifacts under `data/published/layers/hazards/`.

For any Hazards layer, dataset, evidence bundle, or report that has been promoted to `PUBLISHED` (or is a candidate, corrected, withdrawn, or superseded version of one), this document answers:

- **Where is its `ReleaseManifest`?** *(under [`release/manifests/`](../../../release/manifests/))*
- **What `PromotionDecision`, `RollbackCard`, `CorrectionNotice`, or `WithdrawalNotice` governs it?** *(under the corresponding `release/` subfolder)*
- **What `EvidenceBundle`, `RunReceipt`, and `ValidationReport` close its catalog?** *(under [`data/proofs/`](../../../data/proofs/), [`data/receipts/`](../../../data/receipts/), and [`data/catalog/domain/hazards/`](../../../data/catalog/domain/hazards/))*
- **What is its current state, vintage, source-role posture, sensitivity posture, and rollback target?**

This index is **not** a regulatory record, not a CDN cache controller, and not a substitute for the canonical artifacts it points to.

[⬆ back to top](#contents)

---

## 2. What this index is — and is not

| | **Is** | **Is not** |
|---|---|---|
| **Authority** | A docs-side navigation and audit hub for Hazards releases | The release decision authority — that role belongs to `release/manifests/` plus `release/promotion_decisions/` (CONFIRMED doctrine, [Directory Rules §9.2](../../doctrine/directory-rules.md)) |
| **Scope** | All Hazards artifact families: events, contexts, declarations, detections, summaries, timelines, tiles, drawer payloads, AI envelopes | Hazards source-edge captures (those live in `data/raw/hazards/`) and quarantined material (`data/quarantine/hazards/`) |
| **Trust posture** | Cite-or-abstain; release-state visible per row | A truth store, citation authority, or rights authority |
| **Alerting** | A history of planning-context hazards artifacts | A live alerting feed, a watch/warning publisher, or a regulatory determination |
| **Maintenance** | Updated whenever a Hazards release is promoted, corrected, rolled back, withdrawn, or superseded | Auto-generated from the registry; **PROPOSED**: a CI job under [`tools/docs/`](../../../tools/) could regenerate the registry tables from `release/manifests/` and `data/catalog/domain/hazards/` (NEEDS VERIFICATION). |

> [!NOTE]
> Where this index conflicts with the canonical `release/` artifacts, **the canonical artifacts win**. Open a drift entry in [`docs/registers/DRIFT_REGISTER.md`](../../registers/DRIFT_REGISTER.md) and reconcile.

[⬆ back to top](#contents)

---

## 3. Repo fit & where artifacts actually live

This document sits inside the **Hazards docs lane** per [Domain Placement Law §12](../../doctrine/directory-rules.md). It is one file in a family of Hazards-lane artifacts spread across responsibility roots. The diagram below shows what this index points *to*, not what it owns.

```mermaid
flowchart LR
  subgraph DOC["docs/domains/hazards/ (this lane)"]
    IDX["RELEASE_INDEX.md (this file)"]
    RDM["README.md"]
    PB["PUBLICATION_AND_BOUNDARY.md"]
    PM["PRESERVATION_MATRIX.md"]
  end

  subgraph REL["release/ — release DECISIONS"]
    CAND["release/candidates/hazards/ — candidate dossiers"]
    MAN["release/manifests/ — ReleaseManifest by release_id"]
    PRO["release/promotion_decisions/ — PromotionDecision records"]
    RBK["release/rollback_cards/"]
    CN["release/correction_notices/"]
    WN["release/withdrawal_notices/"]
    SIG["release/signatures/ — DSSE / Sigstore"]
    CHG["release/changelog/"]
  end

  subgraph DATA["data/ — release ARTIFACTS & proof"]
    PUB["data/published/layers/hazards/ — public-safe outputs"]
    CAT["data/catalog/domain/hazards/ — STAC / DCAT / PROV"]
    PR["data/proofs/ — EvidenceBundle / ProofPack"]
    RC["data/receipts/ — RunReceipt / release receipts"]
    RBD["data/rollback/hazards/ — rollback revert receipts"]
    REG["data/registry/sources/hazards/"]
  end

  IDX -->|"indexes"| MAN
  IDX -->|"indexes"| CAND
  IDX -->|"indexes"| PRO
  IDX -->|"indexes"| RBK
  IDX -->|"indexes"| CN
  IDX -->|"indexes"| WN
  IDX -->|"points to artifacts"| PUB
  IDX -->|"points to closure"| CAT
  IDX -->|"points to closure"| PR
  IDX -->|"points to closure"| RC

  classDef thisFile fill:#FEF3C7,stroke:#B45309,color:#7C2D12;
  class IDX thisFile;
```

> [!IMPORTANT]
> **`data/published/` holds released artifacts. `release/` holds release decisions.** Mixing the two is one of the four primary drift patterns called out in [Directory Rules §13.2](../../doctrine/directory-rules.md). A ReleaseManifest does **not** live in `data/published/`; a published PMTiles file does **not** live in `release/`. Rollback **cards** (the decision) live in `release/rollback_cards/`; rollback **revert receipts** (the data event) live in `data/rollback/hazards/<release_id>/`. _(CONFIRMED: Directory Rules §9.1, §9.2.)_

### Hazards lane at a glance

```text
docs/domains/hazards/                  # human-facing (this lane)
  ├── README.md                        # domain overview                  [PROPOSED]
  ├── RELEASE_INDEX.md                 # ← this file                      [PROPOSED]
  ├── PUBLICATION_AND_BOUNDARY.md      # publication path + boundary      [PROPOSED]
  ├── PRESERVATION_MATRIX.md           # preservation per stage/tier      [PROPOSED]
  └── ...                              # other Hazards docs               [PROPOSED]

contracts/domains/hazards/             # object meaning                   [PROPOSED]
schemas/contracts/v1/domains/hazards/  # object shape (per ADR-0001)      [PROPOSED]
policy/domains/hazards/                # admissibility / release policy   [PROPOSED]
policy/release/hazards/                # release-gate .rego (alt home, §13.5; ADR-HAZ-07) [PROPOSED]
tests/domains/hazards/                 # enforceability proof             [PROPOSED]
fixtures/domains/hazards/              # golden / valid / invalid inputs  [PROPOSED]
packages/domains/hazards/              # shared domain libraries          [PROPOSED]
pipelines/domains/hazards/             # executable pipeline logic        [PROPOSED]
pipeline_specs/hazards/                # declarative pipeline config      [PROPOSED]

data/raw/hazards/                      # immutable intake captures        [PROPOSED]
data/work/hazards/                     # normalized intermediates         [PROPOSED]
data/quarantine/hazards/               # failed validation / sensitivity  [PROPOSED]
data/processed/hazards/                # validated canonical records      [PROPOSED]
data/catalog/domain/hazards/           # STAC / DCAT / PROV               [PROPOSED]
data/triplets/                         # graph deltas / exports (shared)  [PROPOSED]
data/published/layers/hazards/         # released public-safe artifacts   [PROPOSED]
data/rollback/hazards/                 # rollback revert receipts         [PROPOSED]
data/registry/sources/hazards/         # source descriptors / cadence     [PROPOSED]

release/candidates/hazards/            # candidate release dossiers       [PROPOSED]
release/manifests/                     # ReleaseManifests (all domains)   [PROPOSED]
release/promotion_decisions/           # PromotionDecisions               [PROPOSED]
release/rollback_cards/                # rollback decision cards          [PROPOSED]
release/correction_notices/            # public correction notices        [PROPOSED]
release/withdrawal_notices/            # withdrawal records               [PROPOSED]
release/signatures/                    # DSSE / Sigstore artifacts        [PROPOSED]
release/changelog/                     # release-level changelog          [PROPOSED]
```

> **Status reminder.** Per [Directory Rules §5](../../doctrine/directory-rules.md), the **rules** here are CONFIRMED (the `release/` and `data/` trees above match §9.1 / §9.2 verbatim); the **specific paths actually existing in the mounted repo** are PROPOSED until verified.

[⬆ back to top](#contents)

---

## 4. Hazards release scope — artifact families

**CONFIRMED doctrine.** The Hazards domain releases the following artifact families, each of which appears in this index when promoted to `PUBLISHED`. Object identities and source roles are governed elsewhere; this index records *release state*, not *truth*.

> [!NOTE]
> **Source-role vocabulary (v2).** Roles below use the canonical seven-class anti-collapse enum — `observed · regulatory · modeled · aggregate · administrative · candidate · synthetic` — set at admission and never upgraded by promotion. _(CONFIRMED: Atlas §24.1.1; vocabulary is ADR-class as ADR-S-04.)_ The informal four-way shorthand (`authority/observation/context/model`) from the §12.D dossier column is reconciled to this enum throughout.

<details>
<summary><strong>4.1 Canonical object families (released as derivatives, not as raw evidence)</strong></summary>

| Object family | Public release form (illustrative) | Sensitivity default | Source role (canonical, §24.1.1) |
|---|---|---|---|
| `HazardEvent` | Historical event point/line/polygon with attribution and time | T0 public-safe (with caveats) | `observed` / `administrative` — never alert |
| `HazardObservation` | Sensor or report observation tied to a source | T0 public-safe with provenance | `observed` — never relabeled regulatory |
| `WarningContext` | NWS warning footprint as **historical/contextual** record only | public-safe + *"not for life safety"*; T3 for any current use | `observed`/`administrative` presented as context — never current alert |
| `AdvisoryContext` | NWS advisory footprint as **historical/contextual** record only | public-safe + *"not for life safety"*; T3 for any current use | `observed`/`administrative` presented as context — never current alert |
| `DisasterDeclaration` | FEMA / state declaration record | T0 public-safe | `administrative` (+ `regulatory` where binding) |
| `FloodContext` | FEMA NFHL polygons as **regulatory context** | public-safe + *"regulatory context, verify with authority"* | `regulatory` — not a site-specific determination |
| `WildfireDetection` | NASA FIRMS / NOAA HMS detection points/polygons | T0 public-safe | `observed` (detection) — never alert |
| `SmokeContext` | NOAA HMS smoke polygons | T0 public-safe + provisional/expired badging | `observed` / `modeled` |
| `DroughtIndicator` | U.S. Drought Monitor / state monitor index | T0 public-safe | `modeled` / `aggregate` |
| `EarthquakeEvent` | USGS earthquake catalog event | T0 public-safe | `observed` |
| `HeatColdEvent` | Heat / cold event records and indices | T0 public-safe + caveats | `observed` / `modeled` |
| `ExposureSummary` | Population, infrastructure, asset exposure summary | review-gated; **T4 when critical-infrastructure detail implied**; aggregate-only by default | `modeled` / `aggregate` (derived) |
| `ResilienceSummary` | Resilience plan / capacity summary | review-gated | `modeled` / `aggregate` |
| `HazardTimeline` | Multi-event timeline overlay | T0 public-safe | `modeled` (derived) |
| `ImpactArea` | Impact polygon (historical / modeled) | review-gated when joined to sensitive lanes | `modeled` (derived) |

Citations: hazards object families per the KFM Domain & Capability Encyclopedia §7.10 and the Domains Culmination Atlas §12.

</details>

<details>
<summary><strong>4.2 Map / tile / drawer / AI artifact families</strong></summary>

| Artifact family | Carrier | Bound by |
|---|---|---|
| Hazards `LayerManifest` | one per public layer | `ReleaseManifest`, `SourceDescriptor`, `EvidenceBundle`, policy posture |
| Hazards PMTiles archive | versioned filename, root-hash sidecar | `TileArtifactManifest`, attestation, rollback target |
| Hazards COG raster (e.g., drought index, smoke) | versioned filename, checksum | `TileArtifactManifest` / raster manifest |
| Hazards STAC items / collections | one per dataset bundle | `kfm:` profile (PROPOSED) — see [PMTILES](../../standards/PMTILES.md) and [ISO-19115](../../standards/ISO-19115.md) |
| Hazards Evidence Drawer payload | per feature click | `EvidenceDrawerPayload` + `EvidenceBundle` projection |
| Hazards Focus Mode answer | per AI request | Runtime Response Envelope + `AIReceipt`; **ABSTAIN** if evidence is insufficient; **DENY** if life-safety / regulatory / sensitivity is implicated |

> [!NOTE]
> Map artifacts are **downstream carriers**, not authorities. Tiles, layers, and drawer payloads consume releases — they do not produce them. The renderer-boundary doctrine lives in the Master MapLibre source; renderer access goes through `packages/maplibre-runtime/` (Directory Rules §7.2.a, v1.3).

</details>

[⬆ back to top](#contents)

---

## 5. Hazards release lifecycle

**CONFIRMED doctrine: `RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED`. Promotion is a governed state transition, not a file move.** ([Directory Rules §9.1](../../doctrine/directory-rules.md) / [ENCY Appendix E].)

```mermaid
flowchart LR
  SRC[("Hazards source feeds")]:::ext
  RAW["RAW — data/raw/hazards/"]
  WORK["WORK — data/work/hazards/"]
  QUAR["QUARANTINE — data/quarantine/hazards/ — unknown role · rights · sensitivity · expiry"]:::quar
  PROC["PROCESSED — data/processed/hazards/ + receipts + proofs"]
  CAT["CATALOG / TRIPLET — data/catalog/domain/hazards/ — STAC · DCAT · PROV closure"]
  CAND["release/candidates/hazards/ — candidate dossier"]
  PUB["PUBLISHED — data/published/layers/hazards/ + release/manifests/"]:::pub
  COR["PUBLISHED-prime (corrected)"]
  SUP["SUPERSEDED"]:::endst
  WD["WITHDRAWN"]:::endst
  RBK["ROLLBACK — release/rollback_cards/"]:::endst

  SRC -->|"SourceDescriptor + rights/role/cadence"| RAW
  RAW --> WORK
  RAW -. fail-closed .-> QUAR
  QUAR -. remediate .-> WORK
  WORK -->|"ValidationReport · PolicyDecision"| PROC
  PROC -->|"EvidenceBundle · RunReceipt · catalog closure"| CAT
  CAT --> CAND
  CAND -->|"PromotionDecision (separation of duties)"| PUB
  PUB -. CorrectionNotice .-> COR
  PUB -. WithdrawalNotice .-> WD
  PUB -. RollbackCard .-> RBK
  RBK -. restores prior .-> PUB
  COR -. supersedes .-> SUP

  classDef ext fill:#F3F4F6,stroke:#6B7280,color:#374151;
  classDef pub fill:#DCFCE7,stroke:#15803D,color:#14532D;
  classDef quar fill:#FEE2E2,stroke:#B91C1C,color:#7F1D1D;
  classDef endst fill:#FEF3C7,stroke:#B45309,color:#7C2D12;
```

### Hazards lifecycle gate table

| Transition | Pre-condition | Required artifacts (PROPOSED minimum) | Fail-closed outcome | Status |
|---|---|---|---|---|
| Admission (`— → RAW`) | `SourceDescriptor` exists; rights/role/cadence set | `SourceDescriptor`; payload hash | source not admitted; logged as candidate | PROPOSED |
| Normalization (`RAW → WORK / QUARANTINE`) | schema, geometry, time, identity, evidence, rights, policy rules are runnable | `TransformReceipt`; `ValidationReport`; `PolicyDecision` | quarantine with reason; never silent promote | PROPOSED |
| Validation (`WORK → PROCESSED`) | deterministic validators tied to fixtures | `ValidationReport` pass; `RedactionReceipt` if sensitivity | stay in WORK; structured FAIL | PROPOSED |
| Catalog closure (`PROCESSED → CATALOG / TRIPLET`) | `EvidenceRef` resolves; catalog matrix + digests close | `CatalogMatrix`; `EvidenceBundle`; graph/triplet | HOLD at PROCESSED; no public edge | PROPOSED |
| Release (`CATALOG → PUBLISHED`) | Review state where required; release authority distinct from author when materiality applies | `ReleaseManifest`; rollback target; correction path; `ReviewRecord` | HOLD at CATALOG; no public surface change | PROPOSED |
| Correction (`PUBLISHED → PUBLISHED'`) | Detected error or new evidence; downstream derivatives identified | `CorrectionNotice`; new manifest; derivative invalidation | superseded with public notice | PROPOSED |
| Rollback (`PUBLISHED → prior PUBLISHED`) | Rollback target named in release | `RollbackCard`; cache invalidation; revert receipt in `data/rollback/hazards/` | retraction with rollback receipt | PROPOSED |

Sources: KFM Domains Culmination Atlas §24.6.1; Encyclopedia §7.10.H; Idea Index `KFM-IDX-REL-001`..`KFM-IDX-REL-005`.

[⬆ back to top](#contents)

---

## 6. Release state vocabulary

**CONFIRMED doctrine.** The `release_state` enumeration is shared across KFM and surfaced consistently in `kfm:` profile fields (PROPOSED for finalization in the STAC profile). Hazards releases inherit this vocabulary without modification.

| State | Meaning | Visible on public UI? | Allowed transitions |
|---|---|---|---|
| `unreleased` | Internal candidate; never on the public path | No | `→ candidate`, `→ withdrawn (pre-release)` |
| `candidate` | Dossier under `release/candidates/hazards/`; awaiting `PromotionDecision` | No | `→ released`, `→ withdrawn (pre-release)` |
| `released` | Promoted with valid `ReleaseManifest`; on the public path | Yes (with trust badges) | `→ corrected`, `→ superseded`, `→ withdrawn`, `→ rolled back` |
| `corrected` | Replaced by a corrected version after a `CorrectionNotice` | Yes (corrected badge + notice) | `→ superseded`, `→ withdrawn` |
| `superseded` | A newer release exists; historical record retained | Yes (superseded badge) | `→ withdrawn` (rare) |
| `withdrawn` | Removed from the public path via `WithdrawalNotice`; history retained | Public notice; layer hidden | terminal |

> [!IMPORTANT]
> **Rollback does not silently delete history.** A rollback retracts public visibility of one release in favor of a prior `ReleaseManifest` and emits a `RollbackCard`. The original release record stays on file under `release/manifests/` (CONFIRMED doctrine: [ENCY Appendix E], `KFM-IDX-REL-004`).

[⬆ back to top](#contents)

---

## 7. Active releases registry

> [!NOTE]
> **PROPOSED template.** No live Hazards releases are CONFIRMED in this session. The rows below are illustrative placeholders showing the schema each row should follow when populated. **NEEDS VERIFICATION** against the mounted repo before any row is treated as fact.

| Release ID | Layer / artifact | Vintage | `release_state` | Source role (§24.1.1) | Sensitivity | `ReleaseManifest` | `PromotionDecision` | Rollback target | Last reviewed |
|---|---|---|---|---|---|---|---|---|---|
| `hazards-r0001` *(PROPOSED)* | `hazards-historical-events-ks` | 1950–2024 | `released` *(PROPOSED)* | `observed` / `administrative` | T0 public-safe | `release/manifests/hazards-r0001.yaml` *(PROPOSED)* | `release/promotion_decisions/hazards-r0001.yaml` *(PROPOSED)* | — *(first release)* | `<YYYY-MM-DD>` |
| `hazards-r0002` *(PROPOSED)* | `hazards-nfhl-context-ks` | NFHL `<vintage>` | `released` *(PROPOSED)* | `regulatory` | public-safe + *"verify with authority"* | `release/manifests/hazards-r0002.yaml` *(PROPOSED)* | `release/promotion_decisions/hazards-r0002.yaml` *(PROPOSED)* | — | `<YYYY-MM-DD>` |
| `hazards-r0003` *(PROPOSED)* | `hazards-firms-detections-ks` | `<rolling cadence>` | `released` *(PROPOSED)* | `observed` (detection) | public-safe + provisional badging | `release/manifests/hazards-r0003.yaml` *(PROPOSED)* | `release/promotion_decisions/hazards-r0003.yaml` *(PROPOSED)* | — | `<YYYY-MM-DD>` |

> [!TIP]
> **First credible thin slice** for Hazards (CONFIRMED, KFM Encyclopedia §7.10 / Atlas §12): a historical flood/severe-weather event fixture plus NFHL context and an exposure summary, **with warning feeds disabled or contextual-only**. Use this as the seed pattern for `hazards-r0001`.

[⬆ back to top](#contents)

---

## 8. Candidate releases registry

> [!NOTE]
> **PROPOSED template.** Candidates that have not yet received a `PromotionDecision` live under `release/candidates/hazards/`. They are not on the public path.

| Candidate ID | Layer / artifact | Source set | Closure state | Blocking gates | Steward | Target promotion window |
|---|---|---|---|---|---|---|
| `hazards-c0001` *(PROPOSED)* | `<layer-id>` | `<sources>` | `catalog-pending` *(example)* | `evidence_closure_gate`, `review_gate` | `<hazards-domain-steward>` | `<YYYY-Qn>` |
| `hazards-c0002` *(PROPOSED)* | `<layer-id>` | `<sources>` | `policy-pending` *(example)* | `sensitivity_gate`, `rights_gate` | `<hazards-domain-steward>` | `<YYYY-Qn>` |

### Candidate dossier minimum (PROPOSED)

A candidate dossier under `release/candidates/hazards/<candidate-id>/` SHOULD contain:

- `manifest.candidate.json` — proposed `ReleaseManifest` (status: `candidate`)
- `evidence.bundle.json` — resolved `EvidenceBundle` projection
- `validation.report.json` — `ValidationReport` linkage
- `policy.decision.json` — preliminary `PolicyDecision` (`ANSWER` / `ABSTAIN` / `DENY` / `ERROR`)
- `provenance.prov.jsonld` — W3C PROV-O graph (see [`docs/standards/PROV.md`](../../standards/PROV.md))
- `review.notes.md` — steward review markdown payload
- `closure.checklist.md` — catalog/proof/release closure walkthrough

[⬆ back to top](#contents)

---

## 9. Corrected, withdrawn, and superseded releases

> [!NOTE]
> **PROPOSED template.** Corrections, withdrawals, and supersessions retain their historical record. Each row points to the canonical notice under `release/correction_notices/`, `release/withdrawal_notices/`, or back to a `ReleaseManifest`.

| Original release | Event | Reason | Notice / card | Replaced by | Public notice date |
|---|---|---|---|---|---|
| `hazards-r####` *(PROPOSED)* | `corrected` | `<short reason>` | `release/correction_notices/<id>.yaml` | `hazards-r####` | `<YYYY-MM-DD>` |
| `hazards-r####` *(PROPOSED)* | `withdrawn` | `<short reason>` | `release/withdrawal_notices/<id>.yaml` | — | `<YYYY-MM-DD>` |
| `hazards-r####` *(PROPOSED)* | `superseded` | newer release | — | `hazards-r####` | `<YYYY-MM-DD>` |
| `hazards-r####` *(PROPOSED)* | `rolled back` | `<short reason>` | `release/rollback_cards/<id>.yaml` | restored to `hazards-r####` | `<YYYY-MM-DD>` |

[⬆ back to top](#contents)

---

## 10. Per-layer release lineage

> [!NOTE]
> **PROPOSED template.** One block per Hazards layer showing its release sequence. Populate from `release/manifests/` and `release/changelog/` once entries exist (NEEDS VERIFICATION).

<details>
<summary><strong>10.1 <code>hazards-historical-events-ks</code> (PROPOSED)</strong></summary>

| Release | State | Vintage | Manifest | Promotion | Notes |
|---|---|---|---|---|---|
| `hazards-r0001-v1` | `released` | 1950–2024 | `release/manifests/hazards-r0001-v1.yaml` | `release/promotion_decisions/hazards-r0001-v1.yaml` | initial thin slice; NCEI Storm Events archive |

</details>

<details>
<summary><strong>10.2 <code>hazards-nfhl-context-ks</code> (PROPOSED)</strong></summary>

| Release | State | Vintage | Manifest | Promotion | Notes |
|---|---|---|---|---|---|
| `hazards-r0002-v1` | `released` | NFHL `<vintage>` | `release/manifests/hazards-r0002-v1.yaml` | `release/promotion_decisions/hazards-r0002-v1.yaml` | regulatory **context**, not determination |

</details>

<details>
<summary><strong>10.3 <code>hazards-firms-detections-ks</code> (PROPOSED)</strong></summary>

| Release | State | Vintage | Manifest | Promotion | Notes |
|---|---|---|---|---|---|
| `hazards-r0003-v1` | `released` | rolling | `release/manifests/hazards-r0003-v1.yaml` | `release/promotion_decisions/hazards-r0003-v1.yaml` | provisional badge required |

</details>

> [!TIP]
> When a Hazards PMTiles archive is part of a release, follow the **versioned-filename + root-hash sidecar** discipline (CONFIRMED, `KFM-IDX-REL-003`; see [`docs/standards/PMTILES.md`](../../standards/PMTILES.md)). Avoid in-place overwrites — they corrupt CDN/HTTP-Range caches and may render partially.

[⬆ back to top](#contents)

---

## 11. Catalog / proof / release closure for Hazards

**CONFIRMED doctrine.** "Ready" is a **closure property**, not a process outcome ([`KFM-IDX-REL-001`]). A Hazards release MUST resolve cleanly across all six closure links.

```mermaid
flowchart TB
  CAT["Catalog — STAC / DCAT (data/catalog/domain/hazards/)"]
  PROV["Provenance — W3C PROV-O (data/catalog/prov/ or data/proofs/)"]
  EVD["Evidence — EvidenceBundle (data/proofs/evidence_bundle/)"]
  POL["Policy — PolicyDecision (policy/domains/hazards/)"]
  PRF["Proof — RunReceipt · attestation (data/receipts/ · release/signatures/)"]
  REL["Release — ReleaseManifest (release/manifests/)"]

  CAT <--> PROV
  CAT <--> EVD
  EVD <--> POL
  EVD <--> PRF
  PRF <--> REL
  REL <--> CAT
  POL <--> REL

  classDef node fill:#EEF2FF,stroke:#3730A3,color:#312E81;
  class CAT,PROV,EVD,POL,PRF,REL node;
```

### Hazards closure checklist (PROPOSED minimum per release)

- [ ] `SourceDescriptor` exists for every contributing source under [`data/registry/sources/hazards/`](../../../data/registry/sources/hazards/)
- [ ] Source-role honored — no `observed → regulatory` upgrade, no `modeled → observed` flattening, no `aggregate → per-place` join (seven-class enum, §24.1.1)
- [ ] `EvidenceBundle` resolves; `EvidenceRef` chain has no phantoms
- [ ] `ValidationReport` passes; negative fixtures cover at least: stale warning denial, role anti-collapse, emergency-alert denial, sensitive-join denial
- [ ] `PolicyDecision` ≠ `DENY`; rights, sensitivity, life-safety, and release-state gates evaluated
- [ ] STAC item / DCAT record under [`data/catalog/domain/hazards/`](../../../data/catalog/domain/hazards/) with `kfm:` profile fields populated
- [ ] PROV-O graph (`provenance.prov.jsonld`) linked from the STAC item per [`docs/standards/PROV.md`](../../standards/PROV.md)
- [ ] `RunReceipt` and (for tile artifacts) attestation sidecar present; signature in `release/signatures/`
- [ ] `ReleaseManifest` references everything above by stable identifier or digest
- [ ] `rollback target` is named and resolvable
- [ ] `correction_path` is named and resolvable
- [ ] Trust state on the public surface includes *"planning context, not alerting"*

[⬆ back to top](#contents)

---

## 12. Sensitivity, rights, and the life-safety boundary

This is the section that distinguishes Hazards from every other KFM domain.

> [!CAUTION]
> **Hazards is not life-safety.** Warning/advisory polygons are released as **historical or contextual** evidence, never as live alerts. The labels *"planning context, not alerting"* and (for NFHL) *"regulatory context, verify with authority"* MUST appear on the public surface. Emergency-alert denial is a release gate, not a UI tooltip — and the alert-authority boundary is **T4 forever, with no transform path** (CONFIRMED doctrine: `KFM-IDX-PLN-002`; Atlas §24.5.2).

### Hazards-specific publication gates (CONFIRMED doctrine, PROPOSED implementation)

Tier labels use the canonical T0–T4 scheme (Atlas §24.5.1: T0 Open · T1 Generalized · T2 Reviewer · T3 Restricted · T4 Denied).

| Gate | Trigger | Outcome if failed |
|---|---|---|
| `source_role_gate` | Inappropriate source role for claim type (e.g., `modeled → observed`, `regulatory → observed`, `aggregate → per-place` collapse) | `DENY` — quarantine |
| `temporal_gate` | Stale warning, expired advisory, missing `valid/issue/expiry` | `DENY` — never publish expired operational state as current |
| `emergency_alert_gate` | Attempt to publish operational alert content / KFM as alert authority | `DENY` — redirect to NWS / official alerting (T4 forever) |
| `rights_gate` | License / terms / redistribution unclear (e.g., third-party feed) | `DENY` until rights resolved |
| `sensitivity_gate` | Sensitive join (e.g., hazard × archaeology × infrastructure × parcel) producing precise location | `DENY` or generalize per `RedactionReceipt` (T4 critical detail) |
| `evidence_closure_gate` | `EvidenceRef → EvidenceBundle` does not resolve | `ABSTAIN` (runtime) or `DENY` (release) |
| `citation_gate` | Generated / public claim without validated citation | `ABSTAIN` |
| `review_gate` | Steward review required for sensitive / regulatory-context / exposure releases | `HOLD` |
| `release_gate` | Missing `ReleaseManifest`, proof, correction path, or rollback target | `DENY` |
| `rollback_gate` | Rollback target untested | `DENY` |

Sources: KFM Encyclopedia Appendix I (Policy gate index); Domains Culmination Atlas §12.K, §24.5.2.

### Hazards trust-state vocabulary on the public surface

| Trust state | When shown | Public meaning |
|---|---|---|
| `released` | Default for valid public layer | citable historical / contextual evidence |
| `released · provisional` | FIRMS / HMS / NWS detections still under steward verification | use with caution |
| `released · regulatory context` | NFHL / declarations | verify with authority before action |
| `released · stale` | Source past freshness threshold | display, but no longer current |
| `corrected` | After `CorrectionNotice` | older version replaced; see notice |
| `withdrawn` | After `WithdrawalNotice` | layer hidden; record retained |

[⬆ back to top](#contents)

---

## 13. Promotion gates and decisions

**CONFIRMED doctrine.** Promotion is a `PromotionDecision`, recorded with a `PromotionReceipt`. **No watcher, cron job, validator pass, or steward approval alone is promotion** ([`KFM-IDX-REL-002`]). For Hazards specifically, promotion of any warning/advisory or exposure summary requires **separation of duties** between author and release authority when materiality applies (CONFIRMED, Encyclopedia §10 Master Action Matrix; Atlas §24.7 — separation is maturity-dependent and tooling-enforced as the public surface grows).

### Promotion gate sequence (PROPOSED CI mapping)

| # | Gate | Decision artifact | Pass rule | Status |
|---|---|---|---|---|
| A | STAC / EvidenceRef validation | `evidence_ref + spec_hash` | Valid STAC item; spec hash reproducible | PROPOSED |
| B | Policy / Conftest evaluation | `policy_report.json` | No `DENY`; all required `allow`s satisfied | PROPOSED |
| C | Artifact attestation | DSSE / cosign attestation | Sig/attestation present; subject digest bound | PROPOSED |
| D | Attestation verification | `verify_report.json` | Attestation verifies vs subject; trusted issuer | PROPOSED |
| E | Steward approval | signed `approval_token.json` | Token valid, in window, bound to same `spec_hash` | PROPOSED |
| F | Integration smoke | `runtime_smoke.json` | All smoke checks pass; no PII / sensitivity leaks | PROPOSED |
| G | Publish ledger | `ledger_entry.json` + `run_receipt.json` | Entry committed; pointers resolvable; immutable | PROPOSED |

> [!NOTE]
> **Object separation rule.** `ValidationReport`, `PolicyDecision`, `RunReceipt`, `PromotionDecision`, `ReleaseManifest`, `CorrectionNotice`, `RollbackPlan` / `RollbackCard`, and `ProofPack` are **distinct objects** and MUST NOT be merged. That separation is what preserves auditability, replayability, temporal correction lineage, steward accountability, and legal defensibility.

[⬆ back to top](#contents)

---

## 14. Correction and rollback path

```mermaid
flowchart LR
  PUB["Released — hazards-r####-vN"]
  ERR["Error detected or new evidence"]
  CN["CorrectionNotice — release/correction_notices/"]
  NEWPUB["hazards-r####-v(N+1) — PROMOTED"]
  RBK["RollbackCard — release/rollback_cards/"]
  PRIOR["Restored to hazards-r####-v(N-1)"]
  WD["WithdrawalNotice — release/withdrawal_notices/"]
  HID["Layer hidden — record retained"]

  PUB --> ERR
  ERR -- "correctable" --> CN
  CN -->|"new manifest + derivative invalidation"| NEWPUB
  ERR -- "rollback safer" --> RBK
  RBK -->|"alias repoint + cache invalidation"| PRIOR
  ERR -- "withdraw entirely" --> WD
  WD --> HID
```

### Rollback drill — Hazards (PROPOSED)

A complete Hazards rollback drill (NEEDS VERIFICATION in CI) should:

1. Pick one Hazards release with a named rollback target (e.g., `hazards-r####-vN` → `hazards-r####-v(N-1)`).
2. Issue a `RollbackCard` referencing both manifests by stable digest.
3. Invalidate downstream caches: PMTiles CDN entries, drawer payload cache, Focus Mode response cache, graph projection.
4. Re-verify the public surface serves the prior `ReleaseManifest`.
5. Record the rollback revert receipt under [`data/rollback/hazards/<release_id>/`](../../../data/rollback/) and the run receipt under [`data/receipts/release/`](../../../data/receipts/).

> [!IMPORTANT]
> Open question (CONFIRMED gap, `KFM-IDX-REL-004`): how far rollback propagates through tiles, graphs, Focus Mode caches, and Story Nodes. Tracked under §17 below.

[⬆ back to top](#contents)

---

## 15. Source drift, watchers, and freshness

**CONFIRMED doctrine.** Hazards source feeds (NOAA Storm Events, NWS API, FEMA NFHL, FEMA disaster declarations, USGS earthquakes, USGS Water, NASA FIRMS, NOAA HMS, drought monitors, state EM) are change-prone and time-bound. Watchers SHOULD detect drift and emit candidate intake records with a `WORK_CANDIDATE` publication state — **never** publish or auto-promote (watcher-as-non-publisher; [`KFM-IDX-REL-005`], [`KFM-IDX-SRC-006`], Directory Rules §13.5).

| Source family | Suggested cadence (PROPOSED) | Freshness threshold (PROPOSED) | Drift watcher (PROPOSED) | Canonical role (§24.1.1) |
|---|---|---|---|---|
| NOAA Storm Events (NCEI archive) | monthly | per-archive vintage | `tools/ingest/storm_events_watch/` | `observed` / `administrative` |
| NWS API (warnings / advisories) | hourly (context only) | issue/expiry strict | `tools/ingest/nws_context_watch/` | `observed`/`administrative` as context — **expired ≠ current** |
| FEMA Disaster Declarations | weekly | rolling | `tools/ingest/fema_decl_watch/` | `administrative` |
| FEMA NFHL / MSC | quarterly | per-vintage | `tools/ingest/nfhl_watch/` | `regulatory` |
| USGS Earthquakes | hourly / daily | per-event | `tools/ingest/usgs_eq_watch/` | `observed` |
| USGS Water | per source | per-record | shared with `hydrology` lane | `observed` (cross-lane) |
| NASA FIRMS / NOAA HMS | per granule cadence | provisional badging required | `tools/ingest/firms_hms_watch/` | `observed` / `modeled` |
| Drought Monitors | weekly | per-week | `tools/ingest/drought_watch/` | `modeled` / `aggregate` |
| Kansas / local EM | per source | per-source | `tools/ingest/state_em_watch/` | `administrative`; rights NEEDS VERIFICATION |

> [!WARNING]
> **Expired operational context MUST NOT appear as current warning state.** This is a release gate (`temporal_gate`), not a UI affordance. Failure here is a structural trust violation, not a styling issue (CONFIRMED, Atlas §12.I).

[⬆ back to top](#contents)

---

## 16. Validators, tests, and fixtures

**PROPOSED implementation.** Per the Hazards H/I/K sections of the Domains Culmination Atlas, the following Hazards-specific test families gate releases. Each is PROPOSED until repo evidence confirms presence and pass status.

| Test family | Purpose | Suggested path (PROPOSED) | Status |
|---|---|---|---|
| Source-role anti-collapse | Reject any release that flattens the seven-class roles (e.g., `modeled → observed`, `regulatory → observed`, `aggregate → per-place`) | `tests/domains/hazards/test_source_role_anti_collapse.py` | PROPOSED |
| Temporal-role validators | Verify `event_time`, `valid/issue/expiry`, `source_time`, `retrieval_time`, `release_time`, `correction_time` stay distinct | `tests/domains/hazards/test_temporal_role.py` | PROPOSED |
| Emergency-alert denial | Confirm `emergency_alert_gate` returns `DENY` for operational alert content (T4 forever) | `tests/domains/hazards/test_emergency_alert_denial.py` | PROPOSED |
| Operational expiry / freshness | Confirm expired warnings/advisories cannot be served as current | `tests/domains/hazards/test_operational_expiry.py` | PROPOSED |
| Catalog closure | STAC + DCAT + PROV + EvidenceBundle + RunReceipt + ReleaseManifest resolve | `tests/domains/hazards/test_catalog_closure.py` | PROPOSED |
| Evidence Drawer disclaimer | Drawer payload always carries *"planning context, not alerting"* (and NFHL *"verify with authority"*) | `tests/domains/hazards/test_drawer_disclaimer.py` | PROPOSED |
| UI no-direct-source | Public client cannot reach `RAW` / `WORK` / `QUARANTINE` / source APIs directly | `tests/domains/hazards/test_no_direct_source.py` | PROPOSED |
| Rollback drill | Release → `RollbackCard` → restored prior manifest + cache invalidation + revert receipt | `tests/domains/hazards/test_rollback_drill.py` | PROPOSED |
| Negative-fixture deny set | `missing_spec_hash`, `unresolved_evidence`, `restricted_exact_geometry`, `stale_evidence`, `unknown_policy_label`, `publication_before_review` | `fixtures/domains/hazards/negative/` | PROPOSED |

[⬆ back to top](#contents)

---

## 17. Open questions & verification backlog

| Item | Evidence that would settle it | Status |
|---|---|---|
| Confirm `release/manifests/` and `release/candidates/hazards/` exist with at least one Hazards release | mounted repo `git ls-tree`-equivalent | NEEDS VERIFICATION |
| Confirm `policy/domains/hazards/` (or `policy/release/hazards/`) carries Hazards-specific gates (life-safety, expiry, role anti-collapse) | Rego files + Conftest fixtures | NEEDS VERIFICATION |
| Confirm release-gate `.rego` home: `policy/domains/hazards/` vs. `policy/release/hazards/` (both admissible per §13.5) | ADR | OPEN (ADR-HAZ-07) |
| Confirm Hazards STAC profile fields under `kfm:` namespace are fixed and validated | `schemas/contracts/v1/stac/kfm-profile-v1.schema.json` | NEEDS VERIFICATION |
| Confirm Hazards CI pipeline runs the gate sequence A–G with fail-closed semantics | GitHub Actions workflow + run logs | NEEDS VERIFICATION |
| Confirm rollback drill propagates through PMTiles cache, drawer cache, Focus Mode cache, and graph projection | rollback drill spec + receipts | OPEN (`KFM-IDX-REL-004`) |
| Confirm an ADR resolves whether this file is `RELEASE_INDEX.md` (chosen here for visibility) vs. `release-index.md` (lowercase repo convention) | ADR | OPEN |
| Confirm the open `PROV.md` vs `PROVENANCE.md` naming inconsistency (referenced from §11) | ADR | OPEN (Directory Rules §13.5 / OPEN-DR-01) |
| Confirm Hazards source rights and endpoint terms across NOAA, FEMA, USGS, NASA, KS-EM | source registry entries + dated probe receipts | NEEDS VERIFICATION |
| Confirm role taxonomy (seven-class enum) and freshness states are implemented (Atlas §12.N item 2) | schemas + validators + tests | NEEDS VERIFICATION |
| Confirm emergency-alert boundary enforcement (Atlas §12.N item 3) | release gate + fixture | NEEDS VERIFICATION |
| Confirm release / correction / rollback drill executes end-to-end (Atlas §12.N item 4) | drill receipts + manifests | NEEDS VERIFICATION |

> [!NOTE]
> Open items are tracked in [`docs/registers/VERIFICATION_BACKLOG.md`](../../registers/VERIFICATION_BACKLOG.md) (PROPOSED path). Drift between this index and the canonical `release/` artifacts is tracked in [`docs/registers/DRIFT_REGISTER.md`](../../registers/DRIFT_REGISTER.md) (PROPOSED path).

[⬆ back to top](#contents)

---

## Related docs

- [`docs/domains/hazards/README.md`](./README.md) — Hazards domain overview (PROPOSED)
- [`docs/domains/hazards/PUBLICATION_AND_BOUNDARY.md`](./PUBLICATION_AND_BOUNDARY.md) — publication path + not-for-life-safety boundary (PROPOSED)
- [`docs/domains/hazards/PRESERVATION_MATRIX.md`](./PRESERVATION_MATRIX.md) — preservation per lifecycle stage and tier (PROPOSED)
- [`docs/domains/hazards/MISSING_OR_PLANNED_FILES.md`](./MISSING_OR_PLANNED_FILES.md) — lane planning inventory (PROPOSED)
- [`ai-build-operating-contract.md`](../../../ai-build-operating-contract.md) — operating contract (`CONTRACT_VERSION = "3.0.0"`)
- [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md) — Directory Rules (Domain Placement Law §12, `data/` §9.1, `release/` §9.2, anti-patterns §13)
- [`docs/standards/PROV.md`](../../standards/PROV.md) — W3C PROV-O profile *(see open naming question in §17)*
- [`docs/standards/PMTILES.md`](../../standards/PMTILES.md) — PMTiles release discipline
- [`docs/standards/OGC-API-TILES.md`](../../standards/OGC-API-TILES.md) — Tile delivery integration
- [`docs/standards/ISO-19115.md`](../../standards/ISO-19115.md) — Metadata crosswalk
- [`docs/standards/OAI-PMH.md`](../../standards/OAI-PMH.md) — Harvest governance
- [`release/README.md`](../../../release/README.md) — `release/` root README (PROPOSED)
- KFM Domain & Capability Encyclopedia §7.10 (Hazards)
- KFM Domains Culmination Atlas §12 (Hazards), §24.1.1 (source-role enum), §24.5 (tiers), §24.6.1 (Lifecycle gates)
- KFM Pass 20 Part 2 Idea Index: `KFM-IDX-REL-001`..`KFM-IDX-REL-005`, `KFM-IDX-PLN-002`, `KFM-IDX-SRC-006`

---

<sub>Doc: <strong>Hazards Release Index</strong> · Path: <code>docs/domains/hazards/RELEASE_INDEX.md</code> · Version: <code>v2</code> · Pins: CONTRACT_VERSION = "3.0.0" · Status: <code>draft</code> · Last updated: <code>2026-06-05</code> · <a href="#contents">⬆ back to top</a></sub>
