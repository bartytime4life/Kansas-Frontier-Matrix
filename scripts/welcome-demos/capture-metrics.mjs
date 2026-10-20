/** Preserve native resolution without paying for a needless 2x recording canvas. */
export function capturePixelRatio(width, height) {
  if (!(width > 0 && height > 0)) return 1;
  return Math.min(1.5, Math.max(1, 1280 / width, 720 / height));
}
export function nativeCaptureReady({ width, height, clientWidth, clientHeight }) {
  return width >= 1280 && height >= 720 && clientWidth >= 640 && clientHeight >= 360;
}
/** Disabled overlays must not block a recording of unrelated available map tools. */
export function captureBasemapSourceIds(style) {
  return Object.entries(style?.sources ?? {}).filter(([id]) => !/^(external-|kfm-|scene-)/.test(id)).map(([id]) => id);
}
/** Interpolate only the camera; source records, measurements and clocks stay untouched. */
export function captureCameraAt(start, end, fraction) {
  const t = Math.max(0, Math.min(1, Number.isFinite(fraction) ? fraction : 0));
  const interpolate = (a, b) => a + (b - a) * t;
  return {
    center: [interpolate(start.center[0], end.center[0]), interpolate(start.center[1], end.center[1])],
    zoom: interpolate(start.zoom, end.zoom), pitch: interpolate(start.pitch, end.pitch), bearing: interpolate(start.bearing, end.bearing),
  };
}
/** Decode only our bounded synchronous JPEG canvas export, without idle callbacks. */
export function jpegDataUrlBytes(value) {
  const prefix = 'data:image/jpeg;base64,';
  if (typeof value !== 'string' || !value.startsWith(prefix)) throw new Error('Expected native JPEG export');
  const encoded = value.slice(prefix.length);
  if (encoded.length > Math.ceil(2_000_000 / 3) * 4) throw new Error('Native JPEG exceeds frame limit');
  const binary = atob(encoded);
  if (binary.length > 2_000_000 || binary.charCodeAt(0) !== 255 || binary.charCodeAt(1) !== 216) throw new Error('Invalid native JPEG export');
  const bytes = new Uint8Array(binary.length);
  for (let index = 0; index < binary.length; index++) bytes[index] = binary.charCodeAt(index);
  return bytes;
}
