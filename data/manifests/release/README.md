<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/data-manifests-release-readme
title: data/manifests/release/README.md — Release Manifest Compatibility and Retirement Lane
version: v0.2
type: readme; data-compatibility-segment; release-manifest-routing-guide; retirement-contract
status: repository-grounded draft; non-canonical; pointer-only; indexed-inventory-bounded; release-path-conflicted; release-readiness-held; non-authoritative
owners: NEEDS VERIFICATION — Release steward · Manifest steward · Data steward · Evidence steward · Proof steward · Catalog steward · Rights reviewer · Sensitivity reviewer · Security reviewer · Migration steward · Docs steward
created: NEEDS VERIFICATION — greenfield stub existed before v0.1 expansion
updated: 2026-07-24
supersedes: v0.1 documentation at the same path; no manifest, candidate, decision, payload, release, runtime, deployment, or publication state is superseded
prepared_under_prompt: KFM Markdown Modernization & GitHub Documentation Implementation Agent v4.0.0
policy_label: repository-facing; data; manifests; release; compatibility; pointer-only; deny-new-writes; no-direct-public-path; correction-aware; rollback-aware
current_path: data/manifests/release/README.md
owning_root: data/
truth_posture: >
  CONFIRMED the tracked README and stable identity, non-canonical data/manifests parent,
  canonical lifecycle root, release responsibility root, draft singular and plural release-manifest
  collection READMEs, absence of release/manifests/release/README.md, ReleaseManifest contract and
  permissive id-only schema, ADR-0011 separation posture, proposed ADR-0018 gate sequence, current
  release-dry-run readiness holds, current promotion-gate readiness holds, and default CODEOWNERS
  routing / PROPOSED retain-as-pointer, migrate-and-tombstone, or retire outcome; object-family
  routing; minimum migration packet; consumer cutover; stale-reference detection; and recovery
  procedure / CONFLICTED singular release/manifest versus plural release/manifests convention and
  topic-level data/manifests/release versus responsibility-rooted release governance / UNKNOWN
  exhaustive recursive subtree, Git history consumers, Git LFS or external stores, actual accepted
  ReleaseManifest instances, active release service, signer, deployment, CDN state, branch rules,
  reviewer independence, and public effects / NEEDS VERIFICATION accountable stewards, accepted
  manifest collection path, hardened ReleaseManifest schema, fixtures and validator, policy runtime,
  evidence closure, signing, candidate assembly, review enforcement, migration execution,
  deprecation entry, consumer cutover, cache invalidation, and rollback drill
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: c2ea87522cfaa2944076fcba4398e1471d685d2b
  prior_blob: 6bf84d2616022fce28a8a0e6fa3e5b827d3fe800
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  data_root_readme_blob: fb7b0acfaea25b630a3042f24cb97558a996d05a
  data_manifests_parent_blob: c4cdbf0c0038f737447a7dc173f0fe49ef62490e
  release_root_readme_blob: 0752610b1df6d11143158f6f162f65ecd650e6a6
  release_manifest_singular_readme_blob: 6014cfc0f8394a44167f4226975b74f94f3b2a03
  release_manifests_plural_readme_blob: c699a527ff11bebad6a874ed1a37aa3a8213b86c
  release_manifest_contract_blob: 9ca1c9d4a5b247196aa84a31a158fe734c8a6720
  release_dry_run_workflow_blob: 9baf5b92f954c994ab11e8bb54d480e6309a0579
  promotion_gate_adr_blob: 6cde5af9a7c8ef03df3fb22816074c900df659b7
  adr_0011_blob: 40b0f47b87d584040803ed76aa6b31f5204b7fca
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  checked_absent_paths:
    - release/manifests/release/README.md
  exact_path_search_results: "this README only"
  open_overlapping_pull_requests_found: "0"
  inventory_method: exact GitHub file reads, bounded indexed search, workflow and ADR inspection, and open-PR overlap search; no recursive Git tree, Git history walk, Git LFS inventory, object store, database, signer, deployment, CDN, branch ruleset, or production environment was inspected
related:
  - ../README.md
  - ../../README.md
  - ../../published/README.md
  - ../../catalog/README.md
  - ../../proofs/README.md
  - ../../receipts/README.md
  - ../../registry/README.md
  - ../../rollback/README.md
  - ../../../release/README.md
  - ../../../release/manifest/README.md
  - ../../../release/manifests/README.md
  - ../../../release/candidates/README.md
  - ../../../release/rollback_cards/README.md
  - ../../../contracts/release/release_manifest.md
  - ../../../schemas/contracts/v1/release/release_manifest.schema.json
  - ../../../policy/release/README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/doctrine/lifecycle-law.md
  - ../../../docs/doctrine/trust-membrane.md
  - ../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../docs/adr/ADR-0018-promotion-gate-sequence.md
  - ../../../migrations/data/README.md
  - ../../../.github/workflows/release-dry-run.yml
  - ../../../.github/workflows/promotion-gate.yml
  - ../../../.github/CODEOWNERS
tags: [kfm, data, manifests, release, compatibility, release-manifest, promotion, correction, withdrawal, rollback, migration, trust-membrane]
notes:
  - "v0.2 is a same-path, no-loss modernization of the existing Release compatibility README."
  - "The first twelve H2 sections follow Directory Rules section 15 exactly."
  - "No ReleaseManifest instance, candidate packet, decision, payload, schema, validator, policy result, release, redirect, migration, deployment, or publication state is created."
  - "New trust-bearing writes under data/manifests/release/ are denied pending accepted placement, schema, review, consumer, migration, and rollback decisions."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/manifests/release/` — Release Manifest Compatibility and Retirement Lane

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#status)
[![Authority: compatibility only](https://img.shields.io/badge/authority-compatibility%20only-b42318?style=flat-square)](#authority-level)
[![Release collection: conflicted](https://img.shields.io/badge/release%20collection-CONFLICTED-b42318?style=flat-square)](#release-manifest-path-conflict)
[![Release readiness: held](https://img.shields.io/badge/release%20readiness-WORKFLOW__HOLD-b42318?style=flat-square)](#current-release-readiness)
[![New writes: denied](https://img.shields.io/badge/new%20trust%20writes-denied-b42318?style=flat-square)](#what-does-not-belong-here)
[![Public path: denied](https://img.shields.io/badge/public%20path-denied-b42318?style=flat-square)](#outputs)

> **One-line purpose.** Preserve a frozen, reversible compatibility pointer while routing release manifests, promotion decisions, rollback cards, correction and withdrawal records, receipts, proofs, catalogs, and published artifacts to the responsibility root that owns each object.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed) · [Inventory](#current-bounded-inventory) · [Families](#release-object-family-separation) · [Path conflict](#release-manifest-path-conflict) · [Readiness](#current-release-readiness) · [Gates](#release-and-promotion-gates) · [Closure](#minimum-release-manifest-closure) · [Routing](#release-object-routing) · [Migration](#retain-migrate-or-retire) · [Cutover](#consumer-cutover-and-stale-reference-control) · [Recovery](#correction-deprecation-and-rollback) · [Verification](#open-verification-register)

> [!IMPORTANT]
> **This path is not release authority.** A file named `manifest`, a valid JSON object, a green workflow, a pull request, a merge, a signature-shaped file, or bytes under a familiar path do not create a KFM release.

> [!CAUTION]
> **The release-manifest collection path is unresolved.** Both [`release/manifest/`](../../../release/manifest/README.md) and [`release/manifests/`](../../../release/manifests/README.md) are documented as draft. This README must not silently choose one, create a third editable authority, or migrate records by naming preference.

> [!WARNING]
> **Current release automation is intentionally held.** The release-dry-run workflow confirms that no candidate packet, accepted dry-run command, `ReleaseManifest` fixture set, or declared validator exists. The promotion sequence remains proposed and readiness-oriented. No current green hold proves release, signing, rollback, or publication.

---

<a id="purpose"></a>

## Purpose

`data/manifests/release/` is a **compatibility and retirement lane** beneath the non-canonical [`data/manifests/`](../README.md) segment.

It exists to answer a narrow governance question:

> Which historical or proposed references used `data/manifests/release/`, what object family did each reference actually represent, where is its responsibility-aligned home, and what evidence is required before this compatibility path can be retained, migrated, tombstoned, or retired?

This lane may document the answer. It must not:

- assemble a release;
- approve promotion;
- write a `ReleaseManifest`;
- sign or attest a release;
- store release payloads;
- close evidence or proof;
- publish a public artifact;
- switch a `current` or `latest` alias;
- invalidate caches;
- execute rollback;
- become a public API, UI, map, download, or AI source.

The canonical lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Promotion is a governed state transition. Directory placement, copying, renaming, merging, or deploying bytes is not that transition.

[Back to top](#top)

---

<a id="authority-level"></a>

## Authority level

**Compatibility pointer only; non-canonical, non-executable, non-public, and subordinate to release governance and every referenced authority family.**

| Question | Owning authority | Role of this lane |
|---|---|---|
| What a `ReleaseManifest` means | [`contracts/release/release_manifest.md`](../../../contracts/release/release_manifest.md) | Link only; do not redefine semantics. |
| What machine shape is valid | [`schemas/contracts/v1/release/release_manifest.schema.json`](../../../schemas/contracts/v1/release/release_manifest.schema.json) | Report current maturity and conflicts; do not store schemas. |
| Whether release is allowed | [`policy/release/`](../../../policy/release/README.md), promotion/release decisions, and accountable review | Never infer or grant permission. |
| Where release records belong | [`release/`](../../../release/README.md) and an accepted manifest collection path | Preserve the unresolved path decision. |
| Which candidate is under review | [`release/candidates/`](../../../release/candidates/README.md) | Point to candidate dossiers; do not duplicate them. |
| What a process executed | [`data/receipts/`](../../receipts/README.md) | Reference receipts; never treat them as approval. |
| Why claims or artifacts are supportable | [`data/proofs/`](../../proofs/README.md) and resolvable EvidenceBundles | Reference proof support; never become proof. |
| How release contents are discovered | [`data/catalog/`](../../catalog/README.md) and triplet/catalog projections | Reference catalog closure; do not duplicate catalogs. |
| Which bytes are public-safe carriers | [`data/published/`](../../published/README.md) after release | Never store or serve payload bytes here. |
| How migration mechanics are governed | [`migrations/data/`](../../../migrations/data/README.md) | Link to reviewed migration packets. |
| How GitHub review is routed | [`.github/CODEOWNERS`](../../../.github/CODEOWNERS) | Routing only; not stewardship or approval proof. |

### Authority anti-collapse rule

The following identities must stay distinct:

```text
ReleaseManifest
!= PromotionDecision
!= PolicyDecision
!= ReviewRecord
!= Receipt
!= Proof
!= Catalog record
!= Published artifact
!= RollbackCard
!= CorrectionNotice
!= WithdrawalNotice
```

Cross-references are required where material. Substitution is prohibited.

[Back to top](#top)

---

<a id="status"></a>

## Status

| Surface | Current evidence | Truth status | Safe conclusion |
|---|---|---:|---|
| This README | Existing same-path document with stable ID | **CONFIRMED** | Compatibility documentation only |
| Parent `data/manifests/` | Documented non-canonical compatibility root | **CONFIRMED** | Must not gain independent trust authority |
| Exact indexed path inventory | This README only | **CONFIRMED BOUNDED** | Recursive and historical inventories remain open |
| `release/manifests/release/README.md` | Exact read returned not found | **CONFIRMED ABSENT at inspection** | Do not invent a release-named child collection |
| Singular release collection | `release/manifest/README.md` present and draft | **CONFIRMED DRAFT** | Not selected as canonical |
| Plural release collection | `release/manifests/README.md` present and draft | **CONFIRMED DRAFT** | Not selected as canonical |
| `ReleaseManifest` semantic contract | Present | **CONFIRMED DRAFT / PROPOSED** | Defines target meaning, not accepted operational release |
| `ReleaseManifest` schema | Permissive, `id`-only required | **CONFIRMED THIN / PROPOSED** | Shape validity cannot establish governance closure |
| Manifest fixtures | Release-dry-run asserts fixture directory absent | **CONFIRMED HOLD CONDITION** | No accepted fixture corpus established |
| Manifest validator | Release-dry-run asserts declared validator absent | **CONFIRMED HOLD CONDITION** | No accepted validator established |
| Candidate assembly | No candidate payload; helper and Make target are placeholders | **CONFIRMED HELD** | No release candidate assembled |
| Promotion sequence | ADR-0018 proposed; workflow readiness/shape checks only | **CONFIRMED PROPOSED / HELD** | No accepted gate runtime |
| Signing and attestations | Not inspected as operational service | **UNKNOWN** | No signing capability claim |
| Public deployment | Not inspected | **UNKNOWN** | No public effect claim |
| Retain, migrate, or retire decision | No accepted decision found | **OPEN / NEEDS VERIFICATION** | Freeze writes and preserve reversibility |

### Safe current action

1. Deny new trust-bearing writes to this path.
2. Retain this README as a warning and crosswalk.
3. Inventory the subtree and consumers recursively.
4. Resolve the singular/plural release-manifest collection through reviewed governance.
5. Harden `ReleaseManifest` semantics, schema, fixtures, validator, policy, and review controls.
6. Migrate or retire only through a bounded, reversible packet.

[Back to top](#top)

---

<a id="what-belongs-here"></a>

## What belongs here

Accepted contents are intentionally narrow:

- this README;
- a frozen compatibility index that maps legacy paths or identifiers to reviewed canonical targets;
- bounded inventory notes stating what was inspected and what remains unknown;
- migration IDs and links to reviewed migration packets under `migrations/data/`;
- deprecation, supersession, correction, withdrawal, and rollback references;
- consumer-cutover records that identify repositories, jobs, scripts, APIs, CDNs, caches, documentation, and external integrations moved away from this path;
- immutable tombstone metadata after a successful migration;
- non-sensitive explanation of why the path is frozen, redirected, or retired.

### Compatibility record requirements

Any compatibility record retained here should contain:

| Field | Requirement |
|---|---|
| `legacy_path` | Exact prior path or identifier |
| `object_family` | ReleaseManifest, decision, receipt, proof, catalog, payload, or another explicit family |
| `canonical_target` | Accepted responsibility-aligned path or stable identifier |
| `status` | `FROZEN`, `MIGRATING`, `TOMBSTONED`, or `RETIRED` |
| `migration_ref` | Required when content moved |
| `deprecation_ref` | Required when consumers must stop using the legacy path |
| `correction_or_withdrawal_ref` | Required when public or release meaning changed |
| `rollback_ref` | Required for reversible cutover |
| `verified_at` | ISO date/time of verification |
| `verified_by` | Accountable human or governed service identity |
| `limitations` | Inventory, consumer, runtime, or external-system limits |

Such a record is a pointer. It is not a release object.

[Back to top](#top)

---

<a id="what-does-not-belong-here"></a>

## What does NOT belong here

| Prohibited material | Correct authority home |
|---|---|
| `ReleaseManifest` instances | Accepted collection under [`release/`](../../../release/README.md) after path resolution |
| Promotion decisions | Release promotion-decision lane under `release/` |
| Policy decisions or Rego bundles | `policy/` and decision-record homes |
| Candidate dossiers | [`release/candidates/`](../../../release/candidates/README.md) |
| Rollback cards | [`release/rollback_cards/`](../../../release/rollback_cards/README.md) |
| Correction or withdrawal notices | Appropriate release/correction governance lane |
| Signatures, DSSE envelopes, attestations, transparency proofs | Accepted signing/release provenance lanes |
| Release receipts or validation receipts | [`data/receipts/`](../../receipts/README.md) |
| EvidenceBundles, ProofPacks, integrity or citation proof | [`data/proofs/`](../../proofs/README.md) |
| STAC, DCAT, PROV, domain catalogs, graph/triplet records | [`data/catalog/`](../../catalog/README.md) and accepted triplet lanes |
| Source, dataset, rights, sensitivity, or layer registry records | [`data/registry/`](../../registry/README.md) |
| RAW, WORK, QUARANTINE, PROCESSED, or PUBLISHED payloads | Their lifecycle lanes |
| Public files, downloads, tiles, reports, stories, APIs | [`data/published/`](../../published/README.md) after release |
| Contracts or schemas | `contracts/` and `schemas/` |
| Policy rules | `policy/` |
| Validators, fixtures, tests, pipelines, packages, workflows | Their implementation roots |
| Credentials, keys, tokens, certificates, signing secrets | Approved external secret stores |
| Direct public routes, redirects, or aliases | Governed API/static-delivery and release infrastructure |
| AI summaries framed as release truth | Governed AI surfaces resolving released evidence |

### Forbidden naming shortcuts

A file must not be admitted here merely because its name contains:

- `release`;
- `manifest`;
- `approved`;
- `signed`;
- `final`;
- `public`;
- `production`;
- `latest`;
- `current`;
- `rollback`;
- `proof`.

Names are metadata. Authority comes from accepted object meaning, shape, evidence, policy, review, release state, and verification.

[Back to top](#top)

---

<a id="inputs"></a>

## Inputs

This lane may consume **governance metadata and references only**:

- exact recursive tree and Git-history inventories;
- Git LFS and external artifact-store inventories;
- code, workflow, configuration, documentation, API, deployment, CDN, and cache consumer searches;
- object-family classification for each discovered file;
- current path and stable identifier maps;
- content digests and canonicalization profiles;
- source, evidence, rights, sensitivity, policy, review, candidate, promotion, release, correction, withdrawal, and rollback references;
- accepted architecture decisions;
- migration and deprecation records;
- dry-run and rollback-drill results;
- stale-reference and cache-invalidation reports.

### Input trust requirements

Inputs must be:

- attributable;
- bounded in scope;
- dated;
- digestable where practical;
- explicit about omissions;
- free of secrets and restricted payloads;
- reviewed at a burden appropriate to their release significance.

Search absence is bounded evidence. It is not proof of global absence.

[Back to top](#top)

---

<a id="outputs"></a>

## Outputs

This lane may emit only:

- a compatibility posture;
- a bounded inventory summary;
- an object-family routing matrix;
- a legacy-to-canonical path crosswalk;
- a retain, migrate, tombstone, or retire recommendation;
- links to migration, deprecation, correction, withdrawal, cutover, and rollback records;
- a list of unresolved verification items;
- a final retirement receipt reference after all gates close.

It must not emit:

- a release decision;
- a manifest instance;
- a signed attestation;
- a candidate;
- a proof;
- a catalog record;
- a published artifact;
- a public alias;
- a deployment;
- a runtime response;
- an AI answer.

### Public-path posture

Direct reads from `data/manifests/release/` are denied for public clients, ordinary UI, public APIs, static hosting, model context, search indexes, or release resolution.

A public consumer may use only:

1. a governed API response, or
2. a release-resolved, digest-bound public-safe artifact served through an approved static edge.

[Back to top](#top)

---

<a id="validation"></a>

## Validation

### README validation

The README must preserve:

- one H1;
- the required first twelve H2 sections in exact order;
- stable `doc_id`;
- valid anchors and relative links;
- explicit authority boundaries;
- truth labels;
- a no-loss ledger;
- rollback to the prior blob.

### Compatibility-lane validation

Before any status stronger than `FROZEN`:

- recursively inventory the tracked subtree;
- inspect Git history for moved or deleted release-shaped files;
- inspect Git LFS pointers and external object stores;
- search repository consumers;
- inspect CI workflows, release tooling, deployment configs, CDN mappings, caches, public URLs, and external integrations;
- classify every item by object family;
- verify rights and sensitivity;
- verify stable identity and digests;
- verify accepted target homes;
- verify migration and rollback plans.

### ReleaseManifest maturity validation

Current schema validity proves only the current machine shape. A production-grade release-manifest capability additionally needs:

- accepted semantic contract;
- accepted schema home and version;
- non-vacuous valid and invalid fixtures;
- executable validator;
- deterministic identity and canonicalization;
- artifact and digest closure;
- EvidenceRef resolution;
- rights and sensitivity closure;
- policy decisions;
- promotion decision;
- accountable review;
- separation of duties where required;
- signatures or attestations where required;
- correction, withdrawal, supersession, and rollback;
- public-client and static-edge enforcement;
- reproducible dry-run and rollback-drill evidence.

### Failure posture

Unresolved validation produces one of:

- `HOLD`;
- `QUARANTINE`;
- `RESTRICT`;
- `ABSTAIN`;
- `DENY`;
- `ERROR`.

It never produces implied release.

[Back to top](#top)

---

<a id="review-burden"></a>

## Review burden

| Change | Minimum review burden |
|---|---|
| Typo, dead link, or wording clarification | Documentation and data-lane review |
| Compatibility crosswalk update | Data, release, and migration review |
| Discovery of a manifest-shaped file | Release, contracts, schemas, evidence, policy, security, and affected-domain review |
| Change to manifest object meaning or shape | Contracts/schema review and versioning decision |
| Selection of singular or plural manifest collection | Architecture/release decision with migration and compatibility plan |
| Candidate or promotion behavior | Release, policy, evidence, review, rollback, and CI review |
| Signing or attestation behavior | Security, supply-chain, release, and key-management review |
| Public path, alias, CDN, cache, or API change | Release, security, infrastructure, governed-API, and rollback review |
| Retirement of this lane | Recursive inventory, consumer cutover, stale-reference proof, deprecation, correction review, and rollback drill |

CODEOWNERS routes review to `@bartytime4life`. It does not prove:

- accountable stewardship;
- independent approval;
- branch protection;
- ruleset enforcement;
- review completion;
- release authorization;
- separation of duties.

[Back to top](#top)

---

<a id="related-folders"></a>

## Related folders

### Lifecycle and trust artifacts

- [`data/`](../../README.md)
- [`data/published/`](../../published/README.md)
- [`data/catalog/`](../../catalog/README.md)
- [`data/proofs/`](../../proofs/README.md)
- [`data/receipts/`](../../receipts/README.md)
- [`data/registry/`](../../registry/README.md)
- [`data/rollback/`](../../rollback/README.md)

### Release governance

- [`release/`](../../../release/README.md)
- [`release/manifest/`](../../../release/manifest/README.md)
- [`release/manifests/`](../../../release/manifests/README.md)
- [`release/candidates/`](../../../release/candidates/README.md)
- [`release/rollback_cards/`](../../../release/rollback_cards/README.md)

### Meaning, shape, policy, and change control

- [`ReleaseManifest` contract](../../../contracts/release/release_manifest.md)
- [`ReleaseManifest` schema](../../../schemas/contracts/v1/release/release_manifest.schema.json)
- [`policy/release/`](../../../policy/release/README.md)
- [`migrations/data/`](../../../migrations/data/README.md)

### Doctrine and automation

- [`Directory Rules`](../../../docs/doctrine/directory-rules.md)
- [`Lifecycle Law`](../../../docs/doctrine/lifecycle-law.md)
- [`Trust Membrane`](../../../docs/doctrine/trust-membrane.md)
- [`release-dry-run`](../../../.github/workflows/release-dry-run.yml)
- [`promotion-gate`](../../../.github/workflows/promotion-gate.yml)

[Back to top](#top)

---

<a id="adrs"></a>

## ADRs

### ADR-0011 — artifact-family separation

[`ADR-0011`](../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md) proposes and documents separation among receipts, proofs, catalogs, release manifests/decisions, and published artifacts.

Current safe use:

- preserve separation;
- do not infer acceptance or complete enforcement;
- do not use `data/manifests/release/` as a mixed trust bucket.

### ADR-0018 — promotion gate sequence

[`ADR-0018`](../../../docs/adr/ADR-0018-promotion-gate-sequence.md) remains proposed. Current repository evidence establishes shape checks and readiness holds, not an accepted gate runtime.

Current safe use:

- keep promotion evaluation distinct from `ReleaseManifest`;
- keep policy decisions, gate results, review records, receipts, proofs, manifests, and publication authority distinct;
- do not treat a schema-valid `APPROVE` as operational approval.

### Decision still required

A reviewed decision must settle:

1. `release/manifest/`, `release/manifests/`, or a defined split;
2. manifest instance naming and identity;
3. canonicalization and digest profile;
4. accepted schema version;
5. fixture and validator obligations;
6. candidate-to-manifest assembly;
7. review and separation-of-duties requirements;
8. signing/attestation requirements;
9. correction, withdrawal, and rollback semantics;
10. compatibility and retirement of `data/manifests/**`.

This README does not make that decision.

[Back to top](#top)

---

<a id="last-reviewed"></a>

## Last reviewed

| Field | Value |
|---|---|
| Date | `2026-07-24` |
| Repository snapshot | `main@c2ea87522cfaa2944076fcba4398e1471d685d2b` |
| Target prior blob | `6bf84d2616022fce28a8a0e6fa3e5b827d3fe800` |
| Review class | Same-path documentation modernization |
| Re-review trigger | Manifest collection decision, schema hardening, fixture or validator appearance, first candidate packet, first accepted manifest, signing integration, public release, migration, deprecation, correction, withdrawal, rollback drill, or six months elapsed |

[Back to top](#top)

---

<a id="current-bounded-inventory"></a>

## Current bounded inventory

| Surface | Observed state | Limit |
|---|---|---|
| `data/manifests/release/README.md` | Present | Documentation only |
| Other exact indexed files under `data/manifests/release/` | None surfaced | Not a recursive tree or history proof |
| `release/manifests/release/README.md` | Absent at inspection | Does not prove no differently named manifest collection exists |
| `release/manifest/README.md` | Present, draft | Canonical status unresolved |
| `release/manifests/README.md` | Present, draft | Canonical status unresolved |
| Candidate payloads | Workflow asserts none under `release/candidates/` beyond guidance/placeholders | Workflow snapshot only |
| Release dry-run implementation | Comment-only helper and TODO Make target | No accepted dry-run command |
| `ReleaseManifest` fixtures | Workflow asserts configured fixture root absent | No accepted fixture corpus |
| Declared manifest validator | Workflow asserts configured validator absent | No accepted validator |
| PromotionDecision fixtures | Non-empty shape fixtures exist | Shape test is not promotion |
| Rollback-card records | Two proposed placeholder records are inspected by workflow | Not operational rollback proof |
| Signing and transparency | Not operationally inspected | UNKNOWN |
| Deployment and public artifacts | Not inspected | UNKNOWN |

### Inventory consequence

The path is eligible only for a **freeze**, not automatic retirement. Retirement requires broader evidence than indexed search.

[Back to top](#top)

---

<a id="release-object-family-separation"></a>

## Release object family separation

| Object family | Core question | Correct home | Does it release? |
|---|---|---|---:|
| Candidate dossier | What is proposed for review? | `release/candidates/` | No |
| Validation receipt | What check ran and with what result? | `data/receipts/` | No |
| EvidenceBundle / proof | What supports the claims and integrity? | `data/proofs/` | No |
| Catalog record | How is the dataset/artifact described and discovered? | `data/catalog/` | No |
| PolicyDecision | Is a bounded operation admissible? | Policy/decision record home | No by itself |
| PromotionDecision | Is a governed transition approved, denied, or abstained? | Release promotion-decision home | No by itself |
| ReviewRecord | Who reviewed what scope and when? | Review-governance home | No by itself |
| ReleaseManifest | Which approved artifact set and support refs define the release? | Accepted release manifest collection | Binds release; does not replace approval |
| Signature/attestation | Which digest-bound statement was signed? | Accepted signing/release provenance lane | No by itself |
| Published artifact | Which public-safe bytes may consumers use? | `data/published/` | Downstream carrier |
| CorrectionNotice | What public meaning is corrected? | Release/correction lane | Changes public lineage |
| WithdrawalNotice | What is withdrawn and why? | Release/withdrawal lane | Changes availability |
| RollbackCard | How can a release or alias be reversed safely? | `release/rollback_cards/` | Enables recovery |

### Assembly rule

A mature release assembles references across these families. It does not collapse them into one generic manifest.

[Back to top](#top)

---

<a id="release-manifest-path-conflict"></a>

## Release manifest path conflict

The repository currently documents:

```text
release/manifest/
release/manifests/
```

Both are draft. No accepted evidence inspected here chooses one.

### Allowed resolution patterns

| Pattern | Description | Requirements |
|---|---|---|
| Singular canonical | All manifest instances or current manifest workflow under `release/manifest/` | Accepted decision, migration, redirects/tombstones, consumer cutover, rollback |
| Plural canonical | Collection and instances under `release/manifests/` | Accepted decision, migration, redirects/tombstones, consumer cutover, rollback |
| Defined split | Singular for a stable current pointer or workflow, plural for immutable instances | Explicit object semantics, write rules, schema rules, tests, and no editable duplication |
| New successor | A different release collection chosen by ADR | Directory Rules update, full migration, compatibility period, rollback |
| Editable duplication | Both paths independently store mutable manifest authority | **DENY** |

### No implicit selection

The following do not select a canonical path:

- more files in one directory;
- a newer README;
- a passing link checker;
- a generated example;
- a branch or pull request;
- user familiarity;
- singular/plural grammar preference.

[Back to top](#top)

---

<a id="current-release-readiness"></a>

## Current release readiness

The current [`release-dry-run`](../../../.github/workflows/release-dry-run.yml) workflow is a **read-only readiness and drift-hold workflow**.

It confirms a bounded set of current facts:

- candidate lanes contain guidance/placeholders and no candidate packet payload;
- `tools/release/release_dry_run.py` remains a comment-only placeholder;
- the `Makefile` target remains TODO-only;
- the `ReleaseManifest` schema remains proposed and permissive;
- the configured manifest fixture root does not exist;
- the configured manifest validator does not exist;
- PromotionDecision fixtures can exercise shape validation;
- rollback-card tooling and records remain placeholder/proposed surfaces;
- no manifest, release, signature, deployment, or public artifact is emitted.

### Readiness labels

| Label | Meaning |
|---|---|
| `CONFIRMED` | The inspected repository surface has the stated bounded property |
| `HELD` | Workflow deliberately blocks graduation while preserving drift detection |
| `PROPOSED` | Contract, schema, ADR, or implementation direction is not accepted |
| `NEEDS VERIFICATION` | A concrete check remains |
| `UNKNOWN` | Inspected evidence cannot resolve the state |
| `CONFLICTED` | Current repository surfaces disagree |

### Green hold interpretation

A green readiness workflow means:

> The expected hold conditions were observed.

It does not mean:

> The release system is ready.

[Back to top](#top)

---

<a id="release-and-promotion-gates"></a>

## Release and promotion gates

A governed release sequence should preserve at least these distinct closures:

```mermaid
flowchart LR
  C["Candidate identity<br/>and immutable refs"]
  E["Evidence + proof<br/>closure"]
  R["Rights + sensitivity<br/>closure"]
  P["Policy decisions"]
  V["Validation +<br/>integrity checks"]
  H["Accountable review<br/>and duty separation"]
  D["PromotionDecision"]
  M["ReleaseManifest<br/>artifact binding"]
  S["Signature / attestation<br/>when required"]
  U["Published public-safe<br/>artifacts"]
  B["Correction + withdrawal<br/>+ rollback support"]

  C --> E --> R --> P --> V --> H --> D --> M --> S --> U --> B
```

The diagram is a governance model, not proof that the repository executes the full sequence.

### Gate anti-substitution

| Present item | Missing item it cannot replace |
|---|---|
| Candidate README | Candidate dossier |
| Schema-valid manifest | Evidence, policy, review, approval, signing |
| PromotionDecision fixture | Executed promotion decision |
| ReleaseManifest | PromotionDecision |
| Receipt | Proof or approval |
| ProofPack | Release decision |
| Signature file | Key governance or release approval |
| Published bytes | ReleaseManifest and public-safe decision |
| Green workflow | Runtime execution and public effect |
| Merge commit | Promotion or publication |

[Back to top](#top)

---

<a id="minimum-release-manifest-closure"></a>

## Minimum release manifest closure

The current schema requires only `id`. That is insufficient for production governance.

A mature `ReleaseManifest` should bind or resolve:

### Identity and immutability

- stable manifest ID;
- release ID and version;
- canonicalization profile;
- manifest digest;
- creation, decision, publication, effective, supersession, and withdrawal times;
- immutable prior/successor references.

### Contents and integrity

- every included artifact by stable ref;
- artifact digests;
- catalog/triplet refs;
- build and spec hashes;
- environment or producer identity where material;
- no embedded restricted payloads.

### Evidence and source posture

- resolvable EvidenceRefs;
- EvidenceBundle refs for consequential claims;
- source descriptors and source roles;
- citation and attribution;
- validity and freshness caveats.

### Rights, sensitivity, and policy

- rights and license refs;
- sensitivity and access classification;
- redaction/generalization refs;
- policy decisions and obligations;
- audience and precision limits;
- embargo or restricted-access state.

### Validation and review

- validation receipts and reports;
- review records;
- reviewer scope;
- separation-of-duties state where required;
- unresolved warnings and explicit finite disposition.

### Promotion, publication, and recovery

- candidate ref;
- promotion decision ref;
- release-facing effect;
- published artifact refs;
- governed client posture;
- correction and withdrawal refs;
- rollback card and rollback target;
- cache/CDN invalidation requirements;
- successor or null-release state.

Missing required closure must fail closed.

[Back to top](#top)

---

<a id="release-object-routing"></a>

## Release object routing

| Discovered item | Route |
|---|---|
| Actual `ReleaseManifest` | Hold until collection path resolved; then migrate to accepted `release/` collection |
| Candidate dossier | `release/candidates/` |
| PromotionDecision | Accepted release promotion-decision lane |
| PolicyDecision | Accepted policy decision record lane |
| ReviewRecord | Accepted release-review lane |
| RollbackCard | `release/rollback_cards/` |
| CorrectionNotice | Release/correction lane |
| WithdrawalNotice | Release/withdrawal lane |
| Signature or attestation | Accepted signing/provenance lane |
| Run or validation receipt | `data/receipts/` |
| EvidenceBundle or proof | `data/proofs/` |
| Catalog record | `data/catalog/` |
| Source/dataset/layer registry record | `data/registry/` |
| Published payload | `data/published/` if release-approved; otherwise hold/quarantine |
| Contract or schema | `contracts/` or `schemas/` |
| Policy rule | `policy/` |
| Executable implementation | Tools, packages, pipelines, workflows, apps, or infrastructure root by responsibility |
| Secret or signing key | External approved secret store; incident handling if committed |
| Unknown object family | Freeze and quarantine classification; do not move by extension |

### Classification before movement

Do not move an item until its:

- object family;
- stable identity;
- current consumers;
- rights/sensitivity posture;
- digest;
- target authority;
- correction implications;
- rollback route

are documented.

[Back to top](#top)

---

<a id="retain-migrate-or-retire"></a>

## Retain, migrate, or retire

### Strategy A — retain as frozen pointer

Use when:

- historical links remain;
- external consumers are not fully inventoried;
- the release collection decision is open;
- no trust-bearing payload remains here.

Requirements:

- deny writes;
- retain README and crosswalk only;
- add deprecation posture;
- monitor stale references;
- re-review on release architecture changes.

### Strategy B — migrate and tombstone

Use when:

- trust-bearing files are discovered;
- accepted target homes exist;
- consumers can be cut over.

Requirements:

1. inventory;
2. classify;
3. digest;
4. choose accepted targets;
5. create migration packet;
6. dry-run;
7. copy or move without changing meaning;
8. validate target instances;
9. update consumers;
10. invalidate caches;
11. add tombstone;
12. run rollback drill;
13. observe a compatibility window.

### Strategy C — retire

Use only when:

- recursive and historical inventories are complete enough;
- no active internal or external consumer remains;
- all records are migrated or intentionally withdrawn;
- stale-reference checks pass;
- correction/deprecation obligations close;
- rollback drill passes;
- accountable reviewers approve retirement.

### Strategy D — make canonical

**Not recommended.** It bends the responsibility-root rule and creates a parallel release root under `data/`.

It requires:

- accepted ADR;
- Directory Rules update;
- migration and compatibility plan;
- explicit reason why `release/` no longer owns the records;
- contracts, schemas, tests, workflows, public-client boundaries, correction, and rollback changes.

### Strategy E — editable duplicate

**DENY.**

[Back to top](#top)

---

<a id="minimum-migration-packet"></a>

## Minimum migration packet

A migration packet should record:

```yaml
migration_id: <stable-id>
status: PROPOSED
source_path: data/manifests/release/
source_snapshot:
  git_commit: <sha>
  inventory_digest: <digest>
target_decision_ref: <accepted-adr-or-path-decision>
object_mappings:
  - legacy_path: <path>
    object_family: <family>
    stable_id: <id>
    content_digest: <digest>
    target_path: <path>
    transformation: none | canonicalization-only | reviewed-transform
consumer_inventory_ref: <ref>
rights_review_ref: <ref-or-na>
sensitivity_review_ref: <ref-or-na>
validation_plan_ref: <ref>
cutover_plan_ref: <ref>
deprecation_ref: <ref>
correction_or_withdrawal_refs: []
cache_invalidation_plan_ref: <ref>
rollback_plan_ref: <ref>
review_record_refs: []
```

### Migration invariants

- preserve stable IDs;
- preserve history and digests;
- do not rewrite meaning silently;
- do not upgrade draft/proposed records to accepted;
- do not change release state during relocation;
- do not expose restricted material;
- do not remove the legacy path before cutover verification;
- preserve correction, withdrawal, and rollback lineage.

[Back to top](#top)

---

<a id="consumer-cutover-and-stale-reference-control"></a>

## Consumer cutover and stale-reference control

Search and verify:

- repository code and tests;
- workflows and actions;
- Make targets and scripts;
- contracts, schemas, policy, fixtures, and docs;
- governed API resolvers;
- public UI and MapLibre configuration;
- release tooling and signing jobs;
- deployment manifests;
- object-store keys;
- CDN routes and redirects;
- cache keys;
- dashboards and alert rules;
- external documentation and integrations;
- retained branches and tags where operationally material.

### Cutover phases

| Phase | Required result |
|---|---|
| Inventory | Every known consumer has owner, path, and criticality |
| Dual-read compatibility | Only if justified; canonical writes remain single-home |
| Validation | Old and new refs resolve to digest-equivalent intended records |
| Switch | Consumers use accepted target |
| Observe | Logs and stale-reference monitors remain clean |
| Tombstone | Legacy path points to migration/deprecation record |
| Retire | Compatibility removed after review window and rollback drill |

### Stale-reference outcomes

- `HOLD` when a consumer cannot be identified;
- `ABSTAIN` when release identity cannot be resolved;
- `DENY` when the request targets internal or unreleased state;
- `ERROR` for broken resolver/cutover behavior;
- never fall back silently to a compatibility directory.

[Back to top](#top)

---

<a id="correction-deprecation-and-rollback"></a>

## Correction, deprecation, and rollback

### Correction

A migration or path decision requires correction review when it changes:

- a public manifest URL;
- a cited release ID;
- included artifact meaning;
- release status;
- rights/sensitivity posture;
- correction or withdrawal lineage;
- consumer-visible release metadata.

### Deprecation

Deprecation should state:

- legacy path;
- accepted successor;
- object families affected;
- start and sunset dates;
- compatibility behavior;
- consumer obligations;
- stale-reference detection;
- support contact or steward role;
- rollback conditions.

### Rollback

Rollback must restore or preserve:

- prior path resolution;
- manifest identity and digest;
- public alias state;
- API/static-edge behavior;
- catalog and proof references;
- correction/withdrawal lineage;
- cache and CDN state;
- audit records explaining the rollback.

Rollback does not delete the attempted migration history.

### Documentation rollback

For this README-only change:

- prior blob: `6bf84d2616022fce28a8a0e6fa3e5b827d3fe800`;
- restore only if v0.2 introduces a factual, structural, link, governance, or compatibility defect;
- restoring v0.1 does not restore or change any release state.

[Back to top](#top)

---

<a id="security-rights-and-sensitivity"></a>

## Security, rights, and sensitivity

Release manifests can leak sensitive or operational information even without payload bytes.

Review:

- exact sensitive locations;
- living-person or DNA/genomic associations;
- private land or title linkages;
- archaeology, burial, sacred, or culturally restricted knowledge;
- rare-species detail;
- infrastructure topology;
- internal endpoints or bucket keys;
- unredacted filenames and paths;
- object-store layout;
- private review identities;
- embargoed release timing;
- signing and verification endpoints;
- rollback targets that reveal restricted artifacts;
- cache keys that permit enumeration.

### Fail-closed rule

When sensitivity, rights, sovereignty, consent, embargo, or security posture is unresolved:

- do not publish the manifest;
- do not expose exact refs;
- generalize, redact, restrict, quarantine, delay, or deny;
- record the transform and reason;
- preserve an auditable review path.

Secrets and private keys never belong in repository manifests or compatibility notes.

[Back to top](#top)

---

<a id="public-client-and-governed-ai-boundary"></a>

## Public client and governed-AI boundary

Public clients must not resolve this compatibility path directly.

A governed release response should:

- resolve the accepted manifest by stable release identity;
- verify digest/signature requirements;
- enforce release, policy, rights, sensitivity, correction, withdrawal, and stale state;
- return only public-safe artifact refs;
- provide citations and limitations;
- return finite outcomes such as `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR` where applicable.

Governed AI may summarize released EvidenceBundles and release metadata. It must not:

- infer release from a path;
- treat manifest prose as evidence;
- use compatibility files as canonical context;
- expose internal refs;
- invent approval or review state;
- bypass correction or withdrawal;
- reveal private reasoning or secrets.

EvidenceBundle and release records outrank generated language.

[Back to top](#top)

---

<a id="failure-and-incident-handling"></a>

## Failure and incident handling

Stop normal migration or release work when:

- a real secret or key is found;
- a manifest references restricted or unreleased payloads;
- a public route reads this compatibility path;
- two mutable manifest homes diverge;
- a digest mismatch appears;
- a signature cannot be verified;
- an approved/released label lacks supporting decision and review records;
- a correction or withdrawal is missing;
- rollback cannot restore prior safe state;
- consumers continue using a deprecated path after cutover;
- public caches serve stale or withdrawn release metadata.

Record:

- discovery time;
- affected paths and stable IDs;
- exposure scope;
- digests;
- consumers;
- immediate containment;
- rights/sensitivity/security assessment;
- correction/withdrawal requirement;
- recovery plan;
- accountable review.

Do not delete evidence of the incident to make the tree look clean.

[Back to top](#top)

---

<a id="open-verification-register"></a>

## Open verification register

| ID | Verification item | Evidence that closes it | Current status |
|---|---|---|---|
| REL-MAN-V-001 | Recursive subtree inventory | Commit-pinned recursive tree report | NEEDS VERIFICATION |
| REL-MAN-V-002 | Git-history inventory | Old-path and rename history report | NEEDS VERIFICATION |
| REL-MAN-V-003 | Git LFS and external store inventory | Object inventory with digests and owners | UNKNOWN |
| REL-MAN-V-004 | Internal consumer inventory | Code/workflow/config/docs dependency report | NEEDS VERIFICATION |
| REL-MAN-V-005 | External consumer inventory | Integration and public URL inventory | UNKNOWN |
| REL-MAN-V-006 | Manifest collection decision | Accepted ADR or equivalent decision | CONFLICTED |
| REL-MAN-V-007 | Manifest ID grammar | Accepted contract/schema/tests | NEEDS VERIFICATION |
| REL-MAN-V-008 | Canonicalization and digest profile | Accepted standard and fixtures | NEEDS VERIFICATION |
| REL-MAN-V-009 | Hardened schema | Versioned non-permissive schema | NEEDS VERIFICATION |
| REL-MAN-V-010 | Fixture corpus | Non-vacuous valid and invalid fixtures | HELD |
| REL-MAN-V-011 | Validator | Executable tested validator | HELD |
| REL-MAN-V-012 | Candidate assembler | Deterministic no-write dry run and tests | HELD |
| REL-MAN-V-013 | Promotion gate runtime | Accepted gate contracts, policy, review, receipts, tests | HELD |
| REL-MAN-V-014 | Evidence resolution | Resolver tests and closure report | NEEDS VERIFICATION |
| REL-MAN-V-015 | Rights and sensitivity enforcement | Policy tests and review records | NEEDS VERIFICATION |
| REL-MAN-V-016 | Independent review enforcement | Ruleset and review evidence | UNKNOWN |
| REL-MAN-V-017 | Signing and attestation | Key governance, signer, verifier, tests | UNKNOWN |
| REL-MAN-V-018 | Correction and withdrawal propagation | End-to-end tests and public record refs | NEEDS VERIFICATION |
| REL-MAN-V-019 | Rollback usability | Successful bounded rollback drill | NEEDS VERIFICATION |
| REL-MAN-V-020 | Cache/CDN invalidation | Verified cutover and invalidation report | UNKNOWN |
| REL-MAN-V-021 | Public trust-membrane enforcement | Route/network tests | NEEDS VERIFICATION |
| REL-MAN-V-022 | Migration packet | Reviewed mapping, cutover, and rollback packet | NOT STARTED |
| REL-MAN-V-023 | Deprecation entry | Approved deprecation record | NOT STARTED |
| REL-MAN-V-024 | Retirement eligibility | All prior items closed or explicitly waived with authority | NOT READY |

[Back to top](#top)

---

<a id="evidence-ledger"></a>

## Evidence ledger

| Evidence | Status | Supports | Does not prove |
|---|---:|---|---|
| Existing target README | CONFIRMED | Stable path and prior compatibility posture | Payload absence or retirement readiness |
| Parent `data/manifests/README.md` | CONFIRMED | Parent is non-canonical | Complete migration |
| `release/README.md` | CONFIRMED | Release responsibility root | Operational release capability |
| Singular and plural manifest READMEs | CONFIRMED DRAFT | Path conflict exists | Accepted canonical collection |
| Missing `release/manifests/release/README.md` | CONFIRMED at inspection | No same-name child guide | Global absence of release records |
| `ReleaseManifest` contract | CONFIRMED DRAFT/PROPOSED | Intended semantic role | Accepted field closure |
| `ReleaseManifest` schema | CONFIRMED THIN/PROPOSED | Current id/version/spec_hash shape | Governance completeness |
| Release-dry-run workflow | CONFIRMED | Explicit holds and selected shape checks | Candidate assembly, signing, release, publication |
| ADR-0011 | CONFIRMED proposed record | Artifact-family separation posture | Accepted enforcement |
| ADR-0018 | CONFIRMED proposed record | Proposed promotion sequence and current hold | Executed gate runtime |
| CODEOWNERS | CONFIRMED | GitHub review routing | Stewardship, review, approval, duty separation |
| Indexed search | CONFIRMED BOUNDED | This exact path surfaced only README | Recursive, historical, external, or runtime absence |

[Back to top](#top)

---

<a id="v01-to-v02-no-loss-ledger"></a>

## v0.1 to v0.2 no-loss ledger

| v0.1 substance | v0.2 preservation |
|---|---|
| Path is non-canonical | Preserved and strengthened as frozen pointer-only posture |
| Parent manifest lane is compatibility | Preserved |
| Release records belong under release governance | Preserved without falsely selecting singular/plural collection |
| Published bytes belong under `data/published/` | Preserved |
| Receipts, proofs, catalogs, registry, schemas, policy, and code remain separate | Preserved and expanded into object-family matrix |
| New trust-bearing writes are prohibited | Preserved and made explicit |
| Migration requires rollback | Preserved with minimum packet, cutover, and drill requirements |
| File move is not promotion | Preserved and connected to current workflow/ADR evidence |
| Retirement decision remained open | Preserved with explicit retain/migrate/retire criteria |
| Rollback target existed | Preserved as prior blob reference |

No v0.1 authority claim, prohibition, or rollback path is intentionally removed.

[Back to top](#top)

---

<a id="change-summary"></a>

## Change summary

### v0.2 — 2026-07-24

- preserved same path and stable identity;
- applied Directory Rules folder-README order;
- recorded exact bounded inventory and absent same-name release child;
- corrected overconfident plural-path wording;
- documented release collection conflict;
- grounded current release and promotion readiness holds;
- separated release object families;
- added closure, security, public-client, migration, cutover, correction, and rollback requirements;
- added open verification and evidence ledgers;
- created no release or implementation state.

---

<a id="final-operating-rule"></a>

## Final operating rule

> Keep `data/manifests/release/` frozen as a compatibility pointer. Route every discovered object by responsibility, preserve identity and audit history, resolve the release-manifest collection through reviewed governance, and migrate or retire only after consumers, evidence, policy, review, correction, and rollback are verified.

<p align="right"><a href="#top">Back to top</a></p>
