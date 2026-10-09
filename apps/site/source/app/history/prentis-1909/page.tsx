"use client";
import { useEffect, useMemo, useState } from "react";
import { historyParagraphs, searchHistory, readHistoryText, OCR_PAGE_SIZE } from "../../history-reader-model";
import s from "../../downloads/workspace.module.css";
import h from "../../history.module.css";

export default function HistoryReader() {
  const [text, setText] = useState(""), [error, setError] = useState(""), [query, setQuery] = useState(""), [page, setPage] = useState(0), [attempt, setAttempt] = useState(0);
  useEffect(() => { const controller = new AbortController(); setError(""); fetch("/history/prentis-1909.txt", { signal: controller.signal }).then(readHistoryText).then(value => { if (!controller.signal.aborted) setText(value); }).catch(reason => { if (!controller.signal.aborted) setError(reason instanceof Error ? reason.message : "Unable to load the text."); }); return () => controller.abort(); }, [attempt]);
  const paragraphs = useMemo(() => historyParagraphs(text), [text]), results = useMemo(() => searchHistory(paragraphs, query), [paragraphs, query]);
  const pages = Math.max(1, Math.ceil(results.length / OCR_PAGE_SIZE)), current = Math.min(page, pages - 1);
  return <main className={s.page}><div className={s.wrap}><div className={h.reader}>
    <nav aria-label="History navigation"><a href="/downloads#history">← History &amp; archives</a><a href="https://archive.org/details/historyofkansas00pren_0" target="_blank" rel="noreferrer">View scanned pages ↗</a><a href="/history/prentis-1909.txt" download>Save full OCR text · 740 KiB</a></nav>
    <p className={s.eyebrow}>KANSAS HISTORICAL REFERENCE · 1909</p><h1>A history of Kansas</h1><p>Noble L. Prentis · edited and revised by Henrietta V. Race · published by Caroline Prentis, Topeka.</p>
    <p className={s.alert}>This is an uncorrected historical text, with period biases, omissions and OCR errors. It is not a modern factual assessment. Verify quotations and printed page numbers against the scan. Paragraph numbers below identify OCR passages, not book pages.</p>
    <label>Search the complete text<input type="search" value={query} onChange={event => { setQuery(event.target.value); setPage(0); }} placeholder="Search a place, person or event…" /></label>
    <output aria-live="polite">{text ? `${results.length.toLocaleString()} ${query.trim() ? "matching" : "total"} passages · page ${current + 1} of ${pages}` : error ? "Text unavailable" : "Loading 740 KiB of verified text…"}</output>
    {error && <p role="alert">{error} <button type="button" onClick={() => setAttempt(value => value + 1)}>Retry loading</button></p>}
    {text && !results.length && <p>No passages match all your search words. Try fewer words or a different spelling.</p>}
    {text && <><nav aria-label="Text pages"><button type="button" disabled={!current} onClick={() => setPage(current - 1)}>Previous passages</button><button type="button" disabled={current + 1 >= pages} onClick={() => setPage(current + 1)}>Next passages</button></nav><article aria-label="Historical OCR passages">{results.slice(current * OCR_PAGE_SIZE, (current + 1) * OCR_PAGE_SIZE).map(row => <section key={row.number}><small>OCR passage {row.number}</small><p>{row.text}</p></section>)}</article></>}
    <details><summary>Source and preservation</summary><p>Digitized copy contributed by the Library of Congress through Internet Archive. The archive records a 1909 publication and a statement that the Library of Congress is unaware of copyright restrictions. The OCR is reproduced unchanged, with a verified SHA-256 checksum. Downloads of the original PDF are available from History &amp; archives.</p><a href="/history/prentis-1909-provenance.json" download>Download provenance &amp; checksums</a></details>
  </div></div></main>;
}
