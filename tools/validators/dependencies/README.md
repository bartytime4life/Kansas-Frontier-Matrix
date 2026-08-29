<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-dependencies-readme
title: tools/validators/dependencies — Dependency Audit Boundary
type: README; validator-lane; supply-chain-readiness
version: v0.3
status: proposed; executable-validator; focused-tests; fail-closed; non-authoritative
owner: OWNER_TBD — Supply-chain reviewer · Validator steward · CI steward
created: 2026-07-29
updated: 2026-08-29
policy_label: repository-facing; dependency-audit; pnpm; npm; deterministic-readiness; network-classification; fail-closed; non-release
owning_root: tools/
responsibility: validate repository-local dependency-audit preconditions and classify external pnpm and npm audit output without owning manifests, lockfiles, advisories, dependency admission, release, deployment, or publication
truth_posture: CONFIRMED implementation and focused no-network tests / PROPOSED workflow execution / NEEDS VERIFICATION exact-head remote audit result
related:
  - ../README.md
  - pnpm_audit_readiness.py
  - ../../../tests/validators/test_pnpm_audit_readiness.py
  - ../../../.github/workflows/dependency-scan.yml
  - ../../../package.json
  - ../../../pnpm-workspace.yaml
  - ../../../pnpm-lock.yaml
notes:
  - "Repository readiness is no-network and deterministic; the pnpm and npm audits are point-in-time registry queries."
  - "PASS means only that declared checks passed for the inspected revision and configured advisory response."
  - "The stable workflow job id remains npm-audit; root coordination uses pnpm while the Explorer installed graph uses npm."
  - "Audit classification emits a bounded package/advisory identity projection; it never echoes the complete registry response."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `tools/validators/dependencies/` — Dependency Audit Boundary

> **Purpose.** Keep the package-manager and lockfile preflight deterministic,
> then distinguish a vulnerability regression from a broken or unavailable
> audit before CI interprets the result.

## Implemented surface

[`pnpm_audit_readiness.py`](pnpm_audit_readiness.py) has two commands:

```bash
python tools/validators/dependencies/pnpm_audit_readiness.py \
  validate-repository \
  --repository-root .

python tools/validators/dependencies/pnpm_audit_readiness.py \
  classify-audit \
  --report /path/to/pnpm-audit.json \
  --command-exit-code 0 \
  --audit-level high \
  --manager pnpm
```

`validate-repository` performs no network access. It checks:

- the accepted exact `pnpm@11.17.0` manager pin and current Node 22 engine
  contract;
- agreement between `package.json` workspaces and
  `pnpm-workspace.yaml`;
- the supported `pnpm-lock.yaml` version and complete importer set;
- safe, parseable root and workspace manifests; and
- absence of npm, Yarn, or Bun root lockfiles that would make the authority
  ambiguous.

`classify-audit` parses an already-produced npm-compatible JSON report and
labels the result for either `pnpm` or `npm`. It never queries the registry
itself. When the report supplies package-level vulnerability records, the
one-line result also includes a deterministic `threshold_vulnerabilities`
projection with package name, severity, bounded advisory IDs, and a bounded
fix hint. The projection is limited to 50 sorted package records and 10 sorted
advisory IDs per record. It does not echo titles, descriptions, dependency
paths, registry payloads, or arbitrary advisory URLs. `NOT_PROVIDED`,
`PARTIAL_INVALID`, and `COUNT_MISMATCH` remain explicit instead of being
misrepresented as a complete finding inventory.

## Finite outcomes

| Outcome | Exit | Meaning |
|---|---:|---|
| `PASS` | `0` | Readiness is coherent, or the report has no finding at or above the selected threshold and the command succeeded. |
| `REGRESSION` | `1` | The command failed and the structured report confirms one or more findings at or above the selected threshold. |
| `ERROR` | `2` | Inputs are missing, unsafe, malformed, inconsistent, unsupported, or the audit failed without confirmed threshold findings. |

Reason codes, findings, and the bounded threshold projection are sorted before
one-line JSON emission. Identical inputs therefore produce identical output.

## Workflow boundary

The `dependency-scan` workflow:

1. runs the no-network readiness command;
2. activates the exact manager through Corepack;
3. executes `pnpm audit --audit-level high --json` for the root coordination
   graph;
4. executes `npm --prefix apps/kansas-frontier-matrix-explorer audit
   --package-lock-only --workspaces=false --audit-level high --json` for the
   Explorer graph actually installed by its `npm ci` helper; and
5. passes both reports and command exit codes to the classifier, then fails if
   either graph reports a regression or error.

The workflow does not use `--ignore-registry-errors`. An unavailable registry,
unparseable response, command failure without qualifying findings, or
command/report polarity mismatch is `ERROR`, not a clean audit.

Pull-request code runs on a GitHub-hosted runner with read-only repository
permission, no secrets, no OIDC, and no write or deployment path. The advisory
lookup is still network-dependent and point-in-time.

## Authority and non-claims

This lane owns checker behavior only.

| Concern | Authority |
|---|---|
| Manager, workspace, and dependency declarations | root manifests |
| Deterministic dependency resolution | `pnpm-lock.yaml` |
| Advisory data | configured package registry |
| Readiness and report classification | this validator |
| Focused enforceability proof | `tests/validators/` |
| CI orchestration | `.github/workflows/` |
| Dependency admission and exception decisions | accepted security/supply-chain governance |
| Release, deployment, and publication | their governed responsibility roots |

A `PASS` does not prove vulnerability absence, provenance, license or rights
clearance, compatibility, reproducible artifacts, source integrity, release
readiness, deployment approval, or publication authority. Advisory data can
change without a repository commit.

## Focused tests

```bash
python -m pytest tests/validators/test_pnpm_audit_readiness.py -q
```

The suite covers the positive repository contract plus manager, engine,
workspace, lockfile, importer, malformed-manifest, symlink, threshold,
bounded advisory-projection, missing-detail, count-mismatch, malformed-report,
command-failure, polarity, deterministic-output, and CLI-exit cases. Fixtures
are temporary, synthetic, and no-network.

## Correction and rollback

If the manager, Node engine, workspace syntax, or lockfile format changes,
update the manifest/lockfile decision, validator, tests, workflow, and related
documentation in one reviewed unit. Do not relax checks to make a new format
appear compatible.

Before merge, close the draft or restore the recorded preimages. After merge,
revert the reviewed commit; do not rewrite shared history or delete prior audit
outcomes.

[Back to top](#top)
