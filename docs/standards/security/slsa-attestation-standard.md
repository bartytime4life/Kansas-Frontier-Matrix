---
title: "🧾 KFM v11 — SLSA & In-Toto Provenance Attestation Standard (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/security/slsa-attestation-standard.md"
version: "v11.0.0"
last_updated: "2025-11-23"
review_cycle: "Quarterly · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../releases/v11.0.0/security-audits-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/slsa-attestation-standard-v11.json"
governance_ref: "../governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active · Enforced"
doc_kind: "Security Standard"
semantic_document_id: "kfm-slsa-attestation-standard-v11"
doc_uuid: "urn:kfm:standards:security:slsa-attestation-standard:v11"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Medium-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 🧾 **KFM v11 — SLSA & In-Toto Provenance Attestation Standard**  
`docs/standards/security/slsa-attestation-standard.md`

**Purpose:**  
Define the **required structure, metadata, format, and validation rules** for SLSA-based and  
in-toto provenance attestations in KFM v11.  
Attestations cryptographically bind datasets, models, STAC assets, code artifacts, and pipeline outputs  
to the exact tools, inputs, environments, and code that produced them.

</div>

---

# 📘 1. Overview

This standard governs how KFM v11 records **verifiable provenance** for:

- Data ETL outputs  
- STAC Items & Collections  
- COG rasters  
- Parquet/NetCDF tables  
- ML/AI model artifacts  
- Story Node generation bundles  
- API + UI build artifacts  
- Full releases under `releases/<ver>/`  

It aligns with:

- **SLSA v1.0**  
- **in-toto** (link metadata)  
- **OpenLineage v2.5**  
- **SPDX SBOM Standard v11**  
- **Checksum ⇄ SBOM ⇄ Provenance Integration Standard**  
- **Data Integrity Standard v11**  
- **FAIR+CARE ethics constraints**

Attestations MUST be machine-verifiable, cryptographically signed (when supported), and  
exported as JSON.

---

# 🔐 2. Attestation Requirements (KFM v11)

Every artifact MUST have an attestation with:

| Field | Required | Description |
|-------|----------|-------------|
| `type` | ✔ | MUST be `slsa-provenance` or in-toto `link` |
| `subject[]` | ✔ | MUST contain artifact name + sha256 digest |
| `builder` | ✔ | Builder identity (`github-actions://…`, `kfm-autonomous-pipeline://…`, etc.) |
| `buildType` | ✔ | MUST reflect KFM pipeline type (`LangGraph v11 DAG`, containerized build, etc.) |
| `buildConfig` | ✔ | MUST detail pipeline, DAG node, tool versions |
| `metadata` | ✔ | MUST include start/end timestamps |
| `materials[]` | ✔ | MUST include upstream inputs, commit hashes, dependencies |
| `environment` | Recommended | Container digest, OS info, env vars (scrubbed) |
| `invocation` | Optional | Command-line, configs, params |

Attestations MUST be stored under:

```
releases/<ver>/attestations/<artifact>.slsa.json
```

---

# 📦 3. SLSA Subject Requirements

Each subject entry MUST contain:

```json
{
  "name": "data/processed/hydrology/statewide/gauges.parquet",
  "digest": {
    "sha256": "<hex>"
  }
}
```

Digest MUST exactly match:

- Checksum registry (`registry.jsonl`)  
- SBOM file entry  
- OpenLineage run output digest  

Mismatch → **CI FAILURE**.

---

# 🧬 4. Required Provenance Fields

### 4.1 Builder
```
"builder": {
  "id": "github-actions://kfm/pipelines@v11"
}
```

or for autonomous DAGs:

```
"builder": {
  "id": "kfm-autonomous-hydrology-refresh@v11"
}
```

### 4.2 BuildType
```
"https://slsa.dev/spec/v1.0/buildType/containerized"
```

### 4.3 BuildConfig
Must include:

- DAG name  
- Node name  
- Tool versions (GDAL, PROJ, Python, LangGraph version)  
- CRS + vertical-axis metadata  
- STAC version  
- Dataset schema version  
- AI model version (if applicable)

### 4.4 Metadata Block
```
"metadata": {
  "buildStartedOn": "2025-11-20T21:59:00Z",
  "buildFinishedOn": "2025-11-20T22:14:00Z"
}
```

### 4.5 Materials[]
Each MUST provide:

- Upstream dataset paths  
- Checksum digest(s)  
- Git commit ID  
- Container digest(s)  
- SPDX identifiers if already in SBOM  

---

# 🛰 5. Linkage to OpenLineage (Mandatory)

Attestations MUST reference the OpenLineage run that produced the artifact:

```json
"attributionTexts": [
  "OpenLineage: ../../docs/archives/provenance/chains/hydrology/streamflow/statewide/run-2025-11-20.json"
]
```

OpenLineage runs MUST include:

- Dataset input + output digests  
- DAG → node details  
- Execution timestamps  
- Runtime environment  
- Link to SLSA attestation  
- CRS + vertical-axis info for all geospatial transformations  

---

# 🔗 6. SBOM Cross-Reference (Mandatory)

The attestation MUST include an **ExternalRef** that points to:

- The SBOM element describing the artifact  
- The SBOM document itself  

Example:

```json
"externalRefs": [
  {
    "referenceCategory": "SECURITY",
    "referenceType": "other",
    "referenceLocator": "https://slsa.dev/attestation#json:../../releases/v11.0.0/attestations/gauges.parquet.slsa.json"
  }
]
```

Additionally, the SBOM MUST contain the inverse reference.

---

# 🔍 7. FAIR+CARE Attestation Requirements

All attestations MUST include CARE-aligned metadata when applicable:

```
"care": {
  "sensitivity": "L1|L2|L3|L4",
  "authority": "Tribal Nation Name",
  "consent_required": true|false,
  "masking_method": "h3-generalization|redaction"
}
```

Attestations MUST NOT reveal:

- Raw coordinates of L3/L4 Indigenous sites  
- Sensitive archaeological periods without masking  
- Unapproved lineage sources  

---

# 🧪 8. CI Validation Gates

CI **MUST** enforce:

### ✔ Schema Validation  
Attestation MUST conform to KFM v11 JSON schema (`slsa-attestation-v11.schema.json`).

### ✔ Checksum Verification  
`subject.digest.sha256` MUST match checksum registry.

### ✔ SBOM Cross-Reference  
SPDX element MUST exist and its checksum MUST match.

### ✔ Provenance Integrity  
All materials MUST reference existing, verifiable upstream assets.

### ✔ OpenLineage Synchronization  
Lineage run file MUST reference same digest as attestation.

### ✔ Ethical (FAIR+CARE) Validation  
Check that sensitive data references are masked or removed.

Failure of **any** gate → PR rejected.

---

# 🧭 9. Storage Structure (v11)

```
releases/
  v11.0.0/
    sbom.spdx.json
    manifest.zip
    registry.jsonl
    attestations/
      <artifact>.slsa.json
    provenance/
      <artifact>/lineage.json
```

All paths MUST be relative-safe and CI-resolvable.

---

# 🧱 10. Minimal SLSA Attestation Example (v11)

```json
{
  "type": "slsa-provenance",
  "subject": [
    {
      "name": "data/processed/hydrology/statewide/gauges.parquet",
      "digest": {"sha256": "<hex>"}
    }
  ],
  "builder": {"id": "github-actions://kfm/pipelines@v11"},
  "buildType": "https://slsa.dev/spec/v1.0/buildType/containerized",
  "buildConfig": {
    "pipeline": "LangGraph v11 DAG",
    "node": "hydrology-refresh/export",
    "tools": {
      "python": "3.11",
      "gdal": "3.8",
      "proj": "9.3",
      "langgraph": "v11"
    }
  },
  "metadata": {
    "buildStartedOn": "2025-11-20T21:59:00Z",
    "buildFinishedOn": "2025-11-20T22:14:00Z"
  },
  "materials": [
    {
      "uri": "git+https://github.com/bartytime4life/Kansas-Frontier-Matrix.git#<commit>",
      "digest": {"sha1": "<hex>"}
    }
  ]
}
```

---

# 🕰 11. Version History

- **v11.0.0 (2025-11-23)** — Initial SLSA & in-toto Attestation Standard.

---

<div align="center">

**Kansas Frontier Matrix — SLSA & In-Toto Provenance Standard (v11)**  
*Verifiable · Reproducible · Supply-Chain Safe*

</div>

---

### 🔗 Footer  
[⬅ Back to Security Standards](./README.md) · [📦 SBOM Standard](./sbom-standard.md) · [🔗 Checksum–SBOM–Provenance](./checksum-sbom-provenance.md) · [🏛 Governance](../governance/ROOT-GOVERNANCE.md)

