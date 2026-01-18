# UI JSON Schemas (Samples) 🧩

![JSON Schema](https://img.shields.io/badge/JSON%20Schema-2020--12-informational)
![Contract-first](https://img.shields.io/badge/Contract--First-%E2%9C%85-success)
![Provenance-first](https://img.shields.io/badge/Provenance--First-%F0%9F%93%9C-blue)
![Focus Mode](https://img.shields.io/badge/Focus%20Mode-Hard%20Gates-orange)

This folder contains **JSON Schemas** used to validate **sample UI configuration assets** shipped with the web app (ex: Story Node JSON “steps”, map/timeline presets, Focus Mode UI configs). The goal is simple:

> **If it shows up in the UI, it must be structured, predictable, and provenance-resolvable.** ✅

---

## 📦 Where you are

```text
📁 web/assets/samples/_shared/schemas/ui/
├─ 📄 README.md   👈 you are here
└─ 📄 *.schema.json
```

These are **sample-asset schemas**, meant to keep `web/assets/samples/**` coherent and safe to load in dev, demos, docs, and tests.

---

## 🧭 Why UI schemas exist in KFM

KFM uses a **contract-first + provenance-first** approach: anything the UI renders should be traceable to cataloged sources and processing, and “mystery layers” are not allowed. ✅

In practice, this matters a lot for **Story Mode**:

- Stories are authored as **Markdown + JSON config**.
- The JSON provides UI instructions like:  
  **“at step 2, activate layer X & Y, set map camera to `[lon, lat, zoom]`, set timeline to year `1935`.”** 🗺️🕰️
- The front-end applies these instructions via the map engine APIs (ex: MapLibre/Cesium).  

Schemas make story configs:
- **author-friendly** (non-devs can fill templates)
- **machine-validated** (CI can block invalid configs)
- **safer by design** (hard gates against unsourced / sensitive leakage)

---

## 🛡️ Focus Mode hard gates (must not regress)

Focus Mode is the interactive reading experience where a Story Node is shown alongside map + timeline context. It has **strict trust rules** that the UI and configs must respect:

- **Only provenance-linked content**  
  If it’s not in the catalogs/graph with provenance, it doesn’t appear. 🚫
- **AI is opt-in + clearly labeled**  
  AI-generated content must never show by default, must be user-triggered, and must be labeled + include uncertainty/confidence. 🤖🏷️
- **No sensitive location leaks**  
  Sensitive locations must be generalized/omitted so the UI can’t become a side-channel around sovereignty/safety rules. 🕊️🧭

**Schema implication:** any config that can affect what gets shown must carry enough structure to:
- resolve to provenance IDs (catalog references),
- mark AI blocks explicitly,
- and carry sensitivity hints that downstream renderers must enforce.

---

## ✅ Schema conventions (how we write schemas here)

### 1) File naming 📄
- Prefer `kebab-case.schema.json`
- Keep schema scope tight:
  - `story-config.schema.json` ✅
  - `map-view.schema.json` ✅
  - `focus-mode-panel.schema.json` ✅

### 2) Schema headers 🧷
Every schema should include:
- `$schema` (recommend: 2020-12)
- `$id` (stable, unique within repo)
- `title`, `description`
- `type`
- `additionalProperties: false` (default rule unless there’s a reason)

### 3) Reuse `$defs` ♻️
Put shared shapes in `$defs` and reference them with `$ref`:
- camera tuple/object
- timeline state
- provenance reference
- sensitivity classification
- “UI step action” union types (via `oneOf`)

### 4) Be explicit about “allowed unknowns” 🧠
If a schema must allow extension, do it deliberately:
- Prefer: `x-kfm-*` fields for experimental/forward-compatible metadata
- Avoid: unbounded free-form objects in top-level configs

---

## 🧱 Common schema building blocks

These are the recurring “shapes” most UI configs need.

> The exact filenames/types may differ per schema file, but these concepts should remain stable.

### 🗺️ Map camera / view
KFM story configs often use a simple tuple for camera targeting:

- `camera: [lon, lat, zoom]`

Schema guidance:
- `lon`: `-180..180`
- `lat`: `-90..90`
- `zoom`: `0..24` (or whatever the renderer supports)

Optionally support a richer object form later (bearing/pitch):

- `{ "lon": -98.5, "lat": 38.5, "zoom": 6, "bearing": 0, "pitch": 0 }`

### 🧭 Layer toggles
A Story Step should be able to declare:
- which layers must be **on**
- which layers must be **off**
- optional styling: opacity/filters, etc.

### 🕰️ Timeline state
Story steps commonly need:
- a year (single point),
- or a range (start/end),
- or a named preset (“DustBowlEra”, etc.)

### 📎 Provenance references
Any visual or narrative element that depends on data should reference something resolvable:
- a dataset ID (DCAT-style)
- an asset/item ID (STAC-style)
- a graph entity ID (stable identifier)
- a provenance activity/process ID (PROV-style)

### 🕊️ Sensitivity / sovereignty hints
Configs must be able to express:
- “public ok”
- “generalize location”
- “omit exact geometry”
- “redact details unless role-based access allows”

Even if enforcement is runtime, **schemas should make it hard to forget to declare sensitivity**.

---

## ✨ Example: Story JSON config (validated by a schema)

Below is a **representative** story config shape. Use it as a mental model for the schemas in this folder.

```json
{
  "$schema": "./story-config.schema.json",
  "id": "dust-bowl-intro",
  "title": "Dust Bowl: Kansas in the 1930s",
  "summary": "A guided tour through drought, land use, and migration patterns.",
  "steps": [
    {
      "id": "s1",
      "title": "Before the crisis",
      "map": {
        "camera": [-98.5, 38.5, 5.6],
        "layers": { "on": ["rainfall_1920s"], "off": ["dust_storm_reports"] }
      },
      "timeline": { "year": 1925 },
      "provenance": {
        "datasets": ["dcat:rainfall_normals_v1"],
        "entities": ["graph:region.kansas"]
      }
    },
    {
      "id": "s2",
      "title": "1935: conditions worsen",
      "map": {
        "camera": [-99.2, 38.2, 6.3],
        "layers": { "on": ["rainfall_1930s", "migration_by_county_1935"] }
      },
      "timeline": { "year": 1935 },
      "provenance": {
        "datasets": ["dcat:rainfall_timeseries_v2", "dcat:migration_by_county_v1"],
        "entities": ["graph:event.dust_bowl"]
      }
    }
  ]
}
```

---

## 🧪 Validating configs locally

Schemas are meant to be enforceable in CI, but you should also validate locally.

### Option A: Ajv (Node) ⚙️
```ts
// validate-ui-config.ts (example)
import Ajv from "ajv";
import addFormats from "ajv-formats";
import schema from "./story-config.schema.json" assert { type: "json" };
import config from "./dust-bowl-intro.story.json" assert { type: "json" };

const ajv = new Ajv({ allErrors: true, strict: false });
addFormats(ajv);

const validate = ajv.compile(schema);
const ok = validate(config);

if (!ok) {
  console.error(validate.errors);
  process.exit(1);
}

console.log("✅ UI config valid");
```

### Option B: CI gate 🔒
Recommended CI behavior (conceptually):
- validate all `web/assets/samples/**/*.json` against the correct schema(s)
- fail fast on:
  - schema violations
  - missing provenance references
  - AI blocks not explicitly labeled
  - disallowed sensitive-location precision

---

## 🧰 Adding or changing a UI schema

Checklist for PRs:

- [ ] Schema includes `$schema`, `$id`, `title`, `description`
- [ ] `additionalProperties: false` is applied at key object levels
- [ ] Reusable shapes moved into `$defs`
- [ ] Examples exist (at least one JSON file that validates)
- [ ] Story/Focus Mode configs include provenance references where applicable
- [ ] Sensitive-location rules are representable (and not bypassable via config)
- [ ] Any new UI layer includes a path to attribution/metadata display (source + license)

---

## 🚫 Common gotchas

- **“It renders in dev, so it’s fine.”**  
  Not enough — sample assets must validate so they remain stable across refactors.
- **Layer IDs without attribution hooks**  
  If you can turn it on, you must be able to explain what it is (source/license).
- **AI content sneaking in as normal text**  
  AI content must be explicitly typed/labeled in configs and UI.
- **Precision coordinates for protected places**  
  If something is classified sensitive, configs must not carry exact coordinates.

---

## 📚 Related KFM references (by path)

- 📄 `docs/templates/TEMPLATE__STORY_NODE_V3.md` (Story Node template)
- 📄 `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- 📄 `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- 📁 `src/server/contracts/` (API contracts: OpenAPI / GraphQL)
- 📁 `web/` (frontend app; layer registry/config lives here)

---

## 🗂️ Glossary

- **Story Node** 📘: Markdown narrative with citations + semantic annotations that the system can parse/index.
- **Focus Mode** 🧠: Interactive reading view that merges Story Node + map + timeline with strict trust rules.
- **Provenance** 📜: Source + processing lineage (what data came from where and how it was transformed).
- **“Hard gate”** 🛡️: A rule that must *always* be enforced (schema/CI/runtime), not a “best effort”.

---

### ✅ If you only remember one thing…

**UI configs are contracts.**  
Contracts protect the project from drift, and protect users from unsourced claims or sensitive leaks. 🧭🛡️
