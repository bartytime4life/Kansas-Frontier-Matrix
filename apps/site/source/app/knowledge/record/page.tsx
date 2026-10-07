"use client";

import { Suspense, useEffect, useState } from "react";
import Link from "next/link";
import { useSearchParams } from "next/navigation";
import { readKnowledge, knowledgeUnavailable, type KnowledgeResult } from "../../knowledge-read";
import styles from "../knowledge.module.css";

export default function KnowledgeRecordPage() {
  return <Suspense fallback={<main className={styles.page}><p role="status">Checking reviewed record…</p></main>}><SelectedRecord /></Suspense>;
}

function SelectedRecord() {
  const params = useSearchParams();
  const id = params.get("id") ?? "";
  return <KnowledgeRecordContent key={id} id={id} />;
}

function KnowledgeRecordContent({ id }: { id: string }) {
  const [result, setResult] = useState<KnowledgeResult | null>(null);
  const [retry, setRetry] = useState(0);
  const busy = result === null;
  useEffect(() => {
    const abort = new AbortController();
    void readKnowledge({ kind: "record", id }, abort.signal)
      .then(result => { if (!abort.signal.aborted) setResult(result); })
      .catch(() => { if (!abort.signal.aborted) setResult(knowledgeUnavailable()); });
    return () => abort.abort();
  }, [id, retry]);

  const record = result?.data?.records?.[0];
  return <main className={styles.page}>
    <header className={styles.header}><Link href="/knowledge">← Kansas knowledge</Link><span>REVIEWED RECORD</span></header>
    <div className={styles.intro}><p>KANSAS KNOWLEDGE</p><h1>{record?.title ?? "Record status"}</h1>
      <p>Only the active, reviewed release can supply this page. Named locations are source labels, not inferred boundaries or exact sites.</p></div>
    <section className={styles.results} aria-live="polite" aria-busy={busy}>
      {busy && <p>Checking reviewed record…</p>}
      {!busy && result?.envelope.reason_code === "NO_APPROVED_KNOWLEDGE" && <p>No knowledge release is active yet.</p>}
      {!busy && result?.envelope.reason_code === "RECORD_NOT_FOUND" && <p>No released record matches this identifier. A source record may still exist outside the released collection.</p>}
      {!busy && result?.envelope.reason_code === "RELEASE_HELD" && <p>The current knowledge release is held or withdrawn.</p>}
      {!busy && result?.envelope.outcome === "ERROR" && <><p>The reviewed knowledge store is unavailable.</p><button type="button" onClick={() => { setResult(null); setRetry(value => value + 1); }}>Retry record</button></>}
      {!busy && result?.envelope.reason_code === "INVALID_QUERY" && <p>The record identifier is invalid.</p>}
      {!busy && result?.envelope.reason_code === "RELEASED" && record && <article className={styles.card}>
        <div className={styles.tags}><span>{record.kind}</span><span>{record.geometry_role}</span><span>{record.time_start ? `${record.time_start}${record.time_end && record.time_end !== record.time_start ? `–${record.time_end}` : ""}` : "Time unspecified"}</span></div>
        <h2>{record.title}</h2><p>{record.summary}</p><p className={styles.place}>{record.location_label}</p>
        <div className={styles.assertions}>{record.assertions.map((item, index) => <p key={`${record.record_id}-${index}`}><strong>{item.status === "documented" ? "Documented" : item.status === "conflicting" ? "Conflicting account" : "Narrative interpretation"}</strong> {item.text}<small> Source {item.source_ref} · evidence {item.evidence_ref}</small></p>)}</div>
        <footer><a href={record.source_url} target="_blank" rel="noopener noreferrer">Official source ↗</a><small>Evidence {record.evidence_ref} · review {record.review_ref}</small></footer>
        <p className={styles.release}>Reviewed {result.data?.reviewed_at?.slice(0, 10)} · released {result.data?.released_at?.slice(0, 10)} · package {result.data?.release_id}</p>
      </article>}
    </section>
  </main>;
}
