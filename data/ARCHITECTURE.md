<div align="center">


🗃️ Kansas Frontier Matrix — Data & Catalog Architecture

</div>



⸻

Overview: This document describes the data architecture of Kansas-Frontier-Matrix (KFM), following Master Coder Protocol (MCP) principles of documentation-first and reproducibility. It details how data is structured, processed through ETL pipelines, cataloged via STAC, and tracked for provenance. It is intended as a technical guide for maintainers and contributors to understand the data directories, standards, and workflows that ensure the project’s data is consistent, interoperable, and auditable.

📚 Table of Contents
	•	Directory Structure
	•	data/sources/
	•	data/raw/
	•	data/processed/
	•	data/stac/
	•	Data Processing Pipeline
	•	Spatial Catalog (STAC)
	•	Provenance & Reproducibility
	•	Open Formats & Interoperability Standards
	•	Tooling & Automation
	•	Contributing New Data

Directory Structure

In KFM, all data files and metadata reside under the data/ directory. Each subdirectory serves a distinct role in the data lifecycle, from source description to processed outputs and catalog metadata. The layout is as follows ￼:

data/
├─ sources/     # JSON manifests for datasets (external pointers + metadata)
├─ raw/         # downloaded source files (original artifacts; tracked via DVC/LFS)
├─ processed/   # derived datasets (COGs, GeoJSON, CSV, etc., ready for use)
└─ stac/        # STAC catalog (collections and items as JSON metadata)
``` [oai_citation:1‡GitHub](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/f9deb1eea7a0a02129183f945da69e6d7a1e12e5/README.md#L66-L69)

### data/sources/

This folder contains **source manifest files** (in JSON format) for each dataset. A manifest in `data/sources/` describes an external dataset and how to retrieve it, without storing the data itself. Each JSON file typically includes: 

- **Identifier and title:** A unique dataset ID (used in filenames and references) and a human-readable title or description.
- **Source URLs or API references:** Pointers to the actual data source (e.g. download URLs, API endpoints, or repository links).
- **Spatial extent (bbox):** The geographic bounding box of the data coverage.
- **Temporal range:** Date or range of dates the dataset pertains to (for time-aware integration).
- **Licensing and credits:** The usage license (e.g. public domain, CC-BY) and source attribution information.

These manifest files act as **catalog pointers** to external data, encapsulating what the data is and where it comes from [oai_citation:2‡GitHub](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/f9deb1eea7a0a02129183f945da69e6d7a1e12e5/README.md#L106-L108). The ETL pipeline reads these descriptors to **fetch the raw data** and transform it into standardized open formats. By keeping only pointers and metadata in Git (instead of bulky data files), the repository stays lean while enabling reproducible data ingestion.

### data/raw/

This directory stores the **raw artifacts** obtained from external sources (e.g. original raster files, shapefiles, CSV tables, scanned documents). After running the fetch step of the pipeline, the downloaded files are saved under `data/raw/` in a structured way (often organized by dataset or theme). 

**Versioning & storage:** Large files in `data/raw/` are not committed directly into Git history; instead, they are tracked via **Data Version Control (DVC)** or **Git LFS** as pointer files [oai_citation:3‡GitHub](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/f9deb1eea7a0a02129183f945da69e6d7a1e12e5/README.md#L170-L171). This means the repository holds lightweight references, and the actual binary data is stored in external storage or pulled on demand. Using DVC/LFS avoids bloating the repo while still maintaining a link to specific versions of the raw data (enabling reproducibility).

**Integrity checks:** For every raw file, an **SHA-256 checksum sidecar** file may be generated (e.g. `dataset.zip.sha256`). These checksums record the exact content hash of the source file at download time, serving as a provenance audit trail. If a source file changes upstream, the checksum mismatch will flag that the data has diverged, reinforcing data integrity (see [Provenance & Reproducibility](#provenance--reproducibility) below). The `make checksums` command in the pipeline automates generating/verifying these sidecar files [oai_citation:4‡GitHub](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/f9deb1eea7a0a02129183f945da69e6d7a1e12e5/README.md#L176-L179).

### data/processed/

The `processed` directory contains **derived data outputs** that result from running the ETL transformation steps on the raw sources. These are the files used directly by the application (and indexed in the catalog). Processed files are converted to **standard, interoperable formats** for efficient use and distribution:

- For **raster** datasets (e.g. elevation models, scanned maps), the pipeline produces **Cloud-Optimized GeoTIFFs (COGs)**. COG is an open GeoTIFF format optimized for streaming and web access, with internal tiling and overviews. All rasters are reprojected to a common spatial reference (WGS84 latitude/longitude, EPSG:4326) unless otherwise noted, to ensure consistency across the project. If source rasters are in legacy formats (e.g. MrSID, or different projections like NAD27), they are converted and reprojected using GDAL before being saved as COGs [oai_citation:5‡GitHub](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/f9deb1eea7a0a02129183f945da69e6d7a1e12e5/README.md#L106-L110).
- For **vector** datasets (points, lines, polygons) and tabular data, the pipeline outputs **GeoJSON** files (or CSV/Parquet for purely tabular data). GeoJSON is a widely compatible format for vector geospatial features. Like rasters, vector data is standardized to WGS84 coordinates. Attribute tables or time-series may be stored as CSV or Parquet if appropriate, but often still accompanied by a GeoJSON for spatial features.

All processed files are organized by thematic layers or dataset name within `data/processed/` (for example, raster layers might reside in a subfolder `processed/cogs/...` and vector layers in `processed/geojson/...`). These outputs are the **authoritative, cleaned datasets** that power the map and timeline. By using COG and GeoJSON, KFM ensures broad GIS compatibility and efficient web delivery [oai_citation:6‡GitHub](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/f9deb1eea7a0a02129183f945da69e6d7a1e12e5/README.md#L106-L108).

### data/stac/

This directory contains the **Spatial Temporal Asset Catalog (STAC)** for the project. STAC is a standardized JSON-based catalog system for geospatial assets. In `data/stac/`, every dataset layer is represented as a STAC **Collection or Item** (with associated asset metadata):

- A **STAC Collection** is a group of related Items (e.g. “Historic Maps” could be a collection grouping many map items). Collections provide high-level metadata (description, license, spatial/temporal extent covering all items in the collection).
- A **STAC Item** represents an individual dataset or asset with spatial extent. Each Item is a GeoJSON Feature-like JSON containing fields like an **id**, a geometry or bbox, a **datetime** (or time range) if applicable, and a list of **assets** (the actual files). 

In KFM’s static catalog, each processed data file has a corresponding STAC Item JSON describing it. The item’s `assets` section points to the file (using a relative path to the file under `data/processed/`) along with media type and other properties. For example, a historic map TIFF might have an Item with an asset entry like:

```json
{
  "type": "Feature",
  "id": "usgs_topo_larned_1894",
  "properties": {
    "datetime": "1894-01-01T00:00:00Z",
    "proj:epsg": 4326
  },
  "assets": {
    "cog": {
      "href": "data/processed/overlays/usgs_topo_larned_1894.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized"
    }
  },
  "bbox": [-99.4, 38.1, -99.0, 38.4]
}

(Example STAC Item for a 1894 USGS topographic map, showing the COG asset and its spatial/temporal metadata.)

The STAC catalog provides a machine-readable index of all data in KFM, including crucial metadata like spatial extent, time range, coordinate reference (EPSG code), license, and provenance. This makes data discovery and validation easier: one can query the catalog to find all assets covering a certain area and time, or verify that each dataset has proper metadata. The catalog is validated in CI to ensure compliance with the STAC specification ￼ ￼. It also links to source data provenance: for example, each STAC Item can include a link with rel="derived_from" pointing to the source URL or source Item, ensuring traceability of how a processed layer was derived. Overall, data/stac/ is the core index that ties together sources, raw data, processed outputs, and their metadata.

Data Processing Pipeline

The journey from data/sources to data/processed and data/stac is managed by a reproducible ETL pipeline, primarily orchestrated via the Makefile and Python scripts in src/pipelines/. The high-level flow is:

flowchart TD
    A["Manifest JSON<br/>(data/sources/*.json)"] -->|`make fetch`| B["Raw Data<br/>(data/raw/)"]
    B -->|`make cogs`/`make vectors`| C["Processed Data<br/>(data/processed/, COGs & GeoJSON)"]
    C -->|`make stac`| D["STAC Catalog<br/>(data/stac/*.json)"]
    B --> E["SHA-256 checksums<br/>(integrity sidecars)"]
    C --> E

Fetch – The process starts with make fetch, which reads each source manifest in data/sources/ and downloads the specified files into data/raw/. Custom download scripts or tools/ utilities may handle authentication, API pagination, or format-specific retrieval as needed. Each downloaded file is verified (e.g., via checksum or size) to ensure the fetch was successful.

Transform – Next, make cogs and/or make vectors (or a combined make data target) processes the raw data into the desired formats. This involves running Python ETL jobs (in src/pipelines/) for each dataset or data type. Typical transformations include:
	•	Converting raster images to COG (using GDAL or the rio-cogeo library) ￼, building internal overviews for multi-scale performance.
	•	Reprojecting data to WGS84 (if not already in lat/long) using GDAL or rasterio.
	•	For vector data, converting shapefiles or other formats to GeoJSON (using GDAL/OGR or Python libraries).
	•	Cleaning or standardizing attributes, and possibly deriving additional data (e.g. calculating hillshade from a DEM raster, or computing summary statistics).
	•	Ensuring filenames of outputs are clear and include identifiers (e.g., datasetid_year.ext for time-specific data).

Each ETL step is deterministic, meaning running it on the same input will produce the same output, which is important for reproducibility ￼. The Makefile targets sequence these steps and can be run all at once (make data performs fetch + process in one go).

Catalog – After data is processed, make stac generates or updates the STAC catalog entries in data/stac/. Using the PySTAC library ￼ and project-specific scripts, each dataset is turned into a STAC Item JSON (or grouped into Collections). The script populates metadata from the source manifest (title, description, license) and from the data itself (bbox, datetime, file size, checksum, etc.). The resulting STAC JSONs are saved in a structured manner (e.g., one JSON per dataset, possibly organized in subfolders by theme or collection). Finally, the catalog is validated against the STAC specification (e.g., using pystac.validate() or the STAC CLI) as part of continuous integration ￼, catching any schema or metadata errors early.

Throughout this pipeline, Makefile recipes and CI checks enforce a documentation-first, reproducible approach:
	•	Every step has logging and (where possible) JSON Schema validation (for example, validating the structure of source manifests or output metadata).
	•	The pipeline can be re-run at any time to rebuild the data from scratch, ensuring that the process is documented and automated rather than manual. This is vital for an open science project where data must be regenerated or updated in a controlled way.

Spatial Catalog (STAC)

The Spatial Temporal Asset Catalog is central to how KFM organizes and exposes its data. Purpose: The STAC catalog provides a unified, searchable index of all geospatial assets in the project. It enables both humans and machines to discover what data is available, the context of each dataset, and how to access it. By adhering to the STAC standard (v1.0.0) ￼, the project ensures compatibility with off-the-shelf tools (such as STAC browsers or clients) and future-proof integration with other catalogs.

Structure: In data/stac/, the STAC is typically organized with:
	•	A root Catalog or Catalog JSON that references all Collections (if using collections) or Items.
	•	One or more STAC Collection files (JSON) for grouping related Items. For instance, datasets of similar theme or source might be grouped (e.g., a “Climate Data” collection containing precipitation, temperature, etc. layers; a “Historical Maps” collection for all scanned maps). Each collection JSON includes metadata like extent (spatial and temporal bounds covering all items) and a summary of common properties.
	•	Numerous STAC Item JSONs, each representing a specific data resource (e.g., one historical map sheet, one county boundary layer, one year of climate data, etc.). The items include:
	•	Geometry/Bounding Box: the spatial footprint of the data.
	•	Datetime or Interval: the time frame the data represents (e.g., a single date for a historical map or a date range for a multi-year dataset).
	•	Properties: any additional metadata, such as attribution, license, keywords, or custom extensions (e.g., proj:epsg for projection, file:checksum for the data file’s hash, etc.).
	•	Assets: a dictionary of one or more assets that make up the dataset. Usually there is one primary asset (the data file, like a TIFF or GeoJSON) with a key (e.g., "cog" or "data"). The asset entry specifies the URL/path (href) to the file in data/processed/, the media type (e.g., image/tiff; application=geotiff; profile=cloud-optimized for a COG ￼, or application/geo+json for GeoJSON), and possibly a title or role.

Implementation: The KFM build scripts use PySTAC ￼ to programmatically create these catalog files. Many fields are populated directly from the source manifest (for consistency – e.g., the STAC Item description or license comes from the manifest’s metadata). The pipeline also attaches a provenance link in each Item: typically a link with rel="source" or rel="derived_from" that points back to the original source data or documentation. This means that anyone inspecting a STAC Item can trace back to where the data originated (e.g., a NOAA API endpoint or a USGS download page), reinforcing transparency.

Usage: The STAC catalog is used in multiple ways:
	•	The frontend application can load the catalog (or a processed summary of it) to dynamically populate layer lists, attributions, and to fetch data tiles. In fact, a build step converts the STAC into app configuration (like layers.json) so the React app knows what layers exist and how to render them ￼ ￼.
	•	Developers or external users can use STAC tools or simple HTTP requests to query the catalog. For example, one could search for all items in a date range or with a certain keyword. This makes the data programmatically accessible, aligning with open-data best practices.
	•	The STAC metadata also aids validation and consistency checks. The repository’s CI runs a “STAC Validate” workflow to ensure all entries conform to the spec ￼. This catches issues like missing fields or invalid geometries in the metadata.

In summary, data/stac/ is the metadata hub of KFM’s data: it ties together the raw source information, the processed file, and the descriptive metadata into a single standard structure for easy discovery and integration.

Provenance & Reproducibility

Ensuring trust in the data requires robust provenance tracking and reproducible processes. KFM is built with open science principles in mind – every dataset can be traced and every result can be reproduced. Key mechanisms include:
	•	Source Manifests with Metadata: As described, each data source is declared in a JSON file with fields like source URL, origin, and license. This functions as a provenance record, since it clearly states who/where the data comes from and under what terms. Contributors are expected to fill in these details for any new dataset (including citation of the original data provider).
	•	Checksum Sidecars (.sha256): For every important file (especially large raw data or key outputs), an SHA-256 checksum file is generated and stored. These hash files serve as tamper-evident seals – if someone re-downloads the data, they can verify the checksum to confirm it’s identical to the original version fetched. In CI or during data updates, these checksums can be verified to ensure no unintentional data corruption or upstream changes have occurred. This practice of attaching provenance sidecars is part of the MCP philosophy for data integrity ￼.
	•	Data Version Control: Large data files are managed with DVC/Git LFS, which not only prevents storing data directly in the repo, but also maintains version pointers. DVC can lock a dataset to a specific version or checksum and can even connect to remote storage (so others can dvc pull the exact same file versions). This means that historical versions of datasets can be retained or recreated, facilitating experiments and auditing. The combination of DVC and checksums ensures that the exact state of the data at any commit is known and retrievable ￼.
	•	Deterministic ETL & Scripts: The ETL pipeline is designed to be deterministic – given the same input data and code, it will produce the same outputs. No manual tweaking or random processes are involved without being captured in code or configuration. This is critical for reproducibility: others should be able to run make data and end up with the identical data/processed/ results. Randomized steps (e.g., sampling) are avoided or seeded when necessary. Additionally, the project uses schema validations (like STAC validation, and potentially JSON Schema for source manifests) in CI to catch anomalies ￼.
	•	Continuous Integration (CI) checks: The CI pipeline enforces the above. On every pull request or commit to the main branch, automated tests will run to validate STAC metadata compliance ￼, verify that checksums match the files, and run any unit tests on data processing code. This ensures that contributors cannot accidentally break the reproducibility or integrity of the data without it being noticed and fixed before merge.
	•	Documentation-first approach: In line with MCP, any significant data addition or change is expected to be accompanied by documentation. This could mean updating this architecture doc if the structure changes, adding a dataset README or metadata file, or noting assumptions in a docs/ entry. By documenting before or alongside coding, provenance and rationale are recorded. Every PR is required to include relevant updates to docs and metadata ￼, which keeps knowledge about the data up-to-date and reviewable.

Through these measures, KFM ensures that from raw data acquisition to processed layer publication, every step is traceable and repeatable. If an issue or question arises (e.g., “Where did this layer’s data come from?” or “How was this raster generated?”), one can find the answers in the source manifests, STAC entries, and associated documentation, with cryptographic hashes and version control confirming the lineage.

Open Formats & Interoperability Standards

The project embraces open data formats and standards to maximize interoperability:
	•	GeoTIFF / COG for rasters and GeoJSON for vectors have been chosen as the primary output formats ￼. These formats are widely supported in GIS software, web mapping libraries, and data science tools. In particular, Cloud-Optimized GeoTIFFs (an extension of GeoTIFF) enable efficient use in cloud and web contexts by allowing partial reads (important for large images). GeoJSON, being JSON-based, is easy to integrate with web applications and is human-readable.
	•	CSV/Parquet are used for tabular data (e.g., time series from weather stations) when spatial geometry is not needed or as a complement to GeoJSON for attribute-heavy data. Parquet provides efficient columnar storage which is useful for large time-series.
	•	STAC (SpatioTemporal Asset Catalog): As detailed, STAC provides a standard for cataloging the data. It inherently supports linking to standard metadata like DCAT.
	•	DCAT and JSON-LD: While the STAC catalog itself is in JSON, it can be augmented or cross-walked to DCAT (Data Catalog Vocabulary) for broader interoperability ￼. DCAT is a W3C standard used by many open data portals to describe datasets in a catalog (often in RDF or JSON-LD). KFM’s catalog could be extended with JSON-LD context to make the STAC records interpretable as DCAT entries, allowing integration with semantic web tools or data catalogs. In practical terms, this means KFM’s metadata can be mapped to concepts like Dataset, Distribution, etc., enabling, for example, a library or state data portal to ingest KFM’s catalog easily.
	•	Semantic Ontologies: Beyond file formats, KFM leverages ontologies (like CIDOC-CRM for cultural heritage, OWL-Time for temporal information) in the knowledge graph. While this is more about the graph database, it underscores a commitment to semantic interoperability – the idea that data concepts are well-defined and linkable. On the file side, using JSON-LD to tag certain fields (like linking a license URL to a standard definition, or tagging keywords with ontology references) could further enhance machine-readability of the catalog.
	•	Descriptive Metadata Standards: Within STAC Items, fields like license, keywords, provider are used consistently. Each STAC Item includes a reference to the dataset’s license, so users know the terms (e.g., CC-BY 4.0) ￼. The use of common vocabularies for places or times (when applicable) also improves interoperability (for instance, aligning dates to ISO 8601, and place names to known gazetteers if mentioned).

By adhering to these formats and standards, KFM ensures that its data can be easily shared, indexed, and used alongside other datasets. A researcher could, for example, combine KFM’s STAC catalog with another STAC catalog, or import KFM GeoJSON files into QGIS or a Python notebook with minimal friction. The data and metadata are self-descriptive and packaged in a way that doesn’t require proprietary software to interpret.

Tooling & Automation

The data stack relies on a variety of tools to automate processing and maintain quality:
	•	Makefile Pipelines: A top-level Makefile orchestrates common tasks like make fetch, make cogs, make stac, and make checksums. This provides a simple interface for contributors to run the entire pipeline or specific steps. Make’s dependency rules also help in partial rebuilds – e.g., if only one source manifest changed, the fetch or processing for that dataset can be run without reprocessing everything.
	•	Python & GDAL: The heavy lifting of data conversion is done via Python scripts (in src/pipelines/) that often use GDAL (Geospatial Data Abstraction Library) or high-level wrappers like rasterio. GDAL is the Swiss-army knife for geospatial data, enabling format conversion, reprojection, tiling, etc. The project uses GDAL both directly (command-line or via subprocess calls for tasks like warping projection) and indirectly via libraries:
	•	rasterio: a Python library for raster data built on GDAL, used to read/write GeoTIFFs and manipulate raster data in arrays.
	•	rio-cogeo: a specialized plugin/tool to create COGs (Cloud Optimized GeoTIFFs) easily ￼. It handles generating internal overviews and proper metadata tags for COG.
	•	Fiona/OGR: likely used for vector format translations (reading shapefiles, writing GeoJSON, etc.).
	•	PySTAC: Used to create and manipulate STAC catalog JSONs in Python ￼. This library ensures that the STAC files conform to the spec and simplifies adding standard fields (like automatically computing bbox from geometries, etc.).
	•	GeoJSON & JSON Schema libraries: The pipeline may use JSON validation libraries to enforce schema on the source manifests and output metadata. For instance, a JSON Schema could define required fields in sources/*.json (id, title, license, etc.), and a validation step can catch if a contributor forgot to include something. The STAC validation largely covers the output side.
	•	DVC (Data Version Control): DVC commands are used to manage the state of data. For example, dvc pull/push might be part of the bootstrap process (as indicated by make bootstrap in the quickstart) to retrieve data artifacts. DVC also generates human-readable .dvc files that map a data file to a hash in remote storage, which are stored in Git to keep track of data versions. This way, even if data/raw/largefile.tif is not in Git, a data/raw/largefile.tif.dvc file is, containing the hash and remote location.
	•	Pre-commit Hooks & CI: Tools like pre-commit run linters and formatters on JSON and code to maintain consistency. In particular, JSON and Markdown might be formatted or linted to ensure readability. CI workflows (GitHub Actions) run STAC validation, pytest for any data processing functions, and CodeQL/Trivy scans (as seen by badges) to ensure security and code quality ￼.
	•	Utilities in tools/: The repository’s tools/ directory likely contains one-off scripts for tasks that are not pure ETL but needed for data prep. Examples could include georeferencing tools (e.g., if a historic map needs control points and warp, a script might assist with that), importers for specific APIs (like a script to page through NOAA’s API to get all storm events), or converters for odd formats. These tools complement the main pipeline.

By leveraging these tools, the project achieves a high level of automation. A new developer can run a single make data command and behind the scenes all the above tools coordinate to produce final data and metadata ￼ ￼. This reduces human error and saves time, while the use of familiar open-source tools makes the process transparent and modifiable.

Contributing New Data

Adding a new dataset to the Kansas Frontier Matrix follows a documented, step-by-step process to ensure consistency and completeness. Whether you’re an internal team member or an external contributor, you should adhere to these best practices:
	1.	Plan & Document the Data Source: Before adding any files, create a source manifest in data/sources/. Copy the JSON template from an existing entry and fill in all required metadata fields. At minimum, include:
	•	id: a short unique identifier (used in filenames, STAC ids, etc., e.g. "noaa_storms").
	•	title and/or description: a clear human-friendly name for the dataset.
	•	urls or source: the download link(s) or API endpoint for the data. If multiple files (e.g., one per year), list them or indicate a pattern.
	•	temporal coverage: the date or date range the data represents (e.g., "start": "1950-01-01", "end": "2020-12-31" or a single date for a snapshot).
	•	bbox: the bounding box of the data (in WGS84 lat/long coordinates).
	•	license: the license of the source data (and include a provider or citation if appropriate).
Ensure the manifest is saved as <id>.json. This manifest will serve as the authoritative reference for provenance and metadata ￼.
	2.	Fetch the Data via the Pipeline: Run the ETL pipeline to retrieve and process the data. Typically:
	•	Execute make fetch to download the raw files into data/raw/ (the pipeline uses your new JSON manifest to know what to get). Confirm that the files land in a logical subdirectory (the fetch scripts usually organize by dataset).
	•	If the data needs custom processing not already in the pipeline, you may need to add a Python script in src/pipelines/ or adjust the Makefile. For many standard formats (GeoTIFFs, shapefiles, etc.), generic rules may handle them. If writing a new pipeline script, follow existing examples and document any novel steps.
	•	Run make cogs (for raster data) and/or make vectors (for vector data) to perform format conversion. This will generate COGs or GeoJSONs in data/processed/. Ensure that rasters are reprojected to EPSG:4326 and vectors use WGS84 coordinates ￼. Check the output files: do they look correct in GIS software? Are attributes preserved? Iterate as needed.
	•	Run make stac to generate a STAC Item for your dataset. This will create a new JSON in data/stac/ describing your layer. Open it and verify that fields like title, description, time, and license are properly populated (the script pulls from your source manifest). Also verify the asset href points to the correct processed file, and that bbox and other properties are correct.
	3.	Verify Provenance & Integrity: After processing:
	•	Run make checksums to produce SHA-256 checksum files for the new raw and processed files. This will create .sha256 files alongside the data files. Commit those to version control along with your other changes. These checksums ensure others can verify the data’s integrity ￼.
	•	Double-check that your source manifest JSON includes all necessary metadata (especially license and source URL). This is important for transparency and for populating STAC. If the source data came with its own metadata or README, consider adding a reference or copying important notes into a comment in the JSON or a separate README in data/sources/ for that dataset.
	•	Ensure that large files are handled via DVC or LFS. If you added a new large file and it’s appearing in git status as an untracked file, you may need to run dvc add or move it to LFS. The repository should not directly contain the binary content of large datasets.
	4.	Integrate with the Application (if applicable): To make the new layer appear in the frontend map interface, you likely need to update the configuration:
	•	Add an entry in web/config/layers.json (or equivalent config) referencing the new STAC Item or dataset. This usually includes a layer name, a display style (color, opacity), and the temporal attribute (for the timeline) if any. Use existing layers as a guide for the schema. This step ties the data into the UI (so the user can toggle it on/off, see it on the timeline, etc.).
	•	If the dataset contains time information (e.g., a historical map from 1894, or a climate record spanning years), make sure the time metadata is correctly set in the STAC (the datetime or interval) so that the timeline slider can pick it up. For example, for a historical map, set the Item’s datetime to the map’s year ￼. For a multi-year dataset, use the interval start and end. This will ensure the layer is only visible in the appropriate time range on the timeline.
	•	Add any legends or descriptive text needed for the layer (some projects maintain a separate legend file or you might include it in layers.json).
	5.	Testing and Documentation: Before submitting your contribution:
	•	Re-run make stac-validate (or the full CI test suite if possible) to ensure your new STAC entries pass validation. Fix any errors (common ones might be missing fields or invalid geometry in bbox).
	•	View the site locally (run docker compose up and make serve-web) to see that the layer appears and data loads correctly on the map.
	•	Update documentation: If your dataset is significant, consider adding a note in the docs/data-resources.md index or a short README in data/sources/ describing the dataset and its origin. All contributions should include provenance info and methodology as per MCP ￼.
	•	Ensure that your commit/PR includes all relevant files: the new JSON manifest, any new script, updated config, and data pointers/checksums. Follow the repository’s style (format JSON with 2 spaces, etc.) and naming conventions.

By following these best practices, you help maintain the project’s high standards for data quality, transparency, and reproducibility. KFM’s maintainers will review the PR for completeness, check that the data is appropriately licensed and attributed, and verify that CI passes (including STAC validation and checksums) before merging. This process ensures that each new layer added to the Kansas Frontier Matrix enriches the atlas while upholding the principles of open, reliable data.

Contributor tip: Focus on metadata and documentation as much as on the data itself. A well-documented dataset (with clear source info, description, and usage notes) is far more valuable. The goal is that a future user can read the STAC Item or source manifest and instantly understand what the data is, where it’s from, and any caveats. This makes the KFM a truly living, trustworthy atlas of Kansas’s spatiotemporal data.

Sources:
	1.	Kansas Frontier Matrix repository README – data directory structure and formats ￼ ￼
	2.	Kansas Frontier Matrix Architecture documentation – reproducibility, provenance, and open standards ￼ ￼
	3.	Kansas Frontier Matrix src/README.md – core tools and technologies (GDAL, rio-cogeo, PySTAC) used in the data pipeline ￼
	4.	Kansas Frontier Matrix Architecture documentation – guidelines for adding new datasets (manifest fields, conversion, WGS84 projection) ￼
	5.	Kansas Frontier Matrix repository README – build pipeline commands and contribution guidelines (checksums, STAC validation, metadata requirements) ￼ ￼
