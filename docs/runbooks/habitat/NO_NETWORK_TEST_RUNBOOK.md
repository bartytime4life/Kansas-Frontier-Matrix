<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook/habitat/no-network-test
title: Habitat — No-Network Test Runbook
type: runbook; operational-procedure; domain-lane; sensitive-domain; non-authoritative
version: v0.2
prior_version: v1 planning-oriented draft
status: draft; repository-grounded; one-bounded-no-live-source-profile-executable; broader-habitat-source-evidence-policy-proof-release-and-publication-held; non-publisher
owners:
  - "@bartytime4life — verified GitHub review route"
owner_status: "Habitat, land-cover, source, rights, sensitivity/geoprivacy, evidence, policy, validation, proof, review, release, correction, rollback, security, CI, and operations assignments remain NEEDS VERIFICATION; CODEOWNERS routing does not create those authorities."
created: 2026-05-12
updated: 2026-08-25
policy_label: public-review; habitat; land-cover; no-network; synthetic-fixtures; sensitive-location; fail-closed; non-release
current_path: docs/runbooks/habitat/NO_NETWORK_TEST_RUNBOOK.md
owning_root: docs/
responsibility: "Document the exact bounded Habitat no-live-source procedure currently supported by the inactive land-cover materiality profile, deterministic synthetic fixtures, focused validator tests, and read-only workflows, while keeping live sources, Habitat truth, species occurrences, rights, geoprivacy, evidence closure, policy, proof, review, release, deployment, promotion, publication, and public authority outside the test boundary."
truth_posture: cite-or-abstain
prepared_under_prompt: KFM Repository Build-Out & Markdown Modernization Implementation Agent v6.0.0
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 434195e8727e6e8649fd6a9e7de06808c3e15261
  target_prior_blob: e7c9bba0025ea2c24db530dd0bf498e472af5727
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adoption_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  habitat_source_refresh_runbook_blob: 80a91eedd27b369963ebe7a12d9ef5a0e75aa769
  domain_habitat_workflow_blob: 59771c027f688d7028a46c4635c0ec710b34e3ab
  focused_materiality_workflow_blob: fd73a098c1dbf8fd07135ce3cdab04b280b30904
  materiality_contract_blob: c7ad48b435d8cc7fcdcf2910fb675e9c9778e7e7
  materiality_profile_schema_blob: 9857ead389deaf0a8306d143fe72900303d7e4cc
  materiality_profile_blob: 8553fc03da35e2d86d254d362392ca414bdf73af
  habitat_materiality_validator_blob: 931677daf9d4d54150cd10aadf8285c7ef8ae93e
  shared_material_change_validator_blob: 0e7810c9dacd55ae79e3d445fa023902f557020e
  habitat_materiality_test_blob: 4f322c8107d74447d64afea38f42a941a43eb8d5
  valid_fixture_manifest_blob: 68dc6948b8a1c3b12fd11ee7ac52602aeecf29a3
  invalid_fixture_manifest_blob: db47ee07c8e98661930be1bfd145b52a2ff34089
  habitat_fixture_index_blob: 674c5acf8c2f1739762625e392616ce1034de0e6
  habitat_tests_index_blob: 4503de9bcb1c92db45012d897d647fb39a9f7172
  habitat_proof_readme_blob: be4e0a82a86f12972de6f78e82fd3ca051618077
  habitat_release_candidate_readme_blob: e55b9344cda673e069bce5525937f5a50666bf63
drive_sources:
  - title: kfm_habitat_architecture_pdf_only_blueprint_2026-04-21.pdf
    file_id: 1Ys9Z_AYfEz6oStxY0YqZjih9DFHc5GA6
    role: planning lineage; fixture-first, source-role, evidence, sensitivity, and no-network principles; not current repository implementation proof
  - title: KFM_Habitat_Fauna_Thin_Slice_Extended_Pro_Blueprint.pdf
    file_id: 1KU3Z_KkqbKAkv3E7oyulTAQlN4f1Gz5w
    role: cross-domain thin-slice planning lineage; not proof of current executable closure or release state
inspection_boundary: "Current-session GitHub reads of the target, accepted Directory Rules decision, CODEOWNERS, Habitat source-refresh boundary, two Habitat workflows, materiality contract/profile/schema, domain and shared validators, focused tests, fixture manifests, parent fixture/test indexes, proof lane, and release-candidate lane; plus connected Google Drive planning sources. A mounted repository checkout and repository-native commands were not available during authoring. No live source, credential, real Habitat record, exact sensitive geometry, species occurrence, policy evaluator, evidence resolver, proof producer, release service, deployed consumer, or public carrier was exercised."
related:
  - docs/runbooks/README.md
  - docs/runbooks/habitat/README.md
  - docs/runbooks/habitat/SOURCE_REFRESH_RUNBOOK.md
  - docs/runbooks/habitat/PROMOTION_RUNBOOK.md
  - docs/runbooks/habitat/ROLLBACK_RUNBOOK.md
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/domains/habitat/README.md
  - contracts/domains/habitat/land_cover/materiality_profile.md
  - schemas/contracts/v1/domains/habitat/land_cover/materiality_profile.schema.json
  - schemas/contracts/v1/data/material_change_assessment.schema.json
  - pipeline_specs/habitat/land_cover/materiality_profile.v1.json
  - fixtures/domains/habitat/land_cover/materiality/
  - tools/validators/domains/habitat/validate_land_cover_materiality.py
  - tools/validators/validate_material_change_assessment.py
  - tests/validators/domains/habitat/test_land_cover_materiality.py
  - tests/domains/habitat/README.md
  - data/proofs/habitat/README.md
  - release/candidates/habitat/README.md
  - .github/workflows/domain-habitat.yml
  - .github/workflows/habitat-land-cover-materiality.yml
tags: [kfm, habitat, land-cover, runbook, no-network, no-live-source, synthetic-fixtures, validation, materiality, sensitive-location, fail-closed]
notes:
  - "v0.2 replaces the no-mounted-repository assumption, hypothetical full Habitat validator/policy/release chain, proposed fixture tree, invented receipt path, and unverified egress-lockdown claims with the exact current bounded executable profile and explicit holds."
  - "The retained operating principle is fixture-first, deterministic, synthetic, no-live-source, fail-closed, and reversible. Current implementation proves only the inactive Habitat land-cover materiality adapter against reviewed local fixtures and the shared MaterialChangeAssessment shape."
  - "The focused test does not install a socket, DNS, HTTP, or operating-system egress guard. The domain workflow sets KFM_NO_NETWORK=1 as a convention; checkout, Python setup, and dependency installation may still use network services. Strong no-egress proof therefore requires separately recorded environment enforcement."
  - "The inspected top-level tests/domains/habitat Python files are proposal placeholders except for one tautological smoke test; they are not the substantive no-network profile documented here."
  - "The domain workflow intentionally holds Habitat proof production and release dry-run execution. A green held job is readiness evidence, not proof, review, release, deployment, promotion, or publication."
  - "This document changes no source, contract, schema, profile, fixture, validator, test, workflow, evidence object, operational receipt, proof, candidate, lifecycle state, runtime, deployment, promotion, rollback execution, or publication state."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat — No-Network Test Runbook

> **Run and interpret the Habitat lane's current synthetic land-cover materiality profile without contacting a live Habitat source, exposing sensitive ecological locations, or confusing fixture conformance with Habitat truth, evidence closure, policy approval, proof, release, or publication.**

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#current-repository-posture)
[![Executable profile: one bounded](https://img.shields.io/badge/profile-one%20bounded-1a7f37?style=flat-square)](#current-executable-profile)
[![Input: synthetic local fixtures](https://img.shields.io/badge/input-synthetic%20local%20fixtures-0969da?style=flat-square)](#fixture-inventory-and-frozen-invariants)
[![Network: no live source](https://img.shields.io/badge/network-no%20live%20source-b42318?style=flat-square)](#no-network-contract)
[![Proof and release: held](https://img.shields.io/badge/proof%20and%20release-HOLD-d4a72c?style=flat-square)](#current-holds-and-graduation-gates)
[![Publisher: no](https://img.shields.io/badge/publisher-no-6e7781?style=flat-square)](#authority-and-placement)

> [!IMPORTANT]
> **A green local or hosted result proves only the inactive synthetic Habitat land-cover materiality profile at the tested revision.** It does not establish land-cover truth, habitat condition, species presence, critical-habitat status, source admission, rights clearance, geoprivacy, an `EvidenceBundle`, a `PolicyDecision`, proof, review, release, deployment, promotion, publication, or public use.

> [!WARNING]
> **Never place real, exact, or reverse-engineerable sensitive ecological locations in this procedure.** Rare-species, rare-plant, nest, den, roost, hibernaculum, breeding, spawning, stewardship, cultural, archaeological, private-land, infrastructure-adjacent, transform-secret, restricted-source, or credential detail does not belong in fixtures, logs, workflow summaries, issues, pull requests, screenshots, or review packets.

> [!CAUTION]
> **“No network” is bounded, not magical.** The current adapter reads local files and performs no intentional source request. Its focused tests do not patch socket, DNS, HTTP, or `urllib`, and the workflows do not establish an operating-system egress sandbox. Checkout, Python setup, and dependency installation can use network services before the focused commands run. Use the finite evidence grades in this runbook; do not report stronger no-egress proof than the environment actually supplies.

**Quick navigation:** [Purpose](#purpose-and-terminal-boundary) · [Authority](#authority-and-placement) · [Posture](#current-repository-posture) · [Profile](#current-executable-profile) · [Network](#no-network-contract) · [Fixtures](#fixture-inventory-and-frozen-invariants) · [Preflight](#preconditions-and-stop-conditions) · [Local run](#local-procedure) · [CI](#hosted-ci-procedure) · [Results](#finite-outcomes-and-result-interpretation) · [Failures](#failure-diagnosis) · [Sensitivity](#sensitivity-rights-and-security) · [Receipts](#evidence-receipts-and-proof-boundary) · [Handoff](#review-handoff) · [Holds](#current-holds-and-graduation-gates) · [Rollback](#correction-and-document-rollback) · [References](#related-current-surfaces) · [Checklist](#operator-checklist) · [Lineage](#v1-lineage-and-superseded-assumptions) · [Non-effects](#non-effects)

---

<a id="purpose-and-terminal-boundary"></a>

## Purpose and terminal boundary

Use this runbook to execute and review the exact Habitat fixture profile currently wired by the repository:

```text
inactive county land-cover materiality profile
  + seven valid synthetic comparison fixtures
  + six invalid synthetic comparison fixtures
  + deterministic domain adapter
  + shared MaterialChangeAssessment validation
  + nine focused unittest methods
  + read-only hosted orchestration
  -> bounded fixture conformance or stable fail-closed findings
  -> exact-revision review handoff
  -/> live source access or source admission
  -/> Habitat, land-cover, species, or regulatory truth
  -/> rights, sensitivity, geoprivacy, evidence, policy, proof, or review authority
  -/> lifecycle mutation, release, deployment, promotion, or publication
```

The KFM lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLETS -> PUBLISHED
```

This procedure does not enter, advance, or mutate that lifecycle. It reads repository-owned synthetic files and emits console test or validator output only.

### In scope

- `contracts/domains/habitat/land_cover/materiality_profile.md`;
- `schemas/contracts/v1/domains/habitat/land_cover/materiality_profile.schema.json`;
- `schemas/contracts/v1/data/material_change_assessment.schema.json`;
- `pipeline_specs/habitat/land_cover/materiality_profile.v1.json`;
- `fixtures/domains/habitat/land_cover/materiality/valid/` and `invalid/`;
- `tools/validators/domains/habitat/validate_land_cover_materiality.py`;
- `tools/validators/validate_material_change_assessment.py`;
- `tests/validators/domains/habitat/test_land_cover_materiality.py`;
- `.github/workflows/domain-habitat.yml` and `.github/workflows/habitat-land-cover-materiality.yml`;
- profile schema/hash checks, inactive-governance checks, bounded input validation, deterministic outcome mapping, expected fixture polarity, shared assessment validation, CLI behavior, and exact-revision handoff.

### Out of scope

- live NLCD, NWI, GAP, LANDFIRE, PAD-US, USFWS ECOS, KDWP, NatureServe, GBIF, iNaturalist, iDigBio, field-survey, remote-sensing, or other source requests;
- source admission, activation, endpoint verification, authentication, retrieval, cadence, rights review, or source health;
- real habitat polygons, land-cover exports, occurrence records, stewardship records, source-native restricted payloads, or protected joins;
- general Habitat schema coverage beyond the named profile;
- the proposal-placeholder modules under `tests/domains/habitat/`;
- active Habitat policy evaluation or sensitivity/geoprivacy adjudication;
- `EvidenceRef` resolution to a real `EvidenceBundle`;
- proof construction, release-candidate assembly, release dry run, deployment, publication, correction execution, withdrawal execution, cache invalidation, or operational rollback;
- public API, map, tile, export, search, graph, Evidence Drawer, Focus Mode, or AI-answer behavior;
- scientific adoption of the materiality thresholds.

**Maximum result:** a bounded validation handoff for the exact inactive synthetic profile at an exact repository revision.

[Back to top](#top)

---

<a id="authority-and-placement"></a>

## Authority and placement

### Directory Rules result

**`PLACE` — confirmed for this same-path update.**

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts [Directory Rules v2](../../doctrine/directory-rules.md). A human operational procedure belongs under `docs/runbooks/`, with `habitat/` as the domain segment. The tracked target therefore remains:

```text
docs/runbooks/habitat/NO_NETWORK_TEST_RUNBOOK.md
```

This update creates no new root, parallel runbook authority, contract home, schema home, policy home, source registry, fixture lane, proof lane, release lane, or public path.

| Responsibility | Owning surface | This runbook's role |
|---|---|---|
| Human procedure | `docs/runbooks/habitat/` | Explain exact execution, interpretation, stops, and handoff |
| Habitat meaning | `docs/domains/habitat/`, `contracts/domains/habitat/` | Cite; do not redefine ecological or regulatory truth |
| Machine shape | `schemas/contracts/v1/domains/habitat/`, shared data schemas | Document only the schemas invoked by the bounded profile |
| Declarative profile | `pipeline_specs/habitat/land_cover/` | Require exact inactive profile bytes and hash |
| Synthetic inputs | `fixtures/domains/habitat/land_cover/materiality/` | Consume only the reviewed valid and invalid profiles named here |
| Validator implementation | `tools/validators/domains/habitat/`, shared validator home | Document exact entry points and bounded finding contracts |
| Executable tests | `tests/validators/domains/habitat/` | Document assertions without expanding their proof |
| Workflow orchestration | `.github/workflows/` | Bind results to a revision; do not infer release authority |
| Source admission | source registry and source-authority controls | Require separately accepted records; this procedure activates none |
| Policy and sensitivity | `policy/domains/habitat/` and accepted geoprivacy controls | Record the hold; this procedure does not evaluate them |
| Evidence and proof | evidence contracts and `data/proofs/habitat/` | Keep fixture references distinct from evidence closure |
| Candidate and release | `release/candidates/habitat/`, shared release roots | Preserve holds; do not assemble or approve |
| Public clients | governed APIs and released public-safe artifacts | Outside this procedure |

`CODEOWNERS` routes repository review to `@bartytime4life`. It does not establish Habitat stewardship, policy authority, sensitivity review, independent approval, release authority, or publication authority.

[Back to top](#top)

---

<a id="current-repository-posture"></a>

## Current repository posture

The observations below are pinned to `main@434195e8727e6e8649fd6a9e7de06808c3e15261`.

| Surface | Confirmed repository evidence | Bounded conclusion |
|---|---|---|
| Requested target | This tracked runbook exists at prior blob `e7c9bba0025ea2c24db530dd0bf498e472af5727` | Same-path reconciliation is appropriate |
| Materiality contract | Declares one county land-cover adapter for the shared `MaterialChangeAssessment` object | Scope is one domain adapter, not the whole Habitat lane |
| Profile | `status: PROPOSED_INACTIVE`; all governance flags are false and `release_ref` is null | The profile is fixture-first and non-authorizing |
| Domain adapter | Reads local JSON/profile/schema files, validates exact fields, limits file size to 1 MiB, verifies hashes, emits finite classifications, and performs no intentional source request | Local deterministic comparison is implemented; source access is not |
| Focused executable tests | `tests/validators/domains/habitat/test_land_cover_materiality.py` contains nine substantive `unittest` methods | This is the current executable no-live-source test surface |
| Valid fixture manifest | Seven expected fixtures: unchanged, byte-only, semantic non-material, two material triggers, and two holds | Expected positive and hold polarity is explicit |
| Invalid fixture manifest | Six expected finding profiles: missing metric, negative area, noncanonical refs, invalid time order, unknown field, and zero digest | Fail-closed negative polarity is explicit |
| Shared validation | Every emitted assessment is passed to the shared `MaterialChangeAssessment` validator in focused tests | Shape and local consistency are checked; evidence and policy are not |
| Domain workflow | `validate-habitat` runs the profile; `build-proof-habitat` and `publish-dry-run-habitat` are explicit readiness holds | Green workflow status includes held non-execution for proof and release |
| Focused workflow | Runs only when materiality profile files change or by manual dispatch | A docs-only runbook PR normally does not trigger this path-filtered workflow |
| Top-level Habitat tests | Seven inspected files are proposal docstring placeholders; `test_habitat_smoke.py` only asserts `True` | `pytest tests/domains/habitat` is not current substantive Habitat conformance proof |
| Habitat fixtures parent | Documents many synthetic child lanes but says payload inventory and consumers remain only partly verified | Do not generalize the one materiality profile to every documented fixture lane |
| Habitat proof lane | Retains “Implementation depth remains UNKNOWN” and no accepted proof producer | Proof production remains held |
| Habitat candidate lane | No non-README candidate record or active Habitat candidate is established | Release readiness is not established |
| Source refresh boundary | Current repository-grounded runbook reports no active Habitat source-refresh path and only this inactive synthetic comparison profile | This runbook must not fetch or imply source activation |
| Accountable stewardship | Only the GitHub review route is verified | Domain, policy, sensitivity, proof, release, and independent-review roles remain `NEEDS VERIFICATION` |

### Safe current determination

```text
Executable Habitat no-live-source profile: one
Profile state: PROPOSED_INACTIVE
Valid fixture cases: seven
Invalid fixture cases: six
Focused substantive unittest methods: nine
Live source access: none in the profile
Habitat-wide policy/evidence/proof/release closure: not established
Public release or publication: not established
```

[Back to top](#top)

---

<a id="current-executable-profile"></a>

## Current executable profile

### Profile identity

| Field | Current value |
|---|---|
| Profile ID | `kfm://materiality-profile/habitat/land-cover/county-change-v1` |
| Profile version | `1.0.0` |
| Profile status | `PROPOSED_INACTIVE` |
| Domain / sublane | `habitat` / `land_cover` |
| Analysis unit | `county` |
| Canonicalization | `kfm-canonical-json-v1` |
| Digest | SHA-256 |
| Combination | `ANY` trigger may classify a semantic change as material |
| Source activated | `false` |
| Policy evaluated | `false` |
| Promotion authorized | `false` |
| Public use allowed | `false` |
| Release reference | `null` |

### Declared synthetic triggers

The profile carries two strict-greater-than triggers:

1. `reclassification_fraction > 0.02`; or
2. `max_net_class_delta_ha > max(250 ha, analysis_unit_area_ha * 0.0015)`.

These thresholds are executable fixture parameters. They are not established here as scientifically, legally, operationally, or steward-approved thresholds for live Habitat data.

### Outcome mapping

| Input state | Change class | Adapter outcome | Interpretation |
|---|---|---|---|
| Identical baseline and candidate digests | `UNCHANGED` | `NON_EVENT` | No material-change candidate |
| Byte change with declared no semantic change | `BYTE_ONLY` | `NON_EVENT` | Byte drift only |
| Semantic change below both thresholds | `SEMANTIC_NON_MATERIAL` | `NON_EVENT` | Bounded profile says no material candidate |
| Semantic change above either threshold | `MATERIAL` | `PROMOTION_CANDIDATE` | Candidate for later governed inspection only |
| Semantic state unavailable or analysis unit unsupported | `UNDETERMINED` | `HOLD` | Do not infer a result |
| Invalid profile or candidate | No assessment | Findings and nonzero file result | Fail closed |

`PROMOTION_CANDIDATE` is a materiality classification. It is not source admission, policy approval, a promotion decision, release approval, or publication authority.

### Focused assertions

The nine substantive tests currently verify:

1. profile JSON Schema validity and canonical `spec_hash`;
2. all seven valid fixtures match their reviewed change classes and outcomes;
3. all six invalid fixtures match their reviewed finding-code sets;
4. repeated evaluation is deterministic;
5. thresholds are strictly greater than, not greater-than-or-equal;
6. profile tampering fails with `PROFILE_HASH_MISMATCH`;
7. the fixture CLI exits successfully, emits a material-candidate outcome, and omits one specific example-county identifier from stdout;
8. duplicate JSON object keys fail with `JSON_DUPLICATE_KEY`; and
9. non-finite JSON numbers fail with `JSON_NONFINITE_NUMBER`.

The example-identifier assertion is narrow. It does not prove universal log redaction or geoprivacy enforcement.

[Back to top](#top)

---

<a id="no-network-contract"></a>

## No-network contract

Use one of the following evidence grades. Record the grade explicitly in every handoff.

| Grade | Requirements | What may be claimed |
|---|---|---|
| `NO_LIVE_SOURCE_PASS` | Exact local profile/fixtures; focused commands exit as expected; no connector, endpoint, credential, or live payload is invoked | The bounded repository profile passed without intentional live-source access |
| `NO_EGRESS_ENVIRONMENT_PASS` | All `NO_LIVE_SOURCE_PASS` requirements plus separately verified operating-system, container, runner, proxy, or network-policy egress denial during the focused commands | The bounded profile passed while the execution environment denied outbound egress |
| `HOSTED_ORCHESTRATION_PASS` | Exact workflow revision is green and logs show the intended job/commands | Hosted orchestration passed at that revision; network isolation remains limited to what the workflow proves |
| `NOT_PROVEN` | Revision, fixture set, commands, environment, or logs cannot be verified | Do not claim no-network success |

### What current repository code proves

- The adapter uses local filesystem, JSON, hashing, time parsing, and JSON Schema validation.
- The profile and fixture paths are repository-local.
- The adapter does not call a Habitat connector or live source.
- The focused test imports the adapter and shared local validator, creates temporary local files, and runs the local CLI.

### What current repository code does not prove

- The focused test does not monkeypatch socket, DNS, HTTP clients, or `urllib`.
- `KFM_NO_NETWORK=1` in `domain-habitat.yml` is a convention; the adapter does not use it as an active firewall.
- `habitat-land-cover-materiality.yml` does not set `KFM_NO_NETWORK`.
- Both workflows use checkout and Python setup actions; dependency installation may contact approved package infrastructure.
- Neither workflow defines an operating-system firewall, network namespace, deny proxy, or runner-level egress policy.

### Dependency preparation is outside the focused no-egress claim

The hosted workflows install declared project runtime dependencies with:

```bash
python tools/ci/install_python_ci.py project-runtime
```

That step may require network access. For a strong no-egress rehearsal, prepare the environment first, record the dependency source and lock/revision evidence, then enforce egress denial before running the focused commands. Do not include package installation in a claim that the entire job had no network access unless the environment proves it.

[Back to top](#top)

---

<a id="fixture-inventory-and-frozen-invariants"></a>

## Fixture inventory and frozen invariants

### Valid fixture manifest

| Fixture | Expected change class | Expected adapter outcome |
|---|---|---|
| `valid_unchanged.json` | `UNCHANGED` | `NON_EVENT` |
| `valid_byte_only.json` | `BYTE_ONLY` | `NON_EVENT` |
| `valid_semantic_non_material.json` | `SEMANTIC_NON_MATERIAL` | `NON_EVENT` |
| `valid_material_net_area.json` | `MATERIAL` | `PROMOTION_CANDIDATE` |
| `valid_material_reclassification.json` | `MATERIAL` | `PROMOTION_CANDIDATE` |
| `valid_hold_metric_unavailable.json` | `UNDETERMINED` | `HOLD` |
| `valid_hold_wrong_analysis_unit.json` | `UNDETERMINED` | `HOLD` |

### Invalid fixture manifest

| Fixture | Expected finding code |
|---|---|
| `invalid_missing_metric.json` | `METRIC_MISSING` |
| `invalid_negative_area.json` | `ANALYSIS_UNIT_AREA_INVALID` |
| `invalid_noncanonical_refs.json` | `REFS_NOT_CANONICAL` |
| `invalid_time_order.json` | `BASELINE_AFTER_CANDIDATE` |
| `invalid_unknown_field.json` | `INPUT_FIELD_UNKNOWN` |
| `invalid_zero_digest.json` | `DIGEST_PLACEHOLDER` |

### Frozen invariants

Stop and re-review this runbook if any of these change:

- profile ID, version, `spec_hash`, canonicalization profile, digest algorithm, or trigger semantics;
- `PROPOSED_INACTIVE` status or any false/null governance field;
- valid or invalid fixture manifest membership or expected polarity;
- shared `MaterialChangeAssessment` schema version or outcome vocabulary;
- file-size limit, duplicate-key behavior, non-finite-number behavior, canonical-ref rules, or timing rules;
- validator CLI contract or path;
- focused test count or assertions;
- workflow paths, job names, required-path checks, dependency installer, or hold conditions;
- proof, candidate, policy, source, or public-carrier state.

A fixture name or test pass is not scientific evidence. Fixtures are synthetic test inputs and expected outputs only.

[Back to top](#top)

---

<a id="preconditions-and-stop-conditions"></a>

## Preconditions and stop conditions

### Required preconditions

- [ ] The repository is `bartytime4life/Kansas-Frontier-Matrix`.
- [ ] The exact revision under test is recorded.
- [ ] The working tree is clean or every unrelated change is excluded from the result.
- [ ] Python 3.11 or a repository-approved compatible interpreter is active.
- [ ] Declared runtime dependencies are installed from the reviewed project configuration.
- [ ] Every required profile, schema, fixture manifest, validator, and test path exists.
- [ ] The profile remains `PROPOSED_INACTIVE` with all governance flags false and `release_ref: null`.
- [ ] Fixtures are synthetic, compact, public-safe, and contain no real restricted source material.
- [ ] The intended no-network evidence grade and environmental enforcement are recorded before execution.
- [ ] Output will be stored outside canonical lifecycle, proof, receipt, candidate, release, or published roots.

### Required paths

The domain workflow currently requires:

```text
contracts/domains/habitat/land_cover/materiality_profile.md
schemas/contracts/v1/domains/habitat/land_cover/materiality_profile.schema.json
pipeline_specs/habitat/land_cover/materiality_profile.v1.json
fixtures/domains/habitat/land_cover/materiality/valid/expected_outputs_manifest.json
fixtures/domains/habitat/land_cover/materiality/invalid/expected_findings_manifest.json
tools/validators/domains/habitat/validate_land_cover_materiality.py
tests/validators/domains/habitat/test_land_cover_materiality.py
schemas/contracts/v1/data/material_change_assessment.schema.json
tools/validators/validate_material_change_assessment.py
```

### Stop immediately when

- repository identity, revision, or profile identity is ambiguous;
- profile hash, version, status, or governance posture does not match the reviewed contract;
- a required path is missing, duplicated into a parallel authority, or unexpectedly generated;
- a fixture contains real source bytes, real occurrence coordinates, restricted joins, credentials, or transform secrets;
- the adapter or test introduces source, socket, DNS, HTTP, browser, cloud, database, or external-service access;
- expected fixture polarity changes without contract, fixture, test, and documentation review;
- a proof producer, release target, active candidate, live source, or public carrier appears where the workflows currently expect a hold;
- a command would write lifecycle, evidence, proof, receipt, release, or published state;
- the execution environment cannot support the evidence grade being claimed;
- output may expose sensitive or identifying detail.

A stop is `HOLD` or `DENY`, not permission to weaken the guardrail.

[Back to top](#top)

---

<a id="local-procedure"></a>

## Local procedure

### 1. Freeze repository state

From the repository root:

```bash
set -euo pipefail

git rev-parse --show-toplevel
git remote -v
git rev-parse HEAD
git status --short
```

Record the exact commit. Do not combine this result with an unreviewed dirty tree.

### 2. Verify required paths

```bash
set -euo pipefail

required_paths=(
  "contracts/domains/habitat/land_cover/materiality_profile.md"
  "schemas/contracts/v1/domains/habitat/land_cover/materiality_profile.schema.json"
  "pipeline_specs/habitat/land_cover/materiality_profile.v1.json"
  "fixtures/domains/habitat/land_cover/materiality/valid/expected_outputs_manifest.json"
  "fixtures/domains/habitat/land_cover/materiality/invalid/expected_findings_manifest.json"
  "tools/validators/domains/habitat/validate_land_cover_materiality.py"
  "tests/validators/domains/habitat/test_land_cover_materiality.py"
  "schemas/contracts/v1/data/material_change_assessment.schema.json"
  "tools/validators/validate_material_change_assessment.py"
)

for required_path in "${required_paths[@]}"; do
  test -f "$required_path" || {
    printf 'missing required path: %s\n' "$required_path" >&2
    exit 1
  }
done
```

### 3. Verify inactive governance before execution

```bash
python - <<'PY'
import json
from pathlib import Path

path = Path("pipeline_specs/habitat/land_cover/materiality_profile.v1.json")
profile = json.loads(path.read_text(encoding="utf-8"))
assert profile["status"] == "PROPOSED_INACTIVE"
assert profile["governance"] == {
    "source_activated": False,
    "policy_evaluated": False,
    "promotion_authorized": False,
    "public_use_allowed": False,
    "release_ref": None,
}
print(profile["profile_id"])
print(profile["profile_version"])
print(profile["spec_hash"])
PY
```

Any assertion failure is a `HOLD`. Do not edit the profile merely to make the runbook pass.

### 4. Prepare dependencies separately

Use an already provisioned environment, or run the repository's reviewed installer before claiming no-egress execution:

```bash
python tools/ci/install_python_ci.py project-runtime
```

Record whether this step used network access. It is not part of the focused profile's no-live-source assertion.

### 5. Establish deterministic execution settings

```bash
export KFM_NO_NETWORK=1
export PYTHONDONTWRITEBYTECODE=1
export PYTHONHASHSEED=0
export PYTHONUNBUFFERED=1
export TZ=UTC
```

These variables improve reproducibility and communicate intent. They do not enforce egress denial. Apply the approved operating-system, container, runner, proxy, or network-policy control separately when claiming `NO_EGRESS_ENVIRONMENT_PASS`.

### 6. Run focused tests

```bash
python -m unittest discover \
  --start-directory tests/validators/domains/habitat \
  --pattern 'test_land_cover_materiality.py' \
  --verbose
```

Expected current result when the reviewed bytes and dependencies are intact:

```text
Ran 9 tests
OK
```

The count is tied to the current test file. A different count requires review; it is not automatically a failure or success.

### 7. Run the fixture CLI

```bash
python tools/validators/domains/habitat/validate_land_cover_materiality.py --fixtures
```

Expected current result:

- process exit code `0`;
- thirteen compact JSON lines, one for each reviewed valid or invalid fixture;
- valid fixtures report adapter `outcome: PASS` and their expected `change_class` / `assessment_outcome`;
- invalid fixtures report per-file `outcome: FAIL` with the expected finding codes;
- no `FIXTURE_POLARITY_ERROR` line.

The per-file `FAIL` on an invalid fixture is expected negative-path behavior. The overall command passes only when the invalid result matches the reviewed finding manifest.

### 8. Capture a non-authoritative result packet

Store temporary output outside governed object-family roots:

```bash
result_dir="$(mktemp -d)"
revision="$(git rev-parse HEAD)"

python -m unittest discover \
  --start-directory tests/validators/domains/habitat \
  --pattern 'test_land_cover_materiality.py' \
  --verbose \
  >"$result_dir/unittest.stdout" \
  2>"$result_dir/unittest.stderr"

python tools/validators/domains/habitat/validate_land_cover_materiality.py --fixtures \
  >"$result_dir/fixtures.jsonl" \
  2>"$result_dir/fixtures.stderr"

printf '%s\n' "$revision" >"$result_dir/revision.txt"
sha256sum \
  "$result_dir/unittest.stdout" \
  "$result_dir/unittest.stderr" \
  "$result_dir/fixtures.jsonl" \
  "$result_dir/fixtures.stderr" \
  >"$result_dir/output.sha256"

printf 'temporary result packet: %s\n' "$result_dir"
```

This directory is operator evidence only. It is not automatically a canonical `RunReceipt`, `ValidationReport`, proof, review record, release record, or published artifact. Do not commit it without an accepted object contract and owning-path decision.

### 9. Confirm the test made no repository write

```bash
git status --short
```

Any unexpected tracked or untracked output requires investigation. Do not move test output into lifecycle or release roots by convenience.

[Back to top](#top)

---

<a id="hosted-ci-procedure"></a>

## Hosted CI procedure

### `domain-habitat`

`.github/workflows/domain-habitat.yml` runs on pull requests, pushes to `main`, and manual dispatch. It has three jobs:

| Job | Current role | Correct green interpretation |
|---|---|---|
| `validate-habitat` | Executes the bounded synthetic land-cover materiality tests and CLI | Profile conformance at the tested revision |
| `build-proof-habitat` | Verifies required proof-boundary docs and confirms no accepted proof producer or payload has appeared | Explicit proof `HOLD` remains intact |
| `publish-dry-run-habitat` | Verifies release-boundary docs and confirms no active candidate or accepted release dry-run target has appeared | Explicit release `HOLD` remains intact |

A successful held job does not mean proof or release occurred. If the hold job fails because new proof/candidate/target material surfaced, stop and reconcile the owning contracts, schemas, policy, validators, access controls, review state, correction path, and rollback before changing the workflow or this runbook.

### `habitat-land-cover-materiality`

`.github/workflows/habitat-land-cover-materiality.yml` is path-filtered to the materiality contract, schema, profile, fixtures, validator, test, and workflow itself. It runs the same focused test and CLI commands.

A change only to this runbook is outside that workflow's current path filter. Report the focused workflow as `NOT_APPLICABLE` unless manually dispatched or triggered by an in-scope file change. Do not claim it passed merely because another workflow passed.

### Hosted network boundary

Both workflows check out repository bytes and set up Python. Dependency installation can use package infrastructure. The domain workflow sets `KFM_NO_NETWORK=1`; the focused workflow does not. Neither workflow establishes an operating-system egress block. Hosted results therefore support `HOSTED_ORCHESTRATION_PASS` and bounded no-live-source behavior, not an unqualified whole-job no-egress claim.

### Review exact-head status

For the pull-request head under review, record:

- workflow name and run URL;
- exact head SHA;
- job conclusion;
- whether the job was triggered, skipped, pending, cancelled, or not applicable;
- the tested command and fixture/profile scope;
- any inherited or unrelated failure separately from changed-path failure;
- proof and release holds as holds, not successful publication states.

[Back to top](#top)

---

<a id="finite-outcomes-and-result-interpretation"></a>

## Finite outcomes and result interpretation

| Procedure outcome | Conditions | Required action |
|---|---|---|
| `PASS_BOUNDED` | Exact focused tests and CLI pass; profile/fixtures match; no unexpected repository write | Record exact revision, commands, evidence grade, and bounded conclusion |
| `PASS_NO_EGRESS` | `PASS_BOUNDED` plus independently verified egress denial during focused execution | Record the environmental enforcement and supporting evidence |
| `HOLD` | Unsupported analysis unit, unavailable semantic state, changed profile posture, unresolved revision, surfaced proof/release work, or incomplete environment evidence | Preserve state; route to accountable review |
| `ABSTAIN` | Asked to infer Habitat truth, species presence, regulatory status, rights, public safety, or evidence closure from this profile | State that the profile cannot support the claim |
| `DENY` | Real sensitive data, credentials, live source access, unsafe logging, lifecycle write, proof/release shortcut, or publication attempt enters the procedure | Stop, contain, remove unsafe material through governed correction, and escalate |
| `FAIL` | Unit test or fixture CLI exits nonzero, expected polarity differs, or required path is missing | Diagnose; do not promote or weaken assertions |
| `ERROR` | Interpreter, dependency, filesystem, checkout, or orchestration failure prevents a reliable result | Fix environment or rerun at a clean exact revision; do not treat as content failure without evidence |

### What `PASS_BOUNDED` means

It means the reviewed inactive profile, fixtures, adapter, shared assessment validator, and focused tests agree at one revision.

### What `PASS_BOUNDED` does not mean

It does not mean:

- the profile thresholds are approved for live use;
- any source is admitted, current, accurate, complete, or rights-cleared;
- any habitat, land-cover, species, wetland, or critical-habitat claim is true;
- exact geometry is safe;
- geoprivacy or sensitivity policy ran;
- `EvidenceRef` resolved to `EvidenceBundle`;
- policy, stewardship, independent review, proof, candidate, release, deployment, promotion, publication, correction, withdrawal, or rollback completed.

[Back to top](#top)

---

<a id="failure-diagnosis"></a>

## Failure diagnosis

| Symptom | Likely boundary | Safe response |
|---|---|---|
| `ModuleNotFoundError: jsonschema` | Declared runtime dependency is not installed | Prepare the reviewed environment; do not add an ad hoc dependency in this docs task |
| Required-path error | Wrong revision, partial checkout, rename, or incomplete dependency set | Freeze exact head and inspect the owning change; do not invent a replacement path |
| `PROFILE_HASH_MISMATCH` | Profile changed without matching canonical hash | Review version/hash change; do not recompute silently |
| `PROFILE_NOT_INACTIVE` | Profile status changed | `HOLD`; source, policy, promotion, public-use, and release implications need separate review |
| `PROFILE_GOVERNANCE_VIOLATION` | One or more non-authorizing governance fields changed | `DENY` this runbook as authority; route to governing source/policy/release review |
| `SCHEMA_UNAVAILABLE` or emitted-assessment schema failure | Profile/shared schema is missing, invalid, or incompatible | Repair the contract/schema/adapter slice together and rerun |
| `FIXTURE_POLARITY_ERROR` | Actual result differs from reviewed manifest | Inspect fixture, manifest, profile, and adapter; do not update expected output merely to green CI |
| Unexpected `MATERIAL` / `PROMOTION_CANDIDATE` | Threshold or fixture semantics changed | Treat only as a candidate classification; review change and preserve non-authorizing posture |
| Invalid fixture prints `outcome: FAIL` but command exits `0` | Expected negative fixture matched its reviewed finding set | Correct behavior; distinguish per-file polarity from run status |
| Network attempt or external request observed | No-live-source boundary was violated | Stop, record `DENY`, remove or quarantine unsafe behavior, and require a separately governed integration tier |
| Sensitive identifier or location appears in logs | Logging/geoprivacy boundary failed | Stop distribution, contain the output, follow correction and sensitivity escalation, and add a negative test |
| `build-proof-habitat` fails because implementation surfaced | Readiness hold is stale | Do not remove the hold mechanically; establish proof contract, fixtures, validator, policy/access controls, review, and rollback |
| `publish-dry-run-habitat` fails because candidate/target surfaced | Release boundary changed | Do not treat new files as release; reconcile candidate identity, evidence, policy, review, correction, and rollback |
| `pytest tests/domains/habitat` is green | Placeholder smoke/docs may have passed | Do not report Habitat conformance; use the focused validator suite in this runbook |
| Hosted job cancelled or pending | No settled conclusion | Report `PENDING` or `CANCELLED`; do not infer pass/fail |

A repair should be the smallest dependency-closed change that preserves the fixture's intended polarity and the trust boundary.

[Back to top](#top)

---

<a id="sensitivity-rights-and-security"></a>

## Sensitivity, rights, and security

### Data allowed in this profile

- compact synthetic county-comparison records;
- toy identifiers, timestamps, hashes, refs, metrics, and evidence pointers;
- reviewed expected-output and expected-finding manifests;
- public repository paths and non-sensitive validation output.

### Data forbidden in this profile or ordinary handoff

- real occurrence coordinates or source-native restricted geometry;
- exact rare-species, rare-plant, nest, den, roost, breeding, spawning, hibernaculum, stewardship, cultural, archaeological, private-land, or infrastructure-adjacent locations;
- reversible redaction offsets, generalization secrets, transform parameters, hidden joins, or decryption material;
- credentials, tokens, signed URLs, private endpoints, cookies, API keys, or account identifiers;
- unreviewed source exports or copyrighted/restricted payloads;
- claims that a model, classification, or materiality result is regulatory or observational truth.

### Source-role anti-collapse

This profile evaluates declared change metrics. It does not assign or upgrade source roles. In particular:

- modeled habitat is not regulatory critical habitat;
- land-cover classification is not species occurrence;
- a material change is not ecological significance;
- a public map carrier is not evidence authority;
- a fixture evidence reference is not an `EvidenceBundle`;
- `PROMOTION_CANDIDATE` is not a promotion decision.

### Rights and terms

Synthetic fixtures avoid live source terms, but that does not clear any future source. Live-source use requires a separately admitted `SourceDescriptor`, current rights/terms review, citation obligations, sensitivity classification, access control, and review state.

[Back to top](#top)

---

<a id="evidence-receipts-and-proof-boundary"></a>

## Evidence, receipts, and proof boundary

The current commands emit console evidence. They do not create canonical accountability objects.

| Artifact | Current status in this procedure | What it proves |
|---|---|---|
| `unittest` output | Operator/CI execution evidence | Named test methods ran at a revision |
| Fixture CLI JSONL | Operator/CI execution evidence | Each fixture matched or failed its local validator contract |
| Git commit SHA | Byte identity anchor | Which repository revision was tested |
| Output SHA-256 | Integrity aid for the captured packet | Captured bytes did not change after hashing |
| GitHub workflow log | Hosted orchestration evidence | Hosted steps and conclusions at an exact head |
| `RunReceipt` | Not produced by the current adapter | Nothing unless a separately accepted producer emits one |
| `ValidationReport` | Not produced as a governed object by this procedure | Console success is not automatically a canonical report |
| `EvidenceBundle` | Not resolved or produced | Fixture refs are not evidence closure |
| `ProofPack` / Habitat proof object | Explicitly held | No accepted proof producer is established |
| `PromotionDecision` / `ReleaseManifest` | Not produced | No release state is created |

Do not rename a temporary result packet to make it look like a governed receipt or proof. Establish the object contract, deterministic identity, owning path, producer, validator, review state, correction path, and rollback before admitting a new accountability object.

[Back to top](#top)

---

<a id="review-handoff"></a>

## Review handoff

A review packet should contain only non-sensitive, exact-revision evidence.

### Required fields

```yaml
repository: bartytime4life/Kansas-Frontier-Matrix
revision: <exact commit SHA>
profile_id: kfm://materiality-profile/habitat/land-cover/county-change-v1
profile_version: 1.0.0
profile_spec_hash: <exact spec_hash>
evidence_grade: NO_LIVE_SOURCE_PASS | NO_EGRESS_ENVIRONMENT_PASS | HOSTED_ORCHESTRATION_PASS | NOT_PROVEN
commands:
  - python -m unittest discover --start-directory tests/validators/domains/habitat --pattern test_land_cover_materiality.py --verbose
  - python tools/validators/domains/habitat/validate_land_cover_materiality.py --fixtures
unit_test_result: PASS | FAIL | ERROR | NOT_RUN
unit_test_count: 9 | <actual reviewed count>
fixture_cli_result: PASS | FAIL | ERROR | NOT_RUN
valid_fixture_count: 7 | <actual reviewed count>
invalid_fixture_count: 6 | <actual reviewed count>
output_digests: [<sha256 values or empty>]
hosted_checks:
  domain_habitat: PASS | FAIL | PENDING | CANCELLED | NOT_RUN | UNKNOWN
  focused_materiality: PASS | FAIL | PENDING | CANCELLED | NOT_APPLICABLE | NOT_RUN | UNKNOWN
network_enforcement: <exact bounded description>
repository_writes: none | <exact unexpected paths>
sensitive_data_observed: false | true-and-contained
proof_state: HOLD
release_state: HOLD
publication_effect: none
limitations: [<explicit bounded limitations>]
review_route: "@bartytime4life — GitHub routing only"
accountable_stewardship: NEEDS_VERIFICATION
```

### Reviewer decisions

The reviewer should decide only whether:

1. the documented command/path/profile inventory matches the branch;
2. the fixture manifests and focused tests support the claimed bounded result;
3. the network evidence grade is truthful;
4. no sensitive or real source material entered the path;
5. the inactive governance and no-publication boundaries remain intact;
6. failures are introduced, inherited, environmental, expected negative polarity, or unrelated;
7. documentation remains synchronized with workflows and executable code.

This review does not approve live source use, scientific thresholds, geoprivacy, policy, proof, release, deployment, promotion, or publication.

[Back to top](#top)

---

<a id="current-holds-and-graduation-gates"></a>

## Current holds and graduation gates

### Current holds

| Capability | Current state | Required before graduation |
|---|---|---|
| Live Habitat source use | `HOLD` | Accepted source identity, role, rights, terms, connector, cadence, credentials boundary, fixtures, and activation decision |
| Habitat-wide schemas and validators | `HOLD` beyond one profile | Accepted contracts/schemas, substantive fixtures, validators, negative tests, and bounded consumers for each object family |
| Active Habitat policy | `HOLD` | Accepted policy source, bundle, selector, evaluator, tests, finite outcomes, reviewers, and versioned decisions |
| Sensitivity/geoprivacy execution | `HOLD` | Accepted transforms, public-safe fixtures, redaction/generalization receipts, negative tests, access controls, and accountable review |
| Evidence closure | `HOLD` | Deterministic `EvidenceRef -> EvidenceBundle` resolution, citation validation, and bounded consumer |
| Habitat proof production | Explicit workflow `HOLD` | Accepted proof contract/schema/profile, producer, validator, public-safe fixtures, policy/access binding, receipts, correction, and rollback |
| Release dry run | Explicit workflow `HOLD` | Candidate identity, immutable artifact pointer, evidence/rights/sensitivity closure, policy, review, validation receipts, correction, withdrawal, and rollback |
| Public API/map/AI consumption | `HOLD` | Governed API over released public-safe artifacts with evidence, policy, stale/correction state, and no direct internal path |
| Strong no-egress CI proof | `NEEDS VERIFICATION` | Runner/environment egress control and auditable evidence for the focused execution window |
| Accountable and independent review roles | `NEEDS VERIFICATION` | Verified assignments beyond CODEOWNERS routing |

### Graduation rule

Do not broaden this runbook merely because new files appear. A new profile belongs here only after:

- its contract, schema, deterministic profile, synthetic valid/invalid fixtures, validator, and focused tests are present;
- the profile's source, evidence, policy, sensitivity, proof, release, and public-use non-effects are explicit;
- network behavior is classified and tested in proportion to risk;
- the domain workflow deliberately wires the profile or records a clear separate entry point;
- rollback and correction are defined;
- the runbook is updated in the same dependency-closed review slice.

[Back to top](#top)

---

<a id="correction-and-document-rollback"></a>

## Correction and document rollback

### Before merge

- close the draft pull request or restore the target file on the feature branch;
- do not force-push or write directly to `main`;
- no source, lifecycle, proof, candidate, release, deployment, or publication rollback is required because this is documentation-only.

### After merge

Revert the documentation commit or restore prior blob:

```text
e7c9bba0025ea2c24db530dd0bf498e472af5727
```

Use a reviewed correction pull request. Record why the current procedure was inaccurate, which executable/profile/workflow revision controls, and whether any operator relied on the incorrect text.

### When executable behavior changes

Do not roll back code by editing this runbook. Revert or correct the owning contract, schema, profile, fixture, validator, test, or workflow through its own reviewed change, then synchronize this document. Preserve profile version/hash lineage and do not silently rewrite reviewed fixture polarity.

### Sensitive-output correction

If a log or packet contains protected detail:

1. stop sharing and preserve a restricted incident record;
2. remove public exposure through the authorized platform process;
3. rotate credentials if applicable;
4. identify the producing path and affected revisions/runs;
5. add a fail-closed negative test or logging guard;
6. issue the appropriate correction/withdrawal record through owning systems;
7. rerun only after the sensitivity boundary is reviewed.

[Back to top](#top)

---

<a id="related-current-surfaces"></a>

## Related current surfaces

| Surface | Relationship |
|---|---|
| [`docs/runbooks/README.md`](../README.md) | Parent operational-procedure boundary |
| [`docs/runbooks/habitat/SOURCE_REFRESH_RUNBOOK.md`](./SOURCE_REFRESH_RUNBOOK.md) | Source-head inspection only; no fetch or activation |
| [`docs/runbooks/habitat/PROMOTION_RUNBOOK.md`](./PROMOTION_RUNBOOK.md) | Downstream proposal-era promotion procedure; does not become authority through this pass |
| [`docs/runbooks/habitat/ROLLBACK_RUNBOOK.md`](./ROLLBACK_RUNBOOK.md) | Domain rollback documentation; no rollback is executed here |
| [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md) | Adopted placement doctrine via ADR-0029 |
| [`docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md`](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Accepted Directory Rules decision |
| [`docs/domains/habitat/README.md`](../../domains/habitat/README.md) | Habitat bounded-context and source-role doctrine |
| [`contracts/domains/habitat/land_cover/materiality_profile.md`](../../../contracts/domains/habitat/land_cover/materiality_profile.md) | Semantic contract for the one current profile |
| [`pipeline_specs/habitat/land_cover/materiality_profile.v1.json`](../../../pipeline_specs/habitat/land_cover/materiality_profile.v1.json) | Inactive deterministic profile |
| [`tools/validators/domains/habitat/validate_land_cover_materiality.py`](../../../tools/validators/domains/habitat/validate_land_cover_materiality.py) | Domain adapter |
| [`tools/validators/validate_material_change_assessment.py`](../../../tools/validators/validate_material_change_assessment.py) | Shared emitted-object validator |
| [`tests/validators/domains/habitat/test_land_cover_materiality.py`](../../../tests/validators/domains/habitat/test_land_cover_materiality.py) | Substantive focused tests |
| [`fixtures/domains/habitat/land_cover/materiality/`](../../../fixtures/domains/habitat/land_cover/materiality/) | Synthetic valid and invalid fixture profile |
| [`data/proofs/habitat/README.md`](../../../data/proofs/habitat/README.md) | Explicit proof-support boundary and hold |
| [`release/candidates/habitat/README.md`](../../../release/candidates/habitat/README.md) | No-active-candidate boundary |
| [`.github/workflows/domain-habitat.yml`](../../../.github/workflows/domain-habitat.yml) | Domain validation plus proof/release readiness holds |
| [`.github/workflows/habitat-land-cover-materiality.yml`](../../../.github/workflows/habitat-land-cover-materiality.yml) | Path-filtered focused profile validation |

[Back to top](#top)

---

<a id="operator-checklist"></a>

## Operator checklist

### Before

- [ ] Repository identity and exact revision recorded.
- [ ] Working tree state recorded and unrelated changes excluded.
- [ ] Required paths present.
- [ ] Profile status is `PROPOSED_INACTIVE`.
- [ ] All governance flags are false and `release_ref` is null.
- [ ] Fixture manifests contain seven valid and six invalid cases or the changed inventory has been reviewed.
- [ ] Dependency preparation is separated from the focused no-egress claim.
- [ ] Evidence grade and environmental network enforcement are declared.
- [ ] No real or sensitive source material is present.

### During

- [ ] Run the exact focused `unittest` discovery command.
- [ ] Run the exact fixture CLI command.
- [ ] Preserve exit codes and stdout/stderr separately.
- [ ] Treat expected invalid fixture `FAIL` lines as fixture polarity, not overall failure.
- [ ] Stop on sensitive output, live access, unexpected writes, profile governance change, or polarity drift.

### After

- [ ] Confirm repository status is unchanged.
- [ ] Record exact revision, profile hash, commands, counts, and evidence grade.
- [ ] Hash captured output if retained.
- [ ] Report hosted checks as pass/fail/pending/not-run/not-applicable/unknown.
- [ ] Preserve proof and release as `HOLD`.
- [ ] Do not commit temporary output as a receipt or proof.
- [ ] Do not imply review, release, deployment, promotion, publication, or public safety.

[Back to top](#top)

---

<a id="v1-lineage-and-superseded-assumptions"></a>

## v1 lineage and superseded assumptions

The prior v1 document was a useful planning artifact written without current repository evidence. This v0.2 retains its safe intent and supersedes its unverified current-state claims.

### Retained principles

- start with deterministic synthetic fixtures before live source activation;
- fail closed on invalid or unsupported inputs;
- keep sensitive ecological locations and credentials out of fixtures and logs;
- preserve source-role distinctions;
- treat a green test as necessary but insufficient for publication;
- keep promotion, release, correction, and rollback separate from test execution;
- make the procedure reproducible and reversible.

### Superseded as current procedure

| v1 assumption | Current repository-grounded correction |
|---|---|
| No mounted repository and unknown test/CI surface | Current profile, validator, fixtures, tests, and workflows are directly inspected |
| Full Habitat schema → evidence → rights → sensitivity → policy → release chain is runnable | Only the inactive land-cover materiality adapter is substantively executable |
| Every Habitat object family has five fixture classes | Current reviewed profile has seven valid and six invalid materiality fixtures only |
| `tests/fixtures/domains/habitat/` is the active fixture home | The current profile uses `fixtures/domains/habitat/land_cover/materiality/` |
| `tests/domains/habitat/` is the substantive suite | Inspected top-level modules are placeholders or a tautological smoke; substantive tests live under `tests/validators/domains/habitat/` |
| Habitat policy bundle is executed | Active Habitat policy evaluation is not established |
| `EvidenceBundle`, finite public runtime outcomes, receipts, and release manifests are produced | The profile emits bounded `MaterialChangeAssessment` data to stdout; governed evidence, receipts, proof, and release remain held |
| Environment egress is proven by the procedure | Current tests/workflows do not establish operating-system egress denial |
| A passing run is a promotion prerequisite for all Habitat artifacts | The pass applies only to this inactive synthetic profile and creates no promotion authority |

This lineage section preserves the planning record without allowing repetition to become implementation proof.

[Back to top](#top)

---

<a id="non-effects"></a>

## Non-effects

Updating or following this runbook does not:

- admit, activate, suspend, refresh, or withdraw a source;
- fetch or transform source bytes;
- create or mutate RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLETS, or PUBLISHED state;
- establish Habitat, land-cover, species, wetland, stewardship, or regulatory truth;
- clear rights, terms, sensitivity, geoprivacy, or public-safe precision;
- create an `EvidenceBundle`, `PolicyDecision`, `ReviewRecord`, proof, candidate, `PromotionDecision`, `ReleaseManifest`, correction notice, withdrawal notice, or rollback card;
- approve, release, deploy, promote, publish, or expose a public carrier;
- change a repository setting, branch protection, ruleset, secret, environment, workflow permission, or external connector;
- replace accountable human review.

The durable conclusion is intentionally narrow: **one inactive, synthetic, local Habitat land-cover materiality profile can be tested deterministically and handed off without being mistaken for the rest of the Habitat trust path.**

[Back to top](#top)
