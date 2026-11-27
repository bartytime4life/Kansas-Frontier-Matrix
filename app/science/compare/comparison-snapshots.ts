import air from "../../labs/daily-air-quality/snapshot-manifest.json";
import climate from "../../labs/heat-and-rain/snapshot-manifest.json";
import drought from "../../labs/county-drought/snapshot-manifest.json";
import sunlight from "../../labs/sunlight-and-sky/snapshot-manifest.json";
import { loadAirSnapshot } from "../../labs/daily-air-quality/snapshot-loader.mjs";
import { loadClimateSnapshot } from "../../labs/heat-and-rain/snapshot-loader.mjs";
import { loadDroughtSnapshot } from "../../labs/county-drought/snapshot-loader.mjs";
import { loadSunlightSnapshot } from "../../labs/sunlight-and-sky/snapshot-loader.mjs";
import { TOPEKA_COMPARISON } from "./comparison-model.mjs";

export async function loadComparisonInputs(signal: AbortSignal) {
  const station = climate.stations.find(item => item.id === TOPEKA_COMPARISON.climateId);
  const point = sunlight.points.find(item => item.id === TOPEKA_COMPARISON.sunlightId);
  if (!station || !point) throw new Error("A Topeka source is missing from the public manifests.");

  const [climateSnapshot, droughtSnapshot, airSnapshot, sunlightSnapshot] = await Promise.all([
    loadClimateSnapshot(station, { signal }),
    loadDroughtSnapshot(drought, { signal }),
    loadAirSnapshot(air, { signal }),
    loadSunlightSnapshot(point, { signal }),
  ]);

  return {
    snapshots: { climate: climateSnapshot, drought: droughtSnapshot, air: airSnapshot, sunlight: sunlightSnapshot },
    evidence: { climate: station, drought, air, sunlight: point },
  };
}
