<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-26-idea-atlas-reconciliation-source-map
title: Pass 26 Idea Atlas Reconciliation Source Map
type: source-map
version: v1.0.0
status: proposed
owners: OWNER_TBD - Documentation steward; Source steward; Evidence steward; Sensitivity steward; Release steward
created: 2026-08-12
updated: 2026-08-12
owning_root: docs/
policy_label: internal; exploratory; non-authoritative; privacy-minimized
responsibility: Reconcile the connected Pass 26 atlas against current repository ownership without adopting source proposals or creating operational authority.
truth_posture: CONFIRMED connected-Drive inventory and current-repository anchors / PROPOSED non-authoritative reconciliation / NEEDS VERIFICATION human review and hosted exact-head CI
related:
  - ./README.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../contracts/evidence/evidence_bundle.md
  - ../../../contracts/evidence/evidence_ref.md
  - ../../../contracts/evidence/runtime_evidence_resolution.md
  - ../../../contracts/governance/evidence_resolution_record.md
  - ../../../packages/evidence-resolver/README.md
  - ../../../contracts/data/catalog_closure_packet.md
  - ../../../contracts/release/promotion_receipt.md
  - ../../../contracts/correction/correction_impact_assessment.md
  - ../../../contracts/ui/renderer_capability_profile.md
  - ../../standards/STAC_DWC_PROFILE.md
  - ../../../policy/sensitivity/fauna/sensitive_taxa_deny.rego
tags: [kfm, intake, pass-26, evidence, biodiversity, catalog, release, sensitivity, reconciliation, source-map, cite-or-abstain]
notes:
  - "The connected atlas is a non-authoritative downstream carrier; its cards do not establish source rights, implementation, release, or publication authority."
  - "The private Drive locator, PDF bytes, source body, credentials, and sensitive occurrence details are deliberately omitted."
[/KFM_META_BLOCK_V2] -->

# Pass 26 Idea Atlas Reconciliation Source Map

> **PROPOSED, NON-AUTHORITATIVE:** This record reconciles the 61 Pass 26 cards against a pinned repository snapshot. It preserves lineage, sensitivity boundaries, and explicit holds; it does not adopt the atlas, resolve evidence, activate a biodiversity source, or authorize publication.

## Outcome

`CONFIRMED`: the connected `KFM_Pass_26_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf` identifies itself as Pass 26, with run date 2026-05-17, and contains 61 Pass 26 card records: 20 idea, 31 programming, and 10 feature cards. Sixty are active; `KFM-P26-PROG-0031` is quarantine.

`CONFIRMED`: on repository snapshot `main@753dfe4c4d17482c51bdf90ae8f8bb93e8644d3c`, broad parts of the atlas are already represented by EvidenceBundle/EvidenceRef contracts and schemas, the evidence resolver, catalog-closure and promotion-receipt contracts, correction and renderer profiles, STAC/Darwin Core guidance, sensitivity policy, validators, fixtures, and read-only UI surfaces.

`PROPOSED`: the smallest distinct addition is this pass-wide reconciliation record. The atlas does not establish a safe basis for parallel evidence, catalog, release, biodiversity, policy, or runtime authority.

`NEEDS VERIFICATION`: source rights and terms, current biodiversity endpoints and cadence, taxonomy and boundary versions, consent and credential posture, sensitive-taxa handling, hosted execution, operational settings, and public-release readiness.

## Source and privacy boundary

| Field | Evidence-backed value |
|---|---|
| Source title | `KFM_Pass_26_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf` |
| Source posture | `CONFIRMED`: downstream carrier; cite-or-abstain; repository implementation recorded as unknown in the source |
| Source lineage | `CONFIRMED`: synthesized from Pass 25 plus New Ideas 4-23-26 and New Ideas 4-25-26 candidate material |
| Inventory | `CONFIRMED`: 61 unique Pass 26 stable IDs; 20 idea, 31 programming, 10 feature |
| Source status exception | `CONFIRMED`: `KFM-P26-PROG-0031` is quarantined in the source |
| Rights and license | `UNKNOWN`; the atlas records its generated-atlas license as needing verification |
| Disclosure | Title, pass, run date, stable IDs, normalized themes, and bounded reconciliation only |
| Omitted | Drive locator, private link, PDF bytes, source-body reproduction, credentials or consent material, contributor identities, and exact sensitive locations |

The Drive-readable text was scanned end to end. All 61 new-card records were enumerated, and their stable ID, class, category, status, and title were compared with current repository names and responsibilities. Source prose, source hashes, source-declared implementation status, and proposed file homes were not treated as repository evidence.

## Repository inspection boundary

The comparison was pinned to `main@753dfe4c4d17482c51bdf90ae8f8bb93e8644d3c`. Inspection covered current paths and targeted content search, recent pull-request lineage, exact proposed path/title/branch searches, and repository-wide open pull requests.

At preparation time:

- `CONFIRMED`: the exact proposed path, title, and branch were absent;
- `CONFIRMED`: no pre-existing open pull request targeted this pass-wide reconciliation;
- `CONFIRMED`: the source's major evidence, catalog, release, correction, renderer, standards, and sensitivity families had current responsibility owners;
- `CONFIRMED`: every explicit repository anchor in this record existed on the pinned snapshot;
- `UNKNOWN`: file presence does not prove source admission, current configuration, runtime use, policy approval, release state, or publication safety.

## Directory Rules path decision

```yaml
path_decision:
  artifact: "Pass 26 Idea Atlas Reconciliation Source Map"
  proposed_path: "docs/intake/exploratory/pass-26-idea-atlas-reconciliation-source-map.md"
  artifact_kind: "human-readable exploratory source reconciliation"
  authority_owner: "documentation intake"
  lifecycle: "non-data; exploratory intake"
  execution_role: "none"
  scope_or_id: "pass-26-idea-atlas-reconciliation"
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

This table accounts for every Pass 26 stable ID without copying the source body.

| Category | Stable IDs | Count |
|---|---|---:|
| Catalog and source control | `KFM-P26-FEAT-0004`, `0006`; `KFM-P26-IDEA-0005`; `KFM-P26-PROG-0025` | 4 |
| Data lifecycle and bundle linkage | `KFM-P26-FEAT-0001`; `KFM-P26-PROG-0010`, `0014` | 3 |
| Documentation and file-home control | `KFM-P26-PROG-0031` | 1 |
| Evidence identity and resolution | `KFM-P26-FEAT-0008`; `KFM-P26-IDEA-0002`, `0003`, `0006`, `0008`; `KFM-P26-PROG-0004`, `0005`, `0008`, `0011`, `0012` | 10 |
| Map and rendering profiles | `KFM-P26-FEAT-0007`, `0010`; `KFM-P26-IDEA-0018`; `KFM-P26-PROG-0029` | 4 |
| Metadata, catalog closure, and spatial spine | `KFM-P26-IDEA-0007`, `0016`; `KFM-P26-PROG-0013` | 3 |
| Models, normalization, and crosswalks | `KFM-P26-IDEA-0012`, `0015`; `KFM-P26-PROG-0019`, `0026`-`0028` | 6 |
| Pipelines, watchers, harvesting, and validators | `KFM-P26-FEAT-0005`; `KFM-P26-IDEA-0001`, `0011`, `0014`; `KFM-P26-PROG-0001`-`0003`, `0007`, `0015`, `0016`, `0018`, `0020`, `0023`, `0024`, `0030` | 15 |
| Policy, licensing, and sensitivity | `KFM-P26-IDEA-0013`, `0019`; `KFM-P26-PROG-0021`, `0022` | 4 |
| Release, correction, and proof lanes | `KFM-P26-IDEA-0004`, `0009`, `0010`, `0020`; `KFM-P26-PROG-0006` | 5 |
| Security and portable profile enforcement | `KFM-P26-IDEA-0017`; `KFM-P26-PROG-0009`, `0017` | 3 |
| Governed UI | `KFM-P26-FEAT-0002`, `0003`, `0009` | 3 |
| **Total** |  | **61** |

Numeric ranges retain the fully written prefix and include both endpoints. The source remains the authority for exact card text; this inventory preserves only enough identity to prevent duplicate mining.

## Reconciliation against the pinned snapshot

Status terms are intentionally narrow:

- `REPRESENTED` means an adjacent or matching repository surface exists; it does not mean the surface is adopted, deployed, or operationally proven.
- `PARTIAL` means only part of the cluster is represented or exact semantic equivalence was not established.
- `HOLD` means no implementation or operational claim should transfer from the source without new evidence and owner review.

| Atlas cluster | Current repository anchors | Reconciliation |
|---|---|---|
| EvidenceBundle, EvidenceRef, and runtime resolution | `contracts/evidence/evidence_bundle.md`; `contracts/evidence/evidence_ref.md`; `contracts/evidence/runtime_evidence_resolution.md`; `contracts/governance/evidence_resolution_record.md`; `packages/evidence-resolver/README.md` | `REPRESENTED/PARTIAL`: semantic, shape, resolver, fixture, and validation owners exist. Presence does not resolve a real reference, authenticate evidence, establish currentness, or authorize an answer. |
| Catalog closure across STAC, DCAT, and provenance | `contracts/data/catalog_closure_packet.md`; current catalog-closure validators and fixtures | `REPRESENTED/PARTIAL`: catalog closure has a governed owner. No biodiversity catalog, live distribution, or release is proven. |
| Promotion, proof, correction, and negative states | `contracts/release/promotion_receipt.md`; `contracts/correction/correction_impact_assessment.md`; current proof-pack and Evidence Drawer families | `REPRESENTED/PARTIAL`: decision and correction families exist. No source card becomes an applied promotion, proof, correction, or public status. |
| Rendering capability and release constraints | `contracts/ui/renderer_capability_profile.md`; current release-manifest families | `REPRESENTED/PARTIAL`: renderer capability and release identity are separate owners. No budget is adopted, measured, or bound to a real release by this map. |
| Darwin Core, STAC, biodiversity, and normalization | `docs/standards/STAC_DWC_PROFILE.md`; current biodiversity contract/schema/validator lanes | `PARTIAL/HOLD`: standards guidance and lanes exist. Live harvest, normalization equivalence, taxonomy authority, deduplication, and catalog output remain unverified. |
| HUC12, administrative, and PLSS context | current boundary, hydrology, station-assignment, and PLSS source documentation | `PARTIAL/HOLD`: contextual responsibilities exist. No live overlap, crosswalk, corner, line, parcel, or legal-land claim is inferred. |
| License, consent, and sensitive taxa | `policy/sensitivity/fauna/sensitive_taxa_deny.rego`; current rights, consent, and source-descriptor families | `REPRESENTED/HOLD`: fail-safe owners exist. No credential, consent, license compatibility, source access, or public coordinate is approved. |
| Source-proposed file homes | accepted Directory Rules v2 and ADR-0029 | `HOLD`: quarantined `KFM-P26-PROG-0031` stays quarantined. Source-proposed paths do not create or move authority. |

## Retained holds

| Claim or action | Status | Required before narrowing the hold |
|---|---|---|
| Redistribute the source PDF or expose its private locator | `HOLD` | Confirm rights, license, audience, and steward approval. |
| Claim current GBIF, iDigBio, BISON, USDA PLANTS, NatureServe, WBD, Census, or PLSS terms, endpoints, cadence, or versions | `NEEDS VERIFICATION` | Check authoritative current source material and bind an evidence snapshot. |
| Store or expose credentials, consent material, private source metadata, or contributor identity | `HOLD` | Approved secret-management, consent, privacy, and least-privilege process. |
| Publish exact sensitive taxa or occurrence coordinates | `DENY/HOLD` | Sensitivity authority, rights, policy decision, approved generalization or access lane, evidence, review, and release state. |
| Treat an EvidenceRef as resolved or a composed claim as answerable | `HOLD` | Bundle resolution, integrity, currentness, policy, sensitivity, review, and finite outcome through the governed resolver. |
| Adopt taxonomy normalization, deduplication, HUC12-admin crosswalks, or PLSS identity | `HOLD` | Versioned authorities, semantic contract, ambiguity rules, positive/negative fixtures, validation, evidence, and steward review. |
| Activate watchers, harvesters, trigger guards, or promotion writers | `HOLD` | Source admission, no-secret configuration, rights, resource budgets, no-network tests, receipts, policy, and human authorization. |
| Build or publish biodiversity or ecology derivatives | `HOLD` | Source admission, rights, sensitivity, provenance, validation, catalog closure, proof, review, release, correction, and rollback. |
| Resolve the quarantined placement card | `HOLD` | A separate Directory Rules/ADR decision; this source map cannot authorize file homes. |

## Validation and rollback

Preparation checks:

- the Drive-readable source scan returned exactly 61 unique Pass 26 IDs with the class counts recorded above;
- the inventory accounts for all 61 IDs and preserves the one quarantined card;
- the exact proposed path, title, and branch were collision-checked against the pinned repository state;
- every explicit relative link and repository anchor resolved on the pinned snapshot;
- the document has one MetaBlock v2 opening/closing pair and one H1;
- the document contains no Drive URL, private locator, credentials, consent payload, source data, exact sensitive location, executable policy, schema, runtime code, data mutation, or release action;
- the proposed change is one additive documentation file with no source, data, runtime, release, or publication effect.

Before merge, hosted exact-head checks and human documentation, source, evidence, sensitivity, security, and release review remain `NEEDS VERIFICATION`.

Rollback is one-file and non-operational: close the draft and delete its branch before merge, or revert the single additive commit after merge. Either action removes only this reconciliation record and leaves sources, contracts, schemas, policies, data, receipts, proofs, releases, applications, and public products unchanged.
