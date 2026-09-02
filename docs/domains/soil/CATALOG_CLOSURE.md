# Soil catalog closure

**Status:** PROPOSED / repository-grounded status surface.  
**Authority:** informational; not a catalog, release, or publication decision.

The Soil lane is **not catalog-closed** at this repository snapshot. The domain README explicitly records that no complete ingestion path, catalog closure, proof-bearing release, or published Soil product has been established.

## Closure dimensions

A candidate is `READY_FOR_REVIEW` only when the fixture-only `CatalogClosureAssessment` declares all of these dimensions satisfied: semantic contract, schema, source descriptor, support-type profile, deterministic identity, EvidenceBundle, validation report, rights decision, sensitivity decision, correction target, and rollback target.

Any unresolved or denied dimension yields `HOLD`. This status does not write CATALOG/TRIPLET state and does not authorize promotion, release, deployment, publication, or public use.

## Current bounded implementation

The executable assessment profile is defined in `contracts/domains/soil/catalog_closure_assessment.md`, shaped by `schemas/contracts/v1/domains/soil/catalog_closure_assessment.schema.json`, and exercised only against synthetic fixtures by the repository validator and focused tests.

This file should be updated when a real Soil candidate is independently verified through the governed lifecycle. Until then, catalog closure remains unclaimed.
