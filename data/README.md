<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/readme
title: data/ — Governed Lifecycle, Accountability, Registry, Catalog, and Released Carrier Root
type: readme; root-readme; canonical-data-root; lifecycle-and-accountability-boundary; compatibility-drift-index
version: v0.4.0
status: repository-grounded; ADR-0029-aligned; root-registry-active; mixed-maturity; payload-and-runtime-enforcement-unverified; no-release; no-publication
owners: ["@bartytime4life"]
created: 2026-06-29
updated: 2026-08-08
supersedes: v0.3.0 documentation at the same path; no data instance, lifecycle state, source admission, policy decision, release decision, runtime behavior, or publication state is superseded
prepared_under_prompt: KFM Repository Build-Out & Markdown Modernization Implementation Agent v6.0.0
policy_label: repository-facing; data-root; lifecycle-governed; internal-by-default; mixed-exposure; no-direct-public-path; release-gated; source-role-aware; rights-aware; sensitivity-aware; correction-aware; rollback-aware
current_path: data/README.md
owning_root: data/
root_registry_id: root.data
responsibility: governed lifecycle, accountability, registry, catalog, and released carrier instances
review_packet_id: kfm-data-root-readme-20260808
truth_posture: >
  CONFIRMED same-path target and stable document identity; accepted ADR-0029; adopted
  Directory Rules v2 bytes; active root.data machine projection; current main, repository,
  and data tree identities; nineteen current direct child directories; ten present canonical
  data lanes; absent conditional pre_raw lane; current compatibility, deprecated, and
  migration-candidate children; bounded data/catalog, data/registry, data/document,
  data/reports, data/maps, data/manifests, and data/rollback evidence; no exact-path open PR /
  PROPOSED future child-README convergence, recursive object-family inventory, migration
  manifests, consumer cutovers, and enforcement ratchets / CONFLICTED current direct and
  nested paths versus adopted subtype-first, lifecycle-first, and object-family-first
  placement; child READMEs that still cite prior Directory Rules or describe superseded
  authority; catalog domain/domains duplication; registry source and domain duplication /
  UNKNOWN exhaustive payloads, external stores, writers, consumers, runtime routes,
  deployed services, current source admissions, emitted closure objects, branch-rule
  coupling, retention execution, public hosting, and production effects / NEEDS VERIFICATION
  accountable specialist stewards, independent review, recursive rights and sensitivity
  posture, current-main enforcement breadth, compatibility expiry, correction propagation,
  cache invalidation, and rollback drills
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 1001a87233e0f23695b6b12e60c654f938e6ffb5
  base_tree: 1ef11008331b41797b8601f45003e2fe42c5c029
  data_tree: e4ce79ed25b3d6b772bf00ec77fca92d38801fd3
  prior_blob: 22d13b833369c290fe99e4a3d3c083835e5f2a37
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_sha256: sha256:44f7e94344cb42b630008eb0bc03a13fcb97dbdfba6f3e56579693a272571e6e
  directory_rules_decision: ADR-0029 accepted
  root_registry_blob: 024f668b5f0a9239bafa4f8b09e2afd86300ff8c
  catalog_tree: 6d7849e718244a9f9b540d047af6993a47cd0ed9
  registry_tree: 515fa1ff5ae98a332114b67b2cb486791f5d07d8
  document_tree: 0f790bcc92eddec204968aa0219663debb94a019
  reports_tree: 89de9c854233576cdeac443f480ad4b9ae881946
  direct_child_directories: 19
  direct_child_files: 1
  open_exact_path_pull_requests: 0
  inventory_method: exact commit and blob reads, exact Git tree inspection, bounded child README reads, code and pull-request search, and workflow threat preflight; no clone, payload download, Git LFS walk, object-store query, database query, runtime probe, deployment inspection, or production access
related:
  - raw/README.md
  - work/README.md
  - quarantine/README.md
  - processed/README.md
  - catalog/README.md
  - triplets/README.md
  - receipts/README.md
  - proofs/README.md
  - registry/README.md
  - published/README.md
  - document/README.md
  - reports/README.md
  - maps/README.md
  - manifests/README.md
  - prov/README.md
  - rollback/README.md
  - trade-routes/README.md
  - triplet/README.md
  - triplet(s)/README.md
  - ../release/README.md
  - ../docs/doctrine/directory-rules.md
  - ../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../control_plane/root_registry.yaml
  - ../docs/doctrine/lifecycle-law.md
  - ../docs/doctrine/trust-membrane.md
  - ../contracts/README.md
  - ../schemas/README.md
  - ../policy/README.md
  - ../tools/validators/README.md
  - ../tests/README.md
  - ../fixtures/README.md
  - ../pipelines/README.md
  - ../connectors/README.md
  - ../apps/governed-api/README.md
  - ../apps/explorer-web/README.md
  - ../.github/workflows/README.md
  - ../.github/PULL_REQUEST_TEMPLATE.md
tags: [kfm, data, lifecycle, raw, work, quarantine, processed, catalog, triplets, receipts, proofs, registry, published, release, correction, compatibility, migration, cite-or-abstain]
notes:
  - "v0.4.0 reconciles the root README with accepted ADR-0029 and the exact current data tree."
  - "The README follows the adopted ROOT_FULL profile and preserves legacy anchors used by prior editions."
  - "The current direct-child tree is evidence, not automatic canon; nonconforming children remain visible and fail closed."
  - "No payload, child README, source activation, contract, schema, policy, fixture, test, validator, pipeline, workflow, release record, migration, redirect, tombstone, runtime, API, UI, deployment, or public artifact is changed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/` — Governed Lifecycle and Accountability Root

> **One-line purpose.** `data/` owns governed lifecycle instances, accountability records, registries, catalog projections, and release-approved public-safe carriers. It does not create semantic meaning, policy permission, release authority, or truth merely by containing bytes.

**Quick navigation:** [Purpose](#purpose) · [Authority](#root-class-and-authority-owner) · [Status](#adoption-and-conformance-status) · [Belongs](#what-belongs-here) · [Prohibited](#what-does-not-belong-here) · [Inputs and outputs](#inputs-outputs-and-permitted-writers) · [Exposure and storage](#exposure-sensitivity-mutability-retention-and-storage) · [Validation](#validation-and-negative-checks) · [Review](#owners-reviewers-and-escalation) · [Governance](#governing-decisions-aliases-migrations-and-compatibility) · [Directory map](#direct-child-directory-map) · [Review triggers](#last-evidence-review-and-review-triggers) · [Lifecycle](#operating-model-and-lifecycle-invariant) · [Current classification](#current-direct-child-classification) · [Drift](#current-nested-drift-and-documentation-conflicts) · [Public boundary](#public-client-and-sensitive-data-boundary) · [Open verification](#open-verification-register) · [Evidence](#evidence-ledger)

> [!IMPORTANT]
> **A path is not promotion.** A file, digest, registry entry, receipt, proof, catalog record, triplet, map, report, manifest, workflow result, pull request, merge, or placement under `data/published/` does not become factual truth, policy permission, review approval, release authority, or KFM publication by location alone.

> [!CAUTION]
> **Normal public clients do not read internal lifecycle or compatibility lanes.** Public interfaces resolve release-approved, public-safe carriers through governed APIs or approved static delivery. RAW, WORK, QUARANTINE, PROCESSED, receipts, proofs, registries, internal catalogs, graph projections, and compatibility paths remain behind the trust membrane.

> [!WARNING]
> **Restricted bytes must not be committed because `data/` is their logical home.** Credentials, private endpoints, living-person private data, DNA/genomic material, precise rare-species or archaeology locations, sensitive infrastructure detail, protected cultural knowledge, unsafe private-land joins, and unclear-rights source payloads require approved storage, access, audit, retention, redaction, generalization, quarantine, or denial.

---

<a id="scope"></a>
<a id="purpose"></a>

## Purpose

`data/` is the canonical responsibility root for KFM **data instances** and their governed lifecycle and accountability relationships.

It answers these questions:

1. What stable data instance, capture, candidate, hold, validated record, projection, registry record, receipt, proof-support object, or released carrier is this?
2. Which lifecycle or accountability lane owns it?
3. Which source identity, source role, spatial scope, temporal scope, rights posture, sensitivity posture, digest, schema version, code/spec identity, and producer receipt travel with it?
4. Which validation, evidence, policy, review, release, correction, withdrawal, and rollback obligations remain open?
5. Which governed interface may expose it, to which audience and at which precision?

The durable public unit remains the **inspectable claim**. Data instances may support or carry that claim, but this root cannot make a claim true, cited, rights-cleared, reviewed, released, or public by implication.

This README documents repository state and adopted boundaries. It does not change lifecycle state or authorize any source, payload, release, migration, public route, or deletion.

[Back to top](#top)

---

<a id="repo-fit"></a>
<a id="authority-level"></a>
<a id="root-class-and-authority-owner"></a>

## Root class and authority owner

| Field | Current bounded result |
|---|---|
| Root ID | `root.data` |
| Root class | `canonical` |
| Projection status | `ACTIVE` |
| Responsibility | Governed lifecycle, accountability, registry, catalog, and released carrier instances |
| Allowed artifact kind | `data_instance` |
| Prohibited artifact kinds | `policy_rule`, `release_decision`, `schema`, `semantic_contract` |
| Exposure | `mixed` |
| Mutation | `mixed` |
| Retention | `lifecycle_policy` |
| Verified repository owner/review route | `@bartytime4life` |
| Validation profile | `lifecycle_and_accountability` |

The values above are projected by [`control_plane/root_registry.yaml`](../control_plane/root_registry.yaml) from accepted Directory Rules v2. The registry is **machine projection only**: it cannot activate a source, approve a policy, admit a payload, migrate a path, release an artifact, or publish.

### Authority split

| Concern | Authority owner | `data/` role |
|---|---|---|
| Semantic meaning and interface promises | [`contracts/`](../contracts/README.md) | Stores conforming instances; does not redefine meaning. |
| Machine shape and declared generated types | [`schemas/`](../schemas/README.md) | References validated shapes; does not host parallel schemas. |
| Allow, deny, hold, restrict, redact, or abstain rules | [`policy/`](../policy/README.md) | Carries policy references and obligations; path placement grants no permission. |
| Source-specific fetch and admission | [`connectors/`](../connectors/README.md) | Receives admitted candidates only through governed boundaries. |
| Transform and lifecycle orchestration | [`pipelines/`](../pipelines/README.md) and owned tools/packages | Stores results and receipts; job completion is not promotion. |
| Executable conformance | [`tests/`](../tests/README.md), [`fixtures/`](../fixtures/README.md), and validators | Provides bounded evidence; success is not review or release authority. |
| Release, correction, withdrawal, rollback, promotion, and signatures | [`release/`](../release/README.md) | Stores public-safe released carriers only after a separate decision. |
| Public delivery | Governed API and approved static delivery | Consumes release-resolved carriers; does not read internal stores as the normal path. |

[Back to top](#top)

---

<a id="status"></a>
<a id="status-notes"></a>
<a id="adoption-and-conformance-status"></a>

## Adoption and conformance status

### Current evidence snapshot

| Evidence | Current result | Interpretation |
|---|---|---|
| Default branch | `main@1001a87233e0f23695b6b12e60c654f938e6ffb5` | Immutable base for this review. |
| Repository tree | `1ef11008331b41797b8601f45003e2fe42c5c029` | Current root tree at the base. |
| `data/` tree | `e4ce79ed25b3d6b772bf00ec77fca92d38801fd3` | Exact current direct-child inventory. |
| Prior README blob | `22d13b833369c290fe99e4a3d3c083835e5f2a37` | v0.3.0 source replaced in place. |
| Directory Rules | blob `fd49a0b83e55cef52c1124281f093e263526898d` | Exact bytes adopted by ADR-0029. |
| Directory Rules decision | `ADR-0029`, `accepted` | Makes `docs/doctrine/directory-rules.md` the single writable human authority. |
| Root Registry | blob `024f668b5f0a9239bafa4f8b09e2afd86300ff8c` | Active projection; does not create authority. |
| Current direct children | 19 directories plus this README | Exact direct tree, not recursive payload proof. |
| Present canonical lanes | 10 | `raw`, `work`, `quarantine`, `processed`, `catalog`, `triplets`, `receipts`, `proofs`, `registry`, `published`. |
| Conditional `pre_raw/` | Absent | Correct unless a durable bounded intake queue is implemented and governed. |
| Noncanonical/deprecated direct children | 9 | Compatibility, migration, or deprecation work remains open. |
| Exact-path open PR search | 0 found | No open PR was found for `data/README.md` at preflight. |
| Runtime and deployed consumers | Not inspected | Current behavior remains `UNKNOWN`. |

### Conformance determination

**CONFIRMED:** `data/` is a canonical active root and its core present lifecycle/accountability lanes agree with adopted v2.

**CONFLICTED:** the current tree also retains topic buckets, singular/placeholder collection names, direct provenance, generic manifest, and generic rollback paths that adopted v2 classifies as compatibility, migration candidates, deprecated, or denied for new canonical writes.

**NEEDS VERIFICATION:** current payload families, active producers and consumers, external storage, rights and sensitivity, complete receipt/proof/catalog/release closure, enforcement breadth, and safe migration order.

The correct posture is **brownfield ratcheting**: preserve recoverability, deny new instances of known drift, classify before moving, cut producers to canonical single-write, prove consumers, and retire only after evidence supports it.

[Back to top](#top)

---

<a id="accepted-material"></a>
<a id="what-belongs-here"></a>

## What belongs here

### Canonical lifecycle and accountability instances

| Lane | Owns |
|---|---|
| [`raw/`](raw/README.md) | Immutable source captures or governed logical pointers with retrieval identity. |
| [`work/`](work/README.md) | Candidate normalization, georeferencing, crosswalk, extraction, transformation, and review state. |
| [`quarantine/`](quarantine/README.md) | Held material, reason codes, obligations, remediation linkage, and denied or unresolved state. |
| [`processed/`](processed/README.md) | Validated canonical records and deterministic versions that are not automatically public. |
| [`catalog/`](catalog/README.md) | STAC, DCAT, PROV, domain, matrix, discovery, and closure projections. |
| [`triplets/`](triplets/README.md) | Optional rebuildable relationship and graph projections. |
| [`receipts/`](receipts/README.md) | Durable process memory describing what ran, on what, with which inputs, tools, policies, and outputs. |
| [`proofs/`](proofs/README.md) | Evidence, validation, citation, review, integrity, and proof-pack support. |
| [`registry/`](registry/README.md) | Stable source, dataset, layer, domain, rights, sensitivity, and crosswalk identities. |
| [`published/`](published/README.md) | Immutable, versioned, release-approved public-safe carriers. |

A durable `pre_raw/` lane belongs here only when an accepted implementation establishes a bounded intake queue. It is not required for every source edge and is absent at the reviewed base.

### Instance requirements

A consequential instance should carry or resolve, as applicable:

- stable object identity and version;
- source identity, authority role, and upstream locator;
- observed, valid, source, retrieval, processing, release, and correction time without collapsing them;
- spatial scope, CRS, scale, precision, geometry digest, and public-safe transform;
- media type, size, content digest, schema version, and canonicalization rule;
- rights, attribution, sensitivity, access, retention, and legal-hold posture;
- producer code/spec/tool identity and run or transform receipt;
- evidence and citation references;
- validation, policy, review, and release references;
- correction, withdrawal, supersession, and rollback target.

Not every field belongs inline. A stable reference is acceptable when the referenced object is governed and resolvable.

[Back to top](#top)

---

<a id="exclusions"></a>
<a id="what-does-not-belong-here"></a>

## What does not belong here

| Material or behavior | Owning home or safe action |
|---|---|
| Semantic contracts | [`contracts/`](../contracts/README.md) |
| JSON Schema, contexts, generated type authority | [`schemas/`](../schemas/README.md) |
| Normative policy modules or release policy | [`policy/`](../policy/README.md), including `policy/release/` |
| ReleaseManifest, PromotionDecision/Receipt, CorrectionNotice, WithdrawalNotice, RollbackCard, or signatures | Object-family-first collections under [`release/`](../release/README.md) |
| Connector, pipeline, application, runtime, infrastructure, or reusable library code | Its execution-responsibility root |
| Secrets, credentials, private keys, signed URLs, or private endpoints | Approved secret and restricted operational systems |
| Unreviewed production, private, restricted, or harmful-precision data committed for test convenience | Synthetic fixtures or approved controlled storage |
| Direct public routes to RAW, WORK, QUARANTINE, PROCESSED, registry, receipt, proof, internal catalog, graph, or compatibility lanes | Governed API or released static delivery only |
| Topic-level data buckets used as new writable authorities | Route by lifecycle, accountability family, and registered scope |
| Hand-authored catalog or published records that claim release by location | Generate or validate from governed inputs and separate release decisions |
| Generated preview, build output, cache, virtual environment, or dependency install | Ignored local cache, external CI artifact, or approved generated-output boundary |
| AI output, map pixels, reports, graph edges, indexes, or scores represented as sovereign truth | Resolve EvidenceRef to EvidenceBundle and release state, or abstain/deny |

**Negative rule:** no new canonical writes go to `data/document/`, `data/manifests/`, `data/maps/`, `data/prov/`, `data/reports/`, `data/rollback/`, `data/trade-routes/`, `data/triplet/`, or `data/triplet(s)/` without an accepted decision and migration-compatible authority model.

[Back to top](#top)

---

<a id="inputs-outputs-and-permitted-writers"></a>

## Inputs, outputs, and permitted writers

### Inputs

Inputs may include:

- admitted source captures and event/admission records;
- source, dataset, layer, domain, rights, sensitivity, and crosswalk registry identities;
- deterministic pipeline outputs and receipts;
- validated domain records and evidence references;
- policy, review, and release references;
- correction, withdrawal, and supersession records;
- externally stored payload manifests whose locators are access-appropriate and digest-bound.

An input is not admissible merely because a connector fetched it or a workflow produced it.

### Outputs

| Output family | Maximum meaning |
|---|---|
| RAW capture | Preserved source response or logical pointer; not normalized truth. |
| WORK candidate | Mutable/versioned candidate under review. |
| QUARANTINE record | Held material plus obligations; not a failure to be hidden. |
| PROCESSED record | Validated canonical instance; not automatically public. |
| Catalog/triplet projection | Rebuildable discovery or relationship projection; not canonical replacement. |
| Receipt | Process memory; not proof, approval, release, or publication. |
| Proof-support object | Evidence/validation/review/integrity support; not release authority by itself. |
| Registry record | Stable identity and routing; not domain fact or release. |
| Published carrier | Release-approved public-safe bytes or logical artifact; release decision remains under `release/`. |

### Permitted writer classes

| Writer class | Bounded capability |
|---|---|
| Source admission | Emit governed RAW or QUARANTINE candidates and ingest receipts. |
| Pipeline processor | Emit WORK, QUARANTINE, or PROCESSED instances plus transform receipts. |
| Catalog/triplet builder | Emit rebuildable projections from validated inputs. |
| Receipt emitter | Record process memory without claiming proof or approval. |
| Proof builder | Emit proof-support objects from resolvable evidence and receipts. |
| Registry steward/process | Create or version stable identity records after required review. |
| Release assembler | Materialize `data/published/` carriers only from an accepted release decision. |
| Correction/rollback executor | Emit execution receipts and updated carriers without erasing prior lineage. |

Capabilities come from authenticated runtime policy and reviewed implementation, not from directory convention.

[Back to top](#top)

---

<a id="exposure-sensitivity-mutability-retention-and-storage"></a>

## Exposure, sensitivity, mutability, retention, and storage

### Exposure

| Lane class | Default exposure |
|---|---|
| RAW, WORK, QUARANTINE | Internal, steward-only, or restricted |
| PROCESSED, receipts, proofs, registries, internal catalogs/triplets | Internal unless an explicit governed projection permits more |
| PUBLISHED | Public or semi-public only within the release decision and access policy |
| Compatibility/deprecated paths | No direct public use |

### Mutability

- RAW captures are immutable or append-only by identity.
- WORK is mutable/versioned and must preserve derivation.
- QUARANTINE is append-only for holds, obligations, and remediation lineage; remediation emits a new state.
- PROCESSED instances are versioned; corrections do not silently overwrite relied-upon history.
- Catalogs and triplets are rebuildable projections with deterministic inputs where practical.
- Receipts, proof support, and registries preserve audit history appropriate to their role.
- PUBLISHED carriers are immutable by release identity; corrections create new release/correction lineage.

### Retention and deletion

Retention is policy-driven and may depend on source terms, legal hold, public reliance, sensitivity, incident response, and correction needs. Deletion is never inferred from a README, an empty directory, a migration target, or a new release. Restricted or trust-bearing content is inventoried before movement or deletion.

### Logical home versus physical bytes

The directory tree defines logical authority even when bytes live in PostGIS, object storage, a package registry, an external archive, or another governed service. A logical record or manifest should resolve:

- object ID and version;
- storage class and access-appropriate locator;
- digest, media type, size, and creation time;
- source, rights, sensitivity, retention, and legal-hold posture;
- schema, policy, producer, and receipt versions;
- exposure and release references;
- correction, withdrawal, and rollback target.

A locator is not authority. Restricted bytes must not be committed merely to make a repository tree look complete.

[Back to top](#top)

---

<a id="required-checks-before-use"></a>
<a id="validation"></a>
<a id="validation-and-negative-checks"></a>
<a id="root-guardrails"></a>

## Validation and negative checks

Validation is layered. A pass proves only the check's declared scope.

### Required checks by effect

| Effect | Minimum checks |
|---|---|
| README-only edit | UTF-8/LF/final newline, one H1, metadata parse, heading order, anchors, relative links, current-tree claims, no unsupported maturity claims, diff review, generated receipt integrity |
| New or changed data instance | Contract/schema, identity/digest, source role, temporal/spatial scope, rights/sensitivity, provenance/receipt, evidence/citation, policy/review, release/correction/rollback dependencies |
| Lifecycle transition | Valid predecessor, transition rule, actor/tool identity, input/output digests, finite outcome/reason code, receipt, replay/idempotency, failure and rollback path |
| Catalog/triplet projection | Canonical input refs, deterministic projection identity, STAC/DCAT/PROV or graph profile checks, parity, stale/supersession handling, non-authority statement |
| Published carrier | Evidence/proof closure, policy/review state, accepted release decision, immutable manifest/digests, public-safe transform, governed delivery, correction/withdrawal/cache invalidation, rollback target |
| Compatibility migration | Accepted authority decision when required, per-object classification, migration manifest, single-write cutover, bounded dual-read, consumer proof, parity, zero-writer/zero-consumer evidence, retirement record |

### Representative repository checks

```bash
git diff --check

python tools/validators/validate_generated_receipt.py \
  data/receipts/generated/<receipt>.json

make validate
```

Inspect each command and its dependencies before execution. Use deterministic no-network fixtures by default. Hosted checks remain separate evidence tied to an exact head SHA.

### Fail-closed negative checks

Reject or hold:

- source capture without source identity, role, rights, sensitivity, or retrieval identity;
- direct public reads from internal or compatibility lanes;
- RAW or QUARANTINE material presented as released;
- PROCESSED material assumed public-safe;
- a receipt treated as proof, or proof treated as release approval;
- a catalog/triplet projection treated as canonical truth;
- `data/published/` bytes without a release reference and correction/rollback path;
- new writes to deprecated or compatibility paths without governed migration authority;
- duplicate writable source, registry, catalog, triplet, proof, receipt, or published homes;
- exact sensitive geometry hidden only by client styling;
- silent overwrite, deletion, history erasure, or correction without supersession lineage.

[Back to top](#top)

---

<a id="owners-reviewers-and-escalation"></a>
<a id="review-burden"></a>

## Owners, reviewers, and escalation

`@bartytime4life` is the verified repository owner and Root Registry review route. That is not proof that specialist stewardship or independent approval has occurred.

| Change | Minimum review posture |
|---|---|
| Root README wording with no changed authority | Root owner plus documentation review |
| Lifecycle or accountability semantics | Data architecture, affected lane, contract/schema, policy, and validation review |
| Source admission or registry identity | Source steward, rights/sensitivity review, affected domain, and validation |
| Sensitive payload or precision change | Qualified rights/privacy/cultural/security/domain review; independent approval where required |
| Migration, alias, deprecation, or deletion | Old/new owners, producers, consumers, migration/validation, correction, and rollback review |
| Published carrier, correction, withdrawal, or rollback | Release authority, evidence/proof, policy, public-surface, correction, and rollback review |
| Public route or client behavior | Governed API/public UI owner plus policy, security, release, and affected data owners |

Escalate unresolved authority, identity, rights, sensitivity, public exposure, or migration conflicts to `HOLD`. Do not resolve them by prose, path convention, or majority of similar files.

[Back to top](#top)

---

<a id="governing-decisions-aliases-migrations-and-compatibility"></a>
<a id="adrs"></a>

## Governing decisions, aliases, migrations, and compatibility

### Governing authority

- [`ADR-0029`](../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) is accepted and adopts the exact v2 bytes at [`docs/doctrine/directory-rules.md`](../docs/doctrine/directory-rules.md).
- [`control_plane/root_registry.yaml`](../control_plane/root_registry.yaml) projects `root.data` as canonical and active without granting data, policy, release, or publication authority.
- Other numbered ADRs referenced by older data READMEs may remain proposed. Their filenames or prose do not override ADR-0029.

### Compatibility rule

Compatibility paths use **dual-read/single-write** only when verified consumers require it. New writes go to canonical homes. A compatibility pointer may preserve old-to-new mappings, migration facts, and recovery instructions; it may not retain a live writable copy of authority.

Every compatibility or deprecation record should identify:

- old path and canonical target;
- object family and stable identity mapping;
- reason and accepted decision;
- known producers and consumers;
- write prohibition and allowed read window;
- generation/synchronization method when a mirror exists;
- owner, start, expiry, and exit criteria;
- parity validation and rollback or forward-fix behavior.

### Migration discipline

1. Freeze authority inputs, tree, producers, consumers, identities, and digests.
2. Classify each object; do not route by filename alone.
3. Accept an authority decision before dependent structural work when required.
4. Add the canonical target and negative write guard.
5. Record old-to-new mappings in a schema-backed migration manifest.
6. Cut producers to canonical single-write.
7. Support bounded dual-read only for verified consumers.
8. Validate content, identity, rights, sensitivity, imports, links, schemas, policy, tests, workflows, release, correction, and rollback.
9. Prove zero writers and zero consumers at the old path.
10. Retire the alias while preserving decision history.

No migration, redirect, tombstone, or deletion is performed by this README update.

[Back to top](#top)

---

<a id="directory-map"></a>
<a id="direct-child-directory-map"></a>

## Direct-child directory map

The map below is the exact direct-child tree at `data_tree=e4ce79ed25b3d6b772bf00ec77fca92d38801fd3`. It shows repository state, not automatic canonicality.

```text
data/
├── README.md
├── catalog/
├── document/
├── manifests/
├── maps/
├── processed/
├── proofs/
├── prov/
├── published/
├── quarantine/
├── raw/
├── receipts/
├── registry/
├── reports/
├── rollback/
├── trade-routes/
├── triplet(s)/
├── triplet/
├── triplets/
└── work/
```

`pre_raw/` is not present. Adopted v2 makes it conditional, so absence is conforming until a durable bounded intake queue is actually implemented.

A child README owns deeper detail. This root README does not reproduce recursive domain trees or imply that every child payload was inspected.

[Back to top](#top)

---

<a id="last-reviewed"></a>
<a id="last-evidence-review-and-review-triggers"></a>

## Last evidence review and review triggers

- **Review date:** 2026-08-08
- **Base:** `main@1001a87233e0f23695b6b12e60c654f938e6ffb5`
- **Target prior blob:** `22d13b833369c290fe99e4a3d3c083835e5f2a37`
- **Review type:** exact root and direct-child tree inspection; accepted Directory Rules/ADR/Root Registry inspection; bounded child README and workflow preflight; no payload/runtime/deployment inspection
- **Direct-child directories:** 19
- **Current open exact-path PRs:** 0 found at preflight

Re-review when:

- authority, root class, permitted writer, consumer, exposure, sensitivity, storage, retention, or public route changes;
- a lifecycle, receipt, proof, registry, catalog, graph, published, release, correction, or rollback contract changes;
- a child is added, removed, renamed, reclassified, migrated, or retired;
- a compatibility deadline arrives;
- a payload, producer, consumer, secret, rights issue, sensitive-data issue, security event, correction, withdrawal, or rollback is discovered;
- validator/CODEOWNERS/workflow/ruleset coupling changes;
- current repository evidence materially diverges from the snapshot above.

[Back to top](#top)

---

<a id="lifecycle-invariant"></a>
<a id="operating-model-and-lifecycle-invariant"></a>

## Operating model and lifecycle invariant

The canonical lifecycle remains:

```text
SOURCE EDGE
  -> PRE_RAW candidate, when a durable bounded queue exists
  -> RAW
  -> WORK or QUARANTINE
  -> PROCESSED
  -> CATALOG and optional TRIPLETS
  -> PUBLISHED
```

A more precise state model is:

```text
PRE_RAW --admit----------------------> RAW
PRE_RAW --hold or reject-------------> QUARANTINE or finite denial record
RAW ---------------------------------> WORK
RAW --hold----------------------------> QUARANTINE
WORK --validate-----------------------> PROCESSED
WORK --hold---------------------------> QUARANTINE
QUARANTINE --remediate---------------> WORK
PROCESSED ----------------------------> CATALOG
PROCESSED --when applicable-----------> TRIPLETS
CATALOG + PROOF + ACCEPTED RELEASE ---> PUBLISHED
PUBLISHED --correct/supersede---------> new release lineage
PUBLISHED --withdraw------------------> withdrawal state plus invalidation
```

### Transition law

Promotion emits a new governed state or version. It is never inferred from a copy, move, filename, mutable alias, successful job, merge, or public URL.

A transition record should make these facts inspectable:

- object ID and predecessor version;
- source and evidence references;
- transition type and finite outcome;
- actor, tool, code/spec, schema, and policy versions;
- input and output digests;
- observed/effective/decision times;
- validation, policy, review, and release references;
- reason code, obligations, denied alternatives, and error state;
- correction, withdrawal, rollback, and replay behavior.

[Back to top](#top)

---

<a id="canonical-lane-map"></a>

## Canonical lane map

| Lane | Current path state | Canonical role | Public posture |
|---|---:|---|---|
| `pre_raw/` | `ABSENT / CONDITIONAL` | Bounded intake events and admission candidates only when implemented | Denied |
| [`raw/`](raw/README.md) | `PRESENT` | Immutable capture or governed pointer | Denied |
| [`work/`](work/README.md) | `PRESENT` | Candidate transform/review state | Denied |
| [`quarantine/`](quarantine/README.md) | `PRESENT` | Held material and obligations | Denied |
| [`processed/`](processed/README.md) | `PRESENT` | Validated canonical records | Internal by default |
| [`catalog/`](catalog/README.md) | `PRESENT` | Discovery, interoperability, provenance, and closure projections | Governed |
| [`triplets/`](triplets/README.md) | `PRESENT / OPTIONAL BY ARTIFACT` | Rebuildable relationship projections | Governed |
| [`receipts/`](receipts/README.md) | `PRESENT` | Durable process memory | Internal |
| [`proofs/`](proofs/README.md) | `PRESENT` | Evidence, validation, citation, review, and integrity support | Internal/review |
| [`registry/`](registry/README.md) | `PRESENT` | Stable identities and routing | Internal/governed projection |
| [`published/`](published/README.md) | `PRESENT` | Immutable release-approved public-safe carriers | Release-scoped |

The presence of a lane proves repository bytes, not populated payload quality, active producers, complete validation, release fitness, or public deployment.

[Back to top](#top)

---

<a id="confirmed-child-roots"></a>
<a id="current-direct-child-classification"></a>

## Current direct-child classification

| Direct child | Current disposition | Adopted destination or rule | Safe current action |
|---|---|---|---|
| `catalog/` | `PLACE` with nested drift | Canonical subtype-first catalog family | Keep canonical; reconcile nested names separately. |
| `processed/` | `PLACE` | Canonical lifecycle lane | Preserve. |
| `proofs/` | `PLACE` | Canonical accountability lane | Preserve separation from receipts/release. |
| `published/` | `PLACE` | Canonical released-carrier lane | Require separate release decision. |
| `quarantine/` | `PLACE` | Canonical hold lane | Preserve reason/obligation lineage. |
| `raw/` | `PLACE` | Canonical capture lane | Preserve immutable identity. |
| `receipts/` | `PLACE` | Canonical process-memory lane | Preserve non-proof boundary. |
| `registry/` | `PLACE` with nested drift | Canonical subtype-first registry family | Keep canonical; reconcile duplicate topic views separately. |
| `triplets/` | `PLACE` | Canonical optional graph lane | Preserve as rebuildable projection. |
| `work/` | `PLACE` | Canonical candidate lane | Preserve. |
| `document/` | `MIGRATE/HOLD` compatibility pointer | Route artifacts by lifecycle and authority | Freeze payload writes; retain pointer until inventory/cutover. |
| `manifests/` | `MIGRATE/HOLD` compatibility subtree | Route each manifest by object family | Deny new trust-bearing writes; classify and migrate. |
| `maps/` | `MIGRATE/HOLD` compatibility pointer | Route source/work/catalog/registry/published/release/rendering separately | Deny new canonical writes; preserve recovery. |
| `reports/` | `MIGRATE/HOLD` compatibility candidate lane | Unreleased candidates vs `data/published/reports/` vs `docs/reports/` | Freeze authority expansion; inventory producers/consumers. |
| `prov/` | `MIGRATE` candidate | `data/catalog/prov/` | Cut writers only after inventory and mapping. |
| `rollback/` | `DEPRECATED/HOLD` ambiguous lane | Decisions: `release/rollback_cards/`; execution: `data/receipts/rollback/` | No new generic writes; classify before migration. |
| `trade-routes/` | `MIGRATE/HOLD` topic bucket | `data/<lifecycle>/roads-rail-trade/` or registered object family | No bulk move; classify each object. |
| `triplet/` | `MIGRATE` compatibility source | `data/triplets/` | Canonical single-write after consumer inventory. |
| `triplet(s)/` | `DENY FOR NEW CANONICAL USE` | `data/triplets/` | Parenthesized placeholder grammar is nonconforming; preserve only for migration evidence. |

These outcomes classify path posture; they do not authorize the migrations themselves.

[Back to top](#top)

---

<a id="compatibility-and-placement-conflicts"></a>
<a id="current-nested-drift-and-documentation-conflicts"></a>

## Current nested drift and documentation conflicts

### `data/catalog/`

The exact direct catalog tree currently contains:

```text
catalog/
├── README.md
├── dcat/
├── domain/
├── domains/
├── prov/
├── settlements-infrastructure/
└── stac/
```

Current conflicts:

- both `domain/` and `domains/` exist;
- adopted v2 selects collection spelling `domains/`;
- `settlements-infrastructure/` is a direct topic child rather than a subtype-first domain projection;
- adopted v2's illustrative `matrix/` collection is absent;
- the current catalog README was authored against prior rules and does not enumerate the exact current tree.

These are migration and documentation-convergence candidates, not permission for this PR to move or create payloads.

### `data/registry/`

The exact direct registry tree contains canonical subtype-first families—`crosswalks/`, `datasets/`, `domains/`, `layers/`, `rights/`, `sensitivity/`, and `sources/`—plus domain topic directories and `source_descriptors/`.

Adopted v2 makes `data/registry/sources/<source_id>/` the canonical source identity/descriptor home. Domain-specific source views may be generated but not independent writers. The current `sources/` versus `source_descriptors/` split and topic-domain directories therefore require producer/consumer and identity analysis before convergence.

### Child README conflicts

- `data/rollback/README.md` still describes `data/rollback/` as canonical rollback support, while adopted v2 deprecates the generic lane and separates decision cards from execution receipts.
- several compatibility child READMEs cite prior Directory Rules and proposed ADR status;
- the v0.3 root README omitted current `document/` and `reports/` direct children;
- the current exact tree, adopted rules, and some child documentation are therefore not fully synchronized.

This root README records those conflicts. It does not silently rewrite child history or claim child conformance.

[Back to top](#top)

---

<a id="minimum-artifact-contract"></a>

## Minimum artifact and transition contract

A reviewable lifecycle artifact should provide, inline or by resolvable reference:

| Concern | Minimum support |
|---|---|
| Identity | Stable ID, version, object family, domain/source/scope identifiers |
| Source | Source ID, role, authority class, native ID, locator, retrieval identity |
| Time | Observation/valid/source/retrieval/processing/release/correction times as applicable |
| Space | CRS, geometry type, scope, precision, scale, digest, transform/generalization |
| Integrity | Media type, size, canonicalization, content/spec/schema digests |
| Rights and sensitivity | Rights/license/attribution, access class, sensitivity tier, obligations |
| Process | Producer code/spec/tool identity, inputs, outputs, receipt, finite outcome |
| Evidence | EvidenceRef, EvidenceBundle resolution, citations, limitations |
| Governance | Validation, policy, review, release, correction, withdrawal, rollback refs |
| Storage | Logical home, access-appropriate physical locator, retention/legal-hold posture |

A missing field does not always invalidate the object. It must, however, yield an explicit finite result—such as `HOLD`, `QUARANTINE`, `ABSTAIN`, `DENY`, or `ERROR`—when the missing support is material to the next transition.

[Back to top](#top)

---

<a id="transition-evidence-profile"></a>

## Transition evidence profile

| Transition | Required evidence posture | Failure posture |
|---|---|---|
| PRE_RAW -> RAW | Source activation/admission state, event/candidate identity, rights/sensitivity precheck, ingest receipt | Hold, quarantine, reject, or error |
| RAW -> WORK | Immutable input identity, transform plan/spec, target schema, run identity | Error or quarantine |
| RAW/WORK -> QUARANTINE | Reason code, obligations, restricted access, source link, remediation target | Remain held |
| WORK -> PROCESSED | Schema/contract, identity, geometry/time, source-role, rights/sensitivity, deterministic output, validation/transform receipt | Hold, quarantine, or error |
| PROCESSED -> CATALOG/TRIPLETS | Canonical input refs, projection spec/hash, catalog/graph profile, parity and stale handling | Abstain, hold, or error |
| CATALOG + PROOF -> PUBLISHED | Evidence closure, policy/review state, accepted release decision, immutable manifest/digests, public-safe transform, rollback/correction | Deny, hold, abstain, or error |
| PUBLISHED -> CORRECTED/WITHDRAWN | Prior release identity, reason, replacement/withdrawal object, affected surfaces, invalidation, new manifest or tombstone, rollback/forward fix | Error and containment |

Watchers and drift detectors may create candidates and receipts. They are non-publishers.

[Back to top](#top)

---

<a id="public-client-and-sensitive-data-boundary"></a>

## Public client and sensitive data boundary

### Public clients

Normal clients may consume:

- governed API responses resolved against release state;
- released static files and public-safe distributions;
- released map/tile/raster/vector carriers and catalog projections;
- EvidenceBundle-backed explanations and finite AI response envelopes;
- correction, supersession, stale, and withdrawal state appropriate to the audience.

They must not consume internal lifecycle or compatibility paths directly.

### Sensitive data

When rights, sovereignty, cultural sensitivity, living-person data, genomics, rare species, archaeology, infrastructure, private land, exact locations, or harmful inference are unclear:

1. stop or narrow intake;
2. preserve source and evidence lineage;
3. quarantine, restrict, redact, generalize, aggregate, delay, or deny;
4. record the transform, reason, policy, reviewer, and precision change;
5. validate cross-layer inference and side-channel leakage;
6. release only a reviewed public-safe carrier;
7. preserve correction, withdrawal, and rollback.

Client-side hiding is not a public-safe transform.

[Back to top](#top)

---

<a id="compatibility-retirement-sequence"></a>

## Compatibility retirement sequence

For each noncanonical direct child:

1. pin the tree, history, direct and indirect payloads, LFS/external stores, and current README;
2. identify object families, stable IDs, rights, sensitivity, lifecycle state, and release reliance;
3. identify all repository, runtime, deployed, external, and historical producers/consumers;
4. choose `MIRROR`, `MIGRATE`, `HOLD`, or `DENY` through the applicable authority;
5. add canonical target and negative write guard;
6. create a migration manifest with old/new path, digests, producers, consumers, compatibility window, validation, and rollback/forward-fix;
7. cut writers to canonical single-write;
8. support bounded dual-read only where verified consumers require it;
9. validate identity, content, links, imports, policy, rights, sensitivity, catalogs, graphs, public surfaces, caches, correction, and rollback;
10. prove zero writers and zero consumers before tombstone retirement or deletion;
11. preserve decision and supersession history.

A broad cleanup command is not an acceptable migration plan.

[Back to top](#top)

---

<a id="open-verification-register"></a>

## Open verification register

| ID | Item | Current status | Evidence needed before higher-risk action |
|---|---|---:|---|
| DATA-V-001 | Recursive object-family inventory | `NEEDS VERIFICATION` | Commit-pinned recursive tree, LFS/external-store inventory, per-object classification |
| DATA-V-002 | Active writers and consumers | `UNKNOWN` | Connector, pipeline, tool, workflow, API/UI, deployed-service, external-consumer graph |
| DATA-V-003 | Rights, sensitivity, retention, legal hold | `NEEDS VERIFICATION` | Source terms, policy decisions, steward review, storage/access/retention evidence |
| DATA-V-004 | Lifecycle contract/schema enforcement | `UNKNOWN` | Accepted contracts/schemas, validators, fixtures, negative tests, current hosted results |
| DATA-V-005 | Receipt/proof/catalog/release closure | `UNKNOWN` | Emitted linked instances and identity/digest agreement |
| DATA-V-006 | Public route and cache boundary | `UNKNOWN` | Governed route inventory, authorization, static hosting, cache/invalidation evidence |
| DATA-V-007 | Compatibility producer cutover | `NOT STARTED` | Per-path migration manifests, single-write proof, bounded dual-read consumers |
| DATA-V-008 | `catalog/domain` vs `catalog/domains` | `CONFLICTED` | Payload/producer/consumer inventory and accepted mapping |
| DATA-V-009 | `registry/sources` vs `registry/source_descriptors` | `CONFLICTED` | Canonical source ID mapping, writer inventory, generated-view decision |
| DATA-V-010 | Generic `data/rollback/` convergence | `HOLD` | Classification into release decisions vs execution receipts; consumer and recovery proof |
| DATA-V-011 | Triplet aliases | `HOLD` | Identity/parity, writer/consumer graph, canonical single-write and retirement plan |
| DATA-V-012 | Child README convergence | `NEEDS VERIFICATION` | Separate bounded docs slice against adopted v2 and exact child trees |
| DATA-V-013 | Specialist and independent stewardship | `NEEDS VERIFICATION` | Named accountable roles and review policy |
| DATA-V-014 | Current-main enforcement breadth | `NEEDS VERIFICATION` | Directory validator, required-check/ruleset evidence, latest exact-head runs |
| DATA-V-015 | Correction/withdrawal/rollback drill | `NOT RUN` | Representative released fixture, invalidation plan, replay and recovery evidence |

Unknowns narrow claims and block higher-risk transitions. They do not invite plausible defaults.

[Back to top](#top)

---

<a id="evidence-ledger"></a>

## Evidence ledger

| Evidence | What it supports | What it does not prove |
|---|---|---|
| `main@1001a87233e0f23695b6b12e60c654f938e6ffb5` | Repository/base identity for this review | Runtime, deployment, or public behavior |
| `data_tree=e4ce79ed25b3d6b772bf00ec77fca92d38801fd3` | Exact direct-child names and object IDs | Recursive payload quality, writers, consumers, or rights |
| `data/README.md` prior blob `22d13b...` | Stable target identity and v0.3 lineage | Current governance alignment after ADR-0029 |
| Adopted Directory Rules blob `fd49a0...` and digest `44f7e9...` | Normative placement, lifecycle/accountability, data/release split, naming, README, migration rules | Whether every current path conforms |
| Accepted ADR-0029 | Adoption and sole writable Directory Rules authority | Child migrations or release/publication approval |
| Root Registry blob `024f66...` | Active machine projection for `root.data` | Authority expansion, source activation, policy, review, or release |
| Catalog tree `6d7849...` | Exact direct catalog children | Semantic equivalence or safe migration |
| Registry tree `515fa1...` | Exact direct registry children | Canonical writer/consumer choice for duplicated families |
| `data/document/README.md` and tree `0f790b...` | Pointer-only compatibility posture and bounded direct contents | External/deployed consumers |
| `data/reports/README.md` and tree `89de9c...` | Transitional report-candidate posture and exact direct domain children | Payload correctness or release state |
| `data/maps/README.md` | Noncanonical pointer/retirement boundary | Complete map artifact inventory or renderer readiness |
| `data/manifests/README.md` | Noncanonical manifest routing/retirement boundary | Complete manifest inventory or accepted target for every family |
| `data/rollback/README.md` | Historical support-lane documentation | Current authority under adopted v2 |
| Workflow governance README and `repository-control.yml` | Non-publisher posture; bounded trusted-base `pull_request_target` guard | Complete safety audit of all workflows or effective settings |
| Open PR search | No exact-path open PR at preflight | No stale branch, external work, or future overlap |

No source in this ledger proves release, deployment, publication, source fitness, or public safety.

[Back to top](#top)

---

## No-loss ledger

| Prior v0.3 material | v0.4 disposition |
|---|---|
| Stable path, `doc_id`, created date, H1 role, and legacy anchors | Preserved |
| Lifecycle law and state-transition framing | Preserved and aligned to adopted v2 |
| Trust membrane and no-direct-public-path rule | Preserved and strengthened |
| Source-role, rights, sensitivity, evidence, policy, review, release, correction, and rollback controls | Preserved |
| Receipts/proofs/catalogs/triplets/registries/release separation | Preserved and corrected where v2 is more precise |
| Compatibility debt for maps, manifests, prov, triplet variants, and trade routes | Preserved and updated |
| `document/` and `reports/` omission | Repaired from exact current tree |
| Directory Rules v1.4/proposed-authority framing | Superseded by accepted ADR-0029 and adopted v2 evidence |
| Generic `data/rollback/` as canonical support | Corrected to adopted v2 deprecation and object-family split |
| `catalog/domain/` singular target | Corrected to adopted subtype-first `catalog/domains/`; current conflict remains visible |
| Current direct-child map | Replaced with exact 19-directory tree |
| Static badge wall | Removed; status is expressed through evidence tables and alerts |
| Payload, source, code, schema, policy, workflow, release, migration, or public-state change | None |

### Change history

#### v0.4.0 — 2026-08-08

- reconciled the same-path root README with accepted ADR-0029 and the active Root Registry;
- pinned current main, repository tree, data tree, target blob, and key child trees;
- adopted the v2 `ROOT_FULL` README profile without treating path or prose as authority;
- refreshed the exact direct-child map and classified all 19 current directories;
- corrected the data/release/rollback split and conditional `pre_raw/` posture;
- surfaced exact catalog and registry naming/authority drift;
- preserved trust, sensitivity, no-public-path, correction, migration, and rollback boundaries;
- changed documentation only.

#### v0.3.0 — 2026-07-24

- documented lifecycle and compatibility boundaries against then-current v1.4 evidence;
- refreshed maps and manifests compatibility posture;
- preserved v0.2 lifecycle, authority, and no-loss material.

> **Operating rule:** classify by responsibility and lifecycle first; preserve evidence and identity; release only through governed state transitions; keep every compatibility path single-write, reviewable, and reversible.

[Back to top](#top)
