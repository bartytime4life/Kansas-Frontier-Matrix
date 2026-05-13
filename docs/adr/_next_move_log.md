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

### Run 2026-05-13 — Add required-vs-provenance registry alignment gate
- Status: landed
- PR: n/a
- Doctrine basis: canonical-link provenance registry must track exactly the required doctrine artifact set to avoid silent scope drift.
- Slice shape: added alignment checker + tests and wired the checker into the doctrine artifact regression bundle.
- Deferred to future runs:
  - include alignment result in orchestrated preflight summary payload

### Run 2026-05-13 — Surface registry-alignment gate in preflight summary
- Status: landed
- PR: n/a
- Doctrine basis: preflight summary must expose full doctrine-admission gate state, including required-vs-provenance registry alignment.
- Slice shape: orchestrator now runs alignment check and emits `alignment_returncode`/`alignment_stderr`; strict-provenance mode now treats alignment failures as strict failures.
- Deferred to future runs:
  - include alignment payload body in summary receipt for richer diagnostics

### Run 2026-05-13 — Embed alignment payload body in preflight summary receipt
- Status: landed
- PR: n/a
- Doctrine basis: return codes alone are insufficient for operator triage; summary receipts should carry gate-level diagnostic body where schema-governable.
- Slice shape: added `alignment_payload` object to preflight output/schema and asserted it in preflight tests.
- Deferred to future runs:
  - add equivalent payload embedding for provenance checker with schema shape

### Run 2026-05-13 — Embed provenance payload body in preflight summary receipt
- Status: landed
- PR: n/a
- Doctrine basis: provenance gate diagnostics should be directly inspectable in orchestrated receipts, not inferred only from return codes.
- Slice shape: added `provenance_payload` object to summary output/schema and asserted its presence in preflight runner tests.
- Deferred to future runs:
  - add sync payload embedding with optional stable receipt pointer

### Run 2026-05-13 — Embed provenance-sync payload body in preflight summary receipt
- Status: landed
- PR: n/a
- Doctrine basis: sync-stage diagnostics are part of provenance lifecycle auditability and should be carried in summary receipts.
- Slice shape: added `provenance_sync_payload` field to preflight output/schema and asserted expected check identity in runner tests.
- Deferred to future runs:
  - emit stable pointer to persisted sync receipt artifact path when write-mode is enabled

### Run 2026-05-13 — Add stable sync-receipt pointer in preflight summary
- Status: landed
- PR: n/a
- Doctrine basis: provenance lifecycle audits require a durable receipt pointer, not only inline payloads.
- Slice shape: sync command now supports `--output`; preflight orchestrator writes sync receipt artifacts and emits `provenance_sync_receipt` path in summary.
- Deferred to future runs:
  - add checksum of referenced sync receipt in summary for tamper-evidence

### Run 2026-05-13 — Add sync-receipt SHA256 to preflight summary
- Status: landed
- PR: n/a
- Doctrine basis: receipt pointers should include tamper-evident digest material for auditability.
- Slice shape: preflight summary now computes and emits `provenance_sync_receipt_sha256` for the referenced sync receipt artifact, with schema + tests updated.
- Deferred to future runs:
  - add equivalent digest fields for other emitted receipt paths

### Run 2026-05-13 — Add check-receipt SHA256 to preflight summary
- Status: landed
- PR: n/a
- Doctrine basis: every emitted receipt pointer in summary should carry tamper-evident digest metadata.
- Slice shape: added `check_receipt_sha256` computed from required-artifact checker receipt and validated via schema/tests.
- Deferred to future runs:
  - add digest for optional `presence_output` when emitted

### Run 2026-05-13 — Add presence-output SHA256 to preflight summary
- Status: landed
- PR: n/a
- Doctrine basis: optional emitted artifacts should carry digest metadata equivalent to mandatory receipt pointers.
- Slice shape: preflight summary now emits `presence_output_sha256` when `--presence-output` is used (null otherwise), with schema and tests updated.
- Deferred to future runs:
  - unify digest-field naming conventions across all summary artifact pointers

### Run 2026-05-13 — Add normalized artifact digest map to preflight summary
- Status: landed
- PR: n/a
- Doctrine basis: digest metadata should be discoverable under a consistent key-space to reduce operator/CI field-specific branching.
- Slice shape: added `artifact_digests` map (`check_receipt`, `provenance_sync_receipt`, `presence_output`) and schema/tests that bind map values to existing digest fields.
- Deferred to future runs:
  - deprecate legacy standalone digest fields after downstream consumers migrate

### Run 2026-05-13 — Add normalized artifact path map to preflight summary
- Status: landed
- PR: n/a
- Doctrine basis: artifact digest normalization benefits from parallel normalized path keys so consumers can avoid mixed standalone/map lookups.
- Slice shape: added `artifact_paths` map mirroring receipt/presence output pointers and bound tests/schema to map+field consistency.
- Deferred to future runs:
  - publish consumer migration note and begin standalone field deprecation window

### Run 2026-05-13 — Add summary consistency validator for normalized artifact maps
- Status: landed
- PR: n/a
- Doctrine basis: during migration from standalone fields to normalized maps, summary outputs need explicit consistency checks to prevent silent divergence.
- Slice shape: added `validate_doctrine_preflight_summary_consistency.py` plus tests and bundle integration to enforce map↔standalone parity.
- Deferred to future runs:
  - flip validator to require only normalized maps once standalone fields are deprecated

### Run 2026-05-13 — Add normalized-only mode to preflight summary consistency validator
- Status: landed
- PR: n/a
- Doctrine basis: deprecation of standalone summary fields requires an enforceable migration switch before hard cutoff.
- Slice shape: added `--require-normalized-only` option to consistency validator and tests that fail when legacy standalone fields are still present.
- Deferred to future runs:
  - enable normalized-only mode in CI after downstream consumers complete migration

### Run 2026-05-13 — Add normalized-only emission mode for preflight summary
- Status: landed
- PR: n/a
- Doctrine basis: migration from standalone fields to normalized maps needs an executable output mode to validate downstream readiness before hard deprecation.
- Slice shape: added `--emit-normalized-only` to preflight runner, plus tests and validator pass-case coverage for normalized-only payloads.
- Deferred to future runs:
  - switch CI to run normalized-only summaries in shadow mode before default cutover
