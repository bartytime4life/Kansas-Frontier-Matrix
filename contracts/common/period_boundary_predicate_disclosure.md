<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/common/period-boundary-predicate-disclosure
title: PeriodBoundaryPredicateDisclosureCandidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Common contract steward · Temporal steward · Evidence steward · Validation steward
created: 2026-08-10
updated: 2026-08-10
owning_root: contracts/
policy_label: internal; common; temporal; interval-boundary; disclosure; auditability
responsibility: Define fixture-only interval-convention, endpoint-predicate, and intersection-shape disclosure semantics without creating temporal truth, evidence, policy, review, release, or publication authority.
truth_posture: "CONFIRMED supplied-card traceability and repository placement; PROPOSED inactive contract; UNKNOWN consumer adoption; NEEDS VERIFICATION human review and hosted CI"
related:
  - ./temporal_window.md
  - ../../schemas/contracts/v1/common/period_boundary_predicate_disclosure.schema.json
  - ../../fixtures/contracts/v1/common/period_boundary_predicate_disclosure/cases.json
  - ../../tools/validators/validate_period_boundary_predicate_disclosure.py
  - ../../tests/validators/test_validate_period_boundary_predicate_disclosure.py
  - ../../docs/intake/exploratory/pass-18-period-boundary-predicate-disclosure-source-map.md
[/KFM_META_BLOCK_V2] -->

# PeriodBoundaryPredicateDisclosureCandidate

`PeriodBoundaryPredicateDisclosureCandidate` is an additive, fixture-only profile for making interval-boundary conventions and the resulting temporal predicate visible next to one bounded claim comparison.

It implements the smallest reviewable portion of supplied Pass 18 card `KFM-P18-INV-462`: temporal claims should disclose whether their periods are closed, open, half-open, or explicitly mixed, and should distinguish relations such as meeting, overlapping, starting, during, and finishing.

## Boundary

The profile is `PROPOSED_INACTIVE`, no-network, and non-authoritative. A validator `PASS` means only that:

- the candidate is closed under this schema;
- its deterministic profile hash replays;
- its two synthetic intervals are proper UTC intervals;
- their inclusivity flags agree with the declared convention;
- the declared 13-value endpoint predicate matches deterministic endpoint ordering;
- the declared intersection shape accounts for endpoint inclusion; and
- evidence references are canonically ordered.

It does **not** resolve the claim, either `TemporalWindow`, or any evidence reference. It does not establish that the supplied intervals are true, choose a domain-wide boundary convention, interpret uncertain or open-ended time, decide claim fitness, approve review, promote lifecycle state, release, deploy, publish, or authorize public use.

## Profile fields

| Field | Meaning |
|---|---|
| `profile_spec_hash` | Canonical JSON plus SHA-256 binding of the complete candidate except this field. |
| `claim_ref` / `claim_digest` | Pinned identity of the candidate temporal claim; no reference resolution occurs. |
| `claim_scope` | Pinned scope reference and explicit local resolution state. |
| `interval_convention` | `CLOSED`, `OPEN`, either half-open convention, or `MIXED_EXPLICIT`. |
| `left_window` / `right_window` | Pinned `TemporalWindow` references plus explicit proper UTC intervals and inclusive-boundary flags. |
| `declared_predicate` | One of the 13 finite endpoint-order relations. |
| `declared_intersection_shape` | `EMPTY`, `POINT`, or `INTERVAL`, computed with boundary inclusion. |
| `explanation` | Bounded public-facing explanation candidate; not a release or publication act. |
| `evidence_refs` | Canonically ordered evidence references retained for a later resolver. |
| `authority_claims` | Fixed-false declaration preventing evidence, policy, review, promotion, release, publication, or public-use authority. |

The relation vocabulary is `BEFORE`, `MEETS`, `OVERLAPS`, `STARTS`, `DURING`, `FINISHES`, `EQUALS`, `FINISHED_BY`, `CONTAINS`, `STARTED_BY`, `OVERLAPPED_BY`, `MET_BY`, and `AFTER`. These names describe the bounded validator profile; they do not claim adoption of an external temporal standard.

## Meeting is not intersection

Endpoint ordering and set intersection are disclosed separately. Two periods whose endpoints meet have predicate `MEETS` (or `MET_BY`) regardless of inclusivity. Their intersection is:

- `POINT` only when both periods include the shared boundary; or
- `EMPTY` when either period excludes it.

This prevents a half-open adjacency from being silently presented as a shared instant and prevents a closed-boundary meeting from being silently presented as disjoint.

## Finite validation outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Shape, identity, interval convention, endpoint relation, intersection shape, and canonical references are coherent. |
| `ABSTAIN` | The claim scope or either referenced window remains unresolved. |
| `DENY` | A deterministic identity, UTC, interval order, convention, predicate, intersection, or canonicalization invariant fails. |
| `ERROR` | The candidate cannot be evaluated safely under the closed machine schema. |

These are validator outcomes only. They are not temporal truth states, evidence findings, policy decisions, review decisions, release states, or runtime answers.

## Directory Rules basis

The accepted responsibility-root model places semantic meaning under `contracts/`, machine shape under `schemas/`, synthetic cases under `fixtures/`, repository validation under `tools/`, executable checks under `tests/`, CI orchestration under `.github/`, human source reconciliation under `docs/`, and authoring accountability under `data/receipts/generated/`.

The object is adjacent to `contracts/common/temporal_window.md` because interval-boundary and predicate semantics are shared temporal value semantics. It composes the existing window authority by reference and does not change the current `TemporalWindow` shape or vocabulary. No parallel temporal, evidence, policy, release, or publication authority is created.

## Validation

```bash
python -m unittest tests.validators.test_validate_period_boundary_predicate_disclosure -v
python tools/validators/validate_period_boundary_predicate_disclosure.py --fixtures
```

## Rollback

Revert the additive profile packet. It has no consumer and mutates no claim, source, evidence, policy, review, lifecycle, catalog, release, cache, route, deployment, or public artifact.
