<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/common/spatial-geometry
title: contracts/common/spatial_geometry.md — SpatialGeometry Contract
type: contract
version: v0.3
status: draft
owners: OWNER_TBD — Contract steward · Schema steward · GIS steward · Policy steward · Validation steward · Release steward · Docs steward
created: 2026-06-20
updated: 2026-08-10
policy_label: public; contracts; common; spatial-geometry; semantic-contract; shared-kernel; geoprivacy-aware
owning_root: contracts/
responsibility: Define the shared semantic meaning and authority limits of the SpatialGeometry carrier while deferring canonical machine shape, validation implementation, domain meaning, evidence, policy, review, release, and public use to their owning roots.
truth_posture: cite-or-abstain; bounded validator behavior requires current repository and test evidence; passing carrier validation is not geometry, source, survey, policy, release, or publication truth
related:
  - ./README.md
  - ../../schemas/contracts/v1/common/spatial_geometry.schema.json
  - ../../fixtures/contracts/v1/common/spatial_geometry/
  - ../../tools/validators/validate_spatial_geometry.py
  - ../../policy/common/
  - ../../policy/sensitivity/
  - ../../docs/architecture/contract-schema-policy-split.md
  - ../../data/proofs/
  - ../../release/
tags: [kfm, contracts, common, spatial-geometry, geometry, crs, precision-bucket, geoprivacy, shared-kernel, evidence, governance]
notes:
  - "Expanded from scaffold into a semantic contract for the common spatial_geometry object."
  - "Machine-checkable shape is in schemas/contracts/v1/common/spatial_geometry.schema.json. This edit does not change schema fields, enum values, or validation rules."
  - "The declared validator now implements a bounded, deterministic, no-network carrier profile with reviewed fixtures and generated property tests."
  - "The implemented profile supports Point, MultiPoint, LineString, MultiLineString, Polygon, and MultiPolygon; explicit EPSG identifiers; consistent 2D/3D positions; simple polygon rings; and EPSG:4326 coordinate bounds."
  - "The validator does not repair topology, transform CRS, resolve CRS registry authority, evaluate domain policy, or authorize release or public use."
  - "spatial_geometry is a geometry carrier, not a map-rendering instruction, not a CRS transformation engine, not a geocoder, not proof of survey accuracy, and not permission to expose sensitive locations."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# SpatialGeometry Contract

> Semantic contract for `spatial_geometry`, a common KFM geometry carrier that binds a geometry payload to an explicit coordinate reference system and a precision bucket so downstream policy, evidence, validation, and release gates can reason about spatial exposure.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Owner: OWNER_TBD" src="https://img.shields.io/badge/owner-OWNER__TBD-lightgrey">
  <img alt="Family: common" src="https://img.shields.io/badge/family-common-blue">
  <img alt="Schema: proposed" src="https://img.shields.io/badge/schema-PROPOSED-orange">
  <img alt="Validator: bounded" src="https://img.shields.io/badge/validator-bounded-blue">
  <img alt="Authority: semantic" src="https://img.shields.io/badge/authority-semantic__contract-green">
</p>

`contracts/common/spatial_geometry.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema pairing](#schema-pairing) · [Accepted uses](#accepted-uses) · [Exclusions](#exclusions) · [Fields](#fields) · [Invariants](#invariants) · [Precision buckets](#precision-buckets) · [Sensitive-location posture](#sensitive-location-posture) · [Examples](#examples) · [Compatibility and versioning](#compatibility-and-versioning) · [Lifecycle](#lifecycle) · [Validation](#validation) · [No-loss preservation](#no-loss-preservation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Definition of done](#definition-of-done)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Owner:** `OWNER_TBD`  
> **Contract path:** `contracts/common/spatial_geometry.md`  
> **Schema path:** `schemas/contracts/v1/common/spatial_geometry.schema.json`  
> **Truth posture:** `CONFIRMED` contract path, schema path, schema shape, bounded validator, synthetic fixture profile, and focused generated-property tests; policy behavior, CRS registry resolution, runtime integration, CRS transformation, full computational-geometry validity, and downstream usage remain `NEEDS VERIFICATION`.

---

## Meaning

`spatial_geometry` is a compact spatial carrier for a governed KFM geometry.

It answers three questions:

1. **What geometry is being carried?** — `geometry`.
2. **What coordinate reference system gives the coordinates meaning?** — `crs`.
3. **What precision/exposure tier should downstream gates assume?** — `precision_bucket`.

This contract exists because many KFM object families need to carry a geometry while preserving a shared language for coordinate reference, precision, geoprivacy, and release posture.

`spatial_geometry` is a shared-kernel value object. It must stay small, stable, and semantically narrow.

---

## Repo fit

```text
contracts/
└── common/
    ├── README.md
    ├── identity_token.md
    └── spatial_geometry.md

schemas/
└── contracts/
    └── v1/
        └── common/
            └── spatial_geometry.schema.json
```

Adjacent responsibility roots:

| Root | Relationship to this contract |
|---|---|
| `./README.md` | Common contract directory boundary and shared-kernel discipline. |
| `../../schemas/contracts/v1/common/spatial_geometry.schema.json` | Machine-checkable shape for this contract. |
| `../../fixtures/contracts/v1/common/spatial_geometry/` | Synthetic reviewed carrier cases with exact expected finding sets. |
| `../../tools/validators/validate_spatial_geometry.py` | Bounded deterministic carrier validator; not a repair, transform, policy, or release engine. |
| `../../policy/common/` | Schema-declared policy home; existence and behavior remain `NEEDS VERIFICATION`. |
| `../../policy/sensitivity/` | Expected sensitivity/geoprivacy policy surface for location exposure. |
| Domain contracts | Own domain-specific meaning of the thing being located; `spatial_geometry` only carries common geometry semantics. |

---

## Schema pairing

The paired schema is:

```text
schemas/contracts/v1/common/spatial_geometry.schema.json
```

The schema defines machine shape. This Markdown contract defines meaning.

The current schema metadata identifies:

| Schema metadata | Value | Verification posture |
|---|---|---|
| `$id` | `https://schemas.kfm.local/contracts/v1/common/spatial_geometry.schema.json` | `CONFIRMED` from schema. |
| `contract_doc` | `contracts/common/spatial_geometry.md` | `CONFIRMED` from schema. |
| `fixtures_root` | `fixtures/contracts/v1/common/spatial_geometry/` | `CONFIRMED` synthetic exact-polarity carrier profile; broader domain/policy/release coverage remains `NEEDS VERIFICATION`. |
| `validator` | `tools/validators/validate_spatial_geometry.py` | `CONFIRMED` bounded structure, dimensionality, ring, EPSG-identifier, and EPSG:4326-bounds profile. |
| `policy` | `policy/common/` | `NEEDS VERIFICATION` existence/behavior. |
| `status` | `PROPOSED` | `CONFIRMED` from schema metadata. |

---

## Accepted uses

| Use | Allowed? | Rule |
|---|---:|---|
| Carrying a geometry with explicit CRS and precision posture | Yes | Required fields are `geometry`, `crs`, and `precision_bucket`. |
| Referencing a common geometry from domain contracts | Yes | Domain contract still owns what the geometry means. |
| Supporting policy decisions about location exposure | Yes | `precision_bucket` is policy-relevant but not policy by itself. |
| Public display after release gates | Conditional | Requires sensitivity, rights, audience, review, redaction/geoprivacy, and release checks where applicable. |
| Claiming survey accuracy | No | `precision_bucket: survey` is not proof of survey authority without evidence. |
| Performing CRS transformation or geometry repair | No | Transformation/repair belongs in tools, validators, or processing pipelines. |
| Encoding map styling or UI rendering | No | Map/UI behavior belongs in governed UI/style roots. |

---

## Exclusions

| Does not belong in `spatial_geometry` | Correct owner / surface |
|---|---|
| Domain meaning of the located object | Owning domain contract. |
| JSON Schema beyond the paired shape | `../../schemas/contracts/v1/common/spatial_geometry.schema.json`. |
| CRS transformation rules and coordinate reprojection logic | Processing tools / validators after accepted placement. |
| Geometry validity/repair implementation | Validators or geometry-processing packages. |
| Public geoprivacy transform values | Policy bundles; do not expose sensitive thresholds in public contract docs. |
| Source-derived precision evidence | EvidenceBundle / SourceDescriptor / source-family contracts. |
| Release permission | PolicyDecision, ReviewRecord, ReleaseManifest, and release gates. |
| Map rendering style | UI/style/map roots. |
| Tiles, PMTiles, GeoParquet, vector indexes, or scene assets | Data/artifact/publication roots after validation and release. |
| Exact sensitive-location publication | Denied unless governed redaction/review/policy/release gates allow safe transformed representation. |

---

## Fields

| Field | Required by schema | Semantic meaning | Notes |
|---|---:|---|---|
| `geometry` | Yes | Geometry payload being carried. | Current schema requires nested `type` and `coordinates`, but does not restrict geometry type or coordinate shape. |
| `crs` | Yes | Coordinate reference system identifier that gives the coordinates meaning. | Must be explicit. `UNKNOWN`/implicit CRS must not be normalized into public or promoted geometry. |
| `precision_bucket` | Yes | Coarse, policy-evaluable precision posture. | Current enum: `survey`, `parcel`, `community`, `region`, `coarse`. |

The paired schema remains intentionally permissive inside `geometry`. The
current validator adds one proposed executable profile without changing schema
shape:

- supported types: `Point`, `MultiPoint`, `LineString`, `MultiLineString`,
  `Polygon`, and `MultiPolygon`;
- positions: finite, consistently 2D or 3D within one carrier;
- lines: at least two positions;
- polygon rings: at least four positions, closed, non-degenerate, and without
  detected simple-ring self-intersections;
- CRS identifiers: uppercase `EPSG:<positive integer>` syntax; and
- `EPSG:4326`: longitude/latitude bounds are checked without transforming or
  silently reordering coordinates.

This is a bounded validator profile, not a CRS registry, complete GeoJSON
implementation, computational-geometry engine, or compatibility promise for
future schema versions.

---

## Invariants

A `spatial_geometry` must preserve these invariants:

- `geometry`, `crs`, and `precision_bucket` must be present.
- `geometry.type` and `geometry.coordinates` must be present in the nested geometry object.
- `crs` must be explicit and meaningful to the consumer.
- `precision_bucket` must remain a closed enum value until a schema version explicitly changes it.
- `precision_bucket` is a policy-relevant declaration, not proof of accuracy or release permission.
- Exact or high-precision geometry must not be public by default.
- Sensitive-location exposure must be evaluated through policy/review/release gates before publication.
- A valid shape must not be treated as proof that the geometry is correct, source-authoritative, rights-cleared, policy-allowed, or released.
- Geometry used for claims must retain EvidenceRef/EvidenceBundle support through the owning object, receipt, or release surface.

---

## Precision buckets

| Bucket | Meaning | Governance posture |
|---|---|---|
| `survey` | Highest precision posture; may imply field-grade or instrument-grade geometry. | Requires evidence before being treated as authoritative; sensitive public exposure fails closed. |
| `parcel` | Parcel- or property-scale geometry. | May implicate land, ownership, infrastructure, or privacy; policy checks required. |
| `community` | Community/neighborhood/local-area precision. | Often safer than parcel/survey but still policy-relevant. |
| `region` | Regional generalized geometry. | Common public-safe posture when supported by release gates. |
| `coarse` | Very generalized geometry. | Lowest precision posture; still not automatically publishable. |

> [!CAUTION]
> `precision_bucket` is not a release decision. A geometry can be coarse and still sensitive, or survey-grade and allowed only in restricted/admin contexts.

---

## Sensitive-location posture

`spatial_geometry` is intentionally geoprivacy-aware.

Rules:

- sensitive ecology, archaeology, infrastructure, living-person, land/title, cultural, and other protected location contexts fail closed unless policy permits exposure;
- exact coordinates must not be exposed merely because they validate against shape;
- transformed public geometry must carry or link to appropriate redaction/generalization/aggregation receipts where required;
- public UI, API, AI, tile, scene, and export surfaces must use governed, released, policy-safe geometry;
- consumers must not reverse-join generalized public geometry back to restricted exact geometry.

---

## Examples

These examples are illustrative and must still validate against the schema, owning domain contracts, policy, and release gates.

### Valid shape — coarse regional polygon

```json
{
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [-99.0, 38.0],
        [-98.5, 38.0],
        [-98.5, 38.5],
        [-99.0, 38.5],
        [-99.0, 38.0]
      ]
    ]
  },
  "crs": "EPSG:4326",
  "precision_bucket": "region"
}
```

### Valid shape — point with explicit CRS

```json
{
  "geometry": {
    "type": "Point",
    "coordinates": [-98.7654, 38.1234]
  },
  "crs": "EPSG:4326",
  "precision_bucket": "parcel"
}
```

### Invalid shape — missing CRS

```json
{
  "geometry": {
    "type": "Point",
    "coordinates": [-98.7654, 38.1234]
  },
  "precision_bucket": "parcel"
}
```

The invalid example fails the current schema because `crs` is required. It also violates this contract because coordinates without explicit CRS are not governed spatial evidence.

---

## Compatibility and versioning

Current compatibility posture:

- Schema status is `PROPOSED` according to `x-kfm.status`.
- `precision_bucket` values are closed in the current schema.
- The current schema allows any `geometry.type` string and unconstrained `coordinates`; stricter geometry typing would be a schema change.
- The current schema permits additional nested properties inside `geometry` but forbids additional top-level properties.
- The bounded validator is intentionally stricter than the schema for supported geometry types and coordinate structure; schema-only consumers must not claim equivalent semantic validation.
- Adding new precision buckets is compatibility-significant and requires schema, fixture, validator, policy, and consumer updates.
- Changing CRS requirements or default assumptions is compatibility-significant and requires migration review.

Versioning expectations:

1. Update this contract when field meaning changes.
2. Update the schema when machine shape changes.
3. Add fixtures for valid and invalid cases.
4. Update validators and policy gates where applicable.
5. Record migration and rollback posture for consumers.

---

## Lifecycle

```mermaid
flowchart LR
  CREATE[Create or derive geometry] --> VALIDATE[Schema validation]
  VALIDATE --> GEOM[Geometry validity checks]
  GEOM --> EVID[Evidence / source linkage]
  EVID --> POLICY[Policy + sensitivity gate]
  POLICY --> RELEASE[Review + release decision]
  RELEASE --> USE[Use in governed API/UI/export]
```

Lifecycle notes:

- A geometry may be created during RAW/WORK processing, derived during PROCESSED generation, or transformed for public release.
- Schema validation proves only shape.
- Geometry validity checks prove only geometric consistency, not source authority or release eligibility.
- Policy/review/release gates decide whether a geometry may be exposed for a specific audience and purpose.
- Supersession of geometry must preserve correction/rollback posture in the owning object, receipt, or release record.

---

## Validation

Before relying on this contract, verify:

- schema validation passes against `schemas/contracts/v1/common/spatial_geometry.schema.json`;
- the bounded validator and reviewed fixture profile pass;
- generated property tests exercise valid carriers plus open rings, out-of-bounds positions, deterministic diagnostics, duplicate keys, and non-finite input;
- consumers distinguish the validator's closed supported-type profile from the schema's currently open `geometry.type` field;
- coordinate order, dimensionality, ring closure, simple-ring intersections, and declared bounds pass this profile while full topology remains separately governed;
- CRS values satisfy the local identifier syntax, while accepted CRS registry resolution remains `NEEDS VERIFICATION`;
- `precision_bucket` remains closed or versioned changes are documented;
- policy behavior for sensitive/high-precision geometry exists in an accepted policy root;
- public-release contexts check sensitivity, rights, audience, review state, redaction/geoprivacy receipts, and release state before exposing geometry;
- downstream consumers do not treat schema-valid geometry as source-authoritative or release-approved by itself.

---

## No-loss preservation

| Existing element | Disposition | Reason |
|---|---|---|
| Prior meaning section | `KEEP + EXPAND` | The scaffold correctly identified governed semantics; v0.2 adds concrete spatial meaning. |
| Schema URL | `KEEP + GROUND` | The paired schema exists and is now cited through repo evidence. |
| Field section | `KEEP + REPLACE WITH SEMANTIC TABLE` | The old field section delegated too much meaning to schema properties. |
| Invariants | `KEEP + STRENGTHEN` | Required fields/enums/no-extra-properties were preserved and expanded with KFM spatial and geoprivacy constraints. |
| Lifecycle | `KEEP + CLARIFY` | The lifecycle now separates creation/derivation, schema validation, geometry checks, evidence linkage, policy, release, and use. |
| Open questions | `KEEP + MOVE INTO VALIDATION / DEFINITION OF DONE` | Open verification items are now testable checklist items. |

---

## Evidence basis

| Source | Status | Supports | Limits |
|---|---|---|---|
| Prior `contracts/common/spatial_geometry.md` scaffold | `CONFIRMED` | Contract existed and referenced the schema URL, lifecycle, and open verification note. | Scaffold delegated field meaning to schema and lacked semantic boundaries. |
| `schemas/contracts/v1/common/spatial_geometry.schema.json` | `CONFIRMED` | Current field set, required fields, precision enum values, top-level additionalProperties false, and x-kfm metadata. | Schema does not prove geometry validity, CRS policy, release permission, or validator behavior. |
| `tools/validators/validate_spatial_geometry.py` | `CONFIRMED bounded implementation` | Deterministic schema binding, strict JSON reading, supported coordinate structures, dimensionality, ring checks, EPSG identifier syntax, EPSG:4326 bounds, finite findings, and safe diagnostics. | Does not repair/transform geometry, resolve CRS registry authority, prove topology generally, evaluate policy, or release. |
| `fixtures/contracts/v1/common/spatial_geometry/cases.json` and `tests/validators/test_validate_spatial_geometry.py` | `CONFIRMED authored profile` | Synthetic exact-polarity cases and generated property tests for the bounded validator behavior. | Hosted exact-head execution remains `NEEDS VERIFICATION` until CI completes. |
| `contracts/common/README.md` | `CONFIRMED` | Common contracts may define small cross-cutting value objects only when no single domain owns them; common must stay narrow. | Does not prove individual common contract inventory. |
| `docs/architecture/contract-schema-policy-split.md` | `CONFIRMED` | Contracts define meaning; schemas define shape; policy decides admissibility; tests/fixtures prove enforceability. | Path presence and runtime behavior remain verification-bound. |
| Uploaded `KFM Repository Markdown Authoring Agent — Full Operating Prompt v2` | `CONFIRMED user-supplied guidance` | Requires no-loss preservation, evidence grounding, truth labels, GitHub polish, contract/schema doc sections, Markdown QA, and pre-publish discipline. | It is authoring guidance, not repo implementation proof. |

---

## Rollback

Rollback is required if this contract is used as a schema authority, CRS transformation engine, geometry repair implementation, map renderer, release decision, or permission to expose exact/sensitive locations.

Rollback target: prior scaffold content SHA `f0945594fb5f2553f62248de35052c3074a10056`.

---

## Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [x] Validator is implemented beyond placeholder behavior for the bounded carrier profile.
- [x] Synthetic fixtures exist and cover valid/invalid carrier cases with exact finding sets.
- [x] Supported geometry types and coordinate rules are explicit and tested for this profile.
- [ ] CRS values are constrained or resolved by accepted CRS policy/registry.
- [ ] Policy behavior for precision buckets is linked and verified.
- [ ] Public-release review confirms geoprivacy and sensitivity exposure rules.
- [ ] Downstream consumers document how geometry is resolved, transformed, validated, and released.
- [ ] Any precision-bucket or geometry-type expansion is versioned and migration-tested.

---

## Status summary

`spatial_geometry` is a common semantic value object for carrying geometry, CRS, and precision posture. The paired bounded validator checks a declared subset of carrier structure; neither the carrier nor a passing result is the located object itself, proof of spatial accuracy or source authority, a CRS transformation or repair engine, map-rendering instruction, policy decision, release artifact, or permission to expose sensitive location.

<p align="right"><a href="#top">Back to top</a></p>
