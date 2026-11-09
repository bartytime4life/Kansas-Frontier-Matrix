'use client';
import { useEffect, useMemo, useRef, useState } from 'react';
import { KANSAS_BOUNDS, KANSAS_OUTLINE_CREDIT, cividis, fmt, kansasPath, kansasProjection, useStoryCanvas } from './story-kit.mjs';
import { compareGroups, comparisonMode, comparisonModes, describe, distribution, filterRecords, metricOf, monthlySeries, numeric, recordGeometry, recordModel, recordOutsideBounds, recordRange, recordsCSV, timeText, yearCounts } from './record-model.mjs';
import './record-lab.css';

export const range = recordRange;
export const toCSV = recordsCSV;
const number = value => fmt(value, { digits: value !== null && !Number.isInteger(value) && Math.abs(value) < 10 ? 2 : 0 });
const nameOf = record => String(record?.name || record?.label || record?.id || 'Unnamed record');
const display = value => value === null || value === undefined || value === '' ? 'Not recorded' : typeof value === 'number' ? number(value) : typeof value === 'object' ? JSON.stringify(value) : String(value);
const columnLabel = (model, column) => column.key === model.yearField && model.data.timeUnit === 'Ma' ? 'Age midpoint before present' : column.label;
const INK = '#071c29', GOLD = '#ebca87', WATER = '#78cbd2';

// Keep SVG units equal to rendered CSS pixels so axes remain legible on phones.
// Thumbnail graphics retain their original composition and do not need an observer.
function useChartWidth(compact = false, enabled = true) {
  const ref = useRef(null), [width, setWidth] = useState(720);
  useEffect(() => {
    if (compact || !enabled || !ref.current) return undefined;
    const observer = new ResizeObserver(entries => {
      const measured = Math.round(entries[0]?.contentRect.width || 0);
      if (measured > 0) setWidth(Math.max(200, measured));
    });
    observer.observe(ref.current);
    return () => observer.disconnect();
  }, [compact, enabled]);
  return [ref, compact ? 720 : width];
}

function geometryParts(geometry) {
  if (!geometry?.coordinates) return [];
  const c = geometry.coordinates;
  if (geometry.type === 'Point') return [{ type: 'point', coordinates: [c] }];
  if (geometry.type === 'MultiPoint') return c.map(point => ({ type: 'point', coordinates: [point] }));
  if (geometry.type === 'LineString') return [{ type: 'line', coordinates: c }];
  if (geometry.type === 'MultiLineString') return c.map(line => ({ type: 'line', coordinates: line }));
  if (geometry.type === 'Polygon') return [{ type: 'polygon', rings: c, coordinates: c.flat() }];
  if (geometry.type === 'MultiPolygon') return c.map(polygon => ({ type: 'polygon', rings: polygon, coordinates: polygon.flat() }));
  return [];
}
function mapModel(model) {
  const mapped = model.records.map(row => ({ row, parts: geometryParts(recordGeometry(row)) })).filter(item => item.parts.length);
  return { mapped };
}
function boundsFor(mapped, includeKansas = true) {
  const bounds = includeKansas ? { ...KANSAS_BOUNDS } : { west: Infinity, east: -Infinity, south: Infinity, north: -Infinity };
  for (const item of mapped) for (const part of item.parts) for (const [lon, lat] of part.coordinates) {
    if (numeric(lon) === null || numeric(lat) === null || Math.abs(lon) > 180 || Math.abs(lat) > 90) continue;
    bounds.west = Math.min(bounds.west, lon); bounds.east = Math.max(bounds.east, lon);
    bounds.south = Math.min(bounds.south, lat); bounds.north = Math.max(bounds.north, lat);
  }
  return bounds;
}
function trace(ctx, coordinates, projection, close = false) {
  coordinates.forEach(([lon, lat], index) => { const x = projection.x(lon), y = projection.y(lat); if (index) ctx.lineTo(x, y); else ctx.moveTo(x, y); });
  if (close) ctx.closePath();
}
function drawMap(ctx, frame, scene, records, metric, selected, hitState, compact = false, zoom = 1, extent = 'kansas') {
  const { w, h } = frame, pad = compact ? 12 : 38, selectedSet = new Set(records);
  const mapped = scene.mapped.filter(item => selectedSet.has(item.row)), bounds = extent === 'kansas' ? KANSAS_BOUNDS : boundsFor(mapped);
  const baseProjection = kansasProjection(w, h, { padding: pad, bounds });
  const selectedParts = selected ? geometryParts(recordGeometry(selected)) : [];
  const selectedBounds = selectedParts.length ? boundsFor([{ parts: selectedParts }], false) : null;
  const candidateAnchor = selectedParts[0]?.type === 'point' ? selectedParts[0].coordinates[0] : selectedBounds ? [(selectedBounds.west + selectedBounds.east) / 2, (selectedBounds.south + selectedBounds.north) / 2] : baseProjection.invert(w / 2, h / 2);
  const anchor = candidateAnchor[0] >= bounds.west && candidateAnchor[0] <= bounds.east && candidateAnchor[1] >= bounds.south && candidateAnchor[1] <= bounds.north ? candidateAnchor : baseProjection.invert(w / 2, h / 2);
  const projection = zoom === 1 ? baseProjection : { ...baseProjection, x: lon => w / 2 + (baseProjection.x(lon) - baseProjection.x(anchor[0])) * zoom, y: lat => h / 2 + (baseProjection.y(lat) - baseProjection.y(anchor[1])) * zoom };
  ctx.fillStyle = INK; ctx.fillRect(0, 0, w, h);
  const outline = kansasPath(projection);
  ctx.fillStyle = '#123244'; ctx.fill(outline);
  ctx.strokeStyle = '#8aa9b26b'; ctx.lineWidth = 1; ctx.stroke(outline);
  if (!compact) {
    ctx.font = '11px ui-monospace, monospace'; ctx.textAlign = 'center';
    for (let lon = Math.ceil(bounds.west); lon < bounds.east; lon += 2) {
      const x = projection.x(lon); ctx.strokeStyle = '#b3d4df12'; ctx.beginPath(); ctx.moveTo(x, 24); ctx.lineTo(x, h - 28); ctx.stroke();
      ctx.fillStyle = '#90aeb9'; ctx.fillText(`${Math.abs(lon)}°W`, x, h - 10);
    }
    for (let lat = Math.ceil(bounds.south); lat < bounds.north; lat++) {
      const y = projection.y(lat); ctx.strokeStyle = '#b3d4df12'; ctx.beginPath(); ctx.moveTo(28, y); ctx.lineTo(w - 18, y); ctx.stroke();
      ctx.fillStyle = '#90aeb9'; ctx.fillText(`${lat}°N`, 19, y - 5);
    }
  }
  const summary = describe(records, metric?.key), hits = [];
  const draw = (item, active) => {
    const value = numeric(item.row[metric?.key]), relative = value === null ? null : (value - summary.min) / (summary.max - summary.min || 1);
    const color = active ? '#fff4ce' : relative === null ? '#91a9b1' : cividis(.18 + relative * .82);
    for (const part of item.parts) {
      const path = new Path2D();
      if (part.type === 'point') { const [lon, lat] = part.coordinates[0]; path.arc(projection.x(lon), projection.y(lat), active ? 7 : compact ? 2 : 3.5, 0, Math.PI * 2); }
      else if (part.type === 'polygon') for (const ring of part.rings) trace(path, ring, projection, true);
      else trace(path, part.coordinates, projection);
      ctx.fillStyle = color; ctx.strokeStyle = color; ctx.lineJoin = 'round'; ctx.lineCap = 'round'; ctx.lineWidth = active ? 3 : compact ? 1 : 1.6;
      if (part.type === 'polygon') { ctx.globalAlpha = active ? .7 : .43; ctx.fill(path, 'evenodd'); ctx.globalAlpha = active ? 1 : .8; ctx.stroke(path); }
      else if (part.type === 'point') { ctx.globalAlpha = active ? 1 : .83; ctx.fill(path); if (active) { ctx.strokeStyle = '#061a26'; ctx.lineWidth = 2; ctx.stroke(path); } }
      else { ctx.globalAlpha = .8; ctx.stroke(path); }
      if (!compact) hits.push({ row: item.row, path, type: part.type });
    }
  };
  ctx.save();
  if (extent === 'kansas') { ctx.beginPath(); ctx.rect(projection.x(bounds.west), projection.y(bounds.north), projection.x(bounds.east) - projection.x(bounds.west), projection.y(bounds.south) - projection.y(bounds.north)); ctx.clip(); }
  for (const item of mapped) if (item.row.id !== selected?.id && (extent !== 'kansas' || !recordOutsideBounds(item.row, bounds))) draw(item, false);
  if (selected && (extent !== 'kansas' || !recordOutsideBounds(selected, bounds))) { const item = scene.mapped.find(entry => entry.row === selected); if (item) draw(item, true); }
  ctx.restore();
  ctx.globalAlpha = 1;
  if (!compact) { ctx.fillStyle = GOLD; ctx.textAlign = 'right'; ctx.font = '600 11px ui-monospace, monospace'; ctx.fillText('N ↑', w - 14, 20); }
  if (hitState) hitState.current = { hits, ctx, dpr: frame.dpr };
}

function SpatialView({ scene, records, metric, selected, onSelect, compact = false, defaultExtent = 'kansas' }) {
  const [zoom, setZoom] = useState(1);
  const [extent, setExtent] = useState(defaultExtent);
  const hitState = useRef(null), summary = describe(records, metric?.key), count = records.filter(row => recordGeometry(row)).length;
  const outside = records.filter(row => recordOutsideBounds(row, KANSAS_BOUNDS)).length;
  const ref = useStoryCanvas({ animate: false, deps: [scene, records, metric, selected, zoom, extent], draw(ctx, frame) { drawMap(ctx, frame, scene, records, metric, selected, hitState, compact, zoom, compact ? 'kansas' : extent); } });
  const select = event => {
    const current = hitState.current, box = event.currentTarget.getBoundingClientRect(); if (!current) return;
    const x = (event.clientX - box.left) * current.dpr, y = (event.clientY - box.top) * current.dpr;
    current.ctx.save(); current.ctx.lineWidth = 12;
    const hit = [...current.hits].reverse().find(item => current.ctx.isPointInPath(item.path, x, y, 'evenodd') || current.ctx.isPointInStroke(item.path, x, y));
    current.ctx.restore(); if (hit) onSelect?.(hit.row.id);
  };
  if (compact) return <canvas ref={ref} className="story-canvas" aria-hidden="true"/>;
  return <figure className="record-map">
    <div className="record-map-extent"><label>Map extent<select value={extent} onChange={event => { setExtent(event.target.value); setZoom(1); }}><option value="kansas">Kansas</option><option value="all">All source locations</option></select></label><span>Extent changes the map only. Table and exports retain every selected record.</span></div>
    <div className="record-map-tools" role="group" aria-label="Map magnification"><button type="button" aria-label="Zoom out" disabled={zoom <= 1} onClick={() => setZoom(Math.max(1, zoom / 2))}>−</button><span>{zoom}×</span><button type="button" aria-label="Zoom in around selected record" disabled={zoom >= 16} onClick={() => setZoom(Math.min(16, zoom * 2))}>+</button><button type="button" onClick={() => setZoom(1)}>Fit</button></div>
    <canvas ref={ref} onClick={select} role="img" aria-label={`${count.toLocaleString()} matching records mapped at source coordinates. Color encodes ${metric?.label || 'availability'}. Select an individual record using the record table below.`}/>
    <figcaption><span><b>{count.toLocaleString()}</b> located · {records.length - count} without geometry</span><span>{zoom > 1 ? 'Zoom centered on selection · Fit restores extent' : 'Source geometry · select a record to center zoom'}</span></figcaption>
    {extent === 'kansas' && <p className="record-extent-note" role="status"><b>{outside.toLocaleString()}</b> located record{outside === 1 ? '' : 's'} entirely outside the Kansas frame. {outside > 0 ? 'Choose All source locations to inspect these source coordinates.' : 'All selected geometry extents intersect this frame.'}{zoom > 1 ? ' Magnification may place additional marks outside the viewport; Fit restores the chosen extent.' : ''}</p>}
    {metric && summary.count > 0 && <div className="record-map-key"><span>{metric.label}{metric.unit ? ` · ${metric.unit}` : ''}</span><div><b>{number(summary.min)}</b><i style={{ background: `linear-gradient(90deg,${[.18, .38, .58, .78, 1].map(cividis).join(',')})` }}/><b>{number(summary.max)}</b></div><small>Gray = not recorded · scale follows selection</small></div>}
  </figure>;
}

function DistributionView({ records, metric, selected, compact = false }) {
  const [chartRef, w] = useChartWidth(compact), h = compact ? 320 : 300;
  const bins = distribution(records, metric?.key, compact ? 24 : w < 450 ? 12 : 18), maxCount = Math.max(1, ...bins.map(bin => bin.count));
  const left = compact ? 22 : 62, bottom = compact ? 22 : 40, plotW = w - left - 20, plotH = h - 32 - bottom;
  const summary = describe(records, metric?.key);
  return <figure className={`record-distribution${compact ? ' record-distribution-compact' : ''}`}>
    {!compact && <div className="record-chart-title"><strong>{metric?.label || 'Measurement'}{metric?.unit ? ` (${metric.unit})` : ''}</strong><span>FREQUENCY DISTRIBUTION</span></div>}
    <svg ref={chartRef} viewBox={`0 0 ${w} ${h}`} height={compact ? undefined : h} role={compact ? undefined : 'img'} aria-hidden={compact || undefined} aria-label={compact ? undefined : `${metric?.label || 'Value'} distribution: ${summary.count} numeric values; ${summary.missing} not recorded. Minimum ${number(summary.min)}, median ${number(summary.median)}, maximum ${number(summary.max)}. The table below provides the individual values.`}>
      <rect width={w} height={h} fill={INK}/>
      {(w < 450 ? [0, .5, 1] : [0, .25, .5, .75, 1]).map(tick => <g key={tick}><line x1={left} x2={w - 20} y1={h - bottom - tick * plotH} y2={h - bottom - tick * plotH} stroke="#abc8d325"/>{!compact && <text x={left - 9} y={h - bottom - tick * plotH + 4} textAnchor="end" fill="#b9d0d9" fontSize="12">{number(tick * maxCount)}</text>}</g>)}
      {bins.map((bin, index) => <rect key={index} x={left + index / bins.length * plotW + 1} y={h - bottom - bin.count / maxCount * plotH} width={Math.max(1, plotW / bins.length - 3)} height={bin.count / maxCount * plotH} fill={cividis(.25 + .75 * index / Math.max(1, bins.length - 1))}><title>{number(bin.from)}–{number(bin.to)}: {bin.count} records</title></rect>)}
      {selected && numeric(selected[metric?.key]) !== null && <g><line x1={left + (selected[metric.key] - summary.min) / (summary.max - summary.min || 1) * plotW} x2={left + (selected[metric.key] - summary.min) / (summary.max - summary.min || 1) * plotW} y1="24" y2={h - bottom} stroke="#fff5d5" strokeWidth="2" strokeDasharray="4 3"/><text x={left + 8} y="20" fill="#fff5d5" fontSize="12">Selected record: {number(selected[metric.key])}</text></g>}
      {!compact && <><text x={left} y={h - 16} fill="#d7e3e7" fontSize="12">{number(summary.min)}</text><text x={w - 20} y={h - 16} textAnchor="end" fill="#d7e3e7" fontSize="12">{number(summary.max)}</text><text x="12" y="18" fill="#b9d0d9" fontSize="11">RECORDS</text></>}
      {!bins.length && !compact && <text x={w / 2} y={h / 2} textAnchor="middle" fill="#c1d3dc" fontSize="14">No numeric measurements<tspan x={w / 2} dy="22">match this selection</tspan></text>}
    </svg>
    {!compact && <figcaption>Frequency distribution · equal-width bins · {summary.missing} missing values excluded</figcaption>}
  </figure>;
}

function SeriesView({ model, records, metric, compact = false }) {
  const [chartRef, width] = useChartWidth(compact), height = compact ? 340 : 310;
  const left = compact ? 65 : 64, right = width - 20, top = compact ? 35 : 20, bottom = height - 42, plotHeight = bottom - top;
  const rows = monthlySeries(records, model.data.dateField, metric?.key, model.categoryField), measured = rows.filter(row => row.mean !== null);
  const categories = [...new Set(rows.map(row => row.category))], colors = [WATER, GOLD, '#db9e8b', '#b7c5eb', '#b2d6a6'];
  const minX = Math.min(...rows.map(row => row.timestamp)), maxX = Math.max(...rows.map(row => row.timestamp));
  const minY = Math.min(0, ...measured.map(row => row.mean)), maxY = Math.max(1, ...measured.map(row => row.mean));
  const x = time => left + (time - minX) / Math.max(1, maxX - minX) * (right - left), y = value => bottom - (value - minY) / (maxY - minY) * plotHeight;
  const paths = categories.map(category => { let last = null; return rows.filter(row => row.category === category).map(row => { const previous = last; last = row; if (row.mean === null) return ''; const continuous = previous?.mean !== null && previous && row.timestamp - previous.timestamp < 32 * 86400000; return `${continuous ? 'L' : 'M'}${x(row.timestamp).toFixed(2)},${y(row.mean).toFixed(2)}`; }).join(' '); });
  return <figure className={`record-series${compact ? ' record-distribution-compact' : ''}`}>
    {!compact && <div className="record-chart-title"><strong>{metric?.label}{metric?.unit ? ` (${metric.unit})` : ''}</strong><span>MONTHLY MEAN</span></div>}
    <svg ref={chartRef} viewBox={`0 0 ${width} ${height}`} height={compact ? undefined : height} role={compact ? undefined : 'img'} aria-hidden={compact || undefined} aria-label={compact ? undefined : `${metric?.label}: monthly arithmetic means of selected reported values, ${categories.length} source groups. Gaps are not filled. The record table provides the exact observations.`}>
    <rect width={width} height={height} fill={INK}/>{(width < 450 ? [0, .5, 1] : [0, .25, .5, .75, 1]).map(tick => <g key={tick}><line x1={left} x2={right} y1={bottom - tick * plotHeight} y2={bottom - tick * plotHeight} stroke="#b7d0dc22"/>{!compact && <text x={left - 9} y={bottom + 4 - tick * plotHeight} textAnchor="end" fill="#adc5cf" fontSize="12">{number(minY + tick * (maxY - minY))}</text>}</g>)}
    {paths.map((path, index) => <path key={categories[index]} d={path} fill="none" stroke={colors[index % colors.length]} strokeWidth={compact ? 2.5 : 2} strokeDasharray={index >= colors.length ? '5 3' : undefined}/>)}
    {!compact && <><text x={left} y={height - 16} fill="#adc5cf" fontSize="12">{rows[0]?.date}</text><text x={right} y={height - 16} textAnchor="end" fill="#adc5cf" fontSize="12">{rows.at(-1)?.date}</text></>}
    {!measured.length && !compact && <text x={width / 2} y={height / 2} textAnchor="middle" fill="#adc5cf" fontSize="14">No dated measurements<tspan x={width / 2} dy="22">match this selection</tspan></text>}
  </svg>{!compact && <figcaption><ul>{categories.map((category, index) => <li key={category}><i style={{ borderColor: colors[index % colors.length], borderStyle: index >= colors.length ? 'dashed' : 'solid' }}/>{category}</li>)}</ul><p>Each line joins monthly arithmetic means of reported records within one source group. Missing months break the line. Counts and daily records remain in the table; incomplete periods are not normalized.</p></figcaption>}</figure>;
}

function Timeline({ model, records, time, onTime }) {
  const isMa = model.data.timeUnit === 'Ma';
  const years = yearCounts(isMa ? records.map(row => ({ ...row, [model.yearField]: Math.floor(row[model.yearField] / 10) * 10 })) : records, model.yearField), max = Math.max(1, ...years.map(row => row.count));
  const [chartRef, width] = useChartWidth(false, years.length >= 2);
  if (years.length < 2) return null;
  const minYear = years[0].year, maxYear = years.at(-1).year, plotW = width - 70;
  const barWidth = Math.max(1, Math.min(24, plotW / (maxYear - minYear + 1) - 1));
  return <figure className="record-timeline">
    <figcaption><span>{isMa ? 'COLLECTIONS / 10 MILLION YEAR BINS' : model.data.temporalMode === 'interval' ? 'SOURCE VERSIONS BY START YEAR' : 'OBSERVATIONS THROUGH TIME'}</span><b>{timeText(model, time ?? maxYear)}</b></figcaption>
    <svg ref={chartRef} viewBox={`0 0 ${width} 120`} height="120" role="img" aria-label={`Records through time, ${timeText(model, minYear)} to ${timeText(model, maxYear)}. Highest bin count ${max}. Use the timeline slider to change the selection.`}>
      {[.5, 1].map(tick => <g key={tick}><line x1="44" x2={width - 20} y1={80 - tick * 60} y2={80 - tick * 60} stroke="#bfd6df20"/><text x="35" y={84 - tick * 60} textAnchor="end" fill="#94b3c1" fontSize="12">{number(tick * max)}</text></g>)}
      {years.map(row => <rect key={row.year} x={44 + (row.year - minYear) / Math.max(1, maxYear - minYear) * (plotW - barWidth)} y={80 - row.count / max * 60} width={barWidth} height={Math.max(1, row.count / max * 60)} fill={time === null || row.year <= time ? WATER : '#456171'} onClick={() => onTime?.(Math.min(model.last, Math.max(model.first, row.year + (isMa ? 10 : 0))))}><title>{timeText(model, row.year)}: {row.count} records. Set playback cutoff.</title></rect>)}
      <text x="44" y="108" fill="#b9d0d9" fontSize="12">{timeText(model, minYear)}</text><text x={width - 20} y="108" textAnchor="end" fill="#b9d0d9" fontSize="12">{timeText(model, maxYear)}</text>
    </svg>
    <p>Counts describe the source snapshot, not detection rates or change in underlying risk.</p>
  </figure>;
}

function Compare({ model, records, controls, change, metric }) {
  const mode = comparisonMode(model, controls), modes = comparisonModes(model), groups = compareGroups(model, records, controls);
  if (!mode) return null;
  const middle = model.first !== null ? Math.floor((model.first + model.last) / 2) : null;
  return <section className="record-compare" aria-label="Compare subsets">
    <div className="record-section-title"><div><span className="record-eyebrow">A / B FIELD NOTES · {metric?.label || 'RECORDS'}</span><h3>Look at the difference.</h3></div><label>Compare by<select value={mode} onChange={event => change({ compareMode: event.target.value })}>{modes.map(option => <option key={option} value={option}>{option === 'category' ? 'Category' : 'Period'}</option>)}</select></label></div>
    <div className="record-compare-grid">{groups.map((group, index) => <div key={index} className="record-cohort">
      <span className="record-cohort-letter">{index ? 'B' : 'A'}</span>
      {mode === 'category' ? <label>Category {index ? 'B' : 'A'}<select value={controls[index ? 'compareB' : 'compareA'] ?? model.categories[index] ?? ''} onChange={event => change({ [index ? 'compareB' : 'compareA']: event.target.value })}>{model.categories.map(category => <option key={category}>{category}</option>)}</select></label>
        : <div className="record-pair">{['From', 'To'].map((part, partIndex) => { const key = `compare${index ? 'B' : 'A'}${part}`, fallback = index ? (partIndex ? model.last : middle === null ? '' : middle + (model.data.timeStep || 1)) : partIndex ? middle : model.first, value = controls[key] ?? fallback ?? ''; return <label key={part}>{model.data.timeUnit === 'Ma' ? `${partIndex ? 'Younger' : 'Older'} age (Ma)` : `${part} year`} {index ? 'B' : 'A'}<input type="number" step={model.data.timeStep || 1} value={value === '' ? '' : model.data.timeUnit === 'Ma' ? Math.abs(value) : value} onChange={event => change({ [key]: event.target.value === '' ? '' : model.data.timeUnit === 'Ma' ? -Math.abs(Number(event.target.value)) : event.target.value })}/></label>; })}</div>}
      <strong>{group.total.toLocaleString()}<small>matching records</small></strong>
      <dl><div><dt>Median {metric?.unit || ''}</dt><dd>{number(group.median)}</dd></div><div><dt>Mean {metric?.unit || ''}</dt><dd>{number(group.mean)}</dd></div><div><dt>Measured / missing</dt><dd>{group.count} / {group.missing}</dd></div></dl>
    </div>)}</div>
    <p>Descriptive summaries of the current selection. These are unweighted record means; unequal coverage, overlapping periods, reporting changes and repeated observations can prevent a fair comparison. No significance or causal claim is made.</p>
  </section>;
}

function RecordTable({ model, records, controls, change, selectedId, onSelect }) {
  const [requestedPage, setPage] = useState(0), pageSize = 20, pages = Math.max(1, Math.ceil(records.length / pageSize)), page = Math.min(requestedPage, pages - 1);
  const visible = records.slice(page * pageSize, (page + 1) * pageSize);
  return <section className="record-data" aria-label="Individual source records">
    <div className="record-section-title"><div><span className="record-eyebrow">OPEN THE RECORD</span><h3>Every mark has a source.</h3></div><span>{records.length.toLocaleString()} matching rows</span></div>
    <div className="record-table-scroll" tabIndex={0} aria-label="Scrollable record table"><table><caption className="sr-only">Filtered source records. Column headings sort the table; Inspect selects a record in the map and inspector. CSV includes all matching rows.</caption><thead><tr><th scope="col">Inspect</th>{model.columns.map(column => <th key={column.key} scope="col" aria-sort={controls.sort === column.key ? controls.direction === 'desc' ? 'descending' : 'ascending' : 'none'}><button type="button" onClick={() => { setPage(0); change({ sort: column.key, direction: controls.sort === column.key && controls.direction !== 'desc' ? 'desc' : 'asc' }); }}>{columnLabel(model, column)}{column.unit ? ` (${column.unit})` : ''}<span aria-hidden="true"> {controls.sort === column.key ? controls.direction === 'desc' ? '↓' : '↑' : '↕'}</span></button></th>)}</tr></thead>
      <tbody>{visible.map((record, index) => <tr key={record.id ?? index} data-selected={record.id === selectedId || undefined}><td><button type="button" aria-label={`Inspect ${nameOf(record)}`} aria-pressed={record.id === selectedId} onClick={() => onSelect(record.id)}>↗ <span>Inspect</span></button></td>{model.columns.map(column => <td key={column.key} className={column.type === 'number' ? 'record-numeric' : undefined}>{column.key === model.yearField || column.key === model.data.endYearField ? timeText(model, record[column.key]) : display(record[column.key])}</td>)}</tr>)}</tbody>
    </table>{!records.length && <p className="record-empty">No records match. Clear a filter or extend the selected period.</p>}</div>
    <div className="record-pagination"><span>Page {page + 1} of {pages} · 20 rows per page</span><div><button type="button" disabled={page === 0} onClick={() => setPage(page - 1)}>← Previous</button><button type="button" disabled={page >= pages - 1} onClick={() => setPage(page + 1)}>Next →</button></div></div>
  </section>;
}

function Provenance({ bundle, model, records }) {
  const snapshot = model.data.sourceSnapshot || model.data.sourceSnapshots?.[0];
  return <details className="record-evidence"><summary>Evidence, coverage & missing values<span>Inspect the snapshot ↗</span></summary><div className="record-evidence-body">
    <p>{model.data.coverage || 'Coverage details are provided in the source notes below.'}</p>
    <p>{model.records.length.toLocaleString()} records in this local snapshot. {model.records.filter(row => numeric(row[model.yearField]) === null).length} have no numeric time coordinate. Undated rows are excluded by an active time filter or an earlier playback cutoff.</p>
    <div className="record-evidence-columns"><div><h4>Missingness in your selection</h4><ul>{model.columns.map(column => <li key={column.key}><span>{column.label}</span><b>{records.filter(row => column.type === 'number' ? numeric(row[column.key]) === null : row[column.key] === null || row[column.key] === undefined || row[column.key] === '').length} / {records.length}</b></li>)}</ul></div>
      <div><h4>Trace this extraction</h4>{snapshot ? <dl><dt>Retrieved (UTC)</dt><dd>{snapshot.retrievedAt || 'Not supplied'}</dd><dt>Raw SHA-256</dt><dd className="record-hash">{snapshot.rawSha256 || 'Not supplied'}</dd><dt>Source query</dt><dd>{snapshot.queryUrl && /^https?:\/\//.test(snapshot.queryUrl) ? <a href={snapshot.queryUrl} target="_blank" rel="noopener noreferrer">Open the exact source request ↗</a> : 'Not supplied'}</dd></dl> : <p>No extraction receipt supplied in this bundle.</p>}<p>CSV exports retain source URLs and snapshot identity. Blank CSV cells mean missing, not zero. Spreadsheet formula-like source text is escaped for safe opening.</p>{bundle.sources?.map(source => source.citation ? <p key={source.name}>{source.citation}</p> : null)}</div>
    </div>
  </div></details>;
}

function RecordInstrument({ bundle, time, onTime, controls = {}, onControls }) {
  const model = recordModel(bundle), scene = useMemo(() => mapModel(model), [model]);
  const change = patch => onControls?.({ ...controls, ...patch });
  const selectedId = controls.selectedId ?? null;
  const setSelected = selectedId => change({ selectedId });
  const records = useMemo(() => filterRecords(model, { controls, time }), [model, controls, time]);
  const timelineRecords = useMemo(() => filterRecords({ ...model, data: { ...model.data, temporalMode: 'events' } }, { controls }), [model, controls]);
  const metric = metricOf(model, controls), summary = describe(records, metric?.key), selected = records.find(row => row.id === selectedId) || null;
  const hasSeries = Boolean(model.data.dateField && model.data.temporalMode === 'events');
  const view = controls.view || (model.data.preferredView === 'chart' && hasSeries ? 'trend' : scene.mapped.length ? 'map' : 'chart'), yearRange = recordRange(bundle);
  const isMa = model.data.timeUnit === 'Ma';
  const activeFilters = Boolean(controls.query || controls.category || controls.from || controls.to || controls.minValue || controls.maxValue);
  return <div className="record-lab">
    <div className="record-intro"><div><span className="record-eyebrow">THE KANSAS RECORD / RESEARCH INSTRUMENT</span><h3>{model.data.title || 'Follow the evidence.'}</h3><p>{model.data.description}</p></div><div className="record-snapshot"><i/><span>REAL SOURCE SNAPSHOT<small>{bundle.built_at?.slice(0, 10) || 'Date not supplied'} · local exploration</small></span></div></div>
    <div className="record-workspace">
      <aside className="record-controls" aria-label="Filter the source records"><div className="record-control-heading"><span>01</span><h4>Shape your question</h4></div>
        <label>Find a record<input type="search" value={controls.query || ''} placeholder="Name, place, source field…" onChange={event => change({ query: event.target.value })}/></label>
        {model.metrics.length > 0 && <label>Measure<select value={metric?.key || ''} onChange={event => change({ metric: event.target.value, minValue: '', maxValue: '' })}>{model.metrics.map(column => <option key={column.key} value={column.key}>{column.label}{column.unit ? ` · ${column.unit}` : ''}</option>)}</select></label>}
        {model.categories.length > 0 && <label>{model.columns.find(column => column.key === model.categoryField)?.label || 'Category'}<select value={controls.category || ''} onChange={event => change({ category: event.target.value })}><option value="">All categories</option>{model.categories.map(category => <option key={category}>{category}</option>)}</select></label>}
        {model.first !== null && !['snapshot', 'interval'].includes(model.data.temporalMode) && <fieldset><legend>{isMa ? 'Approximate age midpoint (Ma)' : 'Observation period'}</legend><div className="record-pair">{['from', 'to'].map((key, index) => <label key={key}>{isMa ? index ? 'Younger bound' : 'Older bound' : index ? 'To year' : 'From year'}<input type="number" step={model.data.timeStep || 1} placeholder={String(isMa ? Math.abs(index ? model.last : model.first) : index ? model.last : model.first)} value={controls[key] === '' || controls[key] === undefined ? '' : isMa ? Math.abs(controls[key]) : controls[key]} onChange={event => change({ [key]: event.target.value === '' ? '' : isMa ? -Math.abs(Number(event.target.value)) : event.target.value })}/></label>)}</div></fieldset>}
        {metric && <fieldset><legend>{metric.label}{metric.unit ? ` (${metric.unit})` : ''}</legend><div className="record-pair"><label>Minimum<input type="number" step="any" placeholder="Any" value={controls.minValue ?? ''} onChange={event => change({ minValue: event.target.value })}/></label><label>Maximum<input type="number" step="any" placeholder="Any" value={controls.maxValue ?? ''} onChange={event => change({ maxValue: event.target.value })}/></label></div></fieldset>}
        {activeFilters && <button type="button" className="record-clear" onClick={() => { onControls?.({}); onTime?.(yearRange?.max ?? null); }}>Clear selection filters ↺</button>}
        <div className="record-selection-count" role="status" aria-live="polite"><strong>{records.length.toLocaleString()}</strong><span>of {model.records.length.toLocaleString()} source records selected</span></div>
        <p className="record-control-note">The map, statistics, table and CSV follow this selection. {model.data.temporalMode === 'snapshot' ? 'The timeline selects one observation year, so repeated county estimates are never combined.' : model.data.temporalMode === 'interval' ? 'The timeline shows boundaries in force on December 31 of the selected year. Earlier versions are excluded.' : isMa ? 'The timeline advances from older to younger approximate age midpoints. Collection counts are not fossil abundance.' : 'Playback adds an upper-year boundary.'}</p>
        <details className="record-coverage"><summary>Read coverage</summary><p>{model.data.coverage}</p></details>
      </aside>
      <main className="record-stage" aria-label="Linked data visualizations">
        <div className="record-stage-heading"><span><b>02</b> READ THE PATTERN</span><div className="record-view-switch" role="group" aria-label="Visualization"><button type="button" disabled={!scene.mapped.length} aria-pressed={view === 'map'} onClick={() => change({ view: 'map' })}>Geography</button>{hasSeries && <button type="button" aria-pressed={view === 'trend'} onClick={() => change({ view: 'trend' })}>Trend</button>}<button type="button" aria-pressed={view === 'chart'} onClick={() => change({ view: 'chart' })}>Distribution</button></div></div>
        {view === 'map' && scene.mapped.length ? <SpatialView scene={scene} records={records} metric={metric} selected={selected} onSelect={setSelected} defaultExtent={model.data.temporalMode === 'interval' ? 'all' : 'kansas'}/> : view === 'trend' && hasSeries ? <SeriesView model={model} records={records} metric={metric}/> : <DistributionView records={records} metric={metric} selected={selected}/>}
        <div className="record-stat-strip"><div><span>Measured records</span><strong>{summary.count.toLocaleString()}</strong></div><div><span>Median {metric?.unit || ''}</span><strong>{number(summary.median)}</strong></div><div><span>Range {metric?.unit || ''}</span><strong>{number(summary.min)} <i>→</i> {number(summary.max)}</strong></div><div><span>Missing measure</span><strong>{summary.missing.toLocaleString()}</strong></div></div>
        <Timeline model={model} records={timelineRecords} time={time} onTime={onTime}/>
        <div className="record-inspector" aria-live="polite"><div><span className="record-eyebrow">03 / FIELD INSPECTOR</span><h4>{selected ? nameOf(selected) : 'A closer look changes everything.'}</h4><p>{selected ? `Source record ${selected.id}` : 'Select a mark on the map, or use Inspect in the keyboard-accessible record table.'}</p></div>{selected && <dl>{model.columns.map(column => <div key={column.key}><dt>{columnLabel(model, column)}{column.unit ? ` (${column.unit})` : ''}</dt><dd>{column.key === model.yearField || column.key === model.data.endYearField ? timeText(model, selected[column.key]) : typeof selected[column.key] === 'string' && /^https?:\/\//i.test(selected[column.key]) ? <a href={selected[column.key]} target="_blank" rel="noopener noreferrer">Open source record ↗</a> : display(selected[column.key])}</dd></div>)}</dl>}</div>
      </main>
    </div>
    <Compare model={model} records={records} controls={controls} change={change} metric={metric}/>
    <RecordTable model={model} records={records} controls={controls} change={change} selectedId={selected?.id} onSelect={setSelected}/>
    <Provenance bundle={bundle} model={model} records={records}/>
    <p className="record-map-credit">{KANSAS_OUTLINE_CREDIT} Real source snapshots support exploration; they do not imply a governed release or complete coverage.</p>
  </div>;
}

function RecordCard({ bundle }) {
  const model = recordModel(bundle), scene = useMemo(() => mapModel(model), [model]), metric = metricOf(model);
  const records = useMemo(() => filterRecords(model), [model]);
  return model.data.preferredView === 'chart' && model.data.dateField ? <SeriesView model={model} records={records} metric={metric} compact/> : scene.mapped.length ? <SpatialView scene={scene} records={records} metric={metric} compact/> : <DistributionView records={records} metric={metric} compact/>;
}

export default function RecordLab(props) {
  return props.mode === 'card' ? <RecordCard bundle={props.bundle}/> : <RecordInstrument {...props}/>;
}
