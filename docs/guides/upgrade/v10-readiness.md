---
title: "🚀 Kansas Frontier Matrix — v10 Readiness & Upgrade Guide"
path: "docs/guides/upgrade/v10-readiness.md"
version: "v10.0.0"
last_updated: "2025-11-08"
review_cycle: "Pre-Release / Continuous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.0.0/manifest.zip"
telemetry_ref: "../../../releases/v10.0.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/upgrade-v10-readiness.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
---

<div align="center">

# 🚀 **Kansas Frontier Matrix — v10 Readiness & Upgrade Guide**
`docs/guides/upgrade/v10-readiness.md`

**Purpose:** Provide a comprehensive readiness checklist, feature summary, and migration path for developers and maintainers upgrading the Kansas Frontier Matrix (KFM) from **v9.7.x → v10.0.0**.  
Ensures alignment with new containerized architecture, streaming ETL, predictive pipelines, FAIR+CARE governance, and MCP v6.3 standards.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../standards/markdown_rules.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Certified-orange)](../../standards/faircare.md)
[![Status: Stable](https://img.shields.io/badge/Status-Stable-brightgreen)]()

</div>

---

## 📘 Overview

KFM **v10.0** represents the platform’s evolution from a static, batch-based MVP into a **real-time, federated, AI-driven knowledge system**.  
It introduces predictive modeling, Focus Mode v2, live data ingestion, a reorganized monorepo, and stricter governance pipelines.  

This guide outlines the **required preparation, migration steps, and validation tasks** for environments currently running any **v9.7.x** branch.

---

## 🗂️ Directory Layout (v10 Reference)

```bash
KansasFrontierMatrix/
├── src/
│   ├── ai/                 # AI/ML models & explainability
│   ├── api/                # FastAPI / GraphQL services
│   ├── graph/              # Neo4j schema, Cypher utilities
│   ├── pipelines/
│   │   ├── etl/            # Batch ETL
│   │   ├── etl/streaming/  # Kafka-based live ingestion
│   │   └── predictive/     # ML-driven forecast generation
│   ├── telemetry/          # Metrics & governance logs
│   └── web/                # React + MapLibre frontend
├── data/
│   ├── sources/            # v3 data contracts (with streaming fields)
│   ├── processed/
│   └── stac/               # Live STAC/DCAT bridge catalog
├── docs/
│   ├── guides/upgrade/
│   └── standards/
├── tests/
├── docker-compose.yml
└── Makefile
```

---

## 🧩 Core Upgrades from v9.7.x

| Area | v9.7.x | v10.0 Enhancement |
|------|---------|-------------------|
| **Architecture** | Static containers, single-node graph | Multi-service Docker Compose stack with HA Neo4j cluster & Kafka streaming |
| **ETL Pipelines** | Batch-only ingestion | Dual-mode ETL: batch + streaming (Kafka topics, WebSocket feeds) |
| **Predictive Modeling** | None | ML-based predictive ETL producing simulated datasets (e.g., 2030–2100) |
| **Focus Mode** | v1 (LLM summaries) | v2 “Focus Transformer” with dual-encoder AI, explainability graphs |
| **API** | REST endpoints only | REST + GraphQL hybrid, JWT/OAuth2 support |
| **Data Standards** | STAC 1.0, partial DCAT 2.0 | Full STAC↔DCAT 3.0 bridge, auto-publishing STAC Items |
| **Governance** | FAIR+CARE (manual audit) | FAIR+CARE automated ledger validation + telemetry schema |
| **Docs & CI** | Semi-manual validation | Full docs-lint, FAIR audit, SBOM/manifest enforcement in CI |
| **Frontend** | 2D map/timeline | 3D time-aware map layers + adaptive Focus Mode panels |

---

## ⚙️ Pre-Upgrade Checklist

Before migration, verify the following in the **v9.7.x** environment:

1. **Data Integrity**
   - [ ] Run `make data-validate` to ensure all STAC Items and DCAT contracts pass schema checks.  
   - [ ] Verify no orphan nodes exist in the Neo4j graph (`MATCH (n) WHERE NOT (n)--() RETURN count(n)` → expect 0).

2. **Container Baseline**
   - [ ] Back up Neo4j volumes (`neo4j-admin dump`).
   - [ ] Export `.env` configuration for reuse (API keys, ports, etc.).
   - [ ] Remove deprecated environment variables: `KFM_LEGACY_PATHS`, `AI_MODEL_V1`.

3. **Documentation Synchronization**
   - [ ] Update local documentation to the new Markdown compliance rules (`make docs-lint`).
   - [ ] Confirm each module’s README includes YAML front-matter and version tags.

4. **Governance & FAIR+CARE**
   - [ ] Ensure `docs/standards/faircare.md` and `data/contracts/*.json` reflect current ethics & license.
   - [ ] Run governance ledger verification: `make governance-validate`.

5. **Dependencies**
   - [ ] Python ≥ 3.12, Node ≥ 20.x, Docker ≥ 26.x, Compose v2.  
   - [ ] Neo4j 5.x and Kafka 3.x installed or containerized.  
   - [ ] Rebuild virtual environments: `make install-deps`.

---

## 🔄 Upgrade Steps

1. **Pull Latest Monorepo**
   ```bash
   git fetch origin main
   git checkout v10.0.0
   ```

2. **Rebuild Containers**
   ```bash
   docker compose down
   docker compose build --no-cache
   docker compose up -d
   ```

3. **Run Database Migration**
   ```bash
   make migrate-graph
   ```
   This applies new schema updates (`Dataset`, `SensorStream`, `FEDERATED_WITH` relationships).

4. **Reinitialize STAC/DCAT Bridge**
   ```bash
   make data-stac-rebuild
   make data-dcat-validate
   ```

5. **Test Streaming ETL**
   ```bash
   python src/pipelines/etl/streaming/consume.py --topic weather.ks
   ```
   Confirm live ingestion events appear in Neo4j.

6. **Validate Focus Mode v2**
   ```bash
   pytest tests/ai/focus_v2_test.py -v
   ```

7. **Run Full CI Verification**
   ```bash
   make validate-all
   ```

---

## 🧠 Developer Notes

- **Predictive ETL Integration:**  
  Models trained under `src/ai/predictive/` now produce STAC Items with `datetime` in the future.  
  Ensure outputs include `"temporal": {"start": "2030-01-01"}` fields for validation.

- **Streaming Pipelines:**  
  Kafka configuration located in `config/kafka.yml`. Each feed defines a topic, schema, and retention.  
  To add new feeds, append entries in `data/sources/*.json` with `"streaming": {"topic": "..."}`.

- **Graph Schema Extensions:**  
  Neo4j constraints and indexes auto-applied via `src/graph/schema/migrate_v10.cypher`.  
  Review these if adding new entity classes.

- **Focus Mode AI Model:**  
  Focus Transformer v2 uses cross-modal attention for summaries and explanations.  
  Model weights are in `src/ai/models/focus_transformer_v2/weights/`.

- **Security Enhancements:**  
  OAuth2 + JWT roles introduced. Configure `.env` roles:  
  ```
  ADMIN_ROLES=admin,maintainer
  READONLY_ROLES=viewer,guest
  ```

---

## ✅ Post-Upgrade Validation

| Task | Command | Expected Result |
|------|----------|----------------|
| API health check | `curl http://localhost:8000/health` | `{status:"ok", version:"10.0.0"}` |
| Graph count | `MATCH (n) RETURN count(n)` | Non-zero; same order as v9.7 backup |
| STAC validation | `make stac-validate` | All items valid (exit 0) |
| Focus Mode summary test | `pytest tests/ai/focus_v2_test.py` | Passes 100% |
| FAIR+CARE audit | `make faircare-audit` | 0 violations |
| Docs lint | `make docs-lint` | All compliant |

---

## 🧾 Version History

| Version | Date | Author | Summary |
|----------|------|---------|----------|
| v10.0.0 | 2025-11-08 | Core Dev Team | Initial release – containerized architecture, streaming ETL, Focus Mode v2 |
| v9.7.0 | 2025-05-01 | Core Dev Team | Stable MVP with AI Focus Mode v1, FAIR+CARE audit workflows |
| v9.5.0 | 2025-02-12 | DevOps Council | Full STAC/DCAT 2.0 alignment, governance ledger introduced |

---

<div align="center">

© 2025 Kansas Frontier Matrix · Master Coder Protocol v6.3  
**FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified**  
[Back to Guides Index](../README.md) · [Governance Charter](../../standards/governance/ROOT-GOVERNANCE.md)

</div>
