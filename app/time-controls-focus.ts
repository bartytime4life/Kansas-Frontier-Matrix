/** Keep keyboard context when a container query replaces a time control.
 * Pointer actions and deliberate focus changes always take precedence. */
export function retainTimeControlFocus(root: HTMLElement) {
  const usable = (node: HTMLElement | null) => Boolean(node?.isConnected
    && !node.closest('[hidden], [inert], [aria-hidden="true"]') && !node.matches(":disabled")
    && node.getClientRects().length && window.getComputedStyle(node).visibility !== "hidden");
  let focused = root.contains(document.activeElement) ? document.activeElement as HTMLElement : null;
  let datePart = focused?.closest(".compact-time-date") ? focused : null;
  let frame: number | undefined, disposed = false;
  const remember = (event: FocusEvent) => {
    // CSS can blur a disappearing control to body without a user focus move.
    if (event.target === document.body && focused && !usable(focused)) return;
    focused = event.target instanceof HTMLElement && root.contains(event.target) ? event.target : null;
    if (!focused) datePart = null;
    else if (focused.closest(".compact-time-date")) datePart = focused;
  };
  const pointer = (event: PointerEvent) => {
    if (event.target instanceof Node && !focused?.contains(event.target)) { focused = null; datePart = null; }
  };
  const refresh = () => {
    if (frame !== undefined) window.cancelAnimationFrame(frame);
    frame = window.requestAnimationFrame(() => {
      frame = undefined;
      if (disposed || document.hidden || !focused?.isConnected || usable(focused) || !usable(root)) return;
      const active = document.activeElement;
      if (active !== focused && active !== document.body && active !== document.documentElement) return;
      const counterpart = focused.closest(".compact-time-date") ? root.querySelector<HTMLElement>(".compact-time-date-mobile")
        : focused.matches(".compact-time-date-mobile") ? usable(datePart) ? datePart : root.querySelector<HTMLElement>(".compact-time-date select") : null;
      const target = [counterpart, root.querySelector<HTMLElement>(".compact-time-more"), root.querySelector<HTMLElement>(".compact-time-clock-toggle")].find(usable);
      target?.focus({ preventScroll: true });
    });
  };
  const observer = typeof ResizeObserver === "undefined" ? null : new ResizeObserver(refresh);
  observer?.observe(root.closest(".timeline-panel") ?? root);
  document.addEventListener("focusin", remember, true);
  document.addEventListener("pointerdown", pointer, true);
  window.addEventListener("resize", refresh);
  return () => {
    disposed = true;
    observer?.disconnect();
    document.removeEventListener("focusin", remember, true);
    document.removeEventListener("pointerdown", pointer, true);
    window.removeEventListener("resize", refresh);
    if (frame !== undefined) window.cancelAnimationFrame(frame);
  };
}
