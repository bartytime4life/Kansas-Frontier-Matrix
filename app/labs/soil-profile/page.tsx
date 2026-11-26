import SoilProfile from "./soil-profile";
import manifest from "./snapshot-manifest.json";

export const metadata = {
  title: "Soil Profile Lab | Kansas Frontier Matrix",
  alternates: { canonical: "https://kansasfrontiermatrix.com/labs/soil-profile" },
  description: "Explore measured soil moisture and temperature at five depths at two Kansas NOAA stations, with daily observations, visible gaps and reproducible downloads.",
};

export default function SoilProfilePage() {
  return <SoilProfile manifest={manifest} />;
}
