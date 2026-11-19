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

### Run the `policy` lane locally

Use the OPA build CI uses: v1.19.0, the static Linux x86-64 binary, checked
against the SHA-256 pinned in `pass12-release-policy-v1.yml` and
`policy-test.yml`. Keep it outside the repository and pass it through `OPA_BIN`
so nothing on `PATH` changes:

```bash
OPA_DIR="$HOME/.local/opt/opa-1.19.0" &&
mkdir -p "$OPA_DIR" &&
curl -fsSL -o "$OPA_DIR/opa.download" \
  https://github.com/open-policy-agent/opa/releases/download/v1.19.0/opa_linux_amd64_static &&
echo "1dd5c5591ff856f5e20a1d66bafae9511ddf3c5552ed3b5070c70b2b6580ee3f  $OPA_DIR/opa.download" | sha256sum -c - &&
chmod 0755 "$OPA_DIR/opa.download" &&
mv "$OPA_DIR/opa.download" "$OPA_DIR/opa" &&
OPA_BIN="$OPA_DIR/opa" make policy
```

Every step is chained with `&&`, so a failed download or checksum stops the
block even when it is pasted into an interactive shell, and the binary only
reaches the `opa` path after it verifies. The lane runner trusts whatever
`OPA_BIN` names, so never point it at an unverified file. A passing run prints
`"status":"PASS"` with reason `BOUNDED_REGO_PAIR_PASSED` and exits 0. On other platforms,
download the v1.19.0 asset for that platform and check it against the
`.sha256` file published beside it; the pinned digest above covers only the
Linux x86-64 binary. The same `OPA_BIN` also lets the OPA-backed tests in
`tests/policy/` run instead of skipping with `OPA_BINARY_UNAVAILABLE`.

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
