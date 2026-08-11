<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-validators-telemetry-readme
title: Telemetry Projection Validator Tests
type: README
version: v0.1.0
status: draft; executable-proof; synthetic; no-network; non-authoritative
owners:
  - TODO-validation-steward
  - TODO-observability-steward
created: 2026-08-07
updated: 2026-08-07
policy_label: repository-facing; tests; telemetry; no-network
owning_root: tests/
responsibility: provide executable synthetic proof for telemetry projection contracts schemas generators validators deterministic identity and workflow safety without representing runtime export release or publication
truth_posture: CONFIRMED fifteen focused local tests and eighteen fixture cases / PROPOSED profile pending review / NEEDS VERIFICATION hosted exact-head CI
related:
  - ../../../contracts/telemetry/openlineage_run_event_projection.md
  - ../../../schemas/contracts/v1/telemetry/openlineage_run_event_projection.schema.json
  - ../../../fixtures/contracts/v1/telemetry/openlineage_run_event_projection/README.md
  - ../../../tools/generators/telemetry/README.md
  - ../../../tools/validators/telemetry/README.md
notes:
  - "Tests use only synthetic candidates and local repository files."
  - "Workflow safety checks pin read-only permissions and reject endpoint/export credentials in the new workflow."
[/KFM_META_BLOCK_V2] -->

# `tests/validators/telemetry/` — Telemetry Projection Validator Tests

The focused test modules prove the bounded local behavior of the inactive OpenLineage terminal RunEvent projection and its remote-sensing metrics/PROV companion.

## Covered behavior

- Draft 2020-12 schema validity and local RunReceipt reference resolution;
- exact replay of eighteen positive and negative fixtures;
- pinned deterministic `projection_id` and `spec_hash`;
- UTC-second normalization without wall-clock access;
- successful and failed source runs mapping to `COMPLETE` and `FAIL` terminal events;
- `PARTIAL` RunReceipt abstention;
- strict public release/public-safe/evidence gates;
- restricted and telemetry-denied evidence rejection;
- receipt and EvidenceBundle digest binding without source payloads;
- geometry side-channel rejection;
- identity changes when source receipt identity changes;
- validator non-mutation;
- static denial of network and repository-write clients;
- deterministic CLI bytes; and
- read-only, immutable-pinned, no-export workflow posture.

## Run

```bash
python -m unittest discover \
  --start-directory tests/validators/telemetry \
  --pattern 'test_openlineage_run_event_projection.py' \
  --verbose

python -m unittest discover \
  --start-directory tests/validators/telemetry \
  --pattern 'test_remote_sensing_lineage_activity.py' \
  --verbose
```

## Limits

These tests do not prove a live OpenLineage backend, upstream-schema compatibility, signed provenance, public release, or runtime authorization.

## Rollback

Remove the test lane with the paired implementation slice. No test fixture represents canonical or public data.
