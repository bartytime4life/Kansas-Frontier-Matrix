<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-telemetry-openlineage-run-event-projection
title: OpenLineage RunEvent Projection Contract
type: semantic-contract; telemetry; lineage; projection
version: v0.1.0
status: draft; PROPOSED; fixture-first; local-only; no-network; non-authoritative
owners:
  - TODO-observability-steward
  - TODO-runtime-steward
  - TODO-contracts-steward
  - TODO-validation-steward
created: 2026-08-07
updated: 2026-08-07
policy_label: public; contracts; telemetry; lineage; no-truth-authority
owning_root: contracts/
responsibility: define the semantic boundary for deterministic terminal OpenLineage RunEvent-shaped projections derived from canonical KFM RunReceipt and EvidenceBundle-resolution summaries without exporting telemetry or creating evidence policy review release publication or public-use authority
truth_posture: CONFIRMED source and repository lane inspection plus focused local validation / PROPOSED inactive projection profile / NEEDS VERIFICATION upstream OpenLineage profile conformance hosted exact-head CI and steward adoption
related:
  - ./README.md
  - ../../schemas/contracts/v1/telemetry/openlineage_run_event_projection.schema.json
  - ../../schemas/contracts/v1/runtime/run_receipt.schema.json
  - ../../fixtures/contracts/v1/telemetry/openlineage_run_event_projection/README.md
  - ../../tools/generators/telemetry/README.md
  - ../../tools/validators/telemetry/README.md
  - ../../tests/validators/telemetry/README.md
  - ../../docs/standards/OPENLINEAGE_FACETS.md
  - ../../docs/intake/exploratory/new-ideas-4-openlineage-run-event-projection-source-map.md
notes:
  - "The profile emits no network traffic; it builds and validates JSON in memory or from explicit local candidates only."
  - "Only terminal COMPLETE or FAIL events are projected in v1; START admission remains a separate future slice because a completed RunReceipt is not pre-run authority."
  - "A passing projection is telemetry-shape evidence only and cannot promote a dataset or authorize public use."
[/KFM_META_BLOCK_V2] -->

# OpenLineage RunEvent Projection

`OpenLineageRunEventProjection` is a deterministic, fixture-only KFM object that derives one terminal OpenLineage `RunEvent`-shaped document from an existing canonical `RunReceipt`, explicitly declared input/output datasets, and bounded EvidenceBundle-resolution summaries.

The profile answers one narrow question:

> Can this already-recorded KFM run be represented as a terminal lineage event without losing receipt identity, evidence resolution, lifecycle state, sensitivity posture, or public-use restrictions?

It does not post the event, contact an OpenLineage backend, verify an external schema URL, create evidence, make a policy decision, move lifecycle state, approve review, promote, release, deploy, publish, or authorize public use.

## Status and authority boundary

| Surface | State | Limit |
|---|---|---|
| Semantic contract | **PROPOSED** | Defines a bounded local projection profile; it is not an adopted OpenLineage backend contract. |
| Draft 2020-12 schema | **CONFIRMED locally valid** | Closed machine shape with a local reference to the repository runtime `RunReceipt` schema. |
| Generator and validator | **CONFIRMED locally executable** | Deterministic, no-network, no repository mutation, fixture-only. |
| Synthetic fixture suite | **CONFIRMED** | Eighteen positive and negative cases with exact outcomes and finding-code sets. |
| Pull-request workflow | **CONFIRMED definition / NEEDS VERIFICATION execution** | Read-only, immutable action pins, no exporter credentials, exact-head hosted result pending. |
| OpenLineage upstream conformance | **NEEDS VERIFICATION** | The caller pins `schema_url`; this slice does not fetch or certify the upstream schema. |
| Runtime export or backend | **ABSENT by design** | No endpoint, transport, collector, Marquez/DataHub integration, credential, or event posting. |

## Source-derived pattern and KFM narrowing

The source packet proposes deterministic job/run identities, OpenLineage `START` and terminal events, signed provenance, and PR-first promotion. This slice adopts the smallest dependency-closed lineage portion and deliberately narrows it:

| Source idea | KFM adaptation in this slice |
|---|---|
| Emit OpenLineage events with stable IDs | Derive one deterministic terminal `COMPLETE` or `FAIL` event-shaped document using repository RFC 8785 JCS plus SHA-256 support and a deterministic UUIDv5 run identifier. |
| Attach job, run, input, output, and custom facets | Carry receipt references, source run identity, dataset lifecycle state, EvidenceRef identifiers, EvidenceBundle IDs and digests, sensitivity class, and public-safe state. |
| Post events to a lineage backend | **Deferred.** The implementation has no network client, endpoint, exporter, or credentials. |
| Emit `START` before work | **Deferred.** A terminal `RunReceipt` cannot establish pre-run admission. A later profile must bind a pre-run admission object and policy state. |
| Sign PROV/SLSA/Sigstore attestations | **Deferred.** No signing profile, OIDC audience, subject policy, transparency-log requirement, or release authority is introduced. |
| Create or update promotion PRs | **Outside this telemetry object.** Agent-operation and repository-delivery controls remain separate. |

## Directory Rules basis

Accepted ADR-0029 makes Directory Governance Standard v2 the placement authority. The profile uses existing responsibility roots rather than the source packet's illustrative top-level `telemetry/`, `prov/`, `plans/`, or `artifacts/` homes.

| Responsibility | Home |
|---|---|
| Telemetry object meaning | `contracts/telemetry/` |
| Machine shape | `schemas/contracts/v1/telemetry/` |
| Synthetic examples | `fixtures/contracts/v1/telemetry/openlineage_run_event_projection/` |
| Deterministic construction | `tools/generators/telemetry/` |
| Repository validation | `tools/validators/telemetry/` |
| Executable conformance proof | `tests/validators/telemetry/` |
| Read-only orchestration | `.github/workflows/` |
| Exploratory source adaptation | `docs/intake/exploratory/` |
| AI authoring provenance | `data/receipts/generated/` |

No parallel evidence, receipt, policy, catalog, release, proof, telemetry-sink, or publication authority is created.

## Input contract

A candidate contains the following bounded inputs:

| Field | Meaning |
|---|---|
| `request` | Requested visibility, pinned event time, namespace, job name, producer URI, caller-pinned OpenLineage schema URI, and RunReceipt reference. |
| `source_run_receipt` | Canonical repository runtime `RunReceipt` shape. The projection does not redefine that object. |
| `datasets` | Explicit input/output bindings with logical identity, lifecycle stage, public-safe flag, and EvidenceRefs. No payload or geometry is admitted. |
| `evidence_resolutions` | Resolution summaries that bind each EvidenceRef to an EvidenceBundle ID and `spec_hash`, release state, sensitivity level, telemetry permission, and public-use permission. |

The candidate must use sorted, unique bindings. Dataset references must match the receipt's declared inputs and outputs exactly, and the set of dataset EvidenceRefs must match the resolution set exactly.

## Finite decision model

The projection has four declared decisions:

| Decision | Event | Meaning |
|---|---|---|
| `PASS` | Required | A terminal event can be derived without violating the bounded gates. |
| `ABSTAIN` | `null` | The source RunReceipt is `PARTIAL`; terminal lineage would overstate completion. |
| `DENY` | `null` | Dataset/receipt binding, evidence closure, lifecycle, sensitivity, telemetry, or public-use gates fail. |
| `ERROR` | `null` | Reserved by the contract for safe operational failure; malformed input is reported by the validator as `ERROR` or `DENY` depending on readability and shape. |

A failed source run does **not** make the projection fail. A complete, internally admissible `RunReceipt.outcome = FAIL` projects a terminal OpenLineage `FAIL` event so failure lineage remains visible.

## Public and sensitivity gates

Internal projection still requires complete EvidenceRef resolution and `telemetry_allowed = true`. Evidence marked `restricted`, `unknown`, or `quarantine` is denied even when no payload is present.

Public projection is stricter. Every dataset must be `PUBLISHED` and `public_safe = true`; every EvidenceBundle summary must be `PUBLISHED`, use sensitivity `public` or `generalized`, allow telemetry, and allow public use. Any failed condition returns `DENY` and emits no event.

## Deterministic identity

The profile uses repository-native RFC 8785 JCS and SHA-256:

```text
identity projection
  = complete candidate excluding projection_id and spec_hash

spec_hash
  = SHA-256(RFC8785-JCS(identity projection))

projection_id
  = "kfm:openlineage-projection:" + spec_hash hex

run.runId
  = UUIDv5(URL namespace, source_run_receipt.run_id + "|" + source_run_receipt.spec_hash)
```

The pinned event time is normalized to UTC seconds before identity is computed. The generator does not read the wall clock.

### Identity compatibility note

The repository draft `docs/standards/OPENLINEAGE_FACETS.md` proposes direct parity between `RunReceipt.run_id` and OpenLineage `run.runId`. The canonical runtime `RunReceipt` schema, however, admits stable non-UUID identifiers, while the OpenLineage-shaped event field is constrained to UUID form in this profile. This inactive slice therefore derives a deterministic UUIDv5 and preserves the original receipt identity in the `kfm_runReceipt.sourceRunId` facet. That is a bounded compatibility projection, not a claim that the draft facet standard has been adopted or that direct run-ID parity is satisfied. Final identity semantics remain **NEEDS VERIFICATION** through an accepted OpenLineage facet/identity decision before runtime export.

## Derived terminal event

A `PASS` decision produces exactly one event with:

- `eventType`: `COMPLETE` for a successful source run or `FAIL` for a failed source run;
- the normalized caller-pinned `eventTime`;
- deterministic `run.runId`;
- a run facet binding RunReceipt reference, source run ID and `spec_hash`, code reference, source descriptors, validation references, and source outcome;
- a job facet stating the inactive projection profile, visibility, no-authority posture, and no-network mode;
- input/output datasets with lifecycle/public-safe state and EvidenceBundle IDs/digests; and
- caller-pinned `producer` and `schemaURL` values.

The closed schema rejects geometry, coordinates, raw payloads, source bytes, arbitrary custom properties, and unexpected side channels.

## Stable validator outcomes

| Validator outcome | Exit | Meaning |
|---|---:|---|
| `PASS` | `0` | Shape, ordering, binding, evidence closure, finite decision, event derivation, non-effects, and identity all match. |
| `DENY` | `1` | Readable candidate violates schema or one or more semantic invariants. |
| `ERROR` | `1` | Input JSON could not be read safely. |

Representative finding families include `SCHEMA_INVALID`, `DATASETS_NOT_SORTED`, `INPUT_DATASET_BINDING_MISMATCH`, `OUTPUT_DATASET_BINDING_MISMATCH`, `EVIDENCE_RESOLUTION_SET_MISMATCH`, `DECISION_OUTCOME_MISMATCH`, `REASON_CODES_MISMATCH`, `EVENT_PRESENCE_MISMATCH`, `EVENT_RUN_ID_MISMATCH`, `EVENT_TIME_MISMATCH`, `SPEC_HASH_MISMATCH`, and `PROJECTION_ID_MISMATCH`.

## Validation

```bash
python -m unittest discover \
  --start-directory tests/validators/telemetry \
  --pattern 'test_openlineage_run_event_projection.py' \
  --verbose

python tools/validators/telemetry/validate_openlineage_run_event_projection.py \
  --fixtures
```

Render one deterministic fixture and validate it:

```bash
python tools/generators/telemetry/build_openlineage_run_event_projection.py \
  --case valid-internal-success-complete \
  > /tmp/openlineage-projection.json

python tools/validators/telemetry/validate_openlineage_run_event_projection.py \
  --candidate /tmp/openlineage-projection.json
```

## Explicit non-effects

The candidate carries the exact ordered non-effects list:

1. `does_not_post_or_export_openlineage_events`
2. `does_not_create_or_modify_canonical_evidence`
3. `does_not_admit_sources_or_mutate_lifecycle_state`
4. `does_not_grant_policy_review_or_release_authority`
5. `does_not_promote_release_deploy_or_publish`
6. `does_not_authorize_public_use`

A green workflow is validation evidence only. It is not a source-admission record, EvidenceBundle, PolicyDecision, review approval, PromotionDecision, ReleaseManifest, deployment, publication, or runtime authorization.

## Rollback

Before merge, close the draft pull request and delete its feature branch. After an authorized merge, revert the dependency-closed contract, schema, fixtures, generator, validator, tests, workflow, source map, README integration, and generated authoring receipt. No live endpoint, stored event, external backend, canonical evidence, lifecycle record, release, deployment, or public artifact requires migration, withdrawal, or cache invalidation.
