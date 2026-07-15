<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-nasa-smap-nested-readme
title: connectors/nasa/smap/ — NASA SMAP README-Only Nested Product-Lane Boundary
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Connector steward · NASA/SMAP source steward · Soil steward · Agriculture steward · Security reviewer · Rights reviewer · Validation steward · Test steward · Docs steward
created: 2026-06-19
updated: 2026-07-14
policy_label: public-doctrine; readme-only; nested-product-lane; path-posture-unresolved; nasa; smap; model-assimilated-reference; surface-root-zone-separated; no-network; no-activation; raw-quarantine-only; no-publication
current_path: connectors/nasa/smap/README.md
truth_posture: CONFIRMED repository-present README-only nested lane at named conventional probes, v0.1 lineage, parallel nested/flat README surfaces, placeholder Soil/Agriculture registry records, empty machine source-authority register, draft downstream Soil pipeline documentation, conflicted SourceDescriptor schema authority, and TODO-only generic connector validation / CONFLICTED final NASA product-lane topology and SourceDescriptor schema path / PROPOSED future server-side SMAP source adapter / UNKNOWN recursive lane inventory, runtime implementation, credentials, endpoint allowlist, product identifiers, rights clearance, quotas, retry budgets, fixtures, executable tests, lifecycle artifacts, deployment, release state, and owners
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: d6c6556e2e20a06d12b49d4c94ed6fe996e003d7
  prior_blob: 303712b0601751deea432c1375691ce89b241b8c
related:
  - ../README.md
  - ../../README.md
  - ../../nasa-smap/README.md
  - ../../nasa-earthdata/README.md
  - ../../../CONTRIBUTING.md
  - ../../../.github/CODEOWNERS
  - ../../../.github/PULL_REQUEST_TEMPLATE.md
  - ../../../.github/workflows/connector-gate.yml
  - ../../../.github/workflows/source-descriptor-validate.yml
  - ../../../docs/architecture/directory-rules.md
  - ../../../docs/adr/README.md
  - ../../../docs/adr/ADR-0012-connector-outputs-to-data-raw-or-data-quarantine-only.md
  - ../../../docs/registers/DRIFT_REGISTER.md
  - ../../../docs/sources/catalog/OPEN-QUESTIONS.md
  - ../../../docs/sources/catalog/nasa/README.md
  - ../../../docs/sources/catalog/nasa/nasa-smap.md
  - ../../../docs/sources/catalog/nasa/nasa-earthdata.md
  - ../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../contracts/source/source_descriptor.md
  - ../../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../../schemas/contracts/v1/sources/source_descriptor.schema.json
  - ../../../control_plane/source_authority_register.yaml
  - ../../../data/registry/sources/soil/nasa-smap.yaml
  - ../../../data/registry/sources/agriculture/nasa-smap.yaml
  - ../../../data/registry/sources/agriculture/nasa_smap.yaml
  - ../../../pipelines/domains/soil/smap_ingest/README.md
  - ../../../data/raw/
  - ../../../data/quarantine/
  - ../../../policy/source/
  - ../../../policy/rights/
  - ../../../policy/sensitivity/
  - ../../../release/
tags: [kfm, connectors, nasa, nested-lane, nasa-smap, smap, soil-moisture, earthdata, readme-only, source-admission, model-assimilated, surface-root-zone, nrt, reprocessed, soil, agriculture, rights, freshness, raw, quarantine, governance]
notes:
  - "At the pinned base, this README is the only confirmed file at the nested lane's directly inspected conventional package and test probes. Exact probes for pyproject.toml, src/nasa_smap/__init__.py, tests/README.md, __init__.py, client.py, and tests/test_smap.py returned Not Found. This is bounded named-path evidence, not an exhaustive recursive tree receipt."
  - "The repository also contains connectors/nasa-smap/README.md. Both paths are documentation boundaries; no accepted ADR or migration note inspected here selects one as the final canonical implementation home."
  - "OPEN-DSC-14 remains DEFERRED. data/registry/sources/nasa/README.md was not found, so the documented family-promotion gate is not satisfied by folder presence."
  - "The machine source-authority register has entries: []; the inspected Soil and Agriculture SMAP YAML files are PROPOSED placeholders, and Agriculture has both hyphenated and underscored placeholder names. None establishes activation."
  - "The populated singular SourceDescriptor schema declares the plural path canonical, while the plural file is an empty permissive PROPOSED scaffold. This README does not choose a winning schema path."
  - "The Soil SMAP pipeline README exists and is detailed, but executable behavior, source linkage, schedules, CI, and release wiring remain unverified; pipeline_specs/soil/smap_ingest.yaml was not found."
  - "The generic connector and SourceDescriptor workflows are TODO-only echo scaffolds and therefore do not prove enforcement."
  - "Only this Markdown file changes. No code, package metadata, credential, endpoint configuration, SourceDescriptor, registry activation, policy, schema, contract, fixture, executable test, workflow, lifecycle artifact, release object, path move, or public artifact is created or modified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# NASA SMAP README-Only Nested Product-Lane Boundary

> [!IMPORTANT]
> **Document lifecycle:** `draft v0.2`  
> **Component maturity:** README-only at the directly inspected nested-lane probes; no supported package, SMAP client, Earthdata client, downloader, parser, admission decision, test lane, or lifecycle handoff is verified  
> **Path posture:** the nested lane exists, but NASA-family promotion and final nested-versus-flat product topology remain `DEFERRED / CONFLICTED / NEEDS VERIFICATION`  
> **Authority:** implementation-boundary documentation inside `connectors/`; no source, credential, schema, policy, registry, evidence, lifecycle, release, routing, or publication authority

> [!CAUTION]
> NASA product access may require account credentials, bearer tokens, cookies, signed URLs, or provider redirects. Never commit, log, serialize, fixture, expose to a browser, or place in an error message any credential value, authorization header, cookie, token cache, private redirect, signed URL, or protected payload.

![status](https://img.shields.io/badge/status-draft-yellow?style=flat-square)
![maturity](https://img.shields.io/badge/maturity-README--only-lightgrey?style=flat-square)
![topology](https://img.shields.io/badge/topology-DEFERRED%20%2F%20CONFLICTED-orange?style=flat-square)
![authority](https://img.shields.io/badge/authority-source--admission-blue?style=flat-square)
![lifecycle](https://img.shields.io/badge/output-RAW%20%7C%20QUARANTINE-orange?style=flat-square)
![publication](https://img.shields.io/badge/publication-NOT%20AUTHORIZED-critical?style=flat-square)

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [What belongs](#what-belongs-here) · [What does not](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed) · [Topology](#flat-and-nested-lane-alignment) · [Semantic boundary](#smap-source-role-and-semantic-boundary) · [Access](#access-authentication-and-secret-boundary) · [Operations](#endpoint-format-cadence-and-resilience-posture) · [Lifecycle](#lifecycle-and-quarantine-boundary) · [Identity](#identity-hashing-deduplication-and-replay) · [Fixtures](#no-network-fixture-strategy) · [Activation](#activation-promotion-and-publication) · [Evidence](#evidence-basis) · [Rollback](#correction-rollback-and-deactivation) · [Backlog](#verification-backlog) · [Done](#definition-of-done)

---

## Purpose

`connectors/nasa/smap/` currently provides a documentation boundary for a possible nested NASA SMAP product adapter under the NASA connector-family lane.

This README is for connector, source, Soil, Agriculture, security, rights, validation, test, and documentation maintainers. It exists to:

- prevent this folder from being mistaken for an implemented, activated, or canonical connector;
- keep the nested lane aligned with the parallel flat [`connectors/nasa-smap/`](../../nasa-smap/) boundary;
- preserve SMAP product, collection, granule, processing-level, version, cadence, layer, grid, source-role, temporal, rights, and provenance distinctions;
- keep observation-class product candidates distinct from model-assimilated reference candidates;
- keep surface and root-zone soil-moisture semantics separate;
- keep near-real-time and standard/reprocessed candidates separate until downstream supersession handling is proven;
- constrain any future connector output to source references, secret-free run-local sidecars, or caller-owned RAW/QUARANTINE handoff candidates;
- keep connector activity upstream of normalization, EvidenceBundle closure, cataloging, promotion, release, public API/UI behavior, and AI interpretation.

This README does not prove implementation, canonical placement, source activation, product selection, rights clearance, endpoint availability, or public-release eligibility.

---

## Authority level

| Concern | Status | Evidence-bounded determination |
|---|---:|---|
| Owning responsibility root | **CONFIRMED** | Directory Rules §7.3 assigns source-specific fetch and admission to `connectors/`. |
| Current nested path | **CONFIRMED** | `connectors/nasa/smap/README.md` exists at the pinned base. |
| Final product-lane topology | **CONFLICTED / DEFERRED** | Both nested and flat SMAP README surfaces exist. No accepted ADR or migration note inspected here selects one as canonical or compatibility-only. |
| NASA family promotion | **DEFERRED** | `OPEN-DSC-14` requires an ADR plus a populated connector and source-registry companion. The named NASA registry-family README was not found. |
| Connector implementation | **NOT ESTABLISHED** | The README is verified; named conventional package, module, client, and test probes were absent. Differently named or deeper content remains `UNKNOWN`. |
| Source authority / activation | **NOT ESTABLISHED** | `control_plane/source_authority_register.yaml` contains `entries: []`; inspected SMAP registry YAMLs are PROPOSED placeholders. |
| SourceDescriptor authority | **CONFLICTED** | The populated singular schema points to a plural canonical path whose file is an empty permissive scaffold. |
| Product/source doctrine | **DRAFT / PROPOSED** | The NASA SMAP catalog page preserves useful semantic boundaries but does not create machine authority or activation. |
| Downstream pipeline | **DOCUMENTED / EXECUTION NOT ESTABLISHED** | The Soil SMAP pipeline README exists; its named pipeline spec was not found. |
| Rights and sensitivity enforcement | **UNKNOWN** | No SMAP-specific executable rights or sensitivity decision was verified. |
| CI enforcement | **TODO-ONLY SCAFFOLDS** | The inspected connector and SourceDescriptor workflows only echo TODO messages. |
| Public output | **NONE AUTHORIZED** | This lane creates no map, API payload, claim, EvidenceBundle, release, or publication artifact. |

This edit does not choose the winning topology, SourceDescriptor schema path, registry naming, product collection, credential provider, environment-variable names, endpoint allowlist, retry budget, rate limit, source activation state, or public-release posture.

---

## Status

At `main@d6c6556e2e20a06d12b49d4c94ed6fe996e003d7`, exact probes confirmed this target README and returned `Not Found` for:

```text
connectors/nasa/smap/pyproject.toml
connectors/nasa/smap/src/nasa_smap/__init__.py
connectors/nasa/smap/tests/README.md
connectors/nasa/smap/__init__.py
connectors/nasa/smap/client.py
connectors/nasa/smap/tests/test_smap.py
pipeline_specs/soil/smap_ingest.yaml
data/registry/sources/nasa/README.md
```

These are bounded named-path absences, not an exhaustive recursive tree receipt.

| Surface | Confirmed state | Safe conclusion |
|---|---|---|
| This README | v0.1 exists at prior blob `303712b0…` | A boundary document existed; runtime does not follow from it. |
| Nested lane | Target README exists | Path presence does not establish canonical topology or package maturity. |
| Flat lane | `connectors/nasa-smap/README.md` exists at v0.2 | A fuller parallel boundary exists; it is not accepted as canonical by folder presence alone. |
| NASA umbrella | `connectors/nasa/README.md` exists at v0.1 | Umbrella planning exists; `OPEN-DSC-14` remains deferred. |
| Machine authority register | Empty | No source authority or activation is established. |
| Soil SMAP registry | PROPOSED placeholder | A filename is not a validated SourceDescriptor. |
| Agriculture SMAP registries | Hyphenated and underscored PROPOSED placeholders | Naming and duplication require reconciliation; neither grants authority. |
| SourceDescriptor schemas | Populated singular file plus empty plural scaffold | Canonical schema and validator wiring are conflicted. |
| Soil pipeline README | Detailed draft documentation | Downstream semantics are documented; execution and release wiring remain unproven. |
| Generic workflows | TODO-only jobs | A workflow file or green run would not prove connector behavior. |

---

## What belongs here

Until topology, authority, implementation, and activation gates close, this lane should contain only:

- this boundary document and evidence pointers;
- topology, migration, deprecation, redirect, and rollback notes;
- future product, collection, and granule discovery code that preserves upstream identity and query evidence;
- future server-side authorization and protected-source access adapters;
- future download and integrity helpers with bounded size, timeout, redirect, and format checks;
- future RAW/QUARANTINE candidate-envelope helpers that receive destinations from governed orchestration;
- future no-network tests and rights-cleared fixtures;
- future secret-free run evidence tied to one source attempt.

Every non-document file still requires an accepted topology, a real consumer, settled contracts and schemas, reviewed source descriptors, policy and rights posture, tests, and rollback.

## What does NOT belong here

This lane must not own or contain:

- NASA source-family doctrine or SMAP product doctrine;
- authoritative SourceDescriptor instances or source-activation decisions;
- canonical contracts, schemas, policies, rights decisions, or sensitivity rules;
- credentials, token caches, cookies, `.netrc` files, signed URLs, or protected payload fixtures;
- normalization, resampling, reprojection, aggregation, model execution, joins, or Mesonet calibration logic;
- WORK, PROCESSED, CATALOG, TRIPLET, PROOF, RELEASE, PUBLISHED, API, UI, map, alert, or AI outputs;
- release manifests, correction notices, rollback cards, or publication receipts;
- a second implementation that diverges from the flat SMAP lane.

---

## Inputs

### Current inputs

The only confirmed input is repository documentation used to define this boundary.

### Future admissible inputs

A future connector may accept only reviewed, explicit inputs such as:

- a validated product-specific SourceDescriptor and activation reference;
- an approved product, collection, version, provider, processing-level, layer, and cadence selection;
- a server-side credential handle, never a credential value in arguments, files, logs, or receipts;
- approved endpoint and redirect allowlists;
- request geometry and time bounds with product-native constraints preserved;
- caller-owned RAW or QUARANTINE destination intent;
- timeout, retry, backoff, rate-limit, circuit-breaker, and maximum-size budgets;
- an idempotency or replay key;
- a policy-safe clock and run identifier.

Unknown descriptor, rights, sensitivity, access, identity, or destination state must fail closed.

## Outputs

### Current outputs

This README emits no runtime output.

### Future permitted output classes

A future connector may return:

- a source-head or discovery result;
- a secret-free retrieval receipt candidate;
- a checksum manifest and content-identity record;
- an admission candidate for caller-owned `data/raw/` handoff;
- a structured quarantine candidate with reason evidence;
- a deterministic no-op, deny, retry-later, or error result.

The connector must not promote, normalize, catalog, prove, release, publish, or serve the material.

---

## Validation

### Current validation posture

- Markdown structure and repository-relative links can be checked for this documentation change.
- The connector and SourceDescriptor workflows are TODO-only scaffolds.
- No executable nested-lane tests, fixtures, package, client, parser, or handoff validator were verified.
- Passing generic repository checks would not establish SMAP implementation or activation.

### Required future checks

A future implementation must prove:

- nested and flat lanes cannot diverge or both activate;
- credentials and protected URLs never reach logs, exceptions, fixtures, receipts, browsers, or public clients;
- product, layer, cadence, processing-level, version, grid, source role, and temporal identity are preserved;
- observation-class and model-assimilated materials remain distinct;
- surface and root-zone values remain distinct;
- NRT and standard/reprocessed materials retain explicit supersession state;
- downloads enforce endpoint, redirect, media-type, archive, size, timeout, retry, and integrity limits;
- checksums, deduplication, replay, stale/no-op, quarantine, and outage behavior are deterministic;
- outputs can land only in caller-owned RAW or QUARANTINE targets;
- no connector path writes to downstream lifecycle, proof, release, public API/UI, map, or AI surfaces;
- default tests are no-network and fixture rights are recorded.

---

## Review burden

`CODEOWNERS` has no connector-specific rule at the pinned base. The repository-wide placeholder owner applies, but it does not prove that the named team exists or that SMAP review responsibility is accepted.

A future implementation should require, as applicable:

- connector and NASA/SMAP source stewardship;
- Soil and Agriculture semantic review;
- security review for credentials, redirects, archives, parsers, and denial-of-service limits;
- rights and sensitivity review;
- contract, schema, policy, validation, and test review;
- release/public-surface review only for downstream changes outside this lane.

## Related folders

| Surface | Relationship |
|---|---|
| [`../`](../) | Proposed NASA umbrella connector-family boundary. |
| [`../../nasa-smap/`](../../nasa-smap/) | Parallel flat SMAP README-only product lane; topology is unresolved. |
| [`../../`](../../) | Connector-root source-admission contract. |
| [`../../../docs/sources/catalog/nasa/nasa-smap.md`](../../../docs/sources/catalog/nasa/nasa-smap.md) | Draft SMAP product/source documentation; useful semantics, not activation authority. |
| [`../../../data/registry/sources/`](../../../data/registry/sources/) | Intended SourceDescriptor registry home; inspected SMAP files are placeholders. |
| [`../../../pipelines/domains/soil/smap_ingest/`](../../../pipelines/domains/soil/smap_ingest/) | Downstream pipeline documentation; execution remains unverified. |
| [`../../../data/raw/`](../../../data/raw/) and [`../../../data/quarantine/`](../../../data/quarantine/) | Only permitted future payload handoff classes. |
| [`../../../release/`](../../../release/) | Release, correction, withdrawal, and rollback authority outside connectors. |

## ADRs

- No accepted ADR inspected here resolves nested-versus-flat SMAP topology or promotes the NASA family.
- [`OPEN-DSC-14`](../../../docs/sources/catalog/OPEN-QUESTIONS.md#open-dsc-14--connector-derived-families-second-wave) is `DEFERRED` and requires an ADR per family plus populated connector and registry companions.
- [`ADR-0012`](../../../docs/adr/ADR-0012-connector-outputs-to-data-raw-or-data-quarantine-only.md) is repository-present but `draft / proposed`; Directory Rules §7.3 remains the governing connector-output authority.
- The SourceDescriptor singular/plural schema conflict requires an accepted migration or ADR decision before this lane relies on one schema as canonical.

## Last reviewed

**2026-07-14** — repository evidence pinned to `main@d6c6556e2e20a06d12b49d4c94ed6fe996e003d7`.

Review again when topology, source descriptors, product selection, authentication, endpoint behavior, rights, schemas, tests, workflows, pipeline execution, or release state changes.

---

## Flat and nested lane alignment

The nested and flat paths must never become independent runtime authorities.

Until an accepted ADR or migration note chooses a topology:

- treat both paths as README-only boundaries;
- do not activate both implementations;
- do not split product variants, credentials, fixtures, tests, or output paths across them by convenience;
- keep shared source-admission rules in the connector-root contract or settled contracts, schemas, and policies rather than copying them into two code paths;
- require any future move to define canonical and compatibility paths, imports, package metadata, tests, fixture ownership, redirects, deprecation, sunset criteria, and rollback;
- preserve Git history and correction lineage.

This README does not name either path canonical.

---

## SMAP source role and semantic boundary

Repository documentation proposes several SMAP product classes. The connector must preserve the selected product-specific SourceDescriptor role and must not promote a draft catalog claim into machine authority.

Minimum anti-collapse rules:

- SMAP Level-4 material is model-assimilated reference material, not raw measurement or ground truth.
- Observation-class and model-assimilated product candidates remain separate.
- Surface and root-zone values remain separate and are never averaged into generic “soil moisture” by connector convenience.
- Near-real-time and standard/reprocessed candidates remain separate until explicit supersession handling is proven.
- SMAP and Kansas Mesonet or other in-situ observations remain parallel evidence sources; any comparison or calibration belongs downstream and requires a reviewed derived-product contract.
- Native product, layer, version, grid/projection, source resolution, QA/no-data, and temporal identity must survive admission.
- A successful fetch proves retrieval only. It does not prove truth, fitness, freshness, citation closure, release eligibility, or public safety.

---

## Access, authentication, and secret boundary

No authentication implementation or environment-variable name is defined for this nested lane at the pinned base.

Before implementation, current official provider documentation and repository security review must confirm:

- the approved authentication method;
- exact environment-variable or secret-manager key names;
- token refresh, expiry, revocation, and storage behavior;
- redirect and download-host allowlists;
- whether account, terms, or additional agreement acceptance is required;
- safe redaction rules for URLs, headers, cookies, errors, metrics, and receipts.

Authentication must remain server-side. Public clients must never call protected NASA distribution surfaces or receive connector credentials, token-derived URLs, or protected raw payloads.

---

## Endpoint, format, cadence, and resilience posture

Current endpoints, protocols, product identifiers, pagination rules, formats, quotas, and cadence are not established by this README.

| Concern | Current status | Required future evidence |
|---|---:|---|
| Provider and distribution surface | **NEEDS VERIFICATION** | Product-specific SourceDescriptor plus current official provider documentation. |
| Authentication | **NOT IMPLEMENTED** | Reviewed server-side credential contract and secret-leak tests. |
| Endpoint and redirect allowlist | **UNKNOWN** | Approved host list and redirect-denial tests. |
| Protocol and format | **NEEDS VERIFICATION** | Pinned product/version docs, parser limits, and fixture coverage. |
| Pagination and ordering | **UNKNOWN** | Deterministic discovery contract and duplicate-page tests. |
| Cadence and freshness | **NEEDS VERIFICATION** | Descriptor values, stale policy, and source-head behavior. |
| Quotas and rate limits | **UNKNOWN** | Current provider terms plus reviewed budgets. |
| Timeouts and retries | **NOT DEFINED** | Bounded per-attempt/total budgets and jittered backoff tests. |
| Circuit breaking and outage behavior | **NOT DEFINED** | State contract, operator visibility, and recovery tests. |

A future client must distinguish stale, unchanged, unavailable, denied, rate-limited, malformed, integrity-failed, and successfully retrieved states. It must never convert an outage or empty response into a public “no data” claim.

Near-real-time material must retain preliminary cadence and version state. Reprocessed material must not silently overwrite prior identity; any downstream supersession must be explicit and auditable.

---

## Lifecycle and quarantine boundary

The connector may prepare or hand off source material only for RAW or QUARANTINE admission. It does not own the destination root and must receive destination intent from governed orchestration.

A future RAW candidate should require, at minimum:

- validated descriptor and activation references;
- permitted product, layer, version, cadence, format, and request scope;
- resolved rights and sensitivity posture for retention;
- approved endpoint/redirect path and successful secret redaction;
- media-type, size, archive, parser, checksum, and content-identity checks;
- source URI or protected-source reference handled according to policy;
- retrieval time, upstream version/source-head evidence, and run identity;
- caller-owned RAW destination intent.

Quarantine is required when identity, descriptor, activation, rights, sensitivity, access, format, size, archive, parser, integrity, layer semantics, cadence, grid, temporal metadata, destination, or source drift cannot be resolved safely.

Connector activity is not publication authority. RAW and QUARANTINE are not public paths.

---

## Identity, hashing, deduplication, and replay

A future implementation should derive identity from stable source facts, not local filenames or request order. The exact formula remains `NEEDS VERIFICATION` pending settled descriptors and identity contracts.

Required properties:

- preserve provider, product, collection, granule, processing-level, version, layer, cadence, grid, and upstream revision identity;
- hash fetched bytes with the repository-approved algorithm and retain a checksum manifest;
- distinguish identical bytes from conflicting bytes under the same upstream identity;
- make pagination and discovery ordering deterministic;
- support safe replay from pinned descriptor, request, source-head, implementation, and checksum evidence;
- make repeated unchanged retrievals explicit no-ops rather than duplicate admissions;
- never include secrets or signed URLs in IDs, hashes, logs, or receipts;
- never silently overwrite a prior run or hide an upstream correction.

---

## Normalization and downstream responsibility

This lane may preserve source-native metadata and package a source-admission candidate. It must not:

- normalize SMAP values into KFM domain truth;
- resample or reproject rasters;
- aggregate time windows;
- merge layers or cadence classes;
- compare or calibrate against Mesonet;
- create STAC, DCAT, PROV, EvidenceBundle, catalog, proof, release, public layer, API, UI, or AI outputs.

Those responsibilities belong to reviewed downstream pipelines and governance surfaces. A successful download cannot bypass them.

---

## Receipts, evidence, and emitted artifacts

A future connector run should preserve enough secret-free evidence for review without claiming proof closure:

- descriptor and activation references;
- request identity and approved destination intent;
- provider, product, collection, granule, version, layer, cadence, and grid identifiers;
- retrieval start/end time and finite result class;
- policy-safe status, response, redirect, size, media-type, and source-head evidence;
- content checksum and checksum-manifest reference;
- retry, backoff, rate-limit, timeout, no-op, outage, and circuit state;
- rights and sensitivity decision references, not duplicated policy;
- RAW or QUARANTINE handoff reference;
- quarantine, deny, or no-op reason evidence;
- implementation/spec version and replay inputs.

These are process records, not an EvidenceBundle, proof pack, release manifest, or public citation.

---

## No-network fixture strategy

Default tests must not require NASA credentials, live provider access, or mutable upstream state.

A future fixture lane should include small, synthetic or explicitly rights-cleared examples for:

- observation-class and model-assimilated product metadata;
- surface and root-zone semantics;
- NRT and standard/reprocessed candidates;
- pagination, deterministic ordering, duplicate pages, and no-op discovery;
- fictional redirect allow/deny behavior;
- content-type, checksum, truncation, archive-bomb, oversized-object, and malformed-file failures;
- QA, fill-value, no-data, grid, projection, resolution, and time preservation;
- identical duplicate bytes and conflicting duplicate bytes;
- stale, outage, rate-limit, timeout, retry-exhausted, and circuit-open states;
- missing descriptor, inactive source, unresolved rights, unresolved sensitivity, and schema drift;
- credential, token, cookie, signed-URL, and protected-header redaction;
- RAW handoff success and deterministic QUARANTINE outcomes;
- assertions that no downstream lifecycle, proof, release, or public output is written.

Live probes, if later authorized, belong in a separate manual or scheduled lane with explicit terms, budgets, logging controls, and no publication side effects.

---

## Activation, promotion, and publication

A SMAP connector must remain inactive until all applicable items pass:

- final connector topology is accepted or migration/compatibility behavior is documented;
- NASA-family promotion or an explicit product-lane exception is recorded through the required governance path;
- product-specific SourceDescriptors validate against one settled schema authority;
- the machine source-authority register records an approved role and activation state;
- rights, attribution, redistribution, access, sensitivity, retention, and citation are reviewed;
- product, collection, provider, version, processing level, layer, and cadence selections are pinned;
- server-side credential handling and endpoint/redirect allowlists are reviewed;
- no-network fixtures and negative tests exist;
- parsers, limits, retries, timeouts, rate handling, checksums, quarantine, and replay behavior pass;
- RAW/QUARANTINE sinks and secret-free process evidence are proven;
- downstream compatibility is tested without granting the connector normalization or publication authority;
- connector CI performs substantive checks rather than TODO echoes;
- owners and review burden are assigned.

Activation permits source admission only. It does not permit promotion, EvidenceBundle closure, public map/API/UI/AI use, drought or crop-management claims, silent resampling, silent supersession, release, correction, withdrawal, or publication.

Watchers and connectors are not publication authorities.

---

## Rights, attribution, sensitivity, and public safety

Current SMAP-specific rights, attribution, redistribution, access, retention, and citation decisions are not established by this README.

Before activation, authoritative records must answer:

- which provider, product, and version terms apply;
- whether account acceptance or additional agreements apply;
- whether KFM may retain, transform, cache, mirror, redistribute, or publish derived artifacts;
- required attribution and citation text;
- whether protected distribution references impose handling limits;
- whether joins with private fields, infrastructure, archaeological sites, rare species, or other sensitive data raise the sensitivity floor;
- how source corrections, reprocessing, withdrawal, or retirement affect retained and released artifacts.

Public-sector origin does not by itself prove unrestricted redistribution. Coarse satellite resolution does not remove sensitivity created by downstream joins. When rights or sensitivity are unclear, quarantine, restrict, generalize, delay, deny, or abstain rather than assume.

---

## Evidence basis

| Evidence | Status | Supports | Does not prove |
|---|---:|---|---|
| Target README at `main@d6c6556e…` | **CONFIRMED** | v0.1 exists at prior blob `303712b0…`. | Runtime, activation, tests, or canonical topology. |
| Exact nested-lane probes | **CONFIRMED bounded result** | Named package, module, client, and test paths were absent. | Exhaustive recursive absence of every possible implementation file. |
| `connectors/README.md` and Directory Rules §7.3 | **CONFIRMED doctrine/repo docs** | Connector source-admission and RAW/QUARANTINE boundary. | Executable enforcement. |
| Parallel `connectors/nasa-smap/README.md` | **CONFIRMED** | A flat README-only lane also exists. | Which path is canonical. |
| `OPEN-DSC-14` | **CONFIRMED register state** | NASA-family promotion is deferred and gated. | Future resolution. |
| `control_plane/source_authority_register.yaml` | **CONFIRMED empty** | No machine source-authority entry exists. | Future or external authority. |
| Soil/Agriculture SMAP registry YAMLs | **CONFIRMED placeholders** | Proposal filenames and source-doc pointers exist. | Valid SourceDescriptors or activation. |
| Singular/plural SourceDescriptor schemas | **CONFIRMED conflict** | The populated singular schema points to an empty plural canonical scaffold. | Accepted canonical schema or validator behavior. |
| SMAP source catalog page | **CONFIRMED draft document** | Current KFM semantic intent: model-assimilated role, layer/cadence separation, no silent merge. | Current upstream details, rights, endpoint behavior, or machine authority. |
| Soil SMAP ingest pipeline README | **CONFIRMED draft document** | Downstream responsibility and anti-collapse intent. | Executable pipeline, spec, tests, schedules, or release wiring. |
| Generic connector/descriptor workflows | **CONFIRMED TODO-only** | Workflow names and triggers exist. | Substantive validation or gate enforcement. |

Where documentation and machine authority conflict, this README narrows the claim and defers activation.

---

## Correction, rollback, and deactivation

### Documentation rollback

This v0.2 change can be reversed by restoring:

```text
repository: bartytime4life/Kansas-Frontier-Matrix
base commit: d6c6556e2e20a06d12b49d4c94ed6fe996e003d7
prior blob: 303712b0601751deea432c1375691ce89b241b8c
path: connectors/nasa/smap/README.md
```

Rollback changes only this README. It must not delete source material, registry lineage, the flat-lane README, pipeline documentation, or release history.

### Future source deactivation

A future activated connector should support fail-closed pause or deactivation when:

- topology, product, version, provider, endpoint, format, or schema changes incompatibly;
- terms, rights, attribution, access, redistribution, or sensitivity posture changes;
- credentials or secret handling is compromised;
- identity, layer, cadence, QA, grid, or temporal semantics drift;
- repeated integrity, parser, timeout, rate-limit, or outage failures exceed reviewed thresholds;
- descriptor, policy, schema, registry, fixture, validator, or CI state becomes invalid;
- nested and flat lanes diverge;
- upstream correction, withdrawal, or KFM review requires a hold.

Deactivation stops new admission. It does not silently delete prior RAW evidence, overwrite lineage, retract a release, or correct a public claim. Release and correction systems own those actions.

---

## Verification backlog

| Item | Status | Evidence required to close |
|---|---:|---|
| Resolve NASA-family promotion under `OPEN-DSC-14`. | **DEFERRED** | Accepted ADR plus required connector and registry companion state. |
| Resolve nested `connectors/nasa/smap/` versus flat `connectors/nasa-smap/`. | **NEEDS VERIFICATION** | ADR or migration note defining canonical, compatibility, imports, tests, redirects, sunset, and rollback. |
| Produce a complete recursive inventory for both SMAP paths. | **NEEDS VERIFICATION** | Non-truncated tree or contents receipt at a pinned commit. |
| Assign owners and connector-specific review rules. | **NEEDS VERIFICATION** | CODEOWNERS or approved ownership record. |
| Resolve singular/plural SourceDescriptor schema authority. | **CONFLICTED** | Accepted ADR/migration, populated canonical schema, fixtures, validator, and parity tests. |
| Replace SMAP placeholders with validated descriptors or remove duplicates. | **NEEDS VERIFICATION** | Registry decision, descriptor instances, validation, naming migration, and review. |
| Populate machine source-authority state for approved products. | **NOT STARTED** | Reviewed authority/activation entries tied to descriptors and policy. |
| Select and pin product, collection, provider, version, layer, and cadence roles. | **NEEDS VERIFICATION** | Current upstream review plus approved product-specific SourceDescriptors. |
| Verify access, authentication, endpoints, redirects, formats, paging, quotas, and terms. | **NEEDS VERIFICATION** | Current official documentation, security/rights review, and client tests. |
| Define timeouts, retry/backoff, rate handling, circuit breaking, and size limits. | **NEEDS VERIFICATION** | Reviewed configuration contract plus deterministic tests. |
| Create safe no-network fixtures and negative cases. | **NOT ESTABLISHED** | Fixture registry, rights record, tests, and leak checks. |
| Implement and test RAW/QUARANTINE handoff and secret-free run evidence. | **NOT ESTABLISHED** | Code, schemas/contracts, sink tests, process records, and boundary tests. |
| Implement substantive connector and SourceDescriptor CI. | **NOT ESTABLISHED** | Workflows invoking real tests/validators with negative-state coverage. |
| Implement and validate the downstream SMAP pipeline spec. | **NEEDS VERIFICATION** | Accepted spec path, executable code, fixtures, process records, and tests. |
| Prove semantic anti-collapse rules. | **NEEDS VERIFICATION** | Negative fixtures and end-to-end validation receipts. |
| Verify rights, attribution, redistribution, citation, sensitivity, correction, and deactivation. | **NEEDS VERIFICATION** | Policy decisions and steward review. |
| Prove no connector/browser/public-path access and no connector publication. | **NEEDS VERIFICATION** | Architecture tests, dependency checks, route tests, and release-gate evidence. |

---

## Definition of done

This connector lane is not implementation-complete until all applicable criteria pass:

- [ ] An accepted topology decision identifies the canonical lane and any compatibility or migration behavior.
- [ ] NASA-family promotion or a product-lane exception is recorded through the required governance path.
- [ ] Product-specific SourceDescriptors validate against one accepted schema authority.
- [ ] Machine authority/activation entries exist for selected products and roles.
- [ ] Rights, attribution, redistribution, access, retention, sensitivity, citation, and correction postures are reviewed.
- [ ] Product, provider, collection, version, processing-level, layer, cadence, grid, and temporal identities are pinned.
- [ ] Server-side credential handling, endpoint/redirect allowlists, parser limits, and secret-redaction tests pass.
- [ ] Timeouts, retry/backoff, rate limits, circuit breaking, paging, checksums, and replay behavior are deterministic and tested.
- [ ] No-network valid, invalid, and golden fixtures exist with rights and provenance notes.
- [ ] RAW and QUARANTINE handoffs are append-only, checksummed, and bounded by Directory Rules.
- [ ] Observation/model, surface/root-zone, NRT/reprocessed, source-native/derived, and grid/station distinctions are enforced by negative tests.
- [ ] Connector output cannot reach downstream lifecycle, proof, release, public API/UI/map, or AI surfaces.
- [ ] The downstream Soil pipeline consumes admitted inputs without giving the connector normalization or publication authority.
- [ ] CI runs substantive tests and validators rather than TODO echoes.
- [ ] Owners, review burden, operational runbook, correction path, deactivation path, and rollback target are assigned.
- [ ] Nested, flat, umbrella, registry, schema, policy, test, and pipeline documentation agree.

Until then, the honest status is **README-only / inactive / not publication-authorized**.

---

## Changelog

### v0.2 — 2026-07-14

- Replaced broad implementation uncertainty with a commit-pinned repository evidence snapshot.
- Recorded the nested/flat SMAP path conflict without selecting a canonical home.
- Recorded the deferred NASA-family promotion gate and missing family registry companion.
- Distinguished placeholder registry filenames from validated SourceDescriptors and activation.
- Surfaced the singular/plural SourceDescriptor schema-authority conflict.
- Distinguished downstream pipeline documentation from verified executable behavior.
- Recorded TODO-only connector validation and placeholder CODEOWNERS posture.
- Added the Directory Rules §15 folder README contract in required order.
- Added source-role, credential, endpoint/cadence, resilience, stale/outage, lifecycle, quarantine, identity/replay, fixture, activation, rights, rollback, deactivation, and definition-of-done boundaries.
- Preserved the v0.1 anti-collapse posture: Level-4 model-assimilated reference is not raw measurement; surface is not root-zone; NRT is not reprocessed; SMAP is not silently merged with in-situ evidence.
- Changed no file except this README and granted no implementation, source, registry, release, or publication authority.

### v0.1 — 2026-06-19

- Replaced a blank placeholder with the initial nested SMAP product-lane boundary note.

---

## Maintainer note

Keep this lane conservative. A connector may preserve and admit source material after gates; it may not decide what the material proves, normalize it into domain truth, merge it with in-situ evidence, publish it, or turn a successful fetch into a public claim.

<p align="right"><a href="#top">Back to top</a></p>
