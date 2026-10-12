<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/data-manifests-readme
title: data/manifests/ — Non-Canonical Manifest Compatibility, Routing, and Retirement Root
type: README; per-directory-readme; compatibility-root; retirement-boundary; manifest-family-routing-index
version: v0.2.0
status: draft; repository-grounded; non-canonical; compatibility-only; five-child-readmes-confirmed; payload-inventory-unverified; release-manifest-lanes-conflicted; manifest-terminology-overloaded; ADR-0011-proposed; migration-unresolved; retirement-unresolved; no-direct-public-path; non-release; non-publication
owner: NEEDS VERIFICATION — CODEOWNERS routes this path through the repository default owner @bartytime4life; accountable data, release, manifest, evidence, catalog, registry, domain, policy, security, migration, correction, rollback, UI, and documentation stewardship plus independent approval were not established
created: NEEDS VERIFICATION — a greenfield stub existed before v0.1
updated: 2026-07-24
supersedes: v0.1 documentation at the same path; no manifest, payload, contract, schema, policy, receipt, proof, catalog, registry, release, correction, rollback, runtime, or publication state is superseded
prepared_under_prompt: KFM Markdown Modernization & GitHub Documentation Implementation Agent v4.0.0
policy_label: repository-facing; data; manifests; compatibility; routing; retirement; deny-new-writes; authority-separation; evidence-aware; release-gated; correction-aware; rollback-aware; fail-closed; non-publisher
current_path: data/manifests/README.md
owning_root: data/
responsibility: preserve and retire a non-canonical topic-level manifest subtree by routing each manifest family and misplaced trust artifact to its actual responsibility root without becoming a parallel manifest, release, evidence, catalog, registry, published-artifact, policy, runtime, or publication authority
truth_posture: >
  CONFIRMED same-path target; canonical data root; data-root conflict between data/manifests and release manifests; release/ as the
  release-governance root; both release/manifest and release/manifests draft lanes; five direct child compatibility READMEs at geo,
  layers, release, flora, and story; current child posture denying new trust-bearing writes; ADR-0011 effective status proposed;
  ReleaseManifest and KFMGeoManifest draft semantic contracts with permissive schema stubs; selected child-specific contract,
  schema, published, registry, catalog, and release surfaces; current CODEOWNERS routing; and bounded indexed search /
  PROPOSED parent compatibility states, manifest-family classification, child routing contract, deny-new-writes rule, migration
  packet, redirect/tombstone semantics, validation outcomes, consumer cutover, retirement gates, rollback, and definition-of-done /
  CONFLICTED topic-level data/manifests versus responsibility-rooted release, published, registry, catalog, receipt, and proof lanes;
  singular release/manifest versus plural release/manifests; selected manifest-family schema and terminology overlaps /
  UNKNOWN exhaustive recursive subtree, historical payloads, generated or external stores, Git LFS content, active producers and
  consumers, runtime resolvers, accepted release services, signing infrastructure, deployment, CDN state, public endpoints,
  branch rules, and production effects / NEEDS VERIFICATION accountable stewards, accepted release-manifest collection path,
  accepted manifest-family homes, hardened schemas, fixtures, validators, policy wiring, complete payload and inbound-reference
  inventory, migration execution, deprecation register entries, consumer cutover, stale-reference detection, cache invalidation,
  correction propagation, independent review, and rollback rehearsal
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: a31e2f84bed7300c3f8adb8a9640ad1591597144
  target_prior_blob: c4cdbf0c0038f737447a7dc173f0fe49ef62490e
  historical_stub_blob: 6723e635ccf1e4885d8359d214467a3e6d4de9de
  data_root_readme_blob: fb7b0acfaea25b630a3042f24cb97558a996d05a
  release_root_readme_blob: 0752610b1df6d11143158f6f162f65ecd650e6a6
  release_manifest_singular_readme_blob: 6014cfc0f8394a44167f4226975b74f94f3b2a03
  release_manifests_plural_readme_blob: c699a527ff11bebad6a874ed1a37aa3a8213b86c
  geo_child_readme_blob: fbff970d99a6244ed1dad6f664a0831fbdcf8a64
  layers_child_readme_blob: 181c8ee653bf00f4e4fbb7037de121d9f35659fa
  release_child_readme_blob: 2c1dd216d74941d95b2b0c8a7e05a25fa4996346
  flora_child_readme_blob: d978bf9ddefc8d2a7988ee91af4255aa6799a01b
  story_child_readme_blob: d602f7438dd8c3a56d64164962acfe3c33a7841b
  adr_0011_blob: 40b0f47b87d584040803ed76aa6b31f5204b7fca
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  release_manifest_contract_blob: 9ca1c9d4a5b247196aa84a31a158fe734c8a6720
  release_manifest_schema_blob: 727db0a781900aa3816dcdce723fe355fec2e786
  geo_manifest_contract_blob: cf8e467cf32323718e38ad1510da3e5f60bef884
  geo_manifest_schema_blob: 931a0de24e45af4bc237c596c69bcaf305fb811f
  open_overlapping_pull_requests_found: "0"
  branch_name_preflight_matches: "0"
  inventory_method: exact GitHub file reads for the parent and five direct child READMEs, bounded indexed search, current-head inspection, branch-name search, and open-PR overlap search; no clone, recursive Git tree, Git history walk, Git LFS inventory, external store, signer, deployment, CDN, public endpoint, or production environment was inspected
related:
  - ../README.md
  - ./geo/README.md
  - ./layers/README.md
  - ./release/README.md
  - ./flora/README.md
  - ./story/README.md
  - ../published/README.md
  - ../receipts/README.md
  - ../proofs/README.md
  - ../catalog/README.md
  - ../registry/README.md
  - ../rollback/README.md
  - ../../release/README.md
  - ../../release/manifest/README.md
  - ../../release/manifests/README.md
  - ../../contracts/release/release_manifest.md
  - ../../contracts/evidence/kfm_geo_manifest.md
  - ../../contracts/data/layer_manifest.md
  - ../../contracts/ui/story_manifest.md
  - ../../schemas/contracts/v1/release/release_manifest.schema.json
  - ../../schemas/contracts/v1/evidence/kfm_geo_manifest.schema.json
  - ../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../docs/doctrine/directory-rules.md
  - ../../migrations/data/README.md
  - ../../.github/CODEOWNERS
notes:
  - "v0.2.0 is a same-path documentation-only modernization grounded in current repository evidence."
  - "The first twelve H2 sections follow the Directory Rules folder-README contract."
  - "Five direct child compatibility READMEs are confirmed: geo, layers, release, flora, and story."
  - "The parent does not select release/manifest or release/manifests as canonical; that conflict remains unresolved."
  - "No manifest instance, payload, redirect, tombstone, migration, deprecation entry, release, correction, rollback, runtime, or publication state is created."
  - "Static badges summarize inspected repository state only; they are not proof of inventory completeness, validation, migration, retirement, release, or publication."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/manifests/` — Non-Canonical Manifest Compatibility, Routing, and Retirement Root

> **One-line purpose.** Keep the historical `data/manifests/` subtree fail-closed as a compatibility, routing, and retirement surface while directing every manifest family, trust record, released payload, and implementation artifact to its actual responsibility root.

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#status)
[![Authority: compatibility only](https://img.shields.io/badge/authority-compatibility%20only-b42318?style=flat-square)](#authority-level)
[![Children: five confirmed](https://img.shields.io/badge/direct%20children-five%20confirmed-2da44e?style=flat-square)](#current-bounded-topology)
[![Writes: deny trust records](https://img.shields.io/badge/new%20trust%20writes-denied-b42318?style=flat-square)](#admission-and-deny-new-writes-contract)
[![Release manifest path: conflicted](https://img.shields.io/badge/release%20manifest%20path-CONFLICTED-d4a72c?style=flat-square)](#manifest-terminology-and-authority-split)
[![ADR-0011: proposed](https://img.shields.io/badge/ADR--0011-proposed-d4a72c?style=flat-square)](#adrs)
[![Retirement: unresolved](https://img.shields.io/badge/retirement-unresolved-d4a72c?style=flat-square)](#compatibility-and-retirement-state-model)
[![Publisher: no](https://img.shields.io/badge/publisher-no-6e7781?style=flat-square)](#authority-level)
[![Reviewed: 2026-07-24](https://img.shields.io/badge/reviewed-2026--07--24-0969da?style=flat-square)](#last-reviewed)

> [!IMPORTANT]
> **Safe current conclusion:** `data/manifests/` exists as a documented, non-canonical compatibility subtree with five confirmed direct child READMEs: `geo/`, `layers/`, `release/`, `flora/`, and `story/`. Current evidence does **not** establish a complete recursive payload inventory, accepted migration target, redirect, tombstone, consumer cutover, deprecation record, or retired state.

> [!CAUTION]
> The word **manifest** is overloaded. A `ReleaseManifest`, `KFMGeoManifest`, layer manifest, UI `StoryManifest`, catalog descriptor, generated receipt, and artifact sidecar are different object families with different authorities. Similar filenames or JSON shapes do not make them interchangeable.

> [!WARNING]
> Do not place new trust-bearing records or public payloads under this subtree. Public clients must use governed interfaces and released artifacts; they must not read a compatibility path, internal lifecycle store, or manifest-shaped file directly.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed) · [Topology](#current-bounded-topology) · [Children](#child-compatibility-lanes) · [Families](#manifest-terminology-and-authority-split) · [States](#compatibility-and-retirement-state-model) · [Admission](#admission-and-deny-new-writes-contract) · [Routing](#routing-misplaced-content) · [Consumers](#consumer-and-inbound-reference-inventory) · [Migration](#migration-and-retirement-procedure) · [Redirect](#redirect-and-tombstone-contract) · [Rollback](#rollback-correction-and-supersession) · [Done](#definition-of-done) · [Open verification](#open-verification-register)

---

<a id="boundary"></a>

## Purpose

`data/manifests/` is a **non-canonical compatibility and retirement subtree** beneath the canonical [`data/`](../README.md) responsibility root.

Its present responsibility is narrow:

1. make the historical path visible;
2. prevent new trust-bearing writes;
3. classify manifest terminology and artifact families;
4. route misplaced records to their real authority roots;
5. preserve stable redirects, migration notes, and retirement evidence when needed;
6. keep uncertainty, conflicts, and incomplete inventory visible;
7. support a reversible decision to retain, redirect, tombstone, or retire the subtree.

This directory does not become canonical merely because several child paths exist or because a document uses the word “manifest.”

The KFM lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Promotion is a governed state transition, not a move into a directory named `manifests`.

A manifest-shaped record may describe, bind, index, or support an artifact. It does not by itself make the artifact true, evidence-closed, rights-cleared, policy-admitted, reviewed, released, public-safe, or recoverable.

[Back to top](#top)

---

<a id="repo-fit"></a>

## Authority level

**Compatibility guidance and routing index only; non-canonical, non-semantic, non-schema, non-policy, non-evidence, non-catalog, non-release, non-runtime, and non-publication authority.**

| Question | Controlling authority | Role of `data/manifests/` |
|---|---|---|
| What does a named manifest object mean? | The matching contract under `contracts/` | Links to semantic authority; does not redefine it |
| What machine shape is accepted? | The matching schema under `schemas/` | Records schema maturity; does not become a schema home |
| Which source or evidence supports a claim? | Source records, `EvidenceRef`, `EvidenceBundle`, receipts, and proofs | Preserves references; cannot manufacture closure |
| What policy permits use or exposure? | `policy/` and governed decisions | Carries pointers only |
| Which records are cataloged? | `data/catalog/` | Routes catalog records; cannot become a catalog |
| Which process occurred? | `data/receipts/` | Routes process memory; cannot replace receipts |
| What proves integrity or support? | `data/proofs/` and governed validation | Routes proof support; cannot become proof storage |
| Where are source descriptors kept? | `data/registry/` and accepted source governance | Routes source records; cannot activate or rank sources |
| Where are released public-safe bytes kept? | `data/published/` after release gates | Must not store or expose payload bytes |
| Who decides release state? | `release/` governance records and accountable review | Has no approval authority |
| Which release-manifest collection path is canonical? | Accepted decision resolving `release/manifest/` versus `release/manifests/` | Records the conflict; does not decide it |
| How is a compatibility path migrated? | `migrations/data/`, reviewed plan, validation, and recovery | May carry a pointer to the migration packet |
| What may public clients read? | Governed APIs and released artifacts | This internal compatibility subtree is not a public interface |

### Anti-collapse rules

`data/manifests/` must not collapse:

- `ReleaseManifest` into `KFMGeoManifest`;
- release governance into artifact metadata;
- a layer descriptor into release approval;
- a UI `StoryManifest` into a release manifest;
- a receipt into proof;
- proof into catalog;
- catalog into publication;
- a signature-shaped object into accountable release approval;
- a schema-valid record into a release-complete record;
- a file move into promotion;
- a redirect into migration completion;
- a README into retirement evidence;
- CODEOWNERS routing into stewardship or independent approval;
- a merged pull request into operational cutover.

[Back to top](#top)

---

## Status

### Repository-grounded status matrix

| Surface | Current evidence | Safe conclusion |
|---|---|---|
| Parent README | v0.1 exists at the same path | **CONFIRMED — documentation** |
| Parent authority posture | Current data root records `data/manifests` versus release manifests as conflicted compatibility debt | **CONFIRMED — non-canonical** |
| Direct child `geo/` | Repository-grounded v0.2.0 README | **CONFIRMED — compatibility only** |
| Direct child `layers/` | Repository-grounded v0.2 README | **CONFIRMED — compatibility only** |
| Direct child `release/` | Repository-grounded v0.2 README | **CONFIRMED — compatibility only** |
| Direct child `flora/` | Repository-grounded v0.2 README | **CONFIRMED — compatibility only** |
| Direct child `story/` | Repository-grounded v0.2 README | **CONFIRMED — compatibility only** |
| Exact recursive payload inventory | Not established by current connector inspection | **UNKNOWN / NEEDS VERIFICATION** |
| Trust-bearing records beneath the parent | Child searches generally found README-only or no child record, but methods were bounded | **NOT ESTABLISHED; absence not proven** |
| Release-manifest collection | Both singular and plural release lanes exist as draft guidance | **CONFLICTED** |
| `ReleaseManifest` contract and schema | Draft semantic contract plus permissive schema stub | **CONFIRMED mixed maturity** |
| `KFMGeoManifest` contract and schema | Draft semantic contract plus permissive schema stub | **CONFIRMED mixed maturity** |
| Layer manifest authority | Contracts and schemas exist with placement and release-bridge conflicts | **CONFLICTED / NEEDS VERIFICATION** |
| Story manifest terminology | UI story manifests, release manifests, published story payloads, and story-node catalogs are distinct | **CONFIRMED split; placement incomplete** |
| Parent redirect or tombstone | Not established | **UNKNOWN** |
| Accepted migration or retirement decision | Not established | **NEEDS VERIFICATION** |
| Consumer cutover and stale-reference detection | Not established | **NEEDS VERIFICATION** |
| Production/runtime use | Not inspected | **UNKNOWN** |
| Public or publication authority | Denied by responsibility boundary | **NOT OWNED** |

### Truth labels used here

| Label | Meaning |
|---|---|
| `CONFIRMED` | Verified from current repository bytes or governing doctrine inspected for this update |
| `PROPOSED` | Design, state, routing rule, migration, or target not accepted and verified |
| `CONFLICTED` | Current paths or authority descriptions disagree and require coordinated resolution |
| `UNKNOWN` | Evidence is insufficient to support a stronger statement |
| `NEEDS VERIFICATION` | A concrete repository, review, migration, runtime, or operational check remains |

The parent is therefore **documented compatibility debt with bounded child guidance**, not a canonical manifest registry or a completed retirement.

[Back to top](#top)

---

<a id="accepted-contents"></a>

## What belongs here

Only compatibility and retirement material whose primary responsibility is preserving the historical subtree may remain here:

- this parent README;
- direct child compatibility READMEs;
- bounded inventory notes that list exact tracked paths, blobs, references, and classification status;
- migration packet pointers;
- reviewed crosswalks from historical paths to accepted responsibility roots;
- redirect or tombstone records that contain no trust-bearing payload;
- deprecation and consumer-cutover notes;
- correction or supersession pointers for stale documentation;
- validation summaries proving path classification, no-new-writes posture, link integrity, and migration readiness;
- rollback references for a compatibility migration;
- explicit `UNKNOWN`, `CONFLICTED`, `HOLD`, `NOT_RUN`, and `NEEDS VERIFICATION` records.

Any retained compatibility artifact must state:

- why it remains;
- whether it is normative, pointer-only, deprecated, redirected, tombstoned, or retained for history;
- which accepted target owns the actual object;
- which inbound references still depend on it;
- what validation and review were performed;
- what removes the compatibility need;
- how rollback or correction works.

[Back to top](#top)

---

<a id="exclusions"></a>

## What does not belong here

Do **not** place any of the following under `data/manifests/` or its children as new trust-bearing content:

- `ReleaseManifest` instances;
- release decisions, promotion decisions, candidate packets, review records, rollback cards, withdrawal notices, correction notices, signatures, or changelogs;
- `KFMGeoManifest` instances used as active artifact sidecars;
- layer-manifest instances used by active registries, release packages, or published artifacts;
- UI `StoryManifest` instances, story-deck payloads, or story-player runtime assets;
- RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED payloads;
- PMTiles, COGs, GeoJSON, GeoParquet, tiles, rasters, reports, exports, archives, or API payloads;
- process receipts;
- evidence bundles, proof packs, validation proof objects, integrity bundles, or signature evidence;
- STAC, DCAT, PROV, CatalogMatrix, domain-catalog, or search-index records;
- SourceDescriptor or registry records;
- canonical semantic contracts;
- canonical machine schemas;
- policy bundles, allow/deny decisions, rights decisions, or sensitivity rules;
- validators, tests, fixtures, connectors, pipelines, packages, application code, or runtime configuration;
- secrets, keys, certificates, signing credentials, private endpoints, restricted payloads, or precise sensitive locations;
- generated summaries represented as truth, evidence, review, or release authority;
- unreviewed aliases or redirects that silently preserve a deprecated path.

When trust-bearing content is found here, do not normalize it by merely renaming or moving the file. Classify it, preserve identity and history, apply rights and sensitivity handling, migrate through the governed path, validate the target, record correction and recovery, and keep the old path fail-closed.

[Back to top](#top)

---

## Inputs

A compatibility, routing, or retirement decision may consume:

| Input | Minimum posture |
|---|---|
| Directory Rules and accepted ADRs | Establish responsibility roots and migration authority |
| Current parent and child READMEs | Establish documented compatibility boundaries |
| Recursive tracked inventory | Identify every file, symlink, subdirectory, LFS pointer, and generated record |
| Git history and rename analysis | Preserve historical identity and inbound references |
| Object-family contracts and schemas | Classify manifest meaning and machine shape |
| Source, evidence, rights, and sensitivity records | Prevent unsafe migration or exposure |
| Release records and decisions | Determine whether release-facing content exists |
| Receipt, proof, catalog, registry, and published inventories | Route each artifact family correctly |
| Producer and consumer inventory | Identify writers, readers, caches, examples, docs, and workflows |
| Link and reference graph | Identify inbound and outbound path dependencies |
| Migration packet | Pin source, target, digests, order, validation, and recovery |
| Retention and deletion policy | Determine whether history requires a retained pointer or tombstone |
| Correction and rollback context | Preserve reversible change and stale-state handling |

Inputs must be pinned by path, commit, digest, object ID, release ID, or migration ID where material. “Everything under manifests” is not an adequate migration scope.

[Back to top](#top)

---

## Outputs

This compatibility root may produce documentation and routing evidence only:

- parent and child compatibility contracts;
- bounded path inventories;
- object-family classification matrices;
- inbound-reference inventories;
- migration and retirement plans;
- redirect and tombstone specifications;
- validation outcomes;
- consumer-cutover checklists;
- deprecation and drift-register pointers;
- correction, supersession, and rollback references;
- evidence-bounded status reports.

| Output | What it proves | What it does not prove |
|---|---|---|
| Compatibility README | The boundary is documented | Payload inventory or migration completion |
| Bounded path inventory | Named paths were inspected | Recursive completeness unless the method proves it |
| Classification matrix | Intended authority routing is explicit | Content was moved or accepted |
| Redirect plan | A compatibility mechanism is designed | Redirect exists or consumers use it |
| Migration packet | Source, target, validation, and recovery are specified | Migration was executed |
| Link-check result | Tested links resolved at a revision | Runtime consumer cutover |
| Tombstone record | A deprecated path is intentionally retained | Public caches or external clients stopped using it |
| Deletion commit | Repository path was removed | External storage, history, or downstream references are safe |
| Pull request or merge | Repository bytes changed | Release, publication, retirement, or production parity |

This root emits no release, policy, evidence, source, lifecycle, or public state by itself.

[Back to top](#top)

---

<a id="validation-checklist"></a>

## Validation

Validation must be **classification-aware, fail-closed, and evidence-bounded**.

### Finite validation outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | The named check ran against pinned inputs and satisfied its stated expectation |
| `FAIL` | The named check ran and found a violation |
| `HOLD` | Required evidence, authority, review, target, or recovery is incomplete |
| `NOT_APPLICABLE` | A reviewed rationale shows the check does not apply |
| `NOT_RUN` | The check was intentionally not executed and the gap remains visible |
| `ERROR` | Tooling or environment failure prevented a trustworthy result |

### Parent validation matrix

| Check | Expected result |
|---|---|
| Directory placement | Parent remains a compatibility subtree under `data/`; no new root is created |
| First twelve sections | Folder README contract remains in the required order |
| Child index | Every confirmed direct child is listed with bounded status |
| Recursive inventory | Every tracked file, LFS pointer, and subdirectory is classified—or status remains `HOLD` |
| New-write guard | No trust-bearing record is admitted under parent or child compatibility paths |
| Contract/schema routing | Every manifest family points to its accepted semantic and machine authorities |
| Release routing | Release records route to the accepted release-governance lane after singular/plural conflict resolution |
| Data-plane routing | Receipts, proofs, catalogs, registries, and published bytes route to their own lanes |
| Sensitive material | Rights, sensitivity, living-person, cultural, infrastructure, and precise-location risks are reviewed before handling |
| Identity preservation | IDs, digests, release references, correction lineage, and Git history remain reconstructable |
| Inbound references | Writers, readers, docs, examples, tests, workflows, and runtime consumers are inventoried |
| Redirect behavior | Any redirect is deterministic, non-authoritative, non-public, and tested |
| Stale-reference detection | Deprecated paths fail visibly or resolve through the approved compatibility mechanism |
| Migration recovery | Source state, target state, rollback/forward-fix path, and post-recovery checks are recorded |
| Public boundary | No public client or normal UI path consumes `data/manifests/` |
| Host rendering | Markdown, anchors, tables, alerts, and relative links render correctly |

### Current validation boundary

This documentation update validates the README structure and inspected repository references. It does **not** establish:

- a recursive subtree inventory;
- absence of historical or external payloads;
- accepted canonical manifest-family paths;
- redirect behavior;
- consumer cutover;
- signing or manifest validation;
- release readiness;
- migration execution;
- retirement;
- runtime or public behavior.

[Back to top](#top)

---

## Review burden

Review burden scales with authority, sensitivity, consequence, and recoverability.

| Change | Minimum review posture |
|---|---|
| README-only clarification | Documentation maintainer plus affected compatibility-lane maintainer |
| Add or change child routing | Data maintainer plus owner of every target responsibility root |
| Classify a manifest family | Contract/schema maintainers plus affected producer and consumer maintainers |
| Resolve `release/manifest` versus `release/manifests` | Release governance, architecture, migration, and affected consumer review |
| Add a compatibility redirect | Data, runtime, API/UI, security, and migration review |
| Move receipts, proofs, catalogs, or registry records | Owning trust-artifact maintainers plus migration review |
| Move published or release-facing content | Release authority, policy, rights, sensitivity, correction, and rollback review |
| Remove a tracked path | Inbound-reference, retention, documentation, migration, and rollback review |
| Sensitive-domain material | Relevant domain, rights, sensitivity, and security review |
| Destructive or irreversible cleanup | Explicit risk acceptance and independently reviewed recovery posture |
| Public-client or cache effect | Governed API/UI, release, deployment, correction, and cache-invalidation review |

CODEOWNERS routing is not a `StewardshipAssignment`, `ReviewRecord`, policy decision, release approval, or proof of independent review.

[Back to top](#top)

---

## Related folders

### Direct child compatibility lanes

| Child | Current bounded responsibility |
|---|---|
| [`geo/`](./geo/README.md) | Routes `KFMGeoManifest`, geo release records, signatures, catalogs, proofs, receipts, source records, and published geospatial bytes |
| [`layers/`](./layers/README.md) | Routes layer descriptors, layer manifests, release bridges, registry entries, catalogs, and published layers |
| [`release/`](./release/README.md) | Routes `ReleaseManifest`, decisions, signatures, candidates, corrections, rollback records, and published artifacts |
| [`flora/`](./flora/README.md) | Routes Flora manifest terminology and sensitive domain release/published/catalog/proof/registry surfaces |
| [`story/`](./story/README.md) | Separates UI `StoryManifest`, `ReleaseManifest`, published story payloads, story-node catalogs, policy, and runtime |

### Responsibility roots

| Location | Responsibility |
|---|---|
| [`../`](../README.md) | Canonical data lifecycle and data-plane trust root |
| [`../receipts/`](../receipts/README.md) | Process memory and execution receipts |
| [`../proofs/`](../proofs/README.md) | Evidence and integrity support |
| [`../catalog/`](../catalog/README.md) | Discovery and interchange records |
| [`../registry/`](../registry/README.md) | Source and accepted registry records |
| [`../published/`](../published/README.md) | Release-approved public-safe artifact bytes |
| [`../rollback/`](../rollback/README.md) | Data-plane rollback support |
| [`../../release/`](../../release/README.md) | Release governance, review, decision, correction, withdrawal, and rollback records |
| [`../../release/manifest/`](../../release/manifest/README.md) | Draft singular release-manifest lane |
| [`../../release/manifests/`](../../release/manifests/README.md) | Draft plural release-manifest collection lane |
| [`../../contracts/`](../../contracts/README.md) | Semantic meaning |
| [`../../schemas/`](../../schemas/README.md) | Machine-checkable shape |
| [`../../policy/`](../../policy/README.md) | Admissibility, rights, sensitivity, and obligations |
| [`../../migrations/data/`](../../migrations/data/README.md) | Governed data-state migration mechanics |

[Back to top](#top)

---

## ADRs

### Current decisions and conflicts

| Record | Effective status | Relevance |
|---|---|---|
| [`ADR-0011`](../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md) | `proposed` | Proposes explicit separation among receipts, proofs, catalogs, release manifests/decisions, and published artifacts; identifies `data/manifests/` as migration debt |
| Release manifest singular/plural decision | **Not accepted** | Must resolve `release/manifest/` versus `release/manifests/` before hard-coded migration |
| Manifest-family schema-home decisions | Mixed / unresolved | Geo, layer, story, and domain-specific manifest families require accepted semantic and machine homes |
| Public-client boundary | Governed doctrine and proposed ADRs | Compatibility paths must not become public data interfaces |

This README does not accept ADR-0011, select a canonical release-manifest collection, move a file, authorize deletion, or graduate any manifest family.

### ADR trigger

A new or amended ADR is required when a proposed change:

- selects or changes the canonical release-manifest collection path;
- creates a new manifest authority root;
- collapses multiple manifest families into one object;
- changes the contract/schema/policy responsibility split;
- creates a public compatibility API;
- changes the data lifecycle or release boundary;
- authorizes a non-reversible retirement with material consequences;
- intentionally bends a KFM invariant.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-24 |
| Review status | Repository-grounded v0.2.0 compatibility-root modernization |
| Current maturity | Five documented child lanes; recursive inventory, accepted routing, consumer cutover, migration, and retirement unverified |
| Next review trigger | Accepted manifest-path decision, new child lane, discovered payload, migration packet, redirect implementation, deprecation entry, consumer cutover, path removal, or public-impacting change |

[Back to top](#top)

---

## Current bounded topology

The directly confirmed README topology is:

```text
data/
└── manifests/
    ├── README.md
    ├── geo/
    │   └── README.md
    ├── layers/
    │   └── README.md
    ├── release/
    │   └── README.md
    ├── flora/
    │   └── README.md
    └── story/
        └── README.md
```

This is a **bounded named-path inventory**, not a recursive tree attestation. Differently named files, deeper descendants, unindexed paths, Git LFS objects, generated outputs, external stores, historical branches, and restricted systems remain `UNKNOWN`.

### Parent-child rule

A child README may specialize classification and migration guidance. It may not:

- make its child path canonical;
- override the parent’s deny-new-writes posture;
- choose an unresolved authority path without an accepted decision;
- admit payloads, release records, or public access;
- treat bounded search as recursive proof;
- convert proposed semantics into implemented behavior.

[Back to top](#top)

---

## Child compatibility lanes

### `geo/`

Primary ambiguity: geospatial artifact metadata, signed sidecars, release manifests, catalogs, proofs, receipts, sources, and published PMTiles/COG bytes.

Current bounded posture:

- `KFMGeoManifest` semantic contract exists;
- a permissive Draft 2020-12 schema stub exists;
- ADR-0023 remains proposed;
- declared validator and fixture coverage are not established;
- the child path remains compatibility-only.

### `layers/`

Primary ambiguity: layer descriptor versus data LayerManifest versus release bridge versus registry/catalog/published layer records.

Current bounded posture:

- contract and schema surfaces exist;
- release and schema-home conventions remain conflicted;
- active manifest instances and runtime consumers are unverified;
- the child path remains pointer-only compatibility.

### `release/`

Primary ambiguity: historical topic path versus canonical release governance, plus singular `release/manifest/` versus plural `release/manifests/`.

Current bounded posture:

- `ReleaseManifest` contract and permissive schema stub exist;
- release readiness workflows expose holds rather than operational release machinery;
- accepted collection path, validator, fixtures, signing, review enforcement, and promotion execution remain unresolved;
- the child path remains compatibility-only.

### `flora/`

Primary ambiguity: domain manifest notes versus release records, published Flora artifacts, catalogs, proof/evidence support, registries, and sensitivity policy.

Current bounded posture:

- release, candidate, published, catalog, proof, registry, policy, and package surfaces exist;
- sensitive Flora precision requires fail-closed review;
- exact child payload inventory is bounded;
- the child path remains compatibility-only.

### `story/`

Primary ambiguity: UI `StoryManifest`, release manifest, published story payload, story-node catalog, story policy, and runtime Story Player assets.

Current bounded posture:

- multiple story object families and runtime surfaces exist;
- no accepted story release-manifest sublane was established at the checked paths;
- “manifest” terminology is overloaded and must be classified before migration;
- the child path remains compatibility-only.

[Back to top](#top)

---

## Manifest terminology and authority split

<a id="manifest-families"></a>

| Family | Core question | Semantic home | Instance / payload posture |
|---|---|---|---|
| `ReleaseManifest` | Which governed artifact set and support records define a release? | `contracts/release/release_manifest.md` | Release-governance lane selected by accepted decision; not under `data/manifests/` |
| `KFMGeoManifest` | Which geospatial artifact, digest, provenance, spatial scope, and evidence/policy context are bound? | `contracts/evidence/kfm_geo_manifest.md` | Artifact sidecar or release support only after accepted schema, validation, policy, and release flow |
| Data LayerManifest | Which layer artifact, identity, geometry, source, and display-relevant data properties are described? | `contracts/data/layer_manifest.md` | Accepted registry, release, or published-adjacent location; current placement conflict remains |
| Release layer-manifest bridge | Which layer release-facing binding references data and release records? | `contracts/release/layer_manifest.md` | Release governance, not data compatibility |
| UI `StoryManifest` | Which story nodes, sequence, presentation, and interaction behavior compose a story? | `contracts/ui/story_manifest.md` | UI/runtime or released story payload path; not a ReleaseManifest |
| Catalog record | How is an artifact discovered and interchanged? | Catalog contracts and `data/catalog/` | Catalog lane; not proof or release decision |
| Receipt | What process ran and what did it observe? | Receipt contracts and `data/receipts/` | Process memory; not proof or release |
| Proof object | What evidence or integrity support closes a requirement? | Proof/evidence contracts and `data/proofs/` | Support record; not catalog or release |
| Published artifact | Which approved bytes may governed clients consume? | Release binding plus `data/published/` | Public-safe released bytes; not stored here |

### Classification test

Before moving any file containing “manifest,” answer:

1. What object family is it?
2. Which contract defines its meaning?
3. Which schema defines its shape?
4. Is it an instance, index, payload, sidecar, receipt, proof, catalog record, or release record?
5. Which authority decided its current state?
6. Which evidence, policy, rights, sensitivity, review, release, correction, and rollback references apply?
7. Which producer writes it?
8. Which consumers read it?
9. Is the proposed target accepted or still conflicted?
10. How will the old path fail safely after cutover?

If any material answer is absent, classify the move `HOLD`.

[Back to top](#top)

---

## Compatibility and retirement state model

These states are **PROPOSED documentation states**, not release, policy, runtime, or truth states.

| State | Meaning |
|---|---|
| `DOCUMENTED_COMPATIBILITY` | README explains the non-canonical boundary |
| `INVENTORY_PENDING` | Recursive payload and reference inventory is incomplete |
| `INVENTORIED` | Tracked and external material has been enumerated within a stated scope |
| `CLASSIFIED` | Every item has an object family, authority, target, and sensitivity posture |
| `BLOCKED` | Authority, target, evidence, review, or recovery is unresolved |
| `MIGRATION_READY` | Source, target, mapping, validation, review, and recovery packet is complete |
| `MIGRATING` | Governed migration is in progress for a pinned scope |
| `CUTOVER_PENDING` | Target exists but producers or consumers still depend on the old path |
| `REDIRECTED` | Approved deterministic compatibility pointer serves remaining consumers |
| `TOMBSTONED` | Path remains only as an explicit deprecated marker with no trust payload |
| `RETIRED` | No required consumer depends on the path and reviewed removal/retention criteria are closed |
| `ROLLED_BACK` | Prior compatibility state was restored after a failed migration |
| `SUPERSEDED` | A later reviewed compatibility decision replaces the current one |

The current parent state is:

```text
DOCUMENTED_COMPATIBILITY + INVENTORY_PENDING + BLOCKED
```

It is not `MIGRATION_READY`, `REDIRECTED`, `TOMBSTONED`, or `RETIRED`.

[Back to top](#top)

---

## Admission and deny-new-writes contract

<a id="guardrails"></a>

### Default rule

**Deny new trust-bearing writes under `data/manifests/` and all child compatibility lanes.**

Allowed writes are limited to:

- README improvements;
- bounded inventory records;
- migration, redirect, tombstone, correction, supersession, and rollback notes;
- validation summaries;
- reviewed compatibility indexes.

### Required response to a proposed new file

| Proposed content | Response |
|---|---|
| New release manifest | `DENY` — route to accepted release-governance lane |
| New GeoManifest sidecar | `DENY` — route to accepted artifact/release sidecar location after gates |
| New layer manifest instance | `HOLD` — classify data, registry, release, catalog, or published role |
| New UI story manifest | `DENY` — route to accepted UI/runtime/released story payload lane |
| Receipt | `DENY` — route to `data/receipts/` |
| Proof | `DENY` — route to `data/proofs/` |
| Catalog record | `DENY` — route to `data/catalog/` |
| Source record | `DENY` — route to `data/registry/` |
| Published bytes | `DENY` — require release approval and route to `data/published/` |
| Compatibility inventory or migration note | `ALLOW_FOR_REVIEW` — documentation only, no authority gain |

### Fail-closed behavior

When classification is uncertain:

- do not create the file here;
- use WORK or QUARANTINE for untrusted payloads where applicable;
- open a path/ADR/migration review;
- record `UNKNOWN` or `NEEDS VERIFICATION`;
- preserve source material and evidence references;
- avoid public exposure;
- do not infer approval from an existing neighboring README.

[Back to top](#top)

---

<a id="migration-posture"></a>

## Routing misplaced content

| Discovered content | Primary target | Required preservation |
|---|---|---|
| ReleaseManifest instance | Accepted lane under `release/` after singular/plural decision | Stable ID, digests, evidence, policy, review, correction, rollback |
| Release decision or promotion record | `release/` decision lane | Decision identity, reviewer, outcome, reason, timestamp |
| Signature or attestation packet | Accepted release signature/attestation lane | Signed payload digest, signer identity, verification evidence |
| GeoManifest instance | Accepted geo artifact/release sidecar location | Artifact digest, CRS, extent, evidence, policy, release lineage |
| Layer manifest instance | Accepted data, registry, release, catalog, or published-adjacent lane after classification | Layer ID, artifact refs, source/evidence lineage, sensitivity |
| UI StoryManifest | Accepted UI/runtime/released story path | Story ID, node ordering, policy, accessibility, release linkage |
| Receipt | `data/receipts/` | Run ID, spec hash, tool version, inputs, outcome |
| Proof | `data/proofs/` | Evidence refs, digests, validation method, closure scope |
| Catalog record | `data/catalog/` | Catalog identity, source role, temporal/spatial scope, provenance |
| Source record | `data/registry/` | Source identity, authority role, rights, admission state |
| Published payload | `data/published/` only after release gates | Release ID, manifest refs, digests, sensitivity transform, rollback target |
| Contract | `contracts/` | Semantic identity and inbound links |
| Schema | `schemas/` | `$id`, version, references, fixtures, validator parity |
| Policy | `policy/` | Rule identity, scope, decisions, tests |
| Code or workflow | Owning implementation or `.github/workflows/` root | Behavior, tests, permissions, rollback |
| Unknown or sensitive material | WORK / QUARANTINE or approved restricted store | Original bytes, reason, access controls, review state |

No target is canonical merely because it appears in this table. Conflicted targets remain `HOLD` until accepted.

[Back to top](#top)

---

## Consumer and inbound reference inventory

Before redirecting, tombstoning, or retiring any path, inventory:

- repository Markdown links;
- contracts and schema metadata;
- fixtures and tests;
- validator paths;
- workflow commands and path filters;
- Makefile and script targets;
- package, connector, pipeline, and runtime code;
- example and tutorial paths;
- release manifests, candidates, corrections, rollback cards, and changelogs;
- catalog, proof, receipt, registry, and published records;
- generated files and build artifacts;
- Git LFS pointers;
- external object stores and databases;
- deployment configuration;
- public URLs, CDN aliases, caches, service workers, bookmarks, and client state;
- downstream repositories and consumers;
- incident, audit, and retention requirements.

### Minimum inventory record

```yaml
compatibility_path: data/manifests/<lane>
inventory_revision: <commit>
inventory_method:
  tracked_tree: NOT_RUN
  git_history: NOT_RUN
  indexed_search: PASS
  external_stores: NOT_RUN
items: []
inbound_references: []
producers: []
consumers: []
public_or_cache_refs: []
sensitive_material: UNKNOWN
outcome: HOLD
```

The template is **PROPOSED** documentation guidance, not an accepted schema.

[Back to top](#top)

---

## Migration and retirement procedure

A migration must be a governed, reversible state transition.

### Phase 1 — freeze

1. Deny new trust-bearing writes.
2. Pin the source revision and current parent/child blobs.
3. Record accountable author, reviewer, and target decision.
4. Isolate sensitive or restricted material.
5. Preserve Git history and external-store references.

### Phase 2 — inventory

1. Enumerate tracked files and subdirectories.
2. Inspect Git history and prior renames.
3. Identify LFS, generated, external, and runtime material.
4. Find producers, consumers, links, caches, and public references.
5. Record `UNKNOWN` areas rather than assuming absence.

### Phase 3 — classify

1. Assign each item to an object family.
2. Resolve semantic contract and machine schema.
3. Determine authority, lifecycle, rights, sensitivity, and release state.
4. Choose an accepted target or mark `BLOCKED`.
5. Identify correction, supersession, retention, and rollback obligations.

### Phase 4 — prepare target

1. Confirm target path against Directory Rules and accepted ADRs.
2. Harden contract/schema/fixture/validator/policy surfaces where required.
3. Create target records without deleting the source.
4. Preserve stable IDs and digests.
5. Validate source-to-target mapping.

### Phase 5 — migrate and cut over

1. Execute the reviewed migration packet.
2. Update producers first or use a documented dual-write window when safe.
3. Migrate historical instances.
4. Update consumers and documentation.
5. Validate target behavior and stale-reference detection.
6. Invalidate caches and aliases where applicable.

### Phase 6 — compatibility posture

Choose one reviewed outcome:

- retain documented compatibility;
- redirect;
- tombstone;
- remove after verified cutover;
- hold because authority or consumers remain unresolved.

### Phase 7 — close

1. Record migration and validation receipts.
2. Record correction or supersession lineage.
3. Verify rollback or forward-fix posture.
4. Update drift and deprecation registers.
5. Remove temporary dual-write behavior.
6. Re-run link, consumer, release, and public-boundary checks.
7. Mark retirement only when every applicable gate is closed.

[Back to top](#top)

---

## Redirect and tombstone contract

A redirect or tombstone must not become a parallel authority.

### Redirect requirements

- stable old-path identity;
- exact accepted target;
- target object-family and authority;
- effective date;
- deprecation state;
- consumer scope;
- no embedded trust-bearing payload;
- deterministic resolution;
- no direct public exposure;
- failure behavior when the target is missing or unauthorized;
- correction, supersession, and rollback references;
- removal trigger.

### Tombstone requirements

A tombstone states that the old path is deprecated or retired. It must not:

- contain an active release object;
- duplicate a receipt, proof, catalog record, registry entry, or published payload;
- authorize release or public access;
- silently redirect to a conflicted target;
- hide unresolved consumers;
- delete history required for audit or correction.

### Removal gate

Do not remove the path until:

- recursive inventory is complete;
- no required producer writes it;
- no required consumer reads it;
- accepted targets exist;
- redirects or link updates are deployed where required;
- caches and aliases are handled;
- retention and audit obligations are satisfied;
- correction and rollback paths are tested;
- independent review is recorded when material.

[Back to top](#top)

---

<a id="evidence-ledger"></a>

<a id="rollback"></a>

## Rollback, correction, and supersession

### Documentation rollback

Revert the documentation commit to restore the prior README bytes. This changes guidance only.

### Compatibility migration rollback

A migration rollback must name:

- source revision and source path;
- target revision and target path;
- migration ID;
- item IDs and digests;
- producers and consumers affected;
- redirect/tombstone state;
- cache and alias state;
- correction and supersession records;
- recovery class;
- activation conditions;
- reversal, disablement, restore, or forward-fix steps;
- post-recovery validation.

### Release rollback

Release correction, withdrawal, supersession, alias restoration, and public rollback remain under `release/` and approved data-plane rollback mechanisms. This parent compatibility README cannot authorize them.

### Non-destructive default

Prefer:

1. retain source history;
2. copy or transform into the accepted target;
3. validate equivalence and authority;
4. cut over consumers;
5. tombstone or redirect;
6. remove only after reviewed closure.

A failed migration must not expose quarantined, sensitive, stale, unsupported, or unreleased content through the old or new path.

[Back to top](#top)

---

## Definition of done

The parent compatibility subtree is not complete merely because the README is modernized.

### Documentation complete

- [ ] Parent follows the Directory Rules section order.
- [ ] All confirmed child lanes are indexed.
- [ ] Authority and anti-collapse boundaries are explicit.
- [ ] Current conflicts and unknowns remain visible.
- [ ] Relative links and legacy anchors resolve.
- [ ] No documentation claims migration, retirement, release, or runtime behavior without evidence.

### Inventory complete

- [ ] Recursive tracked tree is enumerated.
- [ ] Git history and prior renames are inspected.
- [ ] LFS, generated, external, restricted, and runtime stores are checked.
- [ ] Every item is classified.
- [ ] Producers, consumers, links, caches, and public references are inventoried.

### Migration ready

- [ ] Accepted targets exist for every item.
- [ ] Manifest-family contracts and schemas are adequate.
- [ ] Fixtures, validators, policy, and release gates exist where applicable.
- [ ] Source and target identities and digests are pinned.
- [ ] Sensitive handling is approved.
- [ ] Consumer cutover and stale-reference checks are defined.
- [ ] Recovery packet and reviewers are recorded.

### Retirement complete

- [ ] Migration executed and verified.
- [ ] Producers no longer write the old path.
- [ ] Consumers no longer require the old path.
- [ ] Redirect or tombstone behavior is tested where retained.
- [ ] Caches and aliases are invalidated or updated.
- [ ] Correction and supersession lineage is recorded.
- [ ] Rollback or forward-fix path is rehearsed as required.
- [ ] Deprecation and drift registers are updated.
- [ ] No public client reads the compatibility subtree.
- [ ] Reviewed state is `RETIRED`, not inferred from file absence.

[Back to top](#top)

---

## No-loss ledger

| v0.1 material | v0.2.0 disposition |
|---|---|
| Non-canonical parent posture | Preserved and strengthened |
| Release governance belongs outside `data/manifests/` | Preserved, with singular/plural conflict made explicit |
| Receipt/proof/catalog/publication separation | Preserved and expanded to registry, policy, schema, runtime, and published bytes |
| Accepted compatibility-only content | Preserved and formalized |
| Exclusion list | Preserved and expanded by manifest family |
| Migration posture | Preserved and replaced with phased governed procedure |
| Guardrails | Preserved as deny-new-writes contract |
| Evidence ledger | Preserved as evidence snapshot, status matrix, and bounded inventory |
| Validation checklist | Preserved and expanded with finite outcomes |
| Rollback | Preserved and separated into documentation, compatibility migration, and release rollback |
| Owner placeholders | Replaced by verified CODEOWNERS routing plus stewardship uncertainty |
| Child topology | Added from five current direct child READMEs |
| Manifest terminology | Added to prevent cross-family authority collapse |
| Consumer cutover and tombstone rules | Added |
| Retirement definition of done | Added |
| Historical stub identity | Preserved in metadata |

[Back to top](#top)

---

## Open verification register

- [ ] Obtain a recursive tracked inventory of `data/manifests/`.
- [ ] Inspect Git history, prior renames, deleted files, and historical branches for manifest payloads.
- [ ] Inspect Git LFS, generated artifacts, external object stores, databases, and restricted systems.
- [ ] Confirm whether direct children beyond `geo`, `layers`, `release`, `flora`, and `story` exist.
- [ ] Confirm whether any child contains trust-bearing files beyond documentation.
- [ ] Resolve `release/manifest/` versus `release/manifests/` through reviewed decision and migration.
- [ ] Confirm the accepted instance home for `ReleaseManifest`.
- [ ] Confirm the accepted instance and sidecar home for `KFMGeoManifest`.
- [ ] Resolve data LayerManifest, release bridge, registry, catalog, and published-adjacent placement.
- [ ] Confirm UI `StoryManifest`, story payload, story catalog, and story release-manifest placement.
- [ ] Harden applicable semantic contracts and machine schemas.
- [ ] Add valid, invalid, denied, held, stale, correction, and rollback fixtures where required.
- [ ] Implement or verify validators declared by manifest schemas.
- [ ] Verify policy and promotion-gate wiring.
- [ ] Inventory every producer and consumer of parent and child paths.
- [ ] Inventory Markdown links, workflow filters, tests, examples, scripts, packages, and runtime references.
- [ ] Inventory public URLs, aliases, caches, service workers, and CDN references.
- [ ] Define stable compatibility-path and migration IDs.
- [ ] Define a machine-readable migration packet only after the contract is accepted.
- [ ] Define redirect and tombstone shapes, owning root, and tests.
- [ ] Define stale-reference detection and fail-closed resolution.
- [ ] Confirm rights, sensitivity, retention, deletion, and audit requirements.
- [ ] Confirm correction, withdrawal, supersession, and rollback integration.
- [ ] Define cache and alias invalidation procedures.
- [ ] Populate deprecation and drift registers for the subtree.
- [ ] Confirm accountable stewards and independent approval requirements.
- [ ] Verify branch protection or ruleset requirements.
- [ ] Rehearse migration rollback for representative child lanes.
- [ ] Verify no public client or normal UI route reads `data/manifests/`.
- [ ] Decide whether the parent is retained, redirected, tombstoned, or removed.
- [ ] Revisit this README after the first accepted migration packet or retirement decision.

[Back to top](#top)

---

## Changelog

### v0.2.0 — 2026-07-24

- Reorganized the parent README to the Directory Rules folder contract.
- Reconciled the parent with five repository-grounded child compatibility READMEs.
- Corrected the prior overstatement that `release/manifests/` is already canonical.
- Made the singular/plural release-manifest conflict visible.
- Added manifest-family terminology and authority routing.
- Added deny-new-writes, finite validation outcomes, compatibility states, consumer inventory, migration, redirect, tombstone, rollback, and definition-of-done contracts.
- Replaced unsupported owner certainty with verified GitHub routing and visible stewardship gaps.
- Preserved the same path, historical stub identity, legacy anchors, no-loss ledger, and non-publication boundary.

### v0.1 — 2026-06-25

- Expanded the greenfield stub into a non-canonical compatibility and retirement note.
- Established receipt/proof/catalog/publication separation.
- Directed release-governance records away from the data root.
- Preserved the prior stub as the documentation rollback target.

<p align="right"><a href="#top">Back to top</a></p>
