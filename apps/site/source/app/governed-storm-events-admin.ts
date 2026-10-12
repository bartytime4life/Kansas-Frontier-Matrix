// Hosted Storm Events release steps (ADR-0047): the water admin steps run against the storm events family's
// own D1 tables and R2 prefix, with the storm events package parser and serving gate.
import { activateWaterPackage, stageWaterPackage, waterAdminStatus, withdrawWaterPackage, familyObjectKey, type ReleaseFamily, type WaterAdminStore } from "./governed-water-admin";
import { parseStormEventsPackage, projectStormEvents, STORM_EVENTS_PACKAGE_LIMIT, type StormPackage } from "./governed-storm-events";

export const STORM_EVENTS_FAMILY: ReleaseFamily = {
  name: "storm-events", packages: "storm_events_packages", active: "storm_events_active", events: "storm_events_activation_events",
  prefix: "governed-storm-events/v1/objects/", limit: STORM_EVENTS_PACKAGE_LIMIT, parse: parseStormEventsPackage,
  project: (pkg, decision, view, now) => projectStormEvents(pkg as StormPackage, decision, view, now),
};
export const stormEventsObjectKey = (packageId: string) => familyObjectKey(STORM_EVENTS_FAMILY, packageId);
export const stageStormEventsPackage = (store: WaterAdminStore, text: string, actor: string, now: string) => stageWaterPackage(store, text, actor, now, STORM_EVENTS_FAMILY);
export const activateStormEventsPackage = (store: WaterAdminStore, body: unknown, now: string) => activateWaterPackage(store, body, now, STORM_EVENTS_FAMILY);
export const withdrawStormEventsPackage = (store: WaterAdminStore, body: unknown, now: string) => withdrawWaterPackage(store, body, now, STORM_EVENTS_FAMILY);
export const stormEventsAdminStatus = (store: WaterAdminStore) => waterAdminStatus(store, STORM_EVENTS_FAMILY);
