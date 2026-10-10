"use client";
import { useEffect, useMemo, useState } from "react";
import {
  filterHistoryResearch, historyResearchKnowledgeLink, loadHistoryResearchCatalog,
  HISTORY_RESEARCH_KINDS, HISTORY_RESEARCH_PAGE_SIZE, type HistoryResearchCatalog,
} from "../../history-research-model";
import s from "../../downloads/workspace.module.css";
import h from "../../history-research.module.css";

const kindLabels = { person: "Person", event: "Event", topic: "Topic", organization: "Organization", fictional: "Fictional character" };
const accessLabels = { readable: "Readable", partial: "Partially accessible", blocked: "Blocked — not acquired" };

export default function PeopleEventsResearch() {
  const [catalog, setCatalog] = useState<HistoryResearchCatalog | null>(null);
  const [error, setError] = useState("");
  const [attempt, setAttempt] = useState(0);
  const [query, setQuery] = useState("");
  const [sourceId, setSourceId] = useState("all");
  const [kind, setKind] = useState("all");
  const [page, setPage] = useState(0);
  useEffect(() => {
    const controller = new AbortController();
    void loadHistoryResearchCatalog(controller.signal).then(value => {
      if (!controller.signal.aborted) setCatalog(value);
    }).catch(() => {
      if (!controller.signal.aborted) setError("The research catalogue could not be loaded or validated. Try again; no entries are shown until validation succeeds.");
    });
    return () => controller.abort();
  }, [attempt]);
  const records = useMemo(() => catalog ? filterHistoryResearch(catalog, query, sourceId, kind) : [], [catalog, query, sourceId, kind]);
  const sources = useMemo(() => new Map(catalog?.sources.map(source => [source.id, source]) ?? []), [catalog]);
  const pages = Math.max(1, Math.ceil(records.length / HISTORY_RESEARCH_PAGE_SIZE));
  const current = Math.min(page, pages - 1);
  const first = current * HISTORY_RESEARCH_PAGE_SIZE;
  const clear = () => { setQuery(""); setSourceId("all"); setKind("all"); setPage(0); };
  const filtered = !!query || sourceId !== "all" || kind !== "all";
  return <main className={s.page}><div className={`${s.wrap} ${h.wrap}`}>
    <nav className={h.navigation} aria-label="History navigation"><a href="/downloads#history">← History &amp; archives</a><a href="/knowledge">Reviewed KFM knowledge</a><a href="#research-sources">Source catalogue</a></nav>
    <header className={h.intro}><p className={s.eyebrow}>KANSAS HISTORY · SOURCE RESEARCH</p><h1>People, events &amp; historical context</h1>
      <p>Explore entries from the supplied history and biography pages. Each entry preserves source metadata and context; repeated names remain separate source assertions.</p>
    </header>
    <p className={s.alert}>Research candidates · source admission: not admitted · review: pending · map activation: none. Dates and places retain their stated context; a place is not automatically a birthplace or an exact location. These entries are separate from reviewed KFM knowledge.</p>
    <div className={h.downloads}><a href="/history/people-events.json" download>Download catalogue JSON</a><a href="/history/people-events.csv" download>Download entries CSV</a></div>
    {!catalog && <output className={h.status} aria-live="polite">{error ? "Research catalogue unavailable" : "Loading research metadata from this Site (maximum 3 MiB)…"}</output>}
    {error && <p className={s.alert} role="alert">{error} <button type="button" onClick={() => { setError(""); setAttempt(value => value + 1); }}>Retry loading</button></p>}
    {catalog && <>
      <div className={h.summary}><p><strong>{catalog.records.length.toLocaleString("en-US")}</strong> source entries</p><p><strong>{catalog.sources.length}</strong> supplied sources</p><p><strong>{catalog.sources.filter(source => source.access === "blocked").length}</strong> blocked sources</p></div>
      <p className={s.muted}>{catalog.scope}</p><p className={s.snapshot}>Catalogue checked {catalog.checkedAt} · entry counts are not counts of unique people or verified facts.</p>
      <section aria-labelledby="research-results-title">
        <h2 id="research-results-title">Browse source entries</h2>
        <div className={h.filters}>
          <label htmlFor="history-research-query">Search entries<input id="history-research-query" type="search" value={query} maxLength={300} onChange={event => { setQuery(event.target.value); setPage(0); }} placeholder="Name, date, place or topic…" /></label>
          <label htmlFor="history-research-source">Source<select id="history-research-source" value={sourceId} onChange={event => { setSourceId(event.target.value); setPage(0); }}><option value="all">All sources</option>{catalog.sources.map(source => <option key={source.id} value={source.id}>{source.title} ({source.recordCount}; {accessLabels[source.access]})</option>)}</select></label>
          <label htmlFor="history-research-kind">Entry kind<select id="history-research-kind" value={kind} onChange={event => { setKind(event.target.value); setPage(0); }}><option value="all">All kinds</option>{HISTORY_RESEARCH_KINDS.map(value => <option key={value} value={value}>{kindLabels[value]}</option>)}</select></label>
        </div>
        <div className={h.resultHeading}><output className={h.status} aria-live="polite">{records.length.toLocaleString("en-US")} matching entries{records.length > 0 ? ` · showing ${first + 1}–${Math.min(first + HISTORY_RESEARCH_PAGE_SIZE, records.length)} · page ${current + 1} of ${pages}` : ""}</output>{filtered && <button type="button" onClick={clear}>Clear filters</button>}</div>
        <p className={s.muted}>“Search reviewed KFM” searches released knowledge by the entry title. A matching released record may be absent; the search does not establish identity or a geographic link.</p>
        {!records.length && <p className={s.empty}>No entries match these filters. Try another term or choose all sources and kinds. Blocked sources remain listed below even when no records were acquired.</p>}
        {records.length > 0 && <><nav className={h.pagination} aria-label="Research entry pages"><button type="button" disabled={current === 0} onClick={() => setPage(value => Math.max(0, value - 1))}>Previous entries</button><span>Page {current + 1} of {pages}</span><button type="button" disabled={current + 1 >= pages} onClick={() => setPage(value => Math.min(pages - 1, value + 1))}>Next entries</button></nav>
          <ul className={h.records} aria-label="Source research entries">{records.slice(first, first + HISTORY_RESEARCH_PAGE_SIZE).map(record => {
            const source = sources.get(record.sourceId)!;
            return <li key={record.id}><article className={h.record}>
              <p className={s.eyebrow}>{kindLabels[record.kind]} · {record.category}</p><h3>{record.title}</h3>
              <p className={h.attribution}>Source: <a href={`#research-source-${source.id}`}>{source.title}</a> · {source.publisher}</p>
              <p>{record.relation}</p>
              <dl className={h.context}><div><dt>Date stated by source</dt><dd>{record.date ?? "Not specified in this entry"}</dd></div><div><dt>Place context stated by source</dt><dd>{record.place ?? "Not specified in this entry"}</dd></div></dl>
              <p className={h.review}>{record.reviewNote}</p>
              {record.themes.length > 0 && <p className={h.themes}>Topics: {record.themes.join(" · ")}</p>}
              <div className={h.actions}><a href={record.sourceUrl} target="_blank" rel="noopener noreferrer">Source page ↗</a>{record.targetUrl !== record.sourceUrl && <a href={record.targetUrl} target="_blank" rel="noopener noreferrer">Linked source entry ↗</a>}<a href={historyResearchKnowledgeLink(record.title)}>Search reviewed KFM →</a></div>
            </article></li>;
          })}</ul>
        </>}
      </section>
      <section id="research-sources" className={h.sourceSection} aria-labelledby="research-sources-title"><h2 id="research-sources-title">Source catalogue</h2><p className={s.muted}>All supplied sources remain visible here. Access and completeness describe this curation check, not the entire publisher’s holdings.</p>
        <ul className={h.sources} aria-label="Supplied research sources">{catalog.sources.map(source => <li key={source.id} id={`research-source-${source.id}`}><article>
          <p className={s.eyebrow}>{source.publisher}</p><h3><a href={source.url} target="_blank" rel="noopener noreferrer">{source.title} ↗</a></h3>
          <p className={h.access} data-access={source.access}>{accessLabels[source.access]} · {source.recordCount.toLocaleString("en-US")} curated entries</p>
          <p>{source.accessNote}</p><p><strong>Completeness:</strong> {source.completeness}</p><p><strong>Coverage:</strong> {source.coverage}</p>
          <details><summary>Rights &amp; check date</summary><p>{source.rights}</p><p>Checked {source.checkedAt}</p></details>
        </article></li>)}</ul>
        <p className={h.attribution}>{catalog.attribution}</p>
      </section>
    </>}
  </div></main>;
}
