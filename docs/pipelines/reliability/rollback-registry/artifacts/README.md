---
title: "♻️ KFM v11.2.2 — Rollback Artifact Bundles (OCI · tar.zst · SLSA Verified)"
path: "docs/pipelines/reliability/rollback-registry/artifacts/README.md"
version: "v11.2.2"
last_updated: "2025-11-30"
review_cycle: "Quarterly · Reliability Engineering · FAIR+CARE Council"
release_stage: "Stable / Governed"
status: "Active / Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

doc_uuid: "urn:kfm:pipelines:rollbackregistry:artifacts:v11.2.2"
semantic_document_id: "kfm-rollback-artifact-bundles"
event_source_id: "ledger:pipelines/rollback-registry/artifacts"
immutability_status: "version-pinned"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
signature_ref: "../../../../../releases/v11.2.2/signature.sig"
attestation_ref: "../../../../../releases/v11.2.2/slsa-attestation.json"

telemetry_ref: "../../../../../releases/v11.2.2/pipelines-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/rollback-registry-v1.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"

doc_kind: "Subsystem Specification"
intent: "kfm-rollback-artifact-bundles"
classification: "Internal · Safety-Critical"
lifecycle_stage: "LTS"

fair_category: "F1-A1-I3-R4"
care_label: "Respectful · Minimization"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "60 months"
sunset_policy: "Superseded by v12 rollback bundle structure"
---

<div align="center">

# ♻️ **Rollback Artifact Bundles (KFM v11.2.2)**  
### *Immutable · Deterministic · SLSA-Verified Rollback Packages*  

`docs/pipelines/reliability/rollback-registry/artifacts/README.md`

**Purpose**  
Document the structure, governance, and validation rules for **rollback-bundle artifacts**  
stored under the Rollback Registry’s `artifacts/` directory.  
These bundles contain the **entire system state** required for perfect rollback and replay.

</div>

---

## 🗂️ Directory Layout

~~~text
docs/pipelines/reliability/rollback-registry/artifacts/
├── 📄 README.md                       # This file
└── 📦 <lakefs_commit>.tar.zst         # Immutable rollback bundle
~~~

Each filename **must** match:

**`<lakefs_commit>.tar.zst`**

or the OCI equivalent:

**`oci://kfm-registry/rollback/<lakefs_commit>`**

Bundles are **immutable**, **SLSA-attested**, and tracked through the registry index.

---

## 📦 Bundle Contents (Authoritative Specification)

A rollback artifact contains **all** data necessary to restore KFM subsystems  
to the **exact** state at a specific lakeFS commit.

Each bundle includes:

### 1. ❄️ Frozen STAC Snapshots  
- Collections + Items pinned to lakeFS refs  
- No mutable HTTP URLs  
- STAC validation reports  
- Checksum manifest

### 2. ⚙️ Pipeline Configurations  
- All YAML/TOML/JSON configs loaded during the run  
- SHA256-pinned  
- Config-schema validation included

### 3. 🧠 Model Binaries  
- Focus Transformer / Downscaling models / Climate models / Embedding stacks  
- Exact versions  
- SHA256 + signature metadata  
- Provenance block with training lineage (if applicable)

### 4. 🛰️ Raster / Vector Data  
- Sentinel-1, GOES, HRRR, NEXRAD, GRACE, GLDAS, NWM outputs used in the run  
- Only frozen lakeFS or S3-versioned objects allowed

### 5. 🔍 OpenLineage Run Context  
- Run ID  
- Job facets  
- Input/output dataset lists  
- Parent/child run relationships

### 6. 📡 OTel Trace Tree  
- Full trace graph  
- Span metadata  
- Errors/events/exceptions  
- Resource attributes

### 7. 🔐 SLSA Attestation  
- Provenance statement  
- in-toto metadata  
- Build pipeline chain-of-custody  

### 8. 🌱 Energy & Carbon Record  
- Energy consumed (kWh)  
- CO2-equivalent emissions  
- Renewable/offset metadata  
- CI energy source annotations  

### 9. 🧾 Checksum Ledger  
- SHA256 for:  
  - bundle  
  - models  
  - configs  
  - STAC files  
  - lineage documents  

---

## 📑 Internal Bundle Manifest (Within Each tar.zst)

Every rollback bundle contains:

```
MANIFEST.yaml        # internal manifest
checksums.json       # cryptographic ledger
lineage.json         # PROV-O lineage record
stac/                # frozen STAC assets (lakeFS refs)
models/              # model binaries + metadata
configs/             # full pipeline configs
otel/                # trace dump
openlineage/         # run context
energy/              # kWh + CO2e
carbon/              # lifecycle info
attestation/         # SLSA + signatures
```

**Everything inside must be deterministic and reproducible.**

---

## 🔐 Governance Requirements

Rollback bundles must:

- be **append-only**  
- never be replaced or mutated  
- include **complete provenance**  
- include **SLSA Level ≥1** attestation  
- attach **energy & carbon telemetry**  
- pass KFM Reliability Checks:
  - metadata schema validation  
  - checksum validation  
  - frozen STAC and frozen lakeFS refs  
  - OpenLineage + OTel link consistency  
  - artifact immutability enforcement  

---

## 🧪 CI/CD Validation

For each bundle:

- Validate **bundle manifest** against schema  
- Validate **checksums**  
- Validate **STAC collections/items**  
- Validate **lakeFS refs** exist  
- Validate **SLSA attestation signature**  
- Validate **OpenLineage run**  
- Validate **OTel trace graph**  
- Validate **CF/CRS consistency** for rasters  
- Validate **energy/carbon schemas**  

All failures block ingestion into the registry index.

---

## 📬 Publishing New Bundles (Internal Workflow)

1. Airflow / LangGraph freeze lakeFS commit  
2. Export configs, models, STAC  
3. Export lineage + telemetry  
4. Package into `.tar.zst` or OCI manifest  
5. Hash + sign (SHA256 → signature → SLSA)  
6. Upload to `rollback-registry/artifacts/`  
7. Update registry index  
8. Emit governance event  
9. Notify reliability channel  

---

## 🕰️ Version History

| Version | Date       | Summary                                                        |
|--------:|------------|----------------------------------------------------------------|
| v11.2.2 | 2025-11-30 | Initial governed rollback-bundle spec; OCI + energy/carbon v2. |
| v11.2.1 | 2025-11-29 | Added bundle structure & checksum ledger definition.           |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
[📚 Docs Home](../../../../README.md) · [📏 Standards Index](../../../standards/README.md) · [🛡 Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

