<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/datasets/readme
name: Dataset Registry README
path: data/registry/datasets/README.md
type: data-registry-datasets-parent-readme
version: v0.2.0
status: draft
owners:
  - <registry-steward>
  - <dataset-steward>
  - <source-steward>
  - <catalog-steward>
  - <policy-steward>
  - <proof-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: internal-governance
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: registry
registry_scope: dataset-registry-records
path_posture: existing-parent-stub-replaced; flora-child-lane-confirmed; exact-dataset-registry-layout-needs-verification
sensitivity_posture: registry-internal; no-public-path; source-role-preserving; evidence-aware; policy-aware; release-blocked-until-gates-close
related:
  - ../README.md
  - ../sources/
  - ../crosswalks/README.md
  - flora/README.md
  - ../../raw/
  - ../../work/
  - ../../quarantine/
  - ../../processed/
  - ../../catalog/
  - ../../receipts/
  - ../../proofs/
  - ../../published/
  - ../../../contracts/
  - ../../../schemas/contracts/v1/
  - ../../../policy/
  - ../../../tests/
  - ../../../fixtures/
  - ../../../release/
  - ../../../docs/architecture/directory-rules.md
tags:
  - kfm
  - data
  - registry
  - datasets
  - dataset-identity
  - source-role
  - provenance
  - evidence
  - rights
  - sensitivity
  - catalog-readiness
  - release-gated
  - no-public-path
notes:
  - "This README replaces the greenfield stub at `data/registry/datasets/README.md`."
  - "Dataset registry records identify and govern dataset state. They do not store source payloads, define contracts, enforce schemas, hold policy, emit receipts, prove claims, close catalogs, or publish artifacts."
  - "Confirmed child lane during this edit: `flora/README.md`."
  - "Exact dataset registry object names, schemas, validators, emitted examples, CI enforcement, and final lane taxonomy remain NEEDS VERIFICATION until checked against implementation evidence."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Dataset Registry

Parent lane for governed dataset identity and dataset-state records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: registry" src="https://img.shields.io/badge/family-registry-blueviolet">
  <img alt="Lane: datasets" src="https://img.shields.io/badge/lane-datasets-blue">
  <img alt="Boundary: not source data" src="https://img.shields.io/badge/boundary-not%20source%20data-critical">
  <img alt="Exposure: no public path" src="https://img.shields.io/badge/exposure-no%20public%20path-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Confirmed child lanes](#confirmed-child-lanes) · [Dataset boundary](#dataset-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Suggested directory shape](#suggested-directory-shape) · [Suggested record shape](#suggested-record-shape) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/registry/datasets/` is for dataset registry records only. It is not RAW source storage, WORK staging, QUARANTINE, PROCESSED data, catalog output, proof storage, receipt storage, policy, schema authority, release authority, public API/UI material, or generated-answer authority.

---

## Scope

`data/registry/datasets/` is the parent lane for governed dataset identity and dataset-state records across KFM domains and shared dataset families.

A dataset registry record may answer bounded governance questions such as:

- What stable dataset, dataset family, source collection, derivative collection, or release-candidate dataset is being referenced?
- Which source descriptors, source roles, rights terms, access terms, cadence, authority limits, and stewardship obligations apply?
- Which lifecycle payloads are associated with the dataset across RAW, WORK, QUARANTINE, PROCESSED, CATALOG/TRIPLET, and PUBLISHED states?
- Which validation receipts, proof records, catalog records, policy decisions, review records, release manifests, corrections, supersessions, withdrawals, or rollback targets are relevant?
- Is the dataset public-safe, restricted, quarantined, candidate-only, stale, deprecated, superseded, withdrawn, or denied?

Dataset registry records are **governance handles**. They help KFM reason about admission, refresh, validation, catalog closure, release readiness, correction, and rollback. They do not contain dataset payloads and do not publish anything by themselves.

---

## Path posture

The requested parent lane is:

```text
data/registry/datasets/
```

Directory Rules place lifecycle data and emitted governance objects under `data/`, and explicitly name `registry` as a data-side phase that sits alongside raw, work, quarantine, processed, catalog, triplets, published, receipts, proofs, and rollback. Dataset registry records therefore belong under `data/registry/`, not under a new root.

Domain-specific dataset lanes should remain segments inside this parent lane, for example:

```text
data/registry/datasets/<domain>/
```

This README does not claim that this subtype-first layout is final for every dataset family. Exact registry layout remains **NEEDS VERIFICATION** until accepted registry contracts, schemas, validators, fixtures, and ADR or README governance confirm it.

---

## Repo fit

| Responsibility | Home | Boundary |
|---|---|---|
| Dataset registry records | `data/registry/datasets/` | Dataset identity, lifecycle pointers, rights/sensitivity posture, cadence, status, eligibility, and correction state. |
| Source registry records | `data/registry/sources/` or accepted source registry lane | Source identity, authority, role, rights, terms, and cadence. |
| Crosswalk registry records | `data/registry/crosswalks/` | Mapping state between source values, authority IDs, vocabulary terms, fields, and KFM identities. |
| Source payloads | `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/`, `data/published/` | Actual data lives in lifecycle lanes, not registry records. |
| Semantic contracts | `contracts/` | Object-family meaning and invariants. |
| Machine-checkable schemas | `schemas/contracts/v1/` | Enforceable shape. |
| Policy and admissibility | `policy/` | Rights, sensitivity, geoprivacy, access, source-role, and release rules. |
| Validation receipts | `data/receipts/validation/` | Process memory for validation runs. |
| Evidence and proof | `data/proofs/` | EvidenceBundle closure, proof packs, citation validation, signatures, and integrity support. |
| Catalog/discovery projections | `data/catalog/` | STAC/DCAT/PROV/domain catalog records and discovery state. |
| Release decisions | `release/` | Promotion, release manifests, correction notices, supersession, withdrawal, and rollback cards. |
| Public clients | governed APIs and released artifacts | Public clients do not read dataset registry internals directly. |

---

## Confirmed child lanes

The child lane below was confirmed by current GitHub reads while replacing this parent stub. This confirms path/README evidence only; it does **not** prove emitted dataset registry payloads, schemas, validators, fixtures, CI enforcement, signing, release integration, correction hooks, rollback hooks, or public-safe summaries.

| Child lane | Status | Purpose | Boundary |
|---|---:|---|---|
| [`flora/`](flora/README.md) | CONFIRMED README | Flora dataset identity and dataset-state records for taxon backbones, specimens, occurrences, rare plants, vegetation communities, invasive plants, phenology, range polygons, restoration datasets, and public-safe derivatives. | Not source payload storage, Flora truth, catalog closure, proof, receipt storage, policy, release authority, or public output. |

---

## Dataset boundary

| Rule | Handling |
|---|---|
| Registry record is a handle | It identifies and governs a dataset; it does not contain the dataset payload. |
| Registry state is not source truth | The registry can point to source payloads, but does not make a source claim true. |
| Source role is preserved | Dataset role must not be upgraded by normalization, cataloging, release review, or public presentation. |
| Rights and sensitivity fail closed | Unclear rights, source terms, steward obligations, sensitivity, cultural risk, living-person risk, rare-species risk, archaeology risk, infrastructure risk, or precise-location risk blocks public promotion. |
| Registry is not validation | Validation receipts and run receipts remain separate process-memory objects. |
| Registry is not proof | EvidenceBundle/proof support remains separate. |
| Registry is not catalog | STAC/DCAT/PROV/domain catalog records live under `data/catalog/`. |
| Registry is not release | Public exposure requires validation, policy, review, proof/catalog support, release manifest, correction path, and rollback path. |
| Registry changes are auditable | Dataset identity, source version, lifecycle refs, correction state, supersession, withdrawal, stale state, and rollback dependencies should remain traceable. |
| Public clients do not read this lane | Public UI/API surfaces consume governed APIs, released artifacts, catalog/triplet/proof-backed responses, and policy-safe envelopes. |

---

## Accepted material

Accepted content is limited to dataset registry records and registry-local support files:

- dataset identity records;
- dataset family README files;
- domain-specific dataset indexes;
- registry-local manifests, checksums, signatures, and index sidecars;
- source descriptor refs, source-role refs, rights posture, sensitivity posture, cadence, steward, version, retrieval, and lifecycle pointer metadata;
- blocker states such as `RIGHTS_UNRESOLVED`, `SENSITIVITY_UNRESOLVED`, `SOURCE_ROLE_CONFLICT`, `VALIDATION_FAILED`, `EVIDENCE_MISSING`, `RELEASE_BLOCKED`, `STALE`, `SUPERSEDED`, or `WITHDRAWN`;
- pointers to validation receipts, proof packs, catalog records, release candidates, release manifests, correction notices, supersession notices, withdrawal notices, and rollback cards;
- public-safe summary fields only when sensitive details have been removed and policy permits review-surface exposure.

Registry records should point outward by stable ID, path, URI, digest, or EvidenceRef rather than copying source payloads, proof material, catalog records, policy decisions, or release manifests into the registry lane.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw source payloads, source-native extracts, restricted tables, private identifiers, exact sensitive coordinates, rasters, shapefiles, GeoParquet, COG, PMTiles, or source archives | `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/`, or governed restricted storage depending on lifecycle state |
| Source descriptors, source terms, source registry records, or source activation decisions | `data/registry/sources/` or accepted source registry/source-catalog lanes |
| Crosswalk mapping records | `data/registry/crosswalks/` |
| Semantic contracts | `contracts/` |
| JSON Schema or machine contract shape | `schemas/contracts/v1/` |
| Policy rules, rights rules, sensitivity rules, geoprivacy rules, access-control rules, or release rules | `policy/` |
| Validator code, connector code, pipelines, transformations, package code, or app code | `tools/`, `connectors/`, `pipelines/`, `packages/`, `apps/` |
| Fixtures, tests, or CI workflows | `fixtures/`, `tests/`, `.github/workflows/` |
| Validation receipts, run receipts, redaction receipts, review receipts, or process-memory logs | `data/receipts/` |
| EvidenceBundle records, proof packs, signatures, or citation-validation closure | `data/proofs/` |
| STAC/DCAT/PROV/domain catalog records | `data/catalog/` |
| Published artifacts, map layers, tiles, dashboards, reports, public API payloads, or generated-answer carriers | `data/published/`, governed app/API roots, and release-approved public artifact lanes |
| ReleaseManifest, PromotionDecision, CorrectionNotice, RollbackCard, withdrawal notice, or supersession notice | `release/` |

---

## Suggested directory shape

The map below is **PROPOSED** documentation guidance, not proof that child folders or records exist beyond confirmed README evidence.

```text
data/registry/datasets/
├── README.md
├── flora/
│   └── README.md
├── <domain>/
│   ├── README.md
│   ├── <dataset_family>/
│   │   ├── README.md
│   │   └── index.local.json
│   └── index.local.json
└── index.local.json
```

`index.local.json` files are registry-local lookup aids. They are not proof indexes, catalog records, release manifests, search indexes, vector indexes, graph projections, map sources, public API payloads, or generated-answer sources.

---

## Suggested record shape

The exact schema remains **NEEDS VERIFICATION**. A dataset registry record should be structured enough for audit, refresh, validation, catalog closure, correction, rollback, and release review.

```json
{
  "id": "kfm-dataset:<domain-or-family>:<stable-id>",
  "record_type": "dataset_registry_record",
  "domain": "flora | fauna | hydrology | soil | habitat | geology | atmosphere | archaeology | hazards | agriculture | people-dna-land | other",
  "dataset_family": "source-specific or domain-specific dataset family",
  "title": "Human-readable dataset title",
  "status": "candidate | active | restricted | quarantined | deprecated | superseded | withdrawn | denied",
  "source_descriptor_refs": [],
  "source_role": "observed | regulatory | modeled | aggregate | administrative | candidate | synthetic | context | restricted",
  "rights_posture": "open | attribution-required | restricted | stewarded | unknown | denied",
  "sensitivity_posture": "public-safe | generalized | restricted | denied | needs-review",
  "cadence": "one-time | periodic | event-driven | unknown",
  "retrieval_refs": [],
  "lifecycle_refs": {
    "raw": [],
    "work": [],
    "quarantine": [],
    "processed": [],
    "catalog": [],
    "published": []
  },
  "evidence_refs": [],
  "proof_refs": [],
  "validation_receipt_refs": [],
  "policy_refs": [],
  "review_refs": [],
  "catalog_refs": [],
  "release_refs": [],
  "correction_refs": [],
  "rollback_refs": [],
  "public_exposure": "none | eligible-after-review | released-public-safe | denied",
  "blockers": [],
  "created_at": "timestamp",
  "updated_at": "timestamp"
}
```

Do not treat this JSON block as a live schema. It is a maintainer-facing sketch until paired contracts, schemas, validators, fixtures, examples, CI, and review workflows are verified.

---

## Required checks before use

- [ ] Confirm the object is a dataset registry record, not a source payload, source descriptor, crosswalk, proof, receipt, catalog record, release decision, policy, schema, validator, fixture, or test.
- [ ] Confirm the owning root is `data/` and the registry lane is appropriate under Directory Rules.
- [ ] Confirm source descriptor refs, source role, rights posture, cadence, stewardship obligations, and authority limits are preserved.
- [ ] Confirm source role is not upgraded by normalization, cataloging, release review, API shaping, map rendering, or generated explanation.
- [ ] Confirm sensitive details are not exposed in registry files, local indexes, or public summaries.
- [ ] Confirm rights, sensitivity, geoprivacy, cultural, living-person, rare-species, archaeology, infrastructure, precise-location, and source-term risks fail closed when unresolved.
- [ ] Confirm validation receipts exist before catalog or release eligibility is asserted.
- [ ] Confirm EvidenceRef/EvidenceBundle and proof refs exist for consequential use.
- [ ] Confirm catalog refs point to STAC/DCAT/PROV/domain catalog records rather than embedding them.
- [ ] Confirm release refs point to ReleaseManifest/PromotionDecision objects rather than implying publication from registry state.
- [ ] Confirm correction, supersession, withdrawal, stale-state, and rollback paths exist for mutable or externally governed datasets.
- [ ] Confirm no public client, map layer, graph edge, vector index, generated answer, report, or dashboard reads this registry lane as direct public truth.

---

## Status notes

| Claim | Status |
|---|---:|
| This README replaces the greenfield stub at `data/registry/datasets/README.md`. | CONFIRMED authored |
| The target path existed in the live repository as a greenfield stub before this edit. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/datasets/flora/README.md` exists as a child dataset registry README. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/crosswalks/README.md` exists as a sibling registry README and keeps registry state separate from contracts, schemas, policy, proofs, catalog, release decisions, and public claims. | CONFIRMED by GitHub contents API during this edit |
| Emitted dataset registry payloads exist under this parent lane. | UNKNOWN |
| A canonical dataset registry schema is fully enforced. | NEEDS VERIFICATION |
| CI validates dataset registry records. | UNKNOWN |
| This README grants public access to dataset registry internals. | DENY |

---

## Maintainer note

Dataset registry records are useful because they make dataset identity, cadence, source role, rights, sensitivity, lifecycle linkage, correction, and rollback inspectable. They become dangerous when treated as payloads, proofs, catalog closure, or release decisions. Keep the chain explicit:

```text
source descriptor + dataset registry record -> lifecycle payload -> validation receipt -> proof/catalog/policy/review -> release -> governed public surface
```

Never collapse it into:

```text
dataset registry record -> public truth
```
