import air from "../../labs/daily-air-quality/snapshot-manifest.json";
import climate from "../../labs/heat-and-rain/snapshot-manifest.json";
import drought from "../../labs/county-drought/snapshot-manifest.json";
import sunlight from "../../labs/sunlight-and-sky/snapshot-manifest.json";
import { loadAirSnapshot } from "../../labs/daily-air-quality/snapshot-loader.mjs";
import { loadClimateSnapshot } from "../../labs/heat-and-rain/snapshot-loader.mjs";
import { loadDroughtSnapshot } from "../../labs/county-drought/snapshot-loader.mjs";
import { loadSunlightSnapshot } from "../../labs/sunlight-and-sky/snapshot-loader.mjs";
import { comparisonPlace } from "./comparison-places.mjs";

export type CountySnapshots = {
  drought: Awaited<ReturnType<typeof loadDroughtSnapshot>>;
  air: Awaited<ReturnType<typeof loadAirSnapshot>>;
};

export async function loadComparisonInputs(place: string, signal: AbortSignal, shared?: CountySnapshots) {
  const area = comparisonPlace(place);
  if (!area) throw new Error("Choose a supported Kansas comparison area.");
  const station = climate.stations.find(item => item.id === area.climateId);
  const point = sunlight.points.find(item => item.id === area.sunlightId);
  if (!station || !point || !drought.counties.some(county => county.id === area.countyId) ||
      !air.counties.some(county => county.id === area.countyId)) {
    throw new Error("A required source for this area is missing from the public manifests.");
  }

  const [climateSnapshot, droughtSnapshot, airSnapshot, sunlightSnapshot] = await Promise.all([
    loadClimateSnapshot(station, { signal }),
    shared?.drought ?? loadDroughtSnapshot(drought, { signal }),
    shared?.air ?? loadAirSnapshot(air, { signal }),
    loadSunlightSnapshot(point, { signal }),
  ]);

  return {
    snapshots: { climate: climateSnapshot, drought: droughtSnapshot, air: airSnapshot, sunlight: sunlightSnapshot },
    evidence: { climate: station, drought, air, sunlight: point },
  };
}
