// A compact Layers dialog owns input until it closes. Restore the exact prior
// background state so held/hidden tools do not become active during cleanup.
export function isolateModalBackground(panel: HTMLElement, root: HTMLElement | null) {
  if (!root?.contains(panel)) return () => {};
  const prior: Array<{ element: HTMLElement; inert: boolean; ariaHidden: string | null }> = [];
  let branch: Element = panel;
  for (let parent = panel.parentElement; parent; parent = parent.parentElement) {
    for (const sibling of parent.children) {
      if (sibling === branch || !(sibling instanceof HTMLElement)) continue;
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

/** A panel returns focus to its opener on a later task. By then the visitor may have moved to
 * another control; that newer choice keeps focus. The return still runs when focus is where it
 * was at close, was dropped to the page, or is left inside the panel that just closed. */
export function focusReturnStillWanted(focusedAtClose: Element | null, active: Element | null, closedPanel: Element | null, page: Element | null): boolean {
  return !active || active === page || active === focusedAtClose || Boolean(closedPanel?.contains(active));
}
