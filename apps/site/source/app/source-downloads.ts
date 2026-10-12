import type { OfficialContextId } from "./live-context";

const nationalMap = "https://apps.nationalmap.gov/downloader/";
export const SOURCE_DOWNLOADS: Record<OfficialContextId, { href: string; label: string }> = {
"kgs-aquifer-alluvial": { href: "https://services.kansasgis.org/arcgis8/rest/services/wwc5/wwc5_v2/MapServer/4", label: "KGS boundary service" },
"kgs-aquifer-dakota": { href: "https://services.kansasgis.org/arcgis8/rest/services/wwc5/wwc5_v2/MapServer/5", label: "KGS boundary service" },
"kgs-aquifer-glacial-drift": { href: "https://services.kansasgis.org/arcgis8/rest/services/wwc5/wwc5_v2/MapServer/6", label: "KGS boundary service" },
"kgs-aquifer-high-plains": { href: "https://services.kansasgis.org/arcgis8/rest/services/wwc5/wwc5_v2/MapServer/7", label: "KGS boundary service" },
"kgs-aquifer-ozark": { href: "https://services.kansasgis.org/arcgis8/rest/services/wwc5/wwc5_v2/MapServer/8", label: "KGS boundary service" },
"kgs-aquifer-osage": { href: "https://services.kansasgis.org/arcgis8/rest/services/wwc5/wwc5_v2/MapServer/10", label: "KGS boundary service" },
"kgs-aquifer-flint-hills": { href: "https://services.kansasgis.org/arcgis8/rest/services/wwc5/wwc5_v2/MapServer/11", label: "KGS boundary service" },
"kgs-water-table": { href: "/data/groundwater/kgs-water-table.geojson", label: "Download dated KGS GeoJSON snapshot" },
"kgs-saturated-thickness": { href: "/data/groundwater/kgs-saturated-thickness.geojson", label: "Download dated KGS GeoJSON snapshot" },
"kgs-depth-to-water": { href: "/data/groundwater/kgs-depth-to-water.geojson", label: "Download dated KGS GeoJSON snapshot" },
"kgs-monitoring-wells": { href: "/data/groundwater/kgs-monitoring-wells.geojson", label: "Download dated KGS GeoJSON snapshot" },

  "kdot-bridges-state": { href: "https://kanplan.ksdot.gov/arcgis_web_adaptor/rest/services/Structures/State_Bridges/MapServer/0", label: "KDOT provider inventory and fields" },
  "kdot-bridges-local": { href: "https://kanplan.ksdot.gov/arcgis_web_adaptor/rest/services/Structures/Non_State_Bridges/MapServer/0", label: "KDOT provider inventory and fields" },
  "kdot-bridges-historic": { href: "https://kanplan.ksdot.gov/arcgis_web_adaptor/rest/services/Structures/Non_State_Bridges/MapServer/0", label: "KDOT provider inventory and fields" },
  "kdot-bridges-old": { href: "https://kanplan.ksdot.gov/arcgis_web_adaptor/rest/services/Structures/Non_State_Bridges/MapServer/0", label: "KDOT provider inventory and fields" },
  "kdot-bridges-closed": { href: "https://kanplan.ksdot.gov/arcgis_web_adaptor/rest/services/Structures/Non_State_Bridges/MapServer/0", label: "KDOT provider inventory and fields" },
  "kdot-roads-1918": { href: "https://kanplan.ksdot.gov/arcgis_web_adaptor/rest/services/Transportation/Historical_Roads/MapServer/0", label: "KDOT provider inventory and fields" },
  "kdot-roads": { href: "https://kanplan.ksdot.gov/arcgis_web_adaptor/rest/services/Transportation/LRS_County/MapServer/4", label: "KDOT public road reference" },
  "kdot-rail-active": { href: "https://kanplan.ksdot.gov/arcgis_web_adaptor/rest/services/Transportation/Railroads/MapServer/0", label: "KDOT active railroad reference" },
  "kdot-rail-abandoned": { href: "https://kanplan.ksdot.gov/arcgis_web_adaptor/rest/services/Transportation/Railroads/MapServer/1", label: "KDOT abandoned railroad reference" },
  "fema-flood-zones": { href: "https://msc.fema.gov/portal/home", label: "FEMA effective maps and amendments" },

  "fema-disaster-declarations": { href: "https://www.fema.gov/api/open/v2/DisasterDeclarationsSummaries", label: "OpenFEMA declaration records" },
  "blm-plss-townships": { href: "https://gis.blm.gov/arcgis/rest/services/Cadastral/BLM_Natl_PLSS_CadNSDI/MapServer/1", label: "BLM township service" },
  "blm-plss-sections": { href: "https://gis.blm.gov/arcgis/rest/services/Cadastral/BLM_Natl_PLSS_CadNSDI/MapServer/2", label: "BLM section service" },
  "blm-plss-intersected": { href: "https://gis.blm.gov/arcgis/rest/services/Cadastral/BLM_Natl_PLSS_CadNSDI/MapServer/3", label: "BLM intersected division service" },
  "blm-mlrs-leases-authorized": { href: "https://gis.blm.gov/nlsdb/rest/services/Fluid_Minerals/Oil_Gas_Leases_Case_Disp/MapServer/0", label: "BLM MLRS authorized oil and gas lease cases" },
  "blm-mlrs-leases-closed": { href: "https://gis.blm.gov/nlsdb/rest/services/Fluid_Minerals/Oil_Gas_Leases_Case_Disp/MapServer/3", label: "BLM MLRS closed oil and gas lease cases" },
  "nasa-firms-active-fire": { href: "https://gibs.earthdata.nasa.gov/layer-metadata/v1.0/VIIRS_NOAA20_Thermal_Anomalies_375m_All.json", label: "NASA GIBS image source metadata" },
  "nasa-gibs-fire-points": { href: "/api/source-download?source=nasa-gibs-fire-points", label: "Download mapped detections · GeoJSON" },
  "nifc-fire-reports": { href: "/api/source-download?source=nifc-fire-reports", label: "Download recent reports · GeoJSON" },
  "census-counties": { href: "/api/source-download?source=census-counties", label: "Download county baseline · GeoJSON" },
  "usgs-streamflow": { href: "/api/source-download?source=usgs-streamflow", label: "Download current observations · JSON" },
  "noaa-nwps-gauges": { href: "https://water.noaa.gov/about/api", label: "NOAA gauge data & API downloads" },
  "usgs-3dhp-hydrography": { href: nationalMap, label: "Download USGS hydrography" },
  "usgs-wbd-watersheds": { href: nationalMap, label: "Download watershed boundaries" },
  "noaa-nwm-analysis": { href: "https://nomads.ncep.noaa.gov/pub/data/nccf/com/nwm/prod/", label: "Download National Water Model files" },
  "noaa-nwm-short-range": { href: "https://nomads.ncep.noaa.gov/pub/data/nccf/com/nwm/prod/", label: "Download National Water Model files" },
  "usgs-earthquakes": { href: "/api/source-download?source=usgs-earthquakes", label: "Download catalog records · GeoJSON" },
  "noaa-hms-smoke": { href: "/api/source-download?source=noaa-hms-smoke", label: "Download mapped smoke · GeoJSON" },
  "noaa-goes-geocolor": { href: "https://satellitemaps.nesdis.noaa.gov/arcgis/rest/services/MERGEDGC_Last_24hr/ImageServer", label: "NOAA dated GeoColor image catalog" },
  "raspberry-shake-stations": { href: "/api/source-download?source=raspberry-shake-stations", label: "Download station metadata · GeoJSON" },
  "usgs-3dep-hillshade": { href: nationalMap, label: "Download source elevation data" },
  "usgs-3dep-slope": { href: nationalMap, label: "Download source elevation data" },
  "nws-alerts": { href: "/api/source-download?source=nws-alerts", label: "Download current alerts · GeoJSON" },
  "nws-radar": { href: "https://www.ncei.noaa.gov/products/radar/next-generation-weather-radar", label: "NOAA radar archive & downloads" },
  "nws-forecast-wind": { href: "https://open-meteo.com/en/docs/gfs-api", label: "GFS model forecast documentation" },
  "nasa-lightning-climatology": { href: "https://gibs.earthdata.nasa.gov/layer-metadata/v1.0/LIS_High_Resolution_Full_Climatology_Combined_Flash_Rate_Climatology.json", label: "NASA climatology source metadata" },
  "noaa-lightning-density": { href: "https://nowcoast.noaa.gov/geoserver/observations/lightning_detection/ows?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetCapabilities", label: "NOAA lightning density capabilities" },
};

const ARCHIVE_DOWNLOAD_SOURCES = new Set<OfficialContextId>(["usgs-earthquakes", "noaa-hms-smoke", "nasa-gibs-fire-points", "raspberry-shake-stations"]);
export function sourceDownloadHref(id: OfficialContextId, archiveDay?: string) {
  const href = SOURCE_DOWNLOADS[id].href;
  return archiveDay && ARCHIVE_DOWNLOAD_SOURCES.has(id) ? `${href}&day=${encodeURIComponent(archiveDay)}` : href;
}
