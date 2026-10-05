"use client";

import { useId, useMemo, useState, type KeyboardEvent, type ReactNode } from "react";
import { RiverNetworkSignal } from "./river-network-signal";
import { nearestRiverSample } from "./river-pulse-visuals";
import { WaterTerrainProfile } from "./water-terrain-profile";
import type { WaterPathAnalysis } from "./water-path-analysis";
import { waterReadingCue } from "./water-flow-context";
import {
  buildHydrographSegments,
  stationObservations,
  streamflowDisplayFrames,
  type StreamflowBundle,
  type StreamflowFrame,
  type StreamflowObservation,
  type StreamflowStation,
} from "./streamflow";

export type HydrologyObservatoryState = "idle" | "loading" | "ready" | "partial" | "empty" | "stale" | "error";
export type HydrologyRange = "24h" | "7d" | "30d" | "1y";
export type HydrologyPlaybackSpeed = 0.5 | 1 | 2;

export type HydrologyObservatoryProps = Readonly<{
  bundle: StreamflowBundle | null;
  state: HydrologyObservatoryState;
  error: string | null;
  frame: StreamflowFrame | null;
  frameIndex: number;
  playing: boolean;
  speed: HydrologyPlaybackSpeed;
  range: HydrologyRange;
  selectedStationId: string | null;
  frameTimes?: readonly string[];
  reducedMotion: boolean;
  downstreamState: "idle" | "loading" | "ready" | "empty" | "error";
  downstreamPathCount: number;
  downstreamAnalysis?: WaterPathAnalysis | null;
  sourceSwitcher?: ReactNode;
  onRefresh: () => void;
  onTogglePlay: () => void;
  onStep: (direction: "reverse" | "forward") => void;
  onSeek: (index: number) => void;
  onJumpLatest: () => void;
  onSpeed: (speed: HydrologyPlaybackSpeed) => void;
  onRange: (range: HydrologyRange) => void;
  onSelectStation: (stationId: string | null) => void;
  onShowDirection: () => void;
}>;

const CHART_WIDTH = 640;
const CHART_HEIGHT = 180;
const CHART_PADDING = 20;

const RANGE_OPTIONS: readonly Readonly<{
  value: HydrologyRange;
  label: string;
  stationRequired: boolean;
}>[] = Object.freeze([
  Object.freeze({ value: "24h", label: "24 hours", stationRequired: false }),
  Object.freeze({ value: "7d", label: "7 days", stationRequired: true }),
  Object.freeze({ value: "30d", label: "30 days", stationRequired: true }),
  Object.freeze({ value: "1y", label: "1 year", stationRequired: true }),
]);

const STATE_LABELS: Readonly<Record<HydrologyObservatoryState, string>> = Object.freeze({
  idle: "NOT LOADED",
  loading: "LOADING",
  ready: "READY",
  partial: "PARTIAL",
  empty: "NO OBSERVATIONS",
  stale: "STALE",
  error: "UNAVAILABLE",
});

const asRecord = (value: unknown): Record<string, unknown> => value && typeof value === "object"
  ? value as Record<string, unknown>
  : {};

const finiteNumber = (value: unknown): number | null => typeof value === "number" && Number.isFinite(value)
  ? value
  : null;

const stringValue = (value: unknown): string | null => typeof value === "string" && value.trim() !== ""
  ? value
  : null;

const frameProperties = (frame: StreamflowFrame | null) => frame?.features.map((feature) => asRecord(feature.properties)) ?? [];

const formatLocalTime = (value: string | null) => {
  if (!value || !Number.isFinite(Date.parse(value))) return "No confirmed observation frame";
  return new Intl.DateTimeFormat(undefined, {
    year: "numeric",
    month: "short",
    day: "numeric",
    hour: "numeric",
    minute: "2-digit",
    second: "2-digit",
    timeZoneName: "short",
  }).format(new Date(value));
};

const formatUtcTime = (value: string | null) => {
  if (!value || !Number.isFinite(Date.parse(value))) return "UTC unavailable";
  const normalized = new Date(value).toISOString();
  return `${normalized.slice(0, 10)} · ${normalized.slice(11, 19)}Z`;
};

const stationLabel = (station: StreamflowStation) => station.name === station.stationId
  ? station.stationId
  : `${station.name} · ${station.stationId}`;

const formatDischarge = (value: number | null, unit: string | null) => value === null
  ? "not reported"
  : `${value.toLocaleString("en-US", { maximumFractionDigits: value >= 100 ? 0 : 2 })} ${unit === "ft^3/s" ? "ft³/s" : unit ?? "unknown unit"}`;

const observationGapMinutes = (observations: readonly StreamflowObservation[]) => {
  const deltas = observations.slice(1).flatMap((observation, index) => {
    const previous = Date.parse(observations[index].observedAt);
    const current = Date.parse(observation.observedAt);
    const minutes = (current - previous) / 60_000;
    return Number.isFinite(minutes) && minutes > 0 ? [minutes] : [];
  }).sort((left, right) => left - right);
  const median = deltas.length ? deltas[Math.floor(deltas.length / 2)] : 15;
  return Math.max(30, Math.ceil(median * 2));
};

type HydrographSummary = Readonly<{
  valid: readonly StreamflowObservation[];
  minimum: number | null;
  maximum: number | null;
  latest: StreamflowObservation | null;
  unit: string | null;
}>;

const summarizeHydrograph = (observations: readonly StreamflowObservation[]): HydrographSummary => {
  const valid = observations.filter((observation) => observation.value !== null);
  const values = valid.map((observation) => observation.value as number);
  return {
    valid,
    minimum: values.length ? Math.min(...values) : null,
    maximum: values.length ? Math.max(...values) : null,
    latest: valid.at(-1) ?? null,
    unit: valid.at(-1)?.unit ?? observations.at(-1)?.unit ?? null,
  };
};

const pointForObservation = (
  observation: StreamflowObservation | null,
  summary: HydrographSummary,
  observations: readonly StreamflowObservation[],
): Readonly<{ x: number; y: number }> | null => {
  if (!observation || observation.value === null || summary.valid.length === 0 || observations.length === 0) return null;
  const firstTime = Date.parse(observations[0].observedAt);
  const lastTime = Date.parse(observations.at(-1)!.observedAt);
  const observationTime = Date.parse(observation.observedAt);
  if (![firstTime, lastTime, observationTime].every(Number.isFinite)) return null;
  const timeSpan = Math.max(1, lastTime - firstTime);
  const valueSpan = (summary.maximum ?? observation.value) - (summary.minimum ?? observation.value);
  return {
    x: CHART_PADDING + ((observationTime - firstTime) / timeSpan) * (CHART_WIDTH - CHART_PADDING * 2),
    y: valueSpan === 0
      ? CHART_HEIGHT / 2
      : CHART_PADDING + (1 - (observation.value - (summary.minimum ?? observation.value)) / valueSpan) * (CHART_HEIGHT - CHART_PADDING * 2),
  };
};

export function HydrologyObservatory({
  bundle,
  state,
  error,
  frame,
  frameIndex,
  playing,
  speed,
  range,
  selectedStationId,
  frameTimes,
  reducedMotion,
  downstreamState,
  downstreamPathCount,
  downstreamAnalysis = null,
  sourceSwitcher,
  onRefresh,
  onTogglePlay,
  onStep,
  onSeek,
  onJumpLatest,
  onSpeed,
  onRange,
  onSelectStation,
  onShowDirection,
}: HydrologyObservatoryProps) {
  const chartTitleId = useId();
  const chartGradientId = useId();
  const [expanded, setExpanded] = useState(false);
  const [sampleProbe, setSampleProbe] = useState<{ station: string; time: string } | null>(null);
  const chartDescriptionId = useId();
  const stationOptions = useMemo(
    () => [...(bundle?.stations ?? [])].sort((left, right) => stationLabel(left).localeCompare(stationLabel(right))),
    [bundle],
  );
  const observationTimes = useMemo(
    () => frameTimes ?? (bundle ? streamflowDisplayFrames(bundle) : []),
    [bundle, frameTimes],
  );
  const selectedStation = useMemo(
    () => stationOptions.find((station) => station.stationId === selectedStationId) ?? null,
    [selectedStationId, stationOptions],
  );
  const selectedSeries = useMemo(
    () => bundle && selectedStation ? stationObservations(bundle, selectedStation.stationId) : [],
    [bundle, selectedStation],
  );
  const gapMinutes = useMemo(() => observationGapMinutes(selectedSeries), [selectedSeries]);
  const hydrographSegments = useMemo(
    () => buildHydrographSegments(selectedSeries, {
      width: CHART_WIDTH,
      height: CHART_HEIGHT,
      gapMinutes,
      padding: CHART_PADDING,
    }),
    [gapMinutes, selectedSeries],
  );
  const hydrographSummary = useMemo(() => summarizeHydrograph(selectedSeries), [selectedSeries]);
  const frameValues = frameProperties(frame);
  const frameTime = stringValue(frameValues[0]?.frameCursor)
    ?? observationTimes[Math.max(0, Math.min(frameIndex, observationTimes.length - 1))]
    ?? null;
  const reportingCount = frameValues.filter((properties) => finiteNumber(properties.value) !== null && properties.missing !== true).length;
  const explicitMissingCount = frameValues.filter((properties) => properties.missing === true || finiteNumber(properties.value) === null).length;
  const missingCount = Math.max(explicitMissingCount, Math.max(0, stationOptions.length - reportingCount));
  const provisionalCount = frameValues.filter((properties) => stringValue(properties.approvalStatus)?.toLowerCase().includes("provisional")).length;
  const selectedFrameProperties = frameValues.find((properties) => stringValue(properties.stationId) === selectedStationId) ?? null;
  const selectedWaterCue = waterReadingCue(frame?.features.find((feature) => feature.properties.stationId === selectedStationId)?.properties ?? null, selectedSeries);
  const relativePosition = selectedWaterCue.rangePosition === null ? null
    : selectedWaterCue.rangePosition <= 0.2 ? "Near loaded low" : selectedWaterCue.rangePosition >= 0.8 ? "Near loaded high" : "Between loaded low and high";
  const activeObservationTime = selectedFrameProperties ? stringValue(selectedFrameProperties.observedAt) : null;
  const activeObservation = activeObservationTime
    ? selectedSeries.find((observation) => observation.observedAt === activeObservationTime) ?? null
    : null;
  const latestPoint = pointForObservation(hydrographSummary.latest, hydrographSummary, selectedSeries);
  const activePoint = selectedFrameProperties?.missing ? null : pointForObservation(activeObservation, hydrographSummary, selectedSeries);
  const gapCount = Math.max(0, hydrographSegments.length - 1);
  const probeIndex = sampleProbe?.station === selectedStationId ? selectedSeries.findIndex(sample => sample.observedAt === sampleProbe.time) : -1;
  const probeObservation = probeIndex >= 0 ? selectedSeries[probeIndex] : activeObservation ?? selectedSeries.at(-1) ?? null;
  const probePoint = pointForObservation(probeObservation, hydrographSummary, selectedSeries);
  const inspectIndex = (index: number) => { const sample = selectedSeries[index]; if (sample && selectedStationId) setSampleProbe({ station: selectedStationId, time: sample.observedAt }); };

  const safeFrameIndex = Math.max(0, Math.min(frameIndex, Math.max(0, observationTimes.length - 1)));
  const canPlay = !reducedMotion && observationTimes.length > 1 && state !== "loading" && state !== "empty" && state !== "error";
  const canStep = observationTimes.length > 1 && state !== "loading";
  const atLatest = observationTimes.length > 0 && safeFrameIndex === observationTimes.length - 1;
  const displayState = playing && (state === "ready" || state === "partial") ? "PLAYING" : STATE_LABELS[state];
  const queryMode = bundle?.query.mode.replaceAll("-", " ") ?? "not loaded";
  const chartSummary = `${hydrographSummary.valid.length} exact observations; minimum ${formatDischarge(hydrographSummary.minimum, hydrographSummary.unit)}; maximum ${formatDischarge(hydrographSummary.maximum, hydrographSummary.unit)}; latest ${formatDischarge(hydrographSummary.latest?.value ?? null, hydrographSummary.unit)}; ${gapCount} detected gap${gapCount === 1 ? "" : "s"}.`;

  const handleKeyDown = (event: KeyboardEvent<HTMLElement>) => {
    if (event.target !== event.currentTarget) return;
    if (event.key === " ") {
      event.preventDefault();
      if (canPlay) onTogglePlay();
      return;
    }
    if (event.key === "ArrowLeft") {
      event.preventDefault();
      if (canStep && safeFrameIndex > 0) onStep("reverse");
      return;
    }
    if (event.key === "ArrowRight") {
      event.preventDefault();
      if (canStep && !atLatest) onStep("forward");
      return;
    }
    if (event.key === "Home") {
      event.preventDefault();
      if (observationTimes.length) onJumpLatest();
    }
  };

  return <aside
    className="hydrology-observatory"
    data-state={state}
    data-playing={playing}
    data-expanded={expanded}
    tabIndex={0}
    aria-label="River Pulse streamflow observation controls"
    aria-busy={state === "loading"}
    onKeyDown={handleKeyDown}
  >
    {sourceSwitcher}
    <header className="hydrology-header">
      <div className="hydrology-identity">
        <span>RIVER PULSE · USGS OBSERVATIONS</span>
        <strong>Current and historical Kansas streamflow</strong>
      </div>
      <div className="hydrology-header-actions">
        <button type="button" className="river-follow" onClick={() => { setExpanded(false); onShowDirection(); }} disabled={!bundle?.stations.length}>Follow a river</button>
        <button type="button" className="river-expand" aria-expanded={expanded} onClick={() => setExpanded(value => !value)}>{expanded ? "Compact" : "Expand details"}</button>
        <b className="hydrology-state" role="status" aria-live={playing ? "off" : "polite"}>{displayState}</b>
        <button type="button" onClick={onRefresh} disabled={state === "loading"}>{state === "loading" ? "Refreshing…" : "Refresh"}</button>
      </div>
    </header>

    <RiverNetworkSignal frame={frame} selected={selectedStationId} onSelect={onSelectStation} />
    <div className="hydrology-clock" role="status" aria-live={playing ? "off" : "polite"} aria-atomic="true">
      <div>
        <span>{observationTimes.length ? "EXACT OBSERVATION FRAME" : "REQUEST END · NO OBSERVATIONS"}</span>
        <strong><time dateTime={frameTime ?? undefined}>{formatLocalTime(frameTime)}</time></strong>
        <small><time dateTime={frameTime ?? undefined}>{formatUtcTime(frameTime)}</time> · {queryMode}</small>
      </div>
      <span>{observationTimes.length ? `${safeFrameIndex + 1} / ${observationTimes.length}` : "No frames"}</span>
    </div>

    <div className="hydrology-transport" aria-label="Streamflow playback">
      <button type="button" onClick={() => onStep("reverse")} disabled={!canStep || safeFrameIndex <= 0} aria-label="Previous exact streamflow frame">‹</button>
      <button className="hydrology-play" type="button" aria-pressed={playing} onClick={onTogglePlay} disabled={!canPlay}>{playing ? "Ⅱ Pause" : "▶ Play"}</button>
      <button type="button" onClick={() => onStep("forward")} disabled={!canStep || atLatest} aria-label="Next exact streamflow frame">›</button>
      <input
        type="range"
        min="0"
        max={Math.max(0, observationTimes.length - 1)}
        value={safeFrameIndex}
        disabled={observationTimes.length < 2 || state === "loading"}
        onChange={(event) => onSeek(Number(event.target.value))}
        aria-label="Select an exact streamflow observation frame"
        aria-valuetext={`${formatLocalTime(frameTime)}; ${reportingCount} reporting, ${missingCount} missing, ${provisionalCount} provisional`}
      />
      <button className="hydrology-latest" type="button" aria-pressed={atLatest} onClick={onJumpLatest} disabled={!observationTimes.length}>Latest</button>
    </div>

    <div className="hydrology-settings">
      <label>
        <span>Range</span>
        <select value={range} onChange={(event) => onRange(event.target.value as HydrologyRange)}>
          {RANGE_OPTIONS.map((option) => <option key={option.value} value={option.value} disabled={option.stationRequired && !selectedStationId}>{option.label}{option.stationRequired ? " · station" : ""}</option>)}
        </select>
      </label>
      <label>
        <span>Speed</span>
        <select value={speed} onChange={(event) => onSpeed(Number(event.target.value) as HydrologyPlaybackSpeed)} disabled={reducedMotion}>
          <option value={0.5}>0.5×</option>
          <option value={1}>1×</option>
          <option value={2}>2×</option>
        </select>
      </label>
      <label className="hydrology-station-control">
        <span>Station</span>
        <select value={selectedStationId ?? ""} onChange={(event) => onSelectStation(event.target.value || null)}>
          <option value="">Statewide gauges</option>
          {stationOptions.map((station) => <option key={station.stationId} value={station.stationId}>{stationLabel(station)}</option>)}
        </select>
      </label>
    </div>


    <section className="hydrology-water-reading" data-reading={selectedWaterCue.kind} aria-label="Selected station water movement and range">
      <div className="hydrology-water-reading-head"><span>{selectedStation?.name ?? "WATER AT SELECTED GAUGE"}</span><strong>{selectedStation ? selectedWaterCue.kind === "missing" ? "No reading at this frame" : formatDischarge(selectedWaterCue.value, hydrographSummary.unit) : "Choose a station to inspect flow"}</strong></div>
      {selectedStation && <>
        <div className="river-reading-meta"><b>{selectedWaterCue.kind === "missing" ? "NO FRESH MEASUREMENT" : selectedWaterCue.kind === "zero" ? "MEASURED ZERO" : selectedWaterCue.kind.toUpperCase()}</b><span>{activeObservationTime ? formatLocalTime(activeObservationTime) : "No source timestamp"}</span><span>{stringValue(selectedFrameProperties?.approvalStatus) ?? "Quality not supplied"}</span></div>
        <p>{selectedWaterCue.kind === "zero" ? "Observed zero discharge at this gauge. The extent of dry channel is unknown."
          : selectedWaterCue.kind === "missing" ? "Missing is unknown, not zero or dry."
          : selectedWaterCue.change !== null ? `${selectedWaterCue.change > 0 ? "Rising" : selectedWaterCue.change < 0 ? "Falling" : "Steady"} by ${formatDischarge(Math.abs(selectedWaterCue.change), hydrographSummary.unit)} since the prior reported observation.`
          : "No prior reported value is available for comparison in this frame."}</p>
        {relativePosition && <div className="hydrology-range-position"><div role="meter" aria-label="Position within loaded station observations" aria-valuemin={0} aria-valuemax={100} aria-valuenow={Math.round(selectedWaterCue.rangePosition! * 100)} aria-valuetext={relativePosition}><i style={{ left: `${selectedWaterCue.rangePosition! * 100}%` }} /></div><small>{relativePosition} · {formatDischarge(selectedWaterCue.rangeMinimum, hydrographSummary.unit)} to {formatDischarge(selectedWaterCue.rangeMaximum, hydrographSummary.unit)} in loaded station range</small></div>}
      </>}
      <details className="river-path-details"><summary>Channel direction &amp; terrain</summary>
      <div className="hydrology-direction-status" role="status"><strong>MAPPED FLOW DIRECTION</strong><span>{!selectedStation ? "Show direction to choose a reporting gauge and inspect its nearby mapped channels." : downstreamState === "ready" ? `Downstream guide follows ${downstreamAnalysis?.segments ?? downstreamPathCount} USGS mapped reach${(downstreamAnalysis?.segments ?? downstreamPathCount) === 1 ? "" : "es"}. ${selectedWaterCue.kind === "zero" ? "Measured zero: the amber guide is stationary, with no moving arrows." : selectedWaterCue.kind === "missing" ? "Measurement unavailable: the dashed guide is stationary, with no arrows." : "Motion follows a positive reading and pauses when the feed is unavailable or stale."} Luminous trails show mapped direction; their pace is illustrative, not measured water speed.` : downstreamState === "loading" ? downstreamPathCount ? "Showing verified nearby direction while checking the longer mapped path and terrain…" : "Checking mapped channel direction…" : downstreamState === "empty" ? "No verified directional channel segment nearby; arrows hidden. Try another gauge." : downstreamState === "error" ? "Mapped channel direction unavailable; arrows hidden." : "Mapped direction is not loaded."}</span></div>
      {downstreamState === "ready" && downstreamAnalysis && <WaterTerrainProfile analysis={downstreamAnalysis} />}
      </details>
      <button className="hydrology-direction-action" type="button" onClick={onShowDirection} disabled={!bundle?.stations.length}>{selectedStation ? "Zoom to flow direction" : "Show flow direction on map"}</button>
      <small className="hydrology-reading-boundary">Gauge rings show change at a station. Relative low or high describes only the loaded station readings; it is not a drought or flood threshold.</small>
    </section>

    {(state === "loading" || state === "empty" || state === "stale" || state === "error" || error) && <div className="hydrology-message" data-state={state} role={state === "error" ? "alert" : "status"}>
      <strong>{state === "loading" ? "Loading source observations" : state === "empty" ? "No observations returned" : state === "stale" ? "Last confirmed observations are stale" : state === "error" ? "Streamflow is unavailable" : "Source notice"}</strong>
      <span>{error ?? (state === "empty" ? "No returned observation is interpreted as zero flow or an all-clear." : state === "stale" ? "The last confirmed frame remains labeled with its original observation time." : "Previously confirmed map context remains unchanged while the request settles.")}</span>
    </div>}

    <details className="hydrology-legend">
      <summary>Discharge, trend and quality legend</summary>
      <div className="hydrology-legend-grid">
        <section aria-label="Discharge marker size">
          <strong>DISCHARGE MAGNITUDE</strong>
          <div className="hydrology-size-key"><span><i data-size="small" />Lower</span><span><i data-size="medium" />Medium</span><span><i data-size="large" />Higher</span></div>
          <p>Marker area uses a logarithmic ft³/s scale. Raw discharge is not a flood category and is not directly comparable across differently sized basins.</p>
        </section>
        <section aria-label="Observation trend">
          <strong>CHANGE FROM PRIOR OBSERVATION</strong>
          <div className="hydrology-trend-key"><span data-trend="rising">↑ Rising</span><span data-trend="falling">↓ Falling</span><span data-trend="steady">— Steady</span><span data-trend="unknown">? Unknown</span></div>
          <p>Trend compares two reported observations only; it is not a forecast, rate of travel, or causal interpretation.</p>
        </section>
        <section aria-label="Observation quality">
          <strong>QUALITY / AVAILABILITY</strong>
          <div className="hydrology-quality-key"><span data-quality="approved"><i />Approved</span><span data-quality="provisional"><i />Provisional</span><span data-quality="missing"><i />Dashed ×: missing or too old</span><span data-quality="zero"><i />Amber −: measured zero</span></div>
          <p>Missing stations remain hollow. Provisional USGS values may be revised.</p>
        </section>
      </div>
    </details>

    {selectedStation && <section className="hydrology-hydrograph" aria-labelledby={chartTitleId}>
      <header>
        <div>
          <span>SELECTED-STATION HYDROGRAPH</span>
          <strong id={chartTitleId}>{selectedStation.name}</strong>
          <small>{selectedStation.stationId} · discharge parameter 00060</small>
        </div>
        <b>{hydrographSummary.valid.length} OBS</b>
      </header>
      {hydrographSummary.valid.length > 0 ? <figure>
        <svg
          className="hydrology-chart"
          viewBox={`0 0 ${CHART_WIDTH} ${CHART_HEIGHT}`}
          width={CHART_WIDTH}
          height={CHART_HEIGHT}
          preserveAspectRatio="none"
          role="img"
          aria-labelledby={`${chartTitleId} ${chartDescriptionId}`}
          onPointerMove={(event) => {
            if (!selectedSeries.length) return;
            const bounds = event.currentTarget.getBoundingClientRect();
            const fraction = Math.max(0, Math.min(1, ((event.clientX - bounds.left) / bounds.width * CHART_WIDTH - CHART_PADDING) / (CHART_WIDTH - CHART_PADDING * 2)));
            inspectIndex(nearestRiverSample(selectedSeries, Date.parse(selectedSeries[0].observedAt) + fraction * (Date.parse(selectedSeries.at(-1)!.observedAt) - Date.parse(selectedSeries[0].observedAt))));
          }}
        >
          <defs><linearGradient id={chartGradientId} x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stopColor="#5ef0e6" stopOpacity=".35" /><stop offset="100%" stopColor="#5ef0e6" stopOpacity="0" /></linearGradient></defs>
          <desc id={chartDescriptionId}>{chartSummary}</desc>
          <line className="hydrology-chart-grid" x1={CHART_PADDING} y1={CHART_PADDING} x2={CHART_WIDTH - CHART_PADDING} y2={CHART_PADDING} />
          <line className="hydrology-chart-grid" x1={CHART_PADDING} y1={CHART_HEIGHT / 2} x2={CHART_WIDTH - CHART_PADDING} y2={CHART_HEIGHT / 2} />
          <line className="hydrology-chart-grid" x1={CHART_PADDING} y1={CHART_HEIGHT - CHART_PADDING} x2={CHART_WIDTH - CHART_PADDING} y2={CHART_HEIGHT - CHART_PADDING} />
          {hydrographSegments.map((segment, index) => {
            const start = pointForObservation(selectedSeries.find(sample => sample.observedAt === segment.startTime) ?? null, hydrographSummary, selectedSeries);
            const end = pointForObservation(selectedSeries.find(sample => sample.observedAt === segment.endTime) ?? null, hydrographSummary, selectedSeries);
            return start && end && segment.pointCount > 1 ? <path key={`area-${index}`} d={`${segment.path} L${end.x},${CHART_HEIGHT - CHART_PADDING} L${start.x},${CHART_HEIGHT - CHART_PADDING} Z`} fill={`url(#${chartGradientId})`} /> : null;
          })}
          <text className="river-chart-axis" x={CHART_WIDTH - CHART_PADDING} y="14" textAnchor="end">{formatDischarge(hydrographSummary.maximum, hydrographSummary.unit)}</text>
          {hydrographSegments.map((segment, index) => <path key={`${segment.startTime}:${segment.endTime}:${index}`} className="hydrology-chart-segment" d={segment.path} fill="none" vectorEffect="non-scaling-stroke" />)}
          {latestPoint && <circle className="hydrology-chart-latest" cx={latestPoint.x} cy={latestPoint.y} r="4.5" vectorEffect="non-scaling-stroke" />}
          {probePoint && <><line className="river-probe-line" x1={probePoint.x} x2={probePoint.x} y1={CHART_PADDING} y2={CHART_HEIGHT - CHART_PADDING} /><circle className="river-probe-halo" cx={probePoint.x} cy={probePoint.y} r="11" /><circle className="river-probe-dot" cx={probePoint.x} cy={probePoint.y} r="4" /></>}
          {activePoint && <>
            <line className="hydrology-chart-cursor" x1={activePoint.x} y1={CHART_PADDING} x2={activePoint.x} y2={CHART_HEIGHT - CHART_PADDING} vectorEffect="non-scaling-stroke" />
            <circle className="hydrology-chart-active" cx={activePoint.x} cy={activePoint.y} r="6" vectorEffect="non-scaling-stroke" />
          </>}
        </svg>
        <div className="river-sample-probe" aria-label="Exact source sample inspector"><div><span>INSPECTED SAMPLE</span><strong>{formatDischarge(probeObservation?.value ?? null, probeObservation?.unit ?? null)}</strong><time>{formatLocalTime(probeObservation?.observedAt ?? null)}</time></div><small>{probeObservation?.approvalStatus ?? "No sample"} · {probeObservation?.value === null ? "Missing value; no point invented." : "Exact reported value. Inspection does not change map time."}</small>
          <input type="range" min="0" max={Math.max(0, selectedSeries.length - 1)} value={probeIndex >= 0 ? probeIndex : Math.max(0, selectedSeries.indexOf(probeObservation!))} disabled={!selectedSeries.length} onChange={event => inspectIndex(Number(event.target.value))} aria-label="Inspect exact station sample" aria-valuetext={`${formatDischarge(probeObservation?.value ?? null, probeObservation?.unit ?? null)} at ${formatLocalTime(probeObservation?.observedAt ?? null)}`} />
        </div>
        <figcaption className="hydrology-chart-caption">
          <span>{formatLocalTime(selectedSeries[0]?.observedAt ?? null)}</span>
          <strong>Exact values · gaps break the path</strong>
          <span>{formatLocalTime(selectedSeries.at(-1)?.observedAt ?? null)}</span>
        </figcaption>
      </figure> : <div className="hydrology-hydrograph-empty" role="status"><strong>No plottable discharge values</strong><span>The selected range returned no numeric observations; this is not interpreted as zero flow.</span></div>}
      <dl className="hydrology-hydrograph-summary" aria-label="Hydrograph textual summary">
        <div><dt>Minimum</dt><dd>{formatDischarge(hydrographSummary.minimum, hydrographSummary.unit)}</dd></div>
        <div><dt>Maximum</dt><dd>{formatDischarge(hydrographSummary.maximum, hydrographSummary.unit)}</dd></div>
        <div><dt>Latest</dt><dd>{formatDischarge(hydrographSummary.latest?.value ?? null, hydrographSummary.unit)}</dd></div>
        <div><dt>Detected gaps</dt><dd>{gapCount} · threshold {gapMinutes} min</dd></div>
      </dl>
      <p className="hydrology-chart-boundary">{chartSummary} The unsmoothed paths join reported values for readability; values between observations are not inferred.</p>
    </section>}

    {reducedMotion && <p className="hydrology-motion-note">Reduced motion is active. Automatic playback and animated direction effects are off; exact-frame stepping remains available.</p>}
    <footer className="hydrology-boundary">Exact source observations only · no value interpolation · marker size is not flood severity · situational context, not flood guidance or an emergency-warning service.</footer>
  </aside>;
}
