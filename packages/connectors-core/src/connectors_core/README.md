<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-connectors-core-src-connectors-core-readme
title: Connectors Core Source Module README
type: readme
version: v0.1
status: draft
owners:
  - <package-owner>
  - <connector-steward>
  - <source-steward>
  - <security-steward>
  - <evidence-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: packages/connectors-core/src/connectors_core/README.md
related:
  - packages/README.md
  - packages/connectors-core/README.md
  - connectors/README.md
  - docs/sources/ADMISSION_PROCESS.md
  - data/registry/sources/
  - data/raw/
  - data/quarantine/
  - data/receipts/ingest/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - contracts/source/
  - schemas/contracts/v1/source/
  - schemas/contracts/v1/receipts/
  - policy/sources/
  - policy/sensitivity/
  - tests/packages/connectors-core/
  - fixtures/packages/connectors-core/
tags: [kfm, packages, connectors-core, src, connectors_core, shared-library, source-admission, fetch-result, retry, manifest, checksum, quarantine, receipts, governance]
notes:
  - "This README fills the empty packages/connectors-core/src/connectors_core README with a governed source-module contract."
  - "packages/connectors-core/src/connectors_core/ may contain internal source code for shared connector primitives only; it must remain subordinate to packages/connectors-core/."
  - "Connector primitives may shape fetch results, retry behavior, manifest fields, and safe errors. They cannot admit sources, write lifecycle records, create EvidenceBundles, decide policy, or approve release."
  - "Concrete language runtime, module exports, build scripts, and CI coverage remain NEEDS VERIFICATION until repository evidence proves them."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Connectors Core Source Module

> Internal source-code module area for the `packages/connectors-core/` shared library. This directory may hold reusable connector primitives, but it must not become source-specific connector code, source admission authority, lifecycle writer, policy engine, EvidenceBundle authority, release authority, or public trust membrane.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-packages%2Fconnectors--core%2Fsrc%2Fconnectors__core%2F-0a7ea4)
![authority](https://img.shields.io/badge/authority-package%20source%20module-0a7ea4)
![connectors](https://img.shields.io/badge/source--specific-connectors%2F-d62728)
![admission](https://img.shields.io/badge/admission-governed-d62728)

**Status:** Draft  
**Path:** `packages/connectors-core/src/connectors_core/README.md`  
**Parent package:** `packages/connectors-core/`  
**Responsibility root:** `packages/` — shared libraries used by apps, workers, pipelines, and tools  
**Source-specific connector root:** `connectors/`  
**Source registry:** `data/registry/sources/`  
**Lifecycle homes:** `data/raw/` and `data/quarantine/` for governed connector/admission output  
**Placement posture:** source code for reusable connector primitives only. Runtime, exports, package manifest, and active tests are `NEEDS VERIFICATION` until checked by current repo evidence.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Module boundary](#3-module-boundary)
- [4. Anti-collapse rules](#4-anti-collapse-rules)
- [5. What belongs here](#5-what-belongs-here)
- [6. What does not belong here](#6-what-does-not-belong-here)
- [7. Expected module families](#7-expected-module-families)
- [8. Inputs and outputs](#8-inputs-and-outputs)
- [9. Minimal module contract shape](#9-minimal-module-contract-shape)
- [10. Tests and fixtures](#10-tests-and-fixtures)
- [11. Definition of done](#11-definition-of-done)
- [12. Open questions](#12-open-questions)

---

## 1. Purpose

`packages/connectors-core/src/connectors_core/` may hold internal source modules for the shared connector support package.

It may support reusable helpers for:

- connector base interfaces and abstract result types;
- retry, backoff, timeout, and bounded failure behavior;
- fetch result and fetch error normalization;
- source-head, ETag, Last-Modified, header, checksum, digest, and manifest helpers;
- source-intake and admission-preflight helper structures;
- quarantine reason and fail-closed helper structures;
- safe metadata capture and redaction labels;
- no-network fixture and fake transport helpers for tests.

It does **not** own source-specific fetch behavior, source admission decisions, RAW capture authority, QUARANTINE routing authority, EvidenceBundle creation, policy decisions, or release decisions.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why under `packages/connectors-core/`? | Parent package is the shared connector support library. | CONFIRMED parent package contract |
| Why `src/connectors_core/`? | This is a plausible internal module path for connector-core source code. | PROPOSED / NEEDS VERIFICATION |
| Is this source-specific connector code? | No. Source-specific fetch and admission code belongs under `connectors/`. | CONFIRMED boundary posture |
| Can this admit sources? | No. Admission is a governed decision tied to source identity, role, rights, sensitivity, cadence, and steward review. | CONFIRMED admission separation |
| Can this write RAW or QUARANTINE directly? | Not as hidden package behavior. Governed connector/admission flows own lifecycle writes. | CONFIRMED lifecycle posture |
| Can this decide policy, evidence, or release? | No. It may preserve metadata and refs only. | CONFIRMED policy/evidence/release separation |

> [!IMPORTANT]
> Source modules here can help format, validate, and preserve connector metadata. They cannot turn a fetch result into admitted source material, evidence closure, policy approval, or release approval.

[⬆ Back to top](#top)

---

## 3. Module boundary

Allowed direction:

```text
source-specific connector / watcher / ingest pipeline / test
  -> packages/connectors-core/src/connectors_core helper
  -> normalized fetch result, manifest fields, retry decision, safe error, or fixture object
  -> governed connector/admission flow handles lifecycle output where authorized
```

Blocked direction:

```text
packages/connectors-core/src/connectors_core helper
  -> source admission decision
  -> hidden data/raw write
  -> hidden data/quarantine write
  -> policy decision
  -> EvidenceBundle creation
  -> catalog truth
  -> release approval
```

The module should be side-effect-minimal where practical. Any future IO helper must be explicit, bounded, test-covered, reviewable, and used by governed connector/admission code.

[⬆ Back to top](#top)

---

## 4. Anti-collapse rules

Disallowed collapses:

```text
source module -> source-specific connector
base class -> source admission
retry success -> source validation
fetch success -> rights approval
checksum match -> EvidenceBundle closure
manifest helper -> RunReceipt authority
source-head helper -> freshness proof by itself
SourceDescriptorRef -> source activation
fixture response -> production source
successful module test -> source admissibility
```

Required separations:

- reusable source code stays under `packages/connectors-core/src/connectors_core/`;
- source-specific connector code stays under `connectors/`;
- source descriptors and activation state stay in source registry/admission homes;
- RAW and QUARANTINE writes stay in governed lifecycle flows;
- receipts stay in receipt homes;
- EvidenceBundles stay in proof homes;
- schemas and contracts stay under their authority roots;
- source/sensitivity policy decisions stay under `policy/`;
- release decisions stay under `release/`.

[⬆ Back to top](#top)

---

## 5. What belongs here

Appropriate source modules include helpers for:

- connector base interfaces;
- fetch client abstraction interfaces;
- retry, backoff, timeout, and failure-state models;
- fetch result, fetch error, and source-change result models;
- manifest, checksum, digest, ETag, Last-Modified, source-head, and header helpers;
- redaction-safe metadata helpers;
- source-intake helper types that do not decide admission;
- quarantine reason-code helpers;
- receipt-adjacent shape helpers;
- fake transport and no-network fixture helpers.

A good placement test:

> If the module is reusable connector primitive code that remains source-agnostic and does not decide admission, write lifecycle records, evaluate policy, or approve release, it may belong here.

[⬆ Back to top](#top)

---

## 6. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Source-specific connector implementation | `connectors/<source>/` |
| Source admission decision code | source admission workflow / source registry authority |
| Source descriptors | `data/registry/sources/` |
| RAW payloads | `data/raw/` |
| QUARANTINE payloads | `data/quarantine/` |
| Runtime receipts | `data/receipts/ingest/`, `data/receipts/pipeline/` |
| EvidenceBundles | `data/proofs/evidence_bundle/` |
| Catalog records | `data/catalog/` |
| Canonical schemas | `schemas/contracts/v1/` |
| Object contracts | `contracts/` |
| Source/sensitivity policy decisions | `policy/sources/`, `policy/sensitivity/` |
| Release decisions/manifests/corrections/rollback cards | `release/` |
| Executable ingest pipelines | `pipelines/ingest/` or accepted domain ingest lanes |
| Watcher execution | `pipelines/watchers/` |
| Tests | `tests/packages/connectors-core/` |
| Fixtures | `fixtures/packages/connectors-core/` unless package-local convention is accepted |

[⬆ Back to top](#top)

---

## 7. Expected module families

| Module family | Responsibility | Status |
|---|---|---|
| `base` | Connector base interfaces and abstract result contracts. | PROPOSED |
| `retry` | Retry, backoff, timeout, and bounded failure behavior. | PROPOSED |
| `fetch_result` | Normalized fetch result and fetch error shapes. | PROPOSED |
| `manifest` | Manifest field assembly and integrity helper fields. | PROPOSED |
| `checksum` | Checksum, digest, and source-head helpers. | PROPOSED |
| `errors` | Safe error classification and reporting helpers. | PROPOSED |
| `redaction` | Metadata safety and redaction labels. | PROPOSED |
| `fixtures` | Fake transport and no-network test helpers. | NEEDS VERIFICATION |

[⬆ Back to top](#top)

---

## 8. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Module source | `packages/connectors-core/src/connectors_core/` | Shared helper source only. |
| Package entrypoint | `packages/connectors-core/` | Language-specific entrypoint is not verified. |
| Source-specific connector | `connectors/<source>/` | Uses helpers; owns source-specific logic. |
| Source descriptor | `data/registry/sources/` | Referenced, not activated here. |
| RAW payload | `data/raw/` | Written by governed admission/ingest. |
| QUARANTINE payload | `data/quarantine/` | Written by governed fail-closed flow. |
| Ingest receipt | `data/receipts/ingest/` | Emitted by governed execution. |
| Pipeline receipt | `data/receipts/pipeline/` | Emitted by governed execution. |
| Evidence proof | `data/proofs/evidence_bundle/` | Not created here. |
| Tests | `tests/packages/connectors-core/` | Package validation. |
| Fixtures | `fixtures/packages/connectors-core/` | No-network package fixtures. |

[⬆ Back to top](#top)

---

## 9. Minimal module contract shape

```yaml
module_id: kfm.packages.connectors_core.src.connectors_core
status: draft
authority: package_source_module
not_authority_for:
  - source_specific_connector
  - source_admission
  - raw_capture
  - quarantine_write
  - lifecycle_promotion
  - policy_decision
  - evidence_bundle
  - release_decision
allowed_responsibilities:
  - connector base interfaces
  - retry and timeout helpers
  - fetch result models
  - manifest helpers
  - checksum and digest helpers
  - safe error models
  - no-network fixture helpers
required_invariants:
  no_hidden_lifecycle_writes: true
  no_source_admission: true
  no_policy_bypass: true
  no_evidence_fabrication: true
  no_release_approval: true
  sensitive_metadata_safe: true
```

[⬆ Back to top](#top)

---

## 10. Tests and fixtures

Recommended validation coverage:

```text
tests/packages/connectors-core/
├── test_connectors_core_module_boundaries.py # PROPOSED
├── test_base_interfaces.py                   # PROPOSED
├── test_retry_backoff_bounds.py              # PROPOSED
├── test_fetch_result_shape.py                # PROPOSED
├── test_manifest_helpers.py                  # PROPOSED
├── test_checksum_digest_helpers.py           # PROPOSED
├── test_sensitive_metadata_safe.py           # PROPOSED
├── test_no_hidden_lifecycle_writes.py        # PROPOSED
├── test_no_source_admission.py               # PROPOSED
└── test_fake_transport_no_network.py         # PROPOSED
```

Fixture material should live in `fixtures/packages/connectors-core/` unless a package-local fixture convention is explicitly accepted. Fixtures should be synthetic or sanitized and must not contain private connection material or sensitive payloads.

[⬆ Back to top](#top)

---

## 11. Definition of done

This README is done when it:

- fills the empty `packages/connectors-core/src/connectors_core/README.md` file;
- identifies this directory as package source for shared connector primitives;
- keeps source-specific connectors under `connectors/`;
- keeps source admission, RAW/QUARANTINE output, receipts, evidence, policy, and release in their own authority roots;
- blocks helper modules from becoming source-specific connectors, source-admission tools, lifecycle writers, EvidenceBundle creators, policy engines, release approvers, schema authority, or contract authority;
- defines expected module families, inputs/outputs, tests, fixtures, and open questions.

Future source files in this module are done only when they are test-covered, steward-reviewed, metadata-safe, deterministic where practical, and unable to bypass source admission, lifecycle, evidence, policy, and release controls.

[⬆ Back to top](#top)

---

## 12. Open questions

| ID | Question | Status |
|---|---|---|
| `PKG-CONN-CORE-SRC-001` | Which language/runtime owns `packages/connectors-core/src/connectors_core/`? | UNKNOWN |
| `PKG-CONN-CORE-SRC-002` | Which module names are actually exported by the package? | UNKNOWN |
| `PKG-CONN-CORE-SRC-003` | Should fake transports and fixture builders live in source, tests, or `fixtures/packages/connectors-core/` only? | NEEDS VERIFICATION |
| `PKG-CONN-CORE-SRC-004` | Which canonical schema owns fetch result, manifest, and receipt-adjacent helper shapes? | NEEDS VERIFICATION |
| `PKG-CONN-CORE-SRC-005` | Which CI workflow verifies retry bounds and no hidden lifecycle writes? | UNKNOWN |
| `PKG-CONN-CORE-SRC-006` | Which source-intake helper names are canonical versus proposed? | NEEDS VERIFICATION / ADR |

---

## Maintainer note

Keep this module source-agnostic, metadata-safe, deterministic, and subordinate to source admission governance. Do not add source-specific admission decisions, lifecycle writers, EvidenceBundle writers, policy decisions, release decisions, public API routes, UI behavior, private connection material, sensitive real payloads, or generated truth claims here.
