// Hosted weather release steps (ADR-0045): the water admin steps run against the weather family's
// own D1 tables and R2 prefix, with the weather package parser and serving gate.
import { activateWaterPackage, stageWaterPackage, waterAdminStatus, withdrawWaterPackage, familyObjectKey, type ReleaseFamily, type WaterAdminStore } from "./governed-water-admin";
import { parseWeatherPackage, projectWeather, WEATHER_PACKAGE_LIMIT, type WeatherPackage } from "./governed-weather";

export const WEATHER_FAMILY: ReleaseFamily = {
  name: "weather", packages: "weather_packages", active: "weather_active", events: "weather_activation_events",
  prefix: "governed-weather/v1/objects/", limit: WEATHER_PACKAGE_LIMIT, parse: parseWeatherPackage,
  project: (pkg, decision, view, now) => projectWeather(pkg as WeatherPackage, decision, view, now),
};
export const weatherObjectKey = (packageId: string) => familyObjectKey(WEATHER_FAMILY, packageId);
export const stageWeatherPackage = (store: WaterAdminStore, text: string, actor: string, now: string) => stageWaterPackage(store, text, actor, now, WEATHER_FAMILY);
export const activateWeatherPackage = (store: WaterAdminStore, body: unknown, now: string) => activateWaterPackage(store, body, now, WEATHER_FAMILY);
export const withdrawWeatherPackage = (store: WaterAdminStore, body: unknown, now: string) => withdrawWaterPackage(store, body, now, WEATHER_FAMILY);
export const weatherAdminStatus = (store: WaterAdminStore) => waterAdminStatus(store, WEATHER_FAMILY);
