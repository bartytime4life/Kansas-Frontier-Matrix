import CountyDrought from "./county-drought";
import manifest from "./snapshot-manifest.json";

export const metadata = {
  title: "County Drought Lab | Kansas Frontier Matrix",
  description: "Compare weekly drought area, severity and observed runs across all Kansas counties with U.S. Drought Monitor assessments from 2020–2025.",
};

export default function CountyDroughtPage() {
  return <CountyDrought manifest={manifest} />;
}
