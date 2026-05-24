<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/focus-mode-organization-rules   # NEEDS_VERIFICATION until registered
title: "Focus Mode — Organization Rules (categorization spec for docs/focus-mode/)"
type: standard
version: v0.2
status: draft
owners:
  - <OWNER:focus-mode-steward>
  - <OWNER:directory-rules-steward>
created: 2026-05-24
updated: 2026-05-24
policy_label: public
authority: derives from docs/doctrine/directory-rules.md §6.7 (as amended by ADR-0029 §7) and docs/focus-mode/README.md v0.5; supersedes the ad-hoc rules in tools/focus_mode_organize.py v1
related:
  - docs/doctrine/directory-rules.md
  - docs/focus-mode/README.md
  - docs/focus-mode/counties/domains.md                                # cross-domain composition reference (separate doc)
  - docs/adr/ADR-0029-focus-mode-lane-structure-canonized.md
  - docs/adr/ADR-0028 — State-scale Focus Mode scope.md                # 13-domain coverage rule
  - tools/validators/validate_focus_mode_index.py                      # NEEDS_VERIFICATION — implementer of these rules
  - /tmp/kfm-organize/organize_v2.py                                   # working v2 categorizer; reference implementation at commit 334b8d6
tags:
  - kfm
  - focus-mode
  - organization-rules
  - categorization
  - drift-register
  - validator-spec
  - canonical-vs-drift
notes:
  - v0.2 is the first version after ADR-0029 acceptance proposes singular lane + container layout + snake_case area dirs + consolidated single-file template. v0.1 existed only as the in-code rules of the v1 categorizer.
  - This document specifies WHAT belongs where; docs/focus-mode/README.md v0.5 specifies WHY. Read them together.
  - Every rule in §3 has a disposition column matching the categorizer output (keep-root | keep-area | keep-template | optional-keep | drift-out-of-lane | drift-within-lane | unknown). The dispositions are normative; the categorizer's column names match by design.
[/KFM_META_BLOCK_V2] -->

[![status: draft v0.2](https://img.shields.io/badge/status-draft%20v0.2-yellow)](#1-purpose)
[![authority: derives from ADR-0029](https://img.shields.io/badge/authority-derives%20from%20ADR--0029-blue)](docs/adr/ADR-0029-focus-mode-lane-structure-canonized.md)
[![implements: directory-rules.md §6.7](https://img.shields.io/badge/implements-directory--rules.md%20%C2%A76.7-blue)](docs/doctrine/directory-rules.md)
[![scope: docs/focus-mode/ only](https://img.shields.io/badge/scope-docs%2Ffocus--mode%2F%20only-purple)](#1-purpose)

<a id="top"></a>

# Focus Mode — Organization Rules

> [!IMPORTANT]
> This document is the **categorization spec** for `docs/focus-mode/`. For every file path under that root, exactly one rule in §3 applies and assigns the file a **disposition** (one of seven categories). The categorizer at `/tmp/kfm-organize/organize_v2.py` (and its eventual production successor at `tools/validators/validate_focus_mode_index.py`) implements these rules. If categorizer behavior diverges from this document, **this document wins**; file a follow-up PR against the categorizer.

---

## Contents

- [1. Purpose](#1-purpose)
- [2. Vocabulary](#2-vocabulary)
- [3. Categorization rules](#3-categorization-rules)
  - [3.1 Lane-root files (`docs/focus-mode/<file>`)](#31-lane-root-files-docsfocus-modefile)
  - [3.2 Container-level files (`docs/focus-mode/<container>/<file>`)](#32-container-level-files-docsfocus-modecontainerfile)
  - [3.3 Template files (`docs/focus-mode/<container>/_template/<file>`)](#33-template-files-docsfocus-modecontainer_templatefile)
  - [3.4 Per-area lane files (`docs/focus-mode/<container>/<area>_<scope>/<file>`)](#34-per-area-lane-files-docsfocus-modecontainerarea_scopefile)
  - [3.5 In-lane domain folders (`docs/focus-mode/<domain>/<file>`)](#35-in-lane-domain-folders-docsfocus-modedomainfile)
  - [3.6 Anything else under `docs/focus-mode/`](#36-anything-else-under-docsfocus-mode)
- [4. Drift signature reference](#4-drift-signature-reference)
- [5. Disposition policy — what each category triggers](#5-disposition-policy--what-each-category-triggers)
- [6. Exemptions and edge cases](#6-exemptions-and-edge-cases)
- [7. Cross-references and out-of-scope rules](#7-cross-references-and-out-of-scope-rules)
- [8. Categorizer contract](#8-categorizer-contract)
- [9. Self-check](#9-self-check)

---

## 1. Purpose

This document specifies, for every file path under `docs/focus-mode/`, **which category it belongs to** and **what disposition that category triggers**. It serves three audiences:

1. **Authors** — before creating or moving a file under `docs/focus-mode/`, look up the path pattern in §3 to see whether it is canonical, optional, drift-within-lane, drift-out-of-lane, or unknown.
2. **Reviewers** — when reviewing a PR that touches `docs/focus-mode/`, check the categorizer output (`/tmp/kfm-organize/organize_v2.py docs/focus-mode/` or its successor) against the dispositions in §5.
3. **Validators / CI** — the categorizer is the executable form of this spec. CI runs it; drift findings block merge per the disposition policy in §5.

This document is **scoped strictly to `docs/focus-mode/`**. Cross-root placement (`schemas/`, `policy/`, `data/`, `tools/`, etc.) is governed by `docs/doctrine/directory-rules.md`; this document cites that doctrine but does not restate it.

[↑ Back to top](#top)

---

## 2. Vocabulary

| Term | Definition |
|---|---|
| **Lane** | The Focus Mode lane root: `docs/focus-mode/`. CONFIRMED singular per ADR-0029 §3.6. |
| **Container** | A scope-level subdirectory of the lane: `counties/`, `state/`, `regions/`, `corridors/`. Canonical per ADR-0029 §3.2. |
| **Per-area lane** | A directory under a container holding the artifacts for one area at one scope: `docs/focus-mode/counties/ellsworth_county/`, `docs/focus-mode/state/kansas_state/`. Names use `snake_case` with `_<scope>` suffix per ADR-0029 §3.3. |
| **In-lane domain folder** | A subdirectory of the lane root named after one of the 13 canonical domains: `docs/focus-mode/hydrology/`, `docs/focus-mode/soil/`, etc. Holds *focus-mode framework treatment of each domain*, NOT domain doctrine (see §3.5 and ADR-0029 §7.3). |
| **Template** | A file under `<container>/_template/` providing the canonical shape for per-area-lane artifacts. The consolidated single-file template `<scope>_focus_mode_build_plan.md` is canonical per ADR-0029 §3.4. |
| **Canonical** | Required to exist OR allowed to exist in this exact path/name. Disposition: `keep-*`. |
| **Optional** | Allowed to exist but not required. Disposition: `optional-keep`. |
| **Drift-within-lane** | Wrong subdirectory but the content type belongs in `docs/focus-mode/` somewhere. Disposition: `drift-within-lane`. |
| **Drift-out-of-lane** | The content type belongs in a different root entirely (e.g., schema, policy, data). Disposition: `drift-out-of-lane`. |
| **Unknown** | No rule in §3 matches. Disposition: `unknown` — halts for human review. |

[↑ Back to top](#top)

---

## 3. Categorization rules

For each path under `docs/focus-mode/`, apply the first matching rule from §3.1 through §3.6 in order.

> [!NOTE]
> All hidden files and directories (names starting with `.`) are skipped from categorization. CI tooling, editor configuration, and similar live under `docs/focus-mode/.<name>` paths and are not subject to this spec.

### 3.1 Lane-root files (`docs/focus-mode/<file>`)

A file with exactly one path component below `docs/focus-mode/`.

| Filename | Disposition | Required? | Authority |
|---|---|---|---|
| `README.md` | `keep-root` | **REQUIRED** | docs/focus-mode/README.md v0.5 §1 |
| `ORGANIZATION_RULES.md` | `keep-root` | **REQUIRED** (this file) | ADR-0029 §6.1 |
| Any other `.md` | `unknown` | — | halt for human review |
| `MIGRATION_NOTE.md` | `drift-out-of-lane` | — | belongs under `migrations/<migration-id>/` per directory-rules.md §2.5 |
| `CHANGELOG.md` | `drift-out-of-lane` | — | belongs under `migrations/<migration-id>/` or at repo root |
| Any non-`.md` file | `unknown` | — | halt for human review |

> [!IMPORTANT]
> The v1 categorizer accepted `COUNTY_INDEX.md` and `STATE_INDEX.md` at the lane root. **This is no longer canonical.** Per ADR-0029 §3.2, those indexes are **container-scoped**: `docs/focus-mode/counties/COUNTY_INDEX.md` and `docs/focus-mode/state/STATE_INDEX.md`. The legacy lane-root locations are `drift-within-lane`.

### 3.2 Container-level files (`docs/focus-mode/<container>/<file>`)

A file directly under one of the four canonical containers `counties/`, `state/`, `regions/`, `corridors/`.

| Container | Filename | Disposition | Required? | Authority |
|---|---|---|---|---|
| `counties/` | `README.md` | `keep-area` | **REQUIRED** | ADR-0029 §3.2 |
| `counties/` | `COUNTY_INDEX.md` | `keep-area` | **REQUIRED** | ADR-0029 §3.2 |
| `counties/` | `domains.md` | `optional-keep` | optional | cross-domain composition reference (this file is documented; if present it is canonical at this path) |
| `state/` | `README.md` | `keep-area` | **REQUIRED** | ADR-0029 §3.2 |
| `state/` | `STATE_INDEX.md` | `keep-area` | **REQUIRED** | ADR-0029 §3.2 (gated on ADR-0028 acceptance) |
| `regions/` | `README.md` | `keep-area` | **REQUIRED if container exists** | ADR-0029 §3.2 |
| `regions/` | `REGION_INDEX.md` | `keep-area` | **REQUIRED if container exists** | ADR-0029 §3.2 |
| `corridors/` | `README.md` | `keep-area` | **REQUIRED if container exists** | ADR-0029 §3.2 |
| `corridors/` | `CORRIDOR_INDEX.md` | `keep-area` | **REQUIRED if container exists** | ADR-0029 §3.2 |
| Any container | `.*-notes.md` | `optional-keep` | optional | framing notes (cross-container scope) |
| Any container | other `.md` | `unknown` | — | halt for human review |

> [!NOTE]
> Containers `regions/` and `corridors/` are canonical placeholders per ADR-0029 §3.2 even if not yet populated. If a container directory does not exist, no enforcement applies — only when the container exists do its `README.md` and `<SCOPE>_INDEX.md` become required.

### 3.3 Template files (`docs/focus-mode/<container>/_template/<file>`)

A file directly under a container's `_template/` subdirectory.

| Container | Canonical template filename | Disposition | Authority |
|---|---|---|---|
| `counties/_template/` | `county_focus_mode_build_plan.md` | `keep-template` | ADR-0029 §3.4 |
| `state/_template/` | `state_focus_mode_build_plan.md` | `keep-template` | ADR-0029 §3.4 (gated on ADR-0028) |
| `regions/_template/` | `region_focus_mode_build_plan.md` | `keep-template` | ADR-0029 §3.4 (PROPOSED) |
| `corridors/_template/` | `corridor_focus_mode_build_plan.md` | `keep-template` | ADR-0029 §3.4 (PROPOSED) |
| Any `_template/` | `README.md` | `optional-keep` | optional template-overview file |
| Any `_template/` | other `.md` | `unknown` | halt for human review |
| Any `_template/<subdir>/*` | `unknown` | — | templates are flat (no nested subdirs) |

> [!IMPORTANT]
> The legacy kebab-case templates `county-build-plan.md` and `state-build-plan.md` are **`drift-within-lane`** — same container, wrong filename. Authors should rename in-place to the snake_case consolidated form per ADR-0029 §3.4.

### 3.4 Per-area lane files (`docs/focus-mode/<container>/<area>_<scope>/<file>`)

A file under a per-area lane directory. The directory name MUST match `^[a-z][a-z0-9_]*_(county|state|region|corridor)$` per ADR-0029 §3.3.

| Filename pattern | Disposition | Required? | Authority |
|---|---|---|---|
| `README.md` | `keep-area` | **REQUIRED** | ADR-0029 §3.4 |
| `<area>_<scope>_focus_mode_build_plan.md` (exact match to dir name) | `keep-area` | **REQUIRED** | ADR-0029 §3.4 |
| `*-notes.md` | `optional-keep` | optional | framing notes (per-area scope) |
| `build-plan.md`, `layer-registry.md`, `evidence-model.md`, `acceptance-checklist.md`, `source-seed-list.md`, `public-safety-notes.md` | `drift-within-lane` | — | legacy seven-file split per pre-ADR-0029 README v0.4; should be consolidated into the single-file build plan per ADR-0029 §3.4 |
| Any other `.md` | `unknown` | — | halt for human review |
| Files in subdirectories of the per-area lane | `unknown` | — | per-area lanes are flat per ADR-0029 §3.4 |

> [!CAUTION]
> The per-area build plan's filename MUST match its parent directory name. If the directory is `ellsworth_county/`, the build plan is `ellsworth_county_focus_mode_build_plan.md` — not `ellsworth-county_focus_mode_build_plan.md`, not `ellsworth_focus_mode_build_plan.md`, not `focus_mode_build_plan.md`. The self-describing-filename principle (ADR-0029 §4.3) requires this exact match.

### 3.5 In-lane domain folders (`docs/focus-mode/<domain>/<file>`)

A file under one of the 13 canonical thematic domain subdirectories of the lane root: `hydrology/`, `soil/`, `atmosphere_air/`, `geology/`, `fauna/`, `flora/`, `habitat/`, `agriculture/`, `hazards/`, `roads_rail/`, `settlements_infrastructure/`, `archaeology/`, `people_dna_land/`.

| Filename | Disposition | Required? | Authority |
|---|---|---|---|
| `README.md` | `keep-area` | **REQUIRED if folder exists** | docs/focus-mode/README.md v0.5 §14 (domain coverage matrix); ADR-0028 §3 (13-domain rule) |
| `*-notes.md` | `optional-keep` | optional | framing notes (domain scope) |
| Any other `.md` | `unknown` | — | halt for human review |
| Files in subdirectories | `unknown` | — | in-lane domain folders are flat |

> [!IMPORTANT]
> **In-lane domain folders are NOT domain doctrine.** They are *focus-mode framework treatment of each canonical domain* per ADR-0029 §7.3. Domain doctrine lives at `docs/domains/<domain>/`. An in-lane `<domain>/README.md` cross-references the corresponding `docs/domains/<domain>/` but does not duplicate it. The §8.3 anti-pattern "Focus Mode is NOT a domain" is preserved by this distinction.
>
> **Non-canonical domain folder names** (`hydrogeology/`, `roads/`, `railroads/`, `atmosphere/`, `people/`, `settlements-infrastructure/`) are `drift-within-lane` (wrong name, same role) and require per-domain content review against `KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.md` Appendix C before relocation.

### 3.6 Anything else under `docs/focus-mode/`

| Pattern | Disposition | Authority |
|---|---|---|
| `*.schema.json` (any depth) | `drift-out-of-lane` | belongs in `schemas/contracts/v1/focus_mode/` per directory-rules.md §6.4 + ADR-0001 |
| `*.rego` (any depth) | `drift-out-of-lane` | belongs in `policy/` per directory-rules.md §6.5 + ADR-0003 |
| `*.py` (any depth) | `drift-out-of-lane` | belongs in `tools/` per directory-rules.md §6.6 |
| `**/{valid,invalid}/*.json` | `drift-out-of-lane` | fixtures belong in `fixtures/focus_modes/<area>/{valid,invalid}/` per directory-rules.md §6.6 + §6.7.2 |
| `source[-_]descriptors.ya?ml` | `drift-out-of-lane` | belongs in `data/catalog/sources/<area>/` per directory-rules.md §6.7.2 |
| `*[Rr]elease*[Mm]anifest*.json` | `drift-out-of-lane` | belongs in `release/manifests/focus_modes/` per directory-rules.md §6.7.2 |
| Anything else | `unknown` | halt for human review |

[↑ Back to top](#top)

---

## 4. Drift signature reference

The categorizer reports drift findings with one or more **signature tags** in addition to the disposition. The seven signatures and their meanings:

| Sig | Description | Resolution path |
|---|---|---|
| **#1** | Legacy plural lane name (`docs/focus-modes/` instead of `docs/focus-mode/`) | mechanical rename per ADR-0029 §3.6 (closes OPEN-FM-01) |
| **#2** | File under a container subdirectory (`counties/`, `state/`, etc.) | **CANONICAL** per ADR-0029 §3.2 — no longer a drift signature post-ADR-0029. Categorizer should be updated to drop this tag. |
| **#3** | File under `state/` container — state-scale | gated on ADR-0028 acceptance; informational tag only |
| **#4** | Domain folder at lane root | **CANONICAL** per §3.5 — no longer a drift signature post-ADR-0029. The earlier "move to docs/domains/" disposition was wrong; in-lane domain folders are *framework treatment* per ADR-0029 §7.3 |
| **#5** | Legacy kebab-case area dir (`<area>-county`) | mechanical rename to `<area>_county` per ADR-0029 §3.3 (closes OPEN-DR-08) |
| **#6** | Non-canonical domain folder name | per-domain content review against Atlas Appendix C; reconciliation is per-folder content work |
| **#7** | Legacy seven-file split in per-area lane | consolidate into `<area>_<scope>_focus_mode_build_plan.md` per ADR-0029 §3.4 |

> [!NOTE]
> Signatures #2 and #4 in the v1 categorizer were authored against the pre-ADR-0029 spec (flat layout; domain folders → docs/domains/). Post-ADR-0029 they are **not drift**. The v2 categorizer at `/tmp/kfm-organize/organize_v2.py` retains them with informational dispositions; production validator updates per ADR-0029 §6.3 will remove them.

[↑ Back to top](#top)

---

## 5. Disposition policy — what each category triggers

| Disposition | CI behavior | Author action |
|---|---|---|
| `keep-root` | pass | none |
| `keep-area` | pass | none |
| `keep-template` | pass | none |
| `optional-keep` | pass | none |
| `drift-within-lane` | **warn** in PR review; **fail** at next minor version | rename / consolidate per the resolution column of §4 |
| `drift-out-of-lane` | **fail** | relocate to the canonical target root per §3.6 |
| `unknown` | **fail** | author or reviewer must classify the file: rename to a canonical pattern, relocate, or delete |

CI fails the PR if any file in `docs/focus-mode/` has disposition `drift-out-of-lane` or `unknown`. `drift-within-lane` is a warning during the migration window and becomes a failure at the next minor version of `directory-rules.md` after ADR-0029 acceptance.

[↑ Back to top](#top)

---

## 6. Exemptions and edge cases

### 6.1 Hidden files

Any file or directory whose name begins with `.` is skipped from categorization. This includes `.gitkeep`, `.codeowners`, editor metadata, etc.

### 6.2 Empty placeholder files

A 1-byte `README.md` is treated identically to a populated `README.md` for categorization purposes. Population is a separate concern tracked elsewhere (per-area content work). The categorizer does not enforce content; it enforces placement.

### 6.3 Legacy filenames during migration window

For one minor version of `directory-rules.md` after ADR-0029 acceptance, the following legacy filenames are tolerated as `drift-within-lane` (warn, not fail):

- Lane-root `COUNTY_INDEX.md`, `STATE_INDEX.md` (now container-scoped)
- Kebab-case templates: `county-build-plan.md`, `state-build-plan.md`
- Kebab-case area dirs: `<area>-county/`, `kansas-state/`
- Seven-file split: `build-plan.md`, `layer-registry.md`, `evidence-model.md`, `acceptance-checklist.md`, `source-seed-list.md`, `public-safety-notes.md`

After the migration window, these become `drift-out-of-lane` (fail).

### 6.4 The two `domains.md` files

There are two `domains.md` files in the live corpus and they have **different roles**:

1. `docs/focus-mode/counties/domains.md` — **cross-domain composition reference** for county-scale Focus Modes; `optional-keep` (§3.2). Owned by `<OWNER:focus-mode-steward>`.
2. `docs/domains/INDEX.md` (PROPOSED) — domain-doctrine root index; lives **out of lane** per directory-rules.md §12.

The two files do not duplicate each other and are governed separately. This document only categorizes the first.

[↑ Back to top](#top)

---

## 7. Cross-references and out-of-scope rules

### 7.1 Out of scope for this document

- **Cross-root placement** (`schemas/`, `policy/`, `data/`, `tools/`, `release/`, etc.). Governed by `docs/doctrine/directory-rules.md`; this document only cites it.
- **Per-area lane content** — *what* each per-area build plan must say is governed by `docs/focus-mode/README.md` v0.5 §13–§14 and the consolidated template at `docs/focus-mode/counties/_template/county_focus_mode_build_plan.md`. This document only governs *which files* are present.
- **Sensitivity tiers** — `docs/focus-mode/README.md` v0.5 §15 + `docs/standards/SENSITIVITY_RUBRIC.md`. Per-file sensitivity is content, not placement.
- **Schema and validator implementation** — `schemas/contracts/v1/focus_mode/` (ADR-0001) and `tools/validators/`. This document specifies the rules; the validator implements them.

### 7.2 Cross-references to companion documents

- `docs/focus-mode/README.md` v0.5 — orientation and design rationale (the **why**); this document is the categorization spec (the **what**).
- `docs/focus-mode/counties/domains.md` v0.1 — cross-domain composition reference; how the 13 domains compose in a county slice.
- `docs/doctrine/directory-rules.md` v1.2 (as amended by ADR-0029 §7) — root-level placement contract.
- `docs/adr/ADR-0029-focus-mode-lane-structure-canonized.md` — the structural decision this document implements.
- `docs/adr/ADR-0028 — State-scale Focus Mode scope.md` — `-state` scope + 13-domain coverage rule (independent prerequisite for state-scale rules in §3.2 / §3.3).

[↑ Back to top](#top)

---

## 8. Categorizer contract

The categorizer at `/tmp/kfm-organize/organize_v2.py` (working reference implementation as of commit `334b8d6` on branch `claude/magical-johnson-jP2GB`) implements this document's rules. Its production successor at `tools/validators/validate_focus_mode_index.py` (path **NEEDS_VERIFICATION**) MUST:

1. Accept this document as its specification.
2. Emit one disposition tag per file from the set: `keep-root | keep-area | keep-template | optional-keep | drift-within-lane | drift-out-of-lane | unknown`.
3. Emit zero or more signature tags per file from §4.
4. Emit a per-file `rationale` string citing the §3.x rule that applied.
5. Exit non-zero if any file's disposition is `drift-out-of-lane` or `unknown` (per §5).
6. Exit non-zero if a `REQUIRED` file is missing from a present container per §3.2.
7. Verify (as a separate check, not categorization) that each per-area lane's `<area>_<scope>_focus_mode_build_plan.md` enumerates exactly the 13 canonical domain keys in its `domain_coverage` block per ADR-0028 §3.

The categorizer is **idempotent and read-only**. It does not move, rename, or delete files.

[↑ Back to top](#top)

---

## 9. Self-check

- [x] **Every path under `docs/focus-mode/` is covered by exactly one rule in §3?** Yes; §3.6's catch-all closes the space.
- [x] **No rule in §3 contradicts another?** Yes; rules apply in §3.1 → §3.6 order, first match wins.
- [x] **Every disposition in §5 has a corresponding category in §3?** Yes; 4 keep-* / optional dispositions + 3 drift dispositions.
- [x] **Every drift signature in §4 has a documented resolution path?** Yes.
- [x] **No fabricated owner names?** Yes; placeholders `<OWNER:focus-mode-steward>` etc.
- [x] **Cite-or-abstain on all doctrinal claims?** Yes; every rule cites a specific section of ADR-0029, ADR-0028, README v0.5, or directory-rules.md.
- [x] **Truth labels on uncertain claims?** Yes; `NEEDS_VERIFICATION` on `tools/validators/validate_focus_mode_index.py` path.
- [x] **Backwards-compatible during migration?** Yes (§6.3 migration window).

[↑ Back to top](#top)

---

**Last updated:** 2026-05-24 · v0.2 · Authority: derives from ADR-0029 + ADR-0028 + `docs/focus-mode/README.md` v0.5 + `docs/doctrine/directory-rules.md` v1.2
