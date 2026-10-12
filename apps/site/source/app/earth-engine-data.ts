// Site-local discovery metadata, not a canonical KFM SourceDescriptor or admission record.
export const EARTH_ENGINE_CHECKED_AT = "2026-10-06";
export const EARTH_ENGINE_CATALOG = "https://developers.google.com/earth-engine/datasets/catalog";
export const EARTH_ENGINE_ACCESS = "https://developers.google.com/earth-engine/guides/access";
export const KANSAS_BOUNDARY = "TIGER/2018/States";
export const EARTH_ENGINE_REVIEW = "Review source assets, coverage, QA, reuse terms, sensitivity, transformations, integrity and provenance; then use KFM steward review and separate admission and release gates.";

export type EarthEngineDataset = Readonly<{
  id: string; asset: string; title: string; provider: string; topic: string;
  resolution: string; cadence: string; coverage: string; catalogSlug: string;
  use: string; limitation: string; terms: string; recipe: string;
  firstYear: number | null; lastYear: number | null;
  temporalMode: "annual" | "period-summary" | "source-mosaic";
  recipeKind?: "inventory";
}>;

export const EARTH_ENGINE_DATASETS: readonly EarthEngineDataset[] = Object.freeze([
  { id: "ee-cdl", asset: "USDA/NASS/CDL", title: "Cropland Data Layer", provider: "USDA NASS", topic: "Agriculture", resolution: "30 m", cadence: "Annual · harvest year", coverage: "Catalog: 1997–2024; recipes: 2008–2024", catalogSlug: "USDA_NASS_CDL", use: "Inspect crop classifications across Kansas and prepare annual crop-pattern studies.", limitation: "Classification is not a field survey or yield estimate. Check state/year accuracy; winter wheat can be planted the prior year. Recipe coverage is not verified pixel availability.", terms: "Public domain; acknowledge USDA NASS and the product year.", recipe: "Annual cropland classes", firstYear: 2008, lastYear: 2024, temporalMode: "annual" },
  { id: "ee-dynamic-world", asset: "GOOGLE/DYNAMICWORLD/V1", title: "Dynamic World", provider: "Google / World Resources Institute", topic: "Land cover", resolution: "10 m", cadence: "Scene-based · cloud dependent", coverage: "From 2015-06-27; ongoing catalog", catalogSlug: "GOOGLE_DYNAMICWORLD_V1", use: "Explore nine land-cover classes and their predicted probabilities.", limitation: "Model predictions need validation. A 0.6 probability screen in the recipe is an exploratory choice; it does not establish accuracy or change on the ground.", terms: "CC BY 4.0; preserve the attribution and Sentinel notice on the catalog page.", recipe: "Probability-screened annual class mode", firstYear: 2015, lastYear: 2025, temporalMode: "annual" },
  { id: "ee-landsat8", asset: "LANDSAT/LC08/C02/T1_L2", title: "Landsat 8 surface reflectance", provider: "USGS", topic: "Imagery", resolution: "30 m reflectance", cadence: "16-day revisit · cloud dependent", coverage: "From 2013-03-18; ongoing catalog", catalogSlug: "LANDSAT_LC08_C02_T1_L2", use: "Inspect annual natural-color composites with Landsat quality flags and reflectance scaling.", limitation: "Annual medians mix acquisition dates. Clouds and masking leave gaps; surface reflectance is not air temperature or proof of land-use change.", terms: "Public domain; acknowledge the U.S. Geological Survey.", recipe: "QA-masked annual RGB median", firstYear: 2013, lastYear: 2025, temporalMode: "annual" },
  { id: "ee-sentinel2", asset: "COPERNICUS/S2_SR_HARMONIZED", title: "Sentinel-2 harmonized reflectance", provider: "European Union / ESA / Copernicus", topic: "Imagery", resolution: "10 m RGB · 20 m scene classes", cadence: "Multi-day revisit · cloud dependent", coverage: "From 2017-03-28; early coverage incomplete", catalogSlug: "COPERNICUS_S2_SR_HARMONIZED", use: "Inspect natural-color Kansas imagery using harmonized reflectance values.", limitation: "Recipe retains SCL vegetation, bare-soil and water pixels only. Snow and unclassified pixels are excluded; median imagery does not prove a dated event.", terms: "Copernicus Sentinel terms apply; retain the required attribution and notices.", recipe: "SCL-screened annual RGB median", firstYear: 2017, lastYear: 2025, temporalMode: "annual" },
  { id: "ee-surface-water", asset: "JRC/GSW1_4/GlobalSurfaceWater", title: "Global Surface Water v1.4", provider: "EC Joint Research Centre / Google", topic: "Water", resolution: "30 m", cadence: "Fixed historical summary", coverage: "1984-03-16 through 2021-12-31", catalogSlug: "JRC_GSW1_4_GlobalSurfaceWater", use: "Examine historical water occurrence as a percentage of observations.", limitation: "This image summarizes 1984–2021. It is not current flood extent, streamflow or a selectable annual observation. Never-observed water areas may be masked.", terms: "Copernicus reuse conditions; acknowledge the source and cited study as directed by the catalog.", recipe: "Historical water occurrence", firstYear: null, lastYear: null, temporalMode: "period-summary" },
  { id: "ee-chirps", asset: "UCSB-CHG/CHIRPS/DAILY", title: "CHIRPS daily precipitation v2", provider: "UCSB Climate Hazards Center", topic: "Climate", resolution: "0.05° · about 5.6 km", cadence: "Daily", coverage: "From 1981; catalog end observed 2026-08-31", catalogSlug: "UCSB-CHG_CHIRPS_DAILY", use: "Prepare annual rainfall totals with daily completeness checks.", limitation: "Gridded satellite/station estimates are not a local rain gauge or warning service. A complete time axis does not prove pixel accuracy.", terms: "Public domain; cite the CHIRPS dataset and Funk et al. (2015).", recipe: "Complete-year precipitation sum · mm", firstYear: 1981, lastYear: 2025, temporalMode: "annual" },
  { id: "ee-terraclimate", asset: "IDAHO_EPSCOR/TERRACLIMATE", title: "TerraClimate drought index", provider: "University of Idaho / University of California, Merced", topic: "Climate", resolution: "About 4.6 km", cadence: "Monthly", coverage: "1958–2024; last listed month December 2024", catalogSlug: "IDAHO_EPSCOR_TERRACLIMATE", use: "Explore annual mean Palmer Drought Severity Index from twelve monthly modeled grids.", limitation: "A modeled regional index is not measured soil moisture or a local drought declaration. Fine-scale patterns and trends inherit parent-data limitations.", terms: "CC0 public domain; retain the provider and study citation.", recipe: "Twelve-month mean PDSI · scaled by 0.01", firstYear: 1958, lastYear: 2024, temporalMode: "annual" },
  { id: "ee-3dep", asset: "USGS/3DEP/10m_collection", title: "3DEP elevation collection", provider: "USGS", topic: "Terrain", resolution: "1/3 arc-second · about 10 m", cadence: "Source mosaic · mixed acquisition dates", coverage: "Catalog metadata span: 1924–2022; not annual coverage", catalogSlug: "USGS_3DEP_10m_collection", use: "Preview Kansas elevation in meters using the replacement for the deprecated single-image asset.", limitation: "Source dates and vertical datum require inspection. A mosaic is not annual terrain change, raw LiDAR or survey-grade evidence.", terms: "Generally U.S. public domain; review source metadata and credit USGS.", recipe: "Deterministically ordered elevation mosaic", firstYear: null, lastYear: null, temporalMode: "source-mosaic" },
  ...([
    ["4", "LT04", 1982, 1993, "TM", "Acquisition dates 1982–1993; first and last years are partial."],
    ["5", "LT05", 1984, 2012, "TM", "Acquisition dates 1984–2012; first and last years are partial."],
    ["7", "LE07", 1999, 2024, "ETM+", "Scan-line corrector failure from 2003 leaves gaps; no gap filling or cross-sensor harmonization is implied."],
    ["9", "LC09", 2021, 2025, "OLI-2", "From October 2021; first year is partial. Current partial year remains available in the provider catalog."],
  ] as const).map(([mission, code, firstYear, lastYear, sensor, limit]) => ({
    id: `ee-landsat${mission}`, asset: `LANDSAT/${code}/C02/T1_L2`, title: `Landsat ${mission} surface reflectance`, provider: "USGS", topic: "Imagery",
    resolution: "30 m reflectance", cadence: "Scene-based · cloud dependent", coverage: `${firstYear}–${lastYear} recipe years · ${sensor}`,
    catalogSlug: `LANDSAT_${code}_C02_T1_L2`, use: "Inspect sensor-specific, quality-screened historical Kansas imagery.",
    limitation: `${limit} Annual medians mix source dates. Sensor transitions are not measured environmental change.`,
    terms: "Public domain; acknowledge USGS. Exclude requester-pays cloud mirrors.", recipe: `${sensor} QA-masked annual RGB median`, firstYear, lastYear, temporalMode: "annual" as const,
  })),
  { id: "ee-landsat-mss", asset: "LANDSAT/LM01/C02/T1", title: "Landsat 1 MSS historical inventory", provider: "USGS", topic: "Imagery", resolution: "MSS sensor bands · 60 m nominal", cadence: "Scene-based", coverage: "1972-07-26–1978-01-06", catalogSlug: "LANDSAT_LM01_C02_T1", use: "Find the earliest Landsat scenes for Kansas; inspect scene IDs before ordering data.", limitation: "Raw digital numbers are not surface reflectance. No natural-color preview, harmonized trend or continuity across MSS missions is claimed.", terms: "Public domain; acknowledge USGS. Exclude requester-pays cloud mirrors.", recipe: "Source inventory only · no derived raster", recipeKind: "inventory", firstYear: 1972, lastYear: 1978, temporalMode: "annual" },
  ...([ ["monthly", "ANm", 1895], ["daily", "ANd", 1981] ] as const).map(([cadence, asset, firstYear]) => ({
    id: `ee-prism-${cadence}`, asset: `OREGONSTATE/PRISM/${asset}`, title: `PRISM ${cadence} precipitation`, provider: "PRISM Climate Group / Oregon State University", topic: "Climate",
    resolution: "About 4 km", cadence: cadence === "daily" ? "Daily" : "Monthly", coverage: `${firstYear} onward · contiguous United States`, catalogSlug: `OREGONSTATE_PRISM_${asset}`,
    use: "Inspect full-period Kansas precipitation history with explicit completeness checks.", limitation: "Do not use for century-long climate trends: non-climatic station/network changes affect the record. Current data may be revised; estimates are not local gauge observations.",
    terms: "PRISM reuse terms apply; retain PRISM Climate Group attribution and source revision.", recipe: "Complete-year precipitation sum · mm", firstYear, lastYear: 2025, temporalMode: "annual" as const,
  })),
  ...([ ["ee-era5", "ECMWF/ERA5/HOURLY", "ERA5", 1940, "Global atmosphere · about 28 km"], ["ee-era5-land", "ECMWF/ERA5_LAND/HOURLY", "ERA5-Land", 1950, "Global land · about 11 km"] ] as const).map(([id, asset, title, firstYear, resolution]) => ({
    id, asset, title: `${title} hourly reanalysis inventory`, provider: "ECMWF / Copernicus", topic: "Climate", resolution, cadence: "Hourly", coverage: `${firstYear} onward · reanalysis`, catalogSlug: asset.replaceAll("/", "_"),
    use: "Discover the complete supported history before selecting variables and export volumes.", limitation: "Reanalysis is modeled context, not station observations. Accumulation conventions and ERA5-Land's documented evapotranspiration component issue require product-specific validation.",
    terms: "Copernicus C3S licence and attribution apply.", recipe: "Source inventory only · choose variables before export", recipeKind: "inventory" as const, firstYear, lastYear: 2025, temporalMode: "annual" as const,
  })),
].map((item) => Object.freeze(item)) as EarthEngineDataset[]);

export const earthEngineUrl = (dataset: EarthEngineDataset) => `${EARTH_ENGINE_CATALOG}/${dataset.catalogSlug}`;

// Display ramps shared by Code Editor previews, the map legend and the tile renderer
// (scripts/earth-engine/prepare_display_set.py keeps an identical copy; a test compares them).
export type EarthEngineRamp = Readonly<{ stops: readonly number[]; colors: readonly string[] }>;
export const EARTH_ENGINE_DISPLAY_RAMPS: Readonly<Record<string, EarthEngineRamp>> = Object.freeze({
  "ee-chirps": { stops: [0, 600, 1200], colors: ["#fff4c2", "#79c9bc", "#235ca8"] },
  "ee-prism-monthly": { stops: [0, 600, 1200], colors: ["#fff4c2", "#79c9bc", "#235ca8"] },
  "ee-prism-daily": { stops: [0, 600, 1200], colors: ["#fff4c2", "#79c9bc", "#235ca8"] },
  "ee-terraclimate": { stops: [-5, 0, 5], colors: ["#a63603", "#f6eedb", "#0868ac"] },
  "ee-3dep": { stops: [200, 600, 900, 1300], colors: ["#28594e", "#c4c98a", "#a67e54", "#efe7d4"] },
});
// Natural-color stretch used by the tile renderer: reflectance 0–0.3 with gamma 1.2.
export const EARTH_ENGINE_REFLECTANCE_VIS = "{min: 0, max: 0.3, gamma: 1.2}";

const gcd = (a: number, b: number): number => b ? gcd(b, a % b) : a;
const hexChannels = (color: string) => [1, 3, 5].map((i) => parseInt(color.slice(i, i + 2), 16));
// Earth Engine spaces palette colors evenly between min and max. Sampling the
// piecewise ramp at the common stop spacing reproduces unevenly spaced stops exactly.
export function earthEnginePalette(ramp: EarthEngineRamp): string[] {
  const first = ramp.stops[0], last = ramp.stops[ramp.stops.length - 1];
  const step = ramp.stops.slice(1).reduce((value, stop, i) => gcd(value, stop - ramp.stops[i]), 0);
  const palette: string[] = [];
  for (let value = first; value <= last; value += step) {
    const segment = Math.max(0, ramp.stops.findIndex((stop, i) => i > 0 && value <= stop) - 1);
    const t = (value - ramp.stops[segment]) / (ramp.stops[segment + 1] - ramp.stops[segment]);
    const [a, b] = [hexChannels(ramp.colors[segment]), hexChannels(ramp.colors[segment + 1])];
    palette.push(a.map((channel, i) => Math.round(channel + (b[i] - channel) * t).toString(16).padStart(2, "0")).join(""));
  }
  return palette;
}
export function earthEngineVisParams(ramp: EarthEngineRamp): string {
  return `{min: ${ramp.stops[0]}, max: ${ramp.stops[ramp.stops.length - 1]}, palette: ${JSON.stringify(earthEnginePalette(ramp)).replaceAll('"', "'").replaceAll(",", ", ")}}`;
}
export function earthEngineLegendGradient(ramp: EarthEngineRamp): string {
  const first = ramp.stops[0], span = ramp.stops[ramp.stops.length - 1] - first;
  return `linear-gradient(90deg, ${ramp.colors.map((color, i) => `${color} ${Math.round((ramp.stops[i] - first) / span * 1000) / 10}%`).join(", ")})`;
}
export function findEarthEngineDatasets(query: string, topic = "All") {
  const words = query.trim().toLowerCase().split(/\s+/).filter(Boolean);
  return EARTH_ENGINE_DATASETS.filter((d) => (topic === "All" || d.topic === topic) && words.every((word) => `${d.title} ${d.asset} ${d.provider} ${d.topic} ${d.use}`.toLowerCase().includes(word)));
}

function checkedRequest(id: string, year?: number) {
  const dataset = EARTH_ENGINE_DATASETS.find((d) => d.id === id);
  if (!dataset) throw new Error("Choose a listed Earth Engine dataset.");
  if (dataset.temporalMode === "annual" && (!Number.isInteger(year) || year! < dataset.firstYear! || year! > dataset.lastYear!)) {
    throw new Error(`Choose a supported recipe year from ${dataset.firstYear} to ${dataset.lastYear}.`);
  }
  if (dataset.temporalMode !== "annual" && year !== undefined) throw new Error("This product has no selectable observation year.");
  return dataset;
}

export function earthEngineReviewPacket(id: string, year?: number) {
  const dataset = checkedRequest(id, year);
  return {
    kind: "kfm-earth-engine-discovery-draft", version: 1,
    status: "PROPOSED", execution: "NOT_RUN", admission: "NOT_ADMITTED", release: "NOT_RELEASED",
    metadataCheckedAt: EARTH_ENGINE_CHECKED_AT, dataset, catalogUrl: earthEngineUrl(dataset),
    scope: { boundaryAsset: KANSAS_BOUNDARY, stateFips: "20", boundaryEdition: "2018", note: "Kansas study boundary, not a current legal boundary" },
    requestedPeriod: dataset.temporalMode === "annual" ? { startInclusive: `${year}-01-01`, endExclusive: `${year! + 1}-01-01` } : null,
    processing: dataset.recipe, recipeVersion: 1,
    unresolved: ["Authenticated execution", "Exact input asset IDs and retrieval times", "Pixel coverage and scientific validation", "Rights and sensitivity review", "Integrity and EvidenceBundle linkage", "Separate review, admission and release decisions"],
    nextStep: EARTH_ENGINE_REVIEW,
  };
}

// Downloads contain inert script text. KFM never evaluates it or calls Earth Engine.
export function buildEarthEngineRecipe(id: string, year?: number): string {
  const d = checkedRequest(id, year);
  const lines = [
    "// KFM exploratory recipe v1 — NOT RUN; NOT ADMITTED; NOT RELEASED.",
    `// ${d.title} — ${earthEngineUrl(d)}`,
    `// Catalog metadata checked ${EARTH_ENGINE_CHECKED_AT}; this is not a data retrieval timestamp.`,
    `// ${d.terms}`, `// ${d.limitation}`,
    "// Run manually in https://code.earthengine.google.com/ with registered project access.",
    "// No export, upload, asset write or KFM promotion is performed.",
    `var states = ee.FeatureCollection('${KANSAS_BOUNDARY}');`,
    "var kansas = states.filter(ee.Filter.eq('STATEFP', '20')).geometry();",
    "Map.centerObject(kansas, 7);",
    "Map.addLayer(kansas, {color: 'e8c66b'}, 'Kansas · TIGER 2018 study boundary', false);",
  ];
  const addLayer = (expression: string, vis: string) => [
    `  var result = ${expression};`,
    `  Map.addLayer(result.clip(kansas), ${vis}, ${JSON.stringify(d.recipe + (year ? ` · ${year}` : "") + " · exploratory")});`,
  ];
  if (d.temporalMode === "period-summary") {
    lines.push(`var source = ee.Image('${d.asset}');`, "// This fixed product summarizes 1984–2021; no date filter is applied.",
      ...addLayer("source.select('occurrence')", "{min: 0, max: 100, palette: ['f4f0cf', '49a0cb', '073763']}"),
      "print('Source image', source);", "print('Units', 'Water occurrence (%) across the fixed historical period');");
  } else {
    lines.push(`var collection = ee.ImageCollection('${d.asset}').filterBounds(kansas);`);
    if (d.id.startsWith("ee-prism-")) lines.push(
      "// PRISM daily labels name the ending day of a noon-UTC interval; calendar timestamps would shift boundary days.",
      `collection = collection.filter(ee.Filter.gte('system:index', '${year}${d.id === "ee-prism-daily" ? "0101" : "01"}')).filter(ee.Filter.lt('system:index', '${year! + 1}${d.id === "ee-prism-daily" ? "0101" : "01"}'));`);
    else if (d.temporalMode === "annual") lines.push(`var start = '${year}-01-01';`, `var end = '${year! + 1}-01-01'; // exclusive`, "collection = collection.filterDate(start, end);");
    lines.push("collection = collection.sort('system:index');", "print('Matching source assets', collection.size());",
      "print('Input asset IDs (first 1000; retain complete provenance before release)', collection.limit(1000).aggregate_array('system:index'));",
      "collection.size().evaluate(function(count, error) {",
      "  if (error) { print('SOURCE ERROR — no result', error); return; }",
      "  if (!count) { print('NO DATA — no result; do not substitute another year.'); return; }");
    if (d.id === "ee-cdl") {
      lines.push("  if (count !== 1) { print('REVIEW REQUIRED — expected one annual CDL image.'); return; }",
        ...addLayer("ee.Image(collection.first()).select('cropland')", "{}"));
    } else if (d.id === "ee-dynamic-world") {
      lines.push("  var labels = collection.map(function(image) {",
        "    var confidence = image.select(['water', 'trees', 'grass', 'flooded_vegetation', 'crops', 'shrub_and_scrub', 'built', 'bare', 'snow_and_ice']).reduce(ee.Reducer.max());",
        "    return image.select('label').updateMask(confidence.gte(0.6));", "  });",
        ...addLayer("labels.mode()", "{min: 0, max: 8, palette: ['419bdf', '397d49', '88b053', '7a87c6', 'e49635', 'dfc35a', 'c4281b', 'a59b8f', 'b39fe1']}"),
        "  Map.addLayer(labels.count().clip(kansas), {min: 0, max: 100}, 'Retained observations per pixel', false);");
    } else if (d.recipeKind === "inventory") {
      lines.push("  print('INVENTORY ONLY — inspect dates, bands and metadata; no raster was calculated.');",
        "  print('First source', collection.first());",
        "  print('Source timestamps (first 1000; not complete coverage proof)', collection.limit(1000).aggregate_array('system:time_start'));");
    } else if (/^ee-landsat[45789]$/.test(d.id) || d.id === "ee-sentinel2") {
      lines.push("  var clean = collection.map(function(image) {");
      if (/^ee-landsat[45789]$/.test(d.id)) lines.push(
        "    var mask = image.select('QA_PIXEL').bitwiseAnd(63).eq(0).and(image.select('QA_RADSAT').eq(0));",
        `    return image.select(${/ee-landsat[457]$/.test(d.id) ? "['SR_B3', 'SR_B2', 'SR_B1']" : "['SR_B4', 'SR_B3', 'SR_B2']"}).multiply(0.0000275).add(-0.2).updateMask(mask);`);
      else lines.push("    var scl = image.select('SCL');", "    var mask = scl.eq(4).or(scl.eq(5)).or(scl.eq(6));",
        "    return image.select(['B4', 'B3', 'B2']).multiply(0.0001).updateMask(mask);");
      lines.push("  });", ...addLayer("clean.median()", EARTH_ENGINE_REFLECTANCE_VIS),
        "  Map.addLayer(clean.select(0).count().clip(kansas), {min: 0, max: 50}, 'Retained observations per pixel', false);");
    } else if (d.id === "ee-chirps" || d.id === "ee-terraclimate" || d.id.startsWith("ee-prism-")) {
      const daily = d.id === "ee-chirps" || d.id === "ee-prism-daily";
      const precipitation = d.id !== "ee-terraclimate";
      const expected = daily ? (Date.UTC(year! + 1, 0, 1) - Date.UTC(year!, 0, 1)) / 86400000 : 12;
      lines.push(`  var expected = ${expected};`,
        d.id.startsWith("ee-prism-") ? "  var dateKeys = collection.aggregate_array('system:index').distinct();" : `  var dateKeys = collection.aggregate_array('system:time_start').map(function(time) { return ee.Date(time).format('${daily ? "YYYY-MM-dd" : "YYYY-MM"}'); }).distinct();`,
        "  dateKeys.size().evaluate(function(periods, dateError) {",
        "    if (dateError || count !== expected || periods !== expected) { print('INCOMPLETE OR DUPLICATE TIME COVERAGE — no annual result', dateError || periods); return; }",
        `    var values = collection.select('${d.id.startsWith("ee-prism-") ? "ppt" : daily ? "precipitation" : "pdsi"}');`,
        `    var result = values.${precipitation ? "sum()" : "mean().multiply(0.01)"}.updateMask(values.count().eq(expected));`,
        `    Map.addLayer(result.clip(kansas), ${earthEngineVisParams(EARTH_ENGINE_DISPLAY_RAMPS[d.id] ?? EARTH_ENGINE_DISPLAY_RAMPS["ee-chirps"])}, '${precipitation ? "Annual precipitation sum (mm)" : "Annual mean PDSI"} · ${year} · exploratory');`,
        "    print('Only pixels with every expected observation are displayed.');", "  });");
    } else if (d.id === "ee-3dep") {
      lines.push("  // Order is deterministic, not a claim that the last tile is newest.", "  // Mixed source dates: inspect source metadata and datum before analysis.",
        ...addLayer("collection.select('elevation').mosaic()", earthEngineVisParams(EARTH_ENGINE_DISPLAY_RAMPS[d.id])));
    }
    lines.push("});");
  }
  lines.push(`print('KFM review boundary', ${JSON.stringify(EARTH_ENGINE_REVIEW)});`, "");
  return lines.join("\n");
}
