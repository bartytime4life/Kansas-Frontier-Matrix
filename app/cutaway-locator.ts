type LayoutMap = {
  getContainer(): Pick<HTMLElement, "clientWidth" | "clientHeight" | "closest">;
  getCanvas(): {style: Pick<CSSStyleDeclaration, "width" | "height">};
  resize(): unknown;
};

/** MapLibre emits movement even for a no-op resize. Preserve fixed selectors
 * and explicitly requested surface probes when a drawer leaves the size alone. */
export function resizeMapAfterLayout(map: LayoutMap, skipUnchanged = false) {
  const container = map.getContainer();
  if (skipUnchanged || container.closest(".map-stage")?.querySelector('[data-cutaway-panel="true"]')) {
    const canvas = map.getCanvas();
    // Match MapLibre's public canvas CSS size, including its hidden-container fallback.
    if (canvas.style.width === `${container.clientWidth || 400}px` && canvas.style.height === `${container.clientHeight || 300}px`) return false;
  }
  map.resize();
  return true;
}

/** Absolute children use scroll-content coordinates, while DOM rectangles use viewport coordinates. */
export function cutawayLocatorPlacement(slot: {left:number;top:number;width:number;height:number;bottom:number},
  stage: {left:number;top:number;scrollLeft:number;scrollTop:number}, clip: {top:number;bottom:number}) {
  return {
    left: slot.left - stage.left + stage.scrollLeft,
    top: slot.top - stage.top + stage.scrollTop,
    width: slot.width, height: slot.height,
    clipTop: Math.max(0, clip.top - slot.top), clipBottom: Math.max(0, slot.bottom - clip.bottom),
    visible: slot.bottom > clip.top && slot.top < clip.bottom,
  };
}
