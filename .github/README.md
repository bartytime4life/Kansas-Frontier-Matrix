<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/github-folder-readme
title: .github — GitHub Platform Governance Hooks
type: standard
version: v1.1
status: draft
owners: <repo stewards · governance reviewers · CI maintainers — placeholder, confirm via CODEOWNERS>
created: 2026-05-11
updated: 2026-05-22
policy_label: public
related:
  - ../directory-rules.md
  - ../docs/doctrine/ai-build-operating-contract.md
  - ../docs/registers/AUTHORITY_LADDER.md
  - ../docs/registers/DRIFT_REGISTER.md
  - ../docs/registers/VERIFICATION_BACKLOG.md
  - ../CODEOWNERS
  - ../policy/
  - ../tools/validators/
  - ../release/
  - ../infra/
tags: [kfm, governance, ci, github, infra, policy-parity, starter-pack]
notes:
  - "Folder role as a canonical root is CONFIRMED by directory-rules.md §5; folder contents (workflows, CODEOWNERS body, templates) remain PROPOSED until verified against a mounted repository."
  - "Workflow filenames inside are sourced from KFM design reports (Whole-UI + Governed-AI Expansion, Pass-10 idea C14-01) and from Unified Manual §25 CI/CD lanes; only `integrity.yml`, `ui-governed.yml`, and `contracts-ui-ai.yml` are CONFIRMED in source — the remaining filenames are author-chosen and SHOULD be frozen via ADR before branch protection references them."
  - "MetaBlock v2 fields follow atlas card KFM-P22-PROG-0002 (release-anchor MetaBlock v2)."
[/KFM_META_BLOCK_V2] -->

<p align="center">
  <img src="../docs/brand/logo/The-Kansas-Frontier-Matrix-Seal-transparent-cropped.png" alt="Kansas Frontier Matrix Seal — transparent crop" width="240" />
</p>

# `.github/` — GitHub Platform Governance Hooks

> Workflows, templates, and platform hooks that turn KFM governance doctrine — Directory Rules, the seven-gate matrix, evidence-first promotion, policy-as-code, the five-file starter pack — into enforceable, observable signals on every push, pull request, and release dry-run.

![Authority](https://img.shields.io/badge/authority-canonical%20root-1f4f8f)
![Status](https://img.shields.io/badge/status-PROPOSED%20contents-orange)
![Doctrine](https://img.shields.io/badge/doctrine-Directory%20Rules%20%C2%A75%20%C2%B7%20%C2%A715%20%C2%B7%20%C2%A720-2b6cb0)
![Gates](https://img.shields.io/badge/gates-A%E2%80%93G%20fail--closed-2f855a)
![Policy parity](https://img.shields.io/badge/CI%20%3D%20Runtime-policy%20parity-805ad5)
![Starter pack](https://img.shields.io/badge/C14--01-five--file%20starter%20pack-0b7285)
![Watcher-as-non-publisher](https://img.shields.io/badge/invariant-watcher--as--non--publisher-d97706)
![Last reviewed](https://img.shields.io/badge/last%20reviewed-2026--05--22-lightgrey)

**Status:** PROPOSED — folder *role* as a canonical root is **CONFIRMED** by `directory-rules.md` §5 and §20; the specific files, workflow names, branch-protection coupling, and CODEOWNERS body inside are **PROPOSED / NEEDS VERIFICATION** until inspected against a mounted repository.
**Owners:** `<repo stewards · governance reviewers · CI maintainers — placeholder, confirm via CODEOWNERS>`
**Last updated:** 2026-05-22

---

## Quick jump

- [Purpose](#purpose)
- [Authority level](#authority-level)
- [Status](#status)
- [What belongs here](#what-belongs-here)
- [What does NOT belong here](#what-does-not-belong-here)
- [Inputs](#inputs)
- [Outputs](#outputs)
- [Validation](#validation)
- [Review burden](#review-burden)
- [Related folders](#related-folders)
- [ADRs](#adrs)
- [Last reviewed](#last-reviewed)
- [Directory tree (PROPOSED)](#directory-tree-proposed)
- [How `.github/` sits in the canonical tree](#how-github-sits-in-the-canonical-tree)
- [Responsibility map](#responsibility-map)
- [Five-file governance starter pack (C14-01)](#five-file-governance-starter-pack-c14-01)
- [Workflow catalog (PROPOSED)](#workflow-catalog-proposed)
- [CI gate map (A–G)](#ci-gate-map-ag)
- [Cross-cutting requirements (all workflows)](#cross-cutting-requirements-all-workflows)
- [Adoption checklist](#adoption-checklist)
- [Anti-patterns specific to `.github/`](#anti-patterns-specific-to-github)
- [FAQ](#faq)
- [Open questions / NEEDS VERIFICATION](#open-questions--needs-verification)

---

## Purpose

`.github/` is the **canonical home for GitHub-platform-specific governance hooks** in the Kansas Frontier Matrix repository. It is the operational seam that wires KFM doctrine — Directory Rules, the seven-gate matrix, policy-as-code, evidence-first promotion, the five-file starter pack — into the day-to-day signals contributors see: workflows, required checks, code ownership, issue and pull-request templates, and dependency-intake configuration.

This folder **invokes** validators, policies, and tools that live elsewhere. It does **not** own their logic, schemas, or decisions. Workflows are glue; the trust membrane lives in `policy/`, `tools/validators/`, `schemas/`, `contracts/`, and `release/`.

> [!IMPORTANT]
> `.github/` is **infrastructure for governance**, not governance itself. A workflow that disagrees with `policy/` is drift — fix the policy or fix the workflow; do not let CI invent rules that doctrine has not authored.

---

## Authority level

**Canonical.** Listed in `directory-rules.md` §5 and §20 as a canonical root. The folder is governance-bearing in role (it operationalizes gates) but *compatibility-shaped* in convention: its directory layout is dictated by GitHub, not by KFM.

| Field | Value |
|---|---|
| Authority class | **Canonical** |
| Sub-class | **implementation-bearing** — workflows execute; they do not author truth |
| Governs | CI orchestration, code ownership, issue/PR intake, platform-level governance hooks |
| Does not govern | Policy decisions, schema shape, contract meaning, validator logic, release decisions, lifecycle data, source identity |

---

## Status

**CONFIRMED** as a canonical root by `directory-rules.md`.
**PROPOSED** for everything inside it in this session — file presence, workflow names, CODEOWNERS body, branch-protection coupling, and any specific check name. No mounted repository was inspected, so the actual contents of `.github/` are **UNKNOWN / NEEDS VERIFICATION**.

| Claim | Truth label |
|---|---|
| `.github/` is a canonical root | **CONFIRMED** (Directory Rules §5, §20) |
| `CODEOWNERS` may live at `.github/CODEOWNERS` *or* repo root | **CONFIRMED** (Directory Rules §5) |
| The seven-gate matrix (A–G) is doctrine | **CONFIRMED** (Pass-10 C5-01) |
| Default-deny promotion via signed receipts + DQ pass is doctrine | **CONFIRMED** (Pass-10 C5-02) |
| Policy parity (CI = runtime, same OPA bundle digest) is doctrine | **CONFIRMED** (Pass-10 C5-03) |
| Five-file starter pack + `integrity.yml` + `verify.sh` is doctrine | **CONFIRMED** (Pass-10 C14-01) |
| Watcher-as-non-publisher is invariant | **CONFIRMED** (Master MapLibre v2.0; doctrine synthesis §27) |
| Workflow files named below exist on disk | **UNKNOWN / NEEDS VERIFICATION** |
| Branch protection currently enforces the gates listed here | **NEEDS VERIFICATION** |
| The seven-gate matrix is enforced today in this repo | **PROPOSED** — doctrine confirmed; enforcement not verified |

---

## What belongs here

| Class | Path pattern | Role |
|---|---|---|
| GitHub Actions workflows | `.github/workflows/*.yml` | CI invocations of validators, policies, gates, and release dry-runs. |
| Composite / reusable actions | `.github/actions/<name>/action.yml` | Repo-local action definitions reused by multiple workflows. |
| Code ownership | `.github/CODEOWNERS` *(or repo-root `CODEOWNERS`)* | Path-to-reviewer map enforced at PR review time. |
| Issue templates | `.github/ISSUE_TEMPLATE/*.yml` or `*.md` | Structured intake for bugs, drift entries, ADR proposals, verification-backlog items. |
| Pull request template | `.github/PULL_REQUEST_TEMPLATE.md` *(or `PULL_REQUEST_TEMPLATE/`)* | Required PR description scaffold: cited Directory Rules section, gate impact, rollback target, AI-receipt link (see `ai-build-operating-contract.md` §27.1, §47). |
| Dependency-intake config | `.github/dependabot.yml` | Pinned-toolchain dependency updates as reviewable PRs. |
| Funding metadata | `.github/FUNDING.yml` | Optional; community/funding pointers. |
| Discussion templates | `.github/DISCUSSION_TEMPLATE/*.yml` | Optional; community discussion intake. |
| Folder README | `.github/README.md` | **This file.** Required by Directory Rules §15. |

> [!NOTE]
> `CODEOWNERS` MAY live at `.github/CODEOWNERS` or at repo root. The canonical tree in Directory Rules §5 shows both options. Choose one home, document the choice here, and do **not** maintain two copies.

---

## What does NOT belong here

| Misplacement | Belongs in | Why |
|---|---|---|
| Validator logic (Python/Node code) | `tools/validators/` | Workflows invoke validators; they do not contain them. |
| Policy bundles (Rego, JSON policy) | `policy/` (with `policies/` only as compatibility mirror) | Policy is authored, versioned, and reviewed in `policy/`; CI references it by digest. |
| Schemas | `schemas/contracts/v1/...` per ADR-0001 default | Schema authority is `schemas/`. |
| Contracts (object meaning) | `contracts/` | Semantic Markdown belongs there. |
| Release manifests, decisions, rollback cards | `release/` | Trust-bearing release artifacts. |
| Run receipts, proofs, evidence bundles | `data/receipts/`, `data/proofs/` | Lifecycle data and emitted proof. |
| Deployment manifests, infra config | `infra/` | Hosting, network, exposure posture. |
| Executable pipeline logic / declarative pipeline specs | `pipelines/` and `pipeline_specs/` | Workflows may *trigger* pipelines; they do not *contain* pipeline logic. |
| Documentation prose / ADRs / runbooks | `docs/` | Human-facing control plane. |
| `SECURITY.md` (the public security policy) | Repo root | Directory Rules §5 places `SECURITY.md` at root. A `.github/SECURITY.md` mirror is permitted only with explicit justification. |
| Test fixtures | `fixtures/` or `tests/fixtures/` | Workflows reference fixtures; they do not store them. |
| Source descriptors, source registry entries | `data/registry/sources/`, `data/registry/source_descriptors/` | Source identity is lifecycle data, not CI config. |

> [!WARNING]
> A workflow that embeds policy logic inline — Rego, allow/deny lists, license allowlists, sensitivity rules — is **drift**. The workflow MUST load these from `policy/` so that **CI parity (gate C, Pass-10 C5-03)** holds: CI and runtime MUST evaluate the same policy bundle digest.

---

## Inputs

Files in `.github/` are authored by stewards and reviewed by CODEOWNERS. They reference:

- **`tools/validators/`** — workflows shell out to repo-wide validators (schema, evidence, lifecycle, source, sensitivity, citation, geometry, geo manifest). *PROPOSED inventory.*
- **`policy/`** — Conftest/OPA decisions, license allowlists, sensitivity gates, promotion rules.
- **`schemas/contracts/v1/...`** — for schema-validation jobs.
- **`fixtures/`** and **`tests/fixtures/`** — for validator and policy fixture suites (positive and negative).
- **`tests/`** — unit, contract, end-to-end, accessibility, and finite-outcome tests.
- **`docs/registers/`** — drift, verification, lineage, and authority registers referenced from PR templates and CODEOWNERS comments.
- **`release/`** — release dry-run and rollback workflows reference release manifests and rollback cards.
- **`infra/`** — for **C5-03** policy-parity coupling (CI and runtime MUST reference the same OPA bundle digest).

---

## Outputs

`.github/` emits **signals**, not trust-bearing artifacts:

- **Check Runs and status checks** on PRs and pushes (consumed by branch protection).
- **Workflow logs and annotations** — advisory; the source of truth remains the validator/receipt/policy output, not the log line.
- **PR comments** from bot workflows (drift summaries, gate rollups, **deterministic obligations** on policy-gated publish failure per Pass-23 idea KFM-P17-FEAT-0001, AI-patch reviews).
- **Triggered downstream jobs** — `repository_dispatch`, `workflow_dispatch`, or reusable workflow calls into `tools/` and `pipelines/`.

Workflows MUST NOT emit release decisions, receipts, proofs, or catalog updates as their **sole** output. Those belong in `data/receipts/`, `data/proofs/`, `release/`, and `data/catalog/` — written by the tools the workflow invoked, not by the workflow file itself. This preserves the **watcher-as-non-publisher** invariant.

> [!IMPORTANT]
> The CI signal is *evidence that the gate ran*. The CI signal is **not** the gate. Auditors must be able to recompute the same result on a clean local checkout via a `verify.sh`-style script (Pass-10 C14-01).

---

## Validation

The contents of `.github/` are themselves checked:

1. **Workflow lint** — `actionlint` (or equivalent) over `.github/workflows/*.yml`. *PROPOSED.*
2. **CODEOWNERS lint** — GitHub validates CODEOWNERS on push; CI MAY run a coverage check that fails when canonical roots lack owners.
3. **Path / drift scan** — repo-wide Directory Rules check (§16 reviewer checklist, mechanized). *PROPOSED — depends on `tools/validators/path_role/` once it exists.*
4. **Pinned action digests** — every `uses:` MUST pin a commit SHA, not a floating tag. Aligns with Pass-10 C13 tool-pinning.
5. **Policy parity check** — verify the OPA bundle digest referenced in any workflow matches the bundle digest referenced in `infra/` deployment manifests (Pass-10 C5-03).
6. **Branch-protection coupling** — required-check names MUST match the names branch protection requires. **NEEDS VERIFICATION** against current repository settings.
7. **Kill-switch presence** — every long-running or write-emitting workflow SHOULD honor a named env-var kill-switch (e.g., `KFM_<PIPELINE>_KILL=true`) per atlas card KFM-P8-PROG-0005, producing an explicit "kill-switch activated" outcome rather than a silent skip.

---

## Review burden

Changes under `.github/` require review by:

- **The owner(s) named in `CODEOWNERS`** for the affected path.
- **CI maintainers** for any new workflow, action, or branch-protection-relevant rename.
- **Governance reviewers** when the change affects required checks, CODEOWNERS coverage, PR-template gating, issue-intake routing, or any gate in the A–G matrix.
- **Subsystem owners** when a workflow's job affects their subsystem (UI, governed AI, contracts, schemas, policy, release, infra).

A workflow rename or check-name change that breaks branch protection MUST land with a coordinated update to repository settings; otherwise required checks become unmatchable and merges silently block.

---

## Related folders

| Folder | Relationship |
|---|---|
| [`../policy/`](../policy/) | Source of truth for allow / deny / restrict / abstain decisions. Workflows reference policy by digest. |
| [`../tools/validators/`](../tools/validators/) | Validator logic invoked by workflows. |
| [`../schemas/`](../schemas/) | Schema authority (`schemas/contracts/v1/...` per ADR-0001 default). |
| [`../contracts/`](../contracts/) | Object-family meaning (semantic Markdown). |
| [`../tests/`](../tests/) | Test suites invoked by CI. |
| [`../fixtures/`](../fixtures/) | Fixture inputs to validator and policy suites. |
| [`../release/`](../release/) | Release decisions; dry-run workflows reference manifests here. |
| [`../infra/`](../infra/) | Deployment manifests; policy-parity coupling lives here. |
| [`../docs/registers/AUTHORITY_LADDER.md`](../docs/registers/AUTHORITY_LADDER.md) | Authority order CI helps enforce. |
| [`../docs/registers/DRIFT_REGISTER.md`](../docs/registers/DRIFT_REGISTER.md) | Where drift between workflows and doctrine is recorded. |
| [`../docs/registers/VERIFICATION_BACKLOG.md`](../docs/registers/VERIFICATION_BACKLOG.md) | NEEDS-VERIFICATION items, including branch-protection coupling. |
| [`../docs/doctrine/directory-rules.md`](../docs/doctrine/directory-rules.md) | The doctrine this folder operationalizes (placement authority). |
| [`../docs/doctrine/ai-build-operating-contract.md`](../docs/doctrine/ai-build-operating-contract.md) | PR-body minimum (§27.1), companion-artifacts table (§47), adoption checklist (§48). |
| [`../CODEOWNERS`](../CODEOWNERS) *or* [`./CODEOWNERS`](./CODEOWNERS) | Path-to-reviewer map. Confirm the chosen home. |

---

## ADRs

The ADRs relevant to this folder are listed below. **All listed ADR IDs except ADR-0001 are PROPOSED placeholders** until a mounted `docs/adr/` confirms them.

| ADR | Topic | Why it touches `.github/` |
|---|---|---|
| **ADR-0001** *(referenced in Directory Rules)* | Schema home — default `schemas/contracts/v1/...` | Schema-validation workflows MUST target the canonical home. |
| **ADR-CI-PARITY** *(PROPOSED)* | Policy parity — CI bundle digest equals runtime bundle digest | C5-03 enforcement; coupling between this folder and `infra/`. |
| **ADR-REQUIRED-CHECKS** *(PROPOSED)* | Pinning required-check names to branch protection | Prevents silent-block drift between workflow renames and protection rules. |
| **ADR-STARTER-PACK** *(PROPOSED)* | Five-file governance starter pack + `integrity.yml` + `verify.sh` | C14-01 minimum viable governance posture. |
| **ADR-AI-RECEIPT-GATE** *(PROPOSED)* | CI check requiring `GENERATED_RECEIPT.json` on every AI-authored merge | Operating-contract §34, §48 adoption checklist. |

> [!NOTE]
> No ADR has been verified in this session. Mounted-repo inspection is required to confirm ADR numbers, acceptance state, and supersession links.

---

## Last reviewed

**2026-05-22.** Older than six months from this date → flag for review per Directory Rules §15.

[Back to top](#github--github-platform-governance-hooks)

---

## Directory tree (PROPOSED)

> [!CAUTION]
> The tree below is **PROPOSED**. It synthesizes the canonical-root role from `directory-rules.md` with workflow names that appear in KFM design reports (Whole-UI + Governed-AI Expansion §29–§30; Pass-10 idea C14-01) and CI lanes from the Unified Implementation Manual §25. It does **not** describe the current state of any mounted repository.

```text
.github/
├── README.md                                # this file (Directory Rules §15)
├── CODEOWNERS                                # OR at repo root — choose one
├── PULL_REQUEST_TEMPLATE.md                  # PROPOSED — renders operating-contract §27.1 PR-body
├── dependabot.yml                            # PROPOSED — pinned-toolchain intake
├── FUNDING.yml                               # OPTIONAL
├── ISSUE_TEMPLATE/
│   ├── bug_report.yml                        # PROPOSED
│   ├── drift_entry.yml                       # PROPOSED — feeds docs/registers/DRIFT_REGISTER.md
│   ├── verification_item.yml                 # PROPOSED — feeds docs/registers/VERIFICATION_BACKLOG.md
│   ├── adr.md                                # PROPOSED — operating-contract §28 ADR skeleton
│   └── config.yml                            # PROPOSED — intake routing
├── DISCUSSION_TEMPLATE/                      # OPTIONAL
├── actions/                                  # PROPOSED — composite / reusable actions
│   └── <action-name>/action.yml
└── workflows/
    ├── integrity.yml                         # CONFIRMED filename in source — C14-01 starter-pack workflow
    ├── path-and-drift.yml                    # PROPOSED — Directory Rules §16 mechanized
    ├── contracts-ui-ai.yml                   # CONFIRMED filename in source — schema + fixture + policy validation
    ├── ui-governed.yml                       # CONFIRMED filename in source — PR-safe UI validation
    ├── policy-parity.yml                     # PROPOSED — C5-03 CI = runtime digest check
    ├── promotion-dry-run.yml                 # PROPOSED — release gate dry-run, no public effect
    ├── catalog-closure.yml                   # PROPOSED — PROV / STAC / DCAT closure check
    ├── signing-integrity.yml                 # PROPOSED — RunReceipt / spec_hash / digest verify
    └── rollback-drill.yml                    # PROPOSED — rollback card replay
```

---

## How `.github/` sits in the canonical tree

```mermaid
flowchart LR
    classDef canon fill:#e6f0fb,stroke:#1f4f8f,color:#0b2545,stroke-width:1.2px;
    classDef hook fill:#fff5e6,stroke:#b25900,color:#5a3500,stroke-width:1.4px;
    classDef result fill:#f3eaf9,stroke:#6b21a8,color:#3b1361,stroke-width:1.2px;
    classDef reg fill:#eef7ee,stroke:#2f7d32,color:#1b3b1c,stroke-width:1.2px;

    GH[".github/<br/>workflows · templates · CODEOWNERS"]:::hook

    POL["policy/<br/>OPA bundle (digest-pinned)"]:::canon
    TLS["tools/validators/<br/>schema · evidence · source · sensitivity · geometry"]:::canon
    SCH["schemas/contracts/v1/<br/>machine shape"]:::canon
    FIX["fixtures/ &amp; tests/fixtures/<br/>positive + negative"]:::canon
    REL["release/<br/>manifests · rollback · correction"]:::canon
    INF["infra/<br/>deployment manifests"]:::canon

    DAT["data/receipts/ · data/proofs/<br/>(written by tools, not by workflows)"]:::result
    CHK["Check Runs<br/>required by branch protection"]:::result
    REG["docs/registers/<br/>DRIFT · VERIFICATION · LINEAGE"]:::reg

    POL -- "digest" --> GH
    TLS -- "invoked by" --> GH
    SCH -- "validated against" --> GH
    FIX -- "fed into" --> GH
    REL -- "dry-run target" --> GH
    INF -- "must match policy digest" --> GH

    GH --> CHK
    GH -- "triggers validators that emit" --> DAT
    GH -- "intake templates feed" --> REG
```

[Back to top](#github--github-platform-governance-hooks)

---

## Responsibility map

| Responsibility | Lives in | `.github/` role |
|---|---|---|
| Decide allow / deny / restrict / abstain | `policy/` | **Reference** the bundle by digest; never inline rules. |
| Define object meaning | `contracts/` | **Validate** that PRs touching contracts pair with schema and fixture changes. |
| Define machine shape | `schemas/` | **Invoke** schema-validation jobs over `schemas/contracts/v1/` + fixtures. |
| Prove a rule is enforceable | `tests/` | **Run** unit / contract / e2e / accessibility / finite-outcome suites. |
| Repo-wide validator logic | `tools/validators/` | **Shell out** to validators; never duplicate logic in YAML. |
| Release decisions | `release/` | **Dry-run** release gates; never publish from CI alone. |
| Receipts, proofs, manifests | `data/receipts/`, `data/proofs/`, `release/manifests/` | **Written by tools** the workflow invokes, not by the workflow file. |
| Deployment posture | `infra/` | **Parity check** — CI and infra reference the same bundle digest. |
| Source identity, rights, sensitivity | `data/registry/`, `policy/sensitivity/` | **Validate** that source-bearing PRs cite a descriptor and policy tier. |
| Human explanation | `docs/` | **Linked** from PR templates, issue templates, CODEOWNERS comments. |

---

## Five-file governance starter pack (C14-01)

> [!IMPORTANT]
> Pass-10 idea **C14-01** (CONFIRMED) defines the minimum viable governance posture for any KFM-governed repository: **five files + one workflow + one script**. Of these, only `CODEOWNERS` and `integrity.yml` live under `.github/`. The remaining files live in their canonical homes so they remain inspectable to runtime, not just to CI.

| Starter-pack item | Canonical home | `.github/` involvement |
|---|---|---|
| `CODEOWNERS` | `.github/CODEOWNERS` *or* repo root | **Yes** — path-to-reviewer enforcement at PR review time. |
| `tool-versions.yaml` | `configs/` or repo root | Referenced by `integrity.yml` to pin the toolchain (C13-01). |
| `policy-bundle.json` | `policy/` (digest-pinned) | Referenced by every policy-evaluating workflow (C5-03 parity). |
| `sbom.yaml` | `release/` or repo root | Generated by build; verified by `signing-integrity.yml`. |
| `run_receipt.schema.json` | `schemas/contracts/v1/receipts/` | Validated against in `signing-integrity.yml`. |
| `integrity.yml` *(CI workflow)* | **`.github/workflows/integrity.yml`** | **Yes** — runs `verify.sh` on every push and PR. |
| `verify.sh` *(local script)* | `scripts/dev/` or `tools/` | Local-reproducibility script; CI invokes the same script. |

A KFM repository missing any of these surfaces governance-by-convention, which drifts. With them, governance is enforced by files that CI reads and the developer can inspect locally.

---

## Workflow catalog (PROPOSED)

> [!NOTE]
> Every row below is **PROPOSED**. Three filenames — `integrity.yml`, `ui-governed.yml`, and `contracts-ui-ai.yml` — are explicitly named in KFM source material (Pass-10 C14-01; Whole-UI + Governed-AI Expansion §30). The remaining filenames are author-chosen names that map one-to-one onto the CI/CD lanes listed in Unified Manual §25; an ADR or working-group decision SHOULD freeze final names before they enter branch protection.

| Workflow | Trigger | Purpose | Gate(s) | Source for the filename / lane |
|---|---|---|---|---|
| `integrity.yml` | push, pull_request | Run `verify.sh`; same checks locally and in CI | A, B, C, F | C14-01 (filename CONFIRMED in source) |
| `path-and-drift.yml` | pull_request | Mechanize Directory Rules §16 reviewer checklist; flag root creation, schema-home drift, trust-content placement | A | Unified Manual §25 lane "Path and drift scan" (filename author-chosen) |
| `contracts-ui-ai.yml` | pull_request | Schema, fixture, and policy validation for UI + governed-AI surfaces | B, C | Whole-UI Expansion §30 (filename CONFIRMED in source) |
| `ui-governed.yml` | pull_request | PR-safe UI validation: schema / component / e2e / a11y | B, C, G | Whole-UI Expansion §30 (filename CONFIRMED in source) |
| `policy-parity.yml` | pull_request | C5-03 check — CI bundle digest equals runtime bundle digest | C | C5-03 (filename author-chosen) |
| `promotion-dry-run.yml` | pull_request, workflow_dispatch | Run promotion gates without public effect | A–F | Unified Manual §25 lane "Promotion dry-run" (filename author-chosen) |
| `catalog-closure.yml` | pull_request | Validate PROV / STAC / DCAT-style closure | F | Unified Manual §25 lane "Catalog closure" (filename author-chosen) |
| `signing-integrity.yml` | pull_request, push | Verify RunReceipt, spec_hash, digest, Merkle patterns | F | Unified Manual §25 lane "Signing / integrity" + C1-02 (filename author-chosen) |
| `rollback-drill.yml` | workflow_dispatch, schedule | Replay rollback card against a dry-run release | F, G | KFM Encyclopedia PR-10 (filename author-chosen) |

---

## Cross-cutting requirements (all workflows)

> [!WARNING]
> These requirements apply to **every** workflow in `.github/workflows/`. A workflow that violates any of them should fail the `path-and-drift.yml` lint or `actionlint` policy before it can merge.

- **No-network default** for the first PR pipeline. Live connectors, external endpoints, package-version probes, and runtime smoke tests are **opt-in, source-activated** jobs. *(Unified Manual §25; operating-contract §24.2.)*
- **Fail-closed.** Absent evidence blocks promotion. *(Pass-10 C5-02; default-deny posture.)*
- **Pinned actions.** Every `uses:` references a commit SHA, never a floating tag. *(C13-01.)*
- **Watcher-as-non-publisher.** Workflows MUST NOT write canonical truth, mutate catalogs, or publish directly. They emit candidate decisions and receipts only. *(Master MapLibre v2.0 anti-pattern register; doctrine synthesis §27.)*
- **Kill-switch honored.** Every long-running or write-emitting workflow SHOULD honor a named env-var kill-switch (`KFM_<PIPELINE>_KILL=true`), producing an explicit "kill-switch activated" outcome rather than a silent skip. *(KFM-P8-PROG-0005.)*
- **Deterministic obligations.** On a policy-gated publish failure, the workflow SHOULD post a deterministic obligations comment back to the PR enumerating which gate, which fixture, and which evidence is missing. *(KFM-P17-FEAT-0001.)*
- **MetaBlock v2 release anchor.** Workflows that emit release candidates MUST verify the candidate carries a MetaBlock v2 with `doc_id`, `owner`, `status`, `policy_label`, `spec_hash`, and `related` catalog references. *(KFM-P22-PROG-0002.)*
- **AI-receipt enforcement.** If any file in the diff was AI-authored, the merge MUST be gated by `GENERATED_RECEIPT.json` presence and well-formedness. *(operating-contract §34, §48.)*

---

## CI gate map (A–G)

The seven-gate matrix is **CONFIRMED doctrine** (Pass-10 C5-01). Its **current enforcement** in this repo is **PROPOSED / NEEDS VERIFICATION** until branch protection and workflow inventory are inspected.

| Gate | Intent | Required evidence | CI surface |
|---|---|---|---|
| **A** Structure & Metadata | MetaBlock presence, zone correctness, path-role validity | Path/drift scan + MetaBlock check | `path-and-drift.yml` *(PROPOSED)* |
| **B** Schemas & Contracts | Object conforms to schema + contract vocabulary | jsonschema/ajv over `schemas/contracts/v1/` and fixtures | `contracts-ui-ai.yml`, `ui-governed.yml` *(PROPOSED)* |
| **C** Policy Parity | CI and runtime decide on the same OPA bundle digest | Conftest/OPA against pinned bundle | `policy-parity.yml`, `integrity.yml` *(PROPOSED)* |
| **D** Security & Sensitivity | Rights, sensitivity, license allowlist, secret hygiene | SPDX allowlist + sensitivity classifier + secret scan | *(integrated in `integrity.yml`; PROPOSED)* |
| **E** Data Quality | DQ profilers, assertions, threshold pass | DQ check outputs with `status: pass` | *(integrated in `promotion-dry-run.yml`; PROPOSED)* |
| **F** Provenance & Lineage | RunReceipt, spec_hash, signed bundle, catalog closure | Receipt verification + closure check | `signing-integrity.yml`, `catalog-closure.yml` *(PROPOSED)* |
| **G** Reviewability | CODEOWNERS + two-key approval + policy approval | GitHub review + policy decision | branch protection + `CODEOWNERS` + policy webhook *(NEEDS VERIFICATION)* |

> [!IMPORTANT]
> **Required-check names** in branch protection MUST exactly match the workflow job names listed here. A rename without a coordinated protection update results in **silent merge blocks**. This coupling is **NEEDS VERIFICATION** against current GitHub repository settings.

[Back to top](#github--github-platform-governance-hooks)

---

## Adoption checklist

> [!TIP]
> Distilled from `ai-build-operating-contract.md` §48 (CONFIRMED authored in attached corpus; mounted-repo presence NEEDS VERIFICATION). Tick items as a mounted repo is inspected.

```text
[ ] CODEOWNERS placed at .github/CODEOWNERS OR repo root (pick one; document choice in this README)
[ ] .github/workflows/integrity.yml present and invokes verify.sh
[ ] scripts/dev/verify.sh (or tools/verify.sh) reproduces CI signal locally
[ ] .github/PULL_REQUEST_TEMPLATE.md renders operating-contract §27.1 PR-body
[ ] .github/ISSUE_TEMPLATE/adr.md renders operating-contract §28 ADR skeleton
[ ] .github/ISSUE_TEMPLATE/drift_entry.yml feeds docs/registers/DRIFT_REGISTER.md
[ ] .github/ISSUE_TEMPLATE/verification_item.yml feeds docs/registers/VERIFICATION_BACKLOG.md
[ ] dependabot.yml (or Renovate config) present and reviewed (choose one; not both)
[ ] Branch protection required-check names match workflow job names
[ ] OPA bundle digest pinned identically in CI workflows and infra/ manifests (C5-03)
[ ] Every `uses:` in workflows pinned to a commit SHA (no floating tags)
[ ] No workflow embeds policy logic, allow/deny lists, or license allowlists inline
[ ] No workflow writes canonical truth, mutates catalogs, or publishes directly
[ ] CI check enforces GENERATED_RECEIPT.json on every AI-authored merge (§34)
[ ] no-direct-model-client and no-public-raw-path tests are wired in
[ ] Drift between workflow filename and required-check name → DRIFT_REGISTER.md entry
```

[Back to top](#github--github-platform-governance-hooks)

---

## Anti-patterns specific to `.github/`

Beyond the placement anti-patterns in Directory Rules §13, these failure modes are specific to this folder:

| Anti-pattern | Symptom | Fix |
|---|---|---|
| **Policy inlined in YAML** | `allowlist:`, `deny:`, license lists embedded directly in workflow steps | Move to `policy/`; workflow references by digest. Restores C5-03 parity. |
| **Floating action tags** | `uses: actions/checkout@v4` instead of a pinned SHA | Pin to commit SHA; updates land as reviewable PRs. |
| **Required-check drift** | Workflow renamed; branch protection still requires the old name | Rename and update protection in the same PR; ADR if the rename is structural. |
| **Workflow as publisher** | A workflow `git push`-es to `data/published/`, `data/catalog/`, or `release/` | Watcher-as-non-publisher invariant broken. Workflows emit receipts and candidate decisions; promotion is governed. |
| **CI-only validator** | Validator logic lives only inside a workflow `run:` block | Extract to `tools/validators/`; CI calls into it. Restores local reproducibility (C14-01 `verify.sh`). |
| **CODEOWNERS without coverage** | A new canonical root lands without a CODEOWNERS line | CODEOWNERS-coverage check fails; block merge. |
| **Schema job pointing at a compatibility root** | Workflow validates `jsonschema/` instead of `schemas/contracts/v1/` | Compatibility roots are mirrors; canonical home is `schemas/`. |
| **PR template smoothing over governance** | PR template omits "Directory Rules section cited" or "rollback target" fields | Restore required fields per operating-contract §27.1; reviewers cannot waive them. |
| **Two CODEOWNERS files** | One at `.github/CODEOWNERS`, one at repo root | Pick one home; delete the other; note the choice here. |
| **Secret-bearing workflow on PRs from forks** | Workflow with elevated permissions triggered by `pull_request` from forks | Use `pull_request_target` only with care; default to least-privilege tokens. |
| **Silent kill-switch skip** | Workflow short-circuits with no labeled outcome when kill-switch is set | Emit an explicit "kill-switch activated" status (KFM-P8-PROG-0005). |
| **Missing AI receipt** | AI-authored PR merges without a `GENERATED_RECEIPT.json` | CI gate fails the merge; operating-contract §34 violation. |

---

## FAQ

<details>
<summary><strong>Why does <code>.github/</code> count as a canonical root if its layout is dictated by GitHub?</strong></summary>

Because **role** decides root membership, not naming flexibility. The folder carries repo-wide responsibility for CI orchestration, code ownership, and platform-level governance hooks — that is a canonical responsibility per Directory Rules §3. GitHub's naming conventions inside the folder are operational details, not authority questions.

</details>

<details>
<summary><strong>Where does <code>CODEOWNERS</code> belong — here or at repo root?</strong></summary>

Either is permitted by Directory Rules §5 ("may live in `.github/CODEOWNERS` instead"). Choose one home, document the choice in this README, and ensure tooling (CI, GitHub settings) points at the chosen path. Maintaining two copies is the anti-pattern.

</details>

<details>
<summary><strong>Why not put validators or policy bundles in <code>.github/</code>?</strong></summary>

Because they have canonical homes — `tools/validators/` and `policy/` respectively — and because **policy parity (C5-03)** requires CI and runtime to evaluate the same bundle. If the bundle lived in `.github/`, runtime could not reference it without `.github/` becoming a parallel authority, which violates the "no parallel authority" rule in Directory Rules §13.

</details>

<details>
<summary><strong>Can a workflow publish a release?</strong></summary>

No, not autonomously. A workflow MAY *trigger* a release pipeline whose output is a `ReleaseManifest` under `release/manifests/`, but the release decision is governed: it requires receipts, proof closure, source-activation evidence, policy approval, and (gate G) reviewer approval. The **watcher-as-non-publisher** invariant means workflows emit candidate decisions and receipts; humans (or reviewed gates) promote.

</details>

<details>
<summary><strong>What happens if branch protection requires a check that no workflow produces?</strong></summary>

PRs become unmergeable until either (a) the missing check is produced or (b) branch protection is updated. Either change is a governance event — record it in `docs/registers/DRIFT_REGISTER.md` and resolve via PR + reviewer sign-off. An ADR is needed only if the gate matrix itself changes.

</details>

<details>
<summary><strong>How does this folder relate to the five-file governance starter pack (C14-01)?</strong></summary>

See [Five-file governance starter pack (C14-01)](#five-file-governance-starter-pack-c14-01) above. Briefly: only `CODEOWNERS` and `integrity.yml` live under `.github/`. The remaining starter-pack files — `tool-versions.yaml`, `policy-bundle.json`, `sbom.yaml`, `run_receipt.schema.json` — live in their canonical homes so runtime can reference them, not just CI. `verify.sh` lives in `scripts/dev/` (or `tools/`) so developers can reproduce the CI signal locally.

</details>

<details>
<summary><strong>How do PR templates and issue templates contribute to governance?</strong></summary>

PR templates require contributors to cite the Directory Rules section justifying any path change (§4 Step 5), name affected gates, identify a rollback target, and (for AI-authored work) link a `GENERATED_RECEIPT.json`. Operating-contract §27.1 defines the required PR-body shape; §47 names the companion artifacts (PR template at `.github/PULL_REQUEST_TEMPLATE.md`; ADR issue template at `.github/ISSUE_TEMPLATE/adr.md`). Issue templates route intake into the right register: bug reports, drift entries, ADR proposals, and verification-backlog items each have their own form so reviewers see structured input, not free-form prose.

</details>

<details>
<summary><strong>What is a "deterministic obligations comment"?</strong></summary>

When a policy-gated publish or promotion gate fails in CI, the workflow SHOULD post a comment back to the PR that enumerates — deterministically, without free-form prose — which gate failed, which fixture or evidence is missing, and the specific remediation step. The comment is reproducible from the same inputs and avoids "look at the logs" handoffs. *(KFM-P17-FEAT-0001, PROPOSED.)*

</details>

<details>
<summary><strong>Do workflows need a kill-switch?</strong></summary>

Long-running or write-emitting workflows SHOULD. The pattern: read a named env var (e.g., `KFM_NWIS_KILL=true`) as the workflow's first step, and abort with an explicit "kill-switch activated" outcome if set. A repo-level `.kfm/kill-switch.yml` MAY centralize emergency shutdown. The point is to make pauses *visible* — an outage with a paper trail, not a silent skip. *(KFM-P8-PROG-0005, CONFIRMED.)*

</details>

---

## Open questions / NEEDS VERIFICATION

These items SHOULD be tracked in `docs/registers/VERIFICATION_BACKLOG.md`:

- **NEEDS VERIFICATION** — Whether `.github/` exists in the current mounted repo and which of the workflows listed above are present.
- **NEEDS VERIFICATION** — Whether `CODEOWNERS` lives at `.github/CODEOWNERS` or repo root in the current repo. Doctrine permits either; the repo MUST pick one.
- **NEEDS VERIFICATION** — Current branch-protection rules: which check names are required, on which branches, for which event types.
- **NEEDS VERIFICATION** — Whether the OPA bundle digest is pinned identically in CI workflows and `infra/` deployment manifests (C5-03 parity).
- **NEEDS VERIFICATION** — Whether action SHA-pinning is enforced (a `path-and-drift.yml` rule or `actionlint` policy).
- **NEEDS VERIFICATION** — Whether any workflow currently writes to `data/published/`, `data/catalog/`, or `release/manifests/` (watcher-as-non-publisher audit).
- **NEEDS VERIFICATION** — Whether the AI-receipt gate is wired in CI per operating-contract §34, §48.
- **OPEN** — Should `dependabot.yml` and Renovate co-exist, or is one canonical?
- **OPEN** — Should `SECURITY.md` live at repo root only, or also be mirrored at `.github/SECURITY.md`? Doctrine places it at root; GitHub renders either.
- **OPEN** — Which OIDC issuers belong on the cosign verifier's allowlist for KFM — GitHub Actions OIDC, an in-house issuer, or both? *(Pass-10 C1-03.)*
- **OPEN** — Should the starter-pack files be vendored per repo, centrally generated, or remote-included? *(Pass-10 C14-01.)*
- **OPEN** — Final workflow filenames for the author-chosen names in the [Workflow catalog](#workflow-catalog-proposed); freeze via ADR-REQUIRED-CHECKS before they enter branch protection.

---

> **Conformance note.** This README is governance content. Material changes to its mandatory sections (Directory Rules §15) follow the change discipline in Directory Rules §17. Adding or renaming a canonical workflow whose check is required by branch protection requires a coordinated update; see [Open questions](#open-questions--needs-verification).

**Related docs:** [`directory-rules.md`](../docs/doctrine/directory-rules.md) · [`ai-build-operating-contract.md`](../docs/doctrine/ai-build-operating-contract.md) · [`docs/registers/AUTHORITY_LADDER.md`](../docs/registers/AUTHORITY_LADDER.md) · [`docs/registers/DRIFT_REGISTER.md`](../docs/registers/DRIFT_REGISTER.md) · [`docs/registers/VERIFICATION_BACKLOG.md`](../docs/registers/VERIFICATION_BACKLOG.md) · [`policy/README.md`](../policy/README.md) · [`tools/validators/README.md`](../tools/validators/README.md) · [`release/README.md`](../release/README.md)

**Last updated:** 2026-05-22 · **Status:** draft · **Version:** v1.1

[Back to top ↑](#github--github-platform-governance-hooks)
