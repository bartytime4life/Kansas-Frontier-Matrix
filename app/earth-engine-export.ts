import { EARTH_ENGINE_DATASETS, KANSAS_BOUNDARY, earthEngineUrl } from "./earth-engine-data";
import { EARTH_ENGINE_CONTEXT_LAYERS, type EarthEngineContextLayerId } from "./earth-engine-context";

export type EarthEngineExportScope = "sample" | "statewide";
const GRID_30M = { crs: "EPSG:5070", crsTransform: [30, 0, -1200000, 0, -30, 2400000] };
export const EARTH_ENGINE_EXPORT_GRID = Object.freeze(GRID_30M);
const NATIVE_CLIMATE_GRIDS = {
  "ee-chirps": [0.05, 0, -180, 0, -0.05, 50],
  "ee-terraclimate": [1 / 24, 0, -180, 0, -(1 / 24), 90],
} as const;

export function buildEarthEngineExportRecipe(id: EarthEngineContextLayerId, scope: EarthEngineExportScope): string {
  const selected = EARTH_ENGINE_CONTEXT_LAYERS.find((layer) => layer.id === id);
  const catalog = EARTH_ENGINE_DATASETS.find((layer) => layer.id === id);
  if (!selected || !catalog || !["sample", "statewide"].includes(scope)) throw new Error("Choose one of the five reviewed display products.");
  const highResolution = id === "ee-cdl" || id === "ee-sentinel2" || id === "ee-3dep";
  const name = `kfm_${id.replaceAll("-", "_")}_${id === "ee-3dep" ? "mixed_dates" : "2024"}_${scope}`;
  const lines = [
    "// KFM Earth Engine Drive export recipe v1. Run only in the owner's registered noncommercial project.",
    "// REVIEW CONTEXT ONLY: neither an admitted KFM source nor claim evidence.",
    `// ${catalog.title}: ${earthEngineUrl(catalog)}`,
    `// ${catalog.terms}`,
    `// ${catalog.limitation}`,
    "// Run the small sample first; inspect masks, units, coverage and task outcome before running statewide.",
    "// Copy the complete source IDs, task ID, parameters and Google Drive output hashes into the external private review record.",
    `var kansas = ee.FeatureCollection('${KANSAS_BOUNDARY}').filter(ee.Filter.eq('STATEFP', '20')).geometry();`,
    "var sample = ee.Geometry.Rectangle([-99.5, 38.2, -99.3, 38.4], null, false).intersection(kansas, ee.ErrorMargin(1));",
    `var region = ${scope === "sample" ? "sample" : "kansas"};`,
    `var source = ee.ImageCollection('${catalog.asset}').filterBounds(region).sort('system:index');`,
  ];
  if (id !== "ee-3dep") lines.push("source = source.filterDate('2024-01-01', '2025-01-01');");
  lines.push(
    "print('Input collection count', source.size());",
    "print('All source image IDs (export this list for the review record)', source.aggregate_array('system:id'));",
    "print('Input time starts', source.aggregate_array('system:time_start'));",
    "print('Input footprints and properties', source);",
  );
  if (id === "ee-cdl") lines.push(
    "// One annual categorical raster; nearest-neighbor sampling only.",
    "if (source.size().getInfo() !== 1) throw new Error('Expected exactly one 2024 CDL source image. Export held.');",
    "var image = ee.Image(source.first()).select('cropland').rename('crop_class').toUint16();",
    "print('Expected one 2024 CDL image', source.size());",
    "print('CDL class histogram in validation sample', image.reduceRegion({reducer: ee.Reducer.frequencyHistogram(), geometry: sample, scale: 30, maxPixels: 1e8}));",
  );
  if (id === "ee-chirps") lines.push(
    "// 2024 has 366 daily periods. Mask pixels missing any daily observation.",
    "var expected = 366;",
    "var periods = source.aggregate_array('system:time_start').map(function(t) { return ee.Date(t).format('YYYY-MM-dd'); }).distinct().size();",
    "print('Expected 366 images and unique dates', source.size(), periods);",
    "if (source.size().getInfo() !== expected || periods.getInfo() !== expected) throw new Error('CHIRPS 2024 time coverage is incomplete or duplicated. Export held.');",
    "var values = source.select('precipitation');",
    "var image = values.sum().updateMask(values.count().eq(expected)).rename('annual_precip_mm').toFloat().addBands(values.count().rename('retained_count').toFloat());",
    "print('Retained-observation count', values.count());",
  );
  if (id === "ee-terraclimate") lines.push(
    "// 12 monthly periods. PDSI source scale factor is 0.01; index is unitless.",
    "var expected = 12;",
    "var periods = source.aggregate_array('system:time_start').map(function(t) { return ee.Date(t).format('YYYY-MM'); }).distinct().size();",
    "print('Expected 12 images and unique months', source.size(), periods);",
    "if (source.size().getInfo() !== expected || periods.getInfo() !== expected) throw new Error('TerraClimate 2024 time coverage is incomplete or duplicated. Export held.');",
    "var values = source.select('pdsi');",
    "var image = values.mean().multiply(0.01).updateMask(values.count().eq(expected)).rename('annual_mean_pdsi').toFloat().addBands(values.count().rename('retained_count').toFloat());",
    "print('Retained-observation count', values.count());",
  );
  if (id === "ee-sentinel2") lines.push(
    "// SCL 4 vegetation, 5 bare soil and 6 water. Cloud, shadow, snow and unclassified pixels are held.",
    "if (source.size().getInfo() < 1) throw new Error('No 2024 Sentinel-2 source images. Export held.');",
    "var clean = source.map(function(scene) {",
    "  var scl = scene.select('SCL');",
    "  var good = scl.eq(4).or(scl.eq(5)).or(scl.eq(6));",
    "  return scene.select(['B4','B3','B2']).multiply(0.0001).updateMask(good).resample('bilinear');",
    "});",
    "var image = clean.median().rename(['red','green','blue']).toFloat().addBands(clean.select(0).count().rename('retained_count').toFloat());",
    "print('Retained per-pixel observation count', clean.select(0).count());",
  );
  if (id === "ee-3dep") lines.push(
    "// Deterministically ordered mosaic; source acquisition dates and vertical datum may differ.",
    "if (source.size().getInfo() < 1) throw new Error('No 3DEP source images. Export held.');",
    "var image = source.select('elevation').map(function(tile) { return tile.resample('bilinear'); }).mosaic().rename('elevation_m').toFloat();",
    "print('Source acquisition metadata; review mixed dates and vertical datum before approval', source);",
  );
  lines.push(
    "print('Output band names and source projection', image.bandNames(), image.projection());",
    "print('Validation sample non-null pixel count', image.reduceRegion({reducer: ee.Reducer.count(), geometry: sample, scale: " + (highResolution ? "30" : "5000") + ", maxPixels: 1e8}));",
    "Map.centerObject(region, " + (scope === "sample" ? "10" : "7") + ");",
    "Map.addLayer(" + (id === "ee-sentinel2" ? "image.select(['red','green','blue'])" : "image.select(0)") + ".clip(region), " + (id === "ee-cdl" ? "{}" : id === "ee-sentinel2" ? "{min:0,max:0.3}" : id === "ee-3dep" ? "{min:200,max:1300}" : id === "ee-chirps" ? "{min:0,max:1200}" : "{min:-5,max:5}") + ", 'Export candidate · review only');",
    "// Export remains a manual Code Editor task. Confirm source count and time periods before clicking Run.",
    "// A completed task is not approval: inspect the GeoTIFF and record its SHA-256 outside Git.",
  );
  const noData = id === "ee-cdl" ? "65535" : "-9999";
  const projection = highResolution
    ? `crs: '${GRID_30M.crs}', crsTransform: ${JSON.stringify(GRID_30M.crsTransform)},`
    : `crs: 'EPSG:4326', crsTransform: ${JSON.stringify(NATIVE_CLIMATE_GRIDS[id as keyof typeof NATIVE_CLIMATE_GRIDS])},`;
  lines.push(
    "Export.image.toDrive({",
    `  image: image.clip(region).unmask({value: ${noData}, sameFootprint: false}),`,
    `  description: '${name}', fileNamePrefix: '${name}', folder: 'KFM_EE_Review',`,
    "  region: region,",
    `  ${projection}`,
    ...(scope === "statewide" && highResolution ? ["  fileDimensions: 2048, // Small GeoTIFF shards for complete private retrieval; retain every shard."] : []),
    "  maxPixels: 1e13, fileFormat: 'GeoTIFF', formatOptions: {cloudOptimized: true, noData: " + noData + "}",
    "});",
    "",
  );
  return lines.join("\n");
}
