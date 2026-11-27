"use client";

import { useEffect, useMemo, useRef, useState, useSyncExternalStore } from "react";
import Link from "next/link";
import { loadSoilSnapshot } from "./snapshot-loader.mjs";
import { analyseSoil, soilCsv, soilReceipt, soilReadingLabel } from "./soil-model.mjs";
import styles from "./soil-profile.module.css";

const MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
const DEPTHS = [5, 10, 20, 50, 100];
const COLORS = ["#f4d38b", "#eba485", "#86d9c5", "#a8ccec", "#cbb4e8"];
const DASHES = ["", "8 3", "", "3 3", "9 3 2 3"];
const LOCATION_EVENT = "kfm-soil-selection";
const PAGE_SIZE = 10;
const PLOT = { width: 940, height: 326, left: 65, right: 24, top: 24, bottom: 53 };
const number = (value, digits = 0) => Number.isFinite(value) ? value.toLocaleString("en-US", { maximumFractionDigits: digits, minimumFractionDigits: digits }) : "—";
const unit = (variable) => variable === "temperature" ? "°C" : "m³/m³";
const variableLabel = (variable) => variable === "temperature" ? "Soil temperature" : "Volumetric water content";
const digits = (variable) => variable === "temperature" ? 1 : 3;

function integer(raw, minimum, maximum, fallback) {
  return raw !== null && /^\d+$/.test(raw) && Number(raw) >= minimum && Number(raw) <= maximum ? Number(raw) : fallback;
}

function calendarDate(date) {
  if (!/^\d{4}-\d{2}-\d{2}$/.test(date)) return false;
  const parsed = new Date(`${date}T12:00:00Z`);
  return Number.isFinite(parsed.getTime()) && parsed.toISOString().slice(0, 10) === date;
}

export function soilSelection(manifest, search = "") {
  const query = new URLSearchParams(search);
  const preferred = manifest.stations.find((station) => /Oakley/i.test(station.name)) ?? manifest.stations[0];
  const year = integer(query.get("year"), 2020, 2025, 2025);
  const month = integer(query.get("month"), 0, 12, 0);
  const requestedDate = query.get("date") ?? "";
  const date = calendarDate(requestedDate) && requestedDate.startsWith(String(year)) && (!month || Number(requestedDate.slice(5, 7)) === month)
    ? requestedDate : `${year}-${String(month || 7).padStart(2, "0")}-15`;
  return {
    station: manifest.stations.some((station) => station.id === query.get("station")) ? query.get("station") : preferred.id,
    year,
    month,
    depth: DEPTHS.includes(Number(query.get("depth"))) ? Number(query.get("depth")) : 20,
    variable: query.get("variable") === "temperature" ? "temperature" : "moisture",
    date,
  };
}

export function soilLink(href, selection) {
  const url = new URL(href);
  url.search = "";
  url.hash = "";
  for (const key of ["station", "year", "month", "depth", "variable", "date"]) url.searchParams.set(key, String(selection[key]));
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

function dateLabel(date, short = false) {
  return new Intl.DateTimeFormat("en-US", { timeZone: "UTC", month: short ? "short" : "long", day: "numeric", ...(short ? {} : { year: "numeric" }) }).format(new Date(`${date}T12:00:00Z`));
}

function captureLabel(raw) {
  const value = new Date(raw);
  return Number.isFinite(value.getTime()) ? value.toISOString().replace("T", " ").replace(/\.\d+Z$/, " UTC") : "Not supplied";
}

function plotDomain(values, variable) {
  const finite = values.filter(Number.isFinite);
  const low = finite.length ? Math.min(...finite) : 0;
  const high = finite.length ? Math.max(...finite) : variable === "temperature" ? 20 : 0.4;
  const span = Math.max(high - low, variable === "temperature" ? 10 : 0.1);
  const magnitude = 10 ** Math.floor(Math.log10(span / 4));
  const step = [1, 2, 5, 10].map((factor) => factor * magnitude).find((value) => span / value <= 5) ?? magnitude * 10;
  const min = Math.floor(low / step) * step;
  const max = Math.max(min + step, Math.ceil(high / step) * step);
  return { min, max, ticks: Array.from({ length: Math.round((max - min) / step) + 1 }, (_, index) => min + index * step) };
}

export function soilSeriesPath(days, variable, depthIndex, x, y) {
  let drawing = false;
  return days.map((day, index) => {
    const value = day[variable][depthIndex].value;
    if (!Number.isFinite(value)) { drawing = false; return ""; }
    const command = drawing ? "L" : "M";
    drawing = true;
    return `${command}${x(index).toFixed(2)},${y(value).toFixed(2)}`;
  }).join(" ");
}

export function SoilMetrics({ analysis, variable, depth }) {
  return <dl className={styles.metrics}>
    <div><dt>Median at {depth} cm</dt><dd><strong>{number(analysis.median, digits(variable))}</strong><span>{unit(variable)}</span></dd><small>{analysis.valid}/{analysis.expected} valid daily readings</small></div>
    <div><dt>Observed range</dt><dd className={styles.range}><strong>{number(analysis.min, digits(variable))}<span> – </span>{number(analysis.max, digits(variable))}</strong></dd><small>{unit(variable)} · lowest to highest daily average</small></div>
    <div><dt>Missing or withheld</dt><dd><strong>{number(analysis.missing)}</strong><span>days</span></dd><small>{analysis.expected} calendar dates · no gap filling</small></div>
    <div><dt>Daily mean at or below 0 °C</dt><dd><strong>{analysis.temperatureValid ? number(analysis.meanColdDays) : "—"}</strong><span>days</span></dd><small>{analysis.temperatureValid}/{analysis.expected} valid temperatures · {depth} cm</small></div>
  </dl>;
}

export function SoilPlot({ analysis, variable, depth, selectedIndex, onSelectDepth }) {
  const days = analysis.days;
  const innerWidth = PLOT.width - PLOT.left - PLOT.right;
  const bottom = PLOT.height - PLOT.bottom;
  const innerHeight = bottom - PLOT.top;
  const domain = plotDomain(days.flatMap((day) => day[variable].map((reading) => reading.value)), variable);
  const x = (index) => PLOT.left + (days.length < 2 ? innerWidth / 2 : index / (days.length - 1) * innerWidth);
  const y = (value) => bottom - (value - domain.min) / (domain.max - domain.min) * innerHeight;
  const chosenIndex = DEPTHS.indexOf(depth);
  const current = days[selectedIndex];
  const month = analysis.settings.month;
  const year = analysis.settings.year;
  const xTicks = days.reduce((ticks, day, index) => {
    if (month ? [0, 7, 14, 21, days.length - 1].includes(index) : day.date.endsWith("-01") && ["01", "03", "05", "07", "09", "11"].includes(day.date.slice(5, 7))) ticks.push(index);
    return ticks;
  }, []);
  const order = DEPTHS.map((_depth, index) => index).filter((index) => index !== chosenIndex).concat(chosenIndex);
  return <figure className={styles.plot}>
    <div className={styles.plotHeader}><div className={styles.depthLegend} role="group" aria-label="Choose highlighted depth">{DEPTHS.map((value, index) => <button type="button" key={value} aria-pressed={depth === value} onClick={() => onSelectDepth(value)} style={{ "--depth-color": COLORS[index] }}><i />{value} cm</button>)}</div><span className={styles.axisUnit}>{variableLabel(variable)} · {unit(variable)}</span></div>
    <div className={styles.plotScroll} role="region" aria-label="Daily soil observations chart, horizontally scrollable" tabIndex={0}>
      <svg className={styles.chart} viewBox={`0 0 ${PLOT.width} ${PLOT.height}`} role="img" aria-labelledby="soil-chart-title soil-chart-description">
        <title id="soil-chart-title">{`${variableLabel(variable)} at five depths · ${analysis.station.name} · ${year}`}</title><desc id="soil-chart-description">The {depth} centimeter measurements are emphasized. Other depths provide context. Lines break wherever daily observations are missing or withheld. Use the date inspector for exact values.</desc>
        {domain.ticks.map((tick) => <g key={tick}><line x1={PLOT.left} x2={PLOT.width - PLOT.right} y1={y(tick)} y2={y(tick)} className={styles.gridLine} /><text x={PLOT.left - 12} y={y(tick) + 5} textAnchor="end" className={styles.axisText}>{number(tick, variable === "temperature" ? 0 : 2)}</text></g>)}
        {variable === "temperature" && domain.min <= 0 && domain.max >= 0 && <line x1={PLOT.left} x2={PLOT.width - PLOT.right} y1={y(0)} y2={y(0)} className={styles.zeroLine} />}
        {order.map((index) => <path key={DEPTHS[index]} d={soilSeriesPath(days, variable, index, x, y)} className={depth === DEPTHS[index] ? styles.chosenLine : styles.contextLine} stroke={COLORS[index]} strokeDasharray={DASHES[index]} />)}
        {days.length <= 31 && days.flatMap((day, index) => Number.isFinite(day[variable][chosenIndex].value) ? [<circle key={day.date} cx={x(index)} cy={y(day[variable][chosenIndex].value)} r={2.3} fill={COLORS[chosenIndex]} />] : [])}
        {xTicks.map((index) => <text key={index} x={x(index)} y={PLOT.height - 19} textAnchor="middle" className={styles.axisText}>{month ? Number(days[index].date.slice(8, 10)) : MONTHS[Number(days[index].date.slice(5, 7)) - 1].slice(0, 3)}</text>)}
        {current && <g><line x1={x(selectedIndex)} x2={x(selectedIndex)} y1={PLOT.top} y2={bottom + 10} className={styles.selectedLine} />{current[variable].map((reading, index) => Number.isFinite(reading.value) && <circle key={DEPTHS[index]} cx={x(selectedIndex)} cy={y(reading.value)} r={index === chosenIndex ? 4.5 : 2.5} fill={COLORS[index]} stroke="#0b252e" strokeWidth={1.5} />)}</g>}
        {!analysis.valid && <text x={PLOT.left + innerWidth / 2} y={PLOT.top + innerHeight / 2} textAnchor="middle" className={styles.emptyPlot}>{depth} cm: no valid {variable} observations</text>}
      </svg>
    </div>
    <figcaption className={styles.plotCaption}><span>{days.length ? `${dateLabel(days[0].date, true)} – ${dateLabel(days.at(-1).date, true)}, ${year}` : year} · NOAA USCRN daily averages</span><span>Emphasized: {depth} cm · missing readings leave line gaps.</span></figcaption>
  </figure>;
}

export function SoilDayInspector({ days, selectedIndex, variable, depth, onSelectDate, onSelectDepth }) {
  const day = days[selectedIndex];
  if (!day) return null;
  const domain = plotDomain(day[variable].map((reading) => reading.value), variable);
  const x = (value) => 70 + (value - domain.min) / (domain.max - domain.min) * 252;
  const y = (value) => 35 + value / 100 * 300;
  function selectDate(event) {
    const value = event.currentTarget.value;
    if (days.some((candidate) => candidate.date === value)) onSelectDate(value);
  }
  return <section className={styles.inspector} aria-labelledby="soil-inspector-heading">
    <div className={styles.inspectorHeading}><div><span className={styles.eyebrow}>One day / five measured depths</span><h3 id="soil-inspector-heading">Look beneath the surface.</h3></div><div className={styles.dateControls}><label htmlFor="soil-inspection-date">Inspect a daily observation<input id="soil-inspection-date" type="date" value={day.date} min={days[0].date} max={days.at(-1).date} onInput={selectDate} onChange={selectDate} /></label><div className={styles.dayArrows}><button type="button" aria-label="Previous observation day" disabled={selectedIndex === 0} onClick={() => onSelectDate(days[selectedIndex - 1].date)}>←</button><button type="button" aria-label="Next observation day" disabled={selectedIndex === days.length - 1} onClick={() => onSelectDate(days[selectedIndex + 1].date)}>→</button></div></div></div>
    <div className={styles.profileGrid}>
      <figure className={styles.profile}>
        <div className={styles.profileScroll} role="region" aria-label="Selected-day depth profile, horizontally scrollable" tabIndex={0}>
          <svg viewBox="0 0 380 402" role="img" aria-labelledby="soil-profile-title soil-profile-description">
            <title id="soil-profile-title">{`${variableLabel(variable)} at five measured depths on ${dateLabel(day.date)}`}</title>
            <desc id="soil-profile-description">Separate points represent observations at 5, 10, 20, 50 and 100 centimeters. There is no interpolated value between these depths. Missing observations have no point.</desc>
            <text x="9" y="18" className={styles.profileLabel}>Depth</text>
            <text x="324" y="18" textAnchor="end" className={styles.profileLabel}>{unit(variable)}</text>
            {domain.ticks.map((tick) => <g key={tick}><line x1={x(tick)} x2={x(tick)} y1={35} y2={335} className={styles.profileGridLine} /><text x={x(tick)} y={365} textAnchor="middle" className={styles.profileLabel}>{number(tick, variable === "temperature" ? 0 : 2)}</text></g>)}
            {DEPTHS.map((value, index) => <g key={value}>
              <line x1={60} x2={332} y1={y(value)} y2={y(value)} className={styles.profileDepthLine} />
              <text x={49} y={y(value) + 4} textAnchor="end" className={styles.profileLabel}>{value} cm</text>
              {Number.isFinite(day[variable][index].value) ? <circle cx={x(day[variable][index].value)} cy={y(value)} r={depth === value ? 6 : 4} fill={COLORS[index]} stroke={depth === value ? "#f4efdf" : "none"} strokeWidth={1.5} /> : <text x={195} y={y(value) + 4} textAnchor="middle" className={styles.profileGap}>Missing or withheld</text>}
            </g>)}
          </svg>
        </div>
        <figcaption>Five measurement depths. The soil between them is not measured here.<span className={styles.profileHint}>Scroll across for the complete profile on small screens.</span></figcaption>
      </figure>
      <div className={styles.profileReadings} aria-live="polite" aria-atomic="true"><div className={styles.inspectedDate}><time dateTime={day.date}>{dateLabel(day.date)}</time><span>Local standard day · UTC−6</span></div><div className={styles.tableScroll} role="region" aria-label="Selected day readings at each depth, horizontally scrollable" tabIndex={0}><table className={styles.dayTable}><caption>Moisture and temperature are independent daily averages.</caption><thead><tr><th scope="col">Depth</th><th scope="col">Moisture · m³/m³</th><th scope="col">Temperature · °C</th></tr></thead><tbody>{DEPTHS.map((value, index) => <tr key={value} data-selected={depth === value}><th scope="row"><button type="button" onClick={() => onSelectDepth(value)} aria-pressed={depth === value} style={{ "--depth-color": COLORS[index] }}><i />{value} cm</button></th>{["moisture", "temperature"].map((measure) => <td key={measure} data-state={day[measure][index].state}><strong>{soilReadingLabel(day[measure][index], measure)}</strong><span>Raw {day[measure][index].raw ?? "absent"} · {day[measure][index].state}</span></td>)}</tr>)}</tbody></table></div><p className={styles.versionNote}>Datalogger version {day.version ?? "not supplied"} · no interpolation between days or depths.</p></div>
    </div>
  </section>;
}

export function SoilCoverage({ analysis, variable, depth, onSelectDepth }) {
  return <section className={styles.coverage} aria-labelledby="soil-coverage-heading"><div className={styles.sectionHeader}><div><h3 id="soil-coverage-heading">Every depth has its own evidence.</h3><p>Missing observations can differ by depth and measurement. Select a row to emphasize that depth.</p></div><span className={styles.tableUnit}>{unit(variable)}</span></div><div className={styles.tableScroll} role="region" aria-label="Observation coverage by depth, horizontally scrollable" tabIndex={0}><table className={styles.coverageTable}><caption>{variableLabel(variable)} · {analysis.expected} calendar dates in this selection.</caption><thead><tr><th scope="col">Depth</th><th scope="col">Valid / expected</th><th scope="col">Missing / withheld</th><th scope="col">Median</th><th scope="col">Observed range</th><th scope="col">Mean ≤ 0 °C days</th></tr></thead><tbody>{analysis.depths.map((row) => <tr key={row.depthCm} data-selected={depth === row.depthCm}><th scope="row"><button type="button" aria-pressed={depth === row.depthCm} onClick={() => onSelectDepth(row.depthCm)}>{row.depthCm} cm<span aria-hidden="true">↗</span></button></th><td>{row.valid}/{analysis.expected}</td><td>{row.missing}</td><td>{number(row.median, digits(variable))}</td><td>{number(row.min, digits(variable))} – {number(row.max, digits(variable))}</td><td>{row.temperatureValid ? row.meanColdDays : "—"}<small>{row.temperatureValid}/{analysis.expected} valid temperatures</small></td></tr>)}</tbody></table></div><p className={styles.coverageNote}>A daily mean at or below 0 °C can miss shorter freezes. A missing moisture reading alone does not identify frozen soil.</p></section>;
}

function downloadText(text, type, filename) {
  const objectUrl = URL.createObjectURL(new Blob([text], { type }));
  const link = document.createElement("a");
  link.href = objectUrl;
  link.download = filename;
  document.body.append(link);
  link.click();
  link.remove();
  setTimeout(() => URL.revokeObjectURL(objectUrl), 1000);
}

export default function SoilProfile({ manifest }) {
  const search = useSyncExternalStore(subscribeLocation, locationSearch, serverSearch);
  const selection = useMemo(() => soilSelection(manifest, search), [manifest, search]);
  const descriptor = manifest.stations.find((station) => station.id === selection.station);
  const [result, setResult] = useState(null);
  const [retry, setRetry] = useState(0);
  const requestId = useRef(0);
  const [recordsPage, setRecordsPage] = useState({ key: "", page: 0 });
  const [shareStatus, setShareStatus] = useState("");
  const [shareFallback, setShareFallback] = useState("");
  const [exportError, setExportError] = useState("");
  const shareId = useRef(0);

  useEffect(() => {
    const controller = new AbortController();
    const id = ++requestId.current;
    loadSoilSnapshot(descriptor, { signal: controller.signal }).then((snapshot) => {
      if (!controller.signal.aborted && requestId.current === id) setResult({ stationId: descriptor.id, snapshot, error: "" });
    }).catch((error) => {
      if (!controller.signal.aborted && requestId.current === id) setResult({ stationId: descriptor.id, snapshot: null, error: error instanceof Error ? error.message : "The station snapshot could not be read." });
    });
    return () => controller.abort();
  }, [descriptor, retry]);

  const currentResult = result?.stationId === selection.station ? result : null;
  const snapshot = currentResult?.snapshot ?? null;
  const analysis = useMemo(() => snapshot ? analyseSoil(snapshot, { year: selection.year, month: selection.month, depth: selection.depth, variable: selection.variable }) : null, [snapshot, selection.year, selection.month, selection.depth, selection.variable]);
  const days = analysis?.days ?? [];
  const selectedIndex = Math.max(0, days.findIndex((day) => day.date === selection.date));
  const analysisKey = `${selection.station}:${selection.year}:${selection.month}`;
  const pageCount = Math.ceil(days.length / PAGE_SIZE);
  const currentPage = recordsPage.key === analysisKey ? Math.min(recordsPage.page, Math.max(0, pageCount - 1)) : 0;
  const pageDays = days.slice(currentPage * PAGE_SIZE, (currentPage + 1) * PAGE_SIZE);
  const loading = !currentResult;
  const periodLabel = `${selection.month ? `${MONTHS[selection.month - 1]} ` : ""}${selection.year}`;

  function updateSelection(patch) {
    const next = soilSelection(manifest, new URL(soilLink(window.location.href, { ...selection, ...patch })).search);
    if (next.station !== selection.station) setResult(null);
    shareId.current += 1;
    setShareStatus("");
    setShareFallback("");
    setExportError("");
    window.history.replaceState(window.history.state, "", soilLink(window.location.href, next));
    window.dispatchEvent(new Event(LOCATION_EVENT));
  }

  async function copyLink() {
    const link = soilLink(window.location.href, selection);
    const id = ++shareId.current;
    try {
      if (!navigator.clipboard?.writeText) throw new Error("Clipboard unavailable");
      await navigator.clipboard.writeText(link);
      if (id === shareId.current) { setShareStatus("Analysis link copied, including the inspected date."); setShareFallback(""); }
    } catch {
      if (id === shareId.current) { setShareFallback(link); setShareStatus("Select and copy the analysis link below."); }
    }
  }

  function exportAnalysis(kind) {
    if (!analysis || !snapshot || !days.length) return;
    try {
      const filename = `kfm-soil-${selection.station}-${selection.year}${selection.month ? `-${String(selection.month).padStart(2, "0")}` : ""}`;
      if (kind === "csv") downloadText(soilCsv(analysis, manifest.citation), "text/csv;charset=utf-8", `${filename}.csv`);
      else downloadText(`${JSON.stringify({ ...soilReceipt(analysis, descriptor, manifest.citation), selectedDate: days[selectedIndex]?.date ?? null }, null, 2)}\n`, "application/json", `${filename}-receipt.json`);
      setExportError("");
    } catch {
      setExportError("This browser could not create the download. Try again or open the original NOAA sources below.");
    }
  }

  return <main className={styles.page}><div className={styles.frame}>
    <nav className={styles.navigation} aria-label="Science lab navigation"><Link href="/">← KFM Explorer</Link><Link href="/science">Science tools</Link><Link href="/observatory/sources">Research & sources</Link><a href="#soil-evidence">Source & methods ↓</a></nav>
    <header className={styles.hero}><div><span className={styles.eyebrow}>Kansas field notebook / Soil Profile Lab</span><h1>What changes<br /><em>beneath the surface?</em></h1><p>Follow daily moisture and temperature at five measured depths. Start with a season, then inspect one day in the soil.</p></div><div className={styles.scope}><span className={styles.badge}><i />NOAA USCRN observations</span><strong>5 → 100 <span>cm</span></strong><span>2 Kansas stations · 2020–2025<br />Five depths · daily averages</span></div></header>

    <section className={styles.setup} aria-labelledby="soil-setup-heading"><div className={styles.sectionHeader}><div><span className={styles.eyebrow}>01 / Choose your observations</span><h2 id="soil-setup-heading">A place, a season, a depth.</h2></div><button type="button" className={styles.shareButton} onClick={copyLink}>Copy analysis link ↗</button></div><div className={styles.selects}>
      <label>Soil station<select value={selection.station} onChange={(event) => updateSelection({ station: event.target.value })}>{manifest.stations.map((station) => <option key={station.id} value={station.id}>{station.name}</option>)}</select></label>
      <label>Year<select value={selection.year} onChange={(event) => updateSelection({ year: Number(event.target.value) })}>{[2025, 2024, 2023, 2022, 2021, 2020].map((year) => <option key={year} value={year}>{year}</option>)}</select></label>
      <label>Time window<select value={selection.month} onChange={(event) => updateSelection({ month: Number(event.target.value) })}><option value={0}>Full year</option>{MONTHS.map((month, index) => <option key={month} value={index + 1}>{month}</option>)}</select></label>
      <label>Measurement<select value={selection.variable} onChange={(event) => updateSelection({ variable: event.target.value })}><option value="moisture">Soil moisture · m³/m³</option><option value="temperature">Soil temperature · °C</option></select></label>
      <label>Highlighted depth<select value={selection.depth} onChange={(event) => updateSelection({ depth: Number(event.target.value) })}>{DEPTHS.map((depth) => <option key={depth} value={depth}>{depth} cm</option>)}</select></label>
    </div><p className={styles.shareStatus} role="status">{shareStatus}</p>{shareFallback && <label className={styles.shareFallback}>Analysis link<input type="text" readOnly value={shareFallback} onFocus={(event) => event.target.select()} /></label>}</section>

    <section className={styles.analysis} aria-labelledby="soil-analysis-heading" aria-busy={loading}><div className={styles.sectionHeader}><div><span className={styles.eyebrow}>02 / Read the measurements</span><h2 id="soil-analysis-heading">{descriptor.name}<span className={styles.headingPeriod}> / {periodLabel}</span></h2></div><span className={styles.stationId}>WBAN {descriptor.id}</span></div>
      {loading && <div className={styles.loadState} role="status"><span className={styles.statusMark}>…</span><div><h3>Reading {descriptor.name} observations</h3><p>Loading and verifying the selected station snapshot.</p></div></div>}
      {currentResult?.error && <div className={styles.loadState} role="alert"><span className={styles.statusMark}>!</span><div><h3>The station snapshot could not be loaded.</h3><p>{currentResult.error}</p><button type="button" onClick={() => { setResult(null); setRetry((value) => value + 1); }}>Retry station snapshot</button></div></div>}
      {analysis && <><SoilMetrics analysis={analysis} variable={selection.variable} depth={selection.depth} /><p className={styles.coverageNote}>Moisture is the volume of water per volume of soil, not plant-available water or percent saturation. Cold-day counts use independent temperature observations.</p>
        {!days.length ? <div className={styles.loadState} role="status"><div><h3>No daily records in this selection.</h3><p>Choose another month or year. Missing observations are never filled with estimated soil conditions.</p></div></div> : <><div className={styles.plotIntro}><h3>{selection.variable === "moisture" ? "Follow water at each depth." : "Watch the season reach deeper."}</h3><p>Choose a depth to emphasize it. Read exact measurements in the date inspector.</p></div><SoilPlot analysis={analysis} variable={selection.variable} depth={selection.depth} selectedIndex={selectedIndex} onSelectDepth={(depth) => updateSelection({ depth })} /><SoilDayInspector days={days} selectedIndex={selectedIndex} variable={selection.variable} depth={selection.depth} onSelectDate={(date) => updateSelection({ date })} onSelectDepth={(depth) => updateSelection({ depth })} /></>}
        <SoilCoverage analysis={analysis} variable={selection.variable} depth={selection.depth} onSelectDepth={(depth) => updateSelection({ depth })} />
        <details className={styles.records}><summary>Inspect daily source records<span>All five depths · raw tokens and states</span></summary><div className={styles.recordsBody}><p>Each cell retains its raw source token and interpretation. Missing moisture (−99.000) and temperature (−9999.0) are not zero. Out-of-range values are withheld. Download the CSV for all depths and dates together.</p><div className={styles.tableScroll} role="region" aria-label="Daily soil source records, horizontally scrollable" tabIndex={0}><table className={styles.recordsTable}><caption>{descriptor.name} · {periodLabel} · {variableLabel(selection.variable)} · page {pageCount ? currentPage + 1 : 0} of {pageCount}</caption><thead><tr><th scope="col">Observation date</th>{DEPTHS.map((depth) => <th key={depth} scope="col">{depth} cm · {unit(selection.variable)}</th>)}<th scope="col">Version</th></tr></thead><tbody>{pageDays.map((day) => <tr key={day.date}><th scope="row"><time dateTime={day.date}>{day.date}</time></th>{day[selection.variable].map((reading, index) => <td key={DEPTHS[index]} data-state={reading.state}>{soilReadingLabel(reading, selection.variable)}<small>Raw {reading.raw ?? "absent"} · {reading.state}</small></td>)}<td>{day.version ?? "—"}</td></tr>)}</tbody></table></div><div className={styles.pagination}><button type="button" disabled={currentPage === 0} onClick={() => setRecordsPage({ key: analysisKey, page: currentPage - 1 })}>← Previous</button><span>{days.length ? `${currentPage * PAGE_SIZE + 1}–${Math.min((currentPage + 1) * PAGE_SIZE, days.length)} of ${days.length} dates` : "No dates"}</span><button type="button" disabled={currentPage + 1 >= pageCount} onClick={() => setRecordsPage({ key: analysisKey, page: currentPage + 1 })}>Next →</button></div></div></details>
      </>}
    </section>

    <section className={styles.evidence} id="soil-evidence" aria-labelledby="soil-evidence-heading"><div className={styles.sectionHeader}><div><span className={styles.eyebrow}>03 / Keep the evidence</span><h2 id="soil-evidence-heading">Every reading has roots.</h2></div><span className={styles.evidenceTag}>Provider context · review pending</span></div><div className={styles.downloads}><button type="button" disabled={!analysis || !days.length} onClick={() => exportAnalysis("csv")}>Download daily CSV ↓</button><button type="button" disabled={!analysis || !days.length} onClick={() => exportAnalysis("receipt")}>Download analysis receipt ↓</button><a href={manifest.documentation} target="_blank" rel="noreferrer">NOAA documentation ↗</a></div><p className={styles.downloadNote}>The CSV contains both measurements, raw tokens and states for all five depths. The JSON records coverage, summaries, settings and the inspected date. Both include NOAA citations and source capture details.</p>{exportError && <p role="alert" className={styles.errorText}>{exportError}</p>}
      <div className={styles.evidenceGrid}><div><h3>A station point, in its place.</h3><dl className={styles.sourceFacts}><div><dt>Station</dt><dd>{descriptor.name} · WBAN {descriptor.id}</dd></div><div><dt>Coordinates</dt><dd>{number(descriptor.latitude, 2)}°, {number(descriptor.longitude, 2)}°</dd></div><div><dt>Provider</dt><dd>{manifest.provider}</dd></div><div><dt>Snapshot period</dt><dd>{manifest.period.from} through {manifest.period.to}</dd></div><div><dt>Observation day</dt><dd>Local standard time · UTC−6 all year</dd></div><div><dt>Measurement depths</dt><dd>5, 10, 20, 50 and 100 cm</dd></div></dl></div><div className={styles.limitations}><h3>Understand the soil, and the limits.</h3><p>Daily averages come from hourly sensors at five separate depths. These are station observations, not a county average, a satellite pixel or a continuous 0–100 cm water profile.</p><p>NOAA may suppress moisture observations near freezing. Missing data alone does not identify the cause. A daily mean at or below 0 °C does not count every brief freeze.</p><p>Differences between depths or stations can reflect soil and site conditions. Curves alone do not establish infiltration or rainfall effects. Six years do not establish a climate normal.</p></div></div>
      <details className={styles.methods}><summary>Measurement rules, original files & integrity</summary><div className={styles.methodsBody}><p>Moisture is volumetric water content, measured in m³/m³. Temperature is in °C. Missing tokens remain missing; values outside 0–1 m³/m³ or −50–60 °C are withheld from analysis and retain their raw tokens. No values are interpolated between dates or depths, and no root-zone average is inferred.</p><p>The mean ≤ 0 °C count uses valid daily mean temperature at the chosen depth, with a separate denominator from moisture. It is not a duration of frozen soil. NOAA local standard dates remain UTC−6 throughout the year, without daylight saving adjustment.</p><p>Datalogger version is retained for each day. Version and processing changes can affect comparability; consult NOAA’s documentation before treating changes as environmental signals.</p><p>{manifest.citation}</p><div className={styles.documentationLinks}><a href="https://doi.org/10.1175/JHM-D-12-0146.1" target="_blank" rel="noreferrer">Soil moisture & temperature measurement paper ↗</a><a href="https://doi.org/10.1175/BAMS-D-12-00170.1" target="_blank" rel="noreferrer">USCRN network reference ↗</a><a href={manifest.documentation} target="_blank" rel="noreferrer">Daily observations format & measurement definitions ↗</a>{manifest.headerSource?.url && <a href={manifest.headerSource.url} target="_blank" rel="noreferrer">NOAA field headers ↗</a>}</div><dl className={styles.hashes}><div><dt>Selected station display snapshot · SHA-256</dt><dd><a href={descriptor.url}>Open verified display file ↗</a><code>{descriptor.sha256}</code></dd></div></dl><div className={styles.tableScroll} role="region" aria-label="Captured annual NOAA sources, horizontally scrollable" tabIndex={0}><table className={styles.sourceTable}><caption>Captured originals for {descriptor.name}. Provider URLs may now serve revised bytes.</caption><thead><tr><th scope="col">Year / source</th><th scope="col">Captured</th><th scope="col">Bytes / SHA-256</th></tr></thead><tbody>{descriptor.sources.map((source) => <tr key={source.year}><th scope="row"><a href={source.url} target="_blank" rel="noreferrer">{source.year} NOAA daily file ↗</a></th><td><time dateTime={source.capturedAt}>{captureLabel(source.capturedAt)}</time>{source.lastModified && <small>Last-Modified: {source.lastModified}</small>}</td><td>{number(source.bytes)} bytes<code>{source.sha256}</code></td></tr>)}</tbody></table></div><p className={styles.integrityNote}>KFM calculated these file hashes; they are not provider-issued signatures. Snapshot bytes and structure are checked before display. This display is provider context with review pending; it does not promote the observations into a governed KFM release.</p></div></details>
      <footer className={styles.footer}><span>Kansas Frontier Matrix · Soil Profile Lab</span><Link href="/science">Explore the science tools ↗</Link></footer>
    </section>
  </div></main>;
}
