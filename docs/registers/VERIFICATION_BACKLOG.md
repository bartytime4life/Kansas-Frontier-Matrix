# VERIFICATION_BACKLOG register

Indexes the corresponding `control_plane/*.yaml` register.

## Exact-head repository conformance baseline — 2026-08-12

**Status:** PROPOSED baseline; human review is pending.  
**Source proposal:** `KFM_Pass_20_Part_2_Idea_Index_Category_Atlas_and_Expansion_Dossier.md`, EXP-009.  
**Snapshot:** `main@753dfe4c4d17482c51bdf90ae8f8bb93e8644d3c`; recursive inventory contained **16,906 path entries**. The scan inspected repository paths and selected governing documents; it did not execute hosted CI, probe deployments, inspect branch protection, or assert runtime effectiveness.

| Category | CONFIRMED on the snapshot | PROPOSED convergence work | NEEDS VERIFICATION |
|---|---|---|---|
| **DOC** | `docs/` contains 2,085 path entries. `docs/doctrine/directory-rules.md` and adopting `docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md` are present. | Resolve the compatibility posture of `docs/architecture/directory-rules.md` and the naming parity between `OBJECT_FAMILY.md` and `OBJECT_FAMILY_MAP.md` through the existing governance process. | Confirm document-registry parity, metadata-block coverage, links, and steward acceptance; path presence alone is not semantic conformance. |
| **VAL** | `tools/validators/` contains 946 path entries and `tests/` contains 1,472. The generated-receipt schema, validator, and verification-backlog workflow are present. | Either project the open human-readable backlog into `control_plane/verification_backlog.yaml` or explicitly document why the views intentionally diverge. | Run exact-head hosted checks and measure validator coverage. The control-plane backlog currently has zero entries while this register has open items. |
| **REL** | `release/` contains 193 path entries; `contracts/release/` contains 29; and `schemas/contracts/v1/release/` contains 27. Promotion decisions, manifests, correction notices, withdrawal notices, and rollback cards have repository homes. | Reconcile any remaining duplicate object-family homes before introducing new release artifacts. | Verify current manifest integrity, signatures, rollback readiness, and deployment behavior. No publication or release-state change was performed by this scan. |
| **POL** | `policy/` contains 519 path entries, including `policy/promotion/`; policy contracts and schemas are present under their canonical responsibility roots. | Bind newly proposed policy behavior to existing contracts, fixtures, and finite outcomes instead of creating parallel policy homes. | Verify policy-bundle completeness, deny-path fixtures, request-time enforcement, and hosted CI outcomes. Structural presence does not prove effective enforcement. |

### Snapshot findings

- **CONFIRMED:** the repository has distinct documentation, contract, schema, policy, proof/receipt, and release responsibility roots.
- **CONFIRMED:** the human-readable and machine-readable verification backlog views are not currently in parity.
- **PROPOSED:** treat this section as the dated EXP-009 baseline and supersede it with a new exact-head section rather than rewriting historical observations.
- **NEEDS VERIFICATION:** semantic conformance, current deployment posture, protected-branch settings, runtime gate behavior, and steward approval.
- **UNKNOWN:** whether uninspected external services or unpublished branches contain additional implementation evidence.

### Non-effects

This baseline creates no schema, contract, policy rule, source activation, release, deployment, publication, or runtime authority. It records exact-head evidence for review and planning only.

- 2026-05-09: NEEDS VERIFICATION: domain-specific evidence_bundle duplicates should be migrated to $ref in follow-up PR.
- 2026-05-09: CONFIRMED PR-001 closes the local-resolver gap. Open: domain-specific schemas not yet on `$ref` form remain candidates for follow-up; runtime/UI/policy slices still UNKNOWN.


- 2026-05-09 — OPEN: Release manifest schema is intentionally permissive in PR-001; fields for signed manifests, layer manifests, and rollback linkage are PROPOSED for ADR-0023 follow-up.

- 2026-05-14 — OPEN: `docs/registers/CANONICAL_LINEAGE_EXPLORATORY.md` path and template exist as PROPOSED governance scaffold; first steward-reviewed entry and citation pattern are NEEDS VERIFICATION.
- 2026-05-15 — OPEN: `docs/doctrine/directory-rules.md` created as PROPOSED canonical-home stub; NEEDS VERIFICATION steward decision on authority cutover vs mirror pattern from `docs/doctrine/directory-rules.md`.
- 2026-05-15 — OPEN: `docs/registers/AUTHORITY_LADDER.md` and `docs/registers/OBJECT_FAMILY_MAP.md` created as PROPOSED naming-parity scaffolds; NEEDS VERIFICATION whether legacy `OBJECT_FAMILY.md` remains canonical, is superseded, or is maintained as compatibility mirror.

- 2026-05-15 — RESOLVED: Re-ran branch-local checks and attached evidence in `control_plane/normalized_summary_consumer_readiness.yaml`; consumer statuses restored to `validated` on 2026-05-16.

- 2026-05-15 — OPEN: Populate steward-approved authoritative `source_url` values in `control_plane/doctrine_artifact_provenance_sources.yaml` for each required doctrine artifact before provenance status may be promoted.

- 2026-05-15 — OPEN: Resolve canonical filename/path mapping for required doctrine artifacts and promote `control_plane/document_registry_doctrine_required.yaml` entries from `needs_verification` only after steward-approved path + provenance evidence is attached.

- 2026-05-15 — RESOLVED: Remediated parser compatibility for `needs_verification` status; `run_doctrine_artifact_preflight.py` no longer trips the prior check path and downstream consistency tests now pass.

- 2026-05-15 — RESOLVED: Reran `pytest -q tests/policy/test_preflight_summary_consistency.py` (5 passed) and promoted consumer readiness to `validated` with 2026-05-16 evidence timestamp.
- 2026-05-16 — OPEN (superseded by 2026-05-17 action split): Finalize canonical path + provenance mapping for doctrine inputs (atlas canonical form + naming decisions for `New Ideas 5-8-26` and `DomainDriven Design Reference`).
- 2026-05-17 — OPEN (superseded by steward-signoff action below): Canonicalization action set with three tracked decisions (atlas canonical form, plus authoritative naming decisions for `New Ideas 5-8-26` and `DomainDriven Design Reference`).
- 2026-05-17 — OPEN: Produce steward sign-off record that maps each current path variant to one canonical target name (`KFM_Domains_Culmination_Atlas_v1_1.pdf`, `New_Ideas_5-8-26.pdf`, `DomainDriven_Design_Reference.pdf`) and updates register/provenance entries atomically in the same change set.
