import { EARTH_ENGINE_DATASETS, EARTH_ENGINE_DISPLAY_RAMPS, EARTH_ENGINE_REFLECTANCE_VIS, KANSAS_BOUNDARY, earthEngineUrl, earthEngineVisParams } from "./earth-engine-data";
import { EARTH_ENGINE_CONTEXT_LAYERS, EARTH_ENGINE_SOURCE_YEARS, type EarthEngineContextLayerId } from "./earth-engine-context";

export type EarthEngineExportScope = "sample" | "statewide";
const GRID_30M = { crs: "EPSG:5070", crsTransform: [30, 0, -1200000, 0, -30, 2400000] };
export const EARTH_ENGINE_EXPORT_GRID = Object.freeze(GRID_30M);
// PRISM ANm/ANd projection read directly from authenticated GEE metadata on 2026-10-06.
export const PRISM_NATIVE_GRID = { crs: "EPSG:4269", crsTransform: [0.041666666667, 0, -125.0208333333335, 0, -0.041666666667, 49.9375000000005] } as const;
const NATIVE_CLIMATE_GRIDS = {
  "ee-prism-monthly": PRISM_NATIVE_GRID.crsTransform,
  "ee-prism-daily": PRISM_NATIVE_GRID.crsTransform,
  "ee-chirps": [0.05, 0, -180, 0, -0.05, 50],
  "ee-terraclimate": [1 / 24, 0, -180, 0, -(1 / 24), 90],
} as const;

export function buildEarthEngineExportRecipe(id: EarthEngineContextLayerId, scope: EarthEngineExportScope, year?: number): string {
  const selected = EARTH_ENGINE_CONTEXT_LAYERS.find((layer) => layer.id === id);
  const catalog = EARTH_ENGINE_DATASETS.find((layer) => layer.id === id);
  if (!selected || !catalog || !["sample", "statewide"].includes(scope)) throw new Error("Choose a supported display preparation product.");
  const bounds = EARTH_ENGINE_SOURCE_YEARS[id];
  if (bounds ? !Number.isInteger(year) || year! < bounds[0] || year! > bounds[1] : year !== undefined) throw new Error("Choose a supported source year; elevation has mixed acquisition dates.");
  const endYear = year === undefined ? undefined : year + 1;
  const dayCount = year === undefined ? undefined : (Date.UTC(endYear!, 0, 1) - Date.UTC(year, 0, 1)) / 86_400_000;
  const landsat = /^ee-landsat[45789]$/.test(id);
  const rgb = landsat || id === "ee-sentinel2";
  const highResolution = landsat || id === "ee-cdl" || id === "ee-sentinel2" || id === "ee-3dep";
  const name = `kfm_${id.replaceAll("-", "_")}_${year ?? "mixed_dates"}_${scope}`;
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
  if (id.startsWith("ee-prism-")) lines.push(
    "// PRISM dates use the provider's native day/month labels. A daily label ends its noon-UTC observation interval.",
    `source = source.filter(ee.Filter.gte('system:index', '${year}${id === "ee-prism-daily" ? "0101" : "01"}')).filter(ee.Filter.lt('system:index', '${endYear}${id === "ee-prism-daily" ? "0101" : "01"}'));`,
    `var expectedProjection = ee.Projection('${PRISM_NATIVE_GRID.crs}', ${JSON.stringify(PRISM_NATIVE_GRID.crsTransform)});`,
    "source = source.map(function(scene) {",
    "  var native = scene.select('ppt').projection();",
    "  var sameCrs = ee.Algorithms.IsEqual(native.crs(), expectedProjection.crs());",
    "  var sameTransform = ee.Algorithms.IsEqual(native.transform(), expectedProjection.transform());",
    "  return scene.set('kfm_native_grid_ok', ee.Algorithms.If(sameCrs, ee.Algorithms.If(sameTransform, 1, 0), 0));",
    "});",
    "if (source.aggregate_min('kfm_native_grid_ok').getInfo() !== 1) throw new Error('PRISM native grid differs or no scenes exist. Export held; inspect source projections.');",
  );
  else if (year !== undefined) lines.push(`source = source.filterDate('${year}-01-01', '${endYear}-01-01');`);
  lines.push(
    "print('Input collection count', source.size());",
    "print('Source image IDs (console lists truncate; the CSV task below holds the complete inventory)', source.aggregate_array('system:id'));",
    "print('Input time starts', source.aggregate_array('system:time_start'));",
    "print('Input footprints and properties', source);",
    "// Complete source inventory for exports/<layer>/source_ids.csv; its task ID is the review's sourceInventoryTaskId.",
    "Export.table.toDrive({",
    "  collection: ee.FeatureCollection(source.map(function(scene) {",
    "    return ee.Feature(null, {source_image_id: scene.get('system:id'), time_start_ms: scene.get('system:time_start')});",
    "  })),",
    `  description: '${name}_source_ids', fileNamePrefix: '${name}_source_ids', folder: 'KFM_EE_Review',`,
    "  fileFormat: 'CSV', selectors: ['source_image_id', 'time_start_ms']",
    "});",
  );
  if (id === "ee-cdl") lines.push(
    "// One annual categorical raster; nearest-neighbor sampling only.",
    `if (source.size().getInfo() !== 1) throw new Error('Expected exactly one ${year} CDL source image. Export held.');`,
    "var image = ee.Image(source.first()).select('cropland').rename('crop_class').toUint16();",
    `print('Expected one ${year} CDL image', source.size());`,
    "print('CDL class histogram in validation sample', image.reduceRegion({reducer: ee.Reducer.frequencyHistogram(), geometry: sample, scale: 30, maxPixels: 1e8}));",
  );
  if (id === "ee-chirps") lines.push(
    `// ${year} has ${dayCount} daily periods. Mask pixels missing any daily observation.`,
    `var expected = ${dayCount};`,
    "var periods = source.aggregate_array('system:time_start').map(function(t) { return ee.Date(t).format('YYYY-MM-dd'); }).distinct().size();",
    `print('Expected ${dayCount} images and unique dates', source.size(), periods);`,
    `if (source.size().getInfo() !== expected || periods.getInfo() !== expected) throw new Error('CHIRPS ${year} time coverage is incomplete or duplicated. Export held.');`,
    "var values = source.select('precipitation');",
    "var image = values.sum().updateMask(values.count().eq(expected)).rename('annual_precip_mm').toFloat().addBands(values.count().rename('retained_count').toFloat());",
    "print('Retained-observation count', values.count());",
  );
  if (id === "ee-prism-monthly" || id === "ee-prism-daily") lines.push(
    "// Retain the observed native NAD83 grid; do not relabel it as WGS84.",
    `var expected = ${id === "ee-prism-daily" ? dayCount : 12};`,
    "var periods = source.aggregate_array('system:index').distinct().size();",
    `if (source.size().getInfo() !== expected || periods.getInfo() !== expected) throw new Error('PRISM ${year} time coverage is incomplete or duplicated. Export held.');`,
    "var values = source.select('ppt');",
    "var image = values.sum().updateMask(values.count().eq(expected)).rename('annual_precip_mm').toFloat().addBands(values.count().rename('retained_count').toFloat());",
    "print('Retained-observation count; source revisions and station-network limitations apply', values.count());",
  );
  if (id === "ee-terraclimate") lines.push(
    "// 12 monthly periods. PDSI source scale factor is 0.01; index is unitless.",
    "var expected = 12;",
    "var periods = source.aggregate_array('system:time_start').map(function(t) { return ee.Date(t).format('YYYY-MM'); }).distinct().size();",
    "print('Expected 12 images and unique months', source.size(), periods);",
    `if (source.size().getInfo() !== expected || periods.getInfo() !== expected) throw new Error('TerraClimate ${year} time coverage is incomplete or duplicated. Export held.');`,
    "var values = source.select('pdsi');",
    "var image = values.mean().multiply(0.01).updateMask(values.count().eq(expected)).rename('annual_mean_pdsi').toFloat().addBands(values.count().rename('retained_count').toFloat());",
    "print('Retained-observation count', values.count());",
  );
  if (id === "ee-sentinel2") lines.push(
    "// SCL 4 vegetation, 5 bare soil and 6 water. Cloud, shadow, snow and unclassified pixels are held.",
    `if (source.size().getInfo() < 1) throw new Error('No ${year} Sentinel-2 source images. Export held.');`,
    "var clean = source.map(function(scene) {",
    "  var scl = scene.select('SCL');",
    "  var good = scl.eq(4).or(scl.eq(5)).or(scl.eq(6));",
    "  return scene.select(['B4','B3','B2']).multiply(0.0001).updateMask(good).resample('bilinear');",
    "});",
    "var image = clean.median().rename(['red','green','blue']).toFloat().addBands(clean.select(0).count().rename('retained_count').toFloat());",
    "print('Retained per-pixel observation count', clean.select(0).count());",
  );
  if (landsat) lines.push(
    "// QA_PIXEL bits 0–5: fill, dilated cloud, cirrus (unused in TM/ETM+), cloud, shadow, snow.",
    "// QA_RADSAT == 0 also rejects saturation and dropped pixels. No SLC gap filling or cross-sensor harmonization.",
    `if (source.size().getInfo() < 1) throw new Error('No ${year} Landsat source images. Export held.');`,
    "var clean = source.map(function(scene) {",
    "  var good = scene.select('QA_PIXEL').bitwiseAnd(63).eq(0).and(scene.select('QA_RADSAT').eq(0));",
    `  return scene.select(${/^ee-landsat[457]$/.test(id) ? "['SR_B3','SR_B2','SR_B1']" : "['SR_B4','SR_B3','SR_B2']"}).multiply(0.0000275).add(-0.2).updateMask(good).resample('bilinear');`,
    "});",
    "var image = clean.median().rename(['red','green','blue']).toFloat().addBands(clean.select(0).count().rename('retained_count').toFloat());",
    "print('Retained per-pixel observation count; partial mission years and gaps remain explicit', clean.select(0).count());",
  );
  if (id === "ee-3dep") lines.push(
    "// Deterministically ordered mosaic; source acquisition dates and vertical datum may differ.",
    "if (source.size().getInfo() < 1) throw new Error('No 3DEP source images. Export held.');",
    "var image = source.select('elevation').map(function(tile) { return tile.resample('bilinear'); }).mosaic().rename('elevation_m').toFloat();",
    "print('Source acquisition metadata; review mixed dates and vertical datum before approval', source);",
  );
  const noData = id === "ee-cdl" ? "65535" : "-9999";
  const projection = highResolution
    ? `crs: '${GRID_30M.crs}', crsTransform: ${JSON.stringify(GRID_30M.crsTransform)},`
    : `crs: '${id.startsWith("ee-prism-") ? PRISM_NATIVE_GRID.crs : "EPSG:4326"}', crsTransform: ${JSON.stringify(NATIVE_CLIMATE_GRIDS[id as keyof typeof NATIVE_CLIMATE_GRIDS])},`;
  // Previews use the installed tile styling. CDL keeps its source band name so Earth Engine
  // applies the catalog class palette; the renamed uint16 band would stretch to black.
  const preview = id === "ee-cdl" ? "ee.Image(source.first()).select('cropland')" : rgb ? "image.select(['red','green','blue'])" : "image.select(0)";
  const vis = id === "ee-cdl" ? "{}" : rgb ? EARTH_ENGINE_REFLECTANCE_VIS : earthEngineVisParams(EARTH_ENGINE_DISPLAY_RAMPS[id]);
  lines.push(
    "print('Output band names and source projection', image.bandNames(), image.projection());",
    `print('Validation sample non-null pixel count on the export grid', image.reduceRegion({reducer: ee.Reducer.count(), geometry: sample, ${projection} maxPixels: 1e8}));`,
    "Map.centerObject(region, " + (scope === "sample" ? "10" : "7") + ");",
    `Map.addLayer(${preview}.clip(region), ${vis}, 'Export candidate · review only');`,
    "// Export remains a manual Code Editor task. Confirm source count and time periods before clicking Run.",
    "// A completed task is not approval: inspect the GeoTIFF and record its SHA-256 outside Git.",
  );
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
