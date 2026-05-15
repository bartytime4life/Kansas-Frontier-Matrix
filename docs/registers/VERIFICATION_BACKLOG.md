# VERIFICATION_BACKLOG register

Indexes the corresponding `control_plane/*.yaml` register.
- 2026-05-09: NEEDS VERIFICATION: domain-specific evidence_bundle duplicates should be migrated to $ref in follow-up PR.
- 2026-05-09: CONFIRMED PR-001 closes the local-resolver gap. Open: domain-specific schemas not yet on `$ref` form remain candidates for follow-up; runtime/UI/policy slices still UNKNOWN.


- 2026-05-09 — OPEN: Release manifest schema is intentionally permissive in PR-001; fields for signed manifests, layer manifests, and rollback linkage are PROPOSED for ADR-0023 follow-up.

- 2026-05-14 — OPEN: `docs/registers/CANONICAL_LINEAGE_EXPLORATORY.md` path and template exist as PROPOSED governance scaffold; first steward-reviewed entry and citation pattern are NEEDS VERIFICATION.
- 2026-05-15 — OPEN: `docs/doctrine/directory-rules.md` created as PROPOSED canonical-home stub; NEEDS VERIFICATION steward decision on authority cutover vs mirror pattern from `docs/directory-rules.md`.
- 2026-05-15 — OPEN: `docs/registers/AUTHORITY_LADDER.md` and `docs/registers/OBJECT_FAMILY_MAP.md` created as PROPOSED naming-parity scaffolds; NEEDS VERIFICATION whether legacy `OBJECT_FAMILY.md` remains canonical, is superseded, or is maintained as compatibility mirror.
