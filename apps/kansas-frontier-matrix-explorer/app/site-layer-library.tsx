"use client";

import { useLayoutEffect, useRef } from "react";
import { mountLayerLibrary } from "../../../packages/ui/src/layer-library-view";
import { normalizeWorkspace, projectCatalog, sameWorkspace, type Workspace } from "../../../packages/ui/src/layer-library-model";
import { projectSiteDemoCards, type AnalysisBounds } from "./site-layer-library-metadata";
import { isLayerAvailableAtTime } from "./map-interface";
import type { LayerRecord } from "./explorer-data";
import type { SiteLibraryChange, SiteRequestedLayerSnapshot } from "./site-requested-layer-state";
export type { SiteLibraryChange } from "./site-requested-layer-state";

type Props = Readonly<{
  layers: readonly LayerRecord[]; visibility: Readonly<Record<string, boolean>>;
  opacity: Readonly<Record<string, number>>; layerOrder: readonly string[];
  area: AnalysisBounds | null; year: number; membershipEpoch: number;
  /** Read the same synchronous owner used by EVERY app writer, not cached props. */
  readState: () => SiteRequestedLayerSnapshot;
  onChange: (change: SiteLibraryChange, expected: SiteLibraryChange) => boolean;
  onInspect: (layerId: string) => void;
}>;

const CATALOG_SCROLL_SELECTOR = ".layer-panel .catalog-groups";
const CATALOG_SCROLL_TOLERANCE = 2;
const CATALOG_ENHANCEMENT_ATTRIBUTES = [
  "tabindex", "role", "aria-label", "data-scrollable", "data-at-start", "data-at-end",
  "data-layer-count", "data-requested-count", "data-time-compatible-count",
] as const;

function catalogScrollState(region: HTMLElement) {
  const scrollable = region.scrollHeight - region.clientHeight > CATALOG_SCROLL_TOLERANCE;
  return {
    scrollable,
    atStart: !scrollable || region.scrollTop <= CATALOG_SCROLL_TOLERANCE,
    atEnd: !scrollable || region.scrollTop + region.clientHeight >= region.scrollHeight - CATALOG_SCROLL_TOLERANCE,
  };
}

function syncCatalogScrollState(region: HTMLElement) {
  const state = catalogScrollState(region);
  region.dataset.scrollable = String(state.scrollable);
  region.dataset.atStart = String(state.atStart);
  region.dataset.atEnd = String(state.atEnd);
}

/** Progressively expose the existing full catalog as one keyboard-scrollable region.
 * This adds presentation and accessibility metadata only: it never clicks a control,
 * changes requested visibility, reads source data, or crosses the renderer boundary.
 */
function enhanceCatalogScrollRegion() {
  const region = document.querySelector<HTMLElement>(CATALOG_SCROLL_SELECTOR);
  if (!region) return;
  const previous = new Map(CATALOG_ENHANCEMENT_ATTRIBUTES.map((name) => [name, region.getAttribute(name)]));
  region.tabIndex = 0;
  region.setAttribute("role", "region");

  const sync = () => syncCatalogScrollState(region);
  region.addEventListener("scroll", sync, { passive: true });
  window.addEventListener("resize", sync, { passive: true });
  const resizeObserver = typeof ResizeObserver === "function" ? new ResizeObserver(sync) : null;
  resizeObserver?.observe(region);
  const mutationObserver = typeof MutationObserver === "function" ? new MutationObserver(sync) : null;
  mutationObserver?.observe(region, {
    childList: true,
    subtree: true,
    characterData: true,
    attributes: true,
    attributeFilter: ["aria-expanded", "data-active", "hidden"],
  });
  sync();

  return () => {
    region.removeEventListener("scroll", sync);
    window.removeEventListener("resize", sync);
    resizeObserver?.disconnect();
    mutationObserver?.disconnect();
    for (const [name, value] of previous) {
      if (value === null) region.removeAttribute(name);
      else region.setAttribute(name, value);
    }
  };
}

/** A failed owner read can still show bounded supplied metadata, but the port's
 * read below must throw so controls fail closed; this fallback is never state acknowledgement. */
function projectContext(p: Props) {
  let state: SiteRequestedLayerSnapshot;
  try { state = p.readState(); }
  catch { state = { visibility: p.visibility, opacity: p.opacity, layerOrder: p.layerOrder, membershipEpoch: p.membershipEpoch }; }
  return {
    cards: projectSiteDemoCards(p.layers, p.area, (layer) => isLayerAvailableAtTime(layer, p.year))
      .map((card) => ({ ...card, defaultOpacity: state.opacity[card.id!] ?? card.defaultOpacity })),
    areaLabel: p.area ? "Selected analysis bounds (bbox filter)" : "No analysis area selected",
    timeLabel: `Existing year filter: ${p.year}; no interpolation`,
    fixedOrder: state.layerOrder, workspaceEpoch: state.membershipEpoch,
  };
}

/** Only hidden row membership is session-local. Visibility, opacity and order
 * always come from the existing app's state owner, including immediate readback.
 * The legacy saved-workspace format is neither migrated nor silently extended.
 */
export default function SiteLayerLibrary(props: Props) {
  const host = useRef<HTMLSpanElement>(null);
  const latest = useRef(props);
  useLayoutEffect(() => { latest.current = props; });
  const members = useRef(new Set<string>());
  const epoch = useRef<number | null>(null);
  const controller = useRef<ReturnType<typeof mountLayerLibrary> | null>(null);
  const requestedCount = props.layers.reduce((count, layer) => count + Number(props.visibility[layer.id] === true), 0);
  const timeCompatibleCount = props.layers.reduce((count, layer) => count + Number(isLayerAvailableAtTime(layer, props.year)), 0);

  useLayoutEffect(() => enhanceCatalogScrollRegion(), []);
  useLayoutEffect(() => {
    const region = document.querySelector<HTMLElement>(CATALOG_SCROLL_SELECTOR);
    if (!region) return;
    region.dataset.layerCount = String(props.layers.length);
    region.dataset.requestedCount = String(requestedCount);
    region.dataset.timeCompatibleCount = String(timeCompatibleCount);
    region.setAttribute("aria-label",
      `Layer catalog: ${props.layers.length} controls; ${requestedCount} requested visible; ${timeCompatibleCount} time-compatible at ${props.year}. Scroll to reach every layer.`);
    syncCatalogScrollState(region);
  }, [props.layers.length, props.year, requestedCount, timeCompatibleCount]);

  useLayoutEffect(() => {
    if (!host.current) return;
    const context = () => projectContext(latest.current);
    const read = (): Workspace => {
      const state = latest.current.readState();
      if (epoch.current !== state.membershipEpoch) {
        members.current.clear(); epoch.current = state.membershipEpoch;
      }
      for (const card of projectCatalog(context().cards)) {
        if (state.visibility[card.id]) members.current.add(card.id);
      }
      // Retain revoked member IDs only inside the cleanup transaction. The view
      // projects them out before rendering; refused cleanup must not disclose them.
      return Object.freeze([...new Set([...state.layerOrder, ...members.current])]
        .filter((id) => members.current.has(id))
        .map((id) => Object.freeze({ id, visible: state.visibility[id] === true, opacity: state.opacity[id] ?? 1 })));
    };
    controller.current = mountLayerLibrary(host.current, {
      read,
      write: (next, expected) => {
        if (!sameWorkspace(read(), expected)) return false;
        const state = latest.current.readState();
        const cards = projectCatalog(context().cards);
        if (!sameWorkspace(next, normalizeWorkspace(next, cards))) return false;
        const nextIds = new Set(next.map((item) => item.id));
        const fixedOrder = state.layerOrder.filter((id) => nextIds.has(id));
        if (fixedOrder.length !== next.length || next.some((item, index) => item.id !== fixedOrder[index])) return false;
        const byId = new Map(next.map((layer) => [layer.id, layer]));
        const changedIds = [...new Set([...expected.map((layer) => layer.id), ...byId.keys()])];
        const accepted = latest.current.onChange({
          visibility: Object.fromEntries(changedIds.map((id) => [id, byId.get(id)?.visible ?? false])),
          opacity: Object.fromEntries(next.map((layer) => [layer.id, layer.opacity])),
        }, {
          visibility: Object.fromEntries(changedIds.map((id) => [id, state.visibility[id] === true])),
          opacity: Object.fromEntries(changedIds.map((id) => [id, state.opacity[id] ?? 1])),
        });
        if (accepted !== true) return false;
        members.current = new Set(next.map((layer) => layer.id));
        return true; // The view immediately reads the actual owner again.
      },
      inspect: (id) => latest.current.onInspect(id),
    }, context(), { dialogHost: document.body });
    return () => { controller.current?.destroy(); controller.current = null; };
  }, []);
  useLayoutEffect(() => {
    controller.current?.update(projectContext(latest.current));
  }, [props.layers, props.visibility, props.opacity, props.layerOrder, props.area, props.year, props.membershipEpoch]);
  return <span className="site-layer-library-shell">
    <span ref={host} className="site-layer-library-host" aria-label="Inspected fixture layer library" />
    <span className="site-layer-library-summary" role="status" aria-live="polite"
      aria-label={`${requestedCount} layers requested visible; ${timeCompatibleCount} time-compatible at ${props.year}; renderer delivery remains held.`}>
      <span><strong>{requestedCount}</strong> requested</span><i aria-hidden="true">·</i><span><strong>{timeCompatibleCount}</strong> time match</span>
    </span>
  </span>;
}
