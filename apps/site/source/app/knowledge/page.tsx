"use client";

import { useEffect, useState, useSyncExternalStore } from "react";
import Link from "next/link";
import { readKnowledge, knowledgeUnavailable, type KnowledgeResult } from "../knowledge-read";
import styles from "./knowledge.module.css";

const subscribeLocation = (changed: () => void) => {
  window.addEventListener("popstate", changed);
  return () => window.removeEventListener("popstate", changed);
};
const locationTerm = () => new URLSearchParams(window.location.search).get("term") ?? "";
const serverTerm = () => "";

export default function KansasKnowledgePage() {
  const term = useSyncExternalStore(subscribeLocation, locationTerm, serverTerm);
  return <KnowledgeSearch key={term} initialTerm={term} />;
}

function KnowledgeSearch({ initialTerm }: { initialTerm: string }) {
  const [query, setQuery] = useState(initialTerm.slice(0, 80));
  const [submitted, setSubmitted] = useState({ term: initialTerm });
  const [completed, setCompleted] = useState<{ request: typeof submitted; result: KnowledgeResult } | null>(null);
  const result = completed?.request === submitted ? completed.result : null;
  const busy = result === null;
  useEffect(() => {
    const abort = new AbortController();
    void readKnowledge({ kind: "search", term: submitted.term }, abort.signal)
      .then(result => { if (!abort.signal.aborted) setCompleted({ request: submitted, result }); })
      .catch(() => { if (!abort.signal.aborted) setCompleted({ request: submitted, result: knowledgeUnavailable() }); });
    return () => abort.abort();
  }, [submitted]);

  const records = result?.data?.records ?? [];
  return <main className={styles.page}>
    <header className={styles.header}><Link href="/">← Kansas map</Link><span>REVIEWED KNOWLEDGE</span></header>
    <div className={styles.intro}><p>KANSAS KNOWLEDGE</p><h1>Places, facts, people, events, and stories</h1>
      <p>Search only entries whose sources, rights, sensitivity, evidence, and release have been reviewed. Narratives and conflicting accounts remain labeled. A place label is not an exact site location.</p></div>
    <form className={styles.search} onSubmit={event => { event.preventDefault(); setSubmitted({ term: query.trim() }); }}>
      <label htmlFor="knowledge-term">Search released entries</label>
      <div><input id="knowledge-term" type="search" maxLength={80} value={query} onChange={event => setQuery(event.target.value)} placeholder="Kansas place, event, or topic" /><button type="submit" disabled={busy}>Search</button></div>
    </form>
    <section className={styles.results} aria-live="polite" aria-busy={busy}>
      {busy && <p>Checking reviewed records…</p>}
      {!busy && result?.envelope.reason_code === "NO_APPROVED_KNOWLEDGE" && <p>No knowledge release is active yet. Source discovery and candidate preparation do not publish entries.</p>}
      {!busy && result?.envelope.reason_code === "RECORD_NOT_FOUND" && <p>No released record matches this search. This does not mean no source record exists.</p>}
      {!busy && result?.envelope.reason_code === "RELEASE_HELD" && <p>The current knowledge release is held or withdrawn.</p>}
      {!busy && result?.envelope.reason_code === "INVALID_QUERY" && <p>The search is invalid. Use at most 80 characters.</p>}
      {!busy && result?.envelope.outcome === "ERROR" && <p>The reviewed knowledge store is unavailable. Try again later.</p>}
      {!busy && result?.envelope.reason_code === "RELEASED" && <><p className={styles.release}>Released {result.data?.released_at?.slice(0, 10)} · {records.length} shown{result.data?.has_more ? " · more results exist; narrow your search" : ""}</p>
        <div className={styles.cards}>{records.map(record => <article key={record.record_id} className={styles.card}>
          <div className={styles.tags}><span>{record.kind}</span><span>{record.geometry_role}</span><span>{record.time_start ? `${record.time_start}${record.time_end && record.time_end !== record.time_start ? `–${record.time_end}` : ""}` : "Time unspecified"}</span></div>
          <h2><Link href={`/knowledge/record?id=${encodeURIComponent(record.record_id)}`}>{record.title}</Link></h2><p>{record.summary}</p><p className={styles.place}>{record.location_label}</p>
          <div className={styles.assertions}>{record.assertions.map((item, index) => <p key={`${record.record_id}-${index}`}><strong>{item.status === "documented" ? "Documented" : item.status === "conflicting" ? "Conflicting account" : "Narrative interpretation"}</strong> {item.text}</p>)}</div>
          <footer><a href={record.source_url} target="_blank" rel="noopener noreferrer">Official source ↗</a><small>Evidence {record.evidence_ref} · review {record.review_ref}</small></footer>
        </article>)}</div>
      </>}
    </section>
  </main>;
}
