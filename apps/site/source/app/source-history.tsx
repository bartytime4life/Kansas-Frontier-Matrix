"use client";
import type { EarthEngineDataset } from "./earth-engine-data";
import { earthEngineSetYear, type EarthEngineContextManifest } from "./earth-engine-context";
import styles from "./source-history.module.css";

export function SourceHistory({ dataset, manifests, loading, error, chooseYear }: { dataset: EarthEngineDataset; manifests: readonly EarthEngineContextManifest[]; loading: boolean; error: string | null; chooseYear(year: number): void }) {
  const years = dataset.temporalMode === "annual" ? Array.from({length: dataset.lastYear! - dataset.firstYear! + 1}, (_, i) => dataset.firstYear! + i) : [];
  const entries = manifests.flatMap((manifest) => manifest.layers.filter((layer) => layer.id === dataset.id).map((layer) => ({ manifest, layer, year: earthEngineSetYear(manifest) })));
  const approved = new Set(entries.filter(({layer}) => layer.status === "approved").map(({year}) => year));
  const held = new Set(entries.filter(({layer}) => layer.status === "held").map(({year}) => year));
  return <section className={styles.panel} aria-label={dataset.title + " coverage history"}>
    <h3>Source history & installed periods</h3>
    <p>{dataset.coverage}. This is catalog scope; usable Kansas scenes and gaps must be enumerated before a transfer.</p>
    {loading ? <p role="status">Checking installed display periods…</p> : error ? <p role="status">{error} Installed coverage is unknown.</p> : <p>{entries.filter(({layer}) => layer.status === "approved").length} approved display periods installed. {held.size ? held.size + " period(s) held for review." : ""} Other recipe years have no approved frame here.</p>}
    {years.length > 0 && <><div className={styles.key}><span>● Approved display</span><span>◐ Held display</span><span>○ Recipe only / availability unverified</span></div><div className={styles.years} role="group" aria-label="Choose a recipe year">{years.map((year) => <button key={year} type="button" data-state={!loading && !error && approved.has(year) ? "approved" : "unavailable"} onClick={() => chooseYear(year)} aria-label={year + ": " + (loading || error ? "installed state unknown" : approved.has(year) ? "approved display installed" : held.has(year) ? "display held" : "recipe only, no approved display") + "; select recipe year"}>{!loading && !error && approved.has(year) ? "●" : !loading && !error && held.has(year) ? "◐" : "○"} {year}</button>)}</div></>}
    {!!entries.length && <details><summary>Installed source dates and review details</summary>{entries.map(({manifest, layer}) => <div key={manifest.setId}><strong>{layer.period} · {layer.status}</strong><p>Reviewed {manifest.approvedAt}<br />{layer.source} · {layer.resolutionMeters} m</p><p>{layer.limits}</p></div>)}</details>}
    <p className={styles.note}>Missing years are never filled with another year. Annual imagery combines scene dates; a review date is not an acquisition date. MSS, TM, ETM+, OLI and OLI-2 remain separate products. Quantitative change requires scientific validation.</p>
  </section>;
}
