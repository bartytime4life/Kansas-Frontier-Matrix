<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/promotion-criteria
title: Intake Promotion Criteria
type: governance-guide; intake-criteria-reference
version: v1.0-draft
status: draft; repository-grounded; intake-only; human-review-guidance; non-authoritative; no-release-effect
owners:
  - "@bartytime4life — verified CODEOWNERS review route only"
owner_status: "No accepted StewardshipAssignment, independent reviewer capacity, approval, canonicalization authority, source-admission authority, release authority, or separation of duties is implied."
created: 2026-05-16
updated: 2026-08-23
policy_label: repository-facing; intake; review-guidance; cite-or-abstain
owning_root: docs/
current_path: docs/intake/promotion-criteria.md
responsibility: >-
  Explain the human review criteria for deciding whether a non-authoritative
  documentation-intake recommendation is developed enough to enter candidate
  review, receive an intake disposition, or hand off to one verified owning
  responsibility root without defining object meaning, machine shape, policy,
  source admission, lifecycle state, release state, or publication authority.
truth_posture: >-
  CONFIRMED current path, creation history, surrounding intake and promotion
  lane contracts, accepted Directory Rules placement, CODEOWNERS routing, and
  bounded repository promotion surfaces / PROPOSED intake criteria and reviewer
  burden where no accepted machine policy exists / UNKNOWN independent human
  assignments and operational enforcement / NEEDS VERIFICATION canonical lane
  classification, sibling vocabulary convergence, and exact-head hosted checks;
  cite-or-abstain.
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: f732cbd1003898dc765a7afe4b635d710e295d17
  target_prior_blob: a542f5ea32c5a5e6ea666cdf216baa769f56066b
  target_creation_commit: 18ab67d61b9d4d0d226ea80a78e5c6ca65253cfa
  intake_readme_blob: 35cc8f301be00526d3334f0778d65d52965a8687
  canonicalization_policy_blob: 49f141f674a9095c4d4df37f2ce2ae42e23b9888
  promotions_readme_blob: c6379a1dd445591cf0ab138ab811cf640e7afdeb
  candidates_readme_blob: fe8374e5927a97087eeb916eea414ed798ba51fe
  accepted_readme_blob: ab721761ac304f83a8f0fbe26a5a748b0c53b594
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  adr_0018_blob: 51cedfdf98b92f1a9af492ce3a1cde231eed9308
  publication_promotion_gates_blob: a3126726a625b5a15712b1c3cc7dc2a317192dd9
  docs_meta_block_workflow_blob: c2054a053ba3050cf41b731d85a7a0996e9231f6
inspection_boundary: >-
  Current-session GitHub reads covered the exact target and creation commit,
  parent intake lane, canonicalization guidance, promotion packet parent and
  state-lane READMEs, accepted Directory Rules decision and bytes, CODEOWNERS,
  proposed ADR-0018, the bounded publication-promotion overview, and the
  Markdown metadata workflow. No actor was authenticated as an independent
  reviewer, no StewardshipAssignment was accepted, no intake packet was
  dispositioned, no source was admitted, no production policy bundle was
  evaluated, no lifecycle transition was applied, and no release, deployment,
  publication, correction, withdrawal, or operational rollback was exercised.
related:
  - ./README.md
  - ./triage-rules.md
  - ./canonicalization-policy.md
  - ./promotions/README.md
  - ./promotions/candidates/README.md
  - ./promotions/accepted/README.md
  - ./promotions/deferred/README.md
  - ./promotions/rejected/README.md
  - ../doctrine/directory-rules.md
  - ../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../adr/ADR-0018-promotion-gate-sequence.md
  - ../architecture/publication/promotion-gates.md
  - ../governance/REVIEW_DUTIES.md
  - ../registers/DRIFT_REGISTER.md
  - ../registers/VERIFICATION_BACKLOG.md
  - ../../.github/CODEOWNERS
  - ../../.github/workflows/docs-meta-block.yml
  - ../../.github/workflows/promotion-gate.yml
  - ../../contracts/release/promotion_decision.md
  - ../../contracts/release/promotion_receipt.md
  - ../../tools/validators/promotion_gate/README.md
tags: [kfm, docs, intake, promotion-criteria, candidate-review, canonicalization, evidence, rights, sensitivity, validation, rollback]
notes:
  - "v1.0-draft replaces a twelve-line placeholder with repository-grounded human review guidance at the same path."
  - "This document is not a JSON Schema, Rego policy, PromotionDecision, PromotionReceipt, ReviewRecord, release gate, or publication control."
  - "The phrase intake promotion is qualified throughout so it cannot be confused with lifecycle or release promotion."
  - "No sibling file, contract, schema, policy, fixture, validator, workflow, registry, release object, or public carrier is changed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>
<a id="promotion-criteria"></a>
<a id="intake-promotion-criteria"></a>

# Intake Promotion Criteria

> **Human review criteria for advancing a non-authoritative intake recommendation toward one verified owning path—without confusing packet review with canon, implementation, lifecycle promotion, release, or publication.**

[![Document: draft](https://img.shields.io/badge/document-draft-d4a72c?style=flat-square)](#2-authority-and-state-separation)
[![Path: confirmed](https://img.shields.io/badge/path-confirmed-1a7f37?style=flat-square)](#1-purpose-and-scope)
[![Authority: intake only](https://img.shields.io/badge/authority-intake--only-8250df?style=flat-square)](#2-authority-and-state-separation)
[![Criteria: human guidance](https://img.shields.io/badge/criteria-human%20guidance-0969da?style=flat-square)](#3-criteria-model)
[![Machine policy: not established](https://img.shields.io/badge/machine%20policy-not%20established-bc6f00?style=flat-square)](#11-machine-enforcement-boundary)
[![Release effect: none](https://img.shields.io/badge/release%20effect-none-6e7781?style=flat-square)](#16-non-effects)

> [!IMPORTANT]
> **Intake promotion is a documentation-review transition only.** A criteria pass, candidate packet, accepted intake recommendation, branch, pull request, merge, test, badge, generated report, or polished narrative does not by itself create doctrine, accept an ADR, define a contract or schema, admit a source, approve policy, authenticate evidence or reviewers, apply a lifecycle transition, release an artifact, or publish a claim.

> [!CAUTION]
> **No score compensates for a failed trust gate.** Unknown rights, unsafe precision, unresolved authority, parallel writable homes, missing evidence closure, missing correction or rollback for public state, hidden model authority, or an unaccepted required decision remains a hold, deferral, split, abstention, or rejection condition regardless of perceived feature value.

> [!NOTE]
> This page summarizes and operationalizes the current **human intake-review** threshold. The packet lane contract remains in [`promotions/README.md`](promotions/README.md); state-specific authoring guidance remains in the [`candidates/`](promotions/candidates/README.md), [`accepted/`](promotions/accepted/README.md), [`deferred/`](promotions/deferred/README.md), and [`rejected/`](promotions/rejected/README.md) READMEs. The separately bounded lifecycle-promotion surfaces remain under release, policy, validation, and publication responsibilities.

## Current profile

| Field | Current bounded value |
|---|---|
| Repository path | `docs/intake/promotion-criteria.md` — **CONFIRMED**, same-path update |
| Creation evidence | First added by commit `18ab67d61b9d4d0d226ea80a78e5c6ca65253cfa` at `2026-05-16T02:44:33Z` |
| Prior target blob | `a542f5ea32c5a5e6ea666cdf216baa769f56066b` |
| Owning root | `docs/` — human-readable explanation and governance guidance |
| Placement posture | `PLACE` for this same-path update; exact `docs/intake/` direct-child classification remains **NEEDS VERIFICATION** |
| Primary responsibility | Human criteria for documentation-intake candidate readiness, disposition, and owning-path handoff |
| Review route | `@bartytime4life` through default CODEOWNERS routing; no independent review or stewardship proof |
| Machine enforcement | **Not established by this document**; current executable promotion tooling has a different, bounded release-readiness scope |
| Source admission / lifecycle / release authority | None |
| Release, deployment, publication effect | None |
| Evidence review | 2026-08-23 against `main@f732cbd1003898dc765a7afe4b635d710e295d17` |

---

## Contents

1. [Purpose and scope](#1-purpose-and-scope)
2. [Authority and state separation](#2-authority-and-state-separation)
3. [Criteria model](#3-criteria-model)
4. [Universal promotion-review gates](#4-universal-promotion-review-gates)
5. [Non-compensable gates](#5-non-compensable-gates)
6. [Conditional criteria by change class](#6-conditional-criteria-by-change-class)
7. [Evidence sufficiency](#7-evidence-sufficiency)
8. [Disposition matrix](#8-disposition-matrix)
9. [Review burden and separation](#9-review-burden-and-separation)
10. [Authoring checklist and decision record](#10-authoring-checklist-and-decision-record)
11. [Machine-enforcement boundary](#11-machine-enforcement-boundary)
12. [Validation for criteria and packets](#12-validation-for-criteria-and-packets)
13. [Anti-patterns](#13-anti-patterns)
14. [Open verification and sibling drift](#14-open-verification-and-sibling-drift)
15. [Rollback and correction](#15-rollback-and-correction)
16. [Non-effects](#16-non-effects)
17. [No-loss modernization ledger](#17-no-loss-modernization-ledger)

---

## 1. Purpose and scope

This document answers one bounded question:

> **When is a documentation-intake recommendation sufficiently identified, evidenced, placed, scoped, safe, reviewable, testable, and reversible to advance to the next human intake-review state or to an implementation handoff in its verified owning root?**

It applies to:

- idea packets, source maps, exploratory notes, carry-forward records, and candidate promotion packets;
- proposed doctrine, architecture, ADR, runbook, standard, or documentation-control changes;
- proposed contracts, schemas, policy, fixtures, validators, workflows, packages, applications, pipelines, source-registry work, migrations, or corrections while they are still being evaluated at the intake-documentation layer;
- recommendations supported by a branch or draft pull request used to gather implementation evidence;
- recommendations that may be accepted as already satisfied by current repository evidence.

It does **not**:

- define the meaning of `PromotionDecision`, `PromotionReceipt`, `ReviewRecord`, `ReleaseManifest`, or another trust object;
- define machine-checkable shape, policy, or evaluator behavior;
- admit, activate, retrieve, transform, or publish a source;
- move data through `RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED`;
- approve repository merge, release, deployment, public serving, correction, withdrawal, or rollback;
- establish a reviewer identity, quorum, independent capacity, or separation-of-duties proof;
- make `docs/intake/` a canonical authority merely because the path exists.

### 1.1 Relationship to adjacent documents

| Surface | Primary responsibility | This document's boundary |
|---|---|---|
| [`README.md`](README.md) | Overall documentation-intake lane map | This page does not redefine the lane |
| [`triage-rules.md`](triage-rules.md) | Initial intake classification | Still a placeholder at this snapshot; this page does not silently complete it |
| [`canonicalization-policy.md`](canonicalization-policy.md) | Draft path from intake to one canonical destination | This page extracts a criteria-focused operating view without adopting the policy |
| [`promotions/README.md`](promotions/README.md) | Promotion-packet bridge, states, packet shape, workflow | This page defines the shared threshold used during review |
| [`promotions/candidates/README.md`](promotions/candidates/README.md) | Candidate admission and active review | This page provides the common gate vocabulary |
| [`promotions/accepted/README.md`](promotions/accepted/README.md) | Accepted intake recommendation records | Acceptance remains an intake disposition only |
| [`ADR-0018`](../adr/ADR-0018-promotion-gate-sequence.md) | Proposed final lifecycle-promotion-readiness sequence | Separate scope; not accepted and not adopted here |
| [`publication/promotion-gates.md`](../architecture/publication/promotion-gates.md) | Bounded final readiness A–G explanation | Separate from documentation-intake review |

### 1.2 Directory Rules basis

The target is an existing tracked human-facing guidance file under `docs/`. Accepted ADR-0029 adopts the current Directory Rules bytes and makes `docs/` the human-readable governance and explanation root. The parent intake README records that `docs/intake/` exists but is not enumerated in the adopted direct-child map, so its exact canonical or compatibility classification remains **NEEDS VERIFICATION**.

The smallest sound placement result is therefore:

| Question | Result |
|---|---|
| Does the target exist at this path? | **CONFIRMED** |
| Does its responsibility remain human explanation? | **CONFIRMED** |
| Is this a same-path modernization? | **CONFIRMED / PLACE** |
| Does this change create a new root or parallel authority? | **No** |
| Does it settle the classification of `docs/intake/`? | **No / NEEDS VERIFICATION** |
| Does it authorize moving, renaming, mirroring, or deleting siblings? | **No** |

[Back to top](#top)

---

## 2. Authority and state separation

### 2.1 Authority ladder for an intake review

Use the source appropriate to the claim:

1. trust, evidence, public-boundary, sensitivity, correction, and rollback invariants;
2. accepted, unsuperseded ADRs;
3. adopted Directory Rules and governing machine projections;
4. current contracts, schemas, policy, registries, implementation, tests, workflows, receipts, proofs, and release records for current behavior;
5. current repository evidence pinned to an immutable ref;
6. supplied source documents and external primary sources for the claims they can actually support;
7. explicit inference or proposal, labeled as such.

A fluent packet does not outrank any higher authority.

### 2.2 State axes that must remain distinct

| State axis | Typical values | What an intake criteria result proves |
|---|---|---|
| Intake capture | captured, triaged, exploratory-retained, lineage-only | Only documentation classification |
| Intake packet review | candidate-for-promotion, accepted, deferred, rejected | Only the packet's human review disposition |
| Canonicalization or adoption | draft document, proposed ADR, accepted ADR, adopted doctrine, verified owning artifact | Nothing unless the actual authority-bearing destination and decision are cited |
| Repository delivery | not started, branch, draft PR, ready PR, merged commit | Only how bytes were delivered |
| Implementation maturity | absent, scaffold, fixture-only, partial, verified behavior | Nothing without code/config/test/runtime evidence |
| Source admission | unresolved, context-only, admitted, quarantined, denied | Nothing unless the source authority records it |
| Policy and review | allow, restrict, redact, generalize, abstain, deny; review pending/complete | Nothing unless policy and review records exist |
| Lifecycle | RAW, WORK/QUARANTINE, PROCESSED, CATALOG/TRIPLET, PUBLISHED | Nothing; intake is not a lifecycle stage |
| Release and public serving | candidate, held, released, corrected, withdrawn, rolled back | Nothing; intake acceptance is not release |

### 2.3 Qualified terminology

| Prefer | Avoid when unsupported |
|---|---|
| `intake candidate` | `promotion candidate` without scope |
| `intake recommendation accepted` | `promoted`, `approved`, or `canonical` |
| `implementation handoff authorized for review` | `implementation approved` |
| `draft PR delivered` | `released` or `published` |
| `APPROVE_READY` in the bounded A–G profile | `APPROVE` |
| `NEEDS VERIFICATION` | optimistic assumptions or implied closure |

[Back to top](#top)

---

## 3. Criteria model

The criteria are evaluated at three human-review thresholds. Passing an earlier threshold does not imply the later one.

### 3.1 Threshold A — eligible for candidate review

An item may enter or remain in [`promotions/candidates/`](promotions/candidates/README.md) when:

- it has one stable identity and one bounded subject;
- one observable proposed outcome is stated;
- source or repository support is linked, or the evidence gap is explicit;
- current artifacts, issues, branches, pull requests, packets, and authority surfaces were checked for overlap;
- one primary responsibility root and a placement basis are identified;
- direct dependencies, non-goals, risks, validation, review route, and rollback are inspectable;
- remaining `UNKNOWN` or `NEEDS VERIFICATION` items are bounded enough for structured review.

Candidate status means **reviewable and undecided**, not canonical or approved.

### 3.2 Threshold B — eligible for intake acceptance or another final disposition

A candidate may receive an `accepted`, `deferred`, `rejected`, `split`, `reconcile`, or `already satisfied` disposition when:

- the recommendation's evidence and truth posture survive review;
- the owning root and destination do not create parallel authority;
- accepted scope and excluded or routed scope are explicit;
- direct dependencies are closed for the accepted outcome or named as a deferral blocker;
- rights, sensitivity, privacy, sovereignty, security, compatibility, and public-path effects are bounded;
- review burden is identified without inventing people or teams;
- validation and rollback are credible for the accepted scope;
- implementation, adoption, release, and publication states remain separate.

Acceptance means the recommendation **may proceed through its owning authority process**. It does not mean that process has completed.

### 3.3 Threshold C — eligible for repository implementation handoff

A recommendation may hand off to feature-branch work when:

- current user authority or another legitimate implementation trigger exists;
- repository, default branch, immutable base, target bytes, and concurrent work are rechecked;
- path-scoped instructions, Directory Rules, accepted ADRs, root contracts, workflows, and direct dependencies are inspected;
- the smallest complete implementation boundary and rollback boundary are the same;
- required checks can be run or explicitly left pending on a draft PR;
- no direct default-branch write, merge, release, deployment, promotion, publication, or administrative bypass is implied.

A draft implementation may be used to gather evidence while the intake recommendation remains under review. Delivery does not decide the packet.

### 3.4 Threshold D — lifecycle or public release

This document does not define Threshold D. A release-significant candidate must satisfy the separately governed evidence, policy, review, decision, transition, release, correction, rollback, and public-serving controls. Intake review cannot waive them.

[Back to top](#top)

---

## 4. Universal promotion-review gates

Every active candidate must pass—or explicitly route around through `defer`, `split`, `reconcile`, `abstain`, or `reject`—the following human review gates.

| # | Gate | Required question | Minimum support | Failure or routing outcome |
|---|---|---|---|---|
| 1 | Identity and origin | Is the candidate stably named and traceable to its intake/source lineage? | Stable ID or slug; originating record or source refs | Return to intake or `ABSTAIN` |
| 2 | Source traceability | Can each material recommendation be traced to source material, current repo evidence, or a labeled inference? | Direct refs plus evidence boundary | Correct, defer, or reject |
| 3 | Distinctness and concurrency | Is this distinct from current authority, implementation, issue, branch, PR, or packet? | Search at an immutable repository ref | Reconcile, supersede, split, or reject duplicate work |
| 4 | Scope closure | Is there one observable outcome, one primary owner root, one validation story, and one rollback boundary? | Accepted scope and non-goals | Narrow or `SPLIT` |
| 5 | Placement | Does the target follow adopted Directory Rules and accepted ADRs? | Same-path basis or explicit placement decision | `HOLD`, `MIGRATE`, `MIRROR`, or `DENY` as applicable |
| 6 | Authority collision | Would the result create another writable doctrine, contract, schema, policy, source, registry, receipt, proof, catalog, release, or publication home? | Authority-owner comparison | `DENY` until accepted migration or decision resolves it |
| 7 | Truth posture | Are doctrine, current behavior, lineage, proposal, unknowns, and verification needs separate? | Explicit labels where material | Return for correction |
| 8 | Direct dependency closure | Are required docs, contracts, schemas, policy, fixtures, tests, validators, config, workflows, generated outputs, migrations, and runtime surfaces included or ruled out? | Dependency matrix | Hold, narrow, or split |
| 9 | Rights and sensitivity | Are rights, privacy, sovereignty, cultural, ecological, archaeological, infrastructure, living-person, genomic, land/title, source-term, and harmful-precision risks handled? | Public-safe summary, policy need, review class, or not-applicable reason | Quarantine, redact, generalize, stage, defer, abstain, or reject |
| 10 | Compatibility and consumers | Are current consumers, aliases, generated mirrors, migrations, deprecations, and version effects understood? | Consumer search and compatibility posture | Hold or require migration plan |
| 11 | Validation | Can success and fail-closed behavior be observed with the smallest strong repository-native checks? | Positive, negative, safety, and delivery checks | `NEEDS VERIFICATION`; not ready for final review |
| 12 | Stewardship and review | Is the verified GitHub route known, and are specialist or independent reviewer classes named when significance requires them? | CODEOWNERS route plus reviewer classes | Keep review pending; do not invent identities |
| 13 | Correction and rollback | Can the recommendation and any implementation be abandoned, corrected, superseded, reverted, or forward-fixed without hiding history? | Before-merge and after-merge paths | Hold until credible |
| 14 | Freshness and staleness | Are version-sensitive or state-sensitive claims current at the review snapshot? | Checked date, immutable ref, refresh trigger | Refresh or mark stale / NEEDS VERIFICATION |

### 4.1 Required evidence packet

A criteria review should be able to answer:

- **What is proposed?** One bounded recommendation.
- **Why now?** The source or repository condition that makes review timely.
- **What was inspected?** Exact source identities and repository refs.
- **What remains unknown?** Concrete gaps, not generic caveats.
- **Where does it belong?** One verified or proposed owning path.
- **What must change with it?** Direct dependencies and non-goals.
- **What can go wrong?** Authority, evidence, rights, sensitivity, security, compatibility, and public-path risks.
- **How is it tested?** Positive, negative, changed-area, delivery, and hosted checks.
- **Who reviews?** Verified routing identity and reviewer classes.
- **How does it end?** Acceptance, deferral, rejection, split, correction, and rollback paths.

[Back to top](#top)

---

## 5. Non-compensable gates

The following failures cannot be offset by impact, urgency, popularity, completeness of prose, number of source documents, passing unrelated checks, or interface polish.

| Non-compensable failure | Default intake posture |
|---|---|
| No identifiable owning responsibility root | `HOLD` or return to triage |
| Required accepted ADR or governance decision has not occurred | `DEFER` / `HOLD` |
| Proposal creates a parallel writable authority | `REJECT` or `HOLD` pending migration decision |
| Overlapping active issue, branch, PR, migration, or packet owns the same surface | `RECONCILE`, `SPLIT`, or `DEFER` |
| Source rights, consent, sovereignty, cultural authority, or terms are unresolved | `DEFER`, quarantine, abstain, or reject public use |
| Protected or harmful precision is exposed without an approved transform | Redact, generalize, stage, or reject |
| Consequential public claim lacks resolvable evidence | `ABSTAIN` or reject public-facing scope |
| Public client would read RAW, WORK, QUARANTINE, canonical/internal stores, or direct model output | `DENY` the design |
| AI, map, tile, graph, index, dashboard, scene, screenshot, or generated prose becomes truth authority | `DENY` or redesign |
| Public or operational state lacks correction, withdrawal, or rollback path | `HOLD` |
| High-consequence behavior lacks a negative or fail-closed test plan | `HOLD` / `NEEDS VERIFICATION` |
| Review identity or independence is claimed without evidence | Remove claim; keep review pending |
| Evidence snapshot is stale enough to change the decision | Refresh before disposition |

A scorecard may help order a queue, but it must not convert a failed trust gate into acceptance. Numeric ranking is **PROPOSED tooling at most** unless an accepted contract, policy, fixtures, validator, and review process define it.

[Back to top](#top)

---

## 6. Conditional criteria by change class

Universal gates always apply. The additional burden below activates only when the candidate has the stated consequence.

### 6.1 Documentation-only or editorial candidate

Required additions:

- current target bytes and legitimate creation/update dates;
- stable H1, anchors, inbound links, and metadata preserved where relied upon;
- source-derived content distinguished from repository evidence and inference;
- no behavioral, authority, release, or publication claim introduced accidentally;
- Markdown structure, links, metadata, document graph, and stale references checked as triggered;
- exact documentation rollback target;
- no-loss ledger for a large rewrite.

### 6.2 Contract, schema, policy, validator, or machine-behavior candidate

Required additions:

- semantic owner and machine-shape owner distinguished;
- contract and schema consequences identified;
- positive, negative, boundary, and compatibility fixtures identified;
- validator and policy consequences identified;
- finite outcomes and reason codes defined in their owning surfaces, not in intake prose;
- migration, versioning, consumer, and generated-output impacts identified;
- executable checks tied to the exact implementation head;
- documentation updated with behavior rather than used as a substitute for it.

### 6.3 Structural, placement, rename, split, merge, mirror, or retirement candidate

Required additions:

- accepted Directory Rules and applicable ADRs inspected;
- current writers, readers, links, fragments, generated mirrors, aliases, and external consumers inventoried;
- one writable authority preserved;
- migration order, tombstone or compatibility behavior, and deletion hold stated;
- link and consumer closure demonstrated before physical retirement;
- reversible branch/PR boundary and post-merge rollback defined.

### 6.4 Source, connector, registry, or source-refresh candidate

Required additions:

- source identity, role, authority class, rights, terms, access method, cadence, geographic/temporal scope, and sensitivity posture;
- source-role anti-collapse check;
- activation and admission kept separate from file presence or connector code;
- retrieval, digest, snapshot, freshness, error, and quarantine handling;
- no live retrieval or public exposure unless explicitly within scope and separately authorized;
- source-specific policy, fixtures, validators, and citation behavior where applicable.

### 6.5 Public, API, UI, MapLibre, export, or AI-facing candidate

Required additions:

- public client uses governed APIs or released public-safe carriers;
- `EvidenceRef` resolves to `EvidenceBundle` before consequential claims are authoritative;
- policy, review, release, stale, correction, and denial states remain visible;
- denied or protected fields cannot be reconstructed client-side;
- map, tile, scene, search, summary, and model output remain downstream carriers;
- accessibility, mobile, low-connectivity, degraded-state, and error behavior are part of correctness;
- correction, cache/index invalidation, withdrawal, and rollback effects are defined;
- no direct browser-to-model or browser-to-internal-store path.

### 6.6 Sensitive or rights-bearing candidate

Required additions:

- public-safe rationale that does not disclose the protected fact it is meant to contain;
- specialist reviewer class and restricted review route where needed;
- generalization, redaction, withholding, delayed release, staged access, or denial transform;
- transform receipt or equivalent accountability need identified;
- living-person, DNA/genomic, archaeology, rare-species, cultural/sacred, infrastructure, private-land, and title implications explicitly screened;
- inability to verify rights or authority fails closed.

### 6.7 Version-sensitive dependency or standard candidate

Required additions:

- authoritative primary source checked date;
- version, endpoint, package, service, or standard identity;
- compatibility range or explicit reason for a hard pin;
- license, supply-chain, provenance, security, and rollback posture;
- refresh and invalidation trigger;
- repository lockfile or implementation evidence before claiming admission.

### 6.8 Correction, deprecation, supersession, or rollback candidate

Required additions:

- predecessor identity and current consumers;
- reason, scope, effective time, and affected public or internal carriers;
- forward link and preserved lineage;
- compatibility or migration window;
- cache, index, tile, API, UI, AI, and export correction propagation where applicable;
- rollback target and forward-fix option;
- no silent history rewrite or deletion of decision evidence.

[Back to top](#top)

---

## 7. Evidence sufficiency

### 7.1 Evidence by claim type

| Claim | Minimum admissible support | What the evidence does not prove |
|---|---|---|
| File or path exists | Repository read at an immutable ref | Canonical authority, correctness, review, or release |
| Bytes changed | Commit, blob, or diff | Runtime behavior, security, or public effect |
| Unit or fixture profile passes | Exact command/run and result | Production authority or deployment |
| Hosted check passes | Exact workflow and exact head | Conditions outside that workflow's scope |
| Contract or schema exists | Current tracked artifact and status | Acceptance, producer/consumer use, or semantic correctness |
| Policy file exists | Policy artifact, activation register, evaluator wiring, tests | Production evaluation or public permission |
| Reviewer route exists | CODEOWNERS or platform route | Authenticated review, independence, approval, or quorum |
| Source document proposes an idea | Stable source identity and relevant section | Repository implementation or adoption |
| External fact is current | Authoritative primary source checked now | KFM admission or compatibility |
| Runtime/deployment works | Current logs, traces, environment, probes, or operational evidence | Broader release authority beyond the tested scope |

The following are useful support but are not sovereign proof: badges, diagrams, screenshots, generated summaries, search results, map renders, a green check without exact-head identity, repository-shaped paths in PDFs, pull request bodies, merged commits without behavior evidence, repeated statements across documents, and AI-generated explanations.

### 7.2 Cite or abstain

When support is insufficient:

1. narrow the claim;
2. label it `UNKNOWN` or `NEEDS VERIFICATION`;
3. identify the concrete closure check;
4. defer, split, abstain, or reject the unsupported scope;
5. preserve source and decision lineage.

Do not fill the gap with plausibility.

[Back to top](#top)

---

## 8. Disposition matrix

The dispositions below are human documentation-intake outcomes. They are not policy codes, lifecycle transitions, or release decisions.

| Disposition | Use when | Required retained record | Does not mean |
|---|---|---|---|
| `CANDIDATE_FOR_PROMOTION` | Structured review can proceed | Identity, evidence, placement, dependencies, risks, validation, review, rollback | Canonical or accepted |
| `ACCEPTED_FOR_HANDOFF` | The bounded recommendation may proceed to its owning path | Accepted scope, destination, constraints, next authority step | Implemented, merged, released, or published |
| `ACCEPTED_WITH_BOUNDED_SCOPE` | Only a clear subset is accepted | Accepted and routed remainder, narrowing rationale | Whole proposal accepted |
| `ACCEPTED_AS_ALREADY_SATISFIED` | Current authority or implementation already fulfills it | Pinned destination and comparison | New change required |
| `ACCEPTED_PENDING_SEPARATE_ADOPTION` | Draft implementation may proceed but another authority must decide adoption | Required decision, current state, no-adoption boundary | ADR/policy/source/release accepted |
| `DEFERRED` | A named, checkable prerequisite blocks review or handoff | Blocker, owner or evidence route, re-entry trigger | Rejected forever |
| `REJECTED` | Submitted form is duplicate, unsupported, unsafe, authority-colliding, or out of scope | Public-safe rationale, source lineage, reopen condition if any | Source falsehood or policy denial unless separately decided |
| `SPLIT` | Multiple outcomes, owners, validation stories, or rollback boundaries are bundled | Child scopes and dependency order | Any child automatically accepted |
| `RECONCILE` | Overlapping authority or active work must converge | Compared artifacts, precedence, retained parts, migration or closure plan | Winner chosen by recency |
| `EXPLORATORY_RETAINED` | Useful pressure remains but criteria are not met | Value, gaps, next trigger | Active candidate |
| `LINEAGE_ONLY` | Historical context should remain inspectable | Preservation reason and “do not use for” boundary | Current guidance |
| `ABSTAIN` | Evidence is insufficient to decide | Missing support and closure check | Hidden acceptance |

Use **deferral** when a concrete prerequisite could change the decision. Use **rejection** when the submitted form should not advance even if more time passes, unless materially new evidence or a redesigned scope is supplied.

An accepted intake recommendation can have a separately stated implementation state: not started, draft artifact, workspace patch, pushed branch, draft PR, ready PR, merged commit, fixture-only behavior, partial behavior, verified behavior, or deployment unknown. Never infer one from the other.

[Back to top](#top)

---

## 9. Review burden and separation

### 9.1 Minimum reviewer classes

| Change class | Minimum human review posture | Additional trigger |
|---|---|---|
| Routine intake metadata | Verified docs/intake route | None when no authority or behavior changes |
| Documentation correction or modernization | Docs-aware reviewer | Owning-domain reviewer when substantive meaning changes |
| Doctrine or architecture | Architecture/canon reviewer | Accepted ADR when durable authority changes |
| Contract or schema | Contract/schema owner class | Policy-aware and consumer review when behavior changes |
| Policy or release gate | Policy and architecture reviewer classes | Independent release/review class when significance requires it |
| Source or registry | Source and policy reviewer classes | Rights/sensitivity reviewer where applicable |
| Workflow, validator, package, app, or runtime | Tooling/implementation owner class | Security, domain, or operations review as triggered |
| UI, map, export, or AI surface | UI/shell and doctrine-aware reviewer classes | Accessibility, sensitivity, and public-boundary review |
| Sensitive or rights-bearing scope | Relevant specialist, policy, and architecture classes | Rights-holder or community authority where applicable |
| Structural migration or retirement | Directory governance and affected root owner classes | Consumer and rollback review |

### 9.2 Current verified route

At the evidence snapshot, `@bartytime4life` is the default CODEOWNERS route. CODEOWNERS explicitly does **not** prove a StewardshipAssignment, that review occurred, reviewer independence, approval, policy authority, release authority, or publication authority.

Where a policy-significant, sensitive, authority-changing, or release-significant decision requires distinct actors, keep the candidate pending until an accepted assignment and review route can support that separation. A single-owner bootstrap exception, when explicitly authorized elsewhere, must be recorded as an exception rather than presented as independent review.

[Back to top](#top)

---

## 10. Authoring checklist and decision record

### 10.1 Compact criteria checklist

#### Identity, evidence, and distinctness

- [ ] Stable packet or candidate identity exists.
- [ ] One observable recommendation is stated.
- [ ] Originating intake record and source refs are linked.
- [ ] Repository evidence is pinned to an immutable ref.
- [ ] Current authority, implementation, issues, branches, PRs, and packets were searched for overlap.
- [ ] Source facts, repository facts, inference, proposal, and unknowns remain distinct.

#### Placement, scope, and dependencies

- [ ] One primary owning responsibility root is identified.
- [ ] Target path is verified or explicitly `PROPOSED`.
- [ ] Directory Rules and applicable accepted ADRs support the placement.
- [ ] No parallel writable authority is created.
- [ ] Accepted scope and non-goals are explicit.
- [ ] Direct dependencies and generated/mirror effects are included or ruled out.
- [ ] Compatibility, consumer, migration, and version effects are addressed where applicable.

#### Safety, validation, and review

- [ ] Rights, sensitivity, privacy, sovereignty, security, and harmful-precision risks are screened.
- [ ] Public clients remain behind governed interfaces and released public-safe carriers.
- [ ] Consequential claims resolve evidence or abstain.
- [ ] Positive, negative, fail-closed, changed-area, delivery, and hosted checks are identified as needed.
- [ ] Verified GitHub review route and specialist reviewer classes are named without invented identities.
- [ ] Remaining blockers are routed to deferral, split, reconciliation, abstention, or rejection.

#### Correction and reversibility

- [ ] Before-merge abandonment path exists.
- [ ] After-merge revert or forward-fix path exists.
- [ ] Supersession and correction preserve lineage.
- [ ] Public caches, indexes, tiles, APIs, UI, AI, and exports are included when actual public state could be affected.
- [ ] Refresh and invalidation triggers are recorded.

### 10.2 Human decision-record template

The following is an authoring aid, not an adopted schema or policy bundle.

```yaml
criteria_review_id: kfm://intake/criteria-review/<stable-slug>
candidate_ref: <promotion packet or intake record>
review_snapshot:
  repository_ref: <immutable commit>
  target_blob: <blob or not applicable>
  reviewed_at: <ISO date>
recommendation:
  summary: <one observable outcome>
  truth_posture: <CONFIRMED / PROPOSED / UNKNOWN / NEEDS VERIFICATION split>
placement:
  owning_root: <verified root or HOLD>
  target_path: <verified or PROPOSED path>
  outcome: <PLACE / SPLIT / MIGRATE / MIRROR / HOLD / DENY>
distinctness:
  compared_refs: []
  result: <distinct / reconcile / already-satisfied / duplicate / NEEDS VERIFICATION>
direct_dependencies:
  required: []
  ruled_out_with_reason: []
rights_sensitivity_policy:
  posture: <bounded summary>
validation:
  planned_or_observed_checks: []
review:
  github_route: []
  specialist_classes: []
  independence_status: <verified / not-required-with-reason / NEEDS VERIFICATION>
disposition:
  result: <candidate / accepted / deferred / rejected / split / reconcile / abstain>
  reason_codes: []
  accepted_scope: []
  routed_scope: []
rollback:
  before_merge: <abandon/close path>
  after_merge: <revert/forward-fix path>
residual_unknowns: []
```

Example human reason labels may include `SOURCE_SUPPORT_INCOMPLETE`, `DUPLICATE_ACTIVE_WORK`, `SCOPE_NOT_CLOSED`, `PLACEMENT_AUTHORITY_UNRESOLVED`, `PARALLEL_AUTHORITY_RISK`, `RIGHTS_OR_SENSITIVITY_UNRESOLVED`, `DIRECT_DEPENDENCY_MISSING`, `VALIDATION_NOT_OBSERVABLE`, `REVIEW_ROUTE_UNVERIFIED`, `ROLLBACK_NOT_CREDIBLE`, and `ALREADY_SATISFIED_AT_PINNED_REF`.

These examples are not a machine enum. Do not create machine consumers without an accepted contract, schema, policy, fixtures, tests, validator, and migration plan.

[Back to top](#top)

---

## 11. Machine-enforcement boundary

### 11.1 What exists

Repository evidence confirms separate bounded promotion-related surfaces, including:

- proposed ADR-0018;
- a fixture-first final-readiness A–G validator and read-only workflow;
- `PromotionDecision` and `PromotionReceipt` contract/schema families;
- publication-promotion architecture guidance;
- documentation metadata validation.

Those surfaces concern different responsibilities and maturity states. Their presence does not turn this intake criteria document into executable policy.

### 11.2 What is not established here

This change does not establish:

- a JSON Schema for intake criteria reviews;
- a Rego bundle or policy-gate registration for intake promotion;
- a validator that decides candidate or accepted packet state;
- a machine index for promotion packets;
- authenticated actor or stewardship resolution;
- an independent review quorum;
- a lifecycle transition applier;
- a release or publication service;
- public-serving permission.

### 11.3 Relationship to final-readiness A–G

The bounded final-readiness profile starts with a declared `CATALOG` or `TRIPLET` candidate targeting `PUBLISHED` and returns readiness for separate decision processing. It is not the documentation-intake process described here.

| Intake criteria | Final-readiness A–G |
|---|---|
| Evaluates whether a recommendation is reviewable and routeable | Evaluates declared closure of a lifecycle promotion-readiness packet |
| Human documentation guidance | Bounded executable validator profile plus documentation |
| Candidate/accepted/deferred/rejected packet dispositions | Readiness outcomes defined by its own profile |
| No lifecycle subject required | Declared `CATALOG` or `TRIPLET` candidate |
| No transition or release effect | No transition or release effect |
| Does not emit `PromotionDecision` or `PromotionReceipt` | Still separate from actual decision, transition, and release objects |

Use the exact profile and gate name rather than the word “promotion” alone.

[Back to top](#top)

---

## 12. Validation for criteria and packets

Validation is proportionate to the changed surface. A green check supports only the condition it actually evaluates.

### 12.1 Documentation checks for this page

A valid update should demonstrate:

- one H1 and one closed `KFM_META_BLOCK_V2`;
- creation and update dates grounded in repository history/current work;
- stable legacy H1 anchor preserved through explicit aliases;
- balanced Markdown fences, tables, alerts, and HTML anchors;
- repository-relative paths and case resolve;
- exact target, prior blob, base commit, inspection boundary, and rollback target recorded;
- no sibling authority silently selected or rewritten;
- intake, canonicalization, repository delivery, source admission, lifecycle, review, release, and publication states remain separate;
- no secret, private locator, living-person data, genomic material, protected coordinate, restricted source text, or harmful operational detail added;
- final newline and no trailing whitespace;
- remote diff limited to the intended path unless a direct dependency is explicitly added and justified.

### 12.2 Packet review checks

Select from:

- full-file and full-diff review;
- metadata, link, fragment, document graph, stale-reference, and docs-build checks;
- contract, schema, policy, fixture, validator, and workflow checks when behavior is involved;
- positive and negative fixture polarity;
- security, rights, sensitivity, privacy, source-role, and public-path review;
- compatibility and migration tests;
- no-network determinism where expected;
- exact-head hosted check inventory;
- remote branch, commit, file bytes, diff, and PR-state read-back.

### 12.3 Validation result labels

| Result | Meaning |
|---|---|
| `PASS` | The named check passed for the exact subject/ref |
| `FAIL` | The named check found a blocking condition |
| `WARNING` | A bounded non-blocking or inherited concern remains |
| `SKIPPED` | The check intentionally did not run; reason required |
| `PENDING` | No settled result yet |
| `NEEDS VERIFICATION` | A concrete check remains before reliance |

Do not use `PASS` without the check name and exact ref.

A draft PR may be delivered while hosted checks remain pending. Ready-for-review status requires the checks applicable to the changed area and risk to settle successfully, unless a documented inherited failure is separately classified and the current user explicitly authorizes that terminal state. Merge remains separate.

[Back to top](#top)

---

## 13. Anti-patterns

| Anti-pattern | Why it fails | Corrective posture |
|---|---|---|
| Treating a packet as canon | Intake has no authority over the destination | Cite the owning artifact or keep proposal labeled |
| Treating acceptance as `PromotionDecision` | Collapses documentation and release object families | Use “intake recommendation accepted” |
| Using file presence as implementation proof | Bytes do not prove behavior | Inspect code, config, tests, logs, or runtime |
| Counting repeated source documents as votes | Repetition is not adoption | Deduplicate and attach corroboration |
| Choosing a path by topic name | Violates responsibility-root law | Choose the owning responsibility and verify placement |
| Creating a second schema, policy, registry, proof, or release home | Splits authority and creates drift | Reconcile or require migration/ADR |
| Hiding a blocker in an aggregate score | Allows value to compensate for trust failure | Record gate result and reason explicitly |
| Approving your own evidence by role label | Role text is not identity or independence | Resolve accepted assignment and actor identity |
| Treating CODEOWNERS as review proof | Routing is not a `ReviewRecord` | Cite actual review evidence separately |
| Treating green CI as release | CI proves only tested conditions | Require separate decision and release authority |
| Publishing model or map output as root truth | Derived carriers can be fluent or visually convincing but wrong | Resolve evidence and policy or abstain |
| Client-side hiding of sensitive detail | Hidden data may remain recoverable | Transform before public delivery |
| Silent correction or deletion | Erases decision history and downstream reliance | Preserve correction, supersession, and rollback lineage |
| Leaving inactive candidates indefinitely | Produces an unreviewable shadow backlog | Defer, reject, archive, or record a re-entry trigger |
| Copying protected rationale into public Markdown | Discloses the harm the control is meant to prevent | Use public-safe summary and restricted route |

[Back to top](#top)

---

## 14. Open verification and sibling drift

| Priority | Item | Current bounded posture | Closure evidence |
|---|---|---|---|
| P0 | Exact canonical or compatibility classification of `docs/intake/` | **NEEDS VERIFICATION** | Accepted parent-root or Directory Rules decision with migration/non-effects |
| P0 | `triage-rules.md` remains a short placeholder | **CONFIRMED placeholder** | Separate dependency-closed modernization and review |
| P1 | Parent intake, canonicalization, and promotions documents describe this target as a placeholder at older evidence snapshots | **STALE sibling wording after this change** | Refresh those snapshots in their own same-path reviews; no behavioral dependency |
| P1 | Keep this criteria page aligned with the repository-grounded canonicalization policy when shared vocabulary changes | **CURRENT / trigger-based review** | Joint terminology review at the next material intake-state or adoption-boundary change |
| P1 | `candidate-canonical` and `candidate-for-promotion` vocabulary relationship | **CONFLICTED / NEEDS VERIFICATION** | Governed crosswalk or accepted vocabulary decision |
| P1 | Whether every packet requires `KFM_META_BLOCK_V2` | **NEEDS VERIFICATION** | Lane contract and metadata-workflow profile decision |
| P1 | Whether intake criteria should gain machine schema/policy/validator support | **PROPOSED only** | Accepted responsibility, contract, schema, policy, fixtures, tests, migration, and non-effects |
| P2 | Independent docs/intake stewardship beyond GitHub routing | **UNKNOWN** | Accepted assignments and review records |
| P2 | Machine packet index or register | **Not established** | Demonstrated need plus accepted authority and migration decision |
| P2 | Exact required hosted check set for this path | **NEEDS VERIFICATION** | Exact-head workflow results and repository settings/ruleset evidence |

### 14.1 Drift handling rule

Do not repair sibling snapshot prose by pretending its older evidence statement was false when authored. A later change should update its evidence snapshot, current profile, and no-loss ledger. This file's modernization creates documentation drift in those older summaries, not an authority or runtime conflict.

### 14.2 Re-review triggers

Re-evaluate these criteria when:

- Directory Rules, canonicalization guidance, or packet-state vocabulary changes;
- an intake criteria contract, schema, policy, validator, or register is proposed;
- a recurring candidate exposes a missing gate or ambiguous disposition;
- review assignments or CODEOWNERS routing changes;
- release/promotion vocabulary changes;
- a canonical surface cites this page as machine authority;
- rights, sensitivity, sovereignty, or public-boundary doctrine changes;
- the lane gains external consumers or automated mutation.

[Back to top](#top)

---

## 15. Rollback and correction

### 15.1 Documentation rollback target

**Prior blob:** `a542f5ea32c5a5e6ea666cdf216baa769f56066b`

### 15.2 Before merge

- Close or abandon the unmerged draft pull request and branch through separately authorized repository operations.
- Preserve the PR, diff, and review history.
- Do not delete a branch or comment merely to conceal the attempted change.

### 15.3 After an authorized merge

1. Revert the exact documentation commit or restore the prior blob through a new reviewed pull request.
2. Confirm the target path returns to the intended bytes.
3. Re-run metadata, link, graph, stale-reference, and documentation checks as triggered.
4. Correct sibling references if they were updated downstream.
5. Preserve the reason for rollback and any supersession record.

Correct or supersede this page when it directs work to the wrong owner root, creates parallel authority, collapses intake acceptance into adoption or release, weakens evidence or sensitivity boundaries, cites stale current behavior as confirmed, invents enforcement or reviewer state, exposes protected rationale, or conflicts with an accepted successor decision.

Because this change does not alter operational or public state, its rollback is documentation-only unless later work independently relied on mistaken guidance. Any such downstream reliance must be corrected in its own authority.

[Back to top](#top)

---

## 16. Non-effects

This update does not:

- accept or amend ADR-0018 or ADR-0029;
- settle the canonical classification of `docs/intake/`;
- complete or modify `triage-rules.md`, `canonicalization-policy.md`, or promotion state-lane READMEs;
- create a `PromotionDecision`, `PromotionReceipt`, `ReviewRecord`, `PolicyDecision`, `ReleaseManifest`, `CorrectionNotice`, `WithdrawalNotice`, or `RollbackCard`;
- create or change a contract, schema, policy, fixture, validator, register, workflow, package, app, pipeline, connector, source descriptor, receipt, proof, catalog, or published artifact;
- authenticate an actor, prove reviewer independence, or assign stewardship;
- admit or activate a source;
- apply a lifecycle transition;
- change branch protection, rulesets, repository settings, permissions, secrets, environments, or deployment configuration;
- release, deploy, promote, publish, correct, withdraw, or roll back public state.

[Back to top](#top)

---

## 17. No-loss modernization ledger

| Prior placeholder material | v1.0-draft treatment | Reason |
|---|---|---|
| H1 `Promotion Criteria` | **RETAINED through H1 wording and stable alias anchors** | Preserve reader intent and inbound navigation |
| “Evaluate whether an intake item is ready to move toward an owning authority path” | **RETAINED / EXPANDED** | Remains the document's one-line purpose |
| Placeholder warning | **SUPERSEDED** | The file is now substantive human guidance, not adopted policy |
| Source traceability | **RETAINED / EXPANDED as Gate 2** | Evidence-first operating requirement |
| Directory authority fit | **RETAINED / EXPANDED as placement and authority-collision gates** | Aligns with accepted Directory Rules |
| Rights/sensitivity screening | **RETAINED / EXPANDED as universal and conditional criteria** | Fail-closed public-safety requirement |
| Stewardship assignment | **RETAINED / NARROWED** | Verified routing and reviewer classes are required; assignments are not invented |
| Rollback feasibility | **RETAINED / EXPANDED** | Adds correction, supersession, abandonment, and downstream propagation |
| Missing state separation | **ADDED** | Prevents intake review from masquerading as lifecycle promotion or release |
| Missing distinctness and concurrency check | **ADDED** | Prevents duplicate work and parallel authority |
| Missing dependency closure | **ADDED** | Makes accepted scope buildable and reviewable |
| Missing validation and evidence sufficiency rules | **ADDED** | Gives reviewers observable criteria and bounded claims |
| Missing dispositions and anti-patterns | **ADDED** | Makes failure and routing outcomes explicit |
| Missing exact rollback target | **ADDED** | Preserves reversibility |

---

**Truth posture:** CONFIRMED current path, creation history, surrounding lane contracts, accepted placement authority, and bounded repository promotion surfaces / PROPOSED human intake criteria where no accepted machine policy exists / UNKNOWN independent assignments and operational enforcement / NEEDS VERIFICATION lane classification, sibling convergence, and exact-head hosted checks.

<p align="right"><a href="#top">Back to top</a></p>
