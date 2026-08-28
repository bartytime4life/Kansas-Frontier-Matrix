<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-hydrology-ingest-wbd-huc-readme
title: Hydrology WBD HUC Ingest Pipeline README
type: readme
version: v0.2
status: implemented; fixture-first; no-network; non-publisher
owners: OWNER_TBD — Hydrology pipeline owner; Hydrology domain steward; USGS source steward; validation steward
created: 2026-06-13
updated: 2026-08-07
policy_label: repository-facing; hydrology; source-admission; fixture-only; no-public-path
owning_root: pipelines/
responsibility: Own executable transformation of already captured WBD HUC12 source packages into deterministic source-admission candidate projections without fetching, persisting lifecycle data, or publishing.
truth_posture: cite-or-abstain; implementation claims require current repository evidence
related:
  - ../../../../contracts/domains/hydrology/wbd_huc12_ingest_candidate.md
  - ../../../../contracts/domains/hydrology/wbd_huc12_material_change_assessment.md
  - ../../../../schemas/contracts/v1/domains/hydrology/wbd_huc12_source_package.schema.json
  - ../../../../schemas/contracts/v1/domains/hydrology/wbd_huc12_ingest_candidate.schema.json
  - ../../../../pipeline_specs/hydrology/wbd_huc12_ingest.yaml
  - ../../../../data/registry/hydrology/sources/wbd_huc12.yaml
  - ../../../../fixtures/domains/hydrology/wbd_huc12_ingest/
  - ../../../../tests/pipelines/domains/hydrology/test_wbd_huc12_ingest_candidate.py
  - ../../../../docs/adr/ADR-0026-hydrology-source-spine-starts-with-wbd-huc12.md
  - ../../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
notes:
  - "v0.2 replaces the prior implementation-plan-only README with current bounded executable evidence."
  - "The producer consumes captured packages only; connectors own retrieval and conditional requests."
  - "The output is a projection. It never writes RAW, QUARANTINE, PROCESSED, CATALOG, TRIPLET, PUBLISHED, receipt, proof, or release state."
[/KFM_META_BLOCK_V2] -->

# USGS WBD HUC12 fixture-first ingest candidate

> **One-line purpose.** Validate one already captured HUC12 response, reuse the existing deterministic material-change engine, and emit either a `RAW_CANDIDATE` or `NO_CHANGE_RECEIPT` projection without network access or lifecycle writes.

## Current implementation

| File or surface | Current state |
|---|---|
| `produce_wbd_huc12_candidate.py` | **CONFIRMED executable**; reads one bounded source-package JSON object and emits compact deterministic JSON. |
| Source-package and candidate schemas | **CONFIRMED machine shapes** under the canonical schema root. |
| Material-change validator | **CONFIRMED reused dependency**; geometry canonicalization and geometry-plus-area fingerprints remain centralized. |
| Fixture matrix | **CONFIRMED synthetic/public-safe**; metadata churn, material geometry change, add, remove, HTTP 304, and duplicate-HUC failure. |
| Focused tests | **CONFIRMED executable**; deterministic output, digest binding, finite dispositions, no overwrite, and failure polarity. |
| Workflow | **CONFIRMED read-only orchestration**; installs declared test dependencies and runs no-network checks. |
| Live retrieval, activation, persistence, promotion, publication | **NOT IMPLEMENTED / not authorized here**. |

## Responsibility boundary

This lane owns the **how** of transforming already captured WBD HUC12 bytes into a bounded candidate projection. It does not own:

- network retrieval, credentials, conditional request state, or source activation (`connectors/` or a governed manual probe);
- source identity and activation (`data/registry/`);
- semantic meaning (`contracts/`), machine shape (`schemas/`), or allow/deny policy (`policy/`);
- lifecycle instances (`data/`), proofs, catalogs, review, release, correction, or rollback;
- public API, map, Focus Mode, or AI behavior.

WBD polygons remain administrative hydrography context. They are not observed streamflow, modeled network topology, flood regulation, watershed condition, or jurisdictional boundary proof.

## Flow

```text
captured WbdHuc12SourcePackage fixture
  -> schema + spec_hash + response-digest checks
  -> one exact HUC12 selection
  -> normalized geometry-plus-area fingerprint
  -> existing WbdHuc12MaterialChangeAssessment
  -> RAW_CANDIDATE or NO_CHANGE_RECEIPT projection
  -> no lifecycle write
```

## Finite outcomes

- `NO_CHANGE_RECEIPT / HTTP_NOT_MODIFIED`
- `NO_CHANGE_RECEIPT / CONTENT_UNCHANGED`
- `RAW_CANDIDATE / FEATURE_ADDED`
- `RAW_CANDIDATE / FEATURE_REMOVED`
- `RAW_CANDIDATE / FEATURE_MATERIAL_CHANGE`
- nonzero exit with stable findings for malformed or contradictory inputs

## Commands

```bash
python pipelines/domains/hydrology/ingest_wbd_huc/produce_wbd_huc12_candidate.py \
  fixtures/domains/hydrology/wbd_huc12_ingest/valid/no_change.json

python -m pytest \
  tests/pipelines/domains/hydrology/test_wbd_huc12_ingest_candidate.py \
  tests/validators/domains/hydrology/wbd_huc12_material_change/test_validate_wbd_huc12_material_change.py \
  -q --strict-config --strict-markers
```

## Trust boundary

A successful run proves only deterministic validation and projection over the supplied bytes. It does not authenticate USGS, resolve EvidenceBundle support, evaluate policy, persist a candidate, or authorize promotion, release, deployment, publication, or public use.

## Rollback

Revert the bounded implementation commit. No external service, source activation, lifecycle mutation, release state, deployment, or public artifact must be unwound.
