Root Architecture Overview for Kansas Frontier Matrix

Kansas Frontier Matrix Architecture

Kansas Frontier Matrix is a multi-disciplinary, open-source spatiotemporal knowledge hub for Kansas history, integrating geography, climate, culture, and events into a unified platform
GitHub
. This document outlines the system’s purpose, design, and component architecture for contributors, developers, and researchers.

📚 Contents

Purpose and Mission

Architecture Overview

Data Ingestion (ETL)

AI/ML Enrichment

Knowledge Graph

API Layer

Frontend Application

Reproducibility & Observability

Open Science & Semantic Interoperability

Extending and Adding New Data

🚀 Purpose and Mission

Kansas’s history has long been fragmented across treaties, disasters, railroads, floods, climate data, and oral histories scattered in different archives
GitHub
. The mission of this project is to rebuild that story into a time-aware atlas and knowledge graph, linking disparate data and narratives into one interactive, layered resource. By combining spatial (map-based) and temporal (timeline-based) context, the system enables researchers and the public to explore how terrain, climate, culture, and events intersect across centuries. The platform is designed as an open-source project to encourage collaboration and knowledge sharing, and as a multidisciplinary hub that brings together GIS, history, climatology, archaeology, and more under a common framework.

🏗 Architecture Overview

The Kansas Frontier Matrix architecture is organized into several layers, from data ingestion to end-user presentation. Figure 1 (below) illustrates the full stack and data flow across these layers. In essence, the system ingests and processes raw historical datasets, enriches them with AI/ML, indexes them in a spatiotemporal catalog, integrates them into a semantic knowledge graph, and delivers them through an API and interactive frontend. Each layer is described in detail in subsequent sections.

flowchart TD
    A["Sources\nscans · rasters · vectors · documents"] --> B["ETL Pipeline\nMakefile · Python · checksums"]
    B --> C["Processed Layers\nraster COGs · GeoJSON"]
    B --> I["AI/ML Enrichment\nNER · geocoding · linking"]
    C --> D["STAC Catalog\ncollections · items · assets"]
    D --> E["Config Build\napp.config.json · layers.json"]
    D --> H["Knowledge Graph\nNeo4j · CIDOC CRM · OWL-Time"]
    I --> H
    H --> J["API Layer\nFastAPI · GraphQL"]
    D --> J
    J --> F["Frontend (React + MapLibreGL)\ntimeline · search · filters"]
    E --> F
    E --> G["Google Earth Exports\nKML · KMZ"]


Figure 1: End-to-end architecture flow. Raw Sources (scanned maps, rasters, GIS vectors, documents, etc.) are processed by an ETL Pipeline (via Makefiles and Python scripts with data integrity checksums) to produce standardized Processed Layers (e.g. cloud-optimized GeoTIFFs and GeoJSON files). These are indexed in a STAC Catalog (spatiotemporal asset catalog) which in turn feeds a Config Build for the web app and populates the Knowledge Graph. An AI/ML enrichment pipeline runs in parallel to extract entities and links from unstructured data (feeding into the Knowledge Graph). A dedicated API Layer (FastAPI/GraphQL) provides programmatic access to both the catalog and knowledge graph. Finally, the Frontend React application (with MapLibre GL for mapping) presents an interactive timeline and map UI to end users, and also supports search and filtering. Ancillary outputs like Google Earth exports (KML/KMZ files) are also generated for 3D visualization.

📥 Data Ingestion (ETL)

Data ingestion is handled by an ETL (Extract, Transform, Load) pipeline that consolidates diverse source materials into a common repository. Sources include historical maps and scans, geospatial raster data (e.g. DEMs, climate grids), vector GIS data (e.g. boundaries, trails), tabular datasets, and textual documents. These raw inputs may come from external APIs and open data portals (e.g. USGS, NOAA, state archives) or from digitized files. Each data source is documented with metadata (format, source URL, license, etc.) in the data/sources/ directory for transparency and provenance.

 

The ETL process is orchestrated by a Makefile and implemented in Python scripts
GitHub
. The Makefile defines tasks for fetching data, converting formats, and building outputs (for example, make fetch, make cogs, make terrain, make stac, etc. as referenced in the README
GitHub
). Using Makefile ensures a reproducible order of execution and easy one-command rebuilds of the entire dataset. The pipeline performs transformations such as reprojecting coordinates to a common spatial reference, converting raster data into Cloud-Optimized GeoTIFFs (COGs), vector data into GeoJSON (or other standardized formats), and extracting text or tabular data as needed
GitHub
. Data integrity is safeguarded by verifying SHA-256 checksums of source files and generated artifacts
GitHub
. This guarantees that data hasn’t been corrupted or altered unexpectedly and allows caching of results when inputs haven’t changed.

 

During ingestion, the pipeline also applies validation checks. Every dataset’s metadata is validated against JSON Schemas and the STAC specification to ensure compliance
GitHub
. This validation step (integrated into continuous integration) catches issues like missing fields or incorrect geospatial/temporal metadata early in the process. By the end of the ETL stage, we have a collection of cleaned and standardized data layers, each with accompanying metadata ready to be indexed.

🤖 AI/ML Enrichment

The AI/ML enrichment layer augments the raw datasets with additional semantic information. This involves applying natural language processing and machine learning techniques to extract entities, relationships, and insights from unstructured or semi-structured data. For example, historical documents or narrative texts are processed with Named Entity Recognition (NER) to identify mentions of people, places, organizations, and events. Identified place names are then geocoded – i.e. matched to geographic coordinates (often by linking to known gazetteers or using services like Google Maps API or Geonames). Person names might be linked to authority records or Wikidata entries for consistency. Documents can also be summarized using NLP summarization to distill key points (useful for creating concise descriptions in the user interface).

 

Another enrichment task is entity linking, where extracted entities (from text or from disparate datasets) are connected to each other or to canonical identifiers. For instance, an oral history transcript mentioning “Fort Larned” can be linked to the Fort Larned location entity in the knowledge graph, and a date like “August 1867” can be linked to a timeline interval. The enrichment pipeline may use pre-trained language models or custom models to perform these tasks. It generates outputs such as annotated text, lists of entity links, or additional attributes (e.g. tagging a historical photo with the names of people it depicts). These enriched outputs are then fed into the Knowledge Graph layer to become part of the structured knowledge network (e.g. new nodes for previously unknown entities, or new relationships between existing nodes). In addition, enrichment results can improve the frontend experience – for example, enabling a free-text search index, or providing content for map popups and story panels (like dynamically generated summaries or definitions when a user clicks on an item).

 

Overall, the AI/ML enrichment layer bridges the gap between raw data and meaningful knowledge, ensuring that hidden connections in narratives and data are exposed and formally represented in the system.

🧩 Knowledge Graph

The Knowledge Graph is a central component that semantically interconnects the people, places, events, and artifacts in the Kansas Frontier Matrix. Implemented in a graph database (Neo4j), it encodes a network of entities and their relationships, allowing complex queries and inferences. The design of the knowledge graph follows the CIDOC CRM ontology – a conceptual reference model from the cultural heritage domain that provides an extensible semantic framework for integrating information
cidoc-crm.org
. By mapping our data to CIDOC CRM classes and properties, we ensure that historical events (e.g. a treaty signing, a battle, a flood) are represented as CRM events linked to related actors (people or organizations), places (geographic locations), and dates/time periods.

 

Temporal information in the graph is modeled using standards like OWL-Time, the W3C’s ontology for temporal concepts
w3.org
. This allows events and entities in the graph to have well-defined dates or date ranges (e.g. an event node might have a time:hasBeginning and time:hasEnd corresponding to its start and end dates), supporting timeline queries and reasoning about historical intervals. Spatial entities (places, regions) are linked to geospatial coordinates or boundary definitions, often via external gazetteers.

 

The knowledge graph also captures provenance and source citations for each piece of data. For example, a fact that “X happened in 1854 at location Y” would be tied to a source document or dataset in the graph, ensuring traceability. Each dataset from the STAC catalog can also be represented in the graph (with nodes for datasets, and edges indicating what real-world entities or phenomena they describe). This dual link – between the geospatial/time-indexed data and the semantic knowledge – is powerful. It means users can ask questions like “show me all events related to indigenous treaties within 50 miles of this river during the 1860s” and get answers by traversing the graph relationships.

 

Data from the AI/ML enrichment pipeline is ingested into the graph as well. For instance, if NER finds a person’s name in a document, a node for that person is added (or linked to an existing node if already known), and a relationship is created between the document (as a graph node) and that person (e.g. “Person X is mentioned in Document Y”). The result is an increasingly rich knowledge network that complements the raw data layers.

 

To maintain semantic interoperability, the graph not only uses CIDOC CRM and OWL-Time, but also aligns with other ontologies when appropriate. Notably, historical periods are standardized using the PeriodO period gazetteer (a Linked Open Data resource of named historical period definitions
perio.do
). This means if a dataset uses terms like “Dust Bowl era” or “Civil War period,” those can be linked to a formal PeriodO definition, giving them clear date ranges and references. By adhering to these established ontologies and vocabularies, the knowledge graph can easily interoperate with other Linked Data and knowledge graph initiatives in the open history and cultural heritage community.

🔌 API Layer

The API layer provides programmatic access to the data and knowledge contained in Kansas Frontier Matrix. It serves as an intermediary between the backend (STAC catalog + knowledge graph) and client applications (including our own frontend). The project uses a modern web service stack: FastAPI (a high-performance Python web framework) to build RESTful endpoints, and a GraphQL interface for flexible, query-based retrieval. Through the API, external applications or analyses can query the system for information without needing direct access to the raw files or database.

 

Key capabilities of the API include:

Data access endpoints (REST): These allow retrieval of geospatial data or metadata by key, such as fetching a particular raster file, vector layer, or STAC item JSON. For example, a GET request might return the GeoJSON for a specific county’s boundary, or a list of available datasets in a certain date range.

Knowledge graph queries (GraphQL): The GraphQL API provides a unified schema to query the graph of people, places, events, etc. Clients can ask complex questions in a single query (e.g. get all events of type “battle” with their locations and participating parties, or fetch all places that were part of a certain treaty agreement). The GraphQL layer is likely powered by Neo4j’s GraphQL integration or custom resolvers that translate queries to graph database lookups. This abstraction lets clients obtain exactly the fields they need in a convenient JSON structure.

Integrated queries: Because the API layer straddles both the STAC catalog and the knowledge graph, it can support queries that join both worlds. For instance, an API call could filter data items by semantic tags (e.g. find all datasets related to “wildfire” events in the 1930s). Under the hood, the API might first query the knowledge graph for relevant event IDs, then return links to corresponding data layers in the catalog.

The API is designed with standard web protocols, making it easy to build third-party tools or integrate the Kansas Frontier Matrix with other systems. For example, a researcher could use the API to pull data into a Jupyter notebook for analysis, or a public website could query the API to show a timeline of Kansas historical events. Authentication and rate limiting (if needed for public usage) would be handled at this layer, though within this open science project most data will likely be public. The API layer also facilitates the frontend by offloading heavy query logic – the React app can call lightweight endpoints or GraphQL queries, rather than downloading large datasets or doing client-side filtering exclusively. This keeps the frontend efficient and responsive.

🖥️ Frontend Application

The frontend is an interactive single-page application (SPA) that allows users to explore Kansas Frontier Matrix data visually and intuitively. It is built with React and leverages MapLibre GL JS for map rendering (an open-source Mapbox GL JS alternative) to display rich geospatial layers. The frontend integrates a custom timeline component (canvas-based for performance) that lets users navigate through time, alongside the map. This combination enables a unique experience: as the user moves through the timeline, map layers appear or change according to the data relevant to that time period.

 

Map and Layers: The map viewer supports multiple base layers and overlay layers representing different datasets (terrain models, hydrology, land cover, historical maps, etc.). Layers are configured via JSON files (e.g. web/layers.json and app.config.json) that are generated during the build
GitHub
. These config files define how each dataset is styled, what legend to show, and its temporal range. The frontend reads this configuration to build layer menus, legends, and to know which data to fetch for a given time span. MapLibre GL handles the rendering of raster COGs (via tiling) and vector data. Users can toggle layers on/off, and the legend panel updates accordingly to explain symbology.

 

Timeline: A timeline slider or scrubber allows the user to select a year or date range. The timeline is likely drawn on an HTML canvas or SVG, showing markers for significant events and a range for each dataset’s coverage. When the timeline changes, the app filters the visible map layers to those active in that time. This temporal filter might be applied by adjusting layer opacity or fetching different item assets (for example, choosing the 1950s land cover layer when the timeline is set to 1950). The timeline can also highlight narrative “story” points – for example, pins or cards for key events like the Dust Bowl period or the Kansas-Nebraska Act – which users can click to see more details.

 

Search and Filters: The frontend includes an integrated search bar and filtering controls. The search allows full-text queries across the knowledge graph and catalog – a user could type a keyword like "railroad" or "Cheyenne" and get suggestions for relevant layers, places on the map, or historical events. This is powered by an index of names and descriptions (populated by the enrichment pipeline and knowledge graph). Filters enable narrowing down the content by category (e.g. only show environmental data, or only cultural events) or by facets like source or certainty. For instance, a filter might allow viewing only treaty-related layers, or only data with high confidence scores (if uncertainty metadata is present from the AI stage). These interactive tools ensure users can easily find information of interest within the vast trove of data.

 

Pop-ups and Storytelling: When users click on map features, pop-up windows display detailed information drawn from the knowledge graph and metadata. A popup for a site might show its name, a brief description or historical note, and links to related entities (e.g. people associated with that place). Thanks to the enrichment, pop-ups can also include glossary definitions or context – e.g. clicking a treaty boundary might show an excerpt about that treaty from a historical text. The frontend is also planned to support story maps and narrative guides (as hinted by project milestones), which would present curated sequences of map views and text for educational purposes.

 

Under the hood, the frontend is decoupled from the data. It loads data either from the static web/data directory (which mirrors processed GeoJSON for quick client access) or via the API for more complex queries. This separation means the UI is flexible and can be updated without altering the data pipeline. The use of React and modular components will help future contributors extend the interface (for example, adding a 3D globe view or integrating a CesiumJS time animation as mentioned in the roadmap). Overall, the frontend is the user-facing culmination of the project’s architecture – translating the complex backend into an accessible interactive atlas with a timeline, fulfilling the vision of a “Kansas Geo Timeline”
GitHub
.

✅ Reproducibility & Observability

Ensuring reproducibility is a core principle of the Kansas Frontier Matrix architecture. The entire pipeline – from data ingestion to site deployment – is designed to be repeatable and transparent. A new contributor can clone the repository and, with a single command (e.g. make fetch cogs terrain stac site), regenerate the datasets and web assets from scratch
GitHub
. This is possible because all data transformations and external data dependencies are codified in the Makefile and scripts, and all outputs are deterministic given the same inputs. To further bolster reproducibility, the project provides Docker containers (see the docker/ directory) that encapsulate the required runtime environment. This means the pipeline can run on any system (local or CI server) with identical results, avoiding “works on my machine” issues.

 

Observability of the pipeline and data quality is achieved through continuous integration (CI) and automated checks. The repository is equipped with CI workflows on GitHub Actions
GitHub
, including:

Build & Deploy pipeline (site.yml): Automatically rebuilds the site and data on new commits, and deploys updates (for the GitHub Pages demo and other outputs). This ensures that the live demo is always up-to-date with the latest data.

STAC validation (stac-validate.yml): Runs the STAC and JSON Schema validators on the catalog, producing dataset health shields (badges) that reflect the completeness and correctness of metadata
GitHub
. For example, the README displays badges indicating if the STAC catalog passes validation and the coverage status of datasets.

Code and security checks (codeql.yml and trivy.yml): These workflows run static analysis (CodeQL) and vulnerability scans (Trivy) on the codebase and Docker images
GitHub
. They help maintain code quality and security, which is essential in an open-source, data-centric project.

Pre-commit hooks: The project uses a pre-commit configuration to enforce coding standards (formatting, linting) and to run quick checks before code is pushed, reducing errors caught by CI later
GitHub
.

All artifacts produced by the pipeline (data files, catalogs, config, etc.) are accompanied by SHA-256 checksums
GitHub
. This not only ensures data integrity but also allows tracking if an output changed unexpectedly after a pipeline run. Observability is further enhanced by logging and verbose outputs during pipeline execution – contributors can inspect logs to understand each step of data processing.

 

Another aspect of reproducibility is documentation of processes. The project follows “MCP” templates for Methodology, which include experiment reports, Standard Operating Procedures (SOPs), and model cards for any analytical or modeling components
GitHub
. For example, if a machine learning model is used to geocode place names, there will be an experiment.md documenting the approach and a model_card.md detailing the model’s performance and limitations. These documents (often stored under an mcp/ directory) ensure that complex processes can be understood and repeated by others, reinforcing the open-science approach.

 

In summary, through automated builds, rigorous validation, containerization, and thorough documentation, the architecture guarantees that results are reproducible and that the system’s state is observable at every step. Any issues can be traced and resolved with confidence about what data and code produced which outcome.

🌐 Open Science & Semantic Interoperability

The Kansas Frontier Matrix is committed to open science principles and to using semantic web standards for maximal interoperability. All code is released under an open-source license (MIT)
GitHub
, and the data assembled (much of it public domain or openly licensed) is redistributed in open formats. The use of a reproducible pipeline and documentation (as described above) means that external researchers can verify and build upon the project’s work – a key tenet of open science.

 

Crucially, the project doesn’t exist in a vacuum: it aligns with widely adopted data standards to ensure its outputs can integrate with other platforms. Some of these key standards and vocabularies include:

CIDOC CRM: As noted, the knowledge graph adopts CIDOC CRM, the ISO standard ontology for cultural heritage integration. This provides a shared semantic language so that our representation of historical events, people, and places can be understood alongside museum, archive, or library data elsewhere. CIDOC CRM acts as a semantic glue, enabling information from diverse sources to connect in a meaningful way
cidoc-crm.org
. By using CRM classes (like E5 Event for historical events, E53 Place for locations, etc.), we facilitate data exchange with other CRM-based knowledge graphs and ensure longevity of our data model.

OWL-Time: Temporal data in the system is structured using the OWL-Time ontology
w3.org
. This means time spans, intervals, and dates are represented in a machine-interpretable way (for example, using time:Interval, time:hasBeginning, time:inXSDDateTime and so forth). Aligning to OWL-Time allows compatibility with other datasets that use the same ontology for temporal reasoning, and it provides a standardized way to express things like a decade or a season in linked data format.

PeriodO: The project takes advantage of PeriodO, which is a Linked Open Data gazetteer of historical period definitions
perio.do
. By referencing PeriodO entries for named eras (e.g. “Civil War (1861–1865)” or region-specific periods defined by historians), our knowledge graph can link to broader definitions and context for those time periods. This not only avoids reinventing definitions but also connects our data to a broader scholarly ecosystem – any other dataset referencing the same PeriodO period can be directly related. For users, this means clearer context: a period name in our UI could be resolved to a well-known definition with bibliography, via PeriodO.

DCAT (Data Catalog Vocabulary): For describing datasets and metadata catalogs, we embrace W3C’s DCAT standard. DCAT is an RDF vocabulary designed to standardize how data catalogs are described on the Web
en.wikipedia.org
. By mapping our STAC catalog metadata to DCAT (they are conceptually similar, as STAC is a specific kind of spatiotemporal catalog), we ensure that external catalog aggregators or search engines can harvest our metadata. In practical terms, a DCAT-aligned catalog makes the project’s datasets more discoverable – e.g. a portal aggregating open datasets could include Kansas Frontier Matrix entries seamlessly. DCAT also promotes federated search across catalogs, meaning someone looking for Kansas historical flood data might find our dataset alongside others, if both are described in DCAT.

GeoSPARQL and other ontologies: Although not explicitly mentioned in the prompt, it’s worth noting that any geospatial semantic queries could leverage GeoSPARQL (an OGC standard for spatial RDF queries) in the future. The commitment to semantic standards implies we keep an eye on using the right ontology for the right job (for instance, if we include geological data, we might look at GeoSciML or other domain ontologies as hinted in the roadmap
GitHub
).

Additionally, the project fosters open science by making not just the end products but also intermediate outputs and methodologies available. For example, the STAC catalog (in JSON form) is published openly for browsing
GitHub
, and the knowledge graph could be exported as RDF or CSV for others to analyze. The use of open data formats like GeoJSON, COG, and CSV ensures that even without specialized software, anyone can use the data. We also incorporate community-driven standards like DCAT-AP (DCAT Application Profile for datasets in Europe) where applicable, and plan for integration with Wikidata for linking entities (roadmap milestone for “semantic web” integration
GitHub
).

 

In summary, by adhering to these standards (CIDOC CRM, OWL-Time, PeriodO, DCAT, etc.), the Kansas Frontier Matrix ensures that its rich trove of information is not siloed. Instead, it becomes a part of the global graph of linked open data, contributing to and drawing from the collective knowledge of historical and geospatial information. This semantic interoperability amplifies the impact of the project’s data, enabling cross-domain research and ensuring the longevity of the data in forms that will remain understandable and reusable for years to come.

➕ Extending and Adding New Data

One of the goals of this project is to serve as a living platform that can be extended with new datasets and modules. The modular architecture and directory structure make it straightforward to add additional sources or features. Below is guidance for contributors on how to incorporate a new dataset or functionality into the Kansas Frontier Matrix:

Plan and Document the Data Source: Start by creating a source metadata file under data/sources/. This is typically a JSON (or YAML) file describing the dataset – including its name, description, source URL or archive information, license, and any preprocessing notes. For example, if adding a new historic trail map, you might create data/sources/historic_trail_map.json with fields detailing where the data comes from and how it should be handled. This file acts as the authoritative reference for provenance (and is used to generate provenance entries in the STAC and knowledge graph)
GitHub
.

Extend the ETL Pipeline: Develop the necessary extraction and transformation code in the scripts/ (or src/) directory. This could mean writing a new Python script or Jupyter notebook to fetch the raw data (e.g. download a zip or call an API), and then process it into the desired format. Reuse existing modules if possible (for instance, if it’s another raster layer, you might leverage an existing script for downloading and COGifying rasters). Update the Makefile to include targets for the new data (e.g. add make historic_trail_fetch and make historic_trail_process) so that it integrates with the overall build
GitHub
. Ensure to produce outputs in line with project conventions (place processed files in a logical subfolder under data/, such as data/processed/<category>/...).

Generate STAC Metadata: Every new dataset should be represented in the STAC catalog. This involves adding a Collection JSON in stac/collections/ and one or more Item JSON files in stac/items/. The collection file describes the dataset as a whole (spatial extent, temporal extent, provider info, license, etc.), and each item file describes an individual spatiotemporal asset (e.g. a specific map sheet, a year’s raster layer, an episode of an oral history). You can use existing collections as templates. For example, if adding a Kansas River dataset, you might create stac/collections/ks_kansas_river.json and then stac/items/ks_kansas_river/ containing items for each segment or each time slice
GitHub
. Be sure to include links back to the source (the data/sources entry) and set proper IDs, dates, and bounding boxes. After writing these, run make stac-validate to ensure the catalog remains compliant.

Integrate with the Knowledge Graph: If the new data introduces new entities (e.g. new historical events or places), consider how they map to the ontology. You might need to extend the graph ingestion script to incorporate this dataset. For instance, adding a dataset of historical figures might require creating Person nodes and linking them to places or events from other data. Follow the CIDOC CRM mapping guidelines; e.g., a new set of events might be represented as E5 Event nodes, each linked to a place (E53 Place) and time (E52 Time-Span). Also, include provenance links in the graph (like a P148 has component relation to a dataset node or a citation). This step might involve writing a small ETL for the graph (possibly as part of the Python scripts).

Update Frontend Configuration: To expose the new layer or content on the map and timeline, update the config files in web/. Add a new entry in layers.json for the dataset, specifying how it should appear (layer type, style, legend, timeline settings). Also update app.config.json or any relevant config to ensure the layer group and metadata are included
GitHub
. For example, define the display name, the icon or color, and link to the STAC collection or directly to the data assets. If the data should be part of a specific category (like “Hydrology” or “Culture”), place it accordingly in the config’s hierarchy.

Run and Verify: Re-run the pipeline (make commands) to fetch, process, and integrate the new data. Then open the web app (locally via python -m http.server or via the Docker setup) to verify that the new layer appears on the map, that its timeline activation works, and that metadata is showing up in pop-ups. Also verify that the STAC catalog now contains the new collection and that make stac-validate passes (meaning your JSON metadata is correct). Check the knowledge graph (if you have Neo4j or another interface set up) to see that new nodes/relations are created as expected.

Document and Commit: Add an entry to the project documentation or changelog about the new dataset. If the dataset or feature is complex, consider writing a short docs/ guide or an mcp/ experiment report explaining any analysis done. All new code should adhere to coding standards (run pre-commit hooks) and any new terms in STAC or graph schema should be explained. Once ready, commit your changes and open a Pull Request for review.

By following these steps, you ensure new additions are smoothly integrated into the Kansas Frontier Matrix. The architecture’s modularity (with clearly separated concerns: data files in data/, metadata in stac/, code in scripts/, config in web/) allows the project to grow in scope without losing organization. Each new module or dataset strengthens the knowledge hub, and thanks to the CI checks (STAC validation, etc.), you’ll get feedback quickly if something needs adjustment
GitHub
 (for example, CI will flag if a STAC field is missing or if the dataset isn’t reproducible with the Makefile).

 

Finally, contributors are encouraged to follow the project’s open science ethos when adding new content – include your sources, use standard schemas (e.g. if your data has an existing schema or ontology, align with it), and provide documentation. This way, Kansas Frontier Matrix will continue to expand as a reliable, interoperable resource for understanding the rich tapestry of Kansas history.
