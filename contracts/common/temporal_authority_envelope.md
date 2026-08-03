<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/common/temporal-authority-envelope
title: TemporalAuthorityEnvelope Contract
type: semantic-contract; shared-metadata-envelope
version: v0.1.0
status: proposed; fixture-first; no-network; non-authoritative
owners: OWNER_TBD — Contract steward · Temporal steward · Source steward · Geometry steward · Governance steward · Validation steward
created: 2026-08-03
updated: 2026-08-03
policy_label: public; common; temporal; authority; lineage; no-public-authority
related:
  - ./README.md
  - ./temporal_window.md
  - ../../docs/architecture/briefing-integration.md
  - ../../docs/adr/ADR-0014-temporal-vocabulary--six-time-kinds-tracked.md
  - ../../schemas/contracts/v1/common/temporal_authority_envelope.schema.json
  - ../../fixtures/contracts/v1/common/temporal_authority_envelope/
  - ../../tools/validators/validate_temporal_authority_envelope.py
  - ../../tests/validators/test_validate_temporal_authority_envelope.py
tags: [kfm, common, temporal-authority-envelope, source-role, geometry-role, correction, supersession, shared-kernel]
notes:
  - "This is the bounded no-network profile proposed by the Briefing-to-System Integration Architecture."
  - "It wraps domain-native objects with shared metadata; it does not replace SourceDescriptor, advisory, observation, forecast, program, project, or governance-event contracts."
  - "It does not accept ADR-0014, replace TemporalWindow, or settle the repository's unresolved global temporal vocabulary."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# TemporalAuthorityEnvelope

> `TemporalAuthorityEnvelope` is a shared metadata envelope for a changing object whose identity, source-descriptor role binding, authority, time, geography, state, lineage, and governance references must remain inspectable. The domain payload stays in its owning contract.

## Status and boundary

| Field | Value |
|---|---|
| Status | `PROPOSED` / fixture-first / no-network |
| Contract home | `contracts/common/temporal_authority_envelope.md` |
| Machine shape | `schemas/contracts/v1/common/temporal_authority_envelope.schema.json` |
| Authority | Shared metadata meaning only |
| Public use | Always false in this profile |
| Domain payload | Out of scope; remains in the owning domain contract |
| Temporal-vocabulary decision | Not made by this contract |

This profile operationalizes the briefing-integration proposal without silently resolving the existing temporal vocabulary conflict. In particular, it does **not**:

- accept or supersede ADR-0014;
- redefine `TemporalWindow`;
- claim that `issued_at`, `effective_at`, `valid_from`, `valid_to`, `observed_at`, `retrieved_at`, `corrected_at`, and `superseded_at` are KFM's universal time vocabulary;
- infer source truth, policy approval, review completion, release, or publication;
- embed a domain payload or generic replacement for domain contracts.

## Why this is a common contract

The envelope is shared across volatile advisories, observations, forecasts, governance events, grants, projects, and other time-changing objects. No single domain owns those cross-cutting identity, authority, temporal, geometry, lineage, and governance-reference concerns. `contracts/common/` therefore owns the shared meaning, while each domain continues to own its native object and state machine.

## Shape

```text
TemporalAuthorityEnvelope
├── identity
│   ├── object_id
│   ├── object_type
│   ├── native_id
│   └── revision_id
├── source
│   ├── source_descriptor_ref
│   ├── source_role_ref
│   ├── issuing_authority_ref
│   └── authority_scope
├── time
│   ├── issued_at
│   ├── effective_at
│   ├── valid_from
│   ├── valid_to
│   ├── observed_at
│   ├── retrieved_at
│   ├── corrected_at
│   └── superseded_at
├── space
│   ├── native_geography_text
│   ├── geography_ref
│   ├── geometry_role
│   └── geometry_confidence
├── state
│   ├── native_state
│   ├── normalized_state
│   └── certainty
├── lineage
│   ├── supersedes
│   ├── superseded_by
│   ├── correction_refs
│   └── withdrawal_refs
└── governance
    ├── evidence_refs
    ├── policy_refs
    ├── review_refs
    ├── release_ref
    └── public_use_allowed = false
```

## Field semantics

### Identity

| Field | Meaning |
|---|---|
| `object_id` | Stable identity of the domain object across revisions. |
| `object_type` | Domain-native object family, such as `ObservationRecord` or `GovernanceEvent`. |
| `native_id` | Source-native identifier when one exists; otherwise `null`. |
| `revision_id` | Identity of the exact revision represented by this envelope. It must not equal `object_id`. |

### Source and authority

`source_descriptor_ref` identifies the governed SourceDescriptor whose admission record owns source role, rights, sensitivity, cadence, and access posture. `source_role_ref` must equal that descriptor reference plus `#/source_role`. This keeps the envelope bound to the repository's existing SourceDescriptor vocabulary instead of creating a second source-role enum or silently crosswalking the older seven-role doctrine into the current schema.

The validator proves only the lexical binding between those two references. It does not resolve the SourceDescriptor, authenticate the referenced role, or establish source admission. `issuing_authority_ref` names the issuing or observing authority for the represented source statement; it is not KFM release authority. `authority_scope` describes the bounded authority claim, not a general endorsement.

### Time

| Field | Meaning | Misuse to reject |
|---|---|---|
| `issued_at` | When an authority issued the source statement or product. | Treating it as observation or validity time. |
| `effective_at` | When a rule, advisory, decision, award, or status takes effect. | Assuming it equals issue or retrieval time. |
| `valid_from` / `valid_to` | Interval represented by the domain object. | Replacing an interval with one generic timestamp. |
| `observed_at` | When an instrument or observer measured the condition. | Using retrieval time as observation time. |
| `retrieved_at` | When KFM captured the represented source state. | Treating capture time as source or release time. |
| `corrected_at` | When a source or governed correction was recorded. | Overwriting the earlier revision. |
| `superseded_at` | When a later revision became preferred for current-state use. | Deleting the superseded revision. |

The profile permits future `effective_at` and validity intervals. Source issue, observation, correction, and supersession times must not occur after the capture represented by `retrieved_at`.

### Space

`native_geography_text` preserves source-native place wording. `geography_ref` points to a governed geography or geometry object when resolved. The role and confidence fields say what the geometry represents and how strongly it is supported; they are separate from source certainty or event severity.

When `geography_ref` is unresolved, geometry role and confidence must remain `unresolved` or `not_applicable`. The envelope cannot use a centroid, county polygon, station point, or venue point as a substitute for a different geographic object.

### State and certainty

`native_state` preserves the source vocabulary. `normalized_state` supports cross-source routing without erasing the native term. `certainty` is one of `confirmed`, `probable`, `uncertain`, `unknown`, or `conflicted`.

A `confirmed` envelope requires at least one evidence reference. This proves only that support was declared and shape-valid; the envelope does not resolve or authenticate the referenced evidence.

### Lineage and governance

Correction and supersession are append-only relationships. A correction timestamp requires a correction reference. A supersession timestamp requires a `superseded_by` reference. Self-lineage and contradictory forward/backward lineage are invalid.

`policy_refs`, `review_refs`, and `release_ref` are references only. Their presence does not prove the referenced decision is valid, current, applicable, or sufficient. `public_use_allowed` is fixed to false so this first profile cannot become a public release shortcut.

## Invariants

- Every envelope has stable object and exact-revision identity.
- At least one non-retrieval time assertion is present.
- Every non-null date-time includes an explicit timezone offset.
- A validity interval is either fully present or fully absent.
- `valid_from` must not be later than `valid_to`.
- Source-role meaning remains owned by the referenced SourceDescriptor and owning domain contract; this shared profile does not re-declare or reinterpret it.
- Source issue, observation, correction, and supersession times cannot be later than `retrieved_at`.
- Corrections and supersessions preserve prior records and carry references.
- SourceDescriptor role binding, geometry role, certainty, and public-use posture remain distinct.
- A valid envelope is not evidence truth, source admission, policy approval, review approval, release, publication, or a domain object by itself.

## Valid example

```json
{
  "schema_version": "1.0.0",
  "identity": {
    "object_id": "kfm:condition:synthetic-station-001",
    "object_type": "ObservationRecord",
    "native_id": "station:synthetic-001",
    "revision_id": "kfm:revision:synthetic-station-001:20260803T120500Z"
  },
  "source": {
    "source_descriptor_ref": "src:synthetic:station-feed",
    "source_role_ref": "src:synthetic:station-feed#/source_role",
    "issuing_authority_ref": "authority:synthetic:station-operator",
    "authority_scope": "Synthetic station observation fixture only"
  },
  "time": {
    "issued_at": null,
    "effective_at": null,
    "valid_from": null,
    "valid_to": null,
    "observed_at": "2026-08-03T12:00:00Z",
    "retrieved_at": "2026-08-03T12:05:00Z",
    "corrected_at": null,
    "superseded_at": null
  },
  "space": {
    "native_geography_text": "Synthetic station",
    "geography_ref": "kfm:geometry:synthetic-station-001",
    "geometry_role": "authoritative",
    "geometry_confidence": "confirmed"
  },
  "state": {
    "native_state": "reported",
    "normalized_state": "observed",
    "certainty": "confirmed"
  },
  "lineage": {
    "supersedes": [],
    "superseded_by": [],
    "correction_refs": [],
    "withdrawal_refs": []
  },
  "governance": {
    "evidence_refs": ["evidence:synthetic:station-sample"],
    "policy_refs": [],
    "review_refs": [],
    "release_ref": null,
    "public_use_allowed": false
  }
}
```

## Validation

The no-network validator checks:

- closed JSON Schema shape, aware date-time syntax, and formats;
- duplicate-key, non-finite-number, depth, size, symlink, and non-regular-file safety;
- exact SourceDescriptor-to-role-reference binding;
- validity-interval ordering;
- source-time versus retrieval-time ordering;
- correction and supersession ordering;
- object/revision identity separation;
- self-lineage and contradictory lineage directions;
- deterministic bounded diagnostics; and
- positive and exact-negative fixture polarity.

A passing validator result does not fetch a source, resolve evidence, evaluate policy, validate domain state, approve a correction, or authorize public use.

## Compatibility, correction, and rollback

This is a new `PROPOSED` profile. Changes to field names, source-reference binding, time roles, or lineage semantics are compatibility-significant. Before merge, rollback is closing the draft PR and abandoning the branch. After merge, rollback is a reviewed revert or corrective PR that preserves any identifiers already consumed by downstream fixtures or contracts.

[Back to top](#top)
