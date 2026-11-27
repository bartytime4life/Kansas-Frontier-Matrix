"use client";

import { useEffect, useMemo, useRef, useState, useSyncExternalStore } from "react";
import Link from "next/link";
import ScienceNav from "../../science/science-nav";
import { loadClimateSnapshot } from "./snapshot-loader.mjs";
import { analyseClimate, climateCsv, climateReceipt, readingLabel } from "./climate-model.mjs";
import styles from "./heat-and-rain.module.css";

const MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
const LOCATION_EVENT = "kfm-climate-selection";
const PAGE_SIZE = 14;
const PLOT = { width: 900, height: 330, left: 58, right: 20, top: 22, bottom: 62 };
const number = (value, digits = 0) => Number.isFinite(value) ? value.toLocaleString("en-US", { maximumFractionDigits: digits }) : "—";
const temperature = (value, units) => units === "imperial" ? value * 9 / 5 + 32 : value;
const rain = (value, units) => units === "imperial" ? value / 25.4 : value;
const tempUnit = (units) => units === "imperial" ? "°F" : "°C";
const rainUnit = (units) => units === "imperial" ? "in" : "mm";
const validNumber = (raw, minimum, maximum, fallback, integer = false) => {
  if (raw === null || !/^-?\d+(?:\.\d+)?$/.test(raw)) return fallback;
  const value = Number(raw);
  return Number.isFinite(value) && value >= minimum && value <= maximum && (!integer || Number.isInteger(value)) ? value : fallback;
};

export function climateSelection(manifest, search = "") {
  const query = new URLSearchParams(search);
  const defaultStation = manifest.stations.find((station) => /WICHITA/i.test(station.name)) ?? manifest.stations[0];
  return {
    station: manifest.stations.some((station) => station.id === query.get("station")) ? query.get("station") : defaultStation.id,
    year: validNumber(query.get("year"), 2020, 2025, 2025, true),
    month: validNumber(query.get("month"), 0, 12, 0, true),
    units: query.get("units") === "imperial" ? "imperial" : "metric",
    heat: validNumber(query.get("heat"), -60, 60, 32.2),
    wet: validNumber(query.get("wet"), 0.1, 500, 1),
  };
}

export function climateLink(href, selection) {
  const url = new URL(href);
  url.search = "";
  url.hash = "";
  for (const key of ["station", "year", "month", "units", "heat", "wet"]) url.searchParams.set(key, String(selection[key]));
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

function captureLabel(date) {
  const parsed = new Date(date);
  return Number.isFinite(parsed.getTime()) ? parsed.toISOString().replace("T", " ").replace(/\.\d+Z$/, " UTC") : "Not supplied";
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

function plotDomain(values, minimumSpan = 10) {
  const finite = values.filter(Number.isFinite);
  const low = finite.length ? Math.min(...finite) : 0;
  const high = finite.length ? Math.max(...finite) : minimumSpan;
  const span = Math.max(high - low, minimumSpan);
  const magnitude = 10 ** Math.floor(Math.log10(span / 4));
  const step = [1, 2, 5, 10].map((factor) => factor * magnitude).find((value) => span / value <= 5) ?? magnitude * 10;
  const min = Math.floor(low / step) * step;
  const max = Math.max(min + step, Math.ceil(high / step) * step);
  const ticks = Array.from({ length: Math.round((max - min) / step) + 1 }, (_, index) => min + index * step);
  return { min, max, ticks };
}

export function temperaturePath(days, element, units, x, y) {
  let drawing = false;
  return days.map((day, index) => {
    const value = day[element]?.value;
    if (!Number.isFinite(value)) { drawing = false; return ""; }
    const command = drawing ? "L" : "M";
    drawing = true;
    return `${command}${x(index).toFixed(2)},${y(temperature(value, units)).toFixed(2)}`;
  }).join(" ");
}

export function ClimatePlot({ analysis, units, view, selectedIndex }) {
  const rainy = view === "rain";
  const days = analysis.days;
  const innerWidth = PLOT.width - PLOT.left - PLOT.right;
  const innerHeight = PLOT.height - PLOT.top - PLOT.bottom;
  const bottom = PLOT.height - PLOT.bottom;
  const x = (index) => PLOT.left + (days.length < 2 ? innerWidth / 2 : index / (days.length - 1) * innerWidth);
  const threshold = rainy ? rain(analysis.wetMm, units) : temperature(view === "frost" ? 0 : analysis.heatC, units);
  const observedValues = rainy
    ? days.map((day) => day.prcp.value).filter(Number.isFinite).map((value) => rain(value, units))
    : days.flatMap((day) => [day.tmax.value, day.tmin.value]).filter(Number.isFinite).map((value) => temperature(value, units));
  const domain = plotDomain(rainy ? [0, ...observedValues] : [...observedValues, threshold], rainy ? (units === "imperial" ? 0.5 : 10) : 10);
  const y = (value) => bottom - (value - domain.min) / (domain.max - domain.min) * innerHeight;
  const xTicks = days.reduce((ticks, day, index) => {
    if (analysis.month ? [0, 7, 14, 21, days.length - 1].includes(index) : day.date.endsWith("-01") && ["01", "03", "05", "07", "09", "11"].includes(day.date.slice(5, 7))) ticks.push(index);
    return ticks;
  }, []);
  const current = days[selectedIndex];
  const thresholdVisible = threshold >= domain.min && threshold <= domain.max;
  const unit = rainy ? rainUnit(units) : tempUnit(units);
  const barWidth = Math.max(1.4, Math.min(18, innerWidth / Math.max(days.length, 1) * 0.72));

  return <figure className={styles.plot}>
    <div className={styles.plotHeader}>
      <ul className={styles.legend} aria-label="Chart legend">
        {rainy ? <>
          <li><i className={styles.rainKey} />Quantified precipitation</li>
          <li><i className={styles.zeroKey} />Recorded zero</li>
          <li><span className={styles.traceKey}>○</span>Trace</li>
          <li><span className={styles.gapKey}>×</span>Missing or withheld</li>
        </> : <>
          <li><i className={styles.heatKey} />Daily maximum</li>
          <li><i className={styles.frostKey} />Daily minimum</li>
          <li>Missing readings leave line gaps</li>
        </>}
      </ul>
      <span className={styles.axisUnit}>{rainy ? "Daily precipitation" : "Daily temperature"} · {unit}</span>
    </div>
    <div className={styles.plotScroll} role="region" aria-label="Daily observation chart, scroll horizontally on small screens" tabIndex={0}>
      <svg className={styles.chart} viewBox={`0 0 ${PLOT.width} ${PLOT.height}`} role="img" aria-labelledby="climate-chart-title climate-chart-description">
        <title id="climate-chart-title">{`${rainy ? "Daily precipitation" : "Daily maximum and minimum temperature"} · ${analysis.station.name} · ${analysis.year}`}</title>
        <desc id="climate-chart-description">{days.length} observation dates. {rainy ? "Bars show quantified liquid-equivalent precipitation. Short marks show recorded zero; circles show trace; crosses below the axis show missing or withheld readings." : "Amber shows maximum temperature; blue dashes show minimum temperature. Lines break at missing or withheld observations."} Use the date inspector below for exact readings and flags.</desc>
        {domain.ticks.map((tick) => <g key={tick}>
          <line x1={PLOT.left} x2={PLOT.width - PLOT.right} y1={y(tick)} y2={y(tick)} className={styles.gridLine} />
          <text x={PLOT.left - 12} y={y(tick) + 5} textAnchor="end" className={styles.axisText}>{number(tick, rainy && units === "imperial" ? 2 : 1)}</text>
        </g>)}
        {thresholdVisible && <g>
          <line x1={PLOT.left} x2={PLOT.width - PLOT.right} y1={y(threshold)} y2={y(threshold)} className={styles.thresholdLine} />
          <text x={PLOT.width - PLOT.right - 4} y={y(threshold) - 7} textAnchor="end" className={styles.thresholdLabel}>{view === "frost" ? "Freezing ≤ " : rainy ? "Wet day ≥ " : "Heat ≥ "}{number(threshold, 6)} {unit}</text>
        </g>}
        {!rainy && <>
          <path d={temperaturePath(days, "tmax", units, x, y)} className={styles.maximumLine} />
          <path d={temperaturePath(days, "tmin", units, x, y)} className={styles.minimumLine} />
          {days.length <= 31 && days.flatMap((day, index) => ["tmax", "tmin"].filter((element) => Number.isFinite(day[element].value)).map((element) => <circle key={`${day.date}-${element}`} cx={x(index)} cy={y(temperature(day[element].value, units))} r={2.3} className={element === "tmax" ? styles.maximumPoint : styles.minimumPoint} />))}
        </>}
        {rainy && days.map((day, index) => {
          const reading = day.prcp;
          if (Number.isFinite(reading.value)) return reading.value === 0
            ? <line key={day.date} x1={x(index) - barWidth / 2} x2={x(index) + barWidth / 2} y1={bottom} y2={bottom} className={styles.zeroMark} />
            : <rect key={day.date} x={x(index) - barWidth / 2} y={y(rain(reading.value, units))} width={barWidth} height={Math.max(1, bottom - y(rain(reading.value, units)))} className={styles.rainBar} />;
          if (reading.state === "trace") return <circle key={day.date} cx={x(index)} cy={bottom + 12} r={2.5} className={styles.traceMark} />;
          return <path key={day.date} d={`M${x(index) - 2},${bottom + 10}l4,4m-4,0l4,-4`} className={styles.gapMark} />;
        })}
        {xTicks.map((index) => <text key={index} x={x(index)} y={PLOT.height - 24} textAnchor="middle" className={styles.axisText}>{analysis.month ? Number(days[index].date.slice(8, 10)) : MONTHS[Number(days[index].date.slice(5, 7)) - 1].slice(0, 3)}</text>)}
        {current && <g>
          <line x1={x(selectedIndex)} x2={x(selectedIndex)} y1={PLOT.top} y2={bottom + 16} className={styles.selectedLine} />
          {!rainy && ["tmax", "tmin"].filter((element) => Number.isFinite(current[element].value)).map((element) => <circle key={element} cx={x(selectedIndex)} cy={y(temperature(current[element].value, units))} r={4.5} className={styles.selectedPoint} />)}
        </g>}
        {!observedValues.length && <text x={PLOT.left + innerWidth / 2} y={PLOT.top + innerHeight / 2} textAnchor="middle" className={styles.emptyPlot}>No quantified {rainy ? "precipitation" : "temperature"} readings in this selection</text>}
      </svg>
    </div>
    <figcaption className={styles.plotCaption}>
      <span>{days.length ? `${dateLabel(days[0].date, true)} – ${dateLabel(days.at(-1).date, true)}, ${analysis.year}` : analysis.year} · NOAA observation dates</span>
      <span>{rainy ? "Trace is observed precipitation without a quantified amount." : "Daily extremes are separate observations; the space between lines is not a continuous record."}</span>
    </figcaption>
  </figure>;
}

export function ClimateMetrics({ analysis, units }) {
  const metrics = [
    { label: "Hot days", value: analysis.valid.tmax ? number(analysis.hotDays) : "—", rule: `Maximum ≥ ${number(temperature(analysis.heatC, units), 6)} ${tempUnit(units)}`, support: `${analysis.valid.tmax}/${analysis.expected} days with valid maximum`, tone: "heat" },
    { label: "Days at or below freezing", value: analysis.valid.tmin ? number(analysis.frostDays) : "—", rule: `Minimum ≤ ${number(temperature(0, units))} ${tempUnit(units)}`, support: `${analysis.valid.tmin}/${analysis.expected} days with valid minimum`, tone: "frost" },
    { label: "Wet days", value: analysis.valid.prcp ? number(analysis.wetDays) : "—", rule: `Precipitation ≥ ${number(rain(analysis.wetMm, units), 6)} ${rainUnit(units)}`, support: `${analysis.valid.prcp}/${analysis.expected} days with quantified precipitation`, tone: "rain" },
    { label: "Quantified precipitation", value: analysis.rainMm === null ? "—" : number(rain(analysis.rainMm, units), units === "imperial" ? 2 : 1), unit: rainUnit(units), rule: `${number(analysis.traceDays)} trace ${analysis.traceDays === 1 ? "day" : "days"} · excluded from sum`, support: `${analysis.valid.prcp}/${analysis.expected} days with quantified precipitation`, tone: "rain" },
  ];
  return <dl className={styles.metrics}>
    {metrics.map((metric) => <div key={metric.label} data-tone={metric.tone}>
      <dt>{metric.label}</dt>
      <dd><strong>{metric.value}</strong>{metric.unit && <span className={styles.metricUnit}>{metric.unit}</span>}</dd>
      <span className={styles.metricRule}>{metric.rule}</span>
      <small>{metric.support}</small>
    </div>)}
  </dl>;
}

function ThresholdForm({ selection, onApply }) {
  const initialHeat = String(Number(temperature(selection.heat, selection.units).toFixed(6)));
  const initialWet = String(Number(rain(selection.wet, selection.units).toFixed(6)));
  const [heatInput, setHeatInput] = useState(initialHeat);
  const [wetInput, setWetInput] = useState(initialWet);
  const [error, setError] = useState("");
  const imperial = selection.units === "imperial";
  function apply(event) {
    event.preventDefault();
    const heatValue = Number(heatInput);
    const wetValue = Number(wetInput);
    const heat = heatInput === initialHeat ? selection.heat : imperial ? (heatValue - 32) * 5 / 9 : heatValue;
    const wet = wetInput === initialWet ? selection.wet : imperial ? wetValue * 25.4 : wetValue;
    if (heatInput.trim() === "" || wetInput.trim() === "" || !Number.isFinite(heat) || !Number.isFinite(wet) || heat < -60 || heat > 60 || wet < 0.1 || wet > 500) {
      setError(`Use a heat threshold from ${number(temperature(-60, selection.units), 1)} to ${number(temperature(60, selection.units), 1)} ${tempUnit(selection.units)} and a wet-day threshold from ${number(rain(0.1, selection.units), imperial ? 4 : 1)} to ${number(rain(500, selection.units), imperial ? 4 : 1)} ${rainUnit(selection.units)}.`);
      return;
    }
    setError("");
    onApply({ heat: Number(heat.toFixed(6)), wet: Number(wet.toFixed(6)) });
  }
  return <details className={styles.thresholdDetails}>
    <summary>Adjust the science question <span>Heat and wet-day thresholds</span></summary>
    <form onSubmit={apply} className={styles.thresholdForm}>
      <label>Hot-day maximum ({tempUnit(selection.units)})<input name="heat" type="number" inputMode="decimal" step="any" required value={heatInput} onChange={(event) => setHeatInput(event.target.value)} /></label>
      <label>Wet-day precipitation ({rainUnit(selection.units)})<input name="wet" type="number" inputMode="decimal" step="any" required value={wetInput} onChange={(event) => setWetInput(event.target.value)} /></label>
      <button type="submit">Apply thresholds</button>
      <p>Counts include readings at the threshold. The freezing threshold is a daily minimum at or below {number(temperature(0, selection.units))} {tempUnit(selection.units)}. Analysis thresholds are {number(selection.heat, 6)} °C and {number(selection.wet, 6)} mm; unit conversions in labels may be rounded.</p>
      {error && <p className={styles.errorText} role="alert">{error}</p>}
    </form>
  </details>;
}

function ReadingFlags({ reading }) {
  const flag = (value) => typeof value === "string" && value.trim() ? value.trim() : "—";
  return <small className={styles.flags}>Raw {reading.raw ?? "—"} · M {flag(reading.measurementFlag)} · Q {flag(reading.qualityFlag)} · S {flag(reading.sourceFlag)}</small>;
}

export function ClimateDayInspector({ days, selectedIndex, units, onSelectDate }) {
  const selectedDay = days[selectedIndex];
  if (!selectedDay) return null;
  function selectDate(event) {
    const date = event.currentTarget.value;
    if (days.some((day) => day.date === date)) onSelectDate(date);
  }
  return <div className={styles.inspector}>
    <div className={styles.dateControls}><label htmlFor="climate-day">Inspect an observation day<input id="climate-day" type="date" min={days[0].date} max={days.at(-1).date} value={selectedDay.date} onInput={selectDate} onChange={selectDate} /></label><div className={styles.dayArrows}><button type="button" aria-label="Previous observation day" disabled={selectedIndex === 0} onClick={() => onSelectDate(days[selectedIndex - 1].date)}>←</button><button type="button" aria-label="Next observation day" disabled={selectedIndex === days.length - 1} onClick={() => onSelectDate(days[selectedIndex + 1].date)}>→</button></div></div>
    <div className={styles.dayReadings} aria-live="polite" aria-atomic="true"><span className={styles.inspectedDate}>{dateLabel(selectedDay.date)}</span>{[["tmax", "Daily maximum"], ["tmin", "Daily minimum"], ["prcp", "Daily precipitation"]].map(([element, label]) => <div key={element}><span>{label}</span><strong>{readingLabel(selectedDay[element], element, units)}</strong><ReadingFlags reading={selectedDay[element]} /></div>)}</div>
  </div>;
}

export default function HeatAndRain({ manifest }) {
  const search = useSyncExternalStore(subscribeLocation, locationSearch, serverSearch);
  const selection = useMemo(() => climateSelection(manifest, search), [manifest, search]);
  const descriptor = manifest.stations.find((station) => station.id === selection.station);
  const [result, setResult] = useState(null);
  const [retry, setRetry] = useState(0);
  const requestId = useRef(0);
  const [view, setView] = useState("heat");
  const [selectedDate, setSelectedDate] = useState("");
  const [recordsPage, setRecordsPage] = useState({ key: "", page: 0 });
  const [shareStatus, setShareStatus] = useState("");
  const [shareFallback, setShareFallback] = useState("");
  const [exportError, setExportError] = useState("");
  const shareId = useRef(0);

  useEffect(() => {
    const controller = new AbortController();
    const id = ++requestId.current;
    loadClimateSnapshot(descriptor, { signal: controller.signal }).then((snapshot) => {
      if (!controller.signal.aborted && requestId.current === id) setResult({ stationId: descriptor.id, snapshot, error: "" });
    }).catch((error) => {
      if (!controller.signal.aborted && requestId.current === id) setResult({ stationId: descriptor.id, snapshot: null, error: error instanceof Error ? error.message : "The station snapshot could not be read." });
    });
    return () => controller.abort();
  }, [descriptor, retry]);

  const currentResult = result?.stationId === selection.station ? result : null;
  const snapshot = currentResult?.snapshot ?? null;
  const analysis = useMemo(() => snapshot ? analyseClimate(snapshot, { year: selection.year, month: selection.month, heatC: selection.heat, wetMm: selection.wet }) : null, [snapshot, selection.year, selection.month, selection.heat, selection.wet]);
  const days = analysis?.days ?? [];
  const selectedIndex = Math.max(0, days.findIndex((day) => day.date === selectedDate));
  const analysisKey = `${selection.station}:${selection.year}:${selection.month}`;
  const pageCount = Math.ceil(days.length / PAGE_SIZE);
  const currentPage = recordsPage.key === analysisKey ? Math.min(recordsPage.page, Math.max(0, pageCount - 1)) : 0;
  const pageDays = days.slice(currentPage * PAGE_SIZE, (currentPage + 1) * PAGE_SIZE);
  const loading = !currentResult;
  const periodLabel = `${selection.month ? `${MONTHS[selection.month - 1]} ` : ""}${selection.year}`;

  function updateSelection(patch) {
    const next = { ...selection, ...patch };
    if (next.station !== selection.station) setResult(null);
    shareId.current += 1;
    setShareStatus("");
    setShareFallback("");
    setExportError("");
    window.history.replaceState(window.history.state, "", climateLink(window.location.href, next));
    window.dispatchEvent(new Event(LOCATION_EVENT));
  }

  async function copyLink() {
    const link = climateLink(window.location.href, selection);
    const id = ++shareId.current;
    try {
      if (!navigator.clipboard?.writeText) throw new Error("Clipboard unavailable");
      await navigator.clipboard.writeText(link);
      if (id === shareId.current) { setShareStatus("Analysis link copied."); setShareFallback(""); }
    } catch {
      if (id === shareId.current) { setShareFallback(link); setShareStatus("Select and copy the analysis link below."); }
    }
  }

  function exportAnalysis(kind) {
    if (!analysis || !snapshot || !days.length) return;
    try {
      const filename = `kfm-${selection.station}-${selection.year}${selection.month ? `-${String(selection.month).padStart(2, "0")}` : ""}`;
      if (kind === "csv") downloadText(climateCsv(analysis, selection.units), "text/csv;charset=utf-8", `${filename}.csv`);
      else downloadText(`${JSON.stringify(climateReceipt(analysis, descriptor, selection.units), null, 2)}\n`, "application/json", `${filename}-receipt.json`);
      setExportError("");
    } catch {
      setExportError("This browser could not create the download. Try again or open the original NOAA source below.");
    }
  }

  return <main className={styles.page}>
    <div className={styles.frame}>
      <ScienceNav active="weather" selection={selection} sourceHref="#climate-evidence" sourceLabel="Source & methods ↓" extraLinks={[{ href: "/observatory/sources", label: "Research & sources ↗" }]} />
      <header className={styles.hero}>
        <div><span className={styles.eyebrow}>Kansas field notebook · 01</span><h1>Heat <span>&</span> Rain Lab</h1><p>Turn daily weather observations into useful questions about growing seasons, heat exposure and water.</p></div>
        <div className={styles.scope}><span className={styles.badge}><i />NOAA station snapshots</span><strong>2020–2025</strong><span>{manifest.stations.length} Kansas stations · daily observations</span></div>
      </header>

      <section className={styles.setup} aria-labelledby="climate-setup-heading">
        <div className={styles.sectionHeader}><div><span className={styles.eyebrow}>01 / Choose your observations</span><h2 id="climate-setup-heading">Start with a place and a year.</h2></div><button type="button" className={styles.shareButton} onClick={copyLink}>Copy analysis link ↗</button></div>
        <div className={styles.selects}>
          <label>Weather station<select value={selection.station} onChange={(event) => updateSelection({ station: event.target.value })}>{manifest.stations.map((station) => <option key={station.id} value={station.id}>{station.name}</option>)}</select></label>
          <label>Year<select value={selection.year} onChange={(event) => updateSelection({ year: Number(event.target.value) })}>{[2025, 2024, 2023, 2022, 2021, 2020].map((year) => <option key={year} value={year}>{year}</option>)}</select></label>
          <label>Time window<select value={selection.month} onChange={(event) => updateSelection({ month: Number(event.target.value) })}><option value={0}>Full year</option>{MONTHS.map((month, index) => <option key={month} value={index + 1}>{month}</option>)}</select></label>
          <label>Display units<select value={selection.units} onChange={(event) => updateSelection({ units: event.target.value })}><option value="metric">°C · millimeters</option><option value="imperial">°F · inches</option></select></label>
        </div>
        <p className={styles.shareStatus} role="status">{shareStatus}</p>
        {shareFallback && <label className={styles.shareFallback}>Analysis link<input type="text" value={shareFallback} readOnly onFocus={(event) => event.target.select()} /></label>}
        <ThresholdForm key={`${selection.units}:${selection.heat}:${selection.wet}`} selection={selection} onApply={updateSelection} />
      </section>

      <section className={styles.analysis} aria-labelledby="climate-analysis-heading" aria-busy={loading}>
        <div className={styles.sectionHeader}><div><span className={styles.eyebrow}>02 / Read the season</span><h2 id="climate-analysis-heading">{descriptor.name}<span className={styles.headingPeriod}> / {periodLabel}</span></h2></div><span className={styles.stationId}>{descriptor.id}</span></div>
        {loading && <div className={styles.loadState} role="status"><span className={styles.statusMark}>…</span><div><h3>Reading {descriptor.name} observations</h3><p>Loading and verifying the selected station snapshot.</p></div></div>}
        {currentResult?.error && <div className={styles.loadState} role="alert"><span className={styles.statusMark}>!</span><div><h3>The station snapshot could not be loaded.</h3><p>{currentResult.error}</p><button type="button" onClick={() => { setResult(null); setRetry((value) => value + 1); }}>Retry station snapshot</button></div></div>}
        {analysis && <>
          <ClimateMetrics analysis={analysis} units={selection.units} />
          <p className={styles.coverageNote}>Each count uses the valid observations for its measurement. Precipitation is measured as liquid water and can include melted snow. The sum excludes traces, partial periods, and withheld or missing amounts.</p>
          {!days.length ? <div className={styles.loadState} role="status"><div><h3>No daily records in this selection.</h3><p>Choose another month or year to inspect observations. Empty dates are never filled with estimated weather.</p></div></div> : <>
            <div className={styles.plotIntro}><div><h3>{view === "rain" ? "When did precipitation arrive?" : view === "frost" ? "When did minimum temperatures reach freezing?" : "How did the heat build?"}</h3><p>{view === "rain" ? "Compare quantified amounts, recorded zeroes, traces and missing readings." : "Read the daily extremes, then inspect any observation date below."}</p></div><div className={styles.viewButtons} role="group" aria-label="Observation view">{[["heat", "Heat", "TMAX"], ["frost", "Freezing", "TMIN"], ["rain", "Precipitation", "PRCP"]].map(([value, label, element]) => <button type="button" key={value} aria-pressed={view === value} onClick={() => setView(value)}>{label}<span>{element}</span></button>)}</div></div>
            <ClimatePlot analysis={analysis} units={selection.units} view={view} selectedIndex={selectedIndex} />
            <ClimateDayInspector days={days} selectedIndex={selectedIndex} units={selection.units} onSelectDate={setSelectedDate} />
          </>}

          <section className={styles.monthly} aria-labelledby="climate-monthly-heading"><div className={styles.sectionHeader}><div><h3 id="climate-monthly-heading">The year, month by month.</h3><p>Select a month to focus the plot and headline readings.</p></div>{selection.month !== 0 && <button type="button" onClick={() => updateSelection({ month: 0 })}>Show full year</button>}</div>
            <div className={styles.tableScroll} role="region" aria-label="Monthly climate summary, horizontally scrollable" tabIndex={0}><table className={styles.monthTable}><caption>{descriptor.name} · {selection.year}. Support beneath each value is valid days / expected days for that measurement.</caption><thead><tr><th scope="col">Month</th><th scope="col">Hot days</th><th scope="col">Days at or below freezing</th><th scope="col">Wet days</th><th scope="col">Quantified precipitation ({rainUnit(selection.units)})</th></tr></thead><tbody>{analysis.monthly.map((month) => <tr key={month.month} data-selected={selection.month === month.month}><th scope="row"><button type="button" aria-pressed={selection.month === month.month} onClick={() => updateSelection({ month: month.month })}>{MONTHS[month.month - 1]}<span aria-hidden="true">↗</span></button></th><td>{month.valid.tmax ? number(month.hotDays) : "—"}<small>{month.valid.tmax}/{month.expected} valid</small></td><td>{month.valid.tmin ? number(month.frostDays) : "—"}<small>{month.valid.tmin}/{month.expected} valid</small></td><td>{month.valid.prcp ? number(month.wetDays) : "—"}<small>{month.valid.prcp}/{month.expected} quantified</small></td><td>{month.rainMm === null ? "—" : number(rain(month.rainMm, selection.units), selection.units === "imperial" ? 2 : 1)}<small>{month.valid.prcp}/{month.expected} quantified · {month.traceDays} trace</small></td></tr>)}</tbody></table></div>
          </section>

          <details className={styles.records}><summary>Inspect daily source records<span>{days.length} dates · values and raw flags</span></summary><div className={styles.recordsBody}><p>Raw temperature and precipitation values are NOAA tenths of °C and mm. M is the measurement flag, Q the quality flag and S the source flag; — means no flag. Quality-flagged, unqualified and unresolved readings remain visible and are withheld from analysis.</p><div className={styles.tableScroll} role="region" aria-label="Daily source records, horizontally scrollable" tabIndex={0}><table className={styles.recordsTable}><caption>{descriptor.name} · {periodLabel} · page {pageCount ? currentPage + 1 : 0} of {pageCount}</caption><thead><tr><th scope="col">Observation date</th><th scope="col">Maximum · TMAX</th><th scope="col">Minimum · TMIN</th><th scope="col">Precipitation · PRCP</th></tr></thead><tbody>{pageDays.map((day) => <tr key={day.date}><th scope="row"><time dateTime={day.date}>{day.date}</time></th>{["tmax", "tmin", "prcp"].map((element) => <td key={element} data-state={day[element].state}>{readingLabel(day[element], element, selection.units)}<ReadingFlags reading={day[element]} /></td>)}</tr>)}</tbody></table></div><div className={styles.pagination}><button type="button" disabled={currentPage === 0} onClick={() => setRecordsPage({ key: analysisKey, page: currentPage - 1 })}>← Previous</button><span>{days.length ? `${currentPage * PAGE_SIZE + 1}–${Math.min((currentPage + 1) * PAGE_SIZE, days.length)} of ${days.length} dates` : "No dates"}</span><button type="button" disabled={currentPage + 1 >= pageCount} onClick={() => setRecordsPage({ key: analysisKey, page: currentPage + 1 })}>Next →</button></div></div></details>
        </>}
      </section>

      <section className={styles.evidence} id="climate-evidence" aria-labelledby="climate-evidence-heading">
        <div className={styles.sectionHeader}><div><span className={styles.eyebrow}>03 / Take the evidence with you</span><h2 id="climate-evidence-heading">Useful science keeps its source.</h2></div><span className={styles.evidenceTag}>Provider context</span></div>
        <div className={styles.downloads}><button type="button" disabled={!analysis || !days.length} onClick={() => exportAnalysis("csv")}>Download daily CSV ↓</button><button type="button" disabled={!analysis || !days.length} onClick={() => exportAnalysis("receipt")}>Download analysis receipt ↓</button><a href={descriptor.source.url} target="_blank" rel="noreferrer">Original NOAA source ↗</a></div><p className={styles.downloadNote}>The provider’s source file may update. Your receipt identifies the version captured for this snapshot.</p>
        {exportError && <p className={styles.errorText} role="alert">{exportError}</p>}
        <div className={styles.evidenceGrid}><div><h3>A station record, in its place.</h3><dl className={styles.sourceFacts}><div><dt>Station</dt><dd>{descriptor.name} · {descriptor.id}</dd></div><div><dt>Coordinates</dt><dd>{number(descriptor.latitude, 4)}°, {number(descriptor.longitude, 4)}° · elevation {number(descriptor.elevationM, 1)} m</dd></div><div><dt>Provider</dt><dd>{manifest.provider}</dd></div><div><dt>Source captured</dt><dd><time dateTime={descriptor.source.capturedAt}>{captureLabel(descriptor.source.capturedAt)}</time></dd></div><div><dt>Snapshot scope</dt><dd>{manifest.period.from} through {manifest.period.to}</dd></div></dl></div><div className={styles.limitations}><h3>Read the boundaries.</h3><p>These are observations at individual stations. They are not county averages, gridded estimates, forecasts or a complete picture of conditions between stations.</p><p>Six years support exploration of these observations; they do not establish a climate normal or a climate trend. This snapshot is provider context and has not been admitted as a KFM dataset.</p><p>Dates follow NOAA’s observation-day convention. A reported day may differ from a midnight-to-midnight local calendar day; observation time is not inferred here.</p></div></div>
        <details className={styles.methods}><summary>Measurement rules, flags & file integrity</summary><div className={styles.methodsBody}><p>NOAA stores TMAX and TMIN in tenths of °C and PRCP in tenths of mm. Values shown here are converted to your selected units. A nonblank quality flag withholds a value from analysis. Missing values stay missing. A trace flag means precipitation was observed without a quantified amount, so traces are counted separately.</p><p>Hot days use TMAX at or above your heat threshold. Days at or below freezing use TMIN at or below 0 °C. The daily minimum alone cannot tell when it occurred or whether frost formed. Wet days use quantified PRCP at or above your wet threshold. Each measurement has its own valid-day denominator. Partial PRCP periods flagged A, C or E are visible in source records and excluded from daily totals and counts.</p><p>The CSV carries daily values, raw flags, source hash and analysis settings. The JSON receipt records the selection, settings, coverage and provenance for this analysis.</p><a href={manifest.documentation} target="_blank" rel="noreferrer">Read NOAA’s GHCN-Daily documentation ↗</a><dl className={styles.hashes}><div><dt>Station snapshot SHA-256</dt><dd><code>{descriptor.sha256}</code></dd></div><div><dt>Captured original source SHA-256</dt><dd><code>{descriptor.source.sha256}</code></dd></div></dl><p>These SHA-256 values were calculated for the captured files; they are not provider-issued checksums. The selected snapshot is checked before observations are shown.</p></div></details>
        <footer className={styles.footer}><span>Kansas Frontier Matrix · Science tools</span><Link href="/observatory/sources">Keep exploring the sources ↗</Link></footer>
      </section>
    </div>
  </main>;
}
