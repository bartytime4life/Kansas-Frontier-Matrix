# FrontierRouteTrustStatus

**Status:** PROPOSED contract for a fixture-first, no-network Roads/Rail/Trade trust projection.  
**Owning responsibility:** `contracts/` defines meaning; the canonical machine shape is in `schemas/contracts/v1/domains/roads-rail-trade/`.  
**Source basis:** the supplied *New Ideas 3-31-26* packet proposes a small trust overlay keyed by `kfm_id`, with `publish`, `quarantine`, and `deny` dispositions plus a public-catalog visibility flag.

## Purpose

`FrontierRouteTrustStatus` carries the already-decided trust posture of historical-route and route-linked waypoint features to a governed map or steward-review surface. It lets a renderer resolve a feature id to a bounded overlay without recomputing policy in the browser.

The object is a **projection**, not a policy decision, EvidenceBundle, release manifest, proof, source record, route dataset, or publication event.

```text
PolicyDecision + EvidenceRef/EvidenceBundle + release state
  -> FrontierRouteTrustStatus projection
  -> audience admission
  -> minimal TrustOverlay keyed by kfm_id
  -> MapLibre styling / feature inspection
```

## Authority and audience boundary

Two audiences are explicit:

- `public`: the payload may contain only released `publish` entries. It must not contain withheld feature ids, denial reasons, quarantine reasons, or steward-only metadata.
- `steward`: the payload may contain `publish`, `quarantine`, and `deny` entries for authorized review surfaces.

A public client must never receive a `steward` payload and rely on client-side filtering to hide it. The TypeScript adapter fails closed when a caller attempts that boundary crossing.

## Required fields

### Collection

| Field | Meaning |
|---|---|
| `profile` | Fixed contract profile for deterministic dispatch. |
| `collection_id` | Stable governed collection identity. |
| `generated_at` | Time the projection was assembled. |
| `audience` | `public` or `steward`. |
| `collection_decision` | Aggregate disposition derived from the feature decisions. |
| `features` | Non-empty, deterministically ordered feature trust rows. |

### Feature trust row

| Field | Meaning |
|---|---|
| `kfm_id` | Stable feature identity used to join map features and trust state. |
| `name` | Bounded display label; not an authority field. |
| `decision` | `publish`, `quarantine`, or `deny`, copied from upstream governed disposition. |
| `code` | Stable reason code suitable for the admitted audience. |
| `detail` | Bounded, audience-safe explanation; it must not leak protected facts. |
| `source_uri` | HTTPS source locator used for review context. |
| `policy_decision_ref` | Reference to the upstream policy decision. |
| `evidence_refs` | One or more evidence references; the projection does not resolve them. |
| `release_id` | Required for `publish`; `null` for `quarantine` and `deny`. |
| `visible_in_public_catalog` | `true` only for `publish`. |

## Invariants

1. `kfm_id` values are unique within the payload.
2. `visible_in_public_catalog` is true if and only if `decision` is `publish`.
3. `publish` requires a non-null `release_id`; non-publish decisions require `release_id: null`.
4. `collection_decision` is derived deterministically:
   - all publish -> `publish`;
   - all deny -> `deny`;
   - any deny in a mixed set -> `deny-partial`;
   - otherwise any quarantine -> `quarantine-partial`.
5. A `public` payload contains only publishable entries and has `collection_decision: publish`.
6. Unknown or missing trust status fails closed: it is not visible in public mode and does not receive a trusted style.
7. Geometry, raw source bytes, canonical records, private policy rationale, credentials, review identities, and model output are excluded.

## Finite validation outcomes

The validator emits deterministic findings and exits non-zero for malformed or unsafe payloads. Representative codes include:

- `SCHEMA_INVALID`
- `DUPLICATE_FEATURE_ID`
- `VISIBILITY_DECISION_MISMATCH`
- `RELEASE_BINDING_MISMATCH`
- `COLLECTION_DECISION_MISMATCH`
- `PUBLIC_PROJECTION_LEAK`

A validator pass proves only conformance to this projection contract. It does not establish source truth, policy approval, rights clearance, evidence closure, review authority, release, promotion, deployment, or publication.

## Directory Rules basis

This packet uses existing responsibility roots and the accepted schema-home ADR:

- semantics: `contracts/domains/roads-rail-trade/`;
- machine shape: `schemas/contracts/v1/domains/roads-rail-trade/`;
- fixtures: `fixtures/domains/roads-rail-trade/`;
- validator: `tools/validators/domains/roads-rail-trade/`;
- tests: `tests/validators/` and `apps/explorer-web/tests/`;
- UI adapter: `apps/explorer-web/src/features/domains/roads_rail_trade/`.

No new root, parallel policy home, release home, catalog home, or proof home is created.

## Rollback

Rollback is one commit: remove this contract, schema, fixtures, validator, focused tests, and workflow, then restore the previous `layers.ts` placeholder. No data migration, release withdrawal, or public cache invalidation is required because this slice creates no released artifact and performs no publication.
