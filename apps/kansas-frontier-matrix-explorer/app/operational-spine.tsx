"use client";

import { useCallback, useEffect, useMemo, useState } from "react";
import { usePathname } from "next/navigation";

type WorkflowAction =
  | "scope"
  | "layers"
  | "time"
  | "measure"
  | "inspect"
  | "evidence"
  | "report"
  | "share";

type ExplorerSnapshot = Readonly<{
  area: string;
  time: string;
  evidence: string;
  selection: string;
  layerCount: number;
  hasArea: boolean;
  hasSelection: boolean;
  drawerOpen: boolean;
  utilityView: string | null;
  reportRecordCount: number | null;
}>;

type WorkflowStep = Readonly<{
  id: WorkflowAction;
  index: string;
  label: string;
  shortLabel: string;
  description: string;
}>;

const DEFAULT_SNAPSHOT: ExplorerSnapshot = Object.freeze({
  area: "Map extent",
  time: "2026",
  evidence: "Demonstration",
  selection: "No selection",
  layerCount: 0,
  hasArea: false,
  hasSelection: false,
  drawerOpen: false,
  utilityView: null,
  reportRecordCount: null,
});

const WORKFLOW_STEPS: readonly WorkflowStep[] = Object.freeze([
  Object.freeze({ id: "scope", index: "01", label: "Area of interest", shortLabel: "Scope", description: "Define the report geography" }),
  Object.freeze({ id: "layers", index: "02", label: "Layer catalog", shortLabel: "Layers", description: "Choose governed context" }),
  Object.freeze({ id: "time", index: "03", label: "Temporal scope", shortLabel: "Time", description: "Set active or comparison time" }),
  Object.freeze({ id: "measure", index: "04", label: "Measurement", shortLabel: "Measure", description: "Quantify spatial context" }),
  Object.freeze({ id: "inspect", index: "05", label: "Feature inspection", shortLabel: "Inspect", description: "Resolve a catalog candidate" }),
  Object.freeze({ id: "evidence", index: "06", label: "Evidence review", shortLabel: "Evidence", description: "Check support and limits" }),
  Object.freeze({ id: "report", index: "07", label: "Report builder", shortLabel: "Report", description: "Compose a reproducible artifact" }),
  Object.freeze({ id: "share", index: "08", label: "Share analysis", shortLabel: "Share", description: "Copy the public-safe view" }),
]);

const normalizedText = (value: string | null | undefined) => value?.replace(/\s+/g, " ").trim() ?? "";

const clickFirstButton = (selector: string, matcher: RegExp): HTMLButtonElement | null => {
  const button = Array.from(document.querySelectorAll<HTMLButtonElement>(selector)).find((candidate) => {
    const searchable = [candidate.textContent, candidate.getAttribute("aria-label"), candidate.getAttribute("title")]
      .map(normalizedText)
      .filter(Boolean)
      .join(" · ");
    return matcher.test(searchable) && !candidate.disabled;
  });
  if (!button) return null;
  button.click();
  return button;
};

const afterExplorerPaint = (callback: () => void) => {
  window.requestAnimationFrame(() => window.requestAnimationFrame(callback));
};

const readExplorerSnapshot = (): ExplorerSnapshot => {
  const params = new URL(window.location.href).searchParams;
  const contextValues = document.querySelectorAll<HTMLElement>(".top-context > span:not(.release-indicator) strong");
  const releaseIndicator = document.querySelector<HTMLElement>(".release-indicator");
  const missionText = normalizedText(document.querySelector<HTMLElement>(".mission-band p")?.textContent);
  const layerMatch = missionText.match(/(?:^|\D)(\d+)\s+layers?\b/i);
  const layerIds = params.get("l")?.split(",").map((id) => id.trim()).filter(Boolean) ?? [];
  const reportText = normalizedText(document.querySelector<HTMLElement>(".report-preview > header > strong")?.textContent);
  const reportMatch = reportText.match(/(\d+)\s+included/i);
  const utilityPanel = document.querySelector<HTMLElement>(".map-utility-panel");
  const evidenceDrawer = document.querySelector<HTMLElement>(".evidence-drawer");
  const selection = normalizedText(contextValues[0]?.textContent) || "No selection";

  return Object.freeze({
    area: params.has("aoi") ? "AOI locked" : "Map extent",
    time: normalizedText(contextValues[1]?.textContent) || params.get("t") || "2026",
    evidence: normalizedText(releaseIndicator?.textContent) || "Demonstration",
    selection,
    layerCount: Number(layerMatch?.[1] ?? layerIds.length),
    hasArea: params.has("aoi"),
    hasSelection: params.has("f"),
    drawerOpen: evidenceDrawer?.dataset.open === "true",
    utilityView: utilityPanel?.dataset.open === "true" ? utilityPanel.dataset.view ?? null : null,
    reportRecordCount: reportMatch ? Number(reportMatch[1]) : null,
  });
};

const statusForStep = (step: WorkflowAction, snapshot: ExplorerSnapshot) => {
  switch (step) {
    case "scope": return snapshot.hasArea ? "ready" : "waiting";
    case "layers": return snapshot.layerCount > 0 ? "ready" : "waiting";
    case "time": return "ready";
    case "measure": return snapshot.utilityView === "measure" ? "active" : "waiting";
    case "inspect": return snapshot.utilityView === "inspect" ? "active" : snapshot.hasSelection ? "ready" : "waiting";
    case "evidence": return snapshot.drawerOpen ? "active" : snapshot.hasSelection ? "ready" : "blocked";
    case "report": return snapshot.utilityView === "report" ? "active" : "ready";
    case "share": return "ready";
  }
};

const detailForStep = (step: WorkflowAction, snapshot: ExplorerSnapshot) => {
  switch (step) {
    case "scope": return snapshot.hasArea ? "Locked" : "Map extent";
    case "layers": return `${snapshot.layerCount} visible`;
    case "time": return snapshot.time;
    case "measure": return snapshot.utilityView === "measure" ? "Workbench open" : "Available";
    case "inspect": return snapshot.hasSelection ? snapshot.selection : "Select a feature";
    case "evidence": return snapshot.hasSelection ? snapshot.evidence : "Needs selection";
    case "report": return snapshot.reportRecordCount === null ? "Live builder" : `${snapshot.reportRecordCount} included`;
    case "share": return "Public-safe view";
  }
};

export default function OperationalSpine() {
  const pathname = usePathname();
  const [snapshot, setSnapshot] = useState<ExplorerSnapshot>(DEFAULT_SNAPSHOT);
  const [currentAction, setCurrentAction] = useState<WorkflowAction>("scope");
  const [announcement, setAnnouncement] = useState("Analysis workflow ready");

  useEffect(() => {
    if (pathname !== "/") return;
    const refresh = () => setSnapshot(readExplorerSnapshot());
    refresh();
    const interval = window.setInterval(refresh, 650);
    window.addEventListener("popstate", refresh);
    window.addEventListener("hashchange", refresh);
    return () => {
      window.clearInterval(interval);
      window.removeEventListener("popstate", refresh);
      window.removeEventListener("hashchange", refresh);
    };
  }, [pathname]);

  const openUtilityView = useCallback((view: "report" | "inspect" | "measure", afterOpen?: () => void) => {
    const panel = document.querySelector<HTMLElement>(".map-utility-panel");
    if (panel?.dataset.open !== "true") {
      clickFirstButton(".map-mobile-actions button, .map-tool-rail button", /^(?:Report|R|Build a custom report)(?:\b|$)/i);
    }
    afterExplorerPaint(() => {
      const tab = document.querySelector<HTMLButtonElement>(`#map-utility-tab-${view}`);
      if (tab && tab.getAttribute("aria-selected") !== "true") tab.click();
      tab?.focus({ preventScroll: true });
      if (afterOpen) afterExplorerPaint(afterOpen);
    });
  }, []);

  const runAction = useCallback((action: WorkflowAction) => {
    setCurrentAction(action);
    switch (action) {
      case "scope":
        openUtilityView("report", () => {
          const draw = clickFirstButton(".report-map-query button", /(?:draw|redraw) on map/i);
          setAnnouncement(draw ? "Area-of-interest drawing opened" : "Report scope controls opened");
        });
        return;
      case "layers": {
        const opened = clickFirstButton(".map-mobile-actions button, .header-workflows button", /^Layers\b/i);
        setAnnouncement(opened ? "Layer catalog opened" : "Layer catalog control was unavailable");
        return;
      }
      case "time": {
        const opened = clickFirstButton(".map-mobile-actions button", /^Time\b/i)
          ?? clickFirstButton(".timeline-toggle", /^Time\b/i);
        setAnnouncement(opened ? "Temporal workspace opened" : "Timeline control was unavailable");
        return;
      }
      case "measure":
        openUtilityView("measure");
        setAnnouncement("Measurement workbench opened");
        return;
      case "inspect":
        openUtilityView("inspect");
        setAnnouncement("Feature inspection workbench opened");
        return;
      case "evidence": {
        const opened = clickFirstButton(".map-mobile-actions button", /^Evidence\b/i);
        if (opened) {
          afterExplorerPaint(() => document.querySelector<HTMLButtonElement>("#drawer-tab-evidence")?.click());
          setAnnouncement("Evidence Drawer opened for the current selection");
        } else {
          openUtilityView("inspect");
          setAnnouncement("Select a feature in Inspect before opening evidence");
        }
        return;
      }
      case "report":
        openUtilityView("report");
        setAnnouncement("Custom report builder opened");
        return;
      case "share": {
        const shared = clickFirstButton(".share-action, .secondary-tools button", /(?:share current map view|share view)/i);
        setAnnouncement(shared ? "Public-safe map view prepared for sharing" : "Share control was unavailable");
        return;
      }
    }
  }, [openUtilityView]);

  const completion = useMemo(() => {
    let completed = 2;
    if (snapshot.hasArea) completed += 1;
    if (snapshot.hasSelection) completed += 2;
    if (snapshot.utilityView === "measure") completed += 1;
    if (snapshot.utilityView === "report") completed += 1;
    return Math.min(WORKFLOW_STEPS.length, completed);
  }, [snapshot]);

  if (pathname !== "/") return null;

  return (
    <>
      <section className="kfm-operational-spine" aria-label="Map-to-report analysis workflow" data-kfm-enhancement="operational-spine-v1">
        <div className="kfm-spine-intro">
          <span>ANALYSIS PATH</span>
          <strong>Map → report</strong>
          <small>{completion} of {WORKFLOW_STEPS.length} stages prepared</small>
        </div>

        <nav className="kfm-workflow-nav" aria-label="Analysis stages">
          {WORKFLOW_STEPS.map((step) => {
            const state = statusForStep(step.id, snapshot);
            return (
              <button
                key={step.id}
                type="button"
                className="kfm-workflow-step"
                data-state={state}
                data-current={currentAction === step.id}
                aria-current={currentAction === step.id ? "step" : undefined}
                aria-label={`${step.label}. ${step.description}. ${detailForStep(step.id, snapshot)}.`}
                onClick={() => runAction(step.id)}
              >
                <span className="kfm-step-index" aria-hidden="true">{step.index}</span>
                <span className="kfm-step-copy"><strong>{step.shortLabel}</strong><small>{detailForStep(step.id, snapshot)}</small></span>
                <i aria-hidden="true" />
              </button>
            );
          })}
        </nav>

        <div className="kfm-spine-trust" data-state={snapshot.hasSelection ? snapshot.evidence.toLowerCase().replaceAll(" ", "-") : "demonstration"}>
          <span>TRUST POSTURE</span>
          <strong>{snapshot.evidence}</strong>
          <small>Rendered context is not evidence</small>
        </div>
        <p className="sr-only" role="status" aria-live="polite">{announcement}</p>
      </section>

      <section className="kfm-report-ribbon" aria-label="Current report context">
        <div className="kfm-report-ribbon__identity">
          <span>REPORT FROM THIS MAP</span>
          <strong>{snapshot.hasSelection ? snapshot.selection : "Kansas spatial context"}</strong>
        </div>
        <dl className="kfm-report-ribbon__metrics">
          <div><dt>Scope</dt><dd>{snapshot.area}</dd></div>
          <div><dt>Time</dt><dd>{snapshot.time}</dd></div>
          <div><dt>Layers</dt><dd>{snapshot.layerCount}</dd></div>
          <div><dt>Evidence</dt><dd>{snapshot.evidence}</dd></div>
        </dl>
        <div className="kfm-report-ribbon__actions">
          <button type="button" onClick={() => runAction("report")}>Review report</button>
          <button type="button" onClick={() => runAction("share")}>Share analysis</button>
        </div>
      </section>
    </>
  );
}
