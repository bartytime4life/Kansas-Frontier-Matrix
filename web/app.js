/* web/app.js
   Kansas-Frontier-Matrix — MapLibre App (upgraded, connected, resilient)
   ----------------------------------------------------------------------
   ✅ Config priority: ./config/app.config.json → viewer.json → layers.json → legacy ./layers.json
   ✅ Optional merge: ./config/time_config.json (overrides time + defaultYear, fps, loop, step, presets)
   ✅ Layer types: raster (XYZ/TileJSON/COG), raster-dem (hillshade fallback), image overlays, geojson, vector
   ✅ Timeline: filters layers by [start,end] (YYYY|ISO|time.start|time.end); supports presets + autoplay
   ✅ Sidebar UI: toggles + opacity sliders (class .kfm-sidebar if available)
   ✅ Connections:
      - window.LegendControl? legend control
      - window.attachPopup?    popup wiring (map, { layers: ['id', ...], maxFeatures })
   ✅ Extras: robust date parsing; idempotent add; localStorage UI state; safer source/layer add ordering
   ✅ Image assets: one logical "image" layer can auto-switch scanned sheets by year (nearest)
   ✅ Debug surface: window.KFM { map, cfg, setYear, setVisible, setOpacity, getLayer, addLayer, flyTo }
*/

(() => {
  // ------------------------------- tiny DOM utils -------------------------------
  const $ = (sel, root = document) => root.querySelector(sel);
  const $$ = (sel, root = document) => [...root.querySelectorAll(sel)];
  const el = (tag, attrs = {}, children = []) => {
    const n = document.createElement(tag);
    for (const [k, v] of Object.entries(attrs || {})) {
      if (k === "class") n.className = v;
      else if (k === "style") Object.assign(n.style, v);
      else if (k.startsWith("on") && typeof v === "function") n.addEventListener(k.slice(2), v);
      else if (v !== undefined && v !== null) n.setAttribute(k, String(v));
    }
    const arr = Array.isArray(children) ? children : [children];
    for (const c of arr) n.appendChild(typeof c === "string" ? document.createTextNode(c) : c);
    return n;
  };

  // ------------------------------- app state -------------------------------
  const state = {
    cfg: null,
    defaults: {},
    year: null,
    layersById: new Map(),       // id -> normalized layer
    uiState: loadUIState(),      // persisted UI (visibility/opacity/year)
    map: null,
    readySources: new Set(),     // sources that finished addSource
    layerAddQueue: [],           // queued layer ids waiting for source
  };

  function loadUIState() {
    try { return JSON.parse(localStorage.getItem("kfm_ui")) || {}; } catch { return {}; }
  }
  function saveUIState() {
    try { localStorage.setItem("kfm_ui", JSON.stringify(state.uiState)); } catch {}
  }

  // ------------------------------- bootstrap -------------------------------
  document.readyState === "loading" ? document.addEventListener("DOMContentLoaded", init) : init();

  async function init() {
    try {
      const cfg = (state.cfg = await loadConfig());
      state.defaults = cfg.defaults || {};
      ensureDOMSkeleton(cfg);

      // style (use object or URL; fallback to OSM)
      const defaultStyle = {
        version: 8,
        sources: {
          osm: {
            type: "raster",
            tiles: ["https://tile.openstreetmap.org/{z}/{x}/{y}.png"],
            tileSize: 256,
            attribution: "© OpenStreetMap contributors",
          },
        },
        layers: [{ id: "osm-bg", type: "raster", source: "osm" }],
      };
      const style = typeof cfg.style === "string" ? cfg.style : (cfg.style || defaultStyle);

      const map = (state.map = new maplibregl.Map({
        container: "map",
        style,
        center: cfg.center || [-98.3, 38.5],
        zoom: cfg.zoom ?? 6,
        attributionControl: cfg.attributionControl !== false,
        hash: cfg.hash ?? true,
        preserveDrawingBuffer: false,
      }));

      // controls
      if (cfg.navControl !== false) map.addControl(new maplibregl.NavigationControl({ visualizePitch: true }), "top-left");
      map.addControl(new maplibregl.ScaleControl({ unit: "imperial" }));

      // load
      map.on("load", () => {
        // normalize & register layers (defer add until used)
        (cfg.layers || []).forEach(registerLayer);

        // popups
        if (typeof window.attachPopup === "function") {
          try {
            const clickable = (cfg.layers || [])
              .filter(l => l.interactive !== false && ["geojson", "vector"].includes((l.type || "").toLowerCase()))
              .map(l => l.id);
            if (clickable.length) window.attachPopup(map, { layers: clickable, maxFeatures: 12 });
          } catch (e) { console.warn("Popup attach failed:", e); }
        }

        // legend
        if (typeof window.LegendControl === "function") {
          try {
            map.addControl(new window.LegendControl({ layersConfig: cfg.layers, title: cfg.legendTitle || "Legend" }), "bottom-right");
          } catch (e) { console.warn("Legend addControl failed:", e); }
        }

        // UI
        buildTimeUI(cfg);
        buildLayerUI(cfg, map);

        // initial year (uiState > config > time.default)
        const fallbackYear = toYear(cfg.defaultYear ?? cfg.time?.defaultYear ?? 1900);
        const y0 = clampYear(toYear(state.uiState.year ?? fallbackYear), cfg);
        updateYear(y0, map);

        // if some layers persisted as visible, ensure added now
        (cfg.layers || []).forEach(l => {
          const L = state.layersById.get(l.id);
          if (!L) return;
          const persistedVisible = state.uiState.visibility?.[L.id];
          const shouldShow = typeof persistedVisible === "boolean" ? persistedVisible : (L.visible !== false);
          if (shouldShow) addLayerToMap(map, L);
        });
      });

      // source readiness
      map.on("sourcedata", (e) => {
        if (e.isSourceLoaded && e.sourceId) {
          state.readySources.add(e.sourceId);
          flushLayerQueue(e.sourceId);
        }
      });

      // debug surface
      window.KFM = {
        map,
        cfg,
        setYear: (y) => updateYear(clampYear(toYear(y), cfg), map),
        setVisible: (id, v) => setLayerVisibility(map, id, !!v),
        setOpacity: (id, a) => setLayerOpacity(map, id, +a),
        getLayer: (id) => state.layersById.get(id),
        addLayer: (def) => { registerLayer(def); addLayerToMap(map, normalizeLayer(def)); },
        flyTo: (center, zoom) => map.flyTo({ center, zoom: zoom ?? map.getZoom() }),
      };
    } catch (err) {
      console.error("KFM init failed:", err);
      document.body.appendChild(el("div", { style: { padding: "12px", color: "#b91c1c", fontFamily: "system-ui" } }, [
        "Failed to initialize map. See console for details."
      ]));
    }
  }

  async function loadJSON(url) {
    const r = await fetch(url, { cache: "no-store" });
    if (!r.ok) throw new Error(`${url} not found`);
    return r.json();
  }

  async function loadConfig() {
    const candidates = [
      "./config/app.config.json",
      "./config/viewer.json",
      "./config/layers.json",
      "./layers.json",
    ];
    let base = null;
    for (const url of candidates) {
      try { base = await loadJSON(url); console.info("[KFM] Loaded config:", url); break; } catch {}
    }
    if (!base) throw new Error("No config found (tried ./config/app.config.json, viewer.json, layers.json, ./layers.json)");

    // optional time overrides
    try {
      const tcfg = await loadJSON("./config/time_config.json");
      if (tcfg?.time) {
        base.time = { ...(base.time || {}), ...tcfg.time };
        if (Number.isFinite(tcfg.time.defaultYear)) base.defaultYear = tcfg.time.defaultYear;
      }
      if (Array.isArray(tcfg?.presets)) base.timePresets = tcfg.presets;
      console.info("[KFM] Merged time_config.json");
    } catch {}

    // sensible defaults
    base.time = base.time || {};
    base.defaults = base.defaults || {};
    return base;
  }

  function ensureDOMSkeleton(cfg) {
    // map
    if (!$("#map")) document.body.appendChild(el("div", { id: "map" }));
    // sidebar
    if (!$("#sidebar")) {
      const sidebar = el("div", { id: "sidebar", class: "kfm-sidebar" }, [
        el("div", { style: { padding: "12px 12px 6px 12px", borderBottom: "1px solid var(--border, #eee)" } }, [
          el("h2", { style: { margin: "0 0 8px 0", fontSize: "16px", fontWeight: "700" } }, [cfg.title || "Kansas-Frontier-Matrix"]),
          el("div", { style: { fontSize: "12px", color: "var(--muted, #666)" } }, [cfg.subtitle || "Time-aware layers"]),
        ]),
        el("div", { id: "timebox", style: { padding: "12px", borderBottom: "1px solid var(--border, #eee)" } }),
        el("div", { id: "layerbox", style: { padding: "12px" } }),
      ]);
      document.body.appendChild(sidebar);
    }
  }

  // ------------------------------- normalization -------------------------------
  function toYear(v) {
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
  function coalesce(...vals) { for (const v of vals) if (v !== undefined && v !== null) return v; return null; }
  function nnum(...vals) { for (const v of vals) if (Number.isFinite(+v)) return +v; return undefined; }

  function normalizeLayer(l) {
    const d = state.defaults;
    const type = (l.type || "").toLowerCase();
    const url = l.url || (Array.isArray(l.tiles) && l.tiles[0]) || l.path || null;
    const start = toYear(coalesce(l.start, l.year, l.time?.start, null));
    const end   = toYear(coalesce(l.end,   l.year, l.time?.end,   null));
    const persistedOpacity = state.uiState.opacity?.[l.id];
    const persistedVisible = state.uiState.visibility?.[l.id];

    return {
      id: l.id,
      title: l.title || l.id,
      type, // raster | vector | image | geojson | raster-dem
      url,
      tiles: Array.isArray(l.tiles) ? l.tiles : (url ? [url] : null),
      source: l.source || l.id,
      sourceLayer: l["source-layer"] || l.sourceLayer || l.id,
      paint: l.paint || {},
      layout: l.layout || {},
      start,
      end,
      opacity: (persistedOpacity ?? nnum(l.opacity, d.opacity, 1)),
      minzoom: nnum(l.minzoom, d.minzoom, 0),
      maxzoom: nnum(l.maxzoom, d.maxzoom, 24),
      visible: typeof persistedVisible === "boolean" ? persistedVisible
              : (typeof l.visible === "boolean" ? l.visible : (typeof d.visible === "boolean" ? d.visible : true)),
      tileSize: nnum(l.tileSize, d.tileSize, 256),
      bounds: l.bounds || d.bounds || null,
      coordinates: l.coordinates || null,
      category: l.category || l.group || "Layers",
      attribution: l.attribution || "",
      interactive: l.interactive !== false,
      timeProperty: l.timeProperty || l["time-property"] || null, // optional for per-feature filtering in GeoJSON

      // image assetization
      assets: Array.isArray(l.assets) ? l.assets : null,
      assetKey: l.assetKey || "year",
      assetStrategy: l.assetStrategy || "nearest",
      _activeAsset: null
    };
  }

  function registerLayer(l) {
    if (!l || !l.id || !l.type) return;
    state.layersById.set(l.id, normalizeLayer(l));
  }

  // ------------------------------- image asset helpers -------------------------------
  function pickAssetForYear(layer, year) {
    if (!Array.isArray(layer.assets) || !layer.assets.length) return null;
    const key = layer.assetKey || "year";
    const numeric = layer.assets.filter(a => Number.isFinite(+a[key]));
    if (!numeric.length) return layer.assets[0];

    if ((layer.assetStrategy || "nearest") === "nearest") {
      let best = null, bestDiff = Infinity;
      for (const a of numeric) {
        const diff = Math.abs(+a[key] - year);
        if (diff < bestDiff) { best = a; bestDiff = diff; }
      }
      return best || numeric[0];
    }
    // exact
    return numeric.find(a => +a[key] === +year) || numeric[0];
  }

  function updateImageAsset(map, layer, year) {
    const srcId = layer.source || layer.id;
    const src = map.getSource(srcId);
    if (!src || src.type !== "image") return;

    const chosen = pickAssetForYear(layer, year);
    if (!chosen) return;

    const active = layer._activeAsset || {};
    if (active.href === chosen.href) return; // already showing

    try {
      if (typeof src.updateImage === "function") src.updateImage({ url: chosen.href });
      if (typeof src.setCoordinates === "function" && Array.isArray(chosen.coordinates)) {
        src.setCoordinates(chosen.coordinates);
      }
      layer._activeAsset = { href: chosen.href, year: chosen[layer.assetKey || "year"] };
    } catch (e) {
      console.warn("updateImageAsset failed:", layer.id, e);
    }
  }

  // ------------------------------- adding layers -------------------------------
  function addLayerToMap(map, layer) {
    const srcId = layer.source || layer.id;

    // avoid double add (consider geojson companions)
    const anyAlready = [layer.id, layer.id + "_line", layer.id + "_circle"].some(id => !!map.getLayer(id));
    if (map.getSource(srcId) && anyAlready) return;

    // ensure source then add layer(s)
    const ensure = () => {
      switch (layer.type) {
        case "raster":      return addRaster(map, layer, srcId);
        case "raster-dem":  return addRasterDEM(map, layer, srcId);
        case "image":       return addImage(map, layer, srcId);
        case "geojson":     return addGeoJSON(map, layer, srcId);
        case "vector":      return addVector(map, layer, srcId);
        default:
          console.warn("Unknown layer.type:", layer.type, layer);
      }
    };

    // if source exists and loaded, add now; if exists but not loaded, queue; else add and rely on on('sourcedata')
    if (map.getSource(srcId)) {
      if (state.readySources.has(srcId)) ensure();
      else enqueueLayer(srcId, layer.id, ensure);
    } else {
      addSource(map, layer, srcId);
      enqueueLayer(srcId, layer.id, ensure);
    }
  }

  function enqueueLayer(srcId, layerId, fn) {
    // prevent duplicates
    if (!state.layerAddQueue.find(q => q.srcId === srcId && q.layerId === layerId)) {
      state.layerAddQueue.push({ srcId, layerId, fn });
    }
  }
  function flushLayerQueue(srcId) {
    const remain = [];
    for (const q of state.layerAddQueue) {
      if (q.srcId === srcId) {
        try { q.fn(); } catch (e) { console.warn("Deferred layer add failed:", q.layerId, e); }
      } else remain.push(q);
    }
    state.layerAddQueue = remain;
  }

  function addSource(map, layer, srcId) {
    try {
      if (map.getSource(srcId)) return;

      // Raster: accept tiles array or TileJSON url
      if (layer.type === "raster") {
        const looksTileJSON = typeof layer.url === "string" && /\.json(\?|$)/i.test(layer.url);
        if (looksTileJSON) map.addSource(srcId, { type: "raster", url: layer.url, tileSize: layer.tileSize || 256 });
        else map.addSource(srcId, { type: "raster", tiles: layer.tiles, tileSize: layer.tileSize || 256, bounds: layer.bounds || undefined });
        return;
      }

      if (layer.type === "raster-dem") {
        const looksTileJSON = typeof layer.url === "string" && /\.json(\?|$)/i.test(layer.url);
        if (looksTileJSON) map.addSource(srcId, { type: "raster-dem", url: layer.url, tileSize: layer.tileSize || 512 });
        else {
          // fallback treat as raster
          map.addSource(srcId, { type: "raster", tiles: layer.tiles, tileSize: layer.tileSize || 256, bounds: layer.bounds || undefined });
        }
        return;
      }

      if (layer.type === "image") {
        // support assetized images (choose initial)
        let url = layer.url, coords = layer.coordinates;
        if ((!url || !Array.isArray(coords)) && Array.isArray(layer.assets) && layer.assets.length) {
          const initial = pickAssetForYear(layer, state.year ?? (layer.assets[0]?.[layer.assetKey || "year"] ?? 0)) || layer.assets[0];
          url = initial?.href || url;
          coords = initial?.coordinates || coords;
          layer._activeAsset = initial ? { href: initial.href, year: initial[layer.assetKey || "year"] } : null;
        }
        if (!url || !Array.isArray(coords)) { console.warn("Image layer missing url/coordinates:", layer.id); return; }
        map.addSource(srcId, { type: "image", url, coordinates: coords });
        return;
      }

      if (layer.type === "geojson") {
        const data = layer.data || layer.url;
        map.addSource(srcId, { type: "geojson", data });
        return;
      }

      if (layer.type === "vector") {
        map.addSource(srcId, { type: "vector", url: layer.url });
        return;
      }
    } catch (e) {
      console.warn("addSource failed:", layer.id, e);
    }
  }

  function addRaster(map, layer, srcId) {
    if (!map.getLayer(layer.id)) {
      map.addLayer({
        id: layer.id,
        type: "raster",
        source: srcId,
        minzoom: layer.minzoom,
        maxzoom: layer.maxzoom,
        paint: { "raster-opacity": layer.opacity, ...(layer.paint || {}) },
        layout: { visibility: layer.visible ? "visible" : "none", ...(layer.layout || {}) },
      });
    }
  }

  function addRasterDEM(map, layer, srcId) {
    if (map.getSource(srcId)?.type === "raster-dem") {
      if (!map.getLayer(layer.id)) {
        map.addLayer({
          id: layer.id,
          type: "hillshade",
          source: srcId,
          layout: { visibility: layer.visible ? "visible" : "none", ...(layer.layout || {}) },
          paint: { ...(layer.paint || {}) },
        });
      }
    } else {
      // fallback already added a raster source; draw as raster
      addRaster(map, layer, srcId);
    }
  }

  function addImage(map, layer, srcId) {
    // source already added in addSource; just add a raster layer
    if (!map.getLayer(layer.id)) {
      map.addLayer({
        id: layer.id,
        type: "raster",
        source: srcId,
        paint: { "raster-opacity": layer.opacity, ...(layer.paint || {}) },
        layout: { visibility: layer.visible ? "visible" : "none", ...(layer.layout || {}) },
      });
    }
  }

  function addGeoJSON(map, layer, srcId) {
    // We add 3 companions: circle (points), line (LineString), fill (Polygon)
    const baseVisible = layer.visible ? "visible" : "none";

    if (!map.getLayer(layer.id + "_circle")) {
      map.addLayer({
        id: layer.id + "_circle",
        type: "circle",
        source: srcId,
        paint: {
          "circle-radius": 4,
          "circle-color": "#c33",
          "circle-opacity": Math.min(layer.opacity, 0.9),
          ...(layer.paint?.circle || {})
        },
        layout: { visibility: baseVisible, ...(layer.layout || {}) },
        filter: ["==", ["geometry-type"], "Point"],
      });
    }

    if (!map.getLayer(layer.id + "_line")) {
      map.addLayer({
        id: layer.id + "_line",
        type: "line",
        source: srcId,
        paint: {
          "line-color": "#c33",
          "line-width": 1.3,
          "line-opacity": layer.opacity,
          ...(layer.paint?.line || {})
        },
        layout: { visibility: baseVisible, ...(layer.layout || {}) },
        filter: ["any", ["==", ["geometry-type"], "LineString"], ["==", ["geometry-type"], "MultiLineString"]],
      });
    }

    if (!map.getLayer(layer.id)) {
      map.addLayer({
        id: layer.id,
        type: "fill",
        source: srcId,
        paint: {
          "fill-color": "#c33",
          "fill-opacity": Math.min(layer.opacity, 0.35),
          ...(layer.paint?.fill || {})
        },
        layout: { visibility: baseVisible, ...(layer.layout || {}) },
        filter: ["any", ["==", ["geometry-type"], "Polygon"], ["==", ["geometry-type"], "MultiPolygon"]],
      });
    }

    // Optional per-feature year filter if layer.timeProperty present
    if (layer.timeProperty) applyPerFeatureTimeFilter(layer);
  }

  function addVector(map, layer, srcId) {
    const sourceLayer = layer.sourceLayer;
    if (!sourceLayer) { console.warn("Vector layer missing source-layer:", layer.id); return; }

    if (!map.getLayer(layer.id)) {
      map.addLayer({
        id: layer.id,
        type: "line",
        source: srcId,
        "source-layer": sourceLayer,
        paint: { "line-color": "#c33", "line-width": 1.3, "line-opacity": layer.opacity, ...(layer.paint || {}) },
        layout: { visibility: layer.visible ? "visible" : "none", ...(layer.layout || {}) },
        minzoom: layer.minzoom, maxzoom: layer.maxzoom,
      });
    }
  }

  // ------------------------------- visibility/opacity -------------------------------
  function setLayerVisibility(map, layerId, visible) {
    const L = state.layersById.get(layerId);
    if (!L) return;
    L.visible = visible;
    state.uiState.visibility = state.uiState.visibility || {};
    state.uiState.visibility[layerId] = visible;
    saveUIState();

    if (!map.getLayer(layerId) && !map.getLayer(layerId + "_line") && !map.getLayer(layerId + "_circle")) {
      addLayerToMap(map, L);
    }

    [layerId, layerId + "_line", layerId + "_circle"].forEach(id => {
      if (map.getLayer(id)) map.setLayoutProperty(id, "visibility", visible ? "visible" : "none");
    });
  }

  function setLayerOpacity(map, layerId, opacity) {
    const L = state.layersById.get(layerId);
    if (!L) return;
    L.opacity = opacity;

    state.uiState.opacity = state.uiState.opacity || {};
    state.uiState.opacity[layerId] = opacity;
    saveUIState();

    const apply = (id, prop, val) => map.getLayer(id) && map.setPaintProperty(id, prop, val);
    const baseType = map.getLayer(layerId)?.type;

    if (baseType === "raster") apply(layerId, "raster-opacity", opacity);
    if (baseType === "fill")   apply(layerId, "fill-opacity", Math.min(opacity, 0.9));
    if (baseType === "line")   apply(layerId, "line-opacity", opacity);
    if (baseType === "hillshade") apply(layerId, "hillshade-exaggeration", Math.max(0.1, opacity)); // proxy

    // companions
    apply(layerId + "_line", "line-opacity", opacity);
    apply(layerId + "_circle", "circle-opacity", Math.min(opacity, 0.9));
  }

  // ------------------------------- time UI + logic -------------------------------
  function buildTimeUI(cfg) {
    const timebox = $("#timebox");
    timebox.innerHTML = "";

    const min = toYear(cfg.time?.min) ?? 1700;
    const max = toYear(cfg.time?.max) ?? 2100;
    const step = nnum(cfg.time?.step, 1);
    const persisted = toYear(state.uiState.year);
    const cur = clampYear(toYear(coalesce(persisted, cfg.defaultYear, cfg.time?.defaultYear, min)), cfg);

    const labelRow = el("div", { style: { display: "flex", alignItems: "center", gap: "8px", marginBottom: "6px", flexWrap: "wrap" } }, [
      el("strong", { style: { fontSize: "13px" } }, ["Year:"]),
      el("span", { id: "yearLabel", style: { fontVariantNumeric: "tabular-nums" } }, [String(cur)]),
      el("div", { style: { marginLeft: "auto", display: "flex", gap: "6px", alignItems: "center" } }, [
        (Array.isArray(cfg.timePresets) && cfg.timePresets.length)
          ? presetSelect(cfg.timePresets, cur) : el("span", {}, []),
      ]),
    ]);

    const slider = el("input", {
      id: "yearSlider", type: "range", min: String(min), max: String(max), step: String(step), value: String(cur),
      style: { width: "100%" },
      oninput: (e) => {
        const y = clampYear(parseInt(e.target.value, 10), cfg);
        $("#yearLabel").textContent = String(y);
        scheduleYearUpdate(y);
      }
    });

    // keyboard nudging
    slider.addEventListener("keydown", (e) => {
      if (e.key === "ArrowLeft" || e.key === "ArrowDown") slider.stepDown();
      if (e.key === "ArrowRight" || e.key === "ArrowUp") slider.stepUp();
      const y = clampYear(parseInt(slider.value, 10), cfg);
      $("#yearLabel").textContent = String(y);
      scheduleYearUpdate(y);
    });

    timebox.append(labelRow, slider);

    // autoplay dock
    if (cfg.time && (cfg.time.loop || cfg.time.fps)) {
      const dock = el("div", { style: { marginTop: "8px", display: "flex", gap: "6px" } });
      const btnPrev = el("button", { class: "btn", title: "Step backward", onclick: () => { slider.stepDown(); slider.dispatchEvent(new Event("input")); } }, ["⟨"]);
      const btnNext = el("button", { class: "btn", title: "Step forward",  onclick: () => { slider.stepUp();   slider.dispatchEvent(new Event("input")); } }, ["⟩"]);
      let playing = false, raf = null, last = 0;
      const fps = nnum(cfg.time.fps, 8);
      const loop = !!cfg.time.loop;

      const btnPlay = el("button", { class: "btn btn--primary" }, ["▶"]);
      btnPlay.onclick = () => { playing ? stop() : play(); };

      function play() {
        playing = true; btnPlay.textContent = "⏸"; last = performance.now();
        const minY = +slider.min, maxY = +slider.max;
        const tick = (now) => {
          if (!playing) return;
          const interval = 1000 / Math.max(1, fps);
          if (now - last >= interval) {
            last = now;
            const before = +slider.value;
            slider.stepUp();
            if (+slider.value === before && loop) slider.value = String(minY);
            slider.dispatchEvent(new Event("input", { bubbles: true }));
            if (+slider.value >= maxY && !loop) stop();
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

  function presetSelect(presets, cur) {
    const sel = el("select", { title: "Time presets", style: { fontSize: "12px" } },
      [el("option", { value: "" }, ["Presets"])].concat(
        presets.map(p => el("option", { value: String(p.year || p) }, [p.label || String(p)]))
      )
    );
    sel.value = String(cur);
    sel.addEventListener("change", () => {
      const y = toYear(sel.value);
      if (y != null) scheduleYearUpdate(y);
    });
    return sel;
  }

  let _yearRaf = null, _yearPending = null;
  function scheduleYearUpdate(y) {
    _yearPending = y;
    if (_yearRaf) return;
    _yearRaf = requestAnimationFrame(() => {
      _yearRaf = null;
      if (_yearPending != null) {
        updateYear(_yearPending, state.map);
        state.uiState.year = _yearPending; saveUIState();
        _yearPending = null;
      }
    });
  }

  function isActiveForYear(layer, year) {
    const s = toYear(layer.start), e = toYear(layer.end);
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
      setLayerVisibility(map, l.id, active && l.visible !== false);

      // assetized image layers: swap to nearest sheet for current year
      if (l.type === "image" && Array.isArray(l.assets) && active) {
        updateImageAsset(map, l, year);
      }

      // per-feature filtering for GeoJSON if timeProperty provided
      if (l.type === "geojson" && l.timeProperty) applyPerFeatureTimeFilter(l);
    });

    $("#yearLabel") && ($("#yearLabel").textContent = String(year));
    const slider = $("#yearSlider"); if (slider) slider.value = String(year);
  }

  function applyPerFeatureTimeFilter(layer) {
    // For GeoJSON layers with a timeProperty, filter feature visibility on the three companions.
    const prop = layer.timeProperty;
    const y = state.year;

    const toFilter = (id) => {
      const exists = state.map.getLayer(id);
      if (!exists) return;
      // accept ISO date strings or numeric years; equality on year
      const filter = [
        "all",
        ["any",
          ["==", ["typeof", ["get", prop]], "number"],
          ["==", ["typeof", ["get", prop]], "string"]
        ],
        ["==", ["to-number", ["slice", ["concat", ["get", prop], ""], 0, 4]], y]
      ];
      state.map.setFilter(id, filter);
    };

    toFilter(layer.id + "_circle");
    toFilter(layer.id + "_line");
    toFilter(layer.id);
  }

  // ------------------------------- layer UI -------------------------------
  function buildLayerUI(cfg, map) {
    const layerbox = $("#layerbox");
    layerbox.innerHTML = "";

    // group by category
    const groups = (cfg.layers || []).reduce((acc, l) => {
      const key = l.group || l.category || "Layers";
      (acc[key] = acc[key] || []).push(l);
      return acc;
    }, {});

    for (const [groupName, ls] of Object.entries(groups)) {
      const groupEl = el("details", { open: true, style: { marginBottom: "10px" } }, [
        el("summary", { style: { cursor: "pointer", fontWeight: "600", marginBottom: "6px" } }, [groupName])
      ]);

      ls.forEach((l) => {
        const L = state.layersById.get(l.id) || normalizeLayer(l);
        state.layersById.set(L.id, L);
        // pre-add to ensure instant control effect (defer heavy vector/geojson until visible)
        if (L.visible !== false) addLayerToMap(map, L);

        const chkId = `chk_${L.id}`;
        const opId = `op_${L.id}`;

        const row = el("div", {
          style: {
            display: "grid",
            gridTemplateColumns: "24px 1fr 90px",
            gap: "6px",
            alignItems: "center",
            marginBottom: "8px"
          }
        }, [
          el("input", {
            id: chkId, type: "checkbox",
            checked: L.visible !== false,
            onchange: (e) => setLayerVisibility(map, L.id, e.target.checked)
          }),
          el("label", { for: chkId, style: { fontSize: "13px", cursor: "pointer", display: "flex", flexDirection: "column" } }, [
            el("span", {}, [L.title]),
            el("span", { style: { color: "var(--muted, #999)", fontSize: "11px" } }, [timeBadge(L)])
          ]),
          el("input", {
            id: opId,
            type: "range", min: "0", max: "1", step: "0.05", value: String(L.opacity ?? 1),
            title: "Opacity",
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
})();