<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-epa-tests-readme
title: EPA connector tests README
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — connector steward · source steward · validation steward
created: 2026-06-18
updated: 2026-06-18
policy_label: public
proposed_path: connectors/epa/tests/README.md
truth_posture: CONFIRMED doctrine / PROPOSED local test contract / UNKNOWN live repo implementation
related:
  - connectors/epa/README.md
  - tests/README.md
  - fixtures/README.md
  - data/registry/sources/README.md
  - docs/doctrine/directory-rules.md
  - docs/doctrine/trust-membrane.md
  - docs/doctrine/lifecycle-law.md
  - docs/sources/catalog/epa.md
  - schemas/contracts/v1/source/
  - policy/sensitivity/
tags:
  - kfm
  - connectors
  - epa
  - tests
  - source-admission
  - validation
  - fixtures
  - receipts
notes:
  - "This README is connector-local guidance. It does not replace root tests/, root fixtures/, source descriptors, schemas, policy, release gates, or governed publication decisions."
  - "Commands, object names, and adjacent paths are PROPOSED until verified against the mounted repository."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# EPA Connector Tests

![status](https://img.shields.io/badge/status-draft-yellow?style=flat-square)
![scope](https://img.shields.io/badge/scope-connector--local-blue?style=flat-square)
![network](https://img.shields.io/badge/network-off_by_default-critical?style=flat-square)
![truth](https://img.shields.io/badge/truth-CONFIRMED%20%2F%20PROPOSED%20%2F%20UNKNOWN-lightgrey?style=flat-square)
![publication](https://img.shields.io/badge/publication-not_a_publisher-orange?style=flat-square)

> **One-line purpose.** Keep the EPA connector test surface small, deterministic, no-network by default, and aligned with KFM source-admission governance: connectors may fetch or admit source material, but they do not validate truth, promote records, publish artifacts, or bypass policy.

---

## Mini table of contents

- [1. Status and evidence boundary](#1-status-and-evidence-boundary)
- [2. Placement and responsibility](#2-placement-and-responsibility)
- [3. What these tests are allowed to prove](#3-what-these-tests-are-allowed-to-prove)
- [4. What does not belong here](#4-what-does-not-belong-here)
- [5. Test classes](#5-test-classes)
- [6. Fixture and mock-data rules](#6-fixture-and-mock-data-rules)
- [7. No-network default](#7-no-network-default)
- [8. Expected local layout](#8-expected-local-layout)
- [9. Running the tests](#9-running-the-tests)
- [10. Acceptance checklist](#10-acceptance-checklist)
- [11. Failure handling](#11-failure-handling)
- [12. Review and rollback](#12-review-and-rollback)
- [13. Verification backlog](#13-verification-backlog)

---

## 1. Status and evidence boundary

| Claim | Status | Meaning |
|---|---:|---|
| KFM doctrine requires source material to move through the trust membrane before publication. | **CONFIRMED doctrine** | The connector test plan preserves `RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED`. |
| `connectors/` is the responsibility root for source-specific fetchers and admitters. | **CONFIRMED doctrine** | This README treats EPA as a source family under the connector root, not as a domain root. |
| `connectors/epa/tests/` exists in the live repo and is wired into CI. | **UNKNOWN** | No mounted repository, workflow run, or CI result was inspected while drafting this README. |
| The commands in this README are runnable as written. | **NEEDS VERIFICATION** | Validate against the mounted repo’s Python environment, package manager, Makefile, and CI workflow. |
| EPA source endpoints, schemas, terms, and limits are current. | **NEEDS VERIFICATION** | Source activation must be checked by source stewards before live use. |

This file is useful as a connector-local contract even before implementation is complete. It should not be cited as proof that the EPA connector exists, is complete, is rights-cleared, or is production-ready.

---

## 2. Placement and responsibility

`connectors/epa/tests/README.md` is a **connector-local README**. Its job is to explain the tests that live beside the EPA connector implementation.

**Directory placement basis:**

| Path segment | Responsibility |
|---|---|
| `connectors/` | Source-specific fetchers and admitters. |
| `epa/` | EPA source-family lane. EPA is a source family, not a KFM domain. |
| `tests/` | Connector-adjacent tests for local fetch/admission behavior. |
| `README.md` | Human-facing explanation of the local test contract. |

> [!IMPORTANT]
> This folder must not become a second canonical `tests/` root. Cross-connector, contract, policy, release, integration, and end-to-end tests belong in the repo-wide testing structure. This folder may hold connector-local unit tests, adapter contract tests, mock response tests, and source-admission smoke tests only.

---

## 3. What these tests are allowed to prove

EPA connector-local tests should prove that the connector behaves safely at the **source-admission edge**.

They may verify:

- the connector can parse its own local configuration without secrets in source control;
- source descriptors or source references are required before live fetch behavior is enabled;
- network access is disabled by default in normal test runs;
- mocked EPA responses are parsed into bounded connector outputs;
- deterministic IDs, retrieval metadata, checksums, timestamps, and source labels are emitted where the connector contract requires them;
- connector outputs are shaped for `data/raw/` or `data/quarantine/` admission paths, not direct publication;
- failed fetches produce finite error outcomes instead of partial silent success;
- rights, source terms, sensitivity, and freshness signals are carried forward for later policy gates;
- malformed, partial, stale, oversized, or unexpected responses fail closed;
- retry and rate-limit behavior is bounded and testable without live endpoint pressure.

They must not claim that EPA-derived facts are true. Truth support belongs to EvidenceBundle resolution, validation, review, policy, catalog closure, and release gates downstream.

---

## 4. What does not belong here

Do not put these in `connectors/epa/tests/`:

| Do not place here | Correct home or next step |
|---|---|
| Golden cross-domain fixtures shared by multiple systems | `fixtures/` or `tests/fixtures/`, per repo convention. |
| Source descriptors or source registry records | `data/registry/sources/` or the current source registry home. |
| Object-family contract docs | `contracts/`. |
| Machine-checkable schemas | `schemas/contracts/v1/`. |
| Policy decisions, source-rights decisions, sensitivity decisions | `policy/`, `release/`, or the relevant review surface. |
| Pipeline transforms that normalize EPA material into domain records | `pipelines/` or `packages/domains/<domain>/`, depending on responsibility. |
| Published outputs, catalogs, proofs, receipts, or release manifests | `data/`, `release/`, or other canonical lifecycle/release homes. |
| Live endpoint credentials or API keys | Never commit. Use local secret management outside the repo. |

---

## 5. Test classes

### 5.1 Contract-shape tests

**Purpose:** Confirm that connector-local outputs match the expected adapter envelope before any downstream pipeline accepts them.

Expected checks:

- required fields are present;
- unknown fields are either rejected or explicitly carried in a quarantine-safe extension field;
- timestamps are timezone-aware or clearly normalized;
- source URL, retrieval time, digest, and source descriptor reference are present when applicable;
- empty payloads produce `ABSTAIN` or `ERROR`, not fake success.

### 5.2 No-network unit tests

**Purpose:** Exercise parser, mapper, and error-handling logic using local mocks only.

Expected checks:

- tests pass with no internet access;
- all HTTP calls are blocked unless a deliberate live-integration flag is set;
- mocked responses include successful, empty, malformed, rate-limited, forbidden, timeout, and changed-schema cases.

### 5.3 Source-admission tests

**Purpose:** Confirm the connector can prepare source material for the KFM lifecycle without skipping governance gates.

Expected checks:

- connector output targets only RAW or QUARANTINE admission;
- no test writes to `data/processed/`, `data/catalog/`, `data/published/`, or `release/`;
- source-role, retrieval metadata, and candidate evidence references are preserved;
- incomplete source-rights or sensitivity context causes quarantine-safe behavior.

### 5.4 Error and drift tests

**Purpose:** Detect source-shape drift early without creating public claims.

Expected checks:

- missing fields fail with actionable messages;
- added fields are either ignored safely or quarantined for review;
- changed units, geometry fields, time fields, or identifiers are surfaced as `NEEDS VERIFICATION`;
- repeated failures can emit a candidate drift note without promoting data.

### 5.5 Optional live smoke tests

**Purpose:** Verify that a steward-approved EPA endpoint is reachable and still resembles the expected source shape.

Default posture:

- skipped unless explicitly enabled;
- never runs in default unit-test CI;
- never requires secrets committed to the repo;
- emits no publication artifacts;
- records enough metadata for review without storing sensitive or excessive response bodies.

---

## 6. Fixture and mock-data rules

Use small, reviewable, artificial or minimized fixtures. Do not copy large EPA payloads into the repo unless source terms, size, provenance, and review state allow it.

Fixture rules:

1. Prefer synthetic fixtures that preserve shape but not unnecessary source volume.
2. Preserve source field names only when needed to test parser behavior.
3. Include at least one valid fixture and several invalid fixtures.
4. Record whether a fixture is synthetic, minimized, redacted, or copied from a real source response.
5. Store shared fixtures in the repo’s fixture authority, not in multiple competing fixture homes.
6. Do not include secrets, personal data, restricted location detail, or raw response dumps without review.

Recommended fixture metadata fields:

```yaml
fixture_id: epa-example-valid-001
fixture_status: synthetic
source_family: epa
supports_tests:
  - parser_valid_shape
  - source_admission_envelope
rights_posture: non-authoritative-test-fixture
sensitivity_posture: public_safe_synthetic
created: 2026-06-18
review_state: draft
```

---

## 7. No-network default

> [!CAUTION]
> Live EPA calls must be opt-in. Default tests should pass on a plane, in CI, and in a no-network sandbox.

Expected controls:

- no live endpoint access unless `KFM_ALLOW_LIVE_EPA_TESTS=1` or the repo’s approved equivalent is set;
- no live integration tests unless a source descriptor or source registry entry is present and reviewable;
- no credential-bearing test output;
- no auto-update of fixtures from live endpoints;
- no promotion, catalog write, or release write from connector tests.

Suggested skip condition, subject to repo test framework verification:

```python
pytestmark = pytest.mark.skipif(
    os.getenv("KFM_ALLOW_LIVE_EPA_TESTS") != "1",
    reason="Live EPA tests are opt-in and disabled by default.",
)
```

---

## 8. Expected local layout

This layout is **PROPOSED** until checked against the mounted repository.

```text
connectors/epa/tests/
├── README.md
├── test_config.py                  # PROPOSED: local config parsing and safety defaults
├── test_parser.py                  # PROPOSED: mocked EPA payload parsing
├── test_admission_envelope.py      # PROPOSED: connector output envelope checks
├── test_errors.py                  # PROPOSED: malformed/rate-limited/timeout cases
├── test_no_network_default.py      # PROPOSED: blocks accidental live calls
└── live/
    └── test_live_smoke.py          # OPTIONAL / SKIPPED BY DEFAULT
```

Shared fixture candidates should be placed in the repository’s fixture authority after inspection. If local fixtures are temporarily needed, keep them minimal and clearly marked as connector-local.

---

## 9. Running the tests

The exact command is **NEEDS VERIFICATION** against the mounted repo.

Likely local command:

```bash
python -m pytest connectors/epa/tests
```

Likely no-network CI command:

```bash
KFM_ALLOW_LIVE_EPA_TESTS=0 python -m pytest connectors/epa/tests
```

Optional live smoke command, only after source-steward approval:

```bash
KFM_ALLOW_LIVE_EPA_TESTS=1 python -m pytest connectors/epa/tests/live
```

If the repo provides `make test`, `make test-connectors`, `uv run`, `poetry run`, `tox`, `nox`, or another test runner, prefer the repo-standard command and update this section.

---

## 10. Acceptance checklist

A PR touching EPA connector tests should satisfy this checklist before review:

- [ ] Default test run performs no live network calls.
- [ ] Live smoke tests are isolated and skipped by default.
- [ ] No secrets, credentials, tokens, or private URLs are committed.
- [ ] Tests do not write to `data/processed/`, `data/catalog/`, `data/published/`, or `release/`.
- [ ] Tests preserve source metadata needed for downstream evidence and policy checks.
- [ ] Malformed or incomplete source responses fail closed.
- [ ] Source-rights and sensitivity uncertainty is represented as `NEEDS VERIFICATION`, `ABSTAIN`, `DENY`, or quarantine-safe behavior.
- [ ] Shared fixtures are not duplicated across competing fixture homes.
- [ ] Any live endpoint assumption is documented and reviewable.
- [ ] The root-level test or CI entry point is updated if these tests are meant to run automatically.

---

## 11. Failure handling

Use finite, reviewable outcomes. Do not let connector failures degrade into ambiguous parser exceptions or partial data writes.

| Situation | Expected outcome |
|---|---|
| Source descriptor missing | `ABSTAIN` or test failure with actionable message. |
| Source terms or rights unclear | Quarantine-safe output; no promotion. |
| Unexpected schema change | `NEEDS VERIFICATION`; drift note candidate. |
| HTTP timeout or rate limit | Bounded retry result; no partial success. |
| Empty response | `ABSTAIN` unless empty is explicitly valid for that source. |
| Malformed response | `ERROR` with source metadata preserved where safe. |
| Sensitive field detected | `DENY` or quarantine/generalization path, depending on policy. |
| Live test accidentally enabled in CI | Fail fast unless CI explicitly authorizes live smoke tests. |

---

## 12. Review and rollback

Connector test changes are reversible when they are small, isolated, and do not rewrite shared test infrastructure unnecessarily.

Review notes:

- Keep connector-local changes local.
- Move shared helpers to `tools/`, `packages/`, or root `tests/` only after the pattern is reused.
- Record fixture lineage when adding or replacing mock payloads.
- Update this README when test classes, fixture location, or live-smoke posture changes.

Rollback path:

1. Revert the connector-local test change.
2. Remove new connector-local fixtures that are no longer referenced.
3. Restore prior skip/default-network behavior.
4. Re-run the repo-standard no-network test command.
5. If a source-shape drift issue triggered the change, keep or update the drift/verification record rather than deleting the signal.

---

## 13. Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm `connectors/epa/` implementation layout. | **NEEDS VERIFICATION** | Mounted repo tree. |
| Confirm test runner and dependency manager. | **NEEDS VERIFICATION** | `pyproject.toml`, Makefile, CI workflow, or equivalent. |
| Confirm root fixture authority. | **NEEDS VERIFICATION** | `fixtures/README.md`, `tests/README.md`, and current repo convention. |
| Confirm EPA source descriptor home and naming. | **NEEDS VERIFICATION** | Source registry and source catalog docs. |
| Confirm live smoke-test policy. | **NEEDS VERIFICATION** | CI policy, source steward decision, and secret-management posture. |
| Confirm expected connector output envelope. | **NEEDS VERIFICATION** | Contracts and schemas for source/admission envelopes. |
| Confirm whether EPA feeds include sensitive or restricted fields for the selected source family. | **NEEDS VERIFICATION** | Source descriptor, sensitivity policy, and steward review. |

---

## Maintainer note

This README should make the EPA connector safer to build, not heavier to maintain. Keep the local test surface focused on source-admission behavior. Promote shared rules upward only when multiple connectors need them, and keep publication authority downstream of evidence, policy, validation, review, release, and rollback.
