<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/atmosphere/no-network-test-runbook
title: Atmosphere — No-Network Test Runbook
type: runbook; operational-procedure; domain-lane; non-authoritative
version: v1.0
prior_version: planning-only v1
status: draft; repository-grounded; bounded-fixture-profiles-executable; broader-validation-proof-release-and-live-source-hold; non-publisher; not-for-life-safety
owners:
  - "@bartytime4life — verified GitHub review route only"
owner_status: "Atmosphere, test, evidence, policy, source-rights, sensitivity, Hazards-seam, review, release, and operations assignments remain NEEDS VERIFICATION; CODEOWNERS routing does not create those authorities."
created: 2026-05-13
updated: 2026-08-24
policy_label: public-review; atmosphere; no-network; synthetic-fixtures; fail-closed; non-release; not-for-life-safety
current_path: docs/runbooks/atmosphere/NO_NETWORK_TEST_RUNBOOK.md
owning_root: docs/
responsibility: >-
  Document the exact bounded Atmosphere no-network procedures currently supported
  by repository fixtures, validators, tests, and read-only workflows, and produce
  a truthful review handoff without granting source, scientific, policy, review,
  release, deployment, or publication authority.
truth_posture: cite-or-abstain
prepared_under_prompt: KFM Repository Build-Out & Markdown Modernization Implementation Agent v6.0.0
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 0c63d45e2a6f132052c8b6d67cae47a373860eae
  target_prior_blob: afb46fd291491cf10d094a09b343c8d98bda8cc0
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adoption_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  parent_runbook_index_blob: 80f53b61d485c25acdb55eaa01129e13e63ca90e
  domain_atmosphere_workflow_blob: fccba4b6e2cdae561ec8a4904446ed5dbe6ec8ce
  validation_runbook_blob: 4ae9d1e8b33ad2ed5df915813f859140602628d1
  atmosphere_tests_readme_blob: 29204b56a1e35ff74ba8a2e33bd8a424175e9dab
  atmosphere_validators_readme_blob: 64680d31a964d4052b4cf444700982a9d3a9e579
inspection_boundary: >-
  Current-session GitHub reads of the target, accepted Directory Rules decision,
  parent index, Atmosphere workflow, test and validator indexes, validation
  runbook, and proof, policy, source-registry, and release boundaries.
  Repository-native commands were not executed in a mounted checkout during
  authoring. No live source was contacted and no executable, lifecycle, release,
  deployment, promotion, publication, alert, health, or regulatory state changed.
related:
  - ../README.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../domains/atmosphere/README.md
  - ./VALIDATION_RUNBOOK.md
  - ./SOURCE_REFRESH_RUNBOOK.md
  - ./CORRECTION_RUNBOOK.md
  - ./ROLLBACK_RUNBOOK.md
  - ./PROMOTION_RUNBOOK.md
  - ../../../fixtures/domains/atmosphere/README.md
  - ../../../policy/domains/atmosphere/README.md
  - ../../../tests/domains/atmosphere/README.md
  - ../../../tools/validators/domains/atmosphere/README.md
  - ../../../release/candidates/atmosphere/README.md
  - ../../../.github/workflows/domain-atmosphere.yml
  - ../../../.github/workflows/atmosphere-airnow-aqs-reconciliation.yml
  - ../../../.github/workflows/correctable-environmental-event-assessment.yml
  - ../../../.github/workflows/pm-sensor-trust-profile.yml
  - ../../../.github/workflows/pm25-sensor-colocation-manifest.yml
  - ../../../.github/workflows/pm25-trigger-candidate-assessment.yml
tags: [kfm, atmosphere, air, weather, climate, runbook, no-network, fixtures, validation, source-role, evidence, fail-closed]
notes:
  - "v1.0 replaces proposal-era, no-mounted-repository assumptions and illustrative nonexistent commands with current repository evidence and exact bounded entry points."
  - "A green no-network run proves only the declared synthetic profile behavior at the tested revision."
  - "Broader Atmosphere validation, evidence closure, proof, policy, release, deployment, and publication remain held."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Atmosphere — No-Network Test Runbook

> **Run and interpret the Atmosphere lane's current deterministic, synthetic checks while keeping live sources, credentials, scientific endorsement, official alerting, internal stores, proof production, promotion, release, deployment, and publication outside the test boundary.**

> [!IMPORTANT]
> **No-network validation is bounded evidence, not Atmosphere truth.** A passing fixture, validator, test, workflow, digest, or generated authoring receipt proves only the claim declared by that exact check at that exact revision. It does not certify a live observation, resolve a production `EvidenceBundle`, activate policy, complete human review, approve a release, deploy a service, or publish a carrier.

> [!WARNING]
> **KFM is not an official AQI, medical, regulatory, emergency-alerting, or life-safety authority.** Do not use this runbook to issue health guidance, certify a concentration, declare an event, replace an agency warning, or infer safety from synthetic output.

> [!CAUTION]
> **Default execution is fixture-only and credential-free.** Do not contact EPA, KDHE, NOAA/NWS, Kansas Mesonet, community-sensor, satellite, model, forecast, or other upstream services merely to make a test feel realistic.

**Quick navigation:** [Purpose](#1-purpose-scope-and-terminal-boundary) · [Authority](#2-authority-placement-and-current-evidence) · [Contract](#3-no-network-contract) · [Profiles](#4-current-executable-profile-inventory) · [Preflight](#5-preflight-and-stop-conditions) · [Core run](#6-core-suite-procedure) · [Specialty](#7-specialty-profile-procedure) · [Outcomes](#8-result-and-ci-interpretation) · [Safety](#9-rights-sensitivity-and-life-safety) · [Failures](#10-failure-diagnosis) · [Handoff](#11-review-handoff) · [Rollback](#12-document-rollback-and-correction) · [Open work](#13-current-holds-and-open-verification) · [Related](#14-related-surfaces) · [History](#15-change-log)

---

## 1. Purpose, scope, and terminal boundary

Use this runbook to execute the Atmosphere lane's current no-network checks at an exact repository revision and report what they do—and do not—establish.

The operator must:

1. freeze the exact revision, changed paths, and applicable profile set;
2. deny live-source access and remove ambient source credentials;
3. use only synthetic, public-safe, repository-controlled fixtures;
4. execute the smallest current profile set covering the change;
5. prove positive acceptance and exact negative rejection where defined;
6. preserve source role, knowledge character, identity, unit, time, lineage, uncertainty, rights, sensitivity, and non-release boundaries;
7. bind hosted status to the exact pull-request head; and
8. stop at a validation handoff.

```text
exact revision
  -> synthetic fixture
  -> validator and tests
  -> PASS / expected ABSTAIN / expected DENY / ERROR polarity
  -> exact-head workflow evidence
  -> human review handoff
  -/> live source admission
  -/> production evidence or policy closure
  -/> promotion, release, deployment, or publication
```

The lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLETS -> PUBLISHED
```

No command in this runbook performs that lifecycle.

### In scope

- core profiles admitted by [`.github/workflows/domain-atmosphere.yml`](../../../.github/workflows/domain-atmosphere.yml);
- focused specialty profiles with dedicated workflows;
- exact valid/invalid fixture polarity;
- active no-network guards declared by accepted tests and validators;
- generated authoring-receipt integrity only where the owning workflow requires it;
- cross-domain ownership-isolation checks;
- exact-head CI evidence and review handoff.

### Out of scope

- live fetch, authentication, source admission, connector activation, or source-rights approval;
- scientific, sensor, correction, model-skill, AQI, health, regulatory, or event certification;
- production `EvidenceBundle`, proof, policy, or reviewer authority;
- canonical `ValidationReport` or `DomainValidationReport` production where no accepted producer exists;
- writes to governed lifecycle, proof, release, or public homes;
- official warning or life-safety issuance;
- promotion, release, deployment, publication, correction, withdrawal, or public rollback.

The maximum result is a **validation handoff**, not a state transition.

[Back to top](#top)

---

## 2. Authority, placement, and current evidence

### Directory Rules result

**`PLACE` — CONFIRMED for this same-path update.** Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts the exact [Directory Rules v2](../../doctrine/directory-rules.md) bytes. This tracked human procedure remains under `docs/runbooks/atmosphere/`; no path, authority root, schema, contract, policy, test, fixture, validator, workflow, receipt, proof, or release object is created or moved.

| Concern | Owning surface | This runbook's relationship |
|---|---|---|
| Atmosphere meaning | `docs/domains/atmosphere/`, `contracts/domains/atmosphere/` | cite, not redefine |
| Machine shape | `schemas/contracts/v1/` | identify tested paths only |
| Fixtures | `fixtures/` | consume synthetic/public-safe inputs |
| Validators and tests | `tools/validators/`, `tests/` | document exact entry points |
| Workflows | `.github/workflows/` | document orchestration; no required-check claim |
| Source admission, rights, evidence, policy | owning registries and governance surfaces | preserve holds |
| Review and release | review and `release/` authorities | prepare handoff only |
| Public delivery | governed APIs and released carriers | outside this runbook |

The parent [runbook index](../README.md) governs navigation. The local `docs/runbooks/atmosphere/README.md` remains a one-byte placeholder at the evidence snapshot, so the local lane README contract is still `HOLD / NEEDS VERIFICATION`; this file does not replace it.

### Current evidence

Pinned to `main@0c63d45e2a6f132052c8b6d67cae47a373860eae`:

- **CONFIRMED:** the prior target contains planning-only paths, fictional aggregate commands, and broad unimplemented fixture claims.
- **CONFIRMED:** `domain-atmosphere.yml` is a read-only Python 3.11 fixture-first entry point for a bounded profile set.
- **CONFIRMED:** several validators/tests are substantive while others remain explicit placeholders; the workflow ratchets that inventory.
- **CONFIRMED:** proof production and Atmosphere release dry-run remain explicit workflow holds.
- **CONFIRMED:** no accepted `atmosphere-validate` or `validate-atmosphere` Make target exists; the workflow treats unexpected appearance as a review trigger.
- **PROPOSED:** future aggregate runner, canonical domain validation report, active policy evaluator, live-source validation, proof producer, and release integration.
- **UNKNOWN:** deployed consumers, production source admission, public releases, operational policy enforcement, and runtime behavior.
- **NEEDS VERIFICATION:** accountable owners, independent review, exact-head hosted results, required-check coupling, source rights, and release authority.

Repository-native commands were not run in a mounted checkout during this documentation update.

[Back to top](#top)

---

## 3. No-network contract

| Requirement | Required posture | Failure result |
|---|---|---|
| Upstream access | No live HTTP, HTTPS, DNS, socket, API, tile, model, or source request from repository code | `DENY` and stop |
| Credentials | No source token, key, cloud credential, or unrelated secret exposed | `DENY` and stop |
| Inputs | Fixed synthetic/public-safe repository fixtures | `DENY` on protected or mutable input |
| Determinism | `TZ=UTC`; `PYTHONHASHSEED=0` where declared; no wall-clock truth inference | `ERROR` or `FAIL` |
| Model providers | No direct local or hosted model invocation | `DENY` |
| Internal stores | No production database, object store, graph, index, canonical store, or public service | `DENY` |
| Lifecycle writes | No write to governed data, proof, release, or public homes | `DENY` or `HOLD` |
| Polarity | Valid fixtures succeed; invalid fixtures fail | `FAIL` on unexpected outcome |
| Network proof | Accepted guard is exercised where the profile declares it | `HOLD` if merely assumed |

Core environment:

```bash
export KFM_NO_NETWORK=1
export PYTHONDONTWRITEBYTECODE=1
export PYTHONHASHSEED=0
export PYTHONUNBUFFERED=1
export TZ=UTC

python tools/ci/install_python_ci.py project-test
```

PM sensor trust and PM2.5 colocation use `project-runtime`. Dependency installation may require network access before the governed test phase; separate installation from repository-code execution and expose no source credentials.

A folder name, missing key, green workflow, or documentation statement does not prove no-network behavior by itself.

[Back to top](#top)

---

## 4. Current executable profile inventory

### Core domain workflow

| Profile | Executable surface | Bounded claim |
|---|---|---|
| Public-safe precipitation | `validate_public_safe_precipitation_fixture.py`; `test_atmosphere_smoke.py` | Synthetic observed-sensor character, generalized support, time, millimetre units, accumulation bounds, and alert denial |
| Knowledge character | `validate_knowledge_character.py`; `test_knowledge_character_registry.py` | Six synthetic character pairings and exact anti-collapse denials |
| Low-cost sensor caveats | `validate_low_cost_sensor_caveats.py`; `test_low_cost_sensor_caveat_required.py` | Synthetic caveat, confidence, limitations, correction lineage, collocation/evaluation, transferability, and drift posture |
| Observed versus modeled | `validate_observed_modeled_separation.py`; `test_observed_modeled_separation.py` | Closed observation/forecast distinction, identity, time, units, lineage, uncertainty, abstention, denial, and false-release rejection |
| Cross-domain boundary | `test_environmental_observation_boundaries.py` | Soil/Atmosphere/Hydrology ownership isolation |
| AirNow-to-AQS reconciliation | dedicated validator/tests | Synthetic monitor key, provisional/regulatory role, QA/certification, deterministic reconciliation, and finite outcomes |
| Prescribed-burn quality flag | dedicated validator/test | Measurement remains observation; burn/smoke remains context; no causal attribution |
| PM2.5 trigger candidate | dedicated validator/test | Synthetic categorical candidate/hold assessment; no threshold, AQI, health, detector, policy, or release action |
| Correctable environmental event | dedicated validator/test, executed by dedicated workflow | Synthetic lifecycle/reference coherence only |

### Dedicated workflows

| Profile | Workflow |
|---|---|
| PM sensor trust | [`pm-sensor-trust-profile.yml`](../../../.github/workflows/pm-sensor-trust-profile.yml) |
| PM2.5 colocation manifest | [`pm25-sensor-colocation-manifest.yml`](../../../.github/workflows/pm25-sensor-colocation-manifest.yml) |
| AirNow-to-AQS reconciliation | [`atmosphere-airnow-aqs-reconciliation.yml`](../../../.github/workflows/atmosphere-airnow-aqs-reconciliation.yml) |
| PM2.5 trigger candidate | [`pm25-trigger-candidate-assessment.yml`](../../../.github/workflows/pm25-trigger-candidate-assessment.yml) |
| Correctable environmental event | [`correctable-environmental-event-assessment.yml`](../../../.github/workflows/correctable-environmental-event-assessment.yml) |

None fetches a live source, proves scientific validity, activates policy, authenticates review, mutates a detector, declares a real event, or releases/publishes state.

### Explicit held surfaces

- Other Atmosphere files remain placeholders or documentation-only lanes.
- The workflow rejects unwired substantive files and accepted-profile regressions to placeholders.
- Generic/domain validation-report machine profiles remain incomplete or permissive; no accepted release-grade producer exists.
- Atmosphere policy remains unbound for these procedures.
- `data/proofs/atmosphere/pm25_2026/evidence_bundle.json` is an inventoried `PROPOSED` placeholder, not proof.
- `release/candidates/atmosphere/` has no accepted candidate record at the snapshot.
- Proof and release-dry-run jobs emit explicit `HOLD`.
- No executable live Atmosphere connector or live-source validation entry point was verified.

[Back to top](#top)

---

## 5. Preflight and stop conditions

Before running:

- [ ] Record full base and candidate head SHAs.
- [ ] List changed paths and map them to profiles.
- [ ] Check open overlap; use `HOLD` if unresolved.
- [ ] Use one exact revision for code and fixtures.
- [ ] Match the owning workflow's Python/dependency profile.
- [ ] Set no-network variables and remove source credentials.
- [ ] Confirm fixtures are synthetic and public-safe.
- [ ] Identify valid/invalid polarity.
- [ ] Keep output outside canonical truth/release homes unless an accepted producer owns it.

Stop immediately when:

- repository code contacts a live source or requests a credential;
- a fixture contains protected, private, rights-restricted, or harmful-precision detail;
- a known-invalid fixture is accepted;
- a valid fixture is rejected without an understood profile change;
- zero tests are collected or a validator becomes a no-op;
- placeholder/substantive inventory changes without deliberate wiring;
- an aggregate command is invented;
- a passing result is described as evidence, policy, review, proof, release, or publication closure;
- KFM is presented as an AQI, medical, regulatory, emergency, or life-safety authority;
- the proposed fix weakens negative fixtures, network guards, or authority boundaries.

[Back to top](#top)

---

## 6. Core suite procedure

### 6.1 Install and run core tests

```bash
export KFM_NO_NETWORK=1
export PYTHONDONTWRITEBYTECODE=1
export PYTHONHASHSEED=0
export PYTHONUNBUFFERED=1
export TZ=UTC

python tools/ci/install_python_ci.py project-test

python tests/domains/atmosphere/test_atmosphere_smoke.py --verbose
python tests/domains/atmosphere/test_knowledge_character_registry.py --verbose
python tests/domains/atmosphere/test_low_cost_sensor_caveat_required.py --verbose
python tests/domains/atmosphere/test_observed_modeled_separation.py --verbose
python tests/cross_domain/test_environmental_observation_boundaries.py --verbose

python -m pytest \
  tests/validators/domains/atmosphere/airnow_aqs_reconciliation/test_validate_reconciliation.py \
  tests/domains/atmosphere/test_prescribed_burn_quality_flag.py \
  tests/domains/atmosphere/test_pm25_trigger_candidate_assessment.py \
  -q --strict-config --strict-markers
```

Record collection counts and exit codes. Zero collected tests is `FAIL`.

### 6.2 Replay exact fixture polarity

```bash
python tools/validators/domains/atmosphere/validate_public_safe_precipitation_fixture.py \
  fixtures/domains/atmosphere/public_safe_precipitation/valid/public_safe_precipitation.json

if python tools/validators/domains/atmosphere/validate_public_safe_precipitation_fixture.py \
  fixtures/domains/atmosphere/public_safe_precipitation/invalid/role_location_time_governance_collapse.json
then
  echo "Known-invalid precipitation fixture was accepted" >&2
  exit 1
fi

python tools/validators/domains/atmosphere/validate_knowledge_character.py \
  fixtures/domains/atmosphere/knowledge_character/valid/*.json

if python tools/validators/domains/atmosphere/validate_knowledge_character.py \
  fixtures/domains/atmosphere/knowledge_character/invalid/*.json
then
  echo "Known-invalid knowledge-character fixtures were accepted" >&2
  exit 1
fi

python tools/validators/domains/atmosphere/validate_low_cost_sensor_caveats.py \
  fixtures/domains/atmosphere/low_cost_sensor_calibration/valid/*.json

if python tools/validators/domains/atmosphere/validate_low_cost_sensor_caveats.py \
  fixtures/domains/atmosphere/low_cost_sensor_calibration/invalid/*.json
then
  echo "Known-invalid low-cost-sensor fixtures were accepted" >&2
  exit 1
fi

python tools/validators/domains/atmosphere/validate_observed_modeled_separation.py \
  fixtures/domains/atmosphere/observed_modeled_separation/valid/air_observation_bound.json \
  fixtures/domains/atmosphere/observed_modeled_separation/valid/forecast_context_bound.json \
  fixtures/domains/atmosphere/observed_modeled_separation/valid/air_observation_unresolved.json

if python tools/validators/domains/atmosphere/validate_observed_modeled_separation.py \
  fixtures/domains/atmosphere/observed_modeled_separation/invalid/air_observation_model_run_ref.json \
  fixtures/domains/atmosphere/observed_modeled_separation/invalid/forecast_context_missing_lineage.json
then
  echo "Known-invalid observed-versus-modeled fixtures were accepted" >&2
  exit 1
fi
```

### 6.3 Preserve the broader hold

Even when every command passes, record:

```text
WORKFLOW_HOLD:
broader Atmosphere semantics, live evidence resolution, policy evaluation,
proof production, accountable review, release dry-run, deployment, and
publication remain unestablished.
```

Do not invent `make atmosphere-validate` or `make validate-atmosphere`; no accepted target exists at the snapshot.

[Back to top](#top)

---

## 7. Specialty profile procedure

Use the exact commands in the owning workflow and the [Atmosphere Validation Runbook](./VALIDATION_RUNBOOK.md). Current command families are:

| Profile | Dependency profile | Test/validator | Receipt check |
|---|---|---|---|
| PM sensor trust | `project-runtime` | unittest `test_pm_sensor_trust_profile.py`; `validate_pm_sensor_trust_profile.py --fixtures` | `genrec-pass30-pm-sensor-trust-profile-20260809.json` |
| PM2.5 colocation | `project-runtime` | unittest `test_pm25_sensor_colocation_manifest.py`; `validate_pm25_sensor_colocation_manifest.py --fixtures` | `genrec-pass30-pm25-sensor-colocation-manifest-20260809.json` |
| AirNow-to-AQS | `project-test` | focused reconciliation pytest | `genrec-atmosphere-airnow-aqs-reconciliation-20260806.json` |
| PM2.5 trigger | `project-test` | `test_pm25_trigger_candidate_assessment.py` | `genrec-pass32-pm25-trigger-candidate-20260810.json` |
| Correctable event | `project-test` | `test_correctable_environmental_event_assessment.py` | `genrec-correctable-environmental-event-assessment-20260810.json` |
| Prescribed burn | `project-test` | `test_prescribed_burn_quality_flag.py` | none declared by core procedure |

A generated authoring receipt proves only its declared source/output binding and integrity. It is not a runtime validation result, `ValidationReport`, `EvidenceBundle`, `PolicyDecision`, `ReviewRecord`, or release receipt. Do not invent one where the owning workflow does not require it.

[Back to top](#top)

---

## 8. Result and CI interpretation

### Result labels

| Label | Meaning |
|---|---|
| `PASS` | Named check passed at the exact revision |
| `FAIL` | Named check failed |
| `EXPECTED_REJECTION` | Known-invalid input returned the intended non-success result |
| `UNEXPECTED_ACCEPTANCE` | Known-invalid input passed; fail the run |
| `UNEXPECTED_REJECTION` | Declared valid input failed; fail or deliberately revise the profile |
| `ERROR` | Check could not execute or infrastructure failed |
| `NOT_RUN` | No execution occurred |
| `PENDING` | Hosted check has not settled |
| `SKIPPED` | Intentional non-execution; reason required |
| `NOT_APPLICABLE` | Outside changed-area contract |
| `HOLD` | Required authority, implementation, evidence, review, or release closure is missing |

`ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` are candidate/runtime outcomes, not test-runner states. A test can pass because a subject correctly abstained or denied.

### Exact-head CI rule

For each hosted result record:

```yaml
head_sha: <full SHA>
workflow: <workflow name>
run_id: <run id>
status: <queued | in_progress | completed>
conclusion: <success | failure | cancelled | skipped | null>
observed_at: <UTC timestamp>
```

Classify failures as `INTRODUCED`, `INHERITED`, `UNRESOLVED`, `EXPECTED_HOLD`, `INFRASTRUCTURE`, or `PENDING`. Do not call a failure inherited merely because the pull request is documentation-only; compare the exact base/head or equivalent evidence.

A green workflow does not prove required-check significance, independent review, source admission, evidence/proof closure, active policy, release, deployment, or public-state parity.

[Back to top](#top)

---

## 9. Rights, sensitivity, and life-safety

Fixtures and logs must not contain live credentials, private-person detail, precise protected infrastructure, archaeology, rare-species or private-land locations, proprietary records, or rights-restricted source material. Use synthetic identifiers, bounded values, and generalized support. Style hiding is not a security control.

Preserve these distinctions:

1. AQI/report context is not measured concentration.
2. AOD or a remote-sensing proxy is not ground-level PM2.5.
3. Model/forecast output is not an observation.
4. Provisional reporting is not a certified regulatory archive.
5. Low-cost output is not reference-grade by default.
6. Candidate detection is not a real-world event.
7. Smoke/burn context is not causal attribution.
8. Advisory context is not KFM-issued instruction.
9. Climate anomaly requires a declared baseline.

Treat live access, secret exposure, protected fixture content, public-path mutation, life-safety language, or unexpected proof/release/lifecycle writes as stop-and-escalate incidents.

[Back to top](#top)

---

## 10. Failure diagnosis

| Symptom | Required response |
|---|---|
| Invalid fixture accepted | `FAIL`; isolate validator/fixture drift; do not weaken fixture |
| Valid fixture rejected | `FAIL` or `HOLD`; inspect contract/schema/migration intent |
| Zero tests collected | `FAIL` |
| Network call attempted | `DENY`; stop and inspect stack/credentials |
| Identical replay differs | `FAIL`; isolate nondeterminism |
| Placeholder becomes substantive | `HOLD`; deliberately admit with contract, tests, and workflow wiring |
| Accepted profile becomes placeholder | `FAIL`; restore or retire through reviewed change |
| Generated receipt fails | `FAIL`; do not rewrite blindly |
| Proof job is green/held | Preserve `HOLD`; it is readiness evidence, not proof |
| Release dry-run job is green/held | Preserve `HOLD`; it is not release readiness |
| Docs-only PR fails unrelated workflow | Compare exact base/head; keep `UNRESOLVED` until proved |
| Output implies AQI/health/emergency authority | `DENY`; correct the authority collapse |
| Policy execution is requested | `HOLD`; current policy integration is not established |

Route schema/contract defects to owning reviewers; source/rights issues to admission and rights authorities; evidence gaps to the resolver/proof lane; life-safety matters to Hazards and official issuers; release/public-state matters to release, correction, withdrawal, and rollback authorities.

[Back to top](#top)

---

## 11. Review handoff

Record at minimum:

```yaml
record_type: atmosphere_no_network_validation_handoff
repository: bartytime4life/Kansas-Frontier-Matrix
base_commit: <full SHA>
candidate_head: <full SHA>
executed_at: <UTC timestamp>
changed_paths: [<path>]
profiles:
  - id: <profile>
    command: <exact command>
    dependency_profile: <project-test | project-runtime>
    fixtures: [<paths and digests when practical>]
    test_result: <PASS | FAIL | ERROR | NOT_RUN>
    negative_polarity: <EXPECTED_REJECTION | UNEXPECTED_ACCEPTANCE | n/a>
    network_guard: <exercised | not-exercised | unknown>
    limitations: [<bounded limitation>]
hosted_checks:
  - workflow: <name>
    run_id: <id>
    head_sha: <full SHA>
    status: <status>
    conclusion: <conclusion>
findings:
  introduced: []
  inherited: []
  unresolved: []
  expected_holds:
    - live-source validation
    - production evidence and policy closure
    - proof and release integration
evidence_state: bounded-fixture-only
policy_state: unbound
review_state: pending
release_state: held
publication_state: unchanged
rollback: <branch close, revert, or follow-up correction>
```

Do not label this handoff a canonical `DomainValidationReport`.

[Back to top](#top)

---

## 12. Document rollback and correction

This update changes documentation only.

1. Before merge, close the pull request or revert the feature-branch commit.
2. After merge, create a normal revert commit restoring the prior target blob.
3. Rerun Markdown, link, metadata, stale-scan, and changed-area checks.
4. Do not force-push shared history or edit `main` directly.
5. A Markdown revert does not roll back public state.

When a command, profile, workflow, or hold changes, pin the exact revision, inspect owning executable surfaces, update this runbook and [VALIDATION_RUNBOOK.md](./VALIDATION_RUNBOOK.md) only where their responsibilities require it, and keep validation, review, merge, release, deployment, promotion, and publication separate.

[Back to top](#top)

---

## 13. Current holds and open verification

| Item | State | Needed closure |
|---|---|---|
| Accountable owners and independent review | `NEEDS VERIFICATION` | Accepted assignments |
| Local Atmosphere runbook README | `HOLD` | Substantive lane boundary without executable-authority drift |
| Aggregate no-network runner | `PROPOSED` | Accepted command, tests, workflow wiring, and migration from exact commands |
| Domain validation report producer | `HOLD` | Closed semantics/schema, deterministic producer, validator, fixtures, receipts, and consumers |
| Atmosphere policy evaluator | `HOLD` | Accepted rules, negative tests, evaluator binding, versioning, and review |
| Live-source validation | `UNKNOWN / HOLD` | Admitted sources, rights, cadence, endpoint contracts, credentials, and isolated profile |
| Proof producer | `HOLD` | Real EvidenceRef-to-EvidenceBundle resolution, producer, access controls, and review |
| Release dry-run | `HOLD` | Candidate contract, artifacts, rights, time, evidence, policy, review, correction, and rollback |
| Required-check/ruleset significance | `NEEDS VERIFICATION` | Hosted branch/ruleset evidence |
| Deployment/public behavior | `UNKNOWN` | Runtime, release, deployment, carrier, cache, and public evidence |

The smallest safe next improvement is one clearly owned, dependency-closed gap—not an invented broad command.

[Back to top](#top)

---

## 14. Related surfaces

- [Parent runbook index](../README.md)
- [Atmosphere Validation Runbook](./VALIDATION_RUNBOOK.md)
- [Atmosphere Source Refresh Runbook](./SOURCE_REFRESH_RUNBOOK.md)
- [Atmosphere Correction Runbook](./CORRECTION_RUNBOOK.md)
- [Atmosphere Rollback Runbook](./ROLLBACK_RUNBOOK.md)
- [Atmosphere Promotion Runbook](./PROMOTION_RUNBOOK.md)
- [Accepted Directory Rules ADR](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
- [Atmosphere domain README](../../domains/atmosphere/README.md)
- [Atmosphere fixtures](../../../fixtures/domains/atmosphere/README.md)
- [Atmosphere tests](../../../tests/domains/atmosphere/README.md)
- [Atmosphere validators](../../../tools/validators/domains/atmosphere/README.md)
- [Atmosphere policy](../../../policy/domains/atmosphere/README.md)
- [Atmosphere release candidates](../../../release/candidates/atmosphere/README.md)
- [Core Atmosphere workflow](../../../.github/workflows/domain-atmosphere.yml)

[Back to top](#top)

---

## 15. Change log

| Version | Date | Change | Effect |
|---|---|---|---|
| `v1.0` | 2026-08-24 | Replaced planning-only paths, fictional commands, broad unimplemented claims, and no-repository assumptions with current profile inventory, exact commands, workflow holds, result labels, safety boundaries, and review/rollback procedure | Documentation only; no executable, lifecycle, release, deployment, or publication effect |
| `v1` | 2026-05-13 | Initial planning-era no-network runbook | Lineage only; implementation claims were largely proposed |

[Back to top](#top)
