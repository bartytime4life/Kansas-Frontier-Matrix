---
title: "🔍 KFM v11.2.2 — Local Scan Guidance for Dependency-Confusion Defense (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/security/supply-chain/dependency-confusion/checks/local-scan-guidance.md"
version: "v11.2.2"
last_updated: "2025-11-30"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Supply-Chain Security Council"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../../../../releases/v11.2.2/signature.sig"
attestation_ref: "../../../../../releases/v11.2.2/slsa-attestation.json"
sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/release-manifest.zip"
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

doc_kind: "Security · Local-Scan-Guidance"
intent: "developer-local-scanning · early-detection · dependency-confusion-prevention"

fair_category: "F1-A1-I1-R1"
care_label: "CARE · Governance · Infrastructure Protection"
classification: "Security · Developer Tooling · Local Validation"
sensitivity: "Security-Sensitive (non-personal)"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
indigenous_rights_flag: true
risk_category: "Medium"
redaction_required: false

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon next local-scan policy revision"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"
  owl_time: "ProperInterval"
  geosparql: "geo:Feature"

metadata_profiles:
  - "DCAT 3.0"
  - "STAC 1.0.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/security/supply-chain/dependency-confusion/checks/local-scan-guidance.md@v11.2.1"
  - "docs/security/supply-chain/dependency-confusion/checks/local-scan-guidance.md@v11.2.0"
  - "docs/security/supply-chain/dependency-confusion/checks/README.md"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: false

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:security:depconf:checks:local-scan-guidance:v11.2.2"
semantic_document_id: "kfm-depconf-checks-local-scan-v11.2.2"
event_source_id: "ledger:depconf.checks.localscan.v11.2.2"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"

ai_transform_permissions:
  - "summary"
  - "metadata-extraction"
  - "semantic-highlighting"
  - "timeline-generation"
  - "diagram-extraction"

ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🧩 Local Scan Tooling Provided"
    - "🔧 Installation (KFM Developer Toolkit)"
    - "🛰️ Running Local Namespace Scans"
    - "🔒 Checking Registry Isolation Locally"
    - "📦 Validating Dependency Pinning"
    - "🧬 Verifying SBOM Drift Locally"
    - "✍️ Local Provenance & Signature Verification"
    - "🧯 Testing Fallback Activation"
    - "🕰️ Version History"
---

<div align="center">

# 🔍 **Local Scan Guidance for Dependency-Confusion Defense**  
`docs/security/supply-chain/dependency-confusion/checks/local-scan-guidance.md`

**Purpose:**  
Provide step-by-step instructions for developers, security engineers, and CI maintainers to run  
manual/local dependency-confusion scans **before** code is pushed or pipelines are executed.  
These checks mirror KFM-CI behavior to catch namespace collisions, pinning drift, signature failures,  
registry anomalies, and SBOM inconsistencies at the earliest possible stage.

</div>

---

## 📘 Overview

While CI enforces policy centrally, **local scanning empowers developers** to:

- Catch issues early  
- Maintain deterministic, secure environments  
- Prevent dependency-confusion vulnerabilities from ever reaching CI/CD  

Local scans help ensure:

- Correct dependency pinning  
- Registry isolation  
- Cryptographic integrity  
- SBOM + dependency graph alignment  
- Provenance correctness  
- Proper fallback behaviors during degraded conditions  

---

## 🗂️ Directory Layout

~~~text
📁 dependency-confusion/
└── 📁 checks/
    ├── 📄 README.md                     # Automated checks index
    ├── 📄 ci-validation-rules.md        # CI validation rules
    ├── 📄 provenance-hooks.md           # Attestation/provenance hooks
    ├── 📄 registry-anomaly-detection.md # Registry anomaly detection rules
    ├── 📄 pre-commit-rules.md           # Developer-machine validation policies
    └── 📄 local-scan-guidance.md        # This file — manual/local scan guidance
~~~

---

## 🧩 Local Scan Tooling Provided

KFM provides the following local tools via the **KFM Developer Toolkit (KFM-DTK)**:

| Scan Type            | Local Tool              | Description                                        |
|----------------------|------------------------|----------------------------------------------------|
| Namespace Collision  | `kfm-ns-scan`          | Scans public registries for KFM-like names         |
| Registry Isolation   | `kfm-reg-audit`        | Validates registry URLs + TLS pinning              |
| Pinning Integrity    | `kfm-lock-verify`      | Ensures lockfiles match SBOM & hashes              |
| SBOM Drift           | `kfm-sbom-diff`        | Compares deps to last sealed SBOM                  |
| Provenance/Signatures| `kfm-provenance-verify`| Validates artifact & commit signatures + provenance|
| Fallback Mode        | `kfm-fallback-test`    | Simulates degraded mirror / fallback behavior      |

These tools are designed to mirror CI checks, locally.

---

## 🔧 Installation (KFM Developer Toolkit)

Install via PyPI:

```bash
pip install kfm-dtk
```

Or from source:

```bash
git clone https://github.com/bartytime4life/Kansas-Frontier-Matrix.git
cd tools/kfm-dtk
pip install -e .
```

> All local scans require Python ≥ 3.11.

---

## 🛰️ Running Local Namespace Scans

Detects public-package collisions and suspicious variants:

```bash
kfm-ns-scan .
```

Flags:

- First-publish collisions  
- Typosquatting / homoglyph variants  
- Suspicious namespace permutations  
- Public names identical to internal packages  

Results written to:

```text
docs/security/supply-chain/dependency-confusion/policy/evidence/namespace-scan.json
```

---

## 🔒 Checking Registry Isolation Locally

Validate that your environment uses **only** KFM-approved mirrors:

```bash
kfm-reg-audit --strict
```

Checks:

- No references to `pypi.org`, `registry.npmjs.org`, `crates.io`, etc.  
- TLS pinning & CA correctness  
- Mirror allow-list compliance  
- No fallback registrar behavior  

---

## 📦 Validating Dependency Pinning

```bash
kfm-lock-verify
```

Ensures:

- All deps are fully pinned (version + registry + hash)  
- No floating versions  
- Lockfiles match SBOM  
- No cross-registry contamination  

---

## 🧬 Verifying SBOM Drift Locally

```bash
kfm-sbom-diff --local
```

Detects:

- Hash mismatches  
- Package additions/removals  
- Unapproved upgrades  
- Potential shadow dependencies  

---

## ✍️ Local Provenance & Signature Verification

```bash
kfm-provenance-verify --all
```

Validates:

- Cosign signatures  
- GPG commit/tag signatures  
- SLSA provenance bundles  
- Provenance metadata → SBOM → artifact consistency  

Unsigned / unverifiable components → **ERROR** and remediation instructions.

---

## 🧯 Testing Fallback Activation

Simulate failing mirrors or metadata drift:

```bash
kfm-fallback-test
```

Triggers:

- Lockfile freeze  
- Local-only artifact mode  
- Registry quarantine simulation  

Use this to debug registry failures and confirm fallback logic matches policy in  
`../policy/fallback-controls.md`.

---

## 🕰️ Version History

| Version  | Date       | Notes                                              |
|----------|------------|----------------------------------------------------|
| v11.2.2  | 2025-11-30 | Extended metadata; layout moved; v11.2.2 alignment |
| v11.2.1  | 2025-10-18 | Added fallback simulation and provenance checks    |
| v11.2.0  | 2025-09-02 | Initial local/manual scan guidance                 |

---

<div align="center">

🧪 [Automated Checks](./README.md) • 🔒 [Registry Isolation](../policy/registry-isolation.md) • 🧭 [Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
