<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/standards/dp-budgets
title: KFM Standard — Differential Privacy Budgets
type: standard
version: v0.2.0
status: draft; guidance-only; operational-use-hold
owners:
  - NEEDS VERIFICATION — privacy steward
  - NEEDS VERIFICATION — data steward
  - NEEDS VERIFICATION — policy and security stewards
created: 2026-05-14
updated: 2026-08-18
policy_label: public
owning_root: docs/
responsibility: Human-readable differential-privacy budget, accounting, validation, and graduation guidance; no contract, schema, policy, runtime, release, or publication authority.
truth_posture: >-
  CONFIRMED exact target, standards-lane boundary, accepted Directory Rules v2,
  current draft sensitivity doctrine, current aggregation-receipt placement hold,
  proposed-inactive typed-receipt aggregation contract, absence of a verified
  DP-specific machine authority in the bounded current-repository inspection, and
  NIST SP 800-226 final publication / PROPOSED DP deployment profile, budget
  account, release-plan, receipt extensions, validation matrix, and graduation
  gates / UNKNOWN operative privacy parameters, accountant, ledger placement,
  runtime integration, release consumers, and accountable reviewers / NEEDS
  VERIFICATION exhaustive repository coverage, accepted semantic and machine
  contracts, policy enforcement, mechanism implementation, fixtures, validators,
  security review, utility review, correction propagation, and rollback rehearsal
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 31503aaadcf430499c5e3181f759db6b582a84c0
  prior_blob: 294a987ded1cb2e4d2a39a4522bc4c63f43dbb4d
  inspected_on: 2026-08-18
external_snapshot:
  nist_sp_800_226: final; published 2025-03; doi 10.6028/NIST.SP.800-226
  opendp_docs: stable documentation inspected 2026-08-18; not an admitted KFM dependency
  opendp_registry: transparency guidance inspected 2026-08-18; not KFM policy
related:
  - README.md
  - ../doctrine/sensitivity.md
  - SENSITIVITY_RUBRIC.md
  - REDACTION_PROFILES.md
  - CONSENT_TOKENS.md
  - ../security/DATA_CLASSIFICATION.md
  - ../../data/receipts/aggregation/README.md
  - ../../contracts/data/typed_receipt_aggregation.md
  - ../../schemas/contracts/v1/receipts/generated_receipt.schema.json
  - ../adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags:
  - kfm
  - privacy
  - differential-privacy
  - privacy-budget
  - composition
  - aggregate-release
  - standards
notes:
  - This document does not set a KFM epsilon, delta, privacy unit, mechanism, accountant, ledger location, or release policy.
  - Operational DP use remains HOLD until the graduation gates in this document close through owning authorities and current implementation evidence.
  - Differential privacy is not a geometry-redaction profile, a consent substitute, a rights decision, a release decision, or a security boundary.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KFM Standard — Differential Privacy Budgets

> **One-line purpose.** Define the evidence and governance packet required before KFM may claim that an aggregate release is differentially private, while keeping every operative parameter and implementation decision on explicit hold until accepted authorities and tested code exist.

[![Status: grounded draft](https://img.shields.io/badge/status-grounded%20draft-f59e0b?style=flat-square)](#status-and-operational-hold)
[![Operational use: hold](https://img.shields.io/badge/operational%20use-HOLD-b42318?style=flat-square)](#status-and-operational-hold)
[![Scope: aggregate releases](https://img.shields.io/badge/scope-aggregate%20releases-0969da?style=flat-square)](#scope-and-non-goals)
[![Default epsilon: none](https://img.shields.io/badge/default%20epsilon-none-6e7781?style=flat-square)](#budget-selection-no-default-numbers)
[![Authority: guidance only](https://img.shields.io/badge/authority-guidance%20only-6e7781?style=flat-square)](#authority-and-evidence-boundary)

> [!IMPORTANT]
> **This page is guidance, not a privacy guarantee or permission to release.** It does not adopt a differential-privacy variant, privacy unit, neighboring relation, mechanism, library, accountant, epsilon, delta, ledger, contract, schema, policy rule, validator, or runtime. A DP claim is admissible only after the complete deployment profile, implementation, evidence, policy, review, release, correction, and rollback packet has been verified.

> [!WARNING]
> **KFM has no default epsilon band.** Epsilon is not meaningful by itself. The unit of privacy, neighboring relation, DP variant, delta or other privacy-loss parameter, contribution bounds, query set, composition scope, trust model, public side releases, accuracy, and implementation security are part of the guarantee.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-and-evidence-boundary) · [Status](#status-and-operational-hold) · [Scope](#scope-and-non-goals) · [Vocabulary](#minimum-vocabulary) · [Profile](#deployment-profile-before-budget) · [Budget](#budget-selection-no-default-numbers) · [Accounting](#composition-and-budget-accounting) · [Lifecycle](#lifecycle-and-object-family-boundaries) · [Outcomes](#finite-outcomes-and-fail-closed-rules) · [Candidate fields](#candidate-records-not-wire-contracts) · [Implementation](#mechanism-and-implementation-requirements) · [Tests](#validation-and-negative-test-matrix) · [Gates](#graduation-gates) · [Correction](#correction-withdrawal-cache-and-reuse) · [Hazards](#privacy-hazards-and-anti-patterns) · [No-loss](#no-loss-modernization-ledger) · [Open](#open-verification-register) · [Sources](#source-ledger) · [Rollback](#maintenance-correction-and-rollback)

---

<a id="1-scope"></a>
<a id="purpose"></a>

## Purpose

Differential privacy (DP) is a mathematical framework for bounding privacy loss associated with a defined unit of privacy under a defined neighboring-dataset relation. In KFM, a future DP deployment would be one possible control for a **numeric aggregate release**. It would not make source records public-safe, settle rights or consent, redact exact geometry, authorize a release, or replace access control.

This standard exists to prevent a weak statement such as “noise was added” or “epsilon was small” from being presented as a KFM privacy guarantee. A credible claim must bind the mathematical guarantee to the release design, implementation, cumulative accounting, evidence, policy, review, and correction path.

This revision has four jobs:

1. disclose the current repository evidence and operational hold;
2. define the minimum deployment and accounting vocabulary;
3. make missing authority and implementation work testable; and
4. preserve useful prior concepts without retaining unsupported defaults or paths.

[Back to top](#top)

---

<a id="authority-and-evidence-boundary"></a>

## Authority and evidence boundary

[`docs/standards/`](./README.md) is the human-readable standards-guidance lane. It may explain upstream guidance and proposed KFM profiles, but machine meaning and permission remain separated:

| Question | Owning authority | This document's role |
|---|---|---|
| What a DP object means | An accepted semantic contract under `contracts/` | Describe candidate semantics; do not create authority |
| What fields and constraints are valid | An accepted schema under `schemas/` | List minimum candidate fields; do not claim a wire shape |
| Whether a release is allowed | `policy/`, qualified review, and the release decision plane | Explain fail-closed conditions; do not decide a case |
| What code implements a guarantee | Pinned implementation, dependency lock, tests, and measured outputs | State requirements; do not infer implementation |
| What privacy loss has been consumed | One accepted, atomic accounting authority | Define accounting obligations; do not choose its path |
| Whether evidence and release closure exist | Evidence, proof, manifest, review, correction, and rollback authorities | Require closure; do not substitute for it |
| Whether an external source is current | The authoritative upstream issuer at a dated snapshot | Record the external snapshot and currentness risk |

Accepted [`ADR-0029`](../adr/ADR-0029-adopt-directory-governance-standard-v2.md) makes the current Directory Rules v2 bytes the placement authority. This is a same-path update to an existing standards document. It creates no new authority root, object store, or runtime surface.

### Current evidence used

| Evidence | CONFIRMED bounded result | Consequence |
|---|---|---|
| [`docs/standards/README.md`](./README.md) | Standards pages are guidance and not conformance or release proof | This file cannot make DP operational |
| [`docs/doctrine/sensitivity.md`](../doctrine/sensitivity.md) | DP is described as **PROPOSED** for approved numeric aggregates and not as geometry generalization | Aggregate-only planning boundary retained |
| [`data/receipts/aggregation/README.md`](../../data/receipts/aggregation/README.md) | Current lane is README-only, placement-held, and does not prove an emitted AggregationReceipt or enforcing schema | No DP receipt instance or canonical write path is claimed |
| [`contracts/data/typed_receipt_aggregation.md`](../../contracts/data/typed_receipt_aggregation.md) | Contract is proposed, inactive, fixture-only, and explicitly non-authoritative | It is not a DP budget or release contract |
| Bounded current-tree and exact-path inspection | No accepted DP-specific semantic contract, schema, ledger, policy rule, mechanism implementation, fixture family, validator, emitted receipt, or runtime consumer was verified | Operational use remains `HOLD`; exhaustive absence is not claimed |
| NIST SP 800-226 | Final guidance published March 2025 | External evaluation framework; not KFM adoption |
| OpenDP stable documentation | Describes privacy units, privacy loss, composition, budget-aware query contexts, and filters | Implementation reference only; no dependency admission |

### Claim-strength rule

A commit proves that bytes exist at that commit. A green documentation check proves only the checked documentation assertions. A mathematical proof for a mechanism does not prove that KFM selected the right privacy unit, bounded contributions correctly, accounted for all releases, implemented the mechanism safely, or authorized publication.

[Back to top](#top)

---

<a id="status"></a>
<a id="status-and-operational-hold"></a>

## Status and operational hold

| Surface | Current state |
|---|---|
| Document path | `docs/standards/DP_BUDGETS.md` |
| Document role | Human-readable draft guidance |
| KFM DP profile | `UNKNOWN`; no accepted profile verified |
| Default epsilon or delta | **None** |
| Privacy unit and neighboring relation | `UNKNOWN`; use-case decision required |
| Mechanism, variant, and accountant | `UNKNOWN`; no admitted implementation verified |
| Canonical budget ledger and writer | `UNKNOWN`; placement and concurrency authority unresolved |
| Contract and schema | `NEEDS VERIFICATION`; no accepted DP-specific machine authority confirmed |
| Policy and review | `NEEDS VERIFICATION`; no active DP release rule confirmed |
| Fixtures, validator, and CI | `NEEDS VERIFICATION`; no DP-specific enforcement confirmed |
| Emitted release or receipt | `UNKNOWN`; none verified in the bounded inspection |
| Public or semi-public use | **HOLD** |

> [!CAUTION]
> The hold is not a recommendation to choose a convenient epsilon later. It means KFM must first define what is protected, from whom, across which releases, under which trust model, with what accuracy and equity burden, and through which accepted implementation and review authorities.

The hold may be lifted only for a named deployment profile after all [graduation gates](#graduation-gates) close. Approval for one profile does not establish a project-wide default.

[Back to top](#top)

---

<a id="2-doctrine--when-dp-applies-and-when-it-does-not"></a>
<a id="scope-and-non-goals"></a>

## Scope and non-goals

### Potentially eligible scope

A future KFM DP profile may cover a **defined numeric aggregate or model output** when all of the following are true:

- the privacy goal can be expressed with a meaningful unit of privacy and neighboring relation;
- the query domain, contribution bounds, and public information are specified before the private computation;
- the release family and cumulative composition scope are enumerable;
- the chosen mechanism and variant support the query and trust model;
- utility, bias, subgroup, and spatial/temporal accuracy are measured;
- rights, sensitivity, review, release, correction, and rollback obligations are independently satisfied; and
- the implementation and accounting path are accepted and tested.

Examples may include predeclared counts, bounded sums, histograms, or a separately reviewed DP machine-learning profile. Examples are not approvals.

### Out of scope or independently governed

| Surface | Required posture |
|---|---|
| Raw point coordinates, parcel links, site locations, or other exact geometry | Use approved suppression, redaction, generalization, aggregation, or denial. DP does not turn a point into truthful public geometry. |
| Record-level exports or identifier-bearing joins | Deny or use an independently governed restricted workflow. A DP aggregate does not de-identify the underlying table. |
| Consent, sovereignty, rights, source terms, or purpose limitation | Resolve independently. DP is not permission. |
| Data collection, storage, access control, incident response, or analyst trust | Govern independently. A release guarantee does not protect a breached canonical store. |
| Rank-5, T4, or otherwise denied material | DP does not unlock publication. |
| Small-denominator or sparse-geography release | Require an explicit release design; DP may be insufficient or may destroy utility. |
| Synthetic data | Treat as a separate release profile. “Synthetic” does not imply DP. |
| Privacy-preserving machine learning | Require a distinct profile covering training, sampling, clipping, accounting, model release, attacks, and utility. |
| Non-private public aggregates | Do not imply that adding noise automatically improves governance; define the purpose and utility cost. |

### Anti-collapse rule

Sensitivity classification, geometry redaction, k-thresholding, differential privacy, access control, consent, evidence, and release are separate controls. One may complement another, but no control silently satisfies the others.

[Back to top](#top)

---

<a id="minimum-vocabulary"></a>

## Minimum vocabulary

A DP claim is incomplete unless the terms below are bound to concrete, reviewed values.

| Term | Required meaning |
|---|---|
| **Protected entity / privacy unit** | What one protected contribution means: a person, household, organization, event, person-period, or another justified unit |
| **Neighboring relation** | Exactly how two admissible datasets may differ; bounded and unbounded models are not interchangeable |
| **Contribution bounds** | Maximum rows, groups, time windows, geography units, or value range attributable to one privacy unit, plus the enforcement transform |
| **Data domain** | Types, bounds, allowed categories, public bins, null handling, and invariants known independently of private data |
| **Query or workload** | The exact statistic, vector of statistics, model, or interactive query family |
| **DP variant / privacy measure** | Pure DP, approximate DP, zero-concentrated DP, Rényi DP, or another accepted formulation, including original parameters |
| **Mechanism** | The accepted library constructor and mechanism applied to the defined domain, metric, sensitivity, and privacy measure |
| **Privacy-loss parameters** | Epsilon and delta where applicable, plus original parameters when converted from another variant |
| **Trust model** | Central, local, shuffle, secure-computation-assisted, or another explicit model |
| **Query model** | Prespecified data release, interactive query answering, model release, or another explicit release model |
| **Composition group** | The set of releases that must be accounted together because they protect the same or overlapping privacy units |
| **Public or unprotected information** | Invariants, bins, totals, schemas, and side releases excluded from the guarantee, with a privacy rationale |
| **Budget account** | The accepted authority that reserves, commits, and reports cumulative privacy loss |
| **Utility and fairness profile** | Accuracy targets, uncertainty, bias tests, subgroup/geography/time evaluations, and stopping criteria |
| **Release artifact** | Immutable bytes and metadata actually exposed, not merely the query plan |
| **Correction lineage** | How supersession, withdrawal, cache invalidation, and future accounting remain traceable |

### Comparability rule

Do not compare two DP claims by epsilon alone. At minimum, compare the privacy unit, neighboring relation, variant, delta or original privacy-loss parameters, contribution bounds, workload, composition scope, trust model, public information, and implementation assumptions.

NIST SP 800-226 specifically warns that guarantees with different deltas or units of privacy are not directly comparable and that a poorly chosen unit may fail to cover the real-world situations the adversary seeks to distinguish.

[Back to top](#top)

---

<a id="deployment-profile-before-budget"></a>

## Deployment profile before budget

Budget selection comes **after** a named deployment profile is defined. The profile is a candidate governance object, not an accepted KFM contract.

### Minimum profile packet

| Area | Required record |
|---|---|
| Purpose | Intended use, users, decisions supported, prohibited uses, and expected lifetime |
| Harm model | Protected entities, sensitive facts, plausible adversaries, side information, and failure consequences |
| Source and rights | Source identity, authority role, rights, consent or sovereignty obligations, retention, and sensitivity |
| Privacy definition | Unit, neighboring relation, bounded/unbounded posture, variant, and trust model |
| Data and contribution model | Domain, bounds, clipping/truncation, deduplication, group limits, time and geography limits |
| Workload | Exact query set or interactive query grammar, public bins, invariants, and post-processing |
| Mechanism | Library, pinned version, constructor, parameters, accountant, and security assumptions |
| Budget | Per-operation reservation, total cap, time horizon, composition groups, and exhaustion behavior |
| Utility | Accuracy targets and measured burden by subgroup, geography, time, and edge case |
| Transparency | Public description of the guarantee, protected unit, parameters, limitations, and known non-DP releases |
| Operations | Writers, ledger transaction model, monitoring, incident response, correction, withdrawal, and rollback |
| Review | Privacy, domain, data, security, policy, release, and independent review evidence |

### Query-model choice

A prespecified data release has a finite workload that can be reviewed before publication. An interactive query service adds query authorization, adaptive composition, concurrency, analyst trust, side-channel, and exhaustion risks. KFM must not present an interactive endpoint as a simple extension of a static release.

[Back to top](#top)

---

<a id="6-epsilon-budget-table-proposed"></a>
<a id="budget-selection-no-default-numbers"></a>

## Budget selection: no default numbers

This standard intentionally contains **no numeric epsilon or delta defaults and no public/internal/restricted bands**. Deployment choices are context-specific and must be approved for one named profile.

### Required selection process

1. Define the harm model and strongest practical privacy unit.
2. Define adjacency, contribution bounds, public information, and the complete workload.
3. Select the DP variant, mechanism, trust model, and accountant.
4. Set candidate privacy-loss parameters as a governance decision, not a library default.
5. Evaluate accuracy, uncertainty, bias, subgroup disparity, geographic distortion, temporal distortion, and decision fitness across a parameter grid.
6. Account for every overlapping release, side release, prior public artifact, and planned correction.
7. Record the chosen point and rejected alternatives with their privacy and utility tradeoffs.
8. Obtain the required reviews before any real-data release.
9. Publish a bounded transparency record appropriate to the audience and sensitivity.
10. Monitor the deployed profile and stop releases when assumptions or utility evidence drift.

### Parameter rules

- Lower epsilon generally represents a stronger guarantee **only when the rest of the definition is fixed**.
- Delta is not a generic tolerance knob. Its interpretation, value, population relationship, and composition must be justified.
- If a guarantee is converted from another privacy measure, retain the original measure and parameters so reviewers can evaluate or recompute the conversion.
- A value copied from another deployment is evidence about that deployment, not a KFM default.
- Library examples, tutorials, and test constants are not policy.
- Accuracy targets must be specified before selecting the final budget, then verified on representative synthetic or approved benchmark data.
- A release that cannot meet minimum utility without an unacceptable privacy loss returns `ABSTAIN` or remains on `HOLD`; KFM does not weaken the declared unit silently.

### Transparency minimum

A public-facing DP claim should state, at a level that does not expose restricted operations:

- the protected unit and neighboring relation;
- the DP variant and privacy-loss parameters;
- the release or query model;
- the composition scope and reporting period;
- the principal contribution bounds and public information;
- the mechanism family and implementation version;
- known limitations, accuracy evidence, and correction state; and
- a stable release and evidence reference.

[Back to top](#top)

---

<a id="7-composition-and-cross-dataset-budgets"></a>
<a id="composition-and-budget-accounting"></a>

## Composition and budget accounting

Privacy loss composes across analyses that protect the same or overlapping units. KFM therefore needs one accepted accounting authority before a DP deployment may graduate.

### Account identity

A budget account must be keyed by the dimensions that determine composition, not merely a dataset name:

- deployment-profile identifier and version;
- protected entity and privacy unit;
- neighboring relation;
- source population or governed cohort identity;
- jurisdiction, geography, and time horizon;
- release/query model;
- DP variant and accountant;
- composition group and declared disjointness evidence; and
- policy and review version.

### Transaction states

| State | Meaning | Required behavior |
|---|---|---|
| `PROPOSED` | Candidate query or release has not reserved budget | No private computation or public artifact |
| `RESERVED` | Atomic reservation acquired for a bounded operation | Prevent concurrent oversubscription; expiration and cancellation rules explicit |
| `COMMITTED` | A new disclosure was produced or exposed | Append-only expenditure; bind exact artifact and receipt |
| `CANCELLED_BEFORE_DISCLOSURE` | Reservation ended with proof no output escaped | Release reservation under accepted rules; preserve audit record |
| `HELD` | Accounting, policy, utility, or review evidence is incomplete | No release |
| `EXHAUSTED` | Proposed operation exceeds the accepted cap or filter | Deny the operation; do not silently reset the period |
| `WITHDRAWN_AFTER_DISCLOSURE` | Artifact is no longer served | **Do not refund privacy loss**; preserve expenditure and correction lineage |
| `ERROR` | Ledger, accountant, or atomicity failed | Fail closed; produce no release |

### Accounting rules

- Use a conservative composition rule unless a tighter accountant is accepted, implemented, and reviewable.
- Preserve the original privacy measure and parameters; do not report only a converted epsilon.
- Prove disjointness before using parallel-composition assumptions. Unknown overlap composes.
- Predeclare whether repeated time windows are independent; do not assume person-day or person-year independence.
- A query retry that can produce different noisy output is a new disclosure candidate and must be accounted.
- Bit-for-bit re-delivery of an already released immutable artifact may be classified as the same disclosure only when identity and bytes are verified; prefer serving the existing artifact rather than regenerating it.
- Withdrawing, deleting, rolling back, or correcting a released artifact does not erase information already observed and does not restore the budget.
- Mixed DP and non-DP releases over the same population must be evaluated together. DP does not mitigate leakage from unrestricted side releases.
- Interactive services require atomic reservations, privacy filters or odometers where appropriate, abuse controls, rate limits, query canonicalization, and a defined response when the accounting service is unavailable.
- Budget summaries may be public, but internal identifiers, security controls, and restricted population details remain policy-bounded.

### Placement hold

This standard does not choose a ledger path. The current aggregation-receipt README records unresolved child-lane placement and no accepted DP object family was verified. Ledger placement, physical storage, mutability, retention, access, writer identity, transaction semantics, and backup/restore therefore remain `NEEDS VERIFICATION`.

[Back to top](#top)

---

<a id="8-lifecycle-placement"></a>
<a id="lifecycle-and-object-family-boundaries"></a>

## Lifecycle and object-family boundaries

DP does not alter KFM's lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

| Stage | Permitted DP-related activity | Required boundary |
|---|---|---|
| RAW | Preserve admitted source material or immutable reference | Never overwrite raw evidence with noisy derivatives |
| WORK | Develop the aggregate, bounds, mechanism, utility study, and candidate release plan | Restricted, no public path; failures go to quarantine |
| QUARANTINE | Hold unresolved rights, privacy unit, accounting, utility, security, or policy cases | Record finite reason and review route |
| PROCESSED | Store a validated candidate output and process receipt | Not released; receipt is process memory, not proof |
| CATALOG / TRIPLET | Emit discoverability and provenance projections from accepted objects | Catalog presence does not authorize exposure |
| PUBLISHED | Serve immutable, reviewed, policy-approved output through governed delivery | Bind release, evidence, budget transaction, correction, and rollback references |

### Separation of object families

| Object family | Owns | Must not be used as |
|---|---|---|
| `SourceDescriptor` and source capture | Source identity, terms, retrieval, and authority role | DP permission |
| `EvidenceRef` / `EvidenceBundle` | Support for factual and methodological claims | Budget ledger |
| Sensitivity, rights, consent, and `PolicyDecision` | Admissibility and obligations | Mathematical proof |
| Candidate DP deployment profile | Privacy definition and release design | Accepted policy until reviewed |
| Candidate budget account and transaction | Composition and cumulative expenditure | Release approval |
| `RunReceipt`, `TransformReceipt`, or `AggregationReceipt` | Process memory and parameters | Proof, review, or publication |
| Validation and utility reports | Bounded test results | General safety guarantee |
| `ReleaseManifest` and authorized decision | Exact released artifacts and state transition | Source truth |
| Correction, withdrawal, and rollback records | Downstream remediation and lineage | Privacy-loss refund |
| Map, tile, API, export, graph, or AI output | Governed delivery or interpretation | Sovereign truth |

### Geometry boundary

A DP-protected count grid may be a released derivative of sensitive observations. It does not authorize exposing the source points, and its cells must not be described as precise occurrence locations. Geometry redaction and representation honesty remain separate obligations.

[Back to top](#top)

---

<a id="4-decision-flow"></a>
<a id="finite-outcomes-and-fail-closed-rules"></a>

## Finite outcomes and fail-closed rules

This document does not create a new policy-decision vocabulary. It maps DP failures into KFM's established outward outcomes:

| Condition | Outward result | Required record |
|---|---|---|
| Released, in-scope aggregate; evidence, DP profile, accounting, policy, review, citation, and release all close | `ANSWER` | Stable release and evidence references |
| Evidence, privacy definition, accuracy, or requested scope is insufficient | `ABSTAIN` | Bounded reason; no claim of DP safety |
| Rights, sensitivity, prohibited use, invalid unit, unbounded contribution, budget exhaustion, or release policy blocks exposure | `DENY` | Policy/review reason without leaking sensitive details |
| Mechanism, dependency, ledger, validator, receipt, identity, or runtime fails | `ERROR` | Incident-safe error; no permissive fallback |

### Mandatory fail-closed cases

The release remains held or denied when any of these is unknown or invalid:

- privacy unit or neighboring relation;
- contribution bounds or value domain;
- private-data-derived bins or query domain without a private selection mechanism;
- complete workload and composition scope;
- original privacy-loss measure and parameters;
- budget reservation or committed-expenditure state;
- implementation version, mechanism constructor, or security posture;
- accuracy, bias, subgroup, spatial, and temporal evaluation;
- rights, consent, sovereignty, sensitivity, review, or source role;
- evidence, release manifest, correction path, or rollback target; or
- public side releases that may invalidate the stated harm model.

[Back to top](#top)

---

<a id="5-required-receipt-fields"></a>
<a id="candidate-records-not-wire-contracts"></a>

## Candidate records, not wire contracts

The names and fields below are **PROPOSED semantic candidates**. They do not prove that corresponding schemas or runtime objects exist.

### Candidate `DPDeploymentProfile`

| Field group | Minimum content |
|---|---|
| Identity | `profile_id`, version, owner roles, status, supersession |
| Purpose | intended use, prohibited uses, protected entities, harm model |
| Privacy definition | unit, adjacency, bounded/unbounded model, variant, trust and query models |
| Domain and bounds | data domain, categories/bins, value bounds, contribution bounds and enforcement |
| Workload | query set or grammar, invariants, public information, post-processing |
| Implementation | library, version, mechanism constructor, accountant, dependency and security references |
| Budget | cap, period, composition groups, reservations, exhaustion policy |
| Utility | target metrics, subgroup/geography/time tests, accepted thresholds |
| Governance | rights, sensitivity, policy, review, transparency, correction and rollback |

### Candidate `DPBudgetRecord`

The current sensitivity doctrine names a proposed `DPBudgetRecord`. A minimum candidate would include:

- dataset and release/query references;
- jurisdiction, cohort, and composition-group identity;
- privacy unit and neighboring relation;
- contribution and value bounds;
- DP variant, mechanism, original and reported privacy-loss parameters;
- accountant and composition rule;
- reservation, commitment, cancellation, exhaustion, and disclosure timestamps;
- exact released artifact digest;
- policy, review, evidence, receipt, release, correction, and rollback references;
- **randomness handling policy, never a public production seed**; and
- finite outcome and reason code.

### Candidate DP-bearing receipt extension

A DP-bearing process receipt should record enough to audit the operation without becoming the ledger or leaking protected implementation secrets:

| Field | Requirement |
|---|---|
| Profile and workload refs | Exact profile version and canonical query/workload identity |
| Input refs | Governed source/version and approved private-data identity, not private rows |
| Domain and bounds | Unit, adjacency, contribution bounds, value bounds, and public bins |
| Mechanism | Library, pinned version, constructor/profile, privacy measure, and accountant |
| Privacy loss | Reserved and committed parameters, original measure, composition group, transaction ref |
| Output | Exact artifact digest, schema/profile, uncertainty and utility report refs |
| Decisions | Policy, review, evidence, release, correction, and rollback refs |
| Security | Execution environment and dependency attestation refs where adopted |
| Randomness | Generator/profile and operational handling; no public seed or secret state |

> [!CAUTION]
> Production randomness is not a reproducibility souvenir. Synthetic fixtures may use explicit deterministic seeds to test code paths. Real releases should preserve exact released bytes and implementation metadata rather than publish secret randomness or regenerate new noise as a “replay.”

### Candidate `DPValidationReport`

A validation report should identify the exact profile, fixture/benchmark set, implementation revision, parameter sweep, privacy checks, utility and bias results, failures, and the limited assertions the report proves.

[Back to top](#top)

---

<a id="3-library-choices"></a>
<a id="mechanism-and-implementation-requirements"></a>

## Mechanism and implementation requirements

No library is approved by this document. A future implementation must pass dependency admission and demonstrate the complete guarantee, not merely call a function named `laplace` or `gaussian`.

### Implementation minimums

- Use a maintained DP library or formally reviewed implementation; handwritten production mechanisms are denied by default.
- Pin the exact dependency and feature set through the repository's admitted dependency authority.
- Construct the mechanism from explicit domains, metrics, contribution bounds, sensitivity, privacy measure, and accountant.
- Use public, predeclared bins and categories, or account for their private selection.
- Treat clipping, truncation, deduplication, sampling, partition selection, and thresholding as guarantee-bearing transforms.
- Document all invariants and non-DP side releases.
- Test integer and floating-point behavior, discrete mechanisms where appropriate, overflow, underflow, NaN/infinity, and serialization.
- Address timing, error-message, memory, cache, and other side channels for the chosen query model.
- Keep canonical data encrypted and access-controlled; DP does not compensate for a breach.
- Separate test randomness from production randomness.
- Make budget reservation and commit atomic with artifact identity.
- Bind exact implementation, policy, schema, profile, and release versions to the receipt.
- Prevent direct public access to canonical/private stores and analyst tooling.
- Define dependency vulnerability response, incident response, and emergency release suspension.
- Prove deterministic identity for plans and artifacts without requiring deterministic production noise.

### Utility, bias, and representation

A DP release may be mathematically valid and still be unfit or misleading. Validation must include:

- absolute and relative error;
- confidence or accuracy intervals appropriate to the mechanism;
- zero, negative, fractional, clipped, and inconsistent outputs;
- rare categories and small geographies;
- subgroup disparity and systemic/statistical bias;
- temporal trend distortion and repeated-release effects;
- spatial pattern distortion, map classification effects, and visual thresholds;
- downstream ratios, rankings, models, and decisions;
- reproducible post-processing; and
- explicit labels that the output is a privacy-protected estimate, not canonical truth.

[Back to top](#top)

---

<a id="11-validation"></a>
<a id="validation-and-negative-test-matrix"></a>

## Validation and negative-test matrix

The first implementation slice must be deterministic, synthetic, no-network, and unable to touch a live sensitive source or publication surface.

| Case | Expected result | Required proof |
|---|---|---|
| Valid prespecified count release over one bounded synthetic user contribution with public bins | Candidate `PASS`; no publication | Schema, privacy map, accounting reservation/commit, utility assertions, exact artifact digest |
| Missing privacy unit or adjacency | `ABSTAIN` / `HOLD` | Stable reason; no mechanism execution |
| Event-level unit used for a stated user-level harm without justification | `DENY` | Harm-model mismatch fixture |
| Unbounded rows, groups, values, time windows, or geographies | `DENY` | Contribution-bound validator |
| Bins or categories inferred from private data without private selection | `DENY` | Domain/public-information validator |
| Missing, stale, or unavailable ledger | `ERROR` | Fail-closed; no artifact exposed |
| Concurrent reservations exceed cap | One atomic winner; others `DENY` or `ERROR` | Race/replay test and immutable transaction trail |
| Budget exhausted | `DENY` | No silent period reset or override |
| Overlap declared disjoint without evidence | Compose conservatively or `HOLD` | Disjointness fixture |
| Same query rerun with fresh randomness | New reservation required | Accounting test |
| Exact previously released bytes re-served | Same disclosure identity | Digest and release-identity test |
| Released artifact withdrawn | Budget remains committed | Correction/withdrawal test |
| Public receipt contains a production seed or restricted population details | `DENY` | Receipt-safety validator |
| Custom floating-point mechanism lacks implementation review | `DENY` | Dependency/mechanism admission test |
| Non-DP side release invalidates the harm model | `HOLD` / `DENY` | Mixed-release inventory test |
| Accuracy or subgroup threshold fails | `ABSTAIN` | Utility report and no publication |
| DP label applied to raw points or exact geometry | `DENY` | Output-class validator |
| Policy, rights, consent, sensitivity, review, evidence, or release ref missing | `DENY` or `ABSTAIN` by owning authority | Cross-object closure fixture |
| Ledger commit succeeds but artifact write fails, or inverse | `ERROR` and recovery path | Transaction/compensation test; no ambiguous disclosure state |
| Correction regenerates different noise without accounting | `DENY` | Correction regression fixture |
| Validator or accountant crashes | `ERROR` | No fallback to allow |

### Required test layers

1. contract and schema positive/negative fixtures;
2. mechanism-level privacy-map and domain tests;
3. accounting state-machine, concurrency, replay, and exhaustion tests;
4. utility, bias, subgroup, geography, and time tests;
5. policy and cross-object closure tests;
6. security and side-channel review appropriate to the query model;
7. correction, withdrawal, cache invalidation, and rollback rehearsal;
8. release dry run proving no real source activation or public write; and
9. aggregate and boundary validation at the exact branch head.

A test pass proves only the assertions encoded by that test. It does not independently prove legal compliance, source rights, adequate privacy, utility, or release approval.

[Back to top](#top)

---

<a id="graduation-gates"></a>

## Graduation gates

Operational DP use remains `HOLD` until all applicable gates close for one named deployment profile.

| Gate | Required closure |
|---|---|
| **G0 — Authority and ownership** | Accepted owner roles, review route, contract/schema/policy homes, ledger authority, and separation of duties |
| **G1 — Use case and harm model** | Named release, users, decisions, protected entities, adversaries, prohibited uses, and stopping conditions |
| **G2 — Source, rights, and sensitivity** | Admitted sources, rights, consent/sovereignty, retention, classification, and public-safe purpose |
| **G3 — Privacy definition** | Privacy unit, neighboring relation, bounded/unbounded model, variant, trust model, and query model |
| **G4 — Domain and contribution bounds** | Public domain/categories, value bounds, row/group/time/geography bounds, deduplication, clipping, and private selection |
| **G5 — Mechanism and dependency** | Admitted library/version/features, exact constructor, accountant, original parameters, threat model, and supply-chain review |
| **G6 — Budget and utility decision** | Candidate parameter sweep, composition plan, accuracy/bias/equity review, chosen values, rejected alternatives, and qualified approval |
| **G7 — Accounting authority** | Atomic account identity, reservations, commits, replay, overlap, exhaustion, retention, backup/restore, and audit behavior |
| **G8 — Contracts, schemas, and policy** | Accepted semantic and machine contracts, compatibility rules, reason codes, fail-closed policy, and no parallel authority |
| **G9 — Fixtures, validators, and CI** | Synthetic positive/negative matrix, deterministic validation, exact-head CI, and no-network proof |
| **G10 — Security and operations** | Access control, canonical-store protection, side-channel review, monitoring, incident response, dependency response, and release suspension |
| **G11 — Release and correction closure** | Evidence, review, immutable artifact, transparency record, manifest, cache behavior, correction, withdrawal, rollback, and downstream propagation |
| **G12 — Bounded pilot and post-release review** | One approved pilot, observed accuracy and accounting, independent review, documented residual risks, and explicit decision before expansion |

A gate may close only with owning-surface evidence. This document cannot close any gate by assertion.

[Back to top](#top)

---

<a id="correction-withdrawal-cache-and-reuse"></a>

## Correction, withdrawal, cache, and reuse

### Privacy loss is not reversible

Once a new DP output is exposed to an audience, withdrawing it does not remove the information already learned. Its committed privacy loss remains in the account.

### Correction rules

- Prefer correcting metadata, citations, labels, or non-sensitive post-processing without regenerating the private measurement when mathematically and semantically valid.
- When the private query, input population, bounds, mechanism, parameters, or random draw changes, treat the result as a new disclosure candidate and account it.
- Serve exact immutable released bytes for re-downloads and cache fills; do not rerun the mechanism on every request.
- Bind API, tile, export, report, graph, search, and AI representations to the same release identity and correction state.
- Purge or tombstone withdrawn artifacts from governed delivery while preserving the restricted audit record.
- Propagate correction and withdrawal to catalogs, caches, map layers, downloads, indexes, model context, stories, and documentation.
- Do not reveal restricted ledger details or original private values in correction notices.
- Record when a correction cannot restore privacy and what future releases were stopped or narrowed.

### Cache-key minimum

Any cache of a DP artifact must include the immutable release/artifact identity, profile version, query/workload identity, policy/review state, and correction version. A cache keyed only by URL or query text can serve stale or differently governed output.

[Back to top](#top)

---

<a id="12-failure-modes-and-anti-patterns"></a>
<a id="privacy-hazards-and-anti-patterns"></a>

## Privacy hazards and anti-patterns

| Anti-pattern | Why it fails | Required response |
|---|---|---|
| “Epsilon is 1, therefore safe” | Ignores unit, delta, variant, workload, bounds, composition, trust, and side releases | Reject the claim; require the full profile |
| Choosing event-level privacy for repeated user activity without a harm analysis | May protect one row while exposing a person's overall behavior | Start from user-level privacy where practical or justify the weaker unit |
| Unlimited or unenforced contributions | Sensitivity and guarantee do not match real data | Deny until bounds and enforcement are proven |
| Data-dependent bins published without privacy accounting | Missing categories can leak zero or presence information | Predeclare bins or use an accepted private selection method |
| Releasing invariants or companion tables without analyzing them | Non-DP side releases can dominate the privacy risk | Inventory and review the complete release surface |
| Resetting a budget after deletion, rollback, or calendar change without a privacy model | Previously observed information remains | Preserve expenditure; define time horizon before release |
| Multiple ledgers or non-atomic counters | Composition becomes ambiguous or oversubscribed | One accepted authority with atomic transactions |
| Re-running the same query until a pleasing answer appears | Consumes privacy and enables averaging/selection attacks | Account every new disclosure; prohibit output shopping |
| Public production seeds or deterministic noise derived from record IDs | Can enable reconstruction, correlation, or replay misuse | Keep production randomness protected; preserve released bytes |
| Handwritten floating-point noise | Numerical gaps and side channels can break the formal mechanism | Use admitted implementations and test numerical behavior |
| Treating DP as encryption or access control | Canonical data may still breach | Maintain security and least privilege independently |
| Treating DP as consent, rights, or de-identification | Mathematical privacy does not settle lawful or ethical use | Require independent rights, consent, sovereignty, and review |
| Applying DP to raw geometry | Produces misleading coordinates and does not define a truthful map representation | Use approved geometry controls; deny the DP claim |
| Hiding negative, fractional, clipped, biased, or inconsistent values | Users may treat protected estimates as exact | Publish utility/limitation metadata and honest UI |
| Using aggregate accuracy only | Burden may fall on small groups or places | Test subgroups, geographies, time, and downstream decisions |
| Claiming DP because a library was used | A library cannot choose the harm model or governance | Verify the complete construction and deployment |
| Allowing analysts to infer schema, bins, or timing through errors | Interactive systems leak outside the declared mechanism | Normalize errors, rate-limit, review side channels, and fail closed |
| Collecting unnecessary sensitive data because DP is planned | DP does not eliminate collection exposure | Minimize collection and retention first |

[Back to top](#top)

---

<a id="no-loss-modernization-ledger"></a>

## No-loss modernization ledger

### Retained and strengthened

- aggregate-release scope and the prohibition on using DP as raw-point redaction;
- explicit epsilon/delta and mechanism reporting;
- cumulative composition and exhaustion as first-class concerns;
- separation of process receipts, budget accounting, evidence, policy, release, correction, and rollback;
- the KFM lifecycle and cite-or-abstain posture;
- fail-closed validation and synthetic negative fixtures;
- NIST SP 800-226 as the primary external evaluation reference; and
- worked, transparent pilots before expansion.

### Corrected or narrowed

| Prior posture | Current disposition |
|---|---|
| Three named libraries appeared acceptable | They are external candidates only; dependency admission and implementation review are required |
| Sensitivity rank alone triggered DP | Removed. Sensitivity informs review, but a named use case and full profile decide whether DP is appropriate |
| A proposed ledger path was presented as the likely home | Removed. Placement and writer authority remain on hold |
| Placeholder epsilon table organized future defaults | Replaced with a no-default selection process and graduation gate |
| Receipt fields were described as confirmed wire requirements | Recast as candidate semantics until accepted contracts and schemas exist |
| A Laplace count sketch assumed sensitivity 1 | Removed. Sensitivity depends on the privacy unit, adjacency, vector workload, and enforced contribution bounds |
| Rollback or withdrawal could be read as budget recovery | Explicitly prohibited; privacy loss remains committed after disclosure |
| EDPB pseudonymisation guidance was presented as a co-framework | Removed from the DP profile. Pseudonymisation remains a separate concern |
| DP could be optional “defence in depth” without a defined purpose | Narrowed. Every use must state its privacy goal and utility cost |
| Standards language could read as current runtime enforcement | Bounded to guidance; operational use is `HOLD` |

### Compatibility anchors

The previous major section fragments are preserved by explicit HTML anchors:

`#1-scope`, `#2-doctrine--when-dp-applies-and-when-it-does-not`, `#3-library-choices`, `#4-decision-flow`, `#5-required-receipt-fields`, `#6-epsilon-budget-table-proposed`, `#7-composition-and-cross-dataset-budgets`, `#8-lifecycle-placement`, `#9-sensitivity-rubric-integration`, `#10-framework-alignment`, `#11-validation`, `#12-failure-modes-and-anti-patterns`, `#13-open-questions`, `#14-related-docs-and-adrs`, `#appendix-a--worked-example-sketch-illustrative`, and `#appendix-b--receipt-fragment-schema-sketch-illustrative`.

No inbound fragment reference was found in the bounded repository search, but preserving the anchors makes the same-path rewrite reversible and link-safe.

[Back to top](#top)

---

<a id="9-sensitivity-rubric-integration"></a>
<a id="sensitivity-and-adjacent-controls"></a>

## Sensitivity and adjacent controls

Sensitivity rank or release tier may trigger additional review, but neither determines a DP mechanism or numeric budget by itself.

| Adjacent control | Relationship to a future DP profile |
|---|---|
| Sensitivity classification | Identifies harm and handling obligations; does not define adjacency, bounds, workload, or privacy loss |
| Redaction/generalization | Produces an honest public representation of geometry or attributes; DP does not replace it |
| k-thresholding or suppression | May reduce disclosure risk but has different guarantees and failure modes |
| Consent, rights, and sovereignty | Decide whether processing and release are permitted; DP cannot waive them |
| Access control and encryption | Protect canonical data and operations; DP protects a defined release |
| Evidence and provenance | Support factual and methodological claims; a valid DP computation can still be unsupported or stale |
| Review and release state | Authorize one artifact for one audience; a budget transaction is not approval |
| Correction and rollback | Stop or supersede delivery; they do not refund privacy loss |

A rank-5, T4, or otherwise denied record remains denied even when a mathematically valid aggregate could be computed. Conversely, a low-sensitivity record does not justify DP merely as decoration: the deployment must state a privacy purpose and utility cost.

[Back to top](#top)

---

<a id="13-open-questions"></a>
<a id="open-verification-register"></a>

## Open verification register

| ID | Question | Required authority or evidence | Current state |
|---|---|---|---|
| DP-01 | What is KFM's first approved DP use case and protected harm model? | Privacy + domain + data steward decision | `UNKNOWN` |
| DP-02 | Which owner roles and independent reviewers are accountable? | CODEOWNERS/maintainer decision with named human assignment where required | `NEEDS VERIFICATION` |
| DP-03 | What semantic contract and schema names/homes are canonical? | Accepted contract/schema decision; Directory Rules compliance | `NEEDS VERIFICATION` |
| DP-04 | Where does the one budget-accounting authority live, and who may write it? | Architecture/placement decision plus transactional implementation | `UNKNOWN` |
| DP-05 | What privacy unit, adjacency, contribution bounds, workload, and time horizon apply? | Named deployment profile | `UNKNOWN` |
| DP-06 | Which variant, mechanism, library, version, and accountant are admitted? | Dependency, privacy, security, and implementation review | `UNKNOWN` |
| DP-07 | What epsilon, delta, or original privacy parameters are accepted? | Parameter study, utility/equity review, and qualified governance decision | `UNKNOWN` |
| DP-08 | How are overlap, disjointness, prior releases, and non-DP side releases inventoried? | Release-family inventory and composition model | `UNKNOWN` |
| DP-09 | What fields are safe for public transparency versus restricted receipts? | Policy/security/privacy review | `UNKNOWN` |
| DP-10 | What fixtures, validators, tests, and CI checks enforce the profile? | Repository implementation at an exact revision | `UNKNOWN` |
| DP-11 | How are ledger atomicity, backup/restore, incident response, and outage behavior proven? | Operational design and drills | `UNKNOWN` |
| DP-12 | How do correction, withdrawal, cache invalidation, and downstream AI/map/export propagation work? | End-to-end rehearsal | `UNKNOWN` |
| DP-13 | What monitoring detects accuracy drift, assumption drift, abuse, and budget anomalies? | Runtime observability and review cadence | `UNKNOWN` |
| DP-14 | What legal, rights, consent, sovereignty, and public-communication review applies? | Qualified steward/legal/privacy review | `UNKNOWN` |
| DP-15 | Does an exhaustive current-tree inventory reveal existing DP implementation not found by the bounded search? | Recursive repository scan and runtime evidence | `NEEDS VERIFICATION` |

Until these questions close for a named profile, the correct operational decision is `HOLD`.

[Back to top](#top)

---

<a id="10-framework-alignment"></a>
<a id="14-related-docs-and-adrs"></a>
<a id="source-ledger"></a>

## Source ledger

### Current repository evidence

| Source | Use | Limitation |
|---|---|---|
| [`docs/standards/README.md`](./README.md) | Standards-lane authority and negative authority | Does not prove child conformance |
| [`docs/doctrine/sensitivity.md`](../doctrine/sensitivity.md) | Current proposed DP scope and candidate `DPBudgetRecord` concept | Draft doctrine, not implementation |
| [`docs/standards/SENSITIVITY_RUBRIC.md`](./SENSITIVITY_RUBRIC.md) | Adjacent sensitivity vocabulary | Draft; does not select a DP profile |
| [`docs/standards/REDACTION_PROFILES.md`](./REDACTION_PROFILES.md) | Separate geometry/attribute redaction boundary | Draft; profile implementation unverified |
| [`docs/security/DATA_CLASSIFICATION.md`](../security/DATA_CLASSIFICATION.md) | Adjacent rights/sensitivity/tier concepts | Draft and mixed maturity |
| [`data/receipts/aggregation/README.md`](../../data/receipts/aggregation/README.md) | Receipt-lane current evidence and placement hold | README boundary, not an emitted DP receipt |
| [`contracts/data/typed_receipt_aggregation.md`](../../contracts/data/typed_receipt_aggregation.md) | Current proposed-inactive aggregation declaration contract | Not a DP budget or release object |
| [`schemas/contracts/v1/receipts/generated_receipt.schema.json`](../../schemas/contracts/v1/receipts/generated_receipt.schema.json) | Provenance schema for this AI-authored documentation change | Not a DP receipt schema |
| [`ADR-0029`](../adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Adopted Directory Rules v2 placement authority | Does not decide DP architecture |

### Authoritative external references

| Reference | Current fact used | KFM boundary |
|---|---|---|
| [NIST SP 800-226, *Guidelines for Evaluating Differential Privacy Guarantees*](https://doi.org/10.6028/NIST.SP.800-226) | Final March 2025 guidance; privacy unit, parameters, comparison, algorithms, utility/bias, deployment, implementation, security, and privacy hazards | Primary evaluation reference; not KFM adoption or legal advice |
| [OpenDP stable Context documentation](https://docs.opendp.org/en/stable/api/user-guide/context/) | A budget-aware context can require privacy loss up front and prevent queries beyond the available budget | Illustrative implementation capability; no KFM dependency admission |
| [OpenDP stable combinator documentation](https://docs.opendp.org/en/stable/api/python/opendp.combinators.html) | Composition, adaptive composition, and privacy-filter/odometer support exist in the referenced library | Capability reference only; exact version/features must be pinned |
| [Differential Privacy Deployments Registry transparency tiers](https://registry.opendp.org/transparency-tiers/) | Higher transparency records include the privacy unit, privacy parameters, trust model, domain/unprotected quantities, composition, implementation, and security | Transparency model reference; not KFM policy |
| [Differential Privacy Deployments Registry](https://registry.opendp.org/) | Deployment decisions are context-specific and benefit from public technical and sociotechnical documentation | Background; not a source of default parameter values |

External pages were inspected on 2026-08-18. Version-sensitive claims must be rechecked before dependency pinning or operational adoption.

[Back to top](#top)

---

<a id="appendix-a--worked-example-sketch-illustrative"></a>

## Appendix A — Candidate release decision packet

The packet below is an **illustrative checklist**, not an approved profile or numeric example.

```yaml
deployment_profile:
  id: "<candidate-profile-id>"
  version: "<candidate-version>"
  purpose: "<bounded public use>"
  privacy_unit: "<defined protected entity>"
  adjacency: "<bounded-or-unbounded relation>"
  trust_model: "<central-or-other>"
  query_model: "<prespecified-release-or-interactive>"
  workload_ref: "<canonical workload>"
  contribution_bounds_ref: "<enforced bounds>"
  public_information_ref: "<bins, invariants, schemas, side releases>"
  dp_variant: "<variant>"
  mechanism_profile_ref: "<library, version, constructor>"
  accountant_profile_ref: "<accountant and original privacy measure>"
  budget_account_ref: "<accepted account authority>"
  privacy_loss:
    original_measure: "<measure>"
    original_parameters: "<policy-approved values>"
    reported_epsilon: "<if applicable>"
    reported_delta: "<if applicable>"
  utility_report_ref: "<accuracy, bias, subgroup, geography, time>"
  evidence_refs:
    - "<evidence-ref>"
  policy_decision_ref: "<policy-decision>"
  review_record_refs:
    - "<privacy-review>"
    - "<domain-review>"
    - "<security-review>"
  release_manifest_ref: "<release-manifest>"
  correction_ref: "<correction-or-withdrawal-plan>"
  rollback_ref: "<rollback-target>"
```

A valid packet must reference accepted objects and exact released bytes. Filling every placeholder in a document does not make the profile operational.

[Back to top](#top)

---

<a id="appendix-b--receipt-fragment-schema-sketch-illustrative"></a>

## Appendix B — Candidate DP receipt fragment

This fragment illustrates **information categories**, not field authority, casing, nesting, or a wire schema.

```json
{
  "object_type": "PROPOSED_DP_PROCESS_RECEIPT_EXTENSION",
  "deployment_profile_ref": "<accepted-profile-and-version>",
  "workload_ref": "<canonical-query-or-model>",
  "privacy_definition": {
    "unit_ref": "<privacy-unit>",
    "adjacency_ref": "<neighboring-relation>",
    "contribution_bounds_ref": "<enforced-bounds>",
    "public_information_ref": "<bins-invariants-side-releases>"
  },
  "implementation": {
    "library": "<admitted-library>",
    "version": "<locked-version>",
    "mechanism_profile_ref": "<exact-constructor-profile>",
    "accountant_profile_ref": "<exact-accountant-profile>"
  },
  "privacy_loss": {
    "original_measure": "<measure>",
    "original_parameters": "<parameters>",
    "reported_epsilon": "<if-applicable>",
    "reported_delta": "<if-applicable>",
    "budget_transaction_ref": "<atomic-reservation-and-commit>"
  },
  "output": {
    "artifact_ref": "<immutable-artifact>",
    "artifact_digest": "sha256:<digest>",
    "utility_report_ref": "<report>"
  },
  "governance": {
    "evidence_refs": ["<evidence-ref>"],
    "policy_decision_ref": "<policy-decision>",
    "review_record_refs": ["<review-record>"],
    "release_manifest_ref": "<release-manifest>",
    "correction_ref": "<correction-plan>",
    "rollback_ref": "<rollback-target>"
  },
  "randomness": {
    "production_seed_disclosed": false,
    "released_bytes_reused_for_replay": true
  }
}
```

[Back to top](#top)

---

<a id="maintenance-correction-and-rollback"></a>

## Maintenance, correction, and rollback

### Document maintenance

Recheck this standard when any of the following changes:

- NIST issues an update or erratum to SP 800-226;
- KFM accepts a DP contract, schema, policy, ledger, dependency, or deployment profile;
- a pilot, incident, privacy audit, or utility review changes the risk model;
- the aggregation-receipt placement hold is resolved;
- release, correction, or rollback semantics change; or
- an implementation emits a real DP-bearing artifact.

### Rollback

This is a same-path documentation modernization plus its generated provenance receipt. Before merge, close or abandon the draft pull request. After an authorized merge, revert the documentation commit through normal review and restore the prior blob recorded in the metadata.

No source, sensitive record, privacy budget, ledger transaction, mechanism, policy decision, release, cache entry, deployment, or public artifact is created by this change. Rolling it back therefore requires no privacy-budget refund, data migration, source deactivation, cache purge, withdrawal notice, or public correction.

[Back to top](#top)
