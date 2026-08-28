<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-blm-src-readme
title: connectors/blm/src/ — BLM Connector Source Tree
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Connector steward · Source steward · Land/Cadastral steward · Data steward · Validation steward · Docs steward
created: 2026-06-16
updated: 2026-07-10
policy_label: public; package-source-root; implementation-support; source-admission-only
related:
  - ../README.md
  - ./blm/README.md
  - ../tests/README.md
  - ../../../docs/sources/catalog/blm.md
  - ../../../data/registry/sources/
  - ../../../data/raw/
  - ../../../data/quarantine/
  - ../../../data/receipts/
  - ../../../data/proofs/
  - ../../../policy/rights/
  - ../../../policy/sensitivity/
  - ../../../release/
tags: [kfm, connectors, blm, src, python-source-root, source-admission, side-effect-free-import, raw, quarantine, receipts, governance]
notes:
  - "v0.2 updates the BLM connector source-tree contract without claiming unverified package modules or runtime behavior."
  - "connectors/blm/src/ is a Python source-root container, not BLM source truth, registry authority, schema authority, policy authority, proof authority, release authority, or publication authority."
  - "Imports below this root must be side-effect-free: no network calls, filesystem writes, credential reads, source activation, or lifecycle mutation at import time."
  - "Implementation may support explicit raw, quarantine, and receipt handoffs only; downstream governed stages own processing, catalog, triplets, proofs, release, and publication."
  - "Concrete package discovery, modules, exports, dependencies, tests, fixtures, CI coverage, source activation, endpoints, and runtime behavior remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# BLM Connector Source Tree

> Python source-root boundary for importable Bureau of Land Management connector code. This tree supports governed source admission; it does not establish land, title, access, cadastral, mineral, cultural-resource, or publication truth.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Owner: OWNER_TBD" src="https://img.shields.io/badge/owner-OWNER__TBD-lightgrey">
  <img alt="Scope: Python source root" src="https://img.shields.io/badge/scope-python__source__root-blue">
  <img alt="Import: side effect free" src="https://img.shields.io/badge/import-side--effect--free-green">
  <img alt="Lifecycle: raw quarantine receipts" src="https://img.shields.io/badge/lifecycle-raw%20%7C%20quarantine%20%7C%20receipts-orange">
</p>

`connectors/blm/src/`

## Quick jumps

[Status](#status) · [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted contents](#accepted-contents) · [Exclusions](#exclusions) · [Source-root contract](#source-root-contract) · [Import safety](#import-safety) · [Package discovery](#package-discovery) · [I/O boundary](#io-boundary) · [BLM anti-collapse rules](#blm-anti-collapse-rules) · [Validation](#validation) · [Safe change pattern](#safe-change-pattern) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Definition of done](#definition-of-done)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / `NEEDS VERIFICATION`  
> **Owner:** `OWNER_TBD`  
> **Path:** `connectors/blm/src/`  
> **Mode:** Python source-root container for the BLM connector package  
> **Truth posture:** `CONFIRMED` README path, parent connector README, and adjacent package README. Actual package discovery, Python modules, exports, dependencies, tests, fixtures, CI wiring, endpoints, source activation, emitted receipts, and runtime behavior remain `NEEDS VERIFICATION`.

---

## Scope

`connectors/blm/src/` contains importable source code for the BLM connector package.

Code below this root may support:

- descriptor-gated request and client construction;
- service, layer, package, and record locators;
- source-family and dataset-family metadata parsing;
- source-native identifier preservation;
- scale, vintage, rights, source-role, and limitation metadata;
- deterministic digest and retrieval metadata helpers;
- bounded probe and admission outcomes;
- explicit raw, quarantine, and receipt handoff preparation;
- offline, deterministic test support that does not become fixture authority.

This source root must not decide final truth, activate a source implicitly, write downstream lifecycle records, close EvidenceBundles, approve release, produce public API/UI behavior, or publish artifacts.

---

## Repo fit

```text
connectors/
└── blm/
    ├── README.md
    ├── src/
    │   ├── README.md
    │   └── blm/
    │       └── README.md
    └── tests/
        └── README.md
```

| Surface | Relationship to this source root |
|---|---|
| `../README.md` | Defines the BLM connector-family boundary and source-admission posture. |
| `./blm/README.md` | Defines the importable `blm` package namespace. |
| `../tests/` | Owns connector-local test organization where that convention is verified. |
| `../../../docs/sources/catalog/blm.md` | Human-facing BLM source profile and authority limits. |
| `../../../data/registry/sources/` | SourceDescriptor and activation authority. This source tree consumes references; it does not own them. |
| `../../../policy/rights/`, `../../../policy/sensitivity/` | Rights and sensitivity gates supplied by governed orchestration. |
| `../../../data/raw/`, `../../../data/quarantine/`, `../../../data/receipts/` | Permitted handoff surfaces when explicitly supplied by the caller. |
| `../../../data/work/`, `processed/`, `catalog/`, `triplets/`, `proofs/`, `published/` | Downstream lifecycle surfaces outside this source root. |
| `../../../release/` | Release, correction, rollback, and publication decisions outside connector ownership. |

---

## Accepted contents

| Belongs under `connectors/blm/src/` | Required posture |
|---|---|
| Python package directories | Package names and discovery must match verified package metadata. |
| Package-local documentation | Describe boundaries and interfaces without claiming unverified runtime behavior. |
| Pure constants and enums | Descriptive only; must not replace registry, schema, policy, or source-role authority. |
| Descriptor-gated client adapters | Require explicit configuration and SourceDescriptor reference; no implicit activation. |
| Metadata and response parsers | Preserve source-native fields, source role, scale, vintage, and limitations. |
| Digest and checksum helpers | Deterministic and side-effect-free unless passed explicit bytes or paths. |
| Bounded outcome types | Represent admit, quarantine, deny, skip, no-op, rate-limit, stale, and error states without promotion. |
| Raw/quarantine/receipt handoff helpers | Require explicit destinations and metadata; never infer or hard-code lifecycle homes. |
| Offline test-support utilities | Small, deterministic, and non-authoritative. |

---

## Exclusions

| Does not belong here | Correct responsibility root |
|---|---|
| Raw or quarantine payload files | `../../../data/raw/`, `../../../data/quarantine/` |
| Processed domain records | `../../../data/processed/` |
| Catalog or triplet records | `../../../data/catalog/`, `../../../data/triplets/` |
| EvidenceBundle or proof closure | `../../../data/proofs/` and governed proof workflows |
| SourceDescriptor records or activation decisions | `../../../data/registry/sources/` |
| Rights or sensitivity policy | `../../../policy/rights/`, `../../../policy/sensitivity/` |
| Machine-schema authority | `../../../schemas/contracts/` after accepted placement |
| Human contract authority | `../../../contracts/` |
| Release, correction, or rollback decisions | `../../../release/` |
| Public API, UI, map, or AI behavior | Governed application roots after evidence, policy, review, and release gates |
| Generated reports and QA artifacts | `../../../artifacts/` |
| Secrets, tokens, credentials, or local credential caches | Approved secret/runtime configuration surfaces; never source control |

---

## Source-root contract

Every importable package beneath this root should receive consequential runtime inputs explicitly rather than discovering authority implicitly.

Expected injected inputs may include:

- SourceDescriptor reference and activation state;
- source-family and dataset-family identifiers;
- endpoint, service, layer, package, or record locator;
- request timeout, retry, backoff, rate-limit, and user-agent configuration;
- rights, sensitivity, review, and access posture;
- source role and authority scope;
- source version, vintage, scale, epoch, and update cadence;
- explicit raw, quarantine, and receipt destinations;
- run ID, retrieval time, digest algorithm, and receipt metadata.

> [!CAUTION]
> Hard-coded endpoints may be implementation defaults only when verified and overrideable. Hard-coded source activation, rights approval, publication permission, or lifecycle destinations are prohibited.

---

## Import safety

Importing any package below `connectors/blm/src/` must not:

- make network requests;
- read credentials or secrets;
- activate a source;
- write files or lifecycle records;
- create directories;
- mutate environment variables;
- emit release, catalog, proof, or publication decisions;
- start background workers, schedules, or polling loops;
- log sensitive locations, credentials, tokens, or protected records.

Module import should be deterministic and safe in tests, documentation tooling, type checking, and static analysis.

---

## Package discovery

Package discovery and import paths remain `NEEDS VERIFICATION` until checked against package metadata and tests.

Before treating this layout as operational, confirm:

1. the build metadata points to `connectors/blm/src/`;
2. the import namespace is `blm` or another explicitly documented name;
3. accidental namespace packages are not created;
4. package data excludes raw payloads, credentials, large fixtures, and generated artifacts;
5. public exports are explicit or intentionally absent;
6. imports succeed without network, filesystem, or credential side effects.

---

## I/O boundary

```text
MAY PREPARE OR SUPPORT:
  data/raw/<domain>/<source_id>/<run_id>/
  data/quarantine/<domain>/<source_id>/<run_id>/
  data/receipts/<run_id>/

MUST NOT OWN OR WRITE DIRECTLY:
  data/work/
  data/processed/
  data/catalog/
  data/triplets/
  data/proofs/ as closure authority
  data/published/
  release/ decisions
  apps/ public API or UI behavior
```

Receipt helpers may describe a connector run, probe, denial, no-op, rate limit, or admission attempt. A receipt is not proof closure, catalog closure, legal interpretation, or publication authority.

---

## BLM anti-collapse rules

Package code must preserve distinctions among BLM dataset families and the claims they can support.

| Source context | Must not be silently treated as |
|---|---|
| PLSS or CadNSDI reference geometry | Current parcel ownership, legal title, surveyed boundary conclusiveness, or county cadastral authority |
| Surface-management or administrative boundaries | Fee-simple ownership, access permission, jurisdictional certainty, or local legal advice |
| Roads, trails, or access layers | Guaranteed legal access, current road condition, emergency route, or local road authority |
| Mineral or land-record context | Mineral ownership, active legal right, title opinion, lease status, or final regulatory determination |
| Historic land records and GLO materials | Present ownership, present boundary, or present-day legal status without crosswalk and review |
| Recreation and conservation layers | Universal access, safety guarantee, habitat truth, or land-use permission |
| Fire, range, vegetation, and wildlife context | Official incident command, ecological ground truth, species-location publication approval, or hazard instruction |
| Cultural-resource-related material | Public-safe exact location, consultation completion, consent, or release approval |

Exact or sensitive locations involving archaeology, sacred or cultural resources, rare species, infrastructure, private holdings, or security concerns must fail closed to quarantine unless policy and review inputs explicitly permit handling.

---

## Validation

Before relying on this source tree, verify:

- [ ] package metadata and source-root discovery are correct;
- [ ] actual package directories and modules are inventoried;
- [ ] imports are side-effect-free;
- [ ] SourceDescriptor/configuration inputs are explicit and required;
- [ ] endpoint and request behavior is configurable and bounded;
- [ ] parsers preserve source-native fields, source role, scale, vintage, rights, and limitations;
- [ ] no-network fixtures cover representative success and failure cases;
- [ ] bounded outcomes cover success, quarantine, denial, skip, no-op, stale input, rate limiting, and error;
- [ ] output helpers cannot write work, processed, catalog, triplet, proof-closure, published, or release records;
- [ ] logs and exceptions do not expose credentials or protected locations;
- [ ] CI runs the relevant checks or the gap remains `NEEDS VERIFICATION`.

---

## Safe change pattern

For changes under `connectors/blm/src/`:

1. Confirm the file is importable connector code, package-local documentation, or source-root support material.
2. Confirm package discovery and import paths remain valid.
3. Confirm imports produce no network, filesystem, credential, activation, or lifecycle side effects.
4. Confirm SourceDescriptor, source role, rights, sensitivity, scale, vintage, and limitation inputs are preserved.
5. Confirm outputs remain limited to explicit raw, quarantine, and receipt handoffs.
6. Confirm dataset-family distinctions and sensitive-location controls remain intact.
7. Update tests and fixtures or mark the exact gap `NEEDS VERIFICATION`.
8. Update adjacent documentation when interfaces or package layout change.

---

## Evidence basis

| Evidence | Status | Supports | Does not prove |
|---|---|---|---|
| Existing `connectors/blm/src/README.md` v0.1 | `CONFIRMED` | Source-tree path, intended source-admission boundary, prior exclusions, and prior validation posture | Actual modules, imports, tests, package discovery, or runtime behavior |
| `connectors/blm/src/blm/README.md` v0.2 | `CONFIRMED` documentation | Adjacent package boundary, import-safety expectation, dataset-family anti-collapse, and I/O limits | Implementation conformance or source activation |
| `connectors/blm/README.md` | `CONFIRMED` documentation | Parent connector-family purpose and BLM source limitations | Endpoint health, rights clearance, registry activation, or release state |
| Current repository inspection | `PARTIAL / NEEDS VERIFICATION` | Target and adjacent README paths exist | Complete recursive inventory, CI results, emitted receipts, deployment, or runtime state |

---

## Rollback

Rollback is required if this README or a source-tree change is used to justify:

- network, credential, filesystem, activation, or lifecycle mutation at import time;
- direct writes beyond raw, quarantine, or receipt handoffs;
- embedded SourceDescriptor, schema, policy, proof, catalog, release, API, UI, or publication authority;
- BLM material as conclusive parcel, title, ownership, access, legal, ecological, cultural-resource, or hazard truth;
- exposure of protected locations or sensitive records;
- undocumented package-discovery or import-path breakage.

Rollback target: prior blob `4791da8fe594c0345c059521915ae78fffc97e71`.

---

## Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [ ] Package metadata and `src`-layout discovery are verified.
- [ ] Actual package directories and modules are inventoried.
- [ ] Public exports are documented or intentionally absent.
- [ ] Import side effects are tested and absent.
- [ ] Descriptor/configuration gates are tested.
- [ ] Dataset-family and authority distinctions are preserved.
- [ ] Sensitive-location handling fails closed.
- [ ] Raw/quarantine/receipt-only handoff boundaries are tested.
- [ ] No processed/catalog/triplet/proof-closure/published/release/API/UI authority lives here.
- [ ] Tests, fixtures, and CI behavior are verified or marked `NEEDS VERIFICATION`.

---

## Status summary

`connectors/blm/src/` is the Python source-root container for the BLM connector package. It may support descriptor-gated source intake and explicit raw, quarantine, and receipt handoffs. It is not BLM or land truth, registry authority, schema authority, policy authority, catalog/triplet authority, proof closure, release authority, public API/UI behavior, publication authority, fixture authority, or generated-report storage.

<p align="right"><a href="#top">Back to top</a></p>
