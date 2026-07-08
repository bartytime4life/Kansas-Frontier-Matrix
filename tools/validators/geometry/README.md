<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-geometry-readme
title: tools/validators/geometry README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-gis-steward-plus-geometry-steward-plus-schema-steward-plus-policy-steward-plus-evidence-steward-plus-release-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; geometry-validator; spatial-geometry; shared-kernel; CRS; precision-bucket; geoprivacy-aware; fail-closed; release-gated; non-authoritative
owning_root: tools/
responsibility: proposed shared Geometry validator lane for checking spatial_geometry carrier shape, CRS declaration, precision_bucket posture, geometry role, geometry validity, topology sanity, bounds/coordinate order, dimensionality, uncertainty/scale caveats, sensitivity/geoprivacy linkage, EvidenceRef/EvidenceBundle linkage, policy/review/release linkage, correction and rollback linkage, finite negative outcomes, and public-surface denial checks while deferring geometry semantics, domain meaning, CRS transformation implementation, geocoding, proof storage, receipts, policy decisions, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../geology/public_safe_geometry/README.md
  - ../geology/README.md
  - ../cross-domain-joins/README.md
  - ../evidence/README.md
  - ../citation/README.md
  - ../evidence_bundle/README.md
  - ../../validate_spatial_geometry.py
  - ../../../contracts/common/spatial_geometry.md
  - ../../../schemas/contracts/v1/common/spatial_geometry.schema.json
  - ../../../fixtures/contracts/v1/common/spatial_geometry/
  - ../../../policy/common/
  - ../../../policy/sensitivity/
  - ../../../policy/geoprivacy/
  - ../../../docs/architecture/contract-schema-policy-split.md
  - ../../../data/proofs/
  - ../../../data/receipts/
  - ../../../release/
notes:
  - "This README replaces an empty file. It does not confirm executable validator behavior."
  - "The common SpatialGeometry contract says spatial_geometry is a geometry carrier with geometry, CRS, and precision_bucket. It is not a map-rendering instruction, CRS transformation engine, geocoder, proof of survey accuracy, or permission to expose sensitive locations."
  - "The declared validator tools/validators/validate_spatial_geometry.py exists, but current repo evidence shows it is a greenfield placeholder that raises NotImplementedError."
  - "Domain contracts own what the geometry means. This shared geometry validator must check common carrier posture and delegate domain-specific sensitivity, rights, policy, release, and public-safe transform decisions to owning roots."
  - "This lane must not publish geometry, transform CRS by itself, store geometry payloads, create receipts, decide policy, approve release, or authorize public display."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/geometry

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-geometry--validator-informational)
![posture](https://img.shields.io/badge/posture-fail--closed-critical)
![implementation](https://img.shields.io/badge/implementation-placeholder-red)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/geometry/` is the proposed shared validator lane for common geometry-carrier checks: geometry shape, CRS, precision bucket, geometry role, validity/topology posture, geoprivacy/sensitivity linkage, evidence, policy, release, correction, rollback, and public-surface denial.

---

## Purpose

`tools/validators/geometry/` exists for shared geometry validation concerns under the durable `tools/validators/` surface.

The durable KFM question for this lane is:

> Does a geometry-bearing candidate preserve a valid common geometry carrier, declared CRS, precision/exposure posture, geometry role, spatial uncertainty, scale caveats, sensitivity/geoprivacy posture, EvidenceRef/EvidenceBundle support, policy/review state, release linkage, correction lineage, rollback target, and public-surface denial before it reaches catalog, proof, release, map, API, graph, Focus Mode, export, or AI surfaces?

The answer should be a deterministic validation result. This folder should not define geometry semantics for a domain object, transform CRS by itself, geocode, store source geometry, store public geometry, create RedactionReceipts, create EvidenceBundles, store proofs, store receipts, decide policy, approve release, publish map layers, expose public API payloads, or authorize AI answers.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/geometry/README.md` | **CONFIRMED** | This README replaces the previous empty file. |
| Common SpatialGeometry contract | **CONFIRMED in repo evidence / draft** | `contracts/common/spatial_geometry.md` defines `spatial_geometry` as a compact carrier binding geometry, CRS, and precision bucket. |
| Paired spatial geometry schema | **CONFIRMED in repo evidence / proposed** | The common contract points to `schemas/contracts/v1/common/spatial_geometry.schema.json`; fixture coverage and downstream usage remain NEEDS VERIFICATION. |
| Declared legacy validator file | **CONFIRMED placeholder / NEEDS IMPLEMENTATION** | `tools/validators/validate_spatial_geometry.py` exists but raises `NotImplementedError`. |
| Domain-specific geometry gates | **CONFIRMED README examples / executable NEEDS VERIFICATION** | `tools/validators/geology/public_safe_geometry/README.md` is a domain-specific public-safe geometry gate and should not be replaced by this shared lane. |
| Shared geometry executable, report schema, fixtures, policy bundles, receipt emission, runtime behavior, and CI wiring | **NEEDS VERIFICATION** | This README does not claim implemented validator behavior, runtime routing, or CI enforcement. |

[Back to top](#top)

---

## Relationship to nearby lanes

| Concern | Preferred home |
|---|---|
| Shared geometry validator lane | `tools/validators/geometry/` |
| Existing placeholder validator file | `tools/validators/validate_spatial_geometry.py` |
| Shared validator plumbing | `tools/validators/_common/` |
| Domain-specific public-safe geometry | `tools/validators/geology/public_safe_geometry/` and future domain lanes |
| Cross-domain geometry joins | `tools/validators/cross-domain-joins/` |
| SpatialGeometry semantics | `contracts/common/spatial_geometry.md` |
| SpatialGeometry machine shape | `schemas/contracts/v1/common/spatial_geometry.schema.json` |
| Domain meaning of located things | `docs/domains/`, `contracts/domains/` |
| Policy and geoprivacy | `policy/common/`, `policy/sensitivity/`, `policy/geoprivacy/`, or accepted policy homes |
| Proofs, receipts, release | `data/proofs/`, `data/receipts/`, `release/` |

This README does not move, replace, or override those roots. It only defines where shared geometry validation may be documented or implemented after verification.

[Back to top](#top)

---

## Proposed validation focus

Until executable behavior and field-level schema bindings are verified, this README treats the following as proposed validation concepts:

| Concept | Validator question | Must not be treated as |
|---|---|---|
| Geometry carrier | Is the geometry payload present in the accepted common shape? | Domain meaning or claim truth. |
| CRS | Is coordinate reference explicit, valid for the payload, and not assumed from context? | CRS transformation by validation alone. |
| Precision bucket | Is precision/exposure posture declared and compatible with the requested use? | Policy approval or survey accuracy. |
| Geometry role | Is geometry exact, internal, generalized, redacted, aggregated, suppressed, public-safe, or denied? | Public display permission by default. |
| Validity/topology | Are geometry type, rings, self-intersections, empty geometries, dimensionality, bounds, and topology caveats acceptable for the requested stage? | Release readiness by itself. |
| Spatial uncertainty and scale | Are uncertainty, source scale, source resolution, simplification, clipping, tiling, and precision loss visible when material? | Proof of accuracy. |
| Sensitivity/geoprivacy | Do location exposure, redaction, generalization, aggregation, and most-restrictive-policy needs route to policy gates? | A local decision in this validator. |
| Evidence/release posture | Are EvidenceRefs, EvidenceBundles, ReviewRecords, PolicyDecisions, ReleaseManifests, correction paths, and rollback targets present before public use? | Publication by validation alone. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Shared geometry validator lane | `tools/validators/geometry/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Existing placeholder validator script | `tools/validators/validate_spatial_geometry.py` |
| SpatialGeometry contract | `contracts/common/spatial_geometry.md` |
| SpatialGeometry schema | `schemas/contracts/v1/common/spatial_geometry.schema.json` |
| Domain geometry meaning | `docs/domains/`, `contracts/domains/` |
| Domain-specific public-safe geometry gates | `tools/validators/<domain>/`, `tools/validators/domains/<domain>/`, or accepted domain validator homes |
| Policy/admissibility/geoprivacy | `policy/common/`, `policy/sensitivity/`, `policy/geoprivacy/`, `policy/` |
| Evidence/proof support | `data/proofs/` |
| Receipts | `data/receipts/` |
| Release decisions, correction, rollback, withdrawal | `release/` |
| Tests and fixtures | `tests/validators/geometry/`, `fixtures/contracts/v1/common/spatial_geometry/`, `tests/common/`, or accepted conventions |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **CONFIRMED AS PLACEHOLDER:** `tools/validators/validate_spatial_geometry.py` exists but currently raises `NotImplementedError`.
- **PROPOSED:** validator code may live here when it checks declared common geometry-carrier, CRS, precision, topology, sensitivity, evidence, policy, release, correction, and public-surface rules and writes reports/receipts only to accepted roots.
- **NEEDS VERIFICATION:** exact executable names, schema bindings, geometry libraries, CRS registry, precision-bucket vocabulary, geometry-role vocabulary, fixture shape, report destinations, receipt emission, package integration, policy enforcement, release integration, runtime behavior, and CI wiring.
- **DENY:** using this folder as geometry semantics, domain doctrine, CRS transformation engine, geocoder, source geometry store, public geometry store, schema home, proof storage, receipt storage, policy home, release record store, public runtime surface, AI answer authority, or publication authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/geometry/` include checks that:

- verify common `spatial_geometry` candidates include accepted geometry, CRS, and precision/exposure posture;
- verify geometry type, dimensionality, empty geometry state, ring validity, topology posture, bounds, and coordinate plausibility are acceptable for the requested stage;
- verify CRS is explicit and not silently assumed;
- verify public-bound geometry routes through sensitivity/geoprivacy/public-safe geometry gates before display;
- verify geometry role, source scale, source resolution, uncertainty, simplification, clipping, tiling, and transform caveats remain visible;
- verify domain-specific exact-location restrictions are delegated to the owning domain validator/policy lane;
- emit deterministic findings for downstream review without storing geometry payloads, transform receipts, proof artifacts, or approving release.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/geometry/` | Correct home |
|---|---|
| SpatialGeometry meaning | `contracts/common/spatial_geometry.md` |
| SpatialGeometry schema/enums | `schemas/contracts/v1/common/spatial_geometry.schema.json` |
| Domain object meaning for the located thing | `docs/domains/`, `contracts/domains/` |
| Domain-specific public-safe geometry policy | domain validator and policy lanes |
| Source geometry, transformed geometry payloads, tiles, layers, or public map artifacts | dedicated `data/` lifecycle roots and governed release/published roots |
| CRS transformation implementation, geocoding, topology repair, simplification, tiling, or geometry helper packages | `packages/`, `pipelines/`, or accepted implementation roots |
| Policy rules and sensitivity/geoprivacy decisions | `policy/` |
| EvidenceBundles, proofs, receipts, validation reports, redaction receipts, aggregation receipts | `data/proofs/`, `data/receipts/` |
| Release manifests, correction notices, rollback cards, withdrawals | `release/` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| Public API, UI, map, tile, export, search, graph, Focus Mode, AI runtime output, legal/survey/engineering determinations, or publication output | governed application/runtime roots |
| Generated QA reports that are not source code | `artifacts/qa/` or accepted report lane |
| Tests and fixtures | `tests/` and fixture conventions |

[Back to top](#top)

---

## Geometry validator posture

Geometry validators must fail closed, deny, abstain, hold, or route to review when a candidate:

- lacks required geometry, CRS, precision bucket, geometry role, EvidenceRef, EvidenceBundle/proof reference, sensitivity posture, policy posture, review state, release reference, correction path, or rollback target required for its use;
- silently assumes CRS, coordinate order, units, precision, or public-safe exposure;
- treats precision bucket as proof of survey accuracy, source authority, policy approval, or release approval;
- treats a geometry carrier as proof of the underlying domain claim;
- exposes exact or sensitive location detail to a public-bound surface without the owning domain's public-safe transform, receipt, review, policy, release, correction, and rollback support;
- hides uncertainty, source scale, source resolution, CRS, topology caveats, simplification, clipping, tiling, redaction, aggregation, or precision loss that materially affects interpretation;
- allows catalog, proof, release, map, API, graph, Focus Mode, export, or AI surfaces to depend on geometry-incomplete or public-safe-geometry-incomplete candidates;
- points public surfaces at RAW, WORK, QUARANTINE, unresolved candidates, direct internal stores, direct model outputs, stale source descriptors, exact sensitive geometry, or incomplete proof closure;
- treats geometry validation as SourceDescriptor creation, EvidenceBundle creation, RedactionReceipt creation, PolicyDecision creation, release approval, publication, public API behavior, survey/legal/engineering determination, or AI answer authority.

The validator lane must preserve the KFM lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `GEOMETRY_VALIDATOR_PASS` | Configured shared geometry checks passed. |
| `GEOMETRY_VALIDATOR_FAIL` | One or more configured shared geometry checks failed. |
| `GEOMETRY_MISSING` | Required geometry payload is absent. |
| `GEOMETRY_SCHEMA_INVALID` | Candidate does not satisfy accepted common geometry schema. |
| `CRS_MISSING` | Required CRS declaration is absent. |
| `CRS_UNSUPPORTED` | CRS is not accepted for the requested stage or cannot be interpreted safely. |
| `COORDINATE_ORDER_RISK` | Coordinate order or units are ambiguous or unsafe. |
| `PRECISION_BUCKET_MISSING` | Required precision/exposure posture is absent. |
| `GEOMETRY_ROLE_MISSING` | Required geometry role is absent. |
| `GEOMETRY_EMPTY_OR_INVALID` | Geometry is empty, malformed, topologically invalid, or unsupported. |
| `GEOMETRY_BOUNDS_RISK` | Coordinates fall outside expected bounds or domain extent. |
| `SPATIAL_UNCERTAINTY_GAP` | Required uncertainty, scale, precision, or source-resolution posture is absent. |
| `PUBLIC_SAFE_GEOMETRY_GAP` | Required public-safe transform, receipt, policy, release, or domain gate is absent. |
| `SENSITIVE_LOCATION_EXPOSURE_DENIED` | Candidate exposes sensitive location detail without approved public-safe support. |
| `EVIDENCE_REF_MISSING` | Required EvidenceRef, EvidenceBundle, or proof reference is absent. |
| `POLICY_OR_RELEASE_GAP` | Required policy, review, release, correction, or rollback support is absent. |
| `PUBLIC_SURFACE_LEAK_RISK` | Candidate is unsafe for public/governed output as shaped. |
| `REPORT_DESTINATION_INVALID` | QA report or receipt destination is outside an accepted root. |
| `ABSTAIN` | Validator cannot decide safely with available context. |
| `DENY` | Candidate is explicitly disallowed for the requested use. |
| `HOLD` | Candidate requires steward review, geometry repair, public-safe transform, evidence closure, quarantine, or release closure before use. |
| `ERROR` | Validator could not safely complete. |

[Back to top](#top)

---

## Validation

Suggested future test surface:

```text
tests/validators/geometry/
├── README.md
├── test_geometry_validator.py
└── fixtures/
    ├── valid_spatial_geometry_point/
    ├── valid_spatial_geometry_polygon/
    ├── missing_geometry/
    ├── missing_crs/
    ├── unsupported_crs/
    ├── coordinate_order_risk/
    ├── missing_precision_bucket/
    ├── invalid_topology/
    ├── bounds_risk/
    ├── spatial_uncertainty_gap/
    └── sensitive_location_exposure_denied/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/geometry
```

```bash
python tools/validators/geometry/validate_geometry.py --repo-root . --format json
```

> [!NOTE]
> This is a proposed interface, not proof that `validate_geometry.py` exists here. Current repo evidence confirms only `tools/validators/validate_spatial_geometry.py`, and that file is a placeholder that raises `NotImplementedError`.

[Back to top](#top)

---

## Review checklist

- [ ] Validator reads declared common geometry contracts, schemas, fixtures, policy, evidence records, release records, and correction/rollback records rather than defining meaning locally.
- [ ] Domain-specific meaning of the located thing remains in domain contracts/docs.
- [ ] CRS, coordinate order, units, precision bucket, geometry role, uncertainty, source scale, source resolution, topology, simplification, clipping, and tiling posture remain visible.
- [ ] Precision bucket is not treated as survey proof, policy approval, or release approval.
- [ ] Sensitive-location exposure routes to domain-specific public-safe geometry and geoprivacy policy lanes.
- [ ] Public-bound outputs never point clients at RAW, WORK, QUARANTINE, unresolved candidates, direct internal stores, direct model outputs, stale source descriptors, exact sensitive geometry, public-safe-transform-incomplete candidates, or incomplete proof closure.
- [ ] Reports and receipts are written only to accepted roots.
- [ ] Validator output is not described as truth, transform receipt, policy approval, release, publication, source admission, geometry authority, survey authority, legal authority, engineering authority, or Directory Rules approval.
- [ ] Tests use public-safe or synthetic fixtures.
- [ ] Executable claims are backed by current repo evidence.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-08 |
| Review state | Draft README replacement for empty shared Geometry validator file. |
| Next smallest safe change | Decide whether to implement `tools/validators/geometry/validate_geometry.py`, replace/forward `tools/validators/validate_spatial_geometry.py`, or preserve both with a compatibility note; then verify schema binding, fixture coverage, CRS/geometry libraries, precision-bucket vocabulary, report destination, receipt emission, policy enforcement, release linkage, and CI/runtime wiring before promoting this lane beyond draft. |
