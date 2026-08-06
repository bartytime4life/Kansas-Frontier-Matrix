# CSV-to-GeoJSON fixture preflight

## Status

**PROPOSED fixture-only implementation.** This lane is a deterministic `tools/ingest/` support helper. It is not a connector, pipeline of record, source registry, lifecycle writer, policy engine, evidence authority, release system, or public map builder.

## Use

```bash
PYTHONPATH=packages/hashing/src \
  python tools/ingest/csv_geojson_preflight/preflight.py \
  --profile fixtures/ingest/csv_geojson_preflight/profile.json \
  --csv fixtures/ingest/csv_geojson_preflight/valid.csv \
  --output /tmp/csv-geojson-candidate.json
```

The command refuses to overwrite an existing output. Valid input emits a deterministic review candidate and exit code `0`. A bounded input problem emits a value-minimized `QUARANTINE_CANDIDATE` report to stdout and exit code `2`. An unexpected operational failure emits `ERROR` and exit code `1`.

## Trust boundary

The helper:

- accepts regular, non-symlink profile and CSV files;
- reads at most 128 KiB of profile JSON and 1 MiB of CSV;
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
