<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-nrcs-scan-readme
title: connectors/nrcs-scan/ — NRCS SCAN Sibling Compatibility and Source-Admission Boundary
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Source steward · Connector steward · NRCS steward · Soil steward · Hydrology steward · Agriculture steward · Atmosphere/Climate steward · Tribal/sovereignty reviewer · Rights reviewer · Sensitivity reviewer · Security steward · Validation steward · Migration steward · CI steward · Docs steward
created: 2026-06-19
updated: 2026-07-15
policy_label: "public-doctrine; connector-boundary; compatibility-lane; nrcs; scan; awdb; station-observation; depth-aware; cadence-aware; freshness-aware; tribal-review; placement-conflicted; source-inactive; no-network-by-default; raw-quarantine-only; descriptor-gated; rights-aware; sensitivity-aware; provenance-preserving; correction-aware; fixture-first; not-life-safety; no-publication; rollback-aware; no-secrets"
current_path: connectors/nrcs-scan/README.md
truth_posture: CONFIRMED repository path and prior v0.1 README, canonical NRCS family README, NRCS source-root and package-boundary READMEs, nested connectors/nrcs/scan README, NRCS connector test README, kfm-connector-nrcs 0.0.0 project metadata, empty central package initializer, bounded absence of sibling implementation files and central SCAN product/test modules, NRCS source-family and SCAN product-page doctrine, minimal PROPOSED soil registry placeholder, proposed empty source-authority register, draft downstream scan_awdb_ingest pipeline README, absent tested pipeline-spec path, and TODO-only connector-gate workflow / PROPOSED sibling compatibility contract, freeze-by-default topology posture, explicit request and transport profiles, product parser and admission-candidate interfaces, connector-local finite outcomes and reason codes, fixture taxonomy, product-specific tests, migration plan, receipt handoff, correction, supersession, and rollback / CONFLICTED sibling connectors/nrcs-scan versus nested connectors/nrcs/scan placement, source-role and authority-use vocabulary layering, source registry and descriptor home references, SCAN versus Tribal SCAN release posture, and documentation-rich boundaries versus absent executable implementation / UNKNOWN accepted canonical path, active SourceDescriptor, approved endpoints, current source formats, station inventory, variables, units, depths, cadences, timezone and quality vocabularies, rights, package installability, executable parser behavior, fixtures, tests, CI enforcement, live retrieval, schedules, receipts, deployment, downstream consumers, and runtime health / NEEDS VERIFICATION accepted owners, placement ADR or migration note, compatibility classification, source identity and activation, rights and attribution, Tribal/sovereignty review rules, product profile, endpoint allowlist, network and retry policy, parser contracts, validators, fixture approval, test collection, CI gates, lifecycle routing, correction and supersession, deprecation, and rollback automation
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: ac419b0942eb8c229b666aed147cd71dc7e9c42b
  prior_blob: 7f4893f4dc5fb68e6e232b91cc5eb64e6b639e62
  nrcs_family_blob: 888236f218fc0892c54c947c0c2651b34ca5137b
  nrcs_source_root_blob: 3b26759548ddaf52eb5b6de0e25dfa354e1d62ec
  nrcs_package_readme_blob: 3e022257cc553e8661b988e9e01c61cccc1fddc8
  nested_scan_blob: 3e5b8e6bc980b8d3e1c1078a4dac4f121c1fa2d3
  nrcs_tests_blob: 7c65ba6ef85a8369e17c40d5e3fbc388b04a306b
  package_metadata_blob: c6bb1565db7df490bee52a597d04d694e2b9f8a4
  product_page_blob: e9460e920b2f58f154f6c8f1ac0ba38b17cafa15
  source_catalog_blob: c6985eb052191092daaeae6303e84538b423ce7c
  soil_registry_placeholder_blob: 8e9a441cd3adeac6c2a73b5f2f6e2a874ed13d8d
  source_authority_register_blob: 82c23722520922f5ca0dad7f37ed794d1c2edf81
  downstream_pipeline_readme_blob: 1915d19e0c283453a47227740cdfdf13544dbb5a
  connector_gate_workflow_blob: fc36ecced55bb0b4002d551cb28addfff0be918a
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  bounded_path_checks:
    - connectors/nrcs-scan/README.md exists at v0.1 before this revision
    - connectors/nrcs-scan/__init__.py was not found
    - connectors/nrcs-scan/client.py was not found
    - connectors/nrcs-scan/parser.py was not found
    - connectors/nrcs/scan/README.md exists at v0.1
    - connectors/nrcs/src/nrcs/__init__.py is empty
    - connectors/nrcs/src/nrcs/products/scan.py was not found
    - connectors/nrcs/tests/test_scan.py was not found
    - connectors/nrcs/tests/test_scan_parser.py was not found
    - connectors/nrcs/pyproject.toml contains only project name and version 0.0.0
    - data/registry/sources/soil/nrcs-scan.yaml is a minimal PROPOSED placeholder
    - data/registry/sources/soil/nrcs_scan.yaml was not found
    - data/registry/sources/nrcs/scan.yaml was not found
    - data/registry/source_descriptors/nrcs.scan.yaml was not found
    - control_plane/source_authority_register.yaml is PROPOSED and entries is empty
    - pipeline_specs/soil/scan_awdb_ingest.yaml was not found
    - .github/workflows/connector-gate.yml contains TODO echo steps
related:
  - ../README.md
  - ../nrcs/README.md
  - ../nrcs/src/README.md
  - ../nrcs/src/nrcs/README.md
  - ../nrcs/scan/README.md
  - ../nrcs/tests/README.md
  - ../nrcs/pyproject.toml
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0017-source-descriptor-admission-process.md
  - ../../docs/sources/catalog/nrcs.md
  - ../../docs/sources/catalog/nrcs/README.md
  - ../../docs/sources/catalog/nrcs/scan-soil-climate.md
  - ../../docs/domains/soil/README.md
  - ../../docs/domains/hydrology/README.md
  - ../../docs/domains/agriculture/README.md
  - ../../docs/domains/atmosphere/README.md
  - ../../control_plane/source_authority_register.yaml
  - ../../data/registry/sources/soil/nrcs-scan.yaml
  - ../../pipelines/domains/soil/scan_awdb_ingest/README.md
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
tags: [kfm, connectors, nrcs, scan, tribal-scan, awdb, nwcc, station-observation, soil-moisture, soil-temperature, depth-aware, cadence-aware, heartbeat-freshness, source-admission, raw, quarantine, provenance, no-network, fixture-first, anti-collapse, tribal-review, migration, rollback]
notes:
  - "This revision changes only connectors/nrcs-scan/README.md."
  - "Both the flat sibling and nested SCAN paths are repository-present as README boundaries; this file does not ratify, migrate, deprecate, delete, supersede, or redirect either path."
  - "The central NRCS package remains a 0.0.0 empty shell, and the proposed products/scan.py module and product-specific tests were not found."
  - "The inspected SCAN registry record is a minimal inventory placeholder and the source-authority register has no entries; source activation is not established."
  - "The product page uses observed/candidate lifecycle language while the family catalog uses primary/restricted authority-use classes; an accepted descriptor and contract must reconcile the machine vocabulary."
  - "External details such as endpoints, station inventory, variables, units, sensor depths, cadences, timezone behavior, quality flags, rights, and attribution are version-sensitive and are not pinned here as implementation facts."
  - "A SCAN record remains station-, network-, variable-, time-, cadence-, unit-, quality-, and where applicable depth-scoped. It is not area, soil-column, compliance, water-rights, forecast, alert, or management truth."
  - "Connector activity is limited to explicit source admission and RAW or QUARANTINE handoff."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# NRCS SCAN Sibling Compatibility and Source-Admission Boundary

`connectors/nrcs-scan/`

> Repository-present but placement-conflicted sibling boundary for USDA NRCS Soil Climate Analysis Network source admission. Current evidence establishes a documentation lane—not a runnable connector, active source, approved endpoint, tested parser, or release-ready station-observation workflow.

![status](https://img.shields.io/badge/status-draft-yellow)
![version](https://img.shields.io/badge/version-v0.2-informational)
![maturity](https://img.shields.io/badge/maturity-README--only-lightgrey)
![placement](https://img.shields.io/badge/placement-CONFLICTED-orange)
![source](https://img.shields.io/badge/source-NRCS__SCAN-2e7d32)
![network](https://img.shields.io/badge/network-off__by__default-critical)
![lifecycle](https://img.shields.io/badge/lifecycle-RAW%20%7C%20QUARANTINE-blue)
![area truth](https://img.shields.io/badge/area__truth-DENIED-red)
![tribal posture](https://img.shields.io/badge/Tribal__SCAN-review__required-orange)

**Quick links:** [Purpose](#purpose) · [Status](#status-and-evidence) · [Authority](#authority-boundary) · [Directory basis](#directory-rules-basis) · [Topology](#topology-and-compatibility) · [Context](#bounded-context) · [Invariants](#keystone-invariants) · [Inputs](#explicit-input-contract) · [Transport](#transport-and-security) · [Identity](#source-network-station-and-record-identity) · [Time](#time-cadence-freshness-and-vintage) · [Parsing](#parsing-and-preservation-contract) · [Quality](#quality-missingness-and-uncertainty) · [Depth](#sensor-depth-and-soil-variable-boundary) · [Tribal](#tribal-scan-rights-sovereignty-and-sensitivity) · [Admission](#source-admission-handoff) · [Outcomes](#connector-outcomes-and-reason-codes) · [Testing](#testing-and-fixtures) · [Pipeline](#watcher-pipeline-and-publication-separation) · [Implementation](#smallest-sound-implementation-sequence) · [Done](#definition-of-done) · [Open](#open-verification-register) · [Rollback](#rollback-correction-deprecation-and-supersession)

> [!IMPORTANT]
> **This README is not an activation or placement decision.** Path presence does not establish a canonical implementation, active SourceDescriptor, approved source surface, parser, fixtures, tests, receipts, schedules, CI enforcement, deployment, or publication readiness.

> [!CAUTION]
> **A SCAN station record is not an area claim or operational advisory.** A connector may preserve a station reading and its metadata. It may not silently interpolate, aggregate, substitute depths, collapse cadences, claim conservation compliance or water-rights status, issue management advice, or publish a public result.

---

<a id="purpose"></a>

## Purpose

This README defines the allowed source-admission boundary for `connectors/nrcs-scan/` while the repository contains both a sibling and a nested SCAN lane.

A future implementation associated with this path may exist only after governance either:

1. selects this lane as canonical;
2. classifies it as a transitional or compatibility adapter; or
3. explicitly keeps it as documentation-only while implementation lives under the NRCS family package.

Any allowed implementation must remain:

- subordinate to the canonical `connectors/` responsibility root;
- subordinate to the NRCS family boundary;
- descriptor-gated and source-activation-aware;
- no-network by default;
- fixture-first and deterministic;
- explicit about approved source locators and report/query profiles;
- bounded in timeouts, retries, redirects, pagination, payload size, archive handling, and decompression;
- lossless about source, network, station, report/query, record, variable, time, cadence, units, quality, missingness, depth, freshness, and correction context;
- rights-, sovereignty-, and sensitivity-aware without becoming policy authority;
- limited to RAW or QUARANTINE admission candidates;
- separate from normalization, aggregation, modeling, evidence closure, release, public API, UI, map, notification, and AI behavior.

It must not become:

- a second independent NRCS implementation;
- an NRCS or SCAN doctrine home;
- a SourceDescriptor registry;
- an endpoint catalog embedded in prose;
- a watcher or scheduler authority;
- a Soil, Hydrology, Agriculture, or Atmosphere truth resolver;
- a compliance, water-rights, drought, forecast, alert, or management-advice service;
- an evidence, policy, proof, release, or publication system;
- a public API, UI, map, search, notification, or generated-answer surface.

[Back to top](#top)

---

<a id="status-and-evidence"></a>

## Status and evidence

### Current repository state

| Surface | Status | Safe conclusion |
|---|---:|---|
| `connectors/nrcs-scan/README.md` | **CONFIRMED v0.1 before this revision** | The flat sibling boundary exists. |
| Flat sibling `__init__.py`, `client.py`, `parser.py` | **NOT FOUND in bounded checks** | No implementation is established in this lane. |
| `connectors/nrcs/scan/README.md` | **CONFIRMED v0.1** | A nested README boundary also exists. |
| `connectors/nrcs/README.md` | **CONFIRMED v0.1** | The family README identifies `connectors/nrcs/` as the canonical family spine and records SCAN placement as unresolved. |
| `connectors/nrcs/src/README.md` | **CONFIRMED v0.1** | A central source-root contract exists. |
| `connectors/nrcs/src/nrcs/README.md` | **CONFIRMED v0.1** | A central Python package contract exists. |
| `connectors/nrcs/src/nrcs/__init__.py` | **CONFIRMED empty** | Package presence does not establish exports or behavior. |
| `connectors/nrcs/src/nrcs/products/scan.py` | **NOT FOUND** | No central SCAN product adapter is established. |
| `connectors/nrcs/pyproject.toml` | **CONFIRMED placeholder** | Distribution name is `kfm-connector-nrcs`; version is `0.0.0`. |
| `connectors/nrcs/tests/README.md` | **CONFIRMED v0.1** | A family test contract exists, but executable coverage is unproved. |
| `test_scan.py` / `test_scan_parser.py` | **NOT FOUND in bounded checks** | No product-specific test is established at those expected paths. |
| `docs/sources/catalog/nrcs/scan-soil-climate.md` | **CONFIRMED draft product page** | It provides proposed doctrine and identifies current external facts as needing verification. |
| `docs/sources/catalog/nrcs.md` | **CONFIRMED draft family profile** | It recognizes SCAN and Tribal SCAN with distinct authority-use and sensitivity postures. |
| `data/registry/sources/soil/nrcs-scan.yaml` | **CONFIRMED minimal placeholder** | Status is `PROPOSED`; it does not establish a mature descriptor or activation. |
| Other tested descriptor homes | **NOT FOUND** | No alternative active descriptor was established in the bounded checks. |
| `control_plane/source_authority_register.yaml` | **CONFIRMED proposed and empty** | SCAN is not activated there. |
| `pipelines/domains/soil/scan_awdb_ingest/README.md` | **CONFIRMED draft** | A downstream normalization boundary exists; runtime implementation remains unproved. |
| `pipeline_specs/soil/scan_awdb_ingest.yaml` | **NOT FOUND** | The README reference does not prove an executable/declarative spec at that path. |
| `.github/workflows/connector-gate.yml` | **CONFIRMED TODO-only** | A green workflow run cannot prove connector behavior. |

### Evidence boundary

This README may confidently state that the paths and documents above exist at the inspected snapshot. It must not claim:

- canonical placement;
- source activation;
- an accepted source role or role-vocabulary profile;
- package installability;
- a working client or parser;
- approved live endpoints;
- current station or variable inventory;
- accepted depth, cadence, timezone, missing-value, or quality vocabularies;
- executable tests or CI enforcement;
- successful captures or receipts;
- schedules, deployment, consumers, runtime health, or release readiness.

[Back to top](#top)

---

<a id="authority-boundary"></a>

## Authority boundary

### This lane may own, if ratified

- product-specific compatibility documentation;
- a thin compatibility adapter to the accepted central implementation;
- explicit request-profile types for approved SCAN source surfaces;
- bounded transport invocation helpers;
- source-response metadata capture;
- station/report/query manifest candidates;
- product-specific parser adapters;
- source-native parsed-record candidates;
- deterministic content-digest and replay helpers;
- RAW or QUARANTINE admission-candidate construction;
- connector-local finite outcomes and errors;
- tests and fixtures only if repository placement is accepted.

### This lane does not own

| Concern | Owning boundary |
|---|---|
| NRCS family or SCAN product meaning | `docs/sources/catalog/nrcs.md` and `docs/sources/catalog/nrcs/scan-soil-climate.md` |
| Active source identity and activation | Accepted SourceDescriptor and source-authority records |
| Source role, authority-use class, cadence, rights, sensitivity | Accepted source contracts, descriptors, and policy |
| Soil, Hydrology, Agriculture, Atmosphere object meaning | Domain contracts and documentation |
| Machine shape | `schemas/` under accepted schema homes |
| Downstream normalization | `pipelines/domains/soil/scan_awdb_ingest/` or accepted pipeline home |
| Lifecycle storage | `data/raw/`, `data/quarantine/`, and downstream lifecycle roots |
| Receipts and evidence closure | `data/receipts/`, `data/proofs/`, validators, and review |
| Public release | `release/` plus policy and review |
| Public API/UI/map/AI behavior | Governed application and released-artifact surfaces |

### Prohibited authority claims

This README cannot establish that:

- SCAN is active;
- Tribal SCAN data are cleared for public use;
- a station is current, healthy, or representative;
- a value proves conditions outside its station/depth/time scope;
- an NRCS record proves compliance, eligibility, ownership, management, or water-rights status;
- a near-current record is safe for operational use;
- a parser or release is correct merely because the README describes it.

[Back to top](#top)

---

<a id="directory-rules-basis"></a>

## Directory Rules basis

The target remains under the existing `connectors/` responsibility root because its only permissible concern is source-specific fetch, parse, integrity, provenance, and admission support.

Directory Rules establish that:

```text
connectors/ -> data/raw/<domain>/<source_id>/<run_id>/
           -> data/quarantine/<domain>/<source_id>/<run_id>/
```

Connectors must not publish, mutate canonical truth, or write directly to processed, catalog, or published stores.

Directory Rules list `connectors/nrcs/` in the connector-family spine. The repository also contains `connectors/nrcs/scan/` and this sibling path. Therefore:

- `connectors/nrcs/` is the family responsibility boundary;
- the final SCAN implementation home remains a placement decision;
- this README must not create a parallel implementation by implication;
- any path change requires an accepted ADR or migration note with compatibility and rollback;
- source doctrine, descriptors, schemas, policy, lifecycle data, receipts, proofs, release, and public surfaces remain outside this lane.

[Back to top](#top)

---

<a id="topology-and-compatibility"></a>

## Topology and compatibility

### Current topology

```text
connectors/nrcs/                  # family boundary
├── src/nrcs/                    # central Python package shell
├── tests/                       # family test-boundary README
└── scan/README.md               # nested SCAN README-only lane

connectors/nrcs-scan/README.md   # this sibling README-only lane
```

### Status of each lane

| Path | Current safe classification |
|---|---|
| `connectors/nrcs/` | Family boundary named in Directory Rules. |
| `connectors/nrcs/scan/` | Nested README-only product boundary; implementation not established. |
| `connectors/nrcs-scan/` | Sibling README-only compatibility candidate; implementation not established. |
| `connectors/nrcs/src/nrcs/products/scan.py` | Not found in bounded check. |

### Freeze-by-default rule

Until an accepted placement decision exists, do not create independent copies of:

- clients or transport logic;
- parser implementations;
- source identifiers or SourceDescriptors;
- endpoint or request configuration;
- credentials or secret references;
- fixture authorities;
- test suites;
- package exports or import aliases;
- schedules or watcher jobs;
- receipts, release records, or public consumers.

A compatibility lane may delegate to one accepted implementation. It must not become a second source of behavior or truth.

### Required migration decision

Any consolidation must specify:

1. canonical path;
2. canonical source ID and descriptor home;
3. treatment of `connectors/nrcs-scan/` and `connectors/nrcs/scan/`;
4. compatibility class: transitional, deprecated, mirror, or removed;
5. import and configuration migration;
6. fixture and test migration;
7. reference updates;
8. deprecation window;
9. correction and receipt continuity;
10. rollback target and validation.

[Back to top](#top)

---

<a id="bounded-context"></a>

## Bounded context

This connector boundary concerns source admission for SCAN-family station records and explicit source-response metadata.

It may preserve candidates describing:

- source family and source surface;
- network identity such as SCAN or a separately governed Tribal SCAN context;
- station identity and source station metadata;
- report/query identity;
- record identity;
- variable/element identity;
- observation and report times;
- cadence and duration;
- units and value representation;
- sensor depth where applicable;
- source quality and missing-value signals;
- retrieval status and content integrity;
- rights, attribution, sovereignty, sensitivity, and routing references;
- freshness and correction context.

It does not perform:

- station interpolation;
- county, watershed, field, or raster generalization;
- soil-column integration;
- data fusion with Mesonet, USCRN, SMAP, SNOTEL, or other sources;
- normals or anomaly computation;
- drought, irrigation, crop, yield, or management interpretation;
- regulatory, conservation-compliance, or water-rights determinations;
- public release or operational guidance.

[Back to top](#top)

---

<a id="keystone-invariants"></a>

## Keystone invariants

1. **Source admission only.** The lane may prepare RAW or QUARANTINE candidates and nothing later.
2. **Import is not activation.** Package or path presence cannot establish source availability or permission.
3. **No hidden network.** Live access must be explicit, descriptor-gated, and configuration-bound.
4. **Station is not area.** A station record cannot silently become a county, watershed, field, or raster value.
5. **Depth is identity.** Depth-aware variables must preserve source depth value and unit; depths cannot be substituted.
6. **Cadence is identity.** Hourly, daily, monthly, seasonal, annual, report-duration, and derived outputs remain distinct.
7. **Time roles do not collapse.** Observation, report-window, source-update, retrieval, processing, correction, and supersession times remain distinguishable.
8. **Network identity remains visible.** SCAN and Tribal SCAN contexts cannot be silently merged.
9. **Quality and missingness remain visible.** Source flags and missing conventions cannot be dropped or guessed.
10. **Observation is not normal or aggregate.** Raw readings, calculated values, normals, medians, averages, percent-of-normal, and modeled derivatives remain distinct.
11. **Watcher is non-publisher.** Source-change or heartbeat signals are review candidates, not admitted readings or public truth.
12. **Rights and sovereignty fail closed.** Unresolved Tribal, rights, redistribution, or sensitivity posture routes to quarantine or denial.
13. **No life-safety or management advice.** SCAN does not become a warning, forecast, drought declaration, irrigation instruction, or emergency service.
14. **No compliance authority.** Records do not prove conservation compliance, program participation, field practice, or water-rights status.
15. **Deterministic replay.** The same captured bytes and explicit profile must yield the same parse candidate and digest.
16. **Corrections are new state.** Changed bytes or interpretation require explicit lineage, not silent overwrite.
17. **References do not become authority.** Descriptor, policy, receipt, proof, and release references must resolve through their owning systems.
18. **Public clients stay behind the trust membrane.** No public client reads this lane or lifecycle stores directly.

[Back to top](#top)

---

<a id="explicit-input-contract"></a>

## Explicit input contract

A connector invocation should accept an immutable, explicit request profile rather than discovering behavior from ambient state.

### Minimum request context

| Input | Required treatment |
|---|---|
| SourceDescriptor reference and revision | Required before live retrieval; must resolve to accepted source identity, product scope, rights, sensitivity, and activation posture. |
| Product/network identity | Preserve NRCS family, SCAN product, network class, and any source-exposed product/version identity. |
| Approved locator | Use an allowlisted source locator supplied by configuration; do not hard-code changing endpoints in this README. |
| Request/report/query profile | Preserve requested station set, elements, depths, duration, function, value type, report period, output format, and pagination/listing context where applicable. |
| Retrieval policy | Bind schemes, hosts, redirects, timeouts, retries, backoff, rate limits, maximum bytes, pagination bounds, and resume behavior. |
| Integrity expectations | Preserve expected object identity, size, checksum algorithm/digest, encoding, compression, and source metadata when known. |
| Time interpretation profile | Preserve source timezone behavior and distinct observation/report/retrieval/correction roles. |
| Quality/missingness profile | Identify accepted source flag vocabulary and missing-value treatment; unknown values fail closed. |
| Depth profile | Require explicit depth value/unit for depth-aware variables; unknown or conflicting depth routes to quarantine. |
| Routing context | Name proposed owning domain and RAW/QUARANTINE destination without granting promotion. |
| Rights and sensitivity references | Carry approved governing references; unresolved posture does not become implicit permission. |
| Replay identity | Pin connector/profile version, fixture or payload digest, and deterministic parse settings. |

### Ambient-state prohibition

Connector behavior must not silently depend on:

- developer workstation state;
- current working directory;
- unreviewed environment variables;
- credentials loaded at import time;
- user-specific cookies or browser sessions;
- a live endpoint selected by fallback;
- local timezone or locale;
- current date used to reinterpret source records;
- unpinned external documentation;
- AI-generated field mappings or guessed units.

[Back to top](#top)

---

<a id="transport-and-security"></a>

## Transport and security

### Default posture

```text
network: disabled unless explicitly invoked
credentials: external secret reference only when approved
schemes: allowlist
hosts: allowlist
redirects: bounded and revalidated
timeouts: required
retries: bounded
backoff: bounded
rate limits: respected
pagination/listing: bounded
response bytes: bounded
archive members: bounded
expanded bytes: bounded
logs: sanitized
writes: caller-owned temporary or admission handoff only
```

### Required controls

- reject non-approved schemes and hosts;
- resolve and re-check redirect targets;
- mitigate SSRF, loopback, link-local, metadata-service, and private-network targets;
- bound DNS, connection, read, and total request time;
- avoid retry storms and retry only safe operations;
- honor source-side throttling and retry guidance;
- cap page count, object count, record count, and total bytes;
- reject unexpected content type or encoding;
- validate archive member names and prevent traversal;
- cap compressed and expanded sizes and compression ratios;
- reject unsafe serialization formats and object construction;
- sanitize station names, source messages, and other untrusted text before logging;
- redact authorization headers, cookies, tokens, signed parameters, and private URLs;
- avoid logging full sensitive or Tribal-linked payloads;
- preserve response status, headers needed for provenance, observed length, digest, and retrieval time;
- return finite failures rather than partial success disguised as complete capture.

### Dependency posture

Any future implementation must pin and review dependencies, minimize transitive packages, avoid unreviewed plugin loading, and prevent dependency confusion between the distribution name and import namespace.

[Back to top](#top)

---

<a id="source-network-station-and-record-identity"></a>

## Source, network, station, and record identity

### Identity hierarchy

Preserve every source-exposed layer that is needed to distinguish records:

```text
source family
  -> source surface / product
    -> network
      -> station
        -> request or report profile
          -> variable / element
            -> sensor depth, when applicable
              -> observation time
                -> source record or row
```

### Required distinctions

- source profile is not source activation;
- network is not station;
- station identifier is not station name;
- current station metadata is not historical station metadata;
- variable is not unit;
- depth value is not depth label;
- report/query identity is not record identity;
- a normal or aggregate is not a native observation;
- corrected or superseded material is not the original capture;
- a station location is not area coverage.

### Deterministic identity candidates

Exact canonical IDs require accepted contracts. A future implementation may construct candidates from a versioned canonicalization profile over fields such as:

- accepted source ID and descriptor revision;
- network ID;
- source station ID;
- source object/report/query identity;
- variable/element identity;
- depth value and unit;
- source observation timestamp and timezone interpretation;
- source record key or stable row identity;
- source vintage/correction marker.

Do not invent identity from display labels, array position, local row number alone, or unstable query ordering.

[Back to top](#top)

---

<a id="time-cadence-freshness-and-vintage"></a>

## Time, cadence, freshness, and vintage

### Separate time kinds

Preserve, where exposed or generated by the governed process:

| Time kind | Meaning |
|---|---|
| Observation time | Time the source associates with the station reading. |
| Report-window start/end | Time interval requested or represented by the report/query. |
| Source update time | Source-provided publication or modification time. |
| Retrieval time | Time KFM obtained the bytes or response. |
| Processing time | Time the connector parsed or evaluated the capture. |
| Freshness evaluation time | Time a heartbeat/staleness decision was evaluated. |
| Correction time | Time a correction was identified or issued. |
| Supersession time | Time a new artifact superseded an earlier artifact. |

Never replace an unknown source time with retrieval time without an explicit, separately labeled field.

### Cadence boundary

Source-native and source-derived outputs must retain cadence or duration semantics. Do not silently reinterpret:

- sub-daily as daily;
- daily as monthly;
- report duration as source-native cadence;
- annual or seasonal values as observations;
- normals, medians, averages, percentages, or counts as raw readings.

### Freshness boundary

Near-current data require an accepted freshness profile. The connector may preserve inputs needed for downstream freshness evaluation, but it must not invent a universal heartbeat threshold in this README.

Stale, delayed, future-dated, timezone-ambiguous, contradictory, or incomplete records route to finite review outcomes. Staleness is not proof of safe conditions or no event.

### Vintage and correction

Changed bytes at the same locator or for the same apparent record must not silently replace earlier captures. Preserve old and new digests, request profile, observed metadata, correction/supersession relationship, and review status.

[Back to top](#top)

---

<a id="parsing-and-preservation-contract"></a>

## Parsing and preservation contract

### Parser posture

Parsers should be pure or side-effect-minimal functions over supplied bytes, decoded text, records, and explicit profiles.

They must:

- reject unsupported or ambiguous formats;
- preserve source field names and source metadata before normalization;
- preserve raw values separately from parsed candidates;
- preserve units rather than guessing or silently converting;
- preserve timezone/source-time evidence;
- preserve network and station identity;
- preserve depth and depth unit where applicable;
- preserve quality flags and missing-value codes;
- preserve raw/calculated/normal/aggregate/modelled status where source evidence supports it;
- preserve report/query parameters and output-format identity;
- preserve source and content digests;
- emit deterministic issues for unknown fields or schema drift;
- avoid hidden web lookups or AI-based gap filling;
- avoid interpolation, aggregation, fusion, and management interpretation.

### Prohibited transformations

Do not silently convert:

```text
station reading -> county / watershed / field value
station point -> raster surface
one depth -> another depth
one cadence -> another cadence
missing value -> zero
quality-rejected value -> accepted value
normal / median / average -> raw observation
percent-of-normal -> measured value
watcher heartbeat -> station observation
near-current record -> operational guidance
SCAN -> Tribal SCAN or Tribal SCAN -> ordinary public context
SCAN reading -> Mesonet / USCRN / SMAP / SNOTEL value
station context -> conservation compliance or water-rights determination
```

### Schema drift

Unknown headers, fields, encodings, table structures, units, quality codes, missing codes, network identifiers, timezone conventions, or depth representations must fail closed to quarantine or error. They must not be accepted merely because common fields still parse.

[Back to top](#top)

---

<a id="quality-missingness-and-uncertainty"></a>

## Quality, missingness, and uncertainty

Quality metadata are part of the source record, not optional decoration.

Preserve:

- source quality flags;
- source status or provisional/final indicators, if defined by current evidence;
- missing-value codes and reason context;
- calculated or estimated-value indicators;
- sensor or station status fields;
- source-reported precision or uncertainty, if available;
- parser warnings and schema-drift findings;
- rejected, suspect, unavailable, and not-applicable states distinctly.

Do not:

- treat missing as zero;
- drop rejected/suspect status;
- promote a calculated value to direct observation;
- infer certainty from the absence of a quality flag;
- invent quality categories from prose;
- treat a successful HTTP response as scientific validation;
- treat a parsed record as evidence closure or release approval.

[Back to top](#top)

---

<a id="sensor-depth-and-soil-variable-boundary"></a>

## Sensor depth and soil-variable boundary

For depth-aware soil variables, depth is a required semantic dimension.

A parser must preserve:

- source depth value;
- depth unit;
- source depth label or column identifier;
- variable identity;
- station identity;
- observation time;
- source quality/missingness state;
- any source-exposed sensor or installation metadata;
- the evidence used to interpret depth.

Fail closed when:

- depth is missing for a depth-dependent variable;
- depth unit is unknown;
- multiple depth fields conflict;
- a header changes without an accepted profile update;
- one depth is substituted for another;
- a depth-specific value is presented as a soil-column value;
- a downstream request seeks area or field truth without separate modeled/aggregation evidence.

Exact supported depth values are external, version-sensitive facts and must be verified from approved source evidence and captured in accepted profiles—not hard-coded from this README.

[Back to top](#top)

---

<a id="tribal-scan-rights-sovereignty-and-sensitivity"></a>

## Tribal SCAN, rights, sovereignty, and sensitivity

### Default posture

The repository source profile treats Tribal SCAN as requiring additional review. This README does not convert that doctrine into a complete machine policy.

Until accepted rights, sovereignty, sensitivity, and release rules are bound to an active descriptor:

- treat Tribal SCAN context as review-required;
- preserve network identity explicitly;
- do not merge Tribal and non-Tribal records into one indistinguishable public layer;
- minimize precise station and contextual metadata to what the approved use requires;
- do not infer tribal affiliation, land status, ownership, jurisdiction, or consent from station/network labels;
- do not expose restricted or culturally sensitive context by default;
- route unresolved rights, redistribution, attribution, sovereignty, location, or sensitivity questions to QUARANTINE or DENIED;
- document any redaction, generalization, withholding, delayed release, or access-tier decision with a reason and receipt.

### Rights boundary

A public source interface does not automatically prove unrestricted redistribution or downstream public release. The connector carries references and unresolved flags; policy and release systems decide admissibility.

### No authority substitution

SCAN or Tribal SCAN records do not establish:

- tribal government positions;
- tribal land ownership or jurisdiction;
- cultural-resource status;
- program participation;
- conservation-plan contents;
- water rights;
- legal access;
- private producer or landowner identity.

[Back to top](#top)

---

<a id="source-admission-handoff"></a>

## Source-admission handoff

### Permitted destinations

```text
RAW candidate
QUARANTINE candidate
```

A library/parser function should preferably return an immutable candidate to a governed runner. Persistent lifecycle writes, ingest receipts, and atomic handoff behavior belong to the runner and owning lifecycle contracts.

### Minimum admission-candidate content

Subject to accepted contracts, preserve or reference:

- candidate ID and connector/profile version;
- SourceDescriptor reference and revision;
- source family, product, and network identity;
- approved request/report/query profile;
- source object/response identity;
- station and record identity;
- variable, units, depth, cadence, and source-time metadata;
- quality and missingness metadata;
- retrieval status and relevant response metadata;
- observed and expected sizes;
- source/content digests and canonicalization profile;
- rights, attribution, sovereignty, sensitivity, and routing references;
- finite connector outcome;
- deterministic issue and quarantine reason codes;
- proposed RAW or QUARANTINE destination;
- correction/supersession references;
- receipt handoff context.

### Prohibited direct outputs

The connector must not emit directly to:

- WORK;
- PROCESSED;
- CATALOG;
- TRIPLETS;
- PUBLISHED;
- EvidenceBundle or proof authority;
- release manifests or decisions;
- public API/UI/map/search/notification/AI surfaces;
- compliance, water-rights, drought, forecast, alert, or management-advice products.

[Back to top](#top)

---

<a id="connector-outcomes-and-reason-codes"></a>

## Connector outcomes and reason codes

The exact vocabulary requires an accepted contract. A package-local candidate vocabulary may include:

| Outcome | Meaning |
|---|---|
| `CAPTURED` | Complete source material passed admission preconditions and may be proposed for RAW handoff. |
| `NOT_MODIFIED` | A validated conditional or inventory check found no new capture to admit. |
| `QUARANTINED` | Material was captured or parsed but requires review before RAW admission or downstream use. |
| `SKIPPED` | Explicit scope/configuration excluded the item without implying source absence. |
| `ABSTAINED` | Required evidence was insufficient to make a safe connector decision. |
| `DENIED` | Policy, rights, sensitivity, host, scheme, source, or configuration rules prohibit the operation. |
| `ERROR` | A bounded system or source failure prevented a valid outcome. |

These connector outcomes are not canonical `PolicyDecision` outcomes and must not be silently reused as release or public-answer states.

### Proposed reason-code families

- `SOURCE_DESCRIPTOR_MISSING`
- `SOURCE_INACTIVE`
- `SOURCE_IDENTITY_AMBIGUOUS`
- `PLACEMENT_UNRESOLVED`
- `NETWORK_IDENTITY_UNKNOWN`
- `TRIBAL_REVIEW_REQUIRED`
- `RIGHTS_UNRESOLVED`
- `ATTRIBUTION_UNRESOLVED`
- `SENSITIVITY_UNRESOLVED`
- `LOCATOR_NOT_ALLOWED`
- `REDIRECT_NOT_ALLOWED`
- `RATE_LIMITED`
- `RETRY_EXHAUSTED`
- `PAYLOAD_TOO_LARGE`
- `ARCHIVE_UNSAFE`
- `CONTENT_TYPE_UNEXPECTED`
- `CONTENT_INCOMPLETE`
- `DIGEST_MISMATCH`
- `SCHEMA_DRIFT`
- `STATION_ID_MISSING`
- `VARIABLE_UNKNOWN`
- `UNIT_UNKNOWN`
- `DEPTH_MISSING`
- `DEPTH_CONFLICT`
- `CADENCE_UNKNOWN`
- `TIMEZONE_AMBIGUOUS`
- `STALE_SOURCE`
- `FUTURE_DATED_RECORD`
- `QUALITY_FLAG_UNKNOWN`
- `MISSINGNESS_UNKNOWN`
- `CORRECTION_LINEAGE_MISSING`
- `DOMAIN_ROUTING_UNRESOLVED`
- `AREA_TRUTH_COLLAPSE`
- `COMPLIANCE_CLAIM_ATTEMPT`
- `WATER_RIGHTS_CLAIM_ATTEMPT`
- `OPERATIONAL_GUIDANCE_ATTEMPT`
- `DOWNSTREAM_WRITE_ATTEMPT`

Reason codes must be stable, namespaced if required, safe for logs, and separate from untrusted source messages.

[Back to top](#top)

---

<a id="testing-and-fixtures"></a>

## Testing and fixtures

### Current evidence

The family test README exists, but bounded checks did not establish SCAN-specific executable tests or fixtures. The following are requirements, not coverage claims.

### Default test posture

- network disabled;
- no live credentials, cookies, tokens, private sessions, or source-side effects;
- explicit blocking of unexpected socket/DNS/HTTP access;
- synthetic fixtures preferred;
- minimized, redacted, or explicitly approved public snapshots only;
- temporary directories for any runner-write test;
- deterministic clock/timezone/configuration;
- no publication, release, API, UI, map, or AI output;
- negative paths treated as first-class requirements.

### Minimum test classes

| Test class | Required proof |
|---|---|
| Import safety | Import performs no network, secret, clock-dependent mutation, filesystem write, or lifecycle action. |
| Placement guard | Sibling and nested paths cannot become independent implementations without an accepted migration record. |
| Descriptor gate | Live access and RAW admission require accepted source identity and activation. |
| Configuration | Defaults are no-network and reject unknown hosts, schemes, redirects, units, depths, and quality vocabularies. |
| Transport | Timeouts, retries, rate limits, pagination, sizes, redirects, content type, archives, and partial responses fail safely. |
| Station identity | Station/network/report/record identity remains stable and distinct. |
| Time/cadence | Observation, report, retrieval, freshness, correction, and cadence roles do not collapse. |
| Depth | Depth value/unit are retained and missing/conflicting depth fails closed. |
| Quality/missingness | Flags and missing codes are retained; unknown values quarantine. |
| Product class | Observation, calculated, normal, aggregate, percent-of-normal, and modeled products remain distinct. |
| Tribal review | Tribal SCAN identity triggers accepted review behavior and cannot silently enter ordinary public context. |
| Rights/sensitivity | Unresolved use, attribution, sovereignty, location, or release posture fails closed. |
| Admission | Only RAW or QUARANTINE candidates can be produced. |
| Anti-collapse | Station-as-area, depth, cadence, source-fusion, compliance, water-rights, and guidance collapses are rejected. |
| Correction/replay | Same capture/profile replays deterministically; changed bytes require correction lineage. |
| Security | SSRF, secrets, log injection, unsafe archives, decompression bombs, and unsafe deserialization are blocked. |
| Downstream refusal | Connector code cannot write processed/catalog/published/proof/release/public outputs. |

### Fixture classes

At minimum:

- synthetic station metadata;
- synthetic depth-aware observation records;
- synthetic non-depth climate variable records;
- multiple cadence/report-duration cases;
- quality and missing-value cases;
- stale/future/timezone-ambiguous cases;
- calculated/normal/aggregate versus observation cases;
- Tribal SCAN review-trigger cases;
- malformed/partial/oversized responses;
- schema/header/unit/depth/quality drift cases;
- duplicate and conflicting identity cases;
- correction and supersession cases;
- rights/sensitivity denial cases;
- station-to-area and compliance/guidance misuse cases.

### Fixture metadata

Each fixture should state:

- fixture ID and status;
- synthetic/redacted/minimized/approved classification;
- source family/product/network;
- purpose and expected outcome;
- source evidence or synthetic-generation basis;
- creation/retrieval date;
- digest;
- rights and sensitivity posture;
- redaction/minimization actions;
- supported tests;
- supersession/correction status.

[Back to top](#top)

---

<a id="watcher-pipeline-and-publication-separation"></a>

## Watcher, pipeline, and publication separation

### Connector

The connector fetches or receives explicit source material, preserves provenance and product semantics, and prepares RAW or QUARANTINE admission candidates.

### Watcher

A watcher may detect new readings, delayed heartbeat, source inventory change, schema drift, or correction signals. It emits review candidates and receipts. It does not admit a station record, publish data, or establish source truth.

### Pipeline

The downstream `scan_awdb_ingest` lane may normalize admitted lifecycle material into Soil work/processed candidates and quarantine records. Its README does not prove implementation, and it must not fetch live source data as a hidden connector.

### Publication

Only governed downstream validation, EvidenceBundle closure, policy, catalog/triplet, release, correction, and rollback processes may authorize a public artifact. Public clients use governed APIs and released artifacts, never connector directories or RAW/QUARANTINE stores.

### Required handoff chain

```text
explicit source profile
  -> connector retrieval/capture
  -> RAW or QUARANTINE admission candidate
  -> runner-owned atomic handoff + ingest receipt
  -> downstream domain pipeline
  -> validation and evidence closure
  -> policy and release review
  -> governed public interface
```

[Back to top](#top)

---

<a id="smallest-sound-implementation-sequence"></a>

## Smallest sound implementation sequence

### Stage 0 — resolve governance blockers

- choose or formally defer sibling-versus-nested placement;
- identify owners;
- accept source ID and descriptor home;
- reconcile source-role/authority-use vocabulary;
- establish rights, attribution, Tribal/sovereignty, sensitivity, and activation posture;
- approve an endpoint/request profile and no-network testing method.

**Stop condition:** no live code while source identity, placement, or rights are unresolved.

### Stage 1 — package and import proof

- verify package discovery and build backend;
- keep imports inert;
- define explicit public exports;
- add import-safety and namespace-collision tests.

**Stop condition:** no transport if imports or packaging are ambiguous.

### Stage 2 — result and error types

- define immutable connector outcome and issue types;
- define stable reason codes;
- keep them separate from policy/release outcomes.

### Stage 3 — configuration and transport

- define immutable request/retrieval profiles;
- implement allowlists, timeouts, retries, throttling, pagination, size, archive, redirect, and SSRF controls;
- capture sanitized response metadata and digests.

**Stop condition:** no live access until transport negative tests pass.

### Stage 4 — one fixture-first product slice

- choose one approved SCAN structural profile;
- implement parsing from synthetic/minimized fixtures;
- preserve station, network, variable, time, cadence, unit, quality, missingness, depth, and product class;
- emit parsed candidates and deterministic issues only.

### Stage 5 — admission candidate

- bind an accepted descriptor revision;
- implement RAW/QUARANTINE candidate construction;
- reject all downstream destinations;
- add correction/replay tests.

### Stage 6 — runner and receipts

- implement atomic handoff outside pure parser functions;
- emit ingest receipts through the accepted receipt contract;
- prove rollback and duplicate handling.

### Stage 7 — optional live smoke test

Only after approval:

- opt-in and skipped by default;
- non-mutating and narrowly scoped;
- descriptor-gated;
- rate-limited and size-bounded;
- no sensitive payload retention;
- not required for ordinary unit tests.

### Stage 8 — CI and operational evidence

- replace TODO-only connector workflow steps with substantive checks;
- retain test and validation artifacts;
- document coverage boundaries;
- add correction and rollback drills;
- do not claim production readiness from documentation-only checks.

[Back to top](#top)

---

<a id="definition-of-done"></a>

## Definition of done

This lane is not implemented until all applicable items are proved:

- [ ] Accepted owners replace `OWNER_TBD`.
- [ ] Canonical path or compatibility classification is recorded by ADR/migration note.
- [ ] Source ID and descriptor home are accepted.
- [ ] SCAN and Tribal SCAN activation posture is explicit.
- [ ] Rights, attribution, sovereignty, sensitivity, and location-release rules are approved.
- [ ] Package build backend, discovery, dependencies, and imports are verified.
- [ ] Import performs no network, secret, or filesystem side effects.
- [ ] Endpoint/request profile is approved and versioned.
- [ ] Host/scheme/redirect/timeout/retry/rate-limit/size/archive controls are tested.
- [ ] Parser preserves source-native station, network, record, variable, time, cadence, units, quality, missingness, depth, and product-class fields.
- [ ] Unknown schema, units, depth, quality, or timezone values fail closed.
- [ ] Tribal SCAN review behavior is policy-backed and tested.
- [ ] Station-as-area, depth, cadence, product-class, compliance, water-rights, and guidance collapses are rejected.
- [ ] RAW/QUARANTINE candidate contract is accepted and validated.
- [ ] Pure parser functions do not persist lifecycle data.
- [ ] Runner writes atomically and emits accepted ingest receipts.
- [ ] Replay and correction/supersession behavior are deterministic.
- [ ] Fixtures are synthetic/minimized/redacted/approved and governed.
- [ ] Product-specific no-network tests exist and pass.
- [ ] CI executes substantive checks rather than TODO echoes.
- [ ] Test logs/artifacts are retained and inspectable.
- [ ] Downstream pipeline linkage is explicit and does not hide live fetches.
- [ ] Release, correction, and rollback boundaries are documented and tested.
- [ ] No public client reads connector or lifecycle-internal stores directly.

[Back to top](#top)

---

<a id="open-verification-register"></a>

## Open verification register

| # | Verification item | Status | Required evidence |
|---:|---|---:|---|
| 1 | Accepted connector owner | **NEEDS VERIFICATION** | CODEOWNERS/steward record. |
| 2 | Canonical sibling or nested path | **CONFLICTED** | Accepted ADR/migration note. |
| 3 | Compatibility class for losing path | **NEEDS VERIFICATION** | Deprecation/migration record. |
| 4 | Canonical source ID | **NEEDS VERIFICATION** | Accepted descriptor/identity contract. |
| 5 | Canonical descriptor home | **CONFLICTED / NEEDS VERIFICATION** | Registry decision and schema-home alignment. |
| 6 | Source activation | **NOT ESTABLISHED** | Non-empty approved authority register and decision. |
| 7 | SCAN versus Tribal SCAN activation split | **NEEDS VERIFICATION** | Source descriptors and policy decisions. |
| 8 | Source-role machine vocabulary | **CONFLICTED / NEEDS VERIFICATION** | Accepted source-role contract and descriptor. |
| 9 | Authority-use classification | **NEEDS VERIFICATION** | Accepted source profile/descriptor mapping. |
| 10 | Rights and redistribution | **NEEDS VERIFICATION** | Current authoritative terms and rights record. |
| 11 | Attribution requirements | **NEEDS VERIFICATION** | Rights/citation record. |
| 12 | Tribal/sovereignty review rules | **NEEDS VERIFICATION** | Accepted policy and steward review. |
| 13 | Station-location sensitivity | **NEEDS VERIFICATION** | Sensitivity policy and release profile. |
| 14 | Approved endpoint/source surface | **NEEDS VERIFICATION** | Versioned source profile. |
| 15 | Authentication/access posture | **NEEDS VERIFICATION** | Descriptor and security review. |
| 16 | Host/scheme allowlist | **PROPOSED** | Accepted transport configuration. |
| 17 | Timeout/retry/rate-limit policy | **PROPOSED** | Config contract and tests. |
| 18 | Payload/pagination/archive limits | **PROPOSED** | Config contract and tests. |
| 19 | Current response/file formats | **UNKNOWN** | Captured source docs and fixtures. |
| 20 | Station inventory | **UNKNOWN** | Approved source evidence. |
| 21 | Variable/element vocabulary | **UNKNOWN** | Versioned source profile and fixtures. |
| 22 | Unit vocabulary | **UNKNOWN** | Source profile and parser tests. |
| 23 | Sensor-depth vocabulary | **UNKNOWN** | Source profile and parser tests. |
| 24 | Cadence/report-duration vocabulary | **UNKNOWN** | Source profile and parser tests. |
| 25 | Timezone behavior | **UNKNOWN** | Source docs, fixtures, and time contract. |
| 26 | Quality-flag vocabulary | **UNKNOWN** | Source docs and fixtures. |
| 27 | Missing-value vocabulary | **UNKNOWN** | Source docs and fixtures. |
| 28 | Raw/calculated/normal/aggregate classification | **NEEDS VERIFICATION** | Accepted product profile and tests. |
| 29 | Package build/install behavior | **UNKNOWN** | Hardened `pyproject.toml` and build test. |
| 30 | Public package exports | **UNKNOWN** | Implementation and API contract. |
| 31 | Central SCAN adapter | **NOT FOUND** | Implemented module after placement decision. |
| 32 | Product-specific tests | **NOT FOUND** | Test modules and logs. |
| 33 | Fixture inventory and approval | **UNKNOWN** | Fixture manifest and review. |
| 34 | RAW/QUARANTINE candidate schema | **NEEDS VERIFICATION** | Accepted contract/schema. |
| 35 | Connector outcome vocabulary | **PROPOSED** | Accepted contract and validators. |
| 36 | Reason-code vocabulary | **PROPOSED** | Accepted registry/contract. |
| 37 | Ingest receipt integration | **UNKNOWN** | Runner code, schema, receipts, and tests. |
| 38 | Pipeline spec | **NOT FOUND at tested path** | Accepted declarative spec or corrected reference. |
| 39 | Downstream runtime implementation | **UNKNOWN** | Pipeline code, tests, and logs. |
| 40 | Watcher implementation and heartbeat thresholds | **UNKNOWN** | Watcher contract, tests, and receipts. |
| 41 | CI enforcement | **NOT ESTABLISHED** | Non-TODO workflow and successful required checks. |
| 42 | Scheduled/live operation | **UNKNOWN** | Schedule config and run receipts. |
| 43 | Deployment and runtime health | **UNKNOWN** | Deployment evidence and monitoring. |
| 44 | Downstream consumers | **UNKNOWN** | Imports, configs, or API contracts. |
| 45 | Correction invalidation | **PROPOSED** | Correction contract and integration tests. |
| 46 | Deprecation process | **NEEDS VERIFICATION** | Deprecation register and migration plan. |
| 47 | Rollback automation | **UNKNOWN** | Rollback test and artifacts. |
| 48 | Public release profile | **UNKNOWN** | Evidence, policy, release manifest, and review. |

[Back to top](#top)

---

<a id="rollback-correction-deprecation-and-supersession"></a>

## Rollback, correction, deprecation, and supersession

### Documentation rollback

This v0.2 revision changes documentation only. Restore the prior blob recorded in the metadata or revert the documentation commit if the boundary is found inaccurate.

### Connector rollback

A future implementation rollback should identify:

- connector/package version;
- accepted source/profile version;
- configuration and endpoint profile;
- parser/canonicalization version;
- affected captures and candidate IDs;
- receipt and digest references;
- correction/supersession relationship;
- replacement or prior known-good version;
- reason, reviewer, and timestamp;
- downstream artifacts requiring invalidation or review.

### Source correction

When source bytes, metadata, station identity, quality interpretation, depth, units, cadence, or timezone behavior changes:

1. preserve the original capture and receipt;
2. capture or reference the corrected source material;
3. record old and new digests;
4. identify affected records and downstream artifacts;
5. issue correction/supersession state through owning governance surfaces;
6. re-run validation, evidence, policy, and release gates;
7. never rewrite history silently.

### Path migration

Do not delete or redirect `connectors/nrcs-scan/` solely because the nested README exists. Migration requires an accepted plan, reference inventory, compatibility window, test movement, descriptor/config updates, import checks, receipt continuity, deprecation notice, and tested rollback.

### Supersession rule

A newer README, parser, profile, source file, or station record does not erase an earlier artifact. Supersession must remain explicit and auditable.

[Back to top](#top)

---

## Maintainer summary

`connectors/nrcs-scan/` is presently a **README-only, placement-conflicted sibling boundary** for NRCS SCAN source admission. It is not an active source, runnable connector, tested parser, SourceDescriptor authority, Tribal release decision, station-to-area model, compliance or water-rights authority, pipeline, proof system, release surface, public API, public map, or operational advisory.

Keep the lane frozen against parallel implementation until placement and source identity are governed. Preserve station, network, variable, time, cadence, units, quality, missingness, depth, freshness, rights, sovereignty, sensitivity, and correction context. Fail closed to QUARANTINE, DENIED, ABSTAINED, or ERROR when required evidence is unresolved.

<p align="right"><a href="#top">Back to top</a></p>
