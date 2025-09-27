// web/components/legend-control.js
// Minimal MapLibre legend control with a live Year badge (upgraded).
// Still exposes window.LegendControl + window.wireTimelineToLegend for app.js wiring.

(function (global) {
  class LegendControl {
    /**
     * @param {Object} opts
     * @param {string}  [opts.position="top-right"]
     * @param {string}  [opts.title="Legend"]
     * @param {number}  [opts.year]
     * @param {boolean} [opts.collapsible=true]
     * @param {boolean} [opts.showYear=true]
     * @param {string}  [opts.persistKey="kfm_legend_collapsed"]  // localStorage key
     */
    constructor(opts = {}) {
      this._map = null;
      this._container = null;
      this._body = null;
      this._badge = null;

      this._pos = opts.position || "top-right";
      this._title = opts.title || "Legend";
      this._year = opts.year ?? null;

      this._collapsible = opts.collapsible !== false;
      this._showYear = opts.showYear !== false;
      this._persistKey = opts.persistKey || "kfm_legend_collapsed";

      this._onHeaderClick = () => this._toggleCollapse();
    }

    getDefaultPosition() { return this._pos; }

    onAdd(map) {
      this._map = map;

      const root = document.createElement("div");
      root.className = "kfm-legend maplibregl-ctrl";
      root.setAttribute("role", "region");
      root.setAttribute("aria-label", this._title);

      // Header (collapsible)
      const header = document.createElement("div");
      header.className = "kfm-legend-header";
      header.textContent = this._title;
      if (this._collapsible) header.addEventListener("click", this._onHeaderClick);

      // Year row
      const yr = document.createElement("div");
      yr.className = "kfm-legend-year";
      if (!this._showYear) yr.style.display = "none";
      yr.append("Year: ");
      const badge = document.createElement("span");
      badge.className = "kfm-year-badge";
      badge.textContent = this._year == null ? "—" : String(this._year);
      yr.append(badge);
      this._badge = badge;

      // Body
      const body = document.createElement("div");
      body.className = "kfm-legend-body";
      this._body = body;

      root.append(header, yr, body);
      this._container = root;

      // restore collapsed state
      if (this._readPersist()) this._container.classList.add("collapsed");

      return root;
    }

    onRemove() {
      if (this._container) {
        const header = this._container.querySelector(".kfm-legend-header");
        if (header && this._collapsible) header.removeEventListener("click", this._onHeaderClick);
        if (this._container.parentNode) this._container.parentNode.removeChild(this._container);
      }
      this._map = null;
      this._container = this._body = this._badge = null;
    }

    // ---------------- Public API ----------------
    setYear(y) {
      this._year = y;
      if (this._badge) this._badge.textContent = y == null ? "—" : String(y);
      return this;
    }

    setTitle(text) {
      this._title = String(text ?? "Legend");
      const header = this._container?.querySelector(".kfm-legend-header");
      if (header) header.textContent = this._title;
      if (this._container) this._container.setAttribute("aria-label", this._title);
      return this;
    }

    setCollapsed(collapsed) {
      if (!this._container) return this;
      this._container.classList.toggle("collapsed", !!collapsed);
      this._writePersist(!!collapsed);
      return this;
    }

    isCollapsed() { return this._container?.classList.contains("collapsed") || false; }

    clear() {
      if (this._body) this._body.innerHTML = "";
      return this;
    }

    /**
     * Replace legend body with a custom node/HTML string.
     */
    setBody(node) {
      if (!this._body) return this;
      this._body.innerHTML = "";
      if (node == null) return this;
      if (typeof node === "string") {
        this._body.innerHTML = node;
      } else if (node instanceof Node) {
        this._body.appendChild(node);
      } else if (Array.isArray(node)) {
        node.forEach(n => this.setBody(n)); // recursive
      }
      return this;
    }

    /**
     * Create a section wrapper and append it to body.
     * @param {string} title
     * @returns {HTMLElement} section element
     */
    addSection(title) {
      if (!this._body) return null;
      const section = document.createElement("div");
      section.className = "kfm-legend-section";

      if (title) {
        const t = document.createElement("div");
        t.className = "kfm-legend-title";
        t.textContent = title;
        section.appendChild(t);
      }

      this._body.appendChild(section);
      return section;
    }

    /**
     * Add a legend row to a given section.
     * @param {HTMLElement} section
     * @param {Object} item
     *   - color:       fill color
     *   - lineColor:   stroke color
     *   - lineWidth:   px
     *   - pointColor:  point fill
     *   - pointRadius: px
     *   - gradient:    array of colors (for ramps)
     *   - label:       string
     */
    addRow(section, item = {}) {
      if (!section) return null;
      const row = document.createElement("div");
      row.className = "kfm-legend-row";

      const sw = document.createElement("span");
      sw.className = "kfm-legend-swatch";

      // Choose swatch style
      if (Array.isArray(item.gradient) && item.gradient.length) {
        const stops = item.gradient.slice(0, 8).join(",");
        sw.style.background = `linear-gradient(90deg, ${stops})`;
      } else if (item.lineColor || item.lineWidth) {
        sw.style.width = "24px";
        sw.style.height = "0";
        sw.style.borderTop = `${Math.max(2, item.lineWidth || 2)}px solid ${item.lineColor || "#666"}`;
      } else if (item.pointColor || item.pointRadius) {
        const r = Math.max(6, item.pointRadius || 6);
        sw.style.width = `${r}px`;
        sw.style.height = `${r}px`;
        sw.style.borderRadius = "999px";
        sw.style.background = item.pointColor || "#666";
      } else {
        sw.style.background = item.color || "#ccc";
      }

      const lab = document.createElement("span");
      lab.className = "kfm-legend-label";
      lab.textContent = item.label || "";

      row.append(sw, lab);
      section.appendChild(row);
      return row;
    }

    getContainer() { return this._container; }
    destroy() { this.onRemove(); }

    // ---------------- Internals ----------------
    _toggleCollapse() {
      if (!this._collapsible) return;
      const collapsed = this._container.classList.toggle("collapsed");
      this._writePersist(collapsed);
      try {
        this._container.dispatchEvent(new CustomEvent("toggle", { detail: { collapsed } }));
      } catch {}
    }

    _readPersist() {
      try { return localStorage.getItem(this._persistKey) === "1"; } catch { return false; }
    }
    _writePersist(v) {
      try { localStorage.setItem(this._persistKey, v ? "1" : "0"); } catch {}
    }
  }

  // Helper to wire a Timeline instance to this control (unchanged API)
  function wireTimelineToLegend(timeline, legendControl) {
    if (!timeline || !legendControl) return () => {};
    legendControl.setYear(timeline.getState().value);
    const onDom = (e) => legendControl.setYear(e.detail?.value ?? timeline.getState().value);
    const cb = (y) => legendControl.setYear(y);
    timeline.addEventListener?.("change", onDom);
    timeline.onChange?.(cb);
    return () => {
      timeline.removeEventListener?.("change", onDom);
      timeline.offChange?.(cb);
    };
  }

  // Safe globals
  global.LegendControl = global.LegendControl || LegendControl;
  global.wireTimelineToLegend = global.wireTimelineToLegend || wireTimelineToLegend;
})(window);
