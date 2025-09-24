// web/components/popup.js
// Kansas-Frontier-Matrix — Map Popup Component (MapLibre GL JS)
// -------------------------------------------------------------
// Features:
// - Safe HTML (basic escaping) to avoid injection
// - Works with point/click + queryRenderedFeatures cluster handling
// - Flexible field mapping (title/meta/desc/link), with fallbacks
// - Tiny utilities: date formatting, truncation, coord formatting
//
// Usage:
// import { attachPopup } from "./components/popup.js";
// attachPopup(map, { layers: ["events", "places"], maxFeatures: 8 });
//
// Or build manually:
// import { buildPopupHTML } from "./components/popup.js";
// new maplibregl.Popup().setLngLat([lng, lat]).setHTML(buildPopupHTML([feature])).addTo(map);

function esc(str = "") {
  return String(str)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#39;");
}

function isURL(s) {
  try {
    const u = new URL(s);
    return ["http:", "https:"].includes(u.protocol);
  } catch {
    return false;
  }
}

function fmtDate(v) {
  // Accepts year, iso date, or partial; returns compact label
  if (v == null) return "";
  const s = String(v).trim();
  if (/^\d{4}-\d{2}-\d{2}/.test(s)) {
    const d = new Date(s);
    if (!isNaN(d)) {
      return d.toLocaleDateString(undefined, { year: "numeric", month: "short", day: "numeric" });
    }
  }
  if (/^\d{4}-\d{2}/.test(s)) return s; // YYYY-MM
  if (/^\d{4}$/.test(s)) return s;      // YYYY
  return s;
}

function fmtCoord([lng, lat]) {
  const n = (x) => (Math.round(x * 10000) / 10000).toFixed(4);
  return `${n(lat)}°, ${n(lng)}°`;
}

function trunc(s, max = 240) {
  s = String(s || "");
  return s.length > max ? s.slice(0, max - 1) + "…" : s;
}

function pick(props, keys = []) {
  for (const k of keys) {
    if (props[k] != null && props[k] !== "") return props[k];
  }
  return undefined;
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
 */
function renderItem(feature, fields) {
  const p = feature?.properties || {};

  const title = pick(p, fields.title) ?? "(untitled)";
  const meta = pick(p, fields.meta);
  const date = fmtDate(pick(p, fields.date));
  const desc = trunc(pick(p, fields.desc) ?? "", 480);
  const link = pick(p, fields.link);

  // Optional: include layer id as a faint badge to help debugging mixed clicks
  const layerId = feature?.layer?.id;

  let headerMeta = [meta, date].filter(Boolean).join(" • ");

  return `
    <div class="kfm-popup-item">
      <div class="kfm-popup-title">${esc(title)}</div>
      ${headerMeta ? `<div class="kfm-popup-meta">${esc(headerMeta)}</div>` : ""}
      ${desc ? `<div class="kfm-popup-desc">${esc(desc)}</div>` : ""}
      <div class="kfm-popup-actions">
        ${isURL(link) ? `<a class="kfm-popup-link" target="_blank" rel="noopener" href="${esc(link)}">Open source</a>` : ""}
        ${layerId ? `<span class="kfm-badge" title="Layer">${esc(layerId)}</span>` : ""}
      </div>
    </div>
  `;
}

/**
 * Build full popup HTML for one or many features.
 * @param {Array<Feature>} features - GeoJSON-like features
 * @param {Object} options
 *  - fields: {title,meta,date,desc,link} arrays of property keys
 *  - lngLat: [lng, lat] to show coordinates (optional)
 *  - heading: custom header string (optional)
 *  - maxItems: clamp list length for multi features
 */
export function buildPopupHTML(features = [], options = {}) {
  const fields = {
    title: options.fields?.title || DEFAULT_FIELDS.title,
    meta: options.fields?.meta || DEFAULT_FIELDS.meta,
    date: options.fields?.date || DEFAULT_FIELDS.date,
    desc: options.fields?.desc || DEFAULT_FIELDS.desc,
    link: options.fields?.link || DEFAULT_FIELDS.link
  };
  const maxItems = Number.isFinite(options.maxItems) ? options.maxItems : 8;

  const items = features.slice(0, maxItems).map((f) => renderItem(f, fields)).join("");

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
 * Attach click popups to a set of layers.
 * - Collects features from the clicked pixel across provided layers
 * - Deduplicates by feature id+layer
 * - Builds a consolidated popup
 *
 * @param {maplibregl.Map} map
 * @param {Object} opts
 *  - layers: array of layer ids to query (required)
 *  - padding: pixel tolerance for queryRenderedFeatures (default 4)
 *  - maxFeatures: clamp for multi feature popup (default 8)
 *  - fields: override field map (see buildPopupHTML)
 *  - makeHeading: fn(features) -> string (optional)
 */
export function attachPopup(map, opts = {}) {
  const layers = opts.layers || [];
  const padding = Number.isFinite(opts.padding) ? opts.padding : 4;
  const maxFeatures = Number.isFinite(opts.maxFeatures) ? opts.maxFeatures : 8;

  let popup = new maplibregl.Popup({
    closeButton: true,
    closeOnClick: true,
    maxWidth: "360px",
    offset: 12
  });

  function onClick(e) {
    if (!layers.length) return;

    const bbox = [
      [e.point.x - padding, e.point.y - padding],
      [e.point.x + padding, e.point.y + padding]
    ];

    const feats = map.queryRenderedFeatures(bbox, { layers }).filter(Boolean);

    if (!feats.length) return;

    // Deduplicate by (layer:id || generated)
    const seen = new Set();
    const dedup = [];
    for (const f of feats) {
      const key = `${f.layer?.id ?? "layer"}:${f.id ?? JSON.stringify(f.geometry)}`;
      if (seen.has(key)) continue;
      seen.add(key);
      dedup.push(f);
    }

    const heading =
      typeof opts.makeHeading === "function" ? opts.makeHeading(dedup) :
      (dedup.length > 1 ? `${dedup.length} items` : undefined);

    const html = buildPopupHTML(dedup, {
      fields: opts.fields,
      maxItems: maxFeatures,
      lngLat: [e.lngLat.lng, e.lngLat.lat],
      heading
    });

    popup.setLngLat(e.lngLat).setHTML(html).addTo(map);
  }

  map.on("click", onClick);

  // Return a small controller so callers can remove or rebuild popups if needed
  return {
    remove() {
      map.off("click", onClick);
      try { popup.remove(); } catch {}
    },
    setLayers(nextLayers = []) {
      // update layer list for subsequent clicks
      opts.layers = Array.isArray(nextLayers) ? nextLayers : [];
    }
  };
}

/**
 * Optional helper to wire a single-symbol layer with a specific click behavior.
 * If you need per-layer custom popups, call this instead of attachPopup().
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
    const html = buildPopupHTML([feats[0]], {
      fields: options.fields,
      lngLat: [e.lngLat.lng, e.lngLat.lat]
    });
    popup.setLngLat(e.lngLat).setHTML(html).addTo(map);
  }

  map.on("click", layerId, onClick);

  return {
    remove() {
      map.off("click", layerId, onClick);
      try { popup.remove(); } catch {}
    }
  };
}

