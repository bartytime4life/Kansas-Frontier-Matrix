<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-noaa-src-readme
title: connectors/noaa/src/ — NOAA Connector Source Root and Package Boundary
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Source steward · Connector steward · NOAA steward · Hazards steward · Atmosphere steward · Climate steward · Soil steward · Data steward · Validation steward · Security steward · Docs steward
created: 2026-06-19
updated: 2026-07-15
policy_label: "public-doctrine; implementation-root; source-admission; multi-role; not-life-safety; import-safe; no-network-by-default; raw-quarantine-only; descriptor-gated; rights-aware; sensitivity-aware; provenance-preserving; finite-outcomes; fixture-first; replayable; rollback-aware; no-secrets"
current_path: connectors/noaa/src/README.md
truth_posture: CONFIRMED repository path, NOAA connector-family README, NOAA connector test README, merged NOAA Python package README, empty package __init__.py, package project name and 0.0.0 version, NOAA source-family catalog, connector-root contract, proposed source-admission ADR, and RAW-WORK/QUARANTINE-PROCESSED-CATALOG/TRIPLET-PUBLISHED lifecycle doctrine / PROPOSED source-root organization contract, package discovery, build backend, import namespace, module boundaries, configuration profile, transport interfaces, product-adapter registry, parsed-record model, admission-candidate model, connector outcome and reason-code vocabularies, receipt handoff, and orchestration integration / UNKNOWN complete source-tree inventory, package installability, dependencies, import consumers, active NOAA SourceDescriptor entries, accepted endpoint inventory, product implementations, parser coverage, fixtures, tests, CI, schedules, deployment, runtime health, emitted receipts, and downstream consumers / NEEDS VERIFICATION accepted owners, package metadata hardening, namespace collision review, source-schema home, activation states, rights and sensitivity bindings, network policy, retry/rate-limit policy, validators, fixture approvals, tests, CI, correction workflow, deprecation policy, and rollback automation
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 7862e6c8b3c724839be32bbc465dc159e443e424
  prior_blob: 9327e47383af287222b9d66dcc07a386a940f5c0
  child_package_blob: 1303a10954d16844557653e871f4c0592e87e2c1
  bounded_path_checks:
    - connectors/noaa/src/README.md exists at v0.1 before this revision
    - connectors/noaa/src/noaa/README.md exists at v0.1 and documents an empty package shell
    - connectors/noaa/src/noaa/__init__.py is empty
    - connectors/noaa/src/noaa/client.py was not found in the bounded check recorded by the child README
    - connectors/noaa/pyproject.toml contains only project name and version 0.0.0
    - connectors/noaa/tests/README.md exists as a draft no-network test contract
related:
  - ../README.md
  - ./noaa/README.md
  - ../tests/README.md
  - ../pyproject.toml
  - ../../README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0017-source-descriptor-admission-process.md
  - ../../../docs/sources/catalog/noaa/README.md
  - ../../../docs/sources/catalog/noaa/storm-events.md
  - ../../../docs/sources/catalog/noaa/nws-api.md
  - ../../../docs/sources/catalog/noaa/hms-fire-smoke.md
  - ../../../docs/sources/catalog/noaa/hrrr-smoke.md
  - ../../../docs/sources/catalog/noaa/goes-abi-aod.md
  - ../../../docs/sources/catalog/noaa/viirs-hotspot.md
  - ../../../docs/sources/catalog/noaa/noaa-uscrn.md
  - ../../../docs/sources/catalog/noaa/station-climate-products.md
  - ../../../data/registry/sources/README.md
  - ../../../data/raw/
  - ../../../data/quarantine/
  - ../../../data/receipts/
  - ../../../data/proofs/
  - ../../../contracts/
  - ../../../schemas/
  - ../../../policy/rights/
  - ../../../policy/sensitivity/
  - ../../../release/
tags: [kfm, connectors, noaa, source-root, python, package-boundary, source-admission, multi-role, ncei, nws, hms, hrrr, goes, viirs, uscrn, storm-events, climate, hazards, atmosphere, soil, raw, quarantine, provenance, import-safety, no-network, fixture-first, governance]
notes:
  - "This revision changes only connectors/noaa/src/README.md."
  - "The child package README is now CONFIRMED repository-present on main; the v0.1 source-root statement that the child was future or merely proposed is superseded by this revision."
  - "Repository presence does not establish package implementation: the child README records an empty __init__.py, no client.py at the proposed path, and 0.0.0 project metadata."
  - "NOAA is a multi-role source family; product identity, source role, time kinds, units, quality, geometry, uncertainty, rights, sensitivity, and caveats must remain product-specific."
  - "KFM is not an emergency alerting system."
  - "Code under this source root may prepare RAW or QUARANTINE admission candidates only; it may not publish, promote, close evidence, certify truth, issue alerts, or serve public clients."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# NOAA Connector Source Root and Package Boundary

`connectors/noaa/src/`

> Source-tree boundary for the NOAA connector family. This root organizes importable source-admission code and its package contract; it does not establish NOAA truth, activate a source, issue warnings, approve publication, or own any lifecycle state beyond a governed RAW or QUARANTINE handoff.

![status](https://img.shields.io/badge/status-draft-yellow)
![version](https://img.shields.io/badge/version-v0.2-informational)
![maturity](https://img.shields.io/badge/maturity-empty__package__shell-lightgrey)
![root](https://img.shields.io/badge/root-connectors%2Fnoaa%2Fsrc-blue)
![package](https://img.shields.io/badge/package-noaa__present-0a7ea4)
![source role](https://img.shields.io/badge/source--role-multi--role-purple)
![network](https://img.shields.io/badge/network-off__by__default-critical)
![lifecycle](https://img.shields.io/badge/lifecycle-RAW%20%7C%20QUARANTINE-orange)
![life safety](https://img.shields.io/badge/life__safety-NOT__ALERT__AUTHORITY-red)

**Quick links:** [Purpose](#purpose) · [Status](#status-and-evidence) · [Authority](#authority-boundary) · [Directory basis](#repository-fit-and-directory-rules-basis) · [Snapshot](#confirmed-repository-snapshot) · [Root contract](#source-root-contract) · [Package relationship](#package-boundary-and-inheritance) · [Imports](#import-and-side-effect-contract) · [Packaging](#packaging-and-build-contract) · [Modules](#module-placement-contract) · [Configuration](#configuration-contract) · [Transport](#transport-and-resource-contract) · [Products](#product-lane-and-source-role-contract) · [Parsing](#parsing-and-preservation-contract) · [Admission](#source-admission-handoff-contract) · [Outcomes](#finite-outcome-and-reason-code-contract) · [Provenance](#provenance-identity-and-time) · [Security](#security-and-data-minimization) · [Testing](#testing-and-validation) · [Implementation](#smallest-sound-implementation-sequence) · [Done](#definition-of-done) · [Open](#open-verification-register) · [Rollback](#rollback-correction-deprecation-and-supersession)

> [!IMPORTANT]
> **This is an implementation boundary, not implementation proof.** The source root, package directory, package README, and package marker exist. Current evidence does not establish a working client, parser, product registry, build backend, installable package, source activation, fixtures, tests, CI, live access, scheduled runs, receipts, or production consumers.

> [!CAUTION]
> **KFM is not an emergency alerting system.** NOAA watches, warnings, advisories, forecasts, smoke products, storm records, detections, and station observations may be admitted only as product-specific source material with official-source caveats. This source root must never issue KFM alerts, emergency instructions, or life-safety determinations.

---

<a id="purpose"></a>

## Purpose

This README defines the responsibility boundary for `connectors/noaa/src/`.

The source root may organize code that eventually supports:

- an importable NOAA connector package;
- package-local configuration and immutable request profiles;
- bounded network or file-distribution clients;
- approved fixture loading;
- product-specific adapter dispatch;
- deterministic parsing of captured source payloads;
- source-native metadata preservation;
- product-specific source-role candidates;
- freshness and time-kind preservation;
- rights, attribution, and sensitivity context propagation;
- content-integrity metadata and replay support;
- finite connector outcomes and quarantine reasons;
- RAW or QUARANTINE admission candidates;
- no-network connector-local testing.

It must not become:

- NOAA source-family or product doctrine;
- the active `SourceDescriptor` registry;
- a general-purpose weather SDK;
- a scheduler, watcher, or uncontrolled poller;
- an alert relay or emergency guidance service;
- a domain truth resolver or canonicalizer;
- a policy decision point;
- a schema or semantic-contract authority;
- an EvidenceBundle resolver;
- a processing, catalog, triplet, release, or publication pipeline;
- a public API, UI, map, search, or AI surface;
- a credential or secret store.

The source root exists so package structure, imports, side effects, product boundaries, and source-admission handoff remain explicit and reviewable before executable connector work grows.

[Back to top](#top)

---

<a id="status-and-evidence"></a>

## Status and evidence

### Current repository state

| Surface | Status | Safe conclusion |
|---|---:|---|
| `connectors/noaa/src/README.md` | **CONFIRMED v0.1 before this revision** | The source-root README exists but still describes the child package as future/proposed. |
| `connectors/noaa/src/noaa/README.md` | **CONFIRMED v0.1** | The child package boundary is now repository-present and documents an empty package shell. |
| `connectors/noaa/src/noaa/__init__.py` | **CONFIRMED empty** | A package marker exists; no exported API or runtime behavior is established. |
| `connectors/noaa/src/noaa/client.py` | **NOT FOUND in the child’s bounded check** | The previously proposed client module is not established at that path. |
| `connectors/noaa/pyproject.toml` | **CONFIRMED placeholder** | Project name is `kfm-connector-noaa`; version is `0.0.0`. |
| Build backend, package discovery, dependencies, entry points | **UNKNOWN** | The inspected project metadata does not establish packaging or installability. |
| `connectors/noaa/README.md` | **CONFIRMED draft** | Defines NOAA-family, multi-role, not-life-safety, RAW/QUARANTINE-only boundaries. |
| `connectors/noaa/tests/README.md` | **CONFIRMED draft** | Defines no-network, fixture-first, product-specific test expectations. |
| NOAA source catalog | **CONFIRMED draft doctrine** | Defines heterogeneous NOAA product lanes and anti-collapse rules. |
| Source-admission ADR | **CONFIRMED repository-present; status proposed** | Defines descriptor admission, fixture-before-live behavior, and RAW/QUARANTINE handoff doctrine. |
| Complete source-tree inventory | **UNKNOWN** | This bounded pass verified named paths, not a recursive repository tree. |
| Product code, fixtures, tests, CI, schedules, deployment | **NOT SURFACED / UNKNOWN** | No implementation or operational proof was established. |

### Evidence boundary

This README may confidently state:

- the source-root path exists;
- the package child path and its README exist;
- the package marker is empty;
- project metadata is a `0.0.0` placeholder;
- the family and tests READMEs define draft boundaries;
- NOAA is treated as a multi-role source family;
- connector work is limited to source admission and RAW/QUARANTINE handoff.

This README must not claim:

- package installability;
- accepted Python namespace behavior;
- working imports beyond the empty marker;
- a working HTTP client;
- active NOAA endpoints;
- admitted source descriptors;
- parser correctness;
- test coverage;
- CI enforcement;
- scheduled or deployed connector runs;
- emitted receipts or persisted candidates;
- production health;
- publication safety.

Those claims remain `UNKNOWN`, `PROPOSED`, or `NEEDS VERIFICATION` until code, metadata, tests, workflows, logs, or emitted artifacts prove them.

[Back to top](#top)

---

<a id="authority-boundary"></a>

## Authority boundary

### This source root may own

If implemented and reviewed, `connectors/noaa/src/` may own:

- import-package directories;
- package-local source code;
- package markers and typing markers;
- connector-local configuration types;
- bounded transport interfaces;
- request canonicalization helpers;
- response metadata capture;
- product adapter interfaces;
- product-specific parsers;
- package-local parsed-record types;
- admission-candidate builders;
- package-local finite outcomes and error types;
- content-digest and deterministic replay helpers;
- package-level documentation.

### This source root does not own

| Concern | Owning boundary |
|---|---|
| NOAA source-family and product meaning | `docs/sources/catalog/noaa/` |
| SourceDescriptor records and activation state | `data/registry/sources/` and accepted source-governance artifacts |
| Semantic contracts | `contracts/` under repository-confirmed homes |
| Machine schemas | `schemas/` under repository-confirmed homes |
| Rights and sensitivity decisions | `policy/rights/`, `policy/sensitivity/` |
| Source-side secrets | External secret manager or approved deployment mechanism, never this tree |
| RAW and QUARANTINE persistence | Caller/orchestrator using explicit governed handoff paths |
| Receipts and proofs | `data/receipts/`, `data/proofs/` and their owning workflows |
| WORK, PROCESSED, CATALOG, TRIPLET | Downstream lifecycle roots and pipelines |
| Release decisions and rollback state | `release/` |
| Published artifacts | `data/published/` after governed release |
| Public API and UI behavior | Governed application roots |
| Emergency or alert authority | Official NOAA/NWS source surfaces, not KFM |

### Non-authority rule

A connector result is evidence of source interaction or a candidate for admission. It is not proof that:

- the source is active;
- the record is true;
- the product is current enough for a use;
- the source role is finally accepted;
- rights permit downstream reuse;
- sensitivity permits rendering;
- evidence is closed;
- publication is approved.

[Back to top](#top)

---

<a id="repository-fit-and-directory-rules-basis"></a>

## Repository fit and Directory Rules basis

### Owning responsibility root

`connectors/` is the owning responsibility root because this file governs source-specific fetch, parse, provenance, and admission implementation.

The placement follows responsibility rather than topic:

```text
connectors/noaa/src/        # NOAA connector source-tree implementation
```

It does not create a new root or parallel authority home.

### Lifecycle position

```text
External NOAA source or approved fixture
  -> connectors/noaa/src/
  -> RAW candidate or QUARANTINE candidate
  -> governed persistence and receipt emission by an accepted runner
  -> WORK / QUARANTINE
  -> PROCESSED
  -> CATALOG / TRIPLET
  -> PUBLISHED
```

The source root must not skip lifecycle stages or write directly to downstream truth-bearing stores.

### Compatibility roots preserved

This README does not move or redefine:

- `connectors/`;
- `docs/sources/`;
- `contracts/`;
- `schemas/`;
- `policy/`;
- `data/` lifecycle roots;
- `release/`;
- governed application roots.

Any future move from `connectors/noaa/src/noaa/` to another namespace or package layout requires:

1. a confirmed path decision or ADR when authority boundaries change;
2. import-compatibility analysis;
3. consumer inventory;
4. migration notes;
5. deprecation and removal windows;
6. test evidence;
7. rollback instructions.

[Back to top](#top)

---

<a id="confirmed-repository-snapshot"></a>

## Confirmed repository snapshot

The bounded, directly verified source-root shape is:

```text
connectors/noaa/
├── README.md                     # CONFIRMED family boundary
├── pyproject.toml                # CONFIRMED 0.0.0 placeholder
├── src/
│   ├── README.md                 # this file
│   └── noaa/
│       ├── README.md             # CONFIRMED package boundary
│       └── __init__.py           # CONFIRMED empty
└── tests/
    └── README.md                 # CONFIRMED test boundary
```

This is not asserted as a complete recursive listing. Product-lane documentation and sibling connectors exist elsewhere in the repository, but this source-root snapshot includes only paths directly checked for this package boundary.

### Drift corrected by this revision

The prior source-root README said:

```text
noaa/  # PROPOSED import package; NEEDS VERIFICATION
README.md  # future implementation-package boundary, if created
```

That statement is stale. The package directory and package README are now `CONFIRMED` repository-present. Their implementation maturity remains an empty package shell.

### Safe maturity summary

```text
path presence:       CONFIRMED
package marker:      CONFIRMED empty
package README:      CONFIRMED boundary document
project version:     CONFIRMED 0.0.0 placeholder
working client:      UNKNOWN / not surfaced
product parsers:     UNKNOWN / not surfaced
installability:      UNKNOWN
source activation:   UNKNOWN
fixtures and tests:  UNKNOWN
CI and deployment:   UNKNOWN
```

[Back to top](#top)

---

<a id="source-root-contract"></a>

## Source-root contract

The source root should remain narrow and boring.

### Allowed content classes

- import-package directories;
- `.py` implementation files inside a package;
- `py.typed` if typed-package support is intentionally adopted;
- package-local static typing support that does not become a schema authority;
- package READMEs and maintenance notes;
- small package-local data only when it is code-adjacent, non-sensitive, reviewed, and not source truth;
- generated-code markers only when generation is governed and reproducible.

### Disallowed content classes

- raw NOAA payload archives;
- live response caches;
- credentials, API keys, tokens, cookies, `.env` files, or secret-bearing examples;
- SourceDescriptor authority records;
- source catalog doctrine;
- JSON Schema authority;
- semantic contracts;
- policy bundles or decisions;
- fixtures that belong in the test/fixture authority;
- tests that belong under `connectors/noaa/tests/`;
- receipts, proof packs, release manifests, or published artifacts;
- notebooks or generated reports;
- public UI/API payloads;
- mutable “latest” data snapshots.

### Root-level rule

Files directly under `connectors/noaa/src/` should be exceptional. Importable implementation should live within an explicit package directory. Additional package directories require a documented ownership and namespace reason; convenience alone is insufficient.

[Back to top](#top)

---

<a id="package-boundary-and-inheritance"></a>

## Package boundary and inheritance

The confirmed package child is:

```text
connectors/noaa/src/noaa/
```

Its README defines package-level contracts for imports, configuration, transport, adapters, parsing, admission candidates, outcomes, provenance, policy context, security, tests, and staged implementation.

### Parent/child responsibility split

| Concern | Source-root README | Package README |
|---|---:|---:|
| Source-tree ownership | **Owns** | Inherits |
| Package inventory and relationships | **Owns** | Describes itself |
| Cross-package import rules | **Owns** | Conforms |
| Package-local module APIs | Boundary only | **Owns when implemented** |
| Product adapter interfaces | Shared constraint | Package specialization |
| Parser implementation | Does not own details | Package-local |
| Test-root relationship | **Owns relationship** | Links to tests |
| Build metadata location | **Owns placement rule** | Does not duplicate |
| Source doctrine | No | No |
| Source activation | No | No |
| Publication or alert authority | No | No |

### Inheritance rule

The child package may tighten source-root requirements, but it must not weaken:

- no network at import time;
- no secret access at import time;
- no hidden source activation;
- product-specific source roles;
- explicit time kinds;
- RAW/QUARANTINE-only handoff;
- no direct publication;
- not-life-safety posture;
- deterministic fixture parsing;
- finite, safe failures;
- no direct public API/UI behavior.

### Additional package rule

A second package under `src/` must not be created until reviewers confirm that it has a distinct responsibility and will not duplicate `noaa/`. Candidate examples such as `noaa_cli`, `noaa_models`, or `noaa_shared` are `PROPOSED` only and should not be created without evidence of need.

[Back to top](#top)

---

<a id="import-and-side-effect-contract"></a>

## Import and side-effect contract

Importing any package under this source root must be safe.

### Import-time prohibitions

An import must not:

- call NOAA, NWS, NCEI, cloud storage, or any external service;
- probe DNS or network connectivity;
- read credentials, API keys, tokens, cookies, or private certificate material;
- require an account or authenticated session;
- enumerate source registries or lifecycle stores;
- open or write cache files;
- create directories;
- write RAW, QUARANTINE, receipts, logs, temporary payloads, or outputs;
- start threads, processes, schedulers, event loops, or watchers;
- mutate global environment state;
- select a live endpoint implicitly;
- configure root logging handlers;
- emit warnings that reveal secrets or source payloads.

### Public import surface

Until implementation is proved, the package export surface is `UNKNOWN`.

When adopted, `noaa/__init__.py` should:

- remain small;
- export only reviewed stable names;
- avoid importing optional network clients eagerly;
- avoid wildcard exports;
- define `__all__` when a stable surface exists;
- avoid performing version discovery that requires package installation or filesystem mutation;
- avoid re-exporting domain truth or policy authority types.

### Namespace collision review

The top-level package name `noaa` may collide with third-party or local packages. Before treating it as a stable public namespace, verify:

- workspace package discovery;
- dependency graph collisions;
- import behavior in editable and wheel installs;
- test runner path behavior;
- deployment environment behavior;
- whether a namespaced package such as `kfm_connectors.noaa` is required.

A namespace change is a compatibility decision and must include migration and rollback evidence.

[Back to top](#top)

---

<a id="packaging-and-build-contract"></a>

## Packaging and build contract

`connectors/noaa/pyproject.toml` currently proves only:

```toml
[project]
name = "kfm-connector-noaa"
version = "0.0.0"
```

It does not establish:

- a build backend;
- `requires-python`;
- package discovery;
- runtime dependencies;
- optional development dependencies;
- entry points;
- license metadata;
- README packaging;
- typed-package support;
- wheel or source-distribution behavior;
- test configuration;
- lint/type-check configuration.

### Required packaging decisions before installability is claimed

| Decision | Required evidence |
|---|---|
| Build backend | Accepted `build-system` configuration and successful clean build. |
| Package discovery | Verified inclusion of the intended package and exclusion of tests/data. |
| Python support | Explicit `requires-python` aligned with repository policy. |
| Runtime dependencies | Minimal, pinned or bounded according to repository standards. |
| Optional live dependencies | Separated from fixture-only parsing where practical. |
| Version source | Single, deterministic source; no mutable runtime lookup. |
| Entry points | Added only when a CLI or runner has a confirmed owner and contract. |
| Editable install | Verified without changing import semantics. |
| Wheel contents | Inspected for secrets, fixtures, bulk payloads, or accidental files. |
| Reproducibility | Build commands and resulting metadata documented and tested. |

### Packaging anti-patterns

- declaring the package installable because `pyproject.toml` exists;
- adding dependencies before a module requires them;
- hiding network activation in an entry point;
- bundling raw NOAA samples in wheels;
- duplicating source contracts or schemas as package data;
- deriving version from network or git state at runtime;
- making tests pass only when repository root is on `PYTHONPATH` accidentally.

[Back to top](#top)

---

<a id="module-placement-contract"></a>

## Module placement contract

The package child README proposes module responsibilities. This parent document governs how any such modules fit under `src/`.

### Proposed package layout

The following remains `PROPOSED`, not a current inventory:

```text
connectors/noaa/src/
├── README.md
└── noaa/
    ├── README.md
    ├── __init__.py
    ├── config.py
    ├── transport.py
    ├── products.py
    ├── parser.py
    ├── admission.py
    ├── provenance.py
    ├── outcomes.py
    ├── errors.py
    └── adapters/
        ├── storm_events.py
        ├── nws_api.py
        ├── hms_smoke.py
        ├── hrrr_smoke.py
        ├── goes_abi_aod.py
        ├── viirs_hotspot.py
        ├── uscrn.py
        └── station_climate.py
```

The exact names must follow the smallest accepted implementation and may differ.

### Placement rules

| Responsibility | Placement posture |
|---|---|
| Configuration values and validation | Package-local module; no secret values committed. |
| HTTP/file transport | Package-local bounded interface; no scheduler ownership. |
| Product dispatch | Explicit registry or mapping; unknown product fails closed. |
| Product parsing | One product-specific adapter or clearly separated parser family. |
| Admission candidate construction | Package-local helper returning data, not writing lifecycle stores. |
| Provenance capture | Package-local metadata helper; receipt authority remains external. |
| Finite outcomes and errors | Package-local types until a cross-connector contract is accepted. |
| Shared cross-connector utilities | Move only after multiple connectors prove a common need. |
| Tests | `connectors/noaa/tests/`, not `src/noaa/`. |
| Fixtures | Connector-local or repository fixture authority, not source package data. |

### Avoid premature abstraction

Do not create a large generic NOAA framework before one product path is implemented end to end with:

- an admitted descriptor;
- a synthetic fixture;
- deterministic parsing;
- source-role preservation;
- admission-candidate output;
- negative tests;
- rollback instructions.

[Back to top](#top)

---

<a id="configuration-contract"></a>

## Configuration contract

Configuration must be explicit, immutable where practical, safe to log after redaction, and separate from source truth.

### Proposed configuration families

| Family | Examples | Required posture |
|---|---|---|
| Product selection | product key, distribution family, adapter name | Explicit; unknown product fails closed. |
| Network mode | disabled, fixture-only, live-opt-in | Disabled or fixture-only by default in tests. |
| Endpoint profile | approved base URL key, distribution path template | Allowlisted; descriptor-gated; no arbitrary user URL by default. |
| Timeouts | connect, read, total | Finite and bounded. |
| Retries | maximum attempts, backoff, retryable statuses | Finite, observable, no retry storms. |
| Rate limits | requests per interval, concurrency | Product/source-specific and bounded. |
| Payload limits | maximum bytes, decompressed bytes, record count | Explicit protection against resource exhaustion. |
| Caching | disabled, conditional request, caller-owned cache | No hidden mutable cache. |
| User agent | repository-approved identifier and contact posture | Explicit and source-compliant. |
| Parsing profile | product version, parser profile, strictness | Recorded with candidate/provenance metadata. |
| Output mode | return candidate, return quarantine candidate | No implicit persistent writes. |

### Environment variables

Environment variables may supply deployment configuration only when accepted by repository policy.

Rules:

- no environment reads at import time;
- no secret values in examples, logs, exceptions, or receipts;
- explicit mapping from environment names to typed configuration;
- missing required live configuration fails before network access;
- unknown variables do not silently change behavior;
- test defaults remain no-network.

### Configuration identity

A consequential run should be reproducible from a redacted configuration fingerprint or spec hash. The fingerprint must exclude secrets while including behavior-changing fields.

[Back to top](#top)

---

<a id="transport-and-resource-contract"></a>

## Transport and resource contract

Transport code must be bounded, source-aware, and non-authoritative.

### Required controls

- explicit endpoint allowlist or descriptor-approved distribution reference;
- HTTPS by default unless an accepted source exception exists;
- finite connect/read/total timeouts;
- finite retries with bounded backoff and jitter where appropriate;
- retry classification by safe method and response status;
- rate-limit and `Retry-After` handling;
- maximum response size;
- maximum decompressed size;
- content-type and file-signature checks;
- redirect limits and destination validation;
- conditional request support when source metadata permits;
- safe temporary-file handling when streaming is required;
- digest calculation over captured bytes;
- explicit cancellation and cleanup;
- sanitized request and response metadata for logging/receipts.

### Transport must not

- follow arbitrary redirects to unapproved hosts;
- accept `file://`, loopback, link-local, or private-network destinations from untrusted input;
- retry forever;
- turn a `404`, `204`, empty file, or source-side no-data state into fabricated records;
- parse an HTML error page as a data product;
- decompress unbounded archives;
- extract paths outside a controlled directory;
- disable TLS verification silently;
- log authorization headers, cookies, query secrets, or complete sensitive payloads;
- schedule repeated polling on its own.

### Live access gate

Live access requires all of the following, when applicable:

1. source descriptor reference;
2. allowed activation state;
3. approved product lane;
4. rights and citation posture;
5. sensitivity posture;
6. explicit live-mode configuration;
7. finite timeout and rate-limit profile;
8. approved endpoint/distribution;
9. receipt-capable orchestration;
10. rollback or disable path.

Missing or unresolved support must fail closed before the request is sent.

[Back to top](#top)

---

<a id="product-lane-and-source-role-contract"></a>

## Product-lane and source-role contract

NOAA is a source family, not one epistemic role.

The final role for an admitted source belongs to its accepted SourceDescriptor and governance records. The table below records typical or doctrinal posture that implementations must preserve; it is not a substitute for descriptor admission.

| Product lane | Typical role posture | Non-negotiable anti-collapse rule |
|---|---|---|
| Storm Events | historical observed event record, with contextual fields | Do not turn a record into a current alert, continuous measurement, flood extent, or disaster declaration. |
| NWS API | official forecast/alert/observation context; regulatory or contextual role as accepted | Do not rebroadcast as a KFM-issued warning or life-safety instruction. |
| HMS Fire and Smoke | mixed analysis/detection product | Keep fire detections and smoke polygons distinct; qualitative density is not concentration or exposure. |
| HRRR-Smoke | modeled forecast | Preserve model run, cycle, forecast hour, valid time, grid/version, and modeled caveats. |
| GOES ABI AOD | satellite retrieval | Aerosol optical depth is not PM2.5 or ground-level exposure. |
| VIIRS Hotspot | satellite thermal detection | A detection is not confirmed ground-fire perimeter, cause, severity, or incident authority. |
| USCRN | station observation/reference network product | A station value is not area-wide truth; preserve station, cadence, variable, units, depth, and flags. |
| Station climate products | observed, modeled, or aggregate depending on product | Do not collapse observations, normals, anomalies, reanalysis, and model fields. |

### Product identity requirements

Every parsed result or admission candidate should preserve, where applicable:

- source family;
- product key;
- sub-product, table, collection, or distribution identity;
- source-native record or file identifier;
- source version, file vintage, model cycle, or release identifier;
- candidate source role;
- role justification or descriptor reference;
- product-specific caveat profile.

### Unknown product behavior

Unknown, unsupported, ambiguous, or version-drifted products must not fall through to a generic permissive parser. They should return an explicit unsupported or quarantine-safe outcome.

[Back to top](#top)

---

<a id="parsing-and-preservation-contract"></a>

## Parsing and preservation contract

Parsers transform source bytes into structured source material. They do not establish truth.

### Parser requirements

A parser should be:

- deterministic for identical bytes and parser profile;
- network-free;
- free of persistent writes;
- explicit about expected media type and product/version;
- strict enough to detect structural drift;
- conservative about coercion;
- able to preserve unknown fields or report their loss according to contract;
- able to produce bounded warnings and quarantine reasons;
- testable with synthetic or minimized fixtures;
- safe against hostile or malformed source-shaped input.

### Native field preservation

Preserve, where applicable:

- source-native identifiers;
- table, product, collection, station, model, platform, instrument, or sensor identity;
- units exactly as supplied;
- missing-value sentinels and null semantics;
- quality flags and confidence fields;
- geometry type, CRS, coordinate order, and native precision;
- observation, issue, valid, expiration, retrieval, file-vintage, and correction times;
- model run and forecast hour;
- station depth or measurement level;
- source narrative and caveat fields;
- provenance needed to replay the parse.

### Prohibited parser behavior

A parser must not silently:

- infer source truth from presence;
- fill missing values with plausible values;
- convert AOD to PM2.5;
- convert smoke density to concentration;
- treat a station as an area surface;
- convert detections into confirmed incidents;
- convert historical storm records into current warnings;
- merge observed, modeled, aggregate, administrative, candidate, or contextual roles;
- strip quality flags because they are inconvenient;
- collapse distinct time kinds into one timestamp;
- round coordinates or units without recording a transform;
- upgrade a quarantined record to admissible.

### Schema drift

Unexpected columns, missing required fields, changed enumerations, incompatible units, new archive layouts, or product-version changes should produce a drift signal and quarantine-safe result until reviewed.

[Back to top](#top)

---

<a id="source-admission-handoff-contract"></a>

## Source-admission handoff contract

This source root should return structured candidates to a governed runner or orchestration boundary. Persistent lifecycle writes should not be hidden inside parser functions.

### Proposed admission candidate families

| Candidate | Meaning | Allowed next action |
|---|---|---|
| RAW candidate | Source bytes and metadata were captured under an allowed source/product context. | Runner may persist to an explicit RAW target and emit an ingest receipt. |
| QUARANTINE candidate | Source bytes or parsed metadata require review because support is missing, uncertain, stale, malformed, or policy-sensitive. | Runner may persist to an explicit QUARANTINE target with a reason. |
| NO-CHANGE result | Conditional request or source manifest indicates no new source state. | Emit a bounded no-op/run receipt if the owning workflow requires it. |
| NO-DATA result | Source responded successfully with a product-valid no-data state. | Record without fabricating records. |
| RETRY-LATER result | Rate limit or transient source condition prevents completion. | Scheduler/orchestrator decides future retry; package does not self-schedule. |
| ERROR result | Integrity, transport, parser, configuration, or unexpected process failure. | Fail closed and retain safe diagnostics. |

These names are `PROPOSED` until a connector result contract or schema is accepted.

### Minimum candidate metadata

A candidate should carry references or safe values for:

- candidate ID;
- source descriptor reference;
- activation decision reference when available;
- source family and product key;
- source-native file or record identity;
- request fingerprint;
- approved endpoint/distribution key;
- retrieval time;
- source time kinds;
- HTTP/file metadata;
- media type and size;
- content digest;
- parser/adapter profile and version;
- source-role candidate;
- rights and sensitivity context refs;
- lifecycle target candidate;
- reasons and warnings;
- correction/supersession markers when available.

### Persistence rule

The preferred library boundary is:

```text
package returns candidate
  -> governed runner validates target and obligations
  -> runner writes RAW or QUARANTINE
  -> runner emits receipt
```

If package code is ever allowed to perform persistence directly, that behavior requires an explicit interface, supplied target, atomic-write semantics, receipt integration, tests, and review. It must never infer a repository path from current working directory or write to downstream lifecycle roots.

[Back to top](#top)

---

<a id="finite-outcome-and-reason-code-contract"></a>

## Finite outcome and reason-code contract

Connector outcomes must be finite, explicit, and distinct from policy or runtime-answer outcomes.

### Vocabulary boundary

Do not confuse package-local connector outcomes with canonical `PolicyDecision` outcomes such as `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` unless a policy gate actually produced a `PolicyDecision`.

A connector may report that a fetch or parse is ready, unchanged, empty, quarantined, retryable, or failed. A separate policy gate decides admissibility or downstream action under its own contract.

### Proposed outcome set

```text
READY_FOR_RAW
READY_FOR_QUARANTINE
NO_CHANGE
NO_DATA
RETRY_LATER
ERROR
```

This enum is `PROPOSED`; implementation must use an accepted schema or typed model before callers depend on it.

### Proposed reason-code families

| Family | Example codes |
|---|---|
| Configuration | `NOAA_CONFIG_MISSING`, `NOAA_PRODUCT_UNKNOWN`, `NOAA_LIVE_MODE_DISABLED` |
| Descriptor/activation | `NOAA_DESCRIPTOR_MISSING`, `NOAA_SOURCE_INACTIVE`, `NOAA_ROLE_UNRESOLVED` |
| Rights/sensitivity | `NOAA_RIGHTS_UNRESOLVED`, `NOAA_SENSITIVITY_REVIEW_REQUIRED`, `NOAA_LIFE_SAFETY_BOUNDARY` |
| Transport | `NOAA_TIMEOUT`, `NOAA_RATE_LIMITED`, `NOAA_REDIRECT_BLOCKED`, `NOAA_RESPONSE_TOO_LARGE` |
| Integrity | `NOAA_DIGEST_MISMATCH`, `NOAA_MEDIA_TYPE_MISMATCH`, `NOAA_ARCHIVE_UNSAFE` |
| Parsing | `NOAA_MALFORMED_PAYLOAD`, `NOAA_SCHEMA_DRIFT`, `NOAA_UNIT_UNSUPPORTED`, `NOAA_TIME_INVALID` |
| Product semantics | `NOAA_ROLE_COLLAPSE`, `NOAA_PRODUCT_VERSION_UNKNOWN`, `NOAA_CAVEAT_MISSING` |
| Lifecycle | `NOAA_TARGET_INVALID`, `NOAA_PERSISTENCE_FORBIDDEN`, `NOAA_RECEIPT_REQUIRED` |

Reason codes must not include secrets, raw authorization material, complete sensitive payloads, or unbounded source text.

[Back to top](#top)

---

<a id="provenance-identity-and-time"></a>

## Provenance, identity, and time

### Source interaction identity

Deterministic identity should be used where practical.

A proposed candidate identity basis is:

```text
candidate_id = digest(
  source_descriptor_ref
  + product_key
  + request_fingerprint
  + source_native_identity
  + retrieval_or_manifest_identity
  + content_digest
  + parser_profile
)
```

The exact canonicalization and digest profile remain `NEEDS VERIFICATION` against repository standards.

### Request fingerprint

A request fingerprint should include behaviorally relevant, non-secret values:

- approved endpoint/distribution key;
- method or file selection profile;
- canonical parameters;
- headers that affect representation, excluding secrets;
- product/profile version;
- requested time or spatial range;
- pagination or manifest selection state.

### Time kinds

Do not collapse materially distinct times.

| Time kind | Meaning |
|---|---|
| Observation time | When a measurement, detection, or event was observed. |
| Event time | When a documented event occurred or was reported to occur. |
| Issue time | When a forecast, warning, advisory, analysis, or product was issued. |
| Valid time | Period or instant for which a product applies. |
| Expiration time | When a product should no longer be treated as current context. |
| Model initialization time | Start cycle of a model run. |
| Forecast hour | Offset from model initialization. |
| File vintage | Source file edition, batch, or archive release identity. |
| Retrieval time | When KFM fetched or received the bytes. |
| Correction time | When the source corrected, replaced, or superseded material. |
| Release time | Downstream KFM release time; not connector-owned. |

### Corrections and supersession

A corrected NOAA file or record should not overwrite lineage silently. Candidate metadata should preserve prior identity, correction markers, source replacement semantics, and downstream invalidation hints where available.

[Back to top](#top)

---

<a id="rights-sensitivity-and-life-safety-boundaries"></a>

## Rights, sensitivity, and life-safety boundaries

### Rights

The package may carry rights and attribution references. It does not decide rights authority.

Live access or persistence should fail closed when required terms, redistribution limits, attribution, export restrictions, or review state are missing or unresolved.

### Sensitivity

NOAA material may include or imply:

- exact infrastructure locations;
- casualty or damage details;
- private-property impacts;
- emergency-response context;
- precise incident or hazard locations;
- sensitive operational metadata;
- source-side restrictions.

The connector must preserve sensitivity context and route unresolved material to QUARANTINE. It must not publish, redact, generalize, or downgrade sensitivity on its own.

### Life-safety boundary

The package must not generate:

- “take shelter” or evacuation instructions;
- KFM-issued warning severity;
- emergency countdowns;
- implied official alert status;
- personalized hazard advice;
- source-independent interpretations of whether an area is safe.

Any downstream public surface must direct users to official sources for current life-safety action.

### Generated language

Generated summaries, parser diagnostics, or AI-assisted labels are not evidence and must not become source fields without explicit provenance, review, and a suitable source role.

[Back to top](#top)

---

<a id="security-and-data-minimization"></a>

## Security and data minimization

### Threats to address

| Threat | Required defense |
|---|---|
| SSRF through configurable URLs | Descriptor-approved allowlist; block loopback, link-local, private networks, and non-HTTP schemes by default. |
| Secret leakage | Redact headers/query values; never serialize secrets into candidates, errors, receipts, fixtures, or logs. |
| Decompression bomb | Bound compressed and decompressed sizes, entries, and expansion ratio. |
| Archive path traversal | Reject absolute paths, `..`, symlinks, device files, and extraction outside a controlled directory. |
| Resource exhaustion | Bound bytes, records, geometry complexity, nesting depth, concurrency, retries, and parse time. |
| Content-type confusion | Validate headers, file signatures, expected product format, and archive contents. |
| HTML/error-page ingestion | Detect source error pages and refuse parsing as product data. |
| Unsafe deserialization | Avoid pickle and unsafe YAML/object loaders; use explicit parsers. |
| Log injection | Normalize or escape untrusted line breaks and control characters. |
| Namespace dependency confusion | Verify package name, registry behavior, lockfiles, and installation source before publishing/installing. |
| Payload persistence leakage | Keep temporary data controlled, cleaned, and excluded from commits; persist only through governed targets. |
| Parser ambiguity | Fail closed on unknown version, unit, role, or required field. |

### Data minimization

Retain only what is needed for:

- source replay;
- integrity verification;
- product identity;
- parsing and validation;
- rights and citation obligations;
- lifecycle admission;
- correction and rollback.

Do not duplicate bulk source payloads into logs, exception messages, Markdown, test snapshots, or receipts.

[Back to top](#top)

---

<a id="testing-and-validation"></a>

## Testing and validation

Connector-local tests belong under:

```text
connectors/noaa/tests/
```

The current test README is a draft contract. Test implementation and CI remain unproved.

### Default test posture

```text
network: disabled
credentials: not required
live downloads: not required
fixtures: synthetic, minimized, redacted, or explicitly approved
writes: no lifecycle or release stores
source side effects: forbidden
```

### Minimum test matrix

| Test family | Required cases |
|---|---|
| Import safety | Import package and submodules with network/filesystem/secret access blocked. |
| Package discovery | Clean editable and wheel installs include intended package only. |
| Namespace collision | Verify the intended `noaa` import resolves to this project in supported environments. |
| Configuration | Missing, unknown, malformed, and live-disabled profiles fail safely. |
| Descriptor gate | Missing/inactive descriptor blocks live access and admissible handoff. |
| Transport | Timeout, DNS failure, rate limit, redirect, oversized response, content-type mismatch, partial download. |
| Integrity | Digest match/mismatch, file-size mismatch, archive safety, conditional no-change. |
| Parsing | Valid, empty, malformed, truncated, version-drifted, unknown-field, missing-field, invalid-unit, invalid-time. |
| Product dispatch | Known product selects correct adapter; unknown product fails closed. |
| Source-role preservation | Product roles remain distinct; generic NOAA-wide role collapse fails. |
| Time preservation | Observation, issue, valid, expiration, retrieval, file vintage, correction, and model times remain distinct. |
| Product anti-collapse | Storm record≠alert; AOD≠PM2.5; density≠concentration; station≠area; detection≠confirmed fire. |
| Admission candidate | RAW and QUARANTINE candidates contain required metadata and safe reasons. |
| Persistence boundary | Package functions do not write lifecycle, proof, release, API, UI, tile, or alert outputs. |
| Security | SSRF, path traversal, decompression bomb, secret redaction, log injection, unsafe archive entries. |
| Determinism | Same bytes + same parser profile produce identical normalized output/digest. |
| Correction | Corrected source material preserves prior identity and supersession lineage. |

### Product-specific negative tests

- Storm Events record must not become current warning or measured inundation.
- NWS content must not become KFM-issued emergency instruction.
- HMS qualitative density must not become concentration or exposure.
- HRRR modeled fields must not lose run/forecast metadata.
- GOES AOD must not become PM2.5.
- VIIRS detection must not become confirmed incident or perimeter.
- USCRN station readings must not become area truth or lose depth/cadence/flags.
- Climate normals must not be treated as observations for a specific event time.

### Validation commands

The exact runner is `NEEDS VERIFICATION`. Do not claim a command is canonical until package metadata, repository tooling, or CI establishes it.

Illustrative only:

```bash
python -m pytest connectors/noaa/tests
```

A live-test suite, if approved, must be separate, skipped by default, descriptor-gated, rate-limited, and excluded from required offline CI unless repository governance explicitly says otherwise.

[Back to top](#top)

---

<a id="smallest-sound-implementation-sequence"></a>

## Smallest sound implementation sequence

Implement the package in reversible, reviewable slices.

### Phase 0 — reconcile documentation and package decision

1. Confirm owners.
2. Confirm the intended import namespace and collision posture.
3. Harden `pyproject.toml` enough to build an empty package deterministically.
4. Update the parent and child READMEs together when behavior changes.
5. Confirm the accepted source descriptor and source-admission contract homes.

**Stop if:** namespace, package discovery, source activation, or authority boundaries are unresolved.

### Phase 1 — import-safe shell

1. Keep `__init__.py` side-effect free.
2. Add package-local typed configuration and error/outcome types.
3. Add import-safety tests.
4. Build and inspect wheel contents.

**Stop if:** import triggers network, secrets, writes, global logging, or environment-dependent behavior.

### Phase 2 — fixture-first pilot

1. Select one NOAA product with an admitted or reviewable descriptor.
2. Create a synthetic/minimized product-shaped fixture.
3. Implement a deterministic parser only.
4. Preserve identity, time, units, flags, caveats, and source-role candidate.
5. Add valid and negative parser tests.

**Stop if:** the parser needs to infer missing truth, discard caveats, or collapse source roles.

### Phase 3 — admission candidate

1. Define or adopt the candidate model.
2. Add content digest and request/source metadata.
3. Return RAW or QUARANTINE candidates without persistent writes.
4. Add reason codes and deterministic replay tests.

**Stop if:** the package must invent lifecycle paths or bypass a governed runner.

### Phase 4 — bounded transport

1. Add a fake/in-memory transport interface.
2. Add an allowlisted live transport implementation.
3. Enforce timeouts, limits, redirect controls, retries, and secret redaction.
4. Test all failure paths offline.

**Stop if:** live access cannot be descriptor-gated, rate-limited, receipt-capable, or disabled quickly.

### Phase 5 — governed live dry run

1. Use an approved endpoint/distribution.
2. Run once under steward review.
3. Persist only to an explicit RAW or QUARANTINE target through an accepted runner.
4. Emit run/ingest receipt evidence.
5. Compare captured bytes with fixture and parser expectations.

**Stop if:** rights, source role, sensitivity, integrity, or correction handling changes unexpectedly.

### Phase 6 — product-by-product expansion

Add one product adapter at a time with:

- descriptor evidence;
- product doctrine link;
- fixture set;
- parser tests;
- transport tests;
- anti-collapse tests;
- admission-candidate tests;
- correction and rollback notes.

Do not activate a generic “all NOAA” path.

### Phase 7 — CI and operational maturity

1. Wire no-network tests into CI.
2. Add package build inspection.
3. Add dependency and security checks.
4. Add connector boundary guards.
5. Add optional governed live smoke checks only after review.
6. Document health, receipts, retry, disable, correction, and rollback operations.

[Back to top](#top)

---

<a id="definition-of-done"></a>

## Definition of done

This source root is implementation-ready only when all applicable items are satisfied.

### Governance and ownership

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [ ] Package namespace and placement are accepted.
- [ ] SourceDescriptor and activation-decision requirements are linked.
- [ ] Rights, sensitivity, validation, evidence, release, correction, and rollback boundaries remain separate.
- [ ] README claims match current code and test evidence.

### Packaging and imports

- [ ] `pyproject.toml` defines an accepted build backend and package discovery.
- [ ] Supported Python versions are explicit.
- [ ] Runtime and development dependencies are explicit and minimized.
- [ ] Clean wheel and editable installs work in supported environments.
- [ ] Wheel contents contain no raw payloads, secrets, private fixtures, or authority documents.
- [ ] Importing the package performs no network, secret, cache, scheduler, logging, or unsafe filesystem side effects.
- [ ] Namespace collision tests pass.

### Source admission

- [ ] Live access requires an allowed SourceDescriptor/activation context.
- [ ] Product identity and source-role candidate are explicit.
- [ ] Rights and sensitivity uncertainty routes to QUARANTINE.
- [ ] RAW/QUARANTINE candidates carry source identity, time, digest, parser profile, reasons, and provenance.
- [ ] Package code does not persist beyond an accepted, explicit handoff interface.
- [ ] Connectors do not publish, promote, close EvidenceBundles, or issue alerts.

### Product integrity

- [ ] Product-specific adapters preserve native identifiers and caveats.
- [ ] Observation, issue, valid, expiration, retrieval, file-vintage, correction, and model times remain distinct.
- [ ] Units, quality flags, geometry, precision, station/depth, model-run, detection, and uncertainty metadata are preserved.
- [ ] Unknown product/version/schema drift fails closed.
- [ ] NOAA-wide source-role collapse is prevented.

### Testing and operations

- [ ] Offline tests cover imports, configuration, transport, parsing, admission, security, role collapse, and persistence boundaries.
- [ ] Fixtures are synthetic, minimized, redacted, or explicitly approved.
- [ ] CI runs no-network tests and package-build checks.
- [ ] Optional live tests are isolated, skipped by default, and steward-approved.
- [ ] Run receipts, no-op outcomes, rate limits, and failures are observable without leaking secrets or payloads.
- [ ] Disable, correction, deprecation, and rollback paths are documented and tested.

[Back to top](#top)

---

<a id="review-burden-and-change-discipline"></a>

## Review burden and change discipline

### Review classes

| Change | Minimum review posture |
|---|---|
| README-only clarification | Connector/source steward review; verify no authority drift. |
| New module with no network | Connector maintainer plus tests. |
| New product parser | Connector, source, and owning-domain review; fixture and anti-collapse tests. |
| New live endpoint/distribution | Source, rights, sensitivity, security, and connector review. |
| New dependency | Maintainer and security/dependency review. |
| New persistent write behavior | Data/lifecycle, receipt, and rollback review. |
| New public import or entry point | Compatibility and consumer review. |
| Namespace/package move | ADR or migration decision, deprecation plan, tests, and rollback. |
| Life-safety-adjacent behavior | Hazards/policy review; default deny for KFM-issued guidance. |

### Smallest-change rule

Prefer:

- one product adapter per PR;
- fixture before live access;
- explicit typed interfaces before general frameworks;
- returned candidates before persistent writes;
- additive imports before removals;
- deprecation before breaking change;
- reversible configuration flags;
- bounded dependencies;
- documentation tied to code and tests.

Avoid broad rewrites that make source admission less inspectable or mix product roles.

[Back to top](#top)

---

<a id="open-verification-register"></a>

## Open verification register

| ID | Item | Status | Evidence needed |
|---|---|---:|---|
| NOAA-SRC-01 | Confirm accepted owners and CODEOWNERS coverage. | **NEEDS VERIFICATION** | CODEOWNERS and steward approval. |
| NOAA-SRC-02 | Confirm complete `connectors/noaa/src/` inventory. | **NEEDS VERIFICATION** | Recursive tree or mounted checkout. |
| NOAA-SRC-03 | Confirm top-level package namespace `noaa`. | **NEEDS VERIFICATION** | Namespace collision and packaging review. |
| NOAA-SRC-04 | Confirm build backend and package discovery. | **NEEDS VERIFICATION** | Hardened `pyproject.toml` and clean build. |
| NOAA-SRC-05 | Confirm supported Python versions. | **NEEDS VERIFICATION** | Repository runtime policy and CI matrix. |
| NOAA-SRC-06 | Confirm runtime and development dependencies. | **NEEDS VERIFICATION** | Lock/config files and dependency review. |
| NOAA-SRC-07 | Confirm package installability. | **UNKNOWN** | Wheel/editable install tests. |
| NOAA-SRC-08 | Confirm public import surface. | **UNKNOWN** | Implemented modules and API review. |
| NOAA-SRC-09 | Confirm active NOAA SourceDescriptor IDs. | **NEEDS VERIFICATION** | Source registry and activation decisions. |
| NOAA-SRC-10 | Confirm accepted source-role vocabulary. | **NEEDS VERIFICATION** | Source contract/schema/ADR. |
| NOAA-SRC-11 | Confirm source-admission candidate contract/schema. | **NEEDS VERIFICATION** | Contracts, schemas, validators, fixtures. |
| NOAA-SRC-12 | Confirm connector result/outcome vocabulary. | **NEEDS VERIFICATION** | Cross-connector contract decision. |
| NOAA-SRC-13 | Confirm reason-code registry location. | **NEEDS VERIFICATION** | Contract or registry evidence. |
| NOAA-SRC-14 | Confirm approved endpoint/distribution inventory. | **UNKNOWN** | Source descriptors and rights review. |
| NOAA-SRC-15 | Confirm network allowlist and SSRF policy. | **NEEDS VERIFICATION** | Security policy and transport tests. |
| NOAA-SRC-16 | Confirm timeout, retry, and rate-limit profiles. | **NEEDS VERIFICATION** | Product/source profiles and tests. |
| NOAA-SRC-17 | Confirm maximum payload/archive limits. | **NEEDS VERIFICATION** | Security/resource policy and tests. |
| NOAA-SRC-18 | Confirm rights and attribution bindings. | **NEEDS VERIFICATION** | Rights policy and descriptor refs. |
| NOAA-SRC-19 | Confirm sensitivity and life-safety bindings. | **NEEDS VERIFICATION** | Policy modules, tests, steward review. |
| NOAA-SRC-20 | Confirm product adapter inventory and owners. | **UNKNOWN** | Code tree, catalog, tests. |
| NOAA-SRC-21 | Confirm parser profiles and supported product versions. | **UNKNOWN** | Code, fixtures, tests, source docs. |
| NOAA-SRC-22 | Confirm fixture homes and approval status. | **NEEDS VERIFICATION** | Fixture manifests and steward review. |
| NOAA-SRC-23 | Confirm actual offline test runner. | **NEEDS VERIFICATION** | `pyproject.toml`, Makefile, CI, or test config. |
| NOAA-SRC-24 | Confirm CI wiring and boundary guards. | **UNKNOWN** | Workflow definitions and completed runs. |
| NOAA-SRC-25 | Confirm receipt emission and linkage. | **UNKNOWN** | Runner code, receipt artifacts, tests. |
| NOAA-SRC-26 | Confirm RAW/QUARANTINE persistence owner. | **NEEDS VERIFICATION** | Runner/orchestration contract. |
| NOAA-SRC-27 | Confirm deterministic canonicalization/digest profile. | **NEEDS VERIFICATION** | Standards, code, and golden tests. |
| NOAA-SRC-28 | Confirm correction and source-supersession handling. | **UNKNOWN** | Source-specific examples and tests. |
| NOAA-SRC-29 | Confirm disable/retire behavior for sources and products. | **UNKNOWN** | Activation workflow and operational runbook. |
| NOAA-SRC-30 | Confirm downstream import consumers. | **UNKNOWN** | Code search, dependency graph, builds. |
| NOAA-SRC-31 | Confirm package deprecation policy. | **NEEDS VERIFICATION** | Repository deprecation process and migration template. |
| NOAA-SRC-32 | Confirm rollback automation and drill evidence. | **UNKNOWN** | Runbook, tests, workflow logs, artifacts. |

Open items must not be converted into implementation facts through repetition in documentation.

[Back to top](#top)

---

<a id="rollback-correction-deprecation-and-supersession"></a>

## Rollback, correction, deprecation, and supersession

### Documentation rollback

To undo this documentation-only revision:

- revert the commit that introduced v0.2; or
- restore prior blob `9327e47383af287222b9d66dcc07a386a940f5c0`.

That rollback restores the previous source-root README but also restores its stale statement that the child package was only future/proposed.

### Implementation rollback principles

Future executable changes should preserve:

- a package-level disable switch for live behavior;
- product-level activation/disable controls;
- bounded dependency rollback;
- backward-compatible imports during deprecation where practical;
- candidate/receipt lineage sufficient to identify affected runs;
- no automatic deletion of prior source material;
- downstream invalidation or correction signals when parser behavior changes materially.

### Parser correction

A parser correction should:

1. identify affected product versions and captured payloads;
2. assign a new parser profile/version;
3. replay approved captured fixtures/payloads deterministically;
4. compare old and new candidates;
5. emit correction or reprocessing records through owning workflows;
6. preserve prior outputs and lineage;
7. avoid silently rewriting published claims;
8. trigger downstream correction/rollback review when material.

### Package deprecation

Before removing or renaming a module, package, public import, configuration field, outcome, or reason code:

- inventory consumers;
- announce deprecation in code and docs;
- provide replacement guidance;
- retain compatibility for an accepted period where practical;
- add tests for old and new paths;
- document the removal release;
- preserve a rollback target.

### Supersession note

This v0.2 README supersedes the v0.1 source-root documentation claim that `src/noaa/` and its package README were only proposed future paths. It does not supersede the child package README, family README, test README, source catalog, Directory Rules, source-admission ADR, contracts, schemas, policy, or release authority.

[Back to top](#top)

---

<details>
<summary><strong>Appendix A — illustrative package configuration</strong></summary>

The following shape is illustrative and is not a verified schema or implemented API.

```yaml
connector:
  source_descriptor_ref: source:noaa:PRODUCT_TBD
  product_key: PRODUCT_TBD
  network_mode: fixture_only
  endpoint_profile: ENDPOINT_PROFILE_TBD
  parser_profile: PARSER_PROFILE_TBD
transport:
  connect_timeout_seconds: 5
  read_timeout_seconds: 30
  total_timeout_seconds: 60
  max_attempts: 2
  max_response_bytes: 52428800
  max_decompressed_bytes: 209715200
output:
  mode: return_candidate
  allowed_targets:
    - RAW
    - QUARANTINE
security:
  allowed_hosts: []
  redact_headers:
    - authorization
    - cookie
```

</details>

<details>
<summary><strong>Appendix B — illustrative admission candidate</strong></summary>

The following shape is illustrative and is not a verified schema or implemented API.

```json
{
  "candidate_id": "noaa:candidate:EXAMPLE",
  "outcome": "READY_FOR_QUARANTINE",
  "source_descriptor_ref": "source:noaa:PRODUCT_TBD",
  "source_family": "noaa",
  "product_key": "PRODUCT_TBD",
  "source_native_id": "SOURCE_ID_TBD",
  "source_role_candidate": "ROLE_TBD",
  "request_fingerprint": "sha256:REQUEST_TBD",
  "retrieved_at": "2026-07-15T00:00:00Z",
  "content": {
    "media_type": "application/octet-stream",
    "size_bytes": 0,
    "digest": "sha256:CONTENT_TBD"
  },
  "parser": {
    "profile": "PARSER_PROFILE_TBD",
    "version": "VERSION_TBD"
  },
  "time_context": {
    "observed_at": null,
    "issued_at": null,
    "valid_from": null,
    "valid_to": null,
    "file_vintage": null
  },
  "reasons": ["NOAA_DESCRIPTOR_MISSING"],
  "warnings": [],
  "target_candidate": "QUARANTINE"
}
```

</details>

<details>
<summary><strong>Appendix C — no-loss preservation note</strong></summary>

This revision preserves the v0.1 README’s strongest material:

- source-admission-only scope;
- RAW/QUARANTINE boundary;
- import safety;
- no secrets;
- NOAA multi-role posture;
- product-specific field and caveat preservation;
- no life-safety authority;
- no direct publication;
- test relationship;
- definition of done;
- verification backlog.

It corrects one material drift: the child package and package README are no longer merely proposed paths. They exist, but remain an empty package shell with unproved implementation depth.

</details>

---

## Status summary

`connectors/noaa/src/` is a confirmed source-code root containing a confirmed `noaa/` package shell and package boundary README. It remains **documentation-first and implementation-unproved**. The next sound step is not broad NOAA client development; it is package metadata hardening, namespace verification, import-safety tests, an admitted product descriptor, and one fixture-first product adapter that returns governed RAW or QUARANTINE candidates without publishing or issuing alerts.

<p align="right"><a href="#top">Back to top</a></p>
