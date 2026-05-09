# VERIFICATION_BACKLOG register

Indexes the corresponding `control_plane/*.yaml` register.
- 2026-05-09: NEEDS VERIFICATION: domain-specific evidence_bundle duplicates should be migrated to $ref in follow-up PR.
- 2026-05-09: CONFIRMED PR-001 closes the local-resolver gap. Open: domain-specific schemas not yet on `$ref` form remain candidates for follow-up; runtime/UI/policy slices still UNKNOWN.


- 2026-05-09 — OPEN: Release manifest schema is intentionally permissive in PR-001; fields for signed manifests, layer manifests, and rollback linkage are PROPOSED for ADR-0023 follow-up.
