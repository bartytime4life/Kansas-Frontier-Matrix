"use client";

import { useEffect, useRef } from "react";
import { IS_PUBLIC_COPY } from "./public-profile";
import { ATLAS_MISSION_GROUPS, atlasMissionAvailability } from "./map-starters";

/**
 * First-visit chooser over existing controls and question drafts. It never
 * sends a model request, activates data, or changes evidence state. The only
 * optional storage remains the device-local dismissal flag.
 */
export const EXPLORER_GUIDE_STORAGE_KEY = "kfm.explorer.guide.dismissed.v1";

export type ExplorerGuideAction = "layers" | "time" | "underground" | "qwen";

export function readExplorerGuideDismissed(): boolean {
  try {
    return window.localStorage.getItem(EXPLORER_GUIDE_STORAGE_KEY) === "1";
  } catch {
    return false;
  }
}

export function writeExplorerGuideDismissed(dismissed: boolean): void {
  try {
    if (dismissed) window.localStorage.setItem(EXPLORER_GUIDE_STORAGE_KEY, "1");
    else window.localStorage.removeItem(EXPLORER_GUIDE_STORAGE_KEY);
  } catch {
    // Device storage is optional; the guide still closes for this session.
  }
}

const PRIVATE_STEPS: ReadonlyArray<{ action: ExplorerGuideAction; glyph: string; title: string; body: string }> = [
  { action: "layers", glyph: "≡", title: "Start with a purpose", body: "Choose a small layer set for land, learning, science or planning, then customize your map." },
  { action: "time", glyph: "◷", title: "Travel through time", body: "Explore map time and dated archives. Source dates and gaps remain distinct from the display clock." },
  { action: "underground", glyph: "⛏", title: "Look underground", body: "Frame an area and orbit recorded well and core columns in 3D." },
  { action: "qwen", glyph: "Q", title: "Ask about this view", body: "Get a bounded explanation of what is on screen — never a substitute for evidence." },
];

const PUBLIC_STEPS: typeof PRIVATE_STEPS = [
 { action: "layers", glyph: "≡", title: "Check available layers", body: "Check source roles, release holds and missing coverage before using a layer." },
 { action: "time", glyph: "◷", title: "Explore source dates", body: "Actual source dates stay separate from atlas time. Unobserved history is not reconstructed." },
 { action: "underground", glyph: "⛏", title: "Inspect original logs", body: "Recorded intervals remain unavailable until their public release is approved." },
];
const STEPS = IS_PUBLIC_COPY ? PUBLIC_STEPS : PRIVATE_STEPS;

export function ExplorerGuide({ open, onClose, onAction, onMore, onMission, onChoosePlace }: Readonly<{
  open: boolean;
  onClose: (rememberDismissal: boolean) => void;
  onAction: (action: ExplorerGuideAction) => void;
  onMore?: () => void;
  onMission?: (query: string, starterId?: string) => void;
  onChoosePlace?: () => void;
}>) {
  const panelRef = useRef<HTMLElement | null>(null);
  const rememberRef = useRef<HTMLInputElement | null>(null);
  const onCloseRef = useRef(onClose);
  useEffect(() => { onCloseRef.current = onClose; }, [onClose]);

  useEffect(() => {
    if (!open) return;
    const first = panelRef.current?.querySelector<HTMLElement>("[data-guide-autofocus]");
    first?.focus({ preventScroll: true });
    const onKeyDown = (event: KeyboardEvent) => {
      if (event.key === "Escape" && panelRef.current?.contains(document.activeElement)) {
        event.stopPropagation();
        onCloseRef.current(Boolean(rememberRef.current?.checked));
      }
    };
    window.addEventListener("keydown", onKeyDown);
    return () => window.removeEventListener("keydown", onKeyDown);
  }, [open]);

  if (!open) return null;
  const remember = () => Boolean(rememberRef.current?.checked);
  const chooseMission = (query: string, starterId?: string) => {
    if (IS_PUBLIC_COPY) onAction(starterId === "historical-landscape" ? "time" : "layers");
    else if (onMission) onMission(query, starterId);
    else onAction(starterId ? "layers" : "qwen");
    onClose(remember());
  };
  return (
    <section ref={panelRef} className="explorer-guide" role="dialog" aria-modal="false" aria-labelledby="explorer-guide-title" aria-describedby="explorer-guide-summary">
      <header className="explorer-guide-header">
        <p className="explorer-guide-kicker">Atlas Studio · Prairie Field Desk</p>
        <h2 id="explorer-guide-title">What would you like to explore?</h2>
        <p id="explorer-guide-summary">{IS_PUBLIC_COPY ? "Start with a Kansas place, then check available sources, dates and release limits. This restricted preview keeps unapproved data withheld." : "Start with a Kansas place and a question. Follow its sources, dates and limits, then save what you learn."}</p>
        <button className="explorer-guide-close" type="button" aria-label="Close quick start" onClick={() => onClose(remember())}>×</button>
      </header>
      <div className="atlas-welcome-place">
        <button type="button" data-guide-autofocus="" onClick={() => { if (onChoosePlace) onChoosePlace(); else onAction(IS_PUBLIC_COPY ? "layers" : "qwen"); onClose(remember()); }}>Find a place or layer</button>
        <p>Search the available index without waiting for an AI model. County records require an approved source.</p>
      </div>
      <div className="atlas-welcome-intents" role="group" aria-label="Starting investigations">
        <button type="button" onClick={() => chooseMission("What can I learn about this place from the available county, land and water sources? Show the dates and limits.", "learning-kansas")}>
          <strong>Understand this place</strong><small>Begin with county and landscape context.</small>
        </button>
        <button type="button" onClick={() => chooseMission("Help me investigate change in this place using available dated sources. Identify which times and layers can actually be compared.", "historical-landscape")}>
          <strong>Investigate change</strong><small>Find dated sources and compatible comparisons.</small>
        </button>
        <button type="button" onClick={() => { if (onChoosePlace) onChoosePlace(); else onAction(IS_PUBLIC_COPY ? "layers" : "qwen"); onClose(remember()); }}>
          <strong>Find places &amp; layers</strong><small>Search the available index without the AI model.</small>
        </button>
      </div>
      <p className="atlas-welcome-boundary">{IS_PUBLIC_COPY ? "Layer and time actions open existing controls. They do not approve data or call an AI model. Chat with KFM opens the separate live website; no map selection or draft is transferred." : <>Question starters prepare unverified discussion drafts for you to review and send. They do not search the corpus, change layers or start an AI request. Use Find or Evidence in the composer to retrieve records. Existing context recipes remain in Layers with their source dates and limits.</>}</p>
      {IS_PUBLIC_COPY ? <div className="atlas-welcome-topics"><a href="/topics">Explore all topics &amp; audiences →</a></div> : <details className="atlas-welcome-topics">
        <summary>Explore all topics &amp; audiences</summary>
        <p>Choose a discussion prompt for your topic. These drafts do not promise indexed data; check Find or Evidence for actual coverage.</p>
        <div className="atlas-welcome-groups">
          {ATLAS_MISSION_GROUPS.map(group => <details key={group.id} className="atlas-welcome-group">
            <summary>{group.title}<small>{group.missions.length} starting questions</small></summary>
            <p>{group.description}</p>
            <ul>{group.missions.map(mission => <li key={mission.id}>
              <button type="button" onClick={() => chooseMission(mission.question, mission.starterId)}>
                <strong>{mission.title}</strong><small>{atlasMissionAvailability(mission)}</small>
              </button>
            </li>)}</ul>
          </details>)}
        </div>
      </details>}
      <details className="atlas-welcome-tools">
        <summary>Map tools &amp; help</summary>
        <ol className="explorer-guide-steps">
        {STEPS.map(step => (
          <li key={step.action}>
            <button type="button" onClick={() => { onAction(step.action); onClose(remember()); }}>
              <span className="explorer-guide-text"><strong>{step.title}</strong><small>{step.body}</small></span>
              <span className="explorer-guide-go" aria-hidden="true">→</span>
            </button>
          </li>
        ))}
      </ol>
      </details>
      <footer className="explorer-guide-footer">
        <p>{IS_PUBLIC_COPY ? <>Use search for available layers and places. Check sources and holds in the <b>Evidence Drawer</b>. Reopen this chooser with <b>?</b>.</> : <>Use Find for places and layers, Evidence for released records, and Ask for discussion. Inspect a map selection in its <b>Evidence Drawer</b>. Reopen this chooser with <b>?</b>.</>}{onMore && <> <button className="explorer-guide-link" type="button" onClick={() => { onClose(remember()); onMore(); }}>More about the map</button></>}</p>
        <div>
          <label><input ref={rememberRef} type="checkbox" defaultChecked /> Don&apos;t show on start</label>
          <button className="explorer-guide-primary" type="button" onClick={() => onClose(remember())}>Explore freely</button>
        </div>
      </footer>
    </section>
  );
}
