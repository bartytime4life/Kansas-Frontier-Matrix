<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook-quarantine-handling
title: Quarantine Handling Runbook
type: runbook
version: v2.0
prior_version: v1
status: draft; repository-grounded; procedure-and-rehearsal-only; live-writer-unverified
owners:
  - "@bartytime4life — verified GitHub review route"
  - "NEEDS VERIFICATION — data, policy, rights, sensitivity, domain, and independent-review assignments"
created: 2026-05-12
updated: 2026-09-01
policy_label: restricted-review; no-direct-public-path; release-gated
current_path: docs/runbooks/QUARANTINE_HANDLING.md
owning_root: docs/
responsibility: "Guide bounded quarantine triage, candidate-record validation, accountable review handoff, reprocessing, correction escalation, and fail-closed operation without granting lifecycle, review, release, or publication authority."
truth_posture: cite-or-abstain
truth_labels: [CONFIRMED, PROPOSED, UNKNOWN, NEEDS VERIFICATION, CONFLICTED, HOLD]
authority_class: explanatory operational procedure
authority_rank: subordinate to accepted doctrine and ADRs, contracts, schemas, policy, evidence, review, lifecycle, correction, rollback, and release authorities
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  prepared_base_commit: 246573b531ecfa4b221c08f25a28e6ae762cfd9f
  reconciled_base_commit: 6a4b988784c31583af5d1cded3b2654360c1c123
  target_prior_blob: 845f72f6b98d3d385b483a21fece783b9ede4426
  target_prior_sha256: 2e61b576982fdfcbd4b1afca1e0bf43a9d7e3f9f050f2a6df1fa488c2b807d80
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - docs/doctrine/trust-membrane.md
  - docs/doctrine/retention.md
  - docs/adr/ADR-0021-quarantine-has-structured-exit-paths.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - data/quarantine/README.md
  - contracts/governance/governed_run_chain.md
  - schemas/contracts/v1/governance/quarantine_record.schema.json
  - schemas/contracts/v1/governance/governed_run_chain.schema.json
  - tools/validators/governance/validate_governed_run_chain.py
  - apps/workers/src/quarantine_review_worker/README.md
tags: [kfm, runbook, lifecycle, governance, quarantine, fail-closed, review]
notes:
  - "This runbook explains bounded current repository capability and held operational work; it does not create a writer, reviewer, lifecycle transition, release, or publication authority."
  - "ADR-0021's five-exit model remains proposed and must not be represented as accepted or executable."
  - "The current QuarantineRecord and GovernedRunChain validator profile is fixture-first and no-network; a pass proves shape and linkage only."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Quarantine Handling Runbook

> Use this runbook to identify a quarantine condition, preserve the affected
> material and its lineage, create or rehearse the repository's bounded
> control-plane record, and hand the case to accountable review without
> bypassing KFM's lifecycle or trust membrane.

**Current operating result:** `REPOSITORY_REHEARSAL_AVAILABLE / LIVE_QUARANTINE_WRITER_HELD`

> [!IMPORTANT]
> `QUARANTINE` is a governed fail-closed hold, not a staging directory. Material
> leaves only through reprocessing plus review. A file move, successful
> validator, pull request, merge, or dashboard status is not a lifecycle
> transition and never authorizes public use.

> [!CAUTION]
> Do not place secrets, private endpoints, protected personal information,
> genomic material, sovereign or cultural material, or harmful-precision
> locations in an ordinary public-repository path. Preserve references and
> public-safe audit facts here; use an approved restricted system for protected
> bytes.

**Quick navigation:** [Purpose](#purpose-and-scope) · [Current capability](#current-capability) · [Authority](#authority-boundary) · [Lifecycle](#lifecycle-boundary) · [Triage](#triage) · [Record](#quarantine-record) · [Validation](#bounded-validation) · [Entry](#entry-procedure) · [Review](#review-and-disposition) · [Corrections](#correction-and-revocation) · [Incidents](#incident-escalation) · [Checklists](#operator-checklists) · [Gaps](#open-verification-register) · [References](#related-repository-surfaces)

---

<a id="purpose-and-scope"></a>

## 1. Purpose and scope

This runbook covers repository-grounded handling for material that is, or may
need to be, held in KFM `QUARANTINE` because identity, provenance, source role,
rights, sensitivity, schema, geometry, time, evidence, validation, policy,
review, correction, or rollback requirements are unresolved.

Use it to:

- distinguish refusal, quarantine, hold, error, denial, and revocation;
- preserve subject identity, content hash, run linkage, policy linkage, reasons,
  obligations, time, and resolution lineage;
- rehearse the proposed `QuarantineRecord` and `GovernedRunChain` profile with
  tracked fixtures and deterministic no-network validation;
- prepare a public-safe review handoff without exposing protected material; and
- keep remediation, reprocessing, review, lifecycle transition, correction,
  rollback, release, and publication authority separate.

Do not use it to:

- authorize a live connector, writer, queue, worker, reviewer, or scheduled job;
- copy a quarantined item directly into `PROCESSED`, `CATALOG / TRIPLET`, or
  `PUBLISHED`;
- treat a fixture, schema pass, receipt, policy-shaped record, or generated
  summary as evidence closure or accountable approval;
- invent reason-code semantics, retention periods, reviewer identities, or
  storage controls; or
- reveal protected bytes, exact sensitive locations, restricted source
  locators, credentials, or unsafe operational detail.

[Back to top](#top)

---

<a id="current-capability"></a>

## 2. Current capability

The repository contains a useful but bounded validation slice. It does not yet
contain a verified end-to-end quarantine service.

| Surface | Current repository evidence | What it does not prove |
|---|---|---|
| Canonical lane | [`data/quarantine/README.md`](../../data/quarantine/README.md) defines the fail-closed path boundary and prohibits direct public use. | Active writers, recursive payload conformance, approved restricted storage, or runtime enforcement. |
| Semantic linkage | [`contracts/governance/governed_run_chain.md`](../../contracts/governance/governed_run_chain.md) defines a fixture-first linkage across run, policy, quarantine, and promotion records. | Live policy evaluation, review, lifecycle mutation, promotion, release, or publication. |
| Machine shapes | Proposed closed schemas exist for [`QuarantineRecord`](../../schemas/contracts/v1/governance/quarantine_record.schema.json) and [`GovernedRunChain`](../../schemas/contracts/v1/governance/governed_run_chain.schema.json). | Accepted object authority, an operational case store, or the five exits proposed by ADR-0021. |
| Validator | [`validate_governed_run_chain.py`](../../tools/validators/governance/validate_governed_run_chain.py) performs deterministic JSON, schema, and cross-object linkage checks. | Authentication, reference resolution, signature checks, OPA execution, human review, or state changes. |
| Fixtures and tests | Four valid outcomes and fail-closed negative fixtures are tracked with focused tests. | Production data fitness, operational readiness, source admission, or public safety. |
| Review worker | [`quarantine_review_worker`](../../apps/workers/src/quarantine_review_worker/README.md) has a detailed boundary README and a one-line comment-only `main.py`. | An executable worker, queue consumer, schedule, receipt writer, review route, or deployment. |
| Structured exits | [ADR-0021](../adr/ADR-0021-quarantine-has-structured-exit-paths.md) proposes five governed exits. | Acceptance or implementation; its status remains `proposed`. |

### 2.1 Current finite validation outcomes

The tracked `GovernedRunChain` profile recognizes this matrix:

| Chain outcome | Required linkage | Forbidden linkage | Bounded meaning |
|---|---|---|---|
| `PROMOTABLE` | Successful `RunReceipt`, promotion-family `PolicyDecision.outcome = ANSWER`, no quarantine record, and matching `PromotionDecision.decision = APPROVE` | Any `QuarantineRecord` | The fixture linkage is internally consistent; no lifecycle or release action occurs. |
| `QUARANTINED` | Promotion-family `PolicyDecision.outcome = DENY` and linked record state `QUARANTINED` | Any `PromotionDecision` | The candidate remains outside a higher-trust state. |
| `HELD` | Promotion-family `PolicyDecision.outcome = ABSTAIN` and linked record state `HELD` | Any `PromotionDecision` | An obligation or authority requirement remains unresolved. |
| `ERROR` | Failed `RunReceipt` and promotion-family `PolicyDecision.outcome = ERROR` | Quarantine or promotion record | The bounded validation chain failed operationally; it is not a denial or clearance. |

Unknown, contradictory, or mixed combinations fail closed.

[Back to top](#top)

---

<a id="authority-boundary"></a>

## 3. Authority boundary

GitHub repository evidence is the authority for current implementation. Accepted
ADRs and adopted Directory Rules govern architecture and placement. Doctrine
governs lifecycle and trust semantics. Contracts define meaning, schemas define
shape, policy governs admissibility, reviewers supply accountable judgment,
lifecycle writers perform state transitions, and release authorities own
release or publication decisions.

This runbook is subordinate to all of them.

| Action | This runbook may guide | Separate authority required |
|---|:---:|---|
| Inspect repository evidence and protected references safely | Yes | Read authorization for any restricted system |
| Run tracked no-network fixtures and tests | Yes | Repository execution environment |
| Prepare a candidate `QuarantineRecord` for review | Yes | An accepted writer and storage boundary before persistence |
| Decide rights, sensitivity, sovereignty, or source-role posture | No | Accountable specialist or steward review |
| Approve, reject, release, or retire a quarantined subject | No | Accepted review and lifecycle authority |
| Move bytes between lifecycle stages | No | Accepted idempotent lifecycle writer plus required receipts |
| Correct, withdraw, roll back, release, deploy, or publish | No | Owning correction, rollback, release, and operational authorities |

### 3.1 Evidence is not authority

Keep these distinctions explicit:

- A validator pass proves only the validator's declared scope.
- A `RunReceipt` records process memory; it is not a proof or approval.
- A `PolicyDecision` records a policy-family result; it is not a human review.
- A `ReviewRecord` may support a transition; it does not perform one.
- A `PromotionDecision` in a fixture does not promote anything.
- A release artifact is not KFM `PUBLISHED` until the governed release path
  materializes it for an authorized public surface.

[Back to top](#top)

---

<a id="lifecycle-boundary"></a>

## 4. Lifecycle boundary

Preserve the canonical vocabulary exactly:

```text
(Pre-RAW) -> RAW -> WORK / QUARANTINE -> PROCESSED
          -> CATALOG / TRIPLET -> PUBLISHED
```

`QUARANTINE` is a one-way detour from `WORK`, and may also receive a later-stage
artifact when a defect or revocation is discovered. Public exposure is `DENY`.
Material leaves only through reprocessing plus review and returns through
`WORK`; direct `QUARANTINE -> PROCESSED` promotion is forbidden.

### 4.1 Refusal, quarantine, and revocation

| Disposition | Trigger | Required posture |
|---|---|---|
| Refusal | A gate cannot begin because a precondition is absent or invalid. | Keep the subject in its current stage and record the refusal safely. Do not fabricate a quarantine transition. |
| Quarantine | Gate preconditions are present but a check fails, or rights, sensitivity, source-role, policy, or review logic fails closed. | Preserve the subject and lineage in the governed hold; prevent public and downstream use. |
| Revocation | New evidence, rights change, correction, or re-check invalidates a prior warrant. | Contain the affected subject, propagate correction impact, and preserve prior release history. |
| Error | The validator or operating environment cannot produce a reliable result. | Stop; report `ERROR`; do not translate an operational failure into approval, denial, or clearance. |

### 4.2 Placement is not transition

The doctrinal materialization is:

```text
data/quarantine/<domain>/<reason>/<run_id>/
```

That shape does not authorize a writer or make public-repository storage safe.
The canonical lane README states that protected material requires approved
storage and access controls outside ordinary public paths. A future accepted
writer must bind the logical `QUARANTINE` state to the correct storage system,
receipt family, retention profile, access policy, and reviewer route.

[Back to top](#top)

---

<a id="triage"></a>

## 5. Triage

### 5.1 Stop and contain

When a possible quarantine condition appears:

1. Stop the affected candidate from advancing.
2. Preserve the originating subject, stage, content digest, run identity, and
   existing receipts without modifying the source capture.
3. Prevent public, search, map, export, graph, AI, tile, or report consumers from
   receiving the quarantined subject.
4. Minimize logs and handoffs to public-safe identifiers and finite reason
   codes. Do not copy protected payloads into issues, pull requests, chat,
   ordinary logs, or public repository fixtures.
5. Determine whether the event is a refusal, quarantine, revocation, or
   operational error. If evidence is insufficient, remain held and escalate.

### 5.2 Classify the trigger without inventing authority

| Trigger family | Examples | First safe disposition |
|---|---|---|
| Identity or integrity | Unstable identifier, duplicate identity, content-hash mismatch, unresolved lineage | `HELD` or `ERROR`, depending on whether the check ran reliably |
| Source and rights | Missing SourceDescriptor, incompatible source role, unknown or withdrawn rights | `QUARANTINED` or policy `DENY` |
| Sensitivity and sovereignty | Harmful precision, living-person or genomic data, rare species, archaeology, infrastructure, cultural or sovereign concerns | `QUARANTINED`; restricted accountable review required |
| Shape and semantics | Schema failure, invalid geometry, unit or CRS mismatch, unsupported time expression | `QUARANTINED` when the check completed; `ERROR` when it could not run |
| Evidence and citation | Missing or unresolved `EvidenceRef`, incomplete EvidenceBundle, citation mismatch | `HELD`, `QUARANTINED`, or public-surface `ABSTAIN` |
| Policy and review | `DENY`, `ABSTAIN`, missing reviewer authority, separation-of-duties conflict | `QUARANTINED` or `HELD`; never self-approve |
| Correction and rollback | Published claim invalidated, source withdrawn, downstream derivatives unresolved | Revocation and correction escalation; preserve prior history |

Reason codes in the current schema are syntactically constrained uppercase
tokens, but their complete canonical vocabulary and semantics are not accepted.
Reuse a reason code only when an owning contract or policy defines it. Otherwise
record the case as held and identify the vocabulary decision as unresolved.

[Back to top](#top)

---

<a id="quarantine-record"></a>

## 6. `QuarantineRecord`

The tracked proposed schema is a closed control-plane shape. It is not the full
case model proposed by ADR-0021 and does not settle the older
`quarantine_case_record` naming or exit-grammar conflict.

### 6.1 Required fields

| Field | Current schema rule | Operator purpose |
|---|---|---|
| `record_id` | Stable lowercase identifier matching the schema pattern | Join the hold and its later resolution without relying on a path |
| `subject_ref` | Non-empty, whitespace-free reference | Identify the affected subject without embedding its protected payload |
| `spec_hash` | `sha256:` plus 64 lowercase hex characters | Bind the record to exact candidate bytes or canonical specification |
| `run_receipt_ref` | Non-empty, whitespace-free reference | Link the process attempt |
| `policy_decision_ref` | Non-empty, whitespace-free reference | Link the exact policy-family result |
| `state` | `QUARANTINED`, `HELD`, `RELEASED`, or `REJECTED` | Record the bounded control-plane state |
| `reason_codes` | One to 64 unique uppercase tokens | Give finite, machine-readable causes without leaking protected detail |
| `obligations` | Up to 64 unique bounded strings | State what must be resolved before a later decision |
| `recorded_at` | RFC 3339 / JSON Schema date-time | Preserve event time |
| `resolution_ref`, `resolved_at` | Required only for `RELEASED` or `REJECTED`; forbidden for open `QUARANTINED` or `HELD` states | Bind a closed record to its resolution evidence |

### 6.2 Illustrative schema-valid record

This example matches the tracked `QUARANTINED` fixture. It is synthetic and
creates no live case, policy decision, receipt, or lifecycle effect.

```json
{
  "record_id": "quarantine:sample:quarantined",
  "subject_ref": "kfm://candidate/sample",
  "spec_hash": "sha256:1111111111111111111111111111111111111111111111111111111111111111",
  "run_receipt_ref": "run:sample:quarantined",
  "policy_decision_ref": "policy:sample:quarantined",
  "state": "QUARANTINED",
  "reason_codes": [
    "POLICY_NOT_CLEARED"
  ],
  "obligations": [
    "resolve the recorded policy hold"
  ],
  "recorded_at": "2026-08-07T19:00:00Z"
}
```

### 6.3 Cross-object invariants

Within a `GovernedRunChain`:

- chain and run `spec_hash` values must match;
- any quarantine record must repeat the chain's `subject_ref` and `spec_hash`;
- `run_receipt_ref` must equal the embedded `RunReceipt.run_id`;
- `policy_decision_ref` must equal the embedded
  `PolicyDecision.decision_id`;
- the embedded policy family must be `promotion`;
- `QUARANTINED` and `HELD` require a quarantine record and forbid a promotion
  decision; and
- `PROMOTABLE` forbids a quarantine record and requires an `APPROVE` promotion
  decision bound to the same run.

[Back to top](#top)

---

<a id="bounded-validation"></a>

## 7. Bounded validation

Run validation only against public-safe candidate files or the repository's
tracked synthetic fixtures. The validator is local and no-network by design.

### 7.1 Focused commands

From the repository root:

```bash
python tools/validators/governance/validate_governed_run_chain.py \
  fixtures/contracts/v1/governance/governed_run_chain/valid/quarantined.json
```

Expected bounded result:

```json
{"authority":{"lifecycle_write":false,"network_fetch":false,"policy_evaluation":false,"promotion":false,"publication":false,"release":false,"source_activation":false},"findings":[],"ok":true,"outcome":"ANSWER","scope":"fixture-only-governed-run-chain"}
```

Run the focused test family:

```bash
python -m pytest \
  tests/validators/governance/governed_run_chain/test_validate_governed_run_chain.py
```

For this Markdown change, also run the repository's applicable documentation
metadata, document-graph, and link checks plus `git diff --check`. Exact command
names may evolve; inspect current workflow and validator registries rather than
copying an obsolete invocation from an old runbook edition.

### 7.2 Interpret the result narrowly

| Validator result | Safe interpretation | Forbidden interpretation |
|---|---|---|
| `ANSWER` | JSON safety, schema conformance, and linkage checks passed for the inspected file. | Policy approved, reviewer approved, quarantine cleared, or lifecycle changed. |
| `DENY` | The candidate contradicts a schema or linkage invariant. | The underlying real-world subject is permanently denied or false. |
| `ERROR` | The validator could not produce a trustworthy bounded result. | Retry until green, silently quarantine, or treat the last successful run as current. |

### 7.3 Negative proof

The focused suite includes negative fixtures for a quarantine `spec_hash`
mismatch and a promotion decision that bypasses quarantine. Keep those failures
non-vacuous. Do not weaken the schema, validator, or tests to make a candidate
pass.

[Back to top](#top)

---

<a id="entry-procedure"></a>

## 8. Entry procedure

There is no verified live quarantine writer bound to this runbook. Until one is
accepted, this procedure produces a review candidate or rehearsal result only.

1. **Pin the evidence.** Record the subject reference, current lifecycle stage,
   exact content or specification hash, run reference, validator version, policy
   reference, and time.
2. **Preserve the source.** Do not edit `RAW` in place or delete prior receipts,
   proof, review, release, correction, or rollback history.
3. **Determine the disposition.** Classify refusal, quarantine, revocation, or
   operational error. Unknown or conflicted authority remains `HELD`.
4. **Minimize the record.** Use stable references and public-safe reason codes;
   keep protected payloads and sensitive rationale in an approved restricted
   review system.
5. **Validate the candidate shape.** Use the tracked schema and, when composing
   the full chain, the no-network GovernedRunChain validator.
6. **Bind accountable handoff.** Identify the required domain, rights,
   sensitivity, sovereignty, policy, correction, or release reviewer roles.
   CODEOWNERS routing alone is not review evidence.
7. **Persist only through an accepted writer.** If the writer, path binding,
   access control, receipt family, idempotency rule, or retention profile is
   unresolved, stop at `VALIDATED_CANDIDATE_ONLY`.
8. **Verify containment.** Confirm public routes, indexes, exports, map layers,
   caches, AI surfaces, and downstream derivations cannot resolve the held
   subject.

### 8.1 Entry handoff packet

The public-safe packet should include:

| Field | Required content |
|---|---|
| Subject | Stable opaque reference and affected domain |
| Scope | Originating stage and bounded affected surfaces |
| Integrity | Exact `spec_hash`, run reference, code/schema/validator versions |
| Cause | Finite reason code plus non-sensitive summary |
| Obligations | Concrete unresolved work or authority requirement |
| Evidence | References to validation, policy, review, and source records |
| Containment | Public and downstream paths checked; unresolved exposure stated |
| Ownership | Required reviewer roles and verified contact route |
| Result | `VALIDATED_CANDIDATE_ONLY`, `HELD`, `QUARANTINED`, or `ERROR`, bounded to actual authority |

[Back to top](#top)

---

<a id="review-and-disposition"></a>

## 9. Review and disposition

### 9.1 Review before any exit

Review must verify:

- exact subject identity and lineage;
- the originating gate and reproducible finding;
- rights, sensitivity, sovereignty, source-role, geometry, and time posture as
  applicable;
- closed evidence and resolvable references;
- reviewer competence, independence, and separation of duties;
- remediation, transform, receipt, correction, rollback, and downstream-impact
  requirements; and
- the accepted lifecycle writer and target stage.

If any material item remains unknown, conflicted, stale, or unsupported, the
record remains `HELD` or `QUARANTINED`. A reviewer must not approve their own
sensitive, rights-bearing, correction, or release-affecting work when the owning
policy requires separation.

### 9.2 Reprocessing path

Current lifecycle doctrine requires quarantined material to return through
reprocessing plus review:

1. Remediate the source of the failure without modifying immutable source
   capture or history.
2. Create a new `WORK` artifact with a new `TransformReceipt` through an
   accepted writer.
3. Re-run the original failed check and every downstream gate affected by the
   remediation.
4. Capture the required review record and policy decision.
5. Link the successor to the quarantine record and prior subject.
6. Leave promotion, release, deployment, and publication to their owning
   procedures and authorities.

Direct `QUARANTINE -> PROCESSED`, path-only clearance, and in-place status edits
that erase the open-case history are forbidden.

### 9.3 ADR-0021 five-exit proposal

ADR-0021 proposes these future exits:

| Proposed exit | Current runbook posture |
|---|---|
| Return to `WORK` | Consistent with accepted lifecycle doctrine when performed through reprocessing, review, and an accepted writer. |
| Promote to `PROCESSED` candidate | Do not use directly from `QUARANTINE`; current lifecycle doctrine requires return through `WORK`. |
| Release a safer derivative | Requires a separately governed derivative that traverses the normal lifecycle and release path; the original remains protected. |
| Deny public use | Requires the owning policy/review decision and durable lineage; no silent deletion. |
| Withdraw or correct a release | Requires correction, downstream impact, rollback, and public-notice handling through owning authorities. |

The list is design guidance only. Until the ADR is accepted and its contract,
schema, policy, validators, fixtures, review bindings, writers, and receipts are
aligned, do not encode it as a live state machine or claim five-exit closure.

[Back to top](#top)

---

<a id="correction-and-revocation"></a>

## 10. Correction and revocation

Use [Evidence Correction](./EVIDENCE_CORRECTION.md) when a defect affects an
already released or release-facing claim, and [Rollback Runbook](./ROLLBACK_RUNBOOK.md)
for a separately authorized rollback.

1. Preserve the prior release, evidence, receipt, review, and manifest history.
2. Record the correction or rights/sensitivity change through the accepted
   correction surface.
3. Identify every released derivative, catalog/triplet projection, tile, export,
   report, story, AI response, cache, and downstream subject that depended on
   the revoked warrant.
4. Contain or withdraw affected public surfaces through authorized controls.
5. Re-evaluate downstream evidence and default to `ABSTAIN`, `DENY`, or `HOLD`
   where the warrant no longer closes.
6. Produce a corrected successor only through the normal lifecycle and release
   path with new evidence, review, and rollback bindings.

Quarantine is containment, not deletion. Retention and eventual vacuuming remain
governed by [`retention.md`](../doctrine/retention.md); this runbook does not set
numeric retention periods or erase records.

[Back to top](#top)

---

<a id="incident-escalation"></a>

## 11. Incident escalation

Escalate to [Incident Response](./INCIDENT_RESPONSE.md) when any of these are
observed:

- quarantined or revoked material reached a public UI, API, map, tile, export,
  report, search, graph, or AI surface;
- protected bytes, sensitive coordinates, personal/genomic data, private source
  locators, credentials, or restricted rationale entered an unauthorized path;
- a writer or pipeline bypassed `WORK`, reprocessing, review, policy, receipt,
  correction, rollback, or release gates;
- required evidence or audit history was deleted, rewritten, or made
  unresolvable; or
- the affected scope cannot be bounded reliably.

Do not declare an incident resolved merely because a repository fix validates.
Live containment, evidence custody, accountable review, correction, recovery,
and public notice remain separate operational decisions.

[Back to top](#top)

---

<a id="operator-checklists"></a>

## 12. Operator checklists

### 12.1 Entry or candidate preparation

- [ ] Exact subject, stage, run, content/spec hash, and time are pinned.
- [ ] Source capture and prior audit history remain unchanged.
- [ ] Refusal, quarantine, revocation, and error are distinguished.
- [ ] Reason code is defined by an owning surface or the vocabulary gap is held.
- [ ] Protected payloads remain in an approved restricted system.
- [ ] `QuarantineRecord` shape and cross-object references validate where used.
- [ ] Result is bounded to actual authority; no lifecycle change is implied.
- [ ] Required reviewers and separation-of-duties needs are visible.
- [ ] Public and downstream containment is checked.

### 12.2 Clearance or successor review

- [ ] The original failure reproduces against the pinned subject or is explained.
- [ ] Remediation changes a successor, not immutable history.
- [ ] A new `WORK` artifact and `TransformReceipt` are produced by an accepted writer.
- [ ] The original gate and all affected downstream gates rerun.
- [ ] Evidence, policy, rights, sensitivity, sovereignty, and review obligations close.
- [ ] Successor identity and lineage point back to the quarantine record.
- [ ] No direct `QUARANTINE -> PROCESSED` or public path exists.
- [ ] Correction and rollback impact is resolved for any prior release.
- [ ] Promotion and release remain separate accountable decisions.

### 12.3 Review handoff

- [ ] Only public-safe identifiers, counts, codes, and summaries are exposed.
- [ ] Validation commands, versions, exact results, and limitations are recorded.
- [ ] Introduced and inherited failures are distinguished.
- [ ] Unknown, conflicted, stale, and needs-verification items remain explicit.
- [ ] No reviewer, approval, source activation, lifecycle write, release,
      deployment, promotion, publication, or repository-setting effect is claimed
      without exact evidence.

[Back to top](#top)

---

<a id="anti-patterns"></a>

## 13. Anti-patterns

| Anti-pattern | Why it fails | Correct posture |
|---|---|---|
| Treating `data/quarantine/` as a soft staging folder | Bypasses the governed hold and audit model | Reprocess through `WORK` with review and receipts |
| Direct public reads from quarantine | Breaks the trust membrane | Serve only released public-safe material through governed interfaces |
| Retrying a policy or validator until one run passes | Hides unstable evidence and erases failure history | Preserve every attempt and resolve the underlying cause |
| Deleting a quarantine record after clearance | Breaks correction and audit lineage | Preserve history and link the successor resolution |
| Using prose-only reason codes as machine authority | Invents policy and incompatible vocabulary | Bind accepted contracts/policy or remain held |
| Treating `RELEASED` in the proposed record schema as KFM publication | Confuses control-plane shape with lifecycle/release state | Require the complete governed lifecycle and release path |
| Letting a worker select an exit or approve a review | Collapses preparation into authority | Worker may prepare candidates only after accepted binding |
| Copying protected material into a PR or issue for convenience | Creates uncontrolled exposure and retention | Use opaque references and approved restricted review systems |
| Weakening a schema or validator to clear one candidate | Converts a finding into silent drift | Repair the candidate or open a reviewed contract/schema change |

[Back to top](#top)

---

<a id="open-verification-register"></a>

## 14. Open verification register

| Item | Current state | Evidence required to close |
|---|---|---|
| Live quarantine writer | `UNKNOWN / HOLD` | Accepted job and writer contracts, idempotency, permissions, storage binding, receipts, tests, deployment, and observed run evidence |
| Review worker | `CONFIRMED PLACEHOLDER-ONLY` | Executable package, accepted queue/job binding, least privilege, safe logging, tests, deployment, and observed candidate-only behavior |
| Case identity and exit grammar | `CONFLICTED / PROPOSED` | Accepted decision aligning `QuarantineRecord`, older case terminology, lane README, runbook, policy, validators, and receipts |
| Canonical reason-code vocabulary | `NEEDS VERIFICATION` | Owned semantic contract, versioned schema enum or registry, policy binding, fixtures, and migration plan |
| Five-exit model | `PROPOSED` | ADR-0021 acceptance plus aligned implementation and negative tests |
| Restricted storage and access | `NEEDS VERIFICATION` | Approved system, access model, retention, audit, incident, and recovery evidence |
| Reviewer assignments | `NEEDS VERIFICATION` | Named accountable roles, competence, independence, and separation-of-duties proof |
| Recursive quarantine payload conformance | `UNKNOWN` | Authorized inventory and content-safe validation against accepted contracts |
| Public-path isolation | `PARTIAL / NEEDS VERIFICATION` | Non-vacuous route, API, search, map, export, graph, AI, cache, and deployment tests |
| Retention and vacuuming | `PROPOSED / per-source` | Accepted RetentionPolicy bindings and lineage-safe vacuuming receipts |

[Back to top](#top)

---

<a id="related-repository-surfaces"></a>

## 15. Related repository surfaces

### Governing doctrine and decisions

- [Directory Rules](../doctrine/directory-rules.md) — accepted placement authority
  through [ADR-0029](../adr/ADR-0029-adopt-directory-governance-standard-v2.md).
- [Lifecycle Law](../doctrine/lifecycle-law.md) — stage meanings, receipts,
  exposure, and reprocessing requirement.
- [Trust Membrane](../doctrine/trust-membrane.md) — refusal, quarantine,
  revocation, and public-path isolation.
- [Retention](../doctrine/retention.md) — retention classes and proposed
  lineage-safe vacuuming.
- [ADR-0021](../adr/ADR-0021-quarantine-has-structured-exit-paths.md) — proposed
  five-exit model; not accepted or fully implemented.

### Current bounded implementation evidence

- [Quarantine lane contract](../../data/quarantine/README.md).
- [Governed Run Chain semantic contract](../../contracts/governance/governed_run_chain.md).
- [`QuarantineRecord` schema](../../schemas/contracts/v1/governance/quarantine_record.schema.json).
- [`GovernedRunChain` schema](../../schemas/contracts/v1/governance/governed_run_chain.schema.json).
- [No-network validator](../../tools/validators/governance/validate_governed_run_chain.py).
- [Synthetic fixtures](../../fixtures/contracts/v1/governance/governed_run_chain/).
- [Focused tests](../../tests/validators/governance/governed_run_chain/test_validate_governed_run_chain.py).
- [Placeholder review-worker boundary](../../apps/workers/src/quarantine_review_worker/README.md).
- [Review Console architecture](../architecture/ui/REVIEW_CONSOLE.md).

### Companion procedures

- [First Ingest](./FIRST_INGEST.md) — fixture-first intake readiness and the held
  RAW-or-QUARANTINE writer boundary.
- [Evidence Correction](./EVIDENCE_CORRECTION.md) — released or release-facing
  evidence defects.
- [Rollback Runbook](./ROLLBACK_RUNBOOK.md) — separately authorized reversal.
- [Incident Response](./INCIDENT_RESPONSE.md) — exposure, integrity, or
  containment incidents.

---

## 16. Revision history

| Version | Date | Change |
|---|---|---|
| `v2.0` | 2026-09-01 | Replaced proposal-era path and schema claims with current `QuarantineRecord`/`GovernedRunChain` evidence; separated validation from policy, review, lifecycle, correction, release, and publication authority; recorded the placeholder-only worker and proposed ADR-0021 boundary; added current no-network rehearsal and public-safe handoff procedures. |
| `v1` | Earlier repository edition | Doctrine-oriented draft with proposed reason codes, speculative schema-home claims, and unverified operational paths. |

**Last reviewed:** 2026-09-01 against
`main@6a4b988784c31583af5d1cded3b2654360c1c123`.

[Back to top](#top)
