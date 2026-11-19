'use client';
import { useEffect, useRef, useState } from 'react';
import Link from 'next/link';
import { deleteLocalInvestigation, exportLocalInvestigations, getLocalInvestigation, listLocalInvestigations, saveLocalInvestigation, sourceBindingsMatch, validateInvestigationNotes } from './notebook.mjs';
import { validateInvestigationState } from './investigation-state.mjs';
import NotebookTransfer from './NotebookTransfer.jsx';
import NotesEditor from './NotesEditor.jsx';
import styles from './NotebookPanel.module.css';

function downloadJSON(text) {
  const url = URL.createObjectURL(new Blob([text], { type: 'application/json' }));
  const link = document.createElement('a'); link.href = url; link.download = 'kfm-local-investigations.json'; link.click();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}

export default function NotebookPanel({ workspace, state, sourceBindings, onRestore, privateData, title: suggestedTitle }) {
  const [entries, setEntries] = useState([]), [title, setTitle] = useState(''), [notes, setNotes] = useState(''), [status, setStatus] = useState(''), [pending, setPending] = useState(null);
  const queryRead = useRef(false), review = useRef(null), feedback = useRef(null);
  useEffect(() => {
    if (pending) { review.current?.scrollIntoView({ block: 'center' }); review.current?.focus({ preventScroll: true }); }
  }, [pending]);
  useEffect(() => {
    let live = true;
    queueMicrotask(() => { if (live) { try { setEntries(listLocalInvestigations()); } catch (error) { setStatus(error.message); } } });
    const sync = event => { if (event.key === null || event.key === 'kfm-science-notebook-v1') { try { setEntries(listLocalInvestigations()); } catch (error) { setStatus(error.message); } } };
    window.addEventListener('storage', sync);
    return () => { live = false; window.removeEventListener('storage', sync); };
  }, []);
  useEffect(() => {
    let live = true;
    queueMicrotask(() => {
      if (!live || queryRead.current || !Object.keys(sourceBindings || {}).length) return;
      queryRead.current = true;
      const params = new URLSearchParams(window.location.search);
      if (!params.has('investigation')) return;
      try {
        const entry = getLocalInvestigation(params.get('investigation'));
        if (!entry) throw new Error('That investigation is not saved in this browser. Import its notebook JSON here to reopen it.');
        if (entry.workspace !== workspace) throw new Error('That investigation belongs to the other workspace. Open it from your research notebook.');
        const checked = { ...entry, state: validateInvestigationState(workspace, entry.state, { privateData: entry.privateData }) };
        if (!sourceBindingsMatch(checked.sourceBindings, sourceBindings)) { setPending(checked); return; }
        const savedNotes = validateInvestigationNotes(checked.notes ?? '');
        onRestore(checked); setNotes(savedNotes); setStatus(`Reopened “${entry.title}” with the matching source snapshots and its saved notes.`);
      } catch (error) {
        setStatus(error.message || 'This saved investigation could not be restored.');
        requestAnimationFrame(() => { if (live) { feedback.current?.scrollIntoView({ block: 'center' }); feedback.current?.focus({ preventScroll: true }); } });
      }
    });
    return () => { live = false; };
  }, [workspace, sourceBindings, onRestore]);
  const refresh = () => setEntries(listLocalInvestigations());
  const save = () => {
    try {
      const checkedState = validateInvestigationState(workspace, state, { privateData });
      const checkedNotes = validateInvestigationNotes(notes);
      const entry = saveLocalInvestigation({ workspace, title: title.trim() || suggestedTitle || (workspace === 'county' ? 'County investigation' : 'Signal investigation'), notes: checkedNotes, state: checkedState, sourceBindings, ...(privateData ? { privateData } : {}) });
      refresh(); setTitle(''); setStatus(`Saved “${entry.title}” in this browser${privateData ? ', including your private county data' : ''}.`);
    } catch (error) { setStatus(error.message || 'Browser storage is unavailable. Download an analysis receipt instead.'); }
  };
  const restore = (entry, allowChangedSources = false) => {
    try {
      const checked = { ...entry, state: validateInvestigationState(workspace, entry.state, { privateData: entry.privateData }) };
      const matched = sourceBindingsMatch(checked.sourceBindings, sourceBindings);
      if (!matched && !allowChangedSources) { setPending(checked); setStatus(''); return; }
      const savedNotes = validateInvestigationNotes(checked.notes ?? '');
      onRestore(checked); setNotes(savedNotes); setPending(null); setStatus(matched ? `Reopened “${entry.title}” with the matching source snapshots and its saved notes.` : `Reopened “${entry.title}” and its notes with current sources. The original saved entry is kept; results may differ.`);
    }
    catch (error) { setStatus(error.message || 'This saved investigation could not be restored.'); }
  };
  const remove = id => { try { deleteLocalInvestigation(id); refresh(); if (pending?.id === id) setPending(null); setStatus('Saved investigation removed from this browser.'); } catch (error) { setStatus(error.message); } };
  const exportNotebook = () => { try { downloadJSON(exportLocalInvestigations()); setStatus('Notebook downloaded. It includes personal notes and any private county data attached to saved investigations.'); } catch (error) { setStatus(error.message); } };
  const shown = entries.filter(entry => entry.workspace === workspace);
  return <section className={styles.notebook} aria-labelledby={`${workspace}-notebook-title`}>
    <div className={styles.heading}><div><span>YOUR RESEARCH NOTEBOOK</span><h2 id={`${workspace}-notebook-title`}>Keep a question open.</h2><p>Saved on this browser only. Reopen the settings and source fingerprints that shaped your investigation.</p></div><Link prefetch={false} href="/labs/notebook" className={styles.local}>ALL SAVED RESEARCH ↗</Link></div>
    <div className={styles.save}><label>Investigation name<input type="text" maxLength={120} value={title} onChange={event => setTitle(event.target.value)} placeholder={suggestedTitle || 'What are you investigating?'}/></label></div>
    <NotesEditor id={`${workspace}-research-notes`} value={notes} onChange={setNotes}/>
    {privateData && <p className={styles.private}>Your uploaded county values will be included in this browser’s saved copy. They are excluded from share links.</p>}
    <div className={styles.saveAction}><span>Keep the current controls, source fingerprints and notes together.</span><button type="button" onClick={save}>Save investigation +</button></div>
    {status && <p ref={feedback} tabIndex={-1} className={styles.status} role="status">{status}</p>}
    {pending && <section ref={review} tabIndex={-1} className={styles.changed} aria-label="Review changed sources before reopening"><span>SOURCE CHECK</span><h3>Reopen with a changed record?</h3><p>“{pending.title}” was saved with different source fingerprints. The original snapshots are not loaded here. Using the current release can change the results.</p><ul>{[...new Set([...Object.keys(pending.sourceBindings), ...Object.keys(sourceBindings)])].filter(id => pending.sourceBindings[id] !== sourceBindings[id]).map(id => <li key={id}>{id} · saved {pending.sourceBindings[id]?.slice(0, 12) || 'not included'} / current {sourceBindings[id]?.slice(0, 12) || 'not included'}</li>)}</ul><div><button type="button" onClick={() => restore(pending, true)}>Reopen with current sources</button><button type="button" onClick={() => { setPending(null); setStatus('Saved investigation kept. Current settings were not changed.'); }}>Keep current view</button></div></section>}
    {shown.length ? <ul className={styles.entries}>{shown.map(entry => <li key={entry.id}><div><strong>{entry.title}</strong><small>{entry.createdAt?.slice(0, 10)} · {sourceBindingsMatch(entry.sourceBindings, sourceBindings) ? 'Source fingerprints match' : 'Sources changed since saving'}{entry.privateData ? ' · private data attached' : ''}</small></div><button type="button" onClick={() => restore(entry)}>Reopen ↗</button><button type="button" className={styles.remove} aria-label={`Delete saved investigation ${entry.title}`} onClick={() => remove(entry.id)}>×</button></li>)}</ul> : <p className={styles.empty}>Save this view to make it the beginning of your next visit.</p>}
    <div className={styles.foot}><span>Up to 12 investigations. Clearing browser storage removes local copies.</span><button type="button" disabled={!entries.length} onClick={exportNotebook}>Download notebook JSON ↓</button></div>
    <NotebookTransfer onChange={refresh}/>
  </section>;
}
