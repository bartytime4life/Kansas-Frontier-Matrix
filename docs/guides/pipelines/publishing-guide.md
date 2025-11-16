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
checksum-locked datasets into public-facing **STAC**, **DCAT**, **Neo4j graph structures**, and  
**RDF/GeoSPARQL Linked Data**, with complete lineage, provenance, and governance metadata.

This is the authoritative, immutable specification for **KFM v10.4.2** publishing workflows.

</div>

---

# 📘 Overview

Publishing is the **final, irreversible, certification step** of any Kansas Frontier Matrix (KFM) pipeline.

After a dataset passes:

- schema validation  
- FAIR+CARE governance checks  
- deterministic transforms  
- provenance verification  
- telemetry v2 emission  

…it becomes eligible for **Publication**, the process that exposes the dataset to:

- **STAC 1.0** endpoints  
- **DCAT v3.0** dataset catalog  
- **Neo4j** knowledge graph ingestion  
- **RDF/GeoSPARQL–compliant Linked Data**  
- **Public KFM Releases** (manifest + SBOM + CHANGELOG)  

All published assets are **versioned**, **checksum-locked**, **lineage-linked**, and **immutable**.

---

# 🗂️ Directory Layout (Canonical KFM Publishing Layer)

~~~text
data/
├── processed/                               # Final FAIR+CARE-approved datasets
│   └── <dataset>/<version>/
│       ├── data.parquet                     # Deterministic, typed artifact
│       ├── lineage.jsonld                   # PROV-O + CIDOC + CARE lineage
│       ├── telemetry.ndjson                 # Telemetry v2 run metrics
│       └── checksums.txt                    # SHA-256 + multihash integrity locks
│
├── stac/
│   └── published/
│       ├── collections/<collection>.json    # STAC Collections
│       └── items/<collection>/<id>.json     # STAC Items
│
├── dcat/
│   └── datasets/<dataset>.jsonld            # DCAT 3.0 Dataset metadata
│
├── rdf/
│   └── <dataset>/<version>/*.ttl            # GeoSPARQL RDF triples
│
└── lineage/
    └── <dataset>/<version>.jsonld           # Dataset-wide lineage index
~~~

---

# 🌐 **Full-Page Publishing Gate Diagram (KFM-Styled Mermaid)**

```mermaid
flowchart TD

%% ------------------------------------------------------------
%%  TOP-LEVEL PUBLISHING GATE (FULL PAGE)
%% ------------------------------------------------------------

subgraph STAGING["Staging → Processed<br/><span style='font-size:12px'>Validated · CARE-labeled · Checksum-locked</span>"]
    A["Processed Dataset<br/><span style='font-size:12px'>data/processed/&lt;dataset&gt;/&lt;version&gt;</span>"]
end

subgraph GATE["Publishing Gate<br/><span style='font-size:12px'>FAIR+CARE · Schema · Provenance · Telemetry</span>"]
    B["Gatekeeper<br/><span style='font-size:12px'>All validations must PASS</span>"]
    A --> B
end

subgraph EXPORTS["Publication Targets (Multi-Surface Release)"]
    direction LR
    C["STAC<br/>Collections + Items"]
    D["DCAT<br/>Dataset JSON-LD"]
    E["Neo4j Graph<br/>Scene · Event · Place"]
    F["RDF Export<br/>GeoSPARQL Linked Data"]
end

B -->|PASS| C
B -->|PASS| D
B -->|PASS| E
B -->|PASS| F

subgraph GOVERN["Governance & Observability"]
    G["Governance Ledger<br/><span style='font-size:12px'>Append Entry</span>"]
    H["Telemetry v2<br/><span style='font-size:12px'>Metrics · energy · CO₂ · events</span>"]
end

C --> G
D --> G
E --> G
F --> G
G --> H

classDef staging fill:#ebf8ff,stroke:#2b6cb0,stroke-width:1px,color:#1a365d;
classDef gate fill:#fffbea,stroke:#dd6b20,stroke-width:1px,color:#7b341e;
classDef exports fill:#faf5ff,stroke:#805ad5,stroke-width:1px,color:#553c9a;
classDef ledger fill:#f0fff4,stroke:#38a169,stroke-width:1px,color:#22543d;

class STAGING staging;
class GATE gate;
class EXPORTS exports;
class GOVERN ledger;
````

---

# 🛠 1. Publishing Gate Requirements

### ✔ Validation Requirements

A dataset may **only** pass the gate if:

* **GX validation**: all tests pass
* **Schema validation**: STAC / DCAT / JSON-LD shapes valid
* **GeoSPARQL validation**: RDF/WKT shapes valid
* **FAIR+CARE** enforcement: sovereignty → masking strategy correct
* **Checksum stability**: typed Parquet + metadata must match SHA-256
* **Provenance**: lineage JSON-LD complete & valid
* **Telemetry v2**: metrics recorded and valid

### ✔ Required Metadata Fields

| Field                   | Description                   |
| ----------------------- | ----------------------------- |
| `kfm:version`           | Dataset SemVer                |
| `kfm:checksum_sha256`   | Integrity lock                |
| `kfm:careLabel`         | CARE v2 classification        |
| `kfm:maskingStrategy`   | H3 / bounding / centroid-only |
| `kfm:lineageRef`        | Link to JSON-LD provenance    |
| `kfm:telemetryRef`      | Link to NDJSON telemetry      |
| `kfm:processingSteps[]` | Pipeline-level trace          |
| `kfm:provenanceRef`     | Governance ledger entry       |

---

# 📦 2. STAC Publication

STAC collections and items must be written to:

```text
data/stac/published/
```

### **Collections**

Path:

```text
data/stac/published/collections/<collection>.json
```

Must include:

* Spatial & temporal extents
* Multihash checksums
* Provider + license metadata
* CARE labels + lineage + telemetry refs
* `kfm:stacVersionHistory[]`

### **Items**

Path:

```text
data/stac/published/items/<collection>/<item>.json
```

Must include:

* Normalized geometry
* `datetime`, `bbox`, EO fields
* CARE + provenance metadata
* Lineage + telemetry links
* Multihash asset checksums

---

# 📚 3. DCAT Publication

Path:

```text
data/dcat/datasets/<dataset>.jsonld
```

Requirements:

* DCAT 3.0 Dataset
* `dct:title` / `dct:description` / `dct:publisher`
* Spatial + temporal coverage
* Distribution entries linking STAC items
* CARE + provenance metadata

---

# 🌐 4. Neo4j Publication

Nodes created:

### Scenes

`(:Scene {id})`

* `geom`, `centroid`, `datetime`
* CARE flags
* lineage refs
* provenance details

### Datasets

`(:Dataset {id})`

* Semantic version
* STAC/DCAT references

### Relationships

* `(:Scene)-[:INTERSECTS]->(:County)`
* `(:Scene)-[:WITHIN]->(:AOI)`
* `(:Scene)-[:CREATED_FROM]->(:Dataset)`

All writes must be idempotent:

```text
MERGE … ON MATCH SET …
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
* `prov:wasGeneratedBy`
* CARE metadata

Validation:

* `geosparql_context.jsonld`
* `prov_o_context.jsonld`
* `cidoc_crm_context.jsonld`

---

# 🧬 6. Lineage & Provenance

Stored at:

```text
data/processed/<dataset>/<version>/lineage.jsonld
```

Includes:

* PROV-O + CIDOC chains
* CARE v2 metadata
* processingSteps[]
* input → output lineage

---

# 📡 7. Telemetry v2

Stored at:

```text
data/processed/<dataset>/<version>/telemetry.ndjson
```

Contains:

* run_id
* status
* energy + CO₂ values
* governance flags
* asset counts
* semantic operations

Aggregated to:

```text
releases/v10.4.2/pipeline-telemetry.json
```

---

# 🛡 8. Governance Ledger (Append Only)

Path:

```text
docs/reports/audit/data_provenance_ledger.jsonl
```

Includes:

* dataset
* version
* CARE metadata
* lineageRef
* telemetryRef
* STAC/DCAT/RDF/Graph refs
* SBOM/manifest refs
* reviewer identities
* CI run IDs

---

# 🔒 9. CI Enforcement (Publishing Gate)

Mandatory workflows:

| Workflow                   | Purpose                  |
| -------------------------- | ------------------------ |
| `stac-validate.yml`        | STAC compliance          |
| `dcat-validate.yml`        | DCAT JSON-LD validation  |
| `linked-data-validate.yml` | RDF/GeoSPARQL            |
| `neo4j-schema-guard.yml`   | Graph integrity          |
| `faircare-validate.yml`    | CARE + sovereignty       |
| `sbom-validate.yml`        | Supply chain + manifests |
| `telemetry-export.yml`     | Telemetry v2             |
| `docs-lint.yml`            | KFM MDP compliance       |

---

# 🧭 Developer Publishing Checklist

* [ ] Validation: GX + Schema + FAIR+CARE
* [ ] CARE labels correct; masking verified
* [ ] Lineage JSON-LD validated
* [ ] Telemetry NDJSON complete
* [ ] STAC/DCAT/RDF/Graph exports validated
* [ ] Checksums match
* [ ] Governance ledger appended
* [ ] SBOM + manifest regenerate
* [ ] CHANGELOG updated

---

# 🕰️ Version History

| Version | Date       | Summary                                                                                                    |
| ------: | ---------- | ---------------------------------------------------------------------------------------------------------- |
| v10.4.2 | 2025-11-16 | Full KFM-MDP v10.4.2 upgrade; Added full-page Publishing Gate diagram; lineage/telemetry/CARE v2 expansion |
| v10.3.1 | 2025-11-14 | Initial Publishing Guide                                                                                   |

---

<div align="center">

**Kansas Frontier Matrix — Publishing Guide (v10.4.2)**
FAIR+CARE × Immutable Provenance × STAC/DCAT/Graph/RDF Integration
© 2025 KFM — CC-BY 4.0 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>
