"use client";

import { useEffect, useRef } from "react";

/**
 * First-visit quick start for the Explorer. It only routes to controls that
 * already exist (layers, time, Underground, Qwen); it never loads
 * data, changes evidence state or stores anything beyond a device-local
 * "seen" flag. Storage access is wrapped because private windows and
 * blocked site data can throw.
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

const STEPS: ReadonlyArray<{ action: ExplorerGuideAction; glyph: string; title: string; body: string }> = [
  { action: "layers", glyph: "≡", title: "Turn on layers", body: "Gauges, radar, geology, roads and more — each with its own source and clock." },
  { action: "time", glyph: "◷", title: "Travel through time", body: "Sweep the atlas year from 1800 to today, or step through dated archives." },
  { action: "underground", glyph: "⛏", title: "Look underground", body: "Frame an area and orbit recorded well and core columns in 3D." },
  { action: "qwen", glyph: "Q", title: "Ask about this view", body: "Get a bounded explanation of what is on screen — never a substitute for evidence." },
];

export function ExplorerGuide({ open, onClose, onAction, onMore }: Readonly<{
  open: boolean;
  onClose: (rememberDismissal: boolean) => void;
  onAction: (action: ExplorerGuideAction) => void;
  onMore?: () => void;
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
  return (
    <section ref={panelRef} className="explorer-guide" role="dialog" aria-modal="false" aria-labelledby="explorer-guide-title" aria-describedby="explorer-guide-summary">
      <header className="explorer-guide-header">
        <p className="explorer-guide-kicker">Quick start</p>
        <h2 id="explorer-guide-title">Explore Kansas through place, time and evidence</h2>
        <p id="explorer-guide-summary">Every layer shows its source, its clock and its limits. Pick a starting point — you can reopen this guide from the <b>?</b> button.</p>
        <button className="explorer-guide-close" type="button" aria-label="Close quick start" onClick={() => onClose(remember())}>×</button>
      </header>
      <ol className="explorer-guide-steps">
        {STEPS.map((step, index) => (
          <li key={step.action}>
            <button type="button" data-guide-autofocus={index === 0 ? "" : undefined} onClick={() => { onAction(step.action); onClose(remember()); }}>
              <span className="explorer-guide-glyph" aria-hidden="true">{step.glyph}</span>
              <span className="explorer-guide-text"><strong>{step.title}</strong><small>{step.body}</small></span>
              <span className="explorer-guide-go" aria-hidden="true">→</span>
            </button>
          </li>
        ))}
      </ol>
      <footer className="explorer-guide-footer">
        <p><kbd>/</kbd> searches places, layers and sources. Click any map feature to open its <b>Evidence Drawer</b>.{onMore && <> <button className="explorer-guide-link" type="button" onClick={() => { onClose(remember()); onMore(); }}>More about the map</button></>}</p>
        <div>
          <label><input ref={rememberRef} type="checkbox" defaultChecked /> Don&apos;t show on start</label>
          <button className="explorer-guide-primary" type="button" onClick={() => onClose(remember())}>Start exploring</button>
        </div>
      </footer>
    </section>
  );
}
