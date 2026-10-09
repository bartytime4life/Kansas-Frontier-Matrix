/** Scroll the editable cap and its action into the unobscured part of the page. */
export function transferFocusDelta(field: { top: number; bottom: number }, action: { top: number; bottom: number } | null, visible: { top: number; bottom: number }) {
  const space = Math.max(0, visible.bottom - visible.top);
  if (!space) return 0;
  const fieldHeight = Math.max(0, field.bottom - field.top);
  const groupBottom = Math.max(field.bottom, action?.bottom ?? field.bottom);
  const groupHeight = groupBottom - field.top;
  // With a small keyboard viewport, keeping the focused field visible wins.
  const height = groupHeight <= space ? groupHeight : Math.min(fieldHeight, space);
  return field.top - (visible.top + (space - height) / 2);
}

export function revealTransferControls(field: HTMLElement, action: HTMLElement | null) {
  const scroller = field.closest<HTMLElement>("[data-download-scroll]");
  if (!scroller) { field.scrollIntoView({ block: "center", behavior: "instant" }); return; }
  const viewport = window.visualViewport, frame = scroller.getBoundingClientRect();
  const top = Math.max(frame.top, viewport?.offsetTop ?? 0) + 16;
  let bottom = Math.min(frame.bottom, (viewport?.offsetTop ?? 0) + (viewport?.height ?? window.innerHeight)) - 16;
  const strip = scroller.querySelector<HTMLElement>("[data-transfer-panel]");
  if (strip && window.getComputedStyle(strip).position === "fixed") {
    const overlay = strip.getBoundingClientRect();
    if (overlay.bottom > top && overlay.top < bottom) bottom = Math.min(bottom, overlay.top - 16);
  }
  const delta = transferFocusDelta(field.getBoundingClientRect(), action?.getBoundingClientRect() ?? null, { top, bottom });
  if (Math.abs(delta) > 1) scroller.scrollBy({ top: delta, behavior: "instant" });
}
