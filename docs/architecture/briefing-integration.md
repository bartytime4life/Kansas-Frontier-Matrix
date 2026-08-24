<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-architecture-briefing-integration
title: Briefing-to-System Integration Architecture
type: architecture; implementation-guide
version: v0.8.0
status: proposed; bounded foundations reconciled through authenticated read-only GitHub issue observation
owners: OWNER_TBD — Architecture steward · Governance steward · Domain stewards · Source/evidence/policy/release stewards
created: 2026-07-29
updated: 2026-08-24
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
  - ../../contracts/governance/github_issue_inventory_read.md
  - ../../schemas/contracts/v1/governance/github_issue_inventory_read.schema.json
  - ../../tools/validators/governance/validate_github_issue_inventory_read.py
  - ../../tools/probes/github_issue_inventory_read.py
  - ../../contracts/common/temporal_authority_envelope.md
  - ../../schemas/contracts/v1/common/temporal_authority_envelope.schema.json
  - ../../contracts/source/official_source_snapshot_candidate.md
  - ../../contracts/source/official_source_snapshot_lineage_assessment.md
  - ../../contracts/source/source_obligation_propagation_assessment.md
  - ../../contracts/evidence/evidence_binding_chain_assessment.md
  - ../../examples/briefing_integration/README.md
  - ../../.github/workflows/briefing-integration.yml
  - ../../.github/workflows/github-issue-inventory-read.yml
tags: [kfm, architecture, briefing, identity, deduplication, materiality, routing, issue-inventory, github-read, temporal-authority, source-snapshot, evidence-binding, water-planning, evidence-first]
notes:
  - "v0.8 adds five non-authoritative reporting lenses without creating domain, schema, routing, lifecycle, evidence, policy, review, release, or publication authority."
  - "v0.7 corrects the prior future-stage claim: the repository already contains a separately bounded authenticated read-only GitHub issue-observation profile, probe, validator, fixtures/tests, and workflow."
  - "GitHubIssueInventoryRead remains PROPOSED_INACTIVE and creates no repository mutation, evidence, policy, review, release, publication, or public-use authority."
  - "Live source access, authoritative source/evidence/policy resolution, and public products remain separately reviewed future stages."
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
  -> optional separately invoked authenticated GitHubIssueInventoryRead observation
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

No direct path exists from briefing prose, a score, a candidate issue number, a
fixture projection, or a live-read observation to evidence, PUBLISHED state,
public truth, repository mutation, or a public map/API/AI answer.

## Current bounded foundations

The repository now contains deterministic fixture-backed foundations plus one
separately invoked authenticated read-only GitHub observation profile. The
bounded foundations are:

1. `BriefingSignal` semantic and machine shape;
2. `TemporalAuthorityEnvelope` metadata profile;
3. deterministic daily identity, durable event clustering, replay/collision
   detection, and deduplication dry run;
4. explainable materiality, exact priority reasons, mandatory overrides, and
   finite declared issue routing;
5. a fixture-backed `IssueInventoryProjection` that independently checks whether
   a declared existing-issue target is present and open;
6. `GitHubIssueInventoryRead`, a separate `PROPOSED_INACTIVE` authenticated,
   read-only observation profile with repository/ref binding, freshness,
   rate-limit posture, deterministic response binding, and fixed false
   authority/mutation/public-use flags;
7. `OfficialSourceSnapshotCandidate`, which models an immutable source-snapshot
   candidate without activating or fetching a live source;
8. `OfficialSourceSnapshotLineageAssessment`, which tests correction,
   supersession, conflict, and lineage declarations for snapshot candidates;
9. `EvidenceBindingChainAssessment`, which proves only synthetic reference
   closure from one `SourceArtifact` through parse output and `EvidenceRef` to a
   field binding; and
10. `SourceObligationPropagationAssessment`, which checks that declared
   attribution and use obligations are not dropped across synthetic derivative,
   catalog-candidate, and export-candidate carriers.

The fixture-backed foundations consume repository fixtures and checked-in
examples only. The GitHub read profile may make authenticated GET-only calls
only when explicitly invoked with a read credential; it minimizes returned
issue state and fails closed on authentication, binding, freshness, malformed
responses, or unusable rate-limit posture.

None of these foundations writes GitHub issues, activates sources,
authenticates an `EvidenceBundle`, decides rights or policy, approves review,
mutates lifecycle state, releases, deploys, publishes, or authorizes public use.
A `PASS` on a candidate/assessment or a `FRESH` GitHub read means only that the
named bounded contract closed under its declared conditions.

## Non-authoritative reporting lenses

Recurring briefing stories may be summarized through one primary lens and
secondary tags. The lens identifies the reporting pattern and its anti-collapse
risk; it does not classify truth, replace the native object family, or select a
route.

| Lens | Typical material | Required separation |
|---|---|---|
| Repository governance and control | Branch and pull-request state, CI ambiguity, review coverage, ruleset drift, campaign cursors, and compatibility migration | Repository observations are not geospatial lifecycle or public-truth events. |
| Volatile advisories and public-safety events | Alerts, advisories, closures, rescissions, and status checks | Retrieval failure is not a clear state; the native issuer and event status remain visible. |
| Conditions, observations, classifications, and forecasts | Station observations, modeled grids, surveys, statewide classes, and forecasts | Source role, scale, resolution, time, and uncertainty remain distinct. |
| Governance events and public participation | Meetings, hearings, workshops, rulemaking, comment windows, recommendations, and decisions | Announcement, participation, recommendation, decision, and implementation remain separate states. |
| Funding, projects, and measured outcomes | Programs, eligibility, applications, reviews, awards, agreements, projects, payments, milestones, completion, observations, and evaluation | Funding, completed work, and observed outcomes cannot be inferred from one another. |

These labels are a contributor and reporting view only. They add no domain
type, schema field, priority, state, evidence, policy, review, routing, release,
or publication authority. The native object family, source role, real-world
state, KFM lifecycle state, and governed evidence and policy surfaces continue
to control. See the
[source reconciliation](../intake/exploratory/circled-whole-system-sources-distinctive-delta-source-map.md#33-five-briefing-lenses)
for the proposal lineage.

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

The deterministic fixture profile recognizes only `OPEN` and `CLOSED`.
`GitHubIssueInventoryRead` can separately observe minimized live issue state for
one bound repository/default-branch context when explicitly invoked, but that
observation is not evidence, ruleset/permission authority, review state, merge
state, or repository mutation authorization.

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

A declared existing-issue match passes through a deterministic gate:

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

The fixture projection remains the deterministic contract-test input. A
separately invoked `GitHubIssueInventoryRead` may provide a fresh minimized
repository-state observation for higher-level verification, but it does not by
itself authorize routing mutation or replace the deterministic fixture profile.

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

## GitHubIssueInventoryRead boundary

`GitHubIssueInventoryRead` is a separate authenticated read-only profile, not a
replacement for the fixture contract. Its current contract requires:

- `GET` only;
- credential from `KFM_GITHUB_READ_TOKEN` or `GITHUB_TOKEN`, never serialized or
  logged;
- binding to repository identity, numeric repository ID, default branch, and
  default-branch head SHA;
- unique sorted positive issue numbers;
- issue-only minimized rows containing `number`, `state`, and `updated_at`;
- rejection of pull-request objects returned through the Issues API;
- explicit `retrieved_at` / `stale_at` freshness;
- recorded rate-limit state when supplied;
- deterministic response digest and receipt ID; and
- fixed false mutation, authority, evidence, release, publication, and public-use
  flags.

Its finite outcomes are `FRESH`, `STALE`, `HOLD_AUTH`, `HOLD_RATE_LIMIT`,
`HOLD_BINDING`, and `ERROR`. `FRESH` proves only the bounded observation at the
recorded time. It does not prove issue content correctness or grant any write,
merge, source, evidence, policy, review, release, deployment, or publication
authority.

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
that route to the one open target. Without a projection, it holds rather than
trusting the candidate-supplied issue number.

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

The separate `github-issue-inventory-read` workflow covers the authenticated
read-only profile independently of the deterministic briefing fixture flow. Its
presence does not make every briefing run a live GitHub read and does not grant
write permission.

A green workflow proves only the declared checked behavior. It is not evidence,
issue-mutation authorization, policy, review, proof, release, deployment,
publication, or public truth.

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
| Live-read credential/authentication is unresolved | `HOLD_AUTH`. |
| Live-read repository/ref binding is unresolved | `HOLD_BINDING`. |
| Live-read rate-limit posture is unusable | `HOLD_RATE_LIMIT`. |
| Live-read freshness expires | `STALE`. |
| Live-read response is malformed or includes a pull-request object | `ERROR`. |
| Unsafe route | `REJECT_UNSAFE`; no issue mutation. |
| Missing dependency | `HOLD_FOR_DEPENDENCY`; no issue mutation. |
| Official support unresolved for corrective route | `NO_ACTION` with explicit reason. |
| Confirmed claim lacks evidence | Reject signal. |
| Inline or secret-like candidate data | Reject signal. |
| Public or consequential permission is true | Reject signal. |

## Next implementation stages

The official-source snapshot candidate, snapshot-lineage assessment,
domain-native advisory/condition profiles, bounded evidence/obligation
assessments, and separately bounded authenticated read-only GitHub issue
observation have landed. The remaining stages require stronger evidence or
explicit authorization:

1. resolve candidate source/evidence assessments against actual
   `SourceDescriptor`, rights, sensitivity, evidence, policy, and review state
   only in separately authorized source/evidence slices;
2. add live source access only after source admission, rights, sensitivity,
   retrieval receipt, correction, and rollback gates are verified;
3. connect bounded evidence resolution to governed runtime/API behavior only
   after policy, review, release, citation, correction, and precision obligations
   are explicit and fail-closed; and
4. add public products only after evidence, policy, review, release, correction,
   and rollback close.

No remaining stage is authorized by this document merely because its precursor
fixture packet or read-only observation profile exists.

## Non-goals

- no automatic or live-by-default GitHub read in briefing evaluation;
- no scheduler;
- no GitHub issue-writing automation;
- no repository self-authorization;
- no source activation or authoritative EvidenceBundle construction;
- no live source access by this architecture slice;
- no global temporal-vocabulary decision;
- no public API, map, search, graph, Focus Mode, or AI route from briefing state;
- no policy, review, promotion, release, deployment, or publication;
- no claim that priority, fixture projection, or live-read issue state proves
  urgency, truth, or mutation permission.

## Rollback

Before merge, close the draft and abandon the branch. After merge, revert this
documentation correction through review. The correction does not rewrite fixture
history and does not change the behavior or activation status of the existing
GitHub read profile. No external event, issue mutation, source, evidence,
lifecycle, release, cache, deployment, or public state is created by this slice.

[Back to top](#top)
