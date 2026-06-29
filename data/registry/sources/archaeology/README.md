<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/sources/archaeology/readme
name: Archaeology Source Registry README
path: data/registry/sources/archaeology/README.md
type: data-registry-source-domain-readme
version: v0.2.0
status: draft
owners:
  - <registry-steward>
  - <source-steward>
  - <archaeology-domain-steward>
  - <cultural-review-steward>
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
registry_scope: archaeology-source-descriptor-routing-and-admission-control
path_posture: existing-scaffold-replaced; canonical-under-data-registry-sources; archaeology-descriptor-payloads-unknown; validators-ci-runtime-readers-unknown
sensitivity_posture: registry-internal; no-public-path; T4-default; deny-by-default; exact-location-denial; cultural-review-required; rights-and-sensitivity-fail-closed; release-blocked-until-gates-close
related:
  - ../README.md
  - ../../README.md
  - ../../source_descriptors/README.md
  - ../../sensitivity/README.md
  - ../../../raw/archaeology/
  - ../../../work/archaeology/
  - ../../../quarantine/archaeology/
  - ../../../processed/archaeology/
  - ../../../catalog/archaeology/
  - ../../../triplets/archaeology/
  - ../../../published/archaeology/
  - ../../../receipts/archaeology/
  - ../../../proofs/archaeology/
  - ../../../../docs/domains/archaeology/README.md
  - ../../../../docs/domains/archaeology/MISSING_OR_PLANNED_FILES.md
  - ../../../../contracts/domains/archaeology/
  - ../../../../schemas/contracts/v1/domains/archaeology/
  - ../../../../policy/domains/archaeology/
  - ../../../../policy/sensitivity/archaeology/
  - ../../../../policy/rights/
  - ../../../../release/candidates/archaeology/
  - ../../../../docs/architecture/directory-rules.md
  - ../../../../docs/doctrine/directory-rules.md
tags:
  - kfm
  - data
  - registry
  - sources
  - archaeology
  - cultural-heritage
  - source-descriptor
  - source-role
  - rights
  - sensitivity
  - T4
  - deny-by-default
  - exact-location-denial
  - cultural-review
  - steward-review
  - evidence
  - provenance
  - redaction
  - release-gated
  - rollback
  - no-public-path
notes:
  - "This README replaces the scaffold at `data/registry/sources/archaeology/README.md`."
  - "This lane is a domain segment of the canonical source registry parent at `data/registry/sources/`."
  - "Archaeology source descriptors are admission/control records. They do not store source payloads, exact site geometry, sacred-site knowledge, burial/human-remains detail, policy decisions, receipts, proofs, catalog closure, release decisions, or public map/API material."
  - "Archaeology fails closed by default. Examples of source families in this README are routing candidates only until concrete SourceDescriptor records, rights review, cultural/steward review, sensitivity review, receipts, proofs, catalog records, and release decisions are verified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Archaeology Source Registry

Domain source-registry lane for archaeology and cultural-heritage source descriptors and admission-control routing.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: data registry sources" src="https://img.shields.io/badge/root-data%2Fregistry%2Fsources-0a7ea4">
  <img alt="Domain: archaeology" src="https://img.shields.io/badge/domain-archaeology-6b4f2a">
  <img alt="Sensitivity: T4 default" src="https://img.shields.io/badge/sensitivity-T4%20default-critical">
  <img alt="Posture: deny by default" src="https://img.shields.io/badge/posture-deny--by--default-critical">
  <img alt="Exposure: no public path" src="https://img.shields.io/badge/exposure-no%20public%20path-critical">
</p>

**Quick links:** [Scope](#scope) - [Path posture](#path-posture) - [Archaeology source families](#archaeology-source-families) - [Source-role handling](#source-role-handling) - [Sensitivity controls](#sensitivity-controls) - [Accepted material](#accepted-material) - [Exclusions](#exclusions) - [Suggested directory shape](#suggested-directory-shape) - [Required checks](#required-checks-before-use) - [Status notes](#status-notes)

> [!CAUTION]
> `data/registry/sources/archaeology/` is a source-registry control lane. It is not archaeology data storage, site-location storage, sacred-site knowledge storage, burial or human-remains storage, landowner-detail storage, collection-security storage, proof authority, catalog authority, policy authority, release authority, public API material, public map material, or generated-answer authority.

---

## Scope

This directory records how archaeology and cultural-heritage sources may be treated before their material enters the KFM lifecycle. It belongs under the canonical source-registry parent:

```text
data/registry/sources/
```

Archaeology SourceDescriptor-style records may describe source identity, source role, steward, upstream authority, rights posture, sensitivity posture, cultural/steward review requirements, update cadence, valid/effective time, survey or record vintage, geography scope, geometry precision limits, attribution requirements, stale-state handling, correction path, supersession path, and rollback references.

The registry can help decide whether archaeology material is admitted, quarantined, restricted, generalized, delayed, or denied. It does **not** make an archaeological site, artifact, survey, feature, context, anomaly, chronology, collection, cultural affiliation, public-safe summary, or map layer true or releasable.

---

## Path posture

The requested lane is:

```text
data/registry/sources/archaeology/
```

Directory Rules evidence from the attached copy allows domain-scoped registry lanes using either:

```text
data/registry/<domain>/
data/registry/sources/<domain>/
```

The current registry root and source-registry parent identify `data/registry/sources/` as the source admission and authority-control surface. The archaeology domain docs also list `data/registry/sources/archaeology/` as the source-descriptor lane in the archaeology responsibility-root pattern.

Therefore this archaeology lane is treated as a subtype-first source-registry domain lane, not a parallel domain registry, sensitivity registry, proof lane, catalog lane, release lane, or public-surface lane.

The sibling compatibility lane:

```text
data/registry/source_descriptors/
```

must not duplicate authoritative archaeology SourceDescriptor records from this path. If a future migration changes the canonical source-descriptor topology, add a migration note, redirect, ADR reference, or Directory Rules update before moving records.

---

## Archaeology source families

The table below is **PROPOSED routing guidance**, not evidence that these records exist in the repo. Add concrete descriptors only after rights review, source-role review, sensitivity review, cultural/steward review, and release-risk review.

| Source family | Possible use | Required caution |
|---|---|---|
| State historic preservation and historic-resource inventory sources | Site, survey, eligibility, inventory, or review context where rights and sensitivity allow. | Exact geometry, restricted records, site IDs, collection-security detail, and steward-only fields fail closed. Public release requires redaction/generalization and recorded review. |
| Archaeological survey reports | Survey-area, method, finding, negative-survey, or context evidence. | Report text may contain exact location, private landowner, site condition, artifact, burial, or culturally restricted detail. Quarantine or restrict until reviewed. |
| Cultural-resource management records | Project, compliance, survey, mitigation, or consultation context. | Compliance context is not public permission. Preserve authority, valid/effective time, rights, consultation status, and restricted fields. |
| Tribal, cultural, or steward-provided knowledge | Steward-reviewed cultural context, restricted knowledge boundaries, consultation notes, or public-safe interpretation. | Sovereignty, consent, CARE posture, access limits, and allowed representation control use. Do not encode restricted knowledge in public-readable descriptors. |
| Museum, repository, accession, or collection records | Collection provenance, repository, accession, or artifact-record context. | Collection-security detail, provenience precision, donor restrictions, NAGPRA-related material, human-remains context, and cultural restrictions fail closed. |
| LiDAR, aerial imagery, geophysics, or remote-sensing sources | Candidate anomaly, terrain, feature, or landscape context. | Candidate features are not confirmed sites. Model/remote-sensing output requires uncertainty, method, resolution, vintage, and review state. |
| Historic maps, atlases, land records, route records, or gazetteers | Context for historic place, landscape, route, settlement, or land-use interpretation. | Context does not confirm archaeological presence. Preserve source vintage, georeference uncertainty, transcription uncertainty, and source role. |
| Academic, local-history, or gray-literature sources | Context, interpretation, chronology, historical background, or source leads. | Treat as context or corroborating material unless a concrete dataset, authority, rights, and method are registered. |
| Public interpretive or educational sources | Released public-safe summaries, signage text, or already-public interpretation. | Public prose is not permission to expose restricted precision or derive sensitive joins. Keep release provenance visible. |

---

## Source-role handling

Archaeology sources are high-risk for role collapse because candidate features, old maps, regulatory records, survey reports, and generated summaries can be mistaken for confirmed sites. Preserve source role from admission through processing, proof, catalog, map, graph, and generated-answer use.

| Source role | Archaeology example | Boundary |
|---|---|---|
| `observed` | Field-verified observation or professionally recorded survey finding where rights and sensitivity allow. | Does not imply public release, exact-location disclosure, or site confirmation outside the recorded scope. |
| `regulatory` | Eligibility, review, protection, consultation, or compliance status. | Regulatory status is not field observation and is not public release permission. |
| `modeled` | LiDAR candidate, geophysics interpretation, remote-sensing anomaly, or predictive model output. | Requires model/run refs, method, inputs, uncertainty, validation state, and steward review. |
| `aggregate` | County, region, watershed, survey-area, or generalized public-safe count/summary. | Must not be reverse-engineered into exact site, landowner, collection, or restricted-location facts. |
| `administrative` | Inventory index, accession register, repository record, project list, or cataloged administrative record. | Administrative presence does not prove condition, location, cultural affiliation, or public-safe status. |
| `candidate` | Unreviewed anomaly, OCR extraction, geocode, table extraction, or source lead. | Blocks publication until reviewed, promoted, rejected, generalized, or quarantined. |
| `synthetic` | Training example, generated scene, demo layer, or placeholder archaeology object. | Requires a reality-boundary note and must never be mixed with evidence claims. |
| `context` | Historical map, local-history account, oral-history summary, route context, or background interpretation. | Useful for interpretation but insufficient as claim proof by itself. |
| `restricted` | Exact site, sacred, burial, human-remains, collection-security, private-landowner, steward-only, or looting-risk material. | Defaults to deny, quarantine, redact, generalize, delay, or restrict until governed gates close. |

---

## Sensitivity controls

Archaeology defaults to strict denial for exact and culturally sensitive material. A registry descriptor may record sensitivity posture and point to review artifacts, but it must not carry restricted content in public-readable form.

| Risk | Required posture |
|---|---|
| Exact archaeological site geometry or site identifiers | Do not expose in registry prose, fixtures, public docs, public indexes, vector indexes, map labels, or generated responses. Store only governed pointers and release-safe generalized references where allowed. |
| Burial sites, human remains, funerary objects, sacred places, or culturally restricted knowledge | Fail closed. Require cultural/steward review, rights/sovereignty posture, access limits, redaction/generalization, receipts, proof support, release decision, correction path, and rollback target. |
| Looting, vandalism, collection-security, or site-condition exposure | Treat as restricted even when source material is partly public. Avoid joins that make protected locations discoverable. |
| Private landowner, access, permission, or property-detail exposure | Fail closed unless rights, purpose, minimization, sensitivity, and release posture are recorded. |
| Candidate anomalies and predictive surfaces | Keep as candidate/modeled, not confirmed. Public exposure requires generalization, uncertainty display, review state, and release approval. |
| Historic or georeferenced maps | Preserve georeference uncertainty and source vintage. Do not infer site presence from proximity alone. |
| Cross-domain joins | Review joins to roads/rail/trade, settlement, people/DNA/land, hydrology, hazards, geology, habitat, flora, fauna, and infrastructure before any release. |

---

## Accepted material

Accepted material in this lane is limited to source-registry support for archaeology:

- this README and other registry-local guidance;
- archaeology SourceDescriptor records when their schema home, naming convention, steward, rights review, cultural/steward review, and sensitivity review are verified;
- archaeology source-family indexes that point to canonical descriptor records;
- source-role vocabulary notes that do not replace the canonical vocabulary/schema;
- supersession, correction, stale-state, withdrawal, and rollback pointers for archaeology sources;
- redirect or migration notes if archaeology descriptors are moved between registry shapes;
- blocker notes that identify missing rights, sensitivity, cultural review, evidence, receipt, catalog, release, correction, or rollback support.

Keep registry records compact and pointer-based. Store only the control state needed to govern admission and use. Do not embed sensitive archaeology payloads or exact-location detail here.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw archaeology datasets, reports, scans, exports, imagery, geophysics, LiDAR, tables, shapefiles, GeoJSON, GeoParquet, COG, PMTiles, or API dumps | `data/raw/archaeology/`, `data/work/archaeology/`, or `data/quarantine/archaeology/` depending on review state |
| Exact site geometry, sacred-site detail, burial or human-remains detail, collection-security detail, private-landowner detail, or steward-only knowledge | Never in public-readable registry files; use approved restricted storage and policy-governed pointers only |
| Normalized archaeology objects, candidate features, derived layers, or processed analytics | `data/processed/archaeology/` after validation, or `data/quarantine/archaeology/` when unresolved |
| STAC/DCAT/PROV/domain catalog records | `data/catalog/archaeology/` or accepted catalog lane |
| Graph/triplet projections | `data/triplets/archaeology/` |
| Published public-safe artifacts | `data/published/archaeology/` or accepted published lane only after release |
| Validation, ingest, transform, redaction, review, model, policy, or run receipts | `data/receipts/archaeology/` or accepted receipt lane |
| EvidenceBundle records, proof packs, signatures, or citation-validation closure | `data/proofs/archaeology/` or accepted proof lane |
| SourceDescriptor schemas or JSON Schema definitions | `schemas/contracts/v1/` or accepted schema root |
| Semantic contracts | `contracts/domains/archaeology/` |
| Rights, sensitivity, cultural-review, access, redaction, runtime, or release policy rules | `policy/domains/archaeology/`, `policy/sensitivity/archaeology/`, `policy/rights/`, or accepted policy lanes |
| Connectors, watchers, scrapers, ETL code, model code, or validator code | `connectors/`, `pipelines/`, `packages/`, `tools/`, or accepted implementation roots |
| Release manifests, promotion decisions, correction notices, withdrawal notices, supersession decisions, or rollback cards | `release/candidates/archaeology/` or accepted release lanes |
| Secrets, credentials, tokens, private endpoint details, or restricted access procedures | never in registry; use approved restricted storage and secret management |

---

## Suggested directory shape

This shape is **PROPOSED** until descriptor naming, schema home, validator discovery, sensitivity policy wiring, and CI are verified.

```text
data/registry/sources/archaeology/
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

The exact schema remains governed by the accepted SourceDescriptor schema. Archaeology descriptors should not be considered review-ready unless they can resolve at least the following control facts:

| Field family | Minimum expectation |
|---|---|
| Identity | Stable KFM source ID, upstream source name, upstream identifier where applicable, steward, source owner/authority role, and contact path. |
| Source role | One explicit role with authority scope and no role upgrading. |
| Domain scope | Archaeology scope plus any linked domain context, such as roads/rail/trade, settlements/infrastructure, people/DNA/land, hydrology, hazards, geology, habitat, flora, or fauna. |
| Time scope | Survey date, record date, publication date, valid/effective time, retrieval time, update cadence, stale-state rule, and revision handling where applicable. |
| Geography scope | Coverage area, precision class, generalization/redaction profile, location uncertainty, and exact-location denial posture. |
| Rights scope | License, terms, attribution, redistribution posture, endpoint terms, use restrictions, expiration, steward restrictions, cultural restrictions, and rights review state. |
| Sensitivity scope | T4/default posture, sacred/burial/human-remains risk, looting risk, private-landowner risk, collection-security risk, steward-only knowledge risk, and public-release class. |
| Evidence linkage | EvidenceRef/EvidenceBundle expectations, proof requirements, catalog refs, receipt refs, and release blockers. |
| Review linkage | CulturalReview, StewardReview, SensitivityTransform, RedactionReceipt, PublicationTransformReceipt, ReviewRecord, or equivalent pointers where required. |
| Correction path | Supersession, withdrawal, correction notice, stale-state, and rollback pointers. |

---

## Required checks before use

- [ ] Confirm the source belongs in the archaeology source-registry lane and not only in docs, contracts, schemas, policy, sensitivity registry, catalog, proof, release, or another domain lane.
- [ ] Confirm `SourceDescriptor` schema home, descriptor filename convention, validator discovery, and CI before adding descriptor payloads.
- [ ] Confirm rights, attribution, endpoint terms, redistribution posture, access limits, cultural/steward restrictions, and review state.
- [ ] Confirm sensitivity tier and exposure posture, especially for exact site geometry, site identifiers, sacred places, burial/human-remains context, private landowner detail, collection security, and looting-risk detail.
- [ ] Confirm source role and prevent regulatory, modeled, aggregate, administrative, candidate, context, or synthetic material from being treated as observed or confirmed archaeological truth.
- [ ] Confirm source vintage, survey date, publication date, valid/effective time, stale-state handling, correction path, supersession path, and rollback refs.
- [ ] Confirm any cross-domain join has explicit source-role, sensitivity, rights, policy, proof, and release support.
- [ ] Confirm validation, transform, redaction/generalization, cultural/steward review, policy, model, and run receipts exist before catalog or release eligibility is asserted.
- [ ] Confirm EvidenceRef/EvidenceBundle and proof refs exist before consequential archaeology claims are used publicly.
- [ ] Confirm catalog refs point to STAC/DCAT/PROV/domain catalog records rather than embedding them here.
- [ ] Confirm release refs point to ReleaseManifest/PromotionDecision objects rather than implying publication from registry state.
- [ ] Confirm no public client, map layer, graph edge, vector index, generated answer, report, dashboard, fixture, or local index reads this registry lane as direct public truth.

---

## Status notes

| Claim | Status |
|---|---:|
| This README replaces the scaffold at `data/registry/sources/archaeology/README.md`. | CONFIRMED authored |
| The requested target path existed in the live repository as a scaffold before this edit. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/README.md` exists and frames registry records as governance/control records, not payloads, schemas, policy, receipts, proofs, catalogs, releases, or public output authority. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/sources/README.md` exists and frames `data/registry/sources/` as the pre-RAW source admission and authority-control surface. | CONFIRMED by GitHub contents API during this edit |
| `docs/domains/archaeology/README.md` identifies archaeology as T4/default sensitive and includes `data/registry/sources/archaeology/` as the source-descriptor lane in the domain pattern. | CONFIRMED by GitHub contents API during this edit |
| `docs/domains/archaeology/MISSING_OR_PLANNED_FILES.md` warns that exact archaeological geometry, burial/human-remains, sacred-site, collection-security, looting-risk, and private-landowner detail must not be exposed in public-readable paths. | CONFIRMED by GitHub contents API during this edit |
| The attached Directory Rules copy includes `data/registry/<domain>/` or `data/registry/sources/<domain>/` as valid registry/domain shapes. | CONFIRMED by local PDF text extraction during this edit |
| Concrete archaeology SourceDescriptor payloads exist under this lane. | UNKNOWN |
| Archaeology descriptor schema home, filename convention, validator discovery, and CI enforcement are verified. | NEEDS VERIFICATION |
| Archaeology rights/sensitivity/cultural-review policy profiles are complete. | UNKNOWN |
| Archaeology catalog/proof/release wiring is implemented. | UNKNOWN |
| Runtime registry resolution or governed API behavior reads this lane. | UNKNOWN |
| This README grants public access to archaeology source-registry internals. | DENY |

---

## Maintainer note

Archaeology source descriptors are useful because they preserve source identity, source role, rights, sensitivity, stewardship, cultural review, time scope, geography precision, uncertainty, correction, and rollback before data enters the KFM lifecycle. They become dangerous when treated as site truth, public release, or a shortcut around review and proof.

Keep the chain explicit:

```text
Archaeology SourceDescriptor -> rights/sensitivity/cultural-review gate -> RAW or QUARANTINE admission -> lifecycle processing -> validation/redaction/review receipts -> EvidenceBundle/proof -> catalog/triplet -> release -> governed public surface
```

Never collapse it into:

```text
source descriptor -> archaeology truth -> public map/API/generated answer
```
