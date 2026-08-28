<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-blm-src-blm-readme
title: connectors/blm/src/blm/ — BLM Connector Python Package
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Connector steward · Source steward · Land/Cadastral steward · Data steward · Validation steward · Policy steward · Docs steward
created: 2026-06-16
updated: 2026-07-10
policy_label: public; package-readme; implementation-support; source-admission-only
related:
  - ../../README.md
  - ../../../README.md
  - ../../tests/README.md
  - ../../../../docs/sources/catalog/blm.md
  - ../../../../data/registry/sources/
  - ../../../../data/raw/
  - ../../../../data/quarantine/
  - ../../../../data/receipts/
  - ../../../../data/proofs/
  - ../../../../policy/rights/
  - ../../../../policy/sensitivity/
  - ../../../../release/
tags: [kfm, connectors, blm, python-package, source-admission, land-status, cadastral, plss, public-lands, raw, quarantine, receipts, no-network-on-import, governance]
notes:
  - "v0.2 preserves the v0.1 package boundary and strengthens import safety, SourceDescriptor gating, dataset-family separation, bounded outcomes, sensitive-location handling, validation, and rollback."
  - "connectors/blm/src/blm/ is implementation support for governed BLM source admission only."
  - "Imports must be side-effect-free: no network calls, filesystem writes, credential reads, source activation, or lifecycle mutation at import time."
  - "Package outputs may support raw, quarantine, and receipt handoffs only; processed, catalog, triplet, proof closure, release, API, UI, and publication authority remain outside this package."
  - "Specific modules, public exports, dependency pins, runtime behavior, tests, fixtures, source activation, and CI enforcement remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# BLM Connector Python Package

> Importable implementation support for governed Bureau of Land Management source admission. This package may help fetch, parse, identify, and stage BLM source material; it does not establish land truth, legal interpretation, access rights, cadastral authority, policy, proof closure, or publication state.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Owner: OWNER_TBD" src="https://img.shields.io/badge/owner-OWNER__TBD-lightgrey">
  <img alt="Scope: implementation support" src="https://img.shields.io/badge/scope-implementation__support-blue">
  <img alt="Import: side effect free" src="https://img.shields.io/badge/import-side--effect--free-green">
  <img alt="Lifecycle: raw quarantine receipts" src="https://img.shields.io/badge/lifecycle-raw%20%7C%20quarantine%20%7C%20receipts-orange">
</p>

`connectors/blm/src/blm/`

## Quick jumps

[Status](#status) · [Scope](#scope) · [Package fit](#package-fit) · [Accepted code](#accepted-code) · [Exclusions](#exclusions) · [Import safety](#import-safety) · [Admission contract](#admission-contract) · [Dataset-family discipline](#dataset-family-discipline) · [Sensitive and legal boundaries](#sensitive-and-legal-boundaries) · [I/O boundary](#io-boundary) · [Bounded outcomes](#bounded-outcomes) · [Validation](#validation) · [Safe change pattern](#safe-change-pattern) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Definition of done](#definition-of-done)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / `NEEDS VERIFICATION`  
> **Owner:** `OWNER_TBD`  
> **Path:** `connectors/blm/src/blm/`  
> **Mode:** importable BLM connector helper package  
> **Truth posture:** `CONFIRMED` package README path, parent BLM connector README, and documentation boundary. Actual Python modules, public exports, dependency metadata, endpoint support, SourceDescriptor activation, tests, fixtures, emitted receipts, CI wiring, runtime outputs, and release behavior remain `NEEDS VERIFICATION`.

> [!CAUTION]
> A BLM record is not automatically current land status, legal title, county parcel truth, access permission, road authority, mineral ownership, cultural-resource clearance, habitat truth, or final boundary authority. Preserve source scope and route uncertainty through quarantine or review.

---

## Scope

`connectors/blm/src/blm/` is the Python package namespace for BLM connector implementation support.

It may contain small, testable helpers for:

- descriptor-gated BLM clients and request construction;
- endpoint, service, layer, package, and record locators;
- response, metadata, manifest, and package parsers;
- content-type, checksum, digest, and retrieval metadata handling;
- source-family and dataset-family preservation;
- source vintage, scale, generalization, and authority-scope preservation;
- bounded run-result and receipt-input construction;
- explicit raw or quarantine handoff preparation;
- deterministic no-network fixture support.

It must not become BLM source-family doctrine, SourceDescriptor authority, schema authority, rights policy, sensitivity policy, legal interpretation, cadastral authority, processed-data authority, catalog/triplet authority, proof authority, release authority, public API behavior, public UI behavior, map-layer authority, or publication authority.

---

## Package fit

```text
connectors/
└── blm/
    ├── README.md
    ├── tests/
    └── src/
        └── blm/
            └── README.md
```

Adjacent responsibility roots:

| Surface | Relationship to this package |
|---|---|
| `connectors/blm/README.md` | Defines the source-family connector boundary. |
| `docs/sources/catalog/blm.md` | Human-facing BLM source profile and limitations. |
| `data/registry/sources/` | Owns SourceDescriptor and activation state. |
| `policy/rights/`, `policy/sensitivity/` | Own rights, access, sensitivity, and fail-closed decisions. |
| `data/raw/`, `data/quarantine/`, `data/receipts/` | Allowed governed handoff surfaces. |
| `data/work/`, `data/processed/`, `data/catalog/`, `data/triplets/`, `data/proofs/`, `data/published/` | Downstream lifecycle and evidence surfaces outside package ownership. |
| `release/` | Owns release, correction, supersession, and rollback decisions. |

---

## Accepted code

| Accepted item | Required posture |
|---|---|
| Pure constants and enums | Descriptive only; must not replace source descriptors, schemas, or policy vocabularies. |
| Descriptor-gated clients | Require explicit descriptor/config inputs; no implicit source activation. |
| Endpoint and layer adapters | Preserve endpoint family, service/layer identity, version, and source scope. |
| Metadata and package parsers | Preserve source-native fields, dataset-family identity, vintage, scale, and limitation text. |
| Digest/checksum helpers | Deterministic and side-effect-free unless passed explicit bytes or paths. |
| Run-result and receipt helpers | Represent success, failure, denial, no-op, skipped, rate-limited, stale, and quarantine outcomes. |
| Raw/quarantine handoff helpers | Require explicit destination and lineage metadata; never write downstream lifecycle objects. |
| Test support helpers | Offline, deterministic, sanitized, and non-authoritative. |

---

## Exclusions

| Does not belong here | Correct responsibility root or behavior |
|---|---|
| Source descriptors or activation decisions | `data/registry/sources/` |
| Machine contracts or schemas | `schemas/contracts/v1/` and accepted contract homes |
| Rights, access, or sensitivity policy | `policy/rights/`, `policy/sensitivity/` |
| County parcel, title, deed, or ownership conclusions | Governed land/title domain workflows with appropriate evidence and review |
| Processed land, PLSS, cadastral, recreation, range, fire, or resource records | `data/processed/` after governed processing |
| Catalog or triplet records | `data/catalog/`, `data/triplets/` |
| EvidenceBundle or proof closure | `data/proofs/` and governed proof workflows |
| Published layers or exports | `data/published/` after release gates |
| Release, correction, or rollback decisions | `release/` |
| Public API, map, UI, or AI payload builders | Governed app/UI roots downstream of release and policy checks |
| Generated reports and QA output | `artifacts/` |

---

## Import safety

Imports must be side-effect-free.

Importing this package must not:

- make network requests;
- read credentials, tokens, or secrets;
- activate a source or select a default endpoint;
- write files or lifecycle data;
- create directories;
- mutate caches, databases, registries, or release state;
- emit public-facing claims;
- log sensitive locators, credentials, or protected coordinates.

Runtime clients must receive configuration explicitly from the caller or governed orchestration layer.

---

## Admission contract

Package helpers must preserve, when available:

- BLM source-family identifier;
- SourceDescriptor reference supplied by the caller;
- dataset-family, product-family, service, layer, package, or record identifier;
- endpoint or distribution locator;
- retrieval/import time;
- source publication, update, effective, or vintage time;
- source version, schema version, service version, or layer version;
- source-native identifiers;
- source role and authority scope;
- geographic extent, scale, resolution, and generalization notes;
- rights, access, redistribution, and review posture passed from governed inputs;
- content type, byte size, checksum, digest, or signature inputs;
- caveat, limitation, preliminary, stale, superseded, or correction state;
- quarantine reason and review route when admission cannot proceed safely;
- run receipt and rollback reference where applicable.

No helper may claim that a BLM product is current, legally controlling, cadastral truth, access authority, source-activated, published, or release-approved without registry, policy, evidence, and release support.

---

## Dataset-family discipline

BLM is a multi-product source family. Preserve distinctions rather than collapsing all records into generic “BLM data.”

| Dataset or access family | Required non-collapse posture |
|---|---|
| PLSS / CadNSDI context | Survey/reference context; not county parcel, deed, title, or ownership truth. |
| Surface-management and land-status layers | Versioned administrative context; not a substitute for current legal review. |
| General Land Office and historic land records | Historical documentary evidence; not automatic present-day ownership. |
| Mineral and land records systems | Administrative/resource context; not final mineral ownership or legal interpretation. |
| Recreation and access layers | Informational context; not a guarantee of legal, safe, or current access. |
| Roads and trails | Source-specific route context; not local road authority, maintenance, passability, or access permission. |
| Fire, range, vegetation, wildlife, and conservation products | Domain context whose source role and derivation must remain explicit. |
| ArcGIS REST, hubs, viewers, and download packages | Delivery surfaces, not sovereign truth or publication authority. |

Cross-domain relations may be created downstream through governed contracts. This package must not silently take ownership of cadastral, archaeology, ecology, hazards, roads, land-title, or public-access claims.

---

## Sensitive and legal boundaries

Fail closed or quarantine when material may expose or misrepresent:

- archaeological, sacred, burial, ceremonial, or culturally restricted locations;
- sensitive species, habitat, nesting, denning, or restoration locations;
- critical infrastructure or security-relevant assets;
- non-public land records, personal information, or restricted administrative details;
- exact locations whose exposure could enable looting, trespass, harassment, or resource damage;
- legal title, mineral ownership, easement, access, or jurisdiction conclusions unsupported by controlling evidence.

Sanitized fixtures must not contain protected coordinates, credentials, private records, or operational secrets.

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
  apps/ public API, map, UI, or AI behavior
```

Receipts prove that a connector action occurred or reached a bounded outcome. They do not prove land status, catalog closure, EvidenceBundle closure, or publication eligibility.

---

## Bounded outcomes

Connector operations should return a finite, reviewable outcome rather than silently retrying, promoting, or publishing.

| Outcome | Meaning |
|---|---|
| `admit_raw` | Source identity, descriptor, integrity, and initial policy requirements support raw admission. |
| `quarantine` | Material was captured but requires rights, sensitivity, identity, schema, freshness, or steward review. |
| `deny` | Admission is prohibited under current policy or source conditions. |
| `no_op` | No relevant source change or payload was found. |
| `stale` | Material was retrieved but cannot be treated as current without review. |
| `rate_limited` | The source declined or deferred the request; no silent bypass is allowed. |
| `skipped` | The run was intentionally not attempted, with a recorded reason. |
| `error` | The operation failed; partial material must not be silently promoted. |

---

## Validation

Before relying on this package, verify:

- [ ] actual Python modules and public exports are inventoried;
- [ ] package metadata and import paths are valid;
- [ ] imports are side-effect-free;
- [ ] no-network fixtures exist and contain no protected data;
- [ ] clients reject missing or inactive descriptor/config inputs;
- [ ] endpoint, layer, dataset-family, version, cadence, and timeout assumptions are configurable;
- [ ] parsers preserve source-native identifiers, source role, vintage, scale, and caveats;
- [ ] BLM dataset families remain distinct;
- [ ] raw/quarantine/receipt-only output boundaries are enforced;
- [ ] success, denial, quarantine, no-op, stale, skipped, rate-limited, and error outcomes are tested;
- [ ] downstream stages—not this package—produce processed, catalog, triplet, proof, release, and published objects;
- [ ] CI runs the relevant tests or the status remains `NEEDS VERIFICATION`.

---

## Safe change pattern

For changes under `connectors/blm/src/blm/`:

1. Confirm the file is BLM connector package code or package-local documentation.
2. Confirm imports remain side-effect-free.
3. Confirm every live source action requires explicit descriptor/config input.
4. Confirm source role, dataset family, rights posture, scale, vintage, identifiers, and limitations are preserved.
5. Confirm no legal, title, access, cadastral, cultural, ecological, or infrastructure conclusion is strengthened by convenience.
6. Confirm outputs are restricted to raw, quarantine, and receipt handoffs.
7. Update tests, fixtures, docs, and rollback notes—or mark the gap `NEEDS VERIFICATION`.

---

## Evidence basis

| Source | Status | Supports | Limits |
|---|---|---|---|
| `connectors/blm/src/blm/README.md` v0.1 | `CONFIRMED` baseline | Existing package purpose, allowed helpers, raw/quarantine boundary, source metadata preservation, validation, and exclusions | Did not prove module inventory, imports, tests, endpoints, or runtime behavior |
| `connectors/blm/README.md` v0.1 | `CONFIRMED` adjacent contract | BLM source-family scope, dataset families, rights/scale/vintage limits, and non-authoritative land/access posture | Does not prove active descriptors, endpoint health, or package implementation |
| `connectors/README.md` | `CONFIRMED` root contract | Connectors are source-admission infrastructure and do not publish or promote | Does not prove this package is complete or operational |
| Current GitHub update | `CONFIRMED` documentation change | This README was replaced in place and the prior blob is known | Does not prove runtime conformance |

---

## Rollback

Rollback is required if this README or package is used to justify:

- network, credential, filesystem, or lifecycle side effects during import;
- source activation without a governed SourceDescriptor;
- direct writes to processed, catalog, triplet, proof, published, or release surfaces;
- legal title, parcel, access, road, mineral ownership, or cadastral conclusions;
- exposure of protected cultural, ecological, infrastructure, or private locations;
- direct public API, map, UI, or AI access to connector internals;
- removal of source role, vintage, scale, caveat, or limitation metadata.

Rollback target: prior README blob `e55aee5559f1a880c10deecdecc4e56db5ec3695`.

---

## Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [ ] Actual package modules and public exports are inventoried.
- [ ] Package metadata, dependencies, and import paths are verified.
- [ ] Import side effects are tested and absent.
- [ ] SourceDescriptor and explicit configuration gates are tested.
- [ ] Dataset-family and source-role separation are tested.
- [ ] Legal, cadastral, access, cultural, ecological, and sensitive-location boundaries are tested.
- [ ] Raw/quarantine/receipt-only output boundaries are tested.
- [ ] Bounded outcomes and receipt inputs are covered by deterministic tests.
- [ ] No processed, catalog, triplet, proof, published, release, policy, schema, API, UI, map, AI, fixture-authority, or report authority lives here.
- [ ] Tests and CI behavior are verified or marked `NEEDS VERIFICATION`.

---

## Status summary

`connectors/blm/src/blm/` is a draft implementation-support package for governed BLM source admission. It is not BLM source-family doctrine, land or cadastral truth, legal interpretation, access authority, SourceDescriptor authority, policy authority, schema authority, catalog/triplet authority, proof closure, release authority, public API behavior, public map/UI/AI behavior, or publication authority.

<p align="right"><a href="#top">Back to top</a></p>
