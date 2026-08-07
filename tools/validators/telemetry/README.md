<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-telemetry-readme
title: Telemetry Projection Validators
type: README
version: v0.1.0
status: draft; bounded-executable; local-only; no-network; non-authoritative
owners:
  - TODO-validation-steward
  - TODO-observability-steward
created: 2026-08-07
updated: 2026-08-07
policy_label: repository-facing; tools; validators; telemetry
owning_root: tools/
responsibility: validate bounded telemetry projection shape identity evidence binding lifecycle and finite decision semantics without contacting external systems or granting operational authority
truth_posture: CONFIRMED bounded validator and exact local fixture polarity / PROPOSED inactive profile / NEEDS VERIFICATION hosted exact-head CI and whole-repository integration
related:
  - ../../../contracts/telemetry/openlineage_run_event_projection.md
  - ../../../schemas/contracts/v1/telemetry/openlineage_run_event_projection.schema.json
  - ../../../fixtures/contracts/v1/telemetry/openlineage_run_event_projection/README.md
  - ../../generators/telemetry/README.md
  - ../../../tests/validators/telemetry/README.md
notes:
  - "Findings expose stable codes and JSON paths rather than candidate values."
  - "A green result is local conformance evidence only and never release or publication authority."
[/KFM_META_BLOCK_V2] -->

# `tools/validators/telemetry/` — Telemetry Projection Validators

This lane validates admitted local telemetry projection profiles. It is downstream of semantic contracts and schemas and does not replace policy, evidence review, release decisions, or runtime authorization.

## Current validator

| File | Profile | Finite validator outcomes |
|---|---|---|
| `validate_openlineage_run_event_projection.py` | `kfm.telemetry.openlineage-run-event-projection.v1` | `PASS`, `DENY`, `ERROR` |

The validator checks:

- Draft 2020-12 shape with the local runtime `RunReceipt` schema;
- sorted and unique receipt, dataset, and evidence-resolution bindings;
- exact RunReceipt input/output parity;
- complete EvidenceRef-to-EvidenceBundle resolution summaries;
- deterministic finite decision and stable reason codes;
- terminal event presence, type, time, run UUID, facets, inputs, and outputs;
- exact non-effects;
- RFC 8785 JCS plus SHA-256 `spec_hash` and `projection_id`; and
- closed-shape denial of geometry and payload side channels.

## Run

```bash
python tools/validators/telemetry/validate_openlineage_run_event_projection.py \
  --fixtures

python tools/validators/telemetry/validate_openlineage_run_event_projection.py \
  --candidate /path/to/candidate.json
```

`PASS` exits `0`; `DENY` and `ERROR` exit `1`.

## Trust boundary

The validator does not authenticate EvidenceBundles, external schema URLs, policy claims, signatures, OpenLineage backends, or public releases. It makes no network request and mutates no candidate or repository object.

## Rollback

Revert the dependency-closed telemetry projection slice. No live telemetry, lifecycle, release, or publication state needs repair.
