# Flora Current State

## Verified at
- **Date:** 2026-04-27
- **Path scanned:** `docs/domains/flora/`

## Confirmed files present
- `README.md`
- `ARCHITECTURE.md`
- `CURRENT_STATE.md`
- `SOURCE_REGISTRY.md`
- `DATA_MODEL.md`
- `PIPELINES_AND_LIFECYCLE.md`
- `PUBLICATION_AND_POLICY.md`
- `UI_AND_EVIDENCE_DRAWER.md`
- `VERIFICATION_BACKLOG.md`
- `CHANGELOG.md`
- `ROADMAP.md`
- `FILE_MANIFEST.md`
- `GLOSSARY.md`
- `IDEA_INTAKE.md`

## Confirmed implementation status
- This directory now contains a complete flora documentation skeleton aligned to the Flora README companion map.
- Presence of documentation does **not** prove runtime implementation in API, pipeline, schema, or UI code.

## Unknowns still requiring verification
- Canonical schema home for flora contracts.
- Existing flora source descriptors and rights snapshots.
- Policy engine/toolchain location and test harness.
- Governed API route and DTO implementation paths.
- UI layer registry and Evidence Drawer runtime contracts.

## Next verification actions
1. Inventory `schemas/`, `contracts/`, `policy/`, `tools/validators/`, `pipelines/`, and app directories.
2. Resolve schema-home ambiguity with ADR if needed.
3. Add fixture-driven validation checks for rights and sensitivity fail-closed behavior.
