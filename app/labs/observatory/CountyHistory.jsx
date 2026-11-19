'use client';
import { useEffect, useRef, useState } from 'react';
import { downloadCSV } from '../../living-welcome/stories/story-kit.mjs';
import { safeCell } from '../../living-welcome/stories/record-model.mjs';
import styles from './history.module.css';

const number = new Intl.NumberFormat('en-US', { maximumFractionDigits: 2 });
const compact = new Intl.NumberFormat('en-US', { notation: 'compact', maximumFractionDigits: 1 });
const finite = value => typeof value === 'number' && Number.isFinite(value);
const currency = metric => /dollar|income|homevalue|rent/i.test(`${metric?.unit} ${metric?.key}`);
function format(value, metric = {}) {
  if (!finite(value)) return 'Unavailable';
  if (currency(metric)) return `$${number.format(value)}`;
  return `${number.format(value)}${metric.unit === '%' ? '%' : ''}`;
}
function HistoryPlot({ rows, metric, counties, uncertainty = false }) {
  const ref = useRef(null), [width, setWidth] = useState(560);
  useEffect(() => {
    if (!ref.current) return;
    const observer = new ResizeObserver(entries => {
      const measured = Math.round(entries[0]?.contentRect.width || 0);
      if (measured) setWidth(Math.max(250, measured));
    });
    observer.observe(ref.current);
    return () => observer.disconnect();
  }, []);
  const left = 59, right = width - 35, top = 22, bottom = 205, height = 258;
  const values = rows.flatMap(row => ['A', 'B'].flatMap(side => {
    const value = row[`value${side}`], moe = row[`moe${side}`];
    return finite(value) ? uncertainty && finite(moe) ? [value - moe, value + moe] : [value] : [];
  }));
  const minimum = values.length ? Math.min(...values) : 0, maximum = values.length ? Math.max(...values) : 1;
  const pad = (maximum - minimum || Math.abs(maximum) || 1) * .12;
  const min = minimum - pad, max = maximum + pad;
  const x = index => rows.length < 2 ? (left + right) / 2 : left + index / (rows.length - 1) * (right - left);
  const y = value => bottom - (value - min) / (max - min) * (bottom - top);
  return <svg ref={ref} className={styles.plot} viewBox={`0 0 ${width} ${height}`} role="img" aria-label={`${metric.label}, ${counties.a.name} in gold and ${counties.b.name} in cyan. ${uncertainty ? 'Vertical bars show 90 percent margins of error. Period estimates are separate points.' : 'Annual population estimates; gaps are not connected.'} Exact values follow in the history table.`}>
    <rect width={width} height={height} fill="#071e2c"/>
    {[0, .5, 1].map(tick => { const value = min + (max - min) * tick; return <g key={tick}><line x1={left} x2={right} y1={y(value)} y2={y(value)} stroke="#c5dbe025"/><text x={left - 9} y={y(value) + 4} textAnchor="end" fill="#bbd2d9" fontSize="11">{currency(metric) ? '$' : ''}{compact.format(value)}{metric.unit === '%' ? '%' : ''}</text></g>; })}
    {rows.map((row, index) => <text key={row.year} x={x(index)} y={bottom + 24} textAnchor="middle" fill="#bbd2d9" fontSize="11">{uncertainty ? row.period : row.year}</text>)}
    {['A', 'B'].map((side, sideIndex) => <g key={side}>
      {!uncertainty && rows.slice(1).map((row, index) => finite(rows[index][`value${side}`]) && finite(row[`value${side}`]) && row.year === rows[index].year + 1 ? <line key={row.year} x1={x(index)} y1={y(rows[index][`value${side}`])} x2={x(index + 1)} y2={y(row[`value${side}`])} stroke={sideIndex ? '#7dd5d5' : '#e3c78b'} strokeWidth="2"/> : null)}
      {rows.map((row, index) => { const value = row[`value${side}`], moe = row[`moe${side}`], at = x(index) + (uncertainty ? sideIndex ? 5 : -5 : 0); return !finite(value) ? null : <g key={row.year} fill={sideIndex ? '#7dd5d5' : '#e3c78b'} stroke={sideIndex ? '#7dd5d5' : '#e3c78b'}>{uncertainty && finite(moe) && <><line x1={at} x2={at} y1={y(value - moe)} y2={y(value + moe)} strokeWidth="1.5"/><line x1={at - 4} x2={at + 4} y1={y(value - moe)} y2={y(value - moe)}/><line x1={at - 4} x2={at + 4} y1={y(value + moe)} y2={y(value + moe)}/></>}<circle cx={at} cy={y(value)} r="4" stroke="#071e2c" strokeWidth="1.2"><title>{side}: {counties[side.toLowerCase()].name} · {row.period} · {format(value, metric)}{finite(moe) ? ` ± ${format(moe, metric)} (90% MOE)` : ''}</title></circle></g>; })}
    </g>)}
    {!values.length && <text x={width / 2} y={110} textAnchor="middle" fill="#bbd2d9" fontSize="13">No estimates available for these counties</text>}
  </svg>;
}

export default function CountyHistory({ analysis, metrics, metricKey, onMetricChange, sourceBindings }) {
  if (!analysis) return null;
  const { counties, population, conditions } = analysis;
  const metric = analysis.metric || metrics[0] || { key: 'unavailable', label: 'ACS measure', unit: '' };
  if (!counties.a || !counties.b || !analysis.metric) return <section className={styles.section} aria-labelledby="county-history-title"><header className={styles.heading}><div><h2 id="county-history-title">County histories</h2><p>{analysis.reason || 'Choose two available counties to see their histories.'}</p></div>{metrics.length > 0 && <label>ACS history measure<select value="" onChange={event => onMetricChange(event.target.value)}><option value="" disabled>Choose a history measure</option>{metrics.map(option => <option key={option.key} value={option.key}>{option.label}</option>)}</select></label>}</header></section>;
  const exportHistory = () => downloadCSV('kfm-county-history.csv', [
    ['source', 'county_fips', 'county_name', 'measure', 'period', 'year', 'estimate', 'margin_of_error_90pct', 'unit', 'snapshot_sha256'],
    ...[['census-mosaic', population, { key: 'population', unit: 'people' }], ['county-conditions', conditions, metric]].flatMap(([source, records, descriptor]) => records.flatMap(row => ['A', 'B'].map(side => [source, counties[side.toLowerCase()].fips, safeCell(counties[side.toLowerCase()].name), descriptor.key, row.period, row.year, row[`value${side}`] ?? '', row[`moe${side}`] ?? '', row.unit || descriptor.unit, sourceBindings[source] || '']))),
  ]);
  return <section className={styles.section} aria-labelledby="county-history-title">
    <header className={styles.heading}><div><span className={styles.eyebrow}>04 / FOLLOW CHANGE, KEEP THE UNCERTAINTY</span><h2 id="county-history-title">How did these places change?</h2><p>Follow the same A/B counties through every available population year and ACS period.</p></div><button type="button" onClick={exportHistory}>Download history CSV ↓</button></header>
    <div className={styles.legend}><span><i/>A · {counties.a.name}</span><span><i/>B · {counties.b.name}</span></div>
    {analysis.reason && <p className={styles.notice} role="status">{analysis.reason}</p>}
    <div className={styles.charts}>
      <figure><figcaption><h3>Annual population</h3><p>July 1 estimates · one Census vintage</p></figcaption><HistoryPlot rows={population} metric={{ key: 'population', label: 'Population', unit: 'people' }} counties={counties}/><p className={styles.chartNote}>Annual points are connected only across consecutive years. The vertical scale follows these two counties.</p></figure>
      <figure><figcaption><label>ACS history measure<select value={metrics.some(option => option.key === metricKey) ? metricKey : ''} onChange={event => onMetricChange(event.target.value)}>{!metrics.some(option => option.key === metricKey) && <option value="" disabled>Choose a history measure</option>}{metrics.map(option => <option key={option.key} value={option.key}>{option.label}</option>)}</select></label><p>{currency(metric) ? 'Vintage-year dollars · not inflation adjusted' : metric.unit} · separate five-year estimates</p></figcaption><HistoryPlot rows={conditions} metric={metric} counties={counties} uncertainty/><p className={styles.chartNote}>Bars show available 90% margins of error. The three nonoverlapping periods are separate estimates; overlap of bars is not a formal significance test.</p></figure>
    </div>
    {currency(metric) && <p className={styles.notice}><strong>Dollar years differ.</strong> Income, home values and rent use each release year’s dollars. A larger later estimate alone does not establish greater purchasing power.</p>}
    <details className={styles.values}><summary>Inspect all history values and margins of error</summary><div className={styles.tableScroll} tabIndex={0} aria-label="Scrollable county history table"><table><caption>Population and {metric.label.toLowerCase()}. Missing estimates remain unavailable.</caption><thead><tr><th>Measure / period</th><th>A · {counties.a.name}</th><th>B · {counties.b.name}</th><th>Unit</th></tr></thead><tbody>{population.map(row => <tr key={`p${row.year}`}><th scope="row">Population<small>{row.period}</small></th><td>{format(row.valueA)}</td><td>{format(row.valueB)}</td><td>people</td></tr>)}{conditions.map(row => <tr key={`a${row.year}`}><th scope="row">{metric.label}<small>{row.period} ACS</small></th>{['A', 'B'].map(side => <td key={side}>{format(row[`value${side}`], metric)}<small>{finite(row[`moe${side}`]) ? `± ${format(row[`moe${side}`], metric)} · 90% MOE` : 'MOE unavailable'}</small></td>)}<td>{row.unit || metric.unit}</td></tr>)}</tbody></table></div></details>
    <p className={styles.method}>{analysis.method} The full history uses all available periods independently of the source-year controls above. Missing values are never filled.</p>
  </section>;
}
