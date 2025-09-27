// web/components/sidebar.js
// Kansas-Frontier-Matrix — Sidebar Component (upgraded)
// ----------------------------------------------------
// Works with web/css/map.css (.kfm-sidebar). No framework needed.
//
// Usage in app.js:
//   import Sidebar from "./components/sidebar.js";
//   const sidebar = new Sidebar({ title: cfg.title, subtitle: cfg.subtitle }).mount();
//   sidebar.setTimeContent(/* node */);
//   const grp = sidebar.addGroup("Historical Maps");
//   const row = grp.addLayerRow({ id:"usgs_topo_1894", title:"USGS Topo (1894)", badge:"[1894]",
//                                checked:true, opacity:0.85,
//                                onToggle:(v)=>KFM.setVisible("usgs_topo_1894", v),
//                                onOpacity:(a)=>KFM.setOpacity("usgs_topo_1894", a) });
//   // Later updates:
//   row.setBadge("[1894–1915]").setOpacity(0.7).focus();
//
// Emits events on Sidebar instance:
//   'openchange'  detail: { groupTitle, open }
//   'rowtoggle'   detail: { id, checked }
//   'rowopacity'  detail: { id, opacity }

export default class Sidebar extends EventTarget {
  /**
   * @param {Object} opts
   * @param {string} [opts.title]
   * @param {string} [opts.subtitle]
   * @param {string|HTMLElement} [opts.container]  selector or element (defaults to document.body)
   * @param {boolean} [opts.replaceExisting=false] replace existing #sidebar content if found
   * @param {boolean} [opts.persistOpen=true]      persist <details> open/closed state
   * @param {string}  [opts.persistKey="kfm_sidebar_groups"]
   * @param {string}  [opts.ariaLabel="Sidebar panel"]
   */
  constructor(opts = {}) {
    super();
    this.title = opts.title ?? "Kansas-Frontier-Matrix";
    this.subtitle = opts.subtitle ?? "";
    this.container = typeof opts.container === "string"
      ? document.querySelector(opts.container)
      : (opts.container || document.body);
    this.replaceExisting = !!opts.replaceExisting;
    this.persistOpen = opts.persistOpen !== false;
    this.persistKey = opts.persistKey || "kfm_sidebar_groups";
    this.ariaLabel = opts.ariaLabel || "Sidebar panel";

    this.root = null;
    this.header = null;
    this.timebox = null;
    this.layerbox = null;

    this.groups = [];
    this._rowIndex = new Map(); // layerId -> RowAPI
    this._bound = { onSummaryToggle: (e) => this._onSummaryToggle(e) };
  }

  // ---------------------------------------------------------------------------
  // Mount / DOM skeleton
  // ---------------------------------------------------------------------------
  mount() {
    const existing = document.getElementById("sidebar");
    if (existing && !this.replaceExisting) {
      // Wire existing structure if present
      this.root = existing;
      this.header = existing.querySelector(".kfm-sidebar-header") || existing.firstElementChild;
      this.timebox = existing.querySelector("#timebox") || existing.children?.[1];
      this.layerbox = existing.querySelector("#layerbox") || existing.children?.[2];

      // Ensure required attributes
      this.root.classList.add("kfm-sidebar");
      this.root.setAttribute("role", "region");
      this.root.setAttribute("aria-label", this.ariaLabel);
      return this._ensureHeader()._ensureSlots();
    }

    // Build fresh skeleton
    this.root = Sidebar.el("div", {
      id: "sidebar",
      class: "kfm-sidebar",
      role: "region",
      "aria-label": this.ariaLabel
    }, [
      (this.header = Sidebar.el("div", { class: "kfm-sidebar-header", style: {
        padding: "12px 12px 6px 12px",
        borderBottom: "1px solid var(--kfm-border, #e5e7eb)"
      } }, [
        Sidebar.el("h2", { style: { margin: "0 0 8px 0", fontSize: "16px", fontWeight: "700" } }, [this.title]),
        Sidebar.el("div", { class: "kfm-sidebar-sub", style: { fontSize: "12px", color: "var(--kfm-fg-muted, #666)" } }, [this.subtitle])
      ])),
      (this.timebox = Sidebar.el("div", { id: "timebox", style: {
        padding: "12px",
        borderBottom: "1px solid var(--kfm-border, #e5e7eb)"
      }})),
      (this.layerbox = Sidebar.el("div", { id: "layerbox", style: { padding: "12px" } }))
    ]);

    this.container.appendChild(this.root);
    return this;
  }

  _ensureHeader() {
    if (!this.header) {
      this.header = Sidebar.el("div", { class: "kfm-sidebar-header" }, [
        Sidebar.el("h2", {}, [this.title]),
        Sidebar.el("div", { class: "kfm-sidebar-sub" }, [this.subtitle])
      ]);
      this.root.insertBefore(this.header, this.root.firstChild);
    } else {
      const h2 = this.header.querySelector("h2") || Sidebar.el("h2");
      h2.textContent = this.title;
      if (!h2.parentNode) this.header.appendChild(h2);
      let sub = this.header.querySelector(".kfm-sidebar-sub");
      if (!sub) { sub = Sidebar.el("div", { class: "kfm-sidebar-sub" }); this.header.appendChild(sub); }
      sub.textContent = this.subtitle;
    }
    return this;
  }

  _ensureSlots() {
    if (!this.timebox) {
      this.timebox = Sidebar.el("div", { id: "timebox", style: { padding: "12px", borderBottom: "1px solid var(--kfm-border, #e5e7eb)" } });
      this.root.appendChild(this.timebox);
    }
    if (!this.layerbox) {
      this.layerbox = Sidebar.el("div", { id: "layerbox", style: { padding: "12px" } });
      this.root.appendChild(this.layerbox);
    }
    return this;
  }

  // ---------------------------------------------------------------------------
  // Content slots
  // ---------------------------------------------------------------------------
  setHeader({ title, subtitle } = {}) {
    if (title != null) {
      const h2 = this.header.querySelector("h2") || Sidebar.el("h2");
      h2.textContent = title;
      if (!h2.parentNode) this.header.prepend(h2);
      this.title = title;
    }
    if (subtitle != null) {
      let sub = this.header.querySelector(".kfm-sidebar-sub");
      if (!sub) { sub = Sidebar.el("div", { class: "kfm-sidebar-sub" }); this.header.appendChild(sub); }
      sub.textContent = subtitle;
      this.subtitle = subtitle;
    }
    return this;
  }

  /** Replace the timebox content with a node/element/string */
  setTimeContent(node) { Sidebar.replaceChildren(this.timebox, node); return this; }
  /** Replace the entire layers area with a node/element/string */
  setLayerContent(node) { Sidebar.replaceChildren(this.layerbox, node); return this; }

  // ---------------------------------------------------------------------------
  // Groups & rows (helpers)
  // ---------------------------------------------------------------------------
  /**
   * Add a <details> group into the layers area.
   * @param {string} title
   * @param {boolean} [open=true]
   * @param {string} [id] optional key for persistence (defaults to title)
   * @returns {SidebarGroup}
   */
  addGroup(title, open = true, id) {
    const key = id || title || `group-${this.groups.length + 1}`;
    const persisted = this._readPersist(key);
    const isOpen = this.persistOpen ? (persisted ?? open) : open;

    const det = Sidebar.el("details", { open: isOpen, "data-key": key, style: { marginBottom: "10px" } });
    const sum = Sidebar.el("summary", {
      style: { cursor: "pointer", fontWeight: "600", marginBottom: "6px" },
      onclick: (e) => { /* allow native toggle; handled in toggle listener */ }
    }, [title]);

    det.appendChild(sum);
    det.addEventListener("toggle", this._bound.onSummaryToggle);
    this.layerbox.appendChild(det);

    const group = new SidebarGroup(det, (ev) => this._emit("openchange", { groupTitle: title, open: det.open }), (k, v) => this._writePersist(key, v));
    this.groups.push(group);
    return group;
  }

  /** Convenience to clear all groups/rows */
  clearGroups() {
    Sidebar.replaceChildren(this.layerbox, null);
    this.groups = [];
    this._rowIndex.clear();
    return this;
  }

  /** Retrieve a row API by layer id, if created via addLayerRow */
  getRow(id) { return this._rowIndex.get(id) || null; }

  // ---------------------------------------------------------------------------
  // Persistence helpers
  // ---------------------------------------------------------------------------
  _readPersist(key) {
    if (!this.persistOpen) return null;
    try {
      const obj = JSON.parse(localStorage.getItem(this.persistKey) || "{}");
      if (Object.prototype.hasOwnProperty.call(obj, key)) return !!obj[key];
    } catch {}
    return null;
  }
  _writePersist(key, open) {
    if (!this.persistOpen) return;
    try {
      const obj = JSON.parse(localStorage.getItem(this.persistKey) || "{}");
      obj[key] = !!open;
      localStorage.setItem(this.persistKey, JSON.stringify(obj));
    } catch {}
  }

  _onSummaryToggle(e) {
    const details = e.currentTarget;
    const key = details.getAttribute("data-key") || "";
    if (key) this._writePersist(key, details.open);
    // Fire a single event upward (Sidebar instance)
    this._emit("openchange", { key, open: details.open });
  }

  // ---------------------------------------------------------------------------
  // Lifecyle
  // ---------------------------------------------------------------------------
  destroy() {
    // Remove listeners on all groups
    for (const g of this.groups) g._destroy();
    this.groups = [];
    this._rowIndex.clear();
    if (this.root?.parentNode) this.root.parentNode.removeChild(this.root);
    this.root = this.header = this.timebox = this.layerbox = null;
  }

  // ---------------------------------------------------------------------------
  // Event dispatch
  // ---------------------------------------------------------------------------
  _emit(type, detail) {
    try {
      this.dispatchEvent(new CustomEvent(type, { detail }));
    } catch {
      // IE11-ish fallback (unlikely, but harmless)
      const evt = document.createEvent("CustomEvent");
      evt.initCustomEvent(type, true, true, detail);
      this.dispatchEvent(evt);
    }
  }

  // ---------------------------------------------------------------------------
  // Static DOM helpers
  // ---------------------------------------------------------------------------
  static el(tag, attrs = {}, children = []) {
    const n = document.createElement(tag);
    for (const [k, v] of Object.entries(attrs)) {
      if (k === "class") n.className = v;
      else if (k === "style") Object.assign(n.style, v);
      else if (k.startsWith("on") && typeof v === "function") n.addEventListener(k.slice(2), v);
      else if (v != null) n.setAttribute(k, String(v));
    }
    const arr = Array.isArray(children) ? children : [children];
    for (const c of arr) {
      if (c == null || c === "") continue;
      n.appendChild(typeof c === "string" ? document.createTextNode(c) : c);
    }
    return n;
  }

  static replaceChildren(node, content) {
    if (!node) return;
    while (node.firstChild) node.removeChild(node.firstChild);
    if (content == null) return;
    if (typeof content === "string") node.appendChild(document.createTextNode(content));
    else if (content instanceof Node) node.appendChild(content);
    else if (Array.isArray(content)) content.forEach(c => Sidebar.replaceChildren(node, c));
  }
}

// ===========================================================================
// SidebarGroup — add layer rows with toggle + opacity, with a small RowAPI
// ===========================================================================
class SidebarGroup {
  constructor(rootDetails, onToggleOpen, persistWrite) {
    this.root = rootDetails;
    this.onToggleOpen = onToggleOpen;
    this.persistWrite = persistWrite;
    this._rows = [];
  }

  /**
   * Add a layer row with checkbox and opacity slider.
   * @param {Object} opts
   * @param {string}   opts.id           layer id (used for label/for)
   * @param {string}   opts.title        display name
   * @param {string}   [opts.badge]      small badge (e.g., "[1894–1915]")
   * @param {boolean}  [opts.checked=true]
   * @param {number}   [opts.opacity=1]  0..1
   * @param {Function} [opts.onToggle]   (checked:boolean) => void
   * @param {Function} [opts.onOpacity]  (value:number) => void
   * @param {HTMLElement} [opts.trailing] optional trailing node (e.g., mini tools)
   * @returns {RowAPI}
   */
  addLayerRow(opts) {
    const {
      id, title, badge, checked = true, opacity = 1,
      onToggle, onOpacity, trailing
    } = opts || {};

    const chkId = `chk_${id}`;
    const lblId = `lbl_${id}`;
    const row = Sidebar.el("div", {
      class: "kfm-layer-row",
      style: {
        display: "grid",
        gridTemplateColumns: trailing ? "24px 1fr 60px auto" : "24px 1fr 90px",
        gap: "6px",
        alignItems: "center",
        marginBottom: "8px"
      }
    });

    const checkbox = Sidebar.el("input", {
      id: chkId, type: "checkbox",
      checked: checked ? "checked" : null,
      role: "switch",
      "aria-checked": String(!!checked),
      onchange: (e) => {
        const val = !!e.target.checked;
        checkbox.setAttribute("aria-checked", String(val));
        onToggle && onToggle(val);
        this._emitRowEvent("rowtoggle", { id, checked: val });
      }
    });

    const label = Sidebar.el("label", {
      id: lblId, for: chkId,
      style: { fontSize: "13px", cursor: "pointer", display: "flex", alignItems: "baseline", gap: "6px" }
    }, [
      title || id,
      badge ? Sidebar.el("span", { class: "kfm-badge", style: { marginLeft: "2px" } }, [badge]) : ""
    ]);

    const slider = Sidebar.el("input", {
      type: "range", min: "0", max: "1", step: "0.05",
      value: String(Number.isFinite(opacity) ? opacity : 1),
      title: "Opacity",
      "aria-label": `Opacity for ${title || id}`,
      "aria-valuemin": "0",
      "aria-valuemax": "1",
      "aria-valuenow": String(Number.isFinite(opacity) ? opacity : 1),
      oninput: (e) => {
        const v = parseFloat(e.target.value);
        slider.setAttribute("aria-valuenow", String(v));
        onOpacity && onOpacity(v);
        this._emitRowEvent("rowopacity", { id, opacity: v });
      }
    });

    row.append(checkbox, label, slider);
    if (trailing) row.append(trailing);
    this.root.appendChild(row);

    // Build RowAPI for programmatic control
    const api = {
      id,
      el: row,
      checkbox,
      slider,
      setChecked: (val) => {
        const v = !!val;
        checkbox.checked = v;
        checkbox.setAttribute("aria-checked", String(v));
        onToggle && onToggle(v);
        this._emitRowEvent("rowtoggle", { id, checked: v });
        return api;
      },
      setOpacity: (v) => {
        const n = Math.max(0, Math.min(1, +v));
        slider.value = String(n);
        slider.setAttribute("aria-valuenow", String(n));
        onOpacity && onOpacity(n);
        this._emitRowEvent("rowopacity", { id, opacity: n });
        return api;
      },
      setBadge: (text) => {
        let badgeEl = label.querySelector(".kfm-badge");
        if (!text) {
          if (badgeEl) badgeEl.remove();
          return api;
        }
        if (!badgeEl) {
          badgeEl = Sidebar.el("span", { class: "kfm-badge", style: { marginLeft: "2px" } });
          label.appendChild(badgeEl);
        }
        badgeEl.textContent = text;
        return api;
      },
      setTitle: (text) => { label.childNodes[0].nodeValue = text || id; return api; },
      focus: () => { checkbox.focus(); return api; },
      remove: () => { row.remove(); return api; }
    };

    // Index for quick lookup
    try {
      const owner = this.root.closest("#sidebar")?._sidebarInstance;
      if (owner) owner._rowIndex.set(id, api);
    } catch {}
    this._rows.push(api);
    return api;
  }

  _emitRowEvent(type, detail) {
    const sidebar = this.root.closest("#sidebar")?._sidebarInstance;
    if (!sidebar) return;
    try { sidebar.dispatchEvent(new CustomEvent(type, { detail })); }
    catch {
      const evt = document.createEvent("CustomEvent"); evt.initCustomEvent(type, true, true, detail); sidebar.dispatchEvent(evt);
    }
  }

  _destroy() {
    this.root?.removeEventListener?.("toggle", this.onToggleOpen);
    this._rows.length = 0;
  }
}

// Attach a back-reference so group rows can dispatch on the Sidebar instance
Object.defineProperty(Sidebar.prototype, "_attachBackref", {
  value: function () { if (this.root) this.root._sidebarInstance = this; return this; },
  enumerable: false
});
const _origMount = Sidebar.prototype.mount;
Sidebar.prototype.mount = function patchedMount() { const out = _origMount.apply(this, arguments); this._attachBackref(); return out; };
