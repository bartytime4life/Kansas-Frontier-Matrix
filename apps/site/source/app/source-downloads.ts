import type { OfficialContextId } from "./live-context";

const nationalMap = "https://apps.nationalmap.gov/downloader/";
export const SOURCE_DOWNLOADS: Record<OfficialContextId, { href: string; label: string }> = {
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
  "nws-forecast-wind": { href: "https://digital.weather.gov/", label: "NWS graphical wind forecast" },
};
