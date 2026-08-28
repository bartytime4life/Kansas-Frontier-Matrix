<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/sensitivity/fauna/readme
name: Fauna Sensitivity Registry README
path: data/registry/sensitivity/fauna/README.md
type: data-registry-sensitivity-domain-readme
version: v0.2.0
status: draft
owners:
  - <registry-steward>
  - <sensitivity-steward>
  - <fauna-domain-steward>
  - <wildlife-steward>
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
registry_scope: fauna-sensitivity-registry-records
domain: fauna
path_posture: existing-empty-placeholder-replaced; sensitivity-registry-parent-currently-greenfield-stub; subtype-first-sensitivity-registry-path-confirmed; concrete-records-unknown
sensitivity_posture: registry-internal; no-public-path; sensitive-occurrence-t4-default; exact-sensitive-geometry-denied; nests-dens-roosts-hibernacula-spawning-sites-fail-closed; steward-controlled-records-deny-default; re-identifying-joins-fail-closed; redaction-receipt-required; source-role-preserving; evidence-aware; rights-aware; policy-aware; release-blocked-until-gates-close
related:
  - ../README.md
  - ../../README.md
  - ../../sources/README.md
  - ../../sources/fauna/
  - ../../fauna/README.md
  - ../../fauna/sources/README.md
  - ../../rights/README.md
  - ../../domains/README.md
  - ../../datasets/README.md
  - ../../crosswalks/README.md
  - ../../layers/README.md
  - ../../../raw/fauna/
  - ../../../work/fauna/
  - ../../../quarantine/fauna/
  - ../../../processed/fauna/
  - ../../../catalog/domain/fauna/
  - ../../../published/layers/fauna/
  - ../../../receipts/
  - ../../../proofs/
  - ../../../../docs/domains/fauna/SENSITIVITY.md
  - ../../../../docs/domains/fauna/SOURCE_REGISTRY.md
  - ../../../../docs/domains/fauna/SOURCE_ROLES.md
  - ../../../../docs/domains/fauna/SOURCE_FAMILIES.md
  - ../../../../docs/domains/fauna/DATA_LIFECYCLE.md
  - ../../../../docs/architecture/sensitivity.md
  - ../../../../docs/sources/catalog/kansas/kdwp.md
  - ../../../../docs/sources/catalog/usfws_ecos/esa-listing-status.md
  - ../../../../contracts/domains/fauna/
  - ../../../../schemas/contracts/v1/domains/fauna/
  - ../../../../schemas/contracts/v1/receipts/
  - ../../../../policy/domains/fauna/
  - ../../../../policy/sensitivity/fauna/
  - ../../../../policy/geoprivacy/
  - ../../../../policy/rights/
  - ../../../../release/
tags:
  - kfm
  - data
  - registry
  - sensitivity
  - fauna
  - deny-by-default
  - t4
  - geoprivacy
  - redaction
  - RedactionReceipt
  - sensitive-occurrence
  - sensitive-site
  - exact-geometry
  - nests
  - dens
  - roosts
  - hibernacula
  - spawning-sites
  - steward-controlled-records
  - re-identifying-joins
  - source-role
  - evidence
  - provenance
  - release-gated
  - no-public-path
notes:
  - "This README replaces the empty placeholder at `data/registry/sensitivity/fauna/README.md`."
  - "The parent `data/registry/sensitivity/README.md` is currently a greenfield stub, so sensitivity-registry topology and canonical record shape remain NEEDS VERIFICATION."
  - "Fauna sensitivity registry records are registry/control records. They do not store source payloads, reveal exact sensitive animal locations, define policy, enforce schemas, hold receipts/proofs, close catalogs, or publish artifacts."
  - "Exact sensitive-taxon geometry, nests, dens, roosts, hibernacula, spawning sites, steward-controlled records, and re-identifying joins fail closed unless governed redaction/review/release gates close."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Fauna Sensitivity Registry

Subtype-first sensitivity-registry lane for Fauna sensitivity-control records and release-readiness pointers.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: registry" src="https://img.shields.io/badge/family-registry-blueviolet">
  <img alt="Domain: fauna" src="https://img.shields.io/badge/domain-fauna-2e8b57">
  <img alt="Lane: sensitivity" src="https://img.shields.io/badge/lane-sensitivity-blue">
  <img alt="Default: T4 sensitive occurrence" src="https://img.shields.io/badge/default-T4%20sensitive%20occurrence-critical">
  <img alt="Exposure: no public path" src="https://img.shields.io/badge/exposure-no%20public%20path-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Fauna sensitivity boundary](#fauna-sensitivity-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Suggested directory shape](#suggested-directory-shape) · [Suggested registry shape](#suggested-registry-shape) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/registry/sensitivity/fauna/` is a registry lane for Fauna sensitivity-control records and sensitivity-readiness pointers. It is not RAW source storage, WORK staging, QUARANTINE, PROCESSED data, catalog output, proof storage, receipt storage, semantic contract authority, schema authority, policy, release authority, public API/UI material, exact sensitive-location storage, or generated-answer authority.

---

## Scope

This directory documents and may hold Fauna sensitivity registry records, registry-local indexes, sensitivity-rank mappings, audience-tier mappings, redaction-profile refs, geoprivacy refs, steward-review refs, release-readiness pointers, and routing notes for Fauna objects and derivatives.

A Fauna sensitivity registry record may describe:

- stable subject identity for sensitivity review: source, occurrence record, sensitive site, taxon context, range polygon, derivative, layer, catalog item, release candidate, or published artifact;
- audience tier and per-record sensitivity rank posture when both are material;
- sensitive occurrence, nest, den, roost, hibernacula, spawning site, migration stopover, private-parcel join, steward-controlled record, and re-identifying-join posture;
- named redaction profile refs, geoprivacy transform refs, public-safe representation refs, aggregation refs, and review refs;
- exact/internal geometry denial posture and public-safe geometry constraints;
- links to SourceDescriptor records, rights review records, policy decisions, validation receipts, RedactionReceipts, AggregationReceipts, EvidenceBundle/proof refs, catalog refs, release refs, correction notices, withdrawal notices, and rollback cards;
- sensitivity blockers that prevent activation, processing, catalog closure, release, export, public display, AI response, map popup, vector index exposure, or tile exposure.

They do **not** reveal sensitive locations, store Fauna payloads, grant access, define policy, enforce schemas, replace review, or authorize publication.

---

## Path posture

The requested and existing lane is:

```text
data/registry/sensitivity/fauna/
```

This is a subtype-first registry path: registry family first (`sensitivity`), then domain (`fauna`). The parent currently exists only as a greenfield stub:

```text
data/registry/sensitivity/README.md
```

Therefore, this README treats the target path as **CONFIRMED path presence / NEEDS VERIFICATION canonical shape**. Do not treat this README as proof that live sensitivity registry records, schema validation, policy integration, release integration, or governed API sensitivity resolution already exist.

Fauna sensitivity doctrine points toward `policy/sensitivity/fauna/` and `policy/domains/fauna/` for binding admissibility rules. This registry lane should not duplicate policy. It should record sensitivity-review state and point to the policy, receipt, proof, catalog, release, correction, and rollback objects that carry authority.

---

## Repo fit

| Responsibility | Home | Boundary |
|---|---|---|
| Fauna sensitivity registry records | `data/registry/sensitivity/fauna/` | Sensitivity-review state, redaction/geoprivacy refs, blockers, and release-readiness pointers. |
| Sensitivity registry parent | `data/registry/sensitivity/README.md` | Parent is currently a greenfield stub; canonical parent contract remains NEEDS VERIFICATION. |
| Fauna source descriptors | `data/registry/fauna/sources/`, `data/registry/sources/fauna/`, or accepted source registry lane | Source identity/admission records; sensitivity and geoprivacy posture may be pinned there and referenced here. |
| Fauna domain registry parent | `data/registry/fauna/` | Domain-first registry routing; not sensitivity policy or payload storage. |
| Fauna rights records | `data/registry/rights/fauna/` if/when accepted | Rights review state; not sensitivity policy. |
| Fauna source/lifecycle payloads | `data/raw/fauna/`, `data/work/fauna/`, `data/quarantine/fauna/`, `data/processed/fauna/` | Actual data belongs in lifecycle lanes, not sensitivity registry records. |
| Human-facing Fauna sensitivity doctrine | `docs/domains/fauna/SENSITIVITY.md` | Explains sensitivity and geoprivacy posture; not registry storage. |
| Cross-domain sensitivity architecture | `docs/architecture/sensitivity.md` | Architecture for deny-by-default posture. |
| Fauna semantic meaning | `contracts/domains/fauna/` | Object-family meaning and invariants. |
| Machine schemas | `schemas/contracts/v1/domains/fauna/`, `schemas/contracts/v1/receipts/`, or ADR-selected schema lane | Schema enforcement; sensitivity-registry schema remains NEEDS VERIFICATION. |
| Sensitivity, geoprivacy, and rights policy | `policy/sensitivity/fauna/`, `policy/domains/fauna/`, `policy/geoprivacy/`, `policy/rights/` | Decisions and rules; registry records only point to policy outcomes. |
| Validation/redaction/policy/review receipts | `data/receipts/` and accepted Fauna receipt lanes | Process memory for checks and public-safe transforms. |
| Proof/evidence | `data/proofs/` or accepted proof lanes | EvidenceBundle closure, proof packs, signatures, and citation validation. |
| Catalog projections | `data/catalog/domain/fauna/`, STAC/DCAT/PROV lanes, and triplet lanes | Catalog/discovery carriers after catalog closure. |
| Published artifacts | `data/published/layers/fauna/` if/when accepted | Released public-safe artifacts and direct sidecars only. |
| Release decisions | `release/` | Promotion, correction, rollback, supersession, withdrawal, and release manifests. |
| Public surfaces | governed APIs and released artifacts only | Public clients do not read this registry lane directly. |

---

## Fauna sensitivity boundary

| Rule | Handling |
|---|---|
| Registry record is control state | It records or points to sensitivity-review posture; it does not decide policy or grant access. |
| Sensitive occurrence defaults to deny | Exact sensitive-taxon occurrence geometry fails closed unless policy, steward review, transform receipts, release, correction, and rollback support explicitly permit a public-safe derivative. |
| Sensitive sites default to deny | Nests, dens, roosts, hibernacula, spawning sites, and similar sensitive site classes are denied at exact precision by default. |
| Existence is not location | A public-safe statement that a record exists is not permission to expose exact geometry, source identifiers, or enough joined detail to reconstruct location. |
| Audience tier and record rank are distinct | T0–T4 audience tier and per-record sensitivity rank are separate rubrics where both are used; do not silently merge them. |
| Exact geometry is not public geometry | Exact/internal geometry, sensor traces, telemetry points, survey locations, and steward-controlled detail must remain withheld unless a governed public-safe derivative is released. |
| RedactionReceipt is required for public-safe transforms | Generalization, aggregation, masking, withholding, or redaction must be receipted with named/versioned profile refs where required. |
| Re-identifying joins fail closed | Joins across occurrence, habitat, parcel, time, imagery, route, or public observations that reveal a sensitive location inherit the most restrictive applicable posture. |
| Steward-controlled records remain restricted | Agency, tribal, landowner, researcher, or other steward-controlled records require rights-holder/steward review before any exposure beyond restricted processing. |
| Source role is preserved | Observed, administrative, regulatory, modeled, aggregate, candidate, context, synthetic, or restricted source roles must not be upgraded by processing, map rendering, AI explanation, or release review. |
| Registry is not validation | Validation receipts, redaction receipts, review receipts, and run receipts remain separate process-memory objects. |
| Registry is not proof | EvidenceBundle/proof support remains separate. |
| Registry is not catalog | STAC/DCAT/PROV/domain catalog records and graph/triplet projections live under catalog/triplet lanes. |
| Registry is not release | Public exposure requires validation, policy, review, proof/catalog support, release manifest, correction path, and rollback path. |
| Public clients do not read this lane | Public UI/API surfaces consume governed APIs, released artifacts, catalog/triplet/proof-backed responses, and policy-safe envelopes. |

---

## Accepted material

Accepted content is limited to Fauna sensitivity registry records and registry-local support files:

- sensitivity-family README files and registry-local indexes;
- sensitivity review records for sources, occurrence records, sensitive sites, range products, derivatives, layers, catalog items, release candidates, and published artifacts;
- audience tier refs, per-record sensitivity rank refs, sensitivity profile refs, redaction profile refs, geoprivacy refs, public-safe representation refs, aggregation refs, and review refs;
- steward-review refs, rights-holder refs, agency restriction refs, landowner restriction refs, sensitive-taxa refs, private-parcel join refs, and re-identifying-join refs;
- SourceDescriptor refs, rights refs, dataset refs, layer refs, catalog refs, release refs, and correction/rollback refs;
- validation receipt refs, RedactionReceipt refs, AggregationReceipt refs, RepresentationReceipt refs, policy receipt refs, review receipt refs, EvidenceBundle/proof refs;
- blocker records for missing sensitivity support, unresolved rights/steward review, missing receipt, missing release state, or risky cross-surface inference.

Keep records compact and pointer-based. Do not embed exact locations, source identifiers that can reconstruct sensitive locations, telemetry traces, nest/den/roost/hibernacula/spawning-site detail, private-parcel detail, proof packs, policy decisions, catalog records, release manifests, or Fauna claim content in this lane.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw Fauna payloads, occurrence exports, survey records, telemetry, camera-trap records, sensitive-taxa lists with exposure risk, nest/den/roost/hibernacula/spawning site records, rasters, shapefiles, GeoParquet, COG, PMTiles, or source-native tables | `data/raw/fauna/`, `data/work/fauna/`, `data/quarantine/fauna/`, or `data/processed/fauna/` depending on lifecycle state |
| Exact sensitive-taxon coordinates, sensitive site detail, steward-only notes, private landowner details, restricted agency records, access secrets, or restricted review material | denied, restricted, quarantined, or routed to governed restricted storage |
| Source descriptor/admission records | `data/registry/fauna/sources/` or `data/registry/sources/fauna/` after topology reconciliation |
| Rights registry records | `data/registry/rights/fauna/` after accepted topology |
| Dataset, crosswalk, domain, or layer registry records | `data/registry/datasets/`, `data/registry/crosswalks/`, `data/registry/domains/`, `data/registry/layers/` |
| Semantic object contracts | `contracts/domains/fauna/` |
| JSON Schema | `schemas/contracts/v1/...` |
| Sensitivity policy, geoprivacy policy, rights policy, access-control logic, redaction policy, or release rules | `policy/` |
| Validation receipts, redaction receipts, policy receipts, review receipts, or process-memory logs | `data/receipts/` |
| EvidenceBundle records, proof packs, signatures, or citation-validation closure | `data/proofs/` |
| STAC/DCAT/PROV/domain catalog records or graph/triplet projections | `data/catalog/` and `data/triplets/` |
| Published layers, reports, dashboards, tiles, API payloads, UI payloads, or generated-answer carriers | `data/published/`, governed app/API roots, and release-approved public artifact lanes |
| ReleaseManifest, PromotionDecision, CorrectionNotice, RollbackCard, withdrawal notice, or supersession notice | `release/` |
| Validator code, connector code, pipelines, fixtures, tests, or CI workflows | `tools/`, `connectors/`, `pipelines/`, `fixtures/`, `tests/`, `.github/workflows/` |

---

## Suggested directory shape

The map below is **PROPOSED** documentation guidance, not proof that child folders or records exist.

```text
data/registry/sensitivity/fauna/
├── README.md
├── sensitive_occurrences/
│   ├── README.md
│   └── index.local.json
├── sensitive_sites/
│   ├── README.md
│   └── index.local.json
├── steward_controlled_records/
│   ├── README.md
│   └── index.local.json
├── reidentifying_joins/
│   ├── README.md
│   └── index.local.json
├── range_products/
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

The exact sensitivity-registry schema remains **NEEDS VERIFICATION**. A Fauna sensitivity registry record should be structured enough for audit, public-safe transformation, release readiness, correction, withdrawal, and rollback.

```json
{
  "id": "kfm-sensitivity:fauna:<stable-sensitivity-id>",
  "record_type": "sensitivity_registry_record",
  "domain": "fauna",
  "sensitivity_family": "sensitive_occurrences | sensitive_sites | steward_controlled_records | reidentifying_joins | range_products | redaction_profiles | review_queue | other",
  "subject_ref": "source | record | object_family | derivative | layer | catalog_item | release_candidate | published_artifact",
  "audience_tier": "T0 | T1 | T2 | T3 | T4 | needs-review",
  "sensitivity_rank": "0 | 1 | 2 | 3 | 4 | 5 | needs-review",
  "source_registry_refs": [],
  "rights_registry_refs": [],
  "policy_refs": [],
  "redaction_profile_refs": [],
  "geoprivacy_refs": [],
  "steward_review_refs": [],
  "sensitive_taxa_refs": [],
  "private_parcel_join_refs": [],
  "validation_receipt_refs": [],
  "redaction_receipt_refs": [],
  "aggregation_receipt_refs": [],
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

- [ ] Confirm the sensitivity record belongs in `data/registry/sensitivity/fauna/`, not source payloads, policy, contracts, schemas, receipts, proofs, catalog, published artifacts, or release lanes.
- [ ] Confirm the subject of the sensitivity review is identified: source, record, object family, derivative, layer, catalog item, release candidate, published artifact, or other reviewed object.
- [ ] Confirm audience tier and per-record sensitivity rank are both present where material and are not collapsed into one field.
- [ ] Confirm exact sensitive-taxon occurrence geometry, nests, dens, roosts, hibernacula, spawning sites, steward-controlled records, and re-identifying joins fail closed.
- [ ] Confirm sensitivity evidence exists before asserting any public-safe tier, transform, audience, or display eligibility.
- [ ] Confirm named/versioned redaction or aggregation profile refs and required receipt refs exist before any public-safe transformation is asserted.
- [ ] Confirm rights-holder, agency, landowner, steward-review, policy, and review requirements are current before any use beyond restricted processing.
- [ ] Confirm map popups, exports, AI text, vector indexes, tile surfaces, and cross-domain joins do not leak restricted detail through inference.
- [ ] Confirm sensitivity state does not override rights, source-role, evidence closure, catalog closure, policy decision, review state, or release state.
- [ ] Confirm validation receipts, redaction receipts, aggregation receipts, policy outcomes, and review records exist before catalog or release eligibility is asserted.
- [ ] Confirm EvidenceRef/EvidenceBundle and proof refs exist for consequential use.
- [ ] Confirm release refs point to ReleaseManifest/PromotionDecision objects rather than implying publication from sensitivity state.
- [ ] Confirm correction, supersession, withdrawal, stale-state, and rollback paths exist for changed sensitivity, rights-holder decision, steward review, or release posture.
- [ ] Confirm no public client, map layer, graph edge, vector index, generated answer, report, or dashboard reads this registry lane as direct public truth or permission.

---

## Status notes

| Claim | Status |
|---|---:|
| This README replaces the empty placeholder at `data/registry/sensitivity/fauna/README.md`. | CONFIRMED authored |
| The target path existed in the live repository as an empty placeholder before this edit. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/sensitivity/README.md` exists and is currently a greenfield stub. | CONFIRMED by GitHub contents API during this edit |
| Fauna sensitivity docs state the lane fails closed for exact sensitive-taxon occurrence, nests, dens, roosts, hibernacula, and spawning sites, and does not name exact coordinates or transform parameters. | CONFIRMED by GitHub contents API during this edit |
| Fauna sensitivity docs distinguish the T0–T4 audience-tier scheme from the per-record sensitivity-rank rubric and warn not to silently merge them. | CONFIRMED by GitHub contents API during this edit |
| General sensitivity architecture says deny-by-default means missing rights, sovereignty, sensitivity, or release-state evidence fails closed. | CONFIRMED by GitHub contents API during this sequence |
| Fauna source registry README states source descriptors record sensitivity/geoprivacy posture and do not record animal truth; exact occurrence geometry and sensitive sites remain deny-by-default until governed redaction/review/release gates close. | CONFIRMED by GitHub contents API during this edit |
| Concrete Fauna sensitivity registry payloads exist under this requested lane. | UNKNOWN |
| The final accepted parent contract for `data/registry/sensitivity/` is resolved. | NEEDS VERIFICATION |
| A canonical Fauna sensitivity registry schema is enforced. | NEEDS VERIFICATION |
| CI validates Fauna sensitivity registry records. | UNKNOWN |
| This README grants public access to Fauna sensitivity registry internals. | DENY |

---

## Maintainer note

Fauna sensitivity registry records are useful because they make sensitivity posture, redaction/geoprivacy refs, steward-review state, release readiness, correction, and rollback inspectable before any Fauna object approaches a public surface. They become dangerous when treated as policy, source payloads, exact-location storage, proof closure, catalog closure, release decisions, or permission.

Keep the safe chain explicit:

```text
sensitivity registry record -> source/object refs -> policy/review outcome -> lifecycle payload -> validation/redaction/aggregation receipt -> proof/catalog -> release -> governed public surface
```

Never collapse it into:

```text
sensitivity registry record -> public Fauna permission
```
