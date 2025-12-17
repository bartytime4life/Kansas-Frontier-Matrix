---
title: "Air Quality — Data Classification"
path: "data/air-quality/governance/DATA_CLASSIFICATION.md"
version: "v1.0.0"
last_updated: "2025-12-17"
status: "draft"
doc_kind: "Governance"
license: "CC-BY-4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
mcp_version: "MCP-DL v6.3"
ontology_protocol_version: "KFM-ONTO v4.1.0"
pipeline_contract_version: "KFM-PPC v11.0.0"
stac_profile: "KFM-STAC v11.0.0"
dcat_profile: "KFM-DCAT v11.0.0"
prov_profile: "KFM-PROV v11.0.0"

governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
sovereignty_policy: "docs/governance/SOVEREIGNTY.md"
fair_category: "FAIR+CARE"
care_label: "TBD"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:data:air-quality:governance:data-classification:v1.0.0"
semantic_document_id: "kfm-data-air-quality-data-classification-v1.0.0"
event_source_id: "ledger:kfm:doc:data:air-quality:governance:data-classification:v1.0.0"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "translate"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

# Air Quality — Data Classification

## 📘 Overview

### Purpose
- Define how **air-quality** domain artifacts are labeled for **sensitivity** and **classification**, and how those labels drive:
  - redaction/generalization requirements,
  - catalog + graph metadata handling,
  - API exposure rules,
  - Focus Mode / Story Node safe presentation.

### Scope
| In Scope | Out of Scope |
|---|---|
| Air-quality datasets and derived products (raw/work/processed), plus their STAC/DCAT/PROV metadata | Project-wide classification taxonomy definitions (owned by `docs/governance/*`) |
| Location privacy rules (e.g., when/where to blur/generalize coordinates) for air-quality artifacts | Identity/auth implementation details (owned by API/security architecture) |
| Classification propagation guidance (inputs → outputs) | Non–air-quality data domains |

### Audience
- Primary: Data engineers, catalog/metadata maintainers, governance reviewers for the air-quality domain
- Secondary: API implementers, Story Node authors/editors, UI maintainers

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **sensitivity**: content risk level; drives redaction/generalization and governance review
  - **classification**: access/distribution level; drives where/how data can be published or accessed
  - **raw/work/processed**: canonical data staging tiers used by KFM
  - **generalization**: reducing precision (esp. spatial resolution) to mitigate harm
  - **redaction**: removal/omission of fields (e.g., exact coordinates)
  - **H3 masking**: spatial generalization via H3 hex indexing (if used for sensitive-location handling)

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Air-quality governance index | `data/air-quality/governance/README.md` | Domain steward | Entry point for this domain’s governance docs |
| Root governance | `docs/governance/ROOT_GOVERNANCE.md` | Governance owners | Global rules override domain-local guidance |
| Sovereignty policy | `docs/governance/SOVEREIGNTY.md` | Governance owners | Defines “sensitive location” handling requirements |
| Security program docs | `SECURITY.md` + `docs/security/*` | Security owners | Includes CI gates / incident response expectations |
| Catalogs | `data/stac/` | Data platform | Domain STAC should encode access + redaction stance |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Classification taxonomy + decision flow is explicit and actionable
- [ ] Redaction/generalization rules are explicit (esp. spatial)
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated
- [ ] Version history entry added for changes

## 🗂️ Directory Layout

### This document
- `path`: `data/air-quality/governance/DATA_CLASSIFICATION.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Air-quality governance docs | `data/air-quality/governance/` | Domain governance docs (this file, README, etc.) |
| Raw staging | `data/raw/air-quality/` | Immutable source ingests (not publishable by default) |
| Work/staging | `data/work/air-quality/` | Intermediate transforms + QA artifacts (not publishable by default) |
| Processed/certified | `data/processed/air-quality/` | Certified outputs, publishable only if classification allows |
| STAC catalogs | `data/stac/air-quality/` | STAC Collections/Items for this domain |
| Schemas | `schemas/` | Telemetry + validation schemas (including governance signals) |
| Runs/logs | `mcp/runs/` or `mcp/experiments/` | Deterministic run logs, manifests, reproducibility artifacts |

### Expected file tree for this sub-area
~~~text
📦 data/
├── 📁 air-quality/
│   └── 📁 governance/
│       ├── 📄 README.md                  — Governance entrypoint (scope, owners, links)
│       └── 📄 DATA_CLASSIFICATION.md     — Sensitivity + classification rules (this doc)
├── 📁 raw/
│   └── 📁 air-quality/                   — Source ingests (immutable; not publishable by default)
├── 📁 work/
│   └── 📁 air-quality/                   — Staging + QA outputs (not publishable by default)
├── 📁 processed/
│   └── 📁 air-quality/                   — Certified outputs (publishable only if allowed)
└── 📁 stac/
    └── 📁 air-quality/                   — Domain STAC Collections/Items (may be redacted by class)
~~~

## 🧭 Context

### Background
- Air-quality data is often broadly public, but **privacy and sovereignty risks can arise** when:
  - data includes **private/community sensors** with precise locations,
  - outputs could enable **inference of sensitive locations** (even if not explicitly labeled),
  - datasets are merged with other layers to enable re-identification or pinpointing.

- KFM’s pipeline is ordered and non-negotiable:
  - ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → UI → Story Nodes → Focus Mode.
  - Classification is assigned early (ETL/work) and enforced throughout downstream surfaces.

### Assumptions
- Project-wide allowed values for `sensitivity` and `classification` are governed by `docs/governance/*`.
- This doc provides **domain-local guidance** and a **proposed mapping**; if root governance defines different labels or ordering, **root governance overrides**.

### Constraints / invariants
- **No direct graph access from the frontend**; classification enforcement happens at/behind APIs.
- **No automatic downgrades**: classification/sensitivity must never be reduced without explicit review.
- **Outputs must not be “less restricted” than any of their inputs** (propagation rule).
- Public outputs must not expose:
  - PII,
  - exact sensitive/private locations,
  - anything prohibited by sovereignty policy.

### Open questions
- What is the canonical project-wide taxonomy for `classification` beyond `open`?
- Are sensitive-but-discoverable datasets permitted to appear in public catalogs as **redacted metadata-only** entries?

### Future extensions
- Add automated classification propagation checks using PROV lineage + CI gates.
- Add a dedicated “redacted STAC” build step for public-facing catalogs.

## 🗺️ Diagrams

### System/dataflow diagram
~~~mermaid
flowchart LR
  A[Raw ingest<br/>data/raw/air-quality] --> B[Work / staging<br/>data/work/air-quality]
  B --> C[Processed / certified<br/>data/processed/air-quality]
  C --> D[Catalogs<br/>STAC/DCAT/PROV]
  D --> E[Graph<br/>Neo4j]
  E --> F[APIs]
  F --> G[UI]
  G --> H[Story Nodes]
  H --> I[Focus Mode]

  B -. "classification + redaction checks" .-> C
  C -. "catalog includes access tags" .-> D
  F -. "enforce access + generalization" .-> G
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant ETL as ETL/Validator
  participant Catalog as STAC/DCAT/PROV Builder
  participant API as API Layer
  participant UI as UI/Focus Mode

  ETL->>ETL: Assign sensitivity/classification (proposed rules)
  ETL->>ETL: Apply redaction/generalization (if required)
  ETL->>Catalog: Emit processed artifact + metadata + lineage refs
  Catalog->>API: Publish catalog pointers + access tags
  UI->>API: Request layer/data (with user context)
  API->>API: Filter + generalize per classification policy
  API-->>UI: Contracted payload + provenance refs + governance flags
~~~

## 📦 Data & Metadata

### Inputs
| Input type | Examples (non-exhaustive) | Typical risk | Default handling |
|---|---|---|---|
| Monitoring observations | time-series pollutant measurements (station/sensor) | Low → Medium | Label + validate; generalize if private sensor locations exist |
| Station/sensor metadata | locations, device/station properties | Medium | Treat location precision as sensitive until confirmed public |
| Gridded/raster products | interpolations, models, satellite-derived surfaces | Low → Medium | Ensure resolution is appropriate; avoid leaking restricted inputs |
| QA/ETL artifacts | logs, intermediate joins, diagnostics | Medium → High | Internal-only by default; never publish raw logs with identifiers |

### Outputs
| Output | Where produced | Where stored | Intended use |
|---|---|---|---|
| Certified observations | deterministic ETL from work → processed | `data/processed/air-quality/` | Analytics + maps + narrative evidence |
| Derived summary tables | aggregation (time/space) | `data/processed/air-quality/` | Public-safe trend reporting (if open) |
| Tiles/visual products | renderable map outputs | `data/processed/air-quality/` or `web/` (as governed) | UI layers (must follow access policy) |
| STAC/DCAT/PROV | catalog build stage | `data/stac/air-quality/` | Discovery + provenance + governance flags |

### Sensitivity & redaction

#### Two labels are used throughout KFM
- `sensitivity` (content-based; drives redaction + governance review)
- `classification` (access/distribution-based; drives publishing + API authorization)

> Note: The exact allowed values and ordering are governed globally. The tables below provide a **proposed** air-quality mapping to make this domain actionable.

#### Proposed ordering (for propagation checks)
- `sensitivity`: `public` < `sensitive` < `restricted`
- `classification`: `open` < `controlled` < `restricted` < `embargoed`

#### Classification matrix (domain guidance)
| Scenario | sensitivity | classification | Required action |
|---|---:|---:|---|
| Public agency monitoring stations (no private homes, no user IDs) | public | open (or controlled until reviewed) | OK to publish after validation + catalog build |
| Community/private sensors with precise coordinates | sensitive | controlled/restricted | Generalize coordinates (e.g., H3 / coarse region), or publish only aggregates |
| Any dataset containing PII (names, emails, phone numbers, addresses) | restricted | restricted/embargoed | Remove PII; require governance review before any downstream use |
| Intermediate ETL joins that could enable re-identification | sensitive/restricted | controlled/embargoed | Keep in `data/work/`; do not promote until redacted |
| Redacted public derivative created from restricted inputs | (inherits max input) | open only if proven safe | Must pass lineage + leakage checks; include governance notes |

#### Spatial handling rules (minimum)
- If a dataset includes **private or protected locations**:
  - do not publish exact coordinates in open outputs,
  - use **generalization** (e.g., coarse admin boundary or H3-based masking) and/or **redaction**.
- Do not “back-calculate” or infer sensitive locations from other fields (e.g., device IDs, uncommon timestamps).

#### Recommended metadata fields (proposed)
- In STAC Item/Collection `properties` (or equivalent governed field):
  - `sensitivity: <value>`
  - `classification: <value>`
  - `redaction: { applied: true|false, method: <name>, notes: <string> }`
  - `governance_review: { required: true|false, ticket: <id|TBD> }`

Example (illustrative only):
~~~yaml
properties:
  sensitivity: "sensitive"
  classification: "controlled"
  redaction:
    applied: true
    method: "h3_masking"
    notes: "Private/community sensor coordinates generalized."
~~~

### Quality signals
- Required minimum checks before promotion from `work` → `processed`:
  - schema compliance (required fields present),
  - CRS/geometry validity where applicable,
  - time range + sampling interval sanity checks,
  - governance scan: PII + sensitive-location leakage,
  - checksums recorded for produced artifacts.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Every processed air-quality artifact intended for discovery must be represented as STAC:
  - Collection(s) per product family (observations, rasters, tiles)
  - Item(s) per file/asset granule
- Classification must be carried into STAC metadata so downstream systems can enforce policy.

### DCAT
- DCAT records should reflect access level using standard fields where possible (e.g., access rights).
- If public catalogs are produced, restricted datasets may require:
  - metadata-only entries, or
  - omission from public catalogs (TBD per root governance).

### PROV-O
- Provenance must record:
  - which inputs were used,
  - which transformations were applied,
  - when/where redaction/generalization occurred.
- Classification propagation rule:
  - outputs must not have “lower restriction” than any input used to generate them.

### Versioning
- Air-quality datasets should use governed versioning practices (STAC versioning and/or dataset semantic IDs).
- If an item changes classification (e.g., post-review), treat as:
  - a new version with explicit provenance (`prov:wasRevisionOf`) and review notes.

## 🧱 Architecture

### Components
| Component | Responsibility | Enforcement point for classification |
|---|---|---|
| ETL ingest | Acquire + normalize source data | Assign initial labels; default to more restrictive when unsure |
| Work/staging | Intermediate transforms + QA | Run governance scans; block promotion if violations |
| Processed | Certified outputs | Only store publishable artifacts here after passing checks |
| Catalog builder | STAC/DCAT/PROV emission | Encode labels; optionally build redacted public catalogs |
| Graph ingest | Neo4j load | Store labels on nodes/edges for query-time filtering (via APIs) |
| API layer | Serve data to UI/clients | Authorize + redact/generalize responses by classification |
| UI / Focus Mode | Present layers + narratives | Display governance flags; avoid exposing sensitive locations |

### Interfaces / contracts
- Graph interfaces are not consumed directly by UI; APIs provide:
  - contract-stable payloads,
  - redaction/generalization behavior,
  - provenance pointers for evidence.

### Extension points checklist
- [ ] New air-quality dataset introduced → classification assigned at ingest + recorded in catalogs
- [ ] Any dataset with sensitive location risk → redaction/generalization applied before public use
- [ ] CI gates include sovereignty + leakage scans before merge/release

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Story Nodes / Focus Mode
- Story Nodes must reference:
  - dataset IDs,
  - time ranges,
  - provenance pointers to STAC/DCAT/PROV metadata.
- Focus Mode should:
  - show audit/governance flags when redaction/generalization is applied,
  - avoid rendering exact sensitive coordinates (even if present internally).

### Provenance-linked narrative rule
- Any narrative claim derived from air-quality data must be traceable to:
  - a STAC Item/Collection (or equivalent catalog entity),
  - and a PROV Activity describing derivation.
- If a claim requires restricted inputs, the Story Node inherits that classification and cannot be published as open.

### Optional structured controls (examples)
~~~yaml
focus_layers:
  - "air_quality_observations"
  - "air_quality_surfaces"
focus_time: "TBD"
focus_center: [ "TBD_LON", "TBD_LAT" ]
governance:
  allow_public_render: true
  location_precision: "coarse"   # e.g., coarse | exact (exact requires review)
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Confirm every new artifact has:
  - `sensitivity` + `classification` labels in metadata,
  - provenance pointers to inputs + transforms.
- [ ] Run sovereignty/privacy scans:
  - verify no PII,
  - verify no exact sensitive coordinates in public outputs.
- [ ] Validate STAC/DCAT/PROV outputs against project profiles.
- [ ] Verify classification propagation:
  - no output is “less restricted” than any input in its lineage.

### Reproduction (deterministic)
- Run ETL with pinned configs and record:
  - inputs (hashes),
  - parameters,
  - outputs (hashes),
  - redaction/generalization steps applied.

# Example placeholders — replace with repo-specific commands
~~~bash
# Validate catalogs (replace with actual tooling)
# python tools/validate_stac.py data/stac/air-quality
# python tools/validate_dcat.py data/stac/air-quality
# python tools/validate_prov.py data/stac/air-quality

# Governance scans (replace with actual tooling)
# python tools/scan_pii.py data/work/air-quality
# python tools/scan_sensitive_locations.py data/processed/air-quality

# Produce integrity hashes (replace with actual tooling)
# python tools/hash_manifest.py data/processed/air-quality > mcp/runs/<run_id>/manifest.sha256
~~~

### Telemetry signals (recommended)
- `classification_assigned` (dataset_id, sensitivity, classification)
- `redaction_applied` (method, fields_removed, geometry_generalization)
- `promotion_blocked` (reason, scan_results_ref)
- `catalog_published` (public|internal, counts, validation_status)
- `focus_mode_redaction_notice_shown` (layer_id, redaction_method)

## ⚖ FAIR+CARE & Governance

### Review gates
- Governance review is required when:
  - introducing a new air-quality dataset source,
  - changing an artifact’s classification/sensitivity,
  - publishing any dataset derived from sensitive/restricted inputs,
  - adding a new UI layer that could reveal sensitive locations by interaction/zoom.

### CARE considerations
- If air-quality data is community-provided or intersects with sensitive locations:
  - ensure authority-to-control expectations are respected (per sovereignty policy),
  - prefer coarse/aggregate public products,
  - document decisions in metadata and governance notes.

### AI usage constraints
- Allowed:
  - summarization, structure extraction, translation, keyword indexing.
- Prohibited:
  - generating new policy,
  - inferring sensitive locations (directly or indirectly).
- AI may propose classifications, but **human review** must approve any final labels, especially downgrades.

## 🕰️ Version History

| Version | Date | Change summary | Author | PR / Issue |
|---|---:|---|---|---|
| v1.0.0 | 2025-12-17 | Initial air-quality data classification + redaction guidance | TBD | TBD |

---

## Footer refs (do not remove)
- Master guide: `docs/MASTER_GUIDE_v12.md`
- Template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Ethics: `docs/governance/ETHICS.md`
---
