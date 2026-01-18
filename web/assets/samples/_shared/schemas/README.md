# 🧩 Shared Schemas for Web Samples

![JSON Schema](https://img.shields.io/badge/JSON%20Schema-validated-2ea44f)
![Contract-First](https://img.shields.io/badge/Contract--first-KFM%20standard-1f6feb)
![Provenance](https://img.shields.io/badge/Provenance-first-success)
![Samples](https://img.shields.io/badge/Web%20Samples-_shared%20assets-informational)

This folder contains **JSON Schemas** used by the **web sample assets** 🧪—so the frontend can load and validate sample metadata, narrative fixtures, and UI config **without guessing**.

> [!IMPORTANT]
> These schemas should **mirror the canonical contracts** in the repo’s top-level `schemas/` directory.
> If something differs, the canonical `schemas/` wins 🏛️ (this folder is for *web sample packaging*).

---

## 🎯 Purpose

✅ Provide a **stable, local** set of contract artifacts for sample data  
✅ Enable **offline / static** validation (demo builds, docs, test fixtures)  
✅ Make sample assets **self-describing** and harder to accidentally break 🔧

> [!NOTE]
> The platform is “contract-first”: schemas are first-class artifacts and changes require versioning discipline.  
> In practice: if sample data can’t validate, treat it as a 🚨 red flag.

---

## 🗺️ Folder layout

```text
web/assets/samples/_shared/schemas/
├── 📄 README.md                       # ← you are here 🙂 📌 What schema subsets exist + how samples validate fixtures
├── 🛰️ stac/                           # STAC contracts for sample assets/items/collections (small, representative)
├── 🗂️ dcat/                           # DCAT dataset/distribution discovery contracts (sample catalog metadata)
├── 🧬 prov/                           # PROV lineage/derivation contracts (how sample outputs cite sources/tools)
├── 📚 storynodes/                     # Governed narrative object schemas (Story Node / Focus Mode sample inputs)
├── 🎛️ ui/                             # UI configuration schemas (layers, panels, timelines) used by sample pages
└── 📡 telemetry/                      # Telemetry/event schemas (optional: used when samples emit analytics)
```

If any folder is missing in your branch, that’s okay—**only include what the samples actually ship**. Keep the structure consistent so `$ref` paths don’t churn.

---

## 📦 What’s inside (by category)

| 📁 Folder | What it defines | Used by |
|---|---|---|
| 🛰️ `stac/` | Assets catalog metadata contracts (items/collections) | sample catalogs, map layers, evidence listings |
| 🗃️ `dcat/` | Dataset/distribution discovery contracts | dataset listings, download panels |
| 🧬 `prov/` | Provenance / lineage contracts | evidence traceability, “how was this made?” panels |
| 📝 `storynodes/` | Governed narrative objects with citations & evidence links | Story Node renderer, Focus Mode |
| 🧩 `ui/` | UI configuration and view-model contracts | sample layer registry, UI fixtures |
| 📡 `telemetry/` | Structured events/contracts for logging | demo dashboards, audit trails (optional) |

---

## 🧰 How these schemas are used in the web app

Common usage patterns:

1. **Validate sample JSON on load** 🧪  
   - Load a sample file (e.g., `*.json`)
   - Validate against the matching schema
   - Fail fast with actionable errors (path + message)

2. **Power typed-ish UI behavior** 🧠  
   - Schemas can back:
     - form generation (optional)
     - config validation (highly recommended)
     - fixture sanity checks

3. **Prevent “mystery fields”** 🧱  
   - Prefer explicit properties
   - Avoid silent acceptance of unknown keys unless intentionally allowed

> [!TIP]
> Even if the UI doesn’t validate at runtime, schemas are still useful for **CI validation** and dev tooling.

---

## ✅ Validation & testing

### Option A: Validate via Node tooling (example)
```bash
# Example only — use the project’s chosen validator/tooling if different
npx ajv-cli validate -s ./stac/collection.schema.json -d ../../collections/example.collection.json
```

### Option B: Validate via Python (example)
```bash
python -m jsonschema -i example.json schema.json
```

> [!NOTE]
> Pick one toolchain and standardize it in CI. The key is consistency, not the specific validator.

---

## 🔁 Keeping schemas in sync with canonical contracts

**Golden rule:** update contracts once, then propagate.

### Recommended workflow
1. ✅ Update canonical schema(s) in:  
   `📁 /schemas/...`
2. ✅ Update any docs that describe the contract (if applicable) 📚  
3. ✅ Update sample fixtures to match 🧩  
4. ✅ Copy/propagate the *exact* schema artifact into this folder (or generate it during build)

> [!WARNING]
> Don’t “hot-fix” sample schemas here to make the UI happy if the canonical schema disagrees.
> That creates a split-brain contract and will bite later 🐍.

---

## 🧾 Schema conventions (please follow)

### Must-haves
- 🏷️ `title` + `description` (human clarity)
- 🧭 `$id` (stable identity)
- 🔗 `$ref` only to **local** files whenever possible (offline-friendly)
- 🧱 Tight constraints where it matters (`required`, enums, formats)

### Strong preferences
- ✅ Treat schemas as **contracts**, not suggestions  
- ✅ Prefer explicit `additionalProperties: false` for configuration objects  
- ✅ Use shared definitions (`$defs` / `definitions`) to reduce duplication  
- ✅ Keep schemas deterministic and reviewable (no giant generated blobs unless unavoidable)

### Naming suggestions
- `*.schema.json` for schemas
- `*.example.json` for fixtures/examples (if colocated nearby)

---

## 🚦Change management

When changing a schema, classify the change:

- 🟢 **Additive / backward compatible**: new optional fields, relaxed constraints  
- 🟡 **Behavioral**: changes in defaults/interpretation (document it clearly)  
- 🔴 **Breaking**: renames, removed fields, stricter required sets

> [!IMPORTANT]
> Breaking changes must come with:
> - a version bump 🏷️
> - fixture updates 🧩
> - migration notes 🛠️ (even if short)

---

## 🔐 Governance & safety notes

Even in samples:
- 🧬 Provenance should be represented (or intentionally stubbed with clarity)
- 🧭 Sensitive classifications must not be “lost” when deriving sample artifacts
- 🗺️ If any samples include locations, ensure they’re safe to publish (or generalized)

---

## 🔗 Related docs

These links are intentionally “source-of-truth” oriented:

- 📘 Canonical schemas: `../../../../../schemas/`
- 🧠 Master Guide: `../../../../../docs/MASTER_GUIDE_v13.md`
- 🛰️ STAC profile: `../../../../../docs/standards/KFM_STAC_PROFILE.md`
- 🗃️ DCAT profile: `../../../../../docs/standards/KFM_DCAT_PROFILE.md`
- 🧬 PROV profile: `../../../../../docs/standards/KFM_PROV_PROFILE.md`
- 📝 Story Node template: `../../../../../docs/templates/TEMPLATE__STORY_NODE_V3.md`

---

## 🧯 Troubleshooting

<details>
  <summary><strong>🔗 $ref paths keep breaking</strong></summary>

- Prefer **relative refs** that remain stable if the repo root moves.
- Keep schema folder structure aligned with canonical `schemas/`.
- Avoid `http(s)://` refs for sample builds (offline + reproducibility).

</details>

<details>
  <summary><strong>🧪 Validation fails but the UI “seems fine”</strong></summary>

That’s exactly why we validate 😄  
Fix the mismatch now—otherwise the sample becomes a “quiet liar” and future work will drift.

</details>

