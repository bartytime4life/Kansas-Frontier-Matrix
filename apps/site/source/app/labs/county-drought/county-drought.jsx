"use client";

import { useEffect, useMemo, useRef, useState, useSyncExternalStore } from "react";
import Link from "next/link";
import { loadDroughtSnapshot } from "./snapshot-loader.mjs";
import { analyseDrought, droughtCsv, droughtReceipt } from "./drought-model.mjs";
import styles from "./county-drought.module.css";

const LOCATION_EVENT = "kfm-drought-selection";
const YEARS = [2020, 2021, 2022, 2023, 2024, 2025];
const LEVELS = ["", "D1+ · Moderate or worse", "D2+ · Severe or worse", "D3+ · Extreme or worse", "D4 · Exceptional"];
const CATEGORY_LABELS = ["None", "D0 only · Abnormally dry", "D1 only · Moderate", "D2 only · Severe", "D3 only · Extreme", "D4 · Exceptional"];
const PALETTE = ["#d3dbd1", "#ffff00", "#fcd37f", "#ffaa00", "#e60000", "#730000"];
const PLOT = { width: 900, height: 310, left: 54, right: 24, top: 26, bottom: 47 };
const PAGE_SIZE = 25;
const number = (value, digits = 0) => Number.isFinite(value) ? value.toLocaleString("en-US", { maximumFractionDigits: digits }) : "—";
const thresholdText = (value) => Number.isFinite(value) ? String(value) : "—";
const percent = (value) => Number.isFinite(value) ? `${number(value, 2)}%` : "Unavailable";
const severityName = (level) => level === 4 ? "D4" : `D${level}+`;

function boundedNumber(raw, minimum, maximum, fallback, integer = false) {
  if (raw === null || !(integer ? /^\d+$/ : /^\d+(?:\.\d+)?(?:e[+-]?\d+)?$/i).test(raw)) return fallback;
  const value = Number(raw);
  return Number.isFinite(value) && value >= minimum && value <= maximum && (!integer || Number.isInteger(value)) ? value : fallback;
}

export function validDroughtThreshold(value) {
  return Number.isFinite(value) && value >= 0.01 && value <= 100 && value === Math.round(value * 100) / 100;
}

export function droughtSelection(manifest, search = "") {
  const query = new URLSearchParams(search);
  const hasCounty = (id) => manifest.counties.some((county) => county.id === id);
  const countyId = hasCounty(query.get("county")) ? query.get("county") : hasCounty("20055") ? "20055" : manifest.counties[0].id;
  const defaultComparison = manifest.counties.find((county) => county.id === "20161" && county.id !== countyId) ?? manifest.counties.find((county) => county.id !== countyId);
  const compareId = hasCounty(query.get("compare")) && query.get("compare") !== countyId ? query.get("compare") : defaultComparison.id;
  let fromYear = boundedNumber(query.get("from"), 2020, 2025, 2020, true);
  let toYear = boundedNumber(query.get("to"), 2020, 2025, 2025, true);
  if (fromYear > toYear) { fromYear = 2020; toYear = 2025; }
  const proposedThreshold = boundedNumber(query.get("threshold"), 0.01, 100, 50);
  const threshold = validDroughtThreshold(proposedThreshold) ? proposedThreshold : 50;
  return { countyId, compareId, fromYear, toYear, level: boundedNumber(query.get("level"), 1, 4, 2, true), threshold };
}

export function droughtLink(href, selection) {
  const url = new URL(href);
  url.search = "";
  url.hash = "";
  const entries = { county: selection.countyId, compare: selection.compareId, from: selection.fromYear, to: selection.toYear, level: selection.level, threshold: selection.threshold };
  for (const [key, value] of Object.entries(entries)) url.searchParams.set(key, String(value));
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
  if (!date) return "—";
  return new Intl.DateTimeFormat("en-US", { timeZone: "UTC", month: short ? "short" : "long", day: "numeric", year: "numeric" }).format(new Date(`${date}T12:00:00Z`));
}

function captureLabel(date) {
  const parsed = new Date(date);
  return Number.isFinite(parsed.getTime()) ? parsed.toISOString().replace("T", " ").replace(/\.\d+Z$/, " UTC") : "Not supplied";
}

export function droughtRunNote(run) {
  if (!run?.count) return "No observed qualifying run.";
  const boundaries = [run.leftBoundary, run.rightBoundary];
  if (boundaries.includes("window") && boundaries.includes("missing")) return "Window and missing-data boundaries may shorten this observed run.";
  if (boundaries.includes("window")) return "Touches the analysis window; the full episode may extend beyond it.";
  if (boundaries.includes("missing")) return "Missing assessments bound this run; the full episode length is unknown.";
  return "Consecutive observed Tuesday assessments.";
}

function compactRunBoundary(run) {
  const boundaries = [run?.leftBoundary, run?.rightBoundary];
  return boundaries.includes("window") ? "window edge" : boundaries.includes("missing") ? "missing-data edge" : "observed assessments";
}

function downloadText(text, mime, filename) {
  const url = URL.createObjectURL(new Blob([text], { type: mime }));
  const link = document.createElement("a");
  link.href = url;
  link.download = filename;
  document.body.append(link);
  link.click();
  link.remove();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}

export function droughtSharePath(weeks, x, y) {
  let drawing = false;
  return weeks.map((week, index) => {
    if (week.missing || !Number.isFinite(week.share)) { drawing = false; return ""; }
    const command = drawing ? "L" : "M";
    drawing = true;
    return `${command}${x(index).toFixed(2)},${y(week.share).toFixed(2)}`;
  }).join(" ");
}

export function DroughtMetrics({ analysis }) {
  const metrics = [
    { title: "Threshold weeks", value: (county) => county.valid ? `${number(county.thresholdWeeks)}` : "—", unit: "assessments", note: (county) => `${county.valid}/${county.expected} assessments reported` },
    { title: "Longest observed run", value: (county) => county.valid ? `${number(county.longestRun.count)}` : "—", unit: "assessments", note: (county) => !county.valid ? "No reported assessments" : county.longestRun.count ? `${dateLabel(county.longestRun.from, true)} – ${dateLabel(county.longestRun.to, true)}` : "No qualifying run observed" },
    { title: `Peak ${severityName(analysis.settings.level)} area`, value: (county) => Number.isFinite(county.peakShare) ? number(county.peakShare, 2) : "—", unit: "% of county", note: (county) => `${county.valid}/${county.expected} assessments reported` },
    { title: "Mean DSCI", value: (county) => Number.isFinite(county.meanDsci) ? number(county.meanDsci, 1) : "—", unit: "index points · 0–500", note: (county) => `${county.valid}/${county.expected} assessments reported` },
  ];
  return <dl className={styles.metrics}>{metrics.map((metric) => <div key={metric.title}><dt>{metric.title}</dt>{[analysis.primary, analysis.comparison].map((county, index) => <dd key={county.id} data-series={index === 0 ? "primary" : "comparison"}><span className={styles.metricCounty}>{county.name}</span><strong>{metric.value(county)}</strong><span className={styles.metricUnit}>{metric.unit}</span><small>{metric.note(county)}</small></dd>)}</div>)}</dl>;
}

export function DroughtChart({ analysis, selectedIndex }) {
  const weeks = analysis.primary.weeks;
  const innerWidth = PLOT.width - PLOT.left - PLOT.right;
  const bottom = PLOT.height - PLOT.bottom;
  const x = (index) => PLOT.left + (weeks.length < 2 ? innerWidth / 2 : index / (weeks.length - 1) * innerWidth);
  const y = (value) => bottom - value / 100 * (bottom - PLOT.top);
  const ticks = weeks.reduce((entries, week, index) => {
    const newYear = index === 0 || week.date.slice(0, 4) !== weeks[index - 1].date.slice(0, 4);
    const newQuarter = index === 0 || week.date.slice(0, 7) !== weeks[index - 1].date.slice(0, 7) && ["04", "07", "10"].includes(week.date.slice(5, 7));
    if (analysis.settings.fromYear === analysis.settings.toYear ? newQuarter : newYear) entries.push(index);
    return entries;
  }, []);
  const selected = weeks[selectedIndex];
  const stripWidth = weeks.length > 1 ? innerWidth / (weeks.length - 1) : innerWidth;
  return <figure className={styles.plot}>
    <div className={styles.plotHeading}><ul className={styles.seriesLegend} aria-label="County chart legend"><li><i className={styles.primaryKey} />{analysis.primary.name}</li><li><i className={styles.comparisonKey} />{analysis.comparison.name}</li></ul><span>{severityName(analysis.settings.level)} county area · percent</span></div>
    <div className={styles.plotScroll} role="region" aria-label="County drought chart and severity strip, horizontally scrollable together" tabIndex={0}><div className={styles.plotCanvas}>
      <svg className={styles.chart} viewBox={`0 0 ${PLOT.width} ${PLOT.height}`} role="img" aria-labelledby="drought-chart-title drought-chart-description">
        <title id="drought-chart-title">{`${severityName(analysis.settings.level)} county-area share: ${analysis.primary.name} and ${analysis.comparison.name}`}</title>
        <desc id="drought-chart-description">Weekly Tuesday assessments show the percentage of each county in the selected severity or worse. Teal solid line is {analysis.primary.name}; amber dashed line is {analysis.comparison.name}. The horizontal guide is {analysis.settings.threshold} percent. Missing assessments break lines. Choose an assessment below for exact values.</desc>
        {[0, 25, 50, 75, 100].map((tick) => <g key={tick}><line x1={PLOT.left} x2={PLOT.width - PLOT.right} y1={y(tick)} y2={y(tick)} className={styles.gridLine} /><text x={PLOT.left - 12} y={y(tick) + 5} textAnchor="end" className={styles.axisText}>{tick}%</text></g>)}
        <line x1={PLOT.left} x2={PLOT.width - PLOT.right} y1={y(analysis.settings.threshold)} y2={y(analysis.settings.threshold)} className={styles.thresholdLine} />
        <text x={PLOT.width - PLOT.right - 4} y={y(analysis.settings.threshold) - 7} textAnchor="end" className={styles.thresholdLabel}>Threshold ≥ {thresholdText(analysis.settings.threshold)}%</text>
        <path d={droughtSharePath(weeks, x, y)} className={styles.primaryLine} />
        <path d={droughtSharePath(analysis.comparison.weeks, x, y)} className={styles.comparisonLine} />
        {ticks.map((index) => <text key={index} x={x(index)} y={PLOT.height - 17} textAnchor="middle" className={styles.axisText}>{analysis.settings.fromYear === analysis.settings.toYear ? dateLabel(weeks[index].date, true).split(" ")[0] : weeks[index].date.slice(0, 4)}</text>)}
        {selected && <g><line x1={x(selectedIndex)} x2={x(selectedIndex)} y1={PLOT.top} y2={bottom} className={styles.selectedLine} />{[analysis.primary, analysis.comparison].map((county) => Number.isFinite(county.weeks[selectedIndex]?.share) ? <circle key={county.id} cx={x(selectedIndex)} cy={y(county.weeks[selectedIndex].share)} r={4} className={styles.selectedPoint} /> : null)}</g>}
        {!analysis.primary.valid && !analysis.comparison.valid && <text x={PLOT.left + innerWidth / 2} y={y(50)} textAnchor="middle" className={styles.emptyPlot}>No reported assessments in this selection</text>}
      </svg>
    <div className={styles.stripHeading}><h4>{analysis.primary.name} · the full severity mix</h4><span>Exclusive categories · approximately 100% per assessment, with source rounding</span></div>
      <svg className={styles.categoryStrip} viewBox={`0 0 ${PLOT.width} 84`} role="img" aria-labelledby="drought-strip-title drought-strip-description">
        <title id="drought-strip-title">{`Exclusive drought categories in ${analysis.primary.name}`}</title><desc id="drought-strip-description">Each vertical slice is one Tuesday assessment. None and D0-only through D4 are mutually exclusive county-area percentages. Missing assessments are left empty.</desc>
        {weeks.map((week, index) => {
          if (week.missing || !Array.isArray(week.categories)) return <rect key={week.date} x={x(index) - stripWidth / 2} y={7} width={stripWidth} height={44} className={styles.missingStrip} />;
          let cumulative = 0;
          return <g key={week.date}>{week.categories.map((share, category) => {
            const lower = cumulative;
            cumulative += share;
            return <rect key={category} x={x(index) - stripWidth / 2} y={7 + 44 * (100 - lower - share) / 100} width={stripWidth + 0.05} height={44 * share / 100} fill={PALETTE[category]} data-category={category} />;
          })}</g>;
        })}
        {ticks.map((index) => <text key={index} x={x(index)} y={74} textAnchor="middle" className={styles.axisText}>{analysis.settings.fromYear === analysis.settings.toYear ? dateLabel(weeks[index].date, true).split(" ")[0] : weeks[index].date.slice(0, 4)}</text>)}
        {selected && <rect x={x(selectedIndex) - stripWidth / 2} y={5} width={Math.max(2, stripWidth)} height={48} className={styles.stripSelection} />}
      </svg>
    </div></div>
    <ul className={styles.categoryLegend} aria-label="Exclusive category legend">{CATEGORY_LABELS.map((label, index) => <li key={label}><i style={{ background: PALETTE[index] }} />{label}</li>)}</ul>
    <figcaption className={styles.plotCaption}><span>{dateLabel(analysis.period.from, true)} – {dateLabel(analysis.period.to, true)}</span><span>Weekly county-area assessments · missing values are never filled</span></figcaption>
  </figure>;
}

export function DroughtInspector({ analysis, selectedIndex, onSelectDate }) {
  const weeks = analysis.primary.weeks;
  const selected = weeks[selectedIndex];
  if (!selected) return null;
  return <div className={styles.inspector}>
    <div className={styles.assessmentControls}><label htmlFor="drought-assessment">Inspect a Tuesday assessment<select id="drought-assessment" value={selected.date} onChange={(event) => { const date = event.currentTarget.value; if (weeks.some((week) => week.date === date)) onSelectDate(date); }}>{weeks.map((week) => <option key={week.date} value={week.date}>{dateLabel(week.date, true)}</option>)}</select></label><div className={styles.assessmentArrows}><button type="button" aria-label="Previous Tuesday assessment" disabled={selectedIndex === 0} onClick={() => onSelectDate(weeks[selectedIndex - 1].date)}>←</button><button type="button" aria-label="Next Tuesday assessment" disabled={selectedIndex === weeks.length - 1} onClick={() => onSelectDate(weeks[selectedIndex + 1].date)}>→</button></div><p>Each date is a weekly assessment of area, not a count of physical drought days.</p></div>
    <div className={styles.breakdown} aria-live="polite" aria-atomic="true"><table><caption>{dateLabel(selected.date)} · exclusive county-area percentages</caption><thead><tr><th scope="col">Category</th><th scope="col">{analysis.primary.name}</th><th scope="col">{analysis.comparison.name}</th></tr></thead><tbody>{CATEGORY_LABELS.map((label, index) => <tr key={label}><th scope="row"><i style={{ background: PALETTE[index] }} />{label}</th>{[analysis.primary, analysis.comparison].map((county) => <td key={county.id}>{county.weeks[selectedIndex]?.missing ? "Missing" : percent(county.weeks[selectedIndex]?.categories?.[index])}</td>)}</tr>)}<tr className={styles.selectedSeverity}><th scope="row">{severityName(analysis.settings.level)} cumulative area</th>{[analysis.primary, analysis.comparison].map((county) => <td key={county.id}>{county.weeks[selectedIndex]?.missing ? "Missing" : percent(county.weeks[selectedIndex]?.share)}</td>)}</tr><tr><th scope="row">DSCI · 0–500 points</th>{[analysis.primary, analysis.comparison].map((county) => <td key={county.id}>{county.weeks[selectedIndex]?.missing ? "Missing" : number(county.weeks[selectedIndex]?.dsci, 2)}</td>)}</tr></tbody></table></div>
  </div>;
}

function ThresholdForm({ threshold, onApply }) {
  const [draft, setDraft] = useState(String(threshold));
  const [error, setError] = useState("");
  function submit(event) {
    event.preventDefault();
    const value = Number(draft);
    if (!draft.trim() || !validDroughtThreshold(value)) { setError("Enter a county-area threshold from 0.01 to 100%, in 0.01% steps (up to two decimal places)."); return; }
    setError("");
    onApply(value);
  }
  const change = (event) => setDraft(event.currentTarget.value);
  return <form className={styles.thresholdForm} onSubmit={submit} noValidate><label htmlFor="drought-threshold">County area threshold (%)</label><div className={styles.thresholdFields}><input id="drought-threshold" type="number" inputMode="decimal" step="0.01" min="0.01" max="100" required value={draft} onInput={change} onChange={change} aria-invalid={Boolean(error)} aria-describedby={error ? "drought-threshold-error" : "drought-threshold-guidance"} /><button type="submit">Apply</button></div><small id="drought-threshold-guidance" className={styles.thresholdGuidance}>0.01–100%, in 0.01% steps.</small>{error && <p id="drought-threshold-error" className={styles.errorText} role="alert">{error}</p>}</form>;
}

export function DroughtLoadState({ error, onRetry }) {
  return <div className={styles.loadState} role={error ? "alert" : "status"}><span className={styles.statusMark}>{error ? "!" : "…"}</span><div><h3>{error ? "The county assessments could not be loaded." : "Reading Kansas county assessments"}</h3><p>{error || "Loading and verifying the captured U.S. Drought Monitor record."}</p>{error && <button type="button" onClick={onRetry}>Retry drought snapshot</button>}</div></div>;
}

export default function CountyDrought({ manifest }) {
  const search = useSyncExternalStore(subscribeLocation, locationSearch, serverSearch);
  const selection = useMemo(() => droughtSelection(manifest, search), [manifest, search]);
  const [result, setResult] = useState(null);
  const [retry, setRetry] = useState(0);
  const requestId = useRef(0);
  const shareId = useRef(0);
  const [selectedDate, setSelectedDate] = useState("");
  const [rankPage, setRankPage] = useState({ key: "", page: 0 });
  const [shareStatus, setShareStatus] = useState("");
  const [shareFallback, setShareFallback] = useState("");
  const [exportError, setExportError] = useState("");

  useEffect(() => {
    const controller = new AbortController();
    const id = ++requestId.current;
    loadDroughtSnapshot(manifest, { signal: controller.signal }).then((snapshot) => {
      if (!controller.signal.aborted && requestId.current === id) setResult({ snapshot, error: "", snapshotHash: manifest.snapshot.sha256 });
    }).catch((error) => {
      if (!controller.signal.aborted && requestId.current === id) setResult({ snapshot: null, error: error instanceof Error ? error.message : "The drought snapshot could not be read.", snapshotHash: manifest.snapshot.sha256 });
    });
    return () => controller.abort();
  }, [manifest, retry]);

  const currentResult = result?.snapshotHash === manifest.snapshot.sha256 ? result : null;
  const snapshot = currentResult?.snapshot ?? null;
  const analysis = useMemo(() => snapshot ? analyseDrought(snapshot, selection) : null, [snapshot, selection]);
  const primary = manifest.counties.find((county) => county.id === selection.countyId);
  const comparison = manifest.counties.find((county) => county.id === selection.compareId);
  const weeks = analysis?.primary.weeks ?? [];
  const foundWeek = weeks.findIndex((week) => week.date === selectedDate);
  const selectedIndex = foundWeek >= 0 ? foundWeek : weeks.length - 1;
  const rankKey = `${selection.fromYear}:${selection.toYear}:${selection.level}:${selection.threshold}`;
  const pageCount = Math.ceil((analysis?.ranking.length ?? 0) / PAGE_SIZE);
  const currentPage = rankPage.key === rankKey ? Math.min(rankPage.page, Math.max(0, pageCount - 1)) : 0;
  const rankings = analysis?.ranking.slice(currentPage * PAGE_SIZE, (currentPage + 1) * PAGE_SIZE) ?? [];
  const loading = !currentResult;

  function updateSelection(patch) {
    const next = { ...selection, ...patch };
    if (next.countyId === next.compareId) next.compareId = selection.countyId !== next.countyId ? selection.countyId : manifest.counties.find((county) => county.id !== next.countyId).id;
    if (next.fromYear > next.toYear) {
      if (patch.fromYear !== undefined) next.toYear = next.fromYear;
      else next.fromYear = next.toYear;
    }
    shareId.current += 1;
    setShareStatus("");
    setShareFallback("");
    setExportError("");
    window.history.replaceState(window.history.state, "", droughtLink(window.location.href, next));
    window.dispatchEvent(new Event(LOCATION_EVENT));
  }

  async function copyLink() {
    if (!analysis) return;
    const link = droughtLink(window.location.href, selection);
    const id = ++shareId.current;
    try {
      if (!navigator.clipboard?.writeText) throw new Error("Clipboard unavailable");
      await navigator.clipboard.writeText(link);
      if (id === shareId.current) { setShareStatus("Comparison link copied."); setShareFallback(""); }
    } catch {
      if (id === shareId.current) { setShareFallback(link); setShareStatus("Select and copy the comparison link below."); }
    }
  }

  function exportAnalysis(kind) {
    if (!analysis || !snapshot || !analysis.expected) return;
    try {
      const filename = `kfm-drought-${selection.countyId}-${selection.compareId}-${selection.fromYear}-${selection.toYear}`;
      if (kind === "csv") downloadText(droughtCsv(analysis), "text/csv;charset=utf-8", `${filename}.csv`);
      else downloadText(`${JSON.stringify({ ...droughtReceipt(analysis, manifest.snapshot), inspectedDate: weeks[selectedIndex]?.date ?? null }, null, 2)}\n`, "application/json", `${filename}-receipt.json`);
      setExportError("");
    } catch { setExportError("This browser could not create the download. Try again or use the original source files below."); }
  }

  return <main className={styles.page}><div className={styles.frame}>
    <nav className={styles.navigation} aria-label="Science lab navigation"><Link href="/">← KFM Explorer</Link><Link href="/science">Science tools</Link><Link href="/observatory/sources">Research & sources</Link><a href="#drought-evidence">Source & meaning ↓</a></nav>
    <header className={styles.hero}><div><span className={styles.eyebrow}>Kansas field notebook / County Drought Lab</span><h1>How often did drought<br className={styles.heroBreak} /> cover your county?</h1><p>Compare the reach, severity and observed runs of drought, one weekly assessment at a time.</p></div><div className={styles.scope}><span className={styles.badge}><i />U.S. Drought Monitor</span><strong>{manifest.period.from.slice(0, 4)}–{manifest.period.to.slice(0, 4)}</strong><span>{manifest.counties.length} counties · {manifest.snapshot.weeks} Tuesday assessments</span></div></header>

    <section className={styles.setup} aria-labelledby="drought-setup-heading"><div className={styles.sectionHeading}><h2 id="drought-setup-heading">Put two counties side by side.</h2><button type="button" className={styles.shareButton} disabled={!analysis} onClick={copyLink}>Copy comparison link ↗</button></div><div className={styles.controls}>
      <label>Primary county<select value={selection.countyId} onChange={(event) => updateSelection({ countyId: event.currentTarget.value })}>{manifest.counties.map((county) => <option key={county.id} value={county.id}>{county.name}</option>)}</select></label>
      <label>Compare with<select value={selection.compareId} onChange={(event) => updateSelection({ compareId: event.currentTarget.value })}>{manifest.counties.map((county) => <option key={county.id} value={county.id} disabled={county.id === selection.countyId}>{county.name}</option>)}</select></label>
      <label>From<select value={selection.fromYear} onChange={(event) => updateSelection({ fromYear: Number(event.currentTarget.value) })}>{YEARS.map((year) => <option key={year} value={year}>{year}</option>)}</select></label>
      <label>Through<select value={selection.toYear} onChange={(event) => updateSelection({ toYear: Number(event.currentTarget.value) })}>{YEARS.map((year) => <option key={year} value={year}>{year}</option>)}</select></label>
      <label>Severity<select value={selection.level} onChange={(event) => updateSelection({ level: Number(event.currentTarget.value) })}>{LEVELS.slice(1).map((level, index) => <option key={level} value={index + 1}>{level}</option>)}</select></label>
      <ThresholdForm key={selection.threshold} threshold={selection.threshold} onApply={(threshold) => updateSelection({ threshold })} />
    </div><p className={styles.question}>Your question: when did <strong>{severityName(selection.level)}</strong> cover at least <strong>{thresholdText(selection.threshold)}%</strong> of each county’s area?</p><p className={styles.shareStatus} role="status">{shareStatus}</p>{shareFallback && <label className={styles.shareFallback}>Comparison link<input type="text" value={shareFallback} readOnly onFocus={(event) => event.currentTarget.select()} /></label>}</section>

    <section className={styles.analysis} aria-labelledby="drought-analysis-heading" aria-busy={loading}><div className={styles.sectionHeading}><div><span className={styles.eyebrow}>Weekly evidence / {selection.fromYear}–{selection.toYear}</span><h2 id="drought-analysis-heading"><span className={styles.primaryName}>{primary.name}</span><span className={styles.versus}> vs </span><span className={styles.comparisonName}>{comparison.name}</span></h2></div>{analysis && <span className={styles.support}>{analysis.expected} expected assessments</span>}</div>
      {loading && <DroughtLoadState />}{currentResult?.error && <DroughtLoadState error={currentResult.error} onRetry={() => { setResult(null); setRetry((value) => value + 1); }} />}
      {analysis && <><DroughtMetrics analysis={analysis} /><p className={styles.metricNote}>“Weeks” means Tuesday assessments, with reported coverage shown for each county. DSCI combines all drought categories into a 0–500 index; it is separate from your selected severity.</p>
        {[analysis.primary, analysis.comparison].filter((county) => county.longestRun.count && (county.longestRun.leftBoundary || county.longestRun.rightBoundary)).map((county) => <p className={styles.runNotice} key={county.id}><strong>{county.name}:</strong> {droughtRunNote(county.longestRun)}</p>)}
        {!weeks.length ? <div className={styles.emptyState} role="status"><h3>No assessments in this window.</h3><p>Choose another year range. Empty observations are never replaced with drought-free values.</p></div> : <><div className={styles.chartIntro}><h3>Follow drought’s footprint through time.</h3><p>Lines show cumulative {severityName(selection.level)} area. The strip below separates every category without double counting.</p></div><DroughtChart analysis={analysis} selectedIndex={selectedIndex} /><DroughtInspector analysis={analysis} selectedIndex={selectedIndex} onSelectDate={setSelectedDate} /></>}
        <section className={styles.ranking} aria-labelledby="drought-ranking-heading"><div className={styles.sectionHeading}><div><h3 id="drought-ranking-heading">Every county. The same question.</h3><p>{manifest.counties.length} counties ranked by qualifying assessments, then peak area. Select a county to make it your primary comparison.</p></div></div><div className={styles.rankScroll} role="region" aria-label="All Kansas county rankings, horizontally and vertically scrollable" tabIndex={0}><table><caption>{severityName(selection.level)} area ≥ {thresholdText(selection.threshold)}% · {selection.fromYear}–{selection.toYear}</caption><thead><tr><th scope="col">County</th><th scope="col">Threshold weeks</th><th scope="col">Longest run</th><th scope="col">Peak area</th><th scope="col">Mean DSCI</th><th scope="col">Reported coverage</th></tr></thead><tbody>{rankings.map((county, index) => <tr key={county.id} data-selected={county.id === selection.countyId}><th scope="row"><button type="button" aria-pressed={county.id === selection.countyId} onClick={() => updateSelection({ countyId: county.id })}><span className={styles.rankNumber}>{currentPage * PAGE_SIZE + index + 1}</span><span>{county.name}<small>FIPS {county.id}</small></span><span className={styles.rankArrow} aria-hidden="true">↗</span></button></th><td>{county.valid ? number(county.thresholdWeeks) : "—"}<small>assessments</small></td><td>{county.valid ? number(county.longestRun.count) : "—"}<small>{compactRunBoundary(county.longestRun)}</small></td><td>{Number.isFinite(county.peakShare) ? `${number(county.peakShare, 2)}%` : "—"}</td><td>{number(county.meanDsci, 1)}<small>index points</small></td><td>{county.valid}/{county.expected}<small>{county.missing} missing</small></td></tr>)}</tbody></table></div><div className={styles.pagination}><button type="button" disabled={currentPage === 0} onClick={() => setRankPage({ key: rankKey, page: currentPage - 1 })}>← Previous counties</button><span>{analysis.ranking.length ? `${currentPage * PAGE_SIZE + 1}–${Math.min((currentPage + 1) * PAGE_SIZE, analysis.ranking.length)} of ${analysis.ranking.length}` : "No counties"}</span><button type="button" disabled={currentPage + 1 >= pageCount} onClick={() => setRankPage({ key: rankKey, page: currentPage + 1 })}>Next counties →</button></div></section>
      </>}
    </section>

    <section className={styles.evidence} id="drought-evidence" aria-labelledby="drought-evidence-heading"><div className={styles.sectionHeading}><div><span className={styles.eyebrow}>Keep the assessment in context</span><h2 id="drought-evidence-heading">Area, severity and the limits between them.</h2></div><span className={styles.evidenceTag}>Provider context</span></div><div className={styles.meaning}><p><strong>Drought begins at D1.</strong> D0 means abnormally dry. These percentages describe county area; they are not the share of residents affected, a soil-moisture measurement or a count of precise physical drought days.</p><p><strong>Runs follow consecutive observed Tuesday assessments.</strong> Missing weeks break runs. A run touching your analysis window may continue beyond it. Six years do not establish a climate normal or a causal explanation.</p></div>
      <div className={styles.downloads}><button type="button" disabled={!analysis || !analysis.expected} onClick={() => exportAnalysis("csv")}>Download comparison CSV ↓</button><button type="button" disabled={!analysis || !analysis.expected} onClick={() => exportAnalysis("receipt")}>Download analysis receipt ↓</button></div>{exportError && <p className={styles.errorText} role="alert">{exportError}</p>}
      <details className={styles.sourceDetails}><summary>Source files, assessment rules & integrity</summary><div className={styles.sourceBody}><p className={styles.attribution}>{manifest.attribution}</p><div className={styles.sourceLinks}><a href={manifest.documentation} target="_blank" rel="noreferrer">Official data documentation ↗</a><a href={manifest.permission} target="_blank" rel="noreferrer">Permission & attribution ↗</a><a href={manifest.snapshot.url} download>Captured Kansas snapshot ↓</a></div><p>Cumulative D1+/D2+/D3+ shares include every more severe category. The stacked strip uses the mutually exclusive categories None, D0 only, D1 only, D2 only, D3 only and D4. No cumulative shares are stacked together.</p><p>Threshold comparisons include values at the threshold. Every county keeps its own reported/expected assessment count; missing values are never filled. The mean DSCI averages reported index values, in points on a 0–500 scale.</p><dl className={styles.snapshotFacts}><div><dt>Captured coverage</dt><dd>{manifest.counties.length} counties · {number(manifest.snapshot.weeks)} assessment dates · {number(manifest.snapshot.records)} county-assessment records</dd></div><div><dt>Snapshot prepared</dt><dd><time dateTime={manifest.generatedAt}>{captureLabel(manifest.generatedAt)}</time></dd></div><div><dt>Display snapshot SHA-256</dt><dd><code>{manifest.snapshot.sha256}</code></dd></div></dl><h3>Original annual provider files</h3><p>The provider endpoints may update; captured hashes identify the exact source bytes used here.</p><ul className={styles.sourceFiles}>{manifest.sources.map((source) => <li key={source.year}><a href={source.url} target="_blank" rel="noreferrer">{source.year} county-area CSV ↗</a><small>Captured {captureLabel(source.capturedAt)} · {number(source.bytes)} bytes</small><code>{source.sha256}</code></li>)}</ul><p>SHA-256 values are integrity checks computed for captured files, not provider signatures. This is a source-attributed exploration view; KFM dataset admission and scientific release review remain pending.</p></div></details><footer className={styles.footer}><span>Kansas Frontier Matrix · County Drought Lab</span><Link href="/science">Explore another science question ↗</Link></footer>
    </section>
  </div></main>;
}
