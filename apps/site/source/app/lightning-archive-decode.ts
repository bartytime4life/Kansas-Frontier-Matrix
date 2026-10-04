import type { GlmFlash } from "./lightning-flashes";
import type { GlmArchiveFile } from "./lightning-archive";
export type HdfReader = typeof import("h5wasm");
let sequence = 0;

/** Native HDF5 metadata handles compact and dense attributes across NOAA eras. */
export function decodeArchiveFlashes(bytes: ArrayBuffer, file: GlmArchiveFile, start: number, end: number, hdf: HdfReader) {
  if (bytes.byteLength > 4 * 1024 * 1024 || bytes.byteLength !== file.size) throw new Error("NOAA file size changed.");
  const fs = hdf.FS;
  if (!fs) throw new Error("Archive reader unavailable.");
  const name = `/kfm-lightning-${sequence++}.nc`;
  fs.writeFile(name, new Uint8Array(bytes));
  let handle: InstanceType<HdfReader["File"]> | undefined;
  try {
    handle = new hdf.File(name, "r");
    const attributes = handle.attrs;
    if (attributes.platform_ID?.value !== `G${file.satellite}` || attributes.dataset_name?.value !== file.key.split("/").at(-1)
      || Date.parse(String(attributes.time_coverage_start?.value)) !== file.start || Date.parse(String(attributes.time_coverage_end?.value)) !== file.end) throw new Error("NOAA file identity or observation coverage changed.");
    const dataset = (key: string) => { const value = handle!.get(key); if (!(value instanceof hdf.Dataset)) throw new Error("Missing NOAA flash array."); return value; };
    const lat = dataset("flash_lat"), lon = dataset("flash_lon"), time = dataset("flash_time_offset_of_first_event"), id = dataset("flash_id"), quality = dataset("flash_quality_flag");
    const count = lat.shape?.[0];
    if (typeof count !== "number" || !Number.isInteger(count) || count < 0 || count > 20_000 || [lat, lon, time, id, quality].some(d => d.shape?.length !== 1 || d.shape[0] !== count)
      || lat.attrs.units?.value !== "degrees_north" || lon.attrs.units?.value !== "degrees_east" || time.dtype !== "<h" || id.dtype !== "<h") throw new Error("Unsupported NOAA flash arrays.");
    const units = String(time.attrs.units?.value).match(/^(seconds|milliseconds) since (\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}(?:\.\d+)?)$/);
    const base = units ? Date.parse(`${units[2]}T${units[3]}Z`) : NaN;
    const scalar = (value: unknown) => Number(Array.isArray(value) || ArrayBuffer.isView(value) ? (value as ArrayLike<number>)[0] : value);
    const scale = scalar(time.attrs.scale_factor?.value), offset = scalar(time.attrs.add_offset?.value);
    const unsigned = time.attrs._Unsigned?.value === "true";
    const modern = units?.[1] === "seconds" && unsigned && scale > 0 && scale < .001 && offset === -5;
    const legacy = units?.[1] === "milliseconds" && !unsigned && scale === 2 && offset === 0;
    if (!Number.isFinite(base) || base !== file.start || !(modern || legacy)) throw new Error("Unsupported NOAA flash clock.");
    if (count === 0) return { flashes: [], omittedQuality: 0 };
    const lats = lat.value as Float32Array, lons = lon.value as Float32Array, times = time.value as Int16Array, ids = id.value as Int16Array, flags = quality.value as Int16Array;
    if ([lats, lons, times, ids, flags].some(values => !values || values.length !== count)) throw new Error("NOAA flash arrays have inconsistent lengths.");
    const flashes: GlmFlash[] = []; let omittedQuality = 0;
    for (let i = 0; i < count; i++) {
      const latitude = lats[i], longitude = lons[i];
      if (!Number.isFinite(latitude) || !Number.isFinite(longitude) || latitude < -90 || latitude > 90 || longitude < -180 || longitude > 180) { if (flags[i] !== 0) continue; throw new Error("Invalid NOAA flash coordinate."); }
      if (longitude < -102.2 || longitude > -94.45 || latitude < 36.85 || latitude > 40.12) continue;
      const timeMs = Math.round(base + ((unsigned ? times[i] & 0xffff : times[i]) * scale + offset) * (modern ? 1000 : 1));
      if (timeMs < start || timeMs >= end) continue;
      if (flags[i] !== 0) { omittedQuality++; continue; }
      flashes.push({ id: `G${file.satellite}:${ids[i] & 0xffff}:${timeMs}:${longitude}:${latitude}`, longitude, latitude,
        timeMs, observedAt: new Date(timeMs).toISOString(), energyFj: null, areaKm2: null });
    }
    return { flashes, omittedQuality };
  } finally { try { handle?.close(); } finally { fs.unlink(name); } }
}
