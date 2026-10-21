"use client";
import { useEffect, useRef, useState } from "react";
import { createAviationSession, aviationQuestion } from "./aviation-session.mjs";

/** Bounded held control inside the existing map. No competing Explorer surface. */
export function AviationControl({ contextKey }: { contextKey: string }) {
  const [open, setOpen] = useState(false), [county, setCounty] = useState("ELLSWORTH"), [edition, setEdition] = useState("present");
  const [status, setStatus] = useState("HELD · No reviewed aviation release is available."), [busy, setBusy] = useState(false);
  const session = useRef(createAviationSession());
  const retire = () => { session.current.retire(); setBusy(false); setStatus("HELD · Selection changed. No released aviation features."); };
  useEffect(() => { const current = session.current; return () => current.retire(); }, []);
  useEffect(() => { session.current.retire(); setBusy(false); setStatus("HELD · Map context changed. No released aviation features."); }, [contextKey]);
  const check = async () => {
    const token = session.current.begin(); setBusy(true); setStatus("Checking released aviation availability…");
    try {
      const query = new URLSearchParams({ county: county.trim().toUpperCase(), edition });
      const response = await fetch(`/api/aviation/airports?${query}`, { signal: token.signal, cache: "no-store" });
      const value = await response.json();
      if (token.current()) setStatus(value.envelope?.reason_code === "AVIATION_RELEASE_PROFILE_REQUIRED"
        ? "HELD · No reviewed FAA aviation release is available."
        : "Unavailable · aviation query could not be completed.");
    } catch { if (token.current()) setStatus("Unavailable · aviation service could not be reached."); }
    finally { if (token.current()) setBusy(false); }
  };
  return <details open={open} className="governed-water-control" onToggle={e => { const visible = e.currentTarget.open; setOpen(visible); if (!visible) retire(); }}>
    <summary>Aviation research · held</summary>
    <p>Research/context only. Not for navigation or flight planning.</p>
    <label>County association<input value={county} maxLength={64} onChange={e => { retire(); setCounty(e.target.value); }} /></label>
    <label>Reference edition<select value={edition} onChange={e => { retire(); setEdition(e.target.value); }}><option value="present">Present · released editions</option><option value="2026-10-01">2026-10-01 · candidate held</option></select></label>
    <button disabled={busy} onClick={() => void check()}>Check availability</button>
    <button onClick={() => { retire(); setEdition("present"); }}>Present</button>
    <p role="status" aria-live="polite">{status}</p>
    <details><summary>Evidence & AI</summary><p>No released feature is selected. Evidence lookup and reports require a stable feature ID and a resolved EvidenceBundle. Observation playback is unavailable.</p>
      <p>You are interacting with AI. Aviation answers require released evidence.</p>
      <button onClick={() => { retire(); const answer = aviationQuestion("county-airports", { county, edition }); setStatus(`${answer.outcome} · No released airport evidence is available for this query.`); }}>Ask AI about this county</button>
      <p>OpenSky operational integration requires written permission. Independent feeds require their own admission and coverage review.</p>
      <a href="https://www.faa.gov/air_traffic/flight_info/aeronav/aero_data/NASR_Subscription/" target="_blank" rel="noreferrer">FAA editions and product documentation ↗</a>
    </details>
  </details>;
}
