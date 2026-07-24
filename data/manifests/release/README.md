<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/data-manifests-release-readme
title: data/manifests/release/ — Non-Canonical Release-Manifest Compatibility and Retirement Lane
type: README; per-directory-readme; compatibility-lane; retirement-boundary; release-manifest-routing-index
version: v0.2.0
status: draft; repository-grounded; non-canonical; compatibility-only; exact-path-readme-confirmed; trust-bearing-payloads-unestablished; parent-conflict-confirmed; release-manifest-lanes-conflicted; release-contract-draft; release-schema-stub-confirmed; validator-absent; fixtures-unestablished; ADR-0011-proposed; retirement-unresolved; non-release; non-publication
owner: NEEDS VERIFICATION — CODEOWNERS routes this path through the repository default owner @bartytime4life; accountable release, manifest, data, evidence, catalog, policy, security, correction, rollback, and documentation stewardship plus independent approval were not established
created: NEEDS VERIFICATION — a greenfield stub existed before v0.1
updated: 2026-07-24
supersedes: v0.1 documentation at the same path; no ReleaseManifest, release decision, promotion record, signature, receipt, proof, catalog record, source record, policy decision, released artifact, correction, rollback, or publication state is superseded
prepared_under_prompt: KFM Markdown Modernization & GitHub Documentation Implementation Agent v4.0.0
policy_label: repository-facing; data; manifests; release; compatibility; retirement; authority-separation; evidence-aware; correction-aware; rollback-aware; release-gated; fail-closed; non-publisher
current_path: data/manifests/release/README.md
owning_root: data/
responsibility: bound and retire a non-canonical compatibility path without allowing it to become a ReleaseManifest collection, release-decision surface, signature store, receipt, proof, catalog, published-artifact, source-registry, policy, runtime, or publication authority
truth_posture: >
  CONFIRMED same-path target; non-canonical parent data/manifests compatibility lane; data-root conflict between data/manifests and release manifests;
  release/ as the release-governance root; both release/manifest and release/manifests draft lanes; ADR-0011 effective status proposed;
  ReleaseManifest semantic contract; Draft 2020-12 schema stub requiring only id; absent declared validator and unestablished fixtures;
  exact-path bounded search returning this README only; and current CODEOWNERS routing / PROPOSED compatibility states, routing matrix,
  redirect contract, migration sequence, validation outcomes, retirement gates, correction/rollback links, and definition-of-done contract /
  UNKNOWN exhaustive recursive directory inventory, historical payloads, release-manifest instance inventory, signature and signing operation,
  candidate assembly, promotion execution, published artifact inventory, producer and consumer adoption, public runtime verification, deployment parity,
  and production effects / NEEDS VERIFICATION final singular-versus-plural release-manifest home, accepted ReleaseManifest profile,
  complete fixture and validator implementation, policy and promotion-gate wiring, migration/retirement decision, inbound-reference inventory,
  branch/ruleset enforcement, accountable stewardship, independent review, correction propagation, alias invalidation, and rollback rehearsal
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  target_prior_blob: 6bf84d2616022fce28a8a0e6fa3e5b827d3fe800
  historical_stub_blob: d30b3fce038248d88f1c6c8561b04ede10a4e09e
  parent_manifests_readme_blob: c4cdbf0c0038f737447a7dc173f0fe49ef62490e
  data_readme_blob: fb7b0acfaea25b630a3042f24cb97558a996d05a
  release_readme_blob: 0752610b1df6d11143158f6f162f65ecd650e6a6
  release_manifest_singular_readme_blob: 6014cfc0f8394a44167f4226975b74f94f3b2a03
  release_manifests_plural_readme_blob: c699a527ff11bebad6a874ed1a37aa3a8213b86c
  adr_0011_blob: 40b0f47b87d584040803ed76aa6b31f5204b7fca
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  release_manifest_contract_blob: 9ca1c9d4a5b247196aa84a31a158fe734c8a6720
  release_manifest_schema_blob: 727db0a781900aa3816dcdce723fe355fec2e786
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  declared_validator_status: ABSENT at tools/validators/release/validate_release_manifest.py
  declared_fixture_readme_status: ABSENT at fixtures/release/release_manifest/README.md
  exact_path_search_result: bounded search returned data/manifests/release/README.md only
  inspection_method: exact GitHub file reads, bounded repository search, exact-path search, branch-name search, and open-PR overlap search; no clone, recursive Git tree, workflow logs, signing system, public endpoint, deployment, or production store was inspected
related:
  - ../README.md
  - ../../README.md
  - ../../published/README.md
  - ../../receipts/README.md
  - ../../proofs/README.md
  - ../../catalog/README.md
  - ../../registry/README.md
  - ../../../release/README.md
  - ../../../release/manifest/README.md
  - ../../../release/manifests/README.md
  - ../../../contracts/release/release_manifest.md
  - ../../../schemas/contracts/v1/release/release_manifest.schema.json
  - ../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../.github/CODEOWNERS
notes:
  - "v0.2.0 is a same-path documentation-only modernization grounded in current repository evidence."
  - "The first twelve H2 sections follow the Directory Rules folder-README contract."
  - "This path remains compatibility-only; no ReleaseManifest, release decision, signature, receipt, proof, catalog record, source record, released artifact, correction, rollback, or publication record is admitted here."
  - "ADR-0011 remains proposed and is not accepted by this README."
  - "The ReleaseManifest contract and schema stub exist, but the declared validator is absent and fixtures were not established."
  - "Static badges summarize inspected repository state only; they are not evidence of validation, review, signing, promotion, release, publication, retirement, correction, or runtime behavior."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/manifests/release/` — Non-Canonical Release-Manifest Compatibility and Retirement Lane

> **One-line purpose.** Keep the existing `data/manifests/release/` path fail-closed as a compatibility and retirement surface while routing release manifests, decisions, signatures, receipts, proofs, catalogs, published bytes, and source records to their actual responsibility roots.

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#status)
[![Authority: compatibility only](https://img.shields.io/badge/authority-compatibility%20only-b42318?style=flat-square)](#authority-level)
[![Exact-path payloads: not established](https://img.shields.io/badge/exact--path%20payloads-not%20established-6e7781?style=flat-square)](#status)
[![Release lanes: conflicted](https://img.shields.io/badge/release%20manifest%20lanes-conflicted-b42318?style=flat-square)](#manifest-lane-conflict)
[![ADR-0011: proposed](https://img.shields.io/badge/ADR--0011-proposed-d4a72c?style=flat-square)](#adrs)
[![Release schema: stub](https://img.shields.io/badge/ReleaseManifest%20schema-stub-f59e0b?style=flat-square)](#releasemanifest-object-boundary)
[![Validator: absent](https://img.shields.io/badge/declared%20validator-absent-b42318?style=flat-square)](#validation)
[![Publisher: no](https://img.shields.io/badge/publisher-no-6e7781?style=flat-square)](#authority-level)
[![Reviewed: 2026-07-24](https://img.shields.io/badge/reviewed-2026--07--24-0969da?style=flat-square)](#last-reviewed)

> [!IMPORTANT]
> **Safe current conclusion:** this compatibility path and README exist. The parent `data/manifests/` lane is documented as non-canonical, and the current data-root documentation records a conflict with release manifests. Bounded exact-path search returned only this README. No admissible evidence reviewed here establishes ReleaseManifest instances, decisions, signatures, release records, published artifacts, redirects, or an operational retirement under this path.

> [!CAUTION]
> The repository contains a draft `ReleaseManifest` semantic contract and a permissive Draft 2020-12 schema stub, but the declared validator is absent and fixtures were not established. A schema file, manifest-shaped JSON object, README, pull request, signature, or green readiness workflow does not prove a release package is complete, reviewed, signed, approved, published, or recoverable.

> [!WARNING]
> Do not use this lane as a shortcut around `release/`, `data/published/`, `data/receipts/`, `data/proofs/`, `data/catalog/`, or `data/registry/`. Promotion is a governed state transition, not a file move, and public clients must not read this internal compatibility path.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed) · [Topology](#current-bounded-topology) · [Families](#artifact-family-and-authority-matrix) · [Release object](#releasemanifest-object-boundary) · [Lane conflict](#manifest-lane-conflict) · [States](#compatibility-and-retirement-state-model) · [Routing](#routing-misplaced-content) · [Guardrails](#anti-collapse-guardrails) · [Evidence](#compatibility-evidence-ladder) · [Migration](#migration-and-retirement-procedure) · [Rollback](#rollback-correction-and-supersession) · [Done](#definition-of-done) · [Open verification](#open-verification-register)

---

<a id="boundary"></a>

## Purpose

`data/manifests/release/` is a **non-canonical compatibility and retirement lane** beneath the canonical `data/` responsibility root.

It exists to prevent a tracked historical path from silently becoming any of the following:

- a canonical `ReleaseManifest` collection;
- a release-decision or promotion-decision surface;
- a signing or signature-packet store;
- a process-receipt lane;
- a proof or evidence-closure lane;
- a STAC, DCAT, PROV, or domain-catalog lane;
- a source registry;
- a published artifact store;
- a correction, withdrawal, or rollback authority;
- a policy, runtime, or public-client interface.

The lane may document compatibility, inventory, redirect, migration, and retirement work. It does not authorize that work merely by describing it.

The KFM lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A `ReleaseManifest` may bind a release package. It does not itself create evidence, approve policy, execute promotion, move bytes, or grant public access.

## Authority level

**Compatibility guidance only; non-canonical, non-release, non-evidence, non-catalog, non-source, non-policy, and non-publication authority.**

| Question | Controlling authority | Role of this lane |
|---|---|---|
| What does `ReleaseManifest` mean? | [`contracts/release/release_manifest.md`](../../../contracts/release/release_manifest.md) | Links to the semantic contract; does not redefine it |
| What machine shape is valid? | [`schemas/contracts/v1/release/release_manifest.schema.json`](../../../schemas/contracts/v1/release/release_manifest.schema.json) or an accepted successor | Records current stub maturity; does not become a schema home |
| Which lane stores ReleaseManifest records? | Accepted decision resolving `release/manifest/` versus `release/manifests/` | Records the conflict; does not decide it |
| What policy permits release? | `policy/` and governed decisions | Carries pointers only |
| What evidence supports released claims? | `EvidenceRef`, `EvidenceBundle`, proof records, and source records | Requires resolvable support; cannot manufacture closure |
| What process occurred? | `data/receipts/` | May point to receipts; cannot replace them |
| What proves integrity or release support? | `data/proofs/` and governed validation | May point to proof support; cannot become proof storage |
| What catalogs the released outputs? | `data/catalog/` | May point to catalog records; cannot become a catalog |
| Where do released bytes live? | `data/published/` after release approval | Must not store or expose artifact bytes |
| Who decides release state? | `release/` governance records and accountable review | This lane has no approval authority |
| What is corrected, withdrawn, superseded, or rolled back? | `release/` correction, withdrawal, supersession, and rollback records | May preserve redirect lineage only |
| What may public clients consume? | Governed APIs and approved released artifacts | Never this compatibility path |

### Authority invariants

This lane must not:

1. create a second release root;
2. turn a compatibility note into a manifest registry;
3. treat a schema-valid object as release-complete;
4. treat a release manifest as a payload store;
5. treat a signature as policy or review approval;
6. treat a receipt as proof;
7. treat proof support as a release decision;
8. treat a catalog entry as publication;
9. treat bytes under `data/` as released by location alone;
10. resolve the singular/plural manifest conflict without an accepted decision and migration.

<a id="repo-fit"></a>

## Status

### Repository-grounded status matrix

| Surface | Current evidence | Safe conclusion |
|---|---|---|
| This README | Present at the same path | **CONFIRMED — compatibility documentation** |
| Parent `data/manifests/` | Present and explicitly non-canonical | **CONFIRMED — compatibility debt** |
| `data/` root | Canonical lifecycle root; records `data/manifests` conflict | **CONFIRMED — does not authorize manifest authority here** |
| `release/` root | Release-governance root with visible readiness holds | **CONFIRMED — governance documentation** |
| `release/manifest/` | Draft singular lane | **CONFIRMED — candidate lane, not canonicalized** |
| `release/manifests/` | Draft plural collection lane | **CONFIRMED — candidate lane, not canonicalized** |
| Singular/plural canonical choice | Both READMEs defer the decision | **CONFLICTED / NEEDS VERIFICATION** |
| ADR-0011 | Indexed with effective status `proposed` | **CONFIRMED record; decision unaccepted** |
| ReleaseManifest semantic contract | Draft v0.2 contract | **CONFIRMED — target semantics** |
| ReleaseManifest schema | Draft 2020-12 stub; requires only `id`; additional properties allowed | **CONFIRMED — thin machine shape** |
| Declared ReleaseManifest validator | Direct fetch returned not found | **ABSENT in checked path** |
| Declared ReleaseManifest fixture README | Direct fetch returned not found | **ABSENT in checked path** |
| ReleaseManifest instances under this exact path | Bounded exact-path search returned this README only | **NOT ESTABLISHED; not a recursive attestation** |
| Release automation | Release root documents readiness holds | **HOLD; operational release machinery not established** |
| GitHub ownership routing | Repository default routes this path to `@bartytime4life` | **CONFIRMED routing; stewardship unverified** |
| Retirement decision | No accepted migration or retirement decision inspected | **NEEDS VERIFICATION** |
| Production release/runtime parity | Not inspected | **UNKNOWN** |
| Release or publication authority | Not owned by this path | **DENIED by boundary** |

### Current posture

The allowed posture is **compatibility-only and fail-closed**:

- no new trust-bearing records;
- no release decisions;
- no signing records;
- no published bytes;
- no mutable release aliases;
- no public routes;
- no canonical registry behavior;
- no silent retirement;
- no inferred migration completion.

<a id="accepted-contents"></a>

## What belongs here

Until a reviewed migration or retirement decision closes the path, allowable content is limited to non-authoritative compatibility material:

- this README;
- a bounded inventory of historical files found at this exact path;
- stable redirect or crosswalk notes;
- migration maps from old identity to new identity;
- deprecation and sunset notices that cite the governing decision;
- checksums of historical compatibility files when needed to preserve migration evidence;
- references to the owning release, receipt, proof, catalog, published, registry, contract, schema, policy, correction, and rollback records;
- sanitized validation summaries proving that redirect or retirement rules behave as intended;
- no-loss ledgers showing what moved, what remained, and why;
- rollback instructions for the compatibility redirect or path retirement.

Every allowed file must state:

- that this path is non-canonical;
- its intended audience;
- its controlling decision or open decision;
- whether it is `PROPOSED`, `ACTIVE_COMPATIBILITY`, `DEPRECATED`, `REDIRECT_ONLY`, `READY_TO_RETIRE`, `RETIRED`, or `BLOCKED`;
- what it may and may not be used to infer;
- where the authoritative record lives;
- how to correct or roll back the compatibility state.

<a id="exclusions"></a>

## What does not belong here

Do not store trust-bearing or operational records under `data/manifests/release/`.

### Release governance

- `ReleaseManifest` instances;
- release candidates;
- release reviews or `ReviewRecord` instances;
- `PromotionDecision` records;
- approval or denial records;
- rollback cards;
- withdrawal notices;
- correction or supersession notices;
- signature packets or signoff records;
- release changelogs;
- mutable release aliases.

### Data and trust artifacts

- RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED payloads;
- public-safe released artifacts;
- PMTiles, COGs, GeoParquet, GeoJSON, tiles, exports, reports, or API payloads;
- process receipts;
- proof packs, integrity bundles, or evidence-closure records;
- STAC, DCAT, PROV, or domain-catalog records;
- source descriptors or registry records.

### Definitions and implementation

- semantic contracts;
- machine schemas;
- policy rules or bundles;
- fixtures;
- validator or test code;
- release assembly or promotion code;
- application, API, UI, MapLibre, runtime, package, connector, or pipeline code;
- secrets, signing keys, tokens, credentials, private endpoints, or protected operational details.

### Prohibited claims

A file in this lane must not claim, merely from presence, that:

- a release was assembled;
- a manifest is complete;
- review occurred;
- policy allowed release;
- a signature is valid;
- evidence closure succeeded;
- release state changed;
- bytes were published;
- a public alias points to the correct release;
- correction or rollback was exercised;
- the compatibility path is retired.

## Inputs

Compatibility and retirement work may consume pointers to the following evidence:

| Input | Minimum requirement |
|---|---|
| Directory Rules or accepted placement decision | Identifies the responsibility-root boundary |
| ADR-0011 or accepted successor | Defines receipt/proof/catalog/release separation |
| Manifest-lane decision | Resolves singular versus plural release-manifest home |
| ReleaseManifest contract and schema | Defines current semantics and machine-shape maturity |
| Historical exact-path inventory | Lists every tracked compatibility item with blob identity |
| Inbound-reference inventory | Identifies links, code, workflows, registries, docs, and external consumers |
| Release records | Stable manifest, decision, correction, withdrawal, rollback, and signature pointers |
| Data-plane records | Stable published, receipt, proof, catalog, and registry pointers |
| Policy and sensitivity review | Constrains public or restricted handling |
| Migration packet | Defines source, destination, transforms, checksums, validation, and recovery |
| Validation evidence | Proves routing, redirect, and negative-path behavior in a named revision |
| Rollback target | Restores the prior path or compatibility state without losing history |

Inputs must be pinned by path, commit, digest, record identifier, or release identifier where material. “Current,” “latest,” or “move everything” is insufficient.

## Outputs

This lane may produce only compatibility-control outputs:

- updated README guidance;
- a historical inventory;
- a redirect map;
- a path-deprecation notice;
- a migration crosswalk;
- a no-loss ledger;
- a reference audit;
- a sanitized validation summary;
- a compatibility-state decision;
- a rollback plan for the compatibility mechanism;
- a retirement readiness report.

| Output | What it may prove | What it does not prove |
|---|---|---|
| Compatibility README | Boundary is documented | Boundary is enforced |
| Inventory | Named files were observed | Inventory is recursively complete unless tree evidence proves it |
| Redirect map | Intended destinations are recorded | Destinations are canonical, valid, or available |
| Link audit | Selected references were checked | External consumers migrated |
| Migration crosswalk | Identity mapping is specified | Bytes or records were moved |
| Validation summary | Named checks ran in a named revision | Release or publication occurred |
| Retirement readiness report | Preconditions were assessed | Path was retired |
| Git commit or PR | Repository text changed | A release record was approved or applied |

This lane never emits release authority or publication authority.

<a id="validation-checklist"></a>

## Validation

Validation must be fail-closed and must distinguish documentation from implementation.

### Required documentation checks

- path remains `data/manifests/release/`;
- metadata marks the lane non-canonical;
- first twelve README sections follow Directory Rules;
- all links resolve to current repository paths;
- legacy anchors remain available;
- manifest-lane conflict is visible;
- ADR statuses are not promoted;
- owner placeholders are not converted into unverified executable teams;
- no trust-bearing payload is embedded;
- no release or publication claim is inferred.

### Compatibility checks

| Check | Expected result |
|---|---|
| Exact-path inventory | Every tracked item is classified or the inventory is explicitly bounded |
| Authoritative destination | Destination is identified by accepted decision, or conflict remains `BLOCKED` |
| Stable identity | Old and new path or record identities remain linked |
| Digest preservation | Content digests or Git identities are retained where needed |
| Reference audit | Internal references are updated or intentionally redirected |
| Negative-path test | New trust-bearing files in this lane are rejected |
| Public-path test | Governed clients cannot consume this path directly |
| Release-authority test | This lane cannot create or change release state |
| Receipt/proof/catalog split | Records route to their owning lanes |
| Published-byte test | Artifact bytes cannot be served from this lane |
| Correction path | Incorrect routing can be superseded visibly |
| Rollback test | Previous compatibility behavior can be restored in a named test context |
| Retirement test | Removal occurs only after zero required inbound references or reviewed exceptions |

### ReleaseManifest maturity checks

Current bounded evidence establishes only a thin schema. Before any actual ReleaseManifest record is treated as operational, verify:

- the semantic contract is reviewed;
- the schema is hardened beyond the permissive stub;
- valid, invalid, edge, correction, withdrawal, and rollback fixtures exist;
- the declared validator exists and fails closed;
- policy tests cover allow, deny, hold, and restricted cases;
- evidence and source references resolve;
- review and decision records are accountable;
- signatures or attestations are digest-bound where required;
- correction and rollback links resolve;
- candidate assembly and promotion behavior are tested;
- public clients consume only approved released artifacts through governed interfaces.

### Finite outcomes

Use only these documentation-validation outcomes:

| Outcome | Meaning |
|---|---|
| `PASS` | All applicable named checks passed with evidence |
| `FAIL` | A required invariant was violated |
| `HOLD` | Evidence or authority is incomplete; no migration or retirement proceeds |
| `NOT_APPLICABLE` | Check is explicitly irrelevant with reason |
| `NOT_RUN` | Check was not executed and must not be implied |
| `ERROR` | Validation could not complete reliably |

A missing destination decision, unresolved singular/plural conflict, absent validator, missing fixture coverage, or unknown inbound dependency is a `HOLD`, not a soft pass.

## Review burden

Review scales with authority, public consequence, sensitivity, and reversibility.

| Change | Minimum review posture |
|---|---|
| README wording only | Documentation review and evidence check |
| Compatibility inventory | Data and release lane review |
| Redirect or alias | Release, data, API/runtime, and correction review |
| Manifest record migration | Release, data, evidence, policy, and manifest review |
| Signature or signing-record migration | Release, security, and signing review |
| Receipt/proof/catalog rerouting | Owners of every affected responsibility root |
| Published artifact rerouting | Release, data, public-interface, and rollback review |
| Sensitive or rights-constrained material | Policy/sensitivity and affected-domain review |
| Path deletion or retirement | Architecture, data, release, docs, and rollback review |
| Breaking inbound-reference change | Every affected producer and consumer |
| Public-client behavior | Governed API, UI/MapLibre, release, policy, and security review |

CODEOWNERS routing is not proof that review occurred. A material migration should separate authoring, approval, execution, and verification when repository maturity supports it.

## Related folders

| Location | Relationship |
|---|---|
| [`../`](../README.md) | Parent non-canonical manifests compatibility lane |
| [`../../`](../../README.md) | Canonical data lifecycle root |
| [`../../published/`](../../published/README.md) | Released public-safe artifact bytes after approval |
| [`../../receipts/`](../../receipts/README.md) | Process and validation memory |
| [`../../proofs/`](../../proofs/README.md) | Evidence/proof support |
| [`../../catalog/`](../../catalog/README.md) | Discovery and interchange records |
| [`../../registry/`](../../registry/README.md) | Source and governed registries |
| [`../../../release/`](../../../release/README.md) | Release-governance responsibility root |
| [`../../../release/manifest/`](../../../release/manifest/README.md) | Draft singular manifest lane |
| [`../../../release/manifests/`](../../../release/manifests/README.md) | Draft plural manifest collection lane |
| [`../../../contracts/release/release_manifest.md`](../../../contracts/release/release_manifest.md) | ReleaseManifest semantic meaning |
| [`../../../schemas/contracts/v1/release/release_manifest.schema.json`](../../../schemas/contracts/v1/release/release_manifest.schema.json) | Current thin machine-shape stub |
| [`../../../docs/doctrine/directory-rules.md`](../../../docs/doctrine/directory-rules.md) | Placement doctrine |
| [`../../../.github/CODEOWNERS`](../../../.github/CODEOWNERS) | GitHub review routing only |

## ADRs

### ADR-0011

[`ADR-0011`](../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md) is present and indexed with effective status `proposed`.

It proposes explicit separation among:

```text
receipt != proof != catalog != release decision != published artifact
```

It also proposes the plural `release/manifests/` collection as the target ReleaseManifest lane and treats `data/manifests/` as compatibility debt. Because its status remains proposed, this README may document and prepare a reversible migration but must not claim the target is accepted.

### Required decision before retirement

Retirement or authoritative redirection requires a reviewed decision that resolves:

1. whether `release/manifest/`, `release/manifests/`, or a distinct split is canonical;
2. whether any ReleaseManifest records exist at this compatibility path;
3. how identities, digests, signatures, reviews, corrections, and rollback links migrate;
4. whether compatibility redirects are required;
5. how public and internal consumers are verified;
6. how the path is rolled back if references break.

### ADR triggers

Create or update an ADR when a change:

- resolves the singular/plural manifest-home conflict;
- creates a new release-record family or root;
- changes the responsibility split among release, data, proof, receipt, catalog, or published artifacts;
- changes public-client trust or release binding;
- changes signature or attestation authority;
- retires a compatibility path used by multiple systems;
- intentionally bends an existing KFM invariant.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-24 |
| Review status | Repository-grounded v0.2.0 compatibility modernization |
| Current maturity | README confirmed; exact-path payloads unestablished; manifest lanes conflicted; contract draft; schema stub; validator and fixtures absent |
| Current authority | Compatibility guidance only |
| Next review trigger | Accepted manifest-lane decision, first concrete ReleaseManifest validator/fixture set, exact-path payload discovery, redirect implementation, migration packet, or retirement proposal |

---

<a id="migration-posture"></a>

## Current bounded topology

```text
data/
└── manifests/                 # non-canonical compatibility lane
    └── release/
        └── README.md          # this compatibility boundary

release/                       # release-governance root
├── manifest/
│   └── README.md              # draft singular lane
└── manifests/
    └── README.md              # draft plural collection lane
```

This is a bounded named-path topology, not a recursive tree or payload inventory.

### What the topology proves

- the compatibility README exists;
- the parent compatibility README exists;
- both singular and plural release-manifest README lanes exist;
- the manifest-home decision remains unresolved.

### What the topology does not prove

- any ReleaseManifest instance exists;
- either release lane is canonical;
- schemas or contracts are accepted;
- validation is operational;
- signatures or attestations exist;
- candidate assembly or promotion is executable;
- a published artifact is bound to a manifest;
- retirement can proceed safely.

## Artifact family and authority matrix

| Family | Primary question | Owning surface | Forbidden collapse |
|---|---|---|---|
| ReleaseManifest semantic contract | What does a release manifest mean? | `contracts/release/` | Contract is not instance or approval |
| ReleaseManifest machine shape | What structure is accepted? | `schemas/contracts/v1/release/` | Schema validity is not release readiness |
| Release manifest instance | What package and release state are bound? | Accepted lane under `release/` | Instance is not payload |
| Promotion decision | May the transition proceed? | Release/policy decision surface | Decision is not manifest or receipt |
| Review record | Who reviewed what and with what outcome? | Release/review governance | CODEOWNERS is not review evidence |
| Signature/attestation | Which bytes or manifest digest were signed? | Release/signature and accepted attestation surfaces | Signature is not policy approval |
| Receipt | What process ran? | `data/receipts/` | Receipt is not proof or release |
| Proof support | What validates integrity, evidence, and closure? | `data/proofs/` | Proof is not release decision |
| Catalog record | How is the object discovered and interchanged? | `data/catalog/` | Catalog is not publication |
| Published artifact | Which approved bytes may be served? | `data/published/` | Bytes are not self-authorizing |
| Source record | What source identity and role apply? | `data/registry/` | Source record is not evidence closure |
| Correction/withdrawal/rollback | How is unsafe release state changed visibly? | `release/` | No silent mutation |
| Compatibility note | How is an old path bounded and retired? | This lane | Compatibility note is not authority |

## ReleaseManifest object boundary

The semantic contract describes `ReleaseManifest` as the governed release binding for a published artifact set. It should eventually connect identity, contents, digests, evidence, source roles, policy, promotion, rights, sensitivity, review, attestations, receipts/proofs, correction lineage, rollback, and time.

Current machine-shape evidence is intentionally thin:

| Field | Current schema posture |
|---|---|
| `id` | Required string |
| `spec_hash` | Optional string |
| `version` | Optional string |
| Other fields | Allowed because `additionalProperties` is `true`, but not governed by the stub |

Therefore:

- schema validity is not manifest completeness;
- `id` presence is not release approval;
- optional `spec_hash` is not proof of correct canonicalization;
- arbitrary extra fields are not accepted semantics;
- a JSON object passing the stub may still lack evidence, policy, review, signatures, rollback, correction, and release closure;
- this compatibility lane must not host instances while the profile remains unresolved.

### Minimum mature ReleaseManifest expectations

A future accepted profile should make applicable fields explicit for:

- stable release identity;
- immutable candidate and release references;
- included artifact and record identities;
- content and manifest digests;
- schema, contract, policy, and spec versions;
- EvidenceRef and EvidenceBundle closure;
- source roles and caveats;
- rights and sensitivity posture;
- validation and proof references;
- accountable review and promotion decisions;
- signatures and attestations;
- published artifact pointers;
- correction, withdrawal, supersession, and rollback targets;
- effective, published, superseded, and withdrawn times;
- public-client consumption posture.

These are design expectations, not claims that the current stub implements them.

## Manifest lane conflict

The repository currently documents two release-manifest lanes:

| Path | Current documentation | Safe conclusion |
|---|---|---|
| `release/manifest/` | Draft singular lane | Candidate home; no canonical decision |
| `release/manifests/` | Draft plural collection lane | Candidate collection home; no canonical decision |
| `data/manifests/release/` | Non-canonical compatibility lane | Must not become a third authority |

Both release-lane READMEs recommend a possible distinction but defer to maintainers. ADR-0011 proposes plural `release/manifests/` as the ReleaseManifest collection and singular `release/manifest/` as compatibility after migration, but the ADR remains proposed.

### Fail-closed rule

Until a reviewed decision resolves the conflict:

- do not create new ReleaseManifest instances here;
- do not migrate historical records blindly to either release lane;
- do not generate redirects that imply one destination is canonical;
- do not delete historical records;
- do not change public or internal consumers;
- classify the work `BLOCKED_BY_AUTHORITY_DECISION`;
- preserve identities, digests, and inbound references for later migration.

## Compatibility and retirement state model

| State | Meaning | Allowed behavior |
|---|---|---|
| `PROPOSED` | Compatibility posture is documented but not active | Documentation and evidence gathering only |
| `ACTIVE_COMPATIBILITY` | Legacy references still depend on the path | README, redirect, crosswalk, and validation only |
| `INVENTORY_INCOMPLETE` | Recursive content or inbound references are not fully known | Hold migration and retirement |
| `BLOCKED_BY_AUTHORITY_DECISION` | Canonical destination is unresolved | No authoritative redirect or move |
| `DEPRECATED` | New use is prohibited; legacy use remains | Fail new writes; preserve reads or notices as approved |
| `REDIRECT_ONLY` | Path serves only a reviewed redirect or tombstone | No trust-bearing content |
| `READY_TO_RETIRE` | All retirement gates pass | Reviewed removal may proceed |
| `RETIRED` | Path removed through governed migration | History, correction, and rollback references retained |
| `SUPERSEDED` | A later compatibility decision replaces this one | Preserve lineage |
| `ROLLED_BACK` | Prior compatibility behavior was restored | Record why and which revision |
| `FAILED` | Migration or redirect violated an invariant | Stop and correct |
| `HOLD` | Evidence, rights, policy, review, destination, or recovery is incomplete | No transition |

These are proposed compatibility states for this README, not a repository-wide machine contract.

## Routing misplaced content

Do not move content solely by filename. Classify its responsibility first.

| Content found here | Correct handling |
|---|---|
| ReleaseManifest instance | Hold until singular/plural destination is accepted; then migrate under `release/` |
| PromotionDecision or release decision | Route to accepted decision lane under `release/` |
| ReviewRecord | Route to accepted review lane under `release/` |
| Signature or attestation packet | Route to accepted release/signature surface; preserve digest binding |
| RollbackCard | Route to release rollback-card authority |
| Correction or withdrawal notice | Route to release correction/withdrawal authority |
| Process receipt | Route to `data/receipts/`; preserve run and target linkage |
| Proof or integrity bundle | Route to `data/proofs/`; preserve evidence and digest identity |
| Catalog record | Route to matching `data/catalog/` lane |
| Published artifact bytes | Quarantine if release state is unclear; otherwise route to approved `data/published/` lane |
| SourceDescriptor or source record | Route to `data/registry/` |
| Contract | Route to `contracts/` |
| Schema | Route to `schemas/` |
| Policy rule | Route to `policy/` |
| Validator or test | Route to `tools/validators/` or `tests/` |
| Historical note | Keep only when it provides migration or compatibility evidence |
| Secret or restricted material | Stop, isolate, and follow security/incident handling |

### Classification questions

Before moving anything, answer:

1. What object family is this?
2. Which authority defines its meaning?
3. Which root owns its instance?
4. Is the object normative, emitted, derived, or historical?
5. Which stable identity and digest must remain?
6. Which references point to it?
7. Does it contain rights, sensitivity, security, or living-person concerns?
8. Which review and policy posture applies?
9. What is the correction and rollback path?
10. Which validation proves the destination did not change meaning?

<a id="guardrails"></a>

## Anti-collapse guardrails

- `ReleaseManifest` is not the release payload.
- `ReleaseManifest` is not a `PromotionDecision`.
- `ReleaseManifest` is not a process receipt.
- `ReleaseManifest` is not proof closure.
- `ReleaseManifest` is not a catalog record.
- `ReleaseManifest` is not a signature by itself.
- `ReleaseManifest` is not an EvidenceBundle.
- `ReleaseManifest` is not a public API response.
- A signature is not evidence that policy or review passed.
- A schema-valid instance is not a complete release package.
- A manifest at a familiar path is not canonical by implication.
- A move into `release/` is not approval.
- A move into `data/published/` is not publication.
- A merged PR is not an applied release transition.
- A workflow hold is not operational capability.
- A redirect is not a migration unless references, identities, validation, correction, and rollback are governed.
- A compatibility README is not authority to delete the path.
- Generated language must not fill missing release evidence.

<a id="evidence-ledger"></a>

## Compatibility evidence ladder

| Grade | Evidence | Permitted claim |
|---|---|---|
| `E0_DOCUMENTED` | README text only | Intended compatibility boundary |
| `E1_INVENTORIED` | Pinned tracked-file and reference inventory | Named repository scope observed |
| `E2_CLASSIFIED` | Every item assigned an object family and destination status | Routing plan exists |
| `E3_DECIDED` | Accepted manifest-lane and migration decision | Destination authority is resolved |
| `E4_STATIC_VALIDATED` | Links, schemas, metadata, digests, and negative paths checked | Static package is coherent |
| `E5_MIGRATION_REHEARSED` | Reversible move/redirect exercised in isolated context | Rehearsal succeeded there |
| `E6_MIGRATED` | Named migration executed with receipts | Repository transition occurred |
| `E7_REFERENCES_VERIFIED` | Internal and required external consumers verified | Adoption checks passed in scope |
| `E8_CORRECTION_READY` | Correction, supersession, and invalidation paths tested | Defects can be surfaced visibly |
| `E9_ROLLBACK_REHEARSED` | Prior compatibility behavior restored in rehearsal | Recovery was demonstrated in scope |
| `E10_RETIRED` | Path removed after gates and review | Governed retirement occurred |
| `E11_OPERATIONALLY_VERIFIED` | Runtime/public behavior and release closure observed | Operational parity supported for named system |

The current README update establishes `E0_DOCUMENTED` and bounded evidence for parts of `E1_INVENTORIED`. It does not claim higher grades.

## Migration and retirement procedure

### 1. Freeze authority growth

- prohibit new trust-bearing records;
- make the lane visibly non-canonical;
- block public reads and normal writers;
- preserve existing bytes and Git history.

### 2. Inventory the lane

Record:

- every tracked file;
- blob SHA and content digest where material;
- object-family classification;
- sensitivity and rights posture;
- current references;
- expected destination;
- disposition state;
- unresolved questions.

### 3. Inventory inbound and outbound references

Search:

- repository links and imports;
- workflows and scripts;
- contracts, schemas, policy, fixtures, validators, and tests;
- manifests, decisions, signatures, correction and rollback records;
- registries and indexes;
- public or internal clients;
- documentation and external integrations where available.

### 4. Resolve the manifest-lane decision

Do not proceed until a reviewed decision selects:

- singular;
- plural;
- or a clearly distinct singular/plural responsibility split.

The decision must also specify migration identity, compatibility window, redirect behavior, review, correction, and rollback.

### 5. Build the migration packet

Minimum packet:

```yaml
migration_id: <stable-id>
source_path: data/manifests/release/
source_revision: <commit>
source_inventory: <pinned-reference>
destination_decision: <accepted-adr-or-record>
destination_paths: []
object_mappings: []
digest_preservation: true
inbound_references: []
public_clients_affected: []
sensitivity_review: <record-or-not-applicable>
validation_plan: <record>
correction_plan: <record>
rollback_plan: <record>
review_records: []
execution_receipt: null
retirement_state: PROPOSED
```

This example is proposed documentation guidance, not a verified machine schema.

### 6. Rehearse

In an isolated context:

- apply the move or redirect;
- verify identities and digests;
- run link and reference checks;
- run valid and invalid instance checks;
- verify no public read bypass;
- verify correction and rollback behavior;
- record `PASS`, `FAIL`, `HOLD`, `NOT_RUN`, `NOT_APPLICABLE`, or `ERROR`.

### 7. Execute the governed migration

Execution requires:

- accepted destination authority;
- complete inventory;
- reviewed packet;
- pinned revisions;
- deterministic transforms;
- validation and negative-path evidence;
- correction and rollback readiness;
- explicit authorization.

### 8. Verify adoption

Confirm:

- authoritative records exist at the accepted release lane;
- no required consumer still reads this path;
- references resolve;
- manifests preserve contents, evidence, policy, review, signatures, correction, and rollback linkage;
- public clients use governed released interfaces;
- no duplicate active authority remains.

### 9. Deprecate and retire

Retire only when:

- the compatibility window is closed;
- zero required inbound references remain, or exceptions are reviewed;
- rollback is rehearsed;
- correction and supersession records are ready;
- documentation and registries are updated;
- removal is approved and reversible.

<a id="rollback"></a>

## Rollback, correction, and supersession

Three rollback scopes must remain distinct.

### Documentation rollback

Revert this README change to restore prior documentation bytes. This does not move records or change release state.

### Compatibility-migration rollback

Restore the prior path, redirect, link map, or compatibility behavior if:

- required references break;
- identities or digests change unexpectedly;
- an object routes to the wrong responsibility root;
- policy or sensitivity obligations are lost;
- public clients bypass governed interfaces;
- duplicate authority appears;
- correction or rollback links fail.

### Release rollback

A release rollback is governed under `release/` and may require rollback cards, withdrawal or correction notices, invalidation, prior release targets, signatures, receipts, proofs, and published-alias handling. This README cannot authorize or execute it.

### Correction principles

- preserve prior records;
- use supersession rather than silent edits;
- record why routing was incorrect;
- preserve stable identities and digests;
- identify affected consumers;
- invalidate stale pointers where governed;
- keep the correction and rollback path visible.

## Definition of done

This lane is complete only when all applicable items are closed:

- [ ] Exact recursive tracked inventory is recorded.
- [ ] Historical payload and reference inventory is complete.
- [ ] Every item is classified by object family.
- [ ] The singular/plural manifest-home conflict is resolved by reviewed decision.
- [ ] ADR-0011 or an accepted successor governs the boundary.
- [ ] ReleaseManifest contract, schema, fixtures, validator, policy, and tests meet the accepted profile.
- [ ] Destination paths are verified against Directory Rules.
- [ ] Stable identities and digests are preserved.
- [ ] Inbound references are migrated or intentionally redirected.
- [ ] No trust-bearing record remains here.
- [ ] No normal writer targets this path.
- [ ] No public or internal governed client consumes this path directly.
- [ ] Release, receipt, proof, catalog, published, registry, contract, schema, and policy objects live in their own roots.
- [ ] Correction and supersession paths are recorded.
- [ ] Compatibility rollback is rehearsed.
- [ ] Release rollback remains governed separately.
- [ ] Documentation and registers are updated.
- [ ] Retirement is approved.
- [ ] The path is removed or retained only as an explicit reviewed redirect/tombstone.
- [ ] No release or publication authority is inferred from retirement.

## No-loss ledger

| v0.1 material | v0.2.0 disposition |
|---|---|
| Non-canonical purpose | Preserved and sharpened |
| Release-level manifest boundary | Preserved; singular/plural conflict made explicit |
| Release-decision boundary | Preserved |
| Receipt/proof/catalog/publication split | Preserved and expanded |
| Accepted compatibility contents | Preserved with required metadata |
| Exclusions | Preserved and expanded |
| Migration routing table | Preserved with authority-decision hold |
| Guardrails | Preserved and expanded |
| Evidence ledger | Reframed as evidence ladder and pinned snapshot |
| Validation checklist | Expanded with finite outcomes and maturity checks |
| Rollback warning | Split into documentation, compatibility, and release rollback |
| Historical stub SHA | Preserved in metadata |
| Owner placeholders | Replaced with verified GitHub routing plus stewardship uncertainty |
| Public exposure prohibition | Preserved |
| Lifecycle invariant | Added explicitly |
| Correction and supersession | Added |
| Definition of done | Added |
| Open verification | Expanded |

## Open verification register

- [ ] Obtain a recursive tracked inventory of `data/manifests/release/`.
- [ ] Confirm whether any historical ReleaseManifest, decision, signature, receipt, proof, catalog, published, or source records exist here.
- [ ] Inventory all inbound links, code references, workflows, registries, and external consumers.
- [ ] Resolve `release/manifest/` versus `release/manifests/` through reviewed decision.
- [ ] Confirm ADR-0011 acceptance, rejection, or supersession.
- [ ] Confirm the accepted ReleaseManifest identity and version grammar.
- [ ] Harden the ReleaseManifest schema beyond the permissive `id`-only stub.
- [ ] Add valid, invalid, edge, correction, withdrawal, supersession, and rollback fixtures.
- [ ] Implement or revise the declared ReleaseManifest validator.
- [ ] Add fail-closed policy and release-gate tests.
- [ ] Define manifest canonicalization and digest rules.
- [ ] Define signature and attestation requirements.
- [ ] Define accountable review and separation-of-duties requirements.
- [ ] Define candidate assembly and promotion-decision linkage.
- [ ] Define evidence, source-role, rights, sensitivity, and temporal closure requirements.
- [ ] Define correction, withdrawal, supersession, invalidation, and rollback link requirements.
- [ ] Define published artifact and alias binding.
- [ ] Define release-manifest collection indexing.
- [ ] Define redirect or tombstone behavior for this path.
- [ ] Create a migration packet with stable identity and checksums.
- [ ] Rehearse migration and compatibility rollback.
- [ ] Verify public and internal clients after migration.
- [ ] Verify branch protection or ruleset requirements.
- [ ] Confirm accountable stewards and independent approval.
- [ ] Update drift and verification registers when the decision is made.
- [ ] Retire the path only after all required gates close.

## Changelog

### v0.2.0 — 2026-07-24

- Reorganized the README to the Directory Rules folder contract.
- Grounded status in current data, release, manifest-lane, ADR, contract, schema, and CODEOWNERS evidence.
- Removed unsupported owner certainty.
- Preserved this path as compatibility-only.
- Made the singular/plural release-manifest conflict explicit.
- Recorded the ReleaseManifest contract and thin schema stub accurately.
- Recorded absent declared validator and unestablished fixture README.
- Added authority matrix, compatibility states, routing, evidence ladder, migration procedure, rollback scopes, definition of done, no-loss ledger, and open verification.
- Preserved legacy anchors and the historical stub identity.
- Changed no release, data, runtime, or publication state.

### v0.1 — 2026-06-25

- Expanded the greenfield stub into a non-canonical compatibility and retirement note.
- Routed release manifests and decisions away from the data compatibility root.
- Preserved receipt, proof, catalog, publication, correction, and rollback boundaries.

<p align="right"><a href="#top">Back to top</a></p>
