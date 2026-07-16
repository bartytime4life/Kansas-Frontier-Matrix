<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/scripts-dev-readme
title: scripts/dev/ — Local Development Helper Boundary
type: readme; directory-readme; canonical-script-sublane; local-development-helper-boundary
version: v0.2
status: draft; repository-grounded; placeholder-scripts-confirmed; implementation-unconfirmed; ci-unverified; non-authoritative
owners: OWNER_TBD — Developer tooling steward · Developer-experience steward · Fixture steward · Test steward · Security steward · CI steward · Docs steward
created: NEEDS VERIFICATION — greenfield stub preceded v0.1
updated: 2026-07-16
supersedes: v0.1 development helper guide
policy_label: "public; scripts; dev; local-only; placeholder-only; no-production-authority; no-release-authority; no-secret-store; no-hidden-mutation; rollback-aware"
current_path: scripts/dev/README.md
truth_posture: >
  CONFIRMED target v0.1 README; parent scripts root v0.2; bootstrap.sh and
  regen_fixtures.sh six-line placeholder implementations; current repository path /
  PROPOSED command contract, dry-run posture, mutation declaration, fixture-regeneration
  admission checklist, finite outcomes, promotion thresholds, validation and rollback /
  UNKNOWN dependency manager, supported operating systems, executable bootstrap behavior,
  fixture families, generator ownership, CI callers, network access, secret integration,
  generated output inventory, and production use /
  NEEDS VERIFICATION accepted owners, CODEOWNERS, Directory Rules-specific treatment,
  first non-placeholder implementation, test harness, CI integration, and graduation destination
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 799ebba5934358b9dd2098779575ef52495e197d
  prior_blob: 264141137c8e867829078643386b85403cc692ea
  scripts_root_blob: 4000b70a60af0d0656a4343ac6ae7f951b5327e3
  bootstrap_blob: a279533131ea08216e09d38d2542b2097d6863d1
  regen_fixtures_blob: 1d24306af6f9c0235da07903bc9a97dffaadad20
related:
  - ../README.md
  - ../maintenance/README.md
  - ../one_off/README.md
  - ../../tools/README.md
  - ../../pipelines/README.md
  - ../../packages/README.md
  - ../../fixtures/README.md
  - ../../tests/README.md
  - ../../configs/README.md
  - ../../configs/local/README.md
  - ../../data/receipts/README.md
  - ../../release/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/security/SECRETS.md
notes:
  - "This revision changes only scripts/dev/README.md."
  - "Both shell scripts remain placeholders; no executable behavior is added."
  - "Long-lived or trust-bearing behavior must graduate to tools/, pipelines/, packages/, tests/, or another accepted responsibility lane."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `scripts/dev/` — Local Development Helper Boundary

> **One-line purpose.** Hold small, explicit, reviewable local-development wrappers while they remain non-authoritative, reversible, and too immature for long-lived tooling, pipelines, reusable packages, formal tests, or governed artifact generation.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Version: v0.2" src="https://img.shields.io/badge/version-v0.2-informational">
  <img alt="Lane: local development" src="https://img.shields.io/badge/lane-local__development-blue">
  <img alt="Maturity: placeholders" src="https://img.shields.io/badge/maturity-placeholders-orange">
  <img alt="Production authority: none" src="https://img.shields.io/badge/production__authority-none-red">
  <img alt="Secrets: forbidden" src="https://img.shields.io/badge/secrets-forbidden-critical">
</p>

> [!IMPORTANT]
> **This lane is convenience, not authority.** A script under `scripts/dev/` may help a maintainer perform a bounded local task, but it does not establish schema validity, policy approval, evidence sufficiency, fixture authority, release readiness, deployment state, or public truth.

> [!CAUTION]
> **Do not treat placeholder output as implementation.** At the inspected snapshot, `bootstrap.sh` prints a dependency-setup TODO and `regen_fixtures.sh` prints `TODO`. Neither installs dependencies, configures a workstation, regenerates fixtures, validates outputs, writes receipts, or proves CI compatibility.

> [!WARNING]
> **Developer scripts must not become hidden mutation paths.** Future scripts that install software, change lockfiles, rewrite fixtures, access networks or secrets, modify governed roots, or emit trust-bearing artifacts must declare those effects, support review and rollback, and move to the correct responsibility lane when maturity requires it.

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Does not](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Inventory](#confirmed-current-inventory) · [Execution](#safe-execution-contract) · [Bootstrap](#bootstrap-boundary) · [Fixtures](#fixture-regeneration-boundary) · [Security](#security-network-and-secret-posture) · [Failures](#finite-outcomes-and-failure-semantics) · [Promotion](#graduation-and-promotion-rules) · [Validation](#validation) · [Review](#review-burden) · [Related](#related-folders) · [ADRs](#adrs) · [Rollback](#correction-and-rollback) · [Open](#open-verification-register) · [Last reviewed](#last-reviewed)

---

## Purpose

`scripts/dev/` is the KFM sublane for small local-development helper scripts whose purpose is narrow, explicit, and reversible.

A safe helper answers:

1. What exact local task does it perform?
2. Which files, processes, networks, package managers, or services may it touch?
3. Which effects are read-only, installed, generated, modified, or deleted?
4. Which prerequisites and versions are required?
5. Which outputs are temporary, ignored, review-only, or governed elsewhere?
6. Which validations prove the helper behaved as intended?
7. How is partial failure detected and recovered?
8. When must it graduate to `tools/`, `pipelines/`, `packages/`, `tests/`, or another governed lane?

This lane does not become authoritative because a command is convenient, frequently used, executable, or successful on one workstation.

[Back to top](#top)

---

## Authority level

**Canonical script sublane / non-authoritative local-development helper boundary.**

| Concern | Authority home | `scripts/dev/` role |
|---|---|---|
| Local convenience wrapper | `scripts/dev/` | Owns only the thin wrapper and usage guidance. |
| Long-lived validator, generator, builder, or QA command | `tools/` | Must graduate when trust-bearing or repeatedly relied upon. |
| Repeatable orchestration or lifecycle flow | `pipelines/` | Must not be hidden in a developer convenience script. |
| Reusable implementation | `packages/` | Shared logic belongs in importable, tested code. |
| Fixture instances and golden/negative cases | `fixtures/` | Scripts may reference them; they do not own fixture truth. |
| Executable proof | `tests/` | Script success is not a substitute for tests. |
| Contracts and schemas | `contracts/`, `schemas/` | Scripts consume them; they do not redefine them. |
| Policy, rights, sensitivity, access, release | `policy/`, review, `release/` | Scripts obey decisions and cannot grant approval. |
| Lifecycle records and receipts | governed `data/` lanes | Scripts emit only through accepted contracts and paths. |
| Shared configuration | `configs/` | Scripts reference reviewed defaults; no parallel config authority. |
| Workstation overrides | ignored `configs/local/` files | Local state remains untracked and non-authoritative. |
| Secrets | approved external mechanism | Use references, never committed values. |
| Deployment and services | `infra/`, app, or runtime roots | Dev helpers cannot authorize deployment. |

A dev script must not collapse setup guidance into an opaque installer, fixture convenience into fixture authority, local success into CI or release proof, generated output into evidence, configuration into policy, or temporary scaffolding into a production dependency.

[Back to top](#top)

---

## Status

At `main@799ebba5934358b9dd2098779575ef52495e197d`, the inspected lane is:

```text
scripts/dev/
├── README.md
├── bootstrap.sh
└── regen_fixtures.sh
```

| Path | Confirmed content | Safe conclusion |
|---|---|---|
| `README.md` | Prior v0.1 guardrail | Documentation exists. |
| `bootstrap.sh` | Bash, `set -euo pipefail`, one TODO echo | Placeholder only; no setup behavior. |
| `regen_fixtures.sh` | Bash, `set -euo pipefail`, one TODO echo | Placeholder only; no regeneration behavior. |

| Capability | Status | Consequence |
|---|---:|---|
| Bootstrap implementation | **NOT IMPLEMENTED** | Do not advertise a working installer. |
| Fixture regeneration | **NOT IMPLEMENTED** | Do not infer generator or fixture authority. |
| Dependency manager | **UNKNOWN** | Python, Node, pre-commit, and platform strategy require evidence. |
| Supported platforms | **UNKNOWN** | No compatibility claim is made. |
| Secret handling | **NOT AUTHORIZED** | No real secret may be stored or printed. |
| Tests and CI use | **UNKNOWN** | Shell syntax alone is insufficient proof. |
| Production/deployment use | **DENIED BY DEFAULT** | Local helpers are not production tooling. |
| Ownership | **OWNER_TBD** | Accepted owners remain unconfirmed. |

[Back to top](#top)

---

## What belongs here

- This README and local-lane indexes.
- Small developer-only wrappers.
- Read-only environment diagnostics that do not expose secrets.
- Setup guidance that prints commands rather than silently changing a workstation.
- Thin wrappers around accepted package-manager, test, validator, formatter, or lint commands.
- Temporary scaffolding with a deletion or graduation plan.
- Deterministic fixture-regeneration wrappers only after generator ownership, inputs, outputs, validation, and rollback are accepted.
- Dry-run and inspection helpers that expose intended changes before mutation.

[Back to top](#top)

---

## What does not belong here

| Do not place here | Correct home |
|---|---|
| Long-lived validators, generators, builders, proof assemblers, or release tools | `tools/` |
| Production or repeatable lifecycle orchestration | `pipelines/` |
| Shared libraries or domain logic | `packages/` |
| Test cases and assertions | `tests/` |
| Fixture payloads, golden outputs, invalid examples, or baselines | `fixtures/` |
| Semantic contracts or JSON Schema | `contracts/`, `schemas/` |
| Policy rules, approvals, sensitivity decisions, or access grants | `policy/` and governed review roots |
| Lifecycle data, receipts, proofs, catalogs, registries, or published payloads | governed `data/` lanes |
| Release manifests, correction notices, rollback cards, publication decisions | `release/` |
| Shared defaults and reusable templates | `configs/` |
| Deployment units, service managers, firewalls, or runtime services | `infra/`, `runtime/`, or app roots |
| Credentials, tokens, passwords, signing keys, private endpoints, or secret-bearing `.env` files | approved external secret system |
| Downloaded dependencies, caches, environments, model weights, package-manager stores | local ignored/cache locations |

[Back to top](#top)

---

## Inputs

Permitted inputs are bounded references to repository identity, tracked manifests and lockfiles, accepted configuration examples, ignored workstation overrides, accepted tool/test/validator entry points, fixture manifests, explicit arguments, non-secret environment variables, approved secret references, and declared dry-run targets.

Future scripts must reject unknown arguments, state the paths they may touch, distinguish tracked and ignored state, avoid broad sensitive-file scans, avoid unpinned remote content, and stop when required package managers, runtimes, fixture families, or versions are unresolved.

[Back to top](#top)

---

## Outputs

Current outputs are only terminal TODO messages.

Future outputs may include setup instructions, bounded diagnostics, finite exit codes, dry-run change plans, temporary ignored files, deterministic fixture candidates, and diff summaries.

Before real behavior is added, document:

| Field | Meaning |
|---|---|
| `command` | Stable invocation. |
| `mode` | inspect, dry-run, apply, or verify. |
| `reads` | Files, environment, services, and network sources read. |
| `writes` | Exact files or directories changed. |
| `deletes` | Exact deletions; default none. |
| `network` | Approved endpoints and integrity posture. |
| `secrets` | References used; never values. |
| `exit_codes` | Finite success and failure meanings. |
| `validation` | Tests proving behavior. |
| `rollback` | Restoration procedure. |
| `owner` | Responsible maintainer. |

[Back to top](#top)

---

## Confirmed current inventory

### `bootstrap.sh`

```bash
#!/usr/bin/env bash
# KFM dev bootstrap — greenfield placeholder.
set -euo pipefail
echo 'TODO: install Python and Node deps, set up pre-commit'
```

It does not detect an operating system, verify runtimes, choose a package manager, create an environment, install dependencies or hooks, edit configuration, access the network, use secrets, or validate setup.

### `regen_fixtures.sh`

```bash
#!/usr/bin/env bash
# Regenerate deterministic fixtures — greenfield placeholder.
set -euo pipefail
echo 'TODO'
```

It does not identify fixture families, invoke a generator, compare output, protect hand-authored fixtures, update manifests, validate contracts/schemas, run tests, emit receipts, or stage changes.

[Back to top](#top)

---

## Safe execution contract

Where mutation is possible, prefer:

```text
inspect -> dry-run -> apply -> verify
```

Required defaults:

- fail closed on missing prerequisites;
- no silent network access;
- no privilege escalation or `sudo` by default;
- no deletion or force overwrite by default;
- no recursive writes outside declared paths;
- no automatic commit or push;
- no secret output;
- no direct writes to `data/published/` or `release/`;
- no bypass of validators, tests, policy, review, or promotion gates;
- idempotent repeat execution or a clear refusal when repetition is unsafe.

[Back to top](#top)

---

## Bootstrap boundary

A future bootstrap helper must confirm repository root, detect a supported platform, check runtime versions, identify accepted package managers from repository evidence, verify lockfiles, show planned changes, install only in apply mode, avoid unnecessary global installation, verify postconditions, report partial failures, and provide rollback guidance.

It must not curl and execute unpinned scripts, silently install system packages, weaken security settings, modify global Git configuration without consent, store credentials, rewrite lockfiles as a side effect, claim untested platform support, or mask partial failure with exit code zero.

[Back to top](#top)

---

## Fixture regeneration boundary

Fixture regeneration is trust-bearing because fixtures can define valid, invalid, golden, regression, and denial behavior.

A future implementation requires an accepted fixture family, accepted generator, deterministic inputs, pinned versions, stable ordering, separation of generated and hand-authored fixtures, dry-run diff review, contract/schema validation, negative-fixture preservation, tests, and rollback.

```text
resolve accepted generator and versions
  -> inspect fixture family and ownership
  -> generate into a temporary location
  -> normalize deterministically
  -> validate contracts and schemas
  -> run positive and negative tests
  -> compare against tracked fixtures
  -> require review for meaningful diffs
  -> copy only approved changes
  -> preserve rollback target and review record
```

Stop when generator identity is unknown, output is nondeterministic, contracts and schemas conflict, sensitive material would be embedded, hand-authored fixtures would be overwritten, or validation fails.

[Back to top](#top)

---

## Security, network, and secret posture

- Default posture is **no network unless declared**.
- Secret values must never be committed, echoed, traced, or copied into diagnostics or PRs.
- Network-enabled helpers must document approved endpoints, TLS/integrity pinning, caching, offline behavior, retry rules, and whether downloaded material may be committed.
- Scripts must not ingest or emit protected coordinates, living-person data, DNA/genomic data, sensitive archaeology, infrastructure-sensitive details, or restricted EvidenceBundle content without explicit policy and access controls.

[Back to top](#top)

---

## Finite outcomes and failure semantics

| Outcome | Meaning |
|---|---|
| `SUCCESS` | Declared operation completed and postconditions passed. |
| `NO_CHANGE` | Desired state already existed; no mutation occurred. |
| `DRY_RUN` | Planned effects were reported; no mutation occurred. |
| `PARTIAL` | Some steps completed, but the target state is not verified. |
| `BLOCKED` | A prerequisite, owner, policy, version, or accepted target is missing. |
| `INVALID_INPUT` | Arguments or repository state are invalid. |
| `VALIDATION_FAILED` | Generated or changed material failed checks. |
| `UNSUPPORTED` | Platform, runtime, package manager, or mode is unsupported. |
| `ERROR` | Unexpected operational failure occurred. |

Printing a TODO, launching a command, or changing files is not verified success.

[Back to top](#top)

---

## Graduation and promotion rules

| Signal | Likely destination | Required action |
|---|---|---|
| Reused by multiple systems | `packages/` plus thin CLI | Extract shared logic and add tests. |
| Long-lived validator/generator/builder | `tools/` | Define command contract, fixtures, tests, and CI. |
| Repeatable multi-step orchestration | `pipelines/` | Define lifecycle inputs/outputs, receipts, failures, and rollback. |
| Fixture generation becomes authoritative | accepted generator/tool lane | Add deterministic generator, tests, manifests, review rules. |
| Used by CI | workflow-owned command or governed tool/test lane | Pin dependencies and fail closed. |
| Installs or configures services | `infra/`, runtime, or app operations lane | Add security, health, and rollback evidence. |
| One-time scaffolding is complete | delete or document lessons | Do not preserve dead scripts indefinitely. |

Moving a script is a governed migration, not a silent rename.

[Back to top](#top)

---

## Validation

Current placeholder checks:

```bash
bash -n scripts/dev/bootstrap.sh
bash -n scripts/dev/regen_fixtures.sh

test "$(bash scripts/dev/bootstrap.sh)" = "TODO: install Python and Node deps, set up pre-commit"
test "$(bash scripts/dev/regen_fixtures.sh)" = "TODO"
```

These prove only current syntax and output.

Future behavior requires shell linting, temporary-directory tests, supported-platform tests, dry-run/apply/verify tests, idempotence, failure-path tests, network-denial tests, secret-redaction tests, unknown-argument tests, write-boundary tests, positive/negative/golden fixture tests, rollback tests, and CI evidence when workflows depend on the command.

[Back to top](#top)

---

## Review burden

| Change class | Minimum review |
|---|---|
| README wording or placeholder message | Maintainer and docs review |
| Read-only diagnostics | Developer-tooling review |
| Package installation or lockfile interaction | Developer-experience, security, package owner |
| Fixture generation or mutation | Fixture, schema/contract, test, domain owner |
| Network access or downloaded content | Security, rights/source, tooling owner |
| Secret references | Security and operations |
| CI integration | CI and owning subsystem |
| Data, receipt, proof, catalog, policy, or release interaction | Relevant governance stewards and rollback review |
| Path graduation or authority change | Directory Rules review; ADR when required |

[Back to top](#top)

---

## Related folders

| Path | Relationship |
|---|---|
| [`scripts/`](../) | Parent script root and graduation rule. |
| [`scripts/maintenance/`](../maintenance/) | Bounded repository maintenance helpers. |
| [`scripts/one_off/`](../one_off/) | Ticket-bound temporary work. |
| [`tools/`](../../tools/) | Long-lived validators, generators, builders, and CLIs. |
| [`pipelines/`](../../pipelines/) | Repeatable orchestration and lifecycle flows. |
| [`packages/`](../../packages/) | Reusable implementation logic. |
| [`fixtures/`](../../fixtures/) | Governed fixture families and examples. |
| [`tests/`](../../tests/) | Executable proof of behavior. |
| [`configs/`](../../configs/) | Shared reviewed defaults and templates. |
| [`configs/local/`](../../configs/local/) | Ignored workstation-local overrides. |
| [`data/receipts/`](../../data/receipts/) | Process-memory records when required. |
| [`release/`](../../release/) | Release, correction, withdrawal, rollback authority. |

[Back to top](#top)

---

## ADRs

No accepted ADR specific to `scripts/dev/` was confirmed in this bounded edit.

An ADR or Directory Rules amendment is required if this lane would become a long-lived trust-bearing tooling home, parallel fixture-generator authority, production/deployment surface, new secret/configuration mechanism, or direct mutation path for governed data or release roots.

[Back to top](#top)

---

## Correction and rollback

A future mutating helper must identify pre-run state, files created/modified/deleted, package or service changes, temporary files, rollback commands, partial-state handling, and evidence preservation where required.

For this documentation revision, rollback is mechanical: revert the update commit or restore prior blob `264141137c8e867829078643386b85403cc692ea`.

No executable script behavior changes in this revision.

[Back to top](#top)

---

## Open verification register

| Item | Evidence needed |
|---|---|
| Exact recursive inventory | Commit-pinned tree listing. |
| Accepted owners and CODEOWNERS | Current ownership configuration and steward confirmation. |
| Directory Rules-specific placement | Relevant doctrine section or accepted ADR. |
| Supported operating systems | Tested platform matrix. |
| Python and Node dependency strategy | Accepted manifests, lockfiles, environment tools, tests. |
| Pre-commit posture | Current config, installation decision, CI relationship. |
| Bootstrap command contract | Implementation, tests, dry-run, idempotence, rollback. |
| Fixture families and generator | Accepted inventory, owner, tool path, schemas/contracts, tests. |
| CI callers | Workflow references and current run evidence. |
| Network and secret behavior | Security review, endpoint list, secret mechanism, negative tests. |
| Generated output homes | Accepted paths, manifests, receipts, validation, cleanup. |
| Promotion destination | Maintainer decision based on implemented behavior. |
| Deletion criteria | Ticket, milestone, or migration record for temporary helpers. |

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-16 |
| Evidence base | `main@799ebba5934358b9dd2098779575ef52495e197d` |
| Target prior blob | `264141137c8e867829078643386b85403cc692ea` |
| Review mode | Repository-grounded documentation revision; one-file scope |
| Implementation effect | None — documentation only |
| Rollback | Revert the update commit or restore the prior blob |

### Maintenance triggers

Re-review when either placeholder gains real behavior; a package manager, runtime version, or platform is selected; bootstrap installs dependencies or hooks; fixture generators are accepted; a script gains network or secret access; CI calls a helper; a script writes tracked or governed artifacts; ownership changes; a script moves or is deleted; or Directory Rules changes.

### v0.1 → v0.2 change summary

- Grounds the README against the parent root and exact placeholder contents.
- Records maturity without overstating setup or fixture behavior.
- Adds inputs, outputs, execution modes, finite outcomes, failure semantics, and idempotence.
- Adds bootstrap and fixture-regeneration admission boundaries.
- Adds security, network, secret, mutation, validation, review, migration, and rollback controls.
- Preserves the parent rule that long-lived trust-bearing behavior graduates from `scripts/`.

<p align="right"><a href="#top">Back to top</a></p>
