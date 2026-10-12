<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/sources/agriculture/readme
name: Agriculture Source Registry README
path: data/registry/sources/agriculture/README.md
type: data-registry-source-domain-readme
version: v0.2.0
status: draft
owners:
  - <registry-steward>
  - <source-steward>
  - <agriculture-domain-steward>
  - <rights-steward>
  - <sensitivity-steward>
  - <policy-steward>
  - <proof-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-29
updated: 2026-06-29
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: registry/source-domain
registry_scope: agriculture-source-descriptor-routing-and-admission-control
path_posture: existing-empty-file-replaced; canonical-under-data-registry-sources; agriculture-descriptor-payloads-unknown; validators-ci-runtime-readers-unknown
sensitivity_posture: registry-internal; no-public-path; source-role-preserving; rights-and-sensitivity-fail-closed; private-farm-and-operator-detail-protected; release-blocked-until-gates-close
related:
  - ../README.md
  - ../../README.md
  - ../../source_descriptors/README.md
  - ../../../raw/agriculture/
  - ../../../work/agriculture/
  - ../../../quarantine/agriculture/
  - ../../../processed/agriculture/
  - ../../../catalog/agriculture/
  - ../../../triplets/agriculture/
  - ../../../published/agriculture/
  - ../../../receipts/agriculture/
  - ../../../proofs/agriculture/
  - ../../../../contracts/
  - ../../../../schemas/contracts/v1/
  - ../../../../policy/
  - ../../../../release/
  - ../../../../docs/sources/catalog/
  - ../../../../docs/architecture/directory-rules.md
  - ../../../../docs/doctrine/directory-rules.md
tags:
  - kfm
  - data
  - registry
  - sources
  - agriculture
  - source-descriptor
  - source-role
  - rights
  - sensitivity
  - evidence
  - provenance
  - crop-year
  - field-boundary
  - farm-operator-privacy
  - release-gated
  - rollback
  - no-public-path
notes:
  - "This README replaces the empty stub at `data/registry/sources/agriculture/README.md`."
  - "This lane is a domain segment of the canonical source registry parent at `data/registry/sources/`."
  - "Agriculture source descriptors are admission/control records. They do not store source payloads, decide policy, emit receipts, prove claims, close catalogs, publish artifacts, or authorize public map/API exposure."
  - "Examples of agriculture source families in this README are routing candidates only until concrete SourceDescriptor records, rights review, sensitivity review, receipts, proofs, catalog records, and release decisions are verified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Agriculture Source Registry

Domain source-registry lane for agriculture source descriptors and admission-control routing.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: data registry sources" src="https://img.shields.io/badge/root-data%2Fregistry%2Fsources-0a7ea4">
  <img alt="Domain: agriculture" src="https://img.shields.io/badge/domain-agriculture-3f7f3f">
  <img alt="Boundary: not source data" src="https://img.shields.io/badge/boundary-not%20source%20data-critical">
  <img alt="Boundary: not release" src="https://img.shields.io/badge/boundary-not%20release-critical">
  <img alt="Exposure: no public path" src="https://img.shields.io/badge/exposure-no%20public%20path-critical">
</p>

**Quick links:** [Scope](#scope) - [Path posture](#path-posture) - [Agriculture source families](#agriculture-source-families) - [Source-role handling](#source-role-handling) - [Agriculture risk controls](#agriculture-risk-controls) - [Accepted material](#accepted-material) - [Exclusions](#exclusions) - [Suggested directory shape](#suggested-directory-shape) - [Required checks](#required-checks-before-use) - [Status notes](#status-notes)

> [!CAUTION]
> `data/registry/sources/agriculture/` is a source-registry control lane. It is not agriculture data storage, crop truth, farm-boundary truth, landowner/operator truth, yield truth, compliance truth, policy authority, proof authority, catalog authority, release authority, public API material, public map material, or generated-answer authority.

---

## Scope

This directory records how agriculture-related sources may be treated before their material enters the KFM lifecycle. It belongs under the canonical source-registry parent:

```text
data/registry/sources/
```

Agriculture SourceDescriptor-style records may describe source identity, source role, steward, upstream authority, rights posture, sensitivity posture, update cadence, crop-year or survey-year scope, geography scope, attribution requirements, stale-state handling, correction path, supersession path, and rollback references.

The registry can help decide whether agriculture material is admitted, quarantined, restricted, delayed, generalized, or denied. It does **not** make a crop, field, ownership, operation, yield, practice, conservation, weather-impact, market, or regulatory claim true.

---

## Path posture

The requested lane is:

```text
data/registry/sources/agriculture/
```

Directory Rules evidence from the attached copy allows domain-scoped registry lanes using either:

```text
data/registry/<domain>/
data/registry/sources/<domain>/
```

The current registry root and source-registry parent identify `data/registry/sources/` as the source admission and authority-control surface. Therefore this agriculture lane is treated as a subtype-first source-registry domain lane, not a parallel domain registry, dataset registry, proof lane, catalog lane, or release lane.

The sibling compatibility lane:

```text
data/registry/source_descriptors/
```

must not duplicate authoritative agriculture SourceDescriptor records from this path. If a future migration changes the canonical source-descriptor topology, add a migration note, redirect, ADR reference, or Directory Rules update before moving records.

---

## Agriculture source families

The table below is **PROPOSED routing guidance**, not evidence that these records exist in the repo. Add concrete descriptors only after rights, sensitivity, source-role, cadence, and steward review.

| Source family | Possible use | Required caution |
|---|---|---|
| USDA NASS statistical sources | Crop acreage, yield, production, survey, census, or county/region aggregate context. | Preserve aggregation level, survey/crop year, estimate/revision status, and citation scope. Do not downscale aggregate values into parcel or field truth. |
| USDA NASS Cropland Data Layer-style products | Crop-cover classification context and time-aware land-cover comparison. | Treat as classified/modeled/derived source material, not direct observation of field operations. Preserve vintage, confidence/accuracy notes, and pixel/class limitations. |
| USDA FSA or farm-program materials | Program, administrative, or participation context where rights permit. | Private farm/operator data, field boundaries, program participation, and compliance-sensitive details require strict rights and sensitivity review. |
| NRCS agriculture and conservation materials | Conservation practice, soils-adjacent, land capability, erosion, or resource-planning context. | Keep soil-domain and agriculture-domain responsibilities separate. Do not treat planning or modeled material as observed farm practice. |
| State agriculture agency materials | State-level program, inspection, market, animal-health, pesticide, or regulatory context. | Regulatory or compliance data may be sensitive, time-bound, rights-bound, and potentially harmful if overexposed. |
| Extension or university materials | Context, interpretation, agronomic guidance, historical reports, or research summaries. | Usually contextual or corroborating unless a specific dataset, method, and authority scope are registered. |
| Weather, climate, drought, hydrology, or irrigation context sources | Crop-impact context, irrigation context, hazard context, and time-aware explanatory features. | Keep source role and domain of origin explicit; context does not become agriculture proof without evidence linkage. |
| Remote-sensing or model outputs | Vegetation index, crop condition, phenology, stress, evapotranspiration, or productivity estimates. | Preserve model/run identity, inputs, uncertainty, spatial/temporal resolution, and validation state. Do not expose sensitive field-level inference by default. |
| Historic agriculture records | Historic crop, land-use, settlement, farmstead, county fair, elevator, or production context. | Preserve source vintage, transcription uncertainty, georeference uncertainty, and interpretive limits. |

---

## Source-role handling

Agriculture sources are especially prone to role collapse. Keep the role explicit from admission through catalog, proof, map, graph, and generated-answer use.

| Source role | Agriculture example | Boundary |
|---|---|---|
| `observed` | Direct measurement or field-verified record where rights and method support that role. | Do not assign this role to classified imagery, surveys, models, or aggregates. |
| `regulatory` | Official designations, compliance status, inspection class, program eligibility, or restricted-use rules. | Regulatory status is not a field observation or public release decision. |
| `modeled` | Crop classification, condition model, evapotranspiration estimate, drought impact model, or remote-sensing inference. | Requires model/run refs, input scope, uncertainty, and validation posture. |
| `aggregate` | County, crop-reporting district, watershed, census, or survey aggregate. | Must not be treated as parcel, field, operator, or exact-location truth. |
| `administrative` | Program records, indexes, inventories, directories, or agency-maintained lists. | Administrative presence does not prove real-world condition without evidence support. |
| `candidate` | Unreviewed imported source, provisional match, extracted table, OCR-derived record, or unverified geocode. | Blocks publication until reviewed, promoted, corrected, or rejected. |
| `synthetic` | Generated crop scenario, demo layer, model-generated teaching example, or placeholder record. | Must carry a reality-boundary note and must not be mixed with evidence claims. |
| `context` | General agronomic notes, explanatory reports, or background references. | Useful for interpretation but insufficient as claim proof by itself. |
| `restricted` | Private, rights-bound, security-sensitive, operator-identifying, or compliance-sensitive material. | Defaults to deny, redact, generalize, delay, or quarantine until policy and review gates close. |

---

## Agriculture risk controls

Agriculture records can expose private, economic, operational, or safety-relevant information. Default to the narrowest useful exposure until rights and sensitivity review say otherwise.

| Risk | Required posture |
|---|---|
| Private farm, ranch, operator, landowner, tenant, or worker identity | Treat as restricted unless explicit rights, purpose, consent/legal basis, minimization, and release posture are confirmed. |
| Field, parcel, facility, storage, chemical, livestock, irrigation, equipment, or logistics detail | Avoid public exact-location exposure unless already public, rights-cleared, sensitivity-cleared, and release-approved. |
| Compliance, inspection, enforcement, disease, pest, contamination, animal-health, or pesticide records | Require source authority, valid/effective time, rights, sensitivity, policy, review, and release gates. |
| Crop-year, survey-year, or seasonal claims | Carry valid time, source vintage, revision status, stale-state handling, and correction path. |
| Remote-sensing or modeled classifications | Preserve uncertainty, class limits, model/run refs, and avoid overstating inferred field conditions. |
| Aggregate data | Keep aggregation unit and suppression rules visible. Do not infer household, farm, parcel, or field-level facts from aggregate cells. |
| Cross-domain joins | Review joins to soil, hydrology, habitat, hazards, people/DNA/land, roads/rail/trade, settlement, or infrastructure lanes before release. |

---

## Accepted material

Accepted material in this lane is limited to source-registry support for agriculture:

- this README and other registry-local guidance;
- agriculture SourceDescriptor records when their schema home, naming convention, steward, rights review, and sensitivity review are verified;
- agriculture source-family indexes that point to canonical descriptor records;
- source-role vocabulary notes that do not replace the canonical vocabulary/schema;
- supersession, correction, stale-state, withdrawal, and rollback pointers for agriculture sources;
- redirect or migration notes if agriculture descriptors are moved between registry shapes;
- blocker notes that identify missing rights, sensitivity, evidence, receipt, catalog, release, correction, or rollback support.

Registry records should be compact and pointer-based. Store only the control state needed to route and govern sources. Do not embed source datasets or sensitive operational details here.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw agriculture datasets, exports, imagery, reports, tables, shapefiles, GeoJSON, GeoParquet, COG, PMTiles, or API dumps | `data/raw/agriculture/`, `data/work/agriculture/`, or `data/quarantine/agriculture/` depending on review state |
| Normalized agriculture objects, derived features, classified layers, or processed analytics | `data/processed/agriculture/` |
| STAC/DCAT/PROV/domain catalog records | `data/catalog/agriculture/` or accepted catalog lane |
| Graph/triplet projections | `data/triplets/agriculture/` |
| Published map/data artifacts | `data/published/agriculture/` only after release |
| Validation, ingest, transform, review, redaction, model, policy, or run receipts | `data/receipts/agriculture/` or accepted receipt lane |
| EvidenceBundle records, proof packs, signatures, or citation-validation closure | `data/proofs/agriculture/` or accepted proof lane |
| SourceDescriptor schemas or JSON Schema definitions | `schemas/contracts/v1/` or accepted schema root |
| Semantic contracts | `contracts/` |
| Rights, sensitivity, access, redaction, runtime, or release policy rules | `policy/` |
| Connectors, watchers, scrapers, ETL code, model code, or validator code | `connectors/`, `pipelines/`, `packages/`, `tools/`, or accepted implementation roots |
| Release manifests, promotion decisions, correction notices, withdrawal notices, supersession decisions, or rollback cards | `release/` |
| Secrets, credentials, tokens, private endpoint details, or restricted operator/farm/facility details | never in registry; use approved restricted storage and secret management |

---

## Suggested directory shape

This shape is **PROPOSED** until descriptor naming, schema home, validator discovery, and CI are verified.

```text
data/registry/sources/agriculture/
├── README.md
├── index.local.json                 # PROPOSED pointer index only
├── source_families.local.yaml       # PROPOSED local routing vocabulary only
├── superseded/                      # PROPOSED retained descriptor pointers
│   └── README.md
└── descriptors/                     # PROPOSED only after schema/topology decision
    └── <source_id>.descriptor.yaml
```

Prefer one canonical descriptor location. If descriptor files are placed directly under this directory instead of `descriptors/`, document that convention before adding records.

---

## Minimum descriptor fields

The exact schema remains governed by the accepted SourceDescriptor schema. Agriculture descriptors should not be considered review-ready unless they can resolve at least the following control facts:

| Field family | Minimum expectation |
|---|---|
| Identity | Stable KFM source ID, upstream source name, upstream identifier where applicable, steward, and contact/owner role. |
| Source role | One explicit role with authority scope and no role upgrading. |
| Domain scope | Agriculture scope plus any linked domain context, such as soil, hydrology, habitat, hazards, trade, settlement, infrastructure, or land records. |
| Time scope | Crop year, survey year, publication date, valid/effective time, retrieval time, update cadence, stale-state rule, and revision handling where applicable. |
| Geography scope | Coverage area, aggregation unit, geometry precision, generalization/redaction profile, and uncertainty where applicable. |
| Rights scope | License, terms, attribution, redistribution posture, endpoint terms, use restrictions, expiration, and rights steward review state. |
| Sensitivity scope | Operator/privacy risk, field/facility risk, compliance/enforcement risk, ecology/geoprivacy risk, infrastructure risk, and public-release class. |
| Evidence linkage | EvidenceRef/EvidenceBundle expectations, proof requirements, catalog refs, receipt refs, and release blockers. |
| Correction path | Supersession, withdrawal, correction notice, stale-state, and rollback pointers. |

---

## Required checks before use

- [ ] Confirm the source belongs in the agriculture source-registry lane and not only in soil, hydrology, habitat, hazards, roads/rail/trade, settlements/infrastructure, people/DNA/land, catalog, proof, or release lanes.
- [ ] Confirm `SourceDescriptor` schema home, descriptor filename convention, and validator discovery before adding descriptor payloads.
- [ ] Confirm rights, attribution, endpoint terms, redistribution posture, and review state.
- [ ] Confirm sensitivity tier and exposure posture, especially for field, farm, operator, compliance, livestock, pesticide, disease, facility, irrigation, and infrastructure-adjacent details.
- [ ] Confirm source role and prevent aggregate, modeled, administrative, regulatory, candidate, context, or synthetic material from being treated as observed truth.
- [ ] Confirm crop-year, survey-year, valid/effective time, source vintage, stale-state handling, correction path, supersession path, and rollback refs.
- [ ] Confirm any cross-domain join has explicit source-role, policy, proof, and release support.
- [ ] Confirm validation, transform, redaction/generalization, model, policy, and review receipts exist before catalog or release eligibility is asserted.
- [ ] Confirm EvidenceRef/EvidenceBundle and proof refs exist before consequential agriculture claims are used publicly.
- [ ] Confirm catalog refs point to STAC/DCAT/PROV/domain catalog records rather than embedding them here.
- [ ] Confirm release refs point to ReleaseManifest/PromotionDecision objects rather than implying publication from registry state.
- [ ] Confirm no public client, map layer, graph edge, vector index, generated answer, report, or dashboard reads this registry lane as direct public truth.

---

## Status notes

| Claim | Status |
|---|---:|
| This README replaces the empty file at `data/registry/sources/agriculture/README.md`. | CONFIRMED authored |
| The requested target path existed in the live repository as an empty file before this edit. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/README.md` exists and frames registry records as governance/control records, not payloads, schemas, policy, receipts, proofs, catalogs, releases, or public output authority. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/sources/README.md` exists and frames `data/registry/sources/` as the pre-RAW source admission and authority-control surface. | CONFIRMED by GitHub contents API during this edit |
| The attached Directory Rules copy includes `data/registry/<domain>/` or `data/registry/sources/<domain>/` as valid registry/domain shapes. | CONFIRMED by local PDF text extraction during this edit |
| Concrete agriculture SourceDescriptor payloads exist under this lane. | UNKNOWN |
| Agriculture descriptor schema home, filename convention, validator discovery, and CI enforcement are verified. | NEEDS VERIFICATION |
| Agriculture rights/sensitivity policy profiles are complete. | UNKNOWN |
| Agriculture catalog/proof/release wiring is implemented. | UNKNOWN |
| Runtime registry resolution or governed API behavior reads this lane. | UNKNOWN |
| This README grants public access to agriculture source-registry internals. | DENY |

---

## Maintainer note

Agriculture source descriptors are useful because they preserve source identity, source role, rights, sensitivity, crop-year/time scope, geography scope, uncertainty, correction, and rollback before data enters the KFM lifecycle. They become dangerous when treated as public truth or as a shortcut around proof and release.

Keep the chain explicit:

```text
Agriculture SourceDescriptor -> rights/sensitivity/stale-state gate -> RAW admission -> lifecycle processing -> validation/redaction/model/review receipts -> EvidenceBundle/proof -> catalog/triplet -> release -> governed public surface
```

Never collapse it into:

```text
source descriptor -> agriculture truth -> public map/API/generated answer
```
