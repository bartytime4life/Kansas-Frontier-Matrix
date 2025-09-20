/* Kansas-Frontier-Matrix — Minimal MapLibre App
   - Reads ./app.config.json (layers + UI options)
   - Time slider filters layers by year (start/end in layer)
   - Supports raster (tile URL) and vector (GeoJSON/tiles)
   - Tiny UI: year slider, layer list with toggles + opacity
*/

(() => {
  const $ = (sel, root = document) => root.querySelector(sel);
  const $$ = (sel, root = document) => [...root.querySelectorAll(sel)];
  const el = (tag, attrs = {}, children = []) => {
    const n = document.createElement(tag);
    Object.entries(attrs).forEach(([k, v]) => {
      if (k === "class") n.className = v;
      else if (k === "style") Object.assign(n.style, v);
      else if (k.startsWith("on") && typeof v === "function") n.addEventListener(k.slice(2), v);
      else n.setAttribute(k, v);
    });
    children.forEach(c => n.appendChild(typeof c === "string" ? document.createTextNode(c) : c));
    return n;
  };

  // --- App State --------------------------------------------------------------
  const state = {
    cfg: null,
    year: null,
    layersById: new Map(), // {id -> layerDef}
  };

  // --- Map Init ---------------------------------------------------------------
  async function init() {
    const cfg = state.cfg = await fetch("./app.config.json").then(r => r.json());

    // Create minimal HTML if not present
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

    // MapLibre
    const map = new maplibregl.Map({
      container: "map",
      style: cfg.style || { version: 8, sources: {}, layers: [] },
      center: cfg.center || [-98.3, 38.5],
      zoom: cfg.zoom ?? 6
    });
    if (cfg.attributionControl !== false) map.addControl(new maplibregl.AttributionControl({ compact: true }));
    if (cfg.navControl !== false) map.addControl(new maplibregl.NavigationControl({ visualizePitch: true }), "top-left");

    map.on("load", () => {
      // Register layers
      (cfg.layers || []).forEach(registerLayer);
      // UI
      buildTimeUI(cfg);
      buildLayerUI(cfg, map);
      // Initial year
      const y0 = clampYear(cfg.defaultYear ?? (cfg.time?.min ?? 1900), cfg);
      updateYear(y0, map);
    });

    // Expose for debugging
    window.KFM = { map, cfg, updateYear: y => updateYear(y, map) };
  }

  // --- Helpers ---------------------------------------------------------------
  function clampYear(y, cfg) {
    const min = cfg.time?.min ?? 1700;
    const max = cfg.time?.max ?? 2100;
    return Math.max(min, Math.min(max, y));
  }

  function registerLayer(l) {
    // Normalize
    const layer = {
      id: l.id,
      title: l.title || l.id,
      type: l.type,            // "raster" | "vector" | "image"
      url: l.url,              // raster tile template OR vector tiles URL OR GeoJSON url
      source: l.source,        // optional: named source
      paint: l.paint || {},
      layout: l.layout || {},
      start: l.start ?? l.year ?? l.time?.start ?? null,
      end: l.end ?? l.year ?? l.time?.end ?? null,
      opacity: l.opacity ?? 1,
      minzoom: l.minzoom ?? 0,
      maxzoom: l.maxzoom ?? 24,
      visibility: l.visibility ?? true,
      // optional for image overlays:
      coordinates: l.coordinates // [[lng,lat],...4]
    };
    state.layersById.set(layer.id, layer);
  }

  function addLayerToMap(map, layer) {
    const srcId = layer.source || layer.id;
    if (map.getSource(srcId)) return; // already added

    if (layer.type === "raster") {
      map.addSource(srcId, { type: "raster", tiles: [layer.url], tileSize: 256 });
      map.addLayer({
        id: layer.id,
        type: "raster",
        source: srcId,
        minzoom: layer.minzoom,
        maxzoom: layer.maxzoom,
        paint: { "raster-opacity": layer.opacity, ...(layer.paint || {}) },
        layout: { visibility: layer.visibility ? "visible" : "none", ...(layer.layout || {}) }
      });
    } else if (layer.type === "vector") {
      // Support either vector tiles or GeoJSON
      if (/\.(json|geojson)(\?|$)/i.test(layer.url)) {
        map.addSource(srcId, { type: "geojson", data: layer.url });
        const lineId = layer.id + "_line";
        map.addLayer({
          id: lineId, type: "line", source: srcId,
          paint: { "line-color": "#c33", "line-width": 1.3, ...(layer.paint?.line || {}) },
          layout: { visibility: layer.visibility ? "visible" : "none", ...(layer.layout || {}) }
        });
        // Optional fill (if polygons present)
        map.addLayer({
          id: layer.id, type: "fill", source: srcId,
          paint: { "fill-color": "#c33", "fill-opacity": 0.15, ...(layer.paint?.fill || {}) },
          layout: { visibility: layer.visibility ? "visible" : "none", ...(layer.layout || {}) },
          filter: ["==", ["geometry-type"], "Polygon"]
        });
      } else {
        // Vector tiles
        map.addSource(srcId, { type: "vector", url: layer.url });
        map.addLayer({
          id: layer.id,
          type: "line",
          source: srcId,
          "source-layer": layer.sourceLayer || layer.id, // allow config to define the source-layer
          paint: { "line-color": "#c33", "line-width": 1.3, ...(layer.paint || {}) },
          layout: { visibility: layer.visibility ? "visible" : "none", ...(layer.layout || {}) }
        });
      }
    } else if (layer.type === "image" && Array.isArray(layer.coordinates)) {
      map.addSource(srcId, { type: "image", url: layer.url, coordinates: layer.coordinates });
      map.addLayer({
        id: layer.id, type: "raster", source: srcId,
        paint: { "raster-opacity": layer.opacity, ...(layer.paint || {}) },
        layout: { visibility: layer.visibility ? "visible" : "none", ...(layer.layout || {}) }
      });
    }
  }

  function setLayerVisibility(map, layerId, visible) {
    const l = state.layersById.get(layerId);
    if (!l) return;
    l.visibility = visible;
    // Add if not yet added
    if (!map.getLayer(layerId) && !map.getLayer(layerId + "_line")) {
      addLayerToMap(map, l);
    }
    // Apply to all sublayers (for vector w/line+fill)
    [layerId, layerId + "_line"].forEach(id => {
      if (map.getLayer(id)) map.setLayoutProperty(id, "visibility", visible ? "visible" : "none");
    });
  }

  function setLayerOpacity(map, layerId, opacity) {
    const l = state.layersById.get(layerId);
    if (!l) return;
    l.opacity = opacity;
    if (map.getLayer(layerId)) {
      const type = map.getLayer(layerId).type;
      if (type === "raster") map.setPaintProperty(layerId, "raster-opacity", opacity);
      if (type === "fill") map.setPaintProperty(layerId, "fill-opacity", opacity);
      if (type === "line") map.setPaintProperty(layerId, "line-opacity", opacity);
    }
    // also for vector helper line layer
    const lineId = layerId + "_line";
    if (map.getLayer(lineId)) map.setPaintProperty(lineId, "line-opacity", opacity);
  }

  // --- Time UI ---------------------------------------------------------------
  function buildTimeUI(cfg) {
    const timebox = $("#timebox");
    timebox.innerHTML = "";
    const min = cfg.time?.min ?? 1700;
    const max = cfg.time?.max ?? 2100;
    const cur = clampYear(cfg.defaultYear ?? min, cfg);

    const label = el("div", { style: { display: "flex", alignItems: "center", gap: "8px", marginBottom: "6px" } }, [
      el("strong", { style: { fontSize: "13px" } }, ["Year:"]),
      el("span", { id: "yearLabel", style: { fontVariantNumeric: "tabular-nums" } }, [String(cur)])
    ]);
    const slider = el("input", {
      id: "yearSlider", type: "range", min: String(min), max: String(max), value: String(cur),
      style: { width: "100%" },
      oninput: (e) => {
        const y = clampYear(parseInt(e.target.value, 10), cfg);
        $("#yearLabel").textContent = String(y);
        updateYear(y, window.KFM?.map);
      }
    });
    timebox.append(label, slider);
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
      setLayerVisibility(map, l.id, active && l.visibility);
    });
  }

  // --- Layer UI --------------------------------------------------------------
  function buildLayerUI(cfg, map) {
    const layerbox = $("#layerbox");
    layerbox.innerHTML = "";
    const groups = groupBy((cfg.layers || []), (l) => l.group || "Layers");
    Object.entries(groups).forEach(([groupName, ls]) => {
      const groupEl = el("details", { open: true, style: { marginBottom: "10px" } }, [
        el("summary", { style: { cursor: "pointer", fontWeight: "600", marginBottom: "6px" } }, [groupName])
      ]);
      ls.forEach((l) => {
        const row = el("div", { style: { display: "grid", gridTemplateColumns: "24px 1fr 60px", gap: "6px", alignItems: "center", marginBottom: "6px" } }, [
          el("input", {
            type: "checkbox",
            checked: l.visibility !== false,
            onchange: (e) => setLayerVisibility(map, l.id, e.target.checked)
          }),
          el("label", { style: { fontSize: "13px", cursor: "pointer" }, for: `chk_${l.id}` }, [
            l.title || l.id,
            el("span", { style: { color: "#999", marginLeft: "6px", fontSize: "11px" } },
              timeBadge(l))
          ]),
          el("input", {
            type: "range", min: "0", max: "1", step: "0.05", value: String(l.opacity ?? 1),
            oninput: (e) => setLayerOpacity(map, l.id, parseFloat(e.target.value))
          })
        ]);
        groupEl.appendChild(row);
        // Add to map now so we can immediately control it
        addLayerToMap(map, state.layersById.get(l.id));
      });
      layerbox.appendChild(groupEl);
    });
  }

  function timeBadge(l) {
    const s = l.start ?? l.year ?? l.time?.start;
    const e = l.end ?? l.year ?? l.time?.end;
    if (s == null && e == null) return [""];
    if (s != null && e != null && s === e) return [`[${s}]`];
    if (s != null && e != null) return [`[${s}–${e}]`];
    if (s != null) return [`[≥${s}]`];
    return [`[≤${e}]`];
  }

  function groupBy(arr, keyFn) {
    return arr.reduce((acc, v) => {
      const k = keyFn(v);
      (acc[k] = acc[k] || []).push(v);
      return acc;
    }, {});
  }

  // --- Kickoff ---------------------------------------------------------------
  document.readyState === "loading" ? document.addEventListener("DOMContentLoaded", init) : init();
})();

