<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/archaeology/no-network-test-runbook
title: Archaeology — No-Network Test Runbook
type: runbook; operational-procedure; domain-lane; sensitive-domain; non-authoritative
version: v0.2
status: draft; repository-grounded; three-substantive-fixture-profiles-present; one-profile-ci-wired; direct-domain-suite-placeholder-heavy; proof-and-release-held; non-publisher
owners:
  - '@bartytime4life — verified GitHub review route'
  - 'NEEDS VERIFICATION — accountable Archaeology, cultural/sovereignty, sensitivity, rights, evidence, policy, fixture, test, release, and independent-review stewards'
created: 2026-05-13
updated: 2026-08-23
policy_label: public-review; archaeology; cultural-heritage; no-network; synthetic-fixtures; fail-closed; exact-location-denied; no-publication-authority
current_path: docs/runbooks/archaeology/NO_NETWORK_TEST_RUNBOOK.md
owning_root: docs/
responsibility: >
  Provide the repository-grounded procedure for executing and interpreting
  bounded Archaeology no-network checks while keeping protected knowledge,
  source admission, evidence authority, cultural authority, policy, lifecycle,
  review, release, deployment, and publication outside the test boundary.
truth_posture: cite-or-abstain
truth_labels: [CONFIRMED, PROPOSED, UNKNOWN, NEEDS VERIFICATION, CONFLICTED, HOLD]
authority_class: explanatory operational documentation
canonical_relationship: same-path update; no new or parallel authority
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 2c010b36609bf2ceb94e5a2d61fa62493e6f298f
  prior_blob: d4418d5e379007965616032fa689472675b147b5
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  domain_workflow_blob: d51ba3b1244844a83d857a34305e1a167e20dadb
  inspected_surfaces:
    - docs/runbooks/README.md
    - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
    - docs/doctrine/directory-rules.md
    - .github/workflows/domain-archaeology.yml
    - Makefile
    - contracts/domains/archaeology/
    - schemas/contracts/v1/domains/archaeology/
    - fixtures/contracts/v1/domains/archaeology/
    - fixtures/domains/archaeology/README.md
    - policy/domains/archaeology/README.md
    - tests/domains/archaeology/
    - tests/validators/domains/archaeology/
    - tools/validators/domains/archaeology/
related:
  - ../README.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../domains/archaeology/README.md
  - ../../domains/archaeology/SENSITIVITY.md
  - ../../domains/archaeology/CULTURAL_REVIEW.md
  - ../../domains/archaeology/PUBLICATION_AND_POLICY.md
  - ../../../contracts/domains/archaeology/README.md
  - ../../../schemas/contracts/v1/domains/archaeology/README.md
  - ../../../fixtures/domains/archaeology/README.md
  - ../../../policy/domains/archaeology/README.md
  - ../../../tests/domains/archaeology/README.md
  - ../../../tools/validators/domains/archaeology/README.md
  - ../../../.github/workflows/domain-archaeology.yml
tags: [kfm, archaeology, cultural-heritage, runbook, tests, no-network, fixtures, governance, sensitivity, fail-closed]
notes:
  - 'v0.2 replaces no-mounted-repository assumptions, nonexistent aggregate commands, and unverified pass records with current repository evidence and exact bounded commands.'
  - 'A green fixture-profile run proves only that declared synthetic cases produced their expected finite outcomes at the tested revision.'
  - 'This document changes no test, fixture, contract, schema, policy, validator, workflow, receipt, proof, lifecycle object, review, release record, deployment, or publication state.'
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Archaeology — No-Network Test Runbook

> **Run deterministic, synthetic, coordinate-free Archaeology checks while keeping live sources, protected cultural knowledge, exact or reverse-engineerable locations, internal stores, model providers, promotion, release, and publication outside the test boundary.**

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#4-current-repository-state)
[![Network contract: local-only](https://img.shields.io/badge/network-local--only-critical?style=flat-square)](#5-no-network-contract)
[![Substantive profiles: 3](https://img.shields.io/badge/substantive%20profiles-3-1f883d?style=flat-square)](#4-current-repository-state)
[![CI-wired profiles: 1](https://img.shields.io/badge/CI--wired%20profiles-1-0969da?style=flat-square)](#4-current-repository-state)
[![Proof and release: HOLD](https://img.shields.io/badge/proof%20%26%20release-HOLD-d4a72c?style=flat-square)](#4-current-repository-state)
[![Publisher: no](https://img.shields.io/badge/publisher-no-6e7781?style=flat-square)](#2-authority-and-non-effects)

> [!IMPORTANT]
> **Current state is bounded, not complete.** The repository contains three substantive synthetic fixture profiles: Archaeological Volume Measurement Assessment, Three-Dimensional Documentation, and Three-Dimensional Visibility Assumption Disclosure. Only the Three-Dimensional Documentation profile is wired into the dedicated `domain-archaeology` workflow. The direct `tests/domains/archaeology/` lane remains placeholder-heavy, and the workflow keeps proof production and release dry-run work explicitly on `HOLD`.

> [!CAUTION]
> A passing test, validator, workflow, schema check, deterministic digest, or fixture replay is not an `EvidenceBundle`, cultural or sovereignty decision, rights clearance, `PolicyDecision`, proof, review approval, promotion decision, release approval, deployment, or publication.

> [!WARNING]
> Do not place real site identifiers, exact or reverse-engineerable geometry, burial or human-remains context, sacred or culturally restricted knowledge, collection-security detail, looting-risk detail, restricted oral history, private-landowner detail, or unreviewed community knowledge in fixtures, test names, logs, snapshots, reports, workflow summaries, or generated artifacts.

**Quick navigation:** [Purpose](#1-purpose) · [Authority](#2-authority-and-non-effects) · [Placement](#3-repo-fit-and-placement) · [State](#4-current-repository-state) · [Network](#5-no-network-contract) · [Inputs](#6-inputs-and-exclusions) · [Preflight](#7-preflight) · [Quickstart](#8-quickstart) · [Profiles](#9-profile-and-command-matrix) · [Procedure](#10-full-execution-procedure) · [Results](#11-result-interpretation) · [Failures](#12-failure-diagnosis-and-escalation) · [CI](#13-ci-review-and-evidence-boundary) · [Containment](#14-sensitive-material-containment) · [Rollback](#15-rollback-and-correction) · [Checklist](#16-acceptance-checklist) · [Record](#17-run-record-template) · [Open work](#18-open-verification-register) · [Related](#19-related-surfaces) · [Change log](#20-change-log) · [Glossary](#21-glossary)

---

## 1. Purpose

This runbook defines the **human procedure** for executing, reviewing, and reporting bounded Archaeology checks that must remain deterministic, synthetic, and local-only.

It answers five questions:

1. Which Archaeology no-network checks are currently substantive?
2. Which exact commands reproduce those checks?
3. Which checks are wired into hosted CI, and which remain local-only?
4. What does each finite result prove—and what does it not prove?
5. Which broader claims must remain `HOLD`, `UNKNOWN`, or `NEEDS VERIFICATION`?

The durable flow is:

```text
synthetic declaration fixture
  -> accepted schema shape for that bounded profile
  -> deterministic validator
  -> expected PASS / ABSTAIN / DENY / ERROR result
  -> reviewable test output
  -/> site confirmation
  -/> cultural or sovereignty authority
  -/> source admission
  -/> EvidenceBundle construction
  -/> policy activation
  -/> promotion
  -/> release
  -/> publication
```

The lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLETS -> PUBLISHED
```

No command in this runbook performs that lifecycle. The current commands inspect fixed repository fixtures and declarations only.

[Back to top](#top)

---

## 2. Authority and non-effects

This runbook is operational documentation. It can point to current tests, validators, fixtures, schemas, contracts, policy, workflows, and holds. It cannot replace or activate any of them.

| Concern | Owning authority | Runbook role |
|---|---|---|
| Placement and documentation boundary | Accepted Directory Rules and `docs/` root contract | Explain the procedure and current path |
| Archaeology object meaning | `contracts/domains/archaeology/` | Cite semantics; do not redefine them |
| Machine shape | `schemas/contracts/v1/domains/archaeology/` and shared canonical schemas | Cite tested shapes; do not create schema authority |
| Synthetic test inputs | Accepted fixture roots | Identify bounded fixtures; do not treat them as records or evidence |
| Validator behavior | `tools/validators/` | Point to exact entry points and finite outcomes |
| Test enforcement | `tests/` | Point to assertions; do not infer enforcement from filenames |
| Rights, sensitivity, consent, cultural and sovereignty decisions | Governed policy and human-review authorities | Preserve fail-closed requirements; do not appoint authority |
| Evidence | `EvidenceRef`, `EvidenceBundle`, proof, and receipt families | State closure requirements; do not manufacture support |
| Lifecycle state | Governed `data/` lanes and transition controls | State non-effects |
| Review and release | Review, `release/`, correction, withdrawal, and rollback authorities | Keep separate from validation |
| Public delivery | Governed APIs and released public-safe carriers | Outside this procedure |

### Non-effects

Running or updating this runbook does **not**:

- confirm an archaeological site, feature, chronology, interpretation, volume, visibility, or cultural association;
- admit a source or activate a connector;
- construct or resolve an `EvidenceBundle`;
- determine rights, sovereignty, consent, cultural authority, or sensitivity;
- activate a policy bundle or evaluator;
- move an object between lifecycle states;
- produce a proof pack, release candidate, or release manifest;
- approve review, promotion, release, deployment, or publication; or
- authorize public use of any Archaeology material.

### Directory Rules result

**Placement outcome: `PLACE` — CONFIRMED for this same-path update.**

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts [Directory Rules v2](../../doctrine/directory-rules.md). This tracked file already lives in the operational-procedure lane under `docs/`, with `archaeology` as a domain segment rather than a new authority root.

[Back to top](#top)

---

## 3. Repo fit and placement

| Property | Current result |
|---|---|
| Path | `docs/runbooks/archaeology/NO_NETWORK_TEST_RUNBOOK.md` |
| Authority owner | `docs/` — human-facing operational procedure |
| Domain scope | Archaeology and cultural heritage |
| Path state | Existing tracked path; same-path modernization |
| Structural effect | None; no create, move, rename, split, mirror, or delete |
| Default GitHub review route | `@bartytime4life` |
| Functional and independent stewards | `NEEDS VERIFICATION` |
| Executable authority | None; commands remain owned by tests, validators, fixtures, and workflows |
| Release or publication effect | None |

This file may explain current repository behavior. It may not turn documentation into runtime, policy, evidence, review, or release authority.

[Back to top](#top)

---

## 4. Current repository state

The observations below are pinned to `main@2c010b36609bf2ceb94e5a2d61fa62493e6f298f`.

### 4.1 Substantive fixture profiles

| Profile | Current paired surfaces | Declared fixture matrix | Dedicated CI | Bounded conclusion |
|---|---|---:|---|---|
| Archaeological Volume Measurement Assessment | Contract, closed schema, fixture manifest, validator, unit test | 26 cases | Not wired in `domain-archaeology.yml` | `CONFIRMED PRESENT`; local fixture-profile validation only |
| Three-Dimensional Documentation | Contract, closed schema, fixture manifest, validator, unit test | 21 cases | Yes | `CONFIRMED PRESENT AND CI-WIRED`; paradata/profile conformance only |
| Three-Dimensional Visibility Assumption Disclosure | Contract, closed schema, fixture manifest, validator, unit test | 23 cases | Not wired in `domain-archaeology.yml` | `CONFIRMED PRESENT`; local fixture-profile validation only |
| EvidenceBundle schema convergence | Domain projection plus shared schema fixtures and unit test | Shared valid/invalid fixtures | Not explicitly wired in the dedicated job | `CONFIRMED PRESENT`; schema-delegation proof only |

All three validator profiles expose the finite outcomes `PASS`, `ABSTAIN`, `DENY`, and `ERROR`. Their tests exercise deterministic replay and patch common Python socket entry points during replay.

### 4.2 Placeholder-heavy surfaces

The direct `tests/domains/archaeology/` lane is **not** a substantive broad Archaeology suite at this snapshot.

- Thirteen named modules remain one-line `PROPOSED` placeholders.
- `test_archaeology_smoke.py` contains a vacuous `assert True` smoke check.
- `test_no_network_fixtures.py` does not prove fixture safety or no-network behavior.
- Several child validator files remain tiny placeholders, including catalog, EvidenceBundle, schema, and SourceDescriptor validators.
- File names and collection success must not be cited as enforcement.

### 4.3 Dedicated workflow

`.github/workflows/domain-archaeology.yml` currently:

- uses Python 3.11;
- installs declared test dependencies through `python tools/ci/install_python_ci.py project-test`;
- sets `KFM_NO_NETWORK=1`, deterministic hashing/time variables, and noninteractive pip variables;
- compiles, unit-tests, and replays the Three-Dimensional Documentation fixture profile;
- records a bounded job summary; and
- retains explicit `WORKFLOW_HOLD` jobs for proof construction and release dry-run readiness.

| Workflow job | Current state | What a green job proves |
|---|---|---|
| `validate-archaeology` | Substantive for Three-Dimensional Documentation | The exact synthetic profile produced its expected fixture outcomes |
| `build-proof-archaeology` | `WORKFLOW_HOLD` | Required proof boundaries remain present and no unreviewed producer has silently appeared |
| `publish-dry-run-archaeology` | `WORKFLOW_HOLD` | Required release boundaries remain present and no unreviewed candidate or command has silently appeared |

### 4.4 Absent aggregate command

There is no verified `make test-archaeology-no-network` target at the pinned snapshot. Do not use or document that command as current behavior.

[Back to top](#top)

---

## 5. No-network contract

### 5.1 What is confirmed

The current bounded profiles are designed for fixed repository inputs. Their unit tests patch `socket.socket` and `socket.create_connection` during deterministic fixture replay so an attempted call through those common Python paths fails.

The dedicated workflow also sets:

```text
KFM_NO_NETWORK=1
PIP_DISABLE_PIP_VERSION_CHECK=1
PIP_NO_INPUT=1
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
TZ=UTC
PYTHONUNBUFFERED=1
```

### 5.2 What is not confirmed

`KFM_NO_NETWORK=1` is a contract marker, not an operating-system firewall. The workflow installs dependencies before executing the profile and does not itself prove global runner egress denial.

Therefore:

| Claim | Status |
|---|---|
| Selected fixture replay uses local tracked files | `CONFIRMED` |
| Common Python socket calls are denied inside the three substantive replay tests | `CONFIRMED` |
| Every library, subprocess, native extension, DNS path, and runner interface is globally blocked | `UNKNOWN / NEEDS VERIFICATION` |
| The dedicated workflow is an independently certified air-gapped environment | `UNKNOWN` |

> [!IMPORTANT]
> Do not describe the current workflow as air-gapped. Describe it as a bounded local-fixture profile with socket-denial assertions and an explicit no-network contract marker.

### 5.3 Required operator posture

For the strongest rehearsal available today:

1. run in an approved isolated environment with outbound egress denied outside the process;
2. provide no ambient cloud, source, model, database, object-store, or signing credentials to repository code;
3. install dependencies before entering the isolated execution phase, or use a reviewed immutable environment image;
4. run only fixed local fixture commands;
5. record the exact environment and commit identity; and
6. treat any attempted network access as `FAIL` or `ERROR`, never as a skipped optional check.

[Back to top](#top)

---

## 6. Inputs and exclusions

### 6.1 Required local inputs

| Input | Requirement |
|---|---|
| Repository revision | Exact feature-branch or commit SHA under review |
| Working directory | Repository root |
| Python | 3.11 for parity with the dedicated workflow |
| Dependencies | Repository-declared test environment |
| Fixtures | Tracked synthetic manifests only |
| Network | No source, API, model, tile, database, graph, vector, or object-store access during execution |
| Credentials | None available to test code |
| Time and hashing | `TZ=UTC`, `PYTHONHASHSEED=0` |
| Output | Public-safe console text only; no protected payloads or retained sensitive artifacts |

### 6.2 Forbidden inputs

Stop the run if any selected fixture, log, snapshot, report, or generated artifact contains or could reveal:

- real exact archaeological site coordinates, polygons, elevations, routes, or collection locations;
- reverse-engineerable generalized detail combined with named context;
- burial, human-remains, sacred, ceremonial, or culturally restricted location detail;
- restricted oral history or community knowledge without authority;
- collection-security or looting-risk details;
- private-landowner, parcel, assessor, address, or living-person data;
- DNA or descendant-match information;
- real credentials, tokens, signed URLs, internal handles, or private storage identifiers;
- a pointer that causes repository code to read `RAW`, `WORK`, `QUARANTINE`, or another internal canonical store; or
- a live source, model, map, tile, vector, search, graph, API, database, or object-store dependency.

A sensitive fixture is not a test-quality problem. It is a containment event. Follow [Sensitive material containment](#14-sensitive-material-containment).

[Back to top](#top)

---

## 7. Preflight

Run preflight before executing repository code.

### 7.1 Freeze identity

```bash
git status --short
git branch --show-current
git rev-parse HEAD
git rev-parse --verify HEAD^{commit}
```

Record:

- exact head SHA;
- base SHA;
- changed paths;
- whether the tree is clean;
- Python and dependency identity;
- whether runner-level egress denial is enforced; and
- whether test code can see credentials.

### 7.2 Inspect the change boundary

```bash
git diff --name-status <base-sha>...HEAD
git diff --check <base-sha>...HEAD
```

Stop if the change unexpectedly touches:

- real Archaeology data;
- lifecycle stores;
- policy or cultural-review authority;
- source activation;
- release candidates or published outputs;
- repository settings, secrets, or deployment state; or
- an overlapping branch or pull request that owns the same path.

### 7.3 Install declared test dependencies

Match the workflow:

```bash
python tools/ci/install_python_ci.py project-test
python --version
python -m pytest --version
```

Dependency installation may use the network in a separate setup phase. That setup traffic is not Archaeology fixture execution and must not be misreported as proof that the test phase was globally offline.

### 7.4 Set deterministic execution variables

```bash
export KFM_NO_NETWORK=1
export PYTHONDONTWRITEBYTECODE=1
export PYTHONHASHSEED=0
export PYTHONUNBUFFERED=1
export TZ=UTC
```

[Back to top](#top)

---

## 8. Quickstart

### 8.1 Reproduce the current CI-wired profile

```bash
set -euo pipefail

export KFM_NO_NETWORK=1
export PYTHONDONTWRITEBYTECODE=1
export PYTHONHASHSEED=0
export PYTHONUNBUFFERED=1
export TZ=UTC

python -m py_compile \
  tools/validators/domains/archaeology/validate_three_d_documentation.py \
  tests/validators/domains/archaeology/test_validate_three_d_documentation.py

python -m unittest \
  tests.validators.domains.archaeology.test_validate_three_d_documentation \
  --verbose

python tools/validators/domains/archaeology/validate_three_d_documentation.py \
  --fixtures
```

This is the exact substantive command sequence in the dedicated workflow. It validates one fixture profile only.

### 8.2 Run the current substantive local set

```bash
set -euo pipefail

export KFM_NO_NETWORK=1
export PYTHONDONTWRITEBYTECODE=1
export PYTHONHASHSEED=0
export PYTHONUNBUFFERED=1
export TZ=UTC

python -m py_compile \
  tools/validators/domains/archaeology/validate_archaeological_volume_measurement_assessment.py \
  tools/validators/domains/archaeology/validate_three_d_documentation.py \
  tools/validators/domains/archaeology/validate_three_d_visibility_assumption_disclosure.py \
  tests/validators/domains/archaeology/test_evidence_bundle_schema_convergence.py \
  tests/validators/domains/archaeology/test_validate_archaeological_volume_measurement_assessment.py \
  tests/validators/domains/archaeology/test_validate_three_d_documentation.py \
  tests/validators/domains/archaeology/test_validate_three_d_visibility_assumption_disclosure.py

python -m unittest \
  tests.validators.domains.archaeology.test_evidence_bundle_schema_convergence \
  tests.validators.domains.archaeology.test_validate_archaeological_volume_measurement_assessment \
  tests.validators.domains.archaeology.test_validate_three_d_documentation \
  tests.validators.domains.archaeology.test_validate_three_d_visibility_assumption_disclosure \
  --verbose

python tools/validators/domains/archaeology/validate_archaeological_volume_measurement_assessment.py --fixtures
python tools/validators/domains/archaeology/validate_three_d_documentation.py --fixtures
python tools/validators/domains/archaeology/validate_three_d_visibility_assumption_disclosure.py --fixtures
```

### 8.3 Inspect placeholder drift

```bash
python -m pytest tests/domains/archaeology --collect-only -q

git grep -n 'PROPOSED placeholder' -- \
  tests/domains/archaeology \
  tools/validators/domains/archaeology

git grep -n 'assert True' -- tests/domains/archaeology
```

Collection is an inventory check. It is not proof that the named invariants are substantively tested.

[Back to top](#top)

---

## 9. Profile and command matrix

| Surface | Unit-test command | Fixture command | Expected bounded result | Current CI state |
|---|---|---|---|---|
| EvidenceBundle schema convergence | `python -m unittest tests.validators.domains.archaeology.test_evidence_bundle_schema_convergence --verbose` | None | Domain projection delegates to the shared closed schema and preserves valid/invalid polarity | Local substantive test; dedicated CI binding not established |
| Volume Measurement Assessment | `python -m unittest tests.validators.domains.archaeology.test_validate_archaeological_volume_measurement_assessment --verbose` | `python tools/validators/domains/archaeology/validate_archaeological_volume_measurement_assessment.py --fixtures` | 26 declared cases reproduce expected finite outcomes | Local substantive profile |
| Three-Dimensional Documentation | `python -m unittest tests.validators.domains.archaeology.test_validate_three_d_documentation --verbose` | `python tools/validators/domains/archaeology/validate_three_d_documentation.py --fixtures` | 21 declared cases reproduce expected finite outcomes | Dedicated workflow |
| Visibility Assumption Disclosure | `python -m unittest tests.validators.domains.archaeology.test_validate_three_d_visibility_assumption_disclosure --verbose` | `python tools/validators/domains/archaeology/validate_three_d_visibility_assumption_disclosure.py --fixtures` | 23 declared cases reproduce expected finite outcomes | Local substantive profile |
| Direct domain suite | `python -m pytest tests/domains/archaeology -q` | None | Mostly placeholder collection plus vacuous smoke | Not acceptable as broad proof |
| Archaeology proof producer | None | None | `HOLD` | Workflow readiness hold |
| Archaeology release dry-run | None | None | `HOLD` | Workflow readiness hold |

### Fixture-profile paths

| Profile | Contract | Schema | Fixture manifest | Validator | Test |
|---|---|---|---|---|---|
| Volume Measurement Assessment | `contracts/domains/archaeology/archaeological_volume_measurement_assessment.md` | `schemas/contracts/v1/domains/archaeology/archaeological_volume_measurement_assessment.schema.json` | `fixtures/contracts/v1/domains/archaeology/archaeological_volume_measurement_assessment/cases.json` | `tools/validators/domains/archaeology/validate_archaeological_volume_measurement_assessment.py` | `tests/validators/domains/archaeology/test_validate_archaeological_volume_measurement_assessment.py` |
| Three-Dimensional Documentation | `contracts/domains/archaeology/three_d_documentation.md` | `schemas/contracts/v1/domains/archaeology/three_d_documentation.schema.json` | `fixtures/contracts/v1/domains/archaeology/three_d_documentation/cases.json` | `tools/validators/domains/archaeology/validate_three_d_documentation.py` | `tests/validators/domains/archaeology/test_validate_three_d_documentation.py` |
| Visibility Assumption Disclosure | `contracts/domains/archaeology/three_d_visibility_assumption_disclosure.md` | `schemas/contracts/v1/domains/archaeology/three_d_visibility_assumption_disclosure.schema.json` | `fixtures/contracts/v1/domains/archaeology/three_d_visibility_assumption_disclosure/cases.json` | `tools/validators/domains/archaeology/validate_three_d_visibility_assumption_disclosure.py` | `tests/validators/domains/archaeology/test_validate_three_d_visibility_assumption_disclosure.py` |

[Back to top](#top)

---

## 10. Full execution procedure

### Step 1 — Select the bounded profile

Select only the profile affected by the change. Run all substantive profiles when shared Archaeology schema, fixture, validator, or test behavior changes.

Do not substitute the placeholder direct-domain suite for the paired validator tests.

### Step 2 — Verify required files

```bash
required_paths=(
  contracts/domains/archaeology/three_d_documentation.md
  schemas/contracts/v1/domains/archaeology/three_d_documentation.schema.json
  fixtures/contracts/v1/domains/archaeology/three_d_documentation/cases.json
  tools/validators/domains/archaeology/validate_three_d_documentation.py
  tests/validators/domains/archaeology/test_validate_three_d_documentation.py
)

for required_path in "${required_paths[@]}"; do
  test -f "$required_path" || {
    printf 'missing required path: %s\n' "$required_path" >&2
    exit 1
  }
done
```

Change the path family when running another profile.

### Step 3 — Compile changed Python

Run `python -m py_compile` against the selected validator and its test module. Compile success proves parse/import syntax only.

### Step 4 — Run the paired unit test

The substantive tests currently verify combinations of:

- JSON Schema validity;
- deterministic identity and hash binding;
- exact fixture count and expected finite outcome polarity;
- coordinate-free or public-safe fixture shape;
- fail-closed source, uncertainty, interpretation, assumption, sensitivity, transform, correction, and rollback requirements;
- duplicate-key and non-finite-number rejection; and
- deterministic replay while common Python socket paths are patched to fail.

A test pass does not inspect actual 3D assets, run a viewshed, calculate a real volume, resolve a site, or approve interpretation.

### Step 5 — Replay the fixture CLI

The validator `--fixtures` commands emit one compact JSON result per declared case. The command succeeds only when every observed outcome and finding list matches the fixture manifest.

Capture console output only when it is public-safe. Do not retain data-shaped debug dumps merely for convenience.

### Step 6 — Re-run for determinism

Run the selected unit test and fixture CLI a second time in the same environment when identity, hashing, ordering, or output changes. Compare normalized output.

### Step 7 — Inspect writes

```bash
git status --short
git diff --name-status
```

The current profile commands should not write lifecycle, proof, release, or published state. Unexpected writes are a failure until explained and reviewed.

### Step 8 — Classify results

Separate:

- expected negative fixture outcomes;
- introduced implementation failures;
- inherited repository failures;
- held work; and
- environment or orchestration errors.

### Step 9 — Record exact-head evidence

Record the exact tested head and commands. Do not reuse results from an older commit after the branch changes.

### Step 10 — Inspect hosted checks

Hosted CI is separate evidence. A local pass does not predict hosted success, and a green hosted check does not perform human review or authorize merge, release, or publication.

[Back to top](#top)

---

## 11. Result interpretation

### 11.1 Validator outcomes

| Outcome | Meaning in the current bounded profiles | Operator action |
|---|---|---|
| `PASS` | The synthetic candidate is internally coherent for the declared fixture profile | Record bounded conformance; do not claim archaeology truth or release readiness |
| `ABSTAIN` | Required method, measurement, uncertainty, assumption, evidence, review, or governance detail is unresolved | Preserve the gap; do not fabricate a value or silently convert to pass |
| `DENY` | Shape, identity, source, representation, uncertainty, sensitivity, transform, public-candidate, correction, or rollback rules conflict | Keep the candidate out of the permitted path and fix the input or governing implementation |
| `ERROR` | Declared processing state is error or bounded file handling cannot complete safely | Diagnose environment/input handling; do not reinterpret as abstention or denial |

### 11.2 Test results versus fixture outcomes

A **passing test suite** can contain many expected `ABSTAIN`, `DENY`, and `ERROR` cases. The suite passes because the validator produced the declared result—not because every fixture was accepted.

A test failure means at least one expectation, implementation, schema, identity rule, fixture, or environment changed. It does not automatically mean the change is unsafe, but the difference must be explained and reviewed.

### 11.3 Workflow holds

A green readiness-hold job means the hold conditions were preserved. It is not proof construction or a release dry run.

### 11.4 Claim ceiling

A clean bounded run may support this statement:

> At `<exact-head>`, the selected synthetic Archaeology fixture profile reproduced its declared finite outcomes under the recorded environment and no-network controls.

It does not support stronger claims about sites, cultural authority, live sources, EvidenceBundles, policy enforcement, release, deployment, or publication.

[Back to top](#top)

---

## 12. Failure diagnosis and escalation

| Failure | Likely class | Immediate action |
|---|---|---|
| Missing paired contract/schema/fixture/validator/test | Dependency closure | Stop; restore or deliberately migrate the paired surface |
| Schema load or schema self-check fails | Machine-shape failure | Inspect the schema diff; do not weaken closure to make fixtures pass |
| Fixture count changes | Contract/fixture drift | Require intentional versioned explanation and updated expectations |
| Expected finding order changes | Determinism or vocabulary drift | Verify canonical ordering and compatibility implications |
| Identity or `spec_hash` mismatch | Deterministic identity failure | Inspect canonicalization and changed bound fields |
| Duplicate key or non-finite number is accepted | Parser safety regression | Stop and restore fail-closed input handling |
| Public candidate lacks sensitivity, transform, correction, or rollback closure | Governance failure | Preserve `DENY`; do not relax the negative fixture |
| Unknown assumptions produce `PASS` | Cite-or-abstain regression | Restore `ABSTAIN` behavior |
| Exact geometry or coordinate fields appear | Sensitive-material event | Stop execution and follow containment |
| Socket patch catches a call | Network-boundary violation | Record `FAIL`; identify caller; do not permit as optional telemetry |
| Runner reaches network outside patched Python paths | Environment-boundary gap | Mark global no-network claim `UNPROVED`; strengthen the runner profile |
| Unexpected file writes | Side-effect regression | Stop; inspect every write before cleanup |
| Hosted failure outside changed paths | Possible inherited failure | Compare exact-head and base evidence before attribution |
| Proof or release hold detects a new producer/candidate | Governance transition | Do not delete the hold; open a separate review for admission and wiring |

### Escalation rule

Escalate rather than improvise when the issue involves:

- real or potentially real protected Archaeology material;
- cultural, sovereignty, consent, rights-holder, or community authority;
- exact/reverse-engineerable location;
- public exposure or data export;
- an EvidenceBundle, proof, policy, release, correction, withdrawal, or rollback decision;
- a workflow or target that would replace an explicit hold; or
- a required reviewer whose authority is unresolved.

[Back to top](#top)

---

## 13. CI, review, and evidence boundary

### Current workflow responsibility

The dedicated workflow orchestrates one bounded fixture profile and two readiness holds. It does not:

- read protected Archaeology payloads;
- fetch live sources;
- resolve cultural authority;
- build an EvidenceBundle or proof pack;
- activate policy;
- promote lifecycle objects;
- create a release candidate;
- deploy; or
- publish.

### Pull-request handoff

A useful handoff records:

| Field | Required content |
|---|---|
| Base | Exact base SHA |
| Head | Exact branch head SHA |
| Changed files | Exact paths and count |
| Selected profile | Why it is the smallest sound validation set |
| Commands | Exact commands run |
| Local results | Pass/fail by command, with expected negative outcomes distinguished |
| No-network evidence | Marker, socket-denial assertions, and runner-level egress posture |
| Hosted results | Exact-head checks, including pending/skipped/failure states |
| Limitations | Placeholder surfaces and held work |
| Human review | Requested/pending/completed, kept separate from CI |
| Non-effects | No release, deployment, promotion, or publication |
| Rollback | Revert or forward-fix boundary |

### Exact-head rule

When the pull-request head changes, prior hosted results become historical evidence. Re-check the current head before marking the handoff ready.

[Back to top](#top)

---

## 14. Sensitive material containment

> [!CAUTION]
> Do not copy suspected protected content into an issue, pull-request comment, chat transcript, test failure, screenshot, or public artifact while escalating it.

If protected or potentially protected material appears:

1. **Stop** the run and prevent further processing.
2. **Do not print or reopen** the payload merely to inspect it.
3. **Contain** access using the approved security and repository process.
4. **Record only public-safe metadata**: affected path, commit, detection time, actor, and a non-revealing reason code.
5. **Notify authorized reviewers** through the approved private channel.
6. **Assess history and cache exposure** before assuming a working-tree deletion is sufficient.
7. **Revoke or rotate credentials** if any secret or signed capability may be exposed.
8. **Determine correction and rollback** without publishing the sensitive substance.
9. **Create a synthetic regression fixture** only after authorized review and without reproducing the protected data.
10. **Resume** only after an authorized containment decision.

Suggested public-safe reason codes:

- `PROTECTED_ARCHAEOLOGY_CONTENT_DETECTED`
- `EXACT_LOCATION_DISCLOSURE_RISK`
- `REVERSE_INFERENCE_RISK`
- `CULTURAL_REVIEW_REQUIRED`
- `RIGHTS_OR_CONSENT_UNRESOLVED`
- `COLLECTION_SECURITY_RISK`
- `CREDENTIAL_EXPOSURE_SUSPECTED`

[Back to top](#top)

---

## 15. Rollback and correction

### Documentation-only rollback

For this runbook update, rollback is one focused commit revert or a corrective same-path edit. No test, fixture, schema, contract, policy, workflow, lifecycle object, release object, deployment, or published state must move with the documentation rollback.

### Test/fixture change rollback

For future executable changes:

- revert the smallest feature-branch commit that introduced the regression; or
- forward-fix when reverting would erase required correction or compatibility work;
- preserve negative fixtures unless the governing contract intentionally changes;
- do not force-push shared history;
- re-run the selected exact-head profile after rollback; and
- keep correction, human review, merge, release, deployment, promotion, and publication as separate transitions.

### Never do this

- Move a denied fixture into a valid directory to make CI green.
- Delete a negative case without explaining the changed rule.
- weaken sensitivity, transform, correction, or rollback requirements for convenience;
- report a reverted file as proof that external caches, artifacts, or history are clean; or
- treat closing a pull request as a release rollback.

[Back to top](#top)

---

## 16. Acceptance checklist

### Identity and scope

- [ ] Exact base and head SHAs are recorded.
- [ ] The change set is bounded to the intended profile or documentation path.
- [ ] No overlapping pull request or task branch owns the same surface.
- [ ] The same-path `docs/` placement remains valid.

### No-network and fixture safety

- [ ] `KFM_NO_NETWORK=1` is set for repository-code execution.
- [ ] Selected tests exercise socket-denial assertions.
- [ ] Runner-level egress status is recorded as `true`, `false`, or `UNKNOWN`.
- [ ] No credentials are available to test code.
- [ ] Fixtures are tracked, synthetic, deterministic, coordinate-free or explicitly public-safe, and reviewable.
- [ ] Dependency setup traffic is separated from test-execution evidence.

### Sensitivity and governance

- [ ] Fixtures and output contain no real or reverse-engineerable protected location.
- [ ] No burial, human-remains, sacred, culturally restricted, collection-security, looting-risk, restricted oral-history, private-landowner, or living-person detail is present.
- [ ] Candidate status is not upgraded to site status.
- [ ] `EvidenceBundle`, policy, cultural authority, review, proof, release, deployment, and publication claims remain separate.
- [ ] Public-candidate negative cases preserve transform, sensitivity, correction, and rollback requirements.
- [ ] Logs and workflow summaries are public-safe.

### Validation and handoff

- [ ] Compile checks ran for changed Python surfaces.
- [ ] Selected unit tests ran at the exact head.
- [ ] Selected fixture CLIs ran with `--fixtures`.
- [ ] Introduced and inherited failures are distinguished.
- [ ] Hosted checks are attached or marked pending.
- [ ] Human review remains pending unless an authorized reviewer actually completed it.
- [ ] Rollback instructions are present.

[Back to top](#top)

---

## 17. Run record template

Use this template in a pull-request comment, issue, or approved validation record. Do not place protected details in it.

```yaml
runbook: docs/runbooks/archaeology/NO_NETWORK_TEST_RUNBOOK.md
runbook_version: v0.2
repository:
  name: bartytime4life/Kansas-Frontier-Matrix
  base_sha: '<base-sha>'
  head_sha: '<exact-tested-head>'
  dirty_tree: false
  changed_paths:
    - '<path>'
environment:
  runner: '<local | GitHub-hosted | approved-isolated-runner>'
  operating_system: '<value>'
  python: '<value>'
  dependency_identity: '<lock/image/environment digest or NEEDS VERIFICATION>'
  kfm_no_network: true
  socket_patch_exercised: true
  runner_egress_denied: '<true | false | UNKNOWN>'
  credentials_available_to_test_code: false
  timezone: UTC
  python_hash_seed: '0'
profiles:
  evidence_bundle_schema_convergence:
    selected: false
    result: '<PASS | FAIL | NOT_RUN>'
  archaeological_volume_measurement_assessment:
    selected: false
    expected_cases: 26
    result: '<PASS | FAIL | NOT_RUN>'
  three_d_documentation:
    selected: true
    expected_cases: 21
    observed_outcomes: [PASS, ABSTAIN, DENY, ERROR]
    result: '<PASS | FAIL | NOT_RUN>'
  three_d_visibility_assumption_disclosure:
    selected: false
    expected_cases: 23
    result: '<PASS | FAIL | NOT_RUN>'
placeholder_posture:
  direct_domain_suite_substantive: false
  placeholder_files_observed: true
  broad_make_target_present: false
hosted_ci:
  exact_head_inspected: false
  domain_archaeology: '<PENDING | PASS | FAIL | NOT_RUN>'
  introduced_failures: []
  inherited_failures: []
governance:
  sensitive_material_detected: false
  cultural_or_sovereignty_review_completed: false
  evidence_bundle_constructed: false
  policy_activated: false
  proof_constructed: false
  release_decision_created: false
  deployed: false
  published: false
overall: '<PASS_BOUNDED_PROFILE | FAIL | HOLD | ERROR>'
limitations:
  - 'Fixture-profile conformance only.'
rollback:
  - 'Revert the feature-branch commit or apply a focused correction.'
```

[Back to top](#top)

---

## 18. Open verification register

| ID | Question | Current state | Closure evidence |
|---|---|---|---|
| `ARCH-NN-001` | Which named humans or institutions hold Archaeology, cultural, sovereignty, rights, sensitivity, policy, evidence, release, and independent-review duties? | `UNKNOWN` | Accepted role and review records |
| `ARCH-NN-002` | Should the two substantive local-only profiles be wired into the dedicated workflow? | `NEEDS VERIFICATION` | Scoped CI decision, runtime budget, exact commands, and review |
| `ARCH-NN-003` | What runner-level mechanism proves global egress denial? | `NEEDS VERIFICATION` | Approved isolated-runner profile and test evidence |
| `ARCH-NN-004` | When will direct `tests/domains/archaeology/` placeholders become deterministic assertions? | `HOLD` | Dependency-closed implementation and negative fixtures |
| `ARCH-NN-005` | When will placeholder child validators be replaced or retired? | `HOLD` | Accepted contracts, schemas, fixtures, tests, and migration note |
| `ARCH-NN-006` | Is there an accepted Archaeology policy bundle, evaluator, and decision normalization contract? | `UNKNOWN / HOLD` | Accepted bundle digest, runtime binding, and negative tests |
| `ARCH-NN-007` | Is complete fixture-to-test consumer coverage known under `fixtures/domains/archaeology/`? | `NEEDS VERIFICATION` | Recursive inventory and consumer map |
| `ARCH-NN-008` | Is a deterministic EvidenceRef-to-EvidenceBundle proof producer established for Archaeology? | `HOLD` | Accepted producer, schemas, fixtures, tests, proof, access, and rollback |
| `ARCH-NN-009` | Is an Archaeology release dry-run command and reviewed candidate dossier established? | `HOLD` | Reviewed candidate, fail-closed command, correction, and rollback evidence |
| `ARCH-NN-010` | Which workflow checks are branch-protection-significant? | `NEEDS VERIFICATION` | Current ruleset and required-check evidence |
| `ARCH-NN-011` | Are exact profile case counts and reason-code vocabularies intentionally versioned? | `NEEDS VERIFICATION` | Versioned contract and compatibility policy |
| `ARCH-NN-012` | Has a sensitive-material containment and rollback drill been rehearsed without real protected data? | `UNKNOWN` | Synthetic drill record and authorized review |
| `ARCH-NN-013` | Should `docs/runbooks/archaeology/README.md` become a substantive local boundary index? | `PROPOSED / separate scope` | Directory Rules review and focused documentation change |

[Back to top](#top)

---

## 19. Related surfaces

### Governing doctrine and decisions

- [Directory Rules v2](../../doctrine/directory-rules.md)
- [ADR-0010 — deny by default for DNA, rare species, archaeology, and infrastructure](../../adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md)
- [ADR-0029 — adopt Directory Rules v2](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
- [`docs/runbooks/` operational index](../README.md)

### Archaeology doctrine and policy

- [Archaeology domain README](../../domains/archaeology/README.md)
- [Sensitivity](../../domains/archaeology/SENSITIVITY.md)
- [Cultural review](../../domains/archaeology/CULTURAL_REVIEW.md)
- [Publication and policy](../../domains/archaeology/PUBLICATION_AND_POLICY.md)
- [Domain policy boundary](../../../policy/domains/archaeology/README.md)

### Contracts, schemas, fixtures, validators, and tests

- [Archaeology contract index](../../../contracts/domains/archaeology/README.md)
- [Archaeology schema index](../../../schemas/contracts/v1/domains/archaeology/README.md)
- [Reusable Archaeology fixture index](../../../fixtures/domains/archaeology/README.md)
- [Archaeology domain test index](../../../tests/domains/archaeology/README.md)
- [Archaeology child-validator index](../../../tools/validators/domains/archaeology/README.md)
- [Dedicated Archaeology workflow](../../../.github/workflows/domain-archaeology.yml)
- [Repository Makefile](../../../Makefile)

### Adjacent operational procedures

- [Source refresh](./SOURCE_REFRESH_RUNBOOK.md)
- [Promotion](./PROMOTION_RUNBOOK.md)
- [Rollback](./ROLLBACK_RUNBOOK.md)

[Back to top](#top)

---

## 20. Change log

| Version | Date | Change |
|---|---|---|
| `v0.1` | 2026-05-13 | Proposal-oriented runbook based on an unverified repository state; included illustrative paths, an unverified aggregate command, and future fixture matrices. |
| `v0.2` | 2026-08-23 | Same-path repository-grounded modernization. Records three substantive fixture profiles, one CI-wired profile, placeholder-heavy direct tests, placeholder child validators, exact current commands, bounded no-network evidence, proof/release holds, result semantics, failure diagnosis, containment, rollback, and a run-record template. |

[Back to top](#top)

---

## 21. Glossary

| Term | Meaning in this runbook |
|---|---|
| **Fixture profile** | A bounded schema, synthetic manifest, validator, and test family with declared finite outcomes |
| **No-network marker** | `KFM_NO_NETWORK=1`; a contract signal, not firewall proof by itself |
| **Runner-level egress denial** | An independently enforced network block outside the repository process |
| **Finite outcome** | `PASS`, `ABSTAIN`, `DENY`, or `ERROR` from the current profile validators |
| **Expected negative case** | A fixture whose correct behavior is `ABSTAIN`, `DENY`, or `ERROR` |
| **Placeholder** | A file whose name suggests coverage but whose implementation does not assert the named invariant |
| **Candidate-not-site** | The rule that a detection, anomaly, or proposed feature is not a confirmed archaeological site |
| **Coordinate-free** | No latitude, longitude, coordinates, geometry, or reverse-engineerable location fields in the bounded fixture |
| **Paradata** | Documentation of acquisition, processing, interpretation, representation, and governance context |
| **Evidence closure** | Consequential support resolves through governed evidence objects; not established by fixture validation |
| **Hold** | A deliberate fail-closed work state because required authority or implementation is absent |
| **Publication** | Governed public exposure through released public-safe carriers; never caused by this runbook |

---

**Document state:** `DRAFT / REPOSITORY-GROUNDED / NON-PUBLISHER`

**Validated claim ceiling:** bounded synthetic fixture-profile conformance at an exact tested revision

**Proof, release, deployment, promotion, and publication effect:** none
