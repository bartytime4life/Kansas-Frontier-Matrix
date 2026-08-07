<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/new-ideas-4-openlineage-run-event-projection
title: New Ideas 4 — OpenLineage RunEvent Projection Source Map
type: exploratory-source-map
version: v1.0.0
status: proposed; source-adaptation; non-authoritative
owners:
  - TODO-architecture-steward
  - TODO-observability-steward
  - TODO-source-intake-steward
created: 2026-08-07
updated: 2026-08-07
policy_label: internal; exploratory; telemetry; lineage
owning_root: docs/
responsibility: record the bounded adaptation of New Ideas 4 OpenLineage deterministic identity and provenance patterns into an inactive fixture-only KFM telemetry projection without adopting the source packet paths network exporters signing workflow or promotion authority
truth_posture: CONFIRMED source extraction and current repository lane inspection / PROPOSED dependency-closed projection slice / NEEDS VERIFICATION hosted exact-head CI upstream OpenLineage conformance and steward adoption
related:
  - ../../../contracts/telemetry/openlineage_run_event_projection.md
  - ../../../schemas/contracts/v1/telemetry/openlineage_run_event_projection.schema.json
  - ../../../fixtures/contracts/v1/telemetry/openlineage_run_event_projection/README.md
  - ../../../tools/generators/telemetry/README.md
  - ../../../tools/validators/telemetry/README.md
  - ../../../tests/validators/telemetry/README.md
  - ../../standards/OPENLINEAGE_FACETS.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
notes:
  - "Source: New Ideas 4.pdf supplied in the authoring session."
  - "Assay base: main@a6bbaa2a7986858bd72629cf3a77181b9e72a761."
  - "No live endpoint, OpenLineage transport, Sigstore identity, GitHub App, source activation, release, deployment, or publication is introduced."
[/KFM_META_BLOCK_V2] -->

# New Ideas 4 — OpenLineage RunEvent Projection Source Map

## Source boundary

| Field | Value |
|---|---|
| Source | `New Ideas 4.pdf` supplied in the authoring session |
| Source role | Exploratory implementation pressure; not repository, standards, policy, or runtime authority |
| Repository assay base | `main@a6bbaa2a7986858bd72629cf3a77181b9e72a761` |
| Placement authority | Accepted ADR-0029 and Directory Governance Standard v2 |
| Selected increment | Deterministic, fixture-only terminal OpenLineage `RunEvent` projection from canonical RunReceipt and EvidenceBundle-resolution summaries |
| Delivery boundary | Additive contract, schema, fixture manifest, generator, validator, tests, read-only workflow, docs, and generated authoring receipt |
| Explicitly absent | Network export, `START` event, live source, signing, OIDC, GitHub App, check-run writes, PR automation, promotion, release, deployment, publication |

## Evidence and gap assay

The source packet proposes a broad detect -> validate -> signed promotion pipeline with deterministic IDs, OpenLineage job/run/input/output facets, Sigstore attestations, GitHub checks, and PR-first delivery. Current repository inspection at the assay base confirmed:

- an adopted responsibility-root placement model;
- a semantic telemetry lane under `contracts/telemetry/`;
- machine telemetry schemas under `schemas/contracts/v1/telemetry/`;
- an existing runtime `RunReceipt` schema;
- repository-native RFC 8785 JCS plus SHA-256 support;
- an existing draft OpenLineage facets standard; and
- an already-implemented fixture-only Watcher/Planner/Executor `AgentOperationEnvelope` slice.

No executable, deterministic `RunReceipt` -> terminal OpenLineage `RunEvent` projection was found at the base. That bounded gap was selected instead of adding a live exporter or duplicating the broader agent architecture.

## Adopted ideas

| Source idea | Repository adaptation | Reason |
|---|---|---|
| Stable job/run identity | Content-derived `spec_hash` and `projection_id`; deterministic UUIDv5 from source run identity | Reuses accepted repository identity tooling while satisfying OpenLineage UUID shape. |
| Job, run, inputs, outputs, and facets | Closed event shape carrying receipt references, dataset lifecycle state, EvidenceRefs, EvidenceBundle IDs/digests, sensitivity, and public-safe state | Makes lineage useful without copying source payloads or creating evidence authority. |
| Terminal `COMPLETE` and `FAIL` events | Successful and failed canonical RunReceipts project terminal event types | Preserves failure lineage rather than treating a failed source run as a projection error. |
| Deterministic serialization and replay | Sorted bindings, pinned event time, RFC 8785 JCS, SHA-256, exact fixture identities | Supports byte-stable review and repeatable validation. |
| Fail-closed gates | `PASS`, `ABSTAIN`, `DENY`, `ERROR`; no event for non-`PASS` decisions | Prevents a fluent or partial projection from implying completion or release. |
| Sensitive-data controls | Restricted, unknown, quarantined, telemetry-denied, and unsafe public candidates emit no event | Preserves KFM default-deny posture even though the event contains references rather than payloads. |
| Evidence/provenance linkage | Every dataset EvidenceRef resolves to a summarized EvidenceBundle ID and digest | EvidenceBundle remains upstream authority; the event is a carrier only. |

**Identity tension retained for review.** The repository draft OpenLineage facet standard proposes `RunReceipt.run_id == run.runId`, while the canonical runtime receipt schema permits non-UUID run IDs. This profile derives a deterministic UUIDv5 and carries the source run ID in a facet rather than silently weakening either shape. Direct parity and upstream-profile adoption remain **NEEDS VERIFICATION** before any exporter is admitted.

## Narrowed and deferred ideas

| Source idea | Disposition | Required evidence before a later slice |
|---|---|---|
| Live OpenLineage HTTP emission | Deferred | Accepted backend/transport profile, authentication, retry/idempotency semantics, endpoint ownership, failure policy, rate limits, operational receipts, and rollback. |
| `START` event emission | Deferred | Pre-run admission object, policy state, source activation state, deterministic start identity, and interrupted-run correction semantics. |
| Sigstore/Cosign/SLSA/Rekor | Deferred | Accepted signing and subject profile, OIDC audience, issuer constraints, bundle home, offline verification, transparency-log requirement, reviewer separation, and rollback. |
| GitHub Check Run posting | Deferred | GitHub App installation identity, exact permission matrix, annotation redaction policy, concurrency, audit receipt, and ruleset coupling. |
| Automated promotion PR | Kept outside telemetry | Agent-operation/executor authority and repository delivery are separate concerns; telemetry cannot grant branch or PR permission. |
| Energy/carbon telemetry gate | Deferred | Measurement authority, units, sampling method, hardware attribution, grid factors, uncertainty, SLO owner, and failure semantics. |
| Source packet `src/`, `telemetry/`, `prov/`, `plans/`, and `artifacts/` paths | Not copied | Directory Rules require responsibility-root placement and prohibit parallel authority homes. |
| Automatic release/publication | Denied | Merge, telemetry success, and attestation are not promotion or publication. |

## Directory reconciliation

The source's implementation-style tree is mapped through current KFM responsibility roots:

- semantics -> `contracts/telemetry/`;
- machine shape -> `schemas/contracts/v1/telemetry/`;
- synthetic cases -> `fixtures/contracts/v1/telemetry/`;
- deterministic construction -> `tools/generators/telemetry/`;
- validation -> `tools/validators/telemetry/`;
- executable proof -> `tests/validators/telemetry/`;
- CI orchestration -> `.github/workflows/`;
- source adaptation -> `docs/intake/exploratory/`;
- authoring provenance -> `data/receipts/generated/`.

This placement creates no new root and no parallel telemetry, provenance, receipt, proof, source, policy, release, or publication authority.

## Acceptance boundary

The slice is dependency-closed when:

1. the projection schema is Draft 2020-12 valid and resolves the canonical runtime RunReceipt schema locally;
2. receipt input/output references equal declared dataset bindings;
3. every dataset EvidenceRef has exactly one resolution summary;
4. restricted, unknown, quarantined, or telemetry-denied evidence emits no event;
5. public projection requires published, public-safe datasets and published public/generalized evidence with public use allowed;
6. `PARTIAL` source runs abstain;
7. failed source runs produce a terminal `FAIL` event when all projection gates pass;
8. event contents bind RunReceipt and EvidenceBundle digests without geometry or source payloads;
9. projection identity and event run UUID replay deterministically;
10. local tests and fixture polarity make no network request;
11. the workflow is read-only and immutable-pinned; and
12. the generated authoring receipt binds every non-self artifact.

## Non-effects

This adaptation does not adopt the source packet as KFM doctrine, certify the external OpenLineage schema, configure a lineage backend, emit a real event, activate a source, install credentials, sign an attestation, open a runtime PR, mutate lifecycle data, promote, release, deploy, publish, or authorize public use.
