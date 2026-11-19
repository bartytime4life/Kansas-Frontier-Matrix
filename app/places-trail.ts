export const MAX_PLACE_TRAIL_STOPS = 12;
export const PLACES_FULL_MESSAGE = `Places is full (${MAX_PLACE_TRAIL_STOPS} maximum). Remove a saved place before adding another.`;

/** Undo inserts the original stop without evicting or replacing another stop. */
export function restorePlaceStop<T extends Readonly<{ id: string }>>(stops: readonly T[], stop: T, index: number): T[] | null {
  if (stops.length >= MAX_PLACE_TRAIL_STOPS || stops.some(item => item.id === stop.id) || !Number.isInteger(index) || index < 0) return null;
  const next = [...stops];
  next.splice(Math.min(index, next.length), 0, stop);
  return next;
}

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
