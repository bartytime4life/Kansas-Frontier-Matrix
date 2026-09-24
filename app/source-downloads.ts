import type { OfficialContextId } from "./live-context";

const nationalMap = "https://apps.nationalmap.gov/downloader/";
export const SOURCE_DOWNLOADS: Record<OfficialContextId, { href: string; label: string }> = {
  "nasa-firms-active-fire": { href: "https://gibs.earthdata.nasa.gov/layer-metadata/v1.0/VIIRS_NOAA20_Thermal_Anomalies_375m_All.json", label: "NASA GIBS image source metadata" },
  "nasa-gibs-fire-points": { href: "https://gibs.earthdata.nasa.gov/vector-metadata/v1.0/FIRMS_VIIRS_Thermal_Anomalies.json", label: "NASA GIBS detection field metadata" },
  "nifc-fire-reports": { href: "https://services3.arcgis.com/T4QMspbfLg3qTGWY/arcgis/rest/services/WFIGS_Incident_Locations_YearToDate/FeatureServer/0", label: "Open NIFC WFIGS incident data" },
  "census-counties": { href: "/api/source-download?source=census-counties", label: "Download county baseline · GeoJSON" },
  "usgs-streamflow": { href: "/api/source-download?source=usgs-streamflow", label: "Download current observations · JSON" },
  "noaa-nwps-gauges": { href: "https://water.noaa.gov/about/api", label: "NOAA gauge data & API downloads" },
  "usgs-3dhp-hydrography": { href: nationalMap, label: "Download USGS hydrography" },
  "usgs-wbd-watersheds": { href: nationalMap, label: "Download watershed boundaries" },
  "noaa-nwm-analysis": { href: "https://nomads.ncep.noaa.gov/pub/data/nccf/com/nwm/prod/", label: "Download National Water Model files" },
  "noaa-nwm-short-range": { href: "https://nomads.ncep.noaa.gov/pub/data/nccf/com/nwm/prod/", label: "Download National Water Model files" },
  "usgs-earthquakes": { href: "/api/source-download?source=usgs-earthquakes", label: "Download catalog records · GeoJSON" },
  "noaa-hms-smoke": { href: "https://satepsanone.nesdis.noaa.gov/pub/FIRE/web/HMS/Smoke_Polygons/KML/", label: "Download dated NOAA smoke · KML" },
  "noaa-goes-geocolor": { href: "https://satellitemaps.nesdis.noaa.gov/arcgis/rest/services/MERGEDGC_Last_24hr/ImageServer", label: "NOAA dated GeoColor image catalog" },
  "raspberry-shake-stations": { href: "/api/source-download?source=raspberry-shake-stations", label: "Download station metadata · GeoJSON" },
  "usgs-3dep-hillshade": { href: nationalMap, label: "Download source elevation data" },
  "usgs-3dep-slope": { href: nationalMap, label: "Download source elevation data" },
  "nws-alerts": { href: "/api/source-download?source=nws-alerts", label: "Download current alerts · GeoJSON" },
  "nws-radar": { href: "https://www.ncei.noaa.gov/products/radar/next-generation-weather-radar", label: "NOAA radar archive & downloads" },
};
