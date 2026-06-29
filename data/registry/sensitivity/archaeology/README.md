<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/sensitivity/archaeology/readme
name: Archaeology Sensitivity Registry README
path: data/registry/sensitivity/archaeology/README.md
type: data-registry-sensitivity-domain-readme
version: v0.2.0
status: draft
owners:
  - <registry-steward>
  - <sensitivity-steward>
  - <archaeology-domain-steward>
  - <sovereignty-reviewer>
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
registry_scope: archaeology-sensitivity-registry-records
domain: archaeology
path_posture: existing-empty-placeholder-replaced; sensitivity-registry-parent-currently-greenfield-stub; subtype-first-sensitivity-registry-path-confirmed; concrete-records-unknown
sensitivity_posture: registry-internal; no-public-path; archaeology-default-t4-deny; exact-site-geometry-denied; human-remains-and-sacred-sites-fail-closed; sovereignty-and-care-aware; redaction-receipt-required; source-role-preserving; evidence-aware; rights-aware; policy-aware; release-blocked-until-gates-close
related:
  - ../README.md
  - ../../README.md
  - ../../sources/README.md
  - ../../sources/archaeology/
  - ../../rights/README.md
  - ../../domains/README.md
  - ../../datasets/README.md
  - ../../crosswalks/README.md
  - ../../layers/README.md
  - ../../../raw/archaeology/
  - ../../../work/archaeology/
  - ../../../quarantine/archaeology/
  - ../../../processed/archaeology/
  - ../../../catalog/domain/archaeology/
  - ../../../published/layers/archaeology/
  - ../../../receipts/archaeology/
  - ../../../proofs/archaeology/
  - ../../../../docs/domains/archaeology/SENSITIVITY.md
  - ../../../../docs/domains/archaeology/MAP_UI_CONTRACTS.md
  - ../../../../docs/domains/archaeology/PUBLICATION_AND_POLICY.md
  - ../../../../docs/domains/archaeology/PRESERVATION_MATRIX.md
  - ../../../../docs/domains/archaeology/RELEASE_INDEX.md
  - ../../../../docs/architecture/sensitivity.md
  - ../../../../docs/doctrine/sensitivity.md
  - ../../../../contracts/domains/archaeology/
  - ../../../../schemas/contracts/v1/domains/archaeology/
  - ../../../../schemas/contracts/v1/receipts/
  - ../../../../policy/domains/archaeology/
  - ../../../../policy/sensitivity/archaeology/
  - ../../../../policy/geoprivacy/
  - ../../../../policy/consent/archaeology/
  - ../../../../policy/rights/
  - ../../../../release/
tags:
  - kfm
  - data
  - registry
  - sensitivity
  - archaeology
  - deny-by-default
  - t4
  - geoprivacy
  - redaction
  - RedactionReceipt
  - CARE
  - sovereignty
  - sacred-sites
  - human-remains
  - site-location
  - looting-risk
  - cultural-knowledge
  - consent
  - revocation
  - embargo
  - source-role
  - evidence
  - provenance
  - release-gated
  - no-public-path
notes:
  - "This README replaces the empty placeholder at `data/registry/sensitivity/archaeology/README.md`."
  - "The parent `data/registry/sensitivity/README.md` is currently a greenfield stub, so sensitivity-registry topology and canonical record shape remain NEEDS VERIFICATION."
  - "Archaeology sensitivity registry records are registry/control records. They do not store source payloads, reveal site geometry, define policy, enforce schemas, hold receipts/proofs, close catalogs, or publish artifacts."
  - "Exact archaeology site geometry, human remains, sacred sites, collection-security details, oral-history/cultural-knowledge restricted context, and looting-risk exposure fail closed unless governed review, redaction, receipts, release, correction, and rollback gates close."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Archaeology Sensitivity Registry

Subtype-first sensitivity-registry lane for Archaeology sensitivity-control records and release-readiness pointers.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: registry" src="https://img.shields.io/badge/family-registry-blueviolet">
  <img alt="Domain: archaeology" src="https://img.shields.io/badge/domain-archaeology-8B5A2B">
  <img alt="Lane: sensitivity" src="https://img.shields.io/badge/lane-sensitivity-blue">
  <img alt="Default: T4 deny" src="https://img.shields.io/badge/default-T4%20DENY-critical">
  <img alt="Exposure: no public path" src="https://img.shields.io/badge/exposure-no%20public%20path-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Archaeology sensitivity boundary](#archaeology-sensitivity-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Suggested directory shape](#suggested-directory-shape) · [Suggested registry shape](#suggested-registry-shape) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/registry/sensitivity/archaeology/` is a registry lane for Archaeology sensitivity-control records and sensitivity-readiness pointers. It is not RAW source storage, WORK staging, QUARANTINE, PROCESSED data, catalog output, proof storage, receipt storage, semantic contract authority, schema authority, policy, release authority, public API/UI material, exact site-location storage, or generated-answer authority.

---

## Scope

This directory documents and may hold Archaeology sensitivity registry records, registry-local indexes, sensitivity-rank mappings, audience-tier mappings, redaction-profile refs, sovereignty/CARE refs, embargo/revocation refs, release-readiness pointers, and routing notes for Archaeology objects and derivatives.

An Archaeology sensitivity registry record may describe:

- stable subject identity for sensitivity review: source, record, site candidate, survey feature, object family, derivative, layer, catalog item, release candidate, or published artifact;
- audience tier and per-record sensitivity rank posture;
- sovereignty, CARE, consent, revocation, embargo, rights-holder, and reviewer requirements;
- named redaction profile refs, geoprivacy transform refs, generalization refs, differential-privacy or k-anonymity refs where applicable;
- exact/internal geometry denial posture and public-safe geometry constraints;
- links to SourceDescriptor records, policy decisions, validation receipts, RedactionReceipts, EvidenceBundle/proof refs, catalog refs, release refs, correction notices, withdrawal notices, and rollback cards;
- sensitivity blockers that prevent activation, processing, catalog closure, release, export, public display, AI response, map popup, or tile exposure.

They do **not** reveal sensitive locations, store archaeological payloads, grant access, define policy, enforce schemas, replace review, or authorize publication.

---

## Path posture

The requested and existing lane is:

```text
data/registry/sensitivity/archaeology/
```

This is a subtype-first registry path: registry family first (`sensitivity`), then domain (`archaeology`). The parent currently exists only as a greenfield stub:

```text
data/registry/sensitivity/README.md
```

Therefore, this README treats the target path as **CONFIRMED path presence / NEEDS VERIFICATION canonical shape**. Do not treat this README as proof that live sensitivity registry records, schema validation, policy integration, release integration, or governed API sensitivity resolution already exist.

Archaeology sensitivity doctrine points toward `policy/sensitivity/archaeology/` for decisions and policy enforcement. This registry lane should not duplicate policy. It should record sensitivity-review state and point to the policy, receipt, proof, catalog, release, correction, and rollback objects that carry authority.

---

## Repo fit

| Responsibility | Home | Boundary |
|---|---|---|
| Archaeology sensitivity registry records | `data/registry/sensitivity/archaeology/` | Sensitivity-review state, redaction profile refs, sovereignty/CARE refs, blockers, and release-readiness pointers. |
| Sensitivity registry parent | `data/registry/sensitivity/README.md` | Parent is currently a greenfield stub; canonical parent contract remains NEEDS VERIFICATION. |
| Archaeology source descriptors | `data/registry/sources/archaeology/` or accepted domain source registry lane | Source identity/admission records; sensitivity rank may be pinned there and referenced here. |
| Archaeology rights records | `data/registry/rights/archaeology/` if/when accepted | Rights review state; not sensitivity policy. |
| Archaeology source/lifecycle payloads | `data/raw/archaeology/`, `data/work/archaeology/`, `data/quarantine/archaeology/`, `data/processed/archaeology/` | Actual data belongs in lifecycle lanes, not sensitivity registry records. |
| Human-facing Archaeology sensitivity doctrine | `docs/domains/archaeology/SENSITIVITY.md` | Explains sensitivity catalogue and redaction posture; not registry storage. |
| Archaeology Map/UI trust contracts | `docs/domains/archaeology/MAP_UI_CONTRACTS.md` | Explains governed surface obligations; not registry storage. |
| Cross-domain sensitivity architecture | `docs/architecture/sensitivity.md`, `docs/doctrine/sensitivity.md` | Architecture and doctrine for deny-by-default posture. |
| Archaeology semantic meaning | `contracts/domains/archaeology/` | Object-family meaning and invariants. |
| Machine schemas | `schemas/contracts/v1/domains/archaeology/`, `schemas/contracts/v1/receipts/`, or ADR-selected schema lane | Schema enforcement; sensitivity-registry schema remains NEEDS VERIFICATION. |
| Sensitivity, geoprivacy, consent, and rights policy | `policy/sensitivity/archaeology/`, `policy/domains/archaeology/`, `policy/geoprivacy/`, `policy/consent/archaeology/`, `policy/rights/` | Decisions and rules; registry records only point to policy outcomes. |
| Validation/redaction/policy/review receipts | `data/receipts/archaeology/` and accepted receipt lanes | Process memory for checks and public-safe transforms. |
| Proof/evidence | `data/proofs/archaeology/` or accepted proof lanes | EvidenceBundle closure, proof packs, signatures, and citation validation. |
| Catalog projections | `data/catalog/domain/archaeology/`, STAC/DCAT/PROV lanes, and triplet lanes | Catalog/discovery carriers after catalog closure. |
| Published artifacts | `data/published/layers/archaeology/` if/when accepted | Released public-safe artifacts and direct sidecars only. |
| Release decisions | `release/` | Promotion, correction, rollback, supersession, withdrawal, and release manifests. |
| Public surfaces | governed APIs and released artifacts only | Public clients do not read this registry lane directly. |

---

## Archaeology sensitivity boundary

| Rule | Handling |
|---|---|
| Registry record is control state | It records or points to sensitivity-review posture; it does not decide policy or grant access. |
| Archaeology defaults to denied for sensitive cases | Exact site geometry, human remains, sacred sites, collection-security details, and looting-risk exposure fail closed. |
| Audience tier and record rank are distinct | T0–T4 audience tier and per-record sensitivity rank are separate rubrics; do not collapse them into one field. |
| Exact geometry is not public geometry | Exact/internal site geometry, survey locations, remote-sensing detections, 3D detail, and collection-security locations must remain withheld unless a governed public-safe derivative is explicitly released. |
| RedactionReceipt is required for public-safe transforms | Generalization, masking, jitter, aggregation, differential privacy, k-anonymity, or withholding must be receipted with named/versioned profile refs. |
| Sovereignty and CARE labels inherit | Tribal/sovereignty-sensitive, cultural-knowledge, oral-history, sacred-site, burial, or rights-holder context carries review and access restrictions downstream. |
| Consent/revocation/embargo controls travel | Consent tokens, revocation state, embargo state, and cache invalidation state must be honored across registry, catalog, UI, AI, and release surfaces. |
| Remote sensing and 3D are sensitivity-bearing | LiDAR, SAR, photogrammetry, 3D reconstructions, and derived detections may increase exposure risk and require policy review. |
| Source role is preserved | Observed, administrative, regulatory, modeled, aggregate, candidate, context, synthetic, or restricted source roles must not be upgraded by processing, map rendering, AI explanation, or release review. |
| Registry is not validation | Validation receipts, redaction receipts, review receipts, and run receipts remain separate process-memory objects. |
| Registry is not proof | EvidenceBundle/proof support remains separate. |
| Registry is not catalog | STAC/DCAT/PROV/domain catalog records and graph/triplet projections live under catalog/triplet lanes. |
| Registry is not release | Public exposure requires validation, policy, review, proof/catalog support, release manifest, correction path, and rollback path. |
| Public clients do not read this lane | Public UI/API surfaces consume governed APIs, released artifacts, catalog/triplet/proof-backed responses, and policy-safe envelopes. |

---

## Accepted material

Accepted content is limited to Archaeology sensitivity registry records and registry-local support files:

- sensitivity-family README files and registry-local indexes;
- sensitivity review records for sources, records, object families, derivatives, layers, catalog items, release candidates, and published artifacts;
- audience tier refs, per-record sensitivity rank refs, sensitivity profile refs, redaction profile refs, geoprivacy refs, and public-safe representation refs;
- sovereignty/CARE refs, consent refs, revocation refs, embargo refs, cache-invalidation refs, rights-holder review refs, and steward review refs;
- SourceDescriptor refs, rights refs, dataset refs, layer refs, catalog refs, release refs, and correction/rollback refs;
- validation receipt refs, RedactionReceipt refs, AggregationReceipt refs, RepresentationReceipt refs, policy receipt refs, review receipt refs, EvidenceBundle/proof refs;
- blocker records for missing sensitivity support, unresolved sovereignty review, unresolved consent, unresolved rights, missing receipt, missing release state, or risky cross-surface inference.

Keep records compact and pointer-based. Do not embed site coordinates, sacred-site details, human-remains details, restricted oral-history content, collection-security detail, proof packs, policy decisions, catalog records, release manifests, or archaeological claim content in this lane.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw Archaeology payloads, site forms, survey records, oral-history transcripts, cultural-knowledge records, remote-sensing scenes, 3D models, LiDAR/SAR products, exact site geometry, collection-security detail, shapefiles, GeoParquet, COG, PMTiles, or source-native tables | `data/raw/archaeology/`, `data/work/archaeology/`, `data/quarantine/archaeology/`, or `data/processed/archaeology/` depending on lifecycle state |
| Exact site coordinates, human-remains detail, sacred-site detail, looting-risk exposure, culturally sensitive knowledge, restricted review material, access secrets, or steward-only notes | denied, restricted, quarantined, or routed to governed restricted storage |
| Source descriptor/admission records | `data/registry/sources/archaeology/` after topology reconciliation |
| Rights registry records | `data/registry/rights/archaeology/` after accepted topology |
| Dataset, crosswalk, domain, or layer registry records | `data/registry/datasets/`, `data/registry/crosswalks/`, `data/registry/domains/`, `data/registry/layers/` |
| Semantic object contracts | `contracts/domains/archaeology/` |
| JSON Schema | `schemas/contracts/v1/...` |
| Sensitivity policy, geoprivacy policy, consent policy, rights policy, access-control logic, redaction policy, or release rules | `policy/` |
| Validation receipts, redaction receipts, policy receipts, consent/revocation receipts, review receipts, or process-memory logs | `data/receipts/` |
| EvidenceBundle records, proof packs, signatures, or citation-validation closure | `data/proofs/` |
| STAC/DCAT/PROV/domain catalog records or graph/triplet projections | `data/catalog/` and `data/triplets/` |
| Published layers, reports, dashboards, tiles, API payloads, UI payloads, or generated-answer carriers | `data/published/`, governed app/API roots, and release-approved public artifact lanes |
| ReleaseManifest, PromotionDecision, CorrectionNotice, RollbackCard, withdrawal notice, or supersession notice | `release/` |
| Validator code, connector code, pipelines, fixtures, tests, or CI workflows | `tools/`, `connectors/`, `pipelines/`, `fixtures/`, `tests/`, `.github/workflows/` |

---

## Suggested directory shape

The map below is **PROPOSED** documentation guidance, not proof that child folders or records exist.

```text
data/registry/sensitivity/archaeology/
├── README.md
├── site_location/
│   ├── README.md
│   └── index.local.json
├── human_remains/
│   ├── README.md
│   └── index.local.json
├── sacred_sites/
│   ├── README.md
│   └── index.local.json
├── cultural_knowledge/
│   ├── README.md
│   └── index.local.json
├── remote_sensing_3d/
│   ├── README.md
│   └── index.local.json
├── redaction_profiles/
│   ├── README.md
│   └── index.local.json
├── sovereignty_review/
│   ├── README.md
│   └── index.local.json
├── embargo_revocation/
│   ├── README.md
│   └── index.local.json
└── index.local.json
```

Do not create a new child lane until the sensitivity object family, source descriptor refs, sensitivity/rank refs, policy refs, review state, receipt refs, release refs, and rollback path are known.

---

## Suggested registry shape

The exact sensitivity-registry schema remains **NEEDS VERIFICATION**. An Archaeology sensitivity registry record should be structured enough for audit, public-safe transformation, release readiness, correction, revocation, and rollback.

```json
{
  "id": "kfm-sensitivity:archaeology:<stable-sensitivity-id>",
  "record_type": "sensitivity_registry_record",
  "domain": "archaeology",
  "sensitivity_family": "site_location | human_remains | sacred_sites | cultural_knowledge | remote_sensing_3d | redaction_profiles | sovereignty_review | embargo_revocation | other",
  "subject_ref": "source | record | object_family | derivative | layer | catalog_item | release_candidate | published_artifact",
  "audience_tier": "T0 | T1 | T2 | T3 | T4 | needs-review",
  "sensitivity_rank": "0 | 1 | 2 | 3 | 4 | 5 | needs-review",
  "source_registry_refs": [],
  "rights_registry_refs": [],
  "policy_refs": [],
  "redaction_profile_refs": [],
  "geoprivacy_refs": [],
  "sovereignty_refs": [],
  "care_refs": [],
  "consent_refs": [],
  "revocation_refs": [],
  "embargo_refs": [],
  "validation_receipt_refs": [],
  "redaction_receipt_refs": [],
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

- [ ] Confirm the sensitivity record belongs in `data/registry/sensitivity/archaeology/`, not source payloads, policy, contracts, schemas, receipts, proofs, catalog, published artifacts, or release lanes.
- [ ] Confirm the subject of the sensitivity review is identified: source, record, object family, derivative, layer, catalog item, release candidate, published artifact, or other reviewed object.
- [ ] Confirm audience tier and per-record sensitivity rank are both present where material and are not collapsed into one field.
- [ ] Confirm exact site geometry, human remains, sacred sites, looting-risk exposure, oral-history/cultural-knowledge restrictions, and collection-security details fail closed.
- [ ] Confirm sensitivity evidence exists before asserting any public-safe tier, transform, audience, or display eligibility.
- [ ] Confirm named/versioned redaction profile refs and RedactionReceipt refs exist before any public-safe transformation is asserted.
- [ ] Confirm sovereignty, CARE, consent, revocation, embargo, rights-holder, and steward-review requirements are current before any use beyond restricted processing.
- [ ] Confirm remote sensing, 3D, AI text, map popups, exports, vector indexes, and tile surfaces do not leak restricted detail through cross-surface inference.
- [ ] Confirm sensitivity state does not override rights, source-role, evidence closure, catalog closure, policy decision, review state, or release state.
- [ ] Confirm validation receipts, redaction receipts, policy outcomes, and review records exist before catalog or release eligibility is asserted.
- [ ] Confirm EvidenceRef/EvidenceBundle and proof refs exist for consequential use.
- [ ] Confirm release refs point to ReleaseManifest/PromotionDecision objects rather than implying publication from sensitivity state.
- [ ] Confirm correction, revocation, embargo, supersession, withdrawal, stale-state, and rollback paths exist for changed sensitivity, rights-holder decision, consent, or release posture.
- [ ] Confirm no public client, map layer, graph edge, vector index, generated answer, report, or dashboard reads this registry lane as direct public truth or permission.

---

## Status notes

| Claim | Status |
|---|---:|
| This README replaces the empty placeholder at `data/registry/sensitivity/archaeology/README.md`. | CONFIRMED authored |
| The target path existed in the live repository as an empty placeholder before this edit. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/sensitivity/README.md` exists and is currently a greenfield stub. | CONFIRMED by GitHub contents API during this edit |
| Archaeology sensitivity docs state archaeology defaults to T4 denied / rank 5 fail-closed for exact site geometry, human remains, sacred sites, collection security, and looting-risk exposure. | CONFIRMED by GitHub contents API during this edit |
| Archaeology sensitivity docs distinguish audience tier T0–T4 from per-record sensitivity rank 0–5. | CONFIRMED by GitHub contents API during this edit |
| General sensitivity architecture says deny-by-default means missing rights, sovereignty, sensitivity, or release-state evidence fails closed. | CONFIRMED by GitHub contents API during this edit |
| Archaeology Map/UI contracts say public clients use governed APIs and released payloads only, and no browser path reads canonical or candidate stores. | CONFIRMED by GitHub contents API during this edit |
| Concrete Archaeology sensitivity registry payloads exist under this requested lane. | UNKNOWN |
| The final accepted parent contract for `data/registry/sensitivity/` is resolved. | NEEDS VERIFICATION |
| A canonical Archaeology sensitivity registry schema is enforced. | NEEDS VERIFICATION |
| CI validates Archaeology sensitivity registry records. | UNKNOWN |
| This README grants public access to Archaeology sensitivity registry internals. | DENY |

---

## Maintainer note

Archaeology sensitivity registry records are useful because they make sensitivity posture, redaction profile refs, sovereignty/CARE state, consent/revocation/embargo state, release readiness, correction, and rollback inspectable before any archaeology object approaches a public surface. They become dangerous when treated as policy, source payloads, site-location storage, proof closure, catalog closure, release decisions, or permission.

Keep the safe chain explicit:

```text
sensitivity registry record -> source/object refs -> policy/review outcome -> lifecycle payload -> validation/redaction receipt -> proof/catalog -> release -> governed public surface
```

Never collapse it into:

```text
sensitivity registry record -> public Archaeology permission
```
