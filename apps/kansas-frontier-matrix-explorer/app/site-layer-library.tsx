"use client";

import { useLayoutEffect, useRef } from "react";
import { mountLayerLibrary } from "../../../packages/ui/src/layer-library-view";
import { normalizeWorkspace, projectCatalog, sameWorkspace, type Workspace } from "../../../packages/ui/src/layer-library-model";
import { projectSiteDemoCards, type AnalysisBounds } from "./site-layer-library-metadata";
import { isLayerAvailableAtTime } from "./map-interface";
import type { LayerRecord } from "./explorer-data";

export type SiteLibraryChange = Readonly<{
  visibility: Record<string, boolean>;
  opacity: Record<string, number>;
}>;
type Props = Readonly<{
  layers: readonly LayerRecord[]; visibility: Readonly<Record<string, boolean>>;
  opacity: Readonly<Record<string, number>>; layerOrder: readonly string[];
  area: AnalysisBounds | null; year: number;
  /** Acknowledge only after a synchronous host-owned compare-and-set.
   * This does not certify a React commit, map delivery or persistence.
   */
  onChange: (change: SiteLibraryChange, expected: SiteLibraryChange) => boolean;
  onInspect: (layerId: string) => void;
}>;

/** Same app state, no second map, local store or event-scraping bridge.
 * Hidden row membership lasts for this component session; the existing legacy
 * snapshot persists visibility/opacity/order, not new membership semantics.
 */
export default function SiteLayerLibrary(props: Props) {
  const host = useRef<HTMLSpanElement>(null);
  const latest = useRef(props);
  // Publish props only after React commits, never from an abandoned render.
  useLayoutEffect(() => { latest.current = props; });
  const snapshot = useRef<Workspace>([]);
  const members = useRef(new Set<string>());
  const controller = useRef<ReturnType<typeof mountLayerLibrary> | null>(null);
  const context = () => {
    const p = latest.current;
    return {
      cards: projectSiteDemoCards(p.layers, p.area, (layer) => isLayerAvailableAtTime(layer, p.year))
        .map((card) => ({ ...card, defaultOpacity: p.opacity[card.id!] ?? card.defaultOpacity })),
      areaLabel: p.area ? "Selected analysis bounds (bbox filter)" : "No analysis area selected",
      timeLabel: `Existing year filter: ${p.year}; no interpolation`,
    };
  };
  const synchronize = () => {
    const p = latest.current;
    const projection = context();
    const cards = projectCatalog(projection.cards);
    const allowed = new Set(cards.map((card) => card.id));
    for (const id of allowed) if (p.visibility[id]) members.current.add(id);
    const ids = [...new Set([...p.layerOrder, ...members.current])]
      .filter((id) => allowed.has(id) && members.current.has(id));
    snapshot.current = normalizeWorkspace(ids.map((id) => ({
      id, visible: p.visibility[id] === true, opacity: p.opacity[id] ?? 1,
    })), cards);
    members.current = new Set(snapshot.current.map((layer) => layer.id));
    return projection;
  };
  useLayoutEffect(() => {
    if (!host.current) return;
    const projection = synchronize();
    controller.current = mountLayerLibrary(host.current, {
      read: () => snapshot.current,
      write: (next, expected) => {
        if (!sameWorkspace(snapshot.current, expected)) return false;
        const previousIds = expected.map((layer) => layer.id);
        const byId = new Map(next.map((layer) => [layer.id, layer]));
        const changedIds = [...new Set([...previousIds, ...byId.keys()])];
        const p = latest.current;
        const accepted = p.onChange({
          visibility: Object.fromEntries(changedIds.map((id) => [id, byId.get(id)?.visible ?? false])),
          opacity: Object.fromEntries(next.map((layer) => [layer.id, layer.opacity])),
        }, {
          visibility: Object.fromEntries(changedIds.map((id) => [id, p.visibility[id] === true])),
          opacity: Object.fromEntries(changedIds.map((id) => [id, p.opacity[id] ?? 1])),
        });
        if (accepted !== true) return false;
        snapshot.current = next;
        members.current = new Set(next.map((layer) => layer.id));
        return true;
      },
      inspect: (id) => latest.current.onInspect(id),
    }, projection);
    return () => { controller.current?.destroy(); controller.current = null; };
  }, []);
  useLayoutEffect(() => { controller.current?.update(synchronize()); },
    [props.layers, props.visibility, props.opacity, props.layerOrder, props.area, props.year]);
  return <span ref={host} className="site-layer-library-host" aria-label="Staged layer library" />;
}
