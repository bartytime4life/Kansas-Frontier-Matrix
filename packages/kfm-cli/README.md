# KFM developer CLI

This package contains small developer-facing command-line utilities for Kansas
Frontier Matrix. It does not create evidence, admit sources, publish data, or
change lifecycle state.

`doctor` checks the packaged YAML configuration with Typer, Hydra/OmegaConf,
and Rich. `telemetry` delegates to the existing repository validator dispatcher;
it does not collect or emit operational telemetry. The greenfield CLI app under
`apps/cli/` is a separate, inactive scaffold and is not this installed command.

## Controlled validation

From the repository root:

```bash
python tools/ci/install_python_ci.py project-test
python tools/ci/install_kfm_cli.py
python -m pytest tests/packages/kfm_cli/test_doctor.py tests/packages/kfm_cli/test_telemetry.py -q --strict-config --strict-markers
kfm doctor
kfm telemetry --fixtures
kfm telemetry --candidate /absolute/path/to/local.json --profile map_build_sustainability
```

The CLI dependency overlay is hash-locked in `tools/ci/python-cli.lock` and is
validated by the dedicated `kfm-cli-doctor` workflow.
The telemetry command accepts only an explicit reviewed profile for a candidate,
binds relative candidate paths to the invoking directory, and prints the bounded
dispatcher result without a candidate path or child stderr. `PASS` and `ABSTAIN`
exit zero; `DENY` and `ERROR` exit nonzero. A checkout without the repository
validator fails closed. This does not validate an emitter, sink, live feed, or
release state.
