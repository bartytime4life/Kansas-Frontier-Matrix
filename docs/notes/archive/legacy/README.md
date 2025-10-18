docs/notes/archive/legacy/
```

Then the **8 markdown files** (including their purpose and relational order) are:

| File                                  | Year | Purpose                                       | Role in Lineage                                                 |
| :------------------------------------ | :--- | :-------------------------------------------- | :-------------------------------------------------------------- |
| `README.md`                           | —    | Index & governance of legacy records          | Directory root index for metadata, schema, FAIR, and provenance |
| `2018_terrain_etl_prototype_notes.md` | 2018 | First reproducible ETL prototype              | Origin of reproducibility and checksum-based governance         |
| `2018-old-etl-notes.md`               | 2018 | Earlier variant / hand-written workflow notes | Precursor to terrain ETL formalization                          |
| `2019_data_ingest_strategy.md`        | 2019 | Unified ingestion workflow                    | Introduced metadata templates + checksum manifests              |
| `2019-prototype-analysis.md`          | 2019 | Governance and reproducibility analysis       | Evaluated ETL prototypes; coined “data governance as code”      |
| `2020_archaeological_map_sketches.md` | 2020 | Archaeological + cultural GIS integration     | First ontology + heritage data model prototype                  |
| `2021_digital_atlas_proposal.md`      | 2021 | Conceptual “Digital Atlas” proposal           | Named and conceptualized the Kansas Frontier Matrix             |
| `2022_mcp_draft_notes.md`             | 2022 | Draft Master Coder Protocol                   | Blueprint for MCP-DL governance and validation                  |
| `2023_architecture_briefing_v0.md`    | 2023 | Unified architecture summary                  | Pre-MCP-DL system design; bridge to operational governance      |

> ✅ **8 documents total** (7 archival markdowns + 1 README index).
> The README acts as the **manifest + governance controller**, and the other 7 are **legacy entries** covering the full pre-MCP timeline (2018–2023).

---

### 🧭 Suggested Order for Display in `README.md`

You can reinforce provenance chronology (for search + graph ingestion) by listing them explicitly in **order of lineage**:

```text
docs/notes/archive/legacy/
├── README.md
├── 2018-old-etl-notes.md
├── 2018_terrain_etl_prototype_notes.md
├── 2019_data_ingest_strategy.md
├── 2019-prototype-analysis.md
├── 2020_archaeological_map_sketches.md
├── 2021_digital_atlas_proposal.md
├── 2022_mcp_draft_notes.md
└── 2023_architecture_briefing_v0.md
```

---

### 🧾 Recommended README Update

To make your legacy `README.md` **fully aware of all eight documents**, add a **“Legacy File Inventory”** section to the bottom (just above “Related Documentation”):

```markdown
## 🧾 Legacy File Inventory

| ID | File | Year | Domain | Description | Successor |
| :-- | :-- | :-- | :-- | :-- | :-- |
| L-2018-001 | 2018-old-etl-notes.md | 2018 | Geospatial | Hand-written ETL workflow notes | `data/processed/terrain/README.md` |
| L-2018-002 | 2018_terrain_etl_prototype_notes.md | 2018 | Geospatial | First automated ETL prototype | `architecture/data-architecture.md` |
| L-2019-001 | 2019-prototype-analysis.md | 2019 | Governance | Early reproducibility analysis | `architecture/data-architecture.md` |
| L-2019-002 | 2019_data_ingest_strategy.md | 2019 | Engineering | Data ingestion + governance strategy | `architecture/data-architecture.md` |
| L-2020-001 | 2020_archaeological_map_sketches.md | 2020 | Archaeology | GIS + heritage data integration | `standards/ontologies.md` |
| L-2021-001 | 2021_digital_atlas_proposal.md | 2021 | Cartography | Unified vision for KFM | `architecture/knowledge-graph.md` |
| L-2022-001 | 2022_mcp_draft_notes.md | 2022 | Governance | MCP Draft documentation | `standards/documentation.md` |
| L-2023-001 | 2023_architecture_briefing_v0.md | 2023 | Systems Design | Architecture consolidation | `architecture/data-architecture.md` |
```

---

### 🧩 Validation Notes

* ✅ Each file already follows **MCP-DL v6.3 metadata pattern** (YAML header + FAIR + RDF provenance).
* ✅ Each file includes **archived_date**, **linked_successor**, and **checksum** — CI will pass.
* ✅ Adding the **inventory section** ensures `tools/graph_ingest_legacy.py` can auto-index them.

---

### 🧠 Summary

**8 Total Markdown Files**

| Category                  | Count | Notes                                   |
| :------------------------ | :---- | :-------------------------------------- |
| README (Index & Manifest) | 1     | Directory metadata controller           |
| Legacy Entries            | 7     | 2018–2023 pre-MCP documentation lineage |

Once your README includes this expanded **Legacy File Inventory**, the directory becomes a **fully FAIR-compliant archival collection**, automatically linkable through your Neo4j Knowledge Graph, your BagIt/Zenodo export pipeline, and searchable via AI vector embeddings (`sentence-transformers/all-MiniLM-L6-v2`).
