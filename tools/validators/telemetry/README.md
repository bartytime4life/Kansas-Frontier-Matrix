<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-telemetry-readme
title: Telemetry Validators
type: README
version: v0.2.0
status: draft; bounded-executable; local-only; no-network; non-authoritative
owners:
  - TODO-validation-steward
  - TODO-observability-steward
created: 2026-08-07
updated: 2026-08-11
policy_label: repository-facing; tools; validators; telemetry
owning_root: tools/
responsibility: validate bounded telemetry profile shape identity binding arithmetic uncertainty and finite decision semantics without contacting external systems or granting operational authority
truth_posture: CONFIRMED bounded local validators and exact fixture polarity / PROPOSED inactive profiles / NEEDS VERIFICATION hosted exact-head CI and whole-repository integration
related:
  - ../../../contracts/telemetry/openlineage_run_event_projection.md
  - ../../../schemas/contracts/v1/telemetry/openlineage_run_event_projection.schema.json
  - ../../../fixtures/contracts/v1/telemetry/openlineage_run_event_projection/README.md
  - ../../generators/telemetry/README.md
  - ../../../tests/validators/telemetry/README.md
  - ../../../contracts/telemetry/map_build_sustainability.md
  - ../../../schemas/contracts/v1/telemetry/map_build_sustainability.schema.json
  - ../../../fixtures/contracts/v1/telemetry/map_build_sustainability/README.md
notes:
  - "Findings expose stable codes and JSON paths rather than candidate values."
  - "A green result is local conformance evidence only and never release or publication authority."
[/KFM_META_BLOCK_V2] -->

# `tools/validators/telemetry/` — Telemetry Validators

This lane validates admitted local telemetry projection profiles. It is downstream of semantic contracts and schemas and does not replace policy, evidence review, release decisions, or runtime authorization.

## Current validator

| File | Profile | Finite validator outcomes |
|---|---|---|
| `validate_openlineage_run_event_projection.py` | `kfm.telemetry.openlineage-run-event-projection.v1` | `PASS`, `DENY`, `ERROR` |
| `validate_remote_sensing_lineage_activity.py` | `kfm.telemetry.remote-sensing-lineage-activity.v1` | `PASS`, `DENY`, `ERROR` |
| `validate_map_build_sustainability.py` | `kfm.telemetry.map-build-sustainability.fixture.v1` | `PASS`, `ABSTAIN`, `DENY`, `ERROR` |

The lineage validators check:

- Draft 2020-12 shape with the local runtime `RunReceipt` schema;
- sorted and unique receipt, dataset, and evidence-resolution bindings;
- exact RunReceipt input/output parity;
- complete EvidenceRef-to-EvidenceBundle resolution summaries;
- deterministic finite decision and stable reason codes;
- terminal event presence, type, time, run UUID, facets, inputs, and outputs;
- exact non-effects;
- RFC 8785 JCS plus SHA-256 `spec_hash` and `projection_id`; and
- closed-shape denial of geometry and payload side channels.

The map-build sustainability validator checks:

- a closed internal-only candidate shape with all authority fixed to false;
- strict bounded JSON input and duplicate-key/surrogate rejection;
- a positive UTC measurement window;
- decimal-string energy, carbon, factor, tolerance, and uncertainty values;
- uncertainty percentages no greater than 100;
- energy-to-carbon arithmetic within declared rounding tolerance capped at `0.001 gCO2e` for fixture consistency;
- consistent safe abstention when measurement or factor evidence is unavailable; and
- exact non-effects, including no measurement, provider call, threshold, release decision, or mapped-truth claim.

## Run

```bash
python tools/validators/telemetry/validate_openlineage_run_event_projection.py \
  --fixtures

python tools/validators/telemetry/validate_openlineage_run_event_projection.py \
  --candidate /path/to/candidate.json

python tools/validators/telemetry/validate_remote_sensing_lineage_activity.py \
  --fixtures

python tools/validators/telemetry/validate_map_build_sustainability.py \
  --fixtures

python tools/validators/telemetry/validate_map_build_sustainability.py \
  --candidate /path/to/candidate.json
```

`PASS` and safe `ABSTAIN` exit `0`; `DENY` and `ERROR` exit `1`.

## Trust boundary

The validators do not authenticate EvidenceBundles, external schema URLs, policy claims, signatures, OpenLineage backends, sustainability methods or factors, telemetry providers, thresholds, or public releases. They make no network request and mutate no candidate or repository object.

## Rollback

Revert the dependency-closed telemetry projection slice. No live telemetry, lifecycle, release, or publication state needs repair.
