'use client';

import Link from 'next/link';
import { useMemo, useRef, useState } from 'react';
import { downloadCSV, KANSAS_OUTLINE_CREDIT } from '../../living-welcome/stories/story-kit.mjs';
import { useStoryBundle } from '../../living-welcome/stories/useStoryBundle.js';
import EpicenterMap from './EpicenterMap.jsx';
import { catalogCsv, catalogWindow, compareCatalog, PERIODS } from './catalog-model.mjs';
import styles from './earthquake.module.css';

const amount = new Intl.NumberFormat('en-US', { maximumFractionDigits: 2 });
const mag = value => value.toFixed(1);
const countLabel = (count, unit) => `${amount.format(count)} ${unit}${count === 1 ? '' : 's'}`;
const pageSize = 10;
const usgsDocs = 'https://www.usgs.gov/programs/earthquake-hazards/anss-comprehensive-earthquake-catalog-comcat-documentation';
const explorer = '/?topic=geology&ctx=usgs-earthquakes,usgs-3dep-hillshade&c=-98.6,38.3&z=6&panel=layers&motion=off';

function PeriodChoice({ label, value, other, onChange }) {
  return <label>{label}
    <select value={value} onChange={event => onChange(event.target.value)}>
      {PERIODS.map(period => <option key={period.id} value={period.id} disabled={period.id === other}>{period.label}</option>)}
    </select>
  </label>;
}

function PeriodSummary({ result, index }) {
  return <article className={styles.summary} data-period={index}>
    <h3>{result.period.label}</h3>
    <p className={styles.rate}><strong>{amount.format(result.perYear)}</strong> catalog records per year</p>
    <p>{countLabel(result.selected.length, 'record')} across four calendar years</p>
    <dl className={styles.years}>{result.years.map(({ year, count }) => <div key={year}>
      <dt>{year}</dt><dd>{amount.format(count)}</dd>
    </div>)}</dl>
    <p>{result.depthCount ? <><strong>{amount.format(result.medianDepth)} km</strong> median reported depth · {countLabel(result.depthCount, 'depth value')}</> : 'No reported depths in this selection.'}</p>
  </article>;
}

function ThresholdChart({ comparison, threshold, onSelect }) {
  const max = Math.max(1, ...comparison.flatMap(result => result.curve.map(point => point.perYear)));
  return <section className={styles.card} aria-labelledby="threshold-chart">
    <h2 id="threshold-chart">How does the minimum magnitude change the counts?</h2>
    <p>Each row counts earthquakes at or above that magnitude. Select a row to update the comparison and map. Small events are easier to miss, and detection can change over time.</p>
    <table className={styles.chart}>
      <thead><tr><th scope="col">At least</th>{comparison.map(result =>
        <th scope="col" key={result.period.id}>{result.period.label}</th>)}</tr></thead>
      <tbody>{comparison[0].curve.map(({ mag: minimum }, index) => (
        <tr key={minimum}>
          <th scope="row"><button type="button" aria-pressed={minimum === threshold} onClick={() => onSelect(minimum)}>M {mag(minimum)}</button></th>
          {comparison.map((result, period) => {
            const { perYear } = result.curve[index];
            return <td key={result.period.id}>
              <span className={styles.barTrack} data-period={period} aria-hidden="true"><i style={{ width: `${100 * Math.log1p(perYear) / Math.log1p(max)}%` }}/></span>
              <span className={styles.barValue}>{amount.format(perYear)}</span>
            </td>;
          })}
        </tr>
      ))}</tbody>
    </table>
    <p className={styles.caption}>Values are catalog records per year. Bar lengths use log(1 + rate) to keep small counts visible. Zero has no bar.</p>
  </section>;
}

function Records({ comparison, onLocate }) {
  const [page, setPage] = useState(0);
  const [periodIndex, setPeriodIndex] = useState(0);
  const rows = useMemo(() => [...comparison[periodIndex].selected]
    .sort((a, b) => b.magnitude - a.magnitude || a.date.localeCompare(b.date)), [comparison, periodIndex]);
  const pages = Math.ceil(rows.length / pageSize);

  return <>
    <label className={styles.tableChoice}>Records from period
      <select value={periodIndex} onChange={event => { setPeriodIndex(Number(event.target.value)); setPage(0); }}>
        {comparison.map(({ period }, index) => <option key={period.id} value={index}>{period.label}</option>)}
      </select>
    </label>
    {pages ? <>
      <div className={styles.tableScroll} role="region" aria-label="Earthquake catalog records" tabIndex={0}>
        <table className={styles.records}>
          <thead><tr><th scope="col">Place</th><th scope="col">Date (UTC)</th><th scope="col">Magnitude</th><th scope="col">Depth (km)</th><th scope="col">Status</th><th scope="col">Map</th></tr></thead>
          <tbody>{rows.slice(page * pageSize, (page + 1) * pageSize).map(row => <tr key={row.id}>
            <th scope="row"><a href={row.url}>{row.name} ↗</a></th>
            <td>{row.date.slice(0, 10)}</td><td>{amount.format(row.magnitude)} <small>{row.magnitudeType}</small></td>
            <td>{Number.isFinite(row.depth) ? amount.format(row.depth) : 'Missing'}</td><td>{row.status}</td>
            <td><button type="button" aria-label={`Locate ${row.name} on ${row.date.slice(0, 10)}`} onClick={() => onLocate(row, periodIndex)}>Locate</button></td>
          </tr>)}</tbody>
        </table>
      </div>
      <div className={styles.pager}>
        <button type="button" disabled={!page} onClick={() => setPage(page - 1)}>Previous</button>
        <span role="status">Page {page + 1} of {pages}</span>
        <button type="button" disabled={page + 1 === pages} onClick={() => setPage(page + 1)}>Next</button>
      </div>
    </> : <p>No events in this period met the selected magnitude.</p>}
  </>;
}

export default function EarthquakeLab({ initial }) {
  const [settings, setSettings] = useState(initial);
  const [layer, setLayer] = useState('both');
  const [selected, setSelected] = useState(null);
  const mapHeading = useRef(null);
  const { bundle, state } = useStoryBundle('shaking-ground');
  const source = bundle?.data.sourceSnapshot;
  const coverage = useMemo(() => catalogWindow(source?.url), [source?.url]);
  const { first, second, mag: threshold } = settings;
  const comparison = useMemo(() => bundle ? compareCatalog(
    bundle.data.records, [PERIODS.find(period => period.id === first), PERIODS.find(period => period.id === second)],
    threshold, coverage,
  ) : null, [bundle, first, second, threshold, coverage]);
  const ready = comparison?.every(Boolean);

  function update(change) {
    const next = { ...settings, ...change };
    setSettings(next);
    setSelected(null);
    const url = new URL(window.location.href);
    for (const [key, value] of Object.entries(next)) url.searchParams.set(key, String(value));
    window.history.replaceState(window.history.state, '', url);
  }

  function locate(row, periodIndex) {
    setSelected(row);
    if (layer !== 'both') setLayer(String(periodIndex));
    mapHeading.current?.focus();
  }

  return <main className={styles.page}>
    <div className={styles.frame}>
      <nav className={styles.nav} aria-label="Research navigation">
        <Link href="/science">← Science &amp; Labs</Link>
        <Link href="/labs?story=shaking-ground">Shaking Ground ↗</Link>
      </nav>
      <header className={styles.hero}>
        <h1>Earthquake Catalog Lab</h1>
        <p>Compare recorded earthquakes around Kansas. Raise the minimum magnitude to see how the difference between two periods changes.</p>
      </header>
      <section className={styles.card} aria-labelledby="compare-title">
        <h2 id="compare-title">Compare two four-year periods</h2>
        <div className={styles.setup}>
          <PeriodChoice label="First period" value={first} other={second} onChange={value => update({ first: value })}/>
          <PeriodChoice label="Second period" value={second} other={first} onChange={value => update({ second: value })}/>
          <div className={styles.range}>
            <label htmlFor="quake-threshold">Minimum magnitude <strong>M {mag(threshold)}</strong></label>
            <input id="quake-threshold" type="range" step=".1" min="1" max="5" value={threshold}
              aria-valuetext={`Magnitude ${mag(threshold)} or greater`} onChange={event => update({ mag: Number(event.target.value) })}/>
          </div>
        </div>
        {ready ? <div className={styles.summaries} aria-live="polite" aria-atomic="true">
          {comparison.map((result, index) => <PeriodSummary key={result.period.id} result={result} index={index}/>)}
        </div> : <p className={styles.notice} role="status">{bundle ? 'The snapshot does not cover both complete comparison periods.' :
          state === 'waiting' || state === 'offline' ? 'The USGS snapshot could not be loaded. Reload the page or open the USGS catalog below.' : 'Loading the USGS catalog snapshot…'}</p>}
      </section>
      {ready && <>
        <ThresholdChart comparison={comparison} threshold={threshold} onSelect={value => update({ mag: value })}/>
        <section className={styles.card} aria-labelledby="catalog-map">
          <div className={styles.sectionIntro}>
            <div>
              <h2 id="catalog-map" ref={mapHeading} tabIndex={-1}>Where did the records cluster?</h2>
              <p>One symbol per catalog epicenter at M {mag(threshold)} or above. Symbols can overlap.</p>
            </div>
            <label>Map layer<select value={layer} onChange={event => { setLayer(event.target.value); setSelected(null); }}>
              <option value="both">Both periods</option>
              {comparison.map(({ period }, index) => <option key={period.id} value={String(index)}>{period.label}</option>)}
            </select></label>
          </div>
          <div className={styles.map}>
            <ul className={styles.legend} aria-label="Map legend">
              {comparison.map(({ period, selected: events }, index) => (layer === 'both' || Number(layer) === index) &&
                <li key={period.id}><i data-period={index} aria-hidden="true"/>{period.label} · {countLabel(events.length, 'epicenter')}</li>)}
              <li><i data-period="boundary" aria-hidden="true"/>Catalog search box</li>
            </ul>
            <EpicenterMap comparison={comparison} layer={layer} selected={selected}/>
            {selected && <p className={styles.located} role="status">Highlighted <a href={selected.url}>{selected.name} ↗</a> · {selected.date.slice(0, 10)} UTC · M {amount.format(selected.magnitude)}</p>}
          </div>
          <p className={styles.caption}>{KANSAS_OUTLINE_CREDIT} The search box extends into neighboring states. <Link href={explorer} prefetch={false}>Open recent USGS earthquakes and shaded relief in Explorer ↗</Link></p>
        </section>
        <section className={styles.card} aria-labelledby="catalog-evidence">
          <div className={styles.sectionIntro}>
            <div><h2 id="catalog-evidence">Inspect the records</h2><p>Open an event in USGS or locate it on the historical map.</p></div>
            <button type="button" onClick={() => downloadCSV(`kansas-earthquake-catalog-${first}-${second}-M${mag(threshold)}.csv`, catalogCsv(comparison))}>Download selected records</button>
          </div>
          <Records key={`${first}-${second}-${threshold}`} comparison={comparison} onLocate={locate}/>
        </section>
      </>}
      <section className={styles.card} aria-labelledby="catalog-method">
        <h2 id="catalog-method">What the catalog can tell us</h2>
        <p>The comparison divides qualifying records by four calendar years. A zero means the snapshot returned no records at that threshold. Detection varies by place and year, especially for small earthquakes. Magnitude types are kept as USGS reported them.</p>
        <p>Depths are source estimates. The chart and map describe catalog records and cannot establish what caused an earthquake or predict future shaking.</p>
        <p>{coverage && <>The query covers {coverage.start} through midnight UTC at the start of {coverage.end}. The comparison uses complete years through 2025. </>}
          <a href={usgsDocs}>USGS catalog documentation ↗</a>{source && <> · <a href={source.url}>Source query ↗</a></>}</p>
      </section>
    </div>
  </main>;
}
