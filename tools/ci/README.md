<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-ci-readme
title: CI Tools README
type: tool-readme
version: v0.4
status: draft; ci-tooling-lane; verified-dependency-bootstrap; bounded-python-no-network-startup-guard; mixed-implementation-status
owners:
  - OWNER_TBD - Tooling steward
  - OWNER_TBD - CI steward
  - OWNER_TBD - QA steward
  - OWNER_TBD - Governance steward
created: 2026-07-07
updated: 2026-09-25
policy_label: public-doc; tools; ci; qa; reviewer-summary; no-network-default; workflow-support
owning_root: tools/
responsibility: Long-lived CI support helpers for deterministic dependency bootstrap, bounded process controls, and reviewer-readable signals; never workflow, policy, test, proof, or release authority.
truth_posture: cite-or-abstain
tags: [kfm, tools, ci, github-actions, qa, reviewer-summary, validation-summary, workflows, NEEDS_VERIFICATION]
related:
  - ../README.md
  - ../../.github/README.md
  - ../../tests/README.md
  - ../../tools/validators/
  - ../../tools/qa/
  - ../../policy/
  - ../../schemas/
  - ../../contracts/
  - ../../release/
  - ../../artifacts/qa/
notes:
  - "This README replaces blank placeholder content at tools/ci/README.md."
  - "tools/README.md lists tools/ci/ as PROPOSED for CI helpers such as render_ui_validation_summary.py."
  - "This lane contains CI support helper code only. GitHub workflow definitions belong under .github/workflows/."
  - "CI helper scripts render and normalize signals; they do not author policy, schemas, contracts, release decisions, or test truth."
  - "The hash-locked Python CI installer, its finite profiles, lockfiles, focused tests, and workflow wiring are VERIFIED; unrelated proposed helper families retain their stated status."
  - "kfm_no_network/sitecustomize.py is an opt-in Python-process startup guard verified by the Hydrology negative proof; it is not runner-wide or non-Python isolation."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# CI tools

> Tooling lane for CI-support helpers under `tools/ci/`. Use this directory for long-lived helper scripts invoked by CI workflows to render summaries, normalize validation output, inspect reports, and make governance signals easier to review.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tools" src="https://img.shields.io/badge/root-tools%2F-blue">
  <img alt="Lane: ci" src="https://img.shields.io/badge/lane-ci-purple">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
</p>

**Path:** `tools/ci/README.md`  
**Status:** draft / CI tooling lane / dependency-bootstrap helper verified / bounded Python startup guard verified / mixed implementation status
**Owning root:** `tools/`  
**Lane family:** `ci`  
**Workflow companion:** `.github/workflows/`  
**Default posture:** deterministic, no-network by default, read-only over inputs, summary/report output only  
**Truth posture:** CONFIRMED `.github/` invokes validators, policies, and tools that live elsewhere and does not own their logic; VERIFIED `install_python_ci.py`, its finite profiles, SHA-256 lock enforcement, focused tests, and `python-dependency-lock.yml` wiring; VERIFIED the opt-in `kfm_no_network/sitecustomize.py` guard denies named Python-process egress paths when explicitly injected; runner-wide and non-Python isolation remain unproved; unrelated helper inventory and artifact destinations retain their file-level status.

---

## Scope

In scope:

- validation-summary renderers;
- reviewer-summary renderers;
- report normalizers;
- CI gate status summarizers;
- artifact index helpers;
- workflow-safe wrappers around validators or QA tools;
- local-parity helper scripts used by CI and developer machines.
- finite dependency-bootstrap profiles backed by committed hash lockfiles.

Out of scope:

- GitHub workflow YAML files;
- policy, schema, contract, validator, or test authority;
- release decisions or promotion approvals;
- generated CI artifacts as source records;
- one-off convenience scripts.

---

## Repo fit

| Responsibility | Correct home | Relationship |
|---|---|---|
| CI helper scripts | `tools/ci/` | This lane. |
| GitHub workflows | `.github/workflows/` | Workflow orchestration that may call these helpers. |
| GitHub platform hooks | `.github/` | Platform governance hooks. |
| Validators and QA tools | `tools/validators/`, `tools/qa/` | Logic these helpers may call or summarize. |
| Tests | `tests/` | Tests prove behavior; CI helpers are not tests. |
| QA reports | `artifacts/qa/` or accepted report roots | Output location, not helper source. |
| Release gates | `release/` | Promotion/release authority. |
| Policy, schemas, contracts | `policy/`, `schemas/`, `contracts/` | Authority roots read or summarized by CI. |

> [!IMPORTANT]
> `tools/ci/` must not become workflow authority, policy authority, schema authority, contract authority, test authority, release authority, artifact storage, or generated-output storage.

---

## CI-helper rule

CI helpers make governance signals readable and repeatable. They do not invent governance.

| Expectation | Required posture |
|---|---|
| Thin wrapper | Calls or summarizes accepted tools, tests, policy, schemas, or contracts. |
| Local parity | Prefer commands that can run locally and in CI with the same inputs. |
| No-network default | Avoid live services unless a workflow explicitly enables a gated live tier. |
| Deterministic output | Same inputs should produce stable summaries. |
| Read-only by default | Do not mutate source, lifecycle data, release records, proofs, or receipts. |
| Fail closed | Missing input, malformed report, unknown gate status, or contradictory result fails visibly. |

---

## Expected helper families

| Family | Purpose | Status |
|---|---|---|
| `install_python_ci` | Install fixed third-party locks, then approved local packages without dependency resolution or build isolation. | VERIFIED with focused tests and Python 3.11/3.12 workflow coverage. |
| `python-dependency-lock-migration.json` | Bind each historical workflow hash to exactly one reviewed locked-install transition. | VERIFIED by the installer and generated-receipt suites; one-time migration only. |
| `kfm_no_network/sitecustomize.py` | Fail closed on named IPv4/IPv6 connection, socket-send, resolver, and URL-open APIs for explicitly guarded Python processes. | VERIFIED by the Hydrology subprocess negative proof; not runner-wide, non-Python, or non-named API isolation. |
| `render_validation_summary` | Convert validator/test output into reviewer-readable Markdown or JSON. | PROPOSED. |
| `render_ui_validation_summary` | Render UI trust-state validation summaries. | PROPOSED in parent README. |
| `normalize_test_report` | Normalize JUnit/coverage/QA reports for downstream checks. | PROPOSED. |
| `gate_status_summary` | Summarize gate outcomes without making the gate decision. | PROPOSED. |
| `artifact_index` | Index generated QA artifacts for reviewer navigation. | PROPOSED. |
| `local_ci_parity` | Help reproduce CI commands locally. | PROPOSED. |

---

## Current and proposed layout

```text
tools/ci/
|-- README.md
|-- install_python_ci.py
|-- kfm_no_network/
|   |-- README.md
|   `-- sitecustomize.py
|-- python-dependency-lock-migration.json
|-- python-audit.lock
|-- python-test.lock
|-- render_validation_summary.PROPOSED
|-- render_ui_validation_summary.PROPOSED
|-- normalize_test_report.PROPOSED
|-- gate_status_summary.PROPOSED
|-- artifact_index.PROPOSED
`-- local_ci_parity.PROPOSED
```

The dependency-bootstrap entries are tracked and verified. The `.PROPOSED` entries remain schematic.

---

## Run posture

Inspect the finite install profiles and run their invariant tests without performing an install:

```bash
python tools/ci/install_python_ci.py --help
python -m unittest tests/ci/test_install_python_ci.py -v
python -m pytest -q -p no:cacheprovider \
  tests/domains/hydrology/test_no_network_proof.py
```

Default operation should be deterministic, local, and no-network. Workflow-specific live checks must be explicit, gated, and reviewed.

---

## Pipeline and native Explorer CI entry points

The repository has two additional local-parity targets. These exercise existing
implementation and emit test diagnostics; they do not run live acquisition or
advance a lifecycle state.

| Target | Scope | Continuous workflow |
|---|---|---|
| `make offline-pipeline-check` | Synthetic KanPlan capture, geometry conversion, evidence resolution, refresh and rollback checks; WBD HUC12 candidates; Mesonet normalization and station health; the people/DNA/land assessment adapter; Python egress-denial proof | [offline-pipeline-check](../../.github/workflows/offline-pipeline-check.yml), Python 3.11 and 3.12 |
| `make native-explorer-check` | Retired monorepo Explorer app | Explicit `WORKFLOW_HOLD` for a retired target |

Prepare the pipeline dependencies before enabling the test-process network guard:

```bash
python tools/ci/install_python_ci.py project-test
python tools/ci/install_python_ci.py geo-transforms
make offline-pipeline-check
```

The finite `geo-transforms` profile uses `python-geo.lock`: the optional
`pyproj==3.7.2` declared by `packages/geo/pyproject.toml`, plus hash-pinned certifi.
Wheel hashes cover Python 3.11/3.12; CI requires binary distributions. This adds
an optional test dependency without changing the root runtime dependency set.
The Make target injects the existing Python startup guard and sets
`PROJ_NETWORK=OFF` to prevent native PROJ grid downloads. This is bounded
process-level protection, not a host firewall or proof of all native-code egress.

The former native app and Explorer Web workbench have been removed from this
branch. Their app-only CI workflows were retired; the Make target remains an explicit
hold for old command callers. Build and test the current application
from the [standalone Site v71 source branch](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/codex/live-site-v71-source-20260925).

The existing local-data, inactive-spec, WBD-ingest, Mesonet-normalizer and
Mesonet-health workflows now react to their Python bootstrap/lock and shared
validator changes. Test processes explicitly inject the existing Python egress
guard, after dependency installation. Cached Python dependencies bind to the test lock where
caching is used. Existing check names and failure behavior remain intact. The three existing
workflow-bound authoring receipts replay their exact historical ancestor bytes
with a full-history checkout; their JSON is not rewritten. The new offline
workflow separately checks the current change receipt and its artifact hashes.
Path-filtered jobs are scoped checks; a filtered/skipped workflow is not passing
validation evidence. Repository-wide CI and independent acceptance remain
separate. See [GitHub workflow filtering](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions#onpushpull_requestpull_request_targetpathspaths-ignore)
and [PROJ network settings](https://pyproj4.github.io/pyproj/stable/api/network.html).

Directory Rules basis: accepted [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md)
places platform orchestration in `.github/`, shared bootstrap tools in `tools/`,
conformance tests in `tests/`, and repository-wide commands in `Makefile`.
Generated authorship receipts remain under `data/receipts/generated/`; JUnit
files are temporary CI diagnostics, not release or proof authority.

Rollback before integration is branch abandonment. After authorized integration,
revert this bounded workflow/Make/bootstrap change together; preserve historical
receipts. Do not remove a later required check without its own control review.
No source registration, provider retrieval, real-data transformation, policy
decision, release, deployment, public serving, or hosted WebGL acceptance follows
from a green result.

---

## Maintenance checklist

- [ ] Keep workflow YAML in `.github/workflows/`, not `tools/ci/`.
- [ ] Keep generated reports in accepted artifact/report roots, not this source lane.
- [ ] Keep helpers read-only unless a reviewed workflow explicitly requires a write.
- [ ] Preserve local parity for commands whenever practical.
- [ ] Do not let CI summaries replace test results, policy decisions, release records, receipts, or proofs.
- [ ] Document CLI inputs, outputs, exit codes, and artifact destinations once implemented.

---

## Verification status

| Item | Status |
|---|---|
| Target README path | CONFIRMED; blank placeholder replaced. |
| Parent `tools/` boundary | CONFIRMED in `tools/README.md`. |
| `tools/ci/` placement | CONFIRMED as PROPOSED helper lane in `tools/README.md`. |
| `.github/` workflow boundary | CONFIRMED in `.github/README.md`. |
| Dependency installer and lockfiles | VERIFIED by `tests/ci/test_install_python_ci.py`. |
| Dependency CLI shape and Python runtime | VERIFIED for fixed profiles; arbitrary package, URL, index, and shell input are denied by construction. |
| Dependency workflow wiring | VERIFIED in `.github/workflows/python-dependency-lock.yml` and migrated callers. |
| Python no-network startup guard | VERIFIED for 15 named Python-process connection, socket-send, resolver, and URL-open APIs; runner-wide, non-Python, and non-named API isolation remain NEEDS VERIFICATION. |
| Artifact/report destinations | NEEDS VERIFICATION. |
| Focused dependency tests | VERIFIED locally; hosted Python 3.11/3.12 checks remain the PR evidence boundary. |
| Unrelated tests and validators | Not claimed by this dependency-bootstrap update. |
