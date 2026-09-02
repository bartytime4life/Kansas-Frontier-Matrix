<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-readme
title: schemas/contracts/ — Versioned Contract Schema Index
type: README
authority_class: schema-parent-index
version: v0.2
status: draft; repository-grounded; version-router; machine-shape-only; v1-configured; direct-policy-compatibility; non-semantic; non-policy; non-release
owner: "@bartytime4life — CONFIRMED CODEOWNERS review route; independent schema, contract, validation, policy, and documentation stewardship remain NEEDS VERIFICATION"
created: 2026-07-04
updated: 2026-08-13
policy_label: public
truth_posture: cite-or-abstain
owning_root: schemas/
responsibility: "Route versioned contract-backed machine shapes, preserve explicit compatibility boundaries, and connect schemas to their semantic contracts, fixtures, validators, tests, and governance without becoming a second authority for any of them."
current_path: schemas/contracts/README.md
supersedes:
  - "v0.1 documentation at the same path"
superseded_by: []
evidence_snapshot: "bartytime4life/Kansas-Frontier-Matrix main@0b0abda8f32ed93833bb5f51dbf1e24bf4460f25"
evidence_refs:
  - "schemas/contracts/README.md@cc2c5da78164ed9f2bb49a0bf2f34b660f78f11b"
  - "schemas/README.md@ce53d0ddb998ddcb8208d0367c90f9c25e31a8ad"
  - "schemas/contracts/policy/README.md@f051807bac9868ae6bb48227d1ce48d80ed7cfd8"
  - "schemas/contracts/v1/README.md@bbe931c9f7a5f0132522c0bda4fa5455c050a973"
  - "schemas/contracts/v1/@6f67859b2562910394722813181659ffd52bf79d"
  - "contracts/README.md@e0b7c126e00a8ac6e8890774ed26cf21aef534a"
  - "docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md@3c520ea8f2f8bcb3d478329a87d98b135ea335fd"
  - "docs/adr/ADR-0002-contracts-vs-schemas-split.md@e626d82970932c319a690fc6044727ed114ada6a"
  - "docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md@3ba5f902ffe20a65a259cb0a7dab07f1725d204b"
  - "docs/doctrine/directory-rules.md@fd49a0b83e55cef52c1124281f093e263526898d"
  - "control_plane/root_registry.yaml@024f668b5f0a9239bafa4f8b09e2afd86300ff8c"
  - ".github/workflows/schema-validation.yml@0e1562f539323daa401184738a0c490b51e2999b"
  - ".github/workflows/validator-suite.yml@dca889a3135b408767ff6cf21b7ce6eedfcc4781"
  - "tools/validators/validator_registry.json@c65c1c2b27b85be4bdc3c42d0555c6e8e44698e2"
  - "tools/validators/_common/run_all.py@39e57978b3d3d24769ab56cf5b805d51de18f33f"
  - "tools/validators/validate_all.py@728cf1404839a5b95e03d70d44567863a6f9b6df"
  - "tools/validate_all.py@c308015da780d7b72f56277b521fb0e42317651e"
  - "Makefile@c5d0aee3de558d76c1e1639bcfd8cf1c71a0d326"
  - ".github/CODEOWNERS@dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61"
related:
  - ../README.md
  - ./policy/README.md
  - ./v1/README.md
  - ../../contracts/README.md
  - ../../policy/README.md
  - ../../fixtures/README.md
  - ../../tests/README.md
  - ../../tests/schemas/README.md
  - ../../tests/contracts/README.md
  - ../../tools/validators/README.md
  - ../../tools/validators/validator_registry.json
  - ../../.github/workflows/schema-validation.yml
  - ../../.github/workflows/validator-suite.yml
  - ../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - ../../docs/adr/ADR-0002-contracts-vs-schemas-split.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../docs/doctrine/directory-rules.md
tags: [kfm, schemas, contracts, versioning, json-schema, compatibility, machine-shape, validation, governance, no-parallel-authority]
notes:
  - "Current direct children are README.md, policy/, and v1/; the unversioned policy/ child is a documentation-only compatibility lane whose declared target is schemas/contracts/v1/policy/."
  - "The pinned v1 tree contains 53 direct child directories and 855 *.schema.json files; counts establish tracked topology only, not family maturity, contract pairing, fixture coverage, consumer closure, acceptance, or release readiness."
  - "Current workflow configuration treats schemas/contracts/v1 as the v1 validation surface, while ADR-0001 and the stricter coupling portions of ADR-0002 remain proposed. Configuration does not accept an ADR."
  - "This revision changes documentation only and creates no schema, contract, policy, fixture, test, validator, lifecycle, review, release, deployment, or publication effect."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `schemas/contracts/` — Versioned Contract Schema Index

> **One-line purpose.** `schemas/contracts/` routes versioned, contract-backed machine shapes and their compatibility boundaries without becoming semantic-contract, policy, fixture, validator, test, data, or release authority.

[![Status: draft](https://img.shields.io/badge/status-draft-d97706?style=flat-square)](#status-and-evidence)
[![Responsibility: machine shape](https://img.shields.io/badge/responsibility-machine%20shape-0969da?style=flat-square)](#authority-and-inheritance)
[![Configured surface: v1](https://img.shields.io/badge/configured%20surface-v1-8250df?style=flat-square)](#version-and-compatibility-routing)
[![Direct compatibility: policy](https://img.shields.io/badge/policy%2F-compatibility%20only-6e7781?style=flat-square)](#version-and-compatibility-routing)
[![Publication: none](https://img.shields.io/badge/publication-none-b42318?style=flat-square)](#non-effects-and-trust-boundary)

> [!IMPORTANT]
> **Shape and meaning stay separate.** Accepted ADR-0029 adopts the repository responsibility-root model: `schemas/` owns machine-checkable shape, while `contracts/` owns semantic meaning. A schema path, a successful validator, or a configured workflow cannot replace the paired semantic contract or accept a proposed ADR.

<!-- callout-separator -->

> [!WARNING]
> **Do not write new schemas into the unversioned `policy/` child.** That lane currently contains compatibility documentation and an empty-directory sentinel only. Its declared target is `schemas/contracts/v1/policy/`; new schemas, references, registries, fixtures, validators, and consumers must not extend the unversioned lane.

<!-- callout-separator -->

> [!CAUTION]
> **Schema-valid is not system-approved.** Machine-shape conformance does not establish semantic truth, source authority, evidence closure, policy approval, consent, rights clearance, sensitivity clearance, review completion, release readiness, public safety, or publication.

**Quick navigation:** [Purpose](#purpose) · [Status](#status-and-evidence) · [Authority](#authority-and-inheritance) · [Map](#current-direct-child-map) · [Version routing](#version-and-compatibility-routing) · [Inventory](#live-v1-inventory) · [Responsibilities](#responsibility-routing) · [Belongs](#what-belongs-here) · [Prohibited](#what-is-prohibited) · [Flow](#inputs-outputs-writers-and-consumers) · [Trust](#non-effects-and-trust-boundary) · [Storage](#exposure-mutation-retention-and-storage) · [Authoring](#schema-authoring-and-versioning-rules) · [Validation](#validation-and-negative-checks) · [CI](#ci-and-execution-surface) · [Change planning](#version-root-and-compatibility-change-planning) · [Contribute](#contributor-workflow) · [Review](#review-and-escalation) · [Rollback](#correction-rollback-deprecation-and-retirement) · [Open items](#open-verification-items) · [References](#references)

---

<a id="purpose"></a>

## Purpose

`schemas/contracts/` is the version-routing boundary beneath the canonical `schemas/` responsibility root. It exists to:

- route contributors and tools toward configured version roots;
- keep machine shape explicitly paired with, but separate from, semantic contract meaning;
- make compatibility paths visible without allowing them to evolve as parallel authority;
- state the conditions for adding, changing, migrating, deprecating, or retiring a version root;
- connect schemas to fixtures, validators, executable tests, policy, and lifecycle decisions while preserving their separate ownership;
- prevent directory presence, file count, or validator success from being described as completeness or approval.

This README owns the parent routing contract and its direct children only. The [`v1/` README](./v1/README.md) owns deeper version-local navigation and lineage. Child schemas own their machine constraints; paired documents under [`contracts/`](../../contracts/README.md) own semantic meaning.

Nothing in this document creates a new version, moves a schema, changes a `$id`, accepts ADR-0001 or ADR-0002, activates a policy, modifies validation, or publishes an artifact.

[Back to top](#top)

---

<a id="status-and-evidence"></a>

## Status and Evidence

This revision is grounded in the repository state pinned in the metadata block. Later repository state must be re-inspected before relying on counts, paths, workflow commands, or decision status.

| Question | Repository-grounded answer | Status |
| --- | --- | --- |
| Does this parent path exist? | Yes; this README and two direct child directories are tracked. | **CONFIRMED** |
| What are the direct child directories? | `policy/` and `v1/`. | **CONFIRMED** |
| What is `policy/` at this level? | A documentation-only compatibility lane declaring `schemas/contracts/v1/policy/` as its current target. | **CONFIRMED; migration closure unverified** |
| What is `v1/`? | The version tree targeted by current schema-validation configuration. | **CONFIRMED configured surface** |
| Is `v1/` accepted as the permanent canonical schema home? | ADR-0001 proposes that narrower decision; it is not accepted in the pinned source. | **PROPOSED** |
| Is the contracts-versus-schemas responsibility split adopted? | ADR-0029 accepts the top-level Directory Rules placement model; ADR-0002's stricter coupling and readiness detail remains proposed. | **PARTLY accepted; narrower detail proposed** |
| Does v1 contain real schemas? | Yes; the pinned recursive tree contains 855 `*.schema.json` files. | **CONFIRMED topology** |
| Are all v1 families mature, paired, tested, and consumed? | File presence and aggregate counts cannot prove those properties. | **NOT ESTABLISHED** |
| Does this README publish or promote anything? | No. It is repository documentation only. | **CONFIRMED boundary** |

### Evidence precedence

When sources disagree, apply this order:

1. accepted ADRs and adopted Directory Rules for responsibility placement;
2. exact current repository bytes for actual paths and configured behavior;
3. machine projections such as the root registry, which describe but do not create authority;
4. proposed ADRs and design documents for pending decisions;
5. this README and child indexes for local routing;
6. file names, folder age, comments, and examples as context only.

An older README count or proposed architecture statement does not override the current tree. A current implementation may demonstrate configuration, but it does not silently accept a proposed governance decision.

[Back to top](#top)

---

<a id="authority-and-inheritance"></a>

## Authority and Inheritance

This directory inherits its responsibility from [`schemas/`](../README.md): machine-checkable shape for KFM objects. The root registry currently projects `schemas/` as public, versioned, durable, and canonical for schema artifacts, while prohibiting semantic contracts, policy, and lifecycle data from that root.

The parent boundary does not outrank:

- accepted ADRs or the adopted [Directory Rules](../../docs/doctrine/directory-rules.md);
- actual schema files and their declared JSON Schema dialect, `$id`, and constraints;
- paired semantic contracts under [`contracts/`](../../contracts/README.md);
- policy rules and policy decisions under [`policy/`](../../policy/README.md);
- fixture manifests and payloads under [`fixtures/`](../../fixtures/README.md);
- executable assertions under [`tests/`](../../tests/README.md);
- validator implementations and registry selection under [`tools/validators/`](../../tools/validators/README.md);
- evidence, review, correction, rollback, release, and publication decisions in their governed roots.

### Decision-status boundary

| Source | Current role | What it does not prove |
| --- | --- | --- |
| [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Accepted adoption of Directory Governance Standard v2 | It does not by itself accept every older nested placement proposal. |
| [Directory Rules](../../docs/doctrine/directory-rules.md) | Adopted responsibility-root and README-profile rules | It does not declare each schema family mature. |
| [ADR-0001](../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) | Proposed narrower canonical-home decision | Current workflow use does not make it accepted. |
| [ADR-0002](../../docs/adr/ADR-0002-contracts-vs-schemas-split.md) | Proposed coupling, readiness, and enforcement detail around the split | The accepted top-level split does not automatically accept all stricter details. |
| [Root registry](../../control_plane/root_registry.yaml) | Machine-readable projection of root responsibility | A projection cannot create or amend governance authority. |

Where accepted placement, current behavior, and a proposal diverge, document the divergence and hold the authority claim. Do not resolve it by assertion.

[Back to top](#top)

---

<a id="current-direct-child-map"></a>

## Current Direct-Child Map

Per the Directory Rules, this parent map lists direct children only:

```text
schemas/contracts/
├── README.md    # this version-routing and boundary contract
├── policy/      # unversioned, documentation-only compatibility lane
└── v1/          # current configured version tree
```

| Direct child | Local role | New writes | Deeper ownership |
| --- | --- | --- | --- |
| [`policy/`](./policy/README.md) | Compatibility index pointing to `v1/policy/` | **No new schema or consumer writes** | Its README owns migration notes until retirement or replacement. |
| [`v1/`](./v1/README.md) | Current configured version tree | Only through reviewed version-local schema work | Its README and child READMEs own deeper routing. |

The 53 direct child directories beneath `v1/` are deliberately not repeated in this parent map. Repeating them here would create two hand-maintained inventories and invite drift. Inspect the live tree and the version-local index when changing a family.

[Back to top](#top)

---

<a id="version-and-compatibility-routing"></a>

## Version and Compatibility Routing

### Current finite routing result

| Requested destination | Route | Authority posture |
| --- | --- | --- |
| New or changed v1 machine shape | An accepted family beneath `schemas/contracts/v1/` | Configured validation surface; family maturity must be established locally. |
| Policy-related v1 machine shape | `schemas/contracts/v1/policy/` | Do not use the direct unversioned `policy/` lane. |
| Semantic meaning | A paired object-family document under `contracts/` | Separate semantic responsibility. |
| New major schema version | No destination is pre-authorized | Requires accepted decision and dependency-closed migration plan. |
| Historical unversioned policy reference | Resolve through `schemas/contracts/policy/README.md`; migrate the consumer | Compatibility read only; no new writer. |

### `v1/` posture

`schemas/contracts/v1/` is the only current version root and the configured v1 validation surface. That statement describes repository behavior. It does not establish that:

- every family is canonical, complete, production-ready, or active;
- every schema has a verified semantic-contract pair;
- every valid and invalid fixture exists;
- every consumer uses the same schema or `$id`;
- every placeholder, `.gitkeep`, example, or README marks an implemented feature;
- the proposed narrower canonical-home decision has been accepted.

### Direct `policy/` compatibility posture

The unversioned `schemas/contracts/policy/` lane contains its README and an empty sentinel, not schema payloads. Under its current contract:

- new schemas go to the versioned policy family;
- new `$ref` values must not target the unversioned lane;
- registries, fixtures, validators, tests, and consumers must not make new dependencies on it;
- historical references must be inventoried and migrated before retirement;
- the lane may remain as a bounded tombstone or navigation surface while verified consumers require it;
- migration completion, external consumers, and deletion safety remain unverified.

### Future version roots

No `v2/` or other version root is implied by this index. Creating one requires an accepted decision or equivalent repository-authorized migration record covering:

- the breaking-change rationale and object-family scope;
- `$id`, `$schema`, `$ref`, and namespace strategy;
- semantic-contract pairing and version semantics;
- writer, reader, validator, test, registry, workflow, and external-consumer inventory;
- fixture polarity and compatibility matrix;
- single-write behavior and any bounded dual-read window;
- correction, rollback, deprecation, and retirement criteria;
- owner, reviewers, start state, exit criteria, and expiry.

Copying `v1/` is not a versioning decision.

[Back to top](#top)

---

<a id="live-v1-inventory"></a>

## Live v1 Inventory

At the pinned evidence snapshot, the recursive `v1/` tree contains:

| Measure | Count | Interpretation |
| --- | ---: | --- |
| Direct child directories | 53 | Version-local routing breadth, not 53 proven mature domains. |
| Recursive tree entries | 1,138 | Git tree topology, including directories and files. |
| Descendant directory entries | 109 | Nested organization only. |
| File blobs | 1,029 | Tracked files of all kinds. |
| `*.schema.json` files | 855 | Candidate schema documents subject to configured v1 meta-validation. |
| Other `.json` files | 9 | Examples or machine artifacts that must not be inferred to be JSON Schemas. |
| `README.md` files | 107 | Local documentation and routing; not implementation proof. |
| `.gitkeep` sentinels | 57 | Empty-path retention; not capability or maturity. |
| Other Markdown files | 1 | Additional documentation, not a schema. |

The counts are deliberately descriptive. They do not prove that all 855 schema files are independently reviewed, semantically paired, fixture-backed, exercised by a family-specific validator, used by a live consumer, compatible with all prior data, or eligible for release.

The version-local README is a navigation aid, not a guaranteed exhaustive manifest. When an index and the live tree differ, reconcile the documentation in a focused change; do not delete or promote a family solely to make the count match.

[Back to top](#top)

---

<a id="responsibility-routing"></a>

## Responsibility Routing

| Concern | Responsible surface | Boundary at `schemas/contracts/` |
| --- | --- | --- |
| Machine-checkable object shape | `schemas/contracts/<version>/<family>/` | Route versions and compatibility; do not duplicate family constraints in prose. |
| Semantic object meaning and invariants | [`contracts/`](../../contracts/README.md) | Link the paired contract; do not treat JSON Schema as complete meaning. |
| Access, redaction, consent, retention policy | [`policy/`](../../policy/README.md) | A schema may represent fields but cannot decide policy. |
| Representative valid and invalid instances | [`fixtures/`](../../fixtures/README.md) | Do not store fixture payloads at this parent. |
| Executable schema assertions | [`tests/schemas/`](../../tests/schemas/README.md) | Tests establish bounded behavior, not semantic or release authority. |
| Executable contract/integration assertions | [`tests/contracts/`](../../tests/contracts/README.md) | Keep cross-surface assertions outside the schema tree. |
| Validator code and selection | [`tools/validators/`](../../tools/validators/README.md) and its [registry](../../tools/validators/validator_registry.json) | A schema file does not self-register or self-execute. |
| Workflow orchestration | [schema-validation](../../.github/workflows/schema-validation.yml) and [validator-suite](../../.github/workflows/validator-suite.yml) | Workflow configuration proves intended execution only. |
| Source, evidence, and lifecycle records | Governed `data/`, registry, evidence, and receipt surfaces | Never store real records under schema paths. |
| Release, correction, and rollback decisions | [`release/`](../../release/README.md) and governed decision records | Validation cannot release, correct, roll back, or publish an object. |
| Version-placement governance | Accepted ADRs and adopted Directory Rules | This README records status; it does not accept decisions. |

When one change spans several surfaces, keep responsibility separate while reviewing the dependency closure together.

[Back to top](#top)

---

<a id="what-belongs-here"></a>

## What Belongs Here

At the parent level:

- this README;
- explicitly reviewed version-root directories;
- bounded compatibility indexes or tombstones with a declared canonical target, no-new-writes rule, consumer inventory, and retirement criteria;
- version-routing, migration, deprecation, and cross-version compatibility documentation;
- links to paired contracts, fixtures, validators, tests, ADRs, registries, and release or migration evidence;
- small machine-readable version manifests only if an accepted design establishes their schema, writer, consumer, validation, and single-authority behavior.

Inside a reviewed version and family lane:

- JSON Schema documents using the repository's configured dialect and identity rules;
- family-local README routing and bounded authoring guidance;
- schema-only reusable definitions where the version structure explicitly assigns them;
- compatibility aliases only when one canonical writer, target, consumer plan, and retirement condition are documented.

Presence in this hierarchy is necessary placement evidence for a schema artifact, not sufficient maturity evidence.

[Back to top](#top)

---

<a id="what-is-prohibited"></a>

## What Is Prohibited

Do not place or establish here:

- semantic contract prose as a substitute for the paired `contracts/` document;
- policy rules, policy decisions, rights approvals, consent decisions, sensitivity approvals, or redaction outcomes;
- source exports, production data, lifecycle records, EvidenceBundles, receipts, proofs, review records, release manifests, correction records, rollback records, or published artifacts;
- fixture payloads, golden outputs, test code, validator implementation, application packages, pipelines, services, UI/API code, map code, tiles, screenshots, or generated dashboards;
- secrets, credentials, private endpoints, private keys, tokens, or restricted source content;
- new unversioned schemas or new dependencies on compatibility-only paths;
- the same writable schema under multiple version, flat, domain, or compatibility paths without an accepted migration and single-writer rule;
- placeholder files or README claims that describe a family as implemented, canonical, validated, active, safe, or released without bounded evidence;
- direct schema files at the parent root when a reviewed version and family destination is required;
- permissive validation commands, swallowed errors, network-dependent checks, or empty-case success presented as proof.

Do not encode mutable policy decisions as schema enums or required values merely to make them machine-checkable. Represent the data shape in schema and keep the deciding rule in its policy authority.

[Back to top](#top)

---

<a id="inputs-outputs-writers-and-consumers"></a>

## Inputs, Outputs, Writers, and Consumers

| Role | Current contract |
| --- | --- |
| Inputs | Accepted placement decisions, paired semantic contracts, version-local schema requirements, compatibility constraints, and verified consumer needs. |
| Parent output | Human-readable version and compatibility routing only. |
| Version output | JSON Schema documents and version-local documentation under reviewed child lanes. |
| Parent writer | Maintainers changing this README through reviewed Git history. |
| Schema writers | Verified schema-family maintainers acting through reviewed version-local changes; independent stewardship remains to be confirmed. |
| Human consumers | Contract authors, schema authors, fixture/test/validator maintainers, reviewers, release maintainers, and integrators. |
| Machine consumers | JSON parsers, schema meta-validation, registered validators, tests, `$ref` resolvers, and applications that explicitly bind to a schema identity. |
| Non-consumers | Policy engines, release systems, and public clients do not gain authority merely by reading schema bytes. |

### Writer rules

- One schema identity has one canonical writable source at a time.
- Generated copies, vendored snapshots, or compatibility mirrors must declare source, generator, digest, edit policy, and retirement condition.
- A new consumer must bind to a stable schema identity or reviewed path; it must not discover authority from the newest-looking directory name.
- A compatibility path must not receive new writers while it is designated read-only or documentation-only.
- Documentation and metadata updates must not mutate schema behavior by implication.

### Consumer obligations

Consumers must:

- pin or otherwise govern the schema version they enforce;
- distinguish path compatibility from schema-identity compatibility;
- surface unsupported or ambiguous versions as failures, not silent fallback;
- preserve actionable diagnostics without leaking restricted instance content;
- participate in migration, deprecation, and rollback testing before a referenced path or `$id` changes.

[Back to top](#top)

---

<a id="non-effects-and-trust-boundary"></a>

## Non-Effects and Trust Boundary

Editing this README, adding a schema, or passing the configured suite does not by itself:

- accept, reject, supersede, or implement an ADR;
- prove the paired semantic contract is complete or approved;
- establish source authority, evidence truth, identity resolution, or provenance closure;
- approve access, redaction, consent, rights, sensitivity, retention, or public display;
- admit an object into a lifecycle stage;
- create a review, receipt, proof, release, correction, rollback, deployment, or publication decision;
- activate a service, write production data, alter an external system, or widen exposure;
- prove that every reader uses the reviewed schema version.

This is a public repository surface. Schema titles, descriptions, examples, defaults, `$comment` values, test diagnostics, and migration notes must exclude secrets and restricted content. For sensitive domains, describe the abstract shape without embedding living-person data, DNA/genomic material, precise protected locations, private-land relationships, culturally restricted knowledge, or critical-infrastructure vulnerability details.

If a schema must represent sensitive fields, the field's existence does not authorize collection, retention, linkage, display, or disclosure. Those decisions remain in policy and governed lifecycle controls.

[Back to top](#top)

---

<a id="exposure-mutation-retention-and-storage"></a>

## Exposure, Mutation, Retention, and Storage

| Concern | Current rule |
| --- | --- |
| Exposure | Public repository source; schema and documentation content must be safe for repository-wide visibility. |
| Mutation | Reviewed Git commits only; no runtime or external writer is authorized. |
| Retention | Durable while a schema version or verified consumer remains supported; documentation-only compatibility paths require explicit review. |
| Physical storage | UTF-8 text in Git. This path is not an object store, database, cache, queue, or secret store. |
| Generation | No parent-index generator is established. Generated schema bytes require declared provenance and edit policy. |
| Immutability | Git preserves history, but current-path bytes are mutable through review; consumers needing immutability must pin identities and revisions. |
| Deletion | Requires consumer, `$ref`, registry, fixture, validator, test, workflow, documentation, and external-reference closure. |
| Rename or move | Requires exact old-to-new mapping, compatibility classification, link repair, and rollback evidence. |
| Backup and recovery | Git history supports byte recovery; operational consumer recovery remains the owning system's responsibility. |

Do not store validation logs, compiled bundles, caches, temporary outputs, generated receipts, or migration payloads here. If a tool compiles schemas for runtime use, its output location, digest, release binding, and cleanup policy must be governed elsewhere.

[Back to top](#top)

---

<a id="schema-authoring-and-versioning-rules"></a>

## Schema Authoring and Versioning Rules

### Identity and dialect

Current configured v1 checks require each `*.schema.json` file under `schemas/contracts/v1/` to:

- parse as JSON;
- declare JSON Schema Draft 2020-12;
- carry a repository-unique `$id`.

Authors must also:

- treat `$id` as externally observable identity, not a decorative label;
- keep `$ref` targets resolvable, intentional, and within reviewed dependency boundaries;
- distinguish a path move from an identity change;
- avoid ambiguous aliases and case-only or punctuation-only identity forks;
- document any external reference, retrieval requirement, vendoring strategy, and offline-validation behavior;
- preserve deterministic validation without live network or credentials unless an accepted design explicitly governs otherwise.

### Shape and semantic pairing

Every material schema family should identify its paired semantic contract or approved profile. The pair must agree on:

- object identity and family;
- required and optional fields;
- field meaning, units, cardinality, and nullability;
- lifecycle and version semantics;
- relationships and referenced identities;
- prohibited states and compatibility expectations;
- correction and deprecation behavior.

JSON Schema can enforce representable constraints. Meaning that cannot be fully encoded remains normative in the semantic contract and may require fixtures, validators, or review evidence.

### Constraint design

- Make `required`, `additionalProperties`, nullability, and union behavior explicit and intentional.
- Use strict constraints only when they reflect accepted semantics and compatible producer behavior.
- Do not rely on `format` annotations unless the enforcing validator behavior is verified.
- Keep examples non-sensitive, synthetic, and subordinate to valid/invalid fixture coverage.
- Prefer reusable definitions within the reviewed version boundary over copied fragments that can drift.
- Reject unknown versions and structurally invalid instances with actionable, non-sensitive diagnostics.
- Preserve negative tests for invalid fixtures and the reason each fixture must fail.

### Change classification

| Change | Default classification | Required closure |
| --- | --- | --- |
| Description, title, or non-behavioral annotation repair | Documentation-compatible | Markdown/JSON parse, schema meta-validation, link and identity review. |
| Optional field addition | Potentially backward-compatible | Contract pairing, producer/consumer review, valid/invalid fixtures, validator/tests. |
| Required field addition | Breaking for existing producers or stored instances | Migration plan, version decision, consumer inventory, rollback. |
| Constraint tightening | Potentially breaking | Corpus/fixture analysis, invalid-case reason review, consumer migration. |
| Constraint widening | Semantically material | Contract/policy review; prove newly admitted values are intended. |
| Field rename, removal, or type change | Breaking | New version or accepted migration, dual-read/write rules if needed, deprecation plan. |
| `$id` or `$ref` change | Identity/reference breaking until proven otherwise | Full reference and consumer closure, compatibility mapping, rollback. |
| Path-only move | Operationally breaking until consumers are checked | Imports, links, path filters, registries, generators, external references, tombstone plan. |

SemVer labels alone do not prove compatibility. Compatibility is an observed relationship among schema identities, instance populations, writers, readers, validators, and governed meaning.

[Back to top](#top)

---

<a id="validation-and-negative-checks"></a>

## Validation and Negative Checks

Run the smallest relevant check first, then the dependency-closed aggregate for material schema behavior.

### Inspect parent routing and live inventory

```bash
# Direct parent routing only.
find schemas/contracts -mindepth 1 -maxdepth 2 -print | LC_ALL=C sort

# Count candidate v1 JSON Schema documents.
find schemas/contracts/v1 -type f -name '*.schema.json' -print \
  | LC_ALL=C sort \
  | wc -l

# Parse every JSON document under this subtree.
find schemas/contracts -type f -name '*.json' -print0 \
  | xargs -0 -r -n 1 python -m json.tool >/dev/null
```

Review differences against a pinned commit. Counts alone are not pass criteria.

### Run current registered validation surfaces

```bash
# Show registered validators and profiles.
python tools/validate_all.py --list

# Run the registry-defined full profile.
python tools/validate_all.py --profile full

# Run the historical schema compatibility entrypoint.
make schemas

# Run executable schema and contract tests.
python -m pytest -q tests/schemas tests/contracts

# Run validators plus executable tests.
make validate
```

### Documentation-only validation

For a change limited to this README, also verify:

- UTF-8 encoding and one final newline;
- exactly one KFM metadata block and the preserved document ID;
- the exact H1 and unique explicit anchors;
- Markdown lint and repository metadata checks;
- every repository-relative link and fragment at the pinned base or proposed head;
- no unrelated file, generated receipt, schema, contract, policy, fixture, test, validator, or workflow change;
- exact local-to-remote blob equality after publication to a branch.

### Required negative assertions

- no command suppresses a nonzero exit with a shell fallback, broad exception swallowing, or empty-case success as proof;
- invalid fixtures fail for the reviewed reason, not merely for any nonzero exit;
- valid fixtures pass without network, credentials, wall-clock dependence, randomness, or mutable service state unless explicitly governed;
- duplicate `$id` values and wrong v1 dialect declarations fail;
- unresolved or unintended `$ref` targets fail before release use;
- a schema change cannot write lifecycle data, modify policy, emit a release decision, or publish an artifact;
- the unversioned `policy/` lane remains free of schema payloads and new consumers;
- a proposed or placeholder family is not upgraded by prose, count, or green aggregate output.

[Back to top](#top)

---

<a id="ci-and-execution-surface"></a>

## CI and Execution Surface

### Schema-validation workflow

The current [schema-validation workflow](../../.github/workflows/schema-validation.yml) establishes this configured behavior:

| Step | Confirmed behavior | Boundary |
| --- | --- | --- |
| Trigger | Pull requests, pushes to `main`, and dispatch; `schemas/**` changes are included. | Trigger inclusion does not make a README executable input. |
| JSON inventory | Parses JSON under `schemas/`. | JSON parse proves syntax only. |
| Schema metadata | Meta-validates every `*.schema.json`. | Meta-validity does not prove semantic pairing or consumer compatibility. |
| Canonical v1 check | Requires v1 schema files to declare Draft 2020-12 and unique `$id` values. | This is configured behavior, not acceptance of ADR-0001. |
| Fixture preflight | Pins eight fixture-backed compatibility validators and requires reviewed valid/invalid lanes. | Fixture inventory is not the full validator registry. |
| Aggregate schemas | Runs `make schemas`. | The compatibility runner delegates to registry-defined validation. |
| Executable tests | Runs `python -m pytest -q tests/schemas tests/contracts`. | Assertions live under `tests/`, not this tree. |
| Output | Process logs and job summary. | No governed report, receipt, proof, release object, or publication is emitted. |

### Full validator profile

The current [validator registry](../../tools/validators/validator_registry.json) defines ten full-profile validators:

- eight fixture-backed object-family validators; and
- two repository guardrails: workflow security and repository topology.

The [validator-suite workflow](../../.github/workflows/validator-suite.yml) exercises the full profile and fail-closed guardrail behavior. Do not describe the eight fixture-backed validators as the complete full profile.

Workflow source proves configured intent. Only the exact-head workflow conclusion proves that a particular revision ran. A green conclusion remains bounded validation evidence; a red conclusion requires log-level classification as head-specific, inherited, flaky, blocked, or cancelled before any claim is made.

[Back to top](#top)

---

<a id="version-root-and-compatibility-change-planning"></a>

## Version-Root and Compatibility Change Planning

### Change classes

| Class | Examples | Minimum decision burden |
| --- | --- | --- |
| Parent documentation | Link, wording, evidence pin, or routing clarification | Preserve identity and boundaries; validate docs and exact scope. |
| Version-local additive schema change | Optional field, new definition, new family | Contract pairing, fixtures, validator/tests, consumer review. |
| Breaking schema change | Required field, removal, rename, tighter constraint, identity change | Version or migration decision, full consumer closure, deprecation and rollback. |
| Compatibility-lane change | Alias, mirror, tombstone, rename, deletion | Single writer, verified consumers, bounded dual-read, expiry, link/path repair. |
| New version root | `v2/` or equivalent | Accepted architecture decision and dependency-closed migration program. |
| Tooling or CI change | Registry, validator, workflow, Makefile, generator | Separate executable scope, security review, positive/negative evidence, canary behavior. |

### Required migration record

For a breaking, path, identity, or version-root change, record:

1. exact source and target paths and schema identities;
2. governing decision and current status;
3. affected object families and semantic contracts;
4. writers, readers, `$ref` users, registries, validators, tests, workflows, documentation, and external consumers;
5. source-instance compatibility findings and fixture matrix;
6. single-write target and any time-bounded dual-read or adapter behavior;
7. start state, checkpoints, exit criteria, owner, reviewers, and expiry;
8. correction, rollback, deprecation, and retirement procedure;
9. evidence that no parallel writable authority remains at closure.

A migration is not complete when files are copied. It is complete when writers, consumers, references, validation, documentation, and rollback obligations have closed.

[Back to top](#top)

---

<a id="contributor-workflow"></a>

## Contributor Workflow

### Parent README maintenance

1. Pin current `main`, the target blob, the direct-child tree, and relevant governing sources.
2. Search open pull requests and recent target history for competing work.
3. Reconcile the direct `policy/` compatibility lane and the current version-root configuration.
4. Edit only this README when no schema, policy, validator, workflow, or migration behavior changes.
5. Preserve the exact path, document ID, H1, version-routing purpose, and compatibility posture.
6. Validate Markdown, metadata, links, anchors, sensitive-content posture, and no-loss coverage.
7. Recheck `main` immediately before writing the branch.
8. Publish a focused draft PR, verify exact remote bytes, and classify hosted checks.

### Schema-family change

1. Identify the paired semantic contract and owning family.
2. Determine the change classification and compatibility impact.
3. Pin the current schema identity, path, fixtures, validators, tests, and consumers.
4. Edit the canonical writable schema only.
5. Add or update valid and invalid fixtures with explicit expected outcomes.
6. Update validator and executable-test coverage in their own responsibility roots.
7. Run the narrow checks, full profile, and dependency-closed tests.
8. Record migration, correction, rollback, and release implications.
9. Keep the PR draft until exact-head evidence and required review are complete.

### New version or compatibility route

Stop before creating directories. Resolve authority, identity, writers, consumers, migration, expiry, and rollback first. Do not combine an undecided architecture change with a large copied schema tree.

[Back to top](#top)

---

<a id="review-and-escalation"></a>

## Review and Escalation

`.github/CODEOWNERS` currently routes `/schemas/` changes to `@bartytime4life`. That is a GitHub review route, not proof of independent schema, contract, validation, policy, security, domain, or release approval.

| Change | Minimum review perspectives |
| --- | --- |
| Typo, link, or non-semantic routing correction | Schema-path owner route and documentation review |
| Constraint or identity change | Schema, paired-contract, fixture, validator, test, and affected consumer/domain review |
| Sensitive-field representation | Schema, contract, privacy/policy, security, source/evidence, and affected domain review |
| New family or version root | Architecture, schema, contracts, validation, migration, security, operations, and documentation review |
| Compatibility alias, mirror, move, or deletion | Verified writers/readers, registry/reference review, migration, correction, rollback, and expiry review |
| Release-facing use | Separate release and trust review in addition to technical validation |

Escalate rather than guess when:

- accepted governance and current implementation appear to conflict;
- a proposed ADR is being treated as accepted because code already points to the path;
- a schema lacks a verified semantic contract or owner;
- `$id`, `$ref`, path, or version changes have unverified consumers;
- the unversioned `policy/` lane contains unexpected payloads or new dependencies;
- validation requires network, credentials, restricted instances, or an external side effect;
- a passing result conflicts with fixture intent or consumer behavior;
- required checks, rulesets, owners, or rollback responsibility cannot be verified.

[Back to top](#top)

---

<a id="correction-rollback-deprecation-and-retirement"></a>

## Correction, Rollback, Deprecation, and Retirement

### Documentation rollback

Before merge, close the draft PR and abandon the scoped branch.

After merge, use a focused reviewed revert or restore the immediate prior v0.1 blob:

```text
cc2c5da78164ed9f2bb49a0bf2f34b660f78f11b
```

Do not roll back by modifying schemas, contracts, fixtures, validators, tests, workflows, policies, data, releases, or topology baselines unless those bytes were part of the reviewed dependency closure.

### Incorrect routing or authority claim

1. Mark the affected statement as held or conflicted.
2. Pin the contradictory accepted decision and current repository evidence.
3. Identify the actual writer, consumer, and decision owner.
4. Correct this README and every directly dependent link or index.
5. Preserve the prior claim in Git history and the review record.
6. Verify that the correction creates no parallel writable authority.

### Schema rollback

Before reverting a schema change, inspect:

1. `$id` and `$ref` identities;
2. paired semantic contracts;
3. producer and stored-instance compatibility;
4. fixtures, validator selection, and executable tests;
5. registries, workflow paths, generated bundles, and caches;
6. API, UI, runtime, map, data, release, and external consumers;
7. any correction or migration already applied to instances.

A Git revert restores bytes. It does not automatically restore consumer compatibility or reverse migrated data.

### Deprecation and retirement

Deprecate before deleting a version or compatibility path. A reviewed deprecation must declare:

- replacement identity and path;
- no-new-writes date;
- verified writers and readers;
- compatibility behavior and diagnostics;
- expiry and removal criteria;
- correction and rollback owner.

Retire only after proving that canonical writers have moved, required readers and references have closed or migrated, fixtures and tests cover the final boundary, registries and links are repaired, generated artifacts cannot reintroduce the path, and a reversible tombstone or deletion strategy exists.

[Back to top](#top)

---

<a id="open-verification-items"></a>

## Open Verification Items

| Item | Current disposition | Resolution evidence |
| --- | --- | --- |
| Acceptance of `schemas/contracts/v1/` as the narrower permanent canonical home | **PROPOSED** | Accepted ADR-0001 or superseding decision |
| Full coupling/readiness rules between semantic contracts and schemas | **PROPOSED / PARTIAL** | Accepted ADR-0002 or superseding controls plus executable evidence |
| Retirement safety for direct `schemas/contracts/policy/` | **NEEDS VERIFICATION** | Complete writer, reader, `$ref`, registry, link, workflow, and external-consumer inventory |
| Canonical `$id` namespace and major-version convention | **NEEDS VERIFICATION** | Accepted schema-identity standard and compatibility tests |
| Family-by-family contract, fixture, validator, and consumer coverage across v1 | **NOT ESTABLISHED by aggregate count** | Maintained object-family register plus executable coverage evidence |
| Generated versus hand-maintained version indexes | **PROPOSED** | Accepted manifest/generator design with single writer and drift checks |
| Independent schema, contract, validation, policy, and docs stewardship | **NEEDS VERIFICATION** | Accepted ownership assignments and enforced review rules |
| Required-check status of schema workflows | **NEEDS VERIFICATION** | Current repository ruleset evidence |
| Exact-head success for this revision | **NEEDS VERIFICATION until hosted runs finish** | GitHub Actions conclusions for the proposed commit |

These items are bounded holds, not permission to invent an answer, add a new root, weaken validation, or promote an object family.

[Back to top](#top)

---

<a id="review-checklist"></a>

## Review Checklist

- [ ] Base commit, prior target blob, current tree, and competing PR search are recorded.
- [ ] The direct-child map lists only `policy/` and `v1/`.
- [ ] The direct `policy/` lane remains documentation-only and routes new work to `v1/policy/`.
- [ ] `v1/` is described as the configured surface without accepting ADR-0001 by implication.
- [ ] Counts are pinned and labeled as topology rather than maturity or readiness.
- [ ] Machine shape, semantic contracts, policy, fixtures, tests, validators, data, and release authority remain separate.
- [ ] Schema dialect, `$id`, `$ref`, compatibility, and semantic-pairing impacts are reviewed where applicable.
- [ ] Valid and invalid fixtures cover material behavior changes.
- [ ] Commands are fail-closed and no-network by default.
- [ ] No secret, restricted instance, private endpoint, or sensitive real-world example is exposed.
- [ ] Links, anchors, metadata, Markdown, exact scope, and remote bytes are validated.
- [ ] Correction, rollback, deprecation, and retirement obligations are explicit.
- [ ] Any generated authoring receipt is either within authorized scope or its omission is explicit.
- [ ] The PR remains draft; no merge, release, deployment, activation, or publication occurs.

[Back to top](#top)

---

## No-Loss and Change Ledger

| v0.1 element | v0.2 disposition |
| --- | --- |
| Versioned contract-schema parent-index purpose | Preserved as the one-line purpose and bounded parent responsibility. |
| Draft and mixed-maturity posture | Preserved; refined with pinned topology and decision-status labels. |
| Schema-versus-contract boundary | Preserved and aligned with accepted ADR-0029 plus proposed ADR-0002 detail. |
| Version-router authority limits | Preserved and expanded across all adjacent responsibility roots. |
| Repository-fit tree | Corrected to show only direct children and include the previously omitted `policy/` compatibility lane. |
| `v1/` current-version route | Preserved as configured behavior without promoting proposed ADR-0001. |
| Future-version caution | Preserved and expanded into a dependency-closed migration record. |
| Belongs list | Preserved; compatibility indexes and possible manifests now require explicit single-authority controls. |
| Prohibited-content list | Preserved and expanded for sensitive material, parallel writes, generated outputs, and false authority claims. |
| Version-root governance | Preserved and separated from directory creation or schema copying. |
| Shape-to-meaning pairing | Preserved with a concrete pairing checklist and explicit non-effects. |
| Stable `$id` and `$ref` posture | Preserved and expanded into identity, dialect, and change-class rules. |
| Fixture and validator version awareness | Preserved with current fixture/test/validator responsibility routes. |
| No-parallel-authority rule | Preserved with single-writer, compatibility, migration, and retirement controls. |
| Provisional `python tools/validate_all.py \|\| true` | Removed; replaced by current fail-closed registry and Makefile entrypoints. |
| Stale singular contract-test path and permissive pytest command | Corrected to `tests/contracts` with fail-closed execution. |
| Promotion checklist | Preserved and broadened into authoring, change-planning, review, and final review checklists. |
| Ordinary README rollback | Preserved with exact prior blob and one-file rollback limits. |
| Version-root rollback concerns | Preserved and expanded to writers, readers, data migration, registries, generated outputs, and external consumers. |
| Generated-index question | Preserved as an open verification item with required governance controls. |
| Canonical `$id` question | Preserved as an open verification item. |
| v1 maturity question | Preserved as family-by-family evidence work, not answered by aggregate count. |
| Criteria for `v2/` | Preserved as a held decision with explicit prerequisites. |
| Maintainer focus on parent routing | Preserved through the direct-child-only map and delegation to `v1/README.md`. |
| Separation from data, policy, release, runtime, validators, fixtures, and public artifacts | Preserved and strengthened in routing, prohibition, trust, and storage sections. |

[Back to top](#top)

---

<a id="references"></a>

## References

### Governing and adjacent documentation

- [Schemas root contract](../README.md)
- [Direct policy compatibility lane](./policy/README.md)
- [v1 version-local index](./v1/README.md)
- [Semantic contracts root](../../contracts/README.md)
- [Policy root](../../policy/README.md)
- [Fixtures root](../../fixtures/README.md)
- [Tests root](../../tests/README.md)
- [Executable schema tests](../../tests/schemas/README.md)
- [Executable contract tests](../../tests/contracts/README.md)
- [Validator root](../../tools/validators/README.md)
- [Release root](../../release/README.md)
- [Root-registry projection](../../control_plane/root_registry.yaml)
- [CODEOWNERS](../../.github/CODEOWNERS)

### Decisions and doctrine

- [ADR-0001 — proposed schema home](../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md)
- [ADR-0002 — contracts versus schemas split](../../docs/adr/ADR-0002-contracts-vs-schemas-split.md)
- [ADR-0029 — accepted Directory Governance Standard v2](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md)
- [Adopted Directory Rules](../../docs/doctrine/directory-rules.md)

### Executable surfaces

- [Schema-validation workflow](../../.github/workflows/schema-validation.yml)
- [Validator-suite workflow](../../.github/workflows/validator-suite.yml)
- [Repository Makefile](../../Makefile)
- [Canonical validator entrypoint](../../tools/validate_all.py)
- [Validator orchestrator](../../tools/validators/validate_all.py)
- [Validator registry](../../tools/validators/validator_registry.json)
- [Compatibility aggregate runner](../../tools/validators/_common/run_all.py)

---

## Change Log

| Version | Date | Change |
| --- | --- | --- |
| `v0.2` | 2026-08-13 | Repository-grounded modernization: corrected the direct-child map, documented the unversioned policy compatibility lane, pinned the configured v1 topology and decision-status boundary, replaced permissive stale commands, and added responsibility routing, authoring, CI, migration, correction, rollback, deprecation, review, and no-loss guidance; changed documentation only. |
| `v0.1` | 2026-07-04 | Expanded the previously empty parent README with version routing, responsibility boundaries, v1 posture, authoring rules, provisional validation, promotion, rollback, and open questions. |

---

**Last reviewed:** 2026-08-13 against `main@0b0abda8f32ed93833bb5f51dbf1e24bf4460f25` · **Role:** version routing and compatibility boundary · **Shape:** `schemas/` · **Meaning:** `contracts/` · **Policy:** `policy/` · **Configured version:** `v1/` · **Publication:** none · **Path:** `schemas/contracts/README.md` · [Back to top](#top)
