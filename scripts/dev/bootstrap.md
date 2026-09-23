# KFM developer bootstrap

`scripts/dev/bootstrap.sh` is a bounded local-development helper for Ubuntu
24.04. It does not establish CI compatibility, policy approval, evidence
closure, source admission, release readiness, deployment, or publication.

## Prerequisite inspection

```bash
scripts/dev/bootstrap.sh --check --json
```

Inspection verifies the repository runtime envelope:

- Python 3.11 or newer;
- Node 22.13 through the end of the 22.x line;
- pnpm 11.17.0;
- Git; and
- Ubuntu 24.04.

`--check` combined with `--install-system` is rejected with exit code 2 before
host or dependency checks, regardless of option order. Adding `--offline` or
`--json` does not permit the combination or produce a success receipt.

Inspection still invokes installed tool version commands. Whether a local pnpm
launcher is a provisioned binary or a Corepack shim needs verification: a shim
may acquire its package-manager runtime when invoked. A universal write-free or
network-free guarantee for those launchers is not established by these checks.

## Apply mode

```bash
scripts/dev/bootstrap.sh
```

Apply mode creates `.venv`, installs the Python test extras from
`pyproject.toml`, installs the Node dependency graph from `pnpm-lock.yaml`,
and installs pre-commit hooks when the accepted Python environment provides
`pre-commit`.

`--offline` adds fail-closed offline flags to both package managers. It does
not promise that the local caches are complete. Missing cached artifacts
remain an error.

## Host mutation boundary

The script never invokes `sudo`. System package installation is disabled
unless `--install-system` is supplied from an already-root shell. That mode is
incompatible with `--check` and `--offline` and is intentionally separate from
normal use.

Use `--python-only`, `--node-only`, or `--no-hooks` to narrow the operation.
Use `--json` to emit the machine-readable
`kfm.dev-bootstrap-receipt/v1` environment receipt.
