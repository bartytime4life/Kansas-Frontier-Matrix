<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/focus-modes-county-index
title: County Focus Mode Master Index (Kansas, 105 counties)
type: standard
version: v1.4
status: draft; repository-grounded; compatibility-lane; non-release; non-publication
owners:
  - "NEEDS VERIFICATION — Focus Mode stewardship"
created: 2026-05-22
updated: 2026-08-21
policy_label: public; documentation; county-scope; compatibility; cite-or-abstain
owning_root: docs/
responsibility: >-
  Provide a human-readable inventory and collision-prevention index for the
  county planning artifacts currently tracked under docs/focus-mode/counties/
  without granting lifecycle, validator, policy, release, or publication state.
authority: >-
  Repository inventory and navigation only. County artifacts, index rows,
  validators, tests, commits, and pull requests do not create source,
  evidence, policy, review, promotion, release, or publication authority.
truth_posture: >-
  CONFIRMED 105 Kansas county names, 105 county-shaped directories, the complete
  non-truncated county tree, current filename and README anomalies, current
  singular compatibility placement, and dormant validator mismatch /
  PROPOSED legacy priority, lane, sensitivity, and source-seed planning signals /
  CONFLICTED current snake_case two-file county tree versus the proposed
  kebab-case seven-file control-plane design / UNKNOWN per-county semantic
  accuracy, source rights, evidence closure, sensitivity review, owner,
  correction readiness, release, rollback execution, deployment, and public
  parity / NEEDS VERIFICATION every county lifecycle state and validator outcome.
current_path: docs/focus-mode/counties/COUNTY_INDEX.md
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  authoring_base_commit: 51d06e47d60e1071a5728267b5dac4255c4c338b
  current_main_inventory_commit: 51d06e47d60e1071a5728267b5dac4255c4c338b
  target_prior_blob: 8a2fa26d607f2da2c1f59c9ea9134d6dda3a222c
  county_tree_current_main: 2a70a8b7a8b9b6a096c818898286be545a09144a
  decatur_readme_blob: 8c42e0a671fc63f6726a53737628338bb1b2732e
  decatur_plan_blob: a56142b219741d857564dd68d803bb48fabdc540
  elk_readme_blob: 310f56a7490adf212313674d8b85f38f0f5b8074
  edwards_typo_readme_prior_blob: e25f1814e51579d5f55c0f1fe0135ddb28a47f4a
  edwards_readme_blob: ce3076c85f89064b7a9fa1d2c06f075185a895c1
  edwards_plan_blob: 41d9d8464b140ad618e560a45a65611bdcc4b409
  doniphan_readme_blob: 3b81c308ac09fb695ea352b95db1e62f60a60732
  focus_mode_readme_blob: 8600c0ac09452b4b03e5f60b94f1eb27c072b5db
  county_readme_blob: 48621badd51614db7bff0882c19096fa388234ac
  county_template_blob: 520922bf756ff5e75f927c5d0dc9cc81e65ca3e0
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  adr_0027_blob: 4dfb29c963cd5662265d3cb97f98be82212d5e08
  adr_0029_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  focus_index_validator_blob: 89391d75680e859dddf3696b9b782369f364c73e
  validator_registry_blob: 86aeadabe7104114c3f1efe60a8708ec11563bb1
  state_index_blob: 8d0b631bd53e6af3747417ee813c791fc67a9c3c
inspection_boundary: >-
  Current-session GitHub reads covered the complete prior v1.3 index,
  current `main@51d06e47d60e1071a5728267b5dac4255c4c338b`, the complete
  non-truncated recursive repository tree, all 105 direct county directories,
  every direct README and build-artifact filename, blob size, and county tree
  identity, plus open pull-request and task-branch search. The recount includes
  the user-identified Comanche, Decatur, and Dickinson merges and all newer
  county state through merged PR #3239. External source pages, source or rights
  review, evidence resolution, policy evaluation, fixtures, runtime, releases,
  corrections, rollback drills, deployments, and public endpoints were not
  exercised.
related:
  - docs/focus-mode/README.md
  - docs/focus-mode/counties/README.md
  - docs/focus-mode/counties/_template/county-build-plan.md
  - docs/focus-mode/state/STATE_INDEX.md
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0027-county-focus-mode-control-plane.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - contracts/focus_mode/focus_mode_payload.md
  - tools/validators/validate_focus_mode_index.py
  - tools/validators/validator_registry.json
tags: [kfm, focus-mode, county, index, inventory, collision-prevention, governed-ai, compatibility, non-publication]
notes:
  - "v1.0 replaces the stale chat-lineage collision register with a pinned current-repository inventory."
  - "v1.1 reconciles the Anderson County README after same-path modernization; PLAN_NAME_DRIFT remains open."
  - "v1.2 carries Allen forward over current main and recomputes the exact county inventory, including the already-merged Barber README."
  - "v1.3 repairs Edwards README filename drift, carries the merged Doniphan README forward, and reconciles every README fact visible in the non-truncated current tree; all lifecycle, validator, release, and publication claims remain fail-closed."
  - "v1.4 recomputes all 105 county rows on current main, clears only the resolved Decatur foreign-plan and Elk one-byte README findings, and preserves every remaining naming, identity, placement, validator, lifecycle, release, and publication hold."
  - "The inventory corrections do not decide the singular-versus-plural Focus documentation placement or authorize broader structural migration."
  - "Legacy P1/P2, lane, sensitivity, and source-seed signals are retained as PROPOSED planning context, not promoted as current repository fact."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# County Focus Mode Master Index

> **Purpose.** Navigate the 105 county planning entries currently tracked under `docs/focus-mode/counties/`, prevent accidental duplicate generation, and expose the repository drift that must be reconciled before any county can claim validated, payload-ready, released, or published state.

> [!IMPORTANT]
> **Every Kansas county has a current repository entry, but no county is proven ready.** At current-main inventory base `51d06e47d60e1071a5728267b5dac4255c4c338b`, the complete non-truncated county tree contains 105 county-shaped directories and exactly one direct build artifact in each. That evidence is sufficient to stop first-time duplicate generation; it is not evidence of semantic correctness, source rights, evidence closure, policy approval, validator success, release, or publication.

> [!CAUTION]
> **Placement remains a compatibility question.** Accepted Directory Rules v2 defines a Focus Mode as a composition scope but does not select one exact documentation tree. The current singular path exists; proposed ADR-0027 describes a plural, kebab-case target but remains unaccepted. This update only reconciles the existing index against current main; any county-lane move, directory rename, or parallel-tree creation remains on **HOLD**.

> [!WARNING]
> **Inventory is not lifecycle state.** A directory, README, build-plan file, table row, validator, passing check, commit, or pull request cannot create a governed `FocusModePayload`, promotion decision, release manifest, correction record, rollback target, deployment, or publication.

**Quick navigation:** [Status and terms](#1-status-and-terms) · [Repository snapshot](#2-repository-snapshot) · [County inventory](#3-master-county-inventory) · [Drift and validator boundary](#4-evidence-limits-drift-and-validator-boundary) · [Planning signals](#5-carried-forward-planning-signals) · [Collision result](#6-collision-prevention-result) · [References and maintenance](#7-cross-references-and-maintenance)

---

<a id="1-status-enum"></a>

## 1. Status and terms

The index uses inventory findings, not the dormant validator's lifecycle enum.

| Term | Meaning | Governing effect |
|---|---|---|
| `TRACKED_PAIR` | The expected current snake_case county directory contains an exact `README.md` and exact legacy `<county>_county_focus_mode_build_plan.md` filename; the README is more than one byte. | Confirms path presence only. |
| `README_1_BYTE` | The directory's README-like file is one byte. | Treat the lane explanation and ownership boundary as absent until reviewed. |
| `DIRECTORY_NAME_DRIFT` | Current directory spelling differs from the Kansas county identity used by the validator. | Reconcile through an explicit rename/migration slice; do not create a second writable lane. |
| `README_NAME_DRIFT` | The README-like filename is not `README.md`. | Repair the exact tracked path in a focused change. |
| `PLAN_NAME_DRIFT` | The expected legacy plan filename is absent and an alternate build artifact is present. | Inspect content and consumers before rename. |
| `FOREIGN_PLAN` | A directory contains a plan named for another county. | Treat county identity as conflicted and fail closed. |
| `DUPLICATE_TREE` | Two county directories resolve to the same Git tree. | Do not infer independent county content. |
| `NEEDS VERIFICATION` | Current evidence cannot support the material claim. | Do not advance lifecycle or public-use claims. |
| `NOT_RUN` | The named executable validation was not run in this documentation change. | A documentation check cannot substitute for it. |

> [!NOTE]
> The prior v0.3 states `register-complete`, `generated-artifact`, and `repo-collision` described a chat-lineage collision register. They are superseded here by the current recursive Git tree. Their useful planning hints are retained in [§5](#5-carried-forward-planning-signals), but they no longer describe repository coverage.

[↑ Back to top](#top)

---

<a id="2-aggregate-counts"></a>

## 2. Repository snapshot

The counts below come from non-truncated repository tree `2a70a8b7a8b9b6a096c818898286be545a09144a` at current-main inventory base `51d06e47d60e1071a5728267b5dac4255c4c338b`.

| Measure | Count | Evidence and limit |
|---|---:|---|
| Kansas counties in the validator reference list | **105** | Exact alphabetical reference tuple in `validate_focus_mode_index.py`. |
| County-shaped directories in the current lane | **105** | Direct children under `docs/focus-mode/counties/`, excluding `_template/`. |
| Exact expected snake_case directory names | **104** | Hodgeman is tracked as `hodgman_county/`. |
| Directories with an exact `README.md` | **105** | Edwards now has canonical `README.md`; the one-byte `README,md` placeholder is absent from the branch snapshot. |
| One-byte README-like files | **56** | All are exact `README.md` files; byte length is inventory evidence, not content-maturity proof. |
| Directories with an exact legacy plan filename | **96** | Nine counties use an alternate or incorrect plan filename. |
| County-directory build artifacts | **105** | Every directory has exactly one direct non-README build artifact. |
| Directories satisfying the validator's seven required filenames | **0** | Current directories use the older two-file layout; no lifecycle implication is inferred. |
| Directories with tree-level anomalies | **57** | Includes one-byte README and the bounded naming/identity findings recorded below. |
| County lifecycle states verified by executable validation | **0** | Validator not run and current tree does not match its configured root/layout. |
| County releases or publications verified | **0** | No release or publication evidence was inspected or inferred. |

### Authority snapshot

| Surface | Current evidence | Effect on this index |
|---|---|---|
| Accepted Directory Rules v2 | Adopted by ADR-0029; §12.4 defines Focus Mode as a composition scope and prohibits copying canonical domain records merely to populate scope directories. | Supports a human inventory under `docs/`; does not authorize a new parallel Focus tree. |
| Current Focus documentation lane | `docs/focus-mode/` exists and its README classifies the path as present but not final canonical placement. | Same-path documentation update is permitted; structural convergence stays on HOLD. |
| ADR-0027 | `proposed`; describes a plural, kebab-case county control plane. | Design evidence only; cannot authorize migration or lifecycle promotion. |
| County index validator | Exists, expects `docs/focus-modes/`, kebab-case lanes, a `Status` table, and seven required files. | Dormant/incompatible with the current singular snake_case two-file tree. |
| Validator registry | Contains no county Focus Mode validator entry. | Aggregate validation does not currently prove this index or county lanes. |
| This file | Human-readable current-tree inventory and collision-prevention surface. | No policy, release, publication, or machine-registry authority. |

[↑ Back to top](#top)

---

<a id="3-master-table-105-kansas-counties"></a>

## 3. Master county inventory

Every link below resolves in the pinned county tree. Link resolution proves only that the path existed at the evidence snapshot. Unless a later evidence-backed change says otherwise, each county remains **lifecycle `NEEDS VERIFICATION`**, owner **`NEEDS VERIFICATION`**, and executable validation **`NOT_RUN`**.

| County | Current directory | README-like file | Build artifact used for collision prevention | Inventory finding |
|---|---|---|---|---|
| [Allen](./allen_county/) | `allen_county` | [`README.md`](./allen_county/README.md) | [`allen_county_focus_mode_build_plan.md`](./allen_county/allen_county_focus_mode_build_plan.md) | `TRACKED_PAIR` |
| [Anderson](./anderson_county/) | `anderson_county` | [`README.md`](./anderson_county/README.md) | [`anderson_county_focus_mode_build_plan_FIXED.md`](./anderson_county/anderson_county_focus_mode_build_plan_FIXED.md) | `PLAN_NAME_DRIFT` |
| [Atchison](./atchison_county/) | `atchison_county` | [`README.md`](./atchison_county/README.md) | [`atchison_county_focus_mode_build_plan.md`](./atchison_county/atchison_county_focus_mode_build_plan.md) | `TRACKED_PAIR` |
| [Barber](./barber_county/) | `barber_county` | [`README.md`](./barber_county/README.md) | [`barber_county_focus_mode_build_plan.md`](./barber_county/barber_county_focus_mode_build_plan.md) | `TRACKED_PAIR` |
| [Barton](./barton_county/) | `barton_county` | [`README.md`](./barton_county/README.md) | [`barton_county_focus_mode_build_plan.md`](./barton_county/barton_county_focus_mode_build_plan.md) | `TRACKED_PAIR` |
| [Bourbon](./bourbon_county/) | `bourbon_county` | [`README.md`](./bourbon_county/README.md) | [`bourbon_county_focus_mode_build_plan.md`](./bourbon_county/bourbon_county_focus_mode_build_plan.md) | `TRACKED_PAIR` |
| [Brown](./brown_county/) | `brown_county` | [`README.md`](./brown_county/README.md) | [`brown_county_focus_mode_build_plan.md`](./brown_county/brown_county_focus_mode_build_plan.md) | `TRACKED_PAIR` |
| [Butler](./butler_county/) | `butler_county` | [`README.md`](./butler_county/README.md) | [`butler_county_focus_mode_build_plan.md`](./butler_county/butler_county_focus_mode_build_plan.md) | `TRACKED_PAIR` |
| [Chase](./chase_county/) | `chase_county` | [`README.md`](./chase_county/README.md) | [`chase_county_focus_mode_build_plan.md`](./chase_county/chase_county_focus_mode_build_plan.md) | `TRACKED_PAIR` |
| [Chautauqua](./chautauqua_county/) | `chautauqua_county` | [`README.md`](./chautauqua_county/README.md) | [`chautauqua_county_focus_mode_build_plan.md`](./chautauqua_county/chautauqua_county_focus_mode_build_plan.md) | `TRACKED_PAIR` |
| [Cherokee](./cherokee_county/) | `cherokee_county` | [`README.md`](./cherokee_county/README.md) | [`cherokee_county_focus_mode_build_plan.md`](./cherokee_county/cherokee_county_focus_mode_build_plan.md) | `TRACKED_PAIR` |
| [Cheyenne](./cheyenne_county/) | `cheyenne_county` | [`README.md`](./cheyenne_county/README.md) | [`cheyenne_county_focus_mode_build_plan.md`](./cheyenne_county/cheyenne_county_focus_mode_build_plan.md) | `TRACKED_PAIR` |
| [Clark](./clark_county/) | `clark_county` | [`README.md`](./clark_county/README.md) | [`clark_county_focus_mode_build_plan.md`](./clark_county/clark_county_focus_mode_build_plan.md) | `TRACKED_PAIR` |
| [Clay](./clay_county/) | `clay_county` | [`README.md`](./clay_county/README.md) | [`clay_county_focus_mode_build_plan.md`](./clay_county/clay_county_focus_mode_build_plan.md) | `TRACKED_PAIR` |
| [Cloud](./cloud_county/) | `cloud_county` | [`README.md`](./cloud_county/README.md) | [`cloud_county_focus_mode_build_plan.md`](./cloud_county/cloud_county_focus_mode_build_plan.md) | `TRACKED_PAIR` |
| [Coffey](./coffey_county/) | `coffey_county` | [`README.md`](./coffey_county/README.md) | [`coffey_county_focus_mode_build_plan.md`](./coffey_county/coffey_county_focus_mode_build_plan.md) | `TRACKED_PAIR` |
| [Comanche](./comanche_county/) | `comanche_county` | [`README.md`](./comanche_county/README.md) | [`comanche_county_focus_mode_build_plan.md`](./comanche_county/comanche_county_focus_mode_build_plan.md) | `TRACKED_PAIR` |
| [Cowley](./cowley_county/) | `cowley_county` | [`README.md`](./cowley_county/README.md) | [`cowley_county_focus_mode_build_plan.md`](./cowley_county/cowley_county_focus_mode_build_plan.md) | `TRACKED_PAIR` |
| [Crawford](./crawford_county/) | `crawford_county` | [`README.md`](./crawford_county/README.md) | [`crawford_county_focus_mode_build_plan.md`](./crawford_county/crawford_county_focus_mode_build_plan.md) | `TRACKED_PAIR` |
| [Decatur](./decatur_county/) | `decatur_county` | [`README.md`](./decatur_county/README.md) | [`decatur_county_focus_mode_build_plan.md`](./decatur_county/decatur_county_focus_mode_build_plan.md) | `TRACKED_PAIR` |
| [Dickinson](./dickinson_county/) | `dickinson_county` | [`README.md`](./dickinson_county/README.md) | [`dickinson_county_focus_mode_build_plan.md`](./dickinson_county/dickinson_county_focus_mode_build_plan.md) | `TRACKED_PAIR` |
| [Doniphan](./doniphan_county/) | `doniphan_county` | [`README.md`](./doniphan_county/README.md) | [`doniphan_county_focus_mode_build_plan.md`](./doniphan_county/doniphan_county_focus_mode_build_plan.md) | `TRACKED_PAIR` |
| [Douglas](./douglas_county/) | `douglas_county` | [`README.md`](./douglas_county/README.md) | [`douglas_county_focus_mode_build_plan.md`](./douglas_county/douglas_county_focus_mode_build_plan.md) | `TRACKED_PAIR` |
| [Edwards](./edwards_county/) | `edwards_county` | [`README.md`](./edwards_county/README.md) | [`edwards_county_focus_mode_build_plan.md`](./edwards_county/edwards_county_focus_mode_build_plan.md) | `TRACKED_PAIR` |
| [Elk](./elk_county/) | `elk_county` | [`README.md`](./elk_county/README.md) | [`elk_county_focus_mode_build_plan.md`](./elk_county/elk_county_focus_mode_build_plan.md) | `TRACKED_PAIR` |
| [Ellis](./ellis_county/) | `ellis_county` | [`README.md`](./ellis_county/README.md) | [`ellis_county_focus_mode_build_plan.md`](./ellis_county/ellis_county_focus_mode_build_plan.md) | `TRACKED_PAIR` |
| [Ellsworth](./ellsworth_county/) | `ellsworth_county` | [`README.md`](./ellsworth_county/README.md) | [`ellsworth_county_focus_mode_build_plan.md`](./ellsworth_county/ellsworth_county_focus_mode_build_plan.md) | `TRACKED_PAIR` |
| [Finney](./finney_county/) | `finney_county` | [`README.md`](./finney_county/README.md) | [`finney_county_focus_mode_build_plan.md`](./finney_county/finney_county_focus_mode_build_plan.md) | `TRACKED_PAIR` |
| [Ford](./ford_county/) | `ford_county` | [`README.md`](./ford_county/README.md) | [`ford_county_focus_mode_build_plan.md`](./ford_county/ford_county_focus_mode_build_plan.md) | `TRACKED_PAIR` |
| [Franklin](./franklin_county/) | `franklin_county` | [`README.md`](./franklin_county/README.md) · 1 byte | [`franklin_county_focus_mode_build_plan.md`](./franklin_county/franklin_county_focus_mode_build_plan.md) | `README_1_BYTE` |
| [Geary](./geary_county/) | `geary_county` | [`README.md`](./geary_county/README.md) | [`geary_county_focus_mode_build_plan.md`](./geary_county/geary_county_focus_mode_build_plan.md) | `TRACKED_PAIR` |
| [Gove](./gove_county/) | `gove_county` | [`README.md`](./gove_county/README.md) · 1 byte | [`gove_county_focus_mode_build_plan.md`](./gove_county/gove_county_focus_mode_build_plan.md) | `README_1_BYTE` |
| [Graham](./graham_county/) | `graham_county` | [`README.md`](./graham_county/README.md) · 1 byte | [`graham_county_focus_mode_build_plan.md`](./graham_county/graham_county_focus_mode_build_plan.md) | `README_1_BYTE` |
| [Grant](./grant_county/) | `grant_county` | [`README.md`](./grant_county/README.md) · 1 byte | [`grant_county_focus_mode_build_plan.md`](./grant_county/grant_county_focus_mode_build_plan.md) | `README_1_BYTE` |
| [Gray](./gray_county/) | `gray_county` | [`README.md`](./gray_county/README.md) · 1 byte | [`gray_county_focus_mode_build_plan.md`](./gray_county/gray_county_focus_mode_build_plan.md) | `README_1_BYTE` |
| [Greeley](./greeley_county/) | `greeley_county` | [`README.md`](./greeley_county/README.md) · 1 byte | [`greeley_county_focus_mode_build.md`](./greeley_county/greeley_county_focus_mode_build.md) | `README_1_BYTE`<br>`PLAN_NAME_DRIFT` |
| [Greenwood](./greenwood_county/) | `greenwood_county` | [`README.md`](./greenwood_county/README.md) · 1 byte | [`greenwood_county_focus_mode_build_plan.md`](./greenwood_county/greenwood_county_focus_mode_build_plan.md) | `README_1_BYTE` |
| [Hamilton](./hamilton_county/) | `hamilton_county` | [`README.md`](./hamilton_county/README.md) · 1 byte | [`hamilton_county_focus_mode_build_plan.md`](./hamilton_county/hamilton_county_focus_mode_build_plan.md) | `README_1_BYTE` |
| [Harper](./harper_county/) | `harper_county` | [`README.md`](./harper_county/README.md) · 1 byte | [`harper_county_focus_mode_build_plan.md`](./harper_county/harper_county_focus_mode_build_plan.md) | `README_1_BYTE` |
| [Harvey](./harvey_county/) | `harvey_county` | [`README.md`](./harvey_county/README.md) | [`harvey_county_focus_mode_build_plan.md`](./harvey_county/harvey_county_focus_mode_build_plan.md) | `TRACKED_PAIR` |
| [Haskell](./haskell_county/) | `haskell_county` | [`README.md`](./haskell_county/README.md) · 1 byte | [`haskell_county_focus_mode_build_plan.md`](./haskell_county/haskell_county_focus_mode_build_plan.md) | `README_1_BYTE` |
| [Hodgeman](./hodgman_county/) | `hodgman_county` | [`README.md`](./hodgman_county/README.md) · 1 byte | [`hodgman_county_focus_mode_build_plan.md`](./hodgman_county/hodgman_county_focus_mode_build_plan.md) | `README_1_BYTE`<br>`DIRECTORY_NAME_DRIFT`<br>`PLAN_NAME_DRIFT` |
| [Jackson](./jackson_county/) | `jackson_county` | [`README.md`](./jackson_county/README.md) | [`jackson_county_focus_mode_build_plan.md`](./jackson_county/jackson_county_focus_mode_build_plan.md) | `TRACKED_PAIR` |
| [Jefferson](./jefferson_county/) | `jefferson_county` | [`README.md`](./jefferson_county/README.md) · 1 byte | [`jefferson_county_focus_mode_build_plan.md`](./jefferson_county/jefferson_county_focus_mode_build_plan.md) | `README_1_BYTE` |
| [Jewell](./jewell_county/) | `jewell_county` | [`README.md`](./jewell_county/README.md) · 1 byte | [`jewell_county_focus_mode_build_plan.md`](./jewell_county/jewell_county_focus_mode_build_plan.md) | `README_1_BYTE` |
| [Johnson](./johnson_county/) | `johnson_county` | [`README.md`](./johnson_county/README.md) | [`johnson_county_focus_mode_build_plan.md`](./johnson_county/johnson_county_focus_mode_build_plan.md) | `TRACKED_PAIR` |
| [Kearny](./kearny_county/) | `kearny_county` | [`README.md`](./kearny_county/README.md) · 1 byte | [`kearny_county_focus_mode_build_plan.md`](./kearny_county/kearny_county_focus_mode_build_plan.md) | `README_1_BYTE` |
| [Kingman](./kingman_county/) | `kingman_county` | [`README.md`](./kingman_county/README.md) · 1 byte | [`kingman_county_focus_mode_build_plan.md`](./kingman_county/kingman_county_focus_mode_build_plan.md) | `README_1_BYTE` |
| [Kiowa](./kiowa_county/) | `kiowa_county` | [`README.md`](./kiowa_county/README.md) · 1 byte | [`kiowa_county_focus_mode_build_plan.md`](./kiowa_county/kiowa_county_focus_mode_build_plan.md) | `README_1_BYTE` |
| [Labette](./labette_county/) | `labette_county` | [`README.md`](./labette_county/README.md) · 1 byte | [`labette_county_focus_mode_build_plan.md`](./labette_county/labette_county_focus_mode_build_plan.md) | `README_1_BYTE` |
| [Lane](./lane_county/) | `lane_county` | [`README.md`](./lane_county/README.md) · 1 byte | [`lane_county_focus_mode_build_plan.md`](./lane_county/lane_county_focus_mode_build_plan.md) | `README_1_BYTE` |
| [Leavenworth](./leavenworth_county/) | `leavenworth_county` | [`README.md`](./leavenworth_county/README.md) | [`leavenworth_county_focus_mode_build_plan.md`](./leavenworth_county/leavenworth_county_focus_mode_build_plan.md) | `TRACKED_PAIR` |
| [Lincoln](./lincoln_county/) | `lincoln_county` | [`README.md`](./lincoln_county/README.md) · 1 byte | [`lincoln_county_focus_mode_build_plan.md`](./lincoln_county/lincoln_county_focus_mode_build_plan.md) | `README_1_BYTE` |
| [Linn](./linn_county/) | `linn_county` | [`README.md`](./linn_county/README.md) | [`linn_county_focus_mode_build_plan.md`](./linn_county/linn_county_focus_mode_build_plan.md) | `TRACKED_PAIR` |
| [Logan](./logan_county/) | `logan_county` | [`README.md`](./logan_county/README.md) · 1 byte | [`logan_county_focus_mode_build_plan.md`](./logan_county/logan_county_focus_mode_build_plan.md) | `README_1_BYTE` |
| [Lyon](./lyon_county/) | `lyon_county` | [`README.md`](./lyon_county/README.md) | [`lyon_county_focus_mode_build_plan.md`](./lyon_county/lyon_county_focus_mode_build_plan.md) | `TRACKED_PAIR` |
| [Marion](./marion_county/) | `marion_county` | [`README.md`](./marion_county/README.md) · 1 byte | [`marion_county_focus_mode_build_plan.md`](./marion_county/marion_county_focus_mode_build_plan.md) | `README_1_BYTE` |
| [Marshall](./marshall_county/) | `marshall_county` | [`README.md`](./marshall_county/README.md) · 1 byte | [`marshall_county_focus_mode_build_plan.md`](./marshall_county/marshall_county_focus_mode_build_plan.md) | `README_1_BYTE` |
| [McPherson](./mcpherson_county/) | `mcpherson_county` | [`README.md`](./mcpherson_county/README.md) | [`mcpherson_county_focus_mode_build_plan.md`](./mcpherson_county/mcpherson_county_focus_mode_build_plan.md) | `TRACKED_PAIR` |
| [Meade](./meade_county/) | `meade_county` | [`README.md`](./meade_county/README.md) · 1 byte | [`meade_county_focus_mode_build_plan.md`](./meade_county/meade_county_focus_mode_build_plan.md) | `README_1_BYTE` |
| [Miami](./miami_county/) | `miami_county` | [`README.md`](./miami_county/README.md) | [`miami_county_focus_mode_build_plan.md`](./miami_county/miami_county_focus_mode_build_plan.md) | `TRACKED_PAIR` |
| [Mitchell](./mitchell_county/) | `mitchell_county` | [`README.md`](./mitchell_county/README.md) · 1 byte | [`mitchell_county_focus_mode_build_plan.md`](./mitchell_county/mitchell_county_focus_mode_build_plan.md) | `README_1_BYTE` |
| [Montgomery](./montgomery_county/) | `montgomery_county` | [`README.md`](./montgomery_county/README.md) · 1 byte | [`montgomery_county_focus_mode_build_plan.md`](./montgomery_county/montgomery_county_focus_mode_build_plan.md) | `README_1_BYTE` |
| [Morris](./morris_county/) | `morris_county` | [`README.md`](./morris_county/README.md) | [`morris_county_focus_mode_build_plan.md`](./morris_county/morris_county_focus_mode_build_plan.md) | `TRACKED_PAIR` |
| [Morton](./morton_county/) | `morton_county` | [`README.md`](./morton_county/README.md) · 1 byte | [`morton_county_focus_mode_build_plan.md`](./morton_county/morton_county_focus_mode_build_plan.md) | `README_1_BYTE` |
| [Nemaha](./nemaha_county/) | `nemaha_county` | [`README.md`](./nemaha_county/README.md) · 1 byte | [`nemaha_county_build_plan.md`](./nemaha_county/nemaha_county_build_plan.md) | `README_1_BYTE`<br>`PLAN_NAME_DRIFT` |
| [Neosho](./neosho_county/) | `neosho_county` | [`README.md`](./neosho_county/README.md) · 1 byte | [`neosho_county_focus_mode_build_plan.md`](./neosho_county/neosho_county_focus_mode_build_plan.md) | `README_1_BYTE` |
| [Ness](./ness_county/) | `ness_county` | [`README.md`](./ness_county/README.md) · 1 byte | [`ness_county_focus_mode_build_plan.md`](./ness_county/ness_county_focus_mode_build_plan.md) | `README_1_BYTE` |
| [Norton](./norton_county/) | `norton_county` | [`README.md`](./norton_county/README.md) · 1 byte | [`norton_county_focus_mode_build_plan.md`](./norton_county/norton_county_focus_mode_build_plan.md) | `README_1_BYTE` |
| [Osage](./osage_county/) | `osage_county` | [`README.md`](./osage_county/README.md) | [`osage_county_focus_mode_build_plan.md`](./osage_county/osage_county_focus_mode_build_plan.md) | `TRACKED_PAIR` |
| [Osborne](./osborne_county/) | `osborne_county` | [`README.md`](./osborne_county/README.md) · 1 byte | [`osborne_county_focus_mode_build_plan.md`](./osborne_county/osborne_county_focus_mode_build_plan.md) | `README_1_BYTE` |
| [Ottawa](./ottawa_county/) | `ottawa_county` | [`README.md`](./ottawa_county/README.md) · 1 byte | [`ottawa_county_focus_mode_build_plan.md`](./ottawa_county/ottawa_county_focus_mode_build_plan.md) | `README_1_BYTE` |
| [Pawnee](./pawnee_county/) | `pawnee_county` | [`README.md`](./pawnee_county/README.md) · 1 byte | [`pawnee_county_focus_mode_build_plan.md`](./pawnee_county/pawnee_county_focus_mode_build_plan.md) | `README_1_BYTE` |
| [Phillips](./phillips_county/) | `phillips_county` | [`README.md`](./phillips_county/README.md) · 1 byte | [`phillips_county_focus_mode_build_plan.md`](./phillips_county/phillips_county_focus_mode_build_plan.md) | `README_1_BYTE` |
| [Pottawatomie](./pottawatomie_county/) | `pottawatomie_county` | [`README.md`](./pottawatomie_county/README.md) | [`pottawatomie_county_focus_mode_build_plan.md`](./pottawatomie_county/pottawatomie_county_focus_mode_build_plan.md) | `TRACKED_PAIR` |
| [Pratt](./pratt_county/) | `pratt_county` | [`README.md`](./pratt_county/README.md) · 1 byte | [`pratt_county_focus_mode_build_plan.md`](./pratt_county/pratt_county_focus_mode_build_plan.md) | `README_1_BYTE` |
| [Rawlins](./rawlins_county/) | `rawlins_county` | [`README.md`](./rawlins_county/README.md) · 1 byte | [`rawlins_county_focus_mode_build_plan.md`](./rawlins_county/rawlins_county_focus_mode_build_plan.md) | `README_1_BYTE` |
| [Reno](./reno_county/) | `reno_county` | [`README.md`](./reno_county/README.md) | [`reno_county_focus_mode_build_plan.md`](./reno_county/reno_county_focus_mode_build_plan.md) | `TRACKED_PAIR` |
| [Republic](./republic_county/) | `republic_county` | [`README.md`](./republic_county/README.md) · 1 byte | [`republic_county_focus_mode_build_plan.md`](./republic_county/republic_county_focus_mode_build_plan.md) | `README_1_BYTE` |
| [Rice](./rice_county/) | `rice_county` | [`README.md`](./rice_county/README.md) | [`rice_county_focus_mode_build_plan.md`](./rice_county/rice_county_focus_mode_build_plan.md) | `TRACKED_PAIR` |
| [Riley](./riley_county/) | `riley_county` | [`README.md`](./riley_county/README.md) | [`riley_county_focus_mode_build_plan.md`](./riley_county/riley_county_focus_mode_build_plan.md) | `TRACKED_PAIR` |
| [Rooks](./rooks_county/) | `rooks_county` | [`README.md`](./rooks_county/README.md) · 1 byte | [`rooks_county_focus_mode_build_plan.md`](./rooks_county/rooks_county_focus_mode_build_plan.md) | `README_1_BYTE` |
| [Rush](./rush_county/) | `rush_county` | [`README.md`](./rush_county/README.md) · 1 byte | [`rush_county_focus_mode_build_plan.md`](./rush_county/rush_county_focus_mode_build_plan.md) | `README_1_BYTE` |
| [Russell](./russell_county/) | `russell_county` | [`README.md`](./russell_county/README.md) · 1 byte | [`Russell_county_build_plan.md`](./russell_county/Russell_county_build_plan.md) | `README_1_BYTE`<br>`PLAN_NAME_DRIFT` |
| [Saline](./saline_county/) | `saline_county` | [`README.md`](./saline_county/README.md) | [`saline_county_focus_mode_build_plan.md`](./saline_county/saline_county_focus_mode_build_plan.md) | `TRACKED_PAIR` |
| [Scott](./scott_county/) | `scott_county` | [`README.md`](./scott_county/README.md) · 1 byte | [`scott_county_focus_mode_build_plan.md`](./scott_county/scott_county_focus_mode_build_plan.md) | `README_1_BYTE` |
| [Sedgwick](./sedgwick_county/) | `sedgwick_county` | [`README.md`](./sedgwick_county/README.md) | [`sedgwick_county_focus_mode_build_plan.md`](./sedgwick_county/sedgwick_county_focus_mode_build_plan.md) | `TRACKED_PAIR` |
| [Seward](./seward_county/) | `seward_county` | [`README.md`](./seward_county/README.md) · 1 byte | [`seward_county_focus_mode_build_plan.md`](./seward_county/seward_county_focus_mode_build_plan.md) | `README_1_BYTE` |
| [Shawnee](./shawnee_county/) | `shawnee_county` | [`README.md`](./shawnee_county/README.md) | [`shawnee_county_focus_mode_build_plan.md`](./shawnee_county/shawnee_county_focus_mode_build_plan.md) | `TRACKED_PAIR` |
| [Sheridan](./sheridan_county/) | `sheridan_county` | [`README.md`](./sheridan_county/README.md) · 1 byte | [`sheridan_county_focus_mode_build_plan.md`](./sheridan_county/sheridan_county_focus_mode_build_plan.md) | `README_1_BYTE` |
| [Sherman](./sherman_county/) | `sherman_county` | [`README.md`](./sherman_county/README.md) · 1 byte | [`stevens_county_focus_mode_build_plan.md`](./sherman_county/stevens_county_focus_mode_build_plan.md) | `README_1_BYTE`<br>`PLAN_NAME_DRIFT`<br>`FOREIGN_PLAN`<br>`DUPLICATE_TREE` |
| [Smith](./smith_county/) | `smith_county` | [`README.md`](./smith_county/README.md) · 1 byte | [`smith_county_build_plan.md`](./smith_county/smith_county_build_plan.md) | `README_1_BYTE`<br>`PLAN_NAME_DRIFT` |
| [Stafford](./stafford_county/) | `stafford_county` | [`README.md`](./stafford_county/README.md) | [`stafford_county_focus_mode_build_plan.md`](./stafford_county/stafford_county_focus_mode_build_plan.md) | `TRACKED_PAIR` |
| [Stanton](./stanton_county/) | `stanton_county` | [`README.md`](./stanton_county/README.md) · 1 byte | [`stanton_county_focus_mode_build_plan.md`](./stanton_county/stanton_county_focus_mode_build_plan.md) | `README_1_BYTE` |
| [Stevens](./stevens_county/) | `stevens_county` | [`README.md`](./stevens_county/README.md) · 1 byte | [`stevens_county_focus_mode_build_plan.md`](./stevens_county/stevens_county_focus_mode_build_plan.md) | `README_1_BYTE`<br>`DUPLICATE_TREE` |
| [Sumner](./sumner_county/) | `sumner_county` | [`README.md`](./sumner_county/README.md) · 1 byte | [`sumner_county_focu_build_plan.md`](./sumner_county/sumner_county_focu_build_plan.md) | `README_1_BYTE`<br>`PLAN_NAME_DRIFT` |
| [Thomas](./thomas_county/) | `thomas_county` | [`README.md`](./thomas_county/README.md) · 1 byte | [`thomas_county_focus_mode_build_plan.md`](./thomas_county/thomas_county_focus_mode_build_plan.md) | `README_1_BYTE` |
| [Trego](./trego_county/) | `trego_county` | [`README.md`](./trego_county/README.md) · 1 byte | [`trego_county_focus_mode_build_plan.md`](./trego_county/trego_county_focus_mode_build_plan.md) | `README_1_BYTE` |
| [Wabaunsee](./wabaunsee_county/) | `wabaunsee_county` | [`README.md`](./wabaunsee_county/README.md) · 1 byte | [`wabaunsee_county_focus_mode_build_plan.md`](./wabaunsee_county/wabaunsee_county_focus_mode_build_plan.md) | `README_1_BYTE` |
| [Wallace](./wallace_county/) | `wallace_county` | [`README.md`](./wallace_county/README.md) · 1 byte | [`wallace_county_focus_mode_build_plan.md`](./wallace_county/wallace_county_focus_mode_build_plan.md) | `README_1_BYTE` |
| [Washington](./washington_county/) | `washington_county` | [`README.md`](./washington_county/README.md) · 1 byte | [`washington_county_focus_mode_build_plan.md`](./washington_county/washington_county_focus_mode_build_plan.md) | `README_1_BYTE` |
| [Wichita](./wichita_county/) | `wichita_county` | [`README.md`](./wichita_county/README.md) · 1 byte | [`wichita_county_build_plan.md`](./wichita_county/wichita_county_build_plan.md) | `README_1_BYTE`<br>`PLAN_NAME_DRIFT` |
| [Wilson](./wilson_county/) | `wilson_county` | [`README.md`](./wilson_county/README.md) · 1 byte | [`wilson_county_focus_mode_build_plan.md`](./wilson_county/wilson_county_focus_mode_build_plan.md) | `README_1_BYTE` |
| [Woodson](./woodson_county/) | `woodson_county` | [`README.md`](./woodson_county/README.md) · 1 byte | [`woodson_county_focus_mode_build_plan.md`](./woodson_county/woodson_county_focus_mode_build_plan.md) | `README_1_BYTE` |
| [Wyandotte](./wyandotte_county/) | `wyandotte_county` | [`README.md`](./wyandotte_county/README.md) | [`wyandotte_county_focus_mode_build_plan.md`](./wyandotte_county/wyandotte_county_focus_mode_build_plan.md) | `TRACKED_PAIR` |

[↑ Back to top](#top)

---

<a id="4-notes-on-corpus-evidence-generated-artifacts-and-discrepancies"></a>

## 4. Evidence limits, drift, and validator boundary

### Current drift ledger

| ID | Confirmed finding | Consequence | Smallest safe follow-up |
|---|---|---|---|
| `COUNTY-INV-001` | Current county materials use singular `docs/focus-mode/counties/`; ADR-0027's plural placement remains proposed. | Exact canonical migration target is unresolved. | Keep this lane single-write; decide ADR-0027 before structural migration. |
| `COUNTY-INV-002` | Current lanes use snake_case directories and verbose plan filenames; the validator expects kebab-case lane directories and seven fixed filenames. | The current validator cannot establish county maturity here. | Reconcile validator, index grammar, and placement as one dependency-closed control-plane slice after authority is settled. |
| `COUNTY-INV-003` | Hodgeman is represented by `hodgman_county/`; the correctly spelled `hodgeman_county/` path is absent. | County identity and path spelling are inconsistent. | Inspect inbound references and rename through one single-write migration with rollback. |
| `COUNTY-INV-004` | **RESOLVED IN v1.3:** Edwards has substantive `README.md`; the one-byte `README,md` placeholder is absent from the branch snapshot. | Standard README discovery is restored; the snapshot-scoped topology baseline may retain historical Edwards anomalies until validator-owned regeneration. | Keep the canonical filename; do not reintroduce the typo or weaken the topology convergence ratchet. |
| `COUNTY-INV-005` | Anderson, Greeley, Nemaha, Russell, Smith, Sumner, and Wichita use alternate or malformed plan filenames. | Filename-based tooling and navigation are unreliable. | Repair one bounded naming cohort with exact consumer checks and rollback. |
| `COUNTY-INV-006` | **RESOLVED IN v1.4:** Decatur contains only its own plan; the prior Stevens-named foreign plan is absent from the current tree. | The tree-level foreign-plan conflict is cleared; plan content correctness remains `NEEDS VERIFICATION`. | Keep the county-local filename; treat any semantic or provenance review as a separate evidence-backed change. |
| `COUNTY-INV-007` | Sherman and Stevens share tree `8c963f0daac7582822b0e7ec84d37275ec04e34e`; both contain a Stevens-named plan. | Sherman cannot be treated as independently implemented. | Reconstruct Sherman identity from source/history in a separate correction PR. |
| `COUNTY-INV-008` | 56 README files are one byte; 49 are substantive by byte length. | Directory presence does not establish lane responsibility, ownership, or usage. | Build or repair leaf READMEs only from verified county content and inherited lane rules. |
| `COUNTY-INV-009` | No current county directory contains the validator's seven required filenames. | No row can be promoted to `draft` or beyond from tree shape alone. | Treat every lifecycle state as `NEEDS VERIFICATION`; do not weaken the validator. |
| `COUNTY-INV-010` | Per-county source descriptors, rights, evidence resolution, policy outcomes, releases, corrections, and rollback execution were not inspected exhaustively. | Content and public fitness remain unknown. | Verify one county at a time through governed evidence and release boundaries. |

### Validator contract mismatch

The current validator is useful design evidence but is not a passing gate for this tree:

```text
validator root:       docs/focus-modes/
current root:         docs/focus-mode/counties/
validator lane:       <county>-county/
current lane:         <county>_county/
validator files:      README.md, build-plan.md, layer-registry.md,
                      evidence-model.md, acceptance-checklist.md,
                      source-seed-list.md, public-safety-notes.md
current common files: README.md plus <county>_county_focus_mode_build_plan.md
registry entry:       absent
execution this PR:    NOT_RUN
```

> [!IMPORTANT]
> Do not make the document appear validator-compatible by assigning false lifecycle statuses or weakening checks. The legitimate closure is to reconcile placement, table grammar, file layout, registry wiring, fixtures, and tests under accepted authority.

### What the snapshot does not prove

- that a build artifact is about the county named by its directory;
- that its sources exist, are current, or carry usable rights;
- that every claim resolves from `EvidenceRef` to `EvidenceBundle`;
- that sensitivity, sovereignty, harmful precision, or living-person risks were reviewed;
- that a governed API can produce finite `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` outcomes;
- that any payload, map layer, AI answer, correction path, rollback target, release, deployment, or publication exists.

[↑ Back to top](#top)

---

<a id="5-priority-subset-p1--directory-rules-v12"></a>

## 5. Carried-forward planning signals

The prior index's lane IDs, P1/P2 cohort, sensitivity hints, and source-seed families are retained below to avoid losing planning context. They are **PROPOSED legacy signals**, not current Directory Rules v2 requirements, registered source evidence, rights clearance, validation results, or release priorities.

### Legacy P1 cohort

| County | Carried-forward rationale |
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

> [!NOTE]
> Accepted Directory Rules v2 §12.4 does not define this cohort. Changing a planning priority does not change evidence, policy, promotion, release, or publication state.

### Default sensitivity posture

| Sensitivity lane | Default bounded posture |
|---|---|
| Parcel/title and land-person joins | `ABSTAIN` or `DENY` when identity, rights, or reidentification risk is unresolved |
| Exact archaeology and burial/sacred locations | `DENY`; use reviewed aggregation or generalization only |
| Rare-species exact locations | `DENY` or generalize under policy |
| Critical-infrastructure exact detail | `DENY` or generalize under policy |
| Living-person identifiers | `DENY` absent explicit lawful, policy-approved need |
| DNA/genomic information | `DENY` by default |
| Emergency-alert interpretation | `ABSTAIN`; do not substitute KFM for the responsible authority |

### Legacy per-county planning table

| County | Proposed logical lane | Legacy priority | Sensitivity planning signal | Source-seed planning signal |
|---|---|---|---|---|
| Allen | `allen-county` | P2 | defaults | County/City GIS · KDOT · KDA/NASS |
| Anderson | `anderson-county` | P2 | defaults | County/City GIS · KDOT |
| Atchison | `atchison-county` | P2 | defaults | County/City GIS · KDOT · KSHS |
| Barber | `barber-county` | P2 | defaults | County/City GIS · KDOT |
| Barton | `barton-county` | P2 | defaults · critical_infrastructure_exact | County/City GIS · KDOT · KGS |
| Bourbon | `bourbon-county` | P2 | defaults | County/City GIS · KDOT |
| Brown | `brown-county` | P2 | defaults | County/City GIS · KDOT |
| Butler | `butler-county` | P2 | defaults | County/City GIS · KDOT |
| Chase | `chase-county` | P2 | defaults | County/City GIS · KDOT |
| Chautauqua | `chautauqua-county` | P2 | defaults | County/City GIS · KDOT |
| Cherokee | `cherokee-county` | P2 | defaults | County/City GIS · KDOT · KGS |
| Cheyenne | `cheyenne-county` | P2 | defaults | County/City GIS · KDOT |
| Clark | `clark-county` | P2 | defaults | County/City GIS · KDOT |
| Clay | `clay-county` | P2 | defaults | County/City GIS · KDOT |
| Cloud | `cloud-county` | P2 | defaults | County/City GIS · KDOT · KSHS |
| Coffey | `coffey-county` | P2 | defaults | County/City GIS · KDOT |
| Comanche | `comanche-county` | P2 | defaults | County/City GIS · KDOT |
| Cowley | `cowley-county` | P2 | defaults | County/City GIS · KDOT |
| Crawford | `crawford-county` | P2 | defaults | County/City GIS · KDOT |
| Decatur | `decatur-county` | P2 | defaults | County/City GIS · KDOT |
| Dickinson | `dickinson-county` | P2 | defaults | County/City GIS · KDOT |
| Doniphan | `doniphan-county` | P2 | defaults | County/City GIS · KDOT |
| Douglas | `douglas-county` | P1 | defaults · living_person_identifiers | County/City GIS · KDOT · KSHS · KU |
| Edwards | `edwards-county` | P2 | defaults | County/City GIS · KDOT |
| Elk | `elk-county` | P2 | defaults | County/City GIS · KDOT |
| Ellis | `ellis-county` | P1 | defaults | County/City GIS · KDOT · KGS |
| Ellsworth | `ellsworth-county` | P2 | defaults · exact_archaeology | County/City GIS · KDOT · KSHS · KHRI |
| Finney | `finney-county` | P1 | defaults · critical_infrastructure_exact | County/City GIS · KDOT · KDA/NASS |
| Ford | `ford-county` | P2 | defaults | County/City GIS · KDOT · KDA/NASS |
| Franklin | `franklin-county` | P2 | defaults | County/City GIS · KDOT |
| Geary | `geary-county` | P2 | defaults · critical_infrastructure_exact | County/City GIS · KDOT · DoD |
| Gove | `gove-county` | P2 | defaults | County/City GIS · KDOT |
| Graham | `graham-county` | P2 | defaults | County/City GIS · KDOT |
| Grant | `grant-county` | P2 | defaults | County/City GIS · KDOT |
| Gray | `gray-county` | P2 | defaults | County/City GIS · KDOT |
| Greeley | `greeley-county` | — | defaults | County/City GIS · KDOT · KDA-DWR · KGS · NASS |
| Greenwood | `greenwood-county` | P2 | defaults | County/City GIS · KDOT |
| Hamilton | `hamilton-county` | P2 | defaults | County/City GIS · KDOT |
| Harper | `harper-county` | — | defaults | County/City GIS · KDOT · KDA-DWR · KGS/KCC · NASS |
| Harvey | `harvey-county` | P2 | defaults | County/City GIS · KDOT |
| Haskell | `haskell-county` | P2 | defaults | County/City GIS · KDOT |
| Hodgeman | `hodgeman-county` | P2 | defaults | County/City GIS · KDOT |
| Jackson | `jackson-county` | P2 | defaults | County/City GIS · KDOT |
| Jefferson | `jefferson-county` | P2 | defaults | County/City GIS · KDOT |
| Jewell | `jewell-county` | P2 | defaults | County/City GIS · KDOT |
| Johnson | `johnson-county` | P1 | defaults · living_person_identifiers · critical_infrastructure_exact | County/City GIS · KDOT · KU/KCK |
| Kearny | `kearny-county` | P2 | defaults | County/City GIS · KDOT |
| Kingman | `kingman-county` | P2 | defaults | County/City GIS · KDOT |
| Kiowa | `kiowa-county` | P2 | defaults | County/City GIS · KDOT · NWS |
| Labette | `labette-county` | P2 | defaults | County/City GIS · KDOT |
| Lane | `lane-county` | — | defaults | County/City GIS · KDOT · KDA-DWR/GMD1 · KGS · NASS |
| Leavenworth | `leavenworth-county` | P1 | defaults · critical_infrastructure_exact | County/City GIS · KDOT · DoD |
| Lincoln | `lincoln-county` | — | defaults | County/City GIS · KDOT · KSHS · KGS |
| Linn | `linn-county` | P2 | defaults | County/City GIS · KDOT |
| Logan | `logan-county` | P2 | defaults | County/City GIS · KDOT |
| Lyon | `lyon-county` | P2 | defaults | County/City GIS · KDOT |
| Marion | `marion-county` | P2 | defaults | County/City GIS · KDOT |
| Marshall | `marshall-county` | P2 | defaults | County/City GIS · KDOT |
| McPherson | `mcpherson-county` | P2 | defaults | County/City GIS · KDOT |
| Meade | `meade-county` | P2 | defaults | County/City GIS · KDOT |
| Miami | `miami-county` | P2 | defaults | County/City GIS · KDOT |
| Mitchell | `mitchell-county` | P2 | defaults | County/City GIS · KDOT |
| Montgomery | `montgomery-county` | P2 | defaults | County/City GIS · KDOT |
| Morris | `morris-county` | P2 | defaults | County/City GIS · KDOT |
| Morton | `morton-county` | P2 | defaults | County/City GIS · KDOT |
| Nemaha | `nemaha-county` | — | defaults | County/City GIS · KDOT · KSHS · hydrology |
| Neosho | `neosho-county` | P2 | defaults | County/City GIS · KDOT |
| Ness | `ness-county` | — | defaults | County/City GIS · KDOT · KGS · fossil/geology |
| Norton | `norton-county` | P2 | defaults | County/City GIS · KDOT |
| Osage | `osage-county` | P2 | defaults | County/City GIS · KDOT |
| Osborne | `osborne-county` | P2 | defaults | County/City GIS · KDOT |
| Ottawa | `ottawa-county` | P2 | defaults | County/City GIS · KDOT |
| Pawnee | `pawnee-county` | P2 | defaults | County/City GIS · KDOT |
| Phillips | `phillips-county` | P2 | defaults | County/City GIS · KDOT |
| Pottawatomie | `pottawatomie-county` | P2 | defaults | County/City GIS · KDOT |
| Pratt | `pratt-county` | P2 | defaults | County/City GIS · KDOT |
| Rawlins | `rawlins-county` | P2 | defaults | County/City GIS · KDOT |
| Reno | `reno-county` | P1 | defaults | County/City GIS · KDOT |
| Republic | `republic-county` | P2 | defaults | County/City GIS · KDOT |
| Rice | `rice-county` | P2 | defaults | County/City GIS · KDOT |
| Riley | `riley-county` | P1 | defaults · critical_infrastructure_exact | County/City GIS · KDOT · DoD · KSU |
| Rooks | `rooks-county` | P2 | defaults | County/City GIS · KDOT |
| Rush | `rush-county` | P2 | defaults | County/City GIS · KDOT |
| Russell | `russell-county` | P2 | defaults | County/City GIS · KDOT |
| Saline | `saline-county` | P1 | defaults | County/City GIS · KDOT |
| Scott | `scott-county` | P2 | defaults | County/City GIS · KDOT |
| Sedgwick | `sedgwick-county` | P1 | defaults · living_person_identifiers · critical_infrastructure_exact | County/City GIS · KDOT · WSU |
| Seward | `seward-county` | P2 | defaults | County/City GIS · KDOT |
| Shawnee | `shawnee-county` | P1 | defaults · living_person_identifiers · critical_infrastructure_exact | County/City GIS · KDOT · KSHS · State Capitol |
| Sheridan | `sheridan-county` | — | defaults | County/City GIS · KDOT · KDA-DWR/GMD4 · KGS · KDWP · KSHS |
| Sherman | `sherman-county` | P2 | defaults | County/City GIS · KDOT |
| Smith | `smith-county` | — | defaults | County/City GIS · KDOT · hydrology · KSHS |
| Stafford | `stafford-county` | P2 | defaults | County/City GIS · KDOT |
| Stanton | `stanton-county` | — | defaults | County/City GIS · KDOT · KDA-DWR · KGS · NASS |
| Stevens | `stevens-county` | P2 | defaults | County/City GIS · KDOT |
| Sumner | `sumner-county` | P2 | defaults | County/City GIS · KDOT |
| Thomas | `thomas-county` | P2 | defaults | County/City GIS · KDOT |
| Trego | `trego-county` | P2 | defaults | County/City GIS · KDOT |
| Wabaunsee | `wabaunsee-county` | P2 | defaults | County/City GIS · KDOT |
| Wallace | `wallace-county` | P2 | defaults | County/City GIS · KDOT |
| Washington | `washington-county` | P2 | defaults | County/City GIS · KDOT |
| Wichita | `wichita-county` | — | defaults | County/City GIS · KDOT · KDA-DWR · KGS · NASS |
| Wilson | `wilson-county` | P2 | defaults | County/City GIS · KDOT |
| Woodson | `woodson-county` | P2 | defaults | County/City GIS · KDOT |
| Wyandotte | `wyandotte-county` | P1 | defaults · living_person_identifiers · critical_infrastructure_exact | County/City GIS · KDOT · KCK |

> [!CAUTION]
> A source name in this table is only a research lead. Before use, resolve the registered source identity, authority role, terms and rights, access method, temporal coverage, sensitivity, provenance, correction behavior, and release eligibility. The build-artifact links in §3 are the review starting points; this appendix is not a source registry.

[↑ Back to top](#top)

---

<a id="6-collision-prevention-result"></a>

## 6. Collision-prevention result

| Question | Repository-grounded result |
|---|---|
| Is any Kansas county absent from the current county-shaped directory set? | **No.** All 105 validator reference names map to a current directory entry, with Hodgeman represented by the misspelled `hodgman_county/`. |
| Does each county directory contain a build artifact? | **Yes, by tree presence.** Content correctness remains `NEEDS VERIFICATION`. |
| Can an assistant safely generate a new first-time county plan? | **No.** The safe authoring posture is `ABSTAIN` from duplicate generation and inspect the existing artifact. |
| Does the inventory prove implementation or release? | **No.** Zero county lifecycle states, validator passes, releases, or publications are claimed. |
| What work is safe next? | Revision, identity repair, filename correction, content validation, source and rights review, fixture construction, or control-plane convergence under accepted authority. |
| What remains prohibited by this index? | Treating presence as truth; creating a parallel writable county lane; bypassing evidence or policy; or inferring promotion, release, deployment, or publication. |

### County repair sequence

1. Pin the selected county directory tree and every inbound reference.
2. Read the complete README and build artifact; identify county identity, owner, source, rights, evidence, sensitivity, and rollback gaps.
3. Distinguish filename/path correction from semantic county-plan repair.
4. Keep any structural move isolated from the still-proposed ADR-0027 decision.
5. Add deterministic positive and negative proof without production data or network dependence.
6. Update this index only from verified repository state; never advance lifecycle from prose alone.

[↑ Back to top](#top)

---

<a id="7-cross-references"></a>

## 7. Cross-references and maintenance

### Current repository references

- [Focus Mode documentation control and compatibility lane](../README.md)
- [County lane README](./README.md)
- [County build-plan template](./_template/county-build-plan.md)
- [State Focus Mode index](../state/STATE_INDEX.md)
- [Accepted Directory Rules v2](../../doctrine/directory-rules.md)
- [ADR-0027 — County Focus Mode Control Plane](../../adr/ADR-0027-county-focus-mode-control-plane.md)
- [ADR-0029 — Adopt Directory Governance Standard v2](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
- [FocusModePayload semantic contract](../../../contracts/focus_mode/focus_mode_payload.md)
- [County Focus Mode index validator](../../../tools/validators/validate_focus_mode_index.py)
- [Validator orchestrator registry](../../../tools/validators/validator_registry.json)

### Authoring validation performed

| Check | Result | Evidence |
|---|---|---|
| Current-main inventory base pinned | **PASS** | Base `main@51d06e47d60e1071a5728267b5dac4255c4c338b`; prior index blob `8a2fa26d607f2da2c1f59c9ea9134d6dda3a222c`. |
| County tree traversal complete | **PASS** | Recursive repository tree `2a70a8b7a8b9b6a096c818898286be545a09144a`; `truncated: false`. |
| County universe and current README recount | **PASS** | 105 unique rows; 105 exact `README.md` files; 56 one-byte and 49 substantive README files; 57 anomalous rows after preserving all remaining naming, identity, foreign-plan, and duplicate-tree findings. |
| Current county directory links | **PASS** | All 105 directory targets exist in the pinned tree. |
| README/build-artifact links | **PASS** | Every table link resolves to a blob in the pinned tree; Decatur and Elk resolve through their current substantive `README.md` files, and Decatur exposes only its own direct build artifact. |
| Index structure | **PASS** | One H1 and one KFM metadata block; legacy index anchors remain intact. |
| Current county validator | **NOT_RUN** | Root, naming, table grammar, file layout, and registry mismatch are disclosed above. |
| Source, rights, evidence, policy, release, rollback, deployment | **NOT_RUN** | Outside this same-path documentation inventory change. |
| Hosted pull-request checks | **PENDING** | Reported only for the final exact draft-PR head after remote delivery. |

> [!NOTE]
> These checks establish the integrity of this inventory revision. They do not validate any county artifact or promote any KFM state.

### Maintenance triggers

Rebuild the evidence snapshot and table when any of the following changes:

- a county directory, README, or build artifact is added, renamed, moved, or deleted;
- ADR-0027 changes effective status;
- the Focus documentation placement decision changes;
- the county validator's root, table grammar, filenames, status model, or registry wiring changes;
- a county gains evidence-backed lifecycle, correction, rollback, or release state;
- a source, rights, sensitivity, or identity correction invalidates a planning signal.

### Rollback and correction

Before merge, close or abandon this draft PR; the current default-branch tree remains unchanged. After merge, revert only this index commit or apply a bounded forward correction against the actual merged bytes. The county README and plan changes already present at the pinned main base are not rollback targets for this PR. This change creates no new county lane, broader structural migration, schema, policy, release, deployment, or publication state.

### Change history

| Version | Date | Change |
|---|---|---|
| v0.3 | 2026-06-11 | Chat-lineage collision register with 95 register-complete, four generated-artifact, and six repository-collision rows. |
| v1.0 | 2026-08-20 | Replaced stale collision claims with a pinned, non-truncated current-tree inventory; exposed filename, README, duplicate-tree, placement, and validator drift; retained legacy planning signals without promoting them. |
| v1.1 | 2026-08-20 | Reconciled the Anderson County row and one-byte count after the same-path README modernization; preserved `PLAN_NAME_DRIFT` and all lifecycle, validator, release, and publication holds. |
| v1.2 | 2026-08-20 | Brought the Allen README over current main; recomputed 67 one-byte, 38 substantive, and 68 anomalous county rows; retained Anderson `PLAN_NAME_DRIFT`; synchronized the already-merged Barber row. |
| v1.3 | 2026-08-21 | Replaced Edwards `README,md` with substantive `README.md`; reconciled its row and resolved drift ledger item `COUNTY-INV-004`; carried the merged Doniphan README and all current-main README facts forward to 58 one-byte, 47 substantive, and 60 anomalous county rows; retained all naming, identity, foreign-plan, duplicate-tree, lifecycle, validator, release, and publication holds. |
| v1.4 | 2026-08-21 | Recomputed the complete 105-county inventory at current main; cleared the resolved Decatur foreign-plan and Elk one-byte README findings; recorded 56 one-byte, 49 substantive, and 57 anomalous county rows; preserved the singular/plural placement HOLD and every remaining naming, identity, validator, lifecycle, source, policy, release, deployment, and publication boundary. |

[↑ Back to top](#top)
