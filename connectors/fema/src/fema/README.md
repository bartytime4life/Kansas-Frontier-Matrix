<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-fema-src-package-readme
title: connectors/fema/src/fema/ — FEMA Connector Python Package
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Source steward · Connector steward · Hazards steward · Hydrology steward · Data steward · Validation steward · Docs steward
created: 2026-06-18
updated: 2026-06-18
policy_label: public-context-only; not-for-life-safety
proposed_path: connectors/fema/src/fema/README.md
truth_posture: CONFIRMED path exists / PROPOSED package contract / UNKNOWN implementation depth
related:
  - ../../README.md
  - ../../../README.md
  - ../../tests/README.md
  - ../../nfhl/README.md
  - ../../../fema-nfhl/README.md
  - ../../../fema-openfema/README.md
  - ../../../../docs/sources/catalog/fema/README.md
  - ../../../../docs/sources/catalog/fema/nfhl-flood-hazard.md
  - ../../../../docs/sources/catalog/fema/openfema-disaster-declarations.md
  - ../../../../docs/sources/catalog/fema/openfema-auxiliary-tables.md
  - ../../../../docs/domains/hazards/README.md
  - ../../../../docs/domains/hydrology/README.md
  - ../../../../data/registry/sources/
  - ../../../../data/raw/
  - ../../../../data/quarantine/
  - ../../../../fixtures/
  - ../../../../schemas/contracts/v1/source/
  - ../../../../policy/sensitivity/
  - ../../../../release/
tags: [kfm, connectors, fema, python-package, nfhl, openfema, hazards, hydrology, regulatory-context, administrative-context, aggregate, source-admission, raw, quarantine, governance]
notes:
  - "This README documents the connector implementation package boundary, not FEMA source truth, hazard truth, regulatory interpretation, administrative truth, or publication authority."
  - "Package code may prepare source material for RAW or QUARANTINE admission only."
  - "Import behavior, product modules, descriptors, endpoint coverage, bulk/download strategy, tests, fixtures, CI wiring, and source terms remain NEEDS VERIFICATION until inspected in the mounted repo."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# FEMA Connector Python Package

> Python package boundary for FEMA source-intake helpers inside `connectors/fema/`.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Owner: OWNER_TBD" src="https://img.shields.io/badge/owner-OWNER__TBD-lightgrey">
  <img alt="Scope: source admission" src="https://img.shields.io/badge/scope-source__admission-blue">
  <img alt="Release: not from package" src="https://img.shields.io/badge/release-not__from__package-critical">
  <img alt="Lifecycle: raw or quarantine only" src="https://img.shields.io/badge/lifecycle-raw%20%7C%20quarantine%20only-orange">
</p>

`connectors/fema/src/fema/`

## Quick jumps

[Scope](#scope) · [Package boundary](#package-boundary) · [Authority boundary](#authority-boundary) · [Expected modules](#expected-modules) · [Runtime posture](#runtime-posture) · [Inputs and outputs](#inputs-and-outputs) · [Product behavior](#product-behavior) · [Errors](#errors) · [Tests](#tests) · [Definition of done](#definition-of-done) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/fema/src/fema/` is the Python implementation package for FEMA connector helpers.

It may contain code that:

- reads connector-local configuration;
- dispatches among FEMA product lanes only when those lanes are explicitly configured;
- prepares FEMA source requests only when live access is explicitly allowed and reviewed;
- parses FEMA-shaped source responses or synthetic fixtures;
- normalizes connector output into bounded source-admission envelopes;
- preserves source product, table identity, source role, retrieval metadata, version metadata, temporal metadata, geography metadata, and digests where applicable;
- routes malformed, incomplete, source-role-unclear, rights-unclear, version-unclear, datum/units-unclear, or source-drift material toward abstain, quarantine, or review-required outcomes;
- exposes small, testable functions used by `connectors/fema/tests/`.

It must not become hazard truth, flood truth, observed-event truth, emergency-alert authority, regulatory interpretation authority, insurance determination authority, benefit-eligibility authority, source registry authority, schema authority, policy authority, catalog authority, release authority, or publication authority.

---

## Package boundary

```text
connectors/
└── fema/
    ├── README.md                  # FEMA connector-family overview
    ├── nfhl/
    │   └── README.md              # nested NFHL product-lane guidance
    ├── src/
    │   └── fema/
    │       ├── README.md          # this file
    │       ├── __init__.py        # PROPOSED / NEEDS VERIFICATION
    │       ├── config.py          # PROPOSED / NEEDS VERIFICATION
    │       ├── client.py          # PROPOSED / NEEDS VERIFICATION
    │       ├── nfhl.py            # PROPOSED / NEEDS VERIFICATION
    │       ├── openfema.py        # PROPOSED / NEEDS VERIFICATION
    │       ├── envelope.py        # PROPOSED / NEEDS VERIFICATION
    │       └── errors.py          # PROPOSED / NEEDS VERIFICATION
    └── tests/
        └── README.md
```

The exact module layout is **PROPOSED**. Use the mounted repo’s actual code, package manager, imports, and CI conventions before treating any filename above as implemented.

---

## Authority boundary

```text
THIS PACKAGE MAY:
  parse synthetic or steward-approved FEMA-shaped payloads
  prepare reviewed source requests when live access is explicitly enabled
  emit connector-local source-admission envelopes
  preserve source product/table identity, source role, retrieval metadata, and digests
  return finite failure, abstain, quarantine, or needs-verification outcomes
  support RAW or QUARANTINE admission

THIS PACKAGE MUST NOT:
  assert observed hazards
  issue warnings or forecasts
  decide eligibility, compliance, insurance, or legal meaning
  write directly to PROCESSED, CATALOG, TRIPLET, PUBLISHED, proof, receipt, or release stores
  bypass source descriptors, source rights, sensitivity policy, review gates, or release gates
  treat generated summaries as evidence
```

KFM lifecycle discipline remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

This package participates only at the source-admission edge.

---

## Expected modules

The module names below are a recommended package contract, not a verified implementation inventory.

| Module | Status | Responsibility |
|---|---:|---|
| `config.py` | **PROPOSED** | Read connector configuration, feature flags, product keys, timeout defaults, and no-network posture. |
| `client.py` | **PROPOSED** | Hold bounded request behavior; no live call unless explicitly enabled. |
| `nfhl.py` | **PROPOSED** | Parse NFHL-shaped source material while preserving regulatory context and source metadata. |
| `openfema.py` | **PROPOSED** | Parse OpenFEMA administrative or aggregate tables with per-table role and admission checks. |
| `envelope.py` | **PROPOSED** | Build source-admission envelopes with source metadata, lifecycle target, review flags, and digest support. |
| `errors.py` | **PROPOSED** | Define finite connector errors safe for logs and review. |
| `__init__.py` | **PROPOSED** | Expose a small public import surface; avoid live calls or secret reads at import time. |

Keep the import surface narrow. Downstream code should receive a governed connector output, not raw FEMA API or bulk-download behavior.

---

## Runtime posture

Default runtime behavior must be safe without special environment setup.

| Concern | Required posture |
|---|---|
| Network access | Disabled or mock-only by default in tests and local dry runs. |
| Credentials | Not required for import, parsing fixtures, or no-network tests. |
| Source descriptors | Required before live source activation. |
| Product/table admission | Explicit; no umbrella OpenFEMA admission. |
| Source role | Explicit: regulatory, administrative, or aggregate. |
| Writes | No direct writes outside allowed RAW or QUARANTINE handoff paths. |
| Publication | Not allowed from this package. |

Optional live behavior should require explicit opt-in, for example a repo-approved equivalent of:

```bash
KFM_ALLOW_LIVE_FEMA_TESTS=1
```

The exact flag name is **NEEDS VERIFICATION** against repo convention.

---

## Inputs and outputs

### Inputs

Expected input classes:

- source descriptor reference;
- connector configuration;
- FEMA product or table key;
- steward-approved endpoint, bulk package, or table identifier;
- request parameters allowed by source policy;
- synthetic local fixture payload for tests;
- optional live response body only when source-steward and policy approvals exist.

### Outputs

Expected output classes:

- parsed regulatory-context candidate from NFHL-like material;
- parsed administrative-context candidate from OpenFEMA declaration-like material;
- parsed aggregate-context candidate from approved OpenFEMA aggregate material;
- source-admission envelope;
- finite error outcome;
- quarantine-safe drift signal;
- metadata bundle containing retrieval time, source label, product/table key, source role, digest, parser version, and review flags where applicable.

Outputs should be shaped for downstream governance. They should not be shaped as direct UI payloads, public claims, warnings, determinations, or truth assertions.

---

## Product behavior

| Product area | Package posture |
|---|---|
| FEMA family dispatch | Route to configured product/table helpers only; do not infer admission from convenience. |
| NFHL | Preserve regulatory attributes, version, effective date, datum, units, and lineage; do not convert to observed event truth. |
| Map Service Center | Treat as document/access context if implemented; do not replace source descriptors. |
| OpenFEMA disaster declarations | Preserve administrative action meaning; do not convert to observed hazard event truth. |
| OpenFEMA auxiliary tables | Require per-table source descriptor, source role, aggregation unit, sensitivity posture, and admission decision. |
| NFIP aggregates | Preserve aggregate meaning; do not infer person-level or site-specific truth. |

---

## Errors

Prefer explicit outcomes over ambiguous exceptions.

| Condition | Package behavior |
|---|---|
| Missing source descriptor | Refuse live activation; return actionable error. |
| Network disabled | Skip or fail with clear no-network outcome. |
| Product or table not admitted | Return `NEEDS_VERIFICATION`-style outcome. |
| Unauthorized, timeout, or rate limit | Return bounded connector error. |
| Empty response | Return `ABSTAIN`-style outcome unless empty is valid. |
| Malformed payload | Return `ERROR` or quarantine-safe parser failure. |
| Source-role unclear | Return review-required or quarantine-safe outcome. |
| Version, datum, units, or effective-date unclear | Return review-required or quarantine-safe outcome. |
| Unexpected source-shape drift | Return `NEEDS_VERIFICATION`-style drift signal. |
| Rights or sensitivity unknown | Route toward quarantine-safe handoff; do not publish. |

Exception messages should help maintainers fix the connector without leaking secrets, over-copying source payloads, or implying public truth.

---

## Tests

Connector-local tests belong in:

```text
connectors/fema/tests/
```

The local test README defines the no-network default, fixture posture, FEMA product boundaries, connector-local test classes, and acceptance checklist.

Likely test command, subject to repo verification:

```bash
python -m pytest connectors/fema/tests
```

The package should be easy to test with synthetic fixtures. Parser and envelope functions should be callable without performing network I/O or reading credentials.

---

## Definition of done

This package is ready for first review when:

- [ ] Importing `fema` does not perform network I/O.
- [ ] Importing `fema` does not require live credentials or live environment secrets.
- [ ] Connector configuration is explicit and testable.
- [ ] Live calls are opt-in and guarded.
- [ ] Source descriptor requirements are enforced before live activation.
- [ ] NFHL parser behavior preserves regulatory context and required metadata.
- [ ] OpenFEMA parser behavior preserves administrative or aggregate context and required metadata.
- [ ] Product/table admission is explicit.
- [ ] Connector outputs include retrieval metadata and digest support where applicable.
- [ ] Outputs target RAW or QUARANTINE handoff only.
- [ ] No code writes directly to processed, catalog, triplet, published, proof, receipt, or release stores.
- [ ] Errors are finite, actionable, and safe to log.
- [ ] CI or local validation can run the no-network test suite.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm actual files under `connectors/fema/src/fema/`. | **NEEDS VERIFICATION** | Mounted repo tree or GitHub file listing beyond this README. |
| Confirm Python package manager and import path. | **NEEDS VERIFICATION** | `pyproject.toml`, workspace config, or connector package metadata. |
| Confirm root connector README contract. | **CONFIRMED path / NEEDS VERIFICATION content maturity** | `connectors/fema/README.md`. |
| Confirm canonical relationship among FEMA connector paths. | **NEEDS VERIFICATION** | Directory Rules, ADR, and migration note. |
| Confirm source catalog pages and source descriptor names. | **NEEDS VERIFICATION** | `docs/sources/catalog/fema/` and source registry entries. |
| Confirm expected source-admission envelope schema. | **NEEDS VERIFICATION** | `schemas/contracts/v1/source/` and related contract docs. |
| Confirm test runner and no-network policy. | **NEEDS VERIFICATION** | `connectors/fema/tests/README.md`, root `tests/`, Makefile, and CI workflows. |

---

## Maintainer note

Keep this package narrow and source-admission focused. It should make FEMA material easier to parse, inspect, quarantine, and review. It must not turn FEMA records into observed hazards, forecasts, warnings, determinations, or public KFM truth without downstream evidence, policy, review, release, and rollback support.
