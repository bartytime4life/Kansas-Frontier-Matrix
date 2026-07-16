# `scripts/one_off/` — Governed One-Off Script Quarantine Lane

> Deletion-first holding boundary for narrowly scoped repository scripts that are temporary, reviewable, reversible, and explicitly barred from becoming hidden production, policy, evidence, lifecycle, or release authority.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/scripts-one-off-readme
title: scripts/one_off/README.md — Governed One-Off Script Quarantine Lane
type: readme; directory-readme; temporary-script-boundary; deletion-first-guardrail
version: v0.2
status: draft; repository-grounded; readme-only; empty-by-default; no-active-one-off-script-established
owners: OWNER_TBD — Developer tooling steward · Maintenance tooling steward · Security reviewer · Data steward · QA steward · Release steward · Docs steward
created: NEEDS VERIFICATION — README existed before v0.1 expansion
updated: 2026-07-16
supersedes: v0.1
policy_label: public-doctrine; temporary-scripts; deletion-first; dry-run-first; review-required; no-production-authority; no-policy-authority; no-release-authority
current_path: scripts/one_off/README.md
truth_posture: CONFIRMED target README, scripts responsibility root, parent scripts README v0.2, maintenance lane README v0.2, Directory Rules authority and lifecycle invariants, and bounded repository search showing no direct one-off script beyond this README / PROPOSED admission manifest, risk classes, execution receipts, expiry enforcement, no-network default, promotion triggers, cleanup evidence, and CI guardrails / UNKNOWN exhaustive recursive inventory, generated or ignored local files, historical one-off scripts, external operator copies, workflow callers, scheduled use, and branch-local temporary scripts / NEEDS VERIFICATION owner assignment, accepted expiry policy, ticket-link format, allowed mutation classes, receipt schema, promotion authority, cleanup cadence, and automated stale-file enforcement
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  visibility: public
  base_ref: main
  base_commit: 799ebba5934358b9dd2098779575ef52495e197d
  target_prior_blob: e49ea8d45b518484985d9b97c621696d271fae33
  related_repository_blobs:
    directory_rules: 2affb080e6f0043867c64c7f06c1ca52030fbd55
    scripts_root_readme: 4000b70a60af0d0656a4343ac6ae7f951b5327e3
    maintenance_readme: e9872db30569bec7222274c0828abe9b35e39685
  direct_lane_files_confirmed:
    - scripts/one_off/README.md
  bounded_inventory_note: repository code search did not establish any direct one-off script under this lane; this is not proof against ignored, unindexed, historical, branch-local, or external files
related:
  - ../README.md
  - ../dev/README.md
  - ../maintenance/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../tools/README.md
  - ../../pipelines/
  - ../../packages/
  - ../../fixtures/
  - ../../tests/
  - ../../artifacts/
  - ../../data/
  - ../../release/
notes:
  - "v0.2 replaces a generic temporary-script note with a repository-grounded, fail-closed execution and cleanup boundary."
  - "The lane is empty by default and currently README-only at the bounded evidence snapshot."
  - "A script may be temporary without being low risk; write-capable, networked, sensitive, lifecycle-touching, policy-touching, or release-touching work receives elevated review."
  - "No one-off script may become the normal path for ingestion, validation, evidence resolution, policy enforcement, promotion, publication, correction, or rollback."
  - "This revision changes documentation only and creates no executable script, workflow, receipt, data mutation, policy decision, proof, or release object."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

<p>
  <img alt="Document status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Inventory: README only" src="https://img.shields.io/badge/inventory-README__only-lightgrey">
  <img alt="Default state: empty" src="https://img.shields.io/badge/default-empty-blue">
  <img alt="Execution: dry run first" src="https://img.shields.io/badge/execution-dry__run__first-orange">
  <img alt="Network: denied by default" src="https://img.shields.io/badge/network-denied__by__default-critical">
  <img alt="Authority: none" src="https://img.shields.io/badge/authority-none-red">
  <img alt="Exit: delete or promote" src="https://img.shields.io/badge/exit-delete__or__promote-purple">
</p>

`scripts/one_off/` is not an implementation destination. It is a temporary containment boundary.

**Quick navigation:** [Status](#status-and-evidence-boundary) · [Purpose](#purpose) · [Authority](#authority-boundary) · [Current state](#confirmed-current-state) · [Admission](#admission-contract) · [Risk](#risk-classification) · [Execution](#execution-contract) · [Mutation](#mutation-and-side-effect-boundary) · [Network](#network-secrets-and-external-services) · [Sensitive data](#sensitive-data-and-high-consequence-domains) · [Outputs](#outputs-and-review-evidence) · [Validation](#validation-and-testing) · [Promotion](#promotion-and-graduation) · [Cleanup](#expiry-deletion-and-cleanup-proof) · [Review](#review-burden) · [Done](#definition-of-done) · [Open](#open-verification-register) · [Evidence](#evidence-ledger)

---

## Status and evidence boundary

> [!IMPORTANT]
> **Document lifecycle:** `draft`  
> **Path:** `scripts/one_off/`  
> **Current bounded inventory:** this README only  
> **Default lane state:** empty  
> **Execution authority:** none  
> **Publication authority:** denied  
> **Truth limit:** absence of tracked files does not prove absence of ignored, historical, branch-local, generated, or external copies.

### Safe conclusion

The repository establishes `scripts/one_off/` as a temporary script lane under the `scripts/` responsibility root. At the inspected snapshot, no direct one-off script was established beyond this README. The parent script root states that long-lived or trust-bearing behavior must graduate to `tools/`, `pipelines/`, or `packages/`.

- **CONFIRMED:** this README exists.
- **CONFIRMED:** `scripts/README.md` defines an operational helper root, not schema, policy, proof, release, or publication authority.
- **CONFIRMED:** `scripts/maintenance/` is the repeatable maintenance lane and is not interchangeable with this directory.
- **CONFIRMED:** bounded repository search did not establish a direct one-off executable here.
- **PROPOSED:** keep the lane empty by default and require task, risk, rollback, expiry, and promotion metadata for every temporary executable.
- **UNKNOWN:** historical, ignored, local, branch-only, workflow-referenced, and external copies.

### Truth labels

| Label | Meaning |
|---|---|
| `CONFIRMED` | Verified from current repository evidence or bounded checks. |
| `PROPOSED` | A recommended control not established as current implementation. |
| `UNKNOWN` | Not proven by inspected evidence. |
| `NEEDS VERIFICATION` | Checkable but unresolved strongly enough to act as fact. |
| `DENY` | Prohibited by this boundary unless governance deliberately changes it. |

---

## Purpose

This lane is for one narrow class of work: a temporary script needed to complete one reviewed repository task when permanent tooling would be premature.

A valid one-off script has:

- one named task and accountable owner;
- exact inputs and outputs;
- a bounded mutation set;
- a meaningful dry run;
- a review and rollback path;
- an expiry condition;
- a final decision to delete or promote.

The lane is not a home for unfinished code, unowned experiments, undocumented migrations, production shortcuts, or behavior whose long-term responsibility root is already known.

### Empty-by-default rule

```text
scripts/one_off/
└── README.md
```

Temporary scripts may appear during an active task, but they must not accumulate into an informal tools directory.

---

## Authority boundary

A one-off script may execute commands. Successful execution grants no authority.

This lane is not:

- schema or semantic contract authority;
- policy, consent, rights, or sensitivity authority;
- source activation or identity authority;
- evidence, receipt, proof, or validator authority;
- lifecycle orchestration authority;
- release, correction, rollback, or publication authority;
- public API or UI behavior;
- a credential or secret store;
- a substitute for tests, review, receipts, or governed promotion.

> [!WARNING]
> Writing a file into a governed directory does not make it a governed object. It still requires the accepted schema, contract, policy, evidence, review, receipt, release, correction, and rollback path appropriate to its significance.

A one-off script must never be treated as proof that a source is approved, a claim is true, rights are cleared, sensitivity is resolved, consent exists, a release is approved, or a public client may consume the output.

---

## Confirmed current state

| Surface | Status | Evidence-bounded conclusion |
|---|---:|---|
| `scripts/one_off/README.md` | `CONFIRMED` | The lane guardrail exists. |
| Direct executable scripts | `NOT ESTABLISHED` | Bounded repository search did not surface one. |
| Dedicated lane tests | `UNKNOWN` | No lane-specific test inventory was established. |
| CI expiry or metadata enforcement | `UNKNOWN` | No dedicated workflow was verified. |
| Admission manifest schema | `NOT ESTABLISHED` | The metadata contract below is proposed. |
| Execution receipts | `UNKNOWN` | No accepted one-off receipt shape was verified. |
| Automated stale-script cleanup | `UNKNOWN` | No cleanup workflow was verified. |
| Promotion authority | `NEEDS VERIFICATION` | Parent documentation identifies destinations, not final approvers. |

The README-only state does not prove that no one-off script has ever existed or exists elsewhere. Those claims require history, branch, deployment, and operator inventory evidence.

---

## Admission contract

Before a script is added, its PR must record:

| Field | Required content |
|---|---|
| `task_id` | Issue, ADR, migration, incident, or decision reference. |
| `owner` | Maintainer responsible for execution and cleanup. |
| `purpose` | One task, stated narrowly. |
| `why_one_off` | Why permanent tooling is not justified yet. |
| `inputs` | Exact paths, commands, services, and parameters read. |
| `outputs` | Exact stdout, files, records, or mutations produced. |
| `risk_class` | `R0` through `R4` from the matrix below. |
| `dry_run` | Command and expected no-write behavior. |
| `network` | `denied` unless specifically reviewed. |
| `secrets` | Normally `none`; identify only the approved injection mechanism, never values. |
| `rollback` | Mechanical reversal or restoration procedure. |
| `validation` | Checks proving bounded behavior. |
| `expiry` | Date or completion condition. |
| `promotion_trigger` | Conditions requiring graduation. |
| `cleanup_owner` | Person responsible for deletion or promotion. |

Each executable should contain an equivalent header:

```text
KFM one-off script
Task: <issue or decision>
Owner: <name or team>
Purpose: <one narrow task>
Risk class: <R0-R4>
Inputs: <exact paths or services>
Outputs: <exact paths or stdout>
Dry run: <command>
Write mode: <command or denied>
Network: denied | reviewed profile
Rollback: <mechanical reversal>
Expires: <date or completion condition>
Promote if: <trigger>
```

Missing metadata is a review failure, not a harmless TODO.

---

## Risk classification

Temporary does not mean low risk.

| Class | Description | Examples | Minimum review |
|---|---|---|---|
| `R0` | Read-only, local, deterministic inspection | list files, summarize metadata, print a proposed diff | maintainer |
| `R1` | Writes disposable local or build artifacts | temporary report outside governed roots | maintainer + cleanup owner |
| `R2` | Mutates repository source, docs, fixtures, or configuration | bounded rename or formatting migration | owning maintainer + dry run + rollback |
| `R3` | Touches lifecycle, registry, schema, contract, policy, evidence, receipt, proof, or release-adjacent surfaces | registry repair or schema migration | owning steward + tests + execution evidence + rollback |
| `R4` | Touches sensitive data, credentials, production state, external mutation, publication, or irreversible operations | DNA/living-person data, destructive remote change | normally `DENY` here; use governed tooling and explicit approval |

When uncertain, classify upward. A script is `R3` or `R4` if failure could alter what KFM considers admissible, evidentiary, policy-compliant, releasable, correctable, or publicly visible.

---

## Execution contract

### Dry-run first

Every write-capable script must support a meaningful dry run unless it is provably read-only. A meaningful dry run resolves inputs, validates preconditions, computes intended changes, produces a reviewable plan, makes no governed mutation, and uses the same target-selection logic as write mode.

A flag that skips the actual selection or validation logic is not a meaningful dry run.

### Explicit write mode

Write mode must require an affirmative action such as `--apply` or `--write`. Running with no write flag should be read-only.

### Determinism

Where practical, pinned inputs and parameters must produce the same plan and output digest. Time, random IDs, filesystem order, locale, environment, and network results must be controlled or recorded.

### Finite outcomes

A script should finish with one explicit result:

- `NOOP` — nothing required;
- `PLANNED` — dry-run plan produced;
- `APPLIED` — bounded mutation completed;
- `PARTIAL` — some work completed; reconciliation required;
- `DENIED` — scope, policy, rights, sensitivity, or consent blocked execution;
- `ERROR` — technical failure.

`PARTIAL`, `DENIED`, and `ERROR` must not be silently converted to success. Until a repository-wide exit-code standard is accepted, every script must document its actual codes.

---

## Mutation and side-effect boundary

A script may mutate only the exact paths and object classes declared in its metadata and reviewed plan.

It must not:

- discover and mutate additional targets silently;
- follow symlinks outside declared scope;
- broaden globs after review;
- overwrite without version-control or backup recovery;
- delete untracked or ignored files without explicit review;
- modify generated and canonical sources in one opaque step;
- bypass validators or pre-commit checks;
- commit, push, merge, tag, publish, or release unless that is the specifically approved task.

Direct mutation of these surfaces is `R3` or higher:

```text
schemas/        contracts/       policy/          control_plane/
data/registry/  data/raw/        data/work/       data/quarantine/
data/processed/ data/catalog/    data/triplets/   data/receipts/
data/proofs/    data/published/  release/
```

A one-off script must not become the normal interface for these roots. Prefer an accepted validator, migration tool, pipeline, package, or runbook with tests and receipts.

Destructive actions require a dry-run inventory, count and size summary, exclusions, explicit apply flag, reproducible restoration source, post-delete validation, and appropriate deletion evidence.

---

## Network, secrets, and external services

Network access is denied by default.

A reviewed exception must identify the service and endpoint family, why an existing connector cannot be used, authentication method, rate and retry limits, request method, data sent and received, current terms and rights posture, sensitivity review, timeout behavior, and receipt and rollback strategy.

External mutation—creating, editing, deleting, uploading, posting, sending, or publishing remote state—is normally `R4` and does not belong in an informal one-off script.

Secrets must never be committed, echoed, written into receipts, included in stack traces, or placed in fixtures. A script must not silently install packages, download executables, alter global environments, or modify lockfiles during execution.

---

## Sensitive data and high-consequence domains

One-off scripts are especially dangerous when they touch living-person records, DNA/genomic material, private person-parcel joins, archaeology, rare-species locations, critical infrastructure, credentials, legal/title/consent records, or emergency and current operational data.

For these classes:

- default to `DENY` or `QUARANTINE`;
- minimize data before execution;
- test with synthetic or de-identified fixtures;
- never log raw sensitive values;
- preserve consent, rights, sensitivity, sovereignty, and purpose limitations;
- require the owning steward’s review;
- record transforms and reasons;
- ensure correction, revocation, takedown, and rollback propagation.

A repository-maintenance objective never overrides privacy, consent, rights, sovereignty, or sensitivity controls.

---

## Outputs and review evidence

| Output | Required posture |
|---|---|
| stdout plan | Preferred for read-only dry runs. |
| temporary report | Use an accepted temporary or QA artifact location. |
| source-tree diff | Must be reviewable in version control. |
| fixture candidate | Promote to the accepted fixture root and review it. |
| lifecycle object | Use the accepted schema, root, validator, and workflow. |
| receipt or proof candidate | Not accepted evidence until validated and reviewed. |
| release or correction candidate | Must enter the release process; script output alone has no authority. |

For `R2` and above, retain enough evidence to identify executor, commit, script digest, parameters, input digests, approved plan, changes, skips or denials, validators, rollback target, and final deletion or promotion disposition.

The accepted receipt shape and canonical home remain `NEEDS VERIFICATION`; do not create parallel receipt authority in this directory. Logs must be bounded and free of secrets or sensitive raw values.

---

## Validation and testing

Before merge, run applicable syntax and inventory checks:

```bash
git diff -- scripts/one_off
find scripts/one_off -maxdepth 2 -type f -print | sort
find scripts/one_off -name '*.sh' -print0 | xargs -0 -r bash -n
find scripts/one_off -name '*.py' -print0 | xargs -0 -r python -m py_compile
find scripts/one_off \( -name '*.js' -o -name '*.mjs' \) -print0 | xargs -0 -r -n1 node --check
```

Syntax checks do not prove safety, correctness, policy compliance, or rollback.

Depending on risk, test empty, expected, malformed, duplicate, and already-applied inputs; missing targets; permission and partial failures; interrupted execution; dry-run/write parity; rollback; path traversal and symlink resistance; sensitive-value redaction; denied network behavior; and deterministic ordering.

Use synthetic, minimal, non-sensitive fixtures. Postconditions must verify both intended change and absence of unintended change.

---

## Promotion and graduation

A script must leave this lane when it is reused, called by CI, imported as reusable logic, used as repeatable orchestration, used as a validator, made into an operator command, or made responsible for trust-bearing receipts, proofs, or release objects.

| Trigger | Likely destination |
|---|---|
| repeated local or operator use | `scripts/dev/`, `scripts/maintenance/`, or `tools/` |
| CI invocation or durable validation | `tools/` or an accepted maintained lane with tests |
| reusable logic | `packages/` |
| repeatable lifecycle orchestration | `pipelines/` |
| contract, schema, policy, evidence, or release validation | `tools/validators/` |
| durable fixture generation | accepted generator/tooling lane plus `fixtures/` |
| persistent external integration | accepted connector, runtime, or infrastructure boundary |

Graduation is a governed change, not a file move. It requires an accepted home, stable command contract, ownership, tests, dependencies, documented inputs and failures, security and policy review where applicable, caller migration, deletion or deprecation of the old path, and rollback.

---

## Expiry, deletion, and cleanup proof

Every script needs an expiry date or concrete completion condition. “Later” and “when no longer needed” are insufficient.

At completion choose exactly one:

1. **Delete** — remove the script and retain only necessary documentation or receipts.
2. **Promote** — move behavior to the correct governed root with tests and migration evidence.
3. **Extend once** — record a new bounded expiry and reason.
4. **Quarantine** — disable execution if results or side effects are uncertain.

Cleanup proof should show the script removed or promoted, temporary outputs removed or placed correctly, stale workflow/docs/config/import references cleared, sensitive logs and credentials absent, rollback and correction obligations closed, and the task record updated.

A script past expiry is disabled pending review; age does not create approval.

---

## Review burden

| Risk | Required review |
|---|---|
| `R0` | maintainer familiar with target paths |
| `R1` | maintainer plus cleanup owner |
| `R2` | owning-root maintainer plus affected-code reviewer |
| `R3` | owning steward, tooling/QA reviewer, and policy or release reviewer where relevant |
| `R4` | normally reject from this lane and use an explicit governed process |

For high-consequence work, author, executor, reviewer, and release approver should not collapse into one unreviewed role.

### Review checklist

- [ ] Task, owner, and one-off justification are explicit.
- [ ] Inputs, outputs, and mutation scope are exact.
- [ ] Risk is not understated.
- [ ] Dry run shares target-selection logic with write mode.
- [ ] Network is denied or specifically reviewed.
- [ ] Secrets and sensitive data are excluded or governed.
- [ ] Partial failure and rollback are safe and tested.
- [ ] Postconditions verify intended and unintended effects.
- [ ] Expiry, cleanup owner, and promotion triggers are explicit.
- [ ] Output paths respect Directory Rules and lifecycle boundaries.

---

## Definition of done

### This README revision

| Criterion | Status |
|---|---:|
| preserves deletion-first purpose | `PASS` |
| records README-only bounded state | `PASS` |
| distinguishes one-off, dev, maintenance, tools, pipelines, and packages | `PASS` |
| defines admission and risk requirements | `PASS` |
| requires meaningful dry run and explicit write mode | `PASS` |
| denies hidden network, secret, policy, evidence, lifecycle, and release authority | `PASS` |
| defines sensitive-data, validation, rollback, expiry, cleanup, and promotion controls | `PASS` |
| changes no executable script or governed object | `PASS` |
| repository-native CI verified after PR creation | `PENDING` |

A future one-off task is complete only when postconditions pass, unintended changes are absent, outputs are correctly placed, execution evidence is retained where required, rollback or correction is closed, and the script is deleted, promoted, extended once, or quarantined.

---

## Open verification register

| ID | Question | Status | Evidence needed |
|---|---|---|---|
| `ONEOFF-001` | Should CI enforce README-only state except on active task branches? | `NEEDS VERIFICATION` | Accepted root policy and workflow design. |
| `ONEOFF-002` | What metadata format should temporary scripts use? | `NEEDS VERIFICATION` | Contract or linter decision. |
| `ONEOFF-003` | Is the proposed `R0–R4` vocabulary accepted? | `PROPOSED` | Tooling and security review. |
| `ONEOFF-004` | What receipt shape and home apply to `R2+` executions? | `NEEDS VERIFICATION` | Receipt contract and lifecycle decision. |
| `ONEOFF-005` | What maximum expiry and extension policy applies? | `NEEDS VERIFICATION` | Maintenance policy. |
| `ONEOFF-006` | Does CI detect stale scripts, missing metadata, and missing dry-run support? | `UNKNOWN` | Validator and workflow evidence. |
| `ONEOFF-007` | Are historical or branch-local scripts still referenced? | `UNKNOWN` | History, branch, and consumer inventory. |
| `ONEOFF-008` | Which exit-code convention is canonical? | `NEEDS VERIFICATION` | Accepted CLI contract. |
| `ONEOFF-009` | Are networked one-off scripts categorically prohibited? | `NEEDS VERIFICATION` | Security and connector policy. |
| `ONEOFF-010` | Who approves promotion into each destination root? | `NEEDS VERIFICATION` | Ownership or CODEOWNERS evidence. |
| `ONEOFF-011` | How are interrupted or partial executions reconciled? | `NEEDS VERIFICATION` | Runbook and rollback tests. |
| `ONEOFF-012` | Is there an approved sandbox for high-risk migrations? | `UNKNOWN` | Infrastructure and runbook evidence. |

---

## Evidence ledger

| Evidence | Status | Supports | Does not prove |
|---|---:|---|---|
| prior target blob `e49ea8d…` | `CONFIRMED` | Existing deletion-first lane and prior README-only statement. | Exhaustive current inventory or enforcement. |
| Directory Rules blob `2affb080…` | `CONFIRMED DOCTRINE` | Responsibility placement, lifecycle invariants, visible authority, reversibility. | Script behavior or CI wiring. |
| scripts root README blob `4000b70a…` | `CONFIRMED ROOT CONTRACT` | Operational-helper boundary and graduation rule. | Every script’s correctness or maturity. |
| maintenance README blob `e9872db3…` | `CONFIRMED ADJACENT CONTRACT` | Difference between repeatable maintenance tooling and one-off work. | One-off inventory or promotion decision. |
| bounded repository search | `CONFIRMED BOUNDED RESULT` | No direct tracked one-off executable was established. | Historical, ignored, local, branch-only, or external copies. |

Current repository files, tests, workflow results, logs, receipts, and release records outrank planning prose for implementation behavior. Directory Rules govern placement. This README governs only the temporary lane boundary and cannot create schema, policy, lifecycle, evidence, or release authority.

---

## Maintainer note

Keep this directory boring and usually empty.

When a temporary script is truly necessary, make its scope smaller than the task, its dry run clearer than its write mode, its rollback mechanical, its expiry explicit, and its final deletion or promotion unavoidable.

<p align="right"><a href="#top">Back to top</a></p>
