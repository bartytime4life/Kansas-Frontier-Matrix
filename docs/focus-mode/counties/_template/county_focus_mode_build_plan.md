<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/focus-mode-county-<county>-build-plan
title: "Focus Mode — <County Title Case> County Build Plan"
type: build-plan
version: v0.1
status: planned                # planned | draft | validated | payload-ready | released | rolled-back | deprecated
created: <DATE-ISO>
updated: <DATE-ISO>
owners:
  - <OWNER:focus-mode-county-steward>
  - <OWNER:focus-mode-steward>
policy_label: public
scale_class: county
area: <county>                  # snake_case, no _county suffix here
area_dir: <county>_county       # snake_case directory name per ADR-0029 §3.3
fips_code: <5-digit FIPS>
authority: per-county Focus Mode composition; restates docs/focus-mode/README.md v0.5; structure governed by ADR-0029
related:
  - docs/focus-mode/README.md
  - docs/focus-mode/ORGANIZATION_RULES.md
  - docs/focus-mode/counties/COUNTY_INDEX.md
  - docs/focus-mode/counties/domains.md
  - docs/adr/ADR-0029-focus-mode-lane-structure-canonized.md
  - docs/adr/ADR-0028-state-scale-focus-mode-scope.md   # 13-domain coverage rule
  # 13 canonical in-lane domain treatments (NEEDS_VERIFICATION for folders not yet present at canonical names)
  - docs/focus-mode/agriculture/README.md
  - docs/focus-mode/archaeology/README.md
  - docs/focus-mode/atmosphere_air/README.md                   # NEEDS_VERIFICATION — live folder is `atmosphere/` (sig #6)
  - docs/focus-mode/fauna/README.md
  - docs/focus-mode/flora/README.md
  - docs/focus-mode/geology/README.md
  - docs/focus-mode/habitat/README.md                          # NEEDS_VERIFICATION — folder not yet present
  - docs/focus-mode/hazards/README.md
  - docs/focus-mode/hydrology/README.md                        # NEEDS_VERIFICATION — live folder is `hydrogeology/` (sig #6)
  - docs/focus-mode/people_dna_land/README.md                  # NEEDS_VERIFICATION — live folder is `people/` (sig #6)
  - docs/focus-mode/roads_rail/README.md                       # NEEDS_VERIFICATION — live folders are split `roads/` + `railroads/` (sig #6)
  - docs/focus-mode/settlements_infrastructure/README.md       # NEEDS_VERIFICATION — live folder is `settlements-infrastructure/` (sig #6)
  - docs/focus-mode/soil/README.md
ui_shell: apps/explorer-web      # NEVER apps/web/ — OPEN-DR-06
tags: [kfm, focus-mode, county, <county>, build-plan]
domain_coverage:                 # REQUIRED: exactly these 13 keys per ADR-0028 §3
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
abstain_justifications:          # REQUIRED for every `abstain` row above
  agriculture: "build plan in `planned` status; population pending"
  archaeology: "build plan in `planned` status; population pending — note sensitivity deny-default"
  atmosphere_air: "build plan in `planned` status; population pending"
  fauna: "build plan in `planned` status; population pending — note sensitive-occurrence deny-default"
  flora: "build plan in `planned` status; population pending — note rare-plant deny-default"
  geology: "build plan in `planned` status; population pending"
  habitat: "build plan in `planned` status; population pending"
  hazards: "build plan in `planned` status; population pending — KFM is never an alert authority"
  hydrology: "build plan in `planned` status; population pending"
  people_dna_land: "build plan in `planned` status; population pending — note living-person and DNA deny-default"
  roads_rail: "build plan in `planned` status; population pending"
  settlements_infrastructure: "build plan in `planned` status; population pending — note critical-infrastructure deny-default"
  soil: "build plan in `planned` status; population pending"
[/KFM_META_BLOCK_V2] -->

[![status: planned](https://img.shields.io/badge/status-planned-lightgrey)](#2-status-and-lifecycle)
[![scale: county](https://img.shields.io/badge/scale-county-blue)](#1-purpose-and-frame)
[![ui-shell: apps/explorer-web](https://img.shields.io/badge/ui--shell-apps%2Fexplorer--web-purple)](#)
[![domain coverage: 0 of 13 populated](https://img.shields.io/badge/domain%20coverage-0%20of%2013%20populated-lightgrey)](#3-13-domain-coverage-matrix)
[![authority: ADR-0029 § ADR-0028](https://img.shields.io/badge/authority-ADR--0029%20%2B%20ADR--0028-blue)](docs/adr/ADR-0029-focus-mode-lane-structure-canonized.md)

<a id="top"></a>

# Focus Mode — `<County Title Case>` County Build Plan

> [!NOTE]
> **Template instance.** This file is the consolidated single-file county build plan per ADR-0029 §3.4. Copy this template to `docs/focus-mode/counties/<county>_county/<county>_county_focus_mode_build_plan.md` and replace every literal `<placeholder>` string. The filename MUST exactly match the parent directory name (self-describing-filename principle, ADR-0029 §4.3).

## Contents

- [1. Purpose and frame](#1-purpose-and-frame)
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
| County name | `<County Title Case>` County | PROPOSED |
| State | Kansas | CONFIRMED |
| FIPS code | `<5-digit FIPS>` | NEEDS_VERIFICATION — cite Census source |
| Area boundary source | TIGER/Line `<year>` Counties (Kansas) + Census Places `<year>` | NEEDS_VERIFICATION — cite specific vintage |
| Temporal frame | `<earliest-date>` through `<latest-date>` (`<temporal-rationale-1-sentence>`) | PROPOSED |
| Lane directory | `docs/focus-mode/counties/<county>_county/` | per ADR-0029 §3.3 |
| Build plan file | `<county>_county_focus_mode_build_plan.md` (this file) | per ADR-0029 §3.4 |

[↑ Back to top](#top)

---

## 2. Status and lifecycle

**Current status:** `planned` (per docs/focus-mode/README.md v0.5 §7 lifecycle).

| Lifecycle gate | Owner | Target date | Status |
|---|---|---|---|
| Authoring (`planned` → `draft`) | `<OWNER:focus-mode-county-steward>` | `<DATE-ISO>` | not-started |
| Population (`draft` → `validated`) | `<OWNER:focus-mode-county-steward>` + domain stewards | `<DATE-ISO>` | not-started |
| Payload emission (`validated` → `payload-ready`) | `<OWNER:focus-mode-steward>` | `<DATE-ISO>` | not-started |
| Release (`payload-ready` → `released`) | `<OWNER:release-steward>` | `<DATE-ISO>` | not-started |

**Next gate:** Authoring. Owner `<OWNER:focus-mode-county-steward>` must populate §1 (frame), §3 (13-domain matrix), §4 (evidence), §6 (source seeds), §7 (public safety notes).

[↑ Back to top](#top)

---

## 3. 13-domain coverage matrix

Per ADR-0028 §3, every county Focus Mode addresses all 13 canonical domains. Each subsection below is one domain; each is either **populated** (with layer-registry rows + evidence refs) or **abstain** (with a one-sentence justification citing §7 of the domain's in-lane README).

> [!IMPORTANT]
> Every entry below MUST resolve to a row in the meta-block `domain_coverage` and `abstain_justifications` map. The validator (§8) verifies consistency. Silent omission of any of the 13 domains is a validator failure.

### 3.1 Agriculture

- **Cross-reference:** `docs/focus-mode/agriculture/README.md`
- **Disposition:** `abstain` _(default — populate or justify)_
- **Justification (if abstain):** `build plan in planned status; population pending` — replace with citation to `docs/focus-mode/agriculture/README.md` §7
- **Layer-registry rows (if populated):**
  ```yaml
  # Example shape per docs/focus-mode/agriculture/README.md §4:
  # - layer_id: agriculture_cdl_<county>_<year>
  #   evidence_ref: <EvidenceRef URI>
  #   sensitivity: T0
  #   style_ref: <style identifier>
  #   owner: <OWNER:agriculture-steward>
  ```

### 3.2 Archaeology

- **Cross-reference:** `docs/focus-mode/archaeology/README.md`
- **Disposition:** `abstain`
- **Justification (if abstain):** `build plan in planned status; population pending — note sensitivity deny-default per docs/focus-mode/archaeology/README.md §7`
- **Public-safety note (always applies):** Exact site coordinates are **DENY default** per `docs/focus-mode/README.md` v0.5 §15. Only generalized representations are public-eligible, after sovereignty review.

### 3.3 Atmosphere / Air

- **Cross-reference:** `docs/focus-mode/atmosphere_air/README.md` _(NEEDS_VERIFICATION — live folder is `atmosphere/`; reconciliation per ADR-0029 §10.2)_
- **Disposition:** `abstain`
- **Justification (if abstain):** `build plan in planned status; population pending`
- **Population note:** Prefer county-intersecting Mesonet stations + KDHE AQ stations + relevant climate normals. KFM is **never** an alert authority.

### 3.4 Fauna

- **Cross-reference:** `docs/focus-mode/fauna/README.md`
- **Disposition:** `abstain`
- **Justification (if abstain):** `build plan in planned status; population pending — note sensitive-occurrence deny-default`
- **Public-safety note (always applies):** Sensitive-species occurrence coordinates are **DENY default** (T4). Public surface only via geoprivacy generalization (T1) after steward review.

### 3.5 Flora

- **Cross-reference:** `docs/focus-mode/flora/README.md`
- **Disposition:** `abstain`
- **Justification (if abstain):** `build plan in planned status; population pending — note rare-plant deny-default`
- **Public-safety note (always applies):** Rare-plant occurrence coordinates are **DENY default** (T4). Same generalization rule as fauna.

### 3.6 Geology

- **Cross-reference:** `docs/focus-mode/geology/README.md`
- **Disposition:** `abstain`
- **Justification (if abstain):** `build plan in planned status; population pending`

### 3.7 Habitat

- **Cross-reference:** `docs/focus-mode/habitat/README.md` _(NEEDS_VERIFICATION — folder not yet present in live tree)_
- **Disposition:** `abstain`
- **Justification (if abstain):** `build plan in planned status; population pending; in-lane habitat/ folder not yet present (sig #6 follow-up)`

### 3.8 Hazards

- **Cross-reference:** `docs/focus-mode/hazards/README.md`
- **Disposition:** `abstain`
- **Justification (if abstain):** `build plan in planned status; population pending — KFM is never an alert authority`
- **Public-safety note (always applies):** Hazard layers are contextual only. **KFM never issues alerts or life-safety instructions** per `docs/focus-mode/README.md` v0.5 §15.

### 3.9 Hydrology

- **Cross-reference:** `docs/focus-mode/hydrology/README.md` _(NEEDS_VERIFICATION — live folder is `hydrogeology/`; reconciliation per ADR-0029 §10.2)_
- **Disposition:** `abstain`
- **Justification (if abstain):** `build plan in planned status; population pending`
- **Population note:** Prefer USGS NHD at HUC-12 + county-intersecting USGS gauges + NFHL zones intersecting county boundary.

### 3.10 People / DNA / Land / Genealogy

- **Cross-reference:** `docs/focus-mode/people_dna_land/README.md` _(NEEDS_VERIFICATION — live folder is `people/`; reconciliation per ADR-0029 §10.2)_
- **Disposition:** `abstain`
- **Justification (if abstain):** `build plan in planned status; population pending — note living-person and DNA deny-default`
- **Public-safety note (always applies):** Living-person identifiers (T4), DNA matches (T4), and private parcel join (T4) are **DENY default**. County land office records (T1) may be admissible after steward review.

### 3.11 Roads / Rail / Trade

- **Cross-reference:** `docs/focus-mode/roads_rail/README.md` _(NEEDS_VERIFICATION — live folders are split `roads/` + `railroads/`; reconciliation per ADR-0029 §10.2)_
- **Disposition:** `abstain`
- **Justification (if abstain):** `build plan in planned status; population pending`
- **Public-safety note:** Public corridors and routes are first-slice safe; **infrastructure vulnerability detail is DENY default** (T4).

### 3.12 Settlements / Infrastructure

- **Cross-reference:** `docs/focus-mode/settlements_infrastructure/README.md` _(NEEDS_VERIFICATION — live folder is `settlements-infrastructure/`; reconciliation per ADR-0029 §10.2)_
- **Disposition:** `abstain`
- **Justification (if abstain):** `build plan in planned status; population pending — note critical-infrastructure deny-default`
- **Public-safety note (always applies):** Critical-infrastructure exact detail is **DENY default** (T4). Generalized footprint may be admissible.

### 3.13 Soil

- **Cross-reference:** `docs/focus-mode/soil/README.md`
- **Disposition:** `abstain`
- **Justification (if abstain):** `build plan in planned status; population pending`
- **Population note:** Prefer SSURGO at county resolution + Mesonet soil-moisture sites intersecting county.

[↑ Back to top](#top)

---

## 4. Evidence model

Every populated layer-registry row in §3 MUST resolve to an `EvidenceRef` that in turn resolves to an `EvidenceBundle` per `docs/standards/Evidence_Bundle.md`. The county build plan asserts:

| Commitment | Path |
|---|---|
| Every layer has a resolvable `EvidenceRef` | per-row in §3 |
| Every layer has a documented sensitivity tier (T0–T4) | per-row in §3 |
| Every layer has a designated style ref | per-row in §3 |
| Every layer has a domain steward owner | per-row in §3 |
| Cite-or-abstain on every claim | enforced by validator (§8) |

[↑ Back to top](#top)

---

## 5. Acceptance checklist

Per `KFM_Unified_Implementation_Architecture_Build_Manual.md` Part VI (gates A–G):

- [ ] **Gate A — Authoring complete.** §1 frame populated; §3 has a non-abstain disposition OR a sourced justification for at least one of {agriculture, geology, hydrology, soil}.
- [ ] **Gate B — Domain coverage closed.** All 13 rows in the meta-block `domain_coverage` map have a value (populated or abstain) with a corresponding `abstain_justifications` entry.
- [ ] **Gate C — Evidence resolved.** Every `populated` row has a resolvable `EvidenceRef` per §4.
- [ ] **Gate D — Sensitivity classified.** Every `populated` row has a documented sensitivity tier per `docs/standards/SENSITIVITY_RUBRIC.md`.
- [ ] **Gate E — Public-safety review.** §7 enumerates every applicable deny-default lane for this county; steward review attached.
- [ ] **Gate F — Validator pass.** §8 validator run is clean (no `drift-*` or `unknown` dispositions; categorization spec at `docs/focus-mode/ORGANIZATION_RULES.md` v0.2).
- [ ] **Gate G — Rollback prepared.** §9 names a `RollbackCard` target.

[↑ Back to top](#top)

---

## 6. Source seeds

Each populated layer in §3 derives from one or more source descriptors. Source descriptors live in `data/catalog/sources/<area>/` per directory-rules.md §6.7.2 (NOT in this lane).

Group source seeds by domain. For each source family, cross-reference the relevant domain README's §5 (Source seeds).

| Domain | County-specific source family seed | Reference |
|---|---|---|
| Agriculture | `<source-name>` (e.g., USDA CDL `<year>` for `<county>`) | `docs/focus-mode/agriculture/README.md` §5 |
| Archaeology | `<source-name>` (e.g., KSHS Site Files — request access; deny-default) | `docs/focus-mode/archaeology/README.md` §5 |
| Atmosphere / Air | `<source-name>` (e.g., KS Mesonet stations intersecting county) | `docs/focus-mode/atmosphere_air/README.md` §5 _(NEEDS_VERIFICATION)_ |
| Fauna | `<source-name>` (e.g., GBIF + KS Biological Survey, generalized) | `docs/focus-mode/fauna/README.md` §5 |
| Flora | `<source-name>` (e.g., KS Biological Survey rare plants, generalized) | `docs/focus-mode/flora/README.md` §5 |
| Geology | `<source-name>` (e.g., KGS bedrock + surficial) | `docs/focus-mode/geology/README.md` §5 |
| Habitat | `<source-name>` (e.g., KS Wildlife Action Plan habitats) | `docs/focus-mode/habitat/README.md` §5 _(NEEDS_VERIFICATION)_ |
| Hazards | `<source-name>` (e.g., FEMA disaster declarations intersecting county) | `docs/focus-mode/hazards/README.md` §5 |
| Hydrology | `<source-name>` (e.g., USGS NHD HUC-12 + NWIS gauges) | `docs/focus-mode/hydrology/README.md` §5 _(NEEDS_VERIFICATION)_ |
| People / DNA / Land | `<source-name>` (e.g., Census decennial; county land office records) | `docs/focus-mode/people_dna_land/README.md` §5 _(NEEDS_VERIFICATION)_ |
| Roads / Rail / Trade | `<source-name>` (e.g., KDOT network + FRA rail) | `docs/focus-mode/roads_rail/README.md` §5 _(NEEDS_VERIFICATION)_ |
| Settlements / Infrastructure | `<source-name>` (e.g., GNIS + Census Places + county GIS) | `docs/focus-mode/settlements_infrastructure/README.md` §5 _(NEEDS_VERIFICATION)_ |
| Soil | `<source-name>` (e.g., NRCS SSURGO at county resolution) | `docs/focus-mode/soil/README.md` §5 |

[↑ Back to top](#top)

---

## 7. Public safety notes

Per `docs/focus-mode/README.md` v0.5 §15 (sensitivity defaults). The following deny-default lanes apply to every county Focus Mode:

| Lane | Default | Source-doctrine citation |
|---|---|---|
| Exact archaeology coordinates | **DENY** | README v0.5 §15 + ADR-0010 |
| Burial / sacred sites | **DENY** | README v0.5 §15 + ADR-0010 |
| Rare species / plants exact occurrences | **DENY** | README v0.5 §15 + ADR-0010 |
| Critical infrastructure exact detail | **DENY** | README v0.5 §15 + ADR-0010 |
| Living person identifiers | **DENY** | README v0.5 §15 + ADR-0010 |
| DNA / genomic data | **DENY** | README v0.5 §15 + ADR-0010 |
| Parcel title detail | **ABSTAIN** | README v0.5 §15 |
| Emergency alert authority | **ABSTAIN** (KFM is never an alert authority) | README v0.5 §15 + ADR-0028 |

County-specific carve-outs (in addition to the above): list any deny-default exceptions specific to `<County Title Case>` County, with steward review attached.

[↑ Back to top](#top)

---

## 8. Validation hooks

Run the validator from the repo root:

```bash
# Production validator (NEEDS_VERIFICATION — path may be updated):
python3 tools/validators/validate_focus_mode_index.py docs/focus-mode/counties/<county>_county/

# Or, during the migration window, the working v2 reference implementation:
python3 /tmp/kfm-organize/organize_v2.py docs/focus-mode/
```

**Expected for a `planned`-status build plan:** All 13 domain rows abstain with justifications; no `drift-*` or `unknown` dispositions on this file; meta-block parses; cross-references resolve (NEEDS_VERIFICATION rows tolerated during migration).

**Checks 1–15 enumerated** in `docs/focus-mode/README.md` v0.5 §19 (the validator-checks list).

[↑ Back to top](#top)

---

## 9. Rollback path

If this county's Focus Mode needs to be rolled back from `released` (or earlier) status:

- **RollbackCard target:** `<rollback-card-uri>` (issue at first `released` promotion)
- **Supersession plan:** new `<county>_county_focus_mode_build_plan.md` revision authored as a new commit; old version preserved in git history; meta-block `status` set to `rolled-back`
- **Correction filing process:** per `docs/runbooks/<correction-runbook>.md` (NEEDS_VERIFICATION — path)

[↑ Back to top](#top)

---

## 10. Cross-references

- `docs/focus-mode/README.md` v0.5 — orientation and design
- `docs/focus-mode/ORGANIZATION_RULES.md` v0.2 — categorization spec for this lane
- `docs/focus-mode/counties/COUNTY_INDEX.md` — 105-county roster
- `docs/focus-mode/counties/domains.md` v0.1 — cross-domain composition reference
- `docs/adr/ADR-0029-focus-mode-lane-structure-canonized.md` — structural decisions this template implements
- `docs/adr/ADR-0028-state-scale-focus-mode-scope.md` — 13-domain coverage rule
- 13 in-lane domain READMEs at `docs/focus-mode/<domain>/README.md` (see meta-block `related:` for full list including NEEDS_VERIFICATION notes for non-canonical live names)
- `docs/standards/Evidence_Bundle.md` — evidence model
- `docs/standards/SENSITIVITY_RUBRIC.md` — sensitivity tiers
- `tools/validators/validate_focus_mode_index.py` — validator (NEEDS_VERIFICATION)

[↑ Back to top](#top)

---

**Last updated:** `<DATE-ISO>` · v0.1 · Authority: ADR-0029 §3.4 (single-file template) + ADR-0028 §3 (13-domain coverage)
