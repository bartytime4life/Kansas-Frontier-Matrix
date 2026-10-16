# Bounded readiness lanes

The former `policy`, `fixtures`, `proof-slice`, and `catalog` Make targets were
zero-exit TODO markers. Each Make target now calls
`tools/readiness/run_lane.py`, and `control_plane/readiness/lanes.json` states
which lane is executable and which lanes remain named HOLDs.

Run or inspect a lane with:

```bash
python tools/readiness/run_lane.py policy --describe
python tools/readiness/run_lane.py policy
python tools/readiness/run_lane.py proof-slice
python tools/readiness/run_lane.py fixtures
```

## Current posture

The table mirrors the registry. `tests/ci/test_readiness_lanes.py` fails when a
lane's status or HOLD reason here differs from `lanes.json`, so change both in
the same commit.

| Lane | Registry status | What runs, or the HOLD reason |
|---|---|---|
| `policy` | IMPLEMENTED | `opa test` on the Pass 12 release-gate pair `policy/rego/release_gate_v1.rego` and `policy/rego/release_gate_v1_test.rego` only. |
| `fixtures` | HOLD | A bounded water fixture regenerator is implemented; repository-wide regeneration remains unaccepted and out of scope. |
| `proof-slice` | IMPLEMENTED | `pipelines/domains/hydrology/proof_slice.py` with `control_plane/readiness/hydrology-proof-slice-profile.json`: the synthetic Hydrology slice from digest-pinned fixtures, without network access. |
| `catalog` | HOLD | A validated water WORK-preview builder exists; processed-input admission and an authoritative catalog input profile remain pending. |

`policy` needs an operator-provided or PATH-resolved OPA binary (`OPA_BIN` or
`opa`); the runner performs no download. Without one the lane exits with the
named HOLD `OPA_BINARY_UNAVAILABLE` even though its registry status is
IMPLEMENTED.

HOLD exits use status code 3 instead of the former misleading zero exit. The
runner emits a structured result and fixes source admission, reviewed-fixture
overwrite, catalog publication, release authorization, and deployment effects
to false.

## Workflow wiring

`policy-test.yml` and `hydrology-proof-slice.yml` read `lanes.json` and fail if
the `policy` or `proof-slice` lane stops being the reviewed IMPLEMENTED command.
`hydrology-proof-slice.yml` also checks that the `proof-slice` Make target still
calls the runner. Changing either lane's command therefore needs the matching
workflow assertion reviewed in the same change.

A green lane result is bounded execution evidence only; it does not establish
repository-wide policy evaluation, source admission, EvidenceBundle acceptance,
release, deployment, or publication.
