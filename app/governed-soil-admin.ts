// Hosted soil release steps (ADR-0046): the water admin steps run against the soil family's
// own D1 tables and R2 prefix, with the soil package parser and serving gate.
import { activateWaterPackage, stageWaterPackage, waterAdminStatus, withdrawWaterPackage, familyObjectKey, type ReleaseFamily, type WaterAdminStore } from "./governed-water-admin";
import { parseSoilPackage, projectSoil, SOIL_PACKAGE_LIMIT, type SoilPackage } from "./governed-soil";

export const SOIL_FAMILY: ReleaseFamily = {
  name: "soil", packages: "soil_packages", active: "soil_active", events: "soil_activation_events",
  prefix: "governed-soil/v1/objects/", limit: SOIL_PACKAGE_LIMIT, parse: parseSoilPackage,
  project: (pkg, decision, view, now) => projectSoil(pkg as SoilPackage, decision, view, now),
};
export const soilObjectKey = (packageId: string) => familyObjectKey(SOIL_FAMILY, packageId);
export const stageSoilPackage = (store: WaterAdminStore, text: string, actor: string, now: string) => stageWaterPackage(store, text, actor, now, SOIL_FAMILY);
export const activateSoilPackage = (store: WaterAdminStore, body: unknown, now: string) => activateWaterPackage(store, body, now, SOIL_FAMILY);
export const withdrawSoilPackage = (store: WaterAdminStore, body: unknown, now: string) => withdrawWaterPackage(store, body, now, SOIL_FAMILY);
export const soilAdminStatus = (store: WaterAdminStore) => waterAdminStatus(store, SOIL_FAMILY);
