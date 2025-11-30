---
title: "♻️ KFM v11.2.2 — Rollback Metadata Manifests (Human-Oriented lakeFS Commit Records)"
path: "docs/pipelines/reliability/rollback-registry/meta/README.md"
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

doc_uuid: "urn:kfm:pipelines:rollbackregistry:meta:v11.2.2"
semantic_document_id: "kfm-rollback-registry-meta"
event_source_id: "ledger:pipelines/rollback-registry/meta"
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

doc_kind: "Metadata Specification"
intent: "kfm-rollback-meta-manifests"
classification: "Internal · Safety-Critical"
fair_category: "F1-A1-I3-R4"
care_label: "Respectful · Minimization"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "60 months"
sunset_policy: "Superseded by v12 rollback metadata redesign"
---

<div align="center">

# ♻️ **Rollback Metadata Manifests (KFM v11.2.2)**  
### *Human-Oriented lakeFS Commit Records · Provenance · Governance Metadata*  

`docs/pipelines/reliability/rollback-registry/meta/README.md`

**Purpose**  
Describe the **human-readable metadata manifests** stored beside rollback bundles,  
capturing high-level provenance, governance, environment, model sets, STAC snapshots,  
and restore instructions in a concise YAML format.

</div>

---

## 🗂️ Directory Layout

~~~text
docs/pipelines/reliability/rollback-registry/meta/
├── 📄 README.md                      # This file
└── 📄 <lakefs_commit>.yaml           # Human-readable rollback manifest
~~~

Each filename must match the lakeFS commit exactly:

**`<lakefs_commit>.yaml`**

Manifests are **append-only**, immutable once committed.

---

## 📘 Overview

The metadata manifest is the **human-facing, governance-friendly** companion  
to the binary artifact bundle and index ledger entry.

It summarizes:

- lakeFS commit metadata  
- frozen STAC refs  
- model versions  
- configs (SHA-validated)  
- provenance lineage  
- telemetry attachments  
- SLSA attestation paths  
- restore instructions  
- retention + governance rules

The manifest does **not** replace the full rollback bundle or index entry —  
it provides a **readable executive summary** of the rollback state.

---

## 🧾 Manifest Structure (Authoritative YAML Schema)

Below is the canonical structure each `<lakefs_commit>.yaml` must follow:

```yaml
lakefs_repo: kfm-main
lakefs_branch: prod
lakefs_commit: <sha>

rollback_bundle: s3://kfm-registry/rollback/artifacts/<sha>.tar.zst

created_at: "2025-11-30T12:00:00Z"
producer: "airflow:dag=kfm-promote"

data_snapshot:
  - stac: "s3://.../collection.json"
    lakefs_ref: "lakefs://kfm@<sha>/path"

models:
  - name: focus-transformer
    version: "3.1.0"
    uri: "s3://models/focus-transformer/3.1.0.bin"

configs:
  - path: "configs/pipeline.yaml"
    sha256: "<sha256>"

lineage:
  openlineage_run_id: "<uuid>"
  otel_trace_id: "<trace-id>"

signatures:
  in_toto: "s3://.../slsa/<sha>.attestation.json"

energy_carbon:
  kwh: <float>
  co2e_kg: <float>

governance:
  provenance: "PROV-O linked"
  retention: 365d
  signature: "SLSA v1.0"
  immutability: true

restore_cmd: >
  kfm rollback --commit <sha> \
    --bundle s3://kfm-registry/rollback/artifacts/<sha>.tar.zst
```

Manifests must pass YAML schema validation in CI.

---

## 🔐 Governance Rules

Human-readable manifests must:

- match **exact** commit SHA  
- be **immutable** once published  
- reference the correct bundle + index entry  
- contain complete provenance  
- reference energy/carbon telemetry  
- contain SLSA & cryptographic chain-of-custody info  
- reflect retention and LTS governance policies  

Missing fields block CI.

---

## 🧪 CI/CD Validation

Checks applied to each manifest:

- YAML schema validation  
- lakeFS commit format check  
- STAC + lakeFS ref existence check  
- SLSA attestation presence  
- provenance completeness  
- energy/carbon schema check  
- config SHA verification  
- model URI and version verification  

Manifests failing validation **cannot** be added to the index.

---

## 🔎 Use in Rollback Workflows

Rollback manifests power:

- SRE debugging  
- Story Node reconstruction  
- Focus Mode audit trails  
- visualization dashboards  
- lakeFS → data → pipeline lineage navigation  
- “What changed?” inquiries during incidents  
- compliance & reliability audits  

---

## 🕰️ Version History

| Version | Date       | Summary                                                             |
|--------:|------------|---------------------------------------------------------------------|
| v11.2.2 | 2025-11-30 | Initial governed rollback metadata manifest spec added.             |
| v11.2.1 | 2025-11-29 | Added retention + governance structure and restore_cmd scaffold.     |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
[📚 Docs Home](../../../../README.md) · [📏 Standards Index](../../../standards/README.md) · [🛡 Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

