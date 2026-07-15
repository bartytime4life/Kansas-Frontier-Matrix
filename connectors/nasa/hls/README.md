<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-nasa-hls-nested-readme
title: connectors/nasa/hls/ — NASA HLS Nested Compatibility Boundary
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · NASA/HLS source steward · Agriculture steward · Remote-sensing steward · Security reviewer · Rights reviewer · Sensitivity reviewer · Validation steward · Test steward · Docs steward
created: "NEEDS VERIFICATION — blank placeholder predates 2026-07-14"
updated: 2026-07-14
policy_label: public-doctrine; compatibility; transitional; duplicate-path-conflict; nasa-hls; readme-only; no-network; no-activation; raw-quarantine-only; no-publication
current_path: connectors/nasa/hls/README.md
truth_posture: CONFIRMED blank nested placeholder, substantive flat HLS README, NASA family README, Agriculture references to the nested path, placeholder source-registry record, empty machine source-authority register, documentation-only HLS-VI fixture lane, conflicted SourceDescriptor schema authority, TODO-only generic connector and descriptor CI, and current official NASA HLS product/access pages / CONFLICTED canonical flat-versus-nested HLS connector placement and SourceDescriptor schema path / PROPOSED documentation-only compatibility pointer pending ADR or migration / UNKNOWN recursive implementation inventory, runtime, credentials, endpoint policy, rights enforcement, executable fixtures/tests, lifecycle artifacts, deployment, release state, and owners
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 6d251686ac367cdb13bb88417bc46c0a78c5ebb3
  prior_blob: 8b137891791fe96927ad78e64b0aad7bded08bdc
  flat_reference_blob: c6a1726c6e11f164a8b8562f5bb9b7215100a0e1
related:
  - ../README.md
  - ../../README.md
  - ../../nasa-hls/README.md
  - ../../nasa-earthdata/README.md
  - ../../nasa-firms/README.md
  - ../../../CONTRIBUTING.md
  - ../../../.github/CODEOWNERS
  - ../../../.github/PULL_REQUEST_TEMPLATE.md
  - ../../../.github/workflows/connector-gate.yml
  - ../../../.github/workflows/source-descriptor-validate.yml
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/README.md
  - ../../../docs/registers/DRIFT_REGISTER.md
  - ../../../docs/sources/catalog/OPEN-QUESTIONS.md
  - ../../../docs/sources/catalog/nasa/README.md
  - ../../../docs/sources/catalog/nasa/nasa-hls.md
  - ../../../docs/domains/agriculture/SOURCE_REGISTRY.md
  - ../../../docs/domains/agriculture/SOURCES.md
  - ../../../pipelines/domains/agriculture/README.md
  - ../../../pipeline_specs/agriculture/README.md
  - ../../../fixtures/domains/agriculture/hls_vi/README.md
  - ../../../data/registry/sources/agriculture/nasa_hls.yaml
  - ../../../contracts/source/source_descriptor.md
  - ../../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../../schemas/contracts/v1/sources/source_descriptor.schema.json
  - ../../../control_plane/source_authority_register.yaml
  - ../../../policy/source/README.md
  - ../../../policy/rights/README.md
  - ../../../policy/sensitivity/README.md
  - https://hls.gsfc.nasa.gov/
  - https://hls.gsfc.nasa.gov/data-products/
  - https://hls.gsfc.nasa.gov/data-access-and-tools/
tags: [kfm, connectors, nasa, hls, compatibility, transitional, duplicate-path, readme-only, agriculture, remote-sensing, source-admission, raw, quarantine, governance]
notes:
  - "This document replaces a one-byte blank placeholder at connectors/nasa/hls/README.md."
  - "The substantive HLS source-admission boundary remains at connectors/nasa-hls/README.md; this revision does not select a canonical implementation path, mirror its full content, move files, or authorize implementation in both homes."
  - "Agriculture pipeline and pipeline-spec documentation reference this nested path, so deleting or silently repurposing it would create unresolved reference drift."
  - "Exact conventional probes beneath both HLS connector paths found no package metadata, source module, or test README at the pinned base. This is bounded named-path evidence, not a recursive tree receipt."
  - "Only this Markdown file changes. No path move, code, package metadata, credential, endpoint configuration, SourceDescriptor, registry activation, contract, schema, policy, fixture payload, executable test, workflow, lifecycle artifact, release object, or public artifact is created or modified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# NASA HLS Nested Compatibility Boundary

> [!IMPORTANT]
> **Document lifecycle:** `draft v0.1`  
> **Lane class:** `compatibility / transitional / README-only`  
> **Path posture:** both `connectors/nasa/hls/` and `connectors/nasa-hls/` exist; final ownership is `CONFLICTED / NEEDS VERIFICATION`  
> **Runtime posture:** no supported package, client, downloader, parser, QA decoder, admission decision, test lane, or lifecycle handoff is established here  
> **Authority:** navigation and migration control only; no independent source, credential, schema, policy, registry, evidence, lifecycle, analysis, release, routing, or publication authority

> [!CAUTION]
> Do not add HLS implementation to both connector paths. Until an ADR or migration plan chooses an owner, use the substantive [`connectors/nasa-hls/` boundary](../../nasa-hls/README.md) for HLS operating doctrine and keep this nested lane as a non-divergent compatibility pointer.

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Does not belong](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed) · [Topology](#path-topology-and-migration-control) · [HLS boundary](#hls-product-and-claim-boundary) · [Lifecycle](#lifecycle-and-security-boundary) · [Evidence](#evidence-basis) · [Rollback](#rollback) · [Backlog](#verification-backlog) · [Done](#definition-of-done)

---

## Purpose

`connectors/nasa/hls/` preserves a discoverable nested HLS connector address already referenced by Agriculture documentation while the repository resolves a competing flat HLS lane.

This README exists to:

- prevent the blank nested folder from being mistaken for an implemented connector;
- route maintainers to the fuller HLS source-admission boundary at [`connectors/nasa-hls/`](../../nasa-hls/README.md);
- expose the flat-versus-nested path conflict instead of silently choosing a winner;
- stop both locations from acquiring independent code, descriptors, fixtures, tests, or configuration;
- preserve a reversible point for a future move, mirror, deprecation, or redirect;
- keep HLS material upstream of analysis, evidence closure, promotion, release, and publication.

This document does not activate NASA HLS, validate credentials, establish a package, choose an endpoint, or prove any runtime behavior.

---

## Authority level

| Concern | Determination |
|---|---|
| Responsibility root | **CONFIRMED:** `connectors/` is the source-specific fetch and admission implementation root under Directory Rules §7.3. |
| Current nested path | **CONFIRMED:** this README path exists; before this revision it was a one-byte blank placeholder. |
| Lane class | **PROPOSED:** compatibility/transitional navigation surface, not an implementation-bearing lane. |
| Substantive HLS boundary | **CONFIRMED:** [`connectors/nasa-hls/README.md`](../../nasa-hls/README.md) holds the current detailed HLS source-admission contract. |
| Canonical HLS implementation home | **CONFLICTED / NEEDS VERIFICATION:** no accepted ADR or migration receipt inspected here chooses flat or nested placement. |
| NASA family placement | **DEFERRED:** source-family documentation tracks `OPEN-DSC-14`; folder presence does not resolve it. |
| Source activation | **NOT ESTABLISHED:** the machine source-authority register is empty and the inspected Agriculture HLS registry record is a placeholder. |
| SourceDescriptor authority | **CONFLICTED:** a populated singular schema names an almost-empty plural schema as canonical. |
| Runtime and tests | **NOT ESTABLISHED:** named conventional probes beneath both HLS lanes found no package metadata, source module, or test README. |
| Public output | **NOT AUTHORIZED:** this lane emits no claim, map, API payload, EvidenceBundle, release, or publication artifact. |

Documentation here may explain constraints. It cannot substitute for an accepted ADR, a conforming SourceDescriptor, policy decisions, executable tests, lifecycle receipts, or release evidence.

---

## Status

### Bounded repository snapshot

| Surface inspected at base `6d251686…` | Status | What it establishes |
|---|---:|---|
| `connectors/nasa/hls/README.md` | **CONFIRMED EMPTY BEFORE REVISION** | Nested address exists; it did not contain a contract or implementation claim. |
| `connectors/nasa-hls/README.md` | **CONFIRMED SUBSTANTIVE README** | Flat lane contains the detailed HLS boundary and records the same topology conflict. |
| `connectors/nasa/README.md` | **CONFIRMED DRAFT FAMILY README** | NASA umbrella is proposed and beyond the named §7.3 family examples. |
| Nested conventional package/source/test probes | **NOT FOUND AT NAMED PATHS** | No `pyproject.toml`, `src/hls/__init__.py`, or `tests/README.md` was found here. |
| Flat conventional package/source/test probes | **NOT FOUND AT NAMED PATHS** | No conventional package or test README was found in the flat lane. |
| Agriculture pipeline and spec READMEs | **CONFIRMED DOCUMENTATION** | Both list `connectors/nasa/hls/` as an adjacent connector path. |
| `data/registry/sources/agriculture/nasa_hls.yaml` | **CONFIRMED PLACEHOLDER** | Candidate filename exists; it is not a conforming or active SourceDescriptor. |
| `control_plane/source_authority_register.yaml` | **CONFIRMED EMPTY REGISTER** | `entries: []`; no HLS authority or activation entry is established. |
| HLS-VI fixture README | **CONFIRMED DOCUMENTATION-ONLY EVIDENCE** | Fixture intent is documented; an executable payload/validator/test consumer is not established here. |
| Generic connector and descriptor workflows | **CONFIRMED TODO-ONLY** | Existing jobs echo TODO text and do not prove enforcement. |

The named probes are deliberately bounded. Differently named or deeper implementation content remains `UNKNOWN` until a recursive inventory is captured and reviewed.

---

## What belongs here

While this lane remains compatibility-only, accepted content is limited to:

- this README;
- a concise, reviewable compatibility marker approved by the path migration plan;
- a generated redirect or import shim only after an ADR identifies the canonical owner and defines parity tests;
- deprecation metadata that points to the selected owner and sunset date;
- links to the canonical connector boundary, migration manifest, drift entry, and rollback receipt.

Any compatibility artifact must be mechanically tied to one owning path and must not evolve independently.

---

## What does NOT belong here

Until topology is resolved, do not add:

- a second HLS client, downloader, discovery adapter, parser, QA decoder, command, service, or package;
- independent endpoint lists, access methods, credentials, tokens, cookies, signed URLs, or secret caches;
- SourceDescriptors, activation records, source-authority entries, rights decisions, sensitivity decisions, or release policy;
- duplicated fixtures, tests, schemas, contracts, pipeline specifications, or configuration;
- RAW, QUARANTINE, WORK, PROCESSED, CATALOG, TRIPLET, PUBLISHED, proof, receipt, or release data;
- browser-side NASA access, public API routes, map layers, claims, alerts, summaries, or AI-ready payloads;
- product documentation that can drift from the detailed flat-lane boundary or current official NASA material.

Do not treat a working redirect, a successful download, or a passing documentation check as HLS source activation.

---

## Inputs

### Current inputs

This compatibility README is grounded in:

- current repository path and blob evidence;
- the detailed flat-lane HLS README;
- Directory Rules §§2.5, 7.3, 14, 15, and 16;
- NASA source-family and HLS product catalog documentation;
- Agriculture source, pipeline, pipeline-spec, registry, and fixture documentation;
- SourceDescriptor contract/schema surfaces and source-authority register state;
- current official NASA HLS product and access documentation checked on 2026-07-14.

### Future migration inputs

A change beyond documentation requires all applicable inputs below:

- accepted ADR or an approved proportional migration plan;
- complete old-to-new path and consumer-reference inventory;
- selected canonical owner and compatibility class;
- source steward, connector steward, domain steward, security, rights, sensitivity, validation, test, and docs review;
- parity, import, link, fixture, and rollback tests;
- deprecation/sunset record when an old address remains temporarily.

---

## Outputs

### Current output

The only output of this lane is a human-readable compatibility and migration boundary.

It provides:

- a stable navigation route for existing nested-path references;
- an explicit conflict label;
- a stop condition against dual implementation;
- a review checklist for future topology work;
- an exact documentation rollback blob.

### Explicitly not emitted

This lane emits no source request, credential, HLS asset, transformed raster, QA result, manifest, SourceDescriptor, authority decision, lifecycle object, receipt, EvidenceBundle, catalog record, release object, API payload, map layer, or published claim.

---

## Validation

### Documentation checks for this revision

- [x] Target path and prior blank blob verified at the pinned base.
- [x] Flat HLS README and NASA parent README read directly.
- [x] Named conventional package, source, and test probes checked beneath both paths.
- [x] Agriculture nested-path references and registry/fixture documentation inspected.
- [x] Source-authority register, SourceDescriptor schema conflict, and TODO-only workflows inspected.
- [x] Current official NASA HLS product and access pages checked.
- [x] No secrets, credentials, tokens, signed URLs, or protected payloads added.
- [x] Scope limited to one Markdown file; no path is moved or activated.

### Required checks for any future compatibility shim or migration

- one canonical implementation owner is named;
- every old and new reference is inventoried and updated or intentionally retained;
- the compatibility surface is generated/frozen and cannot diverge;
- imports, CLI entry points, fixtures, tests, docs, workflows, and package metadata resolve through the selected owner;
- no duplicate network call, retry, cache, receipt, or lifecycle write occurs;
- rollback restores the prior path graph and consumer behavior;
- the deprecation window and removal conditions are recorded;
- link, path, no-network, negative, and parity tests pass.

The generic connector and SourceDescriptor workflows currently echo TODO messages. Their green status must not be described as substantive validation.

---

## Review burden

Changes require review proportional to effect:

| Change | Minimum review |
|---|---|
| README clarification with no authority change | Connector steward + NASA/HLS source steward + docs steward. |
| Compatibility marker, redirect, or import shim | Above + package/test steward + affected Agriculture consumer owner. |
| Credential, endpoint, or access behavior | Above + security + rights + sensitivity reviewers. |
| Flat/nested owner selection or path move | ADR/migration review + connector/source/domain owners + all affected consumer owners. |
| Source activation or lifecycle handoff | Source-authority, policy, validation, operations, and release-gate reviewers outside this README. |

The current [CODEOWNERS file](../../../.github/CODEOWNERS) is a greenfield placeholder and has no HLS-specific route. `OWNER_TBD` remains truthful until accepted ownership is recorded.

---

## Related folders

| Surface | Relationship |
|---|---|
| [`../../nasa-hls/`](../../nasa-hls/README.md) | Detailed current HLS source-admission boundary; do not duplicate it here. |
| [`../`](../README.md) | Proposed NASA connector-family boundary. |
| [`../../`](../../README.md) | Connector-root source-admission and lifecycle contract. |
| [`../../../docs/sources/catalog/nasa/`](../../../docs/sources/catalog/nasa/README.md) | NASA source-family documentation and deferred placement question. |
| [`../../../docs/sources/catalog/nasa/nasa-hls.md`](../../../docs/sources/catalog/nasa/nasa-hls.md) | KFM HLS product/source doctrine; context is not field truth. |
| [`../../../pipelines/domains/agriculture/`](../../../pipelines/domains/agriculture/README.md) | Downstream executable-pipeline boundary that currently references this nested address. |
| [`../../../pipeline_specs/agriculture/`](../../../pipeline_specs/agriculture/README.md) | Declarative Agriculture pipeline-spec boundary that currently references this nested address. |
| [`../../../fixtures/domains/agriculture/hls_vi/`](../../../fixtures/domains/agriculture/hls_vi/README.md) | Documentation-only HLS-VI fixture lane; not connector authority. |
| [`../../../data/registry/sources/agriculture/nasa_hls.yaml`](../../../data/registry/sources/agriculture/nasa_hls.yaml) | PROPOSED placeholder; not activation. |
| [`../../../contracts/source/source_descriptor.md`](../../../contracts/source/source_descriptor.md) | SourceDescriptor meaning. |
| [`../../../policy/source/`](../../../policy/source/README.md) | Source-admission policy boundary. |
| [`../../../policy/rights/`](../../../policy/rights/README.md) and [`../../../policy/sensitivity/`](../../../policy/sensitivity/README.md) | Rights and sensitivity authority outside connector code. |

---

## ADRs

No accepted ADR inspected for this revision selects `connectors/nasa-hls/` or `connectors/nasa/hls/` as the canonical implementation home.

Before an owner is selected:

1. record the conflict in the drift/ADR process;
2. include `OPEN-DSC-14` and NASA family placement in the decision context;
3. identify every consumer and path reference;
4. state whether the losing path becomes a temporary mirror, redirect, deprecated address, or is removed;
5. define old-to-new mapping, compatibility window, parity checks, deprecation date, and rollback;
6. prevent both paths from evolving independently.

Directory Rules §2.5 says conflicted paths remain `PROPOSED / CONFLICTED`; §14 governs moves and structural migration; §16 forbids parallel authority and requires the rule basis in the PR.

---

## Last reviewed

**2026-07-14** — repository evidence was read at `main` commit `6d251686ac367cdb13bb88417bc46c0a78c5ebb3`; current official NASA HLS product and access pages were checked the same day.

Re-review when any of these changes:

- flat or nested HLS path contents;
- NASA-family placement or `OPEN-DSC-14` status;
- Agriculture connector references;
- SourceDescriptor schema authority or registry record shape;
- source-authority entries;
- official HLS products, versions, access surfaces, authentication, known issues, or status;
- connector/test workflow substance.

---

## Path topology and migration control

### Current topology

| Address | Current role | Allowed evolution before decision |
|---|---|---|
| `connectors/nasa-hls/README.md` | Substantive README-only HLS source-admission boundary. | Documentation maintenance that preserves the conflict and does not create runtime authority. |
| `connectors/nasa/hls/README.md` | Nested compatibility/navigation boundary. | Non-divergent pointer and migration-control documentation only. |
| Agriculture pipeline/spec references | Consumers of the nested address in documentation. | Keep intact until deliberately migrated and verified. |

### Decision invariants

Any resolution must preserve:

- one implementation owner;
- HLS product/collection/granule/asset identity;
- source QA without destructive flattening;
- consumer links and import compatibility during the declared window;
- source, rights, sensitivity, lifecycle, evidence, and release authority outside the connector path;
- reversible history and a tested rollback target.

Do not copy the 900-plus-line flat README into this folder. Duplication would create two manually maintained contracts and make drift more likely.

---

## HLS product and claim boundary

The current official NASA HLS pages describe L30 and S30 as primary harmonized surface-reflectance products and HLS-VI as a derived vegetation-index product. They are delivered as 30 m, MGRS-tiled Cloud Optimized GeoTIFF assets with product-specific metadata and Fmask QA. Official access documentation describes multiple discovery/download surfaces and Earthdata Login requirements.

This compatibility README intentionally does not duplicate the detailed, version-sensitive product table maintained in the [flat HLS boundary](../../nasa-hls/README.md). Maintainers must check [NASA HLS Data Products](https://hls.gsfc.nasa.gov/data-products/) and [Data Access and Tools](https://hls.gsfc.nasa.gov/data-access-and-tools/) when product or access behavior matters.

Regardless of path selection:

- L30, S30, HLS-VI, HLS-LL, OPERA-derived products, Landsat archive products, MAIAC, and FIRMS remain distinct;
- HLS imagery and indices are context/derived source material, not field, crop, damage, regulatory, or emergency truth;
- source QA preservation is not downstream analytical validation;
- a successful download is not source admission;
- source admission is not promotion, evidence closure, release, or publication.

---

## Lifecycle and security boundary

If a future implementation is approved at one path, its maximum connector-local flow is:

```text
caller-supplied descriptor + approved server-side credentials
  -> discovery / retrieval / integrity and metadata checks
  -> preserve product, collection, granule, asset, platform, band, QA, and provenance identity
  -> caller-owned RAW candidate or QUARANTINE candidate + secret-free receipt
  -> stop
```

Outside the connector:

```text
normalization -> mask/composite/index analysis -> validation -> evidence closure
-> catalog/triplet -> policy and release decision -> governed publication
```

A future connector must never commit or expose credentials, authorization headers, cookies, signed URLs, token caches, private redirects, or protected payloads. It must not forward authorization across unapproved hosts or let browser/public clients call protected distribution surfaces directly.

---

## Evidence basis

| Evidence | Status | Supports | Does not prove |
|---|---:|---|---|
| Prior nested blob `8b137891…` | **CONFIRMED EMPTY** | Exact rollback target and absence of prior nested doctrine. | Canonicality or implementation. |
| Flat HLS README blob `c6a1726c…` | **CONFIRMED** | Detailed HLS contract and explicit duplicate-path conflict. | Runtime, activation, or final owner. |
| Exact named package/source/test probes | **CONFIRMED BOUNDED EVIDENCE** | Conventional implementation paths were absent beneath both lanes. | Exhaustive recursive inventory. |
| NASA parent and source-catalog READMEs | **CONFIRMED DRAFT DOCS** | Proposed NASA family and deferred placement posture. | Accepted family placement. |
| Agriculture pipeline/spec READMEs | **CONFIRMED DOCS** | Nested address has current documentation consumers. | Executable pipeline or connector. |
| HLS registry YAML and source-authority register | **CONFIRMED PLACEHOLDER / EMPTY** | Activation is not established. | Descriptor compliance or authority. |
| Singular/plural SourceDescriptor schemas | **CONFIRMED CONFLICT** | Schema-home conflict must remain visible. | Accepted canonical schema or working validator. |
| Connector/descriptor workflows | **CONFIRMED TODO-ONLY** | Workflow scaffolds exist. | Substantive enforcement. |
| Official NASA HLS pages checked 2026-07-14 | **CONFIRMED EXTERNAL** | Current product classes, form, QA, and access posture. | KFM activation, rights review, code, tests, or release. |

### Preserved conflicts and unknowns

1. Flat and nested HLS connector paths coexist without an accepted owner-selection record.
2. Agriculture documentation points to the nested path while the detailed boundary is flat.
3. A populated singular SourceDescriptor schema declares an almost-empty plural path canonical.
4. HLS registry and fixture documentation exist without establishing an active descriptor or executable fixture consumer.
5. Generic workflows are present but do not enforce the named connector or descriptor boundaries.

---

## Rollback

### Documentation rollback

Restore the exact prior blank blob:

```text
8b137891791fe96927ad78e64b0aad7bded08bdc
```

Prefer a reviewed revert commit or revert PR. Do not reset, force-push, or rewrite shared history.

### Rollback triggers

Revert or correct this documentation if it:

- is interpreted as selecting the nested path as canonical;
- causes implementation to begin in both paths;
- breaks current nested-path references without a migration plan;
- duplicates and drifts from the flat HLS contract;
- implies source activation, implementation maturity, rights clearance, or public eligibility;
- exposes credential or protected-access details;
- weakens RAW/QUARANTINE-only, QA-preservation, mask-gated-claim, or no-publication boundaries.

Future topology changes need a separate, tested operational rollback covering references, imports, fixtures, package metadata, workflows, and deprecation state.

---

## Verification backlog

| Item | Status | Required evidence |
|---|---:|---|
| Assign HLS connector/source owners | **UNKNOWN** | Accepted ownership and HLS-specific review routing. |
| Resolve `OPEN-DSC-14` | **DEFERRED** | Accepted NASA family decision. |
| Select flat or nested HLS owner | **CONFLICTED** | ADR or migration plan with alternatives and rollback. |
| Inventory all HLS path consumers | **NEEDS VERIFICATION** | Recursive code/docs/config/workflow/import search receipt. |
| Decide compatibility class for losing path | **NEEDS VERIFICATION** | Mirror, redirect, deprecated path, or removal decision plus sunset. |
| Confirm implementation inventory | **UNKNOWN** | Recursive tree receipt for both lanes and adjacent packages. |
| Resolve SourceDescriptor schema home | **CONFLICTED** | Accepted schema authority, validator, migration, and fixtures. |
| Create conforming HLS descriptors | **NOT ESTABLISHED** | Validated product/access descriptors and authority decision. |
| Establish executable no-network fixtures/tests | **NOT ESTABLISHED** | Fixture payloads, consumers, negative tests, and passing CI. |
| Replace TODO-only CI with enforcement | **NOT ESTABLISHED** | Substantive workflow steps and observed runs. |
| Verify rights, sensitivity, credential, and endpoint controls | **UNKNOWN** | Policy decisions, security tests, and operational receipts. |

---

## Definition of done

This nested lane may change from compatibility-only only after:

- [ ] an accepted decision names one canonical implementation owner;
- [ ] `OPEN-DSC-14` impact is resolved or explicitly bounded;
- [ ] every old/new consumer reference is inventoried;
- [ ] the losing path has a declared compatibility class and sunset or removal rule;
- [ ] old-to-new mapping, deprecation, parity, and rollback are documented;
- [ ] one buildable package exists only at the selected owner path;
- [ ] imports, commands, package metadata, fixtures, tests, workflows, and docs route through that owner;
- [ ] SourceDescriptor schema authority and HLS descriptors are accepted and validated;
- [ ] server-side credential, host, redirect, redaction, retry, integrity, and limit controls are tested;
- [ ] HLS product, granule, asset, platform, band, QA, and provenance identity is preserved;
- [ ] no-network success and negative tests prove RAW/QUARANTINE-only handoff and no public access;
- [ ] deactivation, supersession, correction, and rollback can be replayed;
- [ ] owners and review cadence are recorded;
- [ ] README claims are refreshed from current repository and official-source evidence.

Until then, this path is a signpost—not a connector.

<p align="right"><a href="#top">Back to top</a></p>
