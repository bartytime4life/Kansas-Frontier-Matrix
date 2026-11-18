<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://runbook/governance/mrts-06-conformance-refresh-2026-11-18
title: MRTS-06 Conformance Evidence Refresh — 2026-11-18
version: v1.0.0
type: runbook
status: proposed; evidence-checkpoint; blocked; non-authoritative
owner: "@bartytime4life — current CODEOWNERS route; independent acceptance pending"
created: 2026-11-18
updated: 2026-11-18
owning_root: docs/
responsibility: Explain the 2026-11-18 successor conformance report, its execution binding, prerequisite readback, remaining blockers and reversible handoff, and preserve every earlier report.
policy_label: internal-governance; process-evidence-only; non-release
truth_posture: CONFIRMED bounded local executions and GitHub readback at the cited head / PROPOSED successor evidence / NOT_RUN independent acceptance, final-candidate hosted conformance and operational rollback
related:
  - docs/runbooks/mrts-06-ci-conformance-handoff.md
  - docs/runbooks/mrts-06-conformance-refresh-2026-10-08.md
  - artifacts/qa/validation/milestone-1/ci_conformance_report_2026-11-18.json
  - artifacts/qa/validation/milestone-1/ci_conformance_evidence_2026-11-18.json
  - data/receipts/generated/genrec-ci-conformance-report-successor-20261118.json
[/KFM_META_BLOCK_V2] -->

# MRTS-06 conformance evidence refresh — 2026-11-18

The [successor report](../../artifacts/qa/validation/milestone-1/ci_conformance_report_2026-11-18.json)
records results at `main@3e4137714e97c960dad7cf10e973481559a14782`, tree
`cc87c4c9fe1452f2a34c472fba25b37be38f6838`:

- topology is `PASS`;
- governance parity is `HOLD_INHERITED`.

The report is `BLOCKED` process evidence with four unresolved items. It
does not accept the milestone and does not select a final acceptance target.
`repository.final_sha` and `closure.target_sha` stay null.

It follows the [2026-10-08 refresh](mrts-06-conformance-refresh-2026-10-08.md)
and uses the same schema, validator, renderer and procedure. Neither that
report nor the August report is changed.

## What changed since 2026-10-08

| Item | 2026-10-08 at `ebcc4988…` | 2026-11-18 at `3e413771…` |
|---|---|---|
| Tracked paths | 14,244 | 15,313 |
| Topology baselined warnings | 113 | 89 |
| New drift, invariant failures, stale fingerprints | 0, 0, 0 | 0, 0, 0 |
| Parity resolved fingerprints against its historical base | 11 | 35 |
| Topology baseline expiry | 2026-11-10 | 2027-05-10. It was renewed once on main on 2026-10-14. |
| Exact-main push workflow runs | 51, with water-pilot failing; 106 check runs: 103 success, 1 failure, 2 skipped | 52: 51 success, 1 skipped (APIsec), 0 failed |
| water-pilot | FAIL, `MIRROR_REVIEW_REQUIRED` | SUCCESS |
| Validator registry entries | 28 | 29 |
| Native milestone 1 | 5 open, 5 closed; due 2026-09-18 | 5 open, 6 closed; due 2026-11-10, now past |

Renewing the baseline expiry keeps the topology lane from failing on
2026-11-11. The renewal is not a waiver, an owner disposition of the 89
warnings, or a closure decision. This report infers none of those.

## Execution and schema binding

The [evidence sidecar](../../artifacts/qa/validation/milestone-1/ci_conformance_evidence_2026-11-18.json)
records the following for each of the 16 local commands:

- the execution head and tree;
- start and end times;
- the exit code;
- a clean-worktree observation;
- an output digest.

It also holds the full topology result, the full parity result and a bounded
GitHub readback.

The checks ran in a detached worktree of `main@3e413771…`, before this
evidence diff was written. Their PASS results describe that commit, not this
PR's head.

### Environment

- Python 3.13.18, with the versions `pyproject.toml` declares: jsonschema
  4.26.0, PyYAML 6.0.3, rfc8785 0.1.4, rfc3339-validator 0.1.4, pytest 9.1.1
  and Hypothesis 6.168.5.
- Validation used `KFM_NO_NETWORK=1`, `PYTHONDONTWRITEBYTECODE=1`,
  `PYTHONHASHSEED=0` and UTC.

The first full run lacked Hypothesis, rfc8785 and rfc3339-validator. In that
run, `repository-governance-parity` and `trust-spine-fixture-slice` failed
with `ModuleNotFoundError` and `HASHING_UNAVAILABLE`. Those records were
discarded. With the declared versions installed, all 16 commands were rerun
from the start, with no source edits, and every one exited 0. The sidecar's
`execution_limits` records this.

### Schema, validator and digests

The [v1 schema](../../schemas/contracts/v1/governance/ci_conformance_report.schema.json)
and [validator/renderer](../../tools/validators/governance/validate_ci_conformance_report.py)
are unchanged. The renderer does not discover or execute checks.

Every governing, registry, schema, policy, validator and fixture digest was
recomputed against `3e413771…`. ADR-0029's recorded version moves from v1.4 to
v1.5 to match the base tree.

The sidecar is hashed as a `CANDIDATE_TREE` generated-artifact ref. Its own
`sha256` field uses the same method as before: SHA-256 of sorted compact UTF-8
JSON, with that field removed.

## Current local results

| Command | Result at `3e413771…` | Limit |
|---|---|---|
| `make repository-topology` | PASS: 92 topology unit tests, 6 Make-target tests, 29 correction-register tests. 15,313 paths, 0 invariant, 0 new drift, 89 baselined warnings, 0 stale entries. | Ratchet success keeps the warning debt. |
| `make repository-governance-parity` | Profile integrity PASS with 0 findings. Conformance HOLD_INHERITED. 17 tests, fixture polarity and the topology-recovery receipt. | 89 baseline warnings remain a closure hold. |
| `make trust-spine-baseline` | PASS: 11 tests, fixtures, pinned projection and historical receipt. | The pinned MRTS-01 baseline is not a newly accepted authority snapshot. |
| `make control-plane-registry-packet` | PASS: 16 tests, seven registry instances, fixtures and receipt. | Retained ABSENT, CONFLICTED and UNKNOWN states need governance acceptance. |
| `make trust-spine-fixture-slice` | PASS: 15 tests, negative fixtures, 11-artifact flow, ten canonical lanes and receipt. | Synthetic evidence only. No API or Site integration, and no operational rollback. |
| `make ci-conformance-report` before this diff | Integrity PASS: 28 receipt tests, 15 report tests, fixture cases, the August report and receipt, and the 2026-10-08 report and receipt. | Validates earlier reports; does not refresh their observations. |
| `make validator-registry-check` and the fixture-root validator | PASS: 29 aggregate validator entries. | Registry and fixture-root shape only, not full-repository validation. |
| `make workflow-security` | PASS: 28 tests and the source scanner. | Does not prove effective merge protection. |
| `make release-dry-run` | PASS: expected publication denials, 4 unittest cases and 2 synthetic closure tests. | No release candidate, decision, publication or operational rollback. |
| Exact-ancestor historical receipt replay | PASS for MRTS-01, -02, -04 and -05, both conformance receipts, the publication-deny dry run, the release dry run and the ReleaseManifest receipt. | Historical bytes only. Review remains pending. |

## Unresolved items

There are still four blockers. Their IDs are unchanged from 2026-10-08.

| Item | Current state |
|---|---|
| `GOVERNANCE_BASELINE_WARNINGS_HOLD` | Topology passes. Parity holds on 89 baselined warnings, with 0 findings and 0 introduced. `failures.inherited` holds only `BASELINED_WARNINGS=89`. |
| `HOSTED_EXACT_HEAD_CHECKS_NOT_RUN` | The 52 aggregate push runs at the exact head have 0 failures. No dedicated ci-conformance, baseline, registry-packet, parity or fixture-slice workflow run exists at that head. The successor PR head is not yet run. |
| `HUMAN_REVIEW_PENDING` | Reviewer IDs are empty, approval time is null and review is PENDING. |
| `MILESTONE_ISSUES_REMAIN_OPEN` | #3358 is closed. #3359, #3360, #3361, #3363 and #3364 are open. The renewed milestone due date has passed. |

`failures.introduced=[]` describes the measured clean snapshot. The candidate
still needs its own validation of the changed tree.

## Prerequisite readback

Issue and milestone state were read on 2026-11-18 at 02:10 UTC. The sidecar
records the latest comment ID for each issue.

| Prerequisite | State | Remaining acceptance |
|---|---|---|
| [#3358 MRTS-01](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3358) | CLOSED; local lane passes | The closure is an issue state, not independent acceptance of this successor. |
| [#3359 MRTS-02](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3359) | OPEN; no new comment since 2026-09-17 | Governance disposition of the retained ABSENT, CONFLICTED and UNKNOWN states; final-head hosted binding. |
| [#3360 MRTS-03](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3360) | OPEN; the register still declares 10 conflicted required families | Family-level semantic acceptance and consumer and owner disposition. |
| [#3361 MRTS-04](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3361) | OPEN; latest comment 2026-10-13 | Disposition of the baseline debt, plus the #4024 and #4228 boundaries. |
| [#3363 MRTS-05](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3363) | OPEN; local synthetic lane passes | Independent fixture acceptance and final-head hosted binding. |
| [#3364 MRTS-06](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3364) | OPEN / BLOCKED | Final target, complete hosted evidence, independent acceptance and blocker disposition. |

### Milestone 1 and related issues

- Native milestone 1 is titled `Milestone` and is open, with 5 open and 6
  closed issues.
- On 2026-10-14 the owner moved its due date to `2026-11-10T00:00:00Z`. That
  date has passed without closure, and this refresh changes no milestone
  setting.
- The 2026-10-14 comment on #3364 asked whether the baselined warnings block
  closure. This report does not answer that.
- #4024 remains open. Its 2026-10-13 comment records a main ruleset that
  requires status checks, asks whether that rule meets the recovery gate, and
  is still unanswered. This report does not infer platform-control proof from
  green source checks.
- #4228 remains open, with no new comment since 2026-09-21.

## Hosted evidence at the measured head

Readback used `list_workflow_runs` for `branch=main`, `event=push`, filtered to
the exact head SHA. It returned 52 runs: 51 success and 1 skipped.

Individual check runs and jobs were not enumerated. The sidecar's
`check_count` and `check_conclusions` are therefore null, not zero.

| Workflow | Exact-main observation | Consequence |
|---|---|---|
| [validator-suite](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/44219736423) | SUCCESS | Aggregate evidence at the observed head only. Dedicated MRTS conformance is still NOT_RUN. |
| [release-dry-run](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/44219736291) | SUCCESS | Synthetic dry-run scope only. |
| [object-family-register](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/44219736136) | SUCCESS | Register validation does not accept the ten conflicted required families. |
| [water-pilot](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/44219736196) | SUCCESS | The 2026-10-08 mirror-review failure is not present at this head. |
| [APIsec](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/44219736292) | SKIPPED | Not PASS. Separate scope and disposition. |
| Dedicated ci-conformance, baseline, registry-packet, governance-parity and fixture-slice workflows | No push run at this head | Missing exact-head dedicated evidence is kept as NOT_RUN. |

The report's hosted-run entries carry their actual `head_sha`. They are
observations of base main, not hosted validation of this successor. The
aggregate hosted-success criterion stays false.

This refresh does not run browser or WebGL checks, a full local repository
suite, an operational rollback or independent acceptance.

## Validation and reproducibility

`make ci-conformance-report` now also validates this successor and its receipt.
The earlier reports, fixture matrix and exact-ancestor receipt replays stay in
place.

```sh
make ci-conformance-report
```

```sh
python tools/validators/governance/validate_ci_conformance_report.py \
  artifacts/qa/validation/milestone-1/ci_conformance_report_2026-11-18.json --render
```

Repeated `--render` output must equal the committed canonical bytes, and it
does.

Focused negative probes were run against this report. Each was rejected with
its specific code:

- a CHECK_NOT_RUN outcome changed to PASS: `CHECK_OUTCOME_INVALID`;
- an unsupported READY closure: `CLOSURE_*` findings;
- a changed governing digest: `REF_DIGEST_MISMATCH`;
- an enabled authority flag: `AUTHORITY_EFFECT_DENIED`.

These probes check report integrity. They do not approve the recorded
evidence.

A future refresh must collect new execution records and emit a new dated
successor, rather than relabel this one.

## Preservation and rollback

The August report, the 2026-10-08 report and sidecar, and all their receipts
stay byte-identical. The sidecar's `predecessor_evidence` records the
2026-10-08 sidecar file hash and report digest.

- **Before integration:** abandon this unaccepted candidate.
- **After separately authorized integration:** revert this report, sidecar,
  receipt and runbook together with the two Makefile lines and two navigation
  updates. Alternatively, add a dated correction that preserves evidence
  lineage.

Keep every historical receipt hash and exact-ancestor replay ref.

No release, runtime, Site or public state was changed, and no operational
rollback proof is claimed. AI authorship, generation, validation and hosted
successes are kept separate from review, acceptance, ready, merge, release and
publication.
