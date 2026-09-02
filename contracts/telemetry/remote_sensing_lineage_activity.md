<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-telemetry-remote-sensing-lineage-activity
title: Remote-Sensing Lineage Activity Contract
type: semantic-contract
version: v0.1.0
status: draft; PROPOSED; fixture-first; local-only; no-network; non-authoritative
owners:
  - TODO-observability-steward
  - TODO-remote-sensing-steward
  - TODO-runtime-steward
  - TODO-validation-steward
created: 2026-08-10
updated: 2026-08-10
policy_label: public; contracts; telemetry; lineage; remote-sensing; no-truth-authority
owning_root: contracts/
responsibility: define a deterministic companion that binds bounded remote-sensing scene metrics and a PROV-shaped activity to an already governed terminal OpenLineage projection without contacting sources exporting telemetry or creating evidence policy review release publication or public-use authority
truth_posture: CONFIRMED source and repository lane inspection plus focused local validation / PROPOSED inactive companion / NEEDS VERIFICATION hosted exact-head CI upstream interoperability and steward adoption
related:
  - ./openlineage_run_event_projection.md
  - ../../schemas/contracts/v1/telemetry/remote_sensing_lineage_activity.schema.json
  - ../../fixtures/contracts/v1/telemetry/remote_sensing_lineage_activity/README.md
  - ../../tools/generators/telemetry/README.md
  - ../../tools/validators/telemetry/README.md
  - ../../tests/validators/telemetry/README.md
  - ../../docs/intake/exploratory/pass-32-remote-sensing-lineage-activity-source-map.md
notes:
  - "This companion reuses the existing OpenLineage projection contract and validator instead of creating a second run-receipt or lineage authority."
  - "Scene counts, runtime, retries, failures, and source links are synthetic receipt-safe metadata; no imagery, geometry, coordinates, source bytes, or credentials are admitted."
  - "A passing activity is telemetry-shape evidence only and cannot establish remote-sensing truth or authorize release."
[/KFM_META_BLOCK_V2] -->

# Remote-Sensing Lineage Activity

`RemoteSensingLineageActivity` is a deterministic, fixture-only companion to `OpenLineageRunEventProjection`. It records bounded remote-sensing run metrics and a PROV-shaped activity only after an existing local OpenLineage projection has made the receipt, dataset, evidence-resolution, sensitivity, lifecycle, and telemetry gates explicit.

It answers one narrow question:

> Can coherent scene counts, runtime, retries, failure counts, receipt-safe source links, and PROV relations be bound to this already-governed terminal lineage projection without creating a live emitter or a new authority?

It does not fetch imagery, query a catalog, run an algorithm, post an event, contact a lineage backend, verify an external OpenLineage schema, sign an attestation, write evidence, move lifecycle state, promote, release, deploy, publish, or authorize public use.

## Source-derived adaptation

Pass 32 card `KFM-P32-PROG-0012` proposes remote-sensing flows emitting telemetry plus OpenLineage/PROV activities with scene counts, runtime, retries, failure counts, and source links. The connected Drive material also proposes asset-first orchestration with OpenLineage and PROV.

The repository already contains a generic, closed, fixture-only terminal `OpenLineageRunEventProjection`. This slice therefore implements the smallest missing companion:

| Source idea | Bounded repository implementation |
|---|---|
| OpenLineage emission | Embed and revalidate the existing governed terminal projection; no exporter, endpoint, or backend. |
| Scene telemetry | Exact nonnegative counts, retries, runtime, and UTC-second interval with deterministic coherence checks. |
| Source links | Sorted KFM references drawn from the embedded receipt; no private URL, credentials, source bytes, or payload. |
| PROV activity | Closed local activity with `used`, `generated`, association, interval, and source-link relations. |
| Runtime instrumentation | Deferred; the implementation is fixture-only and reads no wall clock. |

## Directory Rules basis

| Responsibility | Home |
|---|---|
| Meaning | `contracts/telemetry/` |
| Machine shape | `schemas/contracts/v1/telemetry/` |
| Synthetic examples | `fixtures/contracts/v1/telemetry/remote_sensing_lineage_activity/` |
| Deterministic construction | `tools/generators/telemetry/` |
| Validation | `tools/validators/telemetry/` |
| Executable proof | `tests/validators/telemetry/` |
| Read-only orchestration | `.github/workflows/` |
| Source reconciliation | `docs/intake/exploratory/` |
| AI authoring provenance | `data/receipts/generated/` |

No parallel source, evidence, receipt, policy, lineage sink, release, or publication root is introduced.

## Required inputs and derived views

| Field | Meaning |
|---|---|
| `source_openlineage_projection` | A complete local object conforming to the existing terminal projection schema and validator. |
| `metrics` | Scene total, processed/failed split, retry count, runtime, and normalized start/end timestamps. |
| `source_links` | Sorted, unique receipt-safe KFM references that include every source descriptor declared by the embedded RunReceipt. |
| `remote_sensing_facet` | Exact camel-case projection of the metrics and source links for downstream facet adaptation. |
| `prov_activity` | Exact PROV-shaped relation from receipt inputs to outputs under the same interval and activity identity. |
| `decision` | Finite companion disposition with sorted stable reason codes. |

The closed schema rejects additional properties, including geometry and coordinates.

## Finite decision model

| Decision | Meaning |
|---|---|
| `PASS` | The embedded projection conforms and passes, counts close, runtime matches the interval, failure state matches the source receipt, and source descriptors are linked. |
| `ABSTAIN` | The embedded projection abstains, normally because the source RunReceipt is partial. |
| `DENY` | The embedded projection denies or metric, outcome, runtime, or source-link closure is incoherent. |
| `ERROR` | Reserved for a declared upstream projection error; unreadable JSON is a validator `ERROR`. |

A failed processing run may still produce a `PASS` lineage activity when the embedded OpenLineage event is `FAIL` and `failed_scene_count` is positive. `PASS` means the failure record is coherent, not that processing succeeded.

## Deterministic identity

The companion uses repository RFC 8785 JCS plus SHA-256 over the complete candidate excluding the self-derived `activity_id`, `spec_hash`, and their repeated facet/PROV aliases:

```text
spec_hash   = SHA-256(RFC8785-JCS(identity projection))
activity_id = "kfm:remote-sensing-activity:" + spec_hash hex
```

The generator normalizes caller-supplied timestamps to UTC seconds and never reads the wall clock.

## Validation

```bash
python -m unittest discover \
  --start-directory tests/validators/telemetry \
  --pattern 'test_remote_sensing_lineage_activity.py' \
  --verbose

python tools/validators/telemetry/validate_remote_sensing_lineage_activity.py \
  --fixtures
```

The validator checks the composed JSON Schemas, invokes the existing OpenLineage projection validator on the embedded object, derives finite decisions, compares exact facet and PROV views, and recomputes identity. Findings expose codes and JSON paths only.

## Explicit non-effects

Every candidate declares that it does not contact remote-sensing sources; post or export lineage; create or modify canonical evidence; admit sources or mutate lifecycle state; grant policy, review, or release authority; promote, deploy, or publish; or authorize public use.

## Rollback

Before merge, close the draft pull request and delete its branch. After an authorized merge, revert this additive contract, schema, fixtures, generator, validator, tests, workflow, source map, README entries, and generated authoring receipt. No live source, event, backend, evidence, lifecycle object, signature, release, deployment, or publication requires migration or withdrawal.
