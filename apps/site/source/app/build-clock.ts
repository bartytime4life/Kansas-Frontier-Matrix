declare const __KFM_BUILD_UTC_YEAR__: number;

// The build embeds the same year in server and browser bundles. The fallback
// keeps direct module tests deterministic without depending on the host clock.
export const BUILD_UTC_YEAR = typeof __KFM_BUILD_UTC_YEAR__ === "number"
  ? __KFM_BUILD_UTC_YEAR__
  : 2026;
