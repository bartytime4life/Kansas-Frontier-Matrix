<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/runtime/place-name-search-projection
title: PlaceNameSearchProjection Contract
type: semantic-contract; runtime; place-name-search; temporal; public-safe-candidate
version: v0.1.0
status: draft; PROPOSED; fixture-first; internal-projection-only
owners: OWNER_TBD — Runtime steward · Settlements/Infrastructure steward · Evidence steward · Policy steward · Contracts steward
created: 2026-08-05
updated: 2026-08-05
policy_label: public; contracts; runtime; place-name-search; non-authoritative
related:
  - ./README.md
  - ../domains/settlements-infrastructure/place_name_authority_graph.md
  - ../../schemas/contracts/v1/runtime/place_name_search_projection.schema.json
  - ../../fixtures/contracts/v1/runtime/place_name_search_projection/
  - ../../tools/validators/validate_place_name_search_projection.py
  - ../../tests/validators/test_validate_place_name_search_projection.py
  - ../../docs/intake/exploratory/new-ideas-4-25-source-map.md
notes:
  - "Implements the search/projection continuation of KFM-TRIAD-061."
  - "This packet is an internal candidate projection. It does not authorize a public search endpoint."
[/KFM_META_BLOCK_V2] -->

# `PlaceNameSearchProjection`

> A deterministic internal projection that turns a validated place-name authority graph into finite, time-aware, source-role-visible search outcomes without creating feature, geometry, legal-status, ownership, policy, release, or public-search authority.

## Purpose

The place-name authority graph preserves official, historical, translated, community, disputed, sensitive, and unbound name assertions. A search surface must not flatten those distinctions into one opaque string match. This contract defines the smallest downstream projection that can expose why a candidate matched, which period it covers, which source role supports it, what ambiguity remains, and why the resolver answered, abstained, denied, or errored.

The projection is deliberately **internal and review-only**. It is not an API route, search index, UI component, policy decision, or release object.

## Directory Rules basis

The primary responsibility is runtime-facing object meaning, so semantic prose belongs under `contracts/runtime/`. The paired shape uses `schemas/contracts/v1/runtime/`; synthetic cases, validator, tests, workflow, and authoring receipt remain in their established responsibility roots. The domain authority graph remains owned by `contracts/domains/settlements-infrastructure/`; this projection consumes it by reference and digest rather than duplicating its authority.

No new repository root, search index, API route, policy home, source registry, evidence store, release family, or public surface is created.

## Inputs

A projection binds:

- the exact `PlaceNameAuthorityGraphPacket` reference and digest;
- the declared place-name authority profile and decision references;
- a normalized query key;
- an `as_of_time` used to evaluate historical validity;
- language preferences;
- audience (`STEWARD` or `PUBLIC`);
- search mode (`EXACT`, `PREFIX`, or `HISTORICAL_AS_OF`); and
- request time.

The packet does not retrieve the graph, resolve evidence, or evaluate policy. Those operations must be proven by the caller and their own receipts.

## Candidate transparency

Every returned candidate exposes:

- assertion and binding references;
- feature reference when one exists;
- display text and normalized key;
- name type and source role;
- valid interval;
- language and community context;
- ambiguity state;
- sensitivity state;
- binding confidence;
- authority-decision reference;
- evidence references and claimed resolution state; and
- rank.

No candidate contains geometry, coordinates, jurisdictional status, title, ownership, private notes, restricted source payloads, or hidden search-score internals.

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `ANSWER` | A steward-only internal projection found one or more time-valid, evidence-resolved, non-disputed, non-withheld candidates under the declared profile. |
| `ABSTAIN` | The resolver cannot safely select a candidate because the name is ambiguous, disputed, unbound, out of time, unsupported, or evidence-unresolved. |
| `DENY` | The requested audience must not receive the name projection because sensitivity or policy review is required. |
| `ERROR` | The resolver or its input failed safely and emitted no candidate. |

This slice intentionally rejects `ANSWER` for `PUBLIC` audience because `public_search_authorized` is fixed to `false`. A later public-search implementation requires released evidence, policy evaluation, a public-safe transform, API/runtime tests, and a separate review boundary.

## Time behavior

`as_of_time` must fall inside every returned candidate's validity interval. Historical queries must therefore return the name valid for the requested period rather than silently applying the current name. A missing interval boundary is open-ended; an inverted interval is invalid.

## Ambiguity behavior

The projection must abstain rather than pick a winner when:

- the same normalized name key maps to different feature references;
- a candidate is explicitly disputed;
- a candidate remains unbound or unresolved; or
- a required authority decision or evidence resolution is absent.

Disputed and withheld assertions may influence reason codes, but their sensitive text is not emitted in a public denial.

## Deterministic fixture hash

`kfm-fixture-json-v1` removes top-level `spec_hash`, serializes sorted-key UTF-8 JSON with compact separators, preserves array order, and computes SHA-256. This remains a local synthetic replay profile rather than a repository-wide canonicalization decision.

## Validation boundary

The validator enforces bounded JSON safety, Draft 2020-12 shape, deterministic hash replay, query normalization, canonical arrays, candidate count/ranking, time filtering, homonym detection, ambiguity/sensitivity/evidence rules, finite-outcome consistency, and explicit non-authority declarations.

A green result does not:

- prove the referenced authority graph exists, is current, or is correct;
- resolve any `EvidenceRef` to an authoritative `EvidenceBundle`;
- evaluate rights, sovereignty, cultural sensitivity, policy, review authority, or release state;
- create or authorize a search index, API route, UI result, map label, Focus Mode answer, or public endpoint;
- establish feature identity, geometry, jurisdiction, legal status, title, ownership, or public access;
- authorize promotion, release, deployment, publication, or public use.

## Correction and rollback

This slice is additive. Before merge, close its draft pull request and abandon the branch. After an authorized merge, revert the contract/schema/fixture/validator/test/workflow/receipt set through a reviewed corrective pull request. No search index, cache, API, release, or published artifact requires restoration because none is created here.
