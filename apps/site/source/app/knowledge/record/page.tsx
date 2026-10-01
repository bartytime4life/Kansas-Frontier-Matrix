"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import styles from "../knowledge.module.css";

type Assertion = { text: string; status: "documented" | "conflicting" | "narrative"; source_ref: string; evidence_ref: string };
type KnowledgeRecord = {
  record_id: string; kind: string; title: string; summary: string; location_label: string;
  geometry_role: string; time_start: string | null; time_end: string | null;
  source_url: string; source_ref: string; evidence_ref: string; review_ref: string;
  assertions: Assertion[];
};
type Result = { envelope: { outcome: string; reason_code: string }; data?: { records: KnowledgeRecord[]; release_id: string; reviewed_at: string; released_at: string } };

export default function KnowledgeRecordPage() {
  const [result, setResult] = useState<Result | null>(null);
  const [busy, setBusy] = useState(true);
  useEffect(() => {
    const abort = new AbortController();
    const id = new URLSearchParams(window.location.search).get("id") ?? "";
    setBusy(true);
    fetch(`/api/governed/v1/knowledge?id=${encodeURIComponent(id)}`, { signal: abort.signal, cache: "no-store" })
      .then(async response => {
        const body = await response.json() as Result;
        if (!response.ok && body.envelope?.reason_code !== "INVALID_QUERY") throw new Error("STORE_UNAVAILABLE");
        setResult(body);
      })
      .catch(error => { if (error.name !== "AbortError") setResult({ envelope: { outcome: "ERROR", reason_code: "STORE_UNAVAILABLE" } }); })
      .finally(() => { if (!abort.signal.aborted) setBusy(false); });
    return () => abort.abort();
  }, []);

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
      {!busy && result?.envelope.outcome === "ERROR" && <p>The reviewed knowledge store is unavailable. Try again later.</p>}
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
