<!--
📍 Path: web/src/assets/map/data/extents/README.md
-->

# 🗺️ Map Extents (BBox) — UI Navigation + Spatial Query Helpers

> [!NOTE]
> **Extents** are small, versioned *UI assets* that describe **named bounding boxes** (bbox) used by the web map to:
> - jump/fly to a region 🧭
> - fit the viewport consistently 🖼️
> - drive bbox-based API requests 🔎

---

## ✨ What lives in this folder?

**This folder contains “extent definitions”** (usually JSON) for geographic regions that the UI needs to reference often.

Typical examples:
- 🟦 Kansas (statewide)
- 🏙️ Metro areas (Wichita / KC / Topeka)
- 🏜️ Dust Bowl focus regions (storytelling presets)
- 🧪 Analysis windows for performance-friendly querying (smaller bboxes)

---

## 🧠 Why extents exist (KFM-flavored)

KFM is a **map + narrative UI** system, and it frequently needs to:
- snap the map to a known place/region (for story beats, UI presets, search scopes)
- use **bbox filters** when searching datasets, streaming GeoJSON, or running spatial queries
- keep these regions **consistent and reusable** across components (no “random bbox in random file”)

Extents are intentionally:
- ✅ small
- ✅ stable (IDs don’t change lightly)
- ✅ UI-friendly (include optional `center` / `zoom` hints when helpful)

---

## 🗂️ Expected folder shape

```text
📦 web/
└─ 🧩 src/
   └─ 🗺️ assets/
      └─ 🧭 map/
         └─ 📚 data/
            └─ 📦 extents/
               ├─ ✅ README.md
               ├─ 🗂️ *.json                # extent files (one per region) OR a single index file
               └─ 🧪 (optional) *_test.*    # lightweight fixtures/tests if the project uses them
```

> [!TIP]
> Keep extents **as data** (not code) whenever possible — it makes them easier to review, diff, and reuse.

---

## 📐 BBox conventions (non-negotiable)

### ✅ Coordinate order
We use the standard bbox order:

```text
[west, south, east, north]
[minLng, minLat, maxLng, maxLat]
```

### ✅ Coordinate system
Use **WGS84 / lon-lat degrees** (commonly written as `EPSG:4326`).

### ✅ Valid ranges
- Longitude: `-180 … 180`
- Latitude: `-90 … 90`

### ✅ Kansas is safe… but still:
Even though Kansas doesn’t cross the antimeridian, keep the rules consistent so the system stays portable.

---

## 🧾 Data contract (recommended)

> [!IMPORTANT]
> The project may evolve the exact shape. This README defines a **recommended** contract for extents stored in `assets/`.

### ✅ Minimum viable extent (MVE)

```json
{
  "id": "ks_state",
  "label": "Kansas (Statewide)",
  "bbox": [-102.05, 36.99, -94.59, 40.00],
  "crs": "EPSG:4326"
}
```

### ⭐ Full-featured extent (recommended)

```json
{
  "id": "ks_state",
  "label": "Kansas (Statewide)",
  "description": "Default statewide extent used by the home view and story reset actions.",
  "bbox": [-102.05, 36.99, -94.59, 40.00],
  "crs": "EPSG:4326",

  "center": [-98.0, 38.5],
  "zoom": 6,

  "tags": ["kansas", "state", "default"],
  "paddingPx": 24,

  "provenance": {
    "source": "Derived from authoritative boundary geometry (preferred) or curated UI bbox.",
    "notes": "If derived, capture the dataset/story that produced this extent."
  }
}
```

### 📋 Field meanings

| Field | Type | Required | Meaning |
|------:|------|:--------:|---------|
| `id` | `string` | ✅ | Stable key used in code/config (`snake_case` recommended) |
| `label` | `string` | ✅ | Human-readable name for menus/UI |
| `bbox` | `[number, number, number, number]` | ✅ | `[west, south, east, north]` (lon/lat) |
| `crs` | `string` | ✅ | `"EPSG:4326"` |
| `description` | `string` | ⛔ | UI tooltip/help text |
| `center` | `[number, number]` | ⛔ | `[lng, lat]` fallback for camera fly-to |
| `zoom` | `number` | ⛔ | fallback zoom (useful for story presets) |
| `paddingPx` | `number` | ⛔ | preferred padding for fit-bounds |
| `tags` | `string[]` | ⛔ | simple grouping/filtering |
| `provenance` | `object` | ⛔ | traceability notes (what boundary/logic produced it) |

---

## 🧩 How the UI should use extents

### 1) Fit the map to bbox 🧷

Most map libs accept a SW/NE pair (or equivalent) derived from bbox:

```ts
// bbox = [west, south, east, north]
const [[west, south], [east, north]] = [[bbox[0], bbox[1]], [bbox[2], bbox[3]]];

// Example (pseudo-code):
map.fitBounds([[west, south], [east, north]], { padding: paddingPx ?? 24 });
```

### 2) Drive bbox-based API calls 🔎

Extents are perfect for:
- dataset discovery inside an area
- limiting feature streaming
- safe spatial query scopes
- story search scopes (when stories are geo-filterable)

> [!TIP]
> **Always** consider bbox scoping for performance. Smaller windows → faster responses and fewer features to render.

---

## 🛠️ Adding a new extent (checklist)

### ✅ Step-by-step

1) **Pick a stable ID**
   - `snake_case`
   - avoid year-specific IDs unless truly needed (`dust_bowl_1935_sw_ks` is okay if it’s a permanent story preset)

2) **Derive bbox from a real geometry when possible**
   - preferred: authoritative boundary geometry (county/state/region polygon)
   - acceptable: curated UI box (document why)

3) **Add padding**
   - don’t make it razor-thin; tiny bboxes cause frequent clipping
   - if the UI supports `paddingPx`, store it here

4) **Write the JSON**
   - keep keys ordered and readable
   - keep numeric precision reasonable (≤ 6 decimals)

5) **Wire it into the UI registry (if applicable)**
   - if the UI uses an index file or registry module, add your new extent there

---

## ✅ Validation rules (fast sanity checks)

> [!WARNING]
> Invalid extents cause subtle bugs (infinite zoom, upside-down view, empty results).

### Must be true
- `west < east`
- `south < north`
- all numbers are finite
- lon/lat ranges are valid

### Optional tiny validator snippet 🧪

<details>
<summary>🧪 Minimal JS validator (copy/paste)</summary>

```js
function validateExtent(ext) {
  const b = ext?.bbox;
  if (!Array.isArray(b) || b.length !== 4) return "bbox must be [w,s,e,n]";
  const [w, s, e, n] = b.map(Number);
  if (![w, s, e, n].every(Number.isFinite)) return "bbox values must be finite numbers";
  if (!(w < e)) return "west must be < east";
  if (!(s < n)) return "south must be < north";
  if (w < -180 || w > 180 || e < -180 || e > 180) return "longitude out of range";
  if (s < -90 || s > 90 || n < -90 || n > 90) return "latitude out of range";
  return null;
}
```

</details>

---

## 🧷 Naming conventions

✅ Good:
- `ks_state.json`
- `ks_southwest.json`
- `wichita_metro.json`
- `smoky_hills_region.json`

🚫 Avoid:
- `Extent1.json`
- `final_final_extent.json`
- `bbox-kansas-latest.json` (extents should be versioned in git, not via filename chaos 😅)

---

## 📚 Glossary

- **Extent**: a named region used by the UI (typically represented by a bbox).
- **BBox (bounding box)**: `[west, south, east, north]` in lon/lat degrees.
- **CRS**: Coordinate Reference System (here: WGS84 / EPSG:4326).
- **Fit bounds**: map operation that changes camera so a bbox is fully visible.

---

## 🧭 Design principle

> [!IMPORTANT]
> **One place for one truth.**  
> If the UI needs a commonly used region, define it here once and reuse it everywhere.
