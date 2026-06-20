<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-noaa-tests-readme
title: connectors/noaa/tests/ — NOAA Connector Tests
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Source steward · NOAA steward · Hazards steward · Atmosphere steward · Climate steward · Soil steward · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-06-19
policy_label: public-doctrine; multi-role; not-life-safety; no-live-by-default
proposed_path: connectors/noaa/tests/README.md
truth_posture: CONFIRMED path exists / PROPOSED local test contract / UNKNOWN implementation depth
related:
  - ../README.md
  - ../uscrn/README.md
  - ../../noaa-uscrn/README.md
  - ../../noaa-hms-smoke/README.md
  - ../../noaa-storm-events/README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/sources/catalog/noaa/README.md
  - ../../../docs/sources/catalog/noaa/storm-events.md
  - ../../../docs/sources/catalog/noaa/nws-api.md
  - ../../../docs/sources/catalog/noaa/hms-fire-smoke.md
  - ../../../docs/sources/catalog/noaa/hrrr-smoke.md
  - ../../../docs/sources/catalog/noaa/goes-abi-aod.md
  - ../../../docs/sources/catalog/noaa/viirs-hotspot.md
  - ../../../docs/sources/catalog/noaa/noaa-uscrn.md
  - ../../../docs/sources/catalog/noaa/station-climate-products.md
  - ../../../docs/domains/hazards/README.md
  - ../../../docs/domains/atmosphere/README.md
  - ../../../docs/domains/soil/README.md
  - ../../../data/registry/sources/
  - ../../../data/raw/
  - ../../../data/quarantine/
  - ../../../fixtures/
  - ../../../schemas/contracts/v1/source/
  - ../../../policy/rights/
  - ../../../policy/sensitivity/
  - ../../../release/
tags: [kfm, connectors, noaa, tests, ncei, nws, hms, hrrr, goes, viirs, uscrn, storm-events, hazards, atmosphere, climate, soil, fixtures, source-admission, raw, quarantine, governance]
notes:
  - "This README replaces a greenfield stub with connector-local test guidance for the NOAA connector family lane."
  - "Tests must be no-network by default and must not require live credentials, live downloads, private datasets, API keys, tokens, cookies, or source-side side effects."
  - "Use synthetic, minimized, redacted, or explicitly approved fixtures only."
  - "Tests may verify connector safety and admission envelopes; they do not prove NOAA source truth, product truth, alert authority, publication eligibility, or release readiness."
  - "NOAA products are multi-role; tests must prevent source-role collapse across observations, forecasts, modeled products, alerts-as-context, historical event records, station readings, retrievals, detections, and aggregates."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# NOAA Connector Tests

> Connector-local test guidance for the canonical NOAA connector family lane under `connectors/noaa/`.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Scope: connector tests" src="https://img.shields.io/badge/scope-connector__tests-blue">
  <img alt="Network: off by default" src="https://img.shields.io/badge/network-off__by__default-critical">
  <img alt="Fixtures: synthetic preferred" src="https://img.shields.io/badge/fixtures-synthetic__preferred-orange">
  <img alt="Source role: multi-role" src="https://img.shields.io/badge/source--role-multi--role-purple">
  <img alt="Life safety: not alert authority" src="https://img.shields.io/badge/life__safety-NOT__ALERT__AUTHORITY-red">
  <img alt="Lifecycle: raw or quarantine only" src="https://img.shields.io/badge/lifecycle-raw%20%7C%20quarantine%20only-orange">
</p>

`connectors/noaa/tests/`

## Quick jumps

[Scope](#scope) · [Test boundaries](#test-boundaries) · [Expected test classes](#expected-test-classes) · [Product-specific checks](#product-specific-checks) · [Fixture rules](#fixture-rules) · [Running tests](#running-tests) · [Acceptance checklist](#acceptance-checklist) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/noaa/tests/` is for connector-local tests for the canonical NOAA source-admission connector family.

Tests may verify:

- import safety;
- no-network defaults;
- missing `SourceDescriptor` behavior;
- source activation gates;
- product-specific parser behavior;
- source-role preservation across heterogeneous NOAA products;
- rights, citation, attribution, and terms guardrails;
- public-safety, freshness, and not-life-safety guardrails;
- geometry, time, cadence, unit, station, depth, quality-flag, model-run, issue-time, and file-vintage metadata preservation;
- malformed, incomplete, stale, ambiguous, or role-collapsed NOAA-shaped payload handling;
- RAW or QUARANTINE handoff envelopes;
- refusal to create public claims, graph truth, release artifacts, alert payloads, public UI layers, or publication outputs.

Tests must not become NOAA source truth, product truth, station truth, storm truth, smoke truth, forecast truth, air-quality truth, regulatory authority, alert authority, source descriptor authority, policy authority, release authority, catalog authority, triplet authority, proof authority, or publication authority.

---

## Test boundaries

Default test behavior:

```text
network: disabled
credentials: not required
live downloads: not required
API keys: not required
source-side side effects: forbidden
fixtures: synthetic, minimized, redacted, or explicitly approved
writes: no processed/catalog/triplet/published/proof/receipt/release writes
outputs: local assertions only
```

Optional live smoke tests, if they ever exist, must be isolated, steward-approved, skipped by default, rate-limited, source-descriptor-gated, and documented in a separate live-test section or file.

---

## Expected test classes

| Test class | Purpose |
|---|---|
| Import safety | Importing NOAA connector modules must not call the network, read live secrets, or write files. |
| Configuration | Defaults must be no-network, no-live, no-alert, and source activation must be explicit. |
| Descriptor gate | Missing SourceDescriptor must block live activation and source admission. |
| Rights gate | Unknown terms, citation, attribution, or permitted-use metadata must route to review-required behavior. |
| Source-role gate | Product-specific source roles must be preserved; NOAA-wide role collapse must fail. |
| Freshness gate | Observation, issue, valid, expiry, retrieval, file-vintage, and correction times must be preserved where applicable. |
| Public-safety gate | Alerts, forecasts, hazards, smoke, storms, and station observations must not become KFM-issued life-safety guidance. |
| Parser behavior | NOAA-shaped test payloads must preserve native fields, units, timestamps, geometries, quality flags, and product caveats. |
| Admission envelope | Connector output must target RAW or QUARANTINE only. |
| Error handling | Malformed, incomplete, stale, or ambiguous payloads must produce finite outcomes. |
| Release blocking | Tests must prove connector code cannot directly publish, tile, release, or create public API/UI outputs. |

---

## Product-specific checks

| NOAA product lane | Required test posture |
|---|---|
| Storm Events | Preserve event ID, episode ID, table type, file vintage, event type, narrative, geometry, magnitude, damage, casualty fields, and historical-event caveats; do not turn records into alerts, direct measurements, flood extents, or disaster declarations. |
| NWS API | Treat watches, warnings, advisories, alerts, forecasts, and observations as official-source context; do not emit KFM-issued alerts or life-safety instructions. |
| HMS Fire and Smoke | Preserve fire detections and smoke polygons separately; smoke density remains qualitative; do not emit PM2.5, exposure, or ground-fire authority. |
| HRRR-Smoke | Preserve model run, forecast hour, valid time, grid/version metadata, and modeled-source caveats. |
| GOES ABI AOD | Preserve retrieval metadata and aerosol optical depth caveats; do not convert AOD to PM2.5 without downstream governed derivation. |
| VIIRS Hotspot | Preserve satellite/detection metadata and uncertainty; do not assert ground-fire truth. |
| USCRN | Preserve station ID, timestamp, variable, units, quality flags, cadence, soil depth, raw/derived status, file vintage, and station-not-area caveat. |
| Station climate products | Preserve station/product/cadence/aggregate semantics; do not silently collapse station observations, climate normals, and derived aggregates. |

---

## Fixture rules

Use synthetic fixtures whenever possible.

Fixture requirements:

1. Do not commit live credentials, API keys, tokens, cookies, private datasets, private URLs, account/session state, or bulk source exports unless explicitly approved by a steward.
2. Keep fixtures minimal and purpose-specific.
3. Mark fixture status clearly: synthetic, redacted, minimized, or approved.
4. Include source family, product lane, source role, rights posture, citation posture, retrieval metadata, and review state when the test path requires it.
5. Include negative fixtures for missing descriptor, missing license/citation/attribution, unclear provenance, stale data, malformed payload, version drift, source-role collapse, and public-safety misuse.
6. Include product-specific negative fixtures for NOAA high-risk collapses: alert rebroadcast, storm record as measurement, HMS density as concentration, AOD as PM2.5, VIIRS/HMS fire as ground truth, USCRN station as area truth, and depth/cadence collapse.
7. Promote shared fixtures to the repo fixture authority only after review.

Example fixture metadata:

```yaml
fixture_id: noaa-synthetic-admission-001
fixture_status: synthetic
source_family: noaa
product_lane: uscrn
source_role: observation
supports_tests:
  - descriptor_gate
  - source_role_gate
  - admission_envelope
rights_posture: test-only
review_state: draft
network_required: false
```

---

## Running tests

The exact command is **NEEDS VERIFICATION** against the repo's package manager and CI configuration.

Likely local command:

```bash
python -m pytest connectors/noaa/tests
```

Likely no-network command:

```bash
KFM_ALLOW_LIVE_NOAA_TESTS=0 python -m pytest connectors/noaa/tests
```

Optional live-test command, only if later approved:

```bash
KFM_ALLOW_LIVE_NOAA_TESTS=1 python -m pytest connectors/noaa/tests/live
```

Use the repo-standard runner if Makefile, `uv`, Poetry, tox, nox, or CI conventions say otherwise.

---

## Acceptance checklist

- [ ] Default tests do not access the network.
- [ ] Tests do not require live credentials, API keys, private source exports, or live downloads.
- [ ] Fixtures are synthetic, minimized, redacted, or explicitly approved.
- [ ] SourceDescriptor is required before source activation.
- [ ] Rights, citation, attribution, terms, and permitted-use uncertainty fails closed.
- [ ] NOAA product lanes remain product-specific and do not collapse to one NOAA-wide source role.
- [ ] Alerts, warnings, watches, forecasts, smoke, storms, and station observations do not become KFM-issued life-safety guidance.
- [ ] Product-native time, cadence, issue, valid, expiry, retrieval, file-vintage, and correction fields are preserved where applicable.
- [ ] Product-native geometry, units, quality flags, station, depth, model-run, detection, and uncertainty fields are preserved where applicable.
- [ ] Connector output is limited to RAW or QUARANTINE handoff candidates.
- [ ] Tests do not write to processed, catalog, triplet, published, proof, receipt, release, API, UI, tile, or alert-output stores.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm actual NOAA connector modules and package layout. | **NEEDS VERIFICATION** | Repo tree, package config, imports, or CI workflow. |
| Confirm actual test runner. | **NEEDS VERIFICATION** | Makefile, `pyproject.toml`, CI workflow, tox/nox/uv/Poetry config. |
| Confirm NOAA SourceDescriptor IDs and activation state. | **NEEDS VERIFICATION** | `data/registry/sources/` entries and accepted source schema. |
| Confirm fixture locations and approval status. | **NEEDS VERIFICATION** | `fixtures/`, connector-local fixtures, fixture manifest, or steward review. |
| Confirm live-test policy and environment flags. | **NEEDS VERIFICATION** | Test config, CI config, secret policy, and steward approval record. |
| Confirm source-role and public-safety gates are implemented. | **NEEDS VERIFICATION** | Parser code, validation code, policy checks, and test logs. |
| Confirm CI wiring. | **NEEDS VERIFICATION** | Workflow files and current CI logs. |

---

## Maintainer note

Keep NOAA tests no-network by default, source-role-aware, product-specific, and conservative. If a test requires live NOAA access, API keys, source-side changes, public release, alert wording, or unreviewed sensitive material, it is not a default connector-local test.

<p align="right"><a href="#top">Back to top</a></p>
