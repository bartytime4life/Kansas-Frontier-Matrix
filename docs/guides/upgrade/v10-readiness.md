---
title: "🚀 Kansas Frontier Matrix — v10 Readiness & Upgrade Guide (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/guides/upgrade/v10-readiness.md"
version: "v10.4.2"
last_updated: "2025-11-16"
review_cycle: "Pre-Release / Continuous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.2/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.2/manifest.zip"
data_contract_ref: "../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../releases/v10.4.2/pipeline-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/upgrade-v10-readiness-v2.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT / CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.2"
status: "Active / Enforced"
doc_kind: "Upgrade Guide"
intent: "v9.7-to-v10-readiness"
fair_category: "F1-A1-I1-R1"
care_label: "C2-A2-R2-E1"
machine_extractable: true
ai_focusmode_usage: "Allowed with restrictions"
ttl_policy: "Review each release"
sunset_policy: "Superseded by v11 readiness guide"
doc_uuid: "urn:kfm:doc:v10-readiness-10.4.2"
semantic_document_id: "kfm-doc-upgrade-readiness"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
---

<div align="center">

# 🚀 **Kansas Frontier Matrix — v10 Readiness & Upgrade Guide**  
`docs/guides/upgrade/v10-readiness.md`

**Purpose**  
Provide the comprehensive readiness checklist, system deltas, and migration roadmap required to upgrade any Kansas Frontier Matrix (KFM) environment from **v9.7.x → v10.x**.  
This guide ensures alignment with:

- **Streaming ETL v10 (Kafka/Webhooks)**  
- **Predictive Pipelines v10**  
- **Focus Mode v2.5 (Explainability + CARE gates)**  
- **Telemetry v2 (energy · carbon · A11y · CARE)**  
- **Lineage v2 (PROV-O · CIDOC · GeoSPARQL)**  
- **FAIR+CARE v2 governance**  
- **KFM-MDP v10.4.2 documentation system**  
- **MCP-DL v6.3 (Master Coder Protocol)**  

</div>

---

# 📘 Overview

KFM v10 introduces:

- **Deterministic streaming ETL** and idempotent watchers  
- **Predictive pipelines** generating future STAC Items  
- **Focus Mode v2.5** with explainability overlays & CARE masking  
- **Reorganized monorepo** with strict directory patterns  
- **Telemetry v2** for pipelines, web UI, ETL, and energy audits  
- **Live STAC↔DCAT sync** (bidirectional catalog parity)  
- **Governance Ledger automation** with SHA-256 signatures  

This guide ensures you validate and prepare your v9.7.x environment for a safe upgrade without breaking lineage, provenance, or CARE datasets.

---

# 🗂️ Directory Layout (v10 Reference — Upgraded Lined Style)

~~~text
KansasFrontierMatrix/
├── src/
│   ├── ai/                               # Focus Transformer v2 · embeddings · explainability
│   ├── api/                              # FastAPI · GraphQL hybrid service layer
│   ├── graph/                            # Neo4j schema · CIDOC CRM · GeoSPARQL · OWL-Time
│   ├── pipelines/                        # Deterministic ETL + streaming + predictive
│   │   ├── ingestion/                    # Watchers · conditional GET · idempotency keys
│   │   ├── validation/                   # GX + schema + CARE v2 validation
│   │   ├── reliable_auto_release/        # ETag-based publish pipelines (v10 standard)
│   │   ├── remote_sensing/               # SVF · LRM · harmonization · RTC · bandstack
│   │   ├── analytics/                    # Hazards · trends · indices · predictive models
│   │   ├── governance/                   # CARE v2 · sovereignty · masking · ledger entries
│   │   └── lineage/                      # Lineage v2 JSON-LD builder
│   ├── telemetry/                        # Telemetry v2 (energy · CO₂ · runtime · A11y)
│   └── web/                              # React + MapLibre v10 UI (Focus Mode v2.5)
│
├── data/
│   ├── sources/                           # Data Contract v3 sources (streaming + batch)
│   ├── raw/                               # Raw datasets (LFS-tracked)
│   ├── work/                              # Staging · temp · ledger · checkpoints
│   ├── processed/                         # Validated, CARE-tagged assets
│   ├── stac/                              # STAC Items/Collections + DCAT mirror
│   └── lineage/                           # Lineage v2 bundles (PROV-O · GeoSPARQL)
│
├── docs/
│   ├── guides/                            # All KFM guides (visualization · workflows · pipelines)
│   │   ├── upgrade/                       # v10 readiness, inventory, consolidation reports
│   │   ├── workflows/                     # CI · FAIR+CARE · telemetry · governance
│   │   ├── visualization/                 # MapLibre · Timeline · Explainability · Accessibility
│   │   └── pipelines/                     # Ingestion · analytics · publishing · validation
│   ├── standards/                         # FAIR+CARE v2 · governance · markdown protocol
│   └── contracts/                         # Data Contract v3 · API schemas
│
├── tools/                                 # CLI utilities (STAC↔DCAT sync · validate · ingest)
├── tests/                                 # Unit · integration · telemetry · lineage tests
├── docker-compose.yml                      # Full v10 stack (Kafka · Neo4j 5.x · API · web)
├── Makefile                                # Standardized entrypoint for CI + dev tasks
├── CONTRIBUTING.md
└── LICENSE
~~~

---

# 🧩 Core Upgrades from v9.7.x → v10.x

| Domain | v9.7.x | v10.x Enhancement |
|--------|--------|-------------------|
| **Architecture** | Static ETL | Streaming ETL + idempotent WAL |
| **Predictive Modeling** | None | Predictive pipelines (hazards, climate) |
| **Focus Mode** | Narrative v1 | Focus Mode v2.5 + explainability + CARE gates |
| **Catalog Sync** | STAC only | Live STAC↔DCAT v3 mirror |
| **Governance** | Manual FAIR checks | Automated FAIR+CARE v2 + sovereignty masking |
| **Lineage** | v1 basic | Lineage v2 (CIDOC · PROV-O · GeoSPARQL) |
| **Telemetry** | Basic metrics | Telemetry v2 (energy · CO₂ · A11y · CARE violations) |
| **Docs** | Inconsistent | MCP-DL v6.3 + KFM-MDP v10.4.2 |
| **Web** | 2D map UI | MapLibre v10 UI + 3D overlays + Focus Mode integration |

---

# ⚙️ Pre-Upgrade Readiness Checklist

## **1. Baseline Validation**
- [ ] All STAC Items validate against v10 schemas  
- [ ] All DCAT datasets validate using JSON-LD SHACL  
- [ ] Run lineage validation (`make lineage-validate`)  
- [ ] Run FAIR+CARE validation (`make faircare-validate`)

## **2. Neo4j Readiness**
- [ ] Export pre-upgrade graph snapshot  
- [ ] Ensure APOC 5.x is available  
- [ ] Check orphan nodes:  
```

MATCH (n) WHERE NOT (n)--() RETURN count(n)

````

## **3. Data Contract v3 Migration**
- [ ] All source manifests updated  
- [ ] Streaming schemas added (`"streaming": {...}`)  
- [ ] CARE v2 fields added

## **4. Web v10 UI Requirements**
- [ ] React 18 + TypeScript strict mode  
- [ ] MapLibre style placeholders replaced with tokenized theming  
- [ ] Focus Mode v2.5 tested

## **5. Governance & Telemetry**
- [ ] Governance ledger validation passes  
- [ ] Telemetry schema upgraded to Telemetry v2  
- [ ] All pipelines emit non-PII telemetry

---

# 🔄 Upgrade Steps (v9.7 → v10)

## 1. Switch to v10 Branch
```bash
git fetch origin
git checkout v10.0.0
````

## 2. Rebuild Full Stack

```bash
docker compose down
docker compose build --no-cache
docker compose up -d
```

## 3. Apply v10 Graph Migration

```bash
make migrate-graph
```

## 4. Refresh Catalog Mirrors

```bash
make stac-rebuild
make dcat-validate
```

## 5. Reinitialize Streaming ETL

```bash
python src/pipelines/ingestion/watchers/ks_weather_watcher.py
```

## 6. Validate Predictive Pipelines

```bash
pytest tests/pipelines/predictive -v
```

## 7. Full Validation Sweep

```bash
make validate-all
```

---

# 🧠 Developer Notes (v10.x)

* Predictive pipelines **must** emit future-dated STAC Items
* Streaming ETL requires **idempotency keys** and **conditional GET**
* Focus Mode v2.5 integrates:

  * Evidence chips
  * Sovereignty masking
  * Subgraph explainability
* All visual layers must use **design tokens**
* Governance ledger entries require SHA-256 checksums for:

  * lineage bundles
  * telemetry bundles
  * STAC Items
  * predictive outputs

---

# ✅ Post-Upgrade Verification

| Check      | Command                     | Expected     |
| ---------- | --------------------------- | ------------ |
| API health | `curl :8000/health`         | `status: ok` |
| Graph      | `MATCH (n) RETURN count(n)` | > 0          |
| STAC       | `make stac-validate`        | Pass         |
| Focus v2   | `pytest tests/ai/focus`     | Pass         |
| FAIR+CARE  | `make faircare-audit`       | 0 violations |
| Lineage    | `make lineage-validate`     | v2 compliant |
| Telemetry  | `make telemetry-validate`   | v2 compliant |

---

# 🕰 Version History

| Version | Date       | Summary                                                                 |
| ------: | ---------- | ----------------------------------------------------------------------- |
| v10.4.2 | 2025-11-16 | Upgraded to Telemetry v2, CARE v2, Lineage v2, directory layout v10.4.2 |
| v10.0.0 | 2025-11-08 | Initial v10 readiness guide                                             |
|  v9.7.x | 2025-05-01 | Pre-upgrade baseline                                                    |

---

<div align="center">

© 2025 Kansas Frontier Matrix
Master Coder Protocol v6.3 · FAIR+CARE v2 Certified
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

[Back to Upgrade Guides](../README.md) · [Governance Charter](../../standards/governance/ROOT-GOVERNANCE.md)

</div>
```
