<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/flora/promotion-runbook
title: Flora Promotion Runbook
type: runbook; operational-procedure; domain-lane; non-authoritative
version: v1.0.0
prior_version: v0.1
status: draft; repository-grounded; bounded-public-safe-fixture-validator-present; flora-candidate-absent; flora-proof-held; policy-inactive; release-dry-run-held; sensitive-location-deny-by-default; non-publisher
owners:
  - "@bartytime4life — verified GitHub review route only"
  - "NEEDS VERIFICATION — accountable Flora, taxonomy, source, rights, sensitivity, geoprivacy, stewardship, evidence, policy, validation, public-surface, release, correction, rollback, operations, and independent-review assignments"
created: 2026-05-13
updated: 2026-08-24
policy_label: restricted-review; flora; promotion-readiness; rare-plants; cultural-knowledge; fail-closed; no-release-authority; no-publication-authority
current_path: docs/runbooks/flora/PROMOTION_RUNBOOK.md
owning_root: docs/
responsibility: >-
  Provide the repository-grounded human procedure for evaluating Flora
  promotion readiness and preparing an accountable, public-safe review handoff
  without granting source admission, botanical or taxonomic authority, rights or
  sensitivity clearance, policy authority, review authority, lifecycle-transition
  authority, release authority, deployment authority, or publication authority.
truth_posture: cite-or-abstain
truth_labels: [CONFIRMED, PROPOSED, UNKNOWN, NEEDS VERIFICATION, CONFLICTED, HOLD]
authority_class: explanatory operational documentation
canonical_relationship: same-path update; no new or parallel authority
path_posture: PLACE
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  content_inspection_commit: 35bb62209569f63af78c6fefe4c85015d3bdceb1
  prior_blob: 89a77d18edc56b9eb9901f5e82ea6eeca4c0c52c
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  promotion_sequence_adr_blob: 51cedfdf98b92f1a9af492ce3a1cde231eed9308
  source_authority_register_blob: 32729857bc8eb5001acb37b8ee8e60bcb6e0dc50
  flora_workflow_blob: 3fe6b1ba8150960692b6b2fc764c6aa31d09565c
  flora_fixture_validator_blob: 17933f997f7cb1219e3057ea74bf2c077dc45386
  flora_fixture_test_blob: 18d15781b78487de4c786c5ee38254f3a48e49e3
  flora_candidate_readme_blob: 15a08f9fb2cdd33041d3a3f3e3c844f26a7a0998
  flora_domain_policy_blob: 247fc146131f4e6598af9fd939cf087d92523ed6
  flora_sensitivity_policy_blob: 4c65abec24135f7e4467fd108e163cdce594d5f9
  flora_proof_readme_blob: 130effccfd6e14f2660de04c3cc30d839503ef8a
  published_flora_readme_blob: 1368127a0ddc2ca2766eec23923c48de26a678e1
  promotion_gate_readme_blob: e729df0cc007e8cf0d9811afc25ec1f5ffbdffdd
  promotion_policy_readme_blob: 79287df1d828010d716ed43d2e24d6dbd610305b
  promotion_decision_contract_blob: 42295bfc83a621cf125d33aa821912b426f70bd2
  promotion_receipt_contract_blob: ed432f8e3e02d170589c9e04d78087a69346909d
  release_manifest_contract_blob: ce7dc89ff447d76d974afdd802b85a38538d8f48
  rollback_card_contract_blob: c6d3c35c56b064e04c3a2532f4709d938d7b0c1a
  release_review_readme_blob: bf3058a5af8fc85aa04a25a36ed03541cd9eb657
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
inspection_boundary: >-
  Current-session GitHub reads of the target, accepted Directory Rules decision,
  proposed promotion-sequence ADR, Flora domain, source, proof, policy,
  sensitivity, candidate, published-carrier, validation, workflow, review,
  decision, receipt, manifest, correction, and rollback boundaries. Google Drive
  Flora architecture material was inspected as planning lineage only. No live
  Flora source, protected location payload, restricted botanical knowledge,
  credential, production policy evaluator, evidence resolver, release service,
  deployed public surface, or lifecycle transition was exercised.
related:
  - ../README.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../adr/ADR-0018-promotion-gate-sequence.md
  - ../../doctrine/directory-rules.md
  - ../../domains/flora/README.md
  - ../../domains/flora/DATA_LIFECYCLE.md
  - ../../domains/flora/RELEASE_INDEX.md
  - ../../domains/flora/SENSITIVITY.md
  - ../../domains/flora/PUBLICATION_AND_ROLLBACK.md
  - ../../../control_plane/source_authority_register.yaml
  - ../../../data/registry/sources/flora/README.md
  - ../../../data/proofs/flora/README.md
  - ../../../data/published/flora/README.md
  - ../../../contracts/release/promotion_decision.md
  - ../../../contracts/release/promotion_receipt.md
  - ../../../contracts/release/release_manifest.md
  - ../../../contracts/release/rollback_card.md
  - ../../../policy/promotion/README.md
  - ../../../policy/domains/flora/README.md
  - ../../../policy/sensitivity/flora/README.md
  - ../../../tools/validators/promotion_gate/README.md
  - ../../../tools/validators/domains/flora/validate_public_safe_fixture.py
  - ../../../tests/domains/flora/test_flora_smoke.py
  - ../../../release/candidates/flora/README.md
  - ../../../release/reviews/README.md
  - ../../../.github/CODEOWNERS
  - ../../../.github/workflows/domain-flora.yml
  - ./NO_NETWORK_TEST_RUNBOOK.md
  - ./SOURCE_REFRESH_RUNBOOK.md
  - ./ROLLBACK_RUNBOOK.md
tags: [kfm, flora, runbook, promotion, readiness, taxonomy, occurrences, specimens, rare-plants, geoprivacy, cultural-knowledge, evidence, policy, review, release, correction, rollback, fail-closed]
notes:
  - "v1.0.0 replaces proposal-era no-mounted-repository assumptions, guessed paths, speculative policy execution, and implied release automation with current repository evidence and bounded procedures."
  - "The Google Drive Flora blueprint remains useful design lineage for source-role, object-family, sensitivity, and lifecycle distinctions; it is not current repository implementation evidence."
  - "The shared A-G promotion-gate validator is executable, deterministic, no-network, read-only, and non-publishing. PASS means APPROVE_READY for accountable review only."
  - "The executable Flora slice validates only synthetic, fixture-only public-safe candidates that are explicitly not released and not promotion eligible."
  - "No child Flora candidate dossier, accepted Flora proof producer, active Flora policy evaluator, accepted Flora release dry-run command, accountable Flora ReviewRecord, Flora PromotionDecision, Flora ReleaseManifest, applied transition, or released Flora carrier was established by the bounded inspection."
  - "This document changes no candidate, source, data, contract, schema, policy, fixture, validator, workflow, evidence object, receipt, proof, review, release record, deployment, lifecycle state, or public surface."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Flora Promotion Runbook

> **Evaluate whether one specifically identified Flora candidate has enough governed, public-safe support for accountable release review. Never translate documentation, a synthetic fixture pass, a green workflow, a schema-valid packet, or an `APPROVE_READY` result into promotion, release, deployment, or publication.**

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#current-repository-posture)
[![Flora fixture validator: present](https://img.shields.io/badge/Flora%20fixture%20validator-present-1f883d?style=flat-square)](#current-executable-validation)
[![Flora candidate: absent](https://img.shields.io/badge/Flora%20candidate-NOT__ESTABLISHED-critical?style=flat-square)](#current-repository-posture)
[![Promotion policy: inactive](https://img.shields.io/badge/promotion%20policy-inactive-d4a72c?style=flat-square)](#current-repository-posture)
[![Sensitive locations: deny by default](https://img.shields.io/badge/sensitive%20locations-deny__by__default-b42318?style=flat-square)](#flora-specific-gates)
[![Publisher: no](https://img.shields.io/badge/publisher-no-6e7781?style=flat-square)](#authority-boundary-and-handoff)

> [!IMPORTANT]
> **Promotion is a governed state transition, not a file move, commit, pull request, merge, workflow result, badge, fixture, candidate dossier, receipt-shaped file, manifest-shaped file, deployment, alias update, map-layer toggle, or generated summary.** Lifecycle and public state may change only after the owning source, evidence, rights, sensitivity, policy, review, decision, release, correction, and rollback controls close.

> [!CAUTION]
> **Current Flora promotion is `HOLD`.** The repository has one bounded synthetic public-safe Flora fixture suite and a separate generic A-G readiness validator. The Flora candidate lane has no verified child dossier; the Flora proof producer and Flora release dry run remain explicit workflow holds; Flora domain policy is inactive; Flora sensitivity policy remains a scaffold; and no accountable Flora review, promotion decision, release manifest, applied transition, or released public carrier was established.

> [!WARNING]
> **Exact or reverse-engineerable plant locations and protected botanical knowledge fail closed.** Do not expose rare or protected occurrences, specimen localities, culturally sensitive plant knowledge, private-land joins, collection or access clues, steward-controlled records, withheld precision, or geoprivacy transform parameters in a candidate packet, pull request, log, screenshot, map, export, graph, cache, or AI answer.

**Quick navigation:** [Purpose](#purpose) · [Current posture](#current-repository-posture) · [Placement](#directory-rules-basis) · [Scope](#scope-and-non-goals) · [Roles](#roles-and-separation-of-duties) · [Lifecycle](#lifecycle-and-object-family-boundaries) · [Preflight](#preflight-and-stop-conditions) · [Procedure](#promotion-readiness-procedure) · [Flora gates](#flora-specific-gates) · [Validation](#current-executable-validation) · [Packet](#candidate-review-packet) · [Outcomes](#finite-outcomes-and-current-holds) · [Authority](#authority-boundary-and-handoff) · [Recovery](#correction-withdrawal-and-rollback) · [Audit](#audit-and-join-keys) · [Checklist](#operator-checklist) · [Open work](#open-verification-register) · [Evidence](#evidence-basis) · [Document rollback](#document-change-rollback)

---

<a id="purpose"></a>

## Purpose

Use this runbook to assess one bounded Flora candidate against the support required for a possible transition from governed `CATALOG` or `TRIPLET` state toward a public-safe released carrier.

The KFM lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

This runbook concentrates on the final readiness boundary. Earlier lifecycle stages remain prerequisites owned by their source, data, evidence, validation, and policy lanes. The operator's output is a public-safe readiness, hold, abstention, denial, or error packet. Completing the procedure cannot create missing authority.

When this runbook conflicts with accepted ADRs, adopted Directory Rules, current contracts, schemas, policy, source-admission records, EvidenceBundles, review records, release decisions, correction records, rollback records, or runtime evidence, stop and record the conflict rather than selecting the convenient interpretation.

### What this runbook can establish

- which candidate and requested lifecycle boundary are being evaluated;
- which current repository checks apply;
- which required support objects are present, absent, stale, conflicted, or unresolved;
- which Flora-specific taxonomic, specimen, occurrence, source-role, rights, sensitivity, geoprivacy, temporal, spatial, uncertainty, and representation distinctions must remain visible;
- which finite readiness outcome applies at the current evidence level; and
- which separately accountable authority must receive the handoff.

### What this runbook cannot establish

- that a Flora source is admitted, active, authoritative, current, or rights-cleared;
- that a taxonomic identification, specimen, occurrence, range, vegetation class, phenology state, invasive status, restoration claim, or modeled surface is botanically true;
- that a public-safe transform is scientifically, ethically, legally, culturally, or operationally sufficient;
- that evidence is complete or authentic merely because a reference is present;
- that policy is accepted, active, or executing;
- that a reviewer is qualified, assigned, independent, or current;
- that a candidate exists because a directory or README exists;
- that a transition occurred because a receipt, decision, manifest, or workflow validates;
- that a map or export is safe because a style hides detail; or
- that release, deployment, promotion, or publication occurred.

[Back to top](#top)

---

<a id="current-repository-posture"></a>

## Current repository posture

The following conclusions are bounded to `main@35bb62209569f63af78c6fefe4c85015d3bdceb1`.

| Surface | Status | Safe conclusion |
|---|---|---|
| This runbook path | **CONFIRMED** | `docs/runbooks/flora/PROMOTION_RUNBOOK.md` is tracked. The prior v0.1 text was proposal-era and still claimed that no repository had been inspected. This revision is a same-path documentation modernization. |
| Directory governance | **CONFIRMED / accepted** | ADR-0029 adopts Directory Rules v2; `docs/runbooks/` owns human operational procedures. |
| Flora candidate lane | **CONFIRMED guidance / no child candidate** | `release/candidates/flora/` contains the parent README and no verified child candidate dossier. “A candidate is not a release.” |
| Flora fixture validation | **CONFIRMED / bounded** | `domain-flora` runs one deterministic, no-network synthetic public-safe fixture suite. Its valid fixture is explicitly not released and not promotion eligible. |
| Flora fixture matrix | **CONFIRMED / synthetic** | One valid fixture and six invalid fixtures exercise malformed candidates, missing public controls or references, role/taxonomy collapse, undeclared transform material, and unsafe location or sensitivity state. |
| Flora proof producer | **CONFIRMED / HOLD** | The domain workflow records no accepted Flora proof producer or deterministic proof command. |
| Flora release dry run | **CONFIRMED / HOLD** | The domain workflow records no accepted Flora release dry-run command or candidate-manifest contract. |
| Generic promotion readiness | **CONFIRMED / bounded** | `tools/validators/promotion_gate/validate_promotion_gate.py` evaluates a declared `CATALOG` or `TRIPLET` to `PUBLISHED` packet through A-G gates with no network or writes. |
| Generic readiness result | **CONFIRMED / non-authoritative** | `PASS` maps to `APPROVE_READY` for accountable review only. It is not `APPROVE`, `PROMOTED`, `RELEASED`, or `PUBLISHED`. |
| Promotion sequence ADR | **CONFIRMED / proposed** | ADR-0018 remains proposed. The current executable gate names are implementation evidence, not an accepted universal sequence. |
| `PromotionDecision` family | **CONFIRMED / PROPOSED contract and shape** | The semantic contract and paired schema define `APPROVE`, `DENY`, or `ABSTAIN`. No Flora instance was established. |
| `PromotionReceipt` family | **CONFIRMED / PROPOSED fixture-first** | Contract, schema, validator, fixtures, tests, and read-only workflow exist. Internal consistency is not proof that a transition occurred. |
| `ReleaseManifest` family | **CONFIRMED / dual-profile candidate validation** | The contract and validator preserve legacy compatibility and a closed fixture-only strict branch. A strict `PASS` is not production release authority. |
| `RollbackCard` family | **CONFIRMED / fixture-first and non-executing** | Contract, schema, validator, fixtures, and tests can check candidate shape and local consistency. They do not execute rollback. |
| Promotion policy | **CONFIRMED / inactive** | `policy/promotion/` contains two no-op Rego stubs. No accepted bundle, evaluator binding, active gate-register entry, or governed consumer is established. |
| Flora domain policy | **CONFIRMED / scaffold corpus and inactive** | The lane contains policy-shaped source, but no accepted Flora entrypoint, bundle, evaluator, native policy test suite, decision normalization, or governed consumer was established. |
| Flora sensitivity policy | **CONFIRMED / scaffold** | `policy/sensitivity/flora/README.md` explicitly says `PROPOSED scaffold`; it is not active geoprivacy or sensitive-knowledge enforcement. |
| Source authority | **CONFIRMED / empty projection** | The central source-authority register is `PROPOSED`, projection-only, `implementation_status: ABSENT`, and has `entries: []`. |
| Flora source registry | **CONFIRMED draft / topology unresolved** | Source guidance exists, but subtype-first and domain-first source-registry lanes remain unresolved. Do not duplicate or infer admitted source records. |
| Flora proof support | **CONFIRMED draft / production hold** | Shared EvidenceBundle surfaces exist, but no accepted Flora proof packet, producer, resolver binding, release linkage, or public-safe proof inventory was established. |
| Published Flora lane | **CONFIRMED guidance / emitted release unverified** | `data/published/flora/README.md` defines a downstream carrier boundary. It does not establish an emitted release or authorize public use. |
| Release review lane | **CONFIRMED guidance** | `release/reviews/` describes review records and a fixture-only Gate G validator. No parent-level accountable Flora review was established. |
| CODEOWNERS | **CONFIRMED routing only** | `@bartytime4life` is the verified GitHub review route. CODEOWNERS is not a stewardship assignment, independent approval, or release authority. |
| Google Drive Flora blueprint | **CONFIRMED source lineage / not repo proof** | The blueprint contributes object-family, source-role, lifecycle, and sensitivity design pressure, but explicitly records that it was produced without a mounted repository. |

### Current bounded outcome

```text
HOLD_FOR_CANDIDATE
+ HOLD_FOR_SOURCE_ADMISSION
+ HOLD_FOR_EVIDENCE
+ HOLD_FOR_POLICY
+ HOLD_FOR_SENSITIVITY
+ HOLD_FOR_REVIEW
+ HOLD_FOR_RELEASE_PATH
+ HOLD_FOR_ROLLBACK
```

This is a readiness statement, not a change to any candidate or lifecycle state.

[Back to top](#top)

---

<a id="directory-rules-basis"></a>

## Directory Rules basis

**Placement outcome: `PLACE` at the existing path.**

Accepted ADR-0029 adopts the exact Directory Rules v2 bytes at `docs/doctrine/directory-rules.md`. Those rules treat a path as an authority claim and place artifacts by their owning responsibility.

| Question | Result |
|---|---|
| What is this artifact? | Human-readable operational procedure. |
| Owning responsibility root | `docs/`. |
| Operational specialization | `docs/runbooks/`. |
| Domain lane | `flora/`. |
| Existing canonical-looking path | `docs/runbooks/flora/PROMOTION_RUNBOOK.md`. |
| Structural effect | None; same-path update only. |
| Parallel authority created | None. |
| Contract, schema, policy, evidence, release, or published-data home created | None. |

The runbook may point to candidate, source, evidence, policy, validation, review, release, correction, and rollback surfaces. It must not absorb their authority or store their instances.

[Back to top](#top)

---

<a id="scope-and-non-goals"></a>

## Scope and non-goals

### In scope

This procedure applies to a specifically identified Flora candidate involving one or more of these families:

- plant taxon and taxon-concept records;
- taxonomic crosswalks and source-name mappings;
- specimen or herbarium records;
- plant occurrences and botanical surveys;
- rare, protected, culturally sensitive, or steward-controlled Flora records;
- vegetation communities and classes;
- invasive-plant records;
- phenology observations or derived condition products;
- range, distribution, suitability, or generalized public surfaces;
- habitat associations and governed cross-lane joins;
- restoration planting records; and
- released map, API, report, export, index, or summary carriers.

### Required distinctions

Never collapse:

- taxon identity into occurrence evidence;
- a specimen record into a current occurrence;
- an observation into a modeled range or suitability surface;
- a regulatory or conservation status into occurrence proof;
- an aggregator into the originating source role;
- an internal exact record into a generalized public derivative;
- a map style or hidden field into redaction;
- a validation receipt into an EvidenceBundle;
- a proof packet into a policy decision;
- a policy result into release approval;
- a review recommendation into a `PromotionDecision`;
- a `PromotionDecision` into a `ReleaseManifest`; or
- generated language into botanical evidence.

### Non-goals

This runbook does not:

- activate or retrieve a live source;
- access or reproduce restricted botanical material;
- resolve taxonomy on behalf of a qualified botanical authority;
- perform a geoprivacy, redaction, aggregation, or generalization transform;
- define sensitivity thresholds or reveal transform parameters;
- activate Rego or another policy engine;
- create or authenticate evidence, proof, review, decision, receipt, or release objects;
- mutate `RAW`, `WORK`, `QUARANTINE`, `PROCESSED`, `CATALOG`, `TRIPLET`, or `PUBLISHED`;
- write a public alias, tile set, API payload, cache, index, or deployment;
- approve, merge, release, deploy, promote, or publish.

[Back to top](#top)

---

<a id="roles-and-separation-of-duties"></a>

## Roles and separation of duties

All accountable assignments below are **NEEDS VERIFICATION**. `@bartytime4life` is the verified GitHub routing identity only.

| Role | Required responsibility | Must not substitute for |
|---|---|---|
| Candidate author or producer | Identify the candidate, immutable artifact set, intended lifecycle boundary, scope, and limitations. | Independent reviewer or release authority. |
| Flora domain steward | Confirm domain scope and object-family boundaries. | Taxonomic, rights, sensitivity, or release authority unless separately assigned. |
| Taxonomy reviewer | Evaluate taxon-concept identity, source-name crosswalks, uncertainty, and conflicts. | Occurrence truth or release approval. |
| Source steward | Confirm source descriptor, source role, admission state, cadence, and authority boundary. | Rights clearance, evidence closure, or botanical truth. |
| Rights reviewer | Confirm license, terms, attribution, redistribution, embargo, and permitted use. | Sensitivity or cultural authority. |
| Sensitivity and geoprivacy reviewer | Assess exact-location risk, join-induced disclosure, public derivative, and withheld-detail posture. | Source, rights, or release authority. |
| Stewardship or community authority | Review steward-controlled or culturally sensitive botanical knowledge where applicable. | Generic repository review routing. |
| Evidence reviewer | Confirm claim-scoped `EvidenceRef` to `EvidenceBundle` closure and limitations. | Policy or release decision. |
| Policy steward | Own accepted policy source, bundle identity, evaluation, result normalization, and obligations. | Candidate production or release authority. |
| Validation steward | Run bounded validators and preserve exact outputs and limitations. | Botanical truth, policy evaluation, or approval. |
| Public-surface reviewer | Inspect the actual proposed map, API, export, report, search, graph, cache, and AI surfaces for leakage. | Upstream transformation or policy. |
| Independent release reviewer | Confirm separation, support closure, scope, and recommendation. | Candidate author. |
| Release authority | Create the separately governed final decision and authorize the accepted release operation. | This runbook, CODEOWNERS, or CI. |
| Correction and rollback steward | Confirm correction, withdrawal, invalidation, restoration, and audit lineage. | Silent deletion or history rewrite. |
| Operations owner | Execute only a separately authorized transition and emit operational records. | Review or policy authority. |

### Separation rules

- The candidate author must not self-approve a material release.
- A GitHub review request is not a `StewardshipAssignment` or `ReviewRecord`.
- A source provider is not automatically the KFM release authority.
- A botanical expert is not automatically a rights, sensitivity, policy, or release authority.
- The operator running validators must not convert their output into approval.
- AI may summarize a public-safe packet, but it may not act as reviewer, steward, rights holder, policy authority, or release authority.
- When an accountable role is absent or its authority cannot be verified, use `HOLD` or `ABSTAIN`.

[Back to top](#top)

---

<a id="lifecycle-and-object-family-boundaries"></a>

## Lifecycle and object-family boundaries

### Lifecycle relationship

```text
SOURCE DISCOVERY
  -> SOURCE ADMISSION
  -> RAW
  -> WORK or QUARANTINE
  -> PROCESSED
  -> CATALOG / TRIPLET
  -> PROMOTION-READINESS EVALUATION
  -> ACCOUNTABLE REVIEW
  -> PROMOTION DECISION
  -> RELEASE MANIFEST AND AUTHORIZED OPERATION
  -> PUBLISHED PUBLIC-SAFE CARRIER
  -> CORRECTION / WITHDRAWAL / ROLLBACK / RECOMPILE
```

This runbook begins only when a candidate claims `CATALOG` or `TRIPLET` readiness for a possible public release. If earlier lifecycle support is absent, return the candidate to the owning lane.

### Object-family separation

| Object or surface | Owning responsibility | What it proves | What it does not prove |
|---|---|---|---|
| `SourceDescriptor` or source-admission record | Source registry and source governance | Reviewed source identity, role, rights/sensitivity posture, and admitted use when actually resolved. | Botanical claim truth or release. |
| Flora candidate dossier | `release/candidates/flora/` | Candidate identity, scope, pointers, blockers, and review state. | Release or public safety. |
| `EvidenceRef` / `EvidenceBundle` | Evidence and proof lanes | Claim-scoped support and limitations when resolved. | Policy approval or release. |
| Validation result | Validator, test, and receipt lanes | What a named executable checked over named bytes. | Botanical truth, reviewer authority, or release. |
| Policy result | Accepted policy source, evaluator, and decision record | Admissibility for a named operation under supplied context. | Evidence truth or release execution. |
| `ReviewRecord` | Release review lane | Accountable review when identity, authority, scope, and validity resolve. | Final decision or publication. |
| `PromotionDecision` | Release-governance lane | `APPROVE`, `DENY`, or `ABSTAIN` for a named transition when authentic and authorized. | Manifest emission or public serving by itself. |
| `PromotionReceipt` | Release/data receipt lane | Declared attempt, gate outcomes, integrity binding, and whether a transition was reported as applied. | Authentic transition or release by shape alone. |
| `ReleaseManifest` | Release-governance lane | Release inventory and governed support binding when approved and persisted. | Artifact storage or public availability by itself. |
| `RollbackCard` | Release-governance lane | Candidate recovery plan, target, invalidation scope, and support. | Rollback execution. |
| Published Flora carrier | `data/published/flora/` or accepted artifact store | Released public-safe bytes only when linked to a valid release state. | Canonical source truth or unrestricted reuse. |
| Map, API, graph, search, export, dashboard, or AI answer | Governed public delivery | Interpretation of released public-safe carriers. | Sovereign truth or hidden authority. |

[Back to top](#top)

---

<a id="preflight-and-stop-conditions"></a>

## Preflight and stop conditions

Perform preflight before assembling or evaluating a candidate packet.

### 1. Freeze repository and task identity

Record:

- repository and exact base commit;
- target candidate ID and candidate version;
- candidate path and immutable artifact digest set;
- requested lifecycle boundary;
- current target runbook blob;
- relevant contract, schema, policy, validator, workflow, and release-object versions;
- open branches or pull requests touching the same candidate or authority surface.

Stop on unresolved overlap, stale target bytes, or conflicting authority.

### 2. Confirm a candidate actually exists

A parent README, proposed thin slice, processed path, catalog entry, test fixture, workflow, or planning document is not a candidate.

Required minimum:

- child candidate dossier under the accepted candidate lane;
- stable candidate ID and version;
- immutable artifact pointer or digest set;
- explicit `CATALOG` or `TRIPLET` source state;
- explicit proposed audience and public carrier;
- no restricted payload in the public-review packet.

**Current result:** no verified child Flora candidate exists. Stop with `HOLD_FOR_CANDIDATE`.

### 3. Confirm source admission and role

For every contributing source, resolve:

- source descriptor identity;
- admission or activation state;
- source role and authority boundary;
- rights, terms, attribution, embargo, and redistribution posture;
- sensitivity and precision floor;
- cadence, source-head, retrieval, and stale-state posture;
- correction, supersession, and withdrawal references.

**Current central projection:** empty and non-implementing. Do not infer admission from a connector, URL, bibliography, source README, or available download.

### 4. Confirm botanical and taxonomic scope

Resolve:

- accepted or bounded taxon-concept reference;
- source-native name and identifier;
- synonym or crosswalk reference;
- identification method and reviewer;
- unresolved or conflicting taxonomy;
- observation, specimen, model, classification, regulatory, aggregate, contextual, or synthetic source role.

Unresolved taxonomy does not automatically require deletion, but it blocks any claim that depends on a resolved taxon concept.

### 5. Confirm evidence closure

Every consequential candidate claim must have resolvable support. Confirm:

- claim IDs and exact scope;
- `EvidenceRef` values;
- `EvidenceBundle` identity, version, digest, source roles, citations, limitations, and validity;
- citation-validation state;
- invalidation, correction, or supersession state;
- no evidence reference points to a fixture or planning artifact as real support.

Missing or unresolved support yields `HOLD_FOR_EVIDENCE` or `ABSTAIN`.

### 6. Confirm rights, sensitivity, and safe representation

Stop if the packet contains or permits inference of:

- exact or reverse-engineerable sensitive plant location;
- restricted specimen locality;
- private-land identity or access route;
- culturally sensitive plant knowledge without verified authority to control;
- collection directions, habitat clues, or joins that defeat generalization;
- withheld precision or redaction parameters;
- unknown rights or prohibited redistribution;
- client-side hiding as the only protection.

The public candidate packet may contain public-safe reason codes and immutable references. It must not contain the restricted value.

### 7. Confirm active policy

Require an accepted policy profile, immutable bundle identity, evaluator, normalized result, obligations, evaluation time, and governed consumer.

**Current result:** promotion policy, Flora domain policy, and Flora sensitivity policy are not active. Stop with `HOLD_FOR_POLICY`; do not treat default Rego declarations or absence of a denial as permission.

### 8. Confirm accountable review and rollback

Require:

- candidate-specific reviewer assignments;
- identity and authority records;
- separation of duties;
- review validity interval and scope;
- correction and withdrawal paths;
- rollback target and invalidation scope;
- re-review triggers for source, taxonomy, rights, sensitivity, evidence, policy, or artifact changes.

Missing accountable authority yields `HOLD_FOR_REVIEW` or `ABSTAIN`.

[Back to top](#top)

---

<a id="promotion-readiness-procedure"></a>

## Promotion-readiness procedure

The procedure is read-only until a separately authorized release operation begins.

### Step 0 — Open an auditable evaluation record

Record the exact candidate, repository checkpoint, operator, evaluation time, requested transition, applicable profiles, and expected output location. Use public-safe identifiers only.

Do not copy candidate payloads, protected coordinates, restricted knowledge, tokens, credentials, or transform parameters into the evaluation record.

### Step 1 — Verify candidate identity and closure

Confirm:

- candidate ID, version, object family, and author;
- source lifecycle state is `CATALOG` or `TRIPLET`;
- proposed target is `PUBLISHED`;
- candidate and proposed manifest identities agree;
- artifact digests are complete, unique, and immutable;
- candidate packet declares the public carrier and audience;
- no mutable alias is used as the sole rollback or evidence anchor.

Failure: `HOLD_FOR_CANDIDATE`, `DENY`, or `ERROR`.

### Step 2 — Verify taxonomy, source role, and source admission

For every claim and artifact:

1. resolve the taxon concept and any source-name crosswalk;
2. retain source-native identifiers and uncertainty;
3. preserve whether support is observed, specimen-backed, aggregate, modeled, regulatory, administrative, contextual, or synthetic;
4. resolve source descriptor and admission state;
5. confirm rights, terms, cadence, source head, and authority boundary;
6. reject role upgrades caused by normalization, aggregation, mapping, or generated explanation.

Failure: `HOLD_FOR_TAXONOMY`, `HOLD_FOR_SOURCE_ADMISSION`, `HOLD_FOR_SOURCE_ROLE`, or `DENY`.

### Step 3 — Verify evidence and catalog support

Confirm that each release-visible claim resolves to:

- claim-scoped EvidenceBundle support;
- source references and source roles;
- citations and limitations;
- integrity and spec hashes;
- validation and transform receipts where applicable;
- STAC, DCAT, PROV, domain-catalog, or triplet references appropriate to the carrier;
- correction and invalidation lineage.

Do not count a catalog record, graph edge, tile, model output, or generated summary as evidence by itself.

Failure: `HOLD_FOR_EVIDENCE`, `HOLD_FOR_CATALOG`, or `ABSTAIN`.

### Step 4 — Verify rights, sensitivity, geoprivacy, and public surfaces

Evaluate both the upstream material and the actual proposed public representation.

Required checks include:

- rights and redistribution permission;
- sensitive taxon, specimen, habitat, or cultural-knowledge flags;
- exact and reverse-engineerable location risk;
- private-land and person/parcel joins;
- temporal, taxonomic, and spatial uncertainty;
- public-safe transform identity and review, without exposing transform secrets;
- map source data, tile payload, feature properties, API response, search index, export, graph, cache, screenshot, and AI context;
- ability to recover restricted detail by differencing, repeated queries, zooming, filters, metadata, or auxiliary joins.

A style filter, collapsed UI panel, or hidden field is not redaction.

Failure: `HOLD_FOR_RIGHTS`, `HOLD_FOR_SENSITIVITY`, `HOLD_FOR_STEWARDSHIP`, `HOLD_FOR_GEOPRIVACY`, `RESTRICT`, or `DENY`.

### Step 5 — Run the bounded Flora fixture proof

Run the repository-native deterministic synthetic suite:

```bash
python -m unittest discover \
  --start-directory tests/domains/flora \
  --pattern 'test_flora_smoke.py' \
  --verbose
```

This suite checks the frozen synthetic public-safe profile. It does not evaluate the real candidate and does not create a proof packet.

If the suite fails, classify the failure before changing the candidate or repository:

- introduced by the current change;
- inherited repository failure;
- fixture/profile drift;
- environment or runner error; or
- unresolved without logs.

Failure: `HOLD_FOR_VALIDATION` or `ERROR`.

### Step 6 — Evaluate the explicit promotion-readiness packet

Run the complete bounded shared fixture proof when appropriate:

```bash
make publish-check
```

Run the current synthetic matrices directly when diagnosis is needed:

```bash
python tools/validators/validate_promotion_gate.py --fixtures
python tools/validators/validate_review_record.py --fixtures
```

Evaluate one explicit candidate packet only after its public-safe packet exists:

```bash
python tools/validators/validate_promotion_gate.py \
  release/candidates/flora/<candidate-id>/promotion-readiness.json
```

The command is read-only. Preserve the exact validator version, input digest, output, exit code, and limitations.

A `PASS` means `APPROVE_READY` for accountable review only.

### Step 7 — Obtain active policy results

Resolve and record:

- accepted Flora domain-policy profile;
- accepted Flora sensitivity/geoprivacy profile;
- applicable rights and promotion policy;
- immutable policy bundle identity and digest;
- accepted evaluator and entrypoint;
- normalized finite result, reasons, and obligations;
- evaluation time and validity;
- governed consumer enforcement.

**Current repository state cannot complete this step.** Retain `HOLD_FOR_POLICY`.

### Step 8 — Assemble the public-safe candidate review packet

Assemble only identifiers, immutable pointers, digests, public-safe summaries, finite outcomes, limitations, and blocker state. Use the packet contract below.

Do not emit a `PromotionDecision`, `PromotionReceipt` with `transition.applied: true`, `ReleaseManifest`, public alias, or published carrier from this step.

### Step 9 — Obtain accountable review

Route the packet to the separately assigned:

- Flora domain reviewer;
- taxonomy reviewer;
- source and rights reviewers;
- sensitivity/geoprivacy reviewer;
- stewardship or community authority where applicable;
- evidence and policy reviewers;
- public-surface reviewer;
- independent release reviewer;
- correction and rollback reviewer; and
- release authority.

Record each review as its owning governed object. GitHub approval text may accompany review but cannot replace it.

### Step 10 — Handoff, do not self-transition

If every required reviewer and policy authority closes the packet, hand it to the release authority for a separately governed decision and operation.

Permitted handoff result:

```text
READY_FOR_ACCOUNTABLE_REVIEW
```

or the bounded validator's:

```text
APPROVE_READY
```

Neither result changes lifecycle state.

[Back to top](#top)

---

<a id="flora-specific-gates"></a>

## Flora-specific gates

The current executable validator uses this bounded A-G profile. ADR-0018 remains proposed, so treat these names as **current implementation evidence**, not accepted universal doctrine.

| Gate | Current executable name | Flora-specific closure | Fail-closed outcome |
|:---:|---|---|---|
| A | Identity and closure | Stable candidate, object family, taxon-concept references, source state, requested lifecycle boundary, proposed carrier, audience, manifest identity, and no restricted payload in the packet. | `DENY` or `HOLD_FOR_CANDIDATE`. |
| B | Asset integrity | Candidate, manifest, receipt, and digest-set agreement; deterministic artifacts; no mutable alias as sole anchor; public-safe artifact set is distinct from restricted originals. | `DENY` or `ERROR`. |
| C | Geometry and CRS | Declared valid geometry, deterministic processing, expected CRS, bounded public-safe extent, and no exact or reverse-engineerable sensitive location. The generic validator does not prove scientific geoprivacy. | `DENY` or `HOLD_FOR_GEOPRIVACY`. |
| D | Temporal semantics | Valid observation, collection, source, retrieval, publication, effective, review, correction, and release times as applicable; taxonomic and source versions; stale-state rules. | `DENY`, `HOLD_FOR_TIME`, or `ABSTAIN`. |
| E | Rights and sensitivity | Resolved rights, source role, sensitivity class, public audience, policy profile, finite policy result, stewardship or community authority where required, and no unsafe join. Current policy is inactive. | `DENY`, `RESTRICT`, `HOLD_FOR_RIGHTS`, `HOLD_FOR_SENSITIVITY`, or `HOLD_FOR_POLICY`. |
| F | Proof and catalog support | EvidenceRefs, EvidenceBundles, source descriptors, citations, receipts, attestations, STAC/DCAT/PROV or domain-catalog references, transform-review reference, and conditional AI receipt. | `ABSTAIN`, `HOLD_FOR_EVIDENCE`, or `DENY`. |
| G | Review and rollback | Accountable review, authority, separation, scope and hash binding, obligations closure, correction and withdrawal paths, rollback target, and public-surface invalidation plan. | `ABSTAIN`, `DENY`, or `HOLD_FOR_REVIEW`. |

### Flora sensitivity and representation matrix

| Material | Ordinary public-review posture | Minimum condition for a public-safe derivative | Failure posture |
|---|---|---|---|
| Common, non-sensitive Flora record | Eligible for review, not automatically public | Source, taxonomy, evidence, rights, policy, review, release, correction, and rollback closure | Hold or abstain |
| Rare or protected occurrence with exact location | **Do not include** | Reviewed public-safe derivative with restricted original retained outside the public packet; transform and review references only | Deny or restrict |
| Specimen locality that reveals a sensitive occurrence | **Do not include** | Generalized or withheld derivative with institution, rights, sensitivity, and review closure | Deny or restrict |
| Culturally sensitive plant knowledge | **Deny by default** | Verified authority to control, permitted purpose and audience, review, and revocation/correction path | Deny |
| Private-land or person/parcel join | **Do not include** | Join removed or safely aggregated; no access clue or identity exposure | Deny |
| Collection route, access direction, locality note, habitat clue, or repeated-query reconstruction path | **Do not include** | No ordinary public exception | Deny |
| Vegetation community, range, suitability, or distribution model | Derived and visibly labeled | Model/source/evidence lineage, uncertainty, time, validation, policy, and non-occurrence caveat | Abstain or deny role collapse |
| Invasive-plant record | Public-safe derivative only | Rights cleared; person, parcel, and access details removed; source role retained | Deny unsafe join |
| Phenology tied to a sensitive specimen or site | Aggregate or withhold | Reviewed aggregation/generalization and evidence support | Deny raw detail |
| Geoprivacy transform parameters, offsets, seeds, thresholds, or withheld precision | **Never ordinary public packet content** | Store only in an authorized restricted control plane where required | Deny and remediate |
| Unknown rights, taxonomy, sensitivity, or stewardship state | Not public | Resolve owning decision and re-run review | Hold, abstain, or deny |

[Back to top](#top)

---

<a id="current-executable-validation"></a>

## Current executable validation

### Flora public-safe fixture validator

Current executable:

```text
tools/validators/domains/flora/validate_public_safe_fixture.py
```

Current focused test:

```text
tests/domains/flora/test_flora_smoke.py
```

Current workflow:

```text
.github/workflows/domain-flora.yml
```

The validator and tests use the Python standard library and a shared bounded-JSON helper. The suite:

- accepts one explicit synthetic public-safe fixture;
- rejects six explicit invalid fixtures;
- blocks network access;
- requires fixture-only source, taxon, rights, evidence, spatial, sensitivity, public-representation, and governance markers;
- requires `release_state: not_released` and `promotion_eligible: false`;
- rejects location aliases, coordinate-like values, WKT, URLs, numeric candidate values, undeclared fields, and transform-secret aliases;
- rejects malformed, duplicate-key, non-finite, oversized, over-deep, over-large, or non-regular JSON input;
- emits stable sorted reason codes and JSON paths without echoing candidate values; and
- uses deterministic exit codes.

A Flora fixture `PASS` proves only conformance to that frozen synthetic profile.

It does **not** establish:

- botanical or taxonomic truth;
- source admission;
- rights or consent;
- sensitivity or geoprivacy approval;
- stewardship or community authority;
- EvidenceBundle closure;
- policy evaluation;
- proof production;
- candidate readiness;
- release, deployment, promotion, publication, or safe public use.

### Shared promotion-readiness validator

Current executable:

```text
tools/validators/promotion_gate/validate_promotion_gate.py
```

Current finite results:

| Result | Readiness | Exit | Meaning |
|---|---|---:|---|
| `PASS` | `APPROVE_READY` | `0` | Every bounded declaration passed; accountable review is still required. |
| `ABSTAIN` | `BLOCKED` | `1` | Support is insufficient without an explicit unsafe contradiction. |
| `DENY` | `BLOCKED` | `1` | A mandatory, unsafe, or contradictory condition blocks readiness. |
| `ERROR` | `BLOCKED` | `2` | Input or policy evaluation could not be completed safely. |

Precedence is:

```text
ERROR > DENY > ABSTAIN > PASS
```

The validator checks declared packet consistency. It does not dereference references, authenticate reviewers, verify real signatures, execute Rego, prove rights or sensitivity clearance, resolve EvidenceBundles, inspect the actual public surface, or mutate lifecycle state.

### Workflow holds

The current Flora workflow deliberately keeps these jobs as holds:

```text
build-proof-flora
  WORKFLOW_HOLD: no accepted Flora proof producer or deterministic proof command

publish-dry-run-flora
  WORKFLOW_HOLD: no accepted Flora release dry-run command or candidate manifest contract
```

A green held job means the hold is still intact. It is not proof production or release readiness.

### Validation recording rule

For every check, record:

- exact repository commit;
- exact executable path and blob or commit;
- exact command;
- exact input path and digest;
- environment and no-network posture;
- start and finish time;
- exit code;
- stdout/stderr or hosted log pointer;
- finite result;
- introduced versus inherited failure classification;
- limitations and unresolved follow-up.

Do not call a check “passing” unless the exact command or hosted exact-head job was observed.

[Back to top](#top)

---

<a id="candidate-review-packet"></a>

## Candidate review packet

Create a child candidate packet only after the candidate exists and its public-safe metadata can be disclosed.

### Required public-safe fields

| Family | Required content |
|---|---|
| Candidate identity | Candidate ID, version, object family, author/producer ID, requested lifecycle boundary, evaluation timestamp. |
| Artifact identity | Immutable artifact pointer, spec hash, content digests, proposed public carrier and audience. |
| Botanical scope | Taxon-concept refs, source-native names/IDs, crosswalk refs, identification state, unresolved taxonomy, object-family and method. |
| Source support | SourceDescriptor refs, admission refs, source roles, source-head/version, authority limits, rights and cadence states. |
| Evidence support | Claim IDs, EvidenceRefs, EvidenceBundle refs, citation-validation refs, limitations, stale/correction state. |
| Spatial and temporal scope | Public-safe spatial support, declared CRS, uncertainty/precision class, relevant time kinds, stale state. |
| Rights and sensitivity | Rights decision refs, sensitivity class, stewardship/community authority refs where applicable, public-safe transform or withholding review refs. |
| Policy | Accepted profile, bundle identity/digest, evaluator, finite result, reasons, obligations, evaluation time and validity. |
| Validation | Exact commands, executable versions, input digests, outputs, exit codes, receipts, limitations. |
| Public-surface review | Map/API/export/search/graph/cache/AI inspection refs and leakage findings. |
| Accountable review | Review IDs, reviewer identities, authority/assignment refs, scope, validity, separation, recommendation. |
| Release and recovery | Proposed PromotionDecision ref, PromotionReceipt ref, ReleaseManifest ref, correction/withdrawal refs, rollback target, invalidation scope. |
| Outcome | Current finite readiness outcome and explicit blockers. |

### Prohibited packet content

Do not include:

- raw or restricted source payloads;
- exact or reverse-engineerable coordinates;
- private-land or person identifiers;
- collection, access, locality, habitat, or route clues;
- culturally sensitive knowledge;
- redaction or generalization parameters;
- credentials, tokens, private URLs, or secret-manager references;
- unredacted logs or screenshots;
- model prompts containing restricted context;
- generated claims without evidence;
- statements that a check, review, merge, or manifest shape caused release.

Use stable public-safe pointers and reason codes. If even a pointer reveals sensitive context, keep it in the authorized restricted system and reference a public-safe review record instead.

[Back to top](#top)

---

<a id="finite-outcomes-and-current-holds"></a>

## Finite outcomes and current holds

These are operational handoff labels for this runbook. They do not replace accepted policy or release vocabularies.

| Outcome | Meaning | Next action |
|---|---|---|
| `READY_FOR_ACCOUNTABLE_REVIEW` | Public-safe packet is complete enough for assigned reviewers. | Open governed review; do not transition. |
| `APPROVE_READY` | Bounded shared validator returned `PASS`. | Treat as one validation input to accountable review. |
| `HOLD_FOR_CANDIDATE` | No stable child candidate or artifact set exists. | Create a candidate only through the accepted release lane. |
| `HOLD_FOR_TAXONOMY` | Taxon concept, identification, or crosswalk is unresolved. | Obtain qualified review or narrow the claim. |
| `HOLD_FOR_SOURCE_ADMISSION` | Source descriptor or admission state is missing or unresolved. | Return to source governance. |
| `HOLD_FOR_SOURCE_ROLE` | Observation, specimen, aggregate, model, regulatory, context, or synthetic role is collapsed or unclear. | Correct role and downstream claims. |
| `HOLD_FOR_RIGHTS` | License, terms, attribution, redistribution, consent, or embargo is unresolved. | Obtain an accountable rights decision. |
| `HOLD_FOR_SENSITIVITY` | Rare-plant, exact-location, private-land, cultural, stewardship, or join-induced risk is unresolved. | Restrict, generalize, withhold, or deny. |
| `HOLD_FOR_STEWARDSHIP` | Required steward or community authority is absent or unresolved. | Obtain an accountable assignment and decision. |
| `HOLD_FOR_GEOPRIVACY` | Public-safe transform, review, or surface inspection is incomplete. | Remediate upstream; never expose transform secrets. |
| `HOLD_FOR_EVIDENCE` | EvidenceRefs or EvidenceBundles do not resolve or are stale/conflicted. | Repair support or abstain. |
| `HOLD_FOR_CATALOG` | Catalog, lineage, or artifact closure is incomplete. | Return to catalog/proof lanes. |
| `HOLD_FOR_TIME` | Required time semantics, validity, or stale state is missing. | Correct time model or narrow scope. |
| `HOLD_FOR_POLICY` | Accepted policy, evaluator, result, or obligations are absent. | Keep candidate held; do not infer permission. |
| `HOLD_FOR_VALIDATION` | Required check is absent, stale, failing, or not exact-head. | Run or repair the bounded proof. |
| `HOLD_FOR_REVIEW` | Accountable reviewer identity, authority, separation, scope, or validity is missing. | Obtain governed review. |
| `HOLD_FOR_RELEASE_PATH` | Decision, receipt, manifest, operation, or public carrier path is unresolved. | Resolve release topology before approval. |
| `HOLD_FOR_CORRECTION_PATH` | Correction, withdrawal, supersession, or invalidation path is incomplete. | Define and review recovery. |
| `HOLD_FOR_ROLLBACK` | No safe prior target or rollback plan exists. | Prepare and validate a RollbackCard candidate. |
| `RESTRICT` | Review may continue only in an authorized restricted environment. | Keep protected material out of ordinary Git and public surfaces. |
| `ABSTAIN` | Support is insufficient for the requested claim or decision. | Narrow scope or obtain evidence. |
| `DENY` | The proposed operation is unsafe, prohibited, or contradictory. | Stop; record public-safe reason and remediation path. |
| `ERROR` | Evaluation could not complete safely. | Preserve prior state and diagnose without leaking values. |

### Current outcome

At the pinned repository checkpoint, the truthful outcome is:

```text
HOLD
```

The strongest immediate blockers are the absent child candidate, empty central source-authority projection, absent accepted Flora proof producer, inactive Flora and promotion policy, scaffolded Flora sensitivity policy, absent accountable Flora review, held Flora release dry run, and unverified released carrier.

[Back to top](#top)

---

<a id="authority-boundary-and-handoff"></a>

## Authority boundary and handoff

This runbook's terminal authority is a review handoff.

A complete handoff contains:

1. exact candidate identity and immutable artifact digests;
2. public-safe scope and audience;
3. source, taxonomy, evidence, rights, sensitivity, policy, validation, and public-surface support refs;
4. current finite outcome and blockers;
5. accountable reviewer and release-authority routing;
6. correction, withdrawal, invalidation, and rollback refs;
7. explicit non-effects.

The handoff must say:

```text
No source was admitted or activated.
No protected Flora payload or exact sensitive location was exposed.
No policy was accepted or activated.
No review or release authority was inferred from CODEOWNERS or CI.
No lifecycle transition was applied.
No release, deployment, promotion, or publication occurred.
```

Only a separately authorized release authority may create or approve the final governed transition records. Operations may execute only the accepted decision and must emit their own receipts. Public clients may consume only released public-safe carriers through governed interfaces.

[Back to top](#top)

---

<a id="correction-withdrawal-and-rollback"></a>

## Correction, withdrawal, and rollback

Promotion readiness is incomplete without a reversible public-state plan.

Before review, identify:

- the prior valid release or explicit no-prior-release state;
- correction and withdrawal triggers;
- candidate, manifest, catalog, evidence, proof, map, API, export, search, graph, cache, and AI-cache invalidation scope;
- downstream consumers and notification route;
- restoration or withdrawal target;
- public correction message requirements;
- review and authority required to apply recovery;
- revalidation and re-release requirements.

Use the sibling [`ROLLBACK_RUNBOOK.md`](./ROLLBACK_RUNBOOK.md) for Flora rollback procedure. That runbook and a schema-valid `RollbackCard` remain non-executing until a separately accountable decision and operation occur.

### Flora-specific recovery triggers

- taxon concept corrected, split, merged, or superseded;
- specimen identification or locality corrected;
- occurrence shown to be false, duplicated, mislocated, or out of scope;
- source rights, terms, consent, or attribution change;
- rare/protected/cultural sensitivity is newly identified;
- public derivative leaks or permits reconstruction of restricted detail;
- transform or generalization is invalidated;
- EvidenceBundle, citation, proof, or source role is withdrawn or corrected;
- model, range, vegetation, or phenology product is stale or misrepresented;
- policy bundle, reviewer authority, or release decision expires or is revoked;
- artifact digest, manifest, catalog, cache, or public alias diverges.

Rollback must preserve audit history. Do not delete or rewrite the original decision trail to make the correction invisible.

[Back to top](#top)

---

<a id="audit-and-join-keys"></a>

## Audit and join keys

Preserve deterministic, public-safe join keys where practical.

| Join key | Purpose |
|---|---|
| `candidate_id` and candidate version | Bind every readiness artifact to one candidate. |
| artifact digest set | Bind checks, review, decision, manifest, and rollback to exact bytes. |
| `spec_hash` | Bind candidate and validation to exact contract/profile identity. |
| taxon-concept and crosswalk refs | Preserve botanical identity and source-name lineage. |
| source descriptor and admission refs | Preserve source role, rights, sensitivity, cadence, and authority boundary. |
| claim ID, EvidenceRef, and EvidenceBundle refs | Bind release-visible claims to evidence. |
| policy profile, bundle digest, evaluator, and decision ref | Bind admissibility to exact policy. |
| validation receipt or hosted exact-head run | Bind reported checks to exact execution. |
| review ID, identity, authority, scope, and validity | Bind accountable review without inferring it from GitHub routing. |
| PromotionDecision and PromotionReceipt refs | Bind decision and attempt while keeping them distinct. |
| ReleaseManifest and release ID | Bind public carrier inventory to release state. |
| CorrectionNotice, WithdrawalNotice, and RollbackCard refs | Bind recovery and audit lineage. |
| public carrier digest and alias generation | Detect cache, index, tile, API, export, or map drift. |

Audit records must not reproduce protected values. Store sensitive detail only in the authorized restricted system and expose public-safe references or reason codes.

[Back to top](#top)

---

<a id="operator-checklist"></a>

## Operator checklist

### Candidate and authority

- [ ] Exact repository checkpoint and target blob are recorded.
- [ ] No open branch or pull request owns the same candidate or runbook surface.
- [ ] A verified child Flora candidate dossier exists.
- [ ] Candidate ID, version, artifact digest set, lifecycle state, target, audience, and carrier are explicit.
- [ ] Accountable role assignments and separation are verified.
- [ ] CODEOWNERS is treated as routing only.

### Taxonomy, source, and evidence

- [ ] Taxon concept, source-native identity, crosswalk, method, and uncertainty are resolved or visibly bounded.
- [ ] Observation, specimen, model, aggregate, regulatory, context, and synthetic roles remain distinct.
- [ ] Every source descriptor and admission state resolves.
- [ ] Rights, terms, attribution, cadence, source head, and authority boundaries resolve.
- [ ] Every consequential claim resolves EvidenceRef to EvidenceBundle.
- [ ] Catalog, proof, citation, receipt, correction, and invalidation refs close.

### Sensitivity and public representation

- [ ] No exact or reverse-engineerable sensitive location appears in the packet.
- [ ] No private-land, person, collection, access, locality, habitat, or route clue appears.
- [ ] No culturally sensitive knowledge appears without verified authority and permitted audience.
- [ ] No redaction or generalization parameters appear.
- [ ] Public-safe transform and review refs are present where needed.
- [ ] Map, API, export, search, graph, cache, screenshot, and AI surfaces were inspected.
- [ ] Client-side styling is not relied on as redaction.

### Policy, validation, review, and recovery

- [ ] Accepted Flora, sensitivity, rights, and promotion policy profiles are active.
- [ ] Policy bundle, evaluator, result, reasons, obligations, time, and validity are recorded.
- [ ] Flora fixture suite ran at the exact candidate branch/head where applicable.
- [ ] Shared promotion-gate and review-record checks ran against exact inputs.
- [ ] Every reported failure is classified as introduced, inherited, or unresolved.
- [ ] `PASS` is recorded only as `APPROVE_READY`.
- [ ] Accountable reviews, authority, scope, validity, separation, and recommendation resolve.
- [ ] Correction, withdrawal, invalidation, and rollback paths are complete.
- [ ] No release, deployment, promotion, or publication is implied by this checklist.

[Back to top](#top)

---

<a id="open-verification-register"></a>

## Open verification register

| Item | Current status | Evidence needed before reliance |
|---|---|---|
| Child Flora candidate dossier | **ABSENT in bounded inventory** | Verified child path, stable ID/version, immutable artifact pointer, public-safe scope, and blocker state. |
| Central source-authority projection | **PROPOSED / empty / implementation absent** | Accepted registry or resolver, populated entries, owners, source-admission records, and consumer enforcement. |
| Flora source-registry topology | **CONFLICTED / NEEDS VERIFICATION** | Accepted canonical lane, migration/compatibility rule, no divergent descriptor sets, and rollback. |
| Flora proof producer | **HOLD** | Accepted Flora proof profile, producer, public-safe fixtures, validators, receipts, access controls, and release linkage. |
| Flora EvidenceBundle resolution | **NEEDS VERIFICATION** | Resolver binding, real Flora bundle inventory, citation validation, invalidation, and consumer tests. |
| Promotion policy | **INACTIVE** | Accepted rules, tests, bundle, evaluator, active gate entry, normalized result, governed consumer, and rollback. |
| Flora domain policy | **M0 scaffold corpus / inactive** | Accepted entrypoint, rule semantics, native tests, evaluator, obligations, receipts, and consumer enforcement. |
| Flora sensitivity policy | **PROPOSED scaffold** | Domain-reviewed geoprivacy and cultural-knowledge rules, tests, evaluator, reviewer assignments, and public-surface enforcement. |
| Taxonomy authority and reviewer | **NEEDS VERIFICATION** | Accepted taxon-concept source/profile, crosswalk rules, qualified assignment, and conflict procedure. |
| Rights and stewardship authority | **NEEDS VERIFICATION** | Accountable assignments, current decisions, consent/authority validity, revocation, and audit path. |
| Flora release dry run | **HOLD** | Accepted candidate-manifest contract, deterministic no-write command, negative fixtures, review, and rollback binding. |
| Accountable Flora ReviewRecord | **NOT ESTABLISHED** | Authenticated identity, authority, scope, separation, validity, obligations, subject, and hash binding. |
| Flora PromotionDecision | **NOT ESTABLISHED** | Authorized candidate-specific decision with evidence, policy, review, and rollback refs. |
| Flora PromotionReceipt | **NOT ESTABLISHED** | Candidate-specific attempt record, exact gate outputs, digest binding, and truthful applied-state declaration. |
| Flora ReleaseManifest | **NOT ESTABLISHED** | Authorized strict release instance, artifact inventory, support refs, signatures, correction, rollback, and persisted release state. |
| Published Flora carrier | **UNVERIFIED** | Release-linked public-safe bytes, digests, governed delivery, cache/index parity, and public-surface tests. |
| Required-check enforcement | **NEEDS VERIFICATION** | Exact-head hosted results and repository ruleset evidence for required checks; green workflow presence is insufficient. |
| Rollback drill | **NEEDS VERIFICATION** | Candidate-specific no-write rehearsal, invalidation inventory, restoration target, receipts, review, and observed recovery behavior. |

[Back to top](#top)

---

<a id="evidence-basis"></a>

## Evidence basis

### Current repository evidence

This revision is grounded in current-session inspection of:

- accepted ADR-0029 and the adopted Directory Rules bytes;
- proposed ADR-0018 and its explicit non-acceptance;
- the exact prior target file;
- the Flora domain workflow;
- the bounded Flora validator, fixtures, and focused tests;
- the central source-authority projection;
- Flora source-registry, proof, policy, sensitivity, candidate, and published-lane boundaries;
- shared promotion-gate, review, PromotionDecision, PromotionReceipt, ReleaseManifest, and RollbackCard surfaces;
- CODEOWNERS review routing; and
- the current main checkpoint.

Repository evidence supports the current bounded implementation claims in this runbook. It does not prove deployment, production policy, active sources, restricted-system state, external consumers, operational release, or public use.

### Google Drive source lineage

The Google Drive document **KFM Flora Architecture PDF-Only Implementation Blueprint** was inspected as planning lineage. It supports the design need to keep taxon/naming, specimens, occurrences, source roles, rare and culturally sensitive flora, modeled/generalized products, evidence, policy, review, correction, and rollback distinct.

The blueprint explicitly records that it was produced without a mounted KFM repository and labels implementation paths as proposed. This runbook therefore uses it for scope and design pressure only. Current GitHub evidence controls claims about repository paths, validators, workflows, policy maturity, candidate inventory, and release state.

### Evidence not established

This revision did not inspect or exercise:

- a live or restricted Flora source;
- real protected coordinates or culturally sensitive knowledge;
- a production evidence resolver;
- a production policy evaluator or bundle;
- an authenticated reviewer or stewardship registry;
- a signer trust root or transparency log;
- a release service or deployment;
- a public map/API/export/search/AI surface;
- a real Flora candidate, proof packet, review, decision, manifest, release, or rollback execution.

[Back to top](#top)

---

<a id="document-change-rollback"></a>

## Document change rollback

This update changes only:

```text
docs/runbooks/flora/PROMOTION_RUNBOOK.md
```

Before merge, close the draft pull request and remove its scoped branch if the revision is rejected or superseded.

After merge, revert the documentation commit through a reviewed pull request or apply a smaller forward correction. Do not rewrite shared history.

Reverting this Markdown:

- does not admit or deactivate a source;
- does not alter a Flora candidate or data artifact;
- does not change contracts, schemas, policy, validators, tests, fixtures, workflows, evidence, proofs, receipts, reviews, decisions, manifests, or published carriers;
- does not execute rollback; and
- does not release, deploy, promote, or publish anything.

[Back to top](#top)
