<!--
COUNTY BUILD PLAN TEMPLATE — KFM Focus Mode Control Plane

Copy this file to:
  docs/focus-modes/<area>-county/build-plan.md

Replace every <PLACEHOLDER> and fill the YAML front-matter exactly per the spec
in the front-matter block. The validator at tools/validators/validate_focus_mode_index.py
will reject this template (placeholders present) and accept a filled instance.

This template is also the spec: do not change required keys or field types
without an ADR (see docs/focus-modes/README.md §9).
-->

---
# === KFM Focus Mode Build Plan front-matter (REQUIRED) ===
# Schema authority: contracts/focus_mode/focus_mode_payload.md §3 (plan→payload crosswalk)
# Validator: tools/validators/validate_focus_mode_index.py
schema_version: "1"                        # bump only via ADR
kfm_artifact: "focus_mode_build_plan"      # MUST equal this literal
area:
  county: "<County Name>"                  # human-readable, e.g., "Ellsworth"
  lane: "<county-slug>-county"             # kebab-case slug + "-county"; MUST match folder name
  scope: "county"                          # one of: county | region | corridor
status: "draft"                            # one of: planned | draft | validated | payload-ready | released | rolled-back | deprecated
owner: "<OWNER>"                           # GitHub handle or steward role; do not leave blank
priority: "P2"                             # P1 (Directory Rules v1.2 priority) | P2 (corpus draft) | P3 (later)
last_reviewed: "YYYY-MM-DD"                # ISO date; updated each substantive revision
plan_anchors:                              # CONFIRMED doctrine citations the plan rests on
  - "directory-rules.md#67"                # Focus Modes placement contract
  - "kfm_unified_doctrine_synthesis.md"    # cite-or-abstain + promotion gates
  - "Master_MapLibre_Components-Functions-Features_v2_1_FULL.md#163"  # COUNTY-01..04
ui_shell: "apps/explorer-web"              # MUST be apps/explorer-web (apps/web is drift per OPEN-DR-06)
canonical_paths:                           # where artifacts from this plan land
  ui_lane: "apps/explorer-web/src/focus-modes/<county-slug>-county/"
  fixtures: "fixtures/focus_modes/<county-slug>-county/{valid,invalid}/"
  source_descriptors: "data/catalog/sources/<county-slug>-county/source_descriptors.yaml"
  published_payload: "data/published/api_payloads/focus-modes/<county-slug>-county.json"
  release_manifest: "release/manifests/focus_modes/<county-slug>-county-v1.json"
sensitivity_lanes:                         # per-lane outcome; defaults from README.md §7
  parcel_title: "ABSTAIN"                  # ABSTAIN | DENY (override only with justification)
  exact_archaeology: "DENY"
  burial_sacred: "DENY"
  rare_species_exact: "DENY"
  critical_infrastructure_exact: "DENY"
  living_person_identifiers: "DENY"
  dna_genomic: "DENY"
  emergency_alert: "ABSTAIN"
sensitivity_overrides: []                  # list any per-lane override; each entry requires:
#  - lane: "parcel_title"
#    new_outcome: "ANSWER"
#    justification: "..."
#    deny_fixture_path: "fixtures/focus_modes/<county-slug>-county/invalid/..."
source_seed_families:                      # short list; full ledger in source-seed-list.md
  - "County/City GIS"
  - "KDOT projects"
  - "FEMA / USGS floodplain administration"
  - "KDA / NASS agriculture data"
  - "KGS geology"
  - "KHRI / Museum heritage"
required_layers_min: 0                     # set when layer-registry.md is populated
required_layers_with_policy_decision: 0    # MUST equal required_layers_min before validated
evidence_refs_resolved: 0                  # claims with EvidenceRef that resolves to EvidenceBundle
evidence_refs_total: 0                     # all claims in evidence-model.md; resolved/total MUST be 1.0 to advance past draft
release:
  promotion_gates_passed: []               # subset of [A, B, C, D, E, F, G]; must be all seven to reach released
  release_manifest_id: null                # set when MapReleaseManifest is signed
  rollback_target_id: null                 # set when rollback target is recorded
  correction_path: null                    # how a correction is filed for this slice
adr_open_questions: []                     # any ADR triggers raised by this plan
# === end front-matter ===
---

<a id="top"></a>

# `<County Name>` County Focus Mode — Build Plan

> **Status:** see front-matter `status` · **Lane:** `docs/focus-modes/<county-slug>-county/` · **Owner:** see front-matter `owner` · **Priority:** see front-matter `priority`

![status](https://img.shields.io/badge/status-PROPOSED-yellow)
![placement](https://img.shields.io/badge/placement-Directory%20Rules%20v1.2%20%C2%A76.7-blue)
![ui--shell](https://img.shields.io/badge/UI%20shell-apps%2Fexplorer--web-green)
![sensitivity](https://img.shields.io/badge/sensitivity%20defaults-fail--closed-orange)
![validator](https://img.shields.io/badge/validator-not--run-lightgrey)

> [!IMPORTANT]
> This file is one of **seven required files** per area lane (§6.2 of `docs/focus-modes/README.md`). It is a planning + acceptance artifact, **not a publication target**. The slice becomes a `FocusModePayload` only through the crosswalk in `contracts/focus_mode/focus_mode_payload.md` §3.

---

## Contents

- [1. Slice scope](#1-slice-scope)
- [2. Geographic and temporal frame](#2-geographic-and-temporal-frame)
- [3. Domains in scope](#3-domains-in-scope)
- [4. Source-seed signals (summary)](#4-source-seed-signals-summary)
- [5. Layer plan (summary)](#5-layer-plan-summary)
- [6. Evidence model (summary)](#6-evidence-model-summary)
- [7. Public-safety posture (summary)](#7-public-safety-posture-summary)
- [8. Promotion path](#8-promotion-path)
- [9. Acceptance criteria reference](#9-acceptance-criteria-reference)
- [10. Open questions](#10-open-questions)
- [11. Cross-references](#11-cross-references)

---

## 1. Slice scope

PROPOSED. State, in one paragraph, what a public user can ask of this Focus Mode and what they will get back. Reference the proof-slice pattern (`Master_MapLibre_Components-Functions-Features_v2_1_FULL.md` §16.3 COUNTY-01). State what this slice does **not** show and why (see §7).

[↑ Back to top](#top)

---

## 2. Geographic and temporal frame

PROPOSED. Bounding geometry (county boundary plus tolerance), CRS, time window for layers (earliest/latest source observation), refresh cadence per source family. The `MapContextEnvelope` schema at `schemas/contracts/v1/ui/map_context_envelope.schema.json` defines acceptable bounds/time fields.

[↑ Back to top](#top)

---

## 3. Domains in scope

PROPOSED. The KFM domain bounded-contexts this slice composes across. Standard set: hydrology, soil, atmosphere, geology, fauna, flora, habitat, archaeology, settlements/infrastructure, hazards, agriculture, people/DNA/land/genealogy. Strike domains not in scope; add per-slice rationale.

[↑ Back to top](#top)

---

## 4. Source-seed signals (summary)

PROPOSED. Bulleted summary; full ledger in `source-seed-list.md`. Each source MUST carry rights posture per `data/catalog/sources/<county-slug>-county/source_descriptors.yaml`.

[↑ Back to top](#top)

---

## 5. Layer plan (summary)

PROPOSED. Bulleted summary; per-layer detail (source, policy, evidence ref, style ref, sensitivity tier) lives in `layer-registry.md`. Each entry MUST have a `SourceDescriptor`, a `LayerManifest`, a `PolicyDecision`, and a sensitivity label (COUNTY-01 acceptance item (c)).

[↑ Back to top](#top)

---

## 6. Evidence model (summary)

PROPOSED. What claims the slice will display, each tied to an `EvidenceRef` ID. Full model in `evidence-model.md`. **Cite-or-abstain is the default truth posture** (`kfm_unified_doctrine_synthesis.md` Part III).

[↑ Back to top](#top)

---

## 7. Public-safety posture (summary)

PROPOSED. Bulleted summary; full posture in `public-safety-notes.md`. Defaults applied from `docs/focus-modes/README.md` §7. List any **proposed overrides** here and in front-matter `sensitivity_overrides[]`. Every override requires a deny-fixture (`fixtures/focus_modes/<county-slug>-county/invalid/`).

[↑ Back to top](#top)

---

## 8. Promotion path

PROPOSED. The promotion gates A–G (per `ai-build-operating-contract.md` Part VI) this slice must clear before `released`. Per-slice promotion is a governed state transition, not a file move (`kfm_unified_doctrine_synthesis.md` Part VI invariants).

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

## 9. Acceptance criteria reference

The eight COUNTY-01 acceptance items (a)–(h) live in `acceptance-checklist.md`. The validator checks that file for the eight literal items.

[↑ Back to top](#top)

---

## 10. Open questions

PROPOSED. Open NEEDS VERIFICATION / UNKNOWN items specific to this slice. Add ADR triggers to front-matter `adr_open_questions[]`.

[↑ Back to top](#top)

---

## 11. Cross-references

- `docs/focus-modes/README.md` — control plane
- `docs/focus-modes/COUNTY_INDEX.md` — master index
- `contracts/focus_mode/focus_mode_payload.md` — plan→payload crosswalk
- `tools/validators/validate_focus_mode_index.py` — validator
- `directory-rules.md` §6.7 — placement contract
- `Master_MapLibre_Components-Functions-Features_v2_1_FULL.md` §16.3 — COUNTY-01..04 governance cards

[↑ Back to top](#top)

