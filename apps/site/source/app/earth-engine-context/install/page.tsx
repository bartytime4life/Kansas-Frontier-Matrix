import { notFound } from "next/navigation";
import { earthEngineOwner } from "../../earth-engine-context-server";
import { EarthEngineInstaller } from "./installer";

export default async function EarthEngineContextInstallPage() {
  try { await earthEngineOwner(); } catch { notFound(); }
  return <EarthEngineInstaller />;
}
