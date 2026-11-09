"use client";
import { useCallback, useEffect, useRef, useState } from "react";
import Link from "next/link";
import { DATA_SOURCES, MAX_UPLOAD_BYTES, REVIEW_LABELS, UPLOAD_EXTENSIONS, type Review, type ReviewState, type Submission } from "../data-intake";
import styles from "./workspace.module.css";

type Detail = { submission: Submission; reviews: Review[]; canReview: boolean };
type ReviewReceipt = { id: string; title: string; status: ReviewState; version: number; note: string; refreshing: boolean; refreshError: string };
export default function DataWorkspace({ mode, name, steward, initialSourceId = "general" }: { initialSourceId?: string; mode: "submit" | "review"; name: string; steward: boolean }) {
  const [items, setItems] = useState<Submission[]>([]), [nextCursor, setNextCursor] = useState<string | null>(null);
  const [message, setMessage] = useState(""), [listError, setListError] = useState("");
  const [busy, setBusy] = useState(false), [loading, setLoading] = useState(true), [detailLoading, setDetailLoading] = useState(false);
  const [detail, setDetail] = useState<Detail | null>(null), [decision, setDecision] = useState<ReviewState>("under_review"), [note, setNote] = useState("");
  const [reviewReceipt, setReviewReceipt] = useState<ReviewReceipt | null>(null);
  const [filter, setFilter] = useState("all"), [sourceId, setSourceId] = useState(() => DATA_SOURCES.some((source) => source.id === initialSourceId) ? initialSourceId : "general"), [fileName, setFileName] = useState("");
  const formRef = useRef<HTMLFormElement>(null), requestId = useRef(0), listRequestId = useRef(0), draftRevision = useRef(0), reviewOperation = useRef(0), acknowledgedVersions = useRef(new Map<string, number>()), mounted = useRef(true), detailRequest = useRef<AbortController | null>(null);
  useEffect(() => { mounted.current = true; return () => { mounted.current = false; detailRequest.current?.abort(); }; }, []);
  const loadList = useCallback((before?: string, signal?: AbortSignal) => {
    const generation = ++listRequestId.current;
    const params = new URLSearchParams({ scope: mode === "review" ? "review" : "mine" });
    if (before) params.set("before", before);
    return fetch(`/api/data-submissions?${params}`, { cache: "no-store", signal }).then(async (response) => {
      const body = await response.json();
      if (!response.ok) throw new Error(body.error ?? "Submissions could not be loaded.");
      if (!mounted.current || signal?.aborted || generation !== listRequestId.current) return;
      setListError("");
      setItems((previous) => before ? [...previous, ...body.items] : body.items);
      setNextCursor(body.nextCursor);
    }).catch((error) => {
      if (mounted.current && !signal?.aborted && generation === listRequestId.current) setListError(error instanceof Error ? error.message : "Submissions could not be loaded.");
    }).finally(() => {
      if (mounted.current && !signal?.aborted && generation === listRequestId.current) setLoading(false);
    });
  }, [mode]);
  useEffect(() => { const controller = new AbortController(); void loadList(undefined, controller.signal); return () => controller.abort(); }, [loadList]);
  const refreshList = (before?: string) => { setLoading(true); setListError(""); return loadList(before); };
  const openDetail = async (id: string) => {
    detailRequest.current?.abort(); const controller = new AbortController(); detailRequest.current = controller;
    const generation = ++requestId.current; ++draftRevision.current; setDetailLoading(true); setDetail(null); setMessage(""); setNote(""); setDecision("under_review");
    try { const response = await fetch(`/api/data-submissions/${id}`, { cache: "no-store", signal: controller.signal }); const body = await response.json(); if (!response.ok) throw new Error(body.error); if (body.submission?.id !== id || body.submission.version < (acknowledgedVersions.current.get(id) ?? 0)) throw new Error("These details could not be confirmed against the recorded review. Reopen this submission to try again."); if (!controller.signal.aborted && generation === requestId.current) { setDetail(body); setDecision(body.submission.status === "under_review" ? "changes_requested" : "under_review"); } }
    catch (error) { if (!controller.signal.aborted && generation === requestId.current) setMessage((error as Error).message); }
    finally { if (!controller.signal.aborted && generation === requestId.current) setDetailLoading(false); if (detailRequest.current === controller) detailRequest.current = null; }
  };
  const submit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault(); setBusy(true); setMessage("");
    const form = event.currentTarget; const data = new FormData(form); const file = data.get("file");
    if (!(file instanceof File) || !file.size || file.size > MAX_UPLOAD_BYTES) { setMessage("Choose a file no larger than 10 MB."); setBusy(false); return; }
    try { const response = await fetch("/api/data-submissions", { method: "POST", body: data }); const body = await response.json(); if (!response.ok) throw new Error(body.error); form.reset(); setSourceId("general"); setFileName(""); await refreshList(); await openDetail(body.id); setMessage("Submission received. Your file is stored for steward review."); }
    catch (error) { setMessage((error as Error).message || "The upload could not be saved. Your form has been kept."); }
    finally { setBusy(false); }
  };
  const review = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault(); if (!detail || busy || decision === detail.submission.status) return;
    const target = detail.submission, selection = requestId.current, draft = draftRevision.current, operation = ++reviewOperation.current, submittedNote = note.trim();
    setBusy(true); setMessage("");
    try {
      const response = await fetch(`/api/data-submissions/${target.id}`, { method: "PATCH", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ status: decision, note, version: target.version }) });
      const body = await response.json(); if (!response.ok) throw new Error(body.error); if (!mounted.current) return;
      const receipt: ReviewReceipt = { id: target.id, title: target.title, status: body.status, version: body.version, note: submittedNote, refreshing: true, refreshError: "" };
      acknowledgedVersions.current.set(target.id, Math.max(acknowledgedVersions.current.get(target.id) ?? 0, receipt.version));
      setReviewReceipt(receipt); setBusy(false);
      setDetail(current => current?.submission.id === target.id && current.submission.version <= receipt.version ? { ...current, submission: { ...current.submission, status: receipt.status, version: receipt.version } } : current);
      if (selection === requestId.current) {
        if (draft === draftRevision.current) { setNote(""); setDecision(receipt.status === "under_review" ? "changes_requested" : "under_review"); }
      }
      void refreshList();
      if (selection === requestId.current) {
        const controller = new AbortController(); detailRequest.current?.abort(); detailRequest.current = controller;
        try {
          const fresh = await fetch(`/api/data-submissions/${target.id}`, { cache: "no-store", signal: controller.signal });
          const updated: Detail = await fresh.json();
          if (!fresh.ok || updated.submission?.id !== target.id || updated.submission.version < receipt.version) throw new Error("The refreshed details could not be confirmed.");
          if (!controller.signal.aborted && selection === requestId.current) setDetail(current => current?.submission.id === target.id && current.submission.version <= updated.submission.version ? updated : current);
        } catch {
          if (!controller.signal.aborted && mounted.current) setReviewReceipt(current => current?.id === target.id && current.version === receipt.version ? { ...current, refreshError: "The review was recorded, but refreshed details could not be loaded. Reopen this submission to check its review history before another decision." } : current);
        } finally { if (detailRequest.current === controller) detailRequest.current = null; }
      }
      if (mounted.current) setReviewReceipt(current => current?.id === target.id && current.version === receipt.version ? { ...current, refreshing: false } : current);
    } catch (error) { if (mounted.current && operation === reviewOperation.current) setMessage((error as Error).message || "The review could not be recorded. Your note has been kept."); }
    finally { if (mounted.current && operation === reviewOperation.current) setBusy(false); }
  };
  const rows = items.filter((item) => filter === "all" || item.status === filter);
  return <main className={styles.page}>
    <header className={styles.header}><Link href="/" className={styles.brand}>KFM <span>Data commons</span></Link><nav aria-label="Data navigation"><Link href="/">Back to map</Link><Link href="/data" aria-current={mode === "submit" ? "page" : undefined}>Contribute data</Link><Link href="/data/land-records">Land records</Link>{steward && <Link href="/stewards" aria-current={mode === "review" ? "page" : undefined}>Steward desk</Link>}</nav><span className={styles.identity}>{name}</span></header>
    <section className={styles.intro}><p className={styles.eyebrow}>{mode === "review" ? "STEWARDSHIP" : "GROW THE KANSAS RECORD"}</p><h1>{mode === "review" ? "Review proposed data" : "Bring your data to KFM"}</h1><p>{mode === "review" ? "Inspect each file, its source and reuse terms. Record a decision that the contributor can follow." : "Propose a new source, fill a historical gap, or send an update to an existing layer."}</p></section>
    {message && <div className={styles.notice} role="status">{message}</div>}
    {reviewReceipt && <div className={styles.notice} role="status"><strong>Review recorded for {reviewReceipt.title} · version {reviewReceipt.version}.</strong><p>{REVIEW_LABELS[reviewReceipt.status]} · {reviewReceipt.note}</p><p>{reviewReceipt.refreshing ? "Refreshing review history…" : "The contributor can see the recorded decision and note. Map integration remains a separate step."}</p></div>}
    {reviewReceipt?.refreshError && <p className={styles.notice} role="alert">{reviewReceipt.refreshError}</p>}
    <div className={styles.layout}>
      {mode === "submit" && <section className={styles.card}><h2>Propose a dataset</h2><p>Files stay in a private review area. Acceptance prepares a candidate for integration; it does not publish it on the map.</p>
        <form ref={formRef} onSubmit={submit} className={styles.form}>
          <label className={styles.upload}>Choose a data file <strong>{fileName || "Browse files · up to 10 MB"}</strong><input type="file" name="file" required accept={UPLOAD_EXTENSIONS.map((ext) => `.${ext}`).join(",")} onChange={(event) => setFileName(event.target.files?.[0]?.name ?? "")} /><small>CSV, GeoJSON, KML, GeoPackage, GeoTIFF, NetCDF, spreadsheets, documents, or ZIP bundles. Files are stored for inspection, not executed.</small></label>
          <label>Dataset title<input name="title" required minLength={3} maxLength={160} placeholder="e.g. Ellsworth County stream readings, 1985–1994" /></label>
          <label>Related source or layer<select name="sourceId" value={sourceId} onChange={(event) => setSourceId(event.target.value)}>{DATA_SOURCES.map((s) => <option key={s.id} value={s.id}>{s.title}</option>)}</select></label>
          <label>Source or download link<input name="sourceUrl" type="url" maxLength={1500} placeholder="https://…" /></label>
          <div className={styles.fieldPair}><label>Coverage starts<input type="date" name="startDate" /></label><label>Coverage ends<input type="date" name="endDate" /></label></div>
          <label>What does the data contain?<textarea name="description" required minLength={10} maxLength={6000} rows={4} placeholder="Geography, measurements, format, units, missing values, and what this adds or corrects. For a revision, include the earlier submission ID." /></label>
          <label>Reuse terms / license<input name="license" required maxLength={1000} placeholder="e.g. US public domain, CC BY 4.0, or Unknown" /></label>
          <label>Sensitivity<select name="sensitivity" defaultValue="unknown"><option value="unknown">Needs steward assessment</option><option value="public">Public data · no protected detail</option><option value="restricted">Restricted / sensitive material</option></select></label>
          <label className={styles.check}><input name="permission" type="checkbox" value="yes" required /><span>I have permission to share this file with KFM stewards for review.</span></label>
          <button className={styles.primary} disabled={busy} type="submit">{busy ? "Saving submission…" : "Submit for review"}</button>
        </form>
      </section>}
      <section className={styles.card}><div className={styles.sectionHeading}><h2>{mode === "review" ? "Review queue" : "Your submissions"}</h2><button onClick={() => void refreshList()} disabled={loading}>Refresh</button></div>
        <label className={styles.filter}>Status<select value={filter} onChange={(e) => setFilter(e.target.value)}><option value="all">All statuses</option>{Object.entries(REVIEW_LABELS).map(([value,label]) => <option key={value} value={value}>{label}</option>)}</select></label>
        {listError && <p role="alert">{listError}</p>}{loading && !items.length && <p role="status">Loading submissions…</p>}
        {!loading && !listError && !rows.length && <div className={styles.empty}><strong>{items.length ? "No submissions with this status" : "No submissions yet"}</strong><p>{mode === "review" ? "New proposals will arrive here with their file, source details, and review history." : "Your saved proposals and steward feedback will appear here."}</p></div>}
        <ul className={styles.items}>{rows.map((item) => <li key={item.id}><button onClick={() => void openDetail(item.id)} aria-pressed={detail?.submission.id === item.id}><span className={styles.badge} data-state={item.status}>{REVIEW_LABELS[item.status]}</span><strong>{item.title}</strong><span>{DATA_SOURCES.find((s) => s.id === item.sourceId)?.title} · {new Date(item.createdAt).toLocaleDateString()}</span><small>{item.fileName} · {(item.fileBytes / 1024).toFixed(0)} KB{mode === "review" && ` · ${item.ownerName}`}</small></button></li>)}</ul>
        {nextCursor && <button disabled={loading} onClick={() => void refreshList(nextCursor)}>Load older submissions</button>}
      </section>
      {(detail || detailLoading) && <section className={`${styles.card} ${styles.detail}`} aria-label="Submission details"><div className={styles.sectionHeading}><h2>Submission details</h2><button onClick={() => { ++requestId.current; detailRequest.current?.abort(); setDetail(null); setDetailLoading(false); }}>Close</button></div>
        {detailLoading ? <p role="status">Loading details…</p> : detail && <><span className={styles.badge} data-state={detail.submission.status}>{REVIEW_LABELS[detail.submission.status]}</span><h3>{detail.submission.title}</h3><p className={styles.prewrap}>{detail.submission.description}</p><dl className={styles.metadata}>
          <div><dt>Submitted by</dt><dd>{detail.submission.ownerName}</dd></div><div><dt>Source</dt><dd>{detail.submission.sourceUrl ? <a href={detail.submission.sourceUrl} target="_blank" rel="noreferrer">Open source ↗</a> : "Not supplied"}</dd></div><div><dt>Coverage</dt><dd>{detail.submission.startDate || "Unknown start"} → {detail.submission.endDate || "Unknown end"}</dd></div><div><dt>Reuse terms</dt><dd>{detail.submission.license}</dd></div><div><dt>Sensitivity</dt><dd>{detail.submission.sensitivity}</dd></div><div><dt>Submission ID</dt><dd>{detail.submission.id}</dd></div><div><dt>SHA-256</dt><dd>{detail.submission.fileSha256}</dd></div>
        </dl><a className={styles.download} href={`/api/data-submissions/${detail.submission.id}?download=1`}>Download submitted file · {(detail.submission.fileBytes / 1024).toFixed(0)} KB</a><p className={styles.muted}>This is an unvalidated contribution. Download it only if you trust its source.</p>
          <h3>Review history</h3>{reviewReceipt?.id === detail.submission.id && !detail.reviews.some(item => item.version >= reviewReceipt.version) ? <p>The latest review is acknowledged above. Reopen this submission if its history entry has not loaded.</p> : !detail.reviews.length && <p>Awaiting a steward’s first review.</p>}<ol className={styles.history}>{detail.reviews.map((review) => <li key={review.id}><strong>{REVIEW_LABELS[review.status]}</strong><small>{review.reviewerName} · {new Date(review.createdAt).toLocaleString()}</small><p className={styles.prewrap}>{review.note}</p></li>)}</ol>
          {mode === "review" && detail.canReview && <form onSubmit={review} className={styles.form}><h3>Record a review</h3><label>Decision<select value={decision} onChange={(e) => { ++draftRevision.current; setDecision(e.target.value as ReviewState); }}>{Object.entries(REVIEW_LABELS).filter(([value]) => value !== "submitted" && (value !== detail.submission.status || value === decision)).map(([value,label]) => <option key={value} value={value} disabled={value === detail.submission.status}>{label}</option>)}</select></label><label>Review note<textarea required minLength={10} maxLength={4000} rows={4} value={note} onChange={(e) => { ++draftRevision.current; setNote(e.target.value); }} placeholder="Record source checks, format/quality findings, reuse and sensitivity checks, and the next action." /></label><p className={styles.muted}>Acceptance requires public sensitivity, stated reuse terms, and a source link. Map integration remains a separate step.</p>{decision === detail.submission.status && <p>Choose a different decision before saving another review. Your newer note has been kept.</p>}<button className={styles.primary} disabled={busy || decision === detail.submission.status} type="submit">{busy ? "Saving review…" : "Save review"}</button></form>}
        </>}
      </section>}
    </div>
  </main>;
}
