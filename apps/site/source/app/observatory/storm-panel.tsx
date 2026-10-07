"use client";

import { ROTATION_COLORS, ROTATION_LABELS, describeStormFeature, type StormFrame } from "../nexrad-storms";

const KEY_ROWS = [
  { color: ROTATION_COLORS.none, label: "Storm cell" },
  { color: ROTATION_COLORS.unknown, label: "Rotation not checked" },
  { color: ROTATION_COLORS.weak, label: ROTATION_LABELS.weak },
  { color: ROTATION_COLORS.strong_aloft, label: ROTATION_LABELS.strong_aloft },
  { color: ROTATION_COLORS.strong_low, label: ROTATION_LABELS.strong_low },
  { color: ROTATION_COLORS.tornado_signature, label: `${ROTATION_LABELS.tornado_signature}*` },
] as const;

/** One-line headline that a first-time visitor can read at a glance. */
export function stormHeadline(frame: StormFrame | null): string {
  if (!frame) return "Storm scans not loaded";
  const { cells, rotations, tornadoSignatures } = frame.counts;
  if (!cells && !rotations) return frame.radars.some((radar) => radar.status === "ok") ? "No storm cells detected" : "No radar storm scan for this time";
  const strong = frame.data.features.filter((feature) => feature.properties?.kind === "cell" && ["strong_low", "strong_aloft", "tornado_signature"].includes(String(feature.properties?.rotation))).length;
  return [`${cells} storm cell${cells === 1 ? "" : "s"}`, strong ? `${strong} rotating strongly` : "", tornadoSignatures ? `${tornadoSignatures} tornado signature${tornadoSignatures === 1 ? "" : "s"}*` : ""].filter(Boolean).join(" · ");
}

/** Compact on-map key: what the colors and lines mean, in plain words. */
export function StormMapKey({ frame, onDetails }: { frame: StormFrame | null; onDetails: () => void }) {
  return <aside className="event-storm-key" aria-label="Storm cell map key">
    <strong>{stormHeadline(frame)}</strong>
    <ul>{KEY_ROWS.map((row) => <li key={row.label}><i style={{ background: row.color }} aria-hidden="true" />{row.label}</li>)}
      <li><i className="event-storm-line" aria-hidden="true" />Where it has been</li>
      <li><i className="event-storm-line" data-dashed="true" aria-hidden="true" />Expected path, next hour</li></ul>
    <small>*Radar algorithm flags, not confirmed tornadoes. Click a storm for details.</small>
    <button type="button" onClick={onDetails}>About this layer</button>
  </aside>;
}

export function StormDetails({ frame, selected }: { frame: StormFrame | null; selected: Record<string, unknown> | null }) {
  return <section className="event-feature-values event-storm-details">
    {selected?.kind === "radar" && <><h3>{String(selected.radarName)} radar · {String(selected.radar)}</h3><p>A NOAA WSR-88D Doppler radar. It sees storms best within about 140 miles; farther away its beam passes above low-level rotation.</p></>}
    {selected && selected.kind !== "radar" && <><h3>{selected.kind === "rotation" ? String(selected.rotationLabel) : `Storm ${String(selected.stormId)}`}</h3><p>{describeStormFeature(selected)}</p>
      <dl>
        <div><dt>Radar scan</dt><dd>{String(selected.volumeTime ?? "").replace("T", " · ").replace(".000Z", " UTC")}</dd></div>
        <div><dt>Distance from radar</dt><dd>{String(selected.distanceFromRadarMiles ?? "—")} mi</dd></div>
        {selected.kind === "cell" && <div><dt>Heading</dt><dd>{selected.toward ? `${String(selected.toward)} (${String(selected.towardDeg)}°) · ${String(selected.speedMph)} mph` : "Not reported"}</dd></div>}
        {selected.kind === "rotation" && <div><dt>Strength rank</dt><dd>{String(selected.strengthRank)} of 25 · base {String(selected.baseKft)} kft · depth {String(selected.depthKft)} kft</dd></div>}
      </dl></>}
    <h3>{stormHeadline(frame)}</h3>
    {frame && <ul className="event-storm-radars">{frame.radars.map((radar) => <li key={radar.id} data-status={radar.status}><b>{radar.name}</b> {radar.status === "ok" ? `scan ${radar.volumeTime?.slice(11, 19)} UTC${radar.message.startsWith("Storm cells only") ? " · storm cells only, rotation not checked" : ""}` : radar.status === "no-scan" ? "no scan in the last 12 min" : "unavailable"}</li>)}</ul>}
    <p className="event-small">Each radar scans about every 4–10 minutes. The map shows each radar&apos;s latest scan at or before the clock (up to 12 minutes earlier) and never carries old storms forward. When two radars see the same storm, the closer radar&apos;s view is drawn once.</p>
  </section>;
}
