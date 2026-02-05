# 🧠 AI Layer Definitions (`web/src/layers/definitions/ai/`)

> **Evidence-first map overlays** for Focus Mode + AI-derived analysis layers.  
> “No Source, No Answer.” ✅

---

## 🎯 What this folder is

This directory contains **declarative layer definitions** for anything in the UI that is:

1) **AI-driven at runtime** (ephemeral overlays):  
   - highlights / outlines of features referenced by Focus Mode  
   - callouts, bounding boxes, “zoom-to” targets  
   - temporary search results returned from AI-orchestrated retrieval

2) **AI-derived but published as evidence** (persisted layers):  
   - AI-generated/assisted analysis products that have been **promoted to first-class artifacts** (cataloged, licensed, provenance-tracked) and are visualized like any other dataset layer.

### 🚫 What this folder is *not*
- Not the LLM / embeddings / RAG pipeline.
- Not the policy engine.
- Not the data catalog.
- Not “random AI experiments that render on the map.”

If you’re writing orchestration logic, that belongs server-side (API + retrieval + policy). The UI **only** renders what it is allowed to render.

---

## 🧱 Where this fits in KFM

KFM is intentionally layered:

- **UI (React/TypeScript)** renders map + timeline + Focus Mode chat.
- **API layer** is the gatekeeper: retrieval, permissions, redaction, policy checks.
- **Datastores** are sources of truth.
- **Ollama (local LLM runtime)** is the text generator *behind* the API.

This folder is the UI-side **last mile**: it converts “approved outputs” (data + citations + map instructions) into visual overlays.

---

## ✅ Non‑negotiables (project invariants)

These are “hard rules” for anything under `definitions/ai`:

- **No hidden data paths**  
  Layer definitions must not reach around the API (no direct DB access, no “mystery files,” no bypass endpoints).

- **Provenance-first**  
  Every persisted AI-derived layer must point to a real dataset artifact (DCAT/STAC metadata + license + provenance lineage).

- **Citations are mandatory**  
  If a layer is the result of Focus Mode (runtime overlays), it must still link back to the **answer citations** and/or the dataset entities that were used to generate the overlay.

- **Fail closed**  
  Missing metadata, missing provenance, missing sensitivity label, missing citations → the layer should not render.

- **CARE-aware rendering**  
  If a layer touches sensitive content (especially culturally sensitive locations), the definition must support **redaction modes** (geometry generalization, obfuscation, or “no map draw, text-only explanation”).

---

## 🗂️ What should live here

### ✅ Good fits
- `focus-mode` overlays (highlight + bbox + pin + route line)
- “AI suggested layers” (UI metadata that lets Focus Mode recommend a layer safely)
- “AI interpretation layers” that are *explicitly labeled* as interpretation and linked to evidence

### ❌ Bad fits
- Hardcoded “facts” inside the layer definition
- Layer code that performs retrieval itself
- A layer that cannot explain its data source / license / provenance

---

## 🧩 Recommended contract: `AiLayerDefinition`

> **Goal:** keep layer definitions predictable, testable, and policy-friendly.

Below is a **suggested** interface (adjust to match your existing layer registry types).

```ts
export type AiLayerKind =
  | "ai:ephemeral"      // Runtime overlays (Focus Mode highlights, callouts)
  | "ai:derived"        // AI-derived dataset layer (persisted, cataloged)
  | "ai:suggestion";    // Non-rendering helper used for AI recommendations

export type Renderer = "maplibre" | "cesium" | "both";

export interface ProvenanceBinding {
  /** Stable IDs that resolve through the API/catalog */
  datasetIds?: string[];        // DCAT dataset IDs
  stacItemIds?: string[];       // STAC items/collections (if used)
  graphEntityIds?: string[];    // Neo4j/graph stable IDs (if applicable)

  /** UI rendering must show these somewhere (layer info, popup, footnotes) */
  requiresCitations: boolean;

  /** Human-readable attribution */
  attributionText?: string;
  licenseId?: string;           // SPDX-like if possible
}

export interface SensitivityPolicy {
  classification: "public" | "internal" | "confidential" | "restricted";

  /**
   * If true, the layer definition must support a "redacted" render mode:
   * - generalized geometry
   * - masked properties
   * - or disabled map drawing with a safe explanation
   */
  requiresRedactionSupport: boolean;

  /** Optional tags for policy packs / UI behavior */
  tags?: string[]; // e.g. ["care:indigenous", "no_exact_coords", "pii-risk"]
}

export interface AiLayerDefinition {
  id: string;                 // stable + unique
  kind: AiLayerKind;

  title: string;
  description?: string;

  renderer: Renderer;

  /** Visibility defaults */
  defaultOn?: boolean;
  userToggleable?: boolean;

  /** Time support (timeline integration) */
  temporal?: {
    enabled: boolean;
    startField?: string;
    endField?: string;
  };

  /** Data access (always through API) */
  data?: {
    mode: "vector-tile" | "raster-tile" | "geojson" | "api-driven";
    tilePath?: string;       // e.g. "/tiles/<layer>/{z}/{x}/{y}.pbf"
    rasterPath?: string;     // e.g. "/tiles/<layer>/{z}/{x}/{y}.png"
    geojsonEndpoint?: string;
    queryEndpoint?: string;
  };

  provenance: ProvenanceBinding;
  sensitivity: SensitivityPolicy;

  /** Map styling hooks */
  style?: {
    /** MapLibre style fragments (declarative) */
    maplibre?: {
      sources?: Record<string, any>;
      layers?: any[];
    };

    /** Cesium styling hooks (if applicable) */
    cesium?: Record<string, any>;
  };

  /** UI semantics */
  ui?: {
    legend?: {
      enabled: boolean;
      items?: Array<{ label: string; symbol: string }>;
    };
    popup?: {
      enabled: boolean;
      templateId?: string;
      fields?: string[];
    };
    /** Where do citations show up for this layer? */
    citations?: {
      mode: "layer-info" | "popup" | "focus-mode-footnotes" | "none";
    };
  };

  /** Optional: Focus Mode affordances (recommendations / safe actions) */
  focusMode?: {
    canRecommend: boolean;
    canAutoEnable: boolean;
    safeMapActions?: Array<"zoom" | "highlight" | "pin" | "filter">;
  };
}
```

### 🧠 Key idea
Even “AI layers” are still **layers with governance**. If you can’t answer:
- *What is this showing?*  
- *Where did it come from?*  
- *Who is allowed to see it?*  
- *How do we cite it?*  
…then it’s not ready to live here.

---

## 🗺️ Focus Mode overlays: expected behavior

Focus Mode can return:
- an evidence-backed answer (with citations)
- optional **map instructions** (highlight these features, zoom here, show this layer)

This folder should provide the **rendering targets** for those instructions:
- stable overlay layer IDs (ex: `ai:focus-highlight`, `ai:focus-callout`)
- safe styling defaults
- redaction-aware fallbacks

> 💡 If the backend says “highlight entity X”, the UI should render it **only** through:
> - an approved endpoint, and
> - a layer definition that already knows how to display citations + handle sensitivity.

---

## ➕ Adding a new AI layer

### A) Ephemeral (Focus Mode) overlay ✅
1. Add a definition under this folder with `kind: "ai:ephemeral"`.
2. Ensure it can render from API-returned GeoJSON/features without extra lookups.
3. Ensure citations are visible via Focus Mode footnotes (or layer info panel).
4. Add redaction behavior if the overlay can point at sensitive locations.

### B) AI-derived dataset layer ✅
1. Treat the output as an **evidence artifact**:
   - pipeline produces it
   - catalog entry exists (DCAT/STAC)
   - provenance lineage exists
2. API serves it (tiles or GeoJSON).
3. Add a definition here with `kind: "ai:derived"` and link `provenance.datasetIds[]`.
4. Ensure legend/popup cites the dataset and license.
5. Add tests: metadata required, citations required, sensitivity enforced.

---

## 🔒 Security & governance hooks

### Prompt / input safety
Focus Mode requests must already be sanitized upstream; UI should not attempt to “helpfully” override system prompts.

### Output safety
Assume policy checks can:
- deny an answer
- sanitize fields
- require redacted geometry
- block exact coordinates for protected content

Your layer definitions must support these “policy-shaped” responses.

---

## ⚡ Performance & UX notes

- Prefer **vector tiles** for large/broad layers.
- Use **GeoJSON overlays** for small, ephemeral, session-scoped overlays.
- Keep ephemeral overlays cheap: minimal layers, minimal expressions, minimal re-renders.
- Prefer stable IDs so session updates can diff cleanly.

---

## 🧪 Testing checklist (CI-friendly)

When you add/change an AI layer definition, ensure:

- [ ] It cannot render without provenance binding when required  
- [ ] Citation requirement is enforced by definition metadata  
- [ ] Sensitivity classification exists and has a redaction plan  
- [ ] The layer doesn’t fetch outside the API abstraction  
- [ ] Focus Mode overlays have stable IDs and deterministic styling  
- [ ] Regression tests cover “no citations → refuse/disable” behavior

---

## 🧰 Troubleshooting

### “Layer doesn’t show up”
- Is the user allowed to see it (classification + role)?
- Is the dataset actually published (catalog entry + license + provenance)?
- Is the tile/data endpoint returning data?

### “Layer shows, but citations are missing”
- Check `provenance.requiresCitations`
- Ensure UI route exists for rendering citations:
  - layer info panel, popup, or Focus Mode footnotes

### “AI highlight points to sensitive place”
- Confirm policy returned redacted geometry (or blocked render)
- Ensure the definition can switch to redacted mode gracefully

---

## 📚 Internal references (recommended reading)

- `docs/architecture/ai/OLLAMA_INTEGRATION.md`
- `docs/architecture/AI_SYSTEM_OVERVIEW.md`
- `src/server/api/README.md`
- `docs/standards/` (metadata + provenance profiles)
- `docs/reports/story_nodes/` (citation-rich narrative artifacts)

---