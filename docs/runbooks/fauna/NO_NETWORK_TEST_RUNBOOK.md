<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/fauna/no-network-test-runbook
title: Fauna — No-Network Test Runbook
type: runbook; operational-procedure; domain-lane; sensitive-domain; non-authoritative
version: v0.2
prior_version: v0.1 planning-only
status: draft; repository-grounded; bounded-fixture-safety-executable; adjacent-occurrence-and-tile-profiles-executable; proof-release-and-live-source-held; non-publisher
owners:
  - "@bartytime4life — verified GitHub review route only"
owner_status: "Fauna, taxonomy, source, rights, sensitivity/geoprivacy, evidence, policy, test, review, proof, release, correction, rollback, and operations assignments remain NEEDS VERIFICATION; CODEOWNERS routing does not establish those authorities."
created: 2026-05-13
updated: 2026-08-24
policy_label: public-review; fauna; no-network; synthetic-fixtures; sensitive-location; fail-closed; non-release
current_path: docs/runbooks/fauna/NO_NETWORK_TEST_RUNBOOK.md
owning_root: docs/
responsibility: >-
  Document the exact bounded Fauna no-network procedure currently supported by
  repository fixtures, the fixture-safety validator, its deterministic tests, and
  read-only workflow orchestration, while keeping source admission, taxonomic
  authority, evidence, policy, review, proof, release, deployment, promotion, and
  publication outside the test boundary.
truth_posture: cite-or-abstain
prepared_under_prompt: KFM Repository Build-Out & Markdown Modernization Implementation Agent v6.0.0
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 67e1e2c698dff941b689dba35cfc968ac573a5af
  target_prior_blob: 1eb1bebe8527fa30041caa04e97cc7efc9869b0a
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adoption_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  fixture_readme_blob: fcd934834470ccbc67f6d2683c5b086ff65b4067
  test_readme_blob: 66b38a6c20b77b36d51f1efa434876ffdb2ac197
  smoke_test_blob: 8154761e55c01db9133f125f7cf268c2fbb8589e
  fixture_validator_blob: fe96d8c4cc78f44679ddf617b2b1251fe621928c
  domain_workflow_blob: 0edc73a77ee0ddb3193db2c0386ed6ac685b139a
inspection_boundary: >-
  Current-session GitHub reads of the target; accepted Directory Rules decision;
  CODEOWNERS; Fauna domain, sensitivity, fixture, policy, test, and validator
  indexes; the fixture-safety validator and test module; and the domain workflow.
  Repository-native commands were not executed in a mounted checkout while this
  document was authored. No live source was contacted, no protected Fauna payload
  was inspected, and no source, evidence, policy, lifecycle, review, proof, release,
  deployment, promotion, publication, correction, or rollback state changed.
related:
  - ../README.md
  - ./README.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../domains/fauna/README.md
  - ../../domains/fauna/SENSITIVITY.md
  - ../../domains/fauna/POLICY.md
  - ./SOURCE_REFRESH_RUNBOOK.md
  - ./PROMOTION_RUNBOOK.md
  - ./ROLLBACK_RUNBOOK.md
  - ../../../fixtures/domains/fauna/README.md
  - ../../../policy/domains/fauna/README.md
  - ../../../policy/sensitivity/fauna/README.md
  - ../../../tests/domains/fauna/README.md
  - ../../../tests/domains/fauna/test_fauna_smoke.py
  - ../../../tools/validators/domains/fauna/README.md
  - ../../../tools/validators/domains/fauna/validate_public_safe_fixture.py
  - ../../../data/registry/sources/fauna/README.md
  - ../../../data/proofs/fauna/README.md
  - ../../../release/candidates/fauna/README.md
  - ../../../.github/workflows/domain-fauna.yml
  - ../../../.github/workflows/fauna-occurrence-evidence.yml
  - ../../../.github/workflows/fauna-tile-field-allowlist.yml
tags: [kfm, fauna, runbook, no-network, fixtures, sensitivity, geoprivacy, validation, fail-closed]
notes:
  - "v0.2 replaces no-mounted-repository assumptions, nonexistent fixture trees, illustrative runner commands, and broad unproved trust-spine claims with current repository evidence and exact bounded entry points."
  - "The primary suite validates synthetic fixture hygiene only; it does not execute production schemas, resolve EvidenceBundles, apply policy, authenticate reviewers, produce proofs, or approve public Fauna use."
  - "Two adjacent no-network profiles—draft OccurrenceEvidence and inactive tile-field allowlist—remain separate bounded executables and are not silently folded into the primary suite."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Fauna — No-Network Test Runbook

> **Run and interpret the Fauna lane's accepted deterministic fixture-safety checks while keeping live sources, real animal records, exact or reconstructable sensitive locations, credentials, internal stores, policy authority, proof production, release, deployment, promotion, and publication outside the test boundary.**

> [!IMPORTANT]
> **The accepted primary result is fixture-hygiene evidence, not Fauna truth.** A passing fixture, validator, test, workflow, digest, or commit proves only the declared synthetic profile at the tested revision. It does not establish taxonomic identity, source admission, rights clearance, geoprivacy approval, EvidenceBundle closure, policy enforcement, human review, release readiness, or safe public use.

> [!WARNING]
> **Never use real or reconstructable sensitive Fauna detail in this procedure.** Exact occurrences, nests, dens, roosts, hibernacula, spawning or breeding sites, telemetry, private-land joins, collection notes, observer identity, and steward-controlled location detail do not belong in fixtures, logs, workflow summaries, issues, pull requests, screenshots, or generated artifacts.

> [!CAUTION]
> **Do not collapse the three current bounded validator profiles.** Synthetic fixture hygiene, draft `OccurrenceEvidence` validation, and inactive tile-field allowlist comparison answer different questions. None independently authorizes a real occurrence, tile, layer, API response, map, export, Focus Mode answer, release, or publication.

**Quick navigation:** [Purpose](#1-purpose-scope-and-terminal-boundary) · [Authority](#2-authority-placement-and-current-evidence) · [Contract](#3-no-network-contract) · [Profiles](#4-current-executable-profile-inventory) · [Fixtures](#5-accepted-primary-fixture-inventory) · [Preflight](#6-preflight-and-stop-conditions) · [Run](#7-primary-suite-procedure) · [Results](#8-results-findings-and-ci-interpretation) · [Sensitivity](#9-sensitivity-geoprivacy-and-public-safety) · [Failures](#10-failure-diagnosis-and-classification) · [Handoff](#11-review-handoff) · [Rollback](#12-correction-document-rollback-and-recovery) · [Open work](#13-current-holds-and-open-verification) · [Related](#14-related-surfaces) · [History](#15-change-log)

---

## 1. Purpose, scope, and terminal boundary

Use this runbook to execute the current Fauna synthetic public-safe fixture profile at an exact repository revision and report what the result does—and does not—establish.

The operator must:

1. freeze the exact revision, target paths, profile, and fixture inventory;
2. remove ambient source credentials and deny intentional live-source access;
3. use only the seven accepted repository-controlled JSON fixtures;
4. execute the exact standard-library test module;
5. prove that both accepted fixture-only candidates pass;
6. prove that all five negative fixtures fail closed with exact stable finding sets;
7. confirm the sensitive-withheld fixture retains its synthetic transform reference, matching fixture geoprivacy state, and withholding caveat;
8. bind any hosted status to the exact pull-request head; and
9. stop at a reviewable validation handoff.

```text
exact revision
  -> seven synthetic fixture files
  -> fixture-safety validator
  -> eight deterministic tests
  -> PASS or exact fail-closed findings
  -> exact-head workflow evidence
  -> human review handoff
  -/> live source admission
  -/> taxonomic, evidence, policy, or geoprivacy authority
  -/> proof, release, deployment, promotion, or publication
```

The KFM lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLETS -> PUBLISHED
```

No command in this runbook performs that lifecycle. The accepted validator reads synthetic fixture files and emits diagnostic JSON only.

### In scope

- `tools/validators/domains/fauna/validate_public_safe_fixture.py`;
- `tests/domains/fauna/test_fauna_smoke.py`;
- the two accepted positive and five accepted negative fixtures under `fixtures/domains/fauna/`;
- the `validate-fauna` job in `.github/workflows/domain-fauna.yml`;
- exact valid/invalid polarity, bounded finding codes, fixture-inventory closure, and test-boundary network guards;
- current adjacent-profile inventory so operators do not misstate coverage;
- exact-head CI interpretation and review handoff.

### Out of scope

- live source fetch, connector execution, source admission, source-rights approval, or source activation;
- validation of real `OccurrencePublic`, `OccurrenceRestricted`, range, migration, mortality, disease, conservation, taxonomic, or sensitive-site records;
- resolution of a `SourceDescriptor`, `EvidenceRef`, `EvidenceBundle`, `RedactionReceipt`, `PolicyDecision`, or `ReviewRecord` instance;
- production geoprivacy transform selection or execution;
- public tile-byte, layer-manifest, API, map, search, graph, export, Evidence Drawer, Focus Mode, or AI validation;
- proof production, release dry-run, promotion, deployment, publication, correction, withdrawal, or operational rollback.

The maximum result is a **bounded validation handoff**.

[Back to top](#top)

---

## 2. Authority, placement, and current evidence

### Directory Rules result

**`PLACE` — CONFIRMED for this same-path update.** Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts the exact [Directory Rules v2](../../doctrine/directory-rules.md) bytes. This tracked human procedure remains at `docs/runbooks/fauna/NO_NETWORK_TEST_RUNBOOK.md`; no root, path, contract, schema, policy, fixture, test, validator, workflow, source record, receipt, proof, release object, or public artifact is created or moved.

| Concern | Owning surface | This runbook's relationship |
|---|---|---|
| Fauna meaning and sensitivity intent | `docs/domains/fauna/`, `contracts/domains/fauna/` | cite; do not redefine |
| Machine shape | `schemas/contracts/v1/domains/fauna/` | do not claim production authority from scaffolds |
| Synthetic inputs | `fixtures/domains/fauna/` | consume the accepted bounded inventory |
| Validator implementation | `tools/validators/domains/fauna/` | document exact entry point and scope |
| Executable proof | `tests/domains/fauna/` | document exact assertions and polarity |
| Workflow orchestration | `.github/workflows/` | report exact-head status; do not infer required-check coupling |
| Source, rights, evidence, policy, review | owning registries and governance surfaces | preserve unresolved holds |
| Proof, release, correction, rollback | `data/proofs/`, `data/receipts/`, `release/` | no writes or authority |
| Public delivery | governed APIs and released public-safe carriers | outside this procedure |

The parent [runbook index](../README.md) governs the broader operational lane. The local [`docs/runbooks/fauna/README.md`](./README.md) is a one-byte placeholder at the pinned snapshot, so the local lane boundary remains `HOLD / NEEDS VERIFICATION`; this runbook does not replace that missing boundary contract.

### Current evidence

Pinned to `main@67e1e2c698dff941b689dba35cfc968ac573a5af`:

| Surface | Status | Bounded conclusion |
|---|---|---|
| Prior target | **CONFIRMED stale planning state** | It names nonexistent `no_network/` fixture/test trees, illustrative runners, proposed publication paths, and broad trust-spine behavior not implemented by the primary suite. |
| Fixture root | **CONFIRMED bounded corpus** | Seven accepted JSON fixtures: two positive and five fail-closed negatives; other fixture lanes remain draft or placeholder. |
| Fixture validator | **CONFIRMED bounded executable** | Standard-library, deterministic, fixture-only, location-withheld, no-network by implementation design, with stable value-safe findings. |
| Primary test module | **CONFIRMED executable** | Eight standard-library tests exercise the exact seven-fixture inventory, sensitive-withheld disclosure, structural limits, encoded clues, and network-call guards. |
| Domain workflow | **CONFIRMED command-bearing definition** | `validate-fauna` runs the exact smoke module; proof and release-dry-run jobs remain explicit holds. |
| Adjacent profiles | **CONFIRMED bounded executables** | Draft `OccurrenceEvidence` and inactive tile-field allowlist have separate validators, tests, fixtures, and workflows. |
| Policy | **CONFIRMED mixed scaffold / unbound** | Direct Rego stubs have conflicting default-result shapes; no accepted Fauna bundle, selector, evaluator, production consumer, or release binding is established. |
| Production schemas and source descriptors | **CONFIRMED draft/proposed surfaces** | Current occurrence schemas and source templates do not establish production admission or public safety for the primary fixture suite. |
| Proof, release, deployment, publication | **HOLD / UNKNOWN** | No accepted Fauna proof producer, candidate release dry-run, deployed consumer, or public publication is established by this procedure. |
| GitHub review route | **CONFIRMED routing only** | CODEOWNERS routes review to `@bartytime4life`; functional and independent stewardship remain unassigned. |

Repository-native commands were not run in a mounted checkout while this documentation revision was authored.

[Back to top](#top)

---

## 3. No-network contract

| Requirement | Required posture | Failure posture |
|---|---|---|
| Upstream access | No intentional HTTP, HTTPS, DNS, socket, API, tile, registry, model, or source request from the validated code path | `DENY` and stop |
| Credentials | No source token, API key, cloud credential, private endpoint, or unrelated secret exposed to the test | `DENY` and stop |
| Inputs | Exact repository-controlled synthetic JSON fixtures only | `DENY` on real, mutable, or protected input |
| Runtime | Python 3.11-compatible standard library for the accepted validator/test slice | `ERROR` on missing or incompatible runtime |
| Internal stores | No production database, object store, graph, index, registry resolver, lifecycle store, or public service | `DENY` |
| Lifecycle writes | No write to RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLETS, PUBLISHED, receipt, proof, or release homes | `DENY` or `HOLD` |
| Fixture polarity | Both accepted positive fixtures produce no findings; all five negative fixtures produce their exact expected findings | `FAIL` on unexpected polarity or finding drift |
| Inventory | `valid/*.json` and `invalid/*.json` exactly match the accepted seven-file set | `FAIL` on silent addition, removal, or rename |
| Sensitive-withheld closure | Synthetic redaction-receipt reference, fixture-only geoprivacy state, and explicit withholding caveat remain present | `FAIL` if incomplete |
| Network guard | Accepted test monkeypatches are exercised | `HOLD` if merely assumed |

### What the accepted network guard proves

`test_fauna_smoke.py` patches these Python entry points to raise on attempted use:

- `socket.socket.connect`;
- `socket.create_connection`;
- `urllib.request.urlopen`.

The validator itself imports only the Python standard library and contains no source client. Together, those facts provide **bounded in-process evidence** for the accepted path.

They do **not** prove operating-system or container-level egress denial, subprocess isolation, DNS interception outside the patched path, or absence of future network-capable imports. A stronger sandbox or network namespace remains a separate `NEEDS VERIFICATION` item.

### Core environment

Run from the repository root:

```bash
export KFM_NO_NETWORK=1
export PYTHONDONTWRITEBYTECODE=1
export PYTHONHASHSEED=0
export PYTHONUNBUFFERED=1
export TZ=UTC
```

The current workflow sets `KFM_NO_NETWORK=1`, `PYTHONDONTWRITEBYTECODE=1`, `PYTHONUNBUFFERED=1`, and `TZ=UTC`. The test monkeypatches—not the environment variable alone—supply the accepted network-call guard.

[Back to top](#top)

---

## 4. Current executable profile inventory

### Primary profile: synthetic public-safe fixture hygiene

| Surface | Exact path | Bounded claim |
|---|---|---|
| Validator | `tools/validators/domains/fauna/validate_public_safe_fixture.py` | Closed synthetic fixture profile; no real occurrence or release validation |
| Tests | `tests/domains/fauna/test_fauna_smoke.py` | Eight deterministic tests over seven exact fixtures |
| Fixtures | `fixtures/domains/fauna/valid/*.json`, `invalid/*.json` | Synthetic, location-withheld, fixture-only, no live URLs, unreleased, promotion-ineligible |
| Workflow | `.github/workflows/domain-fauna.yml` → `validate-fauna` | Read-only orchestration of the exact smoke module |
| Output | JSON lines with `PASS` or `FAIL`, stable code/path findings, and scope `synthetic-public-safe-fixture-only` | Diagnostic output only; not a canonical ValidationReport or decision object |

The validator accepts only a closed candidate shape with synthetic identifiers, `source_role: synthetic`, fixture-only rights and review state, withheld spatial support, synthetic evidence references, `network_access: forbidden`, `release_state: not-released`, and `promotion_state: not-eligible`.

The sensitive-withheld variant additionally requires:

- a `fixture:receipt:redaction:fauna:` reference;
- `geoprivacy_state: withheld-transform-fixture`; and
- the exact public caveat declaring that precision is withheld.

The reference is a fixture string, **not** a resolved `RedactionReceipt` instance.

### Adjacent profile: draft `OccurrenceEvidence`

The separate occurrence validator, tests, fixtures, and [`fauna-occurrence-evidence.yml`](../../../.github/workflows/fauna-occurrence-evidence.yml) workflow prove a draft closed occurrence profile, deterministic identity, source-role/basis anti-collapse, rights/provenance declarations, sensitivity/geometry consistency, and exact fixture replay.

Its result does not establish source admission, taxonomic authority, geoprivacy approval, evidence closure, release readiness, or public occurrence authority. A consistently represented quarantined candidate may pass representation validation while remaining ineligible for release.

### Adjacent profile: inactive tile-field allowlist

The separate tile validator, tests, fixtures, and [`fauna-tile-field-allowlist.yml`](../../../.github/workflows/fauna-tile-field-allowlist.yml) workflow compare synthetic property names against an inactive candidate allowlist.

They do not inspect tile bytes, accept a production vocabulary, activate policy, prove a `LayerManifest`, approve a release, or authorize a public tile.

### Explicit held surfaces

- active Fauna policy bundle, evaluator, normalized input assembler, decision receipt, and obligation handlers;
- real source admission, rights currency, taxonomy resolution, and sensitive-species stewardship;
- production `OccurrencePublic` / restricted-to-public transform and resolved geoprivacy receipts;
- `EvidenceRef` to `EvidenceBundle` production resolution;
- proof production and Fauna release dry-run;
- governed public API, map, tile, search, graph, export, Evidence Drawer, Focus Mode, and AI consumption;
- deployment, promotion, publication, correction propagation, withdrawal, cache invalidation, and rollback drill.

[Back to top](#top)

---

## 5. Accepted primary fixture inventory

The primary suite intentionally uses a small closed inventory. Do not replace it with the proposal-era “valid/invalid/denied/abstain/rollback for every object family” matrix unless actual fixtures, consumers, contracts, and tests are added and reviewed.

### Positive fixtures

| Path | Expected result | What it proves |
|---|---|---|
| `fixtures/domains/fauna/valid/non_sensitive_occurrence.json` | `PASS` | Synthetic, fixture-only, source-role `synthetic`, location-withheld, no-network, unreleased candidate satisfies the closed fixture profile. It is not an accepted `OccurrencePublic` instance. |
| `fixtures/domains/fauna/valid/sensitive_withheld_occurrence.json` | `PASS` | Synthetic sensitive-location scenario with no coordinates retains a synthetic transform reference, matching fixture geoprivacy state, withholding caveat, and held release/promotion state. It is not an accepted `RedactionReceipt` or public release. |

### Negative fixtures

| Path | Exact fail-closed focus |
|---|---|
| `fixtures/domains/fauna/invalid/missing_source_descriptor.json` | missing synthetic source reference |
| `fixtures/domains/fauna/invalid/unresolved_taxonomy.json` | unresolved synthetic taxonomy state |
| `fixtures/domains/fauna/invalid/unresolved_governance.json` | unresolved evidence, rights, policy, geoprivacy, review, correction, and rollback state |
| `fixtures/domains/fauna/invalid/over_precise_sensitive.json` | location-shaped fields, numeric precision hints, unresolved sensitivity, and unsafe spatial kind |
| `fixtures/domains/fauna/invalid/encoded_location_clue.json` | aliased location field, live-URL-shaped text, coordinate-pair-shaped text, and value-safe reporting |

### Structural and content hardening exercised by tests

The suite also constructs in-memory or temporary-file cases for:

- common location aliases such as `lat`, `lon`, `lng`, `x`, `y`, `bbox`, `centroid`, `easting`, and `northing`;
- finite numeric values beneath location-like keys;
- malformed, nested, empty, too-long, or excessive public caveats;
- whitespace- or Unicode-format-obfuscated URL-like strings;
- control characters and coordinate-pair-shaped free text;
- cyclic, deeper-than-64-level, or more-than-4,096-node structures;
- fixture files over 1,000,000 bytes;
- JSON integer tokens over 512 digits; and
- undeclared top-level, spatial, and governance fields, including mixed-type keys.

Findings report stable codes and bounded JSON-like paths. They must not echo protected values.

[Back to top](#top)

---

## 6. Preflight and stop conditions

Run from a clean checkout or isolated worktree at the intended revision.

```bash
git rev-parse HEAD
git status --short
```

Record the exact SHA. A dirty tree is not automatically forbidden, but unexplained changes in the validator, tests, fixtures, workflow, or imported modules are a `HOLD` until separated or reviewed.

### Required paths

```text
tools/validators/domains/fauna/validate_public_safe_fixture.py
tests/domains/fauna/test_fauna_smoke.py
fixtures/domains/fauna/README.md
fixtures/domains/fauna/valid/non_sensitive_occurrence.json
fixtures/domains/fauna/valid/sensitive_withheld_occurrence.json
fixtures/domains/fauna/invalid/missing_source_descriptor.json
fixtures/domains/fauna/invalid/unresolved_taxonomy.json
fixtures/domains/fauna/invalid/unresolved_governance.json
fixtures/domains/fauna/invalid/over_precise_sensitive.json
fixtures/domains/fauna/invalid/encoded_location_clue.json
.github/workflows/domain-fauna.yml
```

### Credential and input preflight

- Remove source-specific credentials from the test environment.
- Do not copy real upstream payloads into fixture directories.
- Do not add real coordinates to demonstrate rejection.
- Do not use a live source or production registry to resolve fixture references.
- Do not point the validator at RAW, WORK, QUARANTINE, PROCESSED, CATALOG, proof, release, or published paths.
- Confirm no overlapping open pull request owns the same target, validator, tests, fixtures, or workflow.

### Stop conditions

Return `HOLD` without running when:

- the exact fixture inventory cannot be established;
- any fixture may contain real or reconstructable protected detail;
- the validator/test import path differs from the pinned profile and the change is unexplained;
- source credentials or production endpoints are required;
- a future change adds network-capable code without a reviewed guard;
- the expected valid/invalid polarity is unknown;
- the branch head changes after results are collected; or
- an overlapping change makes the evidence snapshot stale.

[Back to top](#top)

---

## 7. Primary suite procedure

### Step 1 — Set the bounded environment

```bash
export KFM_NO_NETWORK=1
export PYTHONDONTWRITEBYTECODE=1
export PYTHONHASHSEED=0
export PYTHONUNBUFFERED=1
export TZ=UTC
```

No dependency installation is required for the accepted slice; the validator and tests use the Python standard library.

### Step 2 — Run the accepted test module

```bash
python -m unittest discover \
  --start-directory tests/domains/fauna \
  --pattern 'test_fauna_smoke.py' \
  --verbose
```

Expected local result: eight tests pass. Record the exact command, Python version, repository SHA, start/end time, and complete exit status.

### Step 3 — Optional direct validator diagnostics

Positive fixtures must exit `0`:

```bash
python tools/validators/domains/fauna/validate_public_safe_fixture.py \
  fixtures/domains/fauna/valid/non_sensitive_occurrence.json \
  fixtures/domains/fauna/valid/sensitive_withheld_occurrence.json
```

Negative fixtures must exit `1`. Treat that nonzero result as expected rejection:

```bash
if python tools/validators/domains/fauna/validate_public_safe_fixture.py \
  fixtures/domains/fauna/invalid/missing_source_descriptor.json \
  fixtures/domains/fauna/invalid/unresolved_taxonomy.json \
  fixtures/domains/fauna/invalid/unresolved_governance.json \
  fixtures/domains/fauna/invalid/over_precise_sensitive.json \
  fixtures/domains/fauna/invalid/encoded_location_clue.json; then
  echo "ERROR: negative Fauna fixtures unexpectedly passed"
  exit 1
else
  echo "Expected: negative Fauna fixtures were rejected"
fi
```

The unit suite—not ad hoc visual inspection—is the accepted regression proof because it checks exact finding sets and suppresses sensitive values from CLI output.

### Step 4 — Inspect the exact diff

```bash
git diff --check
git diff -- \
  docs/runbooks/fauna/NO_NETWORK_TEST_RUNBOOK.md \
  tools/validators/domains/fauna/validate_public_safe_fixture.py \
  tests/domains/fauna/test_fauna_smoke.py \
  fixtures/domains/fauna \
  .github/workflows/domain-fauna.yml
```

For a documentation-only change, the executable paths should normally be unchanged. Any executable delta expands the review boundary and requires its own validation evidence.

### Step 5 — Bind hosted evidence to the exact head

After pushing the feature branch or opening the pull request:

1. record the exact branch-head SHA;
2. confirm the `domain-fauna / validate-fauna` job ran for that head;
3. distinguish `build-proof-fauna` and `publish-dry-run-fauna` held-success jobs from implemented proof or release;
4. record all other required or repository-wide checks separately;
5. classify failures as introduced, inherited, infrastructure, or unresolved; and
6. rerun or refresh evidence whenever the head changes.

A green check on an older SHA is stale evidence.

[Back to top](#top)

---

## 8. Results, findings, and CI interpretation

### Primary validator outcome

The fixture validator emits one JSON line per file:

```json
{
  "file": "fixtures/domains/fauna/valid/non_sensitive_occurrence.json",
  "findings": [],
  "outcome": "PASS",
  "scope": "synthetic-public-safe-fixture-only"
}
```

A file with one or more findings emits `FAIL` and the CLI exits `1` if any supplied file fails.

**Do not translate this result into `ANSWER`, `ABSTAIN`, `DENY`, or a production `ERROR` envelope.** The proposal-era runbook asserted that broader finite-outcome path, but the accepted fixture-hygiene validator emits only diagnostic `PASS` / `FAIL`. Policy/runtime outcomes remain separate future or adjacent profiles.

### Stable finding families

| Family | Meaning in this profile |
|---|---|
| `*_MISSING`, `*_INVALID`, `*_UNRESOLVED` | required synthetic fixture state is absent or invalid |
| `UNDECLARED_*_FIELD` | closed fixture shape contains an undeclared field |
| `PRECISE_LOCATION_FIELD_FORBIDDEN` | location-bearing key or alias appears |
| `LOCATION_NUMERIC_VALUE_FORBIDDEN` | finite numeric value appears below a location-like key |
| `LIVE_URL_FORBIDDEN` | URL-like text appears after bounded normalization |
| `COORDINATE_PATTERN_FORBIDDEN` | free text resembles a coordinate pair |
| `CONTROL_CHARACTER_FORBIDDEN` | text contains disallowed control characters |
| `PUBLIC_CAVEAT*` | caveat container, count, item, or length is unsafe |
| `DOCUMENT_*` | cycle, depth, or node-bound violation |
| `FIXTURE_*` | file size, parse, identifier, or fixture-only boundary failure |

### Evidence axes that must remain separate

| Axis | Example | What it does not prove |
|---|---|---|
| File presence | fixture and test are tracked | execution or correctness |
| Local execution | eight tests pass at one SHA | hosted status or review |
| Hosted workflow | `validate-fauna` passes at exact head | source admission, policy, proof, release, or publication |
| Held workflow job | proof/release hold conditions remain intact | implemented producer or dry run |
| Human review | reviewer approves documentation/implementation | release or publication unless the owning release process grants it |
| Merge | bytes enter `main` | lifecycle promotion, deployment, or public exposure |

### Introduced versus inherited findings

For every failing check, record:

- check/workflow/job name;
- tested head SHA;
- failing test or command;
- changed paths implicated by the failure;
- whether the same failure exists on current base;
- classification: `INTRODUCED`, `INHERITED`, `INFRASTRUCTURE`, or `NEEDS VERIFICATION`;
- smallest correction or follow-up.

A docs-only change must not be blamed for an unrelated repository failure without evidence, and an unrelated baseline failure must not be used to hide a changed-document defect.

[Back to top](#top)

---

## 9. Sensitivity, geoprivacy, and public safety

Fauna remains a deny-by-default sensitive domain. Exact or reconstructable locations for sensitive taxa and sites can enable disturbance, collection, poaching, habitat damage, or re-identification.

### Fixture rules

- Use toy identifiers, toy taxa, synthetic references, and withheld spatial support.
- Prefer no geometry.
- Never use a real location in an “invalid” fixture.
- Do not encode location clues in URLs, labels, free text, timestamps, source identifiers, or joins.
- Do not include operational transform radii, offsets, masks, seeds, suppression thresholds, or reviewer-only details in public test prose.
- Keep sensitive-withheld fixtures explicitly unreleased and promotion-ineligible.
- Treat the synthetic redaction-receipt reference as a test declaration only; it does not prove a transform occurred.
- Keep logs value-safe: findings may name a code and path but must not echo protected content.

### Representation boundary

Client-side style filters, hidden fields, coarse zoom, missing popups, or model refusal are not geoprivacy controls. Sensitive material must be transformed, withheld, or denied before it reaches a public carrier, and any real transform requires its owning policy, receipt, review, release, correction, and rollback support.

### Cross-domain joins

A fixture that is harmless alone may become identifying when joined with habitat, hydrology, land, infrastructure, imagery, telemetry, or time. This primary suite does not prove reconstruction resistance across joins. Such work remains held for dedicated policy and validator profiles.

[Back to top](#top)

---

## 10. Failure diagnosis and classification

| Symptom | Likely cause | Required response |
|---|---|---|
| Import or path failure | checkout is not repository root, path moved, or branch is stale | stop; verify exact revision and current placement |
| Network-guard assertion fires | validator or imported code attempted a patched socket/URL path | `DENY`; remove or isolate network behavior before retry |
| Positive fixture gains findings | profile, fixture, or validator meaning drifted | classify the exact finding; do not weaken the validator to restore green |
| Negative fixture passes | fail-closed rule or expected inventory regressed | `FAIL`; restore rejection or document/review an intentional profile change |
| Inventory test fails | JSON fixture added, removed, moved, or renamed silently | inspect consumer and review scope; update inventory only with explicit acceptance |
| Sensitive-withheld fixture fails | synthetic transform ref, geoprivacy state, or caveat is missing/mismatched | restore the closed fixture declaration; do not substitute real detail |
| CLI prints protected value | value-safe serialization regressed | stop, contain logs, correct output, and assess exposure before continuing |
| `DOCUMENT_*` or `FIXTURE_*` finding | bounded structural or parse limit triggered | inspect test-only shape; do not raise limits casually |
| Proof/release held job starts finding implementation | repository maturity changed | stop and replace the hold only through a separately reviewed producer/dry-run slice |
| Unrelated repository check fails | inherited baseline or infrastructure issue may exist | compare exact base/head evidence; classify truthfully |
| Head changes after validation | evidence is stale | rerun the changed-area and hosted checks at the new head |

Do not “fix” a failing sensitive-location test by removing a negative fixture, adding a broad allowlist, weakening closed-field checks, suppressing findings, or relabeling real material as synthetic.

[Back to top](#top)

---

## 11. Review handoff

A review packet should contain:

```text
runbook: docs/runbooks/fauna/NO_NETWORK_TEST_RUNBOOK.md
runbook_version: v0.2
base_sha: <immutable base>
head_sha: <immutable head>
target_prior_blob: 1eb1bebe8527fa30041caa04e97cc7efc9869b0a
profile: synthetic-public-safe-fixture-only
python_version: <exact version>
command: python -m unittest discover --start-directory tests/domains/fauna --pattern test_fauna_smoke.py --verbose
local_result: PASS | FAIL | NOT_RUN
hosted_result: PASS | FAIL | PENDING | NOT_TRIGGERED
accepted_fixture_count: 7
accepted_test_count: 8
introduced_findings: <none or exact list>
inherited_findings: <none or exact list>
proof_status: HOLD
release_dry_run_status: HOLD
functional_review: NEEDS VERIFICATION
release_effect: none
publication_effect: none
```

### Review burden

- `@bartytime4life` is the verified GitHub review route.
- Fauna-domain, taxonomy, source, rights, sensitivity/geoprivacy, evidence, policy, test, review, proof, release, correction, rollback, and security assignments remain `NEEDS VERIFICATION`.
- CODEOWNERS routing does not appoint a qualified wildlife steward, rights holder, sensitivity reviewer, independent approver, policy authority, or release authority.
- A documentation review may approve this runbook's accuracy without approving any source, policy, occurrence, transform, proof, release, or public use.

Keep the pull request draft while exact-head checks or material functional review remain unresolved. Draft status, review approval, merge, release, deployment, promotion, and publication are separate states.

[Back to top](#top)

---

## 12. Correction, document rollback, and recovery

### Before merge

- correct the branch in place when the scope remains this one document;
- abandon or close the draft pull request if the evidence basis is invalid;
- do not mutate `main`, fixtures, validators, tests, policy, proof, release, or public state to compensate for a documentation defect.

### After an authorized merge

Revert the focused documentation commit or restore prior blob:

```text
path: docs/runbooks/fauna/NO_NETWORK_TEST_RUNBOOK.md
prior_blob: 1eb1bebe8527fa30041caa04e97cc7efc9869b0a
```

That rollback restores the prior text only. It does not undo a test run, source access, lifecycle transition, policy decision, review, release, deployment, promotion, publication, correction, withdrawal, cache invalidation, or operational rollback.

### Sensitive-material incident

If real or reconstructable protected Fauna material enters a fixture, log, issue, pull request, artifact, or public surface:

1. stop normal handling and avoid copying the value into additional systems;
2. use the appropriate restricted incident and repository-security process;
3. identify affected commits, branches, logs, artifacts, caches, mirrors, and consumers without repeating the detail publicly;
4. obtain qualified sensitivity, rights, security, correction, and release review;
5. correct or remove the exposure through the owning process;
6. preserve an auditable public-safe record of the action; and
7. do not assume a Git revert erases already exposed bytes.

[Back to top](#top)

---

## 13. Current holds and open verification

| Item | Current state | Evidence needed to graduate |
|---|---|---|
| Accountable functional owners and independent review | `NEEDS VERIFICATION` | approved assignments and separation-of-duties record |
| OS/container-level no-network enforcement | `NEEDS VERIFICATION` | accepted sandbox profile plus negative proof at exact revision |
| Active Fauna policy bundle and evaluator | `HOLD` | accepted input/output contract, bundle digest, selector, evaluator, native tests, consumers, and obligation handlers |
| Source admission and rights currency | `HOLD` | admitted SourceDescriptors, rights review, cadence, authority, sensitivity, and resolver evidence |
| Production taxonomic authority | `HOLD` | accepted taxonomy source/crosswalk contract, validators, evidence, review, correction, and replay |
| Real geoprivacy transformation | `HOLD` | accepted transform policy, deterministic implementation, public-safe fixtures, receipts, reviewer authority, and negative reconstruction tests |
| `EvidenceRef` → `EvidenceBundle` closure | `HOLD` | accepted resolver, bundle contract/schema, fixtures, proof, and governed consumer |
| Production occurrence/public schemas | `HOLD` | accepted semantic and machine profile with migration, compatibility, tests, and policy binding |
| Proof producer | `HOLD` | accepted producer, schema, validator, fixtures, access controls, receipt linkage, and exact-head workflow |
| Release dry run and candidate contract | `HOLD` | immutable candidate identity, evidence/policy/review closure, correction/withdrawal/rollback target, and non-public rehearsal |
| Public API/UI/tile/Focus consumers | `UNKNOWN / HOLD` | governed-interface implementation with released fixtures and negative exposure tests |
| Local `docs/runbooks/fauna/README.md` boundary | `HOLD` | repository-grounded lane README and parent-index reconciliation |
| Required-check coupling | `NEEDS VERIFICATION` | current ruleset evidence linking exact check names to branch requirements |
| Hosted checks for this change | `NEEDS VERIFICATION` until PR head settles | exact-head workflow and check-suite evidence |

Do not turn an open item into a repo fact by documenting a proposed path or command.

[Back to top](#top)

---

## 14. Related surfaces

### Governing documentation

- [Runbook index](../README.md)
- [Local Fauna runbook lane placeholder](./README.md)
- [Directory Rules](../../doctrine/directory-rules.md)
- [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
- [Fauna domain README](../../domains/fauna/README.md)
- [Fauna sensitivity and geoprivacy](../../domains/fauna/SENSITIVITY.md)
- [Fauna policy explanation](../../domains/fauna/POLICY.md)
- [Fauna source refresh runbook](./SOURCE_REFRESH_RUNBOOK.md)
- [Fauna promotion runbook](./PROMOTION_RUNBOOK.md)
- [Fauna rollback runbook](./ROLLBACK_RUNBOOK.md)

### Executable and governed boundaries

- [Fauna fixtures](../../../fixtures/domains/fauna/README.md)
- [Fauna domain tests](../../../tests/domains/fauna/README.md)
- [Primary smoke tests](../../../tests/domains/fauna/test_fauna_smoke.py)
- [Fauna validator index](../../../tools/validators/domains/fauna/README.md)
- [Primary fixture validator](../../../tools/validators/domains/fauna/validate_public_safe_fixture.py)
- [Fauna domain policy](../../../policy/domains/fauna/README.md)
- [Fauna sensitivity policy](../../../policy/sensitivity/fauna/README.md)
- [Fauna source registry](../../../data/registry/sources/fauna/README.md)
- [Fauna proof lane](../../../data/proofs/fauna/README.md)
- [Fauna release candidates](../../../release/candidates/fauna/README.md)
- [Fauna domain workflow](../../../.github/workflows/domain-fauna.yml)
- [OccurrenceEvidence workflow](../../../.github/workflows/fauna-occurrence-evidence.yml)
- [Tile-field allowlist workflow](../../../.github/workflows/fauna-tile-field-allowlist.yml)

[Back to top](#top)

---

## 15. Change log

| Version | Date | Change | Effect |
|---|---|---|---|
| `v0.2` | 2026-08-24 | Replaced planning-only repo assumptions, fictional directory trees, broad unproved trust-spine claims, and illustrative runner commands with the current seven-fixture/eight-test bounded executable; documented adjacent profiles, exact commands, sensitivity limits, CI interpretation, holds, handoff, and documentation rollback. | Documentation only; no executable, source, policy, lifecycle, proof, release, deployment, promotion, or publication effect. |
| `v0.1` | 2026-05-13 | Initial proposal-era no-network trust-spine runbook. | Historical planning state. |

Re-review this runbook when the fixture inventory, validator, tests, workflows, policy activation, source registry, proof/release holds, public consumers, owners, required checks, or sensitive-location posture changes.

[Back to top](#top)
