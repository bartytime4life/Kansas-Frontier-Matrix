<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/sensitivity/flora/readme
name: Flora Sensitivity Registry README
path: data/registry/sensitivity/flora/README.md
type: data-registry-sensitivity-domain-readme
version: v0.2.0
status: draft
owners:
  - <registry-steward>
  - <sensitivity-steward>
  - <flora-domain-steward>
  - <botany-steward>
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
registry_scope: flora-sensitivity-registry-records
domain: flora
path_posture: existing-empty-placeholder-replaced; sensitivity-registry-parent-currently-greenfield-stub; subtype-first-sensitivity-registry-path-confirmed; flora-sensitivity-docs-overlap-conflicted; concrete-records-unknown
sensitivity_posture: registry-internal; no-public-path; rare-protected-culturally-sensitive-plant-location-t4-default; exact-sensitive-geometry-denied; culturally-sensitive-plant-knowledge-protected; steward-controlled-records-deny-default; rights-unclear-feeds-fail-closed; taxonomy-collisions-reviewed; join-induced-sensitivity-fail-closed; redaction-receipt-required; source-role-preserving; evidence-aware; rights-aware; policy-aware; release-blocked-until-gates-close
related:
  - ../README.md
  - ../../README.md
  - ../../sources/README.md
  - ../../sources/flora/
  - ../../flora/README.md
  - ../../flora/sources/README.md
  - ../../rights/README.md
  - ../../rights/flora/README.md
  - ../../domains/README.md
  - ../../datasets/README.md
  - ../../datasets/flora/README.md
  - ../../crosswalks/README.md
  - ../../layers/README.md
  - ../../layers/flora/README.md
  - ../../../raw/flora/
  - ../../../work/flora/
  - ../../../quarantine/flora/
  - ../../../processed/flora/
  - ../../../catalog/domain/flora/
  - ../../../catalog/stac/flora/README.md
  - ../../../published/layers/flora/
  - ../../../receipts/
  - ../../../proofs/
  - ../../../../docs/domains/flora/SENSITIVITY.md
  - ../../../../docs/domains/flora/RIGHTS_AND_SENSITIVITY.md
  - ../../../../docs/domains/flora/SOURCE_REGISTRY.md
  - ../../../../docs/domains/flora/SOURCE_FAMILIES.md
  - ../../../../docs/domains/flora/SOURCES.md
  - ../../../../docs/domains/flora/DATA_LIFECYCLE.md
  - ../../../../docs/domains/flora/PUBLICATION_AND_ROLLBACK.md
  - ../../../../docs/architecture/sensitivity.md
  - ../../../../docs/sources/catalog/gbif/async-download.md
  - ../../../../docs/sources/catalog/natureserve/sensitive-taxa-list.md
  - ../../../../docs/sources/catalog/kansas/kdwp.md
  - ../../../../contracts/domains/flora/
  - ../../../../schemas/contracts/v1/domains/flora/
  - ../../../../schemas/contracts/v1/receipts/
  - ../../../../policy/domains/flora/
  - ../../../../policy/sensitivity/flora/
  - ../../../../policy/geoprivacy/
  - ../../../../policy/rights/
  - ../../../../release/
tags:
  - kfm
  - data
  - registry
  - sensitivity
  - flora
  - deny-by-default
  - t4
  - geoprivacy
  - redaction
  - RedactionReceipt
  - rare-plants
  - protected-plants
  - culturally-sensitive-plants
  - exact-geometry
  - plant-occurrence
  - range-polygon
  - distribution-surface
  - steward-controlled-records
  - taxonomy-collisions
  - join-induced-sensitivity
  - source-role
  - evidence
  - provenance
  - release-gated
  - no-public-path
notes:
  - "This README replaces the empty placeholder at `data/registry/sensitivity/flora/README.md`."
  - "The parent `data/registry/sensitivity/README.md` is currently a greenfield stub, so sensitivity-registry topology and canonical record shape remain NEEDS VERIFICATION."
  - "Flora sensitivity registry records are registry/control records. They do not store source payloads, reveal exact sensitive plant locations, define policy, enforce schemas, hold receipts/proofs, close catalogs, or publish artifacts."
  - "Flora sensitivity docs are currently overlapping/conflicted candidates. This registry lane points to both and does not resolve their authority conflict."
  - "Exact rare, protected, or culturally sensitive plant locations fail closed unless governed redaction/review/release gates close."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Flora Sensitivity Registry

Subtype-first sensitivity-registry lane for Flora sensitivity-control records and release-readiness pointers.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: registry" src="https://img.shields.io/badge/family-registry-blueviolet">
  <img alt="Domain: flora" src="https://img.shields.io/badge/domain-flora-2ea44f">
  <img alt="Lane: sensitivity" src="https://img.shields.io/badge/lane-sensitivity-blue">
  <img alt="Default: T4 rare plants" src="https://img.shields.io/badge/default-T4%20rare%20plants-critical">
  <img alt="Exposure: no public path" src="https://img.shields.io/badge/exposure-no%20public%20path-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Flora sensitivity boundary](#flora-sensitivity-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Suggested directory shape](#suggested-directory-shape) · [Suggested registry shape](#suggested-registry-shape) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/registry/sensitivity/flora/` is a registry lane for Flora sensitivity-control records and sensitivity-readiness pointers. It is not RAW source storage, WORK staging, QUARANTINE, PROCESSED data, catalog output, proof storage, receipt storage, semantic contract authority, schema authority, policy, release authority, public API/UI material, exact sensitive-location storage, culturally sensitive plant-knowledge storage, or generated-answer authority.

---

## Scope

This directory documents and may hold Flora sensitivity registry records, registry-local indexes, sensitivity-tier mappings, sensitivity-rank mappings, redaction-profile refs, geoprivacy refs, steward-review refs, release-readiness pointers, and routing notes for Flora objects and derivatives.

A Flora sensitivity registry record may describe:

- stable subject identity for sensitivity review: source, occurrence record, rare/protected plant record, culturally sensitive plant record, taxon context, range polygon, vegetation community, distribution surface, derivative, layer, catalog item, release candidate, or published artifact;
- audience tier and per-record sensitivity rank posture where both are material;
- rare, protected, culturally sensitive, steward-controlled, rights-unclear, taxonomy-collision, private-parcel, and join-induced sensitivity posture;
- named redaction profile refs, geoprivacy transform refs, public-safe representation refs, aggregation refs, model-run refs, and review refs;
- exact/internal geometry denial posture and public-safe geometry constraints;
- links to SourceDescriptor records, rights review records, policy decisions, validation receipts, RedactionReceipts, AggregationReceipts, ModelRunReceipts, EvidenceBundle/proof refs, catalog refs, release refs, correction notices, withdrawal notices, and rollback cards;
- sensitivity blockers that prevent activation, processing, catalog closure, release, export, public display, AI response, map popup, vector index exposure, or tile exposure.

They do **not** reveal sensitive locations, store Flora payloads, grant access, define policy, enforce schemas, replace review, or authorize publication.

---

## Path posture

The requested and existing lane is:

```text
data/registry/sensitivity/flora/
```

This is a subtype-first registry path: registry family first (`sensitivity`), then domain (`flora`). The parent currently exists only as a greenfield stub:

```text
data/registry/sensitivity/README.md
```

Therefore, this README treats the target path as **CONFIRMED path presence / NEEDS VERIFICATION canonical shape**. Do not treat this README as proof that live sensitivity registry records, schema validation, policy integration, release integration, or governed API sensitivity resolution already exist.

Flora has overlapping sensitivity documentation: `docs/domains/flora/SENSITIVITY.md` and `docs/domains/flora/RIGHTS_AND_SENSITIVITY.md`. Both are useful evidence surfaces, but the overlap is a **CONFLICTED / NEEDS VERIFICATION** doctrine-shape issue until an ADR or drift-register decision selects a single canonical sensitivity home. This registry lane points to both and does not resolve that conflict.

Flora sensitivity doctrine points toward `policy/sensitivity/flora/` and `policy/geoprivacy/` for binding decisions. This registry lane should not duplicate policy. It should record sensitivity-review state and point to the policy, receipt, proof, catalog, release, correction, and rollback objects that carry authority.

---

## Repo fit

| Responsibility | Home | Boundary |
|---|---|---|
| Flora sensitivity registry records | `data/registry/sensitivity/flora/` | Sensitivity-review state, redaction/geoprivacy refs, blockers, and release-readiness pointers. |
| Sensitivity registry parent | `data/registry/sensitivity/README.md` | Parent is currently a greenfield stub; canonical parent contract remains NEEDS VERIFICATION. |
| Flora source descriptors | `data/registry/flora/sources/`, `data/registry/sources/flora/`, or accepted source registry lane | Source identity/admission records; sensitivity and geoprivacy posture may be pinned there and referenced here. |
| Flora domain registry parent | `data/registry/flora/` | Domain-first registry routing; not sensitivity policy or payload storage. |
| Flora rights records | `data/registry/rights/flora/` | Rights review state; not sensitivity policy. |
| Flora layer registry records | `data/registry/layers/flora/` | Layer identity and release-readiness refs; not sensitivity policy. |
| Flora source/lifecycle payloads | `data/raw/flora/`, `data/work/flora/`, `data/quarantine/flora/`, `data/processed/flora/` | Actual data belongs in lifecycle lanes, not sensitivity registry records. |
| Human-facing Flora sensitivity doctrine | `docs/domains/flora/SENSITIVITY.md`, `docs/domains/flora/RIGHTS_AND_SENSITIVITY.md` | Explains sensitivity, geoprivacy, rights, and release posture; overlapping authority needs reconciliation. |
| Cross-domain sensitivity architecture | `docs/architecture/sensitivity.md` | Architecture for deny-by-default posture. |
| Flora semantic meaning | `contracts/domains/flora/` | Object-family meaning and invariants. |
| Machine schemas | `schemas/contracts/v1/domains/flora/`, `schemas/contracts/v1/receipts/`, or ADR-selected schema lane | Schema enforcement; sensitivity-registry schema remains NEEDS VERIFICATION. |
| Sensitivity, geoprivacy, and rights policy | `policy/sensitivity/flora/`, `policy/domains/flora/`, `policy/geoprivacy/`, `policy/rights/` | Decisions and rules; registry records only point to policy outcomes. |
| Validation/redaction/policy/review receipts | `data/receipts/` and accepted Flora receipt lanes | Process memory for checks and public-safe transforms. |
| Proof/evidence | `data/proofs/` or accepted proof lanes | EvidenceBundle closure, proof packs, signatures, and citation validation. |
| Catalog projections | `data/catalog/domain/flora/`, `data/catalog/stac/flora/`, STAC/DCAT/PROV lanes, and triplet lanes | Catalog/discovery carriers after catalog closure. |
| Published artifacts | `data/published/layers/flora/` if/when accepted | Released public-safe artifacts and direct sidecars only. |
| Release decisions | `release/` | Promotion, correction, rollback, supersession, withdrawal, and release manifests. |
| Public surfaces | governed APIs and released artifacts only | Public clients do not read this registry lane directly. |

---

## Flora sensitivity boundary

| Rule | Handling |
|---|---|
| Registry record is control state | It records or points to sensitivity-review posture; it does not decide policy or grant access. |
| Rare/protected/culturally sensitive locations default to deny | Exact rare, protected, or culturally sensitive plant locations fail closed unless policy, steward review, transform receipts, release, correction, and rollback support explicitly permit a public-safe derivative. |
| Exact geometry is not public geometry | Exact/internal occurrence geometry, specimen locality, survey location, private-parcel detail, and steward-controlled detail must remain withheld unless a governed public-safe derivative is released. |
| Source quality never overrides sensitivity | A well-sourced, rights-clean, validated rare-plant record can still be unpublishable at exact precision. |
| Rights and sensitivity are separate gates | Passing rights does not relax sensitivity. Passing sensitivity does not clear rights. Both must close before public release. |
| RedactionReceipt is required for public-safe transforms | Generalization, aggregation, masking, withholding, or redaction must be receipted with named/versioned profile refs where required. |
| Culturally sensitive plant knowledge is protected | Cultural, sovereignty, CARE, traditional-knowledge, or steward-controlled context inherits the most restrictive applicable posture. |
| Join-induced sensitivity fails closed | Joins across occurrence, habitat, parcel, time, imagery, trail, land-use, herbarium, or public observations that reveal a sensitive location inherit the most restrictive applicable posture. |
| Taxonomy collisions need review | Taxon synonymy, ambiguous IDs, sensitive-taxa list joins, and name-resolution collisions must not silently downgrade sensitivity. |
| Modeled outputs keep uncertainty and sensitivity | Distribution surfaces, range polygons, habitat suitability, and model-derived layers are downstream carriers; they do not remove source-role, uncertainty, rights, or sensitivity obligations. |
| Source role is preserved | Observed, administrative, regulatory, modeled, aggregate, candidate, context, synthetic, or restricted source roles must not be upgraded by processing, map rendering, AI explanation, or release review. |
| Registry is not validation | Validation receipts, redaction receipts, review receipts, and run receipts remain separate process-memory objects. |
| Registry is not proof | EvidenceBundle/proof support remains separate. |
| Registry is not catalog | STAC/DCAT/PROV/domain catalog records and graph/triplet projections live under catalog/triplet lanes. |
| Registry is not release | Public exposure requires validation, policy, review, proof/catalog support, release manifest, correction path, and rollback path. |
| Public clients do not read this lane | Public UI/API surfaces consume governed APIs, released artifacts, catalog/triplet/proof-backed responses, and policy-safe envelopes. |

---

## Accepted material

Accepted content is limited to Flora sensitivity registry records and registry-local support files:

- sensitivity-family README files and registry-local indexes;
- sensitivity review records for sources, occurrence records, rare/protected plant records, culturally sensitive plant records, range products, model outputs, derivatives, layers, catalog items, release candidates, and published artifacts;
- audience tier refs, per-record sensitivity rank refs, sensitivity profile refs, redaction profile refs, geoprivacy refs, public-safe representation refs, aggregation refs, model-run refs, and review refs;
- steward-review refs, rights-holder refs, agency restriction refs, cultural/sovereignty/CARE refs, sensitive-taxa refs, private-parcel join refs, taxonomy-collision refs, and join-induced sensitivity refs;
- SourceDescriptor refs, rights refs, dataset refs, layer refs, catalog refs, release refs, and correction/rollback refs;
- validation receipt refs, RedactionReceipt refs, AggregationReceipt refs, RepresentationReceipt refs, ModelRunReceipt refs, policy receipt refs, review receipt refs, EvidenceBundle/proof refs;
- blocker records for missing sensitivity support, unresolved rights/steward review, missing receipt, missing release state, or risky cross-surface inference.

Keep records compact and pointer-based. Do not embed exact locations, source identifiers that can reconstruct sensitive locations, specimen locality strings, culturally sensitive plant knowledge, private-parcel detail, proof packs, policy decisions, catalog records, release manifests, or Flora claim content in this lane.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw Flora payloads, occurrence exports, specimen records, herbarium data, rare-plant locality records, sensitive-taxa lists with exposure risk, vegetation datasets, restoration records, phenology feeds, rasters, shapefiles, GeoParquet, COG, PMTiles, or source-native tables | `data/raw/flora/`, `data/work/flora/`, `data/quarantine/flora/`, or `data/processed/flora/` depending on lifecycle state |
| Exact sensitive plant coordinates, specimen locality strings, culturally sensitive plant knowledge, steward-only notes, private landowner details, restricted agency records, access secrets, or restricted review material | denied, restricted, quarantined, or routed to governed restricted storage |
| Source descriptor/admission records | `data/registry/flora/sources/` or `data/registry/sources/flora/` after topology reconciliation |
| Rights registry records | `data/registry/rights/flora/` |
| Dataset, crosswalk, domain, or layer registry records | `data/registry/datasets/`, `data/registry/crosswalks/`, `data/registry/domains/`, `data/registry/layers/` |
| Semantic object contracts | `contracts/domains/flora/` |
| JSON Schema | `schemas/contracts/v1/...` |
| Sensitivity policy, geoprivacy policy, rights policy, access-control logic, redaction policy, or release rules | `policy/` |
| Validation receipts, redaction receipts, policy receipts, review receipts, model receipts, or process-memory logs | `data/receipts/` |
| EvidenceBundle records, proof packs, signatures, or citation-validation closure | `data/proofs/` |
| STAC/DCAT/PROV/domain catalog records or graph/triplet projections | `data/catalog/` and `data/triplets/` |
| Published layers, reports, dashboards, tiles, API payloads, UI payloads, or generated-answer carriers | `data/published/`, governed app/API roots, and release-approved public artifact lanes |
| ReleaseManifest, PromotionDecision, CorrectionNotice, RollbackCard, withdrawal notice, or supersession notice | `release/` |
| Validator code, connector code, pipelines, fixtures, tests, or CI workflows | `tools/`, `connectors/`, `pipelines/`, `fixtures/`, `tests/`, `.github/workflows/` |

---

## Suggested directory shape

The map below is **PROPOSED** documentation guidance, not proof that child folders or records exist.

```text
data/registry/sensitivity/flora/
├── README.md
├── rare_protected_locations/
│   ├── README.md
│   └── index.local.json
├── culturally_sensitive_plants/
│   ├── README.md
│   └── index.local.json
├── steward_controlled_records/
│   ├── README.md
│   └── index.local.json
├── join_induced_sensitivity/
│   ├── README.md
│   └── index.local.json
├── taxonomy_collisions/
│   ├── README.md
│   └── index.local.json
├── range_products/
│   ├── README.md
│   └── index.local.json
├── distribution_surfaces/
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

Do not create a new child lane until the sensitivity object family, source descriptor refs, sensitivity/rank refs, policy refs, review state, receipt refs, release refs, and rollback path are known.

---

## Suggested registry shape

The exact sensitivity-registry schema remains **NEEDS VERIFICATION**. A Flora sensitivity registry record should be structured enough for audit, public-safe transformation, release readiness, correction, withdrawal, and rollback.

```json
{
  "id": "kfm-sensitivity:flora:<stable-sensitivity-id>",
  "record_type": "sensitivity_registry_record",
  "domain": "flora",
  "sensitivity_family": "rare_protected_locations | culturally_sensitive_plants | steward_controlled_records | join_induced_sensitivity | taxonomy_collisions | range_products | distribution_surfaces | redaction_profiles | review_queue | other",
  "subject_ref": "source | record | taxon | object_family | derivative | model_output | layer | catalog_item | release_candidate | published_artifact",
  "audience_tier": "T0 | T1 | T2 | T3 | T4 | needs-review",
  "sensitivity_rank": "0 | 1 | 2 | 3 | 4 | 5 | needs-review",
  "source_registry_refs": [],
  "rights_registry_refs": [],
  "policy_refs": [],
  "redaction_profile_refs": [],
  "geoprivacy_refs": [],
  "steward_review_refs": [],
  "cultural_sovereignty_refs": [],
  "sensitive_taxa_refs": [],
  "taxonomy_review_refs": [],
  "private_parcel_join_refs": [],
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

- [ ] Confirm the sensitivity record belongs in `data/registry/sensitivity/flora/`, not source payloads, policy, contracts, schemas, receipts, proofs, catalog, published artifacts, or release lanes.
- [ ] Confirm the subject of the sensitivity review is identified: source, record, taxon, object family, derivative, model output, layer, catalog item, release candidate, published artifact, or other reviewed object.
- [ ] Confirm audience tier and per-record sensitivity rank are both present where material and are not collapsed into one field.
- [ ] Confirm exact rare/protected/culturally sensitive plant locations, culturally sensitive plant knowledge, steward-controlled records, taxonomy collisions, and join-induced sensitive outputs fail closed.
- [ ] Confirm sensitivity evidence exists before asserting any public-safe tier, transform, audience, or display eligibility.
- [ ] Confirm named/versioned redaction or aggregation profile refs and required receipt refs exist before any public-safe transformation is asserted.
- [ ] Confirm rights-holder, agency, landowner, steward-review, cultural/sovereignty/CARE, policy, and review requirements are current before any use beyond restricted processing.
- [ ] Confirm map popups, exports, AI text, vector indexes, tile surfaces, and cross-domain joins do not leak restricted detail through inference.
- [ ] Confirm sensitivity state does not override rights, source-role, evidence closure, catalog closure, policy decision, review state, or release state.
- [ ] Confirm validation receipts, redaction receipts, aggregation receipts, model receipts, policy outcomes, and review records exist before catalog or release eligibility is asserted.
- [ ] Confirm EvidenceRef/EvidenceBundle and proof refs exist for consequential use.
- [ ] Confirm release refs point to ReleaseManifest/PromotionDecision objects rather than implying publication from sensitivity state.
- [ ] Confirm correction, supersession, withdrawal, stale-state, and rollback paths exist for changed sensitivity, rights-holder decision, steward review, or release posture.
- [ ] Confirm no public client, map layer, graph edge, vector index, generated answer, report, or dashboard reads this registry lane as direct public truth or permission.

---

## Status notes

| Claim | Status |
|---|---:|
| This README replaces the empty placeholder at `data/registry/sensitivity/flora/README.md`. | CONFIRMED authored |
| The target path existed in the live repository as an empty placeholder before this edit. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/sensitivity/README.md` exists and is currently a greenfield stub. | CONFIRMED by GitHub contents API during this edit |
| Flora sensitivity docs say exact rare, protected, or culturally sensitive plant locations are denied on public surfaces by default and require steward review, generalized/withheld geometry, and RedactionReceipt before public release. | CONFIRMED by GitHub contents API during this edit |
| Flora sensitivity docs warn that overlapping Flora sensitivity surfaces are conflicted candidates until ADR/drift-register reconciliation. | CONFIRMED by GitHub contents API during this edit |
| Flora rights/sensitivity docs say rights and sensitivity are distinct, independently fail-closed checks. | CONFIRMED by GitHub contents API during this edit |
| Flora registry and source registry READMEs say rare-plant exact geometry, culturally sensitive plant knowledge, steward-controlled records, rights-unclear feeds, taxonomy collisions, and join-induced sensitivity fail closed until governed redaction/review/release gates close. | CONFIRMED by GitHub contents API during this edit |
| Concrete Flora sensitivity registry payloads exist under this requested lane. | UNKNOWN |
| The final accepted parent contract for `data/registry/sensitivity/` is resolved. | NEEDS VERIFICATION |
| A canonical Flora sensitivity registry schema is enforced. | NEEDS VERIFICATION |
| CI validates Flora sensitivity registry records. | UNKNOWN |
| This README grants public access to Flora sensitivity registry internals. | DENY |

---

## Maintainer note

Flora sensitivity registry records are useful because they make sensitivity posture, redaction/geoprivacy refs, steward-review state, culturally sensitive plant handling, release readiness, correction, and rollback inspectable before any Flora object approaches a public surface. They become dangerous when treated as policy, source payloads, exact-location storage, proof closure, catalog closure, release decisions, or permission.

Keep the safe chain explicit:

```text
sensitivity registry record -> source/object refs -> policy/review outcome -> lifecycle payload -> validation/redaction/aggregation/model receipt -> proof/catalog -> release -> governed public surface
```

Never collapse it into:

```text
sensitivity registry record -> public Flora permission
```
