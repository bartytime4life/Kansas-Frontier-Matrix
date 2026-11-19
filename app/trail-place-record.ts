/** Only public NPS/partner record pages may become clickable trail-site links.
 * Reject overlong URLs instead of silently turning them into different URLs. */
export const safeTrailPlaceRecordUrl = (value: unknown): string | null => {
  if (typeof value !== "string" || /[\u0000-\u001f\u007f]/.test(value)) return null;
  const url = value.trim();
  if (url.length > 240) return null;
  return /^https:\/\/(?:www\.)?(?:nps\.gov|kshs\.org|kansasmemory\.org)\/[\w/?=&%.:#~-]*$/i.test(url) ? url : null;
};
