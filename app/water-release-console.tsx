"use client";
import { useCallback, useEffect, useState } from "react";
import { expiryText } from "./water-release-expiry";

type Authorized = { package_id: string; expires_at: string };
type Status = { active_package_id: string | null; previous_package_id: string | null; revision: number; decision_expires_at: string | null; authorized_packages: Authorized[]; release_hold?: string };
type Result = { reason_code?: string; revision?: number };
export type ReleaseKind = "water" | "weather" | "soil" | "storm-events" | "earthquakes" | "subsurface" | "groundwater" | "archive";
const reasonText: Record<string, string> = {
  OWNER_REQUIRED: "This account is not an authorized release owner.",
  SIGN_IN_REQUIRED: "Sign in with the owner account to manage releases.",
  WATER_RELEASE_NOT_CONFIGURED: "Owner access has not been configured for this new Site.",
  PUBLIC_DELIVERY_UNCONFIGURED: "The reviewed public delivery list is not configured. No package can be activated.",
  PUBLIC_PACKAGE_NOT_APPROVED: "This package is not in the trusted public delivery list.",
  PACKAGE_NOT_STAGED: "Upload the exact authorized package before activation.",
  ACTIVATION_CONFLICT: "The active package changed. Refresh before trying again.",
  WITHDRAW_CONFLICT: "The active package changed; nothing was withdrawn. Refresh before trying again.",
  PUBLIC_RELEASE_EXPIRED: "This release has expired. A newly reviewed release is required.",
};
const explain = (code?: string) => reasonText[code ?? ""] ?? `Action unavailable (${code ?? "connection failed"}).`;

export default function WaterReleaseConsole() { return <ReleaseConsole kind="water" />; }

/** Owners select an already authorized package; browser input never grants publication authority. */
export function ReleaseConsole({ kind }: { kind: ReleaseKind }) {
  const [status, setStatus] = useState<Status | null>(null);
  const [packageId, setPackageId] = useState("");
  const [message, setMessage] = useState("Loading release status…");
  const [busy, setBusy] = useState(false);
  const [now, setNow] = useState(() => Date.now());
  const refresh = useCallback(async () => {
    try {
      const response = await fetch(`/api/governed/${kind}-admin/status`, { cache: "no-store" });
      const body = await response.json();
      if (!response.ok) { setStatus(null); setMessage(explain(body.reason_code)); return; }
      setStatus(body);
      setMessage(body.release_hold ? "Public serving is held because its publication configuration is not valid. Withdrawal remains available." : body.active_package_id ? `A ${kind} package is active.` : "No package is active. Unreleased records are withheld.");
    } catch { setStatus(null); setMessage("Status could not be loaded. Check the connection and refresh."); }
    setNow(Date.now());
  }, [kind]);
  useEffect(() => { const initial = setTimeout(() => void refresh(), 0); const tick = setInterval(() => setNow(Date.now()), 60_000); return () => { clearTimeout(initial); clearInterval(tick); }; }, [refresh]);
  const packages = status?.authorized_packages?.filter(entry => Date.parse(entry.expires_at) > now) ?? [];
  const selected = packages.find(entry => entry.package_id === packageId);
  async function send(action: "activate" | "withdraw", rollback = false) {
    if (!status) return;
    setBusy(true);
    try {
      const body = action === "activate" ? { package_id: packageId, expected_active: status.active_package_id, rollback }
        : { package_id: status.active_package_id, expected_active: status.active_package_id };
      const response = await fetch(`/api/governed/${kind}-admin/${action}`, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(body) });
      const result: Result = await response.json();
      await refresh();
      setMessage(response.ok ? `${action === "withdraw" ? "Withdrawn; new reads and exports are withheld." : rollback ? "Rolled back to the eligible previous release." : "Authorized package activated."} Revision ${result.revision ?? "–"}.` : explain(result.reason_code));
    } catch { setMessage("The result could not be confirmed. Refresh status before retrying."); }
    finally { setBusy(false); }
  }
  const expired = status?.decision_expires_at && Date.parse(status.decision_expires_at) <= now;
  return <section aria-labelledby={`${kind}-release-heading`} style={{ display: "grid", gap: 16 }}>
    <h2 id={`${kind}-release-heading`} style={{ margin: 0 }}>Active {kind} release</h2>
    <dl style={{ display: "grid", gridTemplateColumns: "max-content 1fr", gap: "4px 16px", margin: 0 }}>
      <dt>Active</dt><dd style={{ margin: 0, overflowWrap: "anywhere" }}><code>{status?.active_package_id ?? "none"}</code></dd>
      <dt>Previous</dt><dd style={{ margin: 0, overflowWrap: "anywhere" }}><code>{status?.previous_package_id ?? "none"}</code></dd>
      <dt>Revision</dt><dd style={{ margin: 0 }}>{status?.revision ?? "–"}</dd>
      <dt>Release expires</dt><dd style={{ margin: 0 }}>{expiryText(status, now)}</dd>
    </dl>
    <label htmlFor={`${kind}-package`} style={{ fontWeight: 600 }}>Previously authorized package</label>
    <select id={`${kind}-package`} value={selected ? packageId : ""} onChange={event => setPackageId(event.target.value)} disabled={busy || !packages.length} style={{ width: "100%", minHeight: 44 }}>
      <option value="">{packages.length ? "Choose an authorized package" : "No authorized packages available"}</option>
      {packages.map(entry => <option key={entry.package_id} value={entry.package_id}>{entry.package_id}</option>)}
    </select>
    <p style={{ margin: 0 }}>Only packages in the reviewed, integrity-pinned delivery list can be selected. The server checks authority, staged bytes, validity, and the current revision again before changing the release.</p>
    <div style={{ display: "flex", flexWrap: "wrap", gap: 8 }}>
      <button type="button" disabled={busy || !selected || !status} onClick={() => void send("activate")}>Activate authorized package</button>
      <button type="button" disabled={busy || !selected || !status?.previous_package_id || packageId !== status.previous_package_id} onClick={() => void send("activate", true)}>Roll back to previous</button>
      <button type="button" disabled={busy || !status?.active_package_id} onClick={() => void send("withdraw")}>Withdraw active package</button>
      <button type="button" disabled={busy} onClick={() => void refresh()}>Refresh status</button>
    </div>
    <p role="status" aria-live="polite" style={{ margin: 0 }}>{message}</p>
    {expired && <p role="alert" style={{ margin: 0 }}>The active release has expired. Its data is withheld until another eligible release is activated.</p>}
  </section>;
}
