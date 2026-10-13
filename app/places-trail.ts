export const MAX_PLACE_TRAIL_STOPS = 12;

export const normalizePlaceStopName = (value: string, fallbackIndex: number) => {
  const normalized = value.trim().replace(/\s+/g, " ").slice(0, 50);
  return normalized || `Kansas place ${fallbackIndex}`;
};

export const reorderPlaceStops = <T extends Readonly<{ id: string }>>(
  stops: readonly T[],
  stopId: string,
  direction: -1 | 1,
) => {
  const currentIndex = stops.findIndex((stop) => stop.id === stopId);
  const targetIndex = currentIndex + direction;
  if (currentIndex < 0 || targetIndex < 0 || targetIndex >= stops.length) return [...stops];
  const next = [...stops];
  [next[currentIndex], next[targetIndex]] = [next[targetIndex], next[currentIndex]];
  return next;
};

export const nextPlaceStopIndex = (length: number, currentIndex: number, direction: -1 | 1) => {
  if (length <= 0) return -1;
  const safeIndex = currentIndex >= 0 && currentIndex < length ? currentIndex : direction === 1 ? -1 : 0;
  return (safeIndex + direction + length) % length;
};
