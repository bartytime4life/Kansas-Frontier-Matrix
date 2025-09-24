/* web/app.js
   Kansas-Frontier-Matrix — Minimal MapLibre App (upgraded & connected)
   --------------------------------------------------------------------
   ✅ Looks for config under ./config/ (app.config.json → viewer.json → layers.json), then legacy ./layers.json
   ✅ Supports raster tiles, image overlays, vector tiles, and GeoJSON (fill/line/circle)
   ✅ Time slider filters layers by [start,end] (layer.start/layer.end or layer.time.{start,end})
   ✅ Sidebar UI (class-based) with toggles + opacity sliders (uses .kfm-sidebar CSS if present)
   ✅ Safer defaults, better error handling, small bug fixes
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
    try {
      const cfg = (state.cfg = await loadConfig());
      state.defaults = cfg.defaults || {};

      ensureDOMSkeleton(cfg);

      // Default style: OSM raster fallback if no style supplied
      const defaultStyle = {
        version: 8,
        sources: {
          osm: {
            type: "raster",
            tiles: ["https://tile.openstreetmap.org/{z}/{x}/{y}.png"],
            tileSize: 256,
            attribution: "© OpenStreetMap contributors"
          }
        },
        layers: [{ id: "osm-bg", type: "raster", source: "osm" }]
      };

      // If cfg.style is a URL string, use it; if it's an object, pass as is
      const style = typeof cfg.style === "string" ? cfg.style : (cfg.style || defaultStyle);

      // MapLibre
      const map = (state.map = new maplibregl.Map({
        container: "map",
        style,
        center: cfg.center || [-98.3, 38.5],
        zoom: cfg.zoom ?? 6,
        attributionControl: cfg.attributionControl !== false
      }));

      if (cfg.navControl !== false) {
        map.addControl(new maplibregl.NavigationControl({ visualizePitch: true }), "top-left");
      }
      map.addControl(new maplibregl.ScaleControl({ unit: "imperial" }));

      map.on("load", () => {
        // Register & normalize layers (but only add to map when needed)
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
        addLayer: (def) => { registerLayer(def); addLayerToMap(map, normalizeLayer(def)); },
      };
    } catch (err) {
      console.error("KFM init failed:", err);
      document.body.appendChild(
        el("div", { style: { padding: "12px", color: "#b91c1c", fontFamily: "system-ui" } }, [
          "Failed to initialize map. See console for details."
        ])
      );
    }
  }

  async function loadConfig() {
    // Prefer config under ./config/, then legacy ./layers.json
    const candidates = [
      "./config/app.config.json",
      "./config/viewer.json",
      "./config/layers.json",
      "./layers.json"
    ];
    for (const url of candidates) {
      try {
        const r = await fetch(url, { cache: "no-store" });
        if (r.ok) {
          const json = await r.json();
          console.info("Loaded config:", url);
          return json;
        }
      } catch {}
    }
    throw new Error("No config found (tried ./config/app.config.json, viewer.json, layers.json, ./layers.json)");
  }

  function ensureDOMSkeleton(cfg) {
    // Map container (use #map to align with CSS)
    if (!$("#map")) {
      document.body.appendChild(el("div", { id: "map" }));
    }

    // Sidebar container (class-based to leverage map.css)
    if (!$("#sidebar")) {
      const sidebar = el("div", { id: "sidebar", class: "kfm-sidebar" }, [
        el("div", { style: { padding: "12px 12px 6px 12px", borderBottom: "1px solid var(--kfm-border, #eee)" } }, [
          el("h2", { style: { margin: "0 0 8px 0", fontSize: "16px", fontWeight: "700" } }, [
            cfg.title || "Kansas-Frontier-Matrix",
          ]),
          el("div", { style: { fontSize: "12px", color: "var(--kfm-fg-muted, #666)" } }, [
            cfg.subtitle || "Time-aware layers"
          ])
        ]),
        el("div", { id: "timebox", style: { padding: "12px", borderBottom: "1px solid var(--kfm-border, #eee)" } }),
        el("div", { id: "layerbox", style: { padding: "12px" } })
      ]);
      document.body.appendChild(sidebar);
    }
  }

  // -----------------------------------------------------------------------------
  // Normalization & Map layer add
  // -----------------------------------------------------------------------------
  function clampYear(y, cfg) {
    const min = cfg.time?.min ?? 1700;
    const max = cfg.time?.max ?? 2100;
    return Math.max(min, Math.min(max, +y));
  }

  function normalizeLayer(l) {
    const d = state.defaults;
    const url = l.url || (Array.isArray(l.tiles) && l.tiles[0]) || l.path || null;
    const type = (l.type || "").toLowerCase();

    return {
      id: l.id,
      title: l.title || l.id,
      type,                    // "raster" | "vector" | "image" | "geojson"
      url,
      tiles: Array.isArray(l.tiles) ? l.tiles : (url ? [url] : null),
      source: l.source,        // optional source id
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

    // Already added? Don't re-add source/layers.
    if (map.getSource(srcId) && (map.getLayer(layer.id) || map.getLayer(layer.id + "_line") || map.getLayer(layer.id + "_circle"))) {
      return;
    }

    // Raster tiles
    if (layer.type === "raster") {
      const tiles = layer.tiles || (layer.url ? [layer.url] : null);
      if (!tiles) { console.warn("Raster layer missing url/tiles:", layer); return; }
      if (!map.getSource(srcId)) map.addSource(srcId, { type: "raster", tiles, tileSize: layer.tileSize, bounds: layer.bounds || undefined });
      if (!map.getLayer(layer.id)) {
        map.addLayer({
          id: layer.id,
          type: "raster",
          source: srcId,
          minzoom: layer.minzoom,
          maxzoom: layer.maxzoom,
          paint: { "raster-opacity": layer.opacity, ...(layer.paint || {}) },
          layout: { visibility: layer.visible ? "visible" : "none", ...(layer.layout || {}) }
        });
      }
      return;
    }

    // Image overlays
    if (layer.type === "image" && Array.isArray(layer.coordinates) && layer.url) {
      if (!map.getSource(srcId)) map.addSource(srcId, { type: "image", url: layer.url, coordinates: layer.coordinates });
      if (!map.getLayer(layer.id)) {
        map.addLayer({
          id: layer.id, type: "raster", source: srcId,
          paint: { "raster-opacity": layer.opacity, ...(layer.paint || {}) },
          layout: { visibility: layer.visible ? "visible" : "none", ...(layer.layout || {}) }
        });
      }
      return;
    }

    // GeoJSON (explicit type or URL with geojson/json)
    const isGeoJSON = layer.type === "geojson" || /\.(json|geojson)(\?|$)/i.test(layer.url || "");
    if (isGeoJSON) {
      if (!layer.url) { console.warn("GeoJSON layer missing url:", layer); return; }
      if (!map.getSource(srcId)) map.addSource(srcId, { type: "geojson", data: layer.url });

      // Circle for points
      const circleId = layer.id + "_circle";
      if (!map.getLayer(circleId)) {
        map.addLayer({
          id: circleId, type: "circle", source: srcId,
          paint: {
            "circle-radius": 4,
            "circle-color": "#c33",
            "circle-opacity": Math.min(layer.opacity, 0.9),
            ...(layer.paint?.circle || {})
          },
          layout: { visibility: layer.visible ? "visible" : "none", ...(layer.layout || {}) },
          filter: ["==", ["geometry-type"], "Point"]
        });
      }

      // Line for LineString
      const lineId = layer.id + "_line";
      if (!map.getLayer(lineId)) {
        map.addLayer({
          id: lineId, type: "line", source: srcId,
          paint: {
            "line-color": "#c33",
            "line-width": 1.3,
            "line-opacity": layer.opacity,
            ...(layer.paint?.line || {})
          },
          layout: { visibility: layer.visible ? "visible" : "none", ...(layer.layout || {}) },
          filter: ["==", ["geometry-type"], "LineString"]
        });
      }

      // Fill for polygons
      if (!map.getLayer(layer.id)) {
        map.addLayer({
          id: layer.id, type: "fill", source: srcId,
          paint: {
            "fill-color": "#c33",
            "fill-opacity": Math.min(layer.opacity, 0.35),
            ...(layer.paint?.fill || {})
          },
          layout: { visibility: layer.visible ? "visible" : "none", ...(layer.layout || {}) },
          filter: ["==", ["geometry-type"], "Polygon"]
        });
      }
      return;
    }

    // Vector tiles
    if (layer.type === "vector") {
      if (!layer.url) { console.warn("Vector tiles layer missing url:", layer); return; }
      if (!map.getSource(srcId)) map.addSource(srcId, { type: "vector", url: layer.url });

      // Default to a line layer; advanced styling can pass paint/layout with correct type via cfg.style instead.
      if (!map.getLayer(layer.id)) {
        map.addLayer({
          id: layer.id,
          type: "line",
          source: srcId,
          "source-layer": layer.sourceLayer,
          paint: { "line-color": "#c33", "line-width": 1.3, "line-opacity": layer.opacity, ...(layer.paint || {}) },
          layout: { visibility: layer.visible ? "visible" : "none", ...(layer.layout || {}) },
          minzoom: layer.minzoom,
          maxzoom: layer.maxzoom
        });
      }
    }
  }

  function setLayerVisibility(map, layerId, visible) {
    const l = state.layersById.get(layerId);
    if (!l) return;
    l.visible = visible;

    // Ensure added
    if (!map.getLayer(layerId) && !map.getLayer(layerId + "_line") && !map.getLayer(layerId + "_circle")) {
      addLayerToMap(map, l);
    }

    // Apply to all sublayers (geojson uses _fill==id, _line, _circle)
    [layerId, layerId + "_line", layerId + "_circle"].forEach(id => {
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

    // geojson companions
    const lineId = layerId + "_line";
    const circleId = layerId + "_circle";
    if (map.getLayer(lineId)) apply(lineId, "line-opacity", opacity);
    if (map.getLayer(circleId)) apply(circleId, "circle-opacity", Math.min(opacity, 0.9));
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
      id: "yearSlider", type: "range", min: String(min), max: String(max), step: "1", value: String(cur),
      style: { width: "100%" },
      oninput: (e) => {
        const y = clampYear(parseInt(e.target.value, 10), cfg);
        $("#yearLabel").textContent = String(y);
        requestAnimationFrame(() => updateYear(y, state.map)); // smooth updates
      }
    });

    // Keyboard nudging with arrow keys while focused
    slider.addEventListener("keydown", (e) => {
      if (e.key === "ArrowLeft" || e.key === "ArrowDown") slider.stepDown();
      if (e.key === "ArrowRight" || e.key === "ArrowUp") slider.stepUp();
      const y = clampYear(parseInt(slider.value, 10), cfg);
      $("#yearLabel").textContent = String(y);
      requestAnimationFrame(() => updateYear(y, state.map));
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
      // Only toggle visibility ON if layer's own visibility isn't false
      setLayerVisibility(map, l.id, active && l.visible !== false);
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
            el("span", { style: { color: "var(--kfm-fg-muted, #999)", marginLeft: "6px", fontSize: "11px" } }, [timeBadge(L)])
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
