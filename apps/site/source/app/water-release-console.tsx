"use client";
import { useEffect, useState } from "react";

type Status = { active_package_id: string | null; previous_package_id: string | null; revision: number; decision_expires_at: string | null; checked_at: number };

const REFRESH_WARNING_MS = 2 * 24 * 60 * 60 * 1000;

function expiryText(status: Status | null) {
  if (!status?.active_package_id || !status.decision_expires_at) return "–";
  const remaining = Date.parse(status.decision_expires_at) - status.checked_at;
  if (remaining <= 0) return `${status.decision_expires_at} (expired; the layer is not serving)`;
  const hours = Math.floor(remaining / 3_600_000);
  return `${status.decision_expires_at} (in ${hours >= 48 ? `${Math.floor(hours / 24)} days` : `${hours} hours`})`;
}

function statusMessage(status: Status) {
  if (!status.active_package_id) return "No water package is active yet.";
  const remaining = status.decision_expires_at ? Date.parse(status.decision_expires_at) - status.checked_at : Infinity;
  if (remaining <= 0) return "The active decision has expired, so the layer is not serving. Run water_release.py cycle and activate the new package.";
  if (remaining <= REFRESH_WARNING_MS) return "The active decision expires soon. Run water_release.py cycle and activate the new package before it does.";
  return "A water package is active.";
}
type Result = { outcome: string; reason_code?: string; package_id?: string; revision?: number };

const reasonText: Record<string, string> = {
  OWNER_REQUIRED: "This account is not on the water release owner list.",
  WATER_RELEASE_NOT_CONFIGURED: "Set KFM_WATER_OWNER_IDS or KFM_WATER_OWNER_EMAILS in Sites runtime settings.",
  PACKAGE_NOT_STAGED: "Stage the package first (water_release.py cycle --site-url or stage-hosted), or it was withdrawn.",
  ACTIVATION_CONFLICT: "The active package changed since this page loaded. Refresh and try again.",
  WITHDRAW_CONFLICT: "The active package changed since this page loaded, so nothing was withdrawn. Check the active package and try again.",
  ROLLBACK_BINDING_MISMATCH: "This package was prepared for a different previous package. Run water_release.py cycle --site-url again so it binds the current active package.",
  INDEPENDENT_REVIEW_REQUIRED: "Reviewer and releaser match, and this package is not an admitted public source. Name a different reviewer.",
  RELEASE_TIME_INVALID: "The decision is expired or not yet valid. Write a new decision.",
};

async function fetchStatus(): Promise<{ status: Status | null; message: string }> {
  const response = await fetch("/api/governed/water-admin/status", { cache: "no-store" });
  const body = await response.json();
  if (!response.ok) return { status: null, message: reasonText[body.reason_code] ?? `Status unavailable (${body.reason_code}).` };
  const status: Status = { ...body, checked_at: Date.now() };
  return { status, message: statusMessage(status) };
}

export default function WaterReleaseConsole() {
  const [status, setStatus] = useState<Status | null>(null);
  const [decisionText, setDecisionText] = useState("");
  const [message, setMessage] = useState("Loading the active package…");
  const [busy, setBusy] = useState(false);

  useEffect(() => {
    let live = true;
    void fetchStatus().then((loaded) => { if (live) { setStatus(loaded.status); setMessage(loaded.message); } });
    return () => { live = false; };
  }, []);

  let decision: Record<string, unknown> | null = null;
  try { decision = decisionText.trim() ? JSON.parse(decisionText) : null; } catch { decision = null; }
  const packageId = typeof decision?.package_id === "string" ? decision.package_id : null;

  async function send(path: string, body: unknown, done: string) {
    setBusy(true);
    try {
      const response = await fetch(path, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(body) });
      const result: Result = await response.json();
      setMessage(response.ok ? `${done} Revision ${result.revision ?? "–"}.` : reasonText[result.reason_code ?? ""] ?? `Refused: ${result.reason_code}.`);
      setStatus((await fetchStatus()).status);
    } finally { setBusy(false); }
  }

  const activate = (rollback: boolean) => send("/api/governed/water-admin/activate",
    { package_id: packageId, decision, expected_active: status?.active_package_id ?? null, rollback },
    rollback ? "Rolled back." : "Activated.");
  const withdraw = () => status?.active_package_id && send("/api/governed/water-admin/withdraw",
    { package_id: status.active_package_id, expected_active: status.active_package_id }, "Withdrawn; the layer stops serving now.");

  return <section aria-labelledby="water-release-heading" style={{ display: "grid", gap: 16 }}>
    <h2 id="water-release-heading" style={{ margin: 0 }}>Active water package</h2>
    <dl style={{ display: "grid", gridTemplateColumns: "max-content 1fr", gap: "4px 16px", margin: 0 }}>
      <dt>Active</dt><dd style={{ margin: 0, overflowWrap: "anywhere" }}><code>{status?.active_package_id ?? "none"}</code></dd>
      <dt>Previous</dt><dd style={{ margin: 0, overflowWrap: "anywhere" }}><code>{status?.previous_package_id ?? "none"}</code></dd>
      <dt>Revision</dt><dd style={{ margin: 0 }}>{status?.revision ?? "–"}</dd>
      <dt>Decision expires</dt><dd style={{ margin: 0 }}>{expiryText(status)}</dd>
    </dl>
    <label htmlFor="water-decision" style={{ fontWeight: 600 }}>Release decision (paste the file written by <code>water_release.py decide</code>)</label>
    <textarea id="water-decision" rows={10} value={decisionText} onChange={(event) => setDecisionText(event.target.value)}
      spellCheck={false} style={{ fontFamily: "ui-monospace, monospace", fontSize: 13, width: "100%" }} />
    <p style={{ margin: 0 }}>{decisionText && !packageId ? "This is not a valid decision record." : packageId ? <>Package <code style={{ overflowWrap: "anywhere" }}>{packageId}</code></> : " "}</p>
    <div style={{ display: "flex", flexWrap: "wrap", gap: 8 }}>
      <button type="button" disabled={busy || !packageId || !status} onClick={() => void activate(false)}>Activate package</button>
      <button type="button" disabled={busy || !packageId || !status?.previous_package_id || packageId !== status.previous_package_id} onClick={() => void activate(true)}>Roll back to previous</button>
      <button type="button" disabled={busy || !status?.active_package_id} onClick={() => void withdraw()}>Withdraw active package</button>
    </div>
    <p role="status" aria-live="polite" style={{ margin: 0 }}>{message}</p>
  </section>;
}
