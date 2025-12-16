---
title: "🧭 KFM — Minimal OpenLineage→STAC/DCAT→Neo4j Mapping (Deterministic Core)"
path: "docs/standards/provenance/minimal-openlineage-stac-dcat-neo4j.md"
version: "v11.2.6"
last_updated: "2025-12-15"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council · Reliability Board"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Standard · Mapping Spec"
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

commit_sha: "<latest-commit-hash>"
signature_ref: "../../../releases/v11.2.6/signature.sig"

governance_ref: "../governance/ROOT-GOVERNANCE.md"
ethics_ref: "../faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../sovereignty/INDIGENOUS-DATA-PROTECTION.md"

semantic_document_id: "kfm-openlineage-minimal-mapping"
doc_uuid: "urn:kfm:prov:minimal:openlineage→stac-dcat-neo4j:v11.2.6"
event_source_id: "ledger:docs/standards/provenance/minimal-openlineage-stac-dcat-neo4j.md"
immutability_status: "version-pinned"

provenance_chain:
  - "docs/standards/provenance/minimal-openlineage-stac-dcat-neo4j.md@v11.2.6"
provenance_requirements:
  versions_required: true
  newest_first: true

classification: "Public Standard"
sensitivity_level: "Low"
fair_category: "F1-A1-I2-R2"
care_label: "Responsible · Stewardship · Ethics"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "metadata-extraction"
ai_transform_prohibited:
  - "summaries"
  - "speculative-additions"
  - "unverified-historical-claims"
  - "governance-override"
  - "content-alteration"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "Quarterly review"
sunset_policy: "Superseded upon next provenance protocol revision"
jurisdiction: "Kansas / United States"
---

# 🧭 KFM — Minimal OpenLineage→STAC/DCAT→Neo4j Mapping

## 📘 Overview

This standard defines a **minimal, storage-efficient** OpenLineage payload plus its **deterministic, governance-safe mappings** into:

- **STAC** (Item/Asset properties + links) for spatiotemporal catalogs
- **DCAT** (Dataset/Distribution fields + provenance links) for data catalogs
- **Neo4j** (queryable lineage subgraph) for graph-native provenance queries

### Design goals

- **Deterministic reproducibility**: identical inputs + code + config → stable identity & derivation signals.
- **Small “load-bearing core”**: store only what is required for traceability, versioning, and replay.
- **Lossless lineage** by reference: the **authoritative OpenLineage event JSON** is retained verbatim in the provenance store; STAC/DCAT/Neo4j carry **compact references + stable keys**.
- **Governance-safe**: no PII, no secret material, and no precision leaks (especially around sensitive/sovereign locations).

### Load‑bearing fields (deterministic core)

The deterministic core is the smallest set of fields required to:

1) identify the run,
2) identify the job,
3) identify output version,
4) prove derivation from inputs,
5) anchor the event in time.

**Core fields:**
- `run.runId`
- `run.facets.kfmRepro.datasetVersion`
- `run.facets.kfmRepro.derivationHash`
- `inputs[].facets.dataQuality.checksums[]` (at minimum `sha256:*`)
- `producer` (producerNamespace)
- `job.namespace` + `job.name` (jobName)
- `eventTime`

### Normative language

The key words **MUST**, **MUST NOT**, **SHOULD**, and **MAY** are to be interpreted as normative requirements.

---

## 🗂️ Directory Layout

This spec maps into existing KFM repo subsystems (schemas, tools, data catalogs, graph loaders). The following layout is normative at the directory level; file names may vary per pipeline.

~~~text
docs/
└── standards/
    └── provenance/
        └── minimal-openlineage-stac-dcat-neo4j.md      # This standard (v11.2.6)

data/
├── provenance/                                         # Provenance store (authoritative OpenLineage JSON)
│   ├── openlineage/                                    # One JSON event per state transition
│   └── prov/                                           # Optional: derived PROV JSON-LD view(s)
└── stac/                                               # STAC collections & items (catalog)

schemas/
├── json/                                               # JSON schemas for docs, pipelines, metadata
├── shacl/                                              # SHACL shapes (DCAT/PROV profiles where used)
└── telemetry/                                          # Telemetry schemas incl. lineage formats

tools/
└── validation/                                         # STAC/DCAT schema checks and validators

src/
└── graph/                                              # Neo4j schema, loaders, and query scripts

releases/
└── v11.2.6/                                            # Versioned release packages (manifest/SBOM/attestation/signature)
~~~

---

## 🧭 Context

KFM uses a “standards-first” publishing model:

- Data moves from **raw → work/staging → processed**; promotion is blocked unless validation and governance gates pass.
- Catalogs (STAC/DCAT) and provenance are treated as **first-class artifacts** alongside data assets and releases.
- Provenance is expected to be **queryable in Neo4j**, not just stored as logs.

This standard supports the KFM pattern where:
- provenance is written to a store under `data/provenance/`,
- and then indexed into Neo4j to be queryable and joinable with datasets/entities (e.g., dataset-to-output-to-site relationships).

---

## 🧱 Architecture

### 1) Authoritative storage rule

1. The **OpenLineage event JSON** is the authoritative record.
2. STAC/DCAT/Neo4j are **derived views** and MUST preserve the ability to reference back to the authoritative event.

### 2) Event emission (minimal OpenLineage)

Pipelines MUST emit **one OpenLineage JSON event per transition**:

- `START`
- `COMPLETE`
- `FAIL`
  - (KFM may use `FAILURE` if aligned with upstream libraries; if so, the mapping rules remain identical)

The emission MUST include the deterministic core fields (above). Anything else is optional.

#### Minimal OpenLineage event example (v11.2.6)

~~~json
{
  "eventType": "COMPLETE",
  "eventTime": "2025-12-15T03:00:00Z",
  "producer": "urn:ns:kfm:etl",
  "job": {
    "namespace": "kfm/etl/soils",
    "name": "gnatsgo→h3-index→stac",
    "facets": {
      "documentation": { "url": "https://…/docs/etl/soils" }
    }
  },
  "run": {
    "runId": "7f3a2c9a-39e0-4e75-9c71-6b3b9e9d2a54",
    "facets": {
      "kfmRepro": {
        "datasetVersion": "v2025.12.15-01",
        "derivationHash": "sha256:af…",
        "seed": 42,
        "containerImage": "ghcr.io/kfm/etl@sha256:…",
        "git": { "repo": "kfm.git", "ref": "refs/tags/v11.2.6", "commit": "abc123…" }
      }
    }
  },
  "inputs": [
    {
      "namespace": "kfm/raw/usda",
      "name": "gnatsgo.tif",
      "facets": { "dataQuality": { "checksums": ["sha256:e1…", "blake3:9f…"] } }
    }
  ],
  "outputs": [
    {
      "namespace": "kfm/derived/soils",
      "name": "gnatsgo_h3.parquet",
      "facets": {
        "version": { "datasetVersion": "v2025.12.15-01" },
        "dataQuality": { "checksums": ["sha256:77…"] }
      }
    }
  ]
}
~~~

### 3) Deterministic identifiers (KFM canonicalization)

This mapping defines canonical IDs used across STAC/DCAT/Neo4j. The goal is stable joins without duplicating large blobs.

#### Canonical strings

- `producerNamespace` := `producer`
- `jobKey` := `${job.namespace}::${job.name}`
- `datasetKey` := `${dataset.namespace}::${dataset.name}`
- `datasetVersion` := `run.facets.kfmRepro.datasetVersion` (for outputs) and/or `outputs[].facets.version.datasetVersion`

#### Canonical URNs

Implementations MUST mint URNs deterministically, using stable, normalized strings:

- `runUrn` := `urn:kfm:prov:run:${run.runId}`
- `jobUrn` := `urn:kfm:prov:job:${sha256(jobKey)}`
- `datasetUrn` := `urn:kfm:data:${sha256(datasetKey)}`
- `datasetVersionUrn` := `urn:kfm:data:${sha256(datasetKey)}#${datasetVersion}`

**Normalization rules**
- Unicode NFC normalization
- trim outer whitespace
- preserve case (do not lower-case identifiers)
- arrays used for hashing MUST be stably sorted

### 4) Derivation hash constraints

`derivationHash` MUST:
- be computed from **inputs + code identity + params**,
- be stable across hosts/CI nodes,
- **exclude** `runId` and `eventTime` (both are run-unique, not derivation-unique).

If a pipeline cannot compute a stable `derivationHash`, it MUST NOT claim deterministic compliance.

---

## 🌐 STAC, DCAT & PROV Alignment

### A) OpenLineage → STAC mapping (minimal)

STAC is used for spatiotemporal cataloging; this mapping only adds **compact lineage references**, not full provenance graphs.

#### Where lineage goes in STAC

- **STAC Item**: stores run + derivation identity as compact properties and a provenance link.
- **STAC Asset**: stores checksum and (optionally) a run reference.

#### Required STAC properties (KFM lineage extension)

| OpenLineage field | STAC location | Required | Notes |
|---|---|:---:|---|
| `run.runId` | `item.properties["kfm:lineage_run_id"]` | ✔ | Join key to provenance store and Neo4j run node |
| `run.facets.kfmRepro.datasetVersion` | `item.properties["kfm:dataset_version"]` | ✔ | Version string for output set |
| `run.facets.kfmRepro.derivationHash` | `item.properties["kfm:derivation_hash"]` | ✔ | Deterministic content-derivation identity |
| `producer` | `item.properties["kfm:producer"]` | ✔ | Producer namespace |
| `job.namespace` + `job.name` | `item.properties["kfm:job_key"]` | ✔ | `${namespace}::${name}` |
| `eventTime` | `item.properties["kfm:lineage_event_time"]` | ✔ | Time anchor for the lineage event |
| `inputs[].checksums` | by reference only | ✔ | Do not embed full lists unless required; reference provenance store |

#### Required STAC links

STAC Items MUST include a provenance link that resolves to the authoritative OpenLineage event:

~~~json
{
  "rel": "provenance",
  "type": "application/json",
  "href": "../../provenance/openlineage/7f3a2c9a-39e0-4e75-9c71-6b3b9e9d2a54/COMPLETE.json"
}
~~~

#### Asset checksum mapping

For each output asset, at minimum:

- `outputs[].facets.dataQuality.checksums` → `item.assets[assetKey].extra_fields["kfm:checksums"]`

~~~json
{
  "assets": {
    "data": {
      "href": "…/gnatsgo_h3.parquet",
      "type": "application/x-parquet",
      "roles": ["data"],
      "extra_fields": {
        "kfm:checksums": ["sha256:77…"],
        "kfm:lineage_run_id": "7f3a2c9a-39e0-4e75-9c71-6b3b9e9d2a54"
      }
    }
  }
}
~~~

### B) OpenLineage → DCAT mapping (minimal)

DCAT provides catalog-level interoperability. This mapping focuses on Dataset/Distribution identity, checksum integrity, and provenance linking.

#### Minimal DCAT mapping rules

| OpenLineage field | DCAT target | Required | Notes |
|---|---|:---:|---|
| `outputs[].namespace + outputs[].name` | `dcat:Dataset` identity | ✔ | Dataset identity (stable across versions) |
| `datasetVersion` | `dcat:Distribution` version | ✔ | Version string |
| output checksums | `dcat:Distribution` checksum | ✔ | Attach checksum(s) per distribution |
| `runId` | `dcterms:provenance` link target | ✔ | Join to provenance record |
| `derivationHash` | `dcterms:provenance` or extension | ✔ | Deterministic derivation identity |

#### Example DCAT JSON-LD fragment (conceptual)

~~~json
{
  "@type": "dcat:Dataset",
  "@id": "urn:kfm:data:…",
  "dcat:distribution": [
    {
      "@type": "dcat:Distribution",
      "@id": "urn:kfm:data:…#v2025.12.15-01",
      "dcat:downloadURL": "…/gnatsgo_h3.parquet",
      "dcterms:hasVersion": "v2025.12.15-01",
      "dcterms:provenance": {
        "@id": "urn:kfm:prov:run:7f3a2c9a-39e0-4e75-9c71-6b3b9e9d2a54"
      }
    }
  ]
}
~~~

### C) OpenLineage → PROV-O mapping (KFM-PROV v11 minimal)

The PROV model is the semantic bridge that makes lineage joinable across catalogs and graphs.

#### Minimal PROV correspondences

- OpenLineage `run` → `prov:Activity`
- OpenLineage `inputs[]` / `outputs[]` → `prov:Entity`
- OpenLineage `producer` / job identity → `prov:Agent` (software/system agent)
- OpenLineage relationships:
  - inputs: `prov:used`
  - outputs: `prov:wasGeneratedBy`
  - producer association: `prov:wasAssociatedWith`
  - revision/versioning: `prov:wasRevisionOf` (optional but recommended for dataset series)

---

## ⚖ FAIR+CARE & Governance

### Non-negotiable safety constraints

Provenance payloads and derived mappings MUST NOT:

- embed secrets, credentials, or internal network identifiers
- include PII
- leak precise coordinates for sensitive/sovereign resources

### Precision & sovereignty handling

If an output dataset (or its derived catalog entry) is sensitive, the catalog layer MUST carry explicit “representation” semantics.

KFM uses the pattern:

- `kfmarch:location_representation = "generalized-region"` (or analogous controlled values)
- geometry/bbox may be generalized; provenance remains intact but must not imply precision

### Governance metadata in lineage

Pipelines SHOULD include governance flags at the run-level (as a facet or parallel record), but MUST ensure those flags are authored by the governance layer (not inferred).

---

## 🧠 Story Node & Focus Mode Integration

This mapping supports UI and explainability paths that need stable provenance joins without bloating UI payloads:

- Story/Focus panels can show “why you’re seeing this” by resolving:
  1) dataset or entity → linked STAC/DCAT record
  2) STAC/DCAT record → `kfm:lineage_run_id`
  3) `runId` → Neo4j run node and/or the authoritative OpenLineage JSON

Implementations SHOULD provide:
- a consistent “Provenance” affordance (chip/link)
- a governance notice when any masking/generalization is in effect

---

## 🧪 Validation & CI/CD

### Required validations (CI-blocking)

1) **OpenLineage minimal schema check**
- event has required core fields
- checksum strings are valid `algo:value` forms (at minimum sha256)

2) **STAC validation**
- STAC Items remain valid against pinned validators
- lineage extension fields do not break STAC JSON structure

3) **DCAT/PROV validation**
- DCAT output validates against KFM-DCAT profile (SHACL where used)
- PROV view validates against KFM-PROV expectations (shape checks where used)

4) **Neo4j ingestion validation**
- run, job, entity nodes and core relationships are present and queryable
- runId joins work (STAC/DCAT → graph)

5) **Governance checks**
- no precision leak
- no restricted geometries exposed
- no PII present in provenance or derived catalog fields

### Determinism checks

Pipelines SHOULD include a repeat-run test where:
- same inputs + same code + same config produce the same `derivationHash`
- output checksums match
- the only expected differences are `runId` and timestamps

---

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A["Pipeline step"] --> B["Emit OpenLineage event JSON"]
  B --> C["Provenance store data/provenance"]
  C --> D["Derive STAC Item and Asset lineage fields"]
  C --> E["Derive DCAT Dataset and Distribution provenance links"]
  C --> F["Ingest lineage into Neo4j"]
  D --> G["Catalog browse and search"]
  E --> G
  F --> H["Graph queries for lineage and evidence"]
  G --> I["UI can resolve provenance by runId"]
  H --> I
~~~

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-15 | Standardized the minimal deterministic core fields and the compact, governance-safe mappings into STAC/DCAT/Neo4j. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0

**Governance Links**  
[Docs Root](../../../README.md) •
[Standards Index](../INDEX.md) •
[Governance Charter](../governance/ROOT-GOVERNANCE.md)

**Compliance**  
KFM-MDP v11.2.6 • KFM-PROV v11 • KFM-STAC v11 • KFM-DCAT v11 • PROV-O • FAIR+CARE • Sovereignty Policy

**End of Document**

</div>