"use client";

import Link from "next/link";
import { useEffect, useMemo, useRef, useState } from "react";
import { CIVIC_SOURCES, type CivicCategory } from "../civic-sources";
import { CIVIC_CATEGORIES, CIVIC_REFLECTION_LENSES, civicCounties, civicMapHref, civicQuestion, civicSourcePage, civicSourceUrl, filterCivicSources, type CivicCounty, type CivicSourceWindow } from "../civic-model";
import styles from "./civic.module.css";

const sourceStatus = { "page-verified": "Source page checked", "link-verified": "Official link found", "needs-verification": "Needs verification" };

export default function CivicAtlas() {
  const [category, setCategory] = useState<CivicCategory | "all">("all"), [query, setQuery] = useState("");
  const [counties, setCounties] = useState<CivicCounty[]>([]), [countyId, setCountyId] = useState("");
  const [countyState, setCountyState] = useState<"idle" | "loading" | "ready" | "error">("idle");
  const [copyState, setCopyState] = useState<{ question: string; message: string } | null>(null);
  const [sourceWindow, setSourceWindow] = useState<CivicSourceWindow | null>(null);
  const [lenses, setLenses] = useState<string[]>([]), [reflection, setReflection] = useState("");
  const request = useRef<AbortController | null>(null), questionField = useRef<HTMLTextAreaElement>(null);
  const sourceHeading = useRef<HTMLHeadingElement>(null);
  useEffect(() => () => { request.current?.abort(); }, []);
  const county = counties.find(item => item.geoid === countyId) ?? null;
  const sources = useMemo(() => filterCivicSources(CIVIC_SOURCES, category, query), [category, query]);
  const filterKey = JSON.stringify([category, query]);
  const sourcePage = civicSourcePage(sources, filterKey, sourceWindow);
  const question = civicQuestion(category, county);

  function chooseCategory(value: CivicCategory | "all") { setCategory(value); setSourceWindow(null); }
  function searchSources(value: string) { setQuery(value); setSourceWindow(null); }

  function showFewerSources() {
    setSourceWindow({ filterKey, limit: 12 });
    // The heading survives collapsed cards and controls, preserving a useful keyboard position.
    sourceHeading.current?.focus({ preventScroll: true });
    sourceHeading.current?.scrollIntoView({ block: "start" });
  }

  async function loadCounties() {
    request.current?.abort();
    const controller = new AbortController(); request.current = controller;
    setCountyState("loading"); setCountyId(""); setCounties([]);
    try {
      const response = await fetch("/api/event-atlas/counties?edition=2020", { signal: AbortSignal.any([controller.signal, AbortSignal.timeout(20000)]) });
      if (!response.ok) throw new Error("unavailable");
      const loaded = civicCounties(await response.json());
      if (loaded.length !== 105) throw new Error("incomplete");
      if (!controller.signal.aborted) { setCounties(loaded); setCountyState("ready"); }
    } catch { if (!controller.signal.aborted) setCountyState("error"); }
  }

  async function copyQuestion() {
    try { await navigator.clipboard.writeText(question); setCopyState({ question, message: "Question copied. Paste it into Ask KFM and review before sending." }); }
    catch { questionField.current?.focus(); questionField.current?.select(); setCopyState({ question, message: "Copy is unavailable in this browser. The question is selected for you to copy." }); }
  }

  return <main className={styles.page}>
    <div className={styles.shell}>
      <header className={styles.topbar}><Link href="/">← Kansas map</Link><nav aria-label="Related KFM pages"><Link href="/topics">Explore topics</Link><Link href="/knowledge">Released knowledge</Link></nav></header>
      <div className={styles.hero}>
        <div><p className={styles.eyebrow}>KANSAS FRONTIER MATRIX · CIVIC ATLAS</p><h1>Understand the decisions<br />that shape your place.</h1>
          <p className={styles.lead}>Follow the public record from your community to the Capitol. Find the office, inspect the money, trace a decision, and ask better questions.</p>
          <div className={styles.heroLinks}><a href="#sources">Explore official sources ↓</a><a href="#compare">Compare fairly</a><a href="#compass">Your moral compass</a></div>
        </div>
        <section className={styles.placeCard} aria-labelledby="place-heading"><span className={styles.placeMark} aria-hidden="true">KS</span><h2 id="place-heading">Start with a place</h2>
          <p>Choose a county for map context and your research question.</p>
          {countyState === "ready" ? <><label htmlFor="civic-county">County</label><select id="civic-county" value={countyId} onChange={event => setCountyId(event.target.value)}><option value="">All Kansas</option>{counties.map(item => <option key={item.geoid} value={item.geoid}>{item.title}</option>)}</select></>
            : <button className={styles.secondaryButton} type="button" disabled={countyState === "loading"} onClick={loadCounties}>{countyState === "loading" ? "Loading county choices…" : countyState === "error" ? "Retry county choices" : "Load county choices"}</button>}
          <p className={styles.small} role="status">{countyState === "error" ? "County choices are unavailable. You can still use statewide sources and the map." : countyState === "ready" ? "105 counties · 2020 Census display boundaries" : "Uses KFM’s existing Census county map source."}</p>
          <Link className={styles.primaryButton} href={civicMapHref(county)} prefetch={false}>{county ? `View ${county.title} on the map` : "Open Kansas county map"}<span aria-hidden="true">↗</span></Link>
          <p className={styles.small}>County selection frames the map; it does not determine your ballot or filter these statewide source links.</p>
        </section>
      </div>

      <div className={styles.scopeNote}><span aria-hidden="true">↗</span><p><strong>A guide to the sources.</strong> These links help you find public records. They do not establish that records are loaded into KFM, released as evidence, or complete for your community.</p></div>

      <section id="sources" className={styles.section} aria-labelledby="source-heading">
        <div className={styles.sectionHeading}><div><p className={styles.eyebrow}>FOLLOW A QUESTION</p><h2 ref={sourceHeading} tabIndex={-1} id="source-heading">Your civic source desk</h2></div><label className={styles.search}><span>Search sources</span><input type="search" placeholder="Try budget, county, jobs…" value={query} onChange={event => searchSources(event.target.value)} maxLength={160} /></label></div>
        <div className={styles.categories} aria-label="Filter sources by subject"><button type="button" aria-pressed={category === "all"} onClick={() => chooseCategory("all")}>All sources</button>{CIVIC_CATEGORIES.map(item => <button type="button" key={item.id} aria-pressed={category === item.id} onClick={() => chooseCategory(item.id)}>{item.title}</button>)}</div>
        <p className={styles.resultCount} aria-live="polite">Showing {sourcePage.shown} of {sourcePage.total} matching source{sourcePage.total === 1 ? "" : "s"}{category !== "all" ? ` · ${CIVIC_CATEGORIES.find(item => item.id === category)?.title}` : ""}. Checks describe discovery on the date shown, not present availability.</p>
        {sources.length ? <div id="civic-source-list" className={styles.sourceGrid}>{sourcePage.items.map(source => <article key={source.id} className={styles.sourceCard}>
          <div className={styles.sourceMeta}><span>{CIVIC_CATEGORIES.find(item => item.id === source.category)?.title}</span><span className={styles.status}>{sourceStatus[source.status]}</span></div>
          <h3><a href={civicSourceUrl(source.url)!} target="_blank" rel="noopener noreferrer">{source.title}<span aria-label="opens in a new tab"> ↗</span></a></h3>
          <p>{source.description}</p><p className={styles.organization}>{source.organization} · {source.geography}</p>
          <details><summary>Source check & limitations</summary><p>Checked <time dateTime={source.checkedAt}>{source.checkedAt}</time></p><p>{source.limitation}</p></details>
        </article>)}</div> : <div className={styles.empty}><h3>No source matches those filters</h3><p>Try a broader word or reset the filters. An empty search does not mean the public record does not exist.</p><button type="button" onClick={() => { chooseCategory("all"); searchSources(""); }}>Reset filters</button></div>}
        {sourcePage.total > 12 && <div className={styles.pagination}>
          <button type="button" aria-controls="civic-source-list" onClick={sourcePage.hasMore ? () => setSourceWindow({ filterKey, limit: sourcePage.nextLimit }) : showFewerSources}>{sourcePage.hasMore ? `Show ${Math.min(12, sourcePage.total - sourcePage.shown)} more sources` : "Show fewer sources"}</button>
          {sourcePage.hasMore && sourcePage.shown > 12 && <button type="button" className={styles.textButton} aria-controls="civic-source-list" onClick={showFewerSources}>Show fewer sources</button>}
          <span>{sourcePage.shown} of {sourcePage.total} shown</span>
        </div>}
      </section>

      <section className={styles.questionCard} aria-labelledby="question-heading"><div><p className={styles.eyebrow}>MAKE THE NEXT QUESTION COUNT</p><h2 id="question-heading">A starting point for Ask KFM</h2><p>This question follows your selected subject{county ? ` and ${county.title}` : ""}. Copy it, then open chat and review it before sending. Your private reflection below is excluded.</p><div className={styles.actions}><button type="button" onClick={copyQuestion}>Copy question</button><Link href="/?kfm-chat=1" prefetch={false}>Open Ask KFM ↗</Link></div><p className={styles.small} role="status">{copyState?.question === question ? copyState.message : "AI can help explain a method. Factual answers still need checked evidence."}</p></div><div><label htmlFor="civic-question">Question to review</label><textarea ref={questionField} id="civic-question" readOnly value={question} rows={7} /></div></section>

      <div className={styles.toolGrid}>
        <section id="compare" className={styles.toolCard} aria-labelledby="compare-heading"><p className={styles.eyebrow}>SAME QUESTIONS · SAME STANDARD</p><h2 id="compare-heading">Compare candidates fairly</h2><p>Start with the official ballot for the same office, district and election. Use the same fields for every candidate; missing evidence stays “not found.”</p>
          <dl className={styles.comparisonFields}><div><dt>Role & authority</dt><dd>What can this office actually decide?</dd></div><div><dt>Public positions</dt><dd>What did the candidate say, where, and when?</dd></div><div><dt>Recorded actions</dt><dd>Which vote, proposal or decision supports the claim?</dd></div><div><dt>Disclosed finances</dt><dd>Which filing, reporting period and amendment are you reading?</dd></div><div><dt>Unknowns & corrections</dt><dd>Which records are missing, disputed or superseded?</dd></div></dl>
          <p className={styles.small}>No candidate ranking or candidate records are loaded here. A donation does not by itself establish influence or wrongdoing.</p><button type="button" className={styles.textButton} onClick={() => { chooseCategory("voting"); searchSources(""); document.getElementById("sources")?.scrollIntoView({ block: "start" }); }}>Find official election sources ↑</button>
        </section>
        <section id="compass" className={styles.toolCard} aria-labelledby="compass-heading"><p className={styles.eyebrow}>PRIVATE REFLECTION · NO SCORE</p><h2 id="compass-heading">Your moral compass</h2><p>Choose the questions that matter to you. This is a way to examine tradeoffs, not a rating of a person’s morality or a voting recommendation.</p>
          <fieldset className={styles.lenses}><legend>Which perspectives would you like to consider?</legend>{CIVIC_REFLECTION_LENSES.map(lens => <label key={lens.id}><input type="checkbox" checked={lenses.includes(lens.id)} onChange={event => setLenses(current => event.target.checked ? [...current, lens.id] : current.filter(id => id !== lens.id))} /><span><strong>{lens.title}</strong><small>{lens.question}</small></span></label>)}</fieldset>
          <label htmlFor="civic-reflection">Your thoughts, questions or unresolved tradeoffs</label><textarea id="civic-reflection" rows={3} value={reflection} onChange={event => setReflection(event.target.value)} maxLength={2000} placeholder="What evidence would help you decide?" />
          <div className={styles.reflectionFooter}><p className={styles.small}>Kept only in this page’s memory. Not saved or included in the prepared AI question; cleared when this page reloads.</p><button type="button" onClick={() => { setLenses([]); setReflection(""); }} disabled={!lenses.length && !reflection}>Clear reflection</button></div>
        </section>
      </div>

      <section className={styles.method} aria-labelledby="method-heading"><div><p className={styles.eyebrow}>FROM A CLAIM TO ITS RECORD</p><h2 id="method-heading">Check what changed.<br />Then ask why.</h2></div><ol><li><strong>Pin the claim.</strong><span>Keep the exact words, speaker, date and place.</span></li><li><strong>Find the underlying record.</strong><span>Check the bill version, vote, budget, filing or survey methods.</span></li><li><strong>Compare like with like.</strong><span>Use the same geography, time period and units; distinguish proposals from actual spending.</span></li><li><strong>Keep the limits visible.</strong><span>A trend is not proof of cause. Missing coverage is not zero, and an opt-in poll cannot represent all residents.</span></li></ol></section>
      <footer className={styles.footer}><p>Public records. Clear limits. Your judgment.</p><Link href="/about">How KFM handles evidence ↗</Link></footer>
    </div>
  </main>;
}
