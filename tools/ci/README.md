<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-ci-readme
title: CI Tools README
type: tool-readme
version: v0.1
status: draft; ci-tooling-lane; verified-dependency-bootstrap; mixed-implementation-status
owners:
  - OWNER_TBD - Tooling steward
  - OWNER_TBD - CI steward
  - OWNER_TBD - QA steward
  - OWNER_TBD - Governance steward
created: 2026-07-07
updated: 2026-08-12
policy_label: public-doc; tools; ci; qa; reviewer-summary; no-network-default; workflow-support
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
**Status:** draft / CI tooling lane / dependency-bootstrap helper verified / mixed implementation status
**Owning root:** `tools/`  
**Lane family:** `ci`  
**Workflow companion:** `.github/workflows/`  
**Default posture:** deterministic, no-network by default, read-only over inputs, summary/report output only  
**Truth posture:** CONFIRMED `.github/` invokes validators, policies, and tools that live elsewhere and does not own their logic; VERIFIED `install_python_ci.py`, its finite profiles, SHA-256 lock enforcement, focused tests, and `python-dependency-lock.yml` wiring; unrelated helper inventory and artifact destinations retain their file-level status.

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
```

Default operation should be deterministic, local, and no-network. Workflow-specific live checks must be explicit, gated, and reviewed.

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
| Artifact/report destinations | NEEDS VERIFICATION. |
| Focused dependency tests | VERIFIED locally; hosted Python 3.11/3.12 checks remain the PR evidence boundary. |
| Unrelated tests and validators | Not claimed by this dependency-bootstrap update. |
