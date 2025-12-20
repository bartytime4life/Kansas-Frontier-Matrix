---
title: "🗺️ KFM — STAC Authoring & Integrity Pattern (Collections · Items · Assets · Validation)"
path: "docs/patterns/stac/README.md"
version: "v12.0.0-draft"
last_updated: "2025-12-20"
status: "active"
doc_kind: "Pattern"
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
care_label: "Public · Low-Risk"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:patterns:stac:authoring-integrity:v12.0.0-draft"
semantic_document_id: "kfm-pattern-stac-authoring-integrity-v12.0.0-draft"
event_source_id: "ledger:kfm:doc:patterns:stac:authoring-integrity:v12.0.0-draft"
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

# 🗺️ KFM — STAC Authoring & Integrity Pattern (Collections · Items · Assets · Validation)

## 📘 Overview

### Purpose
This pattern standardizes how KFM **authors, validates, and publishes STAC** so that:
- catalogs are **deterministic** (stable IDs, stable links, stable structure),
- catalogs are **reliable** (schema-valid, link-valid, consistent extents),
- catalogs are **governable** (clear license/access signals, provenance links),
- downstream systems (Graph, APIs, UI, Story Nodes) can depend on STAC without special-case logic.

### Scope

| In Scope | Out of Scope |
|---|---|
| Static STAC artifacts (Collections, Items, Assets, Links) | Defining STAC API endpoints or server behavior (belongs to API Contract docs) |
| Integrity invariants (IDs, link relations, extent coherence) | Dataset-specific content rules (belongs to dataset docs / QA patterns) |
| Validation checklist + CI gates for STAC correctness | Frontend reading STAC directly from object storage (UI must use APIs) |
| How STAC connects to DCAT and PROV for auditability | Replacing the KFM pipeline ordering or governance process |

### Audience
- Primary: ETL and Catalog maintainers, Data‑Ops / Reliability
- Secondary: API maintainers, UI/Story maintainers, Governance reviewers

### Definitions (link to glossary)
- Link: `docs/glossary.md` *(not confirmed in repo)*
- Terms used in this doc:
  - **STAC Collection**: a grouped dataset description with extents and metadata.
  - **STAC Item**: an individual spatiotemporal record referencing one or more assets.
  - **Asset**: a file (data/metadata/QA/provenance) referenced by an Item.
  - **Integrity**: the item/collection/link invariants that make catalogs navigable and safe.

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Patterns index | `docs/patterns/README.md` | platform@kfm.local | Entry point |
| Change detection pattern | `docs/patterns/change-detection/README.md` | data-ops@kfm.local | Idempotent updates often produce STAC deltas |
| Idempotent handler pattern | `docs/patterns/change-detection/idempotent-handler/README.md` | data-ops@kfm.local | Computes strong digests and promotes artifacts |
| STAC outputs | `data/stac/` | data-ops@kfm.local | Collections + Items outputs |
| DCAT outputs | `data/catalog/dcat/` | data-ops@kfm.local | Dataset + distribution metadata |
| PROV outputs | `data/prov/` | data-ops@kfm.local | Provenance bundles |
| STAC profile doc | `docs/standards/stac/README.md` *(not confirmed in repo)* | governance | Where KFM-specific STAC rules should be codified |

### Definition of done (for this pattern)
- [ ] Catalog structure and naming guidance is deterministic
- [ ] Collection/Item integrity invariants are explicit and testable
- [ ] Asset conventions include checksums + provenance links (where applicable)
- [ ] Validation & CI gates are listed and repeatable
- [ ] Story Node / Focus Mode integration guidance preserves API boundary
- [ ] Mermaid diagrams render (avoid `|` in node labels; avoid `:::class` styling)

---

## 🗂️ Directory Layout

### This document
- `path`: `docs/patterns/stac/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| STAC outputs | `data/stac/` | Collections + Items for published layers |
| STAC collections | `data/stac/collections/` | One folder per collection (recommended) |
| STAC items | `data/stac/items/` | Items partitioned by collection (recommended) |
| DCAT outputs | `data/catalog/dcat/` | DCAT datasets + distributions |
| PROV outputs | `data/prov/` | PROV bundles for runs and artifacts |
| Builders | `src/pipelines/catalog/` *(not confirmed in repo)* | Code that writes STAC/DCAT |
| Validators | `tools/` or `src/.../validate` *(not confirmed in repo)* | Schema + link checks |
| Run artifacts | `mcp/runs/` | Validation reports, link-check reports |

### Expected file tree (recommended)
~~~text
📁 docs/
└── 📁 patterns/
    └── 📁 stac/
        └── 📄 README.md

📁 data/
└── 📁 stac/
    ├── 📁 collections/
    │   └── 📁 <collection-id>/
    │       └── 📄 collection.json
    └── 📁 items/
        └── 📁 <collection-id>/
            └── 📄 <item-id>.json

📁 data/
├── 📁 catalog/
│   └── 📁 dcat/
└── 📁 prov/
~~~

---

## 🧭 Context

### Background
STAC is the primary **catalog surface** that connects KFM’s ETL outputs to:
- catalog validation and governance review,
- graph ingestion (via ETL loaders),
- API responses used by UI/Story Nodes,
- provenance and reproducibility.

Without strict STAC integrity:
- “freshness” becomes untrustworthy,
- broken links silently degrade UI layers,
- collection extents drift and become misleading,
- versioning becomes inconsistent.

### Assumptions
- STAC artifacts are generated by ETL/catalog writers, not edited by hand.
- KFM prefers **stable identifiers** and **idempotent publishing** (duplicate runs converge).
- UI consumes STAC-derived views through APIs (no direct object-store reads).

### Constraints / invariants
- Canonical pipeline ordering is preserved:
  - ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode
- Frontend does not read Neo4j directly (API boundary).
- Every STAC Item must be attributable to a provenance record (directly or indirectly).

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Where is the authoritative KFM STAC profile documented and versioned? | Governance | TBD |
| Do we publish a root STAC Catalog document (catalog.json) or only collections/items? | Data‑Ops | TBD |
| What is the official checksum field convention (properties vs asset fields)? | Data‑Ops | TBD |

### Future extensions
- Add a governed “KFM STAC Profile” doc under `docs/standards/stac/`.
- Add CI checks for: STAC schema validation, link integrity, extent coherence, and broken-link prevention.
- Add a catalog delta format for update-only publishing (pairs well with idempotent handler pattern).

---

## 🗺️ Diagrams

### STAC in the KFM flow (high level)
~~~mermaid
flowchart LR
  ETL["ETL (ingest, normalize)"] --> CAT["Catalog Writer"]
  CAT --> STAC["STAC (Collections, Items)"]
  CAT --> DCAT["DCAT (datasets, distributions)"]
  CAT --> PROV["PROV (lineage bundles)"]

  STAC --> GRAPH["Neo4j Graph Load"]
  DCAT --> GRAPH
  PROV --> GRAPH

  GRAPH --> API["APIs"]
  API --> UI["React, Map UI"]
  UI --> STORY["Story Nodes"]
  STORY --> FOCUS["Focus Mode"]
~~~

### Item integrity loop (validation gates)
~~~mermaid
flowchart TD
  W["Writer emits Collection and Items"] --> V1["Schema validate (STAC core + extensions)"]
  V1 --> V2["Integrity validate (collection, links, assets)"]
  V2 --> V3["Link check (href resolvable)"]
  V3 --> V4["Extent check (bbox and time coherence)"]
  V4 --> PASS["Publish / Promote"]
  V2 --> FAIL["Fail build (block promotion)"]
  V3 --> FAIL
  V4 --> FAIL
~~~

---

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| STAC Collection source metadata | YAML/JSON/config | ETL config | Schema + required fields |
| STAC Item source records | tabular/geo | ETL outputs | Deterministic transforms |
| Assets | files | object store / filesystem | checksum + media type checks |
| Provenance references | JSON-LD | PROV emitter | reference integrity |

### Outputs
| Output | Format | Path | Contract |
|---|---|---|---|
| Collection | JSON | `data/stac/collections/<collection-id>/collection.json` | STAC Collection |
| Item | JSON | `data/stac/items/<collection-id>/<item-id>.json` | STAC Item |
| Validation report | JSON/MD | `mcp/runs/<run-id>/...` | Internal |
| Provenance bundle | JSON-LD | `data/prov/<run-id>/prov.jsonld` | PROV-O |

### Sensitivity & redaction
- Do not embed secrets or internal-only endpoints in STAC `href` fields.
- For restricted datasets (including Indigenous data protections), ensure:
  - Item fields do not reveal sensitive coordinates beyond allowed resolution,
  - assets are access-controlled and links are mediated via APIs as needed.

### Quality signals
- Catalog completeness: % Items with valid geometry/bbox/time
- Link integrity: broken link count = 0 at publish time
- Checksum coverage: % assets with sha256 attached (where policy requires)
- Extent coherence: collection extent matches union of item extents (within policy)

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC invariants (MUST for KFM catalogs)
1. **Stable IDs**
   - Collection `id` and Item `id` must be stable across re-runs for the same logical object.
2. **Collection reference coherence**
   - Item must specify the correct `collection` value (matching a Collection `id`).
3. **Spatial and temporal fields**
   - Item must include `geometry` and `bbox` for spatial datasets (or explicitly documented exceptions).
   - Item must include `datetime` OR `start_datetime` and `end_datetime`.
4. **Asset minimums**
   - Every data-bearing Item must include at least one asset with `href` and appropriate `type`.
5. **Link minimums**
   - Collection and Item should include consistent `self` and parent/root navigation links (strategy must be documented).

> Note: “MUST” here means “required by KFM pattern intent.” The authoritative enforcement should live in a KFM STAC profile doc (not confirmed in repo).

### Recommended asset conventions (SHOULD)
- Roles: `data`, `metadata`, `thumbnail`, `provenance`, `qa`
- Include checksums where required by policy:
  - Prefer sha256 computed during ETL promotion (see idempotent handler pattern).
- Include provenance as an asset or a link:
  - `assets.provenance.href` points to a PROV bundle
  - optional `assets.openlineage.href` if OpenLineage is used

### DCAT mapping (SHOULD)
- A STAC Collection typically maps to a DCAT dataset.
- Assets or published artifacts map to DCAT distributions.
- Checksums and media types should be consistent between STAC assets and DCAT distributions.

### PROV mapping (MUST minimum lineage)
- Each published Collection/Item should be traceable to:
  - a `prov:Activity` (the run),
  - input entities used to generate Items,
  - output entities (published artifacts).

---

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| Catalog writer | Build Collection + Items deterministically | ETL output → STAC JSON |
| Validator | Schema + integrity + link checks | CLI/tool or pipeline step |
| Promotion step | Publish only on pass | gate based on reports |
| API layer | Serve catalog + derived views | REST/GraphQL |
| UI | Render layers and update badges | API only |

### Deterministic ID strategy (recommended)
Pick one deterministic strategy per dataset family:
- Stable upstream identifier (best), plus optional version key
- Or content-addressed digest (sha256) for immutable artifacts

Guidelines:
- Avoid timestamps as primary IDs.
- If Item IDs incorporate versioning, ensure predecessor/successor is represented consistently (via links or properties).

### Minimal examples (illustrative)

#### Collection skeleton
~~~json
{
  "type": "Collection",
  "stac_version": "1.0.0",
  "id": "<collection-id>",
  "description": "…",
  "license": "…",
  "extent": {
    "spatial": { "bbox": [[-180, -90, 180, 90]] },
    "temporal": { "interval": [["2020-01-01T00:00:00Z", null]] }
  },
  "links": [],
  "summaries": {}
}
~~~

#### Item skeleton
~~~json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "<item-id>",
  "collection": "<collection-id>",
  "geometry": null,
  "bbox": [-180, -90, 180, 90],
  "properties": {
    "datetime": "2025-12-20T00:00:00Z"
  },
  "links": [],
  "assets": {
    "data": {
      "href": "s3://.../asset.ext",
      "type": "application/octet-stream",
      "roles": ["data"]
    }
  }
}
~~~

---

## 🧠 Story Node & Focus Mode Integration

### Goal
Story Nodes and Focus Mode should be able to:
- cite a stable Collection/Item ID,
- show “Updated on …” with evidence (catalog timestamps + provenance refs),
- avoid silent changes (versioning and provenance links make changes auditable).

### UI contract (MUST)
- UI must not read STAC directly from object storage unless explicitly governed.
- UI consumes catalog views through APIs that:
  - resolve access rules,
  - apply redaction/masking rules,
  - provide provenance references.

### Recommended API-facing fields derived from STAC (SHOULD)
- `collection_id`
- `item_id`
- `updated_at` (from STAC properties or catalog writer metadata)
- `checksum_sha256` (where policy requires)
- `prov_ref` (link to PROV bundle)
- `qa_summary` (non-sensitive)

---

## 🧪 Validation & CI/CD

### Validation checklist (recommended)
1. **Schema validity**
   - Collection and Item conform to STAC 1.0 core (and any approved extensions).
2. **Item/Collection integrity**
   - Item `collection` matches an existing Collection ID.
3. **Link integrity**
   - `href` values resolve in the intended environment (API resolvers or absolute URLs).
4. **Extent coherence**
   - Item bbox consistent with geometry.
   - Collection extent consistent with Items (policy-defined tolerance).
5. **Asset sanity**
   - Assets have `href`, `type`, and reasonable roles.
   - Checksums present when required.
6. **Governance gates**
   - License, access constraints, sovereignty requirements are reflected and enforced.

### CI outputs to persist (recommended)
- `mcp/runs/catalog/<run-id>/stac_validation.json`
- `mcp/runs/catalog/<run-id>/link_check.json`
- `mcp/runs/catalog/<run-id>/extent_check.json`
- `mcp/runs/catalog/<run-id>/summary.md`

---

## ⚖ FAIR+CARE & Governance

- **FAIR**
  - Findable: stable IDs and catalogs
  - Accessible: access constraints explicit; APIs enforce them
  - Interoperable: STAC/DCAT/PROV mappings documented
  - Reusable: provenance and QA links available

- **CARE / sovereignty**
  - Ensure restricted datasets are redacted appropriately in catalog exposure.
  - Avoid exposing sensitive coordinates or identifiers via public STAC fields.

- **Security**
  - No secrets in `href` or embedded metadata.
  - Link resolution must not leak internal topology.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---:|---|---|
| v12.0.0-draft | 2025-12-20 | Created STAC authoring/integrity pattern and validation gates; aligned to Universal v12 formatting | <name/handle> |

---

<div align="center">

**Navigation**  
[⬅️ Patterns Index](../README.md) ·
[🔔 Change Detection](../change-detection/README.md) ·
[✅ Idempotent Handler](../change-detection/idempotent-handler/README.md)

© 2025 Kansas Frontier Matrix — CC‑BY‑4.0

</div>
