<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-identity-src-identity-readme
title: packages/identity/src/identity/ — Deterministic Identity Namespace and Compatibility Boundary
type: readme
version: v1.1
status: draft
owners: OWNER_TBD — Package steward · Identity steward · Contract steward · Schema steward · Domain stewards · Privacy reviewer · Sensitivity reviewer · Security steward · Validation steward · Migration steward · CI steward · Docs steward
created: NEEDS VERIFICATION — target existed before the current evidence-grounded revision
updated: 2026-07-15
policy_label: "public-doctrine; package-boundary; import-namespace; deterministic-identity; implementation-empty; api-unratified; grammar-profile-unsettled; identity-token-separated; domain-identity-separated; run-id-separated; hashing-delegated; non-credential; no-network; pure-functions; fail-closed; privacy-aware; no-authority; no-secrets; migration-required; rollback-aware"
current_path: packages/identity/src/identity/README.md
truth_posture: CONFIRMED target README v1, parent package/source READMEs, empty identity package initializer, kfm-identity 0.0.0 placeholder metadata, packages and Directory Rules placement, merged hashing package boundary v1.1, draft IdentityToken contract v0.3 and PROPOSED schema, missing declared IdentityToken validator and fixture root at bounded paths, README-only Identity validator routing lane, placeholder identity validator modules, PROPOSED ADR-0013, draft identity/evidence architecture notes, confirmed EvidenceRef contract, representative domain-owned Fauna identity contract, and bounded absence of proposed namespace modules, package-specific tests/workflows, and executable consumers / PROPOSED profile-bound identifier parsing and formatting, typed identity-token adapters, explicit collision-scope checks, alias/supersession/tombstone relation helpers, finite outcomes and reason codes, privacy/resource controls, package/hash delegation, tests, staged implementation, correction, migration, deprecation, and rollback / CONFLICTED common identity_token object versus generic identifier-token string terminology, stable referenced-object identity versus issued token-instance identity, universal KFM ID grammar proposals versus unconstrained common schema id and domain-owned identity semantics, proposed ADR run_id grammar versus unaccepted implementation, generic identity namespace versus domain-specific sameness rules, and rich documentation versus empty implementation / UNKNOWN accepted identifier-profile registry, namespace grammar, normalization rules, package discovery, Python runtime, dependency set, export surface, consumer inventory beyond bounded search, collision authority, resolver behavior, cross-language parity, package tests, CI enforcement, release use, and operational health / NEEDS VERIFICATION owners, accepted ADR or migration decision, identity-profile vocabulary, common/domain boundary, package metadata, API shape, privacy review, test vectors, collision-scope contract, consumer migration, CI gates, correction path, compatibility period, deprecation, and rollback automation
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 49392f54b1e994164000c083366daddf68a6a38a
  prior_blob: 15cf581d868819d5ff4cd5cb25e2908fe1717a3d
  package_readme_blob: ba5f4c0b3e425448906acc6e5e393eefce60ab8b
  source_readme_blob: 4f630edb84ee6d35ee447f779f0798924b2ef513
  package_metadata_blob: 2cf2870a24aad30a34d6b76e67c21315b99f3514
  namespace_initializer_blob: e69de29bb2d1d6434b8b29ae775ad8c2e48c5391
  hashing_package_readme_blob: 3d3174974668623117c1f90bcbc6918262d1b6af
  packages_root_blob: fc18fb3334fefe992a551fe12aa98c812232cd17
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  identity_token_contract_blob: 745bb43868afe132c7d6bac79fa210d620ccdba1
  identity_token_schema_blob: f3eace84a75c2dd97cfabfa7661a098e4353e825
  identity_validator_readme_blob: cbeb616f6dee0967a84dc1a1285b195ee2324972
  identity_jcs_placeholder_blob: 15e4eb31b683af500071e82bfca0407b922be44e
  evidence_identity_validator_placeholder_blob: b2fe2c525028cdd9550fdae143a446885871f3f4
  adr_0013_blob: 528ff0db1db14af43fd3c2867fd9af316c85910e
  identity_architecture_blob: d8b3836bae160ac0f2027407989d383fa016a49b
  evidence_identity_architecture_blob: 5e6b855472a5527e6875e19a2d023494826c1e09
  evidence_ref_contract_blob: 0f337cf07d44224c31329c8eced90d4dddccef87
  fauna_identity_contract_blob: 35c98d6e01afa597c0ddcadc3ac7b92b8dcdb6aa
  bounded_path_checks:
    - packages/identity/src/identity/README.md existed at version v1 before this revision
    - packages/identity/src/identity/__init__.py exists and is empty
    - packages/identity/pyproject.toml contains only project name kfm-identity and version 0.0.0
    - grammar.py, namespaces.py, object_id.py, refs.py, lineage.py, validation.py, token_string.py, and fixtures.py were not found under packages/identity/src/identity/
    - packages/identity/tests/README.md and tests/packages/identity/README.md were not found
    - .github/workflows/identity.yml and package-identity.yml were not found
    - tools/validators/validate_identity_token.py was not found
    - fixtures/contracts/v1/common/identity_token/README.md was not found
    - tools/validators/identity/jcs_spec_hash.py is a documentation-only placeholder
    - tools/validators/evidence/validate_identity.py is a documentation-only placeholder
    - bounded code search did not establish an executable consumer importing the identity package
related:
  - ../../README.md
  - ../README.md
  - __init__.py
  - ../../pyproject.toml
  - ../../../README.md
  - ../../../hashing/README.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../docs/adr/ADR-0013-spec_hash-and-run_id-identity-grammar.md
  - ../../../../docs/architecture/identity-and-spec-hash.md
  - ../../../../docs/architecture/evidence-identity.md
  - ../../../../contracts/common/identity_token.md
  - ../../../../schemas/contracts/v1/common/identity_token.schema.json
  - ../../../../contracts/evidence/evidence_ref.md
  - ../../../../contracts/domains/fauna/domain_feature_identity.md
  - ../../../../contracts/domains/hydrology/reach_identity.md
  - ../../../../contracts/domains/settlements-infrastructure/place-identity.md
  - ../../../../tools/validators/identity/README.md
  - ../../../../tools/validators/identity/jcs_spec_hash.py
  - ../../../../tools/validators/evidence/validate_identity.py
tags: [kfm, packages, identity, deterministic-identity, identity-token, identifier-profile, object-id, run-id, reference, alias, supersession, tombstone, collision, domain-identity, hashing, privacy, compatibility, migration, fail-closed]
notes:
  - "This revision changes only packages/identity/src/identity/README.md."
  - "The namespace currently contains this README and an empty __init__.py; proposed helper modules were not found at the checked paths."
  - "This README does not activate an API, select a universal identifier grammar, accept ADR-0013, define domain sameness, create a collision registry, or authorize package distribution."
  - "The common identity_token object, identifier strings, stable object ids, run ids, evidence/source/release references, aliases, and domain feature identities remain separate governed profiles."
  - "A well-formed identifier is not object existence, person identity, evidence closure, policy approval, release approval, or public safety."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Deterministic Identity Namespace and Compatibility Boundary

`packages/identity/src/identity/`

> Repository-present import namespace for a future reusable deterministic identity library. Current evidence establishes a README and an empty initializer—not an exported ID grammar, token implementation, resolver, collision service, tested package, or CI-enforced identity subsystem.

![status](https://img.shields.io/badge/status-draft-yellow)
![version](https://img.shields.io/badge/version-v1.1-informational)
![maturity](https://img.shields.io/badge/maturity-empty__namespace-lightgrey)
![grammar](https://img.shields.io/badge/grammar-profile__unsettled-orange)
![identity token](https://img.shields.io/badge/identity__token-typed__reference-blue)
![credentials](https://img.shields.io/badge/credentials-DENIED-critical)
![network](https://img.shields.io/badge/network-none-critical)
![authority](https://img.shields.io/badge/truth__authority-none-red)

**Quick links:** [Purpose](#purpose) · [Evidence](#status-and-evidence) · [Placement](#directory-rules-and-authority) · [Profiles](#identity-profile-separation) · [Conflicts](#compatibility-conflicts) · [Invariants](#keystone-invariants) · [Tree](#confirmed-and-proposed-namespace-tree) · [Inputs](#explicit-input-contract) · [Token](#identity-token-profile) · [IDs](#identifier-text-and-object-id-profiles) · [References](#reference-and-lineage-profiles) · [Hash/run](#hashing-and-run-id-boundary) · [API](#proposed-library-api) · [Outcomes](#outcomes-and-reason-codes) · [Security](#security-privacy-and-resource-bounds) · [Testing](#testing-and-parity) · [Migration](#compatibility-and-migration) · [Implementation](#smallest-sound-implementation-sequence) · [Done](#definition-of-done) · [Open](#verification-register) · [Rollback](#rollback-correction-and-deprecation)

> [!IMPORTANT]
> **This README is not an API, identity grammar, resolver, registry, or migration decision.** It does not establish exports, a universal KFM identifier syntax, accepted normalization rules, collision authority, domain sameness, an accepted `run_id` grammar, package discovery, CI enforcement, or operational consumers.

> [!CAUTION]
> **A valid identifier is not proof of identity or truth.** It establishes only local conformance to a declared profile. Object existence, actor identity, source authority, evidence support, rights, sensitivity, policy, review, release, and public safety remain separate governed checks.

---

<a id="purpose"></a>

## Purpose

This README defines the allowed boundary for a future importable `identity` helper namespace inside the shared [`packages/`](../../../README.md) responsibility root.

A conforming library may eventually:

- parse and format identifiers under an explicit, versioned identity profile;
- preserve original text separately from any normalized representation;
- validate profile-specific syntax, kind, namespace, length, and reserved values;
- construct the current common `identity_token` object from explicit fields;
- compare candidate identifiers within an explicit caller-supplied collision scope;
- represent alias, supersession, correction, tombstone, and migration relations from explicit audit-backed inputs;
- accept digest values from [`packages/hashing/`](../../../hashing/README.md) without reimplementing hash semantics;
- return deterministic typed results and stable reason codes;
- support governed callers without owning registries, resolvers, records, policy, or release.

It must not:

- invent a universal grammar from examples or prose;
- treat the common `identity_token` object as a generic string token;
- collapse stable object identity, activity identity, content identity, and reference identity;
- derive domain object sameness without a domain contract and profile;
- silently normalize, repair, suffix, retarget, merge, or migrate identifiers;
- scan or mutate a registry to establish uniqueness;
- resolve identities over the network;
- issue credentials, sessions, API keys, bearer tokens, permissions, consent, or authentication assertions;
- match people, infer ownership, infer kinship, resolve DNA/genomic identity, or publish sensitive actor/location identifiers;
- write lifecycle data, source descriptors, receipts, proofs, catalogs, releases, corrections, or public payloads.

[Back to top](#top)

---

<a id="status-and-evidence"></a>

## Status and evidence

| Surface | Status | Safe conclusion |
|---|---:|---|
| This README | **CONFIRMED v1 before revision** | A namespace guide exists. |
| `identity/__init__.py` | **CONFIRMED empty** | No public exports, import behavior, or side effects are established. |
| `kfm-identity` metadata | **CONFIRMED `0.0.0` placeholder** | A distribution name exists; build backend, source discovery, dependencies, and installability are not established. |
| Proposed namespace modules | **NOT FOUND at bounded paths** | No grammar, namespace, object-ID, reference, lineage, validation, or fixture implementation is established. |
| Package-specific tests | **NOT FOUND at checked README paths** | No dedicated identity-package test boundary is established. |
| Package-specific workflows | **NOT FOUND at checked paths** | No dedicated identity CI behavior is established. |
| Executable consumers | **NOT ESTABLISHED by bounded search** | Search found documentation/contracts/placeholders, not proven imports of this package. |
| Common `identity_token` contract | **CONFIRMED draft v0.3** | Defines a small typed reference object, explicitly not a credential or proof of identity. |
| Common `identity_token` schema | **CONFIRMED `PROPOSED` machine surface** | Requires `id`, `kind`, and `issued_at`; `issuer` is optional; `id` has no grammar pattern. |
| Declared IdentityToken validator | **NOT FOUND** | Schema metadata does not prove executable validation. |
| Declared IdentityToken fixture root | **NOT FOUND at checked README path** | No package or common fixture coverage is established. |
| Identity validator routing lane | **CONFIRMED README-only boundary** | Broad validation responsibilities are documented; runtime wiring remains unproved. |
| Identity validator modules checked | **CONFIRMED placeholders** | They contain provenance comments, not validation behavior. |
| ADR-0013 | **CONFIRMED `proposed`** | Proposes `spec_hash` and `run_id` grammar; it is not an accepted implementation fact. |
| EvidenceRef contract | **CONFIRMED draft/profiled contract** | Evidence references remain evidence-owned pointers, not generic identity-token aliases. |
| Representative Fauna identity contract | **CONFIRMED draft/domain-owned** | Domain sameness preserves source role, object family, time, support, evidence, sensitivity, and lineage. |
| Hashing package boundary | **CONFIRMED v1.1 documentation** | Digest/canonicalization semantics remain delegated; implementation is still empty/unratified. |

### Truth posture

**CONFIRMED**

- The namespace is effectively empty.
- The package metadata is a greenfield placeholder.
- The common `identity_token` is an object, not a credential and not a generic token string.
- Its current schema does not constrain `id` to a universal grammar.
- The current `kind` enum is closed to `run`, `source`, `decision`, `review`, `bundle`, and `actor`.
- ADR-0013 is proposed.
- Domain identity semantics exist outside this common package.
- Checked identity validators are missing or placeholder-only.

**PROPOSED**

- The profile-bound API, result types, reason codes, collision-scope interface, lineage relations, privacy/resource limits, tests, implementation sequence, migration procedure, and rollback procedure below.

**CONFLICTED**

- The phrase “identity token” as a typed object versus “identifier token” as a generic string.
- Stable referenced-object identity versus the issuance identity of an `identity_token` instance.
- Proposed universal KFM ID grammar versus an unconstrained common `id` field and domain-specific identity contracts.
- Proposed `run_id` grammar versus an unaccepted ADR and no executable implementation.
- Common-library convenience versus domain-owned definitions of sameness.
- Generic import namespace `identity` versus unratified package discovery and possible naming collisions.
- Digest-bearing identifiers versus unresolved canonical hash representation in the hashing/contract surfaces.
- Rich documentation versus no verified library behavior.

**UNKNOWN**

- Accepted identifier profiles; normalization rules; namespace registry; collision authority; Python/runtime support; package discovery; dependencies; exports; resolvers; consumers; performance; cross-language parity; CI enforcement; deployment use; and operational health.

**NEEDS VERIFICATION**

- Owners; accepted ADR/profile decisions; common-versus-domain scope; package metadata; API naming; privacy review; collision scope; test vectors; consumers; CI gates; compatibility period; migration; correction; deprecation; and rollback automation.

[Back to top](#top)

---

<a id="directory-rules-and-authority"></a>

## Directory Rules and authority

The owning root is [`packages/`](../../../README.md) because this namespace is intended for reusable implementation helpers. The parent boundaries are:

- [`packages/identity/README.md`](../../README.md) — package mechanics and package-wide responsibility;
- [`packages/identity/src/README.md`](../README.md) — source placement, dependency direction, and implementation conditions;
- this README — proposed import behavior and compatibility safeguards;
- [`identity/__init__.py`](__init__.py) — currently empty export boundary;
- [`pyproject.toml`](../../pyproject.toml) — currently only `kfm-identity` / `0.0.0` placeholder metadata.

### Authority matrix

| Concern | Authority home | Namespace posture |
|---|---|---|
| Common identity-token meaning | [`contracts/common/identity_token.md`](../../../../contracts/common/identity_token.md) | Adapt, never redefine. |
| Common identity-token shape | [`schemas/contracts/v1/common/identity_token.schema.json`](../../../../schemas/contracts/v1/common/identity_token.schema.json) | Validate through accepted schema tooling; do not invent fields. |
| Evidence pointer meaning | [`contracts/evidence/evidence_ref.md`](../../../../contracts/evidence/evidence_ref.md) | Parse/format only under its profile; do not create closure. |
| Domain object sameness | Domain contracts, such as [`Fauna DomainFeatureIdentity`](../../../../contracts/domains/fauna/domain_feature_identity.md) | Domain-owned; common package must not flatten. |
| Hash/canonicalization semantics | [`packages/hashing/`](../../../hashing/README.md), standards, accepted ADRs | Consume explicit digest/profile values. |
| Proposed `spec_hash` / `run_id` grammar | [`ADR-0013`](../../../../docs/adr/ADR-0013-spec_hash-and-run_id-identity-grammar.md) | Treat as proposed until accepted. |
| Identity/evidence architecture | [`identity-and-spec-hash.md`](../../../../docs/architecture/identity-and-spec-hash.md), [`evidence-identity.md`](../../../../docs/architecture/evidence-identity.md) | Architecture context, not executable API proof. |
| Validator routing | [`tools/validators/identity/README.md`](../../../../tools/validators/identity/README.md) | Validators call library helpers; validators own reports, not meaning. |
| Source registries | `data/registry/` | No read/write authority by default. |
| Policy, sensitivity, public exposure | `policy/` and governed review/release surfaces | Namespace does not decide. |
| Receipts and proofs | `data/receipts/`, `data/proofs/` | Namespace returns values; does not persist authority. |
| Release, correction, rollback | `release/` | Namespace may preserve references; it does not approve transitions. |
| Credentials and secrets | secure auth/infra systems | Explicitly out of scope. |

### Directory invariant

```text
contracts/ define meaning
schemas/   define shape
policy/    defines admissibility and exposure
data/      holds lifecycle state and trust artifacts
release/   governs publication, correction, and rollback
packages/  implements reusable helpers
tools/     validates, reports, and operates
apps/      expose governed interfaces
```

No file created under this namespace may become a parallel contract, profile registry, source registry, resolver database, identity-provider store, proof store, or release authority.

[Back to top](#top)

---

<a id="identity-profile-separation"></a>

## Identity profile separation

“Identity” names several different concerns. A safe implementation must require the caller to select the relevant profile instead of guessing from a string.

| Profile | Identifies | Current authority | Must remain separate from |
|---|---|---|---|
| Common `identity_token` | A typed issued reference object | Common contract/schema | Generic token string, credential, object payload |
| Identifier text | A string interpreted under a named grammar | Owning contract/profile | Universal implicit grammar |
| Stable object ID | One domain or object-family entity | Domain/common object contract | Token issuance event, run, content hash |
| `run_id` | One governed execution/activity | Proposed ADR/runtime contracts | Stable object ID and `spec_hash` |
| `spec_hash` / content digest | Canonical content or bytes | Hashing package/contracts/standards | Object existence, source authority, token |
| EvidenceRef | Governed evidence pointer | Evidence contract/schema | EvidenceBundle closure, generic reference |
| Source reference | Source/source-descriptor pointer | Source contracts/registry | Source authority itself |
| Receipt/review/decision reference | Governance-record pointer | Owning record contracts | Policy/release outcome |
| Release/rollback/correction reference | Governed transition pointer | Release contracts | Transition approval |
| Alias/supersession relation | Auditable relation between identifiers | Owning contract/receipt/release | Silent retargeting |
| Actor reference | Governed actor pointer | Actor/governance contracts and policy | Authentication, personhood proof, public display permission |
| Domain feature identity | Domain-specific sameness relation | Domain contract/schema/policy | Universal package-level object ID |

### Selection rule

A future parser should require an explicit `profile_id` or a typed entry point. It must not:

1. inspect punctuation and guess an identity family;
2. assume every `kfm://` string shares the same grammar;
3. treat every `id` field as interchangeable;
4. infer domain object identity from source-native keys alone;
5. infer token kind from identifier text;
6. infer public safety from successful parsing.

[Back to top](#top)

---

<a id="compatibility-conflicts"></a>

## Compatibility conflicts

These conflicts are publication blockers for a universal API.

### 1. `identity_token` object versus identifier token string

The common schema defines:

```json
{
  "id": "src-usgs-ngmdb",
  "kind": "source",
  "issued_at": "2026-06-20T21:00:00Z",
  "issuer": "kfm-source-registry"
}
```

The previous README also proposed `make_identifier_token()` for a string segment. These are different concepts:

- **IdentityToken** — an issued, typed reference object.
- **Identifier text/token segment** — a non-secret string interpreted under a profile.

The word `token` must never let one silently substitute for the other.

### 2. Stable object identity versus token issuance identity

`identity_token.issued_at` is token issuance time. It is not:

- source observation time;
- object valid time;
- record creation time;
- activity/run time;
- release time;
- identity birth time.

Reissuing a token for the same referenced object may produce a different token instance without changing the referenced object ID.

### 3. Common schema versus universal grammar

The common schema currently declares `id` as `type: string` with no pattern. Therefore:

- the schema does not prove `kfm://...` is universally required;
- it does not prove slug, separator, case, Unicode, length, or percent-encoding rules;
- it does not prove source IDs, EvidenceRefs, run IDs, domain IDs, and release refs share a grammar.

A package implementation must use versioned profiles and abstain when a profile is missing.

### 4. Proposed ADR versus accepted behavior

ADR-0013 proposes:

```text
jcs:sha256:<64-lowercase-hex>
run:<orchestrator>:<ULID>
```

The ADR status is `proposed`. The namespace must not expose these as accepted defaults until governance confirms:

- ADR acceptance or supersession;
- controlled orchestrator vocabulary;
- ULID dependency and monotonicity policy;
- compatibility handling;
- fixtures and cross-language vectors;
- interaction with OpenLineage identifiers.

### 5. Common helper versus domain sameness

Domain identity is not just syntax. Representative Fauna doctrine preserves:

- source and source role;
- object family and feature role;
- taxon or subject scope;
- temporal scope;
- support/spatial scope;
- normalized digest;
- evidence, sensitivity, correction, and rollback context.

Other domains may use different identity-defining dimensions. The common namespace may host reusable parsing/result primitives, but domain packages and contracts must supply the identity recipe.

### 6. Digest-bearing IDs versus hash vocabulary

Identifiers may carry or reference digests, but digest meaning belongs to the hashing boundary. The identity namespace must not:

- remove canonicalization prefixes;
- convert bare `sha256:` into `jcs:sha256:` by assumption;
- replace SHA-256 with BLAKE3;
- recompute a digest unless explicitly delegated;
- treat a digest as object identity without an owning profile.

### 7. Import-name compatibility

The distribution placeholder is `kfm-identity`; the proposed import namespace is `identity`. Package discovery is unconfigured. Before ratification, governance must check:

- top-level module collisions;
- external dependency conflicts;
- workspace/import conventions;
- editable and isolated installs;
- public API naming;
- consumer migration cost.

[Back to top](#top)

---

<a id="keystone-invariants"></a>

## Keystone invariants

1. **Profile required.** Every identifier operation uses an explicit, accepted profile.
2. **Original preserved.** Parsing preserves the original input separately from normalized/profile output.
3. **No silent repair.** Invalid input remains invalid; no trimming, case folding, suffixing, or separator replacement without an explicit transform result.
4. **Token object separated.** `identity_token` is never treated as a generic string or credential.
5. **Activity separated.** `run_id` never substitutes for stable object identity or content identity.
6. **Content separated.** `spec_hash` and content digests remain hashing-owned.
7. **Domain sameness preserved.** Common helpers never overwrite domain identity semantics.
8. **Collision scope explicit.** Collision checks use a caller-supplied finite scope; package code does not claim global uniqueness.
9. **Reserved values fail closed.** Reserved namespaces, kinds, prefixes, or profiles do not auto-map.
10. **Lineage explicit.** Alias, supersession, correction, tombstone, and rollback relations are separate auditable objects.
11. **No implicit resolution.** Parsing does not prove the referenced object exists.
12. **No credential semantics.** Identifier tokens are not authentication or authorization material.
13. **Privacy remains external and binding.** A syntactically valid actor/location/property identifier may still be restricted or denied.
14. **No network and no ambient stores.** Helpers operate on supplied values only.
15. **Deterministic outcomes.** Same accepted profile and same inputs yield the same result.
16. **Finite reasons.** Failures return stable reason codes rather than prose-only warnings.
17. **Hash equality is not truth.** Digest or ID equality does not prove evidence, authority, or release.
18. **Migration is governed.** Grammar/profile changes require versioning, compatibility tests, correction, and rollback.
19. **Public clients stay outside.** Normal UI/API surfaces consume governed envelopes, not package internals.
20. **Cite or abstain.** When profile, scope, authority, or sensitivity is unresolved, return a bounded failure or abstention.

[Back to top](#top)

---

<a id="confirmed-and-proposed-namespace-tree"></a>

## Confirmed and proposed namespace tree

### Confirmed tree

```text
packages/identity/
├── README.md
├── pyproject.toml                 # kfm-identity / 0.0.0 placeholder
└── src/
    ├── README.md
    └── identity/
        ├── README.md              # this file
        └── __init__.py            # empty
```

No other implementation module is established by current bounded checks.

### Proposed minimal decomposition

The following is **PROPOSED**, not a file-creation instruction or implementation fact:

```text
packages/identity/src/identity/
├── README.md
├── __init__.py                    # intentionally small export boundary
├── profiles.py                    # accepted profile descriptors; no registry authority
├── identifiers.py                 # profile-bound parse/format/value objects
├── identity_token.py              # adapter for current common token object
├── references.py                  # explicit reference profiles only
├── lineage.py                     # alias/supersession/tombstone relation values
├── results.py                     # finite outcomes and reason codes
└── limits.py                      # deterministic input/resource bounds
```

Initial implementation should **not** add:

- a default universal `grammar.py`;
- an ambient registry client;
- a global collision database;
- `run_id.py` before ADR acceptance;
- domain-feature identity recipes;
- credential/session/token code;
- production fixture generators;
- filesystem/network resolvers.

[Back to top](#top)

---

<a id="explicit-input-contract"></a>

## Explicit input contract

All functions accept explicit, inspectable inputs.

| Input family | Required fields or context | Required posture |
|---|---|---|
| Profile selection | `profile_id`, `profile_version`, accepted grammar/rules | Required; no syntax guessing |
| Identifier text | original string, encoding, profile | Preserve original; reject unsupported encoding/profile |
| IdentityToken payload | `id`, `kind`, `issued_at`, optional `issuer` | Follow current contract/schema exactly |
| Object identity context | domain, object family, role, source/source role, temporal/spatial scope, digest/profile refs | Domain profile owns sameness |
| Reference context | reference family, target kind, owning contract version | Parse/format only; no existence claim |
| Collision context | explicit finite candidate set or supplied index snapshot and snapshot ID | No global scan or mutation |
| Lineage context | prior/current IDs, relation kind, reason/evidence/review/correction refs, effective time | Audit-backed; cycle checked |
| Hash context | digest string/value object, canonicalization profile, algorithm | Supplied by hashing/caller |
| Run context | orchestrator vocabulary, ULID/UUID policy, accepted ADR/profile | Unsupported until accepted |
| Sensitivity context | audience, policy/sensitivity references, redaction state where needed | Package reports requirement; policy decides |
| Limits | maximum bytes, segments, aliases, relations, recursion/cycle depth | Explicit or accepted safe defaults |
| Clock context | explicit `issued_at` or injected clock policy | No ambient time in deterministic builders |
| Fixture context | synthetic/public-safe values | No real people, credentials, DNA, property, or sensitive locations |

### Rejected ambient inputs

A conforming namespace does not depend on:

- current working directory;
- environment-derived identity rules;
- network registries;
- hidden singleton state;
- operator memory;
- UI selection state;
- source credentials;
- current time unless injected and recorded;
- random suffixes unless an accepted profile explicitly requires and receipts them;
- model-generated guesses;
- private chain-of-thought.

[Back to top](#top)

---

<a id="identity-token-profile"></a>

## Identity-token profile

The current common `identity_token` is a narrow reference object.

### Current machine shape

| Field | Required | Current meaning |
|---|---:|---|
| `id` | Yes | Identifier of the referenced governed thing; syntax not constrained by the current common schema |
| `kind` | Yes | Closed enum: `run`, `source`, `decision`, `review`, `bundle`, `actor` |
| `issued_at` | Yes | Token issuance date-time |
| `issuer` | No | Component, actor, steward, service, or process that issued the token |

### Required package behavior

A future adapter may:

- parse a JSON-like mapping;
- validate required/extra fields through accepted schema tooling or an exact compatible adapter;
- expose an immutable value object;
- serialize without adding fields;
- preserve `issued_at` exactly according to accepted date-time normalization;
- return explicit unsupported-kind and invalid-date outcomes;
- require callers to resolve `id + kind` through the owning surface.

It must not:

- validate object existence by syntax alone;
- infer kind from the `id` string;
- convert a generic string into a token without explicit `kind` and `issued_at`;
- make `issuer` authoritative for the referenced object;
- expose an `actor` token as a login identity;
- accept secrets or additional properties;
- use token issuance time as object valid time;
- claim all `id` values use one grammar.

### Object/instance distinction

```text
referenced object identity  !=  identity_token instance
object valid time           !=  token issued_at
object owner                !=  token issuer
token schema validity       !=  target existence
target existence            !=  policy/release allowance
```

[Back to top](#top)

---

<a id="identifier-text-and-object-id-profiles"></a>

## Identifier-text and object-ID profiles

### Identifier text

Identifier text is opaque unless paired with an accepted profile. Profile rules may include:

- prefix or URI scheme;
- separator and segment grammar;
- case sensitivity;
- Unicode normalization preflight;
- percent-encoding rules;
- whitespace policy;
- allowed and forbidden characters;
- minimum/maximum length;
- reserved words and namespaces;
- version marker;
- checksum or digest segment;
- parse/format round-trip guarantees.

The package must preserve:

```text
original_text
profile_id
profile_version
parsed_parts
normalized_text     # only when the profile defines it
transform_receipt   # caller-owned reference when normalization changes bytes
```

### Stable object IDs

A stable object ID may be constructed only from an owning profile. Common helpers may combine already-governed parts, but must not decide which parts define sameness.

A domain profile might require:

```text
source_id
source_role
object_family
object_role
temporal_scope
spatial_or_support_scope
subject_or_taxon_scope
normalized_digest
schema_or_contract_version
```

Different domains can require different dimensions. Therefore:

- source-native ID alone is not globally unique;
- digest alone is not semantic identity;
- display name is not identity;
- geometry alone is not identity;
- one profile's normalization cannot be applied to another;
- changing identity-defining inputs creates a new candidate plus lineage, not an in-place silent rewrite.

### Collision checking

Collision checking is meaningful only within a declared scope:

```text
(profile_id, profile_version, namespace, object_family, collision_snapshot_id)
```

The namespace may compare against an explicit supplied set. It must not:

- query a registry by default;
- claim repository-global uniqueness;
- auto-increment or append random text;
- overwrite an existing identity;
- hide collisions as aliases.

[Back to top](#top)

---

<a id="reference-and-lineage-profiles"></a>

## Reference and lineage profiles

### Reference families

Reference parsing remains subordinate to the owning contract.

| Reference family | Owning meaning | Package limit |
|---|---|---|
| EvidenceRef | Evidence contract | Parse/format fields; no evidence closure |
| Source/source-descriptor ref | Source contract/registry | No source activation or authority |
| Receipt ref | Receipt contracts/store | No receipt validity claim |
| Decision/review ref | Governance/policy contracts | No decision outcome |
| Release/rollback/correction ref | Release contracts | No transition approval |
| Catalog/triplet ref | Catalog/graph contracts | No catalog truth |
| Actor ref | Actor/governance contracts | No authentication/personhood claim |
| Domain object ref | Domain contracts | No cross-domain retargeting |

### Lineage relation values

A future helper may create immutable relation candidates from explicit inputs:

| Relation | Meaning | Required support |
|---|---|---|
| `alias_of` | Alternate identifier for the same governed slot under an accepted rule | Profile/version and reason |
| `supersedes` | New candidate replaces prior candidate prospectively | Prior/current refs, effective time, decision/correction ref |
| `corrects` | New record corrects an error in prior identity/record linkage | Correction reason and evidence/review refs |
| `tombstones` | Prior identifier is no longer active/usable | Tombstone reason, effective time, policy/release context |
| `rollback_to` | Operational state returns to a prior governed target | Rollback record/decision ref |
| `migrates_to` | Identifier/profile version changes under a migration plan | Old/new profile, mapping rule, compatibility window |

### Lineage invariants

- Relations are directional.
- Relations are not stored inside the identifier string.
- Alias and supersession are not synonyms.
- A tombstone does not delete audit history.
- Migration does not retroactively rewrite receipts.
- Cycles fail closed unless a specific contract defines a safe equivalence class.
- Many-to-one mappings require explicit review because they may collapse distinct objects.
- One-to-many mappings require explicit split semantics.
- Sensitive relation details may require restricted storage and public projection.
- The package returns relation candidates; owning governance persists and approves them.

[Back to top](#top)

---

<a id="hashing-and-run-id-boundary"></a>

## Hashing and run-ID boundary

### Hash delegation

This namespace consumes explicit digest values from [`packages/hashing/`](../../../hashing/README.md) or a governed caller.

Allowed:

- preserve digest text and declared profile;
- validate that a supplied identity profile permits a digest field;
- include the digest in a profile-defined identity recipe;
- compare exact supplied digest references when requested;
- report profile/prefix mismatch.

Denied:

- canonicalize and hash content as a hidden side effect;
- strip `jcs:` or `urdna2015:` prefixes;
- convert a bare checksum into `spec_hash`;
- choose SHA-256 or BLAKE3 by convenience;
- interpret digest equality as semantic sameness without the identity profile;
- duplicate the hashing package's canonicalization API.

### `run_id`

`run_id` is activity identity, not object identity.

ADR-0013 proposes `run:<orchestrator>:<ULID>`, but the namespace must not expose a default generator until governance verifies:

- ADR status;
- controlled orchestrator vocabulary;
- ULID dependency and monotonicity behavior;
- clock and concurrency policy;
- OpenLineage bridge;
- fixture vectors;
- compatibility with existing receipts;
- migration and rollback.

Until then, a run ID is an opaque profile-bound input or an `identity_token` target of kind `run`.

### Identity equation

```text
content equality       -> hashing profile
activity sameness      -> run profile
reference instance     -> identity_token profile
domain object sameness -> domain identity profile
string validity        -> identifier syntax profile
```

These outcomes may correlate, but they are never interchangeable.

[Back to top](#top)

---

<a id="proposed-library-api"></a>

## Proposed library API

This section is **PROPOSED** and intentionally profile-first.

### Value objects

| Proposed type | Purpose | Boundary |
|---|---|---|
| `IdentityProfileRef` | Names a profile and version | Does not store the profile registry |
| `IdentifierInput` | Original text plus profile and limits | No implicit normalization |
| `ParsedIdentifier` | Original text, parsed parts, optional normalized text | No target resolution |
| `IdentityTokenView` | Exact common token fields | No credential or existence semantics |
| `CollisionScope` | Explicit finite comparison scope and snapshot reference | No ambient registry |
| `LineageRelation` | Immutable alias/supersession/correction/tombstone candidate | No persistence/approval |
| `IdentityResult` | Finite outcome, value, reason codes, details | No policy/release decision |

### Functions

| Proposed function | Required inputs | Safe output |
|---|---|---|
| `parse_identifier` | text, profile, limits | Parsed result or finite failure |
| `format_identifier` | explicit parts, profile | String plus profile metadata |
| `validate_identifier` | text/parsed value, profile, optional collision scope | Validation result |
| `parse_identity_token` | mapping, schema/profile version | Immutable token view or failure |
| `build_identity_token` | explicit id, kind, issued_at, optional issuer | Candidate object; no target existence claim |
| `compare_identity_candidates` | two candidates, same profile | Equal/different/incomparable result |
| `check_collision` | candidate, explicit finite scope | Clear/no collision/collision/ambiguous |
| `make_lineage_relation` | prior/current IDs, relation kind, reason/effective refs | Candidate relation |
| `validate_lineage_graph` | explicit relation set and limits | Acyclic/invalid/ambiguous result |
| `require_profile_compatibility` | producer profile, consumer profile | Compatible/incompatible/migration-required |

### Functions intentionally excluded

- `generate_global_id()`
- `guess_profile()`
- `resolve_identity()`
- `find_person()`
- `match_actor()`
- `infer_owner()`
- `issue_token()`
- `create_session()`
- `grant_permission()`
- `write_registry()`
- `auto_migrate_ids()`
- `make_public_id()`
- `trust_if_valid()`

### Import posture

No import path is ratified yet. Future imports should expose a small intentional surface from `identity/__init__.py` only after:

- package discovery is configured;
- naming collision review is complete;
- type/API review is approved;
- tests prove no import side effects;
- compatibility policy is documented.

[Back to top](#top)

---

<a id="outcomes-and-reason-codes"></a>

## Outcomes and reason codes

### Finite outcomes

| Outcome | Meaning | Caller posture |
|---|---|---|
| `VALID` | Candidate conforms locally to the declared profile | Continue to schema, resolver, policy, evidence, and release gates |
| `INVALID` | Candidate violates syntax, shape, type, time, or profile rules | Fail closed |
| `RESERVED` | Namespace, prefix, kind, or value is reserved | Fail closed; no retargeting |
| `COLLISION` | Candidate collides within the supplied explicit scope | Block write/promotion; review |
| `AMBIGUOUS` | Profile, object family, target kind, scope, or mapping is insufficient | Abstain/review |
| `MIGRATION_REQUIRED` | Producer and consumer profiles differ under a governed migration path | Use explicit adapter/plan |
| `MIGRATED` | A supplied audit-backed relation validates under an accepted migration plan | Candidate only; downstream gates remain |
| `SENSITIVE_CONTEXT_DENIED` | Operation would process or expose restricted identity context outside allowed scope | Deny |
| `CREDENTIAL_MISUSE` | Identity/token value is being used as credential, authorization, or secret | Deny and report |
| `UNSUPPORTED_PROFILE` | Profile or version is not implemented/accepted | Abstain/error |
| `RESOURCE_LIMIT` | Input exceeds deterministic safety bounds | Error without partial output |
| `ERROR` | Safe completion failed due to dependency/internal/system condition | Error with bounded details |

### Stable reason-code families

```text
IDENTITY_PROFILE_REQUIRED
IDENTITY_PROFILE_UNSUPPORTED
IDENTITY_PROFILE_VERSION_UNSUPPORTED
IDENTITY_SYNTAX_INVALID
IDENTITY_EMPTY_SEGMENT
IDENTITY_LENGTH_EXCEEDED
IDENTITY_SEGMENT_LIMIT_EXCEEDED
IDENTITY_CHARACTER_FORBIDDEN
IDENTITY_ENCODING_INVALID
IDENTITY_NORMALIZATION_UNDECLARED
IDENTITY_ORIGINAL_NOT_PRESERVED
IDENTITY_NAMESPACE_RESERVED
IDENTITY_KIND_UNSUPPORTED
IDENTITY_REQUIRED_FIELD_MISSING
IDENTITY_EXTRA_FIELD_FORBIDDEN
IDENTITY_ISSUED_AT_INVALID
IDENTITY_ISSUER_INVALID
IDENTITY_TOKEN_STRING_OBJECT_COLLAPSE
IDENTITY_REFERENCE_FAMILY_MISMATCH
IDENTITY_TARGET_UNRESOLVED
IDENTITY_COLLISION
IDENTITY_COLLISION_SCOPE_REQUIRED
IDENTITY_ALIAS_CYCLE
IDENTITY_LINEAGE_INCOMPLETE
IDENTITY_MANY_TO_ONE_REVIEW_REQUIRED
IDENTITY_ONE_TO_MANY_REVIEW_REQUIRED
IDENTITY_DIGEST_PROFILE_MISMATCH
IDENTITY_RUN_OBJECT_COLLAPSE
IDENTITY_DOMAIN_PROFILE_REQUIRED
IDENTITY_CREDENTIAL_MISUSE
IDENTITY_SENSITIVE_CONTEXT_DENIED
IDENTITY_RESOURCE_LIMIT
IDENTITY_DEPENDENCY_MISSING
IDENTITY_INTERNAL_ERROR
```

Reason codes describe local helper behavior. They are not PolicyDecisions, ValidationReports, EvidenceBundles, receipts, or release approvals.

[Back to top](#top)

---

<a id="security-privacy-and-resource-bounds"></a>

## Security, privacy, and resource bounds

### Security posture

The namespace is no-network, pure by default, and non-credential.

It must not:

- read environment secrets;
- accept passwords, API keys, JWTs, OAuth tokens, session cookies, bearer tokens, or private keys as identity inputs;
- emit authentication assertions;
- sign identifiers;
- manage keys;
- use HMAC/encryption/password hashing;
- fetch registry or identity-provider data;
- log full sensitive identifiers by default;
- treat hashed PII as automatically safe;
- expose timing or error detail that supports enumeration of restricted identities.

### Privacy and sensitivity

High-risk contexts include:

- living-person identities;
- minors;
- DNA/genomic identity;
- genealogy and kinship;
- private property ownership;
- tribal/sovereign/cultural identity;
- archaeology site identifiers;
- rare-species locations;
- infrastructure identifiers;
- confidential source-native IDs;
- restricted actor/reviewer identifiers.

Default posture:

1. require an explicit profile and audience;
2. minimize fields;
3. avoid real sensitive examples and fixtures;
4. return redacted/bounded error details;
5. do not resolve or match identities;
6. defer exposure to policy/review/release;
7. preserve correction and revocation references;
8. deny when context is insufficient.

### Resource bounds

An accepted implementation should pin and test:

| Bound | Purpose |
|---|---|
| Maximum input bytes | Prevent oversized identifier/token payloads |
| Maximum identifier length | Bound parsing and logs |
| Maximum segment count | Prevent pathological grammars |
| Maximum segment length | Bound memory and output |
| Maximum token object depth | Keep common token flat |
| Maximum lineage relations | Bound cycle detection |
| Maximum lineage traversal depth | Prevent graph exhaustion |
| Maximum collision candidates | Bound explicit-scope checks |
| Maximum error-detail bytes | Prevent sensitive reflection |
| Maximum profile size | Prevent caller-supplied grammar abuse |

Exceeding a bound returns `RESOURCE_LIMIT`; no truncation may produce an authoritative ID.

[Back to top](#top)

---

<a id="testing-and-parity"></a>

## Testing and parity

Current evidence does not establish package-specific tests, fixtures, or CI. A future implementation requires at least the following.

### IdentityToken schema/profile tests

- required `id`, `kind`, and `issued_at`;
- optional `issuer`;
- closed `kind` enum;
- invalid date-time;
- extra property rejection;
- missing field rejection;
- token-object versus string-token misuse;
- `actor` token remains non-credential;
- serialization round trip;
- no target-existence claim.

### Identifier-profile tests

- parse/format round trip;
- original text preservation;
- profile/version required;
- unsupported profile/version;
- case-sensitive and case-insensitive profiles;
- Unicode normalization declared versus undeclared;
- percent encoding;
- leading/trailing whitespace;
- empty and repeated segments;
- forbidden characters;
- maximum length/segments;
- reserved namespaces;
- profile-incompatible comparison;
- no silent repair.

### Collision and lineage tests

- explicit collision scope required;
- same ID in different valid scopes;
- true collision in same scope;
- ambiguous scope;
- alias chain;
- alias cycle;
- supersession direction;
- correction relation;
- tombstone preservation;
- many-to-one collapse review;
- one-to-many split review;
- migration profile/version mismatch;
- rollback relation;
- deterministic relation serialization.

### Domain-separation tests

- common helper does not select a domain profile;
- same source-native ID in different domains is not automatically equal;
- different object families remain distinct;
- temporal and support scopes remain visible;
- source role is not discarded;
- sensitive geometry/actor identifiers are not echoed publicly;
- domain wrapper uses common parser/result primitives without moving domain semantics into common code.

### Hashing and run-ID integration tests

- explicit digest/profile preserved;
- no hidden hashing;
- digest prefix mismatch;
- `spec_hash` not used as run ID;
- run ID not used as stable object ID;
- proposed ADR grammar disabled until accepted;
- accepted profile vectors match hashing package outputs;
- incompatible profile returns migration-required.

### Import and side-effect tests

- import succeeds in isolated environment after package configuration;
- import performs no network, filesystem, registry, clock, random, or logging side effect;
- only intentional exports appear;
- no dependency on apps, connectors, lifecycle stores, policy engines, release writers, or model providers;
- secret scanning and dependency scanning pass;
- type checking and linting pass under accepted runtime.

### Cross-language parity

When another language implements an identity profile, shared golden vectors must prove identical:

- parse results;
- normalized representations;
- formatted strings;
- reserved-value outcomes;
- token object serialization;
- collision keys;
- lineage relation serialization;
- reason codes.

[Back to top](#top)

---

<a id="compatibility-and-migration"></a>

## Compatibility and migration

Identity changes are compatibility-significant because identifiers persist in receipts, proofs, catalogs, graphs, releases, URLs, and corrections.

### Versioning rules

- Every grammar/normalization recipe has a profile ID and version.
- New writes use only an accepted profile.
- Readers do not silently upgrade old identifiers.
- A profile change requires fixtures, parity vectors, consumer inventory, migration plan, correction plan, and rollback.
- Adding an `identity_token.kind` requires contract/schema/fixture/validator/consumer review.
- Making `issuer` required is a schema-breaking change.
- Changing case, Unicode, percent encoding, separators, or reserved words is compatibility-significant.
- Domain identity recipe changes stay domain-scoped unless promoted through governance.

### Safe migration sequence

1. Inventory producers, consumers, persisted records, public URLs, receipts, proofs, catalogs, graph edges, and releases.
2. Pin old and new profile versions.
3. Define one-way mapping and non-mappable outcomes.
4. Add golden vectors and negative tests.
5. Add an explicit adapter outside the core parser when possible.
6. Use a bounded dual-read / single-write period only if approved.
7. Emit alias/supersession/correction relations and migration receipts.
8. Revalidate evidence, policy, sensitivity, release, and public projections.
9. Monitor collision and unresolved-reference rates.
10. End compatibility support through a documented deprecation decision.
11. Preserve rollback to prior package/profile and data state.

### Forbidden migration behavior

- global search-and-replace without object-family review;
- silent case folding;
- silently adding/removing URI schemes;
- converting token objects to strings;
- replacing IDs in receipts/proofs;
- deleting tombstoned identity history;
- auto-aliasing collisions;
- using hashes of PII to bypass sensitivity controls;
- treating a new profile as retroactively authoritative.

[Back to top](#top)

---

<a id="smallest-sound-implementation-sequence"></a>

## Smallest sound implementation sequence

No implementation should begin until the first governance gates are resolved.

### Stage 0 — decisions

- assign owners;
- decide whether `identity` remains the import namespace;
- accept, amend, or supersede ADR-0013;
- establish the identity-profile registry/home without creating parallel authority;
- reconcile common IdentityToken with identifier-string terminology;
- define common-versus-domain responsibilities;
- approve privacy/sensitivity posture;
- choose package runtime/build/dependencies.

### Stage 1 — result and profile primitives

Implement only:

- immutable profile references;
- input/resource limits;
- finite result/reason types;
- no-network/import-safety tests.

No universal grammar, token generator, resolver, or domain identity recipe.

### Stage 2 — common IdentityToken adapter

- implement exact current contract/schema behavior;
- preserve explicit `issued_at`;
- reject extra fields;
- keep actor tokens non-credential;
- add schema/profile fixtures and negative tests.

### Stage 3 — one accepted identifier profile

- select one low-risk, non-sensitive profile;
- implement parse/format/validate;
- preserve original text;
- add cross-language vectors if needed;
- prove no silent normalization.

### Stage 4 — collision and lineage values

- explicit finite collision scope;
- immutable relation values;
- cycle/merge/split checks;
- no registry writes;
- receipts/release handled by callers.

### Stage 5 — tool and validator adapters

- validator lanes import the package;
- no duplicate parser or grammar;
- deterministic ValidationReport-compatible outcomes;
- package/tool parity tests.

### Stage 6 — domain wrappers

- domain packages select domain profiles;
- common namespace supplies primitives only;
- domain contracts remain authority;
- sensitive-domain tests fail closed.

### Stage 7 — consumer migration and release

- inventory and migrate consumers;
- add CI gates;
- package build/install/import tests;
- compatibility window and deprecation;
- rollback drill.

[Back to top](#top)

---

<a id="definition-of-done"></a>

## Definition of done

The namespace is not implementation-ready until all applicable items pass.

- [ ] Owners and review duties assigned.
- [ ] Directory Rules placement re-confirmed.
- [ ] Import/distribution naming approved.
- [ ] Package metadata and build backend configured.
- [ ] Supported runtime versions pinned.
- [ ] Dependencies approved and locked.
- [ ] Identity profiles have an accepted authority home.
- [ ] Common IdentityToken and generic identifier terminology reconciled.
- [ ] `id` grammar/profile decisions are explicit.
- [ ] ADR-0013 accepted, amended, or superseded before run-ID defaults.
- [ ] Common/domain identity responsibility split approved.
- [ ] Hashing dependency contract approved.
- [ ] Privacy/sensitivity review complete.
- [ ] Public API is minimal and versioned.
- [ ] Original/normalized representations are separated.
- [ ] No silent repair, suffixing, retargeting, or migration.
- [ ] Collision scope is explicit and bounded.
- [ ] Lineage relations are immutable and cycle-tested.
- [ ] No network/filesystem/registry side effects.
- [ ] No credentials, secrets, person matching, or identity-provider behavior.
- [ ] IdentityToken schema tests pass.
- [ ] Profile grammar and negative tests pass.
- [ ] Domain-separation tests pass.
- [ ] Hash/run/object/reference separation tests pass.
- [ ] Cross-language vectors pass where applicable.
- [ ] Import/build/install/type/lint tests pass.
- [ ] Dedicated CI gate is enforceable.
- [ ] Consumers are inventoried.
- [ ] Migration/correction/deprecation plan approved.
- [ ] Rollback drill restores package and consumer behavior.
- [ ] Documentation matches implemented behavior.

[Back to top](#top)

---

<a id="verification-register"></a>

## Verification register

| ID | Item | Status | Blocking consequence |
|---:|---|---|---|
| ID-01 | Package/namespace owners | NEEDS VERIFICATION | No accountability |
| ID-02 | Import namespace `identity` | NEEDS VERIFICATION | API cannot be ratified |
| ID-03 | Distribution/import collision review | NEEDS VERIFICATION | Install/import risk |
| ID-04 | Build backend and source discovery | UNKNOWN | Package not installable |
| ID-05 | Supported Python/runtime versions | UNKNOWN | Compatibility unknown |
| ID-06 | Dependency policy | UNKNOWN | Supply-chain risk |
| ID-07 | Accepted identity-profile home | NEEDS VERIFICATION | No grammar authority |
| ID-08 | Profile ID/version grammar | NEEDS VERIFICATION | Results not reproducible |
| ID-09 | Universal KFM URI grammar | NOT ESTABLISHED | No default parser |
| ID-10 | Unicode normalization rules | UNKNOWN | Cross-runtime drift |
| ID-11 | Case rules | UNKNOWN | Equality drift |
| ID-12 | Percent-encoding rules | UNKNOWN | Parse/format drift |
| ID-13 | Whitespace policy | UNKNOWN | Silent repair risk |
| ID-14 | Reserved namespaces/prefixes | UNKNOWN | Collision/authority risk |
| ID-15 | Max identifier/segment limits | NEEDS VERIFICATION | Resource risk |
| ID-16 | IdentityToken terminology split | CONFLICTED | Object/string collapse |
| ID-17 | IdentityToken schema status | PROPOSED | API must remain provisional |
| ID-18 | IdentityToken validator | NOT FOUND | No dedicated validation |
| ID-19 | IdentityToken fixtures | NOT FOUND | No conformance proof |
| ID-20 | `identity_token.id` syntax | UNCONSTRAINED BY SCHEMA | Profile required |
| ID-21 | Closed `kind` enum migration | NEEDS VERIFICATION | Consumer break risk |
| ID-22 | `issued_at` normalization | NEEDS VERIFICATION | Token instance drift |
| ID-23 | `issuer` policy | NEEDS VERIFICATION | Auditability inconsistent |
| ID-24 | Object/token instance separation | PROPOSED safeguard | Time/identity collapse risk |
| ID-25 | Common/domain identity split | NEEDS VERIFICATION | Domain semantics may flatten |
| ID-26 | Domain profile selection | UNKNOWN | No generic object-ID builder |
| ID-27 | Source-role preservation | NEEDS VERIFICATION | Authority collapse |
| ID-28 | Temporal/support scope preservation | NEEDS VERIFICATION | Entity collision |
| ID-29 | Hash representation compatibility | CONFLICTED upstream | Digest-bearing ID blocked |
| ID-30 | ADR-0013 status | PROPOSED | No default run-ID generator |
| ID-31 | Orchestrator vocabulary | UNKNOWN | Run-ID grammar incomplete |
| ID-32 | ULID dependency/monotonic policy | UNKNOWN | Run-ID drift |
| ID-33 | Collision scope contract | NEEDS VERIFICATION | Uniqueness claim unsafe |
| ID-34 | Collision registry authority | UNKNOWN | Package must not query/write |
| ID-35 | Alias semantics | NEEDS VERIFICATION | Retargeting risk |
| ID-36 | Supersession/correction/tombstone semantics | NEEDS VERIFICATION | Audit/rollback risk |
| ID-37 | Cycle/merge/split policy | NEEDS VERIFICATION | Lineage corruption |
| ID-38 | EvidenceRef adapter scope | NEEDS VERIFICATION | Evidence closure collapse |
| ID-39 | Source/release/receipt ref profiles | NEEDS VERIFICATION | Cross-family confusion |
| ID-40 | Actor privacy and authentication split | NEEDS VERIFICATION | Security/privacy risk |
| ID-41 | Living-person/DNA/property safeguards | NEEDS VERIFICATION | Sensitive disclosure risk |
| ID-42 | Package implementation modules | NOT FOUND | No runtime behavior |
| ID-43 | Intentional `__init__` exports | EMPTY | No public API |
| ID-44 | Executable consumers | NOT ESTABLISHED | Migration scope unknown |
| ID-45 | Package-specific tests | NOT FOUND | Behavior unproved |
| ID-46 | Dedicated identity CI | NOT FOUND | No enforcement |
| ID-47 | Validator integration | PLACEHOLDER/README-ONLY | Reports unproved |
| ID-48 | Cross-language parity vectors | UNKNOWN | Interop risk |
| ID-49 | Public API/governed envelope integration | UNKNOWN | Trust-membrane risk |
| ID-50 | Correction and rollback automation | UNKNOWN | Change not reversible |
| ID-51 | Compatibility window | NEEDS VERIFICATION | Migration unsafe |
| ID-52 | Deprecation policy | NEEDS VERIFICATION | Old IDs may persist indefinitely |

[Back to top](#top)

---

<a id="rollback-correction-and-deprecation"></a>

## Rollback, correction, and deprecation

### Documentation rollback

Restore the prior blob for this path or revert the documentation commit. This does not alter package code because this change is documentation-only.

### Future software rollback

A behavior-changing implementation must pin:

- prior package version and artifact digest;
- prior profile versions;
- prior exports and dependency lock;
- consumer versions;
- feature/config flags;
- migration adapters;
- validation vectors;
- rollback command/runbook;
- expected post-rollback IDs and results.

### Data/identity correction

Software rollback does not erase identifiers already emitted. If an implementation produced incorrect IDs:

1. stop new writes;
2. identify affected profile/version and producer runs;
3. preserve erroneous values for audit;
4. emit correction/supersession/tombstone relations through owning governance;
5. rebuild affected receipts, proofs, catalogs, graphs, releases, and public projections where authorized;
6. validate reference resolution and collision effects;
7. record rollback/correction decisions;
8. prevent the bad profile/version from re-entering service.

### Deprecation

Deprecation requires:

- identified consumers;
- accepted replacement profile;
- compatibility adapter where safe;
- warning/reason-code period;
- end date or release threshold;
- fixture and CI coverage;
- correction/rollback path;
- no silent fallback after removal.

[Back to top](#top)

---

<a id="evidence-ledger"></a>

## Evidence ledger

| Evidence | Status | Supports | Limitation |
|---|---:|---|---|
| Current target README | CONFIRMED | Existing namespace documentation and proposed scope | Does not prove code |
| [`identity/__init__.py`](__init__.py) | CONFIRMED empty | No exports or side effects | Does not prove package installability |
| [`pyproject.toml`](../../pyproject.toml) | CONFIRMED placeholder | Distribution name/version | No build/dependency/discovery config |
| [Parent source README](../README.md) | CONFIRMED draft | Source-envelope intent | Still documentation-rich and implementation-unproved |
| [Parent package README](../../README.md) | CONFIRMED draft | Package boundary and hashing delegation | Does not ratify namespace API |
| [Hashing package README](../../../hashing/README.md) | CONFIRMED v1.1 documentation | Digest/canonicalization delegation boundary | Hash implementation remains unproved |
| [IdentityToken contract](../../../../contracts/common/identity_token.md) | CONFIRMED draft v0.3 | Narrow object meaning and non-credential posture | Runtime/validator/fixtures incomplete |
| [IdentityToken schema](../../../../schemas/contracts/v1/common/identity_token.schema.json) | CONFIRMED PROPOSED schema | Exact fields and closed kind enum | `id` has no grammar constraint |
| [Identity validator routing README](../../../../tools/validators/identity/README.md) | CONFIRMED README | Validator responsibility split | Does not prove executable validation |
| [`jcs_spec_hash.py`](../../../../tools/validators/identity/jcs_spec_hash.py) | CONFIRMED placeholder | Path and intended topic | No executable behavior |
| [`validate_identity.py`](../../../../tools/validators/evidence/validate_identity.py) | CONFIRMED placeholder | Path and domain-doc sources | No executable behavior |
| [ADR-0013](../../../../docs/adr/ADR-0013-spec_hash-and-run_id-identity-grammar.md) | CONFIRMED proposed | Candidate hash/run grammar and migration concerns | Not accepted implementation authority |
| [Identity architecture](../../../../docs/architecture/identity-and-spec-hash.md) | CONFIRMED draft doctrine | Deterministic identity principles | Machine/runtime implementation unresolved |
| [Evidence identity architecture](../../../../docs/architecture/evidence-identity.md) | CONFIRMED draft doctrine | Evidence/object identity separation | Paths and runtime details partly proposed |
| [EvidenceRef contract](../../../../contracts/evidence/evidence_ref.md) | CONFIRMED draft profile | Evidence pointer remains evidence-owned | Resolver/policy/release behavior needs verification |
| [Fauna identity contract](../../../../contracts/domains/fauna/domain_feature_identity.md) | CONFIRMED draft domain contract | Domain-specific sameness and sensitivity dimensions | Schema/validator not field-complete |
| Bounded absent-path checks | CONFIRMED for exact paths | No proposed common modules/tests/workflows at tested paths | Does not prove absence under every alternative path |
| Bounded code search | NEEDS VERIFICATION for completeness | Did not establish executable package consumers | Search can miss generated/dynamic/unindexed imports |

---

## Maintainer summary

Treat `packages/identity/src/identity/` as an **empty, unratified compatibility boundary**.

The smallest safe next decision is not “implement all identity helpers.” It is:

1. assign ownership;
2. reconcile IdentityToken object versus identifier-string terminology;
3. accept one profile and its authority;
4. keep domain identity domain-owned;
5. preserve hashing and run-ID separation;
6. implement result/profile primitives with negative tests;
7. add one low-risk profile before expanding.

Until those gates pass, profile ambiguity, collision scope, domain sameness, actor privacy, or lineage uncertainty must produce a bounded failure—not a plausible identifier.

[Back to top](#top)
