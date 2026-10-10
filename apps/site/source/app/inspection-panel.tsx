"use client";
import { useCallback, useState } from "react";

type InspectionPanel = "evidence" | "qwen" | null;

/** One foreground panel; selecting a different view retains its data in Home. */
export function useInspectionPanel() {
  const [inspectionPanel, setInspectionPanel] = useState<InspectionPanel>(null);
  const setRightOpen = useCallback((open: boolean) => {
    setInspectionPanel(current => open ? "evidence" : current === "evidence" ? null : current);
  }, []);
  const setQwenOpen = useCallback((open: boolean) => {
    setInspectionPanel(current => open ? "qwen" : current === "qwen" ? null : current);
  }, []);
  // A delayed hover can arrive after an explicit Qwen action. Never replace it.
  const previewEvidence = useCallback(() => setInspectionPanel(current => current ?? "evidence"), []);
  return { inspectionPanel, rightOpen: inspectionPanel === "evidence", qwenOpen: inspectionPanel === "qwen", setRightOpen, setQwenOpen, previewEvidence };
}

export function InspectionPanelSwitch({ active, onEvidence, onQwen, onClose }: {
  active: Exclude<InspectionPanel, null>;
  onEvidence: () => void;
  onQwen: () => void;
  onClose: () => void;
}) {
  return <nav className="inspection-panel-switch" aria-label="Map inspection views">
    <button type="button" aria-pressed={active === "evidence"} onClick={onEvidence}>Evidence</button>
    <button type="button" aria-pressed={active === "qwen"} onClick={onQwen}>Ask Qwen</button>
    <button className="inspection-close" type="button" onClick={onClose} aria-label={active === "qwen" ? "Close Qwen companion" : "Close Evidence Drawer"} title="Return to map">×</button>
  </nav>;
}
