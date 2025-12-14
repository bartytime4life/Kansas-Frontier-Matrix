---
title: "🧬 Surficial Geology — PROV Lineage Exports"
path: "data/surficial-geology/lineage/prov/README.md"
version: "v0.1.0"
last_updated: "2025-12-14"

governance_ref: "governance/ROOT-GOVERNANCE.md"
ethics_ref: "faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "CC-BY 4.0"
classification: "Public"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"

commit_sha: "<latest-commit-hash>"
provenance_chain: []

doc_uuid: "urn:kfm:doc:data:surficial-geology:lineage:prov:readme:v0.1.0"
semantic_document_id: "kfm-data-surficial-geology-lineage-prov-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:data:surficial-geology:lineage:prov:readme:v0.1.0"

ai_transform_permissions:
  - "summary"
  - "metadata-extraction"
  - "semantic-highlighting"
  - "timeline-generation"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"
---

# 🧬 PROV Lineage Exports

`data/surficial-geology/lineage/prov/`

**Purpose**  
Store machine-readable provenance exports (W3C PROV / PROV-O aligned) that describe *how* Surficial Geology artifacts in this repo were produced, by *which* run, from *which* inputs, using *which* tools/configs.

## 📘 Overview

This directory contains run-scoped PROV exports intended for:

- reproducibility audits (what was generated, from what, and when),
- governance review (what transformations occurred, at what sensitivity),
- downstream ingestion (mapping Entities/Activities/Agents into the KFM graph),
- crosswalk with other lineage outputs (e.g., OpenLineage events and run manifests).

**Immutability expectation**  
Treat run exports as immutable artifacts. If a run must be corrected, emit a new run and new PROV export rather than editing prior run artifacts in-place.

## 🗂️ Directory Layout

~~~text
data/surficial-geology/lineage/prov/
├── README.md
├── run_<run_id>.prov.jsonld
├── run_<run_id>.prov.ttl
├── run_<run_id>.prov.json
└── run_<run_id>.checksums.sha256
~~~

**Notes**

- `run_<run_id>` matches the lineage run identifier used across `data/surficial-geology/lineage/**`.
- Multiple serializations may exist for the same run (e.g., JSON-LD for graph ingestion, Turtle for review, PROV-JSON for tooling).
- `checksums.sha256` is recommended for verifying export integrity and supporting reproducible rebuilds.

## 📦 Data & Metadata

Recommended minimum content for each run export:

- **Entities**: source inputs, intermediate artifacts, final outputs (rasters, vectors, tiles, STAC records, metadata bundles)
- **Activities**: each deterministic pipeline step (ingest, normalize, reproject, tile, vectorize, validate, package)
- **Agents**: pipeline runner (script/service), maintainers (role-based), and CI identity (when applicable)
- **Key relations**:
  - `prov:used` (Activity → Entity inputs)
  - `prov:wasGeneratedBy` (Entity → Activity producing step)
  - `prov:wasAssociatedWith` (Activity → Agent)
  - `prov:wasDerivedFrom` (Entity → Entity lineage)
  - timestamps and checksums where available (avoid secrets)

File naming guidance:

- Prefer stable, parseable filenames:
  - `run_<run_id>.prov.jsonld`
  - `run_<run_id>.prov.ttl`
  - `run_<run_id>.prov.json`
- Keep `<run_id>` consistent with the run manifest identifier (see sibling lineage directories).

## 🌐 STAC, DCAT & PROV Alignment

This PROV output is designed to align with KFM cataloging:

- **STAC**: outputs referenced in STAC Items/Collections should be representable as `prov:Entity` instances with stable identifiers.
- **DCAT**: dataset-level records may map to higher-level `prov:Entity` groupings (e.g., “Surficial Geology vectors vX”).
- **PROV-O**: run exports should support a direct ingest path into Neo4j as provenance subgraphs (Entities/Activities/Agents).

## ⚖ FAIR+CARE & Governance

- Do **not** include secrets, tokens, private URLs, or credentials in PROV exports.
- Do **not** embed sensitive locations at higher precision than permitted by policy; prefer generalized geometry references when required.
- When an output is governed/restricted, provenance should still exist but may need **masking/generalization** (e.g., reference an abstracted place identifier rather than precise coordinates).

## 🧪 Validation & CI/CD

Recommended checks for this directory’s contents:

- filename conventions and run-id consistency (across lineage artifacts),
- checksum presence/format when provided,
- basic PROV structural validity (Entities/Activities/Agents are well-formed),
- no secrets/PII leakage in exported text.

## 🕰️ Version History

- `v0.1.0` (2025-12-14): Initial directory README.

---

<div align="center">

**Surficial Geology — PROV Lineage Exports** · `data/surficial-geology/lineage/prov/README.md`  
Governed KFM lineage documentation (FAIR+CARE + sovereignty aligned).

[🏛️ Governance Charter](/docs/standards/governance/ROOT-GOVERNANCE.md) · [⚖ FAIR+CARE Guide](/docs/standards/faircare/FAIRCARE-GUIDE.md) · [🪶 Indigenous Data Protection](/docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© Kansas Frontier Matrix · CC‑BY 4.0

</div>

