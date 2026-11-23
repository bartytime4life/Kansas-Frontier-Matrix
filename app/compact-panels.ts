export type CompactPanel = "tools" | "chat" | "evidence" | "left" | "time";
export type OpenCompactPanels = Readonly<Record<CompactPanel, boolean>>;

/** One work area owns the narrow layout. Foreground editing wins over the
 * fallback stacking order; a separate dialog or workspace retains ownership. */
export function compactPanelOwner(open: OpenCompactPanels, focused: CompactPanel | null, blocked: boolean): CompactPanel | null {
  if (blocked) return null;
  if (focused && open[focused]) return focused;
  return (["tools", "chat", "evidence", "left", "time"] as const).find(panel => open[panel]) ?? null;
}

const minimumRevealInset = 8;

function scrollPaddingInset(padding: string, height: number) {
  const value = Number.parseFloat(padding);
  if (!Number.isFinite(value)) return minimumRevealInset;
  const pixels = padding.endsWith("%") ? height * value / 100 : value;
  return Math.max(minimumRevealInset, pixels);
}

/** Reveal a control inside its panel, optionally reserving the CSS inset for sticky headings. */
export function revealPanelControl(panel: HTMLElement, control: HTMLElement, { respectScrollPadding = false } = {}) {
  for (let node = control.parentElement; node && panel.contains(node); node = node.parentElement) {
    const style = window.getComputedStyle(node);
    if (!/^(auto|scroll)$/.test(style.overflowY) || node.scrollHeight <= node.clientHeight) continue;
    const frame = node.getBoundingClientRect(), target = control.getBoundingClientRect();
    const startInset = respectScrollPadding ? scrollPaddingInset(style.scrollPaddingTop, node.clientHeight) : minimumRevealInset;
    const endInset = respectScrollPadding ? scrollPaddingInset(style.scrollPaddingBottom, node.clientHeight) : minimumRevealInset;
    const top = frame.top + node.clientTop + startInset;
    const bottom = frame.top + node.clientTop + node.clientHeight - endInset;
    const delta = target.height > bottom - top || target.top < top ? target.top - top : target.bottom > bottom ? target.bottom - bottom : 0;
    if (Math.abs(delta) > 1) node.scrollBy({ top: delta, behavior: "instant" });
  }
}
