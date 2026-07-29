<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-architecture-briefing-integration
title: Briefing-to-System Integration Architecture
type: architecture; implementation-guide
version: v0.1.0
status: proposed; bounded implementation slice
owners: OWNER_TBD — Architecture steward · Governance steward · Domain stewards · Source/evidence/policy/release stewards
created: 2026-07-29
updated: 2026-07-29
policy_label: public; architecture; briefing-integration; no-public-authority
related:
  - ../../contracts/governance/briefing_signal.md
  - ../../schemas/contracts/v1/governance/briefing_signal.schema.json
  - ../../examples/briefing_integration/README.md
  - ../../tools/validators/governance/validate_briefing_signal.py
  - ../../tools/validators/domains/water_planning/validate_status_collapse.py
  - ../../.github/workflows/briefing-integration.yml
  - ../../.github/workflows/infra-compose-smoke.yml
tags: [kfm, architecture, briefing, governance-event, water-planning, compose, evidence-first]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Briefing-to-System Integration Architecture

> Convert daily briefing stories into governed verification and modeling work without using briefing prose as evidence or creating an automatic path to repository mutation, source activation, proof, release, deployment, or publication.

## Operating flow

```text
Daily briefing
  -> BriefingSignal
  -> duplicate and materiality check
  -> official-source snapshot or explicit unresolved state
  -> object-family classification
  -> existing-issue update or bounded new issue
  -> contract/schema/fixture/validator work
  -> source admission and lifecycle processing, when separately authorized
  -> evidence, policy, review, release
  -> governed public-safe product
```

The first implementation stops at the `BriefingSignal`, examples, validation, and issue-routing boundary.

## Three independent states

### Signal state

`DISCOVERED`, `DUPLICATE`, `NEEDS_VERIFICATION`, `CONFLICTED`, `ACCEPTED_FOR_MODELING`, `IMPLEMENTATION_TRACKED`, `REJECTED`, or `CLOSED`.

### Real-world state

Defined by the domain object. Examples include `scheduled`, `cancelled`, `rescinded`, `under_review`, `awarded`, and `completed`.

### KFM lifecycle state

`RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED`.

No transition in one state machine implies a transition in another.

## First integrated reference lane: Kansas water planning

The repository already separates fifteen water-planning families, including meetings, program and scoring versions, application windows, applications, eligibility decisions, recommendations, awards, agreements, projects, construction milestones, completions, and corrections or withdrawals.

The briefing integration workflow executes the existing water-planning anti-collapse suite so that:

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

This workflow does not convert the validator into a required host-side check or release gate by itself. Repository settings must separately require a stable check.

## Hays reference candidate

`examples/briefing_integration/hays_water_local_consult_2026_07_29.json` records only:

- the official source announcement;
- scheduled start and end times;
- venue text;
- conducting agencies;
- announced topics; and
- unresolved venue and regional geometries.

Because the observation occurred after the scheduled window and no authoritative post-event record was captured in this slice, the candidate remains `STATUS_UNCONFIRMED`. It does not claim that the meeting occurred, who attended, what was submitted, or whether a recommendation or decision followed.

## Groundwater action-plan index candidate

`examples/briefing_integration/gmd_action_plan_inventory_2026_07_29.json` records a versioned observation of the Kansas Department of Agriculture index:

- GMD Nos. 2, 3, and 5 have action-plan links on the index;
- GMD No. 1 has a priority-area link but no action-plan link on the index;
- GMD No. 4 priority areas are listed as due January 1, 2028; and
- review, approval, implementation, supersession, and outcome state remain unresolved.

Link presence is not submission acceptance or approval. A missing link is not non-submission. District geometry and priority-area geometry remain separate unresolved references.

## CI integration

### `briefing-integration`

The workflow is read-only and:

1. validates the `BriefingSignal` schema and fixtures;
2. validates the Hays and GMD examples;
3. runs the existing water-planning anti-collapse tests; and
4. emits only GitHub job results and summaries.

It creates no source snapshot, evidence record, issue, receipt, proof, release, deployment, or publication.

### `infra-compose-smoke`

The workflow:

1. runs no-network static path and loopback-exposure checks;
2. runs `docker compose config --quiet`;
3. builds the two placeholder images; and
4. does not start containers or test application runtime.

A green build proves only that the checked-in Compose context and Dockerfiles can render and build on the hosted runner. The Dockerfiles remain placeholders without application copies, commands, health checks, or runtime proof.

## Failure posture

| Condition | Outcome |
|---|---|
| Confirmed claim lacks evidence | Reject signal. |
| Public or consequential permission is true | Reject signal. |
| Candidate payload embeds inline geometry | Reject signal. |
| Meeting occurrence is unsupported | Keep `STATUS_UNCONFIRMED`. |
| Official index lacks a plan link | Record link absence; do not infer non-submission. |
| Source cannot be snapshotted | Keep `SNAPSHOT_PENDING` or `UNAVAILABLE`. |
| Existing issue already owns the work | Update that issue; do not open a duplicate. |
| Compose render or build fails | Block the infrastructure smoke check; do not claim runtime failure beyond the bounded build surface. |

## Next implementation stages

1. Add immutable source-snapshot and evidence-reference adapters.
2. Add deduplication against GitHub issues and existing KFM object identities.
3. Define `TemporalAuthorityEnvelope` for volatile advisories, conditions, governance events, and projects.
4. Add governed source admission for KWO and KDA products.
5. Add separate venue, planning-region, district, and priority-area geometry references.
6. Add correction, supersession, withdrawal, and freshness jobs.
7. Add public products only after evidence, policy, review, release, and rollback close.

## Non-goals of this slice

- no live web connector;
- no scheduler;
- no issue-writing automation;
- no repository self-authorization;
- no meeting attendance, public-comment, plan-approval, or project-outcome inference;
- no container startup;
- no API or UI route;
- no source activation;
- no proof construction;
- no release, deployment, or publication.

## Rollback

Before merge, close the draft and abandon the branch. After merge, revert the scoped integration commit through review. A documentation or workflow revert does not erase external events, source documents, or prior unresolved claims.

[Back to top](#top)
