import { BRIDGE_LAB_SNAPSHOTS } from '../bridge-snapshots.mjs';
import { encodeLabView } from '../view-state.mjs';

const BUILT_KANSAS = 'built-kansas';
const WEB_MERCATOR_RADIUS = 6378137;
const RADIANS_PER_DEGREE = Math.PI / 180;

export function bridgeMarker([longitude, latitude], [west, south, east, north]) {
  const eastward = WEB_MERCATOR_RADIUS * longitude * RADIANS_PER_DEGREE;
  const northward = WEB_MERCATOR_RADIUS * Math.asinh(Math.tan(latitude * RADIANS_PER_DEGREE));
  return {
    left: `${100 * (eastward - west) / (east - west)}%`,
    top: `${100 * (north - northward) / (north - south)}%`,
  };
}

export function bridgeInventoryHref(crossing, snapshot = BRIDGE_LAB_SNAPSHOTS[BUILT_KANSAS]) {
  // The record ID identifies a row in this exact source snapshot.
  if (snapshot?.sha256 !== crossing.snapshot.sha256) return null;
  const view = encodeLabView({
    story: BUILT_KANSAS,
    snapshotSha256: snapshot.sha256,
    controls: { query: crossing.structure, selectedId: crossing.snapshot.recordId },
  });
  return `/labs?${new URLSearchParams({ story: BUILT_KANSAS, view })}`;
}
