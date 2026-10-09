import type { FeatureCollection } from "geojson";

/** Same features in the same order: identical objects, or equal content
 * (frame builders such as the streamflow frame create fresh objects). */
export function sameFeatures(prior: FeatureCollection, next: FeatureCollection): boolean {
  if (prior === next) return true;
  if (prior.features.length !== next.features.length) return false;
  return next.features.every((feature, index) => {
    const before = prior.features[index];
    return before === feature || JSON.stringify(before) === JSON.stringify(feature);
  });
}

/**
 * The collection a source should receive for a playback frame. When the frame's
 * features are the ones the source already holds, the held object is returned so
 * the upload is skipped: MapLibre does not re-tile it, the frame does not wait on
 * it, and its layers can stay visible because their pixels are correct for both
 * the committed and the requested time.
 */
export function reuseUnchanged<T extends FeatureCollection>(held: T | undefined, next: T): T {
  return held && sameFeatures(held, next) ? held : next;
}
