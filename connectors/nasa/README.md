<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-nasa-readme
title: connectors/nasa/ — NASA README-Only Connector Family Boundary
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Connector steward · NASA source steward · Earth-observation steward · Hazards steward · Soil steward · Agriculture steward · Security reviewer · Rights reviewer · Sensitivity reviewer · Validation steward · Test steward · Docs steward
created: 2026-06-19
updated: 2026-07-14
policy_label: public-doctrine; readme-only; connector-family-boundary; nasa; family-promotion-deferred; mixed-flat-nested-topology; no-network; no-activation; raw-quarantine-only; no-publication
current_path: connectors/nasa/README.md
truth_posture: CONFIRMED repository-present v0.1 README, flat Earthdata/FIRMS/HLS/SMAP README lanes, nested HLS/SMAP README lanes, absent named nested Earthdata/FIRMS lanes, empty machine source-authority register, absent NASA family registry companion, product-level placeholder registry records, conflicted Directory Rules placement and SourceDescriptor schema surfaces, placeholder CODEOWNERS, and TODO-only connector/descriptor workflows / DEFERRED NASA family promotion under OPEN-DSC-14 / CONFLICTED final flat-versus-nested connector topology and SourceDescriptor schema authority / PROPOSED future server-side NASA connector-family coordination / UNKNOWN recursive family inventory, runtime implementation, credentials, endpoint allowlists, product selections, rights clearance, quotas, resilience budgets, fixtures, executable tests, lifecycle artifacts, deployment, release state, and owners
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 1c776e17922b5c19ed2337b559d18d8c947e7c63
  prior_blob: d8eea51b9205865de0ea1545e75404ee8c48001c
related:
  - ../README.md
  - ../nasa-earthdata/README.md
  - ../nasa-firms/README.md
  - ../nasa-hls/README.md
  - ../nasa-smap/README.md
  - hls/README.md
  - smap/README.md
  - ../../CONTRIBUTING.md
  - ../../.github/CODEOWNERS
  - ../../.github/PULL_REQUEST_TEMPLATE.md
  - ../../.github/workflows/connector-gate.yml
  - ../../.github/workflows/source-descriptor-validate.yml
  - ../../docs/architecture/directory-rules.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/README.md
  - ../../docs/adr/ADR-0012-connector-outputs-to-data-raw-or-data-quarantine-only.md
  - ../../docs/registers/DRIFT_REGISTER.md
  - ../../docs/sources/catalog/OPEN-QUESTIONS.md
  - ../../docs/sources/catalog/nasa/README.md
  - ../../docs/sources/catalog/nasa/nasa-earthdata.md
  - ../../docs/sources/catalog/nasa/nasa-firms.md
  - ../../docs/sources/catalog/nasa/nasa-hls.md
  - ../../docs/sources/catalog/nasa/nasa-smap.md
  - ../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../contracts/source/source_descriptor.md
  - ../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../schemas/contracts/v1/sources/source_descriptor.schema.json
  - ../../control_plane/source_authority_register.yaml
  - ../../data/registry/sources/agriculture/nasa_hls.yaml
  - ../../data/registry/sources/soil/nasa-smap.yaml
  - ../../data/registry/sources/agriculture/nasa-smap.yaml
  - ../../data/registry/sources/agriculture/nasa_smap.yaml
  - ../../policy/source/README.md
  - ../../policy/rights/README.md
  - ../../policy/sensitivity/README.md
tags: [kfm, connectors, nasa, earth-observation, earthdata, firms, hls, smap, family-boundary, topology, source-admission, rights, sensitivity, freshness, raw, quarantine, governance]
notes:
  - "At the pinned base, exact conventional umbrella probes for pyproject.toml, src/nasa/__init__.py, tests/README.md, and __init__.py returned Not Found. This is bounded named-path evidence, not an exhaustive recursive tree receipt."
  - "OPEN-DSC-14 remains DEFERRED and requires an ADR per family gated on populated connectors/<family>/ plus data/registry/sources/<family>/ companions. data/registry/sources/nasa/README.md was not found; folder or product README presence does not promote the family."
  - "Flat README lanes exist for Earthdata, FIRMS, HLS, and SMAP. Nested HLS and SMAP README lanes also exist; exact nested Earthdata and FIRMS README probes returned Not Found. This document does not choose a canonical topology."
  - "The machine source-authority register has entries: []; inspected HLS and SMAP registry YAMLs are PROPOSED placeholders, and Agriculture contains both hyphenated and underscored SMAP placeholder names. None establishes authority or activation."
  - "Two Directory Rules files exist at architecture and doctrine paths with different versions/status metadata but matching connector and README-order rules. The populated singular SourceDescriptor schema also names an almost-empty plural scaffold as canonical. Neither conflict is resolved here."
  - "The connector and SourceDescriptor workflows only echo TODO checks. CODEOWNERS has a global placeholder and no NASA or connector-specific rule."
  - "Product semantics in this README are bounded to current repository documentation and do not assert current external endpoints, credentials, quotas, cadence, rights, or product versions."
  - "Only this Markdown file changes. No path, code, package metadata, credential, endpoint configuration, SourceDescriptor, registry activation, policy, schema, contract, fixture, executable test, workflow, lifecycle artifact, release object, or public artifact is created or modified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# NASA README-Only Connector Family Boundary

> [!IMPORTANT]
> **Document lifecycle:** `draft v0.2`  
> **Component maturity:** README-only at the directly inspected umbrella implementation probes; no supported family package, router, client, downloader, parser, admission decision, test lane, or lifecycle handoff is verified here  
> **Family posture:** NASA promotion remains `DEFERRED` under `OPEN-DSC-14`; final flat-versus-nested product topology remains `CONFLICTED / NEEDS VERIFICATION`  
> **Authority:** implementation-boundary documentation inside `connectors/`; no source, credential, schema, policy, registry, evidence, lifecycle, release, routing, or publication authority

> [!CAUTION]
> NASA access surfaces may require credentials, keys, bearer tokens, cookies, signed URLs, account agreements, or protected redirects. Never commit, log, serialize, fixture, expose to a browser, or place in an error message any credential value, authorization header, cookie, token cache, private redirect, signed URL, or protected payload.

![status](https://img.shields.io/badge/status-draft-yellow?style=flat-square)
![maturity](https://img.shields.io/badge/maturity-README--only-lightgrey?style=flat-square)
![family](https://img.shields.io/badge/family-DEFERRED-orange?style=flat-square)
![topology](https://img.shields.io/badge/topology-MIXED%20%2F%20CONFLICTED-orange?style=flat-square)
![lifecycle](https://img.shields.io/badge/output-RAW%20%7C%20QUARANTINE-blue?style=flat-square)
![publication](https://img.shields.io/badge/publication-NOT%20AUTHORIZED-critical?style=flat-square)

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [What belongs](#what-belongs-here) · [What does not](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed) · [Topology](#product-lanes-and-path-topology) · [Shared boundary](#shared-family-convention-boundary) · [Source roles](#product-identity-and-source-role-discipline) · [Access](#access-authentication-and-secret-boundary) · [Operations](#endpoint-format-cadence-and-resilience-posture) · [Lifecycle](#lifecycle-and-quarantine-boundary) · [Identity](#identity-hashing-deduplication-and-replay) · [Fixtures](#no-network-fixture-strategy) · [Activation](#activation-promotion-and-publication) · [Evidence](#evidence-basis) · [Rollback](#correction-rollback-and-deactivation) · [Backlog](#verification-backlog) · [Done](#definition-of-done)

---

## Purpose

`connectors/nasa/` currently provides an umbrella documentation boundary for possible NASA Earth-observation connector-family coordination.

This README exists to:

- prevent the folder from being mistaken for a canonical, implemented, or activated NASA connector family;
- expose the unresolved relationship between flat `connectors/nasa-*` lanes and nested `connectors/nasa/*` lanes;
- route maintainers to product-specific boundaries without collapsing product identity, source role, access class, rights, sensitivity, cadence, uncertainty, quality flags, or correction state;
- keep common server-side safety and source-admission conventions distinct from product-specific facts;
- constrain any future connector-family output to secret-free source references, run-local process evidence, or caller-owned RAW/QUARANTINE handoff candidates;
- keep connector activity upstream of normalization, EvidenceBundle closure, cataloging, promotion, release, public API/UI behavior, and AI interpretation.

This README does not promote NASA under Directory Rules §7.3, choose the canonical product topology, establish current upstream details, activate a source, validate a credential, or prove runtime behavior.

[Back to top](#top)

---

## Authority level

| Concern | Status | Evidence-bounded determination |
|---|---:|---|
| Owning responsibility root | **CONFIRMED** | Both inspected Directory Rules files assign source-specific fetch and admission to `connectors/`; connector outputs stop at RAW or QUARANTINE and connectors do not publish. |
| Current umbrella path | **CONFIRMED** | `connectors/nasa/README.md` exists at prior blob `d8eea51b…`. |
| NASA family promotion | **DEFERRED** | `OPEN-DSC-14` requires an ADR per family gated on populated connector and family-registry companions. Folder presence is explicitly insufficient. |
| Family registry companion | **NOT FOUND AT NAMED PATH** | `data/registry/sources/nasa/README.md` returned Not Found at the pinned base. This does not prove every possible NASA descriptor is absent. |
| Product topology | **CONFLICTED / MIXED** | All four flat product READMEs exist; nested HLS and SMAP READMEs exist; named nested Earthdata and FIRMS README paths were absent. No accepted topology decision was found. |
| Umbrella implementation | **NOT ESTABLISHED** | Named conventional package, module, and test probes were absent. Differently named or deeper content remains `UNKNOWN`. |
| Machine authority / activation | **NOT ESTABLISHED** | `control_plane/source_authority_register.yaml` contains `entries: []`. Product placeholder YAMLs do not grant authority. |
| SourceDescriptor schema authority | **CONFLICTED** | The populated singular schema names a plural path as canonical, while the plural schema is an almost-empty permissive PROPOSED scaffold. |
| Directory Rules placement | **CONFLICTED** | Architecture and doctrine copies carry different version/status metadata. Their connector and §15 folder-README rules agree, but this README does not choose the authoritative file location. |
| Rights and sensitivity enforcement | **UNKNOWN** | No NASA-family executable rights or sensitivity decision was verified. Product review remains required. |
| CI enforcement | **TODO-ONLY** | The inspected connector and SourceDescriptor workflows echo TODO steps and do not prove substantive validation. |
| Public output | **NOT AUTHORIZED** | This family boundary creates no claim, alert, map, API payload, EvidenceBundle, release, or publication artifact. |

Documentation may explain the boundary. It cannot substitute for accepted placement governance, conforming SourceDescriptors, machine activation, policy decisions, executable tests, lifecycle evidence, or release review.

[Back to top](#top)

---

## Status

### Bounded repository snapshot

| Surface inspected at `main@1c776e17922b…` | Status | Safe conclusion |
|---|---:|---|
| This README | **CONFIRMED v0.1** | A draft umbrella boundary exists; implementation does not follow from it. |
| Umbrella conventional probes | **NOT FOUND AT NAMED PATHS** | No `pyproject.toml`, `src/nasa/__init__.py`, `tests/README.md`, or root `__init__.py` was found. |
| Flat Earthdata lane | **CONFIRMED README** | An access-surface boundary exists at `connectors/nasa-earthdata/`. |
| Flat FIRMS lane | **CONFIRMED README** | A candidate-detection boundary exists at `connectors/nasa-firms/`. |
| Flat HLS lane | **CONFIRMED README** | A detailed HLS source-admission boundary exists at `connectors/nasa-hls/`. |
| Nested HLS lane | **CONFIRMED COMPATIBILITY README** | A nested compatibility address exists and records the topology conflict. |
| Flat SMAP lane | **CONFIRMED README** | A detailed SMAP product boundary exists at `connectors/nasa-smap/`. |
| Nested SMAP lane | **CONFIRMED README** | A second SMAP boundary exists under this family path. |
| Nested Earthdata and FIRMS probes | **NOT FOUND AT NAMED PATHS** | Exact `earthdata/README.md` and `firms/README.md` probes were absent; exhaustive absence is not claimed. |
| NASA source catalog family page | **DRAFT / PROPOSED** | Product grouping and open questions are documented; machine authority is not established. |
| Machine source-authority register | **CONFIRMED EMPTY** | No NASA source is activated or assigned authority there. |
| HLS and SMAP registry YAMLs | **CONFIRMED PLACEHOLDERS** | Candidate filenames exist; they are not conforming SourceDescriptors or activation entries. |
| NASA family registry README | **NOT FOUND AT NAMED PATH** | The companion named by the promotion gate is not satisfied by the inspected path. |
| CODEOWNERS | **PLACEHOLDER** | A global team is named; no connector- or NASA-specific ownership rule exists. |
| Connector and descriptor workflows | **TODO-ONLY** | Workflow presence does not prove connector behavior or descriptor validity. |
| Drift register | **NO NASA MATCH IN BOUNDED TEXT SCAN** | No NASA-specific entry was found by the inspected match; this is not a complete drift audit. |

These observations are pinned to the evidence snapshot. They do not claim a complete recursive inventory, build result, deployed state, external provider state, or current rights determination.

[Back to top](#top)

---

## What belongs here

While this family remains deferred and README-only, accepted content is limited to:

- this folder boundary and navigation to product-specific connector lanes;
- a topology decision, migration pointer, or compatibility marker after it is authorized by an accepted ADR or migration plan;
- documented shared invariants that are demonstrably common to every participating NASA product lane;
- reviewed family-level security helpers only after code reuse, ownership, package placement, tests, and rollback are established;
- routing metadata that preserves the selected product identity and delegates to exactly one owning product lane;
- secret-free common request correlation, error classification, or process-evidence structures after their contracts are accepted;
- tests proving that shared code cannot collapse product roles, leak credentials, bypass activation, or publish.

Common code belongs here only when multiple NASA product lanes actually consume it and one owner can maintain it without duplicating product-specific behavior.

[Back to top](#top)

---

## What does NOT belong here

Do not place here:

- a second implementation for a product already assigned to a flat or nested lane;
- product endpoints, collection identifiers, versions, quality semantics, cadence, quotas, or rights copied from product authorities;
- credentials, keys, tokens, cookies, signed URLs, private redirects, secret caches, or protected payloads;
- SourceDescriptors, source-authority entries, activation decisions, registry truth, policy, schemas, or semantic contracts;
- product-specific parsers, QA decoders, fixtures, or tests unless an accepted topology makes this their single owning path;
- normalized domain values, resampled rasters, merged detections, event clusters, drought claims, crop claims, or public-safe layers;
- RAW, QUARANTINE, WORK, PROCESSED, CATALOG, TRIPLET, PUBLISHED, proof, receipt, or release data inside the connector folder;
- EvidenceBundles, promotion decisions, release manifests, correction notices, public routes, maps, alerts, summaries, or AI-ready payloads;
- language implying that NASA is one evidence role, one license, one sensitivity tier, one freshness class, or one publication class;
- compatibility shims that can evolve independently from a single canonical product owner.

Do not use this README to ratify a family, choose a path, activate a source, or waive product-specific review.

[Back to top](#top)

---

## Inputs

### Current inputs

The current folder accepts maintainer-authored documentation only. No executable family-level input contract is established.

### Required future inputs

A future family coordinator may accept only reviewed, product-preserving inputs such as:

- an accepted family/topology ADR and migration state;
- a product-lane identifier that resolves to exactly one owner;
- a conforming product-specific SourceDescriptor and machine activation reference;
- caller-owned run identity and RAW/QUARANTINE destination intent;
- product-scoped request parameters allowed by descriptor and policy;
- server-side credential references, never secret values in request payloads;
- product-specific rights, sensitivity, freshness, access, and admissibility decisions by reference;
- bounded timeout, retry, rate, size, redirect, and parser limits;
- implementation/spec version and replay context.

An umbrella request without a product identity must fail closed. The family layer must not infer a product from file shape, endpoint host, or caller preference.

[Back to top](#top)

---

## Outputs

### Current outputs

This folder currently emits no runtime output. This README is its only confirmed artifact at the directly inspected umbrella implementation probes.

### Permitted future outputs

A future reviewed family coordinator may return only:

- a deterministic route to one product connector owner;
- a secret-free request correlation or error result;
- source reference or discovery metadata that preserves product identity;
- caller-owned RAW or QUARANTINE handoff candidates;
- process evidence recording descriptor, activation, policy, request, checksum, retry, and disposition references without secret material.

It must not emit normalized truth, catalog records, public claims, alerts, maps, API responses, EvidenceBundles, promotion decisions, release artifacts, or correction decisions.

[Back to top](#top)

---

## Validation

| Check | Current result | Required durable mechanism |
|---|---:|---|
| §15 folder README order | **DOCUMENTED** | Markdown structure validator and review. |
| Product-lane links | **REPOSITORY-RESOLVED FOR THIS REVISION** | Link checker pinned to a reviewed commit. |
| Family promotion | **DEFERRED** | Accepted ADR plus required connector/registry companion evidence. |
| Topology uniqueness | **FAILS CURRENTLY / CONFLICTED** | Migration manifest and tests proving one owning implementation per product. |
| Umbrella package build/import | **NOT ESTABLISHED** | Package metadata, isolated build, import test, and dependency review. |
| Product-role preservation | **DOCUMENTED ONLY** | Negative routing, fixture, and downstream contract tests. |
| SourceDescriptor validation | **NOT ESTABLISHED** | Settled schema authority, fixtures, and substantive validator CI. |
| Machine activation | **NOT ESTABLISHED** | Reviewed source-authority entries tied to descriptors and policy. |
| Secret handling | **NOT ESTABLISHED** | Redaction, browser-boundary, log, fixture, redirect, and error tests. |
| RAW/QUARANTINE boundary | **DOCUMENTED ONLY** | Sink integration tests and lifecycle assertions. |
| Retry, rate, timeout, and outage behavior | **UNKNOWN** | Deterministic no-network tests with reviewed budgets. |
| Rights/sensitivity enforcement | **UNKNOWN** | Product-specific decisions and deny/quarantine tests. |
| Connector/descriptor workflows | **TODO-ONLY** | Real commands, negative fixtures, stable exit codes, and required checks. |
| No publication | **DOCUMENTED ONLY** | Dependency, route, sink, and release-gate tests. |

Documentation checks do not prove live source access, product correctness, executable admission, or publication safety.

[Back to top](#top)

---

## Review burden

Changes require review appropriate to their effect:

- **README-only boundary changes:** connector, NASA source, affected product/domain, validation, and docs reviewers;
- **family placement or topology:** docs/doctrine steward plus accepted ADR review;
- **shared code or routing:** connector, product, security, test, and operations reviewers;
- **credentials or protected access:** security review and secret-leak tests;
- **rights, redistribution, attribution, or retention:** rights reviewer and affected source steward;
- **sensitive joins or public exposure:** sensitivity, domain, governance, and release reviewers;
- **SourceDescriptor or schema changes:** source, contract, schema, policy, registry, and migration reviewers;
- **RAW/QUARANTINE handoff changes:** lifecycle, data, connector, and validation reviewers;
- **public or release impact:** governed API, evidence, policy, release, and correction reviewers.

The current [CODEOWNERS](../../.github/CODEOWNERS) file is a greenfield placeholder and has no connector- or NASA-specific rule. `OWNER_TBD` therefore remains a blocking ownership gap, not an assignment.

[Back to top](#top)

---

## Related folders

### Connector boundaries

- [`connectors/`](../README.md) — source-admission root boundary.
- [`connectors/nasa-earthdata/`](../nasa-earthdata/README.md) — Earthdata access/discovery boundary.
- [`connectors/nasa-firms/`](../nasa-firms/README.md) — FIRMS candidate-detection boundary.
- [`connectors/nasa-hls/`](../nasa-hls/README.md) — flat HLS source-admission boundary.
- [`connectors/nasa/hls/`](./hls/README.md) — nested HLS compatibility boundary.
- [`connectors/nasa-smap/`](../nasa-smap/README.md) — flat SMAP product boundary.
- [`connectors/nasa/smap/`](./smap/README.md) — nested SMAP product boundary.

### Governance and source documentation

- [Directory Rules — architecture path](../../docs/architecture/directory-rules.md) and [doctrine path](../../docs/doctrine/directory-rules.md) — matching connector/README rules with unresolved placement/version drift.
- [Source catalog open questions](../../docs/sources/catalog/OPEN-QUESTIONS.md) — `OPEN-DSC-14` promotion gate.
- [NASA source-family catalog](../../docs/sources/catalog/nasa/README.md) and product pages for [Earthdata](../../docs/sources/catalog/nasa/nasa-earthdata.md), [FIRMS](../../docs/sources/catalog/nasa/nasa-firms.md), [HLS](../../docs/sources/catalog/nasa/nasa-hls.md), and [SMAP](../../docs/sources/catalog/nasa/nasa-smap.md).
- [SourceDescriptor standard](../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md), [contract](../../contracts/source/source_descriptor.md), [singular schema](../../schemas/contracts/v1/source/source_descriptor.schema.json), and [plural schema](../../schemas/contracts/v1/sources/source_descriptor.schema.json).
- [Machine source-authority register](../../control_plane/source_authority_register.yaml).
- [Source policy](../../policy/source/README.md), [rights policy](../../policy/rights/README.md), and [sensitivity policy](../../policy/sensitivity/README.md).

### Product registry placeholders

- [Agriculture HLS placeholder](../../data/registry/sources/agriculture/nasa_hls.yaml).
- [Soil SMAP placeholder](../../data/registry/sources/soil/nasa-smap.yaml).
- Agriculture SMAP [hyphenated](../../data/registry/sources/agriculture/nasa-smap.yaml) and [underscored](../../data/registry/sources/agriculture/nasa_smap.yaml) placeholders.

These links are evidence pointers, not a claim that every referenced artifact is canonical, complete, compatible, or active.

[Back to top](#top)

---

## ADRs

- No accepted NASA-family promotion or product-topology ADR was identified in the inspected evidence.
- `OPEN-DSC-14` is a deferred register item, not an accepted ADR. Its resolution path calls for an ADR per family and required companion state.
- [ADR-0012](../../docs/adr/ADR-0012-connector-outputs-to-data-raw-or-data-quarantine-only.md) documents the RAW/QUARANTINE connector boundary but remains draft/proposed in the inspected repository; this README relies on the matching Directory Rules §7.3 rule rather than treating the ADR as accepted.
- A future decision must address NASA family placement, flat/nested product ownership, compatibility behavior, import and fixture routing, migration order, sunset criteria, and rollback.
- The Directory Rules file-location conflict and SourceDescriptor schema-path conflict may require separate governance; this README records but does not resolve them.

[Back to top](#top)

---

## Last reviewed

**2026-07-14** against `bartytime4life/Kansas-Frontier-Matrix` at `main@1c776e17922b5c19ed2337b559d18d8c947e7c63`.

Review scope was repository documentation, named conventional probes, machine registry state, placeholder product records, ownership, and generic connector/descriptor workflows. It did not include a complete recursive tree, dependency installation, package build, live NASA access, credential test, external terms review, deployment inspection, or release audit.

[Back to top](#top)

---

## Product lanes and path topology

| Product/surface | Flat lane | Nested lane | Repository-documented boundary | Topology posture |
|---|---|---|---|---:|
| Earthdata | [`connectors/nasa-earthdata/`](../nasa-earthdata/README.md) | Exact `connectors/nasa/earthdata/README.md` probe not found | Access and discovery surface; not itself a measurement product or evidence role. | **FLAT README CONFIRMED / FINAL PLACEMENT DEFERRED** |
| FIRMS | [`connectors/nasa-firms/`](../nasa-firms/README.md) | Exact `connectors/nasa/firms/README.md` probe not found | Candidate remote-sensing detections; no fire confirmation, warning, or alert authority. | **FLAT README CONFIRMED / FINAL PLACEMENT DEFERRED** |
| HLS | [`connectors/nasa-hls/`](../nasa-hls/README.md) | [`connectors/nasa/hls/`](./hls/README.md) | Source imagery/context boundary; nested lane is documented as compatibility/transitional. | **DUPLICATE PATH / CONFLICTED** |
| SMAP | [`connectors/nasa-smap/`](../nasa-smap/README.md) | [`connectors/nasa/smap/`](./smap/README.md) | Product-specific soil-moisture boundary preserving observation/model, layer, cadence, and grid distinctions. | **DUPLICATE PATH / CONFLICTED** |

The named nested Earthdata and FIRMS absences are bounded. The table does not prove no differently named or deeper content exists.

Until governance resolves the topology:

- do not add an umbrella router that makes placement look settled;
- do not mirror product implementations into both flat and nested lanes;
- do not move or delete a compatibility address without a reference and migration audit;
- do not infer that the flat-only named paths are canonical merely because a nested README was not found;
- keep each product README explicit about whether it is substantive, compatibility-only, transitional, or unresolved;
- record path drift rather than smoothing it into a single undocumented convention.

[Back to top](#top)

---

## Shared family convention boundary

### Potentially shareable after review

The family may eventually centralize only conventions proven common across participating product lanes:

- server-side credential-reference interfaces and redaction hooks;
- request correlation and secret-free structured errors;
- finite result classes such as success, unchanged, stale, unavailable, denied, rate-limited, malformed, integrity-failed, and quarantined;
- deterministic retry/backoff interfaces with product-supplied budgets;
- checksum and source-head evidence envelopes;
- common route registration that preserves one product owner;
- tests asserting no browser access, no downstream lifecycle writes, and no publication.

### Must remain product-specific

The family must not own or flatten:

- provider/DAAC, product, collection, granule, instrument, processing level, version, layer, cadence, grid, or temporal semantics;
- authentication method, endpoint/redirect allowlist, pagination, quotas, formats, parser rules, size limits, or source-head behavior;
- source type, source role, authority rank, uncertainty, quality flags, fill/no-data semantics, or correction/supersession state;
- rights, attribution, redistribution, retention, sensitivity, citation, or public-release class;
- downstream normalization, domain interpretation, evidence closure, catalog profiles, release, or correction behavior.

If a proposed shared helper requires product branching throughout its implementation, it likely belongs in product lanes or a reviewed shared package rather than this family folder.

[Back to top](#top)

---

## Product identity and source-role discipline

Repository documentation currently distinguishes the lanes as follows:

- **Earthdata** is an access/discovery surface. Authentication success or metadata discovery is not a measurement, claim, source authority, or publication decision.
- **FIRMS** supplies candidate remote-sensing detections. A detection is not a confirmed fire, incident, warning, emergency alert, or tactical local-condition statement.
- **HLS** supplies source imagery or context candidates. A reflectance or vegetation-index value does not become an agricultural claim without downstream masks, QA, provenance, and governed interpretation.
- **SMAP** includes product candidates whose observation/model, surface/root-zone, near-real-time/reprocessed, version, grid, and temporal distinctions must remain explicit. Model-assimilated material is not silently relabeled as raw in-situ measurement.

These statements summarize current repository boundaries; they do not replace product SourceDescriptors or current upstream documentation.

The family layer must never:

- assign one `NASA` source role to every product;
- treat access metadata as measurement truth;
- promote remote-sensing candidates into confirmed events or domain conclusions;
- silently merge products, layers, cadence classes, grids, versions, or corrections;
- silently join NASA material with in-situ, private, sensitive, or other-provider data;
- upgrade a successful request into evidence closure, release eligibility, or public truth.

[Back to top](#top)

---

## Access, authentication, and secret boundary

No family-level credential names, secret provider, token flow, endpoint allowlist, redirect policy, or authentication implementation is established by this README.

Any future implementation must:

- accept server-side secret references rather than raw credentials in public or persisted request objects;
- scope credentials and caches by product/provider boundary;
- use approved hosts and bounded redirects;
- prevent protocol downgrade, arbitrary-host fetches, and caller-controlled credential forwarding;
- redact authorization headers, keys, tokens, cookies, signed query strings, private paths, and protected payload excerpts from logs, errors, metrics, fixtures, receipts, and telemetry;
- keep browser, map, public API, export, and AI clients outside protected NASA access flows;
- define rotation, revocation, expiry, invalid-credential, clock-skew, and partial-outage behavior;
- fail closed when product identity, credential scope, rights, sensitivity, or destination intent is unresolved.

Do not invent environment-variable names in documentation before configuration authority and secret-provider integration are reviewed.

[Back to top](#top)

---

## Endpoint, format, cadence, and resilience posture

Current family-level endpoints, protocols, formats, pagination, cadence, quotas, and resilience budgets are intentionally undefined. Those values belong to reviewed product-specific authority.

| Concern | Current status | Evidence required before implementation claim |
|---|---:|---|
| Product/provider selection | **NEEDS VERIFICATION** | Product-specific descriptor and current authoritative source documentation. |
| Authentication and credential scope | **NOT ESTABLISHED** | Security-reviewed server-side contract and leak tests. |
| Endpoint and redirect allowlists | **UNKNOWN** | Product-specific approved hosts and redirect-denial tests. |
| Protocol, format, and parser | **NEEDS VERIFICATION** | Pinned product/version docs, parser limits, and rights-cleared fixtures. |
| Discovery, pagination, and ordering | **UNKNOWN** | Deterministic contract and duplicate/missing-page tests. |
| Cadence, freshness, and stale state | **NEEDS VERIFICATION** | Descriptor values and fail-closed stale/outage policy. |
| Quotas and rate limits | **UNKNOWN** | Current provider terms and reviewed budgets per product. |
| Timeouts and retries | **NOT DEFINED** | Per-attempt/total budgets, jitter, retryability matrix, and tests. |
| Circuit breaking and recovery | **NOT DEFINED** | State contract, operator visibility, half-open behavior, and recovery tests. |
| Source corrections and supersession | **NEEDS VERIFICATION** | Product identity, source-head, correction, and lineage contracts. |

The family layer may standardize interfaces but must not apply one budget or cadence to every product. An outage or empty response must never become a public “no data,” “no fire,” “no drought,” or “no change” claim.

[Back to top](#top)

---

## Lifecycle and quarantine boundary

Directory Rules §7.3 constrains connectors to source-specific fetch and admission. Any future family-level coordination may route or prepare candidates only for caller-owned RAW or QUARANTINE destinations.

A future RAW candidate should require, at minimum:

- resolved product owner, conforming descriptor, machine activation, and destination intent;
- permitted provider, product, collection, version, layer, cadence, format, grid, and request scope;
- resolved rights, attribution, redistribution, retention, sensitivity, and citation posture;
- approved endpoint/redirect path and successful secret redaction;
- media-type, size, archive, parser, checksum, and content-identity validation;
- retrieval time, source-head/upstream version evidence, and run identity;
- product-specific QA and no-data metadata preserved without interpretation.

Quarantine is required when product identity, topology, descriptor, activation, access, rights, sensitivity, format, size, parser, integrity, cadence, layer, grid, temporal metadata, destination, or source drift cannot be resolved safely.

The family boundary must not write WORK, PROCESSED, CATALOG, TRIPLET, PUBLISHED, proof, receipt, or release objects as a substitute for downstream systems. Connector activity is not publication authority.

[Back to top](#top)

---

## Identity, hashing, deduplication, and replay

Identity must be product-specific before it is family-aggregated. The exact formula remains `NEEDS VERIFICATION` pending settled descriptors and identity contracts.

Required properties:

- include product/provider identity before collection, granule, processing level, version, layer, cadence, grid, and upstream revision identity;
- never deduplicate across products merely because bytes, timestamps, coordinates, filenames, or hostnames match;
- hash fetched bytes with the repository-approved algorithm and preserve checksum evidence;
- distinguish identical bytes from conflicting bytes under the same product-scoped upstream identity;
- make discovery and pagination ordering deterministic;
- support replay from pinned descriptor, activation, product route, request, source-head, implementation, and checksum evidence;
- record repeated unchanged retrievals as explicit no-ops rather than duplicate admissions;
- exclude secrets and signed URLs from IDs, hashes, logs, and process evidence;
- preserve corrections and supersession without silently overwriting prior runs.

[Back to top](#top)

---

## Normalization and downstream responsibility

This family boundary may eventually route source-native candidates. It must not:

- parse product values into a common NASA domain model that erases product meaning;
- resample, reproject, aggregate, cluster, mask, classify, compare, calibrate, or infer domain conditions;
- merge products, providers, in-situ measurements, private data, or sensitive joins;
- create STAC, DCAT, PROV, EvidenceBundle, catalog, proof, release, public map, API, UI, alert, or AI output;
- decide that a source correction changes a public release.

Product connectors preserve and admit source candidates. Reviewed pipelines, contracts, policies, evidence systems, and release systems own downstream transformation and truth decisions.

[Back to top](#top)

---

## Receipts, evidence, and emitted artifacts

A future family route or shared helper should preserve enough secret-free process evidence for review:

- family and product route identity;
- descriptor and activation references;
- request identity and caller-owned destination intent;
- provider/product/collection/version/layer/cadence/grid identifiers supplied by the product lane;
- retrieval start/end time and finite result class;
- policy-safe status, redirect, size, media-type, and source-head evidence;
- checksum and checksum-manifest reference;
- retry, rate-limit, timeout, no-op, outage, and circuit state;
- rights and sensitivity decision references without duplicated policy;
- RAW/QUARANTINE handoff, deny, or no-op reference;
- implementation/spec version and replay inputs.

These are process records, not EvidenceBundles, proof packs, release manifests, public citations, or claims. Their canonical schema and storage location must be established outside this folder.

[Back to top](#top)

---

## No-network fixture strategy

Default tests must not require NASA credentials, live upstream access, mutable provider state, or protected payloads.

A future fixture suite should include small synthetic or explicitly rights-cleared cases for:

- valid routing to each product owner and failure for unknown/ambiguous products;
- flat/nested compatibility behavior and single-owner enforcement;
- Earthdata access metadata without measurement-role promotion;
- FIRMS candidate detections without confirmation or alert promotion;
- HLS source/context metadata without domain-claim promotion;
- SMAP observation/model, surface/root-zone, and NRT/reprocessed distinctions;
- pagination, deterministic ordering, duplicate pages, and unchanged discovery;
- fictional redirect allow/deny behavior;
- media-type, checksum, truncation, archive-bomb, oversized-object, and malformed-content failures;
- product identity collision, identical duplicate bytes, and conflicting duplicate bytes;
- stale, outage, rate-limit, timeout, retry-exhausted, and circuit-open states;
- missing descriptor, inactive source, unresolved rights/sensitivity, and schema drift;
- credential, key, token, cookie, signed-URL, and protected-header redaction;
- RAW handoff success and deterministic QUARANTINE outcomes;
- assertions that no downstream lifecycle, proof, release, alert, or public output is written.

Live probes, if later authorized, belong in separate manual or scheduled lanes with explicit terms, budgets, logging controls, source scope, and no publication side effects.

[Back to top](#top)

---

## Activation, promotion, and publication

The NASA family and its product connectors must remain inactive until all applicable gates pass:

- `OPEN-DSC-14` is resolved by an accepted family-placement ADR;
- required family connector and registry companion state is populated or an accepted alternative is documented;
- final flat/nested topology, compatibility routes, imports, fixtures, tests, sunset, and rollback are accepted;
- every selected product has a conforming SourceDescriptor against one settled schema authority;
- the machine source-authority register records approved product roles and activation state;
- product-specific rights, attribution, redistribution, retention, access, sensitivity, and citation are reviewed;
- providers, products, collections, versions, layers, cadence classes, grids, and source roles are pinned;
- credential handling and endpoint/redirect allowlists are security reviewed;
- no-network fixtures and negative tests exist;
- parser limits, retries, timeouts, rate handling, checksums, quarantine, and replay pass;
- RAW/QUARANTINE sinks and secret-free process evidence are proven;
- downstream compatibility is tested without granting connector normalization or publication authority;
- connector and descriptor CI execute substantive checks rather than TODO echoes;
- owners and review burden are assigned.

Family promotion is a placement decision. Source activation is a machine authority decision. Admission is a lifecycle action. Promotion and publication are downstream governance actions. None implies the next.

Watchers, access surfaces, routers, and connectors are not publication authorities.

[Back to top](#top)

---

## Rights, attribution, sensitivity, and public safety

No single NASA-family rights, attribution, redistribution, retention, access, sensitivity, citation, or public-release posture is established by this README.

Before product activation, authoritative records must answer:

- which provider, product, version, and access terms apply;
- whether account acceptance, keys, agreements, or other restrictions apply;
- whether KFM may retain, transform, cache, mirror, redistribute, or publish source or derived artifacts;
- required attribution and citation;
- whether protected distribution references impose handling limits;
- whether product precision or joins with private fields, infrastructure, archaeological sites, rare species, people, or other sensitive data raise the sensitivity floor;
- how upstream corrections, reprocessing, withdrawal, or retirement affect retained and released artifacts.

Public-sector origin does not by itself prove unrestricted redistribution. Coarse or remote-sensing data does not eliminate sensitivity introduced by downstream joins. When rights or sensitivity is unclear, quarantine, restrict, generalize, delay, deny, or abstain rather than assume.

[Back to top](#top)

---

## Evidence basis

| Evidence | Status | Supports | Does not prove |
|---|---:|---|---|
| Target README at pinned base | **CONFIRMED** | v0.1 exists at blob `d8eea51b…`. | Runtime, family promotion, activation, or topology. |
| Exact umbrella probes | **CONFIRMED BOUNDED RESULT** | Named package, module, and test paths were absent. | Exhaustive recursive absence of implementation. |
| Two Directory Rules files | **CONFIRMED CONFLICT + MATCHING RULES** | `connectors/` is source admission; outputs stop at RAW/QUARANTINE; §15 order applies. | Accepted canonical Directory Rules file location. |
| `OPEN-DSC-14` | **CONFIRMED DEFERRED** | Family promotion requires an ADR and companion state; folder presence is insufficient. | Future resolution or promotion. |
| NASA catalog family page | **CONFIRMED DRAFT DOCUMENT** | Four product groupings and proposed placement options are documented. | Machine authority, current upstream facts, or accepted topology. |
| Flat product READMEs | **CONFIRMED** | Earthdata, FIRMS, HLS, and SMAP boundaries exist. | Executable product connectors or canonical placement. |
| Nested HLS and SMAP READMEs | **CONFIRMED** | Duplicate/compatibility path questions exist. | Which path owns implementation. |
| Named nested Earthdata/FIRMS probes | **NOT FOUND** | Exact README paths were absent. | Exhaustive absence or flat-path canonicality. |
| Machine source-authority register | **CONFIRMED EMPTY** | No NASA product authority/activation entry exists there. | Future or external authority. |
| HLS/SMAP registry YAMLs | **CONFIRMED PLACEHOLDERS** | Candidate names and source-doc pointers exist. | Conforming descriptors, authority, or activation. |
| Singular/plural SourceDescriptor schemas | **CONFIRMED CONFLICT** | Populated legacy path points to an almost-empty canonical scaffold. | Accepted schema authority or validator behavior. |
| CODEOWNERS | **CONFIRMED PLACEHOLDER** | Global ownership placeholder exists. | Accepted connector/NASA owners. |
| Connector/descriptor workflows | **CONFIRMED TODO-ONLY** | Workflow names and triggers exist. | Substantive validation or enforcement. |

Where documentation and machine authority conflict or remain absent, this README narrows the claim and defers implementation or activation.

[Back to top](#top)

---

## Correction, rollback, and deactivation

### Documentation rollback

This v0.2 revision can be reversed by restoring:

```text
repository: bartytime4life/Kansas-Frontier-Matrix
base commit: 1c776e17922b5c19ed2337b559d18d8c947e7c63
prior blob: d8eea51b9205865de0ea1545e75404ee8c48001c
path: connectors/nasa/README.md
```

Rollback changes only this README. It must not delete product lanes, compatibility addresses, source documentation, registry lineage, or release history.

### Future family deactivation

A future family coordinator should support fail-closed pause or deactivation when:

- family placement, topology, compatibility routing, product ownership, or schema authority changes incompatibly;
- provider, product, version, endpoint, format, rights, access, attribution, redistribution, retention, or sensitivity posture changes;
- credentials or secret handling is compromised;
- product identity, source role, QA, cadence, layer, grid, or temporal semantics drift;
- repeated integrity, parser, timeout, rate-limit, or outage failures exceed reviewed thresholds;
- descriptor, policy, schema, activation, fixture, validator, or CI state becomes invalid;
- flat and nested lanes diverge or route to more than one implementation;
- upstream correction, withdrawal, or KFM review requires a hold.

Deactivation stops new routing/admission. It does not silently delete prior RAW evidence, overwrite lineage, retract a release, or correct a public claim. Release and correction systems own those actions.

[Back to top](#top)

---

## Verification backlog

| Item | Status | Evidence required to close |
|---|---:|---|
| Resolve NASA family promotion under `OPEN-DSC-14`. | **DEFERRED** | Accepted ADR and required connector/registry companion state or accepted alternative. |
| Resolve family-level Directory Rules path/version authority. | **CONFLICTED** | Accepted placement decision, canonical pointer, migration, and link updates. |
| Resolve flat versus nested product topology. | **CONFLICTED** | ADR/migration plan with one owner per product, compatibility behavior, tests, sunset, and rollback. |
| Produce a complete recursive NASA connector inventory. | **NEEDS VERIFICATION** | Non-truncated tree/contents receipt at a pinned commit. |
| Assign family, product, security, rights, sensitivity, test, and docs owners. | **NEEDS VERIFICATION** | CODEOWNERS or approved ownership record. |
| Resolve singular/plural SourceDescriptor schema authority. | **CONFLICTED** | Accepted migration, populated canonical schema, fixtures, validator, and parity tests. |
| Create a NASA family registry companion or approve an alternative. | **NOT ESTABLISHED** | Accepted promotion decision and reviewed registry structure. |
| Replace product placeholder YAMLs with conforming descriptors or retire them. | **NEEDS VERIFICATION** | Registry decision, validated descriptors, naming migration, and review. |
| Populate machine source-authority state for approved products. | **NOT STARTED** | Reviewed authority/activation entries tied to descriptors and policy. |
| Pin product/provider/version/layer/cadence/source-role selections. | **NEEDS VERIFICATION** | Current authoritative review and approved descriptors per product. |
| Verify access, endpoints, redirects, formats, paging, quotas, and terms. | **NEEDS VERIFICATION** | Current authoritative product documentation, security/rights review, and tests. |
| Define per-product timeout, retry, rate, circuit, and size budgets. | **NEEDS VERIFICATION** | Reviewed configuration contracts and deterministic tests. |
| Establish safe no-network fixtures and negative cases. | **NOT ESTABLISHED** | Fixture registry, rights record, test consumers, and leak checks. |
| Implement single-owner routing and product-role preservation. | **NOT ESTABLISHED** | Code, package metadata, imports, fixtures, and negative routing tests. |
| Implement RAW/QUARANTINE handoff and secret-free process evidence. | **NOT ESTABLISHED** | Contracts/schemas, sink tests, process records, and boundary tests. |
| Implement substantive connector and descriptor CI. | **NOT ESTABLISHED** | Workflows invoking real tests/validators with negative-state coverage. |
| Prove no connector/browser/public-path access and no connector publication. | **NEEDS VERIFICATION** | Architecture, dependency, route, sink, and release-gate tests. |
| Verify product-specific rights, attribution, sensitivity, correction, and deactivation. | **NEEDS VERIFICATION** | Policy decisions and steward review. |

[Back to top](#top)

---

## Definition of done

This family boundary is not implementation-complete until all applicable criteria pass:

- [ ] An accepted ADR resolves NASA family placement and `OPEN-DSC-14`.
- [ ] Required connector and family-registry companion state exists or an accepted alternative is documented.
- [ ] One owning implementation path is defined for Earthdata, FIRMS, HLS, SMAP, and each future product.
- [ ] Compatibility paths have mechanically verified routes, sunset criteria, reference audits, and rollback.
- [ ] Product-specific SourceDescriptors validate against one accepted schema authority.
- [ ] Machine authority/activation entries exist for selected products and roles.
- [ ] Rights, attribution, redistribution, access, retention, sensitivity, citation, and correction postures are reviewed per product.
- [ ] Provider, product, collection, version, processing level, layer, cadence, grid, and temporal identities are pinned.
- [ ] Server-side credential handling, endpoint/redirect allowlists, parser limits, and secret-redaction tests pass.
- [ ] Product-scoped timeouts, retries, rate limits, circuit breaking, paging, checksums, and replay are deterministic and tested.
- [ ] No-network valid, invalid, collision, and golden fixtures exist with rights and provenance notes.
- [ ] Product routing preserves access/measurement, candidate/confirmed, context/claim, model/observation, layer, cadence, grid, and version distinctions.
- [ ] RAW and QUARANTINE handoffs are append-only, checksummed, and bounded by Directory Rules.
- [ ] Family and product connector outputs cannot reach downstream lifecycle, proof, release, public API/UI/map/alert, or AI surfaces.
- [ ] CI runs substantive tests and validators rather than TODO echoes.
- [ ] Owners, review burden, operational runbook, correction path, deactivation path, and rollback targets are assigned.
- [ ] Umbrella, flat, nested, catalog, registry, schema, policy, fixture, test, pipeline, and release documentation agree.

Until then, the honest status is **README-only / family promotion deferred / inactive / not publication-authorized**.

[Back to top](#top)

---

## Changelog

### v0.2 — 2026-07-14

- Replaced broad implementation uncertainty with a commit-pinned repository evidence snapshot.
- Recorded the deferred `OPEN-DSC-14` promotion gate and absent named NASA family registry companion.
- Recorded the mixed flat/nested topology: flat Earthdata/FIRMS/HLS/SMAP, nested HLS/SMAP, and absent named nested Earthdata/FIRMS README probes.
- Distinguished product README presence and placeholder registry filenames from implementation, conforming SourceDescriptors, authority, and activation.
- Surfaced the Directory Rules file-location/version conflict and singular/plural SourceDescriptor schema conflict without choosing a winner.
- Recorded the empty machine source-authority register, placeholder CODEOWNERS, and TODO-only connector/descriptor CI.
- Added the required §15 folder README sections in order.
- Added family/product role, shared-convention, credential, operational resilience, lifecycle, quarantine, identity/replay, fixture, activation, rights, rollback, deactivation, and definition-of-done boundaries.
- Preserved product anti-collapse rules: Earthdata access is not measurement; FIRMS detections are not confirmations or alerts; HLS context is not a domain claim; SMAP model/layer/cadence distinctions remain explicit.
- Changed no file except this README and granted no placement, implementation, source, registry, release, or publication authority.

### v0.1 — 2026-06-19

- Replaced a blank placeholder with the initial proposed NASA connector-family boundary.

---

## Maintainer note

Keep this family conservative. It may eventually share proven source-admission mechanics, but it must not flatten product identity, source role, rights, sensitivity, freshness, correction state, or lifecycle authority. A successful route or fetch is not evidence closure, release, or public truth.

<p align="right"><a href="#top">Back to top</a></p>
