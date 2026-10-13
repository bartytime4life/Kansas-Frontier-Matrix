import { readBoundedJson } from "./bounded-json";

/** Loopback intake desk served by tools/local_data/intake_service.py on the operator's computer. */
export const INTAKE_DESK_ORIGIN = "http://127.0.0.1:8771";

export type IntakeBudget = {
  github_limit_bytes: number; reserved_for_code_and_interface_bytes: number; data_ceiling_bytes: number;
  committed_bytes: number; planned_bytes: number; available_for_new_data_bytes: number; level: "ok" | "warn" | "over";
};
export type IntakeOverview = {
  schema: "kfm-intake-overview/v1"; files: number; bytes: number; ready: number; review: number; blocked: number;
  budget: IntakeBudget; releasePlanBytes: number; lastRunFinishedAt: string | null; running: boolean;
};

const object = (v: unknown): v is Record<string, unknown> => Boolean(v && typeof v === "object" && !Array.isArray(v));
const count = (v: unknown): v is number => Number.isSafeInteger(v) && Number(v) >= 0;
const groupFiles = (groups: Record<string, unknown>, key: string) => {
  const group = groups[key];
  return object(group) && count(group.files) ? group.files : 0;
};

/** Accept only the fields the Explorer shows; anything malformed is treated as unavailable. */
export function parseIntakeOverview(value: unknown): IntakeOverview | null {
  if (!object(value) || value.schema !== "kfm-intake-overview/v1" || !count(value.files) || !count(value.bytes)
    || !object(value.by_status) || !object(value.budget) || !count(value.release_plan_bytes)) return null;
  const b = value.budget;
  const fields = ["github_limit_bytes", "reserved_for_code_and_interface_bytes", "data_ceiling_bytes", "committed_bytes", "planned_bytes", "available_for_new_data_bytes"] as const;
  if (!fields.every(key => count(b[key])) || !["ok", "warn", "over"].includes(String(b.level))
    || Number(b.reserved_for_code_and_interface_bytes) + Number(b.data_ceiling_bytes) !== Number(b.github_limit_bytes)) return null;
  for (const group of Object.values(value.by_status)) if (!object(group) || !count(group.files)) return null;
  const ready = groupFiles(value.by_status, "ready"), review = groupFiles(value.by_status, "review"), blocked = groupFiles(value.by_status, "blocked");
  if (ready + review + blocked > value.files) return null;
  const lastRun = value.last_run;
  const finished = object(lastRun) && typeof lastRun.finished_at === "string" && Number.isFinite(Date.parse(lastRun.finished_at)) ? lastRun.finished_at : null;
  if (!(value.running_run === null || typeof value.running_run === "string")) return null;
  const budget = Object.fromEntries([...fields.map(key => [key, b[key]]), ["level", b.level]]) as IntakeBudget;
  return { schema: "kfm-intake-overview/v1", files: value.files, bytes: value.bytes, ready, review, blocked, budget,
    releasePlanBytes: value.release_plan_bytes, lastRunFinishedAt: finished, running: value.running_run !== null };
}

/** One bounded, credential-free read from the loopback desk; the deadline covers a stalled body too. */
export async function intakeOverviewRequest(signal: AbortSignal) {
  const combined = AbortSignal.any([signal, AbortSignal.timeout(8_000)]);
  const response = await fetch(`${INTAKE_DESK_ORIGIN}/api/overview`, { signal: combined, credentials: "omit", cache: "no-store", redirect: "error" });
  const body = await readBoundedJson(response, 256_000, combined);
  combined.throwIfAborted();
  return response.ok ? parseIntakeOverview(body) : null;
}
