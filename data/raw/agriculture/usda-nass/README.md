<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/agriculture/usda-nass/readme
name: USDA NASS Raw Agriculture README
path: data/raw/agriculture/usda-nass/README.md
type: data-raw-source-lane-readme
version: v0.2.0
status: draft
owners:
  - "NEEDS VERIFICATION: agriculture domain steward"
  - "NEEDS VERIFICATION: source steward"
  - "NEEDS VERIFICATION: USDA NASS source steward"
  - "NEEDS VERIFICATION: data steward"
  - "NEEDS VERIFICATION: rights and sensitivity reviewers"
created: 2026-06-27
updated: 2026-07-26
policy_label: restricted-review
truth_posture: cite-or-abstain
lifecycle_phase: raw
responsibility_root: data/
domain: agriculture
source_family: usda-nass
artifact_family: immutable-source-capture
sensitivity_posture: raw-internal; source-role-preserving; rights-needs-verification; aggregate-only-guard-required; field-level-claims-deny; release-blocked
prepared_under_prompt: KFM Markdown Modernization & GitHub Documentation Implementation Agent v4.0.0
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_commit: 2cf6f4322d34adcd441835cb969563b5f64f99b6
  target_blob: 1c6f863bf59b63b4b916957c2ad609df346e86b8
  method: complete target read; bounded repository contents and code-search inspection; no external USDA endpoint or runtime request
related:
  - ../README.md
  - ../../README.md
  - ../../../README.md
  - ../../usda-nass/README.md
  - ../../../quarantine/agriculture/README.md
  - ../../../processed/agriculture/README.md
  - ../../../catalog/domain/agriculture/README.md
  - ../../../published/layers/agriculture/README.md
  - ../../../registry/sources/README.md
  - ../../../../docs/domains/agriculture/SOURCE_REGISTRY.md
  - ../../../../docs/domains/agriculture/SOURCES.md
  - ../../../../docs/domains/agriculture/SENSITIVITY.md
  - ../../../../docs/sources/catalog/usda/usda-nass-quickstats.md
  - ../../../../docs/sources/catalog/usda/usda-nass-cdl.md
  - ../../../../connectors/nass/README.md
  - ../../../../connectors/usda-nass/README.md
  - ../../../../fixtures/domains/agriculture/nass_quickstats/README.md
  - ../../../../fixtures/domains/agriculture/no_network/nass/README.md
  - ../../../../release/manifests/README.md
tags:
  - kfm
  - data
  - raw
  - agriculture
  - usda
  - usda-nass
  - nass
  - quickstats
  - crop-progress
  - cdl
  - aggregate
  - source-role
  - rights-review
  - immutable-capture
  - evidence-first
notes:
  - "This same-path revision preserves the USDA NASS RAW Agriculture source-lane identity and strengthens its evidence boundary."
  - "The parent `data/raw/` and `data/raw/agriculture/` READMEs are now substantive; the earlier greenfield-stub statement is superseded."
  - "ADR-0029 is accepted and adopts the exact v2 blob at `docs/doctrine/directory-rules.md`; the legacy v1.3.1 architecture body is restored as a read-only compatibility dependency pending a separate tombstone migration."
  - "Directory Rules v2 `DIR-SOURCE-001` requires source-first capture identity, so the final canonical payload home for USDA NASS requires migration review; this README does not move data or reinterpret the existing compatibility lane."
  - "QuickStats, Crop Progress, and CDL remain separate product surfaces; no source role, cadence, geometry, parser, or receipt lineage is inherited across products."
  - "Current USDA endpoints, terms, rights, source activation, payload inventory, executable validation, release readiness, and public suitability remain UNKNOWN or NEEDS VERIFICATION unless separately evidenced."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# USDA NASS RAW Agriculture Lane

[![Document: draft](https://img.shields.io/badge/document-draft-d29922?style=flat-square)](#authority-and-evidence-snapshot)
[![Lifecycle: RAW](https://img.shields.io/badge/lifecycle-RAW-f97316?style=flat-square)](#repo-fit)
[![QuickStats: aggregate](https://img.shields.io/badge/QuickStats-aggregate-8250df?style=flat-square)](#product-separation)
[![Rights: needs verification](https://img.shields.io/badge/rights-needs%20verification-b54708?style=flat-square)](#authority-and-evidence-snapshot)
[![Publication authority: none](https://img.shields.io/badge/publication%20authority-none-b91c1c?style=flat-square)](#forbidden-shortcuts)

**Purpose:** preserve immutable USDA National Agricultural Statistics Service source captures or immutable references, with enough admission context to replay and audit them without turning RAW bytes into Agriculture truth or publication authority.

> [!CAUTION]
> `data/raw/agriculture/usda-nass/` is an internal RAW source-capture lane. It is not processed truth, catalog truth, proof, receipt authority, source-registry authority, rights or policy authority, crop or field truth, a public API/UI source, or release authority. Public clients and ordinary UI surfaces must never read this lane directly.

## Navigation

- **Boundary:** [Scope](#scope) · [Repo fit](#repo-fit) · [Authority snapshot](#authority-and-evidence-snapshot)
- **Source handling:** [Product separation](#product-separation) · [Capture contract](#capture-contract) · [Accepted material](#accepted-material) · [Exclusions](#exclusions)
- **Lifecycle:** [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Forbidden shortcuts](#forbidden-shortcuts)
- **Assurance:** [Required checks](#required-checks-before-use) · [Correction and rollback](#correction-replay-and-rollback) · [Status notes](#status-notes) · [Related files](#related-files)

---

## Scope

This directory is the Agriculture-domain RAW landing lane for separately admitted USDA NASS product captures. It may preserve source-native payloads, immutable payload references, request or package identity, source-head metadata, capture context, checksums, and minimal RAW-local sidecars.

The lane supports preservation, replay, audit, and later governed processing. It does not:

- activate a source or choose the canonical NASS connector path;
- decide the meaning, reliability, rights, sensitivity, or public suitability of source material;
- normalize, join, aggregate, redact, prove, catalog, release, or publish data;
- allow one NASS product to inherit another product's role, parser, cadence, spatial support, or release posture.

USDA NASS is a provider family, not one homogeneous dataset. QuickStats, Crop Progress, Cropland Data Layer, and any future product require distinct product identity and admission evidence.

---

## Repo fit

| Field | Bounded current state |
|---|---|
| Path | `data/raw/agriculture/usda-nass/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw/` |
| Domain lane | `agriculture` |
| Source family | `usda-nass` |
| Artifact role | Immutable source captures or immutable references plus RAW-local admission context |
| Placement basis | Repository-present Agriculture RAW lane plus confirmed parent contracts; accepted Directory Rules v2 requires source-first capture identity, so final canonical payload placement is **NEEDS VERIFICATION** |
| Compatibility path | `data/raw/usda-nass/` remains documented as compatibility-only pending a separate v2-conformant migration decision |
| Upstream | A governed source-admission process through an accepted connector home; current NASS connector placement is unresolved |
| Normal exit | Governed handoff to `data/work/agriculture/` or `data/quarantine/agriculture/` |
| Direct public access | **DENY** |
| Release authority | `release/`, not this directory |
| Proof / receipt authority | `data/proofs/` and `data/receipts/`, not this directory |
| Registry / policy authority | The accepted source-registry lane and `policy/`, not this directory |

Promotion remains a governed state transition. A copy, move, commit, pull request, merge, workflow result, or directory name cannot promote RAW material.

---

## Authority and evidence snapshot

The table below records repository evidence at `main@2cf6f4322d34adcd441835cb969563b5f64f99b6`. It is a review checkpoint, not a permanent implementation guarantee.

| Surface | Pinned finding | Consequence |
|---|---|---|
| This target | File exists at the same path; prior blob `1c6f863bf59b63b4b916957c2ad609df346e86b8` | Document identity and stable headings are preserved |
| RAW parent contracts | `data/raw/README.md` and `data/raw/agriculture/README.md` are substantive, not greenfield stubs | This lane inherits an explicit immutable-capture and no-public-path boundary |
| Compatibility lane | `data/raw/usda-nass/README.md` points here as the Agriculture source lane | The compatibility path must not become a second writer |
| Adopted Directory Rules | ADR-0029 adopts exact blob `fd49a0b83e55cef52c1124281f093e263526898d` at `docs/doctrine/directory-rules.md` | v2 is effective even though its immutable adopted bytes retain the internal `PROPOSED_FOR_ADOPTION` artifact label |
| Legacy rules path | `docs/architecture/directory-rules.md` is restored to v1.3.1 blob `18653c00ba193a4afaa3e07a0924452807fb98ef` | Read-only compatibility dependency; tombstoning and deletion remain separate held migrations |
| ADR-0029 | Status is `accepted` after explicit project-owner ratification | Establishes v2 and single-write doctrine authority; does not itself migrate this RAW lane |
| RAW source placement | v2 `DIR-SOURCE-001` requires source-first capture identity, while current parent READMEs place this source beneath the Agriculture lane | **CONFLICTED / NEEDS VERIFICATION**; preserve current bytes and stop short of declaring a canonical payload home |
| NASS connector placement | Repository docs describe `connectors/nass/`, `connectors/usda-nass/`, and `connectors/usda/nass/`; no accepted canonical choice was verified | Capture records must preserve the actual producer identity without normalizing the path conflict away |
| Connector implementation | The inspected coordination README reports placeholder source records, pipeline spec, and tests rather than an established executable connector | Source activation and emitted RAW payloads remain unproved |
| Fixtures and tests | NASS fixture READMEs exist, but payload inventory and no-network execution remain unverified; inspected tests are documentation-only | Fixture presence and filenames are not validation proof |
| External USDA facts | No live endpoint, current terms, rights record, cadence, or source response was checked for this revision | Those facts remain **NEEDS VERIFICATION** at admission and release time |

> [!IMPORTANT]
> Repository documentation can establish the intended boundary and expose conflicts. It cannot substitute for a valid SourceDescriptor, activation decision, rights review, policy decision, substantive tests, observed run receipt, EvidenceBundle, release decision, correction path, or rollback target.

---

## Product separation

| Product surface | Current KFM posture | Preserve in RAW | Never infer |
|---|---|---|---|
| QuickStats | `aggregate` | Product/series identity, commodity, statistic, unit, geography or aggregation unit, reporting period, query parameters, suppression/revision flags where present, source/retrieval time, row or file inventory, and digest | Field, farm, operator, parcel, person, or individual observation truth |
| Crop Progress | Aggregate/reporting posture pending a complete descriptor | Commodity, progress or condition measure, geography, reporting period, revision, retrieval time, response inventory, and digest | Direct observation of a specific field or operation |
| Cropland Data Layer (CDL) | Modeled or classified raster posture pending a complete descriptor | Product year, raster identity, class map/version, spatial support, coordinate reference information, source metadata, file inventory, and digest | QuickStats semantics, ground-observed crop truth, or an exact private-land claim |
| Future NASS product | **NEEDS VERIFICATION** | Its own descriptor, activation decision, role, rights, cadence, support, parser, validation, and receipt lineage | Inheritance from an already admitted NASS product |

The provider name does not collapse product identity. A correction or role change requires governed lineage; it must not be performed by silently editing an existing RAW record.

---

## Capture contract

Before material is relied on as an admitted RAW capture, its owning contract or sidecars should make the following review surface inspectable. Exact field names and filenames remain contract-controlled.

| Concern | Minimum inspectable record |
|---|---|
| Stable identity | Source ID, product ID, capture/run ID, and the referenced descriptor revision |
| Admission authority | Source activation or admission decision and its finite outcome |
| Producer identity | The actual connector/importer identity and version or commit when applicable |
| Request or package identity | Sanitized endpoint family and parameters, or package/distribution identity; never credentials |
| Source-native scope | Geography or spatial support, aggregation unit, reporting/source time, product vintage, and units |
| Capture timing | Source time where supplied and retrieval/capture time kept distinct |
| Response inventory | Status, content type, row/file count, size, pagination/chunking, suppression/revision flags, and parse state where applicable |
| Integrity | Payload or package digest plus source-head metadata available at capture time |
| Rights and sensitivity | Rights, attribution, reuse, sensitivity, and public-release review state |
| Disposition | RAW, QUARANTINE, reject/return, or error outcome with a reason |
| Traceability | Run/ingest receipt reference and any quarantine or correction reference |

Unknown or missing fields must remain visible. Do not fill gaps with plausible defaults merely to complete a sidecar.

---

## Accepted material

Accepted content is limited to source-capture material and RAW-local aids:

- immutable source-native payloads or immutable references to controlled payload storage;
- sanitized request/query snapshots and package/distribution identity;
- source-head, manifest, response-inventory, pagination/chunking, and retrieval records;
- checksums, content hashes, byte counts, and product-vintage metadata;
- product-specific spatial, temporal, aggregation, class-map, suppression, and revision context;
- minimal README, inventory, or index sidecars that explain capture state without becoming registry, policy, receipt, proof, catalog, release, or public authority.

Credentials, tokens, cookies, signed URLs, private endpoints, and unsafe logs are never accepted content.

---

## Exclusions

| Do not place here | Owning surface or action |
|---|---|
| USDA/NASS product doctrine | `docs/sources/catalog/usda/` |
| Agriculture source-role and sensitivity doctrine | `docs/domains/agriculture/` |
| Connector implementation or connector-alias decision | `connectors/` plus an accepted placement decision |
| SourceDescriptor or activation-decision authority | The accepted `data/registry/` source lane |
| Rights, attribution, reuse, or sensitivity decisions | `policy/` and governed review records |
| Mutable normalization, joins, repairs, enrichment, or redaction trials | `data/work/agriculture/` |
| Unresolved, unsafe, malformed, restricted, or rights-unclear material | `data/quarantine/agriculture/` |
| Validated processed Agriculture objects | `data/processed/agriculture/` |
| Catalog records or graph/triplet projections | `data/catalog/` and `data/triplets/` |
| Ingest, transform, aggregation, review, or release receipts | `data/receipts/` |
| EvidenceBundle, ProofPack, or proof closure | `data/proofs/` |
| Release manifests, promotion decisions, corrections, withdrawals, or rollback decisions | `release/` |
| Public layers, PMTiles, reports, stories, API payloads, downloads, or generated answers | `data/published/` or governed public interfaces only after release closure |
| Field-, farm-, operator-, parcel-, person-, or land-ownership truth | The owning governed domain lane; never this source-capture lane |
| Contracts, schemas, validators, tests, fixtures, pipeline code, or app/UI code | Their dedicated responsibility roots |

---

## Directory map

The bounded repository search used for this revision confirmed only this README under the exact target prefix:

```text
data/raw/agriculture/usda-nass/
└── README.md
```

That search is not a recursive tree receipt. Payload existence therefore remains **UNKNOWN**.

<details>
<summary>Proposed logical capture grouping</summary>

When an accepted contract and implementation establish a concrete layout, preserve the existing source/run grouping intent without treating these placeholders as current files:

```text
data/raw/agriculture/usda-nass/
└── <source-id>/
    └── <run-id>/
        ├── <immutable payload or immutable reference>
        ├── <capture and source-head metadata>
        ├── <digests and response inventory>
        └── README.md
```

If a RAW-local index is introduced, it must remain non-authoritative and must not become a public index, source registry, catalog, release manifest, graph edge source, search/vector index, map source, or generated-answer retrieval source.

</details>

---

## Exit gates

| Route | Minimum evidence |
|---|---|
| Retain in RAW | Capture is admitted and hash-bound, but no downstream normalization decision has closed |
| Route to QUARANTINE | Rights, role, product identity, producer path, query lineage, support, sensitivity, citation, integrity, schema, or activation state is unresolved |
| Reject or return | Admission decision says the material does not belong in this lane; preserve the decision and any required audit record |
| Advance to WORK | Descriptor/activation, rights, role, product separation, citation, integrity, and minimum validation evidence are sufficient for governed normalization |
| Promote beyond WORK | Later PROCESSING, CATALOG/TRIPLETS, evidence, policy, review, and RELEASE gates close with correction and rollback support |

No route is proven by moving files. The decision, evidence, receipts, and resulting state must remain inspectable.

---

## Forbidden shortcuts

The following direct path is forbidden:

```text
data/raw/agriculture/usda-nass/
  -> data/processed/agriculture/
  -> data/catalog/ or data/triplets/
  -> data/published/
  -> public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

Each arrow requires its own governed transition. A connector, watcher, README, workflow, commit, pull request, merge, or GitHub release cannot authorize publication.

---

## Required checks before use

Use this as a review checklist, not as a substitute for a recorded admission decision:

- [ ] Confirm the provider and exact NASS product identity.
- [ ] Confirm the material belongs in the Agriculture domain and this source lane rather than the compatibility path.
- [ ] Resolve the actual producer/connector identity without claiming that the connector-path conflict is settled.
- [ ] Resolve the SourceDescriptor revision, activation/admission decision, source role, authority, rights, sensitivity, cadence, citation, and integrity posture.
- [ ] Preserve QuickStats, Crop Progress, CDL, and future products as separate capture and receipt lineages.
- [ ] Preserve aggregation unit, geography or spatial support, period/vintage, units, suppression/revision flags, and source/retrieval times where applicable.
- [ ] Confirm QuickStats and Crop Progress aggregates are not joined to field, farm, parcel, operator, person, or private-yield truth.
- [ ] Confirm CDL remains classified/model-derived and is not represented as ground observation or QuickStats.
- [ ] Confirm payloads or references are immutable and hash-bound; never overwrite a prior run in place.
- [ ] Confirm credentials and sensitive values are absent from payload references, URLs, logs, metadata, examples, and receipts.
- [ ] Route unresolved rights, role, sensitivity, source-head, class-map, spatial-reference, or integrity questions to QUARANTINE or reject/return.
- [ ] Confirm substantive no-network tests and validators actually ran before claiming validation.
- [ ] Confirm no public layer, API payload, map, report, graph, index, or generated answer reads RAW material directly.
- [ ] Confirm downstream correction and rollback targets before promotion.

---

## Correction, replay, and rollback

### Source and capture correction

- Preserve the original capture and digest.
- Record a new descriptor, run, or correction object when role, source metadata, rights, product revision, or payload changes.
- Never relabel `aggregate`, modeled/classified, or another role by editing RAW history in place.
- Preserve the relationship between the superseded capture, replacement capture, reason, reviewer state, and affected downstream consumers.

### Replay

- Replay from an immutable payload or immutable reference and a sanitized, deterministic request/package identity where the source permits it.
- Keep volatile retrieval time distinct from source/reporting time.
- Compare digests, source-head metadata, response inventory, product revision, and parser/version identity.
- Route non-equivalent, stale, unavailable, or rights-changed results through review rather than silently replacing the prior run.

### Rollback

- **Before merge of this README:** leave or close the draft pull request; the default branch remains unchanged.
- **After merge of this README:** transparently revert the documentation commit if the boundary, links, or evidence snapshot is wrong.
- **For data or release state:** select a verified prior capture/release target through the owning lifecycle and release process. Do not delete RAW history or rewrite shared Git history as rollback.

---

## Status notes

| Claim | Current status |
|---|---|
| This README exists at the requested Agriculture RAW source-lane path | **CONFIRMED** at the pinned base |
| The same `doc_id`, path, created date, lifecycle phase, and source-family identity are preserved | **CONFIRMED** in this revision |
| Parent RAW and Agriculture READMEs are substantive rather than greenfield stubs | **CONFIRMED** at the pinned base |
| `data/raw/usda-nass/` is documented as a compatibility pointer to this lane | **CONFIRMED** at the pinned base |
| QuickStats is aggregate and field-level inference fails closed in current KFM source documentation | **CONFIRMED documentation posture** |
| Crop Progress and CDL require product-specific descriptors and must not inherit QuickStats semantics | **CONFIRMED documentation posture** |
| ADR-0029 accepts exact Directory Rules v2 bytes at the doctrine path | **CONFIRMED / ACCEPTED** |
| The legacy v1.3.1 architecture rules body is restored as a read-only compatibility dependency | **CONFIRMED** at the pinned base |
| This target's domain-first payload placement is fully reconciled with v2 `DIR-SOURCE-001` source-first identity | **CONFLICTED / NEEDS VERIFICATION** |
| A canonical executable NASS connector home and active source admission are established | **NEEDS VERIFICATION** |
| Non-README payloads exist beneath this exact target | **UNKNOWN** after bounded search |
| Current USDA endpoints, terms, rights, cadence, or response behavior were verified for this revision | **NOT RUN / NEEDS VERIFICATION** |
| NASS fixtures contain payloads and no-network tests execute substantively | **NEEDS VERIFICATION** |
| Current documentation workflows prove links, citation closure, accessibility, or rendering | **DENY** — inspected workflows are readiness holds or non-enforcing scaffolds |
| This README proves evidence closure, review, release, publication, or public safety | **DENY** |

---

## Related files

### Lifecycle and compatibility

- [`../README.md`](../README.md) — Agriculture RAW parent lane
- [`../../README.md`](../../README.md) — RAW root contract
- [`../../../README.md`](../../../README.md) — governed `data/` root
- [`../../usda-nass/README.md`](../../usda-nass/README.md) — compatibility pointer
- [`../../../quarantine/agriculture/README.md`](../../../quarantine/agriculture/README.md)
- [`../../../processed/agriculture/README.md`](../../../processed/agriculture/README.md)
- [`../../../catalog/domain/agriculture/README.md`](../../../catalog/domain/agriculture/README.md)
- [`../../../published/layers/agriculture/README.md`](../../../published/layers/agriculture/README.md)
- [`../../../registry/sources/README.md`](../../../registry/sources/README.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)

### Source, domain, connector, and fixture context

- [`../../../../docs/domains/agriculture/SOURCE_REGISTRY.md`](../../../../docs/domains/agriculture/SOURCE_REGISTRY.md)
- [`../../../../docs/domains/agriculture/SOURCES.md`](../../../../docs/domains/agriculture/SOURCES.md)
- [`../../../../docs/domains/agriculture/SENSITIVITY.md`](../../../../docs/domains/agriculture/SENSITIVITY.md)
- [`../../../../docs/sources/catalog/usda/usda-nass-quickstats.md`](../../../../docs/sources/catalog/usda/usda-nass-quickstats.md)
- [`../../../../docs/sources/catalog/usda/usda-nass-cdl.md`](../../../../docs/sources/catalog/usda/usda-nass-cdl.md)
- [`../../../../connectors/nass/README.md`](../../../../connectors/nass/README.md)
- [`../../../../connectors/usda-nass/README.md`](../../../../connectors/usda-nass/README.md)
- [`../../../../fixtures/domains/agriculture/nass_quickstats/README.md`](../../../../fixtures/domains/agriculture/nass_quickstats/README.md)
- [`../../../../fixtures/domains/agriculture/no_network/nass/README.md`](../../../../fixtures/domains/agriculture/no_network/nass/README.md)

### Placement authority and migration state

- [`../../../../docs/doctrine/directory-rules.md`](../../../../docs/doctrine/directory-rules.md) — exact v2 bytes adopted by ADR-0029
- [`../../../../docs/architecture/directory-rules.md`](../../../../docs/architecture/directory-rules.md) — restored v1.3.1 read-only compatibility body pending a separate tombstone migration
- [`../../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md`](../../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) — accepted adoption and controlled-migration decision

---

**KFM boundary:** this directory preserves USDA NASS RAW source material and admission context only. It does not own source doctrine, source activation, product meaning, rights, sensitivity, policy, proof, receipts, catalogs, releases, crop or field truth, public artifacts, UI/API behavior, or generated-answer truth.

[Back to top](#top)
