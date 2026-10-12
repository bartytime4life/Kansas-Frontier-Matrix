<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/release-candidates-archaeology-readme
title: Archaeology Release Candidate Review Lane
type: per-domain-release-candidate-index
version: v2
status: draft; repository-grounded; deny-by-default; pre-publication
contract_version: "3.0.0"
owners: [bartytime4life]
created: 2026-07-03
updated: 2026-07-18
policy_label: public
truth_posture: cite-or-abstain
responsibility_root: release/
lane_role: archaeology candidate dossier index and sensitive-domain pre-publication review boundary
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_commit: ede1d1f2dc4dc7d8409fa5c1da0d98b469d973f9
  prior_blob: 2047236f1f8d9a7fb0db8732bd6a492817ce94e5
  bounded_candidate_inventory: parent README only; no child dossier established
related:
  - ../README.md
  - ../../README.md
  - ../../manifests/README.md
  - ../../promotion_decisions/README.md
  - ../../correction_notices/README.md
  - ../../rollback_cards/README.md
  - ../../withdrawal_notices/README.md
  - ../../changelog/README.md
  - ../../../data/processed/archaeology/README.md
  - ../../../data/published/archaeology/README.md
  - ../../../data/registry/sources/archaeology/README.md
  - ../../../data/proofs/archaeology/README.md
  - ../../../contracts/domains/archaeology/README.md
  - ../../../schemas/contracts/v1/domains/archaeology/README.md
  - ../../../policy/domains/archaeology/README.md
  - ../../../tests/domains/archaeology/README.md
  - ../../../fixtures/domains/archaeology/README.md
  - ../../../tools/validators/archaeology/README.md
  - ../../../tools/validators/domains/archaeology/README.md
  - ../../../docs/domains/archaeology/RELEASE_INDEX.md
  - ../../../docs/domains/archaeology/PUBLICATION_AND_POLICY.md
  - ../../../docs/domains/archaeology/SENSITIVITY.md
  - ../../../docs/domains/archaeology/CULTURAL_REVIEW.md
  - ../../../docs/domains/archaeology/PIPELINE.md
  - ../../../docs/domains/archaeology/PRESERVATION_MATRIX.md
  - ../../../docs/domains/archaeology/CANONICAL_PATHS.md
  - ../../../docs/runbooks/archaeology/ROLLBACK_RUNBOOK.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/registers/DRIFT_REGISTER.md
  - ../../../.github/CODEOWNERS
  - ../../../.github/workflows/domain-archaeology.yml
  - ../../../.github/workflows/release-dry-run.yml
tags: [kfm, release, candidates, archaeology, sensitive-domain, cultural-review, sovereignty, evidence, validation, rollback]
notes:
  - "This README indexes Archaeology release-candidate dossiers and defines their pre-publication review boundary. It is not a candidate, source, evidence, policy, cultural-review, release, or publication authority record."
  - "The bounded repository search and current Archaeology workflow establish no child candidate dossier under this lane."
  - "Exact or reverse-engineerable locations, burial or human-remains context, sacred or culturally restricted material, collection-security detail, looting-risk information, consent secrets, and protected review substance must not appear here."
  - "The literal publication-not_yet marker is retained for the current domain-archaeology readiness workflow; it is a compatibility signal, not release proof."
  - "CODEOWNERS review routing is not a stewardship assignment, cultural authority, independent review, release approval, or publication authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `release/candidates/archaeology/` — Archaeology Release Candidate Review Lane

> Index Archaeology release-candidate dossiers, preserve blockers and safe support pointers, and prevent sensitive cultural-heritage material from crossing the trust membrane until evidence, rights, sovereignty, cultural review, policy, validation, correction, and rollback gates close.

![status](https://img.shields.io/badge/status-repository--grounded%20draft-orange)
![root](https://img.shields.io/badge/root-release%2F-blue)
![lane](https://img.shields.io/badge/lane-candidates-blueviolet)
![domain](https://img.shields.io/badge/domain-archaeology-8B4513)
![publication](https://img.shields.io/badge/publication-not_yet-red)
![sensitivity](https://img.shields.io/badge/sensitivity-deny__by__default-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)
![contract](https://img.shields.io/badge/contract-v3.0.0-1f6feb)

> [!CAUTION]
> **Safe conclusion at `main@ede1d1f2…`:** the bounded inspection establishes this parent README but no child Archaeology candidate dossier or reviewed candidate record. The Archaeology release index still describes candidate and release rows as placeholders pending release-plane inspection. No candidate, manifest, promotion decision, proof, workflow result, schema, fixture, merge, generated receipt, or path presence establishes an Archaeology release.
>
> Archaeology remains deny-by-default. Exact or reverse-engineerable protected locations and culturally restricted substance must never be added to this public-review README.

## Quick navigation

- [Purpose](#purpose)
- [Status and evidence boundary](#status-and-evidence-boundary)
- [Authority and repository fit](#authority-and-repository-fit)
- [Current candidate inventory](#current-candidate-inventory)
- [Candidate lifecycle](#candidate-lifecycle)
- [What belongs here](#what-belongs-here)
- [What does not belong here](#what-does-not-belong-here)
- [Candidate admission contract](#candidate-admission-contract)
- [Archaeology release gates](#archaeology-release-gates)
- [Required dossier structure](#required-dossier-structure)
- [Sensitivity, sovereignty, and cultural-review rules](#sensitivity-sovereignty-and-cultural-review-rules)
- [Evidence and source-role rules](#evidence-and-source-role-rules)
- [Validation and fixture posture](#validation-and-fixture-posture)
- [Automation posture](#automation-posture)
- [Release handoff routing](#release-handoff-routing)
- [Correction, withdrawal, and rollback](#correction-withdrawal-and-rollback)
- [Review and separation of duties](#review-and-separation-of-duties)
- [Maintenance and definition of done](#maintenance-and-definition-of-done)
- [Evidence ledger](#evidence-ledger)
- [Open verification](#open-verification)
- [Changelog](#changelog)
- [Rollback for this README](#rollback-for-this-readme)

---

## Purpose

`release/candidates/archaeology/` is the Archaeology pre-publication review lane under the `release/` responsibility root.

It should answer six bounded questions:

1. Which Archaeology release candidates are currently indexed?
2. What is each candidate's verified identity, version, scope, status, and finite decision?
3. Which source, evidence, rights, sensitivity, sovereignty, consent, cultural-review, policy, validation, correction, and rollback records support it?
4. Which details are safe to show in a public-review dossier, and which must remain in restricted governed stores?
5. Which blockers prevent manifest preparation or release?
6. Which shared release lane owns the next governed record?

A candidate is not a release. A candidate directory, README, pull request, merge, workflow result, schema pass, fixture pass, redaction description, generalized map, AI summary, generated receipt, or public URL must not be interpreted as publication approval.

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Promotion is a governed state transition, not a file move or repository event.

[Back to top](#top)

---

## Status and evidence boundary

| Field | Current posture |
|---|---|
| Document type | Per-domain candidate-lane index and sensitive-domain review contract |
| Owning root | `release/` |
| Candidate lane | `release/candidates/archaeology/` |
| Current bounded child inventory | No child dossier established |
| Active candidate | None established by the inspected evidence |
| Approved-for-manifest candidate | None established |
| Approved Archaeology manifest | None established |
| Published Archaeology release | None established |
| Candidate artifact inventory | **UNKNOWN** beyond README-level evidence |
| Executable candidate validation | Not established |
| Cultural/rights-holder approval | None established |
| Release authority of this README | None |
| Default posture | Deny, restrict, hold, abstain, narrow, or error rather than infer safety or authority |

### Truth labels

| Label | Meaning here |
|---|---|
| `CONFIRMED` | Verified from a repository file, immutable ref/blob, workflow definition/run, or generated artifact in the current work session |
| `PROPOSED` | Candidate meaning, path interpretation, gate, profile, transform, or implementation direction not yet established |
| `UNKNOWN` | Not resolved by the bounded inspection |
| `NEEDS VERIFICATION` | Checkable but not verified strongly enough to act as fact |
| `CONFLICTED` | Current repository or doctrine sources disagree and no accepted decision selects a winner |
| `LINEAGE` | Historical or planning material retained for traceability, not current authority by itself |

Runtime and release outcomes such as `HOLD_FOR_CULTURAL_REVIEW`, `PROMOTE_TO_MANIFEST`, `DENY`, `RESTRICT`, `ABSTAIN`, and `ERROR` are operational states, not substitutes for these authoring labels.

### Current safe conclusion

The repository contains a substantial documentation and readiness-control surface for Archaeology, including:

- domain doctrine and lifecycle references;
- sensitivity and cultural-review protocols;
- policy-lane guidance;
- a proof-lane README;
- named test modules whose sampled contents are placeholders;
- read-only CI readiness holds; and
- release and published-data parent lanes.

Those surfaces do not establish a concrete candidate packet, cultural review, evidence closure, policy enforcement, public-safe transform, manifest, release decision, or published carrier.

[Back to top](#top)

---

## Authority and repository fit

Directory Rules place release-candidate review under `release/` while keeping data, cultural-review evidence, policy, tests, proofs, and published carriers in their own responsibility roots.

| Responsibility | Owning lane |
|---|---|
| Archaeology candidate dossiers and blocker state | This lane |
| Cross-domain candidate parent | [`release/candidates/`](../README.md) |
| Release-root authority | [`release/`](../../README.md) |
| Candidate artifacts | [`data/processed/archaeology/`](../../../data/processed/archaeology/README.md) or another accepted staging lane |
| Source admission and source role | [`data/registry/sources/archaeology/`](../../../data/registry/sources/archaeology/README.md) |
| Evidence and proof support | [`data/proofs/archaeology/`](../../../data/proofs/archaeology/README.md) |
| Archaeology meaning | [`contracts/domains/archaeology/`](../../../contracts/domains/archaeology/README.md) |
| Machine-checkable shape | [`schemas/contracts/v1/domains/archaeology/`](../../../schemas/contracts/v1/domains/archaeology/README.md) |
| Admissibility and obligations | [`policy/domains/archaeology/`](../../../policy/domains/archaeology/README.md) |
| Deterministic tests and fixtures | [`tests/domains/archaeology/`](../../../tests/domains/archaeology/README.md) and [`fixtures/domains/archaeology/`](../../../fixtures/domains/archaeology/README.md) |
| Validator implementations | [`tools/validators/archaeology/`](../../../tools/validators/archaeology/README.md) and [`tools/validators/domains/archaeology/`](../../../tools/validators/domains/archaeology/README.md) |
| Cultural-review protocol | [`CULTURAL_REVIEW.md`](../../../docs/domains/archaeology/CULTURAL_REVIEW.md) |
| Sensitivity doctrine | [`SENSITIVITY.md`](../../../docs/domains/archaeology/SENSITIVITY.md) |
| Publication governance | [`PUBLICATION_AND_POLICY.md`](../../../docs/domains/archaeology/PUBLICATION_AND_POLICY.md) |
| Release index | [`RELEASE_INDEX.md`](../../../docs/domains/archaeology/RELEASE_INDEX.md) |
| Release manifest | Shared manifest lane or accepted successor |
| Promotion decision | Shared promotion-decision lane |
| Correction, withdrawal, supersession, and rollback | Shared release-governance lanes |
| Published public-safe carriers | [`data/published/archaeology/`](../../../data/published/archaeology/README.md) |
| Public client access | Governed API and released-artifact paths only |

### No parallel candidate authority

This lane owns candidate review records only. It must not become:

- a source registry;
- a proof store;
- a cultural-knowledge repository;
- a consent-token store;
- a schema or policy home;
- a restricted-coordinate store;
- a release manifest collection;
- a public map layer directory; or
- a substitute for named cultural or rights-holder authority.

### Release topology posture

The repository has shared lanes for manifests, promotion decisions, correction notices, rollback/review cards, withdrawal notices, and changelog records. It also carries singular/plural and domain-segmentation drift in parts of the release tree.

Candidate authors must surface that conflict and use the narrowest verified lane. Do not create duplicate Archaeology record homes merely because a planning document proposes a path.

[Back to top](#top)

---

## Current candidate inventory

The bounded repository search and current `domain-archaeology` workflow establish the following candidate-lane posture:

| Candidate | Status | Evidence | Public effect |
|---|---|---|---|
| No child candidate established | `NO_ACTIVE_CANDIDATE_ESTABLISHED` | Parent README only in the checked lane; workflow expects no non-README candidate record | None |

### Inventory limits

A code-search result, `find` check, or workflow condition is not a permanent recursive filesystem proof. Other candidates, generated files, unindexed records, history-only content, restricted systems, or external governance records remain **UNKNOWN** until directly inspected under authorized access.

Add a candidate row only after:

- a child path exists;
- its safe public-review metadata can be inspected;
- its status and finite decision are explicit;
- protected substance remains outside the dossier; and
- the candidate has not been mistaken for a confirmed site, public artifact, or release.

Do not add roadmap concepts, remote-sensing anomalies, LiDAR detections, synthetic reconstructions, or generalized map previews as active candidates unless a governed candidate identity and review packet exist.

[Back to top](#top)

---

## Candidate lifecycle

Use finite states and preserve the difference between candidate review, cultural approval, manifest preparation, and release authority.

| Candidate state | Meaning | Permitted next step |
|---|---|---|
| `PROPOSED` | Candidate identity exists; packet is incomplete | Assemble bounded support records |
| `ASSEMBLING` | Artifact and support packet are being gathered | Continue closure work |
| `READY_FOR_REVIEW` | Packet is complete enough for required reviewers | Open governed review |
| `BLOCKED` | One or more named gates are unresolved | Hold; remediate the named blocker |
| `REPAIR_REQUIRED` | Candidate content or support records require correction | Return to the owning upstream lane |
| `DEFERRED` | Candidate remains eligible but is not being advanced | Preserve state and review trigger |
| `APPROVED_FOR_MANIFEST` | Governed decision permits manifest preparation | Prepare a manifest in the accepted lane |
| `PROMOTED` | Candidate is bound into an approved release path | Preserve release and reversal lineage |
| `SUPERSEDED` | A newer candidate replaces this candidate | Link the replacement and preserve history |
| `WITHDRAWN` | Candidate is removed from consideration | Record reason and affected references |
| `DENIED` | Requested release posture is prohibited | Preserve safe reason code and do not expose protected detail |

`APPROVED_FOR_MANIFEST` does not mean `RELEASED`. Cultural-review sign-off does not by itself authorize publication, and publication approval does not transfer authority over cultural substance to KFM.

### Candidate hold outcomes

Prefer explicit, reviewable holds:

- `HOLD_FOR_ARTIFACT`
- `HOLD_FOR_SOURCE_ADMISSION`
- `HOLD_FOR_RIGHTS`
- `HOLD_FOR_SENSITIVITY`
- `HOLD_FOR_SOVEREIGNTY_REVIEW`
- `HOLD_FOR_CULTURAL_REVIEW`
- `HOLD_FOR_CONSENT`
- `HOLD_FOR_EVIDENCE`
- `HOLD_FOR_REDACTION`
- `HOLD_FOR_POLICY`
- `HOLD_FOR_VALIDATION`
- `HOLD_FOR_REVIEW`
- `HOLD_FOR_RELEASE_TOPOLOGY`
- `HOLD_FOR_CORRECTION_PATH`
- `HOLD_FOR_ROLLBACK`
- `HOLD_FOR_REVOCATION_OR_EMBARGO`

[Back to top](#top)

---

## What belongs here

- This parent README and candidate-lane indexes.
- One child directory per distinct, governed Archaeology release candidate.
- Public-review-safe candidate dossier Markdown.
- Candidate identity, version, status, decision, and immutable repository evidence snapshot.
- Safe pointers to processed/staged artifacts without duplicating payloads.
- Safe pointers to admitted sources, EvidenceBundles, policy decisions, validation reports, cultural-review records, consent/revocation state, manifests, corrections, withdrawals, supersession records, and rollback targets.
- Candidate readiness checklists and version history.
- Public-safe summaries of why a candidate is held, denied, deferred, repair-required, approved for manifest preparation, superseded, or withdrawn.
- Migration notes when accepted release topology changes.
- Safe reason codes that do not reveal protected location or cultural substance.

Candidate records should be compact, pointer-based, and safe for the repository's audience. Restricted details belong in approved controlled systems and should be represented here only by safe references, digests, and disposition state.

[Back to top](#top)

---

## What does not belong here

- RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED payloads.
- Exact or reverse-engineerable site geometry, coordinate fragments, map screenshots, tile identifiers, transform offsets, jitter seeds, suppression thresholds, or location clues.
- Burial, human-remains, sacred-site, ceremonial, cultural, oral-history, or community-controlled substance not cleared for this audience.
- Collection-security detail, storage locations, looting-risk indicators, private-landowner details, access routes, or field-operation logistics.
- Consent tokens, revocation secrets, identity-provider material, embargo keys, restricted agreements, or private reviewer correspondence.
- Bulk datasets, maps, tiles, rasters, point clouds, imagery, 3D models, exports, API payloads, search indexes, graph extracts, or embeddings.
- Source descriptors, credentials, API keys, source dumps, or private endpoints.
- `EvidenceBundle`, proof, review, consent, policy, or receipt content as the primary record.
- Semantic contracts, machine schemas, policy bundles, validator code, tests, or fixtures.
- Final `ReleaseManifest`, `PromotionDecision`, `CorrectionNotice`, `WithdrawalNotice`, or `RollbackCard` records when a shared lane owns that family.
- AI-generated reconstructions or summaries presented as observation, evidence, cultural interpretation, steward review, or release approval.
- Silent promotion by moving, copying, renaming, merging, rendering, indexing, or publishing files.

[Back to top](#top)

---

## Candidate admission contract

A new child candidate may be indexed only when it has a stable identity, an explicit non-release status, and a public-review-safe metadata packet.

### Minimum fields at candidate creation

| Field | Requirement |
|---|---|
| Candidate ID | Stable and deterministic where practical |
| Candidate version | Explicit and immutable for the dossier revision |
| Domain | `archaeology` |
| Candidate class | Explicit: candidate feature, survey summary, collection/context summary, generalized derivative, educational carrier, or other reviewed class |
| Source role | Candidate, observed, modeled, administrative, context, synthetic, restricted, or another accepted role |
| Proposed meaning | Narrow, bounded, and labeled `PROPOSED` until supported |
| Candidate owner | Verified GitHub identity or `OWNER_TBD`; do not invent teams |
| Artifact state | Safe pointer or explicit `NOT ESTABLISHED` |
| Proposed audience/surface | Named and bounded without exposing protected detail |
| Source/evidence state | Explicit closure status |
| Rights/sensitivity state | Explicit posture and blockers |
| Cultural/sovereignty state | Safe reference and decision status; no protected substance |
| Consent/revocation/embargo state | Explicit where applicable |
| Transform state | Named profile/reference and receipt status; no secret parameters |
| Validation state | Performed checks, failures, and not-run checks |
| Review state | Pending, approved, changes requested, denied, revoked, or governed override |
| Finite decision | Proposed, hold, repair, defer, approve-for-manifest, deny, supersede, or withdraw |
| Correction/rollback state | Safe pointer or explicit blocker |
| Date and immutable evidence snapshot | Required for repository-state claims |

### Candidate identity rules

- Do not derive meaning solely from a folder name, geometry, sensor output, or classifier label.
- Preserve `CandidateFeature`, `RemoteSensingAnomaly`, and `LiDARCandidate` status until governed evidence and review authorize a different object family.
- Do not reuse an ID for materially different source sets, areas, time scopes, cultural authorities, transforms, or audiences.
- Do not mutate an approved packet in place; supersede it with traceable lineage.
- Keep candidate ID distinct from source ID, site ID, artifact ID, review ID, consent ID, release ID, manifest ID, and run ID.
- Do not make candidate IDs or filenames encode protected location, community identity, burial status, sacred status, or collection-security detail.
- Preserve content digests and immutable artifact references where practical.

[Back to top](#top)

---

## Archaeology release gates

Every Archaeology candidate must fail closed when a load-bearing gate is unresolved.

| Gate | Required question | Failure posture |
|---|---|---|
| Identity | Is the candidate stable, versioned, scoped, and owned? | `HOLD_FOR_ARTIFACT` |
| Candidate role | Is candidate/model/anomaly status preserved without promotion to confirmed site truth? | `REPAIR_REQUIRED` or `DENY` |
| Artifact | Is there an immutable safe pointer and digest? | `HOLD_FOR_ARTIFACT` |
| Meaning and shape | Are class, fields, time, geography tier, representation, and schema defined? | `REPAIR_REQUIRED` or hold |
| Source admission | Do sources resolve to admitted records with role, rights, access, and sensitivity? | `HOLD_FOR_SOURCE_ADMISSION` |
| Evidence | Do consequential claims resolve through admissible `EvidenceRef` and `EvidenceBundle` support? | `HOLD_FOR_EVIDENCE` / `ABSTAIN` |
| Sensitivity | Is requested detail safe for the proposed audience? | `DENY`, `RESTRICT`, or hold |
| Cultural/sovereignty review | Has the named authority reviewed where required? | `HOLD_FOR_CULTURAL_REVIEW` |
| Consent/revocation/embargo | Is current consent and embargo state valid? | `HOLD_FOR_CONSENT` or `DENY` |
| Transform | Is a named, versioned, receipt-backed redaction/generalization profile applied? | `HOLD_FOR_REDACTION` |
| Reality boundary | Are reconstructions, models, 3D scenes, and synthetic carriers clearly labeled? | `REPAIR_REQUIRED` |
| Policy | Is a versioned `PolicyDecision` present with obligations and safe reason code? | `HOLD_FOR_POLICY` |
| Validation | Do deterministic positive and negative checks pass without protected-data leakage? | `HOLD_FOR_VALIDATION` |
| Review | Are required, distinct reviewers recorded? | `HOLD_FOR_REVIEW` |
| Release topology | Are manifest and decision homes accepted and non-duplicative? | `HOLD_FOR_RELEASE_TOPOLOGY` |
| Correction | Can defects, revocations, and downstream caches be corrected? | `HOLD_FOR_CORRECTION_PATH` |
| Rollback | Is a prior safe target, withdrawal plan, and drill evidence defined? | `HOLD_FOR_ROLLBACK` |

### Non-negotiable public-surface denials

The candidate cannot proceed to public manifest preparation when the requested output would expose or enable inference of:

- exact or reverse-engineerable protected locations;
- burial or human-remains context;
- sacred, ceremonial, or culturally restricted material;
- collection-security or looting-risk detail;
- private access or landowner information;
- consent or revocation secrets;
- sovereignty-controlled knowledge without named-authority approval; or
- source material whose rights do not permit the proposed use.

A coarser visualization, hidden layer, low opacity, disabled tooltip, client-side filter, or unpublished URL is not a sensitivity control.

[Back to top](#top)

---

## Required dossier structure

A candidate child README should include at least:

```markdown
# <candidate-id> — <public-safe candidate title>

## Candidate status
PROPOSED / ASSEMBLING / READY_FOR_REVIEW / BLOCKED / REPAIR_REQUIRED /
DEFERRED / APPROVED_FOR_MANIFEST / PROMOTED / SUPERSEDED / WITHDRAWN / DENIED

## Candidate identity
<id, version, candidate class, source role, owner, date, evidence snapshot>

## Public-review-safe scope
<bounded purpose, coarse scope, time posture, proposed audience and surface;
no protected location or cultural substance>

## Candidate artifact
<safe immutable pointer, digest, artifact manifest, or NOT ESTABLISHED>

## Source and rights closure
<SourceDescriptor refs, source roles, rights, access, sensitivity, blockers>

## Evidence closure
<EvidenceRef-to-EvidenceBundle mapping and unresolved claims>

## Sensitivity and transform posture
<audience tier, named profile ref, receipt refs, obligations; no secret parameters>

## Cultural, sovereignty, consent, and embargo review
<safe review-record refs and state; no controlled cultural substance>

## Reality boundary
<model, anomaly, candidate, reconstruction, 3D, or synthetic labels and receipts>

## Validation
<schema, identity, source role, evidence, sensitivity, no-leak, policy,
cultural-review, public-boundary, correction, and rollback checks>

## Review
<required reviewer roles, verified identities, states, dates, and separation of duties>

## Release handoff
<PromotionDecision and ReleaseManifest pointers or explicit blockers>

## Correction, revocation, and rollback
<affected consumers, cache invalidation, withdrawal/supersession path,
rollback target and drill evidence>

## Current decision
<finite outcome plus evidence-grounded, public-safe reason>
```

Candidate payloads, review substance, consent objects, evidence objects, policy code, tests, fixtures, and final release records remain in their owning roots.

[Back to top](#top)

---

## Sensitivity, sovereignty, and cultural-review rules

### Deny-by-default posture

Archaeology candidate review must apply the most restrictive relevant rule. Missing or conflicted sensitivity, cultural authority, consent, rights-holder, or sovereignty state is not permission to proceed.

The public-review dossier may state that a review exists or is pending. It must not reproduce restricted review content.

### Named authority controls substance

KFM records governance interfaces and review state. It does not redefine Indigenous knowledge, sacred-place meaning, oral-history substance, community categories, or other authority-controlled content.

When a record carries an `authority_to_control` or equivalent named-authority reference:

- that authority governs the controlled substance;
- KFM may not lower restrictions through internal interpretation;
- lack of response is not consent;
- revoked or expired consent fails closed;
- downstream derivatives inherit applicable restrictions; and
- release review must verify obligations are carried into every public carrier.

### Review classes

Candidate review should determine whether any of the following are required:

- archaeology domain stewardship;
- sensitivity review;
- cultural or tribal review;
- rights-holder representation;
- consent verification;
- sovereignty review;
- human-remains or burial review;
- collection-security review;
- land/access review;
- AI/representation review; and
- release/correction/rollback review.

### Transform rules

A transform may produce a safer representation; it does not erase sensitivity, rights, source role, cultural authority, or revocation obligations.

Every material transform should be:

- named and versioned;
- deterministic or reproducibly bounded where appropriate;
- linked to its policy decision;
- receipt-backed;
- reviewed for reversibility or inference risk;
- tested against public no-leak cases; and
- carried forward into manifest, correction, and rollback lineage.

Do not store transform secrets, exact thresholds, offsets, seeds, masks, or other reverse-engineering aids in this README.

[Back to top](#top)

---

## Evidence and source-role rules

### Source-role anti-collapse

Preserve source role from admission through candidate review:

| Source role | Candidate rule |
|---|---|
| `observed` | Use only when method, identity, rights, and sensitivity support direct-observation status |
| `candidate` | Must remain candidate until governed evidence and review authorize another class |
| `modeled` | Preserve model/run identity, inputs, uncertainty, and reality boundary |
| `remote_sensing_anomaly` | Anomaly is not a site; preserve detection uncertainty and review state |
| `administrative` | Administrative record presence does not prove physical or cultural condition |
| `regulatory` | Preserve legal/effective scope; do not treat as observation or cultural authority |
| `context` | May frame interpretation; cannot prove a sensitive claim alone |
| `synthetic` | Must remain visibly non-real and excluded from evidence claims |
| `representation` | Reconstruction or 3D carrier requires a reality-boundary record |
| `restricted` | Defaults to deny, restrict, redact, generalize, delay, or quarantine |

### Evidence closure

A candidate is not evidence. Consequential claims must resolve to admissible evidence through `EvidenceRef` and `EvidenceBundle` support.

Evidence support should preserve:

- source identity and role;
- rights and access posture;
- sensitivity and cultural restrictions;
- temporal validity and stale-state status;
- artifact and transform digests;
- uncertainty and candidate status;
- review and policy state;
- correction, revocation, and supersession lineage; and
- safe citation behavior for the intended audience.

Missing, stale, revoked, conflicted, or non-resolvable evidence produces a hold, abstention, denial, narrowing, or error.

### Public-safe citations

A citation must not become a location leak. Candidate dossiers should cite safe registry, evidence, review, and release identifiers—not source rows, original coordinates, private documents, restricted URLs, or revealing filenames.

[Back to top](#top)

---

## Validation and fixture posture

Current repository evidence does not establish a complete Archaeology candidate-validation or release-governance suite.

| Surface | Current safe interpretation |
|---|---|
| [`tests/domains/archaeology/`](../../../tests/domains/archaeology/README.md) | Thirteen named direct test modules are documented; sampled modules are one-line placeholders and executable enforcement remains unestablished |
| [`fixtures/domains/archaeology/`](../../../fixtures/domains/archaeology/README.md) | Reusable fixture guidance exists; payload and consumer depth remain verification-bound |
| [`tools/validators/archaeology/`](../../../tools/validators/archaeology/README.md) | Broad validator boundary is documented; accepted executable depth is not established |
| [`tools/validators/domains/archaeology/`](../../../tools/validators/domains/archaeology/README.md) | Domain-specific validator boundary is documented; accepted executable depth is not established |
| [`data/proofs/archaeology/`](../../../data/proofs/archaeology/README.md) | Draft proof-lane guidance; concrete proof schemas, payloads, validators, access controls, and release linkage remain unresolved |
| Archaeology policy lane | Deny-by-default intent documented; concrete bundle, tests, CI binding, and runtime enforcement remain unverified |
| Release schemas | Mixed scaffold maturity; schema validity alone cannot prove cultural, evidence, policy, or release closure |
| Candidate lane | Parent README only in the bounded inspection; no child dossier established |

### Required negative cases

A mature, synthetic, public-safe, no-network suite should reject:

- missing or mutable artifact pointers;
- protected detail in dossier text, filenames, logs, snapshots, reports, or CI artifacts;
- unresolved source identity, rights, access, sensitivity, or source role;
- candidate/anomaly/model-to-confirmed-site promotion;
- cultural authority inferred by KFM rather than recorded from the named authority;
- expired, revoked, or missing consent;
- missing embargo or revocation handling;
- unresolved or stale `EvidenceRef` values;
- absent redaction/generalization receipts;
- transforms that remain reverse-engineerable;
- synthetic or reconstructed material presented as observation;
- missing policy, cultural review, reviewer, manifest, correction, or rollback support;
- direct public access to candidate, processed, catalog, proof, or restricted stores; and
- generated language presented as evidence, cultural interpretation, or approval.

A passing test proves only the declared test scope. It does not confirm a site, clear rights, confer cultural approval, approve a candidate, or release an artifact.

[Back to top](#top)

---

## Automation posture

| Workflow | Current boundary |
|---|---|
| [`domain-archaeology`](../../../.github/workflows/domain-archaeology.yml) | Read-only readiness holds for validation, proof, and release-dry-run maturity; no protected payload access, cultural decision, or release |
| [`release-dry-run`](../../../.github/workflows/release-dry-run.yml) | TODO-only jobs that echo candidate assembly, promotion gate, and rollback-card checks |

`domain-archaeology` currently:

- uses ordinary pull-request and push triggers plus `workflow_dispatch`;
- declares `contents: read`;
- uses GitHub-hosted runners;
- disables persisted checkout credentials;
- checks that this lane contains no non-README candidate record;
- checks sampled test topology without opening protected payloads;
- checks proof-lane and validator maturity; and
- reports explicit `WORKFLOW_HOLD` outcomes while accepted executable commands are absent.

The literal `publication-not_yet` badge in this README is retained for the current workflow's readiness check. It is not a release state or approval.

The general `release-dry-run` workflow still produces TODO-only jobs. A green result is not candidate assembly, promotion-gate enforcement, rollback verification, cultural approval, release approval, or publication authority.

Branch protection, required-check coupling, immutable action pinning, workflow-run history, and independent reviewer enforcement remain separate evidence.

[Back to top](#top)

---

## Release handoff routing

Use the narrowest accepted shared lane for the next record:

| Record or action | Route | Candidate-lane boundary |
|---|---|---|
| Candidate dossier | This lane | Pre-publication review only |
| Promotion decision | [`release/promotion_decisions/`](../../promotion_decisions/README.md) | May permit manifest preparation; does not publish |
| Release manifest | [`release/manifests/`](../../manifests/README.md) or accepted successor | Canonical singular/plural and Archaeology segmentation remain unresolved |
| Correction notice | [`release/correction_notices/`](../../correction_notices/README.md) | Communication record; not correction authority by itself |
| Rollback/review card | [`release/rollback_cards/`](../../rollback_cards/README.md) or accepted successor | Current parent describes review cards; rollback semantics remain conflicted |
| Withdrawal notice | [`release/withdrawal_notices/`](../../withdrawal_notices/README.md) | Notice must point to a governed withdrawal decision |
| Release history | [`release/changelog/`](../../changelog/README.md) | Narrative companion, not sovereign release state |
| Published carrier | [`data/published/archaeology/`](../../../data/published/archaeology/README.md) | Downstream only after governed release |

The Archaeology domain `RELEASE_INDEX.md` is a docs-plane navigator. It must mirror verified release-plane state without becoming a release authority or exposing protected detail.

The repository still carries manifest, correction, and rollback topology drift. Candidate authors must surface that conflict rather than silently selecting or duplicating homes.

[Back to top](#top)

---

## Correction, withdrawal, and rollback

Archaeology correction and rollback must account for more than file replacement.

A defect may require:

- candidate hold or withdrawal;
- manifest supersession;
- correction notice;
- public carrier removal or replacement;
- cache, tile, search, graph, embedding, preview, and AI-output invalidation;
- consent or embargo re-evaluation;
- review-record update;
- rights-holder notification where required;
- tombstone or safe absence marker;
- audit and receipt update; and
- verification that protected detail is no longer exposed or inferable.

### Rollback triggers

Examples include:

- evidence invalidation;
- source-rights change;
- cultural or sovereignty review revocation;
- consent withdrawal or embargo activation;
- sensitivity misclassification;
- redaction/generalization failure;
- protected detail in map, API, report, screenshot, cache, index, or AI output;
- candidate presented as confirmed site;
- stale or superseded interpretation shown as current;
- broken correction lineage;
- release without required separation of duties; or
- rollback target that cannot be verified.

Use the [`Archaeology Rollback Runbook`](../../../docs/runbooks/archaeology/ROLLBACK_RUNBOOK.md) as governance guidance. Its implementation maturity remains bounded and must not be treated as proof that rollback automation exists.

[Back to top](#top)

---

## Review and separation of duties

[`CODEOWNERS`](../../../.github/CODEOWNERS) routes `/release/` and Archaeology domain documentation review to `@bartytime4life`. That is GitHub review routing only.

Before an Archaeology candidate reaches manifest preparation, verify distinct responsibility for:

- Archaeology domain meaning and candidate scope;
- artifact production and pipeline operation;
- source admission, rights, and source-role assignment;
- evidence and proof closure;
- sensitivity and redaction/generalization disposition;
- cultural, tribal, sovereignty, consent, and rights-holder review where applicable;
- deterministic validation and public no-leak cases;
- representation/reality-boundary review;
- release decision and manifest review; and
- correction, revocation, withdrawal, supersession, and rollback.

The generator or candidate author must not be treated as the sole approver for sensitive release work. Merge approval remains separate from cultural authority, consent, release, and publication approval.

### Review burden

| Change | Minimum review posture |
|---|---|
| README-only lane guidance | Docs/release-root review with sensitive-content check |
| New candidate identity or scope | Archaeology domain + release review |
| Candidate artifact or source-set change | Domain + data/pipeline + source/rights review |
| Location precision, transform, or audience change | Sensitivity + policy + no-leak review |
| Cultural, sacred, burial, oral-history, or community-controlled scope | Named cultural/rights-holder/sovereignty review |
| Consent, embargo, or revocation change | Consent authority + policy + release/correction review |
| `READY_FOR_REVIEW` transition | Domain, evidence, policy, sensitivity, cultural-review, validation, and release reviewers identified |
| `APPROVED_FOR_MANIFEST` transition | Independent release decision and complete safe support pointers |
| Supersession, withdrawal, correction, revocation, or rollback | Release + domain + cultural/rights + correction/rollback ownership |

[Back to top](#top)

---

## Maintenance and definition of done

Update this README when:

- a candidate child is added, renamed, superseded, withdrawn, denied, or removed;
- a candidate changes finite state;
- manifest, promotion-decision, correction, withdrawal, or rollback topology changes;
- candidate schemas, validators, fixtures, proof producers, policy rules, or CI mature;
- sensitivity, sovereignty, consent, or cultural-review doctrine changes;
- CODEOWNERS or stewardship assignments change;
- a release or rollback changes the docs-plane index; or
- a correction reveals that this README overstated repository maturity or exposed unsafe detail.

### Definition of done for this lane

This lane may graduate beyond draft only when:

- [ ] child inventory is generated or deterministically validated without reading protected payloads;
- [ ] every indexed child exposes a stable identity, version, status, finite decision, and immutable evidence snapshot;
- [ ] candidate filenames and public metadata cannot leak protected location or cultural substance;
- [ ] source, evidence, rights, sensitivity, sovereignty, consent, transform, policy, validation, review, correction, and rollback fields are machine-checkable or explicitly governed;
- [ ] candidate-local versus shared release-record topology is resolved by accepted decision and migration guidance;
- [ ] substantive synthetic positive and negative fixtures and tests exist;
- [ ] validators produce public-safe diagnostics with stable reason codes;
- [ ] candidate validation and release dry-run commands are deterministic and no-network by default;
- [ ] CI invokes accepted commands and cannot turn missing coverage into success;
- [ ] branch protection and reviewer requirements are verified;
- [ ] cultural-review and revocation paths are operationally tested without exposing controlled content;
- [ ] correction, cache invalidation, withdrawal, and rollback drills have evidence; and
- [ ] public surfaces remain downstream of governed APIs and released artifacts.

[Back to top](#top)

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Prior parent README, blob `2047236f…` | `CONFIRMED` | Existing generic candidate-lane purpose and dossier outline | Did not reflect current workflow, test, proof, policy, or no-active-candidate maturity |
| [`release/candidates/README.md`](../README.md) | `CONFIRMED file / draft guidance` | Parent states and common review fields | Does not prove Archaeology candidate completeness |
| Bounded repository search | `CONFIRMED search` | Surfaced this parent README but no child candidate dossier | Not a permanent recursive filesystem proof |
| [`RELEASE_INDEX.md`](../../../docs/domains/archaeology/RELEASE_INDEX.md) | `CONFIRMED docs index / placeholder rows` | Docs-plane release navigation and no-sensitive-geometry posture | Does not prove release-plane records or public artifacts |
| [`PUBLICATION_AND_POLICY.md`](../../../docs/domains/archaeology/PUBLICATION_AND_POLICY.md) | `CONFIRMED doctrine-facing doc / proposed implementation` | Trust membrane, release review, policy, correction, and rollback expectations | Does not prove executable enforcement |
| [`SENSITIVITY.md`](../../../docs/domains/archaeology/SENSITIVITY.md) | `CONFIRMED sensitivity doctrine / proposed profiles` | Deny-by-default, review, transform, revocation, and no-leak posture | Profile implementations and parameters remain verification-bound |
| [`CULTURAL_REVIEW.md`](../../../docs/domains/archaeology/CULTURAL_REVIEW.md) | `CONFIRMED protocol / proposed operational records` | Named-authority, cultural review, consent, revocation, CARE, and sovereignty governance | Does not substitute for substantive human consultation or approval |
| [`policy/domains/archaeology/`](../../../policy/domains/archaeology/README.md) | `CONFIRMED file / draft lane` | Policy families and fail-closed obligations | Concrete bundle and runtime enforcement remain unknown |
| [`data/proofs/archaeology/`](../../../data/proofs/archaeology/README.md) | `CONFIRMED file / proposed proof lane` | Evidence and proof boundary | No concrete proof payload or accepted producer established |
| [`tests/domains/archaeology/`](../../../tests/domains/archaeology/README.md) | `CONFIRMED named topology / sampled placeholders` | Intended no-leak, evidence, rights, review, release, and rollback coverage | Executable suite and pass rates remain unestablished |
| `test_public_no_leak.py` | `CONFIRMED one-line placeholder` | Demonstrates filename presence is not executable proof | One sampled module does not establish every module's content |
| [`domain-archaeology`](../../../.github/workflows/domain-archaeology.yml) | `CONFIRMED readiness workflow` | Read-only holds and no-candidate detector | Green hold is not candidate, cultural, evidence, or release proof |
| [`release-dry-run`](../../../.github/workflows/release-dry-run.yml) | `CONFIRMED TODO scaffold` | General release orchestration placeholder | Green echo jobs are not substantive validation |
| [`data/published/archaeology/`](../../../data/published/archaeology/README.md) | `CONFIRMED published-lane README` | Public-safe carrier boundary and release prerequisites | Emitted artifact inventory remains unverified |
| Directory Rules and drift register | `CONFIRMED governance artifacts` | Responsibility-root separation and conflict visibility | Do not settle unresolved release topology by themselves |
| CODEOWNERS | `CONFIRMED routing` | Current GitHub review route | Not cultural authority, stewardship, independent approval, or branch-protection proof |

No external web research is required for this repository-state documentation update.

[Back to top](#top)

---

## Open verification

- [ ] Confirm exhaustive child inventory under `release/candidates/archaeology/`.
- [ ] Confirm candidate naming, public-safe identity, and versioning convention.
- [ ] Confirm canonical candidate artifact/staging path and artifact-manifest contract.
- [ ] Confirm accepted Archaeology candidate schema and validator command.
- [ ] Confirm admitted source records, rights, access classes, source roles, and safe source-head references.
- [ ] Confirm EvidenceRef-to-EvidenceBundle and proof-manifest contracts.
- [ ] Confirm public-safe review-record reference shape without exposing review substance.
- [ ] Confirm sensitivity and transform profile registry, receipt contracts, and no-reverse-engineering tests.
- [ ] Confirm cultural/tribal/rights-holder reviewer identity and authority-verification process.
- [ ] Confirm consent, revocation, embargo, tombstone, and cache-invalidation contracts.
- [ ] Confirm representation and reality-boundary contracts for 3D, model, anomaly, and synthetic carriers.
- [ ] Confirm executable Archaeology policy and deterministic public-safe fixtures.
- [ ] Confirm candidate-to-PromotionDecision and candidate-to-ReleaseManifest handoff.
- [ ] Resolve singular/plural manifest, correction, and rollback/review-card topology.
- [ ] Confirm correction consumers, withdrawal/supersession records, rollback target, and drill.
- [ ] Confirm candidate-specific no-network validation and release dry-run.
- [ ] Confirm `domain-archaeology` run behavior after this README revision.
- [ ] Confirm branch protection, required checks, immutable action pinning, and independent reviewer assignments.
- [ ] Confirm whether candidate inventory and status can be generated from machine-readable records without making generated output sovereign truth.
- [ ] Confirm public-release indexes can be updated without exposing protected location, cultural substance, or reverse-engineering aids.

[Back to top](#top)

---

## Changelog

### v2 — 2026-07-18

- Replaced generic Archaeology candidate guidance with a repository-grounded sensitive-domain candidate index and review contract.
- Recorded that no child candidate dossier is established by the bounded inspection.
- Preserved the workflow-compatible `publication-not_yet` marker without treating it as release state.
- Added responsibility routing, finite states and hold outcomes, candidate admission and identity rules, release gates, and a required dossier structure.
- Added sensitivity, sovereignty, cultural-review, consent, revocation, source-role, evidence, representation, validation, automation, correction, and rollback controls.
- Added current test, proof, policy, workflow, and published-lane maturity boundaries.
- Added separation-of-duties expectations, maintenance triggers, definition of done, evidence ledger, open verification, and documentation rollback.
- Added `CONTRACT_VERSION = "3.0.0"` and a bounded evidence snapshot.

### v1 — 2026-07-03

- Replaced the prior greenfield stub with initial Archaeology candidate-lane guidance.

[Back to top](#top)

---

## Rollback for this README

This revision changes documentation only.

Before merge, close the pull request or delete the scoped branch.

After merge, revert the generated-receipt commit and README commit in reverse order and restore the prior README blob:

```text
2047236f1f8d9a7fb0db8732bd6a492817ce94e5
```

No candidate artifact, source admission, pipeline state, evidence, cultural review, consent, policy, validation, manifest, release, publication, correction, withdrawal, revocation, supersession, or rollback state requires restoration.

[Back to top](#top)
