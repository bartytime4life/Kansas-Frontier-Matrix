<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-noaa-readme
title: connectors/noaa/ — NOAA Connector Family Admission Boundary
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Source steward · Connector steward · NOAA steward · Hazards steward · Atmosphere steward · Climate steward · Soil steward · Hydrology liaison · Agriculture liaison · Rights reviewer · Sensitivity reviewer · Security steward · Validation steward · Migration steward · CI steward · Docs steward
created: 2026-06-19
updated: 2026-07-15
policy_label: "public-doctrine; connector-family; source-admission; multi-role; product-specific; not-life-safety; no-network-by-default; raw-quarantine-only; descriptor-gated; rights-aware; sensitivity-aware; provenance-preserving; finite-outcomes; fixture-first; correction-aware; rollback-aware; no-secrets; no-publication"
current_path: connectors/noaa/README.md
truth_posture: CONFIRMED repository path and prior v0.1 README, connectors responsibility root, Directory Rules NOAA family spine, merged NOAA source-root v0.2 README, merged NOAA package-boundary v0.1 README, merged NOAA test-boundary v0.2 README, merged nested USCRN v0.2 boundary, flat NOAA product sibling READMEs, NOAA source-family and product catalog pages, NOAA package project name and 0.0.0 version, empty central package initializer, bounded absence of selected client and product-adapter paths, two USCRN registry placeholders, proposed empty source-authority register, and connector-gate TODO-only workflow / PROPOSED family-level product-adapter registry, explicit connector request profile, transport interface, product parser interface, admission-candidate contract, connector outcome and reason-code vocabulary, family fixture registry, migration map, receipt handoff, correction invalidation, and operational health evidence / CONFLICTED nested versus flat NOAA product-lane placements, duplicate USCRN lanes, NOAA source catalog path conventions, source registry topology, source-schema home references, connector-local outcomes versus canonical PolicyDecision outcomes, and documentation-rich family boundaries versus absent executable implementation / UNKNOWN complete connector-family tree inventory, accepted canonical product topology, package installability, dependencies, import consumers, active NOAA SourceDescriptors, approved endpoints, current product formats and fields, executable product adapters, fixtures, tests, CI enforcement, live retrieval, schedules, emitted receipts, deployment, downstream consumers, and runtime health / NEEDS VERIFICATION accepted owners, topology ADR or migration notes, compatibility classifications, source activation, rights and attribution, exact product profiles, endpoint allowlists, network and retry policies, parser contracts, schema bindings, validators, fixture approval, test collection, CI gates, receipt schemas, correction propagation, deprecation, and rollback automation
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 3b2cb50acf90c9ee5f0f082aec5d1e04601a3b9b
  prior_blob: 44ff6a50ed2c19e8e46092b714066c7ea3ab06fc
  source_root_blob: 0422134d3d1ac6547b9536cd6e5de5e0dd93d314
  package_readme_blob: 1303a10954d16844557653e871f4c0592e87e2c1
  tests_readme_blob: a156c9149d69884a9327fa1257e55e22347ee2ec
  nested_uscrn_blob: 0ddd3e27fec1e432c2040d01adc189037213cef0
  flat_uscrn_blob: 3860f8309b77ffa28a0204827204cc6a2d9d1b52
  package_metadata_blob: 851976fa7a808ce8d5ebc93291c3ddde27a9c349
  source_authority_register_blob: 82c23722520922f5ca0dad7f37ed794d1c2edf81
  connector_gate_workflow_blob: fc36ecced55bb0b4002d551cb28addfff0be918a
  bounded_path_checks:
    - connectors/noaa/README.md exists at v0.1 before this revision
    - connectors/noaa/src/README.md exists at v0.2
    - connectors/noaa/src/noaa/README.md exists at v0.1
    - connectors/noaa/src/noaa/__init__.py is empty
    - connectors/noaa/src/noaa/client.py was not found in the bounded package check
    - connectors/noaa/src/noaa/products/uscrn.py was not found in the bounded product check
    - connectors/noaa/tests/README.md exists at v0.2 and documents a README-only test lane
    - connectors/noaa/tests/test_uscrn.py was not found in the bounded product check
    - connectors/noaa/uscrn/README.md and connectors/noaa-uscrn/README.md both exist as README-only boundaries
    - connectors/noaa/pyproject.toml contains only project name and version 0.0.0
    - control_plane/source_authority_register.yaml is PROPOSED and entries is empty
    - .github/workflows/connector-gate.yml contains TODO echo steps
related:
  - ../README.md
  - ./src/README.md
  - ./src/noaa/README.md
  - ./tests/README.md
  - ./uscrn/README.md
  - ./pyproject.toml
  - ../noaa-storm-events/README.md
  - ../noaa-hms-smoke/README.md
  - ../noaa-uscrn/README.md
  - ../hrrr_smoke/README.md
  - ../hms_smoke/README.md
  - ../goes_abi_aod/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0017-source-descriptor-admission-process.md
  - ../../docs/sources/catalog/noaa/README.md
  - ../../docs/sources/catalog/noaa/storm-events.md
  - ../../docs/sources/catalog/noaa/nws-api.md
  - ../../docs/sources/catalog/noaa/hms-fire-smoke.md
  - ../../docs/sources/catalog/noaa/hrrr-smoke.md
  - ../../docs/sources/catalog/noaa/goes-abi-aod.md
  - ../../docs/sources/catalog/noaa/viirs-hotspot.md
  - ../../docs/sources/catalog/noaa/noaa-uscrn.md
  - ../../docs/sources/catalog/noaa/station-climate-products.md
  - ../../control_plane/source_authority_register.yaml
  - ../../data/registry/sources/README.md
  - ../../data/raw/
  - ../../data/quarantine/
  - ../../data/receipts/
  - ../../data/proofs/
  - ../../contracts/
  - ../../schemas/
  - ../../policy/rights/
  - ../../policy/sensitivity/
  - ../../release/
  - ../../.github/workflows/connector-gate.yml
tags: [kfm, connectors, noaa, connector-family, ncei, nws, storm-events, hms, hrrr, goes, viirs, uscrn, station-climate, hazards, atmosphere, climate, soil, hydrology, agriculture, multi-role, source-admission, raw, quarantine, receipts, provenance, no-network, fixture-first, anti-collapse, not-life-safety, migration, rollback]
notes:
  - "This revision changes only connectors/noaa/README.md."
  - "The NOAA family path is CONFIRMED under connectors/, but product-lane topology is not normalized by this README."
  - "The source root, package boundary, test boundary, and nested USCRN boundary are now repository-present; implementation remains unproved and the central package remains a 0.0.0 empty shell."
  - "NOAA is a heterogeneous multi-role family. Product identity, source role, time kinds, cadence, units, quality, geometry, uncertainty, rights, sensitivity, and caveats must remain product-specific."
  - "Source activation is not established: the inspected source-authority register is empty and known USCRN registry records are placeholders."
  - "The connector-gate workflow is TODO-only; a green run cannot prove connector behavior."
  - "KFM is not an emergency alerting system."
  - "Connector activity is limited to explicit source admission and RAW or QUARANTINE handoff. It does not promote, publish, close evidence, issue alerts, or serve public clients."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# NOAA Connector Family Admission Boundary

`connectors/noaa/`

> Source-family boundary for NOAA fetch, parse, integrity, provenance, and admission support. This lane may organize product-specific connector code and handoff candidates for governed **RAW** or **QUARANTINE** intake. It does not establish NOAA truth, activate a source, issue warnings, approve release, or publish public data.

![status](https://img.shields.io/badge/status-draft-yellow)
![version](https://img.shields.io/badge/version-v0.2-informational)
![maturity](https://img.shields.io/badge/maturity-documentation__rich%20%7C%20implementation__placeholder-lightgrey)
![root](https://img.shields.io/badge/root-connectors%2Fnoaa-blue)
![source role](https://img.shields.io/badge/source--role-multi--role-purple)
![network](https://img.shields.io/badge/network-off__by__default-critical)
![lifecycle](https://img.shields.io/badge/lifecycle-RAW%20%7C%20QUARANTINE-orange)
![life safety](https://img.shields.io/badge/life__safety-NOT__ALERT__AUTHORITY-red)

**Quick links:** [Purpose](#purpose) · [Status](#status-and-evidence) · [Authority](#authority-boundary) · [Directory basis](#repository-fit-and-directory-rules-basis) · [Topology](#family-topology-and-placement) · [Child contract](#child-lane-inheritance-contract) · [Products](#product-family-inventory) · [Invariants](#keystone-invariants) · [Inputs](#explicit-connector-input) · [Transport](#transport-and-resource-contract) · [Roles](#product-identity-and-source-role) · [Time](#time-cadence-and-freshness) · [Parsing](#parsing-and-preservation-contract) · [Admission](#source-admission-handoff) · [Outcomes](#connector-outcomes-and-reason-codes) · [Policy](#rights-sensitivity-and-life-safety) · [Security](#security-and-data-minimization) · [Testing](#testing-and-fixtures) · [Operations](#receipts-corrections-and-operational-evidence) · [Migration](#topology-migration-and-compatibility) · [Implementation](#smallest-sound-implementation-sequence) · [Done](#definition-of-done) · [Open](#open-verification-register) · [Rollback](#rollback-correction-deprecation-and-supersession)

> [!IMPORTANT]
> **The family README is an implementation boundary, not source activation or source authority.** A NOAA product may be mentioned, documented, or represented by a connector lane and still remain inactive. Live retrieval requires an accepted source descriptor, rights and sensitivity posture, product-specific configuration, validation, review, and explicit activation evidence.

> [!CAUTION]
> **KFM is not an emergency alerting system.** Watches, warnings, advisories, forecasts, smoke products, storm records, satellite detections, and station observations may enter KFM only as product-specific source material with official-source caveats. This connector family must never issue KFM alerts, emergency instructions, or life-safety determinations.

---

<a id="purpose"></a>

## Purpose

This README defines the shared NOAA connector-family boundary.

It exists to keep NOAA connector work:

- source-specific rather than NOAA-wide and generic;
- product-specific rather than role-collapsed;
- descriptor-gated;
- explicit about source identity and activation state;
- no-network by default;
- fixture-first;
- deterministic for captured bytes and explicit configuration;
- bounded in timeouts, retries, redirects, payload size, decompression, and resource use;
- provenance-preserving;
- rights- and sensitivity-aware without becoming policy authority;
- limited to RAW or QUARANTINE admission candidates;
- separate from evidence closure, release, public API, public UI, map rendering, search, and AI answers;
- correctable, replayable, and rollback-aware.

This family lane may eventually coordinate:

- the importable NOAA Python package;
- product-adapter registration;
- shared request and integrity helpers;
- explicit product profiles;
- fixture and test conventions;
- source-admission candidate construction;
- connector-local finite outcomes;
- family-level migration records;
- operational evidence pointers.

It must not become:

- NOAA source-family or product doctrine;
- the active source registry;
- a general weather or climate SDK;
- an emergency alert relay;
- a scheduler or uncontrolled watcher;
- a domain truth resolver;
- an evidence resolver;
- a policy decision point;
- a schema or contract authority;
- a lifecycle processor beyond source admission;
- a catalog, triplet, release, or publication pipeline;
- a public API, UI, map, search, notification, or AI surface;
- a secret store.

[Back to top](#top)

---

<a id="status-and-evidence"></a>

## Status and evidence

### Current repository state

| Surface | Status | Safe conclusion |
|---|---:|---|
| `connectors/noaa/README.md` | **CONFIRMED v0.1 before this revision** | The family README exists and defines a conservative family boundary, but it predates the merged child-boundary updates. |
| `connectors/noaa/src/README.md` | **CONFIRMED v0.2** | The source-root boundary exists and records an empty package shell. |
| `connectors/noaa/src/noaa/README.md` | **CONFIRMED v0.1** | The Python package boundary exists, but no working public API is established. |
| `connectors/noaa/src/noaa/__init__.py` | **CONFIRMED empty** | A package marker exists; executable behavior and imports remain unproved. |
| `connectors/noaa/src/noaa/client.py` | **NOT FOUND in bounded check** | A central HTTP client is not established at the proposed path. |
| `connectors/noaa/pyproject.toml` | **CONFIRMED placeholder** | Project name is `kfm-connector-noaa`; version is `0.0.0`. |
| `connectors/noaa/tests/README.md` | **CONFIRMED v0.2** | The test boundary exists but remains README-only. |
| Executable NOAA tests and fixtures | **NOT SURFACED / UNKNOWN** | No complete executable test or fixture inventory is established. |
| `connectors/noaa/uscrn/README.md` | **CONFIRMED v0.2** | The nested USCRN boundary exists and is placement-conflicted. |
| `connectors/noaa-uscrn/README.md` | **CONFIRMED v0.2** | A flat README-only sibling also exists; canonical placement remains unresolved. |
| Other flat product connector lanes | **CONFIRMED where READMEs exist** | Product-specific boundary docs exist outside the family tree; their migration status remains product-specific. |
| NOAA source catalog pages | **CONFIRMED draft documentation** | Source and product doctrine exists, but current external details and implementation are not automatically established. |
| Source-authority register | **CONFIRMED proposed and empty** | No active source entry is established by the inspected register. |
| Known USCRN registry records | **CONFIRMED placeholders** | Presence does not establish a mature SourceDescriptor or activation. |
| Connector-gate workflow | **CONFIRMED TODO-only** | A green run cannot prove connector behavior. |
| Live endpoints, schedules, receipts, deployment | **UNKNOWN** | No operational evidence is established by this README. |

### Evidence boundary

This README may confidently state:

- `connectors/noaa/` is a repository-present connector-family lane;
- Directory Rules place NOAA in the connector family spine;
- merged source, package, test, and nested-USCRN boundary READMEs exist;
- the central package remains a `0.0.0` placeholder with an empty initializer;
- NOAA is a heterogeneous multi-role source family;
- connectors are limited to source admission and RAW/QUARANTINE handoff;
- public clients must not read connector outputs directly.

This README must not claim:

- package installability;
- working imports beyond the empty marker;
- a working HTTP client;
- approved NOAA endpoints;
- active source descriptors;
- product parser correctness;
- fixture or test coverage;
- CI enforcement;
- scheduled or deployed connector runs;
- emitted receipts;
- product freshness;
- publication safety;
- public availability;
- life-safety suitability.

Those remain `UNKNOWN`, `PROPOSED`, or `NEEDS VERIFICATION` until code, schemas, contracts, tests, workflows, logs, receipts, or deployed artifacts prove them.

[Back to top](#top)

---

<a id="authority-boundary"></a>

## Authority boundary

### This family lane may own

If implemented and reviewed, `connectors/noaa/` may own:

- NOAA-family connector implementation organization;
- shared package and source-root documentation;
- package-local configuration types;
- bounded transport interfaces;
- request canonicalization helpers;
- response metadata capture;
- product-adapter registration;
- product-specific parser modules;
- product-local parsed-record types;
- admission-candidate builders;
- connector-local finite outcomes and error types;
- content-digest and deterministic replay helpers;
- no-network connector tests and fixture pointers;
- migration notes for NOAA connector topology;
- pointers to emitted process receipts.

### This family lane does not own

| Concern | Owning boundary |
|---|---|
| NOAA source-family and product meaning | `docs/sources/catalog/noaa/` |
| SourceDescriptor records and activation | `data/registry/sources/` plus accepted source-governance artifacts |
| Source authority register | `control_plane/` or the accepted registry authority |
| Semantic contracts | `contracts/` |
| Machine schemas | `schemas/` |
| Rights and sensitivity decisions | `policy/rights/`, `policy/sensitivity/` |
| Domain truth | Domain contracts, schemas, validators, evidence, and review |
| EvidenceBundle closure | `data/proofs/` and governed evidence-resolution workflows |
| WORK, PROCESSED, CATALOG, TRIPLET | Downstream lifecycle roots |
| Receipts as trust artifacts | `data/receipts/` |
| Release decisions | `release/` |
| Published data | `data/published/` |
| Public API and UI behavior | Governed application roots |
| Alerts and life-safety guidance | Official external authorities, never KFM connector code |

A connector may preserve source facts and process evidence. It cannot make a public claim true, complete, timely, safe, or publishable.

[Back to top](#top)

---

<a id="repository-fit-and-directory-rules-basis"></a>

## Repository fit and Directory Rules basis

### Owning responsibility root

`connectors/` is the correct responsibility root because this lane concerns source-specific:

- fetch;
- probe;
- file or object discovery;
- integrity verification;
- parse;
- source-native preservation;
- source-admission handoff.

Directory Rules identify NOAA in the connector family spine and impose the connector lifecycle limit:

```text
external source
  -> connectors/noaa/
  -> data/raw/<domain>/<source_id>/<run_id>/
     OR data/quarantine/<domain>/<source_id>/<run_id>/
  -> downstream governed lifecycle
```

Connectors must not write directly to:

```text
data/work/
data/processed/
data/catalog/
data/triplets/
data/published/
release/
apps/
```

### No parallel authority

This README does not create:

- a second NOAA source catalog;
- a second source registry;
- a connector-local schema authority;
- a connector-local policy authority;
- a connector-local proof store;
- a connector-local release lane;
- a connector-local public API.

### Path status

| Path class | Posture |
|---|---|
| `connectors/noaa/` family lane | **CONFIRMED repository-present and consistent with Directory Rules.** |
| Nested product lanes | **Allowed only when topology is documented and duplicate authority is prevented.** |
| Flat NOAA product lanes | **Repository-present where verified; migration or compatibility status remains unresolved per product.** |
| Duplicate nested/flat lanes | **ADR- or migration-note-class.** Documentation cannot select a winner by assertion. |

[Back to top](#top)

---

<a id="family-topology-and-placement"></a>

## Family topology and placement

### Current documented topology

```text
connectors/
├── noaa/
│   ├── README.md
│   ├── pyproject.toml
│   ├── src/
│   │   ├── README.md
│   │   └── noaa/
│   │       ├── README.md
│   │       └── __init__.py
│   ├── tests/
│   │   └── README.md
│   └── uscrn/
│       └── README.md
├── noaa-storm-events/
│   └── README.md
├── noaa-hms-smoke/
│   └── README.md
├── noaa-uscrn/
│   └── README.md
├── hms_smoke/
│   └── README.md
├── hrrr_smoke/
│   └── README.md
└── goes_abi_aod/
    └── README.md
```

This is a documentation-oriented snapshot, not a complete recursive inventory.

### Placement posture

The repository currently carries multiple NOAA product-lane patterns:

| Pattern | Example | Status |
|---|---|---|
| Family root | `connectors/noaa/` | Confirmed family lane. |
| Nested product boundary | `connectors/noaa/uscrn/` | Confirmed README-only; placement conflicted with a flat sibling. |
| Flat NOAA-prefixed lane | `connectors/noaa-uscrn/`, `connectors/noaa-storm-events/` | Confirmed where present; compatibility or migration status remains unresolved. |
| Flat product-name lane | `connectors/hrrr_smoke/`, `connectors/goes_abi_aod/` | Confirmed where present; source-family placement remains product-specific. |

### Freeze-by-default duplicate rule

Until topology is resolved:

1. Do not create parallel executable implementations for the same product.
2. Do not create duplicate SourceDescriptors with competing authority.
3. Do not create duplicate config, fixture, test, or schedule authorities.
4. Do not add hidden import aliases that make both paths active.
5. Do not silently copy product code between lanes.
6. Keep both README boundaries explicit about their non-authoritative status.
7. Require an ADR or migration note before activation or consolidation.
8. Require rollback and compatibility handling for any move.

[Back to top](#top)

---

<a id="child-lane-inheritance-contract"></a>

## Child-lane inheritance contract

Every NOAA product connector lane inherits these family invariants.

A child lane may tighten controls. It must not weaken:

- descriptor gating;
- no-network default;
- fixture-first development;
- product-specific source-role preservation;
- explicit time-kind preservation;
- units and quality-flag preservation;
- rights and sensitivity checks;
- source-native identity preservation;
- bounded transport;
- finite outcomes;
- secret-safe logging;
- RAW/QUARANTINE-only output;
- no-publication;
- no-alert;
- no-life-safety;
- correction and rollback requirements.

### Required child README fields

Each non-trivial child README should identify:

- exact path;
- maturity;
- owners;
- source family and product identity;
- placement status;
- source-role posture;
- activation posture;
- explicit inputs;
- allowed outputs;
- anti-collapse rules;
- transport limits;
- parser preservation requirements;
- rights and sensitivity dependencies;
- test and fixture expectations;
- correction path;
- rollback or migration target;
- verification backlog.

### Conflict handling

If a child README conflicts with this family README:

1. Prefer the stricter fail-closed rule for operational safety.
2. Record the conflict.
3. Do not silently normalize terminology or outcomes.
4. Resolve through the owning contract, schema, ADR, or steward review.
5. Keep activation blocked when the conflict affects source identity, rights, sensitivity, lifecycle, or publication.

[Back to top](#top)

---

<a id="product-family-inventory"></a>

## Product family inventory

NOAA is a multi-role family. No single NOAA-wide parser, role, cadence, schema, or release posture is safe.

| Product lane | Primary source-role posture | Required preservation | Dominant anti-collapse rule | Placement posture |
|---|---|---|---|---|
| Storm Events | Historical event record / observation-context candidate | Event/episode identity, table type, file vintage, event type, narrative, geometry, magnitude, damage/casualty fields, corrections | Historical record is not a current alert, direct sensor measurement, flood extent, or disaster declaration | Flat sibling README exists; family consolidation remains migration work |
| NWS API | Contextual official-source material; product-specific observation/forecast/alert context | Product type, issue time, valid time, expiry, office/source identity, status, geometry, update/correction | Official warning or forecast context is not a KFM-issued alert or emergency instruction | Product doctrine exists; executable connector placement needs verification |
| HMS Fire and Smoke | Mixed detection/analysis context | Fire detections separate from smoke polygons, issue time, geometry, qualitative density, provenance | Smoke density is not PM2.5 concentration; detection is not confirmed ground fire | Multiple flat naming patterns exist; migration status unresolved |
| HRRR-Smoke | Modeled forecast | Model run, cycle, forecast hour, valid time, grid/version, variable/units, run correction | Forecast field is not observation or current ground truth | Flat product lane exists; family placement needs review |
| GOES ABI AOD | Satellite retrieval | Product/version, scan time, retrieval flags, geometry/grid, AOD units/quality, provenance | AOD is not PM2.5 without governed downstream derivation | Flat product lane exists; family placement needs review |
| VIIRS Hotspot | Satellite thermal detection | Platform/sensor, acquisition time, confidence/quality, geometry, product/version, source identity | Hotspot is not confirmed ground fire, burn perimeter, cause, or damage | Product documentation exists; connector topology needs verification |
| USCRN | Station observation | Station ID, station metadata vintage, timestamp, timezone, cadence, variable, units, QC, missingness, depth, raw/derived class | Station is not area; depth and cadence do not collapse; reference-grade is not regulatory | Nested and flat README-only lanes conflict |
| Station climate products | Observation and aggregate, product-specific | Station/product identity, aggregation period, cadence, normals/anomalies distinction, version, corrections | Station observation, source-issued aggregate, and KFM-derived aggregate are distinct | Product doctrine exists; implementation placement needs verification |

### Product admission rule

A row in this table is not source activation.

A product may enter live connector work only when:

- a source descriptor or accepted equivalent exists;
- activation state is explicit;
- rights and attribution are reviewed;
- sensitivity posture is reviewed;
- exact source surface and product identity are configured;
- transport limits are approved;
- a fixture exists before live access;
- parser preservation tests exist;
- admission and quarantine behavior are tested;
- rollback and correction paths are documented.

[Back to top](#top)

---

<a id="keystone-invariants"></a>

## Keystone invariants

### Connector invariants

1. **Admission is not publication.**
2. **Source availability is not source activation.**
3. **Successful retrieval is not evidence closure.**
4. **Schema validity is not source truth.**
5. **Official-source status does not make KFM an alert authority.**
6. **NOAA is multi-role; product identity controls role.**
7. **Product time kinds must remain distinct.**
8. **Native units, quality flags, missingness, and uncertainty must be preserved.**
9. **Station, detection, retrieval, model field, event record, and aggregate are different support types.**
10. **RAW and QUARANTINE are the connector’s terminal lifecycle targets.**
11. **Public clients never read connector stores directly.**
12. **Corrections and supersessions must remain traceable.**
13. **No secret or credential belongs in source payload logs, fixtures, or receipts.**
14. **Unknown rights, sensitivity, identity, or format fails closed.**
15. **A duplicate product path does not create duplicate authority.**

### Lifecycle invariant

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

This connector family participates at the left edge only.

[Back to top](#top)

---

<a id="explicit-connector-input"></a>

## Explicit connector input

A future family runner or product adapter should receive an explicit request object.

### Required input groups

| Group | Required content | Fail-closed condition |
|---|---|---|
| Source identity | Source descriptor reference, revision, activation state, source family, product ID | Missing or inactive source identity |
| Product profile | Product profile ID/version, parser profile, expected media/format class | Unknown or unsupported profile |
| Source locator | Approved scheme, host, path/object key, redacted query metadata | Unapproved scheme/host or hidden credentials |
| Request policy | Timeout, retries, backoff, redirect limit, rate-limit behavior, max bytes | Missing unbounded resource policy |
| Expected object | Filename/object key, expected size and digest when known, period/run/station scope | Contradictory or ambiguous identity |
| Routing | Owning domain, proposed RAW/QUARANTINE target, run ID | Missing or unauthorized lifecycle target |
| Rights | Rights/attribution assessment reference, permitted-use posture | Unknown or blocked rights |
| Sensitivity | Sensitivity profile reference and required handling | Unknown or prohibited sensitivity |
| Provenance | Retrieval agent/version, config digest, request fingerprint, clock source | Missing reproducibility metadata |
| Correction state | Known supersession/correction markers and prior object reference | Unresolved correction conflict |

### No hidden fetches

Connector library functions must not:

- discover source descriptors implicitly;
- fetch secrets at import time;
- infer activation from path presence;
- choose endpoints from undocumented defaults;
- infer product roles from a NOAA-wide constant;
- write lifecycle data without an explicit caller-supplied target and runner receipt;
- change release or public state.

[Back to top](#top)

---

<a id="transport-and-resource-contract"></a>

## Transport and resource contract

### Default posture

```text
network: disabled unless explicitly enabled
schemes: allowlist only
hosts: allowlist only
redirects: bounded and revalidated
timeouts: mandatory
retries: finite
backoff: bounded
rate limits: respected
payload bytes: bounded
decompressed bytes: bounded
archive members: bounded
filesystem writes: caller-owned and explicit
credentials: external secret references only
logging: redacted and minimized
```

### Transport requirements

A live-capable adapter must:

- reject unsupported URL schemes;
- validate each redirect target;
- prevent private-address and metadata-service access unless explicitly authorized for a separate internal source;
- use finite connect/read/total timeouts;
- use finite retry counts;
- honor source rate limits and retry hints;
- distinguish retryable from terminal failures;
- cap response bytes before buffering;
- cap decompressed bytes;
- reject path traversal in archives;
- reject unexpected content types or format signatures;
- preserve response status and safe headers;
- compute content digests over preserved bytes;
- avoid automatic interpretation of HTML error pages as data;
- avoid unsafe deserialization;
- close resources deterministically;
- support cancellation.

### Import safety

Importing the package must not:

- access the network;
- read environment secrets;
- inspect user home directories;
- mutate caches;
- write files;
- create lifecycle directories;
- emit receipts;
- start threads;
- start schedulers;
- configure global logging;
- perform source discovery.

[Back to top](#top)

---

<a id="product-identity-and-source-role"></a>

## Product identity and source role

### Identity hierarchy

A NOAA connector record should preserve, when applicable:

```text
source family
  -> source organization or service
  -> product family
  -> product version/profile
  -> distribution or endpoint
  -> source object/file/message
  -> product item or record
  -> station/grid/event/detection/model-run identity
```

### Source-role posture

Source role is assigned at product or record level, not at NOAA family level.

| Candidate role | Appropriate example | Required guard |
|---|---|---|
| `observation` | Native station reading or direct source record | Preserve station/record scope, units, QC, time, and support type |
| `modeled` | Forecast or model field | Preserve run, cycle, forecast hour, grid, model/version, valid time |
| `contextual` | Official warning/advisory context used analytically | Preserve official source and timing; deny KFM-issued alert behavior |
| `aggregate` | Source-issued climate normal or explicit aggregate | Preserve period, method/source identity, and aggregate class |
| `candidate` | Unresolved or quarantined role | Block later lifecycle promotion until reviewed |
| `retrieval` | Satellite-derived retrieval where vocabulary permits | Preserve retrieval algorithm/product/version and quality metadata |

Exact accepted role vocabulary belongs to the source-role contract or registry, not this README.

### Anti-collapse checks

The family must reject:

- `NOAA -> one source role`;
- `station observation -> area truth`;
- `model field -> observation`;
- `warning context -> KFM alert`;
- `historical event record -> current measurement`;
- `smoke polygon density -> concentration`;
- `AOD -> PM2.5`;
- `thermal detection -> confirmed ground fire`;
- `source-issued aggregate -> raw observation`;
- `KFM-derived aggregate -> source observation`;
- `one depth -> another depth`;
- `one cadence -> another cadence`.

[Back to top](#top)

---

<a id="time-cadence-and-freshness"></a>

## Time, cadence, and freshness

NOAA products expose different time semantics. The connector must keep them separate.

### Time kinds

| Time kind | Meaning |
|---|---|
| Observation time | When a sensor or source record applies |
| Issue time | When an advisory, forecast, analysis, or product was issued |
| Valid start/end | The product’s validity interval |
| Model run/cycle time | The model initialization or run identity |
| Forecast lead/hour | Offset from run time to valid time |
| Acquisition/scan time | Satellite or remote-sensing capture time |
| Event begin/end | Historical event interval |
| File or product vintage | Source publication/revision period |
| Retrieval time | When KFM fetched the source object |
| Correction time | When a correction or supersession was issued |
| Processing time | When connector parsing or handoff occurred |

### Cadence posture

Cadence is source-significant.

The connector must not silently convert:

- sub-hourly to hourly;
- hourly to daily;
- daily to monthly;
- model cycles to observations;
- issue-time streams to event-time streams;
- station records to climate normals;
- native products to rolling aggregates.

Any aggregation or resampling belongs downstream and requires a separate transform or aggregation receipt.

### Freshness

Freshness must be product-specific.

A family-wide “fresh” threshold is unsafe because:

- historical Storm Events files may be valid long after publication;
- model forecasts expire quickly;
- station observations have cadence-specific expectations;
- product revisions may supersede older files;
- static station metadata changes on a different schedule.

Freshness policy must be explicit in the product profile and carried into the admission candidate.

[Back to top](#top)

---

<a id="parsing-and-preservation-contract"></a>

## Parsing and preservation contract

### Parser principles

A parser should be:

- deterministic;
- side-effect-minimal;
- callable on supplied bytes or streams;
- independent of live network access;
- explicit about product profile and version;
- strict about required identity;
- conservative about unknown fields;
- capable of preserving source-native values;
- capable of emitting finite issues;
- replayable from captured payloads.

### Common preservation fields

Where present, preserve:

- source descriptor reference and revision;
- source family;
- source organization/service;
- product ID and version;
- object/file/message identity;
- content type and format;
- source URL or redacted locator;
- response status and safe headers;
- source-provided checksum;
- computed checksum;
- observed size;
- compression/archive metadata;
- record identity;
- station/grid/event/detection/model-run identity;
- geometry and CRS/projection metadata;
- observation, issue, valid, run, acquisition, retrieval, correction, and processing times;
- cadence;
- variable;
- value;
- units;
- quality flags;
- missing-value codes;
- uncertainty/confidence;
- depth or vertical coordinate;
- raw, calculated, retrieved, modeled, aggregate, or corrected product class;
- rights and attribution references;
- sensitivity reference;
- parser version and config digest;
- quarantine reasons;
- correction and supersession pointers.

### Unknown fields

Unknown source fields should be:

- preserved in a bounded extension area when allowed;
- recorded in a drift report;
- excluded only through a reviewed transform;
- never silently repurposed;
- never silently converted into canonical domain fields.

### Invalid or ambiguous data

Malformed, incomplete, contradictory, or unsupported payloads must produce:

- a finite connector issue;
- a quarantine candidate when preservation is allowed;
- no later-lifecycle write;
- no public claim;
- no silent partial success unless the accepted product contract defines record-level partial admission.

[Back to top](#top)

---

<a id="source-admission-handoff"></a>

## Source-admission handoff

### Allowed terminal targets

A connector runner may hand off to:

```text
data/raw/<owning-domain>/<source-id>/<run-id>/
data/quarantine/<owning-domain>/<source-id>/<run-id>/
```

Exact layout remains subject to accepted lifecycle contracts.

### Admission candidate

A proposed family-level candidate shape may include:

```yaml
connector_candidate_version: PROPOSED
candidate_id: <deterministic-or-run-scoped-id>
source_descriptor_ref: <required>
source_descriptor_revision: <required>
source_family: noaa
product_id: <required>
product_profile_version: <required>
source_role_candidate: <required>
owning_domain: <required>
lifecycle_target: RAW | QUARANTINE
source_object:
  locator_redacted: <safe>
  object_id: <required>
  media_type: <observed>
  size_bytes: <observed>
  source_digest: <optional>
  computed_digest: <required>
times:
  observation_at: <optional>
  issue_at: <optional>
  valid_from: <optional>
  valid_to: <optional>
  model_run_at: <optional>
  acquisition_at: <optional>
  retrieved_at: <required>
  processed_at: <required>
rights_ref: <required-or-unresolved>
sensitivity_ref: <required-or-unresolved>
parser:
  name: <required>
  version: <required>
  config_digest: <required>
issues: []
quarantine_reasons: []
correction_refs: []
```

This example is **PROPOSED** and not a schema authority.

### Persistent writes

Parser and adapter functions should return candidates, not perform hidden writes.

A runner that persists a candidate must:

- receive an explicit target;
- verify target authority;
- write atomically;
- preserve bytes or an immutable reference;
- emit or reference a process receipt;
- record no-op, denial, error, or quarantine outcomes;
- avoid overwriting prior source objects;
- preserve correction lineage;
- expose rollback targets.

[Back to top](#top)

---

<a id="connector-outcomes-and-reason-codes"></a>

## Connector outcomes and reason codes

Connector outcomes are not canonical `PolicyDecision` outcomes.

### Proposed connector outcomes

| Outcome | Meaning |
|---|---|
| `ADMIT_RAW` | Source object passed connector-level admission preconditions and may be preserved in RAW |
| `QUARANTINE` | Source object is preservable but unresolved, unsafe, malformed, or blocked for normal admission |
| `NO_OP` | No new object or change was found; record an auditable no-op where required |
| `RETRYABLE_ERROR` | Temporary source or transport failure; finite retry policy applies |
| `TERMINAL_ERROR` | Non-retryable connector failure |
| `DISABLED` | Source or product activation is disabled |
| `UNSUPPORTED` | Product profile or format is not supported |

These names are **PROPOSED** until an accepted connector contract exists.

### Proposed reason-code families

```text
NOAA_SOURCE_INACTIVE
NOAA_DESCRIPTOR_MISSING
NOAA_DESCRIPTOR_REVISION_UNSUPPORTED
NOAA_PRODUCT_PROFILE_UNKNOWN
NOAA_PRODUCT_IDENTITY_AMBIGUOUS
NOAA_ENDPOINT_NOT_ALLOWED
NOAA_REDIRECT_NOT_ALLOWED
NOAA_TIMEOUT
NOAA_RATE_LIMITED
NOAA_RETRY_EXHAUSTED
NOAA_PAYLOAD_TOO_LARGE
NOAA_DECOMPRESSED_PAYLOAD_TOO_LARGE
NOAA_ARCHIVE_MEMBER_UNSAFE
NOAA_CONTENT_TYPE_MISMATCH
NOAA_CHECKSUM_MISMATCH
NOAA_FORMAT_UNSUPPORTED
NOAA_SCHEMA_DRIFT
NOAA_REQUIRED_IDENTITY_MISSING
NOAA_TIME_SEMANTICS_AMBIGUOUS
NOAA_UNIT_UNKNOWN
NOAA_QUALITY_FLAG_UNKNOWN
NOAA_DEPTH_MISSING
NOAA_CADENCE_MISSING
NOAA_SOURCE_ROLE_COLLAPSE
NOAA_STATION_AS_AREA
NOAA_MODEL_AS_OBSERVATION
NOAA_ALERT_REBROADCAST
NOAA_RIGHTS_UNRESOLVED
NOAA_SENSITIVITY_UNRESOLVED
NOAA_SECRET_EXPOSURE_BLOCKED
NOAA_CORRECTION_CONFLICT
NOAA_DUPLICATE_LANE_CONFLICT
```

Reason codes should be stable, documented, and testable. They must not leak credentials, private URLs, or oversized source content.

### Policy normalization

A later policy gate may translate connector state into a canonical `PolicyDecision`, but that translation:

- belongs outside this connector family;
- must be explicit;
- must preserve reasons and obligations;
- must not convert `QUARANTINE` into `ANSWER`;
- must not treat `ADMIT_RAW` as publication permission.

[Back to top](#top)

---

<a id="rights-sensitivity-and-life-safety"></a>

## Rights, sensitivity, and life safety

### Independent gates

Connector admission does not replace:

- source rights review;
- attribution requirements;
- sensitivity classification;
- public-safety review;
- infrastructure review;
- privacy review;
- evidence closure;
- release review.

### Fail-closed conditions

Route to QUARANTINE or block live access when:

- rights are unknown;
- attribution requirements are unresolved;
- terms changed without review;
- source redistribution is prohibited or unclear;
- exact-location sensitivity is unresolved;
- casualty or personal information requires review;
- infrastructure details require restricted handling;
- source credentials appear in content or logs;
- public-safety meaning is ambiguous;
- a product could be mistaken for KFM-issued life-safety guidance.

### NOAA warning and alert context

KFM may preserve official-source context for historical or analytical use when governed.

It must not:

- replace official sources;
- alter warning scope or timing;
- generate action instructions;
- imply operational monitoring;
- represent stale content as current;
- suppress source identity;
- turn a connector status into a user-facing safety conclusion.

[Back to top](#top)

---

<a id="security-and-data-minimization"></a>

## Security and data minimization

### Required controls

- scheme and host allowlists;
- SSRF defenses;
- DNS rebinding resistance where relevant;
- redirect revalidation;
- finite timeouts and retries;
- rate-limit handling;
- response and decompression limits;
- archive member count and path limits;
- content-type and magic-byte checks;
- safe temporary files;
- no unsafe deserialization;
- no dynamic code execution;
- no shell interpolation of source values;
- secret redaction;
- log injection prevention;
- bounded exception messages;
- dependency pinning and provenance review;
- deterministic parser versions;
- immutable or append-only source capture where allowed;
- cancellation and cleanup.

### Data minimization

Logs and receipts should carry:

- safe source/product IDs;
- request fingerprint;
- redacted locator;
- timestamps;
- response status;
- size and digest;
- parser/config version;
- outcome and reason codes;
- lifecycle target;
- correction references.

They should not carry:

- credentials;
- API keys;
- cookies;
- authorization headers;
- private query strings;
- full sensitive payloads;
- unnecessary personal information;
- unbounded narratives;
- raw binary content.

### Dependency posture

The package should avoid dependencies until justified by more than one product adapter.

A new dependency requires:

- purpose;
- version policy;
- license review;
- vulnerability posture;
- transitive-dependency review;
- deterministic behavior expectations;
- rollback plan.

[Back to top](#top)

---

<a id="testing-and-fixtures"></a>

## Testing and fixtures

The test README owns the detailed test contract. This family README defines minimum family-wide expectations.

### Default test posture

```text
network: blocked
credentials: absent
live source access: skipped
fixtures: synthetic, minimized, redacted, or explicitly approved
filesystem writes: temporary and isolated
clock: controlled where time affects behavior
randomness: deterministic
logs: captured and scanned for secrets
lifecycle writes: mocked or temporary
public outputs: forbidden
```

### Minimum test classes

| Test class | Required proof |
|---|---|
| Import safety | No network, secret, cache, thread, scheduler, or filesystem side effect on import |
| Package metadata | Expected namespace and package discovery are explicit once implemented |
| Source activation | Missing or inactive descriptor blocks live access |
| Transport | Allowlist, redirect, timeout, retry, rate-limit, payload, decompression, and archive controls |
| Integrity | Digest, size, content-type, and object identity behavior |
| Product dispatch | Unknown product and profile fail closed |
| Source-role preservation | NOAA-wide role collapse is rejected |
| Time preservation | Product-specific time kinds remain distinct |
| Units and quality | Units, QC, missingness, uncertainty, and depth are preserved |
| Anti-collapse | Product-specific unsafe interpretations are denied |
| Admission | Output is RAW or QUARANTINE candidate only |
| No-publication | No direct processed/catalog/triplet/published/release/API/UI write |
| Security | SSRF, secret leakage, path traversal, unsafe archive, and log injection tests |
| Replay | Same bytes and config produce equivalent parsed candidates |
| Correction | Supersession and correction lineage remain explicit |
| Migration | Duplicate product lanes cannot both become active |

### Product-negative matrix

At minimum, test:

- Storm Events record as current alert → reject;
- Storm Events record as direct sensor measurement → reject;
- NWS context as KFM-issued alert → reject;
- HMS qualitative density as concentration → reject;
- AOD as PM2.5 → reject;
- VIIRS/HMS detection as confirmed ground fire → reject;
- HRRR modeled field as observation → reject;
- USCRN station as county/region value → reject;
- USCRN depth substitution → reject;
- cadence collapse without aggregation receipt → reject;
- source-issued aggregate as raw observation → reject;
- duplicate nested/flat adapter activation → reject.

### CI evidence

CI enforcement is not established until:

- the workflow executes real tests rather than `echo TODO`;
- the relevant test path is collected;
- failures block the PR where required;
- test artifacts or summaries are retained;
- no-network controls are active;
- product-negative cases run;
- the workflow revision and runner environment are recorded.

[Back to top](#top)

---

<a id="receipts-corrections-and-operational-evidence"></a>

## Receipts, corrections, and operational evidence

### Process receipts

A connector runner should emit or reference evidence for:

- source activation decision;
- request configuration digest;
- retrieval attempt;
- redirect chain where safe;
- response status;
- object identity;
- byte count;
- content digest;
- parser and config version;
- outcome and reason codes;
- RAW/QUARANTINE target;
- no-op determination;
- retry exhaustion;
- correction or supersession;
- rollback target.

A connector receipt is process evidence. It is not an EvidenceBundle and does not prove the source claim.

### Corrections

When a NOAA source object is corrected or superseded:

1. Preserve prior object identity and digest.
2. Capture new object identity and digest.
3. Record source correction/supersession metadata.
4. Avoid mutating prior RAW bytes.
5. Create a new admission candidate.
6. Notify downstream dependency tracking where implemented.
7. Do not silently replace processed or published artifacts.
8. Require downstream correction and release workflows to decide public effects.

### Operational evidence

Do not claim the connector is operational without evidence such as:

- accepted source activation record;
- implemented package and product adapter;
- passing no-network tests;
- approved live smoke test;
- schedule or invocation configuration;
- recent run receipt;
- observed source object digest;
- runtime logs;
- health signal;
- correction and rollback path.

[Back to top](#top)

---

<a id="topology-migration-and-compatibility"></a>

## Topology migration and compatibility

### Migration decision requirements

Any consolidation of flat and nested NOAA product lanes requires:

- accepted ADR or migration note;
- inventory of both paths;
- canonical target;
- compatibility classification for the non-canonical path;
- import and configuration migration plan;
- SourceDescriptor reference updates;
- fixture and test migration;
- schedule and workflow migration;
- documentation updates;
- redirects or tombstones where appropriate;
- rollback target;
- review owner;
- completion evidence.

### Compatibility classes

A non-canonical product lane may be classified as:

- `transitional`;
- `deprecated`;
- `legacy`;
- `mirror`;
- `redirect-only`.

The classification must be explicit. Until then, duplicate product lanes remain frozen against parallel implementation.

### Migration safety

Do not:

- delete the old lane before consumers are inventoried;
- move code without updating descriptors and tests;
- keep two active schedules;
- maintain two canonical config files;
- duplicate fixtures as independent truth;
- preserve stale imports indefinitely without a deprecation policy;
- use README wording as a substitute for migration evidence.

[Back to top](#top)

---

<a id="smallest-sound-implementation-sequence"></a>

## Smallest sound implementation sequence

### Stage 0 — settle governance prerequisites

1. Confirm owners.
2. Confirm Directory Rules and connector-family topology.
3. Resolve or formally freeze duplicate product lanes.
4. Accept a source descriptor and activation process.
5. Confirm source-role vocabulary.
6. Confirm connector outcome and reason-code contract.
7. Confirm RAW/QUARANTINE candidate contract.
8. Confirm receipt schema and location.
9. Confirm rights and sensitivity review flow.

**Stop if:** placement, source identity, rights, sensitivity, or lifecycle target is unresolved.

### Stage 1 — harden package metadata

1. Add build backend.
2. Declare Python requirement.
3. Declare package discovery.
4. Declare dependencies.
5. Confirm namespace collision risk.
6. Add package metadata tests.
7. Keep `__init__.py` side-effect-free.

**Stop if:** package cannot install in an isolated environment or import safely.

### Stage 2 — implement pure contracts first

1. Configuration types.
2. Product profile type.
3. Transport response metadata type.
4. Parsed-record type.
5. Admission-candidate type.
6. Connector outcome and issue types.
7. Deterministic digest helpers.
8. No network access.

**Stop if:** types duplicate schema or contract authority without an accepted adapter strategy.

### Stage 3 — implement one fixture-only product slice

Choose one product with:

- accepted descriptor;
- stable fixture;
- clear identity;
- clear source role;
- clear rights;
- low sensitivity;
- manageable parser scope.

Implement:

- parser;
- preservation tests;
- negative tests;
- admission candidate;
- quarantine behavior;
- replay.

**Stop if:** product fields, units, time semantics, or rights are unresolved.

### Stage 4 — implement bounded transport

Add:

- allowlists;
- timeouts;
- retries;
- rate-limit handling;
- redirect validation;
- byte limits;
- decompression limits;
- content checks;
- digest capture;
- safe errors.

Keep live access disabled by default.

### Stage 5 — implement runner and receipt handoff

Add a runner that:

- requires explicit activation;
- calls the transport;
- calls the product adapter;
- chooses RAW or QUARANTINE;
- persists atomically;
- emits a process receipt;
- records no-op and errors;
- preserves correction lineage.

### Stage 6 — add real CI

Replace TODO-only jobs with:

- package install;
- import safety;
- no-network enforcement;
- fixture tests;
- product-negative tests;
- security tests;
- candidate-contract validation;
- migration guard tests.

### Stage 7 — controlled live smoke test

Only after approval:

- one source;
- one product;
- bounded object;
- rate-limited;
- no publication;
- steward-observed;
- receipt-emitting;
- rollback-ready.

[Back to top](#top)

---

<a id="definition-of-done"></a>

## Definition of done

The NOAA connector family is not implementation-ready until all applicable items are complete.

### Governance and placement

- [ ] Owners are accepted.
- [ ] NOAA family path is confirmed.
- [ ] Product-lane topology is accepted or explicitly frozen.
- [ ] Duplicate lanes have compatibility classifications.
- [ ] Migration and rollback paths are documented.
- [ ] Source-role vocabulary is accepted.
- [ ] Connector outcome and reason-code vocabulary is accepted.

### Source admission

- [ ] At least one mature SourceDescriptor exists.
- [ ] Activation decision is recorded.
- [ ] Rights and attribution are reviewed.
- [ ] Sensitivity posture is reviewed.
- [ ] Exact source surface and product profile are approved.
- [ ] Lifecycle routing is explicit.
- [ ] Receipt contract is accepted.

### Package and implementation

- [ ] Package metadata is complete.
- [ ] Package installs in isolation.
- [ ] Import is side-effect-free.
- [ ] Dependencies are reviewed.
- [ ] Product adapter registry is explicit.
- [ ] Product parsers preserve native identity and semantics.
- [ ] Transport limits are enforced.
- [ ] Errors are finite and safe.
- [ ] RAW/QUARANTINE candidate contract is validated.
- [ ] No later-lifecycle writes occur.

### Tests and CI

- [ ] No-network tests exist.
- [ ] Import-safety tests exist.
- [ ] Source activation tests exist.
- [ ] Transport-security tests exist.
- [ ] Product anti-collapse tests exist.
- [ ] Time, units, quality, uncertainty, and depth tests exist.
- [ ] Correction and replay tests exist.
- [ ] Duplicate-lane activation tests exist.
- [ ] CI executes real tests.
- [ ] CI failure blocks merge where required.
- [ ] Test evidence is retained.

### Operations

- [ ] Runner emits receipts.
- [ ] No-op behavior is auditable.
- [ ] Retry behavior is bounded.
- [ ] Health evidence is defined.
- [ ] Correction propagation is defined.
- [ ] Rollback is tested.
- [ ] Public clients remain behind governed APIs.
- [ ] KFM alert and life-safety behavior remains denied.

[Back to top](#top)

---

<a id="open-verification-register"></a>

## Open verification register

| ID | Verification item | Status | Required evidence |
|---|---|---:|---|
| NOAA-OPEN-01 | Confirm accepted owners | NEEDS VERIFICATION | CODEOWNERS or steward decision |
| NOAA-OPEN-02 | Confirm current Directory Rules authority/version | NEEDS VERIFICATION | Accepted doctrine record |
| NOAA-OPEN-03 | Resolve nested versus flat product topology | OPEN | ADR or migration note |
| NOAA-OPEN-04 | Classify each flat NOAA product lane | OPEN | Compatibility register |
| NOAA-OPEN-05 | Confirm complete NOAA connector tree | NEEDS VERIFICATION | Recursive repository inventory |
| NOAA-OPEN-06 | Confirm package build backend | UNKNOWN | `pyproject.toml` |
| NOAA-OPEN-07 | Confirm Python requirement | UNKNOWN | Package metadata |
| NOAA-OPEN-08 | Confirm dependencies | UNKNOWN | Package metadata and lockfile |
| NOAA-OPEN-09 | Confirm package discovery and namespace | UNKNOWN | Build/install test |
| NOAA-OPEN-10 | Confirm public import surface | UNKNOWN | Implemented `__init__.py` and tests |
| NOAA-OPEN-11 | Confirm SourceDescriptor schema home | CONFLICTED | ADR/schema registry |
| NOAA-OPEN-12 | Confirm source activation process acceptance | NEEDS VERIFICATION | Accepted ADR and workflow |
| NOAA-OPEN-13 | Confirm active NOAA source descriptors | UNKNOWN | Registry records and activation decisions |
| NOAA-OPEN-14 | Confirm source-authority register population | UNKNOWN | Reviewed register entries |
| NOAA-OPEN-15 | Confirm product profile contract | PROPOSED | Contract/schema |
| NOAA-OPEN-16 | Confirm connector request contract | PROPOSED | Contract/schema |
| NOAA-OPEN-17 | Confirm admission-candidate contract | PROPOSED | Contract/schema |
| NOAA-OPEN-18 | Confirm connector outcome vocabulary | PROPOSED | Contract/ADR |
| NOAA-OPEN-19 | Confirm reason-code registry | PROPOSED | Registry and tests |
| NOAA-OPEN-20 | Confirm receipt schema and location | UNKNOWN | Contract/schema and example |
| NOAA-OPEN-21 | Confirm endpoint allowlist authority | UNKNOWN | Approved configuration |
| NOAA-OPEN-22 | Confirm network opt-in mechanism | UNKNOWN | Runtime config and tests |
| NOAA-OPEN-23 | Confirm timeout and retry policy | UNKNOWN | Product profiles and tests |
| NOAA-OPEN-24 | Confirm rate-limit behavior | UNKNOWN | Source profile and tests |
| NOAA-OPEN-25 | Confirm payload and decompression limits | UNKNOWN | Security config and tests |
| NOAA-OPEN-26 | Confirm parser versioning strategy | UNKNOWN | Package contract |
| NOAA-OPEN-27 | Confirm product adapter registry | PROPOSED | Implemented registry |
| NOAA-OPEN-28 | Confirm source-role vocabulary | CONFLICTED / NEEDS VERIFICATION | Accepted contract |
| NOAA-OPEN-29 | Confirm time-kind contract | NEEDS VERIFICATION | Common temporal contract |
| NOAA-OPEN-30 | Confirm units and quality representation | NEEDS VERIFICATION | Product/domain contracts |
| NOAA-OPEN-31 | Confirm geometry/CRS preservation | NEEDS VERIFICATION | Product adapters and tests |
| NOAA-OPEN-32 | Confirm correction and supersession contract | UNKNOWN | Contract and receipts |
| NOAA-OPEN-33 | Confirm fixture authority | UNKNOWN | Fixture registry and review |
| NOAA-OPEN-34 | Confirm no-network enforcement | UNKNOWN | Test plugin/config and CI |
| NOAA-OPEN-35 | Confirm product-specific test collection | UNKNOWN | Test files and logs |
| NOAA-OPEN-36 | Replace TODO connector-gate workflow | OPEN | Executable workflow |
| NOAA-OPEN-37 | Confirm CI branch-protection role | UNKNOWN | Repository settings |
| NOAA-OPEN-38 | Confirm schedule/orchestration owner | UNKNOWN | Worker or pipeline config |
| NOAA-OPEN-39 | Confirm atomic persistence behavior | UNKNOWN | Runner code and tests |
| NOAA-OPEN-40 | Confirm receipt emission | UNKNOWN | Run artifacts |
| NOAA-OPEN-41 | Confirm operational health evidence | UNKNOWN | Logs, metrics, dashboards |
| NOAA-OPEN-42 | Confirm rights and attribution per product | NEEDS VERIFICATION | Rights assessments |
| NOAA-OPEN-43 | Confirm sensitivity per product | NEEDS VERIFICATION | Sensitivity assessments |
| NOAA-OPEN-44 | Confirm public-safety review | NEEDS VERIFICATION | Policy review |
| NOAA-OPEN-45 | Confirm correction propagation downstream | UNKNOWN | Dependency tracking and runbook |
| NOAA-OPEN-46 | Confirm rollback automation | UNKNOWN | Drill or rollback receipt |
| NOAA-OPEN-47 | Confirm governed API never reads RAW directly | NEEDS VERIFICATION | App code and tests |
| NOAA-OPEN-48 | Confirm no product lane issues KFM alerts | NEEDS VERIFICATION | Negative tests and policy |
| NOAA-OPEN-49 | Confirm flat/nested duplicate activation guard | PROPOSED | Static/runtime guard test |
| NOAA-OPEN-50 | Confirm migration completion evidence format | PROPOSED | Migration template or ADR |

[Back to top](#top)

---

<a id="rollback-correction-deprecation-and-supersession"></a>

## Rollback, correction, deprecation, and supersession

### Documentation rollback

To undo this README revision:

- revert the documentation commit; or
- restore prior blob `44ff6a50ed2c19e8e46092b714066c7ea3ab06fc`.

Documentation rollback does not revert source data, connector runs, registry state, or releases.

### Implementation rollback

A connector implementation rollback should identify:

- affected product adapter;
- package version;
- config revision;
- source descriptor revision;
- run IDs;
- emitted receipts;
- RAW/QUARANTINE objects;
- downstream dependencies;
- replacement or prior package version;
- schedule state;
- correction notices;
- reviewer and timestamp.

### Deprecation

A product lane may be deprecated only after:

- canonical target is accepted;
- consumers are inventoried;
- descriptors and configs are migrated;
- fixtures and tests are migrated;
- schedules are migrated;
- redirects or compatibility aliases are documented;
- rollback remains available;
- the old lane is frozen against new implementation.

### Supersession

Supersession must be explicit for:

- source objects;
- product profiles;
- parser versions;
- SourceDescriptors;
- config profiles;
- fixture versions;
- connector package versions;
- product lanes;
- documentation.

Never silently overwrite prior trust-bearing artifacts.

[Back to top](#top)

---

## Review burden

Changes to this family boundary require review proportional to impact.

| Change | Minimum review |
|---|---|
| Documentation wording only | Connector or docs steward |
| Product inventory or source-role posture | Connector + source + domain steward |
| New live endpoint or product profile | Source + connector + rights + sensitivity + security |
| New dependency | Connector + security + packaging |
| New parser behavior | Connector + product/domain + validation |
| Source activation | Source governance + rights + sensitivity |
| Product-lane migration | Directory/architecture + connector + migration owner |
| Receipt or candidate contract | Contract/schema + connector + evidence |
| Workflow/CI enforcement | Connector + validation + CI |
| Public-safety-related product | Source + hazards/atmosphere + policy + release |
| Release/public behavior | Outside connector authority; release and governed app review |

Separation of duties should increase when source activation, public-safety context, rights, sensitivity, or publication consequences are material.

---

## Maintainer note

Keep `connectors/noaa/` conservative.

The family becomes safer when:

- products remain distinct;
- uncertainty is visible;
- unknown inputs quarantine;
- live access is explicit;
- transport is bounded;
- fixtures precede network access;
- time, units, quality, geometry, uncertainty, and depth survive parsing;
- source activation is separate from path presence;
- receipts prove process rather than truth;
- corrections preserve lineage;
- duplicate lanes remain frozen until governed migration;
- public clients remain behind the governed trust membrane.

It becomes unsafe when a convenient NOAA-wide abstraction erases product meaning, when a connector writes later lifecycle states, when an official-source message is rebroadcast as KFM guidance, or when documentation is mistaken for implementation proof.

<p align="right"><a href="#top">Back to top</a></p>
