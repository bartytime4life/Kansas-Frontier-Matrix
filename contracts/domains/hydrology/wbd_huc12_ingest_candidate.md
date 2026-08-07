<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/domains/hydrology/wbd-huc12-ingest-candidate
title: WBD HUC12 Source Package and Ingest Candidate Contract
type: contract
version: v1.0.0
status: implemented; fixture-first; no-network; non-publisher
owners: OWNER_TBD — Hydrology steward; USGS source steward; pipeline steward; validation steward; evidence steward
created: 2026-08-07
updated: 2026-08-07
policy_label: repository-facing; hydrology; source-admission; fixture-only; fail-closed
owning_root: contracts/
responsibility: Define the meaning and non-authority boundary of captured WBD HUC12 source packages and their deterministic ingest-candidate projection.
truth_posture: cite-or-abstain; implementation claims require current repository evidence
related:
  - ./wbd_huc12_material_change_assessment.md
  - ../../../schemas/contracts/v1/domains/hydrology/wbd_huc12_source_package.schema.json
  - ../../../schemas/contracts/v1/domains/hydrology/wbd_huc12_ingest_candidate.schema.json
  - ../../../pipelines/domains/hydrology/ingest_wbd_huc/README.md
  - ../../../pipeline_specs/hydrology/wbd_huc12_ingest.yaml
  - ../../../data/registry/hydrology/sources/wbd_huc12.yaml
  - ../../../docs/adr/ADR-0026-hydrology-source-spine-starts-with-wbd-huc12.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
notes:
  - "The source package contains already captured fixture bytes and request evidence; it never performs network access."
  - "The candidate producer emits a RAW_CANDIDATE or NO_CHANGE_RECEIPT projection but never writes lifecycle state."
  - "A RAW_CANDIDATE is source-admission input only and is not processed data, evidence closure, promotion, release, or publication."
[/KFM_META_BLOCK_V2] -->

# WBD HUC12 source package and ingest candidate

> **Purpose.** Turn one already captured, public-safe WBD HUC12 response into a deterministic source-admission candidate or a deterministic no-change receipt without fetching, activating, promoting, releasing, or publishing anything.

## Status and authority

| Surface | Status | Authority boundary |
|---|---|---|
| `WbdHuc12SourcePackage` | **CONFIRMED implemented schema and fixtures** | Captured request/response evidence only; no source activation or network behavior. |
| `WbdHuc12IngestCandidate` | **CONFIRMED implemented schema and producer** | Candidate/no-change projection only; no lifecycle write or promotion authority. |
| Material-change assessment | **CONFIRMED reused dependency** | Existing fixture-only geometry-plus-area assessment remains the decision engine. |
| Live WBD retrieval | **NOT IMPLEMENTED / DENIED here** | A future connector or manually governed probe owns retrieval and conditional request behavior. |
| RAW or QUARANTINE persistence | **NOT PERFORMED** | An orchestrator may act on the projection only after separate admission and policy checks. |

## Directory Rules basis

The object meanings belong under `contracts/domains/hydrology/`. Machine shapes belong under `schemas/contracts/v1/domains/hydrology/`. Executable transformation belongs under `pipelines/domains/hydrology/ingest_wbd_huc/`. Declarative orchestration belongs under `pipeline_specs/hydrology/`. Synthetic reusable inputs belong under `fixtures/`, executable conformance under `tests/`, and CI orchestration under `.github/workflows/`.

No new responsibility root or parallel source, schema, policy, receipt, proof, release, or publication authority is created.

## `WbdHuc12SourcePackage`

A source package is an immutable description of one captured request and response at one declared observation time. It binds:

- the accepted WBD HUC12 source descriptor reference;
- one 12-digit HUC code;
- an explicit HTTPS query URL, method, where clause, requested fields, HTTP status, ETag, Last-Modified value, and media type;
- either a canonical GeoJSON FeatureCollection plus its SHA-256 digest for HTTP `200`, or no body for HTTP `304`;
- an optional prior normalized feature snapshot; and
- non-authority declarations proving fixture-only, no-network, no-write behavior.

`spec_hash` is SHA-256 over the UTF-8 compact JSON object after removing `spec_hash` and sorting object keys.

## `WbdHuc12IngestCandidate`

The producer validates and projects a source package into exactly one finite disposition:

| Disposition | Meaning | Reason codes |
|---|---|---|
| `NO_CHANGE_RECEIPT` | The server declared `304`, or normalized geometry and six-decimal area remained unchanged despite source metadata churn. | `HTTP_NOT_MODIFIED`, `CONTENT_UNCHANGED` |
| `RAW_CANDIDATE` | The selected HUC12 was added, removed, or materially changed. | `FEATURE_ADDED`, `FEATURE_REMOVED`, `FEATURE_MATERIAL_CHANGE` |

A `RAW_CANDIDATE` identifies only an admissible next-step candidate. Its declared possible targets are bounded to the WBD HUC12 RAW and QUARANTINE lanes. The producer does not select a target and writes neither location.

## Deterministic checks

The implementation must fail closed on:

- invalid, oversized, non-UTF-8, duplicate-key, non-finite, symlink, or non-object JSON input;
- source-package schema failure or `spec_hash` mismatch;
- response body digest mismatch;
- a `304` response carrying body bytes or lacking a prior snapshot;
- a `200` response lacking a FeatureCollection;
- duplicate matching HUC12 records;
- invalid HUC identity, area, geometry, CRS bounds, fingerprint, or material-change decision;
- output-schema failure; or
- an unsafe output path or overwrite request.

Diagnostics contain stable codes and bounded paths. They do not echo source payload values.

## Non-effects

A passing run does **not** prove:

- current WBD endpoint behavior, cadence, ETag support, rights, or source activation;
- that captured bytes came from USGS or are authentic;
- EvidenceBundle, policy, catalog, review, release, correction, or rollback closure;
- that any candidate was written to RAW or QUARANTINE; or
- promotion, release, deployment, publication, public API, or map behavior.

## Commands

```bash
python pipelines/domains/hydrology/ingest_wbd_huc/produce_wbd_huc12_candidate.py \
  fixtures/domains/hydrology/wbd_huc12_ingest/valid/no_change.json

python -m pytest \
  tests/pipelines/domains/hydrology/test_wbd_huc12_ingest_candidate.py \
  tests/validators/domains/hydrology/wbd_huc12_material_change/test_validate_wbd_huc12_material_change.py \
  -q --strict-config --strict-markers
```

## Rollback

Close the draft pull request before merge, or revert the bounded implementation commit after merge. The change creates no source activation, credentials, external service, lifecycle records, proof objects, release records, cache, deployment, or public artifact.
