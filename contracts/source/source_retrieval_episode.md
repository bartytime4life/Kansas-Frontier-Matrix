<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/source/source-retrieval-episode
title: SourceRetrievalEpisode Contract
type: semantic-contract; source-health process observation; fixture-only
version: v0.1.0
status: proposed; inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Connector steward · Source steward · Validation steward
created: 2026-08-11
updated: 2026-08-11
policy_label: internal; source; retrieval; source-health; no-lifecycle-authority
related:
  - ./source_adapter.md
  - ./source_artifact.md
  - ./retrieval_artifact_handoff.md
  - ../../packages/connectors-core/src/connectors_core/core.py
  - ../../schemas/contracts/v1/source/source_retrieval_episode.schema.json
  - ../../fixtures/contracts/v1/source/source_retrieval_episode/cases.json
  - ../../tools/validators/source/validate_source_retrieval_episode.py
  - ../../tests/validators/test_validate_source_retrieval_episode.py
tags: [kfm, source, retrieval, transport, failure-episode, currentness, fixture-only]
notes:
  - "Adapts the briefing-integration snapshot protocol and the comprehensive research report's requirement to preserve failed retrieval attempts as explicit episodes rather than fabricated evidence."
  - "Complements the existing Retrieval-to-SourceArtifact Handoff; it does not replace transport results, SourceArtifact, IngestReceipt, EvidenceBundle, or source activation."
[/KFM_META_BLOCK_V2] -->

# SourceRetrievalEpisode

## Status and purpose

`SourceRetrievalEpisode` is a **PROPOSED**, fixture-only source-process record
for one bounded retrieval attempt. It preserves the attempted source, safe
locator, method, timing, transport category, validators, payload identity when
one complete body exists, retry posture, and finite next action.

The record closes a specific trust gap between the existing connector transport
result and the existing retrieval-to-`SourceArtifact` handoff:

```text
caller-owned transport
  -> SourceRetrievalEpisode declaration
  -> successful GET may separately enter retrieval-to-SourceArtifact handoff
  -> failed / HEAD-only / partial attempts remain explicit source-health records
  -> later ingest, evidence, policy, review, lifecycle, release, and publication
```

A validator `PASS` proves only that one synthetic episode declaration is
internally coherent. It does not prove that a network request occurred, that a
source is current or authoritative, that bytes are admissible, or that any
downstream object exists.

## Why the object is separate

The current retrieval-to-`SourceArtifact` handoff intentionally emits nothing
for `HEAD`, `NOT_MODIFIED`, timeout, access-denied, rate-limit, partial,
integrity-failed, unsafe, cancelled, or exhausted outcomes. Those outcomes still
matter. Losing them creates two dangerous ambiguities:

1. a failed status check may be misread as “no current data”; and
2. retry, currentness, and source-health evidence may disappear from audit.

`SourceRetrievalEpisode` records the process observation without upgrading it
to source evidence or lifecycle state.

## Finite states

| Episode status | Validator outcome | Meaning |
|---|---|---|
| `CAPTURED` | `PASS` | A complete synthetic `GET` body and digest are coherent. |
| `NO_CHANGE` | `PASS` | A conditional request coherently records `NOT_MODIFIED`; no new body is claimed. |
| `RETRY_REQUIRED` | `ABSTAIN` | A full `GET` is still required, or the attempt timed out, was rate-limited, cancelled, or exhausted its retry budget. |
| `BLOCKED` | `DENY` | Access, integrity, partial-response, or unsafe-response conditions block downstream handoff. |
| `ERROR` | `ERROR` | The episode declares an internal evaluation error. |

A coherent `HEAD` observation remains `RETRY_REQUIRED`. Transport validators
can reduce unnecessary transfers, but `HEAD` alone cannot establish semantic
currentness or produce a `SourceArtifact`.

## Core invariants

- `source_descriptor_ref` binds exactly to `source_id`.
- Attempt and completion times are canonical UTC and completion cannot precede
  the attempt.
- The safe locator contains no userinfo, query, or fragment.
- A successful `GET` requires exact non-empty byte length, SHA-256 body digest,
  media type, and coherent optional `Content-Length`.
- A successful `HEAD` contains no body identity and requires a later full
  verification.
- `NOT_MODIFIED` requires a conditional request and at least one validator
  (`ETag` or `Last-Modified`), but it creates no new body.
- Failure, partial, and no-change episodes cannot carry body digest, body byte
  count, schema fingerprint, or semantic-sentinel digest.
- Diagnostics expose stable reason codes and JSON pointers, never source values,
  credentials, response bodies, or raw locators.
- `current_data_claimed` and `no_current_data_claimed` are always false.
- Source activation, `SourceArtifact`, receipt, evidence, RAW write, promotion,
  release, publication, and public-use authority are always false.
- `episode_id` and `spec_hash` are deterministic RFC 8785 JCS plus SHA-256
  identities over the complete declaration.

## Directory Rules basis

Accepted ADR-0029 makes Directory Rules v2 effective. The primary authority is
the semantic meaning of a source-process observation, so the contract belongs
under `contracts/source/`. Machine shape, synthetic fixtures, validation,
executable proof, read-only CI, source adaptation, and generated authoring
provenance remain in their established responsibility roots.

No new source registry, connector, lifecycle lane, receipt authority, evidence
home, policy home, release home, public route, or generated-output authority is
created.

## Validation

```bash
python -m unittest -v tests.validators.test_validate_source_retrieval_episode
python tools/validators/source/validate_source_retrieval_episode.py --fixtures
```

## Non-effects

This packet does not:

- contact a source or replay a real response;
- activate or admit a source;
- create a `SourceArtifact`, `IngestReceipt`, `EvidenceRef`, or `EvidenceBundle`;
- write RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLETS, or PUBLISHED state;
- decide rights, source authority, policy, review, release, or publication; or
- represent a failed retrieval as absence of current data.

## Rollback

Before merge, close the draft pull request and delete only its feature branch.
After an authorized merge, revert the additive packet and rerun the dedicated
workflow. No source, external object, lifecycle record, evidence, release,
deployment, or public state requires restoration.
