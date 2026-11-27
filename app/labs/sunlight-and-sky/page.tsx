import SunlightAndSky from "./sunlight-and-sky";
import manifest from "./snapshot-manifest.json";

export const metadata = {
  title: "Sunlight & Sky Lab | Kansas Frontier Matrix",
  alternates: { canonical: "https://kansasfrontiermatrix.com/labs/sunlight-and-sky" },
  description: "Compare NASA POWER modeled daily sunlight energy at three Kansas query points, 2020–2025, with clear-sky context, visible gaps and reproducible downloads.",
};

export default function SunlightAndSkyPage() {
  return <SunlightAndSky manifest={manifest} />;
}
