<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/layers/readme
name: Layer Registry README
path: data/registry/layers/README.md
type: data-registry-layers-parent-readme
version: v0.2.0
status: draft
owners:
  - <registry-steward>
  - <layer-steward>
  - <map-layer-steward>
  - <domain-stewards>
  - <policy-steward>
  - <proof-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: registry
registry_scope: layer-registry-records
path_posture: existing-parent-stub-replaced; subtype-first-layer-registry-parent-confirmed; child-domain-readmes-confirmed-for-agriculture-atmosphere-flora-habitat; canonical-record-shape-needs-verification; concrete-records-unknown
sensitivity_posture: registry-internal; no-public-path; domain-sensitive-rules-fail-closed; source-role-preserving; layer-is-not-truth; evidence-aware; rights-aware; policy-aware; release-blocked-until-gates-close
related:
  - ../README.md
  - ../domains/README.md
  - ../datasets/README.md
  - ../sources/README.md
  - ../crosswalks/README.md
  - agriculture/README.md
  - atmosphere/README.md
  - flora/README.md
  - habitat/README.md
  - ../../raw/
  - ../../work/
  - ../../quarantine/
  - ../../processed/
  - ../../catalog/
  - ../../published/layers/
  - ../../receipts/
  - ../../proofs/
  - ../../../contracts/data/layer_descriptor.md
  - ../../../contracts/data/layer_manifest.md
  - ../../../contracts/data/layer_catalog_item.md
  - ../../../contracts/domains/
  - ../../../schemas/contracts/v1/
  - ../../../policy/
  - ../../../release/
tags:
  - kfm
  - data
  - registry
  - layers
  - map-layer
  - layer-registry
  - layer-descriptor
  - layer-manifest
  - layer-catalog-item
  - domain-layer-descriptor
  - source-role
  - rights
  - sensitivity
  - evidence
  - provenance
  - release-gated
  - rollback
  - no-public-path
notes:
  - "This README replaces the greenfield stub at `data/registry/layers/README.md`."
  - "Layer registry records are registry/control records. They do not store layer payloads, render tiles, prove domain claims, define contracts, enforce schemas, hold policy, close catalogs, or publish artifacts."
  - "Confirmed child README lanes during this sequence: agriculture, atmosphere, flora, and habitat. Concrete registry payloads, canonical schemas, validators, fixtures, CI, runtime layer resolution, and public API behavior remain UNKNOWN or NEEDS VERIFICATION."
  - "Published layer bytes and public-safe artifacts belong under governed published/release lanes after validation, evidence, policy, review, release, correction, and rollback gates close."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Layer Registry

Parent registry lane for KFM layer identity, layer-family routing, release-readiness pointers, and domain-safe map-layer control records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: registry" src="https://img.shields.io/badge/family-registry-blueviolet">
  <img alt="Lane: layers" src="https://img.shields.io/badge/lane-layers-blue">
  <img alt="Topology: subtype-first" src="https://img.shields.io/badge/topology-subtype--first-informational">
  <img alt="Boundary: not layer bytes" src="https://img.shields.io/badge/boundary-not%20layer%20bytes-critical">
  <img alt="Exposure: no public path" src="https://img.shields.io/badge/exposure-no%20public%20path-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Confirmed child lanes](#confirmed-child-lanes) · [Layer registry boundary](#layer-registry-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Suggested directory shape](#suggested-directory-shape) · [Suggested registry shape](#suggested-registry-shape) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/registry/layers/` is a registry/control lane for layer identity, layer-family routing, domain meaning pointers, evidence/policy/release references, and rollback-ready layer state. It is not RAW source storage, WORK staging, QUARANTINE, PROCESSED data, catalog output, published layer bytes, tile storage, proof storage, receipt storage, semantic contract authority, schema authority, policy, release authority, public API/UI material, or generated-answer authority.

---

## Scope

`data/registry/layers/` is the subtype-first parent for layer registry records:

```text
data/registry/layers/<domain>/
```

A layer registry record identifies and constrains a layer-like product before it can safely become a governed public surface. It may point to domain-layer descriptors, generic layer contracts, source registry records, dataset registry records, validation receipts, EvidenceBundles, catalog records, policy decisions, release candidates, release manifests, correction notices, and rollback targets.

This parent README exists to prevent layer registry state from collapsing into adjacent authorities. It should help maintainers distinguish:

- layer registry records from source descriptors;
- layer registry records from dataset/domain/crosswalk registry records;
- layer registry records from contracts, schemas, policy, receipts, proofs, catalog records, release records, and published layer artifacts;
- public-safe release-ready layer state from raw/internal/source/candidate state.

A layer registry record does **not** make a layer true, public, rendered, validated, catalog-closed, policy-approved, or released.

---

## Path posture

The confirmed parent lane is:

```text
data/registry/layers/
```

This path uses a subtype-first pattern, matching the broader registry style used by other registry families:

```text
data/registry/sources/<domain>/
data/registry/datasets/<domain>/
data/registry/domains/<domain>/
data/registry/crosswalks/<domain-or-scope>/
data/registry/layers/<domain>/
```

The parent existed as a greenfield stub before this edit. Several child README files now exist, but the canonical layer-registry object schema, emitted records, validators, fixtures, CI checks, runtime resolver, governed API behavior, and release integration remain **NEEDS VERIFICATION** or **UNKNOWN** unless separately verified.

---

## Repo fit

| Responsibility | Home | Boundary |
|---|---|---|
| Layer registry parent | `data/registry/layers/` | Layer identity/routing/control records and registry-local indexes. |
| Domain layer registry lanes | `data/registry/layers/<domain>/` | Domain-specific layer families and release-readiness pointers. |
| Source descriptors | `data/registry/sources/<domain>/` and reconciled source registry lanes | Source identity/admission; not layer identity. |
| Dataset registry records | `data/registry/datasets/<domain>/` | Dataset identity and dataset-state; not layer identity. |
| Domain registry records | `data/registry/domains/<domain>/` | Domain-state records; not layer identity. |
| Crosswalk registry records | `data/registry/crosswalks/` | Mapping state across source IDs, authority IDs, vocabularies, units, fields, classes, and domain lanes. |
| Source/lifecycle payloads | `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/` | Actual source and processed data; not registry control records. |
| Catalog projections | `data/catalog/`, `data/triplets/` | Discovery, catalog closure, and graph/triplet projections. |
| Published layer artifacts | `data/published/layers/<domain>/` if/when accepted | Released public-safe layer bytes and direct release sidecars. |
| Generic layer contracts | `contracts/data/layer_descriptor.md`, `contracts/data/layer_manifest.md`, `contracts/data/layer_catalog_item.md` | Semantic contracts; not registry storage. |
| Domain layer meaning | `contracts/domains/<domain>/domain_layer_descriptor.md` where present and verified | Domain-specific layer meaning; not registry storage. |
| Machine schemas | `schemas/contracts/v1/...` | Machine-checkable shape; schema placement conflicts remain possible until verified. |
| Policy and sensitivity | `policy/` | Access, sensitivity, rights, redaction, public-safety, and release-policy decisions. |
| Receipts | `data/receipts/` | Validation, transform, redaction, aggregation, model, policy, and review process memory. |
| Proofs | `data/proofs/` | EvidenceBundle/proof support and citation closure. |
| Release authority | `release/` | Promotion decisions, ReleaseManifests, correction notices, rollback cards, withdrawal, and supersession. |
| Public surfaces | governed APIs and released artifacts only | Public clients do not read this registry lane directly. |

---

## Confirmed child lanes

This confirms README/path evidence only. It does not prove live layer registry payloads, schema enforcement, validators, fixtures, CI, release integration, tile generation, API behavior, UI behavior, or public-safe summaries.

| Child lane | Status | Layer registry posture |
|---|---:|---|
| [`agriculture/`](agriculture/README.md) | CONFIRMED README | Aggregate-or-permissioned posture; field-level and private-sensitive joins fail closed. |
| [`atmosphere/`](atmosphere/README.md) | CONFIRMED README | Source-role and knowledge-character preservation; not emergency guidance; AQI/AOD/model caveats preserved. |
| [`flora/`](flora/README.md) | CONFIRMED README | Rare/protected/culturally sensitive plant exposure fails closed; redaction/generalization/release support required. |
| [`habitat/`](habitat/README.md) | CONFIRMED README | Occurrence context and sensitive joins fail closed; Habitat does not own Flora/Fauna occurrence truth. |

Future child lanes should follow the same boundary pattern and should not be added as proof of implementation maturity.

---

## Layer registry boundary

| Rule | Handling |
|---|---|
| Registry record is control state | It identifies, routes, and constrains layer families; it does not contain layer bytes. |
| Layer is not truth | Layers, tiles, styles, vectors, rasters, scenes, UI panels, exports, reports, and generated explanations are downstream carriers, not sovereign truth. |
| Registry is not a descriptor contract | `LayerDescriptor`, `LayerManifest`, `LayerCatalogItem`, and domain-layer descriptors remain separate object families under `contracts/`. |
| Registry is not source admission | Source identity, rights, cadence, and activation are handled by source registry records. Layer records only reference them. |
| Registry is not catalog closure | STAC/DCAT/PROV/domain catalog records and graph/triplet projections remain separate. |
| Registry is not evidence closure | EvidenceBundle/proof support remains separate. |
| Registry is not policy | Access, sensitivity, geoprivacy, rights, redaction, public-safety, aggregation, and release rules live under `policy/`. |
| Registry is not release | Public exposure requires validation, policy, review, proof/catalog support, ReleaseManifest/PromotionDecision, correction path, and rollback target. |
| Style is not policy | Styling, layer order, paint/layout rules, and render hints cannot substitute for evidence, policy, redaction, access control, release, or rollback. |
| Public clients do not read this lane | Public UI/API surfaces consume governed APIs, released artifacts, catalog/triplet/proof-backed responses, and policy-safe envelopes. |
| Domain restrictions travel | The domain child lane must preserve source role, sensitivity, rights, temporal, evidence, correction, and rollback constraints from upstream domains. |
| Unknown implementation stays unknown | A README path is not proof of emitted records, schemas, validators, tests, runtime behavior, or public availability. |

---

## Accepted material

Accepted content is limited to layer registry records and registry-local support files:

- parent README and domain child README files;
- domain child lane indexes and local manifests;
- stable layer IDs and layer-family registry records;
- references to `LayerDescriptor`, `LayerManifest`, `LayerCatalogItem`, and domain-layer descriptors;
- source registry, dataset registry, domain registry, and crosswalk registry references;
- policy, sensitivity, geoprivacy, rights, redaction, aggregation, access, caveat, freshness, and public-exposure posture references;
- validation, transform, model, aggregation, redaction, review, and policy receipt references;
- EvidenceRef/EvidenceBundle/proof references;
- catalog, triplet, and graph projection references;
- release candidate, release manifest, promotion decision, correction notice, withdrawal, supersession, and rollback references;
- registry-local index files that point outward without becoming catalog, proof, policy, release, or artifact authority.

Keep records compact and pointer-based. Do not embed layer bytes, source-native dumps, proof packs, policy decisions, catalog records, release manifests, or domain claims in this lane.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw source payloads, processed domain objects, rasters, shapefiles, GeoParquet, COG, PMTiles, vector tile bundles, tile JSON, source-native tables, remote-sensing scenes, or model outputs | `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/`, or `data/published/layers/` depending on lifecycle/release state |
| Published layer bytes or public-safe artifact sidecars | `data/published/layers/<domain>/` after governed release |
| Source descriptor/admission records | `data/registry/sources/<domain>/` and reconciled source registry lanes |
| Dataset identity records | `data/registry/datasets/<domain>/` |
| Domain-state records | `data/registry/domains/<domain>/` |
| Crosswalk mapping records | `data/registry/crosswalks/` |
| Semantic object contracts | `contracts/data/` and `contracts/domains/` |
| JSON Schema | `schemas/contracts/v1/...` |
| Policy rules, sensitivity rules, geoprivacy rules, rights rules, access-control logic, redaction policy, or release rules | `policy/` |
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
data/registry/layers/
├── README.md
├── agriculture/          # CONFIRMED README
│   └── README.md
├── atmosphere/           # CONFIRMED README
│   └── README.md
├── flora/                # CONFIRMED README
│   └── README.md
├── habitat/              # CONFIRMED README
│   └── README.md
├── fauna/                # PROPOSED
│   └── README.md
├── geology/              # PROPOSED
│   └── README.md
├── hazards/              # PROPOSED
│   └── README.md
├── hydrology/            # PROPOSED
│   └── README.md
├── soil/                 # PROPOSED
│   └── README.md
└── index.local.json      # PROPOSED local index, not catalog/release authority
```

Do not create or populate child registry payloads until layer identity, domain object-family ownership, source-role posture, sensitivity posture, policy refs, evidence refs, release refs, and rollback path are known.

---

## Suggested registry shape

The exact layer-registry schema remains **NEEDS VERIFICATION**. A layer registry record should be structured enough for audit, release readiness, correction, and rollback.

```json
{
  "id": "kfm-layer:<domain>:<stable-layer-id>",
  "record_type": "layer_registry_record",
  "domain": "<domain>",
  "layer_family": "<domain-specific-layer-family>",
  "domain_layer_descriptor_refs": [],
  "generic_layer_descriptor_refs": [],
  "layer_manifest_refs": [],
  "layer_catalog_item_refs": [],
  "domain_object_family_refs": [],
  "source_registry_refs": [],
  "dataset_registry_refs": [],
  "domain_registry_refs": [],
  "crosswalk_refs": [],
  "policy_refs": [],
  "sensitivity_refs": [],
  "rights_refs": [],
  "geoprivacy_refs": [],
  "redaction_receipt_refs": [],
  "aggregation_receipt_refs": [],
  "validation_receipt_refs": [],
  "transform_receipt_refs": [],
  "model_receipt_refs": [],
  "evidence_refs": [],
  "proof_refs": [],
  "catalog_refs": [],
  "triplet_refs": [],
  "review_refs": [],
  "release_refs": [],
  "correction_refs": [],
  "rollback_refs": [],
  "public_exposure": "none | eligible-after-review | released-public-safe | generalized-public-safe | permissioned | restricted | denied",
  "blockers": [],
  "created_at": "timestamp",
  "updated_at": "timestamp"
}
```

Do not treat this JSON block as a live schema. It is a maintainer-facing sketch until paired contracts, schemas, validators, fixtures, examples, CI, release workflows, governed API behavior, and UI behavior are verified.

---

## Required checks before use

- [ ] Confirm the record belongs in `data/registry/layers/<domain>/`, not `data/published/layers/<domain>/`, `data/registry/sources/<domain>/`, `data/registry/datasets/<domain>/`, `contracts/`, `schemas/`, `policy/`, `data/receipts/`, `data/proofs/`, `data/catalog/`, or `release/`.
- [ ] Confirm the domain, layer family, object family, source-role posture, sensitivity posture, rights posture, temporal posture, and public exposure posture are identified.
- [ ] Confirm `LayerDescriptor`, `LayerManifest`, `LayerCatalogItem`, and any domain-layer descriptor relationships are pointer-based and not duplicated.
- [ ] Confirm domain-specific fail-closed rules are preserved, including rare-species, culturally sensitive, living-person, private-property, infrastructure, public-safety, or rights-sensitive joins where applicable.
- [ ] Confirm source roles, source families, source snapshots, crosswalk posture, model/run context, aggregation scope, caveats, and cross-lane ownership are preserved.
- [ ] Confirm public-safe transforms such as redaction, generalization, aggregation, withholding, suppression, or denial are visible and receipted where required.
- [ ] Confirm validation receipts, redaction receipts, aggregation receipts, transform receipts, model receipts, review records, and policy outcomes exist before catalog or release eligibility is asserted.
- [ ] Confirm EvidenceRef/EvidenceBundle and proof refs exist for consequential layer use.
- [ ] Confirm catalog refs point to STAC/DCAT/PROV/domain catalog records rather than embedding them.
- [ ] Confirm release refs point to ReleaseManifest/PromotionDecision objects rather than implying publication from registry state.
- [ ] Confirm correction, supersession, withdrawal, stale-state, and rollback paths exist for mutable or sensitive layer material.
- [ ] Confirm no public client, map layer, graph edge, vector index, generated answer, report, or dashboard reads this registry lane as direct public truth.

---

## Status notes

| Claim | Status |
|---|---:|
| This README replaces the greenfield stub at `data/registry/layers/README.md`. | CONFIRMED authored |
| The target path existed in the live repository as a greenfield stub before this edit. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/layers/agriculture/README.md` exists as a confirmed child lane. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/layers/atmosphere/README.md` exists as a confirmed child lane. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/layers/flora/README.md` exists as a confirmed child lane. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/layers/habitat/README.md` exists as a confirmed child lane. | CONFIRMED by GitHub contents API during this edit |
| `contracts/data/layer_descriptor.md` exists and defines LayerDescriptor as a governed renderer-facing descriptor, not a layer payload, proof, policy decision, or release decision. | CONFIRMED by GitHub contents API during this edit |
| Concrete layer registry payloads exist under this parent lane. | UNKNOWN |
| A canonical layer-registry schema is enforced. | NEEDS VERIFICATION |
| CI validates layer registry records. | UNKNOWN |
| Runtime layer resolution or governed API behavior reads this registry lane. | UNKNOWN |
| This README grants public access to layer registry internals. | DENY |

---

## Maintainer note

Layer registry records are useful because they make layer identity, domain meaning, source-role constraints, sensitivity posture, public-safe transformation posture, release readiness, correction, and rollback inspectable before a layer can become a governed public surface. They become dangerous when treated as layer bytes, proofs, catalog closure, release decisions, or truth.

Keep the safe chain explicit:

```text
layer registry record -> layer descriptor refs -> lifecycle payload -> validation/transform/redaction/model receipt -> proof/catalog/policy/review -> release -> governed public surface
```

Never collapse it into:

```text
layer registry record -> public map truth
```
