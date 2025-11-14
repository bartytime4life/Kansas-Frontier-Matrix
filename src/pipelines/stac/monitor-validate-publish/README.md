Here’s a drop‑in, GitHub‑ready Markdown that sets up a STAC polling + validation + publish loop tailored to your KFM stack, using ETags, Great Expectations, and GitHub Actions on a cron. It follows your Markdown Output Protocol (YAML front‑matter, centered title, required sections, Mermaid, directory layout, badges, governance, version history) and stays within one box for copy/paste.

---
title: "🛰️ Kansas Frontier Matrix — STAC Monitor → Validate → Publish Orchestrator (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/stac/monitor-validate-publish/README.md"
version: "v10.3.0"
last_updated: "2025-11-14"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/pipelines-stac-orchestrator-v1.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🛰️ **Kansas Frontier Matrix — STAC Monitor → Validate → Publish Orchestrator**  
`src/pipelines/stac/monitor-validate-publish/README.md`

**Purpose:** Turn **STAC API Item Search** results in the Kansas AOI into reliable, validated items and collections, then **upsert** them to KFM storage/graph on a schedule. Uses **HTTP conditional requests (ETag / If-None-Match)** for efficient polling, **Great Expectations** for schema/range/uniqueness checks, and **GitHub Actions** for cron orchestration and attestable CI.

**Scope:** KFM-wide ingestion of remote sensing & environmental feeds (NOAA/USGS/NASA vendors) within Kansas bounding geometries, producing ready-to-serve STAC assets, provenance, and Neo4j graph links.

</div>

---

## ✅ Goals & Non‑Goals

- **Goals**
  - Poll STAC Item Search for **new/changed** Items in the **Kansas AOI**.
  - Cache and reuse **ETags** so unchanged queries return **304 Not Modified**.
  - Run **Great Expectations Checkpoints** as the **gate** for downstream publish.
  - **Upsert** STAC Items/Collections, refresh **graph edges** (Scenes→Datasets→Themes).
  - Orchestrate on **cron** with **GitHub Actions**, produce artifacts & SLSA/SBOM links.

- **Non‑Goals**
  - Full data science analysis; this is an ingestion/validation/publish loop.
  - Long‑term warehousing strategy (covered in `src/ARCHITECTURE.md`).

---

## 🧭 Kansas AOI

- Authoritative AOI lives at `data/geometry/kansas_aoi.geojson` (CRS: EPSG:4326).
- Derived tiling (H3/quadbin) may be generated to shard polling windows.

---

## 🧩 Flow Overview

### Orchestrator Diagram

```mermaid
flowchart LR
  A[Schedule GitHub Actions] --> B[Poll STAC API with If-None-Match]
  B -->|304 Not Modified| Z[No-Op & Telemetry]
  B -->|200 OK with Items| C[Stage Raw JSONL in data/stac/incoming]
  C --> D[Great Expectations Checkpoint]
  D -->|PASS| E[Transform & Normalize STAC]
  D -->|FAIL| F[Quarantine + Open Issue]
  E --> G[Upsert Items/Collections to data/stac/published]
  G --> H[Update Neo4j Graph Links]
  H --> I[Emit Telemetry + Artifacts]


⸻

📦 Repo Layout (Excerpt)

src/pipelines/stac/monitor-validate-publish/
├─ monitor.py
├─ publish.py
├─ transform.py
├─ etag_cache.json
├─ expectations/
│  ├─ great_expectations.yml
│  ├─ checkpoints/stac_items.yml
│  └─ expectations/stac_item_schema.json
data/stac/
├─ incoming/               # raw polled JSONL
├─ quarantine/             # failed validation
└─ published/              # validated Items/Collections
data/geometry/
└─ kansas_aoi.geojson
.github/workflows/
└─ stac-orchestrator.yml


⸻

🌐 Polling STAC API Efficiently (ETag / If‑None‑Match)

Why: Save bandwidth and API quotas. If nothing changed, server returns 304.

Item Search Query (example):
	•	Endpoint: <PROVIDER_STAC_API>/search
	•	Filters: intersects=<Kansas AOI>, datetime=2020-01-01T00:00:00Z/.., limit=200, collections=[...]

cURL sketch:

ETAG_FILE="src/pipelines/stac/monitor-validate-publish/etag_cache.json"
ETAG=$(jq -r '.search_etag // empty' "$ETAG_FILE" 2>/dev/null)

curl -sS -X POST "${STAC_API}/search" \
  -H "Content-Type: application/json" \
  -H "If-None-Match: ${ETAG}" \
  -d @- <<'JSON' | tee /tmp/stac_response.json
{
  "collections": ["landsat-c2-l2","sentinel-2-l2a"],
  "intersects": { /* load data/geometry/kansas_aoi.geojson */ },
  "datetime": "2020-01-01T00:00:00Z/..",
  "limit": 200
}
JSON

# Capture ETag for next run (if provided on 200)
RESP_CODE=$(jq -r '."http_code" // empty' <<<"{}") # replace with runner-provided status if needed
NEW_ETAG=$(jq -r '."etag" // empty' <<<"{}")       # replace via response headers capture

Python (requests) snippet to persist ETag:

import json, requests
from pathlib import Path

cache = Path("src/pipelines/stac/monitor-validate-publish/etag_cache.json")
etag_cache = json.loads(cache.read_text()) if cache.exists() else {}

headers = {"Content-Type": "application/json"}
if etag_cache.get("search_etag"):
    headers["If-None-Match"] = etag_cache["search_etag"]

payload = {
    "collections": ["landsat-c2-l2","sentinel-2-l2a"],
    "intersects": json.loads(Path("data/geometry/kansas_aoi.geojson").read_text()),
    "datetime": "2020-01-01T00:00:00Z/..",
    "limit": 200
}
resp = requests.post(f"{STAC_API}/search", json=payload, headers=headers)

if resp.status_code == 304:
    print("No changes (304).")
else:
    resp.raise_for_status()
    Path("data/stac/incoming/items.jsonl").write_text(
        "\n".join(json.dumps(f) for f in resp.json().get("features", []))
    )
    if "ETag" in resp.headers:
        etag_cache["search_etag"] = resp.headers["ETag"]
        cache.write_text(json.dumps(etag_cache, indent=2))


⸻

🔎 Validation Gate (Great Expectations)
	•	Checkpoint: expectations/checkpoints/stac_items.yml
	•	Covers: JSON schema conformity, numeric ranges (e.g., cloud cover 0..100), field presence, ID uniqueness, link integrity.
	•	Outcome:
	•	PASS → proceed to transform/publish
	•	FAIL → move batch to data/stac/quarantine/ and open a GitHub Issue with findings

Minimal GE CLI pattern:

cd src/pipelines/stac/monitor-validate-publish/expectations
great_expectations checkpoint run stac_items \
  --config "great_expectations.yml" \
  --suite "stac_item_suite"


⸻

🧪 Transform → Normalize
	•	Normalize Item properties, ensure proj:* & eo:* fields present when applicable.
	•	Recompute/verify assets (media types, roles), fix relative hrefs, embed created/updated.
	•	Add KFM provenance blocks (source, license, ingest signature hash).

# transform.py (excerpt)
def normalize_item(item: dict) -> dict:
    item["properties"].setdefault("kfm:ingest_version", "v10.3.0")
    # ensure datetime, gsd, cloud_cover normalization, media types, etc.
    return item


⸻

⬆️ Publish (Upsert Items & Collections)
	•	Write validated outputs to data/stac/published/collections/<id>.json and .../items/<collection>/<id>.json.
	•	Graph links: call Neo4j to (create or) merge nodes and relationships:
(:Scene {stac_id})-[:BELONGS_TO]->(:Dataset {collection_id})-[:THEMATIC]->(:Theme {name}).

# publish.py (excerpt)
from neo4j import GraphDatabase

def upsert_graph(item):
    with GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASS)) as d:
        q = """
        MERGE (s:Scene {stac_id: $id})
        SET s.updated = timestamp(), s.datetime = $dt
        MERGE (dset:Dataset {id: $collection})
        MERGE (s)-[:BELONGS_TO]->(dset)
        """
        d.session().run(q, id=item["id"], dt=item["properties"]["datetime"], collection=item["collection"])


⸻

⏱️ GitHub Actions (Cron + Artifacts)

File: .github/workflows/stac-orchestrator.yml

name: STAC Orchestrator

on:
  schedule:
    - cron: "5 * * * *"   # every hour at :05
  workflow_dispatch: {}

jobs:
  run:
    runs-on: ubuntu-latest
    permissions:
      contents: write
      issues: write
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install deps
        run: |
          pip install -r requirements.txt
          pip install great_expectations neo4j

      - name: Poll STAC with ETag
        env:
          STAC_API: ${{ secrets.STAC_API }}
        run: |
          python src/pipelines/stac/monitor-validate-publish/monitor.py

      - name: Validate (Great Expectations)
        run: |
          great_expectations checkpoint run stac_items \
            --config src/pipelines/stac/monitor-validate-publish/expectations/great_expectations.yml \
            --suite stac_item_suite

      - name: Publish + Graph
        env:
          NEO4J_URI: ${{ secrets.NEO4J_URI }}
          NEO4J_USER: ${{ secrets.NEO4J_USER }}
          NEO4J_PASS: ${{ secrets.NEO4J_PASS }}
        run: |
          python src/pipelines/stac/monitor-validate-publish/publish.py

      - name: Upload artifacts
        uses: actions/upload-artifact@v4
        with:
          name: stac-run-${{ github.run_id }}
          path: |
            data/stac/incoming/**/*.jsonl
            data/stac/published/**/*.json
            src/pipelines/stac/monitor-validate-publish/expectations/uncommitted/data_docs

      - name: Open issue on validation failure
        if: failure()
        uses: peter-evans/create-issue-from-file@v5
        with:
          title: "STAC validation failure in run ${{ github.run_id }}"
          content-file: data/stac/quarantine/last_failure_summary.md
          labels: pipeline, stac, validation


⸻

🔐 Secrets & Configuration
	•	STAC_API: Provider base URL.
	•	NEO4J_URI, NEO4J_USER, NEO4J_PASS: Graph store.
	•	Optional: HTTP_TIMEOUT, RETRY_COUNT, BATCH_LIMIT.

⸻

📈 Telemetry & Provenance
	•	Emit counters: polled_count, new_items, updated_items, quarantined_items, publish_latency_ms.
	•	Attach run metadata to telemetry_ref and store JSONL in data/stac/telemetry/.
	•	Include ingest hash over normalized Item for immutability audit.

⸻

🧰 Requirements (excerpt)

Add to requirements.txt:

requests>=2.32
great-expectations>=1.0
neo4j>=5.25
jsonschema
shapely
h3


⸻

🧪 Great Expectations: Minimal Check Examples
	•	Schema presence: id, geometry, properties.datetime, assets
	•	Ranges: properties.eo:cloud_cover in [0,100]
	•	Uniqueness: id unique per collection
	•	Links: links[?rel=="self"], links[?rel=="collection"] must exist

⸻

🧯 Failure Handling
	•	On GE failure: move batch to data/stac/quarantine/TS/, write last_failure_summary.md, auto‑open Issue with artifact link.
	•	On publish failure: retry with backoff; if repeated, open Issue + mark as blocked.

⸻

🧪 Local Dry‑Run

export STAC_API="https://example-stac.com"
python src/pipelines/stac/monitor-validate-publish/monitor.py
great_expectations checkpoint run stac_items \
  --config src/pipelines/stac/monitor-validate-publish/expectations/great_expectations.yml \
  --suite stac_item_suite
python src/pipelines/stac/monitor-validate-publish/publish.py


⸻

🧭 Governance & Compliance
	•	FAIR+CARE: metadata completeness, licensing, community impacts logged in provenance.
	•	Security: least‑privilege secrets; attest CI runs; record SBOM/manifest hashes.
	•	Accessibility: data docs exported with alt‑text & WCAG‑aware HTML.

⸻

📜 Badges
	•	✅ GE Checkpoint Gate • 🧪 CI Enforced • 🔒 Secrets Scanned • 🧭 FAIR+CARE Logged • 🧾 SBOM Linked

⸻

📚 References
	•	STAC API — Item Search 1.0.x (query, paging, intersects)
	•	HTTP ETag / If‑None‑Match (conditional requests)
	•	Great Expectations — Checkpoints & Validation Stores
	•	GitHub Actions — on.schedule cron, artifacts, issues

⸻

🗓️ Version History
	•	v10.3.0 (2025‑11‑14): Initial orchestrator spec (ETag polling, GE gate, upsert, GHA cron).

