---
path: data/graph/README.md
status: active
owner: graph-maintainers
last_updated: 2026-01-08
---

<div align="center">

# 🕸️ KFM `data/graph/` — Graph Import Artifacts (Neo4j)

![KFM](https://img.shields.io/badge/KFM-Kansas%20Frontier%20Matrix-222222)
![Graph](https://img.shields.io/badge/graph-Neo4j%20(Property%20Graph)-4C8EDA)
![Artifacts](https://img.shields.io/badge/artifacts-CSV%20%7C%20Cypher-0B7285)
![Provenance](https://img.shields.io/badge/provenance-STAC%20%7C%20DCAT%20%7C%20PROV-6F42C1)
![Governed](https://img.shields.io/badge/governed-API%20boundary%20enforced-black)

**A governed home for graph import artifacts** that build and evolve the **KFM knowledge graph** — with **round‑trip traceability** back to **STAC/DCAT/PROV**.

</div>

---

## 🧭 Non‑negotiable system order (KFM invariant)

> **ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

**If the graph can’t point back to catalogs + lineage, it doesn’t ship.** ✅

---

## ⚡ Quick links (jump points)

- 🛰️ STAC (assets) → `data/stac/`
- 🗂️ DCAT (discoverability) → `data/catalog/dcat/`
- 🧬 PROV (lineage) → `data/prov/`
- 🧠 Graph ingest code (target) → `src/graph/`
- 🔌 API boundary (target) → `src/server/` (or your actual API folder)
- 🗺️ UI (never reads Neo4j directly) → `web/`
- 🎬 Story Nodes (governed narrative) → `docs/reports/story_nodes/` *(if present)*

---

## 📌 Table of contents

- [📘 Overview](#-overview)
- [🗂️ What belongs here (and what doesn’t)](#️-what-belongs-here-and-what-doesnt)
- [📁 Directory layout (target shape)](#-directory-layout-target-shape)
- [🧾 The “Graph Traceability Contract”】【#-the-graph-traceability-contract](#-the-graph-traceability-contract)
- [🏷️ IDs, labels, and ontology guardrails](#️-ids-labels-and-ontology-guardrails)
- [📦 Import artifact specs (CSV)](#-import-artifact-specs-csv)
- [🧩 Post‑import scripts (Cypher)](#-post-import-scripts-cypher)
- [🧪 Validation & CI gates](#-validation--ci-gates)
- [🔐 Governance, privacy, and sensitive locations](#-governance-privacy-and-sensitive-locations)
- [⚙️ Performance notes (keep graph queries fast)](#️-performance-notes-keep-graph-queries-fast)
- [📚 Reference shelf (project library)](#-reference-shelf-project-library)
- [🕰️ Version history](#️-version-history)

---

## 📘 Overview

### Purpose 🎯
`data/graph/` exists so graph imports are:

- ✅ **reviewable** (diffable artifacts, no opaque binary dumps)
- ✅ **reproducible** (generated from deterministic ETL + catalogs)
- ✅ **traceable** (pointers back to STAC/DCAT + PROV lineage)
- ✅ **governed** (UI access only through the API boundary)

### Audience 👥
- 🧑‍🔬 Data/graph contributors producing imports for new domains
- 🧠 Ontology maintainers reviewing labels/relationship changes
- 🔌 API + Story maintainers validating provenance behavior

---

## 🗂️ What belongs here (and what doesn’t)

### ✅ In scope
- 📄 **Graph import CSV exports** (bulk-friendly, deterministic)
- 🧾 **Small, reviewable fixtures** to power tests/examples
- 🧩 **Optional post‑import Cypher scripts** (idempotent, scoped)
- 🔗 **Evidence + lineage pointers** (STAC/DCAT/PROV IDs)

### ❌ Out of scope
- 🗃️ Full Neo4j database store files (deployment concern)
- 🔐 Secrets, credentials, connection strings, operational configs
- 📥 Raw domain source snapshots (belongs in `data/<domain>/raw/`)
- 🧑‍🎨 UI code or direct UI → Neo4j access patterns (blocked by design)

> [!IMPORTANT]
> **This folder stores “import artifacts”, not “truth”.**  
> Truth lives in **STAC/DCAT/PROV + processed domain outputs**. The graph stores **pointers + relationships**.

---

## 📁 Directory layout (target shape)

```text
📦 data/
└─ 🕸️ graph/
   ├─ 📄 README.md
   ├─ 📁 csv/
   │  ├─ 📄 nodes__<Label>__<domain>__<yyyymmdd>.csv
   │  ├─ 📄 rels__<TYPE>__<domain>__<yyyymmdd>.csv
   │  └─ 📄 fixtures__tiny__<purpose>.csv
   ├─ 📁 cypher/
   │  ├─ 📄 constraints__<yyyymmdd>.cypher
   │  ├─ 📄 post_import__<domain>__<purpose>__<yyyymmdd>.cypher
   │  └─ 📄 migrations__<semver>.cypher
   └─ 📁 docs/
      ├─ 📄 ontology.md
      └─ 📄 mapping_rules.md
```

> [!TIP]
> If `data/graph/docs/` doesn’t exist yet, create it. Having **ontology + mapping rules** near the artifacts reduces drift. 🧲

---

## 🧾 The “Graph Traceability Contract”

Graph content must never become an orphaned “fact bucket”. Every node/edge created from data must carry **evidence pointers** and (when applicable) **lineage pointers**.

### ✅ Required pointer fields (minimum viable)
For **every** node/edge row, include one or more:

- `evidence_stac_id` → STAC Item/Collection identifier (preferred for spatial assets)
- `evidence_dcat_id` → DCAT Dataset identifier (preferred for discovery-level linking)
- `prov_activity_id` → PROV activity (how it was generated)
- `prov_entity_id` → PROV entity (what artifact/run output it came from)

> [!NOTE]
> Don’t store big geometries, rasters, or documents inside Neo4j.  
> Store **IDs + small summaries** → let STAC/DCAT/PROV remain canonical. 🧾

### 🧠 Why this exists
- 🧾 **Auditability:** “Where did this claim come from?”
- ♻️ **Reproducibility:** “Can we rebuild it and compare outputs?”
- 🛡️ **Governance:** “Can we enforce redaction/classification consistently?”

---

## 🏷️ IDs, labels, and ontology guardrails

### 1) Stable IDs (don’t make joins sad) 😅
Use a stable, global identifier for nodes and relationships.

**Recommended pattern**
```text
kfm:<kind>:<namespace>:<slug_or_id>[:v<version>]

# examples
kfm:place:us-ks:topeka
kfm:dataset:kfm.ks.transport.railroads.1870_1910.v1
kfm:doc:khs:map_1878_plate12
kfm:event:us-ks:1874_grasshopper_outbreak
```

**Rules**
- ✅ Stable across rebuilds when referring to the “same conceptual thing”
- ✅ Version only when semantics change (not just a re-run)
- ❌ Don’t use auto-increment IDs from Neo4j exports as “identity”

### 2) Label and relationship governance 🧱
Keep labels + relationship types **boring and consistent**:

**Suggested core labels**
- `Place`, `Person`, `Org`, `Event`, `Document`, `Dataset`, `Asset`, `Run`, `Claim`

**Suggested core relationship types**
- `LOCATED_IN`, `OCCURRED_AT`, `MENTIONS`, `CITES`, `DERIVED_FROM`, `PUBLISHED_AS`, `HAS_ASSET`

> [!IMPORTANT]
> If you add/rename labels or relationship types, treat it like a schema change:
> - update `data/graph/docs/ontology.md`
> - add a migration plan (`data/graph/cypher/migrations__*.cypher`)
> - coordinate API contract updates (graph changes are downstream-visible)

### 3) Time + space semantics (KFM-friendly) 🧭🕰️
- Store time as **ISO 8601** strings (`start`, `end`, `at`) and timezone if relevant
- For spatial footprint, prefer:
  - `bbox_wgs84` (safe summary) ✅
  - `geom_hash` (integrity/compare) ✅
  - **Do not** store precise sensitive coordinates when restricted ❌

---

## 📦 Import artifact specs (CSV)

### ✅ CSV standards (minimum)
- UTF‑8
- header row required
- explicit columns (no “mystery” extra fields)
- deterministic ordering (sort by `kfm_id`)

### 🧱 Node CSV: recommended columns
| Column | Required | Meaning |
|---|:---:|---|
| `kfm_id` | ✅ | stable node ID |
| `label` | ✅ | Neo4j label (single) or `labels` (multi) |
| `name` | ✅ | display name |
| `description` | ⚠️ | short summary (don’t paste full docs) |
| `classification` | ✅ | `public/internal/confidential/restricted` |
| `valid_from` / `valid_to` | ⚠️ | temporal validity (ISO 8601) |
| `bbox_wgs84` | ⚠️ | `minLon,minLat,maxLon,maxLat` |
| `evidence_stac_id` | ✅* | STAC pointer (or DCAT pointer) |
| `evidence_dcat_id` | ✅* | DCAT pointer (or STAC pointer) |
| `prov_activity_id` | ⚠️ | PROV activity pointer |
| `prov_entity_id` | ⚠️ | PROV entity pointer |

\*At least one of `evidence_stac_id` or `evidence_dcat_id` is required.

**Example: `nodes__Place__kansas__20260108.csv`**
```csv
kfm_id,label,name,description,classification,bbox_wgs84,evidence_dcat_id,evidence_stac_id,prov_activity_id
kfm:place:us-ks:topeka,Place,Topeka,"Capital city of Kansas.",public,"-95.78,38.95,-95.63,39.10",kfm:dataset/kfm.ks.admin.places.v1,,prov:activity/run_2026_01_08_01
```

### 🧲 Relationship CSV: recommended columns
| Column | Required | Meaning |
|---|:---:|---|
| `src_id` | ✅ | `kfm_id` of start node |
| `rel_type` | ✅ | relationship type |
| `dst_id` | ✅ | `kfm_id` of end node |
| `weight` | ⚠️ | optional numeric weight |
| `confidence` | ⚠️ | `0..1` (or `low/med/high`) |
| `evidence_*` | ✅ | evidence pointer(s) |
| `prov_*` | ⚠️ | lineage pointer(s) |

**Example: `rels__LOCATED_IN__kansas__20260108.csv`**
```csv
src_id,rel_type,dst_id,confidence,evidence_dcat_id,prov_activity_id
kfm:place:us-ks:topeka,LOCATED_IN,kfm:place:us-ks:kansas,0.99,kfm:dataset/kfm.ks.admin.places.v1,prov:activity/run_2026_01_08_01
```

> [!CAUTION]
> If a relationship represents a *claim* (not a hard fact), model it explicitly:
> - create a `Claim` node
> - connect it with `CITES` + `MENTIONS`
> - store confidence + evidence pointers
>
> This keeps “fact vs interpretation” clean for Story Nodes and Focus Mode. 🎬🧠

---

## 🧩 Post‑import scripts (Cypher)

Use Cypher scripts for:
- ✅ constraints/indexes
- ✅ post-import linking
- ✅ idempotent fixes (`MERGE`, not blind `CREATE`)
- ✅ migrations with explicit scope

### ✅ Idempotency patterns (recommended)
```cypher
// Constraints (safe re-run)
CREATE CONSTRAINT kfm_id_unique IF NOT EXISTS
FOR (n) REQUIRE n.kfm_id IS UNIQUE;

// Safe upsert
MERGE (p:Place {kfm_id: $kfm_id})
SET p.name = $name,
    p.classification = $classification;
```

### ❌ Avoid
- global rewrites without a `WHERE` scope
- scripts that assume an empty database
- embedding credentials/endpoints

> [!TIP]
> Keep Cypher small and purposeful. Big rewrites belong in controlled migrations with backups and review. 🧯

---

## 🧪 Validation & CI gates

### ✅ Minimum checks for PRs touching `data/graph/**`
- [ ] CSV UTF‑8 + headers present
- [ ] `kfm_id` non-null and unique per label file
- [ ] relationships reference existing node IDs (referential integrity)
- [ ] at least one evidence pointer present per row (`evidence_stac_id` or `evidence_dcat_id`)
- [ ] pointer targets exist in `data/stac/**` and/or `data/catalog/dcat/**`
- [ ] PROV pointers resolve to `data/prov/**` when used
- [ ] `classification` present and valid values only
- [ ] no restricted/sensitive precision accidentally introduced

### 🧪 Integration testing (recommended)
Spin up Neo4j in CI for a **tiny fixture ingest**:
- import a small set of nodes/rels
- run constraint checks
- run a “golden queries” suite (API-like query patterns)

> [!NOTE]
> “Graph staged in CI” is a feature, not a luxury — it prevents ontology drift and broken joins from reaching the API. 🧪✅

---

## 🔐 Governance, privacy, and sensitive locations

### 🧭 Classification carries through
If an artifact is `confidential` or `restricted`:
- do not publish raw coordinates into public graph exports
- enforce access controls **at the API boundary**
- prefer generalized geometry summaries (`bbox_wgs84`, grid cell ids)

### 🚫 Never commit
- secrets, tokens, passwords, `.env` files
- internal service URLs not intended to be public
- personal data (PII), unless explicitly governed + approved

> [!IMPORTANT]
> KFM is “mostly open”, but **not everything should be public at full resolution**. Protect sensitive places and communities first. ❤️🧭

---

## ⚙️ Performance notes (keep graph queries fast)

Graph is for **relationships + discovery**, not heavy analytics.

### Practical guidelines ✅
- index/constraint `kfm_id`
- keep API queries bounded (limit depth, paginate)
- avoid “mega traversals” from the UI
- cache common API results for Story Nodes/Explore Mode

### Scaling mindset 🔭
If you need:
- centrality/pathfinding at scale
- temporal snapshots
- heavy analytics

…prefer running it in **pipelines** and publishing results as **datasets** (STAC/DCAT/PROV), then link the outputs back into the graph. 🧰➡️🗂️➡️🕸️

---

## 📚 Reference shelf (project library)

> These references shape how we treat the graph as a **governed semantic layer** (performance, provenance, safety, and reproducibility).  
> ⚠️ Library files may have different licenses than repo code — keep them in `docs/library/` (or outside the repo) and respect upstream terms.

<details>
<summary><strong>🕸️ Graph + data spaces + query engines</strong></summary>

- `docs/library/Data Spaces.pdf`
- `docs/library/Scalable Data Management for Future Hardware.pdf`
- `docs/library/PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf`

</details>

<details>
<summary><strong>🧾 Modeling rigor (helps prevent “graph vibes”)</strong></summary>

- `docs/library/Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf`
- `docs/library/Understanding Statistics & Experimental Design.pdf`
- `docs/library/regression-analysis-with-python.pdf`
- `docs/library/think-bayes-bayesian-statistics-in-python.pdf`

</details>

<details>
<summary><strong>🔐 Security mindset (defensive use only)</strong></summary>

- `docs/library/ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf`
- `docs/library/Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf`

</details>

<details>
<summary><strong>🧱 KFM canonical docs</strong></summary>

- `docs/specs/Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.docx`
- `docs/specs/MARKDOWN_GUIDE_v13.md` *(or equivalent export path)*

</details>

---

## 🕰️ Version history

| Version | Date | Change | Author |
|---|---:|---|---|
| v1.0.0 | 2025-12-26 | Initial `data/graph/README.md` | TBD |
| v1.1.0 | 2026-01-08 | Tighten traceability contract, CSV/Cypher specs, CI gates, governance | KFM Maintainers |

---

### ✅ Footer (keep)
- Pipeline invariant: **ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**
- Canonical pointers: `data/stac/` · `data/catalog/dcat/` · `data/prov/`
- Graph ingest: `src/graph/` (target) + API boundary: `src/server/` (target)
- Security policy: `SECURITY.md` (repo root or `.github/SECURITY.md`)