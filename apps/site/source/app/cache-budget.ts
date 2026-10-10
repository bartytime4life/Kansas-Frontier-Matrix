export type CacheBudget = { schema: "kfm-local-cache-budget/v1"; limitBytes: number; defaultLimitBytes: number; usedBytes: number; temporaryBytes: number; replaceableBytes: number; freeBytes: number; reserveBytes: number; sessionToken: string; busy: boolean };
export function parseCacheBudget(value: unknown): CacheBudget | null {
  if (!value || typeof value !== "object" || Array.isArray(value)) return null;
  const v = value as Record<string, unknown>;
  if (v.schema !== "kfm-local-cache-budget/v1" || typeof v.busy !== "boolean" || typeof v.sessionToken !== "string" || !/^[A-Za-z0-9_-]{43}$/.test(v.sessionToken)) return null;
  for (const key of ["limitBytes", "defaultLimitBytes", "usedBytes", "temporaryBytes", "replaceableBytes", "freeBytes", "reserveBytes"]) {
    if (!Number.isSafeInteger(v[key]) || Number(v[key]) < 0) return null;
  }
  if (Number(v.limitBytes) < 1 || Number(v.defaultLimitBytes) < 1 || Number(v.temporaryBytes) + Number(v.replaceableBytes) > Number(v.usedBytes)) return null;
  return v as CacheBudget;
}
/** Decimal GB entered by the owner, converted without rounding large integers. */
export function cacheBudgetBytes(input: string): number | null {
  if (!/^\d{1,7}(?:\.\d{1,9})?$/.test(input)) return null;
  const [whole, fraction = ""] = input.split(".");
  const value = BigInt(whole) * 1_000_000_000n + BigInt(fraction.padEnd(9, "0"));
  return value > 0n && value <= BigInt(Number.MAX_SAFE_INTEGER) ? Number(value) : null;
}
export function cacheBudgetGb(bytes: number): string {
  const value = BigInt(bytes);
  const fractional = String(value % 1_000_000_000n).padStart(9, "0").replace(/0+$/, "");
  return `${value / 1_000_000_000n}${fractional ? `.${fractional}` : ""}`;
}
export const cacheBudgetError = (code: unknown) => code === "DOWNLOAD_ALREADY_RUNNING" || code === "WORKER_BUSY"
  ? "Another budget operation is running. Refresh and try again."
  : code === "CACHE_BUDGET_INVALID" ? "Enter a positive size in GB within the supported numeric range."
  : "The budget could not be confirmed. Refresh the saved budget from this computer before trying again.";
