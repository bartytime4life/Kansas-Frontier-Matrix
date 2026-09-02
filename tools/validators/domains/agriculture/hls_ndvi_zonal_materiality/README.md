# HLS NDVI Zonal Materiality Validator

Validates one fixture-only `HlsNdviZonalMaterialityAssessment` against the closed Draft 2020-12 schema and deterministic source-change, signal-change, pixel-count, and valid-coverage rules.

```bash
python tools/validators/domains/agriculture/hls_ndvi_zonal_materiality/validate_hls_ndvi_zonal_materiality.py \
  fixtures/domains/agriculture/hls_ndvi_zonal_materiality/valid/material_change_candidate.json
```

Exit code `0` means the precomputed fixture is internally consistent. It does not search STAC, read rasters, decode masks, calculate NDVI, create a COG, issue an alert, or authorize promotion, release, or publication.
