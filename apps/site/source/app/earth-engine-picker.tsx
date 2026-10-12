"use client";
import Link from "next/link";
import { useEffect, useRef, useState } from "react";
import { EARTH_ENGINE_DATASETS, buildEarthEngineRecipe, earthEngineUrl, findEarthEngineDatasets } from "./earth-engine-data";
import EarthEngineDownloads from "./earth-engine-downloads";
import type { useLocalDownloads } from "./use-local-downloads";
import s from "./downloads/workspace.module.css";
import p from "./public-map-browser.module.css";

const topics = ["All", ...new Set(EARTH_ENGINE_DATASETS.map(dataset => dataset.topic))];
export default function EarthEnginePicker({ downloads, blockedByOtherDownload, onViewActivity }: { downloads: ReturnType<typeof useLocalDownloads>; blockedByOtherDownload: boolean; onViewActivity: () => void }) {
  const [query, setQuery] = useState(""), [topic, setTopic] = useState("All"), [selectedId, setSelectedId] = useState("");
  const [yearText, setYearText] = useState("");
  const heading = useRef<HTMLHeadingElement>(null), focusSelection = useRef(false), focusReturn = useRef(false), resultsHeading = useRef<HTMLHeadingElement>(null);
  const selected = EARTH_ENGINE_DATASETS.find(dataset => dataset.id === selectedId);
  const visible = findEarthEngineDatasets(query, topic), annual = selected?.temporalMode === "annual", year = annual ? Number(yearText) : undefined;
  let error = "";
  if (selected) { try { buildEarthEngineRecipe(selected.id, year); } catch (cause) { error = cause instanceof Error ? cause.message : "Choose a supported year."; } }
  useEffect(() => { if (focusReturn.current) { focusReturn.current = false; resultsHeading.current?.focus({ preventScroll: true }); if (window.matchMedia("(max-width: 760px)").matches) resultsHeading.current?.scrollIntoView({ block: "start" }); } if (!focusSelection.current) return; focusSelection.current = false; heading.current?.focus({ preventScroll: true }); if (window.matchMedia("(max-width: 760px)").matches) heading.current?.scrollIntoView({ block: "start", behavior: window.matchMedia("(prefers-reduced-motion: reduce)").matches ? "instant" : "smooth" }); }, [selectedId]);
  return <section aria-labelledby="satellite-heading" className={s.satellite}><header className={p.catalogHeading}><div><h2 id="satellite-heading" ref={resultsHeading} tabIndex={-1}>Satellite &amp; climate</h2><p>Choose a Kansas product and period, then set your download maximum.</p></div><span className={p.catalogCount}>{EARTH_ENGINE_DATASETS.length}<small>curated datasets</small></span></header>
    <div className={p.searchRow}><label>Search datasets<input type="search" placeholder="Landsat, rainfall, land cover…" value={query} onChange={event => setQuery(event.target.value)} /></label><label>Topic<select value={topic} onChange={event => setTopic(event.target.value)}>{topics.map(value => <option key={value}>{value}</option>)}</select></label></div>
    <div className={p.filterBar}><span>{visible.length} matching datasets</span>{(query || topic !== "All") && <button type="button" className={s.textButton} onClick={() => { setQuery(""); setTopic("All"); }}>Clear filters</button>}</div>
    <div className={p.results} data-selection={Boolean(selected)}><div className={p.resultColumn}><ul className={p.records}>{visible.map(dataset => <li key={dataset.id}><button type="button" aria-pressed={dataset.id === selectedId} onClick={() => { setSelectedId(dataset.id); setYearText(String(dataset.lastYear ?? "")); focusSelection.current = true; }}><span className={p.recordMeta}>{dataset.topic}<span>{dataset.resolution}</span></span><strong>{dataset.title}</strong><small>{dataset.provider}</small><span className={p.fileHint}>{dataset.firstYear ? `${dataset.firstYear}–${dataset.lastYear}` : "Fixed / mixed dates"}<span aria-hidden="true">↗</span></span></button></li>)}</ul>{!visible.length && <div className={s.empty}><strong>No matching datasets</strong><p>Try another source or topic.</p><button type="button" onClick={() => { setQuery(""); setTopic("All"); }}>Reset search</button></div>}</div>
      <aside className={`${p.detail} ${s.eeDetail}`} aria-label="Selected satellite dataset">{!selected ? <div className={p.selectionEmpty}><span className={p.detailMark} aria-hidden="true">↗</span><h3>Select a dataset</h3><p>Explore available years and capture a source-labelled Kansas product.</p><small>Google sign-in is only needed to start an Earth Engine capture.</small></div> : <>
        <button type="button" className={s.textButton} onClick={() => { focusReturn.current = true; setSelectedId(""); }}>← Back to datasets</button><p className={s.eyebrow}>{selected.topic} · {selected.provider}</p><h3 ref={heading} tabIndex={-1}>{selected.title}</h3><p>{selected.use}</p>
        {annual ? <label className={s.yearField}>Analysis year<input type="number" min={selected.firstYear!} max={selected.lastYear!} value={yearText} aria-invalid={Boolean(error)} aria-describedby="compact-year-error" onChange={event => setYearText(event.target.value)} /><small>{selected.firstYear}–{selected.lastYear} supported recipe years; actual source availability is checked at capture.</small></label> : <p>Fixed product · {selected.coverage}</p>}
        {error && <p id="compact-year-error" className={s.alert} role="alert">{error}</p>}
        <EarthEngineDownloads dataset={selected} year={year} invalid={Boolean(error)} downloads={downloads} blockedByOtherDownload={blockedByOtherDownload} onViewActivity={onViewActivity} compact />
        <details className={p.metadata}><summary>Source details &amp; advanced recipes</summary><dl><div><dt>Coverage</dt><dd>{selected.coverage}</dd></div><div><dt>Resolution</dt><dd>{selected.resolution}</dd></div><div><dt>Timing</dt><dd>{selected.cadence}</dd></div><div><dt>Interpretation</dt><dd>{selected.limitation}</dd></div><div><dt>Reuse terms</dt><dd>{selected.terms}</dd></div></dl><div className={p.actions}><a href={earthEngineUrl(selected)} target="_blank" rel="noreferrer">Provider catalog ↗</a><Link href={`/earth-engine?dataset=${encodeURIComponent(selected.id)}${annual && !error ? `&year=${year}` : ""}`}>Recipes, source history &amp; comparison →</Link></div></details>
      </>}</aside>
    </div>
  </section>;
}
