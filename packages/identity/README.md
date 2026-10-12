<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-identity-readme
title: packages/identity/ — Deterministic Identity Package, Distribution, and Compatibility Boundary
type: readme
version: v1.1
status: draft
owners: OWNER_TBD — Package steward · Identity steward · Contract steward · Schema steward · Domain stewards · Privacy reviewer · Sensitivity reviewer · Security steward · Dependency steward · Validation steward · Release steward · Migration steward · CI steward · Docs steward
created: NEEDS VERIFICATION — target existed before the current evidence-grounded revision
updated: 2026-07-15
policy_label: "public-doctrine; package-boundary; deterministic-identity; implementation-empty; distribution-unratified; api-unratified; profile-registry-unsettled; identity-token-separated; domain-identity-separated; run-id-separated; hashing-delegated; supply-chain-aware; non-credential; no-network; pure-functions; fail-closed; privacy-aware; no-authority; no-secrets; migration-required; rollback-aware"
current_path: packages/identity/README.md
truth_posture: CONFIRMED target README v1, merged source-envelope and import-namespace READMEs v1.1, empty identity package initializer, kfm-identity 0.0.0 placeholder metadata, packages root and Directory Rules placement, merged hashing package boundary v1.1, draft IdentityToken contract v0.3 and PROPOSED schema, missing declared IdentityToken validator and fixture README at bounded paths, README-only Identity validator routing lane, placeholder identity validator modules, PROPOSED ADR-0013, draft identity/evidence architecture notes, confirmed EvidenceRef contract, representative domain-owned Fauna identity contract, and bounded absence of proposed implementation modules, package-specific tests/workflows, package publishing configuration, and executable consumers / PROPOSED package metadata contract, dependency and supply-chain controls, profile-first public API, package/source/namespace/tool/validator delegation, distribution and versioning rules, typed outcomes, resource limits, consumer inventory, compatibility testing, staged implementation, correction, migration, deprecation, and rollback / CONFLICTED common identity_token object versus generic identifier-token string terminology, stable referenced-object identity versus issued token-instance identity, universal KFM ID grammar proposals versus unconstrained common schema id and domain-owned identity semantics, proposed ADR run_id grammar versus unaccepted implementation, generic package versus domain-specific sameness rules, package name kfm-identity versus unratified import namespace identity, and rich documentation versus empty implementation / UNKNOWN accepted identifier-profile registry, namespace grammar, normalization rules, Python runtime, build backend, dependency set, source discovery, export surface, consumer inventory beyond bounded search, collision authority, resolver behavior, artifact reproducibility, cross-language parity, package publishing posture, CI enforcement, deployment use, and operational health / NEEDS VERIFICATION owners, accepted ADR or migration decision, identity-profile vocabulary, common/domain boundary, dependency approval, package metadata, API shape, privacy review, test vectors, collision-scope contract, consumer migration, CI gates, distribution policy, correction path, compatibility period, deprecation, and rollback automation
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: bd957101efb7d9215719c45b107baacfd924ce79
  prior_blob: ba5f4c0b3e425448906acc6e5e393eefce60ab8b
  source_readme_blob: d1ff780d5266a91245f9c31b22565c23a2347eb6
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
    - packages/identity/README.md existed at version v1 before this revision
    - packages/identity/src/README.md exists at version v1.1
    - packages/identity/src/identity/README.md exists at version v1.1
    - packages/identity/src/identity/__init__.py exists and is empty
    - packages/identity/pyproject.toml contains only project name kfm-identity and version 0.0.0
    - packages/identity/package.json was not found
    - grammar.py, namespaces.py, object_id.py, refs.py, lineage.py, validation.py, token_string.py, and fixtures.py were not found under packages/identity/src/identity/
    - packages/identity/tests/README.md and tests/packages/identity/README.md were not found
    - .github/workflows/identity.yml and package-identity.yml were not found
    - tools/validators/validate_identity_token.py was not found
    - fixtures/contracts/v1/common/identity_token/README.md was not found
    - tools/validators/identity/jcs_spec_hash.py is a documentation-only placeholder
    - tools/validators/evidence/validate_identity.py is a documentation-only placeholder
    - bounded code search did not establish an executable consumer importing the identity package
related:
  - src/README.md
  - src/identity/README.md
  - src/identity/__init__.py
  - pyproject.toml
  - ../README.md
  - ../hashing/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0013-spec_hash-and-run_id-identity-grammar.md
  - ../../docs/architecture/identity-and-spec-hash.md
  - ../../docs/architecture/evidence-identity.md
  - ../../contracts/common/identity_token.md
  - ../../schemas/contracts/v1/common/identity_token.schema.json
  - ../../contracts/evidence/evidence_ref.md
  - ../../contracts/domains/fauna/domain_feature_identity.md
  - ../../contracts/domains/hydrology/reach_identity.md
  - ../../contracts/domains/settlements-infrastructure/place-identity.md
  - ../../tools/validators/identity/README.md
  - ../../tools/validators/identity/jcs_spec_hash.py
  - ../../tools/validators/evidence/validate_identity.py
  - ../../contracts/
  - ../../schemas/
  - ../../policy/
  - ../../data/registry/
  - ../../data/receipts/
  - ../../data/proofs/
  - ../../release/
tags: [kfm, packages, identity, deterministic-identity, identity-token, identifier-profile, object-id, run-id, reference, alias, supersession, tombstone, collision, domain-identity, hashing, privacy, packaging, dependencies, supply-chain, distribution, compatibility, migration, fail-closed]
notes:
  - "This revision changes only packages/identity/README.md."
  - "The package currently contains documentation, 0.0.0 placeholder metadata, and an empty import initializer; proposed implementation modules were not found at checked paths."
  - "This README does not activate an API, select a universal identifier grammar, accept ADR-0013, define domain sameness, create a collision registry, approve dependencies, or authorize package publication."
  - "The common identity_token object, identifier strings, stable object ids, run ids, evidence/source/release references, aliases, and domain feature identities remain separate governed profiles."
  - "A well-formed identifier is not object existence, actor identity, evidence closure, policy approval, release approval, or public safety."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Deterministic Identity Package, Distribution, and Compatibility Boundary

`packages/identity/`

> Repository-present package lane for a future reusable deterministic identity library. Current evidence establishes documentation, `0.0.0` placeholder metadata, and an empty import initializer—not an installable, exported, tested, published, or CI-enforced identity package.

![status](https://img.shields.io/badge/status-draft-yellow)
![version](https://img.shields.io/badge/version-v1.1-informational)
![maturity](https://img.shields.io/badge/maturity-package__scaffold-lightgrey)
![profiles](https://img.shields.io/badge/profiles-unsettled-orange)
![identity token](https://img.shields.io/badge/identity__token-typed__reference-blue)
![distribution](https://img.shields.io/badge/distribution-NOT__AUTHORIZED-critical)
![credentials](https://img.shields.io/badge/credentials-DENIED-critical)
![authority](https://img.shields.io/badge/truth__authority-none-red)

**Quick links:** [Purpose](#purpose) · [Evidence](#status-and-evidence) · [Placement](#directory-rules-and-authority) · [Responsibilities](#package-responsibilities) · [Profiles](#identity-profile-separation) · [Conflicts](#compatibility-conflicts) · [Tree](#confirmed-package-tree) · [Invariants](#keystone-invariants) · [Metadata](#package-metadata-and-distribution) · [Dependencies](#dependency-and-supply-chain-boundary) · [API](#public-api-and-versioning) · [Consumers](#caller-and-consumer-contract) · [Delegation](#package-source-namespace-tool-validator-and-release-delegation) · [Security](#security-privacy-and-resource-bounds) · [Testing](#testing-build-and-ci) · [Migration](#compatibility-consumer-migration-and-deprecation) · [Implementation](#smallest-sound-implementation-sequence) · [Done](#definition-of-done) · [Open](#verification-register) · [Rollback](#rollback-correction-and-package-release)

> [!IMPORTANT]
> **This README is not an implementation, API, grammar, dependency, distribution, resolver, registry, or migration decision.** It does not establish exports, a build backend, a universal KFM identifier syntax, accepted normalization rules, collision authority, domain sameness, an accepted `run_id` grammar, CI enforcement, package publication, or operational consumers.

> [!CAUTION]
> **A valid identifier is not proof of identity or truth.** It establishes only local conformance to a declared profile. Object existence, actor identity, source authority, evidence support, rights, sensitivity, policy, review, release, and public safety remain separate governed checks.

---

<a id="purpose"></a>

## Purpose

This README defines the package-level boundary for `packages/identity/`.

A conforming package may eventually provide a reusable, deterministic library for governed callers that need to:

- parse and format identifiers under explicit, versioned identity profiles;
- preserve original text separately from normalized or display forms;
- validate profile-specific syntax, kind, namespace, length, and reserved values;
- construct the current common `identity_token` object from explicit fields;
- compare candidates within explicit caller-supplied collision scopes;
- represent alias, supersession, correction, tombstone, and migration relations from audit-backed inputs;
- accept digest values from [`packages/hashing/`](../hashing/README.md) without reimplementing canonicalization or hash semantics;
- return deterministic typed results and stable reason codes;
- expose a small, versioned import API after contracts, profiles, tests, and consumers are accepted.

The package root additionally owns **package mechanics** once approved:

- distribution identity and version metadata;
- build backend and source discovery;
- dependency declaration and supply-chain review;
- supported runtime versions;
- package-level compatibility and deprecation policy;
- public export control;
- wheel, sdist, isolated-install, import, and test gates;
- consumer inventory and migration support;
- software-distribution rollback.

The package must not become:

- a second contract, schema, identity-profile registry, domain-model, or policy home;
- a universal identity service that defines sameness for every KFM object;
- a registry writer, collision authority, network resolver, lifecycle store, or catalog writer;
- an authentication, authorization, credential, consent, identity-provider, session, or secret-management system;
- a person-matching, property-ownership, kinship, DNA/genomic, or sensitive-location inference system;
- a public API, UI, map, export, search, embedding, or AI answer surface;
- a compatibility shortcut that silently repairs, normalizes, suffixes, retargets, merges, or migrates identifiers;
- a package whose release is confused with KFM data or claim publication.

[Back to top](#top)

---

<a id="status-and-evidence"></a>

## Status and evidence

| Surface | Status | Safe conclusion |
|---|---:|---|
| This README | **CONFIRMED v1 before revision** | A package boundary exists. |
| `src/README.md` | **CONFIRMED v1.1** | Source placement, dependency direction, and implementation admission are documented. |
| `src/identity/README.md` | **CONFIRMED v1.1** | The proposed import namespace has an evidence-grounded profile and compatibility boundary. |
| `src/identity/__init__.py` | **CONFIRMED empty** | No exports, import behavior, or side effects are established. |
| `pyproject.toml` | **CONFIRMED `kfm-identity` `0.0.0` placeholder** | No build backend, dependencies, source discovery, runtime range, entry points, or publishing posture is established. |
| `package.json` | **NOT FOUND** | No Node/TypeScript package surface is established. |
| Proposed implementation modules | **NOT FOUND at bounded paths** | No grammar, token, object-ID, reference, lineage, collision, or validation implementation is established. |
| Package-specific tests | **NOT FOUND at checked README paths** | No dedicated identity package test boundary is established. |
| Package-specific workflows | **NOT FOUND at checked paths** | No dedicated identity CI behavior is established. |
| Executable consumers | **NOT ESTABLISHED by bounded search** | Documentation, contracts, and placeholders are not proof of importing callers. |
| Common `identity_token` contract | **CONFIRMED draft v0.3** | Defines a small typed reference object; explicitly not a credential or proof of identity. |
| Common `identity_token` schema | **CONFIRMED `PROPOSED` machine surface** | Requires `id`, `kind`, and `issued_at`; `issuer` is optional; `id` has no universal grammar pattern. |
| Declared IdentityToken validator | **NOT FOUND** | Schema metadata does not prove executable validation. |
| Declared IdentityToken fixture README | **NOT FOUND** | No common fixture coverage is established. |
| Identity validator routing lane | **CONFIRMED README-only boundary** | Broad validation responsibilities are documented; runtime wiring remains unproved. |
| Checked identity validator modules | **CONFIRMED placeholders** | They contain provenance comments, not validation behavior. |
| ADR-0013 | **CONFIRMED `proposed`** | Proposes `spec_hash` and `run_id` grammar; not accepted implementation fact. |
| EvidenceRef contract | **CONFIRMED draft/profiled contract** | Evidence pointers remain evidence-owned, not generic identity aliases. |
| Representative Fauna identity contract | **CONFIRMED draft/domain-owned** | Domain sameness preserves source role, family, time, support, evidence, sensitivity, and lineage. |
| Hashing package boundary | **CONFIRMED v1.1 documentation** | Digest and canonicalization semantics remain delegated; implementation is still empty/unratified. |

### Truth posture

**CONFIRMED**

- The package is an implementation scaffold, not a functioning identity subsystem.
- Package metadata is a greenfield `0.0.0` placeholder.
- The source and namespace READMEs are evidence-grounded v1.1 boundaries.
- The common `identity_token` is a typed object, not a generic token string and not a credential.
- Domain identity meaning remains domain-owned.
- Checked validators do not establish executable behavior.
- No dedicated identity workflow, test boundary, publishing configuration, or consumer was established.

**PROPOSED**

- Package metadata and build rules.
- Dependency and supply-chain controls.
- A minimal profile-first public API.
- Package/source/namespace/tool/validator delegation.
- Finite result and reason-code families.
- Consumer inventory and compatibility testing.
- Distribution, deprecation, migration, correction, and rollback rules.
- Staged implementation and release gates.

**CONFLICTED**

- `identity_token` object terminology versus generic “identifier token” string terminology.
- Referenced-object identity versus token-instance issuance identity.
- Universal grammar proposals versus an unconstrained common `id` field and domain-owned semantics.
- Proposed ADR-0013 `run_id` grammar versus unaccepted implementation.
- Generic package ambitions versus domain-specific definitions of sameness.
- Distribution name `kfm-identity` versus unratified import namespace `identity`.
- Documentation richness versus empty implementation.

**UNKNOWN**

- Accepted identity-profile registry.
- Universal or shared grammar, if any.
- Normalization and comparison rules.
- Python runtime and build backend.
- Dependency set and approved versions.
- Package discovery and import behavior.
- Export surface and consumer inventory.
- Collision authority and resolver behavior.
- Cross-language parity.
- Artifact reproducibility, publishing posture, CI enforcement, deployment use, and operational health.

**NEEDS VERIFICATION**

- Owners and CODEOWNERS coverage.
- Accepted ADR or migration decision.
- Common-versus-domain identity boundary.
- Package/import naming and metadata.
- Dependency approvals and supply-chain posture.
- API shape, privacy review, fixtures, test vectors, and collision-scope contract.
- Consumer migration, CI gates, distribution policy, correction, deprecation, and rollback automation.

[Back to top](#top)

---

<a id="directory-rules-and-authority"></a>

## Directory Rules and authority

`packages/identity/` is a sound **responsibility root** for a future reusable implementation because [`packages/`](../README.md) owns shared libraries.

| Concern | Owning root | Package relationship |
|---|---|---|
| Shared identity implementation | `packages/identity/` | May implement accepted pure helpers. |
| Source placement | `packages/identity/src/` | Defines module placement and dependency direction. |
| Import namespace | `packages/identity/src/identity/` | May expose an accepted, minimal API. |
| Hashing/canonicalization | `packages/hashing/` | Separate package; identity consumes declared digests. |
| Semantic meaning | `contracts/` | Package implements; contracts define meaning. |
| Machine shape | `schemas/` | Package validates against accepted shapes; does not redefine them. |
| Domain sameness | domain contracts/docs | Package must not invent or flatten it. |
| Registries and source authority | `data/registry/` and accepted control surfaces | Package receives explicit context; does not mutate authority. |
| Policy and sensitivity | `policy/` | Package may preserve policy metadata but does not decide access. |
| Validators and operator tools | `tools/` | May wrap the package after ownership is accepted. |
| Fixtures and tests | `fixtures/`, `tests/` | Provide executable evidence outside package prose. |
| Receipts and proofs | `data/receipts/`, `data/proofs/` | Callers persist trust artifacts; package returns facts only. |
| Release, correction, rollback | `release/` | Package release and KFM publication remain separate events. |
| Public interfaces | `apps/`, governed APIs, released artifacts | Must not expose package internals as authority. |

The package may implement reusable mechanics. It must not become a parallel home for schemas, contracts, profile registries, identity records, lifecycle data, policy decisions, proofs, receipts, release manifests, public payloads, or sensitive identity material.

[Back to top](#top)

---

<a id="package-responsibilities"></a>

## Package responsibilities

### Package-root responsibilities

After approval, the package root may own:

1. distribution name and version;
2. build backend and source-layout configuration;
3. supported runtime versions;
4. dependencies and optional extras;
5. dependency pinning or lock integration required by repository policy;
6. source discovery;
7. typed-package marker configuration;
8. public export and semantic-versioning rules;
9. package build and isolated-install tests;
10. consumer compatibility policy;
11. package changelog and migration notices;
12. software rollback instructions.

### Responsibilities it delegates

The package root delegates:

- source-file placement to [`src/README.md`](src/README.md);
- proposed namespace behavior to [`src/identity/README.md`](src/identity/README.md);
- digest semantics to [`packages/hashing/`](../hashing/README.md);
- identity meaning to common and domain contracts;
- machine shape to schemas;
- policy, rights, sensitivity, and audience decisions to policy/release systems;
- collision-scope authority and registry mutation to explicit governed callers;
- validation orchestration and reporting to accepted validator/tool lanes;
- persistence to owning registries, receipt, proof, catalog, and release roots;
- public serialization to governed applications and APIs.

### Package non-responsibilities

The package does not own:

- the truth that an entity exists;
- proof that two records refer to the same real-world thing;
- actor authentication or authorization;
- personhood, ownership, kinship, consent, or identity-provider assertions;
- source authority;
- evidence closure;
- policy permission;
- release or public exposure;
- a universal cross-domain identity mega-model.

[Back to top](#top)

---

<a id="identity-profile-separation"></a>

## Identity profile separation

| Profile | Identifies | Meaning owner | Package posture |
|---|---|---|---|
| Common `identity_token` | An issued typed reference object | Common contract/schema | Construct, parse, and validate only after accepted API design. |
| Identifier text | A string under a declared grammar/profile | Profile contract/ADR/schema | Never infer profile from appearance alone. |
| Stable object ID | A governed object identity slot | Object/domain contract | Require explicit profile and identity-defining fields. |
| Activity/run ID | One execution/activity | Runtime/receipt contract and accepted ADR | Keep independent from content identity. |
| Content/spec hash | Canonical bytes/content | Hashing package and hash contracts | Consume; do not duplicate. |
| EvidenceRef | Supporting-material pointer | Evidence contracts | Preserve evidence semantics and closure state. |
| SourceDescriptor reference | Source identity pointer | Source contracts/registry | Do not create or activate descriptors. |
| Receipt/review/decision/release reference | Governance-object pointer | Owning contract/root | Parse/format only under explicit profile. |
| Actor reference | Governed actor pointer | Actor/governance/security contracts | Never treat as authentication credential. |
| Alias/supersession/tombstone relation | Identity continuity event | Correction/release/domain contract | Immutable relation candidate; no silent retargeting. |
| Domain feature identity | Domain-specific sameness | Domain contracts and stewards | Common package must not define the recipe. |
| Display slug or label | Human-facing navigation aid | UI/catalog profile | Never treat as canonical identity unless explicitly governed. |

A profile identifier must travel with the values or context needed to interpret it. “Looks like a KFM ID” is not an accepted profile.

[Back to top](#top)

---

<a id="compatibility-conflicts"></a>

## Compatibility conflicts

### `identity_token` object versus token string

The common contract defines an object with `id`, `kind`, `issued_at`, and optional `issuer`. The current schema does not define a universal grammar for `id`. Therefore the package must not equate the full object, its `id` field, a local identifier segment, a credential token, a run ID, or a content hash.

### Stable identity versus token issuance identity

`identity_token.issued_at` describes token issuance. It is not necessarily object creation, observation, source, valid, transaction, review, release, or correction time.

### Common grammar versus domain sameness

A common parser may validate a declared string profile. It cannot decide that two fauna, geology, hydrology, settlement, people, or other domain objects are the same. Domain identity contracts may require source role, object family, temporal scope, spatial support, sensitivity, evidence, and correction context.

### `run_id` proposal versus accepted behavior

ADR-0013 proposes `run:<orchestrator>:<ULID>`, but the ADR remains proposed. The package must not ship a default generator or validator until the decision, controlled vocabulary, compatibility plan, and tests are accepted.

### Package name versus import namespace

`kfm-identity` is present in placeholder metadata. The import name `identity` is documentation-led and unratified. Before publishing or adding consumers, verify third-party collisions, source discovery, import behavior, distribution-to-import mapping, internal conventions, and migration cost.

### Hash-bearing identity

The package may consume a digest plus declared hash profile. It must not recompute through an implicit algorithm, remove canonicalization prefixes, wrap or unwrap incompatible shapes silently, convert SHA-256 and BLAKE3, treat digest equality as semantic identity, or embed a run ID into content identity.

### Documentation versus implementation

Rich README proposals are not executable evidence. Adding code requires accepted contracts/profiles, module ownership, fixtures, tests, consumers, and rollback.

[Back to top](#top)

---

<a id="confirmed-package-tree"></a>

## Confirmed package tree

```text
packages/identity/
├── README.md
├── pyproject.toml
└── src/
    ├── README.md
    └── identity/
        ├── README.md
        └── __init__.py   # empty
```

The following are **PROPOSED only** and were not found at checked paths:

```text
src/identity/
├── profiles.py
├── identity_token.py
├── identifier_text.py
├── object_id.py
├── run_id.py
├── refs.py
├── lineage.py
├── collision.py
├── outcomes.py
└── py.typed
```

Do not create this full tree merely because it appears here. Add the smallest module justified by an accepted profile, caller, contract, schema, fixture set, test, and rollback plan.

[Back to top](#top)

---

<a id="keystone-invariants"></a>

## Keystone invariants

1. A valid identifier is not proof of real-world identity or truth.
2. Identity parsing requires an explicit profile; profile guessing is denied.
3. Original text and normalized/display text remain distinct.
4. Normalization must be profile-declared, deterministic, tested, and non-lossy or explicitly receipted.
5. Stable object identity, activity identity, content identity, reference identity, and token issuance identity remain distinct.
6. The common `identity_token` object is not a generic string token.
7. `identity_token` is not a credential, consent grant, session, bearer token, API key, or authentication proof.
8. Domain sameness remains domain-owned.
9. Hash semantics remain owned by `packages/hashing/` and accepted contracts.
10. Collision checks use a finite caller-supplied scope; package code does not scan registries.
11. Collision results fail closed; no random suffix or silent overwrite.
12. Alias, supersession, correction, tombstone, and migration are explicit relations, not hidden rewrites.
13. Invalid input is not silently repaired into a different identity.
14. Unsupported profiles fail closed.
15. The package is no-network and import-safe.
16. Package code does not read or write lifecycle stores, registries, receipts, proofs, catalogs, releases, or public payloads.
17. Sensitive actor, person, genomic, property, or location data is not logged or placed in public fixtures.
18. Package release is software distribution, not KFM publication.
19. Public clients use governed interfaces, not package internals.
20. Compatibility changes require consumer inventory, migration, tests, and rollback.

[Back to top](#top)

---

<a id="package-metadata-and-distribution"></a>

## Package metadata and distribution

Current `pyproject.toml` establishes only:

```toml
[project]
name = "kfm-identity"
version = "0.0.0"
```

Before installability or distribution can be claimed, package metadata must establish and verify:

| Area | Required decision/evidence |
|---|---|
| Build backend | Approved backend and reproducible configuration. |
| Source discovery | Explicit mapping for the `src/` layout. |
| Runtime range | Supported Python versions, tested in CI. |
| Distribution name | Confirm `kfm-identity`. |
| Import name | Confirm or replace `identity`. |
| Dependencies | Minimal reviewed list with purpose and ownership. |
| Optional dependencies | Explicit extras only where justified. |
| Package data | Include only intended files such as `py.typed`. |
| Entry points | None by default; CLI belongs in a tool adapter unless accepted otherwise. |
| Licensing | Repository-compatible metadata and dependency license review. |
| Versioning | Pre-1.0 compatibility policy and release process. |
| Publishing | Internal-only or registry publication decision; default is not authorized. |
| Provenance | Build receipt, SBOM, or provenance requirements where repository policy requires them. |

A package must not be published merely because it builds. Publication requires accepted owners, package/import names, API and profiles, dependency review, tests, consumer inventory, reproducible-build evidence, artifact inspection, distribution policy, and rollback instructions.

[Back to top](#top)

---

<a id="dependency-and-supply-chain-boundary"></a>

## Dependency and supply-chain boundary

Prefer the standard library and explicit small value objects. A dependency is justified only when it reduces risk more than it adds.

Each dependency should document:

- exact purpose and used surface;
- why local implementation is riskier;
- license and maintenance posture;
- security history and transitive dependencies;
- deterministic behavior;
- Unicode and normalization behavior where relevant;
- supported runtime/platform matrix;
- update and rollback owner.

Dependencies must not perform network calls on import or normal library execution, read environment credentials, inspect local identity services, emit telemetry, load mutable remote profile registries, silently normalize identifiers, generate credentials, write ambient caches, or broaden the package into an identity-provider SDK.

Allowed dependency direction:

```text
packages/identity  ---> packages/hashing
```

Denied circular direction:

```text
packages/hashing  -X-> packages/identity
```

Before release, verify resolved versions, license review, vulnerability scan, SBOM where required, isolated build, wheel/sdist contents, import with network disabled, deterministic vectors, and rollback to the previous accepted artifact.

[Back to top](#top)

---

<a id="public-api-and-versioning"></a>

## Public API and versioning

The public API should be profile-first, explicit, typed, deterministic, side-effect free, small, test-vector backed, and incapable of silently crossing authority boundaries.

These names are illustrative, not accepted exports:

| Family | Possible operation | Required posture |
|---|---|---|
| Profile lookup | `get_profile(profile_id)` | Packaged accepted profile only; no network registry. |
| Identifier parse | `parse_identifier(text, profile)` | Preserve original text and typed result. |
| Identifier format | `format_identifier(parts, profile)` | Fail on missing or unsupported fields. |
| Identifier validation | `validate_identifier(text, profile)` | Local profile conformance only. |
| IdentityToken construction | `make_identity_token(id, kind, issued_at, issuer)` | Contract-shaped object; not credential issuance. |
| IdentityToken validation | `validate_identity_token(value)` | Checks bounded by accepted contract/profile. |
| Candidate object ID | `build_object_id(parts, profile)` | Domain/profile defines identity inputs. |
| Collision comparison | `compare_candidates(candidates, scope)` | Finite explicit scope only. |
| Lineage relation | `make_supersession(old, new, context)` | Immutable candidate; caller persists. |
| Reference parse | `parse_reference(value, profile)` | Preserve owning reference semantics. |
| Outcome formatting | `IdentityResult`, `IdentityReason` | Stable, non-sensitive diagnostics. |

Do not export authentication, authorization, login, session, credential, person matching, ownership/kinship inference, registry mutation, publication, network resolution, profile guessing, or silent repair functions.

| Change | Expected class |
|---|---|
| Documentation clarification without behavior change | Patch |
| Additive compatible outcome field | Minor or profile-version change |
| New profile without existing-profile behavior change | Minor after profile registration |
| New `identity_token.kind` | Schema/contract compatibility event; not package-only |
| Grammar or normalization change | Breaking/profile-version migration |
| Import path or public symbol rename | Breaking package change |
| Collision behavior change | Breaking and governance-significant |
| Domain identity recipe change | Domain contract/schema migration |
| `run_id` grammar acceptance/change | ADR + contract/schema + package migration |
| Dependency changing normalization/comparison | Breaking unless proven identical |

[Back to top](#top)

---

<a id="caller-and-consumer-contract"></a>

## Caller and consumer contract

Callers supply explicit profile/version, original value or identity parts, domain/object family, source role, time and support scope, declared digest profile, finite collision scope, lineage context, and privacy constraints where material.

The package returns a parsed or formatted candidate, preserved original representation, declared profile/version, normalized representation only when allowed, deterministic status, stable reason codes, privacy-safe diagnostics, and no persistence, policy, evidence, or release decision.

Callers remain responsible for object existence, registry resolution, source authority, collision-scope completeness, schema/contract checks outside local helper scope, evidence resolution, policy and sensitivity, persistence, receipts/proofs, review/release, public-safe projection, correction, and rollback.

Before the first stable API or breaking change, maintain a confirmed inventory of importing packages, validators/tools, pipelines/workers, API assemblers, catalog/triplet builders, release tooling, tests/fixtures, and artifacts embedding package-produced identifiers. Code search is evidence input, not a complete consumer inventory.

[Back to top](#top)

---

<a id="package-source-namespace-tool-validator-and-release-delegation"></a>

## Package, source, namespace, tool, validator, and release delegation

| Layer | Owns | Must not own |
|---|---|---|
| Package root | Metadata, build, dependencies, API/versioning, distribution, compatibility | Identity meaning, domain sameness, registry authority |
| `src/` | Source placement, dependency direction, module admission, side-effect limits | Build publication, profile authority |
| `src/identity/` | Accepted pure profile-bound values and operations | Universal grammar, registry scanning, public truth |
| Hashing package | Canonicalization/digest mechanics after acceptance | Object identity semantics |
| Contracts | Meaning and invariants | Executable implementation |
| Schemas | Machine shape | Semantic proof |
| Domain contracts | Domain sameness | Common package distribution |
| Validators/tools | Orchestration, reports, CLI behavior | Contract meaning, policy approval |
| Registries | Reserved namespaces and recorded identities | Package implementation |
| Policy | Rights, sensitivity, audience, allow/deny/restrict/abstain | Identifier mechanics |
| Receipts/proofs | Auditable results | Package source code |
| Release | Publication, correction, withdrawal, rollback | Software package internals |
| Apps/APIs | Governed projections | Canonical internal authority |

A `kfm-identity` package release distributes implementation code and may change APIs. It does not promote records, publish claims or maps, approve sensitive identity exposure, close evidence, or issue a data/claim ReleaseManifest.

[Back to top](#top)

---

<a id="security-privacy-and-resource-bounds"></a>

## Security, privacy, and resource bounds

The package must not accept or emit passwords, API keys, JWTs, bearer tokens, OAuth tokens, authentication session IDs, private keys, signing secrets, consent grants, or access-control decisions.

It must not infer, match, expose, or retain living-person identity beyond explicit governed references; DNA/genomic identity; kinship or genealogy conclusions; private property ownership; restricted archaeology identities or locations; rare-species exact locations; sensitive infrastructure identifiers; or hidden re-identification join keys.

Diagnostics may include profile ID, field/path, status/reason code, safe length/count metadata, and an allowed redacted correlation value. They must not contain full sensitive identifiers, credentials, raw person records, genomic values, restricted coordinates, source payloads, or unrestricted lineage context.

Accepted implementations should define maximum identifier length, segment count, profile size, collision-scope size, relation depth, diagnostic count, recursion depth, and time/memory budgets. Limit exceedance fails closed.

Importing the package must not perform network calls, read environment secrets, scan repositories/registries, create files, write identifier values to logs, register telemetry, mutate global profiles, or initialize model/database/identity-provider clients.

[Back to top](#top)

---

<a id="testing-build-and-ci"></a>

## Testing, build, and CI

Unit tests must cover valid round trips, invalid syntax, unsupported profiles, reserved namespaces, length/count boundaries, Unicode and case behavior, declared normalization, original-value preservation, typed `identity_token` construction, token issuance time separation, collision/ambiguity outcomes, immutable lineage, privacy-safe diagnostics, and import-side-effect absence.

Negative tests must cover profile guessing, silent repair, automatic suffixing, registry scanning, credential misuse, unsupported kinds, missing collision scope, digest/profile mismatch, content/run/object identity collapse, EvidenceRef collapse, domain identity without a domain profile, sensitive inference, resource exhaustion, and network access attempts.

Maintain golden vectors for every accepted profile/version, public API, serializable result, deprecated compatibility window, package/tool/validator parity, and cross-language implementation where present.

Before distribution:

1. build sdist and wheel in isolation;
2. inspect artifact contents;
3. install in a clean environment;
4. import with network disabled;
5. run package and golden-vector tests;
6. run dependency/license scans;
7. verify no undeclared files or credentials;
8. verify source/import mapping;
9. retain the prior accepted artifact for rollback.

A green generic workflow proves only what it executes. It does not prove identity semantics, profile acceptance, domain sameness, collision authority, privacy correctness, consumer migration, or package publication approval.

[Back to top](#top)

---

<a id="compatibility-consumer-migration-and-deprecation"></a>

## Compatibility, consumer migration, and deprecation

Migration-class changes include accepting or changing a profile, normalization, case sensitivity, reserved prefixes, `identity_token.kind`, `run_id`, package/import name, collision semantics, lineage shape, hash representation, or common/domain ownership.

A migration plan should state old/new versions, affected contracts and schemas, confirmed consumers, dual-read/write posture if allowed, conversion rules, ambiguity handling, privacy review, fixtures and tests, compatibility window, warnings, correction path, and rollback target.

The package must not silently replace profiles, rewrite identifiers, normalize legacy values, change wrappers or hash prefixes, change kinds, retarget references, turn aliases into canonical IDs, or hide collisions.

Deprecation requires an owner, replacement, consumer inventory, warning period, migration tooling outside the pure core when needed, tests for both behaviors, removal condition, and rollback. Historical references remain inspectable after deprecation.

[Back to top](#top)

---

<a id="smallest-sound-implementation-sequence"></a>

## Smallest sound implementation sequence

1. Assign package, identity, privacy, security, contract, schema, dependency, and migration owners.
2. Confirm package implementation ownership.
3. Resolve distribution and import names.
4. Accept or reject a shared profile-registry design.
5. Reconcile token-object and identifier-string terminology.
6. Define the common-versus-domain boundary.
7. Resolve ADR-0013 before implementing default `run_id`.
8. Approve dependency policy and runtime.
9. Add complete metadata and source discovery.
10. Implement one narrow profile or value object only.
11. Add fixtures and tests for that slice.
12. Add privacy and resource-limit tests.
13. Add build/install/import checks.
14. Add one confirmed consumer through the accepted API.
15. Add package/tool/validator parity tests where adapters exist.
16. Record consumer inventory and migration posture.
17. Approve distribution posture.
18. Publish only through an accepted software-release process.
19. Retain and test rollback to the prior accepted artifact.

Stop when identity meaning, ownership, package names, privacy posture, collision scope, hashing representation, fixtures/tests, or rollback responsibility is unresolved.

[Back to top](#top)

---

<a id="definition-of-done"></a>

## Definition of done

### Governance

- [ ] Package and cross-cutting owners are assigned.
- [ ] Directory Rules placement remains accepted.
- [ ] Common/domain ownership is documented.
- [ ] Profile and ADR decisions are accepted.
- [ ] Privacy and sensitivity review is complete.

### Package mechanics

- [ ] Build backend and source discovery are configured.
- [ ] Runtime versions are declared and tested.
- [ ] Distribution and import names are accepted.
- [ ] Dependencies and licenses are approved.
- [ ] Versioning and publishing policy is documented.

### Implementation

- [ ] Public exports are intentional and minimal.
- [ ] Operations require explicit profiles where applicable.
- [ ] Imports are side-effect free.
- [ ] Network and registry access are absent from the core.
- [ ] Hashing is delegated without representation collapse.
- [ ] Domain identity is not centralized improperly.
- [ ] Credentials and sensitive inference are denied.

### Evidence

- [ ] Package fixtures exist.
- [ ] Unit and negative tests pass.
- [ ] Compatibility vectors pass.
- [ ] Privacy and resource-limit tests pass.
- [ ] Build, install, and import tests pass.
- [ ] Dedicated CI behavior has been inspected.
- [ ] Confirmed consumers use the accepted API.

### Change and rollback

- [ ] Consumer inventory is maintained.
- [ ] Migration and deprecation plans exist.
- [ ] Correction paths are documented.
- [ ] Prior accepted artifact is retained.
- [ ] Software rollback is tested.
- [ ] Documentation reflects actual behavior.

[Back to top](#top)

---

<a id="verification-register"></a>

## Verification register

| # | Verification item | Status |
|---:|---|---|
| 1 | Package owner and identity steward | NEEDS VERIFICATION |
| 2 | Privacy, security, dependency, migration stewards | NEEDS VERIFICATION |
| 3 | CODEOWNERS coverage | NEEDS VERIFICATION |
| 4 | Package implementation ownership | NEEDS VERIFICATION |
| 5 | Distribution name `kfm-identity` | NEEDS VERIFICATION |
| 6 | Import namespace `identity` | NEEDS VERIFICATION |
| 7 | Build backend and source discovery | UNKNOWN |
| 8 | Supported Python range | UNKNOWN |
| 9 | Dependency set, locks, licenses, SBOM | NEEDS VERIFICATION |
| 10 | Publishing target and authorization | NOT AUTHORIZED |
| 11 | Package version policy | NEEDS VERIFICATION |
| 12 | Accepted public API | UNKNOWN |
| 13 | Profile registry and common grammar | UNKNOWN |
| 14 | Normalization and case rules | UNKNOWN |
| 15 | Reserved namespace authority | UNKNOWN |
| 16 | `identity_token` terminology and kind governance | NEEDS VERIFICATION |
| 17 | Object versus token-instance identity | NEEDS VERIFICATION |
| 18 | Common/domain boundary | NEEDS VERIFICATION |
| 19 | ADR-0013 and `run_id` vocabulary | NEEDS VERIFICATION |
| 20 | Hashing API and representation | NEEDS VERIFICATION |
| 21 | Collision-scope contract | UNKNOWN |
| 22 | Registry/resolver ownership | NEEDS VERIFICATION |
| 23 | Lineage and reference profile contracts | NEEDS VERIFICATION |
| 24 | Actor-reference privacy rules | NEEDS VERIFICATION |
| 25 | Living-person, genomic, kinship, location denial tests | NEEDS VERIFICATION |
| 26 | Resource limits and diagnostic redaction | UNKNOWN |
| 27 | Package fixtures and tests | NOT FOUND |
| 28 | Golden and cross-language vectors | NOT FOUND / UNKNOWN |
| 29 | Dedicated identity workflow | NOT FOUND |
| 30 | Build/install/import tests | NOT FOUND |
| 31 | Dependency scan for package artifact | NEEDS VERIFICATION |
| 32 | Confirmed consumers and inventory | UNKNOWN / NOT FOUND |
| 33 | Package/tool/validator parity | UNKNOWN |
| 34 | Migration tooling and compatibility window | NEEDS VERIFICATION |
| 35 | Deprecation and correction policy | NEEDS VERIFICATION |
| 36 | Software rollback artifact and drill | NEEDS VERIFICATION |
| 37 | Runtime/deployment use | UNKNOWN |
| 38 | Operational health | UNKNOWN |

[Back to top](#top)

---

<a id="rollback-correction-and-package-release"></a>

## Rollback, correction, and package release

For this README-only change, revert the documentation commit or restore prior blob `ba5f4c0b3e425448906acc6e5e393eefce60ab8b`. Documentation rollback does not change runtime behavior.

A future software rollback must identify the bad and prior package versions/artifact digests, affected consumers, API/profile and dependency differences, generated identifiers that need correction or supersession, installation/deployment steps, and post-rollback validation evidence.

Never fix already-issued identifiers by overwriting history. Use explicit correction, alias, supersession, tombstone, withdrawal, migration relation, or rollback reference in the owning governed system. The package may eventually construct a typed relation candidate; it does not persist or approve it.

A future package release record should include version, source commit, artifact digests, build environment, dependencies/SBOM, tests and compatibility vectors, supported runtimes, API/profile versions, migration notes, limitations, and rollback target. It must not be confused with a KFM data or claim `ReleaseManifest`.

Rollback or hold a package release if it introduces profile guessing, silent normalization, unreceipted identity change, token/string collapse, centralized domain sameness, duplicate hashing semantics, credential or identity-provider behavior, sensitive exposure, registry mutation, network/import side effects, unplanned consumer breakage, or no executable rollback.

[Back to top](#top)

---

## Evidence boundary

This README is grounded in the commit-pinned repository evidence in `KFM_META_BLOCK_V2`.

It does not claim implemented APIs, accepted profiles, installability, package publication, complete consumers, runtime behavior, CI enforcement, deployment state, or operational health. Those remain **UNKNOWN** or **NEEDS VERIFICATION** until proved through current metadata, code, fixtures, tests, workflows, built artifacts, consumer evidence, and runtime observations.

[Back to top](#top)
