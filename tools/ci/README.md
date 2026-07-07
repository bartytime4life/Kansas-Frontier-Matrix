<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-ci-readme
title: CI Tools README
type: tool-readme
version: v0.1
status: draft; blank-placeholder-replaced; ci-tooling-lane; PROPOSED / NEEDS VERIFICATION
owners:
  - OWNER_TBD - Tooling steward
  - OWNER_TBD - CI steward
  - OWNER_TBD - QA steward
  - OWNER_TBD - Governance steward
created: 2026-07-07
updated: 2026-07-07
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
  - "Executable inventory, helper names, workflow wiring, artifact destinations, tests, and pass rates remain NEEDS VERIFICATION."
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
**Status:** draft / blank placeholder replaced / CI tooling lane / PROPOSED until executable inventory is verified  
**Owning root:** `tools/`  
**Lane family:** `ci`  
**Workflow companion:** `.github/workflows/`  
**Default posture:** deterministic, no-network by default, read-only over inputs, summary/report output only  
**Truth posture:** CONFIRMED target file existed as blank placeholder content before replacement; CONFIRMED `tools/README.md` lists `tools/ci/` as PROPOSED CI helpers; CONFIRMED `.github/` invokes validators, policies, and tools that live elsewhere and does not own their logic; NEEDS VERIFICATION for actual helper files, workflow names, artifact paths, tests, and pass rates.

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
| `render_validation_summary` | Convert validator/test output into reviewer-readable Markdown or JSON. | PROPOSED. |
| `render_ui_validation_summary` | Render UI trust-state validation summaries. | PROPOSED in parent README. |
| `normalize_test_report` | Normalize JUnit/coverage/QA reports for downstream checks. | PROPOSED. |
| `gate_status_summary` | Summarize gate outcomes without making the gate decision. | PROPOSED. |
| `artifact_index` | Index generated QA artifacts for reviewer navigation. | PROPOSED. |
| `local_ci_parity` | Help reproduce CI commands locally. | PROPOSED. |

---

## Suggested layout

```text
tools/ci/
|-- README.md
|-- render_validation_summary.PROPOSED
|-- render_ui_validation_summary.PROPOSED
|-- normalize_test_report.PROPOSED
|-- gate_status_summary.PROPOSED
|-- artifact_index.PROPOSED
`-- local_ci_parity.PROPOSED
```

The layout is schematic. Actual filenames, language, CLI shape, package manager, and workflow wiring remain NEEDS VERIFICATION.

---

## Run posture

No executable command was verified while authoring this README.

```bash
: "PROPOSED / NEEDS VERIFICATION"
python -m tools.ci --help
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
| Executable helper inventory | NEEDS VERIFICATION. |
| CLI shape and language/runtime | NEEDS VERIFICATION. |
| Workflow wiring | NEEDS VERIFICATION. |
| Artifact/report destinations | NEEDS VERIFICATION. |
| Tests and CI pass rates | NEEDS VERIFICATION. |
| Tests and validators | NOT RUN. |
