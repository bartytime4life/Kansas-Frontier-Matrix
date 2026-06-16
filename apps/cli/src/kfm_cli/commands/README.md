<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://app/cli/src/kfm_cli/commands/readme
title: KFM CLI Commands README
type: app-readme
version: v0.1
status: draft
owners: OWNER_TBD — Apps steward · CLI steward · Release steward · Pipeline steward · Policy steward · Docs steward
created: 2026-06-16
updated: 2026-06-16
policy_label: restricted
related:
  - ../README.md
  - ../../../README.md
  - ../../../../README.md
  - ../../../../governed-api/README.md
  - ../../../../../policy/access/README.md
  - ../../../../../policy/decision/README.md
  - ../../../../../policy/data/README.md
  - ../../../../../packages/README.md
  - ../../../../../tools/README.md
  - ../../../../../scripts/README.md
  - ../../../../../release/README.md
  - ../../../../../data/README.md
  - ../../../../../docs/security/AUDIT_INVARIANTS.md
tags: [kfm, apps, cli, commands, operator-cli, validation, dry-run, diff, report, receipts, fail-closed]
notes:
  - "Initial README for the kfm_cli commands directory."
  - "Repository evidence confirms this README path; command modules and command inventory remain NEEDS VERIFICATION."
  - "Command modules may orchestrate governed checks and report generation, but they must not publish, bypass release, bypass lifecycle gates, bypass policy, or become shared-library homes."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

<div align="center">

# `kfm_cli.commands`

`apps/cli/src/kfm_cli/commands/`

**Command-family boundary for the KFM operator CLI: validation, dry-runs, ingest checks, diffs, reports, receipt inspection, and bounded maintenance commands.**

![status](https://img.shields.io/badge/status-draft-blue)
![owner](https://img.shields.io/badge/owner-OWNER__TBD-lightgrey)
![module](https://img.shields.io/badge/module-kfm__cli.commands-6f42c1)
![truth](https://img.shields.io/badge/truth-NEEDS__VERIFICATION-yellow)
![default](https://img.shields.io/badge/default-dry__run__first-d62728)

[Purpose](#1-purpose) · [Repo fit](#2-repo-fit) · [Boundary](#3-authority-boundary) · [Inputs](#5-inputs) · [Exclusions](#6-exclusions) · [Command families](#7-command-family-map) · [Definition of done](#14-definition-of-done)

</div>

---

> [!IMPORTANT]
> **Status:** draft / `NEEDS VERIFICATION`  
> **Owners:** `OWNER_TBD` — Apps steward · CLI steward · Release steward · Pipeline steward · Policy steward · Docs steward  
> **Path:** `apps/cli/src/kfm_cli/commands/README.md`  
> **Responsibility root:** `apps/` — deployable application surfaces  
> **Truth posture:** CONFIRMED README path / PROPOSED commands-directory contract / UNKNOWN command modules, exports, tests, fixtures, and entry-point wiring

> [!CAUTION]
> Command modules must not publish, promote, mutate lifecycle state, or approve release by themselves. A command may validate, inspect, diff, dry-run, request, or report; consequential transitions still require policy decisions, evidence closure, release authority, rollback support, and receipts.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Repo fit](#2-repo-fit)
- [3. Authority boundary](#3-authority-boundary)
- [4. Default posture](#4-default-posture)
- [5. Inputs](#5-inputs)
- [6. Exclusions](#6-exclusions)
- [7. Command family map](#7-command-family-map)
- [8. Diagram](#8-diagram)
- [9. Result vocabulary](#9-result-vocabulary)
- [10. Command obligations](#10-command-obligations)
- [11. Per-command README contract](#11-per-command-readme-contract)
- [12. Inspection path](#12-inspection-path)
- [13. Validation expectations](#13-validation-expectations)
- [14. Definition of done](#14-definition-of-done)
- [15. Open verification items](#15-open-verification-items)

---

## 1. Purpose

`apps/cli/src/kfm_cli/commands/` is the proposed home for long-lived KFM CLI command-family modules.

It should contain command code only after command inventory, tests, fixtures, receipt/report behavior, and parent CLI wiring are verified. This directory is for operator-facing commands that make governed work repeatable, reviewable, and auditable.

In scope:

- validation command families;
- release dry-run command families;
- ingest prerequisite checks;
- source, schema, contract, policy, package, data, and release diffs;
- redacted report generation;
- receipt/proof inspection;
- bounded maintenance command families.

Out of scope:

- shared reusable libraries;
- repo-wide validator implementations;
- release manifests and rollback cards;
- lifecycle artifacts and receipts as stored records;
- public API routes;
- temporary one-off scripts;
- secrets or private environment values.

[Back to top](#top)

---

## 2. Repo fit

| Concern | Owning root | Expected relationship |
|---|---|---|
| CLI command modules | `apps/cli/src/kfm_cli/commands/` | This README and future command-family modules, if accepted |
| CLI Python module | `apps/cli/src/kfm_cli/` | Parent Python module boundary and shared command utilities |
| CLI app contract | `apps/cli/README.md` | App-wide operator command surface and command-family posture |
| Public trust membrane | `apps/governed-api/` | Public clients use governed API, not CLI commands |
| Shared helpers | `packages/` | Extract reusable behavior here instead of command-private duplication |
| Validators / generators / builders | `tools/` | CLI may invoke, but should not fork validator authority |
| One-off scripts | `scripts/` | Temporary scripts; long-lived trust-bearing flows may graduate to CLI/tools/packages |
| Policy gates | `policy/` | Access, sensitivity, rights, data, and decision policy |
| Release authority | `release/` | Publication, correction, rollback control |
| Lifecycle artifacts | `data/` | Receipts, proofs, catalog, triplets, published artifacts |

## 3. Authority boundary

Command modules orchestrate governed work. They do not own the governance authorities they call.

```text
apps/cli/src/kfm_cli/commands/ = command-family modules
apps/cli/src/kfm_cli/          = CLI Python module boundary
apps/cli/                      = operator CLI deployable
apps/governed-api/             = public trust membrane
packages/                      = shared reusable implementation libraries
tools/                         = validators, generators, builders
policy/                        = finite policy decisions
schemas/                       = machine-readable shape
contracts/                     = object meaning
data/                          = lifecycle artifacts, receipts, proofs, registries
release/                       = publication, correction, rollback authority
```

## 4. Default posture

Commands should be dry-run-first and fail-closed.

A command should return `DENY`, `RESTRICT`, `HOLD`, `ABSTAIN`, or `ERROR` instead of acting when any of these are unresolved:

- target object or path;
- purpose or ticket/reference for consequential actions;
- actor/capability where required;
- source, schema, contract, policy, package, lifecycle, or release context;
- EvidenceRef / EvidenceBundle closure;
- validation report;
- output path and overwrite plan;
- receipt or audit destination;
- rollback or correction target for state-changing actions.

## 5. Inputs

| Input family | Examples | Required posture |
|---|---|---|
| Parsed command | command family, subcommand, flags, config profile, dry-run switch | Explicit and normalized |
| Actor context | operator, CI service identity, maintenance account | Required where consequential |
| Target context | source descriptor, schema, contract, policy bundle, package, data artifact, release candidate | Governed reference |
| Lifecycle context | RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, PUBLISHED, candidate release | Explicit before read/write |
| Policy context | access, rights, sensitivity, decision result, reason code | Required before action |
| Evidence context | EvidenceRef, EvidenceBundle, citation validation, proof pack | Required for claim-bearing checks |
| Output context | stdout mode, report path, receipt path, diff artifact path | Deterministic and safe |

## 6. Exclusions

| Does not belong here | Correct home |
|---|---|
| Shared libraries | `packages/` |
| Validator/generator/builder implementation authority | `tools/` |
| Temporary scripts | `scripts/` |
| Public API routes | `apps/governed-api/` |
| Admin or review UI panels | `apps/admin/`, `apps/review-console/` |
| Policy bundles | `policy/` |
| Schemas and contracts | `schemas/contracts/v1/`, `contracts/` |
| Stored lifecycle artifacts, receipts, proofs, catalog, triplets | `data/` |
| Release manifests, rollback cards, correction notices | `release/` |
| Credentials, tokens, private keys | Secure secret store / deployment environment |

## 7. Command family map

Exact modules remain `NEEDS VERIFICATION`. Candidate command families should be introduced only with tests and command inventory updates.

| Candidate family | Responsibility | Default posture | Status |
|---|---|---|---|
| `validate` | Run schema, contract, evidence, policy, package, or docs checks | Report/receipt; no publish | PROPOSED |
| `release_dry_run` | Assemble release readiness diagnostics | Dry-run only; requires rollback context | PROPOSED |
| `ingest_check` | Check source/admission prerequisites | Hold/quarantine unresolved sources | PROPOSED |
| `diff` | Compare governed artifacts, contracts, schemas, policies, or outputs | Read-only by default | PROPOSED |
| `report` | Produce maintainer/steward reports | Redacted output by default | PROPOSED |
| `receipts` | Inspect receipt/proof presence and linkage | Read-only, scoped display | PROPOSED |
| `maintenance` | Bounded upkeep tasks | Purpose, audit, and dry-run-first | PROPOSED |

> [!WARNING]
> Candidate command-family names are not implementation proof. Do not document a command as runnable until an entry point, tests, fixtures, and command help confirm it.

## 8. Diagram

```mermaid
flowchart TD
    main["kfm_cli main"] --> cmd["commands/<family>"]
    cmd --> context{"target + purpose + mode?"}
    context -->|no| hold["HOLD / ERROR"]
    context -->|yes| checks{"access + policy + evidence?"}
    checks -->|no| deny["DENY / ABSTAIN / HOLD"]
    checks -->|yes| mode{"dry-run/read-only?"}
    mode -->|yes| report["deterministic report + receipt ref"]
    mode -->|no| gate{"release/lifecycle gate supports action?"}
    gate -->|no| hold2["HOLD"]
    gate -->|yes| bounded["bounded action + receipt"]
```

## 9. Result vocabulary

| Result | Meaning | Required behavior |
|---|---|---|
| `ALLOW` | Command may proceed under scoped context | Emit report/receipt metadata where consequential |
| `DENY` | Access, sensitivity, rights, release, or lifecycle policy blocks command | Return safe reason code |
| `RESTRICT` | Command may proceed only as read-only, redacted, dry-run, or narrowed output | Preserve obligations |
| `HOLD` | Required target, evidence, validation, release, rollback, or receipt support is missing | Do not act |
| `ABSTAIN` | Command cannot decide because support is unresolved | Preserve unresolved handles safely |
| `ERROR` | Parse, dependency, filesystem, validation, or runtime failure | Fail closed with safe diagnostics |

## 10. Command obligations

| Obligation | Example effect |
|---|---|
| `dry_run_first` | Release/lifecycle-affecting commands start with dry-run behavior |
| `purpose_required` | Consequential commands require ticket, CI run, or review note |
| `receipt_required` | Consequential commands emit RunReceipt, ValidationReport, or equivalent references |
| `redaction_required` | Terminal and report output hide sensitive fields by default |
| `deterministic_output` | Reports and diffs use stable ordering and stable IDs where practical |
| `safe_failure_required` | Commands return finite safe outcomes and reason codes |
| `no_publish_shortcut` | Command module cannot publish without release authority |
| `no_authority_fork` | Commands invoke owning packages/tools/policies instead of redefining them |

## 11. Per-command README contract

Each command-family subdirectory or module should document:

- purpose;
- accepted inputs and required flags;
- read-only, dry-run, or state-changing class;
- owning package/tool/policy dependencies;
- output report and receipt behavior;
- safe failure modes;
- redaction behavior;
- rollback/correction relationship, when relevant;
- fixtures and tests.

## 12. Inspection path

Command modules, command inventory, tests, fixtures, package metadata, and CLI entry-point wiring remain `NEEDS VERIFICATION`.

```bash
find apps/cli/src/kfm_cli/commands -maxdepth 5 -type f | sort
find apps/cli apps packages tools scripts policy release data tests fixtures -maxdepth 5 -type f 2>/dev/null | grep -Ei 'command|validate|dry[-_ ]?run|ingest|diff|report|receipt|rollback|kfm_cli' | sort
find docs docs/runbooks docs/security -maxdepth 5 -type f 2>/dev/null | grep -Ei 'cli|operator|validation|release|rollback|audit' | sort
```

## 13. Validation expectations

Useful validation for this command lane should cover:

- unknown command family returns `ERROR` with safe help text;
- missing required target returns `HOLD` or `ERROR`;
- missing purpose for consequential command returns `HOLD`;
- missing role/access context returns `DENY` where required;
- release dry-run cannot write PUBLISHED state;
- report and diff output is deterministic and redacted by default;
- state-changing commands require rollback/correction support;
- command modules do not bypass policy, release, lifecycle, or EvidenceBundle gates.

## 14. Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [ ] Command inventory is documented.
- [ ] Command modules and entry-point wiring are confirmed.
- [ ] Per-command help text and README contracts are present.
- [ ] Access/policy checks are implemented for consequential commands.
- [ ] Dry-run behavior is available for release/lifecycle-affecting flows.
- [ ] Receipts and reports are emitted for consequential commands.
- [ ] Tests and fixtures cover allow, deny, restrict, hold, abstain, and error paths.
- [ ] Sensitive output redaction is tested.

## 15. Open verification items

| Item | Why it matters |
|---|---|
| Confirm command modules beyond README | Prevents overclaiming command maturity |
| Confirm command entry-point registration | Required for runnable CLI behavior |
| Confirm command inventory and help text | Required for operator usability |
| Confirm package/tool dependencies | Prevents authority forks |
| Confirm receipt/report output homes | Required for auditability |
| Confirm tests and fixtures | Required before enforcement claims |
| Confirm dry-run release behavior | Required before release-support claims |
| Confirm secrets handling | Prevents credentials in flags, logs, examples, or reports |

<details>
<summary>Appendix A — no-loss preservation note</summary>

The target file was an empty placeholder. This README adds a bounded command-directory contract without claiming command modules, command registration, tests, fixtures, help text, package metadata, CI jobs, or release integration are present.

</details>

## Status summary

`apps/cli/src/kfm_cli/commands/` should contain CLI command-family modules only after command inventory, tests, fixtures, help text, receipt behavior, and entry-point wiring are verified.

It should support validation, dry-runs, ingest checks, diffs, reports, receipt inspection, and maintenance without becoming a public path, release authority, lifecycle store, policy root, schema/contract home, shared library home, or shortcut around governed publication controls.

<p align="right"><a href="#top">Back to top</a></p>
