<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/geology/readme
title: Geology and Natural Resources Runbooks — Operational Procedure Index
type: readme
subtype: domain-runbook-boundary
version: v0.2
prior_version: v0.1 repository-grounded lane index
status: draft; repository-grounded; mixed-child-maturity; documentation-only; non-authoritative; non-publisher
owners:
  - "@bartytime4life — verified GitHub review route"
  - "NEEDS VERIFICATION — accountable Geology, Natural Resources, source, validation, policy, evidence, rights/sensitivity, release, correction, rollback, operations, and independent-review stewards"
created: 2026-08-25
updated: 2026-08-28
policy_label: public-review; geology; natural-resources; operational-documentation; sensitive-location-aware; fail-closed; no-publication-authority
current_path: docs/runbooks/geology/README.md
owning_root: docs/
responsibility: >-
  Define the human-facing boundary, navigation, inheritance, current maturity, safety posture,
  and maintenance contract for Geology and Natural Resources operational procedures without
  granting source admission, evidence, policy, lifecycle, review, release, deployment,
  promotion, rollback-execution, or publication authority.
truth_posture: cite-or-abstain
truth_labels: [CONFIRMED, PROPOSED, UNKNOWN, NEEDS VERIFICATION, CONFLICTED, HOLD]
authority_class: explanatory operational-documentation index
canonical_relationship: >-
  Same-path completion of an existing tracked one-byte file; canonical local boundary for
  docs/runbooks/geology/; no new path, sibling authority, alias, mirror, or migration.
prepared_under_prompt: KFM Repository Build-Out & Markdown Modernization Implementation Agent v6.0.0
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 35d1c6c5b1adb4130ce6c24c37da40b1e7bf9769
  target_prior_blob: 8b137891791fe96927ad78e64b0aad7bded08bdc
  parent_runbooks_readme_blob: 80f53b61d485c25acdb55eaa01129e13e63ca90e
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adoption_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  geology_domain_readme_blob: 5ed55479c776563b65275cd9bc4628266a37aedc
  bedrock_review_blob: 0582f82580c9ae082c64db8c2ab0b16da05f0dfd
  no_network_test_runbook_blob: 0477386e2814a8ae9c495c9d16533d9c13ade692
  promotion_runbook_blob: 682e144d96d28f1ab64419eb0b7dcf352545ef3e
  rollback_runbook_blob: 2932d192ec904d591becc4dd2322b3d2e67a5f4f
  source_refresh_runbook_blob: e0a6d4e39f01bc957fe4bc66b6b918a376503b18
  geology_workflow_blob: 79b6066c9dede603df328d66601fe757ae68c5b3
  source_authority_register_blob: 32729857bc8eb5001acb37b8ee8e60bcb6e0dc50
  subtype_source_registry_blob: 0bb2d794e3179186abfa371a3c99532f50d2c571
  domain_first_bedrock_descriptor_blob: bd4e74bb152f1fa3be461603e81e243ad7097e25
  domain_first_aem_descriptor_blob: 4e69fb735bdfea6dd212d6ebe8ffd76b6f6de12a
  geology_policy_blob: 71e4a939510712346c3b80e62c47d1770e799c03
  geology_proof_readme_blob: fc07012855bb4019008a3b0dce035dc8088156f6
  geology_candidate_lane_blob: f0313cafc641c049d367af82418212e0bad1fc35
guard_adoption_snapshot:
  base_commit: e52165e820b07e65c54830fde519a9c90df8eb1c
  merged_guard_pr: 3709
  shared_guard_blob: e320d3a0fb70a3273a5d11fca513628a4a479d15
drive_lineage:
  - title: KFM_Geology_Natural_Resources_Architecture_PDF_Only_Report_2026-04-21.pdf
    file_id: 1kxONABD4knMG1HYaJR740tzZ_EBrt7Ca
    sha256: d334f43df8fd74f17115cc0f51861cf8238c9cb99d37adaf95f5e4e1655fdf51
    role: planning lineage only; current repository evidence governs implementation claims
related:
  - docs/runbooks/README.md
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/domains/geology/README.md
  - docs/domains/geology/DATA_LIFECYCLE.md
  - docs/domains/geology/SENSITIVITY.md
  - docs/domains/geology/SOURCE_ROLE_MATRIX.md
  - docs/runbooks/geology/BEDROCK_REVIEW.md
  - docs/runbooks/geology/NO_NETWORK_TEST_RUNBOOK.md
  - docs/runbooks/geology/PROMOTION_RUNBOOK.md
  - docs/runbooks/geology/ROLLBACK_RUNBOOK.md
  - docs/runbooks/geology/SOURCE_REFRESH_RUNBOOK.md
  - contracts/domains/geology/README.md
  - schemas/contracts/v1/domains/geology/README.md
  - policy/domains/geology/README.md
  - fixtures/domains/geology/README.md
  - tests/domains/geology/README.md
  - tools/validators/domains/geology/README.md
  - tools/validators/geology/README.md
  - data/registry/sources/geology/README.md
  - data/registry/geology/sources/README.md
  - data/proofs/geology/README.md
  - release/candidates/geology/README.md
  - .github/CODEOWNERS
  - .github/workflows/domain-geology.yml
tags: [kfm, geology, natural-resources, runbooks, operations, validation, source-refresh, promotion, rollback, bedrock, evidence, sensitivity, fail-closed]
notes:
  - "The prior target was a tracked one-byte file. This edition adds the missing BOUNDARY_COMPACT local contract without moving or renaming a procedure."
  - "BEDROCK_REVIEW.md, NO_NETWORK_TEST_RUNBOOK.md, and ROLLBACK_RUNBOOK.md are repository-grounded drafts; PROMOTION_RUNBOOK.md and SOURCE_REFRESH_RUNBOOK.md retain proposal-era assumptions and require their own reconciliation."
  - "The Geology workflow truthfully names four bounded profiles and loads the merged shared named-public-API Python startup guard for each profile command; Geology owns a fresh-process activation and representative-denial proof."
  - "The machine source-authority projection is PROPOSED, implementation_status ABSENT, and empty; source-registry topology remains conflicted between subtype-first and domain-first lanes."
  - "The parent docs/runbooks/README.md carries a historical inventory snapshot that predates this local boundary completion; a later whole-tree reconciliation should refresh it."
  - "This document changes no source, connector, contract, schema, policy, fixture, validator, test, workflow, evidence object, lifecycle object, release record, deployment, promotion, rollback execution, or publication state."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Geology and Natural Resources Runbooks — Operational Procedure Index

> **Start here for Geology and Natural Resources bedrock review, no-network validation, source refresh, promotion, rollback, withdrawal, and recovery procedures.** This directory explains how an authorized actor should proceed; it does not create the authority, evidence, policy decision, review state, release decision, operational capability, or public state that a procedure depends on.

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#current-repository-state)
[![Procedure files: 5](https://img.shields.io/badge/procedure%20files-5-0969da?style=flat-square)](#direct-child-map)
[![Repository-grounded procedures: 3](https://img.shields.io/badge/repository--grounded-3-1f883d?style=flat-square)](#current-repository-state)
[![No-network profiles: 4 bounded](https://img.shields.io/badge/no--network%20profiles-4%20bounded-1f883d?style=flat-square)](#validation-and-rehearsal-boundary)
[![Broader operations: HOLD](https://img.shields.io/badge/broader%20operations-HOLD-d4a72c?style=flat-square)](#current-repository-state)
[![Publisher: no](https://img.shields.io/badge/publisher-no-6e7781?style=flat-square)](#authority-and-negative-authority)

> [!IMPORTANT]
> **Runbooks are instruction surfaces, not authority surfaces.** A runbook may name a `SourceDescriptor`, `EvidenceBundle`, `PolicyDecision`, `ReviewRecord`, `PromotionDecision`, `ReleaseManifest`, `CorrectionNotice`, `RollbackCard`, validator result, or workflow conclusion. It cannot create, approve, replace, or execute those objects by prose alone.

> [!CAUTION]
> **This lane has mixed maturity.** Bedrock review, bounded no-network testing, and rollback have been reconciled against current repository evidence. Promotion and source refresh still contain placeholder ownership, proposed paths, and no-mounted-repository assumptions. Treat those two documents as planning procedures until each receives a repository-grounded update.

> [!WARNING]
> **Exact or reverse-engineerable subsurface, private-well, well-log, core, sample, geochemistry, sensitive-resource, operator/parcel, extraction-targetable, infrastructure, archaeology, or land/title detail fails closed by default.** Do not use a map style, filter, test fixture, Markdown statement, or generated summary as a substitute for rights review, sensitivity policy, generalization, redaction, quarantine, staged access, abstention, or denial.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-and-negative-authority) · [Placement](#placement-and-canonical-relationship) · [State](#current-repository-state) · [Children](#direct-child-map) · [Start here](#start-here) · [Lifecycle](#lifecycle-and-state-separation) · [Belongs](#what-belongs-here) · [Prohibited](#what-does-not-belong-here) · [Inputs and outputs](#inputs-outputs-and-permitted-actors) · [Safety](#geology-specific-safety-rules) · [Outcomes](#finite-outcomes-and-stop-conditions) · [Validation](#validation-and-rehearsal-boundary) · [Maintenance](#maintenance-and-review-triggers) · [Open work](#open-verification-backlog) · [Related](#related-surfaces) · [Evidence](#evidence-basis) · [Rollback](#document-change-rollback)

---

## Purpose

`docs/runbooks/geology/` is the Geology and Natural Resources domain lane inside KFM's human-readable operational-procedure root. It helps maintainers, reviewers, stewards, developers, and operators answer bounded questions such as:

- Which Geology procedure applies to the current candidate, source signal, validation result, release concern, or recovery state?
- Is the procedure repository-grounded, proposal-era, executable, held, conflicted, or unverified?
- Which source identity, rights, sensitivity, evidence, policy, review, release, correction, and rollback prerequisites must resolve before an action begins?
- Which operation belongs to a validator, workflow, connector, source registry, pipeline, policy evaluator, proof builder, review authority, release system, or deployment mechanism rather than Markdown?
- Which finite outcome should stop the procedure, preserve the prior state, quarantine unsafe material, abstain from a claim, deny exposure, or escalate for accountable review?
- Which records must remain inspectable after replay, correction, supersession, withdrawal, or rollback?

The directory is documentation-first. Executable behavior and trust-bearing objects remain in their owning responsibility roots. The runbooks should make the governed path usable without embedding a second source registry, semantic contract, machine schema, policy engine, evidence store, proof system, release plane, or publication mechanism in documentation.

The planning corpus supplies durable domain principles—source-role discipline, public-safe geometry, separate accountability object families, bounded AI, and fixture-first proof—but it was written without a mounted repository. Current repository bytes, accepted decisions, contracts, schemas, policy, tests, workflows, and generated evidence therefore govern claims about present implementation.

[Back to top](#top)

---

## Authority and negative authority

Accepted [`ADR-0029`](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts the exact Directory Rules v2 bytes at [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md). Those rules place human operational procedures under `docs/runbooks/`, require a compact local README where ownership, exposure, mutation, generation, or lifecycle behavior changes, and require directory maps to show only the governed directory and its direct children.

| Concern | Owning authority | This directory's role |
|---|---|---|
| Documentation placement and inheritance | Accepted Directory Rules plus the parent [`docs/runbooks/` contract](../README.md) | Define the Geology procedure boundary and disclose current drift |
| Geology domain meaning | [`docs/domains/geology/`](../../domains/geology/) plus semantic contracts | Orient readers; do not redefine domain truth |
| Object meaning | `contracts/` | Cite semantics; do not restate a competing contract |
| Machine shape | `schemas/` | Cite versions and fields; do not host schema authority |
| Allow, restrict, hold, abstain, deny, or error | `policy/` plus required review | Explain how to obtain and respond to a decision |
| Source identity and admission | `SourceDescriptor`, source-registry, and source-authority controls | Describe safe handling; do not admit or activate a source |
| Evidence and citations | `EvidenceRef`, `EvidenceBundle`, receipts, and proofs | Require resolvable support; do not manufacture evidence |
| Executable behavior | `tools/`, `pipelines/`, `connectors/`, packages, applications, runtime, scripts, and workflows according to role | Point to reviewed entry points and interpret bounded outcomes |
| Lifecycle instances | Governed `data/` phases and accountability families | Describe a transition; do not perform one by file movement |
| Promotion, release, correction, withdrawal, rollback | `release/` and linked accountability objects | Explain the authorized procedure; do not approve or execute it |
| This README | Human navigation, inheritance, maturity disclosure, and maintenance contract | No source, policy, evidence, review, release, deployment, promotion, rollback-execution, or publication authority |

A procedure must stop when its named authority, identity, permission, evidence, policy, review, or rollback target is unresolved. A README cannot convert `UNKNOWN`, `NEEDS VERIFICATION`, `CONFLICTED`, or `HOLD` into permission.

[Back to top](#top)

---

## Placement and canonical relationship

**Placement outcome: `PLACE` — CONFIRMED for this same-path completion.**

| Property | Current result |
|---|---|
| Path | `docs/runbooks/geology/README.md` |
| README profile | `BOUNDARY_COMPACT` |
| Owning root | `docs/` — human-readable operational documentation |
| Scope | Geology and Natural Resources domain runbook lane |
| Prior path state | Existing tracked one-byte file at blob `8b137891…` |
| Structural effect | None; no create, move, rename, split, mirror, alias, compatibility lane, or delete |
| Authority effect | None; documents existing boundaries and current evidence |
| Review route | `@bartytime4life` through the repository default CODEOWNERS rule |
| Accountable and independent stewardship | `NEEDS VERIFICATION` |
| Release and publication effect | None |

This README is the canonical local boundary for the procedure files in this directory. The domain landing page at [`docs/domains/geology/README.md`](../../domains/geology/README.md) explains the Geology domain more broadly; it does not become a second writable procedure authority.

The parent [`docs/runbooks/README.md`](../README.md) retains a repository-wide inventory snapshot pinned to an earlier commit. Its earlier domain-lane README count predates this completion. That historical snapshot should be refreshed through a later whole-tree inventory reconciliation, not silently rewritten in this lane-local change.

[Back to top](#top)

---

## Current repository state

The observations below are pinned to `main@35d1c6c5b1adb4130ce6c24c37da40b1e7bf9769`. They describe tracked bytes and bounded executable evidence. They do not establish live source operation, operational admission, release readiness, deployment, or publication.

| Surface | CONFIRMED evidence at the pinned revision | Bounded conclusion |
|---|---|---|
| This README | Existing tracked file contains only a newline | Local lane boundary is absent in substance |
| Direct procedure packet | Five tracked procedure files plus this README | A stable five-procedure documentation packet exists |
| [`BEDROCK_REVIEW.md`](./BEDROCK_REVIEW.md) | Repository-grounded v0.1 draft; fixture-first candidate-review and handoff procedure | Useful for an immutable bedrock candidate or fixture packet; default disposition remains `HOLD` without complete prerequisites |
| [`NO_NETWORK_TEST_RUNBOOK.md`](./NO_NETWORK_TEST_RUNBOOK.md) | Repository-grounded v0.3 draft; four bounded synthetic profiles under the shared Python startup guard | Useful for exact bounded profiles; broader Geology validation and operational maturity remain `HOLD` |
| [`ROLLBACK_RUNBOOK.md`](./ROLLBACK_RUNBOOK.md) | Repository-grounded v0.2 draft; shared `RollbackCard` candidate validation and marker-protected synthetic rehearsal are present | Candidate shape and synthetic recovery behavior are bounded; production rollback and public-state mutation remain separate and held |
| [`PROMOTION_RUNBOOK.md`](./PROMOTION_RUNBOOK.md) | v1 draft with placeholder owners/dates, proposed paths, and proposal-era implementation statements | Planning reference only until repository-grounded reconciliation |
| [`SOURCE_REFRESH_RUNBOOK.md`](./SOURCE_REFRESH_RUNBOOK.md) | v1 draft with proposed path alternatives, hypothetical watcher/receipt flows, and no-mounted-repository assumptions | Planning reference only; it does not admit, activate, schedule, or fetch a live source |
| [`domain-geology`](../../../.github/workflows/domain-geology.yml) | Read-only workflow executes four bounded profiles with the shared Python startup guard and a Geology-owned fresh-process proof; broader proof and release producers remain held | Current executable boundary is four named profiles plus bounded named-public-API egress denial |
| Machine source-authority projection | `control_plane/source_authority_register.yaml` is `PROPOSED`, projection-only, implementation status `ABSENT`, completeness `empty`, and has no entries | No source authority is established by the machine projection |
| Source-registry topology | Subtype-first `data/registry/sources/geology/` and domain-first `data/registry/geology/sources/` both exist; domain-first YAMLs include proposed templates and disabled records | Topology and canonical writer remain `CONFLICTED`; file presence is not source admission |
| Geology policy | Geology policy README reports default-only scaffolds and an unbound evaluator | Active Geology policy evaluation is not established |
| Geology proof support | Shared EvidenceBundle support exists; Geology-specific closure, resolver integrity, policy coupling, and release linkage remain bounded | Proof readiness is not established by documentation or shared fixtures alone |
| Release candidates | `release/candidates/geology/` contains only its README | No child Geology release-candidate dossier is established |
| Live sources, operational promotion, rollback execution, deployment, publication | Not established by this directory or the inspected current evidence | `UNKNOWN` or `HOLD` until owning surfaces provide exact-revision evidence |

### Current bounded no-network profiles

1. Resource-class and source-role anti-collapse.
2. Announcement-bound GMD 3 AEM campaign-candidate validation.
3. Metadata-only public-safe-geometry assessment.
4. Production material-change assessment.

These profiles prove only their named fixtures, validators, and test assertions at the exact tested revision. They do not establish geologic truth, source admission, rights clearance, evidence closure, policy approval, review completion, release, deployment, promotion, or publication.

[Back to top](#top)

---

## Direct-child map

Directory Rules require a lane README to show the directory it governs and its direct children, not a speculative repository tree.

```text
docs/runbooks/geology/
├── README.md
├── BEDROCK_REVIEW.md
├── NO_NETWORK_TEST_RUNBOOK.md
├── PROMOTION_RUNBOOK.md
├── ROLLBACK_RUNBOOK.md
└── SOURCE_REFRESH_RUNBOOK.md
```

| Child | Primary question | Current documentation posture | Use boundary |
|---|---|---|---|
| [`BEDROCK_REVIEW.md`](./BEDROCK_REVIEW.md) | How should one immutable bedrock candidate or fixture packet be reviewed and handed off? | `CONFIRMED` repository-grounded v0.1 draft | Use for bounded review preparation; no admission, policy, lifecycle, or release authority |
| [`NO_NETWORK_TEST_RUNBOOK.md`](./NO_NETWORK_TEST_RUNBOOK.md) | Which Geology checks can run without live network access, and what does each result prove? | `CONFIRMED` repository-grounded v0.2 draft | Use for the four named synthetic profiles only |
| [`SOURCE_REFRESH_RUNBOOK.md`](./SOURCE_REFRESH_RUNBOOK.md) | How should an already-admitted source change be detected, assessed, and handed off? | `NEEDS VERIFICATION`; proposal-era v1 draft | Do not use to admit, activate, schedule, fetch, or publish a live source |
| [`PROMOTION_RUNBOOK.md`](./PROMOTION_RUNBOOK.md) | Which gates should precede a Geology lifecycle or release transition? | `NEEDS VERIFICATION`; proposal-era v1 draft | Do not treat named paths, signers, gates, or commands as current implementation proof |
| [`ROLLBACK_RUNBOOK.md`](./ROLLBACK_RUNBOOK.md) | How should rollback, withdrawal, hold, correction, invalidation, and recovery be planned and verified? | `CONFIRMED` repository-grounded v0.2 draft | Candidate validation and synthetic rehearsal only; operational execution remains separately authorized |

[Back to top](#top)

---

## Start here

| Situation | Start with | Required companion or next owner | Stop condition |
|---|---|---|---|
| Review a bedrock unit, boundary, cross-section, generalized derivative, or source-probe fixture packet | [`BEDROCK_REVIEW.md`](./BEDROCK_REVIEW.md) | Named source, evidence, rights, sensitivity, spatial, validation, policy, review, correction, and release authorities as applicable | Candidate identity or any material prerequisite cannot be resolved |
| Run current synthetic Geology checks | [`NO_NETWORK_TEST_RUNBOOK.md`](./NO_NETWORK_TEST_RUNBOOK.md) | Exact fixtures, validators, tests, and workflow revision named by the runbook | A live source, real sensitive payload, unbounded network path, or unsupported profile is required |
| Investigate a possible source change | [`SOURCE_REFRESH_RUNBOOK.md`](./SOURCE_REFRESH_RUNBOOK.md) for planning only | Current source registry and authority controls; repository-grounded refresh procedure still required | Source is not admitted; rights, cadence, endpoint, source role, or current implementation is unresolved |
| Evaluate a lifecycle or release transition | [`PROMOTION_RUNBOOK.md`](./PROMOTION_RUNBOOK.md) for planning only | Current contracts, schemas, policy, evidence, review, release, correction, and rollback controls | Any gate depends only on proposal-era prose or an unverified path |
| Contain or recover a defective release-facing state | [`ROLLBACK_RUNBOOK.md`](./ROLLBACK_RUNBOOK.md) | Authorized release/correction/review machinery and current evidence | No safe target, authority, invalidation plan, correction path, or verification evidence exists |
| Determine broad Geology scope, vocabulary, or cross-lane ownership | [`docs/domains/geology/README.md`](../../domains/geology/README.md) and owning contracts | Geology domain and adjacent domain authorities | The question would collapse another domain's truth into Geology |
| Decide what public clients may render or what AI may say | Governed API, release, policy, evidence, and UI/AI contracts | MapLibre and AI remain downstream consumers | Evidence, policy, review, release, or public-safe representation cannot resolve |

### Procedure selection rule

Choose the narrowest procedure whose current evidence covers the intended action. Do not combine several partial runbooks into implied authority. When two procedures disagree:

1. preserve the prior safe state;
2. consult accepted doctrine and ADRs;
3. inspect the current owning contracts, schemas, policy, tests, workflows, and release records;
4. record the conflict;
5. return `HOLD`, `ABSTAIN`, `DENY`, or `ERROR` as appropriate;
6. repair the documentation in a separate reviewed change.

[Back to top](#top)

---

## Lifecycle and state separation

The KFM lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLETS -> PUBLISHED
```

Promotion is a governed state transition, not a file move, branch, commit, pull request, workflow badge, generated receipt, map rendering, or AI response.

### State axes that must remain distinct

| Axis | Example | This README's effect |
|---|---|---|
| File presence | A Markdown file exists | Navigation only |
| Documentation maturity | Blank, proposal-era, repository-grounded, corrected, or stale | Disclosed here |
| Procedure validation | Paths, inputs, commands, negative states, and outputs were checked | Must be established by exact evidence |
| Rehearsal state | A synthetic scenario ran in an approved isolated environment | Does not establish production admission |
| Source state | Proposed, disabled, admitted, stale, withdrawn, or denied | Owned by source authorities |
| Evidence state | Missing, resolvable, conflicting, invalidated, or sufficient for a bounded claim | Owned by evidence/proof controls |
| Policy state | Allow, restrict, hold, abstain, deny, or error under a named policy version | Owned by policy and required review |
| Review state | Pending, completed, rejected, or superseded | Owned by accountable review records |
| Lifecycle state | RAW, WORK, QUARANTINE, PROCESSED, CATALOG/TRIPLETS, PUBLISHED | Owned by governed lifecycle transition records |
| Release state | Candidate, review, published, revoked, or superseded under current contracts | Owned by release authorities |
| Deployment state | Built, staged, deployed, degraded, or rolled back | Owned by deployment and operations evidence |
| Publication state | Public-safe carrier is actually exposed through governed delivery | Not established by repository prose alone |

A child procedure may help an authorized actor prepare or verify one transition. It cannot collapse these axes into a single “done” flag.

[Back to top](#top)

---

## What belongs here

This directory may contain:

- human-readable Geology and Natural Resources operational procedures;
- a compact local boundary and navigation README;
- preflight, review, validation, refresh, promotion, correction, withdrawal, rollback, and recovery instructions;
- exact references to current owning contracts, schemas, policy, fixtures, tests, validators, workflows, evidence, proofs, review records, and release families;
- public-safe finite outcomes, stop conditions, handoff requirements, and troubleshooting guidance;
- documented command examples only when verified against current repository evidence and bounded by their actual effects;
- maintenance, correction, supersession, and document-rollback guidance.

A runbook may explain how to obtain or interpret an authority-bearing record. It must not become that record.

[Back to top](#top)

---

## What does not belong here

Do not store or define any of the following under `docs/runbooks/geology/`:

- source payloads, credentials, endpoint secrets, private URLs, or live connector configuration;
- exact or reverse-engineerable borehole, private-well, well-log, core, sample, geochemistry, resource, extraction, infrastructure, archaeology, parcel, owner, or operator details;
- canonical semantic contracts or JSON Schemas;
- executable policy rules or policy decisions;
- fixtures, tests, validators, pipelines, connectors, application code, runtime adapters, or workflow definitions;
- RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLETS, or PUBLISHED data instances;
- EvidenceBundles, proofs, process receipts, review records, release manifests, promotion decisions, correction notices, withdrawal notices, rollback cards, signatures, or deployment records;
- map tiles, PMTiles, COGs, GeoParquet, graph projections, search/vector indexes, screenshots, 3D scenes, cross-section assets, reports, or AI answers used as sovereign truth;
- duplicate source registries, schema homes, policy homes, release lanes, or public-delivery paths;
- silent copies of external planning documents presented as current repository authority.

When a draft procedure needs one of these artifacts, link to the owning family and stop if it cannot resolve.

[Back to top](#top)

---

## Inputs, outputs, and permitted actors

### Inputs

A procedure may require:

- exact repository revision and target object identity;
- admitted source identity and source-role record;
- rights, attribution, redistribution, and sensitivity posture;
- immutable candidate or fixture references and content digests;
- spatial reference, map edition, scale, resolution, time/vintage, depth, and vertical-reference context;
- EvidenceRef and EvidenceBundle support;
- validator and test results at the exact revision;
- PolicyDecision and required obligations;
- ReviewRecord and accountable reviewer identity;
- PromotionDecision, ReleaseManifest, CorrectionNotice, WithdrawalNotice, or RollbackCard as applicable;
- declared invalidation and rollback targets;
- approved environment, permissions, and audit destination.

### Outputs

A procedure may produce or request a bounded handoff such as:

- reviewed checklist;
- public-safe findings and reason codes;
- candidate disposition;
- validation summary tied to exact inputs and revision;
- quarantine or escalation request;
- correction or rollback candidate;
- explicit next-owner handoff;
- documentation change and its own rollback target.

The durable output must be stored by its owning family. A Markdown table embedded here is not a policy decision, review record, proof, release object, or execution receipt.

### Permitted actors and separation

| Actor | May use this lane to | Must not infer |
|---|---|---|
| Contributor or operator | Follow a verified procedure and prepare a bounded handoff | Authority from authorship |
| Geology domain reviewer | Evaluate domain semantics within assigned scope | Rights, policy, release, or adjacent-domain authority |
| Source steward | Resolve source identity, role, cadence, and admission | Geologic truth from registry presence |
| Rights/sensitivity reviewer | Decide handling obligations within assigned authority | Scientific or release approval |
| Validation/evidence reviewer | Inspect fixtures, validators, EvidenceBundle support, and proof closure | Release or publication from a green check |
| Policy reviewer/evaluator | Produce or review a named finite policy result | Evidence or scientific truth |
| Release/correction/rollback authority | Act through accepted release controls | Permission from documentation alone |
| Public UI or AI consumer | Consume released public-safe responses through governed interfaces | Direct access to this lane as data or truth |

Material source admission, harmful-precision handling, policy-significant review, release, and rollback should use separation of duties when current governance requires it. The verified CODEOWNERS route is not proof that accountable or independent review occurred.

[Back to top](#top)

---

## Geology-specific safety rules

### Source-role and resource-class anti-collapse

Keep these distinctions explicit:

- observation versus interpretation versus model;
- authoritative source versus corroborating source versus context;
- geologic unit versus administrative or regulatory record;
- mineral occurrence versus deposit versus estimate versus reserve;
- permit versus production versus physical geology;
- extraction or reclamation record versus resource existence;
- generalized map product versus source-native detail;
- synthetic fixture versus real-world evidence;
- generated summary versus evidence-backed claim.

A map polygon, lease, permit, production record, well top, model surface, anomaly, AI summary, or source-probe event cannot be silently upgraded into a stronger claim class.

### Harmful precision and sensitive joins

Exact or reverse-engineerable subsurface and resource-adjacent detail requires the strictest applicable handling. This includes:

- boreholes, private wells, well logs, cores, samples, geochemistry, and geophysics;
- extraction-targetable mineral or resource locations;
- operator, parcel, lease, title, ownership, or private-site joins;
- infrastructure-sensitive subsurface context;
- archaeology or cultural-resource intersections;
- redaction offsets, generalization radii, transform secrets, or private endpoint metadata.

A join may be more sensitive than either input. A T0/public input joined to another public input can still produce a restricted result. Policy and review apply to the resulting claim and representation.

### Representation context

Every consequential map, cross-section, generalized derivative, interpolated surface, 3D scene, or AI description must preserve enough context to prevent visual overclaiming:

- source and source role;
- map edition, publication date, and retrieval time;
- compilation scale, resolution, and intended use;
- CRS, datum, and vertical/depth reference;
- observation versus interpretation versus model status;
- uncertainty, confidence, limitations, and stale state;
- transform, generalization, redaction, or aggregation record;
- EvidenceBundle, policy, review, release, correction, and rollback references where material.

A renderer, tile archive, screenshot, or scene is a representation, not direct reality.

### Cross-lane ownership

Geology may relate to adjacent domains without absorbing their authority:

| Related concern | Owning lane |
|---|---|
| Groundwater measurements, flows, levels, and hydrologic interpretation | Hydrology |
| Soil map units, horizons, and soil properties | Soil |
| Fault, landslide, subsidence, flood, or other risk/exposure conclusions | Hazards |
| Parcels, title, lease, ownership, and living-person assertions | People, DNA & Land |
| Roads, pipelines, utilities, and infrastructure operations | Settlements/Infrastructure or Roads/Rail/Trade as applicable |
| Archaeological site meaning and location permissions | Archaeology |
| Airborne survey announcement or candidate campaign metadata spanning groundwater context | Shared source identity with explicit Geology/Hydrology relation; no duplicate authority |

### MapLibre and governed AI

MapLibre, Evidence Drawer, Focus Mode, search, graph, dashboard, report, export, and AI surfaces are downstream consumers. They must use governed APIs or released public-safe carriers, preserve finite non-answer states, show evidence and correction context appropriate to consequence, and never read RAW, WORK, QUARANTINE, restricted stores, direct model output, or this documentation lane as public truth.

[Back to top](#top)

---

## Finite outcomes and stop conditions

This README does not create a new canonical outcome enum. Use the vocabulary defined by the applicable child procedure, contract, schema, validator, policy profile, review record, or release object.

Common meanings in this lane include:

| Outcome | Bounded meaning |
|---|---|
| `PASS` | The named bounded check passed; no broader authority is implied |
| `NO_CHANGE` | The compared bounded inputs show no material change under the named profile |
| `REVIEW_REQUIRED` | A named accountable reviewer must decide the next step |
| `HOLD` | A required authority, input, identity, evidence, permission, target, or implementation boundary is unresolved |
| `ABSTAIN` | Evidence is insufficient to support the requested claim or answer |
| `RESTRICT` | Handling may continue only under a narrower audience, precision, or obligation |
| `DENY` | The requested action or exposure is prohibited under the applicable rule |
| `ERROR` | The procedure could not produce a reliable decision because input, schema, execution, or system state failed |
| `CORRECTION_REQUIRED` | Previously exposed or candidate material requires explicit correction lineage |
| `ROLLBACK_CANDIDATE` | A non-authoritative candidate plan identifies an affected release and possible prior target |
| `WITHDRAWAL_CANDIDATE` | A non-authoritative candidate plan proposes withdrawal without restoring a prior release |

### Mandatory stop conditions

Stop and preserve the prior safe state when any of the following applies:

- source identity, role, admission, rights, terms, cadence, or current version is unresolved;
- the machine source-authority register is being treated as populated when it is empty;
- source records are split across conflicting writable topologies without a canonical writer;
- exact or reverse-engineerable sensitive detail would enter an ordinary repository, log, issue, pull request, screenshot, map, export, or AI response;
- observation, interpretation, model, regulatory, administrative, occurrence, deposit, estimate, reserve, permit, or production roles are collapsed;
- candidate identity, digest, schema version, spatial reference, scale, time, depth, or uncertainty is missing;
- EvidenceRef cannot resolve to admissible support for a consequential claim;
- active policy or required human review cannot be established;
- a procedure depends on proposal-era paths or commands not verified at the current revision;
- release, correction, invalidation, or rollback targets are absent;
- the intended action would mutate public state through documentation, a file move, map rendering, workflow badge, or generated text;
- an overlapping branch, pull request, migration, or authority decision owns the same bytes or boundary;
- the operation would cross into an adjacent domain without its owning authority.

A fail-closed outcome can be the correct successful result of a runbook.

[Back to top](#top)

---

## Validation and rehearsal boundary

### Current bounded executable evidence

| Profile | Current entry points | What a green result supports | What it does not support |
|---|---|---|---|
| Resource-class anti-collapse | Geology resource-class validator, fixtures, and focused test | Frozen synthetic distinctions and expected rejection cases | Real resource classification, reserves, economic viability, or source admission |
| GMD 3 AEM campaign candidate | Document-specific descriptor, fixtures, validator, and focused test | Sparse announcement-bound candidate shape, time scope, and negative controls | Current flight, acquisition, inversion, product, rights, or release state |
| Public-safe geometry | Metadata-only cases, validator, focused test, and generated documentation-convergence receipt | Denial of coordinate material and checks for declared generalized/withheld posture | Execution of a transform, safe public geometry, policy approval, or release |
| Production material change | Version-pinned metadata comparison and focused test | `NO_CHANGE`, `REVIEW`, `HOLD`, or `ERROR` for bounded metadata | Live KGS fetch, production truth beyond the source role, lifecycle mutation, or publication |
| Shared Python startup guard | Geology fresh-process proof and shared `sitecustomize.py` helper | Explicit activation, public `SocketType` denial, and Unix-domain preservation for named Python APIs | Private `_socket.socket`, dependency installation, non-Python, operating-system, or runner-wide egress denial |
| Shared rollback rehearsal | Marker-protected synthetic helper and tests referenced by the rollback runbook | Deterministic synthetic rollback/withdrawal planning and history preservation | Geology-specific operational rollback, public alias mutation, signer custody, or production invalidation |

The workflow header and body now agree on four profiles. The guard proof is enforcement evidence for their Python process startup, not a fifth Geology semantic profile.

### No-network limit

`PYTHONPATH` startup loading, `KFM_NO_NETWORK=1`, and in-process socket/resolver/`urllib` guards are bounded controls. They are not an operating-system firewall, namespace, proxy, dependency-install control, non-Python sandbox, or proof that every network path is blocked. Direct private `_socket.socket` construction is outside the named public-API proof. Use the exact child-runbook qualification.

### Documentation checks

A change to this README should at minimum verify:

- balanced KFM metadata markers;
- valid UTF-8 and final newline;
- balanced fenced code blocks;
- direct-child map matches current repository evidence;
- relative links resolve at the pinned revision;
- headings and navigation anchors agree;
- no unresolved placeholder, transient citation token, secret, private endpoint, exact sensitive coordinate, or speculative command is introduced;
- no statement upgrades documentation or fixture presence into operational, release, deployment, or publication maturity.

Hosted workflow success is exact-revision evidence for what those workflows exercise. It does not establish source admission, geologic truth, policy approval, independent review, release, deployment, or publication.

[Back to top](#top)

---

## Maintenance and review triggers

### Maintenance rules

1. Pin material current-state claims to a repository revision.
2. Update the direct-child map only from verified repository evidence.
3. Keep child status summaries bounded to what each file and owning evidence prove.
4. Preserve source-role, resource-class, sensitivity, rights, evidence, review, release, correction, and rollback distinctions.
5. Link to owning contracts, schemas, policy, fixtures, tests, validators, workflows, evidence, proofs, and release families rather than copying their authority into this README.
6. Record conflicts and stale assumptions instead of silently harmonizing them.
7. Update this README when a child procedure is created, moved, renamed, materially reconciled, deprecated, superseded, or retired.
8. Do not add a proposed child to the current tree before it exists.
9. Keep planning documents as lineage; do not convert their proposed paths or implementation claims into current facts without verification.
10. Update documentation alongside material behavior changes or explain the bounded reason for deferral.

### Review triggers

Re-review this lane when:

- a child runbook's maturity or authority boundary changes;
- an accountable owner or independent reviewer is assigned;
- source-registry topology or source-authority projection is reconciled;
- a live source is admitted, activated, suspended, or withdrawn;
- active Geology policy evaluation is established;
- Geology EvidenceBundle/proof closure graduates;
- a Geology release candidate, release, correction, withdrawal, or rollback instance appears;
- a validator, fixture, test, workflow, or required-check boundary changes;
- an exact-location, rights, sensitivity, security, or cross-lane incident occurs;
- promotion, rollback, invalidation, signer, deployment, or public delivery becomes operational;
- Directory Rules, a governing ADR, or the parent runbook contract changes;
- drift is found between this README, child procedures, or owning implementation.

[Back to top](#top)

---

## Open verification backlog

### Ownership and review

- [ ] Assign accountable Geology and Natural Resources runbook stewardship.
- [ ] Assign source, rights, sensitivity, evidence, policy, validation, review, release, correction, rollback, security, and operations owners.
- [ ] Establish an independent review route for material source, sensitivity, release, and rollback decisions.
- [ ] Verify whether a Geology runbook-specific CODEOWNERS rule is warranted without confusing routing with authority.

### Procedure reconciliation

- [ ] Reconcile [`PROMOTION_RUNBOOK.md`](./PROMOTION_RUNBOOK.md) against current contracts, schemas, policy, evidence, review, release, correction, rollback, workflows, and repository paths.
- [ ] Reconcile [`SOURCE_REFRESH_RUNBOOK.md`](./SOURCE_REFRESH_RUNBOOK.md) against current source-registry topology, source-authority state, material-change validator, receipts, no-network boundaries, and admitted source posture.
- [ ] Decide whether a separate source-onboarding procedure is required only after source-admission ownership and current implementation are verified.
- [ ] Repair the `domain-geology` opening comment's three-versus-four profile drift in a separate exact-head workflow change if no generated receipt or dependent evidence requires coordinated repair.

### Source, policy, evidence, and release

- [ ] Reconcile subtype-first and domain-first Geology source-registry lanes through accepted migration discipline; do not maintain parallel writable authority.
- [ ] Populate or deliberately retire the empty source-authority projection only through its owning governance process.
- [ ] Replace `TBD` source templates with reviewed records or keep them explicitly proposed/disabled.
- [ ] Establish active Geology policy input, evaluator binding, finite decisions, obligations, and receipts.
- [ ] Establish Geology-specific EvidenceBundle/proof closure and resolver integrity.
- [ ] Establish an indexed Geology release-candidate dossier only when a real candidate and all required support exist.
- [ ] Establish signer identity, key custody, public alias control, invalidation mechanisms, deployment boundary, audit destination, and correction/rollback execution evidence before operational claims.
- [ ] Implement and review a Geology-specific synthetic rollback drill if graduation criteria require one.
- [ ] Verify public MapLibre, Evidence Drawer, Focus Mode, export, search, graph, and AI consumers only after governed release composition exists.

### Documentation integration

- [ ] Refresh the parent [`docs/runbooks/README.md`](../README.md) through a full current-tree inventory reconciliation so its domain-boundary count includes this lane.
- [ ] Reconcile stale path and maturity claims in the domain landing page and adjacent documentation through separate dependency-closed changes.
- [ ] Keep this local boundary synchronized when the source-refresh and promotion documents are modernized.

[Back to top](#top)

---

## Related surfaces

### Governing documentation

- [`docs/runbooks/README.md`](../README.md)
- [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md)
- [`ADR-0029`](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
- [`docs/domains/geology/README.md`](../../domains/geology/README.md)
- [`docs/domains/geology/DATA_LIFECYCLE.md`](../../domains/geology/DATA_LIFECYCLE.md)
- [`docs/domains/geology/SENSITIVITY.md`](../../domains/geology/SENSITIVITY.md)
- [`docs/domains/geology/SOURCE_ROLE_MATRIX.md`](../../domains/geology/SOURCE_ROLE_MATRIX.md)

### Procedures in this lane

- [`BEDROCK_REVIEW.md`](./BEDROCK_REVIEW.md)
- [`NO_NETWORK_TEST_RUNBOOK.md`](./NO_NETWORK_TEST_RUNBOOK.md)
- [`SOURCE_REFRESH_RUNBOOK.md`](./SOURCE_REFRESH_RUNBOOK.md)
- [`PROMOTION_RUNBOOK.md`](./PROMOTION_RUNBOOK.md)
- [`ROLLBACK_RUNBOOK.md`](./ROLLBACK_RUNBOOK.md)

### Semantic, machine, policy, validation, and source boundaries

- [`contracts/domains/geology/README.md`](../../../contracts/domains/geology/README.md)
- [`schemas/contracts/v1/domains/geology/README.md`](../../../schemas/contracts/v1/domains/geology/README.md)
- [`policy/domains/geology/README.md`](../../../policy/domains/geology/README.md)
- [`fixtures/domains/geology/README.md`](../../../fixtures/domains/geology/README.md)
- [`tests/domains/geology/README.md`](../../../tests/domains/geology/README.md)
- [`tools/validators/domains/geology/README.md`](../../../tools/validators/domains/geology/README.md)
- [`tools/validators/geology/README.md`](../../../tools/validators/geology/README.md)
- [`data/registry/sources/geology/README.md`](../../../data/registry/sources/geology/README.md)
- [`data/registry/geology/sources/README.md`](../../../data/registry/geology/sources/README.md)
- [`data/proofs/geology/README.md`](../../../data/proofs/geology/README.md)
- [`release/candidates/geology/README.md`](../../../release/candidates/geology/README.md)
- [`domain-geology workflow`](../../../.github/workflows/domain-geology.yml)
- [`.github/CODEOWNERS`](../../../.github/CODEOWNERS)

[Back to top](#top)

---

## Evidence basis

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Target file at `main@35d1c6c...` | `CONFIRMED` | Existing path and one-byte prior state | Does not define a lane boundary |
| Current direct directory listing | `CONFIRMED` | Exact five procedure children and blob identities | Does not prove procedure correctness or operation |
| Accepted ADR-0029 and Directory Rules v2 | `CONFIRMED` accepted placement authority | `BOUNDARY_COMPACT` profile, same-path placement, direct-child map, authority separation | Does not grant source, policy, release, or publication authority |
| Parent runbook README | `CONFIRMED` historical inventory | Inherited operational-documentation boundary | Its pinned domain-lane counts predate this update |
| Bedrock review runbook | `CONFIRMED` repository-grounded draft | Candidate-review/handoff boundary and Geology interpretation controls | No active candidate or approval is established |
| No-network runbook, fixtures, validators, tests, workflow | `CONFIRMED` bounded repository evidence | Four current synthetic profiles and explicit non-effects | No live source, evidence closure, policy, proof, release, or public behavior |
| Rollback runbook, shared RollbackCard profile, synthetic rehearsal | `CONFIRMED` bounded repository evidence | Candidate validation and marker-protected synthetic recovery design | No Geology production rollback, alias mutation, signer, invalidator, or deployment |
| Promotion and source-refresh runbooks | `CONFIRMED` tracked proposal-era drafts | Planning lineage and procedure intent | Current paths, commands, roles, cadences, and operational claims require reconciliation |
| Machine source-authority projection | `CONFIRMED` empty/absent implementation posture | No source is activated or admitted by the projection | Does not enumerate current source records or resolve topology |
| Subtype-first and domain-first source lanes | `CONFIRMED` conflicting repository surfaces | Source topology and proposed/disabled records exist | Presence is not admission, authority, rights clearance, or activation |
| Geology policy README | `CONFIRMED` repository-grounded draft | Default-only scaffolds and evaluator hold | No active Geology policy decision path |
| Geology proof README and shared evidence family | `CONFIRMED` bounded support | Shared EvidenceBundle mechanics and proof-lane boundaries | No Geology-specific closure or public claim support is proven |
| Geology release-candidate directory | `CONFIRMED` README-only inventory | No child candidate dossier in canonical lane | Does not prove absence of external, historical, restricted, or differently located material |
| Connected Drive geology architecture report | `CONFIRMED` planning lineage | Domain scope, anti-collapse, public-safe geometry, separate accountability families, fixture-first posture | Written without mounted repo evidence; paths and implementation claims remain proposals |
| Deployment, runtime, public aliases, live sources, logs, public carriers | `UNKNOWN` in this update | — | No operational, release, deployment, or publication claim is made |

### Source reconciliation note

The connected Drive report proposed a broad Geology and Natural Resources architecture before the repository was available to that authoring session. This README retains the report's durable boundaries—source-role and claim-class anti-collapse, harmful-precision controls, separate evidence/policy/review/release families, downstream map/AI behavior, and fixture-first validation—but does not copy its speculative path or maturity claims. Current repository evidence and accepted governance control this update.

[Back to top](#top)

---

## Document change rollback

This change can be reversed by reverting the feature-branch commit or restoring prior blob:

```text
8b137891791fe96927ad78e64b0aad7bded08bdc
```

Reverting this README restores the blank local boundary. It does not:

- undo or execute a source refresh;
- admit or withdraw a source;
- change a contract, schema, policy, fixture, validator, test, workflow, evidence object, proof, review record, release object, alias, deployment, or public carrier;
- reverse a lifecycle transition;
- invalidate a cache or tile;
- roll back production;
- release, deploy, promote, or publish anything.

A later correction should preserve the history of this document and identify the exact prior and replacement blobs.

[Back to top](#top)
