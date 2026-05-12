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
