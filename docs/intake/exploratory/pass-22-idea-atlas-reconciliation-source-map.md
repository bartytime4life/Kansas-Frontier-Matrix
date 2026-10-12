<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-22-idea-atlas-reconciliation-source-map
title: Pass 22 Idea Atlas Reconciliation Source Map
type: source-map
version: v1.0.0
status: proposed
owners: OWNER_TBD - Documentation steward; Evidence steward; Release steward; Security steward; Applications steward
created: 2026-08-11
updated: 2026-08-11
policy_label: internal; exploratory; non-authoritative; privacy-minimized
related:
  - ./README.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ./pass-22-time-series-promotion-candidate-manifest-source-map.md
  - ./pass-22-signed-bundle-timestamp-evidence-source-map.md
  - ../../../contracts/data/catalog_matrix_closure_profile.md
  - ../../../contracts/governance/receipt_proof_pairing_assessment.md
  - ../../../contracts/release/signed_rollback_token.md
  - ../../../contracts/evidence/verifier_capability_portability.md
  - ../../../apps/explorer-web/src/features/promotion_gate_status_board/README.md
tags: [kfm, intake, pass-22, idea-atlas, reconciliation, source-map, cite-or-abstain]
notes:
  - "The connected atlas is a non-authoritative downstream carrier; its cards do not establish repository behavior, adoption, release, or publication authority."
  - "The private Drive locator, PDF bytes, connector metadata, and source body are deliberately omitted."
[/KFM_META_BLOCK_V2] -->

# Pass 22 Idea Atlas Reconciliation Source Map

> **PROPOSED, NON-AUTHORITATIVE:** This record reconciles the 61 Pass 22 cards against a pinned repository snapshot. It preserves lineage and explicit holds; it does not adopt the atlas, create implementation authority, or prove that any represented surface ran in a hosted environment.

## Outcome

`CONFIRMED`: the connected `KFM_Pass_22_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf` identifies itself as Pass 22, with run date 2026-05-17, and contains 61 Pass 22 card records: 6 idea, 53 programming, and 2 feature cards. Sixty are marked active; `KFM-P22-PROG-0053` is marked quarantine.

`CONFIRMED`: on repository snapshot `main@c142130cd5d0d33c8e18a13a5281d5c86cecfb5d`, broad parts of the atlas are already represented by contracts, schemas, validators, fixtures, runbooks, source maps, and a display-only UI projection. Two exact Pass 22 card-family source maps already exist for the time-series promotion candidate manifest and signed-bundle timestamp evidence.

`PROPOSED`: the smallest distinct repository addition is this pass-wide reconciliation record. Creating another broad implementation packet from the atlas would collide with existing responsibilities and would turn source proposals into apparent repository authority.

`NEEDS VERIFICATION`: operational deployment, hosted exact-head execution, external service currentness, source rights, live data availability, repository settings, and public-release readiness.

## Source and privacy boundary

| Field | Evidence-backed value |
|---|---|
| Source title | `KFM_Pass_22_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf` |
| Source posture | `CONFIRMED`: downstream carrier; cite-or-abstain; repository implementation recorded as unknown in the source |
| Inventory | `CONFIRMED`: 61 unique Pass 22 stable IDs; 6 idea, 53 programming, 2 feature |
| Source status exception | `CONFIRMED`: `KFM-P22-PROG-0053` is quarantined in the source |
| Rights and license | `UNKNOWN`; no permission or redistribution claim is inferred |
| Disclosure | Title, pass, run date, stable IDs, normalized themes, and bounded reconciliation only |
| Omitted | Drive locator, private link, PDF bytes, connector metadata, source-body reproduction, and source-internal person or account metadata |

The Drive-readable text was scanned end to end. All 61 new-card records were enumerated, and their stable ID, category, status, title, and normalized statement were compared with current repository names and responsibilities. The scan did not treat source prose, source hashes, or source-declared implementation status as repository evidence.

## Repository inspection boundary

The repository comparison was pinned to `main@c142130cd5d0d33c8e18a13a5281d5c86cecfb5d`. Inspection covered current paths and targeted content search, recent pull-request lineage, exact proposed path/title/branch searches, and repository-wide open pull requests.

At preparation time:

- `CONFIRMED`: the proposed path and branch name were absent;
- `CONFIRMED`: the repository had no open pull requests or drafts;
- `CONFIRMED`: only two Pass 22-named targeted source maps were present under `docs/intake/exploratory/`;
- `CONFIRMED`: representative repository surfaces below existed on the pinned snapshot;
- `UNKNOWN`: file presence alone does not prove deployment, production use, current configuration, policy approval, or release readiness.

## Directory Rules path decision

```yaml
path_decision:
  artifact: "Pass 22 Idea Atlas Reconciliation Source Map"
  proposed_path: "docs/intake/exploratory/pass-22-idea-atlas-reconciliation-source-map.md"
  artifact_kind: "human-readable exploratory source reconciliation"
  authority_owner: "documentation intake"
  lifecycle: "non-data; exploratory intake"
  execution_role: "none"
  scope_or_id: "pass-22-idea-atlas-reconciliation"
  exposure: "privacy-minimized internal documentation"
  mutability: "versioned Git document"
  evidence:
    - "ADR-0029 accepts the pinned Directory Rules v2 bytes"
    - "docs/intake/exploratory/README.md defines this lane as non-canonical intake"
    - "the proposed exact path is absent on the inspected main snapshot"
  cited_rules:
    - "DIR-SIGNATURE-001"
    - "DIR-PLACE-001"
  outcome: "PLACE"
```

The artifact has one owner and one responsibility: human-readable intake reconciliation. It does not create a machine source identity, schema, contract, policy, receipt, proof, release decision, or new root. The existing exploratory lane is used because its README admits non-canonical idea packets awaiting classification and evidence.

## Complete card inventory by category

This table accounts for every Pass 22 stable ID without copying the source body.

| Category | Stable IDs | Count |
|---|---|---:|
| Catalog | `KFM-P22-IDEA-0003`; `KFM-P22-PROG-0005`, `0030` | 3 |
| Data lifecycle and receipts | `KFM-P22-PROG-0014`, `0020`, `0026`, `0034`, `0045`, `0046`, `0049` | 7 |
| Documentation | `KFM-P22-PROG-0017`, `0018` | 2 |
| Evidence | `KFM-P22-IDEA-0002`; `KFM-P22-PROG-0003`, `0036`, `0050` | 4 |
| Mapping and geometry | `KFM-P22-PROG-0011`, `0041`, `0042` | 3 |
| Metadata and provenance | `KFM-P22-PROG-0002`, `0016`, `0037`, `0038`, `0039` | 5 |
| Modeling and responsibility | `KFM-P22-IDEA-0005`; `KFM-P22-PROG-0051`, `0053` | 3 |
| Pipelines and validators | `KFM-P22-PROG-0001`, `0006`, `0008`, `0010`, `0022`, `0031`, `0035`, `0043`, `0044`, `0047` | 10 |
| Policy | `KFM-P22-PROG-0007`, `0015`, `0021`, `0032`, `0048` | 5 |
| Release and rollback | `KFM-P22-IDEA-0004`; `KFM-P22-PROG-0012`, `0025`, `0027`, `0040` | 5 |
| Security and signing | `KFM-P22-IDEA-0001`; `KFM-P22-PROG-0004`, `0009`, `0019`, `0023`, `0024`, `0028`, `0029`, `0033`, `0052` | 10 |
| Reviewer experience | `KFM-P22-FEAT-0001`, `0002`; `KFM-P22-IDEA-0006`; `KFM-P22-PROG-0013` | 4 |
| **Total** |  | **61** |

Numeric shorthand in a row retains the prefix and class from the first fully written ID in the same semicolon-delimited group. The source remains the authority for exact card text; this map preserves only enough identity to prevent duplicate mining.

## Reconciliation against the pinned snapshot

Status terms are intentionally narrow:

- `REPRESENTED` means an adjacent or matching repository surface exists; it does not mean the surface is adopted, deployed, or proven at runtime.
- `PARTIAL` means only part of the category is represented or exact semantic equivalence was not established.
- `HOLD` means no implementation or operational claim should be transferred from the source without new evidence and owner review.

| Atlas cluster | Current repository anchors | Reconciliation |
|---|---|---|
| Catalog closure and station identity | `contracts/data/catalog_matrix_closure_profile.md`; `contracts/common/station_spatial_assignment_assessment.md` | `REPRESENTED/PARTIAL`: STAC/DCAT/PROV digest closure and station-assignment assessment exist. Live station-registry resolution and publication eligibility remain unproven. |
| Time-series candidates, receipts, and stable diffs | `contracts/data/time_series_promotion_candidate_manifest.md`; `contracts/runtime/run_receipt.md`; `docs/runbooks/STABLE_DIFF_REVIEW_HANDOFF.md` | `REPRESENTED/PARTIAL`: candidate identity, receipt semantics, and stable review summaries have repository surfaces. No live station feed, admitted batch, or executed release is inferred. |
| Documentation metadata and diagnostics | current MetaBlock-bearing documents and documentation validation surfaces | `REPRESENTED/PARTIAL`: metadata conventions are widely present. The source does not prove every document passes current validation or that diagnostics were promoted. |
| Receipts, proofs, evidence, and abstention | `contracts/governance/receipt_proof_pairing_assessment.md`; `contracts/runtime/DecisionEnvelope.md` | `REPRESENTED/PARTIAL`: separation and finite outcomes exist as repository semantics. A receipt remains process memory, not proof, approval, or publication authority. |
| Geometry and overlays | `contracts/evidence/geometry_quality_scope_assessment.md` | `REPRESENTED/PARTIAL`: bounded geometry-quality scope exists. It does not establish that any source geometry is correct, safe, current, or publishable. |
| Catalog metadata and provenance closure | `contracts/data/catalog_matrix_closure_profile.md` | `REPRESENTED/PARTIAL`: shared digest alignment is modeled. Hosted STAC, DCAT, or PROV generation and catalog closure are not proven by presence. |
| Responsibility-root separation | adopted Directory Rules v2 and accepted ADR-0029 | `REPRESENTED/HOLD`: contracts, schemas, policy, receipts, proofs, and release remain separate authorities. Quarantined `KFM-P22-PROG-0053` stays quarantined; its source-proposed homes are not adopted. |
| Promotion grammar and validators | `contracts/runtime/DecisionEnvelope.md` and bounded validators across responsibility roots | `REPRESENTED/PARTIAL`: finite decision structures and validators exist. No single broad “A-G gate” is declared complete by this map. |
| Policy gates | existing policy and decision-reference surfaces | `PARTIAL/HOLD`: policy separation and references exist. Exact station allowlists, active policy bundles, and evaluated candidate decisions require repository and runtime evidence. |
| Immutable release and rollback | `contracts/release/signed_rollback_token.md` | `REPRESENTED/PARTIAL`: signed rollback-token semantics exist. No immutable object-store write, alias mutation, rollback execution, or release approval is authorized. |
| Signing, verifier capability, and timestamp evidence | `contracts/evidence/verifier_capability_portability.md`; `contracts/release/cosign_attestation_verification_plan.md`; `contracts/release/signed_bundle_timestamp_evidence.md` | `REPRESENTED/PARTIAL`: portable capability declarations, a verification plan, and timestamp-evidence semantics exist. Live TSA, Fulcio, Rekor, OCI, OIDC, certificates, signatures, and vulnerability status remain held. |
| Reviewer display and rollback action | `apps/explorer-web/src/features/promotion_gate_status_board/README.md` | `REPRESENTED/HOLD`: a display-only status projection exists. A rollback chooser would be a governed mutation surface and is not inferred or authorized. |
| Source-specific watchers and provenance sidecars | existing source-intake, watcher, receipt, and provenance families | `PARTIAL/HOLD`: connector/watch boundaries are established generally. USFWS behavior, SensorThings/Mesonet endpoints, GEDCOM custom-tag fidelity, rights, and exact source currentness need source-specific evidence. |

## Retained holds

| Claim or action | Status | Required before narrowing the hold |
|---|---|---|
| Redistribute the source PDF or expose its private locator | `HOLD` | Confirm rights, license, audience, and steward approval. |
| Declare a current safe Cosign or verifier version | `NEEDS VERIFICATION` | Check current authoritative security and release sources plus repository pins. |
| Assert branch protection, OIDC, signed-commit, or repository-setting state | `UNKNOWN` | Inspect current settings with authorized evidence. |
| Perform live TSA, Fulcio, Rekor, OCI, registry, certificate, or signature operations | `HOLD` | Approved threat model, credentials, policy, network boundary, and recorded execution proof. |
| Publish or mutate a `spec_hash` alias, immutable store, or rollback target | `HOLD` | Authenticated release authority, separation of duties, policy decision, review, proof, receipt, and rollback plan. |
| Add a rollback chooser or other reviewer action control | `HOLD` | A governed write contract, authorization model, confirmation semantics, audit path, tests, and accepted owner review. |
| Treat live station, habitat, species, or genealogy data as admitted truth | `HOLD` | Source identity, rights, sensitivity, provenance, validation, evidence, policy, review, and release state. |
| Resolve the quarantined responsibility-home card | `HOLD` | A separate Directory Rules/ADR decision; this source map cannot authorize new homes. |

## Unsafe transfers deliberately rejected

- No source proposal becomes a current repository fact merely because a similarly named file exists.
- No generated summary, workflow result, fixture, or receipt becomes proof or release approval.
- No current package version, vulnerability state, service behavior, endpoint availability, or external trust root is asserted from the atlas.
- No private source payload, account metadata, source URL, or document hash is copied into the repository.
- No public client is authorized to read canonical, RAW, WORK, QUARANTINE, restricted, or unreleased stores.
- No geometry, station observation, species location, habitat record, genealogy record, or living-person datum is approved for publication.
- No broad contract, schema, policy, workflow, receipt, proof, release, or UI implementation is added by this reconciliation.

## Validation and rollback

Preparation checks:

- the Drive-readable source scan returned exactly 61 unique Pass 22 IDs with the class counts recorded above;
- the inventory table accounts for all 61 IDs and preserves the one quarantined card;
- the exact proposed path, title, and branch were collision-checked against the pinned repository state;
- every explicit relative repository link in the metadata block resolved on the pinned snapshot;
- the document has one MetaBlock v2 opening/closing pair and one H1;
- the document contains no Drive URL, private locator, source payload, executable policy, schema, credential, or release action;
- the proposed change is one additive documentation file and has no runtime, data, release, or publication effect.

Before merge, hosted exact-head checks and human documentation, evidence, security, release, and applications review remain `NEEDS VERIFICATION`.

Rollback is one-file and non-operational: close the draft and delete its branch before merge, or revert the single additive commit after merge. Either action removes only this reconciliation record and leaves contracts, schemas, policies, data, receipts, proofs, releases, workflows, applications, and public products unchanged.
