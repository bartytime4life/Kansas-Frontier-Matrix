"use client";

import LivingWelcome from "./living-welcome/welcome.jsx";

// One welcome surface. Its WebGL engine still loads separately after paint.
// The welcome is the site's landing page (owner decision, 2026-11-06): every
// arrival without a destination in the address opens it. The former
// "Don't show on start" opt-out is retired; this key is only ever cleared so a
// device that stored the old preference lands on the welcome again.
export const EXPLORER_GUIDE_STORAGE_KEY = "kfm.explorer.guide.dismissed.v2";

export type ExplorerGuideAction = "layers" | "time" | "underground" | "qwen";

/** No device preference hides the landing page. */
export function readExplorerGuideDismissed(): boolean {
  return false;
}

/** Closing the welcome is for this view only; any stored opt-out is removed. */
export function writeExplorerGuideDismissed(_dismissed: boolean): void {
  try {
    window.localStorage.removeItem(EXPLORER_GUIDE_STORAGE_KEY);
  } catch {
    // Device storage is optional; the guide still closes for this view.
  }
}

export function ExplorerGuide({ open, ...props }: Readonly<{
  open: boolean;
  motionEnabled?: boolean;
  onMotionChange?: (enabled: boolean) => void;
  onSearch: (query: string) => void;
  onTopic: (topic: import("./layer-workspaces").LayerWorkspace) => void;
  /** Open the category's own map look (basemap, scene, camera and starter layers). */
  initialTopics?: readonly import("./layer-workspaces").TopicId[];
  onMaps?: (topics: readonly import("./layer-workspaces").TopicId[]) => void;
  onMap?: (topic: import("./layer-workspaces").TopicId) => void;
  onClose: (rememberDismissal: boolean) => void;
  onAction: (action: ExplorerGuideAction) => void;
  onMore?: () => void;
  /** Reveal full provider attribution through the visible welcome controls. */
  onSources?: () => void;
}>) {
  return open ? <LivingWelcome {...props} onMap={props.onMap} onMore={props.onMore} onMotionChange={props.onMotionChange} initialRemember={readExplorerGuideDismissed()} /> : null;
}
