<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook-atmosphere-release
title: Atmosphere / Air Release Runbook
type: standard
profile: repository-grounded-release-readiness-and-handoff
version: v1.0
prior_version: proposed-scaffold
status: draft; repository-grounded; fixture-first; operational-release-hold; documentation-only; non-authoritative; non-publisher; not-for-life-safety
owners:
  - "@bartytime4life — verified GitHub review route only"
owner_status: "Atmosphere, source, evidence, policy, rights, sensitivity, validation, review, release, correction, rollback, deployment, public-surface, and independent-review assignments remain NEEDS VERIFICATION; CODEOWNERS routing does not establish those authorities."
created: NEEDS VERIFICATION — the prior scaffold carried no creation date
updated: 2026-08-24
policy_label: public; atmosphere; release-readiness; no-public-write; fail-closed; non-release; not-for-life-safety
current_path: docs/runbooks/atmosphere/RELEASE_RUNBOOK.md
owning_root: docs/
responsibility: "Document the current bounded procedure for assessing Atmosphere release readiness, exercising repository-owned fixture-only release checks, preparing a public-safe review handoff, and stopping before any operational release, deployment, publication, alerting, or public-state mutation."
truth_posture: >-
  CONFIRMED same-path repository placement, accepted Directory Rules basis,
  current scaffold preimage, empty Atmosphere candidate lane, absence of an
  Atmosphere ReleaseManifest and published payload, fixture-only ReleaseManifest
  contract/schema/validator/workflow, read-only generic release-dry-run checks,
  read-only Atmosphere release-readiness hold, placeholder Atmosphere proof and
  rollback records, inactive Atmosphere policy scaffolds, and one verified GitHub
  review route / PROPOSED future admitted candidate packet, resolvable proof,
  accepted policy evaluator, authenticated independent review, release authority,
  manifest assembly, signer custody, operational transition executor, public
  read-back, correction propagation, rollback, deployment, and monitoring /
  CONFLICTED legacy id-only versus strict fixture-only ReleaseManifest profiles,
  review/correction/storage lane drift, and older release prose versus current
  workflow behavior / UNKNOWN live source admission, production aliases, deployed
  consumers, external caches, public endpoint state, and operational official-source
  parity; cite-or-abstain
prepared_under_prompt: KFM Repository Build-Out & Markdown Modernization Implementation Agent v6.0.0
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 991f9f99634ceeb31228b22e593b1111f9b0510b
  target_prior_blob: 1a3ac56d5108197f57716f84a6db45370320a0f4
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  release_manifest_contract_blob: ce7dc89ff447d76d974afdd802b85a38538d8f48
  release_manifest_schema_blob: c76cd9bdddb34cf33c8eb62801269553726c5923
  release_manifest_validator_blob: 00307dc0d5e2c3867a229076e3702f8111455425
  release_manifest_workflow_blob: 2895266e202bf1f0a1d24c54e14f3b64f8a1c1c4
  release_dry_run_workflow_blob: 63d59382d11ed61f8405618e96af9ab8e49ef028
  domain_atmosphere_workflow_blob: fccba4b6e2cdae561ec8a4904446ed5dbe6ec8ce
  atmosphere_candidate_readme_blob: 2cff863a65c035cc167583ecae481c03580fc24a
  atmosphere_published_readme_blob: 25f26ea54c3c298175c510191427e5cef8eaa4cd
  atmosphere_policy_readme_blob: a300dfd5abda1b58a07fd978935dd40ef232ec71
  atmosphere_validation_runbook_blob: 4ae9d1e8b33ad2ed5df915813f859140602628d1
  atmosphere_stale_state_runbook_blob: 2b2050da0ef0e149101dc90478a0fb9c42417b63
  atmosphere_correction_runbook_blob: f04b6a5904be2b060f70637af8caddaf4511a227
  atmosphere_rollback_placeholder_blob: ba00c2191e8b190059e729d6c70bf8c69d4fc2da
inspection_boundary: >-
  Current-session GitHub reads of the target scaffold, current main, accepted
  Directory Rules evidence, release root and ReleaseManifest family, generic and
  Atmosphere release-readiness workflows, Atmosphere candidate and published
  inventories, policy, validation, stale-state, correction, rollback, review,
  proof, and publish-pipeline boundaries. Repository-native commands were not run
  in a mounted checkout during authoring. No live source was contacted; no
  candidate, manifest, policy decision, review record, release decision, signature,
  correction, withdrawal, rollback, deployment, promotion, publication, alert,
  medical determination, regulatory determination, or public-state transition was
  created or performed.
related:
  - docs/runbooks/README.md
  - docs/runbooks/RELEASE_DRY_RUN.md
  - docs/runbooks/atmosphere/README.md
  - docs/runbooks/atmosphere/SOURCE_REFRESH_RUNBOOK.md
  - docs/runbooks/atmosphere/NO_NETWORK_TEST_RUNBOOK.md
  - docs/runbooks/atmosphere/VALIDATION_RUNBOOK.md
  - docs/runbooks/atmosphere/PROMOTION_RUNBOOK.md
  - docs/runbooks/atmosphere/STALE_STATE_RUNBOOK.md
  - docs/runbooks/atmosphere/CORRECTION_RUNBOOK.md
  - docs/runbooks/atmosphere/ROLLBACK_RUNBOOK.md
  - docs/runbooks/atmosphere/RELEASE_ROLLBACK_RUNBOOK.md
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/domains/atmosphere/README.md
  - docs/domains/atmosphere/PUBLICATION_POSTURE.md
  - docs/domains/atmosphere/RELEASE_INDEX.md
  - contracts/release/release_manifest.md
  - schemas/contracts/v1/release/release_manifest.schema.json
  - fixtures/release/release_manifest/
  - tools/validators/release/validate_release_manifest.py
  - tests/validators/test_validate_release_manifest.py
  - release/README.md
  - release/candidates/atmosphere/README.md
  - release/manifests/README.md
  - release/reviews/atmosphere/README.md
  - release/rollback_cards/rel-atmosphere-pm25-2026-001.card.json
  - data/proofs/atmosphere/README.md
  - data/published/atmosphere/README.md
  - policy/domains/atmosphere/README.md
  - pipelines/domains/atmosphere/publish/README.md
  - .github/workflows/release-manifest.yml
  - .github/workflows/release-dry-run.yml
  - .github/workflows/domain-atmosphere.yml
tags: [kfm, runbook, atmosphere, air, release, release-readiness, release-manifest, evidence, policy, review, correction, rollback, freshness, no-public-write, not-for-life-safety]
notes:
  - "Same-path documentation modernization under accepted ADR-0029; no root, lane, contract, schema, policy, fixture, validator, test, workflow, receipt, proof, release object, or public state is created or moved."
  - "The current repository contains release-oriented fixture checks, but no admitted Atmosphere candidate, operational Atmosphere manifest, accepted Atmosphere release policy, authenticated release authority, or published Atmosphere payload was verified."
  - "The strict ReleaseManifest profile is PROPOSED_INACTIVE and FIXTURE_ONLY; every authority-bearing governance flag remains false even on PASS."
  - "The generic release dry run and the Atmosphere domain workflow are no-public-write readiness checks, not release execution."
  - "KFM Atmosphere is not an official AQI, medical, regulatory, emergency-alerting, or life-safety authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Atmosphere / Air Release Runbook

> **Repository-grounded procedure for determining whether an Atmosphere candidate is ready for accountable release review, exercising only the current no-public-write checks, preparing a traceable handoff, and stopping before any release, deployment, publication, alerting, or public-state mutation.**

<p>
  <img alt="Status: repository-grounded draft" src="https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b">
  <img alt="Domain: atmosphere" src="https://img.shields.io/badge/domain-atmosphere-1f8fff">
  <img alt="Release checks: fixture first" src="https://img.shields.io/badge/release%20checks-fixture%20first-8250df">
  <img alt="Operational release: hold" src="https://img.shields.io/badge/operational%20release-HOLD-b42318">
  <img alt="Public writes: none" src="https://img.shields.io/badge/public%20writes-none-6e7781">
  <img alt="Life safety: not an authority" src="https://img.shields.io/badge/life%20safety-not%20an%20authority-b42318">
</p>

> [!IMPORTANT]
> **This runbook does not release anything.** It documents readiness inspection, fixture-only validation, and review handoff. A candidate, schema-valid manifest, passing test, green workflow, review note, pull request, merge, signature-shaped file, or path under `data/published/` is not a release or publication authority.

> [!WARNING]
> **KFM Atmosphere is not an official AQI, medical, regulatory, emergency-alerting, or life-safety authority.** Do not use this procedure to declare current conditions safe or unsafe, issue health guidance, replace an agency advisory, certify a sensor, or originate operational instructions. Advisory context remains referral-only and must point to the official issuing source.

> [!CAUTION]
> **Operational Atmosphere release remains `HOLD`.** The inspected repository has no child candidate dossier, no Atmosphere ReleaseManifest, no released Atmosphere payload, no accepted Atmosphere policy evaluator, no authenticated release authority, and no domain-specific release executor. The current checks are synthetic, read-only, and explicitly non-publishing.

**Quick navigation:** [Purpose](#1-purpose-scope-and-terminal-boundary) · [Authority](#2-authority-placement-and-current-evidence) · [Posture](#3-current-repository-release-posture) · [Separation](#4-release-state-and-object-family-separation) · [Invariants](#5-atmosphere-release-invariants) · [Roles](#6-roles-and-separation-of-duties) · [Preflight](#7-authority-freeze-preconditions-and-stop-conditions) · [Modes](#8-supported-operating-modes) · [Procedure](#9-release-readiness-and-handoff-procedure) · [Manifest](#10-releasemanifest-profile-and-bounded-validation) · [Outcomes](#11-finite-outcomes-and-claim-boundaries) · [Packet](#12-accountable-review-handoff-packet) · [Public safety](#13-rights-sensitivity-time-and-public-safety) · [CI](#14-hosted-ci-and-exact-head-evidence) · [Correction](#15-correction-withdrawal-rollback-and-read-back) · [Anti-patterns](#16-anti-patterns) · [Open work](#17-current-holds-and-open-verification) · [Maintenance](#18-maintenance-correction-and-document-rollback) · [Checklist](#appendix-a-operator-checklist) · [Commands](#appendix-b-current-command-and-surface-matrix)

---

## 1. Purpose, scope, and terminal boundary

### 1.1 Purpose

Use this runbook when a public-safe Atmosphere candidate appears ready to leave `CATALOG / TRIPLET` and enter accountable release review.

The operator's job is to:

1. freeze the exact repository revision, candidate identity, artifact set, audience, time scope, and requested transition;
2. verify that the candidate actually exists and is not merely a roadmap row, proof placeholder, stale index entry, or generated example;
3. preserve source role, knowledge character, time, freshness, rights, sensitivity, evidence, review, correction, and rollback distinctions;
4. run only the repository-owned no-public-write checks that are currently implemented;
5. interpret every result within its declared fixture or readiness boundary;
6. prepare a public-safe, immutable review handoff;
7. stop when evidence, policy, review, release authority, execution, deployment, or public read-back is absent.

### 1.2 In scope

- Atmosphere release-candidate inventory and identity checks.
- Immutable artifact references and digests.
- SourceDescriptor and EvidenceBundle support pointers.
- Atmosphere validation, source-role, knowledge-character, unit, time, freshness, rights, sensitivity, caveat, and official-authority checks.
- Fixture-only ReleaseManifest shape and semantic validation.
- Generic no-public-write release dry-run and bounded A–G readiness evidence.
- Review, correction, withdrawal, rollback, and stale-state handoff.
- Public-safe review records that disclose blockers without exposing restricted or operational detail.
- Exact-head hosted-check interpretation.

### 1.3 Out of scope

This runbook does not:

- admit or activate a source;
- contact EPA, KDHE, NOAA/NWS, Kansas Mesonet, community sensors, model providers, or any other live service;
- confirm current air quality, weather, smoke, forecast, climate, sensor, or advisory conditions;
- create or resolve an EvidenceBundle when the accepted producer/resolver does not exist;
- activate the Atmosphere Rego files as a policy bundle;
- authenticate a reviewer, steward, signer, or release authority;
- invent a candidate, release ID, artifact digest, rights grant, freshness threshold, review result, rollback target, or official-source statement;
- write or move data into `data/published/`;
- assemble or persist an operational ReleaseManifest;
- mutate an alias, cache, CDN, search index, graph projection, API route, tile service, map layer, dashboard, or AI surface;
- sign, release, deploy, promote, publish, withdraw, correct, or roll back;
- issue medical, regulatory, emergency, or life-safety guidance;
- treat a release path, GitHub merge, badge, map rendering, or generated language as proof of public state.

### 1.4 Terminal boundary

The maximum output of this procedure is a **readiness or hold packet for accountable human review**.

Permitted terminal dispositions include:

- no active candidate verified;
- hold for a named missing dependency;
- deny because a governing condition forbids release;
- error because the release posture cannot be evaluated safely;
- ready for accountable review, with every unresolved transition still explicit.

No disposition from this runbook means `RELEASED`, `DEPLOYED`, or `PUBLISHED`.

[Back to top](#top)

---

## 2. Authority, placement, and current evidence

### 2.1 Directory Rules basis

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts [Directory Rules v2](../../doctrine/directory-rules.md). This file is a human operational procedure at an already tracked path:

```text
docs/runbooks/atmosphere/RELEASE_RUNBOOK.md
```

The placement outcome is `PLACE`: update the existing file in place under the `docs/` responsibility root. Do not create a second release runbook under `release/`, `data/`, `policy/`, `pipelines/`, or the Atmosphere domain dossier.

| Responsibility | Owning surface | Relationship to this runbook |
|---|---|---|
| Human Atmosphere release-readiness procedure | `docs/runbooks/atmosphere/` | **Owned here** |
| Release object meaning | [`contracts/release/`](../../../contracts/release/) | Referenced; not redefined |
| Machine shape | [`schemas/contracts/v1/release/`](../../../schemas/contracts/v1/release/) | Referenced; validation is not approval |
| Release decisions | [`release/`](../../../release/README.md) | Separate append-only decision plane |
| Candidate dossiers | [`release/candidates/atmosphere/`](../../../release/candidates/atmosphere/README.md) | Pre-publication review input |
| Evidence and proof | [`data/proofs/`](../../../data/proofs/) | Separate from release decisions |
| Process memory | [`data/receipts/`](../../../data/receipts/) | Separate from proof and authority |
| Published carriers | [`data/published/atmosphere/`](../../../data/published/atmosphere/README.md) | Downstream public-safe artifacts only |
| Atmosphere policy source | [`policy/domains/atmosphere/`](../../../policy/domains/atmosphere/README.md) | Proposed scaffolds; currently unbound |
| Artifact assembly | [`pipelines/domains/atmosphere/publish/`](../../../pipelines/domains/atmosphere/publish/README.md) | Proposed executable sublane; not release authority |
| Public delivery | Governed APIs and released public-safe carriers | Not exercised by this runbook |

### 2.2 Evidence hierarchy

For this procedure, use the following order:

1. accepted KFM invariants and accepted ADRs;
2. adopted Directory Rules and current machine projections;
3. current contracts, schemas, policy, release records, and exact repository bytes;
4. current tests, validators, workflows, receipts, proofs, and runtime evidence;
5. current accountable human decisions;
6. this runbook;
7. older proposal-era documents, examples, generated text, and memory.

When an older runbook conflicts with current workflows or current object-family evidence, preserve the older document as lineage and use current exact-revision implementation evidence for present behavior.

### 2.3 Negative authority

This document may explain how to prepare a release handoff. It cannot:

- approve a candidate;
- turn a `PASS` into a policy allow;
- appoint a reviewer;
- make CODEOWNERS independent review;
- convert a proposed schema into an accepted contract;
- transform a placeholder into evidence;
- bind a public alias;
- authorize use of a source or carrier;
- make an Atmosphere statement official.

[Back to top](#top)

---

## 3. Current repository release posture

The observations below are pinned to `main@991f9f99634ceeb31228b22e593b1111f9b0510b`.

| Surface | CONFIRMED current evidence | Safe conclusion |
|---|---|---|
| Target file | Short `PROPOSED scaffold`, prior blob `1a3ac56d...` | The scaffold is not an operational procedure |
| Candidate lane | `release/candidates/atmosphere/` contains its README and no child dossier | `NO_ACTIVE_CANDIDATE_VERIFIED` |
| Atmosphere manifest | No Atmosphere entry was found in the inspected `release/manifests/` inventory | No Atmosphere ReleaseManifest is established |
| Published Atmosphere lane | `data/published/atmosphere/` contains only its README and `.gitkeep` | No published Atmosphere payload is established |
| Atmosphere proof lane | One PM2.5 `evidence_bundle.json` is intentionally an exact `PROPOSED` placeholder | Placeholder recognition is not evidence or proof validation |
| Atmosphere rollback record | `rel-atmosphere-pm25-2026-001.card.json` is a four-field `PROPOSED` inventory placeholder | No operational RollbackCard is established |
| ReleaseManifest contract | Draft v0.3 dual-profile contract | Semantic direction exists; production profile remains unaccepted |
| ReleaseManifest schema | Legacy permissive branch plus closed strict candidate branch | An id-only object may validate; strict PASS remains fixture-only |
| ReleaseManifest validator | Deterministic no-network validator with 21 reviewed fixture cases | Local shape/semantic proof only |
| ReleaseManifest workflow | Read-only focused workflow | No refs, bytes, signatures, review, release, or public use are authenticated |
| Generic release dry run | Read-only workflow exercises synthetic publication denials, A–G readiness, and rollback-card readiness | No candidate, decision, manifest, signature, release, or published artifact is emitted |
| Atmosphere domain workflow | Bounded synthetic validation plus explicit proof and release-dry-run holds | Domain release readiness remains held |
| Atmosphere policy | Thirteen default-only Rego scaffolds; no accepted entry point, bundle, evaluator, or runtime | Policy is unbound and inactive |
| Atmosphere review lane | Draft README with proposed roles; no authenticated review record was verified | Review guidance exists; accountable review remains unproved |
| Publish pipeline | README-defined boundary; concrete executable behavior and release wiring remain unverified | Artifact assembly is proposed, not operational |
| GitHub review route | `@bartytime4life` is the verified repository route | Routing is not source, policy, review, signing, or release authority |
| Deployment and public endpoint | Not established by the inspected repository surfaces | `UNKNOWN / HOLD` |

### 3.1 Operational determination

The correct current result for an attempted Atmosphere release is:

```text
HOLD
```

until all of the following are established for one immutable candidate:

- admitted source identity and permitted use;
- public-safe artifact set;
- EvidenceRef-to-EvidenceBundle closure;
- accepted policy evaluation and obligations;
- substantive validation and negative cases;
- authenticated review and required separation of duties;
- accepted ReleaseManifest profile;
- correction, withdrawal, stale-state, and rollback support;
- an authorized operational transition executor;
- deployment and public read-back evidence.

### 3.2 What repository-grounded means here

`repository-grounded` means the runbook accurately describes current repository evidence. It does **not** mean:

- a live source is admitted;
- the procedures are operationally admitted;
- a release authority exists;
- a public endpoint is deployed;
- current Atmosphere information is accurate or safe to use;
- a release has occurred.

[Back to top](#top)

---

## 4. Release state and object-family separation

The canonical lifecycle remains:

```text
SOURCE EDGE
  -> admission decision
  -> RAW
  -> WORK / QUARANTINE
  -> PROCESSED
  -> CATALOG / TRIPLET
  -> candidate and accountable release review
  -> separately authorized release transition
  -> PUBLISHED public-safe carrier
  -> correction / withdrawal / rollback / recompile
```

Promotion and release are governed state transitions. They are not file moves, commits, pull requests, merges, workflow conclusions, signatures, or UI actions.

### 4.1 Do not collapse these states

| State | Example | What it does not prove |
|---|---|---|
| File presence | Candidate README or manifest-shaped JSON exists | Candidate admission, validity, review, or release |
| Candidate state | Dossier assembled under `release/candidates/` | Policy allow or manifest authority |
| Validation state | Schema/validator returns `PASS` | Evidence truth, rights, review, release, or publication |
| Readiness state | Synthetic A–G packet returns `APPROVE_READY` | An authenticated PromotionDecision or applied transition |
| Review state | Review record exists | Release unless the accepted release profile grants that effect |
| Manifest state | ReleaseManifest-shaped record validates | Persisted release decision or public alias binding |
| Signature state | Digest/signature verifies | Evidence truth, rights, policy, review, or public use |
| Release state | Accountable authority approves a specific immutable package | Deployment or public exposure unless separately applied |
| Deployment state | Carrier is present in an environment | Governed public release or correctness |
| Publication state | Governed public-safe carrier is exposed | Truth outside its evidence, scope, time, caveats, and correction lineage |
| Stale state | Support aged beyond a declared condition | The original claim was necessarily wrong |
| Correction state | Superseding release and notice are approved/applied | Erasure of prior audit history |
| Rollback state | Prior safe package is restored through governed controls | Correction of every downstream interpretation without read-back |

### 4.2 Object families remain distinct

| Object family | Role | Cannot prove alone |
|---|---|---|
| `SourceDescriptor` | Source identity, role, rights, cadence, sensitivity, and access context | Claim truth or release |
| `EvidenceRef` / `EvidenceBundle` | Support and limitations for a bounded claim | Policy allow or publication |
| `ValidationReport` | Named checks over a pinned subject | Scientific truth, review, or release |
| `PolicyDecision` | Evaluator result and obligations for a pinned request | Reviewer authority or applied transition |
| `ReviewRecord` | Governed human review for a defined scope | Release unless explicitly authorized |
| `PromotionDecision` | Accountable readiness/transition decision | Applied release or public exposure by itself |
| `ReleaseManifest` | Immutable binding of an approved artifact set and trust references | Artifact storage or release execution |
| `RunReceipt` | Process memory about what ran | Correctness or authority |
| Proof object | Closure evidence for a defined proposition | Release authority |
| `CorrectionNotice` / `WithdrawalNotice` | Public correction or withdrawal lineage | Applied invalidation without execution/read-back |
| `RollbackCard` | Rollback intent, scope, target, and plan | Executed rollback |
| Published carrier | Public-safe released artifact | Canonical source truth beyond its declared role |

### 4.3 Candidate, decision, and carrier homes

```text
release/candidates/atmosphere/     # candidate dossiers and blockers
release/manifests/                 # release decision bindings
release/promotion_decisions/       # promotion/release decision records
release/reviews/atmosphere/        # review records or indexes
release/correction_notices/        # correction lineage
release/withdrawal_notices/        # withdrawal lineage
release/rollback_cards/            # rollback candidates/records
data/published/atmosphere/          # released public-safe carriers
```

Current path presence does not settle every child-lane maturity or canonical conflict. Do not create a trust-bearing record in an ambiguous lane without the release root contract and a current placement decision.

[Back to top](#top)

---

## 5. Atmosphere release invariants

Every Atmosphere release review must preserve these invariants.

### 5.1 Knowledge character

- AQI is not concentration.
- AOD is not surface PM2.5.
- A modeled or forecast field is not an observation.
- A low-cost sensor product is not regulatory evidence merely because it is calibrated or visually plausible.
- A derived fusion product retains its input roles, methods, uncertainty, and limitations.
- Advisory context is not an instruction issued by KFM.

### 5.2 Time and freshness

Keep these time kinds distinct where material:

- source time;
- observed time;
- valid time;
- model-run time;
- retrieval time;
- release/effective time;
- correction time;
- transaction or repository time.

A public-current carrier needs a declared freshness rule and visible stale-state behavior. Do not extend a valid window because a source refresh is late, and do not rewrite history to make a stale release appear current.

### 5.3 Rights and sensitivity

Unknown or changed rights fail closed. Public availability does not settle redistribution, derivative display, attribution, model use, or commercial use.

Exact station, sensor, infrastructure, or cross-layer joins may require generalization, redaction, restriction, or denial. Styling, hidden fields, client-side filters, or default zoom are not security transformations.

### 5.4 Evidence and citations

Every consequential public claim must resolve to admissible support at the release scope. A URL, citation string, source name, map tile, dashboard, model output, or generated summary is not an EvidenceBundle.

### 5.5 Official-authority boundary

For advisories, alerts, and current-sensitive public use:

- identify the official issuing source;
- preserve issue/valid/expiry time and status;
- redirect rather than paraphrase imperative instructions;
- abstain or deny when KFM cannot verify current official context;
- route Hazards-owned event or life-safety concerns to the Hazards seam.

### 5.6 Public-client boundary

Public clients consume only governed APIs and released public-safe carriers. No normal public path may read:

- RAW;
- WORK;
- QUARANTINE;
- candidate stores;
- restricted evidence;
- proof internals;
- direct source credentials;
- direct model/provider output;
- unreviewed generated summaries.

[Back to top](#top)

---

## 6. Roles and separation of duties

Only the GitHub review route is verified. The roles below describe required responsibilities; they are not current appointments.

| Role | Required responsibility | Must not be inferred from |
|---|---|---|
| Atmosphere domain steward | Confirms domain meaning, source-role discipline, time/freshness semantics, caveats, and candidate scope | File authorship or CODEOWNERS alone |
| Source/rights steward | Confirms admission, terms, attribution, redistribution, cadence, and source authority | Public URL or successful fetch |
| Evidence steward | Confirms EvidenceRef closure, claim scope, limitations, and contradiction handling | Citation text or a hash alone |
| Sensitivity/public-safety reviewer | Assesses location, join, public-audience, advisory, and reverse-inference risk | A hidden field or generalized appearance |
| Validation steward | Confirms exact validator profile, revision, fixtures, findings, and proof limit | Green workflow name alone |
| Policy steward | Owns accepted input profile, bundle, entry point, evaluator, decisions, and obligations | Rego file presence |
| Independent reviewer | Reviews consequential support and separation from the author where required | Automated checks or self-declaration |
| Release authority | Decides whether one immutable package may transition under an accepted release profile | Readiness PASS, PR approval, merge, or signature alone |
| Correction/rollback steward | Confirms correction lineage, withdrawal, invalidation, rollback target, and read-back | A placeholder card or path name |
| Deployment/operator role | Applies an authorized transition in the named environment and records read-back | Repository write access |
| AI assistant | May summarize already governed evidence and draft public-safe handoff text | Truth, policy, review, or release authority |

> [!IMPORTANT]
> If the required accountable actor, authority interval, scope, or independence cannot be verified, the result is `HOLD`. Do not lower the review burden to match available staffing.

[Back to top](#top)

---

## 7. Authority freeze, preconditions, and stop conditions

### 7.1 Authority freeze

Before any release-readiness work, record:

- repository and exact base/head SHA;
- candidate ID and path;
- target audience and environment;
- artifact set and immutable digests;
- current release, predecessor, correction, withdrawal, and rollback references;
- applicable contracts, schemas, policy profile, and evaluator;
- required reviewers and authority records;
- active branches and pull requests that overlap the candidate, release family, or public carrier;
- non-goals and terminal boundary.

Recheck this freeze immediately before the review handoff. Base or candidate drift invalidates prior conclusions until reconciled.

### 7.2 Minimum preconditions

A real Atmosphere release review cannot begin unless all applicable items resolve:

- [ ] One child candidate dossier exists under the accepted candidate lane.
- [ ] The dossier has stable identity and an immutable subject/artifact set.
- [ ] Every source is admitted for the exact use and audience.
- [ ] Rights, attribution, redistribution, and sensitivity posture are current.
- [ ] Source roles and knowledge characters are explicit and non-collapsed.
- [ ] Units, averaging periods, spatial scope, CRS, and time facets are coherent.
- [ ] Freshness/stale-state rules and official-source redirects are declared.
- [ ] EvidenceRefs resolve to admissible EvidenceBundles.
- [ ] Required validation reports and negative cases pass at the exact revision.
- [ ] The accepted policy profile evaluates the exact request and obligations are satisfiable.
- [ ] Required review records are authenticated and within authority intervals.
- [ ] The candidate artifact bytes and manifest references are digest-bound.
- [ ] Correction, withdrawal, supersession, and rollback paths are complete.
- [ ] Deployment target, transition executor, alias/cache behavior, and read-back procedure are defined.
- [ ] No active overlapping change owns the same candidate or transition.

At the current repository snapshot, these preconditions are not closed for an Atmosphere release.

### 7.3 Hard stop conditions

Stop and record a public-safe hold when any of the following applies:

1. No actual candidate dossier exists.
2. A proof, rollback card, manifest, review, or policy record is a placeholder.
3. A legacy id-only ReleaseManifest is being treated as release-complete.
4. A strict fixture candidate is being treated as operational authority.
5. EvidenceRefs do not resolve to admissible EvidenceBundles.
6. Rights, sensitivity, source role, currentness, or official-source status is unknown.
7. AQI, concentration, AOD, PM2.5, model, observation, low-cost sensor, advisory, or regulatory roles are collapsed.
8. An Atmosphere policy bundle, entry point, evaluator, or obligations handler is absent.
9. Reviewer identity, authority, scope, validity interval, or separation is unverified.
10. Artifact digests or immutable references are missing or use a floating `latest` pointer.
11. Correction, withdrawal, stale-state, invalidation, or rollback support is absent.
12. The requested command would write to release or public state from untrusted pull-request code.
13. The public client would read internal, candidate, restricted, or direct-model state.
14. A workflow is queued, skipped, canceled, stale, or belongs to another head but is presented as success.
15. The operator cannot state what the result proves and what remains unproved.
16. The operation would position KFM as a medical, regulatory, emergency, or life-safety authority.

[Back to top](#top)

---

## 8. Supported operating modes

### 8.1 Mode A — Repository-only release posture inspection

**Purpose:** Determine whether an Atmosphere candidate and its required release surfaces exist at an exact revision.

**Inputs:** repository SHA, target candidate lane, release root, proof lane, policy lane, published lane.

**Current expected result:** no active candidate verified; operational release `HOLD`.

**Public effect:** none.

### 8.2 Mode B — ReleaseManifest fixture profile

**Purpose:** Validate the repository's synthetic strict ReleaseManifest cases.

**Entry points:**

```bash
python -m unittest tests.validators.test_validate_release_manifest -v
python tools/validators/release/validate_release_manifest.py --fixtures
```

**What PASS proves:** reviewed local fixture polarity, closed strict-candidate shape, selected deterministic semantics, and no-network behavior at the tested revision.

**What PASS does not prove:** reference resolution, artifact bytes, signatures, policy, reviewer authentication, release persistence, alias mutation, deployment, publication, or public use.

### 8.3 Mode C — Generic release dry run

**Purpose:** Exercise repository-owned publication-denial cases, bounded A–G readiness, and rollback-card readiness without public writes.

**Entry point:**

```bash
make release-dry-run
```

The hosted workflow also runs `make publish-check` and rollback-card fixture/rehearsal checks in separate jobs.

**What success proves:** the exact synthetic checks declared by the workflow passed.

**What success does not prove:** an Atmosphere candidate exists, an Atmosphere policy evaluated, a real reviewer approved, a manifest was assembled, or a release occurred.

### 8.4 Mode D — Atmosphere domain release-readiness hold

The `domain-atmosphere` workflow currently inspects release prerequisites and deliberately emits:

```text
WORKFLOW_SKIPPED_EXPLICIT: publish-dry-run-atmosphere
WORKFLOW_HOLD: no accepted Atmosphere release dry-run command or candidate manifest contract
```

That held job is a guard against silently graduating the domain. It is not a skipped requirement that an operator may ignore.

### 8.5 Mode E — Accountable release review handoff

**Purpose:** Package exact evidence and blockers for authorized humans.

**Current support:** documentation and review-lane guidance only.

**Maximum result:** `READY_FOR_ACCOUNTABLE_REVIEW` as a runbook-level handoff label. This label is not a machine PromotionDecision, release approval, or publication state.

### 8.6 Mode F — Operational release

**Status:** `HOLD / UNKNOWN`.

No current evidence in this run establishes:

- an accepted Atmosphere candidate profile;
- an operational manifest assembly path;
- active Atmosphere policy evaluation;
- authenticated independent review;
- signer custody;
- an authorized transition executor;
- production alias/cache mutation;
- deployment;
- public read-back;
- first governed Atmosphere release.

[Back to top](#top)

---

## 9. Release-readiness and handoff procedure

### Step 1 — Freeze exact identity

Record the current repository SHA, candidate path, candidate digest, artifact references, requested audience, target environment, and non-goals.

Search current pull requests and branches for overlap. Do not infer independence from branch names or issue titles.

### Step 2 — Prove the candidate exists

Inspect `release/candidates/atmosphere/` directly.

Accept a candidate only when a child dossier exists and its identity, status, subject, artifact set, blockers, evidence snapshot, and non-release posture are explicit.

At the pinned snapshot, only the lane README exists. Stop with `NO_ACTIVE_CANDIDATE_VERIFIED`.

### Step 3 — Classify every supporting surface

For each referenced object, classify it as:

- substantive current record;
- fixture-only candidate;
- placeholder;
- proposal-era documentation;
- stale;
- conflicted;
- unknown.

Do not upgrade a placeholder `evidence_bundle.json`, rollback card, id-only manifest, README row, generated receipt, or sample path into support.

### Step 4 — Verify source and evidence closure

For each consequential public claim:

1. resolve the admitted SourceDescriptor;
2. verify source role, authority role, rights, terms, cadence, sensitivity, and content identity;
3. resolve each EvidenceRef to the required EvidenceBundle;
4. verify scope, time, limitations, contradictions, and source-role compatibility;
5. record any unresolved support as `HOLD_FOR_EVIDENCE` or the accepted equivalent.

Do not retrieve a live source as part of this release runbook.

### Step 5 — Verify Atmosphere meaning and time

Check:

- parameter and unit;
- averaging period;
- station/network identity;
- observed versus modeled status;
- AQI versus concentration;
- AOD versus surface PM2.5;
- low-cost sensor correction/caveat/confidence/limitations;
- model-run and forecast validity;
- source, observed, valid, retrieval, release, and correction times;
- currentness/stale-state rules;
- official advisory issuer and redirect.

A semantic or time mismatch returns to the owning upstream lane. Do not patch meaning in a ReleaseManifest.

### Step 6 — Run affected bounded validation

Use the current [Atmosphere Validation Runbook](./VALIDATION_RUNBOOK.md) for the exact affected profiles.

Record:

- command;
- repository/head SHA;
- fixture or subject identity;
- expected polarity;
- actual finite outcome;
- findings;
- generated outputs, if any;
- proof limit;
- introduced, inherited, expected, pending, skipped, or unrelated status.

A broad `domain-atmosphere` workflow success does not replace candidate-specific validation.

### Step 7 — Run fixture-only release checks when applicable

For changes to the ReleaseManifest family or when reviewing its current readiness boundary, run:

```bash
python -m unittest tests.validators.test_validate_release_manifest -v
python tools/validators/release/validate_release_manifest.py --fixtures
```

For the generic no-public-write release boundary, run:

```bash
make release-dry-run
```

Do not create a fake Atmosphere candidate merely to make the domain-specific hold job pass.

### Step 8 — Prepare, but do not authorize, the manifest candidate

Only after an accepted candidate profile exists may a manifest candidate be prepared.

It should bind, by immutable references:

- release and candidate identity;
- artifact list, media types, roles, and digests;
- SourceDescriptor refs;
- EvidenceBundle refs;
- policy-decision refs;
- promotion-decision refs;
- review-record refs;
- catalog refs;
- proof and receipt refs;
- attestations;
- audience, rights, sensitivity, generalization, and transform receipts;
- effective time window;
- predecessor, correction, withdrawal, and rollback lineage;
- validator and run-receipt provenance.

A strict fixture candidate must keep all governance authority flags `false`. Do not flip those flags to simulate release.

### Step 9 — Obtain policy and accountable review

Submit the exact immutable candidate to the accepted policy evaluator and required human reviewers.

The packet must preserve:

- evaluator and bundle identity;
- policy input hash;
- finite policy result;
- reason codes and obligations;
- reviewer identity and authority record;
- review scope and validity interval;
- author/reviewer/release-authority separation where required;
- unresolved dissent or conflict.

Current Atmosphere policy and reviewer authority remain unverified. Therefore this step currently ends in `HOLD`.

### Step 10 — Obtain an explicit release decision

Only an authenticated release authority operating under an accepted release profile may decide the transition.

The decision must identify:

- exact candidate;
- exact manifest;
- exact support set;
- exact audience and environment;
- obligations;
- correction and rollback support;
- effective time;
- decision identity and authority interval.

A pull-request approval, merge, or code-owner review is not this decision.

### Step 11 — Apply through an authorized transition executor

This step is outside the current runbook's executable authority and is currently `HOLD`.

A future executor must be:

- deny-by-default;
- least-privilege;
- environment-scoped;
- immutable-input and digest-bound;
- separate from untrusted pull-request execution;
- auditable;
- reversible;
- able to emit an applied-transition record;
- able to invalidate or advance aliases and caches safely;
- unable to read or publish restricted state outside the approved package.

### Step 12 — Verify public read-back

After a separately authorized transition, independently verify:

- served manifest identity;
- carrier digests;
- governed API envelope;
- map/layer state;
- Evidence Drawer resolution;
- time/freshness and stale-state display;
- source-role and knowledge-character labels;
- official-source redirects;
- search, graph, export, cache, dashboard, and AI parity;
- correction, withdrawal, and rollback links.

No such public read-back is performed by this documentation change.

### Step 13 — Close with explicit state separation

Record separately:

- validation result;
- policy result;
- review state;
- release decision state;
- applied transition state;
- deployment state;
- publication/read-back state;
- correction/rollback readiness.

Never summarize the whole sequence as “green” or “released” without naming each state and its evidence.

[Back to top](#top)

---

## 10. ReleaseManifest profile and bounded validation

### 10.1 Current dual-profile schema

The paired schema has two branches:

| Profile | Current shape | Safe interpretation |
|---|---|---|
| Legacy compatibility | `id` required; optional `spec_hash` and `version`; additional properties allowed | Backward-compatible scaffold only; release-incomplete |
| Strict fixture candidate | Closed `ReleaseManifest` object with deterministic identity, artifacts, refs, scope, time, lineage, provenance, and all authority flags false | `PROPOSED_INACTIVE / FIXTURE_ONLY`; local validation only |

> [!WARNING]
> An id-only manifest can pass the legacy branch while proving almost nothing about release completeness. Never cite legacy schema PASS as evidence that a release is valid, approved, deployed, or public.

### 10.2 Strict candidate checks

The current validator checks selected local properties, including:

- RFC 8785 JCS plus SHA-256 identity construction;
- content-derived fixture manifest ID;
- canonical sorted duplicate-free reference arrays;
- canonical artifact ordering and exact artifact count;
- EvidenceBundle artifact/ref pairing;
- denial of floating `latest` references;
- cross-role reference-collapse checks;
- coherent effective-time windows;
- predecessor requirement for corrections;
- public audience requirements for approved rights, acceptable sensitivity, evidence, policy, promotion, and review refs;
- transform-receipt requirements when generalization is declared;
- all governance authority flags remain false;
- bounded JSON parsing, duplicate-key, non-finite-number, symlink, size, and schema-error handling.

### 10.3 Validator outcomes

| Outcome | Meaning | Release effect |
|---|---|---|
| `PASS` | Selected local fixture shape and semantics passed | None |
| `FAIL` | Candidate violated declared shape/semantic rules | None; retain prior state |
| `ERROR` | Validator could not evaluate safely | None; diagnose before reuse |

The validator serializes `authority_created: false`. Preserve that boundary in every handoff.

### 10.4 Workflow boundary

The focused `release-manifest` workflow is:

- pull-request/push/dispatch triggered for the ReleaseManifest family;
- read-only;
- no-network for the profile;
- deterministic;
- receipt-replay aware;
- explicit that PASS does not resolve references, verify artifact bytes or signatures, authenticate review, authorize promotion/release/publication, mutate lifecycle state, or permit public use.

This Atmosphere runbook does not alter that workflow or broaden its path triggers.

[Back to top](#top)

---

## 11. Finite outcomes and claim boundaries

Use the vocabulary owned by each layer. Do not coerce all states into one enum.

### 11.1 Validation

```text
PASS | FAIL | ERROR
```

### 11.2 Generic release readiness

Current generic checks use bounded states such as:

```text
BLOCKED
APPROVE_READY
```

`APPROVE_READY` means ready for an accountable next review step over the declared synthetic packet. It does not mean approved, released, deployed, or published.

### 11.3 Atmosphere candidate coordination

Use the candidate lane's named holds where applicable:

- `HOLD_FOR_ARTIFACT`
- `HOLD_FOR_SOURCE_ADMISSION`
- `HOLD_FOR_RIGHTS`
- `HOLD_FOR_SOURCE_ROLE`
- `HOLD_FOR_EVIDENCE`
- `HOLD_FOR_TIME_SEMANTICS`
- `HOLD_FOR_FRESHNESS`
- `HOLD_FOR_UNITS`
- `HOLD_FOR_KNOWLEDGE_CHARACTER`
- `HOLD_FOR_CAVEATS`
- `HOLD_FOR_POLICY`
- `HOLD_FOR_VALIDATION`
- `HOLD_FOR_REVIEW`
- `HOLD_FOR_RELEASE_TOPOLOGY`
- `HOLD_FOR_CORRECTION_PATH`
- `HOLD_FOR_ROLLBACK`

These are coordination states, not public response outcomes.

### 11.4 Governed outward response

```text
ANSWER | ABSTAIN | DENY | ERROR
```

An outward `ANSWER` requires released evidence and policy appropriate to the request. A release-readiness PASS does not produce an outward answer.

### 11.5 Truth labels

Continue to label claims independently:

- `CONFIRMED`
- `PROPOSED`
- `UNKNOWN`
- `NEEDS VERIFICATION`

Refinements such as `CONFLICTED`, `STALE`, `SUPERSEDED`, or `HOLD` do not replace the truth label.

### 11.6 Claim template

Every result statement should use this form:

```text
At <exact revision>, <named check> returned <finite outcome>
for <exact subject/profile>. This proves <bounded conclusion>.
It does not prove <named unresolved states>.
```

[Back to top](#top)

---

## 12. Accountable review handoff packet

A review handoff should contain only public-safe metadata and resolvable pointers.

### 12.1 Required identity

| Field | Requirement |
|---|---|
| Task/review ID | Stable identifier |
| Repository | Exact repository |
| Base/head | Exact immutable SHAs |
| Candidate | Exact path and candidate ID |
| Candidate digest | Immutable content identity |
| Requested transition | Named source and destination states |
| Audience/environment | Exact intended scope |
| Non-goals | Explicitly bounded |

### 12.2 Required support pointers

- SourceDescriptor refs and admission decisions.
- EvidenceRef/EvidenceBundle refs.
- ValidationReport refs and exact commands/results.
- PolicyDecision refs, evaluator/bundle identity, reasons, and obligations.
- ReviewRecord refs and authority records.
- Candidate ReleaseManifest path, digest, and profile.
- Artifact refs, media types, roles, and digests.
- Catalog, proof, receipt, and attestation refs.
- Freshness/stale-state profile and time window.
- Rights, sensitivity, generalization, redaction, and transform receipts.
- Correction, withdrawal, supersession, and rollback refs.
- Proposed public carriers and affected consumer inventory.
- Deployment/alias/cache/read-back plan.
- Remaining `HOLD`, `UNKNOWN`, `CONFLICTED`, and `NEEDS VERIFICATION` items.

### 12.3 Required non-effects statement

The packet must state whether it did **not**:

- fetch a source;
- admit a source;
- access restricted payloads;
- create evidence;
- evaluate live policy;
- authenticate review;
- assemble/persist a release;
- sign;
- mutate lifecycle state;
- deploy;
- publish;
- issue advice or alerts.

### 12.4 Public-safe reason handling

Use category-level reason codes. Do not include:

- credentials;
- private endpoints;
- restricted station details;
- exploitable location joins;
- internal deliberation;
- sensitive source payloads;
- prompts or hidden reasoning;
- operational secrets.

[Back to top](#top)

---

## 13. Rights, sensitivity, time, and public safety

### 13.1 Rights

Verify rights for the exact source, version, artifact type, audience, and use. Distinguish:

- access;
- storage;
- transformation;
- redistribution;
- public display;
- attribution;
- commercial use;
- model use;
- embargo;
- correction/withdrawal obligations.

Unknown rights produce `HOLD` or `DENY`; they do not default to public.

### 13.2 Station and location sensitivity

Review direct and reverse-inference exposure through:

- coordinates and geometry;
- IDs and labels;
- tile boundaries;
- search filters;
- parcel/infrastructure joins;
- timestamps;
- exports;
- graph edges;
- cache keys;
- screenshots;
- errors;
- model explanations.

Apply approved generalization or redaction before artifact assembly. Record the transform and reason.

### 13.3 Freshness and stale state

For current-sensitive products, bind:

- cadence;
- observation/valid/model-run times;
- issue and expiry times;
- retrieval time;
- release/effective time;
- stale threshold/profile;
- fallback or abstention behavior;
- correction and supersession lineage.

Use the [Stale-State Runbook](./STALE_STATE_RUNBOOK.md) when support may no longer be current. Stale is not automatically wrong; a substantive defect uses the correction path.

### 13.4 Low-cost sensors and derived products

Public release requires the applicable:

- correction method/version;
- calibration or colocation support;
- humidity or regime limitations;
- confidence/quality state;
- caveats;
- provenance;
- evidence;
- time validity;
- non-regulatory label.

### 13.5 Models, forecasts, AOD, and fusion

Public carriers must identify:

- model/sensor/product identity;
- run or acquisition time;
- valid time;
- resolution and spatial support;
- method;
- uncertainty;
- source roles;
- distinction from observations;
- citation and evidence support.

### 13.6 Advisory and life-safety boundary

Atmosphere may expose public-safe advisory **context** only when:

- the official issuer is identified;
- the official source is linked through governed public metadata;
- issue/valid/expiry/status are preserved;
- KFM does not rewrite the instruction as its own;
- the carrier states that KFM is not the issuing authority;
- current-sensitive use can abstain or redirect when verification is insufficient.

[Back to top](#top)

---

## 14. Hosted CI and exact-head evidence

### 14.1 Before citing a hosted result

Verify:

- workflow name and run ID;
- event;
- exact head SHA;
- job and step;
- status and conclusion;
- path trigger relevance;
- logs or summary;
- whether the result is current after base/head drift.

### 14.2 Status classification

Use these states explicitly:

| Classification | Meaning |
|---|---|
| Success | Completed successfully at the cited head |
| Expected hold/skip | Deliberately bounded non-execution |
| Pending/queued | No conclusion yet |
| Canceled | No valid success conclusion |
| Introduced failure | Caused by changed paths/behavior with evidence |
| Inherited failure | Reproduced from base or unrelated shared baseline with evidence |
| Unrelated failure | Outside the changed scope and not caused by the diff |
| Not run | Workflow did not execute for the head/event |

Do not call a failure inherited merely because the PR is documentation-only. Compare exact base/head evidence when classification matters.

### 14.3 Current workflow threat boundary

The inspected release and Atmosphere workflows use read-only repository permissions and do not contain release, deployment, signing, or publication credentials for their current fixture/readiness checks.

A future operational release workflow requires a separate security review covering:

- untrusted PR events;
- `pull_request_target` or chained privileged events;
- secrets and OIDC;
- environment protection;
- artifact provenance;
- command injection;
- path traversal;
- symlink behavior;
- network egress;
- least privilege;
- dual control;
- audit retention;
- rollback and incident response.

### 14.4 CI is not authority

Hosted CI can prove that defined checks ran. It cannot by itself:

- authenticate source authority;
- resolve rights or cultural/sensitivity obligations;
- prove evidence truth;
- establish independent review;
- approve release;
- deploy;
- publish;
- make KFM an official issuer.

[Back to top](#top)

---

## 15. Correction, withdrawal, rollback, and read-back

### 15.1 Correction

Use the [Correction Runbook](./CORRECTION_RUNBOOK.md) when an already released Atmosphere claim, artifact, label, time scope, source role, unit, caveat, or evidence binding is materially wrong.

A correction must preserve:

- prior release identity;
- corrected release identity;
- reason;
- affected claims/carriers;
- evidence and validation deltas;
- public notice;
- invalidation scope;
- supersession lineage;
- rollback support.

Do not silently overwrite the prior record.

### 15.2 Stale state

Use the [Stale-State Runbook](./STALE_STATE_RUNBOOK.md) when support has aged beyond a declared condition but is not necessarily substantively wrong.

Do not use “stale” to avoid a correction.

### 15.3 Withdrawal

Use withdrawal when public use must stop and no immediately approved replacement is available. Preserve the reason, affected carrier inventory, notice, lineage, and public read-back.

### 15.4 Rollback

A rollback requires:

- affected immutable release identity;
- prior safe target;
- verified target digests/manifests;
- accountable authority;
- current policy/review;
- public-carrier and cache invalidation plan;
- correction/withdrawal relationship;
- applied-transition receipt;
- read-back.

The current Atmosphere rollback JSON is a placeholder. It is not an operational card or rollback target.

### 15.5 Read-back

Correction, withdrawal, or rollback is not complete until every in-scope public carrier is checked, including:

- governed API;
- map/layers;
- tiles;
- search;
- graph;
- exports;
- AI/Focus Mode;
- caches/CDN;
- dashboards;
- documentation.

A write to one store does not prove propagation.

[Back to top](#top)

---

## 16. Anti-patterns

Do not:

- create a candidate solely to satisfy a workflow assertion;
- treat the candidate README as a candidate dossier;
- treat the PM2.5 placeholder `evidence_bundle.json` as evidence;
- treat the proposed Atmosphere rollback JSON as an executed RollbackCard;
- validate an id-only legacy manifest and call it release-complete;
- change strict fixture governance flags to `true`;
- bind public clients to a mutable `latest` path;
- combine source, evidence, receipt, proof, policy, review, manifest, release, and published carrier into one JSON object;
- make a pipeline or watcher a publisher;
- use a green fixture workflow as policy or review approval;
- use CODEOWNERS as independent release authority;
- store payloads in `release/` or release decisions in `data/published/`;
- expose RAW, WORK, QUARANTINE, candidate, restricted, or direct-model data to public clients;
- publish AQI as concentration, AOD as PM2.5, model as observation, or low-cost output as regulatory truth;
- hide uncertainty, freshness, caveats, correction, or official-source status;
- copy agency instructions into KFM as though KFM issued them;
- issue public health, regulatory, emergency, or life-safety instructions;
- silently correct, overwrite, rebind, or delete release history;
- mark a pull request ready, merge, release, deploy, or publish merely because this runbook is complete.

[Back to top](#top)

---

## 17. Current holds and open verification

| Item | Current status | Evidence needed before closure |
|---|---|---|
| Active Atmosphere candidate | `ABSENT / HOLD` | Immutable child dossier under accepted candidate lane |
| Atmosphere ReleaseManifest | `ABSENT / HOLD` | Accepted profile plus candidate-specific manifest and refs |
| Atmosphere published payload | `ABSENT / UNKNOWN` | Release decision, applied transition, carrier digest, public read-back |
| Source admission | `UNKNOWN / HOLD` | Accepted SourceDescriptors, rights, activation decisions, receipts |
| Evidence/proof closure | `PLACEHOLDER / HOLD` | Accepted producer/resolver, real EvidenceBundles, validation and limitations |
| Atmosphere policy | `PROPOSED SCAFFOLDS / HOLD` | Accepted package, entry point, tests, bundle, selector, evaluator, obligations |
| Review authority | `UNKNOWN / HOLD` | Authenticated responsibility assignments, scope, intervals, separation |
| Release authority | `UNKNOWN / HOLD` | Accepted authority record and environment-scoped decision profile |
| ReleaseManifest legacy branch | `COMPATIBILITY / CONFLICTED` | Migration/deprecation decision and consumer inventory |
| Strict ReleaseManifest branch | `FIXTURE_ONLY / HOLD` | Production profile, ref/byte/signature verification, policy/review integration |
| Domain release dry run | `WORKFLOW_HOLD` | Candidate contract, domain command, no-public-write proof, review |
| Artifact assembly | `PROPOSED / NEEDS VERIFICATION` | Executable pipeline, fixtures, tests, receipts, release wiring |
| Signer custody/attestations | `UNKNOWN / HOLD` | Approved identities, keyless/key custody, verification, rotation, rollback |
| Correction propagation | `PARTIAL / CONFLICTED` | Canonical lane, worker, policy, carrier inventory, read-back |
| Operational rollback | `HOLD` | Valid card, prior target, executor, invalidation, rehearsal, authority |
| Stale-state propagation | `FIXTURE_FIRST / LIVE HOLD` | Active freshness policy, connector/source cadence, carrier propagation |
| Review lane topology | `DRAFT / NEEDS VERIFICATION` | Parent contract, schemas, accepted record format, authority |
| Release storage/topology drift | `CONFLICTED` | Current release-root decision for duplicate/singular/domain-first lanes |
| Public API/map/search/graph/export/AI parity | `UNKNOWN / HOLD` | Governed exact-release integration and negative leakage tests |
| Deployment/monitoring | `UNKNOWN` | Environment, executor, logs, metrics, alerts, SLOs, rollback exercise |
| Official-source current parity | `UNKNOWN` | Source-specific admitted process and current read-back without KFM authority inflation |
| Independent review capacity | `UNKNOWN / HOLD` | Verified reviewer availability and enforcement |
| First governed Atmosphere release | `NOT ESTABLISHED` | Full end-to-end evidence from candidate through public read-back |

Do not close these items by editing prose. Each requires evidence from its owning surface and, where applicable, a governed decision.

[Back to top](#top)

---

## 18. Maintenance, correction, and document rollback

### 18.1 Review triggers

Update this runbook when any of the following changes materially:

- an Atmosphere candidate dossier appears;
- a ReleaseManifest profile is accepted, deprecated, or migrated;
- the candidate, manifest, review, correction, withdrawal, or rollback topology changes;
- an Atmosphere policy bundle/evaluator becomes active;
- proof production or EvidenceBundle resolution graduates;
- a domain-specific release-dry-run command is accepted;
- artifact assembly becomes executable;
- signer custody or attestation policy is established;
- an operational release executor appears;
- a governed public Atmosphere carrier is deployed;
- correction, withdrawal, stale-state, rollback, alias, or cache behavior changes;
- an actual release incident reveals missing procedure;
- Directory Rules, ADRs, CODEOWNERS routing, or stewardship assignments change;
- public API, map, tile, search, graph, export, dashboard, or AI surfaces change.

### 18.2 Documentation validation

For a change to this runbook, verify:

- one `KFM_META_BLOCK_V2`;
- one H1;
- stable anchors and internal navigation;
- balanced fenced blocks;
- valid relative links;
- UTF-8, LF, and final newline;
- current exact-revision evidence;
- no invented owners, candidates, sources, decisions, routes, or deployments;
- no sensitive/secret details;
- no release or public-state mutation;
- explicit rollback.

### 18.3 Rollback of this document change

This update is documentation-only.

- **Before merge:** close the draft pull request and abandon the feature branch.
- **After merge:** revert the implementation/merge commit through a reviewed pull request or apply a smaller forward correction.
- **Exact preimage:** blob `1a3ac56d5108197f57716f84a6db45370320a0f4` restores the prior scaffold.
- **Non-effect:** reverting this runbook cannot reverse a source, evidence, policy, review, release, deployment, publication, correction, withdrawal, or rollback state.

Do not restore the scaffold merely to hide evidence that the operational release path is held. Correct the substantive document while preserving the current truth posture.

[Back to top](#top)

---

## Appendix A — Operator checklist

### Identity and overlap

- [ ] Repository and exact head SHA recorded.
- [ ] Candidate path and immutable digest recorded.
- [ ] Requested audience/environment and transition recorded.
- [ ] Active PRs and branches searched for overlap.
- [ ] Non-goals and terminal boundary explicit.

### Candidate and artifacts

- [ ] Child candidate dossier exists.
- [ ] Candidate is not a README, placeholder, example, or roadmap row.
- [ ] Artifact refs, roles, media types, and digests are immutable.
- [ ] No floating `latest` refs.
- [ ] Candidate and artifact inventories agree.

### Source, evidence, meaning, and time

- [ ] SourceDescriptors admitted for exact use.
- [ ] Rights and attribution current.
- [ ] EvidenceRefs resolve to EvidenceBundles.
- [ ] Source roles and knowledge characters preserved.
- [ ] AQI/concentration, AOD/PM2.5, model/observation distinctions pass.
- [ ] Units, averaging periods, CRS, spatial scope, and uncertainty pass.
- [ ] Time kinds and freshness/stale rules pass.
- [ ] Official-source redirect and non-authority language present.

### Validation, policy, and review

- [ ] Exact affected Atmosphere profiles run.
- [ ] Positive and negative fixtures have expected polarity.
- [ ] ReleaseManifest fixture tests interpreted within scope.
- [ ] Generic release dry run interpreted within scope.
- [ ] Accepted policy evaluator, bundle, result, and obligations resolve.
- [ ] Reviewer identity, authority, scope, interval, and separation resolve.
- [ ] No pending/skipped/canceled job is presented as success.

### Release safety

- [ ] Accepted ReleaseManifest profile selected.
- [ ] Legacy compatibility is not treated as complete.
- [ ] Correction, withdrawal, stale-state, and rollback support resolve.
- [ ] Signatures/attestations and custody verified where required.
- [ ] Executor is least-privilege and environment-protected.
- [ ] No untrusted PR code receives release credentials.
- [ ] Public read-back plan covers all carriers.
- [ ] KFM does not become an alert, medical, regulatory, or life-safety authority.

### Handoff

- [ ] Every claim uses a truth label where material.
- [ ] Every command/result is tied to an exact subject and head.
- [ ] Every remaining hold is named.
- [ ] Non-effects are explicit.
- [ ] Rollback path is explicit.
- [ ] Review, release, deployment, and publication remain separate.

[Back to top](#top)

---

## Appendix B — Current command and surface matrix

| Purpose | Current entry point | Current evidence boundary |
|---|---|---|
| Atmosphere bounded validation | See [`VALIDATION_RUNBOOK.md`](./VALIDATION_RUNBOOK.md) | Named synthetic profiles only |
| ReleaseManifest unit tests | `python -m unittest tests.validators.test_validate_release_manifest -v` | Fixture-only validator behavior |
| ReleaseManifest fixture replay | `python tools/validators/release/validate_release_manifest.py --fixtures` | 21 synthetic cases; no authority |
| Generic release readiness | `make release-dry-run` | Synthetic publication denials; no writes |
| Generic A–G readiness | `make publish-check` | Synthetic `APPROVE_READY`; no transition |
| Rollback-card readiness | Release dry-run workflow job | Candidate shape/rehearsal only |
| Atmosphere proof readiness | `domain-atmosphere` held job | Recognizes exact placeholder and preserves hold |
| Atmosphere release dry run | `domain-atmosphere` held job | No accepted domain command or candidate contract |
| Operational Atmosphere release | None established | `HOLD / UNKNOWN` |
| Public read-back | None established | `UNKNOWN` |

### Relevant current surfaces

- [`release/README.md`](../../../release/README.md)
- [`contracts/release/release_manifest.md`](../../../contracts/release/release_manifest.md)
- [`schemas/contracts/v1/release/release_manifest.schema.json`](../../../schemas/contracts/v1/release/release_manifest.schema.json)
- [`tools/validators/release/validate_release_manifest.py`](../../../tools/validators/release/validate_release_manifest.py)
- [`release/candidates/atmosphere/README.md`](../../../release/candidates/atmosphere/README.md)
- [`data/published/atmosphere/README.md`](../../../data/published/atmosphere/README.md)
- [`policy/domains/atmosphere/README.md`](../../../policy/domains/atmosphere/README.md)
- [`pipelines/domains/atmosphere/publish/README.md`](../../../pipelines/domains/atmosphere/publish/README.md)
- [`.github/workflows/release-manifest.yml`](../../../.github/workflows/release-manifest.yml)
- [`.github/workflows/release-dry-run.yml`](../../../.github/workflows/release-dry-run.yml)
- [`.github/workflows/domain-atmosphere.yml`](../../../.github/workflows/domain-atmosphere.yml)

[Back to top](#top)
