<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-gbif-src-package-readme
title: connectors/gbif/src/gbif/ — GBIF Connector Python Package
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Source steward · Biodiversity steward · Flora steward · Fauna steward · Habitat steward · Validation steward · Docs steward
created: 2026-06-18
updated: 2026-06-18
policy_label: public-doctrine; rights-and-sensitivity-gated; no-live-by-default
proposed_path: connectors/gbif/src/gbif/README.md
truth_posture: CONFIRMED path exists / PROPOSED package contract / UNKNOWN implementation depth
related:
  - ../../README.md
  - ../../../README.md
  - ../../../plants/README.md
  - ../../../../docs/sources/catalog/gbif/README.md
  - ../../../../docs/sources/catalog/gbif/async-download.md
  - ../../../../docs/domains/fauna/README.md
  - ../../../../docs/domains/flora/README.md
  - ../../../../docs/domains/habitat/README.md
  - ../../../../data/registry/sources/
  - ../../../../data/raw/fauna/
  - ../../../../data/raw/flora/
  - ../../../../data/raw/habitat/
  - ../../../../data/quarantine/fauna/
  - ../../../../data/quarantine/flora/
  - ../../../../data/quarantine/habitat/
  - ../../../../fixtures/
  - ../../../../schemas/contracts/v1/source/
  - ../../../../policy/sensitivity/
  - ../../../../policy/rights/
  - ../../../../release/
tags: [kfm, connectors, gbif, python-package, biodiversity, darwin-core, occurrence, taxonomy, source-admission, raw, quarantine, governance]
notes:
  - "This README fills a previously blank package README for the proposed GBIF connector implementation package."
  - "This package boundary is not a source registry, taxonomy authority, biodiversity truth store, policy engine, release path, or publication surface."
  - "Import behavior, modules, source descriptor, download strategy, Darwin Core handling, backbone version handling, tests, fixtures, CI wiring, and activation state remain NEEDS VERIFICATION."
  - "Package output may prepare RAW or QUARANTINE handoff candidates only; downstream validation, evidence closure, release, publication, correction, and rollback remain outside this package."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# GBIF Connector Python Package

> Importable package boundary for the proposed GBIF connector implementation.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Scope: package boundary" src="https://img.shields.io/badge/scope-package__boundary-blue">
  <img alt="Network: off by default" src="https://img.shields.io/badge/network-off__by__default-critical">
  <img alt="Rights: gated" src="https://img.shields.io/badge/rights-gated-orange">
  <img alt="Lifecycle: raw or quarantine only" src="https://img.shields.io/badge/lifecycle-raw%20%7C%20quarantine%20only-orange">
</p>

`connectors/gbif/src/gbif/`

## Scope

This folder is the proposed implementation package for the GBIF connector.

The package may contain small, testable helpers for:

- reading connector configuration;
- validating no-network defaults;
- checking source descriptor references;
- preparing bounded request or download descriptions;
- parsing GBIF-shaped fixture payloads;
- preserving Darwin Core-style fields where available;
- preserving dataset, publisher, license, citation, and version metadata;
- building source-admission envelopes;
- returning finite quarantine, abstain, review-required, or error outcomes.

The package must not contain credentials, source descriptors as authority records, policy decisions, schemas as authority records, release records, public claims, taxonomy authority, occurrence truth, graph truth, or publication outputs.

---

## Expected package posture

Default behavior:

```text
import behavior: no network, no secret reads
live access: disabled unless explicitly enabled and reviewed
credentials: never committed
source activation: requires SourceDescriptor and review state
rights state: explicit where required
output target: RAW or QUARANTINE handoff candidates only
```

The exact module layout is **NEEDS VERIFICATION**. A possible package shape is:

```text
connectors/gbif/src/gbif/
├── README.md
├── __init__.py
├── config.py
├── client.py
├── downloads.py
├── dwc.py
├── backbone.py
├── envelope.py
└── errors.py
```

Treat these filenames as proposed until confirmed by the repo tree.

---

## Authority boundary

```text
THIS PACKAGE MAY:
  parse approved test fixtures
  enforce no-network defaults
  check required source and rights references
  preserve dataset and taxonomy-version metadata
  build source-admission envelopes
  return finite review-required outcomes

THIS PACKAGE MUST NOT:
  publish data
  write processed/catalog/triplet/published outputs
  make public claims
  serve as source registry authority
  serve as taxonomy authority
  bypass policy, review, release, or rollback gates
```

KFM lifecycle discipline remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

This package participates only at the source-admission edge.

---

## Tests

Connector-local tests are expected to live under the GBIF connector test surface. The exact path is **NEEDS VERIFICATION**.

Likely local command, subject to repo verification:

```bash
python -m pytest connectors/gbif/tests
```

The package should be testable without network access, live accounts, private datasets, or secrets.

---

## Definition of done

This package is ready for first review when:

- [ ] Importing the package performs no network I/O.
- [ ] Importing the package reads no live secrets.
- [ ] Live access is disabled by default.
- [ ] SourceDescriptor checks are explicit.
- [ ] Rights and license references are explicit where required.
- [ ] Parser helpers work with synthetic or approved fixtures.
- [ ] Dataset, publisher, license, citation, retrieval, taxon, source-role, and version metadata are preserved where available.
- [ ] Output is limited to RAW or QUARANTINE handoff candidates.
- [ ] Errors are finite, actionable, and safe to log.
- [ ] Tests cover no-network, missing descriptor, missing license, malformed payload, provenance-unclear, version-unclear, and review-required cases.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm actual package files below this path. | **NEEDS VERIFICATION** | Repo tree or mounted workspace. |
| Confirm Python package import name and packaging convention. | **NEEDS VERIFICATION** | Package metadata and import tests. |
| Confirm source profile and SourceDescriptor. | **NEEDS VERIFICATION** | Source catalog and registry entry. |
| Confirm Darwin Core and backbone-version handling. | **NEEDS VERIFICATION** | Parser tests and source descriptor. |
| Confirm test runner and fixture strategy. | **NEEDS VERIFICATION** | Test tree, fixture registry, and CI workflow. |

---

## Maintainer note

Keep this package narrow and side-effect safe. It should help the connector prepare governed source-admission candidates without becoming a source registry, taxonomy authority, biodiversity truth store, release path, or public truth surface.
