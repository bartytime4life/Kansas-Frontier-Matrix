'use client';

import { useEffect, useState } from 'react';
import Link from 'next/link';
import { deleteLocalInvestigation, exportLocalInvestigations, listLocalInvestigations, sourceBindingsMatch } from '../notebook.mjs';
import { currentSourceBindings, validateInvestigationState } from '../investigation-state.mjs';
import NotebookTransfer from '../NotebookTransfer.jsx';
import styles from './notebook.module.css';

const workspaceName = workspace => workspace === 'county' ? 'County Observatory' : 'Signal Studio';
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

export default function NotebookHub() {
  const [entries, setEntries] = useState([]), [query, setQuery] = useState(''), [workspace, setWorkspace] = useState('all'), [loaded, setLoaded] = useState(false), [status, setStatus] = useState('');
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
    try { downloadNotebook(); setStatus('Notebook downloaded with every saved investigation and its attached private county data. Keep the file somewhere you trust.'); }
    catch (error) { setStatus(error.message || 'The notebook could not be downloaded.'); }
  };
  const privateCount = entries.filter(entry => entry.privateData).length;
  const changedCount = entries.filter(entry => !sourceBindingsMatch(entry.sourceBindings, currentSourceBindings(entry.workspace))).length;
  const search = query.trim().toLocaleLowerCase('en-US');
  const shown = entries.filter(entry => (workspace === 'all' || entry.workspace === workspace) && (!search || `${entry.title} ${workspaceName(entry.workspace)} ${entry.privateData?.fileName || ''}`.toLocaleLowerCase('en-US').includes(search)));
  return <div className={styles.page}>
    <header className={styles.masthead}><Link prefetch={false} href="/labs" className={styles.brand}>KFM <span>THE RESEARCH ATLAS</span></Link><nav aria-label="Research navigation"><Link prefetch={false} href="/labs">All labs ↗</Link><Link prefetch={false} href="/labs/observatory">County Observatory</Link><Link prefetch={false} href="/labs/signals">Signal Studio</Link></nav></header>
    <main className={styles.main}>
      <section className={styles.intro} aria-labelledby="notebook-title"><div><p className={styles.eyebrow}>YOUR WORK / YOUR BROWSER</p><h1 id="notebook-title">A place for the next question.</h1><p>Reopen a saved investigation, check the record behind it, or bring a notebook from another browser. Your settings and private county uploads stay on this device unless you download them.</p></div><div className={styles.download}><button type="button" onClick={exportNotebook} disabled={!entries.length}>Download full notebook ↓</button><span>{privateCount ? `Includes ${privateCount} private attachment${privateCount === 1 ? '' : 's'}.` : 'Portable JSON · settings + source fingerprints'}</span></div></section>
      <section className={styles.desk} aria-labelledby="saved-title">
        <div className={styles.deskTop}><div><span>THE LOCAL RECORD</span><h2 id="saved-title">Saved investigations</h2></div><dl><div><dt>Saved / 12</dt><dd>{loaded ? entries.length : '—'}</dd></div><div><dt>Sources changed</dt><dd>{loaded ? changedCount : '—'}</dd></div><div><dt>Private attachments</dt><dd>{loaded ? privateCount : '—'}</dd></div></dl></div>
        <div className={styles.finder}><label><span>FIND AN INVESTIGATION</span><input type="search" value={query} maxLength={200} onChange={event => setQuery(event.target.value)} placeholder="Search a question, workspace or filename…"/></label><div className={styles.filters} role="group" aria-label="Filter investigations by workspace">{[['all', 'All'], ['county', 'County'], ['signal', 'Signal']].map(([value, label]) => <button type="button" key={value} aria-pressed={workspace === value} onClick={() => setWorkspace(value)}>{label}</button>)}</div></div>
        {status && <p className={styles.status} role="status">{status}</p>}
        {!loaded ? <p className={styles.empty} role="status">Reading this browser’s notebook…</p> : shown.length ? <><p className={styles.resultCount} role="status">{shown.length} of {entries.length} saved investigations</p><ol className={styles.entries}>{shown.map(entry => {
          const matched = sourceBindingsMatch(entry.sourceBindings, currentSourceBindings(entry.workspace)), href = investigationLink(entry);
          return <li key={entry.id}>
            <div className={styles.entryBody}><div className={styles.entryMeta}><span>{workspaceName(entry.workspace)}</span><time dateTime={entry.createdAt}>{entry.createdAt.slice(0, 10)}</time></div><h3>{entry.title}</h3><p className={styles.sourceStatus} data-changed={!matched}>{matched ? 'Source fingerprints match this release' : 'Sources changed · review before reopening'}{entry.privateData && <span>Private CSV attached</span>}</p>
              <details><summary>Inspect saved sources{entry.privateData ? ' + attachment' : ''}</summary><dl className={styles.sources}>{Object.entries(entry.sourceBindings).map(([id, hash]) => <div key={id}><dt>{id}</dt><dd><code>{hash}</code></dd></div>)}</dl>{entry.privateData && <p className={styles.attachment}><strong>{entry.privateData.fileName}</strong> · {entry.privateData.rows.length} county rows · {entry.privateData.columns.length} measures<br/>Attached values are saved in this browser and included in a full notebook download. They never enter an investigation URL.</p>}</details>
            </div><div className={styles.entryActions}>{href ? <Link prefetch={false} href={href} aria-label={`Open saved investigation ${entry.title}`}>Open investigation ↗</Link> : <p>These saved settings are incompatible with this release. Keep a downloaded copy.</p>}<button type="button" onClick={() => remove(entry)} aria-label={`Remove ${entry.title} from this browser`}>Remove local copy</button></div>
          </li>;
        })}</ol></> : <div className={styles.empty}><span aria-hidden="true">∴</span><h3>{entries.length ? 'No saved questions in this view.' : 'Your next visit can start here.'}</h3><p>{entries.length ? 'Try another search or include both workspaces.' : 'Explore a county comparison or a pair of annual signals, then choose Save investigation in its research notebook. You can also import an earlier download below.'}</p><div>{entries.length ? <button type="button" onClick={() => { setQuery(''); setWorkspace('all'); }}>Show all saved research</button> : <><Link prefetch={false} href="/labs/observatory">Start with a county ↗</Link><Link prefetch={false} href="/labs/signals">Follow an annual signal ↗</Link></>}</div></div>}
        <NotebookTransfer onChange={refresh}/>
      </section>
      <aside className={styles.note}><strong>Keep a copy you can carry.</strong><p>This notebook is local browser storage. Clearing site data removes saved entries. Download the JSON to back it up or move it to another browser, then use Import to add it there. A shared investigation link carries settings and source fingerprints; it does not transfer this local notebook or private uploads.</p></aside>
    </main>
    <footer className={styles.footer}><span>KANSAS FRONTIER MATRIX / RESEARCH NOTEBOOK</span><Link prefetch={false} href="/labs">Return to the labs ↑</Link></footer>
  </div>;
}
