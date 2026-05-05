# Archaeology Architecture

This document defines the architecture boundary for the archaeology lane.

## Layering

1. **Source edge**: admitted source descriptors only.
2. **Lifecycle stores**: RAW/WORK/QUARANTINE/PROCESSED/CATALOG/PUBLISHED.
3. **Governance**: policy checks, sensitivity checks, rights checks, promotion checks.
4. **Serving**: governed API DTOs only.
5. **Experience**: MapLibre, Evidence Drawer, Focus Mode, Story/exports.

## Non-negotiable constraints

- Public exact site geometry is denied by default.
- Derived products (tiles, summaries, vectors, search) are not canonical truth.
- EvidenceRef must resolve to an EvidenceBundle for consequential claims.
- Promotion must emit release/proof artifacts and rollback references.

## Required companion docs

- `DOMAIN_MODEL.md`
- `SOURCE_REGISTRY.md`
- `SENSITIVITY_AND_RIGHTS.md`
- `VALIDATION_AND_POLICY.md`
- `CATALOG_AND_PROOF_OBJECTS.md`
- `API_AND_UI_SURFACES.md`
- `DATA_LIFECYCLE.md`
- `PROMOTION_AND_ROLLBACK.md`
- `RUNBOOK.md`
