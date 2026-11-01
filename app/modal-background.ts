// A compact Layers dialog owns input until it closes. Restore the exact prior
// background state so held/hidden tools do not become active during cleanup.
export function isolateModalBackground(panel: HTMLElement, root: HTMLElement | null) {
  if (!root?.contains(panel)) return () => {};
  const prior: Array<{ element: HTMLElement; inert: boolean; ariaHidden: string | null }> = [];
  let branch: Element = panel;
  for (let parent = panel.parentElement; parent; parent = parent.parentElement) {
    for (const sibling of parent.children) {
      if (sibling === branch || !(sibling instanceof HTMLElement)) continue;
      // An existing owner already excludes this branch. Do not acquire a hold
      // or later restore its stale attributes over that owner's next render.
      if (sibling.inert && sibling.getAttribute("aria-hidden") === "true") continue;
      prior.push({ element: sibling, inert: sibling.inert, ariaHidden: sibling.getAttribute("aria-hidden") });
      sibling.inert = true;
      sibling.setAttribute("aria-hidden", "true");
    }
    if (parent === root) break;
    branch = parent;
  }
  return () => {
    for (const { element, inert, ariaHidden } of prior) {
      element.inert = inert;
      if (ariaHidden === null) element.removeAttribute("aria-hidden");
      else element.setAttribute("aria-hidden", ariaHidden);
    }
  };
}

export function modalReturnTarget(trigger: HTMLElement | null, fallback: HTMLElement | null): HTMLElement | null {
  if (!trigger?.isConnected) return fallback;
  let target = trigger;
  // Menu buttons can retain layout boxes after their disclosure closes.
  // Return to its visible summary instead of a hidden descendant.
  for (let parent = trigger.parentElement; parent; parent = parent.parentElement) {
    if (parent instanceof HTMLDetailsElement && !parent.open) {
      const summary = parent.querySelector<HTMLElement>(":scope > summary");
      if (summary) target = summary;
    }
  }
  return target.isConnected && !target.closest("[hidden], [inert]") && target.getClientRects().length > 0 ? target : fallback;
}

/** Native Tab candidates, including disclosure summaries but not closed content.
 * A layout box alone does not make a closed-details descendant focusable.
 * Do not require viewport intersection: focusing a scrolled control reveals it.
 */
export function modalFocusableElements(panel: HTMLElement): HTMLElement[] {
  const selector = "button, input, select, textarea, summary, a[href], [tabindex]";
  return Array.from(panel.querySelectorAll<HTMLElement>(selector)).filter(element => {
    if (element.tabIndex < 0 || element.matches(":disabled") || element.closest("[hidden], [inert]") || !element.getClientRects().length) return false;
    const style = element.ownerDocument.defaultView?.getComputedStyle(element);
    if (style?.display === "none" || style?.visibility === "hidden" || style?.visibility === "collapse") return false;
    for (let ancestor = element.parentElement; ancestor && panel.contains(ancestor); ancestor = ancestor.parentElement) {
      if (ancestor instanceof HTMLDetailsElement && !ancestor.open) {
        const summary = ancestor.querySelector(":scope > summary");
        if (summary !== element && !summary?.contains(element)) return false;
      }
    }
    return true;
  });
}
