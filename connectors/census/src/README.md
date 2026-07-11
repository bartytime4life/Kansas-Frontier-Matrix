<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-census-src-readme
title: connectors/census/src/ — Census Connector Source Tree
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Census source steward · Frontier Matrix steward · Data steward · Validation steward · Docs steward
created: 2026-07-10
updated: 2026-07-10
policy_label: public; package-source-root; implementation-support; source-admission-only
related:
  - ../README.md
  - ./census/README.md
  - ../../../docs/sources/catalog/census/README.md
  - ../../../data/registry/sources/
  - ../../../data/raw/
  - ../../../data/quarantine/
  - ../../../data/receipts/
  - ../../../policy/rights/
  - ../../../policy/sensitivity/
  - ../../../release/
tags: [kfm, connectors, census, python, source-tree, source-admission, aggregate-data, geography-vintage, uncertainty, governance]
notes:
  - "This README replaces a one-character placeholder and defines the Census connector source-root boundary."
  - "Code below this tree may support descriptor-gated Census source intake and raw/quarantine/receipt handoffs only."
  - "The source tree does not own Census doctrine, SourceDescriptor records, schemas, policy, processed data, catalog/triplets, proof closure, release decisions, API behavior, UI behavior, or publication."
  - "Actual modules, dependencies, package discovery, tests, CI behavior, endpoints, and runtime outputs remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Census Connector Source Tree

> Python source-root boundary for governed Census connector implementation support.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Owner: OWNER_TBD" src="https://img.shields.io/badge/owner-OWNER__TBD-lightgrey">
  <img alt="Scope: source tree" src="https://img.shields.io/badge/scope-source__tree-blue">
  <img alt="Import: side effect free" src="https://img.shields.io/badge/import-side--effect--free-green">
  <img alt="Lifecycle: raw quarantine receipts" src="https://img.shields.io/badge/lifecycle-raw%20%7C%20quarantine%20%7C%20receipts-orange">
</p>

`connectors/census/src/`

## Quick jumps

[Status](#status) · [Scope](#scope) · [Source-tree fit](#source-tree-fit) · [Accepted contents](#accepted-contents) · [Exclusions](#exclusions) · [Package boundary](#package-boundary) · [Import and configuration rules](#import-and-configuration-rules) · [Census source-role discipline](#census-source-role-discipline) · [I/O boundary](#io-boundary) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Definition of done](#definition-of-done)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / `NEEDS VERIFICATION`  
> **Owner:** `OWNER_TBD`  
> **Path:** `connectors/census/src/`  
> **Mode:** Python package source-root container  
> **Truth posture:** `CONFIRMED` file path, parent Census connector README, package README, and placeholder package metadata; actual modules, dependencies, package discovery, imports, tests, CI wiring, endpoints, and runtime behavior remain `NEEDS VERIFICATION`.

---

## Scope

`connectors/census/src/` contains importable implementation support for governed Census source admission.

Code below this source tree may support:

- descriptor-gated Census API or download clients;
- product-family adapters;
- request construction and pagination helpers;
- response and manifest parsing;
- vintage and geography metadata preservation;
- estimate, count, universe, annotation, suppression, and margin-of-error preservation;
- digest and retrieval metadata generation;
- bounded raw, quarantine, and receipt handoffs;
- deterministic no-network test support.

This source tree must not become Census source doctrine, demographic truth, administrative-geography truth, schema authority, policy authority, source registry authority, processed-data authority, catalog/triplet authority, proof closure, release authority, public API behavior, public UI behavior, or publication authority.

---

## Source-tree fit

```text
connectors/
└── census/
    ├── README.md
    ├── pyproject.toml
    └── src/
        ├── README.md
        └── census/
            └── README.md
```

Responsibility boundaries:

| Surface | Responsibility |
|---|---|
| `connectors/census/` | Census connector-lane contract and source-family admission boundary. |
| `connectors/census/src/` | Python source-root container only. |
| `connectors/census/src/census/` | Importable package implementation support. |
| `docs/sources/catalog/census/` | Human-facing Census source and product-family doctrine. |
| `data/registry/sources/` | SourceDescriptor and activation authority. |
| `policy/` | Rights, sensitivity, admissibility, and publication policy. |
| `data/raw/`, `data/quarantine/`, `data/receipts/` | Permitted connector handoff surfaces. |
| `data/work/`, `data/processed/`, `data/catalog/`, `data/triplets/`, `data/proofs/`, `data/published/`, `release/` | Downstream lifecycle and release authority outside this tree. |

---

## Accepted contents

| Belongs here | Required posture |
|---|---|
| Importable package folders | Keep package discovery explicit and reviewable. |
| Package-local documentation | Do not claim runtime behavior without tests or logs. |
| Census client and adapter modules | Require explicit descriptor and runtime configuration. |
| Product-family parsers | Preserve Census-native fields, product identity, vintage, geography, and uncertainty. |
| Pure constants and typed helpers | Must not replace schemas, descriptors, or policy vocabulary. |
| Digest and receipt-input helpers | Deterministic and bounded to source interaction evidence. |
| Small test-support utilities | Offline and deterministic; never fixture authority. |

---

## Exclusions

| Does not belong here | Correct home |
|---|---|
| SourceDescriptor records or activation decisions | `data/registry/sources/` |
| Census product doctrine | `docs/sources/catalog/census/` |
| Machine schemas and human contracts | `schemas/contracts/` and `contracts/` under accepted authority rules |
| Rights or sensitivity policy | `policy/` |
| Raw or quarantine payload storage | `data/raw/`, `data/quarantine/` |
| Processed Census records | `data/processed/` |
| Geography crosswalk authority | governed processing, schema, registry, or domain homes after verification |
| Catalog or triplet records | `data/catalog/`, `data/triplets/` |
| EvidenceBundle or proof closure | `data/proofs/` and governed proof workflows |
| Release decisions and rollback state | `release/` |
| Public API, UI, map, or AI behavior | governed downstream application roots |
| Generated reports and QA artifacts | `artifacts/` |

---

## Package boundary

The expected package namespace is `census`, supported by the placeholder project metadata name `kfm-connector-census`.

> [!NOTE]
> Package discovery, build backend, dependencies, module inventory, public exports, and successful installation are not proven by the current placeholder metadata and remain `NEEDS VERIFICATION`.

The source root must not contain parallel package namespaces for the same authority without an ADR or migration note.

---

## Import and configuration rules

Imports must be side-effect-free.

Importing modules below this tree must not:

- make network requests;
- write files or lifecycle records;
- read credentials or API keys;
- activate Census products;
- inspect live endpoints;
- mutate environment variables;
- create catalog, proof, or release objects;
- log sensitive or restricted payload content.

Runtime clients must receive explicit configuration, including where applicable:

- SourceDescriptor reference;
- product-family identifier;
- dataset or endpoint identifier;
- requested vintage;
- geography and geographic hierarchy;
- variables, groups, universes, or tables;
- API key or credential provider;
- timeout, retry, pagination, and rate-limit settings;
- explicit raw, quarantine, and receipt destinations.

Missing or invalid configuration must fail closed with a bounded result rather than implicit source activation.

---

## Census source-role discipline

Package code must preserve product-family distinctions.

| Product family | Required interpretation boundary |
|---|---|
| Decennial counts | Aggregate counts tied to a defined universe, geography, and vintage; not person-level truth. |
| ACS estimates | Estimates with survey period, universe, geography, annotations, and margins of error where supplied. |
| TIGER/Line | Administrative/reference geometry tied to a vintage; not proof of legal title or cross-vintage identity. |
| Geographic relationship and crosswalk products | Versioned mapping evidence; never assume one-to-one continuity without validated weights and methods. |
| Public microdata releases | Governed public-use records with product-specific disclosure and interpretation limits; not unrestricted living-person identity evidence. |
| Historical compilations | Preserve compilation provenance, transcription status, temporal scope, and source limitations. |

Package helpers must not silently:

- convert estimates into counts;
- drop margins of error or annotations;
- treat suppressed, unavailable, and zero values as equivalent;
- join incompatible universes;
- merge geographies across vintages by name alone;
- treat TIGER/Line geometry as immutable;
- infer individual identity from aggregate data;
- convert a Census geography into legal parcel, title, settlement, or community truth.

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
  data/proofs/ as closure authority
  data/published/
  release/ decisions
  apps/ public API or UI behavior
```

Receipts prove that a source interaction or admission attempt occurred. They do not prove demographic truth, successful processing, catalog closure, release approval, or publication readiness.

---

## Validation

Before relying on this source tree, verify:

- [ ] `pyproject.toml` package discovery includes the intended `src/census/` namespace.
- [ ] Actual modules and public exports are inventoried.
- [ ] Imports perform no network, filesystem, credential, or activation side effects.
- [ ] Client creation requires explicit SourceDescriptor and runtime configuration.
- [ ] Decennial, ACS, TIGER/Line, microdata, historical, and crosswalk products remain distinct.
- [ ] Vintage, universe, geography, estimate/count, annotation, suppression, and uncertainty fields are preserved.
- [ ] Pagination, timeout, retry, rate-limit, and partial-response cases are tested.
- [ ] Output helpers cannot write processed, catalog, triplet, proof-closure, published, or release data.
- [ ] No-network fixtures cover success, failure, denial, no-op, rate-limited, skipped, stale, and quarantine outcomes where applicable.
- [ ] CI executes the relevant tests or the gap remains explicitly `NEEDS VERIFICATION`.

---

## Evidence basis

| Evidence | Status | Supports | Does not prove |
|---|---|---|---|
| `connectors/census/README.md` | `CONFIRMED` | Census connector-lane source-admission and product-family boundaries. | Module completeness, source activation, or runtime health. |
| `connectors/census/src/census/README.md` | `CONFIRMED` | Package-level import, product-family, and lifecycle contract. | Actual package implementation or passing tests. |
| `connectors/census/pyproject.toml` | `CONFIRMED` placeholder | Project name `kfm-connector-census` and version `0.0.0`. | Build backend, dependencies, discovery, installation, or release readiness. |
| Current repository inspection | `CONFIRMED` | This path previously contained a one-character placeholder. | Complete recursive inventory or CI state. |

---

## Rollback

Rollback is required if this README is used to justify:

- direct public or downstream access to connector internals;
- implicit source activation;
- network, credential, or filesystem side effects during import;
- silent loss of Census vintage, universe, geography, annotation, suppression, or uncertainty fields;
- direct writes beyond raw, quarantine, and receipt handoffs;
- package-level authority over schemas, policy, evidence closure, release, API, UI, maps, or publication.

Rollback target: prior placeholder blob `e25f1814e51579d5f55c0f1fe0135ddb28a47f4a`.

---

## Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [ ] Source-tree and package modules are inventoried.
- [ ] Package discovery and installation are verified.
- [ ] Public exports are documented or intentionally absent.
- [ ] Import side effects are tested and absent.
- [ ] SourceDescriptor and configuration gates are enforced.
- [ ] Census product-family and source-role distinctions are tested.
- [ ] Geography vintage and uncertainty preservation are tested.
- [ ] Raw/quarantine/receipt-only handoff boundaries are tested.
- [ ] No processed/catalog/triplet/proof/release/API/UI authority lives here.
- [ ] Fixtures, tests, and CI behavior are verified or explicitly marked `NEEDS VERIFICATION`.

---

## Status summary

`connectors/census/src/` is the Python source-root container for Census connector implementation support. It may support descriptor-gated intake and bounded raw, quarantine, and receipt handoffs. It is not Census doctrine, demographic truth, geography authority, schema authority, policy authority, source-registry authority, evidence closure, release authority, public API/UI behavior, or publication authority.

<p align="right"><a href="#top">Back to top</a></p>
