<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests/domains/atmosphere/no-network/readme
title: Atmosphere No-Network Test Lane README
type: test-lane-readme
version: v0.1
status: draft
owners:
  - <PLACEHOLDER — Atmosphere steward>
  - <PLACEHOLDER — Test steward>
  - <PLACEHOLDER — Security/governance reviewer>
created: 2026-07-05
updated: 2026-07-05
policy_label: public
implementation_status: scaffold
verification_status: current-session path verified; network blocker, markers, tests, and CI not verified
related:
  - tests/README.md
  - tests/domains/atmosphere/README.md
  - tests/domains/atmosphere/no-network-fixtures/README.md
  - docs/doctrine/directory-rules.md
  - docs/domains/atmosphere/README.md
  - docs/domains/atmosphere/FILE_SYSTEM_PLAN.md
  - docs/domains/atmosphere/PIPELINE.md
  - docs/domains/atmosphere/API_CONTRACTS.md
  - fixtures/domains/atmosphere/
  - connectors/
  - pipelines/domains/atmosphere/
  - tools/validators/
  - policy/domains/atmosphere/
tags:
  - kfm
  - tests
  - atmosphere
  - no-network
  - offline
  - deterministic-tests
  - network-deny
  - fail-closed
  - governance
] -->

<a id="top"></a>

# Atmosphere No-Network Tests

> Test-lane contract for proving the Atmosphere / Air domain test suite remains deterministic, offline by default, credential-free, and fail-closed when code attempts live network access.

![status: draft](https://img.shields.io/badge/status-draft-orange)
![lane: tests%2Fdomains%2Fatmosphere-informational](https://img.shields.io/badge/lane-tests%2Fdomains%2Fatmosphere-informational)
![network: denied--by--default](https://img.shields.io/badge/network-denied--by--default-success)
![credentials: none](https://img.shields.io/badge/credentials-none-success)
![implementation: scaffold](https://img.shields.io/badge/implementation-scaffold-yellow)
![policy: fail--closed](https://img.shields.io/badge/policy-fail--closed-blue)

**Status:** `draft`  
**Authority:** test-lane README; not a schema, policy, connector, validator, release decision, receipt, proof, or fixture inventory  
**Owning root:** `tests/`  
**Domain segment:** `domains/atmosphere/`  
**Lane:** `no-network/`  
**Default posture:** offline, deterministic, credential-free, fail-closed  
**Last reviewed:** 2026-07-05

> [!IMPORTANT]
> KFM Atmosphere is **not** an emergency alerting or life-safety system. No-network tests may cover advisory-context behavior, but they must not make KFM the issuing authority for emergency guidance. Emergency instructions and official alerts remain outside this lane.

---

## Contents

1. [Purpose](#1-purpose)
2. [Directory fit and authority](#2-directory-fit-and-authority)
3. [Relationship to `no-network-fixtures`](#3-relationship-to-no-network-fixtures)
4. [Status and evidence boundary](#4-status-and-evidence-boundary)
5. [What belongs here](#5-what-belongs-here)
6. [What does not belong here](#6-what-does-not-belong-here)
7. [No-network proof matrix](#7-no-network-proof-matrix)
8. [Denied network surfaces](#8-denied-network-surfaces)
9. [Allowed local dependencies](#9-allowed-local-dependencies)
10. [Fail-closed expectations](#10-fail-closed-expectations)
11. [Lifecycle and publication boundaries](#11-lifecycle-and-publication-boundaries)
12. [Suggested local commands](#12-suggested-local-commands)
13. [Review burden](#13-review-burden)
14. [Related folders](#14-related-folders)
15. [Open questions](#15-open-questions)
16. [Definition of done](#16-definition-of-done)
17. [Changelog](#17-changelog)
18. [Last reviewed](#18-last-reviewed)

---

## 1. Purpose

This directory is the Atmosphere / Air test sublane for **network denial and offline determinism**.

Its job is to prove that the default Atmosphere test suite does not depend on:

- live source services,
- internet access,
- developer machine caches,
- credentials,
- private endpoints,
- cloud runtime state,
- mutable upstream API responses, or
- current weather, air-quality, smoke, AOD, satellite, model, climate, or advisory-provider availability.

A mature no-network suite should support these claims:

1. **Default Atmosphere tests are offline.** The suite can run with network disabled.
2. **Network attempts are visible.** Accidental live HTTP, socket, SDK, tile, geocode, storage, or database calls fail deterministically.
3. **Credential use is rejected.** The default test tier does not read secrets, tokens, cookies, service accounts, `.env` files, or private local state.
4. **Integration behavior is isolated.** Live-source smoke checks, if any, are opt-in and never part of the default CI gate.
5. **Fixture and validator behavior stay separate.** Tests may use local fixtures and validator code, but tests must not become production fetchers or canonical source authority.
6. **Failure outcomes are governed.** Missing source access, denied network, malformed stubs, and absent credentials produce explicit failures or finite response outcomes, not silent fallback.

---

## 2. Directory fit and authority

Directory Rules place enforceability proof under `tests/`. Domain-specific test material uses the domain as a segment inside the responsibility root:

```text
tests/domains/atmosphere/no-network/
```

This path is correct because:

| Placement question | Answer |
|---|---|
| Primary responsibility | Prove offline/no-network behavior for Atmosphere tests. |
| Owning root | `tests/` |
| Domain segment | `domains/atmosphere/` |
| Sublane | `no-network/` |
| Fixture home | `fixtures/domains/atmosphere/` or scoped local test fixtures when documented. |
| Validator home | `tools/validators/` |
| Connector home | `connectors/` |
| Pipeline home | `pipelines/domains/atmosphere/` and `pipeline_specs/atmosphere/`, if implemented. |
| Policy home | `policy/domains/atmosphere/` |
| Data lifecycle home | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/triplets`, `data/published`. |
| Release home | `release/` |
| Receipts/proofs home | `data/receipts/` and `data/proofs/` |

> [!WARNING]
> This directory must not become an alternate connector, adapter, fixture warehouse, policy home, or source cache. It proves that those systems can be tested without live network access.

[↑ Back to top](#top)

---

## 3. Relationship to `no-network-fixtures`

`no-network/` and `no-network-fixtures/` are related but not identical.

| Lane | Focus | Example proof |
|---|---|---|
| `tests/domains/atmosphere/no-network/` | Broad offline and network-denial behavior across tests, validators, connectors, API stubs, map/tile dependencies, and integration boundaries. | A test fails if Atmosphere code tries live HTTP during the default suite. |
| `tests/domains/atmosphere/no-network-fixtures/` | Fixture-specific discipline: local fixture roots, public-safe samples, fixture manifests, fixture metadata, checksums, and fixture/source authority separation. | A test rejects a fixture that requires a live source URL or contains a credential. |

The two lanes should reinforce each other without duplicating responsibility:

- `no-network/` proves **nothing reaches the network by default**.
- `no-network-fixtures/` proves **the local inputs used by those tests are governed and safe**.

---

## 4. Status and evidence boundary

| Item | Status |
|---|---|
| Target path exists in repo | CONFIRMED in this session before this README update. |
| Directory Rules basis for `tests/domains/<domain>/` | CONFIRMED from current repo doctrine. |
| `tests/README.md` says default tests must avoid live network calls | CONFIRMED from current repo docs. |
| Actual no-network test implementation under this directory | UNKNOWN in this README. |
| Network-blocking fixture/hook implementation | NEEDS VERIFICATION. |
| Canonical pytest marker names | NEEDS VERIFICATION. |
| CI workflow names and enforcement status | NEEDS VERIFICATION. |
| Existence and completeness of reusable Atmosphere fixtures | NEEDS VERIFICATION. |

This README defines the test-lane contract. It does not claim the no-network mechanism, CI gate, marker vocabulary, fixtures, or tests are already complete.

---

## 5. What belongs here

This directory may contain:

- README and lane contract material for Atmosphere no-network tests.
- Tests that block or detect live HTTP, socket, SDK, browser, tile, cloud, database, or source-client calls.
- Tests that prove default Atmosphere validators and parsers run without live services.
- Tests that assert source adapters are mocked, stubbed, or excluded from default unit tests.
- Tests that verify integration checks are opt-in and excluded from default CI.
- Tests that verify denied network access produces explicit failure, `DENY`, `ABSTAIN`, `ERROR`, or another governed finite outcome.
- Tests that ensure local fixtures and fixture manifests are used instead of live pulls.
- Tests that prevent accidental credential reads in the default test tier.
- Test-local helper code that is only used to deny, monkeypatch, or assert network boundaries.

---

## 6. What does not belong here

This directory must not contain:

- Production connector code.
- Production pipeline code.
- Source fetchers or scrapers.
- Downloaded source payloads, live cache snapshots, or source-system exports.
- Real credentials, API keys, service accounts, cookies, signed URLs, `.env` files, or private endpoints.
- Raw, work, quarantine, processed, catalog, triplet, or published data.
- Receipts, proofs, release decisions, rollback decisions, or source registry authority.
- Schema, contract, or policy definitions.
- Reusable fixture inventories that belong under `fixtures/domains/atmosphere/`.
- Network-enabled tests that run by default.

> [!CAUTION]
> “It only calls a public endpoint” is not enough. Default tests must be deterministic and no-network even when the endpoint is public, stable, and unauthenticated.

[↑ Back to top](#top)

---

## 7. No-network proof matrix

| Test concern | Required proof | Failure mode |
|---|---|---|
| HTTP denial | Attempts through common HTTP clients are blocked or detected. | Test fails with explicit network-denied message. |
| Socket denial | Raw socket connections are blocked or detected. | Test fails; no silent retry. |
| SDK denial | Source/cloud SDK calls are mocked, blocked, or excluded. | Test fails or is marked integration-only. |
| Tile/geocode denial | Map tiles, style URLs, geocoding, reverse geocoding, and basemap requests are disabled in default tests. | Test fails or substitutes local stub. |
| Credential denial | Environment and local credential files are not required. | Test fails if secret-like dependency is accessed. |
| Integration isolation | Live source checks are opt-in only. | Unmarked live check fails default suite. |
| Fixture-only execution | Default tests use local fixtures or generated stubs. | Live source read fails default suite. |
| Finite outcome | Denied network produces clear validation failure or finite envelope outcome. | No silent fallback, partial truth, or uncited answer. |
| Reproducibility | Results do not change because external service content changed. | Test fails if it depends on live current data. |
| Governance separation | Tests do not publish, catalog, or promote outputs. | Attempted promotion from tests fails. |

---

## 8. Denied network surfaces

Default tests should deny or explicitly mock these surfaces:

- `requests`, `httpx`, `urllib`, `aiohttp`, browser fetch, or any HTTP client.
- Raw sockets and DNS lookups.
- FTP/SFTP clients.
- Cloud storage SDKs.
- Database connections outside local test-only stores.
- Message queues and remote service buses.
- NOAA, EPA, NASA, USGS, state, local, tribal, county, vendor, or academic live service calls.
- Map tile, style, sprite, glyph, geocoding, and reverse-geocoding requests.
- Package downloads, schema downloads, remote JSON references, or remote documentation fetches during tests.
- Remote model endpoints or AI services.

If a live source check is valuable, put it behind an explicit integration/manual marker and keep it out of default CI.

---

## 9. Allowed local dependencies

Default no-network tests may use:

| Dependency | Allowed when |
|---|---|
| Local reusable fixtures | They live in the declared fixture lane and are public-safe. |
| Tiny test-local fixtures | They are deliberately scoped to this test and not reusable domain evidence. |
| Deterministic generated fixtures | Generator is deterministic and does not perform network access. |
| Local schema files | They are read from the repo, not fetched remotely. |
| Local policy files | They are read from the repo, not fetched remotely. |
| Local validator code | Tests call it; tests do not become the validator implementation. |
| Temporary directories | They are test-scoped and cleaned up. |
| Monkeypatch/network-block hooks | They make forbidden access visible and deterministic. |

Local dependencies should not read developer-specific hidden state unless the test explicitly proves that hidden state is ignored or denied.

---

## 10. Fail-closed expectations

No-network tests should prefer explicit negative outcomes over permissive fallback.

| Situation | Expected outcome |
|---|---|
| Code attempts live source fetch in default suite | Fail test. |
| Code attempts to read a credential | Fail test or deny access. |
| Code requires network to resolve schema/policy | Fail test; schemas and policies should be local. |
| Connector accidentally runs during unit test | Fail test or require integration marker. |
| Map shell attempts remote tiles/styles in unit test | Fail test or use local stub. |
| Missing fixture | Fail with clear fixture path message. |
| Malformed fixture | Fail validation. |
| Network unavailable during integration-only test | Skip or fail according to explicit integration contract; never affect default suite. |
| External source changed | Default tests unaffected. |

For public-facing runtime tests, denied network should map to finite governed outcomes rather than improvising truth:

```text
ANSWER | ABSTAIN | DENY | ERROR
```

---

## 11. Lifecycle and publication boundaries

No-network tests can prove behavior across the lifecycle, but they do not move data through the lifecycle:

```text
RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED
```

| Boundary | Rule |
|---|---|
| Source admission | Connectors may be exercised only through mocks/stubs in default tests. |
| RAW | Do not place raw source payloads here. |
| WORK / QUARANTINE | Do not use this directory as scratch space. |
| PROCESSED | Do not store processed datasets here. |
| CATALOG / TRIPLET | Do not treat test outputs as catalog or graph truth. |
| PUBLISHED | Tests never publish. |
| RECEIPTS / PROOFS | Do not store trust-bearing receipts or proofs here. |
| RELEASE | Release decisions remain under `release/`. |

A no-network pass is a proof of test determinism, not a release approval.

---

## 12. Suggested local commands

> [!NOTE]
> Command names, marker names, and CI job names are **NEEDS VERIFICATION** until checked against the actual repository test configuration.

Likely local lane check:

```bash
pytest tests/domains/atmosphere/no-network
```

Likely default suite intent:

```bash
pytest tests/domains/atmosphere -m "not integration"
```

Possible repo-wide validator command if implemented:

```bash
python tools/validate_all.py
```

Candidate marker names only — not authoritative:

```text
no_network
offline
integration
live_source
network
```

---

## 13. Review burden

Reviewers should be able to answer:

- Can the test lane run with network disabled?
- Does it fail if live HTTP/socket/SDK access is attempted?
- Are live-source checks excluded from default CI?
- Are credentials unnecessary and unread?
- Are schemas, policies, fixtures, and docs resolved locally?
- Are fixture paths governed and non-duplicative?
- Does denied network produce finite outcomes instead of invented truth?
- Does the lane avoid storing source data, receipts, proofs, or release decisions?
- Does the lane preserve the Atmosphere non-emergency boundary?
- Are OPEN and NEEDS VERIFICATION items visible rather than hidden?

---

## 14. Related folders

| Path | Relationship |
|---|---|
| `tests/domains/atmosphere/` | Parent Atmosphere test lane. |
| `tests/domains/atmosphere/no-network-fixtures/` | Fixture-specific offline/public-safe fixture discipline. |
| `tests/domains/atmosphere/schema/` | Schema conformance tests. |
| `tests/domains/atmosphere/source-role/` | Source-role anti-collapse tests. |
| `tests/domains/atmosphere/knowledge-character/` | Knowledge-character anti-collapse tests. |
| `tests/domains/atmosphere/policy-deny/` | Policy fail-closed tests. |
| `fixtures/domains/atmosphere/` | Reusable valid/invalid fixture home. |
| `connectors/` | Source-specific admission code; mocked or integration-only in default tests. |
| `pipelines/domains/atmosphere/` | Executable Atmosphere pipeline logic if present. |
| `tools/validators/` | Validator implementation home. |
| `policy/domains/atmosphere/` | Atmosphere policy/deny rules. |
| `docs/domains/atmosphere/` | Human-facing Atmosphere lane docs. |
| `release/candidates/atmosphere/` | Release decision lane if/when present. |

---

## 15. Open questions

| Question | Status | Notes |
|---|---|---|
| What is the canonical no-network marker name? | NEEDS VERIFICATION | Candidate names are not authoritative. |
| Is there a shared network-block fixture in root test config? | NEEDS VERIFICATION | Could live in shared pytest config or test utilities. |
| Should `no-network/` own all socket/HTTP blocking tests, or should some live under root `tests/`? | OPEN | Repo-wide tests may be better for global enforcement. |
| Are Atmosphere live-source checks needed at all? | OPEN | If needed, make them integration/manual only. |
| Is the `no-network-fixtures/` lane now the preferred home for fixture-specific tests? | PROPOSED | This README treats it as fixture-specific and this lane as broader network-denial. |
| What CI job proves offline determinism? | NEEDS VERIFICATION | Must be checked against `.github/workflows/`. |
| Should local map tile/style requests be covered here or in UI tests? | OPEN | Both may be appropriate; avoid duplicate authority. |

---

## 16. Definition of done

This lane is mature when:

- [ ] The default no-network test lane exists and runs locally.
- [ ] HTTP, socket, SDK, tile, geocode, and remote schema/policy/doc fetches are blocked or mocked.
- [ ] Tests fail on accidental live network access.
- [ ] Credentials are not required or read by default tests.
- [ ] Integration/live-source tests, if any, are explicitly marked and excluded from default CI.
- [ ] Fixtures are local, public-safe, and governed by the fixture lane.
- [ ] Denied network maps to explicit validation failure or finite response outcomes.
- [ ] Test outputs cannot become catalog, triplet, published, receipt, proof, or release authority.
- [ ] CI exposes offline/no-network enforcement clearly.
- [ ] README open questions are resolved or tracked in a verification backlog.

---

## 17. Changelog

| Date | Version | Change |
|---|---:|---|
| 2026-07-05 | v0.1 | Initial governed README for the Atmosphere no-network test lane. |

---

## 18. Last reviewed

**2026-07-05** — Initial README scaffold. Target path was present but empty before update. Network blocker implementation, marker names, tests, fixtures, and CI enforcement remain **NEEDS VERIFICATION**.

[↑ Back to top](#top)
