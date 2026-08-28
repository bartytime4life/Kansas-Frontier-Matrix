<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://adr/ADR-0033
title: Keep GeoParquet 1.1 as the default and gate 2.0 evaluation
type: adr
adr_id: ADR-0033
version: v1.1
status: proposed
effective_decision_status: proposed
owners:
  - "OWNER_TBD — architecture decision owner"
  - "OWNER_TBD — geospatial data steward"
  - "OWNER_TBD — data platform steward"
  - "OWNER_TBD — release and correction steward"
owner_status: "CODEOWNERS routes docs, standards, contracts, schemas, validators, tests, workflows, receipts, and published-data lanes to @bartytime4life, but no accepted StewardshipAssignment, independent format approver, implementation owner, downstream-consumer registry, or release authority was verified"
reviewers_required:
  - Architecture steward
  - Geospatial data steward
  - Data platform steward
  - Standards and documentation steward
  - Contracts and schemas steward
  - Validation and CI steward
  - Catalog and provenance steward
  - Release, correction, and rollback steward
  - At least one owner of every confirmed production reader, writer, query engine, or public consumer
created: 2026-08-10
updated: 2026-08-14
policy_label: public
truth_posture: cite-or-abstain
responsibility_root: docs/
owning_root: docs/
responsibility: "Record the proposed GeoParquet version-readiness decision, finite routing outcomes, evidence ladder, current repository proof boundaries, and reversible path to a later 2.x decision without changing standards, dependencies, data, runtime, release, or publication state."
current_path: docs/adr/ADR-0033-geoparquet-version-readiness.md
supersedes: []
superseded_by: []
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 3e1a929a5e23f570b40c56e473b08ef65c3c5673
  target_prior_blob: 239acc3978ac67fb71f9acc6a675d28a8a92c55c
  adr_index_blob: 938c5894c36b99e14810918e2c550ab0e92d53b1
  adr_0029_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  repository_ruleset_id: 15484585
  repository_ruleset_name: Protect
  repository_ruleset_updated_at: 2026-07-29T13:00:55.368-05:00
  geoparquet_standard_blob: 7320145300e2ab6f414078e8479735ec374711c4
  geospatial_carrier_contract_blob: 17055a680b83a4f83834735e88aeb0569322845b
  geospatial_carrier_schema_blob: b6ebec77a6e09c50b89594c4032bd40ec238f6be
  geospatial_carrier_validator_blob: 63e4cfac4838d0095b7f05fc6a3507ebe180fd8b
  geospatial_carrier_tests_blob: 49b8ff390aee4b0d3381ec2d087238ce0c725ccc
  geospatial_carrier_workflow_blob: f5791e0988166dbcdd5d781c690073e8d3b10389
  geospatial_carrier_latest_main_run: 31654972027
  stac_mirror_contract_blob: e5b3aabbee5a697d8e72e84f7df769882fdf76d5
  stac_mirror_workflow_blob: 28bbbf731a1ffb6ba489e9dc0e0b44acb9d6e660
  stac_mirror_latest_main_run: 31654971667
  original_authoring_receipt_blob: 9852afaa9cafbba045fbef03456d211c1e5dc250
  upstream_latest_release: v2.0.0-rc.1
  upstream_rc_commit: 0c7fab74cf1177e2fe61df8eb7fcd1813b73e4aa
  upstream_corrected_1_1_tag: v1.1.0+p1
  upstream_corrected_1_1_commit: 540f6bf547587284e632c47530bc08d9e43bb045
inspection_boundary: >
  Current-session GitHub reads of this ADR, the canonical ADR index, accepted ADR-0029,
  Directory Rules, CODEOWNERS, the active default-branch ruleset, the GeoParquet standards
  reference, geospatial-carrier contract/schema/validator/tests/workflow and hosted run,
  STAC mirror contract/workflow and hosted run, the generated v1 authoring receipt, and the
  tracked GeoParquet publication lanes. Official upstream release evidence was rechecked on
  2026-08-14. No GeoParquet carrier bytes, real production reader/writer/query-engine matrix,
  benchmark, migration, dual-read window, downstream service inventory, runtime trace,
  release manifest, correction drill, rollback drill, deployment, or public consumption was
  exercised.
source_lineage:
  - "Kansas Frontier Matrix Improvements — proposal lineage; not repository authority"
  - "docs/intake/exploratory/spatiotemporal-modernization-blueprint-source-map.md — governed intake and conflict map"
related:
  - docs/adr/README.md
  - docs/adr/INDEX.md
  - docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - docs/adr/ADR-0013-spec_hash-and-run_id-identity-grammar.md
  - docs/adr/ADR-0018-promotion-gate-sequence.md
  - docs/adr/ADR-0020-abstain-is-a-first-class-decision.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/doctrine/directory-rules.md
  - docs/standards/GEOPARQUET.md
  - docs/intake/exploratory/spatiotemporal-modernization-blueprint-source-map.md
  - contracts/release/geospatial_carrier_readiness.md
  - schemas/contracts/v1/release/geospatial_carrier_readiness.schema.json
  - tools/validators/release/validate_geospatial_carrier_readiness.py
  - tests/release/test_geospatial_carrier_readiness.py
  - .github/workflows/geospatial-carrier-readiness.yml
  - contracts/data/stac_geoparquet_mirror_assessment.md
  - .github/workflows/stac-geoparquet-mirror-assessment.yml
  - tools/validators/evidence/validate_kfm_geo_manifest.py
  - data/published/geoparquet/README.md
  - data/receipts/generated/genrec-geoparquet-version-readiness-20260810.json
  - .github/CODEOWNERS
tags: [adr, kfm, geoparquet, parquet, geospatial, compatibility, interoperability, migration, correction, rollback, governance]
notes:
  - "v1.1 is a same-path repository-grounded modernization. It preserves source and effective status proposed and does not accept ADR-0033."
  - "The repository declares GeoParquet 1.1.0 in a draft standards reference and an inactive metadata-only carrier profile; that is not equivalent to an accepted production format policy."
  - "Official upstream evidence still identifies v2.0.0-rc.1 as the latest release and explicitly as a release candidate, not final 2.0.0."
  - "The latest dedicated carrier and STAC-mirror workflow runs passed focused semantic tests but failed generated-authoring-receipt integrity; this revision records that inherited proof-chain drift without repairing or bypassing it."
  - "The original 2026-08-10 authoring receipt remains valid only for the v1/index bytes it names. It is retained as historical evidence and is not represented as the receipt for v1.1."
  - "This revision changes no KFM standard, dependency, contract, schema, validator, fixture, workflow, receipt, data, source, runtime, release, deployment, or publication state."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ADR-0033: Keep GeoParquet 1.1 as the default and gate 2.0 evaluation

> **Proposed decision.** KFM should retain GeoParquet `1.1.0` as the declared baseline and route GeoParquet `2.x` through a separately reviewed, synthetic, byte-level interoperability evaluation. A final stable `2.x` release, complete consumer inventory, migration/correction/rollback evidence, and a later accepted decision are required before any default changes.

[![Decision: proposed](https://img.shields.io/badge/decision-proposed-d4a72c?style=flat-square)](#status)
[![Declared baseline: 1.1.0](https://img.shields.io/badge/declared%20baseline-1.1.0-0969da?style=flat-square)](#current-repository-evidence)
[![Upstream: 2.0.0-rc.1](https://img.shields.io/badge/upstream-2.0.0--rc.1-f59e0b?style=flat-square)](#upstream-evidence-checkpoint)
[![Byte interoperability: absent](https://img.shields.io/badge/byte%20interop-absent-b42318?style=flat-square)](#current-enforcement-maturity)
[![Operational adoption: hold](https://img.shields.io/badge/adoption-HOLD-b42318?style=flat-square)](#current-enforcement-maturity)
[![Publication effect: none](https://img.shields.io/badge/publication-none-6e7781?style=flat-square)](#authority-and-non-effects)

> [!IMPORTANT]
> **Identity is confirmed; acceptance is not.** [`docs/adr/INDEX.md`](./INDEX.md) uniquely assigns `ADR-0033` to this exact path and records it as `proposed`. Editing, validating, or merging this Markdown does not accept the decision, adopt GeoParquet `1.1.0` as production policy, authorize `2.x` evaluation, or create release authority.

> [!CAUTION]
> **The current repository proves declarations and synthetic metadata behavior, not GeoParquet-byte compatibility.** The existing carrier profile is `PROPOSED_INACTIVE`, does not open Parquet bytes, and holds `2.x`. The STAC mirror profile also evaluates declared projections without reading carrier bytes. Neither surface proves a writer, reader, query engine, migration, downgrade, correction, or release path.

> [!WARNING]
> **A version string is not an interoperability result.** Upstream `v2.0.0-rc.1` changes the storage foundation to native Parquet `GEOMETRY` and `GEOGRAPHY` logical types and built-in spatial statistics. A declaration-only validator, successful metadata fixture, or tool that recognizes the tag cannot establish semantic preservation across KFM consumers.

> [!NOTE]
> The repository's draft GeoParquet standards reference calls `1.1.0` canonical, while ADR-0033 remains proposed and no production carrier was inspected. This revision therefore distinguishes a **declared baseline** from accepted operational adoption.

**Quick navigation:** [Status](#status) · [Evidence](#evidence-boundary) · [Context](#context) · [Decision](#proposed-decision) · [Outcomes](#finite-version-readiness-outcomes) · [Maturity](#readiness-and-evidence-maturity) · [Dual evaluation](#dual-evaluation-entry-packet) · [Adoption](#evidence-required-before-adopt-later) · [Denial](#deny-unsupported-boundary) · [Layout](#physical-layout-remains-benchmark-bound) · [Authority](#authority-and-non-effects) · [Repository evidence](#current-repository-evidence) · [Enforcement](#current-enforcement-maturity) · [Convergence](#implementation-and-convergence-plan) · [Acceptance](#acceptance-and-graduation-gates) · [Consequences](#consequences) · [Alternatives](#alternatives-considered) · [Risks](#risk-and-open-question-ledger) · [Migration](#migration-correction-and-rollback) · [Checklist](#verification-checklist) · [References](#references) · [History](#revision-history)

---

<a id="status"></a>

## Status

| Field | Current value |
|---|---|
| **ADR ID** | `ADR-0033` — unique and confirmed in [`INDEX.md`](./INDEX.md) |
| **Tracked path** | `docs/adr/ADR-0033-geoparquet-version-readiness.md` |
| **Source metadata** | `proposed` |
| **Effective decision status** | `proposed` |
| **Record edition** | `v1.1` — evidence reconciliation; decision unchanged |
| **Decision class** | Cross-component format-version readiness, interoperability, migration, correction, rollback, and release compatibility |
| **Current proposed route** | `KEEP_1_1` |
| **Declared repository baseline** | GeoParquet `1.1.0` in a draft standards reference and inactive metadata profile |
| **Upstream checkpoint** | `v2.0.0-rc.1`; release candidate, not final `2.0.0` |
| **Current implementation maturity** | `L1 / PARTIAL`: deterministic metadata fixtures exist; byte-level interoperability and production adoption do not |
| **Current operational outcome** | `HOLD` for default change or `2.x` production use |
| **Release/publication effect** | None |
| **Supersedes / superseded by** | None / none |

### Decision acceptance versus implementation graduation

Two states must remain independent:

1. **ADR acceptance** would approve the routing rule: retain `1.1.0`, allow bounded dual evaluation, require a later evidence-backed decision for `2.x`, and fail closed on unsupported versions.
2. **Implementation graduation** would require versioned contracts, captured carrier bytes, pinned tools, cross-engine tests, consumer inventory, migration receipts, correction/rollback drills, release integration, and observed failure-closed behavior.

An accepted ADR without implementation would be doctrine. A green fixture or workflow without an accepted decision would be candidate evidence. Neither state alone authorizes release.

### Current determination

`KEEP_1_1` is the proposed decision outcome. `DUAL_EVALUATE` is not currently implemented as a governed profile. `ADOPT_LATER` has not met its entry conditions. Unknown or unsupported GeoParquet declarations remain held by the existing metadata preflight.

[Back to top](#top)

---

<a id="evidence-boundary"></a>

## Evidence boundary

This edition uses repository bytes at `main@3e1a929a5e23f570b40c56e473b08ef65c3c5673`, the current GitHub ruleset/review-routing evidence, the latest dedicated hosted runs available for the GeoParquet-adjacent candidate profiles, and official upstream release evidence rechecked on 2026-08-14.

### Evidence layers

| Layer | What can be proved | Current state | What it cannot prove |
|---|---|---|---|
| **L0 — Decision and standards prose** | Declared intent, scope, vocabulary, non-effects | ADR proposed; standards reference draft | Byte behavior, tool support, adoption, release |
| **L1 — Synthetic declaration profile** | Schema-valid metadata candidates and finite declared outcomes | Carrier and STAC-mirror fixtures/validators exist | Actual Parquet encoding, logical types, statistics, round trip |
| **L2 — Captured-byte conformance** | A pinned validator opens deterministic synthetic files and checks bytes plus metadata | Absent | Cross-engine interoperability or production use |
| **L3 — Cross-tool interoperability** | Pinned writers/readers/query engines preserve agreed semantics and negative cases | Absent | Migration of real KFM products or release operation |
| **L4 — Governed operational adoption** | Accepted decision, complete migration, release/correction/rollback evidence, observed consumers | Absent | Future compatibility without ongoing monitoring |

### Truth labels

- **CONFIRMED** — verified from current repository bytes, hosted run evidence, GitHub control evidence, or pinned official upstream evidence.
- **PROPOSED** — the decision, readiness vocabulary, evaluation profile, field roster, path role, or future transition described here.
- **UNKNOWN** — production consumers, external services, local tools, data bytes, and runtime behavior not resolved in this inspection.
- **NEEDS VERIFICATION** — a concrete check remains before acting on the claim.
- **HOLD** — evidence is insufficient for a trust-bearing version transition.

### Explicitly not inspected

No real GeoParquet file, object-store artifact, query log, API payload, downstream notebook, data warehouse, map build, migration output, release manifest, correction notice, rollback card, deployment, or public client was opened or exercised. The tracked `data/published/geoparquet/` lanes contain READMEs and placeholders at the inspected checkpoint, not confirmed release bytes.

[Back to top](#top)

---

<a id="context"></a>

## Context

The governed source map for *Kansas Frontier Matrix Improvements* identifies GeoParquet version readiness as a decision candidate. The motivating proposal couples mandatory GeoParquet `2.0` adoption with fixed physical-layout choices. KFM must separate those questions:

- **format version** defines encoding and interoperability semantics;
- **physical layout** defines dataset- and workload-specific compression, ordering, partitioning, and row-group choices;
- **release readiness** additionally requires evidence, policy, review, integrity, correction, and rollback.

A proposal document, upstream development branch, metadata string, or one implementation's feature claim cannot answer all three.

### Why a decision is required

GeoParquet `2.0` is not a metadata-only substitution. The upstream RC recenters the format on native Parquet `GEOMETRY` and `GEOGRAPHY` logical types, associated spatial statistics, and changed CRS/metadata relationships. KFM's declared `1.1.0` profile instead expects the 1.x metadata model, WKB-oriented declarations, and optional bbox covering behavior. Version-sensitive differences can affect:

- geometry and geography type identity;
- CRS representation, axis order, edge interpretation, and null/unknown CRS behavior;
- row-group and page-index spatial statistics;
- bbox-covering removal or translation;
- empty, null, mixed, nested, three-dimensional, and multi-geometry behavior;
- metadata preservation by readers and writers;
- query pruning and semantic equivalence;
- downgrade loss, mixed-version routing, correction, and rollback.

### Failures this ADR addresses

- silently upgrading because an upstream release is marked “latest”;
- treating an RC as final stable `2.0.0`;
- accepting a `2.x` declaration without opening bytes;
- counting one writer or reader as ecosystem compatibility;
- coupling format adoption to one universal layout recipe;
- losing CRS, statistics, geometry, null, identity, or extension semantics during round trips;
- mixing `1.1` and `2.x` artifacts without routing or correction rules;
- rewriting data before a rollback-compatible migration packet exists;
- treating CI, a receipt, a catalog mirror, or a merged PR as release authority.

[Back to top](#top)

---

<a id="upstream-evidence-checkpoint"></a>

## Upstream evidence checkpoint

Official upstream evidence rechecked on 2026-08-14 still lists `v2.0.0-rc.1` as the latest release. The release explicitly describes itself as a release candidate for final implementation testing and says small details may change before final `2.0.0`. Its pinned commit is `0c7fab74cf1177e2fe61df8eb7fcd1813b73e4aa`.

The corrected stable 1.1 specification remains identified by GeoParquet version `1.1.0`; the repository's `v1.1.0+p1` correction tag peels to `540f6bf547587284e632c47530bc08d9e43bb045`. The correction tag does not create a distinct GeoParquet metadata version.

This upstream checkpoint supports evaluation planning. It does not prove KFM implementation compatibility or authorize a version change.

[Back to top](#top)

---

<a id="proposed-decision"></a>

## Proposed decision

Upon acceptance:

1. **Retain GeoParquet `1.1.0` as the KFM baseline.** Do not represent the draft standard or inactive candidate profile as proof of operational adoption.
2. **Route `2.x` through a separate `DUAL_EVALUATE` profile.** The profile must be synthetic, no-network, dependency-governed, byte-opening, deterministic, and fixed to no release authority.
3. **Require a later decision for production adoption.** `ADOPT_LATER` becomes eligible only after a final stable `2.x` release and the evidence in this ADR are complete.
4. **Fail closed for unknown or unsupported behavior.** A version, logical type, metadata combination, reader/writer result, mixed collection, or downgrade outside an accepted profile yields `DENY_UNSUPPORTED` or `HOLD` at its owning boundary.
5. **Keep physical layout benchmark-bound.** Version selection does not prescribe one compression, ordering, partition, row-group, file-size, or spatial-index strategy.
6. **Preserve object-family boundaries.** Readiness results, validation reports, policy decisions, promotion decisions, release manifests, receipts, proofs, corrections, and rollback records remain separate.
7. **Keep public clients downstream of governed release.** No candidate or evaluation artifact becomes a normal API, map, catalog, or AI source.

### Normative language boundary

`MUST`, `MUST NOT`, `SHOULD`, and `MAY` below describe the proposed accepted state. They do not describe current repository enforcement while ADR-0033 remains proposed.

[Back to top](#top)

---

<a id="finite-version-readiness-outcomes"></a>

## Finite version-readiness outcomes

| Outcome | Meaning | Entry condition | Permitted effect |
|---|---|---|---|
| `KEEP_1_1` | Retain GeoParquet `1.1.0` as the declared baseline. | No accepted later decision; `2.x` evidence incomplete. | Continue current proposal/fixture work without changing standards, bytes, dependencies, or consumers. |
| `DUAL_EVALUATE` | Compare pinned `1.1.0` and one exact `2.x` candidate/final release. | Complete dependency-closed evaluation packet and human review. | Add synthetic fixtures, byte-level validation, interoperability reports, and authoring evidence only. |
| `ADOPT_LATER` | A final stable `2.x` release and all operational acceptance evidence exist. | Separate reviewed status transition or successor decision. | Update affected standards and implementation surfaces with migration/correction/rollback closure. |
| `DENY_UNSUPPORTED` | Declared or observed behavior cannot be safely interpreted under an accepted/evaluation profile. | Known mismatch, missing capability, semantic loss, or required proof unavailable. | Hold or quarantine the carrier; emit finite reasons; no promotion or publication. |

A validator `PASS` means one document coherently reports its bounded outcome. It does not mean the version is adopted, the artifact is correct for every consumer, or release is authorized.

[Back to top](#top)

---

<a id="readiness-and-evidence-maturity"></a>

## Readiness and evidence maturity

| Level | Capability | Required evidence | Release consequence |
|---|---|---|---|
| **L0 — Documented proposal** | Version intent and non-effects are written. | Proposed ADR/standard and source lineage. | No adoption or carrier authority. |
| **L1 — Declared metadata candidate** | Closed synthetic metadata fixtures produce finite outcomes. | Schema, validator, positive/negative cases, deterministic tests. | No byte or release claim. |
| **L2 — Captured-byte conformance** | Pinned tooling opens and validates deterministic synthetic carrier bytes. | Immutable files, digests, metadata/physical-schema dumps, byte-level negative cases. | Evaluation only. |
| **L3 — Multi-engine interoperability** | Multiple pinned writers/readers/query engines preserve agreed semantics. | Matrix, round trips, query/statistics tests, extension preservation, downgrade refusal. | Adoption candidate; still no release without later decision. |
| **L4 — Governed operational adoption** | Accepted decision, migrated products, release integration, correction/rollback drills, monitored consumers. | Complete release packet and observed behavior. | `2.x` may become a governed baseline within the accepted scope. |

### Current level

The repository is **L1 / PARTIAL**:

- the metadata-only geospatial-carrier profile has deterministic fixtures and finite outcomes;
- the STAC mirror assessment has a separate synthetic declared-projection profile;
- neither profile opens GeoParquet bytes;
- no dedicated `DUAL_EVALUATE` contract, schema, fixture family, validator, tool matrix, or workflow was found;
- the latest dedicated hosted runs are red because generated authoring receipts no longer match artifact bytes, even though focused semantic tests passed;
- no confirmed production consumer or release instance was inspected.

Therefore operational adoption remains **HOLD**.

[Back to top](#top)

---

<a id="dual-evaluation-entry-packet"></a>

## Dual-evaluation entry packet

A separate evaluation change **MUST** be dependency-closed and include every directly necessary surface. Exact paths must be checked again against accepted Directory Rules and current repository evidence before creation.

### 1. Immutable upstream identities

- the exact `1.1.0` specification/schema revision;
- the exact `2.x` RC or final specification/schema revision;
- tag, commit, retrieved-at time, digest, and source authority;
- an explicit statement that RC results do not establish final-version conformance.

### 2. Admitted toolchain matrix

For every candidate writer, reader, validator, and query engine:

| Field | Required content |
|---|---|
| Identity | Package/project, version, immutable dependency lock, license, source |
| Role | Write, read, validate, query, transform, catalog, or inspect |
| Supported format | `1.1.0`, exact `2.x`, both, or unsupported |
| Logical types | `GEOMETRY`, `GEOGRAPHY`, WKB/legacy path, nested/multiple geometry |
| Preservation | CRS, edges/algorithm, statistics, metadata, unknown extensions, IDs, null/empty |
| Failure posture | Reject, hold, error, partial read, lossy rewrite, or unsupported |
| Network and mutation | Fixed no-network for tests; no write outside temporary evaluation workspace |

No tool is admitted merely because its documentation claims GeoParquet support.

### 3. Paired public-safe synthetic carrier bytes

Use semantically equivalent `1.1.0` and exact `2.x` files where equivalence is meaningful. Each file must have:

- deterministic source generator or checked-in immutable bytes;
- content digest and size;
- Parquet physical-schema dump;
- GeoParquet metadata dump;
- row-group/page statistics dump where applicable;
- generation tool/version/parameters;
- fixture purpose and expected result;
- no sensitive, proprietary, personal, or source-derived data.

### 4. Required fixture dimensions

At minimum:

- point, line, polygon, multi-geometry, geometry collection where supported;
- empty versus null geometry;
- multiple geometry columns and primary-column declaration;
- two-dimensional and three-dimensional coordinates;
- planar versus geography/spherical semantics where supported;
- explicit PROJJSON, `null` CRS, absent/invalid/conflicting CRS cases;
- bbox covering in `1.1` and native spatial statistics in `2.x`;
- nested/repeated values where the selected engines claim support;
- unknown metadata and extension preservation;
- stable feature identifiers and row-order expectations where material;
- mixed-version collection routing;
- malformed metadata, logical-type mismatch, statistics mismatch, and truncated/corrupt byte cases;
- downgrade refusal where consequential semantics cannot be preserved.

### 5. Required operations

- write then validate;
- read without rewrite;
- query using spatial statistics/pruning where supported;
- round-trip within one engine;
- cross-engine round-trip;
- catalog projection and mirror comparison;
- attempted `2.x` to `1.1` downgrade;
- unsupported-version and tool-unavailable paths;
- deterministic replay of every fixture and report.

### 6. Finite evaluation result

The evaluation object should report a bounded outcome such as `PASS`, `HOLD`, `DENY`, or `ERROR`, plus a separate version-readiness projection. It must not reuse `READY` or `PASS` as release approval.

### 7. Fixed non-effects

Every evaluation permission remains false:

- repository canonical-data write;
- lifecycle promotion;
- source activation;
- policy override;
- release;
- deployment;
- publication;
- public-client use.

### 8. Authoring and replay evidence

The packet must bind all dependencies, fixtures, commands, outputs, expected/actual results, and artifact digests. Receipt integrity must pass at the exact pull-request head before the result is relied upon.

[Back to top](#top)

---

<a id="evidence-required-before-adopt-later"></a>

## Evidence required before `ADOPT_LATER`

A later adoption proposal requires a separately reviewed status transition or successor ADR and all of the following.

### Upstream and semantic closure

- official final stable `2.x` specification/schema tag—not `main`, a mutable branch, or an RC;
- delta analysis from the evaluated RC/final tag to the adopted final tag;
- accepted KFM semantics for logical types, CRS, statistics, extension metadata, null/empty values, IDs, and mixed-version collections.

### Complete consumer inventory

- every confirmed KFM writer, reader, validator, query engine, pipeline, catalog projection, API/export path, map build, notebook, service, and published consumer;
- owner and support evidence for each consumer;
- explicit `UNKNOWN` or `HOLD` for unowned/unverified consumers rather than inferred compatibility.

### Interoperability and migration closure

- passing L2 and L3 evidence for representative public-safe fixtures;
- versioned dual-read window with start, end, owner, exit criteria, telemetry, and correction policy;
- migration receipt model covering inputs, outputs, tools, parameters, digests, failures, retries, and prior state;
- deterministic identity and semantic-equivalence rules;
- mixed-version routing, unsupported-version handling, and downgrade refusal;
- storage, catalog, cache, API, export, and public-client compatibility review.

### Correction and rollback closure

- exact rollback target for every migrated artifact;
- correction/withdrawal path when a reader or writer later changes behavior;
- cache and catalog invalidation plan;
- replay and rollback drill demonstrating that the prior public-safe state can be restored;
- preservation of original bytes and decision history according to retention policy.

### Governance and release closure

- accepted version-readiness decision;
- accepted/current contracts, schemas, policy, validators, fixtures, and workflows for the adopted scope;
- independent qualified review capacity;
- subject-bound review evidence;
- release manifest and proof references to exact migrated bytes;
- observed fail-closed behavior for unsupported or inconsistent carriers.

[Back to top](#top)

---

<a id="deny-unsupported-boundary"></a>

## `DENY_UNSUPPORTED` boundary

A carrier **MUST** be held when any of these conditions applies:

- the declared GeoParquet version is absent, malformed, conflicting, or outside an accepted/evaluation profile;
- the observed Parquet logical type or GeoParquet metadata conflicts with the declaration;
- required metadata or logical-type information cannot be resolved;
- the active tool cannot preserve required geometry, geography, CRS, statistics, extension metadata, null/empty, identifier, or ordering semantics;
- a mixed-version collection lacks accepted routing and correction behavior;
- a downgrade would discard or reinterpret consequential content;
- only declaration-level evidence exists where byte-level evidence is required;
- a required tool, schema, registry, policy, or validator fails;
- receipt or artifact identity does not bind to the bytes evaluated.

The denial must identify the unsupported surface without claiming the artifact is false, malicious, or globally invalid unless separate evidence proves that claim.

### Proposed reason-code families

These are design vocabulary, not current implementation claims:

- `GEOPARQUET_VERSION_DECLARATION_MISSING`
- `GEOPARQUET_VERSION_CONFLICT`
- `GEOPARQUET_VERSION_NOT_IN_PROFILE`
- `GEOPARQUET_LOGICAL_TYPE_UNSUPPORTED`
- `GEOPARQUET_METADATA_LOGICAL_TYPE_MISMATCH`
- `GEOPARQUET_CRS_NOT_PRESERVED`
- `GEOPARQUET_SPATIAL_STATISTICS_NOT_PRESERVED`
- `GEOPARQUET_EXTENSION_METADATA_LOSS`
- `GEOPARQUET_MIXED_VERSION_UNROUTED`
- `GEOPARQUET_DOWNGRADE_LOSS`
- `GEOPARQUET_BYTE_VALIDATION_REQUIRED`
- `GEOPARQUET_TOOLCHAIN_UNVERIFIED`
- `GEOPARQUET_RECEIPT_BINDING_INVALID`

The current metadata validator already emits `GEOPARQUET_VERSION_NOT_ADOPTED` for a `2.x` declaration. That current code is narrower than the proposed future byte-level reason families.

[Back to top](#top)

---

<a id="physical-layout-remains-benchmark-bound"></a>

## Physical layout remains benchmark-bound

Version selection does not select one universal physical layout. These choices remain dataset- and workload-specific:

- compression codec and level;
- row-group row and byte targets;
- sort/order method and parameters;
- partition key, grid, and granularity;
- file count and target size;
- statistics and page-index settings;
- spatial index or covering strategy;
- delivery-versus-analytics optimization.

The current inactive carrier profile correctly records an inspectable, benchmark-referenced layout declaration instead of imposing one global recipe. Neither this ADR nor the motivating proposal makes Hilbert ordering, a fixed row-group range, ZSTD parameters, H3/S2 partitioning, or one grid resolution mandatory for all KFM data.

A layout benchmark must identify the dataset characteristics, query workload, engine versions, storage/transport assumptions, correctness checks, and repeatable commands. Faster output cannot compensate for semantic loss or weaker rollback.

[Back to top](#top)

---

<a id="authority-and-non-effects"></a>

## Authority and non-effects

This ADR is necessary but not sufficient for format adoption. It does not replace:

- the GeoParquet standards reference;
- semantic contracts and machine schemas;
- dependency admission and supply-chain review;
- source, rights, sensitivity, or policy decisions;
- byte-level validation and interoperability evidence;
- PromotionDecision, ReleaseManifest, proof, correction, or rollback objects;
- public-client trust-membrane controls.

This v1.1 revision changes only the ADR text. It does **not**:

- accept ADR-0033;
- change `docs/standards/GEOPARQUET.md`;
- activate `GeospatialCarrierReadinessCheck` or `STACGeoParquetMirrorAssessment`;
- add, pin, upgrade, or execute a GeoParquet/Parquet library;
- create or rewrite Parquet bytes;
- change source, evidence, policy, catalog, data, runtime, API, UI, or AI behavior;
- repair or bypass stale authoring receipts;
- alter CODEOWNERS, rulesets, required reviews, or repository settings;
- promote, release, deploy, publish, or authorize public use.

[Back to top](#top)

---

<a id="current-repository-evidence"></a>

## Current repository evidence

| Surface | Current verified state | Safe conclusion |
|---|---|---|
| ADR inventory | `ADR-0033` is uniquely indexed at this path with effective status `proposed`. | Identity confirmed; decision not accepted. |
| Accepted placement authority | ADR-0029 accepts Directory Rules v2 and keeps ADRs under `docs/adr/`. | Same-path modernization is placement-consistent. |
| [`docs/standards/GEOPARQUET.md`](../standards/GEOPARQUET.md) | Draft standards reference declares GeoParquet `1.1.0` and says `2.0` is not adopted. | Declared baseline only; draft prose is not production proof. |
| [`GeospatialCarrierReadinessCheck`](../../contracts/release/geospatial_carrier_readiness.md) | `PROPOSED_INACTIVE`, metadata-only profile for COG, MVT, and GeoParquet `1.1.0`; holds `2.x`; opens no carrier bytes. | Useful L1 candidate; cannot establish byte conformance or adoption. |
| Carrier schema/validator/tests | Closed synthetic shape with deterministic finite cases; current validator emits `GEOPARQUET_VERSION_NOT_ADOPTED` for `2.x`. | Declaration behavior is testable; byte/tool interoperability absent. |
| Carrier workflow | Latest main run `31654972027` failed overall. Focused tests passed (`14 passed`), all nine exact-polarity cases passed, then generated receipt validation failed with `ARTIFACT_DIGEST_MISMATCH`. | Semantic candidate remains coherent; proof-chain receipt is stale. Green status cannot be claimed. |
| [`STACGeoParquetMirrorAssessment`](../../contracts/data/stac_geoparquet_mirror_assessment.md) | Separate proposed-inactive synthetic assessment of declared STAC/GeoParquet projection parity. | Catalog projection candidate, not GeoParquet byte validation. |
| STAC mirror workflow | Latest main run `31654971667` passed focused deterministic tests and failed generated receipt integrity. | Same proof-chain limit; no format or release authority. |
| Geo manifest validator | Recognizes GeoParquet carrier/media binding. | Manifest/media recognition is not version interoperability. |
| `data/published/geoparquet/` | Root and atmosphere/flora/geology child lanes contain README and `.gitkeep` placeholders at the inspected revision. | Publication homes exist; no tracked carrier bytes were confirmed in these lanes. |
| Dependency manifests/locks | Prior bounded inventory recorded no declared `pyarrow`, `geopandas`, `duckdb`, GeoParquet, or Parquet reader/writer dependency. No later related dependency change was found in the inspected delta. | No repository-pinned production reader/writer matrix can be inferred. |
| Dedicated `DUAL_EVALUATE` profile | No contract/schema/fixture/validator/workflow using that outcome was found in bounded repository search. | Evaluation remains a proposal. |
| Original ADR authoring receipt | `genrec-geoparquet-version-readiness-20260810.json` binds the v1 ADR and index preimage; human review remains pending. | Historical v1 evidence only; it is not the v1.1 receipt. |
| CODEOWNERS | All relevant roots route to `@bartytime4life`; file explicitly disclaims stewardship, approval, and SoD proof. | One review route; no accepted role assignments or independent format approver. |
| Default-branch ruleset | Active `Protect` ruleset requires PR mediation and resolved review threads, but requires zero approvals, no code-owner review, no named reviewers, and no last-push approval. | Platform mediation exists; independent format approval is not enforced. |

### Current source-of-truth conflicts and limits

- The draft standard uses “canonical” language, but no accepted ADR or observed production release establishes operational adoption.
- The current carrier profile can return `READY` for declaration-level `1.1.0` metadata, but its contract explicitly denies byte-level and release implications.
- The original ADR receipt describes an exact earlier authoring packet; this revision must not rewrite that historical preimage into current evidence.
- Hosted workflow red status is caused by stale generated receipts after focused tests pass. That is evidence of proof-chain drift, not evidence that GeoParquet `1.1.0` or `2.x` semantics failed.

[Back to top](#top)

---

<a id="current-enforcement-maturity"></a>

## Current enforcement maturity

| Capability | Current state |
|---|---|
| ADR identity/status | `CONFIRMED / proposed` |
| Declared `1.1.0` standard | Draft reference; not independently accepted as production policy |
| `2.x` upstream status | `v2.0.0-rc.1`; release candidate |
| Metadata shape/profile | `PARTIAL / PROPOSED_INACTIVE` |
| Deterministic metadata fixtures | Present |
| Dedicated hosted workflow | Present but latest run red on generated receipt integrity |
| GeoParquet byte opening | Absent in inspected profile |
| Native logical-type validation | Absent |
| Cross-writer/reader/query matrix | Absent |
| Checked-in evaluation carrier bytes | None confirmed |
| Production reader/writer dependency | None confirmed |
| Downstream consumer registry | Absent / `UNKNOWN` |
| Mixed-version routing | Proposed only |
| Migration receipts | Absent |
| Correction/rollback drill | Absent |
| Independent qualified reviewer capacity | Not established |
| Required platform approval | Zero approvals required at inspected ruleset |
| Governed GeoParquet release instance | None confirmed |
| `2.x` operational adoption | `HOLD` |

**Overall maturity: `L1 / PARTIAL`, operational outcome `HOLD`.** Candidate metadata work may continue. No current evidence supports a claim of GeoParquet `2.x` readiness, production adoption, migration safety, or public release.

[Back to top](#top)

---

<a id="implementation-and-convergence-plan"></a>

## Implementation and convergence plan

Implement in small, dependency-ordered, reversible slices. Each slice must recheck current main, Directory Rules, concurrent work, and generated-receipt impact.

1. **Review this ADR without implying acceptance.** Preserve source/effective `proposed` until an authorized acceptance transition occurs.
2. **Keep the declared `1.1.0` baseline unchanged.** Do not edit standards, dependencies, data, or consumers in the documentation reconciliation.
3. **Repair inherited authoring-receipt drift separately.** Regenerate through the legitimate producer only after tracing each changed artifact; do not weaken receipt verification or bundle unrelated receipt repair into this ADR edit.
4. **Inventory real consumers.** Identify every writer, reader, query engine, pipeline, catalog projection, API/export, notebook, service, and published consumer, including external/downstream systems.
5. **Define the no-authority evaluation contract.** Select the accepted responsibility homes; specify exact inputs, byte artifacts, tool identities, checks, outcomes, reason codes, permissions fixed false, and non-effects.
6. **Add paired immutable synthetic bytes and negative fixtures.** Cover the dimensions in the dual-evaluation packet and bind them to deterministic generators or exact digests.
7. **Implement byte-level conformance validation.** Open files, inspect physical/logical types and metadata, recompute expected semantics, and fail closed on mismatches.
8. **Run a pinned interoperability matrix.** Exercise writer/reader/query/round-trip combinations and record preservation, loss, unsupported behavior, and deterministic results.
9. **Evaluate final stable `2.x`.** Re-run the matrix against the final tag and document any delta from the RC.
10. **Design migration, correction, and rollback.** Define dual-read window, artifact identity, migration receipts, catalog/cache changes, correction propagation, rollback targets, and drills.
11. **Propose adoption in a later decision packet.** Synchronize only the standards, contracts, schemas, policy, fixtures, validators, workflows, data/release docs, and consumers proven to be directly affected.
12. **Graduate only on observed evidence.** A final tag, green tests, or one successful tool does not substitute for the complete release packet.

### Documentation obligations

When behavior changes, update this ADR or an accepted successor, the ADR index if status/supersession changes, the GeoParquet standard, semantic contracts, machine schemas, policy, fixtures, validators, workflows, source/correction/rollback docs, consumer documentation, and generated receipts together as directly required.

[Back to top](#top)

---

<a id="acceptance-and-graduation-gates"></a>

## Acceptance and graduation gates

### ADR acceptance

- [ ] Architecture, geospatial, data-platform, standards/docs, contract/schema, validation, catalog/provenance, release, correction, and rollback reviewers approve the routing model.
- [ ] `KEEP_1_1`, `DUAL_EVALUATE`, `ADOPT_LATER`, and `DENY_UNSUPPORTED` meanings are agreed.
- [ ] The distinction between declared baseline, accepted policy, fixture evidence, and operational adoption is explicit.
- [ ] An RC cannot be represented as final stable `2.x`.
- [ ] Metadata-only checks cannot be represented as byte-level compatibility.
- [ ] Layout decisions remain benchmark-bound and separate from format version.
- [ ] Unsupported or unknown behavior fails closed.
- [ ] Current owner/reviewer and platform-control limitations remain visible.
- [ ] No statement claims current `2.x` adoption, migration, release, deployment, or publication.

### Dual-evaluation graduation

- [ ] Accepted no-authority evaluation contract/schema/profile exists.
- [ ] Dependencies are pinned, licensed, supply-chain reviewed, and represented in the evaluation packet.
- [ ] Paired public-safe carrier bytes and negative fixtures are immutable and digest-bound.
- [ ] Byte-level validator opens files and checks logical/physical type plus metadata semantics.
- [ ] Cross-tool matrix covers write, read, query, preserve, reject, round trip, and downgrade behavior.
- [ ] Tests are deterministic, no-network, and exercise finite failure paths.
- [ ] Exact-head authoring and replay receipts pass.
- [ ] Every permission for source activation, promotion, release, deployment, publication, and public use is fixed false.

### Adoption graduation

- [ ] Final stable `2.x` exists and is pinned.
- [ ] RC-to-final delta is re-evaluated.
- [ ] All confirmed consumers pass or have an approved migration/retirement plan.
- [ ] Dual-read window and exit criteria are approved.
- [ ] Migration receipts, identity, catalog/cache, correction, withdrawal, and rollback behavior are tested.
- [ ] Independent qualified reviewers are available and subject-bound review evidence exists.
- [ ] Release integration passes with exact carrier bytes and rollback targets.
- [ ] Observed fail-closed and recovery behavior is recorded.

[Back to top](#top)

---

<a id="consequences"></a>

## Consequences

### Positive

- Keeps the declared repository posture aligned with the current stable 1.x specification while upstream 2.0 remains an RC.
- Allows early interoperability work without silently changing production authority.
- Separates format semantics from physical layout tuning.
- Makes declaration, byte, tool, migration, release, and operational evidence distinct.
- Requires explicit mixed-version, downgrade, correction, and rollback behavior before data conversion.
- Preserves a reversible path to later `2.x` adoption.
- Prevents catalog, manifest, CI, or receipt surfaces from masquerading as format or release authority.

### Costs

- KFM receives no immediate native Parquet geospatial logical-type adoption.
- A credible evaluation requires admitted tools, immutable carrier bytes, multiple engines, and negative fixtures.
- Downstream consumers must be inventoried rather than inferred.
- Generated-receipt drift must be repaired through its legitimate producer before dedicated workflows can be trusted as green.
- Single-owner review routing may hold adoption until independent qualified capacity exists.

### Accepted tradeoff

The proposed decision accepts slower version adoption in exchange for stable semantics, explicit interoperability, reversible migration, and trustworthy correction behavior. Release-candidate results are useful evaluation evidence, not final adoption evidence.

### Preserved invariants

- No lifecycle phase or responsibility root changes.
- Promotion remains a governed state transition.
- Receipts, proofs, catalogs, decisions, reviews, manifests, corrections, rollback records, and published bytes remain distinct.
- Public clients remain behind governed released surfaces.
- Unknown compatibility fails closed.

[Back to top](#top)

---

<a id="alternatives-considered"></a>

## Alternatives considered

| Alternative | Disposition |
|---|---|
| Adopt GeoParquet `2.0` immediately | Rejected: latest upstream release is an RC; KFM lacks byte/tool/migration evidence. |
| Treat the draft standard's “canonical” wording as accepted operational policy | Rejected: document status and observed release evidence do not support that claim. |
| Reject all `2.x` evaluation until final release | Rejected: a no-authority RC evaluation can expose compatibility gaps early. |
| Allow `2.x` by extending the declaration-only profile | Rejected: declarations cannot prove native logical types, statistics, CRS, preservation, or downgrade behavior. |
| Use one implementation as compatibility proof | Rejected: writer-only or reader-only success does not establish cross-engine interoperability. |
| Make the motivating layout recipe mandatory | Rejected: version conformance and physical optimization are independent. |
| Rewrite real KFM products as the first evaluation | Rejected: synthetic public-safe fixtures provide a smaller reversible boundary. |
| Let a green workflow or receipt authorize adoption | Rejected: checks and receipts are evidence surfaces, not accountable decisions or release authority. |
| Leave the issue only in exploratory intake | Rejected: finite routing is now useful to prevent accidental adoption while preserving a bounded next step. |

[Back to top](#top)

---

<a id="risk-and-open-question-ledger"></a>

## Risk and open-question ledger

| Item | Status | Required resolution |
|---|---|---|
| Final `2.x` specification | `NEEDS VERIFICATION` | Wait for and pin final stable tag; compare against evaluated RC. |
| Declared standard authority | `CONFLICTED` | Reconcile draft “canonical” wording with accepted ADR/policy and operational evidence. |
| Real writers/readers/query engines | `UNKNOWN` | Complete consumer/tool inventory with owners and pinned versions. |
| GeoParquet carrier bytes | `ABSENT IN INSPECTED LANES` | Add only public-safe synthetic evaluation bytes in a governed packet. |
| Native logical-type support | `UNKNOWN` | Byte-level, cross-engine tests. |
| CRS and edge semantics | `OPEN` | Define preservation and failure expectations per tool/profile. |
| Spatial statistics parity | `OPEN` | Compare `1.1` covering behavior and `2.x` native statistics without assuming equivalence. |
| Unknown extension metadata | `OPEN` | Require preserve/reject behavior and negative fixtures. |
| Mixed-version collection | `OPEN` | Define routing, catalog signaling, correction, and query behavior. |
| Downgrade behavior | `OPEN` | Deny semantic loss; define explicit supported transformations if any. |
| Deterministic identity after migration | `OPEN` | Decide object identity versus byte identity and receipt linkage. |
| Physical layout | `BENCHMARK_BOUND` | Keep per-dataset workload evidence; no universal constants. |
| Generated carrier receipt | `STALE` | Trace artifact change and regenerate through legitimate producer in separate work. |
| Generated STAC-mirror receipt | `STALE` | Same bounded repair; no validator weakening. |
| Original ADR receipt | `HISTORICAL` | Retain as v1 preimage evidence; do not claim it covers v1.1. |
| CODEOWNERS route | `CONFIRMED LIMIT` | Add verified qualified owners only after accepted assignments. |
| Required platform approval | `ZERO` | Governance decision needed before relying on platform-enforced independent review. |
| External/downstream consumers | `UNKNOWN` | Identify owners, versions, support commitments, and migration constraints. |
| Correction after tool regression | `OPEN` | Define withdrawal, cache invalidation, revalidation, and rollback sequence. |
| Operational release evidence | `NONE CONFIRMED` | Produce only after accepted adoption and full release closure. |

[Back to top](#top)

---

<a id="migration-correction-and-rollback"></a>

## Migration, correction, and rollback

### Current documentation-only change

This v1.1 revision changes no format, implementation, dependency, data, or consumer. Its rollback target is the immediate prior ADR blob:

```text
239acc3978ac67fb71f9acc6a675d28a8a92c55c
```

A transparent revert restores the prior proposed documentation. It does not alter format support, data, release state, or public artifacts.

### Historical authoring receipt

`data/receipts/generated/genrec-geoparquet-version-readiness-20260810.json` binds the original v1 ADR and index hashes. Retain it as historical authoring evidence. Do not edit it to pretend those hashes describe v1.1. A new receipt, when required by repository process, must be emitted separately by the legitimate producer and bind the actual new bytes.

### If ADR-0033 is later accepted

Accepted ADRs are governance history. Do **not** flip an accepted decision back to `proposed` or silently weaken it. A material change requires an accepted successor/status transition, reciprocal supersession links, index update, migration plan, compatibility evidence, correction analysis, and rollback consequences.

### If `2.x` is later adopted

A governed migration must:

1. freeze the exact source bytes and target specification/toolchain;
2. emit migration receipts for every artifact;
3. retain prior bytes and identities according to policy;
4. update catalog/release references atomically or through an explicit dual-read state;
5. validate semantic equivalence or record intentional change;
6. propagate corrections and cache invalidation;
7. prove rollback to the last supported public-safe state;
8. preserve decision/review history.

Disabling validation, deleting original bytes, changing version declarations without bytes, or downgrading the maturity requirement to unblock release is not an acceptable rollback strategy.

[Back to top](#top)

---

<a id="verification-checklist"></a>

## Verification checklist

### Current v1.1 revision

- [x] Current `main` and target blob rechecked before editing.
- [x] ADR ID, filename, H1, path, and effective `proposed` status preserved.
- [x] Accepted ADR-0029 and Directory Rules placement authority reviewed.
- [x] GeoParquet standard, carrier candidate, STAC mirror candidate, manifest validator, publication lanes, receipt, CODEOWNERS, ruleset, and hosted runs inspected.
- [x] Official upstream release status rechecked on 2026-08-14.
- [x] Declared baseline separated from accepted operational adoption.
- [x] Declaration-level proof separated from byte-level and cross-tool proof.
- [x] Current stale-receipt workflow failures recorded without attributing semantic failure.
- [x] Original receipt retained as historical v1 evidence.
- [x] Finite outcomes, evidence ladder, dual-evaluation packet, adoption gates, denial boundary, layout boundary, risks, and rollback refreshed.
- [x] No standard, dependency, schema, contract, validator, fixture, workflow, receipt, data, runtime, release, deployment, or publication change introduced.
- [ ] Human review completed.
- [ ] ADR accepted.
- [ ] Dual evaluation implemented.
- [ ] Final stable `2.x` evaluated.
- [ ] Governed adoption observed.

### Future dual evaluation

- [ ] Contract/schema/profile accepted and fixed no-authority.
- [ ] Tools and locks admitted.
- [ ] Paired carrier bytes and negative fixtures digest-bound.
- [ ] Byte-level validator and deterministic replay pass.
- [ ] Cross-tool write/read/query/round-trip matrix complete.
- [ ] CRS, statistics, extensions, null/empty, mixed-version, and downgrade cases covered.
- [ ] Exact-head receipts pass.
- [ ] No production read/write, promotion, release, deployment, or publication effect.

### Future adoption

- [ ] Final stable tag pinned.
- [ ] All consumers inventoried and reviewed.
- [ ] Dual-read and migration plan approved.
- [ ] Correction/withdrawal/rollback drills pass.
- [ ] Release packet binds exact carrier bytes and rollback targets.
- [ ] Independent qualified review and platform/governance parity verified.

[Back to top](#top)

---

<a id="references"></a>

## References

### Repository authority and implementation evidence

| Reference | Relationship and current boundary |
|---|---|
| [`docs/adr/README.md`](./README.md) | ADR operating contract; merge does not accept a decision. |
| [`docs/adr/INDEX.md`](./INDEX.md) | Confirms ADR-0033 identity and effective `proposed` status. |
| [ADR-0001](./ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) | Proposed schema-home decision relevant to any future evaluation schema. |
| [ADR-0011](./ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md) | Keeps evaluation results, receipts, proofs, manifests, catalog records, and release distinct. |
| [ADR-0013](./ADR-0013-spec_hash-and-run_id-identity-grammar.md) | Proposed deterministic identity grammar relevant to fixtures and migration receipts. |
| [ADR-0018](./ADR-0018-promotion-gate-sequence.md) | Promotion/release boundary; version readiness is not promotion. |
| [ADR-0020](./ADR-0020-abstain-is-a-first-class-decision.md) | Missing compatibility evidence may hold/abstain rather than guess. |
| [ADR-0029](./ADR-0029-adopt-directory-governance-standard-v2.md) | Accepted placement authority. |
| [Directory Rules](../doctrine/directory-rules.md) | Responsibility-root placement and migration discipline. |
| [GeoParquet standards reference](../standards/GEOPARQUET.md) | Draft declaration of `1.1.0`; not production proof. |
| [Governed source map](../intake/exploratory/spatiotemporal-modernization-blueprint-source-map.md) | Proposal intake, conflict analysis, and decision lineage. |
| [Geospatial carrier contract](../../contracts/release/geospatial_carrier_readiness.md) | Metadata-only `1.1.0` candidate; no byte/release authority. |
| [Carrier schema](../../schemas/contracts/v1/release/geospatial_carrier_readiness.schema.json) | Closed declared-metadata shape. |
| [Carrier validator](../../tools/validators/release/validate_geospatial_carrier_readiness.py) | Deterministic declarations; holds `2.x`. |
| [Carrier tests](../../tests/release/test_geospatial_carrier_readiness.py) | Focused synthetic polarity coverage. |
| [Carrier workflow](../../.github/workflows/geospatial-carrier-readiness.yml) | Hosted candidate check; latest main run red on stale receipt. |
| [STAC mirror contract](../../contracts/data/stac_geoparquet_mirror_assessment.md) | Declared projection parity; no carrier-byte conformance. |
| [STAC mirror workflow](../../.github/workflows/stac-geoparquet-mirror-assessment.yml) | Hosted synthetic check; latest main run red on stale receipt. |
| [Geo manifest validator](../../tools/validators/evidence/validate_kfm_geo_manifest.py) | Carrier/media binding, not version compatibility. |
| [GeoParquet publication lanes](../../data/published/geoparquet/README.md) | Release-gated target lanes; no confirmed carrier bytes in inspected children. |
| [Original ADR receipt](../../data/receipts/generated/genrec-geoparquet-version-readiness-20260810.json) | Historical v1/index authoring preimage; not v1.1 receipt. |
| [CODEOWNERS](../../.github/CODEOWNERS) | One-account review routing; no stewardship or approval proof. |
| Repository ruleset `Protect` (`15484585`) | PR mediation and thread resolution; zero approving reviews required at inspected checkpoint. |

### Primary upstream evidence

- [Official GeoParquet release index](https://geoparquet.org/releases/) — release-channel inventory.
- [Official GeoParquet releases](https://github.com/opengeospatial/geoparquet/releases) — `v2.0.0-rc.1` remains the latest listed release at the evidence checkpoint.
- [GeoParquet `v2.0.0-rc.1` release](https://github.com/opengeospatial/geoparquet/releases/tag/v2.0.0-rc.1) — RC purpose and change summary at commit `0c7fab74cf1177e2fe61df8eb7fcd1813b73e4aa`.
- [Pinned 2.0 RC specification](https://github.com/opengeospatial/geoparquet/blob/0c7fab74cf1177e2fe61df8eb7fcd1813b73e4aa/format-specs/geoparquet.md) — native Parquet geospatial logical types and optional GeoParquet metadata.
- [Corrected 1.1 release/tag](https://github.com/opengeospatial/geoparquet/releases/tag/v1.1.0%2Bp1) — corrected stable 1.1 source while metadata version remains `1.1.0`.
- [Pinned corrected 1.1 specification](https://github.com/opengeospatial/geoparquet/blob/540f6bf547587284e632c47530bc08d9e43bb045/format-specs/geoparquet.md) — `1.1.0` baseline.

External release status and specification details are confirmed only for the pinned revisions and the 2026-08-14 access checkpoint. Later final-release or compatibility claims remain `NEEDS VERIFICATION`.

[Back to top](#top)

---

<a id="revision-history"></a>

## Revision history

| Version | Date | Summary |
|---|---|---|
| `v1.1` | 2026-08-14 | Same-path repository reconciliation against `main@3e1a929a...`: preserves source/effective `proposed`; distinguishes the draft declared `1.1.0` baseline from operational adoption; rechecks upstream `v2.0.0-rc.1`; records current candidate contracts, byte-level gaps, publication placeholders, stale authoring-receipt workflow failures, CODEOWNERS/ruleset limits, and historical receipt boundary; adds evidence maturity, a complete dual-evaluation packet, adoption graduation, future reason-code families, convergence plan, acceptance gates, risk ledger, verification checklist, exact rollback target, refreshed references, and a no-loss ledger. |
| `v1` | 2026-08-10 | Initial proposed version-readiness boundary from governed Drive intake, repository inventory, and pinned GeoParquet release evidence. |

---

<a id="appendix-a--no-loss-modernization-ledger"></a>

## Appendix A — No-loss modernization ledger

| Prior v1 material | v1.1 treatment |
|---|---|
| Title, ID, exact path, source status, and effective status | **Preserved**; `proposed` remains unchanged. |
| Motivation from *Kansas Frontier Matrix Improvements* and governed source map | **Preserved** as proposal/source lineage, not authority. |
| Upstream RC and corrected 1.1 pins | **Preserved and rechecked** on 2026-08-14. |
| Repository inventory of standard, carrier, STAC mirror, manifest, publication lanes, and dependencies | **Preserved and refreshed** with current blobs/runs/placeholder lanes. |
| `KEEP_1_1`, `DUAL_EVALUATE`, `ADOPT_LATER`, `DENY_UNSUPPORTED` | **Preserved and expanded** with entry, maturity, and effect boundaries. |
| Entry evidence for dual evaluation | **Preserved and expanded** into tool, byte, fixture, operation, outcome, non-effect, and receipt requirements. |
| Evidence required before adoption | **Preserved and expanded** with consumer, correction, rollback, review, and release closure. |
| Denial conditions | **Preserved and expanded** with proposed reason-code families while identifying current implemented code separately. |
| Benchmark-bound layout rule | **Preserved** and sharpened; no universal layout constants adopted. |
| Consequences and alternatives | **Preserved and updated** for current evidence and proof-chain drift. |
| Migration plan | **Preserved** as not applicable to this docs-only revision; future migration obligations expanded. |
| Rollback | **Preserved and corrected** to exact prior blob plus historical-receipt handling and successor discipline. |
| Open questions | **Preserved and expanded** into a status-bearing risk ledger. |
| Change history | **Preserved** with v1.1 appended. |
| Standard, dependency, data, runtime, release, deployment, publication effect | **Unchanged:** none. |

---

<sub>**Last updated:** 2026-08-14 · **Source/effective status:** `proposed` · **Declared baseline:** GeoParquet `1.1.0` · **Upstream:** `v2.0.0-rc.1` · **Evidence maturity:** `L1 / PARTIAL` · **Operational adoption:** `HOLD` · **Publication:** none · **Path:** `docs/adr/ADR-0033-geoparquet-version-readiness.md`</sub>
