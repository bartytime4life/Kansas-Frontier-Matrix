'use client';

import { useRef, useState } from 'react';
import { importNotebook, previewNotebookImport, sourceBindingsMatch } from './notebook.mjs';
import { currentSourceBindings } from './investigation-state.mjs';
import styles from './NotebookTransfer.module.css';

const LIMIT = 2 * 1024 * 1024;
const number = new Intl.NumberFormat('en-US');

function PreviewRecord({ entry }) {
  const current = currentSourceBindings(entry.workspace), sourceIds = [...new Set([...Object.keys(entry.sourceBindings), ...Object.keys(current)])];
  return <li><strong>{entry.title}</strong><small>{entry.workspace === 'county' ? 'County Observatory' : 'Signal Studio'} · {sourceBindingsMatch(entry.sourceBindings, current) ? 'Sources match' : 'Sources changed'}{entry.privateData ? ` · private CSV: ${entry.privateData.fileName}` : ''}</small>
    <details className={styles.record}><summary>Inspect exact sources{entry.privateData ? ' + private attachment' : ''}</summary>
      <div className={styles.sourceRecords}>{sourceIds.map(id => <section key={id} data-changed={entry.sourceBindings[id] !== current[id]}><h4>{id}</h4><dl><div><dt>Saved SHA-256</dt><dd>{entry.sourceBindings[id] ? <code>{entry.sourceBindings[id]}</code> : 'Not included in the saved investigation'}</dd></div><div><dt>Current SHA-256</dt><dd>{current[id] ? <code>{current[id]}</code> : 'Not included in the current workspace'}</dd></div></dl></section>)}</div>
      {entry.privateData && <section className={styles.attachment}><h4>Private county attachment</h4><dl><div><dt>Filename</dt><dd>{entry.privateData.fileName}</dd></div><div><dt>County rows</dt><dd>{number.format(entry.privateData.rows.length)}</dd></div><div><dt>Numeric measures</dt><dd>{entry.privateData.columns.length} · {entry.privateData.columns.map(column => column.label).join(', ')}</dd></div><div><dt>File bytes</dt><dd>{number.format(entry.privateData.bytes)}</dd></div><div><dt>Saved file SHA-256</dt><dd><code>{entry.privateData.sha256}</code></dd></div></dl><p>Only attachment metadata is shown here. Import stores its county values in this browser; no private values enter a URL.</p></section>}
    </details>
  </li>;
}

export default function NotebookTransfer({ onChange }) {
  const [preview, setPreview] = useState(null), [status, setStatus] = useState(''), [reading, setReading] = useState(false);
  const fileInput = useRef(null), request = useRef(0);
  const readFile = async event => {
    const file = event.target.files?.[0], nextRequest = ++request.current;
    setPreview(null); setStatus(''); setReading(false);
    if (!file) return;
    if (file.size > LIMIT) { setStatus('Choose a science notebook JSON file of 2 MB or less.'); return; }
    setReading(true);
    try {
      const text = await file.text();
      if (request.current !== nextRequest) return;
      const result = previewNotebookImport(text);
      setPreview({ ...result, text, fileName: file.name.slice(0, 160) });
    } catch (error) { if (request.current === nextRequest) setStatus(error.message || 'This file could not be read as a science notebook.'); }
    finally { if (request.current === nextRequest) setReading(false); }
  };
  const cancel = () => { request.current++; setPreview(null); setStatus(''); setReading(false); if (fileInput.current) fileInput.current.value = ''; };
  const importFile = () => {
    if (!preview) return;
    try {
      const result = importNotebook(preview.text);
      setStatus(`Added ${result.added} investigation${result.added === 1 ? '' : 's'}. ${result.duplicates} duplicate${result.duplicates === 1 ? '' : 's'} skipped. Your existing notebook was kept.`);
      setPreview(null); if (fileInput.current) fileInput.current.value = ''; onChange?.();
    } catch (error) { setStatus(error.message || 'The notebook could not be added. Your existing entries were kept.'); }
  };
  const changed = preview?.entries.filter(entry => !sourceBindingsMatch(entry.sourceBindings, currentSourceBindings(entry.workspace))).length || 0;
  return <section className={styles.transfer} aria-label="Import a science notebook">
    <div className={styles.heading}><div><h3>Bring your research with you.</h3><p>Import a downloaded science notebook into this browser. Review it before adding anything.</p></div><label className={styles.file}>Choose notebook JSON<input ref={fileInput} type="file" accept=".json,application/json" aria-label="Choose science notebook JSON to preview" onChange={readFile}/></label></div>
    <p className={styles.boundary}>County Observatory + Signal Studio · JSON files up to 2 MB · 12 investigations and 512 KB of stored data in total. Import adds entries and never clears your notebook.</p>
    {reading && <p role="status" className={styles.message}>Reading and validating the notebook…</p>}
    {preview && <div className={styles.preview}>
      <div className={styles.previewHead}><span>IMPORT PREVIEW</span><strong>{preview.fileName}</strong></div>
      <dl className={styles.counts}><div><dt>New entries</dt><dd>{preview.additions}</dd></div><div><dt>Duplicates skipped</dt><dd>{preview.duplicates}</dd></div><div><dt>Private attachments</dt><dd>{preview.privateAttachments}</dd></div><div><dt>Changed sources</dt><dd>{changed}</dd></div></dl>
      {!!preview.privateAttachments && <p className={styles.warning}>This file includes private county values. Adding it stores those values in this browser. They stay out of share links.</p>}
      {!!changed && <p className={styles.warning}>Some saved source fingerprints differ from this release. Reopening those entries will ask you to use current sources.</p>}
      <ul className={styles.entries}>{preview.entries.map(entry => <PreviewRecord key={entry.id} entry={entry}/>)}</ul>
      <div className={styles.actions}><button type="button" onClick={importFile} disabled={!preview.additions}>{preview.additions ? `Add ${preview.additions} investigation${preview.additions === 1 ? '' : 's'} to this browser` : 'All entries are already saved'}</button><button type="button" onClick={cancel}>Cancel preview</button></div>
    </div>}
    {status && <p role="status" className={styles.message}>{status}</p>}
  </section>;
}
