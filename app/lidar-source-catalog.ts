/** Shared discovery/readiness projection. Provider availability is not installation.
 * Original surveys may appear in multiple portals: do not count mirrors as
 * independent measurements or blend dates/datums merely because extents overlap.
 */
export type LidarSourceCatalogRecord = Readonly<{
  id: string;
  title: string;
  organization: string;
  coverage: string;
  geometry: "grids-and-point-clouds" | "orbital-profiles" | "survey-index" | "derived-assets";
  readiness: "continuous-terrain" | "sampled-science" | "discovery" | "access-unverified";
  access: "public-no-key" | "free-account" | "unverified";
  products: readonly string[];
  sourceUrl: string;
  notes: string;
  actionUrl?: string;
}>;

export const LIDAR_CATALOG_CHECKED_AT = "2026-11-24T01:47:00Z";

// No paid service, requester-pays bucket or commercial Earth Engine eligibility
// is assumed. These are source families, not an exhaustive installed tile list.
export const KANSAS_LIDAR_SOURCE_CATALOG: readonly LidarSourceCatalogRecord[] = Object.freeze([
  {
    id: "usgs-3dep", title: "USGS 3DEP", organization: "U.S. Geological Survey",
    coverage: "Kansas continuous ground display; exact native products vary by location",
    geometry: "grids-and-point-clouds", readiness: "continuous-terrain", access: "public-no-key",
    products: ["Bare-earth DEM", "Published LiDAR point clouds", "Work-unit metadata"],
    sourceUrl: "https://www.usgs.gov/3d-elevation-program/about-3dep-products-services",
    notes: "KFM's live elevation mosaic supports a continuous ground mesh. It combines resolutions and acquisition dates; the display does not identify one survey or prove statewide one-metre LiDAR coverage. Native downloads use free USGS delivery, excluding requester-pays access.",
  },
  {
    id: "neon", title: "NEON terrain & vegetation", organization: "National Ecological Observatory Network",
    coverage: "Kansas observatory flight footprints; one Konza September 2024 catalog tile is prepared in KFM",
    geometry: "grids-and-point-clouds", readiness: "sampled-science", access: "free-account",
    products: ["Ground model", "Surface model", "Independent canopy model", "Discrete point cloud"],
    sourceUrl: "https://www.neonscience.org/data-collection/lidar", actionUrl: "/labs/terrain",
    notes: "The existing Konza sample has native raster provenance and source-linked science rows. Additional flights and raw point clouds are not made ready by this catalog. Provider canopy is independent of surface minus ground; scientific review remains pending.",
  },
  {
    id: "kansas-dasc", title: "Kansas LiDAR archive", organization: "Kansas Data Access & Support Center",
    coverage: "State and local acquisition projects indexed across Kansas",
    geometry: "grids-and-point-clouds", readiness: "discovery", access: "public-no-key",
    products: ["Tile download index", "Ground and first-return grids where supplied", "Classified points where supplied"],
    sourceUrl: "https://services1.arcgis.com/q2CglofYX6ACNEeu/ArcGIS/rest/services/Kansas_LiDAR_Download_Grid_V2_WFL1/FeatureServer",
    notes: "Inspect each project and download format before processing. Some deliveries use ZLAS or IMG; compatibility and product rights require an asset-level check. A DASC and USGS copy of the same acquisition is one survey, not two independent observations.",
  },
  {
    id: "usiei", title: "Interagency elevation inventory", organization: "NOAA / USGS and federal partners",
    coverage: "Kansas-intersecting surveys within the U.S. public elevation inventory",
    geometry: "survey-index", readiness: "discovery", access: "public-no-key",
    products: ["Survey footprints", "Acquisition metadata", "Provider access points"],
    sourceUrl: "https://coast.noaa.gov/inventory/",
    notes: "Use LiDAR topographic, bathymetric and topobathymetric records to find additional federal, state and local surveys. The inventory is metadata, includes in-progress acquisitions and other sensor types, and does not contain the native elevation files or establish their installation in KFM.",
  },
  {
    id: "nasa-icesat2", title: "ICESat-2 photon tracks & land profiles", organization: "NASA / NSIDC",
    coverage: "Orbital tracks intersecting Kansas; sparse along-track support",
    geometry: "orbital-profiles", readiness: "discovery", access: "free-account",
    products: ["ATL03 geolocated photons", "ATL08 land and vegetation profiles"],
    sourceUrl: "https://icesat-2.gsfc.nasa.gov/icesat-2-data",
    notes: "NASA provides free data access with Earthdata login. Track and segment measurements need product-specific quality flags and vertical references. They do not supply a wall-to-wall native terrain or canopy surface, and are not yet connected to KFM science rows.",
  },
  {
    id: "nasa-gedi", title: "GEDI canopy footprints & waveforms", organization: "NASA / University of Maryland / DAACs",
    coverage: "Available orbital footprints within Kansas; coverage must be queried for the chosen period",
    geometry: "orbital-profiles", readiness: "discovery", access: "free-account",
    products: ["Geolocated waveforms", "Footprint elevation and height metrics", "Canopy profile metrics"],
    sourceUrl: "https://gedi.umd.edu/dataproducts/download/",
    notes: "Public GEDI products are free to download. Footprint-level observations, interpolated grids and modelled biomass products have different support and uncertainty. No GEDI files or canopy estimates are installed by this catalog, and sparse shots must not be rendered as continuous measured terrain.",
  },
  {
    id: "kdot-mobile", title: "KDOT mobile LiDAR asset extracts", organization: "Kansas Department of Transportation",
    coverage: "Kansas state highway collections, including 2021 and 2023 projects",
    geometry: "derived-assets", readiness: "access-unverified", access: "unverified",
    products: ["Roadway asset GIS extracts", "Project and data dictionary records"],
    sourceUrl: "https://www.ksdot.gov/about/our-organization/divisions/planning-and-development/kdot-lidar-project-data-portal",
    notes: "Published GIS extracts are distinct from raw vehicle point clouds and airborne ground models. Download instructions require ArcGIS Online or KanPlan access; raw-data access, redistribution and no-cost use have not been qualified. No subscription or paid account will be activated.",
  },
  {
    id: "noaa-digital-coast", title: "NOAA Digital Coast LiDAR archive", organization: "NOAA Office for Coastal Management / contributors",
    coverage: "Primarily coastal; a Kansas native-data holding has not been established",
    geometry: "grids-and-point-clouds", readiness: "discovery", access: "public-no-key",
    products: ["LAZ point clouds", "Survey DEMs where supplied", "Survey reports and tile indexes"],
    sourceUrl: "https://coast.noaa.gov/htdata/lidar1_z/index.html",
    notes: "The public archive can identify additional provider deliveries. Check the actual footprint before treating it as Kansas coverage. Mirror copies must retain original survey identity; no NOAA point payload is currently prepared for KFM's terrain/science tools.",
  },
].map(record => Object.freeze({ ...record, products: Object.freeze(record.products) })) as LidarSourceCatalogRecord[]);

/** Metadata needed before quantitative cross-source comparison. A checksum
 * proves captured bytes, not spatial/vertical alignment or sensor accuracy. */
export const LIDAR_COMPARISON_REQUIREMENTS = Object.freeze([
  "Original survey, product, revision and asset checksum",
  "Horizontal reference system and coordinate epoch",
  "Vertical datum, geoid, vertical units and conversion method",
  "Acquisition interval, native resolution and measurement support",
  "NoData/quality flags, classification and processing method",
  "Explicit co-registration, resampling and uncertainty assessment",
]);

export function lidarSourceRecord(id: string): LidarSourceCatalogRecord | undefined {
  return KANSAS_LIDAR_SOURCE_CATALOG.find(source => source.id === id);
}
