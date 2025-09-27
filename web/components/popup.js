// web/components/popup.js
// Kansas-Frontier-Matrix — Map Popup Component (MapLibre GL JS)
// -------------------------------------------------------------
// Features:
// - Escape-safe HTML
// - Point/click, bbox-query with padding; dedupe across layers
// - Flexible field mapping (title/meta/date/desc/link) + custom renderer
// - Optional: cluster zoom, feature highlight via setFeatureState
// - Utilities: date/coord formatting, truncation, geometry centroid
//
// Usage:
//   import { attachPopup } from "./components/popup.js";
//   attachPopup(map, { layers: ["events","places"], maxFeatures: 8 });
//
//   // Per-layer popup:
//   import { attachLayerPopup } from "./components/popup.js";
//   attachLayerPopup(map, "events");
//
//   // With cluster expansion:
//   attachPopup(map, { layers: ["events_points"], clusterSourceId: "events_src" });
//
//   // With highlight (your layer paints must read feature-state {selected: true}):
//   attachPopup(map, { layers: ["trails_line"], highlight: true });

function esc(str = "") {
  return String(str)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#39;");
}

function cleanURL(s) {
  if (!s && s !== 0) return null;
  try {
    const u = new URL(String(s).trim());
    return (u.protocol === "http:" || u.protocol === "https:") ? u.toString() : null;
  } catch { return null; }
}

function fmtDate(v) {
  if (v == null) return "";
  const s = String(v).trim();
  if (/^\d{4}-\d{2}-\d{2}/.test(s)) {
    const d = new Date(s);
    if (!isNaN(d)) {
      return d.toLocaleDateString(undefined, { year: "numeric", month: "short", day: "numeric" });
    }
  }
  if (/^\d{4}-\d{2}$/.test(s)) return s; // YYYY-MM
  if (/^\d{4}$/.test(s)) return s;      // YYYY
  return s;
}

function fmtCoord([lng, lat]) {
  const n = (x) => (Math.round(x * 10000) / 10000).toFixed(4);
  return `${n(lat)}°, ${n(lng)}°`;
}

function trunc(s, max = 240) {
  s = String(s ?? "");
  return s.length > max ? s.slice(0, max - 1) + "…" : s;
}

function pick(props, keys = []) {
  for (const k of keys) {
    if (props?.[k] != null && props[k] !== "") return props[k];
  }
  return undefined;
}

// Rough centroid for points/lines/polys for drop location when using geometry click
function centroidOf(feature) {
  try {
    const g = feature?.geometry;
    if (!g) return null;
    if (g.type === "Point") return g.coordinates;
    if (g.type === "MultiPoint") return g.coordinates[0] ?? null;
    if (g.type === "LineString") return g.coordinates[Math.floor(g.coordinates.length / 2)] ?? null;
    if (g.type === "MultiLineString") return g.coordinates[0]?.[Math.floor((g.coordinates[0].length || 1) / 2)] ?? null;
    if (g.type === "Polygon") return g.coordinates[0]?.[0] ?? null;
    if (g.type === "MultiPolygon") return g.coordinates[0]?.[0]?.[0] ?? null;
  } catch {}
  return null;
}

/**
 * Map between typical property names and the semantic slots we display.
 * Override via options.fields.{title,meta,date,desc,link}
 */
const DEFAULT_FIELDS = {
  title: ["title", "name", "label", "site_name", "map_name"],
  meta: ["place", "county", "layer", "type", "category"],
  date: ["date", "year", "start_date"],
  desc: ["description", "summary", "notes", "text"],
  link: ["url", "doc_url", "source_url", "href"]
};

/**
 * Build one item block for a single feature.
 * Provide options.renderItem(feature, fields) to fully override.
 */
function renderItem(feature, fields, { debug = false } = {}) {
  const p = feature?.properties || {};

  const title = pick(p, fields.title) ?? "(untitled)";
  const meta = pick(p, fields.meta);
  const date = fmtDate(pick(p, fields.date));
  const desc = trunc(pick(p, fields.desc) ?? "", 480);
  const link = cleanURL(pick(p, fields.link));
  const layerId = feature?.layer?.id;

  const headerMeta = [meta, date].filter(Boolean).join(" • ");

  const dbg = debug ? renderDebugTable(p) : "";

  return `
    <div class="kfm-popup-item">
      <div class="kfm-popup-title">${esc(title)}</div>
      ${headerMeta ? `<div class="kfm-popup-meta">${esc(headerMeta)}</div>` : ""}
      ${desc ? `<div class="kfm-popup-desc">${esc(desc)}</div>` : ""}
      <div class="kfm-popup-actions">
        ${link ? `<a class="kfm-popup-link" target="_blank" rel="noopener" href="${esc(link)}">Open source</a>` : ""}
        ${layerId ? `<span class="kfm-badge" title="Layer">${esc(layerId)}</span>` : ""}
      </div>
      ${dbg}
    </div>
  `;
}

function renderDebugTable(props) {
  try {
    const rows = Object.entries(props || {}).slice(0, 30)
      .map(([k, v]) => `<tr><th>${esc(k)}</th><td>${esc(Array.isArray(v) ? v.join(", ") : String(v))}</td></tr>`)
      .join("");
    return `<details class="kfm-popup-debug"><summary>Properties</summary><table>${rows}</table></details>`;
  } catch { return ""; }
}

/**
 * Build full popup HTML for one or many features.
 * @param {Array<Feature>} features
 * @param {Object} options
 *  - fields: {title,meta,date,desc,link}
 *  - lngLat: [lng, lat] to show coordinates (optional)
 *  - heading: custom header string (optional)
 *  - maxItems: clamp list length for multi features
 *  - renderItem: fn(feature, fields, {debug}) => string (override)
 *  - debug: boolean to include a properties table
 */
export function buildPopupHTML(features = [], options = {}) {
  const fields = {
    title: options.fields?.title || DEFAULT_FIELDS.title,
    meta:  options.fields?.meta  || DEFAULT_FIELDS.meta,
    date:  options.fields?.date  || DEFAULT_FIELDS.date,
    desc:  options.fields?.desc  || DEFAULT_FIELDS.desc,
    link:  options.fields?.link  || DEFAULT_FIELDS.link
  };
  const maxItems = Number.isFinite(options.maxItems) ? options.maxItems : 8;
  const render = typeof options.renderItem === "function"
    ? (f) => options.renderItem(f, fields, { debug: !!options.debug })
    : (f) => renderItem(f, fields, { debug: !!options.debug });

  const items = features.slice(0, maxItems).map(render).join("");

  const coord = Array.isArray(options.lngLat) ? `
    <div class="kfm-popup-meta">${esc(fmtCoord(options.lngLat))}</div>
  ` : "";

  const header = options.heading
    ? `<div class="kfm-popup-title">${esc(options.heading)}</div>`
    : "";

  const more =
    features.length > maxItems
      ? `<div class="kfm-popup-meta">+${features.length - maxItems} more… zoom in or refine selection</div>`
      : "";

  return `
    <div class="kfm-popup">
      ${header}
      ${coord}
      ${items}
      ${more}
    </div>
  `;
}

/**
 * Attach click popups across multiple layers, with optional cluster expand and highlight.
 *
 * @param {maplibregl.Map} map
 * @param {Object} opts
 *  - layers: array<string> layer ids to query (required)
 *  - padding: number px tolerance for queryRenderedFeatures bbox (default 4)
 *  - maxFeatures: number to clamp list (default 8)
 *  - fields: override field map (see buildPopupHTML)
 *  - makeHeading: fn(features) -> string (optional)
 *  - renderItem: fn(feature, fields, {debug}) -> string (optional)
 *  - debug: boolean show properties table (optional)
 *  - dedupeKey: fn(feature) -> string (optional)
 *  - clusterSourceId: string GeoJSON source id with clustering enabled; will expand on cluster click
 *  - highlight: boolean use setFeatureState({selected:true}) on clicked features (requires paint wiring)
 */
export function attachPopup(map, opts = {}) {
  const layers = Array.isArray(opts.layers) ? opts.layers : [];
  const padding = Number.isFinite(opts.padding) ? opts.padding : 4;
  const maxFeatures = Number.isFinite(opts.maxFeatures) ? opts.maxFeatures : 8;
  const clusterSourceId = opts.clusterSourceId || null;
  const highlight = !!opts.highlight;

  let popup = new maplibregl.Popup({
    closeButton: true,
    closeOnClick: true,
    maxWidth: "360px",
    offset: 12
  });

  // Track highlighted state across clicks for cleanup
  const highlighted = [];

  function clearHighlight() {
    try {
      for (const h of highlighted) {
        map.setFeatureState({ source: h.source, sourceLayer: h.sourceLayer, id: h.id }, { selected: false });
      }
    } catch {}
    highlighted.length = 0;
  }

  function dedupe(feats) {
    const kfn = typeof opts.dedupeKey === "function"
      ? opts.dedupeKey
      : (f) => `${f.layer?.source || "src"}:${f.layer?.sourceLayer || f.layer?.id || "layer"}:${f.id ?? JSON.stringify(f.geometry)}`;
    const seen = new Set();
    const out = [];
    for (const f of feats) {
      const key = kfn(f);
      if (seen.has(key)) continue;
      seen.add(key);
      out.push(f);
    }
    return out;
  }

  async function handleClusterClick(firstFeature, lngLat) {
    try {
      const source = map.getSource(clusterSourceId);
      if (!source || typeof source.getClusterExpansionZoom !== "function") return false;
      const clusterId = firstFeature?.properties?.cluster_id;
      if (clusterId == null) return false;
      const zoom = await new Promise((res, rej) => {
        source.getClusterExpansionZoom(clusterId, (err, z) => err ? rej(err) : res(z));
      });
      map.easeTo({ center: [lngLat.lng, lngLat.lat], zoom });
      return true;
    } catch { return false; }
  }

  function onClick(e) {
    if (!layers.length) return;

    // Query a small bbox for fatter finger clicks
    const bbox = [
      [e.point.x - padding, e.point.y - padding],
      [e.point.x + padding, e.point.y + padding]
    ];
    const feats = map.queryRenderedFeatures(bbox, { layers }).filter(Boolean);
    if (!feats.length) return;

    // Cluster handling (first feature wins for expansion)
    if (clusterSourceId && feats[0]?.properties?.cluster) {
      handleClusterClick(feats[0], e.lngLat);
      return;
    }

    const dedup = dedupe(feats);

    // Optional highlight (requires your style to use ["feature-state","selected"])
    if (highlight) {
      clearHighlight();
      for (const f of dedup) {
        if (f?.id == null) continue; // setFeatureState needs stable id
        try {
          map.setFeatureState(
            { source: f.layer?.source, sourceLayer: f.layer?.sourceLayer, id: f.id },
            { selected: true }
          );
          highlighted.push({ source: f.layer?.source, sourceLayer: f.layer?.sourceLayer, id: f.id });
        } catch {}
      }
    }

    // Heading (custom or count)
    const heading =
      typeof opts.makeHeading === "function" ? opts.makeHeading(dedup) :
      (dedup.length > 1 ? `${dedup.length} items` : undefined);

    // Place popup at click; for non-points, optionally use geom centroid for a nicer anchor
    const anchorLngLat = (() => {
      if (dedup.length === 1) {
        const c = centroidOf(dedup[0]);
        if (Array.isArray(c) && Number.isFinite(c[0]) && Number.isFinite(c[1])) {
          return { lng: c[0], lat: c[1] };
        }
      }
      return e.lngLat;
    })();

    const html = buildPopupHTML(dedup, {
      fields: opts.fields,
      maxItems: maxFeatures,
      lngLat: [anchorLngLat.lng, anchorLngLat.lat],
      heading,
      renderItem: opts.renderItem,
      debug: !!opts.debug
    });

    popup.setLngLat(anchorLngLat).setHTML(html).addTo(map);
  }

  function onMove() {
    // Optional: close + clear highlight when user pans
    try { popup.remove(); } catch {}
    if (highlight) clearHighlight();
  }

  map.on("click", onClick);
  map.on("dragstart", onMove);

  return {
    remove() {
      map.off("click", onClick);
      map.off("dragstart", onMove);
      try { popup.remove(); } catch {}
      clearHighlight();
    },
    setLayers(nextLayers = []) {
      opts.layers = Array.isArray(nextLayers) ? nextLayers : [];
    }
  };
}

/**
 * Attach a simple popup for a single layer id.
 * Accepts same options as buildPopupHTML (fields/renderItem/debug), plus:
 *  - centroidAnchor: boolean (default true) — anchor popup to geometry centroid when not a Point
 */
export function attachLayerPopup(map, layerId, options = {}) {
  let popup = new maplibregl.Popup({
    closeButton: true,
    closeOnClick: true,
    maxWidth: "360px",
    offset: 12
  });

  function onClick(e) {
    const feats = map.queryRenderedFeatures(e.point, { layers: [layerId] });
    if (!feats?.length) return;

    const f = feats[0];
    const anchor = (options.centroidAnchor !== false && f?.geometry?.type !== "Point")
      ? (() => {
          const c = centroidOf(f);
          return Array.isArray(c) ? { lng: c[0], lat: c[1] } : e.lngLat;
        })()
      : e.lngLat;

    const html = buildPopupHTML([f], {
      fields: options.fields,
      lngLat: [anchor.lng, anchor.lat],
      renderItem: options.renderItem,
      debug: !!options.debug
    });
    popup.setLngLat(anchor).setHTML(html).addTo(map);
  }

  map.on("click", layerId, onClick);

  return {
    remove() {
      map.off("click", layerId, onClick);
      try { popup.remove(); } catch {}
    }
  };
}

// Provide global for app.js optional wiring (`if (typeof window.attachPopup === "function") ...`)
if (typeof window !== "undefined") {
  window.attachPopup = window.attachPopup || attachPopup;
}
