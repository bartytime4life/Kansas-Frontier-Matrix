import type {
  AtlasWorkbenchTool,
  MapInteractionTool,
  RepositoryArtifactRef,
  RepositoryLayerConnection,
} from "./types";

const artifact = (
  kind: RepositoryArtifactRef["kind"],
  label: string,
  path: string,
): RepositoryArtifactRef => Object.freeze({ kind, label, path });

const connection = (
  value: Omit<RepositoryLayerConnection, "artifacts" | "relatedToolIds"> &
    Readonly<{
      artifacts: readonly RepositoryArtifactRef[];
      relatedToolIds: readonly string[];
    }>,
): RepositoryLayerConnection =>
  Object.freeze({
    ...value,
    artifacts: Object.freeze([...value.artifacts]),
    relatedToolIds: Object.freeze([...value.relatedToolIds]),
  });

/**
 * Repository-backed layer candidates. These are discoverable connections, not
 * admitted runtime layers. Their state mirrors the referenced repository files.
 */
export const REPOSITORY_LAYER_CONNECTIONS: readonly RepositoryLayerConnection[] =
  Object.freeze([
    connection({
      id: "connection:wbd-huc12",
      name: "WBD HUC12 watershed boundaries",
      domain: "hydrology",
      geometryType: "POLYGON",
      source: "USGS Watershed Boundary Dataset",
      state: "FIXTURE_ONLY",
      summary: "A deterministic, no-network HUC12 candidate pipeline is bound to fixtures, contracts, tests, and CI.",
      statusReason: "The pipeline declaration is fixture-only and explicitly denies live access, lifecycle writes, promotion, release, and publication.",
      cannotProve: "Current watershed condition, observed flow, flood status, source activation, or public release.",
      nextGate: "Complete source, rights, sensitivity, evidence, review, and release decisions for an exact WBD edition.",
      artifacts: [
        artifact("CONNECTOR", "WBD/HUC connector lane", "connectors/usgs/wbd_huc"),
        artifact("PIPELINE_SPEC", "Fixture-first HUC12 pipeline", "pipeline_specs/hydrology/wbd_huc12_ingest.yaml"),
        artifact("CONTRACT", "HUC12 ingest candidate", "contracts/domains/hydrology/wbd_huc12_ingest_candidate.md"),
      ],
      relatedToolIds: ["huc-crosswalk", "layer-catalog", "provenance"],
    }),
    connection({
      id: "connection:nwis-observations",
      name: "USGS NWIS gauge observations",
      domain: "hydrology",
      geometryType: "POINT",
      source: "USGS Water Data for the Nation",
      state: "CAPTURE_FIXTURE",
      summary: "The connector includes a captured-input-only county adapter with synthetic tests; the declared ingest pipeline remains inactive.",
      statusReason: "Live transport, source activation, lifecycle writes, rights closure, evidence, and release are not established.",
      cannotProve: "Current streamflow, inundation, velocity, upstream causation, or safety.",
      nextGate: "Bind an active descriptor and exact service semantics while preserving site identity, units, qualifiers, observation time, and corrections.",
      artifacts: [
        artifact("CONNECTOR", "NWIS captured-input lane", "connectors/usgs/water_data"),
        artifact("PIPELINE_SPEC", "Inactive NWIS ingest candidate", "pipeline_specs/hydrology/ingest_usgs_nwis.yaml"),
        artifact("CONTRACT", "NWIS county capture", "contracts/domains/hydrology/nwis_county_capture.md"),
      ],
      relatedToolIds: ["streamflow-qc", "source-watchlist", "provenance"],
    }),
    connection({
      id: "connection:nhdplus-network",
      name: "NHDPlus HR network context",
      domain: "hydrology",
      geometryType: "LINE",
      source: "USGS NHDPlus High Resolution",
      state: "PROPOSED_INACTIVE",
      summary: "The repository documents the source-role boundary and an inactive ingest declaration for hydrography and modeled network attributes.",
      statusReason: "Connector code, accepted source descriptors, fixtures, and release behavior are not established.",
      cannotProve: "Observed streamflow, flood conditions, engineering fitness, or current safety.",
      nextGate: "Preserve COMID, release vintage, geometry lineage, modeled VAA roles, topology, review, and release evidence.",
      artifacts: [
        artifact("CONNECTOR", "NHDPlus HR connector lane", "connectors/usgs/nhdplus_hr"),
        artifact("PIPELINE_SPEC", "Inactive NHDPlus ingest", "pipeline_specs/hydrology/nhdplus_hr_ingest.yaml"),
        artifact("CONTRACT", "Network revision contract", "contracts/domains/hydrology/nhdplus_network_revision.md"),
      ],
      relatedToolIds: ["huc-crosswalk", "layer-lineage"],
    }),
    connection({
      id: "connection:nfhl-context",
      name: "FEMA NFHL regulatory context",
      domain: "hazards",
      geometryType: "POLYGON",
      source: "FEMA National Flood Hazard Layer",
      state: "PROPOSED_INACTIVE",
      summary: "The preferred product lane and inactive context pipeline are present as regulatory-context boundaries.",
      statusReason: "No executable NFHL adapter, active source descriptor, accepted routing, tests, or release evidence is confirmed.",
      cannotProve: "Observed flooding, parcel status, insurance or legal determination, engineering suitability, or safety.",
      nextGate: "Resolve exact surface, version, effective date, regulatory fields, CRS, datum, rights, routing, and release review.",
      artifacts: [
        artifact("CONNECTOR", "NFHL product lane", "connectors/fema/nfhl"),
        artifact("PIPELINE_SPEC", "Inactive NFHL context", "pipeline_specs/hydrology/nfhl_context.yaml"),
        artifact("CONTRACT", "Layer admission boundary", "contracts/runtime/layer_manifest_admission.md"),
      ],
      relatedToolIds: ["source-watchlist", "layer-lineage"],
    }),
    connection({
      id: "connection:usgs-earthquakes",
      name: "USGS earthquake catalog candidate",
      domain: "hazards",
      geometryType: "POINT",
      source: "USGS Earthquake Catalog",
      state: "DOCUMENTED_ONLY",
      summary: "The repository contains a README-only connector boundary and an inactive, unbound earthquake pipeline declaration; no source export is committed to UI fixtures.",
      statusReason: "Connector placement remains ADR-class and unresolved. Source admission, canonical event identity, rights approval, lifecycle writes, EvidenceBundles, governed API answers, release, and publication are unimplemented.",
      cannotProve: "Earthquake prediction, event completeness, exact Kansas jurisdiction membership, current conditions, impacts, safety, source activation, or public release.",
      nextGate: "Resolve connector placement before code; then review source rights and define canonical alias/revision semantics before contracts, schemas, governed capture, deterministic transforms, evidence, policy, release, correction, and rollback.",
      artifacts: [
        artifact("CONNECTOR", "USGS earthquake connector boundary", "connectors/usgs-earthquake"),
        artifact("PIPELINE_SPEC", "Inactive earthquake pipeline", "pipeline_specs/hazards/usgs_earthquake.yaml"),
        artifact("CONTRACT", "Runtime layer admission", "contracts/runtime/layer_manifest_admission.md"),
      ],
      relatedToolIds: ["source-watchlist", "layer-lineage", "provenance"],
    }),
    connection({
      id: "connection:three-dep-terrain",
      name: "3DEP elevation and terrain",
      domain: "geology",
      geometryType: "RASTER",
      source: "USGS 3D Elevation Program",
      state: "FIXTURE_ONLY",
      summary: "One exact USGS 3DEP 1 m tile is hash-bound as an inactive candidate with closed metadata validation and a minimized offline sample.",
      statusReason: "The delivered-tile geoid and applicable numeric vertical accuracy remain unresolved, human review is pending, and no source descriptor, runtime load, or public release exists.",
      cannotProve: "Survey-grade accuracy, delivered-tile geoid lineage, slope, aspect, terrain safety, current land condition, admission, or runtime fitness.",
      nextGate: "Resolve an applicable numeric accuracy statement, accept or replace the source-work-unit geoid lineage, complete human review, then decide source admission separately.",
      artifacts: [
        artifact("CONNECTOR", "3DEP connector lane", "connectors/usgs/3dep"),
        artifact("CONTRACT", "Exact inactive DEM candidate", "contracts/spatial-foundation/dem_source_asset_candidate.md"),
        artifact("CONTRACT", "Runtime layer admission", "contracts/runtime/layer_manifest_admission.md"),
      ],
      relatedToolIds: ["stac-inspector", "pmtiles-diagnostics"],
    }),
    connection({
      id: "connection:kgs-bedrock",
      name: "KGS bedrock units",
      domain: "geology",
      geometryType: "POLYGON",
      source: "Kansas Geological Survey",
      state: "PROPOSED_INACTIVE",
      summary: "A compatibility connector boundary and an inactive bedrock-units pipeline declaration are discoverable.",
      statusReason: "The declared pipeline is disabled and its source, contract, schema, implementation, fixture, test, and workflow bindings are empty.",
      cannotProve: "Site geology, subsurface continuity, engineering conditions, resources, or ownership.",
      nextGate: "Resolve canonical connector placement, exact map edition, source role, scale, fields, rights, validation, and release.",
      artifacts: [
        artifact("CONNECTOR", "KGS bedrock compatibility lane", "connectors/kgs_bedrock"),
        artifact("PIPELINE_SPEC", "Inactive bedrock units", "pipeline_specs/geology/bedrock_units.spec.yaml"),
        artifact("CONTRACT", "Layer manifest", "contracts/data/layer_manifest.md"),
      ],
      relatedToolIds: ["layer-catalog", "layer-lineage"],
    }),
    connection({
      id: "connection:kgs-surficial",
      name: "KGS surficial geology",
      domain: "geology",
      geometryType: "POLYGON",
      source: "Kansas Geological Survey",
      state: "PROPOSED_INACTIVE",
      summary: "A compatibility connector boundary and an inactive surficial-units pipeline declaration are discoverable.",
      statusReason: "Implementation in the compatibility path is not established and the pipeline is disabled with no bound artifacts.",
      cannotProve: "Field conditions, material depth, engineering behavior, hazards, or resource potential.",
      nextGate: "Resolve canonical placement and bind the exact edition, scale, classification, source role, contracts, tests, review, and release.",
      artifacts: [
        artifact("CONNECTOR", "KGS surficial compatibility lane", "connectors/kgs_surficial"),
        artifact("PIPELINE_SPEC", "Inactive surficial units", "pipeline_specs/geology/surficial_units.spec.yaml"),
        artifact("CONTRACT", "Surficial contract boundary", "contracts/domains/geology/sublanes/surficial"),
      ],
      relatedToolIds: ["layer-catalog", "layer-lineage"],
    }),
    connection({
      id: "connection:wwc5-wells",
      name: "WWC5 well-log references",
      domain: "geology",
      geometryType: "POINT",
      source: "KGS / KDHE WWC5",
      state: "PROPOSED_INACTIVE",
      summary: "The repository preserves a compatibility connector lane, well-log contract, and inactive well-log pipeline candidate.",
      statusReason: "Executable behavior is absent in the compatibility lane and pipeline bindings are empty.",
      cannotProve: "Current groundwater condition, water quality, complete construction history, precise private detail, or suitability.",
      nextGate: "Resolve canonical placement, identity, public-safe precision, rights, source role, schemas, tests, review, and release.",
      artifacts: [
        artifact("CONNECTOR", "WWC5 compatibility lane", "connectors/kgs_kdhe_wwc5"),
        artifact("PIPELINE_SPEC", "Inactive well-log pipeline", "pipeline_specs/geology/well_logs.spec.yaml"),
        artifact("CONTRACT", "Well-log reference", "contracts/domains/geology/WellLogReference.md"),
      ],
      relatedToolIds: ["layer-catalog", "source-watchlist"],
    }),
    connection({
      id: "connection:tiger-roads",
      name: "TIGER/Line road network",
      domain: "roads_rail_trade",
      geometryType: "LINE",
      source: "U.S. Census Bureau TIGER/Line",
      state: "PROPOSED_INACTIVE",
      summary: "A draft connector lane and inactive road-ingest declaration expose the intended network boundary.",
      statusReason: "Current vintages, feature-class allowlists, executable parsing, fixtures, and release behavior remain unverified.",
      cannotProve: "Routability, closure, traffic, ownership, access, pavement condition, or safety.",
      nextGate: "Pin an edition and bind road identity, classifications, geometry quality, rights, tests, review, and release.",
      artifacts: [
        artifact("CONNECTOR", "TIGER/Line connector lane", "connectors/tiger_line"),
        artifact("PIPELINE_SPEC", "Inactive TIGER roads", "pipeline_specs/roads-rail-trade/tiger_roads.yaml"),
        artifact("CONTRACT", "Road segment", "contracts/domains/roads-rail-trade/road_segment.md"),
      ],
      relatedToolIds: ["layer-catalog", "layer-lineage"],
    }),
    connection({
      id: "connection:wzdx-work-zones",
      name: "WZDx work-zone events",
      domain: "roads_rail_trade",
      geometryType: "LINE",
      source: "WZDx-compatible transportation feeds",
      state: "PROPOSED_INACTIVE",
      summary: "The draft connector and disabled v4 pipeline candidate identify a future work-zone event lane.",
      statusReason: "No source descriptor, endpoint, fixture, executable connector, test, or release binding is established.",
      cannotProve: "A current closure, detour, route, traffic condition, access restriction, or travel safety.",
      nextGate: "Bind an exact feed/version and preserve event identity, validity, corrections, geometry, access semantics, review, and release.",
      artifacts: [
        artifact("CONNECTOR", "WZDx connector lane", "connectors/wzdx"),
        artifact("PIPELINE_SPEC", "Inactive WZDx v4", "pipeline_specs/roads-rail-trade/wzdx_v4.yaml"),
        artifact("CONTRACT", "Restriction event", "contracts/domains/roads-rail-trade/restriction_event.md"),
      ],
      relatedToolIds: ["source-watchlist", "layer-lineage"],
    }),
    connection({
      id: "connection:hms-smoke",
      name: "NOAA HMS smoke polygons",
      domain: "atmosphere",
      geometryType: "POLYGON",
      source: "NOAA Hazard Mapping System",
      state: "PROPOSED_INACTIVE",
      summary: "A README-only connector boundary and disabled pipeline candidate keep qualitative smoke context distinct from fire detections.",
      statusReason: "Canonical placement, executable connector code, source activation, schema enforcement, fixtures, and release wiring are unresolved.",
      cannotProve: "Surface PM2.5, AQI, exposure, ground-confirmed fire, health effects, or life-safety guidance.",
      nextGate: "Resolve connector topology and bind component roles, issue/valid time, source identity, rights, safety review, evidence, and release.",
      artifacts: [
        artifact("CONNECTOR", "HMS smoke boundary", "connectors/noaa-hms-smoke"),
        artifact("PIPELINE_SPEC", "Inactive HMS smoke", "pipeline_specs/hazards/noaa_hms_smoke.yaml"),
        artifact("CONTRACT", "Smoke context", "contracts/domains/atmosphere/smoke-context.md"),
      ],
      relatedToolIds: ["source-watchlist", "layer-lineage"],
    }),
    connection({
      id: "connection:nws-alerts",
      name: "NWS alert context",
      domain: "hazards",
      geometryType: "POLYGON",
      source: "National Weather Service API",
      state: "PROPOSED_INACTIVE",
      summary: "The API product boundary and an inactive alert-context pipeline are present for official-source-linked context.",
      statusReason: "The connector topology is conflicted and executable behavior, source activation, fixtures, tests, and release remain unverified.",
      cannotProve: "That KFM is an alert relay, current warning authority, forecast guarantee, or emergency-response system.",
      nextGate: "Resolve topology and bind exact API resources, identifiers, issue/valid times, caching, failure modes, rights, review, and release.",
      artifacts: [
        artifact("CONNECTOR", "NWS API product lane", "connectors/nws-api"),
        artifact("PIPELINE_SPEC", "Inactive NWS alert context", "pipeline_specs/hazards/nws_alerts_context.yaml"),
        artifact("CONTRACT", "Temporal authority envelope", "contracts/evidence/temporal_authority_envelope.md"),
      ],
      relatedToolIds: ["source-watchlist", "layer-lineage"],
    }),
    connection({
      id: "connection:hls-ndvi",
      name: "HLS vegetation-index change",
      domain: "agriculture",
      geometryType: "RASTER",
      source: "NASA Harmonized Landsat Sentinel-2",
      state: "DOCUMENTED_ONLY",
      summary: "The source-admission lane and NDVI materiality/readiness contracts are present, but no active Explorer release is bound.",
      statusReason: "The repository does not establish an active source, public raster artifact, or released layer manifest for this workspace.",
      cannotProve: "Crop identity, yield, ownership, management, causation, or field-level condition.",
      nextGate: "Bind exact items, cloud/nodata handling, computation lineage, materiality thresholds, rights, evidence, review, and release.",
      artifacts: [
        artifact("CONNECTOR", "NASA HLS connector lane", "connectors/nasa-hls"),
        artifact("CONTRACT", "NDVI materiality", "contracts/domains/agriculture/hls_ndvi_zonal_materiality.md"),
        artifact("CONTRACT", "NDVI readiness", "contracts/domains/agriculture/ndvi_readiness.md"),
      ],
      relatedToolIds: ["ndvi-change", "stac-inspector"],
    }),
    connection({
      id: "connection:smap-soil-moisture",
      name: "SMAP soil-moisture observations",
      domain: "soil",
      geometryType: "RASTER",
      source: "NASA Soil Moisture Active Passive",
      state: "DOCUMENTED_ONLY",
      summary: "The source-admission lane and soil-moisture observation contract are discoverable as a future coarse-resolution layer boundary.",
      statusReason: "No active descriptor, pipeline binding, fixture evidence, public raster artifact, or release manifest is established.",
      cannotProve: "Field-scale soil moisture, a specific horizon condition, irrigation need, yield, or ground truth.",
      nextGate: "Bind the exact product, resolution, retrieval time, units, quality flags, nodata, validation, rights, evidence, review, and release.",
      artifacts: [
        artifact("CONNECTOR", "NASA SMAP connector lane", "connectors/nasa-smap"),
        artifact("CONTRACT", "Soil-moisture observation", "contracts/domains/soil/soil_moisture_observation.md"),
        artifact("CONTRACT", "Layer manifest", "contracts/data/layer_manifest.md"),
      ],
      relatedToolIds: ["soil-change", "stac-inspector"],
    }),
  ]);

export const MAP_INTERACTION_TOOLS: readonly MapInteractionTool[] = Object.freeze([
  Object.freeze({
    id: "select",
    name: "Select",
    state: "AVAILABLE_IN_SITE",
    summary: "Choose a catalog layer and resolve its finite Evidence Drawer posture.",
    statusReason: "Available for the bounded site-local layer registry.",
  }),
  Object.freeze({
    id: "draw",
    name: "Draw AOI",
    state: "HELD",
    summary: "Proposed area-of-interest sketch for scoped analysis requests.",
    statusReason: "Geometry, consent, sensitivity, persistence, and evidence-request contracts are not bound.",
  }),
  Object.freeze({
    id: "measure",
    name: "Measure",
    state: "HELD",
    summary: "Proposed distance and area measurement with CRS and accuracy disclosure.",
    statusReason: "Measurement, projection, units, uncertainty, and export contracts are not bound.",
  }),
  Object.freeze({
    id: "profile",
    name: "Profile",
    state: "HELD",
    summary: "Proposed elevation or thematic profile along a governed selection.",
    statusReason: "No admitted terrain or profile artifact and no vertical-datum disclosure are available.",
  }),
]);

const workbench = (
  value: AtlasWorkbenchTool,
): AtlasWorkbenchTool =>
  Object.freeze({
    ...value,
    relatedLayerConnectionIds: Object.freeze([
      ...value.relatedLayerConnectionIds,
    ]),
  });

export const ATLAS_WORKBENCH_TOOLS: readonly AtlasWorkbenchTool[] = Object.freeze([
  workbench({ id: "layer-catalog", name: "Layer Catalog", maturity: "DOCUMENTED", summary: "Discover layer rights, time, evidence, release, and representation context.", featurePath: "apps/explorer-web/src/features/layer_catalog", catalogQuery: "Layer Catalog", relatedLayerConnectionIds: ["connection:wbd-huc12", "connection:kgs-bedrock", "connection:kgs-surficial", "connection:wwc5-wells", "connection:tiger-roads"] }),
  workbench({ id: "huc-crosswalk", name: "HUC crosswalk explorer", maturity: "FIXTURE_FIRST", summary: "Inspect bounded HUC and COMID identifier relationships without treating joins as hydrologic proof.", featurePath: "apps/explorer-web/src/features/huc_crosswalk_explorer", catalogQuery: "HUC crosswalk explorer", relatedLayerConnectionIds: ["connection:wbd-huc12", "connection:nhdplus-network"] }),
  workbench({ id: "streamflow-qc", name: "Streamflow quality dashboard", maturity: "FIXTURE_FIRST", summary: "Inspect quality, freshness, qualifiers, and correction state for streamflow observations.", featurePath: "apps/explorer-web/src/features/streamflow_qc_dashboard", catalogQuery: "Streamflow quality dashboard", relatedLayerConnectionIds: ["connection:nwis-observations"] }),
  workbench({ id: "soil-change", name: "Soil yearly change viewer", maturity: "FIXTURE_FIRST", summary: "Compare bounded soil projections while preserving component, horizon, method, and time identity.", featurePath: "apps/explorer-web/src/features/soil_yearly_change_viewer", catalogQuery: "Soil yearly change viewer", relatedLayerConnectionIds: ["connection:smap-soil-moisture"] }),
  workbench({ id: "ndvi-change", name: "County NDVI change panel", maturity: "FIXTURE_FIRST", summary: "Review vegetation-change projections with materiality and readiness limitations visible.", featurePath: "apps/explorer-web/src/features/county_ndvi_change_panel", catalogQuery: "County NDVI change panel", relatedLayerConnectionIds: ["connection:hls-ndvi"] }),
  workbench({ id: "source-watchlist", name: "Source availability watchlist", maturity: "FIXTURE_FIRST", summary: "Inspect availability and staleness signals without activating a source.", featurePath: "apps/explorer-web/src/features/source_availability_watchlist", catalogQuery: "Source availability watchlist", relatedLayerConnectionIds: ["connection:nwis-observations", "connection:nfhl-context", "connection:usgs-earthquakes", "connection:wwc5-wells", "connection:wzdx-work-zones", "connection:hms-smoke", "connection:nws-alerts"] }),
  workbench({ id: "stac-inspector", name: "STAC conformance inspector", maturity: "FIXTURE_FIRST", summary: "Inspect release-facing STAC metadata without reading raw or quarantine material.", featurePath: "apps/explorer-web/src/features/stac_conformance_inspector", catalogQuery: "STAC conformance inspector", relatedLayerConnectionIds: ["connection:three-dep-terrain", "connection:hls-ndvi", "connection:smap-soil-moisture"] }),
  workbench({ id: "pmtiles-diagnostics", name: "PMTiles range diagnostics", maturity: "FIXTURE_FIRST", summary: "Verify archive, range, index, and render behavior for governed artifacts.", featurePath: "apps/explorer-web/src/features/pmtiles_range_diagnostics", catalogQuery: "PMTiles range diagnostics", relatedLayerConnectionIds: ["connection:three-dep-terrain"] }),
  workbench({ id: "layer-lineage", name: "Layer lineage timeline", maturity: "FIXTURE_FIRST", summary: "Inspect derivation, correction, supersession, and release lineage.", featurePath: "apps/explorer-web/src/features/layer_lineage_timeline", catalogQuery: "Layer lineage timeline", relatedLayerConnectionIds: ["connection:nhdplus-network", "connection:nfhl-context", "connection:usgs-earthquakes", "connection:kgs-bedrock", "connection:kgs-surficial", "connection:tiger-roads", "connection:wzdx-work-zones", "connection:hms-smoke", "connection:nws-alerts"] }),
  workbench({ id: "provenance", name: "Provenance citations", maturity: "FIXTURE_FIRST", summary: "Inspect bounded provenance and citation projections for eligible evidence.", featurePath: "apps/explorer-web/src/features/provenance_citations", catalogQuery: "Provenance citations", relatedLayerConnectionIds: ["connection:wbd-huc12", "connection:nwis-observations", "connection:usgs-earthquakes"] }),
]);

export const findRepositoryLayerConnection = (
  id: string,
): RepositoryLayerConnection | null =>
  REPOSITORY_LAYER_CONNECTIONS.find((entry) => entry.id === id) ?? null;

export const findAtlasWorkbenchTool = (
  id: string,
): AtlasWorkbenchTool | null =>
  ATLAS_WORKBENCH_TOOLS.find((entry) => entry.id === id) ?? null;
