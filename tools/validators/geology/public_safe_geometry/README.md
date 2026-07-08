<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-geology-public-safe-geometry-readme
title: tools/validators/geology/public_safe_geometry README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-geology-steward-plus-geometry-steward-plus-sensitivity-reviewer-plus-redaction-steward-plus-evidence-steward-plus-policy-steward-plus-release-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; geology-validator; public-safe-geometry; exact-location-sensitive; redaction; generalization; aggregation; geometry-role-aware; fail-closed; release-gated; non-authoritative
owning_root: tools/
responsibility: proposed Geology public-safe-geometry validator lane for checking geometry role separation, exact/internal geometry denial, public-safe generalized geometry, CRS and topology posture, spatial uncertainty, redaction/generalization/aggregation receipt posture, sensitive subsurface/resource-location exposure, borehole/sample/private-well/resource-targeting denial, EvidenceRef/EvidenceBundle linkage, policy/review/release linkage, correction and rollback linkage, and public-surface denial checks while deferring Geology meaning, geometry helper implementation, source registry authority, policy decisions, evidence records, proof records, receipts, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../../README.md
  - ../../_common/README.md
  - ../../domains/geology/README.md
  - ../borehole_rights/README.md
  - ../../cross-domain-joins/README.md
  - ../../evidence/README.md
  - ../../citation/README.md
  - ../../evidence_bundle/README.md
  - ../../../../packages/domains/geology/geometry/README.md
  - ../../../../packages/domains/geology/layer_manifest/README.md
  - ../../../../docs/domains/geology/README.md
  - ../../../../docs/domains/geology/POLICY.md
  - ../../../../docs/domains/geology/SENSITIVITY.md
  - ../../../../docs/domains/geology/PRESERVATION_MATRIX.md
  - ../../../../docs/domains/geology/MAP_UI_CONTRACTS.md
  - ../../../../contracts/domains/geology/
  - ../../../../schemas/contracts/v1/domains/geology/
  - ../../../../schemas/contracts/v1/receipts/
  - ../../../../policy/domains/geology/
  - ../../../../policy/sensitivity/geology/
  - ../../../../policy/geoprivacy/
  - ../../../../data/registry/sensitivity/geology/README.md
  - ../../../../data/registry/sources/geology/
  - ../../../../data/proofs/geology/
  - ../../../../data/proofs/
  - ../../../../data/receipts/
  - ../../../../release/
notes:
  - "This README replaces an empty file. It does not confirm executable files."
  - "Geology geometry package evidence says exact/internal geometry must remain separate from public-safe geometry, and that geometry helpers must not publish geometry, decide release, own canonical source geometry, or treat public display geometry as proof."
  - "Geology sensitivity registry evidence says exact subsurface point data, borehole/well-log/core/private-well/geochem sample detail, extraction-targetable resource detail, rights-restricted content, and private-parcel/operator joins fail closed unless governed redaction/review/release gates close."
  - "Geology policy and validator evidence say exact borehole, sample, sensitive-resource, well-log, and private-well locations default to restricted/generalized public geometry and require public-safe transforms, review, evidence, policy, release, correction, and rollback support before exposure."
  - "This validator lane must not decide policy, perform release, create receipts, define geometry semantics, certify exact geometry, or publish public geometry."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/geology/public_safe_geometry

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-public--safe--geometry--validator-informational)
![sensitivity](https://img.shields.io/badge/sensitivity-exact--geometry--deny--default-critical)
![posture](https://img.shields.io/badge/posture-redaction--receipt--aware-blueviolet)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/geology/public_safe_geometry/` is the proposed validator lane for checking whether Geology geometry has been transformed, receipted, reviewed, policy-gated, and release-linked enough to be safe for the requested public or governed surface.

---

## Purpose

`tools/validators/geology/public_safe_geometry/` exists for Geology public-safe geometry checks under the durable `tools/validators/` surface.

The durable KFM question for this lane is:

> Does a Geology geometry candidate preserve exact/internal geometry separation, public-safe geometry role, CRS/topology sanity, spatial uncertainty, source role, sensitivity tier, redaction/generalization/aggregation receipt posture, EvidenceRef/EvidenceBundle support, policy/review state, release linkage, correction lineage, rollback target, and public-surface denial before it reaches catalog, proof, release, map, API, graph, Focus Mode, export, or AI surfaces?

The answer should be a deterministic validation result. This folder should not create Geology truth, define geometry semantics, perform geometry transforms by itself, store exact geometry, create RedactionReceipts, create EvidenceBundles, store proofs, store receipts, decide policy, approve release, publish map layers, expose public API payloads, or authorize AI answers.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/geology/public_safe_geometry/README.md` | **CONFIRMED** | This README replaces the previous empty file. |
| Per-domain Geology validator index | **CONFIRMED README / executable NEEDS VERIFICATION** | The Geology validator index names exact subsurface/resource-location sensitivity, public-safe transforms, evidence, policy, release, correction, rollback, and public-surface denial as validator concerns. |
| Geology geometry package | **CONFIRMED README / implementation NEEDS VERIFICATION** | The package README describes proposed geometry helpers and states exact/internal geometry must remain separate from public-safe geometry. It does not prove implementation behavior. |
| Geology sensitivity registry | **CONFIRMED in repo evidence / draft** | The registry README defines exact subsurface point, borehole/well-log/core/private-well/geochem sample detail, extraction-targetable resource detail, rights-restricted source content, private-parcel/operator joins, redaction receipts, and fail-closed release gating. |
| Public-safe geometry executable, schemas, fixtures, policy bundles, receipt emission, runtime behavior, and CI wiring | **NEEDS VERIFICATION** | This README does not claim a validator script, schema, fixture set, transform implementation, receipt path, runtime route, or CI check exists. |

[Back to top](#top)

---

## Relationship to nearby lanes

| Concern | Preferred home |
|---|---|
| Public-safe geometry validator lane | `tools/validators/geology/public_safe_geometry/` |
| Borehole rights and exact subsurface rights gate | `tools/validators/geology/borehole_rights/` |
| Per-domain Geology validator index | `tools/validators/domains/geology/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Geometry helper implementation | `packages/domains/geology/geometry/` |
| Layer manifest helper implementation | `packages/domains/geology/layer_manifest/` |
| Geology meaning and contracts | `docs/domains/geology/`, `contracts/domains/geology/` |
| Geology and receipt schemas | `schemas/contracts/v1/domains/geology/`, `schemas/contracts/v1/receipts/` |
| Sensitivity registry and policy | `data/registry/sensitivity/geology/`, `policy/domains/geology/`, `policy/sensitivity/geology/`, `policy/geoprivacy/` |
| Source descriptors | `data/registry/sources/geology/` |
| Proofs, receipts, release | `data/proofs/geology/`, `data/proofs/`, `data/receipts/`, `release/` |

This README does not move, replace, or override those roots. It only defines where public-safe geometry validation may be documented or implemented after verification.

[Back to top](#top)

---

## Proposed validation focus

Until executable behavior and field-level schemas are verified, this README treats the following as proposed validation concepts:

| Concept | Validator question | Must not be treated as |
|---|---|---|
| Geometry role | Is the geometry marked as exact/internal, generalized, redacted, aggregated, suppressed, public-safe, or denied? | Public-safe display by default. |
| Exact/internal separation | Is exact source geometry kept out of public-bound payloads and maps? | Public layer geometry. |
| Transform receipt | Is a RedactionReceipt, AggregationReceipt, generalization receipt, geometry-suppression record, or equivalent present when geometry is transformed? | Untracked cartographic simplification. |
| Spatial uncertainty | Are uncertainty, scale, source resolution, and known precision limits preserved? | Precision proof or claim truth. |
| CRS and topology posture | Are CRS, geometry type, validity, simplification, clipping, tiling, and topology caveats visible where required? | Release readiness by itself. |
| Sensitive subsurface/resource detail | Could the geometry expose boreholes, cores, samples, private wells, geochemistry, well logs, or extraction-targetable resources? | Public release without review/policy gates. |
| Cross-domain joins | Could joins to people/parcels, infrastructure, hydrology, archaeology, or habitat increase sensitivity? | Geometry-only decision. |
| Evidence/release posture | Are EvidenceRefs, EvidenceBundles, review records, PolicyDecisions, ReleaseManifests, correction paths, and rollback targets present before public use? | Publication by validation alone. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Public-safe geometry validator lane | `tools/validators/geology/public_safe_geometry/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Geology validator index | `tools/validators/domains/geology/` |
| Borehole-rights validator | `tools/validators/geology/borehole_rights/` |
| Geometry helper implementation | `packages/domains/geology/geometry/` |
| Geology doctrine and contracts | `docs/domains/geology/`, `contracts/domains/geology/` |
| Source descriptors | `data/registry/sources/geology/` or accepted source-registry home |
| Sensitivity registry and policy | `data/registry/sensitivity/geology/`, `policy/domains/geology/`, `policy/sensitivity/geology/`, `policy/geoprivacy/` |
| Source, Geology, and receipt schemas | `schemas/contracts/v1/source/`, `schemas/contracts/v1/domains/geology/`, `schemas/contracts/v1/receipts/` |
| Evidence/proof support | `data/proofs/geology/`, `data/proofs/` |
| Receipts | `data/receipts/` |
| Release decisions, correction, rollback, withdrawal | `release/` |
| Tests and fixtures | `tests/validators/geology/public_safe_geometry/`, `tests/domains/geology/`, `fixtures/domains/geology/`, or accepted conventions |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live here when it checks declared public-safe geometry, sensitivity, transform-receipt, evidence, policy, release, correction, and public-surface rules and writes reports/receipts only to accepted roots.
- **NEEDS VERIFICATION:** exact executable names, accepted schemas, geometry-role vocabulary, transform receipt shapes, fixtures, report destinations, receipt emission, package integration, policy enforcement, release integration, runtime behavior, and CI wiring.
- **DENY:** using this folder as Geology doctrine, geometry semantics, geometry helper implementation, exact geometry storage, source registry, schema home, proof storage, receipt storage, policy home, release record store, public runtime surface, AI answer authority, or publication authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/geology/public_safe_geometry/` include checks that:

- verify public-bound Geology geometries are explicitly marked public-safe or fail closed;
- verify exact/internal geometry is absent from public-bound payloads and maps;
- verify borehole, core, well-log, private-well, sample, geochemistry, and extraction-targetable resource geometry has been redacted, generalized, aggregated, suppressed, or denied according to policy;
- verify RedactionReceipt, AggregationReceipt, geometry-suppression receipt, ReviewRecord, PolicyDecision, ReleaseManifest, correction path, and rollback target exist where required;
- verify CRS, geometry type, simplification, clipping, tiling, scale, uncertainty, and source resolution posture are visible before release review;
- verify cross-domain joins do not make geometry sensitive through person-parcel, infrastructure, archaeology, hydrology, habitat, or other sensitive joins;
- emit deterministic findings for downstream review without storing geometry payloads, transform receipts, proof artifacts, or approving release.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/geology/public_safe_geometry/` | Correct home |
|---|---|
| Geology doctrine, object-family meaning, geometry semantics | `docs/domains/geology/`, `contracts/domains/geology/` |
| Geometry helper implementation | `packages/domains/geology/geometry/` |
| SourceDescriptor records or source registry records | `data/registry/sources/geology/` |
| Exact geometry, transformed geometry payloads, or public tiles/layers | dedicated `data/` lifecycle roots and governed published/release roots |
| Sensitivity registry records or policy bundles | `data/registry/sensitivity/geology/`, `policy/` |
| Schemas and controlled vocabularies | `schemas/contracts/v1/source/`, `schemas/contracts/v1/domains/geology/`, `schemas/contracts/v1/receipts/` |
| EvidenceBundles, proofs, receipts, validation reports, redaction receipts | `data/proofs/`, `data/receipts/` |
| Release manifests, correction notices, rollback cards, withdrawals | `release/` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| Public API, UI, map, tile, export, search, graph, Focus Mode, AI runtime output, extraction guidance, legal/title/lease/permit determinations, engineering recommendations, or publication output | governed application/runtime roots |
| Generated QA reports that are not source code | `artifacts/qa/` or accepted report lane |
| Tests and fixtures | `tests/` and fixture conventions |

[Back to top](#top)

---

## Public-safe geometry validator posture

Public-safe geometry validators must fail closed, deny, abstain, hold, or route to review when a candidate:

- lacks geometry role, source descriptor linkage, source role, sensitivity tier, EvidenceRef, EvidenceBundle/proof reference, transform receipt, policy posture, review state, release reference, correction path, or rollback target required for its use;
- exposes exact/internal borehole, core, sample, well-log, private-well, geochemistry, sensitive-resource, or extraction-targetable geometry to a public-bound surface;
- uses generalized, redacted, aggregated, or suppressed geometry without a receipt and explanation of the transform;
- treats public display geometry as proof of exact source geometry, Geology truth, reserve estimate, resource truth, drilling guidance, or ownership/title/lease/permit truth;
- hides uncertainty, source scale, source resolution, CRS, topology caveats, or geometry simplification/clipping/tiling changes that materially affect interpretation;
- allows person-parcel, infrastructure, hydrology, archaeology, habitat, resource, or rights joins to raise sensitivity without most-restrictive-policy propagation;
- allows catalog, proof, release, map, API, graph, Focus Mode, export, or AI surfaces to depend on public-safe-geometry-incomplete candidates;
- points public surfaces at RAW, WORK, QUARANTINE, unresolved candidates, direct internal stores, direct model outputs, stale source descriptors, exact sensitive geometry, or incomplete proof closure;
- treats public-safe geometry validation as SourceDescriptor creation, EvidenceBundle creation, RedactionReceipt creation, PolicyDecision creation, release approval, publication, public API behavior, or AI answer authority.

The validator lane must preserve the KFM lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `PUBLIC_SAFE_GEOMETRY_PASS` | Configured public-safe geometry checks passed. |
| `PUBLIC_SAFE_GEOMETRY_FAIL` | One or more configured public-safe geometry checks failed. |
| `GEOMETRY_ROLE_MISSING` | Required geometry role is absent. |
| `GEOMETRY_SOURCE_DESCRIPTOR_MISSING` | Required SourceDescriptor or source-registry pointer is absent. |
| `GEOMETRY_SENSITIVITY_TIER_MISSING` | Required sensitivity tier or public-use posture is absent. |
| `EXACT_GEOMETRY_EXPOSURE_DENIED` | Exact/internal sensitive geometry is unsafe for the requested surface. |
| `PUBLIC_SAFE_TRANSFORM_MISSING` | Required redaction, generalization, aggregation, suppression, or public-safe transform is absent. |
| `GEOMETRY_TRANSFORM_RECEIPT_MISSING` | Required transform receipt is absent. |
| `SPATIAL_UNCERTAINTY_GAP` | Required uncertainty, scale, precision, or source-resolution posture is absent. |
| `CRS_OR_TOPOLOGY_GAP` | Required CRS, geometry validity, topology, simplification, clipping, tiling, or geometry-type posture is incomplete. |
| `RESOURCE_TARGETING_GEOMETRY_RISK` | Geometry could enable extraction-targeting harm or sensitive resource exploitation. |
| `MOST_RESTRICTIVE_POLICY_GAP` | Sensitive cross-domain join does not propagate the most restrictive applicable policy. |
| `EVIDENCE_REF_MISSING` | Required EvidenceRef, EvidenceBundle, or proof reference is absent. |
| `POLICY_OR_RELEASE_GAP` | Required policy, review, release, correction, or rollback support is absent. |
| `PUBLIC_SURFACE_LEAK_RISK` | Candidate is unsafe for public/governed output as shaped. |
| `REPORT_DESTINATION_INVALID` | QA report or receipt destination is outside an accepted root. |
| `ABSTAIN` | Validator cannot decide safely with available context. |
| `DENY` | Candidate is explicitly disallowed for the requested use. |
| `HOLD` | Candidate requires steward review, transform receipt, source admission, evidence closure, quarantine, or release closure before use. |
| `ERROR` | Validator could not safely complete. |

[Back to top](#top)

---

## Validation

Suggested future test surface:

```text
tests/validators/geology/public_safe_geometry/
├── README.md
├── test_public_safe_geometry_validator.py
└── fixtures/
    ├── valid_public_safe_geologic_map_polygon/
    ├── valid_generalized_borehole_summary/
    ├── missing_geometry_role/
    ├── exact_geometry_exposure_denied/
    ├── missing_transform_receipt/
    ├── spatial_uncertainty_gap/
    ├── crs_or_topology_gap/
    ├── resource_targeting_geometry_risk/
    ├── most_restrictive_policy_gap/
    └── policy_or_release_gap/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/geology/public_safe_geometry
```

```bash
python tools/validators/geology/public_safe_geometry/validate_public_safe_geometry.py --repo-root . --format json
```

> [!NOTE]
> This is a proposed interface, not proof that `validate_public_safe_geometry.py` or the test path exists here.

[Back to top](#top)

---

## Review checklist

- [ ] Validator reads declared Geology contracts, schemas, source descriptors, sensitivity registry records, policy, transform receipts, evidence records, release records, and correction/rollback records rather than defining meaning locally.
- [ ] Exact/internal and public-safe geometry roles remain separate.
- [ ] Redaction/generalization/aggregation/suppression receipts are required before public-bound sensitive geometry is accepted.
- [ ] Public display geometry is not treated as exact source geometry or proof of the underlying claim.
- [ ] Spatial uncertainty, CRS, topology, simplification, clipping, tiling, source scale, and source resolution remain visible where material.
- [ ] Most-restrictive-policy propagation applies across person-parcel, infrastructure, archaeology, hydrology, habitat, resource, or rights joins.
- [ ] Public-bound outputs never point clients at RAW, WORK, QUARANTINE, unresolved candidates, direct internal stores, direct model outputs, stale source descriptors, exact sensitive geometry, transform-incomplete candidates, or incomplete proof closure.
- [ ] Reports and receipts are written only to accepted roots.
- [ ] Validator output is not described as truth, transform receipt, policy approval, release, publication, source admission, geometry authority, mineral-rights authority, title authority, engineering authority, extraction guidance, or Directory Rules approval.
- [ ] Tests use public-safe or synthetic fixtures.
- [ ] Executable claims are backed by current repo evidence.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-08 |
| Review state | Draft README replacement for empty Geology public-safe-geometry validator file. |
| Next smallest safe change | Verify actual public-safe geometry validator script path, accepted Geology/source/receipt schemas, geometry-role vocabulary, transform receipt shapes, sensitivity-tier binding, fixtures, report destination, receipt emission, package integration, policy enforcement, release linkage, and CI/runtime wiring before promoting this lane beyond draft. |
