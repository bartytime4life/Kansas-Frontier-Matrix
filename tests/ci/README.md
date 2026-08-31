<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-ci-readme
title: CI Helper and Workflow Contract Tests
type: README
version: NEEDS VERIFICATION
status: implemented; repository-test-evidence; workflow-binding-partial
owners: OWNER_TBD
created: 2026-04-13
updated: 2026-08-31
policy_label: public-doc; tests; ci; no-network
owning_root: tests/
responsibility: Document the focused repository tests under tests/ci/ without treating passing tests as workflow, policy, release, deployment, or publication authority.
truth_posture: CONFIRMED four repository-local test modules and bounded source assertions; UNKNOWN complete hosted collection and required-check status; passing tests do not establish review, release, deployment, publication, or source authority
related:
  - ../README.md
  - ../../tools/ci/README.md
  - ../../.github/workflows/accessibility.yml
  - ../../tools/docs/wiki/README.md
[/KFM_META_BLOCK_V2] -->

# CI helper and workflow contract tests

`tests/ci/` contains four focused, repository-local test modules. They check
committed CI helpers and selected workflow or operator-script contracts; they do
not execute a hosted GitHub Actions run, install dependencies, launch a browser,
or publish the native GitHub Wiki.

This is an authored directory README, not a generated test report. The test
files and the repository surfaces they inspect remain the implementation
evidence.

## Inventory

| Test module | Surface under test | Confirmed assertions | Boundary |
|---|---|---|---|
| [`test_accessibility_workflow.py`](test_accessibility_workflow.py) | [`.github/workflows/accessibility.yml`](../../.github/workflows/accessibility.yml) | Preserves the `accessibility` name, the held `axe` job, the active `keyboard-navigation` job, the exact eight public-safe Explorer browser specifications, read-only permissions, `KFM_NO_NETWORK=1`, a 15-minute timeout, immutable action pins, and the absence of named write/secret/upload surfaces. | Parses committed YAML and checks referenced files. It does not run Playwright, prove accessibility conformance, or prove runner-level network isolation. |
| [`test_install_python_ci.py`](test_install_python_ci.py) | [`tools/ci/install_python_ci.py`](../../tools/ci/install_python_ci.py), committed lockfiles, the migration manifest, and workflow callers | Checks the exact finite profile set, hash-required installs, pinned direct dependencies, the migration schema/ID/387-entry ledger, rejection of unhashed or remote requirements, shell-free argument-vector execution, absence of direct `python -m pip install` in workflow YAML, and known-profile use by migrated workflows. | Mocks `subprocess.run`; no package is installed. The workflow-count assertion is a repository-shape invariant, not proof that every hosted job succeeds. |
| [`test_render_runtime_proof_summary.py`](test_render_runtime_proof_summary.py) | [`tools/ci/render_runtime_proof_summary.py`](../../tools/ci/render_runtime_proof_summary.py) | Checks deterministic reviewer Markdown for a synthetic soil-moisture report, visible expected/actual mismatch reporting, rejection of a contradictory `matched` flag, optional file output, and no mutation of the input object. | Uses synthetic JSON in a temporary directory. A rendered summary is reviewer aid, not proof, policy, source truth, or release authority. |
| [`test_sync_kfm_github_wiki_contract.py`](test_sync_kfm_github_wiki_contract.py) | [`tools/docs/wiki/sync_kfm_github_wiki.ps1`](../../tools/docs/wiki/sync_kfm_github_wiki.ps1) | Checks dry-run-by-default behavior, the exact immutable source commit, the exact 16-page allowlist, exclusion of `README.md`, rejection of unexpected changed/staged paths, absence of named force/reset/clean operations, and remote-commit readback after an explicit publish path. | Reads PowerShell as text. It does not execute PowerShell, clone repositories, authenticate, push, or prove that the native wiki matches the source packet. |

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
```

These tests use committed files, synthetic values, mocks, and temporary local
files. They require no network access and should not receive credentials or
secrets.

## Interpret failures

| Failure area | First check |
|---|---|
| Accessibility workflow | Compare the workflow jobs, action pins, permissions, environment, timeout, and exact browser-spec list with the intended bounded change. Do not relax a security assertion merely to accept broader workflow authority. |
| Python CI installer | Check whether the finite profile set, lockfiles, migration ledger, workflow call sites, or safe subprocess construction changed together. A changed workflow count can be repository drift rather than an installer defect. |
| Runtime-proof renderer | Inspect the report contract and whether expected/actual outcomes, mismatch counts, or the `matched` flag became contradictory. Do not hide a mismatch in presentation code. |
| Wiki synchronization | Compare the immutable source commit, allowlisted pages, dry-run gate, Git operations, and remote-readback contract. A desired publication change still requires separate operator authorization. |

A passing module means its committed assertions held for the exact checkout.
It does not establish that a check is required by a ruleset, that a hosted job
reached its substantive stage, or that any source, release, deployment,
promotion, or publication transition occurred.

## Workflow binding

The Python dependency-installer test is explicitly documented by
[`tools/ci/README.md`](../../tools/ci/README.md). The accessibility contract test
is also referenced by accessibility documentation. Current repository search
does not identify a workflow or Make target that names the complete
`tests/ci/` directory, the renderer test, or the wiki-sync contract test.

Treat direct hosted binding for those modules as **UNKNOWN** unless an exact
workflow command or aggregate test command proves it. A broad test command may
still collect them; do not infer that relationship from a workflow name alone.

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
