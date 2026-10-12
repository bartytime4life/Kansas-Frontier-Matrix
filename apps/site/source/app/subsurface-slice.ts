import { meters, type Borehole, type DepthInterval } from "./subsurface-model";

export type SliceInterval = { interval: DepthInterval; index: number; top: number; bottom: number };
/** Display bounds only. Original intervals and indices remain untouched for inspection. */
export function sliceIntervals(record: Borehole, window: [number, number] = [0, 12000]): SliceInterval[] {
  if (!(window[0] >= 0 && window[1] > window[0] && window[1] <= 12000)) return [];
  return record.intervals.flatMap((interval, index) => {
    if (!Number.isFinite(interval.top) || !Number.isFinite(interval.bottom) || interval.top < 0 || interval.bottom <= interval.top) return [];
    const top = Math.max(window[0], meters(interval.top, record.depthUnit));
    const bottom = Math.min(window[1], meters(interval.bottom, record.depthUnit));
    return bottom > top ? [{ interval, index, top, bottom }] : [];
  });
}

/** A deliberate slice opens within a real interval, never at an empty/top boundary. */
export function fitRecordedSlice(record: Borehole, depth: number, preferredIndex: number | null = null) {
  const rows = sliceIntervals(record);
  if (!rows.length) return null;
  const range: [number, number] = [Math.min(...rows.map(row => row.top)), Math.max(...rows.map(row => row.bottom))];
  const preferred = rows.find(row => row.index === preferredIndex);
  const containing = rows.find(row => depth > row.top && depth < row.bottom && (!preferred || row.index === preferred.index));
  const targetDepth = Number.isFinite(depth) && depth > range[0] && depth < range[1] ? depth : (range[0] + range[1]) / 2;
  const target = preferred ?? containing ?? rows.reduce((near, row) => Math.abs((row.top + row.bottom) / 2 - targetDepth) < Math.abs((near.top + near.bottom) / 2 - targetDepth) ? row : near);
  return { range, depth: containing ? depth : (target.top + target.bottom) / 2, intervalIndex: target.index };
}

/** Ray hits above the cut plane are not visible and must not select a hidden layer. */
export function sliceHitVisible(y: number, sliced: boolean, depth: number, rangeTop: number, scale: number, vertical: number) {
  return Number.isFinite(y) && (!sliced || y <= -(depth - rangeTop) * scale * vertical + 0.0001);
}

/** In-place slice toggling must stay within the current displayed/filter window. */
export function sliceWindowDepth(record: Borehole, depth: number, window: [number, number], descriptionFilter = "") {
  const rows = sliceIntervals(record, window).filter(row => !descriptionFilter || row.interval.description === descriptionFilter).slice(0, 500);
  if (!rows.length) return null;
  if (rows.some(row => depth > row.top && depth < row.bottom)) return depth;
  const targetDepth = Number.isFinite(depth) && depth > window[0] && depth < window[1] ? depth : (window[0] + window[1]) / 2;
  const target = rows.reduce((near, row) => Math.abs((row.top + row.bottom) / 2 - targetDepth) < Math.abs((near.top + near.bottom) / 2 - targetDepth) ? row : near);
  return (target.top + target.bottom) / 2;
}
