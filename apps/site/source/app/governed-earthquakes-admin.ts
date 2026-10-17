// Hosted earthquake release steps (ADR-0049): the water admin steps run against the earthquake family's
// own D1 tables and R2 prefix, with the earthquake package parser and serving gate.
import { activateWaterPackage, stageWaterPackage, waterAdminStatus, withdrawWaterPackage, familyObjectKey, type ReleaseFamily, type WaterAdminStore } from "./governed-water-admin";
import { parseEarthquakePackage, projectEarthquakes, EARTHQUAKE_PACKAGE_LIMIT, type EarthquakePackage } from "./governed-earthquakes";

export const EARTHQUAKE_FAMILY: ReleaseFamily = {
  name: "earthquakes", packages: "earthquakes_packages", active: "earthquakes_active", events: "earthquakes_activation_events",
  prefix: "governed-earthquakes/v1/objects/", limit: EARTHQUAKE_PACKAGE_LIMIT, parse: parseEarthquakePackage,
  project: (pkg, decision, view, now) => projectEarthquakes(pkg as EarthquakePackage, decision, view, now),
};
export const earthquakesObjectKey = (packageId: string) => familyObjectKey(EARTHQUAKE_FAMILY, packageId);
export const stageEarthquakePackage = (store: WaterAdminStore, text: string, actor: string, now: string) => stageWaterPackage(store, text, actor, now, EARTHQUAKE_FAMILY);
export const activateEarthquakePackage = (store: WaterAdminStore, body: unknown, now: string) => activateWaterPackage(store, body, now, EARTHQUAKE_FAMILY);
export const withdrawEarthquakePackage = (store: WaterAdminStore, body: unknown, now: string) => withdrawWaterPackage(store, body, now, EARTHQUAKE_FAMILY);
export const earthquakesAdminStatus = (store: WaterAdminStore) => waterAdminStatus(store, EARTHQUAKE_FAMILY);
