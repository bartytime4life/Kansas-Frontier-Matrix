<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-validators-telemetry-readme
title: Telemetry Validator Tests
type: README
version: v0.2.0
status: draft; executable-proof; synthetic; no-network; non-authoritative
owners:
  - TODO-validation-steward
  - TODO-observability-steward
created: 2026-08-07
updated: 2026-08-11
policy_label: repository-facing; tests; telemetry; no-network
owning_root: tests/
responsibility: provide executable synthetic proof for telemetry contracts schemas validators finite outcomes deterministic behavior and workflow safety without representing runtime measurement export release or publication
truth_posture: CONFIRMED focused local tests and exact fixture polarity / PROPOSED profiles pending review / NEEDS VERIFICATION hosted exact-head CI
related:
  - ../../../contracts/telemetry/openlineage_run_event_projection.md
  - ../../../schemas/contracts/v1/telemetry/openlineage_run_event_projection.schema.json
  - ../../../fixtures/contracts/v1/telemetry/openlineage_run_event_projection/README.md
  - ../../../tools/generators/telemetry/README.md
  - ../../../tools/validators/telemetry/README.md
  - ../../../contracts/telemetry/map_build_sustainability.md
  - ../../../schemas/contracts/v1/telemetry/map_build_sustainability.schema.json
  - ../../../fixtures/contracts/v1/telemetry/map_build_sustainability/README.md
notes:
  - "Tests use only synthetic candidates and local repository files."
  - "Workflow safety checks pin read-only permissions and reject endpoint/export credentials in the new workflow."
[/KFM_META_BLOCK_V2] -->

# `tests/validators/telemetry/` — Telemetry Validator Tests

The focused test modules prove the bounded local behavior of inactive OpenLineage, remote-sensing metrics/PROV, and map-build sustainability telemetry profiles.

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

The map-build sustainability suite additionally covers:

- exact `PASS`, `ABSTAIN`, and `DENY` fixture polarity;
- decimal energy-to-carbon arithmetic and explicit rounding tolerance;
- UTC measurement-window ordering and uncertainty bounds;
- missing measurement/factor abstention without invented zeros;
- closed internal-only sensitivity and non-authority fields;
- strict JSON duplicate-key and surrogate rejection;
- deterministic CLI bytes and non-mutation; and
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

python -m unittest discover \
  --start-directory tests/validators/telemetry \
  --pattern 'test_map_build_sustainability.py' \
  --verbose
```

## Limits

These tests do not prove a live OpenLineage backend, upstream-schema compatibility, signed provenance, telemetry measurement/provider accuracy, accounting methodology, threshold, public release, or runtime authorization.

## Rollback

Remove the test lane with the paired implementation slice. No test fixture represents canonical or public data.
