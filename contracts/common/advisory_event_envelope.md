<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/common/advisory-event-envelope
title: AdvisoryEventEnvelope Contract
type: semantic-contract; shared-volatile-event-envelope
version: v0.1.0
status: proposed; fixture-first; no-network; release-neutral
owners: OWNER_TBD — Contract steward · Temporal steward · Hazards steward · Source/evidence/policy/release stewards · Validation steward
created: 2026-08-06
updated: 2026-08-06
policy_label: public; common; advisory; volatile-event; no-alert-authority; no-public-authority
related:
  - ./temporal_authority_envelope.md
  - ../../docs/architecture/briefing-integration.md
  - ../../schemas/contracts/v1/common/advisory_event_envelope.schema.json
  - ../../schemas/contracts/v1/domains/hazards/kdhe_hab_advisory_snapshot.schema.json
  - ../../fixtures/contracts/v1/common/advisory_event_envelope/
  - ../../tools/validators/validate_advisory_event_envelope.py
  - ../../tools/validators/advisory_event_envelope_support.py
  - ../../tests/validators/test_validate_advisory_event_envelope.py
tags: [kfm, common, advisory-event, volatile-status, false-clear, identity-conflict, zone-scope, release-neutral]
notes:
  - "Mined from the Briefing-to-System Integration Architecture Lane B recommendation."
  - "The first profile binds existing KDHE HAB snapshot fixtures; it does not activate KDHE or create a generic replacement for domain contracts."
  - "The envelope creates no alert, policy, review, lifecycle, release, deployment, publication, or public-use authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# AdvisoryEventEnvelope

> `AdvisoryEventEnvelope` supplies shared identity, time, status, scope, lineage,
> false-clear, and release-neutral mechanics around one domain-native volatile
> advisory record. The referenced domain payload remains authoritative for its
> native vocabulary and meaning.

## Status and Directory Rules basis

| Field | Value |
|---|---|
| Status | `PROPOSED` / fixture-first / no-network |
| Semantic owner | `contracts/common/` because heat, HAB, drinking-water, road, and smoke advisories share volatile-event mechanics while retaining separate domain payloads |
| Machine shape | `schemas/contracts/v1/common/advisory_event_envelope.schema.json` |
| First domain profile | Existing `KdheHabAdvisorySnapshot` fixtures under the hazards lane |
| Public use | Fixed false |
| Alert authority | Fixed false |
| Release state | Neutral; any release reference fails validation |

Accepted Directory Rules v2 place shared semantic meaning under `contracts/`,
machine shape under `schemas/`, fixtures under `fixtures/`, enforcement under
`tools/validators/`, and executable proof under `tests/`. This slice adds no
root and no parallel domain authority.

## Purpose

Volatile advisories recur across multiple domains, but they share hard problems:

- source issue, onset, expiry, cancellation, rescission, retrieval, correction,
  and supersession times must remain distinct;
- source-native status must not be flattened into an unsupported clear state;
- a failed or stale source check must never become “no advisory”;
- a zoned advisory must not become a whole-area advisory;
- unresolved identity must not leak guessed geometry;
- forecast, observation, model, regulatory advisory, and synthetic support must
  remain distinct; and
- no wrapper may become alert or publication authority.

The shared envelope handles only those mechanics. It does not define heat,
water-quality, drinking-water, transportation, smoke, or other domain meaning.

## Shape

```text
AdvisoryEventEnvelope
├── temporal_authority      # TemporalAuthorityEnvelope
├── event
│   ├── event_id            # deterministic wrapper identity
│   ├── profile_id
│   ├── event_family
│   ├── native_event_type
│   └── native_event_id
├── source_surface
│   ├── semantics           # complete_snapshot | incremental_feed | single_event | unknown
│   ├── snapshot_complete
│   ├── retrieval_status
│   ├── parse_status
│   ├── freshness_status
│   ├── checked_at
│   └── freshness_budget_hours
├── advisory
│   ├── native_status
│   ├── normalized_status
│   ├── last_confirmed_status
│   ├── severity / certainty / urgency
│   ├── basis
│   └── onset / expiry / cancellation / rescission times
├── scope
│   ├── affected_area_ref
│   ├── geometry_role
│   ├── geometry_confidence
│   └── zone_scope
├── domain_payload
│   ├── payload_type
│   ├── payload_ref
│   ├── payload_schema_id
│   ├── payload_record_digest
│   └── payload_source_content_digest
└── controls
    ├── rescission_ref
    ├── public_guidance_ref
    ├── release_neutral = true
    ├── public_use_allowed = false
    └── alerts_allowed = false
```

## First profile: KDHE HAB snapshot binding

The first profile is deliberately narrow:

```text
profile_id = kfm.advisory-event.hab.v1
event_family = harmful_algal_bloom
payload_type = KdheHabAdvisorySnapshot
source_descriptor_ref = src:ks-kdhe-hab
basis = regulatory_advisory
```

It validates a repository-local reference to an existing, schema-valid KDHE HAB
fixture and recomputes a canonical JSON digest of the payload. It also requires
the wrapper’s source-content digest to equal the payload’s declared
`content_digest`.

The deterministic event identity is SHA-256 over:

```json
{
  "profile_id": "...",
  "native_event_id": "...",
  "payload_record_digest": "sha256:...",
  "revision_id": "..."
}
```

## Finite status mapping

| KDHE HAB payload state | Envelope status |
|---|---|
| `WATCH`, `WARNING`, `HAZARD` | `ACTIVE_CONFIRMED` |
| `LIFTED` | `RESCINDED` |
| `SOURCE_UNAVAILABLE` | `STATUS_CHECK_FAILED` |
| `STALE_SOURCE` | `STATUS_UNCONFIRMED` |
| `IDENTITY_UNRESOLVED` | `IDENTITY_CONFLICT` |
| `GEOMETRY_UNRESOLVED` | `GEOMETRY_UNRESOLVED` |
| `QUARANTINED` | `STATUS_UNCONFIRMED` |

A mapping is routing metadata only. It does not create public truth or authorize
an alert.

## Fail-closed invariants

- Failed retrieval never clears an advisory.
- Stale source state never remains `ACTIVE_CONFIRMED`.
- `RESCINDED` requires a rescission time, rescission reference, and prior
  lineage.
- A zone payload remains a zone; it cannot be promoted to the whole water body.
- Identity conflict and unresolved geometry require a null public area
  reference and unresolved geometry posture.
- HAB support remains `regulatory_advisory`; forecast/model/observation labels
  fail as `SOURCE_ROLE_COLLAPSE`.
- The wrapper, TemporalAuthorityEnvelope, and domain payload identities,
  retrieval times, scope, geometry, and content digests must agree.
- Release references, public-use permission, or alert permission fail closed.

## Deterministic findings

The validator emits stable findings including:

`ISSUING_AUTHORITY_MISSING`, `STATUS_CHECK_FAILED_REQUIRED`,
`FALSE_CLEAR_ATTEMPT`, `SOURCE_STALE`, `RESCISSION_REQUIRED`,
`STATUS_UNCONFIRMED`, `IDENTITY_CONFLICT`, `AFFECTED_AREA_UNRESOLVED`,
`ZONE_SCOPE_COLLAPSE`, `SOURCE_ROLE_COLLAPSE`,
`TEMPORAL_ORDER_INVALID`, `PAYLOAD_RECORD_DIGEST_MISMATCH`,
`PAYLOAD_SOURCE_DIGEST_MISMATCH`, and `EVENT_ID_MISMATCH`.

## Validation

```bash
python -m unittest   tests.validators.test_validate_advisory_event_envelope -v

python tools/validators/validate_advisory_event_envelope.py --fixtures
```

A passing result proves only the bounded fixture checks implemented by this
profile. It does not fetch KDHE, establish current advisory status, authenticate
evidence, evaluate policy, issue public guidance, create an alert, mutate
lifecycle state, release, deploy, publish, or permit public use.

## Compatibility and rollback

The profile is additive and release-neutral. A future heat, drinking-water,
road, or smoke profile should extend the shared mechanics without adding its
native fields to the common schema. Before merge, rollback is closing the draft
pull request. After merge, rollback is an ordinary reviewed revert; no external
source, alert, lifecycle record, release, deployment, or public artifact
requires cleanup.

[Back to top](#top)
