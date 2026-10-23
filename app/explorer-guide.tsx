"use client";

import LivingWelcome from "./living-welcome/welcome.jsx";

// One welcome surface. Its WebGL engine still loads separately after paint.
// The v1 checkbox was preselected, so closing that guide did not establish an
// explicit opt-out. Leave it intact and require an explicit v2 preference.
export const EXPLORER_GUIDE_STORAGE_KEY = "kfm.explorer.guide.dismissed.v2";

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

export function ExplorerGuide({ open, ...props }: Readonly<{
  open: boolean;
  motionEnabled?: boolean;
  onMotionChange?: (enabled: boolean) => void;
  onSearch: (query: string) => void;
  onTopic: (topic: import("./layer-workspaces").LayerWorkspace) => void;
  onClose: (rememberDismissal: boolean) => void;
  onAction: (action: ExplorerGuideAction) => void;
  onMore?: () => void;
}>) {
  return open ? <LivingWelcome {...props} onMore={props.onMore} onMotionChange={props.onMotionChange} initialRemember={readExplorerGuideDismissed()} /> : null;
}
