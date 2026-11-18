'use client';

import Link from 'next/link';
import { useState } from 'react';
import styles from './drought-replay.module.css';

const fullDate = new Intl.DateTimeFormat('en-US', { month: 'long', day: 'numeric', timeZone: 'UTC' });
const shortDate = new Intl.DateTimeFormat('en-US', { month: 'short', day: 'numeric', timeZone: 'UTC' });
const dayName = new Intl.DateTimeFormat('en-US', { weekday: 'short', timeZone: 'UTC' });
const percent = new Intl.NumberFormat('en-US', { style: 'percent', maximumFractionDigits: 2 });
const discharge = new Intl.NumberFormat('en-US', { maximumFractionDigits: 3 });
const formatDay = (value, format = fullDate) => format.format(new Date(`${value}T00:00:00Z`));
const formatShare = value => percent.format(value / 100);
const overviewLabels = new Set([0, 4, 8, 12, 16]);

export default function DroughtReplay({ snapshot, initialWeek }) {
  const { weeks, dailyFlow, sources, station } = snapshot;
  const peakShare = Math.max(...weeks.map(week => week.shares[4]));
  const peakIndex = weeks.findIndex(week => week.shares[4] === peakShare);
  const requestedIndex = weeks.findIndex(week => week.validFrom === initialWeek);
  const [index, setIndex] = useState(requestedIndex < 0 ? peakIndex : requestedIndex);
  const week = weeks[index];
  const readings = dailyFlow.filter(row => row.date >= week.validFrom && row.date <= week.validThrough);
  const zeroDays = dailyFlow.filter(row => row.value === 0).length;
  const mapDate = week.validFrom.replaceAll('-', '');
  const map = `/?topic=agriculture&drought=${mapDate}&c=-100.8774,37.9559&z=8.8&base=civic&panel=layers&motion=off`;

  function selectWeek(next) {
    const target = weeks[next];
    if (!target) return;
    setIndex(next);
    const address = new URL(window.location.href);
    address.searchParams.set('week', target.validFrom);
    window.history.replaceState(window.history.state, '', address);
  }

  function downloadRecords() {
    const file = new Blob([JSON.stringify(snapshot, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(file);
    const link = document.createElement('a');
    link.href = url;
    link.download = 'finney-county-drought-replay-2012.json';
    link.click();
    window.setTimeout(() => URL.revokeObjectURL(url), 1000);
  }

  return <main className={styles.page}>
    <div className={styles.frame}>
      <nav className={styles.breadcrumb} aria-label="Research navigation"><Link href="/labs">Research Labs</Link><span aria-hidden="true">/</span><span>2012 Drought Replay</span></nav>
      <header className={styles.header}>
        <p className={styles.eyebrow}>Finney County, Kansas · June–October 2012</p>
        <h1>The 2012 drought at Garden City</h1>
        <p>Exceptional drought covered {formatShare(weeks[0].shares[4])} of Finney County on {formatDay(weeks[0].validFrom)} and {formatShare(peakShare)} on {formatDay(weeks[peakIndex].validFrom)}. The Garden City gauge reported a daily mean of 0 {station.unit} on {zeroDays} of {dailyFlow.length} days in this replay.</p>
      </header>

      <section className={styles.panel} aria-labelledby="county-drought-title">
        <div className={styles.panelHeading}>
          <div><h2 id="county-drought-title">How much of the county was in drought?</h2><p>Weekly share of Finney County in extreme or exceptional drought</p></div>
          <Link className={styles.action} href={map} prefetch={false}>Open this week on the map <span aria-hidden="true">↗</span></Link>
        </div>
        <div className={styles.legend} aria-hidden="true"><span><i className={styles.extreme}/> Extreme (D3)</span><span><i className={styles.exceptional}/> Exceptional (D4)</span></div>
        <div className={styles.graph} aria-hidden="true">
          <div className={styles.scale}><span>100%</span><span>50%</span><span>0%</span></div>
          <div className={styles.plot}>{weeks.map((item, position) => <div key={item.validFrom} className={styles.column} data-selected={position === index}>
            <div className={styles.stack}>
              <div className={styles.extreme} style={{ height: `${item.shares[3] - item.shares[4]}%` }}/>
              <div className={styles.exceptional} style={{ height: `${item.shares[4]}%` }}/>
            </div>
            {overviewLabels.has(position) && <span className={styles.axisDate}>{formatDay(item.validFrom, shortDate)}</span>}
          </div>)}</div>
        </div>
        <div className={styles.weekControls}>
          <label htmlFor="drought-week">Assessment date <output htmlFor="drought-week">{formatDay(week.validFrom)}</output></label>
          <input id="drought-week" type="range" min="0" max={weeks.length - 1} step="1" value={index} aria-valuetext={formatDay(week.validFrom)} onChange={event => selectWeek(Number(event.target.value))}/>
          <div className={styles.presets}>
            <button type="button" aria-pressed={index === 0} onClick={() => selectWeek(0)}>First assessment</button>
            <button type="button" aria-pressed={index === peakIndex} onClick={() => selectWeek(peakIndex)}>First peak</button>
            <button type="button" aria-pressed={index === weeks.length - 1} onClick={() => selectWeek(weeks.length - 1)}>Last assessment</button>
          </div>
        </div>
        <dl className={styles.shares} aria-live="polite">
          <div><dt>Moderate or worse</dt><dd>{formatShare(week.shares[1])}</dd></div>
          <div><dt>Severe or worse</dt><dd>{formatShare(week.shares[2])}</dd></div>
          <div><dt>Extreme or worse</dt><dd>{formatShare(week.shares[3])}</dd></div>
          <div><dt>Exceptional</dt><dd>{formatShare(week.shares[4])}</dd></div>
        </dl>
      </section>

      <section className={styles.panel} aria-labelledby="daily-flow-title">
        <div className={styles.panelHeading}>
          <div><h2 id="daily-flow-title">What did the river gauge record?</h2><p>Daily mean discharge · Arkansas River at Garden City · USGS 07139000</p></div>
          <a className={styles.action} href="https://waterdata.usgs.gov/monitoring-location/USGS-07139000/">Open USGS station <span aria-hidden="true">↗</span></a>
        </div>
        <div className={styles.tableWrap}>
          <table className={styles.readings}>
            <caption>{formatDay(week.validFrom)}–{formatDay(week.validThrough)}, 2012 · {readings.length} daily records</caption>
            <thead><tr>{readings.map(row => <th key={row.date} scope="col"><span>{formatDay(row.date, dayName)}</span>{formatDay(row.date, shortDate)}</th>)}</tr></thead>
            <tbody><tr>{readings.map(row => <td key={row.date}>{discharge.format(row.value)}<small> {station.unit}</small></td>)}</tr></tbody>
          </table>
        </div>
        <p className={styles.clockNote}>The county assessment uses Tuesday as its valid date and is released Thursday. The table shows approved daily means for the seven calendar dates in that assessment’s validity interval. Some readings are dated after the assessment.</p>
      </section>

      <section className={styles.sources} aria-labelledby="replay-sources-title">
        <h2 id="replay-sources-title">Sources and limits</h2>
        <p>The county shares apply to land area. Streamflow describes one monitoring station. Read the records together as historical context and use basin records to investigate what influenced the river.</p>
        <ul>
          <li><a href={sources.drought.url}>Finney County weekly area statistics</a> · U.S. Drought Monitor</li>
          <li><a href="https://droughtmonitor.unl.edu/About/WhatistheUSDM.aspx">How the U.S. Drought Monitor is made</a> · National Drought Mitigation Center</li>
          <li><a href={sources.flow.url}>Garden City daily mean discharge records</a> · U.S. Geological Survey</li>
        </ul>
        <button className={styles.action} type="button" onClick={downloadRecords}>Download source records (JSON)</button>
      </section>
    </div>
  </main>;
}
