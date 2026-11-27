import HeatAndRain from "./heat-and-rain";
import manifest from "./snapshot-manifest.json";

export const metadata = {
  title: "Heat & Rain Lab | Kansas Frontier Matrix",
  alternates: { canonical: "https://kansasfrontiermatrix.com/labs/heat-and-rain" },
  description: "Explore daily temperature extremes and precipitation at three Kansas weather stations, with NOAA observations, visible data coverage and reproducible downloads.",
};

export default function HeatAndRainPage() {
  return <HeatAndRain manifest={manifest} />;
}
