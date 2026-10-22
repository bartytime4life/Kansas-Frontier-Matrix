"use client";
import { useCallback, useEffect, useMemo, useRef, useState, type ReactNode } from "react";
import { calendarDateParts, calendarDayInRange, calendarFrameDay, calendarFrameIndex, calendarFrames, defaultCalendarSweep, replaceCalendarPart, validCalendarDay, type CalendarFrameOutcome, type CalendarStep, type CalendarSweepView } from "./calendar-sweep";
import "./compact-time-sweep.css";

export type CalendarSourceRow = Readonly<{ id: string; title: string; state: string; detail: string }>;
const months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
const shortDate = (day: string) => months[Number(day.slice(5, 7)) - 1] + " " + Number(day.slice(8)) + ", " + day.slice(0, 4);
// eslint-disable-next-line @next/next/no-img-element -- Fixed-size local library SVGs need no remote image service.
const icon = (name: string) => <img src={"/icons/time-sweep/" + name + ".svg"} width={20} height={20} alt="" aria-hidden="true" />;
export function CompactTimeSweep({ value, year, years, today, reducedMotion, open, onOpenChange, onSeek, onEra, onPresent, sources, imageryComparison, children }: {
  value: CalendarSweepView | null; year: number; years: readonly number[]; today: string; reducedMotion: boolean;
  open: boolean; onOpenChange: (open: boolean) => void;
  onSeek: (view: CalendarSweepView) => Promise<CalendarFrameOutcome>;
  onEra: (year: number) => void; onPresent: () => void;
  sources: readonly CalendarSourceRow[]; imageryComparison?: ReactNode; children?: ReactNode;
}) {
  const state = useMemo(() => value ?? defaultCalendarSweep(year, today), [value, year, today]);
  const date = calendarFrameDay(state);
  const era = year < 1800;
  const frames = useMemo(() => calendarFrames(state.start, state.end, state.step), [state.start, state.end, state.step]);
  const sourcesKey = sources.map(source => source.id).join(",");
  const [playIntent, setPlayIntent] = useState({ active: false, sources: "" });
  const setPlaying = useCallback((active: boolean) => setPlayIntent({ active, sources: sourcesKey }), [sourcesKey]);
  const playing = playIntent.active && playIntent.sources === sourcesKey && !reducedMotion && !era && state.showing === "B" && state.day < state.end;
  const [pending, setPending] = useState(false);
  const [expanded, setExpanded] = useState(false);
  const [checkedFrames, setCheckedFrames] = useState<{ sources: string; frames: ReadonlyMap<string, CalendarFrameOutcome> }>({ sources: "", frames: new Map() });
  const emblemRef = useRef<HTMLButtonElement>(null);
  const [speed, setSpeed] = useState(1), [skipGaps, setSkipGaps] = useState(false);
  const [scrubDay, setScrubDay] = useState<string | null>(null);
  const [outcome, setOutcome] = useState<CalendarFrameOutcome>({ state: "reference", message: "Choose a date to follow selected dated layers. Years and months are dated snapshots, not averages." });
  const [tab, setTab] = useState<"settings" | "compare">("settings");
  const [rangeError, setRangeError] = useState("");
  const requestId = useRef(0), mounted = useRef(true), scrubRef = useRef<string | null>(null);
  const visited = useRef(new Map<string, CalendarFrameOutcome>());
  const popupRef = useRef<HTMLDivElement>(null), settingsRef = useRef<HTMLButtonElement>(null), rootRef = useRef<HTMLDivElement>(null);
  useEffect(() => { visited.current.clear(); }, [sourcesKey]);
  useEffect(() => { mounted.current = true; return () => { mounted.current = false; }; }, []);
  const inactive = value === null || era;
  useEffect(() => {
    if (!inactive) return;
    requestId.current++; scrubRef.current = null;
    const timer = window.setTimeout(() => { setPlaying(false); setPending(false); setScrubDay(null); }, 0);
    return () => window.clearTimeout(timer);
  }, [inactive, setPlaying]);
  useEffect(() => {
    const pause = () => { if (document.hidden) setPlaying(false); };
    document.addEventListener("visibilitychange", pause);
    return () => document.removeEventListener("visibilitychange", pause);
  }, [setPlaying]);

  const seek = useCallback(async (next: CalendarSweepView, automatic = false) => {
    if (!automatic) setPlaying(false);
    const id = ++requestId.current;
    scrubRef.current = null; setScrubDay(null); setPending(true);
    try {
      const result = await onSeek(next);
      if (!mounted.current || id !== requestId.current) return;
      visited.current.set(calendarFrameDay(next), result);
      if (visited.current.size > 512) visited.current.delete(visited.current.keys().next().value!);
      setCheckedFrames({ sources: sourcesKey, frames: new Map(visited.current) });
      setOutcome(result);
      if (result.state === "error" || result.state === "reference") setPlaying(false);
    } catch {
      if (!mounted.current || id !== requestId.current) return;
      setOutcome({ state: "error", message: "The date could not be loaded. Playback paused; check source coverage." }); setPlaying(false);
    } finally { if (mounted.current && id === requestId.current) setPending(false); }
  }, [onSeek, setPlaying, sourcesKey, setScrubDay, setPending, setCheckedFrames, setOutcome]);
  const seekDay = useCallback((day: string, automatic = false) => {
    if (validCalendarDay(day, today)) void seek(calendarDayInRange(state, day), automatic);
  }, [seek, state, today]);
  const flushScrub = useCallback(() => { const day = scrubRef.current; if (day) seekDay(day); }, [seekDay]);
  useEffect(() => {
    if (!scrubDay) return;
    const timer = window.setTimeout(flushScrub, 160);
    return () => window.clearTimeout(timer);
  }, [flushScrub, scrubDay]);
  const index = calendarFrameIndex(frames, scrubDay ?? date);
  const sourceLoading = value !== null && sources.some(source => source.state === "loading");
  const busy = pending || sourceLoading;
  useEffect(() => {
    if (!playing || busy || era || reducedMotion || document.hidden) return;
    let nextIndex = calendarFrameIndex(frames, state.day) + 1;
    if (skipGaps) while (nextIndex < frames.length && visited.current.get(frames[nextIndex])?.state === "empty") nextIndex++;
    const next = frames[nextIndex];
    if (!next) {
      const timer = window.setTimeout(() => setPlaying(false), 0);
      return () => window.clearTimeout(timer);
    }
    const timer = window.setTimeout(() => seekDay(next, true), 1400 / speed);
    return () => window.clearTimeout(timer);
  }, [playing, busy, era, reducedMotion, state.day, state.showing, frames, skipGaps, speed, seekDay, setPlaying]);
  const shown = expanded || open;
  useEffect(() => {
    if (!shown) return;
    const dismiss = (event: PointerEvent) => { if (event.target instanceof Node && !rootRef.current?.contains(event.target)) { onOpenChange(false); setExpanded(false); } };
    document.addEventListener("pointerdown", dismiss);
    return () => document.removeEventListener("pointerdown", dismiss);
  }, [shown, onOpenChange]);
  const reveal = () => { setExpanded(true); onOpenChange(true); };
  const collapse = (returnFocus = false) => {
    onOpenChange(false); setExpanded(false);
    if (returnFocus) window.requestAnimationFrame(() => emblemRef.current?.focus());
  };
  const close = () => collapse(true);
  const togglePlay = () => {
    if (playing) { setPlaying(false); return; }
    if (busy || reducedMotion || era || frames.length < 2) return;
    if (state.showing === "A" || date >= state.end) void seek({ ...state, day: frames[0], showing: "B" }, true);
    else if (!value) void seek(state, true);
    setPlaying(true);
  };
  const shownDay = scrubDay ?? date;
  const [shownYear, shownMonth, shownDate] = shownDay.split("-").map(Number);
  const lastDay = Number(calendarDateParts(shownYear, shownMonth, 31).slice(8));
  const changePart = (part: "year" | "month" | "day", input: number) => seekDay(replaceCalendarPart(shownDay, part, input, today));
  const setRange = (part: "start" | "end", day: string) => {
    const next = { ...state, [part]: day };
    if (!validCalendarDay(day, today) || next.start > next.end) { setRangeError("Choose an ordered UTC range from 1800 through " + today + "."); return; }
    setRangeError("");
    void seek({ ...next, day: next.day < next.start ? next.start : next.day > next.end ? next.end : next.day, showing: "B" });
  };
  const step = (direction: -1 | 1) => {
    if (era) { const i = years.indexOf(year); const next = years[i + direction]; if (next !== undefined) onEra(next); return; }
    const i = calendarFrameIndex(frames, date);
    const next = direction === -1 && frames[i] < date ? frames[i] : frames[i + direction];
    if (next) seekDay(next);
  };
  const badge = scrubDay ? "Preview" : busy ? "Loading" : sources.some(source => source.state === "error") ? "Check sources" : value ? outcome.state === "empty" ? "No data" : outcome.state === "partial" ? "Partial" : outcome.state === "error" ? "Unavailable" : "" : "";
  return <div className="compact-time" data-expanded={shown} ref={rootRef} onKeyDown={event => { if (event.key === "Escape" && shown) { event.preventDefault(); event.stopPropagation(); close(); } }}>
    <button className="compact-time-emblem compact-time-clock-toggle" ref={emblemRef} type="button" aria-label={(shown ? "Close" : "Open") + " time sweep"} aria-expanded={shown} aria-controls="compact-time-transport" onClick={() => shown ? close() : reveal()} onKeyDown={event => { if (event.key === "ArrowUp") { event.preventDefault(); reveal(); } }} title={(shown ? "Close" : "Open") + " time sweep"}>
      {icon("clock")}
      {value && <progress aria-label="Requested position in configured time range" value={index + 1} max={Math.max(1, frames.length)} />}
      {busy && <span className="compact-time-emblem-status">Loading</span>}
    </button>
    <div id="compact-time-transport" className="compact-time-row" role="group" aria-label="Time sweep" inert={!shown}>
      <div className="compact-time-date">
        <label><span>Year</span><select aria-label="Sweep year or earlier era" value={era ? year : shownYear} onChange={event => { const next = Number(event.target.value); if (next < 1800) { setPlaying(false); onEra(next); } else changePart("year", next); }}>{years.map(y => <option key={y} value={y}>{y < 0 ? y <= -1e9 ? Math.abs(y / 1e9) + " Ga BP" : y <= -1e6 ? Math.abs(y / 1e6) + " Ma BP" : Math.abs(y).toLocaleString() + " BCE/BP" : y}</option>)}</select></label>
        <label><span>Month</span><select aria-label="Sweep month" disabled={era} value={shownMonth} onChange={event => changePart("month", Number(event.target.value))}>{months.map((name, i) => <option key={name} value={i + 1} disabled={shownYear === Number(today.slice(0, 4)) && i + 1 > Number(today.slice(5, 7))}>{name}</option>)}</select></label>
        <label><span>Day</span><select aria-label="Sweep day" disabled={era} value={shownDate} onChange={event => changePart("day", Number(event.target.value))}>{Array.from({ length: lastDay }, (_, i) => <option key={i} value={i + 1} disabled={shownDay.slice(0, 7) === today.slice(0, 7) && i + 1 > Number(today.slice(8))}>{i + 1}</option>)}</select></label>
      </div>
      <button className="compact-time-date-mobile" type="button" aria-label="Choose map date" onClick={() => { setTab("settings"); onOpenChange(true); }}>{era ? String(year) : shortDate(shownDay)}</button>
      <div className="compact-time-transport">
        <button className="compact-time-step" type="button" onClick={() => step(-1)} disabled={era ? years.indexOf(year) <= 0 : date <= state.start} aria-label="Previous sweep frame">{icon("caret-left")}</button>
        <button className="compact-time-play" type="button" aria-label={playing ? "Pause time sweep" : "Play time sweep"} aria-pressed={playing} disabled={era || reducedMotion || frames.length < 2 || busy && !playing} onClick={togglePlay} title={reducedMotion ? "Reduced motion: use frame steps" : busy ? "Waiting for selected sources" : "Play dated snapshots"}>{icon(playing ? "pause" : "play")}</button>
        <button className="compact-time-step" type="button" onClick={() => step(1)} disabled={era ? years.indexOf(year) >= years.length - 1 : date >= state.end} aria-label="Next sweep frame">{icon("caret-right")}</button>
      </div>
      <label className="compact-time-step-size"><span className="sr-only">Playback step</span><select aria-label="Playback step" value={state.step} disabled={era} onChange={event => { setPlaying(false); void seek({ ...state, step: event.target.value as CalendarStep, showing: "B" }); }}><option value="years">By year</option><option value="months">By month</option><option value="days">By day</option></select></label>
      <div className="compact-time-scrubber">
        <input type="range" aria-label="Scrub time sweep" aria-valuetext={(scrubDay ? "Preview " : "Selected ") + shortDate(shownDay) + " UTC"} min={0} max={Math.max(0, frames.length - 1)} value={index} disabled={era || frames.length < 2} onChange={event => { setPlaying(false); const day = frames[Number(event.target.value)]; scrubRef.current = day; setScrubDay(day); }} onPointerUp={flushScrub} onKeyUp={flushScrub} onBlur={flushScrub} />
        <div className="compact-time-axis" aria-hidden="true"><span>{state.start}</span><strong>{era ? "Earlier era" : shortDate(shownDay) + " UTC"}</strong><span>{state.end}</span></div>
        <div className="compact-time-coverage" aria-label="Checked dates only; unmarked dates are unchecked">{[...(checkedFrames.sources === sourcesKey ? checkedFrames.frames : new Map<string, CalendarFrameOutcome>())].map(([day, result]) => { const position = calendarFrameIndex(frames, day) / Math.max(1, frames.length - 1) * 100; return day >= state.start && day <= state.end ? <i key={day} data-state={result.state} style={{ left: position + "%" }} title={day + ": " + result.message} /> : null; })}</div>
      </div>
      {badge && <output className="compact-time-badge" data-busy={busy} title={outcome.message}>{badge}</output>}
      <button className="compact-time-compare" type="button" aria-label="Pin or compare dates" aria-pressed={Boolean(state.before)} disabled={era} onClick={() => { setPlaying(false); setTab("compare"); if (!state.before) void seek({ ...state, before: date, showing: "B" }); onOpenChange(true); }}>{icon("columns")}<span>{state.before ? "A / B" : "Compare"}</span></button>
      <button className="compact-time-more" ref={settingsRef} type="button" aria-label="Time sweep settings" aria-expanded={open} aria-controls="compact-time-settings" onClick={() => { setTab("settings"); onOpenChange(!open); }}>{icon("dots-three")}</button>
    </div>
    <p className="sr-only" role="status" aria-live="polite">{busy ? "Loading " + shortDate(date) + " UTC. Prior dated features are withheld." : value ? shortDate(date) + " UTC. " + outcome.message : "Atlas year " + year + ". Calendar sweep not applied."}</p>
    {open && <div className="compact-time-popover" id="compact-time-settings" ref={popupRef} role="dialog" aria-label={tab === "compare" ? "Compare dates" : "Time sweep settings"}>
      <header><div><span>TIME SWEEP · UTC</span><h2>{tab === "compare" ? "Before & after" : "Your time window"}</h2></div><button type="button" aria-label="Close time settings" onClick={close}>{icon("x")}</button></header>
      <div className="compact-time-tabs" role="group" aria-label="Time settings views"><button type="button" aria-pressed={tab === "settings"} onClick={() => setTab("settings")}>Range & playback</button><button type="button" aria-pressed={tab === "compare"} onClick={() => setTab("compare")}>Compare dates</button></div>
      {tab === "settings" ? <>
        <label className="compact-time-exact-date">Map date · UTC<input type="date" aria-label="Exact map date" min="1800-01-01" max={today} value={date} onChange={event => seekDay(event.target.value)} /></label>
        <div className="compact-time-range"><label>From<input type="date" aria-label="Sweep range start" min="1800-01-01" max={state.end} value={state.start} onChange={event => setRange("start", event.target.value)} /></label><label>Through<input type="date" aria-label="Sweep range end" min={state.start} max={today} value={state.end} onChange={event => setRange("end", event.target.value)} /></label></div>
        {rangeError && <p role="alert">{rangeError}</p>}
        <div className="compact-time-options"><label>Speed<select aria-label="Sweep speed" value={speed} onChange={event => setSpeed(Number(event.target.value))}><option value={0.5}>0.5×</option><option value={1}>1×</option><option value={2}>2×</option></select></label><label><input type="checkbox" checked={skipGaps} onChange={event => setSkipGaps(event.target.checked)} /> Skip checked empty dates</label></div>
        <p>{reducedMotion ? "Reduced motion is active. Step between dates manually." : "Playback waits for sources, stops at the range boundary, and pauses when this tab is hidden."}</p>
        <button type="button" className="compact-time-present" onClick={() => { setPlaying(false); requestId.current++; visited.current.clear(); onPresent(); }}>{icon("arrow-counter-clockwise")} Return to present sources</button>
        <details className="compact-time-source-details"><summary>Layer coverage & source clocks</summary><p>{value ? "Selected date: " + shortDate(date) + " UTC." : "The annual atlas is active. Select a date to check supported daily sources."} Years and months select dated snapshots, not averages. Unmarked dates are unchecked; empty responses do not prove absence. The era animation is decorative; the flying car is an imagined future, not a data period.</p><ul>{sources.map(source => <li key={source.id}><strong>{source.title}<em data-state={source.state}>{source.state}</em></strong><small>{source.detail}</small></li>)}</ul><p>Basemap and terrain are orientation context. Source, retrieval, release, and review clocks remain separate.</p></details>
      </> : <>
        <p>Pin A, choose another date for B, then switch the same map between them. Each date checks the selected sources again.</p>
        <div className="compact-time-comparison"><button type="button" disabled={!state.before || busy} aria-pressed={state.showing === "A"} onClick={() => void seek({ ...state, showing: "A" })}><span>A · Before</span><strong>{state.before ? shortDate(state.before) : "Not pinned"}</strong></button><button type="button" disabled={busy} aria-pressed={state.showing === "B"} onClick={() => void seek({ ...state, showing: "B" })}><span>B · After</span><strong>{shortDate(state.day)}</strong></button></div>
        <div className="compact-time-pin-actions"><button type="button" onClick={() => void seek({ ...state, before: date, showing: "B" })}>Pin current date as A</button><button type="button" disabled={!state.before} onClick={() => void seek({ ...state, before: null, showing: "B" })}>Clear pin</button></div>
        <p>Different record availability is not measured real-world change. Missing dates stay unavailable.</p>
        {imageryComparison && <details><summary>Swipe approved imagery years</summary>{imageryComparison}</details>}
      </>}
      <p className="compact-time-outcome" data-state={outcome.state}>{busy ? "Checking selected sources for " + date + "…" : outcome.message}</p>
      {children && <details className="compact-time-legacy"><summary>Advanced atlas years & interpretation</summary>{children}</details>}
    </div>}
  </div>;
}
