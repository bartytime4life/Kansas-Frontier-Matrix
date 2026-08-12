<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/source-retrieval-episode-source-map
title: SourceRetrievalEpisode Source Adaptation Map
type: exploratory source map
version: v0.1.0
status: draft; source-grounded; implementation-companion
owners: OWNER_TBD — Source steward · Documentation steward
created: 2026-08-11
updated: 2026-08-11
policy_label: public; exploratory; source; retrieval
related:
  - ../../../contracts/source/source_retrieval_episode.md
  - ../../../contracts/source/retrieval_artifact_handoff.md
  - ../../../schemas/contracts/v1/source/source_retrieval_episode.schema.json
  - ../../../tools/validators/source/validate_source_retrieval_episode.py
tags: [kfm, source-map, retrieval, failure-state, source-health]
[/KFM_META_BLOCK_V2] -->

# SourceRetrievalEpisode source adaptation map

## Goal

Record why a bounded `SourceRetrievalEpisode` fixture lane is worth adding
without treating planning prose, transport output, or a failed request as
evidence or source authority.

## Evidence boundary

| Evidence | Status | What it supports | What it cannot prove |
|---|---|---|---|
| `KFM_Briefing_to_System_Integration_Architecture.docx` from Google Drive | CONFIRMED supplied design source | Failed status checks must fail closed; source snapshots and finite states should remain explicit; generated briefing prose is discovery input only. | Current repository implementation or live-source behavior. |
| `KFM_Comprehensive_Research_and_Verification_Report.docx` from Google Drive | CONFIRMED supplied research source | Failed retrievals should be preserved as episodes with attempted locator, time, status/error class, validators, retry posture, and safe diagnostics; a failed retrieval must never silently substitute another source or imply absence. | KFM adoption, source rights, endpoint behavior, or production retention. |
| `contracts/source/retrieval_artifact_handoff.md` at base `01b3f70bb0514c0557e777294b36992317e992c8` | CONFIRMED repository evidence | The existing handoff admits only complete successful `GET` bytes and deliberately leaves `HEAD`, `NOT_MODIFIED`, timeout, access-denied, rate-limit, partial, unsafe, integrity-failed, cancelled, and exhausted results as process/source-health observations. | A governed record for those observations. |
| `packages/connectors-core/src/connectors_core/` transport primitives and tests at the same base | CONFIRMED repository evidence | KFM already has source-agnostic transport categories, retries, captured payloads, and result objects that a later adapter could project. | That this fixture candidate is wired into runtime transport. |
| Exact repository search for `RetrievalEpisode` at the same base | CONFIRMED bounded search result | No exact object family with this name was found before authoring. | Absence of every conceptually similar object or external/private implementation. |
| ADR-0029 and adopted Directory Rules v2 | ACCEPTED placement authority | Semantic meaning belongs in `contracts/source/`; shape, fixtures, validators, tests, workflow, source map, and generated receipt remain in their owning roots. | Source activation, policy approval, release, or publication. |

## Adaptation decision

**PROPOSED:** add one source-agnostic, fixture-only declaration that preserves a
retrieval attempt as a deterministic process observation. The candidate
composes existing transport and handoff boundaries but does not modify either.

The adaptation keeps these distinctions explicit:

- request attempt versus source content;
- source-health observation versus evidence;
- `HEAD`/validator observation versus full-body verification;
- `NOT_MODIFIED` versus a new body;
- failure versus “no current data”;
- coherent declaration versus network, source, lifecycle, or release authority.

## Scope admitted in this packet

- one semantic contract;
- one closed Draft 2020-12 schema;
- synthetic positive, abstention, denial, and error fixtures;
- one deterministic no-network validator;
- focused unit, CLI, non-echoing, identity, and false-clear tests;
- one read-only workflow; and
- one generated authoring receipt bound to the final bytes.

## Explicit non-goals

- changing `connectors-core` runtime behavior;
- adding a live connector or endpoint probe;
- storing real locators, credentials, headers, or bodies;
- creating a source registry, `SourceArtifact`, receipt, or EvidenceBundle;
- deciding source authority, rights, currentness, policy, or review;
- writing lifecycle state; or
- releasing or publishing anything.

## Follow-up boundary

A later runtime integration would need separate evidence that the transport
projection is stable, secret-safe, bounded, and linked to caller-owned
`IngestReceipt` and storage decisions. This packet does not pre-authorize that
work.

## Rollback

Revert the additive packet. No existing contract is superseded and no runtime,
source, lifecycle, release, or public state is changed.
