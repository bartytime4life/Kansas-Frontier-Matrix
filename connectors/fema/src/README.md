<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-fema-src-readme
title: connectors/fema/src/ — FEMA Connector Source Root
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Source steward · Connector steward · Hazards steward · Hydrology steward · Data steward · Validation steward · Docs steward
created: 2026-06-18
updated: 2026-06-18
policy_label: public-context-only; not-for-life-safety
proposed_path: connectors/fema/src/README.md
truth_posture: CONFIRMED path exists / PROPOSED source-root contract / UNKNOWN implementation depth
related:
  - ../README.md
  - fema/README.md
  - ../tests/README.md
  - ../nfhl/README.md
  - ../../fema-nfhl/README.md
  - ../../fema-openfema/README.md
  - ../../../docs/sources/catalog/fema/README.md
  - ../../../docs/sources/catalog/fema/nfhl-flood-hazard.md
  - ../../../docs/sources/catalog/fema/openfema-disaster-declarations.md
  - ../../../docs/sources/catalog/fema/openfema-auxiliary-tables.md
  - ../../../docs/domains/hazards/README.md
  - ../../../docs/domains/hydrology/README.md
  - ../../../data/registry/sources/
  - ../../../data/raw/
  - ../../../data/quarantine/
  - ../../../fixtures/
  - ../../../schemas/contracts/v1/source/
  - ../../../policy/sensitivity/
  - ../../../release/
tags: [kfm, connectors, fema, source-root, python, nfhl, openfema, hazards, hydrology, regulatory-context, administrative-context, aggregate, source-admission, raw, quarantine, governance]
notes:
  - "This README documents the FEMA connector source-code root, not FEMA source truth, hazard truth, regulatory interpretation, administrative truth, or publication authority."
  - "The implementation package below this root may prepare source material for RAW or QUARANTINE admission only."
  - "Concrete package metadata, modules, imports, source descriptors, endpoint coverage, bulk/download strategy, tests, fixtures, CI wiring, and source terms remain NEEDS VERIFICATION until inspected in the mounted repo."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# FEMA Connector Source Root

> Source-code root for the FEMA connector implementation under `connectors/fema/`.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Owner: OWNER_TBD" src="https://img.shields.io/badge/owner-OWNER__TBD-lightgrey">
  <img alt="Scope: connector source root" src="https://img.shields.io/badge/scope-connector__source__root-blue">
  <img alt="Release: not from source root" src="https://img.shields.io/badge/release-not__from__source__root-critical">
  <img alt="Lifecycle: raw or quarantine only" src="https://img.shields.io/badge/lifecycle-raw%20%7C%20quarantine%20only-orange">
</p>

`connectors/fema/src/`

## Quick jumps

[Scope](#scope) · [Repository fit](#repository-fit) · [Authority boundary](#authority-boundary) · [Expected contents](#expected-contents) · [Import and packaging posture](#import-and-packaging-posture) · [Lifecycle handoff](#lifecycle-handoff) · [Product posture](#product-posture) · [Testing relationship](#testing-relationship) · [Definition of done](#definition-of-done) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/fema/src/` is the implementation source root for the FEMA connector family lane.

This folder may contain importable connector code that supports FEMA source intake, product dispatch, parsing, source-role checks, normalization into source-admission envelopes, and safe handoff toward RAW or QUARANTINE lifecycle states.

It must not contain:

- FEMA source truth;
- observed hazard truth;
- regulatory interpretation authority;
- administrative truth authority;
- source registry authority;
- policy authority;
- schema authority;
- processed domain records;
- published records;
- release decisions;
- proof packs;
- credentials, tokens, cookies, or private session material;
- UI-facing claim text.

> [!IMPORTANT]
> This root is for connector implementation code. It does not replace `connectors/fema/README.md`, `connectors/fema/tests/README.md`, FEMA source catalog pages, source descriptors, contracts, schemas, policy, release records, or downstream pipeline documentation.

---

## Repository fit

```text
connectors/
└── fema/
    ├── README.md                  # FEMA connector-family overview
    ├── nfhl/
    │   └── README.md              # nested NFHL product-lane guidance
    ├── src/
    │   ├── README.md              # this file
    │   └── fema/
    │       └── README.md          # implementation-package boundary
    └── tests/
        └── README.md              # connector-local tests
```

Related connector paths that need reconciliation:

```text
connectors/fema-nfhl/                # split NFHL product-specific lane; canonicality NEEDS VERIFICATION
connectors/fema-openfema/            # split OpenFEMA product-specific lane; canonicality NEEDS VERIFICATION
```

Related responsibility roots:

```text
connectors/                          # source-specific fetch and admission code
docs/sources/catalog/fema/           # FEMA source-family and product briefings
docs/domains/hazards/                # hazards domain doctrine
docs/domains/hydrology/              # hydrology domain doctrine
data/registry/sources/               # source descriptors and activation state
data/raw/                            # raw staged source outputs, domain-routed
data/quarantine/                     # held material requiring review, domain-routed
fixtures/                            # shared test fixtures, when promoted out of connector-local scope
schemas/contracts/v1/source/         # source/admission schemas, subject to ADR/schema-home convention
policy/sensitivity/                  # sensitivity and release rules
release/                             # release decisions, rollback, and correction state
```

---

## Authority boundary

```text
THIS SOURCE ROOT MAY CONTAIN:
  connector implementation code
  parser helpers
  product-dispatch helpers
  bounded client helpers
  source-admission envelope builders
  connector-local error classes
  package README files

THIS SOURCE ROOT MUST NOT CONTAIN:
  source descriptors as authority records
  policy decisions
  schemas as authority records
  release manifests
  publication outputs
  raw source dumps outside the approved lifecycle
  credentials, tokens, cookies, or private session material
  generated truth claims
```

The FEMA connector source root participates at the source-admission edge only:

```text
FEMA source material
  -> connectors/fema/src/
  -> data/raw/ or data/quarantine/
  -> downstream governed processing, validation, evidence closure, policy, review, release
```

It must not short-circuit the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

---

## Expected contents

The exact implementation inventory is **NEEDS VERIFICATION**. A minimal source-root structure may look like this:

```text
connectors/fema/src/
├── README.md
└── fema/
    ├── README.md
    ├── __init__.py
    ├── config.py
    ├── client.py
    ├── nfhl.py
    ├── openfema.py
    ├── envelope.py
    └── errors.py
```

Recommended separation:

| Area | Responsibility |
|---|---|
| `fema/config.py` | Configuration parsing, feature flags, no-network defaults, source descriptor references, product keys. |
| `fema/client.py` | Bounded request helpers; no live access unless explicitly enabled and reviewed. |
| `fema/nfhl.py` | NFHL parsing and regulatory-context preservation. |
| `fema/openfema.py` | OpenFEMA administrative and aggregate table parsing with per-table admission checks. |
| `fema/envelope.py` | Source-admission envelope construction with metadata, source role, lifecycle target, and digest support. |
| `fema/errors.py` | Finite connector errors safe for logs and review. |
| `fema/__init__.py` | Small import surface that does not trigger network or secret behavior. |

Avoid adding shared utilities here until more than one connector needs them. Shared connector patterns should move to a governed shared package or tool home after review.

---

## Import and packaging posture

Expected posture:

- importing the package should not make network calls;
- importing the package should not read live credentials or secret environment values;
- package-level code should avoid source fetches at import time;
- optional live behavior should be invoked explicitly;
- parser and envelope functions should operate on supplied payloads or fixtures;
- connector outputs should be deterministic for the same input payload and connector configuration;
- source descriptors, schema validation, and policy checks should remain explicit dependencies, not hidden side effects.

Likely import shape, subject to repo verification:

```python
from fema.nfhl import parse_nfhl_payload
from fema.openfema import parse_openfema_table
from fema.envelope import build_source_admission_envelope
```

Do not treat this example as implementation proof until the mounted repo confirms module names and packaging configuration.

---

## Lifecycle handoff

Connector source code may prepare data for lifecycle handoff, but it does not own later lifecycle phases.

| Phase | Connector source-root role |
|---|---|
| Pre-RAW / source contact | May prepare bounded source requests only when source and policy gates allow it. |
| RAW | May write or prepare raw-admission payloads only if the repo’s intake convention allows it. |
| QUARANTINE | May route rights-unclear, role-unclear, malformed, incomplete, stale, or drifted material to quarantine-safe output. |
| WORK / PROCESSED | Out of scope unless a downstream governed pipeline imports connector helpers explicitly. |
| CATALOG / TRIPLET | Out of scope. |
| PUBLISHED | Out of scope. |
| RELEASE / ROLLBACK | Out of scope. |

When in doubt, route uncertain material toward quarantine, explicit abstention, or review-required output rather than guessing.

---

## Product posture

FEMA source products have different source-role meanings. The source root should preserve those differences rather than flattening all FEMA material into one output type.

| Product area | Source-root posture |
|---|---|
| NFHL | Preserve regulatory context and required source metadata; do not convert to observed event truth. |
| Map Service Center | Treat as document/access context if implemented; do not replace source descriptors. |
| OpenFEMA disaster declarations | Preserve administrative action meaning. |
| OpenFEMA auxiliary tables | Require per-table source descriptor, source role, sensitivity posture, and admission decision. |
| NFIP aggregates | Preserve aggregate meaning and aggregation unit. |

---

## Testing relationship

Connector-local tests live outside this source root:

```text
connectors/fema/tests/
```

The source root should be easy to test with synthetic, no-network fixtures:

- import tests should prove no network and no secret read at import time;
- parser tests should pass with static synthetic payloads;
- client tests should mock all HTTP behavior by default;
- source-role tests should cover regulatory, administrative, and aggregate boundaries;
- envelope tests should check metadata, source references, lifecycle target, review flags, and digest fields;
- live smoke tests, if any, should be opt-in and isolated from default CI.

Likely local command, subject to repo verification:

```bash
python -m pytest connectors/fema/tests
```

---

## Definition of done

This source root is ready for first review when:

- [ ] `connectors/fema/src/README.md` explains the source-root boundary.
- [ ] `connectors/fema/src/fema/README.md` explains the package boundary.
- [ ] Importing package modules does not perform network I/O.
- [ ] Importing package modules does not require live credentials or secret environment values.
- [ ] Connector output is limited to RAW or QUARANTINE handoff.
- [ ] Parser and envelope behavior are fixture-testable without live FEMA calls.
- [ ] NFHL, OpenFEMA, and aggregate boundaries remain source-role explicit.
- [ ] Errors are finite, actionable, and safe to log.
- [ ] Live source activation requires source descriptor and steward review.
- [ ] The connector does not write directly to processed, catalog, triplet, published, proof, receipt, or release stores.
- [ ] Test and CI wiring is documented once verified.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm actual files below `connectors/fema/src/`. | **NEEDS VERIFICATION** | Mounted repo tree or GitHub file listing. |
| Confirm whether `src/` is packaged by `pyproject.toml`, workspace config, or connector-specific metadata. | **NEEDS VERIFICATION** | Packaging files and CI. |
| Confirm package import name is `fema`. | **NEEDS VERIFICATION** | Python package metadata and import tests. |
| Confirm shared connector helper home, if any. | **NEEDS VERIFICATION** | Repo tree and ADRs. |
| Confirm source-admission envelope schema. | **NEEDS VERIFICATION** | Contracts and schemas under the accepted schema home. |
| Confirm source descriptor location and FEMA product/table coverage. | **NEEDS VERIFICATION** | Source registry and source catalog docs. |
| Confirm default no-network test behavior. | **NEEDS VERIFICATION** | Test config and CI workflows. |
| Confirm canonical relationship among FEMA connector paths. | **NEEDS VERIFICATION** | Directory Rules, ADRs, migration notes, and current repo paths. |

---

## Maintainer note

Keep `connectors/fema/src/` boring, narrow, and source-admission focused. It should make FEMA material easier to parse, inspect, quarantine, and review. It should not become a hidden pipeline, source registry, policy engine, release path, or public truth surface.
