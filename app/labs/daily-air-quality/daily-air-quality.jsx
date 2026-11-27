"use client";

import { useEffect, useMemo, useRef, useState, useSyncExternalStore } from "react";
import Link from "next/link";
import ScienceNav from "../../science/science-nav";
import { analyseAir, airCsv, airReceipt, CATEGORIES, YEARS } from "./air-model.mjs";
import { loadAirSnapshot } from "./snapshot-loader.mjs";
import styles from "./daily-air-quality.module.css";

const MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
const WEEKDAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
const LOCATION_EVENT = "kfm-air-selection";
const CATEGORY_COLORS = { Good: "#00e400", Moderate: "#ffff00", "Unhealthy for Sensitive Groups": "#ff7e00", Unhealthy: "#ff0000", "Very Unhealthy": "#8f3f97", Hazardous: "#7e0023" };
const CATEGORY_RANGES = ["0–50", "51–100", "101–150", "151–200", "201–300", "301+"];
const PLOT = { width: 980, height: 290, left: 54, right: 22, top: 28, bottom: 48 };
const number = (value, digits = 0) => Number.isFinite(value) ? value.toLocaleString("en-US", { maximumFractionDigits: digits }) : "—";
const color = (category) => CATEGORY_COLORS[category] ?? "#729097";

function integer(raw, minimum, maximum, fallback) {
  return raw !== null && /^\d+$/.test(raw) && Number(raw) >= minimum && Number(raw) <= maximum ? Number(raw) : fallback;
}

function calendarDate(date) {
  if (!/^\d{4}-\d{2}-\d{2}$/.test(date)) return false;
  const parsed = new Date(`${date}T12:00:00Z`);
  return Number.isFinite(parsed.getTime()) && parsed.toISOString().slice(0, 10) === date;
}

export function airSelection(manifest, search = "") {
  const query = new URLSearchParams(search);
  const preferred = manifest.counties.find((county) => county.id === "20173") ?? manifest.counties[0];
  const year = integer(query.get("year"), YEARS[0], YEARS.at(-1), 2023);
  const month = integer(query.get("month"), 0, 12, 0);
  const requestedDate = query.get("date") ?? "";
  const date = calendarDate(requestedDate) && requestedDate.startsWith(String(year)) && (!month || Number(requestedDate.slice(5, 7)) === month)
    ? requestedDate : `${year}-${String(month || 9).padStart(2, "0")}-06`;
  return {
    county: manifest.counties.some((county) => county.id === query.get("county")) ? query.get("county") : preferred.id,
    year,
    month,
    threshold: integer(query.get("threshold"), 0, 500, 101),
    date,
  };
}

export function airLink(href, selection) {
  const url = new URL(href);
  url.search = "";
  url.hash = "";
  for (const key of ["county", "year", "month", "threshold", "date"]) url.searchParams.set(key, String(selection[key]));
  return url.toString();
}

function subscribeLocation(callback) {
  window.addEventListener("popstate", callback);
  window.addEventListener(LOCATION_EVENT, callback);
  return () => {
    window.removeEventListener("popstate", callback);
    window.removeEventListener(LOCATION_EVENT, callback);
  };
}
const locationSearch = () => window.location.search;
const serverSearch = () => "";
const dateLabel = (date, short = false) => new Intl.DateTimeFormat("en-US", { timeZone: "UTC", month: short ? "short" : "long", day: "numeric", ...(short ? {} : { year: "numeric" }) }).format(new Date(`${date}T12:00:00Z`));
const captureLabel = (raw) => raw ? raw.replace("T", " ").replace(/Z$/, " UTC") : "Not supplied";
const boundaryLabel = (value) => value === "window" ? "selected window edge" : value === "missing" ? "adjacent date has no report" : "observed below threshold";

function downloadText(value, type, filename) {
  const objectUrl = URL.createObjectURL(new Blob([value], { type }));
  const link = document.createElement("a");
  link.href = objectUrl;
  link.download = filename;
  document.body.appendChild(link);
  link.click();
  link.remove();
  setTimeout(() => URL.revokeObjectURL(objectUrl), 1000);
}

export function AirMetrics({ analysis }) {
  return <dl className={styles.metrics}>
    <div><dt>Days with AQI ≥ {analysis.settings.threshold}</dt><dd><strong>{number(analysis.thresholdDays)}</strong><span>days</span></dd><small>{analysis.reported ? `${number(analysis.thresholdPct, 1)}% of ${number(analysis.reported)} reported days` : "No reported days in this window"}</small></div>
    <div><dt>Highest reported AQI</dt><dd><strong>{number(analysis.peak?.aqi)}</strong><span>AQI</span></dd><small>{analysis.peak ? `${dateLabel(analysis.peak.date, true)} · ${analysis.peak.parameter}` : "No report · no peak inferred"}</small></div>
    <div><dt>Median reported AQI</dt><dd><strong>{number(analysis.medianAqi, 1)}</strong><span>AQI</span></dd><small>Middle of the reported daily values</small></div>
    <div><dt>Reported / calendar dates</dt><dd className={styles.supportValue}><strong>{number(analysis.reported)}<span> / {number(analysis.expected)}</span></strong></dd><small>{number(analysis.missing)} dates without a report · no gap filling</small></div>
  </dl>;
}

export function airSeriesPath(days, x, y) {
  let drawing = false;
  return days.map((day, index) => {
    if (day.missing) { drawing = false; return ""; }
    const command = drawing ? "L" : "M";
    drawing = true;
    return `${command}${x(index).toFixed(2)},${y(day.aqi).toFixed(2)}`;
  }).join(" ");
}

export function AirTimeline({ analysis, selectedIndex }) {
  const { days } = analysis;
  const bottom = PLOT.height - PLOT.bottom;
  const topValue = Math.max(150, Math.ceil(Math.max(analysis.peak?.aqi ?? 0, analysis.settings.threshold) / 50) * 50);
  const x = (index) => PLOT.left + (days.length < 2 ? .5 : index / (days.length - 1)) * (PLOT.width - PLOT.left - PLOT.right);
  const y = (value) => bottom - value / topValue * (bottom - PLOT.top);
  const ticks = Array.from({ length: 6 }, (_, index) => topValue / 5 * index);
  const day = days[selectedIndex];
  const xTicks = days.reduce((found, item, index) => {
    if (analysis.settings.month ? [0, 7, 14, 21, days.length - 1].includes(index) : item.date.endsWith("-01") && ["01", "03", "05", "07", "09", "11"].includes(item.date.slice(5, 7))) found.push(index);
    return found;
  }, []);
  return <figure className={styles.timeline}>
    <figcaption><h3>The daily record, with its gaps.</h3><p>One value is the county’s highest reported monitor AQI for that date.</p></figcaption>
    <div className={styles.timelineCanvas}><svg viewBox={`0 0 ${PLOT.width} ${PLOT.height}`} preserveAspectRatio="none" role="img" aria-labelledby="air-timeline-title air-timeline-description">
      <title id="air-timeline-title">{`${analysis.county.name} daily AQI, ${analysis.period.from} through ${analysis.period.to}`}</title>
      <desc id="air-timeline-description">{analysis.reported} reported days and {analysis.missing} dates without a report. Missing dates break the line. The dashed reference marks the inclusive AQI threshold of {analysis.settings.threshold}. Use the date inspector or calendar buttons for exact daily source values.</desc>
      {ticks.map((tick) => <g key={tick}><line className={styles.gridLine} x1={PLOT.left} x2={PLOT.width - PLOT.right} y1={y(tick)} y2={y(tick)} /><text className={styles.axisText} x={PLOT.left - 10} y={y(tick) + 4} textAnchor="end">{number(tick)}</text></g>)}
      <text className={styles.axisText} x={PLOT.left} y={15}>AQI</text>
      {days.map((item, index) => item.missing ? <line key={item.date} className={styles.missingMark} x1={x(index)} x2={x(index)} y1={bottom + 7} y2={bottom + 13} /> : null)}
      <line className={styles.thresholdLine} x1={PLOT.left} x2={PLOT.width - PLOT.right} y1={y(analysis.settings.threshold)} y2={y(analysis.settings.threshold)} />
      <path className={styles.aqiLine} d={airSeriesPath(days, x, y)} />
      {days.map((item, index) => !item.missing && (index === 0 || days[index - 1].missing) && (index === days.length - 1 || days[index + 1].missing) ? <circle key={item.date} className={styles.isolatedPoint} cx={x(index)} cy={y(item.aqi)} r={2.5} /> : null)}
      {day && <line className={styles.inspectionLine} x1={x(selectedIndex)} x2={x(selectedIndex)} y1={PLOT.top} y2={bottom} />}
      {day && !day.missing && <circle className={styles.inspectedPoint} cx={x(selectedIndex)} cy={y(day.aqi)} r={5} style={{ fill: color(day.category) }} />}
      {xTicks.map((index) => <text key={index} className={styles.axisText} x={x(index)} y={bottom + 35} textAnchor={index === 0 ? "start" : index === days.length - 1 ? "end" : "middle"}>{dateLabel(days[index].date, true)}</text>)}
    </svg><div className={styles.mobileYAxis} aria-hidden="true"><span className={styles.mobileAxisUnit}>AQI</span>{ticks.map((tick) => <span key={tick} style={{ top: `${y(tick) / PLOT.height * 100}%`, left: `${PLOT.left / PLOT.width * 100}%` }}>{number(tick)}</span>)}</div><div className={styles.mobileXAxis} aria-hidden="true">{xTicks.map((index) => <span key={index} style={{ left: `${x(index) / PLOT.width * 100}%`, top: `${(bottom + 35) / PLOT.height * 100}%` }} data-align={index === 0 ? "start" : index === days.length - 1 ? "end" : "middle"}>{dateLabel(days[index].date, true)}</span>)}</div></div>
    <div className={styles.plotKey}><span><i className={styles.lineKey} />Reported daily AQI</span><span><i className={styles.thresholdKey} />Threshold ≥ {analysis.settings.threshold}</span><span><i className={styles.gapKey} />No report leaves a gap</span></div>
  </figure>;
}

export function AirDayInspector({ analysis, selectedIndex, onSelectDate }) {
  const { days } = analysis;
  const day = days[selectedIndex];
  if (!day) return null;
  function selectDate(event) {
    const date = event.currentTarget.value;
    if (calendarDate(date) && days.some((item) => item.date === date)) onSelectDate(date);
  }
  return <section className={styles.inspector} id="air-day" aria-labelledby="air-day-heading">
    <div className={styles.inspectorHeader}><div><span className={styles.eyebrow}>One date / the source record</span><h3 id="air-day-heading">{dateLabel(day.date)}</h3></div><div className={styles.dateControls}><button type="button" aria-label="Previous calendar day" disabled={selectedIndex === 0} onClick={() => onSelectDate(days[selectedIndex - 1].date)}>←</button><label>Inspect a date<input type="date" value={day.date} min={days[0].date} max={days.at(-1).date} onInput={selectDate} onChange={selectDate} /></label><button type="button" aria-label="Next calendar day" disabled={selectedIndex === days.length - 1} onClick={() => onSelectDate(days[selectedIndex + 1].date)}>→</button></div></div>
    {day.missing ? <div className={styles.noReport} role="status"><strong>No report for this county and date.</strong><p>A missing county-day is not AQI zero or evidence of clean air. No pollutant, monitor count or source row is inferred.</p></div> : <><div className={styles.reading}><div><strong>{number(day.aqi)}</strong><span>AQI · raw token <code>{day.rawAqi}</code></span></div><span className={styles.categoryLabel} style={{ "--aqi-color": color(day.category) }}><i />{day.category}</span><p>{day.meets ? `At or above your threshold of ${analysis.settings.threshold}.` : `Below your threshold of ${analysis.settings.threshold}.`}</p></div><dl className={styles.recordFacts}><div><dt>Defining pollutant</dt><dd>{day.parameter}</dd></div><div><dt>Defining site · source text</dt><dd><code>{day.site}</code></dd></div><div><dt>Reporting sites</dt><dd>{number(day.sites)} <small>· raw token <code>{day.rawSites}</code></small></dd></div><div><dt>Original CSV row</dt><dd>{number(day.sourceRow)} <small>· header is row 1</small></dd></div><div><dt>Original annual file</dt><dd><a href={day.source.url} target="_blank" rel="noreferrer">{day.source.year} EPA county AQI ZIP ↗</a><small>Captured {captureLabel(day.source.capturedAt)}</small></dd></div></dl></>}
  </section>;
}

export function AirCalendar({ analysis, selectedIndex, onSelectDate }) {
  const selected = analysis.days[selectedIndex];
  const months = analysis.months.map((month) => ({ ...month, days: analysis.days.filter((day) => Number(day.date.slice(5, 7)) === month.month) })).filter((month) => month.days.length);
  return <section className={styles.calendarSection} aria-labelledby="air-calendar-heading"><div className={styles.sectionHeader}><div><h3 id="air-calendar-heading">A calendar of the reported air.</h3><p>Choose a date to inspect it. Numbers are calendar days; colors are EPA’s published categories.</p></div><a href="#air-day">Inspect chosen date ↑</a></div>
    <ul className={styles.categoryLegend} aria-label="EPA AQI category legend">{CATEGORIES.map((category, index) => <li key={category}><i style={{ background: color(category) }} /><span>{category}<small>AQI {CATEGORY_RANGES[index]}</small></span></li>)}<li><i className={styles.missingSwatch} /><span>No report<small>Kept on the calendar</small></span></li></ul>
    <p className={styles.calendarNote}>A black corner marks AQI ≥ {analysis.settings.threshold}. The outlined date is selected. A dash means no report.</p>
    <div className={styles.calendars}>{months.map((month) => <section className={styles.month} key={month.month} aria-labelledby={`air-month-${month.month}`}><div className={styles.monthHeading}><h4 id={`air-month-${month.month}`}>{MONTHS[month.month - 1]}</h4><span>{month.reported}/{month.expected} reported</span></div><div className={styles.weekdays} aria-hidden="true">{WEEKDAYS.map((weekday) => <abbr key={weekday} title={weekday}>{weekday.slice(0, 1)}</abbr>)}</div><div className={styles.monthDays}>{Array.from({ length: new Date(`${month.days[0].date}T12:00:00Z`).getUTCDay() }, (_, index) => <span className={styles.blankDay} key={`blank-${index}`} />)}{month.days.map((day) => <button key={day.date} type="button" className={`${styles.calendarDay}${day.missing ? ` ${styles.missingDay}` : ""}${day.meets ? ` ${styles.meets}` : ""}${["Very Unhealthy", "Hazardous"].includes(day.category) ? ` ${styles.lightText}` : ""}`} style={{ "--aqi-color": color(day.category) }} aria-label={`${dateLabel(day.date)}: ${day.missing ? "no report" : `AQI ${day.aqi}, ${day.category}, ${day.parameter}${day.meets ? `, at or above threshold ${analysis.settings.threshold}` : ""}`}`} aria-pressed={day.date === selected?.date} onClick={() => onSelectDate(day.date)}><span>{Number(day.date.slice(8, 10))}</span>{day.missing && <small>—</small>}</button>)}</div></section>)}</div>
    <p className={styles.selectedCalendarDate} role="status">Selected: {selected ? `${dateLabel(selected.date)} · ${selected.missing ? "no report" : `AQI ${selected.aqi} · ${selected.category}`}` : "No date"}. <a href="#air-day">Read the source record ↑</a></p>
  </section>;
}

export function AirSummaries({ analysis }) {
  const run = analysis.longestRun;
  return <section className={styles.summaries} aria-labelledby="air-summaries-heading"><div className={styles.sectionHeader}><div><span className={styles.eyebrow}>The same window / another view</span><h3 id="air-summaries-heading">Count days. Keep the denominator.</h3></div></div><div className={styles.summaryColumns}><div><div className={styles.runSummary}><span>Longest observed run · AQI ≥ {analysis.settings.threshold}</span><strong>{number(run.count)} <small>consecutive reported days</small></strong><p>{run.count ? `${dateLabel(run.from, true)} – ${dateLabel(run.to, true)}. ` : "No reported dates meet this threshold. "}Missing dates break a run. Window boundaries may leave its full duration unknown.</p>{run.count > 0 && <small>Left boundary: {boundaryLabel(run.leftBoundary)} · right boundary: {boundaryLabel(run.rightBoundary)}</small>}</div><div className={styles.tableScroll} role="region" aria-label="Monthly AQI summaries, horizontally scrollable" tabIndex={0}><table><caption>Monthly support and reported AQI · {analysis.settings.year}</caption><thead><tr><th scope="col">Month</th><th scope="col">Reported / dates</th><th scope="col">AQI ≥ {analysis.settings.threshold}</th><th scope="col">Median</th><th scope="col">Peak</th></tr></thead><tbody>{analysis.months.map((month) => <tr key={month.month}><th scope="row">{month.label}</th><td>{month.reported} / {month.expected}</td><td>{month.thresholdDays}<small>{month.reported ? `${number(month.thresholdPct, 1)}% of reported` : "No reports"}</small></td><td>{number(month.medianAqi, 1)}</td><td>{number(month.maxAqi)}</td></tr>)}</tbody></table></div></div><div className={styles.pollutants}><h4>What defined the county’s AQI?</h4><p>Counts of reported days when each pollutant defined the county AQI. These are not concentration exceedances or an inferred cause of smoke.</p><dl>{analysis.pollutantCounts.map((item) => <div key={item.parameter}><dt>{item.parameter}</dt><dd><strong>{number(item.count)}</strong><span>days</span><i style={{ width: `${analysis.reported ? item.count / analysis.reported * 100 : 0}%` }} /></dd></div>)}</dl>{!analysis.reported && <p>No reported days in this selection.</p>}<p className={styles.siteNote}>Reporting-site count in this window: {analysis.siteCountRange.min === null ? "no reports" : `${number(analysis.siteCountRange.min)}–${number(analysis.siteCountRange.max)}`}. Monitoring coverage varies by place and date.</p></div></div></section>;
}

export default function DailyAirQuality({ manifest }) {
  const search = useSyncExternalStore(subscribeLocation, locationSearch, serverSearch);
  const selection = useMemo(() => airSelection(manifest, search), [manifest, search]);
  const descriptor = manifest.snapshot;
  const county = manifest.counties.find((item) => item.id === selection.county);
  const [result, setResult] = useState(null);
  const [retry, setRetry] = useState(0);
  const requestId = useRef(0);
  const shareId = useRef(0);
  const [share, setShare] = useState(null);
  const [exportError, setExportError] = useState("");
  const selectionKey = `${selection.county}:${selection.year}:${selection.month}:${selection.threshold}:${selection.date}`;

  useEffect(() => {
    const controller = new AbortController();
    const id = ++requestId.current;
    loadAirSnapshot(manifest, { signal: controller.signal }).then((snapshot) => {
      if (!controller.signal.aborted && requestId.current === id) setResult({ identity: descriptor.sha256, snapshot, error: "" });
    }).catch((error) => {
      if (!controller.signal.aborted && requestId.current === id) setResult({ identity: descriptor.sha256, snapshot: null, error: error instanceof Error ? error.message : "The county AQI snapshot could not be read." });
    });
    return () => controller.abort();
  }, [manifest, descriptor.sha256, retry]);

  const currentResult = result?.identity === descriptor.sha256 ? result : null;
  const snapshot = currentResult?.snapshot ?? null;
  const analysis = useMemo(() => snapshot ? analyseAir(snapshot, { countyId: selection.county, year: selection.year, month: selection.month, threshold: selection.threshold }) : null, [snapshot, selection.county, selection.year, selection.month, selection.threshold]);
  const days = analysis?.days ?? [];
  const selectedIndex = Math.max(0, days.findIndex((day) => day.date === selection.date));
  const loading = !currentResult;
  const periodLabel = `${selection.month ? `${MONTHS[selection.month - 1]} ` : ""}${selection.year}`;

  function updateSelection(patch) {
    const next = airSelection(manifest, new URL(airLink(window.location.href, { ...selection, ...patch })).search);
    const href = airLink(window.location.href, next);
    if (href === window.location.href) return;
    shareId.current += 1;
    setShare(null);
    setExportError("");
    window.history.pushState(window.history.state, "", href);
    window.dispatchEvent(new Event(LOCATION_EVENT));
  }

  async function copyLink() {
    const link = airLink(window.location.href, selection);
    const id = ++shareId.current;
    try {
      if (!navigator.clipboard?.writeText) throw new Error("Clipboard unavailable");
      await navigator.clipboard.writeText(link);
      if (id === shareId.current) setShare({ key: selectionKey, status: "Analysis link copied, including the inspected date.", fallback: "" });
    } catch {
      if (id === shareId.current) setShare({ key: selectionKey, status: "Select and copy the analysis link below.", fallback: link });
    }
  }

  function exportAnalysis(kind) {
    if (!analysis || !snapshot || !days.length) return;
    try {
      const filename = `kfm-air-${selection.county}-${selection.year}${selection.month ? `-${String(selection.month).padStart(2, "0")}` : ""}-aqi-${selection.threshold}`;
      if (kind === "csv") downloadText(airCsv(analysis), "text/csv;charset=utf-8", `${filename}.csv`);
      else downloadText(`${JSON.stringify(airReceipt(analysis, descriptor, { inspectedDate: days[selectedIndex]?.date ?? null }), null, 2)}\n`, "application/json", `${filename}-receipt.json`);
      setExportError("");
    } catch {
      setExportError("This browser could not create the download. Try again or open the original EPA files below.");
    }
  }

  return <main className={styles.page}><div className={styles.frame}>
    <ScienceNav active="air" selection={selection} sourceHref="#air-evidence" sourceLabel="Source & methods ↓" extraLinks={[{ href: "/labs", label: "Research atlas ↗" }, { href: "/research", label: "Source discovery ↗" }]} />
    <header className={styles.hero}><div><span className={styles.eyebrow}>Kansas field notebook / Daily Air Quality Lab</span><h1>When did<br /><em>the air change?</em></h1><p>Read daily EPA county AQI, then inspect the pollutant and monitor record that defined it. A historical record of reported air, one date at a time.</p></div><div className={styles.scope}><span className={styles.badge}><i />EPA AirData · 2020–2025</span><strong>{manifest.counties.length}<span>reporting counties / 105 Kansas counties</span></strong><span>{number(descriptor.records)} reported county-days<br />Coverage varies by county and date</span></div></header>
    <p className={styles.scopeNote}>Each county-day is the highest reported monitor AQI in that county. It does not describe every location or individual exposure. <a href="https://www.airnow.gov/" target="_blank" rel="noreferrer">Current air quality: AirNow ↗</a></p>

    <section className={styles.setup} aria-labelledby="air-setup-heading"><div className={styles.sectionHeader}><div><span className={styles.eyebrow}>01 / Choose the record</span><h2 id="air-setup-heading">A county, a window, a question.</h2></div><button type="button" className={styles.shareButton} onClick={copyLink}>Copy analysis link ↗</button></div><div className={styles.selects}>
      <label>Reporting county<select value={selection.county} onChange={(event) => updateSelection({ county: event.target.value })}>{manifest.counties.map((item) => <option key={item.id} value={item.id}>{item.name}</option>)}</select></label>
      <label>Year<select value={selection.year} onChange={(event) => updateSelection({ year: Number(event.target.value) })}>{[...YEARS].reverse().map((year) => <option key={year} value={year}>{year}</option>)}</select></label>
      <label>Time window<select value={selection.month} onChange={(event) => updateSelection({ month: Number(event.target.value) })}><option value={0}>Full year</option>{MONTHS.map((month, index) => <option key={month} value={index + 1}>{month}</option>)}</select></label>
      <label>AQI threshold · at or above<input type="number" min={0} max={500} step={1} value={selection.threshold} onChange={(event) => { const raw = event.target.value; if (/^\d+$/.test(raw) && Number(raw) <= 500) updateSelection({ threshold: Number(raw) }); }} /></label>
    </div><div className={styles.thresholdPresets}><span>Start a threshold question:</span>{[[51, "51 · Moderate or higher"], [101, "101 · Unhealthy for sensitive groups or higher"], [151, "151 · Unhealthy or higher"]].map(([threshold, label]) => <button key={threshold} type="button" aria-pressed={selection.threshold === threshold} onClick={() => updateSelection({ threshold })}>{label}</button>)}</div><p className={styles.thresholdNote}>“At or above” includes the exact threshold. Day percentages use reported days; dates without a report are excluded from that denominator.</p>{share?.key === selectionKey && <><p className={styles.shareStatus} role="status">{share.status}</p>{share.fallback && <label className={styles.shareFallback}>Analysis link<input type="text" readOnly value={share.fallback} onFocus={(event) => event.target.select()} /></label>}</>}</section>

    <section className={styles.analysis} aria-labelledby="air-analysis-heading" aria-busy={loading}><div className={styles.sectionHeader}><div><span className={styles.eyebrow}>02 / Follow the days</span><h2 id="air-analysis-heading">{county.name}<span className={styles.headingPeriod}> / {periodLabel}</span></h2></div><span className={styles.countyId}>FIPS {county.id}</span></div>
      {loading && <div className={styles.loadState} role="status"><span className={styles.statusMark}>…</span><div><h3>Reading the county AQI observations</h3><p>Loading the captured EPA record and checking its bytes, hash and structure before display.</p></div></div>}
      {currentResult?.error && <div className={styles.loadState} role="alert"><span className={styles.statusMark}>!</span><div><h3>The county AQI snapshot could not be loaded.</h3><p>{currentResult.error}</p><button type="button" onClick={() => { setResult(null); setRetry((value) => value + 1); }}>Retry county AQI snapshot</button></div></div>}
      {analysis && <><AirMetrics analysis={analysis} />{!analysis.reported && <div className={styles.emptyState} role="status"><h3>No reported AQI in this selection.</h3><p>The calendar dates remain visible below. Choose another county or time window to inspect available records; no air-quality value is inferred for the gaps.</p></div>}<AirTimeline analysis={analysis} selectedIndex={selectedIndex} /><AirDayInspector analysis={analysis} selectedIndex={selectedIndex} onSelectDate={(date) => updateSelection({ date })} /><AirCalendar analysis={analysis} selectedIndex={selectedIndex} onSelectDate={(date) => updateSelection({ date })} /><AirSummaries analysis={analysis} /></>}
    </section>

    <section className={styles.evidence} id="air-evidence" aria-labelledby="air-evidence-heading"><div className={styles.sectionHeader}><div><span className={styles.eyebrow}>03 / Keep the evidence</span><h2 id="air-evidence-heading">Take the dates. Keep the source.</h2></div><span className={styles.evidenceTag}>Historical provider context</span></div><div className={styles.downloads}><button type="button" disabled={!analysis || !days.length} onClick={() => exportAnalysis("csv")}>Download daily CSV ↓</button><button type="button" disabled={!analysis || !days.length} onClick={() => exportAnalysis("receipt")}>Download analysis receipt ↓</button><a href={manifest.documentation} target="_blank" rel="noreferrer">EPA file definitions ↗</a></div><p className={styles.downloadNote}>The CSV includes every selected calendar date, missing states and original source tokens. The JSON receipt preserves this analysis, captured source identities and the inspected date. Downloads are free.</p>{exportError && <p role="alert" className={styles.errorText}>{exportError}</p>}
      <div className={styles.evidenceGrid}><div><h3>What the record supports.</h3><dl className={styles.sourceFacts}><div><dt>Provider</dt><dd>{manifest.provider}</dd></div><div><dt>Captured period</dt><dd>{manifest.period.from} through {manifest.period.to}</dd></div><div><dt>Reporting coverage</dt><dd>{manifest.counties.length} of 105 Kansas counties · {number(descriptor.records)} reported county-days</dd></div><div><dt>Observation support</dt><dd>County’s highest reported monitor AQI for each date</dd></div><div><dt>Source values</dt><dd>EPA-published AQI and categories · no concentration conversion</dd></div></dl></div><div className={styles.limitations}><h3>Read the air, and its limits.</h3><p>Monitors sample particular locations. A county AQI is not a county-wide exposure estimate, a forecast or a measured health outcome. An unreported county or date does not establish clean air.</p><p>The defining pollutant identifies what determined the county AQI that day. It does not identify the cause of an episode or attribute it to smoke. Monitor availability can change the comparison.</p><p>Six years with varying monitoring do not establish a trend. EPA files may be revised, and historical breakpoint handling can change. This lab preserves the published values in the captured files.</p></div></div>
      <details className={styles.methods}><summary>Daily rules, monitoring coverage &amp; captured source files</summary><div className={styles.methodsBody}><p>The lab uses EPA’s daily county AQI summary. It does not recalculate AQI from concentrations. Categories, defining pollutant, defining-site text, number of sites and source CSV row are retained alongside the original AQI token. A reported AQI of zero remains zero.</p><p>Threshold counts use AQI ≥ your selected integer from 0 to 500. Percentages and median use reported county-days only. Calendar rows without an observation remain missing in the calendar and export. Missing dates break observed runs; a run touching a selected window edge or a reporting gap may be only part of a longer episode.</p><p>Monthly statistics and defining-pollutant counts describe the same selected county and time window. They count days, not pollutant concentrations. A date can have one county AQI even when multiple monitoring sites reported.</p><div className={styles.documentationLinks}><a href={manifest.documentation} target="_blank" rel="noreferrer">EPA daily AQI fields ↗</a><a href={manifest.fileIndexSource.url} target="_blank" rel="noreferrer">EPA file index ↗</a><a href={manifest.rights} target="_blank" rel="noreferrer">EPA data license ↗</a><a href="https://www.airnow.gov/aqi/aqi-basics/" target="_blank" rel="noreferrer">About EPA AQI categories ↗</a></div><h4>Coverage across the captured six years</h4><ul className={styles.countyCoverage}>{manifest.counties.map((item) => <li key={item.id}><span>{item.name}</span><strong>{number(item.reportedDays)} / {number(descriptor.calendarDates)} dates</strong></li>)}</ul><dl className={styles.hashes}><div><dt>Display snapshot · {number(descriptor.bytes)} decoded bytes · SHA-256</dt><dd><a href={descriptor.url}>Open the captured display file ↗</a><code>{descriptor.sha256}</code></dd></div><div><dt>Snapshot prepared</dt><dd><time dateTime={manifest.generatedAt}>{captureLabel(manifest.generatedAt)}</time></dd></div></dl><div className={styles.tableScroll} role="region" aria-label="Six captured annual EPA source files, horizontally scrollable" tabIndex={0}><table className={styles.sourceTable}><caption>Six original annual files. Provider URLs may now serve revised bytes.</caption><thead><tr><th scope="col">Year / original</th><th scope="col">Captured / provider created</th><th scope="col">ZIP bytes / SHA-256</th></tr></thead><tbody>{manifest.sources.map((source) => <tr key={source.year}><th scope="row"><a href={source.url} target="_blank" rel="noreferrer">{source.year} EPA county AQI ZIP ↗</a></th><td><time dateTime={source.capturedAt}>{captureLabel(source.capturedAt)}</time><small>Provider file created: {source.providerCreated}</small>{source.lastModified && <small>Last-Modified: {source.lastModified}</small>}</td><td>{number(source.bytes)} bytes<code>{source.sha256}</code></td></tr>)}</tbody></table></div><p className={styles.integrityNote}>KFM calculated these SHA-256 hashes; they are not EPA-issued signatures. The display snapshot is verified before use. Scientific review and dataset admission remain pending; dataset release is unreleased. Public access to this tool does not change that status.</p></div></details>
      <aside className={styles.related} aria-labelledby="air-related-heading"><h3 id="air-related-heading">Keep exploring the observations.</h3><Link href="/labs?story=air-and-health">Annual Air Quality · 2000–2025 summaries ↗</Link><Link href="/labs/observatory">County Observatory ↗</Link><Link href="/labs/heat-and-rain">Heat &amp; Rain Lab ↗</Link><Link href="/labs/county-drought">County Drought Lab ↗</Link><Link href="/labs/soil-profile">Soil Profile Lab ↗</Link></aside>
      <footer className={styles.footer}><span>Kansas Frontier Matrix · Daily Air Quality Lab</span><Link href="/science">Explore the science tools ↗</Link></footer>
    </section>
  </div></main>;
}
