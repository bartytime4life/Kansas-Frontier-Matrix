<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-evidence-readme
title: packages/evidence/ — Evidence-Specific Shared Helper Package Boundary
type: readme
version: v0.2
status: draft; repository-grounded; documentation-only-package-placeholder; purpose-conflicted; non-authoritative
owners:
  - OWNER_TBD — Evidence package owner
  - OWNER_TBD — Evidence and proof steward
  - OWNER_TBD — Identity, hashing, and citation package stewards
  - OWNER_TBD — Evidence resolver package steward
  - OWNER_TBD — Contract, schema, and validator steward
  - OWNER_TBD — Policy, rights, sensitivity, release, security, and docs stewards
created: NEEDS VERIFICATION — target file existed before this revision
updated: 2026-07-15
supersedes: v1 planning-oriented package guide (2026-06-14)
policy_label: public; packages; evidence; package-boundary; EvidenceRef; EvidenceBundle; adapters; cite-or-abstain; no-network-by-default; fail-closed; non-authoritative
path: packages/evidence/README.md
truth_posture: CONFIRMED target and prior blob, packages responsibility root, documentation-only package surface at exact checked paths, absence of pyproject.toml/package.json/src README/import initializer/package test README/package fixture README/dedicated evidence.yml at exact checked paths, sibling evidence-resolver/identity/hashing/citation package READMEs, fielded closed EvidenceRef and EvidenceBundle schemas, current SpecHash schema, missing schema-declared EvidenceRef validator, Directory Rules v1.4, and current resolver package v0.2 / PROPOSED evidence-specific composition adapters, schema-generated carriers, profile-pinned constructors, public-safe synthetic builders, and cross-package integration helpers only after an accepted package-boundary decision / CONFLICTED current v1 scope versus existing identity, hashing, citation, and evidence-resolver package responsibilities; architecture hash notation versus current SpecHash shape; URI/identity/scope ambitions versus permissive current EvidenceRef and free-form claim_scope schemas; package-specific versus contract-schema test and fixture placement / UNKNOWN accepted package purpose, language, build metadata, source layout, exports, dependencies, consumers, validator integration, dedicated CI, package publication, runtime/API wiring, and production behavior / NEEDS VERIFICATION owners, ADR/package-boundary decision, canonical object profiles, canonicalization profile, citation ownership, resolver handoff, correction invalidation, release integration, and rollback integration
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: ac419b0942eb8c229b666aed147cd71dc7e9c42b
  prior_blob: a74e29bf907ded21098adce3ae8bf22f0f66d512
  sibling_resolver_blob: 9c616c83091977709a50c5cf02d8fbe37bfd4329
  sibling_identity_blob: ba5f4c0b3e425448906acc6e5e393eefce60ab8b
  sibling_hashing_blob: c9440697c02f71a8c83f0293d72364bb89930c01
  sibling_citation_blob: 8516033ca7b7f7458cfc0f09438853bd3ac3753e
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  evidence_ref_schema_blob: 42f499df613a9d68e5ca6fc5ec75ff8058c155b9
  evidence_bundle_schema_blob: cf5256831b63dca46a5f68b168441adcf68b8751
  spec_hash_schema_blob: 80b496b01b8de8c0e8ba67bf020977e6b1f3c652
related:
  - ../README.md
  - ../evidence-resolver/README.md
  - ../identity/README.md
  - ../hashing/README.md
  - ../citation/README.md
  - ../../contracts/evidence/evidence_ref.md
  - ../../contracts/evidence/evidence_bundle.md
  - ../../contracts/common/spec_hash.md
  - ../../schemas/contracts/v1/evidence/evidence_ref.schema.json
  - ../../schemas/contracts/v1/evidence/evidence_bundle.schema.json
  - ../../schemas/contracts/v1/common/spec_hash.schema.json
  - ../../fixtures/contracts/v1/evidence/evidence_ref/README.md
  - ../../fixtures/contracts/v1/evidence/evidence_bundle/README.md
  - ../../tools/validators/validate_evidence_bundle.py
  - ../../tests/schemas/test_common_contracts.py
  - ../../docs/architecture/evidence-identity.md
  - ../../docs/doctrine/directory-rules.md
tags: [kfm, packages, evidence, package-boundary, EvidenceRef, EvidenceBundle, identity, hashing, citation, resolver, schema-adapter, deterministic, no-network, fail-closed, cite-or-abstain, rollback]
notes:
  - "v0.2 replaces stale planning language with a commit-pinned description of a documentation-only package placeholder."
  - "No language, distribution, source namespace, supported export, consumer, or executable package behavior is established by the checked repository surface."
  - "The current v1 responsibility list overlaps packages/identity, packages/hashing, packages/citation, and packages/evidence-resolver; v0.2 records the overlap and requires an accepted package-boundary decision before implementation."
  - "If retained, this package should own only evidence-specific composition/adaptation that is not already owned by those sibling packages."
  - "Only this Markdown file changes."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Evidence-Specific Shared Helper Package Boundary

`packages/evidence/`

> Package-level boundary for reusable **evidence-specific composition and adapter helpers** that may eventually connect accepted EvidenceRef, EvidenceBundle, citation, identity, hashing, and resolver profiles. The current repository surface is a **documentation-only placeholder**, not an implemented package: no package metadata, source tree, import namespace, tests, fixtures, exports, consumers, or dedicated CI behavior were established at the exact checked paths.

![status](https://img.shields.io/badge/status-draft-blue)
![version](https://img.shields.io/badge/version-v0.2-informational)
![implementation](https://img.shields.io/badge/implementation-documentation--only-lightgrey)
![purpose](https://img.shields.io/badge/purpose-NEEDS%20DECISION-orange)
![authority](https://img.shields.io/badge/authority-helper%20only-455a64)
![network](https://img.shields.io/badge/network-none%20by%20default-455a64)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-0b7285)

**Quick links:** [Purpose](#purpose-and-audience) · [Status](#current-repository-state) · [Decision](#package-purpose-decision) · [Context](#package-bounded-context) · [Placement](#placement-and-authority) · [Surface](#current-package-surface) · [Overlap](#sibling-package-overlap-and-anti-collapse) · [Responsibilities](#proposed-owned-responsibilities) · [Exclusions](#explicit-non-ownership) · [Profiles](#contract-and-schema-profile-basis) · [EvidenceRef](#evidenceref-boundary) · [EvidenceBundle](#evidencebundle-boundary) · [Identity](#identity-and-hashing-boundary) · [Citation](#citation-boundary) · [Resolver](#resolver-boundary) · [Inputs](#accepted-inputs) · [Outputs](#permitted-outputs) · [Dependencies](#dependency-direction) · [Language](#language-packaging-and-export-boundary) · [Generated code](#generated-types-and-adapters) · [Trust](#lifecycle-policy-release-and-public-safety) · [Failures](#failure-and-error-semantics) · [Security](#security-privacy-and-data-minimization) · [Tests](#tests-fixtures-validators-and-ci) · [Admission](#implementation-admission-sequence) · [Compatibility](#compatibility-correction-and-rollback) · [Validation](#validation-commands) · [Done](#definition-of-done) · [Backlog](#open-verification-register) · [Ledger](#evidence-ledger)

> [!IMPORTANT]
> **Repository snapshot:** `main@ac419b0942eb8c229b666aed147cd71dc7e9c42b`<br>
> **Target blob before this revision:** `a74e29bf907ded21098adce3ae8bf22f0f66d512`<br>
> **Verified package surface:** this README only at the exact checked package paths<br>
> **Package metadata:** not found at `packages/evidence/pyproject.toml` or `packages/evidence/package.json`<br>
> **Source layout:** not found at `packages/evidence/src/README.md` or `packages/evidence/src/evidence/__init__.py`<br>
> **Package tests/fixtures:** not found at the exact checked README paths<br>
> **Dedicated workflow:** not found at `.github/workflows/evidence.yml`<br>
> **Implementation status:** no supported package API, language, build, export, consumer, or runtime behavior is established

> [!CAUTION]
> The existence of a package directory does not prove that the package is needed. The prior README assigns identity, hashing, citation, and resolver-adjacent duties that overlap existing sibling package boundaries. Do not add implementation until the package purpose is accepted and non-overlapping.

---

## Purpose and audience

This README governs the repository boundary represented by `packages/evidence/`.

Its immediate purpose is not to promise an implementation. It is to:

- record what the current repository actually proves;
- stop the directory from becoming a general evidence dumping ground;
- separate evidence-specific composition from identity, hashing, citation, resolution, proof storage, policy, and release authority;
- define the decision required before source code is admitted;
- keep any eventual implementation deterministic, explicit, no-network by default, policy-subordinate, and reversible;
- preserve cite-or-abstain behavior without treating helper output as evidence closure;
- provide an auditable validation and rollback posture.

This README is for:

- package and evidence stewards;
- contract and schema stewards;
- identity, hashing, citation, and resolver package maintainers;
- proof, catalog, policy, rights, sensitivity, release, and correction stewards;
- application, pipeline, validator, and governed API maintainers;
- security, privacy, dependency, and packaging reviewers;
- reviewers deciding whether this package should exist, remain documentation-only, be consolidated, or receive a narrowly bounded implementation.

[Back to top](#top)

---

## Current repository state

### Evidence snapshot

| Field | Value |
|---|---|
| Repository | `bartytime4life/Kansas-Frontier-Matrix` |
| Repository ID | `1059091169` |
| Visibility | public |
| Base ref | `main` |
| Base commit | `ac419b0942eb8c229b666aed147cd71dc7e9c42b` |
| Prior target blob | `a74e29bf907ded21098adce3ae8bf22f0f66d512` |
| Evidence resolver README blob | `9c616c83091977709a50c5cf02d8fbe37bfd4329` |
| Identity README blob | `ba5f4c0b3e425448906acc6e5e393eefce60ab8b` |
| Hashing README blob | `c9440697c02f71a8c83f0293d72364bb89930c01` |
| Citation README blob | `8516033ca7b7f7458cfc0f09438853bd3ac3753e` |
| Directory Rules blob | `2affb080e6f0043867c64c7f06c1ca52030fbd55` |
| Current revision | documentation-only package-boundary v0.2 proposal |

### Exact checked package paths

| Path | Result | Consequence |
|---|---:|---|
| `packages/evidence/README.md` | **CONFIRMED** | The package directory has a planning-oriented README. |
| `packages/evidence/pyproject.toml` | **NOT FOUND at exact path** | No Python distribution identity or build metadata is established. |
| `packages/evidence/package.json` | **NOT FOUND at exact path** | No JavaScript/TypeScript package identity is established. |
| `packages/evidence/src/README.md` | **NOT FOUND at exact path** | No verified source-root contract exists. |
| `packages/evidence/src/evidence/__init__.py` | **NOT FOUND at exact path** | No verified Python import package exists. |
| `tests/packages/evidence/README.md` | **NOT FOUND at exact path** | No package-specific test lane is documented there. |
| `fixtures/packages/evidence/README.md` | **NOT FOUND at exact path** | No package-specific fixture lane is documented there. |
| `.github/workflows/evidence.yml` | **NOT FOUND at exact path** | No dedicated workflow is established by that conventional path. |

These are bounded findings. They do not prove that no related implementation exists anywhere else in the repository. They do prove that the package README must not claim a known distribution, language, source namespace, export surface, test suite, workflow, or production consumer from the exact checked package surface.

### Confirmed neighboring authority surfaces

| Surface | Status | Relevance |
|---|---:|---|
| `packages/evidence-resolver/README.md` v0.2 | **CONFIRMED** | Defines the proposed EvidenceRef-to-EvidenceBundle resolver helper boundary and records unresolved profile conflicts. |
| `packages/identity/README.md` | **CONFIRMED README** | Claims ID grammar, stable IDs, namespaces, and identity-carrier helpers. |
| `packages/hashing/README.md` | **CONFIRMED README** | Claims canonicalization, digest, hash comparison, and replay helper responsibilities. |
| `packages/citation/README.md` | **CONFIRMED README** | Claims citation validation, source/ref display, limitation, and citation-carrier helpers. |
| EvidenceRef schema | **CONFIRMED / `PROPOSED` status** | Closed object with `ref`, `kind`, and optional `bundle_ref`. |
| EvidenceBundle schema | **CONFIRMED / `PROPOSED` status** | Closed claim-scope closure object with required refs, source records, citations, rights, sensitivity, transforms, checksums, and spec hash. |
| SpecHash schema | **CONFIRMED / `PROPOSED` status** | Closed object containing `value: sha256:<64 lowercase hex>`. |
| EvidenceRef dedicated validator | **NOT FOUND at schema-declared path** | Schema metadata and file state conflict. |
| EvidenceBundle validator | **CONFIRMED file** | Validates the contract schema/fixture lane; does not prove package behavior. |
| Generic contract-schema harness | **CONFIRMED test code** | Covers schema fixture families; does not replace package-level behavior tests. |

[Back to top](#top)

---

## Package purpose decision

### Current decision status

The durable purpose of `packages/evidence/` is **NEEDS VERIFICATION / NEEDS DECISION**.

The prior README describes a package that may own:

- EvidenceRef value helpers;
- EvidenceBundle reference helpers;
- deterministic identity helpers;
- canonicalization and digest helpers;
- citation carriers;
- resolver-adjacent adapters;
- fixtures.

Current sibling package documentation already assigns those families across:

- `packages/identity/`;
- `packages/hashing/`;
- `packages/citation/`;
- `packages/evidence-resolver/`.

Therefore, “evidence helpers” is too broad to act as an implementation contract.

### Acceptable decisions

A stewarded decision should select one of these outcomes:

| Decision | Meaning | Required follow-through |
|---|---|---|
| Keep documentation-only | Retain this README as a package-boundary warning; add no source. | Periodically recheck overlap and references. |
| Retain a narrow package | Own only evidence-specific composition/adaptation not already owned by sibling packages. | Define contract, package metadata, imports, tests, dependencies, consumers, and rollback. |
| Consolidate into a sibling | Move intended helpers to identity, hashing, citation, or resolver ownership. | ADR/migration note, import plan, compatibility window, docs and tests. |
| Remove the package directory | Delete the placeholder after references are migrated. | Reviewable deletion, link updates, historical note, rollback target. |
| Establish a broader shared kernel | Make this a deliberate evidence shared-kernel package. | ADR-class decision defining what moves out of sibling packages and why. |

### Decision rule

Do not implement by topic name.

Implement only when the responsibility can be stated without using “and” to join unrelated authority families.

A sufficiently narrow statement might be:

> Evidence-specific, schema-profile-pinned composition adapters that combine already-owned identity, hash, citation, and resolver primitives into candidate EvidenceRef or EvidenceBundle carrier objects without computing identity, validating citations, resolving bundles, deciding policy, storing proof, or approving release.

That statement is **PROPOSED**, not accepted.

[Back to top](#top)

---

## Package bounded context

### Core concept

If retained, this package should be an **evidence-specific composition boundary**, not an evidence authority.

It may compose or adapt values that are already governed elsewhere. It must not decide that those values are correct, admissible, complete, released, or true.

### Ubiquitous language

| Term | Meaning here | Not equivalent to |
|---|---|---|
| Evidence candidate | An in-memory or serialized candidate assembled for validation. | Evidence closure or published proof. |
| EvidenceRef carrier | A profile-bound carrier for `ref`, `kind`, and optional `bundle_ref`. | Verified bundle membership. |
| EvidenceBundle candidate | A candidate object shaped for the current schema. | Stored, validated, reviewed, policy-cleared, released EvidenceBundle. |
| Adapter | Explicit conversion between accepted versioned profiles. | Silent normalization or best-effort guessing. |
| Constructor | Deterministic assembly from explicit inputs. | Source lookup, registry query, policy decision, or release action. |
| Projection | Reduced safe representation prepared for a downstream owner. | Authorization to expose the projection. |
| Profile | Named contract/schema/version/canonicalization set. | Unversioned convention inferred from prose. |
| Helper result | Typed success or failure from local deterministic logic. | Runtime `ANSWER`, policy allow, or release approval. |
| Synthetic fixture | Public-safe test-only input. | Production evidence, a source record, or proof. |

### Aggregate boundary

This package must not define a new sovereign aggregate.

`EvidenceRef` and `EvidenceBundle` meanings stay in contracts. Their shapes stay in schemas. Stored instances stay in governed data/proof roots. Resolution stays with the resolver boundary. Policy and release stay separate.

[Back to top](#top)

---

## Placement and authority

Directory Rules define `packages/` as shared implementation, while contracts define meaning, schemas define shape, policy defines admissibility, release defines publication decisions, and data roots preserve lifecycle and proof state.

The existing path is structurally valid for a shared package **only if** a distinct package responsibility is accepted.

| Concern | Authority home | Authority in this package |
|---|---|---|
| EvidenceRef meaning | `contracts/evidence/evidence_ref.md` | None |
| EvidenceRef shape | `schemas/contracts/v1/evidence/evidence_ref.schema.json` | None |
| EvidenceBundle meaning | `contracts/evidence/evidence_bundle.md` | None |
| EvidenceBundle shape | `schemas/contracts/v1/evidence/evidence_bundle.schema.json` | None |
| SpecHash meaning and shape | common contract/schema surfaces | None |
| ID grammar and stable identity | accepted identity package/contract surfaces | None unless delegated adapter only |
| Canonicalization and digest computation | accepted hashing package/standard | None unless consuming a hash result |
| Citation validation and rendering helpers | accepted citation package/contract surfaces | None unless composing a citation field |
| Ref-to-bundle resolution | `packages/evidence-resolver/` and governed registry/proof systems | None |
| Source admission and source role | source registry and source contracts | None |
| Rights and sensitivity decisions | policy and review surfaces | None |
| Evidence/proof instances | governed data/proof roots | None |
| Receipts | governed receipt roots | None |
| Release/correction/rollback | `release/` and accepted governance records | None |
| Public API response | governed API/runtime envelope surfaces | None |
| Local evidence-specific composition | This package, if accepted | Supporting implementation only |

> [!WARNING]
> Package placement does not move authority. Importing a schema type, generating a dataclass, composing a candidate, or validating local shape does not make this package the evidence, policy, resolver, proof, or release authority.

[Back to top](#top)

---

## Current package surface

### Verified tree

```text
packages/evidence/
└── README.md
```

This is the only package-local file established by the exact checks used for this revision.

### Not established

The following are not established:

- package language;
- distribution name;
- version;
- build backend;
- runtime requirement;
- dependency list;
- source layout;
- import namespace;
- public exports;
- generated code directory;
- package-specific tests;
- package-specific fixtures;
- package-specific CI;
- production consumers;
- release artifact;
- package registry publication;
- runtime/API integration.

### No inferred tree

A proposed future tree appears later in this README, but it is not current repository fact.

[Back to top](#top)

---

## Sibling package overlap and anti-collapse

### Responsibility matrix

| Capability | Current neighboring claimant | Default owner posture |
|---|---|---|
| ID grammar, stable object IDs, namespace parsing | `packages/identity/` README | Identity package |
| Canonicalization, SHA-256, spec/content/geometry/artifact hashes | `packages/hashing/` README | Hashing package |
| Citation shape, display refs, anchors, limitations | `packages/citation/` README | Citation package |
| EvidenceRef-to-EvidenceBundle resolution candidates | `packages/evidence-resolver/` v0.2 | Resolver package |
| Evidence-specific composition across those primitives | No accepted implementation found | Possible narrow role here |
| Contract meaning | `contracts/` | Never a package |
| Machine shape | `schemas/` | Never a package |
| Policy/admissibility | `policy/` | Never a package |
| Proof storage | governed data/proof roots | Never a package |
| Release decision | `release/` | Never a package |

### Disallowed collapses

```text
evidence topic -> all evidence-related code
EvidenceRef carrier -> identity package replacement
EvidenceBundle constructor -> proof closure
hash field -> hashing implementation
citation string -> citation validation
bundle_ref -> resolver result
schema-valid object -> admissible evidence
admissible evidence -> released evidence
released evidence -> public exposure permission
package helper -> governed API
fixture -> proof
generated class -> semantic contract
```

### Import-direction principle

If this package is retained, it should depend on accepted lower-level primitives rather than duplicate them.

Illustrative direction:

```text
identity / hashing / citation primitives
                |
                v
       packages/evidence
 evidence-specific composition
                |
                v
      evidence-resolver / validators
                |
                v
 governed runtime / API / release paths
```

The exact direction is **PROPOSED** and must be verified against accepted package boundaries and cycle analysis.

[Back to top](#top)

---

## Proposed owned responsibilities

These responsibilities are **PROPOSED** and should be admitted only after the package-purpose decision.

### Candidate responsibility set

This package may own:

1. EvidenceRef candidate constructors bound to an explicit schema profile.
2. EvidenceBundle candidate constructors bound to an explicit schema profile.
3. Evidence-specific adapters that combine already-computed IDs, hashes, citations, source record refs, rights summaries, sensitivity labels, transform refs, and spec hashes.
4. Evidence-specific normalization that is explicitly defined by a contract/schema profile and does not duplicate general canonicalization.
5. Evidence-specific typed issue carriers for missing required fields or unsupported profile combinations.
6. Evidence-specific safe projection helpers that remove no field unless the projection contract says so.
7. Generated model wrappers pinned to the authoritative schema digest and generator version.
8. Synthetic public-safe fixture builders for package behavior tests.
9. Compatibility adapters between explicitly named evidence contract versions.
10. Boundary assertions that reject resolver, policy, proof-storage, receipt-storage, release, network, or UI responsibilities.

### Admission test

A proposed helper belongs here only when all answers are yes:

- Is the behavior specific to EvidenceRef/EvidenceBundle composition?
- Is meaning already defined in a contract?
- Is shape already defined in a schema?
- Are identity/hash/citation operations delegated to accepted owners?
- Does it avoid source lookup and bundle resolution?
- Does it avoid policy and release decisions?
- Does it avoid persistence?
- Is the result a candidate, adapter result, or local validation issue?
- Can behavior be deterministic and no-network?
- Can tests use synthetic public-safe inputs?
- Is rollback possible without rewriting authority roots?

[Back to top](#top)

---

## Explicit non-ownership

This package must not own or become:

| Excluded responsibility | Correct authority or implementation family |
|---|---|
| Evidence semantic definitions | `contracts/evidence/` |
| Evidence machine schemas | `schemas/contracts/v1/evidence/` |
| General ID grammar or stable identity algorithms | accepted identity package/contract |
| General canonicalization or digest computation | accepted hashing package/standard |
| General citation validation/rendering | accepted citation package/contract |
| EvidenceRef-to-bundle lookup or resolution authority | evidence resolver plus governed registry/proof systems |
| Source connectors or source admission | `connectors/` and source registry contracts |
| SourceDescriptor registry | governed registry data roots |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | lifecycle-visible data roots |
| EvidenceBundle materialization or proof packs | governed proof/data roots |
| Rights, sensitivity, sovereignty, or admissibility decisions | policy and steward review |
| Validation receipt storage | receipt roots |
| ReleaseManifest, correction notice, rollback card, promotion decision | release/governance roots |
| Runtime orchestration | runtime/apps |
| Public API routes or public serializers | governed API app and accepted schemas |
| UI, Evidence Drawer, Focus Mode, map, or export rendering | downstream app/UI packages |
| AI-generated claims, citations, or summaries as evidence | governed AI path plus evidence validation |
| Secrets, credentials, private raw records, chain-of-thought | nowhere in package source or fixtures |

[Back to top](#top)

---

## Contract and schema profile basis

Any implementation must bind to explicit accepted profiles.

### Current schema facts

The current EvidenceRef schema is a closed object with:

| Field | Required | Current constraint |
|---|---:|---|
| `ref` | Yes | string; no URI pattern is enforced |
| `kind` | Yes | `measurement`, `record`, `dataset`, or `artifact` |
| `bundle_ref` | No | string; no membership verification is enforced |

The current EvidenceBundle schema is a closed object requiring:

- `bundle_id`;
- `claim_scope`;
- `evidence_refs`;
- `source_records`;
- `citations`;
- `rights`;
- `sensitivity`;
- `transforms`;
- `checksums`;
- `spec_hash`.

The current SpecHash schema is a closed object:

```json
{
  "value": "sha256:<64 lowercase hexadecimal characters>"
}
```

### Profile rules

1. Constructors must declare the schema/contract profile they target.
2. Package code must not add undeclared fields to closed schemas.
3. Package code must not silently drop fields to force validation.
4. Package code must not treat a valid string as a verified URI, registry key, citation, or bundle membership unless another accepted contract says so.
5. Package code must not treat `bundle_ref` as closure.
6. Package code must not interpret `claim_scope` more structurally than its accepted contract/profile allows.
7. Package code must not assume `jcs:sha256:` and `{ "value": "sha256:..." }` are equivalent.
8. Generated types must carry source schema identity and generation provenance.
9. Cross-version adapters must be explicit, one-directional where necessary, and tested for information loss.
10. Unknown profile combinations must fail visibly.

[Back to top](#top)

---

## EvidenceRef boundary

### Current EvidenceRef machine profile

```json
{
  "ref": "obs:1",
  "kind": "measurement",
  "bundle_ref": "optional-bundle-id"
}
```

Only `ref` and `kind` are required.

### Helper posture

A package helper may eventually:

- require an explicit profile;
- preserve the original `ref`;
- validate the current `kind` enum;
- carry optional `bundle_ref`;
- return typed local issues;
- prepare a candidate object for schema validation;
- preserve unknown external context outside the closed candidate rather than injecting it into the object.

A helper must not:

- claim that `ref` is canonical merely because it is a string;
- infer evidence kind from prose;
- create a `bundle_ref` from object proximity;
- resolve `bundle_ref`;
- treat a ref as citation completeness;
- infer rights or sensitivity;
- declare release eligibility;
- upgrade a ref into EvidenceBundle closure.

### URI and identity conflict

The prior README proposes URI validation and `kfm://evidence/...` forms. The current schema does not enforce a URI pattern. URI grammar belongs to an accepted identity/contract profile, not to an inferred package convention.

[Back to top](#top)

---

## EvidenceBundle boundary

### Current EvidenceBundle machine profile

A current-profile candidate must provide all required schema fields.

```text
bundle_id
claim_scope
evidence_refs[]
source_records[]
citations[]
rights.license
sensitivity
transforms[]
checksums{...}
spec_hash.value
```

### Constructor posture

A package constructor may eventually:

- require every schema-required field;
- accept evidence refs and other values as explicit inputs;
- preserve order where semantically relevant;
- reject empty required arrays;
- preserve rights and sensitivity inputs;
- validate checksum string shape through accepted hashing/schema helpers;
- preserve transform refs without executing transforms;
- return a candidate plus local issues.

A constructor must not:

- fetch source records;
- resolve citations;
- compute source authority;
- decide that rights are sufficient;
- decide that sensitivity is safe;
- execute transformations;
- create proof storage;
- sign or attest the bundle;
- decide that the bundle closes a claim;
- approve release;
- produce public answer text.

### Closure rule

An EvidenceBundle-shaped object is not automatically an EvidenceBundle with governed closure.

Closure additionally depends on materialized records, resolver integrity, validation, policy, review, release, correction, and rollback posture as required by significance.

[Back to top](#top)

---

## Identity and hashing boundary

### Delegation

General identity belongs with the accepted identity package and contracts.

General canonicalization and digest computation belong with the accepted hashing package and standards.

This package may consume:

- a validated object ID;
- a validated ref string;
- a computed digest;
- a SpecHash object;
- a named canonicalization profile;
- a comparison result.

It must not silently reimplement those algorithms.

### Current conflict

Architecture and sibling hashing prose use `jcs:sha256:<hex>` language. The current SpecHash schema accepts:

```json
{
  "value": "sha256:<hex>"
}
```

The schema does not carry canonicalization identity.

Therefore:

- a schema-valid SpecHash does not prove JCS use;
- two equal SpecHash values are comparable only when the same input/profile is known;
- this package must not add a `jcs:` prefix or remove one silently;
- canonicalization metadata must be carried by an accepted surrounding contract or a versioned profile;
- migration requires explicit compatibility logic and receipts where trust-bearing records are affected.

[Back to top](#top)

---

## Citation boundary

The current EvidenceBundle schema carries `citations` as non-empty strings. It does not itself define a structured citation object.

The citation package README claims citation validation, anchors, limitations, display helpers, and safe citation rendering.

This package may eventually:

- accept citation strings or accepted citation objects from the citation owner;
- preserve them in an EvidenceBundle candidate;
- require non-empty citation input for the current bundle profile;
- return a missing-citation issue.

This package must not:

- parse every citation format as an implicit authority;
- invent citation text;
- validate source support unless delegated to the citation validator;
- turn a source URL into an EvidenceBundle;
- infer a citation from a filename;
- redact citation context without an explicit projection policy;
- expose restricted source details to public clients.

[Back to top](#top)

---

## Resolver boundary

The evidence resolver package owns the proposed pointer-to-closure candidate evaluation boundary.

This package may prepare:

- EvidenceRef candidates;
- EvidenceBundle candidates;
- typed composition issues;
- an explicit profile identifier;
- inputs suitable for a resolver call.

It must not:

- query a bundle registry;
- walk supersession chains;
- determine current head;
- resolve refs;
- emit `RESOLVED`, `UNRESOLVED`, `DENIED`, or resolver `ERROR` as if resolution occurred;
- map results to public runtime outcomes;
- decide policy;
- decide release;
- bypass the governed API.

### Handoff rule

```text
packages/evidence
  -> candidate object + profile + local issues
  -> schema validation
  -> governed registry/proof lookup
  -> evidence resolver
  -> policy/review/release
  -> runtime envelope
  -> governed API
```

Any shortcut from package constructor to public answer breaks the trust membrane.

[Back to top](#top)

---

## Accepted inputs

Inputs must be explicit, inspectable, versioned where material, and supplied by governed callers.

| Input family | Examples | Required handling |
|---|---|---|
| Profile | contract version, schema ID, schema digest, adapter version | Required for profile-sensitive behavior. |
| EvidenceRef values | `ref`, `kind`, optional `bundle_ref` | Preserve exactly; validate only accepted constraints. |
| EvidenceBundle values | required current schema fields | Require completeness; do not fetch missing data. |
| Identity values | object IDs, refs, namespace tokens | Consume from accepted identity owner; do not invent authority. |
| Hash values | checksums, SpecHash, hash comparison result | Consume from accepted hashing owner/profile. |
| Citation values | citation strings or accepted citation carriers | Preserve; delegate citation validation. |
| Source record refs | explicit record handles | Preserve; do not fetch or admit sources. |
| Rights | explicit license summary and refs | Preserve; do not decide sufficiency. |
| Sensitivity | accepted sensitivity label/value | Preserve; do not downgrade. |
| Transform refs | explicit ordered transform identifiers | Preserve; do not execute transforms. |
| Correction context | prior ID, superseding ID, invalidation refs | Preserve; do not mutate history. |
| Fixture context | synthetic public-safe values | Mark test-only; reject secrets and real sensitive records. |

### Prohibited ambient inputs

Helpers must not depend on:

- current working directory contents;
- implicit network access;
- environment credentials;
- UI state;
- hidden global registry clients;
- operator memory;
- generated prose;
- current time unless explicitly passed and contractually required;
- random values unless seeded and recorded;
- unpinned schema downloads.

[Back to top](#top)

---

## Permitted outputs

Permitted outputs are bounded implementation results.

### Candidate output families

- current-profile EvidenceRef candidate;
- current-profile EvidenceBundle candidate;
- evidence-specific projection candidate;
- typed local issue list;
- compatibility adapter result;
- generated-model wrapper;
- fixture object;
- deterministic serialization input;
- package version/profile metadata.

### Output requirements

Every material result should make these visible where applicable:

- profile/version;
- source schema ID or digest;
- adapter/generator version;
- original inputs or input refs;
- lossiness status;
- local validation status;
- issue codes;
- whether network/persistence occurred;
- whether the result is synthetic;
- whether downstream resolver, policy, review, and release are still required.

### Forbidden outputs

The package must not emit:

- proof closure;
- policy allow/deny as authority;
- release approval;
- public `ANSWER`;
- source admission;
- registry mutation;
- receipt persistence;
- proof persistence;
- generated factual claims;
- fabricated citations;
- hidden uncertainty;
- unrestricted sensitive payloads.

[Back to top](#top)

---

## Dependency direction

### Allowed conceptual dependencies

A retained package may depend on accepted interfaces from:

- identity helpers;
- hashing helpers;
- citation helpers;
- generated schema models;
- common error/result primitives.

It may be consumed by:

- validators;
- evidence resolver adapters;
- pipelines assembling evidence candidates;
- governed API internals;
- tests and fixtures;
- proof/release preparation tools.

### Forbidden dependency direction

The package must not require:

- public UI packages;
- governed API route modules;
- runtime service containers;
- source connectors;
- lifecycle stores;
- policy engines;
- release databases;
- model providers;
- secret managers at import time.

### Cycle prevention

Potential cycle:

```text
evidence -> citation -> evidence
```

or:

```text
evidence -> resolver -> evidence
```

must be prevented through:

- lower-level neutral contracts/models;
- protocol interfaces;
- dependency inversion;
- generated schema types;
- ADR-backed package consolidation;
- explicit adapter packages if needed.

Do not solve cycles with runtime import hacks or duplicated model definitions.

[Back to top](#top)

---

## Language packaging and export boundary

No package language or distribution is currently established at the exact checked package paths.

### Before selecting a language

Verify:

- actual consumers;
- dominant repository conventions;
- whether generated models already exist;
- whether the package should be language-neutral documentation only;
- whether functionality belongs in existing packages;
- build-system support;
- test and release support;
- security/dependency implications;
- long-term compatibility needs.

### If Python is selected

A future Python package would require, at minimum:

- accepted distribution name;
- `pyproject.toml`;
- build backend;
- Python version range;
- dependency declarations;
- explicit source discovery;
- import namespace;
- deliberate `__init__.py` exports;
- typed marker decision;
- wheel/editable-install tests;
- versioning and changelog posture.

### If TypeScript/JavaScript is selected

A future package would require, at minimum:

- accepted package name;
- `package.json`;
- runtime and package-manager policy;
- module format;
- build outputs;
- type declarations;
- export map;
- test setup;
- publication posture.

### Export rule

No symbol becomes public merely because a file exists.

Exports must be:

- explicit;
- reviewed;
- versioned;
- documented;
- tested;
- profile-bound;
- safe at import time;
- free of network/persistence side effects.

[Back to top](#top)

---

## Generated types and adapters

Generated code can reduce drift but can also conceal authority errors.

### Permitted generation

Generated artifacts may mirror accepted schema shape when they include:

- source schema path or ID;
- source schema digest;
- generator identity and version;
- generation command;
- generated-file marker;
- deterministic output;
- regeneration test;
- compatibility note;
- review and rollback path.

### Generation must not

- rewrite contract meaning;
- add fields not present in the schema;
- remove fields silently;
- infer policy defaults;
- infer release state;
- embed secrets;
- download mutable schemas during normal builds;
- overwrite hand-written adapters without review;
- treat generated type success as evidence closure.

### Adapter classes

Every cross-profile adapter should declare:

| Field | Requirement |
|---|---|
| Source profile | exact version/ID |
| Target profile | exact version/ID |
| Direction | one-way or two-way |
| Lossiness | none, bounded, or prohibited |
| Defaults | explicit and contract-authorized |
| Unknown fields | reject, preserve out-of-band, or explicitly map |
| Validation | source and target checks |
| Receipt | required when trust-bearing persisted records change |
| Rollback | restore prior representation or re-run from canonical input |

[Back to top](#top)

---

## Lifecycle policy release and public safety

This package is not a lifecycle owner.

```text
RAW
  -> WORK / QUARANTINE
  -> PROCESSED
  -> CATALOG / TRIPLET
  -> PUBLISHED
```

### Lifecycle rules

- Package source must not store lifecycle records.
- Candidate assembly does not promote data.
- Schema validation does not promote data.
- Creating an EvidenceBundle-shaped object does not promote data.
- Package helpers must preserve phase and release refs supplied by callers.
- Unreleased or quarantined inputs must not become public because a constructor succeeded.
- Promotion remains a governed state transition, not a package method.

### Policy rules

The package may preserve:

- rights input;
- sensitivity input;
- obligations;
- policy refs;
- reason codes;
- audience context.

It must not decide:

- allow;
- deny;
- restrict;
- hold;
- abstain;
- redaction;
- generalization;
- release audience;
- public exposure.

### Public path

Public clients must not import this package as an authority surface.

Expected direction:

```text
package candidate
  -> validators / resolver / policy / review / release
  -> runtime response envelope
  -> governed API
  -> public client
```

[Back to top](#top)

---

## Failure and error semantics

### Fail-visible posture

Helpers should return typed issues rather than:

- guessing missing refs;
- selecting a schema profile automatically;
- filling required arrays with placeholders;
- inventing citations;
- substituting default rights;
- downgrading sensitivity;
- recomputing hashes with an inferred profile;
- resolving bundle refs;
- dropping unknown fields silently.

### Proposed issue families

These codes are illustrative and **PROPOSED**:

```text
evidence/profile-required
evidence/profile-unsupported
evidence/ref-required
evidence/ref-kind-invalid
evidence/bundle-ref-unverified
evidence/bundle-field-required
evidence/bundle-array-empty
evidence/claim-scope-unstructured
evidence/citation-required
evidence/rights-required
evidence/sensitivity-required
evidence/checksum-invalid
evidence/spec-hash-profile-unknown
evidence/adapter-lossy
evidence/dependency-owner-conflict
evidence/network-forbidden
evidence/persistence-forbidden
evidence/synthetic-only
```

The canonical reason-code vocabulary remains **NEEDS VERIFICATION**.

### Exception boundary

Programming errors may raise exceptions. Expected candidate invalidity should normally return inspectable issues suitable for deterministic tests and governed downstream handling.

[Back to top](#top)

---

## Security privacy and data minimization

### Default controls

Any future implementation should:

- perform no network access by default;
- perform no persistence by default;
- avoid import-time I/O;
- avoid environment credential reads;
- accept explicit inputs;
- minimize retained payloads;
- support redacted logs;
- avoid logging full evidence records;
- avoid logging secrets or restricted locations;
- avoid serializing living-person, genomic, archaeological, rare-species, or infrastructure-sensitive data into fixtures;
- reject unrestricted production records in test builders;
- make synthetic status explicit;
- use bounded recursion and collection sizes;
- validate untrusted structured input before expensive processing.

### Sensitive context

For rights, sovereignty, cultural sensitivity, living-person data, DNA/genomics, rare species, archaeology, infrastructure, and precise locations:

- do not infer safe exposure;
- preserve the strongest supplied sensitivity;
- do not create public projections without policy authorization;
- prefer omission, redaction, generalization, quarantine, or denial through the owning policy path;
- preserve transform/reason refs where changes are authorized.

### Logging

Safe logs should prefer:

- profile ID;
- candidate type;
- issue code;
- field path;
- counts;
- digests;
- request/run correlation refs.

Avoid raw values where a digest or reference is sufficient.

[Back to top](#top)

---

## Tests fixtures validators and CI

### Current verified posture

| Lane | Current evidence | Limit |
|---|---|---|
| Package tests | No README at exact checked package test path | No package behavior suite is established. |
| Package fixtures | No README at exact checked package fixture path | No package fixture family is established. |
| EvidenceRef contract fixtures | Existing minimal valid/invalid family | Schema coverage only; narrow. |
| EvidenceBundle contract fixtures | Existing minimal valid/invalid family | Schema coverage only; narrow. |
| Generic schema harness | Includes evidence family | Does not test package constructors/adapters. |
| EvidenceRef validator | Missing at schema-declared exact path | Metadata/file conflict. |
| EvidenceBundle validator | File exists | Does not prove package integration. |
| Dedicated evidence workflow | No `.github/workflows/evidence.yml` at exact path | No dedicated package CI established. |

### Minimum future behavior tests

A retained package should test:

1. exact current-profile EvidenceRef construction;
2. invalid `kind`;
3. missing `ref`;
4. optional `bundle_ref` preservation;
5. no claim that `bundle_ref` resolved;
6. exact current-profile EvidenceBundle construction;
7. every required bundle field;
8. empty required arrays;
9. invalid bundle ID;
10. invalid checksum string;
11. SpecHash shape;
12. unknown canonicalization profile;
13. source and target schema validation for adapters;
14. lossy adapter detection;
15. unknown-field handling;
16. deterministic serialization;
17. no network access;
18. no persistence;
19. import-time safety;
20. synthetic fixture marker;
21. sensitive fixture rejection;
22. delegation to identity/hashing/citation owners;
23. no resolver outcome fabrication;
24. no policy/release outcome fabrication;
25. correction/supersession context preservation;
26. rollback compatibility.

### Fixture classes

```text
valid/
invalid/
golden/
migration/
security/
sensitivity/
determinism/
```

These paths are **PROPOSED** and must be placed only after Directory Rules and repository convention checks.

### CI truth rule

A green workflow proves only what its steps execute.

Do not describe package behavior as tested until jobs run actual package tests and fail on the negative paths.

[Back to top](#top)

---

## Implementation admission sequence

The smallest sound change sequence is:

### Stage 0 — decide whether the package exists

1. Assign owners.
2. Inventory intended consumers.
3. Compare responsibilities with identity, hashing, citation, and resolver packages.
4. Choose keep-placeholder, retain-narrow, consolidate, remove, or shared-kernel.
5. Record the decision in an ADR or accepted package-boundary record when cross-package ownership changes.

### Stage 1 — define the contract

6. Define one narrow package purpose.
7. Select language only after consumer evidence.
8. Select package/distribution/import name.
9. Define dependency direction and cycle prevention.
10. Select accepted EvidenceRef, EvidenceBundle, SpecHash, citation, identity, and resolver profiles.
11. Define candidate and issue contracts.
12. Define what is deliberately out of scope.

### Stage 2 — add minimal implementation

13. Add package metadata.
14. Add source-root and import-module READMEs.
15. Add one EvidenceRef candidate constructor.
16. Add one EvidenceBundle candidate constructor.
17. Delegate identity/hash/citation operations.
18. Add explicit profile metadata.
19. Add no-network and no-persistence guards.

### Stage 3 — prove behavior

20. Add package tests and synthetic fixtures.
21. Add source and target schema validation.
22. Add deterministic/golden tests.
23. Add negative security and sensitivity tests.
24. Add package build/import tests.
25. Add real CI steps.
26. Record test evidence.

### Stage 4 — admit consumers

27. Add one governed internal consumer.
28. Confirm no public bypass.
29. Add compatibility and rollback documentation.
30. Version the package.
31. Add correction invalidation rules.
32. Expand only after observed reusable demand.

No broad helper framework should be created before Stage 0 closes.

[Back to top](#top)

---

## Compatibility correction and rollback

### Compatibility

Compatibility applies to:

- package/distribution name;
- import namespace;
- exported symbols;
- EvidenceRef profile;
- EvidenceBundle profile;
- SpecHash representation;
- citation representation;
- issue/result contracts;
- serialized candidate shape;
- dependency interfaces.

### Change discipline

A behavior-changing release should:

1. identify affected profiles and consumers;
2. classify breaking versus compatible change;
3. provide adapter/migration path;
4. test old and new profiles;
5. record lossiness;
6. preserve source inputs for reprocessing;
7. update docs and generated models;
8. update fixtures;
9. update release/rollback records where trust-bearing persisted data is affected.

### Correction propagation

When an evidence profile, source record, citation, checksum, rights statement, sensitivity label, or bundle membership is corrected:

- candidate builders must not preserve invalidated defaults;
- generated projections may need regeneration;
- resolver caches may need invalidation;
- dependent bundles may need supersession;
- public surfaces may need withdrawal or correction;
- receipts should identify the change;
- rollback targets should remain addressable.

This package does not perform those actions. It must preserve enough identifiers for owning systems to do so.

### Rollback triggers

Rollback package changes when they:

- duplicate sibling package authority;
- add silent fallback behavior;
- infer profiles;
- fabricate refs/citations/bundle membership;
- hide lossiness;
- perform network/persistence unexpectedly;
- weaken sensitivity;
- bypass resolver/policy/release;
- create a public trust path;
- break deterministic output;
- introduce an import cycle;
- publish a package without accepted ownership.

### Documentation-only rollback

For this README revision, rollback is a transparent revert restoring prior blob:

```text
a74e29bf907ded21098adce3ae8bf22f0f66d512
```

[Back to top](#top)

---

## Validation commands

These commands are proposed for a repository checkout.

### Inventory

```bash
find packages/evidence -maxdepth 5 -type f | sort
find packages/evidence-resolver -maxdepth 5 -type f | sort
find packages/identity packages/hashing packages/citation -maxdepth 5 -type f | sort
```

### Search ownership and consumers

```bash
git grep -n "packages/evidence\|from evidence\|import evidence" -- . ':!packages/evidence/README.md' || true
git grep -n "EvidenceRef\|EvidenceBundle\|spec_hash\|citation" -- packages apps pipelines tools tests fixtures || true
```

### Verify current schema lanes

```bash
python tools/validators/validate_evidence_bundle.py --fixtures
pytest -q tests/schemas/test_common_contracts.py
```

The EvidenceRef validator command is intentionally omitted because the schema-declared exact file was not found during this revision.

### Documentation checks

```bash
python - <<'PY'
from pathlib import Path
p = Path("packages/evidence/README.md")
text = p.read_text(encoding="utf-8")
assert text.count("# Evidence-Specific Shared Helper Package Boundary") == 1
assert "\t" not in text
assert not any(line.rstrip() != line for line in text.splitlines())
print("basic README checks passed")
PY
```

### Future package checks

After implementation exists:

```bash
# PROPOSED examples only
python -m pytest tests/packages/evidence
python -m build packages/evidence
python -m pip install --no-deps --force-reinstall packages/evidence/dist/*.whl
python -c "import <accepted_namespace>"
```

Do not copy these commands into CI until language, layout, and distribution are accepted.

[Back to top](#top)

---

## Definition of done

### This README revision

This revision is done when it:

- replaces stale implementation assumptions with current repository evidence;
- marks the package as documentation-only at the checked paths;
- records exact checked absences without overgeneralizing;
- preserves the `packages/` responsibility boundary;
- surfaces overlap with identity, hashing, citation, and resolver packages;
- requires a package-purpose decision before implementation;
- grounds EvidenceRef, EvidenceBundle, and SpecHash in current schemas;
- forbids silent profile translation;
- preserves cite-or-abstain and the trust membrane;
- defines validation and rollback;
- changes only this README.

### Future package implementation

Implementation is not done until:

- [ ] owners are assigned;
- [ ] package purpose is accepted;
- [ ] overlap is resolved;
- [ ] language and distribution are selected;
- [ ] package metadata exists;
- [ ] source layout exists;
- [ ] imports and exports are explicit;
- [ ] dependencies and cycles are reviewed;
- [ ] contract/schema profiles are pinned;
- [ ] package tests and fixtures exist;
- [ ] actual CI runs the tests;
- [ ] no-network/no-persistence behavior is proven;
- [ ] security and sensitive-data tests pass;
- [ ] one governed internal consumer is verified;
- [ ] public clients remain behind governed APIs;
- [ ] compatibility, correction, and rollback are documented;
- [ ] release or publication claims are evidence-backed.

[Back to top](#top)

---

## Open verification register

| ID | Question | Status | Closure evidence |
|---|---|---:|---|
| `EVID-PKG-001` | Should `packages/evidence/` remain in the repository? | NEEDS DECISION | ADR or accepted package-boundary record |
| `EVID-PKG-002` | What one responsibility is unique to this package? | NEEDS DECISION | Approved bounded-context statement |
| `EVID-PKG-003` | Who owns the package? | UNKNOWN | CODEOWNERS/steward assignment |
| `EVID-PKG-004` | Is the package language-neutral, Python, TypeScript, or another language? | UNKNOWN | Accepted package metadata |
| `EVID-PKG-005` | What is the distribution/package name? | UNKNOWN | Build metadata |
| `EVID-PKG-006` | What is the import namespace? | UNKNOWN | Source tree and import test |
| `EVID-PKG-007` | Which consumers require it? | UNKNOWN | Verified import/usage inventory |
| `EVID-PKG-008` | Which duties remain in `packages/identity/`? | NEEDS VERIFICATION | Cross-package ownership matrix |
| `EVID-PKG-009` | Which duties remain in `packages/hashing/`? | NEEDS VERIFICATION | Cross-package ownership matrix |
| `EVID-PKG-010` | Which duties remain in `packages/citation/`? | NEEDS VERIFICATION | Cross-package ownership matrix |
| `EVID-PKG-011` | Which duties remain in `packages/evidence-resolver/`? | NEEDS VERIFICATION | Cross-package ownership matrix |
| `EVID-PKG-012` | Is an ADR required for consolidation or deletion? | NEEDS VERIFICATION | Directory Rules/ADR review |
| `EVID-PKG-013` | What EvidenceRef profile is canonical? | NEEDS VERIFICATION | Accepted contract/schema version |
| `EVID-PKG-014` | What EvidenceBundle profile is canonical? | NEEDS VERIFICATION | Accepted contract/schema version |
| `EVID-PKG-015` | What canonicalization profile accompanies SpecHash? | NEEDS VERIFICATION | Accepted standard/schema/contract |
| `EVID-PKG-016` | Are `jcs:sha256:` and current SpecHash representations compatible? | CONFLICTED | Versioned migration decision |
| `EVID-PKG-017` | What citation representation is accepted? | NEEDS VERIFICATION | Citation contract/schema |
| `EVID-PKG-018` | Who owns citation validation? | NEEDS VERIFICATION | Accepted package/validator boundary |
| `EVID-PKG-019` | Who owns EvidenceRef URI grammar? | NEEDS VERIFICATION | Identity/contract decision |
| `EVID-PKG-020` | How is free-form `claim_scope` interpreted safely? | NEEDS VERIFICATION | Structured profile or bounded contract |
| `EVID-PKG-021` | Will the missing EvidenceRef validator be added or schema metadata corrected? | CONFLICTED | File addition or schema change |
| `EVID-PKG-022` | Where do package behavior tests live? | NEEDS VERIFICATION | Accepted test path and tests |
| `EVID-PKG-023` | Where do package fixtures live? | NEEDS VERIFICATION | Accepted fixture path and inventory |
| `EVID-PKG-024` | Is a dedicated package workflow required? | NEEDS VERIFICATION | Workflow decision and actual steps |
| `EVID-PKG-025` | What is the canonical issue-code vocabulary? | UNKNOWN | Contract/schema/registry |
| `EVID-PKG-026` | How are generated models versioned and checked for drift? | UNKNOWN | Generator contract and CI |
| `EVID-PKG-027` | How are adapters receipted when persisted trust records change? | UNKNOWN | Receipt contract and tests |
| `EVID-PKG-028` | What correction invalidates dependent candidates? | UNKNOWN | Correction/supersession contract |
| `EVID-PKG-029` | How are sensitive fixture inputs rejected? | UNKNOWN | Security tests |
| `EVID-PKG-030` | What package versioning policy applies? | UNKNOWN | Release/package policy |
| `EVID-PKG-031` | Is package publication intended? | UNKNOWN | Release record and artifact |
| `EVID-PKG-032` | What is the rollback procedure for consumers? | UNKNOWN | Tested rollback plan |

[Back to top](#top)

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---:|---|---|
| Previous `packages/evidence/README.md` | CONFIRMED | Existing planning intent and prior boundary language | Does not prove package implementation |
| Exact package path checks | CONFIRMED bounded findings | Documentation-only surface at checked paths | Not a recursive proof of total absence elsewhere |
| `packages/evidence-resolver/README.md` v0.2 | CONFIRMED | Resolver package boundary and current conflict posture | Does not prove resolver implementation |
| `packages/identity/README.md` | CONFIRMED README | Existing identity responsibility claim | Implementation maturity remains separately verified |
| `packages/hashing/README.md` | CONFIRMED README | Existing hashing/canonicalization responsibility claim | Architecture notation conflicts with current SpecHash |
| `packages/citation/README.md` | CONFIRMED README | Existing citation responsibility claim | Some resolver-language overlap remains |
| EvidenceRef schema | CONFIRMED / PROPOSED status | Current closed fields and enum | Does not validate URI, authority, rights, or closure |
| EvidenceBundle schema | CONFIRMED / PROPOSED status | Current required closure-candidate shape | Does not prove materialized closure, policy, review, or release |
| SpecHash schema | CONFIRMED / PROPOSED status | Current `sha256:` value shape | Does not identify canonicalization |
| EvidenceRef validator exact path | NOT FOUND | Metadata/file conflict | Does not prove no other validator exists |
| EvidenceBundle validator | CONFIRMED file | Schema fixture validator lane | Does not test this package |
| Generic schema harness | CONFIRMED test code | Evidence schema fixture discovery | Does not test package composition behavior |
| Directory Rules v1.4 | CONFIRMED doctrine | `packages/` implementation responsibility and authority separation | Does not decide whether this package should exist |
| Current revision workflow | CONFIRMED | One-file documentation update | Does not implement or validate package behavior |

---

## Maintainer checklist

Before editing this package boundary:

- [ ] Reconfirm current `main`.
- [ ] Recheck package-local files.
- [ ] Recheck sibling package boundaries.
- [ ] Recheck accepted ADRs.
- [ ] Recheck EvidenceRef/EvidenceBundle/SpecHash schemas.
- [ ] Recheck validator file state.
- [ ] Recheck test and fixture paths.
- [ ] Recheck consumers.
- [ ] Mark all implementation claims with evidence status.
- [ ] Keep public clients behind governed APIs.
- [ ] Preserve cite-or-abstain.
- [ ] Preserve lifecycle boundaries.
- [ ] Preserve policy/release separation.
- [ ] Preserve correction and rollback.
- [ ] Avoid new parallel schema, contract, policy, proof, receipt, or release homes.
- [ ] Make the smallest reversible change.

[Back to top](#top)
