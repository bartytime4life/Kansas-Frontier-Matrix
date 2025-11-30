---
title: "📜 KFM v11 — ETL Governance Event Records (PROV-O · Energy/Carbon · SLSA · FAIR+CARE)"
path: "docs/telemetry/etl-governance-events/README.md"
version: "v11.2.3"
last_updated: "2025-11-29"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Telemetry WG · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
backward_compatibility: "v10.x → v11.x compliant"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../../releases/v11.2.3/signature.sig"
attestation_ref: "../../../releases/v11.2.3/slsa-attestation.json"
sbom_ref: "../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.3/manifest.zip"

telemetry_ref: "../../../releases/v11.2.3/etl-governance-events.json"
telemetry_schema: "../../../schemas/telemetry/etl-governance-event-v1.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-Aligned · Provenance-Logged · Responsible Computing"
classification: "Public (Governed)"
sensitivity: "Low/Moderate"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "United States · Kansas"
---

<div align="center">

# 📜 **ETL Governance Event Records**  
### Deterministic · Cryptographically Signed · FAIR+CARE-Aligned  
`docs/telemetry/etl-governance-events/`

**Purpose**  
Define how **every ETL execution** in KFM becomes a small, immutable, cryptographically verifiable  
**governance event**, containing PROV-O lineage, SLSA attestations, energy/carbon measurement,  
STAC/DCAT dataset references, CI/CD artifacts, and FAIR+CARE ethical metadata.

</div>

---

## 🧭 1. Purpose

Every dataset update in KFM produces a **machine-actionable governance event** that includes:

- **PROV-O lineage:** agents, activities, used/generated entities  
- **Execution metadata:** start/finish timestamps, runtime, status  
- **STAC/DCAT references:** consumed/produced datasets  
- **Telemetry:** energy (kWh), carbon (CO₂e), node count  
- **Artifacts:** logs, SBOMs, manifests, attestations  
- **Cryptographic integrity:** SHA-256 digests, cosign signatures, SLSA provenance  

This directory houses:

- Official event **schema**  
- Usage **specifications**  
- **Examples**  
- Validators  
- Storage/retention rules  

---

## 🗂️ 2. Directory Layout (Emoji-Prefix Standard)

~~~text
docs/telemetry/etl-governance-events/
├── 📄 README.md                          # This file
├── 📁 specs/
│   ├── 📄 event-schema.md                # Human-readable schema reference
│   ├── 📄 prov-patterns.md               # PROV-O usage patterns
│   ├── 📄 energy-carbon.md               # Rules for kWh & CO₂e accounting
│   └── 📄 cicd-integration.md            # How CI/CD constructs + signs events
│
├── 📁 examples/
│   ├── 📄 sample-event.json              # Canonical event example
│   ├── 📄 prov.jsonld                    # Example PROV-O block
│   └── 📄 energy.json                    # Example energy/carbon block
│
├── 🛠️ validators/
│   ├── 🧪 validate-event.py              # CLI validator tool
│   └── 📄 cli.md                         # Usage instructions
│
└── 🗄️ storage/
    ├── 📄 retention-policy.md            # Archival/expiry rules
    └── 📄 indexing-strategy.md           # Indexing & search strategies
~~~

---

## 🏛️ 3. What is an ETL Governance Event?

A **Governance Event** is a signed, FAIR+CARE-compliant, PROV-O structured JSON record that documents:

- What pipeline ran  
- What datasets were used  
- What was produced  
- What energy/carbon was consumed  
- What artifacts were created  
- What provenance chain was generated  
- Whether the job succeeded, failed, or produced partial output  

It conforms to:

- **ETL Governance Event Schema v1**  
- **W3C PROV-O**  
- **SLSA Level 3** provenance  
- **OpenTelemetry conventions**  
- **ISO 50001 energy**  
- **ISO 14064 carbon**  
- **FAIR+CARE governance rules**

It is the **root authority** for ETL lineage.

---

## 🔧 4. Event Schema (Root Fields Summary)

Schema:  
`schemas/telemetry/etl-governance-event-v1.json`

Key fields:

| Field | Purpose |
|-------|---------|
| `event_id` | Deterministic UUID or URN |
| `pipeline` | Fully-qualified pipeline name |
| `dataset` | STAC/DCAT dataset identifier |
| `started_at` / `finished_at` | ISO timestamps |
| `status` | success / failure / partial |
| `prov` | PROV-O lineage block |
| `energy` | Energy usage + runtime details |
| `carbon` | CO₂e footprint & emission factors |
| `artifacts` | SHA256 digests of logs, SBOMs, manifests, attestations |

### 📦 Minimal Example

~~~json
{
  "event_id": "urn:kfm:etl:soil-merge:2025-11-29T06:00Z",
  "pipeline": "kfm.etl.soils.merge@v11",
  "status": "success",
  "prov": {
    "agent": "urn:ci:github-actions",
    "activity": "urn:etl:run",
    "entities": [
      {
        "role": "usedEntity",
        "uri": "urn:stac:collection:soil-gnatsgo@2025-11",
        "hash": "sha256-..."
      }
    ]
  }
}
~~~

---

## 🏗️ 5. How CI/CD Creates Governance Events

All ETL pipelines must follow this process:

### 1. Emit raw telemetry  
Start/stop energy, runtime, node count, CPU time.

### 2. Generate PROV-O  
Produce JSON-LD describing agent/activity/entity graph.

### 3. Assemble event JSON  
Combine PROV-O + telemetry + dataset references + artifacts.

### 4. Validate  
Run JSON schema + CLI validator.

### 5. Sign  
`cosign sign-blob` over event file.

### 6. Produce SLSA attestation  
SLSA L3 provenance referencing the event.

### 7. Upload artifacts  
Logs, provenance, event JSON, signatures, SBOMs.

### 8. Append to governance ledger  
Long-term auditable record.

---

## 🌱 6. Energy & Carbon Accounting (ISO-Aligned)

Events MUST include:

- Total **kWh**  
- **Runtime seconds**  
- **Node count**  
- Carbon footprint (**gCO₂e**)  
- Emission factors  
- Region & hardware class  

References:

- `schemas/telemetry/energy-v2.json`  
- `schemas/telemetry/carbon-v2.json`

---

## 🧬 7. PROV-O Integration

Every event must encode:

- `prov:Activity` (the ETL run)  
- `prov:Agent` (CI runner, orchestrator)  
- `prov:used` (input datasets)  
- `prov:generated` (outputs)  

These events:

- Complement STAC/DCAT dataset metadata  
- Enhance lineage clarity  
- Enable Focus Mode narratives  
- Support reproducible ETL replay

---

## 🔍 8. Validator Tools

Validator scripts ensure:

- JSON Schema conformance  
- Required fields present  
- Artifact hashes correct  
- Optionally: signature presence & validity  

Usage:

~~~bash
python validators/validate-event.py examples/sample-event.json
~~~

---

## 🗄️ 9. Archival & Retention

Governance events are **immutable**.

Retention policies ensure:

- Long-term reproducibility  
- Energy/carbon sustainability tracking  
- FAIR+CARE ethical auditing  
- Governance verifiability  

Stored per:

- `storage/retention-policy.md`  
- `storage/indexing-strategy.md`

---

## 🧭 10. Version History

| Version | Date       | Notes                                                                                   |
|--------:|------------|-----------------------------------------------------------------------------------------|
| v11.2.3 | 2025-11-29 | Metadata aligned to v11.2.3; safe-fence protocol applied; emoji directory style updated |
| v11.2.2 | 2025-11-29 | Full rewrite for KFM-MDP v11.1; energy/carbon telem v2; SLSA + PROV-O proofs            |

---

<div align="center">

📜 **Kansas Frontier Matrix — Telemetry & Governance Layer (v11.2.3)**  
Provenance · Observability · Sustainable Intelligence  

[📘 Docs Root](../../../..) · [📡 Telemetry Index](../README.md) · [⚖ Governance](../../standards/governance/ROOT-GOVERNANCE.md)

</div>
