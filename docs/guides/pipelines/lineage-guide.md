---
title: "🧬 Kansas Frontier Matrix — Lineage & Provenance Guide (v10.4.2 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/guides/pipelines/lineage-guide.md"
version: "v10.4.2"
last_updated: "2025-11-16"
review_cycle: "Quarterly · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.2/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.2/manifest.zip"
telemetry_ref: "../../../releases/v10.4.2/pipeline-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/pipelines-lineage-guide-v2.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.2"
status: "Active / Enforced"
doc_kind: "Guide"
intent: "lineage-provenance"
fair_category: "F1-A1-I1-R1"
care_label: "C2-A2-R2-E1"
kfm_readme_template: "Platinum v7.1"
ci_enforced: true
---

<div align="center">

# 🧬 **Kansas Frontier Matrix — Lineage & Provenance Guide**  
`docs/guides/pipelines/lineage-guide.md`

**Purpose:**  
Define the **KFM v10.4.2 standard** for building **immutable, machine-readable, FAIR+CARE-governed lineage**  
across all pipelines: ingestion, preprocessing, analytics, validation, promotion, and publishing.

This guide unifies **PROV-O**, **CIDOC-CRM**, **OGC GeoSPARQL**, **CARE v2**, **Telemetry v2**,  
and **SLSA-style attestations** into one deterministic lineage model.

</div>

---

# 📘 Overview

Lineage is the **contract of trust** inside KFM.  
It guarantees:

- **Traceability** — every dataset shows where it came from  
- **Reproducibility** — every step is represented and replayable  
- **Governance** — CARE v2 decisions are preserved and inspectable  
- **Spatial integrity** — geometry provenance is explicit  
- **Semantic verifiability** — events, transformations, and derivations are formal  

Every KFM dataset MUST include:

- `lineage.jsonld` (CIDOC + PROV-O + GeoSPARQL + CARE v2)  
- Telemetry v2 references  
- SLSA-style attestations  
- Masking and sovereignty documentation  
- Checksums for *every* intermediate and final artifact  
- Links to STAC/DCAT/RDF/Neo4j entities  

---

# 🗂️ Directory Layout (Canonical · v10.4.2)

~~~text
data/
└── processed/
    └── lineage/
        └── <dataset_id>/
            └── <version>.jsonld        # Fully expanded lineage bundle

src/
└── pipelines/
    └── remote-sensing/
        └── lineage/
            ├── build_lineage.py        # Main lineage builder
            ├── extract_prov.py         # Extract PROV entities/activities
            ├── extract_geo.py          # Extract GeoSPARQL geometry
            ├── extract_telemetry.py    # Telemetry v2 integration
            ├── extract_care.py         # CARE v2 integration
            └── schemas/
                └── lineage.schema.json # Required schema for all lineage bundles
~~~

---

## 🌐 Full-Page Lineage Architecture (KFM-Styled Mermaid)

flowchart TD

%% ------------------------------------------------------------
%%  SOURCE ACQUISITION
%% ------------------------------------------------------------
subgraph INGEST["Source Acquisition"]
    A["Source Entities<br/>STAC · Raster · Vector · External Providers"]
end

%% ------------------------------------------------------------
%%  PIPELINE ACTIVITIES
%% ------------------------------------------------------------
subgraph ACTIVITIES["Pipeline Activities"]
    B["Activities (prov:Activity)<br/>Ingest · Preprocess · Analytics · Validate · Publish"]
end

%% ------------------------------------------------------------
%%  VALIDATION GATE
%% ------------------------------------------------------------
subgraph VALIDATE["Validation Gate"]
    C["Validation Checks<br/>GX · CARE v2 · Schema · Geometry · Telemetry"]
end

%% ------------------------------------------------------------
%%  PROMOTION
%% ------------------------------------------------------------
subgraph PROMOTE["Promotion"]
    D["Promoted Entities<br/>Checksum-locked · CARE-labeled"]
end

%% ------------------------------------------------------------
%%  PUBLISHING
%% ------------------------------------------------------------
subgraph PUBLISH["Publishing"]
    E["Published Outputs<br/>multi-surface release"]
end

%% ------------------------------------------------------------
%%  LINEAGE EXPORT
%% ------------------------------------------------------------
subgraph LINEAGE["Lineage Export"]
    F["Lineage Bundle<br/>JSON-LD · PROV-O · CIDOC · GeoSPARQL · CARE v2"]
end

%% ------------------------------------------------------------
%%  GOVERNANCE LEDGER
%% ------------------------------------------------------------
subgraph GOVERN["Governance Ledger"]
    G["Ledger Entry<br/>Append-only provenance"]
end

%% FLOW
A --> B --> C --> D --> E --> F --> G

---

# 🧬 Lineage Model (v10.4.2)

KFM lineage bundles MUST integrate:

* **W3C PROV-O** — derivation, generation, usage, agents
* **CIDOC CRM** — cultural, temporal, narrative semantics
* **OGC GeoSPARQL** — spatial structure, boundaries, WKT
* **CARE v2** — governance, sovereignty, masking
* **Telemetry v2** — energy, CO₂, timings, anomalies
* **SLSA-style attestations** — pipeline-level provenance

### Required high-level structure:

1. **@context block**
2. **Entities (prov:Entity + geo:Feature)**
3. **Activities (prov:Activity)**
4. **Agents (prov:Agent)**
5. **Relations** (prov:used, prov:generated, prov:derivedFrom, …)
6. **Lineage summary**
7. **Links to STAC/DCAT/RDF/Graph**
8. **Governance ledger reference**

---

# 🧱 JSON-LD Context Requirements

Each lineage bundle MUST use:

```json
[
  "https://www.w3.org/ns/prov.jsonld",
  "https://schema.org/",
  "https://openspatial.org/contexts/geosparql.jsonld",
  "docs/contexts/kfm-care-v2.context.jsonld",
  "docs/contexts/kfm-telemetry-v2.context.jsonld",
  "docs/contexts/kfm-lineage.context.jsonld"
]
```

---

# 🏗 Required Entities

## prov:Entity

Every dataset, raster, vector, STAC Item, and downstream derivative must appear:

```json
{
  "@id": "kfm:sentinel2_L1C_2025_07_11_tile_15SVB",
  "@type": ["prov:Entity", "geo:Feature"],
  "kfm:checksum_sha256": "sha256-abc123...",
  "geo:asWKT": "POLYGON((...))",
  "kfm:careLabel": "public",
  "kfm:telemetryRef": "data/processed/.../telemetry.ndjson"
}
```

## prov:Activity

Each pipeline step:

```json
{
  "@id": "kfm:preprocess_S2_2025_07_11",
  "@type": "prov:Activity",
  "prov:startedAtTime": "2025-11-16T03:11:21Z",
  "prov:endedAtTime": "2025-11-16T03:11:40Z",
  "kfm:processingSteps": [
    "cloud_mask",
    "harmonize_gsd",
    "reprojection",
    "radiometric_normalization",
    "rtc",
    "bandstack"
  ],
  "kfm:energy_wh": 12.1,
  "kfm:co2_g": 8.4
}
```

## prov:Agent

Agents include:

* System pipelines (ingest, preprocess, publish)
* Source providers (USGS, ESA, NASA)
* AI modules (if summaries were created)
* Human reviewers (if applicable)

---

# 🔗 Required Relations

Every lineage bundle MUST include:

### Core PROV-O

* `prov:used`
* `prov:generated`
* `prov:wasDerivedFrom`
* `prov:wasAssociatedWith`

### Spatial (GeoSPARQL)

* `geo:sfWithin`
* `geo:sfIntersects`
* `geo:asWKT`

### Cultural (CIDOC CRM)

* `crm:E5_Event`
* `crm:P17_was_motivated_by`
* `crm:P67_refers_to`

### CARE v2

* `kfm:maskingStrategy`
* `kfm:sovereigntyFlags[]`

---

# 🧬 CARE v2 Integration

CARE v2 requires:

* Explicit labeling: `"careLabel": "public|sensitive|restricted"`
* `"maskingStrategy": "h3_r7" | "h3_r5" | "centroid_only" | "remove"`
* Sovereignty flags (`tribal_overlap`, `restricted_zone`, `heritage_site`)
* Justification fields: `"careReason"`
* Masking evidence included in the lineage bundle

---

# 📡 Telemetry v2 Integration

Telemetry must supply:

* `duration_ms`
* `energy_wh`
* `co2_g`
* `errors[]`
* `pixels_processed`
* `masked_pct`
* `care_violations`

Telemetry is linked into lineage via:

```json
"kfm:telemetryRef": "data/processed/<dataset>/<version>/telemetry.ndjson"
```

---

# 🔐 Governance Ledger Integration

Path:

```text
docs/reports/audit/data_provenance_ledger.jsonl
```

Each lineage bundle must append:

* dataset ID
* version
* checksum
* careLabel + maskingStrategy
* lineageRef
* telemetryRef
* stac/dcat/rdf/graph refs
* sbomRef
* attestationRef
* CI workflow IDs
* reviewer identities

**Ledger is append-only.**

---

# 🧪 Validation Requirements

Required CI workflows:

| Workflow                   | Purpose                   |
| -------------------------- | ------------------------- |
| `lineage-validate.yml`     | Validate JSON-LD + schema |
| `faircare-validate.yml`    | CARE v2 & sovereignty     |
| `linked-data-validate.yml` | RDF + GeoSPARQL           |
| `telemetry-export.yml`     | Telemetry v2 compliance   |
| `docs-lint.yml`            | KFM Markdown protocol     |

Lineage bundles MUST pass:

* JSON Schema
* JSON-LD frame validation
* PROV-O structure
* GeoSPARQL
* CIDOC CRM (if used)
* CARE v2 governance

---

# 🧭 Local Build Pattern

```bash
python build_lineage.py \
  --input data/processed/<dataset>/<version> \
  --out data/processed/lineage/<dataset>/<version>.jsonld \
  --care-label sensitive \
  --attestation sdit/slsa.json \
  --include-telemetry
```

---

# 🪜 Example Lineage Bundle (Abbreviated)

```json
{
  "@context": [
    "https://www.w3.org/ns/prov.jsonld",
    "https://openspatial.org/contexts/geosparql.jsonld",
    "docs/contexts/kfm-care-v2.context.jsonld"
  ],
  "@id": "kfm:landsat_scene_2025_11_14_001",
  "@type": ["prov:Entity", "geo:Feature"],
  "geo:asWKT": "POLYGON((...))",
  "prov:wasGeneratedBy": "kfm:landsat_preprocess_2025_11_14",
  "prov:wasDerivedFrom": "kfm:landsat_ingest_2025_11_14",
  "kfm:checksum_sha256": "sha256-abc123...",
  "kfm:careLabel": "public",
  "kfm:telemetryRef": "data/processed/telemetry/landsat_ingest.ndjson"
}
```

---

# 🕰 Version History

| Version | Date       | Summary                                                                                                                             |
| ------: | ---------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| v10.4.2 | 2025-11-16 | Full v10.4.2 upgrade: CARE v2, Telemetry v2, CIDOC+PROV-O+GeoSPARQL integration, SLSA attestations, KFM-styled architecture diagram |
| v10.3.1 | 2025-11-14 | Initial lineage guide                                                                                                               |

---

<div align="center">

**Kansas Frontier Matrix — Lineage & Provenance Guide (v10.4.2)**
Immutable Provenance × FAIR+CARE v2 × PROV-O × CIDOC CRM × GeoSPARQL
© 2025 Kansas Frontier Matrix — CC-BY 4.0 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>
