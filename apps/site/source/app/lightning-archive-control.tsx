"use client";
import { useEffect, useRef, useState } from "react";
import { GLM_ARCHIVE_FIRST_DAY } from "./lightning-archive";
import { loadLightningArchive } from "./lightning-archive-client";
import type { GlmFlashSnapshot } from "./lightning-flashes";

export function LightningArchiveControl({ onClear, onSnapshot }: { onClear: () => void; onSnapshot: (snapshot: GlmFlashSnapshot) => void }) {
  const [today] = useState(() => new Date().toISOString().slice(0, 10));
  const [day, setDay] = useState(() => new Date(Date.now() - 86400000).toISOString().slice(0, 10));
  const [hour, setHour] = useState(18), [minute, setMinute] = useState(0);
  const [duration, setDuration] = useState<15 | 30 | 60>(15);
  const [busy, setBusy] = useState(false), [status, setStatus] = useState("Choose a UTC date and interval, then load its observed flashes.");
  const active = useRef<AbortController | null>(null), generation = useRef(0);
  useEffect(() => () => { generation.current++; active.current?.abort(); }, []);
  const clear = () => { generation.current++; active.current?.abort(); setBusy(false); onClear(); setStatus("Selection changed. Load this interval to view its observations."); };
  const setCalendar = (year: number, month: number, date: number) => {
    clear();
    const days = new Date(Date.UTC(year, month, 0)).getUTCDate();
    setDay(`${year}-${String(month).padStart(2, "0")}-${String(Math.min(date, days)).padStart(2, "0")}`);
  };
  const [year, month, date] = day.split("-").map(Number);
  const load = async () => {
    clear(); const token = ++generation.current, controller = new AbortController(); active.current = controller;
    setBusy(true); setStatus("Checking NOAA’s archived observation files…");
    const timeout = setTimeout(() => controller.abort(), 8 * 60_000);
    try {
      const snapshot = await loadLightningArchive({ day, hour, minute, duration }, controller.signal, (done, total) => {
        if (generation.current === token) setStatus(`Loading ${day} UTC · ${done}/${total} observation files. You can cancel or change the date.`);
      });
      if (generation.current !== token) return;
      onSnapshot(snapshot); setStatus(`${day} UTC · ${snapshot.providerCount} returned Kansas-area flash centroids · ${snapshot.archive?.files} observation files checked.${snapshot.partialReason ? ` ${snapshot.partialReason}` : ""}`);
    } catch (error) {
      if (generation.current === token) setStatus(controller.signal.aborted ? "Archive loading stopped. Retry or select a shorter interval." : error instanceof Error ? error.message : "Archive unavailable.");
    } finally { clearTimeout(timeout); if (generation.current === token) setBusy(false); }
  };
  return <section className="glm-archive-controls" aria-label="Historical lightning calendar">
    <div className="glm-flash-settings">
      <label>Year<select value={year} onChange={e => setCalendar(+e.target.value, month, date)}>{Array.from({ length: +today.slice(0, 4) - 2017 + 1 }, (_, i) => 2017 + i).reverse().map(y => <option key={y}>{y}</option>)}</select></label>
      <label>Month<select value={month} onChange={e => setCalendar(year, +e.target.value, date)}>{Array.from({ length: 12 }, (_, i) => <option key={i + 1} value={i + 1}>{new Date(Date.UTC(2024, i, 1)).toLocaleString("en-US", { month: "long", timeZone: "UTC" })}</option>)}</select></label>
      <label>Day<select value={date} onChange={e => setCalendar(year, month, +e.target.value)}>{Array.from({ length: new Date(Date.UTC(year, month, 0)).getUTCDate() }, (_, i) => <option key={i + 1}>{i + 1}</option>)}</select></label>
      <label>Hour · UTC<select value={hour} onChange={e => { clear(); setHour(+e.target.value); }}>{Array.from({ length: 24 }, (_, i) => <option key={i} value={i}>{String(i).padStart(2, "0")}:00</option>)}</select></label>
      <label>Interval<select value={duration} onChange={e => { clear(); setDuration(+e.target.value as 15 | 30 | 60); setMinute(0); }}><option value={15}>15 minutes</option><option value={30}>Half-hour</option><option value={60}>One hour</option></select></label>
      <label>Start minute<select value={minute} onChange={e => { clear(); setMinute(+e.target.value); }}>{Array.from({ length: 60 / duration }, (_, i) => <option key={i * duration} value={i * duration}>:{String(i * duration).padStart(2, "0")}</option>)}</select></label>
    </div>
    <div className="glm-flash-actions"><button type="button" disabled={busy || day < GLM_ARCHIVE_FIRST_DAY || day > today} onClick={() => void load()}>Load selected interval</button>{busy && <button type="button" onClick={clear}>Cancel</button>}</div>
    <output role="status">{status}</output>
    <small>NOAA GOES-East archive · July 5, 2017 onward, with gaps. Load one interval at a time; a whole month is not downloaded. All dates and times are UTC.</small>
  </section>;
}
