---
title: "🚨 KFM v11.2.2 — Dependency-Confusion Incident Log (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/security/supply-chain/dependency-confusion/policy/incidents.md"
version: "v11.2.2"
last_updated: "2025-11-30"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Security Council · FAIR+CARE"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

signature_ref: "../../../../../../releases/v11.2.2/signature.sig"
attestation_ref: "../../../../../../releases/v11.2.2/slsa-attestation.json"
sbom_ref: "../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.2/release-manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.2/security-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/security-v3.json"
energy_schema: "../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

doc_kind: "Security · Incident-Log"
intent: "dependency-confusion-forensics · supply-chain-incident-response"

fair_category: "F1-A1-I1-R1"
care_label: "CARE · Governance · Security Oversight"
classification: "Security · Supply Chain · Forensics"
sensitivity: "Security-Sensitive (Non-personal)"
sensitivity_level: "High"
public_exposure_risk: "Low"
indigenous_rights_flag: true
risk_category: "High"
redaction_required: false

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
ttl_policy: "Permanent archive"
sunset_policy: "Superseded by next incident-log version"

ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "Dataset"
  prov_o: "prov:Collection"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "DCAT 3.0"
  - "STAC 1.0.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/security/supply-chain/dependency-confusion/policy/incidents.md@v11.2.1"
  - "docs/security/supply-chain/dependency-confusion/policy/incidents.md@v11.2.0"
  - "docs/security/supply-chain/dependency-confusion/policy/README.md"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: false

immutability_status: "append-only"
doc_uuid: "urn:kfm:doc:security:dependency-confusion:policy:incidents:v11.2.2"
semantic_document_id: "kfm-depconf-policy-incidents-v11.2.2"
event_source_id: "ledger:depconf.policy.incidents.v11.2.2"

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
  - "unverified-architectural-claims"
  - "speculative-additions"
  - "narrative-fabrication"
  - "governance-override"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🧭 Incident Entry Schema (Required)"
    - "📂 Current Incident Log (v11.2.2)"
    - "🔐 Incident Lifecycle Requirements"
    - "🕰️ Version History"
---

<div align="center">

# 🚨 **Dependency-Confusion Incident Log**  
`docs/security/supply-chain/dependency-confusion/policy/incidents.md`

**Purpose:**  
Serve as the authoritative, immutable forensic register for all dependency-confusion–related  
incidents detected or mitigated by KFM v11.2.2 supply-chain controls.  
Each entry is permanently auditable, PROV-O linked, and governed by the Security Council.

</div>

---

## 📘 Overview

This log records all **confirmed or suspected** dependency-confusion incidents, including:

- Namespace collisions  
- Rogue/shadow package injection  
- Malicious dependency resolution attempts  
- Unauthorized registry access  
- SBOM drift suggesting compromise  
- Provenance chain failures  
- SLSA violations  
- Registry poisoning indicators  

Each entry MUST:

- Follow the required schema  
- Include full evidence linkage  
- Reflect FAIR+CARE compliance  
- Be approved by the Security Council  
- Be preserved indefinitely for governance & forensic review  

All machine evidence is stored in:

```
docs/security/supply-chain/dependency-confusion/policy/evidence/
```

---

## 🧭 Incident Entry Schema (Required)

Every incident MUST include:

```yaml
id: INC-DC-YYYY-NNNN
date_detected: "YYYY-MM-DD"
severity: low | medium | high | critical
status: "open" | "mitigated" | "false-positive" | "under-review"
vector: "namespace-collision" | "rogue-package" | "registry-leak" |
        "sbom-drift" | "attestation-failure" | "mirror-drift" | "other"
description: >
  Clear, factual description of the suspicious or malicious behavior.
evidence_refs:
  - "evidence/namespace-scan.json"
  - "evidence/sbom-diff.json"
affected_components:
  - "pipelines/batch/etl"
  - "web/frontend"
  - "graph/neo4j-loader"
root_cause: >
  Explanation of confirmed cause (if known).
mitigation:
  actions:
    - "mirror lock activated"
    - "namespace quarantined"
    - "dependency pinned to hash"
    - "sealed dependency snapshot used"
  completed: true | false
follow_up_actions:
  - "SLSA chain verification"
  - "dependency replacement roadmap"
  - "SBOM regeneration"
date_closed: "YYYY-MM-DD"
approved_by:
  - name: "Security Council Member"
    role: "Council"
```

All fields are mandatory.  
Missing or malformed fields → **CI merge block**.

---

## 📂 Current Incident Log (v11.2.2)

> 🚨 *This registry begins empty. All entries must be added via Security-Council–approved governance PRs.*

_No incidents recorded._

---

## 🔐 Incident Lifecycle Requirements

### 1. 🕵️ Detection  
All anomalies from CI, namespace-monitor, registry checks, or provenance verifiers  
must generate an incident stub.

### 2. 🧪 Investigation  
Security Council performs:

- Evidence correlation  
- Risk scoring  
- Impact assessment  
- Threat attribution  

### 3. 🛡️ Mitigation  
Mitigation MUST:

- Begin immediately  
- Be reproducible  
- Be logged with evidence refs  
- Include namespace quarantining + mirror isolation when relevant  

### 4. 🧾 Closure  
An incident may be closed only after:

- Full mitigation  
- SBOM/provenance realignment  
- Evidence verification  
- Security Council approval  

---

## 🕰️ Version History

| Version  | Date       | Notes |
|----------|------------|---------------------------------------------|
| v11.2.2  | 2025-11-30 | Full extended metadata integration           |
| v11.2.1  | 2025-10-26 | Added mirror-drift vector                    |
| v11.2.0  | 2025-09-10 | Initial forensic schema + evidence linkage   |

---

<div align="center">

🛡️ [Policy Overview](./README.md) • 📁 [Evidence Archive](./evidence/README.md) • 🧭 [Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
