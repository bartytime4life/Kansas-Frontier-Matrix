<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-epa-src-package-readme
title: connectors/epa/src/epa/ — EPA Connector Python Package
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Source steward · Connector steward · Data steward · Validation steward · Docs steward
created: 2026-06-18
updated: 2026-06-18
policy_label: public
proposed_path: connectors/epa/src/epa/README.md
truth_posture: CONFIRMED path exists / PROPOSED package contract / UNKNOWN implementation depth
related:
  - ../../README.md
  - ../../../README.md
  - ../../tests/README.md
  - ../../../../docs/sources/catalog/epa.md
  - ../../../../data/registry/sources/
  - ../../../../data/raw/
  - ../../../../data/quarantine/
  - ../../../../fixtures/
  - ../../../../schemas/contracts/v1/source/
  - ../../../../policy/sensitivity/
  - ../../../../release/
tags: [kfm, connectors, epa, python-package, source-admission, raw, quarantine, governance]
notes:
  - "This README documents the connector implementation package boundary, not EPA source truth or publication authority."
  - "Connector code may prepare source material for RAW or QUARANTINE admission only."
  - "Concrete modules, APIs, source descriptors, endpoint coverage, tests, fixtures, and CI wiring remain NEEDS VERIFICATION until inspected in the mounted repo."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# EPA Connector Python Package

> Python package boundary for EPA source-intake helpers inside `connectors/epa/`.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Owner: OWNER_TBD" src="https://img.shields.io/badge/owner-OWNER__TBD-lightgrey">
  <img alt="Scope: source admission" src="https://img.shields.io/badge/scope-source__admission-blue">
  <img alt="Lifecycle: raw or quarantine only" src="https://img.shields.io/badge/lifecycle-raw%20%7C%20quarantine%20only-orange">
  <img alt="Network: guarded" src="https://img.shields.io/badge/network-guarded-critical">
</p>

`connectors/epa/src/epa/`

## Quick jumps

[Scope](#scope) · [Package boundary](#package-boundary) · [Authority boundary](#authority-boundary) · [Expected modules](#expected-modules) · [Runtime posture](#runtime-posture) · [Inputs and outputs](#inputs-and-outputs) · [Errors](#errors) · [Tests](#tests) · [Definition of done](#definition-of-done) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/epa/src/epa/` is the Python implementation package for EPA connector helpers.

It may contain code that:

- reads connector-local configuration;
- prepares EPA source requests when live access is explicitly allowed;
- parses EPA source-family responses or fixture payloads;
- normalizes connector output into a bounded source-admission envelope;
- preserves source metadata needed by downstream evidence, policy, and validation stages;
- routes uncertain or unsafe material toward quarantine-safe outcomes;
- exposes small, testable functions used by `connectors/epa/tests/`.

It must not become environmental truth, atmospheric truth, hydrology truth, hazards truth, source-family authority, schema authority, policy authority, catalog authority, release authority, or publication authority.

> [!IMPORTANT]
> This package is an intake adapter. It does not decide whether EPA-derived material is publishable. Publication requires downstream validation, evidence closure, policy review, release decision, receipts, proofs, and rollback support.

---

## Package boundary

```text
connectors/
└── epa/
    ├── README.md                  # connector-lane overview, if present
    ├── src/
    │   └── epa/
    │       ├── README.md          # this file
    │       ├── __init__.py        # PROPOSED / NEEDS VERIFICATION
    │       ├── config.py          # PROPOSED / NEEDS VERIFICATION
    │       ├── client.py          # PROPOSED / NEEDS VERIFICATION
    │       ├── parser.py          # PROPOSED / NEEDS VERIFICATION
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
  fetch or parse steward-approved EPA source material
  produce connector-local source-admission envelopes
  preserve retrieval metadata, source identifiers, timestamps, and digests
  return finite failure outcomes
  support RAW or QUARANTINE admission

THIS PACKAGE MUST NOT:
  write directly to PROCESSED, CATALOG, TRIPLET, PUBLISHED, or release stores
  create public claims
  bypass source descriptors, source rights, sensitivity policy, or review gates
  embed credentials, tokens, or private URLs
  silently correct, infer, or complete missing source facts
  treat generated summaries as evidence
```

KFM lifecycle discipline remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

This connector package participates only at the source-admission edge.

---

## Expected modules

The module names below are a recommended package contract, not a verified implementation inventory.

| Module | Status | Responsibility |
|---|---:|---|
| `config.py` | **PROPOSED** | Read connector configuration, feature flags, endpoint names, timeouts, and no-network defaults. |
| `client.py` | **PROPOSED** | Hold bounded EPA request behavior; no live call unless explicitly enabled. |
| `parser.py` | **PROPOSED** | Convert EPA response payloads or fixtures into internal parsed records without asserting truth. |
| `envelope.py` | **PROPOSED** | Build source-admission envelopes with metadata, digests, source references, and lifecycle target. |
| `errors.py` | **PROPOSED** | Define finite, reviewable connector errors and failure outcomes. |
| `__init__.py` | **PROPOSED** | Expose a small public import surface; avoid importing network clients at module import time. |

Keep the import surface intentionally boring. Downstream code should not need to know EPA endpoint quirks to handle a connector output envelope.

---

## Runtime posture

Default runtime behavior should be safe without special environment setup.

| Concern | Required posture |
|---|---|
| Network access | Disabled or mock-only by default in tests and local dry runs. |
| Credentials | Never required for import, parsing fixtures, or no-network tests. |
| Secrets | Never committed and never printed in exceptions. |
| Source descriptors | Required before live source activation. |
| Rate limits | Bounded and explicit; no uncontrolled polling. |
| Retries | Finite, observable, and disabled or small by default. |
| Writes | No direct writes outside allowed RAW or QUARANTINE handoff paths. |
| Publication | Not allowed from this package. |

Optional live behavior should require explicit opt-in, for example a repo-approved equivalent of:

```bash
KFM_ALLOW_LIVE_EPA_TESTS=1
```

The exact flag name is **NEEDS VERIFICATION** against repo convention.

---

## Inputs and outputs

### Inputs

Expected input classes:

- source descriptor reference;
- connector configuration;
- EPA source-family endpoint identifier;
- request parameters that are allowed by source policy;
- local fixture payload for tests;
- optional live response body when source-steward approved.

### Outputs

Expected output classes:

- parsed source payload object;
- source-admission envelope;
- finite error outcome;
- quarantine-safe drift signal;
- metadata bundle containing retrieval time, source label, source URL or endpoint key, digest, and parser version where applicable.

Outputs should be shaped for downstream governance. They should not be shaped as direct UI payloads or published claims.

---

## Errors

Prefer explicit outcomes over ambiguous exceptions.

| Condition | Package behavior |
|---|---|
| Missing source descriptor | Refuse live activation; return actionable error. |
| Network disabled | Skip or fail with clear no-network outcome. |
| Timeout | Return bounded connector error with source metadata where safe. |
| Rate limit | Return retry-aware finite outcome; do not spin. |
| Empty response | Return `ABSTAIN`-style outcome unless empty is valid for that source. |
| Malformed payload | Return `ERROR` or quarantine-safe parser failure. |
| Unexpected schema drift | Return `NEEDS_VERIFICATION`-style drift signal. |
| Rights or sensitivity unknown | Route toward quarantine-safe handoff; do not publish. |

Exception messages should help maintainers fix the connector without leaking credentials or over-copying source payloads.

---

## Tests

Connector-local tests belong in:

```text
connectors/epa/tests/
```

The local test README defines the no-network default, fixture posture, connector-local test classes, and acceptance checklist.

Likely test command, subject to repo verification:

```bash
python -m pytest connectors/epa/tests
```

The package should be easy to test with synthetic or minimized fixtures. Parser functions should be callable without performing network I/O.

---

## Definition of done

This package is ready for first review when:

- [ ] Importing `epa` does not perform network I/O.
- [ ] Connector configuration is explicit and testable.
- [ ] Live calls are opt-in and guarded.
- [ ] Source descriptor requirements are enforced before live activation.
- [ ] Parser behavior is covered by valid, empty, malformed, timeout, forbidden, and drift fixtures.
- [ ] Connector outputs include retrieval metadata and digest support where applicable.
- [ ] Outputs target RAW or QUARANTINE handoff only.
- [ ] No code writes directly to processed, catalog, triplet, published, proof, receipt, or release stores.
- [ ] Errors are finite, actionable, and safe to log.
- [ ] CI or local validation can run the no-network test suite.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm actual files under `connectors/epa/src/epa/`. | **NEEDS VERIFICATION** | Mounted repo tree or GitHub file listing beyond this README. |
| Confirm Python package manager and import path. | **NEEDS VERIFICATION** | `pyproject.toml`, workspace config, or connector package metadata. |
| Confirm root connector README contract. | **NEEDS VERIFICATION** | `connectors/epa/README.md`. |
| Confirm EPA source catalog page and descriptor names. | **NEEDS VERIFICATION** | `docs/sources/catalog/epa.md` and source registry entries. |
| Confirm expected source-admission envelope schema. | **NEEDS VERIFICATION** | `schemas/contracts/v1/source/` and related contract docs. |
| Confirm test runner and no-network policy. | **NEEDS VERIFICATION** | `connectors/epa/tests/README.md`, root `tests/`, Makefile, and CI workflows. |
| Confirm selected EPA source families and rights posture. | **NEEDS VERIFICATION** | Source steward review and source descriptors. |

---

## Maintainer note

Keep this package narrow. It should make EPA source material easier to admit safely, inspect, validate, quarantine, and review. It should not make EPA data appear more authoritative than its source descriptor, evidence support, policy state, review state, and release state allow.
