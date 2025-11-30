---
title: "🔡 KFM v11.2.2 — Typosquatting Examples (Dependency-Confusion Pattern Library)"
path: "docs/security/supply-chain/dependency-confusion/examples/typosquat-examples.md"
version: "v11.2.2"
last_updated: "2025-11-30"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../../../../releases/v11.2.2/signature.sig"
attestation_ref: "../../../../../releases/v11.2.2/slsa-attestation.json"
sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/security-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/security-v3.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive)"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "Public"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Entity"
  owl_time: "ProperInterval"
  geosparql: "geo:Feature"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/security/supply-chain/dependency-confusion/examples/typosquat-examples.md@v11.2.1"
  - "docs/security/supply-chain/dependency-confusion/examples/typosquat-examples.md@v11.2.0"
  - "docs/security/supply-chain/dependency-confusion/examples/README.md"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: false

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:security:dependency-confusion:examples:typosquat-examples:v11.2.2"
semantic_document_id: "kfm-depconf-examples-typosquat-v11.2.2"
event_source_id: "ledger:depconf.examples.typosquat.v11.2.2"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"

ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "metadata-extraction"
  - "diagram-extraction"

ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🔡 Common Typosquat Variants"
    - "🧪 Simulated CI Detection Output"
    - "🛡️ How KFM v11.2.2 Protects Against Typosquatting"
    - "🧭 Developer Guidance"
    - "🕰️ Version History"

---

<div align="center">

# 🔡 **Typosquatting Examples**  
`docs/security/supply-chain/dependency-confusion/examples/typosquat-examples.md`

**Purpose:**  
Serve as a curated pattern library of known typosquatting attack forms used to impersonate  
internal KFM package namespaces. These examples support training, automated reasoning,  
namespace heuristics, and CI/CD enforcement logic.

</div>

---

## 📘 Overview

Typosquatting is one of the most widely used dependency-confusion attack vectors.  
Attackers register packages with names that look nearly identical to official internal packages using:

- homoglyph substitution  
- Unicode confusables  
- subtle misspellings  
- hyphen/dot/underscore variations  
- prefix/suffix manipulation  
- zero-width characters  

These examples demonstrate the most common malicious naming strategies across npm, PyPI, Cargo,  
RubyGems, and Maven ecosystems.

---

## 🗂️ Directory Layout

~~~text
📁 dependency-confusion/
└── 📁 examples/
    ├── 📄 README.md
    ├── 📄 namespace-collision-basic.md
    ├── 📄 namespace-collision-firstpublish.md
    ├── 📄 namespace-collision-versionrace.md
    ├── 📄 typosquat-examples.md           # This file
    ├── 📄 registry-fallback.md
    ├── 📄 mirror-drift.md
    ├── 📄 sbom-drift-basic.json
    ├── 📄 lockfile-drift-attack.md
    ├── 📄 invalid-cosign.sig
    ├── 📄 missing-provenance.json
    ├── 📄 sandbox-network-leak.md
    └── 📄 implicit-upgrade-attack.md
~~~

---

## 🔡 Common Typosquat Variants

### 1. **Simple Character Swaps**
| Legitimate        | Attacker Variant       |
|-------------------|-------------------------|
| `@kfm/core`       | `@kfm/cor`              |
| `kfm-data-core`   | `kfm-data-cor`          |
| `kfm-map-engine`  | `kfm-map-engin`         |

---

### 2. **Omitted Characters**
| Legitimate           | Variant                |
|----------------------|------------------------|
| `kfm-geoscan`        | `kfm-geocan`           |
| `kfm-vision-core`    | `kfm-vision-cre`       |

---

### 3. **Unicode Homoglyphs**
| Legitimate          | Variant                       |
|---------------------|-------------------------------|
| `kfm-core`          | `kfm-c0re`                    |
| `kfm-utils`         | `kfm-utìls`                   |
| `kfm-modeI-runner`  | (uppercase “I” replacing “l”) |

---

### 4. **Prefix / Suffix Manipulation**
Attackers often append or remove subtle vendor-styled suffixes:

| Legitimate | Variant        |
|------------|----------------|
| `@kfm/core` | `@kfm-core`   |
| `kfm-api`   | `kfm-api-tools` |

---

### 5. **Dash / Dot / Underscore Confusion**
| Legitimate         | Variant           |
|--------------------|-------------------|
| `kfm.data.core`    | `kfm-data-core`   |
| `kfm-core`         | `kfm_core`        |
| `kfm-routing-core` | `kfm-routingcore` |

---

### 6. **Zero-Width Character Injection**
Example:

```
kfm​-core    # Contains zero-width space U+200B
```

Visually identical to `kfm-core` in most editors.

---

## 🧪 Simulated CI Detection Output

```text
[typosquat-detector]  WARNING: suspicious near-miss name detected: "kfm-cor"
[namespace-monitor]   INFO: Levenshtein distance = 1 (high-risk proximity)
[policy]              FAIL: potential typosquat package — dependency blocked.
[evidence]            Updated: namespace-scan.json
```

---

## 🛡️ How KFM v11.2.2 Protects Against Typosquatting

- Levenshtein-distance heuristics  
- Unicode confusable detection  
- Prefix/suffix pattern analysis  
- Dangerous-namespace blocking  
- Registry-isolation enforcement  
- Deterministic pinning & SBOM locking  
- SLSA provenance validation  
- Cosign/GPG signature enforcement  
- Pre-commit and CI namespace scanners  

---

## 🧭 Developer Guidance

- Only install dependencies from **internal KFM mirrors**  
- Run local scans:
  ```bash
  kfm-ns-scan .
  ```
- Treat any unexpected dependency suggestion as suspicious  
- Validate provenance:
  ```bash
  kfm-provenance-verify --local
  ```
- Report all suspicious names immediately to the Security Council  

---

## 🕰️ Version History

| Version  | Date       | Notes |
|----------|------------|--------|
| v11.2.2  | 2025-11-30 | Fully expanded v11.2.2 example with extended metadata |

---

<div align="center">

📚 [Examples Index](./README.md) • 🧨 [Collision Examples](./namespace-collision-basic.md) • 🧭 [Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

