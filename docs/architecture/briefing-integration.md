<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-architecture-briefing-integration
title: Briefing-to-System Integration Architecture
type: architecture; implementation-guide
version: v0.5.0
status: proposed; five bounded no-network foundations
owners: OWNER_TBD — Architecture steward · Governance steward · Domain stewards · Source/evidence/policy/release stewards
created: 2026-07-29
updated: 2026-08-06
policy_label: public; architecture; briefing-integration; no-public-authority
related:
  - ../../contracts/governance/briefing_signal.md
  - ../../schemas/contracts/v1/governance/briefing_signal.schema.json
  - ../../tools/validators/governance/validate_briefing_signal.py
  - ../../tools/validators/governance/deduplicate_briefing_signals.py
  - ../../tools/validators/governance/route_briefing_signals.py
  - ../../contracts/governance/issue_inventory_projection.md
  - ../../schemas/contracts/v1/governance/issue_inventory_projection.schema.json
  - ../../tools/validators/governance/validate_issue_inventory_projection.py
  - ../../contracts/common/temporal_authority_envelope.md
  - ../../schemas/contracts/v1/common/temporal_authority_envelope.schema.json
  - ../../examples/briefing_integration/README.md
  - ../../.github/workflows/briefing-integration.yml
tags: [kfm, architecture, briefing, identity, deduplication, materiality, routing, issue-inventory, temporal-authority, water-planning, evidence-first]
notes:
  - "v0.5 adds a deterministic read-only issue inventory projection before any live GitHub read."
  - "Candidate-supplied matched issue IDs no longer suffice for the routing dry run to retain UPDATE_EXISTING_ISSUE."
  - "The projection remains fixture-only and creates no live-state, repository, issue-mutation, policy, review, release, or publication authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Briefing-to-System Integration Architecture

> Convert recurring briefing stories into governed verification and modeling
> work without using briefing prose, priority scores, candidate-supplied issue
> IDs, or dry-run routing as evidence or as authority for repository mutation,
> source activation, policy, proof, release, deployment, publication, or public
> use.

## Operating flow

```text
Daily briefing
  -> BriefingSignal
  -> deterministic identity and event clustering
  -> explainable materiality and declared finite routing
  -> validated local IssueInventoryProjection when an existing issue is claimed
  -> open-target binding or fail-closed HOLD
  -> official-source snapshot or explicit unresolved state
  -> object-family classification
  -> human-reviewed existing-issue update or bounded new issue
  -> domain object + TemporalAuthorityEnvelope, when separately modeled
  -> contract/schema/fixture/validator work
  -> source admission and lifecycle processing, when separately authorized
  -> evidence, policy, review, release
  -> governed public-safe product
```

No direct path exists from briefing prose, a score, a candidate issue number, or
a proposed issue operation to evidence, PUBLISHED state, public truth, or a
public map/API/AI answer.

## Current bounded foundations

The current implementation remains deterministic, no-network, and file-backed:

1. `BriefingSignal` semantic and machine shape;
2. `TemporalAuthorityEnvelope` metadata profile;
3. deterministic daily identity, durable event clustering, replay/collision
   detection, and deduplication dry run;
4. explainable materiality, exact priority reasons, mandatory overrides, and
   finite declared issue routing; and
5. a fixture-backed `IssueInventoryProjection` that independently checks whether
   a declared existing-issue target is present and open.

These foundations read repository fixtures and examples only. They do not fetch
sources, read live GitHub state, write GitHub issues, create evidence, evaluate
policy, approve review, mutate lifecycle state, release, deploy, publish, or
authorize public use.

## Independent state machines

### Signal state

`DISCOVERED`, `DUPLICATE`, `NEEDS_VERIFICATION`, `CONFLICTED`,
`ACCEPTED_FOR_MODELING`, `IMPLEMENTATION_TRACKED`, `REJECTED`, or `CLOSED`.

### Real-world state

Defined by each native domain contract. Examples include `scheduled`,
`cancelled`, `rescinded`, `under_review`, `awarded`, or `completed`.

### KFM lifecycle state

`RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED`.

### Repository issue state

The fixture profile recognizes only `OPEN` and `CLOSED`. That local state is not
a replacement for live GitHub evidence, rulesets, permissions, review state,
merge state, or repository authorization.

A transition in one state machine never implies a transition in another. `P0`
is a review priority, not a lifecycle or authority state. An open issue is not
evidence, policy approval, release authority, or permission to mutate it.

## Deterministic identity and deduplication

One daily revision receives a content-derived `signal_id`. Recurring coverage
shares an `event_cluster_id` derived from story type, normalized primary
authority, source-native identity, geography identity, and durable subject
identity. The briefing date and headline are excluded from the cluster
identity.

Exact replay is counted rather than recreated. A duplicate must reference its
primary signal or matched issue. A duplicate cannot propose opening parallel
work.

Materiality, routing, status, operational metadata, and issue-inventory state
remain outside the signal content digest. Recalibrating a priority or refreshing
an issue projection does not rewrite what was discovered.

## Explainable materiality

The architecture rejects a hidden model judgment or one opaque confidence
number. Every signal declares ten dimensions from `0..5`:

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

The thresholds are the initial versioned profile, not adopted KFM policy. A
successor requires a new profile identifier, exact boundary fixtures, migration
documentation, and historical-score preservation.

### Mandatory overrides

Three finite conditions force `P0` while preserving the raw score:

- confirmed active public-safety conflict;
- unexpected repository merge; and
- a public artifact reading an internal store.

The local validator can prove only that the override declaration is internally
consistent. It cannot prove the underlying event.

### Explainability

Every nonzero dimension produces a finite reason code. Negative-risk dimensions
remain visible rather than being hidden in the total. The applied override
reason is included. A zero-input signal uses `LOW_MATERIALITY`. Free-form
rationale supplements but never replaces the machine reasons.

## Declared routing and issue-inventory binding

The BriefingSignal validator computes a declared route from deduplication,
priority, official-support posture, modeling readiness, dependency state,
safety state, and issue kind. It applies this precedence:

```text
existing issue match
  -> declared UPDATE_EXISTING_ISSUE
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

A declared existing-issue match now passes through a second deterministic gate:

```text
no IssueInventoryProjection
  -> HOLD_FOR_DEPENDENCY / ISSUE_INVENTORY_REQUIRED
target absent
  -> HOLD_FOR_DEPENDENCY / ISSUE_INVENTORY_TARGET_MISSING
all declared targets closed
  -> HOLD_FOR_DEPENDENCY / ISSUE_INVENTORY_TARGET_CLOSED
more than one declared target open
  -> HOLD_FOR_DEPENDENCY / ISSUE_INVENTORY_AMBIGUOUS_OPEN_TARGETS
exactly one declared target open and none missing
  -> UPDATE_EXISTING_ISSUE / ISSUE_INVENTORY_OPEN_TARGET
```

The output remains a proposed operation only. It always carries:

```json
{
  "authority_created": false,
  "repository_mutation_allowed": false
}
```

`ERROR` remains a finite evaluator outcome; it is not a normal route selected
from a valid signal.

## IssueInventoryProjection boundary

`IssueInventoryProjection` profile
`kfm.briefing.issue-inventory.fixture.v1` contains only:

- repository identity;
- fixture provenance;
- projection time;
- sorted issue number;
- `OPEN` or `CLOSED` state;
- issue update time;
- deterministic count, digest, and projection ID; and
- fixed false live-state, authority, and mutation flags.

The digest uses canonical sorted-key JSON excluding only the digest and
projection ID. Duplicate issue numbers, unsorted rows, future update times,
count mismatch, digest mismatch, ID mismatch, and any true trust-bearing flag
fail closed.

The fixture is not current GitHub evidence. It contains no title, body, comment,
label, assignee, reviewer, permission, mergeability, ruleset, or branch state.

## Shared temporal-authority foundation

`TemporalAuthorityEnvelope` binds stable object identity, exact revision
identity, SourceDescriptor role references, issuing/observing authority,
distinct temporal meanings, governed geography, certainty,
correction/supersession lineage, and evidence/policy/review/release references
with public use fixed to false.

It contains no generic domain payload and does not accept ADR-0014, replace
`TemporalWindow`, or silently choose a global temporal vocabulary.

## Water-planning reference lane

The existing water-planning tests preserve distinctions among meeting,
application, recommendation, award, payment, construction, completion, program
version, scoring version, geometry, identity, crosswalk, and lineage.

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

The candidate records only the official source announcement, scheduled times,
venue text, conducting agencies, topics, and unresolved venue/regional
geometries. The occurrence and outcomes remain unverified. It declares existing
issue `#1647`. With the synthetic `open-target` projection, the dry run binds
that route to the one open target. Without a projection, it now holds rather
than trusting the candidate-supplied issue number.

### GMD action-plan index example

The candidate records link-presence observations and listed dates without
converting them into submission acceptance, review, approval, implementation,
supersession, or outcome claims. Missing links are not non-submission. It also
declares `#1647` and follows the same projection-bound behavior.

## CI integration

The read-only `briefing-integration` workflow:

1. runs all `test_briefing_signal*.py` tests;
2. validates positive BriefingSignal fixtures and examples;
3. runs the clustering dry run;
4. validates all positive IssueInventoryProjection fixtures;
5. proves all negative IssueInventoryProjection fixtures fail closed;
6. runs materiality/routing with the synthetic open-target projection;
7. proves structural-invalid and schema-valid semantic-negative BriefingSignal
   fixtures fail closed;
8. preserves TemporalAuthorityEnvelope regression coverage; and
9. preserves water-planning anti-collapse and RAC-registry checks.

A green workflow proves only the declared fixture behavior. It is not evidence,
live issue state, issue authorization, policy, review, proof, release,
deployment, publication, or public truth.

## Failure posture

| Condition | Outcome |
|---|---|
| Declared score differs from recomputation | Reject signal. |
| Declared priority differs from threshold profile | Reject signal. |
| Priority lacks exact reasons | Reject signal. |
| Override lacks compatible dimension context | Reject signal. |
| Proposed disposition differs from deterministic declared routing | Reject signal. |
| Duplicate proposes parallel work | Reject signal. |
| Existing-issue route lacks a projection | `HOLD_FOR_DEPENDENCY`. |
| Projected target is missing or closed | `HOLD_FOR_DEPENDENCY`. |
| More than one declared target is open | `HOLD_FOR_DEPENDENCY`. |
| Projection shape, count, time, digest, or ID is invalid | Fail the dry run. |
| Projection claims live verification, authority, or mutation | Reject projection. |
| Unsafe route | `REJECT_UNSAFE`; no issue mutation. |
| Missing dependency | `HOLD_FOR_DEPENDENCY`; no issue mutation. |
| Official support unresolved for corrective route | `NO_ACTION` with explicit reason. |
| Confirmed claim lacks evidence | Reject signal. |
| Inline or secret-like candidate data | Reject signal. |
| Public or consequential permission is true | Reject signal. |

## Next implementation stages

1. Define an immutable official-source snapshot candidate adapter that emits no
   EvidenceBundle and performs no source activation.
2. Add conflict/correction/supersession fixture profiles for volatile facts.
3. Add a separately reviewed, authenticated read-only GitHub projection adapter
   with retrieval receipts and stale-state handling; preserve this fixture
   profile as the deterministic contract test.
4. Add domain-native advisory and condition envelopes without replacing native
   contracts.
5. Add live source access only after SourceDescriptor, rights, sensitivity,
   retrieval receipt, and rollback gates are verified.
6. Add public products only after evidence, policy, review, release, correction,
   and rollback close.

## Non-goals

- no live web connector;
- no scheduler;
- no live GitHub read;
- no GitHub issue-writing automation;
- no repository self-authorization;
- no source activation or EvidenceBundle construction;
- no global temporal-vocabulary decision;
- no public API, map, search, graph, Focus Mode, or AI route;
- no policy, review, promotion, release, deployment, or publication;
- no claim that priority or projected issue state proves urgency or truth.

## Rollback

Before merge, close the draft and abandon the branch. After merge, revert the
bounded integration commit through review. A future live adapter does not
rewrite fixture history. No external event, issue, source, evidence, lifecycle,
release, cache, deployment, or public state is created by this slice.

[Back to top](#top)
