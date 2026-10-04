"use client";
import { useEffect, useMemo, useRef, useState } from "react";
import { loadLightningArchive } from "./lightning-archive-client";
import type { GlmFlashSnapshot } from "./lightning-flashes";
import { LIGHTNING_DAY, LIGHTNING_HOUR, lightningYearHour, lightningYearQuery, lightningYearRange, nextLightningYearHour } from "./lightning-year";

const label = (ms: number) => new Date(ms).toISOString().slice(0, 16).replace("T", " ") + " UTC";

export function LightningYearControl({ reducedMotion, onClear, onSnapshot }: {
  reducedMotion: boolean; onClear: () => void; onSnapshot: (snapshot: GlmFlashSnapshot) => void;
}) {
  const [now] = useState(() => Date.now());
  const currentYear = new Date(now).getUTCFullYear();
  const [year, setYear] = useState(currentYear - 1);
  const range = useMemo(() => lightningYearRange(year, now), [year, now]);
  const [hour, setHour] = useState(() => lightningYearRange(currentYear - 1, now).start);
  const [playingRequested, setPlaying] = useState(false), [loop, setLoop] = useState(true);
  const playing = playingRequested && !reducedMotion;
  const [holdSeconds, setHoldSeconds] = useState(3);
  const [busy, setBusy] = useState(false), [loadedHour, setLoadedHour] = useState<number | null>(null);
  const [request, setRequest] = useState(0);
  const [status, setStatus] = useState("Choose a year and press Play year. Each frame shows a full observed hour.");
  const cached = useRef<{ hour: number; snapshot: GlmFlashSnapshot } | null>(null);
  const active = useRef<AbortController | null>(null);
  const requested = useRef(0);
  const generation = useRef(0);

  // A single decoded hour stays in memory; the year is never downloaded in bulk.
  useEffect(() => {
    const manual = request !== requested.current;
    requested.current = request;
    if (!playing && !manual) return;
    if (cached.current?.hour === hour) {
      setLoadedHour(hour); onSnapshot(cached.current.snapshot); return;
    }
    const abort = new AbortController(); active.current = abort;
    const token = ++generation.current;
    let disposed = false;
    setLoadedHour(null); setBusy(true); onClear();
    setStatus(`Loading ${label(hour)}…`);
    const timeout = window.setTimeout(() => abort.abort(), 8 * 60_000);
    void loadLightningArchive(lightningYearQuery(hour), abort.signal, (done, total) => {
      if (!disposed && token === generation.current) setStatus(`Loading ${label(hour)} · ${done}/${total} observation files`);
    }).then(snapshot => {
      if (disposed || token !== generation.current || abort.signal.aborted) return;
      cached.current = { hour, snapshot }; setLoadedHour(hour); onSnapshot(snapshot);
      setStatus(`${label(hour)} – ${new Date(hour + LIGHTNING_HOUR).toISOString().slice(11, 16)} UTC · ${snapshot.providerCount.toLocaleString()} returned centroids.${snapshot.partialReason ? ` ${snapshot.partialReason}` : ""}`);
    }).catch(error => {
      if (disposed || token !== generation.current) return;
      setPlaying(false); onClear();
      setStatus(`Playback paused at ${label(hour)}. ${abort.signal.aborted ? "Loading timed out." : error instanceof Error ? error.message : "Archive unavailable."} This hour remains unknown. Retry or move to another day.`);
    }).finally(() => {
      window.clearTimeout(timeout); if (!disposed) setBusy(false);
    });
    return () => { disposed = true; abort.abort(); window.clearTimeout(timeout); active.current = null; setBusy(false); };
  }, [hour, playing, request, onClear, onSnapshot]);

  useEffect(() => {
    if (!playing || reducedMotion || busy || loadedHour !== hour) return;
    const timer = window.setTimeout(() => {
      const next = nextLightningYearHour(hour, range, loop);
      if (next === null) { setPlaying(false); setStatus("Reached the end of the available year. Press Restart year to play it again."); }
      else { setLoadedHour(null); setHour(next); }
    }, holdSeconds * 1000);
    return () => window.clearTimeout(timer);
  }, [playing, reducedMotion, busy, loadedHour, hour, range, loop, holdSeconds]);

  useEffect(() => {
    const pause = () => { if (document.hidden) { generation.current++; active.current?.abort(); setBusy(false); setPlaying(false); } };
    document.addEventListener("visibilitychange", pause);
    return () => document.removeEventListener("visibilitychange", pause);
  }, []);

  const seek = (value: number) => {
    generation.current++; active.current?.abort(); cached.current = null; setLoadedHour(null); onClear();
    setHour(lightningYearHour(value, range)); setRequest(n => n + 1);
  };
  const changeYear = (value: number) => {
    generation.current++; active.current?.abort(); cached.current = null; setPlaying(false); setLoadedHour(null); onClear();
    setYear(value); setHour(lightningYearRange(value, now).start);
    setStatus("Year selected. Press Play year to begin at its first available hour.");
  };
  const firstDay = Math.floor(range.start / LIGHTNING_DAY), lastDay = Math.floor((range.end - 1) / LIGHTNING_DAY);
  return <section className="glm-archive-controls glm-year-controls" aria-label="Whole year lightning playback">
    <div className="glm-year-heading"><label>Year<select value={year} onChange={e => changeYear(+e.target.value)}>{Array.from({ length: currentYear - 2017 + 1 }, (_, i) => currentYear - i).map(y => <option key={y}>{y}{y === currentYear ? " · so far" : ""}</option>)}</select></label><div><strong>{label(hour)}</strong><small>{range.hours.toLocaleString()} calendar hours to explore{range.partial ? " · partial year" : ""}</small></div></div>
    <div className="glm-flash-actions"><button type="button" aria-pressed={playing} disabled={reducedMotion} onClick={() => {
      if (playing) { generation.current++; active.current?.abort(); setBusy(false); if (busy) setStatus("Paused while loading. Press Play year to resume this hour."); }
      setPlaying(value => !value);
    }}>{playing ? "Pause year" : loadedHour === null ? "Play year" : "Resume year"}</button><button type="button" onClick={() => { seek(range.start); setPlaying(!reducedMotion); }}>Restart year</button><button type="button" disabled={busy} onClick={() => { generation.current++; active.current?.abort(); cached.current = null; setRequest(n => n + 1); }}>Load / retry hour</button><label><input type="checkbox" checked={loop} onChange={e => setLoop(e.target.checked)} /> Loop year</label></div>
    <label className="glm-year-scrub">Jump to a day<input type="range" min={firstDay} max={lastDay} step="1" value={Math.floor(hour / LIGHTNING_DAY)} onChange={e => seek(+e.target.value * LIGHTNING_DAY)} aria-label="Day within the lightning year" aria-valuetext={new Date(hour).toISOString().slice(0, 10)} /></label>
    <div className="glm-year-months" role="group" aria-label="Jump to month">{Array.from({ length: 12 }, (_, month) => {
      const start = Date.UTC(year, month, 1), end = Date.UTC(year, month + 1, 1);
      return <button type="button" key={month} disabled={end <= range.start || start >= range.end} aria-pressed={new Date(hour).getUTCMonth() === month} onClick={() => seek(start)}>{new Date(start).toLocaleString("en-US", { month: "short", timeZone: "UTC" })}</button>;
    })}</div>
    <div className="glm-flash-actions"><button type="button" disabled={hour === range.start} onClick={() => seek(hour - LIGHTNING_DAY)}>Previous day</button><button type="button" disabled={Math.floor(hour / LIGHTNING_DAY) === lastDay} onClick={() => seek(hour + LIGHTNING_DAY)}>Next day</button><label>Hold each hour<select value={holdSeconds} onChange={e => setHoldSeconds(+e.target.value)}><option value={1}>1 second</option><option value={3}>3 seconds</option><option value={6}>6 seconds</option></select></label></div>
    <output role="status">{status}</output>
    <small>Every available hour plays in order, including quiet hours. NOAA’s full archive is large: loading each hour can take a minute or longer, and a whole year can take days. Playback waits for observations; it does not sample or invent flashes. Jump to any month or day to explore faster. Dates are UTC.</small>
    {reducedMotion && <small>Reduced motion is active. Use the calendar and Load / retry hour to view still frames.</small>}
  </section>;
}
