<div align="center">


🧾 Climate Derivative Checksums

data/derivatives/climate/checksums/

Purpose: provide reproducible, machine-verifiable integrity for climate derivative artifacts (COGs, GeoJSON, Parquet, CSV) produced by the ETL pipeline.

</div>



⸻

📚 Overview

This folder stores SHA-256 checksum manifests for climate derivative outputs under data/derivatives/climate/….
Checksums are used throughout KFM’s ETL → STAC → Knowledge Graph → API → Web UI stack to guarantee artifact integrity, enable cache-safe rebuilds, and document provenance as required by the project’s MCP standards. The architecture and Makefile-driven pipeline explicitly call out checksums as first-class build artifacts and validation gates.

⸻

🧭 When and where checksums are created

Mermaid (GitHub-safe) diagram of the checksum flow within the climate derivatives path:

flowchart TD
  A["Sources\nNOAA · Daymet · Normals"] --> B["ETL\nnormalize · reproject · derive"]
  B --> C["Climate Derivatives\nCOGs · GeoJSON · Parquet"]
  C --> D["Compute SHA-256\n*.sha256 files"]
  D --> E["STAC Items\nlink assets + checksum"]
  E --> F["Graph Load\nprovenance + asset refs"]
  F --> G["API & Web UI\nserve verified assets"]
  click E "_blank" "Indexed in data/stac/"
  click C "_blank" "data/derivatives/climate/"
%% END OF MERMAID

<!-- END OF MERMAID -->


KFM’s ETL/Makefile orchestrates standardized steps (fetch → process → checksums → STAC validate).

⸻

🗂 Directory layout

data/derivatives/climate/
├── # derived climate products (COGs, GeoJSON, Parquet, CSV)
└── checksums/
    ├── 1991_2020_normals_prcp_cog.tif.sha256
    ├── daymet_1980_2024_tmin_ks_cog.tif.sha256
    ├── drought_index_annual_ks.parquet.sha256
    ├── station_normals_points.geojson.sha256
    └── README.md  # this file

Scope: this folder tracks only .sha256 manifests; binaries live one level up in data/derivatives/climate/.

⸻

🧪 Algorithm & file format
	•	Algorithm: SHA-256 (hex digest)
	•	Format: single line: <HEX_DIGEST>  <FILENAME>
	•	Line endings: LF (\n)
	•	Relative pathing: hash is computed over the binary file as stored in data/derivatives/climate/ (not over symlinks).
	•	Why SHA-256? Modern, collision-resistant and widely available across toolchains (shasum, sha256sum, openssl dgst). KFM’s data architecture calls for checksums and metadata to ensure reproducibility and provenance across STAC and graph ingest.

⸻

🛠️ Generate & verify

Generate (from repo root)

# generate checksums for selected climate derivatives
cd data/derivatives/climate
for f in *.tif *.tif.cog *.parquet *.geojson *.csv; do
  [ -f "$f" ] || continue
  shasum -a 256 "$f" > "checksums/${f}.sha256"
done

Prefer shasum -a 256 (macOS) or sha256sum (GNU coreutils). Either yields a hex digest compatible with our CI verification.

Verify (from repo root)

cd data/derivatives/climate
# verify all checksums in the folder
for c in checksums/*.sha256; do
  base=$(basename "$c" .sha256)
  if command -v sha256sum >/dev/null 2>&1; then
    sha256sum -c "checksums/${base}.sha256"
  else
    # Portable check for macOS 'shasum'
    diff <(shasum -a 256 "$base" | awk '{print $1}') <(awk '{print $1}' "checksums/${base}.sha256")
  fi
done

Makefile target (convention)

KFM uses a Makefile-driven pipeline; checksum generation commonly occurs after processing and before STAC validation. You may expose a helper target such as:

checksums:
	@cd data/derivatives/climate && \
	for f in *.tif *.parquet *.geojson *.csv; do \
	  [ -f "$$f" ] || continue; \
	  shasum -a 256 "$$f" > "checksums/$$f.sha256"; \
	done

The KFM architecture documents the Makefile-orchestrated flow and integrity gates (checksums + STAC validation).

⸻

🔗 STAC integration (provenance)

Each climate derivative asset is described in STAC with:
	•	assets.<key>.href → relative path to the artifact
	•	assets.<key>.checksum:sha256 → hex digest (from this folder)
	•	properties['kfm:provenance'] → optional link to source ids in data/sources/ and the generating ETL task

Why: STAC metadata makes derivatives discoverable and verifiable in downstream tooling and the API/graph.

KFM treats STAC as the canonical catalog for processed layers; checksums are used as validation gates in CI/STAC workflows.

⸻

🧩 Knowledge Graph + API usage
	•	During graph load, we attach checksum_sha256 to asset nodes/edges to preserve evidential provenance and enable end-to-end validation.
	•	The API can expose a HEAD/GET metadata route to return the checksum for a requested asset, enabling client-side verification before display or analysis. (See KFM API/Frontend docs).

⸻

🧱 Naming conventions

Pattern	Example	Notes
<dataset>_<temporal>_<var>_ks_cog.tif.sha256	daymet_1980_2024_tmin_ks_cog.tif.sha256	Use inclusive year ranges; _ks for statewide coverage
<dataset>_<period>_<name>.parquet.sha256	drought_index_annual_ks.parquet.sha256	Parquet for tabular derivatives
<dataset>_<layer>.geojson.sha256	station_normals_points.geojson.sha256	Points/lines/polygons suffix helps readers
<dataset>_<period>_<var>.csv.sha256	normals_1991_2020_prcp.csv.sha256	For small CSV derivatives


⸻

✅ Policy
	1.	Every derivative file must have a matching .sha256 before it is considered “publishable” (ready for STAC/graph).
	2.	Never edit a checksum file by hand—recompute after any transformation.
	3.	CI will fail if a referenced asset’s digest does not match its .sha256 or STAC checksum:sha256. (See STAC validate workflow.)
	4.	Include checksum links in PRs affecting climate derivatives; reviewers verify locally or via CI logs.

⸻

🧪 Example: recompute after regeneration

# After updating a COG with a new overview pyramid:
gdaladdo -r average data/derivatives/climate/daymet_1980_2024_tmin_ks_cog.tif 2 4 8 16
shasum -a 256 data/derivatives/climate/daymet_1980_2024_tmin_ks_cog.tif \
  > data/derivatives/climate/checksums/daymet_1980_2024_tmin_ks_cog.tif.sha256


⸻

🔒 Reproducibility & MCP alignment
	•	Checksums are part of KFM’s reproducible ETL and open data posture. The data/file architecture and monorepo design emphasize provenance, versioning, and integrity across data/sources/, data/processed/, and data/stac/.
	•	Architecture docs show checksums in the canonical flow and integrity checks in CI.

⸻

🧱 Related docs
	•	Architecture (root): docs/ → KFM Architecture / Data Architecture / Monorepo
	•	Data architecture: rationale for data/sources, data/processed, data/stac and integrity gates.
	•	STAC catalog: data/stac/ items (ensure checksum:sha256)

⸻

🗓 Version history
	•	0.1.0 (2025-10-10): Initial checksum policy, naming, examples, and STAC integration.

⸻
