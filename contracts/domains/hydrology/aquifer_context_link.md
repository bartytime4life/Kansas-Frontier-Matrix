<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-hydrology-aquifer-context-link
title: Aquifer Context Link Contract — Hydrology
type: semantic-contract
version: v0.1
status: draft; PROPOSED; separated-pair decision; closed shape and bounded validation present; no publication authority
owners:
  - "@bartytime4life — CODEOWNERS review route"
  - "Hydrology semantic steward assignment — NEEDS VERIFICATION"
  - "Geology semantic steward assignment — NEEDS VERIFICATION"
created: 2026-07-30
updated: 2026-07-30
policy_label: public-with-gates; semantic-contract; hydrology; cross-lane-link; geology; evidence-bound
related:
  - ./aquifer_observation.md
  - ./groundwater_well.md
  - ../geology/HydrostratigraphicUnit.md
  - ../../../docs/domains/hydrology/GLOSSARY.md
  - ../../../docs/domains/hydrology/OBJECT_FAMILIES.md
  - ../../../schemas/contracts/v1/domains/hydrology/aquifer_context_link.schema.json
  - ../../../fixtures/domains/hydrology/aquifer_context_link/README.md
  - ../../../tools/validators/domains/hydrology/validate_aquifer_context_link.py
  - ../../../tests/domains/hydrology/test_aquifer_context_link.py
tags: [kfm, contracts, hydrology, AquiferContextLink, groundwater, geology, cross-lane, evidence, sensitivity]
notes:
  - "This type carries relation metadata only; it never carries measurement values or copied Geology geometry."
  - "The paired schema and tests establish local shape and fixture polarity only."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Aquifer Context Link Contract — Hydrology

`AquiferContextLink` is the Hydrology-owned cross-lane relation from an
`AquiferObservation` or `GroundwaterWell` to a Geology-owned
`HydrostratigraphicUnit`.

> [!IMPORTANT]
> The link records an evidence-scoped interpretation. It does not transfer
> Geology authority, prove either endpoint exists, or turn the linked
> hydrostratigraphic identity into Hydrology-owned truth.

> [!WARNING]
> Closed schema shape is not semantic resolution. Consumers must resolve both
> endpoints, evidence, rights, sensitivity, policy, and release state before a
> consequential or public claim can answer.

## Meaning and boundary

| Concern | `AquiferContextLink` behavior |
|---|---|
| Hydrology endpoint | Typed reference to `AquiferObservation` or `GroundwaterWell` |
| Geology endpoint | Typed reference to Geology `HydrostratigraphicUnit` |
| Relationship | `observed_in`, `screened_in`, `associated_with`, or `interpreted_against` |
| Provenance | Separate source roles, temporal scope, interpretation method, source-record refs, confidence, and evidence refs |
| Sensitivity | Geometry posture and explicit policy-review flag |
| Measurement | Forbidden; remains in `AquiferObservation` |
| Aquifer definition or geometry | Forbidden; remains in Geology |

The link can exist independently of a measurement when the subject is a
`GroundwaterWell`. A measurement can exist independently of a link when an
`AquiferObservation` has no reviewed aquifer interpretation.

## Required semantics

Every link contains:

- stable `id`, `version`, `spec_hash`, and `object_type`;
- a typed Hydrology subject reference;
- a typed Geology endpoint with `owner_domain: geology`;
- one relationship type;
- the source role for each side of the join;
- source time and optional validity/retrieval scope;
- an interpretation method, supporting source-record refs, and confidence;
- a geometry sensitivity posture and policy-review flag;
- at least one evidence reference.

The relationship types are deliberately distinct:

| Relationship | Intended use |
|---|---|
| `observed_in` | Evidence directly assigns an observation to the unit |
| `screened_in` | Evidence assigns a well screen or interval to the unit |
| `associated_with` | Source-supported association that is weaker than direct assignment |
| `interpreted_against` | A documented interpretation or comparison, often lower confidence |

Consumers must not treat these values as interchangeable.

## Anti-collapse rules

The link must not contain:

- groundwater measurement value, unit, basis, qualifier, or no-data state;
- aquifer polygon, interval geometry, lithology, stratigraphy, or a copied
  Geology record;
- well ownership, parcel, title, water-right, allocation, or permit truth;
- an inferred relationship based only on proximity, matching labels, or an
  undocumented overlay;
- a role upgrade, such as modeled or administrative context relabeled observed.

A spatial join may be cited as an interpretation method, but its inputs,
version, tolerance, ambiguity, and confidence remain part of evidence and
validation. The schema does not perform that join.

## Identity, correction, and cardinality

The link has its own identity and lifecycle. Producers must include both
endpoint identities, relationship type, relevant temporal scope, and
interpretation-bearing content in the accepted deterministic identity process.

One observation or well may have zero, one, or multiple links. Multiple links
may represent competing source interpretations, different validity intervals,
or correction history; they must not be silently collapsed to one.

A correction to relationship type, either endpoint, interpretation basis,
source roles, confidence, temporal scope, or sensitivity is link-level
evidentiary change and requires supersession under the accepted identity
policy. It does not mutate the referenced observation or Geology object.

## Compatibility and rollback

This type is additive and optional for measurement-only consumers. New
aquifer-specific consumers must fail closed when the link, endpoint, or
evidence cannot be resolved.

Combined legacy payloads migrate by:

1. retaining measurement fields in `AquiferObservation`;
2. retaining or creating a `GroundwaterWell` only for well/site identity;
3. moving typed aquifer relationship metadata into one or more
   `AquiferContextLink` records; and
4. replacing embedded aquifer content with the Geology endpoint reference.

Rollback must revert the link contract, schema, fixtures, validator, tests, CI
wiring, and every reference from the observation and catalogs together.
Existing `$id` values must not be redirected to a different or permissive
meaning.

## Validation and acceptance

- [x] The schema is closed and Draft 2020-12.
- [x] Hydrology and Geology endpoints are explicitly typed.
- [x] Measurement payloads and copied Geology geometry are rejected.
- [x] Observation-subject and well-subject valid fixtures exist.
- [x] Endpoint mismatch, responsibility collapse, and geometry-copy fixtures
  are expected-invalid.
- [x] A dedicated offline validator and network-denied tests execute in
  Hydrology CI.
- [ ] Endpoint resolution, source admission, evidence closure, cross-lane
  steward review, sensitivity policy, proof, and release remain held.

## Non-goals

This contract does not:

- establish a canonical Geology schema or modify `HydrostratigraphicUnit`;
- require every groundwater observation to name an aquifer;
- calculate, infer, or rank aquifer membership;
- validate real-world scientific correctness;
- authorize exact private-well exposure;
- implement ingestion, policy, proof, release, API, map, or publication logic.

[Back to top](#top)
