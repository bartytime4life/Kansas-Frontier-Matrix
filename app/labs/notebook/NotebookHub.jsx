'use client';

import { useEffect, useRef, useState } from 'react';
import Link from 'next/link';
import { deleteLocalInvestigation, exportLocalInvestigations, listLocalInvestigations, sourceBindingsMatch, updateLocalInvestigationNotes, validateInvestigationNotes } from '../notebook.mjs';
import { currentSourceBindings, validateInvestigationState } from '../investigation-state.mjs';
import NotebookTransfer from '../NotebookTransfer.jsx';
import NotesEditor from '../NotesEditor.jsx';
import StarterInvestigations from '../StarterInvestigations.jsx';
import styles from './notebook.module.css';

const workspaceName = workspace => workspace === 'county' ? 'County Observatory' : 'Signal Studio';
const ownDraft = (drafts, id) => Object.hasOwn(drafts, id) ? drafts[id] : null;
function investigationLink(entry) {
  try {
    validateInvestigationState(entry.workspace, entry.state, { privateData: entry.privateData });
    return `/labs/${entry.workspace === 'county' ? 'observatory' : 'signals'}?investigation=${encodeURIComponent(entry.id)}`;
  } catch { return null; }
}
function downloadNotebook() {
  const text = exportLocalInvestigations(), url = URL.createObjectURL(new Blob([text], { type: 'application/json' }));
  const link = document.createElement('a'); link.href = url; link.download = 'kfm-local-investigations.json'; link.click();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}

function DraftNotes({ draft, entry, removed = false, onChange, onSave, onCancel, onReload, onDownload }) {
  const conflict = !removed && (entry.notes ?? '') !== draft.expectedNotes;
  const canReload = !removed && (conflict || !!draft.error);
  return <section className={styles.draft} aria-label={`Edit research notes for ${draft.entry.title}`}>
    {removed && <p className={styles.noteConflict} role="status">This saved investigation was removed in another tab. Your draft is retained here. Download the notes before closing; editing cannot recreate the removed investigation.</p>}
    {conflict && <p className={styles.noteConflict} role="status">The saved notes changed in another tab. Your draft is retained. Reload saved notes to replace this draft, or keep it and download a copy.</p>}
    <NotesEditor id={`notes-draft-${draft.entry.id}`} value={draft.value} onChange={onChange} autoFocus/>
    {draft.error && <p className={styles.noteError} role="alert">{draft.error} Your draft is still here.</p>}
    <div className={styles.noteActions}><button type="button" onClick={onSave} disabled={removed}>Save notes</button><button type="button" onClick={onCancel}>Cancel editing</button>{canReload && <button type="button" onClick={onReload}>Reload saved notes</button>}{(canReload || removed) && <button type="button" onClick={onDownload}>Download draft text ↓</button>}</div>
    {canReload && <p className={styles.reloadHelp}>Reload saved notes replaces the unsaved text above and uses the latest saved analysis. Saving checks for concurrent note or evidence changes before writing.</p>}
  </section>;
}

export default function NotebookHub() {
  const [entries, setEntries] = useState([]), [query, setQuery] = useState(''), [workspace, setWorkspace] = useState('all'), [loaded, setLoaded] = useState(false), [status, setStatus] = useState(''), [drafts, setDrafts] = useState({});
  const noteButtons = useRef(new Map()), savedHeading = useRef(null);
  const returnNoteFocus = id => requestAnimationFrame(() => {
    const target = noteButtons.current.get(id);
    if (target?.isConnected && target.getClientRects().length) target.focus();
    else savedHeading.current?.focus();
  });
  useEffect(() => {
    let live = true;
    queueMicrotask(() => {
      if (!live) return;
      try { setEntries(listLocalInvestigations()); }
      catch (error) { setStatus(error.message || 'This browser cannot read local notebook storage.'); }
      setLoaded(true);
    });
    const sync = event => {
      if (event.key !== null && event.key !== 'kfm-science-notebook-v1') return;
      try { setEntries(listLocalInvestigations()); }
      catch (error) { setStatus(error.message || 'This browser cannot read local notebook storage.'); }
    };
    window.addEventListener('storage', sync);
    return () => { live = false; window.removeEventListener('storage', sync); };
  }, []);
  const refresh = () => {
    try { setEntries(listLocalInvestigations()); setLoaded(true); }
    catch (error) { setStatus(error.message || 'This browser cannot read local notebook storage.'); }
  };
  const remove = entry => {
    try { deleteLocalInvestigation(entry.id); refresh(); setStatus(`Removed “${entry.title}” from this browser. Downloaded notebook copies are unchanged.`); }
    catch (error) { setStatus(error.message || 'This investigation could not be removed.'); }
  };
  const exportNotebook = () => {
    try { downloadNotebook(); setStatus('Notebook downloaded with every saved investigation, its personal notes and any attached private county data. Unsaved note drafts are excluded. Keep the file somewhere you trust.'); }
    catch (error) { setStatus(error.message || 'The notebook could not be downloaded.'); }
  };
  const editNotes = entry => {
    try { const notes = validateInvestigationNotes(entry.notes ?? ''); setDrafts(current => ({ ...current, [entry.id]: { entry, value: notes, expectedNotes: notes, error: '' } })); }
    catch (error) { setStatus(error.message || 'These notes could not be edited.'); }
  };
  const changeDraft = (id, value) => setDrafts(current => ownDraft(current, id) ? { ...current, [id]: { ...ownDraft(current, id), value } } : current);
  const closeDraft = id => { setDrafts(current => { const next = { ...current }; delete next[id]; return next; }); setStatus('Note draft closed. No saved entry was changed.'); returnNoteFocus(id); };
  const saveNotes = id => {
    const draft = ownDraft(drafts, id); if (!draft) return;
    try {
      const updated = updateLocalInvestigationNotes(id, draft.value, { expectedNotes: draft.expectedNotes, expectedEntry: draft.entry });
      refresh(); setDrafts(current => { const next = { ...current }; delete next[id]; return next; });
      setStatus(`Notes saved for “${updated.title}”. Its analysis settings, source fingerprints and attachments were kept.`);
      returnNoteFocus(id);
    } catch (error) { setDrafts(current => ownDraft(current, id) ? { ...current, [id]: { ...ownDraft(current, id), error: error.message || 'The notes could not be saved.' } } : current); }
  };
  const reloadNotes = id => {
    try {
      const entry = listLocalInvestigations().find(item => item.id === id);
      if (!entry) throw new Error('This saved investigation was removed. Download your draft before closing it.');
      const notes = validateInvestigationNotes(entry.notes ?? '');
      setDrafts(current => ownDraft(current, id) ? { ...current, [id]: { entry, value: notes, expectedNotes: notes, error: '' } } : current);
      refresh(); setStatus(`Latest saved notes loaded for “${entry.title}”.`);
      requestAnimationFrame(() => document.getElementById(`notes-draft-${id}`)?.focus());
    } catch (error) { setDrafts(current => ownDraft(current, id) ? { ...current, [id]: { ...ownDraft(current, id), error: error.message || 'Saved notes could not be reloaded.' } } : current); }
  };
  const downloadDraft = id => {
    const draft = ownDraft(drafts, id); if (!draft) return;
    const url = URL.createObjectURL(new Blob([draft.value], { type: 'text/plain;charset=utf-8' }));
    const link = document.createElement('a'); link.href = url; link.download = 'kfm-research-note-draft.txt'; link.click(); setTimeout(() => URL.revokeObjectURL(url), 1000);
    setStatus(`Unsaved notes for “${draft.entry.title}” downloaded as plain text. They are still open in the editor.`);
  };
  const privateCount = entries.filter(entry => entry.privateData).length;
  const changedCount = entries.filter(entry => !sourceBindingsMatch(entry.sourceBindings, currentSourceBindings(entry.workspace))).length;
  const search = query.trim().toLocaleLowerCase('en-US');
  const shown = entries.filter(entry => (workspace === 'all' || entry.workspace === workspace) && (!search || `${entry.title} ${workspaceName(entry.workspace)} ${entry.privateData?.fileName || ''} ${entry.notes || ''}`.toLocaleLowerCase('en-US').includes(search)));
  const removedDrafts = Object.values(drafts).filter(draft => !entries.some(entry => entry.id === draft.entry.id));
  const hiddenDrafts = Object.keys(drafts).filter(id => entries.some(entry => entry.id === id) && !shown.some(entry => entry.id === id));
  const draftProps = id => ({ onChange: value => changeDraft(id, value), onSave: () => saveNotes(id), onCancel: () => closeDraft(id), onReload: () => reloadNotes(id), onDownload: () => downloadDraft(id) });
  return <div className={styles.page}>
    <header className={styles.masthead}><Link prefetch={false} href="/labs" className={styles.brand}>KFM <span>THE RESEARCH ATLAS</span></Link><nav aria-label="Research navigation"><Link prefetch={false} href="/labs">All labs ↗</Link><Link prefetch={false} href="/labs/observatory">County Observatory</Link><Link prefetch={false} href="/labs/signals">Signal Studio</Link></nav></header>
    <main className={styles.main}>
      <section className={styles.intro} aria-labelledby="notebook-title"><div><p className={styles.eyebrow}>YOUR WORK / YOUR BROWSER</p><h1 id="notebook-title">A place for the next question.</h1><p>Reopen a saved investigation, keep the reasoning behind it, or bring a notebook from another browser. Your notes, settings and private county uploads stay on this device unless you download them.</p></div><div className={styles.download}><button type="button" onClick={exportNotebook} disabled={!entries.length}>Download full notebook ↓</button><span>{privateCount ? `Includes personal notes and ${privateCount} private attachment${privateCount === 1 ? '' : 's'}.` : 'Portable JSON · saved notes, settings + source fingerprints'}</span></div></section>
      <StarterInvestigations/>
      <section className={styles.desk} aria-labelledby="saved-title">
        <div className={styles.deskTop}><div><span>THE LOCAL RECORD</span><h2 ref={savedHeading} tabIndex={-1} id="saved-title">Saved investigations</h2></div><dl><div><dt>Saved / 12</dt><dd>{loaded ? entries.length : '—'}</dd></div><div><dt>Sources changed</dt><dd>{loaded ? changedCount : '—'}</dd></div><div><dt>Private attachments</dt><dd>{loaded ? privateCount : '—'}</dd></div></dl></div>
        <div className={styles.finder}><label><span>FIND AN INVESTIGATION</span><input type="search" value={query} maxLength={200} onChange={event => setQuery(event.target.value)} placeholder="Search a question, note, workspace or filename…"/></label><div className={styles.filters} role="group" aria-label="Filter investigations by workspace">{[['all', 'All'], ['county', 'County'], ['signal', 'Signal']].map(([value, label]) => <button type="button" key={value} aria-pressed={workspace === value} onClick={() => setWorkspace(value)}>{label}</button>)}</div></div>
        {status && <p className={styles.status} role="status">{status}</p>}
        {hiddenDrafts.length > 0 && <p className={styles.draftNotice} role="status">{hiddenDrafts.length} unsaved note {hiddenDrafts.length === 1 ? 'draft is' : 'drafts are'} retained outside this filtered view. <button type="button" onClick={() => { setQuery(''); setWorkspace('all'); }}>Show edited investigations</button></p>}
        {removedDrafts.length > 0 && <section className={styles.removedDrafts} aria-label="Retained drafts for removed investigations"><h3>Your unsaved notes are still here.</h3>{removedDrafts.map(draft => <div key={draft.entry.id}><h4>{draft.entry.title}</h4><DraftNotes draft={draft} entry={draft.entry} removed {...draftProps(draft.entry.id)}/></div>)}</section>}
        {!loaded ? <p className={styles.empty} role="status">Reading this browser’s notebook…</p> : shown.length ? <><p className={styles.resultCount} role="status">{shown.length} of {entries.length} saved investigations</p><ol className={styles.entries}>{shown.map(entry => {
          const matched = sourceBindingsMatch(entry.sourceBindings, currentSourceBindings(entry.workspace)), href = investigationLink(entry);
          return <li key={entry.id}>
            <div className={styles.entryBody}><div className={styles.entryMeta}><span>{workspaceName(entry.workspace)}</span><time dateTime={entry.createdAt}>{entry.createdAt.slice(0, 10)}</time></div><h3>{entry.title}</h3><p className={styles.sourceStatus} data-changed={!matched}>{matched ? 'Source fingerprints match this release' : 'Sources changed · review before reopening'}{entry.privateData && <span>Private CSV attached</span>}</p>
              {ownDraft(drafts, entry.id) ? <DraftNotes draft={ownDraft(drafts, entry.id)} entry={entry} {...draftProps(entry.id)}/> : <section className={styles.fieldNotes} aria-label={`Research notes for ${entry.title}`}><div><h4>Field notes</h4><button ref={node => { if (node) noteButtons.current.set(entry.id, node); else noteButtons.current.delete(entry.id); }} type="button" onClick={() => editNotes(entry)} aria-label={`Edit research notes for ${entry.title}`}>{entry.notes ? 'Edit notes' : 'Add notes +'}</button></div>{entry.notes ? <><p className={styles.notesExcerpt}>{entry.notes.length > 240 ? `${entry.notes.slice(0, 240)}…` : entry.notes}</p>{entry.notes.length > 240 && <details><summary>Read full research notes</summary><p tabIndex={0} className={styles.fullNotes} aria-label={`Full research notes for ${entry.title}`}>{entry.notes}</p></details>}</> : <p className={styles.noNotes}>Keep what you observed, the limits and your next check with this saved analysis.</p>}</section>}
              <details><summary>Inspect saved sources{entry.privateData ? ' + attachment' : ''}</summary><dl className={styles.sources}>{Object.entries(entry.sourceBindings).map(([id, hash]) => <div key={id}><dt>{id}</dt><dd><code>{hash}</code></dd></div>)}</dl>{entry.privateData && <p className={styles.attachment}><strong>{entry.privateData.fileName}</strong> · {entry.privateData.rows.length} county rows · {entry.privateData.columns.length} measures<br/>Attached values are saved in this browser and included in a full notebook download. They never enter an investigation URL.</p>}</details>
            </div><div className={styles.entryActions}>{href ? <Link prefetch={false} href={href} aria-label={`Open saved investigation ${entry.title}`}>Open investigation ↗</Link> : <p>These saved settings are incompatible with this release. Keep a downloaded copy.</p>}<button type="button" onClick={() => remove(entry)} aria-label={`Remove ${entry.title} from this browser`}>Remove local copy</button></div>
          </li>;
        })}</ol></> : <div className={styles.empty}><span aria-hidden="true">∴</span><h3>{entries.length ? 'No saved questions in this view.' : 'Your next visit can start here.'}</h3><p>{entries.length ? 'Try another search or include both workspaces.' : 'Explore a county comparison or a pair of annual signals, then choose Save investigation in its research notebook. You can also import an earlier download below.'}</p><div>{entries.length ? <button type="button" onClick={() => { setQuery(''); setWorkspace('all'); }}>Show all saved research</button> : <><Link prefetch={false} href="/labs/observatory">Start with a county ↗</Link><Link prefetch={false} href="/labs/signals">Follow an annual signal ↗</Link></>}</div></div>}
        <NotebookTransfer onChange={refresh}/>
      </section>
      <aside className={styles.note}><strong>Keep a copy you can carry.</strong><p>This notebook is local browser storage. Clearing site data removes saved entries. Download the JSON to back up saved notes and investigations or move them to another browser, then use Import to add them there. Unsaved note drafts are excluded from the full notebook download. A shared investigation link carries settings and source fingerprints; it does not transfer personal notes, this local notebook or private uploads.</p></aside>
    </main>
    <footer className={styles.footer}><span>KANSAS FRONTIER MATRIX / RESEARCH NOTEBOOK</span><Link prefetch={false} href="/labs">Return to the labs ↑</Link></footer>
  </div>;
}
