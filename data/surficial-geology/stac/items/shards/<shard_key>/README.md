---
title: "🧩 Surficial Geology — STAC Item Shard (<shard_key>)"
path: "data/surficial-geology/stac/items/shards/<shard_key>/README.md"

version: "v0.1.0"
last_updated: "2025-12-14"
release_stage: "Draft / In-Progress"
content_stability: "draft"

status: "Active"
doc_kind: "Index"
header_profile: "standard"
footer_profile: "standard"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

scope:
  domain: "surficial-geology"
  applies_to:
    - "data/surficial-geology/stac/items/shards/<shard_key>/**"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
classification: "Public"
sensitivity: "General (non-sensitive; auto-mask rules apply)"

jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

commit_sha: "<latest-commit-hash>"
provenance_chain: []

doc_uuid: "urn:kfm:doc:data:surficial-geology:stac:items:shards:<shard_key>:readme:v0.1.0"
semantic_document_id: "surficial-geology-stac-items-shards-<shard_key>-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:data:surficial-geology:stac:items:shards:<shard_key>:readme:v0.1.0"

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

# 🧩 **Surficial Geology — STAC Item Shard: `<shard_key>`**
`data/surficial-geology/stac/items/shards/<shard_key>/README.md`

**Purpose**  
Document the **per-shard** storage rules for STAC Items in this bucket, ensuring deterministic layout, valid STAC semantics, and provenance-safe linkage to KFM distribution assets.

</div>

---

## 📘 Overview

This directory is a **single shard bucket** for Surficial Geology STAC Item JSON files.

`<shard_key>` is a deterministic partition key defined by the sharding scheme documented at:

- `data/surficial-geology/stac/items/shards/README.md`

This folder MUST contain only:

- STAC **Item** JSON files assigned to `<shard_key>`, and
- optional shard-local inventory metadata (if the pipeline emits it).

This folder MUST NOT contain:

- data assets (those live under `data/surficial-geology/outputs/**`),
- raw sources (those live under `data/surficial-geology/raw/**`),
- manual “fixes” to emitted Items (fix the generator and regenerate).

---

## 🗂️ Directory Layout

~~~text
📁 data/surficial-geology/stac/items/shards/             — Sharded STAC Items (bucketed)
└── 📁 <shard_key>/                                     — This shard bucket (deterministic)
    ├── 📄 README.md                                    — This file (bucket rules)
    ├── 🧾 <item_id>.json                               — STAC Item (one per id; JSON)
    ├── 🧾 <item_id>.json                               — STAC Item (one per id; JSON)
    └── 🧾 shard.manifest.json                          — Optional (derived): bucket inventory + checksums
~~~

Notes:

- Filenames SHOULD be deterministic and filesystem-safe.
- If a manifest exists, treat it as derived output: regenerate it; do not patch it.

---

## 🧭 Context

Shard buckets are a filesystem scalability strategy for large STAC catalogs. They must not change STAC meaning.

Canonical entry points:

- Dataset-local STAC root: `data/surficial-geology/stac/`
- Collections: `data/surficial-geology/stac/collections/`
- Items: `data/surficial-geology/stac/items/`
- Sharding policy: `data/surficial-geology/stac/items/shards/README.md`

---

## 📦 Data & Metadata

### Item requirements (minimum)

Every `*.json` file in this shard MUST be a valid STAC Item and SHOULD include:

- `type: "Feature"`
- `stac_version`
- `id` (stable; unique across the whole Surficial Geology catalog)
- `collection` (or a collection link per profile)
- `geometry` and `bbox`
- `properties.datetime` or an explicit interval representation
- `links[]` with correct navigation semantics (self/collection/parent/root as defined by generator)
- `assets` pointing to versioned deliverables (vectors/tiles/metadata) and optional provenance artifacts

### Shard membership invariant

- Item placement in this folder MUST match the shard key scheme.
- Do not move Items between shard folders unless the sharding scheme is explicitly migrated.
- A sharding migration is a breaking catalog change and must be recorded in lineage and release notes.

### Optional `shard.manifest.json` (if used)

If emitted, the manifest SHOULD be derived and MAY include:

- shard key, item count
- file inventory (paths + sha256)
- derived bucket bbox/temporal summaries (if computed deterministically)

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Items in this shard belong to a Collection under `data/surficial-geology/stac/collections/`.
- Items’ `assets.*.href` SHOULD reference KFM-managed artifacts, typically under:
  - `data/surficial-geology/outputs/vectors/`
  - `data/surficial-geology/outputs/tiles/`
  - `data/surficial-geology/outputs/metadata/`

### DCAT

- DCAT publication typically occurs at dataset/distribution level.
- Item JSON files are metadata containers; avoid duplicating or contradicting dataset rights statements.

### PROV

- Item JSON files may be modeled as `prov:Entity` outputs of a catalog-generation `prov:Activity`.
- Where lineage is captured, Items should be traceable to:
  - producing run artifacts (`mcp/runs/**`), and/or
  - PROV exports (`data/surficial-geology/lineage/prov/**`), and/or
  - OpenLineage events (`data/surficial-geology/lineage/openlineage/**`).

---

## 🧠 Story Node & Focus Mode Integration

This shard supports:

- fast enumeration of Items for Focus Mode browsing,
- deterministic linking from narratives → STAC Item ids,
- provenance-led “how this asset was produced” views (via linked lineage artifacts).

Focus Mode outputs must remain evidence-led and must not invent missing lineage or rights.

---

## 🧪 Validation & CI/CD

Minimum expectations for changes in this shard:

- STAC validation passes for every Item JSON (validator version pinned by the pipeline).
- No duplicate `id` values across shards.
- `assets.*.href` targets are stable and versioned (repo-relative where applicable).
- Governance scans pass:
  - no secrets
  - no PII
  - no disallowed sensitive precision when sovereignty flags require masking/generalization.

---

## ⚖ FAIR+CARE & Governance

Catalog metadata can increase inference risk when combined with other layers.

For this shard:

- do not embed restricted precision beyond policy thresholds,
- ensure license/rights are inherited from authoritative source tracking,
- record masking/generalization decisions in provenance and (when relevant) catalog metadata.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v0.1.0**  | 2025-12-14 | Initial per-shard README for `<shard_key>` bucket: layout, invariants, validation, and governance expectations. |

---

<div align="center">

🧩 **Surficial Geology — STAC Item Shard: `<shard_key>`**  
KFM Catalog Layer · Deterministic Sharding · Provenance-First

[📘 Docs Root](../../../../../../docs/README.md) ·
[📂 Standards Index](../../../../../../docs/standards/README.md) ·
[📄 Templates Index](../../../../../../docs/templates/README.md) ·
[⚙ CI/CD Workflows](../../../../../../docs/workflows/README.md) ·
[📈 Telemetry Standard](../../../../../../docs/standards/telemetry_standards.md) ·
[📊 Telemetry Docs](../../../../../../docs/telemetry/README.md) ·
[♿ UI Accessibility Standard](../../../../../../docs/standards/ui_accessibility.md) ·
[🏛️ Governance Charter](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP-DL v6.3 · KFM-MDP v11.2.6

</div>

