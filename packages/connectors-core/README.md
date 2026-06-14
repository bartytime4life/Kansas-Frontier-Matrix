<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-connectors-core-readme
title: Connectors Core Package README
type: readme
version: v0.1
status: draft
owners:
  - <package-owner>
  - <connector-steward>
  - <source-steward>
  - <security-steward>
  - <evidence-steward>
  - <pipeline-owner>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: packages/connectors-core/README.md
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - docs/doctrine/trust-membrane.md
  - docs/sources/ADMISSION_PROCESS.md
  - packages/README.md
  - connectors/README.md
  - pipeline_specs/watchers/README.md
  - pipelines/watchers/README.md
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
tags: [kfm, packages, connectors-core, connectors, shared-library, source-admission, retries, manifests, receipts, source-descriptor, source-intake, quarantine, governance]
notes:
  - "This README expands the short packages/connectors-core stub into a governed shared-package contract."
  - "packages/ contains shared libraries; packages/connectors-core/ may contain reusable connector base classes, retry policies, fetch result models, manifest helpers, and receipt helper utilities."
  - "connectors/ owns source-specific fetch and admission code. connectors-core is shared support, not a source-specific connector."
  - "Connector helpers may support admission preflight, manifest field assembly, checksums, and retry behavior, but they cannot admit a source, publish data, create EvidenceBundles, decide policy, or bypass lifecycle gates by themselves."
  - "Concrete implementation, package exports, build scripts, tests, and CI coverage remain NEEDS VERIFICATION until repository evidence proves them."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Connectors Core Package

> Shared library package for connector support: base classes, retry/backoff policies, fetch result types, manifest helpers, checksum/header helpers, source-intake helpers, safe error models, and receipt-adjacent utilities. Source-specific connectors remain under `connectors/`; source admission remains a governed decision; lifecycle outputs remain under `data/`.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-packages%2F-0a7ea4)
![authority](https://img.shields.io/badge/authority-shared%20library-0a7ea4)
![connectors](https://img.shields.io/badge/source--specific-connectors%2F-d62728)
![admission](https://img.shields.io/badge/admission-governed-d62728)

**Status:** Draft  
**Path:** `packages/connectors-core/README.md`  
**Responsibility root:** `packages/` — shared libraries used by apps, workers, pipelines, and tools  
**Companion connector root:** `connectors/` — source-specific fetch and admission code  
**Source registry:** `data/registry/sources/`  
**Lifecycle output homes:** `data/raw/`, `data/quarantine/`, and downstream governed lifecycle roots  
**Placement posture:** `packages/connectors-core/` may host reusable connector support code only when it remains source-agnostic, non-deployable, testable, and subordinate to source admission, lifecycle, policy, and receipt authority.  
**Public posture:** no public API, no source-specific connector authority, no source admission decision, no lifecycle promotion, no EvidenceBundle creation, no policy decision, and no release approval.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Connector responsibility boundary](#3-connector-responsibility-boundary)
- [4. Package anti-collapse rules](#4-package-anti-collapse-rules)
- [5. What belongs here](#5-what-belongs-here)
- [6. What does not belong here](#6-what-does-not-belong-here)
- [7. Package scope](#7-package-scope)
- [8. Manifest and receipt posture](#8-manifest-and-receipt-posture)
- [9. Required gates](#9-required-gates)
- [10. Directory contract](#10-directory-contract)
- [11. Inputs and outputs](#11-inputs-and-outputs)
- [12. Minimal package contract shape](#12-minimal-package-contract-shape)
- [13. Tests, fixtures, and validation](#13-tests-fixtures-and-validation)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`packages/connectors-core/` is a shared-library lane for connector support code that can be reused by source-specific connectors, watcher implementations, ingest workflows, tests, and tools.

It may support:

- connector base classes and interfaces;
- retry, backoff, timeout, and circuit-breaker helpers;
- fetch result and fetch error models;
- source-head, ETag, Last-Modified, checksum, digest, and manifest helpers;
- safe request/response metadata capture;
- source-intake helper models;
- admission preflight helpers;
- quarantine reason helper types;
- receipt-adjacent manifest helpers;
- no-network fixture builders for connector tests.

It does **not** own source-specific fetching, source admission decisions, RAW capture authority, public publication, or release decisions. Those responsibilities stay in their governance roots.

Short rule:

```text
packages/connectors-core/ = shared connector support library
connectors/               = source-specific fetch and admission code
data/registry/sources/    = source descriptors and source identity registry
data/raw/                 = admitted raw source payloads
data/quarantine/          = failed-closed or unresolved source material
policy/                   = source/sensitivity policy decisions
release/                  = release decisions and release control
```

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `packages/`? | This root owns shared libraries used by apps, workers, pipelines, and tools. | CONFIRMED root contract |
| Why `connectors-core/` under packages? | Reusable connector primitives can support source-specific connectors without becoming a connector itself. | CONFIRMED stub intent / NEEDS VERIFICATION for implementation |
| Is this source-specific connector code? | No. Source-specific fetch and admission code belongs under `connectors/`. | CONFIRMED boundary posture |
| Can this admit sources? | No. It may provide helpers, but source admission is a governed decision tied to source identity, role, rights, and sensitivity. | CONFIRMED admission separation |
| Can this write RAW or QUARANTINE directly? | Not as hidden package behavior. Source-specific governed execution owns lifecycle writes. | CONFIRMED lifecycle posture |
| Can this decide policy, evidence, or release? | No. It may preserve refs and receipt fields only. | CONFIRMED policy/evidence/release separation |

> [!IMPORTANT]
> Shared connector primitives are not source authority. A helper that computes a digest, builds a manifest, retries a request, or formats a fetch result does not admit a source, validate evidence, or publish data.

[⬆ Back to top](#top)

---

## 3. Connector responsibility boundary

Allowed direction:

```text
source-specific connector / watcher / ingest pipeline
  -> packages/connectors-core helper
  -> fetch metadata, manifest fields, retry behavior, safe error, or receipt-adjacent structure
  -> governed connector/admission flow writes RAW or QUARANTINE where authorized
```

Blocked direction:

```text
packages/connectors-core helper
  -> source admission decision
  -> hidden data/raw write
  -> hidden data/quarantine write
  -> policy decision
  -> EvidenceBundle creation
  -> catalog truth
  -> release approval
```

The package should favor pure, deterministic, side-effect-minimal helpers. Any IO helper must be explicit, bounded, test-covered, and used by source-specific connector code that emits receipts and respects admission gates.

[⬆ Back to top](#top)

---

## 4. Package anti-collapse rules

Disallowed collapses:

```text
shared package -> source-specific connector
base class -> source admission
retry success -> source validation
fetch success -> rights approval
checksum match -> EvidenceBundle closure
manifest helper -> RunReceipt authority
source-head helper -> freshness proof by itself
SourceDescriptorRef -> source activation
fixture response -> production source
successful package test -> source admissibility
```

Required separations:

- shared connector support stays in `packages/connectors-core/`;
- source-specific connector code stays in `connectors/`;
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

Appropriate contents include:

- connector base classes and interfaces;
- fetch client abstraction interfaces;
- retry/backoff/timeout/circuit-breaker helpers;
- typed fetch result, fetch error, and source-change result models;
- manifest, checksum, digest, ETag, Last-Modified, source-head, and header helpers;
- safe logging/redaction helpers for connector metadata;
- source-intake helper types that do not decide admission;
- quarantine reason-code helpers;
- receipt-adjacent shape helpers;
- no-network fixture builders for connector tests;
- compatibility helpers for connector API migrations.

A good placement test:

> If the file is reusable connector support code that remains source-agnostic and does not decide admission, write lifecycle records, evaluate policy, or approve release, it may belong here.

[⬆ Back to top](#top)

---

## 6. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Source-specific connectors | `connectors/<source>/` |
| Source admission decisions | source admission workflow / source registry authority |
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
| Package tests | `tests/packages/connectors-core/` |
| Package fixtures | `fixtures/packages/connectors-core/` |

[⬆ Back to top](#top)

---

## 7. Package scope

`packages/connectors-core/` may support connector-facing concerns such as:

- stable connector base contracts;
- retry/backoff policy helpers;
- request timeout helpers;
- safe error classification;
- manifest field assembly;
- checksum and digest helpers;
- HTTP metadata capture helpers;
- source-head and source-vintage helper types;
- no-network fixture and fake transport helpers;
- redaction-safe logging helpers;
- helper models that later connectors can map into receipts.

Implementation status for concrete modules, exports, package manager configuration, build steps, and CI remains `NEEDS VERIFICATION` unless backed by current repo evidence.

[⬆ Back to top](#top)

---

## 8. Manifest and receipt posture

This package may help construct manifest-like or receipt-adjacent structures, but it must not blur authority:

| Artifact | Package posture | Authority home |
|---|---|---|
| Fetch manifest fields | Helper output only. | Source-specific connector / ingest pipeline emits governed artifact. |
| Checksum/digest | Integrity helper output. | Receipt or evidence workflow binds it to lifecycle state. |
| Retry log | Helper metadata only. | Execution receipt records final governed result. |
| Source-head/ETag value | Observed source metadata. | Source watcher/connector receipt records and interprets it. |
| RunReceipt | May supply field helpers only. | Receipt writer/emitter owns creation. |
| EvidenceBundle | Never created here. | Evidence proof home and proof workflow. |

A manifest helper is not admission. A receipt helper is not a receipt unless emitted by governed execution with identity, time, source, policy, and lifecycle context.

[⬆ Back to top](#top)

---

## 9. Required gates

Before this package can be used by production connectors, it should have:

1. **Interface gate** — stable connector base interfaces documented and tested.
2. **No-source-specific gate** — no hard-coded source-specific admission rules.
3. **Sensitive-metadata gate** — logs, fixtures, and error paths must avoid exposing private connection material or restricted response metadata.
4. **Retry-safety gate** — retry/backoff behavior is bounded, testable, and does not hide failure state.
5. **Manifest gate** — manifest helpers preserve source URL, retrieval time, content length, checksum, ETag/header/date fields where applicable.
6. **Receipt boundary gate** — helper structures cannot masquerade as emitted receipts.
7. **Admission boundary gate** — helpers cannot admit sources or write RAW/QUARANTINE on their own.
8. **Policy boundary gate** — helpers cannot decide rights or sensitivity outcomes.
9. **Fixture gate** — no-network test coverage and fake transports for deterministic validation.
10. **Review gate** — connector, source, security, and evidence steward review for trust-bearing changes.

[⬆ Back to top](#top)

---

## 10. Directory contract

Recommended shape:

```text
packages/connectors-core/
├── README.md
├── package.json                 # NEEDS VERIFICATION / PROPOSED if JS package
├── pyproject.toml               # NEEDS VERIFICATION / PROPOSED if Python package
├── src/                         # PROPOSED
│   ├── index.*                  # PROPOSED
│   ├── base.*                   # PROPOSED
│   ├── retry.*                  # PROPOSED
│   ├── fetch_result.*           # PROPOSED
│   ├── manifest.*               # PROPOSED
│   ├── checksum.*               # PROPOSED
│   ├── errors.*                 # PROPOSED
│   ├── redaction.*              # PROPOSED
│   └── fixtures.*               # PROPOSED
└── README.md
```

The specific language/runtime is `UNKNOWN` from current evidence. Do not add parallel JS/Python package layouts without an implementation decision, package manifest, tests, and migration note.

[⬆ Back to top](#top)

---

## 11. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Package source | `packages/connectors-core/` | Shared library only. |
| Source-specific connector | `connectors/<source>/` | Uses helpers; owns source-specific logic. |
| Source descriptor | `data/registry/sources/` | Referenced; not created here by helper code alone. |
| Source admission decision | source admission workflow / registry controls | Not decided here. |
| RAW payload | `data/raw/` | Written only by governed admission/ingest. |
| QUARANTINE payload | `data/quarantine/` | Written only by governed failure/quarantine flow. |
| Ingest receipt | `data/receipts/ingest/` | Emitted by governed execution. |
| Pipeline receipt | `data/receipts/pipeline/` | Emitted by governed execution. |
| Evidence proof | `data/proofs/evidence_bundle/` | Not created here. |
| Tests | `tests/packages/connectors-core/` | Package validation. |
| Fixtures | `fixtures/packages/connectors-core/` | No-network package fixtures; synthetic or sanitized only. |

[⬆ Back to top](#top)

---

## 12. Minimal package contract shape

```yaml
package_id: kfm.packages.connectors_core
status: draft
authority: shared_library
not_authority_for:
  - source_specific_connector
  - source_admission
  - raw_capture
  - quarantine_write
  - lifecycle_promotion
  - policy_decision
  - evidence_bundle
  - release_decision
allowed_exports:
  - connector base classes
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

## 13. Tests, fixtures, and validation

Recommended validation coverage:

```text
tests/packages/connectors-core/
├── test_connector_base_interfaces.py       # PROPOSED
├── test_retry_backoff_bounds.py            # PROPOSED
├── test_fetch_result_shape.py              # PROPOSED
├── test_manifest_helpers.py                # PROPOSED
├── test_checksum_digest_helpers.py         # PROPOSED
├── test_sensitive_metadata_safe.py         # PROPOSED
├── test_no_hidden_lifecycle_writes.py      # PROPOSED
├── test_no_source_admission.py             # PROPOSED
├── test_fake_transport_no_network.py       # PROPOSED
└── test_root_boundary.py                   # PROPOSED
```

Fixture material should live in `fixtures/packages/connectors-core/` unless a package-local fixture convention is explicitly accepted. Fixtures should be synthetic or sanitized and must not contain private connection material or sensitive payloads.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- expands the short `packages/connectors-core/README.md` stub;
- identifies `packages/connectors-core/` as shared connector support, not a source-specific connector;
- preserves `connectors/` as source-specific fetch/admission code;
- preserves `data/raw/`, `data/quarantine/`, source registry, receipt, evidence, policy, and release authority boundaries;
- blocks the package from becoming source admission, hidden lifecycle writer, EvidenceBundle creator, policy decision maker, release authority, or public API/UI authority;
- defines expected package scope, manifest/receipt posture, root boundaries, tests, fixtures, and open questions.

Future package files are done only when they are test-covered, steward-reviewed, metadata-safe, deterministic where practical, and unable to bypass source admission, lifecycle, evidence, policy, and release controls.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `PKG-CONN-CORE-001` | Is `packages/connectors-core/` a JavaScript/TypeScript package, Python package, generated-helper home, or mixed-language home? | NEEDS VERIFICATION / ADR |
| `PKG-CONN-CORE-002` | Which connector base interface is canonical? | NEEDS VERIFICATION |
| `PKG-CONN-CORE-003` | Which retry/backoff/timeout policy is canonical across connectors? | NEEDS VERIFICATION |
| `PKG-CONN-CORE-004` | Which manifest and receipt field vocabulary is canonical for connector fetches? | NEEDS VERIFICATION |
| `PKG-CONN-CORE-005` | Which CI workflow validates this package? | UNKNOWN |
| `PKG-CONN-CORE-006` | Should fake transports and fixture builders live here, under tests, or under fixtures only? | NEEDS VERIFICATION / ADR |

---

## Maintainer note

Keep this package source-agnostic, metadata-safe, deterministic, and subordinate to source admission governance. Do not add source-specific admission decisions, lifecycle writers, EvidenceBundle writers, policy decisions, release decisions, public API routes, UI behavior, private connection material, sensitive real payloads, or generated truth claims here.
