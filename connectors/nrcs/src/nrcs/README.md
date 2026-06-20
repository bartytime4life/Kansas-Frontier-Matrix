<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-nrcs-src-nrcs-readme
title: connectors/nrcs/src/nrcs/ — NRCS Connector Python Package Boundary
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Source steward · NRCS steward · Soil steward · Agriculture steward · Hydrology steward · Ecology steward · Climate steward · Data steward · Validation steward · Docs steward
created: 2026-06-20
updated: 2026-06-20
policy_label: public-doctrine; import-safe; source-admission-only
related:
  - ../../README.md
  - ../../sda/README.md
  - ../../scan/README.md
  - ../../gssurgo/README.md
  - ../../gnatsgo/README.md
  - ../../../../nrcs-ssurgo/README.md
  - ../../../../nrcs-scan/README.md
  - ../../../../../docs/doctrine/directory-rules.md
  - ../../../../../docs/sources/catalog/nrcs.md
  - ../../../../../docs/sources/catalog/nrcs/README.md
  - ../../../../../docs/sources/catalog/nrcs/soil-data-access.md
  - ../../../../../docs/sources/catalog/nrcs/scan-soil-climate.md
  - ../../../../../docs/sources/catalog/nrcs/gssurgo.md
  - ../../../../../docs/sources/catalog/nrcs/ssurgo.md
  - ../../../../../docs/domains/soil/README.md
  - ../../../../../docs/domains/agriculture/README.md
  - ../../../../../docs/domains/hydrology/README.md
  - ../../../../../data/registry/sources/
  - ../../../../../data/raw/
  - ../../../../../data/quarantine/
  - ../../../../../data/receipts/
  - ../../../../../data/proofs/
  - ../../../../../policy/rights/
  - ../../../../../policy/sensitivity/
  - ../../../../../release/
tags: [kfm, connectors, nrcs, python-package, source-admission, import-safe, no-network-default, ssurgo, gssurgo, gnatsgo, sda, scan, soil, agriculture, hydrology, raw, quarantine, governance]
notes:
  - "Importable Python package boundary for NRCS connector implementation code under connectors/nrcs/src/."
  - "This README documents the package boundary only; actual modules, imports, package metadata, tests, fixtures, and CI wiring remain NEEDS VERIFICATION until inspected."
  - "Package import must be side-effect-free: no live network calls, no secret reads, no lifecycle writes, no publication, no public claims."
  - "Code in this package may prepare NRCS source material for raw or quarantine admission envelopes only."
  - "Source-family and product doctrine belong under docs/sources/catalog/nrcs.md and docs/sources/catalog/nrcs/; SourceDescriptors remain authoritative for role, rights, cadence, sensitivity, and activation state."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# NRCS Connector Python Package

> Importable package boundary for NRCS connector implementation code under `connectors/nrcs/src/nrcs/`.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Owner: OWNER_TBD" src="https://img.shields.io/badge/owner-OWNER__TBD-lightgrey">
  <img alt="Scope: package boundary" src="https://img.shields.io/badge/scope-python__package__boundary-blue">
  <img alt="Import: safe" src="https://img.shields.io/badge/import-safe-green">
  <img alt="Network: explicit only" src="https://img.shields.io/badge/network-explicit__only-orange">
  <img alt="Lifecycle: raw or quarantine only" src="https://img.shields.io/badge/lifecycle-raw%20%7C%20quarantine%20only-orange">
</p>

`connectors/nrcs/src/nrcs/`

## Scope

`connectors/nrcs/src/nrcs/` is the proposed importable Python package boundary for the NRCS connector family.

This package may contain implementation support for source-admission helpers, bounded request clients, product-specific parsers, query-manifest builders, station metadata parsers, raster/package metadata parsers, source-role checks, freshness checks, rights/citation helpers, sensitivity guard helpers, digest helpers, finite connector errors, and raw/quarantine admission-envelope builders.

It must not become NRCS source-family truth, NRCS product doctrine, Soil domain doctrine, source descriptor authority, schema authority, rights policy authority, sensitivity policy authority, release authority, public API behavior, public UI behavior, processed-data logic, catalog/triplet authority, proof authority, or publication authority.

> [!IMPORTANT]
> **Status:** draft / `NEEDS VERIFICATION`  
> **Owner:** `OWNER_TBD`  
> **Path:** `connectors/nrcs/src/nrcs/`  
> **Truth posture:** the path exists in the repository as this README; actual package files, imports, module names, dependency wiring, endpoint clients, fixtures, tests, and CI behavior remain `NEEDS VERIFICATION`.

---

## Repo fit

```text
connectors/
└── nrcs/
    ├── README.md
    ├── src/
    │   └── nrcs/
    │       └── README.md
    ├── sda/
    │   └── README.md
    ├── scan/
    │   └── README.md
    ├── gssurgo/
    │   └── README.md
    └── gnatsgo/
        └── README.md
```

Related responsibility roots:

```text
connectors/nrcs/                         # canonical NRCS connector-family lane
connectors/nrcs/src/nrcs/                # importable connector package boundary
docs/sources/catalog/nrcs.md             # NRCS source-family profile
docs/sources/catalog/nrcs/               # NRCS product doctrine
data/registry/sources/                   # source descriptors and activation state
data/raw/                                # raw staged source outputs by owning domain
data/quarantine/                         # held material requiring source/role/rights/sensitivity review
data/receipts/                           # ingest, checksum, query, package, transform, and aggregation receipts
data/proofs/                             # EvidenceBundles and proof packs
policy/rights/                           # terms, attribution, and source-use review
policy/sensitivity/                      # release and sensitivity review rules
release/                                 # release decisions, manifests, rollback, correction state
```

---

## Import contract

Importing this package or any submodule should be safe by default.

Required import behavior:

- no network calls at import time;
- no credential, token, cookie, or private session reads at import time;
- no filesystem writes at import time;
- no lifecycle writes to raw, quarantine, work, processed, catalog, triplet, published, receipt, proof, release, API, UI, or tile stores at import time;
- no public claims, public map artifacts, or release artifacts at import time;
- live source access only through explicit, reviewed function calls with descriptor gating;
- deterministic parser behavior for the same supplied payload and configuration.

---

## Expected module areas

Actual modules are **NEEDS VERIFICATION**. A future package layout may include:

```text
nrcs/
├── __init__.py
├── config.py
├── client.py
├── descriptors.py
├── source_roles.py
├── freshness.py
├── rights.py
├── sensitivity.py
├── digest.py
├── envelope.py
├── errors.py
└── products/
    ├── sda.py
    ├── scan.py
    ├── ssurgo.py
    ├── gssurgo.py
    └── gnatsgo.py
```

| Module area | Responsibility |
|---|---|
| `config.py` | No-network defaults, live-access opt-in flags, timeout policy, and product-lane feature flags. |
| `client.py` | Bounded request helpers; no hidden live access. |
| `descriptors.py` | SourceDescriptor reference checks and activation gating; not descriptor authority. |
| `source_roles.py` | Product-specific source-role preservation and NRCS-wide role-collapse prevention. |
| `freshness.py` | Source date, package date, observation time, report period, retrieval time, file vintage, correction/update marker helpers. |
| `rights.py` | Citation, attribution, terms, permitted-use, and review-required helpers. |
| `sensitivity.py` | Tribal, private-land, ecology, cultural, exact-location, compliance, producer, or program-participation review gates. |
| `digest.py` | Query, response, package, manifest, and fixture digest helpers. |
| `envelope.py` | Raw/quarantine source-admission envelope construction. |
| `errors.py` | Finite connector errors safe for logs and review. |
| `products/*.py` | Product-specific parsers that preserve native fields and caveats. |

---

## Product parser boundaries

| Product lane | Package responsibility |
|---|---|
| SDA | Preserve endpoint, query text, parameters, response metadata, table names, row counts, MUKEY/join fields, schema-drift findings, and digest. |
| SCAN | Preserve station ID, network, timestamp, sensor depth, variable, units, quality flags, cadence, freshness, Tribal SCAN posture, source URL, and digest. |
| SSURGO | Preserve survey area, package date, package files, spatial layers, table names, MUKEY/COKEY/CHKEY lineage, scale caveats, source URL, and digest. |
| gSSURGO | Preserve product identity, native grid, CRS, resolution, MUKEY joins, source-survey vintage, SoilTimeCaveat, and digest. |
| gNATSGO | Preserve product identity, native grid, CRS, resolution, product-native join fields, national-scale/generalization caveats, and digest. |

---

## Lifecycle handoff

```mermaid
flowchart LR
  SRC[NRCS source payload or approved fixture] --> PARSE[nrcs package parser]
  PARSE --> GATE[source role / freshness / rights / sensitivity gates]
  GATE --> DECIDE{admit?}
  DECIDE -->|yes| RAW[raw candidate envelope]
  DECIDE -->|unclear / restricted| QUAR[quarantine candidate envelope]
  RAW --> DOWN[downstream governed stages]
  QUAR --> REVIEW[steward review]
```

This package should return handoff envelopes or finite errors. It should not write lifecycle stores directly unless a connector runner owns the write and records receipts.

---

## Anti-collapse rules

| Rule | Package implication |
|---|---|
| NRCS-wide role collapse is forbidden. | Product-specific descriptors, roles, cadence, scale, and caveats must remain separate. |
| Import is not activation. | Importing this package must not prove source activation or availability. |
| Query response is not full source package. | SDA query scope and parameters must remain visible. |
| Station is not area truth. | SCAN readings must not become county, watershed, or raster truth without downstream receipts. |
| Gridded products are not field verification. | gSSURGO/gNATSGO cells are source products, not current point-observed field conditions. |
| SSURGO package is not processed soil truth. | Normalization and release belong downstream. |
| Policy and release are external. | The package may flag review needs but must not decide public release. |

---

## Validation

Before relying on this package, verify actual module files, import paths, dependency configuration, no-network import behavior, descriptor gates, rights and sensitivity gates, product parsers, no-network tests, fixture approval, raw/quarantine-only envelope creation, and CI wiring.

---

## Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [ ] Actual package files and module names are inventoried.
- [ ] Importing package modules performs no network, secret, cache, publication, or unsafe filesystem side effects.
- [ ] Source descriptors and activation decisions are required before live access.
- [ ] Rights, citation, attribution, source-role, freshness, and sensitivity gates fail closed.
- [ ] Product parsers preserve native fields, caveats, lineage, query/package/station/raster metadata, and digests.
- [ ] Output is limited to raw or quarantine admission envelopes.
- [ ] Tests cover no-network defaults, malformed inputs, stale sources, role collapse, schema drift, and public-release misuse paths.
- [ ] CI behavior is verified or marked `NEEDS VERIFICATION`.

---

## Status summary

`connectors/nrcs/src/nrcs/` is for importable NRCS connector source-admission code only. It is not NRCS source-family truth, product doctrine, Soil domain truth, source descriptor authority, schema authority, policy authority, proof closure, release authority, public map authority, public API behavior, public UI behavior, or pipeline authority.

<p align="right"><a href="#top">Back to top</a></p>
