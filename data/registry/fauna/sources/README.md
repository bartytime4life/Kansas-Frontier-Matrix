<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/fauna/sources/readme
name: Fauna Source Registry Compatibility README
path: data/registry/fauna/sources/README.md
type: data-registry-domain-source-compatibility-readme
version: v0.3.0
status: draft; compatibility-boundary; no-independent-writes
owners: NEEDS_VERIFICATION
created: 2026-06-28
updated: 2026-07-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: registry
registry_scope: fauna-source-navigation-view
domain: fauna
path_posture: domain-first compatibility view; subtype-first registry authority; descriptor writes denied here
safety_posture: no-direct-public-path; no-source-activation; deny-by-default-sensitive-sites; fail-closed
related:
  - ../../README.md
  - ../README.md
  - ../../sources/README.md
  - ../../sources/fauna/README.md
  - ../../../raw/fauna/README.md
  - ../../../work/fauna/README.md
  - ../../../quarantine/fauna/README.md
  - ../../../processed/fauna/README.md
  - ../../../receipts/README.md
  - ../../../proofs/fauna/README.md
  - ../../../catalog/domain/fauna/README.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../../docs/domains/fauna/SOURCE_REGISTRY.md
  - ../../../../docs/domains/fauna/SOURCE_ROLES.md
  - ../../../../docs/domains/fauna/SOURCE_FAMILIES.md
  - ../../../../docs/domains/fauna/SENSITIVITY.md
  - ../../../../control_plane/source_authority_register.yaml
  - ../../../../fixtures/domains/fauna/README.md
  - ../../../../schemas/contracts/v1/source/README.md
  - ../../../../schemas/contracts/v1/sources/README.md
  - ../../../../schemas/contracts/v1/domains/fauna/README.md
  - ../../../../contracts/domains/fauna/README.md
  - ../../../../policy/domains/fauna/README.md
  - ../../../../policy/sensitivity/fauna/README.md
  - ../../../../release/README.md
tags:
  - kfm
  - data
  - registry
  - fauna
  - sources
  - compatibility
  - generated-view
  - source-role
  - rights
  - sensitivity
  - geoprivacy
  - evidence
  - correction
  - rollback
  - cite-or-abstain
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_commit: d37b32235ed66ea1995bde69277d5d4ccb471ade
  prior_blob: 59db6ee65734cdb4bc7711c0618bd6245841a2bb
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  adr_0029_blob: cd044a38047cc9b3725d2e083eb201eb86109308
  canonical_fauna_readme_blob: c3a36f721b445ae41d2d9407f7b3524872ed1128
  source_descriptor_standard_blob: 4327c603f76e5b5a76fa058fe24ac2af91e496d8
  fauna_source_registry_doc_blob: 49aeff08ecec1bb52af7ffbfebc1faaf83eed097
  source_authority_register_blob: 82c23722520922f5ca0dad7f37ed794d1c2edf81
  inspection_date: 2026-07-28
notes:
  - "ADR-0029 adopted Directory Rules v2 at docs/doctrine/directory-rules.md."
  - "Directory Rules DIR-SOURCE-003 and DIR-SOURCE-004 make the subtype-first source registry authoritative and prohibit this domain-first path from acting as an independent writer."
  - "The canonical Fauna source README is present but predates Directory Rules v2 adoption and still describes topology as unresolved."
  - "The source-authority register is PROPOSED and contains no entries; no active Fauna source admission is established by that register."
  - "No generator, parity check, active writer, active consumer, or concrete canonical Fauna descriptor inventory was verified for this path."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>
<a id="fauna-source-registry"></a>

# Fauna Source Registry Compatibility View

[![Status: compatibility boundary](https://img.shields.io/badge/status-compatibility%20boundary-f59e0b?style=flat-square)](#status)
[![Writes: denied](https://img.shields.io/badge/writes-denied-b91c1c?style=flat-square)](#write-contract)
[![Sensitivity: fail closed](https://img.shields.io/badge/sensitivity-fail%20closed-b42318?style=flat-square)](#fauna-source-boundary)
[![Truth: cite or abstain](https://img.shields.io/badge/truth-cite%20or%20abstain-1a7f37?style=flat-square)](../../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md)

> **One-line purpose.** Preserve a safe, human-readable Fauna source navigation path while source identity and descriptor writes remain under the subtype-first registry authority.

> [!CAUTION]
> Do not add or edit source descriptors, activation decisions, source payloads, credentials, exact sensitive locations, or public-facing data here. This path does not activate a source, prove an animal claim, grant rights, clear sensitivity, authorize release, or publish KFM content.

**Navigation:** [Purpose](#purpose) · [Status](#status) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Write contract](#write-contract) · [View contract](#view-contract) · [Fauna controls](#fauna-source-boundary) · [Validation](#validation) · [Related authority](#related-authority) · [Open verification](#open-verification)

<a id="scope"></a>

## Purpose

This README governs the existing domain-first path:

```text
data/registry/fauna/sources/
```

Its bounded role is navigation and migration compatibility for readers approaching source governance from the Fauna domain lane. It may identify or link to Fauna-related source records, but it must not become a second registry writer.

The authoritative responsibility remains registry identity and routing, not animal observations, occurrence payloads, status determinations, telemetry, evidence, policy, catalog closure, release, or public delivery.

<a id="status-notes"></a>

## Status

| Surface | Evidence-backed state |
|---|---|
| This README path | **CONFIRMED** at the pinned repository base |
| Governing Directory Rules | **CONFIRMED adopted** through [ADR-0029](../../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) |
| Domain-first source path | **Compatibility/generated-view posture** under `DIR-SOURCE-004` |
| Subtype-first source registry | **Canonical placement rule** under `DIR-SOURCE-003` |
| Canonical Fauna source README | **CONFIRMED present** at [`data/registry/sources/fauna/`](../../sources/fauna/README.md); its topology text predates adoption |
| Concrete canonical Fauna descriptor inventory | **UNKNOWN** in the inspected scope |
| Source-authority register | **CONFIRMED `PROPOSED` and empty**; no active source admission established |
| Generator and parity validation for this view | **NEEDS VERIFICATION** |
| Active writers and consumers of this exact path | **UNKNOWN** |
| Accountable owner and CODEOWNERS routing | **NEEDS VERIFICATION** |
| Public readiness | **DENY BY DEFAULT** |

> [!IMPORTANT]
> Repository presence is not activation. A README, proposed schema, empty register, source-family document, connector, workflow, commit, pull request, or merge does not establish an admitted source, accepted descriptor, rights clearance, sensitivity clearance, evidence closure, release, or public-safe output.

<a id="path-posture"></a>

## Path posture and authority decision

The accepted Directory Rules separate the two path shapes:

| Concern | Governing home | This path's relation |
|---|---|---|
| Machine source identities and descriptors | `data/registry/sources/` | May point to them; must not duplicate or mutate them |
| Human source guidance | `docs/sources/` and Fauna domain documentation | May summarize boundaries and link outward |
| Connector implementation | `connectors/` | No executable or activation authority here |
| Source payloads | `data/raw/`, `data/work/`, or `data/quarantine/` as governed | Payloads are prohibited here |
| Validation evidence and process memory | `data/proofs/` and `data/receipts/` | References only |
| Release decisions and public-safe carriers | `release/` and `data/published/` | No release or publication authority here |

**Placement result for source-descriptor records:** `DENY` independent writes here. A one-way generated navigation view may be `MIRROR` only after its canonical inputs, generator, owner, source and output digests, parity check, consumers, rollback, and exit criteria are verified.

This README remains at the requested path to preserve navigation and make the no-write boundary explicit. It does not resolve source-ID grammar, schema-path drift, producer and consumer inventory, or the migration status of every existing registry artifact.

<a id="suggested-directory-shape"></a>
<a id="suggested-descriptor-shape"></a>

### Retired local sketches

Earlier versions proposed a domain-local child tree and illustrative descriptor JSON. Those sketches are removed because they could become parallel structure or vocabulary. Use the canonical subtype-first registry, paired contract and schema authority, and accepted migration records instead. Exact descriptor shape and implementation maturity remain open verification items.

## Repo fit

| Responsibility | Owning surface | Boundary |
|---|---|---|
| Registry parent | [`data/registry/`](../../README.md) | Registry identity and routing; not lifecycle payload storage |
| Canonical source parent | [`data/registry/sources/`](../../sources/README.md) | Machine source identity and descriptor placement |
| Canonical Fauna source lane | [`data/registry/sources/fauna/`](../../sources/fauna/README.md) | Fauna source-registry surface; record inventory and accepted implementation remain unverified |
| Domain-first Fauna registry parent | [`data/registry/fauna/`](../README.md) | Compatibility and navigation parent; no parallel source authority |
| Source semantics and Fauna guidance | [Source Descriptor Standard](../../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md) and [Fauna Source Registry](../../../../docs/domains/fauna/SOURCE_REGISTRY.md) | Draft human guidance; not descriptor storage or activation |
| Contracts and schemas | [Fauna contracts](../../../../contracts/domains/fauna/README.md), [source schemas](../../../../schemas/contracts/v1/source/README.md), [sources compatibility schemas](../../../../schemas/contracts/v1/sources/README.md), and [Fauna schemas](../../../../schemas/contracts/v1/domains/fauna/README.md) | Meaning and machine shape remain separate; source schema path drift is unresolved |
| Policy and sensitivity | [Fauna policy](../../../../policy/domains/fauna/README.md) and [Fauna sensitivity policy](../../../../policy/sensitivity/fauna/README.md) | Current files are proposed scaffolds; binding enforcement is not inferred |
| Lifecycle payloads | [RAW](../../../raw/fauna/README.md), [WORK](../../../work/fauna/README.md), [QUARANTINE](../../../quarantine/fauna/README.md), and [PROCESSED](../../../processed/fauna/README.md) | Actual source and derived bytes; never stored here |
| Receipts, proofs, and catalog | [Receipts](../../../receipts/README.md), [Fauna proofs](../../../proofs/fauna/README.md), and [Fauna catalog](../../../catalog/domain/fauna/README.md) | Process memory, evidence support, and projections; none is source registry authority |
| Release decisions | [`release/`](../../../../release/README.md) | Promotion, correction, withdrawal, supersession, and rollback authority |
| Public surfaces | Governed APIs and release-approved carriers | Public clients do not read this compatibility path as data |

<a id="accepted-material"></a>

## Write contract

### Allowed

- this compatibility README;
- a verified, generated, read-only index whose entries resolve to canonical subtype-first records;
- migration or tombstone metadata required by an accepted migration;
- parity, source digest, generation, expiry, and rollback metadata that cannot be mistaken for source admission;
- links to canonical contracts, schemas, policies, fixtures, tests, receipts, proofs, catalogs, correction records, rollback targets, and release decisions.

## Exclusions

| Do not place or maintain here | Required handling |
|---|---|
| `SourceDescriptor` records | Write only through the accepted subtype-first registry topology |
| Source-intake or source-activation decisions | Use the accepted control, receipt, or decision process; do not invent a registry-local decision store |
| Occurrence downloads, telemetry, acoustic or eDNA data, mortality or disease reports, rasters, vectors, models, specimen payloads, or source-native files | Route through RAW, WORK, or QUARANTINE according to admission and sensitivity state |
| Manually copied source indexes | Generate from canonical records with parity validation or do not create |
| Exact sensitive occurrences, nests, dens, roosts, hibernacula, spawning or breeding sites, telemetry detail, private identifiers, or steward-only notes | Keep in approved restricted storage and governed lifecycle lanes; fail closed |
| Rights, sensitivity, geoprivacy, stale-state, access, or release policy | Keep normative rules under `policy/` |
| Contracts or machine schemas | Keep meaning under `contracts/` and shape under `schemas/` |
| Receipts, proofs, catalog records, release records, or published carriers | Use each owning object-family lane |
| Credentials, tokens, signed URLs, private endpoints, or restricted operational details | Use approved secret or restricted storage; never commit here |
| Public API, map, dashboard, alert, compliance, or AI output | Use governed released interfaces; cite or abstain |

## View contract

If a generated Fauna view is later implemented, every row must derive from a canonical source record and remain strictly less authoritative than that record.

| Required view property | Minimum behavior |
|---|---|
| Stable identity | Carry the canonical `source_id`; do not mint a domain-local ID |
| Source location | Link to the canonical record or governed resolver |
| Role preservation | Carry the exact canonical role; do not infer or upgrade a role locally |
| Provider and provenance | Preserve original publisher, contributing institution, record origin, and aggregation path where applicable |
| Rights and sensitivity | Surface unresolved or restrictive posture without upgrading it |
| Spatial precision | Preserve precision, generalization, obscuration, embargo, and steward restrictions without exposing protected detail |
| Time and freshness | Preserve source, observation, retrieval, revision, expiration, correction, and stale-state distinctions when material |
| Scope and uncertainty | Preserve taxon, method, geography, sampling, model, aggregation, confidence, and claim limits |
| Change lineage | Carry correction, supersession, withdrawal, deactivation, and rollback references |
| Generation evidence | Record canonical input digest, generator version, output digest, generated time, parity result, and rollback target |

The view must fail closed when a canonical record is missing, ambiguous, stale beyond its declared use, rights- or sensitivity-unresolved, unsupported by its declared role, or inconsistent with the generated projection.

## Fauna source boundary

Fauna sources are especially vulnerable to role, provenance, precision, and rights collapse. These controls apply whether a reader arrives through this compatibility path or the canonical registry.

| Source family | Preserve | Never imply |
|---|---|---|
| Regulatory and steward authorities | issuing authority, jurisdiction, decision type, effective time, revision, access limits, and sensitive-site posture | that a legal status or steward summary is an observed occurrence |
| Occurrence aggregators and community-science systems | original publisher, record basis, institution, license, coordinate privacy, quality flags, and observation time | that the aggregator is the evidence role, every record is verified, or download permits republication |
| Specimen and collection systems | specimen or occurrence basis, institution, collection event, determiner, rights, and collection-security constraints | that specimen-backed identity bypasses sensitivity or current taxonomic review |
| Telemetry, acoustic, eDNA, and agency monitoring | method, sampling event, equipment or assay context, QA, temporal scope, uncertainty, and access restriction | that detection equals abundance, occupancy, unrestricted location truth, or public-safe telemetry |
| Invasive, mortality, disease, and incident reporting | reporting authority, report basis, verification state, privacy, parcel precision, and correction state | that a candidate report is confirmed or safe to expose |
| Modeled range, suitability, utilization, or richness products | model identity, inputs, run/version, scale, valid time, uncertainty, and validation | that modeled or aggregated output is an observed occurrence |
| Habitat, hydrology, soil, land-cover, roads, settlements, and other context | owning-domain identity, source role, scale, time, and governed join purpose | that contextual correlation becomes Fauna truth |
| Historical records | source vintage, changing taxonomy, method, location uncertainty, digitization limits, and correction lineage | current conditions, unchanged comparability, or modern precision |

GBIF, eBird, iNaturalist, iDigBio, BISON-like systems, and similar services are access or aggregation paths unless an accepted descriptor says otherwise. The access path does not replace the originating evidence role.

Sensitive taxa, exact occurrences, nests, dens, roosts, hibernacula, spawning and breeding sites, telemetry, steward-controlled records, private-land joins, and re-identifying combinations default to denial or restriction until policy, review, transform, receipt, release, correction, and rollback support a public-safe derivative.

Promotion must never silently upgrade source role. Aggregation must never create point truth. AI-generated language must never replace a canonical descriptor, EvidenceBundle, policy decision, review record, or release state.

## Inputs and outputs

| Direction | Accepted surface | Boundary |
|---|---|---|
| Input | Canonical source identity, role, provider, provenance, rights, sensitivity, cadence, scope, and correction metadata | Must resolve from an accepted source record or remain unavailable |
| Input | Contract, schema, policy, fixture, validator, receipt, proof, catalog, and release references | A reference does not prove the target is accepted or executed |
| Output | Human navigation to canonical source governance | Read-only and non-authoritative |
| Output | Optional generated domain view | Requires one-way generation and parity evidence |
| Output | Structured hold or verification item | Must not activate, ingest, promote, release, or publish |

Public clients and ordinary AI/UI surfaces must not read this compatibility path as a data service.

## Validation

Before changing this README or materializing a generated view:

- [ ] Re-pin the repository base and re-read the accepted Directory Rules and ADR-0029.
- [ ] Inventory direct children, writers, readers, references, aliases, and generated-file markers.
- [ ] Confirm all source-descriptor writes remain under the accepted subtype-first topology.
- [ ] Verify every view entry resolves to exactly one canonical source identity and matching digest.
- [ ] Verify role, publisher, provenance, rights, sensitivity, time, freshness, spatial precision, uncertainty, correction, and supersession fields are not upgraded or dropped.
- [ ] Verify no source payload, secret, restricted identifier, unsafe precision, steward-only detail, or public-serving path is introduced.
- [ ] Exercise denied and held cases for sensitive locations, unresolved rights, stale sources, missing canonical records, role mismatch, and parity failure.
- [ ] Verify links, anchors, badges, tables, alerts, code fences, HTML comments, and the final newline.
- [ ] Record generator, parity, correction, and rollback evidence, or retain the view as README-only.

The repository's [`link-check`](../../../../.github/workflows/link-check.yml) workflow is an explicit readiness hold. It does not yet validate repository or external links, so manual or future repository-native link checks remain documentation QA only.

## Required checks before use

- [ ] Confirm the object belongs to the canonical source registry and not this compatibility path.
- [ ] Confirm source identity, source role, provider, provenance, rights, terms, cadence, access posture, steward, and authority limits resolve.
- [ ] Confirm source role is not upgraded by normalization, aggregation, cataloging, release review, API shaping, map rendering, or generated explanation.
- [ ] Confirm sensitive details are absent from registry files, indexes, logs, fixtures, and public summaries.
- [ ] Confirm sensitive sites, telemetry, private identifiers, and re-identifying joins fail closed when unresolved.
- [ ] Confirm context sources remain join support and never become Fauna observation truth.
- [ ] Confirm validation receipts exist before catalog or release eligibility is asserted.
- [ ] Confirm consequential use resolves EvidenceRef to EvidenceBundle or accepted proof support.
- [ ] Confirm catalog and release references point to their owning objects rather than embedding them here.
- [ ] Confirm correction, supersession, withdrawal, stale-state, deactivation, and rollback paths exist.
- [ ] Confirm no public client, map layer, graph edge, search or vector index, generated answer, report, or dashboard reads this path as direct truth.

## Correction, supersession, and rollback

1. Correct the canonical source record or its governing authority first.
2. Emit the required correction, supersession, withdrawal, deactivation, or review record through its owning process.
3. Regenerate any admitted view from the corrected canonical inputs.
4. Invalidate stale view bytes and confirm parity before consumers resume.
5. If the view cannot be regenerated safely, remove the derived view while retaining this no-write README or an approved tombstone.

Before merge, rollback is the prior README blob on the scoped branch. After merge, use a transparent revert or follow-up pull request; do not restore independent descriptor writes at this path.

## Related authority

| Reference | Role |
|---|---|
| [Directory Rules v2](../../../../docs/doctrine/directory-rules.md) | Adopted placement doctrine; see `DIR-SOURCE-003`, `DIR-SOURCE-004`, compatibility, and README inheritance |
| [ADR-0029](../../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Adoption and single-authority decision |
| [`data/registry/`](../../README.md) | Parent registry responsibility boundary |
| [Canonical source registry parent](../../sources/README.md) | Current subtype-first source registry surface; broader implementation claims remain draft or proposed |
| [Canonical Fauna source lane](../../sources/fauna/README.md) | Current Fauna source-first surface; README topology language predates adoption |
| [Source Descriptor Standard](../../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md) | Draft semantic and admission guidance |
| [Fauna Source Registry documentation](../../../../docs/domains/fauna/SOURCE_REGISTRY.md) | Draft human domain guidance and sensitivity posture |
| [Fauna source roles](../../../../docs/domains/fauna/SOURCE_ROLES.md) | Draft role-preservation and anti-collapse guidance |
| [Fauna source families](../../../../docs/domains/fauna/SOURCE_FAMILIES.md) | Draft family orientation; current terms and activation remain unverified |
| [Fauna sensitivity guidance](../../../../docs/domains/fauna/SENSITIVITY.md) | Draft deny-by-default and geoprivacy guidance |
| [Source-authority register](../../../../control_plane/source_authority_register.yaml) | `PROPOSED` machine projection with no entries at the pinned base |
| [Fauna fixtures](../../../../fixtures/domains/fauna/README.md) | Synthetic test boundary; not source authority or real sensitive data |
| [Source schema family](../../../../schemas/contracts/v1/source/README.md) | Mixed-maturity draft family with descriptor path and filename drift |
| [Sources schema compatibility lane](../../../../schemas/contracts/v1/sources/README.md) | Draft compatibility index with a permissive placeholder schema |
| [Fauna contracts](../../../../contracts/domains/fauna/README.md) | Draft semantic lane; runtime and validation maturity remain unverified |
| [Fauna policy](../../../../policy/domains/fauna/README.md) | Proposed greenfield scaffold; binding policy is not established by the README |
| [Fauna sensitivity policy](../../../../policy/sensitivity/fauna/README.md) | Proposed scaffold; binding tier behavior is not established |

## Open verification

| Item | Status | Evidence required |
|---|---|---|
| Direct-child inventory at this path | `NEEDS VERIFICATION` | Pinned recursive tree and file classifications |
| Active writers and consumers | `UNKNOWN` | Connector, pipeline, tool, workflow, API/UI, and external-consumer inventory |
| View generator and parity check | `NOT VERIFIED` | Repository-owned generator, deterministic fixtures, tests, and output digest |
| Canonical Fauna descriptor inventory | `UNKNOWN` | Pinned recursive inventory and accepted record classification |
| Canonical source-ID grammar | `NEEDS VERIFICATION` | Accepted identity contract, alias mapping, migration record, and validator |
| SourceDescriptor contract and schema authority | `NEEDS VERIFICATION` | Resolved source/sources and hyphen/underscore drift, accepted pairing, fixtures, and validation |
| Fauna activation state | `NOT ESTABLISHED` | Populated source-authority entry and reviewed activation decision |
| Rights, sensitivity, stale-state, correction, and rollback enforcement | `UNKNOWN` | Policy, negative fixtures, validator outputs, receipts, and drills |
| CODEOWNERS and accountable steward | `NEEDS VERIFICATION` | Current path-specific routing and named accountable owner |

Unknowns narrow behavior and block higher-authority claims; they do not authorize plausible defaults.

## Maintainer note

Keep the chain explicit:

```text
canonical SourceDescriptor
  -> activation decision
  -> RAW admission
  -> WORK / QUARANTINE
  -> PROCESSED
  -> proof + catalog + policy + review
  -> release decision
  -> governed public-safe surface
```

Never collapse it into:

```text
compatibility README or generated view
  -> public Fauna truth
```

## Change history

### v0.3.0 - 2026-07-28

- aligned the existing path with adopted Directory Rules v2 and ADR-0029;
- changed the path posture from unresolved descriptor lane to no-independent-write compatibility view;
- removed the speculative local child tree and unaccepted descriptor JSON;
- preserved source-role, provider, provenance, rights, sensitivity, geoprivacy, correction, rollback, and public-boundary controls;
- added evidence-backed status, compact navigation, validation, stable legacy anchors, and explicit open verification.

### v0.2.0 - 2026-06-28

- replaced the original placeholder with a detailed Fauna source-registry boundary;
- recorded the then-unresolved domain-first versus subtype-first path conflict.

[Back to top](#top)
