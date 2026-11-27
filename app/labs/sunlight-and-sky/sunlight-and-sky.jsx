"use client";

import { useEffect, useMemo, useRef, useState, useSyncExternalStore } from "react";
import Link from "next/link";
import ScienceNav from "../../science/science-nav";
import { analyseSunlight, sunlightCsv, sunlightReceipt } from "./sunlight-model.mjs";
import { loadSunlightSnapshot } from "./snapshot-loader.mjs";
import styles from "./sunlight-and-sky.module.css";

const MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
const YEARS = [2025, 2024, 2023, 2022, 2021, 2020];
const LOCATION_EVENT = "kfm-sunlight-selection";
const PAGE_SIZE = 10;
const UNIT = "kWh/m²/day";
const PLOT = { width: 1000, height: 310, left: 45, right: 18, top: 22, bottom: 47 };
const number = (value, digits = 2) => Number.isFinite(value) ? value.toLocaleString("en-US", { minimumFractionDigits: digits, maximumFractionDigits: digits }) : "—";
const count = (value) => number(value, 0);
const signed = (value) => Number.isFinite(value) ? `${value > 0 ? "+" : ""}${number(value)}` : "—";
const valid = (reading) => reading?.state === "modeled" && Number.isFinite(reading.value);
const dateLabel = (date, short = false) => new Intl.DateTimeFormat("en-US", { timeZone: "UTC", month: short ? "short" : "long", day: "numeric", ...(short ? {} : { year: "numeric" }) }).format(new Date(`${date}T12:00:00Z`));
const captureLabel = (raw) => raw ? raw.replace("T", " ").replace(/Z$/, " UTC") : "Not supplied";

function integer(raw, minimum, maximum, fallback) {
  return raw !== null && /^\d+$/.test(raw) && Number(raw) >= minimum && Number(raw) <= maximum ? Number(raw) : fallback;
}

function calendarDate(value) {
  if (!/^\d{4}-\d{2}-\d{2}$/.test(value)) return false;
  const parsed = new Date(`${value}T12:00:00Z`);
  return Number.isFinite(parsed.getTime()) && parsed.toISOString().slice(0, 10) === value;
}

export function sunlightSelection(manifest, search = "") {
  const query = new URLSearchParams(search);
  const point = (key, preferred) => manifest.points.some((item) => item.id === query.get(key)) ? query.get(key) : (manifest.points.find((item) => item.id === preferred) ?? manifest.points[0]).id;
  const year = integer(query.get("year"), 2020, 2025, 2025);
  const month = integer(query.get("month"), 0, 12, 0);
  const requestedDate = query.get("date") ?? "";
  const date = calendarDate(requestedDate) && requestedDate.startsWith(String(year)) && (!month || Number(requestedDate.slice(5, 7)) === month)
    ? requestedDate : `${year}-${String(month || 7).padStart(2, "0")}-01`;
  return { primary: point("primary", "dodge-city"), comparison: point("comparison", "topeka"), year, month, date };
}

export function sunlightLink(href, selection) {
  const url = new URL(href);
  url.search = "";
  url.hash = "";
  for (const key of ["primary", "comparison", "year", "month", "date"]) url.searchParams.set(key, String(selection[key]));
  return url.toString();
}

function subscribeLocation(callback) {
  window.addEventListener("popstate", callback);
  window.addEventListener(LOCATION_EVENT, callback);
  return () => { window.removeEventListener("popstate", callback); window.removeEventListener(LOCATION_EVENT, callback); };
}
const locationSearch = () => window.location.search;
const serverSearch = () => "";

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

export function SunlightSummary({ analysis }) {
  const { summary } = analysis;
  return <dl className={styles.metrics}>
    <div className={styles.primaryMetric}><dt>{analysis.point.name} · mean daily all-sky</dt><dd><strong>{number(summary.primary.mean)}</strong><span>{UNIT}</span></dd><small>{count(summary.primary.validDays)}/{count(summary.expected)} valid modeled days · {count(summary.primary.missingDays)} unavailable</small></div>
    <div className={styles.comparisonMetric}><dt>{analysis.comparisonPoint.name} · mean daily all-sky</dt><dd><strong>{number(summary.comparison.mean)}</strong><span>{UNIT}</span></dd><small>{count(summary.comparison.validDays)}/{count(summary.expected)} valid modeled days · {count(summary.comparison.missingDays)} unavailable</small></div>
    <div><dt>Mean place difference · common dates only</dt><dd><strong>{signed(summary.paired.meanDifference)}</strong><span>{UNIT}</span></dd><small>Primary − comparison · {count(summary.paired.days)}/{count(summary.expected)} common dates</small></div>
  </dl>;
}

export function sunlightSeriesPath(days, place, parameter, x, y) {
  let drawing = false;
  return days.map((day, index) => {
    const reading = day[place][parameter];
    if (!valid(reading)) { drawing = false; return ""; }
    const command = drawing ? "L" : "M";
    drawing = true;
    return `${command}${x(index).toFixed(2)},${y(reading.value).toFixed(2)}`;
  }).join(" ");
}

export function SunlightPlot({ analysis, selectedIndex }) {
  const { days } = analysis;
  const series = [{ place: "primary", parameter: "clearSky", className: "clearLine", label: "Primary modeled clear-sky reference" }, { place: "comparison", parameter: "allSky", className: "comparisonLine", label: `${analysis.comparisonPoint.name} · all-sky` }, { place: "primary", parameter: "allSky", className: "primaryLine", label: `${analysis.point.name} · all-sky` }];
  const values = days.flatMap((day) => series.flatMap(({ place, parameter }) => valid(day[place][parameter]) ? [day[place][parameter].value] : []));
  const topValue = Math.max(2, Math.ceil((values.length ? Math.max(...values) : 10) / 2) * 2);
  const bottom = PLOT.height - PLOT.bottom;
  const x = (index) => PLOT.left + (days.length < 2 ? .5 : index / (days.length - 1)) * (PLOT.width - PLOT.left - PLOT.right);
  const y = (value) => bottom - value / topValue * (bottom - PLOT.top);
  const ticks = Array.from({ length: 6 }, (_, index) => topValue / 5 * index);
  const xTicks = days.reduce((found, day, index) => {
    if (analysis.month ? [0, 7, 14, 21, days.length - 1].includes(index) : day.date.endsWith("-01") && ["01", "03", "05", "07", "09", "11"].includes(day.date.slice(5, 7))) found.push(index);
    return found;
  }, []);
  const selected = days[selectedIndex];
  return <figure className={styles.plot}><figcaption><div><span className={styles.eyebrow}>Incoming shortwave energy / horizontal surface</span><h3>Follow the daily sunlight.</h3></div><span className={styles.plotUnit}>{UNIT} · NASA Local Solar Time</span></figcaption>
    <div className={styles.plotCanvas}><svg viewBox={`0 0 ${PLOT.width} ${PLOT.height}`} preserveAspectRatio="none" role="img" aria-labelledby="sunlight-plot-title sunlight-plot-description">
      <title id="sunlight-plot-title">{`Modeled daily sunlight energy, ${analysis.point.name} and ${analysis.comparisonPoint.name}, ${days[0]?.date ?? "no dates"} through ${days.at(-1)?.date ?? "no dates"}`}</title>
      <desc id="sunlight-plot-description">Two all-sky series share a scale with the primary area’s modeled clear-sky reference. Unavailable values break each line. Isolated valid values remain plotted. Read exact values and source states in the date inspector and daily table below. This is modeled grid context, not ground-station measurements or panel output.</desc>
      {ticks.map((tick) => <line key={tick} className={styles.gridLine} x1={PLOT.left} x2={PLOT.width - PLOT.right} y1={y(tick)} y2={y(tick)} />)}
      {selected && <line className={styles.inspectionLine} x1={x(selectedIndex)} x2={x(selectedIndex)} y1={PLOT.top} y2={bottom} />}
      {series.map(({ place, parameter, className }) => <g key={`${place}-${parameter}`}><path className={styles[className]} d={sunlightSeriesPath(days, place, parameter, x, y)} vectorEffect="non-scaling-stroke" />{days.map((day, index) => valid(day[place][parameter]) && (!index || !valid(days[index - 1][place][parameter])) && (index === days.length - 1 || !valid(days[index + 1][place][parameter])) ? <circle key={day.date} className={styles[`${className}Point`]} cx={x(index)} cy={y(day[place][parameter].value)} r={3.2} /> : null)}{selected && valid(selected[place][parameter]) && <circle className={styles[`${className}Point`]} cx={x(selectedIndex)} cy={y(selected[place][parameter].value)} r={5} />}</g>)}
      {days.map((day, index) => !valid(day.primary.allSky) || !valid(day.comparison.allSky) ? <line key={day.date} className={styles.missingMark} x1={x(index)} x2={x(index)} y1={bottom + 7} y2={bottom + 13} /> : null)}
    </svg><div className={styles.yAxis} aria-hidden="true">{ticks.map((tick) => <span key={tick} style={{ left: `${PLOT.left / PLOT.width * 100}%`, top: `${y(tick) / PLOT.height * 100}%` }}>{number(tick, tick % 1 ? 1 : 0)}</span>)}</div><div className={styles.xAxis} aria-hidden="true">{xTicks.map((index) => <span key={index} style={{ left: `${x(index) / PLOT.width * 100}%`, top: `${(bottom + 34) / PLOT.height * 100}%` }} data-align={index === 0 ? "start" : index === days.length - 1 ? "end" : "middle"}>{dateLabel(days[index].date, true)}</span>)}</div></div>
    <ul className={styles.plotLegend} aria-label="Sunlight series legend">{[...series].reverse().map((item) => <li key={`${item.place}-${item.parameter}`}><i className={styles[`${item.className}Key`]} />{item.label}</li>)}<li><i className={styles.gapKey} />Unavailable dates leave gaps</li></ul>
    <p className={styles.referenceNote}>The dashed clear-sky line is a modeled atmospheric reference. The difference is not measured cloud effect or cloud percentage. All-sky values above the reference remain unchanged.</p>
  </figure>;
}

function ReadingValue({ reading }) {
  return <><strong>{valid(reading) ? number(reading.value) : "Unavailable"}</strong><small>{valid(reading) ? UNIT : "Missing provider value"} · raw <code>{String(reading.raw)}</code> · {reading.state}</small></>;
}

export function SunlightDayInspector({ analysis, selectedIndex, onSelectDate }) {
  const { days } = analysis;
  const day = days[selectedIndex];
  if (!day) return null;
  function selectDate(event) {
    const date = event.currentTarget.value;
    if (calendarDate(date) && days.some((item) => item.date === date)) onSelectDate(date);
  }
  return <section className={styles.inspector} id="sunlight-day" aria-labelledby="sunlight-day-heading"><div className={styles.inspectorHeader}><div><span className={styles.eyebrow}>Read one modeled day</span><h3 id="sunlight-day-heading">{dateLabel(day.date)}</h3><p>NASA Local Solar Time · source JSON key <code>{day.sourceKey}</code></p></div><div className={styles.dateControls}><button type="button" aria-label="Previous calendar day" disabled={selectedIndex === 0} onClick={() => onSelectDate(days[selectedIndex - 1].date)}>←</button><label>Inspect a date<input type="date" value={day.date} min={days[0].date} max={days.at(-1).date} onInput={selectDate} onChange={selectDate} /></label><button type="button" aria-label="Next calendar day" disabled={selectedIndex === days.length - 1} onClick={() => onSelectDate(days[selectedIndex + 1].date)}>→</button></div></div>
    <div className={styles.inspectorReadings}>{[["primary", analysis.point.name], ["comparison", analysis.comparisonPoint.name]].map(([place, name]) => <div key={place}><h4>{name}</h4><dl><div><dt>All-sky · incoming energy<code>ALLSKY_SFC_SW_DWN</code></dt><dd><ReadingValue reading={day[place].allSky} /></dd></div><div><dt>Modeled clear-sky reference<code>CLRSKY_SFC_SW_DWN</code></dt><dd><ReadingValue reading={day[place].clearSky} /></dd></div></dl><a href={analysis.sources[place].url} target="_blank" rel="noreferrer">Original NASA point-query JSON ↗</a><p className={styles.inspectorSource}>Captured {captureLabel(analysis.sources[place].capturedAt)}<br /><span>SHA-256</span> <code>{analysis.sources[place].sha256}</code></p></div>)}</div>
  </section>;
}

export function SunlightMonths({ analysis, onSelectMonth }) {
  return <section className={styles.monthly} aria-labelledby="sunlight-monthly-heading"><div className={styles.sectionHeader}><div><span className={styles.eyebrow}>The whole selected year / {analysis.year}</span><h3 id="sunlight-monthly-heading">See the seasonal rhythm.</h3><p>Select a month to examine its daily record. Means use valid modeled days.</p></div><button type="button" aria-pressed={analysis.month === 0} onClick={() => onSelectMonth(0)}>Show full year</button></div>
    <div className={styles.monthStrip} aria-label="Select a sunlight month">{analysis.monthly.map((month) => <button type="button" key={month.month} aria-label={`Inspect ${MONTHS[month.month - 1]} ${analysis.year}, ${analysis.point.name} mean ${number(month.primary.mean)} ${UNIT}, ${month.primary.validDays} of ${month.expected} valid days`} aria-pressed={analysis.month === month.month} onClick={() => onSelectMonth(month.month)}><span>{MONTHS[month.month - 1].slice(0, 3)}</span><strong>{number(month.primary.mean)}</strong><small>{month.primary.validDays}/{month.expected} days</small></button>)}</div><p className={styles.monthStripNote}>Primary area monthly means · {UNIT}. The table compares both areas on their own valid days and on common dates.</p>
    <div className={styles.tableScroll} role="region" aria-label="Monthly sunlight summaries, horizontally scrollable" tabIndex={0}><table><caption>{analysis.year} monthly modeled sunlight · means and differences in {UNIT}</caption><thead><tr><th scope="col">Month</th><th scope="col">{analysis.point.name}<small>Mean · valid / dates</small></th><th scope="col">{analysis.comparisonPoint.name}<small>Mean · valid / dates</small></th><th scope="col">Primary − comparison<small>Mean difference · common / dates</small></th></tr></thead><tbody>{analysis.monthly.map((month) => <tr key={month.month} data-selected={month.month === analysis.month}><th scope="row">{MONTHS[month.month - 1]}</th><td>{number(month.primary.mean)}<small>{month.primary.validDays}/{month.expected} valid</small></td><td>{number(month.comparison.mean)}<small>{month.comparison.validDays}/{month.expected} valid</small></td><td>{signed(month.paired.meanDifference)}<small>{month.paired.days}/{month.expected} common dates</small></td></tr>)}</tbody></table></div>
  </section>;
}

export default function SunlightAndSky({ manifest }) {
  const search = useSyncExternalStore(subscribeLocation, locationSearch, serverSearch);
  const selection = useMemo(() => sunlightSelection(manifest, search), [manifest, search]);
  const primary = manifest.points.find((point) => point.id === selection.primary);
  const comparison = manifest.points.find((point) => point.id === selection.comparison);
  const pairKey = `${primary.id}:${primary.sha256}:${comparison.id}:${comparison.sha256}`;
  const selectionKey = `${pairKey}:${selection.year}:${selection.month}:${selection.date}`;
  const [result, setResult] = useState(null);
  const [retry, setRetry] = useState(0);
  const requestId = useRef(0);
  const shareId = useRef(0);
  const [share, setShare] = useState(null);
  const [exportError, setExportError] = useState("");
  const [recordsPage, setRecordsPage] = useState({ key: "", page: 0 });

  useEffect(() => {
    const controller = new AbortController();
    const id = ++requestId.current;
    const primaryRead = loadSunlightSnapshot(primary, { signal: controller.signal });
    const comparisonRead = primary.id === comparison.id && primary.sha256 === comparison.sha256 ? primaryRead : loadSunlightSnapshot(comparison, { signal: controller.signal });
    Promise.all([primaryRead, comparisonRead]).then(([primarySnapshot, comparisonSnapshot]) => {
      if (!controller.signal.aborted && requestId.current === id) setResult({ key: pairKey, primarySnapshot, comparisonSnapshot, error: "" });
    }).catch((error) => {
      if (!controller.signal.aborted && requestId.current === id) { controller.abort(); setResult({ key: pairKey, primarySnapshot: null, comparisonSnapshot: null, error: error instanceof Error ? error.message : "The modeled sunlight record could not be read." }); }
    });
    return () => controller.abort();
  }, [primary, comparison, pairKey, retry]);

  const currentResult = result?.key === pairKey ? result : null;
  const analysis = useMemo(() => currentResult?.primarySnapshot && currentResult?.comparisonSnapshot ? analyseSunlight(currentResult.primarySnapshot, currentResult.comparisonSnapshot, { year: selection.year, month: selection.month }) : null, [currentResult, selection.year, selection.month]);
  const days = analysis?.days ?? [];
  const selectedIndex = Math.max(0, days.findIndex((day) => day.date === selection.date));
  const loading = !currentResult;
  const periodLabel = `${selection.month ? `${MONTHS[selection.month - 1]} ` : ""}${selection.year}`;
  const pageKey = `${pairKey}:${selection.year}:${selection.month}`;
  const pageCount = Math.ceil(days.length / PAGE_SIZE);
  const currentPage = recordsPage.key === pageKey ? Math.min(recordsPage.page, Math.max(0, pageCount - 1)) : 0;
  const pageDays = days.slice(currentPage * PAGE_SIZE, (currentPage + 1) * PAGE_SIZE);

  function updateSelection(patch) {
    const next = sunlightSelection(manifest, new URL(sunlightLink(window.location.href, { ...selection, ...patch })).search);
    const href = sunlightLink(window.location.href, next);
    if (href === window.location.href) return;
    if (next.primary !== selection.primary || next.comparison !== selection.comparison) setResult(null);
    shareId.current += 1;
    setShare(null);
    setExportError("");
    window.history.pushState(window.history.state, "", href);
    window.dispatchEvent(new Event(LOCATION_EVENT));
  }

  async function copyLink() {
    const link = sunlightLink(window.location.href, selection);
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
    if (!analysis || !days.length) return;
    try {
      const filename = `kfm-sunlight-${selection.primary}-vs-${selection.comparison}-${selection.year}-${selection.month ? String(selection.month).padStart(2, "0") : "full-year"}`;
      if (kind === "csv") downloadText(sunlightCsv(analysis), "text/csv;charset=utf-8", `${filename}.csv`);
      else downloadText(`${JSON.stringify({ ...sunlightReceipt(analysis), uiContext: { inspectedDate: days[selectedIndex]?.date ?? null, analysisLink: sunlightLink(window.location.href, selection) } }, null, 2)}\n`, "application/json", `${filename}-receipt.json`);
      setExportError("");
    } catch {
      setExportError("This browser could not create the download. Try again or open the original NASA source files below.");
    }
  }

  return <main className={styles.page}><div className={styles.frame}>
    <ScienceNav active="sunlight" selection={selection} sourceHref="#sunlight-sources" sourceLabel="Source & methods ↓" extraLinks={[{ href: "/labs", label: "Research atlas ↗" }]} />
    <header className={styles.hero}><div><span className={styles.eyebrow}>Kansas field notebook / Sunlight &amp; Sky Lab</span><h1>A day’s sunlight.<br /><em>A season’s rhythm.</em></h1><p>How did estimated daily sunlight on a horizontal surface differ between Kansas places and seasons?</p></div><aside className={styles.scope}><span>NASA POWER · historical modeled energy</span><strong>2020–2025</strong><p>{manifest.points.length} query points · nominal {manifest.grid.latitudeDegrees}° × {manifest.grid.longitudeDegrees}° radiation grid<br />{UNIT} · NASA Local Solar Time</p></aside></header>
    <p className={styles.meaningNote}>Satellite observations and radiative-transfer models infer this incoming shortwave energy. These are coarse grid estimates, not ground-station readings, sunlight hours or panel output.</p>

    <section className={styles.setup} aria-labelledby="sunlight-setup-heading"><div className={styles.sectionHeader}><h2 id="sunlight-setup-heading">Choose two places. Follow the same dates.</h2><button type="button" className={styles.shareButton} onClick={copyLink}>Copy analysis link ↗</button></div><div className={styles.selects}>
      <label>Primary area<select value={selection.primary} onChange={(event) => updateSelection({ primary: event.target.value })}>{manifest.points.map((point) => <option key={point.id} value={point.id}>{point.name}</option>)}</select></label>
      <label>Comparison area<select value={selection.comparison} onChange={(event) => updateSelection({ comparison: event.target.value })}>{manifest.points.map((point) => <option key={point.id} value={point.id}>{point.name}</option>)}</select></label>
      <label>Year<select value={selection.year} onChange={(event) => updateSelection({ year: Number(event.target.value) })}>{YEARS.map((year) => <option key={year} value={year}>{year}</option>)}</select></label>
      <label>Time window<select value={selection.month} onChange={(event) => updateSelection({ month: Number(event.target.value) })}><option value={0}>Full year</option>{MONTHS.map((month, index) => <option key={month} value={index + 1}>{month}</option>)}</select></label>
    </div>{selection.primary === selection.comparison && <p className={styles.sameAreaNote}>Both selections use the same query point. A zero common-date difference is valid.</p>}{share?.key === selectionKey && <><p className={styles.shareStatus} role="status">{share.status}</p>{share.fallback && <label className={styles.shareFallback}>Analysis link<input type="text" readOnly value={share.fallback} onFocus={(event) => event.target.select()} /></label>}</>}</section>

    <section className={styles.analysis} aria-labelledby="sunlight-analysis-heading" aria-busy={loading}><div className={styles.sectionHeader}><div><span className={styles.eyebrow}>Daily modeled energy / {periodLabel}</span><h2 id="sunlight-analysis-heading">{primary.name}<span> &amp; </span>{comparison.name}</h2></div><span className={styles.contextTag}>Horizontal surface · NASA LST</span></div>
      {loading && <div className={styles.loadState} role="status"><span>…</span><div><h3>Reading the modeled sunlight record</h3><p>Loading both captured query points and verifying their bytes, hashes and structure.</p></div></div>}
      {currentResult?.error && <div className={styles.loadState} role="alert"><span>!</span><div><h3>The sunlight snapshots could not be loaded.</h3><p>{currentResult.error}</p><button type="button" onClick={() => { setResult(null); setRetry((value) => value + 1); }}>Retry sunlight snapshots</button></div></div>}
      {analysis && <><SunlightSummary analysis={analysis} />{analysis.summary.primary.validDays === 0 && analysis.summary.comparison.validDays === 0 && <div className={styles.emptyState} role="status"><h3>No valid modeled all-sky values in this window.</h3><p>Unavailable dates remain in the record. Choose another time window; missing means are not zero.</p></div>}<SunlightPlot analysis={analysis} selectedIndex={selectedIndex} /><SunlightDayInspector analysis={analysis} selectedIndex={selectedIndex} onSelectDate={(date) => updateSelection({ date })} /><SunlightMonths analysis={analysis} onSelectMonth={(month) => updateSelection({ month })} />
        <details className={styles.dailyRecords}><summary>Daily values &amp; source states<span>An accessible table of the selected calendar</span></summary><div className={styles.recordsBody}><div className={styles.tableScroll} role="region" aria-label="Daily modeled sunlight source values, horizontally scrollable" tabIndex={0}><table><caption>{periodLabel} · {days.length} selected calendar dates · page {currentPage + 1} of {pageCount}</caption><thead><tr><th scope="col">Date / source JSON key</th><th scope="col">Primary all-sky</th><th scope="col">Comparison all-sky</th><th scope="col">Primary clear-sky</th><th scope="col">Comparison clear-sky</th></tr></thead><tbody>{pageDays.map((day) => <tr key={day.date}><th scope="row"><button type="button" onClick={() => updateSelection({ date: day.date })}>{day.date}</button><code>{day.sourceKey}</code></th>{[["primary", "allSky"], ["comparison", "allSky"], ["primary", "clearSky"], ["comparison", "clearSky"]].map(([place, parameter]) => <td key={`${place}-${parameter}`}><ReadingValue reading={day[place][parameter]} /></td>)}</tr>)}</tbody></table></div><div className={styles.pagination}><button type="button" disabled={currentPage === 0} onClick={() => setRecordsPage({ key: pageKey, page: currentPage - 1 })}>← Previous dates</button><span>{currentPage * PAGE_SIZE + 1}–{Math.min((currentPage + 1) * PAGE_SIZE, days.length)} of {days.length}</span><button type="button" disabled={currentPage + 1 >= pageCount} onClick={() => setRecordsPage({ key: pageKey, page: currentPage + 1 })}>Next dates →</button></div></div></details>
      </>}
    </section>

    <section className={styles.evidence} id="sunlight-sources" aria-labelledby="sunlight-sources-heading"><div className={styles.sectionHeader}><div><span className={styles.eyebrow}>Keep the record / repeat the question</span><h2 id="sunlight-sources-heading">Sunlight, with its source attached.</h2></div><span className={styles.contextTag}>Provider context · scientific review pending</span></div><div className={styles.downloads}><button type="button" disabled={!analysis || !days.length} onClick={() => exportAnalysis("csv")}>Download daily CSV ↓</button><button type="button" disabled={!analysis || !days.length} onClick={() => exportAnalysis("receipt")}>Download analysis receipt ↓</button><a href={manifest.documentation} target="_blank" rel="noreferrer">NASA parameter definitions ↗</a></div><p className={styles.downloadNote}>Free downloads cover the full selected window. They retain both places, all-sky and clear-sky values, unavailable states, source hashes and selection settings. The JSON records the inspected date as context; its analysis still covers the full selected window.</p>{exportError && <p className={styles.errorText} role="alert">{exportError}</p>}
      <div className={styles.methodIntro}><div><h3>Energy, not electricity.</h3><p>Daily incoming shortwave energy is expressed in kilowatt-hours per square meter of horizontal surface. It is not useful electricity, panel yield, sunlight hours, PAR, a forecast or a site-design assessment.</p><p>NASA Local Solar Time uses a 15° longitude swath. These daily dates are not civil CST/CDT. Six historical years do not establish a climate normal or trend. NASA’s global validation statistics do not establish local error bounds for these query points.</p></div><div><h3>Keep the comparisons on common dates.</h3><p>Each area’s mean and sum use its own valid modeled days. The place difference is primary minus comparison using only dates valid in both all-sky series. Missing values do not count as zero.</p>{analysis && <dl className={styles.clearSkySummary}><div><dt>Primary all-sky − clear-sky mean difference</dt><dd>{signed(analysis.summary.clearSky.meanDifference)} {UNIT}<small>{analysis.summary.clearSky.days}/{analysis.expected} dates valid in both primary series</small></dd></div></dl>}<p>The modeled clear-sky reference is not measured cloud effect or a cloud percentage. Values above that reference are retained without clipping.</p></div></div>
      <details className={styles.methods}><summary>Query points, modeled grid context &amp; source integrity</summary><div className={styles.methodsBody}><p>{manifest.grid.description} Three query points provide context for coarse radiation grids, not complete coverage of an area, county or field. Returned coordinates are provider point-query metadata; they do not verify grid-cell centers or boundaries.</p><div className={styles.sourcePoints}>{[primary, ...(comparison.id === primary.id ? [] : [comparison])].map((point) => <article key={point.id}><h3>{point.name}</h3><dl><div><dt>Queried latitude, longitude</dt><dd><code>{String(point.latitude)}, {String(point.longitude)}</code></dd></div><div><dt>Returned geometry array</dt><dd><code>[{point.provider.returnedCoordinates.join(", ")}]</code><small>Longitude, latitude, elevation · provider metadata</small></dd></div><div><dt>Provider / API</dt><dd>{manifest.provider} · {point.provider.api.name} {point.provider.api.version}</dd></div><div><dt>Radiation product / time</dt><dd>{point.provider.sources.join(", ")} · {point.provider.timeStandard}</dd></div><div><dt>Source capture</dt><dd><time dateTime={point.source.capturedAt}>{captureLabel(point.source.capturedAt)}</time>{point.source.lastModified && <small>Last-Modified: {point.source.lastModified}</small>}</dd></div><div><dt>Original query / SHA-256</dt><dd><a href={point.source.url} target="_blank" rel="noreferrer">Open NASA daily point-query JSON ↗</a><code>{point.source.sha256}</code><small>{count(point.source.bytes)} captured bytes</small></dd></div><div><dt>Verified display / SHA-256</dt><dd><a href={point.url}>Open captured display snapshot ↗</a><code>{point.sha256}</code><small>{count(point.bytes)} decoded bytes · {count(point.records)} calendar records</small></dd></div></dl></article>)}</div><div className={styles.documentationLinks}><a href={manifest.documentation} target="_blank" rel="noreferrer">Daily parameter documentation ↗</a><a href={manifest.methodology} target="_blank" rel="noreferrer">NASA POWER methodology ↗</a><a href={manifest.timeDocumentation} target="_blank" rel="noreferrer">Local Solar Time definition ↗</a><a href={manifest.rights} target="_blank" rel="noreferrer">NASA data rights ↗</a><a href={manifest.referencing} target="_blank" rel="noreferrer">POWER credit &amp; citation guidance ↗</a></div><p>{manifest.acknowledgment}</p><p>Source parameter <code>ALLSKY_SFC_SW_DWN</code> is all-sky incoming shortwave energy at a horizontal surface. <code>CLRSKY_SFC_SW_DWN</code> is the modeled clear-sky reference. Provider missing sentinel −999 becomes unavailable; an actual zero remains valid. Original raw values and JSON date keys remain in the export.</p><p className={styles.integrityNote}>KFM calculated these SHA-256 hashes to identify local captured bytes. They are not provider-issued checksums or scientific validation. Scientific review and dataset admission remain pending; dataset release remains unreleased.</p></div></details>
      <aside className={styles.related}><h3>Keep exploring.</h3><p>Daily modeled energy here is separate from the map’s monthly PRISM solar archive and calculated daylight.</p><Link href="/labs/heat-and-rain">Measured Heat &amp; Rain Lab ↗</Link><Link href="/labs/soil-profile">Measured Soil Profile Lab ↗</Link><Link href="/science">All science tools ↗</Link><Link href="/topics#sky">Sky geometry &amp; related tools ↗</Link><Link href="/?topic=weather">Weather &amp; climate map layers ↗</Link></aside><footer className={styles.footer}><span>Kansas Frontier Matrix · Sunlight &amp; Sky Lab</span><Link href="/science">Choose another science question ↗</Link></footer>
    </section>
  </div></main>;
}
