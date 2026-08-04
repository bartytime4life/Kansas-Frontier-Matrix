<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-architecture-briefing-integration
title: Briefing-to-System Integration Architecture
type: architecture; implementation-guide
version: v0.4.0
status: proposed; four bounded no-network foundations
owners: OWNER_TBD — Architecture steward · Governance steward · Domain stewards · Source/evidence/policy/release stewards
created: 2026-07-29
updated: 2026-08-04
policy_label: public; architecture; briefing-integration; no-public-authority
related:
  - ../../contracts/governance/briefing_signal.md
  - ../../schemas/contracts/v1/governance/briefing_signal.schema.json
  - ../../tools/validators/governance/validate_briefing_signal.py
  - ../../tools/validators/governance/deduplicate_briefing_signals.py
  - ../../tools/validators/governance/route_briefing_signals.py
  - ../../contracts/common/temporal_authority_envelope.md
  - ../../schemas/contracts/v1/common/temporal_authority_envelope.schema.json
  - ../../examples/briefing_integration/README.md
  - ../../.github/workflows/briefing-integration.yml
tags: [kfm, architecture, briefing, identity, deduplication, materiality, routing, temporal-authority, water-planning, evidence-first]
notes:
  - "v0.4 adds deterministic explainable materiality and finite routing without GitHub mutation."
  - "The initial threshold profile is proposed and versioned; it is not policy or release authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Briefing-to-System Integration Architecture

> Convert recurring briefing stories into governed verification and modeling work without using briefing prose, priority scores, or dry-run routing as evidence or as authority for repository mutation, source activation, policy, proof, release, deployment, publication, or public use.

## Operating flow

```text
Daily briefing
  -> BriefingSignal
  -> deterministic identity and event clustering
  -> explainable materiality and finite routing dry run
  -> official-source snapshot or explicit unresolved state
  -> object-family classification
  -> human-reviewed existing-issue update or bounded new issue
  -> domain object + TemporalAuthorityEnvelope, when separately modeled
  -> contract/schema/fixture/validator work
  -> source admission and lifecycle processing, when separately authorized
  -> evidence, policy, review, release
  -> governed public-safe product
```

No direct path exists from briefing prose, a score, or a proposed issue operation to evidence, PUBLISHED state, public truth, or a public map/API/AI answer.

## Current bounded foundations

The current implementation remains deterministic, no-network, and file-backed:

1. `BriefingSignal` semantic and machine shape;
2. `TemporalAuthorityEnvelope` metadata profile;
3. deterministic daily identity, durable event clustering, replay/collision detection, and deduplication dry run; and
4. explainable materiality, exact priority reasons, mandatory overrides, and finite issue-routing dry run.

These foundations read repository fixtures and examples only. They do not fetch sources, query or write GitHub issues, create evidence, evaluate policy, approve review, mutate lifecycle state, release, deploy, publish, or authorize public use.

## Independent state machines

### Signal state

`DISCOVERED`, `DUPLICATE`, `NEEDS_VERIFICATION`, `CONFLICTED`, `ACCEPTED_FOR_MODELING`, `IMPLEMENTATION_TRACKED`, `REJECTED`, or `CLOSED`.

### Real-world state

Defined by each native domain contract. Examples include `scheduled`, `cancelled`, `rescinded`, `under_review`, `awarded`, or `completed`.

### KFM lifecycle state

`RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED`.

A transition in one state machine never implies a transition in another. `P0` is a review priority, not a lifecycle or authority state.

## Deterministic identity and deduplication

One daily revision receives a content-derived `signal_id`. Recurring coverage shares an `event_cluster_id` derived from story type, normalized primary authority, source-native identity, geography identity, and durable subject identity. The briefing date and headline are excluded from the cluster identity.

Exact replay is counted rather than recreated. A duplicate must reference its primary signal or matched issue. A duplicate cannot propose opening parallel work.

Materiality, routing, status, and operational metadata remain outside the signal content digest. Recalibrating a priority does not rewrite what was discovered.

## Explainable materiality

The architecture rejects a hidden model judgment or one opaque confidence number. Every signal declares ten dimensions from `0..5`:

- public safety;
- repository integrity;
- geospatial relevance;
- recurrence;
- reuse value;
- authority quality;
- time sensitivity;
- rights and sensitivity risk;
- identity uncertainty; and
- implementation readiness.

The `kfm-briefing-materiality-v1` formula is:

```text
raw_score =
    3*public_safety
  + 3*repository_integrity
  + 2*time_sensitivity
  + 2*recurrence
  + 2*reuse_value
  + 2*geospatial_relevance
  + authority_quality
  + implementation_readiness
  - 2*rights_sensitivity_risk
  - 2*identity_uncertainty
```

### Initial proposed thresholds

| Priority | Deterministic threshold | Interpretation |
|---|---:|---|
| `P0` | `>=55` or mandatory override | Immediate bounded safety or repository-integrity review. |
| `P1` | `35..54` | High-reuse or recurring capability/source work. |
| `P2` | `20..34` | Useful planning, governance, source, or modeling work. |
| `P3` | `1..19` | Context worth retaining or rechecking. |
| `IGNORE` | `<=0` | No engineering action from the current signal. |

The thresholds are the initial versioned profile, not adopted KFM policy. A successor requires a new profile identifier, exact boundary fixtures, migration documentation, and historical-score preservation.

### Mandatory overrides

Three finite conditions force `P0` while preserving the raw score:

- confirmed active public-safety conflict;
- unexpected repository merge; and
- a public artifact reading an internal store.

The local validator can prove only that the override declaration is internally consistent. It cannot prove the underlying event.

### Explainability

Every nonzero dimension produces a finite reason code. Negative-risk dimensions remain visible rather than being hidden in the total. The applied override reason is included. A zero-input signal uses `LOW_MATERIALITY`. Free-form rationale supplements but never replaces the machine reasons.

## Finite routing

The dry-run routing engine consumes deduplication, priority, official-support posture, modeling readiness, dependency state, safety state, and issue kind. It applies this precedence:

```text
existing issue match
  -> UPDATE_EXISTING_ISSUE
else duplicate cluster
  -> NO_ACTION
else unsafe
  -> REJECT_UNSAFE
else dependency blocked
  -> HOLD_FOR_DEPENDENCY
else P0 corrective + official support resolved
  -> OPEN_CORRECTIVE_ISSUE
else P0/P1 source discovery + modeling ready
  -> OPEN_SOURCE_DISCOVERY_ISSUE
else P0/P1 object model + modeling ready
  -> OPEN_OBJECT_MODEL_ISSUE
else
  -> NO_ACTION with exact reason
```

The output is a proposed operation only. It always carries:

```json
{
  "authority_created": false,
  "repository_mutation_allowed": false
}
```

`ERROR` remains a finite evaluator outcome; it is not a normal route selected from a valid signal.

## Shared temporal-authority foundation

`TemporalAuthorityEnvelope` binds stable object identity, exact revision identity, SourceDescriptor role references, issuing/observing authority, distinct temporal meanings, governed geography, certainty, correction/supersession lineage, and evidence/policy/review/release references with public use fixed to false.

It contains no generic domain payload and does not accept ADR-0014, replace `TemporalWindow`, or silently choose a global temporal vocabulary.

## Water-planning reference lane

The existing water-planning tests preserve distinctions among meeting, application, recommendation, award, payment, construction, completion, program version, scoring version, geometry, identity, crosswalk, and lineage.

```text
meeting != approval
application != recommendation
application != award
recommendation != award
award != payment
payment != construction
construction != completion
program/scoring version != outcome
```

### Hays meeting example

The candidate records only the official source announcement, scheduled times, venue text, conducting agencies, topics, and unresolved venue/regional geometries. The occurrence and outcomes remain unverified. Existing issue `#1647` wins routing precedence, so the dry run proposes an idempotent update rather than another issue.

### GMD action-plan index example

The candidate records link-presence observations and listed dates without converting them into submission acceptance, review, approval, implementation, supersession, or outcome claims. Missing links are not non-submission. Existing issue `#1647` again wins routing precedence.

## CI integration

The read-only `briefing-integration` workflow:

1. runs all `test_briefing_signal*.py` tests;
2. validates six positive fixtures and two non-authoritative examples;
3. runs the clustering dry run;
4. runs the explainable materiality/routing dry run;
5. proves five structural-invalid and six schema-valid semantic-negative fixtures fail closed;
6. preserves TemporalAuthorityEnvelope regression coverage; and
7. preserves water-planning anti-collapse and RAC-registry checks.

A green workflow proves only the declared fixture behavior. It is not evidence, issue authorization, policy, review, proof, release, deployment, publication, or public truth.

## Failure posture

| Condition | Outcome |
|---|---|
| Declared score differs from recomputation | Reject signal. |
| Declared priority differs from threshold profile | Reject signal. |
| Priority lacks exact reasons | Reject signal. |
| Override lacks compatible dimension context | Reject signal. |
| Proposed disposition differs from deterministic routing | Reject signal. |
| Duplicate proposes parallel work | Reject signal. |
| Unsafe route | `REJECT_UNSAFE`; no issue mutation. |
| Missing dependency | `HOLD_FOR_DEPENDENCY`; no issue mutation. |
| Official support unresolved for corrective route | `NO_ACTION` with explicit reason. |
| Confirmed claim lacks evidence | Reject signal. |
| Inline or secret-like candidate data | Reject signal. |
| Public or consequential permission is true | Reject signal. |

## Next implementation stages

1. Define an immutable official-source snapshot candidate adapter that emits no EvidenceBundle and performs no source activation.
2. Bind the routing dry run to a read-only, fixture-backed issue inventory projection before any live GitHub read.
3. Add conflict/correction/supersession fixture profiles for volatile facts.
4. Add domain-native advisory and condition envelopes without replacing native contracts.
5. Add live source access only after SourceDescriptor, rights, sensitivity, retrieval receipt, and rollback gates are verified.
6. Add public products only after evidence, policy, review, release, correction, and rollback close.

## Non-goals

- no live web connector;
- no scheduler;
- no GitHub issue-writing automation;
- no repository self-authorization;
- no source activation or EvidenceBundle construction;
- no global temporal-vocabulary decision;
- no public API, map, search, graph, Focus Mode, or AI route;
- no policy, review, promotion, release, deployment, or publication;
- no claim that priority proves urgency or truth.

## Rollback

Before merge, close the draft and abandon the branch. After merge, revert the bounded integration commit through review. A future threshold successor preserves old scores and profile identity. No external event, issue, source, evidence, lifecycle, release, or public state is created by this slice.

[Back to top](#top)
