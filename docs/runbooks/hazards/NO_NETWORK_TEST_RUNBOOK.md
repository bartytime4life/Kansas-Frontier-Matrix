<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook-hazards-no-network-test
title: Hazards No-Network Test Runbook
type: operational-runbook
version: v2.0.0
status: DRAFT_REPOSITORY_GROUNDED; BOUNDED_SYNTHETIC_VALIDATION_ONLY; PROOF_AND_RELEASE_HELD; NON_RELEASE; NON_PUBLICATION
owners: "@bartytime4life — verified CODEOWNERS route; accountable Hazards, validation, safety, policy, and release stewardship NEEDS VERIFICATION"
created: 2026-05-12
updated: 2026-08-27
policy_label: repository-facing; hazards; no-network; synthetic-only; fail-closed; not-for-life-safety; non-publisher
owning_root: docs/
path_authority: same-path modernization under accepted ADR-0029 and Directory Rules v2
authority_effect: none
source_activation_effect: none
release_effect: none
deployment_effect: none
promotion_effect: none
publication_effect: none
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 7da7e26240859ba0d3c7bd9f992a4590e8146cf2
  target_path: docs/runbooks/hazards/NO_NETWORK_TEST_RUNBOOK.md
  target_prior_blob: 3a8e6afaa888b7611e91c7319d76c4d31d77f2a3
  workflow_blob: 9d48f97ff33fedd4f2acf3a6aed2b6753d0caaea
  smoke_test_blob: af8550b8e22c7022e30cc11e5c77a951898cf1f0
  materiality_test_blob: dc71faa0667b8817abe070a7fef08361c9ddc743
  materiality_validator_blob: dac5f56560f40e725c4d8924d8d20138ae5708fd
  dependency_installer_blob: a403f366b5a51767456730d05060b105dca3d3f8
  open_pull_requests_touching_target: 0
source_lineage:
  - title: kfm_hazards_extended_pro_pdf_only_blueprint.pdf
    source_class: PLANNING_LINEAGE
    use: not-for-life-safety, source-role, time, cite-or-abstain, and offline-first design context only
  - title: KFM Markdown Update & Modernization Agent v1.0
    source_class: CURRENT_TASK_GUIDANCE
    use: same-path repository-grounded documentation modernization and draft-PR delivery method
related:
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../doctrine/directory-rules.md
  - ../README.md
  - ../../domains/hazards/README.md
  - ../../domains/hazards/LIFE_SAFETY_BOUNDARY.md
  - ../../domains/hazards/PUBLICATION_AND_BOUNDARY.md
  - NOT_FOR_LIFE_SAFETY_AUDIT_RUNBOOK.md
  - PROMOTION_RUNBOOK.md
  - ROLLBACK_DRILL.md
  - ../../../.github/workflows/domain-hazards.yml
  - ../../../Makefile
  - ../../../tests/domains/hazards/test_hazards_smoke.py
  - ../../../tests/domains/hazards/test_validate_usdm_materiality.py
  - ../../../tools/validators/domains/hazards/validate_usdm_materiality.py
  - ../../../tools/ci/install_python_ci.py
  - ../../../fixtures/domains/hazards/usdm_materiality/cases.json
notes:
  - The current executable lane proves bounded drought-family schema and fixture polarity plus deterministic USDM materiality semantics; it does not prove the complete Hazards trust spine.
  - KFM_NO_NETWORK and in-process socket/URL guards constrain the validation profile, but the hash-locked dependency bootstrap is not an operating-system air-gap proof.
  - The workflow's proof and release jobs are explicit readiness holds. A green held job is not proof, review, release, promotion, deployment, or publication evidence.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hazards No-Network Test Runbook

> **One-line purpose.** Run KFM's current bounded Hazards validation against committed synthetic drought fixtures without contacting live hazard sources, then record exactly what passed, what remained held, and why the result creates no life-safety, source-admission, proof, release, or publication authority.

[![Status: bounded synthetic validation](https://img.shields.io/badge/status-bounded%20synthetic%20validation-8250df?style=flat-square)](#current-disposition)
[![Network: live sources forbidden](https://img.shields.io/badge/live%20sources-forbidden-b42318?style=flat-square)](#what-no-network-means)
[![Life safety: no](https://img.shields.io/badge/life%20safety-not%20an%20alerting%20system-b42318?style=flat-square)](#not-for-life-safety-boundary)
[![Proof and release: held](https://img.shields.io/badge/proof%20%2F%20release-held-6e7781?style=flat-square)](#explicit-holds-and-unproved-behavior)
[![Public effect: none](https://img.shields.io/badge/public%20effect-none-6e7781?style=flat-square)](#authority-and-terminal-boundary)

<a id="not-for-life-safety-boundary"></a>

> [!CAUTION]
> **KFM Hazards is not an emergency-alerting system, incident-command system, regulatory authority, or substitute for official instructions.** This procedure does not retrieve or validate current conditions and must not be used to issue, replace, delay, retract, summarize as actionable, or interpret a warning, evacuation order, shelter instruction, medical direction, all-clear, or other life-safety message. Direct urgent needs to the appropriate official authority.

<a id="current-disposition"></a>

> [!IMPORTANT]
> **Current disposition: `BOUNDED_SYNTHETIC_VALIDATION / PROOF_AND_RELEASE_HOLD`.** At the pinned repository snapshot, the implemented lane validates three drought-family JSON Schemas and their exact fixture polarity, exercises an in-process network-denial guard, and validates deterministic U.S. Drought Monitor materiality cases. EvidenceBundle resolution, active policy evaluation, Hazards proof production, candidate assembly, release dry-run execution, deployment, and publication are not established by this lane.

**Quick navigation:** [Goal](#goal-and-scope) · [Authority](#authority-and-terminal-boundary) · [Current evidence](#current-repository-evidence) · [No-network meaning](#what-no-network-means) · [Preconditions](#preconditions) · [Run](#run-the-focused-validation) · [Interpretation](#interpret-the-results) · [Coverage](#covered-behavior) · [Holds](#explicit-holds-and-unproved-behavior) · [Failures](#failure-handling) · [Hermetic mode](#stronger-hermetic-execution) · [Handoff](#pull-request-and-review-handoff) · [Rollback](#rollback-path) · [Maintenance](#maintenance-and-verification-backlog)

---

<a id="goal-and-scope"></a>

## Goal and scope

Use this runbook when a change touches the current Hazards drought-family schemas, fixtures, materiality validator, focused tests, workflow boundary, or documentation that describes them. The procedure gives a developer or reviewer a reproducible, repository-owned changed-area check while live source admission and public release remain out of scope.

The current executable circle is:

```text
committed synthetic drought fixtures
  -> JSON Schema 2020-12 validation and exact fixture polarity
  -> in-process network-denial checks
  -> deterministic USDM snapshot comparison
  -> finite materiality classification
  -> bounded validation result and review handoff
```

### In scope

- the three committed drought object families:
  - `drought_observation`;
  - `drought_declaration`; and
  - `drought_obs_decl_relationship`;
- their valid and invalid synthetic fixture sets;
- duplicate-key, regular-file, symlink, UTF-8, and fixture-size protections implemented by the smoke test;
- the `kfm-usdm-materiality-v1` fixture profile;
- deterministic materiality, non-event, and hold semantics;
- the repository's current Hazards workflow and exact focused commands; and
- documentation/link validation for this runbook when it changes.

### Out of scope

- NOAA, NWS, FEMA, USGS, NASA, state, local, or other live source access;
- current conditions, warning validity, emergency guidance, or operational source freshness;
- source admission, credentials, rights acceptance, or connector activation;
- hazard families other than the exact drought fixtures and USDM comparison profile named here;
- EvidenceRef-to-EvidenceBundle resolution, active policy evaluation, ProofPack construction, candidate assembly, release, deployment, promotion, or publication;
- production network isolation, firewall enforcement, or air-gap certification; and
- writes to RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, proof, receipt, release, or PUBLISHED stores.

[Back to top](#top)

---

<a id="authority-and-terminal-boundary"></a>

## Authority and terminal boundary

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) and the adopted [Directory Rules v2](../../doctrine/directory-rules.md) place human operational procedures under `docs/runbooks/`, executable validation under `tools/` and `tests/`, machine shape under `schemas/`, policy under `policy/`, lifecycle objects under governed `data/` lanes, and release decisions under `release/`.

This is a same-path modernization of an established file. It creates no new responsibility root or parallel contract, schema, policy, evidence, receipt, proof, release, or publication home.

| Responsibility | Owning surface | This runbook's role |
|---|---|---|
| Human procedure | `docs/runbooks/hazards/NO_NETWORK_TEST_RUNBOOK.md` | Explain the bounded commands, outcomes, limits, and handoff |
| Drought object meaning | `contracts/domains/hazards/` | Link and consume; do not redefine |
| Machine validation shape | `schemas/contracts/v1/domains/hazards/` | Validate current schemas; do not treat shape as truth |
| Synthetic examples | `fixtures/domains/hazards/` | Exercise reviewed fixtures; do not substitute them for source evidence |
| Executable behavior | `tests/domains/hazards/` and `tools/validators/domains/hazards/` | Provide the actual bounded proof of behavior |
| CI orchestration | `.github/workflows/domain-hazards.yml` | Run the same bounded profile and preserve explicit holds |
| Policy, evidence, proof, and release | Their existing responsibility roots | Remain outside this procedure unless separately implemented and governed |

The highest result this runbook can establish is:

```text
BOUNDED_SYNTHETIC_VALIDATION_PASS
```

That result is not `SOURCE_ADMITTED`, `EVIDENCE_RESOLVED`, `POLICY_APPROVED`, `REVIEWED`, `PROOF_COMPLETE`, `RELEASED`, `DEPLOYED`, `PROMOTED`, or `PUBLISHED`.

[Back to top](#top)

---

<a id="current-repository-evidence"></a>

## Current repository evidence

The observations below are pinned to `main@7da7e26240859ba0d3c7bd9f992a4590e8146cf2`. Re-read the exact files when the base, workflow, Makefile, schemas, fixtures, validator, or tests move.

| Surface | CONFIRMED repository evidence | Bounded conclusion |
|---|---|---|
| Focused smoke test | `tests/domains/hazards/test_hazards_smoke.py` validates three JSON Schema 2020-12 families, exact valid/invalid fixture inventories, and selected file-safety properties | Proves only the committed drought-family profile at the tested SHA |
| Network guard | The smoke test patches socket connection, DNS resolution, and `urllib.request.urlopen` entry points to fail closed and verifies representative calls are denied | Proves the named Python process guard; not operating-system egress isolation |
| Materiality tests | `tests/domains/hazards/test_validate_usdm_materiality.py` covers four valid semantic states, deterministic criteria, exact invalid findings, and rejection of legal-declaration fields in an observation snapshot | Proves the named USDM comparison semantics, not current drought truth |
| Materiality validator | `tools/validators/domains/hazards/validate_usdm_materiality.py` requires fixture-only/no-network declarations, validates deterministic inputs, and rejects any candidate that claims authority, source activation, promotion, release, or publication | Produces a comparison result, not a governance decision |
| Make target | `make hazards-validate` runs the USDM materiality unit module and the exact fixture validator with deterministic environment variables | This is the current repository-owned entry point for the materiality profile |
| Domain workflow | `.github/workflows/domain-hazards.yml` runs the smoke test and `make hazards-validate` using read-only repository permission, pinned actions, and `persist-credentials: false` | Hosted orchestration is bounded and non-publishing |
| Dependency bootstrap | The workflow invokes `python tools/ci/install_python_ci.py project-runtime`, which installs exact hash-locked dependencies and the local package | Dependency integrity is bounded; package acquisition may still require an approved cache or network |
| Hazards proof job | `build-proof-hazards` explicitly emits a hold when no accepted producer or deterministic proof command exists | A green held job is readiness-boundary evidence, not a proof |
| Hazards release dry-run job | `publish-dry-run-hazards` explicitly emits a hold when no accepted candidate contract or command exists | A green held job is not release readiness or a release decision |

The April Hazards blueprint remains useful planning lineage for the not-for-life-safety, source-role, time, evidence, and offline-first posture. Its old no-repository assumptions and proposed command paths do not override current repository evidence.

[Back to top](#top)

---

<a id="what-no-network-means"></a>

## What no-network means

The phrase **no-network** has three different possible meanings. Keep them separate.

| Layer | Current status | What may be claimed |
|---|---|---|
| Live hazard sources | **CONFIRMED forbidden by the focused profile** | The implemented tests and validator consume committed fixtures and do not need a live hazard endpoint |
| Python validation process | **CONFIRMED bounded guard** | The smoke test fails selected socket, DNS, and `urllib` access paths closed |
| Runner or operating system | **NEEDS VERIFICATION** | `KFM_NO_NETWORK=1` is an application contract, not proof of firewall, namespace, proxy, DNS, or host-level egress denial |
| Dependency bootstrap | **SEPARATE PRECONDITION** | The hash-locked installer may obtain packages before the focused run; that acquisition is not part of the fixture validation claim |

> [!WARNING]
> Do not call a run hermetic, air-gapped, or infrastructure-level no-egress unless the execution environment independently enforces that property and the handoff records the mechanism. Do not disable or bypass the in-process guard to make a test pass.

[Back to top](#top)

---

<a id="preconditions"></a>

## Preconditions

1. Work from a clean checkout or isolated worktree at a recorded 40-character commit SHA.
2. Run from the repository root.
3. Use Python 3.11 for hosted-workflow parity unless the repository changes that pin.
4. Ensure the committed Hazards schemas, fixtures, tests, validator, workflow, and Makefile are present at the same revision.
5. Keep live-source credentials out of the environment and do not supply source URLs, API keys, tokens, or production data to the focused commands.
6. Install dependencies through the repository-owned hash-locked profile when the environment does not already provide them.

Dependency bootstrap:

```bash
python tools/ci/install_python_ci.py project-runtime
```

> [!NOTE]
> Run dependency installation before applying external network containment, or use an approved pre-populated cache or wheelhouse. Record bootstrap separately from the no-live-source validation. A successful install is supply-chain/bootstrap evidence, not Hazards validation evidence.

Record before running:

```bash
git rev-parse HEAD
git status --short
python --version
```

A dirty working tree is not automatically invalid, but the handoff must identify the exact changed paths and must not attribute unrelated changes to this run.

[Back to top](#top)

---

<a id="run-the-focused-validation"></a>

## Run the focused validation

Set the deterministic environment used by the repository and execute the two current entry points:

```bash
export KFM_NO_NETWORK=1
export PYTHONHASHSEED=0
export PYTHONDONTWRITEBYTECODE=1
export PYTHONUNBUFFERED=1
export TZ=UTC

python -m unittest -v tests.domains.hazards.test_hazards_smoke
make hazards-validate
```

For a documentation change to this file, also run the bounded local link checker:

```bash
python tools/validators/docs/link-check/check_links.py \
  --repo-root . \
  --format text \
  docs/runbooks/hazards/NO_NETWORK_TEST_RUNBOOK.md
```

Review the complete diff:

```bash
git diff --check
git diff -- docs/runbooks/hazards/NO_NETWORK_TEST_RUNBOOK.md
```

### Hosted workflow parity

On pull requests, the `domain-hazards` workflow currently performs these relevant steps:

1. checks out with persisted credentials disabled;
2. installs the `project-runtime` dependency profile;
3. verifies required Hazards boundary paths;
4. runs the smoke test;
5. runs `make hazards-validate`; and
6. records the bounded scope and remaining holds in the job summary.

The local commands above are the focused changed-area check. Hosted results remain bound to the exact workflow run and tested commit identity.

[Back to top](#top)

---

<a id="interpret-the-results"></a>

## Interpret the results

### Procedure result

| Result | Meaning | Required action |
|---|---|---|
| `BOUNDED_SYNTHETIC_VALIDATION_PASS` | Both focused commands exit `0` at the recorded SHA and no unexpected network access occurs | Record the exact scope and limitations; continue to review only |
| `FAIL` | A valid fixture, invalid fixture, schema, expected finding, materiality state, or guard does not match the committed profile | Stop; repair the cause without weakening a required negative case |
| `ERROR` | Dependencies, input files, encoding, repository state, or runner setup prevent a trustworthy run | Stop; repair the environment or classify the result as not established |
| `HOLD` | Required authority or a later lane is absent, or the run attempts to exceed fixture-only scope | Keep proof, release, promotion, deployment, and publication unchanged |

### USDM materiality semantics

The validator's semantic result is separate from command success and governance state.

| Computed state | Computed outcome | Meaning in this profile |
|---|---|---|
| `UNCHANGED` | `NON_EVENT` | No modeled metric or geometry change was detected in the synthetic comparison |
| `SEMANTIC_NON_MATERIAL` | `NON_EVENT` | A change exists but does not meet the committed materiality criteria |
| `MATERIAL` | `PROMOTION_CANDIDATE` | The synthetic comparison meets a materiality criterion and may be considered by a later governed process |
| `UNDETERMINED` | `HOLD` | Geometry changed without supporting metric change; do not infer materiality |

> [!IMPORTANT]
> `PROMOTION_CANDIDATE` is a materiality-classification output. It does not authorize promotion, create a candidate record, satisfy evidence or policy, approve release, or change lifecycle state.

The validator also prints `PASS` or `FAIL` for each fixture validation result. That process-level result must not be confused with an outward `PolicyDecision`, a review decision, a proof, or a release decision.

[Back to top](#top)

---

<a id="covered-behavior"></a>

## Covered behavior

A passing focused run supports only these claims at the tested revision:

- the three named drought schemas are valid JSON Schema 2020-12 documents;
- the expected valid fixture inventory passes and the expected invalid inventory fails with exact findings;
- committed fixture inputs are bounded, UTF-8 JSON regular files and duplicate object keys are rejected by the smoke-test loader;
- valid fixture metadata declares `no_network_required` and `sensitive_data: false`;
- representative Python socket, DNS, and `urllib` network entry points fail closed inside the smoke test;
- USDM synthetic comparisons preserve snapshot time order, digest form, area hierarchy, threshold shape, and deterministic assessment;
- observation snapshots cannot carry undeclared legal or administrative stage fields;
- fixture candidates cannot claim authority creation, source activation, promotion authorization, release authorization, or publication authorization; and
- the exact negative cases retain their expected reason codes.

Maps, dashboards, tiles, indexes, summaries, model outputs, and generated text are not exercised by this profile and do not become evidence because the tests pass.

[Back to top](#top)

---

<a id="explicit-holds-and-unproved-behavior"></a>

## Explicit holds and unproved behavior

The following remain outside the current executable lane:

| Surface | Current disposition | Graduation evidence needed before changing the claim |
|---|---|---|
| Other Hazards families | `UNKNOWN / NOT COVERED` | Accepted contracts, schemas, fixtures, validators, and positive/fail-closed tests for each named profile |
| Live source retrieval | `HOLD` | Admitted SourceDescriptor, rights/terms, credentials handling, retrieval contract, freshness/expiry behavior, and governed connector evidence |
| Evidence closure | `HOLD` | Deterministic EvidenceRef-to-EvidenceBundle resolver, fixtures, citation validation, and negative tests |
| Hazards policy runtime | `HOLD` | Accepted policy profile, evaluator binding, finite outcome record, obligations, tests, and governed consumer path |
| Proof production | `HOLD` | Accepted proof contract, producer, fixtures, freshness/source-role evidence, receipts, access controls, and validator |
| Candidate and release dry run | `HOLD` | Candidate identity, immutable artifact set, manifest contract, policy/review closure, correction path, and rollback target |
| Public API/UI/AI behavior | `UNKNOWN / HOLD` | Exact governed consumer path, not-for-life-safety disclosure, evidence/time/correction state, accessibility, and negative tests |
| Deployment and publication | `ABSENT / HOLD` | Separately authorized operational transition with release, deployment, correction, and rollback evidence |

The workflow's `build-proof-hazards` and `publish-dry-run-hazards` jobs intentionally preserve these holds. They may complete successfully after proving that no premature implementation or candidate has appeared. Read the job summary; do not translate a green held job into `PASS` for the held capability.

[Back to top](#top)

---

<a id="failure-handling"></a>

## Failure handling

| Symptom | Likely class | Safe response |
|---|---|---|
| `ModuleNotFoundError` or missing dependency | Environment/bootstrap error | Run the repository-owned hash-locked installer or use an approved prebuilt environment; do not add an unpinned install command |
| Network-denial assertion | Boundary regression or unsupported dependency behavior | Remove the live dependency from the focused path or provide a local fixture; do not unpatch the guard |
| Valid fixture fails | Schema/fixture/validator drift | Identify which authority changed and update the smallest coherent set with explicit compatibility reasoning |
| Invalid fixture passes | Fail-closed regression | Stop; restore the required negative constraint and retain an exact regression test |
| Exact finding differs | Semantic or diagnostic drift | Reconcile the schema and expected reason code; do not replace exact checks with a generic “must fail” assertion without justification |
| Materiality result differs | Determinism or threshold regression | Compare computed criteria, snapshot fields, time order, geometry digest, and thresholds; preserve domain-role separation |
| Missing required workflow path | Repository topology drift | Re-pin current main and reconcile the path against Directory Rules and the current workflow before editing |
| Proof/release hold job reports a newly surfaced implementation | Dependency-admission event | Open a separate bounded review to establish contract, fixtures, validators, policy/review, and rollback; do not delete the hold reflexively |
| Link checker fails | Documentation defect or path/anchor drift | Repair the exact local path, case, or anchor; external URLs remain unrequested and unverified |
| Hosted result lacks exact commit identity | Evidence gap | Mark hosted validation `NEEDS VERIFICATION`; do not transfer evidence from another SHA |

Never “fix” a failure by contacting a live source, replacing synthetic inputs with current operational data, deleting a negative fixture, weakening source-role separation, suppressing a reason code, or treating a later governance gate as already satisfied.

[Back to top](#top)

---

<a id="stronger-hermetic-execution"></a>

## Stronger hermetic execution

The repository's current process-level guards are useful but do not prove host-level no egress. A stronger rehearsal may be appropriate for security-sensitive review.

1. Prepare the exact repository revision and hash-locked dependencies from an approved local cache or wheelhouse.
2. Apply external network isolation through the approved runner, container, virtual machine, or CI control.
3. Confirm the isolation mechanism without contacting a real hazard source.
4. Run the same focused commands unchanged.
5. Record the isolation mechanism, executor identity, exact SHA, dependency provenance, commands, exit codes, and limitations.

**NEEDS VERIFICATION:** no canonical repository-owned hermetic Hazards runner was confirmed at the pinned snapshot. Do not invent a `sudo`, firewall, container, or namespace command in this runbook and present it as KFM authority. An externally isolated pass remains bounded to these fixtures and still does not establish evidence, policy, proof, release, or public safety.

[Back to top](#top)

---

<a id="pull-request-and-review-handoff"></a>

## Pull-request and review handoff

Record this minimum packet in the pull request or its verified check output:

```yaml
validation_scope: hazards-bounded-synthetic-drought
base_commit: <40-character SHA>
head_commit: <40-character SHA>
commands:
  - python -m unittest -v tests.domains.hazards.test_hazards_smoke
  - make hazards-validate
  - python tools/validators/docs/link-check/check_links.py --repo-root . --format text docs/runbooks/hazards/NO_NETWORK_TEST_RUNBOOK.md
results:
  smoke_test: PASS | FAIL | ERROR | NOT_RUN
  materiality_profile: PASS | FAIL | ERROR | NOT_RUN
  local_link_check: PASS | FAIL | ERROR | NOT_RUN
network_claim:
  live_sources_used: false
  in_process_guard: exercised | not_exercised
  host_egress_isolation: CONFIRMED | NEEDS_VERIFICATION | NOT_APPLICABLE
held_capabilities:
  - live_source_admission
  - evidence_resolution
  - policy_runtime
  - proof_production
  - release_candidate_assembly
  - release
  - deployment
  - promotion
  - publication
```

Use actual values; do not copy the example as evidence. Link hosted runs to the exact PR head. Report skipped, pending, held, inherited, unrelated, or unavailable checks separately from passing checks.

A runbook update and green focused validation may support review. They do not mark the pull request ready, authenticate a reviewer, approve a source, merge the change, release a candidate, deploy, promote, or publish.

[Back to top](#top)

---

<a id="rollback-path"></a>

## Rollback path

Before merge, close the draft pull request and abandon its feature branch. After an authorized merge, revert the focused documentation commit through a new reviewed change. Do not write directly to the default branch or silently restore stale May 2026 implementation claims.

Reverting this Markdown changes only the human procedure. It does not roll back schemas, fixtures, validators, tests, workflows, data, evidence, policy, proof, release, deployment, or publication. Use the [Hazards Rollback Drill](./ROLLBACK_DRILL.md) only for its documented synthetic rehearsal scope; it is not an operational release rollback executor.

[Back to top](#top)

---

<a id="maintenance-and-verification-backlog"></a>

## Maintenance and verification backlog

Update this runbook when any of these surfaces materially changes:

- `.github/workflows/domain-hazards.yml` job names, permissions, dependency profile, commands, required paths, or hold logic;
- the `hazards-validate` Make target;
- the three drought schema families or their exact fixture inventories;
- the network-denial guard or its covered entry points;
- `kfm-usdm-materiality-v1` states, outcomes, thresholds, fields, or reason codes;
- an accepted Hazards policy evaluator, EvidenceBundle resolver, proof producer, candidate contract, or release dry-run command lands;
- a canonical hermetic runner is adopted; or
- accountable Hazards, validation, safety, policy, release, and independent-review ownership is assigned.

Open items at this snapshot:

- **NEEDS VERIFICATION:** accountable domain and safety stewardship beyond the repository CODEOWNERS route;
- **NEEDS VERIFICATION:** exact-host egress enforcement for hosted and local runners;
- **HOLD:** policy runtime, evidence closure, proof production, candidate assembly, release, deployment, promotion, and publication;
- **PARTIAL:** `docs/runbooks/hazards/README.md` remains a one-byte placeholder, so the parent runbook index supplies the current directory boundary; and
- **UNKNOWN:** operational behavior outside the exact committed fixture profile.

### Related procedures and authority surfaces

- [Runbook root index](../README.md)
- [Hazards domain boundary](../../domains/hazards/README.md)
- [Hazards life-safety boundary](../../domains/hazards/LIFE_SAFETY_BOUNDARY.md)
- [Hazards publication boundary](../../domains/hazards/PUBLICATION_AND_BOUNDARY.md)
- [Not-for-Life-Safety Audit Runbook](./NOT_FOR_LIFE_SAFETY_AUDIT_RUNBOOK.md)
- [Hazards Promotion Runbook](./PROMOTION_RUNBOOK.md)
- [Hazards Rollback Drill](./ROLLBACK_DRILL.md)
- [Hazards workflow](../../../.github/workflows/domain-hazards.yml)
- [Hazards smoke test](../../../tests/domains/hazards/test_hazards_smoke.py)
- [USDM materiality tests](../../../tests/domains/hazards/test_validate_usdm_materiality.py)
- [USDM materiality validator](../../../tools/validators/domains/hazards/validate_usdm_materiality.py)
- [Hash-locked dependency installer](../../../tools/ci/install_python_ci.py)
- [USDM fixture manifest](../../../fixtures/domains/hazards/usdm_materiality/cases.json)

### Last reviewed

| Field | Value |
|---|---|
| Review date | 2026-08-27 |
| Evidence base | `main@7da7e26240859ba0d3c7bd9f992a4590e8146cf2` |
| Human review | Pending |
| Release effect | None |
| Publication effect | None |

[Back to top](#top)
