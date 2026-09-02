<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-24-idea-atlas-reconciliation-source-map
title: Pass 24 Idea Atlas Reconciliation Source Map
type: source-map
version: v1.0.0
status: proposed
owners: OWNER_TBD - Documentation steward; Source steward; Evidence steward; Sensitivity steward; Release steward
created: 2026-08-12
updated: 2026-08-12
policy_label: internal; exploratory; non-authoritative; privacy-minimized
related:
  - ./README.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ./new-ideas-4-16-source-map.md
  - ../../../contracts/source/source_descriptor.md
  - ../../../contracts/domains/hydrology/hydro_identity_bridge.md
  - ../../../contracts/data/material_change_assessment.md
  - ../../../contracts/domains/soil/promotion_materiality_profile.md
  - ../../../policy/sensitivity/fauna/sensitive_taxa_deny.rego
  - ../../../contracts/evidence/evidence_drawer_payload.md
  - ../../../contracts/release/geospatial_carrier_readiness.md
tags: [kfm, intake, pass-24, fauna, soils, hydrography, reconciliation, source-map, cite-or-abstain]
notes:
  - "The connected atlas is a non-authoritative downstream carrier; its cards do not establish source rights, implementation, release, or publication authority."
  - "The private Drive locator, PDF bytes, source body, credentials, and sensitive occurrence details are deliberately omitted."
[/KFM_META_BLOCK_V2] -->

# Pass 24 Idea Atlas Reconciliation Source Map

> **PROPOSED, NON-AUTHORITATIVE:** This record reconciles the 61 Pass 24 cards against a pinned repository snapshot. It preserves lineage, sensitivity boundaries, and explicit holds; it does not adopt the atlas, activate a source, approve a crosswalk, or authorize publication.

## Outcome

`CONFIRMED`: the connected `KFM_Pass_24_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf` identifies itself as Pass 24, with run date 2026-05-17, and contains 61 Pass 24 card records: 5 idea, 52 programming, and 4 feature cards. Sixty are active; `KFM-P24-PROG-0052` is quarantine.

`CONFIRMED`: on repository snapshot `main@9d5090be5ec6bcaf4bda3a7ddb41e94d5e35f4fa`, broad parts of the atlas are already represented by source descriptors and catalogs, hydrology identity and crosswalk contracts, material-change and soil-promotion assessments, sensitive-taxa policy, evidence-drawer semantics, validators, fixtures, and geospatial-carrier readiness surfaces.

`PROPOSED`: the smallest distinct addition is this pass-wide reconciliation record. The atlas does not establish a safe basis for another fauna, soil, hydrography, policy, or publication implementation packet.

`NEEDS VERIFICATION`: source rights and terms, current endpoints and cadence, sensitive-taxa handling, exact ScienceBase or DOI identity, live data quality, hosted execution, operational settings, and public-release readiness.

## Source and privacy boundary

| Field | Evidence-backed value |
|---|---|
| Source title | `KFM_Pass_24_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf` |
| Source posture | `CONFIRMED`: downstream carrier; cite-or-abstain; repository implementation recorded as unknown in the source |
| Source lineage | `CONFIRMED`: synthesized from Pass 23 plus New Ideas 4-16-26 and New Ideas 4-17-26 candidate material |
| Inventory | `CONFIRMED`: 61 unique Pass 24 stable IDs; 5 idea, 52 programming, 4 feature |
| Source status exception | `CONFIRMED`: `KFM-P24-PROG-0052` is quarantined in the source |
| Rights and license | `UNKNOWN`; the atlas records its generated-atlas license as needing verification |
| Disclosure | Title, pass, run date, stable IDs, normalized themes, and bounded reconciliation only |
| Omitted | Drive locator, private link, PDF bytes, source-body reproduction, credentials or API keys, contributor identities, and exact sensitive locations |

The Drive-readable text was scanned end to end. All 61 new-card records were enumerated, and their stable ID, category, status, title, and normalized statement were compared with current repository names and responsibilities. Source prose, source hashes, source-declared implementation status, and proposed file homes were not treated as repository evidence.

## Repository inspection boundary

The comparison was pinned to `main@9d5090be5ec6bcaf4bda3a7ddb41e94d5e35f4fa`. Inspection covered current paths and targeted content search, recent pull-request lineage, exact proposed path/title/branch searches, and repository-wide open pull requests.

At preparation time:

- `CONFIRMED`: the exact proposed path, title, and branch were absent;
- `CONFIRMED`: the repository had no open pull requests or drafts;
- `CONFIRMED`: no Pass 24 pass-wide reconciliation record was present;
- `CONFIRMED`: every explicit repository anchor in this record existed on the pinned snapshot;
- `UNKNOWN`: file presence does not prove source admission, current configuration, runtime use, policy approval, release state, or publication safety.

## Directory Rules path decision

```yaml
path_decision:
  artifact: "Pass 24 Idea Atlas Reconciliation Source Map"
  proposed_path: "docs/intake/exploratory/pass-24-idea-atlas-reconciliation-source-map.md"
  artifact_kind: "human-readable exploratory source reconciliation"
  authority_owner: "documentation intake"
  lifecycle: "non-data; exploratory intake"
  execution_role: "none"
  scope_or_id: "pass-24-idea-atlas-reconciliation"
  exposure: "privacy-minimized internal documentation"
  mutability: "versioned Git document"
  evidence:
    - "ADR-0029 accepts the pinned Directory Rules v2 bytes"
    - "docs/intake/exploratory/README.md defines this lane as non-canonical intake"
    - "the proposed exact path is absent on the inspected main snapshot"
  cited_rules:
    - "DIR-SIGNATURE-001"
    - "DIR-PLACE-001"
    - "DIR-PLACE-007"
  outcome: "PLACE"
```

The artifact has one owner and one responsibility: human-readable intake reconciliation. It does not create a machine source identity, contract, schema, policy, receipt, proof, release decision, public artifact, or new root. The existing exploratory lane is used because its README admits non-canonical source and idea packets awaiting evidence and routing.

## Complete card inventory by category

This table accounts for every Pass 24 stable ID without copying the source body.

| Category | Stable IDs | Count |
|---|---|---:|
| Reviewer experience | `KFM-P24-FEAT-0001`, `0002` | 2 |
| Catalog and source descriptors | `KFM-P24-FEAT-0003`; `KFM-P24-PROG-0001`-`0006`, `0033`, `0034` | 9 |
| Release and material change | `KFM-P24-FEAT-0004`; `KFM-P24-IDEA-0003`; `KFM-P24-PROG-0017`-`0019`, `0049`, `0050` | 7 |
| Data lifecycle, hashes, and receipts | `KFM-P24-IDEA-0001`; `KFM-P24-PROG-0009`-`0012`, `0025`, `0043` | 7 |
| Policy and sensitivity | `KFM-P24-IDEA-0002`; `KFM-P24-PROG-0013`, `0016`, `0027` | 4 |
| Modeling and identity | `KFM-P24-IDEA-0004`; `KFM-P24-PROG-0007`, `0008`, `0035`-`0038`, `0048` | 8 |
| Evidence and proof references | `KFM-P24-IDEA-0005`; `KFM-P24-PROG-0028`, `0042` | 3 |
| Pipelines, transforms, and validators | `KFM-P24-PROG-0014`, `0015`, `0020`-`0024`, `0026`, `0029`-`0032`, `0039`-`0041`, `0047` | 16 |
| Security verification | `KFM-P24-PROG-0044` | 1 |
| Metadata and identity graph | `KFM-P24-PROG-0045`, `0046` | 2 |
| Map carriers | `KFM-P24-PROG-0051` | 1 |
| Quarantined placement proposal | `KFM-P24-PROG-0052` | 1 |
| **Total** |  | **61** |

Numeric ranges retain the fully written prefix and include both endpoints. The source remains the authority for exact card text; this inventory preserves only enough identity to prevent duplicate mining.

## Reconciliation against the pinned snapshot

Status terms are intentionally narrow:

- `REPRESENTED` means an adjacent or matching repository surface exists; it does not mean the surface is adopted, deployed, or operationally proven.
- `PARTIAL` means only part of the cluster is represented or exact semantic equivalence was not established.
- `HOLD` means no implementation or operational claim should transfer from the source without new evidence and owner review.

| Atlas cluster | Current repository anchors | Reconciliation |
|---|---|---|
| Source identity, cadence, rights, and freshness | `contracts/source/source_descriptor.md`; current human source catalogs and refresh runbooks | `REPRESENTED/PARTIAL`: source identity and disclosure surfaces exist. Current endpoints, terms, cadence, API-key requirements, and authoritative roles remain source-specific verification work. |
| Fauna sensitivity, generalization, aggregation, and access | `policy/sensitivity/fauna/sensitive_taxa_deny.rego`; `contracts/evidence/evidence_drawer_payload.md` | `REPRESENTED/HOLD`: deny-by-default and evidence-display boundaries exist. No exact occurrence, public coordinate, role grant, redaction result, or sensitivity clearance is inferred. |
| Vendor identity, dual hashes, and material change | `contracts/data/material_change_assessment.md`; current hash-binding and soil dual-hash surfaces | `REPRESENTED/PARTIAL`: deterministic identity and bounded material-change declarations exist. No source row, prior publication, or live threshold evaluation is proven. |
| Soil descriptors, mukey joins, and promotion materiality | `contracts/domains/soil/mukey_properties.md`; `contracts/domains/soil/promotion_materiality_profile.md`; current NRCS source catalogs and connectors | `REPRESENTED/PARTIAL`: soil identity and materiality families exist. No live SSURGO, gSSURGO, gNATSGO, or SoilGrids payload, transform, coverage result, or admitted release is inferred. |
| Hydrology identity bridge and crosswalk evidence | `contracts/domains/hydrology/hydro_identity_bridge.md`; current HUC12/COMID crosswalk surfaces | `REPRESENTED/PARTIAL`: permanent/legacy identity, relationship, abstention, and crosswalk evidence have repository owners. The exact ScienceBase item, DOI, version, checksum, and download remain unverified. |
| Finite outcomes, policy decisions, and proof-pack references | `contracts/runtime/DecisionEnvelope.md`; `contracts/data/catalog_closure_packet.md` | `REPRESENTED/PARTIAL`: finite outcomes and closure references exist. Presence does not prove policy execution, authenticated review, proof resolution, promotion, or release. |
| Evidence drawer, hydro badge, and review queue | `contracts/evidence/evidence_drawer_payload.md` and current read-only review/display surfaces | `PARTIAL/HOLD`: evidence display has a governed semantic owner. No Pass 24-specific badge, action queue, role grant, or mutation surface is authorized by this map. |
| PMTiles/COG carrier readiness | `contracts/release/geospatial_carrier_readiness.md` | `REPRESENTED/PARTIAL`: carrier-readiness declarations exist. No soil carrier was built, signed, released, deployed, cached, or published by this reconciliation. |
| Source-proposed file homes | accepted Directory Rules v2 and ADR-0029 | `HOLD`: quarantined `KFM-P24-PROG-0052` stays quarantined. Source-proposed paths do not create or move authority. |

## Retained holds

| Claim or action | Status | Required before narrowing the hold |
|---|---|---|
| Redistribute the source PDF or expose its private locator | `HOLD` | Confirm rights, license, audience, and steward approval. |
| Claim current eBird, IPaC, KDWP, NRCS, SoilGrids, NHDPlus, or ScienceBase terms, endpoints, cadence, or versions | `NEEDS VERIFICATION` | Check current authoritative source material and bind an evidence snapshot. |
| Store or expose API keys, credentials, account data, or private source metadata | `HOLD` | Approved secret-management and least-privilege process; never place secrets in this record. |
| Publish exact sensitive taxa or occurrence coordinates | `DENY/HOLD` | Sensitivity authority, rights, policy decision, approved generalization or access lane, evidence, review, and release state. |
| Apply coordinate jitter, rounding, or HUC aggregation | `HOLD` | Accepted transform semantics, deterministic parameters, disclosure, policy obligations, validation, receipt, sensitivity review, and rollback. |
| Assert a Permanent Identifier/COMID relationship or ScienceBase lineage | `HOLD` | Versioned crosswalk source, checksum, retrieval evidence, relationship validation, ambiguity handling, and steward review. |
| Activate materiality thresholds for area, density, taxon status, mukey coverage, or hydrologic-group shift | `HOLD` | An owning policy decision, units and scope, positive/negative fixtures, review duties, and rollback semantics. |
| Build or publish fauna, soil, or hydrography derivatives or PMTiles/COGs | `HOLD` | Source admission, rights, sensitivity, provenance, validation, catalog closure, proof, review, release, correction, and rollback. |
| Resolve the quarantined placement card | `HOLD` | A separate Directory Rules/ADR decision; this source map cannot authorize file homes. |

## Unsafe transfers deliberately rejected

- No atlas proposal becomes a current repository fact because a similarly named surface exists.
- No vendor/source identifier is treated as canonical KFM identity without the owning contract and evidence.
- No exact species location, protected-taxa record, contributor identity, credential, or private query is copied.
- No generated summary, workflow result, fixture, receipt, hash, or catalog row becomes proof or release approval.
- No current endpoint, terms-of-use, cadence, DOI, ScienceBase version, checksum, or source availability is asserted from the atlas.
- No public client is authorized to read RAW, WORK, QUARANTINE, restricted, canonical/internal, or unreleased stores.
- No contract, schema, policy, connector, pipeline, transform, validator, receipt, proof, release, or UI implementation is added by this reconciliation.

## Validation and rollback

Preparation checks:

- the Drive-readable source scan returned exactly 61 unique Pass 24 IDs with the class counts recorded above;
- the inventory accounts for all 61 IDs and preserves the one quarantined card;
- the exact proposed path, title, and branch were collision-checked against the pinned repository state;
- every explicit relative link and repository anchor resolved on the pinned snapshot;
- the document has one MetaBlock v2 opening/closing pair and one H1;
- the document contains no Drive URL, private locator, credentials, source payload, exact sensitive location, executable policy, schema, runtime code, data mutation, or release action;
- the proposed change is one additive documentation file with no source, data, runtime, release, or publication effect.

Before merge, hosted exact-head checks and human documentation, source, evidence, sensitivity, security, and release review remain `NEEDS VERIFICATION`.

Rollback is one-file and non-operational: close the draft and delete its branch before merge, or revert the single additive commit after merge. Either action removes only this reconciliation record and leaves sources, contracts, schemas, policies, data, receipts, proofs, releases, applications, and public products unchanged.
