---
title: "🧪 Kansas Frontier Matrix — Event Validator Engine (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/architecture/event-models/validators/README.md"
version: "v10.3.1"
last_updated: "2025-11-13"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/pipelines-event-validators-v1.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🧪 **Kansas Frontier Matrix — Event Validator Engine**  
`src/pipelines/architecture/event-models/validators/README.md`

**Purpose:**  
Define the **validation engine** that enforces structural correctness, FAIR+CARE governance, sovereignty rules, idempotency guarantees, and provenance integrity across all KFM pipeline event envelopes.  
These validators ensure **only compliant, ethical, and reproducible events** enter the KFM pipeline execution graph.

<img alt="Docs" src="https://img.shields.io/badge/Docs-MCP_v6.3-blue"/>
<img alt="License" src="https://img.shields.io/badge/License-MIT-green"/>
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Certified-orange"/>
<img alt="Status" src="https://img.shields.io/badge/Status-Validators-success"/>

</div>

---

## 📘 Overview

The KFM validator engine:

- Validates **event schema** (JSON Schema, Pydantic v2)
- Performs **FAIR+CARE** enforcement on CARE labels and sovereignty metadata
- Enforces **idempotency** by recomputing and comparing idempotency keys
- Runs **license & attribution checks**
- Ensures **provenance completeness** (source IDs, checksums, toolchains)
- Runs **sensitivity + redaction consistency** checks
- Emits telemetry + governance logs for every validation

**No event may be executed by a pipeline unless it passes all validator stages.**

---

## 📁 Directory Layout

~~~~~text
src/pipelines/architecture/event-models/validators/
├── README.md                        # This file
├── validator_base.py                # Shared validator utilities
├── schema_validator.py              # JSON Schema + Pydantic structural checks
├── governance_validator.py          # CARE, sovereignty, consent enforcement
├── provenance_validator.py          # Checksums, lineage, source validation
├── idempotency_validator.py         # Key recomputation + dedupe checks
├── license_validator.py             # SPDX license + attribution gate
├── validator_manifest.json          # Combined validator metadata + signature
└── tests/                           # Unit tests for each validator module
~~~~~

---

## 🧩 Validator Architecture (Indented Mermaid)

~~~~~mermaid
flowchart TD
  A["Incoming Event<br/>Ingest · ETL · AI · Metadata · Governance"] --> B["Schema Validator<br/>JSONSchema · Pydantic"]
  B --> C["Governance Validator<br/>CARE · Sovereignty · Consent"]
  C --> D["Provenance Validator<br/>Checksums · Source IDs · Tools"]
  D --> E["Idempotency Validator<br/>Recompute sha256 · Replay Safety"]
  E --> F["License Validator<br/>SPDX · Attribution"]
  F --> G["Validator Manifest<br/>Telemetry · Governance Ledger"]
~~~~~

---

## 🧱 1. Schema Validator

Validates:

- JSON Schema compliance  
- Required fields (`event_id`, `dataset_id`, `care_label`, etc.)  
- Type correctness  
- Enum compliance (`event_type`, `care_label`, `review_status`)  
- Nested `provenance` structure  

Events failing schema validation **never proceed** to execution.

---

## ⚖️ 2. Governance Validator

Applies FAIR+CARE rules:

- CARE label enforcement  
- Sovereignty metadata validation  
- Sensitive/restricted dataset rules  
- Required masking rules (`h3_r7`, fuzzing)  
- Heritage/tribal content review checks  

Governance violations produce:

- Explicit governance error  
- Telemetry entry  
- Ledger record  

---

## 🧬 3. Provenance Validator

Ensures:

- All `source_ids` present  
- All `source_checksums` valid  
- Tools recorded (`python`, `gdal`, `spaCy`)  
- PROV-O lineage compatibility  

Fails if:

- Checksums mismatch  
- Missing sources  
- Tools undefined  

---

## ♻️ 4. Idempotency Validator

Recomputes:

- `sha256(dataset_id + version + source_uri)`

Checks:

- KV store for previously-seen keys  
- Replay behavior  
- Correct correlation ID linking  

Events failing idempotency checks result in:

- Execution halt  
- No-op path  
- Telemetry to identify duplicates  

---

## 📜 5. License Validator

Enforces:

- SPDX license identification  
- Prohibited licenses (non-redistributable)  
- Attribution presence  
- Compatibility with FAIR  

Governance blocks occur if:

- License incompatible  
- Missing attribution  
- Ambiguous legal statement  

---

## 📡 Telemetry & Governance Logging

All validators must emit telemetry entries:

- `event_id`  
- `validation_status`  
- `care_label`  
- `sovereignty_conflicts`  
- `checksum_failures`  
- `idempotency_conflicts`  
- `license_failures`  
- `energy_wh`  
- `co2_g`

Telemetry stored at:

~~~~~text
../../../../../../releases/v10.3.0/focus-telemetry.json
~~~~~

Governance ledger updates stored at:

~~~~~text
../../../../../../docs/reports/audit/event_validation_ledger.json
~~~~~

---

## 🧾 Example Validator Manifest Entry

~~~~~json
{
  "validator_id": "event_validator_v10.3.1",
  "modules": [
    "schema_validator",
    "governance_validator",
    "provenance_validator",
    "idempotency_validator",
    "license_validator"
  ],
  "validation_passed": true,
  "checksum_verified": true,
  "care_enforced": true,
  "timestamp": "2025-11-13T22:01:00Z",
  "telemetry_linked": true,
  "governance_ref": "docs/reports/audit/event_validation_ledger.json"
}
~~~~~

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|--------|--------|---------|
| v10.3.1 | 2025-11-13 | Pipeline Architecture Team | Introduced validator engine with FAIR+CARE, provenance, idempotency, and license enforcement modules for v10.3. |

---

<div align="center">

**Kansas Frontier Matrix — Event Validation Engine**  
Strong Contracts × Ethical Enforcement × Immutable Provenance  
© 2025 Kansas Frontier Matrix — MIT License  

[Back to Event Models](../README.md)

</div>
