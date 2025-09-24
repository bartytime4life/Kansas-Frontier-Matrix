// web/components/sidebar.js
// Kansas-Frontier-Matrix — Sidebar Component
// ------------------------------------------
// A tiny, framework-free sidebar utility that creates a right-docked panel with
// a header, a time slot, and a layers slot. CSS hooks match `web/css/map.css`
// (.kfm-sidebar). You can supply your own content or use the helpers below.
//
// Typical usage (in app.js):
//
// import Sidebar from "./components/sidebar.js";
//
// const sidebar = new Sidebar({
//   title: cfg.title || "Kansas-Frontier-Matrix",
//   subtitle: cfg.subtitle || "Time-aware layers"
// }).mount(); // creates #sidebar if it doesn't exist
//
// // Fill timebox
// sidebar.setTimeContent(el("div", {}, ["Custom time UI here..."]));
//
// // Add a layer group with rows
// const group = sidebar.addGroup("Historical Maps");
// group.addLayerRow({
//   id: "usgs_topo_1894",
//   title: "USGS Topo (1894)",
//   badge: "[1894]",
//   checked: true,
//   opacity: 0.85,
//   onToggle: (checked) => KFM.setVisible("usgs_topo_1894", checked),
//   onOpacity: (v) => KFM.setOpacity("usgs_topo_1894", v)
// });

export default class Sidebar {
  /**
   * @param {Object} opts
   * @param {string} [opts.title]
   * @param {string} [opts.subtitle]
   * @param {string|HTMLElement} [opts.container] - selector or element (defaults to body)
   * @param {boolean} [opts.replaceExisting=false] - if true, clears any existing sidebar content
   */
  constructor(opts = {}) {
    this.title = opts.title ?? "Kansas-Frontier-Matrix";
    this.subtitle = opts.subtitle ?? "";
    this.container = typeof opts.container === "string"
      ? document.querySelector(opts.container)
      : (opts.container || document.body);
    this.replaceExisting = !!opts.replaceExisting;

    this.root = null;
    this.header = null;
    this.timebox = null;
    this.layerbox = null;
    this.groups = [];
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
      return this;
    }

    // Build fresh skeleton
    this.root = Sidebar.el("div", { id: "sidebar", class: "kfm-sidebar" }, [
      this.header = Sidebar.el("div", { class: "kfm-sidebar-header", style: { padding: "12px 12px 6px 12px", borderBottom: "1px solid var(--kfm-border, #eee)" } }, [
        Sidebar.el("h2", { style: { margin: "0 0 8px 0", fontSize: "16px", fontWeight: "700" } }, [this.title]),
        Sidebar.el("div", { style: { fontSize: "12px", color: "var(--kfm-fg-muted, #666)" } }, [this.subtitle])
      ]),
      this.timebox = Sidebar.el("div", { id: "timebox", style: { padding: "12px", borderBottom: "1px solid var(--kfm-border, #eee)" } }),
      this.layerbox = Sidebar.el("div", { id: "layerbox", style: { padding: "12px" } })
    ]);

    this.container.appendChild(this.root);
    return this;
  }

  // ---------------------------------------------------------------------------
  // Content slots
  // ---------------------------------------------------------------------------
  setHeader({ title, subtitle } = {}) {
    if (title != null) {
      const h2 = this.header.querySelector("h2");
      if (h2) h2.textContent = title;
    }
    if (subtitle != null) {
      const sub = this.header.querySelector("div");
      if (sub) sub.textContent = subtitle;
    }
    return this;
  }

  /** Replace the timebox content with a node/element/string */
  setTimeContent(node) {
    Sidebar.replaceChildren(this.timebox, node);
    return this;
  }

  /** Replace the entire layers area with a node/element/string */
  setLayerContent(node) {
    Sidebar.replaceChildren(this.layerbox, node);
    return this;
  }

  // ---------------------------------------------------------------------------
  // Groups & rows (helpers)
  // ---------------------------------------------------------------------------
  /**
   * Add a <details> group into the layers area.
   * @param {string} title
   * @param {boolean} [open=true]
   * @returns {SidebarGroup}
   */
  addGroup(title, open = true) {
    const det = Sidebar.el("details", { open, style: { marginBottom: "10px" } });
    const sum = Sidebar.el("summary", { style: { cursor: "pointer", fontWeight: "600", marginBottom: "6px" } }, [title]);
    det.appendChild(sum);
    this.layerbox.appendChild(det);

    const group = new SidebarGroup(det);
    this.groups.push(group);
    return group;
  }

  /** Convenience to clear all groups/rows */
  clearGroups() {
    Sidebar.replaceChildren(this.layerbox, null);
    this.groups = [];
    return this;
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
    for (const c of arr) n.appendChild(typeof c === "string" ? document.createTextNode(c) : c);
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
// SidebarGroup — a small helper to add layer rows with toggle + opacity
// ===========================================================================
class SidebarGroup {
  constructor(rootDetails) {
    this.root = rootDetails;
  }

  /**
   * Add a layer row with checkbox and opacity slider.
   * @param {Object} opts
   * @param {string} opts.id         - layer id (used for label/for)
   * @param {string} opts.title      - display name
   * @param {string} [opts.badge]    - small badge text (e.g., time span)
   * @param {boolean} [opts.checked=true]
   * @param {number} [opts.opacity=1]  - 0..1
   * @param {Function} [opts.onToggle]  - (checked:boolean) => void
   * @param {Function} [opts.onOpacity] - (value:number) => void
   */
  addLayerRow(opts) {
    const {
      id,
      title,
      badge,
      checked = true,
      opacity = 1,
      onToggle,
      onOpacity
    } = opts || {};

    const chkId = `chk_${id}`;
    const row = Sidebar.el("div", {
      style: {
        display: "grid",
        gridTemplateColumns: "24px 1fr 60px",
        gap: "6px",
        alignItems: "center",
        marginBottom: "6px"
      }
    }, [
      Sidebar.el("input", {
        id: chkId,
        type: "checkbox",
        checked: checked ? "checked" : null,
        onchange: (e) => onToggle && onToggle(!!e.target.checked)
      }),
      Sidebar.el("label", { for: chkId, style: { fontSize: "13px", cursor: "pointer" } }, [
        title || id,
        badge ? Sidebar.el("span", { style: { color: "var(--kfm-fg-muted, #999)", marginLeft: "6px", fontSize: "11px" } }, [badge]) : ""
      ]),
      Sidebar.el("input", {
        type: "range", min: "0", max: "1", step: "0.05", value: String(Number.isFinite(opacity) ? opacity : 1),
        oninput: (e) => onOpacity && onOpacity(parseFloat(e.target.value))
      })
    ]);

    this.root.appendChild(row);
    return row;
  }
}

