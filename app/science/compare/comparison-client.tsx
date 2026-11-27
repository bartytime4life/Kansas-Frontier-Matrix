"use client";

import { useEffect, useMemo, useState, useSyncExternalStore, type ReactNode } from "react";
import Link from "next/link";
import ScienceNav from "../science-nav";
import { buildScienceComparison } from "./comparison-model.mjs";
import { comparisonCsv, comparisonExportFilename, comparisonJson } from "./comparison-report.mjs";
import { comparisonLabPath, comparisonPath, comparisonSelection, comparisonYears } from "./comparison-selection.mjs";
import { loadComparisonInputs } from "./comparison-snapshots";
import ComparisonView from "./comparison-view";
import styles from "./comparison.module.css";

const LOCATION_EVENT = "kfm-science-comparison-selection";

function subscribeLocation(callback: () => void) {
  window.addEventListener("popstate", callback);
  window.addEventListener(LOCATION_EVENT, callback);
  return () => {
    window.removeEventListener("popstate", callback);
    window.removeEventListener(LOCATION_EVENT, callback);
  };
}

const clientSearch = () => window.location.search;
const serverSearch = () => "";

type InputState = { attempt: number; inputs: Awaited<ReturnType<typeof loadComparisonInputs>> | null };
const detailedLabs = [
  ["climate", "Heat & Rain Lab"], ["drought", "County Drought Lab"],
  ["air", "Daily Air Quality Lab"], ["sunlight", "Sunlight & Sky Lab"],
];

function downloadText(value: string, type: string, filename: string) {
  const url = URL.createObjectURL(new Blob([value], { type }));
  const link = document.createElement("a");
  link.href = url;
  link.download = filename;
  try {
    document.body.appendChild(link);
    link.click();
  } finally {
    link.remove();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
  }
}

export default function ScienceComparison({ children }: { children?: ReactNode } = {}) {
  const search = useSyncExternalStore(subscribeLocation, clientSearch, serverSearch);
  const { year, compareYear } = comparisonSelection(search);
  const [attempt, setAttempt] = useState(0);
  const [result, setResult] = useState<InputState | null>(null);
  const [feedback, setFeedback] = useState<{ path: string; message: string; link?: string } | null>(null);
  const path = comparisonPath({ year, compareYear });
  const inputs = result?.attempt === attempt ? result.inputs : undefined;

  useEffect(() => {
    const controller = new AbortController();
    loadComparisonInputs(controller.signal).then(loaded => {
      if (!controller.signal.aborted) setResult({ attempt, inputs: loaded });
    }).catch(() => {
      if (controller.signal.aborted) return;
      controller.abort();
      setResult({ attempt, inputs: null });
    });
    return () => controller.abort();
  }, [attempt]);

  const report = useMemo(() => {
    if (!inputs) return null;
    try {
      return buildScienceComparison(inputs.snapshots, { year, compareYear }, inputs.evidence);
    } catch {
      return null;
    }
  }, [inputs, year, compareYear]);
  const failed = inputs !== undefined && !report;
  const message = feedback?.path === path ? feedback : null;

  function setYears(nextYear: number, otherYear: number) {
    const nextPath = comparisonPath({ year: nextYear, compareYear: otherYear });
    if (nextPath === path) return;
    window.history.pushState(null, "", nextPath);
    window.dispatchEvent(new Event(LOCATION_EVENT));
    setFeedback(null);
  }

  async function copyLink() {
    const link = new URL(path, window.location.origin).href;
    try {
      await navigator.clipboard.writeText(link);
      setFeedback({ path, message: "Comparison link copied." });
    } catch {
      setFeedback({ path, message: "Select the comparison link to copy it.", link });
    }
  }

  function exportReport(format: "csv" | "json") {
    if (!report) return;
    try {
      if (format === "csv") downloadText(comparisonCsv(report), "text/csv;charset=utf-8", comparisonExportFilename(report, format));
      else downloadText(comparisonJson(report), "application/json", comparisonExportFilename(report, format));
      setFeedback({ path, message: `${format.toUpperCase()} comparison prepared.` });
    } catch {
      setFeedback({ path, message: "This browser could not prepare the download. Try again or print the report." });
    }
  }

  return <>
    <ScienceNav active="comparison" selection={{ year, compareYear }} sourceHref="#comparison-interpretation" sourceLabel="Reading the sources ↓" />
    {children}
    <section className={styles.controls} aria-label="Comparison settings">
      <label className={styles.control}>Reference year<select value={year} onChange={event => {
        const next = Number(event.target.value);
        setYears(next, next === compareYear ? year : compareYear);
      }}>{comparisonYears.map(option => <option key={option}>{option}</option>)}</select></label>
      <label className={styles.control}>Compare with<select value={compareYear} onChange={event => {
        const next = Number(event.target.value);
        setYears(next === year ? compareYear : year, next);
      }}>{comparisonYears.map(option => <option key={option}>{option}</option>)}</select></label>
      <div className={styles.actions}>
        <button type="button" onClick={copyLink}>Copy comparison link</button>
        <button type="button" disabled={!report} onClick={() => exportReport("csv")}>Download CSV</button>
        <button type="button" disabled={!report} onClick={() => exportReport("json")}>Download JSON</button>
        <button type="button" disabled={!report} onClick={() => window.print()}>Print report</button>
      </div>
      {message && <div className={styles.status}><p role="status">{message.message}</p>{message.link &&
        <label className={styles.control}>Comparison link<input readOnly value={message.link} onFocus={event => event.currentTarget.select()} /></label>}</div>}
    </section>
    {inputs === undefined && <p className={styles.status} role="status">Checking four public science snapshots…</p>}
    <div aria-busy={inputs === undefined}>
      {failed && <div className={styles.status} role="alert"><p>The comparison could not verify all four snapshots. You can retry or open an individual lab below.</p><button type="button" onClick={() => setAttempt(value => value + 1)}>Retry comparison</button></div>}
      {report && <ComparisonView report={report} />}
    </div>
    <section className={styles.reading} aria-labelledby="comparison-interpretation">
      <h2 id="comparison-interpretation">Read the results</h2>
      <ul>
        <li>Check coverage beside each value. A precipitation total can omit days without a quantified reading. A peak describes the readings that were reported.</li>
        <li>Compare one metric at a time. The station, county, and modeled grid represent different areas and observation clocks. A shared month suggests a question to investigate.</li>
        <li>Open a detailed lab to inspect dates, flags, and original records for {year}.</li>
      </ul>
      <ul>
        {detailedLabs.map(([metric, title]) => {
          const href = comparisonLabPath(metric, year);
          return href && <li key={metric}><Link href={href}>{title}</Link></li>;
        })}
      </ul>
    </section>
  </>;
}
