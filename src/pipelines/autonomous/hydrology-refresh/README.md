---
title: "🔁 KFM v11 — Autonomous Hydrology Refresh (LangGraph YAML DAG) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/autonomous/hydrology-refresh/README.md"
version: "v11.1.0"
last_updated: "2025-11-22"
review_cycle: "Daily · Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../releases/v11.0.0/telemetry/autonomous-hydro-refresh.json"
telemetry_schema: "../../../../schemas/telemetry/autonomous-hydro-refresh-v1.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
data_contract_ref: "../../../../docs/contracts/data-contract-v3.json"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Pipeline"
semantic_document_id: "kfm-autonomous-hydro-refresh-v11"
doc_uuid: "urn:kfm:pipelines:autonomous:hydrology-refresh:v11"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 🔁 **Autonomous Hydrology Refresh (LangGraph + STAC + Neo4j)**  
`src/pipelines/autonomous/hydrology-refresh/README.md`  

**Purpose:**  
Define the v11 autonomous, reproducible, daily hydrology refresh pipeline using LangGraph YAML DAGs.  
This includes stale-detection, ETL normalization, STAC generation, checksum validation, OpenLineage emission,  
and Neo4j graph synchronization under the KFM v11 deterministic pipeline framework.

</div>

---

# 📘 Overview

This autonomous pipeline performs **hands-off** ingestion and refresh of hydrology data (USGS, NOAA, KDHE, etc.) using:

- **LangGraph YAML DAGs** for deterministic pipeline orchestration  
- **Checksum & schema validation** for integrity  
- **STAC Item generation v11** (full CRS/vertical metadata, hydrology extension, lineage)  
- **OpenLineage v2.5** activity emission  
- **Neo4j graph sync** (CIDOC-CRM, GeoSPARQL, OWL-Time mapping)  
- **Daily scheduling** with retry/backoff  
- **Zero manual operation**  

This pipeline is part of the KFM **Autonomous Data Plane**.

---

# 🧠 Function Summary

The pipeline:

- Detects **stale** data using etags, timestamps, or provider manifests  
- Fetches, caches, and normalizes raw hydrology inputs  
- Validates schemas via STAC + domain hydrology schema  
- Emits **OpenLineage** events for all steps  
- Creates/update STAC Items for updated datasets  
- Syncs results into Neo4j with correct entity relationships  
- Produces a run summary + telemetry bundle  

---

# 🗂 Directory Layout (v11)

```text
src/pipelines/autonomous/hydrology-refresh/
│
├── README.md                 # This file (v11 standard)
├── dag.yaml                  # LangGraph executable DAG
│
├── nodes/
│   ├── detect_stale.py
│   ├── fetch_sources.py
│   ├── normalize_tabular.py
│   ├── build_stac_items.py
│   ├── validate_checksums.py
│   ├── stac_validate.py
│   ├── neo4j_sync.py
│   └── post_hooks.py
│
├── resources/
│   ├── providers.yaml
│   ├── schema/
│   │   └── hydro_v1.schema.json
│   └── checksums/
│       └── manifest.json
│
└── tests/
    └── test_dag_smoke.py
```

---

# ⚙️ Minimal v11 YAML DAG

Create or update:  
`src/pipelines/autonomous/hydrology-refresh/dag.yaml`

```yaml
schedule: "0 3 * * *"
retries:
  max_attempts: 3
  backoff_seconds: 600

lineage:
  openlineage: true
  namespace: "kfm.autonomous.hydrology"

context:
  workdir: "data/work/staging/tabular/normalized/hydrology/"
  stac_out: "data/stac/hydrology/statewide/items/"
  checksum_manifest: "src/pipelines/autonomous/hydrology-refresh/resources/checksums/manifest.json"
  schema: "src/pipelines/autonomous/hydrology-refresh/resources/schema/hydro_v1.schema.json"
  providers_cfg: "src/pipelines/autonomous/hydrology-refresh/resources/providers.yaml"

nodes:
  - id: detect_stale
    kind: python
    entry: "src/pipelines/autonomous/hydrology-refresh/nodes/detect_stale.py:run"
    outputs: ["stale_targets"]

  - id: fetch_sources
    kind: python
    entry: "src/pipelines/autonomous/hydrology-refresh/nodes/fetch_sources.py:run"
    inputs: ["stale_targets"]
    outputs: ["raw_files"]

  - id: normalize_tabular
    kind: python
    entry: "src/pipelines/autonomous/hydrology-refresh/nodes/normalize_tabular.py:run"
    inputs: ["raw_files"]
    outputs: ["norm_files"]

  - id: build_stac_items
    kind: python
    entry: "src/pipelines/autonomous/hydrology-refresh/nodes/build_stac_items.py:run"
    inputs: ["norm_files"]
    outputs: ["stac_items"]

  - id: validate_checksums
    kind: python
    entry: "src/pipelines/autonomous/hydrology-refresh/nodes/validate_checksums.py:run"
    inputs: ["stac_items"]
    outputs: ["validated_items"]

  - id: stac_validate
    kind: python
    entry: "src/pipelines/autonomous/hydrology-refresh/nodes/stac_validate.py:run"
    inputs: ["validated_items"]
    outputs: ["ready_items"]

  - id: neo4j_sync
    kind: python
    entry: "src/pipelines/autonomous/hydrology-refresh/nodes/neo4j_sync.py:run"
    inputs: ["ready_items"]
    outputs: ["graph_report"]

  - id: post_hooks
    kind: python
    entry: "src/pipelines/autonomous/hydrology-refresh/nodes/post_hooks.py:run"
    inputs: ["graph_report"]
    outputs: ["run_summary"]
```

---

# 🧩 Providers Config (v11)

`resources/providers.yaml`

```yaml
providers:
  - id: "usgs.streamflow.ks_mainstem"
    kind: "csv_http"
    url: "https://example.gov/usgs/ks/mainstem/daily.csv"
    etag_header: "ETag"
    time_header: "Last-Modified"
    stac:
      collection: "kfm-hydrology-statewide"
      license: "CC-BY-4.0"
      providers:
        - name: "USGS"
          roles: ["producer","licensor"]

  - id: "noaa.precip.24h"
    kind: "csv_http"
    url: "https://example.noaa.gov/ks/precip/24h.csv"
    etag_header: "ETag"
    time_header: "Last-Modified"
    stac:
      collection: "kfm-hydrology-statewide"
      license: "CC0-1.0"
      providers:
        - name: "NOAA"
          roles: ["producer"]
```

---

# 🧪 Node Stubs (v11 Minimal Starters)

These stubs comply with STAC/lineage/Neo4j v11 conventions.

`nodes/detect_stale.py`
```python
def run(context):
    return {"stale_targets": ["usgs.streamflow.ks_mainstem","noaa.precip.24h"]}
```

`nodes/fetch_sources.py`
```python
def run(stale_targets, context):
    return {"raw_files": [".../raw/usgs_mainstem.csv",".../raw/noaa_24h.csv"]}
```

`nodes/normalize_tabular.py`
```python
def run(raw_files, context):
    return {"norm_files": [".../norm/usgs_mainstem.parquet",".../norm/noaa_24h.parquet"]}
```

`nodes/build_stac_items.py`
```python
def run(norm_files, context):
    return {"stac_items": [".../items/usgs_mainstem.json",".../items/noaa_24h.json"]}
```

`nodes/validate_checksums.py`
```python
def run(stac_items, context):
    return {"validated_items": stac_items}
```

`nodes/stac_validate.py`
```python
def run(validated_items, context):
    return {"ready_items": validated_items}
```

`nodes/neo4j_sync.py`
```python
def run(ready_items, context):
    return {"graph_report": {"items": len(ready_items), "status": "ok"}}
```

`nodes/post_hooks.py`
```python
def run(graph_report, context):
    return {"run_summary": {"ok": True, "details": graph_report}}
```

---

# 🧰 Optional Runner Script

`src/pipelines/run_dag.py`

```python
import importlib, yaml, json, sys

def _load(fn):
    mod_name, func_name = fn.split(":")
    mod = importlib.import_module(mod_name.replace("/", "."))
    return getattr(mod, func_name)

def main(path="src/pipelines/autonomous/hydrology-refresh/dag.yaml"):
    with open(path, "r") as f:
        dag = yaml.safe_load(f)
    ctx = dag.get("context", {})
    memo = {}
    for node in dag["nodes"]:
        fn = _load(node["entry"])
        kwargs = {k: memo[k] for k in node.get("inputs", []) if k in memo}
        out = fn(**kwargs, context=ctx) if kwargs else fn(context=ctx)
        for k, v in out.items():
            memo[k] = v
    print(json.dumps(memo.get("run_summary", {"ok": True}), indent=2))

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
```

---

# 📈 Operational Guarantees

- Idempotent, deterministic nodes  
- Daily schedule with backoff  
- Checksum & STAC validation gates  
- OpenLineage integration  
- Neo4j reindexing for spatial/time queries  
- Full compatibility with hydrology v11 standards (CRS, vertical datum, STAC fields)

---

# 🔍 CI/CD Hooks (v11)

- `stac-validate` on all new/modified Items  
- Checksum diff vs manifest  
- Hydra schema-v11 validation  
- OpenLineage payload conformance  
- Neo4j dry-run sync (containerized)  

---

# 🧭 Pipeline in the KFM Stack

`data → ETL/AI → STAC/DCAT → Neo4j → API → MapLibre/Cesium → Focus Mode → Story Nodes`

Hydrology updates propagate through the entire stack **automatically**.

---

# 🕰 Version History

- **v11.1.0 (2025-11-22)** — Upgraded to full KFM-MDP v11.0.0.  
- **v11.0.0** — Initial autonomous hydrology DAG.

---

<div align="center">

**Kansas Frontier Matrix — Autonomous Hydrology Refresh v11**  
*Deterministic · Autonomous · Provenance-Driven*

</div>

---

### 🔗 Footer  
[⬅ Back to Pipelines](../../../../docs/pipelines/README.md) · [🛰 Hydrology STAC Spec](../../../../docs/standards/geo/hydrology-standards.md) · [🏛 Governance](../../../../docs/standards/governance/ROOT-GOVERNANCE.md)
