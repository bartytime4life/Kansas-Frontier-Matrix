<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook-hydrology-no-network-test
title: Hydrology No-Network Test Runbook
type: operational-runbook
version: v2.0.0
status: DRAFT_REPOSITORY_GROUNDED; BOUNDED_SYNTHETIC_VALIDATION_ONLY; BROADER_TRUST_SPINE_HELD; NON_RELEASE; NON_PUBLICATION
owners: "@bartytime4life — verified CODEOWNERS route; accountable Hydrology, source, identity, validation, policy, QA, proof, and release stewardship NEEDS VERIFICATION"
created: 2026-05-12
updated: 2026-08-27
policy_label: repository-facing; hydrology; no-network; synthetic-only; fail-closed; not-for-life-safety; non-publisher
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
  target_path: docs/runbooks/hydrology/NO_NETWORK_TEST_RUNBOOK.md
  target_prior_blob: 1a2a1480b7f2fe3d52aabd815395ac1b8fb97395
  directory_rules_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  source_authority_register_blob: 32729857bc8eb5001acb37b8ee8e60bcb6e0dc50
  domain_workflow_blob: 36a0287be04639cb75dc77ae2c274fee626f6a00
  usgs_cutover_workflow_blob: 33d2091cf2f9d954adbff5e785361bcc196f0c93
  wbd_material_change_workflow_blob: e3edd2c98b708c170df84cef10d883d2c42b2b61
  evidence_bundle_test_blob: 489b2e1ba0fb7fed3db89a34be9d5531f1975a77
  aquifer_observation_test_blob: 37d22fd7897b321b11c6d560b8486fe06f9885df
  aquifer_context_link_test_blob: 1527c7e1b6ef67f995be6f6520a477b4ee2dbc77
  public_safe_flow_test_blob: 0ea72c4ad930f2ca95a5296aaf67ae4a53d65ef3
  nhdplus_crosswalk_test_blob: cfa57d48fc7c8738993bf082e7783bab260c3f2b
  adaptive_threshold_test_blob: f9a485607e68eeb363e7640d8d29599fb670d021
  hydro_identity_bridge_test_blob: 3e40105de52fff05d2d5e7ead274dd010f729a88
  streamflow_qc_test_blob: a76f0a820a8ce528d220d7aa97d0371115f3bc50
  environmental_boundary_test_blob: 82177ebb8888bd753b5cc4d4b42771179cfcb5ee
  local_link_checker_blob: c5aff503e306709bc193e1b64f934675631dca95
  open_pull_requests_touching_target: 0
source_lineage:
  - title: KFM_Hydrology_Extended_Pro_PDF_Only_Reference_Report_2026-04-21.pdf
    source_class: PLANNING_LINEAGE
    use: Hydrology-first, HUC12, identity-ambiguity, source-role, temporal, offline-first, and public-boundary design context only
  - title: KFM Evidence, Documentation & Ideas Atlas — 2026-08-24
    source_class: COORDINATION_LINEAGE
    use: Notion coordination and maturity-separation context only; repository bytes remain authoritative
  - title: KFM Markdown Update & Modernization Agent v1.0
    source_class: CURRENT_TASK_GUIDANCE
    use: same-path repository-grounded Markdown modernization and reversible delivery method
related:
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../doctrine/directory-rules.md
  - ../README.md
  - ../../domains/hydrology/README.md
  - ../../domains/hydrology/BOUNDARY.md
  - ../../domains/hydrology/PUBLICATION_POSTURE.md
  - ../../domains/hydrology/SOURCE_ROLE_MATRIX.md
  - PROMOTION_RUNBOOK.md
  - ROLLBACK_RUNBOOK.md
  - SOURCE_REFRESH_RUNBOOK.md
  - VALIDATION.md
  - ../../../.github/workflows/domain-hydrology.yml
  - ../../../.github/workflows/hydrology-usgs-water-api-cutover.yml
  - ../../../.github/workflows/hydrology-wbd-huc12-material-change.yml
  - ../../../tests/domains/hydrology/README.md
  - ../../../tests/cross_domain/test_environmental_observation_boundaries.py
  - ../../../tools/validators/domains/hydrology/README.md
  - ../../../policy/domains/hydrology/README.md
  - ../../../data/registry/sources/hydrology/README.md
  - ../../../control_plane/source_authority_register.yaml
  - ../../../release/candidates/hydrology/README.md
notes:
  - The current executable lane proves bounded synthetic schema, fixture-polarity, type-separation, identity, materiality, and context-routing behavior. It does not prove real Hydrology truth or complete the KFM trust spine.
  - KFM_NO_NETWORK and in-process socket, DNS, URL, or import guards constrain the named profiles. They are not operating-system air-gap or firewall evidence.
  - The domain workflow's proof and release jobs are explicit readiness holds. A green held job is not evidence closure, policy approval, review, proof, release, promotion, deployment, or publication.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hydrology No-Network Test Runbook

> **One-line purpose.** Run KFM's current bounded Hydrology validation against committed synthetic fixtures without contacting live water sources, then record exactly what passed, what remained held, and why the result creates no hydrologic, life-safety, regulatory, source-admission, proof, release, or publication authority.

[![Status: bounded synthetic validation](https://img.shields.io/badge/status-bounded%20synthetic%20validation-8250df?style=flat-square)](#current-disposition)
[![Network: live sources forbidden](https://img.shields.io/badge/live%20sources-forbidden-b42318?style=flat-square)](#what-no-network-means)
[![Life safety: no](https://img.shields.io/badge/life%20safety-not%20an%20alerting%20system-b42318?style=flat-square)](#not-for-life-safety-boundary)
[![Proof and release: held](https://img.shields.io/badge/proof%20%2F%20release-held-6e7781?style=flat-square)](#explicit-holds-and-unproved-behavior)
[![Public effect: none](https://img.shields.io/badge/public%20effect-none-6e7781?style=flat-square)](#authority-and-terminal-boundary)

<a id="not-for-life-safety-boundary"></a>

> [!CAUTION]
> **KFM Hydrology is not an emergency-alerting, navigation, engineering, insurance, permitting, or regulatory-determination system.** This procedure does not retrieve or validate current water conditions. It must not be used to issue, replace, delay, retract, summarize as actionable, or interpret flood warnings, evacuation instructions, navigation guidance, engineering conclusions, insurance determinations, permit decisions, or official regulatory interpretations. Direct current or urgent needs to the appropriate official authority.

<a id="current-disposition"></a>

> [!IMPORTANT]
> **Current disposition: `BOUNDED_SYNTHETIC_VALIDATION / BROADER_TRUST_SPINE_HOLD`.** At the pinned repository snapshot, the Hydrology workflow executes eight bounded domain modules, one cross-domain ownership-isolation test, five local schema/semantic validator paths, and expected-invalid fixture rejection. Two dedicated fixture-only workflows separately validate a USGS Water API cutover assessment and WBD HUC12 material-change assessment. Live source access, source activation, actual EvidenceRef resolution, accepted policy evaluation, proof production, candidate assembly, release dry-run execution, deployment, and publication are not established by these checks.

**Quick navigation:** [Goal](#goal-and-scope) · [Authority](#authority-and-terminal-boundary) · [Current evidence](#current-repository-evidence) · [No-network meaning](#what-no-network-means) · [Preconditions](#preconditions) · [Run](#run-the-current-bounded-profile) · [Dedicated profiles](#run-the-dedicated-fixture-only-profiles) · [Interpretation](#interpret-the-results) · [Coverage](#covered-behavior) · [Holds](#explicit-holds-and-unproved-behavior) · [Failures](#failure-handling) · [Hermetic mode](#stronger-hermetic-execution) · [Handoff](#pull-request-and-review-handoff) · [Rollback](#rollback-path) · [Maintenance](#maintenance-and-verification-backlog)

---

<a id="goal-and-scope"></a>

## Goal and scope

Use this runbook when a change touches the current Hydrology schemas, committed fixtures, bounded validators, accepted test modules, domain workflow, dedicated cutover/material-change workflows, or documentation that describes those surfaces.

The current executable circle is:

```text
committed synthetic Hydrology fixtures
  -> JSON Schema 2020-12 shape and exact valid/invalid polarity
  -> bounded semantic validation and deterministic identity checks
  -> in-process network-denial or no-network-dependency checks
  -> finite fixture-profile outcomes
  -> bounded validation result and review handoff
```

### In scope

- the proposed Hydrology `EvidenceBundle` alias fixture pair;
- the separated `AquiferObservation` and `AquiferContextLink` shapes;
- the frozen synthetic public-safe `FlowObservation` profile;
- the synthetic, waterbody-only NHDPlus HR/legacy identifier crosswalk profile;
- the fixture-only adaptive-threshold review proposal;
- the source-native `HydroIdentityBridge` profile;
- the fixture-only streamflow quality-control context assessment;
- the Soil/Atmosphere/Hydrology ownership-isolation check;
- the fixture-only USGS Water API cutover assessment;
- the fixture-only WBD HUC12 material-change assessment;
- exact current commands, finite results, expected-invalid rejection, and documentation validation; and
- explicit proof, release, source, policy, and public-use holds.

### Out of scope

- USGS Water Data, WBD, NHDPlus HR, FEMA NFHL, 3DEP, state, local, or other live-source access;
- current streamflow, groundwater, water quality, flood, drought, watershed, or regulatory conditions;
- source admission, credentials, rights acceptance, source activation, connector execution, or lifecycle writes;
- real endpoint resolution, real gauge/reach/HUC/aquifer membership, or real source-row verification;
- EvidenceRef-to-EvidenceBundle closure, accepted Hydrology policy evaluation, ProofPack construction, candidate assembly, release, deployment, promotion, or publication;
- production network isolation, firewall enforcement, or air-gap certification; and
- writes to RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, receipt, proof, release, or PUBLISHED stores.

[Back to top](#top)

---

<a id="authority-and-terminal-boundary"></a>

## Authority and terminal boundary

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) and the adopted [Directory Rules v2](../../doctrine/directory-rules.md) place human operational procedures under `docs/runbooks/`, executable validation under `tools/` and `tests/`, machine shape under `schemas/`, semantic meaning under `contracts/`, policy under `policy/`, lifecycle objects under governed `data/` phases, and release decisions under `release/`.

This is a same-path modernization of an established file. It creates no new responsibility root or parallel contract, schema, source, policy, evidence, receipt, proof, release, or publication home.

| Responsibility | Owning surface | This runbook's role |
|---|---|---|
| Human procedure | `docs/runbooks/hydrology/NO_NETWORK_TEST_RUNBOOK.md` | Explain current bounded commands, outcomes, limits, and handoff |
| Hydrology meaning | `contracts/domains/hydrology/` | Link and consume; do not redefine |
| Machine shape | `schemas/contracts/v1/domains/hydrology/` | Validate current profiles; do not treat shape as truth |
| Synthetic examples | `fixtures/domains/hydrology/` and `fixtures/contracts/v1/domains/hydrology/` | Exercise reviewed fixture profiles; do not substitute them for source evidence |
| Executable behavior | `tests/domains/hydrology/`, selected `tests/validators/`, `tests/cross_domain/`, and `tools/validators/domains/hydrology/` | Provide the actual bounded implementation evidence |
| CI orchestration | `.github/workflows/domain-hydrology.yml` and two dedicated Hydrology workflows | Run the exact fixture-only profiles and preserve explicit holds |
| Source authority | Source registry and accepted activation decisions | Remains separate; current projection is empty and non-activating |
| Policy, evidence, proof, and release | Their existing responsibility roots | Remain outside this procedure unless separately implemented, accepted, and governed |

The highest result this runbook can establish is:

```text
BOUNDED_SYNTHETIC_VALIDATION_PASS
```

That result is not `SOURCE_ADMITTED`, `SOURCE_ACTIVATED`, `LIVE_SOURCE_VALIDATED`, `EVIDENCE_RESOLVED`, `POLICY_APPROVED`, `REVIEWED`, `PROOF_COMPLETE`, `RELEASED`, `DEPLOYED`, `PROMOTED`, or `PUBLISHED`.

[Back to top](#top)

---

<a id="current-repository-evidence"></a>

## Current repository evidence

The observations below are pinned to `main@b7663990b81cb3b29fd2891c24720cc1064ebe95`. Re-read the exact files when the base, workflow, schemas, fixtures, tests, validators, source registry, policy lane, proof lane, or release lane changes.

| Surface | CONFIRMED repository evidence | Bounded conclusion |
|---|---|---|
| Domain workflow | `.github/workflows/domain-hydrology.yml` runs Python 3.11, installs the hash-locked `project-test` profile, checks an explicit test/validator/source-spec inventory, executes eight bounded domain modules plus the cross-domain ownership test, and preserves proof/release holds | Current repository-owned broad Hydrology entry point |
| EvidenceBundle alias | `test_hydrology_smoke.py` validates one valid and one invalid local alias fixture and patches socket, DNS, and URL entry points to fail closed | Shape and fixture polarity only; not EvidenceRef resolution or evidence closure |
| Aquifer pair | `test_aquifer_observation.py` and `test_aquifer_context_link.py` validate closed local shapes, optional linkage, typed endpoint references, responsibility separation, and network denial | Does not establish real aquifer membership, source validity, or Geology authority transfer |
| Public-safe flow | `test_public_safe_flow_fixture.py` checks exact fixture inventory, measurement bounds, time ordering, location minimization, closed shapes, duplicate/nonfinite JSON rejection, size bounds, CLI behavior, and network denial | Synthetic observation-profile behavior only; not a real reading or warning |
| NHDPlus waterbody crosswalk | `test_nhdplus_hr_ambiguity.py` checks exact/split/merge/complex cardinality, deterministic identity, ordering, bounded input, CLI behavior, and non-exact `ABSTAIN` | Waterbody-only synthetic crosswalk; not live reach/HUC/gauge identity |
| Adaptive threshold | `test_adaptive_threshold_proposal.py` validates deterministic packets with `KEEP_BASELINE`, `REVIEW_RECALIBRATION`, `HOLD`, and `ERROR`, while rejecting exact threshold recommendation or configuration mutation | Review-routing proposal only; computes no threshold or hydrologic event |
| Hydro identity bridge | `test_hydro_identity_bridge.py` preserves current and legacy identifier families, allows bounded `ANSWER` only for an exact one-to-one receipt-backed bridge, abstains on ambiguity, and denies legacy relabeling | No source activation, geometry comparison, evidence resolution, release, or public lookup |
| Streamflow QC context | `test_streamflow_qc_context_assessment.py` validates exact PASS/ABSTAIN/DENY/ERROR fixture polarity and source/context separation without numeric flow or percentile values | Context-routing assessment only; invalidates no sensor and declares no event |
| Cross-domain boundary | `test_environmental_observation_boundaries.py` proves Soil, Atmosphere, and Hydrology validators accept only their own fixture profile even when place/time overlap | Shared place and time do not transfer domain authority |
| Dedicated USGS cutover workflow | `hydrology-usgs-water-api-cutover.yml` validates fixture-only endpoint-family, required-role, rewrite-map, legacy-dependency, dual-run reconciliation, and generated-receipt integrity | No live USGS call, connector activation, hydrologic assertion, or release effect |
| Dedicated WBD material-change workflow | `hydrology-wbd-huc12-material-change.yml` validates geometry normalization, geometry-plus-area fingerprints, metadata-churn suppression, finite material-change states, and generated-receipt integrity | No WBD request, source activation, lifecycle write, or release effect |
| Source authority | `control_plane/source_authority_register.yaml` is `PROPOSED`, projection-only, implementation `ABSENT`, complete as empty, and contains no entries | No source is admitted or activated by the register |
| Source/spec readiness | The domain workflow requires selected Hydrology source and pipeline YAML files to remain explicit `PROPOSED` placeholders | Source/spec presence is a readiness hold, not implementation |
| Policy | `policy/domains/hydrology/README.md` records mixed direct scaffolds, no accepted Hydrology bundle/evaluator binding, and no established production consumer | Fixture checks are not operational policy enforcement |
| Proof and release | The domain workflow's proof and release-dry-run jobs explicitly hold when no accepted producer, command, candidate, or manifest contract exists | A green held job is readiness-boundary evidence only |

The April Drive Hydrology report remains useful planning lineage for HUC12, source-role separation, identity ambiguity, time, evidence, and offline-first design. Its no-mounted-repository assumptions and proposed paths do not override current repository evidence. The Notion Atlas remains coordination evidence and does not prove exact-current-main behavior.

[Back to top](#top)

---

<a id="what-no-network-means"></a>

## What no-network means

The phrase **no-network** has several distinct layers. Do not collapse them.

| Layer | Current status | What may be claimed |
|---|---|---|
| Live Hydrology sources | **CONFIRMED forbidden by these profiles** | The named tests and validators consume committed fixtures and require no live water endpoint |
| Python test process | **CONFIRMED bounded guards** | Several modules patch socket connection, DNS resolution, and URL opening; other modules inspect for network-client imports or execute only local parsing/validation |
| Workflow declaration | **CONFIRMED** | `KFM_NO_NETWORK=1` is set for the bounded jobs or commands where declared |
| Runner or operating system | **NEEDS VERIFICATION** | The environment variable and Python guards do not prove firewall, namespace, proxy, DNS, or host-level egress denial |
| Dependency bootstrap | **SEPARATE PRECONDITION** | `python tools/ci/install_python_ci.py project-test` may use an approved cache or package network before the focused run; that acquisition is not part of the no-live-source claim |
| External documentation links | **NOT REQUESTED BY LOCAL LINK CHECKER** | The repository link checker validates local files/fragments and records external targets without fetching them |

> [!WARNING]
> Do not call a run hermetic, air-gapped, or infrastructure-level no-egress unless the execution environment independently enforces and records that property. Do not disable, bypass, or weaken an in-process guard to make a fixture test pass.

[Back to top](#top)

---

<a id="preconditions"></a>

## Preconditions

1. Work from a clean checkout or isolated worktree at a recorded 40-character commit SHA.
2. Run from the repository root.
3. Use Python 3.11 for hosted-workflow parity unless the workflow pin changes.
4. Ensure the workflow, schemas, fixtures, tests, and validators are from the same revision.
5. Keep live-source URLs, API keys, tokens, credentials, production extracts, and operational payloads out of the focused environment.
6. Install dependencies through the repository-owned `project-test` profile when the environment does not already provide them.
7. Do not substitute the currently held shorthand validators under `tools/validators/hydro/` for the accepted bounded domain validators.

Dependency bootstrap:

```bash
python tools/ci/install_python_ci.py project-test
```

Record before running:

```bash
git rev-parse HEAD
git status --short
python --version
```

> [!NOTE]
> Run dependency installation before applying external network containment, or use an approved pre-populated cache or wheelhouse. Record bootstrap separately from fixture validation. A successful install is dependency/bootstrap evidence, not Hydrology validation evidence.

[Back to top](#top)

---

<a id="run-the-current-bounded-profile"></a>

## Run the current bounded profile

Set the deterministic environment used by the repository:

```bash
export KFM_NO_NETWORK=1
export PYTHONHASHSEED=0
export PYTHONDONTWRITEBYTECODE=1
export PYTHONUNBUFFERED=1
export TZ=UTC
```

Run the exact bounded domain modules:

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

Run the explicit validator paths and expected-invalid rejection:

```bash
python tools/validators/domains/hydrology/validate_evidence_bundle.py \
  fixtures/domains/hydrology/evidence_bundle/valid/valid_1.json

if python tools/validators/domains/hydrology/validate_evidence_bundle.py \
  fixtures/domains/hydrology/evidence_bundle/invalid/invalid_1.json; then
  echo "ERROR: known-invalid Hydrology EvidenceBundle fixture was accepted" >&2
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
  echo "ERROR: known-invalid Hydrology flow fixture was accepted" >&2
  exit 1
fi

python tools/validators/domains/hydrology/validate_nhdplus_waterbody_crosswalk.py \
  --fixtures
```

For a change to this runbook, also run the repository-local link checker:

```bash
python tools/validators/docs/link-check/check_links.py \
  --repo-root . \
  --format text \
  docs/runbooks/hydrology/NO_NETWORK_TEST_RUNBOOK.md
```

> [!IMPORTANT]
> There is no accepted `make hydrology-validate` or `make validate-hydrology` target at the pinned snapshot. The domain workflow intentionally fails if one appears without deliberate wiring and review. Do not document or invent an aggregate Make target until the repository establishes it.

[Back to top](#top)

---

<a id="run-the-dedicated-fixture-only-profiles"></a>

## Run the dedicated fixture-only profiles

The two profiles below are independent of the broad domain-readiness workflow. Run them when their own changed paths are in scope.

### USGS Water API cutover assessment

```bash
python -m pytest \
  tests/validators/domains/hydrology/usgs_water_api_cutover/test_validate_usgs_water_api_cutover.py \
  -q --strict-config --strict-markers

python tools/validators/validate_generated_receipt.py \
  data/receipts/generated/genrec-hydrology-usgs-water-api-cutover-20260806.json \
  --repo-root .
```

This profile evaluates declared endpoint families, required source roles, rewrite mappings, legacy dependencies, and dual-run reconciliation. It does not contact USGS or activate a connector.

### WBD HUC12 material-change assessment

```bash
python -m pytest \
  tests/validators/domains/hydrology/wbd_huc12_material_change/test_validate_wbd_huc12_material_change.py \
  -q --strict-config --strict-markers

python tools/validators/validate_generated_receipt.py \
  data/receipts/generated/genrec-hydrology-wbd-huc12-material-change-20260806.json \
  --repo-root .
```

This profile evaluates normalized geometry, geometry-plus-area fingerprints, metadata-only churn, and finite `ADD`, `REMOVE`, `NO_CHANGE`, or `MATERIAL_CHANGE` assessment states. It does not request WBD data or authorize lifecycle movement.

Generated-receipt validation proves only that the recorded authoring artifact still matches its declared bytes and references. It is not a source receipt, EvidenceBundle, ProofPack, policy decision, review record, or release approval.

[Back to top](#top)

---

<a id="interpret-the-results"></a>

## Interpret the results

### Overall validation result

Use this finite classification for the runbook-level handoff:

| Result | Meaning | Next action |
|---|---|---|
| `BOUNDED_SYNTHETIC_VALIDATION_PASS` | Every selected command passed, expected-invalid inputs were rejected, and no network guard was bypassed | Record exact SHA and commands; preserve all broader holds |
| `BOUNDED_SYNTHETIC_VALIDATION_FAIL` | A fixture, schema, validator, inventory, polarity, or boundary check failed | Repair the owning surface before relying on the profile |
| `NOT_RUN` | The command was unavailable or outside the changed scope | Record it explicitly; never translate to pass |
| `ERROR` | The environment or validator could not evaluate the profile safely | Repair the execution/input problem; do not infer a domain result |

### Profile-local finite outcomes

Some fixtures carry their own finite semantic outcomes. Those outcomes stay inside their profiles:

| Profile | Finite outcomes currently exercised | Bounded meaning |
|---|---|---|
| NHDPlus waterbody crosswalk | `ANSWER`, `ABSTAIN` | Exact relation may answer; split/merge/complex ambiguity remains unresolved |
| Hydro identity bridge | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` | Exact receipt-backed bridge, ambiguity, legacy relabeling, or operational result |
| Streamflow QC context | `PASS`, `ABSTAIN`, `DENY`, `ERROR` | Declared context is accepted, insufficient, forbidden, or malformed |
| Adaptive threshold proposal | `KEEP_BASELINE`, `REVIEW_RECALIBRATION`, `HOLD`, `ERROR` | Review routing only; no exact threshold or detector mutation |
| Validators | `PASS`, `FAIL`, `ERROR` through exit codes | Machine conformance result, not a public answer or policy decision |

A profile-local `ANSWER` is not proof that a real hydrologic claim is true, current, policy-approved, reviewed, released, or publishable.

### Required handoff facts

Record:

- exact repository SHA and dirty-state note;
- dependency bootstrap method and whether it used external access;
- exact commands and exit codes;
- selected fixture/profile results;
- expected-invalid rejection result;
- network-enforcement mechanism actually used;
- dedicated-profile receipt checks when run;
- skipped or unavailable commands;
- unresolved source, evidence, policy, proof, candidate, release, and public-use holds; and
- `live_source_access: NOT_RUN`.

[Back to top](#top)

---

<a id="covered-behavior"></a>

## Covered behavior

| Profile | Covered behavior | Explicit limit |
|---|---|---|
| EvidenceBundle alias | Draft 2020-12 shape, one valid/invalid pair, CLI polarity, selected socket/DNS/URL denial | No EvidenceRef lookup, bundle closure, citation authority, or proof |
| AquiferObservation | Closed observation shape, optional context link, observed role, fixture polarity | No real well/aquifer/source identity or measurement truth |
| AquiferContextLink | Typed Hydrology/Geology endpoints; rejects copied geometry and measurement payload | No endpoint resolution or authority transfer |
| Public-safe flow | Measurement and no-data bounds, time order, county-level support, precise-field denial, deterministic findings, input safety, value-minimized CLI | No real gauge reading, currentness, flood warning, policy, or release |
| NHDPlus crosswalk | Waterbody-only exact/split/merge/complex relations, hash/order/cardinality/area checks, ambiguity abstention | No live NHDPlus/legacy source comparison or reach/HUC lookup |
| Adaptive threshold | Deterministic review packet, finite review states, required baseline/materiality support, no exact threshold/config mutation | No drought extent, percentile, threshold, detector, event, or configuration write |
| Hydro identity bridge | Current/legacy identity separation, exact receipt-backed answer, ambiguity abstention, relabel denial, bounded input and CLI | No geometry comparison, source activation, public lookup, or release |
| Streamflow QC context | Exact fixture polarity, categorical context separation, no raw value/threshold admission, finite minimized output | No percentile computation, sensor invalidation, event declaration, or policy authority |
| Environmental ownership | Soil, Atmosphere, and Hydrology fixtures remain mutually non-interchangeable | Does not establish cross-domain join acceptance |
| USGS cutover assessment | Endpoint-family and migration/cutover packet consistency | No live endpoint behavior or connector readiness |
| WBD material change | Fixture-only normalized geometry and material-change semantics | No live source retrieval or accepted update |

[Back to top](#top)

---

<a id="explicit-holds-and-unproved-behavior"></a>

## Explicit holds and unproved behavior

The following states remain separate even when every bounded check is green.

| Surface | Current state | Why it remains held |
|---|---|---|
| Source authority | `PROPOSED / projection_only / entries: []` | The source-authority register creates no admission or activation |
| Hydrology source descriptors and pipeline specs | Selected records are explicit proposal placeholders | No accepted descriptor/spec and controlled live execution path is established |
| Shorthand validators | `tools/validators/hydro/` remains placeholder/proposed scaffolding | Do not use as an aggregate or substitute implementation |
| Broader Hydrology semantics | Workflow hold | Many source, identity, temporal, endpoint, freshness, NFHL, public-geometry, and policy questions remain outside the bounded profiles |
| Actual evidence closure | Not established | The EvidenceBundle alias test validates local shape and polarity, not EvidenceRef resolution or source support |
| Hydrology policy enforcement | Evaluator unbound / mixed scaffolds | No accepted bundle, result-normalization contract, obligation handlers, or production consumer |
| Proof production | `WORKFLOW_HOLD` | No accepted producer or deterministic proof command |
| Candidate and release dry run | `WORKFLOW_HOLD` | No accepted candidate packet, manifest contract, or domain release command |
| Human review | Needs verification | CODEOWNERS routes a GitHub account; it does not prove functional or independent review |
| Host-level no-egress | Needs verification | Python guards and environment variables do not prove infrastructure containment |
| Release, deployment, promotion, publication | None | These require separate governed transitions and authority |

Do not convert a green `build-proof-hydrology` or `publish-dry-run-hydrology` job into proof or release evidence when the job's successful behavior is to record an explicit hold.

[Back to top](#top)

---

<a id="failure-handling"></a>

## Failure handling

### Classify the failure first

| Failure | Classification | Required response |
|---|---|---|
| Known-invalid fixture is accepted | **Invariant regression** | Stop; repair validator/schema/profile before relying on any pass |
| Network-denial assertion no longer fires | **False-assurance risk** | Stop; restore or replace the guard and document the exact enforcement layer |
| Unexpected substantive test/validator appears outside the accepted inventory | **Readiness transition detected** | Review and wire it deliberately; do not let the broad workflow silently adopt it |
| Accepted test/validator regresses to placeholder | **Implementation regression** | Restore executable behavior or explicitly retire it through reviewed change |
| Source/spec placeholder loses its proposal markers | **Source-governance transition detected** | Verify descriptor authority, rights, activation, implementation, tests, and rollback before changing the hold |
| Schema or fixture polarity changes | **Changed contract/profile** | Update the owning semantic contract, migration note, fixtures, and tests together as applicable |
| Generated receipt integrity fails | **Artifact/receipt closure failure** | Repair the owning generated artifact or successor receipt; do not relabel as unrelated |
| Non-deterministic identity/order finding appears | **Reproducibility failure** | Stop and reconcile canonicalization before accepting new artifacts |
| Proof/candidate artifact appears while hold logic remains | **Authority-boundary drift** | Replace the hold only after the accepted contract, validator, review, and command path exist |
| Local link checker reports a missing file/anchor | **Documentation regression** | Repair the changed link or preserve a compatibility anchor |
| Environment cannot install dependencies | **Bootstrap error** | Record `ERROR` or `NOT_RUN`; use an approved cache/wheelhouse rather than weakening test requirements |

### Severity guidance

- **P0:** live-source or public-boundary breach; network access succeeds unexpectedly; a forbidden role becomes an answer; a known-invalid profile passes.
- **P1:** accepted bounded validator/test regresses; proof/release hold is bypassed; expected finite outcome changes without review.
- **P2:** fixture/schema/link/inventory drift with no external effect.
- **P3:** environmental/bootstrap problem proven unrelated to changed semantics.

Do not loosen a test merely to remove a failure. Where the test enforces a KFM invariant, weakening it is a behavior change that requires its own evidence and review.

[Back to top](#top)

---

<a id="stronger-hermetic-execution"></a>

## Stronger hermetic execution

The current profile is **fixture-only and process-guarded**, not infrastructure-certified. A stronger local or hosted run may add independently verified containment after dependencies are available.

Record all applicable controls:

- dependency cache or wheelhouse identity;
- container or virtual-environment identity;
- network namespace, firewall, proxy, and DNS policy;
- whether loopback remained available;
- filesystem write restrictions;
- environment variables and secret inventory;
- runner image and tool versions;
- confirmation that no source URL or credential entered the process; and
- evidence that a deliberate egress probe was denied by the external mechanism.

Do not place an illustrative firewall or container command in this runbook as though it were the repository standard. Use the owning CI/operations control once it is accepted, then update this section with the exact command and evidence.

[Back to top](#top)

---

<a id="pull-request-and-review-handoff"></a>

## Pull-request and review handoff

Use this documentation-only record for a changed-area handoff. It creates no receipt, review, policy, proof, source, release, or publication object.

```yaml
hydrology_no_network_handoff:
  repository:
    sha: "<40-character SHA>"
    dirty_paths: []
    changed_paths: []
  environment:
    python: "<version>"
    dependency_profile: "project-test"
    dependency_bootstrap: "<command/result>"
    bootstrap_external_access: "<NONE | CACHE | PACKAGE_NETWORK | UNKNOWN>"
    network_enforcement:
      process_guards: "<verified controls>"
      host_or_runner_control: "<control or NOT_ESTABLISHED>"
  broad_profile:
    pytest_modules: "<PASS | FAIL | ERROR | NOT_RUN>"
    public_safe_flow: "<PASS | FAIL | ERROR | NOT_RUN>"
    environmental_boundary: "<PASS | FAIL | ERROR | NOT_RUN>"
    evidence_bundle_valid: "<PASS | FAIL | ERROR | NOT_RUN>"
    evidence_bundle_invalid_rejected: "<PASS | FAIL | ERROR | NOT_RUN>"
    aquifer_observation: "<PASS | FAIL | ERROR | NOT_RUN>"
    aquifer_context_link: "<PASS | FAIL | ERROR | NOT_RUN>"
    public_safe_flow_invalid_rejected: "<PASS | FAIL | ERROR | NOT_RUN>"
    nhdplus_waterbody_crosswalk: "<PASS | FAIL | ERROR | NOT_RUN>"
  dedicated_profiles:
    usgs_cutover: "<PASS | FAIL | ERROR | NOT_RUN>"
    usgs_cutover_receipt: "<PASS | FAIL | ERROR | NOT_RUN>"
    wbd_material_change: "<PASS | FAIL | ERROR | NOT_RUN>"
    wbd_material_change_receipt: "<PASS | FAIL | ERROR | NOT_RUN>"
  documentation:
    local_link_check: "<PASS | FAIL | ERROR | NOT_RUN>"
  authority:
    live_source_access: "NOT_RUN"
    source_activation_effect: "NONE"
    lifecycle_effect: "NONE"
    policy_approval_effect: "NONE"
    proof_effect: "NONE"
    release_effect: "NONE"
    deployment_effect: "NONE"
    promotion_effect: "NONE"
    publication_effect: "NONE"
  holds:
    - "SOURCE_AUTHORITY_REGISTER_EMPTY"
    - "SELECTED_SOURCE_AND_PIPELINE_RECORDS_PROPOSED"
    - "BROADER_HYDROLOGY_SEMANTICS_UNESTABLISHED"
    - "EVIDENCE_RESOLUTION_UNESTABLISHED"
    - "POLICY_EVALUATOR_UNBOUND"
    - "PROOF_PRODUCER_UNESTABLISHED"
    - "RELEASE_DRY_RUN_UNESTABLISHED"
    - "HOST_LEVEL_EGRESS_NEEDS_VERIFICATION"
```

Preserve `NOT_RUN`, `NOT_ESTABLISHED`, and `UNKNOWN`; do not normalize them to pass.

[Back to top](#top)

---

<a id="rollback-path"></a>

## Rollback path

This is a Markdown-only, same-path modernization.

To reverse only this documentation change:

1. revert the documentation commit; or
2. restore prior blob `1a2a1480b7f2fe3d52aabd815395ac1b8fb97395` at this path;
3. rerun the local link checker; and
4. verify the resulting diff contains no unrelated path changes.

Reverting this file changes no source descriptor, connector, fixture, schema, test, validator, workflow, lifecycle object, policy, evidence, receipt, proof, candidate, release, deployment, promotion, or publication state.

For actual Hydrology candidate or released-state recovery, use the owning [Rollback Runbook](./ROLLBACK_RUNBOOK.md) under accountable release authority. A synthetic rollback or green workflow hold is not production recovery proof.

[Back to top](#top)

---

<a id="maintenance-and-verification-backlog"></a>

## Maintenance and verification backlog

Reconcile this runbook whenever any of these surfaces changes:

- `.github/workflows/domain-hydrology.yml`;
- the accepted Hydrology test-module or validator inventory;
- Hydrology schemas, fixtures, expected-error sidecars, or deterministic identity rules;
- the USGS cutover or WBD HUC12 material-change workflows;
- `tools/ci/install_python_ci.py` or the `project-test` dependency profile;
- source descriptors, source-authority projections, activation decisions, or executable pipeline specs;
- Hydrology policy bundle/evaluator binding;
- EvidenceRef resolution or proof production;
- release candidate, dry-run, correction, withdrawal, or rollback implementation; or
- the no-life-safety and public-boundary doctrine.

### Open verification backlog

- Establish an accepted Hydrology source descriptor and source-activation path before any live fetch.
- Resolve the duplicate Hydrology source-registry topology without creating parallel writable authority.
- Replace selected source/pipeline placeholders only when implementation, rights, role, cadence, tests, review, correction, and rollback evidence close together.
- Decide whether an aggregate Hydrology command is useful; until then, preserve the workflow-owned explicit commands.
- Bind an accepted Hydrology policy bundle, evaluator, normalized finite result contract, obligation handlers, negative tests, and governed consumers.
- Implement real EvidenceRef-to-EvidenceBundle resolution separately from the current alias shape test.
- Establish a deterministic proof producer, accepted proof contract, access controls, and release linkage before removing the proof hold.
- Establish a candidate packet and fail-closed release dry-run command before removing the release hold.
- Define and verify host/runner-level egress containment before using `hermetic`, `air-gapped`, or infrastructure no-egress language.
- Assign accountable Hydrology, source, identity, scientific, rights, sensitivity, policy, QA, proof, release, correction, and rollback roles.
- Reconcile the one-byte [`docs/runbooks/hydrology/README.md`](./README.md) and stale adjacent Hydrology runbook summaries in separate, dependency-aware documentation work.

### Source posture

The Drive Hydrology reference report contributes planning lineage for HUC12, source-role anti-collapse, identity ambiguity, time, evidence, and fixture-first validation. Its no-repository assumptions and illustrative implementation paths are superseded for current behavior by repository evidence.

The Notion Atlas contributes coordination and maturity-separation context. It does not replace exact current GitHub files, workflow runs, tests, logs, or review records.

[Back to top](#top)

---

## Related repository surfaces

| Surface | Role |
|---|---|
| [Hydrology domain workflow](../../../.github/workflows/domain-hydrology.yml) | Exact broad fixture-only execution and explicit proof/release holds |
| [USGS Water API cutover workflow](../../../.github/workflows/hydrology-usgs-water-api-cutover.yml) | Dedicated cutover-assessment profile |
| [WBD HUC12 material-change workflow](../../../.github/workflows/hydrology-wbd-huc12-material-change.yml) | Dedicated material-change profile |
| [Hydrology tests index](../../../tests/domains/hydrology/README.md) | Test-lane inventory and enforceability boundary |
| [Hydrology validators index](../../../tools/validators/domains/hydrology/README.md) | Validator inventory and maturity boundary |
| [Hydrology policy boundary](../../../policy/domains/hydrology/README.md) | Mixed-maturity policy inventory and evaluator hold |
| [Hydrology source registry](../../../data/registry/sources/hydrology/README.md) | Source-admission orientation and topology warning |
| [Source authority register](../../../control_plane/source_authority_register.yaml) | Current empty, projection-only authority index |
| [Hydrology candidate lane](../../../release/candidates/hydrology/README.md) | Pre-publication candidate boundary; candidate is not release |
| [Hydrology Promotion Runbook](./PROMOTION_RUNBOOK.md) | Candidate preflight and release-review handoff |
| [Hydrology Source Refresh Runbook](./SOURCE_REFRESH_RUNBOOK.md) | Source-refresh procedure; verify current maturity before use |
| [Hydrology Rollback Runbook](./ROLLBACK_RUNBOOK.md) | Candidate/release correction and recovery boundary |
| [Hydrology Validation](./VALIDATION.md) | Adjacent validation guidance; current workflow and tests outrank stale prose |
| [Hydrology domain README](../../domains/hydrology/README.md) | Domain language, source-role, and public-use boundary |

[Back to top](#top)
