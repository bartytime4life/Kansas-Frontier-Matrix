"use client";
import { useEffect, useState } from "react";
import { expiryText, expiryWarning } from "./water-release-expiry";

type Status = { active_package_id: string | null; previous_package_id: string | null; revision: number; decision_expires_at: string | null };
type Result = { outcome: string; reason_code?: string; package_id?: string; revision?: number };

export type ReleaseKind = "water" | "weather";
const TOOL: Record<ReleaseKind, string> = { water: "water_release.py", weather: "weather_release.py" };
const reasonText: Record<string, string> = {
  OWNER_REQUIRED: "This account is not on the release owner list (KFM_WATER_OWNER_IDS / KFM_WATER_OWNER_EMAILS).",
  WATER_RELEASE_NOT_CONFIGURED: "Set KFM_WATER_OWNER_IDS or KFM_WATER_OWNER_EMAILS in Sites runtime settings.",
  PACKAGE_NOT_STAGED: "Stage the package first (cycle --site-url or stage-hosted), or it was withdrawn.",
  ACTIVATION_CONFLICT: "The active package changed since this page loaded. Refresh and try again.",
  WITHDRAW_CONFLICT: "The active package changed since this page loaded, so nothing was withdrawn. Check the active package and try again.",
  ROLLBACK_BINDING_MISMATCH: "This package was prepared for a different previous package. Run cycle --site-url again so it binds the current active package.",
  RELEASE_BINDING_MISMATCH: "This decision was written for the other layer family. Paste the decision for this layer.",
  INDEPENDENT_REVIEW_REQUIRED: "Reviewer and releaser match, and this package is not an admitted public source. Name a different reviewer.",
  RELEASE_TIME_INVALID: "The decision is expired or not yet valid. Write a new decision.",
};

async function fetchStatus(kind: ReleaseKind): Promise<{ status: Status | null; message: string }> {
  const response = await fetch(`/api/governed/${kind}-admin/status`, { cache: "no-store" });
  const body = await response.json();
  if (!response.ok) return { status: null, message: reasonText[body.reason_code] ?? `Status unavailable (${body.reason_code}).` };
  return { status: body, message: body.active_package_id ? `A ${kind} package is active.` : `No ${kind} package is active yet.` };
}

export default function WaterReleaseConsole() { return <ReleaseConsole kind="water" />; }

/** Owner console for one layer family; each family has its own admin routes, tables and decisions. */
export function ReleaseConsole({ kind }: { kind: ReleaseKind }) {
  const [status, setStatus] = useState<Status | null>(null);
  const [decisionText, setDecisionText] = useState("");
  const [message, setMessage] = useState("Loading the active package…");
  const [busy, setBusy] = useState(false);
  const [now, setNow] = useState(() => Date.now());

  useEffect(() => {
    let live = true;
    void fetchStatus(kind).then((loaded) => { if (live) { setStatus(loaded.status); setMessage(loaded.message); } });
    // Advance the expiry wording while the page stays open.
    const tick = setInterval(() => setNow(Date.now()), 60_000);
    return () => { live = false; clearInterval(tick); };
  }, [kind]);

  let decision: Record<string, unknown> | null = null;
  try { decision = decisionText.trim() ? JSON.parse(decisionText) : null; } catch { decision = null; }
  const packageId = typeof decision?.package_id === "string" ? decision.package_id : null;

  async function send(path: string, body: unknown, done: string) {
    setBusy(true);
    try {
      const response = await fetch(path, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(body) });
      const result: Result = await response.json();
      setMessage(response.ok ? `${done} Revision ${result.revision ?? "–"}.` : reasonText[result.reason_code ?? ""] ?? `Refused: ${result.reason_code}.`);
      setStatus((await fetchStatus(kind)).status);
      setNow(Date.now());
    } finally { setBusy(false); }
  }

  const activate = (rollback: boolean) => send(`/api/governed/${kind}-admin/activate`,
    { package_id: packageId, decision, expected_active: status?.active_package_id ?? null, rollback },
    rollback ? "Rolled back." : "Activated.");
  const withdraw = () => status?.active_package_id && send(`/api/governed/${kind}-admin/withdraw`,
    { package_id: status.active_package_id, expected_active: status.active_package_id }, "Withdrawn; the layer stops serving now.");

  return <section aria-labelledby={`${kind}-release-heading`} style={{ display: "grid", gap: 16 }}>
    <h2 id={`${kind}-release-heading`} style={{ margin: 0 }}>Active {kind} package</h2>
    <dl style={{ display: "grid", gridTemplateColumns: "max-content 1fr", gap: "4px 16px", margin: 0 }}>
      <dt>Active</dt><dd style={{ margin: 0, overflowWrap: "anywhere" }}><code>{status?.active_package_id ?? "none"}</code></dd>
      <dt>Previous</dt><dd style={{ margin: 0, overflowWrap: "anywhere" }}><code>{status?.previous_package_id ?? "none"}</code></dd>
      <dt>Revision</dt><dd style={{ margin: 0 }}>{status?.revision ?? "–"}</dd>
      <dt>Decision expires</dt><dd style={{ margin: 0 }}>{expiryText(status, now)}</dd>
    </dl>
    <label htmlFor={`${kind}-decision`} style={{ fontWeight: 600 }}>Release decision (paste the file written by <code>{TOOL[kind]} decide</code> or <code>cycle</code>)</label>
    <textarea id={`${kind}-decision`} rows={10} value={decisionText} onChange={(event) => setDecisionText(event.target.value)}
      spellCheck={false} style={{ fontFamily: "ui-monospace, monospace", fontSize: 13, width: "100%" }} />
    <p style={{ margin: 0 }}>{decisionText && !packageId ? "This is not a valid decision record." : packageId ? <>Package <code style={{ overflowWrap: "anywhere" }}>{packageId}</code></> : " "}</p>
    <div style={{ display: "flex", flexWrap: "wrap", gap: 8 }}>
      <button type="button" disabled={busy || !packageId || !status} onClick={() => void activate(false)}>Activate package</button>
      <button type="button" disabled={busy || !packageId || !status?.previous_package_id || packageId !== status.previous_package_id} onClick={() => void activate(true)}>Roll back to previous</button>
      <button type="button" disabled={busy || !status?.active_package_id} onClick={() => void withdraw()}>Withdraw active package</button>
    </div>
    <p role="status" aria-live="polite" style={{ margin: 0 }}>{message}</p>
    {expiryWarning(status, now, TOOL[kind]) && <p role="alert" style={{ margin: 0, fontWeight: 600 }}>{expiryWarning(status, now, TOOL[kind])}</p>}
  </section>;
}
