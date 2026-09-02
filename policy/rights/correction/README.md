<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/policy-rights-correction-readme
title: policy/rights/correction/ — Rights-Correction Policy Boundary
type: readme
version: v0.1.0
status: draft; BOUNDARY_COMPACT; repository-grounded; placeholder-only; inactive; fail-closed; non-legal; non-release; non-publication
owner: NEEDS VERIFICATION — CODEOWNERS routes policy/ to @bartytime4life; no accepted rights-correction steward or independent approver was established
created: 2026-08-13
updated: 2026-08-13
current_path: policy/rights/correction/README.md
owning_root: policy/
policy_label: internal; policy; rights; correction; revocation; fail-closed; non-legal; non-release; non-publication
responsibility: Define the policy-source boundary for admissibility after a rights-state correction, expiration, revocation, narrowing, or dispute without owning rights evidence, legal determinations, correction records, release actions, runtime propagation, or publication.
base_commit: 09a01ef8a71a557efc1c35bda6f9b762a429a1f3
prior_blob: 8b137891791fe96927ad78e64b0aad7bded08bdc
truth_posture: CONFIRMED README plus gitkeep only, parent rights boundary documents correction as placeholder, and release/data correction families exist separately / PROPOSED fail-closed rights-correction policy contract / HOLD executable rules until rights decision semantics, lineage inputs, evaluator, consumer, propagation, and rollback are accepted / UNKNOWN operational rights-revocation discovery and completion proof
related:
  - ../README.md
  - ../../README.md
  - ../../../release/README.md
  - ../../../release/corrections/README.md
  - ../../../release/correction_notices/README.md
  - ../../../release/withdrawal_notices/README.md
  - ../../../release/rollback_cards/README.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../apps/workers/src/correction_worker/README.md
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# policy :: rights :: correction

> **One-line purpose.** `policy/rights/correction/` is the policy-source boundary
> for deciding what operations must be held, denied, restricted, or re-evaluated
> after governed rights state changes; it does not decide the legal facts, write
> correction records, execute withdrawal, or approve release.

> [!IMPORTANT]
> **Safe current conclusion at `main@09a01ef8a71a`:** this directory contains
> only `.gitkeep` and this README. It has no correction rule, package, input or
> output contract, fixture, native test, evaluator, consumer, emitted decision,
> or propagation proof. The parent rights README correctly classifies the lane
> as placeholder-only; this document adds a boundary, not capability.

> [!CAUTION]
> A rights correction is not a Git edit and cannot be completed by rewriting a
> descriptor, policy file, registry record, receipt, or release history. Prior
> evidence and decisions remain attributable; successors, corrections,
> withdrawals, and rollback actions are append-only or versioned in their owning
> systems.

**Quick navigation:** [Purpose](#purpose) · [Authority](#inherited-authority-owner-and-scope) · [Status](#current-status) · [Children](#current-direct-child-map) · [Belongs](#what-belongs-here) · [Prohibited](#what-is-prohibited) · [Lifecycle](#lifecycle-behavior) · [Validation](#validation) · [Contributing](#contributor-guidance) · [Correction](#correction-and-rollback-posture) · [Open work](#open-verification-register)

## Purpose

The prospective rule family is **rights-correction admissibility**. Given an
explicit operation and a governed indication that rights or terms were corrected,
expired, revoked, narrowed, disputed, or superseded, it may determine whether
the operation must stop, hold, deny, restrict, re-review, or carry correction
obligations.

It consumes rights facts and lineage. It does not establish the rights holder,
interpret law, negotiate terms, decide whether an external notice is genuine,
or identify affected dependents through hidden searches.

## Inherited authority, owner, and scope

| Field | Current boundary |
|---|---|
| Parent | [`policy/rights/`](../README.md), the documented rights-admissibility policy boundary. |
| Root authority | [`policy/`](../../README.md), the adopted canonical root for normative policy source. |
| README profile | `BOUNDARY_COMPACT`: rights correction changes admissibility, lifecycle reliance, exposure, and release trust. |
| Placement basis | Accepted [ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) and [Directory Rules v2](../../../docs/doctrine/directory-rules.md), especially policy/source separation, README inheritance, naming classification, and correction/rollback discipline. |
| Local owner and scope ID | **NEEDS VERIFICATION.** No accepted rights-correction steward, escalation route, or registered policy scope was established. |
| Current maturity | M0 placeholder; the boundary is documented, but no executable candidate is established. |
| Release authority | None. [`release/`](../../../release/README.md) owns release-facing correction, withdrawal, and rollback decisions. |
| Publication authority | None. A policy result can require action but cannot mutate public state by itself. |

The singular `correction/` name describes a local policy concern, not a
collection of emitted `CorrectionNotice` objects. It does not override Directory
Rules naming guidance for public correction objects or resolve existing release
lane drift.

## Current status

| Surface | Confirmed state | Safe interpretation |
|---|---|---|
| README lineage | PR #2682 added a one-newline file; this revision supplies the local contract | Documentation only. |
| Tracked payload | `.gitkeep` only | No policy behavior exists. |
| Parent rights rules | Two separate default-only Rego stubs at the parent level | They do not implement rights correction or revocation. |
| Rights-currentness assessment | Adjacent fixture-only assessment machinery | Can validate declared currentness cases; cannot discover or enforce correction. |
| Release correction families | `release/corrections/`, `release/correction_notices/`, `release/withdrawal_notices/`, and `release/rollback_cards/` | Separate record and decision families; their presence does not make this policy executable. |
| Correction worker | Documented worker boundary exists | Implementation and orchestration are not policy source or proof of end-to-end propagation. |
| Native tests and runtime consumer | None established for this lane | Operational effect remains **UNKNOWN / fail closed**. |

## Current direct-child map

Verified from the tracked tree at the pinned base:

```text
policy/rights/correction/
├── .gitkeep
└── README.md
```

The placeholder is not a correction queue, registry, evidence store, or release
record collection.

## What belongs here

Subject to an accepted implementation contract, this boundary may contain:

- declarative, versioned rules for operation-specific response to a governed
  rights correction, expiration, revocation, narrowing, dispute, or supersession;
- fail-closed rules that distinguish unknown, stale, conflicting, invalid,
  revoked, and corrected states;
- stable public-safe reason codes and enforceable obligations such as hold,
  re-review, withhold export, attach corrected attribution, or require withdrawal
  review;
- exact package, entrypoint, policy version, effective time, expiry, and
  supersession documentation; and
- references to accepted rights lineage, dependent-object discovery, decisions,
  receipts, release corrections, withdrawals, cache invalidation, and rollback.

## What is prohibited

| Do not place or claim here | Owning surface or response |
|---|---|
| Legal advice, ownership findings, negotiated terms, or authoritative license text | Authorized legal, rights-holder, steward, or source-of-record systems outside this policy lane. |
| Source/right registry instances, evidence, agreements, correspondence, or review records | Their governed registry, evidence, agreement, and review systems. |
| `CorrectionNotice`, withdrawal, supersession, or rollback decision instances | [`release/corrections/`](../../../release/corrections/README.md), [`release/correction_notices/`](../../../release/correction_notices/README.md), [`release/withdrawal_notices/`](../../../release/withdrawal_notices/README.md), and [`release/rollback_cards/`](../../../release/rollback_cards/README.md) as governed. |
| A queue of affected datasets, releases, caches, citations, or users | Accepted operational stores with access, audit, retention, and completion controls. |
| Evaluator, worker, API, crawler, notifier, cache invalidator, or storage code | `packages/`, `apps/`, `runtime/`, tools, or infrastructure by responsibility. |
| Receipts, proofs, validation reports, or lifecycle data | Their accountability, proof, report, and `data/` families. |
| Secrets, private agreements, personal data, exact sensitive locations, or protected facts in reasons/logs | Keep out of Git and public outputs; use safe references and restricted review. |
| Deletion or history rewrite presented as correction completion | Preserve lineage; issue successors and prove propagation. |

## Inputs and outputs

No accepted contract is bound to this placeholder. A future evaluation should
receive explicit, versioned references for:

- the bounded operation, actor/service, audience, purpose, and evaluation time;
- the affected source, object, derivative, release, and dependency lineage;
- prior and current rights/terms identities, states, effective times, and
  authenticated review references;
- consent, stewardship, sovereignty, sensitivity, evidence, lifecycle, and
  public-exposure posture;
- prior decisions and releases that may require re-evaluation;
- policy bundle, module, entrypoint, evaluator, input digest, and correction
  event identity; and
- candidate obligations, correction/withdrawal refs, rollback target, and
  completion-proof refs.

Missing lineage, authenticity, scope, or currentness must yield hold, deny,
abstain, or error according to an accepted outcome contract—never allow.

This directory outputs only policy source and documentation. Emitted decisions,
correction records, receipts, proofs, release actions, and notifications belong
elsewhere.

## Exposure, mutation, and retention

| Dimension | Boundary |
|---|---|
| Exposure | Repository-public source, internal operating posture. Reasons and examples must not reveal restricted terms or affected protected subjects. |
| Mutation | Versioned and review-bound. Material rules preserve prior versions, effective times, and supersession lineage. |
| Retention | Durable policy history; correction evidence, decision instances, notices, and propagation logs retain in their owning systems. |
| Runtime writes | None. Evaluators and workers must not mutate policy source. |
| Generation | No generator or derived relationship is established. |

## Lifecycle behavior

| Stage | Required correction posture | What this lane cannot do |
|---|---|---|
| Notice intake | Authenticate and normalize the correction through an accepted source; preserve the original notice and prior state. | Cannot declare a notice valid by file presence. |
| Scope assessment | Resolve stable lineage from source and rights state to derivatives, catalogs, releases, caches, citations, exports, and AI outputs. | Cannot guess dependency closure. |
| RAW / WORK / QUARANTINE | Hold new affected use and preserve bytes/evidence under existing restrictions. | Cannot delete or silently rewrite lifecycle data. |
| PROCESSED / CATALOG / release candidate | Re-evaluate admissibility and obligations against current rights, sensitivity, consent, evidence, and review. | Cannot promote or approve a replacement. |
| PUBLISHED | Require governed correction, supersession, restriction, withdrawal, or rollback as materiality warrants. | Cannot mutate public carriers directly. |
| Closure | Require accountable decisions, receipts/proofs, cache and carrier verification, unresolved-dependent disclosure, and rollback posture. | Cannot self-certify completion. |

The default operational response to a credible unresolved rights change is to
hold affected operations until an authorized process establishes scope and
disposition.

## Validation

| Check | Current coverage | Limit |
|---|---|---|
| Parent rights documentation | Defines correction, revocation, supersession, and fail-closed expectations | Human boundary; no executable correction rule. |
| Source-rights currentness assessment | Synthetic dated-currentness validation | No live notice authentication, dependency discovery, or enforcement. |
| Release correction/rollback validators | Bounded record or drill families where implemented | Do not evaluate this placeholder or prove all affected rights dependencies. |
| Repository topology validator | Detects new policy-boundary drift and README absence | Placement QA only. |
| Metadata and local-link validators | Check structural metadata and repository-local links | Documentation QA only. |

There is no current native policy test for this lane. `make policy` is a TODO
echo and must not be reported as OPA validation.

## Contributor guidance

1. Pin the exact rights-state source and effective time; do not quote private or
   restricted terms into the repository.
2. Separate the policy rule from the correction event, affected-object index,
   worker implementation, decision, notice, receipt, proof, and release action.
3. Add executable policy only with accepted semantics and shapes, native
   positive/negative/unknown/stale/revoked/error tests, synthetic public-safe
   fixtures, stable reasons and obligations, evaluator/bundle identity, and a
   governed consumer.
4. Prove lineage traversal, idempotency, retry behavior, stale-event handling,
   cache invalidation, partial-failure visibility, and rollback with no hidden
   network dependency in tests.
5. Require rights, source/domain, privacy/security, policy, operations, and
   release review as applicable; a generator or author is not sole approver.

## Correction and rollback posture

For a README defect, revert or forward-fix this file. The prior blank blob is
`8b137891791fe96927ad78e64b0aad7bded08bdc`. Reverting documentation does not
reverse a rights change or repair an external release.

For a future policy defect, preserve the prior rule, bundle, evaluator, fixtures,
tests, inputs, decisions, and effective-time identity; issue a versioned successor;
re-evaluate affected operations; and route public correction, withdrawal, or
rollback through release authority. If rollback would recreate ambiguity or
re-expose material, use a documented forward fix.

For an actual rights revocation, stopping new affected use is distinct from
repairing prior releases. Completion requires dependency-aware evidence across
every governed carrier; a Git revert alone is insufficient.

## Open verification register

| ID | Open item | Posture |
|---|---|---|
| `RGT-COR-001` | Accepted rights-correction event and decision semantics, schemas, and authority source | **NOT ESTABLISHED** |
| `RGT-COR-002` | Local steward, escalation path, independent approver, and scope ID | **NEEDS VERIFICATION** |
| `RGT-COR-003` | Native rule package, finite outcomes, reasons, obligations, evaluator, bundle, and consumer | **NOT ESTABLISHED** |
| `RGT-COR-004` | Complete source-to-derivative-to-release dependency discovery | **UNKNOWN / FAIL CLOSED** |
| `RGT-COR-005` | Idempotent correction, withdrawal, cache invalidation, notification, and completion proof | **UNKNOWN** |
| `RGT-COR-006` | Canonical relationships among release correction, correction-notice, withdrawal, and rollback lanes | **CONFLICTED / NEEDS GOVERNANCE REVIEW** |
| `RGT-COR-007` | Required checks and qualified independent review | **UNKNOWN** |

<p align="right"><a href="#top">Back to top</a></p>
