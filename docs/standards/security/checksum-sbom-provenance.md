---
title: "🔗 KFM v11 — Checksum ⇄ SPDX SBOM ⇄ Provenance Integration Standard (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/security/checksum-sbom-provenance.md"
version: "v11.1.0"
last_updated: "2025-11-23"
review_cycle: "Quarterly · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/checksum-sbom-provenance-v11.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
data_contract_ref: "../../contracts/data-contract-v3.json"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Security Standard"
semantic_document_id: "kfm-checksum-sbom-provenance-v11"
doc_uuid: "urn:kfm:standards:security:checksum-sbom-provenance:v11"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 🔗 **KFM v11 — Checksum ⇄ SPDX SBOM ⇄ Provenance Integration Standard**  
`docs/standards/security/checksum-sbom-provenance.md`

**Purpose:**  
Define the v11 unified security framework linking **checksums**, **SPDX SBOM entries**,  
**SLSA/in-toto provenance attestations**, and **OpenLineage run records** so every artifact in KFM  
has fully cryptographically resolvable identity, lineage, integrity, and auditability.

</div>

---

# 📘 Overview

This v11 security standard closes the **checksum → SBOM → provenance → lineage** loop across the  
entire KFM platform—data, code, pipelines, releases, and STAC artifacts.

Every **checksum row** must be resolvable to:

1. An **SPDX element** (package/file)  
2. A **provenance attestation** (SLSA/in-toto)  
3. An **OpenLineage run** describing the pipeline that created the artifact  

This guarantees:

- Deterministic traceability  
- Cryptographically verifiable provenance  
- FAIR+CARE auditability  
- Strong supply-chain integrity for all KFM artifacts  

---

# 🧩 1. Core Concepts (Plain Terms)

### 🔐 Checksum Registry  
Canonical hash ledger of all artifacts for a given release.

### 📦 SPDX SBOM  
Machine-readable inventory of all files and packages, including their hashes.

### 🧬 Provenance (SLSA or in-toto)  
Describes who/what/when created an artifact.

### 🛰 OpenLineage  
Execution-level lineage: pipeline, node, IO, dataset, checksums, code refs.

---

# ✅ 2. Minimal v11 Requirements

Every checksum entry MUST contain:

```
spdx_element_ref   # e.g. "SPDXRef-File-gauges-parquet"
sbom_uri           # resolved path to sbom.spdx.json
provenance_uri     # SLSA/in-toto attestation
lineage_run_uri    # OpenLineage run record
build_digest       # digest of the attestation (sha256-<hex>)
```

SBOM entries MUST include:

- Matching digest(s)  
- Direct references to provenance attestation  
- Attribution text pointing to OpenLineage run(s)  

---

# 🧱 3. Directory Conventions (KFM v11)

```
releases/<ver>/sbom.spdx.json
releases/<ver>/attestations/<artifact>.slsa.json
data/archive/2025Q4/checksums/registry.jsonl
docs/archives/provenance/chains/...  (pointer to same URIs)
```

All paths MUST be stable, relative-path safe, and resolvable via CI.

---

# 🧪 4. CI Validation Gates

CI **MUST FAIL** if:

- A checksum row lacks a resolvable `spdx_element_ref`  
- SBOM is missing the corresponding element  
- Digest mismatch between checksum and SBOM  
- `provenance_uri` or `lineage_run_uri` is missing or 404s  
- Attestation subject digest ≠ checksum digest  

Gates:

```
make validate-checksum-sbom
make validate-provenance
make emit-openlineage
```

---

# 📄 5. Sample: Checksum Registry Row (JSONL)

One JSON object per line:

```json
{
  "artifact_path": "data/processed/hydrology/statewide/gauges.parquet",
  "sha256": "<hex>",
  "sha512": "<hex>",
  "size": 12345678,
  "spdx_element_ref": "SPDXRef-File-gauges-parquet",
  "sbom_uri": "../../releases/v11.0.0/sbom.spdx.json",
  "provenance_uri": "../../releases/v11.0.0/attestations/gauges.parquet.slsa.json",
  "lineage_run_uri": "../../docs/archives/provenance/chains/hydrology/streamflow/statewide/run-2025-11-20.json",
  "build_digest": "sha256-<hex>",
  "created": "2025-11-20T22:14:31Z"
}
```

---

# 📦 6. Sample: SPDX File Entry

```json
{
  "SPDXID": "SPDXRef-File-gauges-parquet",
  "fileName": "data/processed/hydrology/statewide/gauges.parquet",
  "checksums": [
    {"algorithm": "SHA256", "checksumValue": "<hex>"},
    {"algorithm": "SHA512", "checksumValue": "<hex>"}
  ],
  "attributionTexts": [
    "Provenance: ../../releases/v11.0.0/attestations/gauges.parquet.slsa.json",
    "OpenLineage: ../../docs/archives/provenance/chains/hydrology/streamflow/statewide/run-2025-11-20.json"
  ],
  "externalRefs": [
    {
      "referenceCategory": "SECURITY",
      "referenceType": "other",
      "referenceLocator": "https://slsa.dev/attestation#json:../../releases/v11.0.0/attestations/gauges.parquet.slsa.json"
    }
  ]
}
```

---

# 🧾 7. Sample: SLSA / Provenance Attestation (Minimal)

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
  "buildConfig": {"pipeline": "LangGraph v11 DAG", "node": "hydrology-refresh/export"},
  "metadata": {
    "buildStartedOn": "2025-11-20T21:59:00Z",
    "buildFinishedOn": "2025-11-20T22:14:00Z"
  },
  "materials": [
    {"uri": "git+https://github.com/...#<commit>", "digest": {"sha1": "<hex>"}}
  ]
}
```

---

# 🏁 8. Build & Release Integration

Release workflows MUST:

- Regenerate SBOM  
- Recompute checksum registry  
- Write provenance attestations  
- Link all artifacts using this standard  
- Run all CI validation gates  

`.github/workflows/release.yml` MUST implement:

```
validate-checksum-sbom
validate-provenance
emit-openlineage
attach-artifacts
```

---

# 🔧 9. Integration Targets

### Artifacts that MUST follow this standard:

- STAC Items  
- COG rasters  
- Parquet/CSV/NetCDF files  
- Model outputs  
- Story Node bundles  
- Forecast/AI artifacts  
- Anything placed in `releases/` or referenced by a STAC catalog  

---

# 🧠 10. Why This Closes the Loop

This v11 standard guarantees that **any hash** in the system resolves deterministically to:

- Its **SBOM identity**,  
- Its **verifiable provenance attestation**, and  
- Its **OpenLineage execution record**.

This provides **full supply-chain security**, **FAIR+CARE accountability**, and  
**machine-verifiable evidence** for audits, reproducibility, and scientific governance.

---

# 🕰 Version History

- **v11.1.0 (2025-11-23)** — Upgraded to full KFM-MDP v11.0.0. Added build loop, CI gates, examples, directory schema, and security requirements.  
- **v11.0.0** — Initial mini-spec.

---

<div align="center">

**Kansas Frontier Matrix — Checksum ⇄ SBOM ⇄ Provenance Integration Standard (v11)**  
*Integrity · Identity · Lineage · Trust*

</div>

---

### 🔗 Footer  
[⬅ Back to Security Standards](../README.md) · [📦 SBOM](../../../releases/v11.0.0/sbom.spdx.json) · [🧬 Provenance Chains](../../archives/provenance/chains/) · [🏛 Governance](../../standards/governance/ROOT-GOVERNANCE.md)
