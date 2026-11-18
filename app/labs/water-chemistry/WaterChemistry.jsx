'use client';

import { useEffect, useMemo, useRef, useState } from 'react';
import Link from 'next/link';
import { downloadCSV } from '../../living-welcome/stories/story-kit.mjs';
import {
  observationDate, rangeLabel, reportingLimit, resultText, unitLabel,
  waterBrief, waterComparison, waterCsvRecords, waterLimits, waterRecordSelection,
} from './water-model.mjs';
import styles from './water.module.css';

const significant = new Intl.NumberFormat('en-US', { maximumSignificantDigits: 4 });
const mapArea = '/?c=-97.42,37.88&z=11&topic=water';

function saveText(filename, content, type) {
  const url = URL.createObjectURL(new Blob([content], { type }));
  const link = document.createElement('a');
  link.href = url;
  link.download = filename;
  document.body.append(link);
  link.click();
  link.remove();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}

function PeriodCard({ period }) {
  return <article className={styles.period} data-period={period.id}>
    <h3>{period.label}</h3>
    <p className={styles.median}><strong>{period.median === null ? '—' : significant.format(period.median)}</strong> <span>{unitLabel}</span></p>
    <p className={styles.medianNote}>Median of quantified results</p>
    <dl>
      <div><dt>Quantified</dt><dd>{period.quantified}</dd></div>
      <div><dt>Non-detects</dt><dd>{period.nonDetects}</dd></div>
      <div><dt>Sampled months</dt><dd>{period.sampledMonths} / 24</dd></div>
    </dl>
    <p className={styles.dates}>Samples from <time dateTime={period.firstDate}>{period.firstDate}</time> through <time dateTime={period.lastDate}>{period.lastDate}</time></p>
  </article>;
}

function ComparisonChart({ bins, periods, interval, onSelect }) {
  const counts = bins.map(bin => periods.map(period => bin.records.filter(record => record.period === period.id).length));
  const scale = Math.max(1, ...counts.flat());
  return <div className={styles.chart}>
    <div className={styles.chartHeader}>
      <h3>Quantified samples by concentration</h3>
      <ul aria-label="Sample periods" className={styles.legend}>
        {periods.map(period => <li key={period.id} data-period={period.id}><i aria-hidden="true"/>{period.label}</li>)}
      </ul>
    </div>
    <p className={styles.axisTitle}>Samples per range</p>
    <div className={styles.plotScroll}>
      <div className={styles.plot} role="group" aria-label="Nitrate distributions on matching concentration ranges">
        {bins.map((bin, index) => <button
          type="button"
          key={bin.lower}
          className={styles.bin}
          aria-pressed={interval === index}
          aria-controls="water-records"
          aria-label={`${rangeLabel(bin)} ${unitLabel}. ${periods.map((period, i) => `${period.label}, ${counts[index][i]} samples`).join('. ')}`}
          onClick={() => onSelect(index)}
        >
          {periods.map((period, i) => <span
            className={styles.bar}
            key={period.id}
            data-period={period.id}
            style={{ height: `${counts[index][i] / scale * 100}%` }}
            aria-hidden="true"
          ><span>{counts[index][i]}</span></span>)}
        </button>)}
      </div>
      <div aria-hidden="true" className={styles.axis}>
        <span>0</span>{bins.map(bin => <span key={bin.upper}>{bin.upper}</span>)}
      </div>
    </div>
    <p className={styles.axisTitle}>Dissolved nitrate · {unitLabel}. Choose a range to inspect its records.</p>
  </div>;
}

function SourceRecord({ record, sourceUrl, headingRef }) {
  const entry = record.source;
  const fields = [
    ['Date', entry.ActivityStartDate], ['Local time', entry['ActivityStartTime/Time']],
    ['Provider time zone', entry['ActivityStartTime/TimeZoneCode']],
    ['Activity', entry.ActivityTypeCode], ['Analytical method', entry['ResultAnalyticalMethod/MethodName']],
    ['Collection method', entry['SampleCollectionMethod/MethodName']], ['Sampler', entry.SampleCollectionEquipmentName],
    ['Hydrologic condition', entry.HydrologicCondition], ['Hydrologic event', entry.HydrologicEvent],
    ['Provider result status', entry.ResultStatusIdentifier], ['Qualifier', entry.MeasureQualifierCode],
  ];
  if (record.status === 'not-detected') {
    fields.push(['Detection condition', entry.ResultDetectionConditionText], [
      'Provider reporting limit',
      `${reportingLimit(record)} ${entry['DetectionQuantitationLimitMeasure/MeasureUnitCode']}`,
    ]);
  } else {
    fields.push(['Provider result', `${entry.ResultMeasureValue} ${entry['ResultMeasure/MeasureUnitCode']}`]);
  }
  return <article className={styles.recordDetail} aria-labelledby="water-exact-record">
    <h3 tabIndex={-1} ref={headingRef} id="water-exact-record">Source activity <code>{record.activityId}</code></h3>
    <dl>{fields.map(([label, value]) => <div key={label}><dt>{label}</dt><dd>{value || 'Unspecified in source'}</dd></div>)}</dl>
    <details>
      <summary>Provider row fields</summary>
      <pre>{JSON.stringify(entry, null, 2)}</pre>
    </details>
    <a href={sourceUrl} target="_blank" rel="noreferrer">Open the provider result query ↗</a>
  </article>;
}

export default function WaterChemistry({ snapshot }) {
  const { summaries, bins } = useMemo(() => waterComparison(snapshot), [snapshot]);
  const [period, setPeriod] = useState('all');
  const [detection, setDetection] = useState('all');
  const [interval, setInterval] = useState(null);
  const [selectedId, setSelectedId] = useState('');
  const recordHeading = useRef(null);
  const activeRange = interval === null ? null : bins[interval];
  const rows = waterRecordSelection(snapshot, { period, detection, interval: activeRange });
  const selected = rows.find(record => record.activityId === selectedId);
  const resultSource = snapshot.sources.results;

  useEffect(() => {
    if (selectedId) recordHeading.current?.focus();
  }, [selectedId]);

  function openRange(index) {
    setInterval(current => current === index ? null : index);
    setPeriod('all');
    setDetection('all');
    setSelectedId('');
  }

  return <main className={styles.page}>
    <div className={styles.container}>
      <nav className={styles.nav} aria-label="Water Chemistry navigation">
        <Link href="/labs" prefetch={false}>All Labs</Link>
        <a href="#water-comparison">Compare samples</a>
        <a href="#water-sources">Sources</a>
      </nav>
      <header className={styles.hero}>
        <div>
          <p className={styles.eyebrow}>Kansas Frontier Matrix · Water Chemistry</p>
          <h1>One river, two sample windows.</h1>
          <p>Follow dissolved nitrate results from a single Kansas station. Compare samples reported in the same units, with the same collection equipment and calculation method.</p>
        </div>
        <aside className={styles.station} aria-label="Study station">
          <p className={styles.eyebrow}>USGS station {snapshot.station.id}</p>
          <h2>{snapshot.station.name}</h2>
          <div><Link href={mapArea} prefetch={false}>Open station area on map ↗</Link><a href={snapshot.station.url} target="_blank" rel="noreferrer">USGS station record ↗</a></div>
        </aside>
      </header>

      <section className={styles.comparison} id="water-comparison" aria-labelledby="water-comparison-title">
        <div className={styles.sectionHead}>
          <h2 id="water-comparison-title">Compare the sample windows</h2>
          <p>Dissolved nitrate as nitrogen · USGS parameter 00618</p>
        </div>
        <div className={styles.periods}>
          {summaries.map(item => <PeriodCard key={item.id} period={item}/>)}
        </div>
        <ComparisonChart bins={bins} periods={summaries} interval={interval} onSelect={openRange}/>
        <p className={styles.note}>{waterLimits[1]}</p>
      </section>

      <section className={styles.records} id="water-records" aria-labelledby="water-record-title">
        <div className={styles.sectionHead}>
          <h2 id="water-record-title">Inspect the records</h2>
          <p role="status">{rows.length} {rows.length === 1 ? 'record' : 'records'} shown{activeRange ? ` · ${rangeLabel(activeRange)} ${unitLabel}` : ''}</p>
        </div>
        <div className={styles.filters}>
          <label>Sample window<select value={period} onChange={event => {
            setPeriod(event.target.value);
            setSelectedId('');
          }}>
            <option value="all">Both sample windows</option>
            {summaries.map(item => <option key={item.id} value={item.id}>{item.label}</option>)}
          </select></label>
          <label>Result type<select value={detection} onChange={event => {
            setDetection(event.target.value);
            setInterval(null);
            setSelectedId('');
          }}>
            <option value="all">Quantified and non-detects</option>
            <option value="numeric">Quantified only</option>
            <option value="not-detected">Non-detects only</option>
          </select></label>
          {activeRange && <button type="button" onClick={() => {
            setInterval(null);
            setSelectedId('');
          }}>Clear range</button>}
        </div>
        {rows.length ? <div className={styles.tableScroll} tabIndex={0} role="region" aria-label="Water Chemistry records">
          <table>
            <caption className={styles.srOnly}>Dissolved nitrate source records at the Sedgwick station</caption>
            <thead><tr><th scope="col">Sample date</th><th scope="col">Reported result</th><th scope="col">Provider activity</th></tr></thead>
            <tbody>{rows.map(record => <tr key={record.activityId} data-selected={record === selected}>
              <th scope="row"><time dateTime={observationDate(record)}>{observationDate(record)}</time></th>
              <td>{resultText(record)}{record.status === 'numeric' ? ` ${unitLabel}` : ''}</td>
              <td><button type="button" aria-pressed={record === selected} onClick={() => {
                if (record === selected) recordHeading.current?.focus();
                else setSelectedId(record.activityId);
              }}>{record.activityId}</button></td>
            </tr>)}</tbody>
          </table>
        </div> : <p className={styles.note}>No samples match this selection.</p>}
        {selected && <SourceRecord record={selected} sourceUrl={resultSource.url} headingRef={recordHeading}/>}
        <div className={styles.actions}>
          <button type="button" disabled={!rows.length} onClick={() => downloadCSV('sedgwick-nitrate-records.csv', waterCsvRecords(rows))}>Download visible records · CSV</button>
          <button type="button" onClick={() => saveText('sedgwick-nitrate-brief.md', waterBrief(snapshot), 'text/markdown')}>Download comparison brief · Markdown</button>
          <button type="button" onClick={() => saveText('sedgwick-nitrate-snapshot.json', JSON.stringify(snapshot, null, 2), 'application/json')}>Download source snapshot · JSON</button>
        </div>
      </section>

      <section className={styles.sources} id="water-sources" aria-labelledby="water-source-title">
        <div className={styles.sectionHead}><h2 id="water-source-title">Sources and limits</h2></div>
        <p>{snapshot.credit.name}. Results were reported as computations by the NWIS algorithm. This comparison retains routine surface-water samples with USGS collection method 15 and the US DH-81 sampler.</p>
        <ul>{waterLimits.map(limit => <li key={limit}>{limit}</li>)}</ul>
        <details className={styles.sourceReceipt}>
          <summary>Acquisition and selection receipt</summary>
          <p>Snapshot retrieved <time dateTime={resultSource.retrievedAt}>{resultSource.retrievedAt}</time>. Raw result response size {resultSource.rawBytes.toLocaleString('en-US')} bytes.</p>
          <p>Raw response SHA-256 <code>{resultSource.sha256}</code></p>
          <ul>{summaries.map(item => <li key={item.id}>{item.label} · {item.returned} provider rows, {item.retained} retained, {item.otherContext} outside the fixed comparison context, {item.qualifiedOther} with other qualifications.</li>)}</ul>
          <p>Station map link opens the nearby area. The provider records NAD83 and reports horizontal accuracy of {snapshot.station.horizontalAccuracy} {snapshot.station.horizontalAccuracyUnit}.</p>
        </details>
        <div className={styles.sourceLinks}>
          <a href={resultSource.url} target="_blank" rel="noreferrer">Water Quality Portal result query ↗</a>
          <a href={snapshot.station.providerUrl} target="_blank" rel="noreferrer">Provider station metadata ↗</a>
          <a href={snapshot.credit.rightsUrl} target="_blank" rel="noreferrer">USGS data credit ↗</a>
          <Link href="/data-lab?collection=observations-wqp-results&pack=water-land" prefetch={false}>Open full WQP archive in Record Lab ↗</Link>
        </div>
      </section>
    </div>
  </main>;
}
