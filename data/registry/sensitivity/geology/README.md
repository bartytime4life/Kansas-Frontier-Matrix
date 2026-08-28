<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/sensitivity/geology/readme
name: Geology Sensitivity Registry README
path: data/registry/sensitivity/geology/README.md
type: data-registry-sensitivity-domain-readme
version: v0.2.0
status: draft
owners:
  - <registry-steward>
  - <sensitivity-steward>
  - <geology-domain-steward>
  - <natural-resources-steward>
  - <rights-holder-representative>
  - <policy-steward>
  - <redaction-steward>
  - <proof-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: registry
registry_scope: geology-sensitivity-registry-records
domain: geology
path_posture: existing-empty-placeholder-replaced; sensitivity-registry-parent-currently-greenfield-stub; subtype-first-sensitivity-registry-path-confirmed; concrete-records-unknown
sensitivity_posture: registry-internal; no-public-path; exact-subsurface-point-t4-default; borehole-welllog-core-privatewell-geochem-sample-detail-fail-closed; extraction-targetable-resource-detail-reviewed; rights-restricted-source-content-fail-closed; private-parcel-operator-joins-fail-closed; interpretive-surfaces-require-reality-boundary; redaction-receipt-required; source-role-preserving; evidence-aware; rights-aware; policy-aware; release-blocked-until-gates-close
related:
  - ../README.md
  - ../../README.md
  - ../../sources/README.md
  - ../../sources/geology/
  - ../../geology/README.md
  - ../../geology/sources/README.md
  - ../../rights/README.md
  - ../../domains/README.md
  - ../../datasets/README.md
  - ../../crosswalks/README.md
  - ../../layers/README.md
  - ../../../raw/geology/
  - ../../../work/geology/
  - ../../../quarantine/geology/
  - ../../../processed/geology/README.md
  - ../../../catalog/domain/geology/
  - ../../../published/layers/geology/
  - ../../../receipts/
  - ../../../proofs/
  - ../../../../docs/domains/geology/SENSITIVITY.md
  - ../../../../docs/domains/geology/POLICY.md
  - ../../../../docs/domains/geology/PRESERVATION_MATRIX.md
  - ../../../../docs/domains/geology/RELEASE_INDEX.md
  - ../../../../docs/domains/geology/SCOPE.md
  - ../../../../docs/domains/geology/SOURCE_REGISTRY.md
  - ../../../../docs/domains/geology/SOURCES.md
  - ../../../../docs/domains/geology/SOURCE_LEDGER.md
  - ../../../../docs/domains/geology/SOURCE_ROLE_MATRIX.md
  - ../../../../docs/domains/geology/DATA_LIFECYCLE.md
  - ../../../../docs/architecture/sensitivity.md
  - ../../../../docs/sources/catalog/usgs/usgs-ngmdb.md
  - ../../../../docs/sources/catalog/usgs/usgs-mrds.md
  - ../../../../contracts/domains/geology/
  - ../../../../schemas/contracts/v1/domains/geology/
  - ../../../../schemas/contracts/v1/receipts/
  - ../../../../policy/domains/geology/
  - ../../../../policy/sensitivity/geology/
  - ../../../../policy/geoprivacy/
  - ../../../../policy/rights/
  - ../../../../release/
tags:
  - kfm
  - data
  - registry
  - sensitivity
  - geology
  - natural-resources
  - deny-by-default
  - t4
  - geoprivacy
  - redaction
  - RedactionReceipt
  - boreholes
  - well-logs
  - cores
  - private-wells
  - geochem-samples
  - mineral-resources
  - deposits
  - extraction-targetable
  - subsurface
  - private-parcel-joins
  - interpretive-surfaces
  - RealityBoundaryNote
  - source-role
  - evidence
  - provenance
  - release-gated
  - no-public-path
notes:
  - "This README replaces the empty placeholder at `data/registry/sensitivity/geology/README.md`."
  - "The parent `data/registry/sensitivity/README.md` is currently a greenfield stub, so sensitivity-registry topology and canonical record shape remain NEEDS VERIFICATION."
  - "Geology sensitivity registry records are registry/control records. They do not store source payloads, reveal exact sensitive subsurface/resource locations, define policy, enforce schemas, hold receipts/proofs, close catalogs, or publish artifacts."
  - "Geology sensitivity doctrine notes no explicit geology row in the sensitive-domain matrix; the most restrictive applicable row and default deny/generalize/review posture govern until ratified."
  - "Exact borehole/core/private-well/geochem sample locations, extraction-targetable resource detail, rights-restricted source content, private-parcel/operator joins, and uncertain source material fail closed unless governed redaction/review/release gates close."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Geology Sensitivity Registry

Subtype-first sensitivity-registry lane for Geology and Natural Resources sensitivity-control records and release-readiness pointers.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: registry" src="https://img.shields.io/badge/family-registry-blueviolet">
  <img alt="Domain: geology" src="https://img.shields.io/badge/domain-geology-795548">
  <img alt="Lane: sensitivity" src="https://img.shields.io/badge/lane-sensitivity-blue">
  <img alt="Default: deny exact subsurface" src="https://img.shields.io/badge/default-deny%20exact%20subsurface-critical">
  <img alt="Exposure: no public path" src="https://img.shields.io/badge/exposure-no%20public%20path-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Geology sensitivity boundary](#geology-sensitivity-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Suggested directory shape](#suggested-directory-shape) · [Suggested registry shape](#suggested-registry-shape) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/registry/sensitivity/geology/` is a registry lane for Geology sensitivity-control records and sensitivity-readiness pointers. It is not RAW source storage, WORK staging, QUARANTINE, PROCESSED data, catalog output, proof storage, receipt storage, semantic contract authority, schema authority, policy, release authority, public API/UI material, exact subsurface/resource-location storage, legal/mineral-rights advice, operational drilling guidance, or generated-answer authority.

---

## Scope

This directory documents and may hold Geology sensitivity registry records, registry-local indexes, sensitivity-tier mappings, redaction-profile refs, geoprivacy refs, steward-review refs, release-readiness pointers, and routing notes for Geology and Natural Resources objects and derivatives.

A Geology sensitivity registry record may describe:

- stable subject identity for sensitivity review: source, borehole record, well log, core record, private well, geochemistry sample, mineral occurrence, deposit estimate, subsurface model, interpretive surface, map derivative, layer, catalog item, release candidate, or published artifact;
- audience tier and sensitivity posture when material;
- exact subsurface, resource-adjacent, extraction-targetable, private-parcel, rights-restricted, source-role-sensitive, interpretive, model-derived, and uncertain-source posture;
- named redaction profile refs, geoprivacy transform refs, public-safe representation refs, aggregation refs, model-run refs, RealityBoundaryNote refs, and review refs;
- exact/internal location denial posture and public-safe geometry constraints;
- links to SourceDescriptor records, rights review records, policy decisions, validation receipts, RedactionReceipts, AggregationReceipts, ModelRunReceipts, EvidenceBundle/proof refs, catalog refs, release refs, correction notices, withdrawal notices, and rollback cards;
- sensitivity blockers that prevent activation, processing, catalog closure, release, export, public display, AI response, map popup, vector index exposure, or tile exposure.

They do **not** reveal sensitive locations, store Geology payloads, grant access, define policy, enforce schemas, replace review, or authorize publication.

---

## Path posture

The requested and existing lane is:

```text
data/registry/sensitivity/geology/
```

This is a subtype-first registry path: registry family first (`sensitivity`), then domain (`geology`). The parent currently exists only as a greenfield stub:

```text
data/registry/sensitivity/README.md
```

Therefore, this README treats the target path as **CONFIRMED path presence / NEEDS VERIFICATION canonical shape**. Do not treat this README as proof that live sensitivity registry records, schema validation, policy integration, release integration, or governed API sensitivity resolution already exist.

Geology sensitivity doctrine points toward `policy/sensitivity/` and `policy/domains/geology/` for binding decisions and says the sensitive-domain matrix has no explicit Geology row yet. Until ratified, Geology uses the most restrictive applicable row and default deny/generalize/redact/quarantine/steward-review/receipt posture. This registry lane should not duplicate policy. It should record sensitivity-review state and point to the policy, receipt, proof, catalog, release, correction, and rollback objects that carry authority.

---

## Repo fit

| Responsibility | Home | Boundary |
|---|---|---|
| Geology sensitivity registry records | `data/registry/sensitivity/geology/` | Sensitivity-review state, redaction/geoprivacy refs, blockers, and release-readiness pointers. |
| Sensitivity registry parent | `data/registry/sensitivity/README.md` | Parent is currently a greenfield stub; canonical parent contract remains NEEDS VERIFICATION. |
| Geology source descriptors | `data/registry/geology/sources/`, `data/registry/sources/geology/`, or accepted source registry lane | Source identity/admission records; sensitivity posture may be pinned there and referenced here. |
| Geology domain registry parent | `data/registry/geology/` | Domain-first registry routing; not sensitivity policy or payload storage. |
| Geology rights records | `data/registry/rights/geology/` if/when accepted | Rights review state; not sensitivity policy. |
| Geology source/lifecycle payloads | `data/raw/geology/`, `data/work/geology/`, `data/quarantine/geology/`, `data/processed/geology/` | Actual data belongs in lifecycle lanes, not sensitivity registry records. |
| Human-facing Geology sensitivity doctrine | `docs/domains/geology/SENSITIVITY.md` | Explains classification lattice and sensitivity posture; not registry storage. |
| Cross-domain sensitivity architecture | `docs/architecture/sensitivity.md` | Architecture for deny-by-default posture. |
| Geology semantic meaning | `contracts/domains/geology/` | Object-family meaning and invariants. |
| Machine schemas | `schemas/contracts/v1/domains/geology/`, `schemas/contracts/v1/receipts/`, or ADR-selected schema lane | Schema enforcement; sensitivity-registry schema remains NEEDS VERIFICATION. |
| Sensitivity, geoprivacy, and rights policy | `policy/sensitivity/geology/`, `policy/domains/geology/`, `policy/geoprivacy/`, `policy/rights/` | Decisions and rules; registry records only point to policy outcomes. |
| Validation/redaction/policy/review receipts | `data/receipts/` and accepted Geology receipt lanes | Process memory for checks and public-safe transforms. |
| Proof/evidence | `data/proofs/` or accepted proof lanes | EvidenceBundle closure, proof packs, signatures, and citation validation. |
| Catalog projections | `data/catalog/domain/geology/`, STAC/DCAT/PROV lanes, and triplet lanes | Catalog/discovery carriers after catalog closure. |
| Published artifacts | `data/published/layers/geology/` if/when accepted | Released public-safe artifacts and direct sidecars only. |
| Release decisions | `release/` | Promotion, correction, rollback, supersession, withdrawal, and release manifests. |
| Public surfaces | governed APIs and released artifacts only | Public clients do not read this registry lane directly. |

---

## Geology sensitivity boundary

| Rule | Handling |
|---|---|
| Registry record is control state | It records or points to sensitivity-review posture; it does not decide policy or grant access. |
| Missing Geology row is not permission | No explicit geology row in the sensitive-domain matrix means the most restrictive applicable row and default posture govern. |
| Exact subsurface points fail closed | Boreholes, cores, private wells, well logs, geochemistry sample sites, and similar exact subsurface points default to denied or generalized public exposure. |
| Extraction-targetable detail needs review | Mineral occurrence, deposit, estimate, prospect, quarry, mine, and resource-adjacent detail may expose extraction or trespass risk and requires reviewer-controlled posture. |
| Rights-restricted source content fails closed | LAS/well-log/source-derived restricted content, proprietary records, and terms-limited feeds cannot become public derivatives without rights and policy support. |
| Private-parcel/operator joins fail closed | Operator, permit, private parcel, well, mineral interest, or land-ownership joins are not public-safe by default. |
| Interpretive surfaces need reality boundaries | 3D models, cross-sections, interpolations, reconstructions, and model-derived surfaces must preserve uncertainty, source role, and RealityBoundaryNote/receipt support. |
| Source quality never overrides sensitivity | A well-sourced geology object can still be unsafe or unpublishable at exact precision. |
| RedactionReceipt is required for public-safe transforms | Generalization, aggregation, masking, withholding, or redaction must be receipted with named/versioned profile refs where required. |
| Source role is preserved | Observed, administrative, regulatory, modeled, aggregate, candidate, context, synthetic, or restricted source roles must not be upgraded by processing, map rendering, AI explanation, or release review. |
| Registry is not validation | Validation receipts, redaction receipts, review receipts, and run receipts remain separate process-memory objects. |
| Registry is not proof | EvidenceBundle/proof support remains separate. |
| Registry is not catalog | STAC/DCAT/PROV/domain catalog records and graph/triplet projections live under catalog/triplet lanes. |
| Registry is not release | Public exposure requires validation, policy, review, proof/catalog support, release manifest, correction path, and rollback path. |
| Public clients do not read this lane | Public UI/API surfaces consume governed APIs, released artifacts, catalog/triplet/proof-backed responses, and policy-safe envelopes. |

---

## Accepted material

Accepted content is limited to Geology sensitivity registry records and registry-local support files:

- sensitivity-family README files and registry-local indexes;
- sensitivity review records for sources, boreholes, wells, cores, samples, mineral resources, subsurface models, interpretive surfaces, derivatives, layers, catalog items, release candidates, and published artifacts;
- audience tier refs, sensitivity profile refs, redaction profile refs, geoprivacy refs, public-safe representation refs, aggregation refs, model-run refs, RealityBoundaryNote refs, and review refs;
- steward-review refs, rights-holder refs, source-terms refs, extraction-risk refs, private-parcel join refs, operator/permit join refs, uncertainty refs, and source-role refs;
- SourceDescriptor refs, rights refs, dataset refs, layer refs, catalog refs, release refs, and correction/rollback refs;
- validation receipt refs, RedactionReceipt refs, AggregationReceipt refs, RepresentationReceipt refs, ModelRunReceipt refs, policy receipt refs, review receipt refs, EvidenceBundle/proof refs;
- blocker records for missing sensitivity support, unresolved rights/steward review, missing receipt, missing release state, uncertain source material, or risky cross-surface inference.

Keep records compact and pointer-based. Do not embed exact subsurface locations, private-well coordinates, borehole logs, source-native sample records, resource target details, private parcel/operator joins, proprietary content, proof packs, policy decisions, catalog records, release manifests, or Geology claim content in this lane.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw Geology payloads, borehole datasets, well logs, cores, samples, geochemistry tables, mineral occurrence records, mine/quarry/prospect records, subsurface models, rasters, shapefiles, GeoParquet, COG, PMTiles, LAS files, or source-native tables | `data/raw/geology/`, `data/work/geology/`, `data/quarantine/geology/`, or `data/processed/geology/` depending on lifecycle state |
| Exact sensitive subsurface/resource coordinates, private-well details, proprietary well logs, private-parcel/operator joins, resource-target details, access secrets, or restricted review material | denied, restricted, quarantined, or routed to governed restricted storage |
| Source descriptor/admission records | `data/registry/geology/sources/` or `data/registry/sources/geology/` after topology reconciliation |
| Rights registry records | `data/registry/rights/geology/` after accepted topology |
| Dataset, crosswalk, domain, or layer registry records | `data/registry/datasets/`, `data/registry/crosswalks/`, `data/registry/domains/`, `data/registry/layers/` |
| Semantic object contracts | `contracts/domains/geology/` |
| JSON Schema | `schemas/contracts/v1/...` |
| Sensitivity policy, geoprivacy policy, rights policy, access-control logic, redaction policy, or release rules | `policy/` |
| Validation receipts, redaction receipts, policy receipts, review receipts, model receipts, or process-memory logs | `data/receipts/` |
| EvidenceBundle records, proof packs, signatures, or citation-validation closure | `data/proofs/` |
| STAC/DCAT/PROV/domain catalog records or graph/triplet projections | `data/catalog/` and `data/triplets/` |
| Published layers, reports, dashboards, tiles, API payloads, UI payloads, or generated-answer carriers | `data/published/`, governed app/API roots, and release-approved public artifact lanes |
| ReleaseManifest, PromotionDecision, CorrectionNotice, RollbackCard, withdrawal notice, or supersession notice | `release/` |
| Validator code, connector code, pipelines, fixtures, tests, or CI workflows | `tools/`, `connectors/`, `pipelines/`, `fixtures/`, `tests/`, `.github/workflows/` |
| Legal, mineral-rights, drilling, extraction, investment, safety, or operational instructions | out of scope for this registry lane and for KFM public interpretive surfaces |

---

## Suggested directory shape

The map below is **PROPOSED** documentation guidance, not proof that child folders or records exist.

```text
data/registry/sensitivity/geology/
├── README.md
├── exact_subsurface_points/
│   ├── README.md
│   └── index.local.json
├── well_logs_and_cores/
│   ├── README.md
│   └── index.local.json
├── private_wells/
│   ├── README.md
│   └── index.local.json
├── mineral_resources/
│   ├── README.md
│   └── index.local.json
├── private_parcel_operator_joins/
│   ├── README.md
│   └── index.local.json
├── interpretive_surfaces/
│   ├── README.md
│   └── index.local.json
├── restricted_source_terms/
│   ├── README.md
│   └── index.local.json
├── redaction_profiles/
│   ├── README.md
│   └── index.local.json
├── review_queue/
│   ├── README.md
│   └── index.local.json
└── index.local.json
```

Do not create a new child lane until the sensitivity object family, source descriptor refs, sensitivity refs, policy refs, review state, receipt refs, release refs, and rollback path are known.

---

## Suggested registry shape

The exact sensitivity-registry schema remains **NEEDS VERIFICATION**. A Geology sensitivity registry record should be structured enough for audit, public-safe transformation, release readiness, correction, withdrawal, and rollback.

```json
{
  "id": "kfm-sensitivity:geology:<stable-sensitivity-id>",
  "record_type": "sensitivity_registry_record",
  "domain": "geology",
  "sensitivity_family": "exact_subsurface_points | well_logs_and_cores | private_wells | mineral_resources | private_parcel_operator_joins | interpretive_surfaces | restricted_source_terms | redaction_profiles | review_queue | other",
  "subject_ref": "source | record | sample | well | borehole | resource | object_family | derivative | model_output | layer | catalog_item | release_candidate | published_artifact",
  "audience_tier": "T0 | T1 | T2 | T3 | T4 | needs-review",
  "source_registry_refs": [],
  "rights_registry_refs": [],
  "policy_refs": [],
  "redaction_profile_refs": [],
  "geoprivacy_refs": [],
  "steward_review_refs": [],
  "rights_review_refs": [],
  "private_parcel_join_refs": [],
  "extraction_risk_refs": [],
  "uncertainty_refs": [],
  "reality_boundary_refs": [],
  "validation_receipt_refs": [],
  "redaction_receipt_refs": [],
  "aggregation_receipt_refs": [],
  "model_receipt_refs": [],
  "evidence_refs": [],
  "proof_refs": [],
  "catalog_refs": [],
  "review_refs": [],
  "release_refs": [],
  "correction_refs": [],
  "rollback_refs": [],
  "public_exposure": "none | eligible-after-review | generalized-public-safe | permissioned | restricted | denied",
  "blockers": [],
  "created_at": "timestamp",
  "updated_at": "timestamp"
}
```

Do not treat this JSON block as a live schema. It is a maintainer-facing sketch until paired contracts, schemas, validators, fixtures, examples, CI, review workflows, and release workflows are verified.

---

## Required checks before use

- [ ] Confirm the sensitivity record belongs in `data/registry/sensitivity/geology/`, not source payloads, policy, contracts, schemas, receipts, proofs, catalog, published artifacts, or release lanes.
- [ ] Confirm the subject of the sensitivity review is identified: source, record, sample, well, borehole, resource, object family, derivative, model output, layer, catalog item, release candidate, published artifact, or other reviewed object.
- [ ] Confirm the most restrictive applicable sensitive-domain row and default posture are applied until a Geology-specific row is ratified.
- [ ] Confirm exact borehole, core, private-well, well-log, geochemistry sample, extraction-targetable mineral/resource, restricted-source, and private-parcel/operator join contexts fail closed where required.
- [ ] Confirm sensitivity evidence exists before asserting any public-safe tier, transform, audience, or display eligibility.
- [ ] Confirm named/versioned redaction or aggregation profile refs and required receipt refs exist before any public-safe transformation is asserted.
- [ ] Confirm rights-holder, agency, operator, landowner, steward-review, source-terms, policy, and review requirements are current before any use beyond restricted processing.
- [ ] Confirm map popups, exports, AI text, vector indexes, tile surfaces, and cross-domain joins do not leak restricted detail through inference.
- [ ] Confirm sensitivity state does not override rights, source-role, evidence closure, catalog closure, policy decision, review state, or release state.
- [ ] Confirm validation receipts, redaction receipts, aggregation receipts, model receipts, policy outcomes, and review records exist before catalog or release eligibility is asserted.
- [ ] Confirm EvidenceRef/EvidenceBundle and proof refs exist for consequential use.
- [ ] Confirm release refs point to ReleaseManifest/PromotionDecision objects rather than implying publication from sensitivity state.
- [ ] Confirm correction, supersession, withdrawal, stale-state, and rollback paths exist for changed sensitivity, rights-holder decision, source-terms change, steward review, or release posture.
- [ ] Confirm no public client, map layer, graph edge, vector index, generated answer, report, or dashboard reads this registry lane as direct public truth or permission.

---

## Status notes

| Claim | Status |
|---|---:|
| This README replaces the empty placeholder at `data/registry/sensitivity/geology/README.md`. | CONFIRMED authored |
| The target path existed in the live repository as an empty placeholder before this edit. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/sensitivity/README.md` exists and is currently a greenfield stub. | CONFIRMED by GitHub contents API during this edit |
| Geology sensitivity docs say there is no explicit geology row in the sensitive-domain matrix and that the most restrictive applicable row plus default deny/generalize/redact/quarantine/steward-review/receipt posture govern until ratified. | CONFIRMED by GitHub contents API during this edit |
| Geology sensitivity docs classify exact borehole/core/private-well/geochem sample locations as T4 by default and extraction-targetable or rights-restricted resource detail as reviewer-controlled by default. | CONFIRMED by GitHub contents API during this edit |
| Geology registry/source README files say restricted subsurface and resource-adjacent details fail closed until governed redaction/review/release gates close. | CONFIRMED by GitHub contents API during this edit |
| Concrete Geology sensitivity registry payloads exist under this requested lane. | UNKNOWN |
| The final accepted parent contract for `data/registry/sensitivity/` is resolved. | NEEDS VERIFICATION |
| A canonical Geology sensitivity registry schema is enforced. | NEEDS VERIFICATION |
| CI validates Geology sensitivity registry records. | UNKNOWN |
| This README grants public access to Geology sensitivity registry internals. | DENY |

---

## Maintainer note

Geology sensitivity registry records are useful because they make sensitivity posture, redaction/geoprivacy refs, steward-review state, source-terms constraints, release readiness, correction, and rollback inspectable before any Geology object approaches a public surface. They become dangerous when treated as policy, source payloads, exact subsurface/resource-location storage, proof closure, catalog closure, release decisions, legal/mineral-rights advice, or permission.

Keep the safe chain explicit:

```text
sensitivity registry record -> source/object refs -> policy/review outcome -> lifecycle payload -> validation/redaction/aggregation/model receipt -> proof/catalog -> release -> governed public surface
```

Never collapse it into:

```text
sensitivity registry record -> public Geology permission
```
