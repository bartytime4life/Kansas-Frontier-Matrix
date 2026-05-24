---
# === KFM Focus Mode Build Plan front-matter (REQUIRED) ===
# Schema authority: contracts/focus_mode/focus_mode_payload.md §3 (plan→payload crosswalk)
# Validator: tools/validators/validate_focus_mode_index.py (state extension PROPOSED with ADR-0028)
schema_version: "1"
kfm_artifact: "focus_mode_build_plan"
area:
  state: "Kansas"
  lane: "kansas-state"
  scope: "state"                           # PROPOSED (pending ADR-0028)
status: "planned"
owner: "<OWNER:state-lane-steward>"
priority: "P1"
last_reviewed: "2026-05-24"
plan_anchors:
  - "directory-rules.md#67"
  - "kfm_unified_doctrine_synthesis.md"
  - "docs/focus-mode/README.md#3"
adr_dependency: "ADR-0028 — State-scale Focus Mode scope.md"
ui_shell: "apps/explorer-web"
canonical_paths:
  ui_lane: "apps/explorer-web/src/focus-modes/kansas-state/"
  fixtures: "fixtures/focus_modes/kansas-state/{valid,invalid}/"
  source_descriptors: "data/catalog/sources/kansas-state/source_descriptors.yaml"
  published_payload: "data/published/api_payloads/focus-modes/kansas-state.json"
  release_manifest: "release/manifests/focus_modes/kansas-state-v1.json"
sensitivity_lanes:
  parcel_title: "ABSTAIN"
  exact_archaeology: "DENY"
  burial_sacred: "DENY"
  rare_species_exact: "DENY"
  critical_infrastructure_exact: "DENY"
  living_person_identifiers: "DENY"
  dna_genomic: "DENY"
  emergency_alert: "ABSTAIN"
sensitivity_overrides: []
source_seed_families:
  - "KDOT statewide road & project network"
  - "KDA / NASS statewide agriculture aggregates"
  - "USGS NHD & NWIS (statewide hydrology)"
  - "KGS statewide geology"
  - "KSHS statewide heritage register"
  - "FEMA NFHL statewide floodplain"
  - "NOAA NWS statewide weather & climate"
domain_state_coverage:
  hydrology: "full"
  soil: "full"
  atmosphere: "full"
  geology: "full"
  fauna: "full"
  flora: "full"
  habitat: "full"
  archaeology: "aggregates-only"
  settlements_infrastructure: "full"
  hazards: "full"
  agriculture: "full"
  people_dna_land_genealogy: "aggregates-only"
  roads_railroads: "full"
required_layers_min: 0
required_layers_with_policy_decision: 0
evidence_refs_resolved: 0
evidence_refs_total: 0
release:
  promotion_gates_passed: []
  release_manifest_id: null
  rollback_target_id: null
  correction_path: null
adr_open_questions:
  - "ADR-0028 (state scope) — REQUIRED before merge"
# === end front-matter ===
---

<a id="top"></a>

# Kansas State Focus Mode — Build Plan

> **Status:** planned · **Lane:** `docs/focus-mode/state/kansas-state/` · **Owner:** `<OWNER:state-lane-steward>` · **Priority:** P1

![status](https://img.shields.io/badge/status-PROPOSED-yellow)
![placement](https://img.shields.io/badge/placement-Directory%20Rules%20v1.2%20%C2%A76.7%20(EXTENSION%20PROPOSED)-orange)
![scope](https://img.shields.io/badge/scope-%2Dstate%20PROPOSED-orange)
![adr%20dependency](https://img.shields.io/badge/ADR--0028-required-orange)
![ui--shell](https://img.shields.io/badge/UI%20shell-apps%2Fexplorer--web-green)
![sensitivity](https://img.shields.io/badge/sensitivity%20defaults-fail--closed-orange)
![validator](https://img.shields.io/badge/validator-not--run-lightgrey)

> [!IMPORTANT]
> This is the planning + acceptance artifact for the `kansas-state` lane. It is **not** a publication target. The slice becomes a `FocusModePayload` only through the crosswalk in `contracts/focus_mode/focus_mode_payload.md` §3.

> [!CAUTION]
> **MUST NOT be merged or promoted past `planned` until `ADR-0028 — State-scale Focus Mode scope` is accepted.** Until then, the `-state` scope suffix has no authority in `directory-rules.md` §6.7, and any state-scale lane will be rejected by the validator.

---

## Contents

- [1. Slice scope](#1-slice-scope)
- [2. Geographic and temporal frame (statewide)](#2-geographic-and-temporal-frame-statewide)
- [3. Domains in scope (13 × state)](#3-domains-in-scope-13--state)
- [4. Source-seed signals (statewide summary)](#4-source-seed-signals-statewide-summary)
- [5. Layer plan (statewide summary)](#5-layer-plan-statewide-summary)
- [6. Evidence model (statewide summary)](#6-evidence-model-statewide-summary)
- [7. Public-safety posture (state-scale)](#7-public-safety-posture-state-scale)
- [8. State ↔ county composition](#8-state--county-composition)
- [9. Promotion path](#9-promotion-path)
- [10. Acceptance criteria reference](#10-acceptance-criteria-reference)
- [11. Open questions](#11-open-questions)
- [12. Cross-references](#12-cross-references)

---

## 1. Slice scope

PROPOSED. A user of this Focus Mode can ask statewide questions framed by Kansas's outer boundary and the project's time window — what statewide hydrology, agriculture, transportation, geology, and hazard layers say at a given moment, and how those layers cite to admissible evidence. The slice answers from **statewide-cadence** sources only; questions whose answer requires exact parcel-, archaeological-site-, or critical-infrastructure-level detail are answered with the default sensitivity posture (DENY/ABSTAIN per §7), not by upscaling a county-scale answer.

This slice is the first proof that the same KFM trust path works at state scale that already works at county scale. It is **not** an aggregate of the 105 county lanes (see §8).

[↑ Back to top](#top)

---

## 2. Geographic and temporal frame (statewide)

PROPOSED.

- **Bounds:** Kansas state boundary (canonical envelope), plus a small tolerance for cross-border features (rivers, rail lines, watersheds).
- **CRS:** EPSG:4326 for envelope and exchange; EPSG:5070 (Albers Equal Area CONUS) for area/length operations.
- **Time window:** Earliest source observation: per layer; latest source observation: per layer refresh.
- **Refresh cadence:** Per source family (e.g., KDA/NASS annual; NOAA NWS hourly; USGS NWIS sub-hourly).

The `MapContextEnvelope` schema at `schemas/contracts/v1/ui/map_context_envelope.schema.json` defines acceptable bounds/time fields.

[↑ Back to top](#top)

---

## 3. Domains in scope (13 × state)

PROPOSED. All 13 KFM domains are represented at state scale by default. Coverage labels in front-matter `domain_state_coverage`. Two domains carry an **aggregates-only** default at state scale:

| Domain | Coverage | Notes |
|---|---|---|
| Hydrology | full | NHD + NWIS statewide |
| Soil | full | SSURGO statewide |
| Atmosphere | full | NOAA NWS + climate normals |
| Geology | full | KGS statewide |
| Fauna | full | KDWP + iNaturalist (aggregates for rare species) |
| Flora | full | KDWP + KS Biological Survey |
| Habitat | full | KS GAP + WAFWA |
| Archaeology | aggregates-only | No exact locations at any scale (ADR-0010) |
| Settlements & infrastructure | full | Census Places + KS DOT |
| Hazards | full | FEMA NFHL + NWS storm reports |
| Agriculture | full | KDA + NASS aggregates |
| People / DNA / land / genealogy | aggregates-only | County-and-coarser aggregates only |
| Roads & railroads | full | KDOT + national rail network |

[↑ Back to top](#top)

---

## 4. Source-seed signals (statewide summary)

PROPOSED. Full ledger in `source-seed-list.md` (to be authored). Statewide-cadence feeds only.

- **Transportation:** KDOT statewide road & project network; AAR/USDOT rail
- **Agriculture:** USDA NASS statewide aggregates; KDA
- **Hydrology:** USGS NHD (NHDPlus High-Res); USGS NWIS gauges
- **Geology:** KGS statewide geologic map; KGS oil & gas (rights-aware)
- **Heritage:** KSHS statewide heritage register; KHRI (sensitivity-tiered)
- **Hazards:** FEMA NFHL; NOAA NWS storm reports; Storm Prediction Center outlooks
- **Atmosphere/climate:** NOAA NWS; NCEI normals; KS Mesonet

Each source MUST carry rights posture per `data/catalog/sources/kansas-state/source_descriptors.yaml`.

[↑ Back to top](#top)

---

## 5. Layer plan (statewide summary)

PROPOSED. Per-layer detail (source, policy, evidence ref, style ref, sensitivity tier) lives in `layer-registry.md` (to be authored). First-release seed (subject to per-layer `SourceDescriptor`, `LayerManifest`, `PolicyDecision`, sensitivity label):

- Kansas state boundary (admin)
- HUC-8 watersheds (hydrology)
- NHD flowlines + waterbodies (hydrology)
- NWIS active gauges (hydrology, point)
- KDOT state highway network (roads)
- Class-I rail network (railroads)
- NHGIS Census Places (settlements)
- FEMA NFHL Special Flood Hazard Areas (hazards)
- NASS county-level cropland aggregates (agriculture, choropleth at county)
- KGS statewide bedrock geology (geology)

[↑ Back to top](#top)

---

## 6. Evidence model (statewide summary)

PROPOSED. Full model in `evidence-model.md` (to be authored). Every consequential claim displayed in the state lane MUST carry an `EvidenceRef` ID resolving to an `EvidenceBundle`. **Cite-or-abstain is the default truth posture.**

Example claim families:

- "The Kansas River at Topeka is at <X> ft gauge height as of <T>." → cites NWIS gauge bundle.
- "Cropland in <county> in 2024 was <X> acres." → cites NASS county aggregate bundle.
- "I-70 mile marker <N> intersects <feature>." → cites KDOT road bundle + spatial join receipt.

[↑ Back to top](#top)

---

## 7. Public-safety posture (state-scale)

PROPOSED. State-scale aggregation does **not** lower sensitivity. The default fail-closed lanes (front-matter `sensitivity_lanes`) carry the same outcomes at state scale as at county scale.

| Lane | Default | Notes |
|---|---|---|
| parcel_title | ABSTAIN | No statewide parcel-title display |
| exact_archaeology | DENY | County-and-coarser aggregates only |
| burial_sacred | DENY | No location-bearing display at any scale |
| rare_species_exact | DENY | KDWP-supplied aggregates only |
| critical_infrastructure_exact | DENY | Networks shown at appropriate generalization |
| living_person_identifiers | DENY | No PII display |
| dna_genomic | DENY | Per ADR-0010 |
| emergency_alert | ABSTAIN | KFM is not an emergency-alerting authority |

Any override requires: written justification, a deny-fixture under `fixtures/focus_modes/kansas-state/invalid/`, **and** an additional sensitivity-steward reviewer (state-scale only).

Full posture in `public-safety-notes.md` (to be authored).

[↑ Back to top](#top)

---

## 8. State ↔ county composition

PROPOSED. The state lane is **not** a sum of all 105 county lanes. It composes from statewide-cadence sources independently. Where a county-scale answer disagrees with the state-scale answer for the same claim:

- both are surfaced via `EvidenceRef`s,
- the conflict is recorded in `docs/registers/DRIFT_REGISTER.md`,
- neither is silently reconciled.

This invariant is required so that releases at one scale do not silently invalidate releases at the other.

[↑ Back to top](#top)

---

## 9. Promotion path

PROPOSED. Promotion gates A–G per `docs/doctrine/ai-build-operating-contract.md` Part VI.

| Gate | What it checks | Status |
|---|---|---|
| A | Schema validation across the slice | not-run |
| B | Evidence closure (every claim → EvidenceBundle) | not-run |
| C | Policy decision present per layer | not-run |
| D | Rights posture verified per source | not-run |
| E | Sensitivity decisions applied (defaults + overrides) | not-run |
| F | Release manifest + rollback target signed | not-run |
| G | Reviewer separation-of-duties recorded | not-run |

> [!NOTE]
> No promotion gate can register `pass` until ADR-0028 is accepted. The validator extension for `-state` scope is itself PROPOSED.

[↑ Back to top](#top)

---

## 10. Acceptance criteria reference

The state-scale acceptance items (a)–(h), modelled on COUNTY-01 with state-scale wording, will live in `acceptance-checklist.md` (to be authored). The validator checks that file for the eight literal items.

[↑ Back to top](#top)

---

## 11. Open questions

PROPOSED. The ADR-0028 dependency is already declared in front-matter `adr_open_questions[]`. Additional per-slice open items:

- **CRS for tile output:** confirm EPSG:3857 (Web Mercator) for tile serving while computations stay in EPSG:5070.
- **NASS cadence:** confirm acceptable lag between NASS publication and KFM payload refresh.
- **Cross-border features:** decide tolerance for features that cross into MO/NE/OK/CO at state-boundary precision.

[↑ Back to top](#top)

---

## 12. Cross-references

- [`../STATE_INDEX.md`](../STATE_INDEX.md) — state-scale master index
- [`../_template/state-build-plan.md`](../_template/state-build-plan.md) — state build-plan template + spec
- [`../../README.md`](../../README.md) — Focus Modes control plane (state + county scales)
- [`../../counties/COUNTY_INDEX.md`](../../counties/COUNTY_INDEX.md) — county-scale companion
- [`../../../doctrine/directory-rules.md`](../../../doctrine/directory-rules.md) §6.7 — placement contract
- [`../../../adr/ADR-0028 — State-scale Focus Mode scope.md`](../../../adr/ADR-0028%20%E2%80%94%20State-scale%20Focus%20Mode%20scope.md) — REQUIRED scope-extension ADR

[↑ Back to top](#top)
