"use client";
import { useEffect, useState, type ComponentProps } from "react";
export type { SubsurfaceInspection } from "./underground-panel";

type UndergroundModule = typeof import("./underground-panel");
let loaded: UndergroundModule | null = null;
let pending: Promise<UndergroundModule> | null = null;

// Both surfaces share one import. Importing this loader starts no download,
// worker or data request; only mounting a requested surface does.
function loadUnderground() {
  if (loaded) return Promise.resolve(loaded);
  if (!pending) pending = import("./underground-panel").then(module => {
    loaded = module;
    return module;
  }).finally(() => { pending = null; });
  return pending;
}

function useUndergroundModule() {
  const [state, setState] = useState(() => ({ module: loaded, failed: false }));
  const [attempt, setAttempt] = useState(0);
  useEffect(() => {
    let active = true;
    void loadUnderground().then(
      module => { if (active) setState({ module, failed: false }); },
      () => { if (active) setState({ module: null, failed: true }); },
    );
    return () => { active = false; };
  }, [attempt]);
  return { ...state, retry: () => { setState({ module: null, failed: false }); setAttempt(value => value + 1); } };
}

function LoadStatus({ failed, retry }: { failed: boolean; retry: () => void }) {
  return <><p role={failed ? "alert" : "status"}>{failed
    ? "Underground controls could not load. The map and existing layers remain available."
    : "Loading Underground controls…"}</p>{failed && <button type="button" onClick={retry}>Retry Underground</button>}</>;
}

export default function UndergroundPanelLoader(props: ComponentProps<UndergroundModule["default"]>) {
  const state = useUndergroundModule();
  if (state.module) { const Panel = state.module.default; return <Panel {...props} />; }
  return <section className="map-source-status" aria-label="Underground loading" aria-busy={!state.failed}>
    <header><h2>Underground</h2><button type="button" onClick={props.onClose}>Close Underground</button></header>
    <LoadStatus failed={state.failed} retry={state.retry} />
  </section>;
}

export function SubsurfaceInspector(props: ComponentProps<UndergroundModule["SubsurfaceInspector"]>) {
  const state = useUndergroundModule();
  // A record selected in Underground already has the cached module, so its
  // inspector and focus target render immediately with the current props.
  if (state.module) { const Inspector = state.module.SubsurfaceInspector; return <Inspector {...props} />; }
  return <div className="drawer-scroll"><h3 tabIndex={-1} data-subsurface-inspector>Underground record</h3><LoadStatus failed={state.failed} retry={state.retry} /></div>;
}
