'use client';

import Link from 'next/link';
import { useMemo, useState } from 'react';
import { downloadCSV } from '../../living-welcome/stories/story-kit.mjs';
import { useStoryBundle } from '../../living-welcome/stories/useStoryBundle.js';
import { FlowChart } from './FlowChart.jsx';
import { FLOW_SITES, buildFlowComparison, daysAtFlow, flowAtFrequency, flowCsvRows, flowPeriods, gaugeHref, watershedHref } from './flow-model.mjs';
import styles from './river-flow.module.css';

const EMPTY = [];
const amount = new Intl.NumberFormat('en-US', { maximumFractionDigits: 4 });
const thresholdAmount = new Intl.NumberFormat('en-US', { maximumSignificantDigits: 17 });
const percent = new Intl.NumberFormat('en-US', { style: 'percent', maximumFractionDigits: 1 });
const dateLabel = new Intl.DateTimeFormat('en-US', { dateStyle: 'medium', timeZone: 'UTC' });
const displayDate = date => dateLabel.format(new Date(date));
const pageSize = 12;

function GaugeSelect({ label, value, other, onChange }) {
  return <label>{label}
    <select value={value} onChange={event => onChange(event.target.value)}>
      {FLOW_SITES.map(site => <option key={site.id} value={site.id} disabled={site.id === other}>{site.name}</option>)}
    </select>
  </label>;
}

function DailyRecords({ sites, comparison }) {
  const [gapsOnly, setGapsOnly] = useState(false);
  const [page, setPage] = useState(0);
  const days = gapsOnly ? comparison.days.filter(day => !day.included) : comparison.days;
  const pages = Math.ceil(days.length / pageSize);

  return <details className={styles.details}>
    <summary>Inspect daily source records</summary>
    <div className={styles.detailsBody}>
      <p>Values are daily means in ft³/s. USGS qualifiers are shown where supplied.</p>
      <label className={styles.gaps}><input type="checkbox" checked={gapsOnly} onChange={event => { setGapsOnly(event.target.checked); setPage(0); }}/> Show only dates excluded from the comparison</label>
      {days.length ? <>
        <div className={styles.tableScroll} role="region" aria-label="Daily comparison data" tabIndex={0}>
          <table>
            <thead><tr><th scope="col">Date</th>{sites.map(site => <th scope="col" key={site.id}>{site.short}</th>)}<th scope="col">Included</th></tr></thead>
            <tbody>{days.slice(page * pageSize, (page + 1) * pageSize).map(day => <tr key={day.date}>
              <th scope="row">{day.date}</th>{day.readings.map(({ value, qualifiers }, index) => <td key={sites[index].id}>
                {value === null ? 'Missing' : amount.format(value)}
                {qualifiers && <small>{qualifiers}</small>}
              </td>)}<td>{day.included ? 'Yes' : 'No'}</td>
            </tr>)}</tbody>
          </table>
        </div>
        <div className={styles.pagination}>
          <button type="button" disabled={page === 0} onClick={() => setPage(page - 1)}>Previous</button>
          <span role="status">Page {page + 1} of {pages}</span>
          <button type="button" disabled={page + 1 >= pages} onClick={() => setPage(page + 1)}>Next</button>
        </div>
      </> : <p>Both gauges reported flow on every date in this window.</p>}
    </div>
  </details>;
}

export default function RiverFlow({ initial }) {
  const [settings, setSettings] = useState(initial);
  const [threshold, setThreshold] = useState(String(initial.threshold));
  const { state, bundle } = useStoryBundle('river-memory');
  const records = bundle?.data.records ?? EMPTY;
  const periods = useMemo(() => flowPeriods(records), [records]);
  const period = periods.find(option => option.id === settings.period) ?? periods[0];
  const { first, second, frequency, scale } = settings;
  const sites = [FLOW_SITES.find(site => site.id === first), FLOW_SITES.find(site => site.id === second)];
  const comparison = useMemo(() => bundle ? buildFlowComparison(records, period, first, second) : null, [bundle, records, period, first, second]);
  const ready = comparison?.count > 0;
  const readings = ready ? comparison.curves.map(curve => flowAtFrequency(curve, comparison.count, frequency)) : EMPTY;
  const atThreshold = ready ? comparison.curves.map(curve => daysAtFlow(curve, settings.threshold)) : EMPTY;
  const source = bundle?.data.sourceSnapshot;

  function update(patch) {
    const next = { ...settings, period: bundle ? period.id : settings.period, ...patch };
    setSettings(next);
    const url = new URL(window.location.href);
    for (const [key, value] of Object.entries(next)) url.searchParams.set(key, String(value));
    window.history.replaceState(window.history.state, '', url);
  }

  function exportDays() {
    downloadCSV(`kansas-river-flow-${period.id}-${first}-${second}.csv`, flowCsvRows(comparison.days, first, second));
  }

  return <main className={styles.page}>
    <div className={styles.frame}>
      <nav className={styles.navigation} aria-label="Research navigation">
        <Link href="/labs">← Research Labs</Link>
        <Link href="/explore/drought-and-water">Kansas water guide ↗</Link>
      </nav>
      <header className={styles.hero}>
        <h1>River Flow Lab</h1>
        <p>How often did the rivers run high or low? Compare two Kansas gauges using daily USGS records from the same dates.</p>
      </header>

      <section className={styles.setup} aria-labelledby="choose-gauges">
        <h2 id="choose-gauges">Choose two gauges and a period</h2>
        <div className={styles.selects}>
          <GaugeSelect label="First gauge" value={first} other={second} onChange={value => update({ first: value })}/>
          <GaugeSelect label="Second gauge" value={second} other={first} onChange={value => update({ second: value })}/>
          <label>Period
            <select value={bundle ? period.id : settings.period} onChange={event => update({ period: event.target.value })} disabled={!bundle}>
              {!bundle && settings.period !== period.id && <option value={settings.period}>{settings.period}</option>}
              {periods.map(option => <option value={option.id} key={option.id}>{option.label}</option>)}
            </select>
          </label>
        </div>
        {comparison ? <div className={styles.coverage} role="status">
          <strong>{amount.format(comparison.count)} of {amount.format(comparison.days.length)} days compared</strong>
          <span>{displayDate(period.from)} – {displayDate(period.to)} · Both gauges must report flow for a day to count.</span>
          {comparison.missing.some(Boolean) && <span>{sites.map((site, index) => `${site.short}: ${comparison.missing[index]} missing`).join(' · ')}</span>}
        </div> : <p className={styles.load} role="status">{state === 'offline' || state === 'waiting'
          ? 'The USGS snapshot could not be loaded. Reload this page or open the gauge links below.'
          : 'Loading daily USGS records…'}</p>}
      </section>

      {ready && <section className={styles.analysis} aria-labelledby="frequency-title">
        <div className={styles.chartIntro}>
          <div>
            <h2 id="frequency-title">What flow was reached this often?</h2>
            <p>Pick a share of days. The chart shows the daily mean flow each river reached or exceeded that often.</p>
          </div>
          <label>Chart scale <select value={scale} onChange={event => update({ scale: event.target.value })}>
            <option value="compressed">Show low flows clearly</option><option value="linear">Equal spacing (linear)</option>
          </select></label>
        </div>
        <div className={styles.frequency}>
          <div className={styles.frequencyButtons} aria-label="Common frequencies" role="group">
            {[['10', 'High flow'], ['50', 'Typical flow'], ['90', 'Low flow']].map(([value, label]) => <button
              key={value} type="button" aria-pressed={frequency === Number(value)}
              onClick={() => update({ frequency: Number(value) })}>{value}% <span>{label}</span></button>)}
          </div>
          <div className={styles.slider}>
            <label htmlFor="frequency">Share of matched days <strong>{frequency}%</strong></label>
            <input id="frequency" type="range" min="1" max="100" value={frequency} onChange={event => update({ frequency: Number(event.target.value) })}/>
          </div>
        </div>
        <div className={styles.plot}>
          <ul className={styles.key} aria-label="Chart legend">{sites.map((site, index) => <li key={site.id}>
            <i className={styles.line} data-dashed={index === 1} aria-hidden="true"/>{site.short}</li>)}</ul>
          <span className={styles.yLabel}>Daily mean flow (ft³/s)</span>
          <FlowChart curves={comparison.curves} count={comparison.count} frequency={frequency} readings={readings} scale={scale}/>
          <p className={styles.xLabel}>Share of matched days at or above that flow</p>
        </div>
        <div className={styles.values} aria-live="polite" aria-atomic="true">
          {sites.map((site, index) => <div key={site.id} data-dashed={index === 1}>
            <h3>{site.name}</h3>
            <p><strong>{amount.format(readings[index].value)}</strong> ft³/s</p>
            <small>Reached on {amount.format(readings[index].count)} days ({percent.format(readings[index].count / comparison.count)})</small>
          </div>)}
        </div>
      </section>}
      {ready && <section className={styles.threshold} aria-labelledby="threshold-title">
        <h2 id="threshold-title">How often did a flow level occur?</h2>
        <p>Enter a daily mean flow to count how many matched days each gauge reached that value or higher.</p>
        <form onSubmit={event => {
          event.preventDefault();
          const value = event.currentTarget.elements.threshold.valueAsNumber;
          if (Number.isFinite(value) && value >= 0) update({ threshold: value });
        }}>
          <label>Daily flow (ft³/s)<input name="threshold" type="number" min="0" step="any" required value={threshold} onChange={event => setThreshold(event.target.value)}/></label>
          <button type="submit">Count days</button>
        </form>
        <p className={styles.thresholdResult} role="status"><span>At or above <strong>{thresholdAmount.format(settings.threshold)} ft³/s</strong></span>{sites.map((site, index) =>
          <span key={site.id}>{site.name} · <strong>{amount.format(atThreshold[index])} days ({percent.format(atThreshold[index] / comparison.count)})</strong></span>)}</p>
      </section>}
      {comparison && !ready && <p className={styles.load}>Neither chart can be calculated without a date when both gauges reported flow. Try another period or pair.</p>}

      <section className={styles.evidence} aria-labelledby="evidence-title">
        <div className={styles.chartIntro}>
          <div>
            <h2 id="evidence-title">Follow the evidence</h2>
            <p>Open the gauge records or view the gauge and local watershed boundaries in the Explorer.</p>
          </div>
          {comparison && <button type="button" onClick={exportDays}>Download daily CSV</button>}
        </div>
        <ul className={styles.siteLinks}>{sites.map(site => <li key={site.id}>
          <strong>{site.name}</strong>
          <div><Link prefetch={false} href={watershedHref(site)}>Gauge &amp; watershed map ↗</Link>
            <a href={gaugeHref(site)}>USGS gauge {site.id} ↗</a></div>
        </li>)}</ul>
        {comparison && <DailyRecords key={`${first}-${second}-${period.id}`} sites={sites} comparison={comparison}/>}
        <details className={styles.details}>
          <summary>How the comparison works</summary>
          <div className={styles.detailsBody}>
            <p>A flow-duration curve sorts daily means from highest to lowest. At 10%, for example, the lab finds the first rank that covers at least one tenth of the matched dates. Ties include every day with the same flow, so the reported share can be higher than the selected share. At 50%, this method uses an observed middle value.</p>
            <p>The default chart scale uses log(1 + flow) to show differences among low readings and keep zero on the axis. The linear scale gives equal space to equal changes in ft³/s. Both use the same readings.</p>
            <p>The gauges drain different areas. Flow alone does not indicate which site had more runoff per square mile. Daily means smooth short peaks and cannot be used as flood stages or forecasts. USGS provisional and estimated values are retained with their qualifiers. Missing values are excluded from calculations and left blank in the CSV.</p>
            <p><a href="https://www.usgs.gov/publications/flow-duration-curves">USGS flow-duration method ↗</a> · <Link href="/labs?story=river-memory">View the daily timeline in River Memory ↗</Link></p>
            {source && <p><a href={source.url}>USGS source query ↗</a> · Snapshot fetched {displayDate(source.retrievedAt)}. Explorer layers have separate source dates. The watershed layer uses the published USGS boundary archive.</p>}
          </div>
        </details>
      </section>
    </div>
  </main>;
}
