<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/source/csv-geojson-normalization-candidate
title: CSV-to-GeoJSON Normalization Candidate Contract
type: semantic-contract; fixture-only-preflight
version: v0.1.0
status: proposed
owners: OWNER_TBD — Source steward · Ingest tooling steward · Spatial validation steward
created: 2026-08-06
updated: 2026-08-06
policy_label: public; source-intake; synthetic-fixture; non-authoritative; no-publication
related:
  - ./source_event_envelope.md
  - ./source_descriptor.md
  - ./ingest_receipt.md
  - ../../schemas/contracts/v1/source/csv_geojson_normalization_candidate.schema.json
  - ../../tools/ingest/csv_geojson_preflight/README.md
  - ../../docs/intake/exploratory/new-ideas-3-11-26-source-event-envelope-source-map.md
tags: [kfm, csv, geojson, normalization, preflight, fixture-only, deterministic, no-network]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# CSV-to-GeoJSON Normalization Candidate Contract

> A `CsvGeojsonNormalizationCandidate` is a deterministic, fixture-only review artifact produced from an explicitly mapped CSV file. It is not a source capture of record, a SourceArtifact, an IngestReceipt, an EvidenceBundle, a PolicyDecision, a lifecycle transition, a released layer, or a publication decision.

## Purpose

This contract implements the smallest source-derived follow-up identified by the repository's `New Ideas 3-11-26` source map: a governed CSV-to-GeoJSON normalization runner that reuses the existing source-event identity and hashing boundaries while remaining synthetic, no-network, non-publishing, and reversible.

The candidate proves only that a bounded CSV file can be parsed and represented as deterministic GeoJSON points under one explicit fixture profile. The result is suitable for reviewer inspection and downstream test development. It cannot be cited as public geographic truth.

## Required semantics

| Surface | Required behavior |
|---|---|
| Profile | Exact field mapping, header order, coordinate precision, row budget, source-event reference, source-descriptor reference, source role, and fixture-only geometry policy. |
| Input | Strict UTF-8 CSV, exact headers, bounded bytes and rows, no duplicate headers, no duplicate row identifiers, and no formula-like property cells. |
| Geometry | GeoJSON `Point` only; longitude then latitude; finite WGS84-style numeric bounds; deterministic rounding; synthetic public-safe fixtures only. |
| Identity | Stable feature identity from profile identity, source-descriptor reference, and source row ID. Candidate and feature-collection hashes use the repository hashing package. |
| Output | Features sorted by source row ID; properties restricted to the allowlisted profile fields; deterministic JSON candidate. |
| Failure | Invalid profile, encoding, headers, rows, identifiers, coordinates, or property values fail closed with a value-minimized reason code. No partial feature collection is emitted. |
| Authority | Every authority, evidence, policy, lifecycle, release, source-activation, network, and publication flag is fixed to a non-authoritative value. |

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `NORMALIZED_CANDIDATE` | Every admitted row was normalized into a deterministic fixture-only GeoJSON candidate. |
| `QUARANTINE_CANDIDATE` | A bounded input or profile problem requires review. The preflight emits no feature collection. |
| `ERROR` | An unexpected operational failure prevented safe completion. The diagnostic remains non-secret and non-authoritative. |

`NO_ACTION` is intentionally absent from v0.1. Empty input is not a successful no-op because a CSV normalization request without data cannot prove the intended mapping.

## Non-effects

The candidate and its tool do not:

- fetch a source or access a network;
- activate or edit a `SourceDescriptor`;
- write RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED state;
- mint a `SourceArtifact`, `IngestReceipt`, `EvidenceRef`, `EvidenceBundle`, proof, policy decision, review approval, or release object;
- generalize, redact, or approve real sensitive geometry;
- create a MapLibre source, tile, PMTiles archive, governed API route, or public layer;
- authorize downstream use merely because schema validation or hashes pass.

## Directory Rules basis

Accepted ADR-0029 adopts Directory Rules v2. This slice uses existing responsibility roots:

| Responsibility | Home |
|---|---|
| Semantic meaning | `contracts/source/` |
| Machine shape | `schemas/contracts/v1/source/` |
| Dry-run support implementation | `tools/ingest/csv_geojson_preflight/` |
| Synthetic input fixtures | `fixtures/ingest/csv_geojson_preflight/` |
| Executable proof | `tests/ingest/csv_geojson_preflight/` |
| CI orchestration | `.github/workflows/` |
| Exploratory source adaptation | `docs/intake/exploratory/` |
| AI authoring provenance | `data/receipts/generated/` |

No new root, source registry, lifecycle lane, policy home, receipt authority, proof store, release home, or public route is created.

## Validation

A conforming implementation must prove:

- deterministic repeated output from the same profile and bytes;
- source-event and source-descriptor reference preservation;
- exact header and mapping enforcement;
- coordinate order, range, precision, and finite-number enforcement;
- duplicate identifier denial;
- formula-like property denial;
- stable feature ordering and feature identity;
- schema validation of valid candidates;
- no candidate file on a quarantine result;
- no network or lifecycle dependency in the implementation; and
- fixed non-authority flags.

## Rollback

Before merge, close the draft pull request and abandon the branch. After a future merge, revert the bounded implementation commit. No source, external object, lifecycle record, public geometry, release, deployment, or publication requires cleanup.

[Back to top](#top)
