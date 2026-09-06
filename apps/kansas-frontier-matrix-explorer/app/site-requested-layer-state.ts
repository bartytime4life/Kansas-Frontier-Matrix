/** One app-owned, synchronous requested-layer state owner.
 * React subscribes to this owner; legacy controls and the Library write here.
 * No renderer, storage, network, release or canonical workspace authority.
 */
export type SiteLibraryChange = Readonly<{
  visibility: Readonly<Record<string, boolean>>;
  opacity: Readonly<Record<string, number>>;
}>;
export type SiteRequestedLayers = SiteLibraryChange & Readonly<{ layerOrder: readonly string[] }>;
export type SiteRequestedLayerSnapshot = SiteRequestedLayers & Readonly<{ membershipEpoch: number }>;
type Update<T> = T | ((current: T) => T);
const own = (value: object, key: string) => Object.prototype.hasOwnProperty.call(value, key);
const validOpacity = (value: unknown): value is number =>
  typeof value === "number" && Number.isFinite(value) && value >= 0 && value <= 1;

export function createRequestedLayerStore(initial: SiteRequestedLayers, libraryIds: Iterable<string>) {
  const initialOrder = [...initial.layerOrder];
  const known = new Set(initialOrder);
  const library = new Set(libraryIds);
  const listeners = new Set<() => void>();
  const capture = (value: SiteRequestedLayers, membershipEpoch: number): SiteRequestedLayerSnapshot => {
    if (known.size !== initialOrder.length || value.layerOrder.length !== known.size
      || new Set(value.layerOrder).size !== known.size || value.layerOrder.some((id) => !known.has(id))
      || Object.keys(value.visibility).length !== known.size || Object.keys(value.opacity).length !== known.size
      || [...known].some((id) => !own(value.visibility, id) || !own(value.opacity, id)
        || typeof value.visibility[id] !== "boolean" || !validOpacity(value.opacity[id]))) {
      throw new TypeError("Invalid requested-layer state.");
    }
    return Object.freeze({ visibility: Object.freeze({ ...value.visibility }),
      opacity: Object.freeze({ ...value.opacity }), layerOrder: Object.freeze([...value.layerOrder]), membershipEpoch });
  };
  const serverSnapshot = capture(initial, 0);
  let state = serverSnapshot;
  const publish = (value: SiteRequestedLayers, epoch = state.membershipEpoch) => {
    const next = capture(value, epoch); // Validate/copy both maps before any mutation.
    state = next;
    for (const listener of [...listeners]) listener();
  };
  return Object.freeze({
    getSnapshot: () => state,
    getServerSnapshot: () => serverSnapshot,
    subscribe: (listener: () => void) => { listeners.add(listener); return () => { listeners.delete(listener); }; },
    setVisibility: (update: Update<Readonly<Record<string, boolean>>>) => {
      const visibility = typeof update === "function" ? update(state.visibility) : update;
      publish({ ...state, visibility });
    },
    setOpacity: (update: Update<Readonly<Record<string, number>>>) => {
      const opacity = typeof update === "function" ? update(state.opacity) : update;
      publish({ ...state, opacity });
    },
    setLayerOrder: (update: Update<readonly string[]>) => {
      const layerOrder = typeof update === "function" ? update(state.layerOrder) : update;
      publish({ ...state, layerOrder });
    },
    // Restore/reset is one layer-state change. This epoch is not persisted.
    replace: (value: SiteRequestedLayers) => publish(value, state.membershipEpoch + 1),
    compareAndSet: (next: SiteLibraryChange, expected: SiteLibraryChange): boolean => {
      const ids = new Set([...Object.keys(next.visibility), ...Object.keys(next.opacity)]);
      if (!ids.size || Object.keys(expected.visibility).length !== ids.size
        || Object.keys(expected.opacity).length !== ids.size) return false;
      for (const id of ids) {
        if (!known.has(id) || !library.has(id) || !own(expected.visibility, id) || !own(expected.opacity, id)
          || state.visibility[id] !== expected.visibility[id] || state.opacity[id] !== expected.opacity[id]
          || (own(next.visibility, id) && typeof next.visibility[id] !== "boolean")
          || (own(next.opacity, id) && !validOpacity(next.opacity[id]))) return false;
      }
      publish({ ...state, visibility: { ...state.visibility, ...next.visibility },
        opacity: { ...state.opacity, ...next.opacity } });
      // Confirms acceptance by this state owner, not a React paint or map delivery.
      return true;
    },
  });
}
