<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/github-workflows-readme
title: .github/workflows README
type: README
version: v0.1
status: draft
owners: <repo stewards · governance reviewers · CI maintainers — placeholder, confirm via .github/CODEOWNERS>
created: 2026-07-08
updated: 2026-07-08
policy_label: public; github-actions; workflow-governance; ci; fail-closed; non-publisher; release-gated; non-authoritative
owning_root: .github/
responsibility: workflow-subtree README for GitHub Actions orchestration; documents workflow placement, check-name discipline, CI/runtime policy-parity expectations, no-network/default-fail-closed posture, watcher-as-non-publisher constraints, generated-report boundaries, branch-protection coupling, CODEOWNERS review posture, and finite gate outcomes while deferring validator logic, watcher logic, policy, schemas, contracts, tests, fixtures, evidence/proofs/receipts, release decisions, lifecycle data, and public runtime behavior to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../CODEOWNERS
  - ../../README.md
  - ../../SECURITY.md
  - ../../Makefile
  - ../../tools/README.md
  - ../../tools/ci/README.md
  - ../../tools/validators/README.md
  - ../../tools/watchers/README.md
  - ../../policy/
  - ../../schemas/
  - ../../contracts/
  - ../../tests/
  - ../../fixtures/
  - ../../release/
  - ../../data/receipts/
  - ../../data/proofs/
  - ../../infra/
notes:
  - "This README replaces an empty placeholder at .github/workflows/README.md."
  - "The parent `.github/README.md` is confirmed and marks workflow inventory, branch-protection coupling, action pinning, policy-parity wiring, generated receipts, release dry-runs, and CI/runtime enforcement as NEEDS VERIFICATION. This README preserves that boundary."
  - "Workflow YAML files may orchestrate tools, validators, tests, policy checks, release dry-runs, and summaries. They must not contain canonical validator logic, policy authority, schema authority, contract meaning, release authority, source registry authority, lifecycle data authority, or public-runtime truth."
  - "A workflow run is a platform signal, not sovereign evidence. Durable trust artifacts belong in data/receipts, data/proofs, release, accepted report roots, or other governed homes created by the tools the workflow invokes."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `.github/workflows/`

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-.github%2F-blue)
![scope](https://img.shields.io/badge/scope-github--actions-informational)
![posture](https://img.shields.io/badge/posture-fail--closed-critical)
![publisher](https://img.shields.io/badge/publisher-no-red)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `.github/workflows/` is the GitHub Actions workflow lane for KFM: YAML orchestration that runs validators, tests, policy checks, release dry-runs, summaries, and guardrails without becoming validator authority, policy authority, evidence authority, release authority, lifecycle authority, or publisher.

---

## Purpose

`.github/workflows/` exists to hold GitHub Actions workflow definitions for the KFM repository.

The durable KFM question for this subtree is:

> Which GitHub-hosted checks should run on pushes, pull requests, schedules, and manual dispatches to make KFM governance visible, repeatable, and fail-closed without allowing CI to invent rules, publish artifacts, or bypass the trust membrane?

A workflow may call validators, tests, policy tooling, release dry-runs, QA helpers, and summary renderers. It must not become the place where rules, schemas, contracts, source descriptors, evidence records, receipts, release decisions, or public truth are authored.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `.github/workflows/README.md` | **CONFIRMED README** | This README replaces the previous empty placeholder. |
| `.github/README.md` | **CONFIRMED parent README** | Parent platform-governance README marks workflow inventory and branch-protection coupling as **NEEDS VERIFICATION**. |
| `.github/CODEOWNERS` | **CONFIRMED file** | Placeholder code-owner mappings exist under `.github/`; team validity and branch-protection enforcement remain **NEEDS VERIFICATION**. |
| `.github/workflows/*.yml` inventory | **NEEDS VERIFICATION** | Search and spot checks did not establish a complete workflow inventory in this edit. |
| Required checks / branch protection | **NEEDS VERIFICATION** | GitHub repository settings were not inspected. |
| Workflow run logs, artifacts, receipts, reports, and pass/fail history | **NEEDS VERIFICATION** | No workflow run history or generated artifacts were inspected in this edit. |

[Back to top](#top)

---

## Workflow root rules

| Rule | Required posture | Anti-pattern |
|---|---|---|
| Workflows orchestrate; they do not author authority. | YAML invokes tools, validators, policy checks, tests, and release dry-runs from owning roots. | Policy, schema, contract, validator, or release logic is embedded inline in workflow YAML. |
| Fail closed. | Missing evidence, schema, policy, source descriptor, fixture, report, receipt, release reference, correction path, or rollback target blocks the relevant check. | Missing inputs produce success or best-effort public continuation. |
| Local parity where possible. | Prefer commands that can be reproduced through `Makefile`, `scripts/dev/`, `tools/`, or package scripts. | CI-only logic cannot be rerun by maintainers. |
| No-network by default. | First-pass PR checks should run offline unless a source-activated live tier is explicitly configured. | PR workflows fetch live sources or call external systems without source activation. |
| Least privilege. | Workflow token permissions should be explicit and minimal. | Broad `contents: write`, secrets, or deployment permissions are granted to ordinary validation jobs. |
| Pinned dependencies. | Actions and setup steps should use pinned refs/digests where practical. | Floating action tags silently change validation behavior. |
| Watchers are non-publishers. | Workflow-triggered watchers emit candidates, reports, and receipts only. | A workflow or watcher writes directly to catalog, triplets, published, release, or public runtime truth. |
| Public path stays governed. | CI validates public-surface denial of RAW/WORK/QUARANTINE/candidate/internal/model-output paths. | Workflow creates or blesses public artifacts without release and rollback support. |
| Logs are not trust records. | Logs help debug; durable reports/receipts/proofs live in accepted homes. | A workflow log is the only proof of a gate. |
| Branch-check names are governed. | Required-check names and job names are coordinated with branch protection. | Workflow/job rename silently breaks required checks. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Correct home | Workflow role |
|---|---|---|
| GitHub workflow YAML | `.github/workflows/` | This subtree. |
| GitHub platform root, templates, CODEOWNERS | `.github/` | Parent platform-governance root. |
| CI helper scripts and summary renderers | `tools/ci/` | Workflows may invoke helpers; helper logic lives outside YAML. |
| Validators | `tools/validators/` | Workflows call validators; YAML does not define validator truth. |
| Watchers | `tools/watchers/` | Workflows may schedule or smoke-check watchers; watchers remain non-publishers. |
| Tests | `tests/` | Workflows run tests; tests prove behavior. |
| Fixtures | `fixtures/` | Workflows consume fixtures; fixtures are not stored in workflow YAML. |
| Policy | `policy/` | Workflows evaluate policy from the policy root; they do not inline policy. |
| Schemas | `schemas/` | Workflows validate against schemas from the schema root. |
| Contracts | `contracts/` | Workflows check contract/schema/test alignment. |
| Evidence/proofs | `data/proofs/` | Tools produce or verify proof records. |
| Receipts | `data/receipts/` | Tools produce or verify receipt records. |
| Release decisions, manifests, rollback, corrections | `release/` | Workflows may dry-run release gates; they do not approve release. |
| Deployment/exposure posture | `infra/` | Workflows validate infra assumptions; infra owns deployment. |
| Public API/UI/map/AI runtime | governed app/runtime roots | Workflows test public boundaries; runtime owns public behavior. |

[Back to top](#top)

---

## Expected workflow families

The names below are a target catalog until each file is individually verified.

| Workflow family | Proposed filename | Purpose | Gate posture | Status |
|---|---|---|---|---|
| Integrity baseline | `integrity.yml` | Run local-parity baseline checks, schemas, policy, tests, receipts, and fixture closure. | A/B/C/F | **NEEDS VERIFICATION** |
| Path and drift | `path-and-drift.yml` | Enforce Directory Rules, root discipline, MetaBlock presence, and placement drift checks. | A | **PROPOSED / NEEDS VERIFICATION** |
| Contract/schema/UI/AI | `contracts-ui-ai.yml` | Validate contracts, schemas, fixtures, governed API/UI/AI envelopes. | B/C/G | **PROPOSED / NEEDS VERIFICATION** |
| Governed UI | `ui-governed.yml` | Run UI build, component, a11y, map-shell, and trust-state checks without public-data shortcuts. | B/C/G | **PROPOSED / NEEDS VERIFICATION** |
| Policy parity | `policy-parity.yml` | Check CI policy bundle digest and runtime/infra policy digest alignment. | C | **PROPOSED / NEEDS VERIFICATION** |
| Promotion dry-run | `promotion-dry-run.yml` | Run promotion gates without side effects or public publication. | A-F | **PROPOSED / NEEDS VERIFICATION** |
| Catalog closure | `catalog-closure.yml` | Verify catalog, citation, PROV/STAC/DCAT, EvidenceRef, and release-support closure. | F | **PROPOSED / NEEDS VERIFICATION** |
| Signing / integrity | `signing-integrity.yml` | Verify RunReceipts, spec hashes, signatures, manifests, and artifact digests. | F | **PROPOSED / NEEDS VERIFICATION** |
| Rollback drill | `rollback-drill.yml` | Replay rollback/correction support against dry-run releases. | F/G | **PROPOSED / NEEDS VERIFICATION** |
| Boundary guards | `boundary-guards.yml` | Prove public clients cannot read RAW/WORK/QUARANTINE/candidate/internal/model-output paths. | C/D/G | **PROPOSED / NEEDS VERIFICATION** |
| MapLibre governance | `maplibre-governance.yml` | Validate MapLibre/PMTiles/public-map performance, proof packs, and release gating. | B/C/F | **PROPOSED / NEEDS VERIFICATION** |

[Back to top](#top)

---

## Gate map

| Gate | Intent | Workflow responsibility | Status |
|---|---|---|---|
| **A — Structure & Metadata** | MetaBlock, path role, root discipline, drift detection. | Run path/drift and metadata checks from tools/tests. | **PROPOSED / NEEDS VERIFICATION** |
| **B — Schemas & Contracts** | Machine shape and semantic contract alignment. | Run schema/contract tests against canonical homes. | **PROPOSED / NEEDS VERIFICATION** |
| **C — Policy Parity** | CI and runtime policy decisions use the same policy bundle/digest where shared. | Compare policy bundle refs and evaluate policy fixtures. | **PROPOSED / NEEDS VERIFICATION** |
| **D — Security & Sensitivity** | Secret hygiene, rights, sensitivity, geoprivacy, public-safe defaults. | Run secret/sensitivity/rights/public-boundary checks. | **PROPOSED / NEEDS VERIFICATION** |
| **E — Data Quality** | Profilers, assertions, quality thresholds, fixture quality. | Run no-network DQ checks or dry-run quality gates. | **PROPOSED / NEEDS VERIFICATION** |
| **F — Provenance & Lineage** | Receipts, proofs, source refs, manifests, signatures, rollback support. | Verify generated trust artifacts and catalog/release closure. | **PROPOSED / NEEDS VERIFICATION** |
| **G — Reviewability** | CODEOWNERS, review burden, release decision, rollback/correction trace. | Expose branch-protection-facing checks and review summaries. | **PROPOSED / NEEDS VERIFICATION** |

A gate that did not run should not be treated as a pass. Missing workflow evidence should route to **NEEDS VERIFICATION**, not to optimistic completion.

[Back to top](#top)

---

## Workflow permissions posture

Use least privilege as the default.

| Workflow class | Typical permissions | Notes |
|---|---|---|
| Lint/test/schema/contract checks | `contents: read` | Most PR checks should not need write permissions. |
| PR summary comments | `pull-requests: write` or `issues: write` only when needed | Prefer deterministic comments; never include secrets or sensitive details. |
| Artifact upload | `actions: read` plus upload-artifact action permissions as needed | Artifacts are reviewer aids unless promoted into governed receipt/proof/release homes by accepted tools. |
| Release dry-run | read-only where possible | Dry-runs must not publish or mutate release authority. |
| Release publication | requires separate governance | Do not treat a workflow dispatch alone as release approval. |
| Fork PRs | minimal and secret-free | Avoid secret-bearing jobs or write permissions on untrusted code. |

[Back to top](#top)

---

## Outputs and artifact discipline

Workflow outputs should be easy to inspect and safe to discard unless promoted by governed tools.

| Output | Acceptable use | Boundary |
|---|---|---|
| Check run | Branch-protection signal. | Not a proof object by itself. |
| Log | Debugging and reviewer context. | Not durable evidence or release support. |
| JUnit / coverage / QA report | Test/report artifact for review. | Must not become data authority. |
| Deterministic PR comment | Human-readable obligations summary. | Must not disclose secrets, exact sensitive locations, or restricted source detail. |
| Candidate receipt/proof path | Pointer to output generated by accepted tools. | Receipt/proof authority lives in `data/receipts/` or `data/proofs/`, not YAML. |
| Release dry-run manifest | Candidate review artifact. | Actual release decision belongs in `release/` with review and rollback support. |

[Back to top](#top)

---

## Required negative checks

Workflow suites should eventually prove the system denies or holds unsafe states, including:

- public API/UI/map/AI reads from RAW, WORK, QUARANTINE, candidate, canonical/internal stores, or direct model runtimes;
- policy bundle missing, stale, mismatched, or not equal between CI and runtime/infra;
- schema or contract drift between `contracts/`, `schemas/`, fixtures, validators, and docs;
- missing EvidenceRef/EvidenceBundle, citation validation, receipt, proof, release reference, rollback target, or correction path;
- sensitive geometry, rare species, archaeology, cultural, infrastructure, living-person, DNA/genomic, private-land, or source-restricted material exposed to public surfaces;
- watcher or pipeline code writing directly to catalog, published, release, or public runtime surfaces;
- source-role collapse, AI-inferred authority, modeled-to-observed upgrade, or aggregate-to-place overclaim;
- workflow job that succeeds after required input is missing;
- action/tag drift, unpinned dependencies, or secret-bearing logs.

[Back to top](#top)

---

## Naming and branch-protection discipline

Workflow `name`, job ids, and required-check names are part of the governance surface.

| Item | Rule |
|---|---|
| Workflow file name | Stable, kebab-case, tied to one responsibility. |
| Workflow `name` | Human-readable and stable after branch protection references it. |
| Job id | Stable, lower-kebab or snake style; avoid accidental renames. |
| Required check | Must match produced job/check name exactly. |
| Rename | Requires coordinated branch-protection update and drift/ADR note when material. |
| Deprecated workflow | Keep a migration note until branch protection and docs are updated. |

[Back to top](#top)

---

## Minimal future layout

```text
.github/workflows/
├── README.md                         # CONFIRMED README
├── integrity.yml                     # NEEDS VERIFICATION
├── path-and-drift.yml                # PROPOSED / NEEDS VERIFICATION
├── contracts-ui-ai.yml               # PROPOSED / NEEDS VERIFICATION
├── ui-governed.yml                   # PROPOSED / NEEDS VERIFICATION
├── policy-parity.yml                 # PROPOSED / NEEDS VERIFICATION
├── promotion-dry-run.yml             # PROPOSED / NEEDS VERIFICATION
├── catalog-closure.yml               # PROPOSED / NEEDS VERIFICATION
├── signing-integrity.yml             # PROPOSED / NEEDS VERIFICATION
├── rollback-drill.yml                # PROPOSED / NEEDS VERIFICATION
├── boundary-guards.yml               # PROPOSED / NEEDS VERIFICATION
└── maplibre-governance.yml           # PROPOSED / NEEDS VERIFICATION
```

Do not add workflow files until each one has an owning steward, trigger scope, permission posture, called command, no-network posture, artifact policy, branch-protection name, and rollback/disable path.

[Back to top](#top)

---

## Review checklist

A workflow PR is ready for review when:

- [ ] It names the owning workflow family and gate(s) it supports.
- [ ] It invokes logic from `tools/`, `tests/`, `policy/`, `schemas/`, `contracts/`, `release/`, or package scripts instead of embedding canonical rules in YAML.
- [ ] It uses explicit minimal permissions.
- [ ] It is no-network by default or documents the source-activated exception.
- [ ] It has deterministic failure outcomes and does not silently skip required gates.
- [ ] It does not publish, promote, or mutate lifecycle/release/public surfaces without governed release machinery.
- [ ] It avoids secret-bearing logs and sensitive-location output.
- [ ] It documents any branch-protection-facing check names.
- [ ] It has a kill-switch or disable path for long-running/write-emitting workflows.
- [ ] It updates `.github/README.md`, this README, Makefile/scripts/runbooks, and verification backlog where behavior changes.

[Back to top](#top)

---

## Standard workflow outcomes

| Outcome | Meaning |
|---|---|
| `WORKFLOW_PASS` | Declared checks ran and passed for the declared scope. |
| `WORKFLOW_FAIL` | Declared checks ran and found a defect. |
| `WORKFLOW_DENY` | Requested publication/exposure/action must not proceed. |
| `WORKFLOW_HOLD` | Human, policy, rights, sensitivity, release, correction, or rollback review is required. |
| `WORKFLOW_ABSTAIN` | Workflow lacks enough support to evaluate the requested claim or gate. |
| `WORKFLOW_RESTRICT` | The action may proceed only under declared constraints. |
| `WORKFLOW_SKIPPED_EXPLICIT` | A documented condition skipped the job visibly. |
| `WORKFLOW_KILL_SWITCH_ACTIVE` | A kill switch stopped a workflow with an explicit outcome. |
| `WORKFLOW_PUBLIC_SURFACE_DENIED` | Public-surface exposure is blocked. |
| `WORKFLOW_SYSTEM_ERROR` | Infrastructure, dependency, malformed config, or unexpected runtime error prevented evaluation. |

[Back to top](#top)

---

## Open verification items

- **NEEDS VERIFICATION** — complete inventory of `.github/workflows/*.yml` and `.yaml` on the default branch.
- **NEEDS VERIFICATION** — exact branch-protection required-check names.
- **NEEDS VERIFICATION** — whether `integrity.yml` or equivalent exists and invokes the local verification script.
- **NEEDS VERIFICATION** — whether `verify.sh`, Make targets, or package scripts reproduce CI locally.
- **NEEDS VERIFICATION** — whether workflow actions are SHA-pinned.
- **NEEDS VERIFICATION** — whether policy parity is checked against runtime/infra references.
- **NEEDS VERIFICATION** — whether generated reports, receipts, proofs, release dry-runs, and artifacts write only to accepted homes.
- **NEEDS VERIFICATION** — whether CODEOWNERS review is required by branch protection.
- **NEEDS VERIFICATION** — whether AI-generated receipt gates are wired for AI-authored changes.
- **NEEDS VERIFICATION** — whether public-boundary tests deny RAW/WORK/QUARANTINE/candidate/internal/model-output paths.

[Back to top](#top)

---

## Changelog

| Date | Change | Status |
|---|---|---|
| 2026-07-08 | Replaced empty placeholder with workflow-subtree README. | **CONFIRMED README / workflow behavior NEEDS VERIFICATION** |
