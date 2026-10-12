import type { Metadata } from "next";
import EarthEngineWorkspace from "./workspace";

export const metadata: Metadata = {
  title: "Earth Engine discovery & recipes | Kansas Frontier Matrix",
  description: "Explore Kansas-relevant Earth Engine datasets, compare coverage and prepare reviewable analysis recipes.",
};

export default function EarthEnginePage() {
  return <EarthEngineWorkspace />;
}
