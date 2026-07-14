<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-citation-src-citation-readme
title: Citation Package Source Module README
type: readme
version: v0.2
status: draft; repository-grounded; implementation-placeholder; PROPOSED module contract
owners:
  - OWNER_TBD — Package steward
  - OWNER_TBD — Citation steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Contracts steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Validator steward
  - OWNER_TBD — API steward
  - OWNER_TBD — Security / sensitivity steward
  - OWNER_TBD — Docs steward
created: 2026-06-13
updated: 2026-07-14
policy_label: public
supersedes: v0.1 (2026-06-13)
path: packages/citation/src/citation/README.md
repository_snapshot: main@b24b455b7b749203edbfa06557baa8209c3080f6
initial_evidence_snapshot: main@b04e9b4a576557ec8cf2f48f6cbe45fd07fbec7a
related:
  - ../README.md
  - ../../README.md
  - ../../pyproject.toml
  - ../../../README.md
  - ../../../api/README.md
  - ../../../../contracts/evidence/evidence_ref.md
  - ../../../../contracts/evidence/evidence_bundle.md
  - ../../../../contracts/evidence/citation_validation_report.md
  - ../../../../contracts/ui/citation_validation_report.md
  - ../../../../schemas/contracts/v1/evidence/evidence_ref.schema.json
  - ../../../../schemas/contracts/v1/evidence/evidence_bundle.schema.json
  - ../../../../schemas/contracts/v1/evidence/citation_validation_report.schema.json
  - ../../../../fixtures/contracts/v1/evidence/evidence_ref/README.md
  - ../../../../tests/schemas/test_common_contracts.py
  - ../../../../tools/validators/citation/README.md
  - ../../../../tools/validators/evidence/README.md
  - ../../../../tools/validators/evidence_bundle/README.md
  - ../../../../docs/sources/CITATION_GUIDANCE.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../docs/architecture/trust-membrane.md
  - ../../../../apps/governed-api/README.md
  - ../../../../.github/workflows/citation-validation.yml
tags: [kfm, packages, citation, python, source-module, evidence-ref, evidence-bundle, citation-validation, cite-or-abstain, deterministic, no-network, fail-closed, trust-membrane, rollback]
notes:
  - "v0.2 replaces planning-heavy language with a commit-pinned description of the current package surface."
  - "The current package is a Python greenfield placeholder: pyproject.toml declares kfm-citation 0.0.0, citation/__init__.py is empty, and no citation helper implementation was observed at tested paths."
  - "The EvidenceRef contract/schema/fixtures are concrete enough to anchor future package behavior; the dedicated validate_evidence_ref.py wrapper is not present."
  - "The EvidenceBundle schema and validator wrapper exist, but this package must not create or persist EvidenceBundles."
  - "The evidence-family CitationValidationReport schema remains a permissive scaffold; the UI family has a separate permissive projection schema. This package must not invent a canonical report serialization while that split is unresolved."
  - "The citation-validation workflow exists only as an echo-TODO scaffold and does not prove citation resolution or abstain behavior."
  - "No package-specific tests or fixtures were found at tests/packages/citation/ or fixtures/packages/citation/."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Citation Source Module

`packages/citation/src/citation/`

> Python package-source boundary for reusable, deterministic citation and evidence-reference helpers. The module may preserve and validate already-governed reference shapes; it must not create evidence closure, admit sources, fetch hidden facts, decide policy, approve release, write lifecycle state, or serve as the public trust membrane.

![status](https://img.shields.io/badge/status-draft-blue)
![version](https://img.shields.io/badge/version-v0.2-1f6feb)
![implementation](https://img.shields.io/badge/implementation-placeholder-lightgrey)
![runtime](https://img.shields.io/badge/runtime-Python%20package%20scaffold-3776ab)
![evidence](https://img.shields.io/badge/citation-pointer%20%E2%89%A0%20proof-critical)
![network](https://img.shields.io/badge/default-no--network-success)
![public](https://img.shields.io/badge/public%20path-governed%20API-critical)

> [!IMPORTANT]
> **Review-branch base:** `main` at `b24b455b7b749203edbfa06557baa8209c3080f6`  
> **Detailed evidence snapshot:** `main` at `b04e9b4a576557ec8cf2f48f6cbe45fd07fbec7a`; the target and cited support surfaces were rechecked unchanged or intervening changes were confirmed unrelated  
> **Current package metadata:** `kfm-citation`, version `0.0.0`  
> **Current module implementation:** empty `citation/__init__.py`; no helper implementation observed at tested paths  
> **Current canonical concrete input:** `EvidenceRef` schema with `ref`, `kind`, and optional `bundle_ref`  
> **Current citation-report shape:** unresolved—evidence and UI schemas are permissive scaffolds  
> **Current CI:** `citation-validation` workflow is an echo-TODO scaffold  
> **Public boundary:** consumers expose results only through governed application/runtime envelopes

> [!CAUTION]
> A valid reference is not a valid claim. A resolvable reference is not automatically rights-cleared, sensitivity-cleared, reviewed, released, or current. This package may help carry those states; it cannot manufacture them.

---

## Quick jump

- [1. Purpose and audience](#1-purpose-and-audience)
- [2. Current repository state](#2-current-repository-state)
- [3. Bounded context and ubiquitous language](#3-bounded-context-and-ubiquitous-language)
- [4. Authority and non-authority](#4-authority-and-non-authority)
- [5. Current source surface](#5-current-source-surface)
- [6. Core invariants](#6-core-invariants)
- [7. Concrete EvidenceRef contract](#7-concrete-evidenceref-contract)
- [8. EvidenceBundle relationship](#8-evidencebundle-relationship)
- [9. CitationValidationReport uncertainty](#9-citationvalidationreport-uncertainty)
- [10. Proposed module responsibilities](#10-proposed-module-responsibilities)
- [11. Proposed API admission rules](#11-proposed-api-admission-rules)
- [12. Reference normalization rules](#12-reference-normalization-rules)
- [13. Resolution and I/O boundary](#13-resolution-and-io-boundary)
- [14. Findings, errors, and runtime outcomes](#14-findings-errors-and-runtime-outcomes)
- [15. Source role, rights, sensitivity, and limitations](#15-source-role-rights-sensitivity-and-limitations)
- [16. Temporal, correction, and supersession behavior](#16-temporal-correction-and-supersession-behavior)
- [17. Consumer and trust-membrane contract](#17-consumer-and-trust-membrane-contract)
- [18. Directory and file contract](#18-directory-and-file-contract)
- [19. Tests and fixtures](#19-tests-and-fixtures)
- [20. Validation commands](#20-validation-commands)
- [21. Safe change and compatibility discipline](#21-safe-change-and-compatibility-discipline)
- [22. Security and data minimization](#22-security-and-data-minimization)
- [23. Observability and receipts](#23-observability-and-receipts)
- [24. Definition of done](#24-definition-of-done)
- [25. Open verification register](#25-open-verification-register)
- [26. Evidence ledger](#26-evidence-ledger)
- [27. Maintainer checklist](#27-maintainer-checklist)

---

## 1. Purpose and audience

This directory is the Python import-package lane for citation-specific helpers inside [`packages/citation/`](../../README.md).

Its intended value is narrow:

- make contract-shaped citation and evidence references easier to preserve correctly;
- provide deterministic, side-effect-minimal transformations over already-authorized inputs;
- distinguish structural validation from evidence resolution and evidence closure;
- preserve missing, inaccessible, stale, redacted, restricted, corrected, and superseded states;
- provide reusable package-level primitives for validators, pipelines, governed API adapters, tests, and documentation tooling;
- reduce duplicate reference-handling code without creating a second evidence, policy, release, or source authority.

**Primary audience**

- package maintainers;
- citation and evidence stewards;
- schema and contract reviewers;
- validator authors;
- governed API and Evidence Drawer adapters;
- pipeline developers carrying EvidenceRefs;
- test and fixture authors;
- security, rights, and sensitivity reviewers.

This README is a source-module contract. It is not proof that the proposed helper surface is implemented.

[Back to top](#top)

---

## 2. Current repository state

### 2.1 Confirmed package surface

| Path or surface | Current evidence | Status | Consequence |
|---|---|---|---|
| [`../../pyproject.toml`](../../pyproject.toml) | Contains only `[project]`, `name = "kfm-citation"`, and `version = "0.0.0"`. | **CONFIRMED greenfield placeholder** | Build backend, dependencies, Python requirement, package discovery, entry points, and tooling are not defined there. |
| `__init__.py` | File exists and is empty. | **CONFIRMED** | No public exports, version constant, types, helpers, or errors are currently established. |
| `citation.py` | Exact tested path returned no file. | **CONFIRMED absent at tested path** | Do not claim a citation implementation module exists. |
| `package.json` | Exact tested path returned no file. | **CONFIRMED absent at tested path** | This is not currently evidenced as a JavaScript/TypeScript package. |
| `setup.py` | Exact tested path returned no file. | **CONFIRMED absent at tested path** | Packaging relies on no verified legacy setup entrypoint. |
| [`../README.md`](../README.md) | Defines the package source-root boundary. | **CONFIRMED documentation** | It does not prove implementation depth. |
| [`../../README.md`](../../README.md) | Defines the citation package boundary. | **CONFIRMED documentation** | It does not prove exports, consumers, tests, or release readiness. |
| `tests/packages/citation/` | Exact README path not found; indexed search did not surface package tests. | **NOT OBSERVED / search-limited** | No dedicated package test suite is claimed. |
| `fixtures/packages/citation/` | Exact README path not found; indexed search did not surface package fixtures. | **NOT OBSERVED / search-limited** | No package-specific fixture family is claimed. |
| Consuming imports | Search for `kfm-citation` surfaced the package metadata only. | **NOT OBSERVED / search-limited** | No app, pipeline, validator, or tool consumer is claimed. |
| CODEOWNERS | No citation-package-specific rule; generic `* @kfm/maintainers` applies. | **CONFIRMED** | Package-specific reviewer ownership remains unresolved. |

### 2.2 Confirmed evidence/citation support surfaces

| Surface | Current evidence | Status | Module consequence |
|---|---|---|---|
| [`EvidenceRef` contract](../../../../contracts/evidence/evidence_ref.md) | Defines a governed pointer and strict authority boundary. | **CONFIRMED semantic contract / draft** | This is the strongest current anchor for package input behavior. |
| [`EvidenceRef` schema](../../../../schemas/contracts/v1/evidence/evidence_ref.schema.json) | Requires `ref` and `kind`; permits optional `bundle_ref`; rejects additional properties. | **CONFIRMED fielded schema / PROPOSED status** | Structural helpers may align to this exact shape. |
| [`EvidenceRef` fixtures](../../../../fixtures/contracts/v1/evidence/evidence_ref/README.md) | One valid and one invalid fixture; schema harness documented. | **CONFIRMED fixture family** | Package tests may reuse or mirror these only through an explicit test design. |
| Dedicated `validate_evidence_ref.py` | Schema points to it, but exact path returned no file. | **CONFIRMED missing at tested path** | Do not claim dedicated validator-wrapper enforcement. |
| [`test_common_contracts.py`](../../../../tests/schemas/test_common_contracts.py) | Discovers schema/fixture families and validates valid/invalid cases. | **CONFIRMED harness** | EvidenceRef shape can be exercised through the common schema suite. |
| [`EvidenceBundle` schema](../../../../schemas/contracts/v1/evidence/evidence_bundle.schema.json) | Requires claim scope, evidence refs, source records, citation strings, rights, sensitivity, transforms, checksums, and spec hash. | **CONFIRMED fielded schema / PROPOSED status** | The package may preserve bundle references or inspect already-loaded bundles; it must not close or persist them. |
| `validate_evidence_bundle.py` | Wrapper exists and invokes the common schema runner. | **CONFIRMED validator wrapper** | EvidenceBundle validation is an external dependency surface, not this module's authority. |
| [`CitationValidationReport` evidence schema](../../../../schemas/contracts/v1/evidence/citation_validation_report.schema.json) | Empty `properties`, `additionalProperties: true`, no contract pointer. | **CONFIRMED permissive scaffold** | No canonical report serialization can be inferred. |
| [`CitationValidationReport` UI contract](../../../../contracts/ui/citation_validation_report.md) | Defines a downstream UI projection and acknowledges the stronger evidence-family contract. | **CONFIRMED draft projection** | The package must not collapse evidence-report and UI-projection shapes. |
| [`tools/validators/citation/`](../../../../tools/validators/citation/README.md) | README defines proposed validator responsibility; no executable is established by it. | **CONFIRMED README / implementation unverified** | Validation orchestration belongs under tools, not this package. |
| [`citation-validation` workflow](../../../../.github/workflows/citation-validation.yml) | Two jobs only echo TODO messages. | **CONFIRMED CI scaffold** | Workflow success would not prove citation resolution or abstain behavior. |

### 2.3 Implementation boundary

```text
CONFIRMED:
  Python project metadata exists
  package name = kfm-citation
  package version = 0.0.0
  citation/__init__.py exists and is empty
  EvidenceRef contract/schema/fixtures exist
  EvidenceBundle schema and validator wrapper exist
  common schema fixture harness exists
  citation validator README exists
  citation-validation workflow is a TODO scaffold

NOT OBSERVED:
  helper implementation
  public exports
  package dependency declarations
  consuming imports
  package-specific tests
  package-specific fixtures
  dedicated EvidenceRef validator wrapper
  citation validator executable

UNKNOWN:
  production callers
  runtime resolution
  public API integration
  release behavior
  package publication
  compatibility guarantees
```

[Back to top](#top)

---

## 3. Bounded context and ubiquitous language

### Citation support bounded context

This module belongs to the **citation support** bounded context:

> Pure or explicitly injected helper behavior that preserves references, locators, limitations, and validation findings without assuming evidence closure or public admissibility.

### Terms

| Term | Meaning in this module | Not equivalent to |
|---|---|---|
| `EvidenceRef` | Schema-shaped governed pointer containing `ref`, `kind`, and optional `bundle_ref`. | EvidenceBundle closure, source admission, or release approval. |
| `EvidenceBundle` | Claim-scope evidence closure owned by evidence contracts/data/proof workflows. | A citation string or a list of refs. |
| citation string | Current EvidenceBundle schema stores `citations` as non-empty strings. | A canonical structured Citation object; none was verified. |
| citation locator | Page, line, fragment, anchor, or similar package-local input concept. | Proof that the surrounding source supports the claim. |
| resolution | Attempt to obtain governed target state for a reference through an explicitly supplied resolver. | Policy permission or evidence closure. |
| structural validation | Checking a value against a contract/schema shape. | Source quality, claim support, rights, sensitivity, or release validation. |
| citation validation finding | A deterministic package/tool finding about a citation candidate. | Canonical `CitationValidationReport` serialization while its schema is incomplete. |
| limitation | Caveat, access constraint, redaction/generalization state, stale state, or known scope bound. | A reason to silently discard the citation. |
| consumer | App, pipeline, validator, tool, or test importing package helpers. | A public client entitled to internal data. |

### Vocabulary rule

No package-local type may be named as if it were canonical unless a matching semantic contract and machine schema exist or the type is clearly marked internal/projection-only.

[Back to top](#top)

---

## 4. Authority and non-authority

### This module may own

- Python helper implementation for reference-shape preservation;
- deterministic normalization that does not alter canonical identity;
- package-local internal types and exceptions;
- injected resolver protocols or interfaces that perform no hidden I/O by default;
- safe conversion from canonical evidence objects to caller-specific, non-authoritative projections;
- deterministic validation findings;
- package-local compatibility shims with explicit deprecation windows.

### This module does not own

| Responsibility | Correct authority |
|---|---|
| EvidenceRef meaning | [`contracts/evidence/evidence_ref.md`](../../../../contracts/evidence/evidence_ref.md) |
| EvidenceBundle meaning | [`contracts/evidence/evidence_bundle.md`](../../../../contracts/evidence/evidence_bundle.md) |
| CitationValidationReport meaning | [`contracts/evidence/citation_validation_report.md`](../../../../contracts/evidence/citation_validation_report.md) |
| UI report projection meaning | [`contracts/ui/citation_validation_report.md`](../../../../contracts/ui/citation_validation_report.md) |
| Machine shape | `schemas/contracts/v1/` |
| Schema validation orchestration | `tools/validators/` and `tests/schemas/` |
| Source identity/admission | source contracts, registry, connectors, admission policy |
| Evidence materialization | `data/proofs/` |
| Receipts | `data/receipts/` |
| Rights/sensitivity/admissibility | `policy/` |
| Release/correction/rollback | `release/` |
| Public runtime outcome | governed application/runtime contracts |
| Public routes | `apps/governed-api/` |
| UI rendering | governed app/UI packages |
| Lifecycle writes | pipelines/tools with explicit ownership and receipts |

### Non-authority statement

```text
citation helper success
  != evidence resolution
  != EvidenceBundle closure
  != citation completeness
  != claim validation
  != rights clearance
  != sensitivity clearance
  != review approval
  != release approval
  != public answer permission
```

[Back to top](#top)

---

## 5. Current source surface

Current verified module tree:

```text
packages/citation/
├── README.md
├── pyproject.toml              # name/version placeholder only
└── src/
    ├── README.md
    └── citation/
        ├── README.md           # this file
        └── __init__.py         # empty
```

This snapshot is bounded to tested paths and indexed search. It is not a recursive Git-tree receipt.

### Current exports

None are established by repository evidence.

### Current dependencies

None are established by `packages/citation/pyproject.toml`.

### Current runtime contract

None is established.

### Current compatibility promise

None is established beyond Git history and this README's boundary. Version `0.0.0` indicates greenfield placeholder status; it must not be interpreted as a published or stable API.

[Back to top](#top)

---

## 6. Core invariants

1. A citation pointer never becomes proof by formatting or normalization.
2. `EvidenceRef.ref` is opaque unless its owning contract explicitly defines canonicalization.
3. The package must not lowercase, trim, rewrite, decode, or re-key canonical refs silently.
4. `kind` must remain one of the schema values: `measurement`, `record`, `dataset`, `artifact`.
5. Absence of `bundle_ref` means pre-closure by default.
6. Presence of `bundle_ref` is a claim of linkage, not proof that the bundle exists or is admissible.
7. Missing, malformed, unresolved, inaccessible, stale, withdrawn, superseded, rights-blocked, or sensitivity-blocked support must remain visible.
8. Structural validity must remain distinct from resolution and closure.
9. Resolution must be explicit and injected; no hidden network or store access.
10. Same input and configuration should yield deterministic output and finding order.
11. Package helpers must not mutate caller inputs.
12. Package helpers must not write lifecycle records as a hidden side effect.
13. Package helpers must not issue PolicyDecisions, ReviewRecords, ReleaseManifests, receipts, or rollback records.
14. Package helpers must not convert a validator/tool failure into a supported citation.
15. Package helpers must preserve source role and limitations when supplied.
16. Restricted details must not be echoed into public-safe exceptions or logs.
17. AI output, embeddings, search ranking, and citation count are not evidence authority.
18. Public consumers receive only governed projections through application/runtime boundaries.
19. Corrections and supersessions create new state; prior refs and outputs remain auditable.
20. A future API change must be reversible and documented.

[Back to top](#top)

---

## 7. Concrete EvidenceRef contract

The strongest current machine contract available to this module is:

```json
{
  "ref": "obs:1",
  "kind": "measurement"
}
```

Optional closure linkage:

```json
{
  "ref": "artifact:release:example",
  "kind": "artifact",
  "bundle_ref": "evidence_bundle:example"
}
```

### Schema-confirmed field behavior

| Field | Required | Shape | Package rule |
|---|---:|---|---|
| `ref` | Yes | string | Treat as opaque canonical pointer; reject non-string structurally. |
| `kind` | Yes | enum | Preserve exact allowed value; do not infer from prefix or target. |
| `bundle_ref` | No | string | Preserve when present; do not claim it resolves without a resolver result. |
| additional fields | No | disallowed | Strict adapters must reject or explicitly quarantine unknown keys. |

### Evidence kind behavior

| `kind` | Package interpretation | Prohibited inference |
|---|---|---|
| `measurement` | Pointer declares measurement/observation-like evidence. | Quality, calibration, rights, or publication readiness. |
| `record` | Pointer declares a record-like evidence item. | Source authority or claim completeness. |
| `dataset` | Pointer declares dataset-level support. | Item-level support for a fine-grained claim. |
| `artifact` | Pointer declares file/output/artifact support. | Canonical truth; generated artifacts remain derived. |

### Validation levels

```text
level 1: shape
  ref/kind/bundle_ref types and enum

level 2: reference syntax/profile
  only if a canonical profile exists for the ref family

level 3: resolution
  target exists and is accessible through governed resolver

level 4: closure
  bundle_ref resolves and the EvidenceBundle covers the claim scope

level 5: admissibility
  rights, sensitivity, review, release, and audience permit use
```

This module may implement levels 1–3 only with explicit scope and dependencies. Levels 4–5 remain owned by evidence/policy/release workflows.

[Back to top](#top)

---

## 8. EvidenceBundle relationship

The current EvidenceBundle schema requires:

- `bundle_id`;
- `claim_scope`;
- at least one `evidence_ref`;
- at least one `source_record`;
- at least one citation string;
- rights with a license;
- sensitivity;
- transforms;
- checksums;
- spec hash.

### Package boundary

This module may:

- preserve an EvidenceBundle identifier;
- validate nested EvidenceRef shapes through canonical schema tooling;
- read an already-loaded EvidenceBundle through a caller-supplied typed adapter;
- select a public-safe projection only after the caller supplies policy/release results;
- verify that expected refs remain present after a package-local transformation;
- return deterministic findings when required fields or links are missing.

This module must not:

- assemble claim-scope closure and call it an EvidenceBundle;
- invent source records or citation strings;
- set rights or sensitivity;
- issue checksums over material it did not govern;
- persist proof material;
- approve bundle closure;
- decide that bundle closure is sufficient for public release.

### Citation strings

The EvidenceBundle schema currently models `citations` as strings. No canonical `Citation` contract or `citation.schema.json` was found at the tested evidence paths.

Therefore:

- citation strings must be treated as opaque unless a separate accepted profile is supplied;
- this package must not invent a structured canonical Citation object and serialize it as repository authority;
- package-local parsed locator types must remain internal or explicitly versioned projections;
- caller-visible structured citation output requires a contract/schema decision.

[Back to top](#top)

---

## 9. CitationValidationReport uncertainty

Two report surfaces are present:

1. evidence-family `CitationValidationReport`;
2. UI-family `CitationValidationReport` projection.

Both paired schemas are permissive scaffolds rather than field-complete contracts.

### Current risk

If this package defines a report class now and treats it as canonical, it could:

- choose the wrong authority family;
- freeze fields before contracts/schemas converge;
- collapse validator findings into UI presentation;
- create incompatible report serialization;
- make package behavior appear more mature than CI and fixtures support.

### Required package posture

- Do not export a canonical `CitationValidationReport` model until authority and schema shape are resolved.
- Internal validation results must use a clearly package-local name such as `CitationCheckResult` only after implementation review.
- Internal results must document that they are not the evidence contract or UI projection.
- Provide adapters only after source and destination schemas are field-complete.
- Never silently map evidence findings to UI-safe messages; policy and redaction must participate.
- Preserve unknown fields only when an explicit compatibility mode is requested and tested.
- Prefer explicit failure over lossy conversion.

### Admission gate for canonical report support

All of the following should exist before this package exports canonical report serialization:

- accepted evidence/UI authority split;
- field-complete schema;
- contract/schema agreement;
- valid and invalid fixtures;
- executable validator;
- package adapter tests;
- public/internal field classification;
- reason-code vocabulary;
- correction and supersession behavior;
- governed API/UI integration tests.

[Back to top](#top)

---

## 10. Proposed module responsibilities

Everything in this section is **PROPOSED**, not current implementation.

### Candidate capability families

| Capability family | Allowed responsibility | Explicit non-goal |
|---|---|---|
| EvidenceRef shape adapter | Validate/construct exact schema-shaped mappings. | Resolve or close evidence. |
| reference preservation | Copy refs without lossy normalization. | Rewrite canonical identity. |
| locator parsing | Parse page/line/fragment syntax under an explicit profile. | Decide source support. |
| limitation preservation | Carry caveats, access state, redaction/generalization labels. | Decide policy. |
| deterministic ordering | Stable sort/group for display or testing under explicit keys. | Rank evidence quality. |
| injected resolution | Call a supplied resolver protocol and return typed resolution state. | Hidden network/store access. |
| safe projection | Build caller-specific citation projection from already-governed input. | Public permission or release approval. |
| compatibility adapter | Translate between explicitly versioned shapes. | Guess missing semantics. |
| validation finding | Return stable package-local codes and field locations. | Canonical CitationValidationReport authority. |
| test builders | Construct synthetic values for package tests. | Production evidence or source records. |

### Candidate module decomposition

```text
citation/
├── __init__.py          # explicit reviewed exports only
├── evidence_ref.py      # strict EvidenceRef shape helpers
├── locators.py          # profile-bound locators; no canonical assumption
├── resolution.py        # injected resolver protocols/results
├── limitations.py       # immutable limitation projections
├── findings.py          # package-local deterministic finding types
├── projections.py       # non-authoritative consumer projections
└── compatibility.py     # explicit versioned migrations
```

This tree is **PROPOSED**. Do not create it wholesale without an implementation PR tied to tests and contracts.

### Keep the module small

A helper belongs here only when at least two governed consumers need it and its behavior can be expressed without acquiring evidence, policy, release, source-admission, or lifecycle authority.

[Back to top](#top)

---

## 11. Proposed API admission rules

No public Python exports currently exist. Before adding one, document:

| Requirement | Required evidence |
|---|---|
| Name | Clear, narrow verb/noun that does not imply evidence authority. |
| Input contract | Canonical schema/contract or explicitly package-local type. |
| Output contract | Canonical schema/contract or explicitly package-local result. |
| Purity | Side effects listed; default should be pure. |
| Determinism | Stable output and finding ordering. |
| Network | Disabled by default; resolver injected explicitly. |
| Error semantics | Stable package-local findings/exceptions; no hidden fallback. |
| Sensitivity | Public-safe messages separated from internal details. |
| Versioning | Compatibility and deprecation plan. |
| Tests | Positive, negative, property, and boundary tests. |
| Consumer | At least one verified consumer or justified shared need. |
| Rollback | Revert or feature-disable path. |

### Candidate export names

These names are illustrative only:

```python
parse_evidence_ref(...)
validate_evidence_ref_shape(...)
preserve_evidence_refs(...)
resolve_evidence_ref(...)
project_citation_for_surface(...)
```

They are not current API and must not be added solely because they appear in this README.

### Avoid authority-signaling names

Avoid exports such as:

```text
prove_claim
approve_citation
close_evidence
admit_source
release_citation
make_public
verify_truth
safe_to_publish
```

Those names imply responsibilities owned elsewhere.

[Back to top](#top)

---

## 12. Reference normalization rules

### Preserve identity

Normalization may improve representation only when the contract/profile says the representations are equivalent.

Default rules:

- do not trim `ref` unless the schema/profile explicitly allows surrounding whitespace;
- do not lowercase refs;
- do not Unicode-normalize opaque IDs unless a canonical identity profile requires it;
- do not URL-decode or encode refs implicitly;
- do not remove fragments;
- do not rewrite source-specific prefixes;
- do not infer `kind` from `ref`;
- do not add `bundle_ref` based on proximity or naming;
- do not deduplicate refs whose equality has not been established.

### Deterministic comparison

If callers need deduplication, require an explicit key function or accepted canonicalization profile.

```text
raw string equality                 = allowed default
schema-profile canonical equality  = allowed when profile is supplied
semantic source equivalence        = not package authority
claim-support equivalence          = not package authority
```

### Locator handling

Page, line, fragment, anchor, timestamp, geometry, or byte-range locators should be:

- profile-qualified;
- immutable;
- optional unless the citation contract requires them;
- validated without silently clamping out-of-range values;
- preserved through projections;
- excluded from public output when policy marks them sensitive;
- never treated as proof of claim relevance by location alone.

[Back to top](#top)

---

## 13. Resolution and I/O boundary

### Default: no I/O

Package helpers should operate on values already supplied by the caller.

### Explicit resolver injection

A future resolver interface should make I/O visible:

```text
caller
  -> constructs governed resolver with allowed stores/audience
  -> passes resolver explicitly
  -> package requests resolution
  -> resolver returns bounded state
  -> package returns result without writing lifecycle state
```

### Proposed resolution states

Package-local states may include:

```text
RESOLVED
NOT_FOUND
INACCESSIBLE
WITHHELD
STALE
SUPERSEDED
MALFORMED
ERROR
```

These are not runtime `ANSWER | ABSTAIN | DENY | ERROR` outcomes. The governed caller maps package findings through policy/runtime contracts.

### Resolver rules

- Resolver scope and audience must be explicit.
- Resolver must not fall through from governed stores to arbitrary network access.
- Missing access is not missing evidence; distinguish `INACCESSIBLE` from `NOT_FOUND`.
- Withheld details must not be returned in exceptions.
- Resolution must return identity/version/freshness information where material.
- Cache keys must include authority-relevant inputs.
- Cache invalidation must respond to correction, withdrawal, rights, sensitivity, and release changes.
- Package code must not persist resolved evidence.
- Resolver errors must not be converted into successful placeholder citations.

[Back to top](#top)

---

## 14. Findings, errors, and runtime outcomes

### Three different vocabularies

| Layer | Example vocabulary | Owner |
|---|---|---|
| Package finding | `INVALID_EVIDENCE_REF`, `UNRESOLVED_REF`, `INACCESSIBLE_REF` | This package, after implementation review |
| Validator/report outcome | PASS, FAIL, WARN, HOLD, DENY, ABSTAIN, ERROR, NEEDS_VERIFICATION | Citation validation contract/tooling; final schema unresolved |
| Runtime outcome | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` | Governed runtime response contracts |

Do not collapse them.

### Proposed package finding codes

```text
INVALID_EVIDENCE_REF
UNKNOWN_EVIDENCE_KIND
UNKNOWN_FIELD
MISSING_BUNDLE_REF
BUNDLE_REF_UNRESOLVED
REF_NOT_FOUND
REF_INACCESSIBLE
REF_WITHHELD
REF_STALE
REF_SUPERSEDED
LOCATOR_MALFORMED
LOCATOR_OUT_OF_SCOPE
LIMITATION_DROPPED
NONDETERMINISTIC_ORDER
CANONICAL_REPORT_SHAPE_UNRESOLVED
RESOLVER_ERROR
```

### Mapping rule

The package returns facts/findings. The caller applies evidence, policy, audience, and runtime rules.

Example:

```text
package finding: REF_INACCESSIBLE
policy: public audience cannot access restricted evidence
runtime: DENY

package finding: REF_NOT_FOUND
evidence support required for answer
runtime: ABSTAIN

package finding: RESOLVER_ERROR
runtime: ERROR
```

Mappings are contextual; they must not be hard-coded as universal package truth.

### Exceptions

Exceptions should be reserved for programming/integrity failures. Expected invalid inputs should normally produce deterministic validation findings when the API is designed for batch validation.

[Back to top](#top)

---

## 15. Source role, rights, sensitivity, and limitations

The package may preserve these fields or references when supplied, but it does not assign them.

### Source role

Preserve role labels exactly. Do not infer authority from:

- government domain;
- publication venue;
- file format;
- citation frequency;
- model confidence;
- map visibility;
- prior use;
- package validation success.

### Rights

The package must not infer permission from accessibility.

Preserve:

- license/terms reference;
- attribution requirement;
- redistribution/export constraints;
- embargo;
- derivative restrictions;
- access audience;
- unresolved rights state.

### Sensitivity

Do not embed restricted details in package errors, reprs, logs, snapshots, or fixtures.

Preserve:

- sensitivity label/ref;
- redaction/generalization state;
- exact-location withholding;
- audience restriction;
- review requirement;
- transform/receipt refs where supplied.

### Limitations

A citation projection must not drop:

- claim scope limits;
- temporal limits;
- spatial support;
- source caveats;
- model/observation character;
- stale state;
- inaccessible/withheld state;
- correction/supersession state;
- release limitation.

A shorter display projection may summarize limitations only if the full governed state remains inspectable through an allowed reference.

[Back to top](#top)

---

## 16. Temporal, correction, and supersession behavior

References and citations are time-aware even when the current EvidenceRef schema has no timestamp fields.

Temporal state may live in the referenced source, bundle, release, or correction records.

Package behavior should:

- avoid presenting a resolved target as current without freshness context;
- distinguish source time, observation time, retrieval time, release time, and correction time where supplied;
- preserve versioned identifiers;
- preserve supersession links;
- mark prior projections stale when their refs or bundles are corrected;
- avoid mutating historical citation outputs;
- create new projections/results after correction;
- support deterministic invalidation keys.

### Correction trigger examples

- source record withdrawn;
- EvidenceRef target changed or disappeared;
- EvidenceBundle superseded;
- rights terms changed;
- sensitivity increased;
- public geometry re-generalized;
- citation locator corrected;
- report schema changed;
- release withdrawn or rolled back.

This package can expose invalidation information. Release/correction workflows decide operational action.

[Back to top](#top)

---

## 17. Consumer and trust-membrane contract

### Allowed consumers

Potential consumers include:

- governed API adapters;
- evidence/citation validators;
- pipelines carrying canonical refs;
- report builders;
- Evidence Drawer projection adapters;
- tests and documentation checkers.

### Consumer obligations

A consumer must:

- identify the contract/schema version it expects;
- supply policy/release state when building public projections;
- map package findings to governed runtime outcomes;
- preserve negative states;
- avoid direct public access to internal evidence/source stores;
- enforce audience and sensitivity;
- keep package internals out of browser/public trust decisions;
- record receipts in accepted roots when the operation requires them.

### Public path

```text
canonical evidence / proof / source records
  -> governed resolver
  -> evidence and citation validation
  -> policy + review + release
  -> governed API/runtime envelope
  -> UI / export / AI projection
```

Not:

```text
browser or public caller
  -> imports package helper
  -> reads proof/source store
  -> decides support
```

### Generated AI text

The package may preserve citations attached to generated text. It must not validate the generated statement as supported merely because one or more refs are present.

[Back to top](#top)

---

## 18. Directory and file contract

### Correct ownership

```text
packages/citation/src/citation/   package helper implementation
contracts/evidence/               evidence/citation semantics
schemas/contracts/v1/evidence/    machine shape
fixtures/contracts/v1/evidence/   contract fixture examples
tools/validators/citation/        citation validation orchestration
tests/schemas/                    schema/fixture conformance
tests/packages/citation/          package behavior tests, when created
policy/evidence/                  admissibility/sensitivity policy
data/proofs/                      materialized proof
data/receipts/                    receipts
release/                          publication/correction/rollback
apps/governed-api/                public trust membrane
```

### Files that may eventually belong here

- Python implementation modules;
- package-local type definitions;
- package-local exceptions/findings;
- internal compatibility adapters;
- generated Python types only when generation source/hash is recorded and generated-file policy is accepted.

### Files that do not belong here

- JSON Schemas;
- semantic contract Markdown;
- real EvidenceBundle instances;
- source records;
- policy bundles;
- receipts;
- proof packs;
- release manifests;
- public API route implementations;
- UI components;
- production fixtures;
- generated QA reports;
- secrets or credentials.

### Generated types

Generated code must record:

- source schema path and digest;
- generator/version;
- generation command;
- generated-file marker;
- reproducibility test;
- drift check;
- rollback path.

Do not hand-edit generated types.

[Back to top](#top)

---

## 19. Tests and fixtures

No dedicated package suite was observed. The matrix below is the minimum proposed admission set.

### Unit tests

| Test family | What it proves |
|---|---|
| strict EvidenceRef shape | Required fields, enum, no extras. |
| opaque ref preservation | No silent trim/casefold/decode/rewrite. |
| input immutability | Caller mappings are unchanged. |
| deterministic findings | Same input/config yields stable findings/order. |
| optional bundle ref | Absence remains pre-closure; presence is preserved without assumed resolution. |
| injected resolver | No hidden I/O; resolver states remain distinct. |
| inaccessible vs missing | No collapse between access denial and absent target. |
| limitation preservation | Caveats and restricted states survive projection. |
| safe error messages | No sensitive details leaked. |
| correction/supersession | Stale/superseded refs are visible and invalidate projections. |
| no authority acquisition | Helpers do not emit PolicyDecision, ReleaseManifest, EvidenceBundle, or receipt instances. |
| report-shape guard | Canonical CitationValidationReport serialization remains blocked while schema is permissive. |

### Contract/schema tests

Use the existing common schema harness for canonical schema fixtures.

Current EvidenceRef fixture coverage is minimal:

```text
valid:
  ref + kind

invalid:
  kind only, missing ref
```

Recommended additions at the schema fixture layer—not package-local copies—include:

- each valid `kind`;
- valid optional `bundle_ref`;
- invalid unknown `kind`;
- invalid additional property;
- invalid non-string `ref`;
- invalid non-string `bundle_ref`;
- invalid empty-string policy, if the contract later forbids empty values.

### Package fixtures

If package fixtures are added, use synthetic values and keep them separate from canonical contract fixtures.

Proposed home:

```text
fixtures/packages/citation/
```

This path must be confirmed against package/test conventions before creation.

### No-network requirement

Default tests must not contact:

- source websites;
- proof stores;
- registries;
- databases;
- model runtimes;
- tile services;
- external resolvers.

Use injected fakes with explicit states.

[Back to top](#top)

---

## 20. Validation commands

These commands are grounded in currently verified files where noted. They were not run in this connector-only documentation update.

### Existing schema fixture harness

```bash
python -m pytest tests/schemas/test_common_contracts.py
```

This includes the `evidence` family and will discover the EvidenceRef fixture family.

### Existing EvidenceBundle wrapper

```bash
python tools/validators/validate_evidence_bundle.py
```

### Missing dedicated EvidenceRef wrapper

The schema declares:

```text
tools/validators/validate_evidence_ref.py
```

That file was not found at the tested commit. Do not document it as runnable until added and verified.

### Package import smoke after implementation

PROPOSED:

```bash
python -c "import citation; print(citation.__all__)"
```

This will not provide meaningful evidence until exports and packaging are implemented.

### Structural inspection

```bash
find packages/citation -maxdepth 5 -type f -print | sort
git grep -nE 'kfm-citation|from citation|import citation'
```

### Documentation checks

```bash
grep -c '^# ' packages/citation/src/citation/README.md
python - <<'PY'
from pathlib import Path
p = Path("packages/citation/src/citation/README.md")
text = p.read_text(encoding="utf-8")
assert text.count(chr(96) * 3) % 2 == 0
print("README fence check passed")
PY
```

[Back to top](#top)

---

## 21. Safe change and compatibility discipline

### Smallest useful implementation sequence

1. Strengthen `pyproject.toml` with build backend, Python requirement, package discovery, and test dependencies.
2. Add package-specific test/fixture homes or document accepted alternatives.
3. Implement strict EvidenceRef shape helpers only.
4. Add opaque-identity and no-hidden-I/O tests.
5. Add explicit package exports.
6. Add one verified consumer.
7. Add CI that runs real tests instead of echo stubs.
8. Add resolver protocol only after store/audience boundaries are defined.
9. Add citation projection only after canonical shape/authority is settled.
10. Add compatibility adapters only with versioned source/destination schemas.

### Versioning

Version `0.0.0` is not a compatibility guarantee.

Before the first non-placeholder release, define:

- semantic versioning policy;
- supported Python versions;
- public versus internal exports;
- deprecation window;
- changelog;
- package distribution method;
- schema compatibility matrix;
- migration and rollback strategy.

### Breaking changes

A change is breaking when it alters:

- exported names;
- accepted/refused input shapes;
- finding codes;
- exception types;
- normalization behavior;
- ordering;
- resolver protocol;
- projection fields;
- sensitivity/error redaction behavior.

Breaking changes require explicit migration notes and consumer tests.

### Rollback

Documentation-only rollback: revert the README commit.

Implementation rollback should support:

- revert to prior package commit/version;
- disable new export/adapter;
- restore prior consumer mapping;
- invalidate cached projections;
- preserve prior evidence/release history;
- avoid rewriting refs or proof records.

[Back to top](#top)

---

## 22. Security and data minimization

### Untrusted inputs

Treat citation strings, refs, locators, source labels, and resolver responses as untrusted.

Defend against:

- path traversal;
- URL scheme abuse;
- control characters;
- log injection;
- oversized values;
- recursive/deep payloads;
- Unicode confusables;
- malicious fragments;
- SSRF through automatic dereference;
- disclosure through exception text.

### No automatic URL fetch

A string that looks like a URL must remain a string unless a governed resolver explicitly handles it.

### Sensitive refs

Refs themselves may reveal:

- species or site identity;
- private source IDs;
- internal object paths;
- embargoed document identifiers;
- precise location hints;
- access-control structure.

Public projections may require opaque aliases or redaction. That decision belongs to policy/runtime, not this package alone.

### Serialization

- Avoid serializing Python reprs of internal resolver objects.
- Use bounded field lengths where contracts permit.
- Separate internal diagnostics from public messages.
- Never include credentials, bearer tokens, signed URLs, or private keys.
- Avoid persisting caller payloads in package logs.

[Back to top](#top)

---

## 23. Observability and receipts

This package should not emit governance receipts by default.

Package-level observability may include:

- operation name;
- package version;
- contract/schema version;
- count of refs processed;
- count by bounded finding code;
- duration;
- resolver identifier/version, if supplied;
- deterministic input spec hash when safe and governed.

It must not include raw sensitive refs in broad logs.

When a pipeline, validator, governed API, review, or release operation requires a receipt, the owning executable surface emits it to the accepted receipt root and may include package version/hash as implementation provenance.

### Suggested metrics

PROPOSED:

```text
citation_refs_validated_total
citation_refs_invalid_total
citation_refs_unresolved_total
citation_refs_inaccessible_total
citation_refs_stale_total
citation_resolver_errors_total
citation_projection_blocked_total
citation_limitations_preserved_total
```

Metrics must not become evidence-quality scores.

[Back to top](#top)

---

## 24. Definition of done

### This README revision

- [x] Records the current Python placeholder state.
- [x] Records the empty module implementation.
- [x] Records missing package tests/fixtures and unobserved consumers.
- [x] Anchors future behavior to the concrete EvidenceRef schema.
- [x] Separates EvidenceRef, EvidenceBundle, validation report, policy, release, and runtime authority.
- [x] Documents the unresolved evidence/UI CitationValidationReport split.
- [x] Identifies the TODO workflow as a scaffold rather than CI proof.
- [x] Defines deterministic, no-network, side-effect-minimal expectations.
- [x] Defines security, correction, versioning, and rollback posture.
- [x] Avoids claiming functions or exports exist.

### First implementation milestone

- [ ] `pyproject.toml` is a valid installable project configuration.
- [ ] Supported Python versions and dependencies are pinned.
- [ ] Public/internal export policy is documented.
- [ ] Strict EvidenceRef helpers exist.
- [ ] Tests cover all schema enum/extra-field cases and opaque identity.
- [ ] No-network resolver tests exist.
- [ ] Package-specific CI runs real tests.
- [ ] One governed consumer is verified.
- [ ] Package version is no longer placeholder-only.
- [ ] Rollback is tested.

### Production-ready milestone

- [ ] Canonical Citation shape or explicit string-only posture is accepted.
- [ ] CitationValidationReport authority/schema split is resolved.
- [ ] Resolver/store/audience contract is accepted.
- [ ] Rights and sensitivity integration is tested.
- [ ] Correction/supersession invalidation is tested.
- [ ] Public-safe projection is schema/contract/policy aligned.
- [ ] CI is required and passing.
- [ ] Package ownership and CODEOWNERS are established.
- [ ] Release artifact and provenance are auditable.

[Back to top](#top)

---

## 25. Open verification register

| ID | Question | Status | Evidence needed |
|---|---|---|---|
| `PKG-CIT-SRC-001` | Is Python the accepted long-term implementation language for this package? | NEEDS VERIFICATION | Architecture/package decision and consumers. |
| `PKG-CIT-SRC-002` | What is the accepted build backend and package discovery configuration? | UNKNOWN | Completed `pyproject.toml` and install test. |
| `PKG-CIT-SRC-003` | Which names are public exports versus internal helpers? | UNKNOWN | Implementation and API review. |
| `PKG-CIT-SRC-004` | Is there a canonical structured `Citation` object, or do citations remain strings? | UNKNOWN | Contract/schema/ADR decision. |
| `PKG-CIT-SRC-005` | Which CitationValidationReport family is canonical? | CONFLICTED / NEEDS VERIFICATION | Evidence/UI contract and schema resolution. |
| `PKG-CIT-SRC-006` | What package-local finding vocabulary is accepted? | PROPOSED | Contracts/tooling/runtime crosswalk and tests. |
| `PKG-CIT-SRC-007` | Which resolver protocol and stores are allowed? | UNKNOWN | Resolver architecture, access policy, threat model. |
| `PKG-CIT-SRC-008` | May the package depend directly on `jsonschema`, or consume generated validators/types? | UNKNOWN | Dependency and architecture decision. |
| `PKG-CIT-SRC-009` | Should the missing EvidenceRef validator wrapper be added? | NEEDS VERIFICATION | Validator/tooling owner decision and CI need. |
| `PKG-CIT-SRC-010` | Where should package-specific fixtures live? | NEEDS VERIFICATION | Tests/fixtures convention and Directory Rules check. |
| `PKG-CIT-SRC-011` | Which verified consumers need this shared package? | UNKNOWN | Import inventory and integration PR. |
| `PKG-CIT-SRC-012` | How are refs cached and invalidated after correction/withdrawal? | UNKNOWN | Runtime resolver/cache design and tests. |
| `PKG-CIT-SRC-013` | Which citation details are safe for public versus steward surfaces? | UNKNOWN | Policy, UI projection, and security review. |
| `PKG-CIT-SRC-014` | What CI workflow should replace the echo-TODO scaffold? | NEEDS VERIFICATION | Real package tests and workflow design. |
| `PKG-CIT-SRC-015` | What release/distribution channel publishes `kfm-citation`, if any? | UNKNOWN | Package/release plan. |
| `PKG-CIT-SRC-016` | Who owns package review? | UNKNOWN | CODEOWNERS/team assignment. |

[Back to top](#top)

---

## 26. Evidence ledger

| Evidence | Blob / ref | Supports | Limitation |
|---|---|---|---|
| Target README v0.1 | `179edc9ea66168f19ac0f4c566125c773be54c32` | Prior planning boundary and source-module intent. | Overstated expected modules relative to actual placeholder state. |
| Parent package README | `8516033ca7b7f7458cfc0f09438853bd3ac3753e` | Citation package boundary and non-authority posture. | Concrete implementation remains unverified. |
| Source-root README | `90afd88e87fe07457606a01b67d838856a0ff504` | Source-root and child module relationship. | Proposed future tree is not implementation. |
| Package metadata | `7037b7f228294cd5cca2b85d5472fe8b62d8b15d` | Python project name/version placeholder. | No build backend, dependencies, or package config. |
| `citation/__init__.py` | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` | Module exists but is empty. | No exports or behavior. |
| EvidenceRef contract | `0f337cf07d44224c31329c8eced90d4dddccef87` | Governed-pointer meaning and closure boundary. | Runtime/validator wiring remains unverified. |
| EvidenceRef schema | `42f499df613a9d68e5ca6fc5ec75ff8058c155b9` | Concrete required fields, enum, optional bundle ref, no extras. | Schema status is PROPOSED. |
| EvidenceRef fixture README | `e1ba203007f806b3c9b43ca5c19fa323c546fb61` | Current valid/invalid fixture inventory and missing validator wrapper. | Minimal fixture coverage; tests not run here. |
| Common schema test | `b04342cc034d7f1cc554e155fdd02d6e972976e6` | Schema/fixture discovery and valid/invalid behavior. | Does not test package helpers. |
| EvidenceBundle schema | `cf5256831b63dca46a5f68b168441adcf68b8751` | Concrete bundle fields and nested EvidenceRefs. | Schema status is PROPOSED. |
| EvidenceBundle validator | `c1760c5e92eae6390f5adcde4593e8e9bab26535` | Runnable wrapper path and schema/fixture roots. | Does not validate package behavior. |
| Evidence CitationValidationReport contract | `36cdb2bab1e47479b816950d907868c4e4689283` | Evidence-report semantics and non-authority boundary. | Paired schema is permissive. |
| Evidence report schema | `3cdb7dca322a1a5049afc1e60b89120fbfa1cd90` | Confirms no fields are enforced. | Cannot support canonical package model. |
| UI CitationValidationReport contract | `b5c399d0fcb05fe21205d9488f24b44d1962d011` | Downstream UI projection and evidence/UI split. | Final authority split unresolved. |
| Citation validator README | `574848fac4394a618b5e3132705c903ad5846fcd` | Proposed validator responsibility and boundary. | No executable proven. |
| Citation workflow | `644e60c968c8ad712ed5228d6bcaf1a4d1d9db38` | Workflow name/triggers and TODO jobs. | Echo-only; no real validation. |
| Citation Guidance | `073bc7348903b550c98f6fa5674bd1c7378dfc0e` | Cite-or-abstain doctrine and visible evidence-chain posture. | Some path/field claims are planning-era and require repo reconciliation. |
| Directory Rules | `2affb080e6f0043867c64c7f06c1ca52030fbd55` | `packages/` shared-library placement and authority separation. | Specific package implementation still requires repo evidence. |
| CODEOWNERS | `6adabefcbe58b9d281f105dbabaea451aa165619` | Generic maintainers own unmatched package paths. | No package-specific steward rule. |
| Detailed evidence snapshot | `b04e9b4a576557ec8cf2f48f6cbe45fd07fbec7a` | Commit-pinned package/evidence inspection. | No runtime logs, package install, or tests executed. |
| Review-branch base | `b24b455b7b749203edbfa06557baa8209c3080f6` | Target blob rechecked unchanged; intervening commits changed only `configs/domains/fauna/README.md`. | Does not add runtime evidence. |

### Truth summary

```text
CONFIRMED:
  Python placeholder package exists
  version is 0.0.0
  citation module init is empty
  EvidenceRef schema is concrete
  EvidenceRef fixture family and common schema harness exist
  dedicated EvidenceRef validator wrapper is absent
  EvidenceBundle schema and wrapper exist
  CitationValidationReport schemas are scaffolds
  citation workflow is echo-only

PROPOSED:
  module responsibilities
  candidate API and file split
  package finding codes
  test matrix and implementation sequence
  metrics

UNKNOWN:
  consumers
  production resolver
  public integration
  package distribution
  canonical Citation shape
  canonical CitationValidationReport family
  CI enforcement
```

[Back to top](#top)

---

## 27. Maintainer checklist

Before adding or changing code here:

- [ ] Read the parent package and source-root READMEs.
- [ ] Confirm the helper is shared by more than one governed consumer.
- [ ] Identify the canonical contract and schema.
- [ ] Do not invent a canonical Citation object while no schema/contract is accepted.
- [ ] Treat `ref` as opaque unless an accepted profile says otherwise.
- [ ] Keep `kind` schema-aligned.
- [ ] Preserve optional `bundle_ref` without assuming resolution.
- [ ] Separate shape validation, resolution, closure, policy, and release.
- [ ] Keep network/store access explicitly injected.
- [ ] Preserve inaccessible, withheld, stale, corrected, and superseded states.
- [ ] Use package-local findings, not runtime outcomes, inside the helper layer.
- [ ] Avoid logging raw sensitive refs.
- [ ] Add deterministic positive and negative tests.
- [ ] Use synthetic, no-network fixtures.
- [ ] Update `pyproject.toml` when dependencies or Python support change.
- [ ] Add a verified consumer and integration test.
- [ ] Replace TODO workflow checks with real commands before claiming CI.
- [ ] Record compatibility and rollback.
- [ ] Keep public callers behind governed API/runtime envelopes.
- [ ] Mark unverified claims as `UNKNOWN` or `NEEDS VERIFICATION`.

## Status summary

`packages/citation/src/citation/` is currently an **empty Python implementation placeholder** with a strong governance boundary but no established helper API.

The next sound change is not a broad citation framework. It is a small, tested, deterministic EvidenceRef helper slice grounded in the existing strict schema, with no hidden I/O and no authority beyond package-local validation/preservation.

<p align="right"><a href="#top">Back to top</a></p>
