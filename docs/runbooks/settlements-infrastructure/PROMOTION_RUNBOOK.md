<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook/settlements-infrastructure/promotion
title: Settlements and Infrastructure Promotion Preflight Runbook
type: standard
version: v2.0
prior_state: proposal-heavy May 2026 promotion procedure with unverified gates, commands, artifacts, roles, signing, release execution, and public-surface claims
status: draft; repository-grounded; PROMOTION_EXECUTION_HELD; BOUNDED_STATIC_READINESS; BOUNDED_EVIDENCEBUNDLE_SCHEMA_CONVERGENCE; NON_RELEASE; NON_DEPLOYMENT; NON_PUBLICATION
owners:
  - "@bartytime4life — verified GitHub review route"
  - "NEEDS VERIFICATION — accountable Settlements/Infrastructure, municipal-source, infrastructure-security, cultural, sovereignty, evidence, policy, correction, rollback, and release assignments"
created: 2026-05-12
updated: 2026-08-29
policy_label: repository-facing; critical-infrastructure-sensitive; cultural-and-sovereignty-sensitive; fail-closed
current_path: docs/runbooks/settlements-infrastructure/PROMOTION_RUNBOOK.md
owning_root: docs/
responsibility: human promotion preflight and accountable-review handoff for the Settlements/Infrastructure lane
truth_posture: cite-or-abstain
authority_class: explanatory operational documentation
authority_rank: subordinate to accepted doctrine and ADRs, contracts, schemas, source records, policy, evidence, lifecycle, review, release, correction, rollback, and competent official authorities
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: c00096f904c66053938355e52f4a5cb9402be6a4
  target_before_update_blob: f848e5336d7d013b7221334b5a416cf317a76c4f
  local_runbook_boundary_blob: 0ab5135c16dae9eeda177921a89a18897ad41cf3
  domain_workflow_blob: a47d89c40efd58ac31bc44dbc56bdfb1ccc3a325
  convergence_workflow_blob: 584ac26dcaf5791b1a560cb71bd059e889f55791
  no_network_runbook_blob: 90133c88ddf2d053a9ca1021e1951e2b241a4ebd
  domain_projection_schema_blob: 44c022ffc7f24cc582b061c5f3145b716e3f150f
  shared_evidence_bundle_schema_blob: cf5256831b63dca46a5f68b168441adcf68b8751
  projection_validator_blob: 407c99ad07442e0b4802d057b695e391bdf4f8eb
  convergence_tests_blob: d1cfa0e9064e250dc3d157372d0091ae835d05c1
  candidate_lane_blob: 3594fb43ab481d39697deb41790d484f9782fec2
  proof_lane_blob: 08c0f3bd93a81f7960d7de77d2b8087a213e67ed
  policy_lane_blob: 792a67caab14d119cf4a21dee1365216bfaefb11
  rollback_runbook_blob: 9ac8e114bc18ac5b7a63033e60fdf3559e87ee2b
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adoption_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  candidate_records_observed: 0
  bounded_static_readiness_profiles: 1
  bounded_schema_convergence_profiles: 1
  executable_domain_semantic_validator_profiles: 0
related:
  - ./README.md
  - ./NO_NETWORK_TEST_RUNBOOK.md
  - ./ROLLBACK_RUNBOOK.md
  - ./SOURCE_REFRESH_RUNBOOK.md
  - ../../domains/settlements-infrastructure/README.md
  - ../../domains/settlements-infrastructure/CANONICAL_PATHS.md
  - ../../domains/settlements-infrastructure/IDENTITY_MODEL.md
  - ../../domains/settlements-infrastructure/SENSITIVITY.md
  - ../../doctrine/directory-rules.md
  - ../../doctrine/lifecycle-law.md
  - ../../doctrine/trust-membrane.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../.github/CODEOWNERS
  - ../../../.github/workflows/domain-settlements-infrastructure.yml
  - ../../../.github/workflows/settlements-infrastructure-evidence-bundle-convergence.yml
  - ../../../schemas/contracts/v1/domains/settlements-infrastructure/evidence_bundle.schema.json
  - ../../../schemas/contracts/v1/evidence/evidence_bundle.schema.json
  - ../../../fixtures/contracts/v1/evidence/evidence_bundle/
  - ../../../tools/validators/validate_settlements_infrastructure_evidence_bundle_projection.py
  - ../../../tests/validators/domains/settlements-infrastructure/test_evidence_bundle_schema_convergence.py
  - ../../../tests/domains/settlements-infrastructure/README.md
  - ../../../tools/validators/domains/settlements-infrastructure/README.md
  - ../../../policy/domains/settlements-infrastructure/README.md
  - ../../../data/registry/sources/settlements-infrastructure/README.md
  - ../../../data/proofs/settlements-infrastructure/README.md
  - ../../../data/published/settlements-infrastructure/README.md
  - ../../../release/candidates/settlements-infrastructure/README.md
notes:
  - "v2.0 replaces proposal-era promotion execution with a current-repository preflight and accountable-review handoff."
  - "The current repository contains no Settlements/Infrastructure candidate record; the candidate lane contains README.md only."
  - "The only bounded executable content used here is static readiness plus EvidenceBundle schema-projection convergence over shared synthetic fixtures."
  - "Domain semantic validation, active policy evaluation, proof production, release dry-run, operational rollback, release, deployment, promotion, and publication remain held."
  - "Connected Drive and Notion material was consulted as planning lineage and coordination context; current GitHub evidence controls current-behavior claims."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Settlements and Infrastructure Promotion Preflight Runbook

Prepare, validate, and hand off one Settlements/Infrastructure candidate for
accountable review without creating municipal truth, infrastructure truth,
operational authority, release authority, promotion authority, deployment
authority, or publication state.

> [!WARNING]
> KFM is not an emergency, public-safety, utility-service, infrastructure-
> condition, municipal-law, land-use, planning, inspection, security, legal, or
> regulatory authority. Stop if the requested work could be mistaken for a
> current legal-incorporation finding, facility-safety finding, service-
> availability guarantee, access instruction, emergency decision, or disclosure
> of protected infrastructure detail.

> [!IMPORTANT]
> **Current result: `HOLD`.** The repository contains no
> Settlements/Infrastructure candidate record. Its domain workflow records that
> semantic validation, proof production, and release dry-run are not
> established. The only executable evidence is bounded static readiness and
> no-network-compatible `EvidenceBundle` schema-projection convergence over
> shared synthetic fixtures. This runbook stops at preflight and accountable
> review handoff.

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
Settlements/Infrastructure transition from `CATALOG` or `TRIPLETS` toward
`PUBLISHED`. It helps a maintainer determine whether one immutable candidate is
supported well enough for accountable release review.

### In scope

- freeze one candidate identity, exact repository ref, artifact inventory, and
  digest set;
- verify source role, rights, legal and statistical place roles, sensitivity,
  time, geometry, uncertainty, evidence, validation, policy, review,
  correction, and rollback references;
- run the repository's bounded static-readiness and EvidenceBundle
  schema-convergence checks at the exact reviewed ref;
- record `PASS`, `ABSTAIN`, `DENY`, `ERROR`, and workflow `HOLD` results
  without collapsing them into release state;
- produce a public-safe, reference-only candidate dossier; and
- hand a complete packet to separately authenticated accountable reviewers.

### Out of scope

- source discovery, live retrieval, source admission, or connector operation;
- creating or changing municipality, census-place, townsite, community,
  facility, operator, condition, service, dependency, access, or safety truth;
- moving payloads between lifecycle lanes;
- issuing an operational policy decision or authenticating a reviewer;
- assembling a real proof packet, signature, release manifest, or published
  carrier;
- changing a governed API, map, graph, tile, export, Focus Mode, deployment, or
  runtime surface; and
- approving, releasing, deploying, promoting, publishing, or activating data.

## 2. Authority and terminal boundary

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
adopts the [Directory Rules](../../doctrine/directory-rules.md). Those rules
place human operational procedures under `docs/runbooks/`, candidate dossiers
under `release/candidates/`, release decisions under the appropriate
`release/` object-family lane, proof support under `data/proofs/`, and released
public-safe carriers under `data/published/`.

This file therefore explains a procedure. It is not a source descriptor,
contract, schema, policy rule, EvidenceBundle, proof, review record, promotion
decision, release manifest, rollback card, correction notice, receipt,
signature, published carrier, or operational instruction from a competent
external authority.

Directory placement does not grant truth, rights clearance, review, release,
or publication status. Promotion emits a new governed state or version; it is
never inferred from a copy, move, filename, workflow completion, green check,
pull-request state, merge, deployment, or mutable alias.

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
| Runbook path | This file already exists below `docs/runbooks/settlements-infrastructure/` | **CONFIRMED.** Same-path replacement is valid; no new documentation home is required. |
| Local procedure boundary | `docs/runbooks/settlements-infrastructure/README.md` classifies the prior promotion runbook as proposal-heavy | **CONFIRMED stale procedure.** Replace unverified execution claims with this preflight boundary. |
| Candidate lane | `release/candidates/settlements-infrastructure/` contains `README.md` only | **CONFIRMED / ABSENT candidate.** No real candidate can advance. |
| Static readiness | `.github/workflows/domain-settlements-infrastructure.yml` checks required paths, parses tracked JSON, classifies placeholder posture, and uses read-only permissions | **CONFIRMED / BOUNDED.** It records readiness and explicit holds; it does not execute domain semantic validators. |
| EvidenceBundle projection convergence | A proposed domain projection, shared EvidenceBundle schema, shared fixtures, validator wrapper, three focused tests, and a separate workflow exist | **CONFIRMED / BOUNDED.** They prove shape delegation and selected fixture behavior only. |
| Direct domain semantics | The local boundary records seven docstring-only test modules, one `assert True` smoke test, four `NotImplementedError` validator scripts, and a stub domain-fixture README | **CONFIRMED placeholder posture.** No substantive domain semantic validation is established. |
| Policy | The domain policy lane contains experimental source scaffolds and explicitly remains evaluator-unbound | **CONFIRMED presence / PARTIAL.** File presence is not an accepted candidate-bound policy result. |
| Proof production | The domain workflow reports no accepted deterministic proof producer or command | **CONFIRMED / HOLD.** A green held job is not an EvidenceBundle or proof. |
| Release dry-run | The domain workflow reports no accepted domain release-dry-run command or candidate-manifest contract | **CONFIRMED / HOLD.** The job performs no release, promotion, or public write. |
| Review routing | `CODEOWNERS` routes GitHub review to `@bartytime4life` | **CONFIRMED route / INSUFFICIENT authority.** Routing is not domain, source-rights, infrastructure-security, cultural, sovereignty, policy, rollback, release, or independent approval. |
| Operational rollback | The adjacent rollback runbook remains proposal-heavy and no candidate-bound recovery proof is established | **CONFIRMED documentation / HOLD.** Do not report operational rollback capability. |
| Public boundary | Repository documentation identifies governed-interface and public-safe-carrier requirements, but a complete candidate-bound public implementation was not established in this review | **UNKNOWN / HOLD.** Do not infer exposure, release, deployment, or publication readiness. |

### Current finite result

```yaml
work_state: HOLD
reason_codes:
  - SI_CANDIDATE_ABSENT
  - SI_DOMAIN_SEMANTIC_VALIDATION_UNESTABLISHED
  - SI_PROOF_PRODUCER_UNESTABLISHED
  - SI_RELEASE_DRY_RUN_UNESTABLISHED
  - SI_POLICY_RUNTIME_UNVERIFIED
  - SI_ACCOUNTABLE_REVIEW_AUTHORITY_UNVERIFIED
  - SI_OPERATIONAL_ROLLBACK_UNESTABLISHED
terminal_boundary: ACCOUNTABLE_REVIEW_HANDOFF_ONLY
promotion_execution: HELD
release: NOT_PERFORMED
deployment: NOT_PERFORMED
publication: NOT_PERFORMED
```

These reason codes are explanatory documentation labels, not an accepted
machine enum.

## 4. State and outcome vocabulary

Keep validator result, workflow or work state, review state, promotion
decision, release state, deployment state, and publication state separate.

| Term | Meaning here | Authority effect |
|---|---|---|
| `PASS` | The invoked bounded check found no violation in its declared profile | No lifecycle or release change |
| `ABSTAIN` | Required support is unresolved and a stronger result is not justified | Candidate does not advance |
| `DENY` | A prohibited, unsafe, contradictory, or release-without-closure state was detected | Candidate does not advance |
| `ERROR` | A trustworthy evaluation could not complete | Result is unusable until repaired and rerun |
| `HOLD` | Ownership, authority, rights, sensitivity, overlap, candidate, proof, policy, review, correction, rollback, or operational closure is unresolved | Work remains in its prior state |
| `READY_FOR_ACCOUNTABLE_RELEASE_REVIEW` | Every applicable preflight item is supported and the dossier is reviewable | Still not approval or release |
| `APPROVED` | An authenticated accountable authority approved the exact candidate under an accepted decision contract | Not emitted by this runbook |
| `PUBLISHED` | A separately authorized release decision activated an immutable public-safe carrier | Not emitted by this runbook |

`ESCALATE` is a routing action for competent external or protected review. It
is not a substitute for an accepted policy or release result.

The EvidenceBundle convergence profile's successful outcome is evidence for one
bounded schema profile. Do not translate it into domain truth, policy approval,
review completion, proof, promotion, release, deployment, or publication.

## 5. Preconditions

A candidate is eligible for this preflight only when every applicable item is
bound to an immutable or versioned object. Missing support produces `HOLD`,
`ABSTAIN`, `DENY`, or `ERROR`; it never produces partial promotion.

| # | Required support | Minimum evidence | Default if unresolved |
|---:|---|---|---|
| 1 | Exact candidate identity | Candidate ID, domain, object family, exact repository or build ref, version, artifact inventory, and deterministic digests | `HOLD` or `DENY` |
| 2 | Lifecycle boundary | Prior state and proposed transition are explicit; no skipped state or file-move inference | `DENY` |
| 3 | Canonical source descriptors | Stable source IDs, roles, rights, access, sensitivity, citation, cadence, version, and retrieval identity | `ABSTAIN`, `HOLD`, or `DENY` |
| 4 | Place-role separation | Legal municipality, census place, named place, historic townsite, community, reservation community, post office, and map label remain distinct | `DENY` |
| 5 | Infrastructure-role separation | Asset, facility, network node, network segment, operator, condition observation, service area, dependency, and public representation remain distinct | `DENY` |
| 6 | Time and freshness | Source, observed, valid, legal-effective, census-vintage, retrieval, build, release, expiry, correction, and withdrawal times are distinguished where material | `ABSTAIN`, `HOLD`, or `DENY` |
| 7 | Geometry and uncertainty | CRS, topology, precision, lineage, reconstruction status, uncertainty, and public transform are supported | `ABSTAIN`, `HOLD`, or `DENY` |
| 8 | Rights and sensitivity | Redistribution basis and infrastructure, cultural, sovereignty, archaeology, living-person, private-property, precision, and combination-risk obligations are resolved | `HOLD` or `DENY` |
| 9 | Evidence closure | Every consequential `EvidenceRef` resolves to an admissible candidate-scoped `EvidenceBundle` | `ABSTAIN` or `DENY` |
| 10 | Catalog and projection closure | Catalog and optional triplet or graph projections are reproducible and remain derived | `HOLD` or `DENY` |
| 11 | Policy result | Accepted evaluator identity, policy bundle and version, candidate binding, finite outcome, reasons, and obligations | `HOLD`, `DENY`, or `ERROR` |
| 12 | Validation closure | Applicable schemas, validators, negative fixtures, tests, and exact-ref results are complete | `HOLD`, `DENY`, or `ERROR` |
| 13 | Accountable review | Authenticated roles, current assignments, scope binding, conflicts, independence, time, and required specialist review | `HOLD` or `ABSTAIN` |
| 14 | Correction and rollback | Correction path, invalidation scope, prior target, recovery procedure, and rollback evidence are candidate-bound | `HOLD` or `DENY` |
| 15 | Public boundary | Public consumers use governed interfaces or released carriers; no internal, restricted, candidate, or mutable store is exposed | `DENY` |
| 16 | Overlap and ownership | No active branch, pull request, migration, or steward work owns the same candidate or authority surface | `HOLD` |

## 6. Preflight check matrix

The prior runbook described a seven-gate implementation as though
Settlements/Infrastructure release execution were established. Current
repository evidence supports only static readiness and EvidenceBundle schema
convergence. Use this matrix as a human checklist; it is **not** an accepted
machine enum and must not be reported as an executed release gate.

| Check family | Required closure | Current lane disposition |
|---|---|---|
| Placement and identity | Candidate dossier is in the candidate lane; payloads remain in their owning lifecycle roots; identities and digests are immutable | `HOLD` — no candidate record |
| Sources, roles, and evidence | Source identity, legal or statistical role, rights, retrieval context, citations, EvidenceRefs, and EvidenceBundles close without upcasting | `HOLD` — real candidate support absent |
| Domain semantics, time, and geometry | Place and infrastructure object families, temporal roles, freshness, CRS, precision, reconstruction, uncertainty, and transform lineage are coherent | `HOLD` — semantic profile not established |
| Rights, sensitivity, and cross-domain authority | Critical infrastructure, cultural and sovereignty context, archaeology, private property, living-person proximity, harmful precision, and combination risks are resolved by the correct owners | `HOLD` — accountable roles and transforms unverified |
| Policy and validation | Accepted candidate-bound policy result plus applicable schema, validator, negative-fixture, and test evidence | `HOLD` — schema-convergence profile only; policy runtime unverified |
| Review, correction, and rollback | Authenticated independent review where required, explicit obligations, correction lineage, rollback target, and recovery evidence | `HOLD` — authority and operational closure unverified |
| Release and public boundary | Accepted release process, manifest contract, governed consumers, public-safe carrier, degraded states, and no-internal-store exposure | `HOLD` — release dry-run and candidate-bound public proof unestablished |

## 7. Roles and separation of duties

Do not infer an actor's authority from a filename, commit author, requested
review, CODEOWNERS route, workflow identity, repository permission, or earlier
assistant-generated role label.

| Role | Required responsibility | Current status |
|---|---|---|
| Candidate author | Assemble immutable references and disclose all known gaps; never self-create approval | `UNKNOWN` until a candidate exists |
| Domain steward | Confirm Settlements/Infrastructure semantics, identity, time, and cross-domain boundaries | `NEEDS VERIFICATION` |
| Municipal and source-rights reviewer | Confirm legal or statistical source role, source identity, rights, access, attribution, cadence, and redistribution | `NEEDS VERIFICATION` |
| Infrastructure-security reviewer | Review critical facilities, dependency disclosure, harmful precision, private access, condition detail, and combination risk | `NEEDS VERIFICATION` |
| Cultural and sovereignty reviewer | Review Tribal, treaty, reservation-community, cultural-place, oral-history, sacred, and steward-controlled knowledge where applicable | `NEEDS VERIFICATION` |
| Evidence and policy reviewer | Confirm EvidenceRef-to-EvidenceBundle closure and accepted candidate-bound policy evaluation | `NEEDS VERIFICATION` |
| Correction and rollback reviewer | Confirm correction, invalidation, rollback target, recovery procedure, and rehearsal evidence appropriate to risk | `NEEDS VERIFICATION` |
| Release authority | Decide the exact release under an accepted contract after all required reviews | `NEEDS VERIFICATION`; outside this runbook |

For policy-significant, rights-sensitive, precision-sensitive,
infrastructure-sensitive, first-source, or first-public-surface work, the
candidate author must not self-approve. If required independent authority
cannot be authenticated, return `HOLD`.

## 8. Procedure

### Step 0 — Stop at the official-authority and safety boundary

Confirm that the request is not asking KFM to determine or change current
legal incorporation, zoning, facility condition, utility availability, service
continuity, public access, emergency response, safe passage, security posture,
inspection status, or regulatory status. If it is, stop, preserve repository
and candidate state, and refer the question to the competent official
authority.

Record either `SI_NON_OPERATIONAL_BOUNDARY_CONFIRMED` or the reason for
`DENY` or `ESCALATE`.

### Step 1 — Freeze the candidate and authority baseline

Record:

- exact candidate ID and declared lifecycle transition;
- exact repository commit and build or run reference;
- candidate artifact inventory and deterministic digests;
- contract, schema, validator, fixture, test, policy, and release-profile
  versions;
- source, evidence, receipt, proof, catalog, review, correction, withdrawal,
  and rollback references;
- active branches, pull requests, migrations, and ownership overlaps; and
- failures or holds that predate this candidate.

Do not continue when the candidate is mutable, incompletely inventoried,
semantically owned by overlapping work, or based on floating aliases.

### Step 2 — Verify sources, roles, rights, and evidence

For every contributing source:

1. resolve the canonical source identity and immutable retrieval or version
   reference;
2. preserve the admitted source role without upcasting;
3. verify rights, license, access, attribution, retention, and redistribution;
4. distinguish legal municipality authority, census or statistical geography,
   gazetteer naming, historic reconstruction, operator reporting, observation,
   model, aggregate, context, and synthetic support;
5. resolve every consequential `EvidenceRef` to an admissible
   `EvidenceBundle`; and
6. record all unresolved support explicitly.

Never use a map edit, census label, gazetteer name, facility record,
observation, candidate, generated summary, graph projection, or crowd source as
legal, regulatory, current-operational, ownership, service-availability, or
safety authority.

### Step 3 — Verify identity, time, geometry, and sensitivity

Confirm that:

- municipality, census place, named place, historic townsite, community,
  reservation community, post office, and map label remain distinguishable;
- asset, facility, node, segment, operator, condition observation, service
  area, dependency, and public representation remain distinguishable;
- modern, historic, reconstructed, modeled, narrative, candidate, synthetic,
  and generated representations are labeled;
- source, observed, valid, legal-effective, census-vintage, retrieval, build,
  release, expiry, correction, and withdrawal times remain distinct where
  material;
- geometry has explicit CRS, provenance, precision, uncertainty, and
  reconstruction status;
- public generalization, aggregation, omission, redaction, or delay is
  separately reviewed and receipted;
- Roads/Rail/Trade, Hazards, Hydrology, Archaeology, People/DNA/Land, legal,
  emergency, safety, and regulatory claims remain owned by their proper lanes
  or authorities; and
- graph, tile, search, map, and summary projections remain rebuildable
  derivatives rather than canonical truth.

### Step 4 — Run bounded repository validation

Run the commands in [Section 9](#9-repository-native-validation) from the
repository root at the exact candidate ref. Record exact commands, environment,
inputs, outputs, result status, and limitations.

These checks evaluate repository shape and shared synthetic EvidenceBundle
fixtures. They do not evaluate a real candidate, legal status, active source,
domain semantics, active policy, proof packet, release manifest, public
surface, release, deployment, or publication state.

A failure may be classified as inherited only when exact base and head
evidence supports that classification. Do not weaken a schema, negative
fixture, no-network boundary, policy hold, workflow sentinel, or topology
ratchet to obtain a passing result.

### Step 5 — Require a candidate-bound policy result

An eligible candidate needs an accepted evaluator result bound to:

- the exact candidate and digest set;
- the policy bundle identity and version;
- evaluation time and evaluator identity;
- finite outcome, reason codes, labels, and obligations; and
- source role, rights, sensitivity, precision, evidence, and public exposure.

Policy file presence, syntax, README prose, proposed Rego, or a green static
workflow is not an operational decision. At the pinned snapshot, the
Settlements/Infrastructure policy lane remains experimental and
evaluator-unbound; keep promotion on `HOLD`.

### Step 6 — Complete accountable review

Verify each required review record against:

- reviewer identity, role, current assignment, and authority interval;
- independence and conflict constraints;
- candidate ID, exact ref, scope, artifact set, and digest binding;
- municipal or source-rights, infrastructure-security, cultural or
  sovereignty, evidence, policy, domain, correction, rollback, and public-
  surface responsibilities;
- review time and review outcome; and
- unresolved obligations or dissent.

Requested review, comments, automated review, workflow success, non-draft
pull-request state, merge history, and CODEOWNERS routing are not accountable
approval.

### Step 7 — Close correction and rollback before release review

Require candidate-bound references for:

- correction intake, decision, supersession, and user-visible correction path;
- affected artifact, catalog, graph, cache, API, map, export, search, and
  derived-view invalidation;
- prior release target and forward-fix boundary;
- recovery procedure, stop conditions, and accountable roles; and
- rehearsal or other evidence appropriate to the candidate's risk.

A generic rollback document or synthetic check does not prove that a real
candidate can be recovered.

### Step 8 — Audit the public boundary

When the candidate would affect a public surface, verify that:

- ordinary clients use governed APIs or immutable release-approved carriers;
- no RAW, WORK, QUARANTINE, restricted, internal, or unreleased candidate store
  is exposed;
- evidence, source role, time, policy, review, release, correction, and
  withdrawal state remain inspectable;
- denied, withheld, stale, corrected, unavailable, and error states fail
  safely;
- sensitive precision cannot leak through URLs, logs, tiles, popups, exports,
  screenshots, caches, search, AI context, or deep links; and
- KFM is not presented as current legal, operational, emergency, safety,
  engineering, planning, inspection, service, or regulatory authority.

If the candidate-bound public implementation cannot be inspected, record
`UNKNOWN` and keep the candidate on `HOLD`.

### Step 9 — Reconcile the final preflight result

Apply this precedence:

```text
ERROR > DENY > ABSTAIN > HOLD > READY_FOR_ACCOUNTABLE_RELEASE_REVIEW
```

`HOLD` is a work-state result. It remains mandatory when ownership, authority,
candidate, proof, rights, sensitivity, overlap, review, correction, rollback,
or operational closure is unresolved even when a bounded check returns
`PASS`.

### Step 10 — Hand off; do not promote

When every applicable precondition is supported, assemble the packet in
[Section 11](#11-candidate-handoff-packet) and hand it to the accountable
release authority. This runbook ends there.

Do not mutate lifecycle stores, manifests, aliases, registries, public
carriers, deployments, caches, or public interfaces from this procedure.

## 9. Repository-native validation

Run from the repository root at the exact reviewed ref.

### 9.1 Static readiness classification

The domain workflow invokes:

```bash
python tools/validators/ci_readiness.py \
  --label "Settlements/Infrastructure" \
  --test-root tests/domains/settlements-infrastructure \
  --validator-root tools/validators/domains/settlements-infrastructure \
  --validator-root tools/validators/facilities \
  --validator-root tools/validators/hazard-exposure
```

The workflow also checks required paths, parses tracked JSON schemas and
fixtures, verifies expected policy wording, rejects unexpected proof or
candidate material, and records explicit holds.

The helper classifies repository readiness. It does not execute the placeholder
domain test modules or validator scripts and does not establish domain truth,
policy approval, evidence closure, proof, release, or publication.

### 9.2 Guarded EvidenceBundle projection convergence

Use the complete guarded local procedure in the
[No-Network Test Runbook](./NO_NETWORK_TEST_RUNBOOK.md). Its two focused
profile commands are:

```bash
python -m unittest discover \
  --start-directory tests/validators/domains/settlements-infrastructure \
  --pattern 'test_evidence_bundle_schema_convergence.py' \
  --verbose
python tools/validators/validate_settlements_infrastructure_evidence_bundle_projection.py --fixtures
```

The focused test module contains three tests. It checks that the proposed
domain projection delegates shape to the shared schema, that the shared schema
remains closed with ten required top-level fields, and that one representative
valid fixture is accepted while one representative invalid fixture is
rejected. The validator command replays all two valid and three invalid shared
fixtures.

The separate convergence workflow sets `KFM_NO_NETWORK=1` but does not inject
the shared Python startup guard into `PYTHONPATH`. The environment variable
alone is not proof of process-wide, runner-wide, operating-system, non-Python,
or dependency-install egress denial. Follow the no-network runbook for guarded
local execution and record its limitations.

### 9.3 Hosted workflow interpretation

At an exact commit, a green domain workflow means its structural checks and
hold sentinels behaved as written. A green convergence workflow means the
declared schema-convergence checks passed over tracked synthetic fixtures.

Neither result establishes:

- municipality or historic-place identity;
- facility existence, ownership, operator, condition, capacity, service,
  dependency, access, or safety;
- source admission, rights, freshness, or current legal authority;
- active policy evaluation, accountable review, EvidenceBundle materialization,
  proof production, catalog closure, release readiness, or rollback recovery;
- governed API, map, graph, export, Focus Mode, deployment, promotion, or
  publication behavior.

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
- semantic domain validation, a proof producer, a release dry-run, policy
  runtime, accountable authority, or operational rollback is not established;
- source rights, sensitivity, sovereignty, access, precision, currentness, or
  evidence needs review;
- required ownership, reviewer role, separation, or overlap remains
  unresolved;
- correction, invalidation, recovery, or rollback support is incomplete; or
- a candidate-bound public implementation cannot be inspected.

### Return `ABSTAIN` when

- a consequential EvidenceRef, source role, time, geometry, identity, rights,
  or authority claim cannot be supported strongly enough for a decision; or
- repository evidence is insufficient to distinguish a safe candidate from an
  unsupported claim.

### Return `DENY` when

- a census, gazetteer, map, archive, crowd source, generated summary, or graph
  projection is presented as legal municipal authority without suitable
  evidence;
- a facility record is presented as ownership, operation, condition, capacity,
  availability, safe access, or current service authority without suitable
  support;
- rights, policy, sensitivity, cultural or sovereignty, infrastructure,
  privacy, or public exposure forbids the candidate;
- exact facility, dependency, condition, private-property, cultural,
  archaeological, or living-person detail is more precise than supported;
- place roles, infrastructure roles, cross-domain authority, or lifecycle
  state are collapsed;
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

- the request could affect current emergency response, legal status, public
  safety, utility operation, facility security, infrastructure vulnerability,
  protected cultural or sovereignty knowledge, or another competent
  authority; or
- unsafe details cannot be reviewed in a public pull request.

## 11. Candidate handoff packet

Store only a public-safe, reference-only dossier under
`release/candidates/settlements-infrastructure/`. Keep payloads, source
instances, evidence, proofs, policy, review records, receipts, manifests,
correction notices, rollback cards, and published carriers in their owning
roots.

The packet must contain or reference:

1. candidate ID, domain, object family, lifecycle transition, exact ref, run,
   build, version, and artifact inventory;
2. deterministic artifact and specification digests;
3. source descriptors, roles, versions, retrieval identity, rights, access,
   sensitivity, and citations;
4. legal, census, historic, community, facility, network, operator, condition,
   service, dependency, and cross-domain identity notes;
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
12. introduced and inherited failures with exact base and head evidence; and
13. every remaining `UNKNOWN`, `NEEDS VERIFICATION`, `CONFLICTED`, `HOLD`,
    `ABSTAIN`, `DENY`, or `ERROR` finding.

If a value is sensitive, place only a safe opaque identifier and an
access-controlled reference in the dossier. Never copy credentials, temporary
URLs, restricted payloads, exact sensitive coordinates, facility interiors,
dependency topology, condition or vulnerability detail, private-person data,
rights-holder notes, or reconstructive clues into a filename, commit, pull
request, log, or public candidate packet.

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
semantic domain validator profile, accepted proof producer, accepted domain
release-dry-run command, candidate-manifest contract, verified policy runtime,
authenticated release authority, or operational rollback proof was
established.

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

The existing
[Settlements/Infrastructure rollback runbook](./ROLLBACK_RUNBOOK.md) remains
proposal-heavy. Until its complete commands, inputs, outputs, authority,
candidate binding, and recovery evidence are reconciled, it is not operational
rollback proof.

## 14. Acceptance and negative cases

### Documentation acceptance criteria

- [ ] The runbook states `PROMOTION_EXECUTION_HELD`, `NON_RELEASE`,
      `NON_DEPLOYMENT`, and `NON_PUBLICATION` plainly.
- [ ] The candidate lane is not described as containing a real candidate.
- [ ] Static readiness and EvidenceBundle schema convergence are the only
      claimed executable profiles.
- [ ] Semantic-validation, proof-production, and release-dry-run holds remain
      visible.
- [ ] `PASS`, `ABSTAIN`, `DENY`, `ERROR`, `HOLD`, review, release, deployment,
      promotion, and publication remain separate.
- [ ] Legal, census, historic-place, object-family, time, geometry, rights,
      sensitivity, cross-domain, correction, and rollback boundaries remain
      explicit.
- [ ] Commands and links resolve to current repository surfaces.
- [ ] No source, candidate, policy decision, review, release, promotion,
      deployment, or publication is implied by the documentation change.

### Required negative cases for future promotion implementation

Any future real-candidate preflight must fail closed for at least:

- missing or mutable candidate identity;
- artifact or specification digest mismatch;
- unresolved source identity, role, rights, version, or retrieval context;
- census, gazetteer, archive, map, or generated evidence upcast to legal
  authority;
- place-role, facility, operator, condition, service, dependency, or graph-role
  collapse;
- invalid temporal ordering or stale current-status claim;
- unsupported CRS, precision, historic reconstruction, or geometry lineage;
- missing EvidenceBundle support;
- culturally sensitive, sovereignty-sensitive, private, archaeological,
  living-person, critical-infrastructure, condition, or dependency detail
  without accountable review and public-safe transformation;
- graph, tile, map, index, or generated narrative presented as canonical truth;
- missing accepted policy result or policy obligations;
- missing independent review where required;
- missing correction, invalidation, withdrawal, or rollback target;
- public access to internal or unreleased material; and
- any attempted lifecycle skip or public write during preflight.

## 15. Related repository surfaces

- [Local Settlements/Infrastructure procedure boundary](./README.md)
- [Guarded no-network schema-convergence procedure](./NO_NETWORK_TEST_RUNBOOK.md)
- [Settlements/Infrastructure rollback runbook](./ROLLBACK_RUNBOOK.md)
- [Settlements/Infrastructure source-refresh runbook](./SOURCE_REFRESH_RUNBOOK.md)
- [Domain boundary](../../domains/settlements-infrastructure/README.md)
- [Canonical-path guidance](../../domains/settlements-infrastructure/CANONICAL_PATHS.md)
- [Identity model](../../domains/settlements-infrastructure/IDENTITY_MODEL.md)
- [Sensitivity guidance](../../domains/settlements-infrastructure/SENSITIVITY.md)
- [Directory Rules](../../doctrine/directory-rules.md)
- [Lifecycle Law](../../doctrine/lifecycle-law.md)
- [Trust Membrane](../../doctrine/trust-membrane.md)
- [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
- [CODEOWNERS](../../../.github/CODEOWNERS)
- [Domain readiness workflow](../../../.github/workflows/domain-settlements-infrastructure.yml)
- [EvidenceBundle convergence workflow](../../../.github/workflows/settlements-infrastructure-evidence-bundle-convergence.yml)
- [Domain EvidenceBundle projection](../../../schemas/contracts/v1/domains/settlements-infrastructure/evidence_bundle.schema.json)
- [Shared EvidenceBundle schema](../../../schemas/contracts/v1/evidence/evidence_bundle.schema.json)
- [Shared EvidenceBundle fixtures](../../../fixtures/contracts/v1/evidence/evidence_bundle/README.md)
- [Projection validator](../../../tools/validators/validate_settlements_infrastructure_evidence_bundle_projection.py)
- [Focused convergence tests](../../../tests/validators/domains/settlements-infrastructure/test_evidence_bundle_schema_convergence.py)
- [Domain test boundary](../../../tests/domains/settlements-infrastructure/README.md)
- [Domain validator boundary](../../../tools/validators/domains/settlements-infrastructure/README.md)
- [Domain policy boundary](../../../policy/domains/settlements-infrastructure/README.md)
- [Source-registry boundary](../../../data/registry/sources/settlements-infrastructure/README.md)
- [Proof boundary](../../../data/proofs/settlements-infrastructure/README.md)
- [Published-data boundary](../../../data/published/settlements-infrastructure/README.md)
- [Release-candidate boundary](../../../release/candidates/settlements-infrastructure/README.md)

## 16. Open verification backlog

| Item | Evidence required to close it | Current state |
|---|---|---|
| Real candidate contract and record | Accepted candidate or manifest contract plus one immutable public-safe dossier and artifact inventory | `HOLD` |
| Domain semantic validation | Representative valid, invalid, held, denied, restricted, and cross-domain fixtures plus callable validators and negative tests | `HOLD` |
| Source and legal-role closure | Admitted source descriptors, source-role tests, rights review, retrieval identity, and legal or statistical authority mapping | `HOLD` |
| Proof producer | Accepted producer, schemas, source-role controls, fixtures, validators, receipts, access controls, and deterministic tests | `HOLD` |
| Domain release dry-run | Accepted command, candidate-manifest contract, fail-closed fixtures, no-public-write proof, and rollback boundary | `HOLD` |
| Policy runtime | Accepted evaluator path, bundle and version identity, parity proof, candidate binding, finite result, reasons, and obligations | `NEEDS VERIFICATION` |
| Accountable roles | Current domain, municipal-source, rights, cultural and sovereignty, infrastructure-security, evidence and policy, rollback, and release assignments | `NEEDS VERIFICATION` |
| Public boundary | Governed API or immutable released-carrier implementation, access control, public-safe transformation, correction, degraded-state, and no-leak evidence | `UNKNOWN` |
| Operational recovery | Candidate-bound correction, invalidation, rollback, recovery, and rehearsal evidence | `HOLD` |
| `settlement` and `settlements-infrastructure` convergence | Accepted ADR and migration plan resolving the documented naming and authority variance | `CONFLICTED / HOLD` |

## 17. Runbook maintenance and documentation rollback

Re-review this runbook when a candidate appears, the domain or convergence
workflow changes, domain semantic validators become callable, a proof producer
or release-dry-run command is accepted, policy runtime becomes executable,
accountable roles change, a release contract is adopted, a public surface is
added, or correction and rollback evidence changes.

For a future edit:

1. freeze the exact default-branch commit and relevant blobs;
2. inspect the local procedure boundary, candidate lane, workflows, schemas,
   validators, tests, policy, proof, review, correction, rollback, and public
   surfaces;
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
