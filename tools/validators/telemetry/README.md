<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-telemetry-readme
title: Telemetry Validators
type: README
version: v0.2.1
status: draft; bounded-executable; local-only; no-network; non-authoritative
owners:
  - TODO-validation-steward
  - TODO-observability-steward
created: 2026-08-07
updated: 2026-09-24
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

## Lineage and trace-link admission

Lineage validators check the complete candidate against the bounded RFC 8785
canonicalization domain before schema and identity work. Invalid Unicode,
unsafe integers, and unsupported values return `ERROR / CANONICALIZATION_ERROR`
without candidate values or exception chains. Missing, empty, or non-list fixture
inventories fail the fixture command instead of producing an empty success.

The sibling `../validate_trace_receipt_link.py` reads at most 1,048,577 bytes
from one regular-file descriptor (1 MiB plus a sentinel). It checks descriptor
and path identity, mode, size, and change timestamps; observed replacement or
mutation returns a stable error. Platforms without no-follow/nonblocking opens
fail closed. This is local input admission, not an atomic filesystem snapshot
or protection against hostile parent-directory owners.

## Map-build input safety boundary

The map-build validator accepts at most `1,048,576` input bytes. It opens one
regular-file descriptor with no-follow and nonblocking flags, reads at most the
limit plus one sentinel byte, and compares descriptor/path identity, mode, size,
and modification/change timestamps before accepting the decoded JSON. Symlinks,
non-regular files, observed replacement or modification, invalid UTF-8, and
oversized inputs return `ERROR / JSON_INPUT_INVALID`; candidate contents and
filesystem paths are not echoed by the CLI. Platforms without `O_NOFOLLOW` and
`O_NONBLOCK` fail closed rather than silently using a weaker reader.

Fixture outcomes, finding-code lists, and `candidate_from` references are typed
before set membership, sorting, or dictionary lookup. Malformed fixture metadata
returns `ERROR / FIXTURE_SUITE_INVALID` instead of an uncaught `TypeError`. The
existing eleven-case `PASS` / `ABSTAIN` / `DENY` semantics and schema are unchanged.

This is not a filesystem sandbox or an atomic snapshot: parent-directory
ownership, malicious privileged writers, and changes outside the observed read
remain outside the proof. It does not implement the general telemetry-safety
placeholder, accept the Rego stubs, enable an emitter/sink, or release the
operational telemetry HOLD.

The dedicated workflow runs current profile and input-boundary tests separately
from the unchanged August 11 authoring receipt, which is replayed against its
exact authoring commit `25a58f324e6ada808714aecdf9e745d139e1b3bc`. Historical
receipt success is not current-head conformance or independent security review.

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
