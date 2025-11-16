---
title: "🌐 Kansas Frontier Matrix — Pipeline Publishing Guide (STAC·DCAT·Neo4j·RDF·CARE v2) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/guides/pipelines/publishing-guide.md"
version: "v10.4.2"
last_updated: "2025-11-16"
review_cycle: "Quarterly · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.2/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.2/manifest.zip"
telemetry_ref: "../../../releases/v10.4.2/pipeline-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/publishing-guide-v2.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.2"
status: "Active / Enforced"
doc_kind: "Guide"
intent: "publishing-pipelines"
fair_category: "F1-A1-I1-R1"
care_label: "C2-A2-R2-E1"
kfm_readme_template: "Platinum v7.1"
ci_enforced: true
---

<div align="center">

# 🌐 **Kansas Frontier Matrix — Pipeline Publishing Guide**  
`docs/guides/pipelines/publishing-guide.md`

**Purpose:**  
Define the **official KFM Publishing Standard** for converting validated, FAIR+CARE-compliant,  
checksum-locked datasets into public-facing **STAC**, **DCAT**, **Neo4j graph nodes**,  
and **RDF/GeoSPARQL Linked Data**, with complete lineage, provenance, and governance.

**Scope:**  
This guide describes the **final stage** of every KFM pipeline:  
**Processed → Versioned → Published → Registered → Immutable**.

</div>

---

# 📘 Overview

Publishing is the **irreversible promotion** of a dataset into the Kansas Frontier Matrix public knowledge system.

All published assets MUST be:

- **FAIR+CARE-certified**  
- **Schema-validated** (GX, JSON Schema, STAC/DCAT)  
- **Lineage-complete** (JSON-LD provenance)  
- **Checksum-locked** (SHA-256 → multihash)  
- **Version-pinned** (SemVer X.Y.Z)  
- **Discoverable** (STAC, DCAT, Neo4j, RDF endpoints)  
- **Observable** (telemetry v2 signals)  
- **Immutable** once published  

Only datasets inside:

~~~text
data/processed/<dataset>/<version>/
~~~

are eligible for publication.

---

# 🗂️ Directory Layout (Publishing Layer · KFM-Aligned)

~~~text
data/
├── processed/                               # Final FAIR+CARE-approved datasets
│   └── <dataset>/<version>/                 # Version-pinned payloads
│       ├── data.parquet                     # Typed, deterministic artifact
│       ├── lineage.jsonld                   # Provenance (PROV-O / CIDOC / CARE)
│       ├── telemetry.ndjson                 # Run telemetry v2
│       └── checksums.txt                    # SHA-256 and multihash registry
│
├── stac/
│   └── published/
│       ├── collections/<collection>.json    # STAC Collections
│       └── items/<collection>/<id>.json     # STAC Items
│
├── dcat/
│   └── datasets/<dataset>.jsonld            # DCAT Dataset JSON-LD
│
├── rdf/
│   └── <dataset>/<version>/*.ttl            # RDF + GeoSPARQL triples
│
└── lineage/
    └── <dataset>/<version>.jsonld           # Lineage index (dataset-level)
~~~

---

# 🧩 Publishing Architecture (KFM-Styled Mermaid)

```mermaid
flowchart TD

  subgraph STAGING["Staging → Processed"]
    A["Validated Data<br/>CARE-labeled · checksum-locked"]
  end

  subgraph GATE["Publish Gate"]
    B["FAIR+CARE<br/>+ Provenance Checks"]
  end

  subgraph EXPORT["Exporters"]
    C["STAC Items/Collections"]
    D["DCAT Datasets<br/>JSON-LD"]
    E["Neo4j Nodes + Edges"]
    F["RDF Export<br/>GeoSPARQL Linked Data"]
  end

  subgraph GOVERN["Governance & Observability"]
    G["Governance Ledger<br/>Append Entry"]
    H["Telemetry v2<br/>Publish Metrics"]
  end

  A --> B
  B -->|PASS| C
  B -->|PASS| D
  B -->|PASS| E
  B -->|PASS| F
  F --> G
  G --> H

  classDef staging fill:#ebf8ff,stroke:#2b6cb0,color:#1a365d;
  classDef gate fill:#fefcbf,stroke:#b7791f,color:#744210;
  classDef export fill:#e9d8fd,stroke:#6b46c1,color:#44337a;
  classDef govern fill:#f0fff4,stroke:#2f855a,color:#22543d;

  class STAGING staging;
  class GATE gate;
  class EXPORT export;
  class GOVERN govern;
````

---

# 🛠 1. Publishing Gate Requirements

Datasets must meet ALL:

## ✔ Validation

* **GX validation:** all tests pass
* **JSON Schema / STAC / DCAT validation:** 100% compliant
* **Linked Data validation:** RDF + GeoSPARQL + PROV-O shape checks
* **Accessibility metadata:** required alt-text/titles
* **Energy/Carbon metadata:** embedding telemetry v2

## ✔ Governance (CARE v2)

* No unresolved sovereignty/masking violations
* `kfm:careLabel` present
* `kfm:maskingStrategy` present for sensitive/restricted
* Indigenous data sovereignty rules applied

## ✔ Provenance

* `lineage.jsonld` valid (CIDOC CRM + PROV-O + CARE)
* Versioned processingSteps[]
* Attestations (SLSA-style) generated

## ✔ Required Metadata Fields

| Field                   | Description                   |
| ----------------------- | ----------------------------- |
| `kfm:version`           | Dataset SemVer                |
| `kfm:checksum_sha256`   | Integrity lock                |
| `kfm:careLabel`         | CARE v2 classification        |
| `kfm:maskingStrategy`   | H3 / bounding / centroid-only |
| `kfm:lineageRef`        | Path to JSON-LD lineage       |
| `kfm:telemetryRef`      | Path to NDJSON telemetry      |
| `kfm:processingSteps[]` | Pipeline phase trace          |
| `kfm:provenanceRef`     | Governance ledger link        |

---

# 📦 2. STAC Publishing (Collections + Items)

## Collections

Path:

```text
data/stac/published/collections/<collection>.json
```

Must include:

* STAC 1.0 compliant schema
* `extent.spatial` / `extent.temporal` normalized
* Asset summaries
* Providers + licenses
* KFM extensions:

  * `kfm:version`
  * `kfm:careLabel`
  * `kfm:lineageRef`
  * `kfm:stacVersionHistory[]`

## Items

```text
data/stac/published/items/<collection>/<item>.json
```

Requirements:

* Geometry normalized
* `datetime`, `bbox`, EO fields
* `kfm:*` metadata populated
* Checksum multihash (blake3 OR sha256-multihash)
* Links:

  * `collection`
  * `self`
  * `root`
  * `lineage`
  * `telemetry`

---

# 📚 3. DCAT Publishing (JSON-LD)

Path:

```text
data/dcat/datasets/<dataset>.jsonld
```

Must include:

* `dct:title`, `dct:description`, `dct:creator`, `dct:license`
* `dct:temporal`, `dct:spatial`
* `dcat:distribution[]` referencing STAC items
* CARE + provenance metadata
* `kfm:version`

Validation:
`dcat-validate.yml`

---

# 🌐 4. Neo4j Publishing (Graph)

## Entities

### Scene

`(:Scene {id})`

Properties:

* `geom` (WKT/GeoJSON)
* `centroid` (POINT)
* `temporal_bounds`
* `collection_id`
* CARE flags
* provenance refs

### Dataset

`(:Dataset {id})`

* Semantic version
* License
* STAC/DCAT references

## Relationships

* `(:Scene)-[:INTERSECTS]->(:County)`
* `(:Scene)-[:WITHIN]->(:AOI)`
* `(:Scene)-[:CREATED_FROM]->(:Dataset)`

Writes must be **idempotent**:

```text
MERGE ... ON MATCH SET ...
```

---

# 🌐 5. RDF / GeoSPARQL Publishing

Path:

```text
data/rdf/<dataset>/<version>/*.ttl
```

Triples include:

* `geo:asWKT`
* `geo:sfIntersects` / `geo:sfWithin`
* PROV-O: `prov:wasGeneratedBy`
* Dataset-level PROV + CARE statements

Validation:

* `prov_o_context.jsonld`
* `cidoc_crm_context.jsonld`
* `geosparql_context.jsonld`

---

# 🧬 6. Lineage (PROV-O + CIDOC + CARE)

Stored here:

```text
data/processed/<dataset>/<version>/lineage.jsonld
```

Requirements:

* PROV-O chains (`prov:Activity`, `prov:Entity`, `prov:Agent`)
* CARE metadata
* Full pipeline trace (`processingSteps[]`)
* Input → Output derivation paths
* Collection-wide lineage mirrored to:
  `data/lineage/<dataset>/<version>.jsonld`

---

# 📡 7. Telemetry (v2)

Telemetry NDJSON:

```text
data/processed/<dataset>/<version>/telemetry.ndjson
```

Contains fields:

* `run_id`
* `event` (`publish`)
* `dataset_id` / `version`
* counts: items/collections/graph_nodes/rdf_files
* energy metrics (ISO 50001)
* CO₂e estimates (ISO 14064)
* care violations
* duration_ms
* semantic flags

Aggregated to:

```text
releases/v10.4.2/pipeline-telemetry.json
```

---

# 🛡 8. Governance Ledger (Append-Only)

Path:

```text
docs/reports/audit/data_provenance_ledger.jsonl
```

Record includes:

* dataset ID
* version
* CARE label + masking
* lineageRef
* telemetryRef
* stacRef / dcatRef / graphRef / rdfRef
* sbomRef
* attestationRef (SLSA)
* reviewers
* CI workflow IDs

Ledger entries must be **append-only**.

---

# 🔒 9. CI Enforcement (Publishing Gate)

Before merge → publish:

| Workflow                   | Purpose                    |
| -------------------------- | -------------------------- |
| `stac-validate.yml`        | STAC 1.0 validation        |
| `dcat-validate.yml`        | DCAT JSON-LD validation    |
| `linked-data-validate.yml` | RDF/GeoSPARQL validation   |
| `neo4j-schema-guard.yml`   | Graph constraints          |
| `faircare-validate.yml`    | CARE, sovereignty, masking |
| `sbom-validate.yml`        | SBOM and supply-chain      |
| `telemetry-export.yml`     | Telemetry completeness     |
| `docs-lint.yml`            | KFM MDP enforcement        |

Publications are **blocked** unless all workflows pass.

---

# 🧭 Developer Publishing Checklist

* [ ] Validation (GX/Schema/FAIR+CARE) complete
* [ ] CARE flags + masking correct
* [ ] Lineage JSON-LD valid
* [ ] Telemetry fields populated
* [ ] Checksums validated
* [ ] STAC/DCAT/RDF graphs generated & pass validation
* [ ] Neo4j writes validated
* [ ] Governance ledger updated
* [ ] SBOM present
* [ ] CHANGELOG updated if version changed

---

# 🕰️ Version History

| Version | Date       | Summary                                                                                                      |
| ------: | ---------- | ------------------------------------------------------------------------------------------------------------ |
| v10.4.2 | 2025-11-16 | Full KFM-MDP v10.4.2 upgrade; STAC/DCAT enhancements; lineage v2; telemetry v2; governance ledger extensions |
| v10.3.1 | 2025-11-14 | Initial Publishing Guide; STAC/DCAT/Neo4j/RDF/CARE v1 integration                                            |

---

<div align="center">

**Kansas Frontier Matrix — Canonical Publishing Standard**
FAIR+CARE Data Publishing × Immutable Provenance × STAC/DCAT/Graph/RDF Integration
© 2025 KFM — CC-BY 4.0 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>
```
