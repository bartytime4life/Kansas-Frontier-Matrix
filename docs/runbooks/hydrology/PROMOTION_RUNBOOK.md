<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook-hydrology-promotion
title: Hydrology Promotion Runbook
type: operational-runbook
version: v2.0.0
status: DRAFT_REPOSITORY_GROUNDED; BOUNDED_PROMOTION_READINESS_ONLY; OPERATIONAL_PROMOTION_HELD; NOT_FOR_LIFE_SAFETY; NON_RELEASE; NON_PUBLICATION
owners: "@bartytime4life — verified CODEOWNERS route; accountable Hydrology, source, evidence, policy, rights, sensitivity, review, release, operations, correction, and rollback stewardship NEEDS VERIFICATION"
created: 2026-05-12
updated: 2026-08-27
policy_label: repository-facing; hydrology; promotion-preflight; fail-closed; not-for-life-safety; non-publisher
owning_root: docs/
path_authority: same-path modernization under accepted ADR-0029 and Directory Rules v2
authority_effect: none
source_activation_effect: none
lifecycle_effect: none
release_effect: none
deployment_effect: none
promotion_effect: none
publication_effect: none
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: b7663990b81cb3b29fd2891c24720cc1064ebe95
  target_path: docs/runbooks/hydrology/PROMOTION_RUNBOOK.md
  target_prior_blob: 32081072ca1c368a7b19fc3b63960914c3937c3f
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adoption_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  promotion_gate_readme_blob: e729df0cc007e8cf0d9811afc25ec1f5ffbdffdd
  promotion_gate_workflow_blob: 9b567aad17de2a7419a2a0238386745c1cb5c11c
  hydrology_domain_workflow: .github/workflows/domain-hydrology.yml
  hydrology_validation_runbook_blob: c6c6ee9c89ad394847ef9e5ac053b7a136595678
  promotion_decision_contract_blob: 42295bfc83a621cf125d33aa821912b426f70bd2
  release_manifest_contract_blob: ce7dc89ff447d76d974afdd802b85a38538d8f48
  candidate_lane_readme_blob: 7b93fc2bc3b3363235374f0ee8b9b2c51921ffd2
  hydrology_policy_readme: policy/domains/hydrology/README.md
  hydrology_promoter_stub_blob: 98ec4d03ec0b41f03a85ee1fcedd5b75b4a2f68e
  hydrology_smoke_decision_blob: 50d611f8ef800863e04eafde0716ed2c45303299
  hydrology_proof_lane_payloads: 0
  hydrology_receipt_lane_payloads: 0
  hydrology_published_lane_payloads: 0
  open_pull_requests_touching_target_before_branch: 0
source_lineage:
  - title: KFM_Hydrology_Extended_Pro_PDF_Only_Reference_Report_2026-04-21.pdf
    source_class: PLANNING_LINEAGE
    use: hydrology-first, source-role, temporal, evidence, no-network, promotion, and rollback framing only
  - title: KFM Evidence, Documentation & Ideas Atlas — 2026-08-24
    source_class: NOTION_COORDINATION_ONLY
    use: preserve documentation, validation, review, merge, release, deployment, promotion, and publication as separate states
  - title: KFM Markdown Update & Modernization Agent v1.0
    source_class: CURRENT_TASK_GUIDANCE
    use: same-path repository-grounded Markdown modernization and focused draft-pull-request delivery
related:
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../doctrine/directory-rules.md
  - ../README.md
  - ../../domains/hydrology/README.md
  - VALIDATION.md
  - NO_NETWORK_TEST_RUNBOOK.md
  - SOURCE_REFRESH_RUNBOOK.md
  - ROLLBACK_RUNBOOK.md
  - ../../../release/README.md
  - ../../../release/candidates/hydrology/README.md
  - ../../../release/reviews/README.md
  - ../../../contracts/release/promotion_decision.md
  - ../../../contracts/release/release_manifest.md
  - ../../../schemas/contracts/v1/release/promotion_decision.schema.json
  - ../../../schemas/contracts/v1/release/release_manifest.schema.json
  - ../../../tools/validators/promotion_gate/README.md
  - ../../../tools/validators/validate_promotion_gate.py
  - ../../../tools/validators/validate_review_record.py
  - ../../../policy/domains/hydrology/README.md
  - ../../../data/proofs/hydrology/README.md
  - ../../../data/receipts/hydrology/README.md
  - ../../../data/published/hydrology/README.md
  - ../../../pipelines/domains/hydrology/promote.py
  - ../../../release/promotion_decisions/hydrology/run-local-smoke.json
  - ../../../.github/workflows/promotion-gate.yml
  - ../../../.github/workflows/domain-hydrology.yml
notes:
  - The repository implements deterministic, no-network A-G promotion-readiness validation and bounded Hydrology fixture validation; neither is operational promotion.
  - The Hydrology candidate, proof, receipt, and published-data lanes contain guidance or placeholders but no candidate dossier, proof instance, receipt instance, or published payload at the pinned base.
  - The checked-in Hydrology promoter and automation-smoke decision are explicitly held because they write or declare APPROVE while their EvidenceBundle and rollback references remain unresolved.
  - This runbook prepares and interprets a preflight and review handoff. It never creates a PromotionDecision, ReleaseManifest, review authority, lifecycle transition, release, deployment, promotion, or publication event.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hydrology Promotion Runbook

> **One-line purpose.** Prepare and evaluate one immutable Hydrology candidate for accountable release review using KFM's current bounded readiness checks, then stop before any lifecycle transition, release, deployment, promotion, or publication.

[![Status: operational promotion held](https://img.shields.io/badge/status-operational%20promotion%20held-b42318?style=flat-square)](#current-disposition)
[![Readiness: bounded no-network](https://img.shields.io/badge/readiness-bounded%20no--network-8250df?style=flat-square)](#repository-native-validation)
[![Hydrology: not life safety](https://img.shields.io/badge/hydrology-not%20life%20safety-b42318?style=flat-square)](#hydrology-safety-and-source-role-boundary)
[![Public effect: none](https://img.shields.io/badge/public%20effect-none-6e7781?style=flat-square)](#authority-and-terminal-boundary)

> [!WARNING]
> **KFM Hydrology is not an emergency-alerting, flood-warning, navigation, engineering, insurance, regulatory, or incident-command authority.** Do not use this procedure to issue, replace, delay, retract, summarize as actionable, or interpret a current warning, evacuation instruction, dam-safety direction, regulatory determination, or protective-action message. FEMA NFHL material is regulatory context, not observed inundation. Direct urgent or authoritative decisions to the responsible official source.

<a id="current-disposition"></a>

> [!IMPORTANT]
> **Current disposition: `BOUNDED_PROMOTION_READINESS_AVAILABLE / OPERATIONAL_HYDROLOGY_PROMOTION_HOLD`.** The repository has a deterministic no-network A-G readiness validator, fixture-only ReviewRecord checks, Hydrology shape and polarity checks, and read-only workflows that preserve explicit holds. It does not have a populated Hydrology candidate dossier, Hydrology proof or receipt instance, accepted active Hydrology policy bundle and evaluator, authenticated accountable release review, operational promoter, verified public carrier, or public read-back evidence.

```yaml
work_state: HOLD
available_evidence:
  - BOUNDED_PROMOTION_GATE_FIXTURE_VALIDATION
  - FIXTURE_ONLY_REVIEW_RECORD_VALIDATION
  - BOUNDED_HYDROLOGY_SHAPE_AND_POLARITY_VALIDATION
reason_codes:
  - HYD_PROMOTION_CANDIDATE_ABSENT
  - HYD_PROMOTION_PROOF_ABSENT
  - HYD_PROMOTION_RECEIPT_ABSENT
  - HYD_POLICY_EVALUATOR_UNBOUND
  - HYD_REVIEW_AUTHORITY_UNVERIFIED
  - HYD_PROMOTER_STUB_HELD
  - HYD_RELEASE_PUBLIC_SURFACE_ABSENT
lifecycle_effect: none
release_effect: none
deployment_effect: none
promotion_effect: none
publication_effect: none
```

**Quick navigation:** [Goal](#goal-and-scope) · [Authority](#authority-and-terminal-boundary) · [Evidence](#current-repository-evidence) · [Vocabulary](#state-and-vocabulary-separation) · [Safety](#hydrology-safety-and-source-role-boundary) · [Preconditions](#preconditions) · [Gates](#bounded-a-g-readiness-profile) · [Procedure](#promotion-preflight-procedure) · [Validation](#repository-native-validation) · [Interpretation](#interpret-the-results) · [Stops](#mandatory-stop-conditions) · [Handoff](#accountable-review-handoff-packet) · [Rollback](#correction-withdrawal-and-rollback) · [Open work](#open-verification-and-graduation-gate) · [Related](#related-repository-surfaces) · [Maintenance](#maintenance-and-document-rollback)

---

## Goal and scope

Use this runbook when a maintainer needs to determine whether one exact Hydrology candidate is sufficiently declared and supported to enter **accountable release review**.

The intended lifecycle boundary is:

```text
CATALOG or TRIPLET -> PUBLISHED
```

The current safe operating circle stops earlier:

```text
exact candidate identity and repository SHA
  -> source, evidence, rights, sensitivity, time, geometry, and review preflight
  -> bounded no-network A-G readiness validation
  -> bounded Hydrology validation evidence
  -> PASS / ABSTAIN / DENY / ERROR plus HOLD analysis
  -> accountable review handoff
  -> no lifecycle or public-state mutation
```

### In scope

- freeze the exact candidate, artifacts, repository revision, validation identity, audience, and proposed public surface;
- verify that the candidate actually exists in the accepted Hydrology candidate lane rather than being inferred from prose, a branch, or a smoke fixture;
- require stable source, evidence, rights, sensitivity, spatial, temporal, catalog, review, correction, and rollback references appropriate to the candidate;
- preserve Hydrology source-role distinctions, especially observation, model, regulatory context, derived context, candidate, and synthetic test data;
- run the current bounded promotion and ReviewRecord validation commands;
- run or cite the exact bounded Hydrology validation profile at the same tested revision;
- interpret finite outcomes without upgrading them into approval or execution authority;
- prepare a public-safe handoff for accountable reviewers; and
- preserve the prior lifecycle and public state when support is absent, conflicting, stale, unsafe, or unverified.

### Out of scope

- activating or admitting a live source;
- fetching current USGS, WBD, NHDPlus, FEMA, state, local, or other external data;
- creating or rewriting RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, proof, receipt, release, or PUBLISHED objects;
- treating a synthetic fixture, proposal, shape-valid record, workflow summary, or repository path as current hydrologic truth;
- authenticating reviewer identity or assigning release authority;
- executing Rego or another production policy bundle unless separately accepted and bound;
- running [`pipelines/domains/hydrology/promote.py`](../../../pipelines/domains/hydrology/promote.py) against a real or synthetic release path;
- signing, persisting, approving, releasing, deploying, promoting, publishing, mutating aliases, invalidating production consumers, or changing repository settings; and
- issuing or interpreting emergency, engineering, navigation, insurance, permit, or regulatory guidance.

[Back to top](#top)

---

<a id="authority-and-terminal-boundary"></a>

## Authority and terminal boundary

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts [Directory Rules v2](../../doctrine/directory-rules.md). Those rules place human operating procedures under `docs/runbooks/`, semantic meaning under `contracts/`, machine shape under `schemas/`, policy source under `policy/`, lifecycle and trust artifacts under `data/`, and release decisions under `release/`.

This is a same-path modernization of an established file. It creates no new responsibility root or parallel contract, schema, policy, evidence, proof, receipt, candidate, release, or publication home.

| Responsibility | Owning surface | This runbook may do | This runbook must not do |
|---|---|---|---|
| Human Hydrology promotion procedure | `docs/runbooks/hydrology/PROMOTION_RUNBOOK.md` | Explain preflight, bounded validation, finite outcomes, stops, and handoff | Grant release or promotion authority |
| Hydrology domain meaning | [`docs/domains/hydrology/`](../../domains/hydrology/README.md) and `contracts/domains/hydrology/` | Preserve source-role and safety boundaries | Redefine Hydrology semantics |
| PromotionDecision meaning and shape | [`contracts/release/promotion_decision.md`](../../../contracts/release/promotion_decision.md) and its schema | Require and inspect declared references | Manufacture an authenticated decision |
| ReleaseManifest meaning and shape | [`contracts/release/release_manifest.md`](../../../contracts/release/release_manifest.md) and its schema | Require appropriate candidate support | Treat shape validity as release closure |
| Bounded readiness behavior | [`tools/validators/promotion_gate/`](../../../tools/validators/promotion_gate/README.md) | Run deterministic fixture-first checks | Resolve live authority or mutate state |
| Hydrology executable behavior | `tests/domains/hydrology/`, `tools/validators/domains/hydrology/`, and [`domain-hydrology`](../../../.github/workflows/domain-hydrology.yml) | Require exact changed-area evidence | Treat bounded fixtures as current conditions |
| Source authority and admission | Accepted SourceDescriptors, source registries, and activation decisions | Require exact references | Activate or admit a source |
| Evidence, proof, and receipts | Governed `data/` trust-artifact lanes | Resolve and inspect references | Invent closure or collapse object families |
| Policy and review | Accepted policy bundle/evaluator plus authenticated review records | Require finite outcomes and obligations | Infer approval from CODEOWNERS, CI, or prose |
| Candidate review | [`release/candidates/hydrology/`](../../../release/candidates/hydrology/README.md) | Prepare a candidate handoff | Store payloads or claim publication |
| Release, correction, withdrawal, rollback | [`release/`](../../../release/README.md) | Stop at reviewable handoff | Write or execute a transition |
| Public delivery | Governed APIs and released public-safe carriers | Require evidence-visible consumer behavior | Serve internal or unreleased stores directly |

The highest result this procedure can establish is:

```text
READY_FOR_ACCOUNTABLE_RELEASE_REVIEW
```

That result is not `APPROVED`, `PROMOTED`, `RELEASED`, `DEPLOYED`, or `PUBLISHED`.

[Back to top](#top)

---

## Current repository evidence

The observations below are pinned to `main@b7663990b81cb3b29fd2891c24720cc1064ebe95`. Re-read the exact surfaces when the base, candidate lane, workflow, validator, policy, review, proof, receipt, manifest, promoter, or public carrier changes.

| Surface | CONFIRMED repository evidence | Bounded conclusion |
|---|---|---|
| Runbook path | This file exists under `docs/runbooks/hydrology/` | Same-path update is valid; the prior claim that this path is merely proposed is stale |
| Candidate lane | `release/candidates/hydrology/` contains its README only | No Hydrology candidate dossier exists to advance |
| Shared readiness validator | The promotion-gate implementation evaluates a declared packet through seven deterministic no-network gates | A fixture result can support review; it cannot execute promotion |
| ReviewRecord validation | Fixture-only ReviewRecord validation checks declared identity, authority interval, separation, scope, and hash bindings | No live identity, assignment, authority registry, or completed Hydrology review is authenticated |
| Promotion workflow | `.github/workflows/promotion-gate.yml` runs read-only checks and explicitly retains review and Hydrology-promoter holds | Workflow success means the declared bounded checks and holds behaved as expected |
| Hydrology workflow | `.github/workflows/domain-hydrology.yml` runs bounded synthetic shape, polarity, identity, and cross-domain checks while holding proof and release production | Useful domain validation; not evidence closure, active policy, or release readiness |
| PromotionDecision contract | A proposed contract, paired schema, fixtures, validator, and focused checks exist | Shape and finite enum are bounded; an authenticated operational decision is not established |
| ReleaseManifest contract | A dual-profile proposed contract and fixture-only strict candidate profile exist | Legacy permissiveness and fixture-only strict checks do not prove release closure |
| Hydrology policy | The lane contains mixed allow/deny scaffolds, no accepted active bundle/evaluator binding, and no complete consumer enforcement path | Operational policy evaluation remains `NEEDS VERIFICATION / HOLD` |
| Hydrology proof lane | `data/proofs/hydrology/` contains `.gitkeep` and a README only | No Hydrology proof instance exists |
| Hydrology receipt lane | `data/receipts/hydrology/` contains `.gitkeep` and a README only | No Hydrology receipt instance exists |
| Hydrology published lane | `data/published/hydrology/` contains `.gitkeep` and a README only | No released Hydrology payload is established there |
| Review records | `release/reviews/` contains guidance and an Atmosphere directory; no Hydrology review record is present | Accountable Hydrology review remains absent |
| Hydrology promoter | `pipelines/domains/hydrology/promote.py` is a timestamped automation-smoke stub that writes `APPROVE` | Do not execute it as a promotion mechanism |
| Checked-in smoke decision | `run-local-smoke.json` declares `APPROVE` and references missing Hydrology proof and rollback paths | It is held test/scaffold evidence, not an operational decision |
| Deployment and public read-back | No deployed route, release alias, runtime log, public carrier, invalidation result, or public read-back was established for this procedure | Operational promotion and public recovery remain unknown and held |

### Current finite result

```text
readiness_implementation: BOUNDED_FIXTURE_FIRST
candidate_state: ABSENT
policy_state: UNBOUND
review_state: ABSENT
operational_promotion_state: HOLD
public_state_change: NONE
```

[Back to top](#top)

---

## State and vocabulary separation

Keep validator outcomes, work state, review, decision, lifecycle application, release, and publication separate.

| Term | Meaning here | Effect |
|---|---|---|
| `PASS` | Every check in the invoked bounded validator profile passed | No lifecycle or public-state change |
| `APPROVE_READY` | The promotion-gate validator's readiness projection for a bounded `PASS` | Review may proceed; no approval exists |
| `ABSTAIN` | Support is insufficient without a proven unsafe contradiction | Preserve prior state; narrow or complete support |
| `DENY` | A mandatory, unsafe, prohibited, or contradictory condition blocks readiness | Preserve prior state; do not route around the denial |
| `ERROR` | The evaluation could not complete safely | Preserve prior state; repair input or evaluator |
| `HOLD` | Governance or work-state block such as absent candidate, unbound policy, missing authority, unresolved rights, or pending overlap | No transition and no release handoff |
| `READY_FOR_ACCOUNTABLE_RELEASE_REVIEW` | Candidate and preflight packet are reviewable by the proper authority | Still not an approval or transition |
| `PromotionDecision.APPROVE` | A separately governed release-family decision for an exact run | Does not by itself create a manifest, apply a transition, deploy, or publish |
| `PUBLISHED` | A separately governed transition has completed and a public-safe carrier is available through the proper path | Outside this runbook |

Never translate `SKIPPED`, `NOT_RUN`, `PENDING`, `NO_RUN_FOUND`, a green explicit-hold job, a GitHub merge, or a manifest-shaped file into `PASS`, review approval, or release state.

[Back to top](#top)

---

<a id="hydrology-safety-and-source-role-boundary"></a>

## Hydrology safety and source-role boundary

Every candidate must preserve what the source can support and what KFM is allowed to say about it.

| Object or source family | Required role distinction | Publication-blocking collapse |
|---|---|---|
| WBD / HUC boundaries | Watershed-unit authority/context at a named source vintage | Treating a boundary as an observed water condition or flood extent |
| NHDPlus / hydrography identity | Network, geometry, identity, context, or modeled attributes as explicitly declared | Treating modeled or derived flow attributes as measurements |
| Gauge and water observations | Observation with parameter, unit, datum, qualifier, provisional/final state, observed time, and retrieval time | Presenting stale, provisional, missing, or transformed values as unqualified current fact |
| FEMA NFHL | Regulatory flood-hazard context with effective/version time | Calling a zone observed inundation, a current event, a forecast, or an emergency warning |
| Terrain-derived hydrology | Derived/model context with source DEM, method, resolution, uncertainty, and receipt | Upgrading a derivative to authoritative observation |
| Historical flood evidence | Historical observation/context with date, evidence type, limitations, and correction lineage | Presenting historical evidence as current conditions |
| Synthetic fixtures | Test-only data with no public or scientific authority | Treating a fixture result as Kansas hydrologic truth |
| Map, tile, dashboard, index, graph, or AI answer | Downstream representation of released evidence | Treating representation as sovereign truth |

Use `HOLD`, `ABSTAIN`, or `DENY` when source role, time, units, datum, qualifier, rights, sensitivity, evidence, or public-use posture is unresolved. A policy or materiality score cannot compensate for source-role collapse or life-safety ambiguity.

[Back to top](#top)

---

## Preconditions

Do not run a candidate preflight until every applicable condition is represented by an immutable or versioned reference. Missing support remains a stop condition, not a documentation field to fill by assumption.

| # | Required condition | Minimum evidence | Failure posture |
|---:|---|---|---|
| 1 | Exact candidate exists | Candidate ID, dossier path, byte or artifact digest, current candidate state, and owning lifecycle pointer | `HOLD` |
| 2 | Repository and validation identity are pinned | Full commit SHA plus head, merge-result, or immutable candidate identity | `ERROR` or `NEEDS VERIFICATION` |
| 3 | Source identity and role are accepted | SourceDescriptor IDs/versions, activation state, role, rights, terms, cadence, and citation basis | `HOLD`, `ABSTAIN`, or `DENY` |
| 4 | Candidate shape and semantics are governed | Applicable contracts, schemas, validators, and compatibility profile are named | `DENY` or `ERROR` |
| 5 | Spatial identity is closed | CRS, bounded extent, geometry digest, validity, precision/generalization, and HUC/reach/gauge identity state | `ABSTAIN` or `DENY` |
| 6 | Time is explicit | Source, observed, valid, retrieval, release/effective, freshness, correction, and model-run time where material | `ABSTAIN` or `DENY` |
| 7 | Evidence resolves | Every consequential public claim resolves from EvidenceRef to admissible EvidenceBundle support | `ABSTAIN` or `DENY` |
| 8 | Rights and sensitivity are resolved | Rights/redistribution/attribution state, audience, precision, sensitivity, transforms, and obligations | `DENY` or `HOLD` |
| 9 | Policy evaluation is accepted and reproducible | Accepted bundle/evaluator identity, input profile, finite result, obligations, and consumer enforcement | `ERROR`, `DENY`, or `HOLD` |
| 10 | Validation is complete for the declared profile | Exact commands, tested SHA, positive and negative results, and unresolved skipped/not-run checks | `DENY` or `HOLD` |
| 11 | Proof, catalog, and receipt support exists | Resolvable proof, catalog, provenance, attestation, and receipt references appropriate to significance | `ABSTAIN` or `DENY` |
| 12 | Accountable review is authenticated | Current reviewer identity, authority interval, scope, separation, obligations, and non-superseded record | `HOLD` or `DENY` |
| 13 | Correction and rollback are real | Correction path, prior safe target or withdrawal posture, rollback target, invalidation scope, and public read-back plan | `ABSTAIN`, `DENY`, or `HOLD` |
| 14 | No overlap owns the same candidate or semantics | Current PR/branch overlap inventory and reconciliation result | `HOLD` |

At the pinned base, preconditions 1, 7, 9, 11, 12, and 13 are not established for an operational Hydrology candidate. The current default result is therefore `HOLD` before execution.

[Back to top](#top)

---

## Bounded A-G readiness profile

The current shared validator uses this bounded, deterministic profile. It checks declarations in a packet; it does not resolve or authenticate the external objects those declarations name.

| Gate | Name | Current bounded checks | Failure posture |
|:---:|---|---|---|
| A | Identity and closure | Profile, candidate, author, spec hash, lifecycle boundary, minimal manifest identity | `DENY` on missing or contradictory identity |
| B | Asset integrity | Candidate/manifest/receipt hash agreement and non-empty unique digest-set equality | `DENY` on invalid or mismatched digest |
| C | Geometry and CRS | Declared validity, deterministic processing, `EPSG:4326`, finite ordered world bbox | `DENY` on invalid or nondeterministic geometry |
| D | Temporal semantics | Canonical UTC-second timestamps, bounded interval, and declared evaluation instant | `DENY` on malformed or inverted time |
| E | Rights and sensitivity policy context | Known profile/labels, public-safe discipline, finite supplied policy result | `DENY` on rejection; `ERROR` on evaluator failure |
| F | Proof and catalog support | Declared evidence, attestation, STAC/DCAT/PROV, receipt, and conditional AI-receipt references | `ABSTAIN` for unresolved evidence; `DENY` for mandatory integrity/catalog gaps |
| G | Review and rollback | Fixture-only review declaration, identity syntax and timing, supplied authority interval, separation, scope/hash bindings, rollback, and correction linkage | `DENY` on unsafe or contradictory declarations; `ABSTAIN` on missing authority or correction lineage |

### What the profile does not prove

A bounded `PASS` does not prove:

- that a source is admitted, current, or fit for the candidate claim;
- that a referenced EvidenceBundle, proof, receipt, catalog record, review, policy decision, rollback target, or artifact exists or is authentic;
- that rights, sensitivity, current conditions, or scientific meaning are correct;
- that a live reviewer has the required authority or separation of duties;
- that DSSE, cosign, transparency-log, or artifact-byte verification succeeded;
- that a ReleaseManifest is complete beyond the bounded profile;
- that a transition was applied or a public consumer reads the resulting carrier; or
- that release, deployment, promotion, publication, or recovery occurred.

[Back to top](#top)

---

## Promotion preflight procedure

### 1. Freeze exact scope and authority

Record:

- repository and exact 40-character SHA;
- candidate ID, dossier path, digest, and lifecycle pointer;
- proposed `CATALOG` or `TRIPLET` to `PUBLISHED` boundary;
- included artifacts and excluded claims;
- source roles, geography, time interval, audience, and intended public carriers;
- governing contract/schema/policy profiles;
- accountable roles required for review and execution;
- correction, withdrawal, rollback, invalidation, and public read-back scope; and
- overlapping branches, pull requests, migrations, incidents, or release work.

Stop if the candidate is absent. Do not substitute `run-local-smoke.json`, a fixture, a branch, a merged pull request, or an intended future packet.

### 2. Verify candidate and lifecycle pointers

Confirm the dossier links to candidate bytes in their owning lifecycle lane. The candidate directory must not contain duplicated payloads or imply that its own presence changes lifecycle state.

Verify:

- artifact media types and SHA-256 digests;
- source and producing-run identity;
- current lifecycle state;
- predecessor/supersession relationships;
- proposed published target;
- no floating `latest` or mutable unpinned reference where immutability is required; and
- no internal-store path exposed as a normal public URL.

### 3. Verify Hydrology meaning, source role, time, and representation

For each artifact and claim:

1. classify it as observation, regulatory context, model/derivative, historical context, candidate, synthetic, or another accepted role;
2. record the applicable source, observed, valid, retrieval, freshness, release/effective, correction, and model-run times;
3. preserve parameter, unit, datum, qualifier, provisional/final status, and no-data semantics;
4. verify CRS, geometry validity, scale, resolution, precision/generalization, identity/crosswalk state, and representation limitations;
5. require a representation or transform receipt when geometry, aggregation, interpolation, classification, redaction, or symbology materially changes meaning; and
6. stop on NFHL-as-observed-flood, model-as-observation, stale-as-current, or fixture-as-truth collapse.

### 4. Resolve evidence, rights, sensitivity, and policy prerequisites

Resolve—not merely list—the applicable:

- SourceDescriptors and activation decisions;
- EvidenceRefs and EvidenceBundles;
- rights, license, attribution, redistribution, embargo, and citation records;
- sensitivity, precision, infrastructure, private-property, sovereignty, and cross-lane join posture;
- policy input profile, exact bundle/evaluator identity, finite result, and obligations; and
- downstream consumer support for every obligation.

Do not manufacture an `ALLOW`, `APPROVE`, `DENY`, `ABSTAIN`, or `ERROR` result from documentation. Where the accepted evaluator path is absent or unbound, record `HOLD`.

### 5. Run repository-native bounded validation

Run the commands in [Repository-native validation](#repository-native-validation) at the exact candidate/repository identity. Preserve output and exit status without copying protected payloads or secrets.

A documentation-only change may cite exact hosted results. An operational candidate requires candidate-bound validation, not a green run from an unrelated branch or fixture.

### 6. Interpret finite results without upgrading them

Apply the [interpretation table](#interpret-the-results). A bounded `PASS` is one input to accountable review. It cannot override a missing candidate, unresolved EvidenceBundle, unbound policy evaluator, absent review authority, missing rollback target, or public-safety boundary.

### 7. Assemble the review handoff

Complete the [handoff packet](#accountable-review-handoff-packet). Include all holds and not-run states. Do not request operational execution until the graduation gate is independently satisfied.

### 8. Stop before transition execution

This runbook ends with either:

```text
READY_FOR_ACCOUNTABLE_RELEASE_REVIEW
```

or a finite blocked result with reason codes. It does not run the Hydrology promoter, write a PromotionDecision, emit or sign a ReleaseManifest, copy a carrier into a published lane, mutate an alias, deploy, promote, or publish.

[Back to top](#top)

---

<a id="repository-native-validation"></a>

## Repository-native validation

Run from the repository root at an exact recorded revision. Use the repository lock/installer and workflow environment when dependencies are required.

### Shared promotion-readiness proof

```bash
make publish-check
```

The target runs the fixture-only ReviewRecord and A-G promotion-gate checks. It performs no network access and writes no release object.

Equivalent focused commands:

```bash
python tools/validators/validate_review_record.py --fixtures
python tools/validators/validate_promotion_gate.py --fixtures
```

### Bounded Hydrology validation

Use the current [`Hydrology Bounded Validation Runbook`](VALIDATION.md) and exact module/fixture commands mirrored by [`domain-hydrology`](../../../.github/workflows/domain-hydrology.yml). There is deliberately no accepted `make hydrology-validate` or `make validate-hydrology` parent target at the pinned base; do not invent one.

The focused current profile includes:

- bounded Hydrology domain modules;
- public-safe flow positive and expected-negative fixtures;
- cross-domain ownership isolation;
- fixture-only EvidenceBundle alias shape;
- AquiferObservation and AquiferContextLink shape separation; and
- bounded NHDPlus waterbody crosswalk ambiguity behavior.

### Documentation validation

```bash
python tools/validators/docs/link-check/check_links.py \
  --repo-root . \
  --format text \
  docs/runbooks/hydrology/PROMOTION_RUNBOOK.md
```

The link checker validates local targets and bounded fragments only. It does not prove semantic correctness, external availability, release authority, or operational safety.

### Hosted workflows

- [`promotion-gate`](../../../.github/workflows/promotion-gate.yml) owns bounded readiness orchestration and explicit review/promoter holds.
- [`domain-hydrology`](../../../.github/workflows/domain-hydrology.yml) owns bounded Hydrology shape and polarity orchestration plus explicit proof/release holds.
- Generic docs, schema, contract, policy, security, and repository workflows may also run for a Markdown change.

Record `SKIPPED`, `NOT_RUN`, `PENDING`, or missing-run evidence exactly. A successful hold job proves that the hold remained visible and fail-closed; it does not prove the held capability exists.

[Back to top](#top)

---

<a id="interpret-the-results"></a>

## Interpret the results

| Observation | Required interpretation | Promotion posture |
|---|---|---|
| `make publish-check` returns bounded `PASS` | Declared synthetic packet matrix and ReviewRecord profile passed | Continue preflight; no approval |
| Readiness result is `ABSTAIN` | Required support is unresolved without a hard contradiction | Preserve prior state; resolve or narrow support |
| Readiness result is `DENY` | Mandatory or unsafe condition blocks readiness | Stop; do not route around denial |
| Readiness result is `ERROR` | Input/evaluator could not complete safely | Stop; repair and rerun at exact identity |
| Hydrology valid fixtures pass and expected-invalid fixtures fail | Bounded domain polarity passed at tested SHA | Domain check input only |
| Hydrology fixture, shape, or crosswalk check passes | Only the named synthetic behavior is demonstrated | Do not claim current conditions or evidence closure |
| Candidate dossier is absent | No candidate can be promoted | `HOLD` regardless of validator result |
| Proof, receipt, policy evaluator, review authority, or rollback target is absent | Governance closure is incomplete | `HOLD`, `ABSTAIN`, or `DENY` according to consequence |
| `run-local-smoke.json` says `APPROVE` | Checked-in scaffold/smoke declaration exists | Ignore as operational authority; retain hold |
| Promotion workflow passes its promoter-hold job | The stub remained unexecuted and unresolved refs remained visible | `HOLD` remains correct |
| Pull request merges | Repository history changed | No candidate, release, deployment, promotion, or publication inference |
| Public-looking layer or API response is observed without immutable release and evidence support | Exposure does not prove governance | Contain and escalate; do not call it published-safe |

A candidate is `READY_FOR_ACCOUNTABLE_RELEASE_REVIEW` only when all applicable preconditions are supported and no `HOLD`, `ABSTAIN`, `DENY`, or `ERROR` remains. At the pinned base, that condition is not met for an operational Hydrology candidate.

[Back to top](#top)

---

## Mandatory stop conditions

Stop and record the procedure-specific finite result when any applicable condition below is present:

- no immutable Hydrology candidate dossier exists;
- the candidate, source, artifact, repository, workflow, or validation identity cannot be pinned;
- a source is proposed, inactive, rights-unclear, sensitivity-unclear, stale, superseded, or role-ambiguous;
- NFHL regulatory context would be represented as observed inundation, a current event, forecast, or emergency warning;
- a modeled or terrain-derived result would be represented as an observation;
- parameter, unit, datum, qualifier, provisional/final state, no-data semantics, identity, CRS, geometry, scale, resolution, or time is missing or collapsed;
- EvidenceRef does not resolve to an admissible EvidenceBundle for a consequential claim;
- generated language, a map, tile, graph, index, dashboard, model, or fixture is being treated as canonical truth;
- rights, redistribution, attribution, sensitivity, precision, infrastructure, private-property, Tribal/Indigenous, cultural, living-person, or protected-location posture is unresolved;
- an accepted policy bundle, evaluator, input profile, finite result, obligation set, or consumer binding is absent;
- a proof, receipt, catalog, attestation, review, correction, withdrawal, rollback, or predecessor reference is missing or non-resolving;
- reviewer identity, current authority, scope, separation, obligations, validity interval, or non-superseded state cannot be authenticated;
- no distinct safe predecessor exists and no accepted withdrawal/hold posture is defined;
- the requested action would execute the held Hydrology promoter, write lifecycle or public state, use credentials, access a live source, mutate an alias, release, deploy, promote, publish, invalidate production consumers, or change repository settings;
- the exact command, path, contract, schema, fixture, validator, policy, or workflow differs from the pinned revision; or
- overlapping work owns the same candidate, target path, release semantics, or execution surface and has not been reconciled.

Do not weaken negative fixtures, remove a hold, accept unresolved references, or substitute a documentation assertion merely to obtain a green result.

[Back to top](#top)

---

<a id="accountable-review-handoff-packet"></a>

## Accountable review handoff packet

Use the accepted machine contracts when they exist. The worksheet below is a human handoff aid; it is not a PromotionDecision, ReviewRecord, ReleaseManifest, proof, receipt, or policy result.

```yaml
repository:
  sha: <40-character SHA>
  validation_identity: HEAD | MERGE_RESULT | RELEASE_CANDIDATE
candidate:
  candidate_id: <stable id>
  dossier_path: <release/candidates/hydrology/...>
  artifact_refs: []
  artifact_digests: []
  current_lifecycle_state: CATALOG | TRIPLET
  requested_boundary: PUBLISHED
scope:
  geography: <bounded extent>
  object_families: []
  time_interval: <explicit interval>
  audience: <declared audience>
  public_carriers: []
  excluded_claims: []
source_and_evidence:
  source_descriptors: []
  source_roles: []
  evidence_refs: []
  evidence_bundles: []
  unresolved_support: []
spatial_and_temporal:
  crs: <value>
  geometry_digest: <sha256>
  identity_state: <exact | crosswalk | ambiguous | unresolved>
  observed_time: <value or not applicable>
  valid_time: <value or not applicable>
  retrieval_time: <value>
  freshness_state: <current | stale | expired | unknown>
rights_sensitivity_policy:
  rights_state: <value>
  sensitivity_state: <value>
  transform_receipts: []
  policy_bundle: <ref or NEEDS VERIFICATION>
  policy_outcome: <finite result or HOLD>
  obligations: []
validation:
  promotion_gate_commands: []
  hydrology_commands: []
  tested_sha: <40-character SHA>
  finite_outcomes: []
  expected_negative_results: []
  skipped_or_not_run: []
review:
  required_roles: []
  authenticated_records: []
  separation_of_duties: <confirmed | not confirmed>
release_recovery:
  proposed_manifest_ref: <ref or NEEDS VERIFICATION>
  correction_ref: <ref or NEEDS VERIFICATION>
  withdrawal_posture: <ref or not applicable>
  rollback_target: <ref or NEEDS VERIFICATION>
  invalidation_consumers: []
  public_readback_plan: <ref or NEEDS VERIFICATION>
result:
  readiness: READY_FOR_ACCOUNTABLE_RELEASE_REVIEW | BLOCKED
  reason_codes: []
non_effects:
  source_activated: false
  lifecycle_mutated: false
  promotion_decision_written: false
  release_executed: false
  deployment_executed: false
  promotion_executed: false
  publication_executed: false
```

### Minimum reviewer questions

1. Does the exact candidate exist and match every artifact digest?
2. Are source role, object family, spatial scope, temporal scope, units, datum, qualifiers, uncertainty, and representation limits explicit?
3. Do consequential claims resolve to admissible EvidenceBundles?
4. Are rights, sensitivity, precision, public-safety, and cross-lane obligations enforceable by every consumer?
5. Did exact candidate-bound positive and negative checks run at the stated identity?
6. Is the policy result from an accepted bundle/evaluator rather than a declared fixture value?
7. Are reviewer identity, authority, scope, separation, obligations, validity, and supersession state authenticated?
8. Does a verified prior safe target exist, or is withdrawal/hold the accepted first-release recovery posture?
9. Can aliases, APIs, caches, tiles, catalogs, triplets, search/vector indexes, AI caches, and downstream derivatives be invalidated and read back?
10. Is the requested result still only accountable review, with execution separately authorized?

[Back to top](#top)

---

## Correction, withdrawal, and rollback

Promotion planning is incomplete without recovery planning.

- Use [`ROLLBACK_RUNBOOK.md`](ROLLBACK_RUNBOOK.md) to classify and prepare Hydrology rollback, withdrawal, or forward-correction work.
- Use the accepted release/correction object families under [`release/`](../../../release/README.md); do not invent a local Markdown-only correction authority.
- Preserve the original candidate, decision, manifest, evidence, receipts, proofs, and public-state history. Corrections and supersessions are append-only.
- A first Hydrology release with no distinct safe predecessor needs an accepted withdrawal or fail-closed hold posture; do not invent a rollback target.
- A predecessor is not automatically safer. Revalidate its evidence, rights, sensitivity, policy, integrity, compatibility, and public behavior before proposing restoration.
- Public recovery requires consumer invalidation and public read-back evidence appropriate to actual exposure. A repository revert alone does not recover API, tile, cache, search, graph, AI, deployment, or client state.

The current synthetic rollback and release profiles do not establish an operational Hydrology recovery path. Operational correction, withdrawal, rollback, invalidation, and public recovery remain held.

[Back to top](#top)

---

## Open verification and graduation gate

| Item | Current posture | Smallest truthful next step |
|---|---|---|
| Hydrology candidate dossier | **ABSENT / HOLD** | Assemble one immutable candidate only after source, evidence, rights, sensitivity, validation, policy, review, correction, and rollback prerequisites exist |
| Source authority and live acquisition | **PROPOSED / MIXED / HOLD** | Admit one bounded public-safe source through accepted source governance before candidate assembly |
| Evidence and proof closure | **ABSENT / HOLD** | Produce one resolvable Hydrology EvidenceBundle/proof circle tied to stable identity and exact public claims |
| Hydrology receipts | **ABSENT / HOLD** | Emit governed process receipts from an accepted no-network candidate build without confusing receipts with proof |
| Active Hydrology policy | **SCAFFOLDS / EVALUATOR UNBOUND** | Reconcile result polarity, accept a bundle/input/normalization contract, add native negative tests, and bind governed consumers |
| PromotionDecision profile | **PROPOSED BOUNDED SHAPE** | Accept the semantic/machine profile and authenticate authority before operational use |
| ReleaseManifest profile | **DUAL PROFILE / FIXTURE ONLY** | Resolve common-versus-Hydrology profile authority and close ref, byte, signature, policy, review, persistence, and consumer behavior |
| Accountable review | **ABSENT / NEEDS VERIFICATION** | Establish authenticated Hydrology/release roles, authority intervals, separation, obligations, and revocation |
| Hydrology promoter | **STUB / HOLD** | Replace or retire the timestamped automation-approve stub only through a separately reviewed implementation with no-write dry runs and fail-closed tests |
| Operational transition executor | **ABSENT / HOLD** | Implement an accepted plan/apply boundary with authorization, idempotency, receipts, partial-failure handling, and rollback |
| Published carrier and governed consumer parity | **ABSENT / UNKNOWN** | Demonstrate one immutable public-safe carrier through the governed API, map/Evidence Drawer, finite response, citation, correction, and public read-back |
| Invalidation and rollback | **UNVERIFIED / HOLD** | Exercise real consumer adapters in an approved non-public environment before operational graduation |
| Independent stewardship | **NEEDS VERIFICATION** | Assign accountable source, Hydrology, evidence, policy, rights, sensitivity, review, release, operations, and rollback roles |

### Operational graduation gate

Operational Hydrology promotion remains `HOLD` until current evidence demonstrates all of the following together:

1. one immutable candidate dossier and exact artifact set;
2. admitted source authority and stable source-role semantics;
3. EvidenceRef-to-EvidenceBundle and proof closure;
4. accepted rights, sensitivity, geometry, time, and representation controls;
5. accepted active policy bundle/evaluator and enforceable obligations;
6. authenticated accountable review and separation of duties;
7. accepted PromotionDecision and ReleaseManifest profiles;
8. safe plan/apply execution with idempotency and partial-failure handling;
9. correction, withdrawal, prior-target, invalidation, and rollback support;
10. governed API, map/Evidence Drawer, export, and AI consumer parity;
11. deployment and public read-back evidence at an exact immutable identity; and
12. documented reversal that restores a safe state without erasing history.

No weighted score or deadline may compensate for failure of a non-compensable trust or safety gate.

[Back to top](#top)

---

## Related repository surfaces

### Human procedures and doctrine

- [Parent runbook index](../README.md)
- [Hydrology domain boundary](../../domains/hydrology/README.md)
- [Hydrology bounded validation](VALIDATION.md)
- [Hydrology no-network procedure](NO_NETWORK_TEST_RUNBOOK.md)
- [Hydrology source-refresh procedure](SOURCE_REFRESH_RUNBOOK.md)
- [Hydrology rollback procedure](ROLLBACK_RUNBOOK.md)
- [Directory Rules v2](../../doctrine/directory-rules.md)
- [ADR-0029 — adopt Directory Governance Standard v2](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)

### Promotion, release, policy, and trust artifacts

- [Release governance root](../../../release/README.md)
- [Hydrology candidate lane](../../../release/candidates/hydrology/README.md)
- [Release review lane](../../../release/reviews/README.md)
- [PromotionDecision contract](../../../contracts/release/promotion_decision.md)
- [PromotionDecision schema](../../../schemas/contracts/v1/release/promotion_decision.schema.json)
- [ReleaseManifest contract](../../../contracts/release/release_manifest.md)
- [ReleaseManifest schema](../../../schemas/contracts/v1/release/release_manifest.schema.json)
- [Promotion-gate validator boundary](../../../tools/validators/promotion_gate/README.md)
- [Hydrology policy boundary](../../../policy/domains/hydrology/README.md)
- [Hydrology proof lane](../../../data/proofs/hydrology/README.md)
- [Hydrology receipt lane](../../../data/receipts/hydrology/README.md)
- [Hydrology published lane](../../../data/published/hydrology/README.md)

### Explicit held surfaces

- [Hydrology promoter stub](../../../pipelines/domains/hydrology/promote.py)
- [Automation-smoke decision](../../../release/promotion_decisions/hydrology/run-local-smoke.json)
- [Promotion-gate workflow](../../../.github/workflows/promotion-gate.yml)
- [Hydrology domain workflow](../../../.github/workflows/domain-hydrology.yml)

[Back to top](#top)

---

## Maintenance and document rollback

Update this runbook when:

- the candidate lane gains or loses an actual dossier;
- the promotion-gate profile, finite outcomes, fixture matrix, Make target, or workflow changes;
- the Hydrology validation profile changes;
- source authority, EvidenceBundle resolution, proof, receipt, policy, review, manifest, transition, correction, rollback, deployment, public carrier, or public read-back evidence changes;
- the Hydrology promoter is replaced, retired, or becomes operationally admissible;
- common and Hydrology-specific release-profile authority is reconciled;
- accountable roles or separation of duties are accepted or revoked; or
- a real exercise, correction, withdrawal, rollback, or incident exposes a procedure gap.

This is a documentation-only change. Before merge, close the draft pull request and discard only its task branch. After an authorized merge, revert the focused documentation commit or submit a smaller reviewed forward correction. The prior blob `32081072ca1c368a7b19fc3b63960914c3937c3f` restores the proposal-era document, but reverting this Markdown never reverses a source admission, lifecycle transition, release, deployment, promotion, publication, alias, cache, public carrier, or operational state.

[Back to top](#top)
