# KFM SourceDescriptor v1 bundle

Status: **PROPOSED implementation artifact** generated outside a mounted KFM repository.

This bundle provides the first source-admission contract for Kansas Frontier Matrix:

- `schemas/contracts/v1/sources/source_descriptor.schema.json`
- `data/registry/sources/source_type_registry.v1.yaml`
- valid and invalid no-network fixtures under `tests/fixtures/sources/source_descriptor/`
- a small validator utility under `tools/validators/sources/`
- a pytest smoke test under `tests/sources/`

## Directory Rules basis

The schema is placed under `schemas/contracts/v1/sources/` because it is field-level machine shape. The companion registry is placed under `data/registry/sources/` because it records source role/type vocabulary rather than executable schema. In a real checkout, verify current ADRs and root READMEs before landing.

## Validate locally

```bash
python tools/validators/sources/validate_source_descriptor.py   --schema schemas/contracts/v1/sources/source_descriptor.schema.json   tests/fixtures/sources/source_descriptor/valid/minimal.valid.json

pytest tests/sources/test_source_descriptor_schema.py
```

Invalid fixtures intentionally fail and should remain negative coverage.

## Governance boundary

A `SourceDescriptor` records how a source may be treated. It does not make a source's claims true, does not publish anything, and does not replace EvidenceBundle, PolicyDecision, ReleaseManifest, or PromotionDecision.
