<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-hashing-src-hashing-readme
title: packages/hashing/src/hashing/ — Deterministic Hashing Namespace and Compatibility Boundary
type: readme
version: v1.1
status: draft
owners: OWNER_TBD — Package steward · Integrity/canonicalization steward · Contract steward · Schema steward · Security steward · Validation steward · Release steward · Migration steward · CI steward · Docs steward
created: NEEDS VERIFICATION — target existed before the current evidence-grounded revision
updated: 2026-07-15
policy_label: "public-doctrine; package-boundary; import-namespace; deterministic-hashing; implementation-empty; api-unratified; canonicalization-conflicted; spec-hash-shape-conflicted; tools-package-ownership-conflicted; no-network; pure-functions; fail-closed; no-authority; no-secrets; migration-required; rollback-aware"
current_path: packages/hashing/src/hashing/README.md
truth_posture: CONFIRMED target README, empty hashing package initializer, kfm-hashing 0.0.0 placeholder metadata, package/source/root READMEs, Directory Rules package placement, draft identity and canonicalization doctrine, draft common spec_hash contract and schema, schema fixtures and generic schema test harness, placeholder dedicated validator, README-only tools/spec_hash lane, generated-receipt digest vocabulary, and bounded absence of proposed namespace modules and package-specific test/workflow paths / PROPOSED pure reusable library API, explicit digest/profile value objects, typed comparison outcomes and reason codes, resource limits, package-tool delegation split, migration adapters, implementation sequence, tests, correction, and rollback / CONFLICTED jcs:sha256 string doctrine versus object-wrapped sha256 schema and contract, packages/hashing versus tools/spec_hash implementation ownership, spec_hash canonicalization representation, SHA-256 authority baseline versus BLAKE3-permitted content/provenance fields, and documentation richness versus empty implementation / UNKNOWN accepted Python runtime, build backend, dependency set, pinned JCS implementation, export surface, consumer inventory, installability, runtime behavior, cross-language parity, package-specific tests, CI enforcement, release/deployment use, and operational health / NEEDS VERIFICATION owners, ADR or migration decision, canonical hash vocabulary, schema/contract reconciliation, package ownership, dependencies, API shape, resource limits, test vectors, consumer migration, CI gates, correction path, compatibility period, deprecation, and rollback automation
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 4ba3a0abec525a17955ff0175bdefc4455080c96
  prior_blob: 0398cc127ddcdf6e37f47882a02f11443f884682
  package_readme_blob: c9440697c02f71a8c83f0293d72364bb89930c01
  source_readme_blob: 309afb28791d0f1136358b79f690ee99786a7ae8
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
    - packages/hashing/src/hashing/README.md existed at version v1 before this revision
    - packages/hashing/src/hashing/__init__.py exists and is empty
    - packages/hashing/pyproject.toml contains only project name kfm-hashing and version 0.0.0
    - packages/hashing/package.json was not found
    - packages/hashing/src/hashing.py was not found
    - canonical_json.py, digests.py, spec_hash.py, content_hash.py, geometry_hash.py, merkle.py, run_id.py, compare.py, and fixtures.py were not found under the namespace
    - packages/hashing/tests/README.md and tests/packages/hashing/README.md were not found
    - .github/workflows/hashing.yml, package-hashing.yml, and spec-hash.yml were not found
    - tools/spec_hash/jcs_hash.py and tools/spec_hash/spec_hash.py were not found
    - tools/validators/validate_spec_hash.py raises NotImplementedError
related:
  - ../../README.md
  - ../README.md
  - __init__.py
  - ../../../pyproject.toml
  - ../../../../README.md
  - ../../../../../docs/doctrine/directory-rules.md
  - ../../../../../docs/architecture/identity-and-spec-hash.md
  - ../../../../../docs/standards/CANONICALIZATION.md
  - ../../../../../contracts/common/spec_hash.md
  - ../../../../../schemas/contracts/v1/common/spec_hash.schema.json
  - ../../../../../schemas/contracts/v1/evidence/evidence_bundle.schema.json
  - ../../../../../schemas/contracts/v1/receipts/generated_receipt.schema.json
  - ../../../../../fixtures/contracts/v1/common/spec_hash/README.md
  - ../../../../../tests/schemas/test_common_contracts.py
  - ../../../../../tools/validators/validate_spec_hash.py
  - ../../../../../tools/spec_hash/README.md
  - ../../../../../contracts/
  - ../../../../../schemas/
  - ../../../../../policy/
  - ../../../../../data/receipts/
  - ../../../../../data/proofs/
  - ../../../../../release/
tags: [kfm, packages, hashing, deterministic-identity, canonicalization, jcs, urdna2015, sha256, blake3, spec-hash, content-hash, geometry-hash, artifact-hash, merkle-root, run-id, replay, compatibility, migration, fail-closed]
notes:
  - "This revision changes only packages/hashing/src/hashing/README.md."
  - "The namespace currently contains this README and an empty __init__.py; proposed helper modules were not found at the checked paths."
  - "This README does not activate an API, select a canonical spec_hash representation, or ratify packages/hashing over tools/spec_hash as the sole implementation home."
  - "The current docs and machine contracts disagree about spec_hash representation; callers and future code must not silently translate between them."
  - "Hash equality is integrity evidence about declared bytes/profile only. It is not truth, evidence closure, policy approval, release approval, or public safety."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Deterministic Hashing Namespace and Compatibility Boundary

`packages/hashing/src/hashing/`

> Repository-present import namespace for reusable deterministic hashing helpers. Current evidence establishes a README and an empty initializer—not an installable, exported, tested, or CI-enforced hashing implementation.

![status](https://img.shields.io/badge/status-draft-yellow)
![version](https://img.shields.io/badge/version-v1.1-informational)
![maturity](https://img.shields.io/badge/maturity-empty__namespace-lightgrey)
![canonicalization](https://img.shields.io/badge/canonicalization-CONFLICTED-orange)
![ownership](https://img.shields.io/badge/ownership-CONFLICTED-orange)
![network](https://img.shields.io/badge/network-none-critical)
![authority](https://img.shields.io/badge/truth__authority-none-red)
![behavior](https://img.shields.io/badge/behavior-fail__closed-blue)

**Quick links:** [Purpose](#purpose) · [Evidence](#status-and-evidence) · [Placement](#directory-rules-and-authority) · [Conflicts](#compatibility-conflicts) · [Invariants](#keystone-invariants) · [Inputs](#explicit-input-contract) · [Canonicalization](#canonicalization-contract) · [Hash families](#hash-family-boundaries) · [API](#proposed-library-api) · [Outcomes](#comparison-outcomes-and-reason-codes) · [Security](#security-and-resource-bounds) · [Testing](#testing-and-parity) · [Migration](#compatibility-and-migration) · [Implementation](#smallest-sound-implementation-sequence) · [Done](#definition-of-done) · [Open](#verification-register) · [Rollback](#rollback-correction-and-deprecation)

> [!IMPORTANT]
> **This README is not an API ratification or canonicalization migration.** It does not establish exports, dependencies, a pinned JCS library, supported profiles, a canonical `spec_hash` shape, package ownership over the tool lane, CI enforcement, or operational consumers.

> [!CAUTION]
> **A matching digest is not a truth decision.** It establishes only that the compared inputs produce the same digest under the declared algorithm and canonicalization profile. Schema validity, authority, provenance, evidence sufficiency, rights, sensitivity, policy, review, release, and public safety remain separate gates.

---

<a id="purpose"></a>

## Purpose

This README defines the allowed boundary for a future importable `hashing` library inside the shared `packages/` responsibility root.

A conforming implementation may:

- canonicalize explicit supported inputs under an accepted, versioned profile;
- hash explicit bytes with an accepted digest algorithm;
- format and parse versioned digest references;
- compare recomputed and stored digests;
- return deterministic typed results and stable reason codes;
- support replay, receipt construction, validation, release verification, and rollback tooling **without owning those processes**.

It must not:

- invent object meaning, schema fields, exclusion lists, source authority, or canonicalization profiles;
- choose between conflicting repository contracts by implementation convenience;
- read lifecycle stores, source systems, credentials, UI state, hidden globals, or model output;
- write receipts, proofs, EvidenceBundles, catalogs, release records, signatures, or published artifacts;
- approve promotion, publication, rollback, policy, evidence closure, or public answers;
- become a password-hashing, HMAC, signing, key-management, encryption, or secret-storage library without a separately governed scope change.

[Back to top](#top)

---

<a id="status-and-evidence"></a>

## Status and evidence

| Surface | Status | Safe conclusion |
|---|---:|---|
| Target README | **CONFIRMED v1 before revision** | A namespace boundary exists. |
| `hashing/__init__.py` | **CONFIRMED empty** | No public exports or runtime behavior are established. |
| `kfm-hashing` metadata | **CONFIRMED `0.0.0` placeholder** | Package name exists; installability and discovery are not established. |
| Proposed namespace modules | **NOT FOUND at bounded paths** | No canonicalization, digest, comparison, Merkle, run-id, or geometry implementation is established. |
| Package-specific test README | **NOT FOUND** | No dedicated hashing-package test boundary is established. |
| Package-specific workflow | **NOT FOUND** | No dedicated hashing CI enforcement is established. |
| Parent package/source READMEs | **CONFIRMED draft** | They describe intended boundaries, not implementation. |
| Identity architecture | **CONFIRMED draft doctrine** | States JCS + SHA-256 and recompute-on-gate behavior. |
| Canonicalization standard | **CONFIRMED draft standard** | JCS default; URDNA2015 reserved; pinned implementation remains unresolved. |
| Common `spec_hash` contract/schema | **CONFIRMED draft/PROPOSED machine surface** | Requires an object with `value: sha256:<hex>`. |
| `spec_hash` fixtures | **CONFIRMED minimal shape fixtures** | Test schema acceptance/rejection, not canonicalization correctness. |
| Generic common-contract test harness | **CONFIRMED executable test code** | Discovers schema fixtures; no hashing computation occurs. |
| Dedicated `spec_hash` validator | **CONFIRMED placeholder** | Raises `NotImplementedError`; not operational validation. |
| `tools/spec_hash/` | **CONFIRMED README-only lane** | Tool ownership is proposed; executable files checked were absent. |
| Generated-receipt digest fields | **CONFIRMED schema vocabulary** | Permit `sha256:` or `blake3:` for specified provenance/content fields. |
| EvidenceBundle checksums | **CONFIRMED schema vocabulary** | Use `sha256:` checksums and reference the common `spec_hash` object. |

### Truth posture

**CONFIRMED**

- The namespace is effectively empty.
- The package metadata is a greenfield placeholder.
- Repository doctrine and machine contracts currently disagree about `spec_hash` representation.
- Schema fixture tests exist for the current object wrapper and `sha256:` pattern.
- No checked executable implements RFC 8785 JCS for this package or the tool lane.
- The dedicated validator is a placeholder.

**PROPOSED**

- The pure-library API, typed results, reason codes, resource limits, package/tool delegation split, compatibility adapters, tests, migration sequence, and rollback procedures below.

**CONFLICTED**

- `jcs:sha256:<hex>` strings in architecture/standards versus `{"value":"sha256:<hex>"}` in the common contract/schema.
- Reusable implementation under `packages/hashing/` versus the proposed `tools/spec_hash/` helper home.
- SHA-256 as the baseline for trust-bearing identity versus BLAKE3 being accepted for some generated-receipt content/provenance hashes.
- Canonicalization-profile identity being semantically required while the current common schema does not represent the profile.

**UNKNOWN**

- Supported Python version, build backend, dependencies, pinned RFC 8785 implementation, exports, callers, performance, cross-language parity, release use, and operational health.

**NEEDS VERIFICATION**

- Owners, an ADR or migration note, accepted hash-value model, profile vocabulary, package/tool ownership, dependency policy, fixtures, package tests, CI, consumer migration, compatibility period, correction, and deprecation.

[Back to top](#top)

---

<a id="directory-rules-and-authority"></a>

## Directory Rules and authority

Directory Rules identify `packages/` as the home for shared reusable libraries. The target therefore has a sound **responsibility root** for a reusable pure hashing library.

```text
packages/
└── hashing/
    └── src/
        └── hashing/
            ├── README.md
            └── __init__.py
```

The current placement does **not** prove that `hashing` is a valid import name or that packaging discovers this namespace. Those facts require build metadata and installation tests.

| Responsibility | Owning home | Namespace posture |
|---|---|---|
| Reusable canonicalization/digest code | `packages/hashing/` after ratification | May implement pure helpers. |
| CLI and operator UX | `tools/spec_hash/` or accepted tool home | Should delegate to the package; must not duplicate algorithms. |
| Hash meaning | `contracts/` | Package consumes; does not define. |
| Hash shape | `schemas/` | Package validates/adapts only through accepted versions. |
| Canonicalization standard | `docs/standards/` plus ADRs | Package implements pinned profiles. |
| Validation policy and gate consequences | `policy/`, validators, release workflows | Package returns facts/reasons only. |
| Receipts and proofs | `data/receipts/`, `data/proofs/` | Package may return fields; never persists authority. |
| Release, correction, rollback | `release/` and governed workflows | Package may verify digests; never decides state. |
| Source acquisition and lifecycle reads | `connectors/`, `pipelines/`, governed data access | Out of scope. |
| Public responses | `apps/governed-api/` and released interfaces | Package internals are not a public trust membrane. |

### Proposed package/tool split

Subject to ADR or migration approval:

```text
packages/hashing/   = reusable, side-effect-free library
tools/spec_hash/    = thin CLI/report adapter importing the library
```

Until that split is accepted:

- do not implement separate canonicalizers in both roots;
- do not publish two incompatible result vocabularies;
- do not let the tool lane become the de facto library through imports;
- do not delete or deprecate either lane by README language alone.

[Back to top](#top)

---

<a id="compatibility-conflicts"></a>

## Compatibility conflicts

### Conflict 1 — `spec_hash` representation

Repository evidence currently describes at least two incompatible representations:

| Surface | Shape | Profile carried? | Current posture |
|---|---|---:|---|
| Identity architecture / canonicalization standard | `jcs:sha256:<64 hex>`; rare `urdna2015:sha256:<64 hex>` | Yes, in prefix | Draft doctrine/standard |
| Common contract/schema | `{"value":"sha256:<64 lowercase hex>"}` | No | Draft contract + PROPOSED schema |
| EvidenceBundle `checksums` | `sha256:<64 hex>` | No; checksum only | PROPOSED schema |
| Generated receipt artifact/evidence hashes | `sha256:<hex>` or `blake3:<hex>` | No canonicalization profile | Active schema shape, field-specific |

These values are **not interchangeable** merely because they contain the same digest bytes.

The namespace must not:

- strip `jcs:` or `urdna2015:` to satisfy the common schema;
- wrap or unwrap a digest without an explicit versioned adapter;
- infer canonicalization from `sha256:` alone;
- call a raw checksum a `spec_hash`;
- accept `blake3:` in an authority field whose governing schema allows only SHA-256;
- emit a value that validates syntactically but loses profile identity.

### Conflict 2 — package versus tool ownership

`docs/architecture/identity-and-spec-hash.md` and `tools/spec_hash/README.md` point toward a tool helper lane. Directory Rules place reusable library logic under `packages/`.

A safe resolution requires:

1. one canonical implementation;
2. a documented import direction;
3. no circular dependency;
4. one result model;
5. one test-vector suite;
6. a migration and rollback plan.

### Conflict 3 — canonicalization implementation

The canonicalization standard says bare `json.dumps(sort_keys=True, ...)` is only illustrative and is not RFC 8785-correct for all numeric cases. No pinned implementation was found in the checked package or tool paths.

Until a runtime and library are pinned, production `spec_hash` computation remains **UNSUPPORTED**, not “approximately correct.”

[Back to top](#top)

---

<a id="keystone-invariants"></a>

## Keystone invariants

1. **Canonicalize first, hash second.**
2. **The governing contract selects the profile.** The package does not guess.
3. **Digest equality is not semantic equality unless the profile defines it.**
4. **Algorithm, profile, version, and input class remain inspectable.**
5. **Raw byte hashes and canonical-object hashes remain distinct.**
6. **A checksum is not automatically a `spec_hash`.**
7. **A `spec_hash` is not proof of correctness, authority, evidence, or release.**
8. **Stored hashes are recomputed at governance boundaries.**
9. **Mismatch, profile disagreement, or unsupported input fails closed.**
10. **Canonicalization or algorithm changes are migration/ADR-class.**
11. **No ambient state participates unless the governing profile explicitly includes it.**
12. **No network, source retrieval, lifecycle access, receipt persistence, or publication side effect occurs in the library.**
13. **Sensitive data is not logged merely because it is hash input.**
14. **One canonical implementation serves package users and tool wrappers.**
15. **Compatibility transforms are explicit, versioned, reversible, and receipted by their caller.**

[Back to top](#top)

---

<a id="explicit-input-contract"></a>

## Explicit input contract

A future function must receive enough explicit context to reproduce the result.

| Input | Required information | Failure posture |
|---|---|---|
| Raw bytes | bytes, accepted algorithm, optional media/type label | Reject unsupported algorithm or non-bytes input. |
| JSON value | parsed value, canonicalization profile/version, governing contract/schema ref | Reject missing or unsupported profile. |
| JSON text | UTF-8 bytes, duplicate-key policy, profile/version | Parse once under pinned behavior; reject ambiguity. |
| JSON-LD / RDF | identity layer: JSON/JCS or RDF/URDNA2015, context handling, dataset profile | Do not infer semantic-equivalence intent. |
| Geometry | normalized geometry bytes/value, CRS, axis order, precision, ring/order rules, geometry profile | Return unsupported until a profile is accepted. |
| File set / Merkle input | explicit ordered entries, leaf encoding, path normalization, duplicate rule, tree algorithm/version | Never scan ambient directories implicitly. |
| Run identity input | accepted field set, serialization profile, time/randomness policy | Do not derive from unrecorded clock, PID, path, or random state. |
| Digest comparison | stored value, recomputed value, expected family/profile/schema version | Compare only after representation compatibility checks. |

### Input handling requirements

- Do not mutate caller objects.
- Do not silently coerce floats, decimal strings, bytes, datetimes, paths, or enums.
- Reject NaN and infinities for JCS inputs.
- Reject or explicitly handle duplicate JSON object keys before canonicalization.
- Preserve UTF-8 and Unicode behavior defined by the profile.
- Bound input size, nesting depth, object/array counts, and total canonical output.
- Do not accept a path when the API contract promises bytes unless a separate file adapter is explicitly named.
- Do not read environment variables, current working directory, locale, timezone, or host configuration to complete an identity value.

[Back to top](#top)

---

<a id="canonicalization-contract"></a>

## Canonicalization contract

### JCS default

Draft KFM standard documents RFC 8785 JCS as the default JSON canonicalization profile.

A conforming implementation must use a pinned implementation or demonstrate byte parity against accepted RFC/JCS test vectors. It must not substitute “sorted JSON” and label the result JCS.

Required behaviors include:

- UTF-8 output;
- deterministic object-member ordering;
- no insignificant whitespace;
- RFC-compatible string escaping;
- accepted number serialization;
- explicit rejection of unsupported numeric values;
- stable handling of empty objects/arrays and nested values.

### URDNA2015 reserved profile

URDNA2015 is reserved for RDF-dataset semantic equivalence. It is not a general fallback when JCS fails.

The caller must explicitly identify:

- RDF-semantic comparison as the goal;
- the accepted URDNA2015 implementation/version;
- JSON-LD context and document-loading posture;
- network-disabled context resolution or a pinned local context set;
- canonical N-Quads encoding and digest format.

No initial implementation should enable URDNA2015 unless the dependency, context policy, fixtures, and consumers are verified.

### Field inclusion and exclusion

The library must receive a profile or already-prepared canonical body. It must not decide whether signatures, timestamps, paths, attestations, review state, or other fields belong in identity.

```text
contract/profile selects body
        ↓
library canonicalizes selected body
        ↓
library hashes canonical bytes
```

Changing an exclusion list changes identity and therefore requires a versioned migration.

### YAML and non-JSON inputs

YAML is not JCS input. A caller that starts with YAML must use an accepted conversion profile that defines:

- scalar typing;
- duplicate keys;
- anchors and aliases;
- tags;
- merge keys;
- map ordering;
- timestamps and numeric types;
- conversion into a JSON data model.

Without that profile, the library must return `UNSUPPORTED_PROFILE` or equivalent—not invent a conversion.

[Back to top](#top)

---

<a id="hash-family-boundaries"></a>

## Hash-family boundaries

| Family | What may be hashed | Required profile/context | What it never proves |
|---|---|---|---|
| Raw/content digest | Exact supplied bytes | Algorithm and media/input class | Meaning, validity, provenance, or safety |
| `spec_hash` | Canonical trust-bearing body | Canonicalization profile, version, contract/schema identity | Correctness, authority, or release |
| Geometry hash | Accepted normalized geometry | CRS, axis order, precision, normalization profile | Spatial truth or public exposure safety |
| Style hash | Accepted canonical style body and declared dependent refs | Style/profile version and dependency policy | Render correctness or release |
| Artifact hash | Exact artifact bytes | Algorithm and artifact identity | Artifact admissibility or publication |
| Merkle root | Explicit leaf set | Leaf encoding, ordering, tree version, empty/duplicate rules | Release approval |
| Run ID | Accepted canonical run context | Field set and serialization profile | Receipt authority or runtime success |
| OPA/policy bundle digest | Bundle bytes under policy tooling convention | Governing policy contract/tooling | Policy decision for a specific input |

### Raw/content hashing

A raw hashing helper may be implemented before JCS if it is narrowly named and cannot be mistaken for `spec_hash`.

Safe example concept:

```text
hash_bytes(data, algorithm="sha256") -> ContentDigest
```

Unsafe example concept:

```text
hash_anything(value) -> "spec_hash"
```

### Geometry hashing

No `geometry_hash` helper should be exported until the normalization profile answers at least:

- input geometry model and dimensionality;
- CRS and axis order;
- coordinate precision/rounding;
- ring orientation;
- vertex ordering and duplicate points;
- multipart ordering;
- antimeridian behavior;
- empty and invalid geometry behavior;
- sensitivity/generalization boundary.

### Merkle roots

No Merkle helper should become authority-bearing until the contract pins:

- leaf representation;
- path normalization;
- sort order;
- duplicate handling;
- odd-node handling;
- tree-domain separation;
- empty set root;
- algorithm and version;
- inclusion-proof format.

### Run identity

No `run_id` helper should infer identity from wall-clock time, random UUIDs, process IDs, machine names, or storage paths unless those values are explicit governed fields.

[Back to top](#top)

---

<a id="proposed-library-api"></a>

## Proposed library API

The API below is **PROPOSED**. It is an interface target for review, not implementation evidence.

```python
from dataclasses import dataclass
from typing import Literal, Mapping, Sequence

HashAlgorithm = Literal["sha256", "blake3"]
CanonicalizationProfile = Literal["jcs-rfc8785", "urdna2015"]

@dataclass(frozen=True)
class DigestRef:
    family: str
    algorithm: HashAlgorithm
    value_hex: str
    profile: str | None
    profile_version: str | None

@dataclass(frozen=True)
class HashResult:
    outcome: str
    digest: DigestRef | None
    reason_code: str
    details: Mapping[str, str]

def hash_bytes(data: bytes, *, algorithm: HashAlgorithm) -> HashResult:
    ...

def canonicalize_json(value: object, *, profile: str, profile_version: str) -> bytes:
    ...

def compute_canonical_digest(
    value: object,
    *,
    family: str,
    profile: str,
    profile_version: str,
    algorithm: HashAlgorithm,
) -> HashResult:
    ...

def compare_digest_refs(expected: DigestRef, actual: DigestRef) -> HashResult:
    ...
```

### API requirements

- Keyword-only context for profile-sensitive operations.
- Immutable result/value objects.
- No implicit file reads.
- No automatic network or JSON-LD context loading.
- No fallback from unsupported JCS to developer-formatted JSON.
- No fallback from SHA-256 to BLAKE3 or vice versa.
- No automatic conversion between object-wrapped and string digest representations.
- Deterministic exception or result behavior.
- Stable reason codes.
- No sensitive input echo in error messages.
- Optional constant-time digest-byte comparison where threat modeling justifies it.
- Clear separation between parsing, canonicalization, digesting, formatting, and comparison.

### Import surface

Until packaging and exports are ratified, examples such as these remain **PROPOSED**:

```python
from hashing import hash_bytes
from hashing.canonical_json import canonicalize_json
from hashing.compare import compare_digest_refs
```

The empty `__init__.py` currently exports nothing. Consumers must not begin depending on speculative import paths.

[Back to top](#top)

---

<a id="comparison-outcomes-and-reason-codes"></a>

## Comparison outcomes and reason codes

The following namespace-local outcome model is **PROPOSED** and must be reconciled with validators and runtime envelopes before use.

| Outcome | Meaning | Caller posture |
|---|---|---|
| `MATCH` | Compatible representations and digest bytes match. | Continue to independent schema, evidence, policy, and release gates. |
| `MISMATCH` | Compatible representations differ. | Fail closed; record correction/review need. |
| `INVALID_INPUT` | Input cannot be parsed or violates basic type/encoding rules. | Error/invalid validation result. |
| `UNSUPPORTED_PROFILE` | Profile/version is not implemented or accepted. | Abstain/error; never approximate. |
| `PROFILE_MISMATCH` | Values use different canonicalization profiles or versions. | Do not compare as equal. |
| `ALGORITHM_MISMATCH` | Values use different algorithms. | Do not compare as equal unless a governed multi-hash record exists. |
| `FORMAT_MISMATCH` | Wrapper/prefix/value model differs without a ratified adapter. | Require explicit migration/adapter. |
| `CANONICALIZATION_ERROR` | Accepted profile cannot canonicalize the supplied value. | Fail closed. |
| `DRIFT_DETECTED` | Recomputed identity differs from a previously governed reference. | Block dependent gate and initiate correction review. |
| `RESOURCE_LIMIT` | Input exceeds accepted size/depth/time/memory bounds. | Fail closed without exposing input. |
| `DEPENDENCY_UNAVAILABLE` | Required pinned implementation is unavailable. | Error; do not use fallback serialization. |

### Proposed reason codes

```text
HASH_OK
HASH_BYTES_DIFFER
HASH_INPUT_TYPE_INVALID
HASH_INPUT_ENCODING_INVALID
HASH_JSON_DUPLICATE_KEY
HASH_JSON_NUMBER_UNSUPPORTED
HASH_PROFILE_REQUIRED
HASH_PROFILE_UNSUPPORTED
HASH_PROFILE_VERSION_UNSUPPORTED
HASH_PROFILE_MISMATCH
HASH_ALGORITHM_UNSUPPORTED
HASH_ALGORITHM_MISMATCH
HASH_FORMAT_MISMATCH
HASH_CANONICALIZATION_FAILED
HASH_DIGEST_SYNTAX_INVALID
HASH_DIGEST_LENGTH_INVALID
HASH_RESOURCE_LIMIT
HASH_DEPENDENCY_UNAVAILABLE
HASH_DRIFT_DETECTED
```

These are not `PolicyDecision` outcomes and do not authorize release.

[Back to top](#top)

---

<a id="security-and-resource-bounds"></a>

## Security and resource bounds

Hashing and canonicalization code is security-sensitive even when it has no network access.

### Required controls

- No network access during import or function execution.
- No dynamic code evaluation or unsafe deserialization.
- No automatic remote JSON-LD context resolution.
- Explicit maximum input bytes.
- Explicit maximum nesting depth and collection counts.
- Bounded canonical output size.
- Bounded file-set entry count.
- Streaming byte hashing for large artifacts where semantics permit exact bytes.
- No unbounded in-memory archive or filesystem traversal.
- No logging of full sensitive inputs, secrets, bearer tokens, private records, or exact sensitive geometry.
- Dependency pinning, license review, vulnerability scanning, and reproducibility review.
- Side-effect-free imports.
- Deterministic locale/timezone/encoding behavior.
- Clear error handling for malformed Unicode and invalid numeric forms.
- Test denial-of-service cases: deeply nested values, huge keys, many members, repeated strings, and pathological RDF graphs if URDNA2015 is introduced.

### Cryptographic scope exclusions

This package is not approved for:

- password storage;
- password derivation;
- HMAC authentication;
- digital signatures;
- key derivation or encryption;
- secret comparison;
- certificate validation;
- transparency-log operation;
- cryptographic randomness.

Adding any of those concerns requires a new contract, threat model, ownership, tests, and likely a separate package.

[Back to top](#top)

---

<a id="testing-and-parity"></a>

## Testing and parity

### What is currently tested

The existing generic schema fixture harness can validate the **shape** of the current common `spec_hash` object.

It does not prove:

- RFC 8785 canonicalization;
- digest computation;
- profile-qualified formatting;
- parsing or comparison;
- package exports;
- tool/package parity;
- cross-language determinism;
- runtime resource bounds;
- release-gate integration.

### Minimum future package test matrix

| Test family | Required cases |
|---|---|
| Import safety | No network, writes, environment reads, lifecycle reads, or side effects. |
| Raw SHA-256 | Empty bytes, binary bytes, UTF-8 text, large streaming input, mutation mismatch. |
| JCS vectors | Accepted RFC 8785 vectors and implementation-specific regression vectors. |
| Object ordering | Nested keys, Unicode keys, empty structures. |
| Number behavior | Integers, negative zero, exponent forms, precision boundaries, NaN/Infinity rejection. |
| String behavior | Escapes, control characters, Unicode, surrogate/error cases. |
| Parser behavior | Prefix, lowercase hex, length, unknown algorithm/profile, wrapper versions. |
| Format conflict | `jcs:sha256:` versus `{"value":"sha256:"}` cannot silently compare. |
| Profile mismatch | JCS versus URDNA2015 and profile-version mismatches. |
| Drift | Stored versus recomputed mismatch with stable reason. |
| Resource bounds | Size, nesting, member count, output limits. |
| Geometry | Only after accepted geometry profile and fixtures exist. |
| Merkle | Only after leaf/tree contract is pinned. |
| Run ID | Only after field/profile contract is pinned. |
| Tool parity | CLI delegates to package and returns the same digest/result. |
| Cross-language | Same accepted vectors across every supported implementation. |
| Trust anti-collapse | `MATCH` never yields policy/release/evidence approval from package code. |

### Fixture requirements

Fixtures must include:

- source profile/version;
- exact input encoding;
- expected canonical bytes or canonical byte digest;
- expected digest representation;
- expected outcome/reason code;
- provenance for external standard vectors;
- synthetic/public-safe status;
- migration version when representation changes.

Do not use real secrets, private source records, sensitive coordinates, unreleased receipts, or production EvidenceBundles as committed fixtures.

### CI requirements

A future package gate should prove:

1. package build/install succeeds in a clean environment;
2. imports resolve from the installed artifact, not the repository working tree;
3. official and local vectors pass;
4. negative/resource-bound tests pass;
5. tool wrapper parity passes;
6. no import-time side effects occur;
7. schema/contract compatibility matrix is checked;
8. no unapproved dependency or algorithm appears.

A green generic schema-fixture job is not hashing implementation proof.

[Back to top](#top)

---

<a id="compatibility-and-migration"></a>

## Compatibility and migration

### Required governance decision

Before implementation, an ADR or migration note must decide:

- canonical implementation root;
- import package name;
- accepted `spec_hash` semantic and machine shape;
- canonicalization profile field/prefix model;
- whether raw checksums and canonical identity use distinct types;
- whether BLAKE3 is allowed and for which field families;
- adapter behavior for existing objects;
- compatibility duration and consumer migration;
- correction and rollback strategy.

### Safe compatibility model

A possible **PROPOSED** versioned model is:

```text
CanonicalDigestRef
├── family
├── algorithm
├── profile
├── profile_version
└── value_hex
```

External adapters may then render accepted versioned shapes without losing information.

Do not adopt this model by README alone. It requires contract/schema/fixture/validator changes.

### Migration rules

- Never rewrite stored hashes in place.
- Preserve original representation and governing schema version.
- Recompute from original governed input when possible.
- Record old and new values plus adapter/profile versions in caller-owned correction/migration receipts.
- Treat unresolvable original bytes/profile as `UNKNOWN` or `NEEDS VERIFICATION`, not a successful conversion.
- Update contracts, schemas, fixtures, validators, docs, consumers, and release gates in one governed plan.
- Maintain rollback to the previous parser/formatter during the compatibility window.
- Remove adapters only after repository-wide consumer search and release review.

[Back to top](#top)

---

<a id="smallest-sound-implementation-sequence"></a>

## Smallest sound implementation sequence

### Phase 0 — governance freeze

1. Assign owners.
2. Record the package-versus-tool decision.
3. Resolve or formally version the `spec_hash` shape conflict.
4. Pin the initial runtime, build backend, dependency policy, and supported profile.
5. Define compatibility and rollback.

**Stop condition:** no implementation if the hash representation or canonical implementation owner remains ambiguous.

### Phase 1 — package shell

1. Complete `pyproject.toml` with build backend, Python range, package discovery, dependencies, and metadata.
2. Keep `__init__.py` minimal.
3. Add typed immutable result/value models.
4. Add package-specific test and fixture roots.
5. Prove installed-package imports.

### Phase 2 — narrow byte digest

1. Implement exact-byte SHA-256 only.
2. Add parsing/formatting for the accepted raw/content digest type.
3. Add resource bounds and streaming tests.
4. Do not call it `spec_hash`.

### Phase 3 — one accepted canonical profile

1. Pin an RFC 8785 implementation.
2. Add official and project vectors.
3. Implement one versioned JCS profile.
4. Implement canonical digest creation only for the accepted contract shape.
5. Fail on unsupported representations rather than adapting silently.

### Phase 4 — comparison and drift

1. Add representation compatibility checks.
2. Compare algorithm/profile/version before bytes.
3. Add typed outcomes and reason codes.
4. Add replay/drift fixtures.
5. Keep gate consequences outside the package.

### Phase 5 — thin tool adapter

1. Make `tools/spec_hash/` import the package.
2. Add machine-readable dry-run output.
3. Prove CLI/library parity.
4. Do not duplicate canonicalization code.

### Phase 6 — governed consumers

1. Inventory consumers.
2. Migrate one fixture-only consumer.
3. Add receipts/correction behavior in the consumer’s owning lane.
4. Add CI and release checks.
5. Expand only after parity and rollback drills pass.

[Back to top](#top)

---

<a id="definition-of-done"></a>

## Definition of done

### Governance

- [ ] Owners are assigned.
- [ ] Directory Rules placement is affirmed.
- [ ] Package/tool ownership is resolved.
- [ ] `spec_hash` representation conflict is resolved or versioned.
- [ ] Algorithm/profile vocabulary is accepted.
- [ ] Compatibility, correction, deprecation, and rollback are documented.

### Package

- [ ] Build metadata is complete.
- [ ] Clean-environment install succeeds.
- [ ] Public exports are minimal and documented.
- [ ] Imports have no side effects.
- [ ] No network, lifecycle access, secret access, or authority writes occur.
- [ ] Dependencies are pinned and reviewed.
- [ ] Resource limits are explicit.

### Correctness

- [ ] Accepted JCS vectors pass.
- [ ] Number and Unicode edge cases pass.
- [ ] Raw byte hashing is exact and streaming-capable.
- [ ] Representation/profile/algorithm mismatches fail closed.
- [ ] Tool and package outputs are byte-identical.
- [ ] Cross-language parity is proven where multiple implementations exist.
- [ ] Existing schema fixture tests still pass after any migration.

### Trust boundary

- [ ] Package results cannot approve policy, evidence, promotion, release, or public output.
- [ ] Receipts/proofs/releases remain caller-owned.
- [ ] Hash input is not logged.
- [ ] Sensitive and secret fixtures are prohibited.
- [ ] Stored values are recomputed at governed boundaries.
- [ ] Rollback is tested.

[Back to top](#top)

---

<a id="verification-register"></a>

## Verification register

| ID | Verification item | Status |
|---|---|---|
| HASH-OPEN-01 | Assign package and canonicalization owners. | NEEDS VERIFICATION |
| HASH-OPEN-02 | Ratify `packages/hashing/` as canonical reusable implementation home. | NEEDS VERIFICATION |
| HASH-OPEN-03 | Classify `tools/spec_hash/` as CLI adapter, legacy lane, or alternate owner. | NEEDS VERIFICATION |
| HASH-OPEN-04 | Decide the canonical import name. | NEEDS VERIFICATION |
| HASH-OPEN-05 | Complete build backend and package discovery metadata. | NEEDS VERIFICATION |
| HASH-OPEN-06 | Pin supported Python version. | NEEDS VERIFICATION |
| HASH-OPEN-07 | Pin RFC 8785 implementation and version. | NEEDS VERIFICATION |
| HASH-OPEN-08 | Decide whether URDNA2015 is implemented initially. | NEEDS VERIFICATION |
| HASH-OPEN-09 | Reconcile `jcs:sha256:` doctrine with `sha256:` object schema. | NEEDS VERIFICATION |
| HASH-OPEN-10 | Decide whether profile belongs in prefix, field, wrapper, or contract version. | NEEDS VERIFICATION |
| HASH-OPEN-11 | Separate raw checksum and canonical identity types. | NEEDS VERIFICATION |
| HASH-OPEN-12 | Define approved BLAKE3 scope. | NEEDS VERIFICATION |
| HASH-OPEN-13 | Define parsing and formatting compatibility versions. | NEEDS VERIFICATION |
| HASH-OPEN-14 | Define duplicate-key handling. | NEEDS VERIFICATION |
| HASH-OPEN-15 | Define JSON numeric acceptance and failure behavior. | NEEDS VERIFICATION |
| HASH-OPEN-16 | Define Unicode and malformed-string behavior. | NEEDS VERIFICATION |
| HASH-OPEN-17 | Define maximum input size and nesting depth. | NEEDS VERIFICATION |
| HASH-OPEN-18 | Define canonical output/resource bounds. | NEEDS VERIFICATION |
| HASH-OPEN-19 | Define exception versus result-object policy. | NEEDS VERIFICATION |
| HASH-OPEN-20 | Ratify outcome and reason-code vocabulary. | NEEDS VERIFICATION |
| HASH-OPEN-21 | Define constant-time comparison requirements. | NEEDS VERIFICATION |
| HASH-OPEN-22 | Pin geometry normalization contract before geometry hashing. | NEEDS VERIFICATION |
| HASH-OPEN-23 | Pin Merkle leaf/tree contract before Merkle exports. | NEEDS VERIFICATION |
| HASH-OPEN-24 | Pin run-id field/profile contract before run-id exports. | NEEDS VERIFICATION |
| HASH-OPEN-25 | Inventory all current digest producers and consumers. | NEEDS VERIFICATION |
| HASH-OPEN-26 | Inventory existing stored digest formats. | NEEDS VERIFICATION |
| HASH-OPEN-27 | Add official JCS vectors and provenance. | NEEDS VERIFICATION |
| HASH-OPEN-28 | Add package-specific positive and negative fixtures. | NEEDS VERIFICATION |
| HASH-OPEN-29 | Add installed-package tests. | NEEDS VERIFICATION |
| HASH-OPEN-30 | Implement or retire the dedicated validator placeholder. | NEEDS VERIFICATION |
| HASH-OPEN-31 | Add package/tool parity tests. | NEEDS VERIFICATION |
| HASH-OPEN-32 | Add resource-exhaustion tests. | NEEDS VERIFICATION |
| HASH-OPEN-33 | Add secret/logging tests. | NEEDS VERIFICATION |
| HASH-OPEN-34 | Add package-specific CI. | NEEDS VERIFICATION |
| HASH-OPEN-35 | Define correction records for representation migration. | NEEDS VERIFICATION |
| HASH-OPEN-36 | Define compatibility window and deprecation criteria. | NEEDS VERIFICATION |
| HASH-OPEN-37 | Run rollback drill. | NEEDS VERIFICATION |
| HASH-OPEN-38 | Verify no caller treats `MATCH` as release or truth authority. | NEEDS VERIFICATION |

[Back to top](#top)

---

<a id="rollback-correction-and-deprecation"></a>

## Rollback, correction, and deprecation

### Documentation rollback

This revision changes only:

```text
packages/hashing/src/hashing/README.md
```

Prior blob:

```text
0398cc127ddcdf6e37f47882a02f11443f884682
```

Restore that blob or revert the documentation commit if the revised boundary is rejected.

### Future implementation rollback triggers

Rollback or disable the implementation if it:

- emits a representation that contradicts the accepted schema/contract;
- silently strips, inserts, or changes canonicalization profiles;
- substitutes sorted JSON for RFC 8785 while labeling it JCS;
- changes digest algorithms without a versioned migration;
- creates separate package and tool implementations that drift;
- compares incompatible profiles as equal;
- reads network, lifecycle stores, secrets, or hidden ambient state;
- writes receipts, proofs, release records, policy decisions, or published artifacts;
- logs sensitive hash inputs;
- treats `MATCH` as truth, evidence closure, policy approval, or release approval;
- exceeds accepted resource bounds without deterministic failure.

### Correction posture

A corrected hash is a new governed result, not an in-place truth rewrite.

Caller-owned correction records should preserve:

- original input reference and representation;
- original algorithm/profile/version;
- original digest;
- corrected algorithm/profile/version;
- corrected digest;
- reason for correction;
- implementation and dependency versions;
- validation evidence;
- affected consumers and release targets;
- rollback target.

### Deprecation posture

Do not deprecate the old representation until:

1. consumer inventory is complete;
2. migration adapters are tested;
3. old and new values can be independently recomputed;
4. release/rollback paths are updated;
5. the compatibility window has elapsed;
6. removal is approved through the owning governance process.

---

## Status summary

`packages/hashing/src/hashing/` is a repository-present but effectively empty namespace for a future reusable hashing library. The smallest sound next change is not broad implementation: it is an ADR or migration decision that reconciles package/tool ownership and the conflicting `spec_hash` representations, followed by one fixture-tested JCS/SHA-256 profile and a thin tool adapter.

<p align="right"><a href="#top">Back to top</a></p>
