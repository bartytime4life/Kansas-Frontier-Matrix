# KFM developer CLI

This package contains small developer-facing command-line utilities for Kansas
Frontier Matrix. It does not create evidence, admit sources, publish data, or
change lifecycle state.

`doctor` checks the packaged YAML configuration with Typer, Hydra/OmegaConf,
and Rich. `diff` delegates to the existing repository JSON comparator for
local, top-level structural comparisons. `telemetry` delegates to the existing repository validator dispatcher;
it does not collect or emit operational telemetry. The greenfield CLI app under
`apps/cli/` is a separate, inactive scaffold and is not this installed command.

## Controlled validation

From the repository root:

```bash
python tools/ci/install_python_ci.py project-test
python tools/ci/install_kfm_cli.py
python -m pytest tests/packages/kfm_cli/test_doctor.py tests/packages/kfm_cli/test_telemetry.py tests/packages/kfm_cli/test_diff.py -q --strict-config --strict-markers
kfm doctor
kfm diff --left before.json --right after.json --fail-on-change
kfm telemetry --fixtures
kfm telemetry --candidate /absolute/path/to/local.json --profile map_build_sustainability
```

The CLI dependency overlay is hash-locked in `tools/ci/python-cli.lock` and is
validated by the dedicated `kfm-cli-doctor` workflow.
The diff command requires a repository checkout containing `tools/diff/stable_diff.py`,
does not interpret policy, and emits the comparator's report including local input
paths. Exit codes are 0 for a valid comparison, 1 for a difference when requested,
and 2 for invalid input or a failed handoff. Do not share reports containing
sensitive local path names. An installed CLI without its repository comparator
fails closed.
The telemetry command accepts only an explicit reviewed profile for a candidate,
binds relative candidate paths to the invoking directory, and prints the bounded
dispatcher result without a candidate path or child stderr. `PASS` and `ABSTAIN`
exit zero; `DENY` and `ERROR` exit nonzero. A checkout without the repository
validator fails closed. This does not validate an emitter, sink, live feed, or
release state.
