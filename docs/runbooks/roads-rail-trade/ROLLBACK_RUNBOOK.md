<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook/roads-rail-trade/rollback
title: Roads, Rail, and Trade Routes — Rollback Readiness Runbook
type: runbook
version: v2.0
prior_state: proposal-heavy May 2026 procedure with unverified release records, commands, roles, public surfaces, and live rollback capability
status: draft; repository-grounded; BOUNDED_ROLLBACK_CANDIDATE_VALIDATION; SYNTHETIC_REHEARSAL_ONLY; PRODUCTION_ROLLBACK_EXECUTION_HELD; NON_RELEASE; NON_DEPLOYMENT; NON_PUBLICATION
owners:
  - "@bartytime4life — verified GitHub review route"
  - "NEEDS VERIFICATION — accountable Roads/Rail/Trade, evidence, rights, sensitivity, policy, release, rollback, infrastructure, and cultural-corridor assignments"
created: 2026-05-12
updated: 2026-08-29
policy_label: repository-facing; infrastructure-sensitive; historic and cultural corridor precision-sensitive; fail-closed
current_path: docs/runbooks/roads-rail-trade/ROLLBACK_RUNBOOK.md
owning_root: docs/
responsibility: human incident classification, rollback-readiness validation, and accountable-review handoff for the Roads/Rail/Trade lane
truth_posture: cite-or-abstain
authority_class: explanatory operational documentation
authority_rank: subordinate to accepted doctrine and ADRs, contracts, schemas, source records, evidence, policy, review, release records, correction and withdrawal records, signatures, receipts, proofs, and official authorities
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 702d61158d601ab12ef3c7b4d5e83fd0636ae9d5
  target_before_update_blob: a097a2aa95bda465227a4103aa5da7416a72622d
  local_runbook_boundary_blob: 964d3f7ec2409d01b1cd40fd84403a69f5950b56
  domain_workflow_blob: 391fead3fdd0d7ecead6464be7946cbaf68247e0
  rollback_card_workflow_blob: 1980b6e914532c1478d6f14310b916b69a0fb1c4
  rollback_drill_workflow_blob: 2d0c39fc6ff8e44bd9cf753ce546475079e8ffd5
  rollback_card_contract_blob: c6d3c35c56b064e04c3a2532f4709d938d7b0c1a
  rollback_card_schema_blob: e0a9edf02dd5d6997eda60a054a5bf19636c3dd4
  rollback_card_validator_blob: 9e9ed5a92851935b41a36698e4bead13ef4edf57
  rollback_card_tests_blob: c8aeac6348127fb768981e2b5b5588c6a7bdeb78
  synthetic_rehearsal_helper_blob: a8f6bff350e79b453f425ebce9a9ded6801f8944
  lane_rollback_cards_readme_blob: 1ddc6fb9da9bf415984f2a3de3c1bf839e38334f
  lane_manifests_readme_blob: aaa85fb6f24e32d5526c6b1c901b0b7b8c22f430
  lane_candidate_readme_blob: c989bf2bed10472bc46a168231b2269f17bbda48
  lane_proof_readme_blob: 91c109d463c45c925f1d104d4cd8aaf742cd28af
  lane_policy_readme_blob: 577fde2174817459b87039922e3264e6e1073831
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adoption_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  lane_candidate_records_observed: 0
  lane_release_manifest_records_observed: 0
  lane_rollback_card_records_observed: 0
  lane_proof_artifacts_observed: 0
  lane_published_payloads_observed: 0
related:
  - ./README.md
  - ./NO_NETWORK_TEST_RUNBOOK.md
  - ./PROMOTION_RUNBOOK.md
  - ../../domains/roads-rail-trade/README.md
  - ../../doctrine/directory-rules.md
  - ../../doctrine/lifecycle-law.md
  - ../../doctrine/trust-membrane.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../.github/workflows/domain-roads-rail-trade.yml
  - ../../../.github/workflows/rollback-card.yml
  - ../../../.github/workflows/rollback-drill.yml
  - ../../../contracts/release/rollback_card.md
  - ../../../schemas/contracts/v1/release/rollback_card.schema.json
  - ../../../tools/validators/release/validate_rollback_card.py
  - ../../../tests/validators/test_validate_rollback_card.py
  - ../../../tools/release/rollback_apply.py
  - ../../../release/candidates/roads-rail-trade/README.md
  - ../../../release/manifests/roads-rail-trade/README.md
  - ../../../release/rollback_cards/roads-rail-trade/README.md
  - ../../../data/proofs/roads-rail-trade/README.md
  - ../../../data/rollback/roads-rail-trade/README.md
  - ../../../data/published/roads-rail-trade/README.md
notes:
  - "v2.0 replaces proposed live rollback steps with a current-repository readiness procedure and accountable-review handoff."
  - "The generic RollbackCard profile is closed, fixture-validated, and explicitly non-executing; its schema status remains PROPOSED."
  - "The rollback drill is a read-only readiness workflow. The only apply helper is marker-protected, synthetic-only, and incapable of creating production authority."
  - "The Roads/Rail/Trade candidate, manifest, rollback-card, proof, and published lanes contain guidance only; no lane instance record or public payload was observed."
  - "Production target selection, signature and review verification, policy evaluation, receipt flow, external invalidation, alias mutation, release transition, deployment, and publication remain held."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Roads, Rail, and Trade Routes — Rollback Readiness Runbook

Use this runbook to classify a suspected post-release defect, assemble a
rollback or withdrawal candidate, run the repository's bounded no-network
checks, and hand the result to accountable reviewers. It does not execute a
production rollback.

> [!WARNING]
> Current repository evidence does not establish a Roads/Rail/Trade release to
> roll back. The lane-specific candidate, manifest, rollback-card, proof, and
> published directories contain only their README files and `.gitkeep` markers.
> Stop at `HOLD` unless an exact affected release and all required governed
> support records are independently identified and verified.

> [!CAUTION]
> KFM is not a navigation, dispatch, traffic-control, railroad-operating,
> bridge-safety, emergency-routing, legal-access, right-of-way, regulatory, or
> current-closure authority. A rollback check cannot establish that a road,
> rail line, bridge, crossing, ferry, facility, route, or corridor is open,
> lawful, current, complete, or safe.

**Quick navigation:** [Current capability](#current-capability) ·
[When to use this runbook](#when-to-use-this-runbook) ·
[Inputs and stop conditions](#inputs-and-stop-conditions) ·
[Procedure](#procedure) · [Validation commands](#validation-commands) ·
[Handoff packet](#handoff-packet) · [Rollback of this document](#rollback-of-this-document)

## Purpose and authority boundary

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
adopts the [Directory Rules](../../doctrine/directory-rules.md), which place
human operational procedures below `docs/runbooks/`. This same-path update
therefore remains under the `docs/` responsibility root. It does not create a
new release, policy, proof, data, or execution authority.

The controlling separation is:

| Concern | Owning surface | This runbook's limit |
|---|---|---|
| Incident procedure and handoff | `docs/runbooks/roads-rail-trade/` | Explains and records bounded human steps |
| Rollback candidate meaning and shape | `contracts/release/rollback_card.md` and `schemas/contracts/v1/release/rollback_card.schema.json` | Cites the proposed profile; cannot activate it |
| Release-plane records | `release/manifests/`, `release/rollback_cards/`, `release/correction_notices/`, `release/withdrawal_notices/` | Requires immutable pointers; cannot manufacture a decision |
| Data-plane rollback support | `data/rollback/roads-rail-trade/` | May hold governed support records; cannot authorize rollback |
| Evidence and proof | `data/proofs/` and accepted evidence contracts | Evidence outranks prose, maps, tests, and generated language |
| Policy and sensitivity | `policy/` plus accountable review | Missing or inactive evaluation fails closed |
| Public state | Governed release resolvers and public-safe artifacts | No direct write or read path from this runbook |

Rollback is a governed state transition. It is not deletion, erasure, a file
move, a branch merge, or an undocumented pointer edit. Prior manifests,
artifacts, evidence, receipts, decisions, and correction lineage remain
inspectable unless a separate authorized retention or erasure process applies.

## Current capability

| Surface | Confirmed repository state | Safe conclusion |
|---|---|---|
| Roads/Rail/Trade release inventory | Candidate, manifest, rollback-card, proof, and published subtrees contain no instance records or payloads | No in-repository lane release is available for a real rollback |
| `CorridorRoute` profile | Fourteen focused tests plus a no-network fixture validator are wired in the domain workflow | Synthetic contract validation is available; route truth, policy, proof, release, and rollback are not established |
| Generic `RollbackCard` profile | Closed proposed schema, semantic validator, positive and negative fixtures, focused tests, and read-only workflow | Candidate shape and local consistency can be checked; validation does not authorize mutation |
| Signed rollback token | `PROPOSED_INACTIVE` schema, fixtures, validator, tests, and read-only workflow | Fixture readiness only; no cryptography, signature authority, receipt write, alias mutation, or rollback execution |
| Rollback drill | Read-only workflow inspects holds and runs twelve generic/Hazards synthetic rehearsal tests | Non-vacuous readiness evidence only; no production target or public state is selected or mutated |
| Apply helper | `tools/release/rollback_apply.py` accepts only a marker-protected synthetic workspace and `synthetic: true` scenario | Safe for isolated rehearsal tests; deny all production use |
| Production rollback pipeline | `pipelines/rollback/main.py` remains a greenfield placeholder | Production execution is held |
| Roads/Rail/Trade domain rollback tests | `test_release_manifest_present.py` and `test_transport_graph_rollback.py` contain docstrings only | No lane-specific executable release or graph rollback proof exists |
| Roads/Rail/Trade policy | Repository-grounded scaffold; evaluator and governed consumers are unbound | No active policy decision or obligation enforcement is established |

A green workflow proves only the exact bounded checks it runs at the tested
revision. It is not a `PolicyDecision`, `ReviewRecord`, `ReleaseManifest`,
`RollbackCard` approval, proof, signature, release transition, deployment, or
publication event.

## When to use this runbook

Use it after a suspected defect is reported against material believed to be
released through the Roads/Rail/Trade lane. First determine whether the report
actually names a governed release record. If it names only a map view, branch,
pull request, template, candidate, generated answer, cache entry, screenshot,
or internal data file, do not assume publication.

Classify the earliest supported response:

| Disposition | Use only when | Required posture |
|---|---|---|
| `ROLLBACK_CANDIDATE` | The affected release is exact and a different prior safe release is exact, digest-verified, policy-eligible, reviewed, and complete | Prepare a candidate; do not mutate public state |
| `WITHDRAWAL_CANDIDATE` | Continued exposure is unsafe and no verified safe target is available | Fail closed and prepare withdrawal review |
| `HOLD` | Release identity, target, evidence, rights, sensitivity, policy, review, signature, invalidation, or correction support is unresolved | Preserve the uncertainty and escalate |
| `ERROR` | Inputs are malformed, conflicting, unreadable, or cannot be deterministically evaluated | Repair the evidence or tooling before relying on a result |

Defects that can justify immediate fail-closed escalation include unsupported
evidence, incorrect source role, unknown rights, harmful precision, cultural or
sovereignty exposure, stale or incorrect valid time, route/segment/membership
collapse, digest mismatch, invalid public-safe transform, unreviewed policy
change, or a governed client resolving an unreleased artifact.

## Inputs and stop conditions

### Required incident inputs

- [ ] Exact repository revision and incident identifier.
- [ ] Exact affected `ReleaseManifest` reference and immutable digest.
- [ ] Evidence that the affected release is the public release currently
      resolved by the governed surface; do not infer this from a filename named
      `latest` or `current`.
- [ ] Exact defect class, affected object families, geography, time interval,
      carriers, and public surfaces.
- [ ] Resolvable EvidenceBundle, source-role, rights, sensitivity, policy,
      validation, proof, and review references appropriate to the defect.
- [ ] Correction or withdrawal record reference with a named reason and time.
- [ ] Complete invalidation inventory covering every affected carrier and
      downstream derivative.
- [ ] Accountable release and domain reviewers; cultural, rights, security, or
      infrastructure review when the scope requires it.

### Additional inputs for a rollback candidate

- [ ] Exact target `ReleaseManifest` reference that differs from the affected
      release.
- [ ] Target artifact inventory and digest closure.
- [ ] Proof that the target's evidence, rights, sensitivity, policy, review,
      correction, and public-safe posture remain valid now.
- [ ] Preserved lineage from the target through the affected release and the
      proposed correction.
- [ ] Restoration and post-change verification plan.

### Mandatory stop conditions

Return `HOLD`, `WITHDRAWAL_CANDIDATE`, or `ERROR` as supported when any of the
following is unresolved:

- no exact released state or current governed resolver can be verified;
- the rollback target is absent, equal to the affected release, mutable, stale,
  digest-invalid, unreviewed, or no longer policy-eligible;
- source role, rights, sensitivity, sovereignty, consent, harmful precision,
  currentness, or valid time is unclear;
- evidence, proof, policy, review, signature, correction, withdrawal, receipt,
  or invalidation closure is incomplete;
- a cross-domain dependency would absorb Hydrology, Hazards, Archaeology,
  Settlements/Infrastructure, People/Land, or another lane's authority;
- a proposed action would expose restricted geometry or operational detail;
- the action depends on the synthetic helper, placeholder production pipeline,
  docstring-only domain tests, or proposal-only policy as live authority; or
- an actor would both author and solely approve a policy- or release-significant
  transition without an accepted exception.

## Procedure

### 1. Pin the evidence boundary

Record the exact Git commit, incident ID, affected repository paths, observed
public surface, reporter evidence, and time of observation. Preserve raw reports
outside public logs when they contain restricted geometry or sensitive
infrastructure detail.

Inventory the lane before making a release claim:

```bash
find release/candidates/roads-rail-trade -mindepth 1 -type f \
  ! -name README.md ! -name .gitkeep -print
find release/manifests/roads-rail-trade -mindepth 1 -type f \
  ! -name README.md ! -name .gitkeep -print
find release/rollback_cards/roads-rail-trade -mindepth 1 -type f \
  ! -name README.md ! -name .gitkeep -print
find data/proofs/roads-rail-trade data/published/roads-rail-trade \
  -mindepth 1 -type f ! -name README.md ! -name .gitkeep -print
```

Empty output is not proof that no external release exists, but it blocks an
in-repository rollback claim until the external release identity and governed
records are reconciled.

### 2. Classify the defect and affected carriers

Keep the following identities separate:

- route or corridor identity;
- road or rail segments;
- sourced, time-bounded segment membership;
- legal designation, operator, access, restriction, or status claims;
- historic or interpretive alignment and its uncertainty;
- generalized public geometry versus restricted canonical geometry; and
- graph, tile, search, report, export, Evidence Drawer, and AI derivatives.

List each affected carrier explicitly. The synthetic rehearsal contract names
`API_CACHE`, `CDN`, `TILES`, `CATALOG`, `TRIPLETS`, `SEARCH_INDEX`,
`VECTOR_INDEX`, `AI_CACHE`, and `DOWNSTREAM_DERIVATIVES`; a production plan must
also include any lane-specific carriers confirmed by current deployment
evidence. Do not assume the synthetic list is a complete production inventory.

### 3. Select rollback, withdrawal, or hold

Choose `ROLLBACK_CANDIDATE` only after both manifests and all referenced
artifacts verify. When there is no safe prior target, choose
`WITHDRAWAL_CANDIDATE` or `HOLD` instead of restoring an unverified release.

For rights, cultural, sovereignty, private-access, sensitive-infrastructure, or
harmful-precision defects, prefer immediate governed withdrawal, redaction,
generalization, or denial while review proceeds. Do not publish a more precise
explanation of the defect than the affected public is authorized to see.

### 4. Assemble a non-executing RollbackCard candidate

Use the current generic contract and schema as a proposed candidate profile.
Populate all required groups, including:

- stable identity, version, deterministic `spec_hash`, and finite disposition;
- trigger and affected release reference;
- target mode: `PRIOR_RELEASE`, `WITHDRAWAL`, or `HOLD`;
- EvidenceBundle, policy-decision, review-record, and correction-notice
  references;
- invalidations and restoration verification;
- decision and execution timing;
- supersession lineage; and
- governance non-effects.

The profile's `x-kfm` metadata says its authority is
`candidate_shape_and_local_consistency_only`. Schema validity must not be
reported as approval or executable rollback authority.

### 5. Run bounded validation

Run the exact current commands in [Validation commands](#validation-commands).
Record the revision, command, exit code, and complete finite outcome. Do not
rewrite `ABSTAIN`, `DENY`, `HOLD`, or `ERROR` as success.

### 6. Prepare the accountable handoff

Attach the handoff packet below to a review request. CODEOWNERS routes repository
review to `@bartytime4life`; that is not proof of independent domain, rights,
sensitivity, policy, release, or rollback approval.

Stop here. No command in this runbook authorizes production target selection,
signature creation, policy activation, external cache invalidation, alias
mutation, release transition, deployment, publication, or source activation.

## Validation commands

Run from the repository root at the exact revision under review.

### Roads/Rail/Trade bounded profile

```bash
python -m pytest -q tests/schemas/test_corridor_route_contract.py
python tools/validators/domains/roads-rail-trade/validate_corridor_route.py --fixtures
```

The current workflow expects fourteen focused tests and the fixture-declared
`PASS`, `ABSTAIN`, `DENY`, and `ERROR` polarity. These commands do not validate
a release or rollback.

### Generic RollbackCard candidate profile

```bash
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_rollback_card.py' \
  --verbose
python tools/validators/release/validate_rollback_card.py --fixtures
```

To check a proposed card without mutating state:

```bash
python tools/validators/release/validate_rollback_card.py \
  <path-to-proposed-rollback-card.json>
```

### Fixture-only signed-token readiness

```bash
python -m py_compile \
  tools/validators/release/validate_signed_rollback_token.py \
  tests/validators/test_validate_signed_rollback_token.py
python -m unittest tests.validators.test_validate_signed_rollback_token -v
python tools/validators/release/validate_signed_rollback_token.py --fixtures
```

These checks execute no cryptography, alias mutation, rollback, receipt write,
deployment, or publication.

### Synthetic rehearsal regression profile

```bash
python -m unittest -q \
  tests.release.test_synthetic_rollback_rehearsal \
  tests.domains.hazards.test_synthetic_rollback_rehearsal
```

The current rollback-drill workflow expects twelve non-vacuous tests. The
rehearsal helper is deliberately limited to isolated roots containing the exact
`.kfm-synthetic-rollback-rehearsal` marker and scenarios with `synthetic: true`.
Do not point it at repository, staging, production, published, or externally
mounted state, and do not treat its `--apply` option as a production command.

## Result interpretation

| Observation | Meaning | Required response |
|---|---|---|
| RollbackCard `PASS` | Proposed card satisfied shape, hash, reference syntax, and local semantic checks | Continue accountable review; do not mutate state |
| `ABSTAIN` | Required support is unresolved | Preserve uncertainty and stop advancement |
| `DENY` | Candidate violates a fail-closed rule | Correct the candidate or select withdrawal/hold |
| `ERROR` | Input or evaluation failed | Repair tooling or inputs before relying on the result |
| Signed-token fixture `PASS` | Fixture-only readiness checks passed | Do not claim a signature or authorization exists |
| Synthetic rehearsal `PASS` | Isolated marker-protected history and invalidation behavior passed | Do not generalize to production |
| `rollback-drill` green | Current holds and synthetic checks matched workflow expectations | Production rollback remains held |
| Domain workflow green | Bounded CorridorRoute and readiness checks passed | No route truth, proof, release, or rollback is established |

## Handoff packet

The review packet must contain:

- [ ] incident ID, author, timestamp, and exact Git revision;
- [ ] affected release reference, manifest digest, artifact inventory, and proof
      that the governed public surface resolves it;
- [ ] defect class, evidence, source-role, rights, sensitivity, policy,
      validation, and review references;
- [ ] exact target release and digest closure, or an explicit withdrawal/hold
      reason;
- [ ] proposed RollbackCard candidate plus validator output;
- [ ] correction or withdrawal reference;
- [ ] affected carrier and downstream-derivative inventory;
- [ ] invalidation, stale-state, correction-display, and verification plan;
- [ ] preservation proof for affected and target manifests and artifacts;
- [ ] accountable reviewer identities and separation-of-duties record;
- [ ] communication plan that does not expose restricted detail;
- [ ] finite terminal state: `ROLLBACK_CANDIDATE`,
      `WITHDRAWAL_CANDIDATE`, `HOLD`, or `ERROR`; and
- [ ] explicit statement that no live action occurred during this procedure.

## Definition of done

This readiness pass is complete when the exact evidence boundary is pinned, the
defect and carriers are classified, the candidate passes or returns a truthful
negative result, the handoff packet is complete, and no unauthorized mutation
occurred.

A production rollback is **not** complete merely because this runbook was
followed. Production completion remains held until an accepted executor,
authenticated target and signatures, active policy evaluation, accountable
review, durable receipts, external invalidation, governed alias transition,
post-change verification, correction visibility, and rollback-of-rollback path
are independently implemented and proven.

## Open verification register

| ID | Question | Current status |
|---|---|---|
| RRT-RB-001 | Which exact release and public resolver would be affected? | No lane instance observed; `HOLD` |
| RRT-RB-002 | Who holds accountable domain, release, rollback, rights, sensitivity, and independent-review roles? | `NEEDS VERIFICATION` |
| RRT-RB-003 | Which policy bundle and governed consumer enforce rollback obligations? | Scaffold/evaluator unbound |
| RRT-RB-004 | Which accepted signature and token mechanism authorizes a live transition? | Fixture-only token profile; inactive |
| RRT-RB-005 | Which production engine selects targets, writes receipts, invalidates carriers, and changes the governed resolver? | Production pipeline placeholder |
| RRT-RB-006 | What domain-specific fixtures prove manifest, graph, map, API, Evidence Drawer, export, search, and AI invalidation? | Domain test files are placeholders |
| RRT-RB-007 | What accepted decision resolves the `roads-rail-trade` versus `transport` contract/schema topology? | `NEEDS VERIFICATION`; do not resolve here |
| RRT-RB-008 | Which checks are required by repository rules for a rollback-significant change? | `NEEDS VERIFICATION` |

## Documentation maintenance

Re-review this runbook when a Roads/Rail/Trade candidate, manifest, rollback
card, proof artifact, published payload, accepted policy bundle, governed
consumer, signature mechanism, production executor, invalidation adapter, or
domain rollback test appears. Update current-state claims from exact repository
evidence; do not upgrade a template, README, fixture, workflow, or green check
into release authority.

## Rollback of this document

Before merge, close the draft pull request and discard only its feature branch.
After merge, revert the documentation commit or submit a reviewed forward
correction. Either action changes documentation only; it does not select a
release target, restore data, invalidate a cache, mutate an alias, execute a
rollback, deploy, publish, or activate a source.

## Related responsibility roots

- [Local Roads/Rail/Trade runbook boundary](./README.md)
- [Promotion preflight](./PROMOTION_RUNBOOK.md)
- [Bounded no-network validation](./NO_NETWORK_TEST_RUNBOOK.md)
- [Roads/Rail/Trade domain boundary](../../domains/roads-rail-trade/README.md)
- [Generic RollbackCard contract](../../../contracts/release/rollback_card.md)
- [Generic RollbackCard schema](../../../schemas/contracts/v1/release/rollback_card.schema.json)
- [Generic RollbackCard validator](../../../tools/validators/release/validate_rollback_card.py)
- [Rollback-card workflow](../../../.github/workflows/rollback-card.yml)
- [Rollback-drill readiness workflow](../../../.github/workflows/rollback-drill.yml)
- [Lane candidate boundary](../../../release/candidates/roads-rail-trade/README.md)
- [Lane manifest boundary](../../../release/manifests/roads-rail-trade/README.md)
- [Lane rollback-card boundary](../../../release/rollback_cards/roads-rail-trade/README.md)
- [Lane proof boundary](../../../data/proofs/roads-rail-trade/README.md)
- [Lane data-plane rollback boundary](../../../data/rollback/roads-rail-trade/README.md)
- [Lane published-data boundary](../../../data/published/roads-rail-trade/README.md)

[Back to top](#top)
