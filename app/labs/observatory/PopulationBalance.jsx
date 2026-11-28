'use client';

import { useEffect, useRef, useState } from 'react';
import { downloadCSV } from '../../living-welcome/stories/story-kit.mjs';
import { populationBalanceCsv } from '../population-components.mjs';
import styles from './population-balance.module.css';

const count = new Intl.NumberFormat('en-US', { maximumFractionDigits: 0 });
const mean = new Intl.NumberFormat('en-US', { maximumFractionDigits: 1 });
const signedCount = new Intl.NumberFormat('en-US', { maximumFractionDigits: 0, signDisplay: 'exceptZero' });
const signedRate = new Intl.NumberFormat('en-US', { maximumFractionDigits: 3, signDisplay: 'exceptZero' });
const compact = new Intl.NumberFormat('en-US', { notation: 'compact', maximumFractionDigits: 1, signDisplay: 'exceptZero' });
const calendar = new Intl.DateTimeFormat('en-US', { dateStyle: 'medium', timeZone: 'UTC' });
const finite = value => typeof value === 'number' && Number.isFinite(value);
const people = value => finite(value) ? signedCount.format(value === 0 ? 0 : value) : 'Unavailable';
const rate = value => finite(value) ? signedRate.format(value === 0 ? 0 : value) : 'Unavailable';
const date = value => value ? calendar.format(new Date(`${value}T12:00:00Z`)) : 'Date unavailable';
const countyName = result => result?.name || (result?.fips ? `County ${result.fips}` : 'County unavailable');
const shortLabels = {
  births: ['Births'], deaths: ['Deaths'], netMigration: ['Net', 'migration'],
  remainder: ['Balance', 'remainder'], change: ['Net', 'change'],
};

function steps(result) {
  let cumulative = 0;
  const components = result.contributions.map(component => {
    const from = cumulative;
    cumulative += component.people;
    return { ...component, from, to: cumulative };
  });
  return [...components, { key: 'change', label: 'Net population change', people: result.change, from: 0, to: result.change }];
}

function sharedScale(results) {
  const values = results.filter(result => result?.status === 'ready').flatMap(result => steps(result).flatMap(step => [step.from, step.to]));
  const lower = Math.min(0, ...values), upper = Math.max(0, ...values);
  const padding = (upper - lower || 1) * .15;
  return { min: lower - padding, max: upper + padding, ticks: [...new Set([lower, 0, upper])] };
}

function Waterfall({ result, slot, scale, tableId }) {
  const ref = useRef(null), [width, setWidth] = useState(560);
  useEffect(() => {
    if (!ref.current || typeof ResizeObserver === 'undefined') return;
    const observer = new ResizeObserver(entries => {
      const measured = Math.round(entries[0]?.contentRect.width || 0);
      if (measured) setWidth(Math.max(250, measured));
    });
    observer.observe(ref.current);
    return () => observer.disconnect();
  }, []);
  const bars = steps(result), left = 45, right = width - 12, top = 30, bottom = 204, height = 267;
  const band = (right - left) / bars.length, barWidth = Math.min(46, band * .56);
  const x = index => left + band * (index + .5);
  const y = value => bottom - (value - scale.min) / (scale.max - scale.min) * (bottom - top);
  const color = slot === 'A' ? '#e3c78b' : '#7dd5d5';
  const patternId = `population-balance-${slot}-${result.fips}-negative`;
  return <figure className={styles.figure}>
    <figcaption>Four components, one population balance<span>Shared people scale for A and B · totals start at zero</span></figcaption>
    <svg ref={ref} className={styles.plot} viewBox={`0 0 ${width} ${height}`} role="img" aria-label={`${slot}: ${countyName(result)}. Births add ${count.format(result.births)} people, deaths subtract ${count.format(result.deaths)}, net migration contributes ${people(result.netMigration)}, and the calculated balance remainder contributes ${people(result.remainder)}. Net population change is ${people(result.change)} people. Exact values follow in the table.`} aria-describedby={tableId} data-min={scale.min} data-max={scale.max}>
      <defs><pattern id={patternId} width="6" height="6" patternUnits="userSpaceOnUse"><rect width="6" height="6" fill={color} fillOpacity=".2"/><path d="M-1 1L1-1M0 6L6 0M5 7L7 5" stroke={color} strokeWidth="1.1"/></pattern></defs>
      {scale.ticks.map(tick => <g key={tick}><line x1={left} x2={right} y1={y(tick)} y2={y(tick)} stroke={tick === 0 ? '#c7dbe6' : '#789aa440'} strokeWidth={tick === 0 ? 1.2 : 1} data-waterfall-zero={tick === 0 ? true : undefined}/><text x={left - 7} y={y(tick) + 4} textAnchor="end" fill="#bbd2d9" fontSize="10">{compact.format(tick)}</text></g>)}
      {bars.slice(0, -1).map((bar, index) => <line key={bar.key} x1={x(index) + barWidth / 2} x2={x(index + 1) - barWidth / 2} y1={y(bar.to)} y2={y(bar.to)} stroke="#b4cbd580" strokeDasharray="3 3"/>)}
      {bars.map((bar, index) => <g key={bar.key}>
        <rect x={x(index) - barWidth / 2} y={Math.min(y(bar.from), y(bar.to))} width={barWidth} height={Math.abs(y(bar.from) - y(bar.to))} fill={bar.people < 0 ? `url(#${patternId})` : color} fillOpacity={bar.key === 'remainder' ? .35 : bar.key === 'change' ? .7 : 1} stroke={color} strokeWidth={bar.key === 'change' ? 2 : 1} strokeDasharray={bar.key === 'remainder' ? '3 2' : undefined} data-waterfall-component={bar.key} data-people={bar.people} data-from={bar.from} data-to={bar.to}><title>{`${bar.label}: ${people(bar.people)} people; balance moves from ${people(bar.from)} to ${people(bar.to)}.`}</title></rect>
        {bar.people === 0 && <line x1={x(index) - barWidth / 2} x2={x(index) + barWidth / 2} y1={y(bar.from)} y2={y(bar.from)} stroke={color} strokeWidth="1"/>}
        <text x={x(index)} y={Math.min(y(bar.from), y(bar.to)) - 8} textAnchor="middle" fill="#f6efe0" fontSize="10">{people(bar.people)}</text>
        <text x={x(index)} y={bottom + 25} textAnchor="middle" fill="#bbd2d9" fontSize="10">{shortLabels[bar.key].map((label, line) => <tspan key={label} x={x(index)} dy={line ? 13 : 0}>{label}</tspan>)}</text>
      </g>)}
    </svg>
    <p className={styles.chartNote}>Hatched bars subtract people; a dashed outline marks the calculated remainder. Connectors follow the running balance. The final bar shows net change from zero.</p>
  </figure>;
}

function exactRows(result) {
  return [
    ...result.contributions,
    { key: 'naturalChange', label: 'Natural change · births minus deaths', people: result.naturalChange, per1000: result.naturalChangePer1000, subtotal: true },
    { key: 'change', label: 'Net population change', people: result.change, per1000: result.changePer1000, total: true },
  ];
}

function ExactValues({ result, id, print = false }) {
  return <table id={id} className={print ? undefined : styles.exactTable}>
    <caption>People and KFM-calculated contributions per 1,000 mean estimated residents. Counts reconcile exactly. Rates are rounded to three decimal places and may not sum after rounding; CSV retains calculation values.</caption>
    <thead><tr><th scope="col">Component</th><th scope="col">People</th><th scope="col">Per 1,000 mean residents</th></tr></thead>
    <tbody>{exactRows(result).map(row => <tr key={row.key} data-component={row.key} data-people={row.people} data-per1000={row.per1000} data-subtotal={row.subtotal || undefined} data-total={row.total || undefined}>
      <th scope="row">{row.label}{row.subtotal && <small>Subtotal only; not an additional component</small>}</th><td>{people(row.people)}</td><td>{rate(row.per1000)}</td>
    </tr>)}</tbody>
  </table>;
}

function Equation({ result, className }) {
  const expression = result.contributions.map((component, index) => `${index ? component.people < 0 ? '− ' : '+ ' : component.people < 0 ? '−' : ''}${count.format(Math.abs(component.people))}`).join(' ');
  return <p className={className}><span>Births − deaths + net migration + calculated balance remainder</span>{' '}<strong>{expression} = {people(result.change)} people</strong></p>;
}

function CountyBalance({ result, slot, scale }) {
  const tableId = `population-balance-values-${slot}`;
  return <article className={styles.county} data-population-county={result?.fips || ''} data-status={result?.status || 'unavailable'} data-slot={slot} aria-labelledby={`population-balance-county-${slot}`}>
    <header className={styles.countyHeading}><span>COUNTY {slot}</span><h3 id={`population-balance-county-${slot}`}>{countyName(result)}</h3></header>
    {result?.status !== 'ready' ? <p className={styles.notice} role="status">{result?.reason || 'The public source record is unavailable for this county and year. No population balance is drawn.'}</p> : <>
      <p className={styles.interval}><time dateTime={result.beginDate}>{date(result.beginDate)}</time><span aria-hidden="true"> → </span><time dateTime={result.endDate}>{date(result.endDate)}</time></p>
      <dl className={styles.endpoints}><div data-population="begin" data-people={result.beginPopulation}><dt>Beginning population</dt><dd>{count.format(result.beginPopulation)}</dd></div><div data-population="end" data-people={result.endPopulation}><dt>Ending population</dt><dd>{count.format(result.endPopulation)}</dd></div><div className={styles.netChange} data-population="change" data-people={result.change}><dt>Net change</dt><dd>{people(result.change)}</dd></div></dl>
      <p className={styles.componentDates}>Estimated components: <time dateTime={result.componentFrom}>{date(result.componentFrom)}</time> to <time dateTime={result.componentTo}>{date(result.componentTo)}</time>.</p>
      <Waterfall result={result} slot={slot} scale={scale} tableId={tableId}/>
      <div className={styles.exactValues}><Equation result={result} className={styles.equation}/><ExactValues result={result} id={tableId}/><p className={styles.denominator}>KFM normalization denominator: ({count.format(result.beginPopulation)} + {count.format(result.endPopulation)}) ÷ 2 = <strong>{mean.format(result.meanPopulation)}</strong> mean estimated residents. Each signed contribution ÷ this denominator × 1,000 gives the displayed rate.</p></div>
    </>}
  </article>;
}

function HistoryValues({ rows, slot, name }) {
  return <div className={styles.historyScroll} role="region" tabIndex={0} aria-label={`Population component history for county ${slot}, ${name}`}>
    <table className={styles.historyTable} data-history-slot={slot}><caption>{slot} · {name}. July 1 endpoint years, 2021–2025. Births and deaths below are positive source counts; change, migration and calculated remainder retain their signs. Unavailable intervals stay unavailable.</caption>
      <thead><tr><th scope="col">Endpoint year</th><th scope="col">Beginning population</th><th scope="col">Ending population</th><th scope="col">Births</th><th scope="col">Deaths</th><th scope="col">Natural change</th><th scope="col">Net migration</th><th scope="col">Calculated balance remainder</th><th scope="col">Net change</th><th scope="col">Change per 1,000 mean residents</th></tr></thead>
      <tbody>{rows.map(row => <tr key={row.year} data-history-year={row.year} data-status={row.status}><th scope="row">{row.year}<small>{date(row.componentFrom)} – {date(row.componentTo)}</small></th>{row.status !== 'ready' ? <td colSpan={9}>{row.reason || 'Interval unavailable'}</td> : <>
        <td>{count.format(row.beginPopulation)}</td><td>{count.format(row.endPopulation)}</td><td>{count.format(row.births)}</td><td>{count.format(row.deaths)}</td><td>{people(row.naturalChange)}</td><td>{people(row.netMigration)}</td><td>{people(row.remainder)}</td><td>{people(row.change)}</td><td>{rate(row.changePer1000)}</td>
      </>}</tr>)}</tbody>
    </table>
  </div>;
}

function SourceNotes({ analysis, print = false }) {
  const { source, method } = analysis;
  return <div className={print ? undefined : styles.method}>
    <h3>One source vintage, a transparent calculation.</h3>
    <p>{method.description}</p>
    <p><strong>Calculated balance remainder</strong> is the difference needed to reconcile the retained fields with endpoint population change. It is a KFM calculation, not a separately retained Census residual field. Net migration is a net balance, not arrivals, departures or individual tracking.</p>
    <p>Annual estimates from one vintage can be revised. Components describe estimated accounting, not why a county changed. The 2020 partial-year interval is excluded from this annual comparison.</p>
    <p>{source.name}{source.preparedAt && <> · public snapshot prepared <time dateTime={source.preparedAt}>{source.preparedAt}</time></>}</p>
    <p className={print ? undefined : styles.fingerprint}>Public snapshot SHA-256: <code>{source.sha256 || 'Unavailable'}</code></p>
    {source.sourceSnapshot && <div><p>Original Census source retrieved {source.capturedAt ? <time dateTime={source.capturedAt}>{source.capturedAt}</time> : 'at an unavailable time'}{source.sourceSnapshot.rawBytes && <> · {count.format(source.sourceSnapshot.rawBytes)} bytes</>}. Retrieval time is separate from the estimated population interval.</p>{source.sourceSnapshot.rawSha256 && <p className={print ? undefined : styles.fingerprint}>Raw source SHA-256: <code>{source.sourceSnapshot.rawSha256}</code></p>}</div>}
    <ul className={print ? undefined : styles.sourceLinks}>
      {source.snapshotPath && <li><a href={source.snapshotPath} download>Download the public source snapshot <span aria-hidden="true">↓</span></a></li>}
      {(source.sources || []).map((item, index) => <li key={`${item.url}-${index}`}><a href={item.url}>{item.name || 'Original Census source'} <span aria-hidden="true">↗</span></a>{item.citation && <span>{item.citation}</span>}{item.license && <span>{item.license}</span>}</li>)}
      {(method.documentation || []).map(item => <li key={item.href}><a href={item.href}>{item.title} <span aria-hidden="true">↗</span></a></li>)}
    </ul>
  </div>;
}

export default function PopulationBalance({ analysis }) {
  if (!analysis) return <section id="population-balance" tabIndex={-1} className={styles.section} aria-labelledby="population-balance-title"><header className={styles.heading}><div><h2 id="population-balance-title" tabIndex={-1}>What adds up to population change?</h2><p role="status">Reading the public population record. Exact county balances appear when their source is available.</p></div></header></section>;
  const scale = sharedScale([analysis.countyA, analysis.countyB]);
  return <section id="population-balance" tabIndex={-1} className={styles.section} data-year={analysis.selection.year} aria-labelledby="population-balance-title">
    <header className={styles.heading}><div><span className={styles.eyebrow}>ACCOUNT FOR THE CHANGE</span><h2 id="population-balance-title" tabIndex={-1}>What adds up to population change?</h2><p>Follow the existing A/B counties through the annual interval ending in {analysis.selection.year}. The <a href="#county-source-periods">Population year above</a> sets this view; the five-year history stays available below.</p></div><button type="button" onClick={() => downloadCSV('kfm-population-components-history.csv', populationBalanceCsv(analysis))}>Download population history CSV ↓</button></header>
    <div className={styles.counties}><CountyBalance result={analysis.countyA} slot="A" scale={scale}/><CountyBalance result={analysis.countyB} slot="B" scale={scale}/></div>
    <details className={styles.history}><summary>Inspect the five-year population balance history · 2021–2025</summary><HistoryValues rows={analysis.history.a} slot="A" name={countyName(analysis.countyA)}/><HistoryValues rows={analysis.history.b} slot="B" name={countyName(analysis.countyB)}/></details>
    <SourceNotes analysis={analysis}/>
  </section>;
}

export function PopulationBalancePrint({ analysis }) {
  if (!analysis) return null;
  return <section><h2>Population change components · {analysis.selection.year}</h2><p>The selected Population year determines the annual interval. Counts come from the public Census snapshot, independently of any private county attachment.</p>
    {[['A', analysis.countyA], ['B', analysis.countyB]].map(([slot, result]) => <section key={slot}><h3>{slot} · {countyName(result)}</h3>{result?.status !== 'ready' ? <p>{result?.reason || 'This interval is unavailable.'}</p> : <>
      <p>July 1 endpoints: {date(result.beginDate)} · {count.format(result.beginPopulation)} people; {date(result.endDate)} · {count.format(result.endPopulation)} people. Estimated component period: {date(result.componentFrom)} to {date(result.componentTo)}.</p><Equation result={result}/><ExactValues result={result}/><p>Mean estimated population denominator: ({count.format(result.beginPopulation)} + {count.format(result.endPopulation)}) ÷ 2 = {mean.format(result.meanPopulation)}. KFM contribution rate = signed people ÷ mean estimated residents × 1,000. Natural change is a subtotal, not another contribution.</p>
    </>}</section>)}<SourceNotes analysis={analysis} print/>
  </section>;
}
