# Synthetic soil-moisture fixtures

This lane contains two separate frozen, no-network fixture profiles:

- the station profile in `valid/` and `invalid/`, exercised by
  `tools/validators/domains/soil/moisture/validate_soil_moisture.py`; and
- the profile-local SMAP L4 anti-collapse envelope in `smap_l4/`, exercised by
  `tools/validators/domains/soil/moisture/validate_smap_l4_fixture.py`.

The station profile proves bounded parsing and deterministic validation for
synthetic station readings, including explicit source and support type,
generalized county support, volumetric water content in `m3/m3`, non-negative
depth with units, canonical UTC timestamps with the source timezone preserved,
source QC flags, the
`(station_id, measure, depth_cm, timestamp_iso)` deduplication tuple, and
fixture-only governance state.

The SMAP L4 profile separately proves that modeled surface and root-zone grid
candidates retain product, cadence, QA, uncertainty, grid, assimilation,
evidence, receipt, and non-release posture. It rejects raw-observation,
station, field-truth, in-situ-merge, surface/root-zone, cadence, promotion, and
release collapse. Its vocabulary is local to the fixture profile and is not a
canonical schema or source descriptor.

Neither profile admits a live source, resolves references, assesses scientific
fitness, normalizes provider data, decides staleness, creates evidence or
receipts, promotes lifecycle state, or authorizes release or publication.

The station `valid/` and `invalid/` inventories are closed by
`tests/domains/soil/test_soil_moisture_qc.py`. The `smap_l4/valid/` and
`smap_l4/invalid/` inventories are closed by
`tests/domains/soil/test_smap_l4_anti_collapse.py`. Every invalid JSON fixture
has a tab-separated `.expected_error.txt` sidecar containing exact sorted
`CODE<TAB>JSON_PATH` findings.

The station fixture profile digest is the SHA-256 of the UTF-8 string
`kfm-soil-moisture-station-fixture-v1`:

```text
sha256:a66686f8783156849eb5c0a2cc26fb03a5e0cfcd7283fcc35047088b12cbd8f1
```

