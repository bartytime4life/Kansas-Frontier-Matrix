<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/atmosphere/readme
name: Atmosphere Registry README
path: data/registry/atmosphere/README.md
type: data-registry-domain-parent-readme
version: v0.1.0
status: draft; compatibility-boundary; no-independent-registry-record-writes
owners: NEEDS VERIFICATION
updated: 2026-07-27
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: registry
registry_scope: atmosphere-domain-registry-compatibility-parent
path_posture: confirmed-live-domain-first-parent; subtype-first-registry-authority; independent-registry-record-writes-denied
safety_posture: no-direct-public-path; no-source-activation; no-advisory-or-health-authority; fail-closed; release-gated
related:
  - ../README.md
  - sources/README.md
  - ../sources/README.md
  - ../sources/atmosphere/README.md
  - ../../raw/atmosphere/README.md
  - ../../work/atmosphere/README.md
  - ../../quarantine/atmosphere/README.md
  - ../../processed/atmosphere/README.md
  - ../../receipts/atmosphere/README.md
  - ../../proofs/atmosphere/README.md
  - ../../catalog/domain/atmosphere/README.md
  - ../../published/atmosphere/README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../docs/domains/atmosphere/SOURCE_REGISTRY.md
  - ../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../control_plane/source_authority_register.yaml
  - ../../../contracts/source/source_descriptor.md
  - ../../../schemas/contracts/v1/source/README.md
  - ../../../policy/domains/atmosphere/README.md
  - ../../../.github/workflows/source-descriptor-validate.yml
tags:
  - kfm
  - data
  - registry
  - atmosphere
  - compatibility
  - subtype-first
  - source-role
  - rights
  - sensitivity
  - freshness
  - cite-or-abstain
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_commit: dfa211df5ae68fa9cdf0c2ca774e61191b9b85a0
  prior_blob: 430ae68984de65ff46d8b3a2a838da8cdd4efaa1
  child_compatibility_blob: 6ac6a74530599be6fc74a64645e886cf7d0c0edd
  canonical_source_lane_blob: 6a50dd496225cd9e4c3165dead10cde3d0f23959
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  adr_0029_blob: cd044a38047cc9b3725d2e083eb201eb86109308
  inspection_date: 2026-07-27
notes:
  - "This README replaces the two-line greenfield stub at the same path."
  - "Accepted Directory Rules v2 makes subtype-first registry placement canonical."
  - "The child data/registry/atmosphere/sources/ path is a no-independent-write compatibility view."
  - "No accepted migration, generator, parity check, active consumer, or retirement record was verified for this parent."
  - "Registry presence does not activate a source, prove an Atmosphere claim, authorize operational guidance, release data, or publish KFM content."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Atmosphere Registry

[![Document lifecycle: draft](https://img.shields.io/badge/document-draft-d4a72c?style=flat-square)](#status)
[![Path class: compatibility parent](https://img.shields.io/badge/path-compatibility%20parent-d4a72c?style=flat-square)](#authority-and-path-posture)
[![Registry authority: subtype first](https://img.shields.io/badge/registry%20authority-subtype--first-0969da?style=flat-square)](#authority-and-path-posture)
[![Independent writes: denied](https://img.shields.io/badge/independent%20writes-denied-b42318?style=flat-square)](#registry-boundary)
[![Public or operational use: denied](https://img.shields.io/badge/public%20or%20operational%20use-denied-b42318?style=flat-square)](#atmosphere-safety-boundary)

> **One-line purpose.** Preserve the existing domain-first Atmosphere registry path as a bounded navigation and compatibility parent while authoritative registry records remain in their accepted subtype-first families.

> [!CAUTION]
> Do not add authoritative source descriptors, activation decisions, dataset or layer identities, rights or sensitivity decisions, payloads, or public-facing Atmosphere data here. This path does not establish current conditions, regulatory status, health guidance, emergency direction, release approval, or KFM publication.

**Navigation:** [Status](#status) · [Purpose](#purpose) · [Authority](#authority-and-path-posture) · [Repository fit](#repository-fit) · [Children](#confirmed-child-lanes) · [Boundary](#registry-boundary) · [Safety](#atmosphere-safety-boundary) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs/outputs](#inputs-and-outputs) · [Validation](#validation-and-maintenance) · [Verification](#open-verification) · [Rollback](#correction-migration-and-rollback)

## Status

| Surface | Evidence-backed state |
|---|---|
| Target path | **CONFIRMED** at the pinned base; prior content was `Greenfield stub.` |
| Document lifecycle | `draft` |
| Responsibility | Registry-domain compatibility and navigation only |
| Governing Directory Rules | **CONFIRMED adopted** through [ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) |
| Registry placement | Subtype-first is canonical under `DIR-SOURCE-003` and the registry topology in `DIR-SOURCE-004` |
| Confirmed local child | [`sources/`](sources/README.md), a no-independent-write compatibility view |
| Canonical Atmosphere source lane | [`data/registry/sources/atmosphere/`](../sources/atmosphere/README.md) |
| Records inspected in that source lane | Two JSON files explicitly marked `PROPOSED`; neither establishes active admission |
| Source-authority register | **CONFIRMED present**, `PROPOSED`, and empty at the pinned base |
| Other direct children, generated views, writers, and consumers | **NEEDS VERIFICATION** |
| Public, operational, advisory, or health use | **DENY BY DEFAULT** |

Path presence, a Markdown file, schema-valid bytes, a workflow result, a commit, a pull request, or a merge does not establish source authority, rights clearance, policy admission, evidence closure, release approval, or publication.

## Purpose

This README governs the existing domain-first parent:

```text
data/registry/atmosphere/
```

Its bounded responsibilities are to:

- preserve the path's stable navigation identity while registry topology converges;
- route maintainers to the canonical subtype-first registry family for the object being governed;
- make the child source compatibility boundary and canonical source writer explicit;
- prevent this parent from becoming a parallel Atmosphere registry authority;
- preserve correction, migration, supersession, and rollback requirements;
- keep Atmosphere source-role, rights, sensitivity, time, units, quality, and public-safety boundaries visible.

This README does not define registry object semantics, machine shape, policy, source activation, connector behavior, lifecycle promotion, evidence, catalog closure, release, or public delivery.

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

The topology is sparse and evidence-driven. It does not authorize every family or an Atmosphere child merely because the domain exists.

| Path shape | Bounded posture |
|---|---|
| `data/registry/<subtype>/...` | Canonical registry-family placement when the relevant record and authority are accepted |
| `data/registry/atmosphere/` | Existing domain-first compatibility parent; navigation and migration boundary only |
| [`data/registry/atmosphere/sources/`](sources/README.md) | Read-only compatibility view; independent source-descriptor writes denied |
| [`data/registry/sources/atmosphere/`](../sources/atmosphere/README.md) | Current subtype-first Atmosphere source-registry lane; current records remain draft or proposed until separately accepted |

`DIR-SOURCE-003` places machine source identities and descriptors under `data/registry/sources/`. `DIR-SOURCE-004` permits a domain-first `sources/` path only as a generated view, not an independent writer, when the subtype-first record is canonical.

> [!IMPORTANT]
> Preserve this parent until its writers, readers, links, aliases, and external consumers are inventoried. Do not delete, redirect, repurpose, or promote it without an accepted migration decision, reference closure, parity evidence where applicable, and a rollback target.

## Repository fit

| Responsibility | Owning surface | Relationship to this path |
|---|---|---|
| Registry governance | [`data/registry/README.md`](../README.md) | Parent registry responsibility boundary |
| Canonical source family | [`data/registry/sources/README.md`](../sources/README.md) | Subtype-first source admission and routing family |
| Atmosphere source lane | [`data/registry/sources/atmosphere/`](../sources/atmosphere/README.md) | Canonical placement for Atmosphere source records; current content remains draft/proposed |
| Domain-first source view | [`sources/`](sources/README.md) | Compatibility navigation; no independent descriptor writes |
| Human source guidance | [Atmosphere Source Registry](../../../docs/domains/atmosphere/SOURCE_REGISTRY.md) and [Source Descriptor Standard](../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md) | Draft guidance and admission discipline; not runtime or release proof |
| Semantic meaning | [`contracts/source/source_descriptor.md`](../../../contracts/source/source_descriptor.md) | `SourceDescriptor` meaning and invariants |
| Machine shape | [`schemas/contracts/v1/source/`](../../../schemas/contracts/v1/source/README.md) | Source schema family; acceptance and path reconciliation remain separate |
| Policy | [`policy/domains/atmosphere/`](../../../policy/domains/atmosphere/README.md) | Domain policy boundary; a registry file cannot make a policy decision |
| Governance projection | [`control_plane/source_authority_register.yaml`](../../../control_plane/source_authority_register.yaml) | Proposed source-authority projection; empty at the pinned base |
| Validation workflow | [`source-descriptor-validate.yml`](../../../.github/workflows/source-descriptor-validate.yml) | Read-only workflow evidence; a passing check cannot activate or release a source |
| Payload lifecycle | [RAW](../../raw/atmosphere/README.md), [WORK](../../work/atmosphere/README.md), [QUARANTINE](../../quarantine/atmosphere/README.md), and [PROCESSED](../../processed/atmosphere/README.md) | Atmosphere material and transformations; never stored in this parent |
| Process and evidence support | [Receipts](../../receipts/atmosphere/README.md) and [proofs](../../proofs/atmosphere/README.md) | Separate process-memory and evidence-support families |
| Discovery and delivery | [Catalog](../../catalog/domain/atmosphere/README.md) and [published carriers](../../published/atmosphere/README.md) | Downstream surfaces; neither inherits authority from this registry parent |

## Confirmed child lanes

The bounded inspection confirmed this local structure:

```text
data/registry/atmosphere/
├── README.md
└── sources/
    └── README.md
```

| Child | Confirmed role | Boundary |
|---|---|---|
| [`sources/`](sources/README.md) | Human-readable compatibility view for readers entering through the Atmosphere domain | Not an independent writer, activation lane, payload store, policy source, proof, release record, or public data service |

This map is not a complete recursive-tree claim. It confirms the files inspected for this change; other children, aliases, generated outputs, and external consumers remain **NEEDS VERIFICATION**.

Do not create empty domain-first registry families to make this parent look complete. A new registry object must first resolve its subtype, canonical identity, contract, schema, policy, writer, consumers, review burden, migration behavior, and rollback path.

## Registry boundary

| Rule | Required handling |
|---|---|
| No parallel authority | Do not create authoritative registry records under this parent when a subtype-first family owns the object |
| One canonical identity | Register a source or other governed identity once; derived views must carry the canonical ID |
| Read-only views | Generate from canonical inputs, record input/output digests, and verify parity; do not maintain copies by hand |
| Preserve source role | Do not upgrade modeled, aggregate, administrative, candidate, contextual, restricted, or preliminary material into observed or regulatory truth |
| Rights and sensitivity fail closed | Unknown terms, attribution, redistribution, access, privacy, precision, or security posture blocks activation and public use |
| Time remains explicit | Preserve observation, issue, valid, effective, retrieval, model-run, forecast, revision, expiration, and stale-state distinctions |
| Registry is not payload | Source material enters governed RAW or QUARANTINE intake; it does not live here |
| Registry is not proof or policy | A record may point to evidence and decisions but cannot replace them |
| Watchers do not publish | Drift and freshness checks may propose work or emit process memory; they cannot activate, release, or publish |
| Public clients do not read this parent | APIs, maps, dashboards, graph/vector indexes, exports, and AI surfaces use governed released interfaces |

## Atmosphere safety boundary

Atmosphere records are especially vulnerable to source-role, unit, spatial, and time collapse. Registry routing must preserve the distinctions below without asserting that any source is active.

| Material class | Preserve | Never infer from registry presence |
|---|---|---|
| Regulatory monitoring or archives | parameter, units, method, averaging interval, QA, station/network, revision, and time scope | current conditions, compliance determination, or release permission |
| Public AQI, smoke, or advisory context | issuing authority, issue/valid/expiration time, stale state, caveats, and official-source routing | health advice, emergency instruction, timeless current truth, or raw concentration |
| Weather stations and mesonets | station/sensor identity, siting, units, QA, observation time, and missing/stale markers | universal quality assurance or unrestricted public reuse |
| Forecast, reanalysis, or smoke-model fields | model/version, run time, forecast hour, valid time, inputs, uncertainty, and validation scope | an observation or authoritative advisory |
| Satellite aerosol, smoke, fire, or cloud-adjacent products | product/algorithm identity, resolution, QA, footprint, acquisition time, and limitations | direct ground-level concentration or exposure |
| Low-cost, community, research, or local networks | calibration, correction, confidence, ownership, rights, method, and review posture | regulatory equivalence |
| Climate normals, anomalies, and aggregates | baseline period, method, scale, uncertainty, aggregation unit, and revision state | a station-level event or current condition |

Consequential public claims require EvidenceRef resolution to an appropriate EvidenceBundle, policy and sensitivity evaluation, review and release state, citation, correction path, and rollback support. AI-generated language remains interpretive and evidence-subordinate.

## What belongs here

Until an accepted migration or retirement decision changes the path, accepted content is limited to:

- this boundary README;
- the existing child compatibility README;
- pointer-only alias, redirect, migration, or tombstone notes that resolve to one canonical subtype-first identity;
- public-safe rollback and supersession metadata for an approved migration;
- a deterministic generated navigation index only after its canonical inputs, generator, owner, edit policy, digests, parity check, consumers, rollback, and exit criteria are verified;
- explicit verification items that do not activate, ingest, promote, release, or publish.

## What does not belong here

| Do not place or maintain here | Owning surface or required action |
|---|---|
| New or independently maintained source descriptors | Accepted subtype-first source registry, currently [`data/registry/sources/atmosphere/`](../sources/atmosphere/README.md) |
| Dataset, layer, domain, rights, sensitivity, or crosswalk records written as domain-first authority | Resolve the accepted subtype-first family and migration decision first |
| Observations, station series, grids, rasters, model runs, satellite products, advisories, API responses, or downloaded files | Governed RAW, WORK, QUARANTINE, or PROCESSED Atmosphere lanes |
| Contracts or schemas | `contracts/` and `schemas/` |
| Rights, sensitivity, stale-state, access, public-health, advisory, or release policy | `policy/` |
| Receipts, proofs, catalogs, release decisions, correction notices, rollback cards, or published carriers | Their separate responsibility roots |
| Connector, watcher, pipeline, package, validator, fixture, test, API, map, dashboard, graph, or AI implementation | The applicable implementation responsibility root |
| Credentials, tokens, signed URLs, private endpoints, restricted operational details, or unsafe precision | Approved secret or restricted storage; never ordinary public-repository content |

## Inputs and outputs

| Direction | Accepted surface | Boundary |
|---|---|---|
| Input | Canonical registry identities and subtype-family records | Must resolve to one accepted writer or remain unavailable |
| Input | Contracts, schemas, policies, rights, sensitivity, role, time, scope, evidence, review, correction, and rollback references | A link does not prove acceptance or execution |
| Input | Accepted migration record and canonical-to-compatibility mapping | Required before any generated or redirect behavior |
| Output | Human navigation to canonical registry and governance surfaces | Read-only and non-authoritative |
| Output | Optional deterministic compatibility projection | Requires generator, digests, parity validation, consumer inventory, and rollback |
| Output | Structured hold or verification item | Must not activate a source, admit payloads, approve policy, release, or publish |

This parent has no normal public API, UI, map, alert, health-guidance, or generated-answer contract.

## Validation and maintenance

Before changing this README or adding any compatibility material:

- verify the pinned base, accepted Directory Rules, ADR-0029, parent registry contract, child compatibility README, and canonical subtype-first target;
- inventory direct children, authoritative writers, readers, references, aliases, generated markers, and external consumers;
- confirm the record belongs to a verified subtype-first family and does not mint a competing ID;
- preserve source role, rights, sensitivity, access, time/freshness, units, quality, uncertainty, spatial scope, citation, correction, supersession, and rollback fields;
- verify generated views against canonical input/output digests and fail closed on missing, ambiguous, stale, restricted, or inconsistent records;
- verify Markdown structure, metadata, one H1, headings, anchors, links, badges, alerts, tables, code fences, UTF-8 encoding, and final newline;
- verify no payload, secret, private endpoint, restricted operational information, misleading health/advisory statement, or public-serving path is introduced.

The repository's `source-descriptor-validate` workflow exercises bounded source-schema and fixture behavior with read-only repository permission. Its success does not prove registry topology, source activation, rights clearance, public safety, evidence closure, release readiness, or publication.

The repository's link-check workflow is an explicit readiness hold and does not currently validate repository or external links. Manual link-resolution evidence for this README remains documentation QA only.

## Open verification

| Item | Status | Evidence required |
|---|---|---|
| Complete direct-child and recursive inventory | `NEEDS VERIFICATION` | Pinned tree, file classifications, LFS/external-store review, and generated markers |
| Active writers and consumers | `UNKNOWN` | Connector, pipeline, tool, workflow, runtime, API/UI, and external-consumer inventory |
| Canonical families for any non-source Atmosphere registry records | `NEEDS VERIFICATION` | Accepted subtype taxonomy, IDs, contracts, schemas, writers, and migrations |
| Compatibility generator and parity check | `NOT VERIFIED` | Repository-owned generator, deterministic fixtures, tests, digests, and failure behavior |
| Source activation state | `UNKNOWN` | Reviewed source-authority entries and activation decisions |
| Rights, sensitivity, freshness, correction, and rollback enforcement | `UNKNOWN` | Policy, negative fixtures, validator outputs, receipts, and drills |
| Accountable stewardship | `NEEDS VERIFICATION` | Approved responsibility assignments; CODEOWNERS is routing only |
| Public or operational consumers | `UNKNOWN` | Governed route, release, access, cache, invalidation, correction, and rollback evidence |

Unknowns narrow behavior and block higher-authority claims; they do not authorize plausible defaults.

## Correction, migration, and rollback

1. Correct the canonical subtype-first record or governing authority first.
2. Emit the required correction, supersession, withdrawal, deactivation, review, or release record through its owning process.
3. Regenerate any admitted compatibility view from corrected canonical inputs.
4. Invalidate stale view bytes and re-establish parity before consumers resume.
5. Preserve old-to-new identity mapping, consumer handling, effective time, and rollback target.
6. If safe regeneration or migration cannot be proven, retain this README-only compatibility boundary and fail closed.

Before merge, rollback is the prior blob `430ae68984de65ff46d8b3a2a838da8cdd4efaa1` on the scoped branch. After merge, use a transparent revert or follow-up pull request; do not restore independent registry-record writes here.

## Related authority

| Reference | Role |
|---|---|
| [Directory Rules v2](../../../docs/doctrine/directory-rules.md) | Adopted placement doctrine; see `DIR-SOURCE-003`, `DIR-SOURCE-004`, and subtype-first registry placement |
| [ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Adopts the exact Directory Rules v2 bytes and establishes single-write doctrine authority |
| [`data/registry/`](../README.md) | Parent registry responsibility boundary |
| [Canonical source registry](../sources/README.md) | Source-family parent; current README maturity does not elevate placeholder records |
| [Atmosphere source lane](../sources/atmosphere/README.md) | Subtype-first Atmosphere source-registry surface |
| [Domain-first source view](sources/README.md) | No-independent-write compatibility boundary |
| [Source Descriptor Standard](../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md) | Draft human guidance for source identity, role, rights, sensitivity, cadence, and citation |
| [SourceDescriptor contract](../../../contracts/source/source_descriptor.md) | Draft semantic contract and anti-collapse rules |
| [Source-authority register](../../../control_plane/source_authority_register.yaml) | Proposed machine projection; empty at the pinned base |

## Change history

### v0.1.0 — 2026-07-27

- replaced the two-line greenfield stub with a governed Atmosphere registry parent boundary;
- aligned the path with accepted subtype-first registry placement and ADR-0029;
- documented the child compatibility view and canonical source writer without creating parallel authority;
- added Atmosphere source-role, time/freshness, rights, sensitivity, correction, rollback, and public-safety controls;
- added evidence-backed badges, navigation, repository-fit mappings, validation, and open verification.

[Back to top](#top)
