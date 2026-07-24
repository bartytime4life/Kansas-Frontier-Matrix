<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/data-manifests-geo-readme
title: data/manifests/geo/ — Non-Canonical Geo Manifest Compatibility and Retirement Lane
type: README; per-directory-readme; compatibility-lane; retirement-boundary; geo-manifest-routing-index
version: v0.2.0
status: draft; repository-grounded; non-canonical; compatibility-only; exact-path-readme-confirmed; trust-bearing-payloads-unestablished; parent-conflict-confirmed; release-lane-conflicted; geo-contract-draft; geo-schema-stub-confirmed; validator-absent; fixtures-unestablished; ADR-0011-proposed; ADR-0023-proposed; retirement-unresolved; non-release; non-publication
owner: NEEDS VERIFICATION — CODEOWNERS routes this path through the repository default owner @bartytime4life; accountable geo, data, evidence, catalog, manifest, release, policy, security, and documentation stewardship plus independent approval were not established
created: NEEDS VERIFICATION — a greenfield stub existed before v0.1
updated: 2026-07-24
supersedes: v0.1 documentation at the same path; no GeoManifest, ReleaseManifest, geospatial artifact, receipt, proof, catalog record, source record, policy decision, release state, or publication state is superseded
prepared_under_prompt: KFM Markdown Modernization & GitHub Documentation Implementation Agent v4.0.0
policy_label: repository-facing; data; geo; manifests; compatibility; retirement; authority-separation; evidence-aware; release-gated; fail-closed; non-publisher
current_path: data/manifests/geo/README.md
owning_root: data/
responsibility: bound and retire a non-canonical compatibility path without allowing it to become a GeoManifest, ReleaseManifest, proof, receipt, catalog, published-artifact, source-registry, policy, or runtime authority
truth_posture: >
  CONFIRMED same-path target; non-canonical parent data/manifests compatibility lane; data-root conflict between data/manifests and release manifests;
  release/ as the release-governance root; release/manifests as a current plural collection lane with unresolved singular/plural conflict;
  ADR-0011 and ADR-0023 effective status proposed; KFMGeoManifest semantic contract; Draft 2020-12 schema stub requiring only id;
  absent declared validator and unestablished fixtures; exact-path bounded search returning this README only; and current CODEOWNERS routing /
  PROPOSED compatibility states, routing matrix, redirect contract, migration sequence, validation outcomes, retirement gates, and definition of done /
  UNKNOWN exhaustive recursive directory inventory, historical payloads, deployed GeoManifest sidecars, release-manifest inventory, signing keys,
  DSSE/cosign/Rekor operation, published PMTiles or COG inventory, producer and consumer adoption, runtime verification, CDN parity, and production effects /
  NEEDS VERIFICATION final singular-versus-plural release-manifest home, accepted GeoManifest placement, complete fixture and validator implementation,
  policy and promotion-gate wiring, migration/retirement decision, inbound-reference inventory, branch/ruleset enforcement, accountable stewardship,
  independent review, correction propagation, alias invalidation, and rollback rehearsal
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  target_prior_blob: 3346877eaf5e5a984805ada2bb15ebcf73c6f675
  historical_stub_blob: 9e325758b6d928e735ecb6bf4217159eb03e39e8
  parent_manifests_readme_blob: c4cdbf0c0038f737447a7dc173f0fe49ef62490e
  data_readme_blob: fb7b0acfaea25b630a3042f24cb97558a996d05a
  release_readme_blob: 0752610b1df6d11143158f6f162f65ecd650e6a6
  release_manifests_readme_blob: c699a527ff11bebad6a874ed1a37aa3a8213b86c
  adr_0011_blob: 40b0f47b87d584040803ed76aa6b31f5204b7fca
  adr_0023_blob: 99a984ddde3f5569ef54443bce7798e5ac2f89d4
  adr_index_blob: cf08fae322ac53426f7394d97897fdb942253049
  geo_manifest_contract_blob: cf8e467cf32323718e38ad1510da3e5f60bef884
  geo_manifest_schema_blob: 931a0de24e45af4bc237c596c69bcaf305fb811f
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  declared_validator_status: ABSENT at tools/validators/evidence/validate_kfm_geo_manifest.py
  declared_fixture_readme_status: ABSENT at fixtures/evidence/kfm_geo_manifest/README.md
  exact_path_search_result: bounded search returned data/manifests/geo/README.md only
  inspection_method: exact GitHub file reads, bounded repository search, exact-path search, branch-name search, and open-PR overlap search; no clone, recursive Git tree, workflow logs, signing system, CDN, public endpoint, deployment, or production store was inspected
related:
  - ../README.md
  - ../../README.md
  - ../../published/README.md
  - ../../receipts/README.md
  - ../../proofs/README.md
  - ../../catalog/README.md
  - ../../registry/README.md
  - ../../../release/README.md
  - ../../../release/manifests/README.md
  - ../../../contracts/evidence/kfm_geo_manifest.md
  - ../../../schemas/contracts/v1/evidence/kfm_geo_manifest.schema.json
  - ../../../docs/adr/INDEX.md
  - ../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../docs/adr/ADR-0023-geo-manifest-signs-every-pmtiles-cog-release.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../.github/CODEOWNERS
notes:
  - "v0.2.0 is a same-path documentation-only modernization grounded in current repository evidence."
  - "The first twelve H2 sections follow the Directory Rules folder-README contract."
  - "This path remains compatibility-only; no GeoManifest, ReleaseManifest, signed sidecar, catalog record, proof, receipt, source record, or published artifact is admitted here."
  - "ADR-0011 and ADR-0023 remain proposed and are not accepted by this README."
  - "A KFMGeoManifest contract and schema stub exist, but the declared validator is absent and fixtures were not established."
  - "Static badges summarize inspected repository state only; they are not evidence of signing, validation, release, publication, retirement, or runtime behavior."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/manifests/geo/` — Non-Canonical Geo Manifest Compatibility and Retirement Lane

> **One-line purpose.** Keep the existing `data/manifests/geo/` path fail-closed as a compatibility and retirement surface while routing geospatial artifact metadata, release manifests, signatures, receipts, proofs, catalogs, published bytes, and source records to their actual responsibility roots.

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#status)
[![Authority: compatibility only](https://img.shields.io/badge/authority-compatibility%20only-b42318?style=flat-square)](#authority-level)
[![Exact-path payloads: not established](https://img.shields.io/badge/exact--path%20payloads-not%20established-6e7781?style=flat-square)](#status)
[![ADR-0011: proposed](https://img.shields.io/badge/ADR--0011-proposed-d4a72c?style=flat-square)](#adrs)
[![ADR-0023: proposed](https://img.shields.io/badge/ADR--0023-proposed-d4a72c?style=flat-square)](#adrs)
[![Geo schema: stub](https://img.shields.io/badge/GeoManifest%20schema-stub-f59e0b?style=flat-square)](#kfmgeomanifest-object-boundary)
[![Validator: absent](https://img.shields.io/badge/declared%20validator-absent-b42318?style=flat-square)](#validation)
[![Publisher: no](https://img.shields.io/badge/publisher-no-6e7781?style=flat-square)](#authority-level)
[![Reviewed: 2026-07-24](https://img.shields.io/badge/reviewed-2026--07--24-0969da?style=flat-square)](#last-reviewed)

> [!IMPORTANT]
> **Safe current conclusion:** this compatibility path and README exist. The parent `data/manifests/` lane is documented as non-canonical, and the current data-root documentation records a conflict with release manifests. Bounded exact-path search returned only this README. No admissible evidence reviewed here establishes GeoManifest payloads, signed sidecars, release manifests, public artifacts, or an operational retirement under this path.

> [!CAUTION]
> The repository does contain a draft `KFMGeoManifest` semantic contract and a permissive schema stub, but the declared validator is absent and fixtures were not established. A schema file, ADR proposal, README, signature-shaped object, pull request, or green unrelated workflow does not prove a geospatial artifact is signed, evidence-closed, policy-admitted, released, public-safe, or recoverable.

> [!WARNING]
> Do not use this lane as a shortcut around `release/`, `data/published/`, `data/receipts/`, `data/proofs/`, `data/catalog/`, or `data/registry/`. Promotion is a governed state transition, not a file move, and public clients must not read this internal compatibility path.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed) · [Topology](#current-bounded-topology) · [Families](#artifact-family-and-authority-matrix) · [Geo object](#kfmgeomanifest-object-boundary) · [Release package](#proposed-geo-release-package) · [States](#compatibility-and-retirement-state-model) · [Routing](#routing-misplaced-content) · [Guardrails](#anti-collapse-guardrails) · [Evidence](#compatibility-evidence-ladder) · [Migration](#migration-and-retirement-procedure) · [Rollback](#rollback-correction-and-supersession) · [Done](#definition-of-done) · [Open verification](#open-verification-register)

---

<a id="boundary"></a>

## Purpose

`data/manifests/geo/` is a **non-canonical compatibility and retirement lane** beneath the canonical `data/` responsibility root.

It exists to prevent a tracked historical path from silently becoming any of the following:

- the canonical home for `KFMGeoManifest` semantic meaning;
- the canonical machine-schema home for `KFMGeoManifest`;
- a `ReleaseManifest` collection;
- a signing or signature-packet store;
- a process-receipt lane;
- a proof or evidence-closure lane;
- a STAC, DCAT, PROV, or domain-catalog lane;
- a source registry;
- a published geospatial artifact store;
- a policy or release-decision surface;
- a public-client data path.

The lane may document compatibility, inventory, redirect, migration, and retirement work. It does not authorize that work merely by describing it.

The KFM lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A GeoManifest may describe or bind a geospatial derivative. It does not make that derivative true, admissible, released, or public.

## Authority level

**Compatibility guidance only; non-canonical, non-release, non-evidence, non-catalog, non-source, non-policy, and non-publication authority.**

| Question | Controlling authority | Role of this lane |
|---|---|---|
| What does `KFMGeoManifest` mean? | [`contracts/evidence/kfm_geo_manifest.md`](../../../contracts/evidence/kfm_geo_manifest.md) | Links to the semantic contract; does not redefine it |
| What machine shape is valid? | [`schemas/contracts/v1/evidence/kfm_geo_manifest.schema.json`](../../../schemas/contracts/v1/evidence/kfm_geo_manifest.schema.json) or an accepted successor | Records current stub maturity; does not become a schema home |
| What evidence supports an artifact? | `EvidenceRef`, `EvidenceBundle`, proof records, and source records | Requires resolvable support; cannot manufacture closure |
| What policy permits exposure? | `policy/` and governed decisions | Carries pointers only |
| Which process ran? | [`data/receipts/`](../../receipts/README.md) | Routes process memory; does not store receipts |
| Which proof or integrity support exists? | [`data/proofs/`](../../proofs/README.md) | Routes proof support; does not store proofs |
| How is the artifact discovered? | [`data/catalog/`](../../catalog/README.md) | Routes catalog records; does not become a catalog |
| Where are source records governed? | [`data/registry/`](../../registry/README.md) | Routes source records; does not become a registry |
| Where do released artifact bytes belong? | [`data/published/`](../../published/README.md), after governed release | Never stores published bytes |
| Where do release-governance records belong? | [`release/`](../../../release/README.md) | Points to release authority; does not decide release state |
| Where do release manifest collections currently live? | [`release/manifests/`](../../../release/manifests/README.md), with singular/plural conflict still unresolved | Does not preempt the unresolved migration decision |
| May a public client read this lane? | Governed API and released-artifact interfaces | **No** |
| May this README accept an ADR? | Reviewed ADR process and canonical ADR index | **No** |

### Authority anti-claims

This README does **not** prove that:

- the `KFMGeoManifest` profile is accepted;
- the current schema is production-grade;
- the proposed DSSE/cosign/Rekor path is implemented;
- a release-manifest singular/plural decision is closed;
- any PMTiles, COG, GeoJSON, tile package, or layer has a valid signed sidecar;
- any artifact is public-safe;
- this compatibility path is ready to delete;
- any migration or redirect has executed.

## Status

### Repository-grounded status matrix

| Surface | Current evidence | Safe conclusion |
|---|---|---|
| Target README | Present at the same path; v0.1 baseline inspected | **CONFIRMED — documentation** |
| Parent `data/manifests/` lane | Present and documented as non-canonical compatibility/retirement | **CONFIRMED — compatibility debt** |
| `data/` root | Records `data/manifests` versus release manifests as a conflict | **CONFIRMED — unresolved placement conflict** |
| Exact-path bounded search | Returned this README only | **CONFIRMED bounded result; not a recursive tree attestation** |
| `release/` root | Present as release-governance root | **CONFIRMED — authority boundary** |
| `release/manifests/` | Present as plural collection lane | **CONFIRMED — draft lane** |
| `release/manifest/` versus `release/manifests/` | Current release docs record unresolved singular/plural semantics | **CONFLICTED / NEEDS VERIFICATION** |
| ADR-0011 | Indexed with effective status `proposed` | **CONFIRMED proposal; not accepted** |
| ADR-0023 | Indexed with effective status `proposed` | **CONFIRMED proposal; not accepted** |
| `KFMGeoManifest` semantic contract | Draft v0.2 contract exists | **CONFIRMED — semantic guidance** |
| `KFMGeoManifest` schema | Draft 2020-12 stub; requires `id`, permits optional `version` and `spec_hash`, allows additional properties | **CONFIRMED — thin machine shape** |
| Declared GeoManifest validator | File not found at the schema-declared path | **CONFIRMED absent in direct fetch** |
| Declared GeoManifest fixtures | Fixture README not found at the contract-declared path | **NOT ESTABLISHED** |
| GeoManifest policy enforcement | Not inspected as executable behavior | **UNKNOWN / NEEDS VERIFICATION** |
| Signed-sidecar implementation | No signing workflow, keys, receipts, logs, or public verification inspected | **UNKNOWN** |
| Published PMTiles/COG inventory | Not recursively inspected | **UNKNOWN** |
| Migration/retirement decision | No accepted ADR or verified migration closure identified | **NEEDS VERIFICATION** |
| GitHub routing | Repository default routes to `@bartytime4life` | **CONFIRMED routing; stewardship unverified** |
| Release or publication authority | Explicitly outside this lane | **DENIED by boundary** |

### Truth labels

| Label | Meaning in this README |
|---|---|
| `CONFIRMED` | Verified from current repository bytes or bounded searches in this session |
| `PROPOSED` | Design, route, field, state, or migration not accepted and verified |
| `UNKNOWN` | Evidence is insufficient for a stronger conclusion |
| `NEEDS VERIFICATION` | A concrete check exists but remains open |
| `CONFLICTED` | Relevant current surfaces disagree or overlap |
| `DENIED by boundary` | This lane is prohibited from owning the responsibility |

<a id="accepted-contents"></a>

## What belongs here

Until an accepted path decision and governed retirement complete, this lane may contain only non-trust-bearing compatibility material:

- this README;
- a bounded inventory of historical files that were actually found here;
- migration crosswalks that map each historical item to its owning responsibility root;
- redirect or tombstone notes that preserve old-path discoverability without duplicating authority;
- deprecation notices with stable replacement pointers;
- migration validation summaries that contain no protected payloads or secrets;
- references to migration records, rollback records, correction records, or ADRs;
- a final retirement record after the path is proven empty of live trust-bearing dependencies.

Every additional file must identify:

- why compatibility requires it;
- whether it is normative or informational;
- the exact replacement path or governing record;
- the review state;
- the removal trigger;
- the rollback or restoration path.

Compatibility content must not evolve into an independent manifest specification.

<a id="exclusions"></a>

## What does NOT belong here

The following are prohibited under `data/manifests/geo/`:

- `ReleaseManifest` records or release decisions;
- `KFMGeoManifest` canonical contract or schema definitions;
- signed DSSE envelopes, signature bundles, private keys, certificates, or transparency-log credentials;
- PMTiles, MBTiles, COG, GeoTIFF, GeoJSON, FlatGeobuf, GeoParquet, tiles, rasters, vector packages, or layer bytes;
- public-safe artifact aliases or CDN deployment files;
- process, validation, generation, redaction, promotion, or rollback receipts;
- `EvidenceBundle`, proof packs, integrity proofs, citation-validation reports, or proof-side closure records;
- STAC, DCAT, PROV, `CatalogMatrix`, domain catalog, or discovery records;
- `SourceDescriptor`, source-admission, rights, or source-role registry records;
- canonical policy rules, policy bundles, access decisions, sensitivity decisions, or release decisions;
- fixtures, validators, tests, pipelines, packages, applications, runtime code, or deployment configuration;
- unredacted precise sensitive locations, living-person data, DNA/genomic data, archaeology or sacred-site locations, rare-species locations, critical infrastructure details, private-land joins, or rights-uncertain material;
- secrets, private endpoints, tokens, DSNs, signing credentials, `.env` files, or incident-working data;
- generated prose presented as evidence, approval, release state, or public truth;
- duplicate compatibility files that can diverge from their canonical replacement.

If prohibited content is discovered, do not normalize it in place. Classify it, isolate sensitive material, preserve identity and history, select the owning root, create a governed migration and recovery record, update references, and validate the destination before retirement.

## Inputs

Compatibility and retirement work may consume pointers to:

| Input | Required purpose |
|---|---|
| Exact tracked-path inventory | Establishes what actually exists before classification |
| Git history and prior blob identity | Preserves provenance and rollback |
| Current Directory Rules and accepted ADRs | Controls placement and authority |
| Parent and root README evidence | Establishes current compatibility posture |
| `KFMGeoManifest` contract and schema | Distinguishes semantic meaning from machine shape |
| Release manifest lane evidence | Determines release-governance destination without guessing |
| Artifact identities and digests | Prevents duplicate or ambiguous moves |
| Evidence, receipt, proof, catalog, source, and policy pointers | Preserves cross-family closure |
| Inbound reference inventory | Identifies producers, consumers, docs, tests, workflows, and public surfaces using the old path |
| Rights and sensitivity review | Prevents unsafe disclosure during inspection or migration |
| Release, correction, withdrawal, and rollback context | Preserves public-facing state when applicable |
| Migration and recovery records | Makes movement reversible and auditable |
| Validation plan | Defines how target correctness and old-path retirement will be proven |

Material inputs should be pinned by commit, digest, stable identifier, release ID, or exact path. Terms such as “latest Geo manifest” or “all map files” are insufficient for consequential migration.

## Outputs

This lane may produce documentation-only compatibility outputs:

- an evidence-bounded inventory;
- a classification matrix;
- a path crosswalk;
- a redirect or tombstone note;
- a deprecation notice;
- a migration plan;
- a validation summary;
- a retirement readiness record;
- links to externally owned migration, recovery, release, correction, and rollback records.

| Output | What it may prove | What it does not prove |
|---|---|---|
| README | Boundary and maintainer guidance exist | Any content migrated or retired |
| Inventory | Named files were observed in a named snapshot | Exhaustive production inventory |
| Crosswalk | Proposed or reviewed target routes are documented | Destination contents are valid |
| Redirect note | Old-path readers have a replacement pointer | Runtime consumers followed it |
| Migration plan | Intended movement and checks are reviewable | Migration executed |
| Validation summary | Named checks ran in a named context | Release approval or public safety |
| Retirement record | Closure was claimed with references | Historical dependencies are universally absent |
| Pull request or merge | Repository documentation changed | Data, signing, release, or publication behavior changed |

This lane emits no release manifest, signed sidecar, published artifact, policy decision, proof, receipt, or catalog record.

<a id="validation-checklist"></a>

## Validation

Validation is fail-closed and must match the operation being claimed.

### README validation

- [ ] The first twelve H2 sections follow the Directory Rules folder-README contract.
- [ ] Internal navigation and legacy anchors resolve.
- [ ] Relative links point to current tracked paths or are explicitly marked proposed.
- [ ] ADR-0011 and ADR-0023 remain labeled `proposed`.
- [ ] CODEOWNERS routing is not described as stewardship or approval.
- [ ] The README does not declare `data/manifests/geo/` canonical.
- [ ] The README does not imply a release, publication, migration, signing, or retirement occurred.

### Compatibility-lane validation

- [ ] Obtain an exact tracked inventory for the path.
- [ ] Identify any files beyond this README.
- [ ] Classify every observed item by responsibility family.
- [ ] Confirm no secret or restricted payload is committed.
- [ ] Confirm no public client or runtime reads this path.
- [ ] Confirm no workflow writes trust-bearing output here.
- [ ] Confirm no canonical contract, schema, policy, fixture, validator, receipt, proof, catalog, source, release, or published artifact is owned here.
- [ ] Confirm each redirect has a stable replacement pointer and removal trigger.

### GeoManifest validation boundary

- [ ] Confirm the semantic contract version and status.
- [ ] Confirm the schema version, `$id`, required fields, and permissiveness.
- [ ] Confirm whether the declared validator exists and is wired into CI.
- [ ] Confirm valid, invalid, denied, stale, superseded, signature-failure, digest-mismatch, and sensitivity fixtures.
- [ ] Confirm policy, release, signature, correction, and rollback integration.
- [ ] Confirm artifact digest and manifest digest semantics.
- [ ] Confirm producer and consumer adoption.
- [ ] Confirm public delivery rejects missing, mismatched, revoked, superseded, or unverifiable sidecars.
- [ ] Mark every unobserved check `NOT RUN` or `NEEDS VERIFICATION`.

### Migration and retirement validation

- [ ] Pin source and target revisions.
- [ ] Preserve stable identity, digest, provenance, evidence, source role, rights, sensitivity, temporal scope, spatial scope, and correction lineage.
- [ ] Update all inbound references.
- [ ] Verify the destination under its owning contract, schema, policy, fixtures, validators, and review.
- [ ] Verify the old path is no longer a writer or reader dependency.
- [ ] Preserve a rollback or restoration path.
- [ ] Record remaining residual risk.
- [ ] Keep the lane until the retirement decision and verification close.

### Finite validation outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Named checks passed for a pinned target and scope |
| `FAIL` | A required check failed; migration or retirement must stop |
| `HOLD` | Required authority, evidence, review, target, or recovery is unresolved |
| `NOT_APPLICABLE` | A reviewed rationale establishes that a check does not apply |
| `NOT_RUN` | The check has not executed; no inference is permitted |
| `ERROR` | Validation could not complete reliably |

A `HOLD` is a valid fail-safe outcome. It is not a partial approval.

## Review burden

Review scales with authority and public consequence.

| Change | Minimum review function |
|---|---|
| README wording only | Documentation reviewer familiar with data and release boundaries |
| Compatibility inventory or crosswalk | Data-lifecycle reviewer plus owner of each proposed destination |
| Redirect or tombstone | Data, docs, and affected consumer reviewers |
| Move of a `ReleaseManifest`-like record | Release-governance reviewer plus migration/recovery review |
| Move of a `KFMGeoManifest` or signed sidecar | Geo/evidence, schema, policy, release, signing/security, and artifact-owner review |
| Move of receipt, proof, catalog, or source records | Reviewer for the owning trust-artifact family |
| Change affecting PMTiles, COG, tiles, MapLibre, exports, or public endpoints | Geo/map, governed API, release, policy, and affected domain review |
| Sensitive or rights-uncertain geospatial material | Policy/sensitivity review plus affected domain and rights/sovereignty review where applicable |
| Deletion or retirement of the path | Data, release, docs, migration, recovery, and affected-consumer review |
| Breaking redirect or public behavior | Architecture decision and release review |
| Security incident or credential exposure | Security and incident-response review |

These are review **functions**, not verified repository role assignments. Current accountable individuals, required-review rules, separation of duties, and branch protection remain `NEEDS VERIFICATION`.

## Related folders

| Location | Relationship |
|---|---|
| [`../`](../README.md) | Parent non-canonical manifests compatibility lane |
| [`data/`](../../README.md) | Canonical lifecycle-data root; records manifest placement conflict |
| [`data/published/`](../../published/README.md) | Released public-safe artifact bytes after release gates |
| [`data/receipts/`](../../receipts/README.md) | Process and execution memory |
| [`data/proofs/`](../../proofs/README.md) | Evidence and integrity support |
| [`data/catalog/`](../../catalog/README.md) | STAC, DCAT, PROV, domain, and discovery records |
| [`data/registry/`](../../registry/README.md) | Source and governed registry records |
| [`release/`](../../../release/README.md) | Release-governance root |
| [`release/manifests/`](../../../release/manifests/README.md) | Current plural release-manifest collection lane; canonicality conflict remains |
| [`KFMGeoManifest` contract](../../../contracts/evidence/kfm_geo_manifest.md) | Semantic meaning |
| [`KFMGeoManifest` schema](../../../schemas/contracts/v1/evidence/kfm_geo_manifest.schema.json) | Current thin machine shape |
| [`Directory Rules`](../../../docs/doctrine/directory-rules.md) | Placement and README contract |
| [CODEOWNERS](../../../.github/CODEOWNERS) | GitHub routing only |

<a id="repo-fit"></a>

### Responsibility-root basis

The file remains under `data/` only because the tracked path is being bounded as compatibility debt. It must not evolve as a new responsibility root or as a canonical child authority.

The final treatment—retain as redirect, migrate to a compatibility index, or delete after reference closure—remains a governed migration decision.

## ADRs

| ADR | Current status | Relevance | Limitation |
|---|---|---|---|
| [ADR-0011](../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md) | `proposed` | Separates receipts, proofs, catalogs, release manifests/decisions, and published artifacts; proposes plural release manifests | Does not perform migration or settle enforcement |
| [ADR-0023](../../../docs/adr/ADR-0023-geo-manifest-signs-every-pmtiles-cog-release.md) | `proposed` | Proposes signed `KFMGeoManifest` sidecars for PMTiles and COG release artifacts | Does not prove schema completeness, signing, validators, policy wiring, or public enforcement |
| ADR-0001 | `proposed` | Proposes canonical schema-home discipline | Does not accept the current GeoManifest schema as complete |
| ADR-0015 | `proposed` | Proposes governed rollback for published current aliases | Does not prove alias or rollback implementation |
| ADR-0018 | `proposed` | Proposes promotion-gate sequencing | Does not prove release automation |
| ADR-0024 | `proposed` | Proposes release separation of duties | Does not establish current reviewers |
| ADR-0025 | `proposed` | Proposes that public clients never read canonical/internal stores | Does not prove runtime enforcement |

The canonical ADR index records every numbered ADR above with effective status `proposed`. This README cannot accept, reject, supersede, or amend them.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-24 |
| Review status | Repository-grounded v0.2.0 compatibility modernization |
| Current posture | Non-canonical compatibility lane; bounded search found only this README |
| Current GeoManifest maturity | Draft semantic contract; permissive schema stub; declared validator absent; fixtures unestablished |
| Current release-manifest posture | `release/` authority confirmed; singular/plural collection semantics conflicted |
| Migration posture | No migration, redirect, or retirement executed |
| Publication posture | None |
| Next review trigger | New file under this lane, accepted ADR status, GeoManifest validator/fixtures, signing workflow, release-manifest consolidation, inbound-reference inventory, migration PR, public endpoint, or retirement proposal |

---

## Current bounded topology

The bounded documentation topology relevant to this lane is:

```text
data/
├── README.md
├── manifests/
│   ├── README.md
│   └── geo/
│       └── README.md        # compatibility-only target
├── receipts/
├── proofs/
├── catalog/
├── registry/
└── published/

release/
├── README.md
├── manifest/                # singular lane; semantics unresolved
└── manifests/
    └── README.md            # plural collection lane
```

This is not a recursive payload attestation. Exact-path bounded search returned only this README for `data/manifests/geo`, but hidden, unindexed, historical, generated, deployed, or production material was not inspected.

## Artifact family and authority matrix

```text
receipt != proof != catalog != GeoManifest != ReleaseManifest != published artifact
```

| Family | Core question | Owning surface | Must not substitute for |
|---|---|---|---|
| Receipt | What process ran, with which inputs, code, and outcome? | `data/receipts/` | Proof, catalog, release approval |
| Proof support | What validation, evidence, integrity, or closure supports a consequential assertion? | `data/proofs/` and evidence authorities | Release decision, artifact bytes |
| Catalog | How is an artifact discovered, described, spatially/temporally indexed, and exchanged? | `data/catalog/` | Proof or release approval |
| `KFMGeoManifest` | Which geospatial artifact is described and how is it bound to identity, evidence, spatial reference, transforms, integrity, policy, and release context? | Contract under `contracts/`, schema under `schemas/`, instance placement still governed by accepted release/artifact design | EvidenceBundle, ReleaseManifest, artifact bytes |
| `ReleaseManifest` | Which governed records and artifacts are included in a release and what release-facing state applies? | `release/` | Artifact bytes, receipt, proof, catalog |
| Published artifact | Which release-approved public-safe bytes may governed clients consume? | `data/published/` and approved delivery | Canonical truth, evidence, policy, or release decision |
| This compatibility lane | Where did a historical path route, and how will it be retired safely? | `data/manifests/geo/` temporarily | Every family above |

<a id="guardrails"></a>

## KFMGeoManifest object boundary

The repository currently confirms:

- a draft semantic contract at `contracts/evidence/kfm_geo_manifest.md`;
- a Draft 2020-12 schema stub at `schemas/contracts/v1/evidence/kfm_geo_manifest.schema.json`;
- schema-required `id`;
- optional `version` and `spec_hash`;
- `additionalProperties: true`;
- declared but absent validator `tools/validators/evidence/validate_kfm_geo_manifest.py`;
- unestablished fixture lane at `fixtures/evidence/kfm_geo_manifest/`;
- proposed policy path under `policy/evidence/`;
- proposed release use under ADR-0023.

The object must remain distinct from:

| Adjacent object | Required distinction |
|---|---|
| `EvidenceRef` | Pointer to evidence support; not artifact-manifest closure |
| `EvidenceBundle` | Evidence closure supporting claims; outranks generated artifact metadata |
| `CatalogMatrix` | Catalog-family agreement descriptor; not a release signature |
| `ReleaseManifest` | Release-governance inclusion and state; not the GeoManifest artifact binding |
| Signature/DSSE envelope | Cryptographic wrapper or attestation; not the canonical semantic contract |
| PMTiles/COG/GeoJSON bytes | The geospatial artifact itself |
| Validation receipt | Process record that validation ran |
| Rollback card | Release-facing reversal or supersession decision |
| MapLibre layer configuration | Rendering projection, not truth or release authority |

No instance of this object belongs here by default. Instance placement remains `PROPOSED / NEEDS VERIFICATION` and must be resolved against accepted ADRs, release packaging, published-artifact layout, privacy posture, and consumer requirements.

## Proposed geo release package

The following package is a **proposed coordination model**, not current implementation proof:

```text
release governance
├── ReleaseManifest or release decision record
├── review / policy / signature references
├── correction and rollback references
└── inclusion pointers
        |
        v
published geospatial carrier
├── artifact bytes (PMTiles / COG / other approved format)
├── KFMGeoManifest sidecar or equivalent governed binding
└── stable artifact identity and digest
        |
        +--> catalog records (STAC / DCAT / PROV / domain)
        +--> receipts (build / validation / signing / promotion)
        +--> proof support and EvidenceBundle references
        +--> source and rights records
```

ADR-0023 proposes a DSSE-wrapped sidecar adjacent to PMTiles or COG bytes. That proposal remains unaccepted and unverified operationally. This README does not choose a signing tool, hash grammar, sidecar filename, transparency service, key model, or public delivery behavior.

## Compatibility and retirement state model

<a id="migration-posture"></a>

| State | Meaning | Allowed action |
|---|---|---|
| `COMPATIBILITY_ACTIVE` | Path exists and must remain fail-closed | README and bounded compatibility notes only |
| `INVENTORY_PENDING` | Complete tracked and inbound-reference inventory is missing | Inspect; do not move or delete |
| `CLASSIFIED` | Every observed item has an owning family and proposed target | Prepare migration and recovery plan |
| `MIGRATION_READY` | Targets, digests, references, reviews, validation, and rollback are complete | Execute in a scoped migration |
| `MIGRATING` | Governed movement or reference update is underway | Block new writes; preserve source and receipts |
| `REDIRECT_ONLY` | Trust-bearing content moved; compatibility pointer remains | Validate consumers and sunset window |
| `RETIREMENT_READY` | No writers, readers, payloads, or unresolved references remain | Approve path removal through governed review |
| `RETIRED` | Path removed or retained only as an archived historical record | Prevent recreation without ADR/migration |
| `BLOCKED` | Authority, evidence, target, review, safety, or recovery is unresolved | Hold and record blocker |
| `SUPERSEDED` | A later compatibility decision replaces this plan | Preserve lineage and follow successor |

These are proposed compatibility states, not release states, policy outcomes, or proof of execution.

## Routing misplaced content

Classify by responsibility, not by filename or “manifest” terminology.

| Content found here | Destination posture | Required preservation |
|---|---|---|
| `ReleaseManifest` or release inclusion record | Route to reviewed release manifest lane under `release/`; singular/plural choice remains unresolved | Stable ID, release/candidate pointer, decision, evidence, validation, correction, rollback |
| `KFMGeoManifest` semantic definition | `contracts/evidence/` | Meaning, version, history |
| `KFMGeoManifest` schema | `schemas/contracts/v1/evidence/` or accepted successor | `$id`, `$schema`, references, compatibility |
| GeoManifest instance or sidecar | Target remains governed by accepted artifact/release packaging decision | Artifact identity, digests, evidence, CRS, extent, transforms, rights, sensitivity, release state |
| Signature packet or signing record | Route according to accepted release/signature design | Signer identity, envelope, transparency reference, revocation |
| Process or validation receipt | `data/receipts/` | Run identity, code/spec identity, inputs, outputs, result |
| Proof or integrity support | `data/proofs/` | Evidence/proof identity, validation scope, digests |
| STAC, DCAT, PROV, domain catalog, or CatalogMatrix | Matching `data/catalog/` lane | Catalog identity, cross-family references, temporal/spatial scope |
| Published PMTiles, COG, GeoJSON, or layer artifact | `data/published/` after release gates | Immutable artifact identity, digest, release link, sensitivity transforms |
| SourceDescriptor or source record | `data/registry/` | Source identity, role, rights, activation state |
| Draft candidate metadata | Reviewed candidate or processed/release-candidate lane selected by its responsibility | Candidate identity, status, no public exposure |
| Policy or access decision | `policy/` plus decision records | Decision identity, reason, obligations |
| Fixture, validator, test, package, pipeline, or application code | Its canonical implementation root | Behavior, tests, history |
| Secret or restricted payload | Approved secure store outside ordinary repository paths | Incident handling, access revocation, correction trail |

A move must not create a new duplicate authority. If the destination already contains a competing object, stop and reconcile identity before migration.

## Anti-collapse guardrails

- **GeoManifest is not ReleaseManifest.**
- **Manifest is not artifact.**
- **Receipt is not proof.**
- **Proof is not catalog.**
- **Catalog is not publication.**
- **Signature is not policy approval.**
- **Digest match is not evidence closure.**
- **Schema validity is not semantic correctness.**
- **A permissive schema stub is not production readiness.**
- **A compatibility path is not canonical by longevity.**
- **A file move is not promotion or release.**
- **A redirect is not consumer adoption.**
- **A deleted folder is not migration closure.**
- **A generated map, tile, scene, index, or summary is not sovereign truth.**
- **A public URL is not proof of authorized publication.**
- **CODEOWNERS is not stewardship, review, or release approval.**

If any downstream document or implementation treats this lane as a trust-bearing home, record the conflict and fail closed.

<a id="evidence-ledger"></a>

## Compatibility evidence ladder

| Grade | Claim supported |
|---|---|
| `DOCUMENTED` | Boundary or plan exists in Markdown |
| `INVENTORIED` | Named tracked items and inbound references were observed at a pinned revision |
| `CLASSIFIED` | Each item has an owning family and reviewed target |
| `STATIC_VALIDATED` | Paths, formats, links, schemas, or crosswalks passed named static checks |
| `MIGRATED` | A governed change moved or superseded named repository items |
| `REFERENCE_CLOSED` | Producers, consumers, docs, tests, and workflows no longer depend on the old path |
| `TARGET_VERIFIED` | Destination artifacts pass their owning contracts, schemas, policy, validation, and review |
| `REDIRECT_VERIFIED` | Compatibility readers resolve to the replacement without authority duplication |
| `RETIRED` | Removal or archival was reviewed, executed, and verified |
| `RUNTIME_OBSERVED` | Named deployed consumers were observed using the governed target |
| `PUBLIC_VERIFIED` | Named public surfaces served the approved artifact and rejected invalid states |

This README update establishes `DOCUMENTED` only. It does not establish migration, reference closure, runtime behavior, or public verification.

## Migration and retirement procedure

A future migration should use the smallest reversible sequence:

1. **Freeze new trust-bearing writes** to `data/manifests/geo/`.
2. **Pin the base revision** and record the source blob/tree identity.
3. **Inventory tracked content** and all inbound references.
4. **Classify each item** by receipt, proof, catalog, GeoManifest, ReleaseManifest, published artifact, source, policy, or implementation family.
5. **Identify sensitive or rights-restricted material** and isolate it before ordinary processing.
6. **Resolve target authority conflicts**, including `release/manifest/` versus `release/manifests/`.
7. **Pin destination paths and object identities** using accepted contracts, schemas, ADRs, and Directory Rules.
8. **Prepare migration and recovery records** before moving consequential content.
9. **Validate the destination** with valid, invalid, denied, stale, superseded, and correction cases where applicable.
10. **Move or supersede content without losing history**, digests, evidence links, source roles, temporal/spatial scope, review state, or correction lineage.
11. **Update references atomically where practical**, including docs, workflows, tests, registries, APIs, UI, and release records.
12. **Verify no old-path writer remains.**
13. **Verify no old-path reader remains**, or install a bounded redirect with an explicit sunset.
14. **Run post-migration checks** and record finite outcomes.
15. **Exercise recovery** where consequence requires it, or keep `NOT RUN` visible.
16. **Retire the path only after closure** and preserve a historical migration pointer.

No step may publish, correct, withdraw, or roll back a release without the owning release process.

<a id="rollback"></a>

## Rollback, correction, and supersession

Three rollback scopes must remain distinct:

| Scope | Governing action |
|---|---|
| README documentation rollback | Revert the documentation commit or restore the prior blob |
| Compatibility migration rollback | Restore old-path references or apply a compensating migration using the paired migration-recovery record |
| Public release rollback | Use `release/` rollback, correction, withdrawal, supersession, alias, cache, and notice records |

A compatibility rollback must preserve:

- source and target identities;
- previous and current digests;
- evidence, source-role, rights, sensitivity, temporal, and spatial lineage;
- release and correction references;
- redirect state;
- consumer adoption state;
- reason and reviewer records;
- residual risk.

Do not delete a prior manifest or sidecar solely because a new one supersedes it. Historical records should remain traceable unless law, rights, or security requires a separately governed deletion or redaction process.

## Definition of done

This path is not retired until all applicable items close:

- [ ] Exact tracked inventory is complete.
- [ ] Historical and generated inventories are bounded.
- [ ] Every observed item is classified by owning responsibility.
- [ ] No secret or restricted payload remains in the public repository.
- [ ] `KFMGeoManifest` contract, schema, fixtures, validator, policy, release, correction, and rollback responsibilities are resolved.
- [ ] ADR-0011 and ADR-0023 status and consequences are reviewed.
- [ ] Release manifest singular/plural conflict is resolved or explicitly retained with distinct meanings.
- [ ] Source and destination identities and digests are pinned.
- [ ] Migration and recovery records exist.
- [ ] All inbound references are updated or governed by a bounded redirect.
- [ ] No writer emits trust-bearing content to the old path.
- [ ] No public client reads the old path.
- [ ] Destination objects pass applicable validation and review.
- [ ] Sensitive and rights obligations remain enforced.
- [ ] Release, correction, withdrawal, signature, catalog, receipt, proof, and published-artifact links remain closed.
- [ ] Recovery was rehearsed where required, or the gap remains visible.
- [ ] Redirect sunset and removal trigger are recorded.
- [ ] Path deletion or archival is independently reviewed where consequence warrants it.
- [ ] Rollback target and historical lineage remain accessible.
- [ ] No README, badge, PR, merge, workflow, or file placement is misrepresented as publication proof.

## No-loss ledger

| v0.1 material | v0.2.0 disposition |
|---|---|
| Non-canonical compatibility posture | Preserved and strengthened |
| Parent `data/manifests/` retirement boundary | Preserved and grounded in current data-root conflict |
| Release governance routed to `release/` | Preserved with singular/plural conflict made visible |
| Receipt/proof/catalog/publication separation | Preserved and expanded to distinguish GeoManifest and ReleaseManifest |
| Accepted-content limitation | Preserved under Directory Rules section order |
| Exclusions | Preserved and expanded for signatures, code, sensitive data, and public artifacts |
| Migration posture | Preserved and expanded into finite states and procedure |
| Guardrails | Preserved and expanded with anti-collapse rules |
| Evidence ledger | Preserved as repository-grounded status and evidence ladder |
| Validation checklist | Preserved and expanded by operation type |
| Rollback requirement | Preserved with documentation, migration, and release scopes separated |
| Historical greenfield stub SHA | Preserved in metadata |
| Legacy anchors | Preserved: `boundary`, `repo-fit`, `accepted-contents`, `exclusions`, `migration-posture`, `guardrails`, `evidence-ledger`, `validation-checklist`, `rollback` |
| Placeholder owners | Replaced with verified GitHub routing plus stewardship uncertainty |
| Publication boundary | Preserved and sharpened |

## Open verification register

- [ ] Obtain a recursive tracked inventory of `data/manifests/geo/`.
- [ ] Confirm whether any hidden, generated, archived, or historical trust-bearing files used this path.
- [ ] Identify every inbound repository reference to this path.
- [ ] Identify every deployed or external consumer of this path.
- [ ] Confirm whether the path should remain compatibility-only, become redirect-only, move to an archive, or be deleted.
- [ ] Resolve `release/manifest/` versus `release/manifests/` semantics and canonicality.
- [ ] Confirm instance placement for `KFMGeoManifest` and signed sidecars.
- [ ] Review and decide ADR-0011.
- [ ] Review and decide ADR-0023.
- [ ] Confirm the complete `KFMGeoManifest` field contract.
- [ ] Replace or graduate the permissive schema stub.
- [ ] Implement and test the declared GeoManifest validator.
- [ ] Create valid, invalid, denied, stale, superseded, digest-mismatch, signature-failure, and sensitivity fixtures.
- [ ] Confirm policy evaluation and promotion-gate integration.
- [ ] Confirm DSSE envelope, signing identity, keyless/keyed posture, transparency-log handling, revocation, and supersession.
- [ ] Confirm artifact and manifest digest grammar.
- [ ] Confirm PMTiles and COG build, signing, validation, release, and public-serving behavior.
- [ ] Confirm support for other geospatial carriers before broadening the object.
- [ ] Verify public clients reject missing, mismatched, expired, revoked, superseded, or unverifiable sidecars.
- [ ] Confirm evidence closure and source-role preservation.
- [ ] Confirm rights, sensitivity, generalization, and redaction behavior.
- [ ] Confirm catalog references agree across STAC, DCAT, PROV, and domain records where applicable.
- [ ] Confirm correction, withdrawal, cache invalidation, alias, and rollback propagation.
- [ ] Define migration and recovery record identities for path retirement.
- [ ] Verify branch protection, required review, and independent approval.
- [ ] Confirm accountable stewardship assignments.
- [ ] Formalize host-render and link validation for this README.
- [ ] Revisit this README after the first accepted GeoManifest release profile or retirement migration.

## Changelog

### v0.2.0 — 2026-07-24

- Reorganized the README to the Directory Rules folder contract.
- Grounded the lane in current data-root, release-root, ADR, contract, schema, and CODEOWNERS evidence.
- Preserved the non-canonical compatibility posture.
- Distinguished `KFMGeoManifest`, `ReleaseManifest`, receipts, proofs, catalogs, published artifacts, and signatures.
- Recorded the GeoManifest schema as a permissive stub, the declared validator as absent, and fixtures as unestablished.
- Made ADR-0011 and ADR-0023 proposed status explicit.
- Added compatibility states, routing, evidence grades, finite validation outcomes, migration procedure, rollback scopes, definition of done, and open verification.
- Preserved legacy anchors, historical stub identity, no-loss content, and non-publication boundary.

### v0.1 — 2026-06-25

- Replaced a greenfield stub with a non-canonical Geo manifest compatibility and retirement note.
- Routed release-level manifests to release governance.
- Separated receipts, proofs, catalogs, source records, published artifacts, schemas, policy, and code.
- Added migration, validation, guardrail, evidence, and rollback guidance.

<p align="right"><a href="#top">Back to top</a></p>
