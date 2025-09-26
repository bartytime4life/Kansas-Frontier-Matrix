/* web/app.js
   Kansas-Frontier-Matrix — Minimal MapLibre App (upgraded & connected)
   --------------------------------------------------------------------
   ✅ Loads config in priority: ./config/app.config.json → viewer.json → layers.json → legacy ./layers.json
   ✅ Merges ./config/time_config.json when present (overrides time + defaultYear, step, loop, fps)
   ✅ Supports: raster tiles/COG, image overlays, GeoJSON (fill/line/circle), vector tiles (basic), raster-dem (with fallback)
   ✅ Time slider filters layers by [start,end] (supports YYYY, ISO YYYY-MM-DD, time.start/end)
   ✅ Sidebar UI with toggles + opacity sliders (uses .kfm-sidebar CSS if present)
   ✅ Optional globals:
      - window.LegendControl → legend control
      - window.attachPopup   → popup click handler (map, { layers: ['id', ...], maxFeatures })
   ✅ Safer defaults, robust date parsing, better error handling, idempotent layer add
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
    const arr = Array.isArray(children) ? children : [children];
    for (const c of arr) n.appendChild(typeof c === "string" ? document.createTextNode(c) : c);
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

      // Default style: OSM raster fallback if no style was supplied
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
        // Normalize & register layers (lazy add to the map when needed)
        (cfg.layers || []).forEach(registerLayer);

        // Optional: attach popups if helper is loaded
        if (typeof window.attachPopup === "function") {
          try {
            const clickable = (cfg.layers || [])
              .filter(l => (l.interactive !== false) && (["geojson", "vector"].includes((l.type || "").toLowerCase())))
              .map(l => l.id);
            if (clickable.length) {
              window.attachPopup(map, { layers: clickable, maxFeatures: 12 });
            }
          } catch (e) { console.warn("Popup attach failed:", e); }
        }

        // Optional: legend control if available
        if (typeof window.LegendControl === "function") {
          try {
            map.addControl(new window.LegendControl({ layersConfig: cfg.layers, title: cfg.legendTitle || "Legend" }), "bottom-right");
          } catch (e) { console.warn("Legend addControl failed:", e); }
        }

        // Build UI
        buildTimeUI(cfg);
        buildLayerUI(cfg, map);

        // Initial year (resolve from cfg.time/defaultYear using robust date→year parsing)
        const y0 = clampYear(toYear(nnum(cfg.defaultYear, cfg.time?.defaultYear, 1900)), cfg);
        updateYear(y0, map);
      });

      // Debug surface
      window.KFM = {
        map,
        cfg,
        setYear: (y) => updateYear(clampYear(toYear(y), cfg), map),
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

  async function loadJSON(url) {
    const r = await fetch(url, { cache: "no-store" });
    if (!r.ok) throw new Error(`${url} not found`);
    return r.json();
  }

  async function loadConfig() {
    // Prefer config under ./config/, then legacy ./layers.json
    const candidates = [
      "./config/app.config.json",
      "./config/viewer.json",
      "./config/layers.json",
      "./layers.json"
    ];

    let base = null;
    for (const url of candidates) {
      try {
        base = await loadJSON(url);
        console.info("Loaded config:", url);
        break;
      } catch {}
    }
    if (!base) {
      throw new Error("No config found (tried ./config/app.config.json, viewer.json, layers.json, ./layers.json)");
    }

    // Optional: merge time_config.json overrides
    try {
      const tcfg = await loadJSON("./config/time_config.json");
      if (tcfg?.time) {
        base.time = { ...(base.time || {}), ...tcfg.time };
        if (Number.isFinite(tcfg.time.defaultYear)) {
          base.defaultYear = tcfg.time.defaultYear;
        }
      }
      if (Array.isArray(tcfg?.presets)) {
        base.timePresets = tcfg.presets;
      }
      console.info("Merged time_config.json");
    } catch {
      // no time_config present; ignore
    }

    return base;
  }

  function ensureDOMSkeleton(cfg) {
    // Map container (use #map to align with CSS)
    if (!$("#map")) {
      document.body.appendChild(el("div", { id: "map" }));
    }

    // Sidebar container (class-based to leverage style.css/components)
    if (!$("#sidebar")) {
      const sidebar = el("div", { id: "sidebar", class: "kfm-sidebar" }, [
        el("div", { style: { padding: "12px 12px 6px 12px", borderBottom: "1px solid var(--border, #eee)" } }, [
          el("h2", { style: { margin: "0 0 8px 0", fontSize: "16px", fontWeight: "700" } }, [
            cfg.title || "Kansas-Frontier-Matrix",
          ]),
          el("div", { style: { fontSize: "12px", color: "var(--muted, #666)" } }, [
            cfg.subtitle || "Time-aware layers"
          ])
        ]),
        el("div", { id: "timebox", style: { padding: "12px", borderBottom: "1px solid var(--border, #eee)" } }),
        el("div", { id: "layerbox", style: { padding: "12px" } })
      ]);
      document.body.appendChild(sidebar);
    }
  }

  // -----------------------------------------------------------------------------
  // Dates & Normalization
  // -----------------------------------------------------------------------------
  function toYear(v) {
    // Accepts number, string year, or ISO date string; returns integer year or null
    if (v == null) return null;
    if (Number.isFinite(v)) return Math.trunc(v);
    if (typeof v === "string") {
      const m = v.match(/^(\d{4})/);
      if (m) return parseInt(m[1], 10);
      const n = parseInt(v, 10);
      return Number.isFinite(n) ? n : null;
    }
    return null;
  }

  function clampYear(y, cfg) {
    const min = toYear(cfg.time?.min) ?? 1700;
    const max = toYear(cfg.time?.max) ?? 2100;
    const yy = toYear(y);
    return Math.max(min, Math.min(max, Number.isFinite(yy) ? yy : min));
  }

  function normalizeLayer(l) {
    const d = state.defaults;
    const url = l.url || (Array.isArray(l.tiles) && l.tiles[0]) || l.path || null;
    const type = (l.type || "").toLowerCase();

    const start = toYear(coalesce(l.start, l.year, l.time?.start, null));
    const end   = toYear(coalesce(l.end,   l.year, l.time?.end,   null));

    return {
      id: l.id,
      title: l.title || l.id,
      type,                     // "raster" | "vector" | "image" | "geojson" | "raster-dem"
      url,
      tiles: Array.isArray(l.tiles) ? l.tiles : (url ? [url] : null),
      source: l.source,         // optional source id (for advanced setups)
      sourceLayer: l["source-layer"] || l.sourceLayer || l.id, // for vector tiles
      paint: l.paint || {},
      layout: l.layout || {},
      start,
      end,
      opacity: nnum(l.opacity, d.opacity, 1),
      minzoom: nnum(l.minzoom, d.minzoom, 0),
      maxzoom: nnum(l.maxzoom, d.maxzoom, 24),
      visible: (typeof l.visible === "boolean") ? l.visible : (typeof d.visible === "boolean" ? d.visible : true),
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

  // -----------------------------------------------------------------------------
  // Add to Map
  // -----------------------------------------------------------------------------
  function addLayerToMap(map, layer) {
    const srcId = layer.source || layer.id;

    // Avoid double add
    if (map.getSource(srcId) && (map.getLayer(layer.id) || map.getLayer(layer.id + "_line") || map.getLayer(layer.id + "_circle"))) {
      return;
    }

    // --- Raster tiles/COG/XYZ ---
    if (layer.type === "raster") {
      const tiles = layer.tiles || (layer.url ? [layer.url] : null);
      if (!tiles) { console.warn("Raster layer missing url/tiles:", layer); return; }
      if (!map.getSource(srcId)) {
        const isXYZ = /\{z\}\/\{x\}\/\{y\}/.test(tiles[0]);
        map.addSource(srcId, { type: "raster", tiles, tileSize: layer.tileSize, bounds: layer.bounds || undefined });
      }
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

    // --- Raster DEM (prefer TileJSON url; otherwise fallback to raster) ---
    if (layer.type === "raster-dem") {
      const looksTileJSON = typeof layer.url === "string" && /\.json(\?|$)/i.test(layer.url);
      if (looksTileJSON) {
        try {
          if (!map.getSource(srcId)) map.addSource(srcId, { type: "raster-dem", url: layer.url, tileSize: layer.tileSize || 512 });
          if (!map.getLayer(layer.id)) {
            map.addLayer({
              id: layer.id,
              type: "hillshade",
              source: srcId,
              layout: { visibility: layer.visible ? "visible" : "none", ...(layer.layout || {}) },
              paint: { ...(layer.paint || {}) }
            });
          }
          return;
        } catch (e) {
          console.warn("raster-dem add failed, falling back to raster:", e);
        }
      }
      // Fallback: treat as raster (e.g., local COG tif)
      const fallback = { ...layer, type: "raster" };
      addLayerToMap(map, fallback);
      return;
    }

    // --- Image overlays ---
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

    // --- GeoJSON (explicit or .json/.geojson url) ---
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

    // --- Vector tiles ---
    if (layer.type === "vector") {
      if (!layer.url) { console.warn("Vector tiles layer missing url:", layer); return; }
      if (!map.getSource(srcId)) map.addSource(srcId, { type: "vector", url: layer.url });

      // Default to a line layer (advanced: pass style object via cfg.style)
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

  // -----------------------------------------------------------------------------
  // Visibility & Opacity
  // -----------------------------------------------------------------------------
  function setLayerVisibility(map, layerId, visible) {
    const l = state.layersById.get(layerId);
    if (!l) return;
    l.visible = visible;

    // Ensure added
    if (!map.getLayer(layerId) && !map.getLayer(layerId + "_line") && !map.getLayer(layerId + "_circle")) {
      addLayerToMap(map, l);
    }

    // Apply to all sublayers (geojson uses _fill==id, _line, _circle; hillshade uses main id)
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
    if (type === "hillshade") apply(layerId, "hillshade-exaggeration", Math.max(0.1, opacity)); // simple proxy

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

    const min = toYear(cfg.time?.min) ?? 1700;
    const max = toYear(cfg.time?.max) ?? 2100;
    const cur = clampYear(toYear(nnum(cfg.defaultYear, cfg.time?.defaultYear, min)), cfg);
    const step = nnum(cfg.time?.step, 1);

    const labelRow = el("div", { style: { display: "flex", alignItems: "center", gap: "8px", marginBottom: "6px" } }, [
      el("strong", { style: { fontSize: "13px" } }, ["Year:"]),
      el("span", { id: "yearLabel", style: { fontVariantNumeric: "tabular-nums" } }, [String(cur)])
    ]);

    const slider = el("input", {
      id: "yearSlider", type: "range", min: String(min), max: String(max), step: String(step), value: String(cur),
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

    // Optional: autoplay controls if provided by cfg.time
    if (cfg.time && (cfg.time.loop || cfg.time.fps)) {
      const dock = el("div", { style: { marginTop: "8px", display: "flex", gap: "6px" } });
      const btnPrev = el("button", { class: "btn", onclick: () => slider.stepDown(), title: "Step backward" }, ["⟨"]);
      const btnNext = el("button", { class: "btn", onclick: () => slider.stepUp(),     title: "Step forward"  }, ["⟩"]);
      let playing = false, raf = null, last = 0;
      const fps = nnum(cfg.time.fps, 8);
      const loop = !!cfg.time.loop;

      const btnPlay = el("button", {
        class: "btn btn--primary",
        onclick: () => { playing ? stop() : play(); }
      }, ["▶"]);

      function play() {
        playing = true; btnPlay.textContent = "⏸"; last = performance.now();
        const tick = (now) => {
          if (!playing) return;
          const interval = 1000 / Math.max(1, fps);
          if (now - last >= interval) {
            last = now;
            const before = +slider.value;
            slider.stepUp();
            if (+slider.value === before && loop) slider.value = String(min);
            slider.dispatchEvent(new Event("input", { bubbles: true }));
          }
          raf = requestAnimationFrame(tick);
        };
        raf = requestAnimationFrame(tick);
      }
      function stop() { playing = false; btnPlay.textContent = "▶"; if (raf) cancelAnimationFrame(raf); }

      dock.append(btnPrev, btnPlay, btnNext);
      timebox.appendChild(dock);
    }
  }

  function isActiveForYear(layer, year) {
    const s = toYear(layer.start);
    const e = toYear(layer.end);
    if (s == null && e == null) return true;
    if (s != null && e == null) return year >= s;
    if (s == null && e != null) return year <= e;
    return year >= s && year <= e;
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
          gridTemplateColumns: "24px 1fr 80px",
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
            el("span", { style: { color: "var(--muted, #999)", marginLeft: "6px", fontSize: "11px" } }, [timeBadge(L)])
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
    const s = toYear(coalesce(l.start, l.year, l.time?.start, null));
    const e = toYear(coalesce(l.end,   l.year, l.time?.end,   null));
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
