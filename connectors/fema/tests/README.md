<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-fema-tests-readme
title: FEMA connector tests README
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Source steward · Hazards steward · Hydrology steward · Validation steward · Docs steward
created: 2026-06-18
updated: 2026-06-18
policy_label: public-context-only; not-for-life-safety
proposed_path: connectors/fema/tests/README.md
truth_posture: CONFIRMED path exists / PROPOSED local test contract / UNKNOWN implementation depth
related:
  - ../README.md
  - ../nfhl/README.md
  - ../../fema-nfhl/README.md
  - ../../fema-openfema/README.md
  - ../../../docs/sources/catalog/fema/README.md
  - ../../../docs/sources/catalog/fema/nfhl-flood-hazard.md
  - ../../../docs/sources/catalog/fema/openfema-disaster-declarations.md
  - ../../../docs/sources/catalog/fema/openfema-auxiliary-tables.md
  - ../../../docs/domains/hazards/README.md
  - ../../../docs/domains/hydrology/README.md
  - ../../../data/registry/sources/
  - ../../../data/raw/
  - ../../../data/quarantine/
  - ../../../fixtures/
  - ../../../schemas/contracts/v1/source/
  - ../../../policy/sensitivity/
  - ../../../release/
tags: [kfm, connectors, fema, tests, nfhl, openfema, hazards, hydrology, regulatory-context, administrative-context, aggregate, validation, fixtures, quarantine]
notes:
  - "This README replaces the greenfield stub with connector-local test guidance."
  - "FEMA tests must be no-network by default and must prove source-admission safety only."
  - "Connector tests do not prove observed hazards, current conditions, formal determinations, release readiness, or publication eligibility."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# FEMA Connector Tests

![status](https://img.shields.io/badge/status-draft-yellow?style=flat-square)
![scope](https://img.shields.io/badge/scope-connector--local-blue?style=flat-square)
![network](https://img.shields.io/badge/network-off_by_default-critical?style=flat-square)
![release](https://img.shields.io/badge/release-not_from_tests-critical?style=flat-square)
![truth](https://img.shields.io/badge/truth-CONFIRMED%20%2F%20PROPOSED%20%2F%20UNKNOWN-lightgrey?style=flat-square)

> **One-line purpose.** Keep FEMA connector tests deterministic, no-network by default, source-role explicit, and limited to safe source-admission behavior.

---

## 1. Status and evidence boundary

| Claim | Status | Meaning |
|---|---:|---|
| `connectors/fema/tests/README.md` exists in the live repo. | **CONFIRMED** | The prior content was a greenfield stub before this update. |
| FEMA product pages exist under `docs/sources/catalog/fema/`. | **CONFIRMED from repo search/fetch evidence** | Test docs should link to source-family and product docs. |
| `connectors/fema/` is the FEMA family connector lane. | **CONFIRMED path / PROPOSED contract** | Implementation depth remains unverified. |
| Split/nested FEMA connector paths are reconciled. | **NEEDS VERIFICATION** | `connectors/fema/nfhl/`, `connectors/fema-nfhl/`, and `connectors/fema-openfema/` need ADR, migration note, or repo-tree decision. |
| `connectors/fema/tests/` is wired into CI. | **UNKNOWN** | No workflow run, test log, or CI file was verified in this update. |

This README is a connector-local test contract. It is not evidence that the FEMA connector is implemented, activated, or release-ready.

---

## 2. Placement and responsibility

`connectors/fema/tests/` is for FEMA connector-local tests only.

| Path segment | Responsibility |
|---|---|
| `connectors/` | Source-specific fetchers and admitters. |
| `fema/` | FEMA source-family connector lane. |
| `tests/` | Local tests for import safety, parser behavior, source roles, admission envelopes, failures, and drift. |
| `README.md` | Human-facing test contract. |

This folder must not replace root `tests/`, shared fixture authority, source descriptors, schemas, policy, release records, or downstream validation.

---

## 3. What these tests may prove

FEMA connector-local tests may prove that connector code:

- imports without network calls;
- keeps live access disabled by default;
- requires source descriptors before live activation;
- preserves FEMA product or table identity;
- keeps source role explicit: regulatory, administrative, or aggregate;
- keeps NFHL as regulatory context rather than observed inundation;
- keeps OpenFEMA declaration records as administrative context;
- keeps OpenFEMA aggregate records as aggregate context;
- preserves version, effective date, datum, units, source lineage, retrieval metadata, and digests where available;
- fails closed on malformed, incomplete, stale, role-unclear, rights-unclear, or schema-drift payloads;
- outputs only RAW or QUARANTINE handoff candidates.

They must not prove public truth, release eligibility, current conditions, or formal site-specific conclusions.

---

## 4. What does not belong here

| Do not place here | Correct home or next step |
|---|---|
| Shared golden fixtures | `fixtures/` or accepted fixture authority. |
| Source descriptors | `data/registry/sources/` or accepted source registry home. |
| Object-family contracts | `contracts/`. |
| Machine-checkable schemas | `schemas/contracts/v1/...`. |
| Policy decisions | `policy/`. |
| Release records | `release/`. |
| Processed, catalog, triplet, published, proof, or receipt outputs | Downstream lifecycle roots only. |
| Large copied source extracts | Approved RAW or QUARANTINE paths with receipts. |
| Generated summaries used as evidence | Not allowed; evidence must resolve through governed evidence records. |

---

## 5. Test classes

### Import safety

Expected checks:

- imports do not call the network;
- imports do not read live secrets;
- parser-only tests run without live configuration.

### Configuration and source-role tests

Expected checks:

- each admitted product or table requires a source descriptor reference;
- each product or table has source role, sensitivity posture, rights posture, and cadence fields;
- split paths do not silently create parallel implementation authority.

### NFHL tests

Expected checks:

- NFHL-shaped payloads preserve regulatory attributes;
- version, effective date, datum, units, panel/study, and lineage metadata are preserved where available;
- visualization-only material is not treated as analytic vector source data;
- missing critical metadata routes to review-required or quarantine-safe behavior.

### OpenFEMA tests

Expected checks:

- disaster declaration records remain administrative records;
- auxiliary tables require per-table admission;
- aggregate tables preserve aggregation unit;
- pagination and freshness metadata are explicit;
- unknown table shape produces reviewable drift.

### Admission envelope tests

Expected checks:

- output targets RAW or QUARANTINE only;
- retrieval metadata, product/table key, parser version, digest, and source descriptor reference are present where applicable;
- no test writes directly to processed, catalog, triplet, published, proof, receipt, or release stores.

### Error and drift tests

Expected checks:

- malformed payloads produce finite errors;
- empty payloads produce abstention unless explicitly valid;
- schema or source-shape changes produce `NEEDS_VERIFICATION`-style drift signals;
- timeout/rate-limit cases do not spin forever.

### Optional live smoke tests

Live smoke tests, if any, must be skipped by default, steward-approved, isolated from normal CI, and limited to safe metadata checks.

---

## 6. Fixture rules

Use synthetic, minimized, or reviewed fixtures by default.

Fixture rules:

1. Keep product/table identity explicit.
2. Keep source role explicit.
3. Preserve fields needed to test regulatory, administrative, and aggregate boundaries.
4. Include valid, empty, malformed, stale, incomplete, schema-drift, role-unclear, rights-unclear, datum/units-unclear, and aggregation-unit-unclear cases.
5. Promote shared fixtures to the repo’s fixture authority instead of duplicating them across connector folders.

Example fixture metadata:

```yaml
fixture_id: fema-nfhl-synthetic-zone-001
fixture_status: synthetic
source_family: fema
source_product: nfhl
source_role: regulatory
supports_tests:
  - parser_valid_shape
  - regulatory_context_boundary
  - source_admission_envelope
rights_posture: non-authoritative-test-fixture
sensitivity_posture: public_context_only
created: 2026-06-18
review_state: draft
```

---

## 7. No-network default

Default tests must require no internet, no live FEMA endpoint, no large source download, and no release workflow.

Suggested skip condition, subject to repo convention verification:

```python
pytestmark = pytest.mark.skipif(
    os.getenv("KFM_ALLOW_LIVE_FEMA_TESTS") != "1",
    reason="Live FEMA tests are opt-in and disabled by default.",
)
```

---

## 8. Expected local layout

This layout is **PROPOSED** until checked against the mounted repository.

```text
connectors/fema/tests/
├── README.md
├── test_import_safety.py
├── test_config.py
├── test_nfhl_parser.py
├── test_openfema_parser.py
├── test_admission_envelope.py
├── test_errors.py
└── live/
    └── test_live_smoke.py
```

---

## 9. Running the tests

The exact command is **NEEDS VERIFICATION** against the mounted repo.

Likely local command:

```bash
python -m pytest connectors/fema/tests
```

Likely no-network CI command:

```bash
KFM_ALLOW_LIVE_FEMA_TESTS=0 python -m pytest connectors/fema/tests
```

Optional live smoke command, only after source-steward approval:

```bash
KFM_ALLOW_LIVE_FEMA_TESTS=1 python -m pytest connectors/fema/tests/live
```

Use the repo-standard runner if Makefile, `uv`, Poetry, tox, nox, or CI conventions say otherwise.

---

## 10. Acceptance checklist

- [ ] Default test run performs no live network calls.
- [ ] Live smoke tests are isolated and skipped by default.
- [ ] Fixtures are synthetic, minimized, redacted, or explicitly approved.
- [ ] Each tested FEMA product/table carries explicit source role.
- [ ] NFHL remains regulatory context.
- [ ] OpenFEMA declaration records remain administrative context.
- [ ] OpenFEMA aggregate records remain aggregate context.
- [ ] Datum, units, version, effective-date, lineage, table identity, and aggregation unit are preserved where applicable.
- [ ] Tests do not write to processed, catalog, triplet, published, proof, receipt, or release stores.
- [ ] Root-level test or CI entry point is updated if these tests are meant to run automatically.

---

## 11. Failure handling

| Situation | Expected outcome |
|---|---|
| Source descriptor missing | `ABSTAIN` or test failure with actionable message. |
| Product or table not admitted | `NEEDS_VERIFICATION`; no live activation. |
| Network disabled | Skip or fail with clear no-network outcome. |
| Timeout or rate limit | Bounded connector error. |
| Empty response | `ABSTAIN` unless empty is explicitly valid. |
| Malformed response | `ERROR` with safe metadata. |
| Schema drift | `NEEDS_VERIFICATION`; drift note candidate. |
| Source role unclear | Quarantine or review-required behavior. |
| Datum, units, version, or effective date unclear | Quarantine or review-required behavior. |
| Aggregation unit unclear | Quarantine or review-required behavior. |

---

## 12. Review and rollback

Review notes:

- Keep connector-local tests local.
- Move shared helpers upward only when reused by multiple connectors.
- Treat fixture additions as governance-significant changes.
- Update this README when product lanes, fixture locations, live-smoke posture, or test classes change.

Rollback path:

1. Revert the connector-local test change.
2. Remove new local fixtures that are no longer referenced.
3. Restore no-network defaults.
4. Re-run the repo-standard no-network test command.
5. Preserve any source-role, table-admission, or path-canonicality drift notes revealed by the change.

---

## 13. Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm `connectors/fema/` implementation layout. | **NEEDS VERIFICATION** | Mounted repo tree. |
| Confirm test runner and dependency manager. | **NEEDS VERIFICATION** | `pyproject.toml`, Makefile, CI workflow, or equivalent. |
| Confirm root fixture authority. | **NEEDS VERIFICATION** | `fixtures/README.md`, root `tests/README.md`, and repo convention. |
| Confirm canonical relationship among FEMA connector paths. | **NEEDS VERIFICATION** | Directory Rules, ADR, and migration note. |
| Confirm source descriptor home and source IDs for FEMA products/tables. | **NEEDS VERIFICATION** | Source registry and source catalog docs. |
| Confirm source-admission envelope schema. | **NEEDS VERIFICATION** | `schemas/contracts/v1/source/` and related contract docs. |
| Confirm live smoke-test policy. | **NEEDS VERIFICATION** | Source steward and CI policy. |
| Confirm expected fixture strategy for NFHL and OpenFEMA material. | **NEEDS VERIFICATION** | Fixture registry and validation review. |

---

## Maintainer note

FEMA connector tests should prove restraint. A passing test suite should show that the connector can parse and admit regulatory, administrative, and aggregate source-shaped material safely while refusing to turn FEMA records into public KFM truth without downstream evidence, policy, review, release, and rollback support.
