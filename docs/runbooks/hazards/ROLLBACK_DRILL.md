<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook-hazards-rollback-drill
title: Hazards Rollback Drill
type: operational-runbook
version: v1.1.0
status: DRAFT_REPOSITORY_GROUNDED; BOUNDED_SYNTHETIC_REHEARSAL; HAZARDS_FIXTURE_IMPLEMENTED; OPERATIONAL_ROLLBACK_UNVERIFIED; NON_RELEASE; NON_PUBLICATION
owner: NEEDS VERIFICATION — Hazards domain steward plus rollback/correction reviewer and accountable release authority
created: 2026-08-27
updated: 2026-08-27
policy_label: repository-facing; hazards; rollback-rehearsal; synthetic-only; fail-closed; not-for-life-safety; non-publisher
owning_root: docs/
path_authority: same-path modernization under accepted ADR-0029 and Directory Rules v2
authority_effect: none
release_effect: none
deployment_effect: none
promotion_effect: none
publication_effect: none
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: d6b72570bc71aa4c7adec7cba518c214c38c5cb2
  execution_start_commit: a84670b00e240f0e5bb647e001c342e5387a8625
  target_path: docs/runbooks/hazards/ROLLBACK_DRILL.md
  target_prior_blob: decc1aafd7b5a4ed6f1cac2b3c2501b8f3f047d2
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adoption_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  rollback_tool_blob: a8f6bff350e79b453f425ebce9a9ded6801f8944
  rollback_test_blob: b644ca6c4185b3f81bc339c077eae85299833261
  hazards_fixture_readme_blob: 4b2d23a437a999c6beb249adb0dd7b02037bd34a
  hazards_scenario_blob: 23942cf833d3b5a2484d1fd357e12a6e6c5afaae
  hazards_test_blob: 76d8c6c36df5bcb53d913c9451cecaf230bdf717
  rollback_rehearsal_doc_blob: c65b2790a2796572498ff07d4d12c4f028eb50c6
  hazards_rollback_runbook_blob: 89183e9a619028006921832b5513e811274f2920
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  open_pull_requests_touching_target: 0
source_lineage:
  - title: KFM_Greenfield_Commissioning_Plan_v2_FULL.pdf
    version: 2.0.0
    source_class: PLANNING_REFERENCE
    use: rollback-drill measurement, correction cascade, and smallest-complete-circle framing only
  - title: KFM Alignment Register — 2026-08-23
    source_class: COORDINATION_ONLY
    use: preserve repository, review, rollback, release, deployment, promotion, and publication as separate states
related:
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../doctrine/directory-rules.md
  - ../README.md
  - ../rollback-rehearsal.md
  - ROLLBACK_RUNBOOK.md
  - PROMOTION_RUNBOOK.md
  - NOT_FOR_LIFE_SAFETY_AUDIT_RUNBOOK.md
  - ../../domains/hazards/README.md
  - ../../../tools/release/rollback_apply.py
  - ../../../tests/release/test_synthetic_rollback_rehearsal.py
  - ../../../tests/domains/hazards/test_synthetic_rollback_rehearsal.py
  - ../../../fixtures/domains/hazards/synthetic_rollback_rehearsal/README.md
  - ../../../release/README.md
notes:
  - The implemented helper is generic and synthetic-only; it is not a Hazards-specific or operational rollback executor.
  - The tracked Hazards fixture models one non-locating planning-context rollback from deliberately stale-mislabeled synthetic context to a withheld stale carrier; domain tests copy it to a temporary directory before plan or apply.
  - A successful rehearsal report is process evidence for the named synthetic case. It is not a RollbackCard, CorrectionNotice, ReviewRecord, PolicyDecision, ReleaseManifest, release decision, deployment, promotion, publication, or proof of production recovery.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hazards Rollback Drill

> **One-line purpose.** Rehearse KFM's implemented rollback and withdrawal mechanics against a marker-protected synthetic workspace, verify fail-closed behavior and preservation guarantees, and hand off an evidence-bounded result without touching a real Hazards release or public surface.

[![Status: bounded rehearsal](https://img.shields.io/badge/status-bounded%20synthetic%20rehearsal-8250df?style=flat-square)](#current-disposition)
[![Domain fixture: bounded](https://img.shields.io/badge/Hazards%20fixture-bounded-8250df?style=flat-square)](#current-disposition)
[![Mode: no network](https://img.shields.io/badge/mode-no%20network-0969da?style=flat-square)](#6-run-the-focused-drill)
[![Life safety: no](https://img.shields.io/badge/life%20safety-not%20an%20alerting%20system-b42318?style=flat-square)](#not-for-life-safety-boundary)
[![Public effect: none](https://img.shields.io/badge/public%20effect-none-6e7781?style=flat-square)](#2-authority-and-terminal-boundary)

<a id="not-for-life-safety-boundary"></a>

> [!CAUTION]
> **KFM Hazards is not an emergency-alerting system, emergency-operations system, or regulatory authority.** Do not use this drill to issue, replace, delay, retract, or interpret current life-safety instructions. The fixture must contain synthetic, public-safe material only. A real public Hazards defect requires immediate fail-closed containment and referral to the appropriate official authority through an independently authorized incident and rollback path.

> [!IMPORTANT]
> **Current disposition: `BOUNDED_HAZARDS_FIXTURE_PROOF / OPERATIONAL_HOLD`.** The repository implements a deterministic synthetic rollback/withdrawal helper, eight generic focused tests, one tracked no-sensitive-data Hazards planning-context fixture, and four domain-focused tests. The helper remains generic, does not evaluate policy or review, does not authorize release, and cannot touch an unmarked workspace. No operational release target, authenticated reviewers, live invalidation consumers, or public recovery verification is demonstrated.

## Quick navigation

- [1. Goal and scope](#1-goal-and-scope)
- [2. Authority and terminal boundary](#2-authority-and-terminal-boundary)
- [3. Current disposition](#3-current-disposition)
- [4. Implemented rehearsal contract](#4-implemented-rehearsal-contract)
- [5. Preconditions](#5-preconditions)
- [6. Run the focused drill](#6-run-the-focused-drill)
- [7. Optional direct CLI rehearsal](#7-optional-direct-cli-rehearsal)
- [8. Interpret the report](#8-interpret-the-report)
- [9. Hazards scenario profile](#9-hazards-scenario-profile)
- [10. Stop and escalation conditions](#10-stop-and-escalation-conditions)
- [11. Evidence worksheet](#11-evidence-worksheet)
- [12. Acceptance and negative cases](#12-acceptance-and-negative-cases)
- [13. Operational graduation gate](#13-operational-graduation-gate)
- [14. Related repository surfaces](#14-related-repository-surfaces)
- [15. Runbook maintenance and rollback](#15-runbook-maintenance-and-rollback)

---

## 1. Goal and scope

This drill closes one small, implemented circle:

```text
synthetic current release + synthetic prior release + exact digests
  -> deterministic PLAN
  -> marker-protected APPLY
  -> alias restoration or withdrawal
  -> append-only correction and complete invalidation record
  -> affected release bytes preserved
```

### In scope

- running the focused standard-library test module at an exact repository revision;
- verifying deterministic plan mode and marker-protected apply mode;
- rehearsing both `ROLLBACK` and `WITHDRAWAL` against temporary synthetic roots;
- verifying manifest and artifact digests before mutation;
- verifying alias restoration or withdrawal, correction recording, invalidation coverage, and history preservation;
- exercising implemented negative cases without weakening the helper; and
- recording a bounded result and its limitations for review.

### Out of scope

- a real Hazards release, candidate, manifest, alias, cache, layer, API route, Evidence Drawer payload, Focus Mode answer, source connector, deployment, or public surface;
- source admission, live data retrieval, current warning interpretation, or life-safety action;
- policy evaluation, reviewer authentication, signature verification, release authorization, or separation-of-duties enforcement;
- repository reverts, database migrations, infrastructure failover, production cache purges, feature flags, or source pauses;
- creating a canonical `RollbackCard`, `CorrectionNotice`, `PolicyDecision`, `ReviewRecord`, `ReleaseManifest`, proof, receipt, or release decision; and
- claiming operational recovery, release, deployment, promotion, or publication from a synthetic pass.

[Back to top](#top)

---

## 2. Authority and terminal boundary

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts the exact [Directory Rules v2](../../doctrine/directory-rules.md) bytes. Those rules place human operational procedures and rollback drills under `docs/runbooks/`, executable repository helpers under `tools/`, behavioral proof under `tests/`, and release-governance records under `release/`.

This is a same-path replacement of an existing tracked scaffold. It creates no new responsibility root, compatibility surface, schema home, policy home, release home, or parallel authority.

| Responsibility | Owning surface | Role in this drill |
|---|---|---|
| Human Hazards drill procedure | `docs/runbooks/hazards/ROLLBACK_DRILL.md` | Explains the bounded rehearsal and its stop conditions |
| Generic synthetic rollback mechanics | `tools/release/rollback_apply.py` | Verifies and optionally mutates only a marker-protected synthetic workspace |
| Generic executable behavior evidence | `tests/release/test_synthetic_rollback_rehearsal.py` | Exercises positive and negative helper behavior |
| Hazards reusable fixture | `fixtures/domains/hazards/synthetic_rollback_rehearsal/` | Supplies one public-safe, non-locating stale-context rollback workspace |
| Hazards executable behavior evidence | `tests/domains/hazards/test_synthetic_rollback_rehearsal.py` | Copies the fixture to a temporary root and checks deterministic, apply, preservation, and fail-closed behavior |
| General synthetic operator note | `docs/runbooks/rollback-rehearsal.md` | Supplies the cross-domain concise entry point |
| Hazards rollback design | `docs/runbooks/hazards/ROLLBACK_RUNBOOK.md` | Describes the broader domain procedure; verify its assumptions before use |
| Release decisions and records | `release/` | Remain outside the drill and require separate authority |

The highest supported result is:

```text
SYNTHETIC_REHEARSAL_PASS
```

That result means only that the exact focused checks passed for the synthetic workspace. It does not mean `REVIEWED`, `APPROVED`, `ROLLBACK_AUTHORIZED`, `RECOVERED`, `RELEASED`, `DEPLOYED`, `PROMOTED`, or `PUBLISHED`.

[Back to top](#top)

---

<a id="current-disposition"></a>

## 3. Current disposition

The following assessment is pinned to delivery-base `main@d6b72570bc71aa4c7adec7cba518c214c38c5cb2`. Execution began at `main@a84670b00e240f0e5bb647e001c342e5387a8625`; the intervening merge of unrelated PR #3625 changed only ADR issue-intake and receipt paths.

| Surface | Current evidence | Truth / maturity | Safe conclusion |
|---|---|---|---|
| Target path | Grounded bounded drill merged by PR #3620 | **CONFIRMED / CURRENT BASELINE** | Update only the statements changed by this executable slice. |
| Generic helper | `tools/release/rollback_apply.py` verifies marker, exact scenario fields, manifests, artifacts, digests, alias identity, target identity, and invalidation completeness | **CONFIRMED / IMPLEMENTED BOUNDED** | A synthetic plan/apply rehearsal is available. |
| Generic focused tests | Eight tests cover deterministic no-write plan, rollback apply, withdrawal apply, and five fail-closed cases | **CONFIRMED BY SOURCE / NEEDS EXECUTION AT EACH HEAD** | Retain as helper regression coverage. |
| Hazards-specific tracked fixture | `fixtures/domains/hazards/synthetic_rollback_rehearsal/` contains one marker-protected, non-locating stale-context rollback workspace | **IMPLEMENTED BOUNDED** | The fixture proves only the exact planning-context scenario; it is not release or operational data. |
| Hazards-focused tests | Four tests verify deterministic no-write plan, bounded carrier fields, stale-withholding apply, release-byte preservation, tamper denial, and non-synthetic denial | **IMPLEMENTED BOUNDED / NEEDS EXECUTION AT EACH HEAD** | Run with the generic module as the first milestone-specific drill. |
| Invalidations | Helper requires `API_CACHE`, `CDN`, `TILES`, `CATALOG`, `TRIPLETS`, `SEARCH_INDEX`, `VECTOR_INDEX`, `AI_CACHE`, and `DOWNSTREAM_DERIVATIVES` | **CONFIRMED DECLARED SET** | Completeness of the synthetic record is testable; real consumers are not invoked. |
| Governance fields | Reports state that no authority, policy evaluation, review, release authorization, publication authorization, or public-state mutation occurred | **CONFIRMED REPORT CONTRACT** | A report cannot be promoted into governance evidence it does not own. |
| Operational Hazards rollback | No real candidate, production alias, cache/CDN consumer, authenticated release authority, or public recovery exercise was demonstrated for this drill | **UNKNOWN / HOLD** | Do not run this helper against a real release or claim operational readiness. |
| Open overlap | PR #3625 was the only open PR at execution start and merged without overlap; delivery preflight found open PRs #3626–#3629 on unrelated receipt, governance-parity, MapLibre, and issue-intake paths | **CONFIRMED AT DELIVERY-BASE RECHECK** | No open changed-path or rehearsal-semantics overlap was found; recheck immediately before remote delivery. |

### Current finite result

```text
implementation_state: BOUNDED_HAZARDS_FIXTURE_PROOF
domain_state: SYNTHETIC_ONLY
operational_state: HOLD
reason_codes:
  - HAZ_SYNTHETIC_STALE_CONTEXT_ROLLBACK_TRACKED
  - HAZ_ROLLBACK_POLICY_NOT_EVALUATED
  - HAZ_ROLLBACK_REVIEW_AUTHORITY_UNVERIFIED
  - HAZ_OPERATIONAL_RECOVERY_UNVERIFIED
release_effect: none
publication_effect: none
```

[Back to top](#top)

---

## 4. Implemented rehearsal contract

The helper accepts exactly one synthetic workspace and one scenario object.

### Workspace guard

The workspace root must:

- already exist;
- resolve to a concrete directory;
- contain a regular, non-symlink marker named `.kfm-synthetic-rollback-rehearsal`;
- give that marker the exact UTF-8 content `synthetic-only\n`;
- contain no path traversal or symlink in a scenario-selected path; and
- contain the expected `published/current.json` and release directories.

Missing or malformed protection produces `HOLD` with a stable reason code. The helper must never be pointed at the repository root, `release/`, `data/published/`, a deployment directory, a mounted production volume, or an operator's broad home/workspace directory.

### Scenario contract

The JSON object must contain exactly these fields:

| Field | Implemented requirement |
|---|---|
| `scenario_id` | Non-empty text |
| `synthetic` | Literal `true` |
| `operation` | `ROLLBACK` or `WITHDRAWAL` |
| `affected_release_id` | Non-empty text; must be the exact current synthetic alias target |
| `target_release_id` | Required text for `ROLLBACK`; required `null` for `WITHDRAWAL` |
| `correction` | Object with non-empty `correction_id`, `reason_code`, and `decided_at` |
| `invalidations` | Exact complete implemented invalidation set; no missing or duplicate entry |
| `expected` | Expected canonical alias digest and affected/target manifest digests |

Each release manifest must declare its own `release_id` and at least one artifact with exactly `path` and `digest`. Every artifact digest is recomputed before the rehearsal proceeds.

### Modes

| Mode | Invocation | Implemented effect |
|---|---|---|
| `PLAN` | default | Verifies the scenario and returns the deterministic proposed state; does not mutate the synthetic release workspace. If `--report` is supplied, only that explicitly named local report is written. |
| `APPLY` | `--apply` | Re-verifies the scenario, mutates only the marker-protected synthetic alias, writes a synthetic correction record and invalidation record, and confirms affected release history stayed byte-identical. |

The helper uses Python standard-library file and JSON operations and contains no network client. Run it with the repository no-network environment anyway so the evidence packet records the intended boundary consistently.

[Back to top](#top)

---

## 5. Preconditions

Before running the drill, record or verify:

- [ ] the exact full repository commit under test;
- [ ] a clean or otherwise understood working tree;
- [ ] no open overlapping pull request or branch owns the target drill or helper/test bytes;
- [ ] Python can import the repository helper and standard library;
- [ ] no production credential, token, key, source material, release object, or mounted public-state volume is present in the test process;
- [ ] the focused test is allowed to create and destroy its own operating-system temporary directories;
- [ ] `KFM_NO_NETWORK=1`, deterministic hashing, UTC, and no bytecode writes are set for the run;
- [ ] every test input is synthetic and public-safe; and
- [ ] the operator understands that a pass is bounded process evidence only.

If any precondition is unresolved, return `HOLD` and do not substitute a real release path to make the drill possible.

[Back to top](#top)

---

## 6. Run the focused drill

Run from the repository root at the exact commit being evaluated:

```bash
export KFM_NO_NETWORK=1
export PYTHONHASHSEED=0
export PYTHONDONTWRITEBYTECODE=1
export PYTHONUNBUFFERED=1
export TZ=UTC

python -m unittest -q \
  tests.release.test_synthetic_rollback_rehearsal \
  tests.domains.hazards.test_synthetic_rollback_rehearsal
```

The generic module contains eight focused cases:

| Case | Required observation |
|---|---|
| Deterministic plan | Two identical plans compare equal and create no correction directory |
| Rollback apply | Current alias switches to the prior release; correction and invalidation records exist |
| Withdrawal apply | Alias becomes `WITHDRAWN` with no target while affected release bytes remain |
| Non-synthetic input | Denied with `NON_SYNTHETIC_INPUT_DENIED` |
| Incomplete invalidation set | Denied with `INVALIDATION_SET_INCOMPLETE` |
| Missing target release | Denied with `REQUIRED_FILE_MISSING` |
| Tampered artifact | Denied with `ARTIFACT_DIGEST_MISMATCH` |
| Missing marker | Denied with `SYNTHETIC_MARKER_MISSING` |

The Hazards module adds four fixture-bound cases:

| Case | Required observation |
|---|---|
| Bounded deterministic plan | Both carriers remain synthetic, non-locating, unreleased, unpublished, planning-only, and not for life safety; two plans match; no file changes |
| Stale-context rollback apply | Temporary alias targets the `WITHHELD_STALE` prior carrier; correction and invalidation records exist; both releases remain byte-identical |
| Tampered carrier | Digest mismatch denies apply before alias, correction, or invalidation changes |
| Non-synthetic scenario | `NON_SYNTHETIC_INPUT_DENIED` denies apply before any state change |

Record the exact command, commit, start/end time, exit code, and complete test summary. Do not call the drill `PASS` if the command is skipped, pending, interrupted, or run against a different head.

[Back to top](#top)

---

## 7. Optional direct CLI rehearsal

The focused tests are the preferred first execution because the Hazards module copies the tracked workspace into a temporary directory and cleans it afterward. Use the CLI directly only after copying `fixtures/domains/hazards/synthetic_rollback_rehearsal/workspace/` into a new, narrowly scoped temporary directory. Never apply directly to the tracked fixture.

### Plan

```bash
python tools/release/rollback_apply.py \
  --workspace "$KFM_SYNTHETIC_ROLLBACK_ROOT" \
  --scenario "$KFM_SYNTHETIC_ROLLBACK_ROOT/scenario.json"
```

Expected success:

```text
outcome=PASS
mode=PLAN
reason_code=SYNTHETIC_REHEARSAL_PLANNED
```

### Apply inside the same synthetic root

```bash
python tools/release/rollback_apply.py \
  --workspace "$KFM_SYNTHETIC_ROLLBACK_ROOT" \
  --scenario "$KFM_SYNTHETIC_ROLLBACK_ROOT/scenario.json" \
  --apply
```

Expected success:

```text
outcome=PASS
mode=APPLY
reason_code=SYNTHETIC_REHEARSAL_APPLIED
```

On a handled failure the CLI prints a JSON `HOLD` report and exits `2`. Preserve that result as failure evidence; do not edit the scenario, expected digest, invalidation list, or helper merely to force a pass.

> [!WARNING]
> Never set `KFM_SYNTHETIC_ROLLBACK_ROOT` to the repository root, a parent of the repository, a user's home directory, `release/`, `data/`, a deployment checkout, or any path whose contents and marker were not created specifically for this temporary rehearsal.

[Back to top](#top)

---

## 8. Interpret the report

### Success fields

| Report surface | What it establishes | What it cannot establish |
|---|---|---|
| `before` | Exact synthetic current alias, manifest digest, and artifact digests were verified | Production identity, source authority, or release validity |
| `after` | Expected synthetic alias/withdrawal state and target digests were computed | Real alias mutation, cache purge, or public parity |
| `correction` | The synthetic scenario carried an append-only correction identity, reason, and decision time | A canonical `CorrectionNotice` or authenticated correction decision |
| `invalidations` | The declared synthetic record contains the complete implemented invalidation vocabulary | Any named cache, tile, catalog, index, AI, or downstream consumer was actually invalidated |
| `preservation` | The helper checked affected manifest/artifact retention and append-only correction posture | Backup/restore, retention policy, or external store durability |
| `governance` | The report explicitly disclaims authority, policy, review, release, publication, and public-state mutation | Any later governed transition |

### Finite outcomes

| Outcome | Meaning | Operator posture |
|---|---|---|
| `PASS` | The exact synthetic plan or apply contract completed | Record bounded evidence; keep domain/operational state on `HOLD` unless separately proven |
| `HOLD` | A handled guard or contract failure blocked the rehearsal | Preserve prior state; record reason; repair only the synthetic input or verified helper defect |
| Unexpected exception or non-JSON output | The helper did not return its declared contract | Classify `ERROR`; preserve logs; do not apply |
| `SKIPPED`, `NOT_RUN`, `PENDING`, `NO_RUN_FOUND` | No completed proof exists | Never reclassify as `PASS` |

[Back to top](#top)

---

## 9. Hazards scenario profile

The tracked profile supplies one affected and one prior carrier with deterministic identities and exact digests. Both use a non-locating synthetic area, planning-only context, synthetic source role, fixed UTC times, `not_for_life_safety: true`, and false public-use, release, and publication effects.

The affected carrier is deliberately expired but labeled `CURRENT`; its fixture defect is `STALE_CONTEXT_MISLABELED_CURRENT`. The rollback target preserves the expired time window and changes only the safe display posture to `WITHHELD_STALE`, with wording that asserts no current condition or alert. The scenario uses a fixed correction identity and the complete implemented invalidation vocabulary.

This first slice intentionally does not add a Hazards withdrawal fixture, generalized-geometry case, policy evaluation, evidence resolution, reviewer authentication, signature, real cache consumer, operational release target, or public recovery check. Those remain separate future slices and cannot be inferred from this rollback pass.

The [Not-for-Life-Safety Audit Runbook](NOT_FOR_LIFE_SAFETY_AUDIT_RUNBOOK.md) must govern any later public-surface scenario. A synthetic drill must not fetch or reproduce current official alerts.

[Back to top](#top)

---

## 10. Stop and escalation conditions

Stop before `--apply` and return `HOLD` when:

- the workspace marker is missing, malformed, symlinked, inherited from another run, or outside a dedicated temporary root;
- `synthetic` is not literal `true`;
- the operation, target, correction object, expected digests, or invalidation set is incomplete or contradictory;
- an artifact or manifest digest differs from the scenario;
- the current alias does not identify the affected release;
- the rollback target equals the affected release or cannot be resolved;
- a selected path is absolute, traverses upward, escapes the root, or crosses a symlink;
- any input contains real private, restricted, life-safety, unpublished, credential-bearing, or production material;
- the requested result would require policy, review, signature, release, deployment, promotion, publication, source activation, repository settings, or real public-state mutation;
- the focused tests fail at the exact head; or
- the only apparent fix weakens a guard, expected digest, negative case, or invalidation requirement.

For a real or suspected public Hazards defect, do not adapt this helper in place. Use the independently authorized incident, correction, withdrawal, and [Hazards Rollback Runbook](ROLLBACK_RUNBOOK.md) paths; keep the affected public surface fail-closed and refer current emergency needs to official authorities.

[Back to top](#top)

---

## 11. Evidence worksheet

This worksheet is operator memory, not a schema, receipt, proof, review, rollback card, correction notice, or release decision.

| Field | Required value |
|---|---|
| Repository | `bartytime4life/Kansas-Frontier-Matrix` |
| Evaluated commit | `<full SHA>` |
| Drill command | `<exact command>` |
| Start/end | `<UTC timestamps>` |
| Exit code | `<integer>` |
| Test result | `PASS / FAIL / ERROR / SKIPPED / NOT_RUN / PENDING / NO_RUN_FOUND` |
| Mode | `TEST / PLAN / APPLY` |
| Scenario ID | `<synthetic ID or N/A>` |
| Operation | `ROLLBACK / WITHDRAWAL / N/A` |
| Affected synthetic release | `<ID or N/A>` |
| Target synthetic release | `<ID / null / N/A>` |
| Marker verified | `yes / no / N/A` |
| Digest verification | `PASS / HOLD / ERROR / N/A` |
| Invalidation set | `COMPLETE / INCOMPLETE / N/A` |
| History preservation | `PASS / HOLD / ERROR / N/A` |
| Reason code | `<implemented code or N/A>` |
| Network observed | `no / yes / unknown` |
| Real/public state touched | `no` |
| Evidence location | `<local log or hosted-run reference>` |
| Limitations | `<every unproved operational or Hazards-specific claim>` |
| Domain disposition | `HOLD` unless separately proven |
| Release/publication effect | `none` |

[Back to top](#top)

---

## 12. Acceptance and negative cases

### Documentation acceptance criteria

This runbook is acceptable when it:

- replaces the stale scaffold at the existing canonical path;
- names only currently implemented helper/test commands as executable fact;
- distinguishes generic synthetic mechanics from Hazards semantic and operational recovery;
- preserves the not-for-life-safety boundary;
- documents both `PLAN` and marker-protected `APPLY` accurately;
- lists the implemented complete invalidation vocabulary;
- preserves correction, withdrawal, rollback, review, policy, release, and publication as distinct object and authority families;
- treats skipped or absent execution as not proven;
- provides objective positive and negative cases; and
- includes a reversible fixture, test, and documentation rollback.

### Executable acceptance criteria

| Condition | Required result |
|---|---|
| Focused modules at exact head | All twelve tests pass |
| Hazards fixture plan | Carrier bounds hold, two reports match, and workspace bytes do not change |
| Hazards fixture apply | Alias targets the withheld stale carrier and both release trees remain byte-identical |
| Same scenario planned twice | Reports are byte-for-byte equivalent after canonical serialization |
| Plan without `--report` | No correction or invalidation state is written |
| Valid rollback apply | Synthetic alias points to the prior release; affected bytes remain unchanged |
| Valid withdrawal apply | Synthetic alias is withdrawn; affected bytes remain retained |
| Complete invalidation set | All nine implemented families are present exactly once |
| Non-synthetic scenario | `HOLD / NON_SYNTHETIC_INPUT_DENIED` |
| Marker absent or invalid | `HOLD` with the corresponding marker reason code |
| Artifact tampered | `HOLD / ARTIFACT_DIGEST_MISMATCH` |
| Target missing, equal, or malformed | `HOLD` with the corresponding target/file reason code |
| Unsafe path or symlink | `HOLD / UNSAFE_PATH` or `HOLD / UNSAFE_SYMLINK` |
| Real/public path proposed | Operator `HOLD`; do not invoke the helper |

[Back to top](#top)

---

## 13. Operational graduation gate

Do not upgrade this runbook from bounded synthetic rehearsal until repository and runtime evidence demonstrates, for a named Hazards scope:

- [ ] an admitted, public-safe Hazards release candidate and a distinct prior safe release;
- [ ] accepted contracts and schemas for the involved release, correction, withdrawal, rollback, review, policy, receipt, and evidence families;
- [ ] resolved `EvidenceRef` to `EvidenceBundle` support and source-role/time-role integrity;
- [ ] rights, sensitivity, sovereignty, consent, and precision clearance;
- [ ] an accepted policy evaluator result with version, reasons, and obligations;
- [ ] authenticated Hazards, correction, rollback, and accountable release reviewers with required separation;
- [ ] verified signatures and immutable manifest/artifact identities where required;
- [ ] real implementations for alias mutation, API/CDN/tile/catalog/triplet/search/vector/AI/downstream invalidation, and their receipts;
- [ ] public UI stale, withdrawn, superseded, denied, unavailable, and official-referral states;
- [ ] end-to-end recovery verification, including cache propagation and no residual access to the affected carrier;
- [ ] rollback timing and success-rate evidence from repeated non-production exercises;
- [ ] incident containment, correction notice, and forward-fix/recompile paths; and
- [ ] independent authorization for any production exercise.

Until then, report operational Hazards rollback as `UNKNOWN / HOLD`, even when this synthetic module passes.

[Back to top](#top)

---

## 14. Related repository surfaces

| Surface | Current role | Boundary |
|---|---|---|
| [Directory Rules v2](../../doctrine/directory-rules.md) | Adopted placement and responsibility authority through ADR-0029 | Does not authorize a rollback or release |
| [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Accepted directory-governance decision | Supports same-path placement only |
| [Runbooks README](../README.md) | Operational-procedure boundary | Runbooks describe actions; they do not grant authority |
| [Synthetic rollback rehearsal](../rollback-rehearsal.md) | Concise cross-domain operator entry point | Same generic helper; no domain or public authority |
| [Hazards Rollback Runbook](ROLLBACK_RUNBOOK.md) | Broader draft domain procedure | Verify current paths and operational assumptions before use |
| [Hazards Promotion Runbook](PROMOTION_RUNBOOK.md) | Repository-grounded promotion preflight | Current Hazards promotion remains held |
| [Not-for-Life-Safety Audit](NOT_FOR_LIFE_SAFETY_AUDIT_RUNBOOK.md) | Public-boundary audit procedure | Required for any later public-facing Hazards scenario |
| [Rollback helper](../../../tools/release/rollback_apply.py) | Implemented marker-protected synthetic plan/apply engine | Generic, synthetic-only, no policy/review/release authority |
| [Generic focused tests](../../../tests/release/test_synthetic_rollback_rehearsal.py) | Eight executable positive and negative helper cases | Shared regression coverage |
| [Hazards fixture](../../../fixtures/domains/hazards/synthetic_rollback_rehearsal/README.md) | One tracked non-locating stale-context rollback workspace | Synthetic input only; never operational or public state |
| [Hazards focused tests](../../../tests/domains/hazards/test_synthetic_rollback_rehearsal.py) | Four deterministic, apply, preservation, and fail-closed cases | First milestone-specific rehearsal command |
| [Release root](../../../release/README.md) | Release-governance boundary | Canonical records and decisions stay separate from the helper report |

The read-only Greenfield Commissioning Plan v2 informed the measurable drill, correction-cascade, and smallest-complete-circle framing. It remains a planning reference and does not prove repository implementation. The Notion Alignment Register remains coordination-only and does not authorize rollback or change repository, review, release, deployment, promotion, or publication state.

[Back to top](#top)

---

## 15. Runbook maintenance and rollback

This revision adds one reusable synthetic Hazards fixture and four executable domain tests, then reconciles this runbook and the adjacent fixture/test indexes. It changes no generic helper behavior, source admission, lifecycle data, schema, contract, policy, candidate, governed review, canonical correction or rollback object, release, deployment, promotion, publication, or repository setting.

### Validation for a future edit

1. Re-pin current `main`, target blob, helper blob, test blob, sibling runbooks, and open overlap.
2. Re-read accepted Directory Rules and applicable ADRs.
3. Reinspect the helper's marker, path, scenario, digest, invalidation, preservation, report, and exit-code contracts.
4. Recount and execute the focused tests at the exact head.
5. Recheck tracked Hazards/release fixture families before claiming domain coverage.
6. Verify every relative link and command against current bytes.
7. Read back the committed file and inspect the pull-request diff.

### Rollback of this documentation change

Before merge, close the draft pull request and remove only its task branch if separately authorized. After merge, use a reviewed revert or forward-fix pull request covering the tracked fixture, its domain test, and the three documentation/index updates together. Do not delete a fixture while leaving its test or runbook claim behind.

No real release, alias, cache, catalog, artifact, source, policy decision, deployment, promotion, publication, or public state is touched by reverting this synthetic slice.

[Back to top](#top)
