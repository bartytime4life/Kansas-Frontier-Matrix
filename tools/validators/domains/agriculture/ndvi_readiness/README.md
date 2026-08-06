# NDVI Readiness Sidecar Validator

Validates one fixture-only `NdviReadinessAssessment` JSON document against the Draft 2020-12 schema and deterministic cross-field rules.

```bash
python tools/validators/domains/agriculture/ndvi_readiness/validate_ndvi_readiness.py \
  fixtures/domains/agriculture/ndvi_readiness/valid/emit_candidate.json
```

Exit code `0` means the sidecar is structurally and semantically self-consistent. It does not authorize emission, promotion, release, publication, health guidance, or source activation.
