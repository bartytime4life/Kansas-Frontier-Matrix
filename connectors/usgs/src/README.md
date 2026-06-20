<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-usgs-src-readme
title: connectors/usgs/src/ — USGS Connector Source Root
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Source steward · USGS steward · Data steward · Validation steward · Docs steward
created: 2026-06-20
updated: 2026-06-20
policy_label: public; src-root-readme; implementation-support; source-admission-only
related:
  - ../README.md
  - ./usgs/README.md
  - ../3dep/README.md
  - ../nhdplus_hr/README.md
  - ../nlcd/README.md
  - ../padus/README.md
  - ../../../docs/sources/catalog/usgs/README.md
  - ../../../data/registry/sources/
  - ../../../data/raw/
  - ../../../data/quarantine/
  - ../../../data/receipts/
  - ../../../data/proofs/
  - ../../../policy/rights/
  - ../../../policy/sensitivity/
  - ../../../release/
tags: [kfm, connectors, usgs, src-root, python, implementation-support, source-admission, raw, quarantine, receipts, package-layout, governance]
notes:
  - "Draft README for the USGS connector source-code root."
  - "This src root organizes importable connector helper packages; it does not own source-family doctrine, product doctrine, SourceDescriptor records, schemas, policy, catalog, triplets, proofs, release decisions, API behavior, or UI behavior."
  - "The package-specific boundary lives at connectors/usgs/src/usgs/README.md."
  - "Imports must be side-effect-free: no network calls, filesystem writes, credential reads, or source activation at import time."
  - "Concrete modules, tests, package metadata, CI coverage, and runtime behavior remain NEEDS VERIFICATION until inventoried."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# USGS Connector Source Root

> Draft source-root boundary for USGS connector implementation support. This folder organizes importable helper code; it does not activate sources or publish data.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Owner: OWNER_TBD" src="https://img.shields.io/badge/owner-OWNER__TBD-lightgrey">
  <img alt="Scope: source root" src="https://img.shields.io/badge/scope-source__root-blue">
  <img alt="Import: side effect free" src="https://img.shields.io/badge/import-side--effect--free-green">
  <img alt="Lifecycle: raw quarantine receipts" src="https://img.shields.io/badge/lifecycle-raw%20%7C%20quarantine%20%7C%20receipts-orange">
</p>

`connectors/usgs/src/`

## Quick jumps

[Status](#status) · [Scope](#scope) · [Directory fit](#directory-fit) · [Relationship to package README](#relationship-to-package-readme) · [Allowed contents](#allowed-contents) · [Forbidden contents](#forbidden-contents) · [Import and runtime rules](#import-and-runtime-rules) · [I/O boundary](#io-boundary) · [Validation](#validation) · [Rollback](#rollback) · [Definition of done](#definition-of-done)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / `NEEDS VERIFICATION`  
> **Owner:** `OWNER_TBD`  
> **Path:** `connectors/usgs/src/`  
> **Mode:** source-code root for connector helper packages  
> **Truth posture:** `CONFIRMED` file path and README content; actual modules, package metadata, tests, fixtures, CI wiring, runtime outputs, and release behavior remain `NEEDS VERIFICATION`.

---

## Scope

`connectors/usgs/src/` is the source-code root for USGS connector implementation support.

This folder may contain importable package directories, package-local README files, pure helper modules, typed DTO modules, manifest parser modules, digest helpers, run-receipt helpers, no-network fixture helpers, and product-specific helper packages for accepted USGS connector lanes.

It must not become USGS source-family doctrine, USGS product doctrine, SourceDescriptor authority, schema authority, rights policy, sensitivity policy, domain doctrine, processed-data authority, catalog/triplet authority, proof authority, release authority, public API behavior, public UI behavior, pipeline authority, or publication authority.

---

## Directory fit

```text
connectors/usgs/
├── README.md
└── src/
    ├── README.md
    └── usgs/
        └── README.md
```

This README governs the `src/` layout boundary. The package-specific README at `connectors/usgs/src/usgs/README.md` governs the importable `usgs` package boundary.

---

## Relationship to package README

| File | Boundary |
|---|---|
| `connectors/usgs/src/README.md` | Source-root layout, packaging, and code-placement rules. |
| `connectors/usgs/src/usgs/README.md` | Importable Python package behavior and helper-code contract. |
| `connectors/usgs/README.md` | USGS connector-family coordination and source-admission boundary. |

No move, delete, rename, redirect, or deprecation is implied by this README.

---

## Allowed contents

| Allowed item | Required posture |
|---|---|
| Importable package directories | Keep package boundaries explicit with README files where useful. |
| Pure helper modules | No side effects at import time. |
| DTO and manifest modules | Preserve source fields and metadata; do not replace schemas or contracts. |
| Product helper modules | Product-specific helpers must preserve product identity and source-role separation. |
| Digest and receipt helpers | Deterministic and testable. |
| Offline fixture helpers | No network dependency; fixtures do not become source authority. |

---

## Forbidden contents

| Forbidden item | Reason |
|---|---|
| SourceDescriptor records | Registry roots own descriptors. |
| Source-family or product doctrine | `docs/sources/catalog/` owns doctrine. |
| Rights or sensitivity policy | `policy/` roots own policy. |
| Schemas or contracts | Schema/contract roots own machine contracts. |
| Processed, catalog, triplet, or published outputs | Downstream lifecycle roots own promoted artifacts. |
| Public API/UI behavior | Governed app roots own public behavior. |
| Network, filesystem, or credential side effects on import | Imports must be safe and deterministic. |

---

## Import and runtime rules

- Importing modules under this source root must not perform network calls.
- Importing modules must not write files.
- Importing modules must not read credentials.
- Importing modules must not activate a source.
- Runtime clients must require explicit descriptor/config inputs.
- Runtime writes must be restricted to explicit raw, quarantine, or receipt handoff helpers.
- Product helpers must preserve source-role separation for 3DEP, NHDPlus HR, NLCD, PAD-US, earthquakes, and future USGS product lanes.

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

Before relying on this source root, verify:

- actual directory contents are inventoried;
- package metadata points at the intended source root, if package metadata exists;
- imports are side-effect-free;
- no-network fixtures exist;
- package/module boundaries are documented;
- descriptor/config gates reject missing inputs;
- source-role metadata is preserved by helpers;
- output helpers cannot write processed/catalog/triplet/published data;
- CI runs relevant tests or this remains `NEEDS VERIFICATION`.

---

## Rollback

Rollback is required if this README is used to justify source authority, direct source activation, direct promotion, direct public access, or bypass of SourceDescriptor/policy gates.

Rollback target: initial blank file content SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

---

## Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [ ] Actual source-root contents are inventoried.
- [ ] Package metadata and import paths are verified.
- [ ] Import side effects are tested and absent.
- [ ] Descriptor/config gates are tested.
- [ ] Product-specific helper boundaries are documented.
- [ ] Raw/quarantine/receipt-only output boundaries are tested.
- [ ] No processed/catalog/triplet/published/release/API/UI authority lives here.
- [ ] Tests and CI behavior are verified or marked `NEEDS VERIFICATION`.

---

## Status summary

`connectors/usgs/src/` is a draft source-code root for USGS connector helper packages. It is not USGS source-family doctrine, product doctrine, SourceDescriptor authority, policy authority, schema authority, catalog/triplet authority, proof closure, release authority, public API behavior, public UI behavior, or pipeline authority.

<p align="right"><a href="#top">Back to top</a></p>
