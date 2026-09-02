<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-epa-src-readme
title: connectors/epa/src/ — EPA Connector Source Root
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Source steward · Connector steward · Data steward · Validation steward · Docs steward
created: 2026-06-18
updated: 2026-07-11
policy_label: public
proposed_path: connectors/epa/src/README.md
truth_posture: CONFIRMED repository inventory / PROPOSED source-root contract / UNKNOWN runtime and CI maturity
related:
  - ../README.md
  - epa/README.md
  - ../tests/README.md
  - ../../../docs/sources/catalog/epa/
  - ../../../data/registry/sources/
  - ../../../data/raw/
  - ../../../data/quarantine/
  - ../../../schemas/contracts/v1/source/
  - ../../../policy/
  - ../../../release/
tags: [kfm, connectors, epa, source-root, source-admission, raw, quarantine, governance]
notes:
  - "This README documents the connector source-code root, not EPA source truth or publication authority."
  - "The current package contains README.md, fetch.py, admit.py, and descriptor.yaml; the Python modules and descriptor are greenfield placeholders at the inspected commit."
  - "The connector may prepare material for RAW or QUARANTINE admission only; downstream validation, evidence closure, policy, review, release, correction, and rollback remain outside this root."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# EPA Connector Source Root

> Source-code boundary for EPA fetch and admission helpers under `connectors/epa/`.

> [!IMPORTANT]
> **Document lifecycle:** draft  
> **Component maturity:** experimental scaffold  
> **Owner:** `OWNER_TBD`  
> **Truth posture:** repository inventory confirmed at base commit `30d2c71`; runtime behavior, package wiring, tests, and CI remain unverified.

`connectors/epa/src/`

## Quick navigation

- [Scope](#scope)
- [Repository fit](#repository-fit)
- [Confirmed inventory](#confirmed-inventory)
- [Authority boundary](#authority-boundary)
- [Lifecycle handoff](#lifecycle-handoff)
- [File contracts](#file-contracts)
- [Safety and runtime posture](#safety-and-runtime-posture)
- [Testing relationship](#testing-relationship)
- [Definition of done](#definition-of-done)
- [Verification backlog](#verification-backlog)

---

## Scope

`connectors/epa/src/` owns the source-code boundary for EPA-specific fetching and admission preparation.

This root may contain code and connector-local metadata that:

- contacts a steward-approved EPA source when explicitly enabled;
- preserves source identity, retrieval context, timestamps, and digests;
- prepares material for RAW admission;
- routes malformed, incomplete, rights-unclear, sensitive, or drifted material toward QUARANTINE;
- returns bounded, reviewable failure outcomes;
- supports deterministic no-network tests.

This root does **not** own:

- EPA source truth or environmental-domain truth;
- canonical source registry records;
- contract or schema authority;
- policy decisions;
- processed domain records;
- catalog or triplet records;
- EvidenceBundle authority;
- proof, receipt, promotion, or release authority;
- published artifacts;
- UI-facing claims or generated explanations.

The connector is an admission-edge adapter. It is not a publisher.

---

## Repository fit

Directory Rules place source-specific fetchers and admitters under `connectors/`. EPA remains a source-family lane inside that responsibility root rather than becoming a domain or root-level authority.

```text
connectors/
└── epa/
    ├── README.md
    ├── src/
    │   ├── README.md              # this file
    │   └── epa/
    │       ├── README.md
    │       ├── fetch.py
    │       ├── admit.py
    │       └── descriptor.yaml
    └── tests/
        └── README.md
```

Related responsibility roots:

| Responsibility | Canonical or expected home |
|---|---|
| Source-family documentation | `docs/sources/catalog/epa/` |
| Canonical source descriptors and activation state | `data/registry/sources/` |
| Raw admitted material | `data/raw/` |
| Held or unsafe material | `data/quarantine/` |
| Contract meaning | `contracts/` |
| Machine-checkable shapes | `schemas/contracts/v1/` |
| Policy and sensitivity decisions | `policy/` |
| Downstream normalization and domain processing | `pipelines/` and domain packages |
| Release, correction, and rollback decisions | `release/` |

> [!NOTE]
> The path is consistent with the Directory Rules responsibility-root model: `connectors/` owns source-specific fetch and admission behavior. Topic-specific truth, schemas, policy, lifecycle data, and release records remain in their own authority roots.

---

## Confirmed inventory

The following inventory was verified at base commit `30d2c71ad48ae932f068969cfc0b51676c5c23f3`.

| Path | Status | Confirmed content | What it does not prove |
|---|---:|---|---|
| `connectors/epa/src/README.md` | **CONFIRMED** | Source-root documentation existed as v0.1. | Does not prove connector execution. |
| `connectors/epa/src/epa/README.md` | **CONFIRMED** | Package-boundary documentation exists. | Does not prove the proposed package contract is implemented. |
| `connectors/epa/src/epa/fetch.py` | **CONFIRMED scaffold** | Contains a one-line greenfield placeholder for an EPA fetcher. | No endpoint, network, parsing, retry, or receipt behavior is implemented. |
| `connectors/epa/src/epa/admit.py` | **CONFIRMED scaffold** | Contains a one-line greenfield placeholder for an admission gate. | No RAW/QUARANTINE routing or policy enforcement is implemented. |
| `connectors/epa/src/epa/descriptor.yaml` | **CONFIRMED placeholder** | Declares `name: epa`, with `role: TBD`, `rights: TBD`, and `sensitivity_floor: public`. | Does not establish a reviewed canonical source descriptor, rights decision, or activation state. |
| `connectors/epa/tests/README.md` | **CONFIRMED** | Connector-local test guidance exists. | Does not prove test files, passing tests, or CI wiring. |

### Current maturity determination

The directory is a documented scaffold, not a verified working connector.

- **CONFIRMED:** the source root and four package entries exist.
- **CONFIRMED:** `fetch.py` and `admit.py` are placeholders.
- **CONFIRMED:** `descriptor.yaml` contains unresolved `TBD` values.
- **PROPOSED:** future fetch and admit implementations should preserve the boundary defined here.
- **UNKNOWN:** import path, package metadata, runtime behavior, endpoint coverage, tests, CI, emitted receipts, and downstream integration.

---

## Authority boundary

```text
THIS SOURCE ROOT MAY:
  implement bounded EPA fetch behavior
  prepare source-admission candidates
  preserve source identity and retrieval metadata
  compute deterministic digests
  return finite connector outcomes
  target RAW or QUARANTINE handoff

THIS SOURCE ROOT MUST NOT:
  declare EPA-derived facts true
  act as the canonical source registry
  decide rights or sensitivity by itself
  own schemas, contracts, policy, evidence, proofs, or releases
  write directly to PROCESSED, CATALOG, TRIPLET, or PUBLISHED
  expose credentials or private endpoint material
  silently repair missing source facts
  turn generated language into evidence
```

The local `descriptor.yaml` is connector-adjacent scaffolding. Because its role and rights fields remain unresolved, it must not be treated as an activated or authoritative source descriptor. A reviewed registry record and the applicable policy decision must govern live source use.

---

## Lifecycle handoff

The EPA connector participates only at the source edge of the KFM lifecycle:

```text
EPA source
  -> fetch candidate
  -> admit or quarantine decision
  -> RAW or QUARANTINE
  -> WORK
  -> PROCESSED
  -> CATALOG / TRIPLET
  -> PUBLISHED
```

| Lifecycle stage | Source-root responsibility |
|---|---|
| Pre-RAW | Prepare a bounded request and preserve source context when live access is authorized. |
| RAW | Produce or hand off immutable source material with retrieval metadata and digest support. |
| QUARANTINE | Route unresolved, malformed, sensitive, rights-unclear, or drifted material for review. |
| WORK | No ownership; downstream pipelines may consume admitted material. |
| PROCESSED | No ownership. |
| CATALOG / TRIPLET | No ownership. |
| PUBLISHED | No ownership. |
| RELEASE / CORRECTION / ROLLBACK | No ownership. |

Promotion remains a governed state transition. A successful fetch or admission helper call is not publication evidence.

---

## File contracts

### `epa/fetch.py`

**Current state:** one-line greenfield placeholder.

Future implementation should:

- require explicit configuration rather than hidden import-time behavior;
- make network access deliberate and bounded;
- use finite timeouts and retries;
- preserve the source endpoint key, retrieval time, response status, and safe diagnostic context;
- avoid logging credentials or unrestricted response bodies;
- return a typed or otherwise contract-bound result suitable for admission review;
- avoid writing directly to downstream lifecycle stores.

It should not claim that a successful HTTP response is valid, admissible, authoritative, or publishable.

### `epa/admit.py`

**Current state:** one-line greenfield placeholder.

Future implementation should:

- accept a fetched or fixture-backed source candidate;
- verify the required source descriptor reference and activation state;
- preserve source role, rights, sensitivity, freshness, and retrieval metadata;
- select only RAW, QUARANTINE, ABSTAIN, DENY, or ERROR-style bounded outcomes as the surrounding contract permits;
- emit reviewable reasons for quarantine or refusal;
- avoid normalizing EPA material into domain truth inside the connector.

It should not bypass contracts, schemas, policy, validation, evidence closure, or release review.

### `epa/descriptor.yaml`

**Current state:** placeholder with unresolved role and rights.

```yaml
name: epa
role: TBD
rights: TBD
sensitivity_floor: public
```

Required hardening before live activation:

- replace `TBD` values through source-steward review;
- bind the local file to the canonical source-registry identity or remove duplication if repo convention does not allow a connector-local descriptor;
- record source program or endpoint scope rather than treating all EPA systems as one undifferentiated source;
- record rights, citation, access, cadence, freshness, sensitivity, and failure posture;
- validate the descriptor against the accepted source schema;
- document whether this file is canonical, generated, mirrored, or connector-local configuration.

Until those questions are resolved, live activation remains **DENY by default**.

### `epa/README.md`

The package README documents the intended package boundary. It should be updated alongside implementation so that its module inventory reflects the repository rather than a proposed `config.py` / `client.py` / `parser.py` layout that does not currently exist.

---

## Safety and runtime posture

| Concern | Required posture |
|---|---|
| Import behavior | Importing connector code must not perform network I/O. |
| Credentials | Never required for reading documentation or running no-network tests; never committed. |
| Live access | Explicit opt-in, source-descriptor-backed, rate-limited, and steward-reviewable. |
| Retries | Finite and observable; no uncontrolled polling. |
| Logging | Safe metadata only; no secrets or excessive source payload copying. |
| Determinism | The same fixture, configuration, and code version should produce the same normalized admission candidate and digest. |
| Unknown rights or role | Quarantine, deny, or abstain; do not guess. |
| Schema drift | Surface a reviewable drift outcome; do not silently coerce. |
| Publication | Forbidden from this package. |

> [!CAUTION]
> EPA is an umbrella source family with many programs and endpoints. A single connector label must not flatten distinct source roles, terms, update cadences, spatial supports, or evidentiary limits.

---

## Testing relationship

Connector-local test guidance lives at `connectors/epa/tests/README.md`.

Tests for this source root should be no-network by default and should verify at least:

- importing modules causes no network activity;
- live behavior cannot run without explicit enablement and a reviewed source reference;
- fetch timeout, forbidden, rate-limit, empty-response, malformed-response, and schema-drift cases are finite and reviewable;
- admission results target RAW or QUARANTINE only;
- unresolved rights, role, sensitivity, or source drift fails closed;
- deterministic fixtures produce stable metadata and digests;
- no connector-local test writes to processed, catalog, triplet, published, proof, receipt, or release stores.

The exact test command and CI integration remain **NEEDS VERIFICATION**. Do not claim `pytest` coverage or passing CI until actual test files and workflow results are inspected.

---

## Definition of done

This source root is ready to move beyond scaffold status when:

- [ ] `fetch.py` contains bounded, testable implementation rather than a placeholder.
- [ ] `admit.py` contains contract-bound RAW/QUARANTINE admission logic rather than a placeholder.
- [ ] The source descriptor role, rights, sensitivity, citation, cadence, and activation state are reviewed and schema-valid.
- [ ] Canonical versus connector-local descriptor ownership is documented without creating parallel authority.
- [ ] Imports do not perform network I/O or read secrets as a side effect.
- [ ] Live access is opt-in, bounded, and steward-approved.
- [ ] No-network fixtures cover success and negative cases.
- [ ] Errors and drift outcomes are finite, actionable, and safe to log.
- [ ] Outputs preserve source identity, retrieval metadata, time, and digest support.
- [ ] Outputs are limited to RAW or QUARANTINE handoff.
- [ ] Tests and CI wiring are present and verified.
- [ ] Package and source-root READMEs match the implemented modules.
- [ ] No code in this root bypasses evidence, policy, review, release, correction, or rollback controls.

---

## Verification backlog

| Item | Status | Evidence needed |
|---|---:|---|
| Determine whether `descriptor.yaml` is canonical, generated, mirrored, or connector-local configuration. | **NEEDS VERIFICATION** | Source registry convention, schema, ADRs, and adjacent connector examples. |
| Resolve `role: TBD` and `rights: TBD`. | **BLOCKING / NEEDS VERIFICATION** | Source-steward and rights review for each EPA program or endpoint. |
| Confirm package import name and packaging metadata. | **UNKNOWN** | `pyproject.toml`, workspace configuration, import tests, or build metadata. |
| Confirm the accepted fetch and admission contracts. | **UNKNOWN** | Contract docs and schemas at the accepted authority homes. |
| Confirm actual EPA programs and endpoints in scope. | **UNKNOWN** | Source catalog, registry records, and approved implementation issue or ADR. |
| Confirm test files and default no-network behavior. | **UNKNOWN** | Repository test inventory and test execution. |
| Confirm CI coverage and required checks. | **UNKNOWN** | Workflow configuration and run results. |
| Confirm RAW and QUARANTINE write interfaces. | **UNKNOWN** | Pipeline or intake contracts and integration tests. |
| Confirm emitted receipt or event-envelope requirements. | **UNKNOWN** | Current schemas, validators, and proof-bearing fixture run. |

---

## Maintenance and rollback

When implementation changes:

1. update this inventory and the package README in the same documentation change;
2. keep source-role, rights, sensitivity, and lifecycle boundaries visible;
3. add or update no-network negative tests;
4. avoid broad connector cleanup unrelated to the EPA lane;
5. revert the documentation commit if the revised contract proves inconsistent with the implemented branch, then prepare a narrower correction.

A Git commit or pull request changes repository documentation only. It does not activate an EPA source, admit data, or make any EPA-derived material KFM-published.

---

## Maintainer note

Keep `connectors/epa/src/` narrow, explicit, and boring. Its job is to make EPA source material safer to fetch, inspect, admit, quarantine, and hand off. Evidence, policy, validation, review, publication, correction, and rollback remain downstream governance responsibilities.
