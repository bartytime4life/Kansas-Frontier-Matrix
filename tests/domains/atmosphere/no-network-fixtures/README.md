<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests/domains/atmosphere/no-network-fixtures/readme
title: Atmosphere No-Network Fixture Test Lane README
type: test-lane-readme
version: v0.1
status: draft
owners:
  - <PLACEHOLDER — Atmosphere steward>
  - <PLACEHOLDER — Test steward>
  - <PLACEHOLDER — Fixture steward>
  - <PLACEHOLDER — Governance reviewer>
created: 2026-07-05
updated: 2026-07-05
policy_label: public
implementation_status: scaffold
verification_status: current-session path verified; runner and fixture inventory not verified
related:
  - tests/README.md
  - tests/domains/atmosphere/README.md
  - docs/doctrine/directory-rules.md
  - docs/domains/atmosphere/README.md
  - docs/domains/atmosphere/FILE_SYSTEM_PLAN.md
  - docs/domains/atmosphere/KNOWLEDGE_CHARACTER_REGISTRY.md
  - docs/domains/atmosphere/KNOWLEDGE_CHARACTERS.md
  - fixtures/domains/atmosphere/README.md
  - fixtures/domains/atmosphere/valid/
  - fixtures/domains/atmosphere/invalid/
  - tools/validators/
  - policy/domains/atmosphere/
tags:
  - kfm
  - tests
  - atmosphere
  - fixtures
  - no-network
  - deterministic-tests
  - validation
  - governance
  - cite-or-abstain
] -->

<a id="top"></a>

# Atmosphere No-Network Fixture Tests

> Test-lane contract for proving Atmosphere / Air tests run from deterministic, public-safe fixture inputs without live network calls, live credentials, unpublished source pulls, or hidden source-system side effects.

![status: draft](https://img.shields.io/badge/status-draft-orange)
![lane: tests%2Fdomains%2Fatmosphere-informational](https://img.shields.io/badge/lane-tests%2Fdomains%2Fatmosphere-informational)
![network: none](https://img.shields.io/badge/network-none-success)
![fixtures: public--safe](https://img.shields.io/badge/fixtures-public--safe-green)
![implementation: scaffold](https://img.shields.io/badge/implementation-scaffold-yellow)
![policy: cite--or--abstain](https://img.shields.io/badge/policy-cite--or--abstain-blue)

**Status:** `draft`  
**Authority:** test-lane README; not a schema, policy, source registry, fixture inventory, release decision, receipt, proof, or validator implementation  
**Owning root:** `tests/`  
**Domain segment:** `domains/atmosphere/`  
**Lane:** `no-network-fixtures/`  
**Default posture:** deterministic, offline, public-safe, fail-closed  
**Last reviewed:** 2026-07-05

> [!IMPORTANT]
> KFM Atmosphere is **not** an emergency alerting or life-safety system. This lane verifies deterministic test fixture behavior for air-quality, weather, smoke, aerosol, climate, model, and advisory-context records. It must not simulate official alerts as authoritative instructions or bypass the Hazards lane for emergency guidance.

---

## Contents

1. [Purpose](#1-purpose)
2. [Directory fit and authority](#2-directory-fit-and-authority)
3. [Status and evidence boundary](#3-status-and-evidence-boundary)
4. [What belongs here](#4-what-belongs-here)
5. [What does not belong here](#5-what-does-not-belong-here)
6. [No-network fixture proof matrix](#6-no-network-fixture-proof-matrix)
7. [Fixture source contract](#7-fixture-source-contract)
8. [Network-denial expectations](#8-network-denial-expectations)
9. [Public-safe fixture rules](#9-public-safe-fixture-rules)
10. [Lifecycle and publication gates](#10-lifecycle-and-publication-gates)
11. [Suggested local commands](#11-suggested-local-commands)
12. [Review burden](#12-review-burden)
13. [Related folders](#13-related-folders)
14. [Open questions](#14-open-questions)
15. [Definition of done](#15-definition-of-done)
16. [Changelog](#16-changelog)
17. [Last reviewed](#17-last-reviewed)

---

## 1. Purpose

This directory is the Atmosphere / Air test sublane for **no-network fixture discipline**.

Its job is to prove that Atmosphere tests can run using deterministic, inspectable, public-safe inputs without reaching out to live services or relying on the current state of external source systems.

A passing no-network fixture suite should support these claims:

1. **Default tests are offline.** Unit, schema, policy, validator, and domain tests do not require internet access.
2. **Fixtures are deterministic.** Test inputs are stable files, generated in deterministic ways, or explicitly marked test-only.
3. **Fixtures are public-safe.** Fixture data excludes secrets, private credentials, exact sensitive locations, living-person identifiers, embargoed records, unpublished candidates, and uncontrolled source dumps.
4. **Fixtures do not become source authority.** Fixtures can prove behavior; they do not replace source descriptors, EvidenceBundles, source registries, catalog records, receipts, proofs, or release decisions.
5. **Network failures fail closed.** Any attempted live pull in the default test tier should produce a test failure or an explicit skipped/integration-only outcome, not an invisible fallback.
6. **Source freshness is separated from test correctness.** Tests should not pass or fail because EPA, NOAA, NASA, USGS, state, local, or other external services changed during the run.

---

## 2. Directory fit and authority

Directory Rules place enforceability proof under `tests/`. Domain-specific test material uses the domain as a segment under the tests root:

```text
tests/domains/atmosphere/no-network-fixtures/
```

This path is correct because:

| Placement question | Answer |
|---|---|
| What is the primary responsibility? | Proving test fixture and network-denial behavior. |
| Owning root | `tests/` |
| Domain segment | `domains/atmosphere/` |
| Sublane | `no-network-fixtures/` |
| Canonical fixture home | `fixtures/domains/atmosphere/` unless an in-test fixture is deliberately local and documented. |
| Validator home | `tools/validators/` |
| Policy home | `policy/domains/atmosphere/` |
| Release decision home | `release/` |
| Receipts / proofs home | `data/receipts/` and `data/proofs/` |

> [!WARNING]
> This directory must not become a duplicate fixture warehouse. It may contain tests, test README contracts, tiny local helpers, and intentionally scoped in-test fixture samples only when those samples are not reusable domain fixtures.

[↑ Back to top](#top)

---

## 3. Status and evidence boundary

| Item | Status |
|---|---|
| Target path exists in repo | CONFIRMED in this session before this README update. |
| Directory Rules basis for `tests/domains/<domain>/` | CONFIRMED from current repo doctrine. |
| Atmosphere file-system plan includes `no-network-fixtures/` | CONFIRMED in current repo docs; plan language remains PROPOSED where it describes future lane fan-out. |
| Actual test files under this directory | UNKNOWN in this README. |
| Actual reusable fixture inventory | UNKNOWN in this README. |
| Actual pytest markers, CI job names, or validator module names | NEEDS VERIFICATION. |
| Network blocking implementation | NEEDS VERIFICATION. |

This README defines the lane contract. It does not claim that all tests, fixtures, validators, markers, or CI workflows already exist.

---

## 4. What belongs here

This directory may contain:

- README and lane contract material for Atmosphere no-network fixture tests.
- Tests that assert default Atmosphere test suites do not perform live network calls.
- Tests that verify fixture inputs are loaded from allowed local fixture paths.
- Tests that reject source URLs, credentials, API tokens, private endpoints, or live-service handles in default fixtures.
- Tests that ensure external-source adapters are mocked, stubbed, skipped, or quarantined unless explicitly run as integration tests.
- Tests that validate fixture manifests, fixture checksums, fixture freshness labels, and source-attribution stubs when those objects exist.
- Tests that prove fixtures remain public-safe and do not encode sensitive exact geometry or restricted records.
- Tiny local test-only samples when they are intentionally not shared fixtures and the reason is documented.

---

## 5. What does not belong here

This directory must not contain:

- Production fetchers, source adapters, pipelines, or validators.
- Live source pulls, scraper output, raw source dumps, or local caches from source systems.
- Real credentials, API keys, bearer tokens, cookies, signed URLs, service-account files, or `.env` files.
- Unredacted exact sensitive geometry, rare-species locations, archaeology, burial/sacred-site data, critical-infrastructure detail, living-person identifiers, or DNA/genomic data.
- Emergency alert instructions represented as KFM authority.
- Release manifests, rollback decisions, proofs, receipts, or catalog authority.
- Schema, contract, policy, or source-registry definitions.
- Reusable domain fixtures that should live under `fixtures/domains/atmosphere/`.
- Network-enabled integration tests that run by default.

> [!CAUTION]
> A test that silently reaches a live service is a trust failure even when it passes. It makes the suite non-deterministic and can hide source drift, rate limits, access changes, or policy violations.

[↑ Back to top](#top)

---

## 6. No-network fixture proof matrix

| Test concern | Expected proof | Default outcome |
|---|---|---|
| Network denial | HTTP, socket, cloud SDK, and source-client calls are blocked or mocked in default tests. | Any live attempt fails the test. |
| Fixture path allowlist | Atmosphere tests load fixtures only from approved local fixture lanes or declared tiny test-local samples. | Unknown fixture roots fail closed. |
| Credential absence | Fixtures and test configs do not require secrets or personal credentials. | Secret-like values fail or are rejected by scanner tests. |
| Deterministic fixture content | Fixture content has stable file paths, deterministic serialization, and optional checksums/manifests. | Non-deterministic generation requires explicit marker or fixture build step. |
| Public-safe transformation | Sensitive or high-risk fields are absent, generalized, redacted, or synthetic. | Unsafe fixture fields fail policy tests. |
| Source authority separation | Fixtures include attribution placeholders or EvidenceRef-shaped stubs only when appropriate; they do not claim source authority. | Fixture-only claims cannot be published. |
| Integration isolation | Live source checks, if they exist, are marked integration/manual and excluded from default CI. | Default suite stays offline. |
| Error-path coverage | Missing fixture, malformed fixture, stale fixture metadata, and denied live network access produce finite outcomes. | Tests assert `DENY`, `ABSTAIN`, `ERROR`, or explicit validation failure as appropriate. |
| Atmosphere boundary | Fixtures do not present KFM as emergency-alert authority. | Emergency-style fixture output redirects or denies. |
| Lifecycle discipline | Test fixtures do not masquerade as RAW, PROCESSED, CATALOG, TRIPLET, PUBLISHED, receipt, proof, or release records. | Lifecycle authority remains outside `tests/`. |

---

## 7. Fixture source contract

Reusable Atmosphere fixtures should normally live under:

```text
fixtures/domains/atmosphere/
├── valid/
└── invalid/
```

This test lane may reference those fixtures but should not duplicate them.

A reusable fixture should make the following inspectable where possible:

| Field | Requirement |
|---|---|
| `fixture_id` | Stable deterministic identifier for the fixture. |
| `fixture_kind` | `valid`, `invalid`, `edge_case`, `policy_denial`, or similar controlled value. |
| `domain` | `atmosphere`. |
| `object_family` | Atmosphere object family under test, such as station, observation, raster, advisory context, model field, or climate context. |
| `knowledge_character` | Present when the fixture tests knowledge-character behavior. |
| `source_role` | Present when the fixture tests source-role behavior. |
| `network_required` | Must be `false` for default fixtures. |
| `public_safe` | Must be `true` or accompanied by a documented denial/skipped reason. |
| `synthetic_or_transformed` | Required when the fixture resembles sensitive or operational data. |
| `evidence_mode` | `stub`, `synthetic`, `derived_from_public`, or another governed value when defined. |
| `checksum` | Recommended for non-trivial reusable fixtures. |
| `generated_by` | Required for generated fixtures when a deterministic generator exists. |
| `review_state` | Recommended once fixture governance matures. |

> [!NOTE]
> These fields are a lane contract, not a schema declaration. If a governed fixture manifest schema exists elsewhere, that schema is authoritative.

---

## 8. Network-denial expectations

Default Atmosphere tests should treat the following as denied unless a specific integration marker opts in:

- Direct `requests`, `httpx`, `urllib`, browser, socket, FTP, S3, cloud-storage, database, message-bus, or SDK calls.
- Live calls to air-quality, weather, smoke, AOD, satellite, model, climate, or advisory providers.
- Runtime dependence on local credentials, host machine network state, clock-sensitive URLs, or developer cache state.
- Fetching schemas, policies, source registries, or examples from remote URLs during tests.
- Network-dependent geocoding, tile fetching, basemap fetching, reverse lookup, or map style retrieval.

Integration tests, if needed later, should be separate from the default suite and should state:

```text
marker: integration
network: allowed only by explicit opt-in
credentials: never required for public CI
output: never promoted directly to canonical data or release
```

---

## 9. Public-safe fixture rules

Atmosphere data can look harmless while still carrying risk through exact location, time, site identity, infrastructure adjacency, or emergency-context misuse. Fixture reviewers should check for:

| Risk | Fixture rule |
|---|---|
| Exact sensitive locations | Use synthetic, generalized, redacted, or public-safe transformed locations. |
| Emergency-advisory misuse | Fixtures may test advisory context but must not turn KFM into the issuing authority. |
| Low-cost sensor overstatement | Fixtures should retain caveats and uncertainty where relevant. |
| Model/observation collapse | Fixtures should preserve whether a value is observed, modeled, derived, contextual, advisory, or regulatory. |
| Source-system leakage | Do not store raw access paths, private IDs, tokens, cookies, signed URLs, or scrape-state. |
| Living-person traces | Exclude names, contact details, device owners, private sensor hosts, account IDs, or household-level details. |
| Rare-site inference | Avoid precise exposure of sensitive ecological, archaeological, sacred, or infrastructure-adjacent locations. |

If a fixture cannot be made public-safe, it belongs in quarantine or a restricted governance lane, not in default tests.

---

## 10. Lifecycle and publication gates

No-network fixture tests support the KFM lifecycle but do not replace it:

```text
RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED
```

Fixture test outputs are not canonical lifecycle records.

| Lifecycle concern | Test-lane rule |
|---|---|
| RAW | Do not place raw source payloads in this directory. |
| WORK / QUARANTINE | Do not use this directory as temporary processing storage. |
| PROCESSED | Do not store validated domain products here. |
| CATALOG / TRIPLET | Do not treat fixtures as catalog or graph truth. |
| PUBLISHED | Do not publish from tests. |
| RECEIPTS / PROOFS | Do not store trust-bearing receipts or proofs here. |
| RELEASE | Do not place release decisions here. |

Publication remains a governed state transition. A fixture passing a test means the code path behaved as expected against a sample. It does not prove release readiness by itself.

---

## 11. Suggested local commands

> [!NOTE]
> Command names and markers are **NEEDS VERIFICATION** until checked against actual project test configuration.

Likely local checks:

```bash
pytest tests/domains/atmosphere/no-network-fixtures
```

Possible stricter offline mode if the project defines one:

```bash
pytest tests/domains/atmosphere/no-network-fixtures -m "not integration"
```

Possible repo-wide validation command if available:

```bash
python tools/validate_all.py
```

A mature suite should make the offline/no-network contract visible in CI through a named job or marker, for example:

```text
atmosphere-no-network-fixtures
```

The exact CI job name is **NEEDS VERIFICATION**.

---

## 12. Review burden

A reviewer should be able to answer:

- Does the test run without internet access?
- Does it fail on unexpected network calls?
- Does it avoid credentials and machine-local state?
- Does it use allowed fixture roots only?
- Does it avoid making fixtures into source authority?
- Does it avoid exact sensitive or restricted data?
- Does it preserve Atmosphere knowledge-character and source-role boundaries?
- Does it keep emergency/life-safety material out of KFM authority?
- Does it keep reusable fixture files under `fixtures/domains/atmosphere/` unless a local exception is documented?
- Does it produce finite, inspectable outcomes when fixture or network assumptions fail?

---

## 13. Related folders

| Path | Relationship |
|---|---|
| `tests/domains/atmosphere/` | Parent Atmosphere test lane. |
| `tests/domains/atmosphere/schema/` | Schema conformance tests for Atmosphere object shapes. |
| `tests/domains/atmosphere/source-role/` | Source-role anti-collapse tests. |
| `tests/domains/atmosphere/knowledge-character/` | Knowledge-character anti-collapse tests. |
| `tests/domains/atmosphere/policy-deny/` | Policy denial and fail-closed behavior tests. |
| `fixtures/domains/atmosphere/` | Preferred reusable fixture home. |
| `tools/validators/` | Validator implementation home; tests call into this, not the reverse. |
| `policy/domains/atmosphere/` | Atmosphere policy and deny-rule home. |
| `docs/domains/atmosphere/` | Human-facing domain lane documentation. |
| `data/registry/sources/atmosphere/` | Source registry lane, if/when present. |
| `release/candidates/atmosphere/` | Release candidate decisions, if/when present. |

---

## 14. Open questions

| Question | Status | Notes |
|---|---|---|
| What pytest marker names are canonical for no-network and integration tests? | NEEDS VERIFICATION | Candidate markers include `no_network`, `offline`, and `integration`, but this README does not establish them. |
| Is there a repo-wide network blocker fixture? | NEEDS VERIFICATION | Could live in root test configuration or shared test utilities if implemented. |
| Is there a governed fixture manifest schema? | NEEDS VERIFICATION | If yes, that schema should replace the informal field table above. |
| Are fixture checksums required for all reusable fixtures? | OPEN | Recommended for non-trivial fixtures. |
| Should Atmosphere have a dedicated fixture generator? | OPEN | If created, generator belongs under `tools/` or `scripts/` depending on reuse and governance. |
| Should live-source smoke checks exist? | OPEN | If they exist, keep them integration/manual and excluded from default CI. |
| What CI job proves default offline behavior? | NEEDS VERIFICATION | Must be checked against `.github/workflows/`. |

---

## 15. Definition of done

This lane is ready for mature use when:

- [ ] Default Atmosphere tests pass without internet access.
- [ ] Network attempts fail deterministically in default tests.
- [ ] Integration/live-source tests, if any, are opt-in and separately marked.
- [ ] Fixture roots are allowlisted and documented.
- [ ] Reusable fixtures live under `fixtures/domains/atmosphere/` or another declared canonical fixture root.
- [ ] Fixture manifests, if used, are validated by schema or contract.
- [ ] Fixtures are public-safe and do not contain secrets or restricted detail.
- [ ] Fixture data cannot be mistaken for RAW, PROCESSED, CATALOG, PUBLISHED, receipt, proof, or release authority.
- [ ] Emergency-advisory context fixtures do not make KFM the issuing authority.
- [ ] CI exposes the offline/no-network proof clearly enough for reviewers.

---

## 16. Changelog

| Date | Version | Change |
|---|---:|---|
| 2026-07-05 | v0.1 | Initial governed README for the Atmosphere no-network fixture test lane. |

---

## 17. Last reviewed

**2026-07-05** — Initial README scaffold. Path presence verified in current session; test implementation, fixture inventory, network blocker, markers, and CI job names remain **NEEDS VERIFICATION**.

[↑ Back to top](#top)
