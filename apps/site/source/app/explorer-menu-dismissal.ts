/** Dismiss native menus from a definite outside interaction. Safari can blur a
 * summary without focusing the tapped button, so blur/relatedTarget cannot
 * safely decide whether a menu action has been abandoned. */
export function installExplorerMenuDismissal(header: HTMLElement) {
  const document = header.ownerDocument;
  const dismissOutside = (event: Event) => {
    for (const menu of header.querySelectorAll<HTMLDetailsElement>("details.map-dock-menu[open], details.header-overflow-menu[open]")) {
      if (!menu.contains(event.target as Node | null)) menu.open = false;
    }
  };
  document.addEventListener("pointerdown", dismissOutside, true);
  document.addEventListener("focusin", dismissOutside);
  return () => {
    document.removeEventListener("pointerdown", dismissOutside, true);
    document.removeEventListener("focusin", dismissOutside);
  };
}
