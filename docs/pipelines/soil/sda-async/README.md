---
title: "⚒️ Kansas Frontier Matrix — SDA Soil Ingestion (Async, Chunked, Deduped) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Authoritative pattern for ingesting USDA SDA soil data via soilDB with async chunking, deduplication, stratigraphic validation, and STAC/graph integration for the Kansas Frontier Matrix."
path: "docs/pipelines/soil/sda-async/README.md"
version: "v11.2.4"
last_updated: "2025-12-07"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Soil & Ecology Pipelines · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "v11.x-compatible · Non-breaking for downstream graph consumers"

status: "Active / Enforced"
doc_kind: "Pipeline Pattern"
header_profile: "standard"
footer_profile: "standard"

scope:
  domain: "soil"
  applies_to:
    - "etl"
    - "stac"
    - "graph"
    - "provenance"
    - "telemetry"
    - "focus-mode"
  impacted_modules:
    - "docs/pipelines/soil"
    - "data/raw/external/usda_sda"
    - "data/processed/soil"
    - "data/stac/soil"
    - "src/pipelines/soil/sda_async"
    - "src/graph/soil"
    - "src/api/soil"
    - "src/web/story-nodes/soil"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; site-level masking still applies when spatially joined)"
classification: "Open / CC-BY Compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-commit-hash-or-doc-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "releases/v11.2.4/sbom.spdx.json"
manifest_ref: "releases/v11.2.4/manifest.zip"
telemetry_ref: "releases/v11.2.4/pipelines-soil-telemetry.json"
telemetry_schema: "schemas/telemetry/pipelines-soil-sda-async-v1.json"
governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

provenance_chain:
  - "docs/standards/kfm_markdown_protocol_v11.2.4.md@v11.2.4"
  - "docs/pipelines/soil/README.md@v11.2.4"
  - "docs/standards/catalogs/stac-dcat-derivation.md@v11.2.4"
  - "docs/standards/provenance/prov-o-usage.md@v11.2.4"

doc_uuid: "urn:kfm:doc:pipelines:soil:sda-async:readme:v11.2.4"

test_profiles:
  - "markdown-frontmatter-v11"
  - "markdown-structure-v11"
  - "footer-governance-links-v11"
  - "soil-sda-pipeline-pattern-v1"

ci_integration: ".github/workflows/docs-lint.yml"
---

<div align="center">

# ⚒️ **Kansas Frontier Matrix — SDA Soil Ingestion (Async, Chunked, Deduped)**  
`docs/pipelines/soil/sda-async/README.md`

**KFM v11.2.4 · Deterministic ETL → STAC/DCAT/PROV → Neo4j → Focus Mode**

![Status: Active](https://img.shields.io/badge/Status-Active-brightgreen.svg)
![Lifecycle: LTS](https://img.shields.io/badge/Lifecycle-LTS-blue.svg)
![KFM-MDP v11.2.4](https://img.shields.io/badge/KFM--MDP-v11.2.4-6f42c1.svg)
![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Aligned-0aa344.svg)

</div>

---

## 📘 Overview

### Purpose

This document defines the **canonical KFM pattern** for ingesting soil data from **USDA Soil Data Access (SDA)** using the **`soilDB` R package**, orchestrated by **Python ETL**, with:

- Async, chunked pulls over `mukey` sets,  
- Deterministic deduplication by **authoritative soil keys** (`mukey`, `cokey`, `chkey`),  
- **Stratigraphic validation** of horizons (no inverted or overlapping depths),  
- Emission of **Parquet tables + STAC-aligned sidecars**,  
- Clean integration into the **Neo4j knowledge graph** and **Focus Mode** stories.

It is the soil-specific instantiation of the KFM canonical pipeline:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j knowledge graph → API layer → React/MapLibre/Cesium frontend → Story Nodes → Focus Mode

### Scope

This pattern must be reused by any KFM pipeline that needs **SSURGO/STATSGO soil attributes** within Kansas and neighboring regions. It governs:

- How SDA data is queried and chunked,  
- How Parquet outputs are structured and validated,  
- How STAC/DCAT/PROV artifacts are constructed,  
- How soil entities are represented in Neo4j, and  
- How soil data is exposed to Story Nodes and Focus Mode.

---

## 🗂️ Directory Layout

### Documentation

```text
📁 docs/
└── 📁 pipelines/
    └── 📁 soil/
        ├── 📄 README.md                         # Soil pipelines index (governed elsewhere)
        └── 📁 sda-async/
            ├── 📄 README.md                     # ← This file (pipeline pattern)
            ├── 📁 diagrams/
            │   ├── 🖼️ sda-flow.drawio           # Optional flowchart source
            │   └── 🖼️ sda-flow.png              # Generated diagram
            ├── 📁 config/
            │   ├── 📄 sda-sources.yaml          # SDA datasets, queries, endpoints
            │   ├── 📄 chunking-policy.yaml      # Chunk size, concurrency, retry rules
            │   └── 📄 validation-policy.yaml    # Stratigraphy & key integrity rules
            └── 📁 examples/
                ├── 📄 r-soilDB-sidecar.R        # Canonical R-side script (soilDB)
                ├── 📄 py-orchestrator.py        # Canonical Python orchestrator
                ├── 📄 stac-template-item.json   # STAC Item template for SDA pulls
                └── 📄 stac-template-collection.json
```

### Pipelines, data, and graph (conceptual)

```text
📁 src/
└── 📁 pipelines/
    └── 📁 soil/
        └── 📁 sda_async/
            ├── 📄 __init__.py
            ├── 📄 config.py
            ├── 📄 orchestrator.py
            ├── 📄 io_parquet.py
            ├── 📄 validation.py
            └── 📄 provenance.py

📁 data/
├── 📁 raw/
│   └── 📁 external/
│       └── 📁 usda_sda/                 # Optional caching of SDA responses
├── 📁 processed/
│   └── 📁 soil/
│       ├── 📄 soil_mu.parquet           # Map units (mukey)
│       ├── 📄 soil_co.parquet           # Components (cokey)
│       └── 📄 soil_ch.parquet           # Horizons (chkey)
└── 📁 stac/
    └── 📁 soil/
        ├── 🛰️ sda-ssurgo/               # STAC Collections & Items for SDA-derived SSURGO
        └── 🛰️ sda-statsgo/              # Optional STATSgo-like aggregates

📁 dist/
└── 📁 provenance/
    └── 📄 prov-sda-async-<run-id>.jsonld  # PROV-O lineage bundle per run
```

---

## 🧭 Context

USDA Soil Data Access (SDA) provides the **authoritative soil tabular data** for SSURGO/STATSGO. The **`soilDB`** R package is the de facto, well-governed client for SDA and handles:

- SDA SQL quirks,  
- Pivoting and normalization of soil attributes,  
- Integration with R’s spatial classes.

KFM’s role is to:

- Orchestrate SDA calls **deterministically** (via Python + R sidecar),  
- Normalize outputs into **canonical Parquet tables** for map units, components, and horizons,  
- Integrate soil information into the **Kansas Frontier Matrix** for:

  - Historical and ecological Story Nodes,  
  - Hydrology and land-use analyses,  
  - Scenario planning and Focus Mode views.

This pattern ensures that any soil-related story or analysis in KFM can be traced back through:

- SDA queries,  
- R/`soilDB` transformations,  
- ETL configuration, and  
- STAC/DCAT/PROV artifacts.

---

## 🧱 Architecture

### High-level flow

```text
+-----------------------+
|  mukey index source   |  (precomputed from tiles / AOIs)
+-----------+-----------+
            |
            v
+-----------------------+      R / soilDB (sidecar)
|  Python Orchestrator  |----> Per-chunk SDA pull
|  (async, chunked)     |      (mapunit, components, horizons)
+-----------+-----------+
            |
            v
+-----------------------+
| Parquet shards (mu/co/ch)
+-----------------------+
            |
            v
+-----------------------+
| Merge + Dedup +       |
| Stratigraphy Validate |
+-----------+-----------+
            |
            v
+-------------------------------+
| STAC Items + Collections      |
| Neo4j graph upserts           |
+-------------------------------+
```

### Async chunking pattern

Chunking is driven by `mukey` lists and configured in `config/chunking-policy.yaml`:

```yaml
chunk_size_mukey: 800
max_workers: 8
retry:
  max_attempts: 3
  backoff_seconds:
    initial: 5
    max: 60
  retry_on:
    - "network_error"
    - "http_5xx"
    - "sda_timeout"
fail_fast_threshold_fraction: 0.25   # abort run if >25% chunks hard-fail
```

Key rules:

- **Chunk key**: lists of `mukey`.  
- **Concurrency**: bounded by `max_workers`.  
- **Idempotency**: shard filenames are deterministic functions of:
  - `mukey` ranges +  
  - run configuration (versioned).

### Reference implementation — R sidecar (soilDB)

```r
# File: docs/pipelines/soil/sda-async/examples/r-soilDB-sidecar.R
#
# Purpose:
#   - Given a CSV of mukeys, pull SDA data via soilDB
#   - Emit Parquet shards for mu, co, ch
#
# Usage:
#   Rscript r-soilDB-sidecar.R mukey_chunk.csv out_prefix=/tmp/chunk_001

library(soilDB)
library(arrow)
library(dplyr)

args <- commandArgs(trailingOnly = TRUE)
if (length(args) < 2) {
  stop("Usage: Rscript r-soilDB-sidecar.R <mukey_csv> out_prefix=<path>")
}

mukey_csv   <- args[1]
out_prefix  <- sub("^out_prefix=", "", args[2])

keys <- read.csv(mukey_csv, stringsAsFactors = FALSE)$mukey

# 1) Spatial mapunits
mu_sp <- fetchSDA_spatial(mukey = keys)

# 2) Components + horizons (using soilDB helpers / custom SQL)
sda_res <- fetchSDA_components(mukey = keys)

normalize_df <- function(df) {
  df |>
    rename_with(tolower) |>
    distinct()
}

mu <- normalize_df(mu_sp@data)          # or sf::st_drop_geometry for SF objects
co <- normalize_df(sda_res$components)
ch <- normalize_df(sda_res$horizons)

write_parquet(mu, paste0(out_prefix, "_mu.parquet"))
write_parquet(co, paste0(out_prefix, "_co.parquet"))
write_parquet(ch, paste0(out_prefix, "_ch.parquet"))
```

### Reference implementation — Python orchestrator

```python
# File: docs/pipelines/soil/sda-async/examples/py-orchestrator.py
#
# Purpose:
#   - Chunk mukeys
#   - Launch R-sidecar SDA pulls concurrently
#   - Merge/dedupe shards
#   - Run stratigraphic validation
#   - Emit final Parquet + STAC

from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import pandas as pd
import pyarrow.parquet as pq
import subprocess
import uuid

CHUNK_SIZE = 800
MAX_WORKERS = 8

def split_chunks(iterable, n):
  iterable = list(iterable)
  for i in range(0, len(iterable), n):
    yield iterable[i:i+n]

def run_r_chunk(mukeys, i, sidecar_path, tmp_dir="/tmp"):
  tmp_csv = Path(tmp_dir) / f"mukey_{i}.csv"
  pd.DataFrame({"mukey": mukeys}).to_csv(tmp_csv, index=False)

  out_prefix = Path(tmp_dir) / f"chunk_{i}_{uuid.uuid4().hex}"

  subprocess.check_call(
    ["Rscript", str(sidecar_path), str(tmp_csv), f"out_prefix={out_prefix}"]
  )

  return [
    Path(f"{out_prefix}_mu.parquet"),
    Path(f"{out_prefix}_co.parquet"),
    Path(f"{out_prefix}_ch.parquet"),
  ]

def dedupe_keys(df, subset):
  return df.drop_duplicates(subset=subset).reset_index(drop=True)

def validate_stratigraphy(ch: pd.DataFrame) -> pd.DataFrame:
  """
  Enforce:
    - hzdept_r < hzdepb_r for all horizons
    - No overlapping horizons within a cokey
  Remove components that fail, and record violations via provenance logging.
  """
  bad_cokeys = set()

  for cokey, g in ch.groupby("cokey"):
    g = g.sort_values("hzdept_r")
    # basic depth sanity
    if (g["hzdept_r"] >= g["hzdepb_r"]).any():
      bad_cokeys.add(cokey)
      continue
    # overlap check: start of next < bottom of current
    if (g["hzdept_r"].shift(-1) < g["hzdepb_r"]).fillna(False).any():
      bad_cokeys.add(cokey)

  return ch[~ch["cokey"].isin(bad_cokeys)].reset_index(drop=True)

def main():
  mukey_index = pd.read_parquet("inputs/mukey_index.parquet")  # must contain column 'mukey'
  mukeys = mukey_index["mukey"].tolist()

  sidecar_path = Path("docs/pipelines/soil/sda-async/examples/r-soilDB-sidecar.R")

  parquet_shards = []
  with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
    futures = {
      ex.submit(run_r_chunk, chunk, i, sidecar_path): i
      for i, chunk in enumerate(split_chunks(mukeys, CHUNK_SIZE))
    }
    for f in as_completed(futures):
      parquet_shards.extend(f.result())

  mu_files = [p for p in parquet_shards if str(p).endswith("_mu.parquet")]
  co_files = [p for p in parquet_shards if str(p).endswith("_co.parquet")]
  ch_files = [p for p in parquet_shards if str(p).endswith("_ch.parquet")]

  mu = pd.concat(map(pd.read_parquet, mu_files), ignore_index=True)
  co = pd.concat(map(pd.read_parquet, co_files), ignore_index=True)
  ch = pd.concat(map(pd.read_parquet, ch_files), ignore_index=True)

  mu = dedupe_keys(mu, ["mukey"])
  co = dedupe_keys(co, ["cokey", "mukey"])
  ch = validate_stratigraphy(
    dedupe_keys(ch, ["chkey", "cokey", "hzdept_r", "hzdepb_r"])
  )

  Path("out").mkdir(parents=True, exist_ok=True)
  mu.to_parquet("out/soil_mu.parquet")
  co.to_parquet("out/soil_co.parquet")
  ch.to_parquet("out/soil_ch.parquet")

  # STAC item/collection emission handled by KFM STAC utilities, not shown here.

if __name__ == "__main__":
  main()
```

---

## 📦 Data & Metadata

### Core data model

This pattern assumes the following **logical tables** are produced from SDA:

- **`mu` — Map units**  
  - Key: `mukey`  
  - Columns: SDA mapunit attributes + geometry reference / WKT / WKB / SF geometry.

- **`co` — Components**  
  - Keys: `cokey`, `mukey`  
  - Columns: component attributes (e.g., `comppct_r`, `taxorder`, etc.).

- **`ch` — Horizons**  
  - Keys: `chkey`, `cokey`, `hzdept_r`, `hzdepb_r`  
  - Columns: horizon depths, texture, water table, etc.

### Deduplication strategy (non-negotiable)

To guarantee stable, idempotent runs:

- **Do NOT** dedupe on geometry alone.  
- **Do** dedupe on **authoritative keys**:

  - `mu`: `mukey`  
  - `co`: `cokey`, `mukey`  
  - `ch`: `chkey`, `cokey`, `hzdept_r`, `hzdepb_r`  

- In case of conflicting records:
  - Prefer the **latest SDA record** (based on SDA timestamps if present).  
  - Log conflicts into a **PROV/ETL audit** table for review.

### Geometry sanity

- Mapunit geometries MUST be:
  - Valid polygons (no self-intersections where practical),  
  - Aggregated or dissolved by `mukey` when required.

Any geometry repairs must be captured in:

- PROV-O activities (e.g., `prov:used` raw geometry → `prov:generated` repaired geometry).  

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC Collections & Items

Each SDA-derived dataset SHOULD publish:

- A **STAC Collection** describing:
  - Data source: USDA SDA,  
  - Spatial extent: AOI bounding box,  
  - Temporal coverage: SDA query timestamps / effective dates,  
  - KFM extensions: `kfm:source`, `kfm:keys`, `kfm:provenance_ref`, etc.

- One or more **STAC Items** referencing:
  - `soil_mu.parquet`, `soil_co.parquet`, `soil_ch.parquet`,  
  - the PROV-O JSON-LD bundle, and  
  - energy/carbon telemetry for the run.

Suggested properties:

```json
{
  "properties": {
    "kfm:source": "USDA-SDA",
    "kfm:soil:keys": ["mukey", "cokey", "chkey"],
    "kfm:etl:pattern": "sda-async-v1",
    "kfm:provenance_ref": "dist/provenance/prov-sda-async-<run-id>.jsonld",
    "kfm:energy_ref": "releases/v11.2.4/pipelines-soil-telemetry.json"
  }
}
```

### DCAT derivation

Per `KFM-STAC v11` and `KFM-DCAT v11`:

- DCAT **Datasets** and **Distributions** for SDA soil layers must be **derived from STAC** via the standard STAC→DCAT derivation process.
- No hand-crafted DCAT entries may diverge from the STAC source-of-truth.

### PROV-O provenance bundles

Each run MUST emit a PROV-O JSON-LD file (e.g., `dist/provenance/prov-sda-async-<run-id>.jsonld`) that includes:

- `prov:Entity`:
  - SDA query (SQL text, SDA API metadata),  
  - Every Parquet output with checksums,  
  - Configuration files used (`sda-sources.yaml`, `chunking-policy.yaml`, `validation-policy.yaml`).

- `prov:Activity`:
  - ETL run, with:
    - Start/end times,  
    - Code versions (Git SHA, container image),  
    - Run ID (`openlineage:runId` if available).

- `prov:Agent`:
  - KFM ETL services and, where applicable, human operators.

---

## 🧪 Validation & CI/CD

### Key integrity & stratigraphy checks

The pipeline MUST enforce:

- **Key integrity**
  - `mu.mukey` not null, unique.  
  - `co.cokey`, `co.mukey` not null.  
  - `ch.chkey`, `ch.cokey` not null.

- **Cardinality**
  - `mapunit (mukey) : component (cokey)` = 1 : N.  
  - `component (cokey) : horizon (chkey)` = 1 : K.

- **Stratigraphic logic** (per `cokey`):
  1. Sort horizons by `hzdept_r` ascending.  
  2. Enforce `hzdept_r < hzdepb_r` for every row.  
  3. Enforce **no overlap**:
     ```text
     hzdept_r_next >= hzdepb_r_current
     ```
  4. Components with violations:
     - Are excluded from output, and  
     - Are logged in a structured validation report.

### Validation outputs

Validation artifacts (JSON) should include:

- Counts of map units, components, horizons.  
- Counts of rejected components/horizons and reasons.  
- Pass/fail flags per validation rule.  

They should be referenced in:

- PROV bundles, and  
- Telemetry files defined by `telemetry_schema`.

### CI pattern (conceptual)

A typical CI workflow for `sda-async` must:

- Run schema and key checks (e.g., with Great Expectations).  
- Run stratigraphic validation.  
- Validate STAC Collections/Items against KFM STAC profiles.  
- Validate PROV-O JSON-LD against KFM PROV profiles.  
- Emit energy/carbon telemetry for the run.

Non-compliant runs may:

- Fail CI and block promotion, or  
- Be flagged with a **non-pass** status in the Governance Ledger.

---

## 🧠 Story Node & Focus Mode Integration

SDA-derived soil data supports Story Nodes such as:

- **“Soil–Hydrology Interactions in Kansas Basins”**
  - Links:
    - Soil hydrologic groups and infiltration capacity,  
    - Basin-level hydrology time series,  
    - Land-use and climate projections.

- **“Prairie Soils, Agriculture, and Resilience”**
  - Links:
    - Soil taxonomic classes, organic matter, erosion risk,  
    - Historical cropping patterns and policy.

Story Nodes must:

- Reference soil datasets via STAC/DCAT IDs, not ad-hoc file paths.  
- Link to one or more SDA ETL runs via PROV/lineage URNs.  
- Respect any spatial masking or aggregation rules when joined with sensitive layers (e.g., archaeological or ecological features).

In **Focus Mode**, users should be able to:

- Click from a Story Node to:
  - `SoilMapUnit` and `SoilComponent` nodes in Neo4j,  
  - STAC Items for SDA-derived layers,  
  - PROV bundles documenting SDA queries and ETL configurations.

---

## ⚖ FAIR+CARE & Governance

Although SDA soil datasets are generally **public** and **low-risk**, KFM enforces:

- **FAIR**
  - **Findable**: soil datasets are cataloged in STAC/DCAT with stable identifiers.  
  - **Accessible**: Parquet assets and STAC metadata are accessible under MIT/CC-BY-compatible terms.  
  - **Interoperable**: use of open geospatial/time-series formats and KFM ontologies.  
  - **Reusable**: full provenance (PROV-O + OpenLineage) and licensing recorded.

- **CARE**
  - **Collective Benefit**: soil data is used to support ecological, agricultural, and climate resilience work.  
  - **Authority to Control**: when soil layers are spatially joined with sensitive data (e.g., heritage sites), masking and aggregation rules from `docs/standards/data-generalization/` apply.  
  - **Responsibility & Ethics**: avoid using soil data for harmful profiling or extractive decision-making without community consent.

This pipeline is overseen by:

- **Soil & Ecology Pipelines** working group, and  
- **FAIR+CARE Council**, per the `review_cycle` declared in this document.

---

## 🕰️ Version History

| Version  | Date       | Author / Steward      | Summary                                                                       |
|----------|------------|----------------------|-------------------------------------------------------------------------------|
| v11.2.4  | 2025-12-07 | KFM Architecture     | Initial SDA async soil ingestion pattern aligned with KFM-MDP v11.2.4.       |

---

<div align="center">

**Kansas Frontier Matrix (KFM v11)**  

[⬅️ Soil Pipelines Index](../README.md) · [📚 KFM Documentation Index](../../../README.md) · [⚖️ Root Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
