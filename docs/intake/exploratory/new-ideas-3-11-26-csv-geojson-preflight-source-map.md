# New Ideas 3-11-26 — CSV-to-GeoJSON preflight adaptation

## Status

- **Source:** `New Ideas 3-11-26.pdf`
- **Repository assay base:** `main@3ef64eca521d18f8df04014d768219e8dba36150`
- **Selected increment:** fixture-only CSV-to-GeoJSON normalization preflight
- **Implementation status:** `PROPOSED` until reviewed and merged
- **Network, source activation, lifecycle, release, and publication effects:** none

## Evidence-led selection

The prior source-event adaptation explicitly named a fixture-only CSV-to-GeoJSON normalization runner as the next implementation cursor. Current repository evidence now contains the source-event identity profile, RFC 8785 plus SHA-256 hashing package, source contracts, synthetic fixture conventions, `tools/ingest/` support boundary, and no-network workflow patterns needed to close that increment.

The repository still did not expose an executable CSV-to-GeoJSON preflight at the inspected base. This change therefore implements the named gap without introducing a live connector, shared pipeline writer, source activation, or public geometry.

## Source adaptation

| Packet proposal | Repository adaptation |
|---|---|
| Convert CSV rows into GeoJSON. | Convert only exact-profile synthetic fixture rows into a deterministic review candidate. |
| Use deterministic identity. | Bind profile, source-event reference, source-descriptor reference, row identity, input digest, feature digest, and candidate `spec_hash`. |
| Stage output for PR review. | Write only a caller-selected review path after complete validation; never a lifecycle or public path. |
| Fail closed on validation. | Deny partial output for header, encoding, identifier, coordinate, formula-like cell, size, or row-limit failures. |
| Keep provenance with the artifact. | Preserve source-event and source-descriptor references plus input/header/output hashes. The candidate is not an authoritative receipt. |

## Directory Rules basis

Accepted ADR-0029 makes Directory Rules v2 effective. The primary executable responsibility is a durable, read-only/dry-run ingest-support helper, so implementation lives under `tools/ingest/csv_geojson_preflight/`. Meaning, shape, fixtures, tests, workflow, source adaptation, and authoring provenance remain in their existing responsibility roots.

This change does not create a new root, source registry, pipeline authority, lifecycle writer, policy home, receipt authority, proof store, release home, API route, or map layer.

## Deferred candidates

- source-specific profiles backed by reviewed SourceDescriptors;
- real geometry sensitivity/generalization policy;
- SourceArtifact and IngestReceipt handoff;
- connector or domain-pipeline invocation;
- live network or object-store input;
- RAW or QUARANTINE write ownership;
- MapLibre, PMTiles, catalog, release, or public API consumption.

Each deferred item requires a separate repository assay, explicit authority boundary, tests, and rollback.

## Rollback

Close the draft pull request before merge or revert the bounded implementation after merge. No external state or public artifact is created.
