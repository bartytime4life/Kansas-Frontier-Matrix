<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/datasets/flora/readme
name: Flora Dataset Registry README
path: data/registry/datasets/flora/README.md
type: data-registry-datasets-domain-readme
version: v0.2.0
status: draft
owners:
  - "NEEDS VERIFICATION: registry steward"
  - "NEEDS VERIFICATION: dataset steward"
  - "NEEDS VERIFICATION: Flora domain steward"
  - "NEEDS VERIFICATION: contract, schema, and policy stewards"
  - "NEEDS VERIFICATION: validation, evidence, and release stewards"
created: 2026-06-28
updated: 2026-07-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: registry
registry_scope: flora-dataset-registry-records
path_posture: confirmed-live-canonical-subtype-first-lane; record-inventory-unknown; schema-and-validator-coverage-unverified
sensitivity_posture: registry-internal; no-public-path; rare-plant-deny-default; source-role-preserving; evidence-aware; policy-aware; release-blocked-until-gates-close
related:
  - ../README.md
  - ../../README.md
  - ../../sources/flora/README.md
  - ../../layers/flora/README.md
  - ../../rights/flora/README.md
  - ../../sensitivity/flora/README.md
  - ../../../raw/flora/README.md
  - ../../../work/flora/README.md
  - ../../../quarantine/flora/README.md
  - ../../../processed/flora/README.md
  - ../../../receipts/flora/README.md
  - ../../../proofs/flora/README.md
  - ../../../catalog/stac/flora/README.md
  - ../../../catalog/dcat/flora/README.md
  - ../../../catalog/prov/flora/README.md
  - ../../../published/flora/README.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../../docs/domains/flora/DATA_LIFECYCLE.md
  - ../../../../docs/domains/flora/SENSITIVITY.md
  - ../../../../contracts/data/dataset_version.md
  - ../../../../schemas/contracts/v1/registries/README.md
  - ../../../../policy/domains/flora/README.md
  - ../../../../fixtures/domains/flora/README.md
  - ../../../../tests/domains/flora/README.md
  - ../../../../release/candidates/flora/README.md
tags:
  - kfm
  - data
  - registry
  - datasets
  - flora
  - dataset-identity
  - source-role
  - provenance
  - evidence
  - rights
  - sensitivity
  - rare-plant
  - geoprivacy
  - correction
  - rollback
  - release-gated
  - no-public-path
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_commit: 4f16e53285a7523121419a9fb5b33c6955bd087a
  prior_blob: 14d294f27ab2e9260310bc5487520a15952d87eb
  parent_datasets_blob: 04b67852e50ba3174cc122b8166686e507070253
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  adr_0029_blob: cd044a38047cc9b3725d2e083eb201eb86109308
  registry_schema_guardrail_blob: 9af6574ec32bde3d60a904fccf9b0dc4bb71703b
  dataset_version_contract_blob: 06a0345b19f753632068978c61d5d0e50011305d
  inspection_date: 2026-07-28
notes:
  - "This README preserves and upgrades the existing document at the same canonical subtype-first registry path."
  - "ADR-0029 accepted Directory Rules v2; its registry topology resolves data/registry/datasets/flora/ as a canonical dataset-family lane rather than an unresolved path."
  - "Search-limited repository inspection surfaced no concrete Flora dataset registry payload, accepted dataset-registry schema, registry-specific validator, or registry-specific fixture/test suite."
  - "The shared registry-schema family is README-only and labels dataset_registry_record.schema.json as a proposed candidate; DatasetVersion is a separate draft semantic contract whose paired schema is explicitly a placeholder."
  - "Registry presence does not admit a source, prove a Flora claim, clear rights or sensitivity, authorize release, or publish KFM content."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Flora Dataset Registry

[![Document lifecycle: draft](https://img.shields.io/badge/document-draft-d4a72c?style=flat-square)](#status)
[![Path posture: canonical](https://img.shields.io/badge/path-canonical-0969da?style=flat-square)](#authority-and-path-posture)
[![Artifact family: dataset registry](https://img.shields.io/badge/family-dataset%20registry-8250df?style=flat-square)](#dataset-registry-boundary)
[![Public access: denied](https://img.shields.io/badge/public%20access-denied-b42318?style=flat-square)](#flora-sensitivity-and-publication-boundary)
[![Truth posture: cite or abstain](https://img.shields.io/badge/truth-cite%20or%20abstain-1a7f37?style=flat-square)](#validation-and-maintenance)

> **One-line purpose.** Govern Flora dataset identity and dataset-state records without storing dataset payloads or taking over source, contract, schema, policy, evidence, catalog, release, or publication authority.

> [!CAUTION]
> A registry record is a governance handle, not botanical truth or a public dataset. Exact rare, protected, culturally sensitive, stewarded, or join-sensitive plant information remains denied from public surfaces unless an authorized transform, receipt, policy decision, review, release, correction path, and rollback target close the applicable gates.

## Navigation

[Status](#status) · [Scope](#scope) · [Authority](#authority-and-path-posture) · [Repository fit](#repository-fit) · [Boundary](#dataset-registry-boundary) · [Dataset families](#dataset-family-coverage) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs/outputs](#inputs-and-outputs) · [Lifecycle](#lifecycle-and-governed-use) · [Sensitivity](#flora-sensitivity-and-publication-boundary) · [Validation](#validation-and-maintenance) · [Verification](#open-verification-items) · [Rollback](#correction-supersession-and-rollback)

---

## Status

| Field | Evidence-backed state |
|---|---|
| Repository path | `data/registry/datasets/flora/` — **CONFIRMED** at the pinned base |
| README profile | `BOUNDARY_COMPACT` domain lane under the dataset registry family |
| Directory placement | **CONFIRMED canonical** subtype-first registry topology under accepted Directory Rules v2 |
| Document lifecycle | `draft` |
| Concrete registry-record inventory | **UNKNOWN**; no payload surfaced in the search-limited inspection |
| Shared dataset-registry schema | **NEEDS VERIFICATION**; the shared registry schema lane is README-only and names a candidate schema that is not present |
| Adjacent DatasetVersion contract | **CONFIRMED draft**; its paired schema is explicitly a permissive placeholder |
| Dataset-registry validator, fixtures, tests, and CI | **NEEDS VERIFICATION** |
| Accountable owners and reviewers | **NEEDS VERIFICATION** |
| Direct public access | **DENY** |
| KFM publication effect | None |

A file, stable ID, schema-valid object, passing workflow, commit, pull request, or merge does not establish source admission, dataset correctness, rights clearance, public safety, evidence closure, release approval, or KFM publication.

---

## Scope

This lane governs compact records that identify and route Flora datasets and their governed state. A record may describe:

- taxon backbones and taxon lists;
- herbarium specimen collections;
- occurrence datasets;
- rare, protected, culturally sensitive, or stewarded plant datasets;
- vegetation community datasets;
- invasive plant datasets;
- phenology datasets;
- range or distribution datasets;
- restoration planting datasets;
- public-safe generalized Flora derivatives.

The registry may answer bounded questions:

- Which stable dataset family or dataset version is being referenced?
- Which source identities, source roles, rights terms, sensitivity posture, cadence, spatial scope, temporal scope, and authority limits apply?
- Which RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLETS, or PUBLISHED objects are related?
- Which validation receipts, EvidenceRefs, EvidenceBundles, policy decisions, reviews, catalogs, release decisions, corrections, supersessions, withdrawals, and rollback targets support governed use?
- Which unresolved conditions require hold, restriction, denial, quarantine, abstention, correction, or withdrawal under the applicable contract?

This README does not define a universal dataset-registry schema or outcome vocabulary. Those remain contract- and implementation-specific until accepted authority exists.

---

## Authority and path posture

Accepted [Directory Rules v2](../../../../docs/doctrine/directory-rules.md), adopted through [ADR-0029](../../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md), separates registry identity from lifecycle payloads and makes registry placement subtype-first:

```text
data/registry/
├── sources/
├── datasets/
├── layers/
├── domains/
├── rights/
├── sensitivity/
└── crosswalks/
```

The Flora dataset lane therefore resolves as:

```text
data/registry/datasets/flora/
```

| Responsibility signature axis | Resolved value |
|---|---|
| Artifact kind | Dataset registry record or registry boundary documentation |
| Authority owner | Registry identity and routing |
| Lifecycle stage | Registry accountability plane |
| Scope | Domain lane: `flora` |
| Exposure | Internal or restricted unless a separate released projection exists |
| Placement outcome | `PLACE` at the current subtype-first path |

This placement is canonical for the registry family, but it does not prove that registry payloads, a complete semantic contract, a machine schema, validators, producers, consumers, or public-safe projections are implemented.

`data/registry/flora/` and other domain-first registry parents must not become parallel writers for records owned here. Any compatibility view must remain single-write, generated from canonical records, parity-checked, and governed by an accepted migration.

---

## Repository fit

| Responsibility | Owning surface | Relationship to this lane |
|---|---|---|
| Registry governance | [`data/registry/`](../../README.md) | Parent identity and routing boundary |
| Dataset registry family | [`data/registry/datasets/`](../README.md) | Parent subtype-first dataset family |
| Flora dataset records | `data/registry/datasets/flora/` | Stable dataset identity, state, routing, and correction pointers |
| Flora source identity | [`data/registry/sources/flora/`](../../sources/flora/README.md) | SourceDescriptor, source role, rights, cadence, and authority inputs |
| Flora layer identity | [`data/registry/layers/flora/`](../../layers/flora/README.md) | Layer registry state; does not replace dataset identity |
| Rights and sensitivity identity | [Rights](../../rights/flora/README.md) and [sensitivity](../../sensitivity/flora/README.md) registries | References to governed rights and sensitivity state |
| Dataset-version meaning | [`DatasetVersion`](../../../../contracts/data/dataset_version.md) | Adjacent draft semantic contract; not a complete dataset-registry contract |
| Registry machine shape | [`schemas/contracts/v1/registries/`](../../../../schemas/contracts/v1/registries/README.md) | README-only guardrail; accepted dataset-registry schema not verified |
| Flora policy | [`policy/domains/flora/`](../../../../policy/domains/flora/README.md) | Admissibility, sensitivity, geoprivacy, and exposure decisions |
| Lifecycle payloads | [RAW](../../../raw/flora/README.md), [WORK](../../../work/flora/README.md), [QUARANTINE](../../../quarantine/flora/README.md), and [PROCESSED](../../../processed/flora/README.md) | Actual Flora bytes and governed transforms; never stored here |
| Process and evidence support | [Receipts](../../../receipts/flora/README.md) and [proofs](../../../proofs/flora/README.md) | Process memory and evidence support; neither is registry state |
| Catalog projections | [STAC](../../../catalog/stac/flora/README.md), [DCAT](../../../catalog/dcat/flora/README.md), and [PROV](../../../catalog/prov/flora/README.md) | Discovery and provenance projections; not registry authority |
| Release and delivery | [Flora release candidates](../../../../release/candidates/flora/README.md) and [published carriers](../../../published/flora/README.md) | Separate release decision and public-delivery boundaries |
| Validation evidence | [Flora fixtures](../../../../fixtures/domains/flora/README.md) and [tests](../../../../tests/domains/flora/README.md) | Current domain evidence does not establish dataset-registry coverage |

---

## Dataset registry boundary

| Rule | Required handling |
|---|---|
| Registry record is a handle | Identify and route a dataset; do not embed its payload. |
| Dataset family and version remain distinct | Do not collapse a durable dataset identity into one retrieval, file, release, or mutable alias. |
| Source identity remains separate | Resolve source records and preserve source role; do not duplicate source authority here. |
| Source role cannot be upgraded | Normalization, aggregation, cataloging, mapping, release review, UI display, or AI language cannot promote source authority. |
| Space and time remain explicit | Preserve dataset extent, precision, observation/valid/retrieval/revision/release time, cadence, and stale-state boundaries where material. |
| Rights and sensitivity fail closed | Unknown license, redistribution terms, steward obligations, rare-plant risk, cultural sensitivity, private-land exposure, or harmful precision blocks public use. |
| Registry is not contract or schema | Meaning stays under `contracts/`; machine shape stays under `schemas/`. |
| Registry is not receipt or proof | Process memory and EvidenceBundle support retain separate authority. |
| Registry is not catalog | STAC, DCAT, PROV, domain, and matrix projections remain under `data/catalog/`. |
| Registry is not policy or release | Policy and release decisions cannot be inferred from registry state. |
| Registry changes remain auditable | Preserve version, correction, supersession, withdrawal, stale-state, and rollback lineage. |
| Public clients do not read this lane | APIs, maps, search, graphs, exports, dashboards, and AI surfaces use governed released interfaces. |

Registry records should point outward by stable ID, repository path, governed URI, digest, or EvidenceRef. Copying source payloads, policies, proofs, catalogs, or release objects into the registry creates authority drift.

---

## Dataset family coverage

| Dataset family | Registry concern | Additional Flora control |
|---|---|---|
| Taxon backbone or list | Identity, authority version, source role, temporal coverage, supersession | Preserve accepted and source-native taxonomy; unresolved names remain visible |
| Specimen collection | Collection identity, source, rights, digitization scope, retrieval/version state | Do not expose restricted collector, locality, land, or steward detail |
| Occurrence dataset | Dataset/version identity, spatial and temporal scope, source role, precision | Exact rare or protected plant locations fail closed |
| Rare or stewarded plant dataset | Restricted identity, access class, review and correction lineage | No ordinary public path; generalization does not authorize release by itself |
| Vegetation community dataset | Classification/version identity, method, scale, source roles | Derived class or polygon does not become field observation truth |
| Invasive plant dataset | Authority scope, observation/model distinction, update cadence | Registry presence is not regulatory designation or current condition |
| Phenology dataset | Observation/model distinction, season/year, method, uncertainty | Do not generalize a local or historical series into timeless statewide truth |
| Range or distribution dataset | Model/observation role, scale, vintage, uncertainty, source support | Polygon presence is not point occurrence or completeness proof |
| Restoration dataset | Program/source identity, treatment period, rights, review state | Do not expose private-land, participant, or precise-sensitive details |
| Public-safe derivative | Canonical parent, transform and receipt refs, release/correction lineage | Public-safe status requires policy, review, release, and rollback evidence |

These families describe possible record scope. They do not prove that corresponding child directories or records exist.

---

## What belongs here

- accepted Flora dataset registry records;
- registry-local indexes that resolve to canonical records without becoming catalog, search, graph, map, release, or public API authority;
- stable dataset-family and dataset-version identifiers;
- pointer-only source, rights, sensitivity, lifecycle, evidence, validation, policy, review, catalog, release, correction, withdrawal, supersession, and rollback references;
- cadence, freshness, spatial and temporal scope, public-exposure posture, and blocker state defined by an accepted contract;
- integrity metadata required by the governing registry contract;
- README files that explain the boundary without claiming implementation;
- migration or tombstone metadata required by an accepted single-write migration.

Do not create a child directory merely to reserve a future dataset family. Directory Rules v2 prohibits empty symmetry scaffolding.

---

## What does not belong here

| Do not place here | Owning surface or required action |
|---|---|
| Darwin Core archives, specimen dumps, occurrence exports, tables, rasters, shapefiles, GeoParquet, COG, PMTiles, or source-native payloads | Governed RAW, WORK, QUARANTINE, or PROCESSED Flora lanes |
| Exact rare, protected, culturally sensitive, steward-only, private-land, or join-sensitive plant detail | Approved restricted storage or QUARANTINE with deny-by-default controls |
| SourceDescriptor, source activation, source terms, or source-role authority | `data/registry/sources/`, source contracts, and governed admission |
| Layer, rights, sensitivity, domain, or crosswalk records | Their subtype-first registry families |
| Semantic contract or JSON Schema | `contracts/` and `schemas/` |
| Policy, geoprivacy, access, rights, sensitivity, or release rules | `policy/` |
| Connector, pipeline, package, validator, or application code | Its implementation responsibility root |
| Fixtures, tests, or workflow definitions | `fixtures/`, `tests/`, and `.github/workflows/` |
| Run, validation, redaction, aggregation, review, or correction receipts | `data/receipts/` |
| EvidenceBundle, proof pack, signature, or citation closure | `data/proofs/` |
| STAC, DCAT, PROV, domain, matrix, or other catalog record | `data/catalog/` |
| ReleaseManifest, PromotionDecision, CorrectionNotice, WithdrawalNotice, or RollbackCard | `release/` |
| Public layer, tile, report, dashboard, API payload, export, graph, index, or generated answer | Governed released delivery surface |
| Credentials, tokens, signed URLs, private endpoints, or restricted operational details | Approved secret or restricted storage; never this public repository path |

---

## Inputs and outputs

| Direction | Accepted surface | Boundary |
|---|---|---|
| Input | Stable Flora dataset and version identity | Must be contract-backed or remain explicitly unresolved |
| Input | Canonical source identities and source-role metadata | Registry reference only; no duplicated source authority |
| Input | Rights, sensitivity, spatial/temporal scope, cadence, freshness, evidence, policy, review, catalog, release, correction, and rollback refs | References must resolve before consequential use |
| Output | Compact dataset identity and governed state record | Internal governance handle, not payload or truth |
| Output | Pointer-only routing for lifecycle, catalog, review, correction, and release processes | Does not approve the referenced transition |
| Output | Optional public-safe registry projection | Requires a separate contract, policy, release, correction, and rollback path |
| Output | Explicit unresolved or blocked state | Must preserve the applicable contract vocabulary and fail closed |

No normal public API, map, graph, export, search index, dashboard, or generated-answer contract originates from this directory.

---

## Lifecycle and governed use

```text
source identity + dataset identity
  -> RAW / WORK / QUARANTINE payload
  -> validated PROCESSED representation
  -> evidence + receipts + policy + review
  -> catalog / triplet projection when applicable
  -> release decision
  -> immutable public-safe carrier
```

The dataset registry record may reference each stage, but it does not replace any stage or authorize movement between them.

| Lifecycle concern | Registry obligation |
|---|---|
| Admission | Preserve the dataset/source identity, role, rights, sensitivity, scope, and unresolved conditions |
| Transformation | Link versions and transforms without overwriting source-native identity or prior state |
| Validation | Reference run-specific evidence; do not turn schema validity into truth |
| Cataloging | Link discovery projections; do not duplicate catalog records |
| Release | Link the accepted decision and immutable carrier; do not self-declare publication |
| Correction | Preserve the affected identity, prior version, downstream consumers, and correction lineage |
| Withdrawal or supersession | Retain history and point to the successor or withdrawal authority |
| Rollback | Identify the reviewed prior target and dependent invalidation scope |

[Flora lifecycle guidance](../../../../docs/domains/flora/DATA_LIFECYCLE.md) is documentation evidence, not proof that each registry integration is implemented.

---

## Flora sensitivity and publication boundary

[Flora sensitivity guidance](../../../../docs/domains/flora/SENSITIVITY.md) treats exact rare, protected, culturally sensitive, and stewarded plant locations as deny-by-default public material.

For any dataset whose content or joins could reveal sensitive Flora information:

- classify source role, rights, access, precision, spatial support, temporal support, and re-identification risk;
- preserve restricted identity and review obligations in the registry without copying restricted payloads;
- require an authorized public-safe transform and its receipt before a derivative is considered;
- require policy, steward review, evidence, catalog, release, correction, and rollback closure before public delivery;
- invalidate dependent projections when the canonical dataset, rights, sensitivity, taxonomy, transform, or release state changes;
- abstain or deny when the record, evidence, policy, or release state cannot be resolved.

A public-safe label, generalized geometry, badge, schema-valid record, or README statement is not release evidence.

---

## Validation and maintenance

### Confirmed evidence

- The target README exists at the canonical subtype-first path.
- Accepted Directory Rules v2 identifies `data/registry/datasets/` as a registry family under the `data/` responsibility root.
- `DatasetVersion` exists as a draft semantic contract.
- `schemas/contracts/v1/registries/` exists as a README-only schema-family guardrail.
- The registry-schema guardrail lists `dataset_registry_record.schema.json` only as a proposed candidate.
- Flora source, layer, rights, sensitivity, lifecycle, policy, fixture, test, catalog, proof, receipt, release-candidate, and published boundary documents exist at the linked paths.

### Required checks before relying on a record

- [ ] Confirm the object is a dataset registry record, not a payload, source descriptor, layer, rights record, sensitivity record, crosswalk, contract, schema, policy, receipt, proof, catalog, release object, or delivery artifact.
- [ ] Resolve one stable dataset identity and distinguish dataset family from dataset version.
- [ ] Resolve canonical source identity and preserve source-native role, authority, terms, and temporal scope.
- [ ] Verify rights, sensitivity, access, cultural, private-land, rare-species, join, and harmful-precision posture.
- [ ] Verify spatial extent, spatial precision, observation/valid/retrieval/revision/release time, cadence, and stale-state handling.
- [ ] Validate against an accepted semantic contract and machine schema; do not rely on a placeholder schema.
- [ ] Run deterministic valid, invalid, restricted, stale, conflict, correction, and rollback fixtures through the accepted validator.
- [ ] Resolve consequential EvidenceRefs to EvidenceBundles.
- [ ] Confirm validation receipts, policy decisions, review records, catalog refs, release decisions, correction lineage, and rollback targets as applicable.
- [ ] Confirm no public client or AI/map/search/graph surface reads internal or candidate registry state directly.
- [ ] Confirm no secret, private identifier, restricted note, or sensitive location enters ordinary repository or public output.

The current broad Flora workflow is a read-only readiness workflow with explicit validation, proof, and release holds. It does not validate Flora dataset registry records or establish public readiness. The repository link-check workflow is also an explicit hold and does not currently resolve links.

---

## Open verification items

| Item | Status | Evidence required |
|---|---|---|
| Complete direct-child and record inventory | **UNKNOWN** | Pinned recursive tree plus classification of every non-README object |
| Canonical dataset-registry semantic contract | **NEEDS VERIFICATION** | Accepted contract defining identity, versions, states, invariants, and compatibility |
| Canonical dataset-registry schema | **NEEDS VERIFICATION** | Accepted `$id`, fields, enums, refs, migration policy, and contract pairing |
| Dataset-registry validator | **NEEDS VERIFICATION** | Repository-owned deterministic implementation and finite outcomes |
| Valid, invalid, restricted, stale, conflict, correction, and rollback fixtures | **NEEDS VERIFICATION** | Public-safe synthetic fixture suite and representative observed runs |
| Producers and consumers | **UNKNOWN** | Connector, pipeline, tool, catalog, release, API/UI, map, graph, search, export, and AI inventory |
| Rights and sensitivity enforcement | **NEEDS VERIFICATION** | Policy rules, negative fixtures, decisions, receipts, access controls, and tests |
| Correction and rollback propagation | **NEEDS VERIFICATION** | Corrected dataset/version case, invalidation list, regenerated projections, and rollback drill |
| Steward and reviewer assignments | **NEEDS VERIFICATION** | Accepted authority register or path-specific ownership evidence |

Unknowns narrow permissible use. They do not authorize plausible defaults or public exposure.

---

## Correction, supersession, and rollback

For a registry-record correction:

1. Identify the canonical dataset and affected versions.
2. Preserve the prior record or immutable lineage.
3. Correct the owning source, contract, schema, policy, evidence, or release authority first when the defect originates there.
4. Emit the applicable correction, withdrawal, supersession, review, and release records through their owning families.
5. Invalidate and regenerate dependent catalogs, layers, indexes, graphs, caches, exports, maps, APIs, and generated answers.
6. Verify the reviewed prior release or version before rollback.

For this README before merge, rollback is the prior blob `14d294f27ab2e9260310bc5487520a15952d87eb` on the scoped branch. After merge, use a transparent revert or follow-up pull request. Documentation rollback must not delete dataset records, rewrite history, restore an invalid authority claim, or change release state.

---

## Maintainer rule

```text
dataset registry record
  -> identifies and routes governed dataset state
  -> resolves evidence, policy, review, catalog, release, correction, and rollback
  -> supports a governed public-safe carrier when separately authorized
```

Never collapse the chain into:

```text
registry presence or schema validity
  -> accepted Flora truth or public release
```

## Change history

### v0.2.0 — 2026-07-28

- aligned the existing README with accepted Directory Rules v2 and canonical subtype-first registry placement;
- replaced unresolved-path language with a bounded `PLACE` decision;
- removed the speculative child directory tree and unaccepted record enum;
- distinguished Flora dataset registry state from the draft `DatasetVersion` contract and README-only registry-schema family;
- preserved dataset-family coverage, source role, rights, sensitivity, lifecycle, correction, rollback, and public-boundary controls;
- added evidence-backed badges, navigation, repository-fit mappings, validation, and explicit verification holds.

### v0.1.0 — 2026-06-28

- replaced the original empty placeholder with a detailed Flora dataset-registry boundary;
- recorded path, schema, validator, record, and CI uncertainty then known.

[Back to top](#top)
