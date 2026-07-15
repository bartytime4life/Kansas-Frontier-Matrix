<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-identity-src-readme
title: packages/identity/src/ — Identity Source Envelope and Implementation Placement Boundary
type: readme
version: v1.1
status: draft
owners: OWNER_TBD — Package steward · Identity steward · Contract steward · Schema steward · Domain stewards · Privacy reviewer · Sensitivity reviewer · Security steward · Dependency steward · Validation steward · Migration steward · CI steward · Docs steward
created: NEEDS VERIFICATION — target existed before the current evidence-grounded revision
updated: 2026-07-15
policy_label: "public-doctrine; package-source-boundary; deterministic-identity; implementation-empty; api-unratified; profile-registry-unsettled; identity-token-separated; domain-identity-separated; run-id-separated; hashing-delegated; non-credential; no-network; pure-functions; fail-closed; privacy-aware; no-authority; no-secrets; migration-required; rollback-aware"
current_path: packages/identity/src/README.md
truth_posture: CONFIRMED target README v1, merged child namespace README v1.1, empty identity package initializer, kfm-identity 0.0.0 placeholder metadata, package/root READMEs, Directory Rules package placement, merged hashing package boundary v1.1, draft IdentityToken contract v0.3 and PROPOSED schema, missing declared IdentityToken validator and fixture README at bounded paths, README-only Identity validator routing lane, placeholder identity validator modules, PROPOSED ADR-0013, draft identity/evidence architecture notes, confirmed EvidenceRef contract, representative domain-owned Fauna identity contract, and bounded absence of proposed implementation modules, package-specific tests/workflows, and executable consumers / PROPOSED source-envelope rules, package discovery and dependency direction, profile-first module placement, pure-library constraints, package/namespace/tool/validator/caller delegation, explicit result families, resource bounds, tests, staged implementation, correction, migration, deprecation, and rollback / CONFLICTED common identity_token object versus generic identifier-token string terminology, stable referenced-object identity versus issued token-instance identity, universal KFM ID grammar proposals versus unconstrained common schema id and domain-owned identity semantics, proposed ADR run_id grammar versus unaccepted implementation, generic identity source tree versus domain-specific sameness rules, package name versus unratified import namespace, and rich documentation versus empty implementation / UNKNOWN accepted identifier-profile registry, namespace grammar, normalization rules, Python runtime, build backend, dependency set, source discovery, export surface, consumer inventory beyond bounded search, collision authority, resolver behavior, cross-language parity, package tests, CI enforcement, distribution posture, release use, and operational health / NEEDS VERIFICATION owners, accepted ADR or migration decision, identity-profile vocabulary, common/domain boundary, package metadata, source layout, API shape, privacy review, test vectors, collision-scope contract, consumer migration, CI gates, correction path, compatibility period, deprecation, and rollback automation
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 007d2f93dcaaf4f07e17983e8626e89243ff7705
  prior_blob: 4f630edb84ee6d35ee447f779f0798924b2ef513
  package_readme_blob: ba5f4c0b3e425448906acc6e5e393eefce60ab8b
  namespace_readme_blob: 2ad41cdc9ceda02e7ca04a66c4ac9d8b08770a8e
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
    - packages/identity/src/README.md existed at version v1 before this revision
    - packages/identity/src/identity/README.md exists at version v1.1
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
  - ../README.md
  - identity/README.md
  - identity/__init__.py
  - ../pyproject.toml
  - ../../README.md
  - ../../hashing/README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0013-spec_hash-and-run_id-identity-grammar.md
  - ../../../docs/architecture/identity-and-spec-hash.md
  - ../../../docs/architecture/evidence-identity.md
  - ../../../contracts/common/identity_token.md
  - ../../../schemas/contracts/v1/common/identity_token.schema.json
  - ../../../contracts/evidence/evidence_ref.md
  - ../../../contracts/domains/fauna/domain_feature_identity.md
  - ../../../contracts/domains/hydrology/reach_identity.md
  - ../../../contracts/domains/settlements-infrastructure/place-identity.md
  - ../../../tools/validators/identity/README.md
  - ../../../tools/validators/identity/jcs_spec_hash.py
  - ../../../tools/validators/evidence/validate_identity.py
tags: [kfm, packages, identity, src, deterministic-identity, identity-token, identifier-profile, object-id, run-id, reference, alias, supersession, tombstone, collision, domain-identity, hashing, privacy, dependencies, compatibility, migration, fail-closed]
notes:
  - "This revision changes only packages/identity/src/README.md."
  - "The source envelope currently contains this README and the identity/ child namespace; that namespace contains its v1.1 README and an empty __init__.py."
  - "This README does not activate an API, select a universal identifier grammar, accept ADR-0013, define domain sameness, create a collision registry, approve dependencies, or authorize package distribution."
  - "The common identity_token object, identifier strings, stable object ids, run ids, evidence/source/release references, aliases, and domain feature identities remain separate governed profiles."
  - "A well-formed identifier is not object existence, person identity, evidence closure, policy approval, release approval, or public safety."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Identity Source Envelope and Implementation Placement Boundary

`packages/identity/src/`

> Repository-present source envelope for a future reusable deterministic identity library. Current evidence establishes documentation and an empty import initializer—not an implemented grammar, exported token API, resolver, collision service, tested package, or CI-enforced identity subsystem.

![status](https://img.shields.io/badge/status-draft-yellow)
![version](https://img.shields.io/badge/version-v1.1-informational)
![maturity](https://img.shields.io/badge/maturity-source__scaffold-lightgrey)
![profiles](https://img.shields.io/badge/profiles-unsettled-orange)
![identity token](https://img.shields.io/badge/identity__token-typed__reference-blue)
![credentials](https://img.shields.io/badge/credentials-DENIED-critical)
![network](https://img.shields.io/badge/network-none-critical)
![authority](https://img.shields.io/badge/truth__authority-none-red)

**Quick links:** [Purpose](#purpose) · [Evidence](#status-and-evidence) · [Related evidence](#related-evidence) · [Placement](#directory-rules-and-authority) · [Responsibilities](#source-envelope-responsibilities) · [Profiles](#identity-profile-separation) · [Conflicts](#compatibility-conflicts) · [Tree](#confirmed-and-proposed-source-tree) · [Invariants](#keystone-invariants) · [Imports](#import-and-dependency-direction) · [Modules](#profile-bound-module-placement) · [Delegation](#package-namespace-tool-validator-and-caller-delegation) · [Side effects](#side-effect-and-io-boundary) · [Security](#security-privacy-and-resource-bounds) · [Testing](#testing-fixtures-and-ci) · [Migration](#compatibility-and-migration) · [Implementation](#smallest-sound-implementation-sequence) · [Done](#definition-of-done) · [Open](#verification-register) · [Rollback](#rollback-correction-deprecation-and-migration)

> [!IMPORTANT]
> **This README is not an implementation, API, grammar, dependency, resolver, registry, or migration decision.** It does not establish exports, a universal KFM identifier syntax, accepted normalization rules, collision authority, domain sameness, an accepted `run_id` grammar, package discovery, CI enforcement, or operational consumers.

> [!CAUTION]
> **A valid identifier is not proof of identity or truth.** It establishes only local conformance to a declared profile. Object existence, actor identity, source authority, evidence support, rights, sensitivity, policy, review, release, and public safety remain separate governed checks.

---

<a id="purpose"></a>

## Purpose

This README defines the allowed responsibility boundary for source code under `packages/identity/src/`.

The source envelope may eventually contain a reusable implementation for governed callers that need to:

- parse and format identifiers under explicit, versioned identity profiles;
- preserve original input separately from normalized or canonical display forms;
- validate profile-specific syntax, namespace, kind, length, and reserved values;
- construct the current common `identity_token` object from explicit fields;
- compare identity candidates within explicit, caller-supplied collision scopes;
- represent alias, supersession, correction, tombstone, and migration relations from audit-backed inputs;
- consume digest values from [`packages/hashing/`](../../hashing/README.md) without duplicating canonicalization or hashing semantics;
- return deterministic typed results and stable reason codes;
- support governed flows without owning registries, resolvers, lifecycle records, policy, review, or release.

The source envelope must not become:

- a second contract, schema, identity-profile registry, domain-model, or policy home;
- a universal “identity service” that decides what every KFM object means by sameness;
- a registry scanner, collision authority, resolver, catalog writer, or lifecycle store;
- an authentication, authorization, credential, consent, session, identity-provider, or secret-management system;
- a person-matching, property-ownership, kinship, DNA/genomic, or sensitive-location inference subsystem;
- a public API, UI, map, export, search, embedding, or AI answer surface;
- an ambient filesystem scanner, network client, database client, or model client;
- a compatibility shortcut that silently repairs, normalizes, suffixes, retargets, merges, or migrates identifiers.

The child [`identity/README.md`](identity/README.md) governs proposed import behavior and profile semantics. This parent README governs source placement, module decomposition, dependency direction, side-effect limits, implementation delegation, and the evidence required before source files are added.

[Back to top](#top)

---

<a id="status-and-evidence"></a>

## Status and evidence

| Surface | Status | Safe conclusion |
|---|---:|---|
| This README | **CONFIRMED v1 before revision** | A source-envelope guide exists. |
| Child `identity/README.md` | **CONFIRMED v1.1** | The import namespace has an evidence-grounded compatibility boundary. |
| `identity/__init__.py` | **CONFIRMED empty** | No exports, import behavior, or side effects are established. |
| `kfm-identity` metadata | **CONFIRMED `0.0.0` placeholder** | Distribution name exists; build backend, dependencies, source discovery, and installability are not established. |
| Proposed source modules | **NOT FOUND at bounded paths** | No grammar, namespace, object-ID, token, reference, lineage, validation, or fixture implementation is established. |
| Package-specific test README | **NOT FOUND** | No dedicated identity-package test boundary is established. |
| Package-specific workflow | **NOT FOUND** | No dedicated identity CI behavior is established. |
| Executable consumers | **NOT ESTABLISHED by bounded search** | Search found documentation/contracts/placeholders, not proven imports of this package. |
| Common `identity_token` contract | **CONFIRMED draft v0.3** | Defines a small typed reference object; explicitly not a credential or proof of identity. |
| Common `identity_token` schema | **CONFIRMED `PROPOSED` machine surface** | Requires `id`, `kind`, and `issued_at`; `issuer` is optional; `id` has no universal grammar pattern. |
| Declared IdentityToken validator | **NOT FOUND** | Schema metadata does not prove executable validation. |
| Declared IdentityToken fixture README | **NOT FOUND** | No common fixture coverage is established. |
| Identity validator routing lane | **CONFIRMED README-only boundary** | Validation responsibilities are documented; runtime wiring remains unproved. |
| Checked identity validator modules | **CONFIRMED placeholders** | They contain provenance comments, not validation behavior. |
| ADR-0013 | **CONFIRMED `proposed`** | Proposes `spec_hash` and `run_id` grammar; not accepted implementation fact. |
| EvidenceRef contract | **CONFIRMED draft/profiled contract** | Evidence pointers remain evidence-owned, not generic identity aliases. |
| Representative Fauna identity contract | **CONFIRMED draft/domain-owned** | Domain sameness preserves source role, family, time, support, evidence, sensitivity, and lineage. |
| Hashing package boundary | **CONFIRMED v1.1 documentation** | Hash semantics remain delegated; implementation is still unratified. |

### Truth posture

**CONFIRMED**

- `packages/identity/src/` is a source scaffold, not a functioning implementation.
- The child namespace is effectively empty.
- Package metadata is a greenfield placeholder.
- The common `identity_token` is an object, not a credential and not a generic token string.
- Its schema does not define a universal grammar for `id`.
- Domain identity meaning remains domain-owned.
- The checked validation scripts are placeholders.
- No checked evidence proves package-specific tests, dedicated CI, distribution, or consumers.

**PROPOSED**

- The source placement rules, dependency direction, module decomposition, delegation model, pure-function requirements, result families, resource limits, tests, implementation sequence, correction, migration, deprecation, and rollback procedures below.

**CONFLICTED**

- Common `identity_token` object versus broad “identifier token string” terminology.
- Stable referenced-object identity versus the identity and issuance time of a token instance.
- Universal KFM ID grammar proposals versus unconstrained common-schema `id` and domain-owned sameness.
- Proposed ADR-0013 `run_id` grammar versus no accepted implementation.
- Generic shared source modules versus domain-specific object identity contracts.
- Distribution name `kfm-identity` versus unratified import namespace `identity`.
- Rich documentation versus no verified implementation.

**UNKNOWN**

- Supported Python version, build backend, dependencies, source discovery, exports, consumers, performance, cross-language parity, registry integration, resolver behavior, package distribution, release use, and operational health.

**NEEDS VERIFICATION**

- Owners, accepted ADR or migration note, identity-profile registry, normalization vocabulary, common/domain boundary, package metadata, source layout, public API, privacy review, collision-scope contract, test vectors, consumer migration, CI gates, correction path, compatibility period, deprecation, and rollback automation.

[Back to top](#top)

---

<a id="related-evidence"></a>

## Related evidence

The following current repository files bound this source-envelope revision:

- [`packages/identity/README.md`](../README.md) — package-level boundary and package mechanics.
- [`packages/identity/src/identity/README.md`](identity/README.md) — merged v1.1 import-namespace compatibility boundary.
- [`packages/identity/src/identity/__init__.py`](identity/__init__.py) — confirmed empty initializer.
- [`packages/identity/pyproject.toml`](../pyproject.toml) — confirmed `kfm-identity` `0.0.0` placeholder.
- [`packages/README.md`](../../README.md) — shared-library responsibility-root contract.
- [`packages/hashing/README.md`](../../hashing/README.md) — separate hashing, distribution, and compatibility boundary.
- [`docs/doctrine/directory-rules.md`](../../../docs/doctrine/directory-rules.md) — governing directory placement doctrine.
- [`docs/adr/ADR-0013-spec_hash-and-run_id-identity-grammar.md`](../../../docs/adr/ADR-0013-spec_hash-and-run_id-identity-grammar.md) — proposed grammar decision, not accepted implementation fact.
- [`docs/architecture/identity-and-spec-hash.md`](../../../docs/architecture/identity-and-spec-hash.md) — draft identity/hash architecture.
- [`docs/architecture/evidence-identity.md`](../../../docs/architecture/evidence-identity.md) — draft evidence/identity architecture.
- [`contracts/common/identity_token.md`](../../../contracts/common/identity_token.md) — common typed-reference meaning.
- [`schemas/contracts/v1/common/identity_token.schema.json`](../../../schemas/contracts/v1/common/identity_token.schema.json) — PROPOSED common machine shape.
- [`contracts/evidence/evidence_ref.md`](../../../contracts/evidence/evidence_ref.md) — evidence-owned pointer semantics.
- [`contracts/domains/fauna/domain_feature_identity.md`](../../../contracts/domains/fauna/domain_feature_identity.md) — representative domain-owned sameness model.
- [`contracts/domains/hydrology/reach_identity.md`](../../../contracts/domains/hydrology/reach_identity.md) — domain identity remains hydrology-owned.
- [`contracts/domains/settlements-infrastructure/place-identity.md`](../../../contracts/domains/settlements-infrastructure/place-identity.md) — place identity remains domain-owned.
- [`tools/validators/identity/README.md`](../../../tools/validators/identity/README.md) — validator routing boundary, not implementation proof.
- [`tools/validators/identity/jcs_spec_hash.py`](../../../tools/validators/identity/jcs_spec_hash.py) — confirmed documentation-only placeholder.
- [`tools/validators/evidence/validate_identity.py`](../../../tools/validators/evidence/validate_identity.py) — confirmed documentation-only placeholder.

These documents and files constrain this README. They do not collectively prove an installable package, executable identity grammar, accepted profile registry, global collision service, resolver, package consumer, or CI-enforced runtime.

[Back to top](#top)

---

<a id="directory-rules-and-authority"></a>

## Directory Rules and authority

`packages/` is the confirmed responsibility root for shared reusable implementation libraries. The root contract states that packages may support governed apps, workers, pipelines, tools, and tests, but must not become a second authority for truth, policy, contracts, schemas, release decisions, lifecycle data, or public publication state.

`packages/identity/src/` is therefore a sound **proposed** source envelope because:

- reusable implementation belongs under `packages/`;
- package mechanics belong at `packages/identity/`;
- source placement belongs at `packages/identity/src/`;
- import behavior belongs under `packages/identity/src/identity/`;
- semantic meaning belongs under `contracts/`;
- machine shape belongs under `schemas/contracts/v1/`;
- domain sameness belongs in domain contracts and profiles;
- source and object registries belong in governed registry roots;
- policy and sensitive-identity decisions belong under `policy/`;
- receipts and proofs belong in their dedicated data roots;
- correction, withdrawal, release, and rollback authority belong under `release/`;
- operator validation belongs under `tools/validators/`;
- public behavior belongs behind governed application interfaces.

This README does not create a parallel identity grammar, namespace registry, profile registry, collision registry, resolver registry, migration registry, or privacy-policy home.

### Authority matrix

| Responsibility | Owning surface | Source-envelope role |
|---|---|---|
| Package mechanics | `packages/identity/` | Consume package decisions; do not invent them here. |
| Source placement and dependency direction | `packages/identity/src/` | Owned by this README. |
| Import API and immutable value types | `packages/identity/src/identity/` | Proposed child responsibility after governance. |
| Common IdentityToken meaning | `contracts/common/identity_token.md` | Implement only accepted semantics. |
| Common IdentityToken shape | `schemas/contracts/v1/common/identity_token.schema.json` | Validate against accepted shape. |
| EvidenceRef meaning | `contracts/evidence/evidence_ref.md` | Preserve evidence-owned pointer semantics. |
| Domain identity meaning | Domain `contracts/` and profiles | Never replace with a generic package rule. |
| Hash/canonicalization semantics | `packages/hashing/` plus accepted contracts/standards | Delegate; do not duplicate. |
| Registry uniqueness and resolution | Governed registry/resolver roots | Consume explicit inputs/results only. |
| Policy, rights, sensitivity, access | `policy/` and governed review | Never decide locally. |
| Validation orchestration | `tools/validators/identity/` or accepted runner | Import pure helpers; own reports and routing. |
| Receipts and proofs | `data/receipts/`, `data/proofs/` | Never persist from the library. |
| Release/correction/rollback | `release/` | Consume references; never approve or mutate. |
| Public API/UI/AI behavior | Governed app/runtime roots | Receive only governed projections. |

[Back to top](#top)

---

<a id="source-envelope-responsibilities"></a>

## Source-envelope responsibilities

This source envelope may eventually own:

1. **Module placement**
   - keeping reusable pure identity implementation under one accepted namespace;
   - avoiding duplicate common implementations in tools, apps, domains, or pipelines;
   - keeping domain-specific semantics out of the common source tree.

2. **Dependency direction**
   - allowing imports from low-level standard-library or approved utility dependencies;
   - delegating canonicalization and digest work to the hashing package;
   - denying imports from connectors, pipelines, lifecycle stores, policy engines, release writers, apps, UI, model runtimes, and secret systems.

3. **Profile discipline**
   - requiring every parser, formatter, builder, and validator to name an accepted profile;
   - preventing “best effort” parsing across incompatible identity families;
   - preserving original form, parsed form, normalized form, and validation result separately.

4. **Side-effect discipline**
   - pure functions by default;
   - no network, filesystem scanning, database access, registry mutation, logging of sensitive values, or hidden global state;
   - deterministic results from explicit inputs.

5. **Compatibility discipline**
   - versioned profiles and result types;
   - no silent behavior changes;
   - explicit adapters only during a governed migration window;
   - consumer inventory and rollback support before breaking changes.

6. **Testability**
   - golden vectors for each profile;
   - negative cases for ambiguity, reserved values, collision scope, privacy, and incompatible profiles;
   - parity tests for every tool or validator adapter that imports the library.

It must not own:

- the canonical set of namespaces or reserved prefixes;
- the definition of domain object sameness;
- the complete identifier inventory across KFM;
- global uniqueness or collision registration;
- object existence or resolver truth;
- actor identity proof or authentication;
- public-safe projection decisions;
- source, evidence, catalog, release, or rollback record persistence.

[Back to top](#top)

---

<a id="identity-profile-separation"></a>

## Identity-profile separation

Identity is not one interchangeable string family. Before implementation, each supported concern requires an explicit profile, owner, contract/schema basis, input fields, output type, and migration posture.

| Profile family | Meaning | Common source code may do | Must remain outside |
|---|---|---|---|
| `identity_token` object | Typed reference object with `id`, `kind`, `issued_at`, optional `issuer` | Construct, parse, validate accepted object shape/semantics | Object resolution, credentials, authorization, existence proof |
| Identifier text | Text governed by an explicit grammar/profile | Parse/format and preserve original/normalized forms | Universal grammar invention, registry authority |
| Stable object ID | Identifier for one object under domain/common sameness rules | Apply a supplied profile and explicit identity inputs | Decide domain sameness or source authority |
| Activity/run ID | Identifier for a governed execution | Parse/format accepted profile if ratified | Orchestration, run creation policy, OpenLineage authority |
| Content identity | `spec_hash` or other digest-bearing identity | Carry typed digest references | Canonicalization/hash implementation |
| Evidence/source/review/release ref | Pointer defined by owning contract | Parse/format an accepted profile | Retargeting, resolving, closing evidence, releasing |
| Alias/supersession/correction relation | Auditable relation between identity slots | Construct immutable relation candidates | Writing registries, correction notices, release decisions |
| Tombstone/withdrawal relation | Marks identity withdrawal or invalidation | Construct explicit relation values | Deleting history or deciding withdrawal |
| Domain feature identity | Domain definition of sameness | Host generic primitives used by a domain adapter | Flatten domain role, source, time, geometry, sensitivity, lineage |
| Actor reference | Governed reference to an actor | Preserve accepted typed reference | Authentication, person matching, consent, sensitive identity proof |
| Fixture identity | Synthetic stable test value | Generate only from explicit fixture inputs | Production registry values or real sensitive identities |

### Non-interchangeability rules

- `identity_token.id` is not automatically a stable object-ID grammar.
- An `identity_token` instance is not the referenced object.
- `issued_at` is token issuance time, not object observation, validity, retrieval, review, correction, or release time.
- `run_id` is activity identity, not content identity.
- `spec_hash` is content integrity, not object identity in every domain.
- EvidenceRef is evidence-owned and must not be silently translated to IdentityToken.
- Alias, supersession, tombstone, correction, and rollback are distinct relation meanings.
- A domain object identifier cannot be recomputed without its domain profile and identity-defining inputs.
- A valid actor reference is not proof of personhood or authorization.

[Back to top](#top)

---

<a id="compatibility-conflicts"></a>

## Compatibility conflicts

No implementation should proceed by choosing a convenient interpretation of the following conflicts.

### 1. IdentityToken object versus “token string”

The confirmed common contract defines `identity_token` as a four-field value-object family. Prior source documentation also used “token string” for generic non-secret identifier segments.

Required posture:

- reserve `IdentityToken` for the common typed object;
- use a different governed name for generic identifier text or segments;
- do not serialize one as the other;
- add migration tests before changing existing terminology.

### 2. Referenced-object identity versus token-instance identity

The `id` field points at a governed thing. `issued_at` and `issuer` describe the token instance. They are not part of the referenced object’s identity unless an owning contract explicitly says so.

Required posture:

- model the two layers separately;
- prevent dedupe or equality logic from conflating them;
- test repeated tokens referring to the same object.

### 3. Universal grammar versus profile-specific grammar

The current common schema leaves `id` as an unconstrained string, while architecture and ADR documents describe several grammar proposals.

Required posture:

- require an explicit profile identifier for grammar-sensitive operations;
- reject unknown profiles;
- do not infer a profile from punctuation alone;
- do not treat ADR-0013 as accepted until governance changes its status and implementation evidence exists.

### 4. Common primitives versus domain sameness

Domain contracts may include source role, object family, temporal scope, support geometry, sensitivity, evidence, and lineage in their identity semantics.

Required posture:

- common source code may implement primitives;
- domain packages/adapters supply domain profiles and identity-defining fields;
- common code must not drop or reinterpret domain fields.

### 5. Collision detection versus collision authority

A pure helper can compare values within an explicit supplied scope. It cannot establish repository-global uniqueness without registry access and policy.

Required posture:

- accept a finite collision candidate set or callback result supplied by the caller;
- return `COLLISION` or `SCOPE_INCOMPLETE`;
- never scan ambient stores or append random suffixes.

### 6. Distribution/import naming

The distribution placeholder is `kfm-identity`; the proposed import namespace is `identity`.

Required posture:

- confirm package discovery and name-conflict risk before ratification;
- treat import naming as compatibility-significant;
- do not publish or document install commands until tested.

### 7. Identity versus hashing

Some identity profiles include digests, but hashing has its own unresolved package and contract issues.

Required posture:

- identity source code consumes explicit typed digest values;
- it must not duplicate canonicalization or hash formatting;
- incompatible digest profiles fail closed.

[Back to top](#top)

---

<a id="confirmed-and-proposed-source-tree"></a>

## Confirmed and proposed source tree

### Confirmed tree

```text
packages/identity/src/
├── README.md
└── identity/
    ├── README.md
    └── __init__.py    # empty
```

No additional implementation file is established by the checked paths.

### Proposed decomposition

The following is a design sketch, not a repository fact or file-creation instruction.

```text
packages/identity/src/
├── README.md
└── identity/
    ├── README.md
    ├── __init__.py
    ├── profiles.py
    ├── identity_token.py
    ├── identifier_text.py
    ├── object_id.py
    ├── references.py
    ├── lineage.py
    ├── collision.py
    ├── results.py
    └── errors.py
```

Potential responsibilities:

| Proposed module | Narrow responsibility | Stop condition |
|---|---|---|
| `profiles.py` | Immutable accepted profile identifiers and metadata adapters | Stop if profile authority is not ratified outside code. |
| `identity_token.py` | Common typed object construction/parsing | Stop if contract/schema reconciliation is unresolved. |
| `identifier_text.py` | Profile-bound parse/format without universal inference | Stop if grammar vectors are absent. |
| `object_id.py` | Candidate construction from explicit profile fields | Stop if domain sameness is not supplied. |
| `references.py` | Typed wrappers for accepted reference profiles | Stop if owning contract lacks stable shape/meaning. |
| `lineage.py` | Immutable alias/supersession/correction/tombstone relation values | Stop if relation semantics are not contract-defined. |
| `collision.py` | Compare within explicit finite scope | Stop if caller expects registry access or global uniqueness. |
| `results.py` | Stable typed results and reason codes | Stop if outcome vocabulary is not reviewed. |
| `errors.py` | Programmer/configuration errors distinct from validation outcomes | Stop if exceptions would hide governed finite outcomes. |

Do not create all proposed modules merely to match the diagram. Prefer the smallest reviewed implementation that satisfies one accepted profile and its tests.

[Back to top](#top)

---

<a id="keystone-invariants"></a>

## Keystone invariants

1. **Profile required.** Grammar-sensitive behavior requires an explicit accepted profile.
2. **Original preserved.** Parsing and normalization must not destroy the original supplied value.
3. **No silent repair.** Invalid input remains invalid; code must not change it into a new identity.
4. **No silent retargeting.** References and aliases cannot be redirected without explicit relation metadata.
5. **No ambient uniqueness.** Collision checks operate only on explicit finite scope supplied by the caller.
6. **No random suffixing.** Collision resolution is governance work, not a hidden string operation.
7. **Token object separated.** `IdentityToken` remains distinct from identifier text and the referenced object.
8. **Time kinds separated.** Token issuance time does not replace object, observation, valid, transaction, review, correction, or release time.
9. **Activity/content/object separated.** `run_id`, `spec_hash`, and object ID are not interchangeable.
10. **Domain sameness preserved.** Common utilities cannot flatten domain identity-defining fields.
11. **Hashing delegated.** Canonicalization and digest semantics remain owned by the hashing boundary.
12. **Credential misuse denied.** No function issues or validates authentication credentials, sessions, permissions, API keys, bearer tokens, or consent.
13. **Sensitive inference denied.** No person matching, ownership inference, kinship inference, DNA/genomic resolution, or restricted-location derivation.
14. **No network.** Import and normal calls perform no network access.
15. **No lifecycle I/O.** The package does not read or write RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, PUBLISHED, receipt, proof, or release stores.
16. **Typed finite outcomes.** Validation and comparison return inspectable status and reason code.
17. **Deterministic behavior.** Same explicit inputs and profile produce the same output.
18. **No hidden globals.** Locale, timezone, filesystem state, environment variables, process ID, and current time do not alter identity unless explicitly supplied and profile-approved.
19. **Privacy by construction.** Diagnostic values are bounded and safe; sensitive identifiers are not echoed by default.
20. **Migration explicit.** Profile changes require versioned adapters, fixtures, consumer inventory, correction path, and rollback.

[Back to top](#top)

---

<a id="import-and-dependency-direction"></a>

## Import and dependency direction

### Allowed direction

```text
contracts / schemas / policy / domain profiles
                 │
                 ▼
       governed caller or validator
                 │
                 ▼
 packages/identity/src/identity
                 │
                 ├── consumes explicit profile/rules
                 ├── consumes typed digest values
                 └── calls approved pure hashing primitives only when explicitly delegated
```

### Proposed dependency rule

The identity namespace should remain a low-level pure library.

It may depend on:

- the Python standard library;
- immutable value-object and typing support already accepted by repository convention;
- the hashing package through a narrow, reviewed interface;
- an approved Unicode or parsing dependency only when a profile requires it and supply-chain review is complete.

It must not import:

- `connectors/`;
- `pipelines/` or orchestration frameworks;
- lifecycle data access code;
- source registries or resolver clients;
- policy engines;
- receipt/proof/release writers;
- app/API/UI packages;
- model providers;
- credential or secret clients;
- domain packages from the common namespace.

### Import safety

Importing the namespace must not:

- read files or environment variables;
- initialize a registry;
- load network configuration;
- connect to a database;
- generate an identifier;
- inspect the clock;
- emit logs containing identity values;
- mutate global state;
- register plugins implicitly;
- import optional heavy dependencies eagerly.

[Back to top](#top)

---

<a id="profile-bound-module-placement"></a>

## Profile-bound module placement

Before adding a source module, its proposal should identify:

| Requirement | Evidence needed |
|---|---|
| Profile name and version | Accepted contract, schema, ADR, or migration record |
| Meaning | Owning semantic contract |
| Machine shape | Accepted schema or typed package contract |
| Domain/common classification | Domain steward and package steward agreement |
| Normalization behavior | Explicit profile rule and golden vectors |
| Allowed character/length rules | Contract/schema/profile evidence |
| Collision scope | Explicit caller contract |
| Hash dependency | Accepted digest type/profile |
| Error/outcome vocabulary | Reviewed stable reason codes |
| Privacy classification | Policy/privacy review |
| Consumer list | Verified imports or planned migration targets |
| Test vectors | Positive, negative, ambiguity, collision, migration, privacy |
| Compatibility posture | Versioning, deprecation, adapter window |
| Rollback target | Prior version/profile and consumer rollback procedure |

### Source-code admission test

A proposed source file should not be added merely because its name appears in a README. It should be admitted only when:

1. the responsibility cannot remain in an owning contract/schema/domain package;
2. at least two governed consumers need the same pure behavior, or one foundational consumer justifies a shared kernel;
3. the profile and output semantics are accepted;
4. tests can prove deterministic behavior;
5. the dependency direction remains inward and side-effect-free;
6. privacy and sensitive-identity risks are bounded;
7. compatibility and rollback are documented.

[Back to top](#top)

---

<a id="package-namespace-tool-validator-and-caller-delegation"></a>

## Package, namespace, tool, validator, and caller delegation

| Surface | Owns | Must not own |
|---|---|---|
| `packages/identity/` | Package metadata, build, dependency, distribution, versioning, consumer migration | Identity meaning, registry data, policy, release |
| `packages/identity/src/` | Source placement, dependency direction, side-effect rules, implementation admission | Universal grammar, domain sameness, public API |
| `packages/identity/src/identity/` | Proposed pure value types, parsing, formatting, local validation under explicit profiles | Registry resolution, global collision authority, persistence |
| `packages/hashing/` | Accepted canonicalization/digest helpers once implemented | Object/domain identity meaning |
| `tools/validators/identity/` | Validation orchestration, file/stream I/O, report routing when implemented | Contract meaning, policy decisions, release approval |
| Domain packages | Domain adapters implementing accepted domain profiles | Rewriting common contracts or shared package internals |
| Registry/resolver systems | Object existence, uniqueness scope, resolution, aliases as governed state | Generic parsing implementation duplication |
| Policy/review | Sensitivity, rights, access, admissibility, public exposure | String grammar implementation |
| Release/correction | Promotion, correction, supersession, withdrawal, rollback | Low-level parse/format behavior |
| Apps/APIs/UI/AI | Governed use and projection | Direct source-tree authority or internal-store bypass |

### Tool rule

A future CLI may read input, invoke the package, and render a result. The CLI must not contain a second identity grammar. Package and tool outputs must match for the same profile and input.

### Validator rule

A validator may combine schema validation, package-local profile checks, resolver results, policy, and release context. A package-local `VALID` result is only one input to that validator.

### Caller rule

Callers must provide:

- profile identifier and version;
- explicit identity-defining fields;
- collision scope or resolver result where needed;
- digest values with declared profile where needed;
- privacy/audience context outside the pure package when consequential;
- migration mode explicitly, never by fallback.

[Back to top](#top)

---

<a id="side-effect-and-io-boundary"></a>

## Side-effect and I/O boundary

### Denied in source helpers

- network calls;
- ambient filesystem scans;
- direct registry reads or writes;
- database queries;
- lifecycle-store reads or writes;
- receipt, proof, catalog, release, correction, or rollback writes;
- current-time reads unless supplied through an explicit profile-approved clock value;
- randomness unless supplied as explicit governed input—and random identity generation should normally remain outside;
- environment-variable behavior that changes identity;
- locale-sensitive normalization;
- logging full sensitive identifiers;
- model calls or generated-language inference.

### Permitted pure operations

- type and shape checks over explicit inputs;
- profile lookup from an immutable caller-supplied or compiled accepted set;
- parse and format operations;
- explicit normalization required by an accepted profile;
- deterministic comparison and ordering;
- construction of immutable candidate values;
- collision comparison within explicit finite values;
- relation construction from explicit prior/superseding references;
- stable redacted diagnostic summaries.

### I/O adapters

Any file, stream, API, registry, database, or CLI adapter should remain outside the pure namespace or in a clearly separated adapter layer approved by package architecture. Adapters must not become alternate grammar authority.

[Back to top](#top)

---

<a id="security-privacy-and-resource-bounds"></a>

## Security, privacy, and resource bounds

### Credential boundary

The terms “identity” and “token” create a serious ambiguity. Source code in this package must reject or avoid APIs that imply:

- authentication token;
- authorization grant;
- API key;
- bearer token;
- session;
- password reset token;
- consent token;
- cryptographic signature;
- identity-provider assertion;
- access permission.

Those concerns require separate security contracts, systems, and policy.

### Sensitive identity boundary

The common source tree must not:

- resolve a person from partial identifiers;
- infer ownership or residence;
- join living-person records;
- infer kinship or family relationships;
- process DNA/genomic identity;
- expose sensitive actor identifiers;
- reconstruct exact rare-species, archaeology, infrastructure, or private-property locations;
- log restricted source-native keys;
- use examples copied from private or sensitive data.

### Diagnostic rule

Errors and results should prefer:

- profile name;
- field name;
- length;
- safe prefix class;
- stable reason code;
- optional caller-controlled redacted excerpt.

They should not include raw credentials, full private identifiers, full source-native keys, or unrestricted payloads.

### Proposed resource limits

Every parser/formatter should have explicit tested bounds for:

- maximum input length;
- maximum segment count;
- maximum relation count;
- maximum collision-candidate count;
- maximum profile metadata size;
- maximum nesting for typed objects;
- maximum diagnostic excerpt;
- deterministic timeout or operation budget where complex normalization is possible.

Exceeding a limit should produce a typed fail-closed result such as `RESOURCE_LIMIT_EXCEEDED`, not truncation that creates a different identifier.

[Back to top](#top)

---

<a id="testing-fixtures-and-ci"></a>

## Testing, fixtures, and CI

No package-specific identity test boundary or dedicated workflow is confirmed. The following is a proposed minimum before implementation maturity may be claimed.

### Test layers

| Layer | Required proof |
|---|---|
| Import safety | Import performs no I/O, network, time, randomness, registry loading, or logging. |
| Profile selection | Unknown, missing, deprecated, or incompatible profiles fail closed. |
| IdentityToken | Required fields, closed kind values, issuance-time semantics, non-credential handling. |
| Identifier text | Original preservation, exact parsing, formatting, normalization, invalid syntax, Unicode edge cases. |
| Object ID | Same explicit inputs produce same value; changed identity-defining input changes value. |
| Domain boundary | Common helpers preserve domain fields and reject missing domain profile. |
| Collision | Explicit finite scope, duplicate detection, incomplete scope, no random suffixing. |
| References | Parse/format round trip without retargeting or profile collapse. |
| Lineage | Alias, supersession, correction, tombstone, rollback, and migration remain distinct. |
| Hash delegation | Digest values are not recomputed or reformatted silently. |
| Privacy | Sensitive values are not logged or included in diagnostics. |
| Resource bounds | Oversized and adversarial inputs fail deterministically. |
| Tool parity | CLI/validator output matches package output. |
| Cross-language parity | Other implementations match golden vectors if introduced. |
| Migration | Old/new profile adapters are explicit, reversible, and fixture-backed. |

### Fixture classes

- valid common IdentityToken objects for each accepted `kind`;
- invalid missing-field and extra-field objects;
- repeated token instances referencing the same object;
- profile-specific valid and invalid identifier text;
- ambiguous profile candidates;
- reserved namespace and forbidden-character cases;
- Unicode normalization and confusable cases;
- maximum-length and resource-exhaustion cases;
- stable object-ID vectors with identity-defining field changes;
- domain-profile vectors preserving source role, time, support, sensitivity, and lineage;
- collision and incomplete-scope cases;
- alias, supersession, correction, tombstone, withdrawal, and rollback relations;
- incompatible digest profile cases;
- credential-misuse and sensitive-data leakage cases;
- migration forward and rollback vectors.

### CI gates

A future package gate should prove:

1. source imports safely;
2. package builds reproducibly;
3. isolated install succeeds;
4. all profile vectors pass;
5. negative cases fail with stable reason codes;
6. no secret or credential behavior exists;
7. dependency and vulnerability review passes;
8. no direct lifecycle, registry, policy, release, app, UI, or model imports enter the package;
9. tool and validator adapters remain parity-thin;
10. consumer compatibility and migration tests pass.

Generic documentation, schema, or domain checks do not prove this source implementation.

[Back to top](#top)

---

<a id="compatibility-and-migration"></a>

## Compatibility and migration

Identity behavior is compatibility-significant. Changes may affect dedupe, references, catalogs, receipts, proofs, correction lineage, release records, URLs, caches, and public links.

### Breaking or migration-significant changes

- adding or removing an identity profile;
- changing normalization;
- changing allowed characters or case behavior;
- changing segment order, separators, prefixes, or version markers;
- changing identity-defining fields;
- changing collision scope or equality;
- changing `identity_token.kind`;
- making `issuer` required or changing issuance semantics;
- accepting ADR-0013 or changing `run_id` grammar;
- changing import namespace or public exports;
- changing hash profile representation;
- changing alias, supersession, correction, tombstone, or rollback semantics;
- moving domain identity logic into or out of the common package.

### Migration requirements

A governed migration should include:

1. accepted ADR or migration note;
2. old and new profile identifiers;
3. semantic and machine-contract changes;
4. golden vectors for both versions;
5. explicit adapter behavior;
6. consumer inventory;
7. registry/resolver impact;
8. correction and supersession strategy;
9. public-reference and cache impact;
10. compatibility window and removal criteria;
11. receipts or reports appropriate to significance;
12. rollback target and tested rollback procedure.

### Adapter rule

Adapters must be explicit functions or tools named for source and target profiles. Do not hide migration inside a generic parser.

### Historical identity rule

Old identifiers and tokens remain historical evidence. A migration should add governed relation records; it should not erase prior identity or silently rewrite receipts, proofs, or release history.

[Back to top](#top)

---

<a id="smallest-sound-implementation-sequence"></a>

## Smallest sound implementation sequence

### Gate 0 — governance

- assign owners;
- decide whether `identity` is an acceptable import name;
- define the identity-profile registry owner and storage surface;
- reconcile “IdentityToken” versus generic identifier terminology;
- decide ADR-0013 status;
- document common versus domain profile boundaries.

**Stop** if these are unresolved for the proposed slice.

### Gate 1 — package mechanics

- complete `pyproject.toml`;
- select Python version and build backend;
- configure source discovery;
- declare dependencies;
- define distribution and import names;
- add isolated build/import tests.

**Stop** if installability or dependency review fails.

### Gate 2 — one narrow profile

Implement only the common `identity_token` value object or another single accepted profile:

- immutable input/output types;
- explicit parser/constructor;
- schema-aligned validation;
- non-credential guardrails;
- stable results/reason codes;
- no resolver or registry access;
- golden and negative fixtures.

**Stop** if the contract/schema are not reconciled or the declared validator/fixtures remain undefined.

### Gate 3 — identifier text primitives

Add profile-bound identifier parsing only after:

- profile vocabulary is accepted;
- normalization is specified;
- golden vectors exist;
- ambiguity handling is defined;
- privacy review passes.

**Stop** if a universal fallback parser is requested.

### Gate 4 — domain adapters

Allow domain packages to compose common primitives with domain-owned sameness profiles.

**Stop** if common code must import domain packages or discard domain identity fields.

### Gate 5 — lineage and collision values

Add immutable relation values and finite-scope collision helpers.

**Stop** if implementation requires ambient registry access or automatic conflict resolution.

### Gate 6 — tool and validator adapters

Build thin adapters that import the package, perform I/O externally, and emit governed validation/report outputs.

**Stop** if adapters duplicate parsing or become policy/release authority.

### Gate 7 — consumer migration

- inventory consumers;
- run compatibility tests;
- stage profile adapters;
- record correction/supersession impact;
- test rollback;
- remove adapters only after the compatibility window.

[Back to top](#top)

---

<a id="definition-of-done"></a>

## Definition of done

This source envelope may be considered implementation-ready only when:

- [ ] Package and identity stewards are assigned.
- [ ] Distribution and import names are accepted.
- [ ] The build backend, Python range, source discovery, and dependencies are configured.
- [ ] A profile registry owner and versioning model are accepted.
- [ ] The common IdentityToken contract and schema are reconciled.
- [ ] IdentityToken versus identifier-text terminology is unambiguous.
- [ ] Common versus domain identity responsibilities are documented.
- [ ] ADR-0013 status and `run_id` ownership are resolved.
- [ ] The hashing dependency boundary is accepted and implemented enough for required profiles.
- [ ] The first implementation slice is narrower than a universal grammar.
- [ ] Imports are side-effect free.
- [ ] No network, registry, lifecycle, policy, release, app, UI, or model dependency enters the pure namespace.
- [ ] Every accepted profile has positive and negative golden vectors.
- [ ] Unicode, ambiguity, reserved-value, collision, privacy, and resource-limit tests pass.
- [ ] IdentityToken issuance and referenced-object identity remain distinct.
- [ ] Domain profiles preserve source role, object family, time, support, evidence, sensitivity, and lineage.
- [ ] Credentials, authentication, person matching, kinship, ownership, DNA/genomic resolution, and sensitive inference are denied.
- [ ] Tool and validator adapters are parity-thin.
- [ ] CI builds and tests the package in isolation.
- [ ] Consumer inventory and migration tests exist.
- [ ] Correction, deprecation, and rollback paths are tested.
- [ ] Documentation matches accepted behavior.
- [ ] No claim of truth, policy, evidence closure, release, or public safety is derived from local validity.

[Back to top](#top)

---

<a id="verification-register"></a>

## Verification register

| ID | Question | Status |
|---:|---|---|
| ID-SRC-001 | Who owns the identity package and source envelope? | **NEEDS VERIFICATION** |
| ID-SRC-002 | Is `identity` an accepted import namespace without third-party conflict? | **NEEDS VERIFICATION** |
| ID-SRC-003 | Is `kfm-identity` the accepted distribution name? | **NEEDS VERIFICATION** |
| ID-SRC-004 | What Python versions are supported? | **UNKNOWN** |
| ID-SRC-005 | What build backend is accepted? | **UNKNOWN** |
| ID-SRC-006 | How is source discovery configured? | **UNKNOWN** |
| ID-SRC-007 | Which dependencies are approved? | **UNKNOWN** |
| ID-SRC-008 | Is the package intended for internal-only or external distribution? | **UNKNOWN** |
| ID-SRC-009 | Where is the accepted identity-profile registry? | **NEEDS VERIFICATION** |
| ID-SRC-010 | Who can add or change profiles? | **NEEDS VERIFICATION** |
| ID-SRC-011 | Is ADR-0013 accepted, superseded, or still proposed? | **CONFIRMED proposed / decision needed** |
| ID-SRC-012 | Is `run:<orchestrator>:<ULID>` accepted for implementation? | **NEEDS VERIFICATION** |
| ID-SRC-013 | What is the common identifier-text grammar, if any? | **UNKNOWN** |
| ID-SRC-014 | What normalization rules are accepted? | **UNKNOWN** |
| ID-SRC-015 | How are Unicode confusables handled? | **UNKNOWN** |
| ID-SRC-016 | How are namespace and reserved-prefix vocabularies governed? | **UNKNOWN** |
| ID-SRC-017 | Is IdentityToken the exact code/type name? | **NEEDS VERIFICATION** |
| ID-SRC-018 | How is generic non-secret identifier text named? | **NEEDS VERIFICATION** |
| ID-SRC-019 | Is `issued_at` ever part of equality or only token-instance metadata? | **NEEDS VERIFICATION** |
| ID-SRC-020 | Which `identity_token.kind` values are accepted long-term? | **PROPOSED schema / NEEDS VERIFICATION** |
| ID-SRC-021 | Where is the declared IdentityToken validator? | **NOT FOUND** |
| ID-SRC-022 | Where are the declared IdentityToken fixtures? | **NOT FOUND at checked README path** |
| ID-SRC-023 | What common object-ID profiles are accepted? | **UNKNOWN** |
| ID-SRC-024 | Which identity semantics must remain domain-owned? | **NEEDS VERIFICATION** |
| ID-SRC-025 | How are source role and object family preserved? | **NEEDS VERIFICATION per profile** |
| ID-SRC-026 | How are temporal scopes represented without collapse? | **NEEDS VERIFICATION per profile** |
| ID-SRC-027 | How is spatial/support scope represented safely? | **NEEDS VERIFICATION per profile** |
| ID-SRC-028 | Which digest types/profiles may identity values carry? | **NEEDS VERIFICATION** |
| ID-SRC-029 | Is the hashing package ready for dependency use? | **UNKNOWN / implementation unproved** |
| ID-SRC-030 | Who owns global uniqueness and collision authority? | **UNKNOWN** |
| ID-SRC-031 | What finite collision scope can callers supply? | **NEEDS VERIFICATION** |
| ID-SRC-032 | How is incomplete collision scope reported? | **PROPOSED** |
| ID-SRC-033 | Which reference profiles may common code parse? | **NEEDS VERIFICATION** |
| ID-SRC-034 | How are EvidenceRef and IdentityToken kept distinct? | **NEEDS VERIFICATION in tests** |
| ID-SRC-035 | How are source/review/release refs versioned? | **UNKNOWN** |
| ID-SRC-036 | What are accepted alias semantics? | **UNKNOWN** |
| ID-SRC-037 | What are accepted supersession semantics? | **UNKNOWN** |
| ID-SRC-038 | What are accepted correction and tombstone semantics? | **UNKNOWN** |
| ID-SRC-039 | How is rollback lineage represented? | **UNKNOWN** |
| ID-SRC-040 | What sensitive identity categories are prohibited? | **NEEDS VERIFICATION with policy/privacy** |
| ID-SRC-041 | What diagnostics may include identifier excerpts? | **NEEDS VERIFICATION** |
| ID-SRC-042 | What maximum input and collection sizes apply? | **UNKNOWN** |
| ID-SRC-043 | Are optional parsing/Unicode dependencies supply-chain approved? | **UNKNOWN** |
| ID-SRC-044 | Where do package-specific tests live? | **NOT FOUND / NEEDS VERIFICATION** |
| ID-SRC-045 | What dedicated CI workflow will enforce identity behavior? | **NOT FOUND / NEEDS VERIFICATION** |
| ID-SRC-046 | Which executables consume this package? | **NOT ESTABLISHED by bounded search** |
| ID-SRC-047 | How will tool/package parity be tested? | **PROPOSED** |
| ID-SRC-048 | Is cross-language parity required? | **UNKNOWN** |
| ID-SRC-049 | What compatibility window applies to profile changes? | **UNKNOWN** |
| ID-SRC-050 | How are consumer migrations receipted or audited? | **UNKNOWN** |
| ID-SRC-051 | What deprecation signals are required? | **UNKNOWN** |
| ID-SRC-052 | What rollback automation exists? | **UNKNOWN** |
| ID-SRC-053 | How are historical identifiers preserved after migration? | **NEEDS VERIFICATION** |
| ID-SRC-054 | Who reviews domain-profile adapters? | **NEEDS VERIFICATION** |
| ID-SRC-055 | How is package distribution rolled back independently of data release? | **UNKNOWN** |
| ID-SRC-056 | Which checks prove imports remain side-effect free? | **PROPOSED** |

[Back to top](#top)

---

<a id="rollback-correction-deprecation-and-migration"></a>

## Rollback, correction, deprecation, and migration

### Documentation rollback

For this documentation-only change:

- revert the commit that updates `packages/identity/src/README.md`; or
- restore prior blob `4f630edb84ee6d35ee447f779f0798924b2ef513`.

A README rollback does not undo any separately accepted contract, schema, profile, package, registry, or release change.

### Implementation rollback triggers

Rollback or disable an implementation when it:

- silently changes an identifier;
- infers a profile without explicit authority;
- treats IdentityToken as a generic credential or string;
- collapses object, run, content, reference, or token-instance identity;
- flattens domain sameness rules;
- appends random suffixes or mutates a registry;
- reads lifecycle or sensitive stores;
- performs network resolution;
- logs credentials or sensitive identifiers;
- introduces unreviewed dependencies;
- breaks golden vectors or cross-boundary parity;
- allows local validity to stand in for object existence, evidence, policy, release, or public safety.

### Correction posture

A correction should:

- preserve the prior identifier and profile;
- name the corrected or superseding identity explicitly;
- record the reason and governing review;
- preserve affected references and historical receipts;
- identify consumers and released surfaces;
- remain reversible until the correction is accepted.

### Deprecation posture

Deprecation requires:

- named old and replacement profiles/APIs;
- warning or report behavior that does not leak sensitive values;
- a compatibility window;
- fixture and consumer coverage;
- removal criteria;
- rollback instructions.

### Package rollback versus data rollback

Reverting a software package version is not the same as rolling back KFM data or a public release. Package rollback restores code behavior. Data/release rollback remains governed by lifecycle, receipt, proof, correction, and release controls.

### Final rule

When identity evidence is incomplete, narrow the supported profile or abstain. Do not let a fluent universal API replace contracts, schemas, domain semantics, registry evidence, policy, review, correction, or release state.

[Back to top](#top)
