"use client";
import { useState } from "react";
import styles from "./workspace.module.css";

export default function StoragePanel() {
  const [first, setFirst] = useState('nws-alerts');
  const [releases, setReleases] = useState(1);
  const [mib, setMib] = useState(8);
  const policy = { storagePolicy: { priority: first === 'nws-alerts' ? ['nws-alerts', 'usgs-streamflow'] : ['usgs-streamflow', 'nws-alerts'], maxPublicationsPerTick: releases, maxBytesPerTick: mib * 1024 ** 2 } };
  return <section className={styles.panel} aria-labelledby="storage-heading">
    <h2 id="storage-heading">PC storage &amp; GoDaddy publication</h2>
    <p>Keep full captures and processing history on the development PC. Send approved, compact results to GoDaddy so visitors can read published information without waiting for the PC.</p>
    <div className={styles.table} role="region" aria-label="Data placement" tabIndex={0}><table><thead><tr><th>Priority</th><th>Information</th><th>Location</th></tr></thead><tbody>
      <tr><td>Serve visitors first</td><td>Current approved results, release identities and provenance</td><td>GoDaddy</td></tr>
      <tr><td>Bounded publication</td><td>Approved NWS context and USGS observations; reviewed water/weather packages</td><td>Compact projections on GoDaddy; originals on the PC</td></tr>
      <tr><td>Keep local</td><td>Raw archives, processing intermediates, private records and the SQLite job queue</td><td>Development PC, with independent private backups</td></tr>
    </tbody></table></div>
    <h3>Prepare a publication budget</h3>
    <p>These controls prepare a configuration snippet only. They do not change a running worker, enable publication, or approve data. The automatic worker currently supports NWS and USGS; other pipelines need separate release integrations.</p>
    <div className={styles.controls}>
      <label>Publish first<select value={first} onChange={e => setFirst(e.target.value)}><option value="nws-alerts">NWS weather context</option><option value="usgs-streamflow">USGS streamflow observations</option></select></label>
      <label>Release attempts per run<select value={releases} onChange={e => setReleases(Number(e.target.value))}><option value={1}>1 — conservative</option><option value={2}>2</option></select></label>
      <label>Payload budget per run<select value={mib} onChange={e => setMib(Number(e.target.value))}>{[1,2,4,8,16].map(n => <option key={n} value={n}>{n} MiB</option>)}</select></label>
    </div>
    <p role="status">Draft only: up to {releases} release attempt{releases === 1 ? '' : 's'} and {mib} MiB of normalized payload per run. A single product remains limited to 8 MiB. HTTP overhead, stored history and database indexes use additional space.</p>
    <label>Configuration snippet<textarea readOnly rows={12} value={JSON.stringify(policy, null, 2)} style={{ width: '100%', maxWidth: 640 }} /></label>
    <details><summary>Apply and inspect on the development PC</summary>
      <p>Merge the storagePolicy property into the existing private worker configuration, preserving its paths, mount identity and publication setting. Validate before the next timer run:</p>
      <pre style={{ whiteSpace: 'pre-wrap', overflowWrap: 'anywhere' }}>node scripts/pc-pipeline/cli.mjs plan /etc/kfm-pipeline/config.json{ '\n' }node scripts/pc-pipeline/cli.mjs status /etc/kfm-pipeline/config.json</pre>
      <p>The plan validates settings without contacting GoDaddy. Status checks local storage and shows the latest 100 journal entries, including deferred reasons and retry times. Neither command proves remote capacity or successful publication.</p>
    </details>
    <p>Hosting unavailable or budget reached: collection stays local and eligible current-hour candidates retry on later runs. Older captures remain private; there is no automatic historical catch-up or deletion. A product larger than the chosen budget remains deferred until the budget is raised or a smaller approved product is prepared.</p>
    <p>Hosting capacity and live synchronization are not established by this planner. <a href="/api/pipeline-status">Inspect the current public pipeline status</a> · <a href="/curated">Browse published snapshots</a></p>
  </section>;
}
