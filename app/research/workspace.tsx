"use client";

import { useEffect, useMemo, useState } from "react";
import Link from "next/link";
import type { ScienceEventSpec } from "../science-events";
import { SCIENCE_SUPPORT_LABELS } from "../science-events";
import { INVESTIGATIONS, RESEARCH_FRONTIER, RESEARCH_READING, REPRESENTATIONS, discoveryParams, discoverySearch, readDiscoveryState, sourceMapHref, type DiscoverySource, type DiscoveryState } from "./discovery";
import styles from "./research.module.css";

const PAGE_SIZE = 9;
const external = { target: "_blank", rel: "noreferrer" } as const;

export default function ResearchDiscovery({ sources, instruments, initialState }: { sources: DiscoverySource[]; instruments: readonly ScienceEventSpec[]; initialState: DiscoveryState }) {
  const [state, setState] = useState(initialState);
  const [visibleCount, setVisibleCount] = useState(PAGE_SIZE);
  const [message, setMessage] = useState("");
  const domains = useMemo(() => [...new Set(sources.map(source => source.domain))].sort(), [sources]);
  const results = useMemo(() => discoverySearch(sources, state), [sources, state]);
  const selected = state.compare.flatMap(id => sources.filter(source => source.id === id));

  useEffect(() => {
    const params = discoveryParams(state).toString();
    window.history.replaceState(window.history.state, "", `${window.location.pathname}${params ? `?${params}` : ""}${window.location.hash}`);
  }, [state]);
  useEffect(() => {
    const restore = () => { setState(readDiscoveryState(new URLSearchParams(window.location.search), sources)); setVisibleCount(PAGE_SIZE); };
    window.addEventListener("popstate", restore);
    return () => window.removeEventListener("popstate", restore);
  }, [sources]);

  function filter(patch: Partial<DiscoveryState>) { setState(current => ({ ...current, ...patch })); setVisibleCount(PAGE_SIZE); }
  function toggle(id: string) {
    if (state.compare.includes(id)) { filter({ compare: state.compare.filter(value => value !== id) }); setMessage("Source removed from comparison."); }
    else if (state.compare.length < 3) { filter({ compare: [...state.compare, id] }); setMessage("Source added to comparison."); }
  }
  function investigate(ids: readonly string[]) { filter({ query: "", domain: "", kind: "", compare: ids.filter(id => sources.some(source => source.id === id)).slice(0, 3) }); setMessage("Investigation sources selected. Compare their clocks and limitations below."); }

  return <main className={styles.page}>
    <a className={styles.skip} href="#source-catalog">Skip to source catalogue</a>
    <nav className={styles.nav} id="research-top" aria-label="Research navigation">
      <Link className={styles.brand} href="/"><span className={styles.mark} aria-hidden="true">K</span><span>KANSAS FRONTIER MATRIX<small>Place. Time. Evidence.</small></span></Link>
      <div><Link href="/observatory">Event Observatory</Link><Link href="/observatory/sources">Source guide</Link><Link className={styles.mapLink} href="/">Open Explorer <span aria-hidden="true">↗</span></Link></div>
    </nav>

    <header className={styles.hero}>
      <div className={styles.heroText}><p className={styles.eyebrow}>THE RESEARCH DESK · KANSAS</p><h1>One place.<br /><em>A thousand questions.</em></h1><p className={styles.lede}>Follow a river. Look beneath the plains. Connect a landscape to the science that helps explain it.</p><p className={styles.sublede}>Find the right source, see what it can tell you, and carry the question into the map.</p><div className={styles.heroActions}><a className={styles.primary} href="#source-catalog">Find your data <span aria-hidden="true">↓</span></a><a href="#investigations">Start with a question <span aria-hidden="true">↗</span></a></div></div>
      <div className={styles.fieldDiagram} aria-label="Conceptual research connections across air, land, water and life; not measured data" role="img">
        <div className={styles.diagramLabel}>THE SAME LANDSCAPE, DIFFERENT LENSES</div>
        <div className={styles.stratum}><span>01 / AIR</span><strong>Observe the atmosphere</strong><i /></div>
        <div className={styles.stratum}><span>02 / LIFE</span><strong>Ask an ecological question</strong><i /></div>
        <div className={styles.stratum}><span>03 / LAND</span><strong>Read the surface</strong><i /></div>
        <div className={styles.stratum}><span>04 / WATER</span><strong>Look below the ground</strong><i /></div>
        <p>Connected questions. Independent evidence.</p>
      </div>
    </header>

    <div className={styles.metrics} aria-label="Catalogue scope">
      <div><strong>{sources.length}</strong><span>registered map sources</span></div><div><strong>{domains.length}</strong><span>source domains</span></div><div><strong>{instruments.length}</strong><span>science methods & phenomena</span></div><div className={styles.scopeNote}>A source directory, not a live-health check.<br />Provider context keeps its own dates and limits.</div>
    </div>

    <section className={styles.section} id="investigations" aria-labelledby="investigation-title">
      <div className={styles.sectionHeading}><div><p className={styles.eyebrow}>FOLLOW YOUR CURIOSITY</p><h2 id="investigation-title">Start with a question.</h2></div><p>A few useful connections.<br /> Choose one, then inspect the evidence.</p></div>
      <div className={styles.investigations}>{INVESTIGATIONS.map(item => <article key={item.id} className={`${styles.investigation} ${styles[item.className]}`}><span className={styles.number}>{item.number}</span><h3>{item.title}</h3><p className={styles.question}>{item.question}</p><p>{item.detail}</p><a href="#comparison" onClick={() => investigate(item.ids)}>Compare these sources <span aria-hidden="true">↗</span></a><details><summary>What to check</summary><p>{item.note}</p></details></article>)}</div>
    </section>

    <section className={styles.section} aria-labelledby="terrain-pilot-title">
      <div className={styles.pilotShowcase}>
        <div><p className={styles.eyebrow}>TRY THE DATA · NEON KONZA PRAIRIE</p><h2 id="terrain-pilot-title">Read the prairie in three layers.</h2><p>Compare ground elevation, surface elevation and provider canopy height at the same location. Switch surfaces and probe the original sample values in the terrain lab.</p><a className={styles.primary} href="/acquisition#neon-lidar-lab">Open terrain &amp; canopy lab <span aria-hidden="true">↗</span></a><p className={styles.small}>Choose “Load Konza Prairie pilot” in the lab. Loading is explicit; this link starts no download.</p></div>
        <div className={styles.pilotFacts}><span className={styles.badge}>Provider preview · scientific review pending</span><dl><dt>Where &amp; when</dt><dd>One 1 km KONZ tile · catalog month September 2024 · RELEASE-2026</dd><dt>What you see</dt><dd>10 m display cells sample aligned 1 m source rasters. Each cell is one nearest source sample, not an average.</dd><dt>Before drawing conclusions</dt><dd>Provider canopy is distinct from surface minus ground. Retained outliers, reference systems and accuracy need review. This pilot is not admitted KFM evidence.</dd></dl></div>
      </div>
    </section>

    <section className={styles.section} id="observation-tools" aria-labelledby="observation-tools-title">
      <div className={styles.observationTools}>
        <div><p className={styles.eyebrow}>TRY THE OBSERVATIONS · 2020–2025</p><h2 id="observation-tools-title">From a question to a usable record.</h2><p>Explore daily weather, weekly county drought and measured soil depths. Inspect coverage, change the question and download the source-linked observations.</p><Link className={styles.primary} href="/science">Choose a science question <span aria-hidden="true">↗</span></Link><p className={styles.small}>Provider context with its original dates and missing values. Scientific review and KFM dataset admission remain pending.</p></div>
        <ul className={styles.observationToolLinks}>
          <li><Link href="/labs/heat-and-rain"><span>Heat &amp; Rain Lab</span><h3>When did heat, frost and rain shape the season?</h3><small>NOAA GHCN-Daily · 3 stations · 2020–2025</small><b aria-hidden="true">↗</b></Link></li>
          <li><Link href="/labs/county-drought"><span>County Drought Lab</span><h3>How often did drought cover your county?</h3><small>U.S. Drought Monitor · 105 counties · 313 assessments</small><b aria-hidden="true">↗</b></Link></li>
          <li><Link href="/labs/soil-profile"><span>Soil Profile Lab</span><h3>What changed beneath the surface?</h3><small>NOAA USCRN · 2 stations · 5 measured depths</small><b aria-hidden="true">↗</b></Link></li>
        </ul>
      </div>
    </section>

    <section className={styles.section} id="source-catalog" aria-labelledby="catalog-title">
      <div className={styles.sectionHeading}><div><p className={styles.eyebrow}>FIND THE RIGHT INGREDIENTS</p><h2 id="catalog-title">Explore the source catalogue.</h2></div><p>Search across providers, subjects,<br /> source dates and scientific limitations.</p></div>
      <div className={styles.filters}><label className={styles.search}>Search sources<input type="search" value={state.query} maxLength={160} placeholder="Try groundwater, radar, forecast…" onChange={event => filter({ query: event.target.value })} /></label><label>Subject<select value={state.domain} onChange={event => filter({ domain: event.target.value })}><option value="">All subjects</option>{domains.map(domain => <option key={domain}>{domain}</option>)}</select></label><label>Representation<select value={state.kind} onChange={event => filter({ kind: event.target.value })}><option value="">All representations</option>{Object.entries(REPRESENTATIONS).map(([id, title]) => <option key={id} value={id}>{title}</option>)}</select></label></div>
      <div className={styles.resultSummary}><p role="status" aria-live="polite">{results.length} of {sources.length} sources <span>· {state.compare.length} of 3 selected for comparison</span></p>{(state.query || state.domain || state.kind) && <button onClick={() => filter({ query: "", domain: "", kind: "" })}>Clear filters</button>}</div>
      <div className={styles.sourceGrid}>{results.slice(0, visibleCount).map(source => <article className={styles.source} key={source.id}>
        <div className={styles.sourceTop}><span>{source.domain}</span><button type="button" aria-pressed={state.compare.includes(source.id)} aria-label={`${state.compare.includes(source.id) ? "Remove" : "Compare"} ${source.shortTitle}`} disabled={state.compare.length === 3 && !state.compare.includes(source.id)} onClick={() => toggle(source.id)}>{state.compare.includes(source.id) ? "✓ Selected" : "+ Compare"}</button></div>
        <h3>{source.shortTitle}</h3><p className={styles.publisher}>{source.organization}</p><span className={styles.badge}>{REPRESENTATIONS[source.kind]}</span><p>{source.freshness}</p>
        <details><summary>Source details & limitations</summary><dl><dt>Update rhythm</dt><dd>{source.cadence}</dd><dt>What this cannot establish</dt><dd>{source.boundary}</dd><dt>When data is missing</dt><dd>{source.fallback}</dd><dt>Attribution</dt><dd>{source.attribution}</dd></dl>{source.minDisplayZoom !== undefined && <p>Map detail begins at zoom {source.minDisplayZoom}.</p>}<p>External provider context · {source.evidenceRole}</p></details>
        <div className={styles.sourceActions}><a href={source.mapHref}>Open on map <span aria-hidden="true">↗</span></a><a href={source.sourceHref} {...external}>Provider <span aria-hidden="true">↗</span></a></div>
      </article>)}</div>
      {!results.length && <div className={styles.empty}><h3>No sources match these filters.</h3><p>Try a broader term, another subject, or clear the filters.</p><button onClick={() => filter({ query: "", domain: "", kind: "" })}>Show all sources</button></div>}
      {results.length > visibleCount && <button className={styles.more} onClick={() => setVisibleCount(count => count + PAGE_SIZE)}>Show more sources ({results.length - visibleCount} remaining)</button>}
    </section>

    <section className={`${styles.section} ${styles.comparison}`} id="comparison" aria-labelledby="comparison-title">
      <div className={styles.sectionHeading}><div><p className={styles.eyebrow}>PUT THE DETAILS SIDE BY SIDE</p><h2 id="comparison-title">Compare before you combine.</h2></div>{selected.length > 0 && <button onClick={() => { filter({ compare: [] }); setMessage("Comparison cleared."); }}>Clear comparison</button>}</div>
      <p className={styles.comparisonIntro}>Choose up to three sources. Check their clocks, representation and limitations before treating them as compatible inputs.</p><p className={styles.liveMessage} role="status">{message}</p>
      {selected.length ? <><div className={styles.tableWrap} tabIndex={0} role="region" aria-label="Selected source comparison"><table><caption>Source descriptions only. Runtime health, exact units and spatial or temporal compatibility must be checked in the source records.</caption><thead><tr><th scope="col">Compare</th>{selected.map(source => <th scope="col" key={source.id}>{source.shortTitle}<button aria-label={`Remove ${source.shortTitle} from comparison`} onClick={() => toggle(source.id)}>Remove</button></th>)}</tr></thead><tbody>{([
        ["Provider", (source: DiscoverySource) => source.organization], ["Representation", (source: DiscoverySource) => REPRESENTATIONS[source.kind]], ["Time & freshness", (source: DiscoverySource) => source.freshness], ["Update rhythm", (source: DiscoverySource) => source.cadence], ["Scientific limits", (source: DiscoverySource) => source.boundary], ["Missing data", (source: DiscoverySource) => source.fallback],
      ] as const).map(([label, value]) => <tr key={label}><th scope="row">{label}</th>{selected.map(source => <td key={source.id}>{value(source)}</td>)}</tr>)}<tr><th scope="row">Original source</th>{selected.map(source => <td key={source.id}><a href={source.sourceHref} {...external}>Inspect provider ↗</a>{source.downloadHref && <a href={source.downloadHref} {...external}>{source.downloadLabel} ↗</a>}</td>)}</tr></tbody></table></div><a className={styles.primary} href={sourceMapHref(selected.map(source => source.id))}>Explore selected sources on the map ↗</a><p className={styles.small}>Map services can be unavailable or require a closer zoom. A shared map is a starting point for investigation; it does not establish causation or a reviewed analysis.</p></> : <div className={styles.empty}><span aria-hidden="true">＋</span><h3>Bring a few sources together.</h3><p>Use “Compare” on a source, or choose a guided investigation above.</p><a href="#source-catalog">Browse the catalogue ↑</a></div>}
    </section>

    <section className={styles.section} id="science" aria-labelledby="science-title"><div className={styles.sectionHeading}><div><p className={styles.eyebrow}>GO DEEPER</p><h2 id="science-title">A method for every question.</h2></div><p>Explore the measurements and time rules.<br /> Some need additional data or analysis.</p></div><div className={styles.methods}>{instruments.map(item => <details key={item.id}><summary><span aria-hidden="true">{item.glyph}</span><strong>{item.title}</strong><small>{SCIENCE_SUPPORT_LABELS[item.support]}</small></summary><dl><dt>Measure</dt><dd>{item.measurement}</dd><dt>Time support</dt><dd>{item.clock}</dd><dt>Visual method</dt><dd>{item.representation}</dd><dt>Limit</dt><dd>{item.limitation}</dd></dl><a href={item.sourceUrl} {...external}>{item.sourceLabel} ↗</a></details>)}</div></section>

    <section className={`${styles.section} ${styles.frontier}`} id="frontier" aria-labelledby="frontier-title"><div className={styles.sectionHeading}><div><p className={styles.eyebrow}>THE NEXT QUESTIONS</p><h2 id="frontier-title">Prairie science, across scales.</h2></div><span className={styles.badge}>Research references · not imported</span></div><p className={styles.comparisonIntro}>From field observations to grass transcription studies: follow the original records, inspect their methods, and identify the next useful addition to KFM.</p><div className={styles.frontierGrid}>{RESEARCH_FRONTIER.map(item => <article key={item.id}><span className={styles.eyebrow}>{item.scale}</span><h3><a href={item.href} {...external}>{item.title} ↗</a></h3><p className={styles.publisher}>{item.publisher}</p><p>{item.description}</p><details><summary>Before using this in KFM</summary><p>{item.gate}</p></details><small>Reference checked {item.checked} · {item.id}</small></article>)}</div><div className={styles.reading}><h3>Read the research</h3>{RESEARCH_READING.map(item => <p key={item.id}><a href={item.href} {...external}>{item.title} ↗</a><small>{item.publisher} · PubMed {item.id} · reference checked 2026-11-23</small></p>)}<p className={styles.small}>Reading leads to investigate; this page does not establish their findings or connect their samples to the map.</p></div></section>
    <footer className={styles.footer}><p>Curiosity can connect disciplines.<br /><strong>Evidence tells us how far we can go.</strong></p><div><Link href="/data-library">Browse the data library</Link><Link href="/labs">Open research labs</Link><a href="#research-top">Back to top ↑</a></div></footer>
  </main>;
}
