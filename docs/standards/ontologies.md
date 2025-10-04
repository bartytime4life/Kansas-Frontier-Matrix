<div align="center">

# 🧠 Kansas Frontier Matrix — Ontology & Semantic Standards  
`docs/standards/ontologies.md`

**Purpose:** Define and document the **semantic ontologies and data models** used to describe  
entities, relationships, and provenance in the **Kansas Frontier Matrix (KFM)** knowledge ecosystem.  
These standards ensure that all metadata, datasets, and knowledge graph elements are **interoperable,  
machine-readable, and MCP-aligned** for transparent provenance and reproducible research.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)

</div>

---

## 📚 Overview

The KFM knowledge architecture uses **semantic web and ontology frameworks** to unify datasets,  
models, and documents into a single **provenance-aware knowledge graph**.

Ontologies define:
- 🧩 **What entities exist** (datasets, events, people, places, documents)  
- 🔗 **How they relate** (derived from, located in, authored by, observed during)  
- 🧠 **What standards govern** their meaning (CIDOC CRM, PROV-O, STAC, etc.)  

These ontologies allow data integration across disciplines — connecting **geospatial**, **historical**,  
and **scientific** records within one interoperable model.

---

## 🧩 Core Ontologies & Vocabularies

| Ontology / Standard | Namespace Prefix | Purpose | Source |
|:---------------------|:-----------------|:----------|:---------|
| **CIDOC CRM (v7.1)** | `crm:` | Models cultural heritage and event-based data relationships (e.g., events, actors, places). | [CIDOC CRM](https://www.cidoc-crm.org/) |
| **W3C PROV-O** | `prov:` | Describes provenance, derivation, and workflow lineage of data and models. | [W3C PROV-O](https://www.w3.org/TR/prov-o/) |
| **STAC (v1.0.0)** | `stac:` | Defines geospatial metadata and catalog relationships for datasets and assets. | [STAC Spec](https://stacspec.org) |
| **Dublin Core (DCMI)** | `dc:` | Basic descriptive metadata: title, creator, subject, date, and license. | [Dublin Core](https://dublincore.org/specifications/dublin-core/dcmi-terms/) |
| **OWL-Time** | `time:` | Models temporal intervals and events. | [OWL-Time](https://www.w3.org/TR/owl-time/) |
| **GeoSPARQL (OGC)** | `geo:` | Represents spatial geometry and relationships in RDF. | [OGC GeoSPARQL](https://www.ogc.org/standards/geosparql) |
| **SKOS** | `skos:` | Organizes taxonomies, controlled vocabularies, and themes. | [W3C SKOS](https://www.w3.org/TR/skos-reference/) |
| **MCP Vocabulary** | `mcp:` | Custom extension defining reproducibility, auditability, and build lineage metadata. | Internal (KFM-defined) |

---

## 🧠 KFM Semantic Model Overview

The Kansas Frontier Matrix ontology layer integrates **spatial**, **temporal**, and **provenance** models  
to represent complex relationships across datasets and entities.

```mermaid
erDiagram
  DATASET ||--o{ METADATA : "described_by"
  DATASET ||--o{ CHECKSUM : "verified_by"
  DATASET ||--o{ SOURCE : "derived_from"
  DATASET ||--o{ EVENT : "observed_during"
  EVENT ||--o{ PLACE : "took_place_at"
  DOCUMENT ||--o{ PERSON : "authored_by"
  DOCUMENT ||--o{ EVENT : "mentions"
  DATASET ||--o{ COLLECTION : "member_of"
````

<!-- END OF MERMAID -->

---

## 🧬 Semantic Mapping (RDF Triples)

Example RDF Turtle representation of a dataset and its provenance relationships:

```turtle
@prefix crm: <http://www.cidoc-crm.org/cidoc-crm/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix stac: <https://stacspec.org/v1.0.0/schema#> .
@prefix time: <http://www.w3.org/2006/time#> .
@prefix dc: <http://purl.org/dc/terms/> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix mcp: <https://kfm.org/vocab/mcp#> .

<dataset:ks_1m_dem_2018_2020>
    a crm:E73_Information_Object, stac:Item ;
    dc:title "Kansas 1m DEM (2018–2020)" ;
    prov:wasDerivedFrom <source:usgs_3dep_dem> ;
    geo:hasGeometry <geometry:kansas_extent> ;
    time:hasBeginning "2018-01-01T00:00:00Z"^^xsd:dateTime ;
    time:hasEnd "2020-12-31T23:59:59Z"^^xsd:dateTime ;
    mcp:checksumVerified true ;
    mcp:buildCommit "a93f2c4" ;
    prov:wasGeneratedBy <process:terrain_pipeline> ;
    crm:P7_took_place_at <place:Kansas> .
```

---

## 🧩 Ontology Relationships (CIDOC CRM x PROV-O x STAC)

| Relationship               | Subject    | Predicate                             | Object     | Description                            |
| :------------------------- | :--------- | :------------------------------------ | :--------- | :------------------------------------- |
| Dataset Derived From       | `DATASET`  | `prov:wasDerivedFrom`                 | `SOURCE`   | Tracks parent dataset lineage.         |
| Dataset Observed During    | `DATASET`  | `crm:P12_occurred_in_the_presence_of` | `EVENT`    | Links dataset to recorded event.       |
| Dataset Created By         | `DATASET`  | `prov:wasGeneratedBy`                 | `PROCESS`  | Identifies pipeline or ETL process.    |
| Document Authored By       | `DOCUMENT` | `crm:P94_has_created`                 | `PERSON`   | Links historical documents to authors. |
| Place of Observation       | `EVENT`    | `crm:P7_took_place_at`                | `PLACE`    | Maps events to geographic areas.       |
| Metadata Linked To Dataset | `DATASET`  | `stac:described_by`                   | `METADATA` | Binds data to its STAC item.           |
| Validation Record          | `DATASET`  | `mcp:validated_by`                    | `CHECKSUM` | Connects dataset to integrity record.  |

---

## 🧩 KFM Custom MCP Vocabulary (Internal Extension)

To support **reproducibility and validation tracking**, the KFM ontology defines custom MCP predicates.

| Term                   | Type         | Description                                                    |
| :--------------------- | :----------- | :------------------------------------------------------------- |
| `mcp:checksumVerified` | Boolean      | Indicates whether checksum validation succeeded.               |
| `mcp:buildCommit`      | String       | Git commit hash associated with build or validation.           |
| `mcp:processedBy`      | Resource     | Link to the ETL script or workflow responsible for generation. |
| `mcp:validatedBy`      | Resource     | Link to workflow or CI/CD validation event.                    |
| `mcp:documentation`    | Resource     | Reference to README, SOP, or experiment documentation.         |
| `mcp:auditedBy`        | Agent        | Name or identifier of the reviewer or auditor.                 |
| `mcp:timestamp`        | xsd:dateTime | Timestamp of validation or review event.                       |

Example extension in RDF:

```turtle
<dataset:ks_1m_dem_2018_2020>
    mcp:validatedBy <workflow:stac_validate_yml> ;
    mcp:auditedBy <person:data_governance_team> ;
    mcp:timestamp "2025-10-04T10:30:00Z"^^xsd:dateTime .
```

---

## 🧩 File Storage & Integration

| Component                | Format                    | Directory               | Purpose                                  |
| :----------------------- | :------------------------ | :---------------------- | :--------------------------------------- |
| **Ontology Definitions** | `.ttl`, `.rdf`, `.jsonld` | `data/ontologies/`      | Stores base and extended ontology files. |
| **Graph Data Exports**   | `.ttl`, `.csv`, `.neo4j`  | `data/knowledge_graph/` | Knowledge graph serialization outputs.   |
| **RDF Validation Logs**  | `.log`, `.json`           | `data/work/logs/graph/` | Validation output from RDF parsers.      |

---

## 🧾 Validation Tools & CI/CD Integration

| Validation Type           | Tool                                   | Description                                              |
| :------------------------ | :------------------------------------- | :------------------------------------------------------- |
| **RDF Syntax Validation** | `rapper`, `rdflib`                     | Ensures RDF/Turtle syntax correctness.                   |
| **Ontology Reasoning**    | `owlrl`, `pySHACL`                     | Validates class relationships and reasoning consistency. |
| **SPARQL Tests**          | `jena`, `GraphDB`                      | Confirms query accessibility and expected relationships. |
| **CI/CD Workflow**        | `.github/workflows/graph-validate.yml` | Automates graph validation on each merge.                |

Example command:

```bash
python src/utils/validate_rdf.py data/ontologies/kfm.ttl
```

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                          |
| :---------------------- | :---------------------------------------------------------------------- |
| **Documentation-first** | Ontologies and vocabularies are documented before implementation.       |
| **Reproducibility**     | All semantic entities are machine-readable and version-controlled.      |
| **Open Standards**      | Uses CIDOC CRM, PROV-O, STAC, and W3C RDF specifications.               |
| **Provenance**          | All relationships explicitly model lineage, validation, and authorship. |
| **Auditability**        | RDF validation and reasoning logs stored for traceable verification.    |

---

## 📎 Related Documentation

| File                                   | Description                                           |
| :------------------------------------- | :---------------------------------------------------- |
| `docs/architecture/knowledge-graph.md` | Describes knowledge graph architecture and RDF model. |
| `docs/templates/provenance.md`         | Provenance record template linked to MCP ontology.    |
| `docs/standards/metadata.md`           | Defines metadata schemas aligned with STAC + PROV-O.  |
| `.github/workflows/graph-validate.yml` | Automated graph validation workflow.                  |

---

## 📅 Version History

| Version | Date       | Author                       | Summary                                                        |
| :------ | :--------- | :--------------------------- | :------------------------------------------------------------- |
| v1.0    | 2025-10-04 | KFM Ontology & Metadata Team | Initial ontology and semantic standards documentation for KFM. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Connecting Knowledge Across Time, Space, and Data.”*
📍 [`docs/standards/ontologies.md`](.) · Official ontology and semantic standards guide for MCP-compliant knowledge integration in the Kansas Frontier Matrix.

</div>
