<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-noaa-src-noaa-readme
title: connectors/noaa/src/noaa/ — NOAA Connector Python Package Boundary
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Source steward · Connector steward · NOAA steward · Hazards steward · Atmosphere steward · Climate steward · Soil steward · Data steward · Validation steward · Security steward · Docs steward
created: 2026-07-14
updated: 2026-07-14
policy_label: "public-doctrine; implementation-boundary; source-admission; multi-role; not-life-safety; import-safe; no-network-by-default; raw-quarantine-only; descriptor-gated; rights-aware; sensitivity-aware; finite-outcomes; replayable; rollback-aware; no-secrets"
current_path: connectors/noaa/src/noaa/README.md
truth_posture: CONFIRMED target path and prior empty blob, empty package __init__.py, parent NOAA connector README, NOAA source-root README, NOAA test-root README, connector-root contract, NOAA source-family catalog, proposed source-admission ADR, package project name and 0.0.0 version, and absence of client.py at the proposed path / PROPOSED package responsibility contract, import surface, configuration, transport, product adapters, parser interfaces, admission-candidate model, finite outcomes, error taxonomy, provenance capture, and test plan / UNKNOWN complete directory inventory, package installability, dependencies, import consumers, source descriptor IDs, active NOAA products, live endpoints, parsers, fixtures, runtime orchestration, emitted receipts, CI, schedules, deployment, and health / NEEDS VERIFICATION owners, package namespace, parent README drift, source-schema path drift, activation states, rights and sensitivity bindings, admission contract, validators, tests, CI, correction, and rollback automation
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 63a04206d7cb5c51b6fc45caf684c1c731cc177d
  prior_blob: 8b137891791fe96927ad78e64b0aad7bded08bdc
  bounded_path_checks:
    - connectors/noaa/src/noaa/README.md was empty
    - connectors/noaa/src/noaa/__init__.py was empty
    - connectors/noaa/src/noaa/client.py was not found
    - connectors/noaa/pyproject.toml contained only project name and version 0.0.0
related:
  - ../README.md
  - ../../README.md
  - ../../tests/README.md
  - ../../pyproject.toml
  - ../../../README.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../docs/adr/ADR-0017-source-descriptor-admission-process.md
  - ../../../../docs/sources/catalog/noaa/README.md
  - ../../../../docs/sources/catalog/noaa/storm-events.md
  - ../../../../docs/sources/catalog/noaa/nws-api.md
  - ../../../../docs/sources/catalog/noaa/hms-fire-smoke.md
  - ../../../../docs/sources/catalog/noaa/hrrr-smoke.md
  - ../../../../docs/sources/catalog/noaa/goes-abi-aod.md
  - ../../../../docs/sources/catalog/noaa/viirs-hotspot.md
  - ../../../../docs/sources/catalog/noaa/noaa-uscrn.md
  - ../../../../docs/sources/catalog/noaa/station-climate-products.md
  - ../../../../data/registry/sources/README.md
  - ../../../../data/raw/
  - ../../../../data/quarantine/
  - ../../../../data/receipts/
  - ../../../../data/proofs/
  - ../../../../policy/rights/
  - ../../../../policy/sensitivity/
  - ../../../../release/
tags: [kfm, connectors, noaa, python-package, source-admission, multi-role, ncei, nws, hms, hrrr, goes, viirs, uscrn, storm-events, climate, hazards, atmosphere, soil, raw, quarantine, provenance, import-safety, no-network, governance]
notes:
  - "This revision changes only connectors/noaa/src/noaa/README.md."
  - "The target and __init__.py exist but were empty in the bounded inspection; package behavior is not established."
  - "The parent source-root README still labels this package as PROPOSED even though the path is repository-present; that documentation drift is recorded but not changed here."
  - "The package project metadata is version 0.0.0 and does not establish a build backend, dependencies, package discovery, entry points, or installability."
  - "NOAA is a multi-role source family; product-specific identity, time, role, units, quality, geometry, uncertainty, rights, sensitivity, and caveats must remain distinct."
  - "KFM is not an emergency alerting system."
  - "Connector code may support RAW or QUARANTINE admission only; it may not publish, promote, close evidence, certify truth, or serve public clients."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# NOAA Connector Python Package Boundary

`connectors/noaa/src/noaa/`

> Import-package boundary for NOAA source fetch, parse, provenance, and admission helpers. This package may prepare product-specific NOAA material for governed **RAW** or **QUARANTINE** handoff; it does not establish NOAA truth, issue alerts, approve publication, or bypass KFM governance.

![status](https://img.shields.io/badge/status-draft-yellow)
![version](https://img.shields.io/badge/version-v0.1-informational)
![maturity](https://img.shields.io/badge/maturity-empty__package__shell-lightgrey)
![package](https://img.shields.io/badge/package-kfm--connector--noaa-blue)
![source role](https://img.shields.io/badge/source--role-multi--role-purple)
![network](https://img.shields.io/badge/network-off__by__default-critical)
![lifecycle](https://img.shields.io/badge/lifecycle-RAW%20%7C%20QUARANTINE-orange)
![life safety](https://img.shields.io/badge/life__safety-NOT__ALERT__AUTHORITY-red)

**Quick links:** [Purpose](#purpose) · [Status](#status-and-evidence) · [Authority](#authority-boundary) · [Directory basis](#repository-fit-and-directory-rules-basis) · [Package contract](#package-contract) · [Imports](#import-and-side-effect-contract) · [Configuration](#configuration-contract) · [Transport](#transport-contract) · [Products](#product-adapter-contract) · [Parsing](#parsing-and-preservation-contract) · [Admission](#admission-candidate-contract) · [Outcomes](#finite-outcome-contract) · [Errors](#error-and-quarantine-taxonomy) · [Provenance](#provenance-identity-and-time) · [Policy](#rights-sensitivity-and-life-safety-boundaries) · [Testing](#testing-and-validation) · [Implementation](#smallest-sound-implementation-sequence) · [Done](#definition-of-done) · [Open](#open-verification-register) · [Rollback](#rollback-correction-and-supersession)

> [!IMPORTANT]
> **This package is an intake adapter, not an authority surface.** A valid response from a NOAA system is still source material. Source activation, record admission, rights, sensitivity, validation, evidence closure, review, release, correction, and rollback remain separate governed decisions.

> [!CAUTION]
> **Repository presence is not implementation proof.** Bounded inspection confirmed an empty package README, an empty `__init__.py`, and `0.0.0` project metadata. It did not establish a working client, parsers, product registry, schemas, fixtures, tests, CI, live access, receipts, or production use.

---

<a id="purpose"></a>

## Purpose

This README defines the implementation boundary for the Python package at `connectors/noaa/src/noaa/`.

The package may eventually support:

- explicit connector configuration;
- bounded HTTP or file-distribution transport;
- approved fixture loading;
- product-family dispatch;
- product-specific parsing;
- source-native metadata preservation;
- source-role candidate preservation;
- rights, attribution, and sensitivity context propagation;
- retrieval and content-integrity metadata capture;
- finite connector outcomes;
- RAW or QUARANTINE admission candidates;
- deterministic replay from captured payloads;
- no-network tests.

It must not become:

- a NOAA source-family catalog or SourceDescriptor registry;
- a general weather SDK;
- a KFM emergency-alert service;
- a truth resolver or domain canonicalizer;
- an evidence-closure engine;
- a rights, sensitivity, or release authority;
- a scheduler or watcher authority;
- a processing, catalog, triplet, or publication pipeline;
- a public API, UI, map, search, or AI authority.

[Back to top](#top)

---

<a id="status-and-evidence"></a>

## Status and evidence

| Surface | Status | Safe conclusion |
|---|---:|---|
| `connectors/noaa/src/noaa/README.md` | **CONFIRMED empty before this revision** | The path existed but defined no package boundary. |
| `connectors/noaa/src/noaa/__init__.py` | **CONFIRMED empty** | The package marker exists; no public API or behavior is established. |
| `connectors/noaa/src/noaa/client.py` | **NOT FOUND in bounded check** | The source-root README's proposed client is not implemented at that path. |
| `connectors/noaa/pyproject.toml` | **CONFIRMED placeholder** | Project name is `kfm-connector-noaa`; version is `0.0.0`. |
| Build backend, package discovery, dependencies | **UNKNOWN** | The inspected project file does not establish them. |
| Parent NOAA connector README | **CONFIRMED draft** | Defines multi-role, RAW/QUARANTINE-only, not-life-safety posture. |
| NOAA source-root README | **CONFIRMED draft with drift** | Proposes this package but still describes it as future despite path presence. |
| NOAA test-root README | **CONFIRMED draft** | Defines no-network and product-specific test expectations. |
| NOAA source catalog | **CONFIRMED draft doctrine** | Defines heterogeneous product lanes and anti-collapse rules. |
| Source-admission ADR | **CONFIRMED repository-present; status proposed** | Defines descriptor and record admission, fixture-first work, and RAW/QUARANTINE handoff. |
| Complete package tree | **UNKNOWN** | No full directory listing was available in the bounded inspection. |
| Product code, fixtures, tests, CI, schedules, deployment | **NOT SURFACED / UNKNOWN** | No implementation or operational proof was established. |

This README does not claim that `noaa` is installable, importable in the standard environment, connected to live NOAA endpoints, source-activated, tested, scheduled, deployed, or consumed by downstream code.

[Back to top](#top)

---

<a id="authority-boundary"></a>

## Authority boundary

### This package may own

If implemented and reviewed:

- package-local configuration types;
- bounded transport interfaces;
- request canonicalization;
- response metadata capture;
- explicit product adapter interfaces;
- product-specific parsers;
- package-local parsed-record types;
- admission-candidate construction;
- finite package-local error types;
- content-digest and replay helpers;
- explicit hooks for external descriptor, rights, sensitivity, and receipt systems.

### This package does not own

| Concern | Owning boundary |
|---|---|
| NOAA source-family and product meaning | `docs/sources/catalog/noaa/` |
| Active source inventory and activation | `data/registry/sources/` and accepted source-governance artifacts |
| Source contracts and schemas | `contracts/` and `schemas/` under repository-confirmed homes |
| Rights and sensitivity decisions | `policy/rights/`, `policy/sensitivity/` |
| Domain truth and evidence closure | Domain contracts, validators, EvidenceBundles, and review |
| WORK, PROCESSED, CATALOG, TRIPLET | Downstream lifecycle roots |
| Receipts and proofs as authority | `data/receipts/`, `data/proofs/` |
| Release and published artifacts | `release/`, `data/published/` |
| Public service behavior | `apps/governed-api/` and governed UI surfaces |
| Emergency alerts or life-safety instructions | Official NOAA/NWS and local emergency authorities |

```text
External NOAA source or approved fixture
    -> connectors/noaa/src/noaa/
    -> RAW candidate or QUARANTINE candidate
    -> external orchestration persists governed handoff
    -> WORK / QUARANTINE
    -> PROCESSED
    -> CATALOG / TRIPLET
    -> PUBLISHED
```

The package must never compress that lifecycle into `NOAA response -> public layer`.

[Back to top](#top)

---

<a id="repository-fit-and-directory-rules-basis"></a>

## Repository fit and Directory Rules basis

`connectors/` is the correct responsibility root because this package concerns source-specific fetch, probe, parse, and admission behavior.

The nested source layout separates implementation from doctrine, tests, lifecycle data, policy, and release authority.

Bounded checked snapshot:

```text
connectors/noaa/
├── README.md
├── pyproject.toml              # confirmed minimal 0.0.0 metadata
├── src/
│   ├── README.md
│   └── noaa/
│       ├── README.md           # this file; previously empty
│       └── __init__.py         # confirmed empty
└── tests/
    └── README.md
```

> [!NOTE]
> This is not a complete directory listing. It records only directly checked files.

The existing `src/noaa/` path is a compatibility surface. Do not rename or duplicate it without consumer search, package/build verification, migration notes or ADR support, tests, compatibility handling, and rollback.

The parent source-root README should later be corrected to distinguish **package presence** from **implementation maturity**.

[Back to top](#top)

---

<a id="package-contract"></a>

## Package contract

A caller should eventually be able to:

1. choose one explicitly supported NOAA product adapter;
2. supply descriptor and request context;
3. fetch through an injected transport or provide captured bytes;
4. parse without network access;
5. preserve source-native metadata and caveats;
6. receive a finite result;
7. route the result to RAW or QUARANTINE through external orchestration;
8. emit or request receipts through the governing receipt boundary.

### Invariants

1. Importing the package performs no network, secret read, write, scheduler registration, or lifecycle mutation.
2. An adapter does not activate a source.
3. Descriptor context precedes live fetch.
4. NOAA products retain distinct identities, roles, cadences, units, time semantics, and caveats.
5. Parsing does not turn source material into KFM truth.
6. Observation, issue, valid, expiry, run, file-vintage, correction, and retrieval times remain distinct.
7. Native units and quality flags are not silently discarded or reinterpreted.
8. Missing rights or sensitivity context fails closed or routes to quarantine.
9. NOAA/NWS material never becomes KFM-issued life-safety guidance.
10. Persistence targets are explicit and external.
11. Operations terminate with finite outcomes.
12. Captured bytes, configuration, and parser versions support replay where practical.
13. AI or generated text cannot replace source bytes or evidence.
14. The package never promotes or publishes.
15. Parser corrections remain traceable and reversible.

[Back to top](#top)

---

<a id="import-and-side-effect-contract"></a>

## Import and side-effect contract

The following must be inert:

```python
import noaa
```

Required import posture:

```text
network calls:             none
DNS resolution:            none
credential reads:          none
filesystem writes:         none
lifecycle writes:          none
scheduler registration:    none
global logging changes:    none
telemetry emission:        none
source activation:         none
```

Import must not fail merely because the network is unavailable, live tests are off, no credential exists, an optional product dependency is absent, or a source descriptor is inactive.

Network sessions, clocks, writers, descriptor resolvers, receipt emitters, and policy evaluators should be injected explicitly.

Because `noaa` is a broad import name, verify package collision and workspace resolution before implementation. A namespace change is migration work, not cleanup.

[Back to top](#top)

---

<a id="configuration-contract"></a>

## Configuration contract

Configuration must be explicit, validated at invocation time, and safe by default.

| Family | Required posture |
|---|---|
| Product selection | Select one reviewed product key; do not infer support from a NOAA URL alone. |
| Descriptor reference | Required for live fetch and bound to the selected product. |
| Network mode | Fixture or captured mode by default; live mode explicit. |
| Endpoint key | Reviewed named key preferred over arbitrary URL. |
| Timeouts and retries | Finite, conservative, observable. |
| Rate limits | Explicit; no uncontrolled polling. |
| Spatial/temporal scope | Bounded and reviewable. |
| Integrity | Digest algorithm and verification expectation explicit. |
| Rights/sensitivity | References or unresolved state explicit. |
| Output mode | Return-only preferred; caller-supplied RAW/QUARANTINE writer if approved. |
| Live tests | Disabled by default. |

Configuration must not contain committed secrets, direct published-store paths, silent role overrides, guessed unit conversions, unbounded date ranges, or release switches.

[Back to top](#top)

---

<a id="transport-contract"></a>

## Transport contract

Transport retrieves bytes and transport metadata. It does not interpret product meaning.

It should preserve:

- endpoint/distribution key;
- canonical request parameters;
- retrieval time;
- status or file-access outcome;
- safe `ETag` / `Last-Modified` metadata when supplied;
- content type, encoding, and length;
- enforced size limit;
- content digest;
- safe redirect history;
- retry and rate-limit outcome;
- source URL or object key with required redaction.

It must not parse semantics, infer source role, infer publication eligibility, retry indefinitely, download unbounded content, log credentials, mutate global client state, or write beyond approved RAW/QUARANTINE handoff.

`304 Not Modified` or unchanged digest is an explicit no-change outcome, not a new source fact.

[Back to top](#top)

---

<a id="product-adapter-contract"></a>

## Product adapter contract

NOAA is not one product. Each supported product family needs a distinct adapter or reviewed adapter profile.

| Product family | Preserve | Reject collapse into |
|---|---|---|
| Storm Events | Event/episode IDs, file/table type and vintage, event type, narrative, geometry, magnitude type/value, damage/casualty fields, corrections | Current alert, direct sensor measurement, universal disaster declaration |
| NWS API | Product type, office/zone/grid context, issue/valid/expiry times, status, message IDs | KFM-issued warning, emergency instruction, guaranteed forecast truth |
| HMS Fire and Smoke | Fire detections and smoke polygons separately, analysis date, density category | PM2.5 concentration, exposure dose, ground-fire confirmation |
| HRRR-Smoke | Model cycle, forecast hour, valid time, grid/projection, variable, units, model version | Observation or deterministic future truth |
| GOES ABI AOD | Platform/sensor, product version, retrieval time, grid/pixel metadata, quality flags | PM2.5 or regulatory air quality |
| VIIRS hotspot | Platform/sensor, acquisition time, detection location, confidence/quality | Confirmed incident perimeter or evacuation need |
| USCRN | Station ID, timestamp, variable, units, QC flags, cadence, soil depth, raw/derived status, vintage | Area-wide truth or depth-collapsed soil condition |
| Station climate products | Product/station ID, observation/normal/anomaly distinction, averaging period, baseline, revision | One generic NOAA observation role |
| Future product | Product-specific schema, role, cadence, rights, sensitivity, time, and caveats | Automatic support because publisher is NOAA |

Unknown product keys must fail closed or route to quarantine. Adapter changes affecting interpretation, units, IDs, time, geometry, role, or admission outcome require versioning and fixture revalidation.

[Back to top](#top)

---

<a id="parsing-and-preservation-contract"></a>

## Parsing and preservation contract

Parsing converts captured bytes into an inspectable package-local representation without asserting downstream truth.

A parser may decode, validate basic shape, preserve native fields, parse timestamps while retaining source values, parse geometry while retaining precision and CRS, calculate record digests, surface unknown fields, and reject unsupported content.

A parser must not:

- fabricate missing fields or silently repair contradictions;
- guess timezone or units;
- discard quality flags;
- convert smoke density or AOD into PM2.5;
- turn detections into confirmed incidents;
- turn station values into area values;
- turn forecasts into observations;
- turn historical events into current alerts;
- enrich through hidden web requests;
- call AI to fill gaps;
- create domain canonical objects or choose release posture.

Where practical retain original field/value, normalized value, units, quality flags, missing-value code, source record ID, source file identity, parser version, and warnings.

Unexpected fields must be preserved, quarantined, rejected, or explicitly ignored under a documented product rule—never silently dropped.

[Back to top](#top)

---

<a id="admission-candidate-contract"></a>

## Admission candidate contract

The preferred package output is a source-admission candidate returned to external orchestration.

A proposed candidate should bind:

- product, distribution, and adapter version;
- SourceDescriptor and activation snapshot references;
- request digest and bounded request metadata;
- payload digest, size, media type, and retrieval time;
- native file/object/record identity and source vintage;
- distinct time fields;
- source-role candidate and caveats;
- rights and sensitivity context;
- parser warnings and drift state;
- RAW or QUARANTINE target only;
- stable quarantine reason codes;
- receipt inputs and replay context.

RAW capture does not mean normalized admission passed.

Route to QUARANTINE when descriptor, rights, product identity, role, time, units, integrity, version, sensitivity, or correction state cannot be resolved safely.

Preferred pattern:

```text
package returns candidate -> orchestration writes governed target
```

Any future writer must accept an explicit target, enforce RAW/QUARANTINE-only paths, use atomic immutable writes, prevent path traversal, and never write to WORK, PROCESSED, CATALOG, TRIPLET, PUBLISHED, PROOFS, or RELEASE.

[Back to top](#top)

---

<a id="finite-outcome-contract"></a>

## Finite outcome contract

The exact machine enum remains **PROPOSED** and must be placed in an accepted contract/schema before callers depend on it.

| Outcome | Meaning |
|---|---|
| `CAPTURED` | Permitted bytes captured and a RAW candidate produced; not normalized admission. |
| `NOT_MODIFIED` | Conditional request or digest comparison found no new payload. |
| `QUARANTINED` | Material represented for review but cannot proceed normally. |
| `SKIPPED` | Operation did not run due to configuration, scope, or activation state. |
| `ABSTAINED` | Insufficient admissible context to choose safely. |
| `DENIED` | A governing rule blocks the operation. |
| `ERROR` | Transport, integrity, parser, configuration, or invariant failure. |

No outcome implies evidence closure or release approval.

If a downstream runtime requires `ANSWER | ABSTAIN | DENY | ERROR`, use an explicit adapter. Do not overload `ANSWER` to mean source truth or publication approval.

[Back to top](#top)

---

<a id="error-and-quarantine-taxonomy"></a>

## Error and quarantine taxonomy

Proposed stable families:

| Family | Conditions |
|---|---|
| `NOAA_CONFIG_*` | Invalid product, timeout, mode, or scope. |
| `NOAA_DESCRIPTOR_*` | Missing, inactive, mismatched, or stale descriptor context. |
| `NOAA_TRANSPORT_*` | Timeout, DNS, rate limit, redirect denial, excessive size. |
| `NOAA_INTEGRITY_*` | Digest mismatch, truncation, decompression failure. |
| `NOAA_MEDIA_*` | Unsupported content, encoding, compression, or archive layout. |
| `NOAA_PRODUCT_*` | Unknown product, unsupported version, adapter mismatch. |
| `NOAA_PARSE_*` | Invalid field, time, geometry, or required product content. |
| `NOAA_DRIFT_*` | Header, enum, unit, or schema/version drift. |
| `NOAA_ROLE_*` | Forecast-as-observation, station-as-area, detection-as-incident, family-wide role collapse. |
| `NOAA_RIGHTS_*` | Unknown terms, attribution, or permitted use. |
| `NOAA_SENSITIVITY_*` | Casualty, infrastructure, exact-location, or public-safety review. |
| `NOAA_LIFE_SAFETY_*` | Attempted KFM alert or emergency instruction. |
| `NOAA_OUTPUT_*` | Disallowed lifecycle target or unsafe write. |
| `NOAA_INTERNAL_*` | Invariant violation or adapter defect. |

Errors and logs must not expose credentials, signed URLs, authorization headers, full payloads, secrets, or speculative claims.

Quarantine results should include safe reason code, payload digest, product/adapter version, review owner, retry condition, and protected detail reference.

[Back to top](#top)

---

<a id="provenance-identity-and-time"></a>

## Provenance, identity, and time

Do not collapse source family, sub-agency, product, distribution, request, capture, source object, parsed record, admission candidate, and receipt identities.

Where practical:

```text
payload_identity = sha256(source_bytes)

capture_identity =
  descriptor_id
  + product_key
  + canonical_request_digest
  + retrieval_attempt_id

parsed_record_identity =
  product_key
  + source_native_id
  + source_vintage
  + normalized_record_digest
```

Preserve materially distinct:

- observation/event time;
- issue/effective time;
- valid and expiry time;
- model initialization and forecast lead;
- acquisition/analysis time;
- file vintage and update/correction time;
- retrieval and processing time.

Never substitute retrieval time for missing observation time or rewrite stale data to appear current.

A digest proves byte identity under an algorithm; it does not prove accuracy, rights, or publication eligibility.

[Back to top](#top)

---

<a id="rights-sensitivity-and-life-safety-boundaries"></a>

## Rights, sensitivity, and life-safety boundaries

The package may propagate rights and sensitivity context; it does not decide legal sufficiency or public tier.

Unknown terms, attribution, redistribution, automated-use, retention, or sensitivity posture must fail closed or route to quarantine.

NOAA-derived material may contain casualty, infrastructure, exact-location, operational weather, damage, station, or narrative detail requiring review.

### Not-life-safety invariant

This package must never:

- issue a KFM warning, watch, advisory, evacuation, shelter, medical, fire, flood, tornado, smoke, heat, or severe-weather instruction;
- escalate urgency beyond the source;
- represent cached or stale material as current life-safety guidance;
- imply KFM delivery reliability;
- transform analytical context into operational alert authority;
- generate instructions with AI from NOAA payloads.

```text
NWS alert context        != KFM-issued alert
Storm Events record      != current hazard alert
HMS smoke density        != PM2.5 concentration
GOES AOD                 != surface PM2.5
VIIRS hotspot            != confirmed incident perimeter
HRRR-Smoke forecast      != observation
USCRN station reading    != area-wide condition
NOAA source availability != publication permission
```

[Back to top](#top)

---

<a id="testing-and-validation"></a>

## Testing and validation

Connector-local tests belong under `connectors/noaa/tests/` and must be no-network by default.

| Test class | Required proof |
|---|---|
| Import safety | `import noaa` performs no network, secret read, write, registration, or telemetry. |
| Packaging | Namespace and build assumptions are explicit. |
| Configuration | Defaults are fixture/captured mode and bounded. |
| Descriptor gate | Missing/inactive/mismatched descriptor blocks live fetch. |
| Transport | Timeouts, limits, redirects, conditional requests, rates, and digests are bounded. |
| Dispatch | Unknown product fails closed. |
| Parser purity | Parsing bytes makes no network request or lifecycle write. |
| Preservation | Native IDs, values, units, flags, times, geometry, and versions survive. |
| Drift | Added/removed fields and unit/version drift are explicit. |
| Role anti-collapse | Forecast, observation, model, aggregate, alert-context, station, detection, and event roles remain distinct. |
| Life safety | No adapter emits KFM warning or instruction. |
| Admission | Results target RAW or QUARANTINE only. |
| Error safety | Finite outcomes; no secret or unbounded payload leakage. |
| Replay | Same bytes and versioned config produce stable results where practical. |
| Forbidden writes | No direct downstream lifecycle or publication writes. |

Required negative cases include:

- Storm Events as current alert;
- missing magnitude type guessed;
- NWS message transformed into KFM alert;
- expired product presented as current;
- HMS density or GOES AOD converted to PM2.5;
- VIIRS/HMS detection treated as confirmed incident;
- HRRR field labeled observation;
- USCRN station expanded to area;
- soil depths collapsed;
- climate normal labeled current observation;
- unknown NOAA product auto-accepted;
- unknown rights;
- response size overflow;
- digest mismatch;
- hidden live request during parser test;
- attempted published-store write.

Fixtures must be synthetic, minimized, redacted, or approved; product-specific; versioned; rights-safe; small; and free of credentials.

Proposed commands, **NEEDS VERIFICATION**:

```bash
python -m pytest connectors/noaa/tests
```

```bash
PYTHONPATH=connectors/noaa/src python -c "import noaa"
```

[Back to top](#top)

---

<a id="security-and-resource-controls"></a>

## Security and resource controls

- allow reviewed endpoint keys or hosts only;
- prevent SSRF through arbitrary URL input;
- validate redirects;
- set finite connect/read timeouts and retries;
- bound response size, record count, field size, and geometry complexity;
- stream approved large payloads;
- cap archive expanded size, file count, and decompression ratio;
- reject absolute paths, parent traversal, devices, and unsafe archive members;
- never execute downloaded content;
- never log credentials or signed query strings;
- prevent retry storms;
- make cancellation and timeout observable.

[Back to top](#top)

---

<a id="smallest-sound-implementation-sequence"></a>

## Smallest sound implementation sequence

### PR 1 — Packaging and namespace

Confirm complete tree, build backend, workspace conventions, namespace collision, package discovery, inert import, and parent README drift.

**Stop if:** package home or import namespace is unresolved.

### PR 2 — Results and errors

Add immutable package-local result/error types, safe strings, stable reason families, and unit tests. No network.

**Stop if:** a repository-wide connector contract already exists and should be reused.

### PR 3 — Descriptor-bound configuration

Require product and descriptor context for live mode; preserve fixture/captured mode; add fail-closed tests.

**Stop if:** SourceDescriptor contract, schema, or activation semantics are unresolved.

### PR 4 — Captured-byte transport

Add an injected transport interface and captured-file/bytes implementation with digests, limits, media metadata, archive safety, and no-network tests.

### PR 5 — One product adapter

Choose one product with an accepted descriptor, reviewed rights, safe fixture, clear role, and steward. Implement only that product.

### PR 6 — Admission candidate

Reuse an accepted contract/schema. If none exists, stop and create it in the correct authority roots before implementation.

### PR 7 — Receipts and live transport

Integrate external receipt emission, then add live transport behind activation, host controls, rates, limits, kill switch, and skipped-by-default smoke test.

### PR 8 — CI and docs

Run real tests, block forbidden writes, update parent/test docs and verification records with evidence.

Do not add a second adapter until the first proves descriptor gating, fixture-first tests, native preservation, finite outcomes, RAW/QUARANTINE-only handoff, receipts, drift handling, and rollback.

[Back to top](#top)

---

<a id="definition-of-done"></a>

## Definition of done

### Packaging and governance

- [ ] Namespace is accepted and collision-checked.
- [ ] Build backend, discovery, dependencies, and supported Python versions are explicit.
- [ ] `import noaa` is inert and tested.
- [ ] Owners replace `OWNER_TBD`.
- [ ] SourceDescriptor and activation semantics are confirmed.
- [ ] At least one product has an accepted descriptor, role, rights, sensitivity, and steward.
- [ ] Admission-candidate and receipt contracts are confirmed.
- [ ] Parent source-root documentation is reconciled.

### Implementation

- [ ] Configuration is explicit and fail-closed.
- [ ] Transport is injected and bounded.
- [ ] Live mode is off by default.
- [ ] One product adapter precedes broad expansion.
- [ ] Native IDs, times, units, quality, geometry, and caveats are preserved.
- [ ] Unknown products and drift fail closed.
- [ ] Outcomes are finite and errors are safe.
- [ ] Outputs are RAW/QUARANTINE candidates only.
- [ ] No direct downstream or publication writes exist.

### Validation and operations

- [ ] Synthetic/minimized valid and negative fixtures exist.
- [ ] Import, no-network, descriptor, rights, sensitivity, role, freshness, and life-safety tests pass.
- [ ] Integrity, archive, size, timeout, rate, retry, replay, and forbidden-write tests pass.
- [ ] CI runs real tests.
- [ ] Live activation has a kill switch.
- [ ] Source retirement blocks new fetches.
- [ ] Parser corrections identify affected captures and candidates.
- [ ] Rollback instructions are tested.

[Back to top](#top)

---

<a id="open-verification-register"></a>

## Open verification register

| ID | Item | Status | Evidence needed |
|---|---|---:|---|
| NOAA-PKG-001 | Complete package tree | **NEEDS VERIFICATION** | Repository tree or mounted checkout. |
| NOAA-PKG-002 | Import namespace and collision risk | **NEEDS VERIFICATION** | Workspace imports and build test. |
| NOAA-PKG-003 | Build backend, discovery, dependencies, Python versions | **UNKNOWN** | Complete packaging configuration. |
| NOAA-PKG-004 | Parent source-root documentation drift | **CONFIRMED drift** | Follow-up README update. |
| NOAA-PKG-005 | Canonical source contract/schema path | **NEEDS VERIFICATION** | Reconcile singular/plural references and ADRs. |
| NOAA-PKG-006 | NOAA descriptor IDs and activation states | **UNKNOWN** | Source registry and activation decisions. |
| NOAA-PKG-007 | Approved products and endpoint keys | **UNKNOWN** | Descriptors and steward review. |
| NOAA-PKG-008 | Rights, attribution, automated-use, and rates | **NEEDS VERIFICATION** | Rights assessment. |
| NOAA-PKG-009 | Product source roles and sensitivity bindings | **NEEDS VERIFICATION** | Accepted descriptors and policy. |
| NOAA-PKG-010 | Transport library and security defaults | **UNKNOWN** | Design, implementation, tests. |
| NOAA-PKG-011 | First product adapter | **UNDECIDED** | Steward selection and fixture. |
| NOAA-PKG-012 | Parsed-record and admission-candidate contracts | **PROPOSED / NEEDS VERIFICATION** | Contracts and schemas. |
| NOAA-PKG-013 | Finite connector enum and reason codes | **PROPOSED** | Reuse or create reviewed contract. |
| NOAA-PKG-014 | Receipt integration and persistence owner | **UNKNOWN** | Receipt and orchestration evidence. |
| NOAA-PKG-015 | Fixtures, test runner, live-test convention, CI | **UNKNOWN** | Test tree, workspace scripts, workflows. |
| NOAA-PKG-016 | Runtime consumers, schedules, metrics, health | **UNKNOWN** | Code graph, orchestration, dashboards. |
| NOAA-PKG-017 | Source retirement and correction flow | **NEEDS VERIFICATION** | Register, lineage, runbook, tests. |
| NOAA-PKG-018 | Downstream invalidation and rollback automation | **UNKNOWN** | Governed API/map/search/release evidence. |
| NOAA-PKG-019 | CODEOWNERS and separation of duties | **NEEDS VERIFICATION** | Ownership rules. |

[Back to top](#top)

---

<a id="rollback-correction-and-supersession"></a>

## Rollback, correction, and supersession

This revision changes documentation only.

Rollback options:

1. revert the documentation commit;
2. restore prior blob `8b137891791fe96927ad78e64b0aad7bded08bdc` to return the file to its previous empty state;
3. supersede this README with an implementation-aware version while preserving history.

Future parser correction should:

1. disable the affected adapter when consequence warrants;
2. identify affected payload digests and adapter versions;
3. prevent further promotion;
4. preserve original captures;
5. issue correction/supersession artifacts through the owning boundary;
6. reparse under a new version;
7. compare outputs;
8. quarantine uncertain cases;
9. notify downstream lineage/rollback owners;
10. update fixtures and docs.

A retired source or adapter must block new live fetches while preserving historical captures and lineage according to policy.

Any package move requires an accepted destination, consumer search, import compatibility plan, build/test updates, redirects/deprecation, and rollback. Do not create parallel active package authority.

[Back to top](#top)

---

<a id="maintainer-summary"></a>

## Maintainer summary

`connectors/noaa/src/noaa/` is currently a **package shell**, not a working NOAA connector.

The smallest safe next step is to confirm packaging and namespace, keep import inert, define finite results and errors, bind configuration to admitted source context, implement captured-byte parsing with no-network tests, and then add exactly one reviewed NOAA product adapter.

Keep the package evidence-bounded, product-specific, no-network by default, not-life-safety, RAW/QUARANTINE-only, and reversible.

<p align="right"><a href="#top">Back to top</a></p>
