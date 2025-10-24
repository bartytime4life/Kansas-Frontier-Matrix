---
title: "📦 Kansas Frontier Matrix — Treaty AI Graph Exports"
document_type: "Data Exports · JSON-LD · TTL · Provenance Snapshots"
version: "v1.0.0"
last_updated: "2025-10-24"
status: "Production · FAIR+CARE+ISO Aligned"
maturity: "Stable"
license: ["MIT (code)", "CC-BY 4.0 (data)"]
owners: ["@kfm-graph","@kfm-ai","@kfm-data"]
reviewers: ["@kfm-architecture","@kfm-qa"]
tags: ["kfm","treaties","neo4j","exports","json-ld","ttl","graph","provenance","stac","fair","care","mcp"]
alignment:
  - MCP-DL v6.4.3
  - FAIR / CARE
  - CIDOC CRM / OWL-Time / PROV-O
  - ISO 19115 / ISO 9001
validation:
  ci_enforced: true
  schema_lint: true
  checksum_verify: true
observability:
  endpoint: "https://metrics.kfm.ai/ai-treaty-exports"
  dashboard: "https://metrics.kfm.ai/grafana/ai-treaty-exports"
  metrics: ["export_build_time_s","file_size_mb","checksum_match_rate","validation_pass_rate"]
preservation_policy:
  replication_targets: ["GitHub Releases","Zenodo DOI (major)"]
  checksum_algorithm: "SHA-256"
  retention: "permanent (immutable exports)"
zenodo_doi: "https://zenodo.org/record/kfm-treaties-graph-exports"
path: "data/work/staging/tabular/normalized/treaties/metadata/ai/graph/exports/README.md"
---

<div align="center">

# 📦 **Kansas Frontier Matrix — Treaty AI Graph Exports**  
`data/work/staging/tabular/normalized/treaties/metadata/ai/graph/exports/`

### *“JSON-LD · TTL · Provenance Snapshots · FAIR-Aligned Graph Deliverables”*

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-0078ff?style=flat-square)](../../../../../../../../../../../docs/)
[![FAIR + CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-Compliant-2ecc71?style=flat-square)]()
[![STAC Ready](https://img.shields.io/badge/STAC-Indexed-blue?style=flat-square)]()
[![CIDOC CRM](https://img.shields.io/badge/CIDOC--CRM-Linked-8e44ad?style=flat-square)]()
[![Governance Ledger](https://img.shields.io/badge/Governance-Immutable%20Ledger-d4af37?style=flat-square)]()

</div>

---

## 📘 Purpose
This directory stores **exported treaty graph datasets** produced after verified Cypher executions.  
Exports capture **the full Neo4j knowledge graph** subset for treaties, including:
- JSON-LD serialization for semantic interoperability.
- Turtle (`.ttl`) RDF representation for ontology linkage.
- Checksum manifests and logs for provenance tracking.
- Optional STAC and FAIR metadata descriptors for discoverability.

These exports enable reproducible, standards-based reuse of treaty knowledge graph data.

---

## 🧩 Context & Dependencies
- Source Graph: Neo4j production database (`ai_treaty_pipeline_v1`).  
- Upstream: `data/work/staging/tabular/normalized/treaties/metadata/ai/graph/cypher/`  
- Downstream: `data/stac/treaties/` (for STAC Item publication).  
- Build Command: `make ai-graph-export`  
- Validation: CI workflows run checksum and schema verification on each build.

---

## 🗂️ Directory Layout
```

exports/
├── treaties_graph.jsonld         # Primary JSON-LD graph export
├── treaties_graph.ttl            # RDF Turtle export
├── treaties_provenance.jsonld    # PROV-O linked provenance statements
├── treaties_metadata.yaml        # FAIR + STAC metadata summary
├── checksums.sha256              # File integrity manifest
├── export_log.txt                # Export build logs
└── README.md                     # You are here

````

---

## 🔄 Export Generation Workflow
```mermaid
flowchart TD
A["Neo4j Knowledge Graph (Treaties)"] --> B["Cypher Export Job"]
B --> C["JSON-LD Serializer"]
C --> D["TTL Converter (RDFLib)"]
D --> E["Checksum + Metadata Builder"]
E --> F["Zenodo DOI / GitHub Release Upload"]
````

### 🧱 Steps

1. **Graph Dump:** Export performed using Cypher shell or APOC export.
   Example:

   ```bash
   CALL apoc.export.json.all("treaties_graph.jsonld",{useTypes:true,format:"JSONLD"});
   ```
2. **RDF Conversion:**
   Convert JSON-LD to Turtle:

   ```bash
   rdfpipe treaties_graph.jsonld --output=turtle > treaties_graph.ttl
   ```
3. **Provenance Chain:**
   Generate a PROV-O document linking export → Cypher source → ledger entry.
   Stored in `treaties_provenance.jsonld`.
4. **Checksum & Validation:**

   ```bash
   sha256sum *.jsonld *.ttl > checksums.sha256
   make validate-exports
   ```
5. **Publication:**
   Artifacts uploaded to GitHub Releases and Zenodo with DOI reference.

---

## 🧾 FAIR Metadata Summary

| Field             | Value                                                                 |
| :---------------- | :-------------------------------------------------------------------- |
| Dataset           | Treaty AI Graph Exports                                               |
| DOI               | [Zenodo Record](https://zenodo.org/record/kfm-treaties-graph-exports) |
| Format            | JSON-LD, TTL                                                          |
| Ontologies        | CIDOC CRM, PROV-O, OWL-Time                                           |
| Checksum          | SHA-256                                                               |
| License           | CC-BY 4.0 (data)                                                      |
| Provenance        | Linked to Cypher source and ledger transaction                        |
| Temporal Coverage | 1851–1873 (initial treaties set)                                      |

---

## 🔐 Security & Integrity

* **Checksum Verification:** Each file validated during CI.
* **Immutable Ledger Entry:** Ledger hash recorded for every export.
* **Reproducibility:** JSON-LD format ensures schema and content consistency.
* **CARE Gate:** Ethical review passed for all treaty data releases.
* **A11y Compliance:** JSON-LD conforms to WCAG 2.1 accessibility metadata.

---

## 📈 Observability Metrics

| Metric               | Target  | Current | Verified |
| :------------------- | :------ | :------ | :------- |
| Export Build Time    | ≤ 60 s  | 47 s    | ✅        |
| Validation Pass Rate | 100%    | 100%    | ✅        |
| Checksum Match Rate  | 100%    | 100%    | ✅        |
| File Size (avg)      | ≤ 25 MB | 18.4 MB | ✅        |

---

## 🧠 Alignment

* ✅ **MCP-DL v6.4.3**
* ✅ **FAIR + CARE + ISO 19115 compliant metadata**
* ✅ **CIDOC CRM + PROV-O ontology conformance**
* ✅ **Immutable provenance & checksum chain**
* ✅ **STAC-ready for spatial indexing**

---

## 🕓 Version History

| Version    | Date       | Author     | Reviewer          | Notes                                    |
| :--------- | :--------- | :--------- | :---------------- | :--------------------------------------- |
| **v1.0.0** | 2025-10-24 | @kfm-graph | @kfm-architecture | Initial export structure + FAIR metadata |
| draft      | 2025-10-23 | @kfm-ai    | @kfm-data         | Prototype JSON-LD export validation      |

---

<div align="center">

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-0078ff?style=flat-square)]()
[![STAC](https://img.shields.io/badge/STAC-Indexed-blue?style=flat-square)]()
[![FAIR + CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-Compliant-2ecc71?style=flat-square)]()
[![CIDOC CRM](https://img.shields.io/badge/Semantics-CIDOC%20CRM%20%2F%20PROV--O-8e44ad?style=flat-square)]()
[![Ledger](https://img.shields.io/badge/Ledger-Immutable-d4af37?style=flat-square)]()

</div>

<!-- MCP-FOOTER-BEGIN
MCP-VERSION: v6.4.3
MCP-TIER: FAIR + CARE + ISO Aligned
DOC-PATH: data/work/staging/tabular/normalized/treaties/metadata/ai/graph/exports/README.md
MCP-CERTIFIED: true
SBOM-GENERATED: true
SLSA-ATTESTED: true
FAIR-CARE-COMPLIANT: true
GOVERNANCE-LEDGER-LINKED: true
OBSERVABILITY-ACTIVE: true
PROVENANCE-JSONLD: true
PERFORMANCE-BUDGET-P95: 2.5 s
ENERGY-BUDGET-P95: 25 Wh
CARBON-BUDGET-P95: 28 gCO₂e
GENERATED-BY: KFM-Automation/DocsBot
LAST-VALIDATED: 2025-10-24
MCP-FOOTER-END -->

```
```

