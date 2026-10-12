<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook/promotion
title: KFM Promotion Runbook
type: runbook
version: v2.0
status: draft; repository-grounded; BOUNDED_READINESS_GUIDANCE; OPERATIONAL_PROMOTION_HELD; NON_RELEASE; NON_DEPLOYMENT; NON_PUBLICATION
created: 2026-05-12
updated: 2026-08-31
current_path: docs/runbooks/PROMOTION_RUNBOOK.md
owning_root: docs/
placement_basis: ADR-0029 and docs/doctrine/directory-rules.md; same-path runbook update
truth_posture: cite-or-abstain
authority_class: explanatory operational documentation
authority_rank: subordinate to accepted doctrine and ADRs, contracts, schemas, evidence, policy, authenticated review, release records, signatures, receipts, proofs, and current runtime evidence
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 246573b531ecfa4b221c08f25a28e6ae762cfd9f
  target_before_update_blob: ea01ae337019c9d4f595f5cbb592a01d9ac05f3e
  open_pull_requests_touching_target: 0
inspection_boundary: >-
  Current-session GitHub reads covered the target, accepted Directory Rules,
  lifecycle and trust doctrine, release root, proposed ADR-0018,
  PromotionDecision and PromotionReceipt contracts, bounded promotion-gate
  validator and workflow, promotion policy boundary, correction and rollback
  runbooks, and generated-receipt requirements. Google Drive was consulted as
  read-only planning lineage. No live resolver, authenticated reviewer registry,
  active promotion-policy evaluator, signer trust root, transition executor,
  deployment, public release, or rollback execution was exercised.
notes:
  - "The current A-G profile is executable and fixture-first; ADR-0018 and its final-readiness vocabulary remain proposed."
  - "PASS means APPROVE_READY for review only, not APPROVE, transition, release, deployment, publication, or public-use permission."
  - "No promotion, release, deployment, publication, source activation, policy activation, review approval, signature, or repository-setting change is performed by this document."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KFM Promotion Runbook

Use this runbook to assess whether a `CATALOG` or `TRIPLET` candidate is ready
for separately governed review on a possible transition toward `PUBLISHED`.
The procedure exercises the repository's bounded, no-network readiness checks
and prepares an accountable handoff. It stops before any lifecycle transition,
release, deployment, publication, alias change, cache invalidation, or public
write.

> [!IMPORTANT]
> **This runbook is not promotion authority.** It cannot authenticate evidence
> or reviewers, evaluate the inactive promotion-policy stubs, issue a
> `PromotionDecision`, apply a transition, sign a release, publish an artifact,
> or authorize public use.

> [!CAUTION]
> Promotion is a governed state transition, not a file move, passing workflow,
> pull-request merge, deployment, or layer toggle.

**Navigation:** [authority](#purpose-and-authority) ·
[current capability](#current-repository-capability) ·
[preflight](#preflight) · [procedure](#procedure) ·
[A-G profile](#current-bounded-a-g-profile) ·
[outcomes](#finite-outcomes) · [handoff](#review-handoff) ·
[rollback](#correction-and-rollback) · [validation](#document-validation)

## Purpose and authority

This runbook helps an operator:

1. freeze the exact candidate and authority context;
2. run the current fixture and candidate-packet checks;
3. preserve `PASS`, `ABSTAIN`, `DENY`, or `ERROR` without reinterpretation;
4. inspect evidence, rights, sensitivity, review, and reversal obligations; and
5. prepare a public-safe review handoff that explicitly records no public
   effect.

It does **not** grant authority to review, approve, promote, release, deploy, or
publish. In a conflict, use this order:

1. platform, security, and repository-enforced controls;
2. accepted KFM doctrine and ADRs;
3. current contracts, schemas, policy, validators, tests, and release records;
4. this runbook;
5. planning documents and historical examples.

[ADR-0029](../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
confirms `docs/runbooks/` as the correct responsibility root. The lifecycle
remains:

```text
RAW -> WORK or QUARANTINE -> PROCESSED -> CATALOG or TRIPLET -> PUBLISHED
```

Public clients use governed interfaces and released public-safe artifacts.
Maps, tiles, graphs, indexes, summaries, tests, documentation, and AI output
remain downstream carriers rather than truth or release authority.

## Current repository capability

The repository currently supports a bounded readiness assessment, not an
operational promotion system.

| Surface | Current evidence | Boundary |
|---|---|---|
| `make publish-check` | Exercises the promotion fixture matrix and focused tests | Does not apply a transition |
| `tools/validators/validate_promotion_gate.py` | Deterministic, no-network, read-only packet validator | Checks declared shape and agreement; does not resolve or authenticate references |
| `.github/workflows/promotion-gate.yml` | Runs bounded validator/test coverage | A green workflow is not approval or publication |
| `PromotionDecision` contract/schema/validator | Proposed finite `APPROVE`, `DENY`, `ABSTAIN` shape | Shape validity is not an accountable decision |
| `PromotionReceipt` contract/schema/validator | Proposed fixture-first A-G receipt shape | A receipt records an assessment; it does not prove transition |
| `policy/promotion/` | Proposed, inactive Rego stubs | No active promotion-policy evaluation is established |
| `release/` | Canonical decision-plane homes and bounded fixtures | Operational promotion, signer custody, release, publication, and rollback execution remain unproved |
| ADR-0018 | Proposed final-readiness vocabulary and conflict analysis | Not accepted architecture |

Do not promote a proposal to current behavior merely because a path, fixture,
contract, workflow, or document exists.

## State and object separation

Keep these states and objects distinct:

| Item | Meaning |
|---|---|
| Candidate lifecycle state | Where the subject is now: usually `CATALOG` or `TRIPLET` |
| Readiness result | Validator result: `PASS`, `ABSTAIN`, `DENY`, or `ERROR` |
| Review work state | Human coordination state such as `HOLD` or `REVIEW_REQUIRED` |
| `PromotionDecision` | Separately accountable `APPROVE`, `DENY`, or `ABSTAIN` record |
| Transition application | Auditable change of governed lifecycle/release state |
| Release | Bound artifact/manifest/signature state |
| Deployment | Operational placement of released bytes or services |
| Publication | Governed public exposure |
| `PromotionReceipt` | Record of an assessment; not proof that any later state occurred |
| Proof or attestation | Support for a bounded claim; not the decision itself |

Never translate readiness `PASS` directly into decision `APPROVE`.

## When to use this runbook

Use it only when the candidate, revision, lifecycle boundary, validation
profile, and safe handling route are known.

Do not use it to:

- promote directly from `RAW`, `WORK`, `QUARANTINE`, or unvalidated
  `PROCESSED`;
- bypass evidence, rights, sensitivity, review, correction, or rollback;
- publish because CI is green;
- infer policy evaluation from a fixture field or inactive Rego stub;
- copy restricted payloads into public branches, issues, logs, or receipts;
- self-approve AI-authored, policy-significant, or release-significant work; or
- write directly to `data/published/`, a live alias, CDN, tile endpoint, search
  index, graph projection, or public API.

## Roles and separation of duties

Assignments must be verified for the exact candidate. A CODEOWNER or GitHub
review route proves routing only.

| Role | Responsibility | Must remain separate from |
|---|---|---|
| Candidate author or pipeline operator | Assemble and pin the candidate packet | Final review where separation is required |
| Evidence/source steward | Verify source role, evidence closure, rights, and limits | Generated-language authority |
| Policy/sensitivity steward | Evaluate the accepted policy profile and obligations | Candidate self-attestation |
| Independent reviewer | Check subject binding, scope, obligations, and rollback | Authorship when independent review is required |
| Release/signing operator | Apply a separately authorized transition and release process | This readiness runbook |
| Correction/rollback steward | Verify prior safe target and correction path | Silent history rewrite |

Unverified ownership, authority interval, qualification, or required
separation is a `HOLD`, not permission to continue.

## Preflight

### 1. Freeze the candidate

Record:

- repository and exact commit or immutable snapshot;
- candidate ID, run ID, producer, domain, and current state;
- requested target state;
- contract, schema, validator, and policy profile versions;
- `spec_hash`, artifact digests, and manifest identity;
- active pull requests, migrations, corrections, or release work touching the
  same subject;
- accepted ADRs and Directory Rules; and
- previous public-safe state and rollback target.

A result is stale after any bound input, schema, policy, evidence, review,
rights, sensitivity, artifact, manifest, or rollback reference changes.

### 2. Confirm safe handling

Use public-safe identifiers and references. Never place credentials, signing
material, exploit details, exact sensitive locations, protected cultural
information, living-person records, DNA/genomic material, private-land detail,
or infrastructure vulnerability information in a public packet.

Follow [`SECURITY.md`](../../SECURITY.md) and the
[Incident Response Runbook](./INCIDENT_RESPONSE.md) for active exposure.

### 3. Assemble the declared packet

The bounded validator expects explicit declarations for:

- identity and lifecycle boundary;
- candidate, manifest, run-receipt, and artifact digest binding;
- geometry, CRS, bounds, and deterministic processing;
- real UTC temporal interval and evaluation instant;
- policy profile, labels, result, and reference;
- evidence, proof, attestation, receipt, and catalog support;
- review actor, authority, scope, time, obligations, and separation;
- rollback target and correction lineage; and
- an AI receipt when model mediation materially affected the candidate.

The validator checks declarations and internal agreement. It does not
dereference URIs, authenticate actors, execute Rego, verify signatures, prove
rights, resolve an `EvidenceBundle`, or inspect public surfaces.

## Procedure

### 1. Reproduce the bounded fixture proof

From a checkout at the exact candidate revision:

```bash
make publish-check
```

Record the command, commit, exit status, and complete output. This exercises
repository fixtures and focused tests; it does not evaluate an arbitrary
candidate packet. Do not call the check passing when it was not run, was
inherited from another commit, or did not reach the named assertions.

### 2. Evaluate the explicit packet

```bash
python tools/validators/validate_promotion_gate.py path/to/candidate-packet.json
```

The path is illustrative. Use the actual pinned public-safe packet or an
approved secure working path. The command emits one deterministic JSON line per
input and writes no decision, receipt, proof, manifest, release record, or
public artifact.

### 3. Preserve the exact result

```text
ERROR > DENY > ABSTAIN > PASS
```

- `PASS` means `APPROVE_READY` for separate accountable review.
- `ABSTAIN` means support is unresolved or insufficient.
- `DENY` means a mandatory, unsafe, or contradictory condition blocks
  readiness.
- `ERROR` means the packet or supplied evaluation context could not be
  processed safely.

Every non-`PASS` result is `BLOCKED`; preserve the prior state.

### 4. Run release-family shape checks when relevant

```bash
python tools/validators/release/validate_promotion_decision.py --fixtures
python tools/validators/release/validate_promotion_receipt.py --fixtures
```

These commands validate proposed shapes and bounded consistency. They do not
create an accountable decision or prove a transition.

### 5. Resolve material support

Before a later accountable decision, verify that references exist, are
authentic and current, bind the same subject and artifact set, and are
admissible for the intended audience. At minimum check:

- source identity, role, rights, terms, and sensitivity;
- `EvidenceRef` to `EvidenceBundle` resolution;
- validator and policy profile identity;
- artifact and manifest digest equality;
- spatial and temporal scope;
- review authority, separation, validity interval, and obligations;
- correction, withdrawal, and rollback support; and
- public-safe transformation and representation receipts when material.

A syntactically valid reference is not closure.

### 6. Prepare the handoff and stop

Record:

- candidate ID, exact revision, `spec_hash`, and artifact digests;
- declared `CATALOG` or `TRIPLET` to `PUBLISHED` boundary;
- exact commands and profile;
- complete finite results and public-safe diagnostics;
- evidence, policy, review, attestation, manifest, correction, and rollback
  references;
- unresolved obligations, conflicts, stale support, and unavailable checks;
- overlap and dependency order;
- previous public state and proposed rollback target; and
- an explicit statement that no transition, release, deployment, publication,
  alias mutation, cache invalidation, or public write occurred.

Stop here. A later transition needs separate authority, accepted active policy,
authenticated subject-bound review, accountable decision, evidence and
integrity closure, authoritative manifest/signature handling, and executable
correction/rollback support.

## Current bounded A-G profile

The executable validator uses these names. Proposed
[ADR-0018](../adr/ADR-0018-promotion-gate-sequence.md) selects the same names
for a narrow final-readiness profile, but it remains proposed and records
conflicts with broader lifecycle-wide A-G vocabularies.

| Gate | Name | Declared check | Fail-closed posture |
|:---:|---|---|---|
| A | `identity_and_closure` | Candidate/profile identity, author, `spec_hash`, lifecycle boundary, manifest identity | `DENY` on missing or contradictory identity |
| B | `asset_integrity` | Candidate, manifest, receipt, and non-empty unique digest-set agreement | `DENY` on mismatch or malformed digest |
| C | `geometry_and_crs` | Declared validity, determinism, `EPSG:4326`, ordered finite bounds | `DENY` on invalid or nondeterministic geometry |
| D | `temporal_semantics` | Real UTC-second instants, ordered interval, evaluation time | `DENY` on malformed or inverted time |
| E | `rights_and_sensitivity` | Known policy context, labels, public-safe discipline, supplied finite evaluation | `DENY` on rejection; `ERROR` on evaluator failure |
| F | `proof_and_catalog_support` | Evidence, attestation, run receipt, STAC/DCAT/PROV support, conditional AI receipt | `ABSTAIN` for unresolved evidence; `DENY` for mandatory integrity/catalog gaps |
| G | `review_and_rollback` | Review identity/authority/time/scope/binding plus rollback/correction linkage | `ABSTAIN` or `DENY` on missing, stale, unsafe, self-reviewed, or contradictory context |

A validator may evaluate all seven gates for complete diagnostics. Any
non-`PASS` result still blocks readiness.

## Finite outcomes

| Result | Meaning | Operator action |
|---|---|---|
| `PASS` | Declared packet satisfied the bounded profile | Record `APPROVE_READY`; hand off |
| `ABSTAIN` | Required support is unresolved or insufficient | Preserve state; obtain support or narrow scope |
| `DENY` | Mandatory, unsafe, or contradictory condition exists | Preserve state; correct the source condition |
| `ERROR` | Input or supplied context could not be evaluated safely | Diagnose and rerun from the same pinned state |

The proposed `PromotionDecision` vocabulary is separate:

| Decision | Meaning | Boundary |
|---|---|---|
| `APPROVE` | Accountable decision permits later release processing | Not publication by itself |
| `DENY` | Transition is forbidden | Preserve prior state |
| `ABSTAIN` | Decision maker lacks sufficient trustworthy context | Preserve state and route for resolution |

## Rights, sensitivity, and harmful precision

Unknown or disputed rights, consent, sovereignty, privacy, sensitivity, or
precision fail closed. This is especially important for archaeology, rare
species, protected cultural information, infrastructure, private land,
living-person records, and DNA/genomic material.

Before any later public transition, verify that source terms permit the
intended audience; source roles remain distinct; sensitive geometry was
transformed before delivery rather than hidden by style; any redaction,
generalization, withholding, delay, or staged access has a reason and transform
receipt; required subject/community review occurred; and every affected
derivative can be corrected, withdrawn, invalidated, or rolled back.

Use `ABSTAIN`, `DENY`, or human `HOLD` when required facts are unknown. Never
convert uncertainty into public precision.

## Review handoff

A reviewer must be able to answer:

1. What exact candidate and lifecycle boundary were assessed?
2. Which evidence and policy context support it?
3. Which commands ran against which commit, and what did they prove?
4. Which reviewer identities and assignments are authenticated?
5. Which obligations or conflicts remain?
6. What prior public state is preserved?
7. Which correction and rollback paths apply?
8. Did any public or operational state change? Under this runbook, **no**.

Use the [Review Duties guide](../governance/REVIEW_DUTIES.md). A fixture actor,
CODEOWNER, workflow, pull request, or generated receipt does not prove approval.

## Correction and rollback

Readiness is incomplete without a correction path and rollback target, but this
runbook executes neither.

- Use the [Evidence Correction Runbook](./EVIDENCE_CORRECTION.md) for
  public-safe defect intake, classification, candidate preparation, bounded
  validation, and review handoff.
- Use the [Rollback Runbook](./ROLLBACK_RUNBOOK.md) as companion guidance while
  preserving its documented execution holds.
- Treat [Release Dry-Run](./RELEASE_DRY_RUN.md) as a draft rehearsal guide; its
  conceptual release command is not established as a transition executor.

Correction, withdrawal, and rollback preserve prior records and emit a new
governed decision or notice rather than silently rewriting history. Any
authorized invalidation plan must include downstream caches, tiles, search
indexes, graph projections, stories, exports, and AI-derived surfaces.

## Troubleshooting

| Observation | Safe interpretation | Next action |
|---|---|---|
| `make publish-check` was not run or did not reach named tests | No current fixture proof | Fix or report the exact unavailable check |
| Packet returns `ABSTAIN` | Support is insufficient | Resolve support or narrow scope |
| Packet returns `DENY` | Mandatory or unsafe condition blocks readiness | Preserve state and correct the condition |
| Packet returns `ERROR` | Tool, input, or supplied context failed safely | Diagnose and rerun at the pinned scope |
| `PASS` conflicts with evidence, rights, or review | Validator is not final authority | Record the conflict and hold |
| Referenced object cannot be resolved/authenticated | Presence is not closure | Keep blocked |
| Result is inferred from inactive Rego stubs | No active promotion policy ran | Keep blocked |
| Reviewer equals author where separation is required | Review is not closed | Assign an independent reviewer |
| Step proposes public-store or live-alias write | Authority ceiling crossed | Stop and route to a separate operation |
| Sensitive detail appears in public coordination | Handling is unsafe | Contain privately; retain only safe identifiers |

## Completion checklist

- [ ] Candidate and exact revision are pinned.
- [ ] Boundary is `CATALOG` or `TRIPLET` toward `PUBLISHED`.
- [ ] Public-safe handling and overlap are checked.
- [ ] Fixture checks and explicit packet validation ran or are reported
      unavailable.
- [ ] Finite results and diagnostics are preserved.
- [ ] Material support is resolved or explicitly blocked.
- [ ] Rights, sensitivity, review, correction, and rollback remain visible.
- [ ] Handoff records prior state and no-public-write boundary.
- [ ] No transition, release, deployment, publication, alias mutation, cache
      invalidation, or public serving occurred or was implied.

## Document validation

For changes to this Markdown:

```bash
git diff --check
```

Also verify one H1; balanced code fences and metadata delimiters; logical
heading order; working relative links and anchors; current commands, paths,
contracts, schemas, policy, workflow, and status claims; no invented owner or
maturity; no unrelated churn; final newline; and the required generated
provenance receipt for AI-authored work.

Run repository Markdown/link checks when available. Report unavailable,
inherited, or pending checks separately.

## Open verification

The documentation change does not:

1. accept ADR-0018 or settle every A-G compatibility vocabulary;
2. activate a fail-closed promotion-policy bundle and evaluator;
3. establish authenticated stewards, reviewer qualification, or separation;
4. implement a canonical candidate/evidence resolver;
5. establish signature, transparency, or trust-root verification;
6. implement a transition operator;
7. prove release-manifest assembly or governed public read-back; or
8. exercise correction, withdrawal, cache invalidation, and rollback end to
   end.

## Maintenance and rollback

Update this runbook whenever current repository behavior changes. Preserve
`kfm://doc/runbook/promotion` and repair known inbound links when headings or
scope change.

Before merge, abandon the draft by closing it and deleting only its task branch.
After merge, revert the focused documentation commit through review. Reverting
this document must not change candidate, release, deployment, publication,
policy, review, or public state.

## Related references

- [Runbooks index](./README.md)
- [Lifecycle Law](../doctrine/lifecycle-law.md)
- [Trust Membrane](../doctrine/trust-membrane.md)
- [Directory Rules](../doctrine/directory-rules.md)
- [Publication promotion-gate architecture](../architecture/publication/promotion-gates.md)
- [Proposed ADR-0018](../adr/ADR-0018-promotion-gate-sequence.md)
- [Release governance root](../../release/README.md)
- [`PromotionDecision` contract](../../contracts/release/promotion_decision.md)
- [`PromotionReceipt` contract](../../contracts/release/promotion_receipt.md)
- [Promotion policy boundary](../../policy/promotion/README.md)
- [Bounded promotion-gate validator](../../tools/validators/promotion_gate/README.md)
- [Promotion-gate workflow](../../.github/workflows/promotion-gate.yml)

[Back to top](#top)
