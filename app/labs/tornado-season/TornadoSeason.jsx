'use client';

import Link from 'next/link';
import { useMemo, useState } from 'react';
import { downloadCSV, KANSAS_OUTLINE_CREDIT } from '../../living-welcome/stories/story-kit.mjs';
import { useStoryBundle } from '../../living-welcome/stories/useStoryBundle.js';
import SeasonMap from './SeasonMap.jsx';
import { busiestDate, displayRating, mapCoverage, MONTHS, PERIODS, seasonCsv, summarizeSeason } from './season-model.mjs';
import styles from './tornado-season.module.css';

const number = new Intl.NumberFormat('en-US');
const percent = new Intl.NumberFormat('en-US', { style: 'percent', maximumFractionDigits: 1 });
const dayLabel = new Intl.DateTimeFormat('en-US', { dateStyle: 'medium', timeZone: 'UTC' });
const shareOf = (count, total) => total > 0 ? count / total : 0;
const pageSize = 10;

function Share({ count, total, kind }) {
  const share = shareOf(count, total);
  return <td>
    <span className={styles.bar} data-kind={kind} aria-hidden="true"><i style={{ width: `${share * 100}%` }}/></span>
    <span>{number.format(count)} <small>({percent.format(share)})</small></span>
  </td>;
}

function MonthTable({ summary, selected, onSelect }) {
  return <section className={styles.section} aria-labelledby="month-title">
    <div className={styles.heading}>
      <div><h2 id="month-title">When did tornadoes occur?</h2><p>Each date with at least one record counts as one tornado day. Select a month to filter the map and records.</p></div>
      <button type="button" aria-pressed={selected === 0} onClick={() => onSelect(0)}>All months</button>
    </div>
    <table className={styles.monthTable}>
      <thead><tr><th scope="col">Month</th><th scope="col">Tracks</th><th scope="col">Tornado days</th></tr></thead>
      <tbody>{summary.months.map(month => <tr key={month.month}>
        <th scope="row"><button type="button" aria-pressed={selected === month.month} onClick={() => onSelect(month.month)}>{month.name}</button></th>
        <Share count={month.rows.length} total={summary.tracks} kind="tracks"/>
        <Share count={month.dates.size} total={summary.days} kind="days"/>
      </tr>)}</tbody>
    </table>
    <p className={styles.note}>Percentages use the total for each column across the selected years. <a href="#track-chart">View {selected ? MONTHS[selected - 1] : 'all months'} on the map ↓</a></p>
  </section>;
}

function Records({ rows }) {
  const [page, setPage] = useState(0);
  const pages = Math.ceil(rows.length / pageSize);
  if (!pages) return <p>No records for this selection.</p>;
  return <>
    <div className={styles.tableScroll} tabIndex={0} role="region" aria-label="Tornado records">
      <table className={styles.records}>
        <thead><tr><th scope="col">Reported date</th><th scope="col">SPC ID</th><th scope="col">Rating</th><th scope="col">Path length · mi</th><th scope="col">Path width · yd</th><th scope="col">Injuries</th></tr></thead>
        <tbody>{rows.slice(page * pageSize, (page + 1) * pageSize).map(row => <tr key={row.id}>
          <th scope="row">{row.date}</th><td>{row.sourceId}</td><td>{displayRating(row)}</td><td>{number.format(row.length)}</td><td>{number.format(row.width)}</td><td>{number.format(row.injuries)}</td>
        </tr>)}</tbody>
      </table>
    </div>
    <div className={styles.pager}>
      <button type="button" disabled={!page} onClick={() => setPage(page - 1)}>Previous</button>
      <span role="status">Page {page + 1} of {pages}</span>
      <button type="button" disabled={page + 1 >= pages} onClick={() => setPage(page + 1)}>Next</button>
    </div>
  </>;
}

export default function TornadoSeason({ initial }) {
  const [settings, setSettings] = useState(initial);
  const { state, bundle } = useStoryBundle('tornado-tracks');
  const { period: periodId, month, layer } = settings;
  const period = PERIODS.find(option => option.id === periodId);
  const summary = useMemo(() => bundle ? summarizeSeason(bundle.data.records, period) : null, [bundle, period]);
  const selected = useMemo(() => summary ? (month ? [summary.months[month - 1]] : summary.months) : [], [summary, month]);
  const rows = useMemo(() => selected.flatMap(entry => entry.rows).sort((a, b) => b.date.localeCompare(a.date) || a.id.localeCompare(b.id)), [selected]);
  const coverage = useMemo(() => mapCoverage(rows), [rows]);
  const peak = busiestDate(selected);
  const monthLabel = month ? MONTHS[month - 1] : 'All months';
  const source = bundle?.data.sourceSnapshot;

  function update(change) {
    const next = { ...settings, ...change };
    setSettings(next);
    const url = new URL(window.location.href);
    url.searchParams.set('period', next.period);
    if (next.month) url.searchParams.set('month', next.month);
    else url.searchParams.delete('month');
    if (next.layer === 'lines') url.searchParams.set('layer', 'lines');
    else url.searchParams.delete('layer');
    window.history.replaceState(window.history.state, '', url);
  }

  return <main className={styles.page}>
    <div className={styles.frame}>
      <nav className={styles.nav} aria-label="Research navigation">
        <Link href="/science">← Science &amp; Labs</Link><Link href="/labs?story=tornado-tracks">Tornado Tracks ↗</Link>
      </nav>
      <header className={styles.hero}>
        <h1>Tornado Season Lab</h1>
        <p>Does tornado season look different when you count each track or each day with a tornado? Explore the NOAA record for tornadoes reported as starting in Kansas.</p>
      </header>

      <section className={styles.section} aria-labelledby="season-window">
        <div className={styles.heading}>
          <div><h2 id="season-window">Choose a record period</h2><p>See what share of each total fell in April, May, and June.</p></div>
          <label>Record period<select value={periodId} onChange={event => update({ period: event.target.value })}>
            {PERIODS.map(option => <option key={option.id} value={option.id}>{option.label}</option>)}
          </select></label>
        </div>
        {summary ? <div className={styles.metrics} aria-live="polite" aria-atomic="true">
          <article data-kind="tracks"><h3>Tracks in April–June</h3>
            <strong>{percent.format(shareOf(summary.aprilJuneTracks, summary.tracks))}</strong>
            <p>{number.format(summary.aprilJuneTracks)} of {number.format(summary.tracks)} tracks</p>
          </article>
          <article data-kind="days"><h3>Tornado days in April–June</h3>
            <strong>{percent.format(shareOf(summary.aprilJuneDays, summary.days))}</strong>
            <p>{number.format(summary.aprilJuneDays)} of {number.format(summary.days)} dates</p>
          </article>
        </div> : <p className={styles.notice} role="status">{state === 'waiting' || state === 'offline'
          ? 'The NOAA snapshot could not be loaded. Reload this page or open the source below.'
          : 'Loading NOAA tornado records…'}</p>}
      </section>

      {summary && <>
        <MonthTable summary={summary} selected={month} onSelect={value => update({ month: value })}/>
        <section className={styles.section} aria-labelledby="track-chart">
          <div className={styles.heading}>
            <div><h2 id="track-chart">Where did the reports occur?</h2><p>{monthLabel} · {period.label} · {number.format(rows.length)} records</p></div>
            <label>Map layer<select value={layer} onChange={event => update({ layer: event.target.value })}>
              <option value="starts">Reported starts</option><option value="lines">Reported endpoints</option>
            </select></label>
          </div>
          <div className={styles.map}>
            <SeasonMap coverage={coverage} layer={layer}/>
            <p role="status">{layer === 'starts'
              ? `${number.format(coverage.starts.length)} of ${number.format(rows.length)} records have a start in the map frame.`
              : `${number.format(coverage.paths.length)} of ${number.format(rows.length)} records have both endpoints in the map frame.`}</p>
          </div>
          <p className={styles.note}>Each line connects two reported points. The actual path and damage area can differ. {KANSAS_OUTLINE_CREDIT}</p>
        </section>

        <section className={styles.section} aria-labelledby="track-records">
          <div className={styles.heading}>
            <div><h2 id="track-records">Inspect the source records</h2>
              {peak && <p>Most tracks on one reported date in this selection · <strong>{number.format(peak.tracks)}</strong> on {dayLabel.format(new Date(peak.date))}.</p>}
            </div>
            <button type="button" disabled={!rows.length} onClick={() => downloadCSV(`kansas-tornado-season-${periodId}-${month || 'all'}.csv`, seasonCsv(rows))}>Download selected records</button>
          </div>
          <Records key={`${periodId}-${month}`} rows={rows}/>
        </section>
      </>}

      <section className={styles.section} aria-labelledby="season-method">
        <h2 id="season-method">What’s in the archive?</h2>
        <p>The snapshot covers whole tornado records marked as starting in Kansas from 1950 through 2025. A track may end in another state. Earlier reports missed more events, especially weaker ones. The comparison describes the archive and its reporting coverage.</p>
        <p>Damage ratings switched from F to EF on February 1, 2007. The archive includes unknown ratings. Records without usable coordinates or endpoints stay in the counts and CSV.</p>
        <p><a href={source?.url || 'https://www.spc.noaa.gov/wcm/'}>NOAA Storm Prediction Center source ↗</a> · <a href="https://www.weather.gov/oun/efscale">National Weather Service rating guide ↗</a></p>
      </section>
    </div>
  </main>;
}
