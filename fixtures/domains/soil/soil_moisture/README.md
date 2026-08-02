# Synthetic station soil-moisture fixtures

This lane contains the frozen, no-network fixture profile exercised by
`tools/validators/domains/soil/moisture/validate_soil_moisture.py`.

The profile proves only bounded parsing and deterministic checks for synthetic
station observations: source and evidence references, the repository-native
`fixture_only` source role, generalized county support, VWC units, non-negative
depth, canonical UTC time with the source timezone preserved, source QC flags,
the `(station_id, measure, depth_cm, timestamp_iso)` deduplication tuple, and
fixture-only governance state.

It does not define the full `SoilMoistureObservation` schema, admit Kansas
Mesonet or another source, resolve references, assess scientific fitness,
normalize provider data, decide staleness, produce evidence or receipts,
promote lifecycle state, or authorize release or publication.

The `valid/` and `invalid/` inventories are closed by
`tests/domains/soil/test_soil_moisture_qc.py`. Every invalid JSON fixture has a
tab-separated `.expected_error.txt` sidecar containing exact sorted
`CODE<TAB>JSON_PATH` findings.

The shared fixture profile digest is the SHA-256 of the UTF-8 string
`kfm-soil-moisture-station-fixture-v1`:

```text
sha256:a66686f8783156849eb5c0a2cc26fb03a5e0cfcd7283fcc35047088b12cbd8f1
```
