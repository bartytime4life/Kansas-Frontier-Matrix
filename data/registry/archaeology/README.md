<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/archaeology/readme
name: Archaeology Registry README
path: data/registry/archaeology/README.md
type: data-registry-domain-parent-readme
version: v0.3.0
status: draft
owners:
  - "NEEDS VERIFICATION: registry steward"
  - "NEEDS VERIFICATION: archaeology domain steward"
  - "NEEDS VERIFICATION: cultural review steward"
  - "NEEDS VERIFICATION: rights and sensitivity reviewers"
  - "NEEDS VERIFICATION: policy and validation stewards"
created: 2026-06-28
updated: 2026-07-27
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: registry
registry_scope: archaeology-domain-registry-compatibility-parent
path_posture: confirmed-live-domain-first-parent; compatibility-boundary; independent-writes-denied; migration-needs-accepted-decision
sensitivity_posture: restricted-by-default; protected-location-deny-default; cultural-review-required; rights-and-current-terms-required-before-activation; no-public-path; release-blocked-until-redaction-review-release
related:
  - ../README.md
  - sources/README.md
  - ../sources/README.md
  - ../sources/archaeology/README.md
  - ../source_descriptors/README.md
  - ../../raw/archaeology/README.md
  - ../../work/archaeology/README.md
  - ../../quarantine/archaeology/README.md
  - ../../processed/archaeology/README.md
  - ../../receipts/README.md
  - ../../proofs/README.md
  - ../../catalog/README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../docs/domains/archaeology/SOURCE_REGISTRY.md
  - ../../../docs/domains/archaeology/SOURCES.md
  - ../../../docs/domains/archaeology/SENSITIVITY.md
  - ../../../docs/domains/archaeology/PUBLICATION_AND_POLICY.md
  - ../../../docs/domains/archaeology/VERIFICATION_BACKLOG.md
  - ../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../docs/registers/SOURCE_AUTHORITY.md
  - ../../../control_plane/source_authority_register.yaml
  - ../../../contracts/source/source_descriptor.md
  - ../../../schemas/contracts/v1/source/README.md
  - ../../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../../policy/domains/archaeology/README.md
  - ../../../.github/workflows/source-descriptor-validate.yml
tags:
  - kfm
  - data
  - registry
  - archaeology
  - compatibility
  - source-descriptor
  - admission-control
  - source-role
  - cultural-review
  - sovereignty
  - rights
  - sensitivity
  - protected-location-deny
  - migration
  - cite-or-abstain
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_commit: 3cb429a9dd1027d62fe0f83cd870fa222763e3b8
  prior_blob: d5ab80475accb0fde7077774e3e884c3f99821a0
  child_compatibility_blob: 421d8b3dcb6872c36c87ac7856a5bfbea3f4cc58
  canonical_lane_blob: 40f859e7b61cec8fb6e27268f2f5b38bcd57bb4f
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  adr_0029_blob: cd044a38047cc9b3725d2e083eb201eb86109308
  inspection_date: 2026-07-27
notes:
  - "This README preserves the stable identity of the existing domain-first Archaeology registry parent path."
  - "The source-descriptor writer is data/registry/sources/archaeology/ under adopted Directory Rules v2."
  - "The child data/registry/archaeology/sources/README.md is a read-only compatibility boundary and must not evolve independently."
  - "No accepted migration, redirect, or retirement record was verified for this parent path."
  - "This directory is not raw source storage, a site inventory, proof, catalog, release state, policy source, public output, or protected-location authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Archaeology Registry

[![Document lifecycle: draft](https://img.shields.io/badge/document-draft-d4a72c?style=flat-square)](#status)
[![Path class: compatibility parent](https://img.shields.io/badge/path-compatibility%20parent-d4a72c?style=flat-square)](#path-posture)
[![Canonical writer: subtype-first](https://img.shields.io/badge/canonical%20writer-subtype--first-0969da?style=flat-square)](#path-posture)
[![Independent writer: denied](https://img.shields.io/badge/independent%20writer-denied-b42318?style=flat-square)](#registry-boundary)
[![Protected locations: deny](https://img.shields.io/badge/protected%20locations-deny-b42318?style=flat-square)](#sensitivity-and-publication-boundary)

> Domain-first compatibility parent for Archaeology registry routing. It preserves path identity and makes the canonical source-registry relationship visible; it does not admit, activate, validate, release, or publish a source.

> [!CAUTION]
> Do not add authoritative source descriptors or new independently maintained registry families under this parent. Adopted Directory Rules v2 establishes the source-descriptor writer at [`data/registry/sources/archaeology/`](../sources/archaeology/README.md). The child [`sources/`](sources/README.md) path is a read-only compatibility boundary until an accepted migration or retirement record says otherwise.

> [!WARNING]
> Archaeology is a sensitive domain. Exact site geometry, sacred or burial-associated locations, human-remains context, private-land detail, collection-security information, and culturally restricted knowledge fail closed. Public availability of a source does not authorize KFM ingestion, joining, map exposure, search indexing, AI use, or disclosure.

## Navigation

[Status](#status) · [Scope](#scope) · [Path posture](#path-posture) · [Repository fit](#repository-fit) · [Confirmed child lanes](#confirmed-child-lanes) · [Boundary](#registry-boundary) · [Sensitivity](#sensitivity-and-publication-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Validation](#validation-and-maintenance) · [Required checks](#required-checks-before-use) · [Open verification](#open-verification-items) · [Rollback](#rollback)

---

## Status

| Field | Current result |
|---|---|
| Repository path | `data/registry/archaeology/` — **CONFIRMED** at the pinned base |
| Document lifecycle | `draft` |
| README profile | Sensitive `BOUNDARY_COMPACT` compatibility parent |
| Path class | **Compatibility parent / duplicate-writer risk** |
| Canonical source-descriptor writer | [`data/registry/sources/archaeology/`](../sources/archaeology/README.md) |
| Confirmed local child | [`sources/`](sources/README.md), itself a compatibility boundary |
| Local authoritative descriptor payloads | None established by this README |
| Independent-write posture | **DENY** |
| Source admission or activation | Not established by this README |
| Direct public access | **DENY** |
| KFM publication effect | None |
| Accountable stewardship assignments | **NEEDS VERIFICATION** |

A path, README, YAML file, workflow result, commit, pull request, source URL, or public upstream record does not establish source authority, rights clearance, sensitivity clearance, evidence closure, release approval, or publication.

---

## Scope

This README governs the existing domain-first Archaeology registry parent while the repository converges on subtype-first source-registry placement. Its responsibilities are limited to:

- preserving the parent path's stable document identity and public-safe lineage;
- identifying the canonical source-descriptor writer and preventing parallel authority;
- routing maintainers to the appropriate contract, schema, policy, validation, evidence, catalog, and release surfaces;
- documenting the child compatibility path without treating it as an implementation authority;
- recording migration, correction, rollback, and unresolved-review boundaries.

This README does **not** define or change source roles, approve rights, clear sensitivity, activate connectors, authorize watchers, ingest payloads, construct evidence, approve a release, or publish Archaeology information.

---

## Path posture

Three registry surfaces are relevant:

| Path | Verified repository state | Bounded posture |
|---|---|---|
| `data/registry/archaeology/` | This parent README and the `sources/` child | Domain-first compatibility parent; independent writes denied |
| [`data/registry/archaeology/sources/`](sources/README.md) | Compatibility README; no descriptor payloads confirmed in that path | Read-only compatibility child; independent writes denied |
| [`data/registry/sources/archaeology/`](../sources/archaeology/README.md) | README, registry YAML files, and source-family descriptor records | Canonical subtype-first Archaeology source-registry lane under adopted Directory Rules v2 |

Accepted ADR-0029 adopts the exact Directory Rules v2 bytes and makes `docs/doctrine/directory-rules.md` the placement authority. The adopted rules use subtype-first registry placement and prohibit compatibility or alternate paths from becoming independent writers.

> [!IMPORTANT]
> Path presence is not authority. Preserve this parent until references and consumers are inventoried. Do not move, delete, redirect, repurpose, or retire it without an accepted migration record, reference closure, rollback plan, and verified consumer handling.

---

## Repository fit

| Responsibility | Owning surface | Relationship to this path |
|---|---|---|
| Registry governance | [`data/registry/README.md`](../README.md) | Parent responsibility and registry boundary |
| Canonical source registry | [`data/registry/sources/README.md`](../sources/README.md) | Subtype-first source-admission family |
| Archaeology canonical source lane | [`data/registry/sources/archaeology/README.md`](../sources/archaeology/README.md) | Authoritative current writer and descriptor inventory |
| Domain-first child | [`sources/`](sources/README.md) | Compatibility boundary retained for lineage and consumer handling |
| Compatibility descriptor routing | [`data/registry/source_descriptors/`](../source_descriptors/README.md) | Compatibility/routing lane; must not become a second descriptor authority |
| Human source guidance | [`SOURCE_REGISTRY.md`](../../../docs/domains/archaeology/SOURCE_REGISTRY.md) and [`SOURCES.md`](../../../docs/domains/archaeology/SOURCES.md) | Human explanation, source families, rights, cadence, and review guidance |
| Semantic meaning | [`contracts/source/source_descriptor.md`](../../../contracts/source/source_descriptor.md) | `SourceDescriptor` meaning and invariants |
| Machine shape | [`schemas/contracts/v1/source/`](../../../schemas/contracts/v1/source/README.md) | Proposed schema family and compatibility surface |
| Policy | [`policy/domains/archaeology/`](../../../policy/domains/archaeology/README.md) | Archaeology admissibility, sensitivity, and public-surface decisions |
| Governance register | [`control_plane/source_authority_register.yaml`](../../../control_plane/source_authority_register.yaml) | Source-authority projection; completeness and enforcement need verification |
| Validation workflow | [`source-descriptor-validate.yml`](../../../.github/workflows/source-descriptor-validate.yml) | Workflow evidence only; passing checks do not activate or release a source |
| Payload lifecycle | [RAW](../../raw/archaeology/README.md), [WORK](../../work/archaeology/README.md), [QUARANTINE](../../quarantine/archaeology/README.md), and [PROCESSED](../../processed/archaeology/README.md) | Source payloads and transformations; never stored in this compatibility parent |
| Evidence and release | [receipts](../../receipts/README.md), [proofs](../../proofs/README.md), [catalog](../../catalog/README.md), and `release/` | Separate process memory, evidence closure, discovery, release, correction, and rollback authority |

---

## Confirmed child lanes

The current parent confirms one direct child:

```text
data/registry/archaeology/
├── README.md
└── sources/
    └── README.md
```

| Child lane | Status | Purpose | Boundary |
|---|---:|---|---|
| [`sources/`](sources/README.md) | **CONFIRMED compatibility README** | Preserves the historical domain-first source-registry identity and routes maintainers to the subtype-first canonical lane. | Not an independent writer, not raw source data, not receipts, not proofs, not catalog records, not policy, not release, and not public Archaeology truth. |

This direct-child map does not claim that other domain-first registry families exist or should be added. New registry families require independent placement evidence and must not be created merely to fill this parent.

---

## Registry boundary

| Rule | Required handling |
|---|---|
| No independent writer | Do not create or maintain authoritative registry records under this parent while the subtype-first source lane is canonical. |
| Parent is routing, not authority expansion | This README may explain and link; it cannot expand `data/registry/archaeology/` into a parallel registry hierarchy. |
| Preserve deterministic identity | Any migration must map each prior identity to exactly one reviewed canonical identity and disclose collisions. |
| Preserve source role | Observed, regulatory, modeled, aggregate, administrative, candidate, synthetic, contextual, and restricted roles must not be collapsed. |
| Rights fail closed | Unknown license, terms, attribution, redistribution, access, consent, revocation, or sovereignty posture blocks admission and public use. |
| Sensitivity fails closed | Protected sites and culturally restricted knowledge require denial, quarantine, restriction, redaction, generalization, delay, or steward review. |
| Registry is not source data | Payloads enter approved RAW or QUARANTINE lanes through governed intake. |
| Registry is not a decision | Schema-valid shape does not replace source review, policy evaluation, activation, evidence closure, or release. |
| Watchers are non-publishers | Source-health and drift checks may emit candidates and receipts; they cannot activate a source or publish data. |
| Registry is not receipt, proof, catalog, or release | Those object families retain their own authority homes. |
| Public clients do not read this parent | Normal API, map, search, graph, export, and AI surfaces use governed interfaces and released public-safe artifacts. |

---

## Sensitivity and publication boundary

A source may be public while its Archaeology use remains restricted. Every downstream use must preserve source role, rights, cultural authority, spatial precision, valid time, review state, and release state.

| Risk | Required posture |
|---|---|
| Exact archaeological geometry, identifiers, or precise provenience | Do not expose in public-readable registry files, fixtures, indexes, maps, search, vector stores, exports, or generated responses. |
| Burial sites, human remains, funerary objects, sacred places, or culturally restricted knowledge | Fail closed; require cultural/steward review, rights and sovereignty posture, access limits, transformation receipts, evidence, review, release, correction, and rollback. |
| Looting, vandalism, collection-security, or site-condition exposure | Treat as restricted even when upstream material is partly public. Avoid joins that make protected locations discoverable. |
| Private-landowner or access details | Minimize and restrict; public use requires explicit purpose, rights, policy, review, and transformation evidence. |
| Candidate anomalies and predictive surfaces | Preserve `candidate` or `modeled` role; never relabel as confirmed archaeology. |
| Historic maps and georeferenced records | Preserve source vintage and georeference uncertainty; proximity does not prove a site. |
| Cross-domain joins | Review joins with roads, settlements, people/land, infrastructure, geology, habitat, flora, fauna, hydrology, and hazards before release. |

Publication remains downstream of evidence resolution, policy, sensitivity transformation, review, release manifests, correction paths, and rollback targets. A registry record cannot authorize publication.

---

## Accepted material

Until a migration or retirement decision is accepted, this parent may contain only:

- this boundary README;
- the existing `sources/README.md` compatibility child;
- pointer-only alias, redirect, or migration notes that reference one canonical record;
- public-safe rollback information for an approved migration;
- a generated compatibility index only after its generator, canonical inputs, digest, edit policy, and regeneration command are verified.

Manual creation of new authoritative descriptor records or new domain-first registry families is denied.

---

## Exclusions

| Do not place here | Owning surface |
|---|---|
| New or independently maintained `SourceDescriptor` instances | [`data/registry/sources/archaeology/`](../sources/archaeology/README.md), subject to contracts, schemas, policy, and review |
| Raw Archaeology datasets, reports, scans, exports, imagery, geophysics, LiDAR, tables, or API responses | `data/raw/archaeology/`, `data/work/archaeology/`, or `data/quarantine/archaeology/` according to review state |
| Exact site geometry, sacred-site detail, burial or human-remains detail, collection-security detail, private-landowner detail, or steward-only knowledge | Never in public-readable registry files; use approved restricted storage and governed pointers only |
| Processed Archaeology objects or public-safe derivatives | `data/processed/archaeology/` after validation; `data/published/` only after release closure |
| Human source-family documentation | `docs/domains/archaeology/` and `docs/sources/catalog/` |
| EvidenceBundle, ProofPack, citation validation, integrity proof, or review proof support | `data/proofs/` |
| STAC, DCAT, PROV, discovery records, or public catalog exports | `data/catalog/` |
| RunReceipt, validation receipt, redaction receipt, AI receipt, telemetry receipt, watcher receipt, or correction receipt | `data/receipts/` |
| ReleaseManifest, PromotionDecision, CorrectionNotice, RollbackCard, withdrawal notice, signature, or release changelog | `release/` |
| Policy source, Rego files, source-role rules, cultural-review policy, or access-control rules | `policy/` |
| Semantic contracts and machine schemas | `contracts/` and `schemas/` |
| Connector code, watcher code, packages, fixtures, tests, or CI workflows | `connectors/`, `tools/`, `packages/`, `fixtures/`, `tests/`, `.github/workflows/` |
| Public map/API/UI payloads, graph edges, vector-index content, reports, dashboards, or generated answer text | Governed public outputs only after evidence, policy, validation, review, redaction, release, correction, and rollback gates close |

---

## Validation and maintenance

For this README, validate:

- metadata comment structure and the preserved `doc_id`;
- one H1 and logical heading order;
- relative file and fragment links against the resulting commit;
- tables, alerts, badges, fenced directory map, UTF-8 encoding, and final newline;
- agreement with the child compatibility README and canonical subtype-first README;
- absence of exact locations, protected identifiers, credentials, private endpoints, and restricted cultural information;
- no language that converts a compatibility path into an authority, activation, release, or publication surface.

A passing source-level Markdown check does not prove canonical registry enforcement, SourceDescriptor validity, rights clearance, policy correctness, cultural review, source activation, release readiness, or publication.

Re-review this README when Directory Rules, registry topology, the child compatibility path, the canonical source lane, source contracts/schemas, cultural-review policy, source-authority register, or migration state changes.

---

## Required checks before use

- [ ] Confirm the registry object belongs under the canonical subtype-first source lane rather than this compatibility parent.
- [ ] Confirm no authoritative descriptor, activation decision, source payload, receipt, proof, catalog record, release object, or policy file is being added here.
- [ ] Confirm source identity, publisher or authority, source role, rights, access, sensitivity, cultural review, cadence, and stale-state obligations from current evidence.
- [ ] Confirm exact site, burial, human-remains, sacred-place, private-land, collection-security, or steward-only detail remains excluded.
- [ ] Confirm source role cannot be upgraded by validation, aggregation, modeling, map rendering, graph projection, AI interpretation, or promotion.
- [ ] Confirm public clients and generated-answer surfaces cannot read this parent or its child directly.
- [ ] Confirm any migration preserves identity, aliases, source roles, references, history, correction links, and rollback targets.

---

## Open verification items

| Item | Status |
|---|---:|
| Accountable registry, archaeology, cultural, rights, sensitivity, policy, validation, proof, and release stewards | **NEEDS VERIFICATION** |
| Completeness and enforcement of `control_plane/source_authority_register.yaml` | **NEEDS VERIFICATION** |
| Full schema and validator enforcement for Archaeology source descriptors | **NEEDS VERIFICATION** |
| Runtime, workflow, external, and documentation consumers of this domain-first parent and child | **UNKNOWN** |
| Final migration disposition: tombstone, retained compatibility parent, generated mirror, redirect, or retirement | **PROPOSED / NEEDS VERIFICATION** |
| Physical deletion eligibility | **HOLD** until zero-writer, zero-consumer, link-closure, and retirement evidence exist |

---

## Rollback

Before merge, rollback is closing the draft pull request and leaving the branch unmerged.

After merge, rollback is a transparent revert of the documentation commit. Re-run the metadata, Markdown, link, sensitive-content, and changed-path checks. Do not alter canonical descriptors, source payloads, receipts, proofs, catalogs, policies, release objects, or public artifacts merely to roll back this README.

---

KFM rule: `data/registry/archaeology/` is a compatibility parent for public-safe routing and lineage only. It is not an independent registry writer, source authority, source payload store, evidence authority, policy authority, release authority, protected-location authority, or public Archaeology truth.

[Back to top](#top)
