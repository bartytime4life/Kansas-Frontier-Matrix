<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-intake-exploratory-spatiotemporal-modernization-blueprint-source-map
title: Spatiotemporal modernization blueprint - governed source map
type: exploratory-intake
version: v1.0
status: draft; triaged; noncanonical
owners: OWNER_TBD
created: 2026-07-30
updated: 2026-07-30
policy_label: public
related: [docs/intake/NEW_IDEAS_INDEX.md, docs/intake/new-ideas-register.md, docs/standards/GEOPARQUET.md, docs/standards/STAC.md, data/catalog/stac/README.md, docs/architecture/deployment-topology.md, packages/maplibre/src/README.md, data/maps/README.md]
tags: [kfm, intake, exploratory, geoparquet, stac, pmtiles, maplibre, lifecycle, evidence, performance]
notes: [Source text captured from Pasted text(32).txt; source date and authorship remain NEEDS VERIFICATION; complete 226-line attachment reviewed; source identity is SHA-256 pinned; repository main at 0e4e2ee717730a4b4bfa22cf59c13241eba14bef and cited primary specifications were inspected on 2026-07-30; this file grants no implementation, promotion, source-activation, release, deployment, or publication authority.]
[/KFM_META_BLOCK_V2] -->

# Spatiotemporal modernization blueprint - governed source map

This intake record preserves the useful design pressure in the attached *Architectural Modernization and Governance Blueprint for the Kansas Frontier Matrix* while separating corroboration, current repository drift, upstream-specification uncertainty, benchmark proposals, and unsafe direct transfers.

> [!IMPORTANT]
> **Authority:** `EXPLORATORY / INTAKE ONLY`
> **Disposition:** `TRIAGED`
> **Promotion:** none
> **Implementation:** none
> **Release posture:** no source activation, proof construction, promotion, release, deployment, or publication

The attachment is not doctrine, a standards profile, an accepted ADR, implementation proof, or a performance result. Its imperative language is normalized below into evidence-bounded candidates.

## Source identity and review method

### Confirmed attachment facts

| Field | Value |
|---|---|
| Captured filename | `Pasted text(32).txt` |
| Captured title | `Architectural Modernization and Governance Blueprint for the Kansas Frontier Matrix` |
| SHA-256 | `798d8ee3ab1d99ce92cb04d5e2e69a66c5c89407d1868da350be153c3b9f04a4` |
| Size | 22,806 bytes |
| Line count | 226 |
| Source date | `NEEDS VERIFICATION` |
| Capture and triage date | 2026-07-30 |
| Source class | `EXPLORATORY / EXTERNAL SYNTHESIS` |
| Redistribution | The attachment is not committed or redistributed by this intake packet. |

### Review method and limits

- The complete text attachment was reviewed, including its architecture narrative, comparison tables, lifecycle model, source-role notes, modernization matrix, roadmap, and cited-source list.
- Current KFM repository homes were checked at `main@0e4e2ee717730a4b4bfa22cf59c13241eba14bef` before classifying a proposal as a gap.
- Time-sensitive technical claims were checked against primary GeoParquet, STAC GeoParquet, PMTiles, Cloudflare Pages, and MapLibre documentation on 2026-07-30.
- Corrupted extraction span markers were treated as transcription artifacts, not content.
- The attachment's cited-source list is lineage only. This intake record cites the primary sources actually inspected during triage.
- No benchmark was executed. Throughput, feature-count, frame-rate, compression, cost, and latency statements remain `UNVERIFIED` unless current repository evidence is named.

## Directory Rules and authority basis

This source map follows the repository's existing intake boundary:

- [`docs/intake/NEW_IDEAS_INDEX.md`](../NEW_IDEAS_INDEX.md) records the packet without promoting it.
- [`docs/intake/new-ideas-register.md`](../new-ideas-register.md) records its status, destination pressure, blockers, and smallest next action.
- [`docs/standards/GEOPARQUET.md`](../../standards/GEOPARQUET.md) remains the KFM standards authority for GeoParquet posture.
- [`docs/standards/STAC.md`](../../standards/STAC.md) and [`data/catalog/stac/README.md`](../../../data/catalog/stac/README.md) remain the STAC profile and catalog-lane authorities.
- [`docs/architecture/deployment-topology.md`](../../architecture/deployment-topology.md), [`packages/maplibre/src/README.md`](../../../packages/maplibre/src/README.md), and [`data/maps/README.md`](../../../data/maps/README.md) retain deployment, renderer, and map-data boundaries.
- Structural promotion requires the appropriate ADR, contract, schema, policy, fixture, validator, review, and rollback evidence. Copying proposal prose into a canonical file is not promotion.

## Primary-source and repository drift check

| Attachment claim or pressure | Current evidence | Triage result |
|---|---|---|
| GeoParquet 2.0 should be KFM's mandatory target | The [stable GeoParquet site](https://geoparquet.org/) still points readers to release 1.1.0. The upstream repository's [`main` specification](https://github.com/opengeospatial/geoparquet/blob/main/format-specs/geoparquet.md) describes 2.0.0, but the repository labels its `main` specifications development versions. KFM's current standard explicitly tracks stable 1.1.0 and treats 2.0 as not adopted. | `CONFLICTED / DECISION REQUIRED`; do not silently change the KFM profile. |
| Native geometry means geometry is no longer WKB | The 2.0 development specification uses Parquet `GEOMETRY` or `GEOGRAPHY` logical types annotating a `BYTE_ARRAY` whose feature encoding is WKB. | `CORRECT BEFORE USE`; distinguish logical type from byte encoding. |
| Hilbert order, 50,000-100,000 rows, ZSTD, and H3/S2 partitioning are mandatory | Upstream [distribution guidance](https://github.com/opengeospatial/geoparquet/blob/main/format-specs/distributing-geoparquet.md) recommends ZSTD, spatial ordering, and a starting row-group range, but says there is no single best size, byte size and access pattern matter, and several partition methods can work. Its current quick-start range is not the attachment's strict range. | `BENCHMARK REQUIRED`; no universal KFM mandate from this packet. |
| GeoParquet 2.0 requires a top-level bbox column for pruning | Upstream guidance says 2.0 native geometry statistics provide row-group bounding boxes; a separate bbox covering remains a 1.1 option and can provide different page-level behavior. | `REJECTED AS WRITTEN`; version-specific validation is required. |
| STAC GeoParquet is a stable replacement for STAC JSON/API behavior | The [STAC GeoParquet project](https://github.com/radiantearth/stac-geoparquet-spec) says its specification is under development and has not reached stable v1. Its [current mapping specification](https://github.com/radiantearth/stac-geoparquet-spec/blob/main/stac-geoparquet-spec.md) defines a bulk representation of STAC Items and carries independent metadata/version rules. | `DEFERRED / PROFILE REQUIRED`; useful bulk mirror, not a replacement for KFM catalog closure. |
| Promotion is a file move through five mandatory directories | KFM already defines governed lifecycle transitions and receipts, including RAW to WORK or QUARANTINE before PROCESSED. The attachment's simplified linear path cannot replace current lifecycle law. | `DUPLICATE-CORROBORATIVE`; preserve current finite outcomes and optional branches. |
| A browser service worker should fetch and cache the complete PMTiles archive to emulate ranges | [PMTiles guidance](https://docs.protomaps.com/pmtiles/cloud-storage) is range-first and recommends compatible object storage such as R2. [Cloudflare Pages documentation](https://developers.cloudflare.com/pages/configuration/serving-pages/) currently reports `200`, not spec-compliant `206`, for range requests. Full-archive caching remains constrained by size, device storage, correction freshness, sensitivity, and failure behavior. | `HOSTING DECISION REQUIRED`; a service-worker fallback is not the default architecture. |
| MapLibre guarantees approximately 50,000 interactive entities at stable 60 FPS | KFM's deployment topology marks public-surface performance budgets `NEEDS VERIFICATION`. MapLibre provides a [large-data optimization guide](https://maplibre.org/maplibre-gl-js/docs/guides/large-data/), not a device-independent KFM guarantee. | `UNVERIFIED BENCHMARK CLAIM`; replace with device-class budgets and measured fixtures. |
| SURGICAL, STANDARD, and SHOWCASE modernization levels should be introduced | The repository root README already owns these levels and constrains their use by document role and risk. | `DUPLICATE-CORROBORATIVE`; do not create a second modernization authority. |

## Repository-grounded candidate map

| Candidate | Attachment pressure | Current KFM boundary | Disposition | Required next evidence |
|---|---|---|---|---|
| GeoParquet 2.0 readiness decision | Native Parquet geometry/geography types and statistics | [`docs/standards/GEOPARQUET.md`](../../standards/GEOPARQUET.md) keeps stable 1.1.0 and requires an ADR for 2.0 | `DECISION CANDIDATE` | Stable-channel status; writer/reader/validator compatibility matrix; dual-read window; migration receipt; correction and rollback. |
| Dataset-specific GeoParquet optimization profile | Spatial ordering, compression, row groups, and partitioning | KFM has profile requirements but no repository evidence that one fixed layout fits every data family | `BENCHMARK CANDIDATE` | Representative synthetic fixtures; query suite; row and byte-size observations; writer/version pin; cold/warm reads; deterministic result receipt. |
| STAC GeoParquet collection mirror | Bulk query and transfer of STAC Items | STAC, DCAT, PROV, EvidenceBundle, SourceDescriptor, receipt, release, and CatalogMatrix responsibilities remain separate | `DEFERRED / PROFILE CANDIDATE` | Pin under-development spec revision; define record and collection mapping; validate nested assets/links; preserve catalog closure and correction semantics. |
| Receipt-backed lifecycle transitions | Immutable stage transitions and rollback evidence | Existing lifecycle, promotion, receipt, proof, review, and release families already own this behavior | `DUPLICATE-CORROBORATIVE` | Identify a concrete missing transition or validator before proposing a new object family. |
| Range-first PMTiles hosting profile | Static edge delivery without a tile server | Public clients consume released artifacts only; hosting, cache, sensitivity, correction, and rollback remain governed | `DEPLOYMENT CANDIDATE` | Hosting target; verified `206`, CORS, ETag, size, cost, withdrawal, and offline-expiry behavior; no public unreleased asset. |
| Full-archive service-worker fallback | Local synthetic `206` responses over a cached PMTiles blob | Cache storage is not a trust boundary and cannot silently outlive corrections or withdrawals | `EXPERIMENT ONLY` | Explicit size ceiling; quota and eviction tests; digest-before-render; expiry and correction handling; denial path; browser matrix. |
| Renderer performance envelope | 16.67 ms frame budget and dense entity overlays | MapLibre is the renderer boundary; device-specific budgets remain unknown | `BENCHMARK CANDIDATE` | Named device/browser/GPU classes; dataset and style complexity; interaction cases; p50/p95 frame time; memory; load/idle; degradation and fallback. |
| Static tile and dynamic-entity separation | PMTiles basemap plus higher-frequency overlay | Compatible with renderer-adapter and governed-input boundaries | `CORROBORATIVE / CONSUMER BOUND` | Confirm a current consumer, update cadence, evidence drawer behavior, sensitive-feature policy, and backpressure/fallback semantics. |
| EvidenceBundle inspectable-claim protocol | Cite-or-abstain, temporal validity, uncertainty, and reversibility | Core KFM doctrine and contracts already own evidence and finite response outcomes | `DUPLICATE-CORROBORATIVE` | Extend only through a named contract gap with paired schema, fixtures, validator, tests, and anti-collapse rules. |
| Source-role corrections and multi-domain integration | SSURGO, CDL, PLANTS, SCAN, USCRN, SMAP, 3DHP, and planning-source distinctions | Source authority, rights, access, source role, temporal support, and domain meaning are source-specific | `REPO VERIFY / SOURCE SPECIFIC` | Verify each official source independently; do not promote the attachment's summary table as a source descriptor. |
| Documentation and CI modernization | Tiered Markdown modernization, links, crosswalks, accessibility, generated-asset headers | Modernization intensity exists; validation homes and enforcement depth vary | `PARTIAL / DECOMPOSE` | Name one current validator gap, exact paths, finite outcomes, false-positive posture, generated-file handling, and rollback. |

### Highest-confidence conclusions

1. The attachment usefully identifies a pending **GeoParquet 2.0 readiness decision**, but it does not justify adopting 2.0 or rewriting current standards in this intake change.
2. Spatial ordering, compression, row grouping, and partitioning should be a **versioned, dataset-specific optimization profile backed by benchmarks**, not one global row-count or grid-resolution constant.
3. STAC GeoParquet can be evaluated as a **bulk collection mirror** only after its under-development specification revision and KFM STAC/DCAT/PROV/EvidenceBundle closure are explicit.
4. PMTiles delivery should remain **range-first**. A whole-file browser-cache interceptor is a bounded fallback experiment with strict size, trust-freshness, correction, and denial semantics.
5. The attachment's 50,000-feature and 60-FPS numbers are not KFM acceptance evidence. Performance claims require named hardware, browser, style, data shape, interaction, and percentile budgets.
6. Lifecycle, EvidenceBundle, cite-or-abstain, source-role separation, public-client membrane, and modernization-intensity themes mostly corroborate existing KFM responsibilities and should not be duplicated.

## Conflicts and unsafe direct transfers

| Packet pattern | Why direct transfer is unsafe | Required correction |
|---|---|---|
| “Mandatory GeoParquet 2.0” | Conflicts with KFM's current stable 1.1.0 profile and upstream stable-channel ambiguity. | Use an accepted version-readiness decision with a compatibility and rollback plan. |
| “Native geometry” presented as non-WKB | Collapses Parquet logical type and geometry byte encoding. | Record both logical type and encoding; validate the exact upstream version. |
| Fixed 50,000-100,000 row groups | Row width, query pattern, frontend versus analytics use, and target byte size change the optimum. | Benchmark row and byte limits per dataset/profile. |
| Hilbert-only ordering or H3 resolution 3 everywhere | Ordering and partition strategy are workload-specific; H3/S2 identifiers also create version and crosswalk obligations. | Compare allowed strategies and record the chosen algorithm, version, parameters, and benchmark evidence. |
| Top-level bbox-column mandate for GeoParquet 2.0 | Confuses 1.1 covering columns, file-level bbox metadata, and 2.0 native row-group statistics. | Version the validation rule and preserve compatibility behavior explicitly. |
| STAC GeoParquet as catalog authority | A bulk serialization does not prove source, evidence, policy, rights, review, release, correction, or STAC/DCAT/PROV agreement. | Treat it as a mirror asset subordinate to catalog closure. |
| Full PMTiles download on first page load | Can exceed quota, delay useful rendering, expose complete public bytes, and retain corrected or withdrawn data. | Prefer verified byte ranges; gate any offline cache by size, sensitivity, digest, expiry, and correction behavior. |
| Cloudflare R2 or Workers as a mandate | Hosting is an infrastructure, cost, security, and rollback decision; a vendor example is not KFM doctrine. | Compare targets against an accepted hosting profile and exit strategy. |
| Planetiler or Tilemaker as automatic dependencies | Dependency, license, reproducibility, input support, schema mapping, and generated-output identity are not resolved. | Admit one tool through dependency governance and synthetic deterministic output tests. |
| Universal 60 FPS or 50,000-entity guarantee | Device, browser, GPU, geometry, style, interaction, and update cadence determine behavior. | Record measured budgets by device class and percentile. |
| Dynamic entities bypassing JavaScript objects | Describes one rendering implementation without a verified consumer or current adapter contract. | Keep renderer behavior behind the accepted adapter and benchmark boundary. |
| Simplified five-stage linear lifecycle | Omits KFM's WORK/QUARANTINE branching and can collapse validation, evidence, policy, review, proof, release, and publication. | Extend current lifecycle objects and finite outcomes; do not replace them with folder movement. |
| Source tables treated as current source authority | Program ownership, endpoint, cadence, rights, access, identifiers, and product semantics can change. | Verify primary source pages and create or update source-specific descriptors under separate authority. |
| Successful hash, signature, schema, render, or benchmark result | Each proves only its named check. | Keep integrity, evidence, policy, review, release, publication, correction, and rollback independent. |

## Dependency-ordered continuation

### Wave 1 - decisions and profiles

1. **GeoParquet version readiness**
   - Decide whether KFM stays on stable 1.1.0, opens a dual-track 1.1/2.0 evaluation, or later adopts a stable 2.x release.
   - Pin the exact upstream specification/schema revision used for evaluation.
   - Inventory actual KFM writers, readers, validators, query engines, and published consumers.
   - Define unsupported-version, mixed-version, downgrade, correction, and rollback outcomes.
2. **Optimization-profile semantics**
   - Define the evidence that selects compression, level, ordering algorithm, row/byte group target, partition strategy, and file-size target.
   - Separate required conformance from benchmark-derived recommendations.
   - Bind benchmark inputs, queries, environment, tool versions, results, and digest in a reviewable receipt.
3. **STAC GeoParquet mirror profile**
   - Pin a STAC GeoParquet specification revision and mapping rules.
   - Define item identity, collection membership, links, assets, extensions, datetimes, bbox, geometry, extra fields, missing fields, and collision behavior.
   - Preserve STAC/DCAT/PROV agreement and KFM evidence, policy, release, correction, and rollback references.
4. **PMTiles hosting and cache decision**
   - Verify range, CORS, ETag, immutable identity, maximum artifact size, access policy, cost envelope, correction, withdrawal, offline expiry, and vendor exit.
   - Decide whether a service-worker fallback has any admitted device and artifact class.
5. **Renderer performance contract**
   - Define device/browser/GPU classes, representative released fixtures, interaction scripts, frame-time/load/memory budgets, and finite degraded or denied outcomes.

### Wave 2 - bounded offline evaluation

- Build public-safe synthetic GeoParquet 1.1 fixtures and, only if Wave 1 authorizes it, 2.0 evaluation fixtures.
- Run pinned cross-reader validation and benchmark queries without network access.
- Compare spatial ordering, row/byte group sizes, compression, and partition candidates without declaring one universal winner.
- Build synthetic STAC GeoParquet valid and invalid fixtures only after the mapping profile is frozen.
- Test PMTiles range and optional-cache behavior against local fixtures, including quota, eviction, stale, corrected, withdrawn, digest-mismatch, and unsupported-range outcomes.
- Run MapLibre performance tests against named device classes and representative released-fixture shapes; do not use test results as release authority.

### Wave 3 - integration and public behavior

- Integrate only a profile that has accepted contracts, schemas, fixtures, validators, dependency pins, receipts, policy, review, correction, and rollback.
- Keep STAC GeoParquet a governed mirror asset unless a later accepted decision changes its role.
- Keep public MapLibre clients on released artifacts and governed APIs.
- Activate hosting, caching, or live data behavior only through separate source, infrastructure, release, deployment, and publication authority.

### Recommended next bounded action

Prepare a **decision-only GeoParquet version-readiness issue** grounded in current `docs/standards/GEOPARQUET.md` and primary upstream specifications. It should:

- distinguish the stable 1.1.0 channel from the 2.0 development specification;
- inventory repository writers, readers, validators, query engines, workflows, fixtures, and published consumers;
- define `KEEP_1_1`, `DUAL_EVALUATE`, `ADOPT_LATER`, and `DENY_UNSUPPORTED` outcomes;
- replace fixed layout mandates with a benchmark-profile decision;
- define dual-read, migration, downgrade, correction, and rollback requirements; and
- authorize no data rewrite, source activation, release, deployment, or publication.

That decision can later authorize one dependency-closed implementation PR. This intake packet does not.

## Out of scope

- Changing [`docs/standards/GEOPARQUET.md`](../../standards/GEOPARQUET.md) or the KFM adopted version.
- Adding GeoParquet, STAC GeoParquet, Hilbert, H3, S2, DuckDB, Sedona, Planetiler, Tilemaker, PMTiles, MapLibre, Cloudflare, or other dependencies.
- Creating or rewriting schemas, contracts, policies, validators, fixtures, workflows, data, catalogs, receipts, proofs, release artifacts, or runtime code.
- Converting, partitioning, indexing, tiling, caching, serving, or publishing any dataset.
- Selecting Cloudflare, R2, S3, a CDN, a service worker, a device budget, or a public hosting topology.
- Verifying or activating SSURGO, CDL, PLANTS, SCAN, USCRN, SMAP, 3DHP, Mesonet, or planning sources.
- Treating the attachment's roadmap phases, performance numbers, tool choices, or cited-source list as accepted KFM decisions.

## Validation and review boundary

This intake packet is complete only if:

- the attachment identity, digest, byte count, and line count match the reviewed source;
- the source date and authorship remain explicitly unresolved;
- every repository link resolves from this file;
- every current external fact cites the primary source inspected on 2026-07-30;
- adopted behavior is distinguished from corroboration, conflict, proposal, benchmark need, and unknown implementation depth;
- index and register entries point back to this source map;
- no canonical standard, dependency, source, runtime, release, deployment, or publication state changes; and
- the pull request remains one bounded documentation-only review surface.

## Rollback and correction

Before merge, rollback is closing the draft pull request and abandoning its branch. After a separately authorized merge, use a focused reviewed revert of the three intake paths.

If a source fact, upstream specification, repository path, or implementation claim changes:

1. preserve this source map as dated intake lineage;
2. append or link a correction instead of silently converting exploratory prose into canon;
3. update the index and register disposition;
4. route any promoted decision through the owning ADR, standard, contract, schema, policy, test, release, correction, and rollback surfaces; and
5. never rewrite existing data, published artifacts, or shared history merely because this exploratory source changes.
