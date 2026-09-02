# Soil catalog-closure assessment source map

Status: PROPOSED / implementation adaptation.

## Current repository evidence

At the branch base, the Soil README explicitly states that no complete ingestion path, catalog closure, proof-bearing release, or published Soil product is established. It also reports substantial but partial Soil documentation, contract, schema, registry, policy, pipeline, package, UI, validator, and test surfaces.

The current Soil `DEFINITION_OF_DONE.md` is still a PROPOSED scaffold, while `EXPANSION_BACKLOG.md` and `CHANGELOG.md` are greenfield placeholders. Earlier companion-document names such as `SOURCE_BURDEN.md`, `SUPPORT_TYPES.md`, `LAYER_GUIDE.md`, and `OPEN_VERIFICATION.md` are not present at the current base and are not recreated here because current canonical documentation uses other names and responsibilities.

## Adaptation

This slice converts the remaining phrase “catalog closure” into an inspectable, fixture-only assessment instead of claiming the catalog is complete. The eleven closure dimensions are intentionally cross-root references. A passing assessment means only `READY_FOR_REVIEW`; it never writes CATALOG/TRIPLET or release state.

## Directory Rules basis

Soil semantic meaning remains under `contracts/domains/soil/`; machine shape under `schemas/contracts/v1/domains/soil/`; replay fixtures under `fixtures/contracts/v1/domains/soil/`; validators under `tools/validators/domains/soil/`; tests under `tests/validators/domains/soil/`; CI under `.github/workflows/`; and this non-authoritative adaptation note under `docs/intake/exploratory/`.
