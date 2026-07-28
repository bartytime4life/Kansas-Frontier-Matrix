<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/agriculture/sources/readme
name: Agriculture Source Registry README
path: data/registry/agriculture/sources/README.md
type: data-registry-domain-sources-readme
version: v0.3.0
status: draft
owners:
  - <source-registry-steward>
  - <agriculture-domain-steward>
  - <rights-reviewer>
  - <policy-steward>
  - <validation-steward>
  - <docs-steward>
created: 2026-06-28
updated: 2026-07-27
policy_label: internal-governance
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: registry
registry_scope: agriculture-source-descriptor-compatibility-view
path_posture: confirmed-live-domain-first-path; conflicted-duplicate-writer-risk; independent-writes-denied; migration-needs-accepted-decision
sensitivity_posture: registry-internal; no-public-path; rights-and-sensitivity-fail-closed; private-farm-and-operator-detail-protected; release-blocked-until-gates-close
related:
  - ../README.md
  - ../../README.md
  - ../../sources/README.md
  - ../../sources/agriculture/README.md
  - ../../source_descriptors/README.md
  - ../../../raw/agriculture/README.md
  - ../../../work/agriculture/README.md
  - ../../../quarantine/agriculture/README.md
  - ../../../processed/agriculture/README.md
  - ../../../receipts/README.md
  - ../../../proofs/README.md
  - ../../../catalog/README.md
  - ../../../../docs/domains/agriculture/SOURCE_REGISTRY.md
  - ../../../../docs/domains/agriculture/SOURCES.md
  - ../../../../docs/domains/agriculture/SENSITIVITY.md
  - ../../../../docs/domains/agriculture/VERIFICATION_BACKLOG.md
  - ../../../../docs/architecture/directory-rules.md
  - ../../../../docs/architecture/source-roles.md
  - ../../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../../docs/registers/SOURCE_AUTHORITY.md
  - ../../../../docs/adr/ADR-0017-source-descriptor-admission-process.md
  - ../../../../control_plane/source_authority_register.yaml
  - ../../../../contracts/source/source_descriptor.md
  - ../../../../schemas/contracts/v1/source/README.md
  - ../../../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../../../policy/domains/agriculture/README.md
  - ../../../../.github/workflows/source-descriptor-validate.yml
tags:
  - kfm
  - data
  - registry
  - agriculture
  - sources
  - compatibility
  - source-descriptor
  - source-role
  - rights
  - sensitivity
  - migration
  - quarantine
  - cite-or-abstain
notes:
  - "This README preserves the stable identity of the existing domain-first Agriculture source-registry path."
  - "Four tracked YAML files in this directory are PROPOSED greenfield templates with unresolved fields; they are not active or schema-conformant SourceDescriptor records."
  - "A separate subtype-first Agriculture lane exists at data/registry/sources/agriculture/ and is the path referenced by current repository consumers and planning documents."
  - "No accepted source-registry topology decision or completed migration was verified. This lane must not evolve as an independent writer."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Agriculture Source Registry

[![Document lifecycle: draft](https://img.shields.io/badge/document-draft-d4a72c?style=flat-square)](#status)
[![Path class: compatibility view](https://img.shields.io/badge/path-compatibility%20view-d4a72c?style=flat-square)](#path-posture)
[![Inventory: 4 proposed templates](https://img.shields.io/badge/inventory-4%20proposed%20templates-6e7781?style=flat-square)](#current-inventory)
[![Independent writer: denied](https://img.shields.io/badge/independent%20writer-denied-b42318?style=flat-square)](#source-descriptor-boundary)
[![Publisher: no](https://img.shields.io/badge/publisher-no-6e7781?style=flat-square)](#lifecycle-and-publication-boundary)

> Domain-first compatibility view for four Agriculture source-descriptor templates. It preserves lineage and makes registry drift visible; it does not admit, activate, validate, release, or publish a source.

> [!CAUTION]
> Do not add or update authoritative SourceDescriptor records in this directory. The repository also contains a subtype-first Agriculture registry lane at [`data/registry/sources/agriculture/`](../../sources/agriculture/README.md), and current governance evidence does not authorize two independent writers. Resolve the topology through an accepted decision and migration before changing descriptor instances.

## Navigation

[Status](#status) · [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Inventory](#current-inventory) · [Boundary](#source-descriptor-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Source families](#source-families) · [Descriptor fields](#suggested-descriptor-fields) · [Activation states](#activation-states) · [Lifecycle](#lifecycle-and-publication-boundary) · [Validation](#validation) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes) · [Rollback](#rollback)

---

## Status

| Field | Current result |
|---|---|
| Repository path | `data/registry/agriculture/sources/` - **CONFIRMED** at the pinned base |
| Document lifecycle | `draft` |
| Path class | **PROPOSED compatibility view / CONFLICTED topology** |
| Tracked local records | Four YAML files, all **PROPOSED greenfield templates** |
| Independent-write posture | **DENY** until registry topology and migration are accepted |
| Source admission or activation | **NOT ESTABLISHED** |
| Direct public access | **DENY** |
| KFM publication effect | None |
| Repository review route | [`/data/registry/` is routed to `@bartytime4life`](../../../../.github/CODEOWNERS); this is review routing, not a verified stewardship assignment |

The detailed [SourceDescriptor schema](../../../../schemas/contracts/v1/source/source_descriptor.schema.json) is itself `PROPOSED`. Its required field set is substantially richer than the four local templates. Shape, admission, policy, review, release, and publication remain separate states.

---

## Scope

This README governs the existing domain-first path and its four tracked YAML templates. Its job is to:

- preserve the path's stable document identity and historical records;
- identify the competing registry homes and prevent parallel authority;
- show exactly what the local files do and do not establish;
- route maintainers to source contracts, schemas, policy, validation, evidence, and release owners;
- define a reversible migration boundary.

This README does not choose a canonical descriptor topology, activate a source, approve rights, assign a source role, clear sensitivity, validate a payload, authorize a connector, close evidence, or approve publication.

---

## Path posture

Three tracked registry shapes are relevant:

| Path | Verified repository state | Bounded posture |
|---|---|---|
| `data/registry/agriculture/sources/` | This README plus four YAML templates | Domain-first path; **CONFLICTED** and treated as a compatibility view with independent writes denied |
| [`data/registry/sources/agriculture/`](../../sources/agriculture/README.md) | README plus fourteen YAML placeholders | Subtype-first Agriculture lane; referenced by current connectors, pipeline documentation, runbooks, release documentation, and domain plans |
| [`data/registry/source_descriptors/`](../../source_descriptors/README.md) | Compatibility README; no Agriculture child was found at the pinned base | Compatibility/routing lane, not a second descriptor authority |

The current [Directory Rules](../../../../docs/architecture/directory-rules.md) place source identity, rights, and sensitivity under `data/registry/` and prohibit parallel homes without an accepted ADR. The repository-grounded [Agriculture configuration README](../../../../configs/domains/agriculture/README.md) explicitly marks the three Agriculture registry patterns as `CONFLICTED`.

[ADR-0017](../../../../docs/adr/ADR-0017-source-descriptor-admission-process.md) identifies `data/registry/sources/` as the intended registry instance root, but its effective decision status remains `proposed`. No accepted topology ADR, migration manifest, redirect, or deprecation record was verified for this domain-first path.

> [!IMPORTANT]
> Path presence is not authority. Until the conflict is resolved, retain the four local templates for lineage, make no independent descriptor edits here, and do not infer activation from either registry lane.

---

## Repo fit

| Responsibility | Owning surface | Relationship to this path |
|---|---|---|
| Registry governance | [`data/registry/README.md`](../../README.md) | Parent authority and lifecycle boundary |
| Agriculture registry parent | [`data/registry/agriculture/README.md`](../README.md) | Documents the domain-first parent and the same topology conflict |
| Source registry | [`data/registry/sources/README.md`](../../sources/README.md) | Source admission and authority-control root |
| Agriculture subtype-first lane | [`data/registry/sources/agriculture/README.md`](../../sources/agriculture/README.md) | Competing descriptor lane and primary current reference target |
| Human source guidance | [`SOURCE_REGISTRY.md`](../../../../docs/domains/agriculture/SOURCE_REGISTRY.md) and [`SOURCES.md`](../../../../docs/domains/agriculture/SOURCES.md) | Narrative source families, rights, cadence, and verification backlog |
| Semantic meaning | [`contracts/source/source_descriptor.md`](../../../../contracts/source/source_descriptor.md) | SourceDescriptor meaning and invariants |
| Machine shape | [`schemas/contracts/v1/source/`](../../../../schemas/contracts/v1/source/README.md) | Detailed proposed schema plus documented schema drift |
| Policy | [`policy/domains/agriculture/`](../../../../policy/domains/agriculture/README.md) | Agriculture admissibility and public-surface decisions |
| Governance register | [`control_plane/source_authority_register.yaml`](../../../../control_plane/source_authority_register.yaml) | Present, `PROPOSED`, and empty at the pinned base |
| Validation workflow | [`source-descriptor-validate.yml`](../../../../.github/workflows/source-descriptor-validate.yml) | Validates the currently wired schema fixtures; explicitly does not scan registry records |
| Payload lifecycle | [RAW](../../../raw/agriculture/README.md), [WORK](../../../work/agriculture/README.md), [QUARANTINE](../../../quarantine/agriculture/README.md), and [PROCESSED](../../../processed/agriculture/README.md) | Source payloads and transforms; never stored in this registry view |
| Evidence and release | [receipts](../../../receipts/README.md), [proofs](../../../proofs/README.md), [catalog](../../../catalog/README.md), and `release/` | Separate process memory, evidence closure, discovery, and release decisions |

---

## Current inventory

The pinned tree contains only this README and four YAML templates:

~~~text
data/registry/agriculture/sources/
├── README.md
├── cropland_data_layer.yaml
├── ksu_extension_ag.yaml
├── nass_quickstats.yaml
└── nrcs_conservation.yaml
~~~

| File | Declared identity | Verified content posture | Admission result |
|---|---|---|---|
| [`cropland_data_layer.yaml`](./cropland_data_layer.yaml) | `cropland_data_layer` | `PROPOSED` greenfield template; role, authority, rights, sensitivity, cadence, access, and citation remain `TBD` | **HOLD / not admitted** |
| [`ksu_extension_ag.yaml`](./ksu_extension_ag.yaml) | `ksu_extension_ag` | Same unresolved template surface | **HOLD / not admitted** |
| [`nass_quickstats.yaml`](./nass_quickstats.yaml) | `nass_quickstats` | Same unresolved template surface; a same-named placeholder also exists in the subtype-first lane | **HOLD / duplicate-path conflict** |
| [`nrcs_conservation.yaml`](./nrcs_conservation.yaml) | `nrcs_conservation` | Same unresolved template surface | **HOLD / not admitted** |

All four files parse as YAML mappings and remain useful for lineage inspection, but they omit multiple fields required by the detailed proposed SourceDescriptor schema. No local file is evidence of current rights, source role, sensitivity, cadence, endpoint access, activation, or public-release eligibility.

---

## Source descriptor boundary

| Rule | Required handling |
|---|---|
| No independent writer | Do not create, update, activate, retire, or supersede descriptor instances in this path before topology resolution. |
| Preserve deterministic identity | A migration must map each legacy `id` to exactly one reviewed canonical `source_id` and disclose collisions. |
| Preserve source role | Modeled, aggregate, administrative, regulatory, candidate, synthetic, restricted, and observed material must not be collapsed. |
| Rights fail closed | `TBD` or unresolved license, terms, attribution, redistribution, access, or sovereignty posture blocks admission and public use. |
| Sensitivity fails closed | Private farm, operator, parcel, facility, compliance, pesticide, livestock, irrigation, and precise operational detail remain restricted unless policy and review explicitly allow a bounded use. |
| Descriptor is not source data | Payloads enter approved RAW or QUARANTINE lanes through governed intake, never this directory. |
| Descriptor is not a decision | Schema-valid shape does not replace source review, policy evaluation, activation, evidence closure, or release. |
| Registry is not catalog, proof, or release | Catalog records, EvidenceBundles, ProofPacks, receipts, release manifests, corrections, and rollback records retain their own authority homes. |
| Public clients do not read this lane | Normal UI and API surfaces use governed interfaces and released public-safe artifacts. |

---

## Accepted material

Until a migration is accepted, this path may contain only:

- this boundary README;
- the four existing greenfield templates retained for lineage;
- pointer-only alias, redirect, or migration notes that reference a single canonical record;
- rollback information for an approved migration;
- a generated view only after its generator, canonical input, digest, edit policy, and regeneration command are verified.

Any future generated view must be one-way and reproducible. Manual edits to generated descriptor copies are denied.

---

## Exclusions

| Do not place here | Owning surface |
|---|---|
| New or independently maintained SourceDescriptor instances | The single registry home chosen by an accepted topology decision and migration |
| Raw source payloads, API responses, imagery, tables, or private operational records | `data/raw/agriculture/` or `data/quarantine/agriculture/` through governed intake |
| Work products or normalized Agriculture records | `data/work/agriculture/` and `data/processed/agriculture/` |
| SourceDescriptor contracts or schemas | `contracts/source/` and `schemas/contracts/v1/source/` |
| Policy rules or decisions | `policy/` |
| Connector, watcher, pipeline, validator, fixture, test, or workflow code | `connectors/`, `pipelines/`, `tools/`, `fixtures/`, `tests/`, or `.github/workflows/` |
| Receipts, EvidenceBundles, proofs, catalog records, release decisions, corrections, or rollback cards | Their governed `data/receipts/`, `data/proofs/`, `data/catalog/`, and `release/` homes |
| Secrets, credentials, signed URLs, private endpoints, or restricted exact locations | Approved secret or restricted storage; never this repository lane |
| Public map, API, graph, vector-index, report, dashboard, or generated-answer payloads | Governed public surfaces after evidence, policy, validation, review, release, correction, and rollback gates close |

---

## Source families

The four local filenames name candidate Agriculture source families, but their provider authority and current terms are unresolved in the files themselves. Human-facing source-family context belongs in [`docs/domains/agriculture/SOURCES.md`](../../../../docs/domains/agriculture/SOURCES.md); machine-adjacent records belong only in the eventual single canonical registry home.

Before any source family is admitted, verify:

1. stable source identity and upstream publisher;
2. one explicit source role and any permitted secondary roles;
3. current rights, terms, attribution, redistribution, and access limits;
4. sensitivity, spatial precision, aggregation, and public-release posture;
5. cadence, retrieval time, valid time, freshness window, and stale behavior;
6. connector/manual intake route and immutable source-head or capture reference;
7. contract, schema, policy, fixture, validator, review, correction, and rollback references.

---

## Suggested descriptor fields

The exact machine shape is owned by the [detailed proposed SourceDescriptor schema](../../../../schemas/contracts/v1/source/source_descriptor.schema.json), not by this README. At the pinned base, that schema requires these field families:

| Field family | Required control |
|---|---|
| Identity and version | `object_type`, `schema_version`, `source_id`, `descriptor_version`, and `title` |
| Classification | `source_type`, `source_role`, `authority_rank`, and publisher/steward identity |
| Rights and sensitivity | Structured `rights` and `sensitivity_default` values |
| Time and access | Structured `cadence`, `access`, and `source_head` values |
| Citation and limits | `citation` and `admissibility_limits` |
| Public and governance state | `public_release`, `review_state`, `release_state`, and `lifecycle` |

The four local templates use a smaller legacy field surface. Their `TBD` values and missing required families are explicit blockers, not invitations to infer defaults.

---

## Activation states

[ADR-0017](../../../../docs/adr/ADR-0017-source-descriptor-admission-process.md) keeps review, registry, connector, release, and public posture in separate fields. Its state model remains **PROPOSED**, but the separation is the safe interim rule:

| State dimension | Proposed schema field | Why it cannot be collapsed |
|---|---|---|
| Human review | `review_state` | Review approval is not connector activation or release. |
| Registry lifecycle | `lifecycle.registry_state` | A registry record may be proposed, active, quarantined, retired, or superseded without implying publication. |
| Connector posture | `connectors.activation_state` | Connector enablement controls intake only. |
| Release posture | `release_state` | Release eligibility and released state remain governed transitions. |
| Public conditions | `public_release` | Public use may still require review, redaction, generalization, or denial. |

No accepted `SourceActivationDecision` machine contract was verified. Do not manufacture activation by selecting a favorable value from one field.

---

## Lifecycle and publication boundary

~~~mermaid
flowchart LR
  VIEW["Domain-first compatibility view<br/>no independent writes"] -. "approved migration or generated pointer" .-> DESC["One canonical SourceDescriptor"]
  DESC --> REVIEW["Identity + role + rights + sensitivity review"]
  REVIEW --> DECISION{"Governed admission decision"}
  DECISION -->|deny or unresolved| HOLD["HOLD / QUARANTINE<br/>no public use"]
  DECISION -->|approved internal intake| RAW["RAW"]
  RAW --> WQ["WORK / QUARANTINE"]
  WQ --> PROC["PROCESSED"]
  PROC --> CAT["CATALOG / TRIPLET"]
  CAT --> RELEASE["Policy + evidence + review + release"]
  RELEASE --> PUB["PUBLISHED<br/>public-safe projection"]
~~~

The diagram shows authority boundaries, not current runtime maturity. The repository's source-descriptor workflow validates a bounded schema/fixture slice and explicitly does not scan registry records, admit sources, activate connectors, or publish.

---

## Validation

### Documentation checks

- one H1, logical heading order, balanced fences, valid tables, supported alerts, and a final newline;
- every relative file, directory, fragment, badge endpoint, and badge destination resolves;
- the KFM Meta Block preserves `doc_id`, `created`, and the same canonical path;
- the diff changes only this README and does not alter descriptor templates;
- the Mermaid flow remains valid and understandable without color;
- no badge or prose claims a source is active, schema-conformant, rights-cleared, public-safe, released, or published.

### Registry checks

| Check | Current result |
|---|---|
| Four local YAML files parse as mappings | **PASS** at the pinned base |
| Four local files identify `domain: agriculture` | **PASS** |
| Required modern SourceDescriptor field families are present | **FAIL / HOLD** - the files are greenfield templates with missing and `TBD` values |
| Unique identity across all registry variants | **PARTIAL** - `nass_quickstats` appears in both Agriculture lanes; broader semantic collisions need migration review |
| Registry-wide descriptor scan in CI | **NOT ESTABLISHED** |
| Populated source authority register | **FAIL / HOLD** - the current register has `entries: []` |
| Source admission runtime | **NOT ESTABLISHED** |

### Workflow interpretation

- [`source-descriptor-validate`](../../../../.github/workflows/source-descriptor-validate.yml) runs on pull requests with read-only repository permission and validates the currently wired proposed schema fixtures.
- The workflow explicitly states that it does not scan registry descriptors or emit admission, activation, policy, review, release, or publication authority.
- Documentation build, link checking, and Agriculture-domain workflows currently expose explicit readiness holds; a green hold is not a rendered-doc, link-validity, domain-readiness, or source-admission result.

---

## Required checks before use

- [ ] An accepted ADR or migration record selects one descriptor instance topology.
- [ ] Every legacy `id` maps deterministically to one canonical `source_id`.
- [ ] Duplicate filenames, source identities, aliases, and source-family overlaps across registry variants are reconciled.
- [ ] Rights, terms, attribution, redistribution, access, and review dates are current and cited.
- [ ] Source role, authority rank, publisher, steward, cadence, source head, citation, and admissibility limits are explicit.
- [ ] Sensitivity and spatial-precision controls cover private operator, field, parcel, facility, compliance, pesticide, livestock, irrigation, and cross-domain join risks.
- [ ] Proposed descriptors validate against the accepted schema with positive and negative fixtures.
- [ ] Policy produces a finite fail-closed result for unresolved rights, sensitivity, stale state, source-role collapse, and public-release requests.
- [ ] Connector and watcher code can reference reviewed registry state but cannot mint or mutate its own authority.
- [ ] EvidenceRef resolves to EvidenceBundle before consequential claims or public layers depend on the source.
- [ ] Release, correction, withdrawal, supersession, and rollback references close before any public surface changes.
- [ ] The compatibility lane is converted to pointers or a reproducible generated view, then protected from manual writes.

---

## Status notes

| Claim | Truth status |
|---|---:|
| This README and four YAML templates exist at the requested path. | **CONFIRMED** |
| All four YAML files declare `PROPOSED - greenfield template` and retain unresolved values. | **CONFIRMED** |
| A separate subtype-first Agriculture lane contains fourteen YAML placeholders. | **CONFIRMED** |
| `nass_quickstats.yaml` exists in both Agriculture registry lanes. | **CONFIRMED / CONFLICTED** |
| Current repository references overwhelmingly point to `data/registry/sources/agriculture/` rather than this path. | **CONFIRMED by bounded repository search** |
| The detailed singular SourceDescriptor schema is `PROPOSED` and richer than these templates. | **CONFIRMED** |
| The source authority register is populated. | **FAIL / empty at the pinned base** |
| An accepted registry-topology ADR or completed migration resolves this path. | **NEEDS VERIFICATION; none found in the inspected ADR and drift surfaces** |
| A runtime writer or consumer uses this domain-first lane. | **UNKNOWN; no direct code or workflow reference found in the bounded search** |
| Any source represented here is active, rights-cleared, policy-approved, released, or public-safe. | **UNKNOWN / do not infer** |
| This README grants public access or KFM publication. | **DENY** |

---

## Review burden and migration

Current [`CODEOWNERS`](../../../../.github/CODEOWNERS) routes `/data/registry/` changes to `@bartytime4life`. That route does not prove a source steward, Agriculture steward, rights reviewer, policy approver, separation of duties, or release authority.

A migration requires review across registry, Agriculture, rights, sensitivity, contracts, schemas, policy, validation, connectors, evidence, release, and documentation responsibilities. At minimum it must:

1. pin both registry inventories and all inbound references;
2. select the canonical instance topology through an accepted decision;
3. map legacy IDs and hashes, surface collisions, and preserve supersession lineage;
4. convert or quarantine records without filling unknown fields by inference;
5. update connectors, runbooks, schemas, validators, tests, and docs atomically where required;
6. leave compatibility pointers or a reproducible generated view;
7. validate the resulting branch and record a rollback target.

This one-file README update performs none of those migration steps.

---

## Evidence basis

| Evidence | What it supports | Limit |
|---|---|---|
| Pinned target tree and file blobs | Exact five-file inventory and template contents | Does not prove operational use |
| [Directory Rules](../../../../docs/architecture/directory-rules.md) | `data/registry/` authority, lifecycle separation, and no-parallel-home rule | Does not settle this nested topology |
| [Agriculture configuration README](../../../../configs/domains/agriculture/README.md) | Explicit three-path registry conflict | Does not authorize migration |
| [Subtype-first Agriculture README](../../sources/agriculture/README.md) and repository references | Competing lane presence and current reference direction | Its YAML files are also placeholders |
| [SourceDescriptor contract](../../../../contracts/source/source_descriptor.md) and [schema](../../../../schemas/contracts/v1/source/source_descriptor.schema.json) | Proposed meaning, required shape, and state separation | Proposal and validation do not equal admission |
| [ADR-0017](../../../../docs/adr/ADR-0017-source-descriptor-admission-process.md) | Proposed admission boundary and current implementation holds | Effective status remains `proposed` |
| [Source authority register](../../../../control_plane/source_authority_register.yaml) | Current proposed register structure | `entries` is empty |
| [Source-descriptor workflow](../../../../.github/workflows/source-descriptor-validate.yml) | Read-only fixture validation and explicit non-publisher boundary | Does not scan registry instances |

---

## Rollback

Before merge, rollback is to close the draft pull request and leave its branch unmerged. After merge, revert the scoped documentation commit; do not rewrite shared history.

Content rollback target: prior README blob `78929cd433a2a7edddb6f5acf01c94cdf9050c95`.

No descriptor YAML, source identity, schema, policy, workflow, activation state, release record, or public artifact is changed by this README update.

---

## Last reviewed

| Field | Value |
|---|---|
| Review date | 2026-07-27 |
| Repository | `bartytime4life/Kansas-Frontier-Matrix` |
| Base ref | `main` |
| Pinned base commit | `0fb6e9a0acb0c1a8e2bdb04f110a6b779d03edb1` |
| Prior README blob | `78929cd433a2a7edddb6f5acf01c94cdf9050c95` |
| Directory Rules blob | `18653c00ba193a4afaa3e07a0924452807fb98ef` |
| Subtype-first Agriculture README blob | `7828ec0b11e73f0caeb6aba6ad3c2d7cdee09ea2` |
| Path overlap at review time | No open pull request found for this target |
| Review trigger | Re-review when registry topology, accepted ADR state, writers/consumers, schema authority, CODEOWNERS, or migration status changes |

---

## Maintainer note

The four local YAML files are governance debt made inspectable, not admitted source authority. Preserve them until a reviewed migration can map identity, rights, role, sensitivity, cadence, references, and hashes without inventing facts.

Keep the chain explicit:

~~~text
legacy template -> reviewed migration -> one canonical SourceDescriptor -> governed admission -> RAW / QUARANTINE -> validation + policy + evidence + review -> release -> public-safe surface
~~~

Never collapse it into:

~~~text
template path -> active source -> Agriculture truth
~~~

<p align="right"><a href="#top">Back to top</a></p>
