"use client";
import { useEffect, useRef, useState } from "react";
import { automaticLocalConnection, formatDownloadBytes as bytes, localDownloadRequest } from "./local-download-client";
import { cacheBudgetBytes, cacheBudgetError, cacheBudgetGb, parseCacheBudget, type CacheBudget } from "./cache-budget";
import styles from "./local-cache-settings.module.css";

export default function LocalCacheSettings({ onSaved }: { onSaved?: () => void }) {
  const [saved, setSaved] = useState<CacheBudget | null>(null), [draft, setDraft] = useState("");
  const [busy, setBusy] = useState(false), [notice, setNotice] = useState("");
  const life = useRef<AbortController | null>(null), operating = useRef(false);
  const proposed = cacheBudgetBytes(draft);
  async function request(save = false) {
    const controller = life.current;
    if (!controller || controller.signal.aborted || operating.current || save && (!saved || proposed === null)) return;
    operating.current = true; setBusy(true); setNotice("");
    try {
      const { response, body } = await localDownloadRequest("/cache-budget", controller.signal,
        save ? { limitBytes: proposed } : undefined, save ? saved?.sessionToken : undefined);
      const parsed = parseCacheBudget(body);
      if (!response.ok || !parsed) throw new Error(cacheBudgetError((body as { error?: unknown })?.error));
      if (controller.signal.aborted) return;
      setSaved(parsed); setDraft(cacheBudgetGb(parsed.limitBytes));
      setNotice(save ? `Saved ${cacheBudgetGb(parsed.limitBytes)} GB on this computer. Existing files are retained.` : "Saved budget refreshed.");
      if (save) onSaved?.();
    } catch (error) {
      if (!controller.signal.aborted) setNotice(error instanceof Error && /^(Wait for|Enter a|The budget)/.test(error.message) ? error.message : cacheBudgetError(null));
    } finally { if (life.current === controller) { operating.current = false; if (!controller.signal.aborted) setBusy(false); } }
  }
  useEffect(() => {
    life.current = new AbortController(); operating.current = false;
    if (automaticLocalConnection(window.location.origin)) void request();
    return () => { life.current?.abort(); };
  }, []);
  return <section id="cache-budget" className={styles.card} aria-labelledby="cache-budget-heading">
    <div className={styles.heading}><div><h2 id="cache-budget-heading">Local cache budget</h2><p>Choose how much space the replaceable cache may use. 500 GB is the default; you can go higher or lower.</p></div><button type="button" disabled={busy} onClick={() => void request()}>{busy ? "Checking…" : saved ? "Refresh budget" : "Connect to this computer"}</button></div>
    {saved && <>
      <dl className={styles.stats}><div><dt>Saved budget</dt><dd>{cacheBudgetGb(saved.limitBytes)} GB</dd></div><div><dt>Replaceable cache use</dt><dd>{bytes(saved.usedBytes)}</dd></div><div><dt>Disk space available</dt><dd>{bytes(saved.freeBytes)}</dd></div></dl>
      <form className={styles.form} onSubmit={event => { event.preventDefault(); void request(true); }}>
        <label htmlFor="local-cache-gb">Cache budget (GB)<input id="local-cache-gb" type="text" inputMode="decimal" value={draft} disabled={busy} onChange={event => setDraft(event.target.value)} aria-invalid={proposed === null} aria-describedby="cache-budget-help" /></label>
        <button type="submit" disabled={busy || proposed === null || proposed === saved.limitBytes}>{busy ? "Saving…" : "Save cache budget"}</button>
      </form>
      <p id="cache-budget-help">GB uses decimal bytes. This budget also sets the maximum allowed for a single selected download. Changes apply to new selections; active and queued transfers keep their chosen limits. Downloads still check available disk space. Protected originals, evidence, backups, and basemap tiles are tracked separately.</p>
      {proposed === null && <p role="alert">Enter a positive size in GB, for example 250, 1000, or 2000.</p>}
      {proposed !== null && proposed < saved.usedBytes && <p role="status">The cache is above this budget. Existing files will stay; new cache transfers wait until there is room or you raise the budget.</p>}
      {proposed !== null && proposed > saved.freeBytes + saved.usedBytes && <p>This budget exceeds currently available space. It does not reserve disk space; transfers stop when free capacity is insufficient.</p>}
    </>}
    {!saved && <p>Connect to the local download service to read and save this computer’s budget.</p>}
    <p className={styles.notice} role="status" aria-live="polite">{notice}</p>
  </section>;
}
