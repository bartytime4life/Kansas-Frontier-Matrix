# USGS Water API Cutover Assessment Validator

Validates one fixture-only `UsgsWaterApiCutoverAssessment` against the closed Draft 2020-12 schema and deterministic migration rules.

```bash
python tools/validators/domains/hydrology/usgs_water_api_cutover/validate_usgs_water_api_cutover.py \
  fixtures/domains/hydrology/usgs_water_api_cutover/valid/cutover_candidate.json
```

Exit code `0` means the fixture is internally consistent. It does not verify live USGS services, activate a connector, rewrite production clients, admit source data, or authorize promotion, release, or publication.
