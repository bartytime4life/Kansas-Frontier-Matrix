// MapLibre fires "idle" after every rendered frame once nothing is pending, so
// any map animation raises it many times a second. Handlers that rebuild state
// objects there must keep the current object when nothing changed: React only
// skips a re-render when the next state is the same object.

/** True when every field of `next` already holds the same value in `current`
 * (arrays compared item by item). Fields only in `current` are ignored. */
export const sameValues = (current: object, next: object): boolean => Object.entries(next).every(([key, value]) => {
  const prior = (current as Record<string, unknown>)[key];
  return Array.isArray(value) && Array.isArray(prior)
    ? value.length === prior.length && value.every((item, index) => Object.is(item, prior[index]))
    : Object.is(prior, value);
});

/** True when both records have the same keys and values. */
export const sameRecord = (current: object, next: object): boolean =>
  Object.keys(current).length === Object.keys(next).length && sameValues(current, next);
