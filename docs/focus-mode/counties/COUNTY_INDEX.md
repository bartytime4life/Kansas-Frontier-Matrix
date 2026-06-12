<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/focus-modes-county-index
title: County Focus Mode Master Index (Kansas, 105 counties)
type: standard
version: v0.3
status: draft
owners:
  - <OWNER:focus-mode-steward>
created: 2026-05-22
updated: 2026-06-11
policy_label: public
authority: collision-prevention coverage register plus validator-parseable index candidate; tools/validators/validate_focus_mode_index.py compatibility NEEDS_VERIFICATION
related:
  - docs/focus-mode/README.md
  - docs/focus-modes/README.md
  - _template/county-build-plan.md
  - STATE_INDEX.md
  - docs/doctrine/directory-rules.md
  - tools/validators/validate_focus_mode_index.py
tags: [kfm, focus-mode, county-scale, index, governed-ai, collision-prevention]
notes:
  - Update converts the county index from a stale not-started/draft seed into a collision-prevention coverage register.
  - The 105 county figure is CONFIRMED from Kansas county coverage in this index.
  - Series coverage is now 105/105 under the current supplied completed/collision register plus current-chat generated artifacts plus accessible repo collision hits.
  - Repo implementation, validator status, seven-file lane completeness, payload readiness, promotion, and release remain NEEDS_VERIFICATION unless separately verified.
  - No repository modification, review, promotion, release, or validator run is claimed by this document.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# County Focus Mode Master Index

> **Status:** draft collision-prevention refresh · **Lane basis:** legacy `docs/focus-mode/counties/` plus canonical-restatement divergence to `docs/focus-modes/<area>-county/` · **Authority:** planning / collision-prevention control surface; validator compatibility `NEEDS_VERIFICATION` · **Owners:** `<OWNER:focus-mode-steward>` · **Last reviewed:** 2026-06-11

![counties](https://img.shields.io/badge/counties-105%20total-blue)
![series%20coverage](https://img.shields.io/badge/series%20coverage-105%2F105-blue)
![not--started](https://img.shields.io/badge/not--started-0-brightgreen)
![register--complete](https://img.shields.io/badge/register--complete-95-blue)
![generated--artifact](https://img.shields.io/badge/generated--artifact-4-purple)
![repo--collision](https://img.shields.io/badge/repo--collision-6-orange)
![validator](https://img.shields.io/badge/validator-NEEDS%20VERIFICATION-yellow)
![ci](https://img.shields.io/badge/CI-NEEDS%20VERIFICATION-lightgrey)

> [!IMPORTANT]
> **No selectable Kansas county remains under the current collision-prevention rule.** Every one of the 105 Kansas counties is now either in the supplied completed/collision register, generated as a current-chat artifact, or collision-identified through accessible repository search. Future county-build prompts should `ABSTAIN` unless the user explicitly authorizes revision, migration, repair, validation, or replacement of an existing county artifact.

> [!CAUTION]
> This file is **not** a release manifest, validator result, repository proof, or publication record. `Series state` prevents duplicate county selection. `Repo implementation status` remains `NEEDS_VERIFICATION` for every county unless a mounted-repo validator run or direct path inspection proves otherwise.

---

## Contents

- [1. Status enum](#1-status-enum)
- [2. Aggregate counts](#2-aggregate-counts)
- [3. Master table (105 Kansas counties)](#3-master-table-105-kansas-counties)
- [4. Notes on corpus evidence, generated artifacts, and discrepancies](#4-notes-on-corpus-evidence-generated-artifacts-and-discrepancies)
- [5. Priority subset (P1 — Directory Rules v1.2)](#5-priority-subset-p1--directory-rules-v12)
- [6. Collision-prevention result](#6-collision-prevention-result)
- [7. Cross-references](#7-cross-references)

---

## 1. Status enum

### 1.1 Series state

| Series state | Meaning | Duplicate-selection result |
|---|---|---|
| `register-complete` | County appeared in the supplied completed/collision register for this county Focus Mode series. | `DENY` duplicate build; use repair/revision workflow instead. |
| `generated-artifact` | A downloadable build-plan artifact was generated in this chat/session lineage. Repository landing is not claimed. | `DENY` duplicate build; use repo-addition or migration workflow instead. |
| `repo-collision` | Accessible repository search found an existing county-plan artifact or filename/content collision. | `DENY` duplicate build; inspect and reconcile existing artifact instead. |
| `not-started` | No completed, generated, or collision-identified evidence recorded. | Candidate only after fresh collision search. Current count: 0. |

### 1.2 Repo implementation state

| Repo implementation state | Meaning |
|---|---|
| `NEEDS_VERIFICATION` | Repo path, seven-file lane completeness, schema/contract/policy/fixture homes, validator status, payload readiness, release status, and rollback machinery have not been proven in this file. |
| `validated` | Reserved for a future validator-confirmed county lane. Not used in this refresh. |
| `payload-ready` | Reserved for a future validated `FocusModePayload`. Not used in this refresh. |
| `released` | Reserved for a future governed release manifest and rollback target. Not used in this refresh. |

[↑ Back to top](#top)

---

## 2. Aggregate counts

### 2.1 Collision-prevention / series coverage

| Series state | Count | Evidence basis |
|---|---:|---|
| `register-complete` | 95 | Supplied completed/collision register in the county-build prompt sequence. |
| `generated-artifact` | 4 | Current-chat artifacts: Harper, Lane, Sheridan, Stanton. |
| `repo-collision` | 6 | Accessible repository search collisions: Greeley, Lincoln, Nemaha, Ness, Smith, Wichita. |
| `not-started` | 0 | 105 − (95 + 4 + 6). |
| **Total** | **105** | Full Kansas county set represented in §3. |

### 2.2 Repo implementation / validation

| Repo implementation state | Count | Evidence basis |
|---|---:|---|
| `NEEDS_VERIFICATION` | 105 | No validator run, mounted checkout reconciliation, complete lane inventory, payload validation, promotion proof, or release manifest is claimed here. |
| `validated` | 0 | Not claimed. |
| `payload-ready` | 0 | Not claimed. |
| `released` | 0 | Not claimed. |

> [!NOTE]
> This refresh intentionally separates **series collision coverage** from **repository implementation maturity**. A county can be blocked from duplicate generation while still requiring repo placement, validator, release, and rollback verification.

[↑ Back to top](#top)

---

## 3. Master table (105 Kansas counties)

Columns:

- **County** — display name.
- **Lane** — kebab-case `<county>-county`; proposed logical lane key.
- **Series state** — duplicate-prevention state from §1.1.
- **Repo implementation status** — implementation maturity from §1.2.
- **Owner** — `<OWNER>` placeholder until live assignment.
- **Priority** — `P1` = Directory Rules v1.2 priority subset; `P2` = prior corpus/register cohort; blank = generated/collision-only update bucket.
- **Sensitivity hot lanes** — known sensitive lanes; defaults fail-closed.
- **Source-seed family** — short signal of distinctive sources.
- **Validation** — `validator-pass` / `validator-fail` / `not-run`.
- **Evidence note** — why the county is blocked from duplicate selection.

| County | Lane | Series state | Repo implementation status | Owner | Priority | Sensitivity hot lanes | Source-seed family | Validation | Evidence note |
|---|---|---|---|---|---|---|---|---|---|
| Allen | `allen-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT · KDA/NASS | not-run | supplied completed/collision register |
| Anderson | `anderson-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Atchison | `atchison-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT · KSHS | not-run | supplied completed/collision register |
| Barber | `barber-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Barton | `barton-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults · critical_infrastructure_exact | County/City GIS · KDOT · KGS | not-run | supplied completed/collision register |
| Bourbon | `bourbon-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Brown | `brown-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Butler | `butler-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Chase | `chase-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Chautauqua | `chautauqua-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Cherokee | `cherokee-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT · KGS | not-run | supplied completed/collision register |
| Cheyenne | `cheyenne-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Clark | `clark-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Clay | `clay-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Cloud | `cloud-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT · KSHS | not-run | supplied completed/collision register |
| Coffey | `coffey-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Comanche | `comanche-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Cowley | `cowley-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Crawford | `crawford-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Decatur | `decatur-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Dickinson | `dickinson-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Doniphan | `doniphan-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Douglas | `douglas-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P1 | defaults · living_person_identifiers | County/City GIS · KDOT · KSHS · KU | not-run | supplied completed/collision register |
| Edwards | `edwards-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Elk | `elk-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Ellis | `ellis-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P1 | defaults | County/City GIS · KDOT · KGS | not-run | supplied completed/collision register |
| Ellsworth | `ellsworth-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults · exact_archaeology | County/City GIS · KDOT · KSHS · KHRI | not-run | supplied completed/collision register |
| Finney | `finney-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P1 | defaults · critical_infrastructure_exact | County/City GIS · KDOT · KDA/NASS | not-run | supplied completed/collision register |
| Ford | `ford-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT · KDA/NASS | not-run | supplied completed/collision register |
| Franklin | `franklin-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Geary | `geary-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults · critical_infrastructure_exact | County/City GIS · KDOT · DoD | not-run | supplied completed/collision register |
| Gove | `gove-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Graham | `graham-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Grant | `grant-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Gray | `gray-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Greeley | `greeley-county` | repo-collision | NEEDS_VERIFICATION | `<OWNER>` |  | defaults | County/City GIS · KDOT · KDA-DWR · KGS · NASS | not-run | `docs/focus-mode/counties/greeley_county/greeley_county_focus_mode_build.md` |
| Greenwood | `greenwood-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Hamilton | `hamilton-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Harper | `harper-county` | generated-artifact | NEEDS_VERIFICATION | `<OWNER>` |  | defaults | County/City GIS · KDOT · KDA-DWR · KGS/KCC · NASS | not-run | `/mnt/data/harper_county_focus_mode_build_plan.md` |
| Harvey | `harvey-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Haskell | `haskell-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Hodgeman | `hodgeman-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Jackson | `jackson-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Jefferson | `jefferson-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Jewell | `jewell-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Johnson | `johnson-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P1 | defaults · living_person_identifiers · critical_infrastructure_exact | County/City GIS · KDOT · KU/KCK | not-run | supplied completed/collision register |
| Kearny | `kearny-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Kingman | `kingman-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Kiowa | `kiowa-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT · NWS | not-run | supplied completed/collision register |
| Labette | `labette-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Lane | `lane-county` | generated-artifact | NEEDS_VERIFICATION | `<OWNER>` |  | defaults | County/City GIS · KDOT · KDA-DWR/GMD1 · KGS · NASS | not-run | `/mnt/data/lane_county_focus_mode_build_plan.md` |
| Leavenworth | `leavenworth-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P1 | defaults · critical_infrastructure_exact | County/City GIS · KDOT · DoD | not-run | supplied completed/collision register |
| Lincoln | `lincoln-county` | repo-collision | NEEDS_VERIFICATION | `<OWNER>` |  | defaults | County/City GIS · KDOT · KSHS · KGS | not-run | `docs/focus-mode/counties/lincoln_county/lincoln_county_focus_mode_build_plan.md` |
| Linn | `linn-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Logan | `logan-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Lyon | `lyon-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Marion | `marion-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Marshall | `marshall-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| McPherson | `mcpherson-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Meade | `meade-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Miami | `miami-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Mitchell | `mitchell-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Montgomery | `montgomery-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Morris | `morris-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Morton | `morton-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Nemaha | `nemaha-county` | repo-collision | NEEDS_VERIFICATION | `<OWNER>` |  | defaults | County/City GIS · KDOT · KSHS · hydrology | not-run | `docs/focus-mode/counties/nemaha_county/nemaha_county_build_plan.md` |
| Neosho | `neosho-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Ness | `ness-county` | repo-collision | NEEDS_VERIFICATION | `<OWNER>` |  | defaults | County/City GIS · KDOT · KGS · fossil/geology | not-run | `docs/focus-mode/counties/ness_county/ness_county_focus_mode_build_plan.md` |
| Norton | `norton-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Osage | `osage-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Osborne | `osborne-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Ottawa | `ottawa-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Pawnee | `pawnee-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Phillips | `phillips-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Pottawatomie | `pottawatomie-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Pratt | `pratt-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Rawlins | `rawlins-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Reno | `reno-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P1 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Republic | `republic-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Rice | `rice-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Riley | `riley-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P1 | defaults · critical_infrastructure_exact | County/City GIS · KDOT · DoD · KSU | not-run | supplied completed/collision register |
| Rooks | `rooks-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Rush | `rush-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Russell | `russell-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Saline | `saline-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P1 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Scott | `scott-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Sedgwick | `sedgwick-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P1 | defaults · living_person_identifiers · critical_infrastructure_exact | County/City GIS · KDOT · WSU | not-run | supplied completed/collision register |
| Seward | `seward-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Shawnee | `shawnee-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P1 | defaults · living_person_identifiers · critical_infrastructure_exact | County/City GIS · KDOT · KSHS · State Capitol | not-run | supplied completed/collision register |
| Sheridan | `sheridan-county` | generated-artifact | NEEDS_VERIFICATION | `<OWNER>` |  | defaults | County/City GIS · KDOT · KDA-DWR/GMD4 · KGS · KDWP · KSHS | not-run | `/mnt/data/sheridan_county_focus_mode_build_plan.md` |
| Sherman | `sherman-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Smith | `smith-county` | repo-collision | NEEDS_VERIFICATION | `<OWNER>` |  | defaults | County/City GIS · KDOT · hydrology · KSHS | not-run | `docs/focus-mode/counties/smith_county/smith_county_build_plan.md` |
| Stafford | `stafford-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Stanton | `stanton-county` | generated-artifact | NEEDS_VERIFICATION | `<OWNER>` |  | defaults | County/City GIS · KDOT · KDA-DWR · KGS · NASS | not-run | `/mnt/data/stanton_county_focus_mode_build_plan.md`; repo search later also showed `docs/focus-mode/counties/stanton_county/stanton_county_focus_mode_build_plan.md` |
| Stevens | `stevens-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Sumner | `sumner-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Thomas | `thomas-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Trego | `trego-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Wabaunsee | `wabaunsee-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Wallace | `wallace-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Washington | `washington-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Wichita | `wichita-county` | repo-collision | NEEDS_VERIFICATION | `<OWNER>` |  | defaults | County/City GIS · KDOT · KDA-DWR · KGS · NASS | not-run | `docs/focus-mode/counties/wichita_county/wichita_county_build_plan.md` |
| Wilson | `wilson-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Woodson | `woodson-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run | supplied completed/collision register |
| Wyandotte | `wyandotte-county` | register-complete | NEEDS_VERIFICATION | `<OWNER>` | P1 | defaults · living_person_identifiers · critical_infrastructure_exact | County/City GIS · KDOT · KCK | not-run | supplied completed/collision register |

[↑ Back to top](#top)

---

## 4. Notes on corpus evidence, generated artifacts, and discrepancies

- **95 register-complete counties.** These are the counties from the supplied completed/collision register. They are blocked for duplicate generation even when repository implementation status is still `NEEDS_VERIFICATION`.
- **4 generated-artifact counties.** Harper, Lane, Sheridan, and Stanton were generated as downloadable Markdown artifacts in this chat/session lineage. Their repository landing, review, validation, promotion, and publication are not claimed here.
- **6 repo-collision counties.** Accessible repository search found existing county-plan artifacts for Greeley, Lincoln, Nemaha, Ness, Smith, and Wichita. These are blocked for duplicate generation and should move through inspection/reconciliation, not new-plan generation.
- **0 not-started counties.** Under the current collision-prevention rules, there is no remaining Kansas county that can be safely selected for a new first-time county Focus Mode Build Plan.
- **Legacy-vs-canonical path divergence remains open.** The legacy path `docs/focus-mode/counties/` appears in current materials, while control-plane doctrine also restates `docs/focus-modes/<area>-county/` as the canonical placement. This file does not resolve that divergence. It records the conflict and requires Directory Rules / ADR reconciliation before path edits.
- **Sensitivity hot lanes.** The `defaults` entry means: parcel_title=`ABSTAIN`; exact_archaeology=`DENY`; burial_sacred=`DENY`; rare_species_exact=`DENY`; critical_infrastructure_exact=`DENY`; living_person_identifiers=`DENY`; dna_genomic=`DENY`; emergency_alert=`ABSTAIN`.
- **Validator status.** No `validate_focus_mode_index.py` result is claimed. Every row remains `not-run`.

[↑ Back to top](#top)

---

## 5. Priority subset (P1 — Directory Rules v1.2)

PROPOSED priority cohort (eleven counties), set by population, infrastructure density, or doctrinal significance. The eleven below are retained from the prior file; adjust only via PR with an explicit rationale.

| County | Rationale (short) |
|---|---|
| Douglas | University seat (KU); high-density historical archive |
| Johnson | Largest population; highest infrastructure density |
| Leavenworth | Federal facility footprint; oldest incorporated city |
| Riley | DoD / KSU; critical infrastructure density |
| Sedgwick | Largest standalone metro (Wichita); aerospace |
| Shawnee | State capital; capitol complex |
| Wyandotte | KCK metro; cross-border infrastructure |
| Reno | Central-state hub |
| Saline | I-70 / I-135 crossroads |
| Ellis | Western anchor; KGS |
| Finney | Western agriculture anchor; KDA/NASS density |

The remaining "P1 Directory Rules v1.2" cohort, if it differs from this seed, is the canonical authority — replace this section verbatim with the cohort declared in `directory-rules.md` §6.7.

[↑ Back to top](#top)

---

## 6. Collision-prevention result

| Question | Result |
|---|---|
| Can an assistant safely pick a new Kansas county under the current register? | **No.** |
| Why? | All 105 counties are now either register-complete, generated-artifact, or repo-collision. |
| Correct finite outcome for "pick a new county and build" without override | `ABSTAIN` or `DENY_DUPLICATE_SELECTION`, depending on runtime policy vocabulary. |
| Safe next actions | Choose a county for revision, validation, migration, repo landing, source-ledger hardening, fixture creation, or release-readiness work. |
| Unsafe next action | Generate another first-time county plan while pretending an unclaimed county remains. |

[↑ Back to top](#top)

---

## 7. Cross-references

- `docs/focus-mode/README.md` — legacy control plane path observed in current materials.
- `docs/focus-modes/README.md` — canonical-restatement control plane path; path authority still requires Directory Rules / ADR reconciliation.
- `STATE_INDEX.md` — state-scale companion (PROPOSED).
- `_template/county-build-plan.md` — county build-plan template + spec.
- `docs/doctrine/directory-rules.md` §6.7 — placement contract.
- `tools/validators/validate_focus_mode_index.py` — index validator.

[↑ Back to top](#top)
