'use client';
import { useEffect, useState } from 'react';
import { deleteLocalInvestigation, exportLocalInvestigations, listLocalInvestigations, saveLocalInvestigation, sourceBindingsMatch } from './notebook.mjs';
import styles from './NotebookPanel.module.css';

function downloadJSON(text) {
  const url = URL.createObjectURL(new Blob([text], { type: 'application/json' }));
  const link = document.createElement('a'); link.href = url; link.download = 'kfm-local-investigations.json'; link.click();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}

export default function NotebookPanel({ workspace, state, sourceBindings, onRestore, privateData, title: suggestedTitle }) {
  const [entries, setEntries] = useState([]), [title, setTitle] = useState(''), [status, setStatus] = useState('');
  useEffect(() => {
    let live = true;
    queueMicrotask(() => { if (live) { try { setEntries(listLocalInvestigations()); } catch (error) { setStatus(error.message); } } });
    return () => { live = false; };
  }, []);
  const refresh = () => setEntries(listLocalInvestigations());
  const save = () => {
    try {
      const entry = saveLocalInvestigation({ workspace, title: title.trim() || suggestedTitle || (workspace === 'county' ? 'County investigation' : 'Signal investigation'), state, sourceBindings, ...(privateData ? { privateData } : {}) });
      refresh(); setTitle(''); setStatus(`Saved “${entry.title}” in this browser${privateData ? ', including your private county data' : ''}.`);
    } catch (error) { setStatus(error.message || 'Browser storage is unavailable. Download an analysis receipt instead.'); }
  };
  const restore = entry => {
    const matched = sourceBindingsMatch(entry.sourceBindings, sourceBindings);
    try { onRestore(entry); setStatus(matched ? `Reopened “${entry.title}” with the matching source snapshots.` : `Reopened “${entry.title}” against current sources. The saved source fingerprints differ; the results may have changed.`); }
    catch (error) { setStatus(error.message || 'This saved investigation could not be restored.'); }
  };
  const remove = id => { try { deleteLocalInvestigation(id); refresh(); setStatus('Saved investigation removed from this browser.'); } catch (error) { setStatus(error.message); } };
  const exportNotebook = () => { try { downloadJSON(exportLocalInvestigations()); setStatus('Notebook downloaded. It includes private county data attached to saved investigations.'); } catch (error) { setStatus(error.message); } };
  const shown = entries.filter(entry => entry.workspace === workspace);
  return <section className={styles.notebook} aria-labelledby={`${workspace}-notebook-title`}>
    <div className={styles.heading}><div><span>YOUR RESEARCH NOTEBOOK</span><h2 id={`${workspace}-notebook-title`}>Keep a question open.</h2><p>Saved on this browser only. Reopen the settings and source fingerprints that shaped your investigation.</p></div><span className={styles.local}>BROWSER LOCAL</span></div>
    <div className={styles.save}><label>Investigation name<input type="text" maxLength={120} value={title} onChange={event => setTitle(event.target.value)} placeholder={suggestedTitle || 'What are you investigating?'}/></label><button type="button" onClick={save}>Save investigation +</button></div>
    {privateData && <p className={styles.private}>Your uploaded county values will be included in this browser’s saved copy. They are excluded from share links.</p>}
    {status && <p className={styles.status} role="status">{status}</p>}
    {shown.length ? <ul className={styles.entries}>{shown.map(entry => <li key={entry.id}><div><strong>{entry.title}</strong><small>{entry.createdAt?.slice(0, 10)} · {sourceBindingsMatch(entry.sourceBindings, sourceBindings) ? 'Source fingerprints match' : 'Sources changed since saving'}{entry.privateData ? ' · private data attached' : ''}</small></div><button type="button" onClick={() => restore(entry)}>Reopen ↗</button><button type="button" className={styles.remove} aria-label={`Delete saved investigation ${entry.title}`} onClick={() => remove(entry.id)}>×</button></li>)}</ul> : <p className={styles.empty}>Save this view to make it the beginning of your next visit.</p>}
    <div className={styles.foot}><span>Up to 12 investigations. Clearing browser storage removes local copies.</span><button type="button" disabled={!entries.length} onClick={exportNotebook}>Download notebook JSON ↓</button></div>
  </section>;
}
