<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/source/eo-asset-prefilter-report
title: Earth-Observation Asset Prefilter Report
type: semantic-contract; source-edge-normalized-metadata-report
version: v0.1.0
status: draft; PROPOSED_INACTIVE; fixture-first; no-network; no-source-activation; no-release-authority
owners:
  - OWNER_TBD — Source steward
  - OWNER_TBD — Remote-sensing steward
  - OWNER_TBD — Validation steward
created: 2026-08-05
updated: 2026-08-05
policy_label: public-doc; source; earth-observation; prefilter; synthetic; no-network; review-only
related:
  - ../../docs/standards/STAC-EO.md
  - ../../schemas/contracts/v1/source/eo_asset_prefilter_profile.schema.json
  - ../../schemas/contracts/v1/source/eo_asset_prefilter_report.schema.json
  - ../../pipeline_specs/source/eo_asset_prefilter_profile.v1.json
  - ../../fixtures/contracts/v1/source/eo_asset_prefilter_report/
  - ../../tools/validators/source/validate_eo_asset_prefilter_report.py
  - ../../tests/validators/source/test_eo_asset_prefilter_report.py
notes:
  - "Derived from the New Ideas 5-19-26 county-scale STAC/ETag prefilter concept."
  - "The profile values are synthetic acceptance thresholds, not source, rights, policy, or publication decisions."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Earth-Observation Asset Prefilter Report

> Normalize already-retrieved STAC item and HTTP-validator facts into a deterministic,
> reviewable prefilter result without performing a network request or admitting source bytes.

## Goal

The source dossier proposes county-scale Earth-observation sweeps that first narrow STAC
items by collection, time, cloud cover, item count, valid-pixel fraction, cloud-mask role,
and replayable asset validators such as ETags. This contract creates the smallest reusable
source-edge object needed to make that prefilter testable before any NDVI calculation,
source activation, RAW admission, evidence closure, or release.

## Directory Rules basis

ADR-0029 adopts Directory Rules v2. The artifact has one authority owner per object:

| Responsibility | Home | Artifact |
|---|---|---|
| Source-edge semantic meaning | `contracts/source/` | This contract |
| Machine shape | `schemas/contracts/v1/source/` | Profile and report schemas |
| Declarative inactive thresholds | `pipeline_specs/source/` | Versioned profile instance |
| Synthetic examples | `fixtures/contracts/v1/source/` | Valid and exact-negative reports |
| Reusable validation | `tools/validators/source/` | Deterministic validator and CLI |
| Enforceability proof | `tests/validators/source/` | Unit and CLI tests |
| Orchestration | `.github/workflows/` | Read-only focused workflow |
| Authoring provenance | `data/receipts/generated/` | Generated receipt for this change |

No new root, source registry, policy home, evidence store, proof store, release home, or
published-data lane is created.

## Knowledge character

`EOAssetPrefilterReport` is **process memory over normalized metadata**. It may record:

- a governed county geography reference and deterministic query digest;
- source collection labels and an analysis window;
- item cloud cover, valid-pixel fraction, and reviewed mask role;
- sanitized item, asset, and evidence references;
- normalized strong/weak/missing ETag posture, Last-Modified fallback, byte length,
  response latency, and missing-asset state;
- reconciled counts and a finite `PASS`, `HOLD`, or `DENY` prefilter decision.

It does not contain source credentials, signed URLs, raw imagery, pixel arrays, exact private
field geometry, a source admission decision, an `EvidenceBundle`, policy approval, a
promotion decision, or release state.

## Inactive fixture profile

The committed profile is intentionally `PROPOSED_INACTIVE`:

| Requirement | Fixture value |
|---|---:|
| Minimum items found | 6 |
| Minimum assets per item | 1 |
| Minimum assets found | 6 |
| Minimum valid-pixel fraction | 0.60 |
| Maximum cloud cover | 30% |
| Replay validator | strong ETag or Last-Modified |

The report binds the exact profile ID, version, and spec hash. Changing thresholds requires a
new profile version and review; it does not silently change existing report interpretation.

## Finite decisions

Precedence is `DENY > HOLD > PASS`.

| Condition | Decision | Reason code |
|---|---|---|
| No items found | `DENY` | `NO_ITEMS_FOUND` |
| Any asset is missing | `DENY` | `ASSET_MISSING` |
| Item or asset sample is below the profile | `HOLD` | `INSUFFICIENT_ITEMS` / `INSUFFICIENT_ASSETS` |
| Too few items meet cloud, valid-pixel, asset-count, and replay requirements | `HOLD` | `INSUFFICIENT_USABLE_ITEMS` |
| A non-missing asset has neither a strong ETag nor Last-Modified | `HOLD` | `REPLAY_VALIDATOR_MISSING` |
| Every profile requirement is met | `PASS` | `PREFILTER_REQUIREMENTS_MET` |

`PASS` means only that the synthetic metadata packet is reproducibly adequate for the next
review stage. It is not source admission, evidence resolution, policy approval, promotion,
release, or publication.

## Determinism and privacy

- JSON is parsed as UTF-8 with duplicate keys and non-finite numbers denied.
- The report `spec_hash` is SHA-256 over canonical JSON with `spec_hash` removed.
- Collections, items, assets, reason codes, and evidence references are canonicalized and
  checked for sorted uniqueness where applicable.
- Full HTTP(S) URLs are not accepted in report references. This avoids leaking signed query
  parameters or credentials into fixtures, logs, receipts, and pull-request diffs.
- CLI output names files and finding paths but does not echo locators, ETags, evidence
  references, or source values.

## Trust boundary and non-effects

The validator:

- performs no network calls;
- activates no connector or source;
- writes no RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLETS, PUBLISHED,
  evidence, proof, receipt-instance, or release record;
- makes no statement that a STAC provider, collection, item, or asset is authoritative;
- makes no rights, sensitivity, geoprivacy, policy, public-use, release, or publication
  decision;
- emits no NDVI value, map layer, alert, recommendation, or AI answer.

All governance flags remain false and `release_ref` remains null.

## Validation

```bash
python -m unittest discover \
  --start-directory tests/validators/source \
  --pattern 'test_eo_asset_prefilter_report.py' \
  --verbose

python tools/validators/source/validate_eo_asset_prefilter_report.py --fixtures

python tools/validators/validate_generated_receipt.py \
  data/receipts/generated/genrec-eo-asset-prefilter-report-20260805.json
```

A green result proves only local schema shape, profile binding, fixture polarity, count
reconciliation, deterministic decisions, hashing, safe parsing, and non-echoing output.

## Rollback

Before merge, close the draft pull request and delete the feature branch. After an authorized
merge, revert the single feature commit. No source activation, lifecycle admission, public
artifact, release record, deployment, or publication requires restoration.

<p align="right"><a href="#top">Back to top</a></p>
