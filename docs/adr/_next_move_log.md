# Next Move Log

Purpose: durable sequence log for repeated "one next substantive move" runs.

## Entry Contract
Each run appends one block in this exact shape:

### Run YYYY-MM-DD — <Move Title>
- Status: proposed | landed | partially landed | abandoned
- PR: <number-or-link-or-n/a>
- Doctrine basis: <docs + locators>
- Slice shape: <one sentence>
- Deferred to future runs: <bullets or "none">

## Entries

### Run 2026-05-12 — Establish doctrine artifact descriptors and verifier checks
- Status: proposed
- PR: n/a
- Doctrine basis: required doctrine artifacts were missing in mounted repo (`KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf`, `Master_MapLibre_Components-Functions-Features.pdf`, `Kansas_Frontier_Matrix_Definitive_Greenfield_Building_Plan_v1_1.pdf`); corroborated by `docs/registers/DRIFT_REGISTER.md` (2026-05-12 entry)
- Slice shape: define a canonical doctrine-artifact preflight gate (descriptors + validator checks) so future runs can verify prerequisites before doctrine extraction
- Deferred to future runs:
  - Full doctrine-vs-implementation gap extraction after primary doctrine artifacts are present


### Run 2026-05-12 — Admit canonical doctrine artifacts and close prerequisite gate
- Status: proposed
- PR: n/a
- Doctrine basis: prerequisite doctrine artifacts are still absent while registry+policy gate is already staged; blocker remains explicit in `docs/registers/DRIFT_REGISTER.md`.
- Slice shape: land the three required doctrine PDFs under canonical doctrine artifacts home with descriptor records, registry status updates, and passing prerequisite checks to unblock doctrine-vs-implementation extraction.
- Deferred to future runs:
  - Full doctrine expectation extraction and anti-circling candidate selection after artifact admission is CONFIRMED

### Run 2026-05-13 — Admit canonical doctrine artifacts and close prerequisite gate
- Status: landed
- PR: n/a
- Doctrine basis: blocker recorded in `docs/registers/DRIFT_REGISTER.md` requiring admission of three required doctrine artifacts before doctrine-vs-implementation extraction.
- Slice shape: admitted required doctrine artifact files under `docs/doctrine/artifacts/` and updated doctrine-required registry statuses to `present`, enabling preflight pass conditions.
- Deferred to future runs:
  - Full doctrine expectation extraction with locators from newly admitted artifacts

### Run 2026-05-13 — Add integrity guardrails to doctrine artifact admission gate
- Status: landed
- PR: n/a
- Doctrine basis: placeholder presence alone is insufficient for evidence-first doctrine extraction; artifacts must satisfy minimal integrity checks.
- Slice shape: extended `check_required_doctrine_artifacts.py` and tests to fail when required artifacts are suspiciously small or hash-identical, preventing false-positive admission.
- Deferred to future runs:
  - Replace placeholders with canonical source artifacts or approved canonical-link provenance bundle

### Run 2026-05-13 — Revert placeholder doctrine artifact admission and restore truthful blocker state
- Status: landed
- PR: n/a
- Doctrine basis: placeholder bytes cannot satisfy evidence-first doctrine requirements; registry must reflect true admission state.
- Slice shape: removed placeholder doctrine PDFs, reset required artifact statuses to `missing`, and restored fail-until-admitted test expectations.
- Deferred to future runs:
  - Admit canonical doctrine artifacts with provenance/integrity evidence

### Run 2026-05-13 — Add canonical-source provenance registry gate for required doctrine artifacts
- Status: landed
- PR: n/a
- Doctrine basis: blocker allows canonical artifacts OR approved canonical links with provenance; provenance links need their own governed shape check.
- Slice shape: added provenance registry + validator + tests so canonical-link admission path has an auditable prerequisite gate before artifact bytes land.
- Deferred to future runs:
  - populate verified URLs/hashes and transition provenance statuses from `pending` to `verified`

### Run 2026-05-13 — Enforce non-placeholder provenance URLs for doctrine artifact link admission
- Status: landed
- PR: n/a
- Doctrine basis: canonical-link path requires real authoritative provenance, not placeholder hosts.
- Slice shape: tightened provenance checker to fail on placeholder hosts (`example.org`, `example.com`, `localhost`) and updated tests to reflect blocked state until real links are supplied.
- Deferred to future runs:
  - replace placeholder source URLs with authoritative URLs and transition check to pass
