<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://adr/ADR-0033
title: Keep GeoParquet 1.1 as the default and gate 2.0 evaluation
type: adr
version: v1
status: proposed
owners: ["Architecture steward", "Geospatial steward", "Data platform steward", "Release steward"]
created: 2026-08-10
updated: 2026-08-10
policy_label: public
owning_root: docs/
responsibility: proposed cross-component version-readiness decision for GeoParquet without changing the adopted standard, dependencies, data, runtime, or release state
truth_posture: CONFIRMED repository inventory and pinned upstream evidence / PROPOSED decision and finite outcomes / UNKNOWN implementation compatibility and adoption timing / NEEDS VERIFICATION final 2.x release and operational consumers
related:
  - "docs/doctrine/directory-rules.md"
  - "docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md"
  - "docs/standards/GEOPARQUET.md"
  - "docs/intake/exploratory/spatiotemporal-modernization-blueprint-source-map.md"
  - "contracts/release/geospatial_carrier_readiness.md"
  - "contracts/data/stac_geoparquet_mirror_assessment.md"
tags: [adr, kfm, geoparquet, parquet, geospatial, compatibility, migration, governance]
supersedes: []
superseded_by: []
notes:
  - "PROPOSED: this record changes no KFM standard or format default and authorizes no data rewrite, dependency, source activation, release, deployment, or publication."
  - "Upstream evidence was rechecked on 2026-08-10: v2.0.0-rc.1 is a release candidate, not a final 2.x release."
[/KFM_META_BLOCK_V2] -->

# ADR-0033: Keep GeoParquet 1.1 as the default and gate 2.0 evaluation

KFM should keep GeoParquet `1.1.0` as its adopted default while the upstream `2.0.0-rc.1` release candidate and KFM's own reader, writer, validator, migration, and rollback compatibility remain unproved. A separately reviewed, dependency-closed evaluation may compare both versions with synthetic public-safe fixtures; production adoption remains a later decision.

| Field | Value |
|---|---|
| **ID** | ADR-0033 |
| **Status** | proposed |
| **Date** | 2026-08-10 |
| **Deciders** | Architecture steward · Geospatial steward · Data platform steward · Release steward |
| **Consulted** | Standards · catalog · evidence · pipeline · validation · correction/rollback stewards |
| **Informed** | Domain · governed-API · map-client · documentation maintainers |
| **Supersedes** | — |
| **Superseded by** | — |
| **Directory Rules trigger** | `n/a — non-structural cross-component decision`; invariant-preserving boundary under §§3, 4, and 6 |
| **Primary responsibility root** | `docs/` |
| **Migration required** | no for this proposal; required before any later adoption |
| **Rollback required** | yes, documentation-only for this proposal |
| **Truth posture** | CONFIRMED current repository/upstream evidence · PROPOSED decision · UNKNOWN compatibility and adoption timing |

---

## 1. Context

The governed source map for *Kansas Frontier Matrix Improvements* identifies GeoParquet version readiness as a decision candidate. The motivating Google Drive document proposes mandatory GeoParquet 2.0 plus fixed layout choices. The source map rejects direct transfer: a format version and a dataset-specific physical layout answer different questions, and neither a proposal document nor a mutable upstream branch is adoption evidence.

KFM's current standards reference explicitly tracks GeoParquet `1.1.0`. Its inactive geospatial-carrier preflight also holds 2.x declarations and states that a separate version-readiness decision is still required. Adjacent repository work makes layout parameters reviewable and assesses a declared STAC GeoParquet mirror projection, but neither opens Parquet bytes nor proves cross-version compatibility.

On 2026-08-10, the official GeoParquet release index and upstream GitHub release page listed `v2.0.0-rc.1` as the latest release. The release notes call it a release candidate for final implementation testing and warn that details may change before final `2.0.0`. The tag and current upstream `main` resolve to commit `0c7fab74cf1177e2fe61df8eb7fcd1813b73e4aa`. The corrected stable 1.1 specification remains identified by version `1.1.0`; its `v1.1.0+p1` tag peels to `540f6bf547587284e632c47530bc08d9e43bb045`.

### 1.1 Why a decision is required

GeoParquet 2.0 is not a minor metadata-only substitution. The release candidate recenters the format on native Parquet `GEOMETRY` and `GEOGRAPHY` logical types and their spatial statistics. The KFM 1.1 profile currently expects 1.1 metadata, WKB geometry declaration, and an optional bbox covering. Version-sensitive readers, writers, validators, catalog projections, correction paths, and downgrade behavior therefore need explicit evidence before any default changes.

### 1.2 Confirmed repository inventory

The following bounded inventory was performed at `main@9e76413313b8529091d01be6132d6e987e3f9fae` on 2026-08-10.

| Surface | Confirmed state | Version-readiness limit |
|---|---|---|
| [`docs/standards/GEOPARQUET.md`](../standards/GEOPARQUET.md) | Tracks GeoParquet `1.1.0` and says 2.0 is not adopted. | Human profile; no 2.0 compatibility proof. |
| [`contracts/release/geospatial_carrier_readiness.md`](../../contracts/release/geospatial_carrier_readiness.md), paired schema, validator, fixtures, and tests | Inactive declared-metadata preflight; holds 2.x and records benchmark-bound layout choices. | Does not open Parquet bytes and explicitly does not satisfy the version decision. |
| [`contracts/data/stac_geoparquet_mirror_assessment.md`](../../contracts/data/stac_geoparquet_mirror_assessment.md) and paired packet | Compares declared STAC projection parity under an exact upstream pin. | Does not read Parquet or establish GeoParquet conformance. |
| [`tools/validators/evidence/validate_kfm_geo_manifest.py`](../../tools/validators/evidence/validate_kfm_geo_manifest.py) | Recognizes the GeoParquet carrier kind and `application/vnd.apache.parquet`. | Media binding is not format or version compatibility. |
| [`data/published/geoparquet/README.md`](../../data/published/geoparquet/README.md) and child READMEs | Define release-gated target lanes. | Bounded repository search found no tracked `.parquet` or `.geoparquet` file. README presence is not a published artifact. |
| Dependency manifests and lockfiles | Bounded search found no declared `pyarrow`, `geopandas`, `duckdb`, `geoparquet`, or Parquet dependency. | No repository-pinned reader/writer matrix can be inferred. |

This is a path-and-declaration inventory, not proof that no external consumer exists. Untracked services, local tools, and downstream users remain `UNKNOWN` until their owners provide evidence.

### 1.3 Evidence boundary

- **CONFIRMED:** KFM's declared default is GeoParquet 1.1.0; its existing carrier check is inactive and declared-metadata-only.
- **CONFIRMED:** upstream `v2.0.0-rc.1` is a release candidate at the pinned commit above, not a final 2.x release.
- **CONFIRMED:** the bounded repository search found no tracked Parquet data and no pinned reader/writer dependency in the searched manifests.
- **PROPOSED:** use the finite outcomes below for version-readiness routing.
- **UNKNOWN:** compatibility of actual KFM or downstream readers, writers, validators, query engines, and published consumers.
- **NEEDS VERIFICATION:** final 2.x specification and schema, supported implementation versions, migration and downgrade behavior, correction and rollback obligations, and workload-specific performance.

### 1.4 Out of scope

This ADR does not edit the KFM GeoParquet standard, activate the existing carrier profile, add a library or service, create a Parquet file, convert or rewrite data, admit a source, run a benchmark, alter catalog authority, release an artifact, deploy a reader, or publish anything.

---

## 2. Decision

> **Decision:** Route the current repository to `KEEP_1_1`. Permit `DUAL_EVALUATE` only through a separate, dependency-closed synthetic-fixture change. Reserve `ADOPT_LATER` for a final stable 2.x release plus accepted compatibility, migration, correction, and rollback evidence. Use `DENY_UNSUPPORTED` whenever a candidate's declared or observed version cannot be safely handled.

### 2.1 Finite outcomes

| Outcome | Meaning | Permitted effect |
|---|---|---|
| `KEEP_1_1` | GeoParquet 1.1.0 remains KFM's adopted default. | Continue current declared profile; do not change standards, bytes, dependencies, or consumers. |
| `DUAL_EVALUATE` | A bounded comparison of pinned 1.1 and 2.0 candidate behavior has met the entry evidence below. | A separate PR may add admitted tooling plus public-safe synthetic fixtures, byte-level validation, a compatibility matrix, tests, and an authoring receipt. No production read/write or release. |
| `ADOPT_LATER` | A final stable 2.x release and the full acceptance evidence exist. | Propose a successor acceptance/change packet that updates standards and versioned implementation surfaces with migration and rollback. This ADR alone cannot adopt 2.x. |
| `DENY_UNSUPPORTED` | A version, logical type, metadata combination, reader/writer behavior, mixed-version set, or downgrade cannot be interpreted under an accepted profile. | Fail closed with finite reasons; hold the artifact and make no release or publication claim. |

These outcomes are architecture-routing vocabulary. They do not replace validator results, policy decisions, promotion decisions, release manifests, or public-answer envelopes.

### 2.2 Entry evidence for `DUAL_EVALUATE`

A separate evaluation PR **MUST** provide:

1. immutable upstream spec and schema pins for both versions, including the exact 2.0 candidate or final tag;
2. dependency-governance evidence for each admitted reader, writer, validator, and query engine;
3. public-safe synthetic fixtures covering geometry/geography logical types, CRS forms, spatial statistics, 1.1 bbox covering, unknown metadata, mixed versions, invalid metadata, and downgrade refusal;
4. a matrix naming each tool/version and its read, write, validate, query, preserve, and reject behavior;
5. deterministic no-network tests with finite `PASS`, `ABSTAIN`, `DENY`, or `ERROR` behavior at the owning validator boundary;
6. fixed-false effects for data rewrite, source activation, promotion, release, deployment, publication, and public-client consumption; and
7. an authoring receipt binding dependencies, fixtures, commands, outputs, and exact artifact hashes.

Release-candidate results may inform a later decision but cannot establish final-version conformance.

### 2.3 Evidence required before `ADOPT_LATER`

Adoption requires a separately reviewed status transition or successor ADR and all of the following:

- an official final stable 2.x specification/schema tag, not `main` or an RC;
- compatibility results for every confirmed KFM writer, reader, validator, query engine, workflow, catalog projection, and published consumer;
- a versioned dual-read window with explicit start, end, owner, and telemetry/evidence criteria;
- byte-identity and semantic-equivalence checks for representative public-safe fixtures;
- a migration receipt model covering inputs, outputs, tool versions, parameters, digests, and failures;
- explicit mixed-version, unsupported-version, downgrade, correction, withdrawal, and rollback behavior;
- a repository-wide path and dependency impact review;
- reviewer acceptance from architecture, geospatial, data platform, catalog, validation, release, and correction/rollback owners; and
- synchronized updates to the standard, contracts, schemas, validators, fixtures, tests, workflows, docs, and receipts actually affected.

### 2.4 `DENY_UNSUPPORTED` conditions

A carrier **MUST** be held when any of these conditions applies:

- its declared GeoParquet version is absent, malformed, conflicting, or outside an accepted/evaluation profile;
- its observed Parquet logical type or GeoParquet metadata conflicts with the declared version;
- the active reader cannot preserve required geometry, CRS, statistics, metadata, null, ordering, or identity semantics;
- a mixed-version collection lacks an accepted routing and correction plan;
- a downgrade would discard or reinterpret consequential content; or
- a validator only inspects declarations where byte-level proof is required.

The denial must identify the unsupported surface without treating the artifact as corrupt, malicious, or false unless separate evidence proves that claim.

### 2.5 Layout decisions remain benchmark-bound

Version selection does not select a universal physical layout. Compression, compression level, ordering method, row-group rows/bytes, partitioning, file size, and index strategy remain dataset- and workload-specific. The existing inspectable layout profile and its benchmark reference remain the correct boundary. Neither this ADR nor the motivating document makes Hilbert ordering, one row-group range, ZSTD parameters, H3/S2 partitioning, or a single grid resolution mandatory for all KFM data.

### 2.6 Placement basis

| Question | Answer |
|---|---|
| **Primary responsibility** | Cross-component version-readiness decision and migration boundary |
| **Owning root** | `docs/adr/` |
| **Domain segment** | `n/a — cross-domain` |
| **Lifecycle phase** | `n/a`; this record creates no data object or transition |
| **Directory Rules basis** | §§3, 4, and 6: keep standards, semantic contracts, machine shape, validation, data, and release authority in their owning roots |
| **Parallel authority risk** | Mitigated by leaving `docs/standards/GEOPARQUET.md` unchanged and requiring later implementation in existing canonical homes |

### 2.7 Conformance language

- KFM **MUST** keep `1.1.0` as the default unless an accepted later decision changes it.
- Evaluations **MUST** pin upstream version, schema, and tool identities and **MUST** use public-safe synthetic data without network access.
- An RC **MUST NOT** be represented as a final stable 2.x release.
- A format check **MUST NOT** imply source, evidence, policy, review, promotion, release, deployment, or publication authority.
- Unknown or unsupported version behavior **MUST** fail closed as `DENY_UNSUPPORTED` at this routing boundary.
- Implementations **SHOULD** preserve sufficient information for correction, replay, and rollback.
- A later change **MAY** propose `ADOPT_LATER` only with the full evidence in §2.3.

---

## 3. Consequences

### 3.1 Positive

- Keeps the production/default posture aligned with KFM's current stable standard.
- Makes release-candidate experimentation possible without silently adopting it.
- Separates wire-format compatibility from workload-specific layout tuning.
- Creates explicit failure and downgrade behavior before data conversion begins.
- Preserves a reversible path to final 2.x adoption.

### 3.2 Negative

- KFM receives no immediate native Parquet geospatial-type capability.
- A useful evaluation requires dependency review, synthetic fixture design, and multi-tool compatibility work.
- Downstream consumers must be inventoried rather than inferred from repository declarations.

### 3.3 Accepted tradeoffs

The project accepts slower version adoption in exchange for stable semantics, explicit compatibility, reversible migration, and trustworthy correction behavior. Release-candidate evidence is useful, but it remains evaluation evidence.

### 3.4 Affected surfaces

| Surface | Impact |
|---|---|
| ADRs | Adds this proposed, non-binding decision record and index row. |
| Standards | No change; GeoParquet 1.1.0 remains the declared KFM default. |
| Contracts, schemas, validators | No change; existing profiles remain proposed/inactive within their stated bounds. |
| Dependencies, fixtures, tests, workflows | No change; a dual evaluation requires a separate PR. |
| Data, catalog, and published lanes | No bytes or records added, converted, moved, released, or published. |
| Runtime and clients | No reader, writer, service, API, or UI behavior changes. |

---

## 4. Alternatives considered

### 4.1 Adopt GeoParquet 2.0 immediately

- **Summary:** Update the KFM standard to the RC and begin producing native Parquet geospatial logical types.
- **Why rejected:** The upstream release is explicitly a candidate, KFM has no pinned implementation matrix, and migration/correction/rollback behavior is unproved.

### 4.2 Reject 2.x evaluation until final release

- **Summary:** Keep 1.1 and perform no compatibility work before final 2.x.
- **Why rejected:** A bounded RC evaluation can expose tool and semantic gaps early without changing production authority.

### 4.3 Accept declarations without opening Parquet bytes

- **Summary:** Extend the current metadata preflight to allow a `2.x` version string.
- **Why rejected:** Version-sensitive logical types, statistics, CRS representation, and downgrade behavior cannot be proved by declaration alone.

### 4.4 Make the motivating document's physical layout mandatory

- **Summary:** Couple 2.0 adoption to one compression, ordering, row-group, and partition strategy.
- **Why rejected:** Format conformance and physical optimization are independent; KFM's existing profile correctly requires benchmark-bound, dataset-specific evidence.

### 4.5 Leave the issue only in exploratory intake

- **Summary:** Take no architecture position until an implementation appears.
- **Why rejected:** Upstream has now published an RC and the proposal is implementation-shaped. Finite routing prevents accidental adoption while preserving a safe next step.

---

## 5. Evidence and references

### 5.1 Governed input and repository evidence

- [*Kansas Frontier Matrix Improvements*](https://docs.google.com/document/d/1qH0oVs3vQN0YXhk_vASnrwAmJORL_vQigOM0cfHJSDI) — motivating proposal; not authority.
- [`docs/intake/exploratory/spatiotemporal-modernization-blueprint-source-map.md`](../intake/exploratory/spatiotemporal-modernization-blueprint-source-map.md) — complete-source triage, conflicts, candidate map, and recommended decision-only action.
- [`docs/standards/GEOPARQUET.md`](../standards/GEOPARQUET.md) — current KFM version posture.
- [`contracts/release/geospatial_carrier_readiness.md`](../../contracts/release/geospatial_carrier_readiness.md) — inactive declared-metadata and dataset-specific layout boundary.
- [`contracts/data/stac_geoparquet_mirror_assessment.md`](../../contracts/data/stac_geoparquet_mirror_assessment.md) — declared projection-parity boundary; not byte-level compatibility.
- [`docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md`](./ADR-0029-adopt-directory-governance-standard-v2.md) — accepted placement authority.

### 5.2 Pinned primary upstream evidence

- [Official GeoParquet release index](https://geoparquet.org/releases/) — release-channel inventory checked 2026-08-10.
- [GeoParquet `v2.0.0-rc.1` release](https://github.com/opengeospatial/geoparquet/releases/tag/v2.0.0-rc.1) — RC purpose and change summary at commit `0c7fab74cf1177e2fe61df8eb7fcd1813b73e4aa`.
- [Pinned 2.0 specification](https://github.com/opengeospatial/geoparquet/blob/0c7fab74cf1177e2fe61df8eb7fcd1813b73e4aa/format-specs/geoparquet.md) — native Parquet geospatial logical types and versioned metadata.
- [Pinned corrected 1.1 specification](https://github.com/opengeospatial/geoparquet/blob/540f6bf547587284e632c47530bc08d9e43bb045/format-specs/geoparquet.md) — stable baseline identified as `1.1.0`.

External release status and specification details are confirmed only for the pinned evidence date and revisions. Future final-release or compatibility claims remain `NEEDS VERIFICATION`.

---

## 6. Migration plan

Not applicable to this proposed decision packet. It changes no standard, implementation, dependency, data, or consumer. A later adoption proposal must provide the dual-read window, migration receipts, synchronized surface updates, downgrade rules, correction behavior, and rollback plan required by §2.3.

---

## 7. Rollback plan

Before merge, close the draft pull request and delete only its scoped branch if desired. After merge, reject or supersede this ADR through normal ADR governance and update `docs/adr/INDEX.md` in the same reviewed change. Revert or supersede the paired generated authoring receipt according to receipt-retention policy. No data, dependency, runtime, release, deployment, or publication state requires rollback.

---

## 8. Open questions

- Which external or downstream KFM consumers exist beyond the bounded repository inventory, and who owns them?
- Which reader/writer implementations can create and preserve GeoParquet 2.0 logical types and statistics at pinned versions?
- What exact mixed-version collection behavior is required during a dual-read window?
- Which representative public-safe geometry, CRS, statistics, metadata, and failure cases belong in an evaluation fixture matrix?
- What evidence is sufficient to prove semantic equivalence where 1.1 bbox covering and 2.0 native statistics differ?
- What correction and rollback sequence applies if an adopted reader later changes or loses support?

---

## 9. Change history

| Date | Status | Change | PR |
|---|---|---|---|
| 2026-08-10 | proposed | Initial version-readiness boundary from governed Drive intake, current repository inventory, and pinned GeoParquet release evidence. | pending |
