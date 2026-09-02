# Kansas Frontier Matrix — Whole-System Build Reference

**Document type:** Markdown master build reference / implementation guide  
**Prepared for:** KFM maintainers, domain-lane leads, source stewards, reviewers, data engineers, UI/API engineers, AI-runtime engineers, security reviewers, and release stewards  
**Prepared:** 2026-05-20  
**Truth posture:** CONFIRMED doctrine and source synthesis; PROPOSED implementation architecture; UNKNOWN live repository/runtime state unless a mounted checkout, CI result, release artifact, dashboard, or log proves it.  
**Primary use:** Build the entire KFM system as a governed, evidence-first, map-first, time-aware spatial knowledge and publication system.

---

## 0. Executive determination

KFM should be built as a **governed spatial evidence and publication system**, not as a map app, not as a generic data warehouse, not as an AI chat product, and not as a pile of domain datasets.

The durable public unit of value is the **inspectable claim**: a statement or map-supported assertion whose evidence, source role, spatial scope, temporal scope, rights posture, sensitivity posture, review state, release state, correction lineage, and rollback target can be inspected.

The practical build target is a system where:

1. Sources are admitted through governed intake.
2. Evidence is normalized into auditable bundles.
3. Domain records and claims remain time-aware and source-role-aware.
4. Policy, rights, sensitivity, and review gates run before public exposure.
5. Publication is a state transition backed by receipts, proofs, manifests, signatures, and rollback.
6. Public clients use governed APIs, released artifacts, catalog records, tile services, and EvidenceBundle resolution.
7. MapLibre, tiles, PMTiles, COGs, GeoParquet, graphs, summaries, dashboards, scenes, and AI answers are downstream carriers, not sovereign truth.
8. AI is interpretive only and always subordinate to evidence, policy, review, and release state.

**Immediate build recommendation:** start with a small proof-bearing slice, not broad implementation. The safest first slice remains **public-safe hydrology or ecology/landcover**, because it can exercise source descriptors, geometry, time, catalog closure, MapLibre rendering, Evidence Drawer, finite AI outcomes, validation, release, and rollback without living-person, DNA, archaeology, rare-species exact-location, or critical-infrastructure exposure.

---

## 1. Evidence basis and source posture

### 1.1 Source classes used

| Source class | Status in this reference | How to use it |
|---|---:|---|
| KFM doctrine and build plans | CONFIRMED as doctrine | Treat as governing intent unless live repo evidence or later accepted ADR supersedes it. |
| Directory Rules | CONFIRMED placement doctrine | Controls proposed file homes and responsibility roots. |
| KFM domain-lane reports | CONFIRMED lineage / PROPOSED design | Use for domain object families, risks, validators, fixtures, and policies; not proof of current implementation. |
| KFM implementation reference | LINEAGE / NEEDS VERIFICATION | Reports prior public repo observations; re-scan the live repo before treating as current. |
| New Ideas packets and Pass atlases | EXPLORATORY / PROPOSED backlog | Convert into SourceIntakeRecords, ADRs, fixtures, or validators before implementation. |
| GIS/software/security references | REFERENCE | Use for craft and patterns; they do not override KFM doctrine. |
| Official external standards/docs | NEEDS VERIFICATION before pinning | Use as current technical anchors; recheck before version locks, API calls, or release claims. |

### 1.2 Key attached source ledger

| ID | Source | Use in this reference | Status |
|---|---|---|---|
| SRC-DIR | `Directory Rules.pdf` | Responsibility-root file placement, schema-home convention, lifecycle roots, no parallel authority. | CONFIRMED doctrine |
| SRC-GREEN | `Kansas_Frontier_Matrix_Definitive_Greenfield_Building_Plan_v1_1.pdf` | Greenfield build principles, inspectable claim, pre-RAW events, PromotionReceipt, RunReceipt, Merkle manifest, STAC profile. | CONFIRMED doctrine / PROPOSED-to-create |
| SRC-PIPE | `Kansas_Frontier_Matrix_Pipeline_Living_Implementation_Manual_v0.3.pdf` | Canonical lifecycle, query-save-validate-compile-review-promote-recompile loop, control-plane object families. | CONFIRMED doctrine / PROPOSED implementation |
| SRC-MAP | `KFM_MapLibre_Operating_Architecture_Governed_UI_AI_Interaction_Manual_REVISED.pdf` | MapLibre renderer boundary, governed shell, Evidence Drawer, Focus Mode, map manifest object family. | CONFIRMED doctrine / PROPOSED implementation |
| SRC-GAI | `KFM_Governed_AI_Extended_Pro_Source_Ledger_PDF_Only_Architecture_Report_2026-04-20.pdf` | Provider-neutral AI adapter, MockAdapter first, citation validation, finite outcomes, AIReceipt. | CONFIRMED design scan / PROPOSED implementation |
| SRC-ENCYC | `kfm_encyclopedia.pdf` | Domain and capability atlas, operating law, sensitivity posture, domain coverage. | CONFIRMED planning manuscript / PROPOSED implementation |
| SRC-IMPLREF | `# Kansas Frontier Matrix Implementation Reference.pdf` | Prior public repo observation, schema-home ambiguity, hydrology/ecology maturity signal. | LINEAGE / NEEDS VERIFICATION |
| SRC-P20 | `KFM_Pass_20_Part_2_Idea_Index_Category_Atlas_and_Expansion_Dossier.md` | Pass 20 category systems, expansion agenda, PMTiles/source-drift/CDL watchers. | CONFIRMED source synthesis / PROPOSED backlog |
| SRC-P18 | `KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf` | 14-category idea atlas, source admission, temporal modeling, evidence/proof, API, map, UI, planning themes. | CONFIRMED synthesis / PROPOSED ideas |
| SRC-POSTGIS | `mastering-postgis-modern-ways-to-create-analyze-and-implement-spatial-data.pdf` | Spatial database mechanics: PostGIS import/export, spatial SQL, validation, topology, routing, web GIS. | REFERENCE; examples are version-sensitive |
| SRC-SDL | `The Security Development Lifecycle.pdf` | Secure development lifecycle, security training, threat modeling, bug bar, secure coding/testing, final review, response. | REFERENCE; modernize with current NIST/OWASP |
| SRC-SE | `Handbook-of-Software-Engineering-Methods-1774561674.pdf` | Requirements, project management, Agile, team communication, RACI, prototyping, inclusivity, refactoring. | REFERENCE |
| SRC-DDD | `Domain-Driven Design Reference.pdf` | Bounded contexts, ubiquitous language, aggregates, repositories, context maps, published language. | REFERENCE |
| SRC-TEMPORAL | `developing-time-oriented-database-applications-in-sql.pdf` | Valid time, transaction time, bitemporal records, temporal keys, tracking logs. | REFERENCE |
| SRC-API | `Designing Great Web APIs.pdf` | API-as-contract, resource ontology, lifecycle, documentation/prototyping. | REFERENCE |

### 1.3 External standards anchors checked for this reference

These are not KFM implementation proof. They are current technical anchors to recheck before version pins, release decisions, or source activation.

| Area | External anchor | Build relevance |
|---|---|---|
| Secure software | NIST SP 800-218 SSDF and current SP 800-218 revision work | Secure software practices, CI gates, vulnerability response, attestable development. |
| AI risk | NIST AI RMF 1.0 and NIST generative-AI SSDF profile | Govern/Map/Measure/Manage posture for AI adapters and Focus Mode. |
| Web/API security | OWASP API Security Top 10 and ASVS | API abuse cases, verification requirements, access control, authentication, authorization, input validation. |
| Spatial database | PostGIS official docs | PostgreSQL/PostGIS as canonical spatial SQL layer. |
| Map rendering | MapLibre GL JS and MapLibre Style Spec | 2D map shell and manifest-bound styles. |
| Static tile artifacts | PMTiles documentation | Immutable public-safe tile bundles and range-request hosting. |
| Raster artifacts | OGC Cloud Optimized GeoTIFF | Cloud-friendly large raster delivery. |
| Vector/tabular artifacts | GeoParquet 1.1 | Spatial columnar interchange and processed/published vector artifacts. |
| Catalog | OGC STAC, W3C DCAT v3, W3C PROV-O | Catalog closure, discovery, provenance, release mapping. |

---

## 2. Truth labels and finite outcomes

### 2.1 Truth labels

| Label | Meaning |
|---|---|
| CONFIRMED | Verified from attached doctrine, current-session file evidence, generated artifacts, current repo scan, tests, logs, dashboards, or authoritative external source. |
| PROPOSED | A design, path, schema, contract, workflow, validator, test, file, or recommendation not yet verified as implemented. |
| UNKNOWN | Not verified strongly enough to act as fact. |
| NEEDS VERIFICATION | Checkable before implementation, source activation, public release, package pinning, or operational use. |
| DENY | System/policy outcome: do not expose, publish, execute, or admit. |
| ABSTAIN | Evidence-bounded outcome: do not answer or claim because support is missing/stale/conflicted/out of scope. |
| ERROR | Operational failure requiring remediation; never fallback to unsafe allow. |

### 2.2 Runtime outcomes

KFM runtime surfaces should converge on four finite outcomes:

| Outcome | Meaning | Examples |
|---|---|---|
| ANSWER | Evidence exists, is released, policy-safe, citation-valid, and in scope. | Focus Mode returns a bounded, cited explanation. |
| ABSTAIN | Evidence is missing, stale, conflicted, unresolved, unsupported for requested time/space, or scope is too broad. | Drawer says “No citable released evidence for this claim.” |
| DENY | Policy blocks exposure because rights, sensitivity, living-person data, DNA, precise rare-species location, archaeology, infrastructure, or source terms are unsafe/unclear. | Exact site geometry withheld; public layer generalized. |
| ERROR | Tool, policy engine, ledger, validator, adapter, resolver, or runtime failed. | Citation validator unavailable; model adapter offline. |

---

## 3. KFM operating law

| Law | Build rule | Failure behavior |
|---|---|---|
| Inspectable claim | Public value is a claim whose evidence, source role, scope, policy, review, release, correction, and rollback can be inspected. | ABSTAIN or DENY if the claim cannot be inspected. |
| Evidence hierarchy | EvidenceBundle and SourceDescriptor outrank map pixels, tiles, graph edges, search indexes, summaries, and generated language. | Generated or rendered-only claims cannot publish. |
| Lifecycle law | `RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED`. | DENY promotion if lifecycle closure is missing. |
| Promotion law | Promotion is a governed state transition, not a file move. | DENY path-only publication. |
| Directory law | File location encodes owner, governance, lifecycle, and responsibility root. | Open drift entry or ADR; do not create parallel authority. |
| Trust membrane | Public clients use governed APIs and released artifacts, not canonical/internal stores. | DENY public raw/canonical access. |
| Cite-or-abstain | Consequential statements cite admissible evidence or abstain. | ABSTAIN on missing/invalid citations. |
| Policy-aware release | Rights, source terms, sensitivity, review, and release state gate exposure. | DENY when uncertain in sensitive areas. |
| Map renderer boundary | MapLibre and other renderers are downstream of trust. | DENY renderer-as-truth. |
| AI boundary | AI is interpretive, provider-neutral, evidence-bounded, policy-checked, and citation-validated. | ABSTAIN/DENY/ERROR; never raw model fallback. |
| Watcher boundary | Watchers propose work; they do not publish. | DENY direct watcher-to-main or watcher-to-published. |
| Reversibility | Every material release has correction, withdrawal, rollback, and cache invalidation paths. | Hold release until rollback target exists. |

---

## 4. Whole-system architecture at a glance

```text
External sources / archives / APIs / field capture / uploads
        |
        v
PRE-RAW EVENT LAYER
(event_envelope -> prefilter_output -> event_run_receipt)
        |
        v
RAW ---------------> QUARANTINE
 |                       ^
 | validation/schema     | unresolved rights, source drift,
 v                       | sensitivity, over-precise geometry
WORK --------------------+
 |
 | normalization, identity, crosswalks, temporalization,
 | geometry transforms, source-role mapping
 v
PROCESSED
 |
 | evidence resolution, domain records, claims, graph projections
 v
CATALOG / TRIPLET
(STAC/DCAT/PROV, CatalogMatrix, relationship projections)
 |
 | promotion gates, policy, review, proof closure,
 | receipts, signatures, manifests, rollback target
 v
PUBLISHED
(api_payloads, layers, pmtiles, geoparquet, reports, stories)
        |
        v
GOVERNED API / TILE SERVICES / CATALOG ENDPOINTS
        |
        v
MAPLIBRE SHELL + EVIDENCE DRAWER + REVIEW + EXPORT + FOCUS MODE
```

### 4.1 Responsibility planes

| Plane | Owns | Must not own |
|---|---|---|
| Source plane | Source descriptors, source terms, retrieval metadata, update cadence, authority role. | Publication decisions. |
| Evidence plane | EvidenceRef, EvidenceBundle, citations, source-role mapping, evidence closure. | Styling or UI behavior. |
| Domain plane | Domain records, temporal assertions, measurements, observation facts, crosswalks. | Public exposure without policy/release. |
| Policy plane | Rights, sensitivity, access class, steward review, public-safe transform. | Canonical truth. |
| Validation plane | Schema checks, contract checks, policy checks, topology checks, citation checks, catalog closure checks. | Replacing review. |
| Publication plane | Release manifests, proof packs, PromotionDecisions, rollback cards, correction notices. | Raw/source intake. |
| Delivery plane | Governed APIs, TileJSON, PMTiles, COG, GeoParquet, STAC/DCAT/PROV endpoints, cache. | Canonical stores. |
| UI/AI plane | Trust-visible exploration, Drawer, Focus Mode, review console, exports, finite outcomes. | Truth authority. |

---

## 5. Proposed repository architecture

**Directory Rules basis:** root folders are responsibility roots, not topic buckets. Domain depth lives under responsibility roots such as `docs/domains/`, `schemas/contracts/v1/domains/`, `policy/domains/`, `tests/domains/`, and `data/<lifecycle>/<domain>/`.

All paths below are **PROPOSED** until verified in a mounted repo and accepted through ADRs/README conventions.

```text
.github/
  workflows/
apps/
  api/
  governed-api/
  explorer-web/
  review-console/
  workers/
connectors/
  <source_family>/
contracts/
  api/
  runtime/
  README.md
control_plane/
  registers/
  drift/
  source_intake/
data/
  raw/
  work/
  quarantine/
  processed/
  catalog/
    stac/
    dcat/
    prov/
    domain/
  triplets/
  receipts/
  proofs/
  published/
  rollback/
  registry/
    sources/
    source_descriptors/
    layers/
    datasets/
    rights/
    sensitivity/
docs/
  doctrine/
  adr/
  architecture/
  control-plane/
  domains/
  runbooks/
  registers/
  sources/
  standards/
fixtures/
  public_safe/
  invalid/
infra/
jsonschema/
packages/
  evidence/
  policy/
  catalog/
  geospatial/
  maplibre-runtime/
  ai/
pipeline_specs/
pipelines/
policy/
  core/
  sensitivity/
  domains/
  ai/
  maplibre/
  release/
release/
  candidates/
  manifests/
  promotion_decisions/
  rollback_cards/
  correction_notices/
  withdrawal_notices/
  signatures/
runtime/
schemas/
  contracts/v1/
    core/
    sources/
    evidence/
    policy/
    catalog/
    promotion/
    release/
    maplibre/
    runtime/
    ai/
    control_loop/
    domains/
scripts/
styles/
tests/
  fixtures/
  contract/
  policy/
  integration/
  e2e/
tools/
  validators/
  attest/
  source_ledger/
  catalog_matrix/
  promotion_gate/
  loop/
ui/
viewer_templates/   # compatibility only if current repo requires it
web/                # compatibility only if current repo requires it
```

### 5.1 Path placement rules for new files

| File type | Proposed home | Rationale |
|---|---|---|
| Human doctrine | `docs/doctrine/` | Governs system-wide truth posture. |
| Architecture notes | `docs/architecture/` | System/subsystem design. |
| Domain docs | `docs/domains/<domain>/` | Domain-specific operating manual. |
| ADRs | `docs/adr/` | Governing decisions and tradeoffs. |
| Machine schemas | `schemas/contracts/v1/<family>/` | Default schema-home convention. |
| API contracts | `contracts/api/` or repo-native OpenAPI home | Interface promise to clients. |
| Runtime envelopes | `schemas/contracts/v1/runtime/` | Machine-verifiable runtime output shape. |
| Source descriptors | `data/registry/source_descriptors/` | Source identity, role, rights, cadence. |
| Policy | `policy/<family>/` | Executable or declarative admissibility gates. |
| Validators | `tools/validators/<family>/` | Deterministic checks; called by CI. |
| Tests | `tests/<family>/` + `tests/fixtures/<family>/` | No-network fixtures and regression tests. |
| Receipts | `data/receipts/<family>/` | Process memory. Not proof by itself. |
| Proofs | `data/proofs/<family>/` | Evidence/proof closure. |
| Release decisions | `release/` | Manifests, promotion decisions, rollback cards, correction notices. |
| Published artifacts | `data/published/<family>/` | Public-safe outputs consumers read. |

---

## 6. Canonical lifecycle

### 6.1 Lifecycle phases

| Phase | Allowed | Must not contain | Required metadata |
|---|---|---|---|
| Pre-RAW | Candidate event envelopes, source-change events, watcher events, upload notices. | Normalized data, public artifacts. | `event_id`, source hint, actor/tool, timestamp, policy precheck, EventRunReceipt. |
| RAW | Immutable source-edge captures. | Public clients, AI context, UI layers, normalized records. | Retrieval time, URL/source, checksum, headers, license snapshot/contact, SourceDescriptor. |
| WORK | Normalized intermediates, candidate assertions, extracted geometries, georeferencing work. | Public API/UI, release aliases. | RunReceipt, transform receipt, candidate IDs, validation status. |
| QUARANTINE | Failed validation, unresolved rights/sensitivity, schema drift, over-precise geometry, source conflicts. | Promotion candidates unless remediated. | Quarantine reason, remediation owner, obligations, source refs. |
| PROCESSED | Validated canonical records not yet public. | Assumption of release/public status. | Deterministic IDs, valid/transaction/source/retrieval time, schema hash, validation report. |
| CATALOG | STAC/DCAT/PROV/domain catalog records. | Uncited claims or unclosed identifiers. | CatalogMatrix, digest, source refs, release refs. |
| TRIPLET | Relationship projections and graph-compatible triples. | Canonical replacement semantics. | Projection manifest, source objects, rebuild recipe. |
| PUBLISHED | Released public-safe artifacts only. | RAW/WORK/QUARANTINE/exact restricted geometry. | ReleaseManifest, PromotionDecision, proof pack, rollback target. |
| RECEIPTS | Process memory: ingest, validation, pipeline, AI, release. | Proof of release by themselves. | Inputs, outputs, tool versions, policy refs, spec_hash. |
| PROOFS | EvidenceBundle, ProofPack, validation report, citation validation. | Process-only receipts without release context. | Evidence closure, citation support, integrity. |
| ROLLBACK | Rollback cards, alias revert receipts, cache invalidation records. | Deleting prior meanings. | Prior release ID, replacement release ID, invalidation target. |
| REGISTRY | Append-only sources, layers, datasets, rights, sensitivity, crosswalks. | Canonical domain truth. | Versioned entries, authority role, status, caveats. |

### 6.2 Promotion gates A–G

The exact gate letters can be finalized by ADR, but the build should preserve this minimum gate sequence:

| Gate | Purpose | Required proof |
|---|---|---|
| A. Source identity | SourceDescriptor exists; source role and authority class known. | SourceDescriptor validation report. |
| B. Rights and terms | License/terms/contact/attribution obligations resolved. | RightsReviewRecord. |
| C. Sensitivity | Living-person, DNA, archaeology, rare species, infrastructure, cultural sensitivity, private land, or sovereignty risks resolved. | PolicyDecision and transform receipts. |
| D. Schema/contract | Artifacts match schemas and API contracts. | SchemaValidationReport. |
| E. Evidence closure | EvidenceRef resolves to EvidenceBundle; citations valid. | EvidenceBundle + CitationValidationReport. |
| F. Catalog/provenance | STAC/DCAT/PROV and CatalogMatrix closed. | CatalogMatrixReport. |
| G. Review/release/rollback | PromotionDecision, release manifest, proof pack, rollback target, correction path. | PromotionReceipt + ReleaseManifest + RollbackCard. |

---

## 7. Core object families

### 7.1 Object map

| Object family | Purpose | Canonical stage | Public exposure |
|---|---|---|---|
| SourceDescriptor | Defines source identity, role, rights, access, update cadence, authority. | Registry / RAW | Only safe metadata. |
| SourceIntakeRecord | Records admission decision for a new source or idea packet. | Pre-RAW / Registry | Administrative. |
| EventEnvelope | Captures a watcher/upload/source-change event before RAW. | Pre-RAW | No public exposure. |
| EventRunReceipt | Signed pre-RAW admission receipt. | Pre-RAW / Receipts | Administrative/proof. |
| RunReceipt | Pins a pipeline/tool action to inputs, outputs, policy, hashes, tool versions. | Receipts | May be referenced in proof. |
| AIReceipt | Records model/tool invocation metadata, not hidden reasoning. | Receipts | Administrative/proof; no private reasoning. |
| EvidenceRef | Small pointer to evidence requiring resolution. | Evidence | Public if released and safe. |
| EvidenceBundle | Resolved, policy-safe evidence context. | Proofs / Published API | Yes, where public-safe. |
| ClaimRecord | A claim with spatial/temporal scope and evidence support. | Processed / Catalog | Yes after release. |
| DecisionEnvelope | Runtime/policy decision payload with finite outcome. | Runtime / Policy | Yes where safe. |
| PolicyDecision | Allow/deny/abstain/error result with reasons. | Policy / Receipts | Summary visible; sensitive reasons may be redacted. |
| ValidationReport | Machine result of schema, geometry, catalog, citation, policy checks. | Proofs / QA | Summary visible. |
| CitationValidationReport | Proves citations resolve to EvidenceBundle/source ledger. | Proofs | Public-safe report. |
| CatalogMatrix | Ties release objects across STAC, DCAT, PROV, digests, assets. | Catalog / Proofs | Yes. |
| TripletManifest | Declares graph/triplet projections and rebuild recipe. | Triplets | Public if released. |
| LayerManifest | Governs map layer identity, evidence, geometry, time, trust badges. | Map delivery | Yes. |
| StyleManifest | Governs style JSON, sprite/glyph hashes, meaning changes, accessibility. | Map delivery | Yes. |
| TileArtifactManifest | Governs MVT/PMTiles/COG/GeoParquet artifact identity and hashes. | Map delivery | Yes. |
| MapReleaseManifest | Binds released layers, styles, tile artifacts, proof pack, rollback. | Release / Published | Yes. |
| PromotionReceipt | Auditable state-transition record with all promotion gates. | Release / Receipts | Summary yes. |
| ProofPack | Release-significant evidence/proof collection. | Proofs / Release | Public-safe subset. |
| RollbackCard | How to restore prior public state and invalidate caches. | Release / Rollback | Yes. |
| CorrectionNotice | Public correction or supersession notice. | Release / Published | Yes. |
| RecompileManifest | Deterministic inputs/outputs for recompiled docs/indexes/artifacts. | Control loop | Administrative/proof. |

### 7.2 Deterministic identity

Use deterministic IDs wherever practical. Suggested pattern:

```text
<namespace>:<object_family>:<stable_key>:<version_or_hash>
```

Examples:

```text
source:usgs:wbd:huc12:v2026-verified
bundle:hydrology:huc12:sha256-...
layer:hydrology:huc12_public:v1
release:map:hydrology_huc12:2026-05-20
claim:frontier:county_year:ks_1870:sha256-...
```

Required identity inputs:

- Source ID and authority role.
- Domain object family.
- Spatial reference and geometry fingerprint when geometry matters.
- Valid time, source time, retrieval time, release time where material.
- Canonicalized payload hash.
- Schema version.
- Transform/policy version where output is derived or public-safe.

### 7.3 Hashing discipline

| Hash | Purpose |
|---|---|
| `content_hash` | Hash of bytes or canonical JSON body. |
| `spec_hash` | Hash of canonical run/config/schema/policy body used to produce output. |
| `geometry_hash` | Hash of normalized geometry with CRS and precision rules. |
| `style_hash` | Hash of style JSON and dependent sprites/glyphs where meaningful. |
| `artifact_hash` | Hash of PMTiles/COG/GeoParquet/report/export. |
| `merkle_root` | Tamper-evident release file set root. |

Hash algorithms should be selected by ADR. SHA-256 is safe as a universal baseline; BLAKE3 can be used for high-speed artifacts such as PMTiles sidecars if the project accepts the dependency and policy posture.

---

## 8. Source intake and watchers

### 8.1 Source admission flow

```text
Source candidate
  -> SourceIntakeRecord
  -> rights/sensitivity/source-role review
  -> SourceDescriptor
  -> pre-RAW event policy
  -> raw capture with retrieval metadata
  -> validation and normalization
```

### 8.2 SourceDescriptor minimum fields

```json
{
  "schema": "kfm.source_descriptor.v1",
  "source_id": "source:agency:dataset:version",
  "source_name": "Human readable source name",
  "source_family": "hydrology | ecology | archives | ...",
  "source_role": "authoritative | governing | observational | derived | corroborative | contextual | exploratory | lineage",
  "authority_scope": "what this source can support",
  "cannot_prove": "what this source must not be used to claim",
  "rights": {
    "license": "NOASSERTION | ...",
    "terms_url": "...",
    "attribution_required": true,
    "public_release_allowed": false
  },
  "sensitivity": {
    "default_access": "public | staged | steward_only | restricted | denied",
    "exact_geometry_allowed_public": false,
    "review_required": true
  },
  "update": {
    "cadence": "weekly | monthly | annual | event-driven | unknown",
    "watcher_allowed": true,
    "materiality_rule_id": "policy://sources/materiality/v1"
  },
  "verification": {
    "last_verified": null,
    "verified_by": null,
    "status": "NEEDS_VERIFICATION"
  }
}
```

### 8.3 Watcher rule

Watchers may:

- Probe source availability and headers.
- Compare ETag/Last-Modified/checksum/material metrics.
- Emit EventEnvelope and PROPOSED_WORK_RECORD.
- Open a reviewed PR or review packet.
- Attach RunReceipt and validation summaries.

Watchers must not:

- Commit directly to main.
- Move data to PUBLISHED.
- Rebuild public artifacts without gates.
- Treat source changes as truth changes without materiality checks.
- Publish AI-generated interpretation.

### 8.4 Material-change sidecars

Use sidecars for high-churn sources such as CDL, PLANTS, air/smoke, hydrology, and map artifacts.

```json
{
  "schema": "kfm.source_watch_sidecar.v1",
  "source_id": "source:usda:cdl:2025:ks",
  "source_url": "...",
  "etag": "...",
  "last_modified": "...",
  "observed_at": "2026-05-20T00:00:00Z",
  "materiality_metrics": {
    "county_fips": "20091",
    "class_histogram_ha": {},
    "relative_pct_threshold": 2.0,
    "absolute_hectares_min": 250
  },
  "spec_hash": "sha256:...",
  "decision": "NO_CHANGE | PROPOSED_WORK_RECORD | QUARANTINE | ERROR"
}
```

---

## 9. Data architecture

### 9.1 Canonical storage recommendation

| Store | Role | Notes |
|---|---|---|
| PostgreSQL + PostGIS | Canonical relational/spatial store for processed records, geometry, relationships, temporal tables, crosswalks. | Use stable schemas, deterministic IDs, access roles, migrations, and row-level policies where needed. |
| Object storage / filesystem | RAW captures, published artifacts, PMTiles, COGs, GeoParquet, receipts, proofs. | Immutable by release ID; no in-place public overwrites. |
| GeoParquet | Processed/published vector-tabular artifacts. | Good for reproducible spatial columnar output and downstream analytics. |
| PMTiles | Public-safe tiled map bundles. | Versioned filenames, range/CORS validation, sidecars, hashes, release manifests. |
| COG | Public-safe or restricted large raster artifacts. | Use manifest-bound access and source/rights checks. |
| STAC/DCAT/PROV | Catalog closure and metadata/provenance. | Derived emissions from receipts/proofs/decisions, not hand-authored release truth. |
| Graph/triplestore/Neo4j/etc. | Relationship projection / triplet layer. | Derived projection only; does not replace canonical domain records. |
| Vector index/search | Retrieval acceleration. | Rebuildable derivative; never root truth. |

### 9.2 Spatial SQL and PostGIS

PostGIS should be the spatial SQL workhorse for:

- CRS-aware geometry storage.
- Geometry validation and repair workflows.
- Spatial joins and overlays.
- Buffering, clipping, intersections, nearest-feature queries.
- Raster/vector conversion where appropriate.
- Topology-aware workflows for boundaries and networks.
- pgRouting-style graph analysis where needed.
- Dynamic tile-serving mediation when public static artifacts are insufficient.

KFM-specific constraints:

- Never expose PostGIS directly to public clients.
- Separate canonical spatial records from public-safe generalized/transformed geometry.
- Record geometry transforms as receipts.
- Version geography and crosswalks explicitly.
- Use database privileges so RAW/WORK/QUARANTINE and restricted exact geometries cannot be accessed by normal UI/API roles.

### 9.3 Temporal and bitemporal posture

KFM must not collapse time into one timestamp.

Minimum temporal axes:

| Axis | Meaning |
|---|---|
| valid_time | When the claim or domain condition is true in the world. |
| observed_time | When a measurement/observation occurred. |
| source_publication_time | When the source published the information. |
| retrieval_time | When KFM acquired it. |
| processing_time | When KFM transformed it. |
| transaction_time | When KFM recorded/changed the internal fact. |
| release_time | When KFM released it publicly/semi-publicly. |
| correction_time | When a correction/withdrawal/supersession occurred. |

Design implication: important tables should support valid-time and transaction-time semantics where historical reconstruction matters.

---

## 10. Domain-lane architecture

Every domain lane should share a common packet:

```text
docs/domains/<domain>/README.md
docs/domains/<domain>/ARCHITECTURE.md
docs/domains/<domain>/SOURCE_ROLE_MATRIX.md
docs/domains/<domain>/SENSITIVITY_POLICY.md
docs/domains/<domain>/VALIDATION_PLAN.md
docs/domains/<domain>/RELEASE_AND_ROLLBACK.md
schemas/contracts/v1/domains/<domain>/*.schema.json
policy/domains/<domain>/*.rego or repo-native policy
connectors/<domain_or_source_family>/
pipelines/<domain>/
tools/validators/<domain>/
tests/fixtures/<domain>/{valid,invalid,public_safe,deny}/
data/registry/source_descriptors/<domain>/
data/processed/<domain>/
data/catalog/{stac,dcat,prov}/<domain>/
data/published/<domain>/
release/manifests/<domain>/
```

### 10.1 Domain-lane minimum contract

| Required item | Purpose |
|---|---|
| Domain README | Plain-language boundary and status. |
| Source role matrix | Defines what each source can and cannot prove. |
| Object-family schema list | Names records, claims, observations, source descriptors, evidence bundles. |
| Sensitivity policy | Public/staged/restricted/deny defaults. |
| Temporal model | Valid/source/retrieval/release/correction time rules. |
| Geometry policy | Exact/generalized/redacted/public-safe rules. |
| Validator list | Deterministic checks and fail-closed behavior. |
| Public layer plan | LayerManifest, StyleManifest, TileArtifactManifest. |
| Evidence Drawer payload | User-facing explanation shape. |
| Focus Mode scope | Allowed questions and abstain/deny cases. |
| Release/rollback plan | Promotion gates and reversion path. |

### 10.2 Hydrology

**Role:** first proof lane candidate.  
**Coverage:** HUCs, watersheds, streams, flowlines, gauges, water observations, flood hazard context, hydrographs, source crosswalks.  
**First slice:** HUC12 public-safe fixture + SourceDescriptor + EvidenceBundle + LayerManifest + MapReleaseManifest dry run.  
**Key sources to model:** WBD/HUC, USGS Water Data, NHDPlus HR/3DHP direction, FEMA NFHL, 3DEP.  
**Risks:** outdated NHD terms, regulatory versus observed flood confusion, station provisional data, stale time series, watershed boundary versioning.  
**Public posture:** public-safe geometry generally possible, but cite source, time, and regulatory/observational distinction.

### 10.3 Soil

**Coverage:** SSURGO/gSSURGO/SDA, soil map units, components, horizons, properties, interpretations, soil moisture context.  
**Risks:** treating map unit as exact ground truth; mixing static soil survey with dynamic moisture; ignoring scale/interpretation caveats.  
**Public posture:** public-safe map layers generally possible with scale/fitness-for-use notes.

### 10.4 Habitat

**Coverage:** habitat patches, ecological systems, suitability, connectivity, restoration, habitat-fauna joins.  
**Risks:** model surfaces as truth; public exact geometry for sensitive habitats; stale landcover.  
**Public posture:** generalized and evidence-bounded; suitability outputs are interpretive derivatives.

### 10.5 Fauna

**Coverage:** taxonomy, occurrence evidence, range, seasonal range, monitoring, corridors, assemblages, invasive species, disease/mortality.  
**Risks:** sensitive species exact locations, nest/den/roost/hibernacula/spawning exposure, aggregator authority confusion, record-level rights.  
**Public posture:** exact sensitive occurrence locations denied by default; public derivatives generalized/redacted with transform receipts.

### 10.6 Flora

**Coverage:** taxonomic identity, plant occurrences/specimens, rare plants, vegetation communities, invasive plants, phenology, remote-sensing vegetation indices.  
**Risks:** rare plant exact locations, community-science quality, herbarium record rights, model/observation confusion.  
**Public posture:** rare exact locations fail closed; generalized public layers with steward review.

### 10.7 Agriculture and landcover

**Coverage:** cropland, CDL, PLANTS, crop history, landcover change, crop stress, irrigation context, field/county summaries.  
**Risks:** noisy annual changes, source-drift false positives, private land inference, over-precise field-level claims.  
**Public posture:** county/generalized products first; material-change watchers propose work only.

### 10.8 Geology and natural resources

**Coverage:** bedrock/surficial geology, stratigraphy, lithology, age, structures, geomorphology, well/core/geophysics/geochemistry, mineral/resource occurrences and estimates.  
**Risks:** conflating physical geology with permits/leases/titles; public exact resource location sensitivity; model uncertainty.  
**Public posture:** public-safe generalized layers; estimates and interpretations clearly labeled.

### 10.9 Atmosphere and air

**Coverage:** air quality, weather observations, smoke, aerosols, climate normals/projections, remote-sensing atmospheric products.  
**Risks:** observed vs modeled vs regulatory vs operational products; emergency-use confusion; freshness and latency.  
**Public posture:** not an alert system; public layers must show source time, freshness, knowledge character, and not-for-life-safety boundary.

### 10.10 Hazards

**Coverage:** historical events, disaster declarations, regulatory hazard areas, operational context, observations, remote-sensing detections, modeled hazards, resilience context.  
**Risks:** becoming an emergency alert system; mixing operational warnings with historical/regulatory/model data; stale warnings; life-safety instructions.  
**Public posture:** not for emergency response; direct users to official alerting and source guidance.

### 10.11 Roads, rail, and trade routes

**Coverage:** modern roads, rail corridors, historic trails, ferries/crossings, depots, yards, trade/mobility corridors, restrictions, graph projections.  
**Risks:** conflating alignment, ownership, operator, legal status, and route claim; false precision for historic/Indigenous/cultural corridors.  
**Public posture:** historic and cultural routes generalized unless reviewed evidence supports precision; graph projections derived only.

### 10.12 Settlements, cities, and infrastructure

**Coverage:** municipalities, census places, townsites, ghost towns, forts, depots, missions, reservation communities, infrastructure assets, service areas, operators, dependencies.  
**Risks:** critical infrastructure exposure, private landowner sensitivity, condition/security misuse, confusing legal city with census/historic place.  
**Public posture:** staged/generalized for sensitive assets; legal and historical identity clearly separated.

### 10.13 Archaeology

**Coverage:** archaeological sites, surveys, remote-sensing anomalies, LiDAR candidates, cultural resources, stratigraphy, 3D/site models, steward review.  
**Risks:** looting, exact site exposure, burial/human remains, sacred places, cultural sensitivity, private land, remote-sensing false positives.  
**Public posture:** exact archaeological site locations denied by default; public output uses reviewed generalized/suppressed geometry and transform receipts.

### 10.14 People, genealogy, DNA, and land ownership

**Coverage:** person assertions, genealogy, family relationships, DNA/genomics, land ownership assertions, parcels, deeds, assessor/tax context, temporal land tenure.  
**Risks:** living-person data, DNA/genomic sensitivity, relationship hypotheses as truth, assessor/tax rows as title truth, parcel geometry as legal boundary proof.  
**Public posture:** living-person and DNA-derived outputs denied/restricted by default. Land ownership is temporal evidence-bound assertion, not a map label alone.

### 10.15 Frontier demography/economy flagship panel

**Coverage:** county-year frontier panel with population, economy, agriculture, access, geography versions, frontier definitions.  
**First objects:** `FrontierDefinition`, `GeographyVersion`, `PopulationObservation`, `EconomicObservation`, `AgricultureObservation`, `AccessObservation`.  
**Risks:** building flagship analysis before source/geography/version proof; flattening uncertainty; treating counties as stable over time.  
**Public posture:** after proof lane, release as versioned analytical layer with evidence-backed definitions and explicit uncertainty.

---

## 11. Evidence and claim model

### 11.1 Claim lifecycle

```text
Candidate claim
  -> source/evidence support attached
  -> spatial and temporal scope declared
  -> source role checked
  -> policy/sensitivity checked
  -> validation report passes
  -> review state recorded
  -> release manifest binds claim to proof
  -> public API/UI exports claim with citations and correction state
```

### 11.2 ClaimRecord sketch

```json
{
  "schema": "kfm.claim_record.v1",
  "claim_id": "claim:hydrology:huc12:...",
  "claim_text": "A bounded public-safe claim.",
  "domain": "hydrology",
  "object_refs": ["domain_object_id"],
  "spatial_scope": {
    "geometry_ref": "geom:...",
    "crs": "EPSG:4326",
    "precision_policy": "public_exact_or_generalized"
  },
  "temporal_scope": {
    "valid_time": "2024-01-01/..",
    "source_time": "2024-01-01",
    "release_time": "2026-05-20"
  },
  "evidence_refs": ["eref:..."],
  "source_roles": ["authoritative_context"],
  "policy_decision_id": "policy_decision:...",
  "review_state": "draft | reviewed | published | withdrawn",
  "release_id": "release:...",
  "correction_state": "current | corrected | superseded | withdrawn"
}
```

### 11.3 EvidenceBundle sketch

```json
{
  "schema": "kfm.evidence_bundle.v1",
  "bundle_id": "bundle:hydrology:huc12:...",
  "evidence_refs": [
    {
      "evidence_ref_id": "eref:001",
      "source_id": "source:usgs:wbd:huc12",
      "source_role": "authoritative_context",
      "citation": "...",
      "retrieval_receipt_id": "receipt:ingest:...",
      "supports": ["claim:..."]
    }
  ],
  "rights": {
    "public_release_allowed": true,
    "attribution": "required"
  },
  "sensitivity": {
    "public_safe": true,
    "exact_geometry_allowed": true
  },
  "validation": {
    "schema_report_id": "validation:...",
    "citation_report_id": "citation:..."
  }
}
```

---

## 12. Catalog, triplet, proof, and release architecture

### 12.1 Catalog closure

KFM should emit STAC, DCAT, and PROV records as **derived catalog artifacts** from release candidates, not as manually authored substitute truth.

| Catalog object | Purpose |
|---|---|
| STAC Item/Collection | Spatial-temporal asset metadata for COG, PMTiles, GeoParquet, reports, outputs. |
| DCAT Dataset/Distribution | Web catalog interoperability and dataset/service descriptions. |
| PROV Entity/Activity/Agent | Provenance graph for source, transformation, validation, release. |
| CatalogMatrix | KFM closure report that binds STAC/DCAT/PROV/digests/release IDs/proof packs. |

### 12.2 CatalogMatrix sketch

```json
{
  "schema": "kfm.catalog_matrix.v1",
  "release_id": "release:map:hydrology_huc12:2026-05-20",
  "assets": [
    {
      "asset_id": "tileartifact:huc12_pmtiles:v1",
      "artifact_type": "pmtiles",
      "artifact_hash": "sha256:...",
      "stac_ref": "stac:item:...",
      "dcat_ref": "dcat:distribution:...",
      "prov_entity_ref": "prov:entity:...",
      "evidence_bundle_id": "bundle:...",
      "policy_decision_id": "policy:..."
    }
  ],
  "closure_status": "closed | open | failed",
  "validation_report_id": "validation:catalog_matrix:..."
}
```

### 12.3 PMTiles attestation sidecar

For public PMTiles, use a signed sidecar pattern:

```json
{
  "schema_version": "v1",
  "pmtiles_filename": "hydrology_huc12_public_v1.pmtiles",
  "spec_hash": "sha256:...",
  "root_hash": "sha256:...",
  "size_bytes": 123456,
  "byte_ranges_manifest": [
    {
      "z": 8,
      "x": 42,
      "y": 96,
      "start": 1000,
      "end": 2000,
      "range_hash": "sha256:...",
      "proof_ref": "..."
    }
  ],
  "attestations": {
    "build_id": "run:...",
    "source_ledger_ref": "source:...",
    "run_receipt_ref": "receipt:...",
    "license_notes": []
  }
}
```

Fail closed if:

- `root_hash` missing.
- `spec_hash` missing.
- signature missing or invalid.
- byte-range manifest malformed.
- sensitive layer lacks public-safe policy.
- release manifest lacks rollback target.

---

## 13. Governed API architecture

### 13.1 API principles

1. API responses are contracts, not incidental JSON.
2. Public APIs never expose RAW, WORK, QUARANTINE, unpublished candidates, private source folders, or canonical stores directly.
3. Every consequential response has a release state and evidence policy.
4. Negative outcomes are first-class payloads.
5. Request scope must carry map context, time context, user role, and release ID where relevant.
6. API docs must include examples for ANSWER, ABSTAIN, DENY, and ERROR.

### 13.2 Proposed API resource families

| Resource | Purpose |
|---|---|
| `/api/catalog` | Public catalog discovery over released records. |
| `/api/layers` | LayerManifest discovery. |
| `/api/releases/{release_id}` | Release manifest and rollback/correction state. |
| `/api/evidence/{bundle_id}` | EvidenceBundle resolution where public-safe. |
| `/api/claims/{claim_id}` | Inspectable claim view. |
| `/api/map/resolve-feature` | Feature click -> governed evidence resolution. |
| `/api/map/context` | MapContextEnvelope creation. |
| `/api/focus/query` | Evidence-bounded AI request. |
| `/api/review/*` | Role-gated review/steward actions. |
| `/api/export/*` | Export artifacts with citations/release metadata. |
| `/api/health/public` | Public health without internals. |
| `/api/admin/*` | Authenticated administrative diagnostics. |

### 13.3 Feature-click request and response

```json
{
  "schema": "kfm.map.feature_click_request.v1",
  "layer_id": "hydrology.huc12.public.v1",
  "feature_id": "huc12:...",
  "release_id": "release:...",
  "active_time": "2026-05-20/..",
  "viewport": {"bbox": [-102, 37, -94, 40], "crs": "EPSG:4326"},
  "user_role": "public"
}
```

```json
{
  "schema": "kfm.ui.evidence_drawer_payload.v1",
  "outcome": "ANSWER",
  "selection_id": "sel:...",
  "candidate_feature": {"layer_id": "hydrology.huc12.public.v1", "feature_id": "huc12:..."},
  "claim_summary": "Public-safe hydrologic unit summary.",
  "evidence_bundle_id": "bundle:...",
  "citations": [{"evidence_ref_id": "eref:001", "source_role": "authoritative_context"}],
  "time_scope": {"valid_time": "...", "release_time": "..."},
  "policy_badges": ["public_safe", "released", "citable"],
  "withheld_counts": {"sensitive_features": 0},
  "correction_state": "current"
}
```

---

## 14. MapLibre and UI architecture

### 14.1 Renderer rule

MapLibre should be the first disciplined 2D renderer and interaction runtime. It may render released artifacts, expose candidate feature IDs, track camera/time state, and drive users to governed APIs. It must not act as truth store, policy engine, publication authority, citation authority, review authority, or AI authority.

### 14.2 Shell surfaces

| Surface | Role | Trust requirement |
|---|---|---|
| Explore | Navigate layers, time, feature selection, trust cues. | Selection resolves through governed API. |
| Evidence Drawer | Shows evidence refs, source roles, citations, rights, sensitivity, review, release, correction. | Every consequential claim resolves to EvidenceBundle. |
| Dossier | Durable object/claim view. | Evidence and time continuity visible. |
| Story | Map-anchored narrative. | Cannot detach from evidence/citation/correction lineage. |
| Compare | Side-by-side releases/times/sources. | Each side has independent release/evidence context. |
| Focus Mode | Evidence-bounded AI. | Finite outcomes; no raw model output. |
| Review | Role-gated steward/reviewer shell. | Review state changes logged and separate from public behavior. |
| Export | Exported artifacts. | Trust metadata, citations, release ID, correction state travel with output. |
| Diagnostics | Authorized manifest/runtime inspection. | Not a public raw/canonical backdoor. |

### 14.3 Trust-visible negative states

The UI must distinguish:

- `MISSING_EVIDENCE`
- `SOURCE_STALE`
- `DENIED_BY_POLICY`
- `GENERALIZED_GEOMETRY`
- `RESTRICTED_ACCESS`
- `CONFLICTED_SUPPORT`
- `CITATION_FAILED`
- `RELEASE_WITHDRAWN`
- `RUNTIME_ERROR`
- `RIGHTS_UNKNOWN`
- `SENSITIVE_LOCATION_BLOCKED`

### 14.4 LayerManifest sketch

```json
{
  "schema": "kfm.map.layer_manifest.v1",
  "layer_id": "hydrology.huc12.public.v1",
  "domain": "hydrology",
  "release_id": "release:map:hydrology_huc12:2026-05-20",
  "artifact_refs": ["tileartifact:huc12_pmtiles:v1"],
  "evidence_policy": {
    "requires_evidence_bundle": true,
    "supports_popup_claims": false,
    "drawer_payload_contract": "kfm.ui.evidence_drawer_payload.v1"
  },
  "geometry_policy": {
    "public_precision": "exact_or_generalized_by_policy",
    "sensitive_exact_geometry_allowed": false,
    "withheld_accounting_required": true
  },
  "time_model": ["valid_time", "source_publication_time", "release_time", "stale_time"],
  "trust_badges": ["released", "citable", "public_safe"],
  "stale_policy": {"mode": "visible_badge_and_focus_abstain"}
}
```

### 14.5 StyleManifest sketch

```json
{
  "schema": "kfm.map.style_manifest.v1",
  "style_id": "kfm_public_default_style_v1",
  "style_spec_version": 8,
  "style_json_hash": "sha256:...",
  "sprite_hash": "sha256:...",
  "glyph_hash": "sha256:...",
  "font_policy": "pinned_or_local_reviewed",
  "bound_layer_ids": ["hydrology.huc12.public.v1"],
  "meaning_change_requires_release": true,
  "accessibility_notes": ["contrast_checked", "non_color_trust_cues_required"]
}
```

---

## 15. Governed AI and Focus Mode

### 15.1 AI rule

AI may interpret released, policy-safe evidence. It may not decide truth, read canonical stores directly, bypass policy, publish uncited answers, or expose chain-of-thought/private reasoning.

### 15.2 Adapter order

| Adapter | Role | Build phase |
|---|---|---|
| MockAdapter | Deterministic fixture adapter; no network/model. | First implementation. |
| NullAdapter | Explicit disabled/offline adapter returning ABSTAIN/ERROR. | With MockAdapter. |
| OllamaAdapter | Local/private runtime behind governed API only. | After contracts, policy, citation tests. |
| OpenAICompatibleAdapter | Provider-compatible runtime behind same internal contract. | After adapter contract and external provider verification. |

### 15.3 Focus Mode flow

```text
User question + MapContextEnvelope
  -> policy precheck
  -> EvidenceRef -> EvidenceBundle resolver
  -> provider-neutral ModelAdapter
  -> structured output
  -> CitationValidator
  -> policy postcheck
  -> RuntimeResponseEnvelope
  -> AIReceipt + RunReceipt
  -> UI finite outcome
```

### 15.4 RuntimeResponseEnvelope sketch

```json
{
  "schema": "kfm.runtime.response_envelope.v1",
  "request_id": "focus_req:...",
  "outcome": "ANSWER | ABSTAIN | DENY | ERROR",
  "answer": "Bounded cited answer only when outcome is ANSWER.",
  "citations": ["eref:001"],
  "abstain_reason": null,
  "denial_reason": null,
  "error_code": null,
  "policy_decision_id": "policy:...",
  "citation_validation_report_id": "citation:...",
  "ai_receipt_id": "receipt:ai:...",
  "release_id": "release:...",
  "visible_limitations": ["Only released public-safe evidence used."]
}
```

### 15.5 AI hard denials

Deny or error when:

- Browser calls model runtime directly.
- Context includes RAW/WORK/QUARANTINE/private/canonical direct access.
- Evidence is not published/cataloged/proof-backed.
- Sensitive precise geometry would leak.
- Rights are unknown.
- Citation validator fails.
- Source ledger is missing.
- Policy engine unavailable.
- Model output includes uncited consequential claims.

---

## 16. Security architecture

### 16.1 Security posture

KFM should combine KFM doctrine, SDL-style lifecycle discipline, NIST SSDF, OWASP verification practices, and least-privilege operations.

| Security area | Build requirement |
|---|---|
| Training | Developers/reviewers understand KFM trust law, source sensitivity, secure coding, threat modeling, and release gates. |
| Threat modeling | Model trust boundaries for source intake, API, map shell, AI runtime, proof stores, admin routes, and connectors. |
| Bug bar | Define security/privacy bug classes and severity before implementation. |
| Secure coding | Avoid unsafe APIs, injection patterns, unbounded resource use, insecure deserialization, weak crypto, secrets in logs. |
| Secure testing | Static analysis, dependency scanning, unit tests, fuzzing for parsers/connectors, policy tests, red-team style misuse fixtures. |
| Final review | Require final security/release review before publishing public surfaces. |
| Response | Maintain vulnerability response runbook, owners, supported components, rollback strategy, communications. |

### 16.2 Trust boundaries to threat model

| Boundary | Threats |
|---|---|
| External source -> pre-RAW | malicious content, source spoofing, license ambiguity, schema drift, huge payloads. |
| RAW -> WORK | parser bugs, injection, geospatial topology failures, unbounded processing. |
| WORK -> PROCESSED | false identity merging, temporal collapse, lost provenance. |
| PROCESSED -> PUBLISHED | policy bypass, sensitivity leak, uncited claims, stale data. |
| API -> client | broken object-level authorization, excessive data exposure, rate/resource abuse. |
| Map client -> API | feature ID tampering, bbox scraping, hidden sensitive geometry inference. |
| UI -> AI runtime | prompt injection, source leakage, direct model access, uncited answer. |
| Admin/review routes | privilege escalation, audit bypass, unauthorized promotion. |
| Artifact hosting | in-place overwrite, stale CDN, missing signatures, range request issues. |

### 16.3 Deployment rules

- Deny by default.
- Public routes go through governed API only.
- Admin/debug/proof/source-ledger/model-health routes require authentication and authorization.
- No direct public traffic to local model runtimes.
- Do not expose Ollama or equivalent model APIs directly.
- Use TLS, rate limits, request size limits, audit logging, and safe CORS/CSP.
- Never commit secrets.
- Logs include request IDs, policy decisions, adapter metadata, citation report IDs, and receipt IDs; logs exclude secrets, private reasoning, raw sensitive evidence, and unrestricted source dumps.
- Published artifacts are immutable by release ID.

---

## 17. Validation, testing, and CI

CI should be thin orchestration that calls repo-native tools. The validators are the trust membrane.

### 17.1 Required checks

| Check | Purpose |
|---|---|
| schema validation | All JSON Schemas and fixtures pass. |
| API contract tests | OpenAPI/runtime envelopes match examples. |
| policy tests | Allow/deny/abstain/error fixtures pass. |
| source-ledger tests | Source IDs, aliases, authority roles, unresolved refs checked. |
| source-rights tests | Unknown rights block public release. |
| sensitivity tests | Rare species/archaeology/DNA/infrastructure exact exposure denied. |
| geometry tests | CRS, topology, precision, simplification, withheld accounting. |
| temporal tests | Valid/source/retrieval/release/correction time preserved. |
| evidence tests | EvidenceRef resolves to EvidenceBundle. |
| citation tests | Claims cite valid evidence/source records. |
| catalog matrix tests | STAC/DCAT/PROV/digest/release closure. |
| promotion gate tests | PromotionReceipt complete; release denied on missing gates. |
| PMTiles/COG tests | Hash, sidecar, signature, Range/CORS, media type. |
| no-public-raw-path | Public API/UI cannot reference RAW/WORK/QUARANTINE. |
| no-direct-model-client | UI/browser cannot call model runtime directly. |
| accessibility tests | Drawer, keyboard navigation, non-color trust cues, contrast. |
| E2E smoke | Click -> API resolve -> Drawer -> Focus finite outcome -> receipt. |
| rollback test | Previous release manifest can be restored and caches invalidated. |

### 17.2 Suggested CI command matrix

```text
make validate-schemas
make validate-source-ledger
make validate-policy
make validate-catalog-matrix
make validate-citations
make test-unit
make test-integration
make test-e2e-public-safe
make check-no-public-raw-path
make check-no-direct-model-client
make check-accessibility
make build-release-dry-run
make rollback-dry-run
```

### 17.3 Fixtures to create first

| Fixture | Expected outcome |
|---|---|
| public-safe hydrology HUC12 EvidenceBundle | ANSWER |
| missing EvidenceBundle | ABSTAIN |
| stale source | ABSTAIN |
| unknown rights | DENY |
| sensitive exact geometry | DENY |
| unpublished candidate | DENY |
| invalid citation | ABSTAIN or ERROR |
| policy engine unavailable | ERROR/DENY |
| bad PMTiles hash | DENY publication |
| missing rollback target | DENY promotion |

---

## 18. Query-save-recompile control loop

### 18.1 Loop purpose

The loop should improve KFM documentation, registries, schemas, indexes, catalogs, fixtures, and derived artifacts without autonomous publication.

```text
query -> save -> validate -> compile -> review -> promote -> recompile
```

### 18.2 Loop object families

| Object | Purpose |
|---|---|
| QueryRunRecord | Saved query/work session metadata without private chain-of-thought. |
| EvidenceResolutionRecord | What evidence was retrieved/resolved. |
| CandidateDelta | Proposed doc/schema/policy/source/test changes. |
| RecompileManifest | Inputs/outputs/hashes for derived rebuild. |
| LoopValidationReport | Schema/policy/source coverage results. |
| LoopDecision | Review/promotion/deny decision. |
| LoopRollbackReference | How to undo the loop output. |

### 18.3 Loop policies

- No autopublish.
- No generated text as root truth.
- No private chain-of-thought storage.
- No raw public path.
- Evidence closure required before promotion.
- Human/steward review required for sensitive or release-significant material.

---

## 19. Implementation roadmap

### Phase 0 — Live repo conformance and ADR baseline

**Goal:** establish current implementation truth before adding files.

Tasks:

1. Run `git status`, branch, commit, tree inventory.
2. Inspect root directories and package markers.
3. Locate schema home, contracts home, policy tooling, app/API/UI framework, tests, CI workflows.
4. Compare with Directory Rules.
5. Open drift entries where repo and doctrine diverge.
6. Accept/update ADRs for schema home, source ledger, map shell, AI adapter, release/proof homes.

Exit criteria:

- `docs/registers/DRIFT_REGISTER.md` updated or confirmed clean.
- Schema-home ADR accepted or verified current.
- No new parallel authority roots introduced.

### Phase 1 — Governance skeleton

Deliver:

- Directory doctrine in repo.
- Source ledger skeleton.
- Authority register.
- Policy register.
- Validator register.
- Release register.
- Initial core schemas.
- No-network fixtures.

Exit criteria:

- Schemas validate.
- Source ledger validates.
- Policy default deny works.
- Documentation links pass.

### Phase 2 — Evidence and receipt core

Deliver:

- SourceDescriptor schema.
- EvidenceRef and EvidenceBundle schemas.
- RunReceipt and ValidationReport schemas.
- CitationValidationReport schema.
- Deterministic ID/hash helper.

Exit criteria:

- Public-safe evidence fixture resolves.
- Missing/stale/conflicted evidence abstains.
- Unresolved source denies/abstains.

### Phase 3 — First domain proof slice

Recommended: hydrology HUC12 or ecology/landcover county sidecar.

Deliver:

- Domain README and architecture.
- SourceDescriptor.
- Processed fixture.
- EvidenceBundle.
- LayerManifest.
- StyleManifest.
- TileArtifactManifest or GeoJSON fixture.
- MapReleaseManifest dry run.

Exit criteria:

- E2E: click feature -> evidence drawer -> finite Focus response -> receipt.
- No live connectors required.

### Phase 4 — Catalog closure

Deliver:

- STAC/DCAT/PROV profile.
- CatalogMatrix validator.
- Release manifest binds catalog records.

Exit criteria:

- Catalog closure validates.
- Human-authored catalog records cannot bypass release logic.

### Phase 5 — Policy and sensitivity hardening

Deliver:

- Rights policy.
- Sensitivity policy.
- Domain deny fixtures.
- Withheld accounting.
- Public-safe geometry transform receipts.

Exit criteria:

- Sensitive exact geometry denied.
- Unknown rights denied.
- Redaction/generalization recorded.

### Phase 6 — Map shell

Deliver:

- MapLibre shell with manifest-driven layer catalog.
- Evidence Drawer.
- Negative-state badges.
- Time scope propagation.
- Accessibility baseline.

Exit criteria:

- No raw/canonical direct access.
- Layer toggle denied if unreleased.
- Drawer validates evidence.

### Phase 7 — Governed AI MockAdapter

Deliver:

- ModelAdapter contract.
- MockAdapter.
- RuntimeResponseEnvelope.
- AIReceipt.
- Citation validation.
- Focus Mode UI fixture.

Exit criteria:

- ANSWER, ABSTAIN, DENY, ERROR fixtures pass.
- No direct browser/model access.

### Phase 8 — Release and rollback dry run

Deliver:

- PromotionReceipt.
- ProofPack.
- ReleaseManifest.
- RollbackCard.
- CorrectionNotice fixture.
- Cache invalidation proof.

Exit criteria:

- Release candidate can publish dry-run and roll back dry-run.

### Phase 9 — Live connector pilot

Deliver:

- One source connector with rights verified.
- Source watcher.
- No-publication default.
- Material-change sidecar.

Exit criteria:

- Connector can ingest to RAW/WORK only.
- Watcher emits proposed work, not publication.

### Phase 10 — Broaden domain lanes

Order recommendation:

1. Hydrology.
2. Soil / agriculture / landcover.
3. Habitat + fauna + flora public-safe derivatives.
4. Atmosphere + hazards with not-emergency-alert boundary.
5. Roads/rail/trade + settlements/infrastructure.
6. Geology/natural resources.
7. Archaeology with steward controls.
8. People/genealogy/DNA/land ownership with living-person/DNA restrictions.
9. Frontier demography/economy panel.

---

## 20. First PR package

The first PR should be small, reversible, and no-network.

### 20.1 Files

```text
docs/doctrine/directory-rules.md
docs/doctrine/truth-posture.md
docs/doctrine/lifecycle-law.md
docs/doctrine/trust-membrane.md
docs/adr/ADR-0001-schema-home.md
docs/registers/SOURCE_LEDGER.md
docs/registers/DRIFT_REGISTER.md
docs/registers/VALIDATOR_REGISTER.md
schemas/contracts/v1/core/source_descriptor.schema.json
schemas/contracts/v1/evidence/evidence_ref.schema.json
schemas/contracts/v1/evidence/evidence_bundle.schema.json
schemas/contracts/v1/receipts/run_receipt.schema.json
schemas/contracts/v1/policy/policy_decision.schema.json
schemas/contracts/v1/runtime/runtime_response_envelope.schema.json
policy/core/default_deny.rego
tools/validators/schema_validate.py
tools/validators/source_ledger_validate.py
tests/fixtures/core/valid/source_descriptor.public_safe.json
tests/fixtures/core/invalid/source_descriptor.unknown_rights.json
tests/fixtures/evidence/valid/evidence_bundle.public_safe.json
tests/fixtures/runtime/answer.json
tests/fixtures/runtime/abstain_missing_evidence.json
tests/fixtures/runtime/deny_sensitive.json
tests/fixtures/runtime/error_policy_unavailable.json
```

### 20.2 Acceptance criteria

- No live connectors.
- No model calls.
- No public release.
- All fixtures validate.
- Default-deny policy works.
- Source ledger has at least one public-safe synthetic or published source entry.
- Runtime outcomes are finite.
- All paths conform to Directory Rules or have ADR/drift note.

---

## 21. Anti-pattern register

| Anti-pattern | Required response |
|---|---|
| Treating map layer as truth | DENY; require EvidenceBundle. |
| Treating tiles/COGs/PMTiles as proof | DENY; require manifest/evidence/proof closure. |
| Publishing via file move | DENY; promotion is state transition. |
| Watcher commits to main | DENY; watcher opens PR/review packet. |
| AI answers from rendered map properties only | ABSTAIN/DENY; rendered features are candidates. |
| Direct browser access to model runtime | DENY. |
| Direct public access to canonical/PostGIS/RAW/WORK/QUARANTINE | DENY. |
| Unknown rights public release | DENY/ABSTAIN. |
| Style-only sensitive geometry hiding | DENY; transform/redact/generalize before release. |
| Catalog record manually authored as release truth | DENY; catalog is derived from receipts/proofs/decision. |
| Graph projection replaces canonical truth | DENY. |
| Assessor parcel treated as title proof | ABSTAIN/DENY depending claim. |
| DNA/living-person data published by default | DENY. |
| Archaeological exact site public by default | DENY. |
| Hazard lane used as emergency alerting | DENY; point to official sources. |
| MLT/3D/native/mobile declared production before parity proof | NEEDS VERIFICATION. |
| Package pin based on stale docs | NEEDS VERIFICATION. |
| Security review left until after release | DENY release. |

---

## 22. Governance roles

| Role | Responsibility |
|---|---|
| Docs steward | Directory doctrine, documentation authority, ADR hygiene, source ledger readability. |
| Source steward | Source descriptors, rights, terms, update cadence, source role. |
| Domain lead | Domain object model, source-role matrix, validators, domain fixtures. |
| Policy steward | Sensitivity, rights, access, default-deny policy, policy tests. |
| Evidence steward | EvidenceBundle contracts, citation validation, proof closure. |
| Data engineer | Ingest, normalization, PostGIS, GeoParquet/PMTiles/COG pipeline. |
| API engineer | Governed API contracts, authorization, runtime envelopes. |
| UI/map engineer | MapLibre shell, layer manifests, Drawer, trust-visible states. |
| AI/runtime engineer | Adapter contract, MockAdapter, model runtime isolation, AIReceipt. |
| Security reviewer | Threat model, secure coding/testing, dependency review, response plan. |
| Release steward | Promotion gates, release manifests, proof packs, rollback/correction. |
| Reviewer/steward | Human review for sensitive, cultural, living-person, rights, release-significant changes. |

Use RACI matrices for each PR wave.

---

## 23. Runbooks to create

| Runbook | Purpose |
|---|---|
| Source intake | Admit/deny/quarantine new source. |
| Source watcher | Configure material-change watcher safely. |
| Rights review | Resolve license/terms/attribution/public release posture. |
| Sensitivity review | Handle rare species, archaeology, living person, DNA, infrastructure, cultural sensitivity. |
| Evidence resolution | Resolve EvidenceRef to EvidenceBundle. |
| Citation validation | Validate claim support. |
| Domain release | Promote domain layer/report/story. |
| PMTiles publication | Build, attest, host, verify Range/CORS, rollback. |
| COG publication | Build, verify, catalog, release. |
| AI Focus Mode | Add model adapter or prompt safely. |
| Security incident | Triage vulnerability, assign owner, patch, communicate. |
| Correction/withdrawal | Issue correction notice, supersede claim, invalidate cache, rollback. |
| Repo drift | Record and resolve path/schema/policy drift. |

---

## 24. Acceptance checklist for “whole system ready for first public proof”

KFM is not ready for a public proof release until:

- [ ] Directory Rules accepted or reconciled through ADR.
- [ ] Schema-home ADR accepted.
- [ ] Source ledger exists and validates.
- [ ] Source authority and source-role matrix exists for proof domain.
- [ ] Rights and sensitivity policies exist with deny fixtures.
- [ ] EvidenceRef resolves to EvidenceBundle.
- [ ] Citation validator passes and fails correctly.
- [ ] CatalogMatrix closes STAC/DCAT/PROV/digest/release refs.
- [ ] PromotionReceipt has all required gates.
- [ ] ReleaseManifest has rollback target.
- [ ] Public API cannot access RAW/WORK/QUARANTINE/canonical stores.
- [ ] MapLibre layer is manifest-bound.
- [ ] Evidence Drawer shows source/evidence/policy/release/correction.
- [ ] Focus Mode uses MockAdapter or governed adapter only.
- [ ] Focus Mode returns ANSWER/ABSTAIN/DENY/ERROR only.
- [ ] No direct model runtime access from browser/client.
- [ ] UI shows negative trust states.
- [ ] Accessibility smoke passes.
- [ ] Security threat model complete for proof slice.
- [ ] Release dry run passes.
- [ ] Rollback dry run passes.

---

## 25. Open verification backlog

| Item | Status | Verification action |
|---|---|---|
| Current live repo topology | UNKNOWN | Mount repo; run tree/package/workflow/schema-policy scan. |
| `contracts/` vs `schemas/` authority | NEEDS VERIFICATION | Inspect ADR-0001 and current schema homes. |
| Package manager and UI framework | UNKNOWN | Inspect package files and app tree. |
| Policy engine | UNKNOWN | Inspect OPA/Conftest/Rego or repo-native equivalent. |
| Existing proof/receipt/release artifacts | UNKNOWN | Inspect `data/receipts`, `data/proofs`, `release`, generated outputs. |
| MapLibre version and lockfile | NEEDS VERIFICATION | Inspect lockfile and official MapLibre releases before pinning. |
| PostGIS/PostgreSQL version | NEEDS VERIFICATION | Inspect database/runtime configuration. |
| PMTiles/COG hosting headers | NEEDS VERIFICATION | Test Range/CORS/cache behavior in target hosting. |
| Source rights for live connectors | NEEDS VERIFICATION | Verify official terms and record SourceDescriptor. |
| Steward review requirements | NEEDS VERIFICATION | Identify responsible stewards for archaeology, cultural, DNA, rare species, infrastructure. |
| Branch protections and release approvals | UNKNOWN | Inspect platform settings. |
| Security response ownership | UNKNOWN | Assign response owners and supported component inventory. |
| AI runtime exposure | NEEDS VERIFICATION | Inspect deployment/proxy/firewall; ensure private binding. |

---

## 26. Build sequence summary

```text
0. Verify live repo and accept path/schema ADRs.
1. Add governance skeleton and source ledger.
2. Add core schemas, receipts, evidence, policy decisions.
3. Add first public-safe hydrology/ecology fixture.
4. Add catalog closure and release dry run.
5. Add MapLibre shell + Drawer from manifests.
6. Add Focus Mode with MockAdapter and finite outcomes.
7. Add rollback/correction dry run.
8. Add first live connector only after rights/source/security verification.
9. Broaden domain lanes in dependency order.
10. Build frontier demography/economy panel after geography/source proof.
```

---

## 27. Source-aware notes for implementation teams

### 27.1 Engineers

Build adapters and validators first. Do not make the first public artifact depend on live external services, a model runtime, or a broad UI.

### 27.2 Domain leads

Your first deliverable is not a dataset. It is a domain contract packet: source-role matrix, object families, sensitivity policy, validators, fixtures, public-safe layer plan, and release/rollback plan.

### 27.3 UI/map team

The map shell is part of the trust system. Popups must not turn feature properties into authoritative claims. The Drawer is the trust object; Focus Mode is evidence-bounded interpretation.

### 27.4 AI team

Start with MockAdapter. Add real providers only after schema, policy, source ledger, citation, and finite-outcome tests pass. Do not persist hidden chain-of-thought. Do not expose local model APIs to clients.

### 27.5 Release/security team

Treat public release like a security-sensitive event. Require proofs, rollback, signatures where appropriate, policy decisions, and response owners.

---

## 28. Glossary

| Term | Meaning |
|---|---|
| Inspectable claim | Public/semi-public assertion reconstructable to evidence, scope, policy, review, release, correction, and rollback. |
| EvidenceRef | Pointer to evidence that must resolve before use. |
| EvidenceBundle | Resolved evidence context that outranks maps, summaries, and generated text. |
| SourceDescriptor | Source identity, role, authority, rights, access, cadence, caveats. |
| RunReceipt | Process memory for a tool/pipeline action. |
| AIReceipt | Process memory for AI/model/tool invocation metadata. |
| ProofPack | Release-significant proof bundle. |
| CatalogMatrix | Closure report tying STAC/DCAT/PROV/digests/assets/release IDs. |
| PromotionReceipt | Auditable record of promotion gates and outcome. |
| ReleaseManifest | Bindings for released artifacts, proof packs, rollback, correction. |
| RollbackCard | Instructions and evidence for reverting public state. |
| MapReleaseManifest | Release manifest for map layers/styles/tile artifacts. |
| LayerManifest | Governs map layer identity, evidence, time, geometry, trust badges. |
| StyleManifest | Governs map style identity, hashes, accessibility, meaning changes. |
| Focus Mode | Evidence-bounded AI interaction inside governed shell. |
| Trust membrane | Boundary preventing raw/internal/unreviewed truth from leaking into public surfaces. |
| Public-safe | Released, rights-cleared, sensitivity-reviewed, citable, reviewable, rollback-capable. |
| Quarantine | Safe holding area for failed validation, unresolved rights/sensitivity, schema drift, over-precise geometry. |

---

## 29. Appendix A — Minimal no-network proof slice

```text
SourceDescriptor(public-safe synthetic hydrology)
  -> RAW fixture metadata only
  -> PROCESSED HUC12 fixture
  -> EvidenceBundle
  -> LayerManifest
  -> StyleManifest
  -> TileArtifactManifest or GeoJSON fixture
  -> CatalogMatrix dry run
  -> PromotionReceipt dry run
  -> MapReleaseManifest dry run
  -> MapLibre click fixture
  -> EvidenceDrawerPayload
  -> FocusModeRequest
  -> MockAdapter response
  -> CitationValidationReport
  -> RuntimeResponseEnvelope
  -> AIReceipt + RunReceipt
  -> rollback target
```

Expected tests:

- ANSWER on valid public-safe fixture.
- ABSTAIN on missing EvidenceBundle.
- DENY on sensitive exact geometry.
- DENY on unknown rights.
- ERROR on policy engine unavailable.
- DENY release on missing rollback.
- DENY UI direct model call.
- DENY public raw path.

---

## 30. Appendix B — Recommended ADR queue

| ADR | Decision |
|---|---|
| ADR-0001 | Schema home and contracts/schema split. |
| ADR-0002 | Source ledger and authority register. |
| ADR-0003 | Lifecycle roots and release/proof/receipt homes. |
| ADR-0004 | Deterministic ID and hash policy. |
| ADR-0005 | EvidenceBundle and CitationValidationReport contract. |
| ADR-0006 | Policy engine and default-deny posture. |
| ADR-0007 | CatalogMatrix / STAC / DCAT / PROV closure. |
| ADR-0008 | MapLibre default 2D shell and renderer boundary. |
| ADR-0009 | PMTiles/COG/GeoParquet artifact policy. |
| ADR-0010 | AI ModelAdapter contract and MockAdapter-first rule. |
| ADR-0011 | Query-save-recompile control loop. |
| ADR-0012 | Sensitive geometry transform and withheld accounting. |
| ADR-0013 | Domain-lane packet standard. |
| ADR-0014 | Release, correction, withdrawal, rollback model. |
| ADR-0015 | Security threat model and response process. |

---

## 31. Appendix C — External reference links

Recheck before pinning versions or activating live integrations.

- NIST SP 800-218 SSDF: https://csrc.nist.gov/pubs/sp/800/218/final
- NIST SSDF project / revision information: https://csrc.nist.gov/projects/ssdf
- NIST AI RMF: https://www.nist.gov/itl/ai-risk-management-framework
- NIST SP 800-218A: https://csrc.nist.gov/news/2024/nist-publishes-sp-800-218a
- OWASP API Security Project: https://owasp.org/www-project-api-security/
- OWASP ASVS: https://owasp.org/www-project-application-security-verification-standard/
- PostGIS: https://postgis.net/
- MapLibre GL JS docs: https://www.maplibre.org/maplibre-gl-js/docs/
- MapLibre Style Spec: https://www.maplibre.org/maplibre-style-spec/
- PMTiles docs: https://docs.protomaps.com/pmtiles/
- GeoParquet 1.1: https://geoparquet.org/releases/v1.1.0/
- OGC STAC: https://www.ogc.org/standards/stac/
- W3C DCAT v3: https://www.w3.org/TR/vocab-dcat-3/
- W3C PROV-O: https://www.w3.org/TR/prov-o/
- OGC Cloud Optimized GeoTIFF: https://www.ogc.org/standards/ogc-cloud-optimized-geotiff/

---

## 32. Final build doctrine in one paragraph

Build KFM as a governed transformation system: sources become evidence, evidence becomes claims, claims become reviewed release candidates, release candidates become public-safe artifacts, artifacts become map/API/UI/AI experiences, and every step remains inspectable, policy-aware, reversible, and bounded by source authority. Any component that cannot show its evidence, policy posture, release state, correction path, and rollback target is not ready to speak as KFM.
