---
title: "♻️ KFM v11.2.2 — Rollback Registry Index (Append-Only Ledger · JSONL · Parquet)"
path: "docs/pipelines/reliability/rollback-registry/index/README.md"
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

doc_uuid: "urn:kfm:pipelines:rollbackregistry:index:v11.2.2"
semantic_document_id: "kfm-rollback-registry-index"
event_source_id: "ledger:pipelines/rollback-registry/index"
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
intent: "kfm-rollback-registry-index"
classification: "Internal · Safety-Critical"
fair_category: "F1-A1-I3-R4"
care_label: "Respectful · Minimization"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "60 months"
sunset_policy: "Superseded by v12 ledger/index redesign"
---

<div align="center">

# ♻️ **Rollback Registry Index (KFM v11.2.2)**  
### *Append-Only Ledger · JSONL + Parquet · Cryptographically Linked Records*  

`docs/pipelines/reliability/rollback-registry/index/README.md`

**Purpose**  
Define the authoritative, append-only, version-pinned ledger used to record  
**every rollback artifact**, **every lakeFS commit**, **every provenance chain**,  
and **every SLSA-verified build** inside the Kansas Frontier Matrix.

</div>

---

## 🗂️ Directory Layout

~~~text
docs/pipelines/reliability/rollback-registry/index/
├── 📄 README.md                           # This file
├── 📄 rollback-index.jsonl                # Append-only canonical ledger
└── 📄 rollback-index.parquet              # Analytics-friendly mirror
~~~

The JSONL file is authoritative.  
The Parquet file is generated via CI and must not be manually edited.

---

## 📘 Overview

The Rollback Registry Index is the **core of KFM’s reliability system**.  
It provides:

- Immutable, append-only recording of **every rollback bundle**  
- Cross-checking of **models**, **configs**, **datasets**, and **STAC snapshots**  
- Verified lineage (OpenLineage + OTel + PROV-O)  
- Cryptographic chain-of-custody (SHA → sig → SLSA)  
- Deterministic rollback availability for **every pipeline commit**  

Every entry corresponds directly to an immutable bundle stored in:

`rollback-registry/artifacts/<lakefs_commit>.tar.zst`

---

## 📑 Index Schema (Authoritative)

Each JSONL row must follow:

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
      "stac": "s3://.../collection.json",
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

This schema must not be changed without Reliability Governance Board approval.

---

## 🔐 Index Invariants (v11.2.2)

The index obeys strict invariants:

- **Append-only**: No updates, no deletions  
- **One row per lakeFS commit**  
- **Immutable**: Any mutation triggers CI governance violation  
- **Cryptographically linked** to rollback artifacts  
- **Lineage-consistent** with OpenLineage & OTel traces  
- **Energy & carbon telemetry required**  
- **SLSA attestation required**  

---

## 🧪 CI/CD Validation

CI enforces the following rules on both JSONL and Parquet outputs:

- JSON schema validation  
- checksum and signature checks  
- STAC + lakeFS ref validation  
- SLSA attestation verification  
- energy/carbon schema checks  
- ordering guarantee (`created_at` monotonic)  
- append-only enforcement  
- Parquet regeneration correctness  

Any failure blocks merge into the registry.

---

## 🧱 Governance Rules

The index is governed jointly by:

- **Reliability Engineering Board**  
- **FAIR+CARE Council**  
- **Security & Supply-Chain Council**  

Changes require multi-signoff:

- schema evolution  
- SLSA policy updates  
- cryptographic method revisions  
- retention policy changes  
- reindexing or compaction workflows  

---

## 📡 Use in Reliability Systems

The index powers:

- `kfm rollback --commit <sha>`  
- Impact analysis (tree of dependent pipelines)  
- Story Node generation for rollback events  
- Focus Mode reconstruction (“Why was rollback triggered?”)  
- Diffs between environment states  
- LTS regression audits  
- Energy/carbon optimization studies  

---

## 🕰️ Version History

| Version | Date       | Summary                                                           |
|--------:|------------|-------------------------------------------------------------------|
| v11.2.2 | 2025-11-30 | Initial governed rollback index spec; parity with main registry.  |
| v11.2.1 | 2025-11-29 | Added Parquet mirror spec + append-only enforcement rules.        |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
[📚 Docs Home](../../../../README.md) · [📏 Standards Index](../../../standards/README.md) · [🛡 Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

