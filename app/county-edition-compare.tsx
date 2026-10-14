"use client";
import { useEffect, useMemo, useState } from "react";
import { browserJsonRequest } from "./browser-json-request";
import { compareCountyEditions, decodeCountyEdition, type CountyEditionData } from "./county-edition-comparison";
let cached: [CountyEditionData, CountyEditionData] | null = null;
type State = { kind: "loading" } | { kind: "error" } | { kind: "ready"; pair: [CountyEditionData, CountyEditionData] };
const shown = (value: number | null) => value === null ? "Not supplied" : value.toLocaleString("en-US");
export default function CountyEditionCompare() {
  const [state, setState] = useState<State>(() => cached ? { kind: "ready", pair: cached } : { kind: "loading" });
  const [attempt, setAttempt] = useState(0), [county, setCounty] = useState(""), [swapped, setSwapped] = useState(false);
  useEffect(() => {
    if (cached && attempt === 0) return;
    const controller = new AbortController();
    void Promise.all((["2010", "2020"] as const).map(async edition => {
      const { response, body } = await browserJsonRequest(`/api/event-atlas/counties?edition=${edition}`, { signal: controller.signal, maxBytes: 6 * 1024 * 1024, timeoutMs: 25_000 });
      if (!response.ok) throw new Error("Census unavailable");
      return decodeCountyEdition(body, edition);
    })).then(result => {
      if (controller.signal.aborted) return;
      const pair = result as [CountyEditionData, CountyEditionData];
      compareCountyEditions(...pair); // Validate the complete join before presenting any totals.
      cached = pair; setState({ kind: "ready", pair });
    }).catch(() => { if (!controller.signal.aborted) { controller.abort(); setState({ kind: "error" }); } });
    return () => controller.abort();
  }, [attempt]);
  const comparison = useMemo(() => state.kind === "ready" ? compareCountyEditions(state.pair[swapped ? 1 : 0], state.pair[swapped ? 0 : 1], county || null) : null, [state, swapped, county]);
  const retry = () => { cached = null; setState({ kind: "loading" }); setAttempt(value => value + 1); };
  const download = () => {
    if (!comparison) return;
    const url = URL.createObjectURL(new Blob([JSON.stringify(comparison, null, 2)], { type: "application/json" }));
    const link = document.createElement("a"); link.href = url; link.download = "kfm-census-edition-comparison.json"; link.click(); setTimeout(() => URL.revokeObjectURL(url), 1000);
  };
  return <section className="county-edition-compare" aria-label="Census edition comparison">
    <header><span>PUBLIC SOURCE COMPARISON</span><h4>County editions · 2010 ↔ 2020</h4></header>
    <p>Compare dated Census population and housing counts by county FIPS. These editions are independent of the map year and are not present-day estimates or KFM released evidence.</p>
    {state.kind === "loading" && <p role="status">Loading both Census editions…</p>}
    {state.kind === "error" && <div role="status"><p>Both complete county editions could not be verified. No totals or changes are inferred.</p><button type="button" onClick={retry}>Retry Census comparison</button></div>}
    {state.kind === "ready" && comparison && <>
      <label>Comparison area<select aria-label="Census comparison county" value={county} onChange={event => setCounty(event.target.value)}><option value="">All 105 Kansas counties</option>{[...state.pair[1].rows].sort((a,b) => a.name.localeCompare(b.name)).map(row => <option key={row.geoid} value={row.geoid}>{row.name}</option>)}</select></label>
      <div className="map-utility-actions"><button type="button" onClick={() => setSwapped(value => !value)}>Swap A and B</button><button type="button" onClick={retry}>Refresh editions</button><button type="button" onClick={download}>Download comparison JSON</button></div>
      <p>{comparison.scope} · {comparison.matchedCounties} matched {comparison.matchedCounties === 1 ? "county" : "counties"}</p>
      <table><caption>Census counts · change is B minus A</caption><thead><tr><th scope="col">Measure</th><th scope="col">A · {comparison.editions[0]}</th><th scope="col">B · {comparison.editions[1]}</th><th scope="col">Change</th></tr></thead><tbody>{([['Population · people',comparison.population],['Housing · units',comparison.housingUnits]] as const).map(([label,metric]) => <tr key={label}><th scope="row">{label}</th><td>{shown(metric.a)}</td><td>{shown(metric.b)}</td><td>{shown(metric.delta)}{metric.percent !== null && <small>{metric.percent.toFixed(2)}%</small>}</td></tr>)}</tbody></table>
      <details><summary>Source editions, retrieval times & limitations</summary>{comparison.sources.map(source => <article key={source.edition}><a href={source.source} target="_blank" rel="noreferrer">{source.edition} U.S. Census Bureau source ↗</a><p>Retrieved {source.retrievedAt}</p><p>{source.limitation}</p></article>)}<p>Missing counts stay missing. A zero starting count has no percentage change. County geometry may differ between editions; this table compares matched counts, not boundary or land-use changes.</p></details>
    </>}
  </section>;
}
