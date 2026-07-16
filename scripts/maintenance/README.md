<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/scripts-maintenance-readme
title: scripts/maintenance/ — Governed Maintenance and Doctrine-Preflight Lane
type: readme; directory-readme; maintenance-script-index; graduation-guardrail
version: v0.3
status: draft; canonical-script-sublane; promotion-sensitive; mixed-maturity; graduation-review-required; NEEDS VERIFICATION
policy_label: public
owners: OWNER_TBD — Maintenance tooling steward · Doctrine steward · Registry steward · Validation steward · Policy steward · Release steward · Docs steward
updated: 2026-07-15
current_path: scripts/maintenance/README.md
truth_posture: CONFIRMED current README and prior blob, scripts-root graduation rule, required-artifact checker, preflight orchestrator, test wrapper, promotion-gate caller, and output-path conflict at the pinned snapshot / UNKNOWN exhaustive callers, accepted receipt authority, production use, and current pass state / NEEDS VERIFICATION ownership, graduation, output-home migration, mutation rollback, and substantive published-alias audit
base_commit: 799ebba5934358b9dd2098779575ef52495e197d
prior_blob: e9872db30569bec7222274c0828abe9b35e39685
related:
  - ../README.md
  - ../../tools/README.md
  - ../../pipelines/README.md
  - ../../packages/README.md
  - ../../control_plane/README.md
  - ../../docs/runbooks/DOCTRINE_ARTIFACT_PREFLIGHT.md
  - ../../docs/doctrine/directory-rules.md
  - ../../data/receipts/validation/doctrine_artifact_check/README.md
  - ../../.github/workflows/promotion-gate.yml
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `scripts/maintenance/` — Governed Maintenance and Doctrine-Preflight Lane

> Bounded repository-maintenance commands for doctrine-artifact checks, provenance and registry alignment, normalized-summary readiness, and promotion-prerequisite support. This lane is operational support—not validator, policy, receipt, pipeline, or release authority.

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-scripts%2Fmaintenance-blue)
![maturity](https://img.shields.io/badge/maturity-mixed-orange)
![graduation](https://img.shields.io/badge/graduation-review__required-critical)

> [!IMPORTANT]
> `scripts/maintenance/` is a valid child of the canonical `scripts/` root, but working code is not automatically permanent code. Directory Rules and `scripts/README.md` require repeated or trust-bearing behavior to graduate to `tools/`, `pipelines/`, or `packages/` when its responsibility stabilizes.

> [!WARNING]
> The lane is already promotion-sensitive: `.github/workflows/promotion-gate.yml` directly runs `check_required_doctrine_artifacts.py`. That proves operational significance, not final placement authority or release approval.

## Quick navigation

[Status](#status-and-evidence-boundary) · [Authority](#authority-and-placement) · [Inventory](#current-inventory) · [Commands](#command-contracts) · [Outputs](#outputs-and-receipt-path-conflict) · [Safety](#mutation-and-safety-posture) · [Proof](#tests-workflows-and-proof-boundary) · [Graduation](#graduation-and-migration) · [Operations](#operator-runbook) · [Validation](#validation) · [Rollback](#correction-and-rollback) · [Backlog](#open-verification-backlog) · [Evidence](#evidence-basis)

---

## Status and evidence boundary

| Surface | Status | Safe conclusion |
|---|---|---|
| Target README | **CONFIRMED** | Existing lane index; prior blob is pinned above. |
| Required-artifact checker | **CONFIRMED executable** | Checks presence, registry status mismatch, minimum size, duplicate SHA-256 groups, and optional JSON output. |
| Preflight orchestrator | **CONFIRMED executable** | Runs child checks, builds normalized output, validates a summary schema, and supports strict gates. |
| Strict shell wrapper | **CONFIRMED present** | Provides a fail-closed invocation profile. |
| Test-suite wrapper | **CONFIRMED executable** | Runs source validators, normalized-only shadow checks, readiness checks, and bounded policy/source tests. |
| Promotion workflow caller | **CONFIRMED** | Promotion prerequisite invokes the checker directly. |
| Published-alias audit | **PLACEHOLDER / NEEDS VERIFICATION** | No substantive implementation is established here. |
| Output receipt home | **CONFLICTED** | Orchestrator defaults to `receipts/doctrine_artifacts/`; a governed lane is documented under `data/receipts/validation/doctrine_artifact_check/`. |
| Current pass state and production use | **UNKNOWN** | Source inspection does not prove successful current execution or deployment. |
| Long-term placement | **NEEDS VERIFICATION** | Repeated, trust-adjacent behavior requires command-by-command graduation review. |

This README provides routing, operating guidance, and drift disclosure only. Source code, contracts, schemas, policy, registries, tests, workflow definitions, emitted records, release decisions, and accepted ADRs outrank it.

---

## Authority and placement

```text
scripts/maintenance/             bounded wrappers and maintenance CLIs
tools/validators/                long-lived validator implementations
tools/release/ or tools/qa/      long-lived release or QA tooling when accepted
pipelines/                       repeatable multi-stage orchestration
packages/                        reusable imported libraries
control_plane/                   machine-readable governance registries
schemas/                         machine-checkable shapes
contracts/                       semantic meaning
policy/                          admissibility and policy authority
tests/ and fixtures/             enforceability proof and examples
data/receipts/ and data/proofs/  governed emitted audit/proof artifacts
release/                         promotion, correction, withdrawal, rollback authority
```

This lane may inspect and reconcile repository state. It must not silently become the policy engine, schema or contract authority, doctrine registry, permanent validator home, receipt root, release-gate definition, correction or rollback authority, publisher, or public client.

A workflow call proves use, not canonicity. A JSON file named `receipt` is not governed merely because a script emitted it.

---

## Current inventory

The inventory is bounded to checked repository evidence.

| File | Role | Maturity |
|---|---|---|
| `_cli_errors.py` | Structured CLI error helper | NEEDS VERIFICATION |
| `_doctrine_registry.py` | Shared required-registry parsing | Substantive helper; reuse scope NEEDS VERIFICATION |
| `check_required_doctrine_artifacts.py` | Presence, status, minimum-size, duplicate-digest check | Substantive; directly inspected |
| `check_doctrine_artifact_provenance.py` | Provenance-registry check | NEEDS VERIFICATION |
| `check_doctrine_registry_alignment.py` | Required/provenance registry alignment | NEEDS VERIFICATION |
| `check_normalized_summary_consumer_readiness.py` | Consumer-readiness check | Substantive / NEEDS VERIFICATION |
| `render_doctrine_presence_input.py` | Render policy-consumer presence input | Substantive / NEEDS VERIFICATION |
| `sync_doctrine_artifact_registry_status.py` | Reconcile required-registry statuses | Mutation-sensitive |
| `sync_doctrine_artifact_provenance_status.py` | Reconcile provenance status | Mutation-sensitive |
| `run_doctrine_artifact_preflight.py` | Multi-command orchestration and summary-schema validation | Trust-adjacent graduation candidate |
| `enforce_doctrine_preflight_gates.sh` | Strict wrapper | Promotion-sensitive |
| `run_doctrine_artifact_test_suite.sh` | Validator and pytest bundle | Substantive; directly inspected |
| `audit_published_aliases.py` | Intended published-alias audit | Placeholder / no authority |

Presence does not prove correctness, ownership, safe defaults, exhaustive tests, stable CLI compatibility, accepted output homes, release readiness, or production use.

---

## Command contracts

### Required-artifact checker

`check_required_doctrine_artifacts.py` accepts a registry, artifacts directory, and optional output path.

Confirmed checks:

- required filename presence;
- registry status mismatch;
- minimum size of `10,000` bytes;
- duplicate SHA-256 digest groups.

| Exit | Meaning |
|---|---|
| `0` | No configured check failed. |
| `1` | One or more configured checks failed. |
| `2` | Structured registry or operating-system error. |

These are integrity signals, not proof of authoritative content, rights, provenance sufficiency, review, or release approval.

### Preflight orchestrator

`run_doctrine_artifact_preflight.py` invokes:

1. required-artifact check;
2. provenance check;
3. provenance-status synchronization;
4. registry-alignment check;
5. normalized-summary consumer-readiness check;
6. presence-input renderer;
7. JSON Schema validation of the combined summary.

Checked options include `--registry`, `--provenance-registry`, `--artifacts-dir`, `--output-dir`, `--presence-output`, `--stable-filenames`, `--strict`, `--strict-provenance`, `--emit-normalized-only`, and `--require-consumer-readiness`.

| Exit | Meaning |
|---|---|
| `0` | Orchestration completed and selected strict gates passed. |
| `1` | A selected strict missing/provenance/readiness gate failed. |
| `2` | Execution, rendering, alignment, or summary-schema error. |

> [!CAUTION]
> Without strict flags, a normal child-check failure can still produce an overall zero after the summary is emitted. Operators and workflows must select the intended fail-closed profile explicitly.

### Strict and test wrappers

`enforce_doctrine_preflight_gates.sh` must remain a thin wrapper that exposes its strict flags, inputs, output paths, and underlying exit code.

`run_doctrine_artifact_test_suite.sh` uses `set -euo pipefail`, creates and cleans a normalized-only temporary summary, runs source validators and readiness checks, and invokes a bounded policy/source pytest set. This proves intended coverage, not a current pass result.

---

## Outputs and receipt-path conflict

The checked orchestrator defaults to:

```text
receipts/doctrine_artifacts/
```

Repository documentation also identifies:

```text
data/receipts/validation/doctrine_artifact_check/
```

This conflict is unresolved.

| Question | Required resolution |
|---|---|
| Is `receipts/` canonical, legacy, or compatibility? | Check Directory Rules, root READMEs, and accepted ADRs. |
| Are outputs receipts, validation reports, or temporary artifacts? | Resolve through contract/schema and governance review. |
| May local runs write into a governed receipt root? | Require explicit mode, identity, collision policy, and rollback. |
| May stable filenames overwrite prior outputs? | Define lineage and immutability rules first. |
| Should CI use ephemeral workflow artifacts? | NEEDS VERIFICATION. |

Safe interim posture:

- treat outputs as candidate maintenance artifacts;
- do not infer release state from them;
- prefer explicit temporary output paths during investigation;
- inspect generated files and `git diff`;
- do not commit outputs until the owning lane is confirmed;
- never delete prior governed records merely to make a run pass.

---

## Mutation and safety posture

Maintenance commands should default to inspection or dry-run behavior, require explicit flags for in-place writes, print target paths, use deterministic serialization, preserve pre-change digests, provide finite exits, emit structured errors, avoid network access by default, avoid secrets, and be idempotent where practical.

Registry-mutating commands must define input schema, pre-change digest, proposed changes, dry-run output, atomic-write strategy, post-write validation, correction procedure, rollback target, reviewer requirements, and whether CI may mutate or only inspect.

Output writers must define destination root, identity, overwrite behavior, timestamp, digest, schema version, source inputs, tool version, redaction posture, retention, correction, and supersession.

Do not add commands here that publish, mutate catalog truth as a routine side effect, approve release, suppress failed checks, rewrite shared Git history, delete audit material without correction, ingest restricted data without admission, log credentials, or expose sensitive payloads in public CI.

---

## Tests, workflows, and proof boundary

The checked promotion workflow runs:

```bash
python scripts/maintenance/check_required_doctrine_artifacts.py
```

as `doctrine-artifact-prereq`. Downstream jobs depend on that prerequisite and a separate schema validator.

Safe conclusion:

- checker failure can block downstream jobs;
- the checker is operationally significant;
- the workflow remains labeled a proposed scaffold;
- workflow success does not establish release approval;
- CI use strengthens the case for graduation review.

Still NEEDS VERIFICATION: complete per-script tests, branch-current pass results, mutation-path tests, concurrent-run behavior, stable-filename collisions, all workflow consumers, output schema coverage, and release rollback drills.

Required negative cases should cover malformed registries, missing/undersized/duplicate artifacts, status mismatch, missing provenance, alignment failure, unreadable inputs, unwritable outputs, malformed child JSON, child execution errors, summary-schema failure, unreadiness, strict/non-strict differences, interrupted writes, unintended mutations, and sensitive log leakage.

---

## Graduation and migration

| Signal | Current evidence | Implication |
|---|---|---|
| CI use | Promotion workflow calls a checker | Validator/tool review |
| Multi-step orchestration | Preflight composes checks and renderers | Tool or pipeline review |
| Schema validation | Orchestrator validates its summary | Stable command-contract review |
| Receipt-shaped output | JSON outputs are written | Output-home and receipt review |
| Registry reconciliation | Sync commands change governance state | Mutation and rollback review |
| Release-adjacent dependency | Downstream jobs depend on prerequisite | Release-steward review |
| Shared helpers | Parsing/error helpers serve multiple commands | Package or internal tool-library review |

Candidate destinations:

| Responsibility | Candidate home | Status |
|---|---|---|
| Required-artifact validator | `tools/validators/source/` or accepted doctrine-validator lane | PROPOSED |
| Preflight orchestration | `tools/validators/`, `tools/release/`, or `pipelines/` | NEEDS VERIFICATION |
| Registry synchronization | `tools/maintenance/` or governance-specific tooling | PROPOSED |
| Reusable registry parsing | `packages/` only if reused broadly | NEEDS VERIFICATION |
| Thin operator wrappers | May remain in `scripts/maintenance/` | PROPOSED |
| Validation receipts | Accepted `data/receipts/validation/...` lane or explicit temporary profile | NEEDS VERIFICATION |

Do not bulk-move the directory. Classify each command as validator, orchestrator, mutator, renderer, thin wrapper, test wrapper, or placeholder. Migrate with caller inventory, compatibility wrappers, tests, workflow updates, output-path migration, documentation, and rollback.

---

## Operator runbook

Inspect help first:

```bash
python scripts/maintenance/check_required_doctrine_artifacts.py --help
python scripts/maintenance/run_doctrine_artifact_preflight.py --help
python scripts/maintenance/check_normalized_summary_consumer_readiness.py --help
```

Use an explicit temporary output directory for investigation:

```bash
tmp_dir="$(mktemp -d)"
python scripts/maintenance/run_doctrine_artifact_preflight.py \
  --output-dir "$tmp_dir"
```

Review stdout, stderr, exit code, written files, input registries, and repository diff.

Run strict gates and the bounded test suite:

```bash
bash scripts/maintenance/enforce_doctrine_preflight_gates.sh
bash scripts/maintenance/run_doctrine_artifact_test_suite.sh
```

A strict failure should be investigated, not bypassed. These commands do not sign, publish, grant access, approve sensitivity downgrades, or replace review.

---

## Validation

Suggested lane checks:

```bash
find scripts/maintenance -maxdepth 2 -type f | sort
find scripts/maintenance -name '*.py' -print0 | xargs -0 -r python -m py_compile
find scripts/maintenance -name '*.sh' -print0 | xargs -0 -r bash -n
python scripts/maintenance/check_required_doctrine_artifacts.py --help
python scripts/maintenance/run_doctrine_artifact_preflight.py --help
bash scripts/maintenance/run_doctrine_artifact_test_suite.sh
```

> [!CAUTION]
> Preflight creates an output directory and may write JSON. Synchronization commands may have write modes. Use temporary paths and inspect help before running them in a working tree.

Validation is not release. Provenance, policy, review, correction, rollback, and release can remain unresolved after tests pass.

---

## Correction and rollback

### Documentation rollback

Before merge, leave the draft PR unmerged or restore prior blob `e9872db30569bec7222274c0828abe9b35e39685` in a transparent commit. After merge, revert the documentation commit or PR; do not reset shared history.

### Incorrect output

1. Stop downstream promotion use.
2. Preserve the incorrect output for audit when required.
3. Identify affected inputs, callers, outputs, and decisions.
4. Emit correction or supersession material in the accepted home.
5. Invalidate affected derived summaries.
6. Correct the root cause before rerunning.
7. Record the corrected tool version and digest.
8. Confirm release state independently.

### Registry rollback

Retain the pre-change blob or commit, validate the rollback, use a normal revert or corrective commit, rerun alignment and schema checks, preserve the reason and reviewer, and never force-push away the failed change.

### Output-home migration rollback

Retain old-reader compatibility for a bounded window, define deterministic mapping and duplicate detection, prevent double counting, preserve rollback to the prior writer/reader pair, and require retirement evidence before deleting the old path.

---

## Open verification backlog

- [ ] Confirm CODEOWNERS and command owners.
- [ ] Produce a recursive inventory with hashes.
- [ ] Inventory imports, subprocess callers, workflows, Make targets, and runbooks.
- [ ] Decide which commands remain wrappers and which graduate.
- [ ] Classify preflight as validator tool, release tool, or pipeline.
- [ ] Resolve `receipts/doctrine_artifacts/` versus `data/receipts/validation/doctrine_artifact_check/`.
- [ ] Confirm schemas, identity, overwrite, retention, correction, and supersession for every output.
- [ ] Confirm dry-run defaults, atomic writes, interruption safety, and collision behavior.
- [ ] Verify logs redact sensitive paths and values.
- [ ] Run the bounded suite on the current branch and record results.
- [ ] Confirm all required-check dependencies and flaky history.
- [ ] Decide whether integrity thresholds belong in policy or implementation.
- [ ] Confirm current state and future home of `audit_published_aliases.py`.
- [ ] Obtain release-steward acceptance before treating any command as release-critical authority.

---

## Evidence basis

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Prior lane README | CONFIRMED | Existing scope, inventory, commands, and questions | Some claims were earlier bounded observations |
| `scripts/README.md` | CONFIRMED | Root boundary and graduation rule | Does not decide each command's final home |
| `check_required_doctrine_artifacts.py` | CONFIRMED direct read | Checks, output, and exit behavior | Does not prove rights, provenance, or release readiness |
| `run_doctrine_artifact_preflight.py` | CONFIRMED direct read | Orchestration, options, output default, summary validation, exits | Current execution result not established |
| `run_doctrine_artifact_test_suite.sh` | CONFIRMED direct read | Bounded validators and tests | Suite not run during this documentation update |
| `promotion-gate.yml` | CONFIRMED direct read | Direct caller and dependency chain | Workflow is labeled a proposed scaffold |
| Validation-receipt README | CONFIRMED surfaced path | Adjacent governed receipt lane | Relationship to legacy `receipts/` remains unresolved |
| Directory Rules | CONFIRMED doctrine | Responsibility and graduation discipline | Migration requires caller and inventory evidence |

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-15 |
| Review posture | Draft, evidence-grounded maintenance-lane contract |
| Implementation changes | None |
| Tests run | None |
| Next trigger | Script, CLI, workflow, output-home, registry mutation, normalized-summary, graduation, or release-gate change |

[Back to top](#top)
