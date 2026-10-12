<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/flora/sources/readme
name: Flora Source Registry Compatibility README
path: data/registry/flora/sources/README.md
type: data-registry-domain-source-compatibility-readme
version: v0.3.0
status: draft; compatibility-boundary; no-independent-writes
owners:
  - "NEEDS VERIFICATION: registry and source stewards"
  - "NEEDS VERIFICATION: Flora domain steward"
  - "NEEDS VERIFICATION: rights, sensitivity, geoprivacy, and cultural-review stewards"
  - "NEEDS VERIFICATION: policy, validation, proof, and release stewards"
created: 2026-06-28
updated: 2026-07-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: registry
registry_scope: flora-source-navigation-view
domain: flora
path_posture: domain-first compatibility view; subtype-first registry authority; descriptor writes denied here
safety_posture: no-direct-public-path; no-source-activation; rare-plant-deny-default; culturally-sensitive-plant-knowledge-protected; fail-closed
related:
  - ../../README.md
  - ../README.md
  - ../../sources/README.md
  - ../../sources/flora/README.md
  - ../../datasets/README.md
  - ../../datasets/flora/README.md
  - ../../crosswalks/README.md
  - ../../../raw/flora/README.md
  - ../../../work/flora/README.md
  - ../../../quarantine/flora/README.md
  - ../../../processed/flora/README.md
  - ../../../receipts/README.md
  - ../../../proofs/flora/README.md
  - ../../../catalog/domain/flora/README.md
  - ../../../published/flora/README.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../../docs/domains/flora/SOURCE_REGISTRY.md
  - ../../../../docs/domains/flora/SOURCE_ROLES.md
  - ../../../../docs/domains/flora/SOURCE_FAMILIES.md
  - ../../../../docs/domains/flora/SENSITIVITY.md
  - ../../../../control_plane/source_authority_register.yaml
  - ../../../../fixtures/domains/flora/README.md
  - ../../../../schemas/contracts/v1/source/README.md
  - ../../../../schemas/contracts/v1/domains/flora/README.md
  - ../../../../contracts/domains/flora/README.md
  - ../../../../policy/domains/flora/README.md
  - ../../../../policy/sensitivity/flora/README.md
  - ../../../../.github/workflows/domain-flora.yml
  - ../../../../release/candidates/flora/README.md
tags:
  - kfm
  - data
  - registry
  - flora
  - sources
  - compatibility
  - generated-view
  - source-role
  - rights
  - sensitivity
  - geoprivacy
  - rare-plants
  - culturally-sensitive-plants
  - taxonomy
  - specimens
  - occurrences
  - vegetation
  - correction
  - rollback
  - cite-or-abstain
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_commit: 92768ffb76b971b134a7a0e600c06170145800d0
  prior_blob: 0dceb51c8fecadc2857539b4a8fe06bbfbe642f6
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  adr_0029_blob: cd044a38047cc9b3725d2e083eb201eb86109308
  canonical_flora_readme_blob: 356cd29ca5a764ffe1e774fb565bce50bba46011
  flora_parent_blob: 920a4eaa3effb81fde79e09e15399040d493b537
  registry_parent_blob: b327d22956f5454482a35dbf265f45b901c1f2a3
  source_registry_parent_blob: 2821e9681273bff6b430920d0a45312c5643ba33
  source_authority_register_blob: 82c23722520922f5ca0dad7f37ed794d1c2edf81
  flora_source_registry_doc_blob: 26479f938d4a08eec9d9dcd66b1a20120b119f06
  domain_flora_workflow_blob: c792d126e5726d8895f56fd97800bee7fcba4a15
  inspection_date: 2026-07-28
notes:
  - "ADR-0029 adopted Directory Rules v2 at docs/doctrine/directory-rules.md."
  - "Directory Rules DIR-SOURCE-003 and DIR-SOURCE-004 make the subtype-first source registry authoritative and prohibit this domain-first path from acting as an independent writer."
  - "The canonical Flora source README is present but predates Directory Rules v2 adoption and still describes topology as unresolved."
  - "The parent data/registry/flora/README.md also predates adoption and remains a separate follow-up modernization surface."
  - "The source-authority register is PROPOSED and empty; no active Flora source admission is established by that register."
  - "No generator, parity check, active writer, active consumer, or concrete canonical Flora descriptor inventory was verified for this path."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>
<a id="flora-source-registry"></a>

# Flora Source Registry Compatibility View

[![Status: compatibility boundary](https://img.shields.io/badge/status-compatibility%20boundary-f59e0b?style=flat-square)](#status)
[![Writes: denied](https://img.shields.io/badge/writes-denied-b91c1c?style=flat-square)](#write-contract)
[![Rare plants: fail closed](https://img.shields.io/badge/rare%20plants-fail%20closed-b42318?style=flat-square)](#flora-source-boundary)
[![Truth: cite or abstain](https://img.shields.io/badge/truth-cite%20or%20abstain-1a7f37?style=flat-square)](../../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md)

> **One-line purpose.** Preserve a safe, human-readable Flora source navigation path while source identity and descriptor writes remain under the subtype-first registry authority.

> [!CAUTION]
> Do not add or edit source descriptors, activation decisions, source payloads, credentials, exact sensitive plant locations, culturally restricted knowledge, or public-facing data here. This path does not activate a source, prove a botanical claim, grant rights, clear sensitivity, authorize release, or publish KFM content.

**Navigation:** [Purpose](#scope) · [Status](#status) · [Authority](#path-posture) · [Repository fit](#repo-fit) · [Write contract](#write-contract) · [View contract](#view-contract) · [Flora controls](#flora-source-boundary) · [Inputs and outputs](#inputs-and-outputs) · [Validation](#validation) · [Correction and rollback](#correction-supersession-and-rollback) · [Related authority](#related-authority) · [Open verification](#status-notes)

<a id="scope"></a>

## Purpose

This README governs the existing domain-first path:

```text
data/registry/flora/sources/
```

Its bounded role is navigation and migration compatibility for readers approaching source governance from the Flora domain lane. It may identify or link to Flora-related source records, but it must not become a second registry writer.

The authoritative responsibility remains registry identity and routing—not botanical observations, specimen payloads, taxonomic conclusions, rare-plant determinations, vegetation classifications, evidence, policy, catalog closure, release, or public delivery.

## Status

| Surface | Evidence-backed state |
|---|---|
| This README path | **CONFIRMED** at `main@92768ffb76b971b134a7a0e600c06170145800d0` |
| Governing Directory Rules | **CONFIRMED adopted** through [ADR-0029](../../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) |
| Domain-first source path | **Compatibility/generated-view posture** under `DIR-SOURCE-004` |
| Subtype-first source registry | **Canonical placement rule** under `DIR-SOURCE-003` |
| Canonical Flora source README | **CONFIRMED present** at [`data/registry/sources/flora/`](../../sources/flora/README.md); its topology text predates adoption |
| Concrete canonical Flora descriptor inventory | **UNKNOWN** in bounded repository search; only the README was established under that path |
| Source-authority register | **CONFIRMED `PROPOSED` and empty**; no active source admission established |
| Flora validation workflow | **Explicit readiness holds**; no executable Flora validator, proof producer, release dry run, source admission, or publication authority |
| Generator and parity validation for this view | **NEEDS VERIFICATION** |
| Active writers and consumers of this exact path | **UNKNOWN** |
| Accountable owner and CODEOWNERS routing | **NEEDS VERIFICATION** |
| Public readiness | **DENY BY DEFAULT** |

> [!IMPORTANT]
> Repository presence is not activation. A README, proposed schema, empty register, source-family document, connector, watcher, workflow, commit, pull request, or merge does not establish an admitted source, accepted descriptor, rights clearance, sensitivity clearance, evidence closure, release, or public-safe output.

<a id="path-posture"></a>

## Path posture and authority decision

The accepted Directory Rules separate the two path shapes:

| Concern | Governing home | This path's relation |
|---|---|---|
| Machine source identities and descriptors | `data/registry/sources/` | May point to them; must not duplicate or mutate them |
| Human source guidance | `docs/sources/` and Flora domain documentation | May summarize boundaries and link outward |
| Connector and watcher implementation | `connectors/`, `tools/`, and `pipelines/` | No executable or activation authority here |
| Source payloads | `data/raw/`, `data/work/`, or `data/quarantine/` as governed | Payloads are prohibited here |
| Validation evidence and process memory | `data/proofs/` and `data/receipts/` | References only |
| Catalog, release, and public-safe carriers | `data/catalog/`, `release/`, and `data/published/` | No catalog, release, or publication authority here |

**Placement result for source-descriptor records:** `DENY` independent writes here. A one-way generated navigation view may be `MIRROR` only after its canonical inputs, generator, owner, source and output digests, parity check, consumers, rollback, and exit criteria are verified.

This README remains at the requested path to preserve navigation and make the no-write boundary explicit. It does not resolve source-ID grammar, schema-path drift, producer and consumer inventory, or the migration status of every existing registry artifact.

<a id="suggested-directory-shape"></a>
<a id="suggested-descriptor-shape"></a>

### Retired local sketches

Earlier versions proposed a domain-local child tree and an illustrative descriptor JSON shape. Those sketches are removed because they could harden into parallel structure, vocabulary, or schema authority. Use the canonical subtype-first registry, paired contract and schema authority, and accepted migration records instead. Exact descriptor shape and implementation maturity remain open verification items.

<a id="repo-fit"></a>

## Repository fit

| Responsibility | Owning surface | Boundary |
|---|---|---|
| Registry parent | [`data/registry/`](../../README.md) | Registry identity and routing; not lifecycle payload storage |
| Canonical source parent | [`data/registry/sources/`](../../sources/README.md) | Machine source identity and descriptor placement |
| Canonical Flora source lane | [`data/registry/sources/flora/`](../../sources/flora/README.md) | Flora source-registry surface; concrete inventory and accepted implementation remain unverified |
| Domain-first Flora registry parent | [`data/registry/flora/`](../README.md) | Existing compatibility/routing parent; it also needs accepted-state alignment |
| Dataset and crosswalk registries | [Flora datasets](../../datasets/flora/README.md) and [crosswalks](../../crosswalks/README.md) | Dataset identity and mapping-state claims; neither is source-descriptor authority |
| Human Flora source guidance | [Flora Source Registry](../../../../docs/domains/flora/SOURCE_REGISTRY.md), [Source Roles](../../../../docs/domains/flora/SOURCE_ROLES.md), [Source Families](../../../../docs/domains/flora/SOURCE_FAMILIES.md), and [Sensitivity](../../../../docs/domains/flora/SENSITIVITY.md) | Draft human guidance; not descriptor storage, activation, or release proof |
| Contracts and schemas | [Flora contracts](../../../../contracts/domains/flora/README.md), [source schemas](../../../../schemas/contracts/v1/source/README.md), and [Flora schemas](../../../../schemas/contracts/v1/domains/flora/README.md) | Meaning and machine shape remain separate; accepted pairing and enforcement need verification |
| Policy and sensitivity | [Flora policy](../../../../policy/domains/flora/README.md) and [Flora sensitivity policy](../../../../policy/sensitivity/flora/README.md) | Binding decisions remain separate; a registry README cannot make them |
| Lifecycle payloads | [RAW](../../../raw/flora/README.md), [WORK](../../../work/flora/README.md), [QUARANTINE](../../../quarantine/flora/README.md), and [PROCESSED](../../../processed/flora/README.md) | Actual source and derived bytes; never stored here |
| Receipts, proofs, and catalog | [Receipts](../../../receipts/README.md), [Flora proofs](../../../proofs/flora/README.md), and [Flora catalog](../../../catalog/domain/flora/README.md) | Process memory, evidence support, and projections; none is source-registry authority |
| Release decisions | [`release/candidates/flora/`](../../../../release/candidates/flora/README.md) and `release/` | Candidate and release authority remain downstream and independently governed |
| Public surfaces | Governed APIs and released artifacts only | Public clients do not read this compatibility path as data |

<a id="accepted-material"></a>

## Write contract

### Allowed

- this compatibility README;
- a verified, generated, read-only index whose entries resolve to canonical subtype-first records;
- migration or tombstone metadata required by an accepted migration;
- parity, source digest, generation, expiry, and rollback metadata that cannot be mistaken for source admission;
- links to canonical contracts, schemas, policies, fixtures, tests, receipts, proofs, catalogs, correction records, rollback targets, and release decisions.

<a id="exclusions"></a>

### Prohibited

| Do not place or maintain here | Required handling |
|---|---|
| `SourceDescriptor` records | Write only through the accepted subtype-first registry topology |
| Source-intake or source-activation decisions | Use the accepted control, receipt, or decision process; do not invent a registry-local decision store |
| Herbarium archives, specimen records, occurrence exports, taxonomy tables, rare-plant feeds, vegetation data, invasive records, phenology feeds, restoration records, remote-sensing scenes, rasters, vectors, models, or source-native files | Route through RAW, WORK, or QUARANTINE according to admission and sensitivity state |
| Manually copied source indexes | Generate from canonical records with parity validation or do not create |
| Exact rare, protected, or culturally sensitive plant locations; steward-only knowledge; private identifiers; seed-source or collection-security detail | Keep in approved restricted storage and governed lifecycle lanes; fail closed |
| Rights, sensitivity, geoprivacy, stale-state, access, or release policy | Keep normative rules under `policy/` |
| Contracts or machine schemas | Keep meaning under `contracts/` and shape under `schemas/` |
| Receipts, proofs, catalog records, release records, or published carriers | Use each owning object-family lane |
| Credentials, tokens, signed URLs, private endpoints, or restricted operational details | Use approved secret or restricted storage; never commit here |
| Public API, map, dashboard, alert, search, graph, vector-index, or AI output | Use governed released interfaces; cite or abstain |

## View contract

If a generated Flora view is later implemented, every row must derive from a canonical source record and remain strictly less authoritative than that record.

| Required view property | Minimum behavior |
|---|---|
| Stable identity | Carry the canonical `source_id`; do not mint a domain-local ID |
| Source location | Link to the canonical record or governed resolver |
| Role preservation | Carry the exact canonical role; do not infer or upgrade a role locally |
| Provider and provenance | Preserve original publisher, contributing institution, collection, observer, dataset, and aggregation path where applicable |
| Rights and sensitivity | Surface unresolved or restrictive posture without upgrading it |
| Taxonomic scope | Preserve authority, accepted name, synonym treatment, concept/version, and uncertainty where provided |
| Spatial precision | Preserve precision, generalization, obscuration, embargo, and steward restrictions without exposing protected detail |
| Time and freshness | Preserve source, collection/observation, retrieval, revision, effective, expiration, correction, and stale-state distinctions when material |
| Scope and uncertainty | Preserve specimen/occurrence/plot/model basis, method, scale, confidence, and limitations |
| Change lineage | Carry correction, supersession, withdrawal, deactivation, and rollback references |
| Generation evidence | Record canonical input digest, generator version, output digest, generated time, parity result, and rollback target |

The view must fail closed when a canonical record is missing, ambiguous, stale beyond its declared use, rights- or sensitivity-unresolved, taxonomically conflicted, or inconsistent with the generated projection.

<a id="flora-source-boundary"></a>

## Flora source boundary

Flora source families are especially vulnerable to taxonomic, spatial, temporal, rights, and source-role collapse. The controls below apply whether a reader arrives through this compatibility path or the canonical registry.

| Source family or material class | Preserve | Never imply |
|---|---|---|
| Taxonomic authorities, checklists, and name services | authority, version/date, accepted name, synonym/concept treatment, rank, and unresolved conflicts | that a name match proves an occurrence, identity beyond scope, or release permission |
| Herbarium, specimen, and collection records | originating institution, catalog/basis of record, collector and collection time where lawful, determination history, precision, rights, and restrictions | current presence, population status, public-safe exact location, or unrestricted reuse |
| Observation and occurrence networks | original provider/observer, basis of record, validation state, coordinate uncertainty, obscuration, license, and event time | that aggregation creates canonical authority or that every record is verified |
| Rare, protected, or steward-controlled plant records | issuing/steward authority, jurisdiction, effective time, embargo, access tier, sensitivity, and disclosure limits | exact-location permission, timeless status, or general public eligibility |
| Vegetation plots, communities, and classifications | classification system/version, plot or survey basis, method, scale, time, uncertainty, and source role | individual plant occurrence, permanence, or equivalence across classification systems |
| Invasive, regulated, or administrative plant records | issuing authority, jurisdiction, effective period, status class, reporting method, and source role | direct field observation, universal legal status, or unchanged current status |
| Phenology observations | protocol, observer/network, life-stage definition, observation time, location precision, QA, and uncertainty | population-wide timing or unrestricted exact-site disclosure |
| Restoration, seed-transfer, and provenance records | material/source provenance, treatment, purpose, geography, time, rights, and stewardship limits | naturally occurring presence, taxonomic certainty beyond evidence, or public release permission |
| Remote-sensing, modeled vegetation, habitat suitability, or candidate surfaces | product/model version, run/acquisition time, inputs, method, resolution, scale, uncertainty, validation, and source role | direct botanical observation, confirmed species presence, or authoritative rare-plant status |
| Context sources such as soil, hydrology, habitat, land cover, roads, settlements, or archaeology | context role, scale, time, uncertainty, and join purpose | botanical occurrence or taxonomic truth |

Cross-domain joins require review before release, especially joins that could reconstruct protected plant locations or expose culturally sensitive knowledge, private-land information, collection-security detail, or stewardship restrictions.

Promotion must never silently upgrade source role. Aggregation must never create point truth. AI-generated language must never replace a canonical descriptor, `EvidenceBundle`, policy decision, review record, or release state.

## Inputs and outputs

| Direction | Accepted surface | Boundary |
|---|---|---|
| Input | Canonical source identities, role, rights, sensitivity, cadence, taxonomic scope, spatial precision, correction, supersession, and rollback metadata | Must resolve from an accepted source record or remain explicitly unavailable |
| Input | Registry, contract, schema, policy, fixture, validator, receipt, proof, catalog, and release references | A reference does not prove the target is accepted or executed |
| Output | Human navigation to canonical source governance | Read-only and non-authoritative |
| Output | Optional generated domain view | Requires one-way generation and parity evidence |
| Output | Structured hold, migration, or verification item | Must not activate, ingest, promote, release, or publish |

Public clients and ordinary AI/UI surfaces must not read this compatibility path as a data service.

## Validation

Before changing this README or materializing a view:

- [ ] Re-pin the repository base and re-read the accepted Directory Rules and ADR-0029.
- [ ] Inventory direct children, writers, readers, references, aliases, and any generated-file markers.
- [ ] Confirm all source-descriptor writes remain under the accepted subtype-first topology.
- [ ] Verify every view entry resolves to exactly one canonical source identity and matching digest.
- [ ] Verify role, provider/origin, rights, sensitivity, taxonomy, time/freshness, spatial scope, citation, correction, and supersession fields are not upgraded or dropped.
- [ ] Verify no source payload, secret, protected identifier, harmful precision, culturally restricted knowledge, or public-serving path is introduced.
- [ ] Verify links, anchors, badges, tables, alerts, code fences, HTML comments, UTF-8 encoding, and the final newline.
- [ ] Record generator, parity, and rollback evidence—or retain the view as README-only.

The repository's [`domain-flora`](../../../../.github/workflows/domain-flora.yml) workflow is an explicit readiness-hold workflow. It checks boundaries and fails when executable Flora tests, validators, geoprivacy implementation, proof material, or release machinery surface without deliberate wiring. It does not validate registry records, admit sources, prove botanical truth, apply geoprivacy policy, build proof, approve release, or publish.

A passing source-level Markdown check or green held workflow does not prove canonical registry enforcement, descriptor validity, rights clearance, geoprivacy review, policy correctness, source activation, evidence closure, release readiness, or public safety.

<a id="required-checks-before-use"></a>

### Required checks before use

- [ ] Confirm the registry object belongs under the canonical subtype-first source lane rather than this compatibility view.
- [ ] Confirm no authoritative descriptor, activation decision, source payload, receipt, proof, catalog record, release object, or policy file is being added here.
- [ ] Confirm source identity, originating provider, source role, rights, access, sensitivity, geoprivacy, cadence, taxonomic scope, spatial precision, and stale-state obligations from current evidence.
- [ ] Confirm exact rare/protected/culturally sensitive plant locations, steward-controlled records, culturally sensitive knowledge, and private or collection-security details remain excluded.
- [ ] Confirm source role cannot be upgraded by aggregation, taxonomic matching, validation, modeling, crosswalking, map rendering, graph projection, AI interpretation, or promotion.
- [ ] Confirm aggregator access does not erase origin, provider, institution, collection, observer, specimen, dataset, or source-role lineage.
- [ ] Confirm public clients and generated-answer surfaces cannot read this path directly.
- [ ] Confirm any migration preserves identity, aliases, source roles, references, history, corrections, withdrawals, and rollback targets.

## Correction, supersession, and rollback

1. Correct the canonical source record or governing authority first.
2. Emit the required correction, supersession, withdrawal, deactivation, review, or rollback record through its owning process.
3. Regenerate any admitted compatibility view from corrected canonical inputs.
4. Invalidate stale view bytes and verify parity before consumers resume.
5. If the view cannot be regenerated safely, remove the derived view while retaining this no-write README or an approved tombstone.

Before merge, rollback is closing the draft pull request and leaving the branch unmerged. After merge, use a transparent revert or follow-up pull request; do not restore independent descriptor writes at this path.

## Related authority

| Reference | Role |
|---|---|
| [Directory Rules v2](../../../../docs/doctrine/directory-rules.md) | Adopted placement doctrine; see `DIR-SOURCE-003`, `DIR-SOURCE-004`, and README inheritance |
| [ADR-0029](../../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Adoption and single-authority decision |
| [`data/registry/`](../../README.md) | Parent registry responsibility boundary |
| [Subtype-first Flora registry](../../sources/flora/README.md) | Canonical placement surface for Flora source records; concrete inventory remains unverified |
| [Source Descriptor Standard](../../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md) | Draft semantic and admission guidance |
| [Flora Source Registry documentation](../../../../docs/domains/flora/SOURCE_REGISTRY.md) | Human domain guidance; explicitly identifies the subtype-first machine-readable home |
| [Source authority register](../../../../control_plane/source_authority_register.yaml) | Proposed machine projection; currently empty |
| [Flora fixtures](../../../../fixtures/domains/flora/README.md) | Test-data boundary; not source authority |
| [Flora workflow](../../../../.github/workflows/domain-flora.yml) | Explicit readiness holds; not validation, source admission, proof, release, or publication authority |

<a id="status-notes"></a>

## Open verification

| Item | Status | Evidence required |
|---|---|---|
| Direct-child inventory at this path | **NEEDS VERIFICATION** | Pinned recursive tree and file classifications |
| Active writers and consumers | **UNKNOWN** | Connector, watcher, pipeline, tool, workflow, API/UI, and external-consumer inventory |
| View generator and parity check | **NOT VERIFIED** | Repository-owned generator, deterministic fixtures, tests, and output digest |
| Concrete descriptor inventory under `data/registry/sources/flora/` | **UNKNOWN** in bounded search | Pinned tree, descriptors, identity register, rights/sensitivity review, and validation |
| Canonical Flora source README modernization | **NEEDS VERIFICATION** | Align its pre-adoption topology text with accepted Directory Rules without changing descriptor state |
| Parent `data/registry/flora/README.md` modernization | **NEEDS VERIFICATION** | Align its pre-adoption topology text while preserving compatibility and migration controls |
| SourceDescriptor contract and schema authority | **NEEDS VERIFICATION** | Accepted contract/schema pairing plus fixtures and validation |
| Flora activation state | **UNKNOWN** | Populated source-authority entry and reviewed activation decision |
| Rights, sensitivity, taxonomy, stale-state, correction, and rollback enforcement | **UNKNOWN** | Policy, negative fixtures, validator outputs, receipts, and drills |
| CODEOWNERS and accountable stewards | **NEEDS VERIFICATION** | Current path-specific routing and named accountable owners |
| Final migration disposition | **PROPOSED / NEEDS VERIFICATION** | Retained compatibility README, generated mirror, redirect/tombstone, or retirement decision |
| Physical deletion eligibility | **HOLD** | Zero-writer, zero-consumer, link-closure, parity/retirement, and rollback evidence |

Unknowns narrow behavior and block higher-authority claims; they do not authorize plausible defaults.

## Change history

### v0.3.0 — 2026-07-28

- aligned the existing path with adopted Directory Rules v2 and ADR-0029;
- changed the path posture from unresolved descriptor lane to no-independent-write compatibility view;
- removed proposed child directories and illustrative descriptor vocabulary that could create parallel authority;
- preserved source-role, provider-origin, taxonomy, rights, sensitivity, geoprivacy, freshness, correction, rollback, and public-boundary controls;
- added evidence-backed status, navigation, validation, workflow-scope, and open-verification sections.

### v0.2.0 — 2026-06-28

- expanded the prior thin README into a detailed Flora source-registry boundary;
- recorded the then-unresolved domain-first versus subtype-first path conflict.

<a id="maintainer-note"></a>

KFM rule: `data/registry/flora/sources/` is a compatibility view for public-safe navigation and lineage only. It is not an independent source-registry writer, payload store, botanical truth authority, evidence authority, policy authority, release authority, sensitive-location authority, or public Flora data service.

[Back to top](#top)
