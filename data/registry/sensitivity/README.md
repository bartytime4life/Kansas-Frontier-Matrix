<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/sensitivity/readme
name: Sensitivity Registry README
path: data/registry/sensitivity/README.md
type: data-registry-sensitivity-parent-readme
version: v0.2.0
status: draft
owners:
  - <registry-steward>
  - <sensitivity-steward>
  - <policy-steward>
  - <domain-stewards>
  - <redaction-steward>
  - <geoprivacy-steward>
  - <rights-steward>
  - <proof-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: registry
registry_scope: sensitivity-registry-records
path_posture: existing-parent-stub-replaced; subtype-first-sensitivity-registry-parent-confirmed; archaeology-fauna-flora-geology-child-readmes-confirmed; canonical-record-shape-needs-verification; concrete-records-unknown
sensitivity_posture: registry-internal; no-public-path; deny-by-default; fail-closed; rights-sovereignty-sensitivity-release-evidence-required; redaction-receipt-aware; geoprivacy-aware; source-role-preserving; evidence-aware; rights-aware; policy-aware; release-blocked-until-gates-close
related:
  - ../README.md
  - ../sources/README.md
  - ../datasets/README.md
  - ../domains/README.md
  - ../crosswalks/README.md
  - ../rights/README.md
  - ../layers/README.md
  - archaeology/README.md
  - fauna/README.md
  - flora/README.md
  - geology/README.md
  - ../../raw/
  - ../../work/
  - ../../quarantine/
  - ../../processed/
  - ../../catalog/
  - ../../published/
  - ../../receipts/
  - ../../proofs/
  - ../../../docs/architecture/sensitivity.md
  - ../../../docs/doctrine/sensitivity.md
  - ../../../docs/domains/archaeology/SENSITIVITY.md
  - ../../../docs/domains/fauna/SENSITIVITY.md
  - ../../../docs/domains/flora/SENSITIVITY.md
  - ../../../docs/domains/flora/RIGHTS_AND_SENSITIVITY.md
  - ../../../docs/domains/geology/SENSITIVITY.md
  - ../../../contracts/
  - ../../../schemas/contracts/v1/
  - ../../../schemas/contracts/v1/receipts/
  - ../../../policy/sensitivity/
  - ../../../policy/geoprivacy/
  - ../../../policy/domains/
  - ../../../policy/rights/
  - ../../../release/
tags:
  - kfm
  - data
  - registry
  - sensitivity
  - deny-by-default
  - fail-closed
  - geoprivacy
  - redaction
  - RedactionReceipt
  - AggregationReceipt
  - RepresentationReceipt
  - ModelRunReceipt
  - RealityBoundaryNote
  - sovereignty
  - CARE
  - rare-species
  - archaeology
  - fauna
  - flora
  - geology
  - source-role
  - evidence
  - provenance
  - release-gated
  - rollback
  - no-public-path
notes:
  - "This README replaces the greenfield stub at `data/registry/sensitivity/README.md`."
  - "Confirmed child README lanes during this sequence: archaeology, fauna, flora, geology. This confirms README/path evidence only, not emitted registry payloads or runtime enforcement."
  - "Sensitivity registry records are registry/control records. They do not store source payloads, reveal restricted details, define policy, enforce schemas, hold receipts/proofs, close catalogs, or publish artifacts."
  - "Sensitivity state can block public exposure, but it cannot by itself authorize release. Rights, evidence, review, catalog/proof support, release, correction, and rollback gates still have to close."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Sensitivity Registry

Parent registry lane for sensitivity-review state, geoprivacy/redaction posture, sensitive-object blockers, and release-readiness pointers.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: registry" src="https://img.shields.io/badge/family-registry-blueviolet">
  <img alt="Lane: sensitivity" src="https://img.shields.io/badge/lane-sensitivity-blue">
  <img alt="Posture: deny by default" src="https://img.shields.io/badge/posture-deny--by--default-critical">
  <img alt="Boundary: not policy" src="https://img.shields.io/badge/boundary-not%20policy-critical">
  <img alt="Exposure: no public path" src="https://img.shields.io/badge/exposure-no%20public%20path-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Confirmed child lanes](#confirmed-child-lanes) · [Sensitivity registry boundary](#sensitivity-registry-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Suggested directory shape](#suggested-directory-shape) · [Suggested registry shape](#suggested-registry-shape) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/registry/sensitivity/` is a registry/control lane for sensitivity-review state and sensitivity-readiness pointers. It is not RAW source storage, WORK staging, QUARANTINE, PROCESSED data, catalog output, proof storage, receipt storage, semantic contract authority, schema authority, policy, release authority, public API/UI material, exact sensitive-location storage, private/restricted knowledge storage, or generated-answer authority.

---

## Scope

`data/registry/sensitivity/` is the subtype-first parent for sensitivity registry records:

```text
data/registry/sensitivity/<domain-or-scope>/
```

A sensitivity registry record makes sensitivity posture inspectable before source activation, downstream processing, catalog closure, export, public display, AI response, map popup, tile exposure, or release. It may point to source descriptors, object-family records, dataset registry records, derivative records, layer registry records, redaction/geoprivacy profile refs, policy outcomes, validation receipts, proof packs, catalog records, release candidates, release manifests, correction notices, and rollback cards.

This parent README exists to prevent sensitivity state from collapsing into adjacent authorities. It should help maintainers distinguish:

- sensitivity registry records from source descriptors, dataset records, layer records, and domain registry records;
- sensitivity registry records from contracts, schemas, policy, receipts, proofs, catalog records, release records, and published artifacts;
- reviewed sensitivity posture from permission to publish;
- release-readiness pointers from actual release decisions.

A sensitivity registry record does **not** make a source usable, a derivative publishable, a claim true, a layer public, a catalog closed, or a sensitive detail safe to disclose. It records a governed review state and points to the evidence/policy/release chain needed to act on that state.

---

## Path posture

The confirmed parent lane is:

```text
data/registry/sensitivity/
```

This path uses a subtype-first pattern, matching the broader registry style used by other registry families:

```text
data/registry/sources/<domain>/
data/registry/datasets/<domain>/
data/registry/domains/<domain>/
data/registry/crosswalks/<domain-or-scope>/
data/registry/layers/<domain>/
data/registry/rights/<domain-or-scope>/
data/registry/sensitivity/<domain-or-scope>/
```

The parent existed as a greenfield stub before this edit. Archaeology, Fauna, Flora, and Geology child READMEs now exist. That confirms path/README evidence only. The canonical sensitivity-registry object schema, emitted records, validators, fixtures, CI checks, runtime sensitivity resolver, governed API behavior, UI behavior, and release integration remain **NEEDS VERIFICATION** or **UNKNOWN** unless separately verified.

---

## Repo fit

| Responsibility | Home | Boundary |
|---|---|---|
| Sensitivity registry parent | `data/registry/sensitivity/` | Sensitivity-state routing, sensitivity-review pointers, blockers, and registry-local indexes. |
| Domain sensitivity registry lanes | `data/registry/sensitivity/<domain-or-scope>/` | Domain-specific sensitivity review records and release-readiness pointers. |
| Source descriptors | `data/registry/sources/<domain>/` and reconciled source registry lanes | Source identity/admission; sensitivity posture may be pinned there and referenced here. |
| Dataset registry records | `data/registry/datasets/<domain>/` | Dataset identity and dataset-state; not sensitivity policy or release authority. |
| Domain registry records | `data/registry/domains/<domain>/` | Domain-state records; not sensitivity review records. |
| Crosswalk registry records | `data/registry/crosswalks/` | Mapping state across source IDs, authority IDs, vocabularies, units, fields, classes, and domain lanes. |
| Rights registry records | `data/registry/rights/<domain-or-scope>/` | Rights review state; rights and sensitivity remain independent fail-closed gates. |
| Layer registry records | `data/registry/layers/<domain>/` | Layer identity and release-readiness pointers; sensitivity refs may be attached but not duplicated. |
| Source/lifecycle payloads | `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/` | Actual source and processed data; not sensitivity registry control records. |
| Catalog projections | `data/catalog/`, `data/triplets/` | Discovery, catalog closure, and graph/triplet projections. |
| Published artifacts | `data/published/` | Released public-safe artifacts and direct release sidecars. |
| Semantic contracts | `contracts/` | Object meaning and invariants; not registry storage. |
| Machine schemas | `schemas/contracts/v1/...` | Machine-checkable shape; sensitivity-registry schema remains NEEDS VERIFICATION. |
| Policy and geoprivacy | `policy/sensitivity/`, `policy/geoprivacy/`, `policy/domains/`, `policy/rights/` | Sensitivity, geoprivacy, access, redaction, rights, public-safety, sovereignty, and release-policy decisions. |
| Receipts | `data/receipts/` | Validation, transform, redaction, aggregation, model, policy, review, and run process memory. |
| Proofs | `data/proofs/` | EvidenceBundle/proof support and citation closure. |
| Release authority | `release/` | Promotion decisions, ReleaseManifests, correction notices, rollback cards, withdrawal, and supersession. |
| Public surfaces | governed APIs and released artifacts only | Public clients do not read this registry lane directly. |

---

## Confirmed child lanes

This confirms README/path evidence only. It does not prove live sensitivity registry payloads, schema enforcement, validators, fixtures, CI, release integration, API behavior, UI behavior, or public-safe summaries.

| Child lane | Status | Sensitivity registry posture |
|---|---:|---|
| [`archaeology/`](archaeology/README.md) | CONFIRMED README | Archaeology defaults to T4/deny for exact site geometry, human remains, sacred sites, collection-security detail, oral-history/cultural-knowledge restricted context, and looting-risk exposure unless governed review/redaction/receipt/release gates close. |
| [`fauna/`](fauna/README.md) | CONFIRMED README | Sensitive occurrence geometry, nests, dens, roosts, hibernacula, spawning sites, steward-controlled records, and re-identifying joins fail closed until governed redaction/review/release gates close. |
| [`flora/`](flora/README.md) | CONFIRMED README | Rare/protected/culturally sensitive plant locations, exact sensitive geometry, culturally sensitive plant knowledge, taxonomy collisions, rights-unclear feeds, and join-induced sensitivity fail closed; Flora sensitivity docs are overlapping/conflicted until ADR/drift reconciliation. |
| [`geology/`](geology/README.md) | CONFIRMED README | Exact subsurface points, boreholes, well logs, cores, private wells, geochemistry samples, extraction-targetable resource detail, rights-restricted source content, private-parcel/operator joins, and interpretive surfaces are review/redaction/RealityBoundaryNote-sensitive. |

Future child lanes should follow the same boundary pattern and should not be added as proof of implementation maturity.

---

## Sensitivity registry boundary

| Rule | Handling |
|---|---|
| Registry record is control state | It records or points to sensitivity-review posture; it does not decide policy or grant access. |
| Deny-by-default governs | Missing rights, sovereignty, sensitivity, or release-state evidence fails closed as `DENY` or `ABSTAIN`, not `ALLOW`. |
| Rights and sensitivity are separate gates | Passing rights does not relax sensitivity. Passing sensitivity does not clear rights. Both must close before public release. |
| Source quality never overrides sensitivity | A well-sourced, validated, rights-clean object can still be unsafe or unpublishable at exact precision. |
| Exact/internal detail stays internal | Exact sensitive coordinates, restricted cultural knowledge, rare species locations, private-property joins, infrastructure-sensitive details, subsurface/resource targets, and other restricted details do not become public from registry state. |
| Public-safe transforms require receipts | Generalization, aggregation, masking, redaction, withholding, model-derived representation, and reality-boundary transforms must point to required receipts when asserted. |
| Sovereignty and CARE controls travel | Tribal, sovereignty, cultural, steward-controlled, consent, embargo, revocation, and rights-holder review constraints inherit downstream. |
| Re-identifying joins fail closed | Joins that reconstruct sensitive locations, people, property, cultural knowledge, ecological locations, subsurface targets, or operationally sensitive context inherit the most restrictive applicable posture. |
| Source role is preserved | Observed, administrative, regulatory, modeled, aggregate, candidate, context, synthetic, or restricted source roles must not be upgraded by processing, cataloging, rendering, AI explanation, or release review. |
| Registry is not validation | Validation receipts, redaction receipts, review receipts, policy receipts, model receipts, and run receipts remain separate process-memory objects. |
| Registry is not proof | EvidenceBundle/proof support remains separate. |
| Registry is not catalog | STAC/DCAT/PROV/domain catalog records and graph/triplet projections live under catalog/triplet lanes. |
| Registry is not release | Public exposure requires validation, policy, review, proof/catalog support, release manifest, correction path, and rollback path. |
| Public clients do not read this lane | Public UI/API surfaces consume governed APIs, released artifacts, catalog/triplet/proof-backed responses, and policy-safe envelopes. |
| Unknown implementation stays unknown | A README path is not proof of emitted records, schemas, validators, tests, runtime behavior, or public availability. |

---

## Accepted material

Accepted content is limited to sensitivity registry records and registry-local support files:

- parent README and domain/scope child README files;
- domain/scope child lane indexes and local manifests;
- sensitivity review records for sources, object families, records, datasets, derivatives, layers, catalog items, release candidates, and published artifacts;
- audience tier refs, per-record sensitivity rank refs, sensitivity profile refs, redaction profile refs, geoprivacy refs, public-safe representation refs, aggregation refs, model refs, RealityBoundaryNote refs, and review refs;
- sovereignty/CARE refs, consent refs, revocation refs, embargo refs, steward-review refs, rights-holder refs, source-terms refs, and cultural/protected-context refs;
- source descriptor refs, dataset refs, crosswalk refs, rights refs, layer refs, catalog refs, release refs, correction refs, rollback refs, supersession refs, stale-state refs, and withdrawal refs;
- validation receipt refs, RedactionReceipt refs, AggregationReceipt refs, RepresentationReceipt refs, ModelRunReceipt refs, policy receipt refs, review receipt refs, EvidenceRef/EvidenceBundle/proof refs;
- blocker records for missing sensitivity support, unresolved rights/steward review, unresolved sovereignty/CARE review, missing receipt, missing release state, changed sensitivity posture, or risky cross-surface inference;
- registry-local index files that point outward without becoming catalog, proof, policy, release, or artifact authority.

Keep records compact and pointer-based. Do not embed full source payloads, exact sensitive details, proof packs, policy decisions, catalog records, release manifests, or domain claims in this lane.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw source payloads, processed domain objects, rasters, shapefiles, GeoParquet, COG, PMTiles, source-native tables, remote-sensing scenes, scans, models, or sensitive records | `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/`, or `data/published/` depending on lifecycle/release state |
| Exact sensitive coordinates, cultural knowledge, private-property joins, living-person detail, rare-species details, archaeological site locations, subsurface/resource targets, infrastructure-sensitive details, restricted source material, secrets, credentials, or access tokens | denied, restricted, quarantined, or routed to governed restricted storage |
| Source descriptor/admission records | `data/registry/sources/<domain>/` and reconciled source registry lanes |
| Dataset identity records | `data/registry/datasets/<domain>/` |
| Domain-state records | `data/registry/domains/<domain>` |
| Crosswalk mapping records | `data/registry/crosswalks/` |
| Rights registry records | `data/registry/rights/<domain-or-scope>/` |
| Layer identity/release-readiness records | `data/registry/layers/<domain>/` |
| Semantic object contracts | `contracts/` |
| JSON Schema | `schemas/contracts/v1/...` |
| Sensitivity policy, geoprivacy policy, rights policy, access-control logic, redaction policy, or release rules | `policy/` |
| Validation, transform, model, aggregation, redaction, policy, review, or run receipts | `data/receipts/` |
| EvidenceBundle records, proof packs, signatures, or citation-validation closure | `data/proofs/` |
| STAC/DCAT/PROV/domain catalog records or graph/triplet projections | `data/catalog/` and `data/triplets/` |
| ReleaseManifest, PromotionDecision, CorrectionNotice, RollbackCard, withdrawal notice, or supersession notice | `release/` |
| Public UI code, MapLibre runtime code, APIs, pipelines, validators, fixtures, tests, or CI workflows | `apps/`, `packages/`, `tools/`, `pipelines/`, `fixtures/`, `tests/`, `.github/workflows/` |
| Generated-answer carriers or AI summaries | governed response/output lanes after evidence, policy, review, and release checks |

---

## Suggested directory shape

The map below is **PROPOSED** documentation guidance. Confirmed README child lanes are marked; other domains are examples until created and verified.

```text
data/registry/sensitivity/
├── README.md
├── archaeology/          # CONFIRMED README
│   └── README.md
├── fauna/                # CONFIRMED README
│   └── README.md
├── flora/                # CONFIRMED README
│   └── README.md
├── geology/              # CONFIRMED README
│   └── README.md
├── agriculture/          # PROPOSED
│   └── README.md
├── atmosphere/           # PROPOSED
│   └── README.md
├── habitat/              # PROPOSED
│   └── README.md
├── hazards/              # PROPOSED; likely restricted/alert-authority boundary
│   └── README.md
├── hydrology/            # PROPOSED
│   └── README.md
├── people-dna-land/      # PROPOSED; likely restricted-review / no public path
│   └── README.md
├── roads-rail-trade/     # PROPOSED; infrastructure/access context
│   └── README.md
├── soil/                 # PROPOSED
│   └── README.md
└── index.local.json      # PROPOSED local index, not catalog/release/policy authority
```

Do not create or populate child registry payloads until subject refs, source descriptor refs, sensitivity evidence refs, policy refs, review state, receipt refs, release refs, and rollback path are known.

---

## Suggested registry shape

The exact sensitivity-registry schema remains **NEEDS VERIFICATION**. A sensitivity registry record should be structured enough for audit, public-safe transformation, release readiness, correction, withdrawal, and rollback.

```json
{
  "id": "kfm-sensitivity:<domain-or-scope>:<stable-sensitivity-id>",
  "record_type": "sensitivity_registry_record",
  "domain": "<domain-or-scope>",
  "sensitivity_family": "site_location | sensitive_occurrence | rare_species | cultural_knowledge | exact_subsurface | reidentifying_join | restricted_source_terms | redaction_profiles | review_queue | other",
  "subject_ref": "source | record | object_family | derivative | model_output | layer | catalog_item | release_candidate | published_artifact",
  "audience_tier": "T0 | T1 | T2 | T3 | T4 | needs-review",
  "sensitivity_rank": "0 | 1 | 2 | 3 | 4 | 5 | needs-review | not-applicable",
  "source_registry_refs": [],
  "dataset_registry_refs": [],
  "rights_registry_refs": [],
  "layer_registry_refs": [],
  "policy_refs": [],
  "redaction_profile_refs": [],
  "geoprivacy_refs": [],
  "steward_review_refs": [],
  "sovereignty_refs": [],
  "care_refs": [],
  "consent_refs": [],
  "revocation_refs": [],
  "embargo_refs": [],
  "validation_receipt_refs": [],
  "redaction_receipt_refs": [],
  "aggregation_receipt_refs": [],
  "representation_receipt_refs": [],
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

Do not treat this JSON block as a live schema. It is a maintainer-facing sketch until paired contracts, schemas, validators, fixtures, examples, CI, release workflows, governed API behavior, and UI behavior are verified.

---

## Required checks before use

- [ ] Confirm the record belongs in `data/registry/sensitivity/<domain-or-scope>/`, not `data/registry/sources/`, `data/registry/datasets/`, `data/registry/domains/`, `data/registry/crosswalks/`, `data/registry/rights/`, `data/registry/layers/`, `contracts/`, `schemas/`, `policy/`, `data/receipts/`, `data/proofs/`, `data/catalog/`, `data/published/`, or `release/`.
- [ ] Confirm the subject of the sensitivity review is identified: source, record, object family, derivative, model output, layer, catalog item, release candidate, published artifact, or other reviewed object.
- [ ] Confirm source descriptor, dataset registry, rights registry, layer registry, catalog, policy, receipt, proof, and release refs are pointer-based and not duplicated.
- [ ] Confirm audience tier and per-record sensitivity rank are both present where material and are not silently collapsed.
- [ ] Confirm sensitivity evidence exists before asserting any public-safe tier, transform, audience, display eligibility, or generated-answer eligibility.
- [ ] Confirm unknown, missing, restricted, conflicting, unresolved, or stale sensitivity state fails closed.
- [ ] Confirm sensitivity state does not override rights, source-role, evidence closure, catalog closure, policy decision, review state, release state, sovereignty/CARE state, consent/revocation state, or rollback state.
- [ ] Confirm rights, sovereignty, consent, revocation, embargo, public-safety, living-person, rare-species, archaeology, infrastructure, and private-property restrictions inherit downstream.
- [ ] Confirm public-safe transforms have named/versioned profile refs and required receipts before catalog or release eligibility is asserted.
- [ ] Confirm map popups, exports, AI text, vector indexes, tile surfaces, graph joins, and cross-domain joins do not leak restricted detail through inference.
- [ ] Confirm EvidenceRef/EvidenceBundle and proof refs exist for consequential sensitivity use.
- [ ] Confirm release refs point to ReleaseManifest/PromotionDecision objects rather than implying publication from sensitivity state.
- [ ] Confirm correction, supersession, withdrawal, stale-state, revocation, embargo, and rollback paths exist for changed sensitivity, source terms, rights-holder decision, steward review, or release posture.
- [ ] Confirm no public client, map layer, graph edge, vector index, generated answer, report, or dashboard reads this registry lane as direct public truth or permission.

---

## Status notes

| Claim | Status |
|---|---:|
| This README replaces the greenfield stub at `data/registry/sensitivity/README.md`. | CONFIRMED authored |
| The target path existed in the live repository as a greenfield stub before this edit. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/sensitivity/archaeology/README.md` exists as a confirmed child lane. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/sensitivity/fauna/README.md` exists as a confirmed child lane. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/sensitivity/flora/README.md` exists as a confirmed child lane. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/sensitivity/geology/README.md` exists as a confirmed child lane. | CONFIRMED by GitHub contents API during this edit |
| General sensitivity architecture says unresolved rights, sovereignty, sensitivity, or release-state evidence fails closed, and public clients do not reach RAW, WORK, QUARANTINE, canonical/internal stores, graph internals, vector indexes, source APIs, or direct model runtimes. | CONFIRMED by GitHub contents API during this edit |
| Concrete sensitivity registry payloads exist under this parent lane. | UNKNOWN |
| A canonical sensitivity-registry schema is enforced. | NEEDS VERIFICATION |
| CI validates sensitivity registry records. | UNKNOWN |
| Runtime sensitivity resolution or governed API behavior reads this registry lane. | UNKNOWN |
| This README grants public access to sensitivity registry internals. | DENY |

---

## Maintainer note

Sensitivity registry records are useful because they make sensitive posture, redaction/geoprivacy refs, steward-review state, release readiness, correction, withdrawal, and rollback inspectable before any object approaches a public surface. They become dangerous when treated as policy, source payloads, exact-location storage, proof closure, catalog closure, release decisions, or permission.

Keep the safe chain explicit:

```text
sensitivity registry record -> source/object refs -> policy/review outcome -> lifecycle payload -> validation/redaction/aggregation/model receipt -> proof/catalog -> release -> governed public surface
```

Never collapse it into:

```text
sensitivity registry record -> public permission
```
