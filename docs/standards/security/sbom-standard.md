---
title: "📦 KFM v11 — SPDX SBOM Standard (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/security/sbom-standard.md"
version: "v11.0.0"
last_updated: "2025-11-23"
review_cycle: "Quarterly · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../releases/v11.0.0/security-audits-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/security-sbom-standard-v11.json"
governance_ref: "../governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active · Enforced"
doc_kind: "Security Standard"
semantic_document_id: "kfm-sbom-standard-v11"
doc_uuid: "urn:kfm:standards:security:sbom-standard:v11"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Medium-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 📦 **KFM v11 — SPDX SBOM Standard**  
`docs/standards/security/sbom-standard.md`

**Purpose:**  
Define the mandatory structure, metadata, validation rules, and governance controls for **SPDX SBOM files**  
in the Kansas Frontier Matrix.  
Ensures all data, code, pipelines, models, and release artifacts have fully cryptographically verifiable  
software bills of materials that align with checksum registries, provenance attestations, and FAIR+CARE ethics.

</div>

---

# 📘 1. Overview

The **SPDX SBOM Standard** governs:

- The creation and validation of **SBOM files** (`sbom.spdx.json`)  
- Mapping **checksums → SPDX Elements**  
- Cross-linking **SPDX → SLSA provenance**  
- Ensuring all artifacts appear in the SBOM and can be resolved  
- Integration with **OpenLineage**, **Data Contract v3**, and **FAIR+CARE** ethics rules  

This ensures transparent, reproducible, audit-ready releases for scientific + historical data.

---

# 📦 2. SBOM Requirements (SPDX 2.3)

The SBOM MUST:

- Use **SPDX 2.3 JSON** format  
- Contain **SPDXID** entries for:
  - STAC Items  
  - COG rasters  
  - Parquet/CSV/NetCDF  
  - AI/ML models + embeddings  
  - Story Nodes (narrative bundles)  
  - Pipeline containers  
  - Any artifact in `/releases/<ver>/`  
- Include all **hashes** stored in the checksum registry  
- Include **ExternalRefs** to:
  - SLSA attestations  
  - Provenance chains  
  - OpenLineage runs  
- Use **absolute or stable relative paths**  
- Include all **licenses** (SPDX-recognized identifiers)

---

# 🔗 3. Required Fields in Every SPDX File Entry

Each `File` entry MUST include:

```json
{
  "SPDXID": "SPDXRef-File-<id>",
  "fileName": "<relative/path/to/artifact>",
  "checksums": [
    {"algorithm": "SHA256", "checksumValue": "<hex>"},
    {"algorithm": "SHA512", "checksumValue": "<hex>"}
  ],
  "licenseConcluded": "MIT OR CC-BY-4.0 OR NOASSERTION",
  "attributionTexts": [
    "Provenance: <relative/path/to/attestation.slsa.json>",
    "OpenLineage: <relative/path/to/lineage.json>"
  ],
  "externalRefs": [
    {
      "referenceCategory": "SECURITY",
      "referenceType": "other",
      "referenceLocator": "https://slsa.dev/attestation#json:<attestation-path>"
    }
  ]
}
```

Additional required fields:

| Field | Requirement |
|-------|------------|
| `fileType` | MUST reflect actual artifact type |
| `verificationCode` | MUST be computed unless SPDX spec prohibits |
| `copyrightText` | `NOASSERTION` unless known |

---

# 🧬 4. SBOM → Checksum Registry Alignment (Mandatory)

For every artifact in the release:

- Its **checksums in the SBOM** MUST match the **checksum registry**  
- Its `SPDXID` MUST be referenced by the registry row as `spdx_element_ref`  
- Missing or mismatched entries → **CI FAILURE**

Example rule linkage:

```
checksum row ↔ SPDX File entry ↔ SLSA attestation ↔ OpenLineage run
```

---

# 🧪 5. CI Validation Gates

CI MUST run the following:

### ✔ SBOM Schema Validation  
Validate SBOM structure using SPDX JSON schema.

### ✔ Cross-Reference Validation  
- `make validate-checksum-sbom`  
- Ensure every checksum row resolves to an SPDX entry  
- Ensure every SPDX entry with asset paths exists in the checksum registry

### ✔ Attestation Linking  
Check `Provenance:` attribution text and `externalRefs`.

### ✔ OpenLineage Linkage  
Ensure lineage paths are valid and refer to existing runs.

### ✔ License Validation  
Every SPDX entry MUST include:

- `licenseConcluded`  
- `licenseInfoInFile`

### ✔ FAIR+CARE Ethics Review  
SBOM must not expose direct paths to protected Indigenous data unless generalized or masked.

---

# 🗄 6. Mandatory SBOM Structure for Releases

A valid release MUST include:

```
releases/<ver>/sbom.spdx.json
releases/<ver>/attestations/*.slsa.json
releases/<ver>/registry.jsonl
releases/<ver>/manifest.zip
```

SBOM must list:

- All included artifacts  
- Build environment container digests  
- Dependency graph for all pipeline code  
- AI model metadata (Model Card UUIDs)  
- Dataset licenses + attribution  

---

# 🛠 7. Required SPDX Sections (KFM v11)

### ✔ `Document`  
Metadata, SPDX version, creation info, creators.

### ✔ `Packages` (optional)  
Used for pipeline containers or software layers.

### ✔ `Files`  
Required for **all data + model artifacts**.

### ✔ `Relationships`  
Link:

- `GENERATED_FROM`  
- `DESCENDANT_OF`  
- `CONTAINS`  
- `DEPENDS_ON`  

### ✔ `ExternalRefs`  
Link to SLSA, provenance, and lineage.

### ✔ `Annotations`  
Add FAIR+CARE notes, Indigenous sovereignty warnings, or masking declarations.

---

# 🌱 8. FAIR+CARE Requirements

SBOM MUST:

- NOT reveal precise locations for sensitive archaeological sites  
- Respect `care:authority` and `care:consent_required` metadata  
- Mark restricted artifacts with:

```
"annotations": [
  {
    "annotationType": "OTHER",
    "comment": "CARE-sensitive location; H3 generalized.",
    "annotator": "KFM Security Automation"
  }
]
```

- Include license metadata linking to cultural or Indigenous data agreements

---

# 🧭 9. Integration with the KFM System Stack

SBOM is consumed by:

- **Release pipelines** (verification)  
- **OpenLineage** (artifact identity)  
- **AI Pipelines** (dataset licensing)  
- **STAC Catalogs** (asset-level checks)  
- **Security audits** (runtime + artifact-level)  
- **Pipeline DAGs** (integrity enforcement)  
- **User-facing API resolvers** (`/resolve?sha256=` endpoints)

SBOM is the **ground truth** for:

- Dataset origins  
- Dependency transparency  
- License and ethics documentation  
- Artifact enumeration  
- Reproducible builds

---

# 🕰 10. Version History

- **v11.0.0 (2025-11-23)** — Initial SPDX SBOM Standard for KFM v11.

---

<div align="center">

**Kansas Frontier Matrix — SPDX SBOM Standard (v11)**  
*Transparency · Integrity · Supply-Chain Trust*

</div>

---

### 🔗 Footer  
[⬅ Back to Security Standards](./README.md) · [🔐 Checksum–SBOM–Provenance Standard](./checksum-sbom-provenance.md) · [🛡️ Audit Framework](./audits/README.md) · [🏛 Governance](../governance/ROOT-GOVERNANCE.md)

