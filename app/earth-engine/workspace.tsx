"use client";

import Link from "next/link";
import { useState } from "react";
import { EARTH_ENGINE_ACCESS, EARTH_ENGINE_CATALOG, EARTH_ENGINE_CHECKED_AT, EARTH_ENGINE_DATASETS, buildEarthEngineRecipe, earthEngineReviewPacket, earthEngineUrl, findEarthEngineDatasets } from "../earth-engine-data";
import { EARTH_ENGINE_CONTEXT_LAYERS, type EarthEngineContextLayerId } from "../earth-engine-context";
import { useEarthEngineContext } from "../earth-engine-context-client";
import { buildEarthEngineExportRecipe } from "../earth-engine-export";
import styles from "./workspace.module.css";

const topics = ["All", ...new Set(EARTH_ENGINE_DATASETS.map((d) => d.topic))];

function download(text: string, name: string, type: string) {
  const url = URL.createObjectURL(new Blob([text], { type }));
  const anchor = document.createElement("a");
  anchor.href = url; anchor.download = name; document.body.append(anchor); anchor.click(); anchor.remove();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}

export default function EarthEngineWorkspace() {
  const context = useEarthEngineContext();
  const [query, setQuery] = useState("");
  const [topic, setTopic] = useState("All");
  const [selectedId, setSelectedId] = useState(EARTH_ENGINE_DATASETS[0].id);
  const [yearText, setYearText] = useState("2024");
  const [compared, setCompared] = useState<string[]>([]);
  const [notice, setNotice] = useState("");
  const selected = EARTH_ENGINE_DATASETS.find((d) => d.id === selectedId)!;
  const visible = findEarthEngineDatasets(query, topic);
  const annual = selected.temporalMode === "annual";
  const year = annual ? Number(yearText) : undefined;
  let recipe = "";
  let error = "";
  try { recipe = buildEarthEngineRecipe(selected.id, year); } catch (cause) { error = cause instanceof Error ? cause.message : "Check the selected recipe."; }
  const comparison = EARTH_ENGINE_DATASETS.filter((d) => compared.includes(d.id));
  const exportable = EARTH_ENGINE_CONTEXT_LAYERS.some((layer) => layer.id === selected.id) && (!annual || year === 2024);

  function choose(id: string) {
    const dataset = EARTH_ENGINE_DATASETS.find((d) => d.id === id)!;
    setSelectedId(id); setYearText(String(dataset.lastYear ?? 2024)); setNotice("");
  }
  function compare(id: string) {
    if (compared.includes(id)) setCompared(compared.filter((current) => current !== id));
    else if (compared.length < 3) setCompared([...compared, id]);
  }
  async function copyRecipe() {
    try { await navigator.clipboard.writeText(recipe); setNotice("Recipe copied. Paste it into the Earth Engine Code Editor and review it before running."); }
    catch { setNotice("Clipboard unavailable. Download the recipe or select the script text below."); }
  }
  function save(kind: "recipe" | "review") {
    try {
      const suffix = annual ? `-${year}` : "-fixed-product";
      download(kind === "recipe" ? recipe : JSON.stringify(earthEngineReviewPacket(selected.id, year), null, 2), `kfm-${selected.id}${suffix}.${kind === "recipe" ? "js" : "json"}`, kind === "recipe" ? "text/javascript" : "application/json");
      setNotice(kind === "recipe" ? "Recipe download prepared. It has not been run." : "Review draft download prepared. It contains metadata and unresolved checks, not imagery or admitted data.");
    } catch { setNotice("Download unavailable. Copy the recipe or try again."); }
  }
  function saveExport(scope: "sample" | "statewide") {
    try {
      const script = buildEarthEngineExportRecipe(selected.id as EarthEngineContextLayerId, scope);
      download(script, `kfm-${selected.id}-${scope}-drive-export.js`, "text/javascript");
      setNotice(`${scope === "sample" ? "Small-area" : "Statewide"} Drive export recipe prepared. It has not been run; check source counts and review the output before approval.`);
    } catch { setNotice("This dataset or year is outside the reviewed 2024 display set."); }
  }

  return <main className={styles.page}>
    <header className={styles.header}>
      <Link href="/" className={styles.brand}>KFM <span>Kansas Frontier Matrix</span></Link>
      <nav aria-label="Earth Engine navigation"><Link href="/">Explorer map</Link><Link href="/earth-engine" aria-current="page">Earth Engine</Link><Link href="/data">Contribute data</Link></nav>
    </header>
    <section className={styles.intro} aria-labelledby="earth-engine-title">
      <div><p className={styles.eyebrow}>KANSAS / SOURCE DISCOVERY</p><h1 id="earth-engine-title">Earth Engine datasets & recipes</h1><p>Find a dataset, compare its limits, and prepare a Kansas analysis for review.</p></div>
      <div className={styles.access}><strong>{context.manifest ? "Processed snapshots available · live Earth Engine disconnected" : "Discovery available · Earth Engine not connected"}</strong><p>{context.manifest ? "Reviewed visual snapshots are available in the map layer controls. They are not KFM claim evidence." : "Recipes run in the owner's registered Earth Engine project. No reviewed Earth Engine display set is installed in this Site."}</p><a href={EARTH_ENGINE_ACCESS} target="_blank" rel="noreferrer">Earth Engine access guide ↗</a></div>
    </section>
    <div className={styles.layout}>
      <section aria-label="Earth Engine dataset discovery" className={styles.discovery}>
        <div className={styles.filters}>
          <label>Find datasets<input type="search" placeholder="Crops, water, Landsat, drought…" value={query} onChange={(event) => setQuery(event.target.value)} /></label>
          <label>Topic<select value={topic} onChange={(event) => setTopic(event.target.value)}>{topics.map((value) => <option key={value}>{value}</option>)}</select></label>
        </div>
        <div className={styles.resultCount}><span role="status">{visible.length} of {EARTH_ENGINE_DATASETS.length} datasets</span><span>Catalog checked <time dateTime={EARTH_ENGINE_CHECKED_AT}>{EARTH_ENGINE_CHECKED_AT}</time></span></div>
        <div className={styles.cards}>{visible.map((dataset) => <article key={dataset.id} className={styles.card} data-selected={selectedId === dataset.id}>
          <div className={styles.cardHeading}><span>{dataset.topic}</span><span>{dataset.resolution}</span></div>
          <h2><button type="button" aria-pressed={selectedId === dataset.id} onClick={() => choose(dataset.id)}>{dataset.title}</button></h2>
          <p className={styles.provider}>{dataset.provider}</p><p>{dataset.use}</p>
          <dl><div><dt>Coverage</dt><dd>{dataset.coverage}</dd></div><div><dt>Timing</dt><dd>{dataset.cadence}</dd></div></dl>
          <div className={styles.cardActions}><button type="button" onClick={() => { choose(dataset.id); document.getElementById("recipe-workspace")?.scrollIntoView({ behavior: "smooth", block: "start" }); }}>{selectedId === dataset.id ? "View selected recipe" : "View recipe"}</button><label><input type="checkbox" checked={compared.includes(dataset.id)} disabled={compared.length === 3 && !compared.includes(dataset.id)} onChange={() => compare(dataset.id)} />Compare<span className={styles.srOnly}> {dataset.title}</span></label></div>
        </article>)}</div>
        {!visible.length && <div className={styles.empty}><h2>No matching datasets</h2><p>Try a provider, topic, or asset ID.</p><button type="button" onClick={() => { setQuery(""); setTopic("All"); }}>Clear filters</button></div>}
        <p className={styles.footnote}>Curated discovery records, not the complete Earth Engine catalog. Catalog coverage does not guarantee usable pixels for a place or year. <a href={EARTH_ENGINE_CATALOG} target="_blank" rel="noreferrer">Browse the full catalog ↗</a></p>
        <section className={styles.comparison} aria-label="Dataset comparison">
          <div className={styles.sectionHeading}><h2>Compare datasets <span>{comparison.length}/3</span></h2>{comparison.length > 0 && <button type="button" onClick={() => setCompared([])}>Clear comparison</button>}</div>
          {!comparison.length ? <p>Select Compare on up to three datasets to see their coverage, resolution and reuse terms side by side.</p> : <div className={styles.tableScroll} tabIndex={0} role="region" aria-label="Scrollable dataset comparison"><table><caption>Metadata comparison only; no measurements or raster differences are computed.</caption><thead><tr><th scope="col">Property</th>{comparison.map((d) => <th scope="col" key={d.id}>{d.title}<button type="button" className={styles.remove} aria-label={`Remove ${d.title} from comparison`} onClick={() => compare(d.id)}>Remove</button></th>)}</tr></thead><tbody>{([['Resolution', 'resolution'], ['Coverage', 'coverage'], ['Timing', 'cadence'], ['Reuse terms', 'terms'], ['Limits', 'limitation']] as const).map(([label, key]) => <tr key={key}><th scope="row">{label}</th>{comparison.map((d) => <td key={d.id}>{d[key]}</td>)}</tr>)}</tbody></table></div>}
        </section>
      </section>
      <aside className={styles.recipe} id="recipe-workspace" aria-labelledby="recipe-title">
        <p className={styles.eyebrow}>PREPARE A KANSAS STUDY</p><h2 id="recipe-title">{selected.title}</h2><code className={styles.asset}>{selected.asset}</code>
        <p>{selected.recipe}</p>
        <dl className={styles.details}><div><dt>Area</dt><dd>Kansas · Census TIGER 2018 state boundary (FIPS 20)</dd></div><div><dt>Time</dt><dd>{selected.coverage}</dd></div><div><dt>Reuse</dt><dd>{selected.terms} <a href={`${earthEngineUrl(selected)}#terms-of-use`} target="_blank" rel="noreferrer">Read terms ↗</a></dd></div></dl>
        {annual ? <label className={styles.year}>Analysis year<input type="number" min={selected.firstYear!} max={selected.lastYear!} step="1" value={yearText} aria-invalid={Boolean(error)} aria-describedby="recipe-time-note recipe-error" onChange={(event) => { setYearText(event.target.value); setNotice(""); }} /><small id="recipe-time-note">Complete calendar years {selected.firstYear}–{selected.lastYear}. End date is January 1 of the following year, exclusive. Actual data availability is checked when run.</small></label> : <p className={styles.fixed}>Fixed product: year selection is unavailable. {selected.temporalMode === "period-summary" ? "The recipe shows the full historical summary." : "The recipe uses a source mosaic with mixed acquisition dates."}</p>}
        <p id="recipe-error" className={styles.error} role="alert">{error}</p>
        <div className={styles.limit}><strong>Interpret with care</strong><p>{selected.limitation}</p></div>
        <div className={styles.recipeActions}><button type="button" className={styles.primary} disabled={Boolean(error)} onClick={() => save("recipe")}>Download recipe · .js</button><button type="button" disabled={Boolean(error)} onClick={() => void copyRecipe()}>Copy recipe</button><button type="button" disabled={Boolean(error)} onClick={() => save("review")}>Download review draft · .json</button></div>
        {exportable && <div className={styles.recipeActions}><button type="button" onClick={() => saveExport("sample")}>Download small-area Drive export</button><button type="button" onClick={() => saveExport("statewide")}>Download statewide Drive export</button></div>}
        {exportable && <p className={styles.footnote}>Run the small-area export first. Keep task IDs, source image IDs, projection, masks, coverage, terms and file hashes in the external private review store. Statewide execution waits for the sample review and Drive capacity check.</p>}
        <p role="status" className={styles.notice}>{notice}</p>
        <details className={styles.instructions}><summary>How to run and review</summary><ol><li><a href={EARTH_ENGINE_ACCESS} target="_blank" rel="noreferrer">Register an Earth Engine project</a> with the access appropriate to your use.</li><li>Copy the script into the <a href="https://code.earthengine.google.com/" target="_blank" rel="noreferrer">Earth Engine Code Editor</a>. Review it, then run it there.</li><li>Inspect source IDs, coverage, quality flags and missing pixels. Keep the complete inputs and processing record before exporting any data.</li><li>Prepare source files and provenance for KFM review. Acceptance for preparation is separate from admission and release.</li></ol><p>These generated recipes have not been executed against Earth Engine. They do not automatically export files, publish layers, or write back to KFM.</p></details>
        <details className={styles.code}><summary>Inspect generated script</summary><pre tabIndex={0} aria-label="Generated Earth Engine JavaScript"><code>{recipe || "Choose a valid year to generate the recipe."}</code></pre></details>
        <div className={styles.links}><a href={earthEngineUrl(selected)} target="_blank" rel="noreferrer">Official dataset & citation ↗</a><Link href={`/data?source=${selected.id}`}>Propose this source for review</Link></div>
      </aside>
    </div>
  </main>;
}
