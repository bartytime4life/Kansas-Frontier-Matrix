<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-census-src-census-readme
title: connectors/census/src/census/ — Census Connector Python Package
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Source steward · Census steward · Frontier Matrix steward · Data steward · Validation steward · Docs steward
created: 2026-07-10
updated: 2026-07-10
policy_label: public; package-readme; implementation-support; source-admission-only
related:
  - ../../README.md
  - ../README.md
  - ../../../../docs/sources/catalog/census/README.md
  - ../../../../docs/sources/catalog/census/acs-estimates.md
  - ../../../../docs/sources/catalog/census/tiger-line.md
  - ../../../../docs/sources/catalog/census/decennial-counts.md
  - ../../../../docs/sources/catalog/census/decennial-microdata.md
  - ../../../../data/registry/sources/
  - ../../../../data/raw/
  - ../../../../data/quarantine/
  - ../../../../data/receipts/
  - ../../../../data/proofs/
  - ../../../../policy/
  - ../../../../release/
tags: [kfm, connectors, census, python-package, acs, decennial, tiger-line, source-admission, aggregate, vintage, uncertainty, raw, quarantine, receipts, governance]
notes:
  - "Draft package-level README for importable Census connector helper code."
  - "This package supports descriptor-gated Census source admission; it does not own Census doctrine, SourceDescriptor records, schemas, policy, catalog, triplets, proofs, release decisions, API behavior, or UI behavior."
  - "Imports must be side-effect-free: no network calls, filesystem writes, credential reads, or source activation at import time."
  - "Connector package outputs may support raw, quarantine, and receipt handoffs only."
  - "Concrete modules, dependencies, tests, package discovery, CI coverage, and runtime behavior remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Census Connector Python Package

> Importable helper code for governed Census source admission. This package preserves product family, vintage, aggregation, geography, and uncertainty; it does not create demographic truth or publication authority.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Owner: OWNER_TBD" src="https://img.shields.io/badge/owner-OWNER__TBD-lightgrey">
  <img alt="Scope: implementation support" src="https://img.shields.io/badge/scope-implementation__support-blue">
  <img alt="Import: side effect free" src="https://img.shields.io/badge/import-side--effect--free-green">
  <img alt="Lifecycle: raw quarantine receipts" src="https://img.shields.io/badge/lifecycle-raw%20%7C%20quarantine%20%7C%20receipts-orange">
</p>

`connectors/census/src/census/`

## Quick jumps

[Status](#status) · [Scope](#scope) · [Package fit](#package-fit) · [Allowed code](#allowed-code) · [Forbidden code](#forbidden-code) · [Admission contract](#admission-contract) · [Product-family discipline](#product-family-discipline) · [Time-geography-and-uncertainty](#time-geography-and-uncertainty) · [I/O boundary](#io-boundary) · [Validation](#validation) · [Rollback](#rollback) · [Definition of done](#definition-of-done)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / `NEEDS VERIFICATION`  
> **Owner:** `OWNER_TBD`  
> **Path:** `connectors/census/src/census/`  
> **Mode:** importable Census connector helper package  
> **Truth posture:** `CONFIRMED` target path, parent connector README, and placeholder package metadata; actual Python modules, dependencies, package discovery, fixtures, tests, CI wiring, emitted receipts, source activation, and runtime behavior remain `NEEDS VERIFICATION`.

---

## Scope

`connectors/census/src/census/` is the Python package namespace for Census connector implementation support.

It may contain:

- pure constants and enums;
- typed request or response helpers;
- descriptor-gated API and download adapters;
- product-family and vintage parsers;
- geography-key and source-identifier helpers;
- digest and retrieval-metadata helpers;
- bounded outcome and run-receipt helpers;
- raw/quarantine handoff helpers;
- deterministic fixture-support utilities.

It must not become Census doctrine, demographic truth, administrative-boundary truth, SourceDescriptor authority, schema authority, policy authority, processed-data authority, catalog/triplet authority, proof closure, release authority, public API behavior, public UI behavior, or publication authority.

---

## Package fit

```text
connectors/census/
├── README.md
├── pyproject.toml
└── src/
    └── census/
        └── README.md
```

The package sits below the connector lane and above downstream lifecycle stages:

```text
SourceDescriptor + explicit runtime configuration
  -> census package helpers
  -> data/raw/ or data/quarantine/ + data/receipts/
  -> downstream normalization / validation
  -> data/work/
  -> data/processed/
  -> data/catalog/ + data/triplets/
  -> release/
  -> data/published/
```

Everything after the raw/quarantine/receipt handoff is outside this package's authority.

---

## Allowed code

| Allowed item | Required posture |
|---|---|
| Pure constants and enums | Descriptive only; must not replace schemas, source descriptors, or policy vocabularies. |
| Descriptor-gated client helpers | Require an explicit SourceDescriptor reference or resolved config; no implicit activation. |
| Census API request builders | Preserve dataset, vintage, geography, variables, predicate filters, and request provenance. |
| Download and manifest helpers | Preserve product family, release/vintage, file identity, digest inputs, and source locator. |
| Response parsers | Preserve source-native fields and do not silently collapse counts, estimates, margins of error, annotations, or null/suppression states. |
| Geography helpers | Preserve source geography code, vintage, hierarchy, and relationship to geometry products. |
| Digest/checksum helpers | Deterministic and side-effect-free unless handed explicit bytes or paths. |
| Run-receipt helpers | Represent success, failure, deny, quarantine, no-op, skipped, stale, or rate-limited outcomes. |
| Raw/quarantine handoff helpers | Require explicit destinations and receipt metadata; never write processed, catalog, triplet, or published data. |
| Test fixture helpers | Offline, deterministic, small, and non-authoritative. |

---

## Forbidden code

| Forbidden item | Reason |
|---|---|
| Network calls at import time | Imports must remain safe, deterministic, and testable. |
| Filesystem writes at import time | Importing the package must not mutate lifecycle data. |
| Credential or environment reads at import time | Secrets and runtime configuration must be explicit. |
| Implicit source activation | Activation belongs to governed registry and policy surfaces. |
| Direct writes to `data/work/`, `data/processed/`, `data/catalog/`, `data/triplets/`, or `data/published/` | Connectors are admission-only. |
| Embedded SourceDescriptor authority | Descriptors belong under governed registry roots. |
| Embedded rights, disclosure, or publication policy | Policy belongs under policy roots and must be applied by gates. |
| Demographic inference or person-level identity resolution | Census products do not authorize unsupported identity or individual claims. |
| Public API, UI, map, or AI payload builders | Public surfaces use governed interfaces and released artifacts. |

---

## Admission contract

Package helpers must preserve, when available:

- Census source-family identifier;
- product-family identifier;
- dataset name and API group;
- vintage, release year, survey year, or decennial year;
- geography type, source geography code, and parent hierarchy;
- variable/group identifiers;
- estimate, count, margin of error, annotation, suppression, null, and universe fields;
- source URL, API request, file locator, or distribution identifier;
- retrieval time and source/release time;
- source role and authority scope;
- rights, disclosure, and review posture supplied by upstream gates;
- content digest and package/file identity;
- bounded outcome, reason code, and rollback target where applicable.

No helper may claim that a dataset is active, authoritative for a downstream claim, released, corrected, or publishable without registry, policy, evidence, review, and release support.

---

## Product-family discipline

Census is a multi-product source family. Package code must preserve the differences among product families.

| Product family | Required distinction |
|---|---|
| Decennial counts | Aggregate counts tied to a specific census, geography vintage, table, universe, and release. |
| ACS estimates | Estimates, not counts by default; preserve margins of error, annotations, universe, period, and release vintage. |
| TIGER/Line | Administrative/reference geometry and relationship files; not demographic or legal-boundary truth by themselves. |
| Decennial microdata | Person/household-level source material subject to disclosure, use, provenance, and release constraints. |
| Historical compilations | Preserve compiler, transcription, revision, geography crosswalk, and source limitations. |
| Crosswalks and relationship files | Derived relationships with explicit vintages and fit-for-use limits; not timeless identity. |

> [!CAUTION]
> A matching name, code, tract, block group, county, place, or boundary does not establish stable identity across vintages. Cross-vintage linkage is a governed transformation outside source admission.

---

## Time, geography, and uncertainty

Package helpers must not collapse distinct temporal or geographic meanings.

Preserve where material:

- survey or census reference period;
- source publication/release time;
- retrieval time;
- geography vintage;
- boundary effective period;
- correction or supersession time;
- estimate versus count;
- margin of error and confidence metadata;
- annotation, suppression, imputation, and unavailable-value semantics;
- universe and denominator definition.

A Census geography identifier is incomplete without product family and vintage. An ACS estimate is incomplete without period, universe, and uncertainty fields when supplied.

---

## I/O boundary

```text
MAY SUPPORT:
  data/raw/<domain>/<source_id>/<run_id>/
  data/quarantine/<domain>/<source_id>/<run_id>/
  data/receipts/<run_id>/

MUST NOT OWN:
  data/work/
  data/processed/
  data/catalog/
  data/triplets/
  data/published/
  data/proofs/ as closure authority
  release/ decisions
  apps/ public API or UI behavior
```

Receipts show what a connector run attempted and observed. They do not prove demographic truth, catalog closure, release readiness, or publication authority.

---

## Validation

Before relying on this package, verify:

- [ ] actual modules are inventoried;
- [ ] package metadata and source discovery are configured correctly;
- [ ] imports make no network calls, filesystem writes, credential reads, or source activations;
- [ ] clients reject missing descriptors and required runtime configuration;
- [ ] product family, vintage, geography, variable, universe, and source-role fields are preserved;
- [ ] ACS margins of error and annotation/suppression states are not silently dropped;
- [ ] TIGER/Line geometry is not treated as demographic or legal truth;
- [ ] cross-vintage geography matching is not performed implicitly;
- [ ] output helpers cannot write processed, catalog, triplet, published, proof-closure, or release data;
- [ ] no-network tests cover success, quarantine, denial, no-op, stale, skipped, error, and rate-limit outcomes;
- [ ] CI execution is verified or remains explicitly `NEEDS VERIFICATION`.

---

## Rollback

Rollback is required if this README or package is used to justify:

- direct public access to connector internals;
- implicit source activation;
- silent loss of margin-of-error, vintage, universe, annotation, or suppression fields;
- timeless geography identity across vintages;
- direct writes beyond raw, quarantine, or receipts;
- demographic, legal, identity, or publication authority not supported by downstream governance.

Rollback target: placeholder content blob `e25f1814e51579d5f55c0f1fe0135ddb28a47f4a`.

---

## Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [ ] Actual Python modules and public exports are inventoried.
- [ ] `pyproject.toml` contains verified build, dependency, and package-discovery configuration.
- [ ] Import side effects are tested and absent.
- [ ] SourceDescriptor and runtime-config gates are tested.
- [ ] Product-family, vintage, geography, universe, and uncertainty preservation are tested.
- [ ] Raw/quarantine/receipt-only output boundaries are enforced.
- [ ] No processed/catalog/triplet/published/proof/release/API/UI authority lives here.
- [ ] Tests and CI behavior are verified or marked `NEEDS VERIFICATION`.

---

## Status summary

`connectors/census/src/census/` is a draft implementation-support package for governed Census source admission. It is not Census doctrine, demographic truth, administrative-boundary truth, SourceDescriptor authority, policy authority, schema authority, catalog/triplet authority, proof closure, release authority, public API behavior, public UI behavior, or publication authority.

<p align="right"><a href="#top">Back to top</a></p>
