<a id="top"></a>
# County Focus Mode Master Index

<!-- KFM Meta Block v2 -->
> **Status:** PROPOSED (first emission) · **Lane:** `docs/focus-modes/` · **Authority:** human + machine navigable index; the validator at `tools/validators/validate_focus_mode_index.py` parses the table below · **Owners:** `<OWNER:focus-mode-steward>` · **Last reviewed:** 2026-05-22

![counties](https://img.shields.io/badge/counties-105%20total-blue)
![draft](https://img.shields.io/badge/draft-34%20(corpus)-orange)
![not--started](https://img.shields.io/badge/not--started-71-lightgrey)
![validator](https://img.shields.io/badge/validator-validate__focus__mode__index.py-blue)
![ci](https://img.shields.io/badge/CI-NEEDS%20VERIFICATION-lightgrey)

> [!IMPORTANT]
> **This index is the single source of truth for which counties are in flight and which are not.** Validator `tools/validators/validate_focus_mode_index.py` parses the table in §3 below. A county that does not appear in this table cannot be claimed; a county claimed twice fails validation; a row with `status: planned` or further without a matching lane fails validation.

---

## Contents

- [1. Status enum](#1-status-enum)
- [2. Aggregate counts (CONFIRMED)](#2-aggregate-counts-confirmed)
- [3. Master table (105 Kansas counties)](#3-master-table-105-kansas-counties)
- [4. Notes on corpus evidence and discrepancies](#4-notes-on-corpus-evidence-and-discrepancies)
- [5. Priority subset (the eleven from Directory Rules v1.2)](#5-priority-subset-the-eleven-from-directory-rules-v12)
- [6. Machine-readable companion](#6-machine-readable-companion)

---

## 1. Status enum

| Status | Meaning |
|---|---|
| `not-started` | No build plan exists; no owner assigned. (CONFIRMED for 71 counties.) |
| `planned` | Owner assigned + lane scaffold (`README.md` + `build-plan.md`) exists. |
| `draft` | Full seven-file lane exists; not yet validator-clean. (CONFIRMED for 34 counties per corpus.) |
| `validated` | Lane passes `validate_focus_mode_index.py` and per-area validators. |
| `payload-ready` | `FocusModePayload` instance exists at `data/published/api_payloads/focus-modes/<area>.json` and validates against schema. |
| `released` | `PromotionDecision` envelope passes gates A–G; `MapReleaseManifest` + `rollback target` recorded. |
| `rolled-back` | `RollbackCard` filed; cache invalidated; awaiting correction. |
| `deprecated` | Superseded by a successor release. |

Transitions are described in `docs/focus-modes/README.md` §4.

[↑ Back to top](#top)

---

## 2. Aggregate counts (CONFIRMED)

| Status | Count | Source |
|---|---|---|
| `not-started` | 71 | (105 − 34) |
| `planned` | 0 | — |
| `draft` | 34 | `Master_MapLibre_Components-Functions-Features_v2_1_FULL.md` Appendix C (CONFIRMED corpus presence) |
| `validated` | 0 | — |
| `payload-ready` | 0 | — |
| `released` | 0 | — |
| **Total** | **105** | Kansas has 105 counties (CONFIRMED). |

> [!NOTE]
> The 34 `draft` counts are CONFIRMED only as **corpus presence of a Build Plan file** (status: draft, dated 2026-05-21). They are NOT confirmed against the live repo. When the live repo is mounted, `validate_focus_mode_index.py` will downgrade rows whose lane files are absent to `not-started` and report each as a NEEDS VERIFICATION finding.

[↑ Back to top](#top)

---

## 3. Master table (105 Kansas counties)

Columns:

- **County** — display name.
- **Lane** — proposed kebab-case area name (`<county>-county`).
- **Status** — see §1.
- **Owner** — `<OWNER>` placeholder until live assignment.
- **Priority** — `P1` = Directory Rules v1.2 priority subset (eleven); `P2` = remainder of corpus draft set; blank = not in corpus.
- **Sensitivity hot lanes** — known sensitive lanes for this area (default DENY/ABSTAIN per `README.md` §7).
- **Source-seed family** — short signal of distinctive sources.
- **Validation** — `validator-pass` / `validator-fail` / `not-run`; only `validator-pass` permits advancement past `draft`.

> [!CAUTION]
> All `Source-seed family` and `Sensitivity hot lanes` values for `draft` rows are **PROPOSED** until the per-county `source-seed-list.md` and `public-safety-notes.md` are read from the live repo. Cited values for the 34 draft rows are paraphrased from `Master_MapLibre_Components-Functions-Features_v2_1_FULL.md` Appendix C distinctive-signals column.

| County | Lane | Status | Owner | Priority | Sensitivity hot lanes | Source-seed family | Validation |
|---|---|---|---|---|---|---|---|
| Allen | `allen-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Anderson | `anderson-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Atchison | `atchison-county` | draft | `<OWNER>` | P2 | parcel, archaeology, infrastructure, living-person | Missouri River, Amelia Earhart history | not-run |
| Barber | `barber-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Barton | `barton-county` | draft | `<OWNER>` | P1 | parcel, archaeology, rare-species, infrastructure | Cheyenne Bottoms, Quivira NWR, bird migration | not-run |
| Bourbon | `bourbon-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Brown | `brown-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Butler | `butler-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Chase | `chase-county` | draft | `<OWNER>` | P2 | parcel, archaeology, rare-species | Cottonwood Falls, Tallgrass Prairie NP | not-run |
| Chautauqua | `chautauqua-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Cherokee | `cherokee-county` | draft | `<OWNER>` | P2 | parcel, archaeology, infrastructure (superfund) | Pittsburg edge, Spring River, mining heritage, Picher superfund edge | not-run |
| Cheyenne | `cheyenne-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Clark | `clark-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Clay | `clay-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Cloud | `cloud-county` | draft | `<OWNER>` | P2 | parcel, archaeology (Pawnee village), infrastructure | Concordia, Republican River, historic Pawnee village | not-run |
| Coffey | `coffey-county` | draft | `<OWNER>` | P2 | parcel, archaeology, **critical-infrastructure (nuclear)** | Burlington, Wolf Creek nuclear plant, John Redmond Lake | not-run |
| Comanche | `comanche-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Cowley | `cowley-county` | draft | `<OWNER>` | P2 | parcel, archaeology, infrastructure | Winfield/Arkansas City, Arkansas River, oil heritage | not-run |
| Crawford | `crawford-county` | draft | `<OWNER>` | P2 | parcel, archaeology, infrastructure | Pittsburg, coal mining heritage | not-run |
| Decatur | `decatur-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Dickinson | `dickinson-county` | draft | `<OWNER>` | P2 | parcel, archaeology, infrastructure, living-person (Eisenhower archive) | Abilene, Eisenhower, Smoky Hill River, Chisholm Trail | not-run |
| Doniphan | `doniphan-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Douglas | `douglas-county` | draft | `<OWNER>` | P1 | parcel, archaeology, infrastructure, living-person | Lawrence, KU, Wakarusa, Kaw River, Bleeding Kansas | not-run |
| Edwards | `edwards-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Elk | `elk-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Ellis | `ellis-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Ellsworth | `ellsworth-county` | draft | `<OWNER>` | P1 | parcel, archaeology, infrastructure | Smoky Hills, Smoky Hill River, ranching, sandstone post rock | not-run |
| Finney | `finney-county` | draft | `<OWNER>` | P2 | parcel, archaeology, infrastructure, aquifer | Garden City, Arkansas River, irrigation, feedlots | not-run |
| Ford | `ford-county` | draft | `<OWNER>` | P1 | parcel, archaeology, infrastructure, aquifer | Dodge City, Arkansas River, livestock, High Plains aquifer | not-run |
| Franklin | `franklin-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Geary | `geary-county` | draft | `<OWNER>` | P2 | parcel, archaeology, **critical-infrastructure (Fort Riley)** | Junction City, Fort Riley, Republican-Kansas confluence | not-run |
| Gove | `gove-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Graham | `graham-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Grant | `grant-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Gray | `gray-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Greeley | `greeley-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Greenwood | `greenwood-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Hamilton | `hamilton-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Harper | `harper-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Harvey | `harvey-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Haskell | `haskell-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Hodgeman | `hodgeman-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Jackson | `jackson-county` | draft | `<OWNER>` | P2 | parcel, archaeology, **tribal sovereignty (Prairie Band Potawatomi)** | Holton, Prairie Band Potawatomi reservation | not-run |
| Jefferson | `jefferson-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Jewell | `jewell-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Johnson | `johnson-county` | draft | `<OWNER>` | P1 | parcel, archaeology, infrastructure, living-person | KCMO suburbs, Indian/Mill Creek, Blue River, urban growth | not-run |
| Kearny | `kearny-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Kingman | `kingman-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Kiowa | `kiowa-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Labette | `labette-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Lane | `lane-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Leavenworth | `leavenworth-county` | draft | `<OWNER>` | P1 | parcel, archaeology, **critical-infrastructure (Fort Leavenworth)** | Fort Leavenworth, Missouri River, oldest KS town | not-run |
| Lincoln | `lincoln-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Linn | `linn-county` | draft | `<OWNER>` | P2 | parcel, archaeology, rare-species, infrastructure | Mound City, Marais des Cygnes NWR, free-state history | not-run |
| Logan | `logan-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Lyon | `lyon-county` | draft | `<OWNER>` | P2 | parcel, archaeology, infrastructure | Emporia, Neosho/Cottonwood, Flint Hills edge, Santa Fe Trail | not-run |
| Marion | `marion-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Marshall | `marshall-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| McPherson | `mcpherson-county` | draft | `<OWNER>` | P2 | parcel, archaeology, infrastructure | McPherson, Smoky Hill/Little Arkansas divide, oil heritage | not-run |
| Meade | `meade-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Miami | `miami-county` | draft | `<OWNER>` | P2 | parcel, archaeology, infrastructure | Paola, Marais des Cygnes, Confederate raid history | not-run |
| Mitchell | `mitchell-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Montgomery | `montgomery-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Morris | `morris-county` | draft | `<OWNER>` | P2 | parcel, archaeology (Santa Fe Trail), infrastructure | Council Grove, Santa Fe Trail, Neosho headwaters | not-run |
| Morton | `morton-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Nemaha | `nemaha-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Neosho | `neosho-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Ness | `ness-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Norton | `norton-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Osage | `osage-county` | draft | `<OWNER>` | P2 | parcel, archaeology, infrastructure | Lyndon, coal heritage, Pomona Lake | not-run |
| Osborne | `osborne-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Ottawa | `ottawa-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Pawnee | `pawnee-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Phillips | `phillips-county` | draft | `<OWNER>` | P2 | parcel, archaeology, infrastructure | Phillipsburg, Solomon River, High Plains | not-run |
| Pottawatomie | `pottawatomie-county` | draft | `<OWNER>` | P2 | parcel, archaeology, infrastructure | Wamego, Tuttle Creek Lake, Big Blue | not-run |
| Pratt | `pratt-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Rawlins | `rawlins-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Reno | `reno-county` | draft | `<OWNER>` | P1 | parcel, archaeology, **critical-infrastructure (salt mines)**, rare-species edge | Hutchinson, salt mines, Cheyenne Bottoms edge | not-run |
| Republic | `republic-county` | draft | `<OWNER>` | P2 | parcel, archaeology (Pawnee Indian Museum), tribal sovereignty | Belleville, Republican River, Pawnee Indian Museum | not-run |
| Rice | `rice-county` | draft | `<OWNER>` | P2 | parcel, archaeology, rare-species (Quivira NWR) | Lyons, central plains, salt, Quivira NWR | not-run |
| Riley | `riley-county` | draft | `<OWNER>` | P1 | parcel, archaeology, **critical-infrastructure (Fort Riley)**, rare-species (Konza) | Konza Prairie, Fort Riley, Manhattan, K-State, Kansas-Big Blue confluence | not-run |
| Rooks | `rooks-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Rush | `rush-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Russell | `russell-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Saline | `saline-county` | draft | `<OWNER>` | P2 | parcel, archaeology, **critical-infrastructure (former Smoky Hill Bombing Range)** | Salina, Smoky Hill River, Smoky Hill Bombing Range | not-run |
| Scott | `scott-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Sedgwick | `sedgwick-county` | draft | `<OWNER>` | P1 | parcel, archaeology, **critical-infrastructure (aviation)** | Wichita, Arkansas/Little Arkansas confluence, aviation | not-run |
| Seward | `seward-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Shawnee | `shawnee-county` | draft | `<OWNER>` | P1 | parcel, archaeology, **critical-infrastructure (state capital)**, living-person | Topeka, state capital, Kansas River, urban hydrology | not-run |
| Sheridan | `sheridan-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Sherman | `sherman-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Smith | `smith-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Stafford | `stafford-county` | draft | `<OWNER>` | P2 | parcel, archaeology, rare-species (Quivira NWR core), wetlands | Quivira NWR core, wetlands, bird migration | not-run |
| Stanton | `stanton-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Stevens | `stevens-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Sumner | `sumner-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Thomas | `thomas-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Trego | `trego-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Wabaunsee | `wabaunsee-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Wallace | `wallace-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Washington | `washington-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Wichita | `wichita-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Wilson | `wilson-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Woodson | `woodson-county` | not-started | — | — | parcel, archaeology, infrastructure | TBD | not-run |
| Wyandotte | `wyandotte-county` | draft | `<OWNER>` | P1 | parcel, archaeology, infrastructure, urban floodplain | Kansas City KS, Missouri/Kansas confluence, urban floodplain | not-run |

[↑ Back to top](#top)

---

## 4. Notes on corpus evidence and discrepancies

> [!CAUTION]
> **The corpus disagrees with itself on the active-county count.** `directory-rules.md` v1.2 §0 enumerates eleven priority counties (CONFIRMED at commit `b6a279…`); `Master_MapLibre_Components-Functions-Features_v2_1_FULL.md` Appendix C enumerates ≥30 counties (CONFIRMED corpus presence; status `draft`, dated 2026-05-21). This index uses the larger Appendix C set (34 named counties) as the corpus state and marks the eleven from Directory Rules as `Priority: P1` (see §5). **Resolution: tracked as OPEN-FM-02 in `README.md` §10.**

The 34 `draft` rows are CONFIRMED as **corpus presence of a Build Plan file**. They are NOT confirmed against the live repo. The validator will downgrade rows whose lane files are absent in the live tree.

Counties not named in the corpus are listed as `not-started` so the universe is explicit and so the validator can detect duplicate claims.

The `Sensitivity hot lanes` column applies defaults from `README.md` §7 plus distinctive-signal-derived flags. The defaults DENY/ABSTAIN apply regardless of whether listed; this column highlights *known* sensitivity concentrations per area.

**Bold sensitivity entries** mark per-area concentrations significant enough to require a per-county `public-safety-notes.md` callout: critical-infrastructure (military installations, nuclear, aviation, state capital, salt mines), tribal sovereignty (Prairie Band Potawatomi, Pawnee Indian Museum), specific living-person archives (e.g., Eisenhower).

[↑ Back to top](#top)

---

## 5. Priority subset (the eleven from Directory Rules v1.2)

**CONFIRMED** per `directory-rules.md` v1.2 §0 — these eleven counties are the priority subset that motivated the §6.7 placement contract. The validator does not enforce ordering, but these should drive PR-1 of the §6.7.6 four-PR sequence first:

1. Ellsworth — `ellsworth-county`
2. Riley — `riley-county`
3. Shawnee — `shawnee-county`
4. Ford — `ford-county`
5. Wyandotte — `wyandotte-county`
6. Sedgwick — `sedgwick-county`
7. Douglas — `douglas-county`
8. Leavenworth — `leavenworth-county`
9. Reno — `reno-county`
10. Johnson — `johnson-county`
11. Barton — `barton-county`

[↑ Back to top](#top)

---

## 6. Machine-readable companion

The validator parses the §3 table directly (markdown-table extraction). A JSON snapshot of the same data is **PROPOSED** for emission by the validator at `tools/validators/_artifacts/focus_mode_index.json` for downstream consumers; it is not authored by hand. See `tools/validators/validate_focus_mode_index.py` `--emit-json` flag.

[↑ Back to top](#top)
