<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/adr-0029-supplement-directory-rules-amendments   # NEEDS_VERIFICATION until registered
title: "ADR-0029 Supplement — Directory Rules amendments (paste-ready patches)"
type: adr-supplement
adr_id: ADR-0029-supplement
version: v0.1
status: proposed
created: 2026-05-24
updated: 2026-05-24
owners:
  - <OWNER:directory-rules-steward>
  - <OWNER:focus-mode-steward>
policy_label: public
authority: paste-ready patches for the four amendments to docs/doctrine/directory-rules.md specified in ADR-0029 §7
supplements: docs/adr/ADR-0029-focus-mode-lane-structure-canonized.md
related:
  - docs/adr/ADR-0029-focus-mode-lane-structure-canonized.md
  - docs/doctrine/directory-rules.md
  - docs/focus-mode/README.md
  - docs/focus-mode/ORGANIZATION_RULES.md
tags:
  - kfm
  - adr-supplement
  - directory-rules
  - amendment
  - focus-mode
  - paste-ready
notes:
  - This is a SUPPLEMENT to ADR-0029, not a replacement of directory-rules.md itself. A human applies the patches below in a separate PR with full diff visibility.
  - The pre-amendment text quoted in the "Before" sections of §§4–7 of this supplement was captured from docs/doctrine/directory-rules.md at commit `b71f2e5` on branch `claude/magical-johnson-jP2GB`. If the live §6.7.2 / §6.7.3 / §13.5 / §18.d text has drifted since, re-run the verification block in §3 before applying.
[/KFM_META_BLOCK_V2] -->

[![status: proposed](https://img.shields.io/badge/status-proposed-yellow)](#1-purpose)
[![supplements: ADR-0029](https://img.shields.io/badge/supplements-ADR--0029-blue)](docs/adr/ADR-0029-focus-mode-lane-structure-canonized.md)
[![target: docs/doctrine/directory-rules.md](https://img.shields.io/badge/target-docs%2Fdoctrine%2Fdirectory--rules.md-orange)](docs/doctrine/directory-rules.md)

<a id="top"></a>

# ADR-0029 Supplement — Directory Rules amendments (paste-ready patches)

## Contents

- [1. Purpose](#1-purpose)
- [2. Pre-amendment verification](#2-pre-amendment-verification)
- [3. Amendment 1 — §6.7.2 placement table, `docs/` row](#3-amendment-1--672-placement-table-docs-row)
- [4. Amendment 2 — §6.7.3 casing convention](#4-amendment-2--673-casing-convention)
- [5. Amendment 3 — §13.5 drift register clarification](#5-amendment-3--135-drift-register-clarification)
- [6. Amendment 4 — §18.d closure entries](#6-amendment-4--18d-closure-entries)
- [7. Validator updates required](#7-validator-updates-required)
- [8. Application checklist](#8-application-checklist)
- [9. Rollback path](#9-rollback-path)
- [10. Cross-references](#10-cross-references)

---

## 1. Purpose

ADR-0029 §7 specifies four amendments to `docs/doctrine/directory-rules.md`. This supplement renders them as paste-ready patches so the directory-rules steward can apply them in **one PR with full diff visibility**.

**Out of scope:** this supplement does NOT modify `docs/doctrine/directory-rules.md` directly. A human applies the patches per §8. Do not skip the pre-amendment verification (§2) — if the live §-text has drifted from what's quoted in the "Before" blocks below, re-quote before applying.

[↑ Back to top](#top)

---

## 2. Pre-amendment verification

Run this before applying any patch. It captures the current §6.7.2 / §6.7.3 / §13.5 / §18.d text so you can compare it visually to the "Before" blocks in §§3–6 of this supplement.

```bash
# Run from the repo root; outputs the current sections for visual diff
sed -n '/^### *6\.7\.2/,/^### *6\.7\.[3-9]/p' docs/doctrine/directory-rules.md > /tmp/dr-current-6.7.2.md
sed -n '/^### *6\.7\.3/,/^### *6\.7\.[4-9]/p' docs/doctrine/directory-rules.md > /tmp/dr-current-6.7.3.md
sed -n '/^## *13\.5/,/^## *13\.[6-9]/p'      docs/doctrine/directory-rules.md > /tmp/dr-current-13.5.md
sed -n '/^## *18\.d/,/^## *18\.[e-z]/p'      docs/doctrine/directory-rules.md > /tmp/dr-current-18.d.md
echo "Review /tmp/dr-current-*.md before applying patches in §§3-6 below."
ls -la /tmp/dr-current-*.md
```

If any of the four `dr-current-*.md` files differs from the "Before" block in the corresponding amendment section below, **STOP**. Re-quote the live text into the "Before" block of this supplement (with a citation to the commit hash you captured from), then proceed.

[↑ Back to top](#top)

---

## 3. Amendment 1 — §6.7.2 placement table, `docs/` row

### 3.1 Before (verbatim from commit `b71f2e5`)

The §6.7.2 example currently specifies the Focus Mode root in `docs/` as a **flat** layout with **plural** lane name and **kebab-case** area dirs with `-<scope>` suffix:

```
docs/focus-modes/<area>-<scope>/
e.g., docs/focus-modes/ellsworth-county/
```

> [!NOTE]
> **NEEDS_VERIFICATION** at application time. The live §6.7.2 placement table may render this as a multi-column row; quote it as it appears at application time. The semantic content above is what this amendment replaces.

### 3.2 After (per ADR-0029 §7.1)

Render as a single placement-table row (or update the existing row in place):

```
| docs/ | docs/focus-mode/{counties,state,regions,corridors}/<area>_<scope>/ | singular lane, kebab-case container, snake_case area dir + scope suffix | README.md, <area>_<scope>_focus_mode_build_plan.md, optional *-notes.md; plus container-level COUNTY_INDEX.md / STATE_INDEX.md and container-scoped _template/; plus 13 in-lane <domain>/ folders holding focus-mode treatment of each canonical domain |
```

Authority for the four placement properties:

| Property | Authority |
|---|---|
| Singular `focus-mode/` (not `focus-modes/`) | ADR-0029 §3.6 (closes OPEN-FM-01) |
| Container subdirs (`counties/`, `state/`, `regions/`, `corridors/`) | ADR-0029 §3.2 |
| `snake_case` area dirs with `_<scope>` suffix | ADR-0029 §3.3 (closes OPEN-DR-08) |
| Single-file `<area>_<scope>_focus_mode_build_plan.md` | ADR-0029 §3.4 |
| 13 in-lane domain folders | ADR-0028 §3 (13-domain coverage rule); ADR-0029 §7.3 (framework treatment, not domain doctrine) |

[↑ Back to top](#top)

---

## 4. Amendment 2 — §6.7.3 casing convention

### 4.1 Before (NEEDS_VERIFICATION)

`docs/doctrine/directory-rules.md` §6.7.3 is the per-host-root casing convention. The current bullet list in this section does not include a Focus Mode exception (as of commit `b71f2e5`). Quote the current §6.7.3 text from `/tmp/dr-current-6.7.3.md` at application time and confirm.

### 4.2 After (per ADR-0029 §7.2)

**Add** a new bullet to the per-host-root casing list:

> - **Singular + snake_case + scope suffix in `docs/focus-mode/`:** `docs/focus-mode/counties/ellsworth_county/`, `docs/focus-mode/state/kansas_state/`. **Deliberate exception** to the general kebab-case sibling-lane convention in `docs/`. Rationale per ADR-0029 §3.3 and §4.3 (self-describing-filename principle).

This bullet is added — no existing bullet is removed or modified.

[↑ Back to top](#top)

---

## 5. Amendment 3 — §13.5 drift register clarification

### 5.1 Before (NEEDS_VERIFICATION)

`docs/doctrine/directory-rules.md` §13.5 enumerates drift anti-patterns. The current list includes (per commit `b71f2e5`) the §8.3 "Focus Mode is NOT a domain" anti-pattern. Quote the current §13.5 text from `/tmp/dr-current-13.5.md` at application time.

### 5.2 After (per ADR-0029 §7.3)

**Add** a clarifying note (does not remove or modify existing anti-patterns):

> **Clarification per ADR-0029.** Per-domain folders inside `docs/focus-mode/<domain>/` are *focus-mode framework treatment of each domain*, NOT domain doctrine. Domain doctrine remains at `docs/domains/<domain>/` per §12 Domain Placement Law. The in-lane `<domain>/README.md` files cross-reference `docs/domains/<domain>/` but do not duplicate it. The §8.3 "Focus Mode is NOT a domain" anti-pattern is preserved: the in-lane folders are not domains, they are framework treatments.

This clarification is added — no existing anti-pattern is removed or weakened.

[↑ Back to top](#top)

---

## 6. Amendment 4 — §18.d closure entries

### 6.1 Before (NEEDS_VERIFICATION)

`docs/doctrine/directory-rules.md` §18.d is the OPEN-items register. OPEN-FM-01 and OPEN-DR-08 are currently `open`. Quote the current §18.d text from `/tmp/dr-current-18.d.md` at application time.

### 6.2 After (per ADR-0029 §7.4)

Update the four ID rows:

| ID | Status before | Status after | Citation |
|---|---|---|---|
| OPEN-FM-01 (singular vs plural Focus Mode lane name) | open | **CLOSED — singular canonical** | ADR-0029 §3.6 |
| OPEN-DR-08 (per-host-root casing for Focus Mode area dirs) | open | **CLOSED — snake_case for Focus Mode area dirs** | ADR-0029 §3.3 |
| OPEN-FM-09 (`-state` scope) | open | unchanged — closed by ADR-0028 §3 (independent) | — |
| OPEN-FM-10 (13-domain coverage rule) | open | unchanged — closed by ADR-0028 §3 (independent) | — |

Two closures are by this amendment (OPEN-FM-01 + OPEN-DR-08). The other two rows are listed for clarity — their closures are by ADR-0028, not this amendment, and their `status: closed` line was already added when ADR-0028 was accepted (or is added in the same PR if ADR-0028 has not yet been applied).

[↑ Back to top](#top)

---

## 7. Validator updates required

Per ADR-0029 §6.3, the validator `tools/validators/validate_focus_mode_index.py` (path **NEEDS_VERIFICATION**) MUST be updated to:

1. Accept `docs/focus-mode/` (singular) as the canonical lane root.
2. Recognize `counties/`, `state/`, `regions/`, `corridors/` as canonical container subdirectories.
3. Recognize `snake_case` area directory names with explicit `_<scope>` suffix.
4. Recognize `<area>_<scope>_focus_mode_build_plan.md` as the canonical per-area build-plan filename.
5. Resolve cross-references to all 13 canonical domain folders and verify the `domain_coverage` map enumerates exactly the 13 canonical keys.
6. Flag legacy plural (`docs/focus-modes/`), legacy kebab (`<area>-county/`), legacy seven-file split, and legacy fragmentary template (`county-build-plan.md`) as drift with a citation to ADR-0029.

The reference implementation at `/tmp/kfm-organize/organize_v2.py` (working v2 at commit `b71f2e5`) implements rules 1–4 in spirit. The production validator update is **out of scope for this supplement** — it requires a separate `tools/validators/` PR.

The categorization spec is `docs/focus-mode/ORGANIZATION_RULES.md` v0.2 (lands in the same chain as this supplement).

[↑ Back to top](#top)

---

## 8. Application checklist

Step-by-step a human-reviewer follows to apply this supplement:

- [ ] Run the pre-amendment verification bash block in §2.
- [ ] For each of §§3–6, read the "Before" block against the corresponding `/tmp/dr-current-*.md` file. If they differ, **STOP** and re-quote.
- [ ] Apply Amendment 1 to `docs/doctrine/directory-rules.md` §6.7.2 (replace the placement-table row for `docs/`).
- [ ] Apply Amendment 2 to §6.7.3 (add the bullet).
- [ ] Apply Amendment 3 to §13.5 (add the clarifying note).
- [ ] Apply Amendment 4 to §18.d (update four ID rows).
- [ ] Bump `directory-rules.md` version (v1.2 → v1.3) in §0 Status & Authority and in the §21 changelog.
- [ ] Update `directory-rules.md` §21 changelog with a new "v1.2 → v1.3" entry citing ADR-0029.
- [ ] Commit with message: `docs/doctrine/directory-rules.md: v1.3 — amendments per ADR-0029 (Focus Mode lane structure canonized)`.
- [ ] Re-run the categorizer: `python3 /tmp/kfm-organize/organize_v2.py docs/focus-mode/`. Should still report a stable disposition set (no behavior change from amendment; the categorizer rules were authored against the amendments-after state per ADR-0029 §3).
- [ ] (Optional) Mark this supplement file `status: accepted` after the directory-rules PR merges.

[↑ Back to top](#top)

---

## 9. Rollback path

If the amendments are rejected after merge:

- Revert the directory-rules PR.
- Set ADR-0029 `status: superseded` with a `superseded_by` link to the rationale.
- Set this supplement `status: superseded`.
- Re-open OPEN-FM-01 and OPEN-DR-08 in `directory-rules.md` §18.d.
- The supplement file itself MAY be deleted if no longer cited (preserved in git history).
- The pack-v2 templates (`county_focus_mode_build_plan.md`, `state_focus_mode_build_plan.md`) and `ORGANIZATION_RULES.md` v0.2 are independent — their fate is governed by ADR-0029's rollback (§9), not by this supplement.

[↑ Back to top](#top)

---

## 10. Cross-references

- `docs/adr/ADR-0029-focus-mode-lane-structure-canonized.md` — the ADR this supplements
- `docs/doctrine/directory-rules.md` v1.2 — the file being amended
- `docs/focus-mode/README.md` v0.5 — orientation; reflects ADR-0029
- `docs/focus-mode/ORGANIZATION_RULES.md` v0.2 — categorization spec
- `docs/adr/ADR-0028 — State-scale Focus Mode scope.md` — independent prerequisite for §6.2 OPEN-FM-09 / OPEN-FM-10 closures

[↑ Back to top](#top)

---

**Last updated:** 2026-05-24 · v0.1 · Authority: paste-ready patches for ADR-0029 §7 amendments
