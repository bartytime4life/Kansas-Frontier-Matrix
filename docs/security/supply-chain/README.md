---
title: "🛡️ Kansas Frontier Matrix — Supply Chain Security, Provenance & NPM Worm Defense (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/security/supply-chain/README.md"

version: "v11.2.3"
last_updated: "2025-11-29"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Security Council"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/docs-security-supply-chain-v4.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

status: "Active / Enforced"
doc_kind: "Security Standard"
intent: "supply-chain-security-and-npm-worm-defense"
category: "Security · Supply Chain · Provenance · NPM Defense"

fair_category: "F1-A1-I2-R2"
care_label: "Supply-Chain-Safe · Community-Protective"
sensitivity_level: "Medium"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Security Council"

sensitivity: "Security-sensitive conceptual architecture; no credentials or secrets stored; CARE applies to downstream impact"
risk_category: "High Governance"
redaction_required: true

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  owl_time: "ProperInterval"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/security/supply-chain/README.md@v10.2.4"
  - "supply-chain-protection/README.md@v10.4.0"
  - "SLSA 1.0 Framework"
  - "Sigstore-Cosign Provenance Notes"
  - "Shai-Hulud NPM Worm Post-Incident Review"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true

json_schema_ref: "../../../schemas/json/security-supply-chain-v11.schema.json"
shape_schema_ref: "../../../schemas/shacl/security-supply-chain-v11-shape.ttl"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "diagram-extraction"
  - "metadata-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "governance-override"
  - "narrative-fabrication"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"
requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
classification: "Public (Governed)"
ttl_policy: "Review required every 12 months"
sunset_policy: "Superseded by v12 supply-chain security standard"
---

<div align="center">

# 🛡️ **Kansas Frontier Matrix — Supply Chain Security, Provenance & NPM Worm Defense**  
`docs/security/supply-chain/README.md`

**Purpose**  
Define the **end-to-end supply-chain security framework** for the Kansas Frontier Matrix, covering  
**provenance, SBOMs, artifact signing, dependency governance**, and the **Shai-Hulud 2.0 / NPM Worm Defense Suite**.  
Ensure all builds are **tamper-evident, reproducible, traceable, and governance-approved**, resilient to Shai-Hulud–class  
npm worms and emerging multi-ecosystem supply-chain threats.

</div>

---

## 📘 1. Overview

The KFM v11.2.x supply-chain framework ensures:

- Every artifact originates from **signed, protected, reviewed source commits**.  
- Every build emits:
  - **SLSA-compliant provenance**
  - **SPDX & CycloneDX SBOMs**
  - **Cosign signatures + attestations**
- All dependencies are validated for:
  - CVEs  
  - Malware and worm-like behaviors  
  - Registry spoofing / typosquatting  
  - Lifecycle-script abuse (`preinstall`, `install`, `postinstall`, `prepare`, etc.)  
- Every CI/CD stage produces:
  - Governance telemetry  
  - FAIR+CARE impact notes  
  - Sustainability metrics (energy, carbon)  
- Any deviation is:
  - Automatically blocked  
  - Logged to the governance ledger  
  - Exposed to Story Nodes + Focus Mode for auditability  

This standard applies to **Node-based pipelines and any other build systems** that invoke npm or import npm tooling.

---

## 🗂️ 2. Directory Layout (Security Standards Context)

~~~text
docs/security/
├── 📄 README.md                         # Security overview
└── 📁 supply-chain/
    ├── 📄 README.md                     # ← This document (governance & architecture)
    ├── 🪱 shai-hulud-2.0/               # Shai-Hulud 2.0 defense suite (indicators, protections, reports)
    │   ├── 📄 README.md
    │   ├── 📊 indicators/
    │   ├── 🛡️ protections/
    │   ├── 🧬 provenance/
    │   ├── 🔧 workflows/
    │   ├── 📑 reports/
    │   └── 📦 stac/
    ├── 🧰 npm-ignore-scripts/          # Lifecycle-script suppression safeguard (policy + examples)
    └── 🛡️ supply-chain-protection/     # Implementation modules (scanners, CI hooks, registries, tests)
~~~

- This **README** defines the **governance specification and architecture**.  
- `shai-hulud-2.0/` defines the **concrete worm-defense model** (indicators, protections, provenance, workflows, reports).  
- `npm-ignore-scripts/` and `supply-chain-protection/` provide **implementation-level policies and tools**.

---

## 🧩 3. Supply Chain Security Flow (v11.2)

~~~text
Source Control  →  Reproducible Build  →  Signing & Attestation  →  SBOMs  
             →  Dependency & Worm Scanning  →  Policy Gates  →  Deployment  
             →  Governance & Telemetry  →  Story Nodes / Focus Mode
~~~

Conceptually, this aligns with the following pipeline:

- **Source Control**  
  - Signed commits  
  - Protected branches  
- **Reproducible Build**  
  - Deterministic tooling  
  - SLSA provenance  
- **Signing & Attestation**  
  - Cosign signatures  
  - SLSA provenance attestations  
- **SBOM Generation**  
  - SPDX + CycloneDX  
- **Dependency & Worm Scanning**  
  - CVE scanners  
  - Shai-Hulud 2.0 / NPM worm detectors  
  - Registry + publisher checks  
- **Policy Gates**  
  - OPA / Conftest rules  
  - FAIR+CARE checks  
  - Secret-safety rules  
- **Deployment**  
  - KFM services, pipelines, AI systems  
- **Governance & Telemetry**  
  - Audit logs  
  - Energy/carbon metrics  
  - Focus Mode / Story Node integration  

The **Shai-Hulud 2.0 Defense Suite** attaches primarily to **Dependency & Worm Scanning** and **Policy Gates**.

---

## 🛡️ 4. Shai-Hulud 2.0 / NPM Worm Defense Suite (Conceptual)

The defense suite enforces **install-time and pipeline-time safety** by:

### ✔ Lifecycle Script Suppression in CI

- CI MUST run with:
  - `npm ci --ignore-scripts`
  - `NPM_CONFIG_IGNORE_SCRIPTS=true`
- Lifecycle hooks are not executed in CI:
  - `preinstall`, `install`, `postinstall`, `prepare`, etc.  
- Equivalent protections required for:
  - Yarn / pnpm / Bun / custom runners  

### ✔ Malware & Worm Scanning

- Static and heuristic inspections for:
  - Obfuscated lifecycle scripts  
  - `child_process` + network usage in install-time code  
  - Known Shai-Hulud 2.0 indicators (from `shai-hulud-2.0/indicators/`)  
- Graph-based checks for:
  - Dependency tree anomalies  
  - Registry-switch behavior  

### ✔ Controlled Internal Registries

- All CI npm traffic must go through an **approval-gated, auditable proxy**:
  - Enforces allow/deny lists  
  - Logs all package resolutions and versions  
  - Supports quarantine and manual review  

### ✔ Registry & Publish Monitoring

- Alerts when:
  - New packages are published under KFM namespaces  
  - Dependencies change outside approved PR flows  
  - High-risk dependencies appear in lockfiles  

### ✔ Developer Hardening Tools

- Git hooks to prevent committing lifecycle scripts  
- CLI wrappers for safe local installs  
- Local scanners to detect suspicious install-time code  
- Warnings for unapproved registries or package sources  

---

## ⚖️ 5. Governance Policies (P1–P6)

### **P1 — SBOM Generation (Mandatory)**

Every release must include:

- SPDX SBOM  
- CycloneDX SBOM  

### **P2 — Artifact Signing**

All release artifacts must be:

- Signed with Cosign  
- Recorded in a transparency log (e.g., Rekor)  

### **P3 — SLSA Provenance**

All builds must emit SLSA v11-compliant provenance describing:

- Builder identity  
- Source repository + ref  
- Inputs + dependencies  
- Environment info  

### **P4 — CVE + Worm Scanning**

Before deployment:

- All dependencies scanned for CVEs  
- Shai-Hulud 2.0 / NPM worm patterns scanned  
- High-risk packages must be patched, replaced, or blocked  

### **P5 — Policy-as-Code Gates**

OPA/Conftest enforce:

- Presence of SBOM + provenance  
- Proper signing  
- Secrets isolation  
- FAIR+CARE metadata & impact tagging  

### **P6 — Telemetry & Governance Logging**

All supply-chain events are logged to:

- `focus-telemetry.json`  
- Governance ledger (risk, energy, carbon, FAIR+CARE status)  

---

## 🧪 6. CI Integration Requirements

### Mandatory Flags

- `npm ci --ignore-scripts`  
- No bare `npm install` in CI  

### Prohibited Patterns in CI

- Execution of any lifecycle hooks  
- Dynamic download of tools from unapproved URLs  
- Direct registry usage bypassing the KFM proxy  

### CI Failure Conditions

- Missing SBOMs or provenance  
- Missing Cosign signatures for artifacts  
- Lifecycle scripts present in install path of CI  
- Registry discrepancies or unapproved sources  
- FAIR+CARE or governance violations  

---

## 📊 7. Telemetry Model

Supply-chain telemetry must record:

- Pass/fail for supply-chain audits  
- Number of dependencies and scan coverage  
- Presence/absence of worm-like behaviors  
- Signing/attestation completeness  
- SBOM coverage  
- Energy (Wh) and carbon (gCO2e) per build  
- FAIR+CARE risk/impact indicators  

Example event:

~~~text
{
  "event": "supply_chain_audit",
  "timestamp": "2025-11-29T21:09:00Z",
  "workflow": "ci-build.yml",
  "sbom_ok": true,
  "provenance_ok": true,
  "npm_ignore_scripts_enforced": true,
  "worm_detected": false,
  "cve_critical": 0,
  "energy_wh": 4.4,
  "carbon_gco2e": 0.0019
}
~~~

---

## ⚖️ 8. FAIR+CARE Integration

Supply-chain security is ethically critical because:

- Compromised pipelines can harm communities that rely on KFM insights.  
- Malicious data paths can distort ecological, hydrologic, or historical interpretations.  
- Data integrity is essential for representing Indigenous and community narratives accurately.  

FAIR+CARE checks ensure:

- Provenance is transparent and verifiable.  
- Risk to downstream communities is minimized.  
- Sensitive or sovereign data is never altered by compromised tooling.  

---

## 🧠 9. Story Node & Focus Mode Integration

This standard underpins KFM’s security-focused narratives:

- **“How the build stayed clean”** — supply-chain integrity stories  
- **“Worm attempt averted”** — telemetry-backed incident avoidance  
- **“From dependency to decision”** — end-to-end provenance narratives  

Focus Mode uses:

- Telemetry  
- STAC Items  
- SBOM/provenance graphs  
- Shai-Hulud 2.0 indicators  

to render **auditable, explainable stories** about supply-chain risk and governance.

---

## 🧭 10. Version History

| Version | Date       | Summary                                                                                                                   |
|--------:|------------|---------------------------------------------------------------------------------------------------------------------------|
| v11.2.3 | 2025-11-29 | Aligned with Shai-Hulud 2.0 subtree; updated directory layout; footer alignment; clarified CI + proxy requirements.       |
| v11.2.2 | 2025-11-27 | Canonical v11.2.2 governance; telemetry and SBOM/provenance tightening; integrated NPM ignore-scripts standard.          |
| v11.2.0 | 2025-11-27 | Initial v11.2 supply-chain security + worm defense specification.                                                        |
| v10.2.4 | 2025-11-12 | v10.2 supply-chain governance; aligned with SBOM and provenance pipelines.                                              |

---

<div align="center">

[📘 Docs Root](../../../../..) · [🧪 Pipelines](../../../../../pipelines) · [🌐 Governance](../../standards/governance/ROOT-GOVERNANCE.md)

</div>
