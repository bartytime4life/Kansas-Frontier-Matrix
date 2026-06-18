<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-epa-src-readme
title: connectors/epa/src/ — EPA Connector Source Root
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Source steward · Connector steward · Data steward · Validation steward · Docs steward
created: 2026-06-18
updated: 2026-06-18
policy_label: public
proposed_path: connectors/epa/src/README.md
truth_posture: CONFIRMED path exists / PROPOSED source-root contract / UNKNOWN implementation depth
related:
  - ../README.md
  - epa/README.md
  - ../tests/README.md
  - ../../../docs/sources/catalog/epa.md
  - ../../../data/registry/sources/
  - ../../../data/raw/
  - ../../../data/quarantine/
  - ../../../fixtures/
  - ../../../schemas/contracts/v1/source/
  - ../../../policy/sensitivity/
  - ../../../release/
tags: [kfm, connectors, epa, source-root, python, source-admission, raw, quarantine, governance]
notes:
  - "This README documents the connector source-code root, not EPA source truth or publication authority."
  - "The implementation package below this root may prepare source material for RAW or QUARANTINE admission only."
  - "Concrete package metadata, modules, imports, source descriptors, endpoint coverage, tests, fixtures, and CI wiring remain NEEDS VERIFICATION until inspected in the mounted repo."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# EPA Connector Source Root

> Source-code root for the EPA connector implementation under `connectors/epa/`.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Owner: OWNER_TBD" src="https://img.shields.io/badge/owner-OWNER__TBD-lightgrey">
  <img alt="Scope: connector source root" src="https://img.shields.io/badge/scope-connector__source__root-blue">
  <img alt="Lifecycle: raw or quarantine only" src="https://img.shields.io/badge/lifecycle-raw%20%7C%20quarantine%20only-orange">
  <img alt="Publication: not publisher" src="https://img.shields.io/badge/publication-not__publisher-critical">
</p>

`connectors/epa/src/`

## Quick jumps

[Scope](#scope) · [Repository fit](#repository-fit) · [Authority boundary](#authority-boundary) · [Expected contents](#expected-contents) · [Import and packaging posture](#import-and-packaging-posture) · [Lifecycle handoff](#lifecycle-handoff) · [Testing relationship](#testing-relationship) · [Definition of done](#definition-of-done) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/epa/src/` is the implementation source root for the EPA connector lane.

This folder may contain importable connector code that supports EPA source intake, parsing, normalization into source-admission envelopes, and safe handoff toward RAW or QUARANTINE lifecycle states.

It must not contain:

- EPA source truth;
- source registry authority;
- policy authority;
- schema authority;
- processed domain records;
- published records;
- release decisions;
- proof packs;
- credentials;
- large copied source payloads;
- UI-facing claim text.

> [!IMPORTANT]
> This root is for connector implementation code. It does not replace `connectors/epa/README.md`, `connectors/epa/tests/README.md`, source catalog documentation, source descriptors, contracts, schemas, policy files, release records, or downstream pipeline documentation.

---

## Repository fit

```text
connectors/
└── epa/
    ├── README.md                  # connector-lane overview, if present
    ├── src/
    │   ├── README.md              # this file
    │   └── epa/
    │       └── README.md          # implementation-package boundary
    └── tests/
        └── README.md              # connector-local tests
```

Related responsibility roots:

```text
connectors/                         # source-specific fetch and admission code
docs/sources/catalog/epa.md          # EPA source-family documentation
data/registry/sources/               # source descriptors and activation state
data/raw/                            # raw staged source outputs
data/quarantine/                     # held material requiring review
fixtures/                            # shared test fixtures, when promoted out of connector-local scope
schemas/contracts/v1/source/         # source/admission schemas, subject to ADR/schema-home convention
policy/sensitivity/                  # sensitivity and release policy
release/                             # release decisions, rollback, and correction state
```

---

## Authority boundary

```text
THIS SOURCE ROOT MAY CONTAIN:
  connector implementation code
  parser helpers
  bounded client helpers
  envelope builders
  connector-local error classes
  small package-local constants
  package README files

THIS SOURCE ROOT MUST NOT CONTAIN:
  source descriptors as authority records
  policy decisions
  schemas as authority records
  release manifests
  publication outputs
  raw source dumps
  credentials or private endpoint material
  generated truth claims
```

The EPA connector source root participates at the admission edge only:

```text
EPA source material
  -> connectors/epa/src/
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
connectors/epa/src/
├── README.md
└── epa/
    ├── README.md
    ├── __init__.py
    ├── config.py
    ├── client.py
    ├── parser.py
    ├── envelope.py
    └── errors.py
```

Recommended separation:

| Area | Responsibility |
|---|---|
| `epa/config.py` | Configuration parsing, feature flags, no-network defaults, endpoint keys. |
| `epa/client.py` | Bounded request helpers; no live access unless explicitly enabled. |
| `epa/parser.py` | Payload parsing from fixtures or live responses without asserting truth. |
| `epa/envelope.py` | Source-admission envelope construction with metadata and digest support. |
| `epa/errors.py` | Finite connector errors safe for logs and review. |
| `epa/__init__.py` | Small import surface that does not trigger network behavior. |

Avoid adding shared utilities here until more than one connector needs them. Shared connector patterns should move to a governed shared package or tool home after review.

---

## Import and packaging posture

Expected posture:

- importing the package should not make network calls;
- importing the package should not require credentials;
- package-level code should avoid reading live environment secrets at import time;
- optional live behavior should be invoked explicitly;
- parser functions should operate on supplied payloads or fixtures;
- connector outputs should be deterministic for the same input payload and connector configuration;
- source descriptors, schema validation, and policy checks should remain explicit dependencies, not hidden side effects.

Likely import shape, subject to repo verification:

```python
from epa.parser import parse_payload
from epa.envelope import build_source_admission_envelope
```

Do not treat this example as implementation proof until the mounted repo confirms module names and packaging configuration.

---

## Lifecycle handoff

Connector source code may prepare data for lifecycle handoff, but it does not own the later lifecycle phases.

| Phase | Connector source-root role |
|---|---|
| Pre-RAW / source contact | May prepare bounded source requests when authorized. |
| RAW | May write or prepare raw-admission payloads only if the repo’s intake convention allows it. |
| QUARANTINE | May route incomplete, rights-unclear, malformed, or sensitive material to quarantine-safe output. |
| WORK / PROCESSED | Out of scope unless a downstream pipeline imports connector helpers explicitly. |
| CATALOG / TRIPLET | Out of scope. |
| PUBLISHED | Out of scope. |
| RELEASE / ROLLBACK | Out of scope. |

When in doubt, route uncertain material toward quarantine or explicit abstention rather than guessing.

---

## Testing relationship

Connector-local tests live outside this source root:

```text
connectors/epa/tests/
```

The source root should be easy to test with no-network fixtures:

- parser tests should pass with static payloads;
- client tests should mock all HTTP behavior by default;
- envelope tests should check metadata, source references, lifecycle target, and digest fields;
- error tests should cover timeout, forbidden, rate-limited, empty, malformed, and schema-drift cases;
- live smoke tests, if any, should be opt-in and isolated from default CI.

Likely local command, subject to repo verification:

```bash
python -m pytest connectors/epa/tests
```

---

## Definition of done

This source root is ready for first review when:

- [ ] `connectors/epa/src/README.md` explains the source-root boundary.
- [ ] `connectors/epa/src/epa/README.md` explains the package boundary.
- [ ] Importing package modules does not perform network I/O.
- [ ] No credentials or private endpoint material are committed.
- [ ] Connector output is limited to RAW or QUARANTINE handoff.
- [ ] Parser behavior is fixture-testable without live EPA calls.
- [ ] Errors are finite, actionable, and safe to log.
- [ ] Live source activation requires source-descriptor and steward review.
- [ ] The connector does not write directly to processed, catalog, triplet, published, proof, receipt, or release stores.
- [ ] Test and CI wiring is documented once verified.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm actual files below `connectors/epa/src/`. | **NEEDS VERIFICATION** | Mounted repo tree or GitHub file listing. |
| Confirm whether `src/` is packaged by `pyproject.toml`, workspace config, or connector-specific metadata. | **NEEDS VERIFICATION** | Packaging files and CI. |
| Confirm package import name is `epa`. | **NEEDS VERIFICATION** | Python package metadata and import tests. |
| Confirm shared connector helper home, if any. | **NEEDS VERIFICATION** | Repo tree and ADRs. |
| Confirm source-admission envelope schema. | **NEEDS VERIFICATION** | Contracts and schemas under the accepted schema home. |
| Confirm source descriptor location and EPA source-family coverage. | **NEEDS VERIFICATION** | Source registry and source catalog docs. |
| Confirm default no-network test behavior. | **NEEDS VERIFICATION** | Test config and CI workflows. |

---

## Maintainer note

Keep `connectors/epa/src/` boring and narrow. It should make EPA source material easier to admit safely, inspect, test, quarantine, and review. It should not become a hidden pipeline, a source registry, a policy engine, or a publication path.
