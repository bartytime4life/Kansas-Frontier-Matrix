<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-ebird-src-ebird-readme
title: connectors/ebird/src/ebird/ — eBird Connector Python Package
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Source steward · Fauna steward · Sensitivity steward · Data steward · QA steward · Docs steward
created: 2026-07-10
updated: 2026-07-10
policy_label: restricted; package-readme; implementation-support; source-admission-only
related:
  - ../../README.md
  - ../README.md
  - ../../../../docs/sources/catalog/ebird/README.md
  - ../../../../docs/sources/catalog/ebird/ebird-api.md
  - ../../../../docs/sources/catalog/ebird/ebird-ebd.md
  - ../../../../docs/sources/catalog/ebird/ebird-sed.md
  - ../../../../docs/domains/fauna/README.md
  - ../../../../data/registry/sources/fauna/
  - ../../../../data/raw/fauna/
  - ../../../../data/quarantine/fauna/
  - ../../../../data/receipts/fauna/
  - ../../../../data/proofs/fauna/
  - ../../../../policy/sensitivity/
  - ../../../../release/
tags: [kfm, connectors, ebird, python-package, fauna, birds, biodiversity, source-admission, sensitivity, raw, quarantine, receipts, no-network-on-import, governance]
notes:
  - "Package-level README for importable eBird connector helper code."
  - "This package supports descriptor-gated source admission; it does not own eBird source-family doctrine, fauna doctrine, source descriptors, schemas, policy, proof closure, release decisions, public APIs, maps, or UI behavior."
  - "Imports must be side-effect-free: no network calls, filesystem writes, credential reads, source activation, or public occurrence emission at import time."
  - "Connector package outputs may support raw, quarantine, and receipt handoffs only."
  - "Concrete modules, exports, dependencies, credentials, tests, fixtures, CI coverage, and runtime behavior remain NEEDS VERIFICATION until inventoried."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# eBird Connector Python Package

> Importable eBird connector helpers for governed fauna source admission. This package is not a source-family authority, fauna truth system, or publication path.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Owner: OWNER_TBD" src="https://img.shields.io/badge/owner-OWNER__TBD-lightgrey">
  <img alt="Scope: implementation support" src="https://img.shields.io/badge/scope-implementation__support-blue">
  <img alt="Import: side effect free" src="https://img.shields.io/badge/import-side--effect--free-green">
  <img alt="Sensitivity: fail closed" src="https://img.shields.io/badge/sensitivity-fail__closed-red">
  <img alt="Lifecycle: raw quarantine receipts" src="https://img.shields.io/badge/lifecycle-raw%20%7C%20quarantine%20%7C%20receipts-orange">
</p>

`connectors/ebird/src/ebird/`

## Quick jumps

[Status](#status) · [Scope](#scope) · [Package fit](#package-fit) · [Allowed code](#allowed-code) · [Forbidden code](#forbidden-code) · [Admission contract](#admission-contract) · [Product-family separation](#product-family-separation) · [Sensitivity boundary](#sensitivity-boundary) · [I/O boundary](#io-boundary) · [Bounded outcomes](#bounded-outcomes) · [Validation](#validation) · [Rollback](#rollback) · [Definition of done](#definition-of-done)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / `NEEDS VERIFICATION`  
> **Owner:** `OWNER_TBD`  
> **Path:** `connectors/ebird/src/ebird/`  
> **Mode:** importable connector helper package  
> **Truth posture:** `CONFIRMED` path and package-name metadata; actual Python modules, exports, dependency configuration, source activation, credentials, fixtures, tests, CI wiring, emitted receipts, and runtime behavior remain `NEEDS VERIFICATION`.

> [!CAUTION]
> Exact bird-occurrence data can expose sensitive species, nesting sites, roosts, migration concentrations, private-property activity, or observer-linked locations. Package code must fail closed and must not emit public-ready exact occurrence data.

---

## Scope

`connectors/ebird/src/ebird/` is the Python package namespace for eBird connector implementation support.

It may contain pure helpers, typed DTOs, constants, descriptor-gated client adapters, response parsers, checklist or observation normalizers, taxonomy and product metadata helpers, digest helpers, retry/rate-limit helpers, run-receipt helpers, raw/quarantine handoff helpers, and deterministic test support.

It must not become:

- eBird source-family doctrine;
- fauna doctrine or taxonomy authority;
- source descriptor or source activation authority;
- schema, contract, rights, or sensitivity policy authority;
- occurrence confirmation or range truth;
- catalog, triplet, EvidenceBundle, proof, or release authority;
- public API, map, tile, export, AI, or UI behavior;
- a route around geoprivacy, source terms, review, or publication controls.

---

## Package fit

```text
connectors/ebird/
├── README.md
├── pyproject.toml
└── src/
    └── ebird/
        └── README.md
```

The package supports the parent connector lane. It does not choose product-family activation, source roles, rights posture, canonical taxonomy, public generalization, or release state.

Related responsibility roots:

```text
docs/sources/catalog/ebird/   # source-family and product documentation
docs/domains/fauna/           # fauna doctrine and domain boundaries
data/registry/sources/fauna/  # SourceDescriptors and activation state
data/raw/fauna/               # admitted source payloads
data/quarantine/fauna/        # held or sensitive material
data/receipts/fauna/          # run and validation receipts
data/proofs/fauna/            # EvidenceBundles and proof packs
policy/sensitivity/           # geoprivacy and release policy
release/                      # release, correction, and rollback decisions
```

---

## Allowed code

| Allowed item | Required posture |
|---|---|
| Pure constants and enums | Descriptive only; do not replace source descriptors, schemas, taxonomy registries, or policy vocabulary. |
| Descriptor-gated client helpers | Require explicit SourceDescriptor/config input; no implicit activation. |
| API or file-product adapters | Preserve product family, source identifiers, retrieval context, access mode, and limitation fields. |
| Observation/checklist parsers | Preserve native identifiers, timestamps, spatial precision, effort/context fields, and review flags. |
| Taxonomy metadata helpers | Preserve source taxonomy identifiers and crosswalk inputs; never assert canonical identity by themselves. |
| Digest/checksum helpers | Deterministic and side-effect-free unless given explicit bytes or paths. |
| Rate-limit/retry helpers | Bounded, configurable, observable, and incapable of unbounded loops. |
| Run-receipt helpers | Produce structured payloads for success, denial, quarantine, no-op, rate-limit, skip, or error states. |
| Raw/quarantine handoff helpers | Require explicit destination and receipt metadata; never write processed, catalog, or published data. |
| Test support helpers | Offline, deterministic, non-sensitive, and not fixture authority. |

---

## Forbidden code

| Forbidden behavior | Reason / correct boundary |
|---|---|
| Network calls at import time | Imports must be safe, deterministic, and testable. |
| Filesystem writes at import time | Importing the package must not mutate lifecycle data. |
| Credential or secret reads at import time | Credentials belong in explicit runtime configuration. |
| Implicit source activation | Activation belongs to governed source descriptors and registry state. |
| Direct writes to processed/catalog/triplets/published | Connectors are admission-only; downstream stages own promotion. |
| Embedded rights or sensitivity policy | Policy belongs in policy roots and governed gates. |
| Public-ready exact occurrence outputs | Sensitive release requires downstream policy, review, transformation, and release state. |
| Canonical taxonomy assertions | Taxonomy resolution requires governed identity and evidence processes. |
| Observer or account profiling | Personal or contributor metadata must not be repurposed beyond approved source handling. |
| Public API, tile, map, export, or UI builders | Public clients use governed interfaces and released artifacts. |

---

## Admission contract

Package helpers must preserve, when available and allowed:

- SourceDescriptor reference supplied by the caller;
- eBird product family and access mode;
- source observation, checklist, taxonomy, location, or sampling-event identifiers;
- retrieval time and source publication/update time;
- observation/checklist start time and duration where supplied;
- coordinates, source precision, location identifier, and spatial uncertainty or withholding state;
- species/taxon source identifier and source taxonomy version where supplied;
- count, presence, absence, effort, protocol, completeness, and review-status fields without strengthening them;
- rights, terms, sensitivity, embargo, and limitation posture passed by governing gates;
- content digest and response metadata;
- run identifier, receipt reference, and rollback target where applicable.

No helper should claim that a record is confirmed, complete, canonical, public-safe, activated, published, or authoritative without downstream evidence and release state.

---

## Product-family separation

The package must preserve distinctions among product families and access modes.

| Product or record family | Required separation |
|---|---|
| eBird API responses | Near-real-time service responses; endpoint, query, rate-limit, and access constraints remain explicit. |
| EBD | Bulk observation and sampling-event product; release/vintage and accompanying metadata remain explicit. |
| SED or sampling-event data | Effort and checklist context; not interchangeable with occurrence rows. |
| Taxonomy data | Source taxonomy/version context; not canonical KFM taxonomic truth. |
| Hotspot/location metadata | Source location context; not proof of public access, ownership, habitat condition, or safe disclosure. |
| Derived summaries | Remain derived outputs; they do not replace source observations or governed evidence closure. |

Do not silently collapse:

- checklist presence into complete absence evidence;
- observation counts into population estimates;
- hotspot geometry into habitat boundaries;
- reviewed status into KFM proof closure;
- source taxonomy into canonical cross-domain identity;
- current API results into stable historical coverage;
- precise coordinates into public-safe coordinates.

---

## Sensitivity boundary

Sensitive fauna handling is deny-by-default.

Package code must preserve or surface:

- source-provided obscuration, withholding, review, or sensitivity indicators;
- exact versus generalized geometry state;
- temporal precision and age of the observation;
- species sensitivity or policy-review requirement supplied by governing inputs;
- private-property, observer-linked, or contributor-linked exposure risk;
- quarantine reason and required review route.

Package code must not:

- reverse source obscuration;
- infer exact locations from generalized outputs;
- log exact sensitive coordinates, API keys, contributor details, or private identifiers;
- place sensitive payloads in fixtures, snapshots, error messages, or generated reports;
- decide public generalization distances or publication eligibility on its own.

---

## I/O boundary

```text
MAY SUPPORT:
  data/raw/fauna/<source_id>/<run_id>/
  data/quarantine/fauna/<source_id>/<run_id>/
  data/receipts/fauna/<run_id>/

MUST NOT OWN:
  data/work/
  data/processed/
  data/catalog/
  data/triplets/
  data/published/
  data/proofs/ as closure authority
  release/ decisions
  public API, map, tile, export, AI, or UI behavior
```

Receipts record what a connector run attempted and observed. They are not proof closure, source activation, policy approval, or publication authority.

---

## Bounded outcomes

Connector entry points should return finite, inspectable outcomes rather than ambiguous booleans or silent fallback:

| Outcome | Meaning |
|---|---|
| `admit_raw` | Payload passed admission checks and may enter the explicit raw target. |
| `quarantine` | Payload requires rights, sensitivity, integrity, taxonomy, or steward review. |
| `deny` | Policy, rights, credential, source, or configuration conditions prohibit admission. |
| `no_change` | A verified digest or source version indicates no new material. |
| `rate_limited` | Source throttling prevented completion; retry posture is explicit. |
| `skipped` | Required descriptor, product, configuration, or precondition was absent. |
| `error` | Retrieval, parsing, validation, integrity, or handoff failed. |

Each outcome should carry a stable reason code, source/product identity, run ID, timestamps, and receipt-ready details without leaking secrets or sensitive locations.

---

## Validation

Before relying on this package, verify:

- [ ] Actual modules and public exports are inventoried.
- [ ] Package discovery and installation are verified.
- [ ] Imports perform no network, filesystem, credential, or activation side effects.
- [ ] SourceDescriptor/config inputs are mandatory for network or handoff behavior.
- [ ] API keys and credentials are runtime-injected and never logged.
- [ ] API, EBD, SED, taxonomy, and location product roles remain distinct.
- [ ] Parsers preserve source IDs, source times, effort/context, taxonomy version, precision, and sensitivity fields.
- [ ] Obscured or withheld locations cannot be reconstructed or published by package helpers.
- [ ] Retry, timeout, pagination, and rate-limit behavior are bounded and configurable.
- [ ] Raw/quarantine/receipt helpers cannot write processed, catalog, triplet, proof-closure, published, or release records.
- [ ] Offline fixtures are tiny, non-sensitive, rights-safe, and provenance-labeled.
- [ ] Tests cover admit, quarantine, deny, no-change, rate-limited, skipped, and error outcomes.
- [ ] CI runs the relevant tests or the package remains `NEEDS VERIFICATION`.

---

## Rollback

Rollback is required if this README or package is used to justify:

- direct public access to connector outputs;
- release of exact sensitive occurrence data;
- implicit source activation;
- bypass of SourceDescriptor, rights, sensitivity, taxonomy, evidence, or release gates;
- import-time network, credential, filesystem, or activation side effects;
- direct writes to processed, catalog, triplet, proof-closure, published, or release roots.

Rollback target: prior placeholder blob `e25f1814e51579d5f55c0f1fe0135ddb28a47f4a`.

---

## Evidence basis

| Source | Status | Supports | Limits |
|---|---|---|---|
| `connectors/ebird/README.md` | `CONFIRMED` | Connector-lane scope, product families, restricted rights/sensitivity posture, raw/quarantine boundary | Does not prove package implementation or runtime behavior |
| `connectors/ebird/pyproject.toml` | `CONFIRMED` | Greenfield package name `kfm-connector-ebird`, version `0.0.0` | Does not prove package discovery, dependencies, modules, tests, or installability |
| `connectors/ebird/src/ebird/README.md` prior content | `CONFIRMED` | Placeholder existed at the requested path | Provides no implementation evidence |

---

## Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [ ] Actual Python modules and exports are inventoried.
- [ ] Package discovery, dependencies, and installation are verified.
- [ ] Imports are side-effect-free.
- [ ] Product-family adapters and SourceDescriptor/config gates are documented and tested.
- [ ] Sensitive-location, rights, contributor, and credential handling fail closed.
- [ ] Raw/quarantine/receipt-only boundaries are tested.
- [ ] No processed, catalog, triplet, proof-closure, published, release, policy, schema, registry, public API, map, tile, export, AI, or UI authority lives here.
- [ ] Tests and CI behavior are verified or marked `NEEDS VERIFICATION`.

---

## Status summary

`connectors/ebird/src/ebird/` is a draft implementation-support package for governed eBird source admission. It is not eBird source-family authority, fauna truth, taxonomy authority, rights or sensitivity policy, EvidenceBundle closure, release authority, publication authority, or a public delivery surface.

<p align="right"><a href="#top">Back to top</a></p>
