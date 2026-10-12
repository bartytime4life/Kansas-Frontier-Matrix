<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/fauna/readme
name: Fauna Registry README
path: data/registry/fauna/README.md
type: data-registry-fauna-parent-readme
version: v0.3.0
status: draft; compatibility-boundary; no-independent-registry-record-writes
owners:
  - "NEEDS VERIFICATION: registry steward"
  - "NEEDS VERIFICATION: fauna domain steward"
  - "NEEDS VERIFICATION: rights, sensitivity, and geoprivacy reviewers"
  - "NEEDS VERIFICATION: source, dataset, domain, and crosswalk stewards"
  - "NEEDS VERIFICATION: policy, validation, proof, and release stewards"
created: 2026-06-28
updated: 2026-07-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: registry
registry_scope: fauna-domain-registry-compatibility-parent
domain: fauna
path_posture: confirmed-live-domain-first-parent; subtype-first-registry-authority; independent-registry-record-writes-denied; migration-needs-accepted-decision
sensitivity_posture: registry-internal; no-public-path; deny-by-default-sensitive-sites; source-role-preserving; rights-and-sensitivity-fail-closed; release-gated
related:
  - ../README.md
  - sources/README.md
  - ../sources/README.md
  - ../sources/fauna/README.md
  - ../datasets/README.md
  - ../domains/README.md
  - ../crosswalks/README.md
  - ../../raw/fauna/README.md
  - ../../work/fauna/README.md
  - ../../quarantine/fauna/README.md
  - ../../processed/fauna/README.md
  - ../../receipts/README.md
  - ../../proofs/fauna/README.md
  - ../../catalog/domain/fauna/README.md
  - ../../published/fauna/README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../docs/domains/fauna/SOURCE_REGISTRY.md
  - ../../../docs/domains/fauna/SOURCE_ROLES.md
  - ../../../docs/domains/fauna/SOURCE_FAMILIES.md
  - ../../../docs/domains/fauna/SENSITIVITY.md
  - ../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../control_plane/source_authority_register.yaml
  - ../../../contracts/domains/fauna/README.md
  - ../../../schemas/contracts/v1/source/README.md
  - ../../../schemas/contracts/v1/domains/fauna/README.md
  - ../../../policy/domains/fauna/README.md
  - ../../../policy/sensitivity/fauna/README.md
  - ../../../.github/workflows/domain-fauna.yml
  - ../../../release/candidates/fauna/README.md
tags:
  - kfm
  - data
  - registry
  - fauna
  - compatibility
  - subtype-first
  - source-role
  - rights
  - sensitivity
  - geoprivacy
  - correction
  - rollback
  - cite-or-abstain
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_commit: 61a2d67e2b246cb291a6ada771811b1472b270e0
  prior_blob: 2ef450acffc92bfd0e5740e757435704a6a5570a
  child_compatibility_blob: 4f1daf93ade8fc65025159a48b53149399730273
  canonical_source_lane_blob: c3a36f721b445ae41d2d9407f7b3524872ed1128
  registry_parent_blob: b327d22956f5454482a35dbf265f45b901c1f2a3
  source_registry_parent_blob: 2821e9681273bff6b430920d0a45312c5643ba33
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  adr_0029_blob: cd044a38047cc9b3725d2e083eb201eb86109308
  source_authority_register_blob: 82c23722520922f5ca0dad7f37ed794d1c2edf81
  domain_fauna_workflow_blob: 85b0a8b42f9af40366de2b0c7d733892d4220ee0
  inspection_date: 2026-07-28
notes:
  - "This README preserves the stable identity of the existing domain-first Fauna registry parent path."
  - "Adopted Directory Rules v2 makes subtype-first registry placement canonical."
  - "The child data/registry/fauna/sources/ path is a no-independent-write compatibility view."
  - "The canonical source lane data/registry/sources/fauna/ is present, but no concrete descriptor inventory was established in the inspected scope."
  - "The source-authority register is PROPOSED and empty; no active Fauna source admission is established by that register."
  - "Registry presence does not prove an animal observation, clear rights or sensitivity, authorize release, or publish KFM content."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Fauna Registry

[![Document lifecycle: draft](https://img.shields.io/badge/document-draft-d4a72c?style=flat-square)](#status)
[![Path class: compatibility parent](https://img.shields.io/badge/path-compatibility%20parent-d4a72c?style=flat-square)](#path-posture)
[![Registry authority: subtype first](https://img.shields.io/badge/registry%20authority-subtype--first-0969da?style=flat-square)](#path-posture)
[![Independent writes: denied](https://img.shields.io/badge/independent%20writes-denied-b42318?style=flat-square)](#fauna-registry-boundary)
[![Sensitive sites: fail closed](https://img.shields.io/badge/sensitive%20sites-fail%20closed-b42318?style=flat-square)](#fauna-safety-and-publication-boundary)

> **One-line purpose.** Preserve the existing domain-first Fauna registry path as a bounded navigation and compatibility parent while authoritative registry records remain in their accepted subtype-first families.

> [!CAUTION]
> Do not add authoritative source descriptors, activation decisions, dataset identities, crosswalk records, domain-state records, payloads, proofs, policies, releases, or public-facing Fauna data under this parent. Source-descriptor writes belong under [`data/registry/sources/fauna/`](../sources/fauna/README.md); the local [`sources/`](sources/README.md) child is a no-independent-write compatibility view.

> [!WARNING]
> Fauna is a sensitive domain. Exact occurrences, nests, dens, roosts, hibernacula, spawning or breeding sites, telemetry detail, eDNA detail, disease or mortality detail, private identifiers, and steward-controlled records fail closed. Public upstream availability does not authorize KFM ingestion, joining, mapping, indexing, AI use, or disclosure.

**Navigation:** [Status](#status) · [Scope](#scope) · [Path posture](#path-posture) · [Repository fit](#repo-fit) · [Children](#confirmed-child-lanes) · [Boundary](#fauna-registry-boundary) · [Safety](#fauna-safety-and-publication-boundary) · [Belongs](#accepted-material) · [Exclusions](#exclusions) · [Inputs/outputs](#inputs-and-outputs) · [Validation](#validation-and-maintenance) · [Checks](#required-checks-before-use) · [Verification](#status-notes) · [Rollback](#correction-migration-and-rollback)

## Status

| Surface | Evidence-backed state |
|---|---|
| Target path | **CONFIRMED** at `main@61a2d67e2b246cb291a6ada771811b1472b270e0` |
| Document lifecycle | `draft` |
| README profile | Sensitive `BOUNDARY_COMPACT` compatibility parent |
| Responsibility | Registry-domain compatibility and navigation only |
| Governing Directory Rules | **CONFIRMED adopted** through [ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) |
| Registry placement | Subtype-first is canonical under `DIR-SOURCE-003` and `DIR-SOURCE-004` |
| Confirmed local child | [`sources/`](sources/README.md), a no-independent-write compatibility view |
| Canonical Fauna source lane | [`data/registry/sources/fauna/`](../sources/fauna/README.md) |
| Concrete canonical descriptor inventory | **UNKNOWN** in the inspected scope; repository search found the README only |
| Source-authority register | **CONFIRMED present**, `PROPOSED`, and empty at the pinned base |
| Fauna workflow evidence | One accepted synthetic, no-network fixture-safety slice; no source-admission, proof, release, or publication authority |
| Independent registry-record writes here | **DENY** |
| Direct public access | **DENY** |
| KFM publication effect | None |
| Accountable stewardship assignments | **NEEDS VERIFICATION** |

A path, README, schema-valid record, passing fixture, workflow result, commit, pull request, or merge does not establish animal truth, source authority, rights clearance, geoprivacy clearance, evidence closure, release approval, or publication.

<a id="scope"></a>

## Scope

This README governs the existing domain-first parent:

```text
data/registry/fauna/
```

Its bounded responsibilities are to:

- preserve the path's stable navigation identity while registry topology converges;
- route maintainers to the canonical subtype-first registry family for the object being governed;
- make the child source compatibility boundary and canonical source writer explicit;
- prevent this parent from becoming a parallel Fauna registry hierarchy;
- preserve correction, migration, supersession, withdrawal, and rollback requirements;
- keep Fauna source-role, rights, sensitivity, geoprivacy, temporal, spatial, and public-safety boundaries visible.

This README does not define registry-object semantics, machine shape, policy, source activation, connector behavior, lifecycle promotion, evidence, catalog closure, release, or public delivery.

<a id="path-posture"></a>

## Authority and path posture

Accepted Directory Rules v2 establishes subtype-first registry placement:

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

The topology is sparse and evidence-driven. It does not authorize every family or a Fauna child merely because the domain exists.

| Path shape | Verified repository state | Bounded posture |
|---|---|---|
| `data/registry/fauna/` | This parent README and the `sources/` child | Domain-first compatibility parent; independent registry-record writes denied |
| [`data/registry/fauna/sources/`](sources/README.md) | Compatibility README | Read-only navigation view under `DIR-SOURCE-004`; no independent source-descriptor writes |
| [`data/registry/sources/fauna/`](../sources/fauna/README.md) | Canonical-lane README; no concrete descriptor files confirmed in bounded search | Canonical subtype-first placement for Fauna source records under `DIR-SOURCE-003`; admission remains unverified |
| [`data/registry/datasets/`](../datasets/README.md) | Registry-family parent | Dataset identity records only; does not arise automatically under this domain parent |
| [`data/registry/domains/`](../domains/README.md) | Registry-family parent | Domain-state records only; do not duplicate them here |
| [`data/registry/crosswalks/`](../crosswalks/README.md) | Registry-family parent | Mapping-state records only; do not duplicate them here |

`DIR-SOURCE-003` places machine source identities and descriptors under `data/registry/sources/`. `DIR-SOURCE-004` permits `data/registry/<domain>/sources/` only as a generated view when the subtype-first record is canonical; it may not act as an independent writer.

> [!IMPORTANT]
> Preserve this parent until its writers, readers, links, aliases, generated views, and external consumers are inventoried. Do not delete, redirect, repurpose, promote, or retire it without an accepted migration decision, reference closure, parity evidence where applicable, and a rollback target.

<a id="repo-fit"></a>

## Repository fit

| Responsibility | Owning surface | Relationship to this path |
|---|---|---|
| Registry governance | [`data/registry/README.md`](../README.md) | Parent registry responsibility boundary |
| Canonical source family | [`data/registry/sources/README.md`](../sources/README.md) | Subtype-first source admission and routing family |
| Fauna source lane | [`data/registry/sources/fauna/`](../sources/fauna/README.md) | Canonical placement for Fauna source records; concrete inventory and active admission remain unverified |
| Domain-first source view | [`sources/`](sources/README.md) | Compatibility navigation; no independent descriptor writes |
| Dataset registry | [`data/registry/datasets/`](../datasets/README.md) | Dataset identity and state, separate from source identity |
| Domain registry | [`data/registry/domains/`](../domains/README.md) | Domain-state records, separate from source and dataset identity |
| Crosswalk registry | [`data/registry/crosswalks/`](../crosswalks/README.md) | Mapping-state claims, separate from source and domain truth |
| Human source guidance | [Fauna Source Registry](../../../docs/domains/fauna/SOURCE_REGISTRY.md), [Source Roles](../../../docs/domains/fauna/SOURCE_ROLES.md), [Source Families](../../../docs/domains/fauna/SOURCE_FAMILIES.md), and [Sensitivity](../../../docs/domains/fauna/SENSITIVITY.md) | Draft guidance and admission discipline; not runtime or release proof |
| Semantic meaning | [`contracts/domains/fauna/`](../../../contracts/domains/fauna/README.md) and source contracts | Domain and source meaning; a registry README cannot amend contracts |
| Machine shape | [Source schemas](../../../schemas/contracts/v1/source/README.md) and [Fauna schemas](../../../schemas/contracts/v1/domains/fauna/README.md) | Machine shape; accepted schema pairing and registry-wide enforcement need verification |
| Policy and geoprivacy | [Fauna policy](../../../policy/domains/fauna/README.md) and [Fauna sensitivity policy](../../../policy/sensitivity/fauna/README.md) | Allow, deny, restrict, generalize, redact, or hold decisions; registry state cannot make them |
| Governance projection | [`control_plane/source_authority_register.yaml`](../../../control_plane/source_authority_register.yaml) | `PROPOSED` source-authority projection; empty at the pinned base |
| Fauna workflow | [`domain-fauna.yml`](../../../.github/workflows/domain-fauna.yml) | Runs a bounded synthetic fixture-safety suite; proof and release remain explicit holds |
| Payload lifecycle | [RAW](../../raw/fauna/README.md), [WORK](../../work/fauna/README.md), [QUARANTINE](../../quarantine/fauna/README.md), and [PROCESSED](../../processed/fauna/README.md) | Fauna source and derived bytes; never stored in this parent |
| Process and evidence support | [Receipts](../../receipts/README.md), [Fauna proofs](../../proofs/fauna/README.md), and [Fauna catalog](../../catalog/domain/fauna/README.md) | Separate process-memory, evidence-support, and projection families |
| Candidate and public delivery | [Fauna candidate lane](../../../release/candidates/fauna/README.md) and [published Fauna](../../published/fauna/README.md) | Downstream surfaces; neither inherits authority from this registry parent |
| Public consumers | Governed APIs and release-approved carriers | Must not read registry internals directly |

<a id="suggested-directory-shape"></a>
<a id="confirmed-child-lanes"></a>

## Confirmed child lanes

The bounded inspection confirms this local structure:

```text
data/registry/fauna/
├── README.md
└── sources/
    └── README.md
```

| Child | Confirmed role | Boundary |
|---|---|---|
| [`sources/`](sources/README.md) | Human-readable compatibility view for readers entering through the Fauna domain | Not an independent writer, activation lane, payload store, proof, catalog, policy, release record, or public data service |

This direct-child map does not authorize additional domain-first registry families or claim that any payload exists. Do not create empty dataset, domain, crosswalk, rights, sensitivity, or layer children merely to make this parent look complete.

<a id="fauna-registry-boundary"></a>

## Fauna registry boundary

| Rule | Required handling |
|---|---|
| No parallel authority | Do not create authoritative registry records under this parent when a subtype-first family owns the object |
| One canonical identity | Register a source, dataset, domain, layer, right, sensitivity rule, or crosswalk once; derived views carry the canonical ID |
| Read-only compatibility views | Generate from canonical inputs, record input/output digests, verify parity, and prohibit manual copies |
| Preserve source role | Do not upgrade observed, regulatory, modeled, aggregate, administrative, candidate, synthetic, contextual, or restricted material through registry routing |
| Preserve origin behind aggregators | Access through GBIF, eBird, iNaturalist, iDigBio, BISON-like systems, or another aggregator does not erase the originating institution, observer, specimen, survey, model, or record role |
| Rights and sensitivity fail closed | Unknown terms, attribution, redistribution, access, embargo, consent, precision, or stewardship posture blocks activation and public use |
| Time remains explicit | Preserve observation, collection, retrieval, revision, expiration, correction, supersession, withdrawal, and stale-state distinctions |
| Registry is not payload | Fauna material enters governed RAW or QUARANTINE intake; it does not live here |
| Registry is not proof or policy | Registry records may reference evidence and decisions but cannot replace them |
| Watchers do not publish | Drift and freshness checks may propose work or emit receipts; they cannot activate, release, or publish |
| Public clients do not read this parent | APIs, maps, dashboards, graph/vector indexes, exports, and AI surfaces use governed released interfaces |

<a id="fauna-safety-and-publication-boundary"></a>

## Fauna safety and publication boundary

A source may be public while its Fauna use remains restricted. Registry routing must preserve source role, rights, taxonomic scope, spatial precision, temporal scope, uncertainty, review state, and release state.

| Material class | Preserve | Never infer from registry presence |
|---|---|---|
| Occurrence, observation, specimen, or survey records | originating provider, basis of record, taxon assertion, observation/collection time, precision, uncertainty, geoprivacy, rights, and review state | confirmed identity outside recorded scope, public-safe exact location, population status, or unrestricted reuse |
| Telemetry, nests, dens, roosts, hibernacula, spawning/breeding sites, eDNA, disease, or mortality records | steward controls, embargo, method, precision, access tier, temporal window, and disclosure risk | public eligibility, exact-location permission, management advice, or legal status |
| Aggregator-mediated records | aggregator path plus original provider, institution, observer, specimen, dataset, and source role | that aggregation creates regulatory, observed, or canonical authority |
| Modeled habitat, range, occupancy, movement, or candidate surfaces | model/version, run time, inputs, scale, method, uncertainty, validation, and source role | direct observation, current presence, breeding confirmation, or release permission |
| Regulatory, conservation-status, harvest, permit, or administrative records | issuing authority, jurisdiction, effective time, scope, revision state, and source role | occurrence truth, abundance truth, public exact-location permission, or timeless current status |
| Context sources such as habitat, hydrology, soil, land cover, roads, or settlements | context role, scale, time, uncertainty, and join purpose | animal occurrence or taxonomic truth |
| Released public summaries | release identity, aggregation/generalization method, evidence references, caveats, correction lineage, and rollback target | permission to reverse-engineer protected sites or reuse internal registry state |

Cross-domain joins require review before release, especially joins that could reconstruct protected locations or expose stewardship, private-land, infrastructure, disease, or collection-security information.

Publication remains downstream of evidence resolution, rights and sensitivity policy, geoprivacy transformation, review, validation receipts, proof/catalog closure, release manifests, correction paths, and rollback targets. A registry record cannot authorize publication.

<a id="accepted-material"></a>

## What belongs here

Until a migration or retirement decision is accepted, this parent may contain only:

- this boundary README;
- the existing [`sources/README.md`](sources/README.md) compatibility child;
- pointer-only alias, redirect, or migration notes that reference one canonical record;
- public-safe correction and rollback information for an approved migration;
- a generated compatibility index only after its generator, canonical inputs, source/output digests, edit policy, parity check, expiry, and regeneration command are verified.

Manual creation of new authoritative registry records or new domain-first registry families is denied.

<a id="exclusions"></a>

## What does not belong here

| Do not place here | Owning surface |
|---|---|
| New or independently maintained `SourceDescriptor` instances | [`data/registry/sources/fauna/`](../sources/fauna/README.md), subject to contracts, schemas, policy, and review |
| Dataset identities, domain-state records, or crosswalk mapping records | `data/registry/datasets/`, `data/registry/domains/`, or `data/registry/crosswalks/` |
| Raw Fauna datasets, occurrence downloads, telemetry, acoustic/eDNA data, disease or mortality reports, rasters, vectors, models, specimens, or API responses | `data/raw/fauna/`, `data/work/fauna/`, or `data/quarantine/fauna/` according to admission and sensitivity state |
| Exact sensitive coordinates, nests, dens, roosts, hibernacula, spawning or breeding sites, telemetry detail, private identifiers, or steward-only notes | Approved restricted storage and governed lifecycle lanes only |
| Processed Fauna objects or public-safe derivatives | `data/processed/fauna/` after validation; `data/published/fauna/` only after release closure |
| Human bibliography or source-family narratives | `docs/domains/fauna/` and `docs/sources/` |
| EvidenceBundle, ProofPack, citation validation, integrity proof, or review proof | `data/proofs/` |
| STAC, DCAT, PROV, domain catalog, graph, or triplet projections | `data/catalog/` and accepted triplet lanes |
| RunReceipt, validation receipt, redaction/generalization receipt, AI receipt, telemetry receipt, watcher receipt, or correction receipt | `data/receipts/` |
| ReleaseManifest, PromotionDecision, CorrectionNotice, WithdrawalNotice, RollbackCard, signature, or release changelog | `release/` |
| Policy, rights, sensitivity, geoprivacy, source-role, access-control, or release rules | `policy/` |
| Semantic contracts and machine schemas | `contracts/` and `schemas/` |
| Connector, watcher, resolver, validator, pipeline, fixture, test, or workflow code | `connectors/`, `tools/`, `packages/`, `pipelines/`, `fixtures/`, `tests/`, and `.github/workflows/` |
| Public map/API/UI payloads, search or vector-index content, dashboards, reports, alerts, or generated answers | Governed released outputs only after evidence, policy, validation, review, transformation, release, correction, and rollback gates close |

## Inputs and outputs

| Direction | Accepted surface | Boundary |
|---|---|---|
| Input | Canonical registry identities, roles, rights, sensitivity, cadence, scope, correction, supersession, and rollback metadata | Must resolve from an accepted record or remain explicitly unavailable |
| Input | Contract, schema, policy, fixture, validator, receipt, proof, catalog, and release references | A reference does not prove acceptance, execution, or release |
| Output | Human navigation to canonical registry families | Read-only and non-authoritative |
| Output | Optional generated compatibility view | Requires one-way generation, parity evidence, and rollback |
| Output | Structured hold, migration, or verification item | Must not activate, ingest, promote, release, or publish |

Public clients and ordinary AI/UI surfaces must not read this parent or its compatibility child as a data service.

## Validation and maintenance

For this README, validate:

- metadata-comment structure, preserved `doc_id`, version, and evidence snapshot;
- one H1 and logical heading order;
- relative file and fragment links against the resulting commit;
- tables, alerts, badges, fenced direct-child map, UTF-8 encoding, and final newline;
- agreement with the child compatibility README and canonical subtype-first README;
- absence of exact locations, protected identifiers, credentials, private endpoints, and steward-only information;
- no language that converts compatibility placement, schema validity, a green fixture suite, or a workflow result into source admission, evidence, policy, release, or publication authority.

The current [`domain-fauna`](../../../.github/workflows/domain-fauna.yml) workflow runs a bounded synthetic, no-network fixture-safety suite. It does not validate registry records, admit sources, resolve taxonomy, construct evidence, apply geoprivacy policy, build proof, approve release, or publish. Its proof and release jobs remain explicit holds.

A passing source-level Markdown check does not prove canonical registry enforcement, descriptor validity, rights clearance, geoprivacy review, policy correctness, source activation, proof closure, release readiness, or public safety.

Re-review this README when Directory Rules, registry topology, the child compatibility path, the canonical source lane, source contracts/schemas, Fauna policy, source-authority register, fixture scope, or migration state changes.

<a id="required-checks-before-use"></a>

## Required checks before use

- [ ] Confirm the registry object belongs under the applicable canonical subtype-first family rather than this compatibility parent.
- [ ] Confirm no authoritative descriptor, dataset identity, domain-state record, crosswalk, activation decision, payload, receipt, proof, catalog record, release object, or policy file is being added here.
- [ ] Confirm source identity, originating provider, source role, rights, access, sensitivity, geoprivacy, cadence, spatial precision, taxonomic scope, and stale-state obligations from current evidence.
- [ ] Confirm exact occurrences, nests, dens, roosts, hibernacula, spawning/breeding sites, telemetry, eDNA, disease, mortality, private identifiers, and steward-only details remain excluded.
- [ ] Confirm source role cannot be upgraded by aggregation, validation, modeling, crosswalking, map rendering, graph projection, AI interpretation, or promotion.
- [ ] Confirm aggregator access does not erase origin, provider, institution, specimen, observer, survey, or source-role lineage.
- [ ] Confirm public clients and generated-answer surfaces cannot read this parent or its child directly.
- [ ] Confirm any migration preserves identity, aliases, source roles, references, history, corrections, withdrawals, and rollback targets.

<a id="status-notes"></a>

## Status notes and open verification

| Item | Status |
|---|---:|
| Accountable registry, fauna, source, dataset, crosswalk, rights, sensitivity, geoprivacy, policy, validation, proof, and release stewards | **NEEDS VERIFICATION** |
| Completeness and enforcement of `control_plane/source_authority_register.yaml` | **NEEDS VERIFICATION**; current register is `PROPOSED` and empty |
| Concrete descriptor inventory under `data/registry/sources/fauna/` | **UNKNOWN** in bounded search |
| Modernization and accepted-state alignment of the canonical Fauna source README | **NEEDS VERIFICATION**; it predates Directory Rules v2 adoption |
| Full source-schema, Fauna-schema, policy, fixture, and validator enforcement | **NEEDS VERIFICATION** |
| Writers, readers, generated views, workflows, runtime consumers, and external consumers of this domain-first parent and child | **UNKNOWN** |
| View generator and parity check | **NOT VERIFIED** |
| Final migration disposition: retained compatibility parent, generated mirror, redirect/tombstone, or retirement | **PROPOSED / NEEDS VERIFICATION** |
| Physical deletion eligibility | **HOLD** until zero-writer, zero-consumer, link-closure, parity/retirement, and rollback evidence exist |

Unknowns narrow behavior and block higher-authority claims; they do not authorize plausible defaults.

## Correction, migration, and rollback

1. Correct the canonical registry record or governing authority first.
2. Emit the required correction, supersession, withdrawal, deactivation, review, or rollback record through its owning process.
3. Regenerate any admitted compatibility view from corrected canonical inputs.
4. Invalidate stale view bytes and verify parity before consumers resume.
5. If a view cannot be regenerated safely, remove the derived view while retaining this no-write README or an approved tombstone.

Before merge, rollback is closing the draft pull request and leaving the branch unmerged. After merge, use a transparent revert or follow-up pull request; do not restore independent registry-record writes under this parent.

## Change history

### v0.3.0 — 2026-07-28

- aligned the parent with adopted Directory Rules v2 and the merged child compatibility view;
- reclassified the domain-first path as a no-independent-write compatibility parent;
- directed source-descriptor writes to the subtype-first Fauna source lane;
- removed speculative domain-first registry expansion and pseudo-completeness;
- added current evidence, workflow scope, validation, open verification, migration, correction, and rollback controls;
- preserved source-role, rights, sensitivity, geoprivacy, public-boundary, and cite-or-abstain posture.

### v0.2.0 — 2026-06-28

- replaced the greenfield stub with a detailed Fauna registry boundary;
- recorded the then-unresolved domain-first versus subtype-first topology.

<a id="maintainer-note"></a>

KFM rule: `data/registry/fauna/` is a compatibility parent for public-safe navigation and lineage only. It is not an independent registry writer, source authority, payload store, evidence authority, policy authority, release authority, sensitive-location authority, or public Fauna truth.

[Back to top](#top)
