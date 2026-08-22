<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/ui/map-context-envelope
title: MapContextEnvelope Semantic Contract
type: semantic-contract; ui; map-runtime; renderer-neutral; fixture-first
version: v0.2.0
status: proposed; inactive; no-network; no-authority
owners: OWNER_TBD — UI steward · Map steward · Evidence steward · Runtime steward · Release steward · Validation steward
created: 2026-08-06
updated: 2026-08-22
policy_label: public; ui; map-context; renderer-neutral; released-input-only; permalink-deny-by-default
related:
  - ./README.md
  - ./map_context_envelope/README.md
  - ../../schemas/contracts/v1/ui/map_context_envelope.schema.json
  - ../../fixtures/ui/map_context_envelope/
  - ../../tools/validators/ui/validate_map_context_envelope.py
  - ../../tests/validators/test_validate_map_context_envelope.py
  - ../../docs/focus-mode/state/map-context-state.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, ui, map, context, envelope, renderer-neutral, released-only, evidence]
[/KFM_META_BLOCK_V2] -->

# `MapContextEnvelope`

> An immutable, renderer-neutral request-context projection that carries released layer identity, selected feature identity, time and area scope, evidence references, and bounded filters from the map shell to governed API, Evidence Drawer, or Focus Mode admission. It is context, not evidence, policy, review, release, an answer, or publication authority.

## Purpose

The map shell may report what the user is viewing and selecting. It must not pass MapLibre implementation objects, rendered feature blobs, style JSON, or direct canonical-store values across the trust membrane. `MapContextEnvelope` provides the anti-corruption boundary: a small published-language object whose semantics do not depend on `queryRenderedFeatures`, `source-layer`, paint/layout properties, feature-state, or a particular renderer.

## Required semantics

1. Every layer is explicitly `PUBLISHED` and carries a release reference and layer spec hash.
2. Every selected feature names one admitted layer and at least one evidence reference.
3. Top-level `release_refs` exactly equal the canonical union of layer release references.
4. Top-level `evidence_refs` exactly equal the canonical union of layer and selection evidence references.
5. Layers, selections, filters, and reference arrays are canonical and deterministic.
6. `assembled_at < expires_at`, with a maximum 15-minute context lifetime.
7. The requested time window is ordered; viewport bounds are ordered and geographic.
8. Filters are renderer-neutral declarations with finite operators and valid arity.
9. References to RAW, WORK, QUARANTINE, canonical/internal stores, direct model output, or proof stores are denied.
10. `permalink_policy` is fixed to `DISABLED` / `DENY`; raw-envelope serialization, exact-location state, and restricted-context state are all explicitly forbidden until a separately reviewed projection contract and serializer exist.
11. `spec_hash` is RFC 8785 JCS + SHA-256 over the envelope without `envelope_id` and `spec_hash`; `envelope_id` uses the first 24 digest hex.

## Authority and non-effects

The envelope records request context only. It does not resolve EvidenceRefs, evaluate policy, establish release state, authorize public use, create citations, return an answer, create a shareable URL, or mutate repository/canonical state. Downstream services must independently resolve current EvidenceBundles, policy, review, release, correction, and rollback state.

## Renderer-neutral boundary

The contract admits stable KFM identifiers and bounded filter declarations. It rejects renderer-specific members such as `sourceLayer`, `queryRenderedFeatures`, `paint`, `layout`, `featureState`, style expressions, camera objects, or raw feature-property payloads. The same envelope can be produced by MapLibre, a test harness, or a future admitted renderer without changing evidence semantics.

## Permalink safety boundary

`permalink_policy` is a fail-closed declaration, not a URL-state codec or a redacted permalink payload. Under this inactive v1 profile it must contain exactly this posture:

- `mode: DISABLED`;
- `outcome: DENY`;
- `reason_codes: [PERMALINK_SERIALIZER_NOT_ADMITTED]`;
- `raw_envelope_serialization: false`;
- `exact_location_state_allowed: false`; and
- `restricted_context_allowed: false`.

Callers must not serialize the raw envelope into a URL, hash, browser history entry, QR code, export, or other outward carrier. A future redacted share-state projection requires a versioned semantic contract and schema, policy and sensitivity review, deterministic positive and negative fixtures, a bounded serializer, consumer migration, correction behavior, and rollback proof. This fixed denial closes the current field-level ambiguity without implying that permalink behavior exists.

## Placement

| Responsibility | Home |
|---|---|
| Semantic meaning | `contracts/ui/map_context_envelope.md` |
| Machine shape | `schemas/contracts/v1/ui/map_context_envelope.schema.json` |
| Synthetic examples | `fixtures/ui/map_context_envelope/` |
| Deterministic validation | `tools/validators/ui/validate_map_context_envelope.py` |
| Tests | `tests/validators/` |
| Read-only CI | `.github/workflows/` |
| AI authoring provenance | `data/receipts/generated/` |

This hardens the already-present UI scaffold at its existing schema path and creates no parallel UI, map, evidence, runtime, policy, or release authority.

## Rollback

Before merge, close the draft pull request and delete its branch. After an authorized merge, revert the bounded packet. No app route, renderer, source, lifecycle data, release, cache, or public artifact is changed.
