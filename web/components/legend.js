// web/components/legend.js
// Kansas-Frontier-Matrix — Dynamic Legend Component (upgraded)

export default class LegendControl {
  /**
   * @param {Object} opts
   * @param {Array}  [opts.layersConfig=[]]  // same array passed into app.js
   * @param {String} [opts.title="Legend"]
   * @param {String} [opts.persistKey="kfm_legend_collapsed"]
   * @param {String} [opts.position="bottom-right"]
   * @param {Number} [opts.maxItemsPerLayer=12]
   * @param {Boolean}[opts.showYear=true]
   */
  constructor(opts = {}) {
    this._map = null;
    this._container = null;
    this._body = null;
    this._badge = null;

    this._layersConfig = Array.isArray(opts.layersConfig) ? opts.layersConfig : [];
    this._title = opts.title || "Legend";
    this._persistKey = opts.persistKey || "kfm_legend_collapsed";
    this._pos = opts.position || "bottom-right";
    this._maxItems = Number.isFinite(opts.maxItemsPerLayer) ? opts.maxItemsPerLayer : 12;
    this._showYear = opts.showYear !== false;

    this._onData = () => this.refresh();
    this._onStyleData = () => this.refresh();
  }

  getDefaultPosition() { return this._pos; }

  onAdd(map) {
    this._map = map;
    const root = document.createElement("div");
    root.className = "kfm-legend maplibregl-ctrl";
    root.setAttribute("role", "region");
    root.setAttribute("aria-label", this._title);

    // Header
    const header = document.createElement("div");
    header.className = "kfm-legend-header";
    header.textContent = this._title;
    header.addEventListener("click", () => this._toggle());

    // Year row
    const yrRow = document.createElement("div");
    yrRow.className = "kfm-legend-year";
    if (!this._showYear) yrRow.style.display = "none";
    yrRow.append("Year: ");
    this._badge = document.createElement("span");
    this._badge.className = "kfm-year-badge";
    this._badge.textContent = "—";
    yrRow.append(this._badge);

    // Body
    this._body = document.createElement("div");
    this._body.className = "kfm-legend-body";

    root.append(header, yrRow, this._body);
    this._container = root;

    // collapsed persistence
    if (this._readPersist()) this._container.classList.add("collapsed");

    // map events → refresh
    map.on("styledata", this._onStyleData);
    map.on("data", this._onData);

    this.refresh();
    return root;
  }

  onRemove() {
    if (!this._map) return;
    try { this._map.off("styledata", this._onStyleData); } catch {}
    try { this._map.off("data", this._onData); } catch {}
    this._map = null;
    if (this._container?.parentNode) this._container.parentNode.removeChild(this._container);
    this._container = this._body = this._badge = null;
  }

  // --- Public API -------------------------------------------------------------
  setYear(y) { if (this._badge) this._badge.textContent = (y == null ? "—" : String(y)); }
  setLayersConfig(cfg) { this._layersConfig = Array.isArray(cfg) ? cfg : []; this.refresh(); }
  getContainer() { return this._container; }
  destroy() { this.onRemove(); }

  refresh() {
    if (!this._body) return;
    this._body.innerHTML = "";

    // Group layers by category/group from config (fall back to “Layers”)
    const groupMap = new Map();
    for (const L of this._layersConfig) {
      const key = L.group || L.category || "Layers";
      if (!groupMap.has(key)) groupMap.set(key, []);
      groupMap.get(key).push(L);
    }

    // Build a section per group
    for (const [groupName, items] of groupMap.entries()) {
      const section = this._section(groupName);
      this._body.appendChild(section);

      for (const cfg of items) {
        // Hide legend rows for layers that aren't on the map (or permanently hidden)
        if (!this._isRenderable(cfg)) continue;

        const rows = this._legendRowsForLayer(cfg);
        if (!rows.length) continue;

        const block = document.createElement("div");
        block.className = "kfm-legend-section";
        const title = document.createElement("div");
        title.className = "kfm-legend-title";
        title.textContent = cfg.title || cfg.id;
        block.appendChild(title);

        for (const r of rows.slice(0, this._maxItems)) block.appendChild(r);

        // If too many categories, provide a hint
        if (rows.length > this._maxItems) {
          const more = document.createElement("div");
          more.className = "kfm-legend-label";
          more.textContent = `+${rows.length - this._maxItems} more…`;
          block.appendChild(more);
        }

        section.appendChild(block);
      }
    }
  }

  // --- Internals --------------------------------------------------------------
  _section(title) {
    const wrap = document.createElement("div");
    // (Optional wrapper if you want collapsible subgroups later)
    // For now we just return a simple div.
    return wrap;
  }

  _toggle() {
    const collapsed = this._container.classList.toggle("collapsed");
    this._writePersist(collapsed);
  }

  _readPersist() {
    try { return localStorage.getItem(this._persistKey) === "1"; } catch { return false; }
  }
  _writePersist(v) {
    try { localStorage.setItem(this._persistKey, v ? "1" : "0"); } catch {}
  }

  _isRenderable(cfg) {
    if (!cfg?.id) return false;
    // If map has the layer and it's visible, render; else if no map layer yet, fall back to config visibility
    const map = this._map;
    const id = cfg.id;
    if (map && map.getLayer(id)) {
      const vis = map.getLayoutProperty(id, "visibility") ?? "visible";
      return vis !== "none";
    }
    // For GeoJSON helpers, check their companions too
    if (map && (map.getLayer(id + "_line") || map.getLayer(id + "_circle"))) {
      const v1 = map.getLayer(id + "_line") ? (map.getLayoutProperty(id + "_line", "visibility") ?? "visible") : "none";
      const v2 = map.getLayer(id + "_circle") ? (map.getLayoutProperty(id + "_circle", "visibility") ?? "visible") : "none";
      return v1 !== "none" || v2 !== "none";
    }
    // Fallback to config flag (default true)
    return cfg.visible !== false;
  }

  _legendRowsForLayer(cfg) {
    // 1) If explicit legend is present, render that.
    if (Array.isArray(cfg.legend) && cfg.legend.length) {
      return cfg.legend.map((item) => this._rowFromLegendItem(item));
    }

    // 2) Otherwise try to auto-derive from live map style
    try {
      if (!this._map) return [];
      const id = cfg.id;
      const rows = [];

      // helpers
      const mkRow = (swatchEl, label) => {
        const row = document.createElement("div");
        row.className = "kfm-legend-row";
        swatchEl.classList.add("kfm-legend-swatch");
        const lab = document.createElement("span");
        lab.className = "kfm-legend-label";
        lab.textContent = label || "";
        row.append(swatchEl, lab);
        return row;
      };
      const colorOf = (prop, fallback) => {
        try {
          const paint = this._map.getPaintProperty(id, prop);
          if (typeof paint === "string" && paint.startsWith("#")) return paint;
          if (Array.isArray(paint) && typeof paint[0] === "string" && paint[0] === "interpolate") {
            // gradient → render a gradient swatch (raster/fill)
            return "__gradient__";
          }
          if (Array.isArray(paint) && typeof paint[0] === "string" && paint[0] === "case") {
            // categorical; we can't easily parse without source data → fallback
            return fallback;
          }
          if (typeof paint === "number") return fallback; // widths/opacity etc.
          return paint || fallback;
        } catch { return fallback; }
      };

      const type = this._map.getLayer(id)?.type || cfg.type;

      if (type === "line" || this._map.getLayer(id + "_line")) {
        const lid = this._map.getLayer(id + "_line") ? id + "_line" : id;
        const col = this._map.getPaintProperty(lid, "line-color") ?? "#666";
        const w = this._map.getPaintProperty(lid, "line-width") ?? 2;
        const sw = document.createElement("span");
        sw.style.width = "24px";
        sw.style.height = "0";
        sw.style.borderTop = `${Math.max(2, +w)}px solid ${typeof col === "string" ? col : "#666"}`;
        rows.push(mkRow(sw, cfg.title || cfg.id));
      }

      if (type === "fill" || this._map.getLayer(id)) {
        const col = colorOf("fill-color", "#888");
        if (col) {
          const sw = document.createElement("span");
          if (col === "__gradient__") {
            // attempt a generic gradient; exact stops not trivially readable here
            sw.style.background = "linear-gradient(90deg,#fff,#888,#000)";
          } else {
            sw.style.backgroundColor = col;
          }
          rows.push(mkRow(sw, (cfg.title || cfg.id)));
        }
      }

      if (type === "circle" || this._map.getLayer(id + "_circle")) {
        const cid = this._map.getLayer(id + "_circle") ? id + "_circle" : id;
        const col = this._map.getPaintProperty(cid, "circle-color") ?? "#666";
        const r = this._map.getPaintProperty(cid, "circle-radius") ?? 4;
        const sw = document.createElement("span");
        sw.style.width = `${Math.max(10, r * 2)}px`;
        sw.style.height = sw.style.width;
        sw.style.borderRadius = "999px";
        sw.style.backgroundColor = typeof col === "string" ? col : "#666";
        rows.push(mkRow(sw, cfg.title || cfg.id));
      }

      if (type === "raster" || cfg.type === "raster" || this._map.getLayer(id)) {
        // Try to detect raster opacity and render a gradient swatch as a hint
        const sw = document.createElement("span");
        sw.style.background = "linear-gradient(90deg,#000,#fff)";
        rows.push(mkRow(sw, cfg.title || cfg.id));
      }

      if (type === "hillshade") {
        const sw = document.createElement("span");
        sw.style.background = "linear-gradient(135deg,#222,#aaa,#eee)";
        rows.push(mkRow(sw, cfg.title || cfg.id));
      }

      if (cfg.type === "image") {
        const sw = document.createElement("span");
        sw.style.background = "repeating-linear-gradient(45deg, #bbb 0 6px, #ddd 6px 12px)";
        rows.push(mkRow(sw, (cfg.title || cfg.id) + " (image)"));
      }

      return rows;
    } catch {
      return [];
    }
  }

  _rowFromLegendItem(item) {
    const row = document.createElement("div");
    row.className = "kfm-legend-row";

    const sw = document.createElement("span");
    sw.className = "kfm-legend-swatch";

    // Support color or line/point hints
    if (item.gradient && Array.isArray(item.gradient)) {
      const stops = item.gradient.slice(0, 6).map(s => s.color || s).filter(Boolean);
      sw.style.background = `linear-gradient(90deg, ${stops.join(",")})`;
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
    return row;
  }
}

// Optional: expose to window for app.js' fallback check
if (typeof window !== "undefined" && !window.LegendControl) {
  window.LegendControl = LegendControl;
}
