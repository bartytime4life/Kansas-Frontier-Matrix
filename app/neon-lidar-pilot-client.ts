import { readSuccessfulJson } from "./bounded-json";
import { parseNeonLidarPreview, type NeonLidarPreview } from "./neon-lidar-preview";

export const NEON_PILOT_MAX_BYTES = 1_000_000;
export type NeonPilotReceipt = {
  format: "kfm-neon-relay-pilot-v1"; preview: NeonLidarPreview; generatedAt: string;
  review: { status: "pending"; scientific_accuracy_verified: false; source_admitted: false;
    canopy_native_max_m: number; canopy_native_cells_above_50m: number;
    surface_minus_ground_native_max_m: number; notes: string[] };
  cache: { state: "live" | "fresh" | "stale"; at: string };
};
const object = (value: unknown): value is Record<string, unknown> => !!value && typeof value === "object" && !Array.isArray(value);
const finite = (value: unknown): value is number => typeof value === "number" && Number.isFinite(value);
function date(value: unknown): value is string {
  if (typeof value !== "string" || !/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,6})?Z$/.test(value)) return false;
  const time = Date.parse(value);
  return Number.isFinite(time) && new Date(time).toISOString().slice(0, 19) === value.slice(0, 19);
}
export function parseNeonPilotReceipt(value: unknown): NeonPilotReceipt | null {
  if (!object(value) || value.format !== "kfm-neon-relay-pilot-v1" || !date(value.generatedAt)) return null;
  const preview = parseNeonLidarPreview(value.preview), review = value.review, cache = value.cache;
  if (!preview || preview.data_kind !== "provider-files" || preview.source.site !== "KONZ"
    || preview.source.month !== "2024-09" || preview.source.acquisition_run !== "2024_KONZ_10"
    || preview.source.release !== "RELEASE-2026" || preview.source.tile !== "NEON_D06_KONZ_DP3_706000_4336000"
    || !object(review) || review.status !== "pending" || review.scientific_accuracy_verified !== false || review.source_admitted !== false
    || !finite(review.canopy_native_max_m) || review.canopy_native_max_m < 0
    || !Number.isSafeInteger(review.canopy_native_cells_above_50m) || (review.canopy_native_cells_above_50m as number) < 0 || (review.canopy_native_cells_above_50m as number) > 1_000_000
    || !finite(review.surface_minus_ground_native_max_m) || !Array.isArray(review.notes) || review.notes.length < 1 || review.notes.length > 20
    || !review.notes.every(note => typeof note === "string" && note.trim().length > 0 && note.length <= 1000 && !/[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f]/.test(note))
    || !object(cache) || !["live", "fresh", "stale"].includes(String(cache.state)) || !date(cache.at)) return null;
  return { format: "kfm-neon-relay-pilot-v1", preview, generatedAt: value.generatedAt,
    review: { status: "pending", scientific_accuracy_verified: false, source_admitted: false,
      canopy_native_max_m: review.canopy_native_max_m, canopy_native_cells_above_50m: review.canopy_native_cells_above_50m as number,
      surface_minus_ground_native_max_m: review.surface_minus_ground_native_max_m, notes: [...review.notes] as string[] },
    cache: { state: cache.state as NeonPilotReceipt["cache"]["state"], at: cache.at } };
}

/** Explicit bounded read of the dev-processed public pilot. No provider credential enters this request. */
export async function readNeonLidarPilot(caller: AbortSignal): Promise<NeonPilotReceipt> {
  caller.throwIfAborted();
  const deadline = new AbortController(), signal = AbortSignal.any([caller, deadline.signal]);
  const timer = setTimeout(() => deadline.abort(new DOMException("Pilot preview request timed out", "TimeoutError")), 45_000);
  try {
    const response = await fetch("/api/neon/preview", { method: "GET", signal, cache: "no-store", credentials: "same-origin", redirect: "error" });
    if (!response.ok) {
      void response.body?.cancel().catch(() => undefined);
      throw new Error("The Konza Prairie preview is unavailable. Import a prepared file or try again later.");
    }
    const body = await readSuccessfulJson(response, NEON_PILOT_MAX_BYTES, signal);
    signal.throwIfAborted();
    const receipt = parseNeonPilotReceipt(body);
    if (!receipt) throw new Error("The Konza Prairie preview failed source and review validation. Nothing has been displayed.");
    return receipt;
  } finally { clearTimeout(timer); }
}
