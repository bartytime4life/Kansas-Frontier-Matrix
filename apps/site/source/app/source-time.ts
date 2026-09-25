import type { OfficialContextPayload } from "./live-context";

const UTC_DAY_MS = 86_400_000;

/** Archive sliders use calendar days, not milliseconds or inferred observations. */
export const utcDayOrdinal = (day: string): number | null => {
  if (!/^\d{4}-\d{2}-\d{2}$/.test(day)) return null;
  const timestamp = Date.parse(`${day}T00:00:00.000Z`);
  if (!Number.isFinite(timestamp) || new Date(timestamp).toISOString().slice(0, 10) !== day) return null;
  return Math.floor(timestamp / UTC_DAY_MS);
};

export const utcDayFromOrdinal = (ordinal: number): string => {
  if (!Number.isSafeInteger(ordinal)) throw new RangeError("UTC day ordinal must be an integer.");
  const date = new Date(ordinal * UTC_DAY_MS);
  if (!Number.isFinite(date.getTime())) throw new RangeError("UTC day ordinal is outside the calendar range.");
  return date.toISOString().slice(0, 10);
};

export const boundedUtcDay = (day: string, minDay: string, maxDay: string): string | null => {
  const min = utcDayOrdinal(minDay);
  const max = utcDayOrdinal(maxDay);
  if (min === null || max === null || min > max) return null;
  return utcDayFromOrdinal(Math.max(min, Math.min(max, utcDayOrdinal(day) ?? max)));
};

/** A successful source query is distinct from a visible map layer. */
export const datedSourceDisplayStatus = (
  returnedCount: number,
  frameCount: number,
  day: string,
  selected: boolean,
  effective: boolean,
  mapReady: boolean,
): string => {
  const loaded = `${returnedCount} returned records for ${day} UTC · ${frameCount} at selected frame`;
  if (!selected) return `${loaded} · Turn on layer to display`;
  if (!effective) return `${loaded} · Held by atlas year`;
  if (!mapReady) return `${loaded} · Waiting for map renderer`;
  return frameCount > 0 ? `${loaded} · shown on map` : `${loaded} · no features to display`;
};

/** Only timestamps returned for the checked UTC day become event sweep stops. */
export const earthquakeEventTimes = (payload: OfficialContextPayload, day: string): readonly string[] =>
  Object.freeze([...new Set(payload.data.features.flatMap((feature) => {
    const time = feature.properties?.observedAt;
    return typeof time === "string" && Number.isFinite(Date.parse(time)) && time.slice(0, 10) === day ? [time] : [];
  }))].sort());

/** An event sweep is cumulative within one checked day. It never carries an
 * earlier day's events into an empty or failed archive query. */
export const earthquakesThroughEvent = (
  original: OfficialContextPayload,
  day: string,
  observedAt: string,
): OfficialContextPayload => {
  const features = original.data.features.filter((feature) => {
    const time = feature.properties?.observedAt;
    return typeof time === "string" && time.slice(0, 10) === day && time <= observedAt;
  });
  return {
    ...original,
    featureCount: features.length,
    data: { type: "FeatureCollection", features },
    limitation: `${original.limitation} Map displays only this UTC day's returned events through ${observedAt}; no events between observations are inferred.`,
  };
};

/** NOAA HMS publishes interval validity, so stops are source interval
 * boundaries rather than fabricated evenly spaced observations. */
export const smokeValidityTimes = (payload: OfficialContextPayload, day: string): readonly string[] => {
  if (!payload.data.features.length) return Object.freeze([]);
  const start = `${day}T00:00:00.000Z`;
  const end = new Date(Date.parse(start) + 86_400_000).toISOString();
  return Object.freeze([start, ...payload.data.features.flatMap((feature) => [feature.properties?.start, feature.properties?.end]
    .filter((time): time is string => typeof time === "string" && Number.isFinite(Date.parse(time)) && time >= start && time < end))]
    .filter((time, index, all) => all.indexOf(time) === index)
    .sort());
};

export const smokeValidAt = (original: OfficialContextPayload, day: string, cursor: string): OfficialContextPayload => {
  const startOfDay = `${day}T00:00:00.000Z`;
  const endOfDay = new Date(Date.parse(startOfDay) + 86_400_000).toISOString();
  const features = cursor >= startOfDay && cursor < endOfDay ? original.data.features.filter((feature) => {
    const start = feature.properties?.start;
    const end = feature.properties?.end;
    return typeof start === "string" && typeof end === "string" && start <= cursor && cursor < end;
  }) : [];
  return {
    ...original,
    featureCount: features.length,
    data: { type: "FeatureCollection", features },
    limitation: `${original.limitation} Map shows polygons whose provider validity interval contains ${cursor}; this is not a measured second-by-second smoke series.`,
  };
};
