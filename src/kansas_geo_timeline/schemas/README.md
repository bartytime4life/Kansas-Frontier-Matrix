# Kansas Geo Timeline — Schemas

This directory contains **formal schemas** (JSON/YAML/GraphQL) used to validate and standardize
all structured data in the **Kansas Geo Timeline / Kansas-Frontier-Matrix** stack.

Schemas ensure:
- **Scientific rigor & reproducibility** — every dataset and document follows a well-defined structure.
- **Cross-disciplinary interoperability** — history, cartography, geology, archaeology, and environmental datasets can be ingested, linked, and compared.
- **Future-proof extensibility** — new data sources (e.g., oral histories, paleoclimate records, AI-extracted features) can be added by extending existing schemas.

---

## Contents

- **`stac/`**  
  JSON Schema validators for **STAC 1.0.0** (Catalog → Collections → Items).  
  Define how historical maps, rasters (COGs), and vector layers are cataloged (provenance, spatial/temporal extents, checksums).

- **`sources/`**  
  YAML/JSON schemas for geospatial source descriptors (e.g., USGS, KGS, TopoView).  
  Required metadata: `id`, `title`, `url`, `format`, `license`, temporal & spatial coverage.

- **`entities/`**  
  JSON Schemas for **knowledge graph nodes**:  
  `Person`, `Organization`, `Place`, `Event`, `Document`.  
  Core attributes, relationships, and optional confidence/uncertainty fields.

- **`experiments/`**  
  Templates for documenting reproducible research experiments:  
  Problem → Hypothesis → Method → Variables → Data → Results → Conclusion.

---

## Workflow Integration

1. **Ingestion** — Raw sources (maps, PDFs, CSVs, scanned docs) are parsed (OCR/NLP) and normalized against these schemas.  
2. **Validation** — STAC metadata, source configs, and extracted entities are validated against their respective schemas.  
3. **Knowledge Graph** — Validated entities/relations (Person–Place–Event) are inserted into the graph DB with provenance and confidence.  
4. **Visualization** — MapLibre / Google Earth / timeline UI read only validated data for overlays and story maps.

---

## System Flow (Mermaid)

> GitHub renders Mermaid diagrams inside triple-backtick code fences with `mermaid` as the language.

```mermaid
flowchart TD
  A[Source Uploads\n(PDF • CSV • Images • HTML)] --> B[Ingestion Pipeline]
  B --> C[Text Extraction / OCR]
  C --> D[NLP • NER • Geocoding]
  D --> E[Normalization & Dedup]
  E --> F{Validate Against Schemas}

  subgraph Schemas
    S1[STAC\n(stac/)]
    S2[Source Descriptors\n(sources/)]
    S3[Entities\n(entities/)]
  end

  F -->|STAC| S1
  F -->|Sources| S2
  F -->|Entities| S3

  S1 --> J[Knowledge Graph]
  S2 --> J
  S3 --> J

  J --> K[APIs\nREST / GraphQL]
  K --> L[UI\nMaps • Timeline • Story Maps]
  L --> M[Research & Insight]
  K --> N[CI/CD\nSchema Tests]


⸻

Design Notes
	•	Documentation-first: Every schema includes a short spec and examples.
	•	Versioned: Semantic versioning (e.g., person.schema.v1.1.json).
	•	Extensible: Add new node/layer types via non-breaking extensions.
	•	Debuggable: examples/ and tests/ folders per schema; CI validates on PRs.

⸻

Next Steps
	•	Add uncertainty models (confidence, error bounds) across entity/event schemas.
	•	Expand environmental schemas (paleoclimate, erosion, fire regimes).
	•	Generate GraphQL bindings from entity schemas for interactive queries.
	•	Add a schema coverage badge in CI (files validated / total).

