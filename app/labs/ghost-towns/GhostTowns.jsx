'use client';

import { useState } from 'react';
import Link from 'next/link';
import { safeCell } from '../../living-welcome/stories/record-model.mjs';
import { downloadCSV } from '../../living-welcome/stories/story-kit.mjs';
import {
  continuityText, locationText, mapOfficeGroups, officesInView, postalCSV, postalMap, postalTimeline, recordedEvents,
} from './post-office-model.mjs';
import snapshot from './post-office-snapshot.json';
import styles from './ghost-towns.module.css';

const { boundary, records, scope, source } = snapshot;
const timeline = postalTimeline(records);
const projection = postalMap(boundary.ring, records);
const peak = Math.max(...timeline.years.map(row => row.established + row.discontinued));
const mappedCount = records.filter(record => record.location).length;

function Timeline({ year, onYear }) {
  return <section className={styles.timeline} aria-labelledby="postal-year-label">
    <div className={styles.timelineHeading}>
      <div>
        <h2 id="postal-year-label">Explore recorded years</h2>
        <p>Each column counts the dates attached to postal records.</p>
      </div>
      <output htmlFor="postal-year" className={styles.year}>{year}</output>
    </div>
    <div className={styles.yearBars} aria-hidden="true">
      {timeline.years.map(row => <span key={row.year} data-current={row.year === year || undefined}>
        <i className={styles.ended} style={{ height: `${row.discontinued / peak * 100}%` }}/>
        <i className={styles.started} style={{ height: `${row.established / peak * 100}%` }}/>
      </span>)}
    </div>
    <input type="range" id="postal-year" min={timeline.min} max={timeline.max} value={year} step={1}
      onChange={event => onYear(Number(event.target.value))} aria-label="Recorded event year"/>
    <div className={styles.timelineFooter}>
      <span>{timeline.min}</span>
      <span className={styles.legend}><span>Recorded establishment</span><span>Recorded discontinuance</span></span>
      <span>{timeline.max}</span>
    </div>
  </section>;
}

function OfficeMap({ visibleRecords, selected, year, view, onPick }) {
  const groups = mapOfficeGroups(visibleRecords, projection.project);
  const unlocated = visibleRecords.filter(record => !record.location).length;
  return <figure className={styles.map}>
    <div className={styles.mapHeading}>
      <h2>Matched locations</h2>
      <span aria-hidden="true">N ↑</span>
    </div>
    <div className={styles.mapArea} role="group" aria-label="Approximate locations of the visible postal records">
      <div className={styles.countyShape} style={{ clipPath: projection.boundaryClip }} aria-hidden="true"/>
      {groups.map(group => {
        const isSelected = group.records.some(record => record.id === selected?.id);
        const next = (group.records.findIndex(record => record.id === selected?.id) + 1) % group.records.length;
        const color = view === 'events' && group.records.every(record => record.discontinued === year && record.established !== year)
          ? 'ended' : 'started';
        return <button key={group.key} type="button" className={styles.pin} data-kind={color} aria-pressed={isSelected}
          style={{ left: `${group.x}%`, top: `${group.y}%` }} onClick={() => onPick(group.records[next].id)}
          aria-label={group.records.length === 1 ? `Inspect ${group.records[0].name}` : `Inspect ${group.records[next].name}, one of ${group.records.length} records at this approximate location`}>
          <span>{group.records.length > 1 ? group.records.length : ''}</span>
        </button>;
      })}
      {groups.length === 0 && <p className={styles.mapEmpty}>The selected view has no matched locations.</p>}
    </div>
    <figcaption>
      {visibleRecords.length - unlocated} of {visibleRecords.length} visible records have a provider-supplied approximate location.
      {unlocated > 0 && ` ${unlocated} remain in the list without a map point.`} The outline is contemporary.
    </figcaption>
  </figure>;
}

function OfficeSource({ office }) {
  return <article className={styles.recordDetail} aria-labelledby="postal-detail-title">
    <p className={styles.sourceId}>Record {office.id}</p>
    <h3 id="postal-detail-title">{office.name}</h3>
    {office.alternateName && <p>Also recorded as {office.alternateName}</p>}
    <dl>
      <div><dt>Established</dt><dd>{office.established ?? 'Unrecorded'}</dd></div>
      <div><dt>Discontinued</dt><dd>{office.discontinued ?? 'Unrecorded'}</dd></div>
      <div><dt>Source county</dt><dd>{office.counties.join(' / ')}</dd></div>
    </dl>
    <p>{continuityText(office)}</p>
    {office.location
      ? <p>Approximate GNIS match for {office.location.gnisName} in {office.location.gnisCounty}. GNIS ID {office.location.gnisId}.</p>
      : <p>The source supplied no matched coordinates for this office.</p>}
    <a href={source.url}>Open the original source file</a>
  </article>;
}

export default function GhostTowns({ initial }) {
  const [year, setYear] = useState(initial.year);
  const [view, setView] = useState(initial.view);
  const [office, setOffice] = useState(initial.office);
  const [share, setShare] = useState(null);
  const dated = officesInView(records, year, 'events');
  const visibleRecords = officesInView(records, year, view);
  const selected = visibleRecords.find(record => record.id === office) ?? visibleRecords[0];
  const copyLink = async () => {
    const url = new URL('/labs/ghost-towns', window.location.origin);
    url.searchParams.set('year', String(year));
    url.searchParams.set('view', view);
    if (selected) url.searchParams.set('office', selected.id);
    try {
      await navigator.clipboard.writeText(url.href);
      setShare({ message: `Link for ${year} copied.` });
    } catch {
      setShare({ message: `Copy the link for ${year}.`, url: url.href });
    }
  };

  const setEventYear = next => {
    setYear(next);
    setView('events');
    setShare(null);
  };
  const exportView = () => downloadCSV(
    `douglas-post-office-${view === 'all' ? 'records' : year}.csv`,
    postalCSV(visibleRecords, year, view, source).map(row => row.map(safeCell)),
  );

  return <main className={styles.page}>
    <nav className={styles.nav} aria-label="Labs navigation">
      <Link href="/labs">← Research Labs</Link>
      <Link href="/data-lab?collection=observations-blevins-post-offices&amp;pack=land-history">Post-office collection in Record Lab</Link>
    </nav>
    <header className={styles.intro}>
      <div>
        <p className={styles.kicker}>{scope.county}, {scope.state}</p>
        <h1>Boom &amp; Ghost Towns</h1>
        <p>Follow documented post-office establishments and discontinuances through the years. Records may reflect name changes, reopenings or status changes.</p>
      </div>
      <div className={styles.introMetric}>
        <strong>{records.length}</strong>
        <span>source records</span>
        <span>{mappedCount} with approximate locations</span>
      </div>
    </header>
    <Timeline year={year} onYear={setEventYear}/>
    <section className={styles.workspace} aria-label="Postal records and locations">
      <div className={styles.workspaceControls}>
        <div className={styles.viewSwitch} role="group" aria-label="Postal record view">
          <button type="button" aria-pressed={view === 'events'} onClick={() => { setView('events'); setShare(null); }}>Events in {year}</button>
          <button type="button" aria-pressed={view === 'all'} onClick={() => { setView('all'); setShare(null); }}>All records</button>
        </div>
        <div className={styles.actions}>
          <button type="button" onClick={copyLink}>Copy view link</button>
          <button type="button" disabled={!visibleRecords.length} onClick={exportView}>Download records CSV</button>
        </div>
      </div>
      {share && <div className={styles.share}>
        <p role="status">{share.message}</p>
        {share.url && <input type="url" aria-label="Postal history view link" value={share.url} readOnly onFocus={event => event.target.select()}/>}
      </div>}
      <div className={styles.workspaceBody}>
        <OfficeMap visibleRecords={visibleRecords} selected={selected} view={view} year={year} onPick={setOffice}/>
        <div className={styles.records}>
          <h2>{view === 'all' ? 'All source records' : `Recorded events in ${year}`}</h2>
          <p className={styles.listContext} aria-live="polite">
            {view === 'all' ? `${visibleRecords.length} records, including entries with missing dates.`
              : `${dated.filter(record => record.established === year).length} recorded establishments · ${dated.filter(record => record.discontinued === year).length} recorded discontinuances`}
          </p>
          {visibleRecords.length > 0 ? <>
            <ul className={styles.recordList} aria-label="Select a post-office record">
              {visibleRecords.map(record => <li key={record.id}>
                <button type="button" aria-pressed={selected?.id === record.id} onClick={() => setOffice(record.id)}>
                  <span>{record.name}</span>
                  <small>{view === 'all' ? locationText(record) : recordedEvents(record, year).join(' and ')}</small>
                </button>
              </li>)}
            </ul>
            {selected && <OfficeSource office={selected}/>}
          </> : <p className={styles.empty}>No source record carries an establishment or discontinuance date in this year. Try another year or open all records.</p>}
        </div>
      </div>
    </section>
    <footer className={styles.sources}>
      <h2>Sources &amp; interpretation</h2>
      <p>{source.authors}, <a href={source.doi}>{source.title} {source.edition}</a>, Harvard Dataverse. <a href={source.licenseUrl}>{source.license}</a>.</p>
      <p>Coverage includes every Kansas record with Douglas as a source county. County assignments reflect the compiler’s geography. These records describe postal events. Settlement dates, population and postal moves require other evidence.</p>
      <p><a href={source.methodUrl}>Source methods and limitations</a> · <a href={source.dictionaryUrl}>Field definitions</a> · <a href={boundary.url}>Census TIGERweb outline</a></p>
      <details>
        <summary>Snapshot provenance</summary>
        <p>Original file retrieved {source.retrievedAt} · {source.bytes.toLocaleString('en-US')} bytes</p>
        <code>SHA-256 {source.sha256}</code>
      </details>
    </footer>
  </main>;
}
