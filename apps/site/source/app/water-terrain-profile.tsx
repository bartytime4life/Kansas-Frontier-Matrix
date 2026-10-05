import type { WaterPathAnalysis } from "./water-path-analysis";

export function WaterTerrainProfile({ analysis }: { analysis: WaterPathAnalysis }) {
  const elevation = analysis.elevation;
  const values = elevation.samples.flatMap(s => s.elevationM === null ? [] : [s.elevationM]);
  const minimum = values.length ? Math.min(...values) : 0, maximum = values.length ? Math.max(...values) : 0;
  const span = Math.max(1, maximum - minimum);
  const lines: string[][] = []; let line: string[] = [], previousDatum: string | null = null;
  for (const sample of elevation.samples) {
    if (sample.elevationM === null) { if (line.length) lines.push(line); line = []; continue; }
    if (line.length && (!sample.datum || sample.datum !== previousDatum)) { lines.push(line); line = []; }
    line.push(`${(12 + sample.distanceM / analysis.lengthM * 436).toFixed(2)},${(maximum === minimum ? 55 : 90 - (sample.elevationM - minimum) / span * 70).toFixed(2)}`);
    previousDatum = sample.datum;
  }
  if (line.length) lines.push(line);
  const datums = [...new Set(elevation.samples.flatMap(s => s.datum ? [s.datum] : []))];
  const resolution = elevation.samples.flatMap(s => s.resolutionM === null ? [] : [s.resolutionM]);
  return <section className="water-terrain-profile" aria-label="Mapped river corridor and sampled terrain">
    <strong>{analysis.name || "Nearest mapped river"}</strong>
    <div className="water-terrain-metrics">
      <div><span>Mapped corridor</span><b>{(analysis.lengthM / 1000).toFixed(1)} km</b><small>{analysis.segments} connected reaches</small></div>
      <div><span>{elevation.dropM !== null && elevation.dropM < 0 ? "Net terrain rise" : "Net terrain fall"}</span><b>{elevation.dropM === null ? "Unavailable" : `${Math.abs(elevation.dropM).toFixed(1)} m`}</b><small>between sampled endpoints</small></div>
      <div><span>Mean terrain slope</span><b>{elevation.slopePercent === null ? "Unavailable" : `${elevation.slopePercent.toFixed(3)}%`}</b><small>positive = downhill</small></div>
    </div>
    {analysis.upstreamM !== undefined && <p>{(analysis.upstreamM / 1000).toFixed(1)} km upstream · {((analysis.downstreamM ?? 0) / 1000).toFixed(1)} km downstream. Mainstem context only; the gauge does not measure discharge along this entire corridor.</p>}
    <small>Nearest channel is {Math.round(analysis.gaugeOffsetM)} m from the gauge. {analysis.stopReason}</small>
    {analysis.connectors > 0 && <small>Dashed route includes {analysis.connectors} USGS abstract connector{analysis.connectors === 1 ? "" : "s"} through waterbodies or surface breaks; it does not outline the wetted channel.</small>}
    <details open><summary>Terrain along the mapped corridor</summary>
      {values.length ? <figure>
        <svg viewBox="0 0 460 118" role="img" aria-label={`Sampled terrain elevation from ${minimum.toFixed(1)} to ${maximum.toFixed(1)} meters along ${(analysis.lengthM / 1000).toFixed(1)} kilometers. Gaps are not interpolated.`}>
          <line x1="12" x2="448" y1="94" y2="94" stroke="#658d93" />
          {lines.map((points, i) => points.length > 1 ? <polyline key={i} points={points.join(" ")} fill="none" stroke="#88eee5" strokeWidth="2.5" /> : <circle key={i} cx={points[0].split(",")[0]} cy={points[0].split(",")[1]} r="2.5" fill="#88eee5" />)}
          {analysis.upstreamM !== undefined && <g><line x1={12 + analysis.upstreamM / analysis.lengthM * 436} x2={12 + analysis.upstreamM / analysis.lengthM * 436} y1="8" y2="94" stroke="#f3c66d" strokeDasharray="3 3" /><text x={12 + analysis.upstreamM / analysis.lengthM * 436} y="10" textAnchor="middle">Gauge</text></g>}
          <text x="12" y="113">Route start</text><text x="448" y="113" textAnchor="end">{(analysis.lengthM / 1000).toFixed(1)} km along route</text>
        </svg>
        <figcaption>{values.length}/{elevation.samples.length} terrain samples · {minimum.toFixed(1)}–{maximum.toFixed(1)} m{resolution.length ? ` · reported resolution ${Math.min(...resolution).toFixed(0)}–${Math.max(...resolution).toFixed(0)} m` : ""}. {datums.length ? datums.join("; ") : "Vertical datum not supplied."}</figcaption>
      </figure> : <p>Terrain elevations are unavailable for this path.</p>}
      {elevation.dropM === null && values.length > 0 && <p>Endpoint fall and mean slope are unavailable without both endpoint elevations and matching reported vertical datums.</p>}
      <p>{elevation.notice}</p>
      <a href="https://elevation.nationalmap.gov/arcgis/rest/services/3DEPElevation/ImageServer" target="_blank" rel="noreferrer">USGS 3DEP elevation source</a>
    </details>
  </section>;
}
