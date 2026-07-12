<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-inaturalist-src-inaturalist-readme
title: connectors/inaturalist/src/inaturalist/ — iNaturalist Connector Python Package
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Connector steward · Source steward · Python/package steward · Test steward · Fauna steward · Flora steward · Biodiversity/taxonomy steward · Rights reviewer · Sensitivity/geoprivacy reviewer · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-07-12
policy_label: public-doctrine; package-contract; source-admission-only; import-side-effect-free; no-network-by-default; descriptor-and-activation-gated; product-explicit; rights-gated; geoprivacy-preserving; sensitivity-fail-closed; raw-quarantine-receipts-only; no-publication
path: connectors/inaturalist/src/inaturalist/README.md
truth_posture: CONFIRMED package scaffold and inspected files / PROPOSED package API, module plan, protocols, and implementation sequence / CONFLICTED connector-local descriptor and adjacent documentation / UNKNOWN installability, runtime behavior, activation, tests, and live-source behavior
related:
  - ../../README.md
  - ../README.md
  - ../../pyproject.toml
  - ../../observations/README.md
  - ../../tests/README.md
  - ./__init__.py
  - ./fetch.py
  - ./admit.py
  - ./descriptor.yaml
  - ../../../../connectors/README.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../docs/sources/catalog/inaturalist/README.md
  - ../../../../docs/sources/catalog/inaturalist/research-grade-observations.md
  - ../../../../docs/sources/catalog/inaturalist.md
  - ../../../../docs/domains/fauna/CANONICAL_PATHS.md
  - ../../../../contracts/domains/fauna/occurrence_evidence.md
  - ../../../../schemas/contracts/v1/domains/fauna/occurrence_evidence.schema.json
  - ../../../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../../../schemas/contracts/v1/sources/source_descriptor.schema.json
  - ../../../../data/registry/sources/
  - ../../../../data/registry/fauna/sources/inaturalist.yaml
  - ../../../../data/raw/fauna/inaturalist/README.md
  - ../../../../data/receipts/
  - ../../../../data/proofs/
  - ../../../../policy/rights/
  - ../../../../policy/sensitivity/
  - ../../../../release/
tags: [kfm, connectors, inaturalist, python-package, source-admission, observations, research-grade, rights, taxonomy, geoprivacy, sensitivity, replay, raw, quarantine, receipts, no-network, fail-closed, governance]
notes:
  - "At inspected base commit 2ef3cf2c21ee2384a51d8ca76cdec302d825770c, direct inspection verified this README, an empty __init__.py, one-line greenfield placeholder fetch.py and admit.py modules, and an unresolved connector-local descriptor.yaml."
  - "The parent pyproject.toml reserves distribution name kfm-connector-inaturalist at version 0.0.0 but declares no build backend, dependencies, package discovery, or verified install/import command."
  - "Direct probes for client.py, models.py, parse.py, rights.py, geoprivacy.py, validate.py, and handoff.py returned Not Found. This is bounded path evidence, not proof that no differently named code exists elsewhere."
  - "The connector-local descriptor.yaml is not SourceDescriptor authority. Its role and rights are TBD, and sensitivity_floor: public conflicts with the source profile's fail-closed posture for unknown sensitivity."
  - "The repository-present observation product README defines the current promotion-track product as research-grade plus normalized Creative Commons rights plus controlled-taxonomy resolution; non-research-grade routing remains unresolved."
  - "This revision defines a safe package contract only. It does not create executable modules, activate live access, choose an endpoint, validate source terms, or emit source data."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# iNaturalist Connector Python Package

> Implementation contract for the source-first Python package namespace under `connectors/inaturalist/src/inaturalist/`. The package may help retrieve, parse, preserve, validate, and hand off approved iNaturalist source material; it must not become source authority, policy authority, occurrence truth, release authority, or a public client path.

<p>
  <img alt="Status: package contract draft" src="https://img.shields.io/badge/status-package__contract__draft-yellow">
  <img alt="Implementation: placeholder scaffold" src="https://img.shields.io/badge/implementation-placeholder__scaffold-lightgrey">
  <img alt="Import: side effect free required" src="https://img.shields.io/badge/import-side__effect__free__required-green">
  <img alt="Network: explicit activation only" src="https://img.shields.io/badge/network-explicit__activation__only-critical">
  <img alt="Product routing: explicit" src="https://img.shields.io/badge/product__routing-explicit-blue">
  <img alt="Sensitivity: fail closed" src="https://img.shields.io/badge/sensitivity-fail__closed-critical">
  <img alt="Lifecycle: RAW quarantine receipts" src="https://img.shields.io/badge/lifecycle-RAW%20%7C%20QUARANTINE%20%7C%20receipts-orange">
  <img alt="Publication: forbidden" src="https://img.shields.io/badge/publication-forbidden-critical">
</p>

`connectors/inaturalist/src/inaturalist/`

> [!IMPORTANT]
> **Inspected state:** at base commit `2ef3cf2c21ee2384a51d8ca76cdec302d825770c`, `__init__.py` was empty; `fetch.py` and `admit.py` each contained only a greenfield placeholder comment; `descriptor.yaml` was unresolved; and the parent project metadata was `kfm-connector-inaturalist` version `0.0.0` without a verified build or install configuration. This README defines the intended boundary. It is not evidence that the package runs.

> [!CAUTION]
> **Never load `descriptor.yaml` as activation authority.** Its current `role: TBD`, `rights: TBD`, and `sensitivity_floor: public` are unsafe defaults. The accepted SourceDescriptor and SourceActivationDecision must come from governed registry and activation surfaces supplied explicitly by the caller. Missing or conflicting authority fails closed.

> [!WARNING]
> **Importing this package must do nothing observable.** No network call, filesystem write, environment-secret read, descriptor discovery, clock read, UUID generation, logging setup, thread/process start, cache mutation, or source activation may happen at import time.

> [!WARNING]
> **Source family is not product.** Every request and admission decision must carry an explicit product identity. The current promotion-track observation product is research-grade plus recognized normalized Creative Commons rights plus controlled-taxonomy resolution. The package must not silently route casual or otherwise non-research-grade observations through that product.

**Quick jumps:** [Purpose](#purpose) · [Current repository state](#current-repository-state) · [Package authority boundary](#package-authority-boundary) · [Design rules](#design-rules) · [Import and public API contract](#import-and-public-api-contract) · [Internal data and protocol model](#internal-data-and-protocol-model) · [Module plan](#module-plan) · [Fetch contract](#fetch-contract) · [Parse and preservation contract](#parse-and-preservation-contract) · [Admission contract](#admission-contract) · [Rights taxonomy geoprivacy and sensitivity](#rights-taxonomy-geoprivacy-and-sensitivity) · [I/O receipt and dependency boundary](#io-receipt-and-dependency-boundary) · [Finite outcomes and errors](#finite-outcomes-and-errors) · [Logging and sensitive-data discipline](#logging-and-sensitive-data-discipline) · [Testing contract](#testing-contract) · [Implementation sequence](#implementation-sequence) · [Definition of done](#definition-of-done) · [Verification backlog](#verification-backlog) · [Review and rollback](#review-and-rollback)

---

## Purpose

This README makes the package boundary concrete enough for small, reversible implementation PRs while keeping unverified behavior visibly unverified.

The package may eventually:

- construct deterministic, bounded request specifications from explicit product and descriptor inputs;
- execute fixture-backed or explicitly activated source requests through an injected transport;
- capture response identity and integrity before parsing;
- parse source-native observation records without discarding source identity, quality, rights, taxonomy, time, geometry, uncertainty, or geoprivacy;
- perform connector-local structural checks and assemble inputs for governed rights, taxonomy, sensitivity, and admission decisions;
- return finite, typed outcomes for admit, quarantine, no-op, rate-limit, abstain, deny, and error;
- build caller-consumable RAW, QUARANTINE, and process-memory receipt candidates;
- support deterministic replay, correction, withdrawal, and no-op detection;
- remain shared by Fauna and Flora without creating domain-specific connector duplicates.

The package does **not**:

- own iNaturalist source-family or product doctrine;
- create, approve, discover, or mutate SourceDescriptor or SourceActivationDecision authority records;
- choose current API endpoints, credentials, rate limits, query scope, cadence, or terms from memory;
- decide legal status, conservation status, taxonomic truth, species presence, range, habitat, public precision, or release eligibility;
- deobscure or infer private coordinates;
- own schemas, policy bundles, EvidenceBundles, proofs, catalog/triplet records, RedactionReceipts, release manifests, corrections, rollback cards, public APIs, maps, UIs, search indexes, graphs, or AI answers;
- write WORK, PROCESSED, CATALOG, TRIPLET, PUBLISHED, proof, registry, or release stores;
- make live network access the default path.

[Back to top ↑](#top)

---

## Current repository state

The snapshot below is bounded to the pinned base commit and direct paths inspected in this session.

```text
connectors/inaturalist/
├── README.md
├── pyproject.toml                         # project name + version 0.0.0 only
├── observations/
│   └── README.md                          # product contract; research-grade default
├── src/
│   ├── README.md
│   └── inaturalist/
│       ├── README.md                      # this package contract
│       ├── __init__.py                    # empty
│       ├── fetch.py                       # one-line greenfield placeholder
│       ├── admit.py                       # one-line greenfield placeholder
│       └── descriptor.yaml                # unresolved local placeholder; not authority
└── tests/
    └── README.md                          # test contract; executable tests unverified
```

| Item | Observed state | Safe conclusion |
|---|---|---|
| `README.md` | v0.1 before this revision; blob `93b4412cf06effe1276a71357748ad34d2657a91`. | The package documentation path exists. |
| `__init__.py` | Empty blob `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`. | A filesystem package namespace is reserved; no public API or import behavior is implemented. |
| `fetch.py` | One-line placeholder. | A fetch responsibility name is reserved; no transport or request behavior is implemented. |
| `admit.py` | One-line placeholder. | An admission responsibility name is reserved; no admission behavior is implemented. |
| `descriptor.yaml` | `name: inaturalist`, `role: TBD`, `rights: TBD`, `sensitivity_floor: public`. | An unsafe local placeholder exists; it is not registry, policy, activation, or default configuration authority. |
| Parent `pyproject.toml` | Distribution name `kfm-connector-inaturalist`; version `0.0.0`; no verified build-system, dependency, or package-discovery configuration. | Distribution identity is reserved; installability, dependency closure, supported Python version, and import command remain unknown. |
| `client.py`, `models.py`, `parse.py` | Not found at direct paths. | The v0.1 proposed modules are not implemented under those names. |
| `rights.py`, `geoprivacy.py`, `validate.py`, `handoff.py` | Not found at direct paths. | Those v0.1 proposed helpers are not implemented under those names. |
| `connectors/inaturalist/tests/README.md` | Documentation exists. | Test expectations exist; executable tests and passing status remain unverified. |
| Search for `test_inaturalist` | No result surfaced from the indexed repository search. | No test with that name was observed at the indexed ref; differently named or unindexed tests remain possible. |
| Current observation product README | Repository-present v0.2 product contract. | Shared package code should support explicit product routing; it does not prove a product module or runtime exists. |
| Live request, source payload, accepted descriptor, activation decision, source-run receipt, package install, import test, parser output, CI proof | Not verified. | Do not infer operation or readiness. |

The v0.1 package README was introduced by commit `45d52f6403180fcbb6a2366b633cd804ce76558b`, expanding a one-line blank placeholder. That history does not justify describing the current file as blank or newly created.

Adjacent documentation is not fully synchronized:

- the parent and source-root READMEs still show incomplete child inventories;
- parent/source/test package language still excludes receipt stores in places, while `connectors/README.md`, Directory Rules, and the observation product README allow bounded process-memory receipt handoffs;
- registry and SourceDescriptor schema paths remain conflicted;
- these are recorded as drift and are not silently rewritten by this package-only change.

[Back to top ↑](#top)

---

## Package authority boundary

```text
PACKAGE MAY:
  define pure types, protocols, constants, reason codes, and deterministic helpers
  normalize explicit request specifications
  invoke an injected transport only after explicit activation
  parse approved source-shaped responses or fixtures
  preserve source-native identity, grade, rights, taxonomy, time, geometry, and geoprivacy
  perform connector-local shape and completeness checks
  combine caller-supplied descriptor, activation, rights, taxonomy, and sensitivity decisions
  return finite outcomes
  build RAW / QUARANTINE / process-memory receipt candidates
  support replay, correction, withdrawal, and no-op detection

PACKAGE MUST NOT:
  auto-discover or approve descriptors
  load connector-local descriptor.yaml as authority
  invent source roles, product identity, rights, taxonomy, sensitivity, or public precision
  read secrets or make network calls at import time
  deobscure or infer exact coordinates
  silently upgrade casual/non-research-grade records into the research-grade product
  write lifecycle destinations chosen internally
  write WORK / PROCESSED / CATALOG / TRIPLET / PUBLISHED / proof / registry / release
  expose public API, map, tile, report, graph, search, vector-index, or AI payloads
  treat receipts as EvidenceBundle, proof, catalog, or publication closure
```

### Inputs owned elsewhere

The caller or a governed adapter must supply, as applicable:

- accepted SourceDescriptor reference and validated descriptor data;
- SourceActivationDecision and permitted product/scope;
- explicit product identifier and version;
- rights-normalization map or rights decision;
- taxonomy crosswalk result and authority/version references;
- sensitivity/geoprivacy policy result and review requirements;
- bounded query specification;
- network-enabled flag, transport, timeout, retry, and page limits;
- clock, identifier, and digest dependencies where nondeterminism would otherwise enter;
- caller-selected RAW, QUARANTINE, and receipt interfaces;
- correction, withdrawal, and prior-run lineage references.

The package may validate that required inputs exist and are internally consistent. It cannot manufacture their authority.

[Back to top ↑](#top)

---

## Design rules

1. **Explicit dependencies.** Network transport, clock, identifier generation, filesystem/storage, retry policy, and logging sink are passed in; they are not hidden globals.
2. **Pure core, thin adapters.** Request canonicalization, parsing, classification, validation, admission assembly, and receipt construction should be deterministic pure functions where practical.
3. **No import side effects.** Importing any package module performs no I/O, configuration discovery, environment access, logging setup, or activation.
4. **Fail closed.** Missing descriptor, activation, product, rights, taxonomy, geoprivacy, sensitivity, identity, time, or integrity support cannot become an admit result.
5. **Preserve before normalize.** Source-native values and their provenance remain available alongside normalized forms; normalization never erases the original.
6. **Product explicitness.** Source-family identity and product identity travel separately through every request, parsed record, decision, handoff, and receipt.
7. **Deterministic replay.** Normalized request digest, page/cursor state, source record identity/version, response digest, connector version, and outcome are preserved.
8. **Finite behavior.** Expected source and governance conditions return structured outcomes and reason codes instead of hanging, retrying forever, or falling back to allow.
9. **Safe observability.** Logs and metrics use an allowlist and never expose secrets, private payloads, exact sensitive coordinates, observer-private data, or media location metadata.
10. **Authority separation.** Package code can implement mechanics against accepted contracts; it cannot become a parallel contract, schema, descriptor, policy, proof, catalog, or release home.
11. **Small public surface.** `__init__.py` exports only stable, reviewed entry points and types. Internal helpers remain internal.
12. **Reversible increments.** Each implementation PR introduces one coherent capability, fixtures, negative tests, documentation, and a rollback path.

[Back to top ↑](#top)

---

## Import and public API contract

### Current state

`__init__.py` is empty. Keep it empty until a tested, intentionally stable public surface exists. Do not use it to instantiate a client, read configuration, load descriptors, register plugins, or trigger source access.

### Proposed stable surface

Names below are **PROPOSED**, not implemented:

```python
from inaturalist import (
    ConnectorOutcome,
    OutcomeCode,
    build_request,
    parse_page,
    evaluate_admission,
)
```

A future public surface should:

- export types and pure orchestration functions, not mutable global clients;
- avoid re-exporting third-party HTTP, schema, policy, or storage types;
- keep transport and storage interfaces injectable;
- use keyword-only configuration for risk-bearing options;
- require explicit product, descriptor, and activation inputs;
- return structured results rather than raw response objects;
- remain usable with fake transports and in-memory handoff sinks;
- document compatibility and versioning before the distribution leaves `0.0.0`.

A public function must not silently read environment variables, current time, local files, package-relative descriptors, default endpoints, or credentials. Convenience constructors may be added only when they remain explicit and testable.

[Back to top ↑](#top)

---

## Internal data and protocol model

These names are **PROPOSED semantic interfaces**, not schemas or implemented classes.

| Interface | Minimum semantic responsibility | Must not imply |
|---|---|---|
| `ObservationQuerySpec` | Product ID/version; geography, taxon, date, sort, page/cursor, and limit scope; normalized representation; query digest. | Endpoint activation or rights approval. |
| `FetchContext` | Descriptor ref, activation ref, run ID, connector version, network-enabled flag, timeout/retry/page bounds, retrieval/snapshot time. | Permission beyond the supplied decisions. |
| `PreparedRequest` | Redacted method/endpoint identity, safe headers, parameters, page state, request digest. | Credential disclosure or source truth. |
| `FetchedPage` | Status, safe header subset, page/cursor state, response bytes/reference, response digest, retrieval time, transport outcome. | Parsed or admitted content. |
| `ParsedObservation` | Source record ID/version, product, quality grade/flags, source taxonomy, event/source times, geometry/support, uncertainty, geoprivacy, rights/attribution, media references. | Public-safe occurrence, canonical taxonomy, or policy approval. |
| `AdmissionContext` | Product rule ref plus caller-supplied descriptor, activation, rights, taxonomy, sensitivity, review, and target-interface decisions. | Package-owned policy. |
| `AdmissionDecision` | Finite outcome, stable reason codes, record references, warnings, and required review/remediation. | Promotion, release, or proof closure. |
| `HandoffCandidate` | Immutable RAW or QUARANTINE candidate with source identity, digests, lineage, and target class. | Permission to choose or bypass lifecycle paths. |
| `ConnectorReceiptCandidate` | Process-memory facts about request, response, parser, decision, counts, digests, duration, and outcome. | EvidenceBundle, ProofPack, ReleaseManifest, or merge approval. |

### Injectable protocols

A future implementation should prefer small protocols over hidden concrete dependencies:

```python
class Transport:
    def send(self, request: PreparedRequest) -> FetchedPage: ...

class Clock:
    def now(self) -> str: ...

class HandoffSink:
    def write_raw(self, candidate: HandoffCandidate) -> str: ...
    def write_quarantine(self, candidate: HandoffCandidate) -> str: ...
    def write_receipt(self, candidate: ConnectorReceiptCandidate) -> str: ...
```

The signatures are illustrative. Accepted contracts, typing conventions, async/sync posture, and storage interfaces remain **NEEDS VERIFICATION**.

[Back to top ↑](#top)

---

## Module plan

The module plan separates verified current files from proposed future files.

### Current files

| File | Intended responsibility after review | Current status |
|---|---|---:|
| `__init__.py` | Deliberate stable exports only. | **CONFIRMED empty** |
| `fetch.py` | Explicit, bounded request execution through an injected transport; no parsing, policy, handoff, or import-time I/O. | **CONFIRMED placeholder / PROPOSED contract** |
| `admit.py` | Pure assembly of finite admission outcomes from parsed records and caller-supplied governance decisions; no network or storage. | **CONFIRMED placeholder / PROPOSED contract** |
| `descriptor.yaml` | No runtime role. Remove, migrate, or formally classify in a separate governed change. | **CONFIRMED unsafe placeholder / CONFLICTED** |
| `README.md` | Package responsibility, API, dependency, test, security, implementation, and rollback contract. | **This revision** |

### Minimal first implementation set

| Proposed file | Narrow responsibility | Dependency rule |
|---|---|---|
| `models.py` | Frozen/immutable internal DTOs and enums for request, page, parsed record, outcome, handoff, and receipt candidates. | Imports no transport, storage, policy engine, or app code. |
| `errors.py` | Stable internal exception and reason-code vocabulary. | Expected conditions still return finite outcomes. |
| `query.py` | Normalize explicit query/product scope and compute deterministic request digest. | Excludes secrets and nondeterministic fields from the digest. |
| `parse.py` | Convert approved fixture/source pages into source-preserving `ParsedObservation` values. | No network, storage, policy, or public-geometry decisions. |
| `validate.py` | Connector-local shape, bounds, completeness, and consistency checks. | Does not replace JSON Schema or policy authority. |
| `receipts.py` | Build process-memory receipt candidates from explicit inputs and outcomes. | No proof, catalog, release, or human-review authority. |
| `handoff.py` | Build or write through caller-supplied RAW/QUARANTINE/receipt interfaces. | Never chooses default lifecycle destinations. |

### Later modules only after contract closure

| Candidate | Why deferred |
|---|---|
| `client.py` or `transport.py` | Live-source behavior, dependency choice, sync/async posture, endpoint, auth, timeout, retry, and rate-limit semantics are not ratified. |
| `rights.py` | Mechanical normalization may be useful, but accepted rights vocabulary and per-observation/per-media behavior require rights review. |
| `taxonomy.py` | Source taxonomy preservation is required, but crosswalk authority, version pinning, and ITIS/GBIF disagreement remain unresolved. |
| `geoprivacy.py` | Preservation helpers are useful, but KFM sensitivity and public-precision decisions must remain policy-owned. |
| `replay.py` | Replay storage/reference contracts, deletion/withdrawal semantics, and no-op identity need closure. |
| `products/observations.py` or another product package | Product-module layout is not yet ratified. The repository-present observations directory is documentation-only. |

Do not add every proposed module at once. A broad empty-module scaffold obscures implementation maturity and creates false API stability.

[Back to top ↑](#top)

---

## Fetch contract

`fetch.py` is reserved for source interaction mechanics, not admission policy.

A future fetch entry point must require:

- explicit SourceDescriptor and activation references supplied by the caller;
- explicit source-family and product identity;
- a fully bounded `ObservationQuerySpec`;
- `network_enabled=True` for live access, with the default remaining false;
- an injected transport;
- bounded timeout, retry count, total page count, records per page, and total-record limits;
- caller-provided clock/run context;
- safe credential reference or already-configured transport without exposing secret values;
- caller-defined capture/reference and receipt behavior.

Required behavior:

1. Canonicalize and hash the safe request specification before sending.
2. Validate descriptor, activation, product, and scope presence before transport use.
3. Refuse live access when the network flag is absent or false.
4. Execute through the injected transport only.
5. Capture safe response status, page/cursor state, retrieval time, and digest before parsing.
6. Treat redirects, forbidden/not-found states, malformed bodies, duplicate pages, cursor loops, partial pages, timeout, rate limit, and source outage as finite outcomes.
7. Bound retries and preserve retry/rate-limit evidence; never retry indefinitely.
8. Keep credentials, authorization headers, cookies, private parameters, and raw payload excerpts out of logs and errors.
9. Do not cache or mirror bytes unless an explicit rights/custody decision and caller-owned storage interface permit it.
10. Return fetched-page values or a structured fetch outcome; do not perform admission or publication.

No endpoint, API version, auth mechanism, rate-limit value, or current source behavior is defined here.

[Back to top ↑](#top)

---

## Parse and preservation contract

Parsing occurs after source-response identity and integrity are recorded.

A parser must preserve, when present:

- source family, product, native observation ID, stable source URL, and record version/modification marker;
- source quality grade and quality flags, including captive/cultivated or disputed states;
- source taxon ID, names, rank, identifications, and source taxonomy context;
- observed/event time, source-created time, source-updated time, retrieval time, and snapshot time as distinct concepts;
- source geometry/support, positional accuracy/uncertainty, place support, and original geoprivacy state;
- observation-level license, normalized rights token if mechanically available, attribution fields, and rights holder;
- media-reference IDs and media-specific rights fields separately from observation rights;
- source deletion/withdrawal markers where represented;
- page/cursor, response digest, request digest, connector version, and parser version;
- unknown, missing, conflicting, and unsupported values without silently inventing replacements.

A parser must not:

- infer research-grade from media content;
- upgrade a casual record;
- resolve taxonomy silently;
- infer precise coordinates from text, photos, timestamps, nearby records, user history, or external joins;
- replace obscured/private geometry with a centroid presented as exact;
- flatten source, observed, retrieval, release, and correction times;
- treat missing rights as permissive;
- treat parse success as admission;
- emit public occurrence or public-safe geometry.

[Back to top ↑](#top)

---

## Admission contract

`admit.py` should be pure orchestration over explicit evidence and caller-supplied decisions.

### Required inputs

- parsed source records and their request/response lineage;
- explicit source-family and product identity;
- accepted descriptor and activation references;
- current product-rule reference;
- rights normalization/decision result;
- taxonomy resolution result;
- source geoprivacy state and KFM sensitivity decision;
- review requirement and disposition;
- caller-selected handoff interfaces or a request to return candidates only.

### Current promotion-track observation product

A record is not eligible for `ADMIT_RAW` under the current product unless all required gates resolve, including:

- upstream quality grade is research-grade;
- observation rights normalize to a recognized Creative Commons variant;
- required attribution is available and permitted;
- controlled-taxonomy resolution succeeds under an accepted crosswalk;
- source geoprivacy is preserved;
- KFM sensitivity and RAW-admission posture are known and allowed;
- required identity, time, geometry/support, integrity, source, and product fields are present;
- no conflicting quality, captive/cultivated, rights, taxonomy, geometry, or review condition remains unresolved.

Casual/non-research-grade records are not silently discarded or upgraded. They return a candidate/quarantine disposition unless a separate accepted product explicitly handles them.

### Decision behavior

Admission assembly must:

- preserve every input decision and reference rather than reducing them to one Boolean;
- use stable, machine-readable reason codes;
- distinguish record-level and batch-level outcomes;
- preserve mixed batches without silently dropping failed records;
- return `QUARANTINE`, `ABSTAIN`, `DENY`, or `ERROR` when a required gate is absent, conflicting, or failed;
- produce no public-safe geometry, release decision, EvidenceBundle, proof, catalog row, or public claim;
- avoid filesystem writes unless an explicit handoff sink is invoked by caller-owned orchestration;
- make repeated identical inputs deterministic where practical.

[Back to top ↑](#top)

---

## Rights taxonomy geoprivacy and sensitivity

### Rights

- Preserve original observation license and normalized token separately.
- Preserve media rights separately from observation rights.
- Treat missing, unrecognized, conflicting, all-rights-reserved, or revoked rights as quarantine or deny under caller-supplied policy.
- Do not infer source-wide permission from one record.
- Do not expose unnecessary observer data in logs, receipts, fixtures, or public artifacts.
- Mechanical token normalization is implementation; reuse permission is policy/review.
- A license change is a source-state change requiring downstream re-evaluation, correction, or withdrawal.

### Taxonomy

- Preserve source taxon identity and identification context before crosswalk.
- Accept crosswalk results and authority/version references from a governed taxonomy surface.
- Do not silently choose between conflicting authorities.
- Keep observation identity stable even when taxonomy changes.
- Return unresolved taxonomy explicitly; the current product fails closed.
- Do not encode legal or conservation status as a consequence of taxonomic resolution.

### Geoprivacy

- Preserve open, obscured, private, generalized/place-only, missing, invalid, and changed states distinctly.
- Never deobscure, back-fill, triangulate, or infer exact location.
- Never place exact restricted coordinates in exceptions, logs, fixtures, diffs, screenshots, or receipt prose.
- Upstream geoprivacy is evidence, not KFM release approval.
- The package may classify source state mechanically; final public precision remains downstream.

### Sensitivity

- Require a caller-supplied KFM sensitivity decision or fail closed.
- Treat unknown sensitivity as restricted/needs review rather than public.
- Preserve triggers such as rare taxa, sensitive sites, private land, cultural or archaeological joins, infrastructure joins, media location metadata, and re-identification risk.
- Do not implement taxon/site policy tables inside the package.
- Do not emit `RedactionReceipt` or generalized public geometry; downstream governed transforms own those artifacts.

[Back to top ↑](#top)

---

## I/O receipt and dependency boundary

### Allowed handoff support

```text
MAY RETURN OR WRITE THROUGH EXPLICIT CALLER-SUPPLIED INTERFACES:
  data/raw/<domain>/<source_id>/<run_id>/
  data/quarantine/<domain>/<reason>/<run_id>/
  data/receipts/<run_id>/

MUST NOT OWN OR SELECT:
  data/work/
  data/processed/
  data/catalog/
  data/triplets/
  data/published/
  data/proofs/ as closure authority
  data/registry/
  release/
  apps/ public API or UI behavior
```

The safest default is candidate construction with no write. A write-capable adapter may be introduced only after target contracts, idempotency, permissions, rollback, tests, and caller ownership are verified.

### Receipt boundary

A connector receipt candidate may record:

- run, source, product, descriptor, activation, connector, and parser identity;
- normalized request digest and safe scope summary;
- page/cursor and response digest;
- retrieval time, durations, counts, retries, rate-limit state, and source status;
- parser/validator versions;
- per-record and batch outcomes and reason codes;
- RAW/QUARANTINE references returned by the caller-owned sink;
- prior-run, correction, withdrawal, or no-op lineage.

It is process memory. It is not an EvidenceBundle, ProofPack, catalog closure, PromotionDecision, ReleaseManifest, human review, or public citation.

### Dependency direction

```text
stdlib / accepted shared low-level libraries
        ↓
pure models + query + parse + validate + decision + receipt builders
        ↓
injected transport / storage / clock adapters
        ↓
connector orchestration outside import time
        ↓
RAW / QUARANTINE / receipt handoff

FORBIDDEN DEPENDENCY DIRECTION:
apps or public UI → connector internals for truth
connector package → release/catalog/proof authority
connector package → embedded policy or registry authority
```

Package dependency versions, Python version, HTTP library, sync/async model, and shared-library choices remain **NEEDS VERIFICATION**.

[Back to top ↑](#top)

---

## Finite outcomes and errors

The package should converge on the following **PROPOSED** outcome vocabulary unless an accepted contract defines another one:

| Outcome | Meaning |
|---|---|
| `ADMIT_RAW` | Required source, product, rights, taxonomy, sensitivity, integrity, and review gates permit bounded RAW handoff. |
| `QUARANTINE` | Material may be retained for review/remediation but is not eligible for promotion-track use. |
| `NO_OP` | The accepted source version/content/request result is unchanged and no new RAW material is needed. |
| `RATE_LIMITED` | Source throttled the request; retry evidence and bounds remain visible. |
| `ABSTAIN` | Scope or support is insufficient to make a connector decision safely. |
| `DENY` | Descriptor, activation, rights, sensitivity, product, or policy blocks the operation. |
| `ERROR` | Transport, parsing, integrity, storage, contract, or unexpected implementation failure occurred. |

Suggested reason-code families, **PROPOSED**:

- `DESCRIPTOR_MISSING`, `DESCRIPTOR_CONFLICT`, `ACTIVATION_MISSING`, `SCOPE_NOT_ALLOWED`;
- `NETWORK_DISABLED`, `AUTH_REQUIRED`, `TIMEOUT`, `RATE_LIMIT`, `SOURCE_UNAVAILABLE`;
- `PAGINATION_LOOP`, `PARTIAL_RESPONSE`, `MALFORMED_RESPONSE`, `SCHEMA_DRIFT`;
- `PRODUCT_UNSUPPORTED`, `GRADE_NOT_ELIGIBLE`, `QUALITY_FLAG_REVIEW`;
- `RIGHTS_MISSING`, `RIGHTS_UNRECOGNIZED`, `ATTRIBUTION_MISSING`, `MEDIA_RIGHTS_UNRESOLVED`;
- `TAXON_UNRESOLVED`, `TAXON_CONFLICT`;
- `GEOPRIVACY_UNKNOWN`, `SENSITIVITY_UNKNOWN`, `SENSITIVE_REVIEW_REQUIRED`;
- `IDENTITY_MISSING`, `TIME_INVALID`, `GEOMETRY_INVALID`, `INTEGRITY_MISMATCH`;
- `HANDOFF_FAILED`, `RECEIPT_FAILED`, `INTERNAL_ERROR`.

Expected source/governance conditions should not be represented only by free-text exceptions. Programmer errors may raise internally, but the connector boundary must convert them to a finite `ERROR` outcome without leaking sensitive context.

[Back to top ↑](#top)

---

## Logging and sensitive-data discipline

Use a structured allowlist.

### Safe by default

- run ID;
- source-family and product IDs;
- connector/parser version;
- request digest, response digest, and page ordinal;
- safe endpoint family label, not secret-bearing URL text;
- response status class;
- record counts and outcome counts;
- duration and bounded retry count;
- finite outcome and stable reason codes;
- non-sensitive RAW/QUARANTINE/receipt references.

### Forbidden by default

- API keys, tokens, authorization headers, cookies, signed URLs, private query values;
- raw response bodies or oversized payload excerpts;
- exact private, obscured, restricted, or sensitive coordinates;
- observer contact details, private profile fields, private-place context, or user history;
- media bytes, EXIF, or embedded location;
- unredacted exception locals;
- package-relative descriptor contents presented as authority;
- public-safe statements not backed by release state.

Logging configuration belongs to the caller. Importing the package must not configure root loggers or emit log lines.

[Back to top ↑](#top)

---

## Testing contract

No executable package-local test was verified in this update. The first implementation PRs must add safe, deterministic, no-network tests in the accepted test authority.

### Import and packaging

- importing `inaturalist`, `inaturalist.fetch`, and `inaturalist.admit` performs no network, filesystem, environment-secret, clock, ID-generation, logging-configuration, or thread/process side effect;
- parent project metadata builds/installs only after build backend, package discovery, dependencies, Python support, and import name are accepted;
- `__init__.py` exports only the reviewed public surface;
- the connector-local `descriptor.yaml` is never auto-loaded and cannot activate access.

### Query and fetch

- query normalization and digest are deterministic;
- secret values do not enter the digest or logs;
- network defaults to disabled;
- fake transport covers success, timeout, forbidden, not-found, rate-limit, outage, malformed body, partial body, duplicate page, cursor loop, and retry exhaustion;
- page, record, retry, timeout, and total-work bounds are enforced;
- response digest is captured before parsing;
- live access tests are separately marked, disabled by default, and require explicit steward approval.

### Parsing and preservation

- source identity, product, grade, flags, taxonomy, rights, attribution, times, geometry/support, uncertainty, geoprivacy, media references, and lineage are preserved;
- unknown and conflicting values remain visible;
- source, observed, retrieval, snapshot, release, and correction times do not collapse;
- exact sensitive coordinates never appear in logs or snapshots;
- parser output does not claim admission or public safety.

### Admission and outcomes

- research-grade + recognized normalized CC + controlled-taxonomy success can reach an `ADMIT_RAW` candidate only when every supplied gate allows;
- casual/non-research-grade records route to candidate/quarantine under the current product;
- captive/cultivated and disputed-quality cases remain explicit;
- missing/unknown/conflicting rights, taxonomy, geoprivacy, sensitivity, identity, time, geometry, integrity, or review support fails closed;
- mixed batches retain per-record decisions;
- outcome and reason-code serialization is stable;
- identical inputs produce deterministic candidate content where practical.

### Handoff, receipts, and boundaries

- default behavior returns candidates without writes;
- fake sinks prove only explicit RAW, QUARANTINE, and receipt methods are callable;
- no path to WORK, PROCESSED, CATALOG, TRIPLET, PUBLISHED, proof, registry, release, API, UI, map, search, graph, or AI exists;
- repeated unchanged input produces a no-op candidate where supported;
- handoff failure returns `ERROR` without losing prior lineage;
- receipts preserve digests and decisions without becoming proof or release authority.

### Fixture safety

- use synthetic, minimized observation records;
- include research-grade/casual pairs, open/obscured/private/missing geometry, rights variants, taxonomy agreement/conflict, and record-version changes;
- use toy coordinates or generalized non-sensitive geometry;
- use no real observer contact data or media bytes;
- never auto-refresh fixtures from the live service.

[Back to top ↑](#top)

---

## Implementation sequence

Use small PRs; do not jump directly to live network access.

| Step | Smallest useful change | Required proof | Rollback |
|---|---|---|---|
| 0 | Resolve or isolate connector-local `descriptor.yaml`; confirm accepted registry/schema posture. | Migration/decision record and test proving no auto-load. | Restore prior placeholder while keeping live access disabled. |
| 1 | Complete `pyproject.toml` and add import-side-effect smoke tests, without source access. | Build/install/import test and dependency review. | Revert packaging commit. |
| 2 | Add immutable models, outcome/reason codes, and query canonicalization. | Unit and serialization tests, deterministic digest fixtures. | Revert pure-core files. |
| 3 | Add parser using synthetic fixtures only. | Field-preservation, malformed-input, privacy, and no-sensitive-log tests. | Revert parser/fixtures. |
| 4 | Add connector-local validation and pure admission assembly using supplied decisions. | Research-grade/casual, rights, taxonomy, geoprivacy, sensitivity, and mixed-batch negative tests. | Revert decision modules. |
| 5 | Add receipt and candidate handoff builders with in-memory sinks. | Idempotency, no-op, integrity, boundary, and failure tests. | Revert adapters. |
| 6 | Add injected fake transport and bounded fetch behavior. | Timeout, retry, rate-limit, pagination, partial-response, and schema-drift tests. | Revert transport implementation. |
| 7 | Consider explicitly activated live transport. | Current official-source review, accepted descriptor/activation, rights review, bounded live test, safe logs, and rollback. | Disable network flag and revert adapter. |
| 8 | Add product-specific module only after layout decision. | Accepted product ID/contract, module-placement decision, tests, and migration note if needed. | Revert product module without changing family package API. |

Each step should update this README or adjacent documentation when behavior materially changes.

[Back to top ↑](#top)

---

## Definition of done

### This documentation revision

- [x] Target and base commit are pinned.
- [x] Verified current package files and placeholder states are listed.
- [x] Parent project metadata and its limits are explicit.
- [x] Proposed v0.1 modules that are absent at common paths are no longer described as uninspected mystery files.
- [x] The connector-local descriptor conflict and unsafe `public` sensitivity default are explicit.
- [x] Source-family, product, descriptor, activation, policy, schema, proof, catalog, release, and public-client boundaries are explicit.
- [x] Import, dependency, API, fetch, parse, admission, rights, taxonomy, geoprivacy, sensitivity, I/O, receipt, error, logging, test, implementation, and rollback contracts are defined.
- [x] RAW, QUARANTINE, and process-memory receipt support is reconciled with root connector doctrine.
- [x] Stale blank-file and unresolved rollback-SHA language is removed.
- [x] No code, endpoint, credential, source data, policy decision, or runtime behavior is claimed.

### Package implementation

- [ ] Owners and reviewers are assigned.
- [ ] Complete recursive inventory confirms no hidden or differently named implementation.
- [ ] `descriptor.yaml` is removed, migrated, or formally classified and cannot activate access.
- [ ] SourceDescriptor schema/registry path conflicts are resolved.
- [ ] Stable source-family and product IDs and aliases are accepted.
- [ ] Build backend, Python version, dependency set, package discovery, install/import command, and versioning policy are accepted.
- [ ] Import side effects are absent and tested.
- [ ] Models, query, parser, validation, decision, receipt, handoff, and error contracts are implemented and tested.
- [ ] Rights, taxonomy, geoprivacy, sensitivity, and quality-grade behavior is supplied by governed decisions and fails closed.
- [ ] RAW/QUARANTINE/receipt interfaces are accepted, idempotent, and tested.
- [ ] Endpoint, auth, pagination, retry, rate limit, cadence, source terms, deletion, correction, and outage behavior are verified.
- [ ] No-network tests and negative fixtures are substantive.
- [ ] CI proves package, connector, rights, taxonomy, geoprivacy, sensitivity, and lifecycle boundaries.
- [ ] Live access remains separately activated, reviewed, bounded, auditable, and reversible.
- [ ] Public clients are proven unable to use connector internals or unreleased material directly.

[Back to top ↑](#top)

---

## Verification backlog

| Item | Status | Evidence required |
|---|---:|---|
| Complete recursive inventory under `connectors/inaturalist/` and repository-wide import/search scan. | **NEEDS VERIFICATION** | Current tree, import graph, and code search. |
| Confirm distribution/import identity, import-namespace collision risk, and supported Python versions. | **NEEDS VERIFICATION** | Accepted `pyproject.toml`, namespace decision, build logs, install test, import test. |
| Select sync/async transport model and dependency library. | **NEEDS VERIFICATION** | Package decision, dependency review, tests, ADR if cross-repo standard. |
| Resolve `descriptor.yaml` disposition. | **CONFLICTED / high priority** | Registry decision, migration note, deletion/rename or fixture classification, negative auto-load test. |
| Resolve singular/plural SourceDescriptor schemas and substantive validation. | **CONFLICTED** | Accepted schema/ADR, fixtures, validator, migration. |
| Reconcile fauna-scoped registry template with `data/registry/sources/<domain>/` doctrine. | **NEEDS VERIFICATION / drift** | Registry inventory, accepted descriptor, validator output. |
| Confirm source-family and observation-product IDs, versions, and aliases. | **NEEDS VERIFICATION** | Source catalog/registry decision. |
| Confirm product-module layout and whether `products/observations.py` or configuration-driven routing is preferred. | **NEEDS VERIFICATION / ADR-class if authority or paths move** | Package/module decision, tests, migration note. |
| Resolve non-research-grade product (`OPEN-INAT-01`). | **OPEN** | Source/Fauna/Flora steward decision and accepted product contract. |
| Resolve ITIS/GBIF taxonomy tie-breaking (`OPEN-INAT-02`). | **OPEN** | Biodiversity/taxonomy decision and deterministic crosswalk tests. |
| Resolve captive/cultivated and other quality flags. | **NEEDS VERIFICATION** | Product contract and fixtures. |
| Verify current endpoint, API version, auth, query, sort, pagination, rate limit, cadence, and outage behavior. | **NEEDS VERIFICATION** | Current official-source review and bounded tests. |
| Verify observation and media rights, attribution, caching, redistribution, training, revocation, and withdrawal. | **NEEDS VERIFICATION** | Rights review, terms review, fixtures, policy tests. |
| Confirm geoprivacy states, source changes, sensitive-taxa/site inputs, public-precision profiles, and media-location handling. | **NEEDS VERIFICATION** | Policy bundles, redaction contracts, fixtures, tests. |
| Confirm request/response digest, replay storage/reference, no-op identity, record deletion, and withdrawal behavior. | **NEEDS VERIFICATION** | Receipt/replay contracts and integration tests. |
| Confirm RAW, QUARANTINE, and process-memory receipt contracts and sink ownership. | **NEEDS VERIFICATION** | Contracts, schemas, adapters, tests. |
| Confirm substantive connector/package CI rather than placeholder workflow steps. | **UNKNOWN** | Workflow definitions, job steps, and current logs. |
| Reconcile adjacent parent/source/test README inventories and receipt language. | **NEEDS VERIFICATION / drift** | Focused follow-up documentation PR and link validation. |
| Confirm no public API/UI, map, tile, report, search, graph, vector index, or AI imports this package or reads unreleased output directly. | **NEEDS VERIFICATION** | App/import graph, access policy, tests, runtime evidence. |

[Back to top ↑](#top)

---

## Review and rollback

Before merge, rollback means closing the draft pull request and abandoning its scoped branch.

After merge, transparently revert the commit that introduces this v0.2 package contract and its paired generated receipt, then rerun applicable documentation, package/import, connector, schema, descriptor, rights, taxonomy, geoprivacy, sensitivity, validation, receipt, lifecycle-boundary, citation, correction, and rollback checks. Do not rewrite shared history.

Concrete prior-state target: v0.1 blob `93b4412cf06effe1276a71357748ad34d2657a91` at base commit `2ef3cf2c21ee2384a51d8ca76cdec302d825770c`.

Rollback or correction is required if this README is used to justify:

- claiming the package is installable, import-tested, implemented, activated, rights-cleared, sensitivity-cleared, or publication-ready without evidence;
- loading `descriptor.yaml` as authority or accepting `sensitivity_floor: public` as a safe default;
- making network, filesystem, environment, clock, ID, logging, thread, or cache side effects at import time;
- making live access implicit or unbounded;
- inventing product, source role, rights, taxonomy, sensitivity, or public precision;
- silently upgrading casual/non-research-grade records;
- deobscuring, inferring, logging, or publishing private or sensitive location;
- collapsing observation and media rights;
- destructive deduplication across observations, specimens, surveys, models, or aggregates;
- writing beyond explicit RAW, QUARANTINE, or process-memory receipt interfaces;
- treating receipts as proof, catalog, promotion, review, or publication closure;
- allowing public applications, maps, search, graphs, indexes, or AI to use connector internals or unreleased material directly.

Required reviewers are **NEEDS VERIFICATION** because current CODEOWNERS has only a catch-all maintainer rule for this path. At minimum, review should cover connector/source ownership, Python packaging, Fauna or Flora semantics, biodiversity/taxonomy, rights, sensitivity/geoprivacy, validation/testing, and documentation.

---

## Maintainer note

Keep this package small, explicit, deterministic, testable, source-preserving, product-aware, and fail-closed. The package is a mechanical admission helper inside the trust membrane. It does not decide truth, policy, public precision, release, or publication.

<p align="right"><a href="#top">Back to top</a></p>
