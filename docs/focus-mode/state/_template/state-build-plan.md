<!--
STATE BUILD PLAN TEMPLATE — KFM Focus Mode Control Plane

Copy this file to:
  docs/focus-mode/state/kansas-state/build-plan.md

Replace every <PLACEHOLDER> and fill the YAML front-matter exactly per the spec
in the front-matter block. The validator at tools/validators/validate_focus_mode_index.py
will reject this template (placeholders present) and accept a filled instance.

PROPOSED. The "-state" scope suffix is not yet enumerated in directory-rules.md §6.7.
This template MUST NOT be filled out and merged until ADR-0028-state-scale-focus-mode-scope.md
is accepted.

This template is also the spec: do not change required keys or field types
without an ADR (see docs/focus-mode/README.md §20).
-->

---
# === KFM Focus Mode Build Plan front-matter (REQUIRED) ===
# Schema authority: contracts/focus_mode/focus_mode_payload.md §3 (plan→payload crosswalk)
# Validator: tools/validators/validate_focus_mode_index.py (state extension PROPOSED with ADR-0028)
schema_version: "1"                        # bump only via ADR
kfm_artifact: "focus_mode_build_plan"      # MUST equal this literal
area:
  state: "<State Name>"                    # human-readable, e.g., "Kansas"
  lane: "<state-slug>-state"               # kebab-case slug + "-state"; MUST match folder name
  scope: "state"                           # PROPOSED (pending ADR-0028); not yet in directory-rules.md §6.7
status: "planned"                          # one of: planned | draft | validated | payload-ready | released | rolled-back | deprecated
owner: "<OWNER:state-lane-steward>"        # GitHub handle or steward role; do not leave blank
priority: "P1"                             # P1 for the canonical state lane
last_reviewed: "YYYY-MM-DD"                # ISO date; updated each substantive revision
plan_anchors:                              # CONFIRMED doctrine citations the plan rests on
  - "directory-rules.md#67"                # Focus Modes placement contract (state suffix PROPOSED)
  - "kfm_unified_doctrine_synthesis.md"    # cite-or-abstain + promotion gates
  - "docs/focus-mode/README.md#3"          # scales: state, county, region, corridor
adr_dependency: "ADR-0028-state-scale-focus-mode-scope.md"  # REQUIRED before this lane can be merged
ui_shell: "apps/explorer-web"              # MUST be apps/explorer-web
canonical_paths:                           # where artifacts from this plan land
  ui_lane: "apps/explorer-web/src/focus-modes/<state-slug>-state/"
  fixtures: "fixtures/focus_modes/<state-slug>-state/{valid,invalid}/"
  source_descriptors: "data/catalog/sources/<state-slug>-state/source_descriptors.yaml"
  published_payload: "data/published/api_payloads/focus-modes/<state-slug>-state.json"
  release_manifest: "release/manifests/focus_modes/<state-slug>-state-v1.json"
sensitivity_lanes:                         # per-lane outcome; defaults from docs/focus-mode/README.md §15
  parcel_title: "ABSTAIN"                  # state-scale aggregation does NOT lower sensitivity
  exact_archaeology: "DENY"
  burial_sacred: "DENY"
  rare_species_exact: "DENY"
  critical_infrastructure_exact: "DENY"
  living_person_identifiers: "DENY"
  dna_genomic: "DENY"
  emergency_alert: "ABSTAIN"
sensitivity_overrides: []                  # any override at state scale requires extra scrutiny:
#  - lane: "parcel_title"
#    new_outcome: "ANSWER"
#    justification: "..."
#    deny_fixture_path: "fixtures/focus_modes/<state-slug>-state/invalid/..."
#    additional_reviewer: "<OWNER:sensitivity-steward>"
source_seed_families:                      # short list; full ledger in source-seed-list.md
  - "KDOT statewide road & project network"
  - "KDA / NASS statewide agriculture aggregates"
  - "USGS NHD & NWIS (statewide hydrology)"
  - "KGS statewide geology"
  - "KSHS statewide heritage register"
  - "FEMA NFHL statewide floodplain"
  - "NOAA NWS statewide weather & climate"
domain_state_coverage:                     # 13 KFM domains × state scale (see STATE_INDEX.md §5)
  hydrology: "full"
  soil: "full"
  atmosphere: "full"
  geology: "full"
  fauna: "full"
  flora: "full"
  habitat: "full"
  archaeology: "aggregates-only"           # no exact locations at any scale
  settlements_infrastructure: "full"
  hazards: "full"
  agriculture: "full"
  people_dna_land_genealogy: "aggregates-only"
  roads_railroads: "full"
required_layers_min: 0                     # set when layer-registry.md is populated
required_layers_with_policy_decision: 0    # MUST equal required_layers_min before validated
evidence_refs_resolved: 0                  # claims with EvidenceRef that resolves to EvidenceBundle
evidence_refs_total: 0                     # all claims in evidence-model.md; resolved/total MUST be 1.0 to advance past draft
release:
  promotion_gates_passed: []               # subset of [A, B, C, D, E, F, G]; must be all seven to reach released
  release_manifest_id: null                # set when MapReleaseManifest is signed
  rollback_target_id: null                 # set when rollback target is recorded
  correction_path: null                    # how a correction is filed for this slice
adr_open_questions:                        # any ADR triggers raised by this plan
  - "ADR-0028 (state scope) — REQUIRED before merge"
# === end front-matter ===
---

<a id="top"></a>

# `<State Name>` State Focus Mode — Build Plan

> **Status:** see front-matter `status` · **Lane:** `docs/focus-mode/state/<state-slug>-state/` · **Owner:** see front-matter `owner` · **Priority:** see front-matter `priority`

![status](https://img.shields.io/badge/status-PROPOSED-yellow)
![placement](https://img.shields.io/badge/placement-Directory%20Rules%20v1.2%20%C2%A76.7%20(EXTENSION%20PROPOSED)-orange)
![scope](https://img.shields.io/badge/scope-%2Dstate%20PROPOSED-orange)
![adr%20dependency](https://img.shields.io/badge/ADR--0028-required-orange)
![ui--shell](https://img.shields.io/badge/UI%20shell-apps%2Fexplorer--web-green)
![sensitivity](https://img.shields.io/badge/sensitivity%20defaults-fail--closed-orange)
![validator](https://img.shields.io/badge/validator-not--run-lightgrey)

> [!IMPORTANT]
> This file is one of **seven required files** per area lane (§13 of `docs/focus-mode/README.md`). It is a planning + acceptance artifact, **not a publication target**. The slice becomes a `FocusModePayload` only through the crosswalk in `contracts/focus_mode/focus_mode_payload.md` §3.

> [!CAUTION]
> **This template MUST NOT be filled out and merged until `ADR-0028-state-scale-focus-mode-scope.md` is accepted.** Until then, the `-state` scope suffix has no authority in `directory-rules.md` §6.7, and any state-scale lane will be rejected by the validator.

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

PROPOSED. State, in one paragraph, what a public user can ask of this state-scale Focus Mode and what they will get back. Statewide answers compose from statewide-cadence sources; questions whose answer requires *exact* parcel/archaeological/critical-infrastructure detail are answered with the default sensitivity posture (DENY/ABSTAIN per §7), not by upscaling a county-scale answer.

[↑ Back to top](#top)

---

## 2. Geographic and temporal frame (statewide)

PROPOSED. Bounding geometry (state boundary plus tolerance), CRS, time window for layers (earliest/latest source observation at statewide cadence), refresh cadence per source family. The `MapContextEnvelope` schema at `schemas/contracts/v1/ui/map_context_envelope.schema.json` defines acceptable bounds/time fields; state bounds use the canonical Kansas envelope.

[↑ Back to top](#top)

---

## 3. Domains in scope (13 × state)

PROPOSED. The 13 KFM domains, each represented at state scale. Default coverage labels are in the front-matter `domain_state_coverage`; this section narrates the per-domain decision. Two domains (archaeology, people/DNA/land/genealogy) are **aggregates-only** at state scale by default (see §7).

[↑ Back to top](#top)

---

## 4. Source-seed signals (statewide summary)

PROPOSED. Bulleted summary; full ledger in `source-seed-list.md`. State-scale sources are the *statewide-cadence* feeds (e.g., KDOT statewide network, KDA/NASS statewide aggregates, NOAA NWS statewide); avoid county-cadence sources here.

[↑ Back to top](#top)

---

## 5. Layer plan (statewide summary)

PROPOSED. Bulleted summary; per-layer detail (source, policy, evidence ref, style ref, sensitivity tier) lives in `layer-registry.md`. Each entry MUST have a `SourceDescriptor`, a `LayerManifest`, a `PolicyDecision`, and a sensitivity label.

[↑ Back to top](#top)

---

## 6. Evidence model (statewide summary)

PROPOSED. What claims the state slice will display, each tied to an `EvidenceRef` ID. Full model in `evidence-model.md`. **Cite-or-abstain is the default truth posture.**

[↑ Back to top](#top)

---

## 7. Public-safety posture (state-scale)

PROPOSED. State-scale aggregation does **not** lower sensitivity. The default fail-closed lanes (see front-matter `sensitivity_lanes`) carry the same outcomes at state scale as at county scale. Any override requires:

- justification,
- a deny-fixture under `fixtures/focus_modes/<state-slug>-state/invalid/`,
- an **additional reviewer** (`additional_reviewer:` in the override entry) — state-scale overrides require sensitivity-steward sign-off, not just lane-owner sign-off.

[↑ Back to top](#top)

---

## 8. State ↔ county composition

PROPOSED. The state lane is **not** a sum of all 105 county lanes. It composes from statewide-cadence sources independently. Where a county-scale answer disagrees with the state-scale answer for the same claim, both are surfaced via `EvidenceRef`s; the conflict is recorded in the `DRIFT_REGISTER.md`, not silently reconciled.

[↑ Back to top](#top)

---

## 9. Promotion path

PROPOSED. The promotion gates A–G (per `ai-build-operating-contract.md` Part VI) this slice must clear before `released`. Per-slice promotion is a governed state transition, not a file move.

| Gate | What it checks (paraphrased) | Status |
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

## 10. Acceptance criteria reference

The state-scale acceptance items (a)–(h), modelled on COUNTY-01 with state-scale wording, live in `acceptance-checklist.md`. The validator checks that file for the eight literal items.

[↑ Back to top](#top)

---

## 11. Open questions

PROPOSED. Open NEEDS VERIFICATION / UNKNOWN items specific to this slice. The ADR-0028 dependency is already declared in front-matter `adr_open_questions[]` and is not a per-slice question.

[↑ Back to top](#top)

---

## 12. Cross-references

- `docs/focus-mode/README.md` — control plane (state + county scales)
- `docs/focus-mode/state/STATE_INDEX.md` — master index (state scale)
- `docs/focus-mode/counties/COUNTY_INDEX.md` — companion (county scale)
- `contracts/focus_mode/focus_mode_payload.md` — plan→payload crosswalk
- `tools/validators/validate_focus_mode_index.py` — validator (state extension PROPOSED with ADR-0028)
- `directory-rules.md` §6.7 — placement contract
- `docs/adr/ADR-0028-state-scale-focus-mode-scope.md` — REQUIRED scope-extension ADR

[↑ Back to top](#top)
