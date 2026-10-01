"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import styles from "./knowledge.module.css";

type RecordItem = {
  record_id: string; kind: string; title: string; summary: string; location_label: string;
  geometry_role: string; time_start: string | null; time_end: string | null;
  source_url: string; evidence_ref: string; review_ref: string;
  assertions: { text: string; status: "documented" | "conflicting" | "narrative"; source_ref: string; evidence_ref: string }[];
};
type Result = { envelope: { outcome: string; reason_code: string }; data?: { records: RecordItem[]; release_id: string; released_at: string; has_more: boolean } };

export default function KansasKnowledgePage() {
  const [query, setQuery] = useState("");
  const [submitted, setSubmitted] = useState("");
  const [result, setResult] = useState<Result | null>(null);
  const [busy, setBusy] = useState(true);
  useEffect(() => {
    const abort = new AbortController();
    setBusy(true);
    fetch(`/api/governed/v1/knowledge?term=${encodeURIComponent(submitted)}`, { signal: abort.signal, cache: "no-store" })
      .then(async response => {
        const body = await response.json() as Result;
        if (!response.ok && body.envelope?.reason_code !== "INVALID_QUERY") throw new Error("STORE_UNAVAILABLE");
        setResult(body);
      })
      .catch(error => { if (error.name !== "AbortError") setResult({ envelope: { outcome: "ERROR", reason_code: "STORE_UNAVAILABLE" } }); })
      .finally(() => { if (!abort.signal.aborted) setBusy(false); });
    return () => abort.abort();
  }, [submitted]);

  const records = result?.data?.records ?? [];
  return <main className={styles.page}>
    <header className={styles.header}><Link href="/">← Kansas map</Link><span>REVIEWED KNOWLEDGE</span></header>
    <div className={styles.intro}><p>KANSAS KNOWLEDGE</p><h1>Places, facts, people, events, and stories</h1>
      <p>Search only entries whose sources, rights, sensitivity, evidence, and release have been reviewed. Narratives and conflicting accounts remain labeled. A place label is not an exact site location.</p></div>
    <form className={styles.search} onSubmit={event => { event.preventDefault(); setSubmitted(query.trim()); }}>
      <label htmlFor="knowledge-term">Search released entries</label>
      <div><input id="knowledge-term" type="search" maxLength={80} value={query} onChange={event => setQuery(event.target.value)} placeholder="Kansas place, event, or topic" /><button type="submit" disabled={busy}>Search</button></div>
    </form>
    <section className={styles.results} aria-live="polite" aria-busy={busy}>
      {busy && <p>Checking reviewed records…</p>}
      {!busy && result?.envelope.reason_code === "NO_APPROVED_KNOWLEDGE" && <p>No knowledge release is active yet. Source discovery and candidate preparation do not publish entries.</p>}
      {!busy && result?.envelope.reason_code === "RECORD_NOT_FOUND" && <p>No released record matches this search. This does not mean no source record exists.</p>}
      {!busy && result?.envelope.reason_code === "RELEASE_HELD" && <p>The current knowledge release is held or withdrawn.</p>}
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
