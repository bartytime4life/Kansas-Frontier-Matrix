> [!CAUTION]
> **PROPOSED — blocked on ADR-0028.** This template lands now so that state-scale work can begin as soon as ADR-0028 (`-state` scope) is accepted. Until then, do **NOT** instantiate this template into a live lane.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/focus-mode-state-kansas-build-plan
title: "Focus Mode — Kansas State Build Plan"
type: build-plan
version: v0.1
status: planned                # planned | draft | validated | payload-ready | released | rolled-back | deprecated
state_scope_adr_status: pending   # tracks ADR-0028 acceptance
created: <DATE-ISO>
updated: <DATE-ISO>
owners:
  - <OWNER:focus-mode-state-steward>
  - <OWNER:focus-mode-steward>
policy_label: public
scale_class: state
area: kansas
area_dir: kansas_state             # snake_case per ADR-0029 §3.3
fips_code: "20"                    # Kansas state FIPS (CONFIRMED — Census FIPS publication)
cardinality: 1                     # exactly one state-scale Focus Mode exists; see §1.1
authority: state-scale Focus Mode composition; restates docs/focus-mode/README.md v0.5; structure governed by ADR-0029; scope gated on ADR-0028
related:
  - docs/focus-mode/README.md
  - docs/focus-mode/ORGANIZATION_RULES.md
  - docs/focus-mode/state/STATE_INDEX.md
  - docs/adr/ADR-0028 — State-scale Focus Mode scope.md
  - docs/adr/ADR-0029-focus-mode-lane-structure-canonized.md
  # 13 canonical in-lane domain treatments (NEEDS_VERIFICATION same as county template)
  - docs/focus-mode/agriculture/README.md
  - docs/focus-mode/archaeology/README.md
  - docs/focus-mode/atmosphere_air/README.md                   # NEEDS_VERIFICATION — live folder is `atmosphere/`
  - docs/focus-mode/fauna/README.md
  - docs/focus-mode/flora/README.md
  - docs/focus-mode/geology/README.md
  - docs/focus-mode/habitat/README.md                          # NEEDS_VERIFICATION
  - docs/focus-mode/hazards/README.md
  - docs/focus-mode/hydrology/README.md                        # NEEDS_VERIFICATION — live folder is `hydrogeology/`
  - docs/focus-mode/people_dna_land/README.md                  # NEEDS_VERIFICATION
  - docs/focus-mode/roads_rail/README.md                       # NEEDS_VERIFICATION
  - docs/focus-mode/settlements_infrastructure/README.md       # NEEDS_VERIFICATION
  - docs/focus-mode/soil/README.md
ui_shell: apps/explorer-web        # NEVER apps/web/ — OPEN-DR-06
tags: [kfm, focus-mode, state, kansas, build-plan]
domain_coverage:
  agriculture: abstain
  archaeology: abstain
  atmosphere_air: abstain
  fauna: abstain
  flora: abstain
  geology: abstain
  habitat: abstain
  hazards: abstain
  hydrology: abstain
  people_dna_land: abstain
  roads_rail: abstain
  settlements_infrastructure: abstain
  soil: abstain
abstain_justifications:
  agriculture: "state lane pending ADR-0028 acceptance"
  archaeology: "state lane pending ADR-0028 acceptance"
  atmosphere_air: "state lane pending ADR-0028 acceptance"
  fauna: "state lane pending ADR-0028 acceptance"
  flora: "state lane pending ADR-0028 acceptance"
  geology: "state lane pending ADR-0028 acceptance"
  habitat: "state lane pending ADR-0028 acceptance"
  hazards: "state lane pending ADR-0028 acceptance"
  hydrology: "state lane pending ADR-0028 acceptance"
  people_dna_land: "state lane pending ADR-0028 acceptance"
  roads_rail: "state lane pending ADR-0028 acceptance"
  settlements_infrastructure: "state lane pending ADR-0028 acceptance"
  soil: "state lane pending ADR-0028 acceptance"
[/KFM_META_BLOCK_V2] -->

[![status: planned](https://img.shields.io/badge/status-planned-lightgrey)](#2-status-and-lifecycle)
[![scale: state](https://img.shields.io/badge/scale-state-blueviolet)](#1-purpose-and-frame)
[![scope ADR: pending ADR-0028](https://img.shields.io/badge/scope%20ADR-pending%20ADR--0028-orange)](docs/adr/ADR-0028%20%E2%80%94%20State-scale%20Focus%20Mode%20scope.md)
[![ui-shell: apps/explorer-web](https://img.shields.io/badge/ui--shell-apps%2Fexplorer--web-purple)](#)
[![cardinality: 1](https://img.shields.io/badge/cardinality-1-blue)](#11-cardinality)
[![domain coverage: 0 of 13 populated](https://img.shields.io/badge/domain%20coverage-0%20of%2013%20populated-lightgrey)](#3-13-domain-coverage-matrix)

<a id="top"></a>

# Focus Mode — Kansas State Build Plan

> [!NOTE]
> **Template instance for the single Kansas state lane.** Per ADR-0029 §3.4 this is a consolidated single-file build plan. Copy this template to `docs/focus-mode/state/kansas_state/kansas_state_focus_mode_build_plan.md` and replace literal `<placeholder>` strings. The filename MUST exactly match the parent directory name (self-describing-filename principle, ADR-0029 §4.3).

## Contents

- [1. Purpose and frame](#1-purpose-and-frame)
  - [1.1 Cardinality](#11-cardinality)
  - [1.4 Independence invariant](#14-independence-invariant)
- [2. Status and lifecycle](#2-status-and-lifecycle)
- [3. 13-domain coverage matrix](#3-13-domain-coverage-matrix)
- [4. Evidence model](#4-evidence-model)
- [5. Acceptance checklist](#5-acceptance-checklist)
- [6. Source seeds](#6-source-seeds)
- [7. Public safety notes](#7-public-safety-notes)
- [8. Validation hooks](#8-validation-hooks)
- [9. Rollback path](#9-rollback-path)
- [10. Cross-references](#10-cross-references)

---

## 1. Purpose and frame

| Field | Value | Truth |
|---|---|---|
| State name | Kansas | CONFIRMED |
| FIPS code | `20` | CONFIRMED — Census FIPS |
| Area boundary source | TIGER/Line `<year>` State (Kansas) | NEEDS_VERIFICATION — cite specific vintage |
| Temporal frame | `<earliest-date>` through `<latest-date>` (`<temporal-rationale-1-sentence>`) | PROPOSED |
| Lane directory | `docs/focus-mode/state/kansas_state/` | per ADR-0029 §3.3 |
| Build plan file | `kansas_state_focus_mode_build_plan.md` (this file) | per ADR-0029 §3.4 |

### 1.1 Cardinality

> [!IMPORTANT]
> **Only one state-scale Focus Mode exists: Kansas. Cardinality = 1** per `docs/focus-mode/README.md` v0.5 §2. The `state/` container holds exactly one per-area lane (`kansas_state/`) plus its template. New state-scale areas would require a project-level scope expansion ADR.

### 1.4 Independence invariant

> [!IMPORTANT]
> **The state lane is NOT a roll-up of the 105 county lanes.** Per `docs/focus-mode/README.md` v0.5 §2 and ADR-0028 §3.6 (when accepted), the state lane is an **independent composition with its own evidence chain**. If the state lane were derived from county lanes, every county-level evidence problem would propagate. Independence at the evidence level ensures the state lane has its own falsification surface and can be released, rolled back, or corrected without reference to county lane status.

[↑ Back to top](#top)

---

## 2. Status and lifecycle

**Current status:** `planned` (per docs/focus-mode/README.md v0.5 §7 lifecycle).
**State-scope ADR status:** `pending` (ADR-0028 acceptance).

| Lifecycle gate | Owner | Target date | Status |
|---|---|---|---|
| ADR-0028 acceptance (precondition) | `<OWNER:adr-steward>` | `<DATE-ISO>` | pending |
| Authoring (`planned` → `draft`) | `<OWNER:focus-mode-state-steward>` | `<DATE-ISO>` | not-started — gated on ADR-0028 |
| Population (`draft` → `validated`) | `<OWNER:focus-mode-state-steward>` + 13 domain stewards | `<DATE-ISO>` | not-started |
| Payload emission (`validated` → `payload-ready`) | `<OWNER:focus-mode-steward>` | `<DATE-ISO>` | not-started |
| Release (`payload-ready` → `released`) | `<OWNER:release-steward>` | `<DATE-ISO>` | not-started |

**Next gate:** ADR-0028 acceptance. This template is `planned` until then; do not promote to `draft`.

[↑ Back to top](#top)

---

## 3. 13-domain coverage matrix

Per ADR-0028 §3, every Focus Mode addresses all 13 canonical domains. At **state scale**, source-family preferences differ from county scale — favor statewide mosaics, full networks, and aggregate cuts over per-county detail.

### 3.1 Agriculture

- **Cross-reference:** `docs/focus-mode/agriculture/README.md`
- **Disposition:** `abstain`
- **State-scale source preference:** USDA CDL statewide mosaic; statewide yield aggregates.
- **Justification (if abstain):** `state lane pending ADR-0028 acceptance`

### 3.2 Archaeology

- **Cross-reference:** `docs/focus-mode/archaeology/README.md`
- **Disposition:** `abstain`
- **State-scale source preference:** Statewide cultural-temporal period overlay; sovereignty review path documented.
- **Justification (if abstain):** `state lane pending ADR-0028 acceptance`
- **Public-safety note:** Site coordinates **DENY default**; only generalized cultural-temporal overlay public-eligible.

### 3.3 Atmosphere / Air

- **Cross-reference:** `docs/focus-mode/atmosphere_air/README.md` _(NEEDS_VERIFICATION — live folder is `atmosphere/`)_
- **Disposition:** `abstain`
- **State-scale source preference:** **Full statewide station network from `ks_mesonet` + `kdhe_aq`.** Climate normals at statewide aggregation.
- **Justification (if abstain):** `state lane pending ADR-0028 acceptance`

### 3.4 Fauna

- **Cross-reference:** `docs/focus-mode/fauna/README.md`
- **Disposition:** `abstain`
- **State-scale source preference:** Statewide range polygons (rare species generalized); statewide migration overlays.
- **Justification (if abstain):** `state lane pending ADR-0028 acceptance`
- **Public-safety note:** Sensitive-species exact occurrence **DENY default**.

### 3.5 Flora

- **Cross-reference:** `docs/focus-mode/flora/README.md`
- **Disposition:** `abstain`
- **State-scale source preference:** Statewide rare-plant generalized ranges; statewide vegetation community map.
- **Justification (if abstain):** `state lane pending ADR-0028 acceptance`
- **Public-safety note:** Rare-plant exact occurrence **DENY default**.

### 3.6 Geology

- **Cross-reference:** `docs/focus-mode/geology/README.md`
- **Disposition:** `abstain`
- **State-scale source preference:** Statewide bedrock + surficial maps; mineral occurrence summary at statewide aggregation.
- **Justification (if abstain):** `state lane pending ADR-0028 acceptance`

### 3.7 Habitat

- **Cross-reference:** `docs/focus-mode/habitat/README.md` _(NEEDS_VERIFICATION)_
- **Disposition:** `abstain`
- **State-scale source preference:** Statewide ecological-system map; statewide stewardship zones.
- **Justification (if abstain):** `state lane pending ADR-0028 acceptance`

### 3.8 Hazards

- **Cross-reference:** `docs/focus-mode/hazards/README.md`
- **Disposition:** `abstain`
- **State-scale source preference:** Statewide hazard event index; all state-level disaster declarations.
- **Justification (if abstain):** `state lane pending ADR-0028 acceptance`
- **Public-safety note:** KFM is **never** an alert authority.

### 3.9 Hydrology

- **Cross-reference:** `docs/focus-mode/hydrology/README.md` _(NEEDS_VERIFICATION — live folder is `hydrogeology/`)_
- **Disposition:** `abstain`
- **State-scale source preference:** **Prefer USGS NHD at HUC-4 / HUC-8 over HUC-12 detail.** Statewide gauges; NFHL coverage summary at state aggregation.
- **Justification (if abstain):** `state lane pending ADR-0028 acceptance`

### 3.10 People / DNA / Land / Genealogy

- **Cross-reference:** `docs/focus-mode/people_dna_land/README.md` _(NEEDS_VERIFICATION)_
- **Disposition:** `abstain`
- **State-scale source preference:** Statewide Census aggregates; statewide 72-year-released historical census.
- **Justification (if abstain):** `state lane pending ADR-0028 acceptance`
- **Public-safety note:** Living-person identifiers + DNA **DENY default**.

### 3.11 Roads / Rail / Trade

- **Cross-reference:** `docs/focus-mode/roads_rail/README.md` _(NEEDS_VERIFICATION)_
- **Disposition:** `abstain`
- **State-scale source preference:** **Full statewide `kdot_network` + `fra_rail`** + statewide historical trails.
- **Justification (if abstain):** `state lane pending ADR-0028 acceptance`

### 3.12 Settlements / Infrastructure

- **Cross-reference:** `docs/focus-mode/settlements_infrastructure/README.md` _(NEEDS_VERIFICATION)_
- **Disposition:** `abstain`
- **State-scale source preference:** **Full statewide GNIS + Census Places + statewide ghost-town gazetteer.**
- **Justification (if abstain):** `state lane pending ADR-0028 acceptance`
- **Public-safety note:** Critical-infrastructure exact detail **DENY default**; generalized statewide footprint may be admissible.

### 3.13 Soil

- **Cross-reference:** `docs/focus-mode/soil/README.md`
- **Disposition:** `abstain`
- **State-scale source preference:** **Prefer `nrcs_gnatsgo` (statewide mosaic) over `nrcs_ssurgo` (county detail).** Statewide hydrologic soil group summary.
- **Justification (if abstain):** `state lane pending ADR-0028 acceptance`

[↑ Back to top](#top)

---

## 4. Evidence model

Same shape as county template §4: every populated layer-registry row resolves to an `EvidenceRef` → `EvidenceBundle`. At state scale, evidence chains are independent of county-level chains per §1.4.

[↑ Back to top](#top)

---

## 5. Acceptance checklist

- [ ] **Gate A — ADR-0028 accepted** _(state-scale gate)_. Verify `docs/adr/ADR-0028 — State-scale Focus Mode scope.md` `status` is `accepted` or `proposed-acceptable`. **REQUIRED.**
- [ ] **Gate A.1 — Authoring complete.** §1 frame populated; §3 has at least one `populated` row.
- [ ] **Gate B — Domain coverage closed.** All 13 rows in `domain_coverage` map have a value with a corresponding `abstain_justifications` entry.
- [ ] **Gate C — Evidence resolved.** Every `populated` row has a resolvable `EvidenceRef`.
- [ ] **Gate D — Sensitivity classified.** Every `populated` row has a documented sensitivity tier.
- [ ] **Gate E — Public-safety review.** §7 enumerates every applicable deny-default lane; steward review attached.
- [ ] **Gate F — Validator pass.** §8 validator run is clean (no `drift-*` or `unknown` dispositions; categorization spec at `docs/focus-mode/ORGANIZATION_RULES.md` v0.2).
- [ ] **Gate G — Rollback prepared.** §9 names a `RollbackCard` target.
- [ ] **Gate H — Independence invariant verified.** Evidence chains contain no implicit reference to county-level evidence (per §1.4).

[↑ Back to top](#top)

---

## 6. Source seeds

State-scale source seed list. Group by domain; cross-reference each source family to the relevant domain README's §5.

(Same shape as county template §6; differs in that every entry uses statewide preferences per §3 above.)

[↑ Back to top](#top)

---

## 7. Public safety notes

Same eight deny-default / abstain lanes as the county template §7. At state scale:

- Aggregate releases (statewide counts, statewide rates) are first-slice safe.
- Per-feature detail is governed by the same per-domain rules as county scale.
- KFM is **never** an alert authority — this applies at every scale.

[↑ Back to top](#top)

---

## 8. Validation hooks

```bash
# Production validator (NEEDS_VERIFICATION):
python3 tools/validators/validate_focus_mode_index.py docs/focus-mode/state/kansas_state/

# Or, working v2 reference implementation:
python3 /tmp/kfm-organize/organize_v2.py docs/focus-mode/
```

**Expected for a `planned`-status state build plan:** All 13 domains abstain with the standard "state lane pending ADR-0028 acceptance" justification; meta-block `state_scope_adr_status: pending`; no `drift-*` or `unknown` dispositions on this file.

After ADR-0028 acceptance, update `state_scope_adr_status: accepted` and proceed to `draft`.

[↑ Back to top](#top)

---

## 9. Rollback path

If the state Focus Mode is rolled back from `released`:

- **RollbackCard target:** `<rollback-card-uri>` (issue at first `released` promotion)
- **Supersession plan:** new `kansas_state_focus_mode_build_plan.md` revision authored as new commit; meta-block `status` set to `rolled-back`
- **Correction filing process:** per `docs/runbooks/<correction-runbook>.md` (NEEDS_VERIFICATION)
- **County lane independence:** rolling back the state lane does NOT roll back any county lane (per §1.4 independence invariant). Each lane has its own RollbackCard chain.

[↑ Back to top](#top)

---

## 10. Cross-references

- `docs/focus-mode/README.md` v0.5 — orientation and design
- `docs/focus-mode/ORGANIZATION_RULES.md` v0.2 — categorization spec
- `docs/focus-mode/state/STATE_INDEX.md` — state-scale index
- `docs/adr/ADR-0028 — State-scale Focus Mode scope.md` — `-state` scope + 13-domain coverage rule (gating ADR)
- `docs/adr/ADR-0029-focus-mode-lane-structure-canonized.md` — structural decisions this template implements
- 13 in-lane domain READMEs at `docs/focus-mode/<domain>/README.md` (NEEDS_VERIFICATION for non-canonical live names)
- `docs/standards/Evidence_Bundle.md` — evidence model
- `docs/standards/SENSITIVITY_RUBRIC.md` — sensitivity tiers
- `tools/validators/validate_focus_mode_index.py` — validator (NEEDS_VERIFICATION)

[↑ Back to top](#top)

---

**Last updated:** `<DATE-ISO>` · v0.1 · Authority: ADR-0028 (scope; gating) + ADR-0029 §3.4 (template structure)
