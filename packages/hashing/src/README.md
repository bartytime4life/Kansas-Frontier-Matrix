<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-hashing-src-readme
title: packages/hashing/src/ — Hashing Source Envelope and Implementation Placement Boundary
type: readme
version: v1.1
status: draft
owners: OWNER_TBD — Package steward · Integrity/canonicalization steward · Contract steward · Schema steward · Security steward · Validation steward · Migration steward · CI steward · Docs steward
created: NEEDS VERIFICATION — target existed before the current evidence-grounded revision
updated: 2026-07-15
policy_label: "public-doctrine; package-source-boundary; hashing; implementation-empty; api-unratified; canonicalization-conflicted; spec-hash-shape-conflicted; tools-package-ownership-conflicted; no-network; pure-functions; fail-closed; no-authority; no-secrets; migration-required; rollback-aware"
current_path: packages/hashing/src/README.md
truth_posture: CONFIRMED target README, merged child namespace README v1.1, empty hashing package initializer, kfm-hashing 0.0.0 placeholder metadata, package/root READMEs, Directory Rules package placement, draft identity and canonicalization doctrine, draft common spec_hash contract and schema, schema fixtures and generic schema test harness, placeholder dedicated validator, README-only tools/spec_hash lane, generated-receipt digest vocabulary, and bounded absence of proposed implementation modules and package-specific test/workflow paths / PROPOSED source-envelope rules, import direction, pure-library placement, dependency controls, package-tool-validator delegation, typed result families, resource limits, staged implementation, tests, correction, migration, deprecation, and rollback / CONFLICTED jcs:sha256 string doctrine versus object-wrapped sha256 schema and contract, packages/hashing versus tools/spec_hash implementation ownership, canonicalization-profile representation, SHA-256 authority baseline versus BLAKE3-permitted provenance/content fields, and documentation richness versus empty implementation / UNKNOWN accepted Python runtime, build backend, dependency set, pinned JCS implementation, export surface, consumer inventory, installability, runtime behavior, cross-language parity, package-specific tests, CI enforcement, release use, and operational health / NEEDS VERIFICATION owners, ADR or migration decision, canonical hash vocabulary, schema/contract reconciliation, package ownership, dependencies, source layout, API shape, resource limits, test vectors, consumer migration, CI gates, correction path, compatibility period, deprecation, and rollback automation
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 2ad80d6362541db0d1933fe729e9a552f7aa19a9
  prior_blob: 309afb28791d0f1136358b79f690ee99786a7ae8
  package_readme_blob: c9440697c02f71a8c83f0293d72364bb89930c01
  namespace_readme_blob: 05a1320e395ad3b1e64ff72f16c844a5e43c3441
  package_metadata_blob: 94a3799821298b4e99ea7bc638d8ab3c4bd7eea2
  namespace_initializer_blob: e69de29bb2d1d6434b8b29ae775ad8c2e48c5391
  packages_root_blob: fc18fb3334fefe992a551fe12aa98c812232cd17
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  identity_architecture_blob: d8b3836bae160ac0f2027407989d383fa016a49b
  canonicalization_standard_blob: 393a4450f64993c26b20d727656a1e6b6494db4e
  spec_hash_contract_blob: 0c2c1161ddb565d4f9f17ef81080b27b8d951937
  spec_hash_schema_blob: 80b496b01b8de8c0e8ba67bf020977e6b1f3c652
  spec_hash_fixture_readme_blob: bc787595d5869c7bd212b0c7909c3eb0b980daf9
  common_contract_test_blob: b04342cc034d7f1cc554e155fdd02d6e972976e6
  spec_hash_validator_blob: de69c6c7001082af29827a4b287a80b7c6a05af3
  tools_spec_hash_readme_blob: 69beb3e00d0c9c59e42348a918da0d11faa82850
  generated_receipt_schema_blob: fba21ed27ebccf1362fe397fe0c3ebd85e072685
  evidence_bundle_schema_blob: cf5256831b63dca46a5f68b168441adcf68b8751
  bounded_path_checks:
    - packages/hashing/src/README.md existed at version v1 before this revision
    - packages/hashing/src/hashing/README.md exists at version v1.1
    - packages/hashing/src/hashing/__init__.py exists and is empty
    - packages/hashing/pyproject.toml contains only project name kfm-hashing and version 0.0.0
    - packages/hashing/package.json was not found
    - packages/hashing/src/hashing.py was not found
    - canonical_json.py, digests.py, spec_hash.py, content_hash.py, geometry_hash.py, merkle.py, run_id.py, compare.py, and fixtures.py were not found under packages/hashing/src/hashing/
    - packages/hashing/tests/README.md and tests/packages/hashing/README.md were not found
    - .github/workflows/hashing.yml, package-hashing.yml, and spec-hash.yml were not found
    - tools/spec_hash/jcs_hash.py and tools/spec_hash/spec_hash.py were not found
    - tools/validators/validate_spec_hash.py raises NotImplementedError
related:
  - ../README.md
  - hashing/README.md
  - hashing/__init__.py
  - ../pyproject.toml
  - ../../README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/architecture/identity-and-spec-hash.md
  - ../../../docs/standards/CANONICALIZATION.md
  - ../../../contracts/common/spec_hash.md
  - ../../../schemas/contracts/v1/common/spec_hash.schema.json
  - ../../../schemas/contracts/v1/evidence/evidence_bundle.schema.json
  - ../../../schemas/contracts/v1/receipts/generated_receipt.schema.json
  - ../../../fixtures/contracts/v1/common/spec_hash/README.md
  - ../../../tests/schemas/test_common_contracts.py
  - ../../../tools/validators/validate_spec_hash.py
  - ../../../tools/spec_hash/README.md
  - ../../../contracts/
  - ../../../schemas/
  - ../../../policy/
  - ../../../data/receipts/
  - ../../../data/proofs/
  - ../../../release/
tags: [kfm, packages, hashing, src, deterministic-identity, canonicalization, jcs, urdna2015, sha256, blake3, spec-hash, content-hash, geometry-hash, artifact-hash, merkle-root, run-id, replay, compatibility, migration, fail-closed]
notes:
  - "This revision changes only packages/hashing/src/README.md."
  - "The source envelope currently contains this README and the hashing/ child namespace; that namespace contains its README and an empty __init__.py."
  - "This README does not activate an API, select a canonical spec_hash representation, ratify a package/tool implementation owner, or claim installability."
  - "The current docs and machine contracts disagree about spec_hash representation; source code must not silently translate between them."
  - "Hash equality is integrity evidence about declared bytes/profile only. It is not truth, evidence closure, policy approval, release approval, or public safety."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hashing Source Envelope and Implementation Placement Boundary

`packages/hashing/src/`

> Repository-present source envelope for a future reusable deterministic hashing library. Current evidence establishes documentation and an empty import initializer—not a functioning canonicalizer, digest implementation, exported API, tested package, or CI-enforced integrity subsystem.

![status](https://img.shields.io/badge/status-draft-yellow)
![version](https://img.shields.io/badge/version-v1.1-informational)
![maturity](https://img.shields.io/badge/maturity-source__scaffold-lightgrey)
![canonicalization](https://img.shields.io/badge/canonicalization-CONFLICTED-orange)
![ownership](https://img.shields.io/badge/ownership-CONFLICTED-orange)
![network](https://img.shields.io/badge/network-none-critical)
![authority](https://img.shields.io/badge/truth__authority-none-red)
![behavior](https://img.shields.io/badge/behavior-fail__closed-blue)

**Quick links:** [Purpose](#purpose) · [Evidence](#status-and-evidence) · [Placement](#directory-rules-and-authority) · [Responsibilities](#source-envelope-responsibilities) · [Conflicts](#compatibility-conflicts) · [Tree](#confirmed-and-proposed-source-tree) · [Invariants](#keystone-invariants) · [Imports](#import-and-dependency-direction) · [Canonicalization](#canonicalization-and-hash-boundary) · [Delegation](#package-tool-validator-and-caller-delegation) · [Outcomes](#expected-result-families) · [Security](#security-and-resource-bounds) · [Testing](#testing-fixtures-and-ci) · [Implementation](#smallest-sound-implementation-sequence) · [Done](#definition-of-done) · [Open](#verification-register) · [Rollback](#rollback-correction-deprecation-and-migration)

> [!IMPORTANT]
> **This README is not an implementation, API, dependency, or migration decision.** It does not establish exports, a pinned JCS library, supported canonicalization profiles, a canonical `spec_hash` shape, package ownership over `tools/spec_hash/`, CI enforcement, or operational consumers.

> [!CAUTION]
> **A matching digest is not a truth decision.** It establishes only that declared inputs produce the same digest under the same declared algorithm and canonicalization profile. Schema validity, semantic correctness, provenance, evidence sufficiency, rights, sensitivity, policy, review, release, and public safety remain separate gates.

---

<a id="purpose"></a>

## Purpose

This README defines the allowed responsibility boundary for source code under `packages/hashing/src/`.

The source envelope may eventually contain one reusable, deterministic implementation used by governed callers for:

- canonical byte production under accepted versioned profiles;
- byte and canonical-content digest computation;
- digest-reference parsing and formatting;
- stored-versus-recomputed comparison;
- deterministic file-set roots from explicit entries;
- deterministic run identifiers from explicit run context;
- replay and parity checks;
- stable typed results and reason codes.

The source envelope must not become:

- a second schema, contract, canonicalization-standard, or policy home;
- a receipt, proof, EvidenceBundle, release, rollback, or lifecycle-data store;
- a source connector or pipeline orchestrator;
- a public API, UI, map, or AI answer surface;
- signing, HMAC, encryption, password-hashing, key-management, or secret-storage authority;
- a compatibility shortcut that silently converts conflicting hash representations;
- an ambient filesystem scanner or network client.

The child namespace README governs proposed import behavior. This parent README governs source placement, import direction, dependency boundaries, implementation delegation, and conditions for adding code.

[Back to top](#top)

---

<a id="status-and-evidence"></a>

## Status and evidence

| Surface | Status | Safe conclusion |
|---|---:|---|
| This README | **CONFIRMED v1 before revision** | A source-envelope guide exists. |
| Child `hashing/README.md` | **CONFIRMED v1.1** | The import namespace has an evidence-grounded compatibility boundary. |
| `hashing/__init__.py` | **CONFIRMED empty** | No exports, import behavior, or side effects are established. |
| `kfm-hashing` metadata | **CONFIRMED `0.0.0` placeholder** | Package name exists; build backend, dependencies, package discovery, and installability are not established. |
| Proposed implementation modules | **NOT FOUND at bounded paths** | No canonicalizer, digest, comparison, Merkle, geometry, run-id, or fixture implementation is established. |
| Package-specific tests | **NOT FOUND at checked README paths** | No dedicated hashing test boundary is established. |
| Package-specific workflows | **NOT FOUND at checked paths** | No dedicated hashing CI behavior is established. |
| Identity architecture | **CONFIRMED draft doctrine** | States JCS + SHA-256 and recompute-on-gate behavior. |
| Canonicalization standard | **CONFIRMED draft standard** | JCS default; URDNA2015 reserved; pinned implementation remains unresolved. |
| Common `spec_hash` contract/schema | **CONFIRMED draft/PROPOSED machine surface** | Requires an object with `value: sha256:<hex>`. |
| `spec_hash` fixtures | **CONFIRMED minimal schema fixtures** | Test shape acceptance/rejection only. |
| Generic contract test harness | **CONFIRMED executable test code** | Discovers and validates JSON Schema fixtures; it does not compute hashes. |
| Dedicated `spec_hash` validator | **CONFIRMED placeholder** | Raises `NotImplementedError`. |
| `tools/spec_hash/` | **CONFIRMED README-only lane at checked executable paths** | Tool-versus-package implementation ownership remains unresolved. |
| Generated-receipt digest fields | **CONFIRMED schema vocabulary** | Permit `sha256:` or `blake3:` for specified provenance/content fields. |
| EvidenceBundle checksums | **CONFIRMED schema vocabulary** | Use `sha256:` checksums and reference the common `spec_hash` object. |

### Truth posture

**CONFIRMED**

- The source envelope has no verified hashing implementation.
- The child import namespace is effectively empty.
- Package metadata is a greenfield placeholder.
- Repository doctrine and machine contracts disagree about `spec_hash` representation.
- Existing fixtures prove only the current schema wrapper and pattern.
- No checked executable implements RFC 8785 JCS in the package or tool lane.
- The dedicated validator is not implemented.

**PROPOSED**

- The source-tree rules, dependency direction, package/tool delegation, result families, resource limits, implementation sequence, tests, migration, correction, deprecation, and rollback procedures below.

**CONFLICTED**

- `jcs:sha256:<hex>` strings in architecture/standards versus `{"value":"sha256:<hex>"}` in the common contract/schema.
- Reusable implementation under `packages/hashing/` versus the proposed `tools/spec_hash/` helper home.
- SHA-256 as the baseline for trust-bearing identity versus BLAKE3 being accepted for some content/provenance fields.
- Canonicalization profile being semantically necessary while the current common schema does not carry one.
- Rich package documentation versus no verified implementation.

**UNKNOWN**

- Supported Python version, build backend, dependency policy, pinned JCS implementation, exports, callers, performance, cross-language parity, release use, and operational health.

**NEEDS VERIFICATION**

- Owners, ADR or migration note, accepted hash-value model, profile vocabulary, source layout, package/tool ownership, dependency policy, API surface, fixtures, package tests, CI, consumer migration, compatibility period, correction, deprecation, and rollback automation.

[Back to top](#top)

---

<a id="directory-rules-and-authority"></a>

## Directory Rules and authority

`packages/` is the responsibility root for shared reusable implementation libraries. The `src/` subdirectory is an implementation envelope within the existing `packages/hashing/` package.

Directory Rules basis:

| Responsibility | Owning home | This source envelope's posture |
|---|---|---|
| Reusable pure hashing implementation | `packages/hashing/src/` after governance accepts the implementation shape | May contain code; does not own meaning or policy. |
| Import namespace | `packages/hashing/src/hashing/` | Child namespace boundary; currently empty. |
| Human architecture and canonicalization rules | `docs/architecture/`, `docs/standards/`, accepted ADRs | Constrain code; source does not redefine them. |
| Semantic meaning | `contracts/` | Contract authority remains outside source code. |
| Machine shape | `schemas/contracts/v1/` | Schema authority remains outside source code. |
| Valid/invalid schema examples | `fixtures/contracts/` | Fixtures are non-authoritative test inputs. |
| Validators of record | `tools/validators/` or accepted validator root | May import the package; must not duplicate algorithms. |
| Operator and CI wrapper | `tools/spec_hash/` after ownership resolution | Should be a thin adapter if retained. |
| Policy decisions | `policy/` | Package returns facts/results, not policy outcomes. |
| Receipts and proofs | `data/receipts/`, `data/proofs/` | Callers persist; source code does not store. |
| Release, correction, rollback | `release/` and governed workflows | Source code supports verification only. |
| Public behavior | Governed application/API boundaries | Package internals are not public authority. |

This README introduces no new root and no parallel schema, contract, policy, receipt, proof, release, or public path.

[Back to top](#top)

---

<a id="source-envelope-responsibilities"></a>

## Source-envelope responsibilities

This parent source README owns five documentation responsibilities:

1. **Placement:** define what classes of implementation may live under `src/`.
2. **Import direction:** prevent source code from importing authority and storage layers in ways that collapse boundaries.
3. **Delegation:** keep reusable algorithms, CLI wrappers, validators, callers, and persistence separate.
4. **Implementation gates:** state what must be verified before modules are added or exported.
5. **Migration discipline:** require compatibility and rollback plans when representations, profiles, or ownership change.

The child namespace README owns proposed import-level behavior, result structures, and API boundaries. It does not supersede contracts, schemas, standards, ADRs, or this source-envelope placement contract.

### Source-envelope scope

Allowed implementation classes, after verification:

- canonicalization profile adapters;
- raw-byte digest functions;
- typed digest/profile value objects;
- digest parsing and formatting;
- deterministic comparison helpers;
- deterministic Merkle construction from explicit ordered entries;
- deterministic run-id construction from explicit fields;
- geometry digest helpers that require already-normalized geometry and an explicit profile;
- stable error/result types;
- internal, non-authoritative compatibility adapters approved by migration documentation.

Disallowed implementation classes:

- source fetchers;
- lifecycle readers/writers;
- policy engines;
- receipt/proof/release persistence;
- schema or contract generators that become authority;
- public endpoint handlers;
- UI components;
- AI/model calls;
- secret handling;
- signing and key management;
- ambient directory discovery as an integrity input;
- automatic representation conversion without an explicit migration profile.

[Back to top](#top)

---

<a id="compatibility-conflicts"></a>

## Compatibility conflicts

### 1. `spec_hash` representation

Current repository evidence exposes at least two incompatible surfaces:

```text
Doctrine / standards:
  jcs:sha256:<64 lowercase hex>
  urdna2015:sha256:<64 lowercase hex>   # reserved RDF-semantic case

Common contract / schema:
  {
    "value": "sha256:<64 lowercase hex>"
  }
```

The source tree must not silently:

- remove `jcs:` or `urdna2015:` profile prefixes;
- add or remove the object wrapper;
- infer canonicalization from `sha256:` alone;
- treat a raw content checksum as `spec_hash`;
- accept both forms as equivalent without a versioned adapter contract;
- emit a third representation.

Until contract, schema, standard, fixtures, validator, and consumers are reconciled, format conversion is **DENIED by default**.

### 2. Package versus tool ownership

Current documentation names both:

- `packages/hashing/` for reusable hashing implementation;
- `tools/spec_hash/` for spec-hash helpers and operator/CI use.

A sound **PROPOSED** split is:

```text
packages/hashing/src/hashing/
  one reusable pure implementation

tools/spec_hash/
  thin CLI/report adapter importing the package

tools/validators/
  validation orchestration importing the package or tool adapter

callers/
  own persistence, policy mapping, evidence, and release consequences
```

This split is not ratified by this README. An ADR or migration note must resolve ownership before implementation appears in both places.

### 3. Algorithm vocabulary

- SHA-256 is the documented baseline for trust-bearing identity.
- Generated-receipt fields permit SHA-256 or BLAKE3 for specified content/provenance hashes.
- BLAKE3 permission for those fields does not authorize BLAKE3 `spec_hash`.
- Algorithms are never selected by performance preference alone.
- Every digest must carry enough declared context for consumers to distinguish algorithm and canonicalization profile.

### 4. Profile representation

Canonicalization profile is required for meaningful comparison, but the common `spec_hash` schema does not currently represent it. Code must not hide that gap in an internal default.

[Back to top](#top)

---

<a id="confirmed-and-proposed-source-tree"></a>

## Confirmed and proposed source tree

### Confirmed bounded inventory

```text
packages/hashing/
├── README.md
├── pyproject.toml              # name/version placeholder only
└── src/
    ├── README.md               # this file
    └── hashing/
        ├── README.md           # v1.1 namespace boundary
        └── __init__.py         # empty
```

No additional implementation module is claimed.

### Proposed future decomposition

The following is a design option, not a repository fact:

```text
packages/hashing/src/hashing/
├── __init__.py                 # minimal explicit exports; no side effects
├── canonicalization.py         # accepted profiles only
├── digests.py                  # raw-byte algorithms and references
├── values.py                   # typed profile/digest/result values
├── compare.py                  # recompute/compare, no policy mapping
├── merkle.py                   # explicit ordered entries only
├── run_id.py                   # explicit context only
├── geometry.py                 # normalized geometry + explicit profile only
├── errors.py                   # stable internal exceptions/result reasons
└── compatibility.py            # only during approved migrations
```

Before any path above is created:

- verify Directory Rules and current package conventions;
- resolve package/tool ownership;
- resolve `spec_hash` shape/profile;
- pin runtime and dependencies;
- define tests and compatibility;
- document rollback.

Do not create separate `spec_hash.py`, `content_hash.py`, and tool implementations if that causes divergent canonicalization logic. Prefer one primitive implementation with explicit profiles and thin domain-specific adapters.

[Back to top](#top)

---

<a id="keystone-invariants"></a>

## Keystone invariants

1. **Canonicalize first, hash second.**
2. **Canonicalization profile is part of comparison context.**
3. **Algorithm is explicit; no fallback.**
4. **Raw-byte hash and canonical-record identity are different operations.**
5. **A digest match is not truth, admissibility, evidence closure, or release.**
6. **Stored hashes are recomputed at governance boundaries.**
7. **Mismatch and drift fail closed.**
8. **Profile or representation changes are migration-class changes.**
9. **The package is pure and no-network by default.**
10. **Imports have no filesystem, network, time, random, locale, or environment side effects.**
11. **The source tree never writes authority records.**
12. **Tools and validators delegate to one implementation rather than fork it.**
13. **Fixtures are synthetic and non-authoritative.**
14. **Secrets and sensitive payloads are not logged or embedded.**
15. **Geometry hashing requires caller-supplied normalization context.**
16. **Merkle roots use explicit ordered entries, not ambient directory scans.**
17. **Run identity uses explicit fields, not an unrecorded current timestamp or randomness.**
18. **Unsupported or ambiguous inputs return stable failure results.**
19. **Compatibility adapters are temporary, versioned, tested, and removable.**
20. **Rollback remains possible without rewriting historical receipts.**

[Back to top](#top)

---

<a id="import-and-dependency-direction"></a>

## Import and dependency direction

### Allowed direction

```text
contracts / schemas / standards / ADRs
                 |
                 v
packages/hashing pure implementation
                 |
        +--------+---------+
        |                  |
        v                  v
tools/spec_hash      tools/validators
        |                  |
        +---------+--------+
                  v
 governed callers / gates
                  |
                  v
 receipts / proofs / release records
```

The arrows show dependency or constraint direction, not authority transfer.

### Import rules

Source modules should:

- import only standard-library and explicitly pinned approved dependencies;
- expose pure functions and immutable/validated value objects where practical;
- accept bytes, parsed values, explicit profiles, and explicit limits;
- return values/results without writing files or records;
- keep `__init__.py` minimal and side-effect free;
- avoid optional dependency behavior that changes output silently;
- avoid importing application, connector, pipeline, data-store, policy, release, or model-runtime modules.

Source modules must not:

- import from `data/`, `release/`, public app handlers, connectors, or pipeline orchestration;
- resolve records by path or ID;
- read environment secrets;
- make network calls;
- scan working directories;
- use current time, locale, process ID, random state, or host information unless explicitly supplied and contractually part of the input;
- return policy or publication decisions;
- catch integrity errors and downgrade them to warnings.

### Dependency policy

A future canonicalization dependency must be:

- version pinned;
- license and supply-chain reviewed;
- capable of the accepted standard, not an approximation;
- tested against normative and project vectors;
- deterministic across supported runtimes;
- included in dependency scanning;
- covered by an upgrade and rollback policy.

A naive `json.dumps(sort_keys=True)` implementation must not be presented as RFC 8785-compliant for authority-bearing identity.

[Back to top](#top)

---

<a id="canonicalization-and-hash-boundary"></a>

## Canonicalization and hash boundary

### Distinct operation classes

| Operation | Input | Required context | Output | Must not imply |
|---|---|---|---|---|
| Raw byte digest | Exact bytes | Algorithm | Digest reference | Canonical semantic identity |
| JSON canonicalization | Parsed JSON value | Versioned profile and limits | Canonical UTF-8 bytes | Schema validity or authority |
| RDF canonicalization | RDF dataset | Accepted RDF profile | Canonical dataset bytes | Default KFM identity |
| `spec_hash` computation | Canonical trust-record body | Accepted representation/profile | Versioned identity value | Correctness or release |
| Digest comparison | Expected and recomputed values | Same algorithm/profile/representation | Typed comparison result | Policy or evidence decision |
| Merkle construction | Explicit ordered entry list | Leaf/node profile | Root digest | Release approval |
| Geometry digest | Already-normalized geometry | CRS, precision, normalization profile | Geometry digest | Spatial correctness or public safety |
| Run-id construction | Explicit run context | Versioned run-id profile | Deterministic identifier | Receipt existence or success |

### Parsing requirements

Future parsers must reject or explicitly classify:

- malformed prefixes;
- unknown algorithms;
- unknown profiles;
- uppercase or non-hex forms where the governing contract disallows them;
- wrong digest lengths;
- ambiguous wrappers;
- duplicate JSON object keys;
- invalid Unicode;
- non-finite numbers;
- numbers outside the supported canonicalization domain;
- profile/representation mismatch;
- conversion requests without an approved adapter.

### Comparison rule

Two digest values are comparable only when:

- their intended operation class matches;
- algorithm matches;
- canonicalization profile matches when applicable;
- representation version matches or an approved adapter is invoked;
- the same inclusion/exclusion rules were used;
- the compared body or bytes are defined by the same contract.

[Back to top](#top)

---

<a id="package-tool-validator-and-caller-delegation"></a>

## Package, tool, validator, and caller delegation

| Surface | May do | Must not do |
|---|---|---|
| `packages/hashing/src/` | Implement reusable pure primitives. | Persist records, decide policy, or own CLI orchestration. |
| `packages/hashing/src/hashing/` | Define accepted imports after ratification. | Hide compatibility conflicts or export unimplemented behavior. |
| `tools/spec_hash/` | Parse CLI input, call package, produce review reports. | Fork canonicalization or become record authority. |
| `tools/validators/` | Validate contract/schema alignment and map package results into validation reports. | Reimplement hashing or approve release. |
| Receipt/proof builders | Call package and persist governed records. | Treat a digest as evidence closure. |
| Promotion/release gates | Recompute, compare, and apply policy/review. | Trust stored digests without recomputation. |
| Public apps/APIs | Consume governed released results. | Expose raw package internals as public truth. |

### Thin-adapter requirement

A tool or validator adapter should contain only:

- input decoding;
- explicit profile selection from accepted configuration;
- call into the package;
- stable report formatting;
- exit-code or validation-result mapping;
- no duplicate canonicalization algorithm.

Parity tests must prove that direct library use and tool/validator use produce identical bytes, digests, and reason codes for the same inputs.

[Back to top](#top)

---

<a id="expected-result-families"></a>

## Expected result families

Exact types and names remain **PROPOSED**. The source envelope should support finite, inspectable result classes such as:

| Result | Meaning | Default posture |
|---|---|---|
| `DIGEST_COMPUTED` | Digest produced from explicit bytes/profile. | Return value; no authority created. |
| `MATCH` | Stored and recomputed values match under identical context. | Continue to other gates. |
| `MISMATCH` | Values differ. | Fail closed. |
| `DRIFT_DETECTED` | Recomputed identity differs from a prior governed expectation. | Block and require review/correction. |
| `INVALID_INPUT` | Input cannot be parsed or represented safely. | Fail closed. |
| `INVALID_DIGEST` | Digest syntax or length is invalid. | Fail closed. |
| `UNSUPPORTED_PROFILE` | Profile is not accepted. | Abstain/error; never infer. |
| `UNSUPPORTED_ALGORITHM` | Algorithm is not accepted for the operation. | Abstain/error; never fallback. |
| `FORMAT_CONFLICT` | Input representation is valid in one repo surface but conflicts with another. | Hold for migration decision. |
| `PROFILE_MISMATCH` | Compared values use different profiles. | Not comparable. |
| `DEPENDENCY_UNAVAILABLE` | Required canonicalization implementation is absent. | Fail closed. |
| `RESOURCE_LIMIT` | Input exceeds configured bounds. | Fail closed without partial authority. |
| `ERROR` | Unexpected safe failure. | No digest authority; sanitized diagnostics. |

Reason codes should be stable, machine-readable, and separate from human explanations. Callers—not this package—map results into PolicyDecision, ValidationReport, PromotionDecision, or release outcomes.

[Back to top](#top)

---

<a id="security-and-resource-bounds"></a>

## Security and resource bounds

Even a no-network library needs defensive limits.

### Required controls

- maximum byte-input size;
- maximum JSON text size before parsing;
- maximum nesting depth;
- maximum object members and array items;
- duplicate-key rejection or explicitly governed handling;
- maximum string length;
- strict UTF-8 behavior;
- non-finite number rejection;
- explicit numeric-domain support;
- maximum Merkle entries;
- maximum path/reference length for explicit entry metadata;
- maximum geometry coordinate count when geometry helpers are enabled;
- bounded diagnostic output;
- no raw payload logging by default;
- no secret, token, credential, or sensitive-record echo;
- deterministic error ordering where multiple errors are returned.

### Cryptographic scope exclusions

This package is not automatically suitable for:

- password storage;
- HMAC or message authentication;
- digital signatures;
- encryption;
- key derivation;
- random-token generation;
- certificate validation;
- secure deletion;
- transparency logging.

Adding any of those is a separate security and architecture decision.

### Denial-of-service posture

Callers must be able to configure conservative limits. Exceeding a limit returns `RESOURCE_LIMIT`; it must not truncate input and compute a misleading digest.

[Back to top](#top)

---

<a id="testing-fixtures-and-ci"></a>

## Testing, fixtures, and CI

### Current verified test posture

- Common contract fixtures validate the object wrapper and `sha256:` pattern.
- The generic schema harness checks valid and invalid JSON Schema fixtures.
- The dedicated `spec_hash` validator raises `NotImplementedError`.
- No package-specific hashing test README was found at checked paths.
- No dedicated hashing workflow was found at checked paths.
- No current test proves RFC 8785 canonicalization, URDNA2015 behavior, digest computation, package/tool parity, or import safety.

### Required future test families

| Test family | Minimum coverage |
|---|---|
| Import safety | No network, filesystem scan, environment read, logging, time/randomness, or lifecycle write during import. |
| Raw bytes | Empty input, binary data, large input bounds, stable SHA-256 vectors. |
| JCS | Normative vectors, key ordering, escapes, Unicode, integers, decimals, exponent forms, negative zero, duplicate keys, invalid numbers. |
| RDF reserved profile | Only after profile acceptance; normative dataset vectors and explicit profile selection. |
| Digest parsing | Valid prefixes, invalid prefixes, length, case, unknown algorithm/profile, wrapper conflicts. |
| Comparison | Match, mismatch, profile mismatch, algorithm mismatch, format conflict, drift. |
| Schema compatibility | Current object wrapper plus any approved migration representation. |
| Tool parity | Library, CLI adapter, and validator produce identical results. |
| Merkle | Ordering, duplicate paths/IDs, empty set policy, leaf/node separation, changed entry detection. |
| Run ID | Explicit field inclusion, order independence where specified, no ambient state. |
| Geometry | Requires normalized input and explicit CRS/precision profile; rejects missing context. |
| Resource limits | Each configured limit fails closed without partial digest authority. |
| Logging | Diagnostics are bounded and do not expose raw/sensitive input. |
| Cross-runtime parity | Same canonical bytes and digest across every supported runtime/platform. |
| Migration | Old/new representations remain distinguishable and adapters are one-way or explicitly reversible as designed. |

### Fixture rules

Package algorithm fixtures should be separate from contract-shape fixtures.

They must:

- be synthetic or normative public vectors;
- include expected canonical bytes where licensing permits;
- include expected digest and profile;
- declare the implementation/version used to establish expectations;
- remain stable;
- avoid production secrets, source records, or sensitive geometry;
- make intentional drift reviewable.

### CI gates before operational use

- package installs in a clean environment;
- import safety passes;
- algorithm/profile vectors pass;
- package/tool/validator parity passes;
- schema compatibility passes;
- dependency and license scanning passes;
- resource-bound tests pass;
- negative paths pass;
- no authority import cycles are introduced;
- docs and type/API surfaces match implementation.

A passing generic schema fixture test does not prove hashing implementation.

[Back to top](#top)

---

<a id="smallest-sound-implementation-sequence"></a>

## Smallest sound implementation sequence

### Stage 0 — governance resolution

Do not add hashing modules until:

1. owners are assigned;
2. accepted `spec_hash` representation is decided;
3. canonicalization profiles and versioning are decided;
4. package-versus-tool ownership is decided;
5. supported runtime and dependency policy are pinned;
6. migration and rollback are documented.

**Stop condition:** unresolved representation or ownership conflict.

### Stage 1 — raw-byte digest primitive

Implement only:

- explicit bytes input;
- SHA-256;
- typed digest value;
- strict parsing/formatting for one accepted raw-content representation;
- size limits;
- deterministic vectors;
- import safety.

Do not call it `spec_hash` unless the profile and representation are accepted.

### Stage 2 — accepted JSON canonicalization

Add the pinned RFC 8785 implementation and normative vectors.

Requirements:

- explicit profile identifier;
- strict input domain;
- duplicate-key policy;
- numeric edge-case tests;
- no approximation;
- no fallback.

### Stage 3 — `spec_hash` adapter

Only after contract/schema reconciliation:

- define the canonical body and exclusions outside the package;
- convert accepted canonical bytes to the accepted representation;
- add compatibility fixtures;
- update validators and consumers;
- prohibit silent legacy conversion.

### Stage 4 — tool and validator delegation

Make `tools/spec_hash/` and `tools/validators/validate_spec_hash.py` import the package. Add parity tests and remove duplicate logic.

### Stage 5 — optional families

Add Merkle, run-id, geometry, RDF, or BLAKE3 support only when a real governed consumer, contract, and test surface exist.

### Stage 6 — operational adoption

Before promotion/release use:

- inventory consumers;
- run replay tests;
- verify receipts and rollback targets;
- stage migration;
- monitor drift;
- preserve old representation readers for the documented compatibility period.

[Back to top](#top)

---

<a id="definition-of-done"></a>

## Definition of done

This source envelope is implementation-ready only when:

- [ ] Owners and CODEOWNERS coverage are confirmed.
- [ ] Directory Rules placement is rechecked.
- [ ] Package/tool ownership is resolved by ADR or migration note.
- [ ] `spec_hash` representation and profile are reconciled across standard, contract, schema, fixtures, validator, and consumers.
- [ ] Supported runtime and build backend are pinned.
- [ ] Package discovery and installability are proven.
- [ ] Dependencies are pinned, reviewed, and scanned.
- [ ] `hashing/__init__.py` exports are explicit, minimal, and side-effect free.
- [ ] One implementation owns canonicalization and digest primitives.
- [ ] Tools and validators delegate to it.
- [ ] Raw-byte and canonical-record operations remain distinct.
- [ ] Algorithms and profiles are explicit.
- [ ] Unsupported or ambiguous inputs fail closed.
- [ ] Resource bounds are implemented and tested.
- [ ] Normative JCS vectors pass.
- [ ] Cross-runtime parity passes for supported runtimes.
- [ ] Package/tool/validator parity passes.
- [ ] Schema-shape and algorithm fixtures remain separate.
- [ ] No lifecycle, policy, receipt, proof, release, public app, or model authority is imported.
- [ ] Consumers recompute rather than trust stored values.
- [ ] Migration, correction, deprecation, and rollback paths are tested.
- [ ] Documentation matches actual exports and behavior.
- [ ] CI gates the relevant behavior.
- [ ] A reviewer can reproduce canonical bytes and digest from declared inputs.

[Back to top](#top)

---

<a id="verification-register"></a>

## Verification register

| ID | Verification item | Status |
|---|---|---:|
| HASH-SRC-001 | Assign package and canonicalization owners. | NEEDS VERIFICATION |
| HASH-SRC-002 | Confirm CODEOWNERS coverage. | NEEDS VERIFICATION |
| HASH-SRC-003 | Confirm current `main` source inventory recursively. | NEEDS VERIFICATION |
| HASH-SRC-004 | Confirm supported Python version. | UNKNOWN |
| HASH-SRC-005 | Confirm build backend and package discovery. | UNKNOWN |
| HASH-SRC-006 | Confirm installability in a clean environment. | UNKNOWN |
| HASH-SRC-007 | Resolve `packages/hashing/` versus `tools/spec_hash/` ownership. | CONFLICTED |
| HASH-SRC-008 | Resolve `jcs:sha256:` versus object-wrapped `sha256:` representation. | CONFLICTED |
| HASH-SRC-009 | Decide whether profile is embedded, adjacent, or versioned by type. | NEEDS VERIFICATION |
| HASH-SRC-010 | Reconcile common contract and schema. | NEEDS VERIFICATION |
| HASH-SRC-011 | Update valid and invalid fixtures after reconciliation. | NEEDS VERIFICATION |
| HASH-SRC-012 | Implement the dedicated validator or revise its declared path. | NEEDS VERIFICATION |
| HASH-SRC-013 | Pin an RFC 8785 implementation. | UNKNOWN |
| HASH-SRC-014 | Review canonicalization dependency license and supply chain. | NEEDS VERIFICATION |
| HASH-SRC-015 | Decide duplicate-key handling. | NEEDS VERIFICATION |
| HASH-SRC-016 | Decide supported numeric domain. | NEEDS VERIFICATION |
| HASH-SRC-017 | Define canonicalization profile versioning. | NEEDS VERIFICATION |
| HASH-SRC-018 | Define raw-content digest representation. | NEEDS VERIFICATION |
| HASH-SRC-019 | Confirm whether URDNA2015 belongs in this package. | UNKNOWN |
| HASH-SRC-020 | Confirm BLAKE3 scope and prohibited uses. | CONFLICTED |
| HASH-SRC-021 | Define result and reason-code types. | PROPOSED |
| HASH-SRC-022 | Define size/depth/count limits. | PROPOSED |
| HASH-SRC-023 | Confirm import-side-effect tests. | NOT FOUND |
| HASH-SRC-024 | Confirm package-specific test root. | NOT FOUND |
| HASH-SRC-025 | Add normative JCS vectors. | NEEDS VERIFICATION |
| HASH-SRC-026 | Add digest parser negative tests. | NEEDS VERIFICATION |
| HASH-SRC-027 | Add package/tool/validator parity tests. | NEEDS VERIFICATION |
| HASH-SRC-028 | Add cross-runtime parity tests. | NEEDS VERIFICATION |
| HASH-SRC-029 | Define Merkle leaf/node profile before implementation. | NEEDS VERIFICATION |
| HASH-SRC-030 | Define run-id field inclusion before implementation. | NEEDS VERIFICATION |
| HASH-SRC-031 | Define geometry normalization ownership before implementation. | NEEDS VERIFICATION |
| HASH-SRC-032 | Inventory all current `spec_hash` consumers. | UNKNOWN |
| HASH-SRC-033 | Inventory all current `sha256:` and `blake3:` producers. | UNKNOWN |
| HASH-SRC-034 | Define compatibility adapter direction and lifetime. | NEEDS VERIFICATION |
| HASH-SRC-035 | Define correction process for previously emitted conflicting digests. | NEEDS VERIFICATION |
| HASH-SRC-036 | Define deprecation notices and consumer deadlines. | NEEDS VERIFICATION |
| HASH-SRC-037 | Define rollback targets and replay checks. | NEEDS VERIFICATION |
| HASH-SRC-038 | Add dedicated CI or prove equivalent repository-wide coverage. | NOT FOUND |
| HASH-SRC-039 | Verify dependency and license scans include the package. | UNKNOWN |
| HASH-SRC-040 | Verify docs reflect actual exports after implementation. | NEEDS VERIFICATION |

[Back to top](#top)

---

<a id="rollback-correction-deprecation-and-migration"></a>

## Rollback, correction, deprecation, and migration

### Documentation rollback

For this README-only change:

- revert the commit that updates `packages/hashing/src/README.md`; or
- restore prior blob `309afb28791d0f1136358b79f690ee99786a7ae8`.

No implementation, contract, schema, fixture, validator, workflow, or runtime behavior is changed by this README.

### Implementation rollback

A future source implementation must be reversible by:

- retaining the prior package version;
- preserving test vectors and replay fixtures;
- preserving old representation readers for the documented compatibility period;
- preventing new writes in the deprecated representation after cutover;
- restoring tool and validator adapters to the prior package version;
- recomputing affected records before accepting rollback success.

### Correction

When an emitted digest is wrong because of implementation, profile, representation, or exclusion-rule error:

1. do not overwrite historical receipts silently;
2. identify affected producer version and consumers;
3. preserve original digest and record;
4. issue the appropriate correction/supersession artifact in its owning root;
5. recompute using the accepted profile;
6. link old and corrected records;
7. verify replay and rollback;
8. update tests to prevent recurrence.

### Deprecation

Deprecating a profile, algorithm, representation, function, or module requires:

- replacement mapping;
- consumer inventory;
- compatibility period;
- warnings with stable reason codes;
- migration fixtures;
- cutover criteria;
- rollback target;
- removal only after consumers and historical replay are addressed.

### Migration principle

Never change the meaning of an existing prefix or wrapper in place. Introduce a versioned representation or adapter, migrate explicitly, and preserve historical verifiability.

[Back to top](#top)

---

## Status summary

`packages/hashing/src/` is a source-code envelope, not a functioning integrity subsystem. Current evidence confirms documentation, placeholder package metadata, an empty child initializer, schema-shape fixtures, and conflicting hash representations. It does not confirm canonicalization code, digest exports, installability, package-specific tests, CI enforcement, operational consumers, or runtime health.

The smallest safe next implementation step is governance reconciliation—not code: resolve representation, profile, ownership, runtime, dependency, tests, migration, and rollback before adding exports.

<p align="right"><a href="#top">Back to top</a></p>
