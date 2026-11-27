import DailyAirQuality from "./daily-air-quality";
import manifest from "./snapshot-manifest.json";

export const metadata = {
  title: "Daily Air Quality Lab | Kansas Frontier Matrix",
  alternates: { canonical: "https://kansasfrontiermatrix.com/labs/daily-air-quality" },
  description: "Inspect EPA daily county AQI for 12 reporting Kansas counties, 2020–2025, with category calendars, defining pollutants, visible gaps and source-linked downloads.",
};

export default function DailyAirQualityPage() {
  return <DailyAirQuality manifest={manifest} />;
}
