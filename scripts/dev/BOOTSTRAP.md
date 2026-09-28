# KFM developer bootstrap

`scripts/dev/bootstrap.sh` is a bounded local-development helper for Ubuntu
24.04. It does not establish CI compatibility, policy approval, evidence
closure, source admission, release readiness, deployment, or publication.
For the separate Site npm install and all configuration paths, use the
[repository installation guide](../../docs/installation.md).

## Safe inspection

```bash
scripts/dev/bootstrap.sh --check --json
```

Inspection verifies the repository runtime envelope:

- Python 3.11 or newer;
- Node 22.13 through the end of the 22.x line;
- pnpm 11.17.0;
- Git; and
- Ubuntu 24.04.

The command is write-free unless the operator explicitly chooses apply mode.

## Apply mode

```bash
scripts/dev/bootstrap.sh --no-hooks
```

Apply mode creates `.venv`, installs the Python test extras from
`pyproject.toml`, installs the Node dependency graph from `pnpm-lock.yaml`,
and, without `--no-hooks`, tries to install pre-commit hooks. The root `test`
extra does not install `pre-commit`, so default apply stops at that point on a
fresh `.venv`. Use `--no-hooks` for dependency setup, or install the optional
hook tool separately before registering hooks. This helper's Python install
uses `pyproject.toml` version ranges; `python tools/ci/install_python_ci.py
project-test` is the committed hash locked path. Neither path installs the
standalone Site's npm dependencies.

`--offline` adds fail-closed offline flags to both package managers. It does
not promise that the local caches are complete. Missing cached artifacts
remain an error.

## Host mutation boundary

The script never invokes `sudo`. System package installation is disabled
unless `--install-system` is supplied from an already-root shell. That mode is
incompatible with `--offline` and is intentionally separate from normal use.

Use `--python-only`, `--node-only`, or `--no-hooks` to narrow the operation.
Use `--json` to emit the machine-readable
`kfm.dev-bootstrap-receipt/v1` environment receipt.
