<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/source/stac-asset-head-prefilter
title: STAC Asset HEAD Prefilter Profile
type: semantic-contract; source-event-profile; pre-raw
version: v0.1.0
status: draft; PROPOSED; fixture-first; no-network; non-operational
owners: OWNER_TBD — Source steward · Catalog steward · Contract steward · Schema steward · Validation steward
created: 2026-08-08
updated: 2026-08-08
policy_label: internal; source-edge; stac; http-head; fixture-only; no-authority
related:
  - ./source_event_envelope.md
  - ./web_delta_profile.md
  - ../../schemas/contracts/v1/source/stac_asset_head_prefilter.schema.json
  - ../../fixtures/contracts/v1/source/stac_asset_head_prefilter/cases.json
  - ../../tools/validators/validate_stac_asset_head_prefilter.py
  - ../../tests/validators/test_validate_stac_asset_head_prefilter.py
  - ../../docs/intake/exploratory/pass-32-stac-head-prefilter-source-map.md
tags: [kfm, stac, asset, http-head, etag, last-modified, prefilter, deterministic, fixture-first]
notes:
  - "Implements the bounded no-network contract-and-validator slice of Pass 32 card KFM-P32-PROG-0004."
  - "Reuses SourceEventEnvelopeCandidate and the already-known asset state rather than creating a parallel event or source authority."
  - "Operational STAC search, network HEAD requests, downloads, source activation, and lifecycle writes remain outside this slice."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# STAC Asset HEAD Prefilter Profile

> A closed, fixture-only profile for deterministically classifying recorded HTTP `HEAD` metadata for an already-known STAC asset before any later download is considered.

## Status and authority boundary

| Field | Value |
|---|---|
| Source card | `KFM-P32-PROG-0004` |
| Contract state | `PROPOSED` / fixture-first / no-network |
| Owning semantic lane | `contracts/source/` |
| Base object | `SourceEventEnvelopeCandidate` |
| Machine profile | `schemas/contracts/v1/source/stac_asset_head_prefilter.schema.json` |
| Execution mode | Fixed to `FIXTURE_ONLY` |
| Network request or asset download | Not performed |
| Source activation, lifecycle write, release, publication | Denied |

Pass 32 proposes querying STAC, issuing `HEAD` against candidate assets, and retaining `ETag` and `Last-Modified` values before downloads. This change implements only the dependency-closed deterministic decision surface over recorded synthetic metadata. It does not implement a live STAC client or network adapter.

The profile is intentionally restricted to **refresh checks for an already-known asset**. The base envelope therefore binds the prior admitted content digest, byte count, `ETag`, and `Last-Modified` state. First-time discovery without a prior asset state remains outside this profile and must not be silently treated as admission evidence.

## Directory Rules basis

Accepted ADR-0029 routes each artifact by the responsibility that owns it:

| Responsibility | Home |
|---|---|
| Human-readable source-profile meaning | `contracts/source/stac_asset_head_prefilter.md` |
| Machine shape | `schemas/contracts/v1/source/stac_asset_head_prefilter.schema.json` |
| Synthetic conformance records | `fixtures/contracts/v1/source/stac_asset_head_prefilter/cases.json` |
| Deterministic validation | `tools/validators/validate_stac_asset_head_prefilter.py` |
| Enforceability proof | `tests/validators/test_validate_stac_asset_head_prefilter.py` |
| Hosted orchestration | `.github/workflows/source-stac-head-prefilter.yml` |
| Source adaptation record | `docs/intake/exploratory/pass-32-stac-head-prefilter-source-map.md` |
| AI authoring provenance | `data/receipts/generated/genrec-source-stac-head-prefilter-20260808.json` |

No new root or parallel source, schema, policy, receipt, proof, catalog, release, or publication authority is created.

## Base-object reuse

```text
Previously admitted STAC asset state
  -> recorded synthetic HEAD observation
  -> SourceEventEnvelopeCandidate
       -> payload.attributes validated as kfm.stac_asset_head_prefilter.v1
       -> UNCHANGED | CHANGED | UNAVAILABLE | DENY | ERROR
       -> NO_ACTION or PROPOSE_QUARANTINE
```

The base envelope remains authoritative for deterministic event identity, payload `spec_hash`, source-role binding, time ordering, finite source-edge routing, and explicit no-authority flags.

## Required fields

All profile values live in the base envelope's bounded flat `payload.attributes` map.

| Group | Required meaning |
|---|---|
| STAC identity | Item ID, asset key, HTTPS asset href, and media type |
| Request profile | Method fixed to `HEAD`; recorded HTTP status |
| Prior state | Prior `ETag`, `Last-Modified`, and positive content length bound to the base subject |
| Observed state | Recorded `ETag`, `Last-Modified`, and content length when supplied |
| Decision | One of `UNCHANGED`, `CHANGED`, `UNAVAILABLE`, `DENY`, or `ERROR` |
| Reason | Stable reason code derived from status and validator comparison |
| Safety | `download_allowed` is always `false` |
| Time | A timezone-aware check time equal to the base event occurrence time |

The asset href and validators are process metadata. They do not prove the source claim, asset bytes, rights, policy approval, freshness fitness, or release eligibility.

## Deterministic outcome table

| Recorded condition | Decision | Routing | Meaning |
|---|---|---|---|
| `304 Not Modified` | `UNCHANGED` | `NO_ACTION` | The recorded conditional check reported no change |
| `200`/`204`, all comparable validators equal | `UNCHANGED` | `NO_ACTION` | Recorded validators agree with prior state |
| `200`/`204`, all comparable validators differ | `CHANGED` | `PROPOSE_QUARANTINE` | Later reviewed fetch work may be proposed; no download occurs here |
| `200`/`204`, validators contradict one another | `ERROR` plus denial finding | `PROPOSE_QUARANTINE` | Fail closed; do not choose one validator silently |
| `200`/`204`, no observed validator | `ERROR` plus denial finding | `PROPOSE_QUARANTINE` | Change state cannot be established |
| `404` or `410` | `UNAVAILABLE` | `PROPOSE_QUARANTINE` | Asset absence requires review; it is not deletion proof |
| `401` or `403` | `DENY` | `PROPOSE_QUARANTINE` | Access is denied; do not bypass |
| `405`, `429`, or supported `5xx` | `ERROR` | `PROPOSE_QUARANTINE` | Method, rate, or upstream failure remains unresolved |

Content length is retained as advisory metadata. It is never sufficient by itself to establish content identity, and disagreement with an otherwise matching validator set is treated as conflict.

## Semantic invariants

The validator enforces that:

1. the complete base `SourceEventEnvelopeCandidate` passes first;
2. the profile asset href, media type, item/asset identity, and prior state are bound to the base subject;
3. the asset href is safe HTTPS without credentials, fragments, localhost, or unsafe literal addresses;
4. at least one prior `ETag` or `Last-Modified` validator exists;
5. the check time is timezone-aware and bound to the event time;
6. every profile event is a scheduled poll;
7. decision and reason are derived deterministically from the recorded status and validators;
8. contradictory or missing validators fail closed;
9. routing matches the finite decision exactly;
10. non-success statuses do not carry observed validator values;
11. no profile permits a download; and
12. validation performs no network, source, lifecycle, policy, release, or publication mutation.

## Validation

```bash
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_stac_asset_head_prefilter.py' \
  --verbose

KFM_NO_NETWORK=1 \
python tools/validators/validate_stac_asset_head_prefilter.py --fixtures
```

A green result proves only the bounded synthetic profile, exact fixture polarity, base-envelope integrity, and no-network boundary.

## Deferred operational work

A later, separately reviewed implementation would be required for:

- live STAC catalog search;
- source-specific authentication and rate limits;
- actual `HEAD` requests and network receipts;
- secure checkpoint storage;
- download proposal creation and reviewed connector execution;
- rights, sensitivity, and source activation decisions;
- RAW admission, evidence resolution, catalog closure, release, correction, and rollback; and
- operational observability and incident handling.

## Rollback

Before merge, close the draft pull request and remove its feature branch. After an authorized merge, revert the additive commit or merge commit. No live source, asset, lifecycle record, queue, database, cache, release, deployment, or public artifact requires restoration.

<p align="right"><a href="#top">Back to top</a></p>
