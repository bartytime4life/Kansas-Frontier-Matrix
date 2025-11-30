---
title: "⚠️ KFM v11.2.2 — Implicit Upgrade Attack (Dependency-Confusion Example)"
path: "docs/security/supply-chain/dependency-confusion/examples/implicit-upgrade-attack.md"
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
  cidoc: "E13 Attribute Assignment"
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
  - "docs/security/supply-chain/dependency-confusion/examples/implicit-upgrade-attack.md@v11.2.1"
  - "docs/security/supply-chain/dependency-confusion/examples/implicit-upgrade-attack.md@v11.2.0"
  - "docs/security/supply-chain/dependency-confusion/examples/README.md"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: false

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:security:dependency-confusion:examples:implicit-upgrade-attack:v11.2.2"
semantic_document_id: "kfm-depconf-examples-implicitupgrade-v11.2.2"
event_source_id: "ledger:depconf.examples.implicitupgrade.v11.2.2"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"

ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "diagram-extraction"
  - "metadata-extraction"

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
    - "📘 Background"
    - "🗂️ Directory Layout"
    - "🧨 Example Scenario"
    - "🧪 CI Detection Output (Simulated)"
    - "🚨 Why This Attack Works (in vulnerable systems)"
    - "🛡️ How KFM v11.2.2 Prevents This Attack"
    - "🧭 Developer Guidance"
    - "🕰️ Version History"
---

<div align="center">

# ⚠️ **Implicit Upgrade Attack Example**  
`docs/security/supply-chain/dependency-confusion/examples/implicit-upgrade-attack.md`

**Purpose:**  
Demonstrate how **implicit dependency upgrades**—triggered by floating versions,  
resolver fallback behavior, or dynamic version selection—can lead to a full dependency-confusion  
compromise even when developers believe they are using internal packages.

</div>

---

## 📘 Background

An **implicit upgrade attack** occurs when:

1. A dependency is declared with a **floating** version:
   ```
   ^3.8.0
   ~3.8
   >=3.8,<4.0
   * 
   latest
   ```
2. The resolver evaluates available versions across *all* configured registries.  
3. An attacker publishes a **higher public version** (e.g., `99.0.0`) under the same name.  
4. The resolver quietly selects the public version because:
   - It satisfies the version specifier  
   - It outranks the internal version  
   - Public registries appear “authoritative”  
   - The environment silently falls back to a public registry  
   - Lockfile is missing, stale, or ignored  

This attack often succeeds in:

- Local developer environments  
- Misconfigured CI runners  
- Environments where lockfiles are ignored  
- Ecosystems with permissive default resolver behavior (npm/pip/poetry/cargo)

---

## 🗂️ Directory Layout

~~~text
📁 dependency-confusion/
└── 📁 examples/
    ├── 📄 README.md
    ├── 📄 namespace-collision-basic.md
    ├── 📄 namespace-collision-firstpublish.md
    ├── 📄 namespace-collision-versionrace.md
    ├── 📄 typosquat-examples.md
    ├── 📄 registry-fallback.md
    ├── 📄 mirror-drift.md
    ├── 📄 sbom-drift-basic.json
    ├── 📄 lockfile-drift-attack.md
    ├── 📄 invalid-cosign.sig
    ├── 📄 missing-provenance.json
    ├── 📄 sandbox-network-leak.md
    └── 📄 implicit-upgrade-attack.md   # This file
~~~

---

## 🧨 Example Scenario

### Internal KFM Package
```txt
package: kfm-vision-core
version: 3.8.0
registry: https://kfm-pypi.internal/simple
```

### Developer Dependency Declaration  
❌ **Incorrect (floating):**
```txt
kfm-vision-core >=3.0
```

### Attacker Publishes a Malicious Public Version
```txt
package: kfm-vision-core
version: 99.0.0
registry: https://pypi.org/simple
files: malicious wheel, telemetry exfiltration payload
```

### Resolver Behavior (Simulated)
```text
resolver: evaluating "kfm-vision-core>=3.0"
found internal: 3.8.0
found public: 99.0.0
selected version: 99.0.0 (highest matching version)
registry: pypi.org
WARNING: resolver fallback detected
```

---

## 🧪 CI Detection Output (Simulated)

```text
[dependency-integrity] ERROR: floating version specifier detected: ">=3.0"
[namespace-monitor]   WARNING: public version outranks private version.
[policy]              FAIL: implicit upgrade attack detected.
[evidence]            Updated: sbom-diff.json, namespace-scan.json
```

---

## 🚨 Why This Attack Works (in vulnerable systems)

- Floating versions allow higher numbers to override internal versions  
- Resolver silently falls back to public registry  
- No lockfile or stale lockfile  
- Public registry not blocked  
- SBOM not enforced  
- Provenance not validated  
- Metadata drift undetected  
- No namespace quarantine system  

---

## 🛡️ How KFM v11.2.2 Prevents This Attack

### ✔ Deterministic Pinning  
No floating versions allowed. All dependencies must specify:

```txt
version + registry + hash
```

### ✔ Registry Isolation  
Public registries: **blocked**  
Internal mirrors: **forced**

### ✔ SBOM Locking  
Dependency graph mismatches → immediate halt.

### ✔ Provenance Enforcement  
Malicious public packages cannot produce valid:

- Cosign signatures  
- SLSA provenance  
- Digest-matching SBOM entries  

### ✔ Namespace Scanning  
Detects suspicious public publishing activity.

### ✔ Developer Pre-Commit Rules  
Local hooks flag any floating or dynamic version specifiers.

### ✔ Hermetic Sandbox  
No resolver fallback allowed.

---

## 🧭 Developer Guidance

To avoid implicit upgrade attacks:

- **Never** use floating versions  
- Always rely on **lockfiles**  
- Ensure local environment uses correct KFM mirrors  
- Regenerate SBOM when modifying dependencies  
- Run local scans:
  ```bash
  kfm-lock-verify
  kfm-ns-scan .
  kfm-sbom-diff --local
  ```

---

## 🕰️ Version History

| Version  | Date       | Notes |
|----------|------------|--------|
| v11.2.2  | 2025-11-30 | Full extended metadata & layout upgrade for implicit upgrade example |

---

<div align="center">

📚 [Examples Index](./README.md) • 🧨 [First-Publish Example](./namespace-collision-firstpublish.md) • 🧭 [Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
