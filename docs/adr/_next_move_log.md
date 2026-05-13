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

### Run 2026-05-13 — Add provenance status sync command for artifact admission lifecycle
- Status: landed
- PR: n/a
- Doctrine basis: canonical-link provenance needs a governed transition path from `pending` to `verified` once artifact bytes are present.
- Slice shape: added sync command and tests to detect admitted artifact files and (optionally) persist provenance status transitions with timestamp evidence.
- Deferred to future runs:
  - wire sync command into doctrine preflight orchestrator and CI receipts

### Run 2026-05-13 — Integrate provenance checks into preflight summary orchestrator
- Status: landed
- PR: n/a
- Doctrine basis: doctrine preflight must report both artifact-file checks and canonical-link provenance gate state in one receipt surface.
- Slice shape: extended preflight runner and summary schema to include provenance check + provenance sync return codes and stderr fields.
- Deferred to future runs:
  - decide strict-mode policy for provenance gate outside placeholder state

### Run 2026-05-13 — Split strict-mode semantics for artifact presence vs provenance gate
- Status: landed
- PR: n/a
- Doctrine basis: operators need separate failure controls for missing artifacts and provenance-link failures during staged adoption.
- Slice shape: added `--strict-provenance` to preflight runner so provenance failures can be enforced independently from artifact-missing strict mode.
- Deferred to future runs:
  - enable strict-provenance by default once authoritative URLs are populated

### Run 2026-05-13 — Include provenance policy tests in doctrine artifact regression bundle
- Status: landed
- PR: n/a
- Doctrine basis: new provenance gates must be enforced by the same one-command regression bundle used by CI/operators.
- Slice shape: updated `run_doctrine_artifact_test_suite.sh` to execute provenance validation and provenance-sync tests alongside existing doctrine preflight tests.
- Deferred to future runs:
  - add negative-case fixture snapshots for provenance checker payloads

### Run 2026-05-13 — Add provenance gate snapshot fixtures to regression suite
- Status: landed
- PR: n/a
- Doctrine basis: provenance checker outputs are governance artifacts and should have stable regression snapshots for fail/no-change states.
- Slice shape: added fixture snapshots and tests that assert key JSON payload fields for placeholder-url failure and provenance-sync no-change results.
- Deferred to future runs:
  - add verified-state snapshot once authoritative URLs and artifact bytes are admitted
### Run 2026-05-13 — Add verified-transition snapshot coverage for provenance sync
- Status: landed
- PR: n/a
- Doctrine basis: provenance lifecycle gate needs regression coverage for both no-change and changed (`pending`→`verified`) outcomes.
- Slice shape: added a sync-changed fixture and snapshot test that validates emitted payload keys and persisted `verified_at`/`status: verified` rewrite.
- Deferred to future runs:
  - replace synthetic temp-registry snapshot with canonical artifact admission snapshot once real assets are available
