<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-usgs-src-package-readme
title: connectors/usgs/src/usgs/ — USGS Connector Python Package
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Source steward · USGS steward · Data steward · Validation steward · Docs steward
created: 2026-06-20
updated: 2026-06-20
policy_label: public; package-readme; implementation-support; source-admission-only
related:
  - ../../README.md
  - ../README.md
  - ../../3dep/README.md
  - ../../nhdplus_hr/README.md
  - ../../nlcd/README.md
  - ../../padus/README.md
  - ../../../../docs/sources/catalog/usgs/README.md
  - ../../../../data/registry/sources/
  - ../../../../data/raw/
  - ../../../../data/quarantine/
  - ../../../../data/receipts/
  - ../../../../data/proofs/
  - ../../../../policy/rights/
  - ../../../../policy/sensitivity/
  - ../../../../release/
tags: [kfm, connectors, usgs, python-package, implementation-support, source-admission, raw, quarantine, receipts, no-network-on-import, governance]
notes:
  - "Draft package-level README for importable USGS connector helper code."
  - "This package supports descriptor-gated source admission; it does not own USGS source-family doctrine, product doctrine, SourceDescriptor records, schemas, policy, catalog, triplets, proofs, release decisions, API behavior, or UI behavior."
  - "Imports must be side-effect-free: no network calls, filesystem writes, credential reads, or source activation at import time."
  - "Connector package outputs may support raw, quarantine, and receipt handoffs only."
  - "Concrete modules, tests, package metadata, CI coverage, and runtime behavior remain NEEDS VERIFICATION until inventoried."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# USGS Connector Python Package

> Draft package boundary for importable USGS connector helper code. This package supports governed source admission; it is not a source-family authority or publication path.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Owner: OWNER_TBD" src="https://img.shields.io/badge/owner-OWNER__TBD-lightgrey">
  <img alt="Scope: implementation support" src="https://img.shields.io/badge/scope-implementation__support-blue">
  <img alt="Import: side effect free" src="https://img.shields.io/badge/import-side--effect--free-green">
  <img alt="Lifecycle: raw quarantine receipts" src="https://img.shields.io/badge/lifecycle-raw%20%7C%20quarantine%20%7C%20receipts-orange">
</p>

`connectors/usgs/src/usgs/`

## Quick jumps

[Status](#status) · [Scope](#scope) · [Package fit](#package-fit) · [Allowed code](#allowed-code) · [Forbidden code](#forbidden-code) · [Admission contract](#admission-contract) · [Source-role discipline](#source-role-discipline) · [I/O boundary](#io-boundary) · [Validation](#validation) · [Rollback](#rollback) · [Definition of done](#definition-of-done)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / `NEEDS VERIFICATION`  
> **Owner:** `OWNER_TBD`  
> **Path:** `connectors/usgs/src/usgs/`  
> **Mode:** importable connector helper package  
> **Truth posture:** `CONFIRMED` file path and README content; actual Python modules, package metadata, fixtures, tests, CI wiring, runtime outputs, and release behavior remain `NEEDS VERIFICATION`.

---

## Scope

`connectors/usgs/src/usgs/` is the Python package namespace for USGS connector implementation support.

It may contain pure helpers, typed DTOs, constants, descriptor-gated client adapters, manifest parsers, package inventory helpers, response-shape normalizers, digest helpers, run-receipt helpers, raw/quarantine handoff helpers, and testable product-specific submodules for accepted USGS connector lanes.

It must not become USGS source-family doctrine, USGS product doctrine, SourceDescriptor authority, schema authority, rights policy, sensitivity policy, domain doctrine, processed-data authority, catalog/triplet authority, proof authority, release authority, public API behavior, public UI behavior, or publication authority.

---

## Package fit

```text
connectors/usgs/
├── README.md
└── src/
    └── usgs/
        └── README.md
```

Related connector lanes may include:

```text
connectors/usgs/3dep/
connectors/usgs/nhdplus_hr/
connectors/usgs/nlcd/
connectors/usgs/padus/
connectors/usgs-earthquake/
```

The package can support these lanes, but it does not choose canonical placement or activate any source by itself.

---

## Allowed code

| Allowed item | Required posture |
|---|---|
| Pure constants and enums | Keep descriptive only; do not replace source-role vocabulary, schemas, or descriptors. |
| Descriptor-gated client helpers | Require explicit descriptor/config input; no implicit source activation. |
| Manifest and response parsers | Preserve source fields, product identity, timestamps, geometry metadata, and digest inputs. |
| Digest/checksum helpers | Deterministic and side-effect-free unless handed explicit bytes/path. |
| Run-receipt helpers | Create structured receipt payloads for successful, failed, denied, no-op, skipped, or rate-limited probes. |
| Raw/quarantine handoff helpers | Require explicit destination and receipt metadata; never write processed/catalog/published data. |
| Test fixture helpers | Keep offline and deterministic; fixtures are not source authority. |

---

## Forbidden code

| Forbidden item | Reason |
|---|---|
| Network calls at import time | Imports must be safe, deterministic, and testable. |
| Filesystem writes at import time | Importing the package must not mutate lifecycle data. |
| Credential reads at import time | Secrets and credentials belong in runtime configuration, not module import side effects. |
| Direct writes to processed/catalog/triplets/published | Connectors are admission only; downstream stages own promotion. |
| Embedded SourceDescriptor authority | Descriptors live under registry roots and are validated separately. |
| Embedded rights/sensitivity policy | Policy lives under policy roots and is applied by gates. |
| Public API/UI payload builders | Public clients use governed interfaces and released artifacts, not connector internals. |

---

## Admission contract

USGS package helpers must preserve:

- product or sub-source identity;
- SourceDescriptor reference supplied by caller;
- source URL/reference or package identity;
- retrieval/import time;
- source role and sub-product role;
- rights and review posture passed by gates;
- source timestamps, version, release, or epoch fields;
- geometry/raster/network metadata when applicable;
- digest/checksum fields;
- run receipt and rollback target where applicable.

No package helper should claim that a source is activated, published, or authoritative without registry and release evidence.

---

## Source-role discipline

USGS is a multi-product source family. Package helpers must preserve source-role separation across sub-products:

| Example | Required separation |
|---|---|
| 3DEP | LAZ observed source material, EPT/COPC analytic delivery, DEMs modeled derivatives. |
| NHDPlus HR | Digitized geometry observed/digitized; VAAs and topology modeled. |
| NLCD | Uniformly modeled class assignments; class maps are versioned. |
| PAD-US | Versioned context with contributor slices; not cadastral or habitat truth. |
| Earthquakes | Event origins, modeled products, and crowdsourced context remain distinct. |

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

Receipts are evidence of a run or probe. Receipts are not proof closure, catalog closure, or publication authority.

---

## Validation

Before relying on this package, verify:

- actual modules are inventoried;
- package metadata exists and points to this source root if applicable;
- imports are side-effect-free;
- no-network fixtures exist;
- descriptor-gated clients reject missing descriptor/config inputs;
- parsers preserve source fields and source-role metadata;
- output helpers cannot write processed/catalog/triplet/published data;
- tests cover success, failure, denial, no-op, skipped, and rate-limited receipt cases;
- CI runs the relevant tests or this remains `NEEDS VERIFICATION`.

---

## Rollback

Rollback is required if this README is used to justify connector authority beyond importable helper code, direct public access, direct promotion, direct release, or bypass of SourceDescriptor/policy gates.

Rollback target: initial blank file content SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

---

## Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [ ] Actual Python modules are inventoried.
- [ ] Package metadata and import paths are verified.
- [ ] Import side effects are tested and absent.
- [ ] Descriptor/config gates are tested.
- [ ] Source-role and sub-product separation are tested.
- [ ] Raw/quarantine/receipt-only output boundaries are tested.
- [ ] No processed/catalog/triplet/published/release/API/UI authority lives here.
- [ ] Tests and CI behavior are verified or marked `NEEDS VERIFICATION`.

---

## Status summary

`connectors/usgs/src/usgs/` is a draft implementation-support package for USGS connector helpers. It is not USGS source-family doctrine, product doctrine, SourceDescriptor authority, policy authority, schema authority, catalog/triplet authority, proof closure, release authority, public API behavior, public UI behavior, or pipeline authority.

<p align="right"><a href="#top">Back to top</a></p>
