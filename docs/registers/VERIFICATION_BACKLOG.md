# VERIFICATION_BACKLOG register

Indexes the corresponding `control_plane/*.yaml` register.
- 2026-05-09: NEEDS VERIFICATION: domain-specific evidence_bundle duplicates should be migrated to $ref in follow-up PR.
- 2026-05-09: CONFIRMED PR-001 closes the local-resolver gap. Open: domain-specific schemas not yet on `$ref` form remain candidates for follow-up; runtime/UI/policy slices still UNKNOWN.


- 2026-05-09 — OPEN: Release manifest schema is intentionally permissive in PR-001; fields for signed manifests, layer manifests, and rollback linkage are PROPOSED for ADR-0023 follow-up.

- 2026-05-14 — OPEN: `docs/registers/CANONICAL_LINEAGE_EXPLORATORY.md` path and template exist as PROPOSED governance scaffold; first steward-reviewed entry and citation pattern are NEEDS VERIFICATION.
- 2026-05-15 — OPEN: `docs/doctrine/directory-rules.md` created as PROPOSED canonical-home stub; NEEDS VERIFICATION steward decision on authority cutover vs mirror pattern from `docs/directory-rules.md`.
- 2026-05-15 — OPEN: `docs/registers/AUTHORITY_LADDER.md` and `docs/registers/OBJECT_FAMILY_MAP.md` created as PROPOSED naming-parity scaffolds; NEEDS VERIFICATION whether legacy `OBJECT_FAMILY.md` remains canonical, is superseded, or is maintained as compatibility mirror.

- 2026-05-15 — RESOLVED: Re-ran branch-local checks and attached evidence in `control_plane/normalized_summary_consumer_readiness.yaml`; consumer statuses restored to `validated` on 2026-05-16.

- 2026-05-15 — OPEN: Populate steward-approved authoritative `source_url` values in `control_plane/doctrine_artifact_provenance_sources.yaml` for each required doctrine artifact before provenance status may be promoted.

- 2026-05-15 — OPEN: Resolve canonical filename/path mapping for required doctrine artifacts and promote `control_plane/document_registry_doctrine_required.yaml` entries from `needs_verification` only after steward-approved path + provenance evidence is attached.

- 2026-05-15 — RESOLVED: Remediated parser compatibility for `needs_verification` status; `run_doctrine_artifact_preflight.py` no longer trips the prior check path and downstream consistency tests now pass.

- 2026-05-15 — RESOLVED: Reran `pytest -q tests/policy/test_preflight_summary_consistency.py` (5 passed) and promoted consumer readiness to `validated` with 2026-05-16 evidence timestamp.
- 2026-05-16 — OPEN: Finalize canonical path + provenance mapping for doctrine inputs by (a) admitting a canonical PDF source for `KFM_Domains_Culmination_Atlas_v1_1` (currently Markdown-only), and (b) approving whether spaced filenames remain authoritative aliases or must be normalized to underscore canonical names for `New Ideas 5-8-26` and `DomainDriven Design Reference`.
- 2026-05-17 — OPEN: Execute canonicalization decision as three tracked actions: (1) choose canonical artifact form for `KFM_Domains_Culmination_Atlas_v1_1` (PDF admission vs approved Markdown exception), (2) decide authoritative naming for `New Ideas 5-8-26` (spaced alias vs underscore canonical), and (3) decide authoritative naming for `DomainDriven Design Reference` (spaced alias vs underscore canonical), each with provenance evidence attached before promotion from `needs_verification`.
