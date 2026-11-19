export type CompactPanel = "tools" | "chat" | "evidence" | "left" | "time";
export type OpenCompactPanels = Readonly<Record<CompactPanel, boolean>>;

/** One work area owns the narrow layout. Foreground editing wins over the
 * fallback stacking order; a separate dialog or workspace retains ownership. */
export function compactPanelOwner(open: OpenCompactPanels, focused: CompactPanel | null, blocked: boolean): CompactPanel | null {
  if (blocked) return null;
  if (focused && open[focused]) return focused;
  return (["tools", "chat", "evidence", "left", "time"] as const).find(panel => open[panel]) ?? null;
}

/** Reveal the retained control using only scroll containers inside its panel. */
export function revealPanelControl(panel: HTMLElement, control: HTMLElement) {
  for (let node = control.parentElement; node && panel.contains(node); node = node.parentElement) {
    if (!/^(auto|scroll)$/.test(window.getComputedStyle(node).overflowY) || node.scrollHeight <= node.clientHeight) continue;
    const frame = node.getBoundingClientRect(), target = control.getBoundingClientRect();
    const top = frame.top + node.clientTop + 8, bottom = frame.top + node.clientTop + node.clientHeight - 8;
    const delta = target.height > bottom - top || target.top < top ? target.top - top : target.bottom > bottom ? target.bottom - bottom : 0;
    if (Math.abs(delta) > 1) node.scrollBy({ top: delta, behavior: "instant" });
  }
}
