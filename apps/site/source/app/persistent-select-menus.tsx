"use client";

import { useCallback, useEffect, useRef, useState } from "react";
import { createPortal } from "react-dom";

type MenuOption = { value: string; label: string; disabled: boolean; group: string | null };
type Menu = {
  select: HTMLSelectElement;
  options: MenuOption[];
  active: number;
  label: string;
  style: { top: number; left: number; width: number; maxHeight: number };
};

const MENU_ID = "site-persistent-select-menu";
const optionId = (index: number) => `${MENU_ID}-option-${index}`;

function menuPosition(select: HTMLSelectElement): Menu["style"] {
  const rect = select.getBoundingClientRect();
  const width = Math.min(window.innerWidth - 16, Math.max(rect.width, 220));
  const left = Math.max(8, Math.min(rect.left, window.innerWidth - width - 8));
  const below = window.innerHeight - rect.bottom - 12;
  const above = rect.top - 12;
  const placeAbove = below < 180 && above > below;
  const maxHeight = Math.max(80, Math.min(340, placeAbove ? above : below));
  const top = placeAbove ? Math.max(8, rect.top - maxHeight - 4) : rect.bottom + 4;
  return { top, left, width, maxHeight };
}

function readOptions(select: HTMLSelectElement): MenuOption[] {
  return Array.from(select.options, option => {
    const parent = option.parentElement;
    const group = parent instanceof HTMLOptGroupElement ? parent : null;
    return {
      value: option.value,
      label: option.label,
      disabled: option.disabled || !!group?.disabled,
      group: group?.label ?? null,
    };
  });
}

function nextEnabled(options: readonly MenuOption[], start: number, step: number): number {
  if (!options.length) return -1;
  for (let count = 0; count < options.length; count += 1) {
    const index = (start + step * count + options.length * 2) % options.length;
    if (!options[index].disabled) return index;
  }
  return -1;
}

/** Gives every native select a click-persistent option panel while retaining its form value. */
export function PersistentSelectMenus() {
  const [menu, setMenu] = useState<Menu | null>(null);
  const menuRef = useRef<Menu | null>(null);
  const panelRef = useRef<HTMLDivElement | null>(null);

  const update = useCallback((next: Menu | null) => {
    const previous = menuRef.current?.select;
    if (previous && previous !== next?.select) {
      previous.removeAttribute("aria-controls");
      previous.removeAttribute("aria-activedescendant");
      previous.setAttribute("aria-expanded", "false");
    }
    menuRef.current = next;
    if (next) {
      next.select.setAttribute("aria-controls", MENU_ID);
      next.select.setAttribute("aria-expanded", "true");
      next.select.setAttribute("aria-activedescendant", optionId(next.active));
    }
    setMenu(next);
  }, []);

  const choose = useCallback((current: Menu, index: number) => {
    const option = current.options[index];
    if (!option || option.disabled || !current.select.isConnected) return;
    update(null);
    const setter = Object.getOwnPropertyDescriptor(HTMLSelectElement.prototype, "value")?.set;
    setter?.call(current.select, option.value);
    current.select.dispatchEvent(new Event("input", { bubbles: true }));
    current.select.dispatchEvent(new Event("change", { bubbles: true }));
    current.select.focus({ preventScroll: true });
  }, [update]);

  useEffect(() => {
    let suppressClick: { select: HTMLSelectElement; at: number } | null = null;
    const eligible = (target: EventTarget | null): HTMLSelectElement | null => {
      if (!(target instanceof Element)) return null;
      const select = target.closest("select");
      return select instanceof HTMLSelectElement && !select.disabled && !select.multiple && select.size <= 1 && select.getClientRects().length > 0 ? select : null;
    };
    const open = (select: HTMLSelectElement) => {
      if (menuRef.current?.select === select) { update(null); return; }
      const options = readOptions(select);
      if (!options.length) return;
      const active = options[select.selectedIndex]?.disabled
        ? nextEnabled(options, select.selectedIndex + 1, 1)
        : Math.max(0, select.selectedIndex);
      const label = select.getAttribute("aria-label")
        || Array.from(select.labels ?? []).map(item => item.textContent?.trim()).filter(Boolean).join(" ")
        || "Choose an option";
      select.focus({ preventScroll: true });
      update({ select, options, active, label, style: menuPosition(select) });
    };
    const onPointerDown = (event: PointerEvent) => {
      if (panelRef.current?.contains(event.target as Node)) return;
      const select = eligible(event.target);
      if (!select) { if (menuRef.current) update(null); return; }
      event.preventDefault();
      suppressClick = { select, at: Date.now() };
      open(select);
    };
    const onMouseDown = (event: MouseEvent) => {
      if (eligible(event.target)) event.preventDefault();
    };
    const onClick = (event: MouseEvent) => {
      const select = eligible(event.target);
      if (!select) return;
      event.preventDefault();
      if (suppressClick?.select === select && Date.now() - suppressClick.at < 1500) { suppressClick = null; return; }
      suppressClick = null;
      open(select);
    };
    const onKeyDown = (event: KeyboardEvent) => {
      const current = menuRef.current;
      const select = eligible(event.target);
      if (!select) return;
      if (!current || current.select !== select) {
        if (event.key === "Enter" || event.key === " " || (event.altKey && event.key === "ArrowDown")) {
          event.preventDefault();
          open(select);
        }
        return;
      }
      if (event.key === "Escape") { event.preventDefault(); update(null); return; }
      if (event.key === "Tab") { update(null); return; }
      if (event.key === "Enter" || event.key === " ") {
        event.preventDefault();
        choose(current, current.active);
        return;
      }
      const step = event.key === "ArrowDown" ? 1 : event.key === "ArrowUp" ? -1 : 0;
      if (step || event.key === "Home" || event.key === "End") {
        event.preventDefault();
        const start = event.key === "Home" ? 0 : event.key === "End" ? current.options.length - 1 : current.active + step;
        const active = nextEnabled(current.options, start, step || (event.key === "Home" ? 1 : -1));
        if (active >= 0) update({ ...current, active });
      }
    };
    const reposition = (event?: Event) => {
      if (event?.target instanceof Node && panelRef.current?.contains(event.target)) return;
      const current = menuRef.current;
      if (!current) return;
      if (!current.select.isConnected || !current.select.getClientRects().length) { update(null); return; }
      update({ ...current, style: menuPosition(current.select) });
    };
    document.addEventListener("pointerdown", onPointerDown, true);
    document.addEventListener("mousedown", onMouseDown, true);
    document.addEventListener("click", onClick, true);
    document.addEventListener("keydown", onKeyDown, true);
    document.addEventListener("scroll", reposition, true);
    window.addEventListener("resize", reposition);
    return () => {
      document.removeEventListener("pointerdown", onPointerDown, true);
      document.removeEventListener("mousedown", onMouseDown, true);
      document.removeEventListener("click", onClick, true);
      document.removeEventListener("keydown", onKeyDown, true);
      document.removeEventListener("scroll", reposition, true);
      window.removeEventListener("resize", reposition);
    };
  }, [choose, update]);

  useEffect(() => {
    if (menu && menu.active >= 0) {
      panelRef.current?.querySelector<HTMLElement>(`#${optionId(menu.active)}`)?.scrollIntoView({ block: "nearest" });
    }
  }, [menu]);

  if (!menu) return null;
  return createPortal(<div
    ref={panelRef}
    id={MENU_ID}
    className="site-persistent-select-menu"
    role="listbox"
    aria-label={menu.label}
    style={menu.style}
  >{menu.options.map((option, index) => <div key={`${index}-${option.value}`}>
    {option.group && (index === 0 || menu.options[index - 1].group !== option.group) && <div className="site-persistent-select-group">{option.group}</div>}
    <button
      id={optionId(index)}
      type="button"
      role="option"
      aria-selected={menu.select.value === option.value}
      data-active={index === menu.active}
      disabled={option.disabled}
      onPointerEnter={() => { if (index !== menuRef.current?.active) update({ ...menu, active: index }); }}
      onClick={() => choose(menu, index)}
    >{option.label}</button>
  </div>)}</div>, document.body);
}
