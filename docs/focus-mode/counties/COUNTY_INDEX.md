<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/focus-modes-county-index
title: County Focus Mode Master Index (Kansas, 105 counties)
type: standard
version: v0.2
status: draft
owners:
  - <OWNER:focus-mode-steward>
created: 2026-05-22
updated: 2026-05-24
policy_label: public
authority: index parsed by tools/validators/validate_focus_mode_index.py
related:
  - docs/focus-mode/README.md
  - _template/county-build-plan.md
  - STATE_INDEX.md
  - docs/doctrine/directory-rules.md
  - tools/validators/validate_focus_mode_index.py
tags: [kfm, focus-mode, county-scale, index, governed-ai]
notes:
  - Refresh of the existing docs/focus-mode/counties/COUNTY_INDEX.md.
  - The 105 county figure is CONFIRMED. Per-row status is PROPOSED until the validator runs against the live repo.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# County Focus Mode Master Index

> **Status:** draft (refresh) · **Lane:** `docs/focus-mode/counties/` · **Authority:** validator-parseable index for the `-county` scope · **Owners:** `<OWNER:focus-mode-steward>` · **Last reviewed:** 2026-05-24

![counties](https://img.shields.io/badge/counties-105%20total-blue)
![status%3Adraft](https://img.shields.io/badge/draft-34%20(corpus)-orange)
![status%3Anot--started](https://img.shields.io/badge/not--started-71-lightgrey)
![validator](https://img.shields.io/badge/validator-validate__focus__mode__index.py-blue)
![ci](https://img.shields.io/badge/CI-NEEDS%20VERIFICATION-lightgrey)

> [!IMPORTANT]
> **Single source of truth for which counties are in flight and which are not.** The validator parses §3 below. A county that does not appear in this table cannot be claimed; a county claimed twice fails validation; a row at `status: planned` or further without a matching lane fails validation.

---

## Contents

- [1. Status enum](#1-status-enum)
- [2. Aggregate counts](#2-aggregate-counts)
- [3. Master table (105 Kansas counties)](#3-master-table-105-kansas-counties)
- [4. Notes on corpus evidence and discrepancies](#4-notes-on-corpus-evidence-and-discrepancies)
- [5. Priority subset (P1 — Directory Rules v1.2)](#5-priority-subset-p1--directory-rules-v12)
- [6. Cross-references](#6-cross-references)

---

## 1. Status enum

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
| `not-started` | 71 | (105 − 34) |
| `planned` | 0 | — |
| `draft` | 34 | Corpus presence of a Build Plan file (CONFIRMED in corpus) |
| `validated` | 0 | — |
| `payload-ready` | 0 | — |
| `released` | 0 | — |
| **Total** | **105** | Kansas has 105 counties (CONFIRMED). |

> [!NOTE]
> The 34 `draft` counts are CONFIRMED only as **corpus presence of a Build Plan file**. They are NOT confirmed against the live repo until `validate_focus_mode_index.py` runs. Rows whose lane files are absent will be downgraded to `not-started`.

[↑ Back to top](#top)

---

## 3. Master table (105 Kansas counties)

Columns:

- **County** — display name.
- **Lane** — kebab-case `<county>-county`; MUST match folder name.
- **Status** — see §1.
- **Owner** — `<OWNER>` placeholder until live assignment.
- **Priority** — `P1` = Directory Rules v1.2 priority subset (eleven); `P2` = remainder of corpus draft set; blank = not in corpus.
- **Sensitivity hot lanes** — known sensitive lanes; defaults fail-closed.
- **Source-seed family** — short signal of distinctive sources.
- **Validation** — `validator-pass` / `validator-fail` / `not-run`.

> [!CAUTION]
> The table below seeds **all 105 counties** at `not-started` by default. The 34 names listed in §4 are upgraded to `draft` per corpus presence and will be reconciled by the validator on first run.

| County | Lane | Status | Owner | Priority | Sensitivity hot lanes | Source-seed family | Validation |
|---|---|---|---|---|---|---|---|
| Allen | `allen-county` | draft | `<OWNER>` | P2 | defaults | County/City GIS · KDOT · KDA/NASS | not-run |
| Anderson | `anderson-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Atchison | `atchison-county` | draft | `<OWNER>` | P2 | defaults | County/City GIS · KDOT · KSHS | not-run |
| Barber | `barber-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Barton | `barton-county` | draft | `<OWNER>` | P2 | defaults · critical_infrastructure_exact | County/City GIS · KDOT · KGS | not-run |
| Bourbon | `bourbon-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Brown | `brown-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Butler | `butler-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Chase | `chase-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Chautauqua | `chautauqua-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Cherokee | `cherokee-county` | draft | `<OWNER>` | P2 | defaults | County/City GIS · KDOT · KGS | not-run |
| Cheyenne | `cheyenne-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Clark | `clark-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Clay | `clay-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Cloud | `cloud-county` | draft | `<OWNER>` | P2 | defaults | County/City GIS · KDOT · KSHS | not-run |
| Coffey | `coffey-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Comanche | `comanche-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Cowley | `cowley-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Crawford | `crawford-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Decatur | `decatur-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Dickinson | `dickinson-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Doniphan | `doniphan-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Douglas | `douglas-county` | draft | `<OWNER>` | P1 | defaults · living_person_identifiers | County/City GIS · KDOT · KSHS · KU | not-run |
| Edwards | `edwards-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Elk | `elk-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Ellis | `ellis-county` | draft | `<OWNER>` | P2 | defaults | County/City GIS · KDOT · KGS | not-run |
| Ellsworth | `ellsworth-county` | draft | `<OWNER>` | P2 | defaults · exact_archaeology | County/City GIS · KDOT · KSHS · KHRI | not-run |
| Finney | `finney-county` | draft | `<OWNER>` | P2 | defaults · critical_infrastructure_exact | County/City GIS · KDOT · KDA/NASS | not-run |
| Ford | `ford-county` | draft | `<OWNER>` | P2 | defaults | County/City GIS · KDOT · KDA/NASS | not-run |
| Franklin | `franklin-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Geary | `geary-county` | draft | `<OWNER>` | P2 | defaults · critical_infrastructure_exact | County/City GIS · KDOT · DoD | not-run |
| Gove | `gove-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Graham | `graham-county` | draft | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run |
| Grant | `grant-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Gray | `gray-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Greeley | `greeley-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Greenwood | `greenwood-county` | draft | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run |
| Hamilton | `hamilton-county` | draft | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run |
| Harper | `harper-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Harvey | `harvey-county` | draft | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run |
| Haskell | `haskell-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Hodgeman | `hodgeman-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Jackson | `jackson-county` | draft | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run |
| Jefferson | `jefferson-county` | draft | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run |
| Jewell | `jewell-county` | draft | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run |
| Johnson | `johnson-county` | draft | `<OWNER>` | P1 | defaults · living_person_identifiers · critical_infrastructure_exact | County/City GIS · KDOT · KU/KCK | not-run |
| Kearny | `kearny-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Kingman | `kingman-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Kiowa | `kiowa-county` | draft | `<OWNER>` | P2 | defaults | County/City GIS · KDOT · NWS | not-run |
| Labette | `labette-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Lane | `lane-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Leavenworth | `leavenworth-county` | draft | `<OWNER>` | P1 | defaults · critical_infrastructure_exact | County/City GIS · KDOT · DoD | not-run |
| Lincoln | `lincoln-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Linn | `linn-county` | draft | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run |
| Logan | `logan-county` | draft | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run |
| Lyon | `lyon-county` | draft | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run |
| Marion | `marion-county` | draft | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run |
| Marshall | `marshall-county` | draft | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run |
| McPherson | `mcpherson-county` | draft | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run |
| Meade | `meade-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Miami | `miami-county` | draft | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run |
| Mitchell | `mitchell-county` | draft | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run |
| Montgomery | `montgomery-county` | draft | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run |
| Morris | `morris-county` | draft | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run |
| Morton | `morton-county` | draft | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run |
| Nemaha | `nemaha-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Neosho | `neosho-county` | draft | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run |
| Ness | `ness-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Norton | `norton-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Osage | `osage-county` | draft | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run |
| Osborne | `osborne-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Ottawa | `ottawa-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Pawnee | `pawnee-county` | draft | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run |
| Phillips | `phillips-county` | draft | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run |
| Pottawatomie | `pottawatomie-county` | draft | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run |
| Pratt | `pratt-county` | draft | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run |
| Rawlins | `rawlins-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Reno | `reno-county` | draft | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run |
| Republic | `republic-county` | draft | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run |
| Rice | `rice-county` | draft | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run |
| Riley | `riley-county` | draft | `<OWNER>` | P1 | defaults · critical_infrastructure_exact | County/City GIS · KDOT · DoD · KSU | not-run |
| Rooks | `rooks-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Rush | `rush-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Russell | `russell-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Saline | `saline-county` | draft | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run |
| Scott | `scott-county` | draft | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run |
| Sedgwick | `sedgwick-county` | draft | `<OWNER>` | P1 | defaults · living_person_identifiers · critical_infrastructure_exact | County/City GIS · KDOT · WSU | not-run |
| Seward | `seward-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Shawnee | `shawnee-county` | draft | `<OWNER>` | P1 | defaults · living_person_identifiers · critical_infrastructure_exact | County/City GIS · KDOT · KSHS · State Capitol | not-run |
| Sheridan | `sheridan-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Sherman | `sherman-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Smith | `smith-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Stafford | `stafford-county` | draft | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run |
| Stanton | `stanton-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Stevens | `stevens-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Sumner | `sumner-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Thomas | `thomas-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Trego | `trego-county` | draft | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run |
| Wabaunsee | `wabaunsee-county` | draft | `<OWNER>` | P2 | defaults | County/City GIS · KDOT | not-run |
| Wallace | `wallace-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Washington | `washington-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Wichita | `wichita-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Wilson | `wilson-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Woodson | `woodson-county` | not-started | `<OWNER>` |  | defaults | County/City GIS · KDOT | not-run |
| Wyandotte | `wyandotte-county` | draft | `<OWNER>` | P1 | defaults · living_person_identifiers · critical_infrastructure_exact | County/City GIS · KDOT · KCK | not-run |

[↑ Back to top](#top)

---

## 4. Notes on corpus evidence and discrepancies

- **34 draft counts (CONFIRMED in corpus).** The county build-plan files listed in this pack as `draft` mirror the 34 counties present in the project corpus. Validator output is the authoritative reconciliation.
- **Spelling.** The current repo contains a folder `republick_county/` which appears to be a typo for `republic_county/`. This index uses the correct `republic-county` slug; the rename is OUT OF SCOPE for this pack — file an ADR or a focused PR.
- **`grove_county`.** The repo also contains a `grove_county/` folder. There is no Kansas county named "Grove" (Gove County exists). The validator will flag this; resolution is OUT OF SCOPE for this pack.
- **Sensitivity hot lanes.** The "defaults" entries mean: all eight default-fail-closed lanes (parcel_title=ABSTAIN; exact_archaeology=DENY; burial_sacred=DENY; rare_species_exact=DENY; critical_infrastructure_exact=DENY; living_person_identifiers=DENY; dna_genomic=DENY; emergency_alert=ABSTAIN). Per-row additions in this column are *also* hot lanes for that county.

[↑ Back to top](#top)

---

## 5. Priority subset (P1 — Directory Rules v1.2)

PROPOSED priority cohort (eleven counties), set by population, infrastructure density, or doctrinal significance. The eleven below are the canonical P1 subset; adjust only via PR with an explicit rationale.

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

## 6. Cross-references

- `docs/focus-mode/README.md` — control plane (state + county scales)
- `STATE_INDEX.md` — state-scale companion (PROPOSED)
- `_template/county-build-plan.md` — county build-plan template + spec
- `docs/doctrine/directory-rules.md` §6.7 — placement contract
- `tools/validators/validate_focus_mode_index.py` — index validator

[↑ Back to top](#top)
