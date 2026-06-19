<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-gbif-tests-readme
title: connectors/gbif/tests/ — GBIF Connector Tests
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Source steward · Biodiversity steward · Flora steward · Fauna steward · Habitat steward · Validation steward · Docs steward
created: 2026-06-18
updated: 2026-06-18
policy_label: public-doctrine; rights-and-sensitivity-gated; no-live-by-default
proposed_path: connectors/gbif/tests/README.md
truth_posture: CONFIRMED path exists / PROPOSED local test contract / UNKNOWN implementation depth
related:
  - ../README.md
  - ../src/README.md
  - ../src/gbif/README.md
  - ../plants/README.md
  - ../../../docs/sources/catalog/gbif/README.md
  - ../../../docs/sources/catalog/gbif/async-download.md
  - ../../../docs/domains/fauna/README.md
  - ../../../docs/domains/flora/README.md
  - ../../../docs/domains/habitat/README.md
  - ../../../data/registry/sources/
  - ../../../data/raw/fauna/
  - ../../../data/raw/flora/
  - ../../../data/raw/habitat/
  - ../../../data/quarantine/fauna/
  - ../../../data/quarantine/flora/
  - ../../../data/quarantine/habitat/
  - ../../../fixtures/
  - ../../../schemas/contracts/v1/source/
  - ../../../policy/sensitivity/
  - ../../../policy/rights/
  - ../../../release/
tags: [kfm, connectors, gbif, tests, biodiversity, darwin-core, occurrence, taxonomy, fixtures, source-admission, raw, quarantine, governance]
notes:
  - "This README replaces a greenfield stub with connector-local test guidance for the GBIF lane."
  - "Tests must be no-network by default and must not require live credentials, live downloads, private datasets, or source-side side effects."
  - "Use synthetic, minimized, redacted, or explicitly approved fixtures only."
  - "Tests may verify connector safety and admission envelopes; they do not prove occurrence truth, taxonomy authority, publication eligibility, or release readiness."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# GBIF Connector Tests

> Connector-local test guidance for `connectors/gbif/`.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Scope: connector tests" src="https://img.shields.io/badge/scope-connector__tests-blue">
  <img alt="Network: off by default" src="https://img.shields.io/badge/network-off__by__default-critical">
  <img alt="Fixtures: synthetic preferred" src="https://img.shields.io/badge/fixtures-synthetic__preferred-orange">
  <img alt="Lifecycle: raw or quarantine only" src="https://img.shields.io/badge/lifecycle-raw%20%7C%20quarantine%20only-orange">
</p>

`connectors/gbif/tests/`

## Scope

This folder is for connector-local tests for the proposed GBIF source-admission connector.

Tests may verify:

- import safety;
- no-network defaults;
- missing-source-descriptor behavior;
- rights, license, and citation guardrails;
- dataset and publisher provenance handling;
- Darwin Core-style field preservation;
- taxonomic-backbone/version metadata handling;
- malformed or incomplete GBIF-shaped payload handling;
- RAW or QUARANTINE handoff envelopes;
- refusal to create public claims, graph truth, release artifacts, or publication outputs.

Tests must not become occurrence truth, taxonomy truth, conservation-status truth, source descriptor authority, policy authority, release authority, or publication authority.

---

## Test boundaries

Default test behavior:

```text
network: disabled
credentials: not required
live downloads: not required
fixtures: synthetic, minimized, redacted, or explicitly approved
writes: no processed/catalog/triplet/published/proof/receipt/release writes
outputs: local assertions only
```

Optional live smoke tests, if they ever exist, must be isolated, steward-approved, skipped by default, and documented in a separate live-test section or file.

---

## Expected test classes

| Test class | Purpose |
|---|---|
| Import safety | Importing modules must not call the network or read live secrets. |
| Configuration | Defaults must be no-network and source activation must be explicit. |
| Descriptor gate | Missing SourceDescriptor must block live activation. |
| Rights gate | Unknown license, citation, or permitted-use metadata must route to review-required behavior. |
| Provenance gate | Dataset, publisher, retrieval, and source-role metadata must be preserved. |
| Version gate | Backbone/version metadata must be preserved where available. |
| Parser behavior | GBIF-shaped test payloads must preserve metadata and uncertainty fields. |
| Admission envelope | Connector output must target RAW or QUARANTINE only. |
| Error handling | Malformed, incomplete, or ambiguous payloads must produce finite outcomes. |
| Release blocking | Tests must prove connector code cannot directly publish or create release outputs. |

---

## Fixture rules

Use synthetic fixtures whenever possible.

Fixture requirements:

1. Do not commit live credentials, private datasets, tokens, cookies, session state, or bulk source exports unless explicitly approved by a steward.
2. Keep fixtures minimal and purpose-specific.
3. Mark fixture status clearly: synthetic, redacted, minimized, or approved.
4. Include license, citation, dataset, publisher, retrieval, source-role, and version metadata when the test path requires it.
5. Include negative fixtures for missing descriptor, missing license, missing citation, unclear provenance, malformed payload, version unclear, and restricted-record cases.
6. Promote shared fixtures to the repo fixture authority only after review.

Example fixture metadata:

```yaml
fixture_id: gbif-synthetic-admission-001
fixture_status: synthetic
source_family: gbif
source_role: candidate
supports_tests:
  - descriptor_gate
  - rights_gate
  - admission_envelope
rights_posture: test-only
review_state: draft
```

---

## Running tests

The exact command is **NEEDS VERIFICATION** against the repo’s package manager and CI configuration.

Likely local command:

```bash
python -m pytest connectors/gbif/tests
```

Likely no-network command:

```bash
KFM_ALLOW_LIVE_GBIF_TESTS=0 python -m pytest connectors/gbif/tests
```

Optional live-test command, only if later approved:

```bash
KFM_ALLOW_LIVE_GBIF_TESTS=1 python -m pytest connectors/gbif/tests/live
```

Use the repo-standard runner if Makefile, `uv`, Poetry, tox, nox, or CI conventions say otherwise.

---

## Acceptance checklist

- [ ] Default tests do not access the network.
- [ ] Tests do not require live credentials or live downloads.
- [ ] Fixtures are synthetic, minimized, redacted, or explicitly approved.
- [ ] SourceDescriptor is required before source activation.
- [ ] Rights, license, and citation uncertainty fails closed.
- [ ] Dataset and publisher provenance are preserved.
- [ ] Taxonomy/backbone version metadata is preserved where available.
- [ ] Connector output is limited to RAW or QUARANTINE handoff candidates.
- [ ] Tests do not write to processed, catalog, triplet, published, proof, receipt, or release stores.
- [ ] Tests do not produce public claims.
- [ ] CI wiring is documented once verified.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm actual test files below this path. | **NEEDS VERIFICATION** | Repo tree or mounted workspace. |
| Confirm test runner and package manager. | **NEEDS VERIFICATION** | Makefile, pyproject, CI workflow, tox, nox, or equivalent. |
| Confirm fixture authority. | **NEEDS VERIFICATION** | Root fixture docs and validation review. |
| Confirm source descriptor and source ID. | **NEEDS VERIFICATION** | Source registry entry and accepted schema. |
| Confirm Darwin Core and backbone-version assertions. | **NEEDS VERIFICATION** | Parser tests and source descriptor. |
| Confirm live-test policy, if any. | **NEEDS VERIFICATION** | Source steward and CI policy. |
| Confirm CI wiring. | **NEEDS VERIFICATION** | Workflow files and test logs. |

---

## Maintainer note

These tests should prove restraint. A passing suite should show that the GBIF connector can be imported, configured, and exercised with safe fixtures while refusing to bypass source descriptors, rights review, lifecycle gates, release controls, or publication boundaries.
