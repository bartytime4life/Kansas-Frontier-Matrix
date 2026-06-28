<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/domains/readme
name: Domain Registry README
path: data/registry/domains/README.md
type: data-registry-domains-parent-readme
version: v0.2.0
status: draft
owners:
  - <registry-steward>
  - <domain-steward>
  - <source-steward>
  - <data-steward>
  - <contract-steward>
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
registry_scope: domain-registry-records
path_posture: existing-parent-stub-replaced; soil-child-lane-confirmed; exact-domain-registry-layout-needs-verification
sensitivity_posture: registry-internal; no-public-path; source-role-preserving; evidence-aware; rights-aware; policy-aware; release-blocked-until-gates-close
related:
  - ../README.md
  - ../sources/
  - ../datasets/README.md
  - ../crosswalks/README.md
  - soil/README.md
  - ../../raw/
  - ../../work/
  - ../../quarantine/
  - ../../processed/
  - ../../catalog/
  - ../../triplets/
  - ../../receipts/
  - ../../proofs/
  - ../../published/
  - ../../../contracts/domains/
  - ../../../schemas/contracts/v1/domains/
  - ../../../policy/domains/
  - ../../../tests/domains/
  - ../../../fixtures/domains/
  - ../../../release/
  - ../../../docs/architecture/directory-rules.md
tags:
  - kfm
  - data
  - registry
  - domains
  - domain-registry
  - domain-state
  - source-role
  - provenance
  - evidence
  - rights
  - sensitivity
  - catalog-readiness
  - release-gated
  - no-public-path
notes:
  - "This README replaces the greenfield stub at `data/registry/domains/README.md`."
  - "Domain registry records describe domain-lane state, object-family coverage, source-family posture, lifecycle links, blockers, and readiness. They do not store source payloads, define contracts, enforce schemas, hold policy, emit receipts, prove claims, close catalogs, or publish artifacts."
  - "Confirmed child lane during this edit: `soil/README.md`."
  - "Exact domain registry object names, schemas, validators, emitted examples, CI enforcement, final lane taxonomy, and governed API behavior remain NEEDS VERIFICATION until checked against implementation evidence."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Domain Registry

Parent lane for governed domain-state registry records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: registry" src="https://img.shields.io/badge/family-registry-blueviolet">
  <img alt="Lane: domains" src="https://img.shields.io/badge/lane-domains-blue">
  <img alt="Boundary: not source data" src="https://img.shields.io/badge/boundary-not%20source%20data-critical">
  <img alt="Exposure: no public path" src="https://img.shields.io/badge/exposure-no%20public%20path-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Confirmed child lanes](#confirmed-child-lanes) · [Domain registry boundary](#domain-registry-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Suggested directory shape](#suggested-directory-shape) · [Suggested record shape](#suggested-record-shape) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/registry/domains/` is for domain-state registry records only. It is not RAW source storage, WORK staging, QUARANTINE, PROCESSED data, catalog output, proof storage, receipt storage, source registry authority, dataset registry authority, semantic contract authority, schema authority, policy, release authority, public API/UI material, or generated-answer authority.

---

## Scope

`data/registry/domains/` is the parent lane for governed domain-state records across KFM. A domain registry record summarizes a domain lane's current governed state: object-family coverage, source-family posture, lifecycle references, sensitivity and rights posture, evidence/proof expectations, catalog readiness, release blockers, correction state, rollback dependencies, and unresolved verification work.

A domain registry record may answer bounded governance questions such as:

- Which object families does a domain currently recognize or claim as in scope?
- Which source families, source roles, dataset registry records, source registry records, and crosswalk registry records support the domain lane?
- Which lifecycle paths have admitted, working, quarantined, processed, cataloged, or published material for the domain?
- Which contracts, schemas, policies, fixtures, tests, validators, receipts, proofs, catalog records, release manifests, corrections, and rollback cards are expected or linked?
- Which blockers prevent public release, catalog closure, generated answers, map display, or governed API exposure?
- Which domain-state records are active, draft, blocked, stale, superseded, withdrawn, denied, or pending review?

Domain registry records are **governance handles**. They help KFM reason about domain readiness and domain-state transitions. They do not contain domain payloads and do not publish anything by themselves.

---

## Path posture

The requested parent lane is:

```text
data/registry/domains/
```

Directory Rules place lifecycle data and emitted governance objects under `data/`, and name `registry` as a data-side phase that sits alongside raw, work, quarantine, processed, catalog, triplets, published, receipts, proofs, and rollback. Domain registry records therefore belong under `data/registry/`, not under a new root.

Domain-specific registry lanes should remain segments inside this parent lane, for example:

```text
data/registry/domains/<domain>/
```

This README does not claim that this domain-first layout is final for every registry subtype. Exact domain registry layout remains **NEEDS VERIFICATION** until accepted registry contracts, schemas, validators, fixtures, and ADR or README governance confirm it.

---

## Repo fit

| Responsibility | Home | Boundary |
|---|---|---|
| Domain registry records | `data/registry/domains/` | Domain-state records, object-family coverage, source-family posture, lifecycle refs, blockers, readiness, correction, and rollback state. |
| Source registry records | `data/registry/sources/` or accepted source registry lane | Source identity, authority, role, rights, terms, cadence, and access posture. |
| Dataset registry records | `data/registry/datasets/` | Dataset identity and dataset-state records. |
| Crosswalk registry records | `data/registry/crosswalks/` | Mapping state between source values, authority IDs, vocabulary terms, fields, and KFM identities. |
| Source payloads | `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/`, `data/published/` | Actual data lives in lifecycle lanes, not registry records. |
| Semantic contracts | `contracts/domains/` and shared `contracts/` lanes | Object-family meaning and invariants. |
| Machine-checkable schemas | `schemas/contracts/v1/` | Enforceable shape. |
| Policy and admissibility | `policy/` | Rights, sensitivity, geoprivacy, access, source-role, and release rules. |
| Validation receipts | `data/receipts/validation/` | Process memory for validation runs. |
| Evidence and proof | `data/proofs/` | EvidenceBundle closure, proof packs, citation validation, signatures, and integrity support. |
| Catalog/discovery projections | `data/catalog/` and `data/triplets/` | STAC/DCAT/PROV/domain catalog records, graph projections, and discovery state. |
| Release decisions | `release/` | Promotion, release manifests, correction notices, supersession, withdrawal, and rollback cards. |
| Public clients | governed APIs and released artifacts | Public clients do not read domain registry internals directly. |

---

## Confirmed child lanes

The child lane below was confirmed by current GitHub reads while replacing this parent stub. This confirms path/README evidence only; it does **not** prove emitted domain registry payloads, schemas, validators, fixtures, CI enforcement, signing, release integration, correction hooks, rollback hooks, governed API behavior, or public-safe summaries.

| Child lane | Status | Purpose | Boundary |
|---|---:|---|---|
| [`soil/`](soil/README.md) | CONFIRMED README | Soil domain-state records for object-family coverage, source-family posture, support-type boundaries, lifecycle refs, readiness, blockers, correction, and rollback. | Not source payload storage, Soil truth, source registry authority, semantic contract authority, catalog closure, proof, receipt storage, policy, release authority, or public output. |

---

## Domain registry boundary

| Rule | Handling |
|---|---|
| Registry record is domain-state metadata | It describes a domain lane's governed state; it does not contain domain payloads. |
| Registry state is not source truth | A registry record can point to source payloads, but does not make a source claim true. |
| Source role is preserved | Domain readiness must not upgrade observed, regulatory, modeled, aggregate, administrative, candidate, synthetic, context, or restricted source roles. |
| Domain ownership stays visible | A domain registry record must not steal ownership from adjacent domains, contracts, policies, sources, proofs, catalogs, or releases. |
| Rights and sensitivity fail closed | Unclear rights, source terms, steward obligations, cultural risk, living-person risk, rare-species risk, archaeology risk, infrastructure risk, precise-location risk, or operational risk blocks public promotion. |
| Registry is not validation | Validation receipts and run receipts remain separate process-memory objects. |
| Registry is not proof | EvidenceBundle/proof support remains separate. |
| Registry is not catalog | STAC/DCAT/PROV/domain catalog records and graph projections live under catalog/triplet lanes. |
| Registry is not release | Public exposure requires validation, policy, review, proof/catalog support, release manifest, correction path, and rollback path. |
| Public clients do not read this lane | Public UI/API surfaces consume governed APIs, released artifacts, catalog/triplet/proof-backed responses, and policy-safe envelopes. |

---

## Accepted material

Accepted content is limited to domain registry records and registry-local support files:

- domain-state records;
- domain readiness records;
- object-family coverage indexes;
- source-family posture indexes;
- support-type, source-role, rights, sensitivity, evidence, catalog-readiness, release-readiness, correction, and rollback state records;
- registry-local manifests, checksums, signatures, and index sidecars;
- pointers to source descriptors, dataset registry records, crosswalk registry records, contracts, schemas, policy refs, lifecycle payloads, validation receipts, proof refs, catalog refs, release candidates, correction notices, supersession notices, withdrawal notices, and rollback cards;
- public-safe summaries only when sensitive details have been removed and policy permits review-surface exposure.

Registry records should point outward by stable ID, path, URI, digest, or EvidenceRef rather than copying source payloads, contracts, schemas, proofs, catalog records, policy decisions, receipts, release manifests, or public artifacts into the registry lane.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw source payloads, source-native extracts, restricted tables, private identifiers, exact sensitive coordinates, rasters, shapefiles, GeoParquet, COG, PMTiles, source archives, or source-native database dumps | `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/`, or governed restricted storage depending on lifecycle state |
| Source descriptors, source terms, source registry records, or source activation decisions | `data/registry/sources/` or accepted source registry/source-catalog lanes |
| Dataset identity records | `data/registry/datasets/` |
| Crosswalk mapping records | `data/registry/crosswalks/` |
| Semantic contracts | `contracts/` |
| JSON Schema or machine contract shape | `schemas/contracts/v1/` |
| Policy rules, rights rules, sensitivity rules, geoprivacy rules, access-control rules, or release rules | `policy/` |
| Validator code, connector code, pipelines, transformations, package code, or app code | `tools/`, `connectors/`, `pipelines/`, `packages/`, `apps/` |
| Fixtures, tests, or CI workflows | `fixtures/`, `tests/`, `.github/workflows/` |
| Validation receipts, run receipts, redaction receipts, review receipts, or process-memory logs | `data/receipts/` |
| EvidenceBundle records, proof packs, signatures, or citation-validation closure | `data/proofs/` |
| STAC/DCAT/PROV/domain catalog records or graph/triplet projections | `data/catalog/` and `data/triplets/` |
| Published artifacts, map layers, tiles, dashboards, reports, public API payloads, generated-answer carriers | `data/published/`, governed app/API roots, and release-approved public artifact lanes |
| ReleaseManifest, PromotionDecision, CorrectionNotice, RollbackCard, withdrawal notice, or supersession notice | `release/` |

---

## Suggested directory shape

The map below is **PROPOSED** documentation guidance, not proof that child folders or records exist beyond confirmed README evidence.

```text
data/registry/domains/
├── README.md
├── soil/
│   └── README.md
├── <domain>/
│   ├── README.md
│   ├── object_families/
│   │   ├── README.md
│   │   └── index.local.json
│   ├── source_families/
│   │   ├── README.md
│   │   └── index.local.json
│   ├── readiness/
│   │   ├── README.md
│   │   └── index.local.json
│   └── index.local.json
└── index.local.json
```

`index.local.json` files are registry-local lookup aids. They are not proof indexes, catalog records, release manifests, search indexes, vector indexes, graph projections, map sources, public API payloads, or generated-answer sources.

---

## Suggested record shape

The exact schema remains **NEEDS VERIFICATION**. A domain registry record should be structured enough for audit, validation, correction, rollback, and release review.

```json
{
  "id": "kfm-domain-registry:<domain>:<stable-id>",
  "record_type": "domain_registry_record",
  "domain": "soil | flora | fauna | hydrology | habitat | geology | atmosphere | archaeology | hazards | agriculture | people-dna-land | roads-rail-trade | settlements-infrastructure | other",
  "registry_family": "domain_state | object_family | source_family | readiness | blocker | release_support | other",
  "status": "candidate | active | restricted | blocked | deprecated | superseded | withdrawn | denied",
  "object_family_refs": [],
  "source_family_refs": [],
  "source_descriptor_refs": [],
  "dataset_registry_refs": [],
  "crosswalk_registry_refs": [],
  "source_role_summary": [],
  "rights_posture": "open | attribution-required | restricted | stewarded | unknown | denied",
  "sensitivity_posture": "public-safe | generalized | restricted | denied | needs-review",
  "lifecycle_refs": {
    "raw": [],
    "work": [],
    "quarantine": [],
    "processed": [],
    "catalog": [],
    "triplets": [],
    "published": []
  },
  "contract_refs": [],
  "schema_refs": [],
  "policy_refs": [],
  "validation_receipt_refs": [],
  "evidence_refs": [],
  "proof_refs": [],
  "catalog_refs": [],
  "review_refs": [],
  "release_refs": [],
  "correction_refs": [],
  "rollback_refs": [],
  "blockers": [],
  "public_exposure": "none | eligible-after-review | released-public-safe | denied",
  "created_at": "timestamp",
  "updated_at": "timestamp"
}
```

Do not treat this JSON block as a live schema. It is a maintainer-facing sketch until paired contracts, schemas, validators, fixtures, examples, CI, and review workflows are verified.

---

## Required checks before use

- [ ] Confirm the object is a domain registry record, not source data, source descriptor, dataset registry record, crosswalk, proof, receipt, catalog record, release decision, policy, schema, validator, fixture, or test.
- [ ] Confirm the owning root is `data/` and the registry lane is appropriate under Directory Rules.
- [ ] Confirm domain segment naming matches accepted domain placement law and does not create a root-level domain folder.
- [ ] Confirm source descriptor refs, source role, rights posture, cadence, source family, support type or domain-specific equivalent, stewardship obligations, and authority limits are preserved.
- [ ] Confirm domain registry state does not upgrade source role, evidence strength, review state, catalog state, release state, or public-safe posture.
- [ ] Confirm sensitive details are not exposed in registry files, local indexes, or public summaries.
- [ ] Confirm rights, sensitivity, geoprivacy, cultural, living-person, rare-species, archaeology, infrastructure, precise-location, and source-term risks fail closed when unresolved.
- [ ] Confirm validation receipts exist before catalog or release eligibility is asserted.
- [ ] Confirm EvidenceRef/EvidenceBundle and proof refs exist for consequential use.
- [ ] Confirm catalog refs point to STAC/DCAT/PROV/domain catalog records rather than embedding them.
- [ ] Confirm release refs point to ReleaseManifest/PromotionDecision objects rather than implying publication from registry state.
- [ ] Confirm correction, supersession, withdrawal, stale-state, and rollback paths exist for mutable or externally governed domain material.
- [ ] Confirm no public client, map layer, graph edge, vector index, generated answer, report, or dashboard reads this registry lane as direct public truth.

---

## Status notes

| Claim | Status |
|---|---:|
| This README replaces the greenfield stub at `data/registry/domains/README.md`. | CONFIRMED authored |
| The target path existed in the live repository as a greenfield stub before this edit. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/domains/soil/README.md` exists as a child domain registry README. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/datasets/README.md` exists as a sibling registry README and keeps dataset registry state separate from payloads, proofs, receipts, catalog records, and releases. | CONFIRMED by GitHub contents API in this sequence |
| `data/registry/crosswalks/README.md` exists as a sibling registry README and keeps crosswalk registry state separate from contracts, schemas, policy, proofs, catalog, release decisions, and public claims. | CONFIRMED by GitHub contents API in this sequence |
| Emitted domain registry payloads exist under this parent lane. | UNKNOWN |
| A canonical domain registry schema is fully enforced. | NEEDS VERIFICATION |
| CI validates domain registry records. | UNKNOWN |
| This README grants public access to domain registry internals. | DENY |

---

## Maintainer note

Domain registry records are useful because they make domain-state, object families, source families, lifecycle refs, blockers, correction, and rollback inspectable. They become dangerous when treated as payloads, proofs, catalog closure, or release decisions. Keep the chain explicit:

```text
source/dataset/crosswalk registry refs + domain registry record -> lifecycle payload -> validation receipt -> proof/catalog/policy/review -> release -> governed public surface
```

Never collapse it into:

```text
domain registry record -> public truth
```
