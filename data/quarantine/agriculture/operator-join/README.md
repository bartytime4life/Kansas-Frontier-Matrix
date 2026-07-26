<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/quarantine/agriculture/operator-join/readme
name: Agriculture Operator Join Quarantine README
path: data/quarantine/agriculture/operator-join/README.md
type: data-quarantine-lane-readme
version: v0.2.0
status: draft
owners:
  - "NEEDS VERIFICATION: agriculture domain steward"
  - "NEEDS VERIFICATION: policy steward"
  - "NEEDS VERIFICATION: rights and privacy reviewers"
created: 2026-06-27
updated: 2026-07-26
policy_label: restricted-review
truth_posture: cite-or-abstain
lifecycle_phase: quarantine
responsibility_root: data/
domain: agriculture
artifact_family: held-agriculture-operator-joins
sensitivity_posture: deny-by-default; private-farm-operator-parcel-joins-fail-closed; named-agreement-or-review-required; no-publication-without-review
related:
  - ../field-level-claim/README.md
  - ../proprietary/README.md
  - ../../README.md
  - ../README.md
  - ../../../README.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../docs/adr/ADR-0021-quarantine-has-structured-exit-paths.md
  - ../../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../../docs/domains/agriculture/CANONICAL_PATHS.md
  - ../../../../docs/domains/agriculture/SENSITIVITY.md
  - ../../../../docs/domains/agriculture/DATA_LIFECYCLE.md
  - ../../../../docs/domains/agriculture/LIFECYCLE.md
  - ../../../../docs/domains/agriculture/ARCHITECTURE.md
  - ../../../../docs/domains/agriculture/CROSS_LANE.md
  - ../../../../docs/domains/agriculture/SOURCE_REGISTRY.md
  - ../../../../docs/domains/agriculture/VERIFICATION_BACKLOG.md
  - ../../../../docs/runbooks/agriculture/PROMOTION_RUNBOOK.md
  - ../../../../docs/runbooks/agriculture/ROLLBACK_RUNBOOK.md
  - ../../../../release/manifests/README.md
tags:
  - kfm
  - data
  - quarantine
  - agriculture
  - operator-join
  - farm-operator
  - parcel-join
  - privacy
  - rights
  - deny-by-default
  - review-required
  - evidence-first
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_commit: 59194561bc6f0813fe6fb3cc505d042747c86948
  prior_blob: 0616ef1f203df0524645fb2ca734eb76a719920c
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  adr_0029_blob: cd044a38047cc9b3725d2e083eb201eb86109308
  inspection_date: 2026-07-26
notes:
  - "This README documents a nested quarantine boundary; it does not create policy, proof, receipt, catalog, registry, release, publication, or access authority."
  - "The repository is public. No-public-path means no ordinary runtime or client consumption; it does not make committed repository content private."
  - "Directory Rules v2 is adopted through accepted ADR-0029 at this evidence snapshot. The source file's PROPOSED_FOR_ADOPTION label remains part of the exact pinned artifact bytes."
  - "Actual payload presence, accepted lane-specific exit contracts, policy automation, validator wiring, owner assignment, retention rules, and end-to-end enforcement remain UNKNOWN or NEEDS VERIFICATION as stated below."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Agriculture Operator Join Quarantine

Hold identity-bearing Agriculture joins until source role, rights, agreement, sensitivity, privacy, evidence, review, correction, and rollback obligations are resolved.

[![Status: draft](https://img.shields.io/badge/status-draft-f59e0b?style=flat-square)](#status-and-evidence)
[![Lifecycle: quarantine](https://img.shields.io/badge/lifecycle-quarantine-b42318?style=flat-square)](../../README.md)
[![Access: no public path](https://img.shields.io/badge/access-no%20public%20path-b42318?style=flat-square)](#exposure-and-sensitivity-boundary)
[![Truth posture: cite or abstain](https://img.shields.io/badge/truth-cite%20or%20abstain-1a7f37?style=flat-square)](#status-and-evidence)

> [!CAUTION]
> This GitHub repository is public. "No public path" means quarantined material must not feed ordinary APIs, maps, reports, stories, indexes, UI, or AI answers. It does **not** make repository content private. Never commit restricted operator, farm, parcel, field, well, agreement, personal, precise-location, or proprietary payloads here. Use an approved restricted system and retain only permitted public-safe pointers, digests, and review metadata.

**Quick navigation:** [Scope](#scope) · [Repository fit](#repo-fit) · [Held material](#held-material) · [Exposure boundary](#exposure-and-sensitivity-boundary) · [Inputs](#inputs) · [Outputs](#outputs-mutation-and-retention) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Shortcuts](#forbidden-shortcuts) · [Required checks](#required-checks-before-use) · [Validation](#validation-and-maintenance) · [Review](#review-burden-and-rollback) · [Status](#status-and-evidence) · [Related files](#related-files)

## Scope

This lane documents the hold boundary when an Agriculture join connects, implies, or may re-identify a farm, operator, parcel, field, well, practice, yield, agreement, account, facility, supply-chain relation, or other private operational context.

The operator or identity-bearing join must be the controlling quarantine reason. Route the material to a sibling lane when another reason owns the hold:

- [`../field-level-claim/`](../field-level-claim/README.md) for field-level claims without an identity-bearing join as the primary concern;
- [`../proprietary/`](../proprietary/README.md) for agreement-bound, producer-supplied, research-collaboration, yield, or other proprietary material when proprietary status is the primary concern.

Quarantine preserves a reviewable state. It is not processed truth, operator truth, parcel truth, catalog truth, proof, release authority, a private storage system, or a staging shortcut to publication.

## Repo fit

| Field | Bounded result |
| --- | --- |
| Path | `data/quarantine/agriculture/operator-join/` |
| Inherited parent | `data/quarantine/agriculture/` |
| Responsibility root | `data/` |
| Lifecycle phase | `quarantine/` |
| Scope | Agriculture operator and identity-bearing joins |
| README profile | Sensitive `BOUNDARY_COMPACT` lane under adopted Directory Rules v2 |
| Document role | Boundary, routing, and reviewer guidance |
| Public-repository posture | README and public-safe metadata only; restricted payloads require approved restricted storage |
| Runtime/public-client posture | No ordinary API, UI, map, report, story, index, or AI-answer consumption |
| Exit posture | Remain held unless the applicable evidence, policy, review, receipt, correction, and rollback requirements close |
| Release authority | `release/`, not this directory |
| Proof and receipt authority | `data/proofs/` and `data/receipts/`, not this directory |
| Catalog and triplet authority | `data/catalog/` and `data/triplets/`, not this directory |
| Registry authority | `data/registry/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Owner assignment | **NEEDS VERIFICATION** |
| Recursive payload inventory | **UNKNOWN** |
| Lane-specific executable enforcement | **UNKNOWN**; the inspected Agriculture workflow is an explicit readiness hold |
| Directory Rules relationship | Exact v2 bytes are adopted by accepted ADR-0029; the source artifact's internal proposal label remains unchanged |

The accepted placement basis is the `data/` quarantine responsibility boundary, including `DIR-DATA-003`, `DIR-PLACE-002`, `DIR-PLACE-007`, `DIR-STORAGE-003`, and the sensitive-boundary README profile in Directory Rules v2. This same-path documentation update creates no new lane or authority.

## Held material

The rows below identify review triggers and routing guidance. They do not prove that a payload exists or that executable policy currently enforces the documented Agriculture posture.

| Held family | Why it is held | Routing note |
| --- | --- | --- |
| Private farm/operator x parcel join | May identify an operator, private parcel relationship, or operational footprint. | Draft Agriculture guidance treats this as deny-default; executable enforcement remains open under `AG-VB-03`. |
| Field/operator or field/parcel join | Can turn generalized or modeled field context into identity-bearing operational detail. | Keep here when the join is the primary risk; otherwise use `field-level-claim/`. |
| Well/field/operator join | Combines operational identity, infrastructure or water context, and location precision. | Apply the most restrictive applicable posture and verify cross-domain review. |
| Practice, application, irrigation, or yield/operator join | May reveal private, agreement-bound, or commercially sensitive activity. | Route to `proprietary/` when rights or agreement restrictions are the controlling hold. |
| Research participant, producer, account, address, or facility join | May expose personal, contractual, or private operational relationships. | Record only public-safe hold metadata in Git. |
| Supply-chain or operator-chain join | May reveal non-public commercial relationships or dependencies. | Keep held until source role, rights, audience, purpose, and review are explicit. |
| Generated, inferred, or probabilistic linkage | A model or heuristic can create a persuasive but unsupported identity claim. | Preserve derivation and uncertainty; never relabel as observed or administrative truth. |
| Map, report, story, graph, search, vector-index, or AI candidate using a held join | A downstream carrier can amplify re-identification or unsupported authority. | Keep out of public and retrieval surfaces until governed evidence and release closure. |

## Exposure and sensitivity boundary

Adopted Directory Rules v2 prohibits ordinary public consumers from reading QUARANTINE and prohibits path placement from making sensitive material public-safe. It also requires restricted bytes to remain outside ordinary Git storage unless separately approved and controlled.

The Agriculture-specific sources below remain `draft` and `AG-VB-03` remains `NEEDS VERIFICATION`. They are evidence of documented review posture, not proof of accepted machine policy or runtime enforcement.

| Situation | Review posture documented in draft Agriculture guidance | Current implementation claim |
| --- | --- | --- |
| Private farm/operator x parcel join | T4 / deny-default; the most-restrictive applicable row wins | **NEEDS VERIFICATION** under `AG-VB-03` |
| Producer-supplied or research-collaboration operator record | Named agreement and restricted audience may be required | **NEEDS VERIFICATION** |
| Operator tied to exact field, parcel, well, address, or facility context | Hold for harmful-precision, privacy, rights, and cross-domain review | **NEEDS VERIFICATION** |
| Model-derived or inferred operator linkage | Preserve source role, derivation, uncertainty, and evidence limits | **NEEDS VERIFICATION** |
| Unknown rights, agreement, consent, source role, or sensitivity | Remain held; availability does not imply permission | **CONFIRMED** fail-closed directory boundary |
| Restricted bytes in this public repository | Prohibited; retain only permitted public-safe pointers and digests | **CONFIRMED** by adopted `DIR-STORAGE-003` |

> [!IMPORTANT]
> A join table, map edge, embedding, similarity score, model output, administrative record, or generated narrative is not sovereign operator truth. Evidence, source role, uncertainty, rights, and review state remain visible; fluent language or visual precision must not increase authority.

## Inputs

Only permitted public-safe hold metadata and review material belong in this repository path, such as:

- a stable hold identifier and explicit quarantine reason;
- public-safe source references, source-role assertions, and content digests;
- a join-family description that does not identify a private person, operator, parcel, field, well, account, facility, or agreement;
- rights, consent, agreement, sensitivity, privacy, purpose, audience, and reviewer status;
- public-safe validation findings and unresolved evidence references;
- draft receipt or decision references clearly labeled as drafts, not final authority;
- correction, withdrawal, revocation, retention, and rollback dependencies;
- a pointer to approved restricted storage when policy and rights permit recording one.

Pointers must not contain credentials, signed URLs, private endpoints, personal data, stable private identifiers, or enough combined detail to reconstruct restricted content.

## Outputs, mutation, and retention

This lane may support public-safe hold metadata, review obligations, and disposition references. It does not emit final policy decisions, receipts, proofs, catalog records, release manifests, published carriers, graph edges, indexes, or AI context.

| Concern | Boundary |
| --- | --- |
| Mutation | Preserve the prior hold reason, digest, and review lineage when metadata changes; do not silently overwrite identity or history. |
| Retention | **NEEDS VERIFICATION** for each governed object; do not infer a deletion schedule from this README. |
| Legal or contractual hold | Preserve the applicable hold and approved restricted-storage record; Git placement does not satisfy retention or access control. |
| Safer derivative | Create a separately identified candidate that traverses normal WORK, validation, evidence, policy, review, release, correction, and rollback gates. |
| Disposition record | Reference the accepted contract-specific decision and canonical receipt or release family; do not invent a universal enum here. |

## Exclusions

| Do not place or claim here | Correct home or action |
| --- | --- |
| Restricted operator, farm, parcel, field, well, agreement, personal, precise-location, or proprietary payloads in this public repository | Approved restricted storage; retain only permitted public-safe pointers and digests |
| Field-level claims without an identity-bearing join as the controlling hold | [`../field-level-claim/`](../field-level-claim/README.md) |
| Agreement-bound or proprietary material as the controlling hold | [`../proprietary/`](../proprietary/README.md) |
| Clean source captures that have not triggered quarantine | `data/raw/agriculture/` or the verified source-specific intake |
| Ordinary transformation candidates with no unresolved hold | `data/work/agriculture/` |
| Validated normalized Agriculture objects | `data/processed/agriculture/` |
| Catalog records or relationship projections | `data/catalog/` or `data/triplets/` |
| EvidenceBundle, ProofPack, or final validation evidence | `data/proofs/` |
| Final process, validation, policy, AI, or release receipts | `data/receipts/` |
| Source, dataset, layer, rights, sensitivity, or crosswalk registry truth | `data/registry/` |
| Policy definitions or decision contracts | `policy/` and `contracts/` |
| Release decisions, manifests, corrections, withdrawals, or rollback cards | `release/` |
| Public layers, tiles, reports, stories, API payloads, indexes, or published artifacts | Governed `data/published/` carriers only after release closure |
| Normal UI, search, retrieval, graph, or AI-answer input | Released public-safe interfaces; otherwise abstain or deny under the applicable contract |

## Directory map

The current session confirms this README at the target path. It does not establish a recursive payload inventory. The following direct-child tree is a **PROPOSED illustrative pattern**, not a claim that a case directory exists:

```text
data/quarantine/agriculture/operator-join/
├── README.md
└── <hold_id>/    # proposed public-safe pointer, digest, and review metadata only
```

Any future case directory needs its own inherited boundary, verified contract or intake path, sensitivity review, retention decision, and repository-visibility approval. Do not create it by copying this diagram. Restricted bytes stay outside the public repository.

## Exit gates

Directory Rules v2 establishes QUARANTINE as held material with recorded remediation before a return to WORK. [`ADR-0021`](../../../../docs/adr/ADR-0021-quarantine-has-structured-exit-paths.md) proposes a more specific closed exit grammar but remains `proposed`. Until an accepted lane-specific contract and executable policy align the exact exit set, use the table below as review guidance rather than claiming implemented state-machine enforcement.

| Disposition | Minimum review evidence |
| --- | --- |
| Remain held | The unresolved reason, affected scope, next review condition, access boundary, and preservation needs remain visible. |
| Reclassify within quarantine | Another sibling lane now owns the controlling hold; preserve identity, digest, source references, and review lineage. |
| Return to WORK | The join-specific quarantine reason is resolved enough for ordinary transformation and revalidation; no public or release implication follows. |
| Advance as a PROCESSED candidate | Applicable source-role, identity, validation, rights, sensitivity, evidence, policy, and review gates close; catalog and release gates still remain. |
| Deny or restrict use | Use the finite outcome and obligations defined by the applicable accepted contract; record reason, audience, purpose, duration, revocation, and correction behavior as required. |
| Release a safer derivative | Keep the held original non-public; the derivative traverses normal processing, evidence, catalog, policy, review, release, correction, and rollback gates. |
| Correct or withdraw a downstream release | Use `release/` correction, withdrawal, invalidation, and rollback authority; never rewrite quarantine history to conceal the prior release. |

This README does not define `HOLD`, `RESTRICT`, or any other term as a universal machine enum. Contract-specific vocabularies remain separate.

## Forbidden shortcuts

The following path-only sequence is forbidden:

```text
data/quarantine/agriculture/operator-join/
→ data/processed/agriculture/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API, MapLibre, report, story, graph, index, or AI answer
```

A less restrictive state requires the applicable governed transition and inspectable evidence. A copy, rename, pull request, merge, badge, generated report, or GitHub release is not promotion or KFM publication.

```mermaid
flowchart TD
    Q["QUARANTINE<br/>held operator join"] --> R{"Join-specific hold closed?"}
    R -->|"No"| H["Remain held<br/>deny or restrict as applicable"]
    R -->|"Yes"| W["WORK<br/>remediate and revalidate"]
    W --> P["PROCESSED<br/>validated candidate"]
    P --> C["CATALOG / TRIPLET<br/>evidence closure"]
    C --> L["RELEASE<br/>decision + rollback target"]
    L --> U["PUBLISHED<br/>public-safe derivative"]
```

The diagram is a lifecycle orientation aid. It does not prove that the transitions, validators, policies, reviews, or release controls are implemented.

## Required checks before use

- [ ] Confirm the material is Agriculture-domain material and an operator or identity-bearing join is the controlling quarantine reason.
- [ ] Confirm no restricted payload, credential, signed URL, private endpoint, precise location, private identifier, or re-identifying combination would enter the public repository.
- [ ] Record the hold identifier, reason, affected scope, public-safe source references, and digest.
- [ ] Distinguish observed, administrative, aggregate, modeled, inferred, candidate, generated, and synthetic roles.
- [ ] Identify every joined object family without exposing private subjects or keys in Git.
- [ ] Verify current source terms, rights, consent, agreement, purpose, audience, attribution, redistribution, retention, and revocation posture.
- [ ] Evaluate operator, farm, parcel, field, well, address, account, facility, supply-chain, private operational, harmful-precision, and re-identification risks.
- [ ] Apply the most restrictive applicable posture when multiple sensitivity contexts intersect.
- [ ] Record required evidence, validation, policy, review, receipt, correction, withdrawal, revocation, retention, and rollback gaps.
- [ ] Confirm no public layer, tile, report, story, API payload, graph edge, search or vector index, UI surface, or AI answer consumes the held join.
- [ ] Before any exit, verify the applicable contract vocabulary and preserve prior identity, digest, hold reason, source role, derivation, and review lineage.

## Validation and maintenance

For this README, validate the metadata comment, single H1, heading order, explicit anchors, tables, alerts, links, badge destinations, code fences, Mermaid syntax, LF endings, final newline, and absence of sensitive content. A source-level Markdown check is not a GitHub-rendered visual inspection.

Repository-native workflow evidence is bounded:

- `.github/workflows/domain-agriculture.yml` is an explicit readiness hold; it reports that executable Agriculture validation, proof production, and release dry-run behavior are not established.
- `.github/workflows/docs-build.yml` is an explicit documentation-generator and preview hold.
- `.github/workflows/link-check.yml` is an explicit link-check implementation hold.

A green result from those held workflows does not validate this operator-join boundary, prove privacy or sensitivity enforcement, close evidence, approve release, or publish anything. No accepted lane-specific validator or complete end-to-end enforcement path was verified at the evidence snapshot.

Re-review this README when Directory Rules, ADR-0029, the quarantine contract, `AG-VB-03`, Agriculture sensitivity policy, owner assignment, validator, workflow, restricted-storage decision, payload inventory, public-consumer inventory, retention rule, correction path, or rollback procedure changes.

## Review burden and rollback

The current metadata names reviewer classes but no accountable steward assignments were verified. Before any less-restrictive disposition, resolve the reviewers required by the accepted contract, affected object families, rights or agreement terms, and cross-domain sensitivity. CODEOWNERS routing or a README owner string is not proof that review occurred.

This documentation change is reversible independently of held material because it changes only this README. Before merge, close the draft pull request and leave the branch unmerged. After merge, revert the implementation commit as a transparent documentation correction and re-run the same checks. Do not delete or rewrite held records merely to roll back prose.

<a id="status-notes"></a>

## Status and evidence

| Claim | Truth status | Evidence boundary |
| --- | --- | --- |
| This README exists at the requested path. | **CONFIRMED** | `main@59194561bc6f0813fe6fb3cc505d042747c86948`; prior blob `0616ef1f203df0524645fb2ca734eb76a719920c` |
| The repository is public. | **CONFIRMED** | GitHub repository metadata at the evidence snapshot |
| The parent quarantine READMEs and both sibling lane READMEs exist. | **CONFIRMED** | `data/quarantine/README.md`, `data/quarantine/agriculture/README.md`, `field-level-claim/README.md`, and `proprietary/README.md` |
| Directory Rules v2 is adopted as the single writable human placement authority. | **CONFIRMED** | Accepted ADR-0029 at the pinned base; exact rules blob `fd49a0b83e55cef52c1124281f093e263526898d` |
| Draft Agriculture guidance documents private farm/operator x parcel joins as deny-default and tracks `AG-VB-03`. | **CONFIRMED documentation state** | `SENSITIVITY.md` and `VERIFICATION_BACKLOG.md`; both remain `draft` |
| The documented Agriculture operator-join sensitivity posture is implemented and enforced. | **NEEDS VERIFICATION** | Policy, validator, fixture, decision, and observed-run closure were not established |
| Actual operator-join payloads or case directories exist in this subtree. | **UNKNOWN** | No recursive payload inventory was established |
| A lane-specific validator and CI enforce this exact boundary. | **UNKNOWN** | The inspected Agriculture workflow is an explicit readiness hold |
| Accountable owners and required independent reviewers are assigned. | **NEEDS VERIFICATION** | No verified assignment record was established |
| This README is not private storage, proof, policy, catalog, registry, receipt, release, publication, operator truth, UI, graph, index, or AI authority. | **CONFIRMED** | Adopted responsibility-root separation and this document's bounded role |

## Related files

Lifecycle and sibling boundaries:

- [`../field-level-claim/README.md`](../field-level-claim/README.md) - field-level claim quarantine
- [`../proprietary/README.md`](../proprietary/README.md) - proprietary material quarantine
- [`../README.md`](../README.md) - Agriculture quarantine parent
- [`../../README.md`](../../README.md) - quarantine root
- [`../../../README.md`](../../../README.md) - `data/` root

Agriculture guidance and verification:

- [`CANONICAL_PATHS.md`](../../../../docs/domains/agriculture/CANONICAL_PATHS.md)
- [`SENSITIVITY.md`](../../../../docs/domains/agriculture/SENSITIVITY.md)
- [`DATA_LIFECYCLE.md`](../../../../docs/domains/agriculture/DATA_LIFECYCLE.md)
- [`LIFECYCLE.md`](../../../../docs/domains/agriculture/LIFECYCLE.md)
- [`ARCHITECTURE.md`](../../../../docs/domains/agriculture/ARCHITECTURE.md)
- [`CROSS_LANE.md`](../../../../docs/domains/agriculture/CROSS_LANE.md)
- [`SOURCE_REGISTRY.md`](../../../../docs/domains/agriculture/SOURCE_REGISTRY.md)
- [`VERIFICATION_BACKLOG.md`](../../../../docs/domains/agriculture/VERIFICATION_BACKLOG.md)

Governance, transition, and rollback:

- [Directory Rules v2 - adopted placement standard](../../../../docs/doctrine/directory-rules.md)
- [ADR-0029 - accepted Directory Rules v2 adoption](../../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md)
- [ADR-0021 - proposed structured quarantine exits](../../../../docs/adr/ADR-0021-quarantine-has-structured-exit-paths.md)
- [`PROMOTION_RUNBOOK.md`](../../../../docs/runbooks/agriculture/PROMOTION_RUNBOOK.md)
- [`ROLLBACK_RUNBOOK.md`](../../../../docs/runbooks/agriculture/ROLLBACK_RUNBOOK.md)
- [`release/manifests/README.md`](../../../../release/manifests/README.md)

---

KFM rule: this directory is an Agriculture quarantine hold lane only. It is not private storage, source authority, proof authority, receipt authority, catalog authority, registry authority, policy authority, release authority, operator truth, public artifact authority, UI authority, graph authority, index authority, or AI truth.

[Back to top](#top)
