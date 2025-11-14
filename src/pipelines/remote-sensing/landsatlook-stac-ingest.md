---
title: "🛰️ Kansas Frontier Matrix — LandsatLook STAC Ingestion & Neo4j Publishing (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/remote-sensing/landsatlook-stac-ingest.md"
version: "v10.3.1"
last_updated: "2025-11-14"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/pipelines-landsatlook-stac-v1.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
kfm_protocol: "Kansas Frontier Matrix — Markdown Output Protocol v10.3.0"
badges:
  - "FAIR+CARE ✅"
  - "SBOM ✅"
  - "CI: stac-validate.yml ✅"
  - "GeoSPARQL-aligned ✅"
related_specs:
  - "../../../schemas/stac/item.schema.json"
  - "../../../schemas/neo4j/spatial.graph.schema.json"
  - "../../../schemas/rdf/geosparql.context.jsonld"
---

<div align="center">

# 🛰️ **Kansas Frontier Matrix — LandsatLook STAC Ingestion & Neo4j Publishing**  
`src/pipelines/remote-sensing/landsatlook-stac-ingest.md`

**Purpose:**  
Continuously discover new **USGS LandsatLook** scenes intersecting **Kansas**, enrich them with AOI overlaps, generate concise AI tags/summaries, and publish to **Neo4j** with **GeoSPARQL**-aligned relationships and RDF exports.

</div>

---

## ✅ Scope & Outcomes

- Query **STAC Item Search** for new Landsat scenes over Kansas (time-windowed, cloud/collection filters).  
- Validate **STAC Item** structure; normalize assets & datetime, geometry, bbox.  
- Compute overlaps with Kansas **counties** and **priority AOIs**; store spatial attributes.  
- **AI describe** (1–2 sentences) + **classification tags** (e.g., `post-flood sediment plume`, `burn scar`, `crop stress`).  
- Upsert: `(:Scene {id})-[:INTERSECTS]->(:County)` with `POINT`/`POLYGON` attributes.  
- Export RDF aligned to **OGC GeoSPARQL** for linked-data pipelines.  

---

## 🔧 Configuration

~~~~~yaml
# src/pipelines/remote-sensing/landsatlook-stac-ingest.config.yaml
stac:
  endpoint: "https://landsatlook.usgs.gov/stac-server/search"
  collections: ["landsat-c2l2-sr", "landsat-c2l2-st"]
  datetime_lookback: "P14D"   # last 14 days
  limit: 200
  max_cloud_cover: 40
  intersects: "data/processed/aoi/kansas_boundary.geojson"  # single-part polygon

aoi:
  counties: "data/processed/admin/kansas_counties.gpkg#counties"
  priority_aoi: "data/processed/aoi/priority_aoi.gpkg#aoi"

ai:
  enable: true
  prompt_template: "docs/prompts/remote-sensing/scene-brief.v1.txt"
  max_tokens: 120
  tags_allowed:
    - burn_scar
    - sediment_plume
    - crop_stress
    - river_flood
    - drought_signal
    - snow_extent
    - urban_heat
    - irrigation_pattern

neo4j:
  uri: "bolt://localhost:7687"
  user: "neo4j"
  secret_ref: "secrets/neo4j.txt"
  spatial_srid: 4326
  index_labels: ["Scene", "County"]

rdf:
  enable: true
  out_dir: "data/processed/rdf/landsat/"
  context: "schemas/rdf/geosparql.context.jsonld"

ci:
  validators:
    - "stac-validate.yml"
    - "faircare-validate.yml"
    - "telemetry-export.yml"
telemetry:
  log_file: "data/processed/telemetry/landsat_ingest.ndjson"
~~~~~

---

## 🧭 Directory Layout

~~~~~text
src/pipelines/remote-sensing/
├─ landsatlook-stac-ingest.md
├─ landsatlook/
│  ├─ __init__.py
│  ├─ fetch.py            # STAC search & pagination
│  ├─ validate.py         # STAC Item validation
│  ├─ enrich.py           # AOI overlaps, footprint normalization
│  ├─ ai_describe.py      # 1–2 sentence summary + tags
│  ├─ publish_neo4j.py    # Cypher upserts, indexes, constraints
│  ├─ export_rdf.py       # GeoSPARQL-aligned JSON-LD/Turtle
│  └─ config.py
└─ configs/
   └── landsatlook-stac-ingest.config.yaml
~~~~~

---

## 🧩 STAC Item Search — Minimal Request

~~~~~json
{
  "collections": ["landsat-c2l2-sr"],
  "datetime": "2025-10-31T00:00:00Z/..",
  "limit": 200,
  "query": { "eo:cloud_cover": { "lte": 40 } },
  "intersects": { "type": "Polygon", "coordinates": "… kansas boundary …" }
}
~~~~~

Implementation notes:

- Use **POST** with pagination (`links[].rel == "next"`).  
- Deduplicate by `id` and asset checksum.  
- Persist raw responses to `data/stac/landsat/YYYY/MM/DD/*.json`.  

---

## 🧪 Validation & Normalization

- Enforce STAC 1.0+ fields: `id`, `type="Feature"`, `geometry`, `bbox`, `properties.datetime`, `assets`.  
- Normalize:

  - `properties.datetime` → ISO 8601 with trailing `Z`.  
  - `geometry` → single polygon (dissolve multiparts).  
  - `assets` → keep SR/ST, thumbnail, QA, MTL; attach `href`, `type`, `roles`.  

- Run `stac-validate` in CI and store results in telemetry.  

---

## 🗺️ AOI Overlaps

- Intersect scene footprint with:

  - County polygons → attach `county_fips`, `county_name`, `area_overlap_km2`, `percent_overlap`.  
  - `priority_aoi` (flood plains, burn areas, basins) → flag `priority_hits`.  

- Persist overlap metrics into Neo4j relationship properties on `[:INTERSECTS]`.  

---

## 🧠 AI Summaries & Tags (Optional)

Goal: **1–2 sentence** description + controlled tags.

Prompt sketch (stored at `docs/prompts/remote-sensing/scene-brief.v1.txt`):

- **Inputs:** date/time, collection, cloud %, bands available, overlap stats, recent hazards (if any).  
- **Output JSON:**  

  ~~~~~json
  {
    "summary": "...",
    "tags": ["burn_scar", "crop_stress"]
  }
  ~~~~~

- **Guardrails:** refuse PII; avoid speculation; reference observable spectral cues.

Store AI output under:

- `properties.kfm.ai.summary`  
- `properties.kfm.ai.tags`  

---

## 🧵 Neo4j Publishing (Cypher)

~~~~~text
// Ensure spatial indexes
CREATE INDEX IF NOT EXISTS FOR (s:Scene) ON (s.id);
CREATE INDEX IF NOT EXISTS FOR (c:County) ON (c.fips);

:param scene => $scene;  // map with id, datetime, cloud, wkt, centroid_lon, centroid_lat

MERGE (s:Scene {id: $scene.id})
  ON CREATE SET
    s.datetime    = datetime($scene.datetime),
    s.cloud       = $scene.cloud,
    s.collection  = $scene.collection,
    s.thumbnail   = $scene.thumbnail,
    s.geom_wkt    = $scene.wkt,
    s.centroid    = point({longitude: $scene.centroid_lon, latitude: $scene.centroid_lat, srid:4326}),
    s.created_at  = datetime()
  ON MATCH SET
    s.updated_at  = datetime();

UNWIND $scene.county_overlaps AS ov
MERGE (c:County {fips: ov.fips})
  ON CREATE SET c.name = ov.name
MERGE (s)-[r:INTERSECTS]->(c)
  ON CREATE SET
    r.percent_overlap = ov.percent,
    r.area_km2        = ov.area_km2
  ON MATCH SET
    r.percent_overlap = ov.percent,
    r.area_km2        = ov.area_km2;
~~~~~

---

## 🌐 RDF / GeoSPARQL Alignment

Mappings:

- `Scene` node → `geo:Feature`  
- Footprint WKT → `geo:hasGeometry` / `geo:asWKT`  
- `County` node → `geo:Feature`  
- `INTERSECTS` relationship → `geo:sfIntersects`  

Exports:

- JSON-LD using `@context: geosparql.context.jsonld`  
- Turtle files to `data/processed/rdf/landsat/`.  

---

## 🏃 Runbook (CLI)

~~~~~bash
# 1) Fetch latest scenes for Kansas
python -m landsatlook.fetch \
  --config configs/landsatlook-stac-ingest.config.yaml

# 2) Validate + normalize
python -m landsatlook.validate \
  --input data/stac/landsat/ \
  --fail-on-error

# 3) Enrich with AOI overlaps
python -m landsatlook.enrich \
  --counties data/processed/admin/kansas_counties.gpkg \
  --priority-aoi data/processed/aoi/priority_aoi.gpkg

# 4) Optional AI summaries
python -m landsatlook.ai_describe \
  --prompt docs/prompts/remote-sensing/scene-brief.v1.txt

# 5) Publish to Neo4j
python -m landsatlook.publish_neo4j \
  --neo4j secrets/neo4j.txt

# 6) Export RDF
python -m landsatlook.export_rdf \
  --out data/processed/rdf/landsat/
~~~~~

---

## 🧰 Implementation Notes

- Respect rate limits; backoff on HTTP `429`.  
- Cache collection → bands/roles mapping to keep prompts compact.  
- Maintain idempotency: hash `(id, updated)` pair to skip unchanged Items.  
- Emit telemetry at every step (`.ndjson`): durations, item counts, filtered counts, errors.  

---

## 🧯 QA & CI Gates

- `stac-validate.yml`: schema + required fields, asset roles.  
- `faircare-validate.yml`: AI prompt provenance, refusals captured, tags within allow-list.  
- `docs-lint.yml`: KFM Markdown Output Protocol compliance.  
- `telemetry-export.yml`: energy/CPU, carbon factors, success rates.  

---

## 📊 Example Telemetry (ndjson)

~~~~~text
{"ts":"2025-11-14T03:00:00Z","stage":"fetch","items":167,"filtered_cloud":42,"kept":125}
{"ts":"2025-11-14T03:01:10Z","stage":"validate","valid":125,"invalid":0}
{"ts":"2025-11-14T03:02:40Z","stage":"enrich","with_county":125,"priority_hits":18}
{"ts":"2025-11-14T03:03:10Z","stage":"ai","enabled":true,"summarized":125,"refused":0}
{"ts":"2025-11-14T03:03:35Z","stage":"publish","neo4j_nodes":125,"rels":310}
{"ts":"2025-11-14T03:04:00Z","stage":"rdf","files":125}
~~~~~

---

## 🧪 Minimal Python (Fetch Page)

~~~~~python
# src/pipelines/remote-sensing/landsatlook/fetch.py
import json
import pathlib
import datetime
import requests
from typing import Optional


EP = "https://landsatlook.usgs.gov/stac-server/search"


def iso_now() -> str:
    return datetime.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"


def search(payload: dict) -> dict:
    resp = requests.post(EP, json(payload), timeout=60)
    resp.raise_for_status()
    return resp.json()


def run(config: dict) -> None:
    out_dir = pathlib.Path("data/stac/landsat") / datetime.date.today().isoformat()
    out_dir.mkdir(parents=True, exist_ok=True)

    resp = search(config["stac_payload"])
    page = 1
    while True:
        (out_dir / f"items_{page:03d}.json").write_text(json.dumps(resp, indent=2))
        nxt = next((l for l in resp.get("links", []) if l.get("rel") == "next"), None)
        if not nxt:
            break
        more = requests.get(nxt["href"], timeout=60)
        more.raise_for_status()
        resp = more.json()
        page += 1


if __name__ == "__main__":
    # TODO: load YAML, build payload from config, call run()
    pass
~~~~~

---

## 🧱 Governance & Provenance

Pipelines MUST:

- Record source endpoint, request payload, response `links`, and `numberMatched`.  
- Capture AI prompt, model ID, temperature, and refusal logs per FAIR+CARE.  
- Maintain SBOM entries for Python dependencies; SLSA attestation for container images.  
- Log all governance decisions and CARE label changes to versioning and governance ledgers.  

---

## 🕰️ Version History

| Version  | Date       | Author | Summary |
|----------|------------|--------|---------|
| v10.3.1 | 2025-11-14 | Remote Sensing Team | Updated to KFM Markdown Protocol (tilde fences), aligned CI references and telemetry examples. |
| v10.3.0 | 2025-11-14 | Remote Sensing Team | Initial LandsatLook STAC → Neo4j pipeline spec; GeoSPARQL mapping; AI tagger; CI gates; RDF export. |