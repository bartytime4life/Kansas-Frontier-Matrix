"use client";
import { useCallback, useEffect, useState } from "react";
import Link from "next/link";
import { HostedSourceStatus } from "../hosted-source-status";
type Receipt = { captureId: string; sourceId: string; retrievedAt: string; byteLength: number; sha256: string; validation: string; lifecycle: string; partial: boolean; limitation: string };
export default function SourceOperations() {
  const [owner, setOwner] = useState(false), [checking, setChecking] = useState(true), [busy, setBusy] = useState(false);
  const [message, setMessage] = useState(""); const [receipts, setReceipts] = useState<Receipt[]>([]);
  const [revision, setRevision] = useState(0);
  const refreshReceipts = useCallback(async (signal?: AbortSignal) => {
    const response = await fetch("/api/source-pipeline/captures", { cache: "no-store", signal });
    if (!response.ok) throw new Error("Capture receipts unavailable.");
    const value = await response.json(); if (!signal?.aborted) setReceipts(value.captures);
  }, []);
  useEffect(() => { const controller = new AbortController();
    void (async () => { try {
      const response = await fetch("/api/owner/session", { cache: "no-store", signal: controller.signal }); const value = await response.json();
      if (!controller.signal.aborted) setOwner(value.owner === true);
      if (value.owner) await refreshReceipts(controller.signal);
    } catch { if (!controller.signal.aborted) setMessage("Owner session or archive unavailable."); }
    finally { if (!controller.signal.aborted) setChecking(false); } })();
    return () => controller.abort();
  }, [refreshReceipts]);
  const operate = async (action: "pause" | "resume" | "capture") => {
    setBusy(true); setMessage("");
    try {
      const response = await fetch(action === "capture" ? "/api/source-pipeline/run" : `/api/source-pipeline/control?action=${action}`, { method: "POST" });
      const result = await response.json(); if (!response.ok) throw new Error(result.error ?? "Operation held.");
      setMessage(action === "capture" ? `${result.captured ?? 0} capture(s) stored. ${result.state === "complete" ? "Review is still required." : "Check the source status for holds."}` : action === "pause" ? "Scheduled capture paused." : "Capture enabled; waiting for the scheduler.");
      setRevision(value => value + 1); await refreshReceipts();
    } catch (error) { setMessage(error instanceof Error ? error.message : "Operation held."); }
    finally { setBusy(false); }
  };
  return <main className="source-operations"><nav><Link href="/?layers=sources">← Explorer source status</Link><Link href="/">Map</Link></nav><header><p>Owner workspace</p><h1>Source operations</h1><p>Preserve source data, inspect capture receipts, and pause or resume the schedule. Review and release remain separate.</p></header>
    <HostedSourceStatus key={revision} /><p><Link href="/connections">Capture and inspect all API connections ↗</Link></p>
    {checking ? <p>Checking owner session…</p> : !owner ? <section><h2>Owner access</h2><p>Only bartytime4life can sign in. The connection uses public GitHub identity and requests no repository or email access.</p><a className="source-sign-in" href="/api/owner/sign-in">Sign in with GitHub</a><p>Sign-in stays unavailable until the hosting connection and identity app are configured.</p></section> : <>
      <section><h2>Capture controls</h2><div className="source-operation-actions"><button disabled={busy} onClick={() => void operate("pause")}>Pause capture</button><button disabled={busy} onClick={() => void operate("resume")}>Resume capture</button><button disabled={busy} onClick={() => void operate("capture")}>Capture due sources</button><form method="post" action="/api/owner/sign-out"><button disabled={busy}>Sign out</button></form></div><p>The 80 GB cap stops new captures; it never deletes an archive to make room. Missed schedule windows stay missing.</p></section>
      <section><h2>Latest capture receipts</h2><p>Latest 50 captures. Original bytes and receipts remain unreleased; structural validation is not rights, sensitivity or publication approval.</p>{receipts.length === 0 ? <p>No captures recorded.</p> : <ol>{receipts.map(receipt => <li key={receipt.captureId}><h3>{receipt.sourceId}</h3><p>{receipt.retrievedAt} · {receipt.byteLength.toLocaleString()} bytes · {receipt.validation}{receipt.partial ? " · partial coverage" : ""}</p><p>{receipt.limitation}</p><code>SHA-256 {receipt.sha256}</code><a href={`/api/source-pipeline/captures?id=${receipt.captureId}`}>Download original entity bytes</a></li>)}</ol>}</section>
    </>}
    <p role="status" aria-live="polite">{message}</p>
  </main>;
}
