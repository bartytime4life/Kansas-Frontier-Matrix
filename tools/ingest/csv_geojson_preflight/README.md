# CSV-to-GeoJSON fixture preflight

## Status

**PROPOSED fixture-only implementation.** This lane is a deterministic `tools/ingest/` support helper. It is not a connector, pipeline of record, source registry, lifecycle writer, policy engine, evidence authority, release system, or public map builder.

## Use

```bash
csv_candidate_dir="$(mktemp -d)" && PYTHONPATH=packages/hashing/src \
  python tools/ingest/csv_geojson_preflight/preflight.py \
  --profile fixtures/ingest/csv_geojson_preflight/profile.json \
  --csv fixtures/ingest/csv_geojson_preflight/valid.csv \
  --output "$csv_candidate_dir/csv-geojson-candidate.json"
```

Run from the repository root on a Linux PC with the repository Python dependencies
installed (`rfc8785==0.1.4` is the only external dependency used by this command).
The command runs offline using three bundled synthetic points and writes a
review candidate into a new private temporary directory. The final JSON summary
reports its path. Inspect it locally; remove that directory when finished. No
real dataset download, source admission, map layer activation, or public use is
implied. General offline release installation and rendering remain separately
governed by the [offline release capsule assessment](../../../contracts/runtime/offline_release_capsule_assessment.md).

The command refuses to overwrite an existing output. Valid input emits a deterministic review candidate and exit code `0`. A bounded input problem emits a value-minimized `QUARANTINE_CANDIDATE` report to stdout and exit code `2`. An unexpected operational failure emits `ERROR` and exit code `1`.

## Trust boundary

The helper:

- accepts regular, non-symlink profile and CSV files;
- admits at most 128,000 bytes of profile JSON and 1,000,000 bytes of CSV (the file reader reads one extra byte to detect an oversized input); the direct `normalize_csv` entrypoint enforces the same CSV limit before decoding or parsing;
- rejects booleans as coordinate-precision or row-count integers and quarantines malformed data rows with the finite `CSV_PARSE_ERROR` reason;
- admits only the `FIXTURE_ONLY` execution mode and `PUBLIC_SAFE_SYNTHETIC_POINTS` geometry policy;
- performs no network request;
- emits no partial feature collection;
- creates no source, evidence, policy, lifecycle, release, or publication authority; and
- writes only the caller-selected candidate path after complete validation.

A successful candidate is not a SourceArtifact, IngestReceipt, EvidenceBundle, released layer, or public-safe approval for real coordinates.

## Validation

```bash
python -m pytest \
  tests/ingest/csv_geojson_preflight \
  -q --strict-config --strict-markers
```

## Rollback

Revert the bounded feature commit. The helper creates no external or governed lifecycle state.
