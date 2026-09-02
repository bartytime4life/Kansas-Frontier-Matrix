<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-epa-aqs-readme
title: connectors/epa_aqs/ — EPA AQS / AirData Connector Lane
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Source steward · Atmosphere domain steward · Connector steward · Validation steward · Docs steward
created: 2026-06-16
updated: 2026-07-11
policy_label: public
related:
  - ../README.md
  - ../epa/README.md
  - ../../docs/sources/catalog/epa/aqs-airdata.md
  - ../../docs/sources/catalog/epa/README.md
  - ../../docs/domains/atmosphere/PIPELINE.md
  - ../../data/registry/sources/
  - ../../data/raw/atmosphere/
  - ../../data/quarantine/atmosphere/
  - ../../schemas/contracts/v1/source/
  - ../../policy/
  - ../../release/
tags: [kfm, connectors, epa-aqs, airdata, atmosphere, air-quality, source-admission, raw, quarantine]
notes:
  - "This README documents an AQS/AirData connector lane scaffold, not an implemented or activated connector."
  - "At the inspected base commit, connectors/epa_aqs/ contains only README.md."
  - "The relationship between connectors/epa_aqs/ and the broader connectors/epa/ lane remains NEEDS VERIFICATION and must not create parallel source authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# EPA AQS / AirData Connector Lane

> Repository boundary for a proposed EPA Air Quality System (AQS) and AirData source-intake adapter.

> [!IMPORTANT]
> **Document lifecycle:** draft  
> **Component maturity:** experimental documentation scaffold  
> **Owner:** `OWNER_TBD`  
> **Truth posture:** path and current one-file inventory are confirmed at base commit `d55923f`; connector code, source activation, endpoint behavior, tests, CI, and emitted artifacts remain unverified.

`connectors/epa_aqs/`

## Quick navigation

- [Scope](#scope)
- [Repository fit](#repository-fit)
- [Confirmed current state](#confirmed-current-state)
- [Authority boundary](#authority-boundary)
- [AQS and AirData source posture](#aqs-and-airdata-source-posture)
- [Lifecycle handoff](#lifecycle-handoff)
- [Proposed connector contract](#proposed-connector-contract)
- [Relationship to connectors/epa](#relationship-to-connectorsepa)
- [Safety and runtime posture](#safety-and-runtime-posture)
- [Testing expectations](#testing-expectations)
- [Definition of done](#definition-of-done)
- [Verification backlog](#verification-backlog)

---

## Scope

`connectors/epa_aqs/` is reserved for source-specific fetch and admission behavior for EPA AQS / AirData material when the repository intentionally maintains that behavior as a distinct connector lane.

A future implementation may:

- contact steward-approved AQS or AirData interfaces when explicitly enabled;
- retrieve bounded ambient-air-monitoring source payloads;
- preserve monitor, parameter, method, qualifier, time, unit, retrieval, and source identifiers;
- prepare material for RAW admission;
- route malformed, incomplete, rights-unclear, stale, unexpected, or policy-sensitive material toward QUARANTINE;
- emit bounded connector outcomes and drift signals;
- support deterministic, no-network tests with minimized fixtures.

This lane must not become:

- EPA or AQS source truth;
- Atmosphere domain doctrine;
- the canonical SourceDescriptor home;
- schema or contract authority;
- policy authority;
- a data-normalization pipeline for processed atmosphere records;
- catalog, triplet, proof, receipt, release, or publication authority;
- a direct UI or MapLibre data source.

---

## Repository fit

Directory Rules place source-specific fetchers and admitters under `connectors/`. AQS is an EPA source product used by the Atmosphere domain; it is not a new repository root or an independent truth domain.

```text
connectors/
├── epa/                         # broader EPA connector lane
└── epa_aqs/
    └── README.md                # this file; current confirmed inventory
```

Related responsibility homes:

```text
docs/sources/catalog/epa/aqs-airdata.md   # source-product documentation
docs/domains/atmosphere/                  # atmosphere domain doctrine and pipeline guidance
data/registry/sources/                    # canonical source descriptors and activation state
data/raw/atmosphere/                      # immutable or source-faithful admitted payloads
data/quarantine/atmosphere/               # held material requiring review
schemas/contracts/v1/source/              # source/admission machine shapes, subject to accepted schema-home rules
policy/                                   # rights, sensitivity, admissibility, and release policy
pipelines/                                # downstream normalization and domain processing
release/                                  # release, correction, withdrawal, and rollback decisions
```

> [!CAUTION]
> The existence of both `connectors/epa/` and `connectors/epa_aqs/` must not create two competing homes for EPA source identity, rights, activation state, shared transport behavior, or release decisions.

---

## Confirmed current state

At base commit `d55923f8956c8da70e9e00b4c926e56e4923ea32`:

| Item | Status | Evidence boundary |
|---|---:|---|
| `connectors/epa_aqs/README.md` | **CONFIRMED** | The file exists in the repository. |
| Additional code or configuration below `connectors/epa_aqs/` | **UNKNOWN / not observed** | Repository code search returned only this README for the lane. Absence is bounded to the inspected search and ref. |
| AQS / AirData product documentation | **CONFIRMED** | `docs/sources/catalog/epa/aqs-airdata.md` exists. |
| AQS connector implementation | **UNKNOWN** | No fetcher, parser, admission module, package metadata, or tests were verified in this lane. |
| Canonical SourceDescriptor activation | **NEEDS VERIFICATION** | Must be confirmed in the source registry. |
| Endpoint, pollutant, monitor, and cadence configuration | **NEEDS VERIFICATION** | Must be grounded in source descriptors and current steward review. |
| CI or runtime integration | **UNKNOWN** | No workflow run, test result, receipt, or emitted artifact was inspected. |

The source catalog page describes AQS / AirData as the validated, long-latency ambient-air-quality archive paired conceptually with real-time AirNow observations. That documentation is a product-page scaffold and does not prove connector activation or current endpoint behavior.

---

## Authority boundary

```text
THIS LANE MAY EVENTUALLY:
  fetch steward-approved AQS / AirData source material
  preserve source identity and retrieval metadata
  prepare RAW admission candidates
  route unsafe or unresolved material to QUARANTINE
  emit finite connector failures and source-drift signals
  support connector-local tests

THIS LANE MUST NOT:
  define canonical source identity, role, rights, or activation state
  decide environmental truth
  produce processed AirObservation authority records by itself
  publish data, tiles, reports, dashboards, or AI answers
  write directly to CATALOG, TRIPLET, PUBLISHED, proof, receipt, or release stores
  bypass evidence, policy, review, correction, or rollback gates
  embed credentials, tokens, private URLs, or uncontrolled source dumps
```

The trust membrane remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Promotion is a governed state transition. A successful AQS fetch is not validation, evidence closure, catalog closure, release, or publication.

---

## AQS and AirData source posture

The product documentation supports the following intended distinction:

| Concern | Required posture |
|---|---|
| Source role | Set by the canonical SourceDescriptor; do not hard-code authority claims in connector code. |
| Temporal meaning | Preserve source, observed, valid, retrieval, release, and correction times where material. |
| Quality state | Preserve qualifiers, methods, nulls, exceptional-event flags, revisions, and validation status without silently normalizing them away. |
| Units | Carry source units and explicit conversion provenance; never infer undocumented conversions. |
| Monitor identity | Preserve stable source identifiers and location/version context; do not merge monitors by label alone. |
| Pollutant scope | Define an explicit allowlist through reviewed configuration or descriptors. |
| Cadence | Treat watcher and refresh schedules as operational configuration, not README authority. |
| Geography | Kansas-only versus national retrieval scope remains a steward decision. |
| Rights and terms | Verify before source activation; unresolved posture routes to quarantine or denial. |
| AirNow relationship | Keep real-time and validated historical observations distinct; any reconciliation is a downstream derived product. |

AQS records must not be presented as real-time observations when the source product represents validated historical data. Conversely, real-time AirNow material must not silently inherit AQS validation status.

---

## Lifecycle handoff

| Stage | Connector-lane responsibility |
|---|---|
| Pre-RAW / source contact | Validate source activation, bounded request scope, network permission, and required configuration before contact. |
| RAW | Preserve source-faithful payloads or references with retrieval metadata and digest support. |
| QUARANTINE | Hold malformed, incomplete, drifted, rights-unclear, unexpectedly sensitive, or unsupported payloads. |
| WORK | Downstream responsibility; may consume admitted material through explicit interfaces. |
| PROCESSED | Atmosphere pipeline responsibility, not connector authority. |
| CATALOG / TRIPLET | Downstream catalog and projection responsibility. |
| PUBLISHED | Governed release only; outside this connector lane. |
| CORRECTION / ROLLBACK | Release and governance responsibility. |

The connector should return or prepare an explicit admission outcome rather than silently succeeding with partial data.

Suggested finite outcomes, subject to repository contract verification:

- `ADMIT_RAW`
- `QUARANTINE`
- `ABSTAIN`
- `DENY`
- `ERROR`

These names are **PROPOSED** until verified against the repository’s accepted connector and event contracts.

---

## Proposed connector contract

The following structure is a future design, not a claim about current files:

```text
connectors/epa_aqs/
├── README.md
├── src/
│   └── epa_aqs/
│       ├── README.md
│       ├── fetch.py
│       ├── parse.py
│       ├── admit.py
│       └── errors.py
└── tests/
    └── README.md
```

Before creating these paths, compare the broader `connectors/epa/` lane and determine whether shared EPA behavior belongs there instead.

| Proposed concern | Contract requirement |
|---|---|
| Fetch | Bounded requests, explicit parameters, timeout, user agent, rate-limit handling, and no hidden retries. |
| Parse | Preserve source fields and uncertainty; reject or quarantine unexpected schema changes. |
| Admit | Emit RAW or QUARANTINE candidates only; never publish. |
| Identity | Retain source monitor, parameter, sample, method, and temporal identifiers. |
| Provenance | Record source descriptor reference, retrieval time, request fingerprint, response digest, and connector version where supported. |
| Errors | Return actionable finite outcomes without credentials or excessive payload content. |
| Network | Disabled or mocked by default for tests and local dry runs. |

Do not create local copies of canonical descriptors, contracts, schemas, policies, or release manifests merely to make the connector self-contained.

---

## Relationship to `connectors/epa/`

The repository currently has both a broader EPA connector lane and this AQS-specific lane. The intended ownership split is **NEEDS VERIFICATION**.

Acceptable resolutions include:

1. **Distinct product connector:** `epa_aqs` owns AQS-specific protocol and parsing behavior, while `epa` owns only genuinely shared EPA utilities.
2. **Subpackage migration:** AQS behavior moves under `connectors/epa/` and this lane becomes a documented compatibility path before retirement.
3. **Registry-only alias:** This lane remains documentation-only while implementation is consolidated elsewhere.

The chosen resolution should be documented before substantive code is added. It must avoid:

- duplicate HTTP clients;
- duplicate descriptor authority;
- inconsistent rights or source-role declarations;
- divergent error envelopes;
- separate release paths;
- two source IDs for the same admitted product without an explicit crosswalk.

A rename, retirement, or compatibility mapping should use a reversible migration note or ADR when required by repository governance.

---

## Safety and runtime posture

A future implementation should follow these defaults:

- importing connector modules performs no network I/O;
- live calls require explicit source activation and runtime opt-in;
- default tests run without internet access;
- credentials are never committed or printed;
- request ranges, parameter lists, pollutants, dates, and geography are bounded;
- retries are finite and observable;
- large responses are streamed or size-bounded where supported;
- response metadata and digests are retained without storing unnecessary copies;
- unexpected schema or code-list changes fail closed;
- no connector response is treated as a direct UI payload;
- no model or AI component fills missing source values.

> [!WARNING]
> Air-quality observations can carry consequential health context. This connector must preserve source qualifiers, temporal scope, units, validation state, and uncertainty. It must not generate medical advice, emergency alerts, or unsupported safety conclusions.

---

## Testing expectations

No connector-local tests were verified for this lane at the inspected commit.

A future test surface should include:

- no-network default tests;
- request-parameter and date-range bounding;
- successful, empty, malformed, partial, forbidden, timeout, and rate-limited responses;
- source-schema and code-list drift;
- monitor and parameter identity preservation;
- unit and qualifier preservation;
- observed-time versus retrieval-time handling;
- RAW versus QUARANTINE routing;
- absence of direct writes to processed, catalog, triplet, published, proof, receipt, or release stores;
- secret and private-URL leak checks.

Use minimized, synthetic, or rights-reviewed fixtures. Do not commit large source dumps merely to exercise parsing.

The exact test command remains **UNKNOWN** until package and CI wiring exist and are inspected.

---

## Definition of done

This connector lane is ready to move beyond documentation scaffold only when:

- [ ] Ownership between `connectors/epa_aqs/` and `connectors/epa/` is documented.
- [ ] A canonical AQS SourceDescriptor exists and is reviewable.
- [ ] Source role, rights, terms, cadence, geographic scope, pollutant scope, and activation state are resolved.
- [ ] Connector code exists under a verified package structure.
- [ ] Importing the package performs no network I/O.
- [ ] Live access is explicit, bounded, and fail-closed.
- [ ] RAW and QUARANTINE handoff contracts are verified.
- [ ] Source identifiers, times, units, qualifiers, validation state, and digests are preserved.
- [ ] Connector-local tests pass with network disabled.
- [ ] Source drift and incomplete payloads produce reviewable outcomes.
- [ ] No direct path exists from connector output to public UI or publication.
- [ ] Downstream atmosphere processing, evidence, policy, release, correction, and rollback ownership is documented.

---

## Verification backlog

| Item | Status | Evidence required |
|---|---:|---|
| Confirm whether this lane is canonical, compatibility-only, or planned for migration. | **NEEDS VERIFICATION** | ADR, per-root README, issue, migration note, or maintainer decision. |
| Confirm complete files below `connectors/epa_aqs/`. | **NEEDS VERIFICATION** | Non-truncated repository tree at the target commit. |
| Confirm AQS SourceDescriptor identity and activation state. | **NEEDS VERIFICATION** | Source registry record and steward review. |
| Confirm current AQS / AirData access method and endpoint contract. | **NEEDS VERIFICATION** | Canonical descriptor and authoritative source review. |
| Confirm Kansas versus national retrieval scope. | **NEEDS VERIFICATION** | Product requirement and source configuration. |
| Confirm retained pollutants, standards, units, and aggregation rules. | **NEEDS VERIFICATION** | Atmosphere contracts, schemas, policy, and tests. |
| Confirm monitor identity and temporal versioning rules. | **NEEDS VERIFICATION** | Domain contracts, fixtures, and validator results. |
| Confirm relationship to AirNow material. | **NEEDS VERIFICATION** | Source-role decision and reconciliation design. |
| Confirm package manager, import path, tests, and CI wiring. | **UNKNOWN** | Repository configuration and successful checks. |
| Confirm emitted admission/event/receipt object families. | **NEEDS VERIFICATION** | Accepted contracts, schemas, fixtures, and generated artifacts. |

---

## Maintainer note

Keep this lane narrow, source-specific, and reversible. Its job is to make AQS / AirData material safer to contact, admit, inspect, quarantine, and hand off. It must not make air-quality data appear more current, validated, complete, precise, or publishable than its source descriptor, evidence, policy, review, and release state support.
