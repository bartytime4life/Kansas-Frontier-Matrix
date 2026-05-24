<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/focus-modes-state-index
title: State Focus Mode Master Index (Kansas-scale, single area)
type: standard
version: v0.1
status: PROPOSED
owners:
  - <OWNER:focus-mode-steward>
created: 2026-05-24
updated: 2026-05-24
policy_label: public
authority: index parsed by tools/validators/validate_focus_mode_index.py (state extension PROPOSED with ADR-0028)
related:
  - docs/focus-mode/README.md
  - docs/focus-mode/counties/COUNTY_INDEX.md
  - _template/state-build-plan.md
  - docs/adr/ADR-0028-state-scale-focus-mode-scope.md
  - tools/validators/validate_focus_mode_index.py
tags: [kfm, focus-mode, state-scale, index, governed-ai]
notes:
  - Single-area index. Kansas has exactly one state; this file expands only if the corpus later admits multi-state scope (not currently in scope).
  - PROPOSED pending ADR-0028 acceptance; until then no kansas-state/ lane may be merged.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# State Focus Mode Master Index

> **Status:** PROPOSED (first emission; pending ADR-0028) · **Lane:** `docs/focus-mode/state/` · **Authority:** validator-parseable index for the `-state` scope · **Owners:** `<OWNER:focus-mode-steward>` · **Last reviewed:** 2026-05-24

![scope](https://img.shields.io/badge/scope-%2Dstate%20PROPOSED-orange)
![areas](https://img.shields.io/badge/areas-1%20(kansas--state)-blue)
![status](https://img.shields.io/badge/status-planned-yellow)
![validator](https://img.shields.io/badge/validator-extension%20PROPOSED-lightgrey)
![ci](https://img.shields.io/badge/CI-NEEDS%20VERIFICATION-lightgrey)
![adr%20dependency](https://img.shields.io/badge/ADR--0028-required-orange)

> [!IMPORTANT]
> **Single source of truth for state-scale Focus Modes.** The validator (`tools/validators/validate_focus_mode_index.py`) parses §3 below. A state-scale area that does not appear in this table cannot be claimed; a row at `status: planned` or further without a matching `docs/focus-mode/state/<area>/` lane fails validation.

> [!CAUTION]
> **The `-state` scope suffix is PROPOSED.** It is not yet enumerated in `directory-rules.md` §6.7. This index is **inert** until `ADR-0028-state-scale-focus-mode-scope.md` is accepted. Until then, treat every row below as design intent, not as an active claim.

---

## Contents

- [1. Status enum](#1-status-enum)
- [2. Aggregate counts](#2-aggregate-counts)
- [3. Master table (state-scale areas)](#3-master-table-state-scale-areas)
- [4. Single-area rationale](#4-single-area-rationale)
- [5. Domain × scale coverage (state row)](#5-domain--scale-coverage-state-row)
- [6. Sensitivity defaults (fail-closed lanes)](#6-sensitivity-defaults-fail-closed-lanes)
- [7. Promotion gates A–G readiness](#7-promotion-gates-ag-readiness)
- [8. Cross-references](#8-cross-references)

---

## 1. Status enum

Same enum as `COUNTY_INDEX.md` §1; reproduced here so the file is self-contained.

| Status | Meaning |
|---|---|
| `not-started` | No build plan exists; no owner assigned. |
| `planned` | Owner assigned + lane scaffold (`README.md` + `build-plan.md`) exists. |
| `draft` | Full seven-file lane exists; not yet validator-clean. |
| `validated` | Lane passes `validate_focus_mode_index.py` and per-area validators. |
| `payload-ready` | `FocusModePayload` instance exists at `data/published/api_payloads/focus-modes/<area>.json` and validates against schema. |
| `released` | `PromotionDecision` envelope passes gates A–G; `MapReleaseManifest` + `rollback target` recorded. |
| `rolled-back` | `RollbackCard` filed; cache invalidated; awaiting correction. |
| `deprecated` | Superseded by a successor release. |

[↑ Back to top](#top)

---

## 2. Aggregate counts

| Status | Count | Source |
|---|---|---|
| `not-started` | 0 | — |
| `planned` | 1 | This index (`kansas-state`) |
| `draft` | 0 | — |
| `validated` | 0 | — |
| `payload-ready` | 0 | — |
| `released` | 0 | — |
| **Total** | **1** | Kansas has exactly one state-scale area in current scope. |

[↑ Back to top](#top)

---

## 3. Master table (state-scale areas)

Columns:

- **Area** — display name.
- **Lane** — kebab-case area slug + `-state` suffix; MUST match folder name under `docs/focus-mode/state/`.
- **Status** — see §1.
- **Owner** — GitHub handle or steward role; no blanks once `planned`.
- **Priority** — `P1` for the canonical Kansas state lane.
- **Sensitivity hot lanes** — known sensitive lanes; defaults fail-closed (see §6).
- **Source-seed family** — short signal of distinctive sources at state scale.
- **Validation** — `validator-pass` / `validator-fail` / `not-run`; only `validator-pass` permits advancement past `draft`.

| Area | Lane | Status | Owner | Priority | Sensitivity hot lanes | Source-seed family | Validation |
|---|---|---|---|---|---|---|---|
| Kansas | `kansas-state` | planned | `<OWNER:state-lane-steward>` | P1 | parcel_title, exact_archaeology, burial_sacred, rare_species_exact, critical_infrastructure_exact, living_person_identifiers, dna_genomic, emergency_alert | KDOT (statewide), KDA/NASS (statewide), USGS NHD/NWIS (statewide), KGS geology (statewide), KSHS (statewide heritage), FEMA NFHL (statewide), NOAA NWS (statewide) | not-run |

[↑ Back to top](#top)

---

## 4. Single-area rationale

PROPOSED. Kansas is the bounded study area of the project. A `kansas-state` lane composes the same 13 KFM domains as a county lane, but at statewide bounds with statewide-cadence sources. There is no second state-scale area in scope; if multi-state ever becomes in scope (e.g., a `frontier-corridor-state` aggregate), it lands as a separate row in this table — not as an alternative spelling of `kansas-state`.

[↑ Back to top](#top)

---

## 5. Domain × scale coverage (state row)

PROPOSED. The state row MUST eventually carry a coverage label per KFM domain. All thirteen are represented at state scale by default; the build plan declares which are in-scope for the first release.

| Domain | State coverage (default) |
|---|---|
| Hydrology | full statewide |
| Soil | full statewide |
| Atmosphere | full statewide |
| Geology | full statewide |
| Fauna | full statewide |
| Flora | full statewide |
| Habitat | full statewide |
| Archaeology | statewide aggregates only (no exact locations; see §6) |
| Settlements / infrastructure | full statewide |
| Hazards | full statewide |
| Agriculture | full statewide |
| People / DNA / land / genealogy | aggregates only (see §6) |
| Roads & railroads | full statewide |

[↑ Back to top](#top)

---

## 6. Sensitivity defaults (fail-closed lanes)

State-scale defaults are the same as county-scale defaults in `docs/focus-mode/README.md` §15. Aggregation at state scale does NOT lower sensitivity for the listed lanes; overrides still require justification, a deny-fixture, and a sensitivity reviewer.

| Lane | Default outcome at state scale |
|---|---|
| parcel_title | ABSTAIN |
| exact_archaeology | DENY |
| burial_sacred | DENY |
| rare_species_exact | DENY |
| critical_infrastructure_exact | DENY |
| living_person_identifiers | DENY |
| dna_genomic | DENY |
| emergency_alert | ABSTAIN |

[↑ Back to top](#top)

---

## 7. Promotion gates A–G readiness

| Gate | What it checks | State row |
|---|---|---|
| A | Schema validation across the slice | not-run |
| B | Evidence closure (every claim → EvidenceBundle) | not-run |
| C | Policy decision present per layer | not-run |
| D | Rights posture verified per source | not-run |
| E | Sensitivity decisions applied (defaults + overrides) | not-run |
| F | Release manifest + rollback target signed | not-run |
| G | Reviewer separation-of-duties recorded | not-run |

[↑ Back to top](#top)

---

## 8. Cross-references

- `docs/focus-mode/README.md` — control plane (state + county scales)
- `docs/focus-mode/counties/COUNTY_INDEX.md` — county-scale companion
- `_template/state-build-plan.md` — state-scale build-plan template
- `docs/adr/ADR-0028-state-scale-focus-mode-scope.md` — scope extension ADR (REQUIRED before any kansas-state/ lane is merged)
- `docs/doctrine/directory-rules.md` §6.7 — placement contract
- `tools/validators/validate_focus_mode_index.py` — index validator (state extension PROPOSED)

[↑ Back to top](#top)
