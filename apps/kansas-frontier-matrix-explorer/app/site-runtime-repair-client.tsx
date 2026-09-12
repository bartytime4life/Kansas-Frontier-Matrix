"use client";

import { useEffect, useLayoutEffect, useRef, useState } from "react";
import { findFeature, LAYER_REGISTRY } from "./explorer-data";
import {
  canonicalizeExplorerUrl,
  DEGRADED_GUIDANCE_STEPS,
  LOCATION_CAMERA_REDACTION_VALUE,
  PRIVATE_CAMERA_VISIBLE_LABEL,
  redactScreenReaderStatus,
  relativeExplorerUrl,
  type DegradedGuidanceStep,
} from "./site-runtime-repair";

type GuidanceMode = "closed" | "examples" | "story";

const hasFeature = (featureId: string): boolean => Boolean(findFeature(featureId));

const repairUrl = (input: string | URL): URL => canonicalizeExplorerUrl(
  input,
  LAYER_REGISTRY,
  hasFeature,
);

const canonicalizeHistoryArgument = (
  value: string | URL | null | undefined,
): string | URL | null | undefined => {
  if (value === null || value === undefined) return value;
  try {
    const candidate = new URL(String(value), window.location.href);
    if (candidate.origin !== window.location.origin) return value;
    return relativeExplorerUrl(repairUrl(candidate));
  } catch {
    return value;
  }
};

const privateCameraIsActive = (): boolean => new URL(window.location.href)
  .searchParams.get("privacy") === LOCATION_CAMERA_REDACTION_VALUE;

const repairPrivateCoordinateProjection = (): void => {
  if (!privateCameraIsActive()) return;

  const statusSpans = document.querySelectorAll<HTMLElement>(".status-bar > span");
  const coordinateStatus = statusSpans.item(1);
  if (coordinateStatus && coordinateStatus.textContent !== PRIVATE_CAMERA_VISIBLE_LABEL) {
    coordinateStatus.textContent = PRIVATE_CAMERA_VISIBLE_LABEL;
  }

  const assistiveStatus = document.querySelector<HTMLElement>(".screenreader-status");
  if (assistiveStatus) {
    const current = assistiveStatus.textContent ?? "";
    const redacted = redactScreenReaderStatus(current);
    if (redacted !== current) assistiveStatus.textContent = redacted;
  }
};

const applyGuidanceStep = (step: DegradedGuidanceStep): void => {
  const url = repairUrl(new URL(window.location.href));
  const visibleLayers = new Set(
    (url.searchParams.get("l") ?? "").split(",").filter(Boolean),
  );
  visibleLayers.add(step.layerId);

  url.searchParams.set("l", Array.from(visibleLayers).join(","));
  url.searchParams.set("t", String(step.year));
  url.searchParams.set("f", step.featureId);
  url.searchParams.set("ws", "trust");
  url.searchParams.set("panel", "evidence");
  url.searchParams.set("drawer", "open");
  url.searchParams.set("focusStage", "outcome");
  url.searchParams.set("focusIntent", "explain");

  window.history.pushState(window.history.state, "", relativeExplorerUrl(repairUrl(url)));
  window.dispatchEvent(new PopStateEvent("popstate", { state: window.history.state }));
};

const panelStyle: React.CSSProperties = {
  position: "fixed",
  right: 16,
  bottom: 72,
  zIndex: 70,
  width: "min(390px, calc(100vw - 32px))",
  maxHeight: "min(620px, calc(100vh - 110px))",
  overflow: "auto",
  padding: 18,
  border: "1px solid rgba(212, 175, 97, 0.72)",
  borderRadius: 12,
  background: "rgba(17, 28, 25, 0.97)",
  boxShadow: "0 20px 60px rgba(0, 0, 0, 0.45)",
  color: "#f5f3ea",
};

const buttonStyle: React.CSSProperties = {
  border: "1px solid rgba(212, 175, 97, 0.55)",
  borderRadius: 8,
  background: "rgba(255, 255, 255, 0.06)",
  color: "inherit",
  padding: "10px 12px",
  textAlign: "left",
  cursor: "pointer",
};

export default function SiteRuntimeRepair() {
  const [degraded, setDegraded] = useState(false);
  const [mode, setMode] = useState<GuidanceMode>("closed");
  const [storyIndex, setStoryIndex] = useState(0);
  const syncQueued = useRef(false);
  const closeButtonRef = useRef<HTMLButtonElement | null>(null);

  useLayoutEffect(() => {
    const originalReplaceState = window.history.replaceState.bind(window.history);
    const originalPushState = window.history.pushState.bind(window.history);

    const sync = () => {
      repairPrivateCoordinateProjection();
      const nextDegraded = Boolean(document.querySelector(".runtime-degraded-banner"));
      setDegraded((current) => current === nextDegraded ? current : nextDegraded);
      if (!nextDegraded) setMode("closed");
    };
    const scheduleSync = () => {
      if (syncQueued.current) return;
      syncQueued.current = true;
      queueMicrotask(() => {
        syncQueued.current = false;
        sync();
      });
    };

    window.history.replaceState = ((data: unknown, unused: string, url?: string | URL | null) => {
      const result = originalReplaceState(data, unused, canonicalizeHistoryArgument(url));
      scheduleSync();
      return result;
    }) as History["replaceState"];
    window.history.pushState = ((data: unknown, unused: string, url?: string | URL | null) => {
      const result = originalPushState(data, unused, canonicalizeHistoryArgument(url));
      scheduleSync();
      return result;
    }) as History["pushState"];

    const initialUrl = repairUrl(new URL(window.location.href));
    const initialRelativeUrl = relativeExplorerUrl(initialUrl);
    const currentRelativeUrl = `${window.location.pathname}${window.location.search}${window.location.hash}`;
    if (initialRelativeUrl !== currentRelativeUrl) {
      originalReplaceState(window.history.state, "", initialRelativeUrl);
    }

    const observer = new MutationObserver(scheduleSync);
    observer.observe(document.body, { childList: true, characterData: true, subtree: true });
    window.addEventListener("popstate", scheduleSync);
    sync();

    return () => {
      observer.disconnect();
      window.removeEventListener("popstate", scheduleSync);
      window.history.replaceState = originalReplaceState;
      window.history.pushState = originalPushState;
    };
  }, []);

  useEffect(() => {
    if (mode === "closed") return;
    closeButtonRef.current?.focus();
    const closeOnEscape = (event: KeyboardEvent) => {
      if (event.key === "Escape") setMode("closed");
    };
    document.addEventListener("keydown", closeOnEscape);
    return () => document.removeEventListener("keydown", closeOnEscape);
  }, [mode]);

  if (!degraded) return null;

  const activeStoryStep = DEGRADED_GUIDANCE_STEPS[storyIndex] ?? DEGRADED_GUIDANCE_STEPS[0];

  return (
    <div data-kfm-runtime-repair="degraded-guidance">
      {mode === "closed" && (
        <button
          type="button"
          aria-label="Open degraded-runtime guide"
          onClick={() => setMode("examples")}
          style={{
            ...buttonStyle,
            position: "fixed",
            right: 16,
            bottom: 72,
            zIndex: 69,
            background: "#172923",
            fontWeight: 700,
          }}
        >
          Guide
        </button>
      )}

      {mode !== "closed" && (
        <aside role="dialog" aria-modal="false" aria-labelledby="degraded-guide-title" style={panelStyle}>
          <header style={{ display: "flex", alignItems: "flex-start", justifyContent: "space-between", gap: 12 }}>
            <div>
              <small style={{ letterSpacing: ".12em", color: "#d4af61" }}>RENDERER-NEUTRAL GUIDE</small>
              <h2 id="degraded-guide-title" style={{ margin: "6px 0 8px", fontSize: 22 }}>
                Explore trust states while the renderer is held
              </h2>
            </div>
            <button ref={closeButtonRef} type="button" aria-label="Close degraded-runtime guide" onClick={() => setMode("closed")} style={buttonStyle}>×</button>
          </header>
          <p style={{ margin: "0 0 14px", lineHeight: 1.5, color: "#d6ded9" }}>
            These actions use existing site-local fixtures and the Evidence Drawer. They do not activate MapLibre, fetch a source, or publish data.
          </p>

          {mode === "examples" && (
            <>
              <div style={{ display: "grid", gap: 8 }}>
                {DEGRADED_GUIDANCE_STEPS.filter((step) => step.id !== "superseded").map((step) => (
                  <button key={step.id} type="button" onClick={() => { applyGuidanceStep(step); setMode("closed"); }} style={buttonStyle}>
                    <small style={{ color: "#d4af61" }}>{step.state}</small>
                    <strong style={{ display: "block", marginTop: 3 }}>{step.title}</strong>
                    <span style={{ display: "block", marginTop: 4, color: "#c8d1cc", lineHeight: 1.4 }}>{step.summary}</span>
                  </button>
                ))}
              </div>
              <button type="button" onClick={() => { setStoryIndex(0); setMode("story"); }} style={{ ...buttonStyle, width: "100%", marginTop: 12, textAlign: "center", fontWeight: 700 }}>
                Start four-step trust story
              </button>
            </>
          )}

          {mode === "story" && (
            <>
              <article style={{ ...buttonStyle, cursor: "default" }}>
                <small style={{ color: "#d4af61" }}>STEP {storyIndex + 1} OF {DEGRADED_GUIDANCE_STEPS.length} · {activeStoryStep.state}</small>
                <h3 style={{ margin: "8px 0 6px" }}>{activeStoryStep.title}</h3>
                <p style={{ margin: 0, color: "#c8d1cc", lineHeight: 1.45 }}>{activeStoryStep.summary}</p>
              </article>
              <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 8, marginTop: 10 }}>
                <button type="button" onClick={() => applyGuidanceStep(activeStoryStep)} style={buttonStyle}>Open this step</button>
                <button
                  type="button"
                  onClick={() => setStoryIndex((current) => Math.min(DEGRADED_GUIDANCE_STEPS.length - 1, current + 1))}
                  disabled={storyIndex >= DEGRADED_GUIDANCE_STEPS.length - 1}
                  style={buttonStyle}
                >
                  Next step
                </button>
                <button
                  type="button"
                  onClick={() => setStoryIndex((current) => Math.max(0, current - 1))}
                  disabled={storyIndex === 0}
                  style={buttonStyle}
                >
                  Previous
                </button>
                <button type="button" onClick={() => setMode("examples")} style={buttonStyle}>Quick examples</button>
              </div>
            </>
          )}
        </aside>
      )}
    </div>
  );
}
