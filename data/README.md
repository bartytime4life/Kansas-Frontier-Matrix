
<div align="center">


📂 Kansas-Frontier-Matrix — data/

Mission: keep inputs immutable, artifacts reproducible, catalogs discoverable, and knowledge auditable.
This directory implements the project’s MCP-style data lifecycle, feeding both the STAC catalog and the Neo4j knowledge graph.

</div>



⸻

Contents
	•	Philosophy
	•	Directory Layout
	•	Git & LFS Policy
	•	Lifecycle & Make Targets
	•	Naming Conventions
	•	Source Descriptor Schema
	•	Provenance & Checksums
	•	STAC Guidance
	•	Knowledge Graph Integration
	•	Uncertainty & Confidence
	•	QA & Validation
	•	Quickstart
	•	Gotchas
	•	TL;DR

⸻

Philosophy
	•	Raw is immutable. Nothing hand-edited; all edits live in *_meta.json sidecars.
	•	Processing is reproducible. Scripts + configs recreate every artifact.
	•	Catalogs are first-class. Every asset lands in STAC 1.0.0.
	•	Graph is connective tissue. Every entity/event is linked into the Neo4j knowledge graph ￼ ￼.
	•	Uncertainty is explicit. Confidence scores & provenance are stored alongside data ￼ ￼.

⸻

Directory Layout

data/
├─ 📥 raw/             # Immutable payloads (never edit)
│  └─ *_src.json       # Provenance sidecars
│
├─ 📝 sources/         # Curated descriptors (JSON/YAML, validated)
│  └─ schema.source.json
│
├─ 🛠 work/            # Scratch staging (ignored in git)
├─ 🧹 tmp/             # Ephemeral build (cleared in CI)
│
├─ 📊 processed/       # Analysis-ready products
│  ├─ vectors/*.geojson
│  ├─ rasters/*.tif
│  └─ _meta.json
│
├─ 🛰 cogs/            # Canonical Cloud-Optimized GeoTIFFs
├─ 🔬 derivatives/     # Higher-order blends & indices
│
├─ 📂 stac/            # STAC catalog (collections + items)
│
├─ 🗺 tiles/            # Web tiles (PNG/PMTiles, ignored)
└─ 📖 provenance/      # Registry of checksums & experiment logs

Rule: each derivation emits _meta.json and .sha256.

⸻

Git & LFS Policy

.gitignore
	•	Ignore processed/**, cogs/**, derivatives/**, work/**, tmp/**, tiles/**.
	•	Commit only: *_meta.json, .sha256, curated descriptors, small docs.

.gitattributes
	•	Route heavy binaries to LFS (*.tif, *.gpkg, *.laz, etc.).
	•	Keep diff-friendly text (JSON, GeoJSON, CSV, YAML) in normal Git.

⸻

Lifecycle & Make Targets

flowchart TD
  S["Define Source<br/>(data/sources/*.json)"] --> F["Fetch<br/>make fetch"]
  F --> P1["Vectors<br/>make vectors"]
  F --> P2["Rasters → COGs<br/>make cogs"]
  P2 --> T["Terrain Derivatives<br/>make terrain"]
  P1 --> D["Derivatives<br/>make derivatives"]
  P2 --> D
  D --> C["STAC Build<br/>make stac"]
  C --> V["Validation<br/>make validate-*"]
  C --> X["Exports<br/>make kml / make site"]

<!-- END OF MERMAID -->



⸻

Naming Conventions
	•	processed/vectors/<layer>_<period>.geojson → hydrography_1936.geojson
	•	processed/dem/<id>.tif → ks_1m_dem_2018.tif
	•	cogs/<id>.tif → canonical COGs
	•	stac/items/<collection>/<id>.json → STAC items
	•	Periods: {YYYY | YYYY-YYYY | 1930s | late-19c} (lowercase, hyphenated)

⸻

Source Descriptor Schema

All sources validate against sources/schema.source.json.

{
  "required": ["id","title","type","license","provenance","retrieved"],
  "properties": {
    "id": {"type":"string","pattern":"^[a-z0-9_\\-]+$"},
    "title": {"type":"string"},
    "type": {"enum":["vector","raster","collection","service","document"]},
    "period": {"type":"string"},
    "bbox": {"type":"array","minItems":4,"maxItems":4},
    "urls": {"type":"array","items":{"type":"string","format":"uri"}},
    "license": {"type":"object"},
    "provenance": {"type":"object"},
    "retrieved": {"type":"string","format":"date-time"},
    "confidence": {"type":"number","minimum":0,"maximum":1}
  }
}


⸻

Provenance & Checksums

Each directory should include:
	•	*_meta.json → command, inputs, outputs, CRS, bbox, stats, versions
	•	*.sha256 → one per binary artifact

⸻

STAC Guidance
	•	Collections: group by domain (terrain, hydrology, treaties, maps).
	•	Items: concrete datasets (e.g., hydrography_1936).
	•	Each item must include: geometry, bbox, datetime, ≥1 asset, roles (data, visual), checksum, license, links.
	•	Use STAC Validator in CI ￼.

⸻

Knowledge Graph Integration

Every processed entity flows into Neo4j:
	•	Nodes: Person, Place, Event, Document ￼
	•	Edges: OCCURRED_AT, MENTIONS, PARTICIPATED_IN ￼
	•	Properties: datetime (OWL-Time), confidence, provenance ￼
	•	Ties directly to timeline + map UI.

⸻

Uncertainty & Confidence
	•	Confidence scores (0–1) on every extraction ￼.
	•	Ambiguous geocodes flagged with confidence < 0.5.
	•	Visualization: low confidence = lighter opacity.

⸻

QA & Validation
	•	make validate-sources → JSON Schema
	•	make validate-vectors → CRS/topology
	•	make validate-cogs → COG structure
	•	make stac-validate → STAC compliance
	•	make checksums → refresh SHA-256

CI runs full suite on PRs.

⸻

Quickstart

# 1. Add a new source descriptor
$ $EDITOR data/sources/ks_hydrography_1936.json

# 2. Fetch & process
$ make fetch vectors stac

# 3. Validate
$ make validate-sources validate-vectors checksums

# 4. Explore
$ open data/processed/vectors/hydrography_1936.geojson
$ open data/stac/items/vectors/hydrography_1936.json


⸻

Gotchas
	•	Shapefiles are brittle → prefer GeoPackage / FlatGeobuf.
	•	Always reproject to EPSG:4326 unless documented otherwise.
	•	Commit _meta.json + .sha256 together.
	•	Never commit intermediates (work/, tmp/).

⸻

TL;DR
	•	Immutable raw in raw/
	•	Curated descriptors in sources/
	•	Reproducible outputs in processed/, cogs/, derivatives/
	•	Discoverable metadata in stac/
	•	Connected graph in Neo4j
	•	Provenance + confidence tracked everywhere

⸻
