<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/archaeology/sources/readme
name: Archaeology Source Registry README
path: data/registry/archaeology/sources/README.md
type: data-registry-domain-sources-readme
version: v0.3.0
status: draft
owners:
  - "NEEDS VERIFICATION: source-registry steward"
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
registry_scope: archaeology-source-descriptor-compatibility-view
path_posture: confirmed-live-domain-first-path; conflicted-duplicate-writer-risk; independent-writes-denied; migration-needs-accepted-decision
sensitivity_posture: restricted-by-default; protected-location-deny-default; cultural-review-required; rights-and-current-terms-required-before-activation; no-public-path; release-blocked-until-redaction-review-release
related:
  - ../README.md
  - ../../README.md
  - ../../sources/README.md
  - ../../sources/archaeology/README.md
  - ../../source_descriptors/README.md
  - ../../../raw/archaeology/README.md
  - ../../../work/archaeology/README.md
  - ../../../quarantine/archaeology/README.md
  - ../../../processed/archaeology/README.md
  - ../../../receipts/README.md
  - ../../../proofs/README.md
  - ../../../catalog/README.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../../docs/domains/archaeology/SOURCE_REGISTRY.md
  - ../../../../docs/domains/archaeology/SOURCES.md
  - ../../../../docs/domains/archaeology/SENSITIVITY.md
  - ../../../../docs/domains/archaeology/PUBLICATION_AND_POLICY.md
  - ../../../../docs/domains/archaeology/VERIFICATION_BACKLOG.md
  - ../../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../../docs/registers/SOURCE_AUTHORITY.md
  - ../../../../control_plane/source_authority_register.yaml
  - ../../../../contracts/source/source_descriptor.md
  - ../../../../schemas/contracts/v1/source/README.md
  - ../../../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../../../policy/domains/archaeology/README.md
  - ../../../../.github/workflows/source-descriptor-validate.yml
tags:
  - kfm
  - data
  - registry
  - archaeology
  - sources
  - compatibility
  - source-descriptor
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
  base_commit: 319788e7282b80ee9646a28ff774eb55b405d296
  prior_blob: 42032fdcee7670628320a2ba5a0951e27536f972
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  adr_0029_blob: cd044a38047cc9b3725d2e083eb201eb86109308
  canonical_lane_blob: 40f859e7b61cec8fb6e27268f2f5b38bcd57bb4f
  parent_blob: d5ab80475accb0fde7077774e3e884c3f99821a0
  inspection_date: 2026-07-27
notes:
  - "This README preserves the stable identity of the existing domain-first Archaeology source-registry path."
  - "The subtype-first lane at data/registry/sources/archaeology/ contains the current SourceDescriptor records and is the canonical lane under adopted Directory Rules v2."
  - "No accepted migration, redirect, or retirement record was verified for this domain-first path. It must not evolve as an independent writer."
  - "This directory is not raw source storage, a site inventory, proof, catalog, release state, policy source, public output, or protected-location authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Archaeology Source Registry

[![Document lifecycle: draft](https://img.shields.io/badge/document-draft-d4a72c?style=flat-square)](#status)
[![Path class: compatibility view](https://img.shields.io/badge/path-compatibility%20view-d4a72c?style=flat-square)](#path-posture)
[![Canonical writer: subtype-first](https://img.shields.io/badge/canonical%20writer-subtype--first-0969da?style=flat-square)](#path-posture)
[![Independent writer: denied](https://img.shields.io/badge/independent%20writer-denied-b42318?style=flat-square)](#source-descriptor-boundary)
[![Protected locations: deny](https://img.shields.io/badge/protected%20locations-deny-b42318?style=flat-square)](#sensitivity-and-publication-boundary)

> Domain-first compatibility view for Archaeology source-registry guidance. It preserves document identity and makes the duplicate-writer risk visible; it does not admit, activate, validate, release, or publish a source.

> [!CAUTION]
> Do not add or update authoritative `SourceDescriptor` records in this directory. Adopted Directory Rules v2 establishes subtype-first placement under `data/registry/sources/<domain>/`, and the populated Archaeology source registry is [`data/registry/sources/archaeology/`](../../sources/archaeology/README.md). This path remains a read-only compatibility boundary until an accepted migration or retirement record says otherwise.

> [!WARNING]
> Archaeology is a sensitive domain. Exact site geometry, sacred or burial-associated locations, human-remains context, private-land detail, collection-security information, and culturally restricted knowledge fail closed. Public availability of a source does not authorize KFM ingestion or disclosure.

## Navigation

[Status](#status) · [Scope](#scope) · [Path posture](#path-posture) · [Repository fit](#repository-fit) · [Current inventory](#current-inventory) · [Boundary](#source-descriptor-boundary) · [Sensitivity](#sensitivity-and-publication-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Validation](#validation-and-maintenance) · [Required checks](#required-checks-before-use) · [Open verification](#open-verification-items) · [Rollback](#rollback)

---

## Status

| Field | Current result |
|---|---|
| Repository path | `data/registry/archaeology/sources/` — **CONFIRMED** at the pinned base |
| Document lifecycle | `draft` |
| README profile | Sensitive `BOUNDARY_COMPACT` compatibility boundary |
| Path class | **Compatibility view / duplicate-writer risk** |
| Canonical source-descriptor writer | [`data/registry/sources/archaeology/`](../../sources/archaeology/README.md) |
| Local descriptor payloads | None confirmed in this path |
| Independent-write posture | **DENY** |
| Source admission or activation | Not established by this README |
| Direct public access | **DENY** |
| KFM publication effect | None |
| Accountable stewardship assignments | **NEEDS VERIFICATION** |

A README, valid YAML, workflow result, commit, pull request, or source URL does not establish source authority, rights clearance, sensitivity clearance, evidence closure, release approval, or publication.

---

## Scope

This README governs the existing domain-first path and preserves its stable document identity while the repository converges on subtype-first registry placement. Its responsibilities are limited to:

- identifying the canonical source-descriptor lane and preventing parallel authority;
- routing maintainers to source contracts, schemas, policy, validation, evidence, and release owners;
- preserving public-safe lineage and compatibility guidance;
- recording the migration, correction, and rollback boundary;
- making unresolved stewardship and enforcement questions visible.

This README does **not** choose or change source roles, approve rights, clear sensitivity, activate connectors, authorize watchers, ingest payloads, establish evidence, approve a release, or publish Archaeology information.

---

## Path posture

Two tracked Archaeology registry shapes are relevant:

| Path | Verified repository state | Bounded posture |
|---|---|---|
| `data/registry/archaeology/sources/` | This README; no descriptor payloads were confirmed in the inspected path | Domain-first compatibility view; independent writes denied |
| [`data/registry/sources/archaeology/`](../../sources/archaeology/README.md) | README, registry YAML files, and source-family descriptor records | Canonical subtype-first source-registry lane under adopted Directory Rules v2 |

Accepted ADR-0029 adopts the exact Directory Rules v2 bytes and makes `docs/doctrine/directory-rules.md` the placement authority. Directory Rules v2 defines the canonical source registry as subtype-first—`data/registry/sources/<source_id or domain lane>/`—and prohibits generated, compatibility, or alternate paths from becoming independent writers.

> [!IMPORTANT]
> Path presence is not authority. Preserve this README until references and consumers are inventoried. Do not move, delete, redirect, or retire the path without an accepted migration record, link closure, rollback plan, and verified consumer handling.

---

## Repository fit

| Responsibility | Owning surface | Relationship to this path |
|---|---|---|
| Registry governance | [`data/registry/README.md`](../../README.md) | Parent responsibility and registry boundary |
| Archaeology domain-first parent | [`data/registry/archaeology/README.md`](../README.md) | Compatibility parent that still documents the older topology conflict |
| Source registry | [`data/registry/sources/README.md`](../../sources/README.md) | Canonical subtype-first source-admission family |
| Archaeology canonical lane | [`data/registry/sources/archaeology/README.md`](../../sources/archaeology/README.md) | Authoritative current writer and descriptor inventory |
| Human source guidance | [`SOURCE_REGISTRY.md`](../../../../docs/domains/archaeology/SOURCE_REGISTRY.md) and [`SOURCES.md`](../../../../docs/domains/archaeology/SOURCES.md) | Human explanation, candidate families, rights, cadence, and review guidance |
| Semantic meaning | [`contracts/source/source_descriptor.md`](../../../../contracts/source/source_descriptor.md) | `SourceDescriptor` meaning and invariants |
| Machine shape | [`schemas/contracts/v1/source/`](../../../../schemas/contracts/v1/source/README.md) | Proposed schema family and compatibility surface |
| Policy | [`policy/domains/archaeology/`](../../../../policy/domains/archaeology/README.md) | Archaeology admissibility, sensitivity, and public-surface decisions |
| Governance register | [`control_plane/source_authority_register.yaml`](../../../../control_plane/source_authority_register.yaml) | Source-authority projection; current completeness needs verification |
| Validation workflow | [`source-descriptor-validate.yml`](../../../../.github/workflows/source-descriptor-validate.yml) | Workflow evidence only; passing checks do not activate or release a source |
| Payload lifecycle | [RAW](../../../raw/archaeology/README.md), [WORK](../../../work/archaeology/README.md), [QUARANTINE](../../../quarantine/archaeology/README.md), and [PROCESSED](../../../processed/archaeology/README.md) | Source payloads and transformations; never stored in this compatibility view |
| Evidence and release | [receipts](../../../receipts/README.md), [proofs](../../../proofs/README.md), [catalog](../../../catalog/README.md), and `release/` | Separate process memory, evidence closure, discovery, release, correction, and rollback authority |

---

## Current inventory

The inspected path confirms only this README. No source descriptor, activation decision, source payload, local index, receipt, proof, catalog record, or release object was established here.

```text
data/registry/archaeology/sources/
└── README.md
```

The canonical subtype-first lane contains the current Archaeology registry files. That inventory must be maintained by its own README and validators rather than duplicated here.

---

## Source descriptor boundary

| Rule | Required handling |
|---|---|
| No independent writer | Do not create, update, activate, retire, or supersede descriptor instances in this path. |
| Preserve deterministic identity | Any migration must map each prior identity to exactly one reviewed canonical `source_id` and disclose collisions. |
| Preserve source role | Observed, regulatory, modeled, aggregate, administrative, candidate, synthetic, contextual, and restricted roles must not be collapsed. |
| Rights fail closed | Unknown license, terms, attribution, redistribution, access, consent, revocation, or sovereignty posture blocks admission and public use. |
| Sensitivity fails closed | Protected sites and culturally restricted knowledge require denial, quarantine, restriction, redaction, generalization, or steward review. |
| Descriptor is not source data | Payloads enter approved RAW or QUARANTINE lanes through governed intake, never this directory. |
| Descriptor is not a decision | Schema-valid shape does not replace source review, policy evaluation, activation, evidence closure, or release. |
| Watchers are non-publishers | Source-health and drift checks may emit candidates and receipts; they cannot activate a source or publish data. |
| Registry is not catalog, proof, or release | Catalog records, EvidenceBundles, ProofPacks, receipts, release manifests, corrections, and rollback records retain separate authority homes. |
| Public clients do not read this lane | Normal API, map, search, graph, export, and AI surfaces use governed interfaces and released public-safe artifacts. |

---

## Sensitivity and publication boundary

A source may be public while the Archaeology use remains restricted. Every downstream use must preserve source role, rights, cultural authority, spatial precision, valid time, review state, and release state.

| Risk | Required posture |
|---|---|
| Exact archaeological geometry, identifiers, or precise provenience | Do not expose in public-readable registry files, fixtures, indexes, maps, search, vector stores, exports, or generated responses. |
| Burial sites, human remains, funerary objects, sacred places, or culturally restricted knowledge | Fail closed; require cultural/steward review, rights and sovereignty posture, access limits, transformation receipts, evidence, review, release, correction, and rollback. |
| Looting, vandalism, collection-security, or site-condition exposure | Treat as restricted even when upstream material is partly public. Avoid joins that make protected locations discoverable. |
| Private-landowner or access details | Minimize and restrict; public use requires explicit purpose, rights, policy, review, and transformation evidence. |
| Candidate anomalies and predictive surfaces | Preserve `candidate` or `modeled` role; never relabel as confirmed archaeology. |
| Historic maps and georeferenced records | Preserve source vintage and georeference uncertainty; proximity does not prove a site. |
| Cross-domain joins | Review joins with roads, settlements, people/land, infrastructure, hydrology, geology, habitat, flora, fauna, and hazards before release. |

A source descriptor, source activation decision, or policy result alone is not publication authority. Public Archaeology outputs require the applicable EvidenceBundle, sensitivity transform, redaction or generalization receipt, review record, release manifest, correction path, and rollback target.

---

## Accepted material

Until a migration or retirement is accepted, this path may contain only:

- this boundary README;
- pointer-only alias, redirect, or migration notes that reference the single canonical lane;
- consumer and reference inventories needed for migration;
- rollback information for an approved migration;
- a generated view only after its canonical input, generator, digest, edit policy, and regeneration command are verified.

Any generated view must be one-way, reproducible, and no more permissive than the canonical source. Manual edits to generated descriptor copies are denied.

---

## Exclusions

| Do not place here | Owning surface |
|---|---|
| New or independently maintained `SourceDescriptor` instances | [`data/registry/sources/archaeology/`](../../sources/archaeology/README.md) |
| Raw reports, scans, imagery, LiDAR, geophysics, tables, shapefiles, GeoJSON, GeoParquet, COG, PMTiles, or API responses | `data/raw/archaeology/` or `data/quarantine/archaeology/` through governed intake |
| Work products or normalized Archaeology objects | `data/work/archaeology/` and `data/processed/archaeology/` |
| Exact locations, sacred knowledge, burial or human-remains detail, collection-security information, or private-land detail | Approved restricted storage with policy-governed pointers; never public-readable Git content |
| Source contracts, schemas, or policy | `contracts/source/`, `schemas/contracts/v1/source/`, and `policy/` |
| Run, validation, watcher, redaction, aggregation, AI, correction, or rollback receipts | `data/receipts/` |
| EvidenceBundles, ProofPacks, citation validation, review proof, or integrity proof | `data/proofs/` |
| STAC, DCAT, PROV, discovery records, or public catalog exports | `data/catalog/` |
| Release manifests, promotion decisions, corrections, withdrawals, rollback cards, or signatures | `release/` |
| Connector, watcher, package, fixture, test, or workflow implementation | `connectors/`, `tools/`, `packages/`, `fixtures/`, `tests/`, and `.github/workflows/` |
| Public API, map, search, graph, vector-index, report, dashboard, story, or AI payload | Governed released outputs only after all applicable gates close |

---

## Validation and maintenance

Validate this README and its connected documentation surface without implying source or publication maturity.

Required source-level checks:

- KFM meta block parses and preserves `doc_id`, path, creation date, and draft lifecycle;
- exactly one H1 and logical heading order;
- all local links and fragments resolve at the branch head;
- badge destinations resolve and their text matches the documented posture;
- tables and alert syntax remain valid GitHub Markdown;
- no sensitive coordinates, site identifiers, access details, credentials, private endpoints, or restricted source content appear;
- no descriptor instance or generated copy was added to this compatibility path;
- the base-to-head diff contains only this README.

Repository workflows and validators may provide additional evidence, but a green result proves only their declared checks. It does not establish rights, sensitivity clearance, cultural approval, source activation, evidence closure, release, or publication.

Re-review this README when the registry topology, Directory Rules, source contracts or schemas, canonical Archaeology lane, source-authority register, CODEOWNERS, migration state, or public-safety posture changes.

---

## Required checks before use

- [ ] Confirm this path is being used only as a compatibility boundary.
- [ ] Add and change authoritative descriptors only in the accepted canonical lane.
- [ ] Confirm source identity, authority, source role, access method, rights, attribution, redistribution, consent, revocation, cadence, freshness, and stale-state behavior.
- [ ] Confirm cultural, sovereignty, sensitivity, protected-location, and stewardship review requirements.
- [ ] Confirm schemas, validators, policies, receipts, proof requirements, catalog expectations, release gates, correction references, and rollback targets.
- [ ] Confirm no credentials, restricted identifiers, exact locations, sensitive joins, or source payloads enter public-readable registry material.
- [ ] Confirm public clients and generated-answer surfaces cannot read this lane directly.
- [ ] Before any migration or retirement, inventory inbound links, runtime consumers, scripts, fixtures, workflows, and external references.

---

## Open verification items

- **NEEDS VERIFICATION:** accountable registry, archaeology, cultural-review, rights, sensitivity, policy, validation, proof, and release stewards.
- **NEEDS VERIFICATION:** completeness and enforcement of the source-authority register and SourceDescriptor schema.
- **NEEDS VERIFICATION:** runtime, connector, watcher, pipeline, and UI consumers of either registry topology.
- **NEEDS VERIFICATION:** whether this path should become a tombstone, generated mirror, or retained compatibility README.
- **UNKNOWN:** external consumers or bookmarks not visible through repository search.

---

## Rollback

This change modifies documentation only.

Before merge, close the draft pull request and leave the branch unmerged. After merge, revert the implementation commit to restore the prior README, then re-run the same Markdown, link, sensitive-content, and changed-path checks.

Rollback of this README must not delete, move, activate, deactivate, or rewrite any source descriptor, source payload, receipt, proof, catalog record, policy decision, release object, correction, or rollback record.

---

KFM rule: this path is a compatibility boundary, not an independent source registry, public source catalogue, evidence store, policy surface, release authority, or Archaeology truth source.

[Back to top](#top)
