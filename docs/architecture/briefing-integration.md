<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-architecture-briefing-integration
title: Briefing-to-System Integration Architecture
type: architecture; implementation-guide
version: v0.3.0
status: proposed; three bounded no-network implementation foundations
owners: OWNER_TBD — Architecture steward · Governance steward · Domain stewards · Source/evidence/policy/release stewards
created: 2026-07-29
updated: 2026-08-03
policy_label: public; architecture; briefing-integration; no-public-authority
related:
  - ../../contracts/governance/briefing_signal.md
  - ../../schemas/contracts/v1/governance/briefing_signal.schema.json
  - ../../tools/validators/governance/validate_briefing_signal.py
  - ../../tools/validators/governance/deduplicate_briefing_signals.py
  - ../../tests/governance/test_briefing_signal.py
  - ../../tests/governance/test_briefing_signal_dedup.py
  - ../../contracts/common/temporal_authority_envelope.md
  - ../../schemas/contracts/v1/common/temporal_authority_envelope.schema.json
  - ../../fixtures/contracts/v1/common/temporal_authority_envelope/
  - ../../tools/validators/validate_temporal_authority_envelope.py
  - ../../tests/validators/test_validate_temporal_authority_envelope.py
  - ../../examples/briefing_integration/README.md
  - ../../tools/validators/domains/water_planning/validate_status_collapse.py
  - ../../.github/workflows/briefing-integration.yml
  - ../../.github/workflows/infra-compose-smoke.yml
tags: [kfm, architecture, briefing, temporal-authority, identity, deduplication, issue-routing, governance-event, water-planning, evidence-first]
notes:
  - "v0.3 adds deterministic BriefingSignal identity, durable event clustering, replay handling, and issue-routing dry-run behavior."
  - "The slice still performs no source retrieval, GitHub issue mutation, source activation, evidence construction, policy, review, release, deployment, publication, or public use."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Briefing-to-System Integration Architecture

> Convert daily briefing stories into governed verification and modeling work without using briefing prose as evidence or creating an automatic path to repository mutation, source activation, proof, release, deployment, or publication.

## Operating flow

```text
Daily briefing
  -> BriefingSignal
  -> deterministic daily signal identity
  -> durable event-cluster and replay check
  -> explainable materiality check
  -> official-source snapshot or explicit unresolved state
  -> object-family classification
  -> existing-issue update or bounded new-issue proposal
  -> domain object + TemporalAuthorityEnvelope, when separately modeled
  -> contract/schema/fixture/validator work
  -> source admission and lifecycle processing, when separately authorized
  -> evidence, policy, review, release
  -> governed public-safe product
```

The current bounded implementation stops at three no-network foundations:

1. `BriefingSignal` meaning, closed shape, examples, and non-authoritative permissions;
2. `TemporalAuthorityEnvelope` metadata profile, synthetic fixtures, and deterministic validation; and
3. deterministic BriefingSignal identity, event clustering, replay detection, and issue-routing dry run.

None fetches a source, creates evidence, mutates an issue, replaces a domain contract, evaluates policy, releases, deploys, publishes, or authorizes public use.

## Three independent states

### Signal state

`DISCOVERED`, `DUPLICATE`, `NEEDS_VERIFICATION`, `CONFLICTED`, `ACCEPTED_FOR_MODELING`, `IMPLEMENTATION_TRACKED`, `REJECTED`, or `CLOSED`.

### Real-world state

Defined by the domain object. Examples include `scheduled`, `cancelled`, `rescinded`, `under_review`, `awarded`, and `completed`.

### KFM lifecycle state

`RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED`.

No transition in one state machine implies a transition in another.

## Deterministic BriefingSignal identity and deduplication

Daily briefings repeat material stories. KFM now models repetition as later signal revisions attached to one durable event cluster rather than as new work each day.

### Identity layers

| Identity | Lifetime | Implemented bounded meaning |
|---|---|---|
| `signal_id` | One daily signal revision | Derived from briefing date and canonicalized substantive candidate content. |
| `event_cluster_id` | Across briefing dates | Derived from story type, authority, native identity key, geography identity, and durable subject key. |
| `signal_digest` | Exact canonical candidate content | Full SHA-256 used to reproduce and collision-check a daily signal. |
| issue `idempotency_key` | One proposed routing operation | Binds cluster, disposition, scope, and matched issue IDs. |

The event cluster intentionally excludes the briefing date and orientation headline. A revised headline creates a new `signal_id` but retains the cluster when authority, native identity, geography, subject, and story type remain the same.

### Exact matching precedence

1. deterministic event-cluster identity;
2. source-native identity plus authority;
3. explicit existing KFM object or issue link;
4. compatible authority, place, event type, and time; and
5. headline similarity only as non-authoritative context after identity and geography checks.

Identity ambiguity becomes `CONFLICTED`; it is not resolved by generated text or a headline-only merge.

### Deduplication outcomes

| Outcome | Required behavior |
|---|---|
| `UNIQUE` | No matches and `NEW_CLUSTER`; a bounded new issue may later be proposed. |
| `DUPLICATE` | References an existing signal or issue; only update-existing or no-action routing is valid. |
| `CONFLICTED` | Retains conflict reason and does not silently collapse identities. |
| `UNRESOLVED` | Holds when match evidence is insufficient. |

`tools/validators/governance/deduplicate_briefing_signals.py` reads validated local records, emits deterministic cluster and proposed-operation JSON, treats exact replay as replay, detects signal-ID collision, and rejects duplicate issue creation. It always emits:

```json
{
  "authority_created": false,
  "repository_mutation_allowed": false
}
```

It does not read GitHub or write an issue.

## Shared temporal-authority foundation

`TemporalAuthorityEnvelope` provides cross-domain metadata around a changing object. It binds:

- stable object identity and exact revision identity;
- a governed SourceDescriptor reference, a role-field reference bound to that descriptor, issuing or observing authority, and authority scope;
- issued, effective, validity, observation, retrieval, correction, and supersession fields;
- source-native geography text, governed geography reference, geometry role, and geometry confidence;
- native and normalized state plus certainty;
- correction, withdrawal, and supersession lineage; and
- evidence, policy, review, release references with `public_use_allowed = false`.

The envelope intentionally contains no generic domain payload. Advisories, observations, classifications, governance events, programs, awards, projects, and completions keep their native semantic contracts and state machines.

### Temporal compatibility boundary

The repository carries a proposed ADR-0014 vocabulary, an executable but still proposed `TemporalWindow` profile, and broader time-awareness doctrine. This envelope does not select among or silently crosswalk those vocabularies. Acceptance or migration of a global temporal vocabulary remains separate governance work.

### Fail-closed checks

| Condition | Outcome |
|---|---|
| Stable object identity equals exact revision identity | Reject envelope. |
| Validity interval is reversed | Reject envelope. |
| Source issue, observation, correction, or supersession time follows represented retrieval | Reject envelope. |
| Source-role reference is not bound to the declared SourceDescriptor role field | Reject envelope. |
| Confirmed state lacks an evidence reference | Reject envelope. |
| Geography is unresolved but presented as authoritative or confirmed | Reject envelope. |
| Correction or supersession lacks linked lineage | Reject envelope. |
| Self-lineage or contradictory lineage direction exists | Reject envelope. |
| Public use is true | Reject envelope. |

A passing envelope proves only bounded shape and semantic consistency.

## First integrated reference lane: Kansas water planning

The repository separates water-planning meetings, program and scoring versions, application windows, applications, eligibility decisions, recommendations, awards, agreements, projects, construction milestones, completions, and corrections or withdrawals.

The briefing workflow executes the water-planning anti-collapse suite so that:

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

The workflow does not convert this validator into a required host-side check or release gate by itself.

## Hays reference candidate

`examples/briefing_integration/hays_water_local_consult_2026_07_29.json` records only the official announcement, scheduled times, venue text, conducting agencies, announced topics, and unresolved geometries.

It is deterministically linked to an event cluster and existing issue #1647. The proposed operation is an idempotent issue update, not a second issue. Because no authoritative post-event record was captured in this slice, the candidate remains `STATUS_UNCONFIRMED` and does not claim occurrence, attendance, submissions, recommendations, decisions, funding, projects, or outcomes.

## Groundwater action-plan index candidate

`examples/briefing_integration/gmd_action_plan_inventory_2026_07_29.json` records a versioned observation of the Kansas Department of Agriculture index:

- GMD Nos. 2, 3, and 5 have action-plan links on the index;
- GMD No. 1 has a priority-area link but no action-plan link on the index;
- GMD No. 4 priority areas are listed as due January 1, 2028; and
- review, approval, implementation, supersession, and outcome state remain unresolved.

It is also linked idempotently to issue #1647. Link presence is not submission acceptance or approval; a missing link is not non-submission. District and priority-area geometries remain separate unresolved references.

## CI integration

### `briefing-integration`

The read-only workflow:

1. runs both BriefingSignal test modules;
2. validates all valid BriefingSignal fixtures and current examples;
3. runs the deterministic cluster/routing dry run over the valid fixture corpus;
4. runs the `TemporalAuthorityEnvelope` tests and fixtures;
5. runs the water-planning anti-collapse tests; and
6. emits only GitHub job results and summaries.

It creates no source snapshot, evidence record, issue, receipt, proof, release, deployment, or publication.

### `infra-compose-smoke`

The workflow runs no-network static checks, renders Compose configuration, and builds two placeholder images. It does not start containers or prove application runtime.

## Failure posture

| Condition | Outcome |
|---|---|
| Declared signal digest/ID/cluster/idempotency key does not reproduce | Reject signal. |
| Identity tokens are not normalized | Reject signal. |
| Confirmed claim lacks evidence | Reject signal. |
| Public or consequential permission is true | Reject signal. |
| Candidate payload embeds inline geometry or secret-like fields | Reject signal. |
| Same cluster opens a second issue | Reject routing. |
| Duplicate lacks a primary signal or issue reference | Reject routing. |
| Signal ID maps to different digests | Report collision and fail dry run. |
| Meeting occurrence is unsupported | Keep `STATUS_UNCONFIRMED`. |
| Official index lacks a plan link | Record link absence; do not infer non-submission. |
| Source cannot be snapshotted | Keep `SNAPSHOT_PENDING` or `UNAVAILABLE`. |
| Compose render or build fails | Block only the bounded infrastructure smoke surface. |

## Next implementation stages

1. Implement explainable materiality and routing thresholds without issue mutation.
2. Add immutable source-snapshot and EvidenceRef adapter contracts using synthetic HTTP fixtures.
3. Define `AdvisoryEventEnvelope` and one domain-native volatile-event payload using the shared temporal-authority profile.
4. Add governed source admission for selected KWO/KDA products after rights verification.
5. Add separate venue, planning-region, district, and priority-area geometry references.
6. Add correction, supersession, withdrawal, and freshness jobs.
7. Add public products only after evidence, policy, review, release, and rollback close.

## Non-goals of this slice

- no live web connector or scheduler;
- no issue-writing automation or repository self-authorization;
- no headline-only fuzzy merge authority;
- no global temporal-vocabulary decision or ADR acceptance;
- no meeting attendance, public-comment, plan-approval, or project-outcome inference;
- no container startup, API, UI route, source activation, proof, release, deployment, or publication.

## Rollback

Before merge, close the draft and abandon the branch. After merge, revert the scoped integration commit through review. A documentation, schema, validator, fixture, test, or workflow revert does not erase external events, source documents, prior signals, or unresolved claims. Preserve identifiers and correction/supersession lineage if any later consumer begins using the profile.

[Back to top](#top)
