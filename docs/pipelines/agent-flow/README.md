---
title: "🚦 KFM-Agent Flow: Deterministic ETL → STAC/DCAT → Neo4j → Telemetry (with Guardrails)"
path: "docs/pipelines/agent-flow/README.md"
version: "v11.2.x"
last_updated: "2025-12-09"

release_stage: "Stable / Governed"
lifecycle: "LTS"
review_cycle: "Quarterly · Reliability & Metadata Councils"
content_stability: "stable"
license: "CC-BY 4.0"

doc_kind: "Pipeline Guide"
status: "Active / Governed"
header_profile: "standard"
footer_profile: "standard"

markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
mcp_version: "MCP-DL v6.3"

standards:
  - STAC 1.0.x
  - DCAT 3.0
  - PROV-O
  - GeoSPARQL / OWL-Time
  - KFM-MDP v11.2.x
  - KFM-PDC v11 (Pipeline/Data Contracts)

governance:
  fairness: "FAIR+CARE"
  sovereignty: "Indigenous data-sovereignty aligned"
  supply_chain: "SBOM + SLSA attestations"
  rollback_policy: "Automatic: repoint to previous DatasetVersion if post-publish checks degrade"

ci_attestations:
  sbom_ref: "releases/v11.2.x/sbom.spdx.json"
  slsa_attestation: "releases/v11.2.x/slsa-attestation.json"
  signature_ref: "releases/v11.2.x/signature.sig"
---

<div align="center">

# 🚦 **KFM-Agent Flow: Deterministic ETL → STAC/DCAT → Neo4j → Telemetry (with Guardrails)**  
`docs/pipelines/agent-flow/README.md`

**Purpose**  
Define the governed KFM agent pattern for **deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j → telemetry**,  
with CI guardrails, FAIR+CARE alignment, and automated rollback.

</div>

---

## 📘 Overview

This Agent ingests new data deterministically (seed‑locked), validates it, and publishes *only* when all gates pass:

1. **Trigger** on new‑data event  
2. **ETL** — deterministic, idempotent upserts  
3. **Great Expectations + schema diffs**  
4. **Pre‑publish canary** — staging bucket + staging graph  
5. **Publish STAC Items/Collections & DCAT Datasets**  
6. **Neo4j `DatasetVersion` nodes** + relationships  
7. **OpenTelemetry spans & dashboards** (including energy/carbon)  
8. **SLO / error‑budget gates + rollback** when post‑publish checks degrade  

Provenance for each run is modeled with **PROV‑O** (Entities, Activities, Agents) so downstream tools can trace every dataset back through ETL steps, agents, and source files. [oai_citation:0‡Comprehensive Guide to W3C PROV-O.pdf](file-service://file-M7Pfz7uE2cTVgom8q9d8B3)  

---

## 🗂️ Directory Layout

~~~text
📁 src/
│  └── 📁 pipelines/
│      └── 📁 soil/                     # deterministic ETL agent entrypoint
📁 great_expectations/                  # data tests & expectation suites
📁 schemas/
│  ├── 📁 stac/                         # STAC Collection/Item schemas for soil
│  ├── 📁 dcat/                         # DCAT dataset schemas for registry export
│  └── 📁 domain/                       # domain schemas (e.g., soil_profile_vN.json)
📁 neo4j/
│  └── 📁 cypher/                       # DatasetVersion + linkage Cypher scripts
📁 ops/
│  ├── 📁 gates/                        # SLO/error-budget, canary & post-publish checks
│  └── 📁 telemetry/                    # OpenTelemetry exporters (incl. energy/carbon)
📁 data/
│  ├── 📁 wal/                          # write-ahead logs for idempotent replay
│  ├── 📁 staging/                      # pre-publish canary outputs & temp artifacts
│  └── 📁 artifacts/                    # GX reports, schema diffs, energy/carbon JSON
📁 .github/
│  └── 📁 workflows/                    # CI/CD orchestrations (agent-soil, lineage, security)
📄 docs/pipelines/agent-flow/README.md  # this file (pipeline guide & contract)
~~~

This directory layout follows the emoji‑formatted tree and `~~~text` fencing profile defined in **KFM‑MDP v11.2.6**. [oai_citation:1‡kfm_markdown_protocol_v11.2.6.md.pdf](file-service://file-S1j2ngbeczrSfsWfRkKX9B)  

---

## 🧱 Architecture

### 🧩 Agent Prompt Contract (KFM‑PDC)

This is the **agent‑side contract**: deterministic behavior, idempotent upserts, and validated outputs. It is expressed as a KFM‑PDC fragment so CI can verify expectations.

~~~yaml
agent:
  name: kfm_etl_agent
  seed: 1337                    # deterministic runs
  idempotency_key: "${{ github.run_id }}"
  contracts:
    outputs:
      - stac_item               # STAC JSON must validate against schemaRef
      - dcat_dataset
      - prov_activity           # PROV-O notes (entities/activities/agents)
    behaviors:
      - "idempotent_upsert"     # safe to re-run with same inputs
      - "deterministic_etl"
    validations:
      - "great_expectations_pass"
      - "schema_diff: no-breaking-change"
  metadata:
    lineage_standard: "PROV-O"
    reproducibility:
      lockfiles: ["poetry.lock", "requirements.txt", "environment.yml"]
      data_hashes: true
~~~

### 🏗️ ETL Skeleton (deterministic + idempotent)

ETL is **pure and seed‑locked**; idempotency is enforced by a stable key derived from source identifiers.

~~~python
# src/pipelines/soil/ingest.py
from hashlib import sha256
import numpy as np

SEED = 1337
np.random.seed(SEED)

def idempotent_key(record) -> str:
    return sha256(
        f"{record['source_id']}|{record['date']}|{record['tile']}".encode()
    ).hexdigest()

def transform(raw):
    # pure, deterministic transforms
    return {
        **raw,
        "value_norm": (raw["value"] - raw["min"]) / (raw["max"] - raw["min"] + 1e-9),
    }

def upsert(store, doc):
    # upsert by stable key, no dupes
    key = idempotent_key(doc)
    store.upsert(key, doc)
~~~

### 🕸️ Neo4j Versioning (DatasetVersion)

Each successful publish **mints a new `DatasetVersion` node** in Neo4j. This graph is the spine that Story Nodes, Focus Mode, and APIs traverse.

~~~cypher
// neo4j/cypher/publish_version.cypher
MERGE (d:Dataset {id: $dataset_id})
MERGE (v:DatasetVersion {id: $version_id})
MERGE (d)-[:HAS_VERSION]->(v)
SET v.sha        = $sha,
    v.createdAt  = timestamp(),
    v.coverage   = $coverage,
    v.nullRate   = $null_rate;
~~~

---

## 📦 Data & Metadata

### 🌐 STAC/DCAT Emission (on pass)

On passing all gates, the agent writes **STAC Items/Collections** and **DCAT Datasets** to governed buckets. STAC/DCAT entries are later harvested into catalogs and exposed via APIs. [oai_citation:2‡Kansas Frontier Matrix Documentation.pdf](file-service://file-Kh5A494Gau4gS5ihmMLDuS)  

~~~yaml
publish:
  stac:
    collection: "soil-v11"
    item_schema: "schemas/stac/soil_item_v11.json"
    dest: "s3://kfm-prod/stac/soil/"
  dcat:
    dataset_schema: "schemas/dcat/dataset_v3.json"
    dest: "s3://kfm-prod/dcat/soil/"
  prov:
    dest: "s3://kfm-prod/prov/soil/"
~~~

### 📈 Telemetry (OpenTelemetry)

Telemetry captures **rows, quality signals, and environmental impact** for each run, wired into KFM’s security‑aware telemetry stack. [oai_citation:3‡Review of Kansas Frontier Matrix Security Policy and Recommendations.pdf](file-service://file-8N8jaQdyg9Q1mx52HBEJv9)  

~~~yaml
telemetry:
  exporter: "otlp"
  resource:
    service.name: "kfm-etl-agent"
    service.version: "11.2.x"
  spans:
    - name: "ingest.fetch"
    - name: "transform.apply"
    - name: "validate.gx"
    - name: "publish.stac"
    - name: "publish.dcat"
    - name: "neo4j.version.link"
  metrics:
    - name: "rows_processed"
    - name: "coverage_pct"
    - name: "null_rate_pct"
    - name: "energy_kwh"
    - name: "carbon_gco2e"
~~~

### 📦 Artifacts & Repro

For each run `run_id`, the pipeline persists a **repro bundle**:

- `prompt.txt` — Agent/system prompts that shaped the ETL behavior  
- `code.sha256` — hash of the code used  
- `gx_report.json` — Great Expectations validation output  
- `schema_diff.json` — schema comparison vs baseline  
- `energy.json`, `carbon.json` — energy and carbon telemetry  

Stored at:

- `data/artifacts/<run_id>/{prompt.txt, code.sha256, gx_report.json, schema_diff.json, energy.json, carbon.json}`  

These artifacts are referenced from STAC/DCAT `links[]` and PROV bundles so consumers can verify lineage and reproducibility. [oai_citation:4‡Kansas Frontier Matrix Documentation.pdf](file-service://file-Kh5A494Gau4gS5ihmMLDuS)  

---

## 🧪 Validation & CI/CD

### ✅ Validation Gates (Great Expectations + Schema Diff)

Data quality is enforced with **Great Expectations** and a **schema‑diff policy** (no breaking changes without an explicit contract update).

~~~yaml
# great_expectations/expectations/soil_profile.yml
expectations:
  - expect_table_row_count_to_be_between:
      min_value: 1
  - expect_column_values_to_not_be_null:
      column: "value_norm"

schema_diff:
  baseline_schema: "schemas/soil_profile_v3.json"
  allow:
    - "additive_columns"
  forbid:
    - "breaking_type_change"
~~~

### 🧪 Pre‑Publish Canary (Staging)

Before touching production catalogs/graph, the pipeline **rehearses the publish** into canary destinations and runs downstream checks.

~~~yaml
pre_publish:
  staging_bucket: "s3://kfm-staging/soil"
  staging_graph: "neo4j+s://staging-graph:7687"
  checks:
    - "downstream_joins_ok"
    - "coverage >= 99%"
    - "null_rate <= 0.5%"
    - "no_lineage_gap"
~~~

Geo‑enabled downstream checks may rely on **GeoSPARQL** when verifying spatial joins and coverage over features like tiles or H3 cells. [oai_citation:5‡GeoSPARQL: Geospatial SPARQL for the Semantic Web.pdf](file-service://file-Gcko4NCD4BXhFG42Sh7Z1o)  

### 🛡️ Guardrails, SLOs & Rollback

Guardrails encode **SLOs and error budgets**. Violations trigger auto‑rollback to the previous `DatasetVersion` and open an incident under the KFM security program. [oai_citation:6‡Review of Kansas Frontier Matrix Security Policy and Recommendations.pdf](file-service://file-8N8jaQdyg9Q1mx52HBEJv9)  

~~~yaml
guardrails:
  slo:
    publish_latency_s: { target: 600,  max: 900 }
    null_rate_pct:     { target: 0.2,  max: 0.5 }
    coverage_pct:      { target: 99.5, min: 99.0 }
  error_budget:
    window_days: 30
    budget_pct: 2.0
    auto_pause_on_breach: true
  wal:
    enable: true
    path: "data/wal/soil/"
    replay_on_retry: true

rollback:
  trigger_if:
    - "coverage_pct < 99.0"
    - "null_rate_pct > 0.5"
    - "post_publish_checks: failed"
  action:
    - "repoint_readers_to_previous_DatasetVersion"
    - "emit_alert and open_incident"
~~~

### ⚙️ GitHub Actions (event‑driven DAG + gates)

The CI workflow is the **control plane** for the agent: it orchestrates ETL, validation, canaries, SLO checks, publish, Neo4j writes, and telemetry.

~~~yaml
# .github/workflows/agent-soil.yml
name: "KFM Soil Agent — Event-Driven Publish"

on:
  workflow_dispatch:
  repository_dispatch:
    types: [new-soil-data]
  schedule:
    - cron: "0 * * * *"

jobs:
  etl-validate-publish:
    runs-on: ubuntu-latest
    env:
      PYTHONHASHSEED: "1337"
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install
        run: |
          pip install -r requirements.txt
          ge --version || true

      - name: ETL (deterministic)
        run: python -m src.pipelines.soil.ingest --seed 1337 --idempotent

      - name: Validate (Great Expectations + schema diff)
        run: make validate_soil

      - name: Pre-publish canary
        run: make canary_soil

      - name: Gate: SLO & error budget
        run: python ops/gates/slo_gate.py --policy configs/slo/soil.yml

      - name: Publish STAC/DCAT/PROV
        if: ${{ success() }}
        run: make publish_soil

      - name: Neo4j DatasetVersion
        if: ${{ success() }}
        run: >
          cypher-shell -f neo4j/cypher/publish_version.cypher
          -u neo4j -p "${{ secrets.NEO4J_PASS }}"

      - name: Emit OTEL spans
        run: python ops/telemetry/emit_spans.py --pipeline soil

      - name: Post-publish verification (rollback if degrade)
        run: >
          python ops/gates/post_publish_checks.py
          --rollback_policy configs/rollback/soil.yml
~~~

All third‑party actions MUST be pinned to immutable SHAs and run with least privilege (`GITHUB_TOKEN` read‑only by default), consistent with KFM’s security standards. [oai_citation:7‡Review of Kansas Frontier Matrix Security Policy and Recommendations.pdf](file-service://file-8N8jaQdyg9Q1mx52HBEJv9)  

---

## 🌐 STAC, DCAT & PROV Alignment

- **STAC**: Items/Collections represent **spatiotemporal assets** (tiles, rasters, vector layers). Each Item’s `properties` include:
  - spatial extent (`bbox`, geometry),
  - temporal extent (`datetime` or `start_datetime` / `end_datetime`),
  - dataset/version identifiers that map back to Neo4j `DatasetVersion` nodes. [oai_citation:8‡Kansas Frontier Matrix Documentation.pdf](file-service://file-Kh5A494Gau4gS5ihmMLDuS)  
- **DCAT**: Datasets describe higher‑level collections (e.g., “Soil Moisture v11”), with DCAT fields for title, description, publisher, temporal and spatial coverage, and license.  
- **PROV‑O**: For each run, we emit a PROV bundle:
  - `prov:Activity` for the ETL run, with `prov:startedAtTime` / `prov:endedAtTime`,  
  - `prov:Entity` for input and output assets (files, STAC Items, DCAT Datasets),  
  - `prov:Agent` for the agent/software and maintainers. [oai_citation:9‡Comprehensive Guide to W3C PROV-O.pdf](file-service://file-M7Pfz7uE2cTVgom8q9d8B3)  

This provenance can be loaded into a triple store or projected into Neo4j, enabling **provenance‑aware queries** such as “show all DatasetVersions derived from a given source dataset” or “show all runs that violated a particular SLO.”  

---

## ⚖ FAIR+CARE & Governance

- **FAIR**:  
  - **Findable** via STAC/DCAT catalogs and graph indices.  
  - **Accessible** through documented APIs and governed buckets.  
  - **Interoperable** through STAC 1.x, DCAT 3, PROV‑O, GeoSPARQL, and OWL‑Time. [oai_citation:10‡Kansas Frontier Matrix Documentation.pdf](file-service://file-Kh5A494Gau4gS5ihmMLDuS)  
  - **Reusable** via explicit licenses, provenance, and reproducible artifacts.  

- **CARE & Indigenous Sovereignty**:  
  - Sensitive locations (e.g., sites with high CARE sensitivity) must be **generalized** or **omitted** in public STAC/DCAT outputs; detailed geometry lives only in restricted catalogs/graphs. [oai_citation:11‡Review of Kansas Frontier Matrix Security Policy and Recommendations.pdf](file-service://file-8N8jaQdyg9Q1mx52HBEJv9)  
  - Any pipeline that touches Indigenous or high‑risk data MUST be co‑governed with the FAIR+CARE council and relevant community stewards.  

- **Security & Supply Chain**:  
  - Releases backed by **SBOMs, SLSA attestations, and signatures**.  
  - CI security workflows (dependency scanning, provenance checks, signature verification) are mandatory gates for this agent. [oai_citation:12‡Review of Kansas Frontier Matrix Security Policy and Recommendations.pdf](file-service://file-8N8jaQdyg9Q1mx52HBEJv9)  

---

## 🕰️ Version History

| Version | Date       | Summary                                                                                                      |
|--------:|-----------:|--------------------------------------------------------------------------------------------------------------|
| v11.2.x | 2025-12-09 | Initial governed KFM Agent Flow guide; aligned with KFM‑MDP v11.2.6; codified deterministic ETL → STAC/DCAT → Neo4j → telemetry pattern with SLO/rollback guardrails. |

---

<div align="center">

🚦 **KFM-Agent Flow: Deterministic ETL → STAC/DCAT → Neo4j → Telemetry (with Guardrails)**  
Deterministic Pipelines · Catalog‑First Lineage · FAIR+CARE Ethics · Secure & Observable CI/CD  

[📘 Docs Root](../..) · [📂 Pipelines Index](../README.md) · [⚖ Governance Charter](../../standards/governance/ROOT-GOVERNANCE.md)

</div>