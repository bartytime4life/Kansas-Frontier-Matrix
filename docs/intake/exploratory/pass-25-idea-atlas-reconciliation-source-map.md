<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-25-idea-atlas-reconciliation-source-map
title: Pass 25 Idea Atlas Reconciliation Source Map
type: source-map
version: v1.0.0
status: proposed
owners: OWNER_TBD - Documentation steward; Source steward; Evidence steward; Sensitivity steward; Release steward
created: 2026-08-12
updated: 2026-08-12
owning_root: docs/
policy_label: internal; exploratory; non-authoritative; privacy-minimized
responsibility: Reconcile the connected Pass 25 atlas against current repository ownership without adopting source proposals or creating operational authority.
truth_posture: CONFIRMED connected-Drive inventory and current-repository anchors / PROPOSED non-authoritative reconciliation / NEEDS VERIFICATION human review and hosted exact-head CI
related:
  - ./README.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ./pass-25-receipt-proof-pairing-source-map.md
  - ./pass-25-station-spatial-assignment-source-map.md
  - ../../../contracts/domains/geology/production_material_change.md
  - ../../../contracts/domains/atmosphere/prescribed_burn_quality_flag.md
  - ../../../contracts/domains/hydrology/adaptive_threshold_proposal.md
  - ../../../contracts/governance/receipt_proof_pairing_assessment.md
  - ../../../contracts/common/station_spatial_assignment_assessment.md
  - ../../../policy/sensitivity/fauna/sensitive_taxa_deny.rego
tags: [kfm, intake, pass-25, habitat, stations, evidence, sensitivity, reconciliation, source-map, cite-or-abstain]
notes:
  - "The connected atlas is a non-authoritative downstream carrier; its cards do not establish source rights, implementation, release, or publication authority."
  - "The private Drive locator, PDF bytes, source body, credentials, and sensitive occurrence details are deliberately omitted."
[/KFM_META_BLOCK_V2] -->

# Pass 25 Idea Atlas Reconciliation Source Map

> **PROPOSED, NON-AUTHORITATIVE:** This record reconciles the 61 Pass 25 cards against a pinned repository snapshot. It preserves lineage, sensitivity boundaries, and explicit holds; it does not adopt the atlas, activate a source, assign a real station, or authorize publication.

## Outcome

`CONFIRMED`: the connected `KFM_Pass_25_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf` identifies itself as Pass 25, with run date 2026-05-17, and contains 61 Pass 25 card records: 20 idea, 31 programming, and 10 feature cards. Sixty are active; `KFM-P25-PROG-0031` is quarantine.

`CONFIRMED`: on repository snapshot `main@753dfe4c4d17482c51bdf90ae8f8bb93e8644d3c`, exact Pass 25 adaptations already exist for production material change, prescribed-burn quality context, drought-context threshold review, receipt/proof pairing, and station spatial assignment. Broader habitat, fauna, evidence, source-descriptor, release, and sensitivity responsibilities also have current repository owners.

`PROPOSED`: the smallest distinct addition is this pass-wide reconciliation record. The atlas does not establish a safe basis for another habitat, fauna, station, watcher, policy, or publication implementation packet.

`NEEDS VERIFICATION`: source rights and terms, current endpoints and cadence, real boundary and station versions, sensitive-taxa handling, live data quality, hosted execution, operational settings, and public-release readiness.

## Source and privacy boundary

| Field | Evidence-backed value |
|---|---|
| Source title | `KFM_Pass_25_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf` |
| Source posture | `CONFIRMED`: downstream carrier; cite-or-abstain; repository implementation recorded as unknown in the source |
| Source lineage | `CONFIRMED`: synthesized from Pass 24 plus New Ideas 4-19-26 and New Ideas 4-21-26 candidate material |
| Inventory | `CONFIRMED`: 61 unique Pass 25 stable IDs; 20 idea, 31 programming, 10 feature |
| Source status exception | `CONFIRMED`: `KFM-P25-PROG-0031` is quarantined in the source |
| Rights and license | `UNKNOWN`; the atlas records its generated-atlas license as needing verification |
| Disclosure | Title, pass, run date, stable IDs, normalized themes, and bounded reconciliation only |
| Omitted | Drive locator, private link, PDF bytes, source-body reproduction, credentials or API keys, contributor identities, and exact sensitive locations |

The Drive-readable text was scanned end to end. All 61 new-card records were enumerated, and their stable ID, class, category, status, and title were compared with current repository names and responsibilities. Source prose, source hashes, source-declared implementation status, and proposed file homes were not treated as repository evidence.

## Repository inspection boundary

The comparison was pinned to `main@753dfe4c4d17482c51bdf90ae8f8bb93e8644d3c`. Inspection covered current paths and targeted content search, recent pull-request lineage, exact proposed path/title/branch searches, and repository-wide open pull requests.

At preparation time:

- `CONFIRMED`: the exact proposed path, title, and branch were absent;
- `CONFIRMED`: no pre-existing open pull request targeted this pass-wide reconciliation;
- `CONFIRMED`: two targeted Pass 25 source maps and five exact card adaptations already existed;
- `CONFIRMED`: every explicit repository anchor in this record existed on the pinned snapshot;
- `UNKNOWN`: file presence does not prove source admission, current configuration, runtime use, policy approval, release state, or publication safety.

## Directory Rules path decision

```yaml
path_decision:
  artifact: "Pass 25 Idea Atlas Reconciliation Source Map"
  proposed_path: "docs/intake/exploratory/pass-25-idea-atlas-reconciliation-source-map.md"
  artifact_kind: "human-readable exploratory source reconciliation"
  authority_owner: "documentation intake"
  lifecycle: "non-data; exploratory intake"
  execution_role: "none"
  scope_or_id: "pass-25-idea-atlas-reconciliation"
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

This table accounts for every Pass 25 stable ID without copying the source body.

| Category | Stable IDs | Count |
|---|---|---:|
| Analytics and anomaly context | `KFM-P25-FEAT-0007`; `KFM-P25-IDEA-0001`-`0003`, `0015` | 5 |
| Catalog and source descriptors | `KFM-P25-FEAT-0003`; `KFM-P25-IDEA-0009`; `KFM-P25-PROG-0001`, `0007`-`0011` | 8 |
| Data lifecycle and provenance | `KFM-P25-FEAT-0008`; `KFM-P25-IDEA-0013`; `KFM-P25-PROG-0016`, `0020` | 4 |
| Documentation and file-home control | `KFM-P25-IDEA-0020`; `KFM-P25-PROG-0031` | 2 |
| Evidence and proof pairing | `KFM-P25-FEAT-0009`; `KFM-P25-IDEA-0017` | 2 |
| Map and renderer surfaces | `KFM-P25-FEAT-0005`; `KFM-P25-IDEA-0010`; `KFM-P25-PROG-0006`, `0024` | 4 |
| Metadata and spatial identity | `KFM-P25-IDEA-0004`, `0011`, `0014`; `KFM-P25-PROG-0025`-`0028` | 7 |
| Models, joins, and canonical variables | `KFM-P25-IDEA-0005`, `0012`; `KFM-P25-PROG-0012`-`0014`, `0021`, `0022`, `0029` | 8 |
| Pipelines, watchers, and validators | `KFM-P25-IDEA-0016`; `KFM-P25-PROG-0002`-`0005`, `0018`, `0019`, `0030` | 8 |
| Policy and sensitivity | `KFM-P25-FEAT-0010`; `KFM-P25-IDEA-0006`; `KFM-P25-PROG-0015`, `0017`, `0023` | 5 |
| Release and review handoff | `KFM-P25-FEAT-0004`; `KFM-P25-IDEA-0007`, `0018` | 3 |
| Security and monitoring posture | `KFM-P25-IDEA-0019` | 1 |
| Governed UI | `KFM-P25-FEAT-0001`, `0002`, `0006`; `KFM-P25-IDEA-0008` | 4 |
| **Total** |  | **61** |

Numeric ranges retain the fully written prefix and include both endpoints. The source remains the authority for exact card text; this inventory preserves only enough identity to prevent duplicate mining.

## Reconciliation against the pinned snapshot

Status terms are intentionally narrow:

- `REPRESENTED` means an adjacent or matching repository surface exists; it does not mean the surface is adopted, deployed, or operationally proven.
- `PARTIAL` means only part of the cluster is represented or exact semantic equivalence was not established.
- `HOLD` means no implementation or operational claim should transfer from the source without new evidence and owner review.

| Atlas cluster | Current repository anchors | Reconciliation |
|---|---|---|
| Production, burn, and drought change assessment | `contracts/domains/geology/production_material_change.md`; `contracts/domains/atmosphere/prescribed_burn_quality_flag.md`; `contracts/domains/hydrology/adaptive_threshold_proposal.md` | `REPRESENTED/PARTIAL`: exact Pass 25 card adaptations exist as bounded, inactive assessments. They do not activate sources, mutate thresholds, establish causation, or publish results. |
| Receipt/proof pairing | `contracts/governance/receipt_proof_pairing_assessment.md`; `docs/intake/exploratory/pass-25-receipt-proof-pairing-source-map.md` | `REPRESENTED`: the exact card family has a fixture-only assessment. Proof authentication, object resolution, release, and publication remain outside it. |
| Station-to-HUC12/county assignment | `contracts/common/station_spatial_assignment_assessment.md`; `docs/intake/exploratory/pass-25-station-spatial-assignment-source-map.md` | `REPRESENTED/PARTIAL`: synthetic assignment semantics exist. No real station, HUC12, county, WBD, TIGER, or source payload is asserted. |
| Habitat, fauna, and biodiversity identity | current habitat/fauna contracts, source catalogs, and validators | `PARTIAL/HOLD`: object and validation lanes exist, but no Pass 25 source suite, live join, occurrence, taxonomy resolution, or canonical-variable adoption is inferred. |
| Sensitive occurrences and access | `policy/sensitivity/fauna/sensitive_taxa_deny.rego`; current evidence-drawer semantics | `REPRESENTED/HOLD`: fail-safe policy and display boundaries exist. No exact coordinate, role grant, data-access approval, or generalization result is inferred. |
| Source descriptors, watcher cadence, and material change | current source-descriptor contracts, catalogs, watcher assessments, and runbooks | `PARTIAL/HOLD`: current source terms, endpoints, cadence, credentials, and redistribution rights remain source-specific verification work. |
| Evidence, release, correction, and review UI | current evidence, receipt, proof, release, correction, and read-only review families | `REPRESENTED/PARTIAL`: responsibility owners exist. Presence does not prove resolution, policy execution, authenticated review, promotion, release, deployment, or publication. |
| Source-proposed file homes | accepted Directory Rules v2 and ADR-0029 | `HOLD`: quarantined `KFM-P25-PROG-0031` stays quarantined. Source-proposed paths do not create or move authority. |

## Retained holds

| Claim or action | Status | Required before narrowing the hold |
|---|---|---|
| Redistribute the source PDF or expose its private locator | `HOLD` | Confirm rights, license, audience, and steward approval. |
| Claim current KGS, KDHE, Drought Monitor, NASS, NLCD, NWI, PAD-US, LANDFIRE, NEON, NatureServe, WBD, or TIGER terms, endpoints, cadence, or versions | `NEEDS VERIFICATION` | Check authoritative current source material and bind an evidence snapshot. |
| Store or expose credentials, private source metadata, or contributor identity | `HOLD` | Approved secret-management, privacy, and least-privilege process. |
| Publish exact sensitive taxa or occurrence coordinates | `DENY/HOLD` | Sensitivity authority, rights, policy decision, approved generalization or access lane, evidence, review, and release state. |
| Assign a real station or observation to a geography | `HOLD` | Versioned source and boundary snapshots, deterministic method, edge-case review, validation, receipt, and steward approval. |
| Activate watcher or materiality thresholds | `HOLD` | Owning policy decision, units and scope, positive/negative fixtures, review duties, and rollback semantics. |
| Build or publish habitat, fauna, station, or burn-risk derivatives | `HOLD` | Source admission, rights, sensitivity, provenance, validation, catalog closure, proof, review, release, correction, and rollback. |
| Resolve the quarantined placement card | `HOLD` | A separate Directory Rules/ADR decision; this source map cannot authorize file homes. |

## Validation and rollback

Preparation checks:

- the Drive-readable source scan returned exactly 61 unique Pass 25 IDs with the class counts recorded above;
- the inventory accounts for all 61 IDs and preserves the one quarantined card;
- the exact proposed path, title, and branch were collision-checked against the pinned repository state;
- every explicit relative link and repository anchor resolved on the pinned snapshot;
- the document has one MetaBlock v2 opening/closing pair and one H1;
- the document contains no Drive URL, private locator, credentials, source payload, exact sensitive location, executable policy, schema, runtime code, data mutation, or release action;
- the proposed change is one additive documentation file with no source, data, runtime, release, or publication effect.

Before merge, hosted exact-head checks and human documentation, source, evidence, sensitivity, security, and release review remain `NEEDS VERIFICATION`.

Rollback is one-file and non-operational: close the draft and delete its branch before merge, or revert the single additive commit after merge. Either action removes only this reconciliation record and leaves sources, contracts, schemas, policies, data, receipts, proofs, releases, applications, and public products unchanged.
