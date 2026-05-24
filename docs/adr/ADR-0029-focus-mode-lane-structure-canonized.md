<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/adr-0029-focus-mode-lane-structure-canonized   # NEEDS_VERIFICATION until registered
title: "ADR-0029 — Focus Mode lane structure canonized (singular lane, containers, snake_case area dirs, scope suffix)"
type: adr
adr_id: ADR-0029
version: v0.1
status: proposed
decision_date: 2026-05-24
owners:
  - <OWNER:focus-mode-steward>
  - <OWNER:directory-rules-steward>
  - <OWNER:docs-steward>
created: 2026-05-24
updated: 2026-05-24
policy_label: public
authority: amends docs/doctrine/directory-rules.md §6.7.2 (placement table for docs/ Focus Mode root), §6.7.3 (per-host-root casing convention), §13.5 (drift register clarification), §18.d (closes OPEN-FM-01 + OPEN-DR-08)
supersedes: none
superseded_by: none
related_adrs:
  - docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md           # CONFIRMED — schema home (anti-pattern #10 in directory-rules.md §13.5)
  - docs/adr/ADR-0027-county-focus-mode-control-plane.md                          # CONFIRMED — county control plane
  - docs/adr/ADR-0028-state-scale-focus-mode-scope.md                           # CONFIRMED — -state scope + 13-domain coverage rule; filename collides with kebab convention (separate question)
related:
  - docs/doctrine/directory-rules.md                                               # CONFIRMED — §6.7.2 current spec is incompatible with live tree; this ADR reconciles
  - docs/focus-mode/README.md                                                      # CONFIRMED — v0.3 in tree; v0.5 bump follows this ADR
  - docs/focus-mode/counties/COUNTY_INDEX.md                                       # CONFIRMED — 105-county roster
  - docs/focus-mode/counties/_template/                                            # CONFIRMED — template location (container pattern)
  - docs/focus-mode/state/                                                         # CONFIRMED — state container; gated on ADR-0028
  - docs/focus-mode/counties/domains.md                                            # CONFIRMED — proto-ORGANIZATION_RULES (v0.1 draft)
  - tools/validators/validate_focus_mode_index.py                                  # NEEDS_VERIFICATION — validator update required (§6.3)
  - KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.md                      # CONFIRMED via ADR-0028 — 13 thematic domains (Appendix C)
tags:
  - kfm
  - adr
  - focus-mode
  - lane-structure
  - directory-rules
  - placement-contract
  - container-pattern
  - snake-case
  - singular-vs-plural
  - drift-reconciliation
trigger_clause: |
  Drift Triage v2 (2026-05-24) classified 133 of 147 files in docs/focus-mode/ as
  "ADR-class" because the live tree uses container subdirectories (counties/, state/)
  while docs/doctrine/directory-rules.md §6.7.2 specifies flat <area>-<scope>/ siblings.
  Per directory-rules.md §2.4 (ADR triggers) and ai-build-operating-contract.md §28,
  reconciling that divergence requires an ADR.
closes_open_items:
  - OPEN-FM-01    # singular vs plural Focus Mode lane name (was open)
  - OPEN-DR-08    # per-host-root casing for Focus Mode area directories (was open)
does_not_close:
  - OPEN-FM-09    # state-scale scope: closed by ADR-0028, gated on its acceptance (independent)
  - OPEN-FM-XX    # ADR-0028 filename convention (separate question; see §10.3)
[/KFM_META_BLOCK_V2] -->

[![status: proposed](https://img.shields.io/badge/status-proposed-yellow)](#1-status)
[![type: ADR](https://img.shields.io/badge/type-ADR-blue)](#)
[![scope: Focus Mode lane](https://img.shields.io/badge/scope-Focus%20Mode%20lane-purple)](#3-decision)
[![authority: amends directory-rules.md](https://img.shields.io/badge/authority-amends%20directory--rules.md-orange)](docs/doctrine/directory-rules.md)
[![closes: OPEN-FM-01 + OPEN-DR-08](https://img.shields.io/badge/closes-OPEN--FM--01%20%2B%20OPEN--DR--08-green)](#36-decision-6--singular-docsfocus-mode-is-canonical-closes-open-fm-01)

<a id="top"></a>

# ADR-0029 — Focus Mode lane structure canonized

> [!IMPORTANT]
> **Four decisions in one ADR.** This ADR closes four interrelated questions about how Focus Mode lanes are structured under `docs/`. They are split into §3.1 through §3.6 below; reading any one in isolation will miss the point. The four decisions together describe the structure the live tree already implements; this ADR reconciles doctrine to that reality rather than the reverse, **for documented reasons** (see §5).

---

## Contents

- [1. Status](#1-status)
- [2. Context](#2-context)
- [3. Decision](#3-decision)
  - [3.1 Decision 1 — Canonical placement table for `docs/` Focus Mode root](#31-decision-1--canonical-placement-table-for-docs-focus-mode-root)
  - [3.2 Decision 2 — Container subdirectories are canonized, not flattened](#32-decision-2--container-subdirectories-are-canonized-not-flattened)
  - [3.3 Decision 3 — `snake_case` area directory names with `_<scope>` suffix](#33-decision-3--snake_case-area-directory-names-with-_scope-suffix)
  - [3.4 Decision 4 — Self-describing filename convention for per-area artifacts](#34-decision-4--self-describing-filename-convention-for-per-area-artifacts)
  - [3.5 The 13 canonical thematic domains (restated from ADR-0028)](#35-the-13-canonical-thematic-domains-restated-from-adr-0028)
  - [3.6 Decision 6 — Singular `docs/focus-mode/` is canonical (closes OPEN-FM-01)](#36-decision-6--singular-docsfocus-mode-is-canonical-closes-open-fm-01)
- [4. Consequences](#4-consequences)
- [5. Alternatives considered](#5-alternatives-considered)
- [6. Migration plan](#6-migration-plan)
- [7. Amendments to `docs/doctrine/directory-rules.md`](#7-amendments-to-docsdoctrinedirectory-rulesmd)
- [8. Acceptance criteria](#8-acceptance-criteria)
- [9. Rollback plan](#9-rollback-plan)
- [10. Open items not resolved by this ADR](#10-open-items-not-resolved-by-this-adr)
- [11. Related ADRs and references](#11-related-adrs-and-references)
- [12. ADR self-check](#12-adr-self-check)

---

## 1. Status

| Field | Value |
|---|---|
| ADR ID | ADR-0029 |
| Status | **proposed** |
| Decision date | 2026-05-24 |
| Deciders | `<OWNER:focus-mode-steward>`, `<OWNER:directory-rules-steward>`, `<OWNER:docs-steward>` |
| Supersedes | none |
| Superseded by | none |
| Amends | `docs/doctrine/directory-rules.md` §6.7.2, §6.7.3, §13.5, §18.d (amendment text in §7) |
| Closes | OPEN-FM-01 (singular vs plural Focus Mode lane name), OPEN-DR-08 (per-host-root casing for Focus Mode area directories) |
| Does not close | OPEN-FM-09 (state-scale scope, closed by ADR-0028 independently) |

[↑ Back to top](#top)

---

## 2. Context

### 2.1 The drift

A drift-triage audit of the live `docs/focus-mode/` tree (`/tmp/kfm-organize/organize_v2.py docs/focus-mode/`, 2026-05-24, full report at `/tmp/kfm-organize/triage.md`) found:

| Drift signature | Files affected | Status |
|---|---:|---|
| #1 Singular `docs/focus-mode/` vs plural `docs/focus-modes/` in spec | 147 (every file) | OPEN |
| #2 `counties/` container subdir vs flat `<area>-county/` siblings in spec | 133 | OPEN |
| #3 `state/` container subdir (gated on ADR-0028) | 2 | gated |
| #4 Domain folders at lane root (`agriculture/`, `archaeology/`, …) | 13 | mechanical (out of scope) |
| #5 snake_case `<x>_county` area dirs vs kebab-case in spec | 126 | OPEN |
| #6 Domain name mismatch vs canonical 13 (e.g., `hydrogeology`, split `roads`/`railroads`) | 6 | content review (out of scope) |

**CONFIRMED** via the categorizer's full-file enumeration at commit `5e11dbf` on branch `claude/magical-johnson-jP2GB`.

Signatures #1, #2, #3, #5 are the four structural questions this ADR resolves. Signatures #4 and #6 are addressed elsewhere (mechanical move to `docs/domains/<domain>/` per §8.3 of `docs/focus-mode/README.md`; per-domain content review against `KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.md` Appendix C).

### 2.2 What `directory-rules.md` v1.2 currently says

**CONFIRMED** by reading `docs/doctrine/directory-rules.md` §6.7.2 (commit `5e11dbf`):

> `docs/focus-modes/<area>-<scope>/` (e.g., `docs/focus-modes/ellsworth-county/`)

Three properties: **plural** lane name (`focus-modes`), **flat** sibling layout, **kebab-case** area-dir with `-<scope>` suffix.

### 2.3 What the live tree actually implements

**CONFIRMED** via `ls` and the categorizer (commit `5e11dbf`):

```
docs/focus-mode/                          # singular, NOT plural
├── README.md                             # v0.3
├── counties/                             # container subdir, NOT flat
│   ├── COUNTY_INDEX.md
│   ├── _template/
│   ├── domains.md                        # cross-domain composition reference
│   └── <area>_county/                    # snake_case + _county suffix, NOT kebab
│       ├── README.md
│       └── <area>_county_focus_mode_build_plan.md
├── state/                                # container subdir, NOT flat
│   ├── STATE_INDEX.md
│   └── _template/
└── <13 domain folders>/                  # treated separately (sig #4)
```

Three properties: **singular** lane name, **container** layout, **snake_case** area-dir with `_<scope>` suffix.

### 2.4 The reconciliation question

Three reasonable resolutions exist:

1. **Reconcile the live tree to the spec** — rename `focus-mode/` → `focus-modes/`, flatten `counties/<x>_county/` → `<x>-county/`, kebab-case everything. Cost: rename ~133 files; update ~225+ bare cross-refs.
2. **Reconcile the spec to the live tree** — amend §6.7.2 to canonize containers + singular + snake_case. Cost: amend doctrine; update validator; no file moves.
3. **Hybrid** — pick some properties from each (e.g., flatten but keep singular). Cost: rename subset; amend partial spec; risk inconsistency.

This ADR chooses Resolution 2 (canonize the live tree) with documented reasons in §5.

### 2.5 What is pre-decided, what is novel

The four decisions in this ADR are **not novel** in this session — they are the structure the live tree already implements and the structure `docs/focus-mode/counties/domains.md` (v0.1 draft, 2026-05-22) already cross-references in its meta block. This ADR's job is to make those decisions explicit, ratify them against `directory-rules.md`, and close OPEN-FM-01 and OPEN-DR-08 with citable rationale.

[↑ Back to top](#top)

---

## 3. Decision

### 3.1 Decision 1 — Canonical placement table for `docs/` Focus Mode root

**The canonical row in `docs/doctrine/directory-rules.md` §6.7.2 for the `docs/` Focus Mode root is:**

| Host root | Canonical path | Convention | Content shape |
|---|---|---|---|
| `docs/` | `docs/focus-mode/{counties,state,regions,corridors}/<area>_<scope>/` | singular lane name, kebab-case container, snake_case area dir + scope suffix | `README.md`, `<area>_<scope>_focus_mode_build_plan.md`, optional `*-notes.md`; plus container-level `COUNTY_INDEX.md` / `STATE_INDEX.md` and container-scoped `_template/`; plus 13 in-lane `<domain>/` folders holding focus-mode treatment of each canonical domain |

**Authority:** this row supersedes the §6.7.2 example previously specified as `docs/focus-modes/ellsworth-county/`.

### 3.2 Decision 2 — Container subdirectories are canonized, not flattened

Per-scope container directories `counties/`, `state/`, `regions/`, `corridors/` are **canonical** under `docs/focus-mode/`. Each container holds:

- A scope-level index (`COUNTY_INDEX.md`, `STATE_INDEX.md`, etc.) — **REQUIRED**
- A scope-scoped `_template/` with the canonical per-area files for that scope — **REQUIRED**
- Per-area lanes named `<area>_<scope>/` — zero or more
- Optionally, a `domains.md` cross-domain composition reference (county container has one, others MAY)

**Rationale (CONFIRMED file distribution at commit `5e11dbf`):**
- 133/147 (90%) of files in `docs/focus-mode/` already live under a container.
- At full population (105 counties + 1 state + N regions + N corridors), the lane root holds ~5 entries instead of ~110. Scannability of the lane root is a documented affordance per `docs/focus-mode/README.md` §6.
- Each container is itself a one-scope lane with its own index, template, and validator profile. The container is doing structural work, not just bucketing.
- Cost of reconciling in the other direction (flatten): 133 `git mv` operations, breaks every existing cross-ref to a county path, requires re-issuing `COUNTY_INDEX.md`. The flatten direction is the higher-cost migration despite being the option that matches §6.7.2 verbatim.

### 3.3 Decision 3 — `snake_case` area directory names with `_<scope>` suffix

Per-area directory names use **`snake_case` with an explicit `_<scope>` suffix**: `ellsworth_county/`, `kansas_state/`, `flint_hills_region/`, `kaw_river_corridor/`.

This is a **deliberate exception** to the general kebab-case sibling-lane convention in `docs/` (which applies to `docs/adr/`, `docs/runbooks/`, etc.).

**Rationale:**
- The per-area lane's primary file is `<area>_<scope>_focus_mode_build_plan.md` (see Decision 4 below). Matching the directory name to the filename's word-separator convention removes a class of authoring errors and string-template mismatches.
- The `_<scope>` suffix in the directory name disambiguates same-named areas at different scales (e.g., `cherokee_county/` vs. a hypothetical `cherokee_region/` for the Cherokee Outlet) without requiring readers to consult the container.
- The 64 county directories already in the live tree (CONFIRMED at commit `5e11dbf`) all use this convention. Migrating to kebab-case would be a 64-rename operation with no semantic gain.

### 3.4 Decision 4 — Self-describing filename convention for per-area artifacts

The per-area build-plan file is named **`<area>_<scope>_focus_mode_build_plan.md`** — fully self-describing: it identifies the area, the scope, and that it is a Focus Mode build plan, all from the filename alone.

The seven-file split from earlier README v0.3/v0.4 drafts (`build-plan.md`, `layer-registry.md`, `evidence-model.md`, `acceptance-checklist.md`, `source-seed-list.md`, `public-safety-notes.md`, plus `README.md`) is **superseded by a single-file consolidated template** per the `/kfm-finish-pack-v2` deliverable contract (which lands the consolidated template at `docs/focus-mode/counties/_template/county_focus_mode_build_plan.md` and `docs/focus-mode/state/_template/state_focus_mode_build_plan.md`).

The per-area lane is therefore **flat with two files**:

```
docs/focus-mode/counties/<area>_county/
├── README.md                                          # lane-level overview + status
└── <area>_county_focus_mode_build_plan.md             # the consolidated build plan
```

Plus optional `*-notes.md` framing files per README §13.2.

**Rationale:**
- A file whose name encodes area + scope + role cannot be silently moved to the wrong directory without the rename being immediately legible.
- The seven-file split was a contract from an earlier draft of the README that has not yet been validated against any populated lane. The 64 live county lanes all use the single-file pattern (CONFIRMED at commit `5e11dbf`).
- Consolidating to one file simplifies the validator: cross-section consistency checks become intra-document checks.

### 3.5 The 13 canonical thematic domains (restated from ADR-0028)

This ADR does **NOT** establish the 13-domain coverage rule. That rule was established by **ADR-0028 §3** and is restated here as a reading aid only, because every per-area build plan's `domain_coverage` block enumerates exactly these 13 keys.

The 13 thematic domains, per `KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.md` Appendix C (restated in `docs/focus-mode/README.md` v0.3 §14.1):

| # | Domain | Short-name |
|---|---|---|
| 1 | Hydrology | `hydrology` |
| 2 | Soil | `soil` |
| 3 | Atmosphere / Air | `atmosphere_air` |
| 4 | Geology | `geology` |
| 5 | Fauna | `fauna` |
| 6 | Flora | `flora` |
| 7 | Habitat | `habitat` |
| 8 | Agriculture | `agriculture` |
| 9 | Hazards | `hazards` |
| 10 | Roads / Rail / Trade | `roads_rail` |
| 11 | Settlements / Infrastructure | `settlements_infrastructure` |
| 12 | Archaeology / Cultural Heritage | `archaeology` |
| 13 | People / DNA / Land / Genealogy | `people_dna_land` |

Three cross-cutting spines (Spatial Foundation, Frontier Matrix, Planetary/3D) are **NOT enumerated** here because they apply to every Focus Mode by construction — they are spine, not domain. See README §14.1 "NOTE" for the spine treatment.

### 3.6 Decision 6 — Singular `docs/focus-mode/` is canonical (closes OPEN-FM-01)

The Focus Mode lane root is `docs/focus-mode/` — **singular**.

**Rationale:**
- The live tree uses singular (CONFIRMED at commit `5e11dbf`).
- The 225+ bare `directory-rules.md`-style references throughout the corpus use singular path fragments contextually; renaming to plural breaks every relative-path link in artifacts under `artifacts/`, `control_plane/`, and `docs/registers/`.
- The plural form `docs/focus-modes/` survives in older draft documents (README v0.3 title, some ADR-0028 cross-refs); those become legacy spellings to be reconciled when their owning documents are next versioned.

This decision **closes OPEN-FM-01**.

> [!NOTE]
> The README v0.3 title and several v0.3 §-references still read `docs/focus-modes/` (plural). README v0.5 (the bump that follows this ADR) updates those to singular and adds a §0 reference to this ADR.

[↑ Back to top](#top)

---

## 4. Consequences

### 4.1 What changes

- `docs/doctrine/directory-rules.md` gains four amendments (§7 below).
- `docs/focus-mode/README.md` bumps v0.3 → v0.5: title, §6, §9, §10, §13 paragraphs reconciled to singular + container + snake_case + scope-suffix + consolidated single-file template.
- `docs/focus-mode/counties/_template/` and `docs/focus-mode/state/_template/` are populated with the consolidated `<scope>_focus_mode_build_plan.md` template (per `/kfm-finish-pack-v2`).
- Validator (`tools/validators/validate_focus_mode_index.py`) recognizes the singular lane name, the container layout, snake_case area dirs, the consolidated filename, and the cross-reference to all 13 canonical domain folders (§6.3 below).

### 4.2 What does NOT change

- ADR-0028 (state-scale scope) is independent and remains in force; its acceptance gate is unchanged.
- The 13-domain coverage rule (ADR-0028 §3) is unchanged.
- `docs/domains/<domain>/` placement (§8.3 of `docs/focus-mode/README.md`) is unchanged — Focus Mode in-lane domain folders are *framework treatment of each domain*, not domain doctrine; the §8.3 anti-pattern ("Focus Mode is NOT a domain") is preserved (see §7.3).
- `schemas/contracts/v1/focus_mode/` remains the schema home (ADR-0001).
- Sensitivity defaults (README §15) are unchanged.

### 4.3 Self-describing-filename principle

Decisions 3 and 4 together establish a principle that may be cited by future ADRs:

> **In a per-area lane whose primary artifact is a single consolidated file, the filename SHOULD encode the area, the scope, and the role unambiguously, and the directory name SHOULD use the same word-separator convention as the filename.**

This is a deliberate exception to the general kebab-case sibling-lane convention in `docs/`, justified when filename-level self-description prevents a class of misplacement errors.

### 4.4 Pack artifacts to rewrite

Per Decision 4 (consolidated single-file template), the following artifacts are **superseded** and will be rewritten or removed:

| Artifact | Status after this ADR |
|---|---|
| `docs/focus-mode/counties/_template/county-build-plan.md` (kebab, fragmentary) | superseded by `county_focus_mode_build_plan.md` (snake, consolidated) |
| `docs/focus-mode/state/_template/state-build-plan.md` (kebab, fragmentary) | superseded by `state_focus_mode_build_plan.md` (snake, consolidated) |
| The implied seven-file split from README v0.3 §13.1 | superseded; collapses to two files: `README.md` + consolidated build plan |
| `MIGRATION_NOTE.md` (if present at lane root) | belongs under `migrations/<migration-id>/` per `directory-rules.md` §2.5 |

[↑ Back to top](#top)

---

## 5. Alternatives considered

### 5.1 Alternative A — Reconcile the live tree to §6.7.2 verbatim (flatten + plural + kebab)

Renames 133 county/state files, plus the lane-root rename, plus a re-issue of every cross-ref in `artifacts/`, `control_plane/`, and `docs/registers/`.

**Rejected** because:
- Migration cost dominates. The categorizer counts 133 file moves before counting cross-ref updates. The exhaustive search at commit `5e11dbf` found 225 bare `directory-rules.md`-style references in the corpus; an analogous count for `focus-mode` references would be in the same range. Each rename cascades.
- The §6.7.2 example (`docs/focus-modes/ellsworth-county/`) was authored as a placeholder when no county lane existed. It encoded an aspirational shape, not an evaluated design choice. Treating it as authoritative against 64 live county lanes inverts the evidence basis.
- Sibling-lane consistency with `docs/adr/` and `docs/runbooks/` (the only argument in favor of Alternative A) is real but local. The Focus Mode lane is structurally different from those lanes — it has nested scopes, per-area populations in the hundreds, and a control-plane index — and consistency with siblings that have none of those properties is weak.

### 5.2 Alternative B — Hybrid (canonize containers; keep kebab + plural)

Keeps containers (Decision 2) but adopts plural lane name and kebab area dirs.

**Rejected** because:
- Splits the four decisions into "two from live, two from spec." Each split decision incurs its own migration cost (rename lane root; rename 64 county dirs; update all bare cross-refs) for no semantic gain.
- The four decisions are mutually reinforcing. The self-describing-filename principle (§4.3) is strongest when the directory name uses the same word-separator as the filename. Hybrid breaks that.

### 5.3 Alternative C — Defer the structural decision; do mechanical fixes only

Resolve sigs #4 and #6 now (the mechanical/content-review fixes); leave sigs #1, #2, #3, #5 in drift register for a future round.

**Rejected** because:
- The drift register already includes OPEN-FM-01 and OPEN-DR-08. Deferring further requires either re-opening them or creating new drift items. Both are bookkeeping cost for no progress.
- The pack-v2 templates (`/kfm-finish-pack-v2`) cannot be authored without a settled lane structure. Deferring blocks downstream work.

### 5.4 Alternative D — Amend §6.7.2 to allow EITHER shape (flat or container) at author's discretion

Document both as canonical; let the populator choose.

**Rejected** because:
- Optional structure is no structure. Authors of the next county lane would have no basis to choose.
- The categorizer cannot meaningfully validate "either shape is OK" without losing its ability to flag drift.

[↑ Back to top](#top)

---

## 6. Migration plan

### 6.1 Pack-v2 artifacts to author after this ADR is accepted

| Artifact | Path | Authoring command |
|---|---|---|
| Bumped README | `docs/focus-mode/README.md` v0.5 | manual edit (~20-line bookkeeping diff on existing v0.3) |
| Organization rules | `docs/focus-mode/ORGANIZATION_RULES.md` v0.2 | extract from `docs/focus-mode/counties/domains.md` v0.1 + the categorizer rules at `/tmp/kfm-organize/organize_v2.py` |
| County template | `docs/focus-mode/counties/_template/county_focus_mode_build_plan.md` | `/kfm-finish-pack-v2 county` |
| State template | `docs/focus-mode/state/_template/state_focus_mode_build_plan.md` | `/kfm-finish-pack-v2 state` (gated on ADR-0028 acceptance for instantiation) |
| Amendment supplement | `docs/adr/ADR-0029-supplement-directory-rules-amendments.md` | `/kfm-finish-pack-v2 amendment` |

### 6.2 Live-tree fixes still required (out of scope for this ADR)

- Sig #4 (13 domain folders at lane root) → mechanical move to `docs/domains/<domain>/` per `docs/focus-mode/README.md` §8.3.
- Sig #6 (domain name mismatch) → content review against Atlas Appendix C (`hydrogeology` → `hydrology`, split `roads`/`railroads` → unified `roads_rail`, `atmosphere` → `atmosphere_air`, `people` → `people_dna_land`, `settlements-infrastructure` → `settlements_infrastructure`).
- The 64 county lanes' `README.md` files are currently 1-byte empty placeholders (CONFIRMED at commit `5e11dbf`). Populating them is per-county content work, not structural.

### 6.3 Validator updates required

`tools/validators/validate_focus_mode_index.py` (path **NEEDS_VERIFICATION**; categorizer at `/tmp/kfm-organize/organize_v2.py` is the working v2) must be updated to:

1. Accept `docs/focus-mode/` (singular) as the canonical lane root. **REQUIRED.**
2. Recognize `counties/`, `state/`, `regions/`, `corridors/` as canonical container subdirectories. **REQUIRED.**
3. Recognize `snake_case` area directory names with explicit `_<scope>` suffix as canonical. **REQUIRED.**
4. Recognize `<area>_<scope>_focus_mode_build_plan.md` as the canonical per-area build-plan filename. **REQUIRED.**
5. Resolve cross-references to all 13 canonical domain folders under `docs/focus-mode/<domain>/` and verify the `domain_coverage` map in each per-area build plan enumerates exactly the 13 canonical keys. **REQUIRED.**
6. Flag legacy plural (`docs/focus-modes/`), legacy kebab (`<area>-county/`), legacy seven-file split, and legacy fragmentary template (`county-build-plan.md`) as drift with a citation to this ADR. **REQUIRED for migration window; MAY be relaxed after 2 minor versions.**

The categorizer at `/tmp/kfm-organize/organize_v2.py` already implements rules 1–4 in spirit; rule 5 requires a cross-reference resolver; rule 6 requires a legacy-drift mode.

[↑ Back to top](#top)

---

## 7. Amendments to `docs/doctrine/directory-rules.md`

This ADR amends four sections of `docs/doctrine/directory-rules.md`. The amendment text below is the **authoritative** version; the rendered before/after patches will be produced by `/kfm-finish-pack-v2 amendment` as a paste-ready supplement file (`docs/adr/ADR-0029-supplement-directory-rules-amendments.md`).

### 7.1 Amendment 1 — §6.7.2 placement table, `docs/` row

**Before** (CONFIRMED in v1.2 at commit `5e11dbf`): the §6.7.2 example `docs/focus-modes/<area>-<scope>/` with `docs/focus-modes/ellsworth-county/`.

**After:**

```
| docs/ | docs/focus-mode/{counties,state,regions,corridors}/<area>_<scope>/ | singular lane, kebab-case container, snake_case area dir + scope suffix | README.md, <area>_<scope>_focus_mode_build_plan.md, optional *-notes.md; plus container-level COUNTY_INDEX.md / STATE_INDEX.md and container-scoped _template/; plus 13 in-lane <domain>/ folders holding focus-mode treatment of each canonical domain |
```

### 7.2 Amendment 2 — §6.7.3 casing convention

**Add** a new bullet to the per-host-root casing list:

> - **Singular + snake_case + scope suffix in `docs/focus-mode/`:** `docs/focus-mode/counties/ellsworth_county/`, `docs/focus-mode/state/kansas_state/`. **Deliberate exception** to the general kebab-case sibling-lane convention in `docs/`. Rationale per ADR-0029 §3.3 and §4.3 (self-describing-filename principle).

### 7.3 Amendment 3 — §13.5 drift register clarification

**Add** a clarifying note (does not remove existing anti-patterns):

> **Clarification per ADR-0029.** Per-domain folders inside `docs/focus-mode/<domain>/` are *focus-mode framework treatment of each domain*, NOT domain doctrine. Domain doctrine remains at `docs/domains/<domain>/` per §12 Domain Placement Law. The in-lane `<domain>/README.md` files cross-reference `docs/domains/<domain>/` but do not duplicate it. The §8.3 "Focus Mode is NOT a domain" anti-pattern is preserved: the in-lane folders are not domains, they are framework treatments.

### 7.4 Amendment 4 — §18.d closures

| ID | Status before | Status after | Citation |
|---|---|---|---|
| OPEN-FM-01 (singular vs plural lane name) | open | **CLOSED — singular canonical** | ADR-0029 §3.6 |
| OPEN-DR-08 (per-root casing for Focus Mode area dirs) | open | **CLOSED — snake_case for Focus Mode area dirs** | ADR-0029 §3.3 |
| OPEN-FM-09 (-state scope) | open | unchanged — closed by ADR-0028 §3 (independent) | — |
| OPEN-FM-10 (13-domain coverage) | open | unchanged — closed by ADR-0028 §3 | — |

[↑ Back to top](#top)

---

## 8. Acceptance criteria

This ADR is accepted when:

1. `<OWNER:directory-rules-steward>` signs off on the §7 amendments. **REQUIRED.**
2. `<OWNER:focus-mode-steward>` signs off on §3.1–§3.4 and §3.6. **REQUIRED.**
3. `<OWNER:docs-steward>` signs off on the singular `docs/focus-mode/` choice and the implications for cross-references. **REQUIRED.**
4. The amendment supplement file (`docs/adr/ADR-0029-supplement-directory-rules-amendments.md`) is produced and reviewed against §7 of this ADR. **REQUIRED.**
5. README v0.5 is authored (per §6.1). **REQUIRED.**
6. `ORGANIZATION_RULES.md` v0.2 is authored (per §6.1). **REQUIRED.**
7. The categorizer (`/tmp/kfm-organize/organize_v2.py` or its successor) is updated to validate per §6.3 rules 1–4 at minimum. **REQUIRED.**
8. No `tools/validators/validate_focus_mode_index.py` regression on the live tree. **REQUIRED if that validator exists** (NEEDS_VERIFICATION at this commit).

[↑ Back to top](#top)

---

## 9. Rollback plan

If this ADR is rejected after acceptance:

1. Revert the amendment commit on `docs/doctrine/directory-rules.md`.
2. Set this ADR's status to `superseded` with a `superseded_by` link.
3. Re-open OPEN-FM-01 and OPEN-DR-08 in §18.d.
4. Revert README v0.5 → v0.3 (or the version current at rollback time).
5. The pack-v2 templates (the two `_focus_mode_build_plan.md` files) and the amendment supplement file may be deleted or marked superseded.

The 64 county lanes' directory names and the singular lane name are **not** reverted — they are the live-tree state and reverting them would require its own ADR.

[↑ Back to top](#top)

---

## 10. Open items not resolved by this ADR

### 10.1 State-scale scope (OPEN-FM-09)

Closed independently by ADR-0028. Not affected by this ADR. State-template population remains gated on ADR-0028 acceptance.

### 10.2 Domain-name reconciliation (sig #6 from drift triage)

Six in-lane domain folders use non-canonical names (`hydrogeology`, `roads`, `railroads`, `atmosphere`, `people`, `settlements-infrastructure`). Reconciliation requires per-domain content review against Atlas Appendix C. Tracked as a follow-up; not blocked by this ADR.

### 10.3 ADR-0028 filename convention

ADR-0028's filename (`ADR-0028-state-scale-focus-mode-scope.md`) uses spaces and an em-dash, diverging from the kebab-case `ADR-NNNN-<slug>.md` convention used by ADR-0001 through ADR-0027 and adopted by this ADR. Rename is a separate question; cross-refs in this file quote the actual filename.

### 10.4 Architecture stub at `docs/architecture/directory-rules.md`

A 16-line scaffold exists at `docs/architecture/directory-rules.md` pointing to source documents. It is independent of this ADR and the canonical-home decision; whether to delete, redirect, or leave it is a separate question.

[↑ Back to top](#top)

---

## 11. Related ADRs and references

- **ADR-0001** — schema home (`schemas/contracts/v1/`); referenced for the drift anti-pattern #10 in §13.5.
- **ADR-0027** — county Focus Mode control plane; this ADR ratifies the structural choices that ADR-0027 implicitly assumed.
- **ADR-0028** — state-scale Focus Mode scope + 13-domain coverage rule; independent; this ADR cites it for the 13-domain list (§3.5) and notes the closure of OPEN-FM-09 + OPEN-FM-10 (§7.4).
- `docs/doctrine/directory-rules.md` v1.2 — amended by this ADR (§7).
- `docs/focus-mode/README.md` v0.3 — to be bumped to v0.5 per §6.1.
- `docs/focus-mode/counties/domains.md` v0.1 — proto-`ORGANIZATION_RULES.md`; cited as the existing cross-domain composition reference.
- `KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.md` — Appendix C; canonical 13 domains.
- `ai-build-operating-contract.md` §28 — ADR trigger rule that motivated this ADR.
- `/tmp/kfm-organize/organize_v2.py` — working categorizer that produced the drift evidence cited in §2.1; CONFIRMED at commit `5e11dbf`.

[↑ Back to top](#top)

---

## 12. ADR self-check

- [x] **Single decision per ADR?** Four interrelated structural decisions; documented in §3 as a coherent set (Decisions 1–4 + 6) with the rationale that splitting them would create false choices (§5.2).
- [x] **Cite-or-abstain on all factual claims?** Yes; live-tree claims cite commit `5e11dbf` and the categorizer output; doctrine claims cite specific section numbers of `docs/doctrine/directory-rules.md` v1.2 and `docs/focus-mode/README.md` v0.3.
- [x] **Truth labels on uncertain claims?** Yes; `NEEDS_VERIFICATION` on the validator path (`tools/validators/validate_focus_mode_index.py`) which has not been confirmed in this commit.
- [x] **No fabricated owner names?** Yes; placeholders `<OWNER:focus-mode-steward>` etc.
- [x] **Rollback path?** Yes (§9).
- [x] **Reverses cleanly?** Mostly. Amendments and version bumps are git-reversible. The 64 county directory names and the lane-root name are live-tree state — reverting them is its own ADR.
- [x] **Closes specific OPEN items in `directory-rules.md` §18.d?** Yes (§7.4): OPEN-FM-01, OPEN-DR-08.
- [x] **Pre-amendment text quoted?** Partially — §6.7.2 example quoted in §2.2; full before/after rendering deferred to the amendment supplement file (§6.1).

[↑ Back to top](#top)

---

**Last updated:** 2026-05-24 · v0.1 · Authority: amends `docs/doctrine/directory-rules.md` §6.7.2, §6.7.3, §13.5, §18.d
