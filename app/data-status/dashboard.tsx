'use client';
import { useCallback, useEffect, useRef, useState } from 'react';
import Link from 'next/link';
import { browserJsonRequest } from '../browser-json-request';
import { HostedSourceStatus } from '../hosted-source-status';
import { gigabytes, HOLD_LABELS, INTAKE_LABELS, parseCapacity, parseLocalReport, type Capacity, type LocalReport } from './model';
import styles from './dashboard.module.css';

function Usage({ used, target, label }: { used: number | null; target: number; label: string }) {
  return <div className={styles.usage}>
    <p><strong>{gigabytes(used)}</strong> <span>of {gigabytes(target)} planning ceiling</span></p>
    {used !== null && <><progress value={Math.min(used, target)} max={target} aria-label={label} />
      <p>{used > target ? `${gigabytes(used - target)} above the planning ceiling` : `${gigabytes(target - used)} below the planning ceiling`}</p></>}
  </div>;
}
export default function DataStatus() {
  const [capacity, setCapacity] = useState<Capacity | null>(null), [loading, setLoading] = useState(true), [failed, setFailed] = useState(false);
  const [local, setLocal] = useState<LocalReport | null>(null), [fileError, setFileError] = useState(''), [reading, setReading] = useState(false);
  const request = useRef<AbortController | null>(null), fileVersion = useRef(0);
  const refresh = useCallback(async () => {
    request.current?.abort(); const controller = new AbortController(); request.current = controller;
    setLoading(true); setFailed(false);
    try {
      const result = await browserJsonRequest('/api/database-capacity', { signal: controller.signal, maxBytes: 16_384, timeoutMs: 10_000 });
      if (!result.response.ok) throw new Error('Status unavailable');
      const checked = parseCapacity(result.body);
      if (!controller.signal.aborted && request.current === controller) setCapacity(checked);
    } catch { if (!controller.signal.aborted && request.current === controller) setFailed(true); }
    finally { if (!controller.signal.aborted && request.current === controller) setLoading(false); }
  }, []);
  useEffect(() => { void refresh(); return () => { request.current?.abort(); fileVersion.current++; }; }, [refresh]);
  const openReport = async (file: File | undefined) => {
    const version = ++fileVersion.current;
    setFileError(''); setReading(Boolean(file));
    if (!file) return;
    try {
      if (file.size > 65_536) throw new Error('Report too large');
      const checked = parseLocalReport(JSON.parse(await file.text()));
      if (version === fileVersion.current) setLocal(checked);
    } catch { if (version === fileVersion.current) setFileError('That file is not a supported status report. Any previously opened report remains below.'); }
    finally { if (version === fileVersion.current) setReading(false); }
  };
  return <main className={styles.page}>
    <Link href="/?layers=sources">← Sources on the map</Link>
    <h1>Database &amp; intake status</h1>
    <p className={styles.intro}>Check hosted storage and capture review separately from the data on your PC. Each measurement keeps its own date and scope.</p>
    <div className={styles.grid}>
      <section className={styles.card} aria-labelledby="hosted-sql-title" aria-busy={loading}>
        <p className={styles.eyebrow}>HOSTED WEBSITE</p><h2 id="hosted-sql-title">SQL database</h2>
        <p role="status">{loading ? 'Checking database metadata…' : failed ? 'Current measurement unknown. Any retained figures are from the previous check.' : capacity?.state === 'measured' ? 'Database metadata checked' : 'Database usage unknown. The server connection or metadata access needs attention.'}</p>
        <Usage used={capacity?.usedBytes ?? null} target={capacity?.targetBytes ?? 85_000_000_000} label="Estimated hosted table and index usage" />
        <dl className={styles.metrics}><div><dt>Visible tables</dt><dd>{capacity?.tables?.toLocaleString() ?? 'Unknown'}</dd></div><div><dt>Estimated rows</dt><dd>{capacity?.estimatedRows?.toLocaleString() ?? 'Unknown'}</dd></div></dl>
        {capacity && <p className={styles.note}>{failed ? 'Previous check' : 'Checked'} <time dateTime={capacity.checkedAt}>{capacity.checkedAt}</time></p>}
        <p className={styles.note}>Estimates cover tables and indexes visible to the app’s database account. They exclude backups, logs and other hosting files. The planning ceiling is not a verified hosting quota or a write limit.</p>
        <button type="button" onClick={() => void refresh()} disabled={loading}>{loading ? 'Checking…' : 'Refresh database status'}</button>
      </section>
      <section className={styles.card} aria-labelledby="local-data-title">
        <p className={styles.eyebrow}>LOCAL PC · PRIVATE REPORT</p><h2 id="local-data-title">Local database &amp; intake</h2>
        <p>This website cannot inspect the PC from your phone. Open a status report generated on that PC to view its recorded measurements here.</p>
        <label className={styles.file}>Open local status report<input type="file" accept="application/json,.json" onChange={event => { void openReport(event.target.files?.[0]); event.target.value = ''; }} /></label>
        <p className={styles.note}>The report stays in this browser tab. It is not uploaded or saved by this page.</p>
        {reading && <p role="status">Reading report…</p>}{fileError && <p role="alert">{fileError}</p>}
        {local ? <>
          <p>Recorded <time dateTime={local.checkedAt}>{local.checkedAt}</time> · not a live PC connection</p>
          <Usage used={local.sql.usedBytes} target={local.sql.targetBytes} label="Recorded local SQL file usage" />
          <p className={styles.note}>{local.sql.catalogCount ?? 'Unknown'} selected catalogs; {gigabytes(local.sql.journalBytes)} in journal and shared-memory files. Exports, backups and unselected databases are excluded.</p>
          <h3>Intake · {local.intake.files?.toLocaleString() ?? 'Unknown'} indexed files</h3>
          {local.intake.counts ? <dl className={styles.metrics}>{Object.entries(INTAKE_LABELS).map(([key, label]) => <div key={key}><dt>{label}</dt><dd>{local.intake.counts![key as keyof typeof INTAKE_LABELS].toLocaleString()}</dd></div>)}</dl> : <p>Intake could not be measured on the PC.</p>}
          <h3>Reported review and sharing holds</h3>
          {local.intake.holds.length ? <ul>{local.intake.holds.map(hold => <li key={hold.code}><strong>{hold.files.toLocaleString()} files:</strong> {HOLD_LABELS[hold.code]}</li>)}</ul> : <p>No specific hold details are included in this report.</p>}
          <p className={styles.note}>One file can have several holds. Local review and stored bytes do not establish approval for public map display.</p>
          <button type="button" onClick={() => { fileVersion.current++; setLocal(null); setFileError(''); setReading(false); }}>Clear local report</button>
        </> : <p role="status">Local database size and intake counts: unknown until a report is opened.</p>}
        <details><summary>How to create a status report</summary><p>On the operator PC, run the repository’s <code>scripts/pc-pipeline/data-status.mjs</code> with the intake index and the SQL catalogs you want measured. See the database status guide in the repository. The report contains totals and fixed hold categories, without file paths or source records.</p></details>
      </section>
    </div>
    <div className={styles.archive}><HostedSourceStatus /></div>
    <p><Link href="/pipelines">Source coverage by map topic →</Link></p>
  </main>;
}
