'use client';

import { useMemo } from 'react';
import { fieldLabel, type Collection } from '../collection-metadata';
import {documentedField,documentedCode} from '../collection-field-dictionary';
import {
  measurementDistribution,
  measurementLayer,
  type LabSnapshot,
  type MeasurementBin,
  type profileCollection,
} from '../collection-lab';
import styles from './lab.module.css';
import { sameRange, type LabMeasurementView } from './lab-bundle';

type FieldProfile = ReturnType<typeof profileCollection>['fields'][number];
const isUnit = (name: string) => /(^|_)units?(_|$)/.test(name);

function contextLabel(context: string,collectionId:string) {
  if (!context.startsWith('{')) return context;
  const entries=Object.entries(JSON.parse(context) as Record<string,string>);
  const multipleUnits=entries.filter(([name])=>isUnit(name)).length>1;
  return entries
    .sort(([a], [b]) => Number(isUnit(b)) - Number(isUnit(a)))
    .map(([name, value]) => {
      const meaning=documentedCode(collectionId,name,value);
      const unit=!meaning&&value.trim()&&Number.isFinite(Number(value))?documentedField(collectionId,name)?.unit:null;
      return `${isUnit(name)&&!multipleUnits ? 'Unit' : fieldLabel(name)}: ${value}${unit?` ${unit}`:''}${meaning?` (${meaning})`:''}`;
    })
    .join(' · ');
}

function intervalLabel(bin: MeasurementBin) {
  if (bin.lower === bin.upper) return `Exactly ${bin.lower}`;
  return bin.includeUpper ? `${bin.lower} to ${bin.upper} inclusive` : `${bin.lower} to less than ${bin.upper}`;
}

const compactNumber = new Intl.NumberFormat('en-US', { maximumSignificantDigits: 6 });
const axisNumber = (value: number) => value !== 0 && (Math.abs(value) < 0.001 || Math.abs(value) >= 1e6)
  ? value.toExponential(3)
  : compactNumber.format(value);

export default function MeasurementExplorer({ collection, snapshot, fields, busy, save, view, onViewChange }: {
  collection: Collection;
  snapshot: LabSnapshot;
  fields: ReadonlyArray<FieldProfile>;
  busy: boolean;
  save: (name: string, content: string, type: string) => void;
  view: LabMeasurementView | null;
  onViewChange: (view: LabMeasurementView) => void;
}) {
  const field = fields.find(candidate => candidate.name === view?.field) ?? fields[0];
  const group = field.groups.find(candidate => candidate.context === view?.context) ?? field.groups[0];
  const contextUnits=group.context.startsWith('{')
    ?Object.fromEntries(Object.entries(JSON.parse(group.context) as Record<string,string>).filter(([name])=>isUnit(name)))
    :{};
  const distribution = useMemo(
    () => measurementDistribution(collection, snapshot, field.name, group.context),
    [collection, snapshot, field.name, group.context],
  );
  const layer = useMemo(
    () => collection.geometry ? measurementLayer(collection, snapshot, field.name, group.context) : null,
    [collection, snapshot, field.name, group.context],
  );
  const activeBin = distribution.bins.find(bin => sameRange(view?.range, bin));
  const tallest = Math.max(1, ...distribution.bins.map(bin => bin.count));
  const firstBin = distribution.bins.at(0);
  const lastBin = distribution.bins.at(-1);
  const shortStart = firstBin ? axisNumber(firstBin.lower) : '';
  const shortEnd = lastBin ? axisNumber(lastBin.upper) : '';

  return <section className={styles.measurements} aria-labelledby="measurements-title">
    <div className={styles.measurementIntro}>
      <div>
        <h3 id="measurements-title">Explore measurements</h3>
        <p>Choose a range to inspect the source records behind it.</p>
      </div>
      <p className={styles.measurementTotal}><strong>{distribution.count}</strong> of {snapshot.rows.length} loaded records</p>
    </div>
    <div className={styles.measurementControls}>
      <label>Measurement field
        <select value={field.name} onChange={event => {
          const selected = fields.find(candidate => candidate.name === event.target.value);
          if (selected) onViewChange({ field: selected.name, context: selected.groups[0].context, range: null });
        }}>
          {fields.map(option => <option key={option.name} value={option.name}>{documentedField(collection.id,option.name)?.label??fieldLabel(option.name)}</option>)}
        </select>
      </label>
      <label>Unit &amp; measurement context
        <select value={group.context} onChange={event => onViewChange({ field: field.name, context: event.target.value, range: null })}>
          {field.groups.map(option => <option key={option.context} value={option.context}>{contextLabel(option.context,collection.id)}</option>)}
        </select>
      </label>
    </div>

    {Object.keys(contextUnits).length>0&&<p className={styles.note}>{contextLabel(JSON.stringify(contextUnits),collection.id)}.</p>}
    <details>
      <summary>Selected context · inspect all recorded fields</summary>
      <p className={styles.note}>{contextLabel(group.context,collection.id)}.</p>
    </details>
    {firstBin && lastBin && <div className={styles.measurementPlot} role="region" aria-label="Measurement distribution">
      <p className={styles.plotLabel}>Records per range</p>
      <div className={styles.plotScroll}>
        <div style={{ minWidth: 48 * distribution.bins.length - 4 }}>
          <div className={styles.plotGrid}>
            {distribution.bins.map((bin, index) => <button
              className={styles.binButton}
              type="button"
              key={index}
              title={intervalLabel(bin)}
              aria-label={`${intervalLabel(bin)}: ${bin.count} ${bin.count === 1 ? 'record' : 'records'}`}
              aria-pressed={activeBin === bin}
              aria-controls="measurement-range-records"
              onClick={() => onViewChange({
                field: field.name, context: group.context,
                range: { lower: bin.lower, upper: bin.upper, includeUpper: bin.includeUpper },
              })}
            >
              <span className={styles.binMark} aria-hidden="true" style={{ height: `${100 * bin.count / tallest}%` }}>
                <span>{bin.count}</span>
              </span>
            </button>)}
          </div>
          <div className={styles.plotAxis} aria-hidden="true">
            <span>{shortStart === shortEnd ? firstBin.lower : shortStart}</span>
            {firstBin.lower !== lastBin.upper && <span>{shortStart === shortEnd ? lastBin.upper : shortEnd}</span>}
          </div>
        </div>
      </div>
      <p className={styles.plotLabel}>
        {documentedField(collection.id,field.name)?.label??fieldLabel(field.name)} · {firstBin.lower === lastBin.upper ? 'One recorded value' : 'Recorded value ranges'}
      </p>
    </div>}

    <div id="measurement-range-records" className={styles.rangeRecords}>
      <p role="status" className={styles.rangeStatus}>
        {activeBin ? `${intervalLabel(activeBin)} · ${activeBin.count} ${activeBin.count === 1 ? 'record' : 'records'}` : ''}
      </p>
      {activeBin && (activeBin.count ? <div className={styles.rangeTable} role="region" aria-label="Loaded records in selected range" tabIndex={0}>
        <table aria-label="Records in selected range">
          <thead><tr><th scope="col">Record</th><th scope="col">Recorded value</th><th scope="col">{snapshot.origin ? 'Source listed in file' : 'Source'}</th></tr></thead>
          <tbody>{activeBin.records.map(record => <tr key={record.id}>
            <th scope="row"><code>{record.id}</code></th>
            <td>{record.value}</td>
            <td>{record.sourceUrl
              ? <a href={record.sourceUrl} target="_blank" rel="noopener noreferrer">{record.sourceId ?? 'Provider record'}</a>
              : record.sourceId ?? 'Unavailable'}</td>
          </tr>)}</tbody>
        </table>
      </div> : <p>No loaded records fall in this range.</p>)}
    </div>

    {layer && <div className={styles.measurementExport}>
      <h4>Create a measurement layer</h4>
      <p>Export the whole selected measurement context using validated longitude/latitude geometry.</p>
      <p>{layer.features.length} features · {layer.kfm.omitted.noUsableGeometry} without usable geometry · {layer.kfm.omitted.notNumeric} without a numeric value · {layer.kfm.omitted.otherContext} in other contexts</p>
      <button
        type="button"
        disabled={busy || !layer.features.length}
        onClick={() => save(`${collection.id}-${field.name}.geojson`, JSON.stringify(layer, null, 2), 'application/geo+json')}
      >Download measurement layer · GeoJSON</button>
    </div>}
  </section>;
}
