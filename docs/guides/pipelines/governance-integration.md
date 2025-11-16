---
title: "⚖️ Kansas Frontier Matrix — Pipeline Governance Integration Guide (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/guides/pipelines/governance-integration.md"
version: "v10.4.2"
last_updated: "2025-11-16"
review_cycle: "Quarterly · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.2/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.2/manifest.zip"
telemetry_ref: "../../../releases/v10.4.2/pipeline-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/pipelines-governance-integration-v2.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.2"
status: "Active / Enforced"
doc_kind: "Guide"
intent: "governance-integration"
fair_category: "F1-A1-I1-R1"
care_label: "C2-A2-R2-E1"
kfm_readme_template: "Platinum v7.1"
ci_enforced: true
---

<div align="center">

# ⚖️ **Kansas Frontier Matrix — Pipeline Governance Integration Guide**  
`docs/guides/pipelines/governance-integration.md`

**Purpose**  
Define how every KFM pipeline integrates **FAIR+CARE v2 governance**, including:  

- CARE-sensitive AOI masking and sovereignty enforcement  
- Ethical AI controls and agent safety  
- Lineage & provenance (PROV-O, CIDOC CRM, GeoSPARQL)  
- Governance ledger integration (append-only)  
- SBOM + SLSA provenance  
- Telemetry v2 (energy · CO₂ · masking · violations)  
- CI gate enforcement  

ensuring full compliance with **Diamond⁹ Ω / Crown∞Ω**, **MCP-DL v6.3**, and the  
**Kansas Frontier Matrix Governance Charter**.

</div>

---

# 📘 Overview

Every KFM pipeline — remote sensing, historical, hydrology, hazards, AI, STAC ingestion —  
must integrate governance at **four core layers**:

1. **Governance metadata injection**  
2. **CARE v2 label & masking enforcement**  
3. **Lineage & provenance emission**  
4. **Governance ledger registration + telemetry v2**

No pipeline may **publish** data, generate STAC/DCAT, enrich Neo4j, or export RDF  
unless **all four layers** have been satisfied.

This guide standardizes governance integration across:

- **Ingestion**  
- **Preprocessing**  
- **Analytics / AI**  
- **Validate → Promote**  
- **Publishing**  

---

# 🗂️ Governance Integration Flow (Mermaid · GitHub-Safe)

```mermaid
flowchart TD

A["Pipeline Stage<br/>ingest · preprocess · analytics · publish"] --> B["Governance Hooks<br/>CARE · sovereignty · ethics"]
B --> C["Provenance Builder<br/>PROV-O · GeoSPARQL · CIDOC CRM"]
C --> D["Governance Ledger Writer<br/>append-only entries"]
D --> E["Telemetry v2 Integrator<br/>energy · CO₂ · care flags"]
````

---

# 🧱 1. Governance Metadata Requirements

Every dataset, batch, scene, or derived product MUST include a **Governance Header Block**
in its manifest (e.g. `processed_manifest.json` / `staging_manifest.json`):

| Field                  | Description                                                                                 |
| ---------------------- | ------------------------------------------------------------------------------------------- |
| `kfm:careLabel`        | CARE v2 label: `public`, `sensitive`, or `restricted` (no defaults; must be explicit)       |
| `kfm:sovereigntyFlags` | Array of flags where AOI intersects sovereignty overlays (e.g. `tribal_overlap`)            |
| `kfm:maskingStrategy`  | Strategy applied to sensitive locations (e.g. `h3_r7`, `centroid_only`, `remove_geometry`)  |
| `kfm:sourceEndpoint`   | Primary source descriptor (STAC/catalog/API/dataset ID)                                     |
| `kfm:lineageRef`       | Path/URI to Lineage v2 JSON-LD bundle                                                       |
| `kfm:telemetryRef`     | Path/URI to Telemetry v2 NDJSON                                                             |
| `kfm:checksum_sha256`  | SHA-256 checksum for main artifact                                                          |
| `kfm:processingSteps`  | Ordered list of standardized pipeline steps (`ingest`, `preprocess`, `validate`, `publish`) |
| `kfm:sbomRef`          | SPDX SBOM reference covering tools used                                                     |
| `kfm:attestationRef`   | SLSA-style attestation reference (where applicable)                                         |

Governance metadata MUST be:

* **stable** (no silent mutation)
* **machine-readable**
* **linked** into lineage & ledger

---

# 🛡️ 2. CARE v2 Enforcement

All pipelines MUST enforce **CARE v2**:

## 2.1 Labels

* `public` — no special masking required beyond privacy guidance
* `sensitive` — masking required for localized AOIs (H3 generalization, precision reduction)
* `restricted` — aggressive generalization or removal of geometry/attributes

## 2.2 Sensitive AOIs

Sensitive AOIs include:

* Indigenous lands & treaty boundaries
* Tribal sovereignty areas
* Archaeological and cultural sites
* Burial sites
* Critical infrastructure locations (if flagged)
* Protected ecological zones
* Hazard impact regions requiring privacy

AOI overlays are stored under (example):

```text
data/processed/aoi/sovereignty_overlays/
```

Pipelines MUST detect intersection with these overlays.

## 2.3 Masking Strategies

Examples (not exhaustive):

```text
h3_r7                   # H3 generalization (coarser hex grid)
h3_r5                   # even coarser H3 masking
bbox_expand_5km         # envelope + padding
precision_reduce_4dp    # coordinate rounding
mask_polygon            # polygons replaced by generalized bounding shapes
remove_geometry         # geometry removed entirely
centroid_only           # replace geometry with single centroid point
```

Masking MUST be:

* **documented** in `kfm:maskingStrategy`
* **consistent** with CARE label
* **validated** via governance CI (`faircare-validate.yml`)

---

# 🧭 3. Sovereignty & Cultural Protections

All pipelines that touch spatial data MUST:

1. Intersect AOIs with sovereignty overlays.
2. Set `kfm:sovereigntyFlags[]` accordingly.
3. Choose masking strategy consistent with CARE label and sovereignty flags.
4. Ensure no publication (STAC/DCAT/Neo4j/RDF) occurs until conflicts are resolved.

Telemetry MUST track:

* `care_violations`
* `sovereigntyConflicts`
* `maskingApplied` (boolean)

Sovereignty rules are defined in the Governance Charter and referenced from:

```text
docs/standards/governance/ROOT-GOVERNANCE.md
```

---

# 🧬 4. Lineage & Provenance Integration (Lineage v2)

Lineage v2 is required for all promoted datasets and must be:

* **JSON-LD**
* **PROV-O** compliant
* **GeoSPARQL-aware**
* **CIDOC CRM**-aware (for events/history)
* **CARE v2** integrated
* **Telemetry-linked**

Stored at:

```text
data/processed/lineage/<dataset>/<version>.jsonld
```

Validated against:

```text
src/pipelines/remote-sensing/lineage/schemas/lineage.schema.json
```

and additional shapes for non-remote-sensing pipelines as applicable.

Lineage MUST record:

* Entities (input + output)
* Activities (ingest, preprocess, validate, publish)
* Agents (pipelines, providers, human reviewers)
* Spatial relationships
* CARE decisions
* Telemetry summary

---

# 📒 5. Governance Ledger Integration

The Governance Ledger is an **append-only audit log**.

Path:

```text
docs/reports/audit/data_provenance_ledger.jsonl
```

Each entry MUST include:

* `dataset_id`
* `version`
* `careLabel` & `maskingStrategy`
* `sovereigntyFlags[]`
* `lineageRef`
* `telemetryRef`
* `stacRef` / `dcatRef` / `rdfRef` / `graphRef` (as relevant)
* `sbomRef`
* `attestationRef`
* `promotionWorkflowRunId`
* `publishingWorkflowRunId` (if used)
* `reviewers[]` (CODEOWNERS or governance reviewers)

All writes MUST be:

* Append-only (no mutation)
* Versioned
* Validated by CI (structure + governance rules)

---

# 🧱 6. SBOM + SLSA Integration

Every pipeline that changes dataset structure or semantics MUST:

* Generate or update an SPDX SBOM:

```text
releases/v10.4.2/sbom.spdx.json
```

* Produce SLSA-style provenance / attestation (e.g. `attestation.json`), packaged into:

```text
releases/v10.4.2/manifest.zip
```

CI workflows:

* `sbom-validate.yml` — ensures packages/tools match SBOM.
* `slsa-verify.yml` — verifies provenance and attestations.

Governance ledger entries MUST link these artifacts via `sbomRef` and `attestationRef`.

---

# 📡 7. Telemetry v2 Integration

Pipelines MUST write Telemetry v2 NDJSON per stage:

```text
data/telemetry/<pipeline>.ndjson
```

Minimal fields:

* `pipeline`
* `stage` (`ingest|preprocess|validate|promote|publish`)
* `run_id`
* `dataset_id` / `collection_id`
* `status` (`success|failure|noop`)
* `duration_ms`
* `rows_processed` / `pixels_processed`
* `energy_wh`
* `co2_g`
* `care_violations`
* `sovereigntyConflicts`
* `maskingApplied`
* `error_codes[]`

Aggregated to:

```text
releases/v10.4.2/pipeline-telemetry.json
```

Validation via:

* `telemetry-export.yml`

Telemetry is referenced from lineage and governance ledger to support Focus Mode, dashboards, and audits.

---

# 🧪 8. CI Enforcement

Governance is enforced via a set of CI workflows:

| Workflow                   | Responsibility                            |
| -------------------------- | ----------------------------------------- |
| `faircare-validate.yml`    | CARE v2 and sovereignty rules             |
| `stac-validate.yml`        | STAC 1.0 structural & semantic validation |
| `dcat-validate.yml`        | DCAT 3.0 Dataset JSON-LD validation       |
| `linked-data-validate.yml` | RDF/GeoSPARQL validation                  |
| `lineage-validate.yml`     | Lineage v2 JSON-LD shapes & schema        |
| `telemetry-export.yml`     | Telemetry v2 presence & schema            |
| `sbom-validate.yml`        | SBOM presence and alignment               |
| `slsa-verify.yml`          | Attestation verification                  |
| `docs-lint.yml`            | KFM-MDP v10.4.2 compliance                |
| `codeql.yml` / `trivy.yml` | Security and CVE scanning                 |

**Any failure** in these governance workflows → **merge blocked**.

---

# 🧭 9. Developer Checklist (Governance Integration)

Before merging or publishing a new/updated pipeline, ensure:

* [ ] `kfm:careLabel` is explicitly set (no default/implicit).
* [ ] `kfm:maskingStrategy` selected and justified.
* [ ] Sovereignty overlays checked; `sovereigntyFlags[]` set if needed.
* [ ] Lineage v2 bundle generated and passes validation.
* [ ] Telemetry v2 emitted and linked into lineage.
* [ ] Governance ledger entry appended with correct refs.
* [ ] SBOM and SLSA attestation updated & validated.
* [ ] All governance CI workflows green in the MR/PR.

---

# 🕰 Version History

| Version | Date       | Summary                                                                                              |
| ------: | ---------- | ---------------------------------------------------------------------------------------------------- |
| v10.4.2 | 2025-11-16 | Full KFM v10.4.2 upgrade: CARE v2, Telemetry v2, Lineage v2, SBOM & SLSA integration, CI enforcement |
| v10.3.1 | 2025-11-14 | Initial governance-integration guide; CARE v1 + lineage v1 + telemetry v1                            |

---

<div align="center">

**Kansas Frontier Matrix — Pipeline Governance Integration (v10.4.2)**
Ethical Pipelines × CARE v2 × Sovereignty Protection × Immutable Provenance
© 2025 Kansas Frontier Matrix — CC-BY 4.0 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>
