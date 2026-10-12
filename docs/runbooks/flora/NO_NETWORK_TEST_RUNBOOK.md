<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/flora/no-network-test-runbook
title: Flora — No-Network Test Runbook
type: runbook; operational-procedure; domain-lane; sensitive-domain; non-authoritative
version: v0.2
prior_version: v0.1 planning-oriented draft
status: draft; repository-grounded; bounded-public-safe-fixture-profile-executable; broader-proof-policy-release-and-live-source-held; non-publisher
owners:
  - "@bartytime4life — verified GitHub review route only"
owner_status: "Flora, taxonomy, source, rights, sensitivity/geoprivacy, stewardship, sovereignty, evidence, policy, validation, review, proof, release, correction, rollback, operations, and independent-review assignments remain NEEDS VERIFICATION; CODEOWNERS routing does not create those authorities."
created: 2026-05-13
updated: 2026-08-24
policy_label: public-review; flora; no-network; synthetic-fixtures; sensitive-location; fail-closed; non-release
current_path: docs/runbooks/flora/NO_NETWORK_TEST_RUNBOOK.md
owning_root: docs/
responsibility: "Document the exact bounded Flora no-network procedure currently supported by repository fixtures, a deterministic validator, its focused test module, and read-only workflow orchestration, while keeping live sources, botanical truth, rights, sensitivity decisions, evidence closure, policy, review, proof, release, deployment, promotion, and publication outside the test boundary."
truth_posture: cite-or-abstain
prepared_under_prompt: KFM Repository Build-Out & Markdown Modernization Implementation Agent v6.0.0
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 35bb62209569f63af78c6fefe4c85015d3bdceb1
  target_prior_blob: 898013af8c5f5ca6d3a86773c9b1cf98d63e9140
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adoption_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  flora_workflow_blob: 3fe6b1ba8150960692b6b2fc764c6aa31d09565c
  flora_validator_blob: 17933f997f7cb1219e3057ea74bf2c077dc45386
  flora_test_blob: 18d15781b78487de4c786c5ee38254f3a48e49e3
  flora_fixture_readme_blob: d09d667a5493628284095941c7a930034dcb7433
  flora_positive_fixture_blob: 6acf77484451b0ede31e3ce86b72088a287a35c8
  source_authority_register_blob: 32729857bc8eb5001acb37b8ee8e60bcb6e0dc50
  flora_domain_policy_readme_blob: 247fc146131f4e6598af9fd939cf087d92523ed6
  flora_sensitivity_policy_readme_blob: 4c65abec24135f7e4467fd108e163cdce594d5f9
  flora_proof_readme_blob: 130effccfd6e14f2660de04c3cc30d839503ef8a
  flora_candidate_readme_blob: 15a08f9fb2cdd33041d3a3f3e3c844f26a7a0998
drive_source:
  title: KFM_Flora_Architecture_PDF_Only_Implementation_Blueprint.pdf
  file_id: 1awNB4HbNr3X4ll0XjJnsO-AqmuO2GSfj
  source_date: 2026-04-21
  role: planning lineage; not current repository implementation proof
inspection_boundary: "Current-session GitHub reads of the target, accepted Directory Rules decision, Flora workflow, validator, tests, exact fixture profile, source-authority projection, Flora source registry, policy, sensitivity, proof, candidate, and generated-receipt surfaces; plus the connected Google Drive Flora architecture blueprint as planning lineage. Repository-native commands were not executed in a mounted checkout during authoring. No live source, credential, protected botanical payload, exact plant location, policy evaluator, evidence resolver, release service, deployed consumer, or public carrier was exercised."
related:
  - ../README.md
  - ./README.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../domains/flora/README.md
  - ../../domains/flora/SENSITIVITY.md
  - ./SOURCE_REFRESH_RUNBOOK.md
  - ./PROMOTION_RUNBOOK.md
  - ./ROLLBACK_RUNBOOK.md
  - ../../../fixtures/domains/flora/README.md
  - ../../../tests/domains/flora/README.md
  - ../../../tools/validators/domains/flora/README.md
  - ../../../tools/validators/domains/flora/validate_public_safe_fixture.py
  - ../../../.github/workflows/domain-flora.yml
  - ../../../control_plane/source_authority_register.yaml
  - ../../../data/registry/sources/flora/README.md
  - ../../../data/proofs/flora/README.md
  - ../../../policy/domains/flora/README.md
  - ../../../policy/sensitivity/flora/README.md
  - ../../../release/candidates/flora/README.md
  - ../../../data/receipts/generated/genrec-flora-public-safe-fixture-validation-20260803.json
tags: [kfm, flora, runbook, no-network, synthetic-fixtures, rare-plants, geoprivacy, validation, fail-closed]
notes:
  - "v0.2 replaces no-mounted-repository assumptions, speculative fixture matrices, illustrative enforcement mechanisms, and broad unproved trust-spine claims with the exact current bounded profile."
  - "The accepted implementation validates one synthetic public-safe candidate and six exact negative fixtures; other Flora fixture directories and object families are not silently included."
  - "The focused test module blocks common socket, DNS, HTTP, and urllib entry points for the validator path. It is not proof of operating-system egress isolation or repository-wide no-network behavior."
  - "The historical generated receipt is traceability evidence for an earlier execution, not current exact-head proof, an EvidenceBundle, a policy decision, a review decision, or release authority."
  - "This document changes no source, contract, schema, policy, fixture, validator, test, workflow, evidence object, receipt, proof, candidate, lifecycle state, runtime, deployment, promotion, rollback execution, or publication state."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Flora — No-Network Test Runbook

> **Run and interpret the Flora lane's current deterministic synthetic public-safe fixture profile without contacting a live botanical source, using protected plant data, or confusing fixture conformance with botanical truth or publication readiness.**

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#current-repository-posture)
[![Profile: bounded executable](https://img.shields.io/badge/profile-bounded%20executable-1a7f37?style=flat-square)](#current-executable-profile)
[![Network: validator path blocked](https://img.shields.io/badge/network-validator%20path%20blocked-b42318?style=flat-square)](#no-network-contract)
[![Sensitivity: fail closed](https://img.shields.io/badge/sensitive%20location-fail%20closed-b42318?style=flat-square)](#sensitivity-geoprivacy-and-security)
[![Proof and release: held](https://img.shields.io/badge/proof%20and%20release-HOLD-d4a72c?style=flat-square)](#current-holds-and-graduation-gates)
[![Publisher: no](https://img.shields.io/badge/publisher-no-6e7781?style=flat-square)](#authority-and-placement)

> [!IMPORTANT]
> **A `PASS` proves only conformance to the frozen synthetic `flora-public-safe-fixture` profile at the tested revision.** It does not establish a real taxon, botanical occurrence, source admission, rights clearance, sensitivity decision, stewardship approval, geoprivacy transform, `EvidenceBundle`, policy result, proof, candidate, release, deployment, promotion, or publication.

> [!WARNING]
> **Never place real or reverse-engineerable plant locations in this procedure.** Exact rare, protected, culturally sensitive, steward-controlled, private-land, access-route, collection-route, or transform-secret detail does not belong in fixtures, logs, workflow summaries, issues, pull requests, screenshots, or handoff packets.

> [!CAUTION]
> **The current suite does not execute Flora Rego policy, resolve evidence, or run an operating-system network sandbox.** It validates a closed file profile and its test module actively patches common Python socket, DNS, HTTP, and `urllib` entry points. Do not broaden that bounded result through prose.

**Quick navigation:** [Purpose](#purpose-and-terminal-boundary) · [Authority](#authority-and-placement) · [Posture](#current-repository-posture) · [Profile](#current-executable-profile) · [Network](#no-network-contract) · [Fixtures](#fixture-inventory-and-frozen-invariants) · [Preflight](#preconditions-and-stop-conditions) · [Local run](#local-procedure) · [CI](#hosted-ci-procedure) · [Results](#results-and-finite-outcome-interpretation) · [Failures](#failure-diagnosis) · [Sensitivity](#sensitivity-geoprivacy-and-security) · [Receipts](#evidence-receipts-and-proof-boundary) · [Handoff](#review-handoff) · [Holds](#current-holds-and-graduation-gates) · [Rollback](#correction-and-document-rollback) · [References](#related-current-surfaces) · [Checklist](#operator-checklist)

---

<a id="purpose-and-terminal-boundary"></a>

## Purpose and terminal boundary

Use this runbook to execute and review the exact Flora fixture-safety slice currently supported by the repository:

```text
one synthetic positive candidate
  + six synthetic exact-negative candidates
  + deterministic standard-library validator
  + focused unittest module with active network-call guards
  + read-only domain workflow
  -> PASS or stable code/path findings
  -> exact-revision review handoff
  -/> live source access
  -/> botanical, rights, sensitivity, evidence, policy, or review authority
  -/> proof, candidate, release, deployment, promotion, or publication
```

The KFM lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLETS -> PUBLISHED
```

This procedure does not enter or mutate that lifecycle. It reads repository-owned synthetic files and emits diagnostic output only.

### In scope

- `tools/validators/domains/flora/validate_public_safe_fixture.py`;
- shared bounded JSON mechanics at `tools/validators/_common/public_safe_fixture.py`;
- `tests/domains/flora/test_flora_smoke.py`;
- the exact positive and negative fixtures listed below;
- `.github/workflows/domain-flora.yml`, especially `validate-flora`;
- exact fixture inventory, polarity, stable finding codes and JSON paths, bounded parser behavior, CLI behavior, and network-call guards;
- exact-head hosted-check interpretation;
- a public-safe review handoff.

### Out of scope

- live GBIF, iNaturalist, USDA PLANTS, NatureServe, herbarium, agency, vegetation, invasive-plant, phenology, restoration, remote-sensing, or other source access;
- source admission, activation, rights review, endpoint verification, cadence, credentials, or retrieval;
- real plant names, specimen identifiers, exact occurrences, private-land records, cultural knowledge, collection clues, or restricted source payloads;
- general Flora contract or JSON Schema conformance;
- operational taxonomy resolution;
- Flora policy evaluation or sensitivity-tier adjudication;
- execution or scientific validation of a geoprivacy transform;
- `EvidenceRef` resolution to a real `EvidenceBundle`;
- proof production, candidate assembly, release dry run, deployment, publication, correction execution, withdrawal execution, or operational rollback.

**Maximum result:** a bounded validation handoff for the exact synthetic profile.

[Back to top](#top)

---

<a id="authority-and-placement"></a>

## Authority and placement

### Directory Rules result

**`PLACE` — confirmed for this same-path update.**

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts [Directory Rules v2](../../doctrine/directory-rules.md). A human operational procedure belongs under `docs/runbooks/`, with `flora/` as its domain segment. The tracked target therefore remains:

```text
docs/runbooks/flora/NO_NETWORK_TEST_RUNBOOK.md
```

This update creates no new root, parallel runbook authority, contract home, schema home, policy home, source registry, fixture lane, proof lane, release lane, or public path.

| Responsibility | Owning surface | This runbook's role |
|---|---|---|
| Human procedure | `docs/runbooks/flora/` | Explain exact execution, interpretation, stops, and handoff |
| Flora meaning | `docs/domains/flora/`, `contracts/domains/flora/` | Cite; do not redefine botanical truth |
| Machine shape | `schemas/contracts/v1/domains/flora/` and shared schema homes | Do not infer broad schema coverage from the fixture profile |
| Synthetic inputs | `fixtures/domains/flora/` | Consume only the frozen inventory named here |
| Validator implementation | `tools/validators/domains/flora/` | Document the exact entry point and finding contract |
| Executable tests | `tests/domains/flora/` | Document the exact assertions and no-network guards |
| Workflow orchestration | `.github/workflows/domain-flora.yml` | Bind results to an exact revision; do not infer release authority |
| Source admission | source registry and source-authority controls | Require separately accepted records; this procedure activates none |
| Policy and sensitivity | `policy/domains/flora/`, `policy/sensitivity/flora/` | Record current posture; this procedure does not evaluate them |
| Evidence and proof | evidence contracts and `data/proofs/` | Keep fixture references distinct from real evidence closure |
| Candidate and release | `release/` | Preserve holds; do not assemble or approve |
| Public clients | governed APIs and released artifacts | Outside this procedure |

A tracked path, detailed Markdown page, passing fixture, green workflow, generated receipt, pull request, or merge does not create an authority that the owning system has not supplied.

[Back to top](#top)

---

<a id="current-repository-posture"></a>

## Current repository posture

The following observations are pinned to `main@35bb62209569f63af78c6fefe4c85015d3bdceb1`. They describe repository bytes and bounded executable surfaces, not deployed behavior.

| Surface | Confirmed repository state | Safe conclusion |
|---|---|---|
| Prior runbook | v0.1 planning-oriented draft written under a no-mounted-repository assumption | Its broad path, fixture, command, and CI claims require replacement or narrowing |
| Flora workflow | `domain-flora` exists with `contents: read`, a substantive validation job, and separate proof/release hold jobs | One fixture profile is wired; proof and release are not |
| Validator | Standard-library `validate_public_safe_fixture.py` is substantive | It validates one closed synthetic profile only |
| Test module | `test_flora_smoke.py` is substantive | Exact inventories, parser limits, CLI behavior, non-echoing findings, and common network entry points are tested |
| Positive fixture | One explicit `public_safe_occurrence.json` | It is synthetic, generalized, fixture-only, not released, and not promotion-eligible |
| Negative fixtures | Six explicit JSON files with exact sorted sidecars | Known unsafe and malformed states fail with stable code/path findings |
| Other fixture directories | Numerous Flora fixture/planning lanes exist outside the accepted profile | Presence does not mean execution, acceptance, or profile coverage |
| Source-authority projection | `entries: []`, `implementation_status: ABSENT`, `authority_mode: projection_only` | No source is admitted or activated by the central projection |
| Flora source registry | README plus a `usda_plants.yaml` placeholder marked `PROPOSED` | A concrete accepted live Flora source is not established |
| Flora domain policy | Repository-grounded M0 scaffold corpus; evaluator unbound and inactive | The fixture suite is not policy evaluation |
| Flora sensitivity policy | Proposed scaffold | Operational sensitivity enforcement is not established |
| Flora proof lane | Repository-grounded draft with explicit workflow hold | No accepted Flora proof producer or populated proof closure is established |
| Flora candidate lane | Parent README only; no verified child dossier | No active candidate, release, or public carrier is established |
| Historical generated receipt | Earlier generated traceability record for the fixture slice | Useful lineage; not current exact-head execution, human review, or release proof |
| Deployment and public serving | Not established by this procedure or inspected surfaces | `UNKNOWN`; no public effect inferred |

### Drive planning lineage

The connected Drive source, *KFM Flora Architecture PDF-Only Implementation Blueprint* dated 2026-04-21, was authored when no repository checkout was available. Its durable guidance remains useful:

- begin with public-safe fixture and validator proof before live source activation;
- preserve taxonomy, occurrence, specimen, model, range, generalized representation, and generated explanation as distinct roles;
- fail closed for rare, protected, culturally sensitive, steward-controlled, or reverse-engineerable plant locations;
- keep tests, evidence, policy, review, release, correction, and rollback as separate responsibilities.

Current GitHub evidence now confirms one bounded implementation slice that the planning report could only propose. The report remains design lineage; it does not override current repository behavior or grant source, sensitivity, policy, or release authority.

[Back to top](#top)

---

<a id="current-executable-profile"></a>

## Current executable profile

### Profile identity

| Field | Current value |
|---|---|
| Scope | `flora-public-safe-fixture` |
| Validator | `tools/validators/domains/flora/validate_public_safe_fixture.py` |
| Shared parser/CLI mechanics | `tools/validators/_common/public_safe_fixture.py` |
| Tests | `tests/domains/flora/test_flora_smoke.py` |
| Workflow | `.github/workflows/domain-flora.yml` |
| Positive inventory | One file |
| Negative inventory | Six files with exact sidecars |
| Runtime dependencies | Python standard library for the focused validator and tests |
| Network posture | Declared forbidden; active common-call guards in the test module |
| Data posture | Repository-owned synthetic fixture values only |
| Release posture | `not_released`; `promotion_eligible: false` |

### What a positive candidate must preserve

The accepted positive fixture is a closed fixture-only candidate. It declares:

- `record_type: flora_public_safe_validation_candidate`;
- `fixture_only: true`;
- `network_access: forbidden`;
- synthetic taxon, source-descriptor, evidence, area, redaction-receipt, and review-record references;
- `source_role: synthetic_occurrence`;
- `taxon_concept_state: synthetic_resolved`;
- `rights_state: fixture_only`;
- generalized fixture-area support rather than coordinates or geometry;
- no exact, reverse-engineerable, private-land, or culturally sensitive location state;
- `policy_state: not_evaluated_fixture`;
- `review_state: fixture_only`;
- `release_state: not_released`;
- `promotion_eligible: false`;
- fixture-only correction and rollback states;
- explicit caveats that it is synthetic, is not a botanical occurrence claim, and is not released.

These values are the frozen test profile, not a proposed universal Flora schema or source-role vocabulary.

### What the validator rejects

The current validator fails closed for:

- non-object or undeclared shapes;
- malformed, duplicate-key, non-finite, oversized, excessively deep, excessively large, or non-regular JSON input;
- missing or malformed taxon, source, evidence, review, or redaction references;
- source-role, taxonomic-state, or rights-state collapse;
- exact-location aliases, coordinate-like or WKT-like values, private-land or access/collection clues;
- URLs or other external references;
- transform secrets such as jitter seeds, offsets, thresholds, precision values, or parameters;
- release or promotion claims;
- malformed public caveats and governance controls;
- numeric values anywhere in this deliberately non-numeric fixture profile.

The final rule is profile-specific. It must not be generalized into a statement that real Flora records can never contain numeric measurements.

[Back to top](#top)

---

<a id="no-network-contract"></a>

## No-network contract

### What is actively proved

For the focused Python path, the test module patches these common entry points and fails if they are called:

- `socket.socket.connect`;
- `socket.socket.connect_ex`;
- `socket.create_connection`;
- `socket.getaddrinfo`;
- `urllib.request.urlopen`.

The validator itself uses local file, JSON, path, regex, and CLI mechanics. The workflow also declares:

```text
KFM_NO_NETWORK=1
PYTHONDONTWRITEBYTECODE=1
```

The focused suite verifies that its validator calls none of the patched network functions.

### What is not proved

A successful run does **not** prove:

- operating-system, container, runner, proxy, or firewall egress isolation;
- that unrelated repository code cannot reach the network;
- that a subprocess added later would be blocked;
- that every Python HTTP client, native library, browser, shell command, or package manager is intercepted;
- that a URL in another fixture lane is safe or admitted;
- that live source credentials are absent from every environment;
- that a workflow environment variable alone enforces network denial.

Treat `KFM_NO_NETWORK=1` as a declared contract signal. The current executable evidence is the focused test's active interception and the validator's local-only implementation.

### Required posture for future expansion

A new test, helper, subprocess, validator, package, or fixture family is not covered merely because it lives under `tests/domains/flora/` or runs in `domain-flora`. It needs:

1. an exact fixture and profile contract;
2. explicit positive and negative behavior;
3. its own active no-network proof appropriate to its implementation;
4. non-echoing diagnostics;
5. bounded parser and file behavior;
6. documentation of what the pass does not establish;
7. workflow wiring and exact-head evidence;
8. a reversible review boundary.

[Back to top](#top)

---

<a id="fixture-inventory-and-frozen-invariants"></a>

## Fixture inventory and frozen invariants

### Exact accepted inventory

| Kind | Path | Expected result | Primary boundary |
|---|---|---|---|
| Positive | `fixtures/domains/flora/valid/public_safe_occurrence.json` | `PASS` | Closed synthetic generalized candidate with no release effect |
| Negative | `fixtures/domains/flora/invalid/candidate_not_object.json` | Findings / exit `1` | Top-level candidate must be an object |
| Negative | `fixtures/domains/flora/invalid/missing_public_controls.json` | Findings / exit `1` | Redaction/review refs and no-release/no-promotion controls are mandatory |
| Negative | `fixtures/domains/flora/invalid/missing_references.json` | Findings / exit `1` | Taxon, source-descriptor, and evidence refs are mandatory |
| Negative | `fixtures/domains/flora/invalid/role_and_taxonomy_collapse.json` | Findings / exit `1` | Frozen source role, taxon state, and rights posture must not collapse |
| Negative | `fixtures/domains/flora/invalid/undeclared_external_transform.json` | Findings / exit `1` | Undeclared fields, URLs, numerics, and transform secrets fail closed |
| Negative | `fixtures/domains/flora/invalid/unsafe_location_and_sensitivity.json` | Findings / exit `1` | Exact, reverse-engineerable, and private-land location material fails closed |

Each negative JSON file has a same-stem `*.expected_error.txt` sidecar. The test requires:

- the discovered JSON set to equal the frozen inventory;
- the discovered sidecar set to equal the frozen sidecar inventory;
- each sidecar to be nonempty, sorted, and exactly equal to validator findings;
- findings to contain only stable `code` and JSON `path` values.

### Inventory closure rule

Do not use wildcards over every Flora child directory and call the result the accepted no-network suite. Other fixture directories may support separate proposed, compatibility, or independently governed profiles. They are outside this runbook until their own executable evidence is admitted.

### Public-safe fixture rule

Accepted fixtures must contain no:

- real taxon, occurrence, specimen, collector, landowner, or steward record;
- coordinates, geometry, bounding box, geohash, WKT, parcel, locality, route, or access clue;
- URL, endpoint, credential, source payload, or live reference;
- culturally sensitive plant knowledge;
- redaction offset, precision, threshold, jitter seed, or transform parameters;
- claim of release, promotion eligibility, policy approval, or botanical truth.

Synthetic references to receipt, review, source, taxon, evidence, and area families are test values only. They do not resolve to authoritative objects.

[Back to top](#top)

---

<a id="preconditions-and-stop-conditions"></a>

## Preconditions and stop conditions

### Preconditions

Before running or reporting this profile:

1. Pin the exact repository revision.
2. Confirm the target paths match the pinned revision.
3. Confirm the fixture inventory is the one listed above.
4. Use Python 3.11 when reproducing the hosted workflow environment unless the repository has since accepted a different version.
5. Remove or withhold live Flora credentials from the test context where practical.
6. Run from the repository root.
7. Keep the workspace non-public and treat all emitted output as diagnostic.
8. Record whether the command is a local run, hosted exact-head run, or historical receipt reference.

### Mandatory stop conditions

Stop with a public-safe handoff instead of improvising when:

- the repository revision or fixture inventory is unresolved;
- a fixture contains or appears to contain a real plant record or sensitive location;
- a path, command, finding code, or expected sidecar differs from the pinned repository;
- a source, URL, credential, network client, or retrieval step is required;
- an operator proposes to substitute a live source for a fixture;
- an operator proposes to use a schema, policy, review, receipt, proof, or release pass that this profile does not execute;
- the positive fixture claims release, promotion eligibility, real policy evaluation, or real review;
- a failure would require exposing candidate values or sensitive detail in a public channel;
- broader Flora fixture directories are being included without an accepted profile;
- a hosted check is being attributed to a different commit;
- a green proof/release hold job is being described as implemented proof or release capability.

[Back to top](#top)

---

<a id="local-procedure"></a>

## Local procedure

### 1. Freeze revision and status

```bash
git rev-parse HEAD
git status --short
```

Record the exact commit. A dirty workspace is not automatically invalid, but unrelated modifications must be disclosed and must not alter the tested files or Python import path.

### 2. Inspect the accepted inventory

```bash
find fixtures/domains/flora/valid -maxdepth 1 -type f -print | sort
find fixtures/domains/flora/invalid -maxdepth 1 -type f -print | sort
```

Expected profile inventory:

```text
fixtures/domains/flora/valid/README.md
fixtures/domains/flora/valid/public_safe_occurrence.json
fixtures/domains/flora/invalid/README.md
fixtures/domains/flora/invalid/candidate_not_object.expected_error.txt
fixtures/domains/flora/invalid/candidate_not_object.json
fixtures/domains/flora/invalid/missing_public_controls.expected_error.txt
fixtures/domains/flora/invalid/missing_public_controls.json
fixtures/domains/flora/invalid/missing_references.expected_error.txt
fixtures/domains/flora/invalid/missing_references.json
fixtures/domains/flora/invalid/role_and_taxonomy_collapse.expected_error.txt
fixtures/domains/flora/invalid/role_and_taxonomy_collapse.json
fixtures/domains/flora/invalid/undeclared_external_transform.expected_error.txt
fixtures/domains/flora/invalid/undeclared_external_transform.json
fixtures/domains/flora/invalid/unsafe_location_and_sensitivity.expected_error.txt
fixtures/domains/flora/invalid/unsafe_location_and_sensitivity.json
```

README files document the profile but are not validator inputs.

### 3. Run the focused suite

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python -m unittest discover \
    --start-directory tests/domains/flora \
    --pattern 'test_flora_smoke.py' \
    --verbose
```

This is the repository's current accepted focused command.

### 4. Optionally inspect positive CLI behavior

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tools/validators/domains/flora/validate_public_safe_fixture.py \
    fixtures/domains/flora/valid/public_safe_occurrence.json
```

Expected shape:

```json
{"file":"fixtures/domains/flora/valid/public_safe_occurrence.json","findings":[],"scope":"flora-public-safe-fixture","status":"PASS"}
```

Path spelling in output reflects the path supplied to the command.

### 5. Optionally inspect negative CLI behavior

```bash
set +e
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tools/validators/domains/flora/validate_public_safe_fixture.py \
    fixtures/domains/flora/invalid/*.json
status=$?
set -e
test "$status" -eq 1
```

Exit `1` is the expected aggregate result because every supplied candidate is intentionally invalid. Do not report an expected negative rejection as a test infrastructure failure.

### 6. Record a value-minimized result

Record:

- exact commit;
- Python version;
- exact command;
- fixture inventory;
- exit code;
- test summary;
- finding codes and paths only when relevant;
- whether network mocks were exercised;
- whether output contained any candidate value;
- unresolved differences;
- terminal boundary: review handoff only.

Do not copy a full candidate, sensitive string, transform parameter, or real source value into the report.

[Back to top](#top)

---

<a id="hosted-ci-procedure"></a>

## Hosted CI procedure

The `domain-flora` workflow currently has three distinct jobs.

### `validate-flora`

This job:

1. checks out the exact workflow revision without persisted credentials;
2. sets up Python 3.11;
3. verifies the required validator, test, and fixture paths;
4. runs the focused unittest discovery command;
5. records `SUBSTANTIVE_SCOPE: flora-public-safe-fixture`;
6. states the exact non-effects in the job summary.

A success is exact-head hosted evidence for the bounded profile only.

### `build-proof-flora`

This job is a **readiness hold**, not a proof producer. It checks that:

- documented Flora proof boundaries remain present;
- the proof lane retains its explicit draft/proposed hold signal;
- no unexpected proof artifact, Make target, or probable Flora proof implementation has appeared without deliberate wiring.

A green result means the hold behaved as designed. It does not build an `EvidenceBundle`, `ProofPack`, validation report, redaction proof, or review record.

### `publish-dry-run-flora`

This job is also a **readiness hold**, not a candidate-specific dry run. It checks that:

- candidate and published-lane boundaries remain present;
- the candidate index still says a candidate is not a release;
- no child candidate record or accepted Flora release-dry-run Make target has appeared without deliberate graduation.

A green result means the release hold behaved as designed. It does not assemble a manifest, approve a candidate, deploy, promote, or publish.

### Exact-head reporting

When a pull request is open:

1. record the pull-request head SHA;
2. inspect runs associated with that exact SHA;
3. distinguish queued, in-progress, success, failure, cancelled, and skipped states;
4. distinguish the substantive validation job from explicit hold jobs;
5. inspect logs before classifying a failure as introduced or inherited;
6. do not use an older-head pass as current evidence;
7. do not treat mergeability, review, merge, release, deployment, promotion, or publication as workflow conclusions.

[Back to top](#top)

---

<a id="results-and-finite-outcome-interpretation"></a>

## Results and finite-outcome interpretation

### Validator and CLI results

| Result | Meaning |
|---|---|
| JSON status `PASS`; exit `0` | Every supplied candidate conforms to the frozen fixture profile |
| JSON status `FAIL`; exit `1` | At least one supplied candidate has stable findings |
| Exit `2` | CLI usage failure, such as no fixture path |
| `FIXTURE_JSON_INVALID` | File, UTF-8, JSON, duplicate-key, numeric, depth, node, or regular-file boundary failed |
| `FIXTURE_TOO_LARGE` | Input exceeds the configured byte limit |

`FAIL` is a validator profile result. It is not automatically a security incident, policy `DENY`, runtime `ERROR`, or release rollback decision.

### Keep result families separate

| Result family | Current use |
|---|---|
| Fixture validator | `PASS` / `FAIL`, with exit `0` / `1` / `2` |
| Unit test runner | test pass, failure, or error |
| Workflow | queued, in progress, success, failure, cancelled, or skipped |
| Proof/release readiness jobs | successful enforcement of an explicit `HOLD` |
| Governed runtime envelope | `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` where an accepted runtime defines them |
| Policy evaluation | allow, restrict, hold, deny, abstain, or error where an accepted policy profile defines them |
| Review and release | separately recorded human and release-governance states |

The current fixture validator does not emit a governed runtime answer and does not execute Flora policy. Do not translate its `PASS` into `ALLOW`, `ANSWER`, `READY`, `APPROVE`, `PROMOTED`, `RELEASED`, or `PUBLISHED`.

[Back to top](#top)

---

<a id="failure-diagnosis"></a>

## Failure diagnosis

### Classify before changing anything

| Failure family | Representative findings or symptoms | First check |
|---|---|---|
| Inventory drift | Extra or missing JSON or sidecar | Compare direct directory inventory with the frozen lists |
| Candidate shape | `CANDIDATE_NOT_OBJECT`, `UNDECLARED_*` | Confirm the candidate and nested objects are closed |
| Identity and support | `RECORD_ID_INVALID`, `TAXON_REF_INVALID`, `SOURCE_DESCRIPTOR_REF_INVALID`, `EVIDENCE_REFS_INVALID` | Confirm fixture-only prefixes and nonempty exact lists |
| Role, taxonomy, rights | `SOURCE_ROLE_INVALID`, `TAXON_CONCEPT_STATE_INVALID`, `RIGHTS_STATE_INVALID` | Confirm the profile's frozen synthetic states |
| Spatial and sensitivity | `SPATIAL_SUPPORT_INVALID`, `SENSITIVE_LOCATION_FIELD_FORBIDDEN`, `COORDINATE_LIKE_VALUE_FORBIDDEN`, `SENSITIVITY_STATE_INVALID` | Remove location-bearing or reverse-engineerable material; do not weaken the check |
| Public controls | `PUBLIC_REPRESENTATION_INVALID`, `PUBLIC_CAVEATS_INVALID`, `GOVERNANCE_STATE_INVALID` | Restore fixture review/redaction refs and no-release/no-promotion state |
| External or transform leakage | `EXTERNAL_REFERENCE_FORBIDDEN`, `TRANSFORM_SECRET_FIELD_FORBIDDEN`, `NUMERIC_VALUE_FORBIDDEN` | Remove URLs, secret parameters, and out-of-profile values |
| Loader bounds | `FIXTURE_TOO_LARGE`, `FIXTURE_JSON_INVALID` | Check UTF-8, JSON shape, duplicate keys, finite/bounded numbers, size, depth, nodes, and file type |
| Network guard | Runtime error stating network access is forbidden | Identify the exact new call; do not bypass the mock or add a live exception |
| Value echo | Candidate sentinel appears in stdout/stderr | Treat as a diagnostic confidentiality defect |
| Hosted CI | Job failure without current log diagnosis | Keep introduced/inherited classification `UNKNOWN` until logs and base comparison support it |

### Correction discipline

- Correct the smallest owning surface.
- Do not weaken a negative fixture to make an unsafe candidate pass.
- Do not remove a sidecar finding without explaining the semantic change.
- If the intended profile changes, update validator, fixtures, sidecars, tests, workflow inventory, READMEs, generated traceability, and this runbook in one coherent review boundary.
- If a real record caused the failure, remove it from the public repository and follow the appropriate sensitivity/security correction process; do not preserve it as a regression fixture.
- If an implementation change alters object meaning, source role, rights, sensitivity, policy, evidence, or release semantics, route it to those owning authorities rather than redefining them in test code.

[Back to top](#top)

---

<a id="sensitivity-geoprivacy-and-security"></a>

## Sensitivity, geoprivacy, and security

### Non-negotiable fixture boundary

This ordinary repository profile must never contain:

- exact or reverse-engineerable rare, protected, culturally sensitive, or steward-controlled plant locations;
- coordinates, geometry, bounding boxes, locality text, parcel IDs, private-land joins, collection routes, or access directions;
- collector, observer, landowner, steward, or living-person identifiers;
- restricted cultural knowledge or community-controlled plant information;
- source credentials, tokens, private endpoints, signed URLs, or source-native payloads;
- jitter seeds, offsets, radii, precision values, grid thresholds, transform rules, or other details that could undo a public-safe representation.

### Representation is not transformation proof

The positive fixture declares generalized fixture-area support and references synthetic redaction and review records. That declaration tests a shape. It does not prove that:

- a real transform was scientifically or ethically appropriate;
- a real restricted location was transformed;
- the transform cannot be reversed;
- the reviewer exists or approved it;
- a `RedactionReceipt` resolves;
- policy permitted public use.

Client styling, field omission, zoom limits, opacity, filters, or hidden popups are not security or geoprivacy transforms.

### Rights and source roles

Fixture-only rights and a synthetic occurrence role are deliberate non-authority states. The profile must not be repurposed to claim that:

- an aggregator is the originating authority;
- a taxonomic backbone proves occurrence;
- a specimen proves current population or range;
- a modeled distribution is an observation;
- a regulatory listing is an occurrence;
- public availability grants redistribution rights;
- a successful HTTP response admits a source.

### Safety response

If real sensitive content is discovered:

1. stop the run and avoid further copying;
2. minimize public discussion and do not quote the sensitive value;
3. preserve only the minimum safe evidence needed for authorized review;
4. notify the verified repository route and the accountable sensitivity/stewardship route when established;
5. remove or restrict exposure through an authorized correction path;
6. inspect logs, artifacts, caches, pull requests, screenshots, and downstream copies;
7. do not claim erasure or closure without evidence.

This runbook is not collection, access, conservation, legal-status, land-access, or emergency guidance.

[Back to top](#top)

---

<a id="evidence-receipts-and-proof-boundary"></a>

## Evidence, receipts, and proof boundary

### Fixture references are not real evidence closure

The positive candidate contains fixture-prefixed evidence, source, review, redaction, taxon, and area references. They prove only that the validator requires the declared fixture shape. They do not resolve to authoritative records.

### Historical generated receipt

`data/receipts/generated/genrec-flora-public-safe-fixture-validation-20260803.json` records an earlier authored slice, artifact hashes, and reported local validation. Interpret it as:

- traceability for an earlier repository checkpoint;
- a generated record whose human-review state remained pending;
- evidence that a bounded implementation effort occurred.

Do not interpret it as:

- current-head execution;
- a canonical `RunReceipt` profile accepted for operational use;
- an `EvidenceBundle` or proof pack;
- current artifact-integrity proof after later file changes;
- policy, sensitivity, stewardship, review, promotion, release, deployment, or publication approval.

Current claims require current exact-revision execution and hosted evidence.

### Proof and release remain separate

A future proof path must resolve claim support, evidence, source role, rights, sensitivity, public-safe representation, integrity, review, correction, and release dependencies under an accepted profile. A future release path must additionally close candidate identity, policy, accountable review, manifest, correction, withdrawal, and rollback. This fixture run does neither.

[Back to top](#top)

---

<a id="review-handoff"></a>

## Review handoff

A useful handoff is value-minimized and exact-revision-bound.

```yaml
profile: flora-public-safe-fixture
repository: bartytime4life/Kansas-Frontier-Matrix
base_or_tested_commit: <40-hex-sha>
pull_request_head: <40-hex-sha-or-null>
execution_kind: local | hosted-exact-head | historical-receipt-reference
command: <exact command>
python_version: <version>
fixture_inventory:
  positive: 1
  negative: 6
result:
  suite: PASS | FAIL | ERROR | NOT_RUN
  cli_exit: 0 | 1 | 2 | null
  findings:
    - code: <stable-code>
      path: <json-path>
network_boundary:
  active_python_guards: true | false | unknown
  os_egress_isolation: true | false | unknown
value_echo_detected: false | true | unknown
hosted_checks:
  domain_flora_validate: success | failure | pending | not_run
  proof_hold: success | failure | pending | not_run
  release_hold: success | failure | pending | not_run
introduced_vs_inherited: confirmed_introduced | confirmed_inherited | unknown | not_applicable
terminal_boundary: review_handoff_only
non_effects:
  - no_live_source
  - no_source_admission
  - no_real_sensitive_record
  - no_policy_evaluation
  - no_evidence_or_proof_creation
  - no_lifecycle_transition
  - no_release_deployment_promotion_or_publication
```

Do not add candidate values, real locations, source credentials, transform parameters, or restricted details to this packet.

[Back to top](#top)

---

<a id="current-holds-and-graduation-gates"></a>

## Current holds and graduation gates

### Current holds

| Area | Current posture | Consequence |
|---|---|---|
| Live source authority | Central projection empty; USDA PLANTS record is a proposal placeholder | No live source access or source-backed claim |
| Taxonomy authority | Synthetic resolved fixture state only | No operational name resolution or taxonomic endorsement |
| Rights | Fixture-only state | No redistribution or use permission established |
| Sensitivity policy | Scaffold; operational evaluator not established | Exact or inferable locations remain fail closed |
| Flora domain policy | M0 scaffold corpus; evaluator unbound | No policy result may be inferred from fixture success |
| Geoprivacy execution | No accepted transform executed by this profile | Synthetic reference is not transform proof |
| Evidence resolution | Fixture refs only | No real `EvidenceBundle` closure |
| Proof production | Explicit workflow hold | No Flora proof packet produced |
| Candidate | No verified child dossier | No candidate-specific review or dry run |
| Release dry run | Explicit workflow hold | No manifest assembly or release rehearsal |
| Deployment/publication | Not established | No public carrier or runtime effect |
| Local Flora runbook index | One-byte placeholder at the inspected base | Navigation drift remains a separate documentation task |
| Broader Flora fixtures | Independent lanes with mixed or unverified maturity | No automatic inclusion in this profile |

### Graduation gates for a broader no-network slice

A future expansion must close, as applicable:

1. accepted semantic contract and machine schema for the exact object family;
2. admitted version-pinned source or an explicitly synthetic source profile;
3. source-role and taxonomy vocabularies;
4. rights, attribution, and use constraints;
5. sensitivity and stewardship inputs;
6. a deterministic public-safe transform profile when location-bearing data is involved;
7. resolvable evidence and proof contracts;
8. accepted policy bundle, entrypoint, evaluator, finite results, and obligations;
9. exact public-safe fixtures and negative cases;
10. deterministic validators with bounded non-echoing diagnostics;
11. active no-network proof for every implementation path and subprocess;
12. accountable review and separation of duties;
13. candidate, correction, withdrawal, and rollback support;
14. workflow wiring, exact-head CI, documentation, and generated traceability;
15. explicit proof that the new profile does not weaken this existing fixture-safety slice.

Until those gates close, keep broader behavior `PROPOSED`, `NEEDS VERIFICATION`, `UNKNOWN`, or `HOLD`.

[Back to top](#top)

---

<a id="correction-and-document-rollback"></a>

## Correction and document rollback

### Before merge

Close or abandon the draft pull request and delete only its task branch when appropriate. No operational rollback is required because this change is documentation-only.

### After merge

Use a reviewed revert or a smaller forward correction. The prior target blob is:

```text
898013af8c5f5ca6d3a86773c9b1cf98d63e9140
```

Restoring that blob restores the previous v0.1 documentation. It does not change the validator, fixtures, tests, workflow, source authority, policy, evidence, proof, candidate, lifecycle, runtime, deployment, promotion, rollback execution, or publication state.

### When behavior changes

If validator, fixture, test, or workflow behavior changes materially, update this runbook in the same review boundary or explain why the documentation remains accurate. Do not leave exact commands, inventories, finding semantics, network claims, or hold states stale.

[Back to top](#top)

---

<a id="related-current-surfaces"></a>

## Related current surfaces

- Parent runbook index: [`docs/runbooks/README.md`](../README.md)
- Local Flora runbook lane: [`docs/runbooks/flora/README.md`](README.md)
- Flora domain boundary: [`docs/domains/flora/README.md`](../../domains/flora/README.md)
- Flora sensitivity documentation: [`docs/domains/flora/SENSITIVITY.md`](../../domains/flora/SENSITIVITY.md)
- Directory Rules: [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md)
- Accepted Directory Rules decision: [`ADR-0029`](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
- Fixture index: [`fixtures/domains/flora/README.md`](../../../fixtures/domains/flora/README.md)
- Test index: [`tests/domains/flora/README.md`](../../../tests/domains/flora/README.md)
- Validator index: [`tools/validators/domains/flora/README.md`](../../../tools/validators/domains/flora/README.md)
- Validator: [`validate_public_safe_fixture.py`](../../../tools/validators/domains/flora/validate_public_safe_fixture.py)
- Workflow: [`domain-flora.yml`](../../../.github/workflows/domain-flora.yml)
- Source-authority projection: [`source_authority_register.yaml`](../../../control_plane/source_authority_register.yaml)
- Flora source registry: [`data/registry/sources/flora/README.md`](../../../data/registry/sources/flora/README.md)
- Flora policy boundary: [`policy/domains/flora/README.md`](../../../policy/domains/flora/README.md)
- Flora sensitivity-policy scaffold: [`policy/sensitivity/flora/README.md`](../../../policy/sensitivity/flora/README.md)
- Flora proof boundary: [`data/proofs/flora/README.md`](../../../data/proofs/flora/README.md)
- Flora candidate boundary: [`release/candidates/flora/README.md`](../../../release/candidates/flora/README.md)
- Historical generated receipt: [`genrec-flora-public-safe-fixture-validation-20260803.json`](../../../data/receipts/generated/genrec-flora-public-safe-fixture-validation-20260803.json)

When these surfaces disagree, prefer accepted doctrine and ADRs for placement, current code/tests/workflows for executable behavior, and owning source/evidence/policy/release objects for authority. Stop rather than choosing the wording that permits broader exposure.

[Back to top](#top)

---

<a id="operator-checklist"></a>

## Operator checklist

### Preflight

- [ ] Exact repository revision recorded.
- [ ] Target validator, test, workflow, and fixture paths verified at that revision.
- [ ] Positive inventory equals one accepted JSON file.
- [ ] Negative inventory equals six JSON files and six exact sidecars.
- [ ] No real taxon, specimen, occurrence, coordinate, private-land detail, cultural knowledge, credential, URL, or transform secret is present.
- [ ] Live Flora credentials are not required.
- [ ] Terminal boundary is review handoff only.

### Execute

- [ ] Run the focused unittest command from repository root.
- [ ] Optionally run the positive validator command and confirm exit `0`.
- [ ] Optionally run all negative fixtures and confirm aggregate exit `1`.
- [ ] Confirm no network mock was called.
- [ ] Confirm findings are stable, sorted, and value-minimized.
- [ ] Confirm stdout/stderr does not echo candidate values.

### Interpret

- [ ] Report `PASS` only as fixture-profile conformance.
- [ ] Keep validator, test, workflow, policy, runtime, review, proof, candidate, and release states distinct.
- [ ] Bind hosted evidence to the exact pull-request head.
- [ ] Inspect failure logs before classifying introduced versus inherited.
- [ ] Treat proof and release job success as successful hold enforcement, not implemented capability.

### Handoff

- [ ] Prepare the value-minimized packet.
- [ ] Record unresolved holds and the smallest owning follow-up.
- [ ] Keep human review, merge, source activation, lifecycle transition, release, deployment, promotion, rollback execution, and publication separate.
- [ ] Preserve a documentation rollback target.

[Back to top](#top)

---

## Change log

| Version | Date | Change |
|---|---|---|
| `v0.1` | 2026-05-13 | Planning-oriented no-network procedure authored without mounted repository evidence |
| `v0.2` | 2026-08-24 | Reconciles the runbook to the exact bounded validator, fixtures, tests, workflow, source/policy/proof/release holds, and Drive planning lineage |

No source, protected botanical material, policy decision, evidence object, lifecycle state, release, deployment, promotion, rollback execution, publication state, or repository setting is changed by this document.
