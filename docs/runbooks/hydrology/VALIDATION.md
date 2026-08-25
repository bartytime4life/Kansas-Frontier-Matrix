<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook-hydrology-validation
title: Hydrology Bounded Validation Runbook
type: runbook
version: 0.2.0
status: DRAFT_REPOSITORY_GROUNDED; BOUNDED_SYNTHETIC_VALIDATION_ONLY; BROADER_SEMANTICS_HELD; NON_RELEASE; NON_PUBLICATION
owners: "@bartytime4life — verified CODEOWNERS route; accountable hydrology, evidence, policy, source, safety, and release stewardship NEEDS VERIFICATION"
created: NEEDS_VERIFICATION
updated: 2026-08-25
owning_root: docs/
responsibility: human validation procedure for the existing hydrology lane
related:
  - docs/domains/hydrology/EXPANSION_BACKLOG.md
  - .github/workflows/domain-hydrology.yml
  - tools/validators/domains/hydrology/README.md
  - tests/domains/hydrology/README.md
  - contracts/domains/hydrology/domain_validation_report.md
[/KFM_META_BLOCK_V2] -->

# Hydrology Bounded Validation Runbook

## Purpose and authority boundary

Use this procedure to run and interpret the Hydrology checks that current repository workflows actually execute. It keeps the bounded synthetic fixture profiles separate from broader hydrologic semantics, EvidenceRef resolution, source admission, policy, proof, release, deployment, publication, and flood-warning or regulatory authority.

This runbook documents existing checks; it does not create a new validator, parent command, contract, policy, source, evidence object, promotion path, or publication path. Accepted ADR-0029 and the adopted Directory Rules place human procedures under `docs/`; this file remains at its existing path and creates no new responsibility root or parallel validation authority.

## Current executable boundary

At the baseline for this runbook, `.github/workflows/domain-hydrology.yml` executes a bounded set of repository-owned synthetic or fixture-only checks. A green workflow establishes only the named behavior at the tested SHA.

| Profile | Executable evidence | Demonstrated boundary |
|---|---|---|
| Domain module set | Seven `pytest` modules named in the workflow | Bounded smoke, aquifer pair, ambiguity, proposal, identity-bridge, and QC-context behavior only. |
| Public-safe flow | `test_public_safe_flow_fixture.py` and the public-safe flow validator with valid and known-invalid fixtures | Frozen synthetic FlowObservation fixture shape and polarity only. |
| Cross-domain ownership | `test_environmental_observation_boundaries.py` | Bounded Soil/Atmosphere/Hydrology ownership isolation. |
| EvidenceBundle alias | `validate_evidence_bundle.py` with one valid and one expected-invalid fixture | PROPOSED alias shape and fixture polarity; not EvidenceRef resolution or evidence closure. |
| Aquifer pair | AquiferObservation and AquiferContextLink validators with `--fixtures` | Separated synthetic observation/context-link shape; not actual membership or geometry. |
| NHDPlus crosswalk | Waterbody crosswalk validator with `--fixtures` | Synthetic waterbody-only cardinality and abstention profile; not live identity or geometry comparison. |

The workflow also records explicit holds. Broader semantics, evidence closure, proof, release, source and endpoint behavior, policy, actual units/freshness, public-safe geometry, regulatory status, correction, rollback, deployment, and publication are not established by these checks.

The workflow deliberately fails if a `hydrology-validate` or `validate-hydrology` Make target appears without deliberate wiring and verification. Do **not** invent or document `make hydrology-validate` as a current command.

## Mandatory stop conditions

Stop and report **HOLD**, **UNKNOWN**, or **NEEDS VERIFICATION**, as applicable, when:

- the exact branch-head or merge-result SHA cannot be established;
- the repository inventory or workflow differs materially from the paths below;
- a valid fixture is rejected, a known-invalid fixture is accepted, or no negative fixture is exercised;
- a check requires network access, a live endpoint, credentials, private payloads, or source activation;
- a passing shape check is being used to claim evidence closure, scientific accuracy, current conditions, regulatory status, public-safe geometry, policy approval, proof, or release readiness;
- EvidenceBundle language is used without resolvable EvidenceRefs and cite-or-abstain behavior;
- source identity, units, time, freshness, geometry, aquifer membership, gauge/reach/HUC linkage, rights, license, sensitivity, or provenance is assumed rather than demonstrated;
- a derived drought class, threshold proposal, map, tile, index, embedding, summary, model output, or generated text is treated as canonical truth;
- the output could expose precise restricted locations, critical infrastructure, Indigenous or Tribal cultural information, archaeology, rare species, living-person information, or rights-unclear material;
- another active PR or branch owns the same validation surface; or
- the requested action would promote, release, deploy, publish, widen access, mutate lifecycle state, or change repository settings.

Do not weaken a validator, negative fixture, policy, inventory hold, or topology ratchet to obtain a pass.

## Validation procedure

### 1. Pin repository and execution identity

Record the full 40-character `slice_base_sha`, branch-head SHA, merge base, current main SHA, and workflow run. A result is **HEAD VALIDATION** only when the tested SHA is the exact branch head. A pull-request merge ref is **MERGE-RESULT VALIDATION** and must name the synthetic merge SHA. If checkout identity or environment comparability is unclear, use **NEEDS VERIFICATION**.

### 2. Verify the workflow inventory before execution

Confirm that the exact workflow and referenced test/validator/fixture paths exist at the tested SHA. Confirm that no unreviewed parent Make target has appeared:

```bash
if grep -Eq '^(hydrology-validate|validate-hydrology):' Makefile; then
  echo "HOLD: unverified Hydrology parent target exists"
  exit 1
fi
```

This is an inventory guard, not permission to add, remove, or rewire a target in this documentation slice.

### 3. Run the bounded domain and cross-domain modules

Use the exact workflow module set:

```bash
python -m pytest -q -p no:cacheprovider \
  tests/domains/hydrology/test_hydrology_smoke.py \
  tests/domains/hydrology/test_aquifer_observation.py \
  tests/domains/hydrology/test_aquifer_context_link.py \
  tests/domains/hydrology/test_nhdplus_hr_ambiguity.py \
  tests/domains/hydrology/test_adaptive_threshold_proposal.py \
  tests/domains/hydrology/test_hydro_identity_bridge.py \
  tests/domains/hydrology/test_streamflow_qc_context_assessment.py

python tests/domains/hydrology/test_public_safe_flow_fixture.py --verbose
python tests/cross_domain/test_environmental_observation_boundaries.py --verbose
```

Run from a clean checkout with the workflow's no-network and deterministic environment. Do not substitute live API calls.

### 4. Run positive and negative fixture polarity

```bash
python tools/validators/domains/hydrology/validate_evidence_bundle.py \
  fixtures/domains/hydrology/evidence_bundle/valid/valid_1.json

if python tools/validators/domains/hydrology/validate_evidence_bundle.py \
  fixtures/domains/hydrology/evidence_bundle/invalid/invalid_1.json; then
  echo "HOLD: known-invalid Hydrology EvidenceBundle fixture was accepted"
  exit 1
fi

python tools/validators/domains/hydrology/validate_aquifer_observation.py --fixtures
python tools/validators/domains/hydrology/validate_aquifer_context_link.py --fixtures

python tools/validators/domains/hydrology/validate_public_safe_flow_fixture.py \
  fixtures/domains/hydrology/public_safe_flow/valid/public_safe_flow.json

if python tools/validators/domains/hydrology/validate_public_safe_flow_fixture.py \
  fixtures/domains/hydrology/public_safe_flow/invalid/role_location_time_governance_collapse.json; then
  echo "HOLD: known-invalid Hydrology flow fixture was accepted"
  exit 1
fi

python tools/validators/domains/hydrology/validate_nhdplus_waterbody_crosswalk.py --fixtures
```

Expected-invalid acceptance is an introduced failure when the exact base rejects the same fixture under a materially equivalent environment and the exact branch head accepts it. Without that comparison, classify the failure **UNRESOLVED / NON-COMPARABLE**, not inherited.

### 5. Interpret the result by demonstrated capability

| Observation | Required interpretation |
|---|---|
| All named modules and fixture-polarity checks pass | The bounded profile passed at the tested SHA; broader semantics and lifecycle claims remain held. |
| A valid fixture fails on both exact base and head with the same signature | **INHERITED** only when command and environment are materially comparable. |
| Exact base passes and exact head fails with the same command/environment | **INTRODUCED**; hold the change. |
| Exact base fails and exact head passes | **RESOLVED** for that exact failure only. |
| Synthetic merge result fails after main changes while the original head/base comparison passed | **BASE-DRIFT / INTEGRATION**; re-evaluate material drift. |
| Network, runner, or nondeterministic evidence is repeated and substantiated | **ENVIRONMENTAL / FLAKY**; retain the evidence and do not claim a product pass. |
| Checkout SHA, command, fixture set, or environment cannot be compared | **UNRESOLVED / NON-COMPARABLE** or **NEEDS VERIFICATION**. |

Never describe an EvidenceBundle shape pass as resolved evidence, an aquifer shape pass as actual aquifer membership, a crosswalk pass as live identity resolution, or a flow-fixture pass as a current hydrologic or flood determination.

### 6. Produce a minimized validation record

Record the command/check, exact tested SHA, baseline result, head or merge-result result, classification, changed paths, negative-fixture result, and unresolved holds. Do not place source payloads, credentials, precise restricted locations, culturally controlled information, proprietary excerpts, or temporary access links in logs or PR text.

The validation record is evidence for accountable review. It is not a PromotionDecision, PromotionReceipt, ReleaseManifest, release approval, deployment approval, publication approval, flood warning, or regulatory determination.

## Acceptance criteria

This documentation slice is complete only when:

1. every documented command exists in the exact current workflow;
2. the unverified parent Make target is explicitly prohibited rather than invented;
3. positive and expected-negative fixture behavior is included;
4. bounded shape/polarity evidence is separated from broader semantics, evidence closure, policy, proof, release, and publication;
5. head, merge-result, baseline, and failure-attribution requirements are explicit;
6. no live, sensitive, proprietary, culturally controlled, rights-unclear, or precise-location material appears; and
7. rollback changes documentation only.

## Proposal-source reconciliation

`KFM_Full_Atlas_seed_cards.md`, v2 expansion section, “Hydrology Proof Lane” (lines 1480–1590 in the inspected Markdown copy; SHA-256 `9a95ab510bd984c257a8c578f8646993c7fe55d76f7d3c5f60d8bb9ad04ec3a2`, retrieved 2026-08-25) proposes evidence, no-network fixtures, validators, proof, and rollback while explicitly saying current repository maturity is unknown and recommending small reversible slices. It is proposal material, not repository authority.

The later `KFM Circled Sources — Distinctive Delta Synthesis` (modified 2026-08-23), §3.1, reinforces separating authority posture from executable capability. It does not adopt a Hydrology proof lane. This runbook documents only capabilities corroborated by the exact-baseline workflow, tests, validators, and accepted ADR-0029; unimplemented proof and release ideas remain held.

## Rollback and non-effects

Before merge, close the draft PR and discard only its campaign branch. After merge, revert the single documentation commit or submit a reviewed forward correction. Either action changes documentation only; it does not remove evidence, correct data, undo a lifecycle transition, revoke a source, or retract public state.

This runbook and its validation commands do not contact a live endpoint, admit or activate a source, resolve real EvidenceRefs, establish evidence closure, activate policy, create proof, issue a flood warning or regulatory determination, promote, release, deploy, publish, widen access, or change repository settings.
