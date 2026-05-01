# KFM Meta Block v2
- Domain: fauna
- Slice: GBIF occurrence ingestion
- Lifecycle: RAW -> WORK/QUARANTINE -> PROCESSED -> CATALOG/TRIPLET -> PUBLISHED
- Status: implementation slice

## Purpose
Fixture-backed GBIF occurrence normalization builds governed EvidenceBundle outputs with fail-closed rights/sensitivity posture.

## Lifecycle placement
Normalization reads RAW fixture CSV records and emits WORK/QUARANTINE-ready EvidenceBundle artifacts. Promotion remains a governed policy transition.

## Field mapping
| Darwin Core/GBIF | KFM field |
|---|---|
| eventDate | occurrenceDate |
| decimalLatitude + decimalLongitude | geopoint |
| datasetKey | kfm:dataset_key |
| basisOfRecord | basisOfRecord |
| coordinateUncertaintyInMeters | geospatialPrecision |
| individualCount | abundance |

## No-network testing posture
All tests use `tests/fixtures/fauna/gbif/*`. Live GBIF calls are intentionally not used.

## License rules
- Public candidate licenses: CC0, CC-BY
- CC-BY-NC: restricted unless explicit override flag is set
- Unknown/missing license: QUARANTINE/fail closed

## Geoprivacy rules
- Public exact sensitive coordinates are denied.
- Public mode rounds coordinates and emits geoprivacy receipt metadata.
- Public aggregate suppression threshold defaults to `n >= 10`.

## CLI example
```bash
python tools/normalizers/fauna/kfm_gbif_normalize.py \
  --input tests/fixtures/fauna/gbif/valid/simple_occurrences.csv \
  --query-predicate tests/fixtures/fauna/gbif/query_predicate.json \
  --download-key TEST_DOWNLOAD_KEY \
  --output /tmp/gbif_evidencebundle.json
```

## Validator/policy gates
- `tools/validators/fauna/gbif_evidencebundle_validator.py` validates schema.
- `policy/fauna/gbif_publication.rego` denies unsafe public publication postures.

## Known limitations
- Species truth is not asserted; records are treated as unreviewed occurrence claims.
- TODO/NEEDS_VERIFICATION: confirm final schema-home convention for fauna GBIF schemas.

## Promotion checklist
- EvidenceBundle present and schema-valid.
- `kfm:spec_hash` present and deterministic.
- rights/sensitivity/geoprivacy checks pass.
- no exact sensitive coordinates in public outputs.
