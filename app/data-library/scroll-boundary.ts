/**
 * Keep the bounded collection list native until it reaches an edge. Some
 * browsers latch input to that list even when the surrounding page can scroll.
 * Relay only that otherwise-unconsumed vertical input to this page's scroller.
 */
export function bindCollectionScrollBoundary(list: HTMLElement, page: HTMLElement) {
  let touch: { id: number; x: number; y: number; startX: number; startY: number; axis: "horizontal" | "vertical" | null } | null = null;
  const maximum = (node: HTMLElement) => Math.max(0, node.scrollHeight - node.clientHeight);

  function relay(delta: number, event: WheelEvent | TouchEvent) {
    if (!event.cancelable || event.defaultPrevented || !Number.isFinite(delta) || delta === 0) return;
    const listMax = maximum(list);
    // Fractional scrollTop and integer clientHeight can disagree by a fraction
    // of a CSS pixel. A list with no scroll range needs no special handoff.
    if (listMax <= 1 || (delta > 0 ? list.scrollTop < listMax - 1 : list.scrollTop > 1)) return;
    const before = page.scrollTop;
    const target = Math.max(0, Math.min(maximum(page), before + delta));
    if (target === before) return;
    page.scrollTop = target;
    // A disabled/detached scroller may refuse the write. Do not cancel native
    // input unless this exact page actually consumed it in the requested direction.
    if ((page.scrollTop - before) * Math.sign(delta) > 0) event.preventDefault();
  }

  function wheel(event: WheelEvent) {
    if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey || event.deltaX !== 0) return;
    let delta = event.deltaY;
    if (event.deltaMode === 1) {
      const lineHeight = Number.parseFloat(list.ownerDocument.defaultView?.getComputedStyle(list).lineHeight || "");
      delta *= Number.isFinite(lineHeight) && lineHeight > 0 ? lineHeight : 16;
    } else if (event.deltaMode === 2) delta *= page.clientHeight;
    else if (event.deltaMode !== 0) return;
    relay(delta, event);
  }

  function start(event: TouchEvent) {
    touch = null;
    if (event.defaultPrevented || event.ctrlKey || event.metaKey || event.shiftKey || event.altKey || event.touches.length !== 1) return;
    const point = event.touches[0];
    touch = { id: point.identifier, x: point.clientX, y: point.clientY, startX: point.clientX, startY: point.clientY, axis: null };
  }
  function move(event: TouchEvent) {
    if (!touch || event.defaultPrevented || event.ctrlKey || event.metaKey || event.shiftKey || event.altKey || event.touches.length !== 1) { touch = null; return; }
    const point = event.touches[0];
    if (point.identifier !== touch.id) { touch = null; return; }
    const deltaX = point.clientX - touch.x;
    const deltaY = touch.y - point.clientY;
    const totalX = point.clientX - touch.startX, totalY = touch.startY - point.clientY;
    touch = { ...touch, x: point.clientX, y: point.clientY };
    if (!touch.axis) {
      if (Math.max(Math.abs(totalX), Math.abs(totalY)) < 4) return;
      touch.axis = Math.abs(totalX) >= Math.abs(totalY) ? "horizontal" : "vertical";
    }
    if (touch.axis !== "vertical" || Math.abs(deltaX) >= Math.abs(deltaY)) return;
    relay(deltaY, event);
  }
  function end() { touch = null; }

  list.addEventListener("wheel", wheel, { passive: false });
  list.addEventListener("touchstart", start, { passive: true });
  list.addEventListener("touchmove", move, { passive: false });
  list.addEventListener("touchend", end, { passive: true });
  list.addEventListener("touchcancel", end, { passive: true });
  return () => {
    touch = null;
    list.removeEventListener("wheel", wheel);
    list.removeEventListener("touchstart", start);
    list.removeEventListener("touchmove", move);
    list.removeEventListener("touchend", end);
    list.removeEventListener("touchcancel", end);
  };
}
