<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook-roads-rail-trade-promotion
title: Roads, Rail, and Trade Promotion Preflight Runbook
type: standard
version: v2.0
prior_state: proposal-heavy May 2026 promotion procedure with unverified paths, commands, gates, receipts, roles, and release execution
status: draft; repository-grounded; PROMOTION_EXECUTION_HELD; BOUNDED_NO_NETWORK_VALIDATION; NON_RELEASE; NON_DEPLOYMENT; NON_PUBLICATION
owners:
  - "@bartytime4life — verified GitHub review route"
  - "NEEDS VERIFICATION — accountable Roads/Rail/Trade, transport, evidence, rights, sensitivity, policy, safety, and release assignments"
created: 2026-05-12
updated: 2026-08-29
policy_label: repository-facing; infrastructure-sensitive; historic and cultural corridor precision-sensitive; fail-closed
current_path: docs/runbooks/roads-rail-trade/PROMOTION_RUNBOOK.md
owning_root: docs/
responsibility: human promotion preflight and accountable-review handoff for the Roads/Rail/Trade lane
truth_posture: cite-or-abstain
authority_class: explanatory operational documentation
authority_rank: subordinate to accepted doctrine and ADRs, contracts, schemas, source records, policy, evidence, lifecycle, review, release, correction, rollback, and official authorities
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 3009a477071271c9a1d2ac0a1fcac98d26e40976
  target_before_update_blob: 315eb67a2c6cadac812f66e4e81f0a42f7f0c40d
  local_runbook_boundary_blob: 5de90772b7ae420f42ed2794e7f545e55035aaa9
  domain_workflow_blob: 391fead3fdd0d7ecead6464be7946cbaf68247e0
  corridor_route_contract_blob: 2bef2e964b8afa855ca7e72c86ca72dad2b63f52
  corridor_route_schema_blob: 663afd8aa09c52a2626d84cfbc6c76965df79942
  corridor_route_validator_blob: 9b75fd5d15d348ec788057fa1e1371f82e685415
  corridor_route_tests_blob: 4df9495c441810e5ad196d88ad67f64e00426136
  candidate_lane_readme_blob: c989bf2bed10472bc46a168231b2269f17bbda48
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adoption_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  candidate_records_observed: 0
  bounded_executable_profiles: 1
related:
  - ./README.md
  - ./NO_NETWORK_TEST_RUNBOOK.md
  - ./ROLLBACK_RUNBOOK.md
  - ../../domains/roads-rail-trade/README.md
  - ../../domains/roads-rail-trade/DATA_LIFECYCLE.md
  - ../../domains/roads-rail-trade/SENSITIVITY.md
  - ../../doctrine/directory-rules.md
  - ../../doctrine/lifecycle-law.md
  - ../../doctrine/trust-membrane.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../.github/workflows/domain-roads-rail-trade.yml
  - ../../../contracts/domains/roads-rail-trade/corridor_route.md
  - ../../../schemas/contracts/v1/domains/roads-rail-trade/corridor_route.schema.json
  - ../../../tools/validators/domains/roads-rail-trade/validate_corridor_route.py
  - ../../../tests/schemas/test_corridor_route_contract.py
  - ../../../fixtures/domains/roads-rail-trade/corridor_route/
  - ../../../data/registry/sources/roads-rail-trade/README.md
  - ../../../data/proofs/roads-rail-trade/README.md
  - ../../../policy/domains/roads-rail-trade/README.md
  - ../../../release/candidates/roads-rail-trade/README.md
notes:
  - "v2.0 replaces proposal-era promotion execution with a current-repository preflight and accountable-review handoff."
  - "The only executable domain profile verified for this update is synthetic, no-network CorridorRoute validation."
  - "The domain workflow deliberately holds proof production and release dry-run; no candidate packet or promotion executor was established."
  - "This documentation change does not admit a source, create a candidate, issue a policy decision, approve review, release, deploy, promote, or publish."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Roads, Rail, and Trade Promotion Preflight Runbook

> Prepare, validate, and hand off one Roads/Rail/Trade candidate for accountable
> review without creating route truth, operational authority, release authority,
> promotion authority, deployment authority, or publication state.

> [!WARNING]
> KFM is not a navigation, dispatch, traffic-control, railroad-operating,
> bridge-safety, emergency-routing, legal-access, right-of-way, regulatory, or
> current-closure authority. Stop if the requested work could be mistaken for
> current safe-passage, legal-access, infrastructure-condition, or emergency
> guidance.

> [!IMPORTANT]
> **Current result: `HOLD`.** The repository contains one bounded, synthetic,
> no-network `CorridorRoute` validation profile. The Roads/Rail/Trade candidate
> lane contains no candidate record, the proof job reports no accepted proof
> producer, and the release-dry-run job reports no accepted domain command or
> candidate-manifest contract. This runbook stops at preflight and handoff.

## Quick navigation

- [1. Goal and scope](#1-goal-and-scope)
- [2. Authority and terminal boundary](#2-authority-and-terminal-boundary)
- [3. Current repository disposition](#3-current-repository-disposition)
- [4. State and outcome vocabulary](#4-state-and-outcome-vocabulary)
- [5. Preconditions](#5-preconditions)
- [6. Preflight check matrix](#6-preflight-check-matrix)
- [7. Roles and separation of duties](#7-roles-and-separation-of-duties)
- [8. Procedure](#8-procedure)
- [9. Repository-native validation](#9-repository-native-validation)
- [10. Mandatory stop conditions](#10-mandatory-stop-conditions)
- [11. Candidate handoff packet](#11-candidate-handoff-packet)
- [12. Release handoff](#12-release-handoff)
- [13. Correction and rollback](#13-correction-and-rollback)
- [14. Acceptance and negative cases](#14-acceptance-and-negative-cases)
- [15. Related repository surfaces](#15-related-repository-surfaces)
- [16. Open verification backlog](#16-open-verification-backlog)
- [17. Runbook maintenance and documentation rollback](#17-runbook-maintenance-and-documentation-rollback)

## 1. Goal and scope

This runbook governs the **preflight and review handoff** for a proposed
Roads/Rail/Trade transition from `CATALOG` or `TRIPLETS` toward `PUBLISHED`.
It helps an operator determine whether an immutable candidate is supported
well enough for accountable review.

### In scope

- freezing one candidate identity, exact repository ref, artifact inventory,
  and digest set;
- verifying source role, rights, sensitivity, time, geometry, uncertainty,
  evidence, validation, policy, review, correction, and rollback references;
- running the repository's bounded synthetic `CorridorRoute` checks at the
  exact reviewed ref;
- recording `PASS`, `ABSTAIN`, `DENY`, `ERROR`, and workflow `HOLD` results
  without collapsing them into release state;
- producing a public-safe, reference-only candidate dossier; and
- handing a complete packet to separately authenticated accountable reviewers.

### Out of scope

- source discovery, live retrieval, source admission, or connector operation;
- creating or mutating route, segment, membership, crossing, facility,
  operator, restriction, legal-access, safe-passage, or current-status truth;
- moving payloads between lifecycle lanes;
- issuing an operational policy decision or authenticating a reviewer;
- assembling a real release manifest, proof pack, signature, or published
  carrier;
- changing a public API, map, graph, tile, export, Focus Mode, deployment, or
  runtime surface; and
- approving, releasing, deploying, promoting, publishing, or activating data.

## 2. Authority and terminal boundary

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
adopts the [Directory Rules](../../doctrine/directory-rules.md). Those rules
place human operational procedures under `docs/runbooks/`, candidate dossiers
under `release/candidates/`, release decisions under the appropriate
`release/<object-family>/` lane, and release-approved public-safe carriers under
`data/published/`.

This file therefore explains a procedure. It is not a source descriptor,
contract, schema, policy rule, EvidenceBundle, proof, review record, promotion
decision, release manifest, rollback card, receipt, signature, published
carrier, or operational instruction.

Directory placement does not grant truth, rights clearance, review, release,
or publication status. Promotion emits a new governed state or version; it is
never inferred from a copy, move, filename, workflow completion, green check,
or mutable alias.

The highest result this runbook may produce is:

```text
READY_FOR_ACCOUNTABLE_RELEASE_REVIEW
```

That result means the dossier is coherent enough for the responsible humans to
review. It does **not** mean `APPROVED`, `RELEASED`, `DEPLOYED`, `PROMOTED`, or
`PUBLISHED`.

## 3. Current repository disposition

The evidence below is bound to the commit and blobs in the metadata block. A
later change must be re-inspected before relying on this table.

| Surface | Current evidence | Bounded conclusion |
|---|---|---|
| Runbook path | This file already exists below `docs/runbooks/roads-rail-trade/` | **CONFIRMED.** Same-path replacement is valid; no new home is required. |
| Local procedure boundary | `docs/runbooks/roads-rail-trade/README.md` classifies the prior promotion runbook as proposal-heavy | **CONFIRMED stale procedure.** Replace its unverified execution claims with this preflight boundary. |
| Candidate lane | `release/candidates/roads-rail-trade/` contains `README.md` only | **CONFIRMED / ABSENT candidate.** No real candidate can advance. |
| Executable domain profile | Contract, schema, validator, synthetic fixtures, and focused tests exist for `CorridorRoute` | **CONFIRMED / BOUNDED.** The profile can return `PASS`, `ABSTAIN`, `DENY`, or `ERROR`; it is not route evidence or release closure. |
| Domain workflow | `.github/workflows/domain-roads-rail-trade.yml` runs the focused tests and fixture validator with `KFM_NO_NETWORK=1` | **CONFIRMED / BOUNDED.** It proves only the named checks at the tested SHA. |
| Broader domain validation | The workflow records broader Roads/Rail/Trade semantic validation as not established | **CONFIRMED / HOLD.** Do not generalize from `CorridorRoute` to the whole lane. |
| Proof production | The workflow reports no accepted Roads/Rail/Trade proof producer or deterministic proof command | **CONFIRMED / HOLD.** A green held job is not an EvidenceBundle or proof. |
| Release dry-run | The workflow reports no accepted Roads/Rail/Trade release-dry-run command or candidate-manifest contract | **CONFIRMED / HOLD.** The job performs no release, promotion, or public write. |
| Policy | Domain policy files and a proposal-oriented policy README exist; the workflow guards the scaffold posture | **CONFIRMED presence / PARTIAL.** File presence does not establish accepted runtime evaluation or a candidate-bound decision. |
| Review routing | `CODEOWNERS` routes repository review to `@bartytime4life` | **CONFIRMED route / INSUFFICIENT authority.** Routing is not domain, rights-holder, sensitivity, release, or independent approval. |
| Operational promotion | No candidate, accepted proof producer, domain release-dry-run command, authenticated authority, or execution path was established | **UNKNOWN / HOLD.** Do not execute a lifecycle transition. |

### Current finite result

```yaml
work_state: HOLD
reason_codes:
  - RRT_CANDIDATE_ABSENT
  - RRT_PROOF_PRODUCER_UNESTABLISHED
  - RRT_RELEASE_DRY_RUN_UNESTABLISHED
  - RRT_POLICY_RUNTIME_UNVERIFIED
  - RRT_ACCOUNTABLE_REVIEW_AUTHORITY_UNVERIFIED
terminal_boundary: ACCOUNTABLE_REVIEW_HANDOFF_ONLY
promotion_execution: HELD
release: NOT_PERFORMED
deployment: NOT_PERFORMED
publication: NOT_PERFORMED
```

## 4. State and outcome vocabulary

Keep validator result, workflow/work state, review state, promotion decision,
release state, deployment state, and publication state separate.

| Term | Meaning here | Authority effect |
|---|---|---|
| `PASS` | The invoked bounded validator found no violation in its declared profile | No lifecycle or release change |
| `ABSTAIN` | Required support is unresolved and the validator refuses a stronger result | Candidate does not advance |
| `DENY` | A prohibited, unsafe, contradictory, or released-without-closure state was detected | Candidate does not advance |
| `ERROR` | Valid evaluation could not complete | Result is unusable until repaired and rerun |
| `HOLD` | Ownership, authority, rights, sensitivity, overlap, candidate, proof, policy, review, correction, rollback, or operational closure is unresolved | Work remains in its prior state |
| `READY_FOR_ACCOUNTABLE_RELEASE_REVIEW` | Every applicable preflight item is supported and the dossier is reviewable | Still not approval or release |
| `APPROVED` | An authenticated accountable authority approved the exact candidate under an accepted decision contract | Not emitted by this runbook |
| `PUBLISHED` | A separately authorized release decision activated an immutable public-safe carrier | Not emitted by this runbook |

The `CorridorRoute` validator's finite result is evidence for one bounded
profile. Do not translate its `PASS` into a review, promotion, release,
deployment, or publication result.

## 5. Preconditions

A candidate is eligible for this preflight only when every applicable item is
bound to an immutable or versioned object. Missing support produces `HOLD`,
`ABSTAIN`, `DENY`, or `ERROR`; it never produces partial promotion.

| # | Required support | Minimum evidence | Default if unresolved |
|---:|---|---|---|
| 1 | Exact candidate identity | Candidate ID, domain, object family, exact repository/build ref, version, artifact inventory, and deterministic digests | `HOLD` or `DENY` |
| 2 | Lifecycle boundary | Prior state and proposed transition are explicit; no skipped state or file-move inference | `DENY` |
| 3 | Canonical source descriptors | Stable source IDs, roles, rights, access, sensitivity, citation, cadence, version, and retrieval identity | `ABSTAIN`, `HOLD`, or `DENY` |
| 4 | Source-role separation | Observed, regulatory, modeled, aggregate, administrative, candidate, context, and synthetic roles remain distinct where applicable | `DENY` |
| 5 | Object and membership identity | Route, segment, membership, crossing, facility, operator, restriction, and graph identities are not collapsed | `DENY` |
| 6 | Time and freshness | Source, observed, valid, retrieval, build, release, expiry, correction, and withdrawal times are distinguished where material | `ABSTAIN`, `HOLD`, or `DENY` |
| 7 | Geometry and uncertainty | CRS, topology, precision, lineage, reconstruction status, uncertainty, and public transform are supported | `ABSTAIN`, `HOLD`, or `DENY` |
| 8 | Rights and sensitivity | Redistribution basis and cultural, sovereignty, infrastructure, access, precision, private-property, and combination-risk obligations are resolved | `HOLD` or `DENY` |
| 9 | Evidence closure | Every consequential `EvidenceRef` resolves to an admissible candidate-scoped `EvidenceBundle` | `ABSTAIN` or `DENY` |
| 10 | Catalog/projection closure | Catalog and optional triplet/graph projections are reproducible and remain derived | `HOLD` or `DENY` |
| 11 | Policy result | Accepted evaluator identity, policy bundle/version, candidate binding, finite outcome, reasons, and obligations | `HOLD`, `DENY`, or `ERROR` |
| 12 | Validation closure | Applicable schemas, validators, negative fixtures, tests, and exact-ref results are complete | `HOLD`, `DENY`, or `ERROR` |
| 13 | Accountable review | Authenticated roles, current assignments, scope binding, conflicts, independence, time, and required rights-holder review | `HOLD` or `ABSTAIN` |
| 14 | Correction and rollback | Correction path, invalidation scope, prior target, recovery procedure, and rollback evidence are candidate-bound | `HOLD` or `DENY` |
| 15 | Public boundary | Public consumers use governed interfaces or released carriers; no internal, restricted, candidate, or mutable store is exposed | `DENY` |
| 16 | Overlap and ownership | No active branch, pull request, migration, or steward work owns the same candidate or authority surface | `HOLD` |

## 6. Preflight check matrix

The prior runbook described a seven-gate implementation as though
Roads/Rail/Trade wiring and release execution were established. Current
repository evidence supports only the bounded `CorridorRoute` profile. Use the
matrix below as a human preflight checklist; it is **not** an accepted machine
enum and must not be reported as an executed release gate.

| Check family | Required closure | Current lane disposition |
|---|---|---|
| Placement and identity | Candidate dossier is in the candidate lane; payloads remain in their owning lifecycle roots; identities and digests are immutable | `HOLD` — no candidate record |
| Artifact integrity | Candidate inventory, manifest references, receipts, proofs, and digests agree over the exact artifact set | `HOLD` — no candidate/proof packet |
| Source and evidence | Source roles, rights, retrieval identity, citations, EvidenceRefs, and EvidenceBundles close without upcasting | `HOLD` — real candidate support absent |
| Time, geometry, and uncertainty | Temporal roles, freshness, CRS, precision, reconstruction, membership, and transform lineage are coherent | `NEEDS VERIFICATION` for any real candidate |
| Rights, sensitivity, and cross-domain authority | Cultural/sovereignty, infrastructure, legal-access, private-property, exact-location, and combination risks are resolved by the correct owners | `HOLD` — accountable roles unverified |
| Policy and validation | Accepted candidate-bound policy result plus applicable schema, validator, negative-fixture, and test evidence | `HOLD` — bounded schema profile only; runtime policy unverified |
| Review, correction, and rollback | Authenticated independent review where required, explicit obligations, correction lineage, rollback target, and recovery evidence | `HOLD` — authority and operational closure unverified |

## 7. Roles and separation of duties

Do not infer an actor's authority from a filename, commit author, requested
review, CODEOWNERS route, workflow identity, or repository permission.

| Role | Required responsibility | Current status |
|---|---|---|
| Candidate author | Assemble immutable references and disclose all known gaps; never self-create approval | `UNKNOWN` until a candidate exists |
| Domain steward | Confirm Roads/Rail/Trade semantics, identity, membership, time, and cross-domain boundaries | `NEEDS VERIFICATION` |
| Source and rights reviewer | Confirm source identity, authority role, rights, access, attribution, cadence, and redistribution | `NEEDS VERIFICATION` |
| Cultural/sovereignty reviewer | Review Indigenous, Tribal, treaty, oral-history, cultural-corridor, and steward-controlled knowledge where applicable | `NEEDS VERIFICATION` |
| Infrastructure/security reviewer | Review critical facilities, harmful precision, private access, and combination risks where applicable | `NEEDS VERIFICATION` |
| Evidence/policy reviewer | Confirm evidence closure and accepted candidate-bound policy evaluation | `NEEDS VERIFICATION` |
| Correction/rollback reviewer | Confirm correction, invalidation, rollback target, recovery procedure, and evidence | `NEEDS VERIFICATION` |
| Release authority | Decide the exact release under an accepted contract after all required reviews | `NEEDS VERIFICATION`; outside this runbook |

For policy-significant, rights-sensitive, precision-sensitive,
infrastructure-sensitive, first-source, or first-public-surface work, the
candidate author must not self-approve. If the required independent authority
cannot be authenticated, return `HOLD`.

## 8. Procedure

### Step 0 — Stop at the operational-safety boundary

Confirm that the request is not asking KFM to determine or change current
safe-passage, traffic control, rail operation, bridge condition, closure,
detour, legal access, emergency response, or regulatory status. If it is, stop,
preserve repository and candidate state, and refer the question to the official
authority.

Record either `RRT_NON_OPERATIONAL_BOUNDARY_CONFIRMED` or the reason for
`DENY` or `ESCALATE`.

### Step 1 — Freeze the candidate and authority baseline

Record:

- exact candidate ID and declared lifecycle transition;
- exact repository commit and build/run reference;
- candidate artifact inventory and deterministic digests;
- contract, schema, validator, fixture, test, policy, and release-profile
  versions;
- source, evidence, receipt, proof, catalog, review, correction, withdrawal,
  and rollback references;
- active branches, pull requests, migrations, and ownership overlaps; and
- failures or holds that predate this candidate.

Do not continue when the candidate is mutable, incompletely inventoried,
semantically owned by overlapping work, or based on floating aliases.

### Step 2 — Verify source role, rights, sensitivity, and evidence

For every contributing source:

1. resolve the canonical source identity and immutable retrieval/version
   reference;
2. preserve the admitted source role without upcasting;
3. verify rights, license, access, attribution, retention, and redistribution;
4. identify cultural, sovereignty, infrastructure, privacy, precision,
   private-property, and combination-risk obligations;
5. resolve every consequential `EvidenceRef` to an admissible
   `EvidenceBundle`; and
6. record all unresolved support explicitly.

Never use a map edit, observation, candidate, crowd source, generated summary,
or graph projection as legal, regulatory, current-operational, or safe-passage
authority.

### Step 3 — Verify route, membership, time, and geometry semantics

Confirm that:

- a route is not collapsed into a segment, route-membership assertion,
  crossing, facility, operator event, restriction, or graph edge;
- modern, historic, reconstructed, modeled, narrative, candidate, synthetic,
  and generated representations remain distinguishable;
- source, observed, valid, retrieval, build, release, expiry, correction, and
  withdrawal times remain distinct where material;
- geometry has explicit CRS, provenance, precision, uncertainty, and
  reconstruction status;
- public generalization or redaction is separately reviewed and receipted;
- Hydrology, Settlements/Infrastructure, Hazards, Archaeology, People/Land,
  legal, safety, and official-authority claims remain owned by their proper
  lanes; and
- graph/triplet projections remain rebuildable derivatives, never canonical
  truth.

### Step 4 — Run bounded repository validation

Run the commands in [Section 9](#9-repository-native-validation) from the
repository root at the exact candidate ref. Record exact commands, environment,
inputs, outputs, result status, and limitations.

The commands evaluate only synthetic `CorridorRoute` fixtures. They do not
evaluate a real candidate, active policy, proof packet, manifest, public
surface, release, or publication state.

A failure may be classified as inherited only when exact base/head evidence
supports that classification. Do not weaken a schema, validator, negative
fixture, no-network boundary, policy hold, workflow sentinel, or topology
ratchet to obtain a passing result.

### Step 5 — Require a candidate-bound policy result

An eligible candidate needs an accepted evaluator result bound to:

- the exact candidate and digest set;
- the policy bundle identity and version;
- evaluation time and evaluator identity;
- finite outcome, reason codes, labels, and obligations; and
- rights, sensitivity, precision, source role, evidence, and public exposure.

Policy file presence, syntax, README prose, a proposed Rego package, or a green
static workflow is not an operational decision. At the pinned snapshot, the
Roads/Rail/Trade policy runtime remains unverified; keep promotion on `HOLD`.

### Step 6 — Complete accountable review

Verify each required review record against:

- reviewer identity, role, current assignment, and authority interval;
- independence and conflict constraints;
- candidate ID, exact ref, scope, artifact set, and digest binding;
- source-rights, cultural/sovereignty, infrastructure/security, evidence,
  policy, domain, correction, rollback, and public-surface responsibilities;
- review time and review outcome; and
- unresolved obligations or dissent.

Requested review, comments, automated review, workflow success, non-draft PR
state, merge history, and CODEOWNERS routing are not accountable approval.

### Step 7 — Close correction and rollback before release review

Require candidate-bound references for:

- correction intake, decision, supersession, and user-visible correction path;
- affected artifact, catalog, graph, cache, API, map, export, and derived-view
  invalidation;
- prior release target and forward-fix boundary;
- recovery procedure, stop conditions, and accountable roles; and
- rehearsal or other evidence appropriate to the candidate's risk.

A generic rollback document or synthetic test does not prove that a real
candidate can be recovered.

### Step 8 — Audit the public boundary

When the candidate would affect a public surface, verify that:

- ordinary clients use governed APIs or immutable release-approved carriers;
- no RAW, WORK, QUARANTINE, restricted, internal, or unreleased candidate store
  is exposed;
- evidence, source role, time, policy, review, release, correction, and
  withdrawal state remain inspectable;
- denied, withheld, stale, corrected, unavailable, and error states fail safely;
- sensitive precision cannot leak through URLs, logs, tiles, popups, exports,
  screenshots, caches, search, AI context, or deep links; and
- KFM is not presented as current legal, operational, navigation, emergency, or
  safe-passage authority.

If no public implementation and evidence can be inspected, record `UNKNOWN`
and keep the candidate on `HOLD`.

### Step 9 — Reconcile the final preflight result

Apply this precedence:

```text
ERROR > DENY > ABSTAIN > HOLD > READY_FOR_ACCOUNTABLE_RELEASE_REVIEW
```

`HOLD` is a work-state result. It remains mandatory when ownership, authority,
candidate, proof, rights, sensitivity, overlap, review, correction, rollback,
or operational closure is unresolved even if a bounded validator returns
`PASS`.

### Step 10 — Hand off; do not promote

When every applicable precondition is supported, assemble the packet in
[Section 11](#11-candidate-handoff-packet) and hand it to the accountable
release authority. This runbook ends there.

Do not mutate lifecycle stores, manifests, aliases, registries, public carriers,
deployments, caches, or public interfaces from this procedure.

## 9. Repository-native validation

Run from the repository root at the exact candidate ref.

### 9.1 Focused `CorridorRoute` contract and validator tests

```bash
python -m pytest -q tests/schemas/test_corridor_route_contract.py
```

The focused module verifies contract/schema pairing, required fields,
route/segment/membership anti-collapse rules, forbidden authority fields,
deterministic hashing, released-posture closure, source-role constraints,
public-sensitive-geometry denial, synthetic/no-network fixture metadata, and
the validator CLI fixture runner.

### 9.2 Deterministic fixture suite

```bash
python tools/validators/domains/roads-rail-trade/validate_corridor_route.py --fixtures
```

The fixture suite expects one `PASS`, one `ABSTAIN`, and eight `DENY` outcomes.
It succeeds only when each tracked fixture returns its declared expected
result. This is bounded synthetic proof, not a real-candidate evaluation.

### 9.3 Hosted domain workflow

The [domain workflow](../../../.github/workflows/domain-roads-rail-trade.yml)
runs both commands with `KFM_NO_NETWORK=1`. It also:

- verifies required repository boundaries and parses domain schemas/fixtures;
- detects implementation appearing in currently documented validator
  scaffolds so it can be wired deliberately;
- preserves the proposal-oriented domain policy sentinel;
- records broader semantic validation as held;
- records proof production as explicitly skipped and held; and
- records release dry-run as explicitly skipped and held.

A green workflow means those checks and hold sentinels behaved as written at
one SHA. It does not establish route truth, source admission, policy approval,
EvidenceBundle closure, proof, accountable review, release, deployment,
promotion, or publication.

### 9.4 Validation result record

Record at least:

```yaml
repository_ref: <exact-commit-sha>
candidate_id: <stable-id-or-NOT_AVAILABLE>
command: <exact-command>
environment: <runner-and-relevant-pins>
inputs: [<schema-contract-fixture-or-candidate-refs>]
result: PASS | ABSTAIN | DENY | ERROR | NOT_RUN
introduced_failures: [<ids>]
inherited_failures: [<ids-with-base-and-head-evidence>]
limitations: [<what-the-check-does-not-prove>]
```

## 10. Mandatory stop conditions

### Return `HOLD` when

- no immutable candidate dossier exists;
- the candidate lane, proof producer, release dry-run, policy runtime, or
  accountable authority is not established;
- source rights, sensitivity, sovereignty, access, precision, currentness, or
  evidence needs review;
- required ownership, reviewer role, separation, or overlap remains unresolved;
- correction, invalidation, recovery, or rollback support is incomplete; or
- a public implementation cannot be inspected.

### Return `ABSTAIN` when

- a consequential EvidenceRef, source role, time, geometry, identity, rights,
  or authority claim cannot be supported strongly enough for a decision; or
- repository evidence is insufficient to distinguish a safe candidate from an
  unsupported claim.

### Return `DENY` when

- the candidate presents observation, candidate, context, graph, generated, or
  crowd material as legal, regulatory, current-operational, or safe-passage
  authority;
- rights, policy, sensitivity, cultural/sovereignty, infrastructure, or public
  exposure forbids the candidate;
- historic or culturally sensitive geometry is more precise than supported;
- route, segment, membership, facility, operator, restriction, cross-domain,
  or lifecycle authority is collapsed;
- the candidate would expose internal, restricted, quarantined, or unreleased
  material; or
- a lifecycle state would be skipped or inferred from placement.

### Return `ERROR` when

- input cannot be parsed or validated;
- schema, contract, hash, artifact inventory, manifest, receipt, proof, review,
  correction, or rollback declarations contradict each other;
- the accepted evaluator or validator cannot run reproducibly; or
- environment or tooling failure prevents a trustworthy result.

### Return `ESCALATE` when

- the request could affect current transportation operation, emergency
  response, legal access, right-of-way, infrastructure security, protected
  cultural knowledge, or another external authority; or
- unsafe details cannot be reviewed in a public pull request.

## 11. Candidate handoff packet

Store only a public-safe, reference-only dossier under
`release/candidates/roads-rail-trade/`. Keep payloads, source instances,
evidence, proofs, policy, review records, receipts, manifests, correction
notices, rollback cards, and published carriers in their owning roots.

The packet must contain or reference:

1. candidate ID, domain, object family, lifecycle transition, exact ref, run,
   build, version, and artifact inventory;
2. deterministic artifact and specification digests;
3. source descriptors, roles, versions, retrieval identity, rights, access,
   sensitivity, and citations;
4. route/segment/membership/crossing/facility/operator/restriction identity and
   cross-domain ownership notes;
5. temporal, CRS, geometry, topology, precision, reconstruction, uncertainty,
   and public-transform records;
6. EvidenceRefs, EvidenceBundle digests, catalog references, and derived graph
   or triplet references;
7. schema, contract, validator, negative-fixture, test, workflow, and exact-ref
   result records;
8. accepted policy evaluator and bundle identity, result, reasons, and
   obligations;
9. authenticated reviewer roles, assignments, conflicts, independence, and
   candidate-bound review records;
10. correction, invalidation, withdrawal, supersession, recovery, and rollback
    references;
11. public-boundary and non-operational-authority assessment;
12. introduced and inherited failures with exact base/head evidence; and
13. every remaining `UNKNOWN`, `NEEDS VERIFICATION`, `CONFLICTED`, `HOLD`,
    `ABSTAIN`, `DENY`, or `ERROR` finding.

If a value is sensitive, place only a safe opaque identifier and an
access-controlled reference in the dossier. Never copy credentials, temporary
URLs, restricted payloads, exact sensitive coordinates, private facility
detail, rights-holder notes, or vulnerability information into a filename,
commit, pull request, log, or public candidate packet.

## 12. Release handoff

### Valid handoff result

```text
READY_FOR_ACCOUNTABLE_RELEASE_REVIEW
```

Use it only when every applicable preflight item is supported and no stronger
finite result applies. Record the exact candidate, commit, artifact set,
digests, validation evidence, limitations, required reviewers, and remaining
obligations.

### Current repository limitation

At the pinned snapshot, the correct result is `HOLD`: no candidate record,
accepted proof producer, accepted domain release-dry-run command,
candidate-manifest contract, verified policy runtime, or authenticated release
authority was established.

The release authority must use a separately accepted release process. This
runbook does not define, simulate, or invoke that process.

## 13. Correction and rollback

### Before release

If preflight fails, keep the candidate in its current lifecycle state. Record
the finding, correction owner, affected references, and rerun boundary. Do not
create a rollback record for a release that never occurred.

### After a separately authorized release

Use the owning correction and rollback procedures. Preserve immutable prior
versions, supersession lineage, affected EvidenceRefs, public invalidation,
recovery targets, accountable decisions, and user-visible correction state.

The existing Roads/Rail/Trade rollback runbook remains classified by the local
procedure boundary as proposal-heavy. Until its complete command, inputs,
outputs, authority, and recovery evidence are reconciled, it is not operational
rollback proof.

## 14. Acceptance and negative cases

### Documentation acceptance criteria

- [ ] The runbook states `PROMOTION_EXECUTION_HELD`, `NON_RELEASE`,
      `NON_DEPLOYMENT`, and `NON_PUBLICATION` plainly.
- [ ] The candidate lane is not described as containing a real candidate.
- [ ] The bounded `CorridorRoute` profile is the only claimed executable domain
      validation slice.
- [ ] Proof and release-dry-run workflow holds remain visible.
- [ ] `PASS`, `ABSTAIN`, `DENY`, `ERROR`, `HOLD`, review, release, deployment,
      promotion, and publication remain separate.
- [ ] Route, segment, membership, time, geometry, rights, sensitivity,
      cross-domain, correction, and rollback boundaries remain explicit.
- [ ] Commands and links resolve to current repository surfaces.
- [ ] No source, candidate, policy decision, review, release, promotion,
      deployment, or publication is implied by the documentation change.

### Required negative cases for future promotion implementation

Any future real-candidate preflight must fail closed for at least:

- missing or mutable candidate identity;
- artifact or specification digest mismatch;
- unresolved source identity, role, rights, version, or retrieval context;
- observation/candidate/context upcast to legal or regulatory authority;
- route, segment, membership, facility, restriction, or graph-role collapse;
- invalid temporal ordering or stale current-status claim;
- unsupported CRS, precision, historic reconstruction, or geometry lineage;
- missing EvidenceBundle support;
- culturally sensitive or infrastructure-sensitive detail without accountable
  review and public-safe transform;
- graph projection presented as canonical truth;
- missing accepted policy result or policy obligations;
- missing independent review where required;
- missing correction, invalidation, withdrawal, or rollback target;
- public access to internal or unreleased material; and
- any attempted lifecycle skip or public write during preflight.

## 15. Related repository surfaces

- [Local Roads/Rail/Trade procedure boundary](./README.md)
- [Bounded no-network procedure](./NO_NETWORK_TEST_RUNBOOK.md)
- [Roads/Rail/Trade rollback runbook](./ROLLBACK_RUNBOOK.md)
- [Domain boundary](../../domains/roads-rail-trade/README.md)
- [Domain lifecycle](../../domains/roads-rail-trade/DATA_LIFECYCLE.md)
- [Domain sensitivity guidance](../../domains/roads-rail-trade/SENSITIVITY.md)
- [Directory Rules](../../doctrine/directory-rules.md)
- [Lifecycle Law](../../doctrine/lifecycle-law.md)
- [Trust Membrane](../../doctrine/trust-membrane.md)
- [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
- [`CorridorRoute` contract](../../../contracts/domains/roads-rail-trade/corridor_route.md)
- [`CorridorRoute` schema](../../../schemas/contracts/v1/domains/roads-rail-trade/corridor_route.schema.json)
- [CorridorRoute validator](../../../tools/validators/domains/roads-rail-trade/validate_corridor_route.py)
- [Focused CorridorRoute tests](../../../tests/schemas/test_corridor_route_contract.py)
- [Synthetic CorridorRoute fixtures](../../../fixtures/domains/roads-rail-trade/corridor_route/)
- [Domain workflow](../../../.github/workflows/domain-roads-rail-trade.yml)
- [Source-registry boundary](../../../data/registry/sources/roads-rail-trade/README.md)
- [Proof boundary](../../../data/proofs/roads-rail-trade/README.md)
- [Domain policy boundary](../../../policy/domains/roads-rail-trade/README.md)
- [Release-candidate boundary](../../../release/candidates/roads-rail-trade/README.md)

## 16. Open verification backlog

| Item | Evidence required to close it | Current state |
|---|---|---|
| Real candidate contract | Accepted candidate/manifest contracts plus one immutable dossier and artifact inventory | `HOLD` |
| Proof producer | Accepted producer, schemas, source-role controls, fixtures, validators, receipts, access controls, and deterministic tests | `HOLD` |
| Domain release dry-run | Accepted command, candidate-manifest contract, fail-closed fixtures, no-public-write proof, and rollback boundary | `HOLD` |
| Policy runtime | Accepted evaluator path, bundle/version identity, parity proof, candidate binding, finite result, reasons, and obligations | `NEEDS VERIFICATION` |
| Accountable roles | Current domain, source, rights, cultural/sovereignty, infrastructure/security, evidence/policy, rollback, and release assignments | `NEEDS VERIFICATION` |
| Full semantic validation | Executable crossing, bridge/river-crossing, facility, source-role, catalog, graph, evidence, public-safety, and release profiles | `HOLD` |
| Public boundary | Governed API or immutable released-carrier implementation, access control, redaction/generalization, correction, and degraded-state evidence | `UNKNOWN` |
| Operational recovery | Candidate-bound correction, invalidation, rollback, recovery, and rehearsal evidence | `HOLD` |
| `roads-rail-trade` / `transport` convergence | Accepted ADR and migration plan resolving the documented naming/authority split | `CONFLICTED / HOLD` |

## 17. Runbook maintenance and documentation rollback

Re-review this runbook when a candidate appears, the domain workflow changes,
a proof producer or release-dry-run command is accepted, policy runtime becomes
executable, accountable roles change, a release contract is adopted, a public
surface is added, or correction/rollback evidence changes.

For a future edit:

1. freeze the exact default-branch commit and relevant blobs;
2. inspect the local procedure boundary, candidate lane, workflow, validator,
   tests, policy, proof, review, correction, rollback, and public surfaces;
3. update only claims supported at that exact snapshot;
4. check headings, anchors, code fences, tables, and relative links;
5. review the complete diff for unrelated churn; and
6. preserve the terminal authority boundary unless a separately accepted
   decision and implementation prove a later state.

Before merge, close the draft pull request and delete only its feature branch.
After merge, revert the documentation commit or submit a reviewed forward
correction. Either action changes documentation only; it does not undo source
admission, evidence, policy, lifecycle, release, deployment, promotion, or
publication state.

[Back to top](#top)
