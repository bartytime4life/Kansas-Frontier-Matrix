# Hydrology File System Plan

## Documentation home
- `docs/domains/hydrology/` for lane orientation and operating guidance.

## Machine artifact homes (proposed)
- `schemas/contracts/v1/hydrology/`
- `data/registry/hydrology/`
- `data/raw|work|quarantine|processed|published/hydrology/`
- `data/catalog/{stac,dcat,prov}/hydrology/`
- `data/proofs/hydrology/`
- `tools/validators/hydrology/`
- `tests/fixtures/hydrology/`

## Rule
Do not split authoritative contracts across both `contracts/` and `schemas/contracts/v1/` once ADR-0001 is resolved.
