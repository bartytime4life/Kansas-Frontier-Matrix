# Bounded readiness lanes

The former `policy`, `fixtures`, `proof-slice`, and `catalog` Make targets were
zero-exit TODO markers. `control_plane/readiness/lanes.json` now states which
lane is executable and which lanes remain named HOLDs.

Run or inspect a lane with:

```bash
python tools/readiness/run_lane.py policy --describe
python tools/readiness/run_lane.py policy
python tools/readiness/run_lane.py fixtures
```

## Current posture

- `policy` executes only the separately governed Pass 12 release-gate Rego file
  and its native test. It requires an operator-provided or PATH-resolved OPA
  binary; it performs no download. Missing OPA is a named HOLD.
- `fixtures` remains HOLD until a repository-wide isolated regeneration producer
  and closed digest manifest exist.
- `proof-slice` remains HOLD until the Hydrology proof producer and accepted
  execution profile exist.
- `catalog` remains HOLD until an executable candidate builder and declared
  input-selection profile exist.

HOLD exits use status code 3 instead of the former misleading zero exit. The
runner emits a structured result and fixes source admission, reviewed-fixture
overwrite, catalog publication, release authorization, and deployment effects
to false.

Registry and schema inputs must be readable UTF-8 JSON, and the schema must be
valid Draft 2020-12. Missing files, malformed JSON, invalid encoding, and invalid
schema shapes return one structured `ERROR` result with exit code 2 before any
lane executes. The same checks apply to `--describe`; these input failures never
become a `PASS` or a named readiness `HOLD`.

The policy workflow checks the registered bounded Rego command and the Makefile
delegation to this runner. A green lane result is bounded execution evidence only; it does not
establish repository-wide policy evaluation, source admission, EvidenceBundle
acceptance, release, deployment, or publication.
