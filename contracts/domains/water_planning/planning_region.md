<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-water-planning-planning-region
title: PlanningRegion Contract — Water Planning
type: semantic-contract
version: v0.2
status: draft; PROPOSED; schema-scaffold; reference-authority checks implemented; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Water Planning domain steward
  - OWNER_TBD — Contracts steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Policy steward
created: 2026-07-28
updated: 2026-07-30
policy_label: public-with-gates; semantic-contract; water-planning; deferred-epic; PROPOSED
related:
  - ./README.md
  - ./rac_geometry_registry.md
  - ../../../schemas/contracts/v1/domains/water_planning/planning_region.schema.json
  - ../../../schemas/contracts/v1/domains/water_planning/rac_geometry_dataset_registry.schema.json
  - ../../../schemas/contracts/v1/domains/water_planning/rac_county_crosswalk_registry.schema.json
  - ../../../fixtures/domains/water_planning/planning_region/
  - ../../../fixtures/domains/water_planning/geometry_authority/
  - ../../../tools/validators/domains/water_planning/validate_geometry_authority.py
  - ../../../tools/validators/domains/water_planning/validate_rac_registry.py
  - ../../../tests/domains/water_planning/test_geometry_authority.py
  - ../../../tests/domains/water_planning/test_rac_registry.py
  - ../../../data/registry/datasets/water_planning/kwo_rac_regions_2026-06-24.json
  - ../../../data/registry/crosswalks/water_planning/kwo_rac_counties_2026-06-24__tiger2025.json
  - ../../../data/registry/crosswalks/README.md
  - ../../../docs/sources/catalog/kansas/kwo.md
  - ../../../tests/schemas/test_water_planning_contracts.py
  - ../../../.github/workflows/schema-validation.yml
  - ../../../.github/workflows/briefing-integration.yml
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# PlanningRegion Contract — Water Planning

[![Contract status: PROPOSED](https://img.shields.io/badge/contract-PROPOSED-d29922?style=flat-square)](#status-and-authority)
[![Schema: Draft 2020-12](https://img.shields.io/badge/schema-Draft%202020--12-0969da?style=flat-square)](../../../schemas/contracts/v1/domains/water_planning/planning_region.schema.json)
[![Release: not authorized](https://img.shields.io/badge/release-not%20authorized-b42318?style=flat-square)](#release-and-public-boundary)

Defines stable KFM identity and reference-coherence rules for Kansas's 14 Regional Advisory Committee planning areas without embedding or inferring geometry or county membership.

> [!IMPORTANT]
> This semantic contract and its paired schema remain `draft` / `PROPOSED`. The `kwo-rac-01` through `kwo-rac-14` ordinals are a KFM identity convention, not KWO-native region numbers. Contract, schema, fixture, validator, registry, workflow, or badge state does not admit a source, clear rights, approve policy, authorize release, or make a record KFM `PUBLISHED`.

## Quick navigation

- [Meaning](#meaning)
- [Status and authority](#status-and-authority)
- [Identity inventory](#identity-inventory)
- [Contract fields](#contract-fields)
- [Authority and resolution rules](#authority-and-resolution-rules)
- [Current internal registry references](#current-internal-registry-references)
- [Anti-collapse boundaries](#anti-collapse-boundaries)
- [Schema posture](#schema-posture)
- [Synthetic example](#synthetic-example)
- [Validation](#validation)
- [Known limits and verification backlog](#known-limits-and-verification-backlog)
- [Release and public boundary](#release-and-public-boundary)
- [Compatibility, correction, and rollback](#compatibility-correction-and-rollback)
- [Related](#related)

## Meaning

A `PlanningRegion` represents one Kansas Regional Advisory Committee (RAC) planning-area identity. The Kansas Water Office source identifies exactly 14 RAC names. KFM assigns `kwo-rac-01` through `kwo-rac-14` in the frozen lexicographic order of that source-grounded name inventory. The ordinal is a KFM identity convention, not a claim that KWO publishes native RAC numbers.

The public KWO page exposes no source-native version. The identity inventory therefore records that unversioned-page posture and an observation date, then pins its normalized authority metadata plus ordered ID/ordinal/name tuples with a KFM record version and digest. The digest is not represented as a digest of remote page bytes. Each `PlanningRegion.source_ref` is intended to resolve to that one identity-authority record. A later correction must create explicit correction or supersession lineage; it must not silently renumber identities.

The contract defines region-identity meaning and explicit reference states. The paired JSON Schema defines accepted document shape. Source admission, authority-record resolution, geometry bytes, county intersections, policy, review, release, correction, and publication remain separate responsibilities.

[Back to top](#top)

## Status and authority

| Surface | Current posture | Authority boundary |
| --- | --- | --- |
| This document | `draft`; `PROPOSED`; v0.2 | Defines semantic identity, reference-state meaning, and anti-collapse rules. |
| [Paired JSON Schema](../../../schemas/contracts/v1/domains/water_planning/planning_region.schema.json) | Draft 2020-12; `x-kfm.status: PROPOSED` | Defines machine-checkable shape and conditional null/reference coherence; it does not resolve references or establish source truth. |
| [Planning-region fixtures](../../../fixtures/domains/water_planning/planning_region/) | Synthetic test inputs | Exercise representative schema acceptance and rejection; they are not RAC authority records. |
| [Geometry-authority fixtures](../../../fixtures/domains/water_planning/geometry_authority/) and [validator](../../../tools/validators/domains/water_planning/validate_geometry_authority.py) | Synthetic, deterministic, no-network validation surface | Enforce the 14-region identity inventory and synthetic reference-authority coherence; they do not validate production geometry or authorize release. |
| [RAC registry contract](./rac_geometry_registry.md), records, and [validator](../../../tools/validators/domains/water_planning/validate_rac_registry.py) | Source-grounded internal candidate; records are `current` and `not-released` | Pin checked-in geometry, source, identity, county-intersection, digest, and release constraints without turning registry state into publication. |
| [KWO source catalog entry](../../../docs/sources/catalog/kansas/kwo.md) | Source-grounded candidate; rights review pending | Records source role, observations, and limitations; it does not activate a recurring connector or clear public release. |
| `policy/domains/water_planning/` | Schema metadata forward pointer; implementation is **NOT ESTABLISHED** | No allow, deny, restrict, hold, abstain, or release decision may be inferred from this contract. |
| [Schema validation](../../../.github/workflows/schema-validation.yml) and [water-planning integration](../../../.github/workflows/briefing-integration.yml) | Read-only pull-request workflows | Produce bounded validation evidence only; they do not write KFM state or grant review, release, deployment, or publication authority. |

Directory placement follows the accepted responsibility-root split: `contracts/` owns semantic meaning, `schemas/` owns machine shape, `tools/` and `tests/` own executable checks, `data/` owns governed records and payloads, and `policy/` and `release/` own their respective decisions. The [`water_planning` segment](./README.md) is a domain lane inside the contract authority root, not a separate authority surface.

[Back to top](#top)

## Identity inventory

The following inventory is the source-grounded candidate pinned by the KWO catalog entry and enforced by the geometry-authority validator. Ordering is lexicographic by official name.

| KFM ID | KFM ordinal | Source-grounded RAC name |
| --- | ---: | --- |
| `kwo-rac-01` | 1 | Cimarron |
| `kwo-rac-02` | 2 | Equus-Walnut |
| `kwo-rac-03` | 3 | Great Bend Prairie |
| `kwo-rac-04` | 4 | Kansas |
| `kwo-rac-05` | 5 | Marais des Cygnes |
| `kwo-rac-06` | 6 | Missouri |
| `kwo-rac-07` | 7 | Neosho |
| `kwo-rac-08` | 8 | Red Hills |
| `kwo-rac-09` | 9 | Smoky Hill-Saline |
| `kwo-rac-10` | 10 | Solomon-Republican |
| `kwo-rac-11` | 11 | Upper Arkansas |
| `kwo-rac-12` | 12 | Upper Republican |
| `kwo-rac-13` | 13 | Upper Smoky Hill |
| `kwo-rac-14` | 14 | Verdigris |

The identity-authority candidate uses record version `kfm-rac-identity-v1`, records `source_native_numeric_ids: false`, and digests normalized authority metadata plus the ordered identity tuples. A source correction may update evidence and lineage, but it must not silently change an established `region_id`.

[Back to top](#top)

## Contract fields

| Field | Required | Schema constraint | Semantic interpretation |
| --- | ---: | --- | --- |
| `region_id` | Yes | String matching `^kwo-rac-(0[1-9]\|1[0-4])$` | Stable KFM region identity. The numeric suffix must correspond to the governed KFM ordinal. |
| `name` | Yes | Non-empty string | Source-grounded RAC planning-region name. Schema shape alone does not verify the pinned name inventory. |
| `rac_number` | Yes | Integer from 1 through 14 | KFM stable ordinal; not a KWO-native numeric identifier. |
| `geometry_ref` | Yes | Non-empty string or `null`, conditional on `geometry_confidence` | Reference to a governed region-geometry authority record; geometry is never embedded here. |
| `geometry_confidence` | Yes | `unresolved`, `approximate`, or `confirmed` | Explicit geometry-reference resolution state. It is not a free-form confidence score. |
| `county_crosswalk_ref` | Yes | Non-empty string or `null`, conditional on crosswalk status | Reference to a governed county-crosswalk authority record; county membership is never embedded here. |
| `county_crosswalk_resolution_status` | Yes | `unresolved` or `resolved` | Explicit crosswalk-reference resolution state. |
| `source_ref` | Yes | Non-empty string | Reference to the governed KWO RAC identity-authority record. Shape validity alone does not resolve the target. |

All eight fields are required, and the current schema rejects unknown fields with `additionalProperties: false`.

[Back to top](#top)

## Authority and resolution rules

### Identity coherence

- Exactly 14 unique IDs and ordinals exist: `kwo-rac-01` through `kwo-rac-14` and 1 through 14.
- `region_id`, `rac_number`, and `name` must correspond to the pinned inventory above. Values `00`, `15`, `99`, gaps, duplicates, mismatches, and foreign namespaces fail the geometry-authority validator.
- `source_ref` must resolve to the governed KWO RAC identity-authority record. The current synthetic authority envelope requires `kwo:rac:regional-advisory-committees`.
- RAC, groundwater-management-district, county, municipality, venue, and project-location identities remain distinct. A GMD reference cannot satisfy a RAC reference.

### Reference-state coherence

| State field | State | Required reference posture |
| --- | --- | --- |
| `geometry_confidence` | `unresolved` | `geometry_ref` must be `null`. |
| `geometry_confidence` | `approximate` or `confirmed` | `geometry_ref` must be a non-empty reference; the authority validator additionally requires a declared `region-geometry` authority in its synthetic envelope. |
| `county_crosswalk_resolution_status` | `unresolved` | `county_crosswalk_ref` must be `null`. |
| `county_crosswalk_resolution_status` | `resolved` | `county_crosswalk_ref` must be a non-empty reference; the authority validator additionally requires a declared `county-crosswalk` authority in its synthetic envelope. |

Approximate and confirmed geometry authorities carry version, digest, correction posture, and use-boundary metadata outside the `PlanningRegion` payload. A resolved county crosswalk is likewise reference-only. Geometry, GeoJSON, coordinates, polygons, centroids, addresses, county arrays, and inferred containment are not valid `PlanningRegion` fields.

> [!WARNING]
> A non-empty reference is not resolution proof. The paired schema checks string/null coherence only; referential authority, kind, version, digest, correction lineage, and use boundary require a validator or resolver operating against the applicable authority records.

[Back to top](#top)

## Current internal registry references

The repository contains one source-grounded KWO RAC geometry dataset version and one derived Census 2025 county-intersection crosswalk. These are governed internal records, not inline `PlanningRegion` content.

| Record | Stable identifier | Checked-in posture | Bounded meaning |
| --- | --- | --- | --- |
| [RAC geometry dataset](../../../data/registry/datasets/water_planning/kwo_rac_regions_2026-06-24.json) | `kfm:dataset-version:water-planning:kwo-rac-regions:2026-06-24` | `record_status: current`; `release_status: not-released`; 14-feature payload | Versioned reference authority for the normalized RAC geometry payload. |
| [RAC/county crosswalk](../../../data/registry/crosswalks/water_planning/kwo_rac_counties_2026-06-24__tiger2025.json) | `kfm:crosswalk:water-planning:kwo-rac-to-county:2026-06-24:tiger-2025` | `record_status: current`; `release_status: not-released`; 105 counties and 209 mappings | Deterministic positive-area polygon intersections between KWO RAC geometry and Census 2025 county geometry. |

Resolved region records may reference these identifiers through their governing authority records. The original synthetic authority fixtures remain test-only and do not override the canonical checked-in records.

The county crosswalk records measured geometry overlap, not county membership. Its `dominant`, `material-partial`, and `boundary-sliver` classes do not establish political, administrative, advisory, funding, or governance relationships. A consumer that needs a binary county list must define and review a separate materiality rule; it must not silently promote a boundary sliver into membership.

[Back to top](#top)

## Anti-collapse boundaries

| Boundary | Required interpretation |
| --- | --- |
| Planning region != meeting, decision, award, or project | A RAC identity does not prove that an event, recommendation, funding action, or project exists. |
| Region identity != region geometry | The stable identity remains distinct from every geometry version and payload. |
| Region geometry != county crosswalk | A county-intersection derivative cannot replace the authoritative RAC boundary geometry. |
| Geometry overlap != membership | Polygon intersection does not create political, administrative, advisory, funding, or governance membership. |
| RAC != GMD, county, municipality, or venue | Similar location language or containment does not collapse distinct namespaces and authority families. |
| Region reference != project location | A project's planning-region relation does not prove its location geometry, and location geometry does not prove region membership. |
| Link presence != authority resolution | A string or source-page link does not prove target kind, version, digest, currency, correction state, or use boundary. |
| Schema or validator pass != source or release authority | Passing checks do not admit a source, construct evidence or proof, clear rights, approve policy, release data, or publish. |

[Back to top](#top)

## Schema posture

| Schema fact | Current value | Consequence |
| --- | --- | --- |
| Canonical machine-shape file | [`planning_region.schema.json`](../../../schemas/contracts/v1/domains/water_planning/planning_region.schema.json) | Change accepted structure in the schema, not by prose alone. |
| JSON Schema dialect | Draft 2020-12 | Consumers must use compatible tooling. |
| Schema status | `PROPOSED` | No stable, released, or published maturity is claimed. |
| Properties / required fields | 8 / 8 | Every reference and state field is explicit, including unresolved states. |
| Exact RAC ID pattern | `^kwo-rac-(0[1-9]\|1[0-4])$` | IDs outside `01` through `14` fail schema validation. |
| Ordinal range | 1 through 14 | Out-of-range ordinals fail schema validation. |
| Geometry coherence | Conditional schema shape | `unresolved` requires `null`; other admitted states require a non-empty string. |
| County-crosswalk coherence | Conditional schema shape | `unresolved` requires `null`; `resolved` requires a non-empty string. |
| Unknown fields | Rejected by `additionalProperties: false` | Inline geometry, county arrays, and undeclared shortcuts are structurally rejected. |
| Cross-field identity and authority | Not fully enforced by this schema | ID/ordinal/name correspondence, exact `source_ref`, uniqueness, inventory completeness, and reference resolution require separate validation. |

The schema and validators form separate layers:

- [`test_water_planning_contracts.py`](../../../tests/schemas/test_water_planning_contracts.py) checks schema presence, representative valid/invalid fixtures, the 1–14 ordinal bound, exact ID range, and null/reference coherence.
- [`validate_geometry_authority.py`](../../../tools/validators/domains/water_planning/validate_geometry_authority.py) checks the complete 14-entry identity inventory, ID/ordinal/name agreement, the exact identity authority, and synthetic geometry/crosswalk authority metadata.
- [`validate_rac_registry.py`](../../../tools/validators/domains/water_planning/validate_rac_registry.py) separately checks the checked-in geometry and county-crosswalk registry records, payload bytes, identities, mappings, digests, source versions, correction posture, and `not-released` state.

No one layer may be described as proving the responsibilities of the others.

[Back to top](#top)

## Synthetic example

The repository's valid fixture preserves unresolved geometry and county-crosswalk references explicitly:

```json
{
  "region_id": "kwo-rac-01",
  "name": "Cimarron",
  "rac_number": 1,
  "geometry_ref": null,
  "geometry_confidence": "unresolved",
  "county_crosswalk_ref": null,
  "county_crosswalk_resolution_status": "unresolved",
  "source_ref": "kwo:rac:regional-advisory-committees"
}
```

This fixture is synthetic and test-only. It proves neither that a source observation is current nor that a geometry, county relationship, policy decision, or release exists. The paired invalid fixture exercises an out-of-range `kwo-rac-15` / ordinal `15` record and missing required crosswalk fields.

[Back to top](#top)

## Validation

Run commands from the repository root.

### Validate the paired schema and fixtures

```bash
python -m pytest -q tests/schemas/test_water_planning_contracts.py
```

### Validate the synthetic identity and authority envelope

```bash
python tools/validators/domains/water_planning/validate_geometry_authority.py \
  fixtures/domains/water_planning/geometry_authority/valid/valid_1.json

python -m unittest tests.domains.water_planning.test_geometry_authority -v
```

Expected validator stdout for the one valid fixture:

```json
{"files":1,"outcome":"VALIDATOR_PASS"}
```

### Validate the checked-in RAC registry slice

```bash
python tools/validators/domains/water_planning/validate_rac_registry.py
python -m unittest tests.domains.water_planning.test_rac_registry -v
```

Expected validator stdout at the pinned registry baseline:

```text
RAC_REGISTRY_OK regions=14 counties=105 mappings=209
```

| Validation surface | What success checks | What success does not prove |
| --- | --- | --- |
| Schema suite | Shape, required fields, exact ID and ordinal bounds, representative polarity, and reference-state coherence | Exact name/source authority, full inventory uniqueness, referential integrity, source truth, rights, or release. |
| Geometry-authority validator and tests | Synthetic identity inventory, authority metadata, non-inline geometry rules, finite findings, and no-network behavior | Production geometry, checked-in registry parity, official county membership, source admission, or publication. |
| RAC registry validator and tests | Pinned local payload, 14-region and 105-county coverage, ordered 209-row mapping digest, source/correction constraints, and `not-released` posture | Source refresh, spatial re-derivation, rights clearance, policy approval, release, or publication. |
| `schema-validation` workflow | Repository schema and contract test lanes on pull requests | Semantic promotion, evidence closure, source authority, rights, policy, or release. |
| `briefing-integration` workflow | Read-only, no-network water-planning domain and registry checks for this path | Review approval, repository authorization, proof, deployment, release, or publication. |

> [!NOTE]
> Validator exit `0` and green workflow status are bounded validation evidence only. They do not emit an EvidenceBundle, receipt, proof, policy decision, release manifest, correction notice, or published carrier.

[Back to top](#top)

## Known limits and verification backlog

| ID | Status | Verification item |
| --- | --- | --- |
| `WP-PR-01` | `NEEDS VERIFICATION` | Decide whether ID/ordinal/name correspondence, exact `source_ref`, uniqueness, and complete-inventory rules should gain a canonical machine-enforcement surface beyond the synthetic authority envelope. |
| `WP-PR-02` | `NEEDS VERIFICATION` | Add or identify an end-to-end resolver that validates a `PlanningRegion` record's non-null geometry and county-crosswalk references against the checked-in canonical registry authority records. |
| `WP-PR-03` | `NEEDS VERIFICATION` | Preserve an admissible, correction-aware observation of the unversioned public KWO RAC name page; the normalized identity digest is not a digest of remote page bytes. |
| `WP-PR-04` | `NEEDS VERIFICATION` | Complete independent rights and source review for the KWO geometry and Census-derived crosswalk before any release decision. |
| `WP-PR-05` | `NEEDS VERIFICATION` | Define compatibility and migration behavior if an official RAC name, boundary, source feature, or county geometry changes without silently renumbering identities. |
| `WP-PR-06` | `NEEDS VERIFICATION` | Establish policy, review, public-safe projection, correction, withdrawal, release, and rollback closure for any consumer-facing region record or map layer. |
| `WP-PR-07` | `NEEDS VERIFICATION` | Establish accountable water-planning, contract, source, schema, and policy stewardship beyond placeholder owners and CODEOWNERS routing. |

Until these items close, preserve unresolved states, narrow claims to the pinned evidence boundary, and do not infer region membership or public-release eligibility from proximity, containment, county, address, venue, recipient, project prose, or a non-empty reference.

[Back to top](#top)

## Release and public boundary

The checked-in geometry dataset and county-crosswalk records are internal and `not-released`. Their `record_status: current` values identify the repository's current internal pointers for the observed versions; they do not override `release_status`, rights review, policy, evidence, correction, or rollback gates.

Public clients, maps, search, exports, graphs, and AI surfaces must consume only governed, release-approved, public-safe interfaces or carriers. They must not read this contract lane, synthetic fixtures, processed geometry, or internal registry records as an ordinary public data path.

A commit, pull request, merge, schema pass, validator pass, workflow result, source descriptor, registry record, badge, or rendered map is not a KFM promotion, release, or publication event.

[Back to top](#top)

## Compatibility, correction, and rollback

Treat the following as compatibility-significant:

- the `kwo-rac-01` through `kwo-rac-14` identity mapping and KFM-ordinal meaning;
- required fields, enums, nullability, ID pattern, ordinal bounds, and `additionalProperties`;
- geometry and county-crosswalk reference-state semantics;
- identity, geometry, crosswalk, source, correction, and release authority boundaries; and
- any consumer rule that converts polygon overlap into a region/county relation.

A material semantic or shape change should update this contract, the paired schema, representative valid and invalid fixtures, applicable validators, tests, authority records, known consumers, and correction lineage in one dependency-closed review boundary. Preserve prior identities, versions, source observations, digests, and supersession links. Do not silently rewrite an established identity or overwrite a relied-on geometry/crosswalk baseline.

Before merge, rollback is to close the draft pull request and leave its scoped branch unmerged. After merge, use a focused revert or corrective pull request against the actual merged commit. Documentation rollback must not delete or rewrite source observations, registry records, processed geometry, correction history, proofs, release state, or published carriers.

[Back to top](#top)

## Related

| Surface | Role |
| --- | --- |
| [`README.md`](./README.md) | Water-planning semantic-contract index and cross-entity anti-collapse boundaries. |
| [`rac_geometry_registry.md`](./rac_geometry_registry.md) | Semantic contract for the checked-in RAC geometry dataset and county-crosswalk record families. |
| [`planning_region.schema.json`](../../../schemas/contracts/v1/domains/water_planning/planning_region.schema.json) | Canonical proposed machine shape for `PlanningRegion`. |
| [RAC geometry registry schema](../../../schemas/contracts/v1/domains/water_planning/rac_geometry_dataset_registry.schema.json) | Machine shape for the geometry dataset registry record. |
| [RAC/county crosswalk registry schema](../../../schemas/contracts/v1/domains/water_planning/rac_county_crosswalk_registry.schema.json) | Machine shape for the derived county-intersection registry record. |
| [Planning-region fixtures](../../../fixtures/domains/water_planning/planning_region/) | Representative synthetic valid and invalid records. |
| [Geometry-authority fixtures](../../../fixtures/domains/water_planning/geometry_authority/) | Synthetic identity and reference-authority envelopes. |
| [`validate_geometry_authority.py`](../../../tools/validators/domains/water_planning/validate_geometry_authority.py) | Deterministic synthetic identity and reference-authority checker. |
| [`validate_rac_registry.py`](../../../tools/validators/domains/water_planning/validate_rac_registry.py) | Deterministic validator for the checked-in source-grounded registry slice. |
| [`test_water_planning_contracts.py`](../../../tests/schemas/test_water_planning_contracts.py) | Schema-family regression tests. |
| [`test_geometry_authority.py`](../../../tests/domains/water_planning/test_geometry_authority.py) | No-network synthetic authority-validation tests. |
| [`test_rac_registry.py`](../../../tests/domains/water_planning/test_rac_registry.py) | Checked-in registry regression tests. |
| [KWO source catalog entry](../../../docs/sources/catalog/kansas/kwo.md) | KWO source role, identity inventory, geometry observation, rights, and release limitations. |
| [RAC geometry dataset record](../../../data/registry/datasets/water_planning/kwo_rac_regions_2026-06-24.json) | Internal digest-pinned reference authority for the 14-feature geometry payload. |
| [RAC/county crosswalk record](../../../data/registry/crosswalks/water_planning/kwo_rac_counties_2026-06-24__tiger2025.json) | Internal digest-pinned 105-county, 209-mapping positive-area intersection record. |
| [Directory Rules v2](../../../docs/doctrine/directory-rules.md) | Accepted responsibility-root and domain-lane placement authority. |
| [ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Adoption record for Directory Rules v2. |
| [`schema-validation.yml`](../../../.github/workflows/schema-validation.yml) | Read-only pull-request schema and contract validation workflow. |
| [`briefing-integration.yml`](../../../.github/workflows/briefing-integration.yml) | Read-only path-triggered water-planning validation workflow. |

[Back to top](#top)
