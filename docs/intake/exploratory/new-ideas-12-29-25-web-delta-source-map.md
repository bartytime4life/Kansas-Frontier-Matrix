<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/new-ideas-12-29-25-web-delta-source-map
title: New Ideas 12-29-2025 — License-Respectful Web Delta Source Map
type: exploratory-source-map; implementation-lineage
version: v0.1.0
status: draft; source-grounded; implementation-bounded
owners: OWNER_TBD — Source steward · Docs steward · Validation steward
created: 2026-08-07
updated: 2026-08-07
policy_label: internal; exploratory; source-map; non-authoritative
source_artifact: New Ideas 12-29-2025.docx.pdf
source_sha256: b658b53dcdab4fc24a6e27ca9d6751bc17aa2af51ead2a010a5f0c088fc7c8b4
related:
  - ../../../contracts/source/web_delta_profile.md
  - ../../../contracts/source/source_event_envelope.md
  - ../../../schemas/contracts/v1/source/web_delta_profile.schema.json
  - ../../../tools/validators/validate_web_delta_profile.py
tags: [new-ideas, source-map, web-delta, conditional-get, license, metadata-only, cloudevents-shaped]
notes:
  - "This map records what was adapted, deferred, or rejected from the attachment. It is not source admission, policy, implementation proof beyond the linked files, or release authority."
[/KFM_META_BLOCK_V2] -->

# New Ideas 12-29-2025 — License-Respectful Web Delta Source Map

## Evidence boundary

| Field | Value |
|---|---|
| Attachment | `New Ideas 12-29-2025.docx.pdf` |
| Attachment SHA-256 | `b658b53dcdab4fc24a6e27ca9d6751bc17aa2af51ead2a010a5f0c088fc7c8b4` |
| Relevant source section | “Pattern — Web → Typed CloudEvents (License-Respectful Deltas)” |
| Current repo base inspected | `main@a6bbaa2a7986858bd72629cf3a77181b9e72a761` before authoring |
| Implementation posture | Fixture-only, no-network profile over the existing `SourceEventEnvelopeCandidate` |

The attachment proposes converting changes on human-readable official pages into schema-bound deltas with conditional HTTP signals, structured extraction, canonicalization, deterministic diffing, provenance, checksums, and license-aware disclosure. It specifically distinguishes contentful payloads under permissive reuse terms from metadata-only notices when license posture is missing, ambiguous, or restrictive.

## Source-to-repository crosswalk

| Source idea | Repository adaptation | Status |
|---|---|---|
| Conditional GET and no-change heartbeat | HTTP `304` fixture maps to a no-action heartbeat with no new content digest | IMPLEMENTED in this bounded slice |
| Structured extraction order | Typed enum records `jsonld`, `microdata`, `rdfa`, `heuristic_tables`, or `none` | IMPLEMENTED as declared metadata only |
| Canonical source-family schema | Required schema reference and canonicalizer version | IMPLEMENTED as a contract/profile binding |
| RFC 6902 patch and severity | Diff digest and finite severity are represented; patch generation is not implemented | PARTIAL / future operational adapter |
| Typed CloudEvent | Reuses the repository’s CloudEvents-shaped `SourceEventEnvelopeCandidate`; does not claim full conformance | IMPLEMENTED with explicit boundary |
| License-respectful disclosure | Permissive may be contentful; restrictive/ambiguous/unknown must be metadata-only and quarantined | IMPLEMENTED as deterministic profile semantics |
| Provenance and checksums | Raw, previous, canonical-new, diff, and manifest SHA-256 references are bounded by profile rules | IMPLEMENTED as references, not proof closure |
| Signed manifest / SLSA | Not introduced; requires target-environment and supply-chain review | DEFERRED |
| STAC/DCAT/PROV, graph, UI | No catalog, graph, Story Node, API, map, or release mutation | DEFERRED |
| Live fetchers and source configs | No network, source activation, or lifecycle persistence | DEFERRED |

## Existing repository evidence that changed the adaptation

The attachment’s suggested `src/pipelines/`, `schemas/events/`, and event-bus layout was not copied. Current repository evidence already provides:

- `contracts/source/source_event_envelope.md`;
- `schemas/contracts/v1/source/source_event_envelope.schema.json`;
- deterministic JCS/SHA-256 event identity;
- source-admission and quarantine routing; and
- fixture-only no-authority validation.

Creating a second event schema or pipeline authority would duplicate responsibility. The new work therefore adds a source-family profile under the existing contract/schema/fixture/validator/test roots.

## Acceptance boundary

The slice is complete when:

- all 17 synthetic cases replay with exact outcomes and findings;
- the base source-event validator remains a hard prerequisite;
- contentful unknown-license records fail;
- restrictive, ambiguous, and unknown licenses carry metadata only;
- a `304` produces a no-action heartbeat;
- unsafe URLs, placeholder digests, disclosure leaks, and inconsistent HTTP flags fail closed;
- no network access occurs; and
- a generated authoring receipt binds every changed non-receipt artifact.

## Non-effects

This source map and implementation do not:

- validate or authorize a real source;
- fetch or retain web content;
- decide license compatibility or source rights;
- generate a real JSON Patch;
- write RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLETS, or PUBLISHED state;
- emit evidence, proof, policy, review, promotion, release, deployment, publication, or public-use authority; or
- merge, release, deploy, or publish the repository change.
