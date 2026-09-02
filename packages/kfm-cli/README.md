# KFM developer CLI

This package contains small developer-facing command-line utilities for Kansas
Frontier Matrix. It does not create evidence, admit sources, publish data, or
change lifecycle state.

The first command is a configuration doctor built with Typer, Hydra/OmegaConf,
and Rich. It checks a small packaged YAML configuration and exits nonzero when a
required setting is missing.

## Controlled validation

From the repository root:

```bash
python tools/ci/install_python_ci.py project-test
python tools/ci/install_kfm_cli.py
python -m pytest tests/packages/kfm_cli/test_doctor.py -q --strict-config --strict-markers
kfm doctor
```

The CLI dependency overlay is hash-locked in `tools/ci/python-cli.lock` and is
validated by the dedicated `kfm-cli-doctor` workflow.
