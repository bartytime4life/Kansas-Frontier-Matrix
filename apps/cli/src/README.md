<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://app/cli/src/readme
title: CLI App Source Tree README
type: app-readme
version: v0.1
status: draft
owners: OWNER_TBD — Apps steward · CLI steward · Release steward · Pipeline steward · Policy steward · Docs steward
created: 2026-06-16
updated: 2026-06-16
policy_label: restricted
related:
  - ../README.md
  - kfm_cli/README.md
  - kfm_cli/commands/README.md
  - ../../README.md
  - ../../governed-api/README.md
  - ../../admin/README.md
  - ../../review-console/README.md
  - ../../../policy/access/README.md
  - ../../../policy/decision/README.md
  - ../../../policy/data/README.md
  - ../../../packages/README.md
  - ../../../tools/README.md
  - ../../../scripts/README.md
  - ../../../release/README.md
  - ../../../data/README.md
  - ../../../docs/security/AUDIT_INVARIANTS.md
tags: [kfm, apps, cli, src, python-src-layout, operator-cli, commands, validation, dry-run, receipts, fail-closed]
notes:
  - "Initial README for the CLI src tree."
  - "Repository evidence confirms this README path and the kfm_cli module README; implementation files, command inventory, CLI entry point, tests, fixtures, package metadata, and CI remain NEEDS VERIFICATION."
  - "src/ is an app implementation source-layout boundary only; it must not become a public path, release authority, lifecycle data store, policy root, schema/contract home, tools root, scripts root, or shared package root."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

<div align="center">

# CLI App Source Tree

`apps/cli/src/`

**Source-layout boundary for the KFM operator CLI: importable CLI code may live here, while reusable libraries, validators, policy, lifecycle artifacts, release records, schemas, contracts, and public APIs remain in their owning roots.**

![status](https://img.shields.io/badge/status-draft-blue)
![owner](https://img.shields.io/badge/owner-OWNER__TBD-lightgrey)
![layout](https://img.shields.io/badge/layout-src%2F-0a7ea4)
![app](https://img.shields.io/badge/app-cli-6f42c1)
![truth](https://img.shields.io/badge/truth-NEEDS__VERIFICATION-yellow)

[Purpose](#1-purpose) · [Repo fit](#2-repo-fit) · [Boundary](#3-authority-boundary) · [Inputs](#5-inputs) · [Exclusions](#6-exclusions) · [Module map](#7-module-map) · [Definition of done](#14-definition-of-done)

</div>

---

> [!IMPORTANT]
> **Status:** draft / `NEEDS VERIFICATION`  
> **Owners:** `OWNER_TBD` — Apps steward · CLI steward · Release steward · Pipeline steward · Policy steward · Docs steward  
> **Path:** `apps/cli/src/README.md`  
> **Responsibility root:** `apps/` — deployable application surfaces  
> **Truth posture:** CONFIRMED source-tree README path / CONFIRMED child `kfm_cli/README.md` / UNKNOWN implementation files, command inventory, tests, fixtures, CLI entry point, and package metadata

> [!CAUTION]
> Code under `apps/cli/src/` must not publish, rewrite lifecycle state, approve release, weaken policy decisions, or expose restricted lifecycle material to public clients. It may orchestrate governed checks, dry-runs, reports, diffs, and receipt-oriented maintenance only within the CLI app boundary.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Repo fit](#2-repo-fit)
- [3. Authority boundary](#3-authority-boundary)
- [4. Default posture](#4-default-posture)
- [5. Inputs](#5-inputs)
- [6. Exclusions](#6-exclusions)
- [7. Module map](#7-module-map)
- [8. Diagram](#8-diagram)
- [9. Source-tree obligations](#9-source-tree-obligations)
- [10. Import-surface expectations](#10-import-surface-expectations)
- [11. Inspection path](#11-inspection-path)
- [12. Validation expectations](#12-validation-expectations)
- [13. Safe change pattern](#13-safe-change-pattern)
- [14. Definition of done](#14-definition-of-done)
- [15. Open verification items](#15-open-verification-items)

---

## 1. Purpose

`apps/cli/src/` is the source-layout container for the KFM operator CLI app.

Its job is to hold importable application implementation modules, currently centered on `kfm_cli/`, that may eventually provide command parsing, command-family routing, dry-run orchestration, deterministic report output, receipt-oriented helpers, safe error handling, and adapters that invoke owning packages, tools, policy runtime, and release/lifecycle checks.

This source tree exists to support the deployable CLI app. It is not evidence that complete command implementations, tests, package metadata, command entry points, or CI integration already exist.

[Back to top](#top)

---

## 2. Repo fit

| Concern | Owning root | Expected relationship |
|---|---|---|
| CLI source tree | `apps/cli/src/` | Packaging/source-layout boundary for importable CLI app code |
| CLI Python module | `apps/cli/src/kfm_cli/` | Python import module and implementation home |
| Command modules | `apps/cli/src/kfm_cli/commands/` | Command-family modules, if implemented and tested |
| Parent CLI app | `apps/cli/` | Operator CLI deployable boundary |
| Public trust membrane | `apps/governed-api/` | Public clients use governed API, not CLI outputs |
| Shared libraries | `packages/` | Reusable helpers should live here, not in app-private source |
| Repo-wide tools | `tools/` | Validators, generators, and builders; CLI may invoke but should not fork |
| Temporary scripts | `scripts/` | One-off operational helpers; durable command flows may graduate to CLI/tools/packages |
| Policy gates | `policy/` | Access, sensitivity, rights, data, and decision policy |
| Release authority | `release/` | Publication, correction, rollback control |
| Lifecycle artifacts | `data/` | Receipts, proofs, catalog, triplets, and published artifacts |

## 3. Authority boundary

This source tree may contain CLI app code. It does not own the governance authorities that CLI commands inspect, validate, or request.

```text
apps/cli/src/       = CLI app source-layout boundary
apps/cli/src/kfm_cli/ = Python CLI module
apps/cli/           = operator CLI deployable
apps/governed-api/  = normal public trust membrane
packages/           = shared reusable libraries
tools/              = validators, generators, builders
scripts/            = one-off operational helpers
policy/             = finite policy decisions
schemas/            = machine-readable shape
contracts/          = object meaning
data/               = lifecycle artifacts, receipts, proofs, registries
release/            = publication, correction, rollback authority
```

## 4. Default posture

Code in this source tree should be dry-run-first for consequential workflows and fail closed when support is unresolved.

A module or command handler should not perform a consequential action when any of these are missing or ambiguous:

- parsed command and target;
- command purpose or ticket/reference;
- actor or service identity where required;
- capability or role binding;
- lifecycle stage;
- source, schema, contract, policy, package, or release context;
- EvidenceRef / EvidenceBundle support;
- validation report;
- rollback or correction target;
- output path and overwrite strategy;
- receipt or audit destination.

## 5. Inputs

| Input family | Examples | Required posture |
|---|---|---|
| Command refs | command family, subcommand, flags, config profile, dry-run switch | Explicit and normalized |
| Actor refs | operator, CI service identity, maintenance account | Authenticated where consequential |
| Target refs | source descriptor, schema, contract, policy bundle, package, data artifact, release candidate | Governed reference, not ad hoc mutation |
| Lifecycle refs | RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, PUBLISHED, candidate release | Explicit before read/write |
| Policy refs | access, rights, sensitivity, finite decision, reason code | Required before action |
| Evidence refs | EvidenceRef, EvidenceBundle, citation validation, proof pack | Required for claim-bearing checks |
| Output refs | stdout mode, report path, receipt path, diff artifact path | Deterministic and safe |

## 6. Exclusions

| Does not belong here | Correct home |
|---|---|
| Shared reusable libraries | `packages/` |
| Repo-wide validators/generators/builders | `tools/` |
| Temporary one-off scripts | `scripts/` |
| Public API implementation | `apps/governed-api/` |
| Admin UI or restricted panels | `apps/admin/` |
| Steward review UI | `apps/review-console/` |
| Policy bundles | `policy/` |
| Schemas and contracts | `schemas/contracts/v1/`, `contracts/` |
| Lifecycle artifacts, receipts, proofs, catalog, triplets | `data/` |
| Release manifests, rollback cards, correction notices | `release/` |
| Secrets, credentials, tokens, private keys | Secret manager / deployment environment, not CLI source or examples |

## 7. Module map

| Path | Responsibility | Status |
|---|---|---|
| `kfm_cli/` | Python import package for CLI command behavior | CONFIRMED child README |
| `kfm_cli/__init__.py` | Initial export boundary | CONFIRMED empty file / NEEDS VERIFICATION |
| `kfm_cli/commands/` | Command-family modules | CONFIRMED child README / command modules NEEDS VERIFICATION |
| future modules | context, results, output, receipts, errors, command wiring | PROPOSED |

## 8. Diagram

```mermaid
flowchart TD
    src["apps/cli/src/"] --> mod["kfm_cli/"]
    mod --> commands["commands/"]
    commands --> parse["parse command + target"]
    parse --> ctx{"purpose + policy + evidence?"}
    ctx -->|no| safe["HOLD / ABSTAIN / ERROR"]
    ctx -->|yes| mode{"dry-run/read-only?"}
    mode -->|yes| report["deterministic report + receipt ref"]
    mode -->|no| gate{"release/lifecycle gate supports action?"}
    gate -->|no| hold["HOLD"]
    gate -->|yes| bounded["bounded action + receipt"]
```

## 9. Source-tree obligations

| Obligation | Example effect |
|---|---|
| `dry_run_first` | Consequential release/lifecycle flows start in dry-run mode |
| `minimal_exports` | Keep import surface small, reviewed, and tested |
| `purpose_required` | State-changing commands require ticket, review note, or CI run reference |
| `receipt_required` | Consequential commands emit RunReceipt, ValidationReport, or equivalent report refs |
| `redaction_required` | Reports and terminal output hide sensitive fields by default |
| `deterministic_output` | Reports and diffs use stable ordering and stable IDs where practical |
| `safe_failure_required` | Errors return finite safe reason codes |
| `no_authority_fork` | CLI source invokes owning packages/tools/policies instead of redefining them |

## 10. Import-surface expectations

The import surface should stay small until implementation is verified.

Candidate exported concepts may include CLI app construction, command context, command result types, safe error types, command-family registration, deterministic output helpers, and receipt/report helpers. These names remain `PROPOSED` until code, tests, command inventory, and package metadata confirm them.

## 11. Inspection path

Implementation files, command inventory, tests, fixtures, package metadata, CLI entry-point wiring, and CI usage remain `NEEDS VERIFICATION`.

```bash
find apps/cli/src -maxdepth 6 -type f | sort
find apps/cli apps packages tools scripts policy release data tests fixtures -maxdepth 5 -type f 2>/dev/null | grep -Ei 'kfm_cli|cli|command|validate|dry[-_ ]?run|ingest|diff|report|receipt|rollback' | sort
find docs docs/runbooks docs/security -maxdepth 5 -type f 2>/dev/null | grep -Ei 'cli|operator|validation|release|rollback|audit' | sort
```

## 12. Validation expectations

Useful validation for this source tree should cover:

- only reviewed import names are exported;
- unknown command returns `ERROR` with safe help text;
- missing required target returns `HOLD` or `ERROR`;
- missing purpose for consequential command returns `HOLD`;
- missing access or role context returns `DENY` where required;
- release dry-run cannot write PUBLISHED state;
- reports and diffs are deterministic and redacted by default;
- state-changing commands require rollback/correction support;
- source modules do not bypass policy, release, lifecycle, or EvidenceBundle gates.

## 13. Safe change pattern

For source changes under `apps/cli/src/`:

1. Add or update command inventory and help text.
2. Add tests for allow, deny, restrict, hold, abstain, and error paths.
3. Prefer dry-run behavior before enabling state-changing behavior.
4. Keep reusable logic in `packages/` or `tools/` instead of duplicating it in app-private code.
5. Update this README, `kfm_cli/README.md`, `commands/README.md`, and parent `apps/cli/README.md` when behavior changes.

## 14. Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [ ] `src/` package layout and package metadata are confirmed.
- [ ] CLI entry point and command inventory are documented.
- [ ] Import module files and export surface are inventoried.
- [ ] Access/policy checks are implemented for consequential commands.
- [ ] Dry-run behavior is available for release/lifecycle-affecting flows.
- [ ] Receipts and reports are emitted for consequential commands.
- [ ] Tests and fixtures cover allow, deny, restrict, hold, abstain, and error paths.
- [ ] Sensitive output redaction is tested.

## 15. Open verification items

| Item | Why it matters |
|---|---|
| Confirm implementation files beyond empty `__init__.py` | Prevents overclaiming source-tree maturity |
| Confirm CLI framework and command entry point | Required for runnable command surface |
| Confirm command inventory and help text | Required for operator usability |
| Confirm package metadata | Required for installable CLI behavior |
| Confirm receipt/report output homes | Required for auditability |
| Confirm tests and fixtures | Required before enforcement claims |
| Confirm CI usage | Determines whether CLI is operator-only or CI-driven |
| Confirm secrets handling | Prevents credentials in args, logs, examples, or reports |

<details>
<summary>Appendix A — no-loss preservation note</summary>

The target file was an empty placeholder. This README adds a bounded `src/` source-tree contract for the CLI app without claiming command implementations, entry-point wiring, tests, fixtures, package metadata, CI jobs, or release integration are present.

The observed child `kfm_cli/__init__.py` is empty, so implementation maturity remains `NEEDS VERIFICATION`.

</details>

## Status summary

`apps/cli/src/` should hold importable operator-CLI source code only after command inventory, tests, fixtures, receipts, and package metadata are verified.

It should support validation, dry-runs, ingest checks, diffs, reports, receipt inspection, and maintenance without becoming a public path, release authority, lifecycle store, policy root, schema/contract home, shared library home, tools root, scripts root, or shortcut around governed publication controls.

<p align="right"><a href="#top">Back to top</a></p>
