---
title: "♻️ KFM v11.2.2 — Rollback Artifact Registry (lakeFS · OpenLineage · OTel · PROV-O)"
path: "docs/pipelines/reliability/rollback-registry/README.md"
version: "v11.2.2"
last_updated: "2025-11-30"
release_stage: "Stable / Governed"
status: "Active / Enforced"
review_cycle: "Quarterly · Reliability Engineering · FAIR+CARE Council"
lifecycle_stage: "LTS"
backward_compatibility: "Guaranteed: v10.x → v11.x"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

doc_uuid: "urn:kfm:pipelines:rollback-registry:v11.2.2"
semantic_document_id: "kfm-rollback-registry"
event_source_id: "ledger:pipelines/rollback-registry"
immutability_status: "version-pinned"

sbom_ref: "../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.2/manifest.zip"
signature_ref: "../../../../releases/v11.2.2/signature.sig"
attestation_ref: "../../../../releases/v11.2.2/slsa-attestation.json"

telemetry_ref: "../../../../releases/v11.2.2/pipelines-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/rollback-registry-v1.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"

doc_kind: "System Specification"
intent: "kfm-rollback-registry"
classification: "Internal · Safety-Critical"
fair_category: "F1-A1-I3-R4"
care_label: "Respectful · Minimization"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
ttl_policy: "60 months"
sunset_policy: "Superseded by v12 Rollback + Replay System"
---

<div align="center">

# ♻️ **KFM v11.2.2 — Rollback Artifact Registry**  
### **Diamond⁹ Ω / Crown∞Ω Ultimate Certified**  
### *Deterministic · Immutable · Cryptographically Verified Rollbacks for the Kansas Frontier Matrix*

`docs/pipelines/reliability/rollback-registry/README.md`

**Purpose**  
Provide **guaranteed, deterministic, fully-governed rollback artifacts** for all KFM pipelines,  
models, datasets, UI builds, and Story Node generation systems — with strict provenance,  
cryptographic signatures, STAC/DCAT-safe dataset freezing, and OTel/OpenLineage telemetry.

</div>

---

## 🧭 1. Overview

The **Rollback Artifact Registry** is an **append-only**, **cryptographically validated**,  
**SLSA-attested**, **lakeFS-pinned** registry mapping:

**`lakefs_commit` → complete rollback bundle**

Each rollback bundle includes:

- ❄️ **Frozen STAC datasets** (collection + items pinned to lakeFS refs)  
- ⚙️ **Pipeline configs** (exact SHA)  
- 🧠 **Model binaries** (exact versions used in production)  
- 🛰️ **Raster/vector assets** pinned to a lakeFS commit  
- 🔍 **OpenLineage run context**  
- 📡 **OTel trace**, span tree, and execution metadata  
- 🔐 **Signatures + SLSA attestations**  
- ⚡ **Energy & carbon telemetry** (governed environmental metrics)

This registry ensures **zero-ambiguity**, **reversible**, **replayable** system behavior  
across v11 pipelines and subsystems.

---

## 🗂️ 2. Directory Layout

~~~text
rollback-registry/
├── 📂 artifacts/                     # Immutable rollback bundles (OCI or .tar.zst)
│   └── <lakefs_commit>.tar.zst
├── 📂 index/
│   ├── 📄 rollback-index.jsonl       # Canonical append-only ledger
│   └── 📄 rollback-index.parquet     # Analytics-friendly mirror
└── 📂 meta/
    └── 📄 <lakefs_commit>.yaml       # Human-readable manifest (governed)
~~~

---

## 🏷️ 3. Registry Index Schema (Authoritative)

Each row in `rollback-index.jsonl` and its Parquet mirror **must** follow:

```json
{
  "lakefs_repo": "kfm-main",
  "lakefs_branch": "prod",
  "lakefs_commit": "abc123",
  "created_at": "2025-11-30T12:00:00Z",

  "producer": "airflow:dag=kfm-promote",
  "openlineage_run_id": "uuid-...",
  "otel_trace_id": "trace-...",

  "artifact_uri": "s3://kfm-registry/rollback/artifacts/abc123.tar.zst",

  "data_snapshot": [
    {
      "stac": "s3://....../collection.json",
      "lakefs_ref": "lakefs://kfm@abc123/path"
    }
  ],

  "models": [
    {
      "name": "focus-transformer",
      "version": "3.1.0",
      "uri": "s3://models/focus-transformer/3.1.0.bin"
    }
  ],

  "configs": [
    {
      "path": "configs/pipeline.yaml",
      "sha256": "..."
    }
  ],

  "checksums": {
    "artifact_sha256": "..."
  },

  "signatures": {
    "in_toto": "s3://.../slsa/abc123.attestation.json"
  },

  "energy_carbon": {
    "kwh": 1.72,
    "co2e_kg": 0.81
  }
}
```

---

## 🗒️ 4. YAML Sidecar Schema (Human-Oriented)

Example: `meta/abc123.yaml`

```yaml
lakefs_repo: kfm-main
lakefs_branch: prod
lakefs_commit: abc123

rollback_bundle: s3://kfm-registry/rollback/artifacts/abc123.tar.zst

includes:
  - frozen STAC collections/items
  - model binaries
  - pipeline configs (SHA-validated)
  - evaluation metrics
  - OpenLineage run context
  - OTel trace tree

governance:
  provenance: PROV-O linked
  signature: slsa v1.0 attestation
  retention: 365d

restore_cmd: >
  kfm rollback --commit abc123 \
    --bundle s3://kfm-registry/rollback/artifacts/abc123.tar.zst
```

---

## 🛠️ 5. How Rollback Bundles Are Produced

### 🔔 Triggers
- Airflow promotion DAG  
- lakeFS branch lifecycle event  
- CrewAI / LangGraph auto-update worker  
- Manual LTS checkpoint  
- CI/CD compliance event  

### 🔄 Process
1. Freeze lakeFS commit  
2. Snapshot STAC collections/items  
3. Export configs (SHA-pinned)  
4. Add model binaries  
5. Export OpenLineage run  
6. Export OTel trace  
7. Compute energy/carbon  
8. Package → OCI/TAR.ZST  
9. Generate signature + SLSA  
10. Append index row  
11. Emit governance event  

Rollback bundles are **immutable** upon creation.

---

## 🧬 6. Restore / Rollback Workflow

Rollback is **deterministic**, **idempotent**, and **cryptographically verifiable**.

```
kfm rollback --commit <sha> \
  --bundle s3://kfm-registry/rollback/artifacts/<sha>.tar.zst
```

Restores:

- lakeFS refs  
- STAC hierarchy  
- configs (exact versions)  
- model binaries  
- provenance evidence  
- OpenLineage + OTel context  

---

## 🔒 7. Reliability Guarantees (v11)

- **Immutable audit log** (append-only)  
- **No mutation** of index rows  
- **One rollback per lakeFS commit**  
- **Cryptographic chain-of-custody** (SHA256 → signature → SLSA attestation)  
- **Guaranteed replayability** of all pipelines  
- **Hotfix-safe**: Instant fallback for any subsystem  

---

## 📚 8. Story Node & Focus Mode Integration

Rollback events are represented as governed system Story Nodes (internal domain).  
Focus Mode can show:

- Why rollback occurred  
- Dependencies affected  
- Graph of upstream/downstream pipelines  
- “Before/After” data & model state reconstruction  

---

## 🕰️ 9. Version History

| Version | Date       | Summary                                                        |
|--------:|------------|----------------------------------------------------------------|
| v11.2.2 | 2025-11-30 | Upgraded to MDP v11.2.2; energy/carbon v2; OCI artifacts added. |
| v11.1   | 2025-03-20 | Initial governed LTS rollback definition.                       |
| v10.x   | 2024-2025 | Prototype non-cryptographic rollback mapping.                    |

---

<div align="center">

©
