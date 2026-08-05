<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/domains/settlements-infrastructure/place-name-authority-graph
title: PlaceNameAuthorityGraphPacket Contract
type: semantic-contract; settlements-infrastructure; place-name; temporal-alias; source-role
version: v0.1.0
status: draft; PROPOSED; fixture-first; non-authoritative
owners: OWNER_TBD — Settlements/Infrastructure steward · Contracts steward · Evidence steward · Review steward
created: 2026-08-05
updated: 2026-08-05
policy_label: public; contracts; place-name; temporal; source-role; non-authoritative
related:
  - ./README.md
  - ./place-identity.md
  - ../../../schemas/contracts/v1/domains/settlements-infrastructure/place_name_authority_graph.schema.json
  - ../../../fixtures/contracts/v1/domains/settlements-infrastructure/place_name_authority_graph/
  - ../../../tools/validators/validate_place_name_authority_graph.py
  - ../../../tests/validators/test_validate_place_name_authority_graph.py
  - ../../../docs/intake/exploratory/new-ideas-4-25-source-map.md
  - ../../../docs/kfm_full_atlas_seed_cards.md
notes:
  - "Implements the bounded KFM-TRIAD-061 gap."
  - "Names remain assertions; they do not become feature identity, geometry, legal status, jurisdiction, or ownership authority."
[/KFM_META_BLOCK_V2] -->

# `PlaceNameAuthorityGraphPacket`

> A fixture-first, reversible record for time-bounded and source-role-bound place-name assertions, alias relations, feature bindings, and authority decisions.

## Purpose

A place name can be official for one purpose, historical for another period, translated in one language, used by a community, disputed, superseded, or intentionally withheld. None of those name assertions proves that the named feature exists now, identifies its geometry, establishes legal status, determines ownership, or authorizes publication.

This contract keeps four object families distinct:

- `PlaceNameAssertion` preserves one source-native name treatment.
- `TemporalAliasEdge` records a typed relation between assertions.
- `FeatureNameBinding` links an assertion to a feature candidate without absorbing feature identity.
- `NameAuthorityDecision` records a reversible, finite working decision for a declared profile and use.

## Directory Rules basis

The primary responsibility is Settlements/Infrastructure semantic meaning, so the contract lives in the existing `contracts/domains/settlements-infrastructure/` lane. Machine shape, synthetic fixtures, executable validation, tests, workflow orchestration, and authoring provenance remain in their established responsibility roots. No new repository root, source registry, policy authority, feature store, graph store, release family, or public route is created.

## Source-role and time separation

Every assertion records a source role and source-native identifier. Supported roles are:

- `NAMING_AUTHORITY`
- `HISTORICAL_RECORD`
- `COMMUNITY_USAGE`
- `TRANSLATION_AUTHORITY`
- `CONTEXT`

A naming authority may support a name assertion. It does not automatically support feature existence, geometry, legal status, jurisdiction, ownership, title, public access, or present-day use.

`valid_from` and `valid_to` describe the period for which the assertion or binding is claimed to apply. `issued_at` records when the source treatment was issued or recorded. `provenance.recorded_at` records when this packet was produced. These axes must not be silently collapsed.

## Alias relations

The packet supports explicit relations:

| Relation | Meaning |
|---|---|
| `VARIANT_OF` | Alternative spelling or form. |
| `FORMER_NAME_OF` | Earlier name for the later assertion. |
| `TRANSLATION_OF` | Language translation without identity collapse. |
| `COMMUNITY_NAME_FOR` | Community-context name for a feature candidate. |
| `DISPUTES` | Competing or contested name treatment. |
| `SUPERSEDES` | Later authority treatment replaces an earlier treatment for a declared use. |
| `SAME_FEATURE_NAME` | Assertions are believed to name the same feature candidate. |
| `UNRESOLVED` | Relationship is not sufficiently resolved. |

Every edge is reversible process history. Active directional alias/supersession edges must be acyclic.

## Finite decisions

| Outcome | Meaning |
|---|---|
| `ACCEPT_FOR_USE` | Accepted only for the declared profile, version, evidence, source role, and time scope. |
| `PROVISIONAL` | May be used as a bounded candidate while uncertainty remains visible. |
| `HOLD` | Review is required before any higher-authority use. |
| `ABSTAIN` | Support is insufficient for the requested decision. |
| `REJECT` | The proposed binding or use is not accepted. |

`ACCEPT_FOR_USE` is not a universal naming decision and cannot cover an unbound or unresolved assertion. Homonyms, disputes, and sensitive names require explicit review rather than automatic resolution.

## Sensitive and disputed names

A name may be marked `WITHHELD` or `REVIEW_ONLY`. The packet stores only the supplied synthetic fixture text; a real implementation must apply rights, sovereignty, cultural sensitivity, living-person, archaeology, infrastructure, and location-exposure policy before a name reaches a public search surface.

A `DISPUTES` edge must remain visible in the packet and must be paired with a non-final decision that records `DISPUTED_NAME_PRESERVED`. The validator rejects winner-takes-all deletion of disputed source assertions.

## Deterministic fixture hash

`kfm-fixture-json-v1` removes top-level `spec_hash`, serializes sorted-key UTF-8 JSON with compact separators, preserves array order, and computes SHA-256. This is a local replay profile, not a repository-wide canonicalization decision.

## Validation boundary

The validator checks bounded JSON safety, schema shape, deterministic hash replay, canonical ordering, reference closure, time order, acyclic alias history, unbound/bound consistency, homonym review, dispute preservation, finite decisions, and explicit non-authority declarations.

A green result does not:

- prove a place exists or identify its canonical geometry;
- establish legal municipal, census, jurisdictional, title, ownership, or access status;
- admit or activate a source;
- resolve `EvidenceRef` to `EvidenceBundle`;
- evaluate rights, sensitivity, sovereignty, policy, reviewer authority, or release state;
- authorize search indexing, lifecycle promotion, release, deployment, publication, or public use.

## Correction and rollback

This slice is additive. Before merge, close the draft pull request and abandon its branch. After an authorized merge, revert the dependency-closed contract/schema/fixture/validator/test/workflow/receipt change. If downstream records later depend on stable assertion, edge, binding, or decision IDs, correct or supersede them rather than erasing relied-on history.
