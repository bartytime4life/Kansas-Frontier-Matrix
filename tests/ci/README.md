<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-ci-readme
title: CI Helper and Workflow Contract Tests
type: README
version: NEEDS VERIFICATION
status: implemented; repository-test-evidence; workflow-binding-partial
owners: OWNER_TBD
created: 2026-04-13
updated: 2026-09-11
policy_label: public-doc; tests; ci; no-network
owning_root: tests/
responsibility: Document the focused repository tests under tests/ci/ without treating passing tests as workflow, policy, release, deployment, or publication authority.
truth_posture: CONFIRMED selected repository-local test modules and bounded source assertions; UNKNOWN complete hosted collection and required-check status; passing tests do not establish review, release, deployment, publication, or source authority
related:
  - ../README.md
  - ../../tools/ci/README.md
  - ../../.github/workflows/accessibility.yml
  - ../../tools/docs/wiki/README.md
[/KFM_META_BLOCK_V2] -->

# CI helper and workflow contract tests

`tests/ci/` contains focused, repository-local test modules. They check
committed CI helpers and selected workflow or operator-script contracts. Default
checks use local files and synthetic fixtures. The explicitly requested root
artifact gate additionally builds distributions and installs them into temporary
targets. These tests do not launch a browser, publish the Wiki, or approve a
release; CI dependency bootstrap is separate from artifact verification.

This is an authored directory README, not a generated test report. The test
files and the repository surfaces they inspect remain the implementation
evidence.

## Selected contract inventory

Use the current directory listing for the complete module inventory. This
2026-09-11 addition covers root-distribution configuration and an opt-in artifact gate; it does not
re-execute or re-audit the other modules summarized below.

| Test module | Surface under test | Confirmed assertions | Boundary |
|---|---|---|---|
| [`test_accessibility_workflow.py`](test_accessibility_workflow.py) | [`.github/workflows/accessibility.yml`](../../.github/workflows/accessibility.yml) | Preserves the `accessibility` name, the held `axe` job, the active `keyboard-navigation` job, the exact eight public-safe Explorer browser specifications, read-only permissions, `KFM_NO_NETWORK=1`, a 15-minute timeout, immutable action pins, and the absence of named write/secret/upload surfaces. | Parses committed YAML and checks referenced files. It does not run Playwright, prove accessibility conformance, or prove runner-level network isolation. |
| [`test_install_python_ci.py`](test_install_python_ci.py) | [`tools/ci/install_python_ci.py`](../../tools/ci/install_python_ci.py), committed lockfiles, the migration manifest, and workflow callers | Checks the exact finite profile set, hash-required installs, pinned direct dependencies, the migration schema/ID/387-entry ledger, rejection of unhashed or remote requirements, shell-free argument-vector execution, absence of direct `python -m pip install` in workflow YAML, and known-profile use by migrated workflows. | Mocks `subprocess.run`; no package is installed. The workflow-count assertion is a repository-shape invariant, not proof that every hosted job succeeds. |
| [`test_render_runtime_proof_summary.py`](test_render_runtime_proof_summary.py) | [`tools/ci/render_runtime_proof_summary.py`](../../tools/ci/render_runtime_proof_summary.py) | Checks deterministic reviewer Markdown for a synthetic soil-moisture report, visible expected/actual mismatch reporting, rejection of a contradictory `matched` flag, optional file output, and no mutation of the input object. | Uses synthetic JSON in a temporary directory. A rendered summary is reviewer aid, not proof, policy, source truth, or release authority. |
| [`test_sync_kfm_github_wiki_contract.py`](test_sync_kfm_github_wiki_contract.py) | [`tools/docs/wiki/sync_kfm_github_wiki.ps1`](../../tools/docs/wiki/sync_kfm_github_wiki.ps1) | Checks dry-run-by-default behavior, the exact immutable source commit, the exact 16-page allowlist, exclusion of `README.md`, rejection of unexpected changed/staged paths, absence of named force/reset/clean operations, and remote-commit readback after an explicit publish path. | Reads PowerShell as text. It does not execute PowerShell, clone repositories, authenticate, push, or prove that the native wiki matches the source packet. |
| [`test_root_python_distribution.py`](test_root_python_distribution.py) | [`pyproject.toml`](../../pyproject.toml) | Checks explicit metadata-only wheel selection, the three-file source-archive allowlist, no alternate root Hatch configuration, no root executable exports, and rejection of payload, hook, backend, or editable-path expansion. | Default checks parse TOML and inspect synthetic archives. With `KFM_RUN_ROOT_PYTHON_ARTIFACTS=1`, a separate test executes installed Hatchling and offline pip against temporary targets; missing build tools fail the requested gate. A default skip is not artifact evidence. |

## Run locally

Use Python 3.11 or later from the repository root. The project test extra
provides `pytest`; the root dependencies include PyYAML for the accessibility
workflow parser.

Run the complete directory:

```bash
python -m pytest -q -p no:cacheprovider tests/ci
```

Run one contract while changing its corresponding surface:

```bash
python -m pytest -q -p no:cacheprovider \
  tests/ci/test_accessibility_workflow.py
python -m unittest tests/ci/test_install_python_ci.py -v
python -m pytest -q -p no:cacheprovider \
  tests/ci/test_render_runtime_proof_summary.py
python -m pytest -q -p no:cacheprovider \
  tests/ci/test_sync_kfm_github_wiki_contract.py
python -m pytest -q -p no:cacheprovider \
  tests/ci/test_root_python_distribution.py
```

These tests use committed files, synthetic values, mocks, and temporary local
files. They require no network access and should not receive credentials or
secrets.

## Root Python distribution boundary

The root `kfm==0.0.0` distribution is a **metadata-only dependency carrier**,
not an importable SDK or the operator CLI. At the reviewed base
`664e46697d4d237870f5a482904bb9acd8f11b20`, the old manifest selected
`src/kfm`, although that root was absent. This correction removes that phantom
selection without recreating `src/`, moving a package, changing a dependency,
or adding root executable exports. Configuration assertions and real
build/install results remain separate evidence, as described below.

The wheel target intentionally specifies `include = ["/pyproject.toml"]` and
`exclude = ["*"]`. The explicit include disables package-name discovery;
exclusion takes precedence, so no project payload is selected. Do not remove
the include as redundant: falling back to discovery could select a future
same-named module. Backend-generated metadata and license metadata are a
separate surface and still require inspection of actual artifacts.

The explicit source-archive selector contains `LICENSE`, `README.md`, and
`pyproject.toml`. This is not the complete archive inventory: Hatchling 1.32.0
also adds the root `.gitignore` and default license-family `AUTHORS.md`, plus
generated `PKG-INFO`. The real gate therefore requires exactly those six
source-archive members and compares all five source-file bytes. Wheels require
exact metadata members including `licenses/LICENSE` and `licenses/AUTHORS.md`;
no arbitrary metadata or payload files are accepted. Retaining `AUTHORS.md`
preserves the existing attribution material; it does not select or clear a license. Application code, child packages, lifecycle data, fixtures, secrets,
commands, and import-path exposure are not part of this root distribution.
Build hooks, forced inclusions, artifact overrides, source remapping, alternate
`hatch.toml`, and executable exports require a separately reviewed change, not
a silent workaround to these assertions. The unchanged `TBD` license metadata
is not license clearance or permission to publish a Python distribution.

The configuration-only tests use the committed manifest as their positive case
and check that single-boundary negative mutations are rejected. Their success
establishes only configuration conformance. It does **not** establish Hatchling execution,
wheel/source-archive contents, wheel-from-source-archive rebuilding, an editable
installation, dependency availability, CLI installation, or hosted CI.

Before claiming packaging works, use a disposable environment with reviewed
build tools already installed. Build both archive formats without fetching
packages, rebuild the wheel from the source archive, inspect all member paths
and metadata, and test ordinary and editable installation without dependency
resolution. The editable result must not add the repository root or child
source directories to Python's import path; an empty backend-generated `.pth`
file is not directory exposure. Record the exact repository SHA, Python and
backend versions, commands, exit codes, archive inventories and hashes, and
metadata/extra parity. Missing build tooling is **NEEDS VERIFICATION**, not a
passing artifact test. The focused workflow bootstraps the existing hash-locked
`test-dependencies` profile in a disposable virtual environment before running the gate. No profile,
lockfile, source-admission, release, or Site deployment setting is changed.

The root declaration preserves all project metadata, dependency ranges, test
extras, backend requirements, pytest configuration, and KFM lifecycle settings.
Software distribution does not admit a source or publish KFM data. Rollback is
a reviewed revert of the manifest, regression, and documentation together. Build
verification installs only into disposable local targets; no deployed runtime
or operator workstation environment is changed. Do not describe it as merged
until GitHub confirms it.

Placement follows accepted
[ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md):
`pyproject.toml` retains root packaging configuration; the regression lives in
the existing `tests/ci/` lane; this README owns contributor-facing explanation.
No new responsibility root or parallel package home is introduced.

Technical references checked on 2026-09-11:
[Hatch file-selection rules](https://hatch.pypa.io/latest/config/build/#patterns)
and [wheel discovery](https://hatch.pypa.io/latest/plugins/builder/wheel/#default-file-selection).
The [source-builder inclusion rules](https://hatch.pypa.io/latest/plugins/builder/sdist/#default-file-selection)
and [Hatchling 1.32.0 metadata implementation](https://github.com/pypa/hatch/blob/hatchling-v1.32.0/backend/src/hatchling/metadata/core.py)
explain automatic VCS-ignore and default license-family inclusion. The first
exact-head artifact run caught the verifier's incorrect four-member assumption;
this correction preserves the manifest and makes the additional exact metadata
inputs explicit rather than accepting every backend-generated extra.

## Interpret failures

| Failure area | First check |
|---|---|
| Accessibility workflow | Compare the workflow jobs, action pins, permissions, environment, timeout, and exact browser-spec list with the intended bounded change. Do not relax a security assertion merely to accept broader workflow authority. |
| Python CI installer | Check whether the finite profile set, lockfiles, migration ledger, workflow call sites, or safe subprocess construction changed together. A changed workflow count can be repository drift rather than an installer defect. |
| Runtime-proof renderer | Inspect the report contract and whether expected/actual outcomes, mismatch counts, or the `matched` flag became contradictory. Do not hide a mismatch in presentation code. |
| Root distribution | Compare wheel selection, source-archive inputs, hooks, metadata sources, alternate Hatch configuration, and executable exports with the metadata-only boundary. A passing configuration test is not an artifact-build result. |
| Wiki synchronization | Compare the immutable source commit, allowlisted pages, dry-run gate, Git operations, and remote-readback contract. A desired publication change still requires separate operator authorization. |

A passing module means its committed assertions held for the exact checkout.
It does not establish that a check is required by a ruleset, that a hosted job
reached its substantive stage, or that any source, release, deployment,
promotion, or publication transition occurred.

## Workflow binding

The Python dependency-installer test is explicitly documented by
[`tools/ci/README.md`](../../tools/ci/README.md). The accessibility contract test
is also referenced by accessibility documentation. These are navigation
references, not current proof of hosted collection. Re-read the exact workflow
and aggregate commands before claiming that they collect this directory or
any of its modules.

For modules other than the root-distribution and installer tests explicitly
bound below, treat direct hosted binding as **UNKNOWN** unless an exact workflow
or aggregate command proves it. A broad command may still collect them; do not
infer that relationship from a workflow name alone.

The focused [root-python-distribution workflow](../../.github/workflows/root-python-distribution.yml)
explicitly collects this module on Python 3.11 and 3.12. It has read-only
repository permission, immutable action pins, no credential persistence, no
cache or artifact upload, and no PR-state, release, or deployment action. Its
path-filtered pushes include main and the preserved packaging branch; it also
runs for matching ordinary pull requests. This is workflow binding, not proof
of a hosted result or a required status check. Inspect the exact-head jobs and
logs before recording either outcome.

The same packaging job now follows the real artifact gate with the existing
installer contract and native workflow-security target in that disposable
environment:

```bash
python -m unittest tests/ci/test_install_python_ci.py -v
make workflow-security
git diff --exit-code
```

All three commands must succeed; no failure is masked. The workflow contract
rejects removal of either verification command, as well as the existing
permission, credential, real-gate, and failure-masking regressions. Trigger
scope remains packaging-focused: these supplementary checks do not replace
their owning lanes or claim complete repository-wide trigger coverage.
The native security target runs its regression suite and scans the checked-out
workflow tree. A pass covers the scanner's implemented static rules, not all
possible YAML semantics, required-check enforcement, or closure of the separate
workflow-security findings tracked under issue #3366. Neither the scanner nor
its waiver baseline is changed by this integration.

### Execute the real artifact gate

In a disposable environment, first install the existing reviewed lock profile:

```bash
python tools/ci/install_python_ci.py test-dependencies
```

That bootstrap may access the package index. The following verification does
not resolve or download dependencies and fails if required tooling is missing:

```bash
KFM_RUN_ROOT_PYTHON_ARTIFACTS=1 PIP_NO_INDEX=1 \
  python -m pytest -q -s -p no:cacheprovider --strict-config --strict-markers \
  tests/ci/test_root_python_distribution.py
```

The test builds a wheel, source archive, and editable wheel using the real
backend. It checks exact member inventories, wheel RECORD hashes/sizes,
metadata/dependency/extra parity, source-byte retention, repeated-build equality,
and a wheel rebuilt from the source archive. Temporary synthetic module,
package, `.env`, and quarantine-shaped canaries must stay excluded. No actual
restricted payload is used.

Actual pip ordinary and editable installations use separate temporary
`--target` directories, `--no-index`, `--no-deps`, and, for editable installation,
`--no-build-isolation`. A fresh `-I -S` Python process processes each checked
target; it must expose only that target and no importable root `kfm` SDK. This
proves the bounded target-install behavior, not dependency resolution, a public
SDK, installation of the separate CLI, every pip/OS combination, or workstation
setup. No claim of OS-level egress isolation is made.

A successful real gate prints `KFM_ROOT_PYTHON_ARTIFACT_VERIFICATION=` followed
by source commit, tool versions, input/artifact hashes, inventories, and the
bounded result. Artifacts remain in pytest-managed temporary directories until
runner disposal or local cleanup; they are not uploaded by this workflow. The
log is a review aid, not a canonical KFM proof or release record. Do not upload or publish
the root distribution while its license and release review remain unresolved.

Placement: the existing test and this README remain owned by `tests/`; the
thin GitHub runner lives under the existing `.github/` platform root, consistent
with the adopted Directory Rules and accepted ADR-0029. No new package,
contract, schema, policy, or proof authority is introduced. Reverting the
workflow and test/documentation follow-up together removes this gate without
changing the preserved metadata-only manifest.

## Maintenance

- Keep each test beside the `tests/ci/` inventory and point it to an existing
  committed source or workflow path.
- Update the test and this inventory together when an asserted profile, pin,
  page allowlist, report contract, or browser-spec list changes deliberately.
- Prefer exact positive and negative assertions over accepting any non-zero
  result as success.
- Keep fixtures synthetic and public-safe; do not add tokens, private URLs,
  restricted payloads, or sensitive locations.
- Document hosted binding only from an exact workflow or aggregate command.
- Preserve the distinction between repository test evidence and GitHub state,
  review, merge, release, deployment, promotion, or publication authority.

## Related boundaries

- [`tests/README.md`](../README.md) defines the repository test-root contract.
- [`tools/ci/README.md`](../../tools/ci/README.md) documents the CI helper lane.
- [`tools/docs/wiki/README.md`](../../tools/docs/wiki/README.md) documents the
  dry-run-first native-wiki transport boundary.
- [`docs/runbooks/pr-reliability-guide.md`](../../docs/runbooks/pr-reliability-guide.md)
  defines exact-SHA validation and failure-attribution guidance.
