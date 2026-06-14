<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-api-readme
title: API Package README
type: readme
version: v0.1
status: draft
owners:
  - <package-owner>
  - <api-steward>
  - <security-steward>
  - <schema-steward>
  - <policy-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: packages/api/README.md
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/trust-membrane.md
  - docs/doctrine/lifecycle-law.md
  - docs/adr/ADR-0004-apps-governed-api-is-the-trust-membrane.md
  - docs/architecture/governed-api.md
  - packages/README.md
  - apps/governed-api/README.md
  - schemas/contracts/v1/runtime/runtime_response_envelope.schema.json
  - contracts/
  - policy/
  - data/proofs/evidence_bundle/
  - release/manifests/
  - tests/packages/api/
  - fixtures/packages/api/
tags: [kfm, packages, api, shared-library, governed-api, runtime-response-envelope, client-contracts, trust-membrane, finite-outcomes, governance]
notes:
  - "This README replaces the one-character packages/api stub with a governed shared-package contract."
  - "packages/ contains shared libraries; packages/api/ may contain shared API client, DTO, envelope, test helper, or contract adapter code only when it remains subordinate to apps/governed-api/."
  - "apps/governed-api/ is the public trust membrane. packages/api/ is not the membrane, not a deployable API, and not a bypass around it."
  - "Public clients must not read RAW, WORK, QUARANTINE, internal stores, graph stores, object stores, vector indexes, model runtimes, or unpublished candidates directly."
  - "Concrete implementation, package exports, build scripts, tests, and CI coverage remain NEEDS VERIFICATION until repository evidence proves them."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# API Package

> Shared library package for governed API client types, finite-outcome envelope helpers, generated client adapters, test fixtures, and non-deployable API support code. The executable public trust membrane remains `apps/governed-api/`; this package must not become a second API surface or a direct-reader shortcut into KFM internals.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-packages%2F-0a7ea4)
![authority](https://img.shields.io/badge/authority-shared%20library-0a7ea4)
![membrane](https://img.shields.io/badge/membrane-apps%2Fgoverned--api%2F-d62728)
![outcomes](https://img.shields.io/badge/outcomes-ANSWER%20%7C%20ABSTAIN%20%7C%20DENY%20%7C%20ERROR-455a64)

**Status:** Draft  
**Path:** `packages/api/README.md`  
**Responsibility root:** `packages/` — shared libraries used by apps, workers, pipelines, and tools  
**Companion executable boundary:** `apps/governed-api/` — the governed API trust membrane  
**Placement posture:** `packages/api/` may host shared API support code only when it remains reusable, non-deployable, schema-aligned, and subordinate to the governed API boundary.  
**Public posture:** no independent public API, no direct lifecycle-store reads, no model-runtime calls, no release decisions, and no policy bypass.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Trust-membrane boundary](#3-trust-membrane-boundary)
- [4. Package anti-collapse rules](#4-package-anti-collapse-rules)
- [5. What belongs here](#5-what-belongs-here)
- [6. What does not belong here](#6-what-does-not-belong-here)
- [7. Package scope](#7-package-scope)
- [8. RuntimeResponseEnvelope posture](#8-runtimeresponseenvelope-posture)
- [9. Required gates](#9-required-gates)
- [10. Directory contract](#10-directory-contract)
- [11. Inputs and outputs](#11-inputs-and-outputs)
- [12. Minimal package contract shape](#12-minimal-package-contract-shape)
- [13. Tests, fixtures, and validation](#13-tests-fixtures-and-validation)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`packages/api/` is a shared-library lane for API-facing support code that can be reused by KFM applications, tests, tools, workers, and documentation checks.

It may support:

- RuntimeResponseEnvelope type helpers;
- finite-outcome enum helpers;
- typed client helpers for the governed API;
- non-network test doubles and fixtures;
- generated or hand-written API DTO adapters;
- validation helpers that bind package types to schema contracts;
- denial, abstention, citation, evidence-ref, release-ref, and reason-code helpers;
- compatibility shims that keep callers from bypassing `apps/governed-api/`.

It does **not** implement the public API server. The executable trust membrane belongs under `apps/governed-api/`.

Short rule:

```text
apps/governed-api/ = executable public trust membrane
packages/api/      = shared support library for API clients/types/helpers
schemas/           = machine shape
contracts/         = object meaning
policy/            = admissibility and exposure decisions
release/           = release decisions and release control
data/              = lifecycle state and artifacts
```

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `packages/`? | This root owns shared libraries used by apps, workers, pipelines, and tools. | CONFIRMED root contract |
| Why `api/` under packages? | API-support code can be reusable across clients and tests without becoming the executable membrane. | PROPOSED / NEEDS VERIFICATION |
| Is this the public API server? | No. The public trust membrane is `apps/governed-api/`. | CONFIRMED boundary posture |
| Can this package read lifecycle data directly? | No. Public/read-facing API behavior must go through governed interfaces. | CONFIRMED trust-membrane posture |
| Can this package define schemas or contracts? | No. It may consume or mirror generated types, but schema and contract authority live in their roots. | CONFIRMED authority separation |
| Can this package approve release or policy? | No. It may carry refs and reason-code helpers only. | CONFIRMED release/policy separation |

> [!IMPORTANT]
> A shared API package is not an API server, not a trust membrane, not schema authority, not policy authority, not evidence authority, and not release authority.

[⬆ Back to top](#top)

---

## 3. Trust-membrane boundary

KFM doctrine treats the governed API as the single public trust path. Public clients should receive finite outcome envelopes from `apps/governed-api/`, not direct reads from internal lifecycle stores or model runtimes.

`packages/api/` may help callers speak to that membrane, but must not bypass it.

Allowed direction:

```text
public client / app / tool
  -> packages/api client helper
  -> apps/governed-api RuntimeResponseEnvelope
  -> released artifacts + evidence + policy + release state behind the membrane
```

Blocked direction:

```text
public client / app / tool
  -> packages/api helper
  -> data/raw, data/work, data/quarantine, data/processed, internal graph, model runtime, source registry, unpublished candidate
```

This package can make safe behavior easier. It cannot make unsafe behavior acceptable.

[⬆ Back to top](#top)

---

## 4. Package anti-collapse rules

Disallowed collapses:

```text
shared package -> executable API server
client helper -> governed-api bypass
DTO helper -> schema authority
type alias -> contract authority
reason-code helper -> policy decision
EvidenceRef helper -> EvidenceBundle closure
ReleaseManifest ref -> release approval
model adapter type -> direct model client
mock response -> production truth
successful package test -> endpoint compliance
```

Required separations:

- executable public API code stays in `apps/governed-api/`;
- shared package code stays in `packages/api/`;
- schemas stay in `schemas/`;
- contracts stay in `contracts/`;
- policy decisions stay in `policy/`;
- lifecycle data stays in `data/`;
- EvidenceBundles stay in proof homes;
- release decisions stay under `release/`;
- public clients use governed envelopes and released surfaces, not package-internal shortcuts.

[⬆ Back to top](#top)

---

## 5. What belongs here

Appropriate contents include:

- API client interfaces for `apps/governed-api/`;
- RuntimeResponseEnvelope type exports when generated from canonical schema;
- finite-outcome constants: `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`;
- citation, limitation, reason-code, and redaction-state helper types;
- EvidenceRef, PolicyDecisionRef, ReleaseManifestRef, CorrectionNoticeRef, and RollbackCardRef reference helpers;
- test doubles that cannot be mistaken for production endpoints;
- schema-generated types, if the generator records the canonical schema source and generation receipt;
- serialization/deserialization helpers;
- fixture builders for tests;
- compatibility helpers for clients migrating to governed envelopes.

A good placement test:

> If the file is reusable API support code that depends on governed API contracts and does not create a deployable public surface, it may belong here. If it serves requests, reads data stores, evaluates policy, owns routes, or publishes claims, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 6. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Public API server routes | `apps/governed-api/` |
| Review console app code | `apps/review-console/` |
| Explorer/web UI code | `apps/explorer-web/` |
| Runtime model adapters | `runtime/` or accepted internal adapter home behind governed API |
| Canonical schemas | `schemas/contracts/v1/` |
| Object contracts | `contracts/` |
| Policy decisions and rules | `policy/` |
| Lifecycle data reads/writes | `data/` through governed writers/readers only |
| Source descriptors | `data/registry/sources/` |
| EvidenceBundles | `data/proofs/evidence_bundle/` |
| Release decisions/manifests/corrections/rollback cards | `release/` |
| Executable pipeline code | `pipelines/` |
| Pipeline specs | `pipeline_specs/` |
| Package tests | `tests/packages/api/` |
| Package fixtures | `fixtures/packages/api/` |
| Secrets, tokens, credentials, raw prompts, stack traces | never in repo; use approved secret/log redaction controls |

[⬆ Back to top](#top)

---

## 7. Package scope

`packages/api/` may support API-facing concerns such as:

- finite outcome modeling;
- governed envelope parsing and validation;
- citation and limitations display helpers;
- reason-code normalization;
- redaction/generalization state helpers;
- typed request/response DTOs;
- generated clients for app-side consumption;
- mock clients for tests and examples;
- compatibility helpers for domain API contracts;
- safe error-envelope helpers that avoid leaking stack traces or internal context.

Implementation status for concrete modules, exports, package manager configuration, build steps, and CI remains `NEEDS VERIFICATION` unless backed by current repo evidence.

[⬆ Back to top](#top)

---

## 8. RuntimeResponseEnvelope posture

Every trust-bearing API response should resolve to one finite outcome:

| Outcome | Meaning in package helpers | Package responsibility |
|---|---|---|
| `ANSWER` | Evidence sufficient and policy/release state allow response. | Render/parse safely; do not invent missing evidence. |
| `ABSTAIN` | Evidence insufficient, stale, unresolved, or uncitable. | Preserve reason codes and limitations. |
| `DENY` | Policy, rights, sensitivity, or release state forbids response. | Preserve denial reason without leaking restricted content. |
| `ERROR` | API cannot evaluate or encountered a contract/infrastructure failure. | Preserve safe error envelope; no stack/prompt/secret leakage. |

Package helpers must not create a fifth public outcome, silently coerce denial into an answer, or treat missing evidence as success.

[⬆ Back to top](#top)

---

## 9. Required gates

Before this package can be used by production callers, it should have:

1. **Schema gate** — generated or hand-written types reconciled with canonical schemas.
2. **Envelope gate** — finite outcomes preserved exactly.
3. **Evidence gate** — EvidenceRef arrays and limitations preserved without fabrication.
4. **Policy gate** — PolicyDecisionRef and denial reason codes preserved without weakening.
5. **Release gate** — ReleaseManifestRef, correction notices, and rollback refs preserved.
6. **Trust-membrane gate** — no direct lifecycle, graph, object-store, source-registry, or model-runtime reads.
7. **Error-safety gate** — safe error envelopes; no secret, stack trace, raw prompt, or internal path leakage.
8. **Fixture gate** — no-network tests for envelope handling.
9. **Compatibility gate** — deprecation/migration notes for any old API shape.
10. **Review gate** — API steward and security steward review for trust-bearing changes.

[⬆ Back to top](#top)

---

## 10. Directory contract

Recommended shape:

```text
packages/api/
├── README.md
├── package.json                 # NEEDS VERIFICATION / PROPOSED if JS package
├── pyproject.toml               # NEEDS VERIFICATION / PROPOSED if Python package
├── src/
│   ├── index.*                  # PROPOSED
│   ├── runtime_response_envelope.*
│   ├── outcomes.*
│   ├── clients/
│   ├── refs/
│   ├── errors/
│   └── fixtures/
├── generated/                   # PROPOSED, only if generated from canonical schemas
└── README.md
```

The specific language/runtime is `UNKNOWN` from current evidence. Do not add parallel JS/Python package layouts without an implementation decision, package manifest, tests, and migration note.

[⬆ Back to top](#top)

---

## 11. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Package source | `packages/api/` | Shared library only. |
| Executable governed API | `apps/governed-api/` | The trust membrane. |
| Runtime envelope schema | `schemas/contracts/v1/runtime/` | Schema authority. |
| Object contracts | `contracts/` | Meaning authority. |
| Policy refs | `policy/` outputs/refs | Do not decide policy here. |
| Evidence refs | `data/proofs/evidence_bundle/` refs | Do not create proof here. |
| Release refs | `release/` refs | Do not approve release here. |
| Tests | `tests/packages/api/` | Package validation. |
| Fixtures | `fixtures/packages/api/` | No-network package fixtures. |
| Public UI consumers | `apps/explorer-web/`, `apps/review-console/`, exports/story surfaces | Consume governed envelopes through package helpers if appropriate. |

[⬆ Back to top](#top)

---

## 12. Minimal package contract shape

```yaml
package_id: kfm.packages.api
status: draft
authority: shared_library
not_authority_for:
  - public_api_server
  - schema_home
  - contract_home
  - policy_decision
  - evidence_bundle
  - release_decision
  - lifecycle_data
allowed_exports:
  - RuntimeResponseEnvelope helpers
  - finite outcome helpers
  - governed API client helpers
  - safe error-envelope helpers
  - citation and limitation helpers
required_invariants:
  finite_outcomes: [ANSWER, ABSTAIN, DENY, ERROR]
  no_direct_lifecycle_reads: true
  no_direct_model_client: true
  no_release_approval: true
  no_policy_bypass: true
  no_evidence_fabrication: true
```

[⬆ Back to top](#top)

---

## 13. Tests, fixtures, and validation

Recommended validation coverage:

```text
tests/packages/api/
├── test_runtime_response_envelope_shape.py      # PROPOSED
├── test_finite_outcomes.py                      # PROPOSED
├── test_abstain_and_deny_are_not_answers.py     # PROPOSED
├── test_evidence_refs_preserved.py              # PROPOSED
├── test_policy_release_refs_preserved.py        # PROPOSED
├── test_no_direct_lifecycle_reads.py            # PROPOSED
├── test_safe_error_envelopes.py                 # PROPOSED
├── test_generated_types_match_schema.py         # PROPOSED
└── test_root_boundary.py                        # PROPOSED
```

A package change is not ready for production use until it has tests, fixtures, schema alignment, steward review, and proof that it cannot bypass the governed API trust membrane.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- replaces the one-character `packages/api/README.md` stub;
- identifies `packages/api/` as shared API support, not a deployable public API;
- preserves `apps/governed-api/` as the trust membrane;
- blocks direct reads of lifecycle stores, model runtimes, source registries, unpublished candidates, and internal proof/receipt stores;
- blocks the package from becoming schema, contract, policy, evidence, release, or public truth authority;
- defines expected package scope, root boundaries, finite outcomes, tests, fixtures, and open questions.

Future package files are done only when they are schema-aligned, test-covered, steward-reviewed, and unable to bypass the governed API trust membrane.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `PKG-API-001` | Is `packages/api/` a JavaScript/TypeScript package, Python package, generated-client home, or mixed-language home? | NEEDS VERIFICATION / ADR |
| `PKG-API-002` | Which schema generator, if any, owns generated API types? | NEEDS VERIFICATION |
| `PKG-API-003` | Which CI workflow validates this package? | UNKNOWN |
| `PKG-API-004` | Which package exports are active today? | UNKNOWN |
| `PKG-API-005` | Should old client shapes be retained as compatibility shims or removed? | NEEDS VERIFICATION |
| `PKG-API-006` | Which tests prove no direct lifecycle/model/source-registry reads? | NEEDS VERIFICATION |

---

## Maintainer note

Keep this package subordinate to the governed API. Do not add public server routes, lifecycle-store readers, source-registry readers for public clients, direct model clients, schema authority, policy decisions, EvidenceBundle fabrication, release decisions, secrets, credentials, raw prompts, stack traces, or generated claims here. Put those concerns in their responsibility roots and reference them through governed contracts.
