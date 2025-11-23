---
title: "📦 KFM v11 — Artifact Integrity & Reproducibility Audit Template (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/security/audits/artifacts-audit-template.md"
version: "v11.0.0"
last_updated: "2025-11-23"
review_cycle: "Quarterly · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../releases/v11.0.0/security-audits-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/security-audits-artifacts-v1.json"
governance_ref: "../../governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active · Enforced"
doc_kind: "Audit Template"
semantic_document_id: "kfm-artifacts-audit-template-v11"
doc_uuid: "urn:kfm:standards:security:audits:artifacts-template:v11"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Medium-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 📦 **Artifact Integrity & Reproducibility Audit Template (v11)**  
`docs/standards/security/audits/artifacts-audit-template.md`

**Purpose:**  
Provide a structured, reproducible audit template for validating artifact integrity, supply-chain provenance,  
SBOM conformance, FAIR+CARE ethics compliance, and deterministic rebuild capability of any KFM artifact.

This template is filled out for:  
STAC assets, COG rasters, Parquet/NetCDF tables, embeddings/models, API bundles, Story Nodes,  
and all release artifacts under `releases/v11.x`.

</div>

---

# 📘 Instructions

Fill out **one copy of this template per artifact**.

All fields are **required** unless marked “optional.”

Save completed audits under:

```
docs/archives/provenance/audits/artifacts/<YYYY-MM-DD>/<artifact>.audit.md
```

Attach:

- SBOM snapshot  
- Provenance attestation  
- Checksum registry excerpt  
- OpenLineage run record  
- Reproduction logs  

---

# 🧱 1. Artifact Identity

| Field | Value |
|------|-------|
| Artifact Path | `<relative path>` |
| Artifact Type | `COG | GeoJSON | Parquet | NetCDF | STAC Item | Model | StoryNode | Other` |
| Version | `<semver or date>` |
| Release Tag | `v11.x.x` |
| Size (bytes) | `<int>` |
| MIME Type | `<string>` |

---

# 🔐 2. Hash & Checksum Verification

| Hash | Value | Verified? |
|------|--------|-----------|
| SHA-256 | `<hex>` | ☐ Yes ☐ No |
| SHA-512 | `<hex>` | ☐ Yes ☐ No |
| Multi-hash (optional) | `<hex>` | ☐ Yes ☐ No |

### Checksum Ledger Entry  
Paste the object from `data/archive/<quarter>/checksums/registry.jsonl`:

```
<JSON object here>
```

Verification result:  
- ☐ Passed  
- ☐ Failed  
- Notes: `<text>`

---

# 📦 3. SBOM Mapping

| Field | Value |
|------|--------|
| SPDX Element Ref | `<e.g., SPDXRef-File-...>` |
| SBOM File | `releases/<ver>/sbom.spdx.json` |
| SBOM Entry Found | ☐ Yes ☐ No |
| Checksums Match SBOM | ☐ Yes ☐ No |

### SBOM Entry  
Paste the relevant SBOM JSON snippet:

```
<SBOM JSON object>
```

---

# 🧬 4. Provenance Attestation (SLSA / in-toto)

| Field | Value |
|------|--------|
| Attestation File | `releases/<ver>/attestations/<artifact>.slsa.json` |
| Builder ID | `<string>` |
| Build Type | `<string>` |
| Build Started | `<ISO datetime>` |
| Build Finished | `<ISO datetime>` |
| Subject Digest Matches Checksum | ☐ Yes ☐ No |

### Attestation Snippet

```
<attestation excerpt>
```

---

# 🛰 5. OpenLineage Run Verification

| Field | Value |
|------|--------|
| Lineage URI | `<path or URL>` |
| Run ID | `<uuid>` |
| Pipeline | `<pipeline name>` |
| Node | `<node name>` |
| Timestamp | `<ISO datetime>` |

### Lineage Snippet

```
<OpenLineage JSON excerpt>
```

---

# 🧪 6. Deterministic Rebuild Test

| Test | Result |
|------|---------|
| Able to rebuild artifact from exact commit? | ☐ Yes ☐ No |
| Output hash matches original? | ☐ Yes ☐ No |
| Environment reproduced (container ID matches)? | ☐ Yes ☐ No |
| Dependencies match SBOM? | ☐ Yes ☐ No |

Notes:

```
<describe reproduction attempt>
```

---

# 🧱 7. FAIR+CARE Ethics Check

| Requirement | Pass? | Notes |
|-------------|--------|-------|
| Indigenous Data Sovereignty respected | ☐ Yes ☐ No | `<text>` |
| Sensitive archaeology masked (H3) | ☐ Yes ☐ No | `<text>` |
| Proper license attribution | ☐ Yes ☐ No | `<text>` |
| No prohibited data leakage | ☐ Yes ☐ No | `<text>` |
| Story Node or Focus Mode safe for narrative generation | ☐ Yes ☐ No | `<text>` |

---

# 🛠 8. Additional Domain-Specific Checks  
*(Customize per artifact domain)*

### Hydrology (if applicable)
- ☐ Vertical datum = NAVD88  
- ☐ CF positive convention correct  
- ☐ Hydro STAC fields valid  

### Climate (if applicable)
- ☐ Units match Data Contract v3  
- ☐ CRS transitions correct  
- ☐ COG structure valid  

### Hazard (if applicable)
- ☐ Hazard taxonomy applied  
- ☐ Severity + casualty fields validated  

### Archaeology (if applicable)
- ☐ Masking rules applied  
- ☐ CARE attributes present  

### ML/AI Models
- ☐ Model Card v11 included  
- ☐ Training lineage validated  
- ☐ Explainability bundles attached  

---

# 📝 9. Final Assessment

```
Overall Status:  ☐ PASS   ☐ FAIL
Auditor Name:    <name>
Auditor Role:    <role>
Audit Date:      <YYYY-MM-DD>
Notes:
<text here>
```

---

# 🕰 Version History

- **v11.0.0 (2025-11-23)** — Initial artifact-level audit template for KFM v11.

---

<div align="center">

**Kansas Frontier Matrix — Artifact Integrity & Reproducibility Audit Template (v11)**  
*Traceable · Verifiable · Ethically Governed*

</div>

---

### 🔗 Footer  
[⬅ Back to Security Audits](./README.md) · [🔗 Checksum–SBOM–Provenance Standard](../checksum-sbom-provenance.md) · [🏛 Governance](../../governance/ROOT-GOVERNANCE.md)

