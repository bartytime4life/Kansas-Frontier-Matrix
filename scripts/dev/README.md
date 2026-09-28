<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/scripts-dev-readme
title: scripts/dev/ — Local Development Helpers
type: readme
version: v0.3
status: repository-grounded; local-development-only
owners: ["@bartytime4life"]
created: 2026-09-27
updated: 2026-09-27
policy_label: public
current_path: scripts/dev/README.md
owning_root: scripts/
responsibility: current usage and limits of local developer helpers
truth_posture: CONFIRMED command source in local checkout; runtime results require separate execution evidence
related:
  - BOOTSTRAP.md
  - ../../docs/installation.md
  - ../../tools/ci/README.md
  - ../../docs/doctrine/directory-rules.md
notes:
  - "This current guide replaces the stale v0.2 placeholder description; the original file creation date was not established."
[/KFM_META_BLOCK_V2] -->

# Local development helpers

These scripts are convenience entry points for a local checkout. The repository's [installation guide](../../docs/installation.md) gives the current dependency and configuration paths. The scripts do not decide policy, source admission, release, deployment, or publication.

## `bootstrap.sh`

The bootstrap is implemented for Ubuntu 24.04. Run its read-only prerequisite check first:

```bash
scripts/dev/bootstrap.sh --check --json
```

It checks Git, Python 3.11 or newer, Node `>=22.13 <23`, and pnpm `11.17.0`. `--python-only` or `--node-only` narrows the checks. `--check` does not create `.venv`, install dependencies, or register hooks.

Apply mode creates or reuses `.venv`, installs root Python `.[test]`, and runs `pnpm install --frozen-lockfile` for the root workspace. It does **not** install the separate `apps/site/source/` npm dependencies. It may use package indexes. The Python step uses `pyproject.toml` version ranges, whereas the repository's [CI installer](../../tools/ci/README.md) uses committed SHA-256 hash locked profiles.

```bash
scripts/dev/bootstrap.sh --no-hooks
```

The default apply command attempts `pre-commit install` after the Python install. The root test extra does not declare `pre-commit`, so default apply stops at that step unless `.venv` already contains it. Use `--no-hooks` for a dependency-only bootstrap, or install and review the optional hook tool separately before registering hooks. An apply failure can leave `.venv` or root `node_modules/` partially populated; inspect them and rerun only the needed component after fixing the cause.

`--offline` forbids network backed package resolution but requires complete local caches. `--install-system` permits `apt-get` only from an already root shell and is incompatible with `--offline`; the script never invokes `sudo`. The `--json` receipt describes observed tools and mode, not test results or a validated install. See [BOOTSTRAP.md](BOOTSTRAP.md) and `scripts/dev/bootstrap.sh --help` for the full option list.

## `regen_fixtures.sh`

This wrapper accepts no arguments and delegates to the fixture readiness lane with `KFM_NO_NETWORK=1`. That lane is currently a named `HOLD` until its producer and manifest are accepted; a hold exits `3`. It does not regenerate fixtures or provide a passing fixture validation result.

```bash
scripts/dev/regen_fixtures.sh
```

Keep generated or governed outputs in their owning roots and review them through the relevant contracts, schemas, policy, fixtures, tests, and release controls. Neither helper should be used as a shortcut around a held target.
