---
title: "🧬 KFM v11 — Data Integrity & Authenticity Standard (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/security/data-integrity-standard.md"
version: "v11.0.0"
last_updated: "2025-11-23"
review_cycle: "Quarterly · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../releases/v11.0.0/security-audits-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/data-integrity-standard-v11.json"
governance_ref: "../governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active · Enforced"
doc_kind: "Security Standard"
semantic_document_id: "kfm-data-integrity-standard-v11"
doc_uuid: "urn:kfm:standards:security:data-integrity:v11"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Medium-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 🧬 **KFM v11 — Data Integrity & Authenticity Standard**  
`docs/standards/security/data-integrity-standard.md`

**Purpose:**  
Define the canonical v11 rules for **data integrity, authenticity, verifiability, and reproducible trust**  
across all KFM datasets, STAC assets, model outputs, lineage chains, and archived files.  
This standard ensures **lossless fidelity**, **cryptographic verification**, **FAIR+CARE alignment**,  
and **SLSA/OpenLineage-based provenance** for all artifacts in the platform.

</div>

---

# 📘 1. Overview

Data integrity in KFM v11 is defined as:

> **The guarantee that every dataset, raster, vector, model, or derivative product is an exact,  
> cryptographically-verifiable, provenance-bound representation of its declared source inputs,  
> with no unauthorized modification or loss of fidelity.**

Integrity = **Checksums + SBOM identity + Provenance attestation + Lineage evidence + CARE protection**.

This standard covers:

- Immutable checksum registries  
- Hash consistency for STAC assets  
- Reproducible ETL & AI pipelines  
- SLSA attestation verification  
- OpenLineage run synchronization  
- FAIR+CARE ethical integrity  
- Raster/vector integrity enforcement  
- Release stability across versions  

---

# 🧱 2. Data Integrity Foundations (KFM v11)

All KFM artifacts MUST satisfy the following **four pillars**:

## 2.1 Cryptographic Integrity  
- SHA-256 required  
- SHA-512 recommended  
- Multi-hash optional (v11+)  
- Hashes stored in authoritative registry (`data/archive/<quarter>/checksums/registry.jsonl`)

## 2.2 SBOM Identity  
- Every artifact must map to an **SPDX File or Package** entry  
- SBOM must contain checksum, license, and external references  
- SBOM must be validated via CI before release

## 2.3 Verified Provenance  
- SLSA v1.0 attestation required  
- OpenLineage run evidence required  
- Provenance subject digest must match checksum digest

## 2.4 Reproducible Generation  
- Pipelines must be deterministic  
- Model outputs must be reproducible with fixed seeds  
- COG rasters must have reproducible tiling  
- Temporal/spatial transforms must match lineage metadata exactly

---

# 🔐 3. Integrity Requirements for KFM Data Types

## 3.1 Tabular Data (CSV, Parquet)
- Schema validation required  
- Byte-for-byte determinism for exported Parquet  
- All nullability / encoding rules must match schema  
- Parquet compression must be deterministic (ZSTD or Snappy w/ fixed settings)

## 3.2 Raster Data (COG, GeoTIFF, NetCDF)
- Tiling: **512×512** blocks (COG standard)  
- Overviews: **2×, 4×, 8×, 16× …**  
- CRS alignment: EPSG:4326 for STAC geometry; EPSG:26914 for processing  
- Vertical axis: NAVD88 + GEOID18  
- Raster integrity checks:
  - Bitwise identical rebuilds  
  - Valid geotransform  
  - Band metadata consistent across outputs  

## 3.3 Vector Data (GeoJSON, Parquet-Vector)
- Coordinates MUST be valid EPSG:4326  
- Geometry MUST match GeoSPARQL rules  
- No unclosed rings or invalid multipolygons  
- Feature ordering must be stable across exports  

## 3.4 STAC Items & Collections
- All STAC Items MUST include:
  - `proj:*`
  - `vertical:*`
  - `kfm:cf_positive`
  - Domain metadata (hydro/climate/heritage/etc.)
  - PROV-O lineage block  
- Hashes of attached assets must match registry  
- Temporal extents must be OWL-Time valid  
- Geometry must be reproducible from source data

## 3.5 Story Nodes (Narrative Artifacts)
- Source references MUST be checked against dataset lineage  
- AI-generated narratives must include attribution + content provenance  
- No unverified claims  
- CARE-sensitive content must be masked at source, not post-hoc  

## 3.6 AI/ML Models
- Model Card v11 required  
- Training provenance required  
- Data dependencies must be SBOM-listed  
- Reproducing model weights MUST yield matching hash (unless stochastic training formally declared)

---

# 🧩 4. Provenance Integration Rules

All artifacts MUST contain resolvable provenance pathways:

```
Checksum → SBOM → Provenance Attestation → OpenLineage Run → Upstream Inputs
```

### Mandatory provenance fields in artifact metadata:

```
spdx_element_ref
sbom_uri
provenance_uri
lineage_run_uri
build_digest
```

### Upstream materials must list:

- Git commit hash  
- Dependency lockfiles  
- Container digest  
- STAC Item IDs and versions  
- Source dataset checksums  

---

# 🛰 5. CI Enforcement Gates (Non-Bypassable)

CI must enforce validation across:

## 5.1 Checksum Registry
- Ensure every artifact is present  
- Reject if SHA mismatch  
- Reject if registry row missing required fields  

## 5.2 SBOM Validation
- Validate SBOM structure  
- Ensure every checksum has an SBOM entry  
- Reject if SBOM missing required licenses

## 5.3 Provenance Attestation
- Validate SLSA subject digests  
- Ensure builder ID + buildType valid  
- Require materials list for training + ETL DAGs  

## 5.4 OpenLineage Evidence
- Validate run files exist  
- Validate run output hashes match registry  
- Validate node metadata (tool versions, CRS, vertical axis, pipeline ID)

## 5.5 FAIR+CARE Data Ethics
- Enforce sensitive-data masking (H3 for archaeology)  
- Ensure no CARE-violating content in outputs  
- Validate provenance of Indigenous datasets  

If ANY check fails → **PR is blocked**.

---

# 🔍 6. Release Artifact Rules (v11)

A KFM release MUST include:

- SBOM (`sbom.spdx.json`)  
- Checksum registry (`registry.jsonl`)  
- Attestation directory (`attestations/*.slsa.json`)  
- Provenance chain (`docs/archives/provenance/...`)  
- Combined lineage index (`lineage-index.json`)  
- Integrity summary (`integrity-report.json`)  

Release workflow MUST:

1. Recompute all checksums  
2. Rebuild COG overviews  
3. Re-validate all STAC Items  
4. Regenerate SBOM  
5. Verify SLSA attestations  
6. Link lineage → provenance → SBOM → checksum  
7. Emit OpenLineage job+run records  
8. Assemble complete release bundle  

---

# 🌱 7. FAIR+CARE Ethical Integrity

Integrity in KFM extends beyond bytes—it includes **ethical integrity**:

- No exposure of sensitive Indigenous site coordinates  
- All L3/L4 archaeological sites must be H3-generalized  
- Provenance must include CARE metadata fields  
- Narrative elements must avoid unverified or harmful inference  
- Story Nodes must reflect truthfulness, sourcing, and cultural respect  
- Sensitive data must have governance-approved lineage  

Ethical integrity checks MUST be included in:

- Security audits  
- Build pipelines  
- AI inference pipelines  
- UI visualization layer  

---

# 🛠 8. Integrity Tooling Reference

Recommended CLI tools:

```
make validate-checksum-sbom
make validate-provenance
make emit-openlineage
make rebuild-artifact
make validate-cog
make validate-parquet
make validate-stac
```

Existing KFM tools:

- `kfm-integrity-cli` (internal)  
- `stac-validate`  
- `gdalinfo`, `gdaladdo`  
- `parquet-tools`  
- `sbom-validate`  
- `slsa-verifier`  
- `openlineage-run-verify`  

---

# 🧠 9. Integration Across KFM System Stack

Integrity flows through:

```
RAW DATA
 → ETL Pipelines (Autonomous / Batch)
 → STAC Items
 → SBOM
 → SLSA Attestation
 → OpenLineage Run
 → API / UI
 → Story Nodes / Focus Mode
 → Release Bundle
```

Every layer MUST maintain:

- Identity  
- Integrity  
- Provenance  
- FAIR+CARE metadata  

No data may bypass this chain.

---

# 🕰 10. Version History

- **v11.0.0 (2025-11-23)** — Initial Data Integrity Standard.

---

<div align="center">

**Kansas Frontier Matrix — Data Integrity & Authenticity Standard (v11)**  
*Truth · Trust · Transparency · Traceability*

</div>

---

### 🔗 Footer  
[⬅ Back to Security Standards](../README.md) · [🔗 Checksum–SBOM–Provenance Spec](./checksum-sbom-provenance.md) · [🏛 Governance](../governance/ROOT-GOVERNANCE.md)

