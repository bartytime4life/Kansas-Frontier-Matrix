<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook-hydrology-validation
title: Hydrology Validation Runbook
type: runbook
version: v1.0.0
status: DRAFT_REPOSITORY_GROUNDED; BOUNDED_NO_NETWORK_VALIDATION_EXECUTABLE; LIVE_SOURCE_PROOF_RELEASE_DEPLOYMENT_AND_PUBLICATION_HELD; NOT_FOR_LIFE_SAFETY
owners:
  - "@bartytime4life — verified GitHub review route"
  - "NEEDS VERIFICATION — accountable Hydrology, evidence, source, policy, safety, proof, release, and operations assignments"
created: 2026-08-25
updated: 2026-08-27
policy_label: repository-facing; validation-sensitive; fail-closed
current_path: docs/runbooks/hydrology/VALIDATION.md
owning_root: docs/
responsibility: Human procedure for reproducing, interpreting, and handing off the Hydrology lane's current bounded no-network validation without claiming live-source, scientific, evidence, proof, release, deployment, publication, or life-safety authority.
truth_posture: cite-or-abstain
authority_class: explanatory operational documentation
authority_rank: subordinate to accepted doctrine and ADRs, contracts, schemas, source and evidence authority, executable validators and tests, policy, review, lifecycle, proof, release, correction, rollback, and official authorities
current_disposition: BOUNDED_NO_NETWORK_VALIDATION_AVAILABLE / BROADER_HYDROLOGY_TRUTH_AND_LIFECYCLE_TRANSITIONS_HELD
reason_codes:
  - HYD_VALIDATION_EXACT_SHA_REQUIRED
  - HYD_VALIDATION_FIXTURE_PROFILE_ONLY
  - HYD_VALIDATION_LIVE_SOURCE_AND_LIFECYCLE_HELD
  - HYD_VALIDATION_EVIDENCE_RESOLUTION_UNESTABLISHED
  - HYD_VALIDATION_PROOF_PRODUCER_HELD
  - HYD_VALIDATION_RELEASE_DRY_RUN_HELD
  - HYD_VALIDATION_LIFE_SAFETY_AUTHORITY_DENIED
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 6cd656e44e9cd8415651fd9da30a56095e6bfbe6
  target_prior_blob: c6c6ee9c89ad394847ef9e5ac053b7a136595678
  domain_workflow_blob: 36a0287be04639cb75dc77ae2c274fee626f6a00
  nwis_capture_workflow_blob: 3d324c7732b372e45bf6dd32ca67366b3550037d
  usgs_cutover_workflow_blob: 33d2091cf2f9d954adbff5e785361bcc196f0c93
  wbd_material_change_workflow_blob: e3edd2c98b708c170df84cef10d883d2c42b2b61
  lane_readme_blob: 67ac2ebd8208b2720c5765336aa9ac8af32fc11e
  source_refresh_runbook_blob: 0af9c08bdc432e234285f788e13d6d223f0796b4
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adoption_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
source_lineage:
  - "KFM_Hydrology_Extended_Pro_PDF_Only_Reference_Report_2026-04-21.pdf — Google Drive planning lineage; not current implementation authority"
  - "KFM Hydrology — Google Drive scaffold report; no-mounted-repository evidence and proposed commands remain lineage only"
  - "KFM Repository Workbench — Notion coordination surface; GitHub remains repository authority"
  - "KFM Markdown Update & Modernization Agent v1.0 — attached editing and delivery guidance"
related:
  - docs/runbooks/hydrology/README.md
  - docs/runbooks/hydrology/SOURCE_REFRESH_RUNBOOK.md
  - docs/runbooks/hydrology/PROMOTION_RUNBOOK.md
  - docs/runbooks/hydrology/ROLLBACK_RUNBOOK.md
  - docs/domains/hydrology/README.md
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0009-hydrology-is-the-first-proof-bearing-lane.md
  - docs/adr/ADR-0026-hydrology-source-spine-starts-with-wbd-huc12.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - .github/workflows/domain-hydrology.yml
  - .github/workflows/hydrology-nwis-county-capture.yml
  - .github/workflows/hydrology-usgs-water-api-cutover.yml
  - .github/workflows/hydrology-wbd-huc12-material-change.yml
  - contracts/domains/hydrology/README.md
  - schemas/contracts/v1/domains/hydrology/README.md
  - fixtures/domains/hydrology/README.md
  - tests/domains/hydrology/README.md
  - tools/validators/domains/hydrology/README.md
  - data/proofs/hydrology/README.md
  - release/candidates/hydrology/README.md
non_effects:
  - does_not_contact_live_sources
  - does_not_read_credentials
  - does_not_activate_or_admit_sources
  - does_not_write_raw_work_quarantine_processed_catalog_triplet_or_published_state
  - does_not_resolve_real_evidence_refs
  - does_not_create_evidence_or_proof
  - does_not_approve_policy_or_review
  - does_not_promote_release_deploy_or_publish
  - does_not_issue_life_safety_guidance
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hydrology Validation Runbook

Repository-grounded procedure for reproducing and interpreting the Hydrology
lane's current deterministic, no-network checks at an exact repository revision.
The procedure ends with a bounded validation record or a finite hold; it does not
turn fixture results into current hydrologic truth or authorize a later lifecycle
transition.

> [!WARNING]
> KFM is not a flood-warning, emergency-response, navigation, engineering,
> insurance, dam-operation, water-rights, legal, or regulatory authority. Use
> the responsible official source for current conditions and life-safety
> decisions. FEMA NFHL is regulatory flood-hazard context, not observed
> inundation. A gauge value, model result, map, fixture, generated receipt, or
> passing test is not an official warning.

> [!IMPORTANT]
> **Current disposition:** bounded no-network validation is executable for the
> profiles named below. Live retrieval, source activation, lifecycle writes,
> real EvidenceRef resolution, EvidenceBundle closure, proof production,
> promotion, release, deployment, publication, and public-use authority remain
> held.

**Quick navigation:** [Authority](#1-purpose-authority-and-scope) ·
[Current checks](#2-current-executable-validation-landscape) ·
[Preflight](#3-authority-freeze-and-preconditions) ·
[Core procedure](#4-reproduce-the-domain-hydrology-validation-job) ·
[Dedicated workflows](#5-run-the-dedicated-bounded-workflows) ·
[Interpretation](#6-profile-by-profile-interpretation) ·
[Attribution](#7-result-and-failure-classification) ·
[Stop conditions](#8-mandatory-stop-deny-and-escalation-conditions) ·
[Record](#9-validation-record-and-review-handoff) ·
[Maintenance](#10-acceptance-maintenance-and-documentation-rollback) ·
[Related surfaces](#11-related-repository-surfaces)

## 1. Purpose, authority, and scope

Use this runbook when a maintainer or reviewer needs to answer four bounded
questions:

1. Which Hydrology checks are executable at the exact revision under review?
2. Did the valid and expected-invalid fixture profiles behave as designed?
3. What may a green result truthfully support?
4. Which broader claims or transitions remain `HOLD`, `ABSTAIN`, `DENY`,
   `ERROR`, or `NEEDS VERIFICATION`?

Accepted directory governance places human operating procedures under
`docs/runbooks/`. This same-path update remains under `docs/` and creates no
new responsibility root or parallel validation authority. Hydrology meaning
remains under `contracts/`, machine shape under `schemas/`, executable behavior
under `tests/` and `tools/validators/`, source admission under governed source
surfaces, policy under `policy/`, proof under proof-bearing stores and
contracts, and release decisions under `release/`.

This file explains and reproduces current checks. It does not create or amend a
contract, schema, source descriptor, activation decision, validator, policy,
workflow, EvidenceBundle, proof, PromotionDecision, ReleaseManifest,
CorrectionNotice, rollback object, deployment, or publication state.

### 1.1 In scope

- The exact bounded commands invoked by current Hydrology workflows.
- Repository-owned synthetic and captured-input fixtures.
- Positive and expected-negative fixture polarity.
- No-network, deterministic execution posture.
- Exact-SHA identity, base/head comparison, merge-result distinction, and
  failure attribution.
- Review handoff with explicit claims, limitations, and unresolved holds.

### 1.2 Out of scope

- Live USGS, WBD, NHDPlus, FEMA, NOAA, NRCS, state, local, or other source
  requests.
- Credentials, source activation, source admission, or endpoint authorization.
- Writes to `RAW`, `WORK`, `QUARANTINE`, `PROCESSED`, `CATALOG`, `TRIPLET`, or
  `PUBLISHED`.
- Current-condition, flood, drought, water-quality, navigation, engineering,
  insurance, legal, emergency, or regulatory determinations.
- Real EvidenceRef resolution, EvidenceBundle closure, proof production,
  promotion, release, deployment, publication, or public access.
- Weakening a validator, negative fixture, policy, no-network guard, inventory
  hold, or topology ratchet to obtain a pass.

[Back to top](#top)

## 2. Current executable validation landscape

The repository currently has one broad Hydrology domain workflow and three
dedicated bounded workflows. Their responsibilities must remain distinct.

| Workflow / job | Current execution | What a green result supports | What remains held |
|---|---|---|---|
| [`.github/workflows/domain-hydrology.yml`](../../../.github/workflows/domain-hydrology.yml) / `validate-hydrology` | Explicit inventory checks; eight accepted domain modules; cross-domain ownership isolation; schema-wrapper and semantic fixture validators; positive and expected-negative fixtures | The named synthetic shape, polarity, finite-outcome, ownership, and abstention profiles passed at the tested SHA | Live sources, real evidence, scientific correctness, proof, promotion, release, deployment, publication, and life-safety authority |
| [`hydrology-nwis-county-capture.yml`](../../../.github/workflows/hydrology-nwis-county-capture.yml) / `validate-nwis-county-capture` | Captured-input-only USGS Water Data county normalizer tests and generated authoring-receipt integrity | Credential-free request planning and strict local normalization of caller-supplied captured pages for the tested fixtures | Network transport, source authenticity/currentness, source activation, RAW writes, evidence resolution, hydrologic interpretation, promotion, release, warning, and publication |
| [`hydrology-usgs-water-api-cutover.yml`](../../../.github/workflows/hydrology-usgs-water-api-cutover.yml) / `validate-usgs-water-api-cutover` | Fixture-only endpoint-family, required-role, rewrite-map, legacy-dependency, and dual-run reconciliation tests plus authoring-receipt integrity | The deterministic cutover-assessment fixture contract passed | Production cutover, live USGS access, source activation, lifecycle writes, hydrologic assertions, safety guidance, promotion, release, and publication |
| [`hydrology-wbd-huc12-material-change.yml`](../../../.github/workflows/hydrology-wbd-huc12-material-change.yml) / `validate-wbd-huc12-material-change` | Fixture-only geometry normalization, geometry-plus-area fingerprints, metadata-churn suppression, and finite material-change decisions plus authoring-receipt integrity | The supplied fixture assessment behaved deterministically | Live WBD retrieval, authoritative source comparison, source activation, lifecycle writes, promotion, release, deployment, and publication |
| `domain-hydrology` / `build-proof-hydrology` | Readiness inspection that deliberately records `WORKFLOW_SKIPPED_EXPLICIT` and a hold | The proof boundary remains fail-closed and no unreviewed proof producer was silently admitted | EvidenceRef-to-EvidenceBundle resolution, proof schemas, proof producer, ProofPack, access controls, receipts, and release linkage |
| `domain-hydrology` / `publish-dry-run-hydrology` | Readiness inspection that deliberately records `WORKFLOW_SKIPPED_EXPLICIT` and a hold | The release boundary remains fail-closed and no unreviewed candidate or dry-run command was silently admitted | Candidate contract, independent review, PromotionDecision, ReleaseManifest, release, deployment, publication, correction, withdrawal, and operational rollback |

> [!NOTE]
> A green held job is successful enforcement of a boundary, not proof that the
> held capability exists. `WORKFLOW_SKIPPED_EXPLICIT` is not a successful proof
> build or release dry run.

### 2.1 Eight accepted domain modules

The broad workflow reserves eight substantive Hydrology modules. Seven execute
in one `pytest` invocation and the public-safe flow module executes as a
standalone script:

| Module | Bounded purpose |
|---|---|
| `test_hydrology_smoke.py` | Basic lane fixture and import posture |
| `test_aquifer_observation.py` | Aquifer observation shape |
| `test_aquifer_context_link.py` | Separate context-link shape |
| `test_public_safe_flow_fixture.py` | Frozen public-safe FlowObservation fixture and known-invalid rejection |
| `test_nhdplus_hr_ambiguity.py` | Ambiguous NHDPlus relation handling |
| `test_adaptive_threshold_proposal.py` | Finite review proposal outcomes without threshold mutation |
| `test_hydro_identity_bridge.py` | Current and legacy identifier separation with abstention/deny behavior |
| `test_streamflow_qc_context_assessment.py` | Fixture-only QC context routing without computing or invalidating observations |

The workflow also runs
`tests/cross_domain/test_environmental_observation_boundaries.py` to preserve
Soil, Atmosphere, and Hydrology ownership isolation.

### 2.2 No aggregate Make target

The broad workflow deliberately fails if either of these targets appears
without deliberate wiring and verification:

- `hydrology-validate`
- `validate-hydrology`

Do not invent or document `make hydrology-validate` or
`make validate-hydrology` as a current command.

[Back to top](#top)

## 3. Authority freeze and preconditions

Complete this preflight before interpreting any result.

### 3.1 Pin the tested revision

Record:

- the full 40-character current `main` SHA;
- the feature-branch head SHA;
- the merge base;
- the exact base SHA used for comparison;
- the pull-request synthetic merge SHA, when applicable;
- the workflow run URL and run attempt;
- the changed paths; and
- whether the result is `HEAD`, `BASELINE`, or `MERGE_RESULT` validation.

A result is `HEAD` validation only when the checked-out SHA equals the current
branch head. A pull-request merge ref is `MERGE_RESULT` validation and must name
the synthetic merge SHA. Do not relabel one as the other.

### 3.2 Freeze the file and workflow inventory

At the tested SHA, confirm the existence and current bytes of:

- the four workflows listed in section 2;
- every test, validator, fixture, schema, and receipt referenced by the commands
  below;
- the Hydrology contracts and schema indexes;
- the Hydrology source, proof, and release boundary documents; and
- the active `Makefile`.

Stop when an unexpected substantive test or validator appears, a reserved
placeholder changes, a symlink enters the governed inventory, a required path
disappears, or a dedicated workflow has been replaced without a reviewed
successor.

### 3.3 Use the workflow toolchain

Current workflows use Python 3.11 and install the repository's declared test
dependencies with:

```bash
python tools/ci/install_python_ci.py project-test
```

Use a clean checkout and a materially equivalent environment for base/head
comparison. Do not compare a lockfile-controlled CI run with an ad hoc
environment and call the difference inherited or introduced without additional
evidence.

### 3.4 Preserve deterministic, no-network posture

Set the repository's no-network and deterministic environment before local
execution:

```bash
export KFM_NO_NETWORK=1
export PIP_DISABLE_PIP_VERSION_CHECK=1
export PIP_NO_INPUT=1
export PYTHONDONTWRITEBYTECODE=1
export PYTHONHASHSEED=0
export PYTHONUNBUFFERED=1
export TZ=UTC
```

The Hydrology tests install fail-closed socket, DNS, and URL guards around the
local validators. The environment variable is not, by itself, proof of
runner-level egress isolation. Any observed DNS lookup, socket connection,
external URL access, credential request, or unverified registry access is a
failure of this procedure.

### 3.5 Confirm the aggregate-target hold

```bash
if grep -Eq '^(hydrology-validate|validate-hydrology):' Makefile; then
  echo "HOLD: an unverified Hydrology aggregate target exists"
  exit 1
fi
```

This is an inventory guard. It does not authorize adding, deleting, or rewiring
a target in a documentation change.

[Back to top](#top)

## 4. Reproduce the `domain-hydrology` validation job

The workflow file is authoritative for its CI behavior. The commands below
reproduce its executable bounded test step; they do not duplicate the workflow's
larger inline AST, placeholder, symlink, and exact-inventory readiness program.

### 4.1 Run the seven-module batch and standalone ownership checks

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

### 4.2 Run schema-wrapper and semantic fixture polarity

```bash
python tools/validators/domains/hydrology/validate_evidence_bundle.py \
  fixtures/domains/hydrology/evidence_bundle/valid/valid_1.json

if python tools/validators/domains/hydrology/validate_evidence_bundle.py \
  fixtures/domains/hydrology/evidence_bundle/invalid/invalid_1.json; then
  echo "HOLD: known-invalid Hydrology EvidenceBundle fixture was accepted"
  exit 1
fi

python tools/validators/domains/hydrology/validate_aquifer_observation.py \
  --fixtures

python tools/validators/domains/hydrology/validate_aquifer_context_link.py \
  --fixtures

python tools/validators/domains/hydrology/validate_public_safe_flow_fixture.py \
  fixtures/domains/hydrology/public_safe_flow/valid/public_safe_flow.json

if python tools/validators/domains/hydrology/validate_public_safe_flow_fixture.py \
  fixtures/domains/hydrology/public_safe_flow/invalid/role_location_time_governance_collapse.json; then
  echo "HOLD: known-invalid Hydrology flow fixture was accepted"
  exit 1
fi

python tools/validators/domains/hydrology/validate_nhdplus_waterbody_crosswalk.py \
  --fixtures
```

Expected-invalid rejection is required evidence. A suite that runs only positive
fixtures is incomplete for this runbook.

### 4.3 Interpret the broad job as a set of finite bounded checks

A green broad job records the following named profiles:

- `hydrology-evidence-bundle-alias-shape`
- `hydrology-aquifer-separated-pair-shape`
- `hydrology-public-safe-flow-fixture`
- `hydrology-nhdplus-waterbody-crosswalk`
- `hydrology-adaptive-threshold-proposal`
- `hydrology-hydro-identity-bridge`
- `hydrology-streamflow-qc-context`

It also preserves the explicit broader hold:

`WORKFLOW_HOLD: broader Hydrology semantics, evidence closure, proof, and release remain unestablished`

Do not omit that hold from a handoff merely because all executable checks are
green.

[Back to top](#top)

## 5. Run the dedicated bounded workflows

These workflows own separate validation stories. The broad domain workflow
inventories their validator files but does not execute their fixture suites.

### 5.1 Captured-input USGS Water county normalization

```bash
python -m pytest \
  tests/connectors/usgs/water_data/test_nwis_county_capture.py \
  -q --strict-config --strict-markers

python tools/validators/validate_generated_receipt.py \
  data/receipts/generated/genrec-pass32-nwis-county-capture-20260810.json \
  --repo-root .
```

This validates caller-supplied captured pages and the authoring receipt's
repository integrity. It does not contact USGS, authenticate source bytes, prove
currentness, activate a source, write `RAW`, or resolve evidence.

### 5.2 Fixture-only USGS Water API cutover assessment

```bash
python -m pytest \
  tests/validators/domains/hydrology/usgs_water_api_cutover/test_validate_usgs_water_api_cutover.py \
  -q --strict-config --strict-markers

python tools/validators/validate_generated_receipt.py \
  data/receipts/generated/genrec-hydrology-usgs-water-api-cutover-20260806.json \
  --repo-root .
```

A passing assessment supports the fixture-defined migration classification only.
It does not perform a production cutover or establish a live endpoint,
credential, rights, source-role, or activation decision.

### 5.3 Fixture-only WBD HUC12 material-change assessment

```bash
python -m pytest \
  tests/validators/domains/hydrology/wbd_huc12_material_change/test_validate_wbd_huc12_material_change.py \
  -q --strict-config --strict-markers

python tools/validators/validate_generated_receipt.py \
  data/receipts/generated/genrec-hydrology-wbd-huc12-material-change-20260806.json \
  --repo-root .
```

The finite fixture outcomes are `NO_CHANGE`, `MATERIAL_CHANGE`, `ADD`, and
`REMOVE`. They classify supplied fixtures only. They do not prove a change in
the authoritative WBD source, admit new geometry, or authorize a lifecycle or
release transition.

### 5.4 Receipt boundary

A generated authoring-receipt integrity pass establishes that the tracked
receipt remains internally consistent with its declared repository inputs at the
tested SHA. A receipt records what was generated or checked; it is not an
EvidenceBundle, scientific proof, source authority, policy approval,
PromotionDecision, ReleaseManifest, or publication approval.

[Back to top](#top)

## 6. Profile-by-profile interpretation

Use the narrowest statement supported by the executed profile.

| Profile | A pass demonstrates | A pass does not demonstrate |
|---|---|---|
| EvidenceBundle alias schema wrapper | The proposed Hydrology alias fixture matches the local schema and the known-invalid fixture is rejected | Real EvidenceRef resolution, admissible evidence, citation closure, source authority, or EvidenceBundle truth |
| AquiferObservation | The synthetic observation fixture matches its local schema | Actual aquifer membership, measured accuracy, units, freshness, geometry, or Geology ownership |
| AquiferContextLink | The synthetic relation fixture remains separate from observations and cannot absorb measurements or copied Geology geometry | A verified real-world relation, geometry intersection, or authoritative membership |
| Public-safe FlowObservation | The frozen valid fixture is accepted and the role/location/time/governance-collapse fixture is rejected | Current streamflow, flood status, safe public precision, warning authority, or source currentness |
| NHDPlus waterbody crosswalk | Exact/split/merge/complex fixture cardinality and non-exact abstention behave as encoded | Live NHDPlus identity, geometry comparison, gauge/reach/HUC linkage, or canonical crosswalk truth |
| Adaptive threshold proposal | Finite `KEEP_BASELINE`, `REVIEW_RECALIBRATION`, `HOLD`, and `ERROR` routing with pinned analytical support and no exact replacement threshold | Drought extent, percentile computation, threshold computation, event calling, detector mutation, or operational calibration |
| HydroIdentityBridge | Current NHDPlus identifiers and legacy COMIDs remain distinct; only an exact one-to-one fixture with a JoinReceipt reference may answer | Source activation, live identity reconciliation, geometry comparison, evidence resolution, release, or publication |
| Streamflow QC context assessment | Declared categorical context is routed for bounded review | Computed percentiles or flow, sensor invalidation, hydrologic event declaration, detector authority, or public guidance |
| Environmental ownership isolation | Soil, Atmosphere, and Hydrology fixture ownership boundaries remain distinct | Complete cross-domain ontology, source admission, or scientific integration |
| Captured-input NWIS county normalization | Request-plan and captured-page normalization behavior is deterministic for supplied fixtures | Network transport, source authenticity, source currentness, rights clearance, RAW capture, or public use |
| USGS API cutover assessment | Fixture-defined endpoint-family and migration dependencies are classified deterministically | Production endpoint cutover, source activation, dual-run completion against live services, or deployment |
| WBD HUC12 material change | Supplied geometry and area fixtures produce the expected finite materiality outcome | Authoritative WBD change, approved geometry replacement, catalog update, promotion, or release |
| Generated authoring receipts | Declared tracked inputs and output integrity remain consistent under the receipt validator | Evidence, proof, approval, release, or publication |

### 6.1 Derived and rendered carriers

A drought class, threshold proposal, QC category, crosswalk, map, tile,
hydrograph, index, graph edge, embedding, summary, generated receipt, model
output, or AI text remains a derived or interpretive carrier. None becomes
canonical truth merely because its fixture validator passes.

### 6.2 Source-role anti-collapse

Preserve these distinctions in fixtures, result records, and review text:

- observation is not forecast;
- forecast is not alert;
- alert is not KFM authority;
- regulatory flood-hazard context is not observed inundation;
- model output is not measurement;
- analytical classification is not an event;
- legacy identifier is not a current identifier;
- captured input is not an admitted source snapshot; and
- receipt is not proof.

[Back to top](#top)

## 7. Result and failure classification

Classify the observed result only after pinning exact SHAs, commands, fixtures,
dependencies, and environment.

| Classification | Required evidence | Required action |
|---|---|---|
| `PASS` | All named checks and expected-negative fixtures pass at the recorded SHA | State the exact bounded capability; retain every broader hold |
| `INTRODUCED` | Exact base passes and exact head fails under materially equivalent command, fixture, dependency, and environment evidence | Hold the change and repair or narrow it |
| `INHERITED` | Exact base and exact head fail with the same materially comparable signature | Report separately; do not attribute to the current diff or silently ignore it |
| `RESOLVED` | Exact base fails and exact head passes under materially comparable evidence | Claim resolution only for the exact failure |
| `BASE_DRIFT / INTEGRATION` | Original head/base comparison passes, but a later synthetic merge result fails after base advancement | Reconcile changed base inputs and rerun at the current merge result |
| `ENVIRONMENTAL / FLAKY` | Repeated evidence isolates runner, network, timing, service, or nondeterministic behavior | Retain logs and attempts; do not claim a product pass |
| `UNRESOLVED / NON_COMPARABLE` | SHA, command, dependency, fixture, or environment identity is incomplete or materially different | Use `NEEDS VERIFICATION`; do not guess introduced or inherited |
| `HOLD` | A prerequisite, authority, rights, sensitivity, source, evidence, proof, review, release, correction, or rollback gate is incomplete | Stop at the current review boundary |
| `DENY` | The requested action would violate a trust, safety, rights, sensitivity, public-boundary, or lifecycle rule | Do not execute the action |
| `ERROR` | The procedure cannot produce a valid result | Preserve diagnostics and avoid converting the error into a domain conclusion |

Expected-invalid acceptance is `INTRODUCED` only when an exact, materially
comparable base rejects the same fixture and the exact head accepts it. Without
that comparison, use `UNRESOLVED / NON_COMPARABLE`.

### 7.1 Head and merge-result truthfulness

- `HEAD VALIDATION` binds to the exact branch-head SHA.
- `MERGE-RESULT VALIDATION` binds to the exact synthetic merge SHA.
- A result from an older head is historical after the branch advances.
- A result from an older base does not establish current merge readiness after
  material base drift.
- A green pull-request check is not human review, source admission, release
  approval, deployment approval, promotion approval, or publication approval.

[Back to top](#top)

## 8. Mandatory stop, deny, and escalation conditions

Stop and record `HOLD`, `DENY`, `ERROR`, `ABSTAIN`, or
`NEEDS VERIFICATION` when any of the following applies:

- the exact checkout SHA, branch head, merge result, base, command, dependency
  set, fixture set, or workflow run cannot be established;
- a workflow, test, validator, schema, fixture, authoring receipt, or required
  path differs materially from the frozen inventory;
- a valid fixture is rejected, a known-invalid fixture is accepted, or no
  expected-negative profile is exercised;
- a check attempts DNS, socket, external URL, live endpoint, credential, private
  payload, or source activation;
- a passing shape or polarity check is being used to claim scientific accuracy,
  current conditions, source authenticity, source admission, evidence closure,
  policy approval, proof, release readiness, or public safety;
- source identity, source role, units, time, freshness, geometry, aquifer
  membership, gauge/reach/HUC linkage, rights, license, sensitivity,
  sovereignty, provenance, public-safe precision, correction state, or rollback
  target is assumed rather than demonstrated;
- precise restricted locations, critical infrastructure, Indigenous or Tribal
  cultural information, archaeology, rare-species locations, living-person
  information, proprietary excerpts, credentials, or rights-unclear material
  could enter fixtures, logs, pull requests, or summaries;
- a derived drought class, threshold proposal, map, tile, graph, index,
  embedding, summary, model output, generated receipt, or AI text is treated as
  sovereign truth;
- `build-proof-hydrology` or `publish-dry-run-hydrology` is described as an
  implemented producer rather than an explicit held readiness check;
- an aggregate Hydrology Make target appears without a reviewed contract,
  command owner, fixture set, and workflow update;
- another active branch or pull request owns the same validation surface;
- a requested action would activate a source, mutate lifecycle state, promote,
  release, deploy, publish, widen access, change repository settings, or bypass
  accountable review; or
- current flooding, emergency response, engineering, insurance, navigation,
  dam-operation, water-rights, legal, or regulatory guidance is requested.

Escalate to the accountable domain, source, evidence, policy, rights,
sensitivity, safety, release, or operations steward when the required decision
is outside this runbook's authority. The verified GitHub review route does not,
by itself, prove all specialist assignments or independent approval.

[Back to top](#top)

## 9. Validation record and review handoff

Produce a minimized record that is sufficient to reconstruct the bounded
result without copying sensitive or source-controlled material.

### 9.1 Required fields

| Field | Required content |
|---|---|
| Repository identity | Repository, exact tested SHA, branch or ref, merge base, comparison base, and synthetic merge SHA when applicable |
| Execution identity | Workflow/job or local command, Python/dependency posture, fixture paths, no-network controls, and run attempt |
| Change scope | Exact changed paths and whether any validator, fixture, schema, workflow, source, policy, or release surface changed |
| Results | Per-profile `PASS`, `FAIL`, `HOLD`, `DENY`, `ERROR`, `ABSTAIN`, or `NEEDS VERIFICATION` |
| Negative polarity | Each expected-invalid fixture and confirmation that it was rejected |
| Attribution | `INTRODUCED`, `INHERITED`, `RESOLVED`, `BASE_DRIFT / INTEGRATION`, `ENVIRONMENTAL / FLAKY`, or `UNRESOLVED / NON_COMPARABLE`, with comparison evidence |
| Claim boundary | The precise capability demonstrated and the scientific, evidence, source, policy, proof, release, deployment, publication, and life-safety claims not demonstrated |
| Review state | Requested reviewers, submitted reviews, unresolved threads, and accountable approval state |
| Follow-up | Smallest unresolved verification, repair, or handoff step |
| Rollback | Branch abandonment before merge or reviewed documentation revert/forward correction after merge |

### 9.2 Illustrative record

```yaml
validation_record:
  repository: bartytime4life/Kansas-Frontier-Matrix
  tested_sha: "<40-character SHA>"
  validation_mode: HEAD
  comparison_base_sha: "<40-character SHA>"
  workflow_or_command: ".github/workflows/domain-hydrology.yml#validate-hydrology"
  changed_paths:
    - "docs/runbooks/hydrology/VALIDATION.md"
  no_network:
    kfm_no_network: true
    external_access_observed: false
  profiles:
    hydrology_evidence_bundle_alias_shape: PASS
    hydrology_aquifer_separated_pair_shape: PASS
    hydrology_public_safe_flow_fixture: PASS
    hydrology_nhdplus_waterbody_crosswalk: PASS
    hydrology_adaptive_threshold_proposal: PASS
    hydrology_hydro_identity_bridge: PASS
    hydrology_streamflow_qc_context: PASS
    invalid_fixture_rejection: PASS
    proof_producer: HOLD
    release_dry_run: HOLD
  attribution: PASS
  human_review: ABSENT
  claims:
    demonstrated:
      - "Named bounded fixture profiles passed at the tested SHA."
    not_demonstrated:
      - "Live source, real evidence, scientific, proof, release, deployment, publication, or life-safety authority."
```

This example is a handoff shape, not a repository contract or schema. Do not
store source payloads, credentials, temporary access links, precise restricted
locations, culturally controlled information, or proprietary excerpts in the
record.

[Back to top](#top)

## 10. Acceptance, maintenance, and documentation rollback

### 10.1 Acceptance criteria for this runbook

This document remains current only when:

1. every executable command matches the named workflow at the pinned
   repository revision;
2. the broad workflow's eight accepted domain modules are represented
   accurately;
3. the three dedicated workflows remain separate from the broad domain job;
4. positive and expected-negative fixture behavior is explicit;
5. generated authoring-receipt integrity is separated from evidence and proof;
6. the aggregate Make target remains prohibited unless deliberately introduced
   and verified;
7. proof and release-dry-run jobs are described as explicit holds, not
   implemented producers;
8. exact-head, merge-result, base comparison, and failure attribution rules are
   visible;
9. no live, sensitive, proprietary, culturally controlled, rights-unclear, or
   precise restricted material is required; and
10. validation, human review, source admission, promotion, release, deployment,
    publication, correction, and rollback remain separate states.

### 10.2 Maintenance triggers

Update or supersede this runbook when:

- a named workflow, command, test, validator, schema, fixture, or authoring
  receipt changes;
- a substantive placeholder becomes executable or an executable module becomes
  a placeholder;
- an accepted aggregate Hydrology validation command is introduced;
- a real EvidenceRef resolver, proof producer, candidate contract, release
  dry-run, or rollback drill is admitted;
- source activation or lifecycle writers become operational;
- a workflow no longer provides expected-negative coverage or no-network guards;
  or
- authority, rights, sensitivity, safety, review, release, or public-use
  boundaries change.

Do not change this documentation to make an unverified command look current.
Change the owning implementation first when authorized, validate it, then update
the runbook with exact evidence.

### 10.3 Documentation rollback

Before merge, abandon the change by closing the draft pull request and deleting
only its task-owned branch. After an authorized merge, use a reviewed revert or
a smaller forward correction.

Reverting this Markdown changes documentation bytes only. It does not undo a
source activation, data write, evidence decision, policy decision, lifecycle
transition, proof, release, deployment, publication, correction, withdrawal, or
operational rollback.

### 10.4 Source-lineage boundary

The connected Hydrology planning reports support fixture-first, no-network,
evidence-aware design, but their repository state and proposed commands were
recorded without a mounted checkout. They remain design lineage. Notion is a
coordination surface. Current GitHub contracts, schemas, tests, validators,
workflows, and exact revision evidence control statements about present
behavior.

[Back to top](#top)

## 11. Related repository surfaces

- [Hydrology operational procedure index](./README.md)
- [Hydrology source-refresh boundary](./SOURCE_REFRESH_RUNBOOK.md)
- [Hydrology promotion preflight](./PROMOTION_RUNBOOK.md)
- [Hydrology rollback planning](./ROLLBACK_RUNBOOK.md)
- [Hydrology domain boundary](../../domains/hydrology/README.md)
- [Hydrology semantic contracts](../../../contracts/domains/hydrology/README.md)
- [Hydrology schema index](../../../schemas/contracts/v1/domains/hydrology/README.md)
- [Hydrology fixtures](../../../fixtures/domains/hydrology/README.md)
- [Hydrology tests](../../../tests/domains/hydrology/README.md)
- [Hydrology validators](../../../tools/validators/domains/hydrology/README.md)
- [Hydrology proof boundary](../../../data/proofs/hydrology/README.md)
- [Hydrology release-candidate boundary](../../../release/candidates/hydrology/README.md)
- [Directory governance](../../doctrine/directory-rules.md)
- [ADR-0009 — Hydrology proof-bearing lane](../../adr/ADR-0009-hydrology-is-the-first-proof-bearing-lane.md)
- [ADR-0026 — WBD HUC12 source spine](../../adr/ADR-0026-hydrology-source-spine-starts-with-wbd-huc12.md)
- [ADR-0029 — Directory governance adoption](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)

[Back to top](#top)
