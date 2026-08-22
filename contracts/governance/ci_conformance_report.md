<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/ci-conformance-report/v1
title: CIConformanceReport Milestone Evidence Contract
version: v1.0.0
type: semantic-contract
status: proposed; repository-grounded; non-authoritative; non-release
owners: Validation/CI steward; Control-plane steward; Release steward; Repository owner
created: 2026-08-22
updated: 2026-08-22
responsibility_root: contracts/
owning_root: contracts/
responsibility: define a deterministic machine-readable milestone conformance inspection record and closure-evidence block without granting review merge release deployment promotion publication public-route issue-close or milestone-close authority
policy_label: internal-governance; cite-or-abstain; no-self-authority; no-network-validation
truth_posture: CONFIRMED adopted Directory Rules and accepted ADR bytes merged MRTS-01 through MRTS-05 artifacts local focused validation observations and inherited topology counts / PROPOSED this contract schema report validator fixtures workflow receipt and handoff / UNKNOWN eventual final SHA hosted exact-head results branch protection independent review release state deployed behavior and public behavior / NEEDS VERIFICATION MRTS-06 review and merge hosted checks human approval issue closure and milestone exit criteria
related:
  - ../../artifacts/qa/validation/milestone-1/ci_conformance_report.json
  - ../../schemas/contracts/v1/governance/ci_conformance_report.schema.json
  - ../../fixtures/contracts/v1/governance/ci_conformance_report/README.md
  - ../../tools/validators/governance/validate_ci_conformance_report.py
  - ../../tools/validators/validate_generated_receipt.py
  - ../../tests/validators/governance/test_validate_ci_conformance_report.py
  - ../../tests/validators/test_validate_generated_receipt.py
  - ../../docs/runbooks/mrts-06-ci-conformance-handoff.md
  - ../../.github/workflows/ci-conformance-report.yml
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
notes:
  - This contract implements the bounded repository portion of MRTS-06 for milestone KFM-MS-MRTS-001.
  - The canonical initial report is BLOCKED because exact-final-head hosted evidence and human review do not exist.
  - Passing validation proves report integrity only; it does not prove milestone conformance or authorize an effect.
[/KFM_META_BLOCK_V2] -->

# CIConformanceReport milestone evidence contract

## Purpose

`CIConformanceReport` is a deterministic inspection record for one exact
milestone evidence checkpoint. It binds repository state, adopted authority
bytes, registry/schema/policy/validator versions, a fixture digest, finite
check outcomes, inherited and introduced failures, generated artifact
digests, unresolved work, and a closure block.

The canonical MRTS-06 candidate is
[`artifacts/qa/validation/milestone-1/ci_conformance_report.json`](../../artifacts/qa/validation/milestone-1/ci_conformance_report.json).
Its location is a non-authoritative QA inspection lane. A material process
receipt belongs separately in `data/receipts/generated/`.

## Authority boundary

The report observes evidence; it cannot manufacture the evidence it records.

| Concern | Owning surface | Report effect |
| --- | --- | --- |
| Placement authority | Adopted Directory Rules and accepted ADRs | Bind exact version and digest only |
| Object meaning and shape | `contracts/` and `schemas/` | Declare versions and validate shape |
| Admissibility | `policy/` and authenticated policy decisions | Record pinned policy source; never decide |
| Run/review evidence | Hosted workflow records and human review | Cite exact evidence only after it exists |
| Release and rollback | `release/` plus governed approvals | Record references; never approve or execute |
| Public behavior | Governed deployed runtime | Not established by repository inspection |

`authority_mode` is always `process_evidence_only`. Every effect flag is
`false`. A generated receipt is process memory and cannot approve its own
report, release, or closure.

## Repository and digest binding

`repository.base_sha` identifies the merged base inspected when the candidate
was authored. A reference with `scope: BASE_TREE` is replayed with `git
cat-file` from that commit. A `CANDIDATE_TREE` reference is replayed from the
bounded current worktree and is appropriate for proposed files absent from
the base.

`repository.final_sha` and `closure.target_sha` stay `null` until the exact
final milestone head exists. They must match when populated.

`report_digest` and the tracked-generated-payload provenance field `sha256`
carry the same SHA-256 over RFC 8259 JSON with sorted keys, compact separators,
UTF-8 encoding, finite numbers, and both digest fields removed. The stored file
itself must equal sorted, two-space-indented canonical JSON plus one trailing
newline. The report cannot list itself as a hashed reference; that would create
a digest cycle.

## Check states and outcomes

Execution state and outcome are separate closed vocabularies.

| Execution state | Allowed outcome |
| --- | --- |
| `EXECUTED_LOCAL` | `PASS`, `FAIL`, or `HOLD_INHERITED` |
| `EXECUTED_HOSTED` | `PASS`, `FAIL`, or `HOLD_INHERITED` |
| `CHECK_NOT_RUN` | `CHECK_NOT_RUN` only |
| `SKIPPED` | `SKIPPED` only |

`CHECK_NOT_RUN` is missing evidence. `SKIPPED` is an intentional exclusion.
Neither can be translated into `PASS`. `HOLD_INHERITED` retains a real
blocking condition while separating it from a candidate-introduced failure.

The report status is finite:

- `NONCONFORMANT` when a check fails or the candidate introduces a failure;
- `BLOCKED` when required evidence is missing, inherited holds remain, or a
  blocking unresolved item exists;
- `CONFORMANT` only when no such condition remains.

## Closure discipline

`closure.state` begins as `BLOCKED`. A `READY` or `CLOSED` record requires all
of the following in the same exact report:

1. identical non-null repository final and closure target SHAs;
2. every required exit criterion set true with evidence;
3. one or more hosted workflow URLs whose successful runs bind that exact SHA;
4. approved human review with reviewer identity and timestamp;
5. zero blocking unresolved items;
6. every required check recorded as `PASS`.

`CLOSED` additionally requires a closer, closure time, and closed milestone
state. These fields record an independently authorized action; the report and
validator never authorize it.

## Deterministic validation

Run:

```bash
make ci-conformance-report
```

The target performs focused unit tests, exact negative-case polarity,
canonical report validation, and generated-receipt hash replay without
network access. `--render` emits canonical bytes to standard output; repeated
runs must be byte-identical.

Historical authoring receipts are never rewritten to follow successor edits.
When a later milestone changes a shared artifact such as `Makefile`, replay
uses `validate_generated_receipt.py --artifact-git-ref <exact-ancestor-sha>`.
The validator accepts only a lowercase 40-character commit that exists and is
an ancestor of the tested head, then reads regular blobs from that immutable
tree. Mutable branch names, tags, symlinks, missing blobs, digest drift, and
non-ancestor commits fail closed.

## Correction and rollback

Correct a current candidate with a same-path forward fix, preserve historical
receipts, and regenerate every affected digest. If the integration itself is
wrong, revert the contract, schema, validator, fixtures, workflow, Make target,
report, runbook, registry entry, and generated authoring receipt as one unit.
Never rewrite an already reviewed historical report to make later evidence
appear earlier. Preserve historical receipt hashes and update only the replay
command to cite the exact authoring tree when shared successor files advance.

## Non-effects

Creation or validation of a report does not:

- approve human review or merge;
- waive or expand a drift baseline;
- accept an ADR, schema candidate, registry proposal, or policy;
- activate or admit a source;
- mutate lifecycle state;
- approve or perform release, deployment, promotion, publication, or routing;
- close an issue or milestone;
- prove hosted, deployed, production, or public behavior.
