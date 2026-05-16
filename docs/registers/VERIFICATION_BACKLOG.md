# VERIFICATION_BACKLOG register

Indexes the corresponding `control_plane/*.yaml` register.
- 2026-05-09: NEEDS VERIFICATION: domain-specific evidence_bundle duplicates should be migrated to $ref in follow-up PR.
- 2026-05-09: CONFIRMED PR-001 closes the local-resolver gap. Open: domain-specific schemas not yet on `$ref` form remain candidates for follow-up; runtime/UI/policy slices still UNKNOWN.


- 2026-05-09 — OPEN: Release manifest schema is intentionally permissive in PR-001; fields for signed manifests, layer manifests, and rollback linkage are PROPOSED for ADR-0023 follow-up.

- 2026-05-14 — OPEN: `docs/registers/CANONICAL_LINEAGE_EXPLORATORY.md` path and template exist as PROPOSED governance scaffold; first steward-reviewed entry and citation pattern are NEEDS VERIFICATION.
- 2026-05-15 — OPEN: `docs/doctrine/directory-rules.md` created as PROPOSED canonical-home stub; NEEDS VERIFICATION steward decision on authority cutover vs mirror pattern from `docs/directory-rules.md`.
- 2026-05-15 — OPEN: `docs/registers/AUTHORITY_LADDER.md` and `docs/registers/OBJECT_FAMILY_MAP.md` created as PROPOSED naming-parity scaffolds; NEEDS VERIFICATION whether legacy `OBJECT_FAMILY.md` remains canonical, is superseded, or is maintained as compatibility mirror.

- 2026-05-15 — OPEN: Re-run and attach branch-local evidence for doctrine artifact test suite and policy preflight consistency checks before restoring `validated` readiness in `control_plane/normalized_summary_consumer_readiness.yaml`.

- 2026-05-15 — OPEN: Populate steward-approved authoritative `source_url` values in `control_plane/doctrine_artifact_provenance_sources.yaml` for each required doctrine artifact before provenance status may be promoted.

- 2026-05-15 — OPEN: Resolve canonical filename/path mapping for required doctrine artifacts and promote `control_plane/document_registry_doctrine_required.yaml` entries from `needs_verification` only after steward-approved path + provenance evidence is attached.

- 2026-05-15 — OPEN: Investigate and remediate `run_doctrine_artifact_preflight.py` check failure (`render_returncode: 2`, `skipped_due_to_check_error`) so `tests/policy/test_preflight_summary_consistency.py` can pass and readiness can be promoted.

- 2026-05-15 — OPEN: After fixing preflight check error, rerun `pytest -q tests/policy/test_preflight_summary_consistency.py` and only then promote consumer status from `failing` to `passing` with updated evidence date.
