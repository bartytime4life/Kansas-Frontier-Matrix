// Pure expiry wording for the water and weather release pages; callers pass the current time so the
// warning and expired states advance while the page stays open.
export const REFRESH_WARNING_MS = 2 * 24 * 60 * 60 * 1000;

type Active = { active_package_id: string | null; decision_expires_at: string | null } | null;

function remainingMs(status: Active, now: number) {
  return status?.active_package_id && status.decision_expires_at ? Date.parse(status.decision_expires_at) - now : null;
}

export function expiryText(status: Active, now: number) {
  const remaining = remainingMs(status, now);
  if (remaining === null || Number.isNaN(remaining)) return "–";
  if (remaining <= 0) return `${status!.decision_expires_at} (expired; the layer is not serving)`;
  const hours = Math.floor(remaining / 3_600_000);
  return `${status!.decision_expires_at} (in ${hours >= 48 ? `${Math.floor(hours / 24)} days` : `${hours} hours`})`;
}

export function expiryWarning(status: Active, now: number, tool = "water_release.py") {
  const remaining = remainingMs(status, now);
  if (remaining === null || Number.isNaN(remaining)) return null;
  if (remaining <= 0) return `The active decision has expired, so the layer is not serving. Run ${tool} cycle and activate the new package.`;
  if (remaining <= REFRESH_WARNING_MS) return `The active decision expires soon. Run ${tool} cycle and activate the new package before it does.`;
  return null;
}
