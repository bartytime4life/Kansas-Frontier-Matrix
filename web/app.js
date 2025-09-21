/* Kansas-Frontier-Matrix — Minimal MapLibre App (upgraded)
   - Prefers ./app.config.json; falls back to ./layers.json
   - Supports raster (tile URL), image overlays, vector tiles, and GeoJSON
   - Time slider filters layers by year (start/end in layer)
   - Sidebar UI with toggles + opacity sliders
*/

(() => {
  const $ = (sel, root = document) => root.querySelector(sel);
  const $$ = (sel, root = document) => [...root.querySelectorAll(sel)];
  const el = (tag, attrs = {}, children = []) => {
    const n = document.createElement(tag);
    for (const [k, v] of Object.entries(attrs)) {
      if (k === "class") n.className = v;
      else if (k === "style") Object.assign(n.style, v);
      else if (k.startsWith("on") && typeof v === "function") n.addEventListener(k.slice(2), v);
      else if (v !== undefined && v !== null) n.setAttribute(k, String(v));
    }
    for (const c of children) n.appendChild(typeof c === "string" ? document.createTextNode(c) : c);
    return n;
  };

  // -----------------------------------------------------------------------------
  // App State
  // -----------------------------------------------------------------------------
  const state = {
    cfg: null,
    defaults: {},
    year: null,
    layersById: new Map(), // id -> normalized layer
    map: null,
  };

  // -----------------------------------------------------------------------------
  // Bootstrap
  // -----------------------------------------------------------------------------
  async function init() {
    const cfg = state.cfg = await loadConfig();
    state.defaults = cfg.defaults || {};

    ensureDOMSkeleton(cfg);

    // MapLibre
    const map = state.map = new maplibregl.Map({
      container: "map",
      style: cfg.style || { version: 8, sources: {}, layers: [] },
      center: cfg.center || [-98.3, 38.5],
      zoom: cfg.zoom ?? 6,
      attributionControl: cfg.attributionControl !== false
    });
    if (cfg.navControl !== false) map.addControl(new maplibregl.NavigationControl({ visualizePitch: true }), "top-left");
    map.addControl(new maplibregl.ScaleControl({ unit: "imperial" }));

    map.on("load", () => {
      // Register & normalize layers
      (cfg.layers || []).forEach(registerLayer);

      // Build UI
      buildTimeUI(cfg);
      buildLayerUI(cfg, map);

      // Initial year
      const y0 = clampYear(cfg.defaultYear ?? (cfg.time?.min ?? 1900), cfg);
      updateYear(y0, map);
    });

    // Debug surface
    window.KFM = {
      map,
      cfg,
      setYear: (y) => updateYear(clampYear(y, cfg), map),
      setVisible: (id, v) => setLayerVisibility(map, id, !!v),
      setOpacity: (id, a) => setLayerOpacity(map, id, +a),
      getLayer: (id) => state.layersById.get(id),
    };
  }

  async function loadConfig() {
    // Prefer app.config.json; fallback to layers.json
    try {
      const r = await fetch("./app.config.json");
      if (r.ok) return r.json();
      throw new Error("app.config.json not ok");
    } catch {
      const r2 = await fetch("./layers.json");
      if (!r2.ok) throw new Error("Failed to load layers.json");
      return r2.json();
    }
  }

  function ensureDOMSkeleton(cfg) {
    if (!$("#map")) {
      document.body.appendChild(
        el("div", { id: "map", style: { position: "absolute", inset: "0 320px 0 0" } })
      );
    }
    if (!$("#sidebar")) {
      document.body.appendChild(
        el("div", {
          id: "sidebar",
          style: {
            position: "absolute", right: "0", top: "0", bottom: "0", width: "320px",
            background: "rgba(255,255,255,0.96)", borderLeft: "1px solid #ddd",
            fontFamily: "system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial", overflow: "auto"
          }
        }, [
          el("div", { style: { padding: "12px 12px 6px 12px", borderBottom: "1px solid #eee" } }, [
            el("h2", { style: { margin: "0 0 8px 0", fontSize: "16px", fontWeight: "600" } }, ["Kansas-Frontier-Matrix"]),
            el("div", { style: { fontSize: "12px", color: "#666" } }, [cfg.subtitle || "Time-aware layers"])
          ]),
          el("div", { id: "timebox", style: { padding: "12px", borderBottom: "1px solid #eee" } }),
          el("div", { id: "layerbox", style: { padding: "12px" } })
        ])
      );
    }
  }

  // -----------------------------------------------------------------------------
  // Normalization & Map layer add
  // -----------------------------------------------------------------------------
  function clampYear(y, cfg) {
    const min = cfg.time?.min ?? 1700;
    const max = cfg.time?.max ?? 2100;
    return Math.max(min, Math.min(max, y));
  }

  function normalizeLayer(l) {
    const d = state.defaults;
    const url = l.url || (Array.isArray(l.tiles) && l.tiles[0]) || l.path || null;
    return {
      id: l.id,
      title: l.title || l.id,
      type: l.type,                  // "raster" | "vector" | "image"
      url,
      tiles: Array.isArray(l.tiles) ? l.tiles : (url ? [url] : null),
      source: l.source,              // optional source id
      sourceLayer: l["source-layer"] || l.sourceLayer || l.id, // for vector tiles
      paint: l.paint || {},
      layout: l.layout || {},
      start: coalesce(l.start, l.year, l.time?.start, null),
      end: coalesce(l.end, l.year, l.time?.end, null),
      opacity: nnum(l.opacity, d.opacity, 1),
      minzoom: nnum(l.minzoom, d.minzoom, 0),
      maxzoom: nnum(l.maxzoom, d.maxzoom, 24),
      visible: bool(l.visible, d.visible, true),
      tileSize: nnum(l.tileSize, d.tileSize, 256),
      bounds: l.bounds || d.bounds || null,
      coordinates: l.coordinates || null, // for image overlays
      category: l.category || l.group || "Layers",
      attribution: l.attribution || ""
    };
  }

  function registerLayer(l) {
    if (!l || !l.id || !l.type) return;
    const layer = normalizeLayer(l);
    state.layersById.set(layer.id, layer);
  }

  function addLayerToMap(map, layer) {
    const srcId = layer.source || layer.id;
    if (map.getSource(srcId)) return; // already added

    if (layer.type === "raster") {
      const tiles = layer.tiles || (layer.url ? [layer.url] : null);
      if (!tiles) { console.warn("Raster layer missing url/tiles:", layer); return; }
      map.addSource(srcId, { type: "raster", tiles, tileSize: layer.tileSize });
      map.addLayer({
        id: layer.id,
        type: "raster",
        source: srcId,
        minzoom: layer.minzoom,
        maxzoom: layer.maxzoom,
        paint: { "raster-opacity": layer.opacity, ...(layer.paint || {}) },
        layout: { visibility: layer.visible ? "visible" : "none", ...(layer.layout || {}) }
      });
    } else if (layer.type === "vector") {
      if (/\.(json|geojson)(\?|$)/i.test(layer.url || "")) {
        // GeoJSON
        map.addSource(srcId, { type: "geojson", data: layer.url });
        const lineId = layer.id + "_line";
        map.addLayer({
          id: lineId, type: "line", source: srcId,
          paint: { "line-color": "#c33", "line-width": 1.3, "line-opacity": layer.opacity, ...(layer.paint?.line || {}) },
          layout: { visibility: layer.visible ? "visible" : "none", ...(layer.layout || {}) }
        });
        map.addLayer({
          id: layer.id, type: "fill", source: srcId,
          paint: { "fill-color": "#c33", "fill-opacity": Math.min(layer.opacity, 0.35), ...(layer.paint?.fill || {}) },
          layout: { visibility: layer.visible ? "visible" : "none", ...(layer.layout || {}) },
          filter: ["==", ["geometry-type"], "Polygon"]
        });
      } else {
        // Vector tiles
        if (!layer.url) { console.warn("Vector tiles layer missing url:", layer); return; }
        map.addSource(srcId, { type: "vector", url: layer.url });
        map.addLayer({
          id: layer.id,
          type: "line",
          source: srcId,
          "source-layer": layer.sourceLayer,
          paint: { "line-color": "#c33", "line-width": 1.3, "line-opacity": layer.opacity, ...(layer.paint || {}) },
          layout: { visibility: layer.visible ? "visible" : "none", ...(layer.layout || {}) }
        });
      }
    } else if (layer.type === "image" && Array.isArray(layer.coordinates) && layer.url) {
      map.addSource(srcId, { type: "image", url: layer.url, coordinates: layer.coordinates });
      map.addLayer({
        id: layer.id, type: "raster", source: srcId,
        paint: { "raster-opacity": layer.opacity, ...(layer.paint || {}) },
        layout: { visibility: layer.visible ? "visible" : "none", ...(layer.layout || {}) }
      });
    }
  }

  function setLayerVisibility(map, layerId, visible) {
    const l = state.layersById.get(layerId);
    if (!l) return;
    l.visible = visible;

    // Ensure added
    if (!map.getLayer(layerId) && !map.getLayer(layerId + "_line")) {
      addLayerToMap(map, l);
    }

    // Apply to all sublayers (vector geojson uses _line + fill)
    [layerId, layerId + "_line"].forEach(id => {
      if (map.getLayer(id)) map.setLayoutProperty(id, "visibility", visible ? "visible" : "none");
    });
  }

  function setLayerOpacity(map, layerId, opacity) {
    const l = state.layersById.get(layerId);
    if (!l) return;
    l.opacity = opacity;

    const apply = (id, prop, val) => map.getLayer(id) && map.setPaintProperty(id, prop, val);

    const type = map.getLayer(layerId)?.type;
    if (type === "raster") apply(layerId, "raster-opacity", opacity);
    if (type === "fill")   apply(layerId, "fill-opacity", opacity);
    if (type === "line")   apply(layerId, "line-opacity", opacity);

    // companion line layer for geojson
    const lineId = layerId + "_line";
    if (map.getLayer(lineId)) apply(lineId, "line-opacity", opacity);
  }

  // -----------------------------------------------------------------------------
  // Time UI
  // -----------------------------------------------------------------------------
  function buildTimeUI(cfg) {
    const timebox = $("#timebox");
    timebox.innerHTML = "";

    const min = nnum(cfg.time?.min, 1700);
    const max = nnum(cfg.time?.max, 2100);
    const cur = clampYear(nnum(cfg.defaultYear, min), cfg);

    const labelRow = el("div", { style: { display: "flex", alignItems: "center", gap: "8px", marginBottom: "6px" } }, [
      el("strong", { style: { fontSize: "13px" } }, ["Year:"]),
      el("span", { id: "yearLabel", style: { fontVariantNumeric: "tabular-nums" } }, [String(cur)])
    ]);

    const slider = el("input", {
      id: "yearSlider", type: "range", min: String(min), max: String(max), value: String(cur),
      style: { width: "100%" },
      oninput: (e) => {
        const y = clampYear(parseInt(e.target.value, 10), cfg);
        $("#yearLabel").textContent = String(y);
        updateYear(y, state.map);
      }
    });

    timebox.append(labelRow, slider);
  }

  function isActiveForYear(layer, year) {
    if (layer.start == null && layer.end == null) return true;
    if (layer.start != null && layer.end == null) return year >= layer.start;
    if (layer.start == null && layer.end != null) return year <= layer.end;
    return year >= layer.start && year <= layer.end;
  }

  function updateYear(year, map) {
    if (!map) return;
    state.year = year;
    state.layersById.forEach((l) => {
      const active = isActiveForYear(l, year);
      setLayerVisibility(map, l.id, active && l.visible);
    });
  }

  // -----------------------------------------------------------------------------
  // Layer UI
  // -----------------------------------------------------------------------------
  function buildLayerUI(cfg, map) {
    const layerbox = $("#layerbox");
    layerbox.innerHTML = "";

    const groups = groupBy((cfg.layers || []), (l) => l.group || l.category || "Layers");
    for (const [groupName, ls] of Object.entries(groups)) {
      const groupEl = el("details", { open: true, style: { marginBottom: "10px" } }, [
        el("summary", { style: { cursor: "pointer", fontWeight: "600", marginBottom: "6px" } }, [groupName])
      ]);

      ls.forEach((l) => {
        const L = state.layersById.get(l.id) || normalizeLayer(l);
        state.layersById.set(L.id, L);

        // Pre-add to map so controls work instantly
        addLayerToMap(map, L);

        const chkId = `chk_${L.id}`;
        const row = el("div", { style: {
          display: "grid",
          gridTemplateColumns: "24px 1fr 60px",
          gap: "6px",
          alignItems: "center",
          marginBottom: "6px"
        }}, [
          el("input", {
            id: chkId,
            type: "checkbox",
            checked: L.visible !== false,
            onchange: (e) => setLayerVisibility(map, L.id, e.target.checked)
          }),
          el("label", { for: chkId, style: { fontSize: "13px", cursor: "pointer" } }, [
            L.title,
            el("span", { style: { color: "#999", marginLeft: "6px", fontSize: "11px" } }, [timeBadge(L)])
          ]),
          el("input", {
            type: "range", min: "0", max: "1", step: "0.05", value: String(L.opacity ?? 1),
            oninput: (e) => setLayerOpacity(map, L.id, parseFloat(e.target.value))
          })
        ]);

        groupEl.appendChild(row);
      });

      layerbox.appendChild(groupEl);
    }
  }

  function timeBadge(l) {
    const s = coalesce(l.start, l.year, l.time?.start, null);
    const e = coalesce(l.end, l.year, l.time?.end, null);
    if (s == null && e == null) return "";
    if (s != null && e != null && s === e) return `[${s}]`;
    if (s != null && e != null) return `[${s}–${e}]`;
    if (s != null) return `[≥${s}]`;
    return `[≤${e}]`;
  }

  // -----------------------------------------------------------------------------
  // Small utils
  // -----------------------------------------------------------------------------
  function coalesce(...vals) {
    for (const v of vals) if (v !== undefined && v !== null) return v;
    return null;
  }
  function nnum(...vals) {
    for (const v of vals) if (Number.isFinite(+v)) return +v;
    return undefined;
  }
  function bool(...vals) {
    for (const v of vals) if (typeof v === "boolean") return v;
    return undefined;
  }
  function groupBy(arr, keyFn) {
    return arr.reduce((acc, v) => {
      const k = keyFn(v);
      (acc[k] = acc[k] || []).push(v);
      return acc;
    }, {});
  }

  // -----------------------------------------------------------------------------
  // Kickoff
  // -----------------------------------------------------------------------------
  document.readyState === "loading" ? document.addEventListener("DOMContentLoaded", init) : init();
})();
