<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-familysearch-tests-readme
title: FamilySearch connector tests README
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Source steward · People/DNA/Land steward · Sensitivity reviewer · Validation steward · Docs steward
created: 2026-06-18
updated: 2026-06-18
policy_label: public-doctrine
proposed_path: connectors/familysearch/tests/README.md
truth_posture: CONFIRMED path exists / PROPOSED local test contract / UNKNOWN implementation depth
related:
  - ../README.md
  - ../../README.md
  - ../../../docs/sources/catalog/familysearch/README.md
  - ../../../docs/domains/people-dna-land/README.md
  - ../../../docs/domains/people-dna-land/SOURCE_REGISTRY.md
  - ../../../data/registry/sources/people-genealogy-dna-land/
  - ../../../data/raw/people-dna-land/
  - ../../../data/quarantine/people-dna-land/
  - ../../../fixtures/
  - ../../../schemas/contracts/v1/source/
  - ../../../policy/genealogy/publication.rego
  - ../../../policy/sensitivity/
  - ../../../release/
tags: [kfm, connectors, familysearch, tests, genealogy, people-dna-land, consent, living-person, source-admission, validation, fixtures, quarantine]
notes:
  - "This README is connector-local test guidance. It does not replace root tests/, fixture authority, source descriptors, schemas, policy, release gates, or governed publication decisions."
  - "FamilySearch tests must be no-network by default and must not require private account access, credentials, or living-person payloads."
  - "Connector tests may prove safe source-admission behavior only; they do not prove family relationships, person identity, consent validity, or publication eligibility."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# FamilySearch Connector Tests

![status](https://img.shields.io/badge/status-draft-yellow?style=flat-square)
![scope](https://img.shields.io/badge/scope-connector--local-blue?style=flat-square)
![network](https://img.shields.io/badge/network-off_by_default-critical?style=flat-square)
![sensitivity](https://img.shields.io/badge/sensitivity-living--person_DENY--by--default-critical?style=flat-square)
![truth](https://img.shields.io/badge/truth-CONFIRMED%20%2F%20PROPOSED%20%2F%20UNKNOWN-lightgrey?style=flat-square)

> **One-line purpose.** Keep FamilySearch connector tests deterministic, no-network by default, privacy-preserving, and limited to source-admission behavior. Tests may verify connector safety; they must not validate genealogy truth or public-release eligibility.

---

## Mini table of contents

- [1. Status and evidence boundary](#1-status-and-evidence-boundary)
- [2. Placement and responsibility](#2-placement-and-responsibility)
- [3. What these tests are allowed to prove](#3-what-these-tests-are-allowed-to-prove)
- [4. What does not belong here](#4-what-does-not-belong-here)
- [5. Test classes](#5-test-classes)
- [6. Fixture and mock-data rules](#6-fixture-and-mock-data-rules)
- [7. No-network and no-account default](#7-no-network-and-no-account-default)
- [8. Living-person and consent gates](#8-living-person-and-consent-gates)
- [9. Expected local layout](#9-expected-local-layout)
- [10. Running the tests](#10-running-the-tests)
- [11. Acceptance checklist](#11-acceptance-checklist)
- [12. Failure handling](#12-failure-handling)
- [13. Review and rollback](#13-review-and-rollback)
- [14. Verification backlog](#14-verification-backlog)

---

## 1. Status and evidence boundary

| Claim | Status | Meaning |
|---|---:|---|
| KFM doctrine treats living-person, DNA-derived, and private person-place material as denied or restricted by default. | **CONFIRMED doctrine from visible repo docs** | FamilySearch test design must assume private genealogy material is sensitive unless proven otherwise. |
| `connectors/familysearch/tests/README.md` exists in the live repo. | **CONFIRMED** | The prior content was a greenfield stub before this update. |
| `connectors/familysearch/tests/` is wired into CI. | **UNKNOWN** | No workflow run, test log, or CI configuration was verified in this update. |
| The exact pytest command is runnable as written. | **NEEDS VERIFICATION** | Confirm against the repo’s package manager, test runner, and workflow files. |
| FamilySearch live endpoint behavior, OAuth behavior, rate limits, terms, and revocation semantics are current. | **NEEDS VERIFICATION** | Source steward and security review are required before any live test. |

This README is a connector-local test contract. It is not evidence that the FamilySearch connector is implemented, source-activated, rights-cleared, consent-ready, or safe for publication.

---

## 2. Placement and responsibility

`connectors/familysearch/tests/README.md` explains the tests that live beside the FamilySearch connector implementation.

| Path segment | Responsibility |
|---|---|
| `connectors/` | Source-specific fetchers and admitters. |
| `familysearch/` | FamilySearch source-family connector lane. |
| `tests/` | Connector-local tests for safe intake, parsing, privacy gating, and source-admission behavior. |
| `README.md` | Human-facing explanation of the local test contract. |

> [!IMPORTANT]
> This folder must not become a second canonical `tests/` root. Cross-domain, contract, policy, release, consent, integration, and end-to-end tests belong in the repo-wide testing and governance structures. This folder may hold connector-local unit tests, adapter contract tests, mock response tests, and source-admission smoke tests only.

---

## 3. What these tests are allowed to prove

FamilySearch connector-local tests should prove that the connector behaves safely at the source-admission edge.

They may verify:

- imports do not perform network calls;
- live or account-mediated access is disabled by default;
- credentials, OAuth tokens, cookies, and session material are never required for default tests;
- mocked FamilySearch-like payloads parse into bounded connector outputs;
- person, relationship, event, place, and citation fragments stay candidate assertions;
- living-person indicators route to `DENY`, quarantine, or review-required behavior;
- source references, retrieval metadata, contributor/source labels, timestamps, and digests are preserved where applicable;
- malformed, partial, empty, private, rights-unclear, or schema-drift payloads fail closed;
- connector outputs target RAW or QUARANTINE handoff only;
- no test creates public claims, release artifacts, proof packs, catalog records, or person-identity merges.

They must not claim that a person identity, relationship, date, place, land connection, or family-tree assertion is true.

---

## 4. What does not belong here

Do not put these in `connectors/familysearch/tests/`:

| Do not place here | Correct home or next step |
|---|---|
| Real account tokens, OAuth secrets, cookies, session exports | Never commit; use approved secret management only. |
| Raw private genealogy exports | Quarantine only after source, rights, consent, and retention review. |
| Living-person fixtures | Avoid; use synthetic fixtures unless sensitivity review approves otherwise. |
| DNA matches, raw DNA segment data, or DNA-derived hypotheses | Out of connector tests by default; require separate deny-by-default policy review. |
| Shared golden fixtures used by multiple systems | `fixtures/` or repo-approved fixture authority. |
| Source descriptors | `data/registry/sources/...` or accepted source registry home. |
| Object-family contracts | `contracts/`. |
| Machine-checkable schemas | `schemas/contracts/v1/...` under accepted schema-home convention. |
| Publication policy | `policy/` and release review surfaces. |
| Published outputs, proofs, receipts, release manifests | Lifecycle/release roots, not connector-local tests. |

---

## 5. Test classes

### 5.1 Import-safety tests

**Purpose:** Confirm package import is side-effect safe.

Expected checks:

- importing connector modules performs no HTTP calls;
- importing connector modules does not read credentials;
- default configuration is no-network and no-account;
- missing secrets do not fail parser-only tests.

### 5.2 Parser tests

**Purpose:** Verify that mocked or synthetic source-shaped payloads can be parsed without asserting truth.

Expected checks:

- valid synthetic person payload parses into a candidate record;
- valid synthetic relationship payload remains a candidate relationship;
- citation/source references are preserved;
- date/place/event fields remain source-attributed;
- unknown or unsupported fields are preserved safely or rejected explicitly.

### 5.3 Privacy and consent tests

**Purpose:** Ensure sensitive material fails closed.

Expected checks:

- living-person indicators route to deny/quarantine/review-required behavior;
- consent scope missing or unknown prevents public-safe output;
- revocation or tombstone markers invalidate cached or re-emitted material;
- private account-only markers do not cross into publishable envelopes;
- fixture metadata records whether data is synthetic, minimized, redacted, or approved.

### 5.4 Source-admission envelope tests

**Purpose:** Confirm connector output is suitable for KFM lifecycle admission, not publication.

Expected checks:

- output targets RAW or QUARANTINE only;
- source descriptor reference is required for live activation;
- retrieval metadata, source label, parser version, and digest support are present where applicable;
- uncertainty is represented explicitly;
- no test writes to `data/processed/`, `data/catalog/`, `data/triplets/`, `data/published/`, `data/proofs/`, `data/receipts/`, or `release/`.

### 5.5 Error and drift tests

**Purpose:** Detect source-shape drift or unsafe access failures without creating public claims.

Expected checks:

- malformed payloads produce finite errors;
- empty payloads produce abstention unless explicitly valid;
- changed source shape produces `NEEDS_VERIFICATION`-style drift signal;
- forbidden, unauthorized, timeout, and rate-limit cases do not leak credentials;
- repeated drift can create a review signal, not a publication artifact.

### 5.6 Optional live smoke tests

**Purpose:** Verify a steward-approved source endpoint or sandbox is reachable and resembles expected shape.

Default posture:

- skipped unless explicitly enabled;
- never runs in default CI;
- never uses personal accounts without approved scope;
- never stores private response bodies;
- emits no publication artifacts;
- records only safe metadata needed for steward review.

---

## 6. Fixture and mock-data rules

Use synthetic fixtures by default. FamilySearch-style fixtures should prove parser and privacy behavior without exposing real people.

Fixture rules:

1. Prefer synthetic people, relationships, events, places, and citations.
2. Do not use real living-person details.
3. Do not include real account exports unless sensitivity, rights, retention, and consent review approve them.
4. Do not include DNA data or DNA-derived relationship hints.
5. Mark each fixture as synthetic, minimized, redacted, or copied with approval.
6. Include fixtures for valid, private, living-person, malformed, empty, rights-unclear, revoked, and schema-drift cases.
7. Promote shared fixtures to the repo’s fixture authority instead of duplicating them across connector folders.

Recommended fixture metadata shape:

```yaml
fixture_id: familysearch-synthetic-person-001
fixture_status: synthetic
source_family: familysearch
supports_tests:
  - parser_valid_shape
  - privacy_gate_living_person
  - source_admission_envelope
rights_posture: non-authoritative-test-fixture
sensitivity_posture: public_safe_synthetic
contains_living_person_data: false
contains_dna_data: false
created: 2026-06-18
review_state: draft
```

---

## 7. No-network and no-account default

> [!CAUTION]
> Default tests must require no internet, no FamilySearch account, no OAuth flow, no token, no browser session, and no private export.

Expected controls:

- no live endpoint access unless an approved opt-in flag is set;
- no account-mediated tests unless steward review approves the scope;
- no credentials printed in logs;
- no fixture auto-refresh from live accounts;
- no persistent cache of private account material;
- no promotion, catalog write, proof write, receipt write, or release write from connector tests.

Suggested skip condition, subject to repo convention verification:

```python
pytestmark = pytest.mark.skipif(
    os.getenv("KFM_ALLOW_LIVE_FAMILYSEARCH_TESTS") != "1",
    reason="Live FamilySearch tests are opt-in and disabled by default.",
)
```

---

## 8. Living-person and consent gates

FamilySearch tests must preserve KFM’s strict privacy posture.

Minimum privacy cases:

| Test case | Expected behavior |
|---|---|
| Living-person marker present | `DENY`, quarantine, or review-required result. |
| Consent scope missing | No public-safe output. |
| Revocation marker present | Invalidate or block re-emission. |
| Private account-only source marker | Quarantine or deny-by-default. |
| Relationship assertion without citation | Candidate assertion only; no promotion. |
| Person-place assertion involving a living person | Deny/quarantine by default. |
| DNA-like field appears unexpectedly | Deny/quarantine and drift signal. |

Consent tests must not invent consent. They should verify that missing, expired, revoked, ambiguous, or mismatched consent fails closed.

---

## 9. Expected local layout

This layout is **PROPOSED** until checked against the mounted repository.

```text
connectors/familysearch/tests/
├── README.md
├── test_import_safety.py             # PROPOSED: imports do not trigger network/secrets
├── test_config.py                    # PROPOSED: no-network and no-account defaults
├── test_parser.py                    # PROPOSED: synthetic FamilySearch-like payload parsing
├── test_privacy_gates.py             # PROPOSED: living-person / consent / private markers
├── test_admission_envelope.py        # PROPOSED: RAW/QUARANTINE-only output envelope
├── test_errors.py                    # PROPOSED: malformed/empty/unauthorized/drift cases
└── live/
    └── test_live_smoke.py            # OPTIONAL / SKIPPED BY DEFAULT
```

Shared fixture candidates should be placed in the repository’s fixture authority after inspection. Local fixtures, if used temporarily, must be synthetic or explicitly reviewed.

---

## 10. Running the tests

The exact command is **NEEDS VERIFICATION** against the mounted repo.

Likely local command:

```bash
python -m pytest connectors/familysearch/tests
```

Likely no-network CI command:

```bash
KFM_ALLOW_LIVE_FAMILYSEARCH_TESTS=0 python -m pytest connectors/familysearch/tests
```

Optional live smoke command, only after source-steward and security approval:

```bash
KFM_ALLOW_LIVE_FAMILYSEARCH_TESTS=1 python -m pytest connectors/familysearch/tests/live
```

If the repo provides `make test`, `make test-connectors`, `uv run`, `poetry run`, `tox`, `nox`, or another test runner, prefer the repo-standard command and update this section.

---

## 11. Acceptance checklist

A PR touching FamilySearch connector tests should satisfy this checklist before review:

- [ ] Default test run performs no live network calls.
- [ ] Default test run requires no account, OAuth flow, token, cookie, or private export.
- [ ] Live smoke tests are isolated and skipped by default.
- [ ] No secrets, credentials, tokens, cookies, or private URLs are committed.
- [ ] Fixtures are synthetic, minimized, redacted, or explicitly approved.
- [ ] No real living-person data is committed.
- [ ] No DNA data or DNA-derived hints are committed.
- [ ] Living-person, consent-missing, revoked, private, and rights-unclear cases fail closed.
- [ ] Relationship and person assertions remain candidate assertions.
- [ ] Tests do not write to processed, catalog, triplet, published, proof, receipt, or release stores.
- [ ] Source metadata needed for downstream evidence and policy checks is preserved.
- [ ] Any live endpoint assumption is documented and reviewable.
- [ ] Root-level test or CI entry point is updated if these tests are meant to run automatically.

---

## 12. Failure handling

Use finite, reviewable outcomes. Do not let connector failures degrade into ambiguous parser exceptions, leaked credentials, or partial public outputs.

| Situation | Expected outcome |
|---|---|
| Source descriptor missing | `ABSTAIN` or test failure with actionable message. |
| OAuth token missing | `ABSTAIN`; default tests still pass using fixtures. |
| Unauthorized or forbidden response | `ERROR` without credential leakage. |
| Consent unknown | `DENY` or quarantine-safe behavior. |
| Consent revoked | Block re-emission; require review. |
| Living-person material detected | `DENY` by default unless an approved restricted handoff exists. |
| DNA-like field detected | `DENY` or quarantine plus drift signal. |
| Empty response | `ABSTAIN` unless empty is explicitly valid. |
| Malformed response | `ERROR` with safe source metadata. |
| Unexpected schema change | `NEEDS_VERIFICATION`; drift note candidate. |
| Source terms unclear | `NEEDS_VERIFICATION`; no live activation. |

---

## 13. Review and rollback

Connector test changes are reversible when they remain small, local, and fixture-safe.

Review notes:

- Keep connector-local tests local.
- Move shared helpers upward only when reused by multiple connectors.
- Treat fixture additions as sensitivity-significant changes.
- Update this README when privacy gates, fixture locations, live-smoke posture, or test classes change.
- Do not delete drift signals simply because the connector is not ready.

Rollback path:

1. Revert the connector-local test change.
2. Remove any new local fixtures that are no longer referenced.
3. Restore no-network and no-account defaults.
4. Re-run the repo-standard no-network test command.
5. Preserve or update source-term, consent, or sensitivity drift notes if the change revealed a real governance issue.

---

## 14. Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm `connectors/familysearch/` implementation layout. | **NEEDS VERIFICATION** | Mounted repo tree. |
| Confirm test runner and dependency manager. | **NEEDS VERIFICATION** | `pyproject.toml`, Makefile, CI workflow, or equivalent. |
| Confirm root fixture authority. | **NEEDS VERIFICATION** | `fixtures/README.md`, root `tests/README.md`, and repo convention. |
| Confirm FamilySearch source descriptor home and source ID. | **NEEDS VERIFICATION** | Source registry and source catalog docs. |
| Confirm live smoke-test policy. | **NEEDS VERIFICATION** | Source steward, security reviewer, and CI policy. |
| Confirm consent, revocation, retention, and tombstone policy. | **NEEDS VERIFICATION** | Policy docs and review decisions. |
| Confirm expected connector output envelope. | **NEEDS VERIFICATION** | Contracts and schemas for source/admission envelopes. |
| Confirm People/DNA/Land path segment convention. | **NEEDS VERIFICATION** | Directory Rules, ADRs, and current repo paths. |

---

## Maintainer note

FamilySearch connector tests should prove restraint. A passing test suite should show that the connector can parse and admit source-shaped material safely, while refusing to turn private, living-person, consent-unclear, or weakly supported genealogy material into public KFM truth.
