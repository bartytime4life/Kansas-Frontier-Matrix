<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/common/open-ended-temporal-semantics-disclosure
title: OpenEndedTemporalSemanticsDisclosureCandidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Common contract steward · Temporal steward · Evidence steward · Validation steward
created: 2026-08-11
updated: 2026-08-11
owning_root: contracts/
policy_label: internal; common; temporal; open-ended; as-of; disclosure; auditability
responsibility: Define fixture-only semantics for explicit, unknown-end, current-until-superseded, and now-relative periods without creating temporal truth, evidence, policy, review, release, or publication authority.
truth_posture: "CONFIRMED supplied-card traceability and repository placement; PROPOSED inactive contract; UNKNOWN consumer adoption; NEEDS VERIFICATION human review and hosted CI"
related:
  - ./temporal_window.md
  - ../../schemas/contracts/v1/common/open_ended_temporal_semantics_disclosure.schema.json
  - ../../fixtures/contracts/v1/common/open_ended_temporal_semantics_disclosure/cases.json
  - ../../tools/validators/validate_open_ended_temporal_semantics_disclosure.py
  - ../../tests/validators/test_validate_open_ended_temporal_semantics_disclosure.py
  - ../../docs/intake/exploratory/pass-18-open-ended-temporal-semantics-disclosure-source-map.md
[/KFM_META_BLOCK_V2] -->

# OpenEndedTemporalSemanticsDisclosureCandidate

`OpenEndedTemporalSemanticsDisclosureCandidate` is an additive, fixture-only profile for making the meaning of an absent period end explicit next to one pinned temporal claim.

It implements the smallest reviewable portion of supplied Pass 18 cards `KFM-P18-INV-093`, `KFM-P18-INV-194`, and `KFM-P18-INV-287`: “now,” “current,” and an unknown end are different meanings; each open-ended interpretation needs a pinned as-of instant; and a far-future timestamp must not masquerade as forever.

## Boundary

The profile is `PROPOSED_INACTIVE`, no-network, and non-authoritative. A validator `PASS` means only that:

- the candidate is closed under this schema and its canonical profile hash replays;
- timestamps use explicit UTC `Z` form and satisfy local order invariants;
- end presence agrees with the declared end semantics;
- an open-ended interpretation carries an explicit as-of time;
- current and now-relative meanings identify which clock role resolves “now”;
- no far-future sentinel is used;
- the interpretation and disclosure obligations agree with the declared semantics; and
- evidence and review references are canonically ordered.

It does **not** resolve the claim scope or evidence, prove a source’s time meaning, choose a domain clock, establish temporal truth, approve policy or review, promote lifecycle state, release, deploy, publish, or authorize public use. A public-explanation candidate must carry a review-record reference, but that reference is only a prerequisite field and grants no authority.

## End-semantics vocabulary

| Value | Required representation | Interpretation |
|---|---|---|
| `EXPLICIT_END` | A finite `end`; no clock role is needed. | `BOUNDED_PERIOD` |
| `UNKNOWN_END` | `end: null`, pinned `as_of_time`, and `now_basis: NOT_APPLICABLE`. | `END_NOT_KNOWN` |
| `CURRENT_UNTIL_SUPERSEDED` | `end: null`, pinned `as_of_time`, explicit clock role, and supersession caveat. | `CURRENT_KNOWN_STATE` |
| `NOW_RELATIVE` | `end: null`, pinned `as_of_time`, and explicit clock role used to resolve “now.” | `NOW_RESOLVED_AT_AS_OF` |

`OBSERVED_TIME`, `SOURCE_TIME`, `TRANSACTION_TIME`, and `RELEASE_TIME` are disclosure roles, not claims that those clocks are equivalent. The profile deliberately does not infer one role from another.

## Profile fields

| Field | Meaning |
|---|---|
| `profile_spec_hash` | Canonical JSON plus SHA-256 binding of the complete candidate except this field. |
| `temporal_claim_ref` / `temporal_claim_digest` | Pinned candidate identity; no reference resolution occurs. |
| `claim_scope` | Pinned scope reference and explicit local resolution state. |
| `intended_use` | Bounded use label for QA, exploration, public explanation, or release review; never an authorization. |
| `period` | Start, nullable end, end semantics, nullable as-of instant, now-basis role, and explicit sentinel declaration. |
| `disclosure` | Completeness, interpretation, obligations, bounded explanation, and review-record references. |
| `evidence_refs` | Canonically ordered evidence references retained for a later resolver. |
| `authority_claims` | Fixed-false declaration preventing temporal-truth, evidence, policy, review, promotion, release, publication, or public-use authority. |

## Far-future sentinels

The machine profile keeps `sentinel_used` and `sentinel_value` explicit so unsafe legacy input can be denied rather than silently normalized. A compliant candidate uses `sentinel_used: false` and `sentinel_value: null`. Values such as `9999-12-31` do not prove that a state remains current, that an end is unknown, or that an interval is infinite.

This profile does not rewrite an existing sentinel. Conversion, source correction, and compatibility migration require a separate reviewed increment with provenance and rollback evidence.

## Finite validation outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Shape, identity, UTC/order, end semantics, as-of basis, disclosure obligations, sentinel prohibition, and canonical references are coherent. |
| `ABSTAIN` | The claim scope is unresolved or disclosure completeness is `INCOMPLETE` or `UNKNOWN`. |
| `DENY` | A deterministic temporal-semantics, sentinel, obligation, review-reference, or canonicalization invariant fails. |
| `ERROR` | The candidate cannot be evaluated safely under the closed machine schema. |

These outcomes are validator states only. They are not temporal truth, evidence findings, policy decisions, review decisions, release states, or runtime answers.

## Directory Rules basis

The accepted responsibility-root model places shared temporal meaning under `contracts/common/`, machine shape under `schemas/contracts/v1/common/`, synthetic cases under `fixtures/`, repository validation under `tools/`, executable checks under `tests/`, CI orchestration under `.github/`, human source reconciliation under `docs/`, and authoring accountability under `data/receipts/generated/`.

The profile is adjacent to `contracts/common/temporal_window.md` and the period-boundary disclosure profile because open-ended meaning is shared temporal value semantics. It composes established objects by reference and does not change their shapes or consumers. No parallel temporal, evidence, policy, review, release, or publication authority is created.

## Validation

```bash
python -m unittest tests.validators.test_validate_open_ended_temporal_semantics_disclosure -v
python tools/validators/validate_open_ended_temporal_semantics_disclosure.py --fixtures
```

## Rollback

Revert the additive profile packet. It has no consumer and mutates no claim, source, evidence, policy, review, lifecycle, catalog, release, cache, route, deployment, or public artifact.
