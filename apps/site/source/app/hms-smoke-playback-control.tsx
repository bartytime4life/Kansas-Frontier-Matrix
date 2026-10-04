"use client";
import { useCallback, useEffect, useRef, useState } from "react";
import { HMS_FIRST_DAY, HmsFrameCache, hmsAdvance, hmsDayNumber, hmsToday, hmsValidDay } from "./hms-smoke-playback";
import type { OfficialContextPayload } from "./live-context";

export function HmsSmokePlayback({ enabled, reducedMotion, displayedDay, payload, onReserve, onFrame, onCurrent }: {
  enabled: boolean; reducedMotion: boolean; displayedDay?: string; payload?: OfficialContextPayload;
  onReserve: (day: string) => void;
  onFrame: (day: string, payload: OfficialContextPayload, signal: AbortSignal, smooth: boolean) => Promise<void>;
  onCurrent: () => void;
}) {
  const [today, setToday] = useState(hmsToday);
  const [from, setFrom] = useState(() => hmsAdvance(hmsToday(), -6));
  const [through, setThrough] = useState(hmsToday);
  const [cursor, setCursor] = useState(hmsToday);
  const [playing, setPlaying] = useState(false), [busy, setBusy] = useState(false);
  const [smooth, setSmooth] = useState(true), [loop, setLoop] = useState(false), [speed, setSpeed] = useState(1500);
  const [status, setStatus] = useState("Select a range and play daily NOAA publications.");
  const cache = useRef(new HmsFrameCache()), request = useRef<AbortController | null>(null), prefetch = useRef<AbortController | null>(null);
  const generation = useRef(0);
  const valid = hmsValidDay(from, today) && hmsValidDay(through, today) && from <= through;
  const stop = useCallback(() => { generation.current++; request.current?.abort(); prefetch.current?.abort(); setBusy(false); setPlaying(false); }, []);
  useEffect(() => {
    if (!enabled || reducedMotion) stop();
  }, [enabled, reducedMotion, stop]);
  useEffect(() => {
    const hidden = () => { if (document.hidden) stop(); };
    document.addEventListener("visibilitychange", hidden);
    const clock = setInterval(() => setToday(hmsToday()), 60_000);
    return () => { request.current?.abort(); prefetch.current?.abort(); generation.current++; clearInterval(clock); document.removeEventListener("visibilitychange", hidden); };
  }, [stop]);
  const show = useCallback(async (day: string) => {
    request.current?.abort(); prefetch.current?.abort();
    const token = ++generation.current, controller = new AbortController(); request.current = controller;
    setCursor(day); setBusy(true); setStatus(`Checking ${day} UTC; displayed frame retained until ready.`); onReserve(day);
    let publicationReady = false;
    try {
      const next = await cache.current.get(day, controller.signal);
      if (generation.current !== token) return;
      publicationReady = true;
      await onFrame(day, next, controller.signal, smooth && !reducedMotion);
      if (generation.current !== token) return;
      setStatus(`${day} UTC · ${next.featureCount} daily footprints${next.state === "partial" ? " · partial publication coverage" : ""}. No polygons is not an all-clear.`);
      if (day < through) {
        const ahead = new AbortController(); prefetch.current = ahead;
        void cache.current.get(hmsAdvance(day, 1), ahead.signal).catch(() => {});
      }
    } catch {
      if (generation.current === token && !controller.signal.aborted) {
        setStatus(publicationReady
          ? `Map update for ${day} UTC did not complete. The displayed date was not advanced. Retry when the map is ready.`
          : `Publication for ${day} UTC could not be checked. Last displayed date retained. Retry or use Next day to skip explicitly.`); setPlaying(false);
      }
    } finally { if (generation.current === token) setBusy(false); }
  }, [onFrame, onReserve, reducedMotion, smooth, through]);
  useEffect(() => {
    if (!playing || busy || !valid || !enabled || reducedMotion) return;
    const next = cursor < through ? hmsAdvance(cursor, 1) : loop ? from : null;
    if (!next) { setPlaying(false); return; }
    const timer = setTimeout(() => void show(next), speed);
    return () => clearTimeout(timer);
  }, [playing, busy, valid, enabled, reducedMotion, cursor, through, loop, from, show, speed]);
  const choose = (start: string) => { stop(); setFrom(start); setThrough(today); setCursor(start); };
  return <div className="hms-playback">
    <p>Daily analyzed smoke footprints, not live measurements or inferred plume motion. Archive begins August 5, 2005; missing publications remain gaps.</p>
    <div className="source-time-actions"><button type="button" onClick={() => choose(hmsAdvance(today, -6))}>7 days</button><button type="button" onClick={() => choose(hmsAdvance(today, -29))}>30 days</button><button type="button" onClick={() => choose(HMS_FIRST_DAY)}>Full archive → latest</button></div>
    <div className="source-time-actions"><label>From UTC<input aria-label="HMS from date" type="date" min={HMS_FIRST_DAY} max={today} value={from} onChange={e => { stop(); setFrom(e.target.value); setCursor(e.target.value); }} /></label><label>Through UTC<input aria-label="HMS through date" type="date" min={from || HMS_FIRST_DAY} max={today} value={through} onChange={e => { stop(); setThrough(e.target.value); }} /></label></div>
    <label>Requested day<input aria-label="HMS playback day" type="date" min={from} max={through} value={cursor} onChange={e => { stop(); setCursor(e.target.value); }} /></label>
    <input type="range" aria-label="HMS archive scrubber" min={0} max={valid ? hmsDayNumber(through) - hmsDayNumber(from) : 0} value={valid ? Math.max(0, Math.min(hmsDayNumber(through) - hmsDayNumber(from), hmsDayNumber(cursor) - hmsDayNumber(from) || 0)) : 0} disabled={!valid || !enabled} onChange={e => { stop(); setCursor(hmsAdvance(from, Number(e.target.value))); }} onPointerUp={() => { if (valid) void show(cursor); }} onKeyUp={e => { if (["ArrowLeft", "ArrowRight", "Home", "End"].includes(e.key) && valid) void show(cursor); }} />
    <div className="source-time-actions"><button type="button" disabled={!valid || !enabled || reducedMotion} onClick={() => { if (playing) stop(); else { setPlaying(true); void show(cursor >= from && cursor <= through ? cursor : from); } }}>{playing ? "Pause" : "Play"}</button><button type="button" disabled={!enabled || !hmsValidDay(cursor) || busy} onClick={() => { stop(); void show(cursor); }}>Check / retry day</button><button type="button" disabled={!enabled || !valid || !hmsValidDay(cursor) || cursor >= through} onClick={() => { stop(); void show(hmsAdvance(cursor, 1)); }}>Next day</button><button type="button" disabled={!enabled} onClick={() => { stop(); setCursor(today); setStatus("Following the latest rolling publication window; source retrieval and coverage are shown below."); onCurrent(); }}>Follow latest publication</button></div>
    <div className="source-time-actions"><label>Frame hold<select aria-label="HMS playback speed" value={speed} onChange={e => setSpeed(Number(e.target.value))}><option value={500}>0.5 seconds</option><option value={1500}>1.5 seconds</option><option value={3000}>3 seconds</option></select></label><label><input type="checkbox" checked={smooth} disabled={reducedMotion} onChange={e => setSmooth(e.target.checked)} />Smooth fade</label><label><input type="checkbox" checked={loop} onChange={e => setLoop(e.target.checked)} />Repeat range</label></div>
    <output aria-live="polite">{status}</output>
    <small>Displayed: {displayedDay ? `${displayedDay} UTC daily footprints` : "latest rolling publication window"}{payload ? ` · retrieved ${payload.retrievedAt.slice(0, 16).replace("T", " ")} UTC` : " · no loaded frame"}. {valid ? `${hmsDayNumber(through) - hmsDayNumber(from) + 1} calendar days requested; coverage checked on demand.` : "Choose a valid range."}</small>
    {payload?.smokeCoverage?.missingDays.length ? <small>Missing publication days: {payload.smokeCoverage.missingDays.join(", ")}.</small> : null}
    <small>{reducedMotion ? "Reduced motion: manual steps available; autoplay and fading disabled." : "Smooth mode fades out, swaps the exact checked daily geometry, then fades in. It does not move or blend plume boundaries."}</small>
    <a href="https://www.ospo.noaa.gov/products/land/hms.html" target="_blank" rel="noreferrer">NOAA HMS methods and archive limits ↗</a>
  </div>;
}
