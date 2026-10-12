<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-hydrology-aquifer-observation
title: Aquifer Observation Contract — Hydrology
type: semantic-contract
version: v0.3
status: draft; PROPOSED; separated-pair decision; closed shape and bounded validation present; no publication authority
owners:
  - "@bartytime4life — CODEOWNERS review route"
  - "Hydrology semantic steward assignment — NEEDS VERIFICATION"
created: 2026-06-22
updated: 2026-07-30
policy_label: public-with-gates; semantic-contract; hydrology; groundwater; observation; evidence-bound; release-gated
related:
  - ./aquifer_context_link.md
  - ./groundwater_well.md
  - ./water_level_observation.md
  - ./domain_observation.md
  - ../geology/HydrostratigraphicUnit.md
  - ../../../docs/domains/hydrology/GLOSSARY.md
  - ../../../docs/domains/hydrology/OBJECT_FAMILIES.md
  - ../../../docs/domains/hydrology/IDENTITY_MODEL.md
  - ../../../schemas/contracts/v1/domains/hydrology/aquifer_observation.schema.json
  - ../../../fixtures/domains/hydrology/aquifer_observation/README.md
  - ../../../tools/validators/domains/hydrology/validate_aquifer_observation.py
  - ../../../tests/domains/hydrology/test_aquifer_observation.py
tags: [kfm, contracts, hydrology, AquiferObservation, groundwater, observation, source-role, evidence, correction, rollback]
notes:
  - "AquiferObservation remains the observed measurement carrier."
  - "AquiferContextLink separately carries the Hydrology-to-Geology relationship."
  - "The paired schema and tests establish local shape and fixture polarity only."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Aquifer Observation Contract — Hydrology

`AquiferObservation` is a first-class Hydrology observation for a
groundwater-level or aquifer-state measurement. It does not carry the
Hydrology-to-Geology relationship; that responsibility belongs to
[`AquiferContextLink`](./aquifer_context_link.md).

> [!IMPORTANT]
> The adopted model is a clearly separated pair. An observation remains valid
> without an aquifer-context link. If a claim requires named aquifer context,
> the consumer must resolve an `AquiferContextLink` and its Geology endpoint or
> abstain from that part of the claim.

> [!WARNING]
> The schema, fixtures, validator, and tests added for this contract establish
> closed local shape and fixture polarity only. They do not admit sources,
> resolve EvidenceRefs, establish groundwater truth, apply policy, expose
> sensitive locations, approve release, or publish data.

## Decision

| Option | Measurement semantics | Cross-lane authority | Migration risk | Decision |
|---|---|---|---|---|
| First-class observation only | Clear | Encourages aquifer identity or geometry to leak into the observation | Medium | Rejected |
| Cross-lane link only | Loses the glossary's measurement carrier and overloads a relation with values | Clear | High | Rejected |
| Separated pair | Measurement stays in `AquiferObservation`; relation stays in `AquiferContextLink` | Geology identity remains reference-only | Lowest, additive path | **Adopted** |

The split preserves the glossary meaning, resolves the object-catalog
ambiguity, and keeps measurement lifecycle independent from interpretation
lifecycle.

## Responsibility boundary

| Type | Owns | Must not own |
|---|---|---|
| `AquiferObservation` | Source-scoped observed parameter, value or no-data state, unit, measurement basis, observation time, site/well context, evidence refs, correction lineage | Aquifer geometry, lithology, stratigraphy, hydrogeologic interpretation, permits, ownership, water rights, modeled surfaces |
| `AquiferContextLink` | Typed Hydrology subject, typed Geology endpoint, relationship kind, temporal scope, interpretation basis, endpoint source roles, sensitivity, evidence refs | Measurement values, copied Geology geometry, Geology identity definition |
| `GroundwaterWell` | Well/site identity and well context | Observation values or a Geology-owned aquifer |
| `WaterLevelObservation` | Surface-water gauge height or stage | Groundwater/aquifer-state measurement |
| Geology `HydrostratigraphicUnit` | Hydrostratigraphic identity and Geology-owned meaning | Hydrology observation lifecycle |

## Required observation meaning

The machine shape requires:

- stable `id`, `version`, `spec_hash`, and `object_type`;
- source descriptor and source-record references;
- `source_role: observed`;
- a named parameter;
- a measurement unit, basis, status, and explicit no-data posture;
- an observation time;
- a site reference and geometry posture;
- at least one evidence reference.

A numeric observation requires `source_value` and `no_data: false`. A no-data
observation requires a reason, sets `no_data: true`, and must not contain a
numeric source value. Normalized values are optional, but when present they
carry the output unit and deterministic transform reference.

## Site, well, and aquifer context

`spatial_context.site_ref` identifies the source location or site context.
`groundwater_well_ref` is optional because some valid regional or
source-defined observations are not keyed to a KFM `GroundwaterWell`.

`aquifer_context_link_refs` is also optional. Its absence means only that no
reviewed link is attached; it does not invalidate the measurement. It also
means the observation alone cannot support “this measurement is in
HydrostratigraphicUnit X.”

Aquifer names, polygons, intervals, lithology, stratigraphy, and other
Geology-owned content must not be embedded in the observation.

## Source role, time, and evidence

- The observation contract accepts only the `observed` role. Administrative,
  modeled, regulatory, aggregate, candidate, or synthetic payloads require a
  different object or pre-admission state.
- `observed_time` is the measurement time. `source_time`, `retrieval_time`, and
  correction time remain separate.
- Provisional, final, corrected, estimated, and source-defined measurement
  status remains explicit.
- Schema validity does not establish evidence closure. Every `evidence_ref`
  still must resolve through the governed evidence path before a consequential
  claim can answer.
- Exact or reverse-engineerable well locations remain subject to policy and
  review. A valid internal shape is not automatically public-safe.

## Identity and correction

The current schema constrains the ID namespace and requires a `spec_hash`; it
does not implement a canonical ID generator. Producers must follow the shared
Hydrology identity doctrine and must not derive identity from retrieval time,
file path, serializer order, or link presence alone.

Changing an observation's evidentiary value, unit, measurement basis,
observation time, source record, or site identity is compatibility-significant
and requires a new identity or explicit supersession under the accepted
identity policy. Link-only changes rotate the `AquiferContextLink`, not the
measurement, unless they also correct an identity-bearing observation field.

## Compatibility and migration

The pair is intentionally additive:

1. Existing prose-only `AquiferObservation` concepts map to the measurement
   type when they contain a groundwater measurement.
2. Any existing payload that combines measurement and aquifer relation must be
   split into one observation plus zero or more context links.
3. A missing context link remains valid for measurement-only consumers.
4. Consumers making aquifer-specific claims must require link resolution and
   must not infer a link from a name, geometry overlay, well label, or proximity.
5. `WaterLevelObservation` is not broadened or reinterpreted.
6. No existing stable schema `$id` is redirected.

Rollback is the removal or revert of both new schema families, fixtures,
validators, tests, workflow wiring, and catalog references as one
dependency-closed unit. Do not roll back only one half of the pair or redirect
the new `$id` values to permissive replacement shapes.

## Validation boundary

| Surface | Established here | Still held |
|---|---|---|
| JSON Schema | Closed Draft 2020-12 object shape | Source admission, semantic evidence resolution, policy |
| Fixtures | Valid linked/unlinked observations and negative role/authority-collapse examples | Real source records, exhaustive correction/sensitivity cases |
| Validator | Offline local schema runner | Endpoint resolution, data-quality or scientific validation |
| Tests | Fixture polarity, valid unlinked case, network denial | Proof, release, public API/UI, publication |
| CI | Intentional inventory and bounded execution | Broader Hydrology readiness and all existing proof/release holds |

## Acceptance criteria

- [x] `AquiferObservation` has a stable, closed schema.
- [x] The schema rejects non-observed roles and embedded Geology content.
- [x] Linked and unlinked observations have valid synthetic fixtures.
- [x] A dedicated validator checks the fixture family without network access.
- [x] Tests prove fixture polarity, optional link behavior, and network denial.
- [x] The glossary, object catalog, identity model, adjacent contracts, indexes,
  and Hydrology CI describe the same separated pair.
- [ ] Source admission, rights, evidence closure, sensitivity policy, identity
  generation, correction policy, and release authority remain separately held.

## Non-goals

This contract does not:

- define or copy Geology aquifer geometry;
- validate that a referenced well or hydrostratigraphic unit exists;
- infer aquifer membership from spatial overlap;
- normalize real measurements or accept a groundwater source;
- implement policy, redaction, proof, release, API, map, or publication logic;
- make KFM an engineering, water-supply, drought-response, regulatory, or
  life-safety authority.

[Back to top](#top)
