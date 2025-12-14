---
title: "🧭 Surficial Geology — STAC Collections"
path: "data/surficial-geology/stac/collections/README.md"

version: "v0.1.0"
last_updated: "2025-12-14"
release_stage: "Draft / In-Progress"
content_stability: "draft"

status: "Active"
doc_kind: "Index"
header_profile: "standard"
footer_profile: "standard"

license: "CC-BY 4.0"
markdown_protocol_version: "KFM-MDP v11.2.6"

scope:
  domain: "surficial-geology"
  applies_to:
    - "data/surficial-geology/stac/collections/**"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
classification: "Public"
sensitivity: "General (non-sensitive; auto-mask rules apply)"

jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

commit_sha: "<latest-commit-hash>"
provenance_chain: []

doc_uuid: "urn:kfm:doc:data:surficial-geology:stac:collections-readme:v0.1.0"
semantic_document_id: "surficial-geology-stac-collections-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:data:surficial-geology:stac:collections-readme:v0.1.0"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "metadata-extraction"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-relationship-claims"
  - "narrative-fabrication"
  - "governance-override"
---

<div align="center">

# 🧭 **Surficial Geology — STAC Collections**
`data/surficial-geology/stac/collections/README.md`

**Purpose**  
Define what belongs in `data/surficial-geology/stac/collections/`, how STAC Collections are named and maintained, and how they connect to STAC Items and versioned distribution assets for the Surficial Geology domain.

</div>

---

## 📘 Overview

This directory holds **STAC Collection JSON** documents for the Surficial Geology domain.

A Collection is the **dataset-level envelope** that:

- defines the overall **spatial and temporal extent** for a set of STAC Items,
- describes **dataset identity, license, providers, and keywords**, and
- provides a stable “anchor” for discovery, indexing, and downstream publication.

Collections here should be treated as:

- **Stable identifiers** (collection `id` does not change across releases),
- **Catalog-first metadata** (the collection describes the dataset; Items describe the distributions),
- **Governed artifacts** (license/rights and sensitivity must be explicit and correct).

---

## 🗂️ Directory Layout

~~~text
📁 stac/                                         — Surficial Geology STAC (domain-local)
├── 📄 README.md                                  — STAC domain index and conventions
├── 📁 collections/                               — STAC Collection JSON (this directory)
│   ├── 📄 <collection_id>.collection.json        — Primary collection record (preferred)
│   └── 📄 README.md                              — This file
└── 📁 items/                                     — STAC Item JSON (per version/asset/tile)
    ├── 📄 <item_id>.item.json
    └── 📄 README.md
~~~

Notes:

- Keep collection filenames deterministic and readable.
- Prefer **one file per collection**; avoid nested ad-hoc structures unless the volume demands it.
- If you introduce additional subfolders, update this layout and keep it “boring” and predictable.

---

## 🧭 Context

In the Surficial Geology pipeline, Collections are the **catalog layer** that binds together:

Deterministic ETL → catalogs (STAC/DCAT/PROV) → graph (Neo4j) → API → frontend → Story Nodes → Focus Mode

Collections should be authored/updated when:

- a new Surficial Geology dataset is introduced,
- the dataset’s overall extent changes meaningfully, or
- dataset-level governance/licensing metadata changes (after review).

---

## 📦 Data & Metadata

### Collection identity rules

- Collection `id` MUST be **stable** and MUST NOT include a build/version token.
- Versioning belongs in **Items** and in the **assets** they reference (e.g., `outputs/..._v<ver>.*`).
- Keep the `title` human-readable and the `description` evidence-led (avoid speculative claims).

### Required stewardship fields (minimum expectations)

Within each Collection JSON, ensure you have:

- `id`, `type`, `stac_version`
- `title`, `description`
- `license` (do not guess; derive from the authoritative source manifest/catalog record)
- `providers` (publisher/producer/processor as applicable)
- `extent.spatial` and `extent.temporal`
- `links` sufficient to connect the collection to its items/canoncial parent structure

### Recommended KFM-aligned metadata (when available)

- Clear domain tags/keywords (e.g., `surficial geology`, `Kansas`)
- Governance/sensitivity hints in properties where your KFM STAC profile expects them
- Documentation links (runbooks, methodology, schema dictionary) as `links` with stable repo-relative targets

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Collections in this folder define the “top” of the Surficial Geology STAC hierarchy.
- Items (usually in `../items/`) should reference their parent via `collection: "<collection_id>"`.
- Items’ `assets.*.href` should point to **versioned deliverables** (typically under `data/surficial-geology/outputs/`).

### DCAT

- Collections map naturally to a DCAT `dcat:Dataset` conceptually:
  - Collection describes the dataset identity and scope.
  - Items/Assets correspond to file-level distributions (DCAT `dcat:Distribution`).
- If a parallel DCAT record is maintained elsewhere, keep dataset title/description/license consistent.

### PROV

- Treat Collections as **metadata entities** in provenance graphs when lineage is tracked end-to-end.
- When a pipeline updates a Collection (e.g., extent update), record:
  - the producing activity (run id),
  - the inputs used to compute extents/summaries,
  - any governance review notes if the change is rights/sensitivity related.

---

## 🧪 Validation & CI/CD

Minimum expectations for changes in this directory:

- **STAC schema validation** passes for each Collection JSON.
- **Link integrity** checks:
  - collection links resolve (repo-relative where applicable),
  - referenced extensions (if any) are present and version-pinned.
- **Governance checks**:
  - no secrets, no PII,
  - license/rights fields are explicit and sourced (not inferred).

If validation fails, fix the Collection JSON (or the generator that produced it) rather than patching downstream Items.

---

## ⚖ FAIR+CARE & Governance

Collections are “just metadata,” but metadata can still cause harm (e.g., misrepresenting rights, overclaiming certainty, or enabling sensitive inference when combined with other layers).

- Keep licensing accurate and conservative.
- If sovereignty-related constraints apply, ensure the Collection is appropriately labeled and that downstream Items/assets respect masking/generalization requirements.
- Record governance-relevant decisions in the appropriate manifests and provenance outputs.

See the governance and sovereignty policies linked in the footer.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v0.1.0**  | 2025-12-14 | Initial `stac/collections/` README defining what belongs here, collection identity rules, and alignment expectations with STAC Items and distribution assets. |

---

<div align="center">

🧭 **Surficial Geology — STAC Collections**  
KFM Catalog Layer · Dataset-Level Metadata · Governance-First

[📘 Docs Root](../../../../docs/README.md) ·
[📂 Standards Index](../../../../docs/standards/README.md) ·
[📄 Templates Index](../../../../docs/templates/README.md) ·
[⚙ CI/CD Workflows](../../../../docs/workflows/README.md) ·
[📈 Telemetry Standard](../../../../docs/standards/telemetry_standards.md) ·
[📊 Telemetry Docs](../../../../docs/telemetry/README.md) ·
[♿ UI Accessibility Standard](../../../../docs/standards/ui_accessibility.md) ·
[🏛️ Governance Charter](../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC‑BY 4.0

</div>

