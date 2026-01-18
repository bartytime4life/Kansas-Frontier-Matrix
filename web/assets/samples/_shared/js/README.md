# 🧩 `_shared/js` — Shared JavaScript Helpers for Samples

![Static Site](https://img.shields.io/badge/site-static%20%2F%20GitHub%20Pages-friendly)
![JS](https://img.shields.io/badge/javascript-ES%20Modules%20%28no%20bundler%29-informational)
![KFM](https://img.shields.io/badge/KFM-provenance--first%20%F0%9F%94%8E-blueviolet)

This folder contains **small, reusable browser modules** that power the sample pages under:

> 📁 `web/assets/samples/`

The goal is simple: **samples stay tiny**, and shared behavior lives here ✅  
(loading configs, fetching JSON safely, map helpers, provenance display, UI widgets, etc.)

---

<details>
<summary><strong>🧭 Quick nav</strong></summary>

- [What belongs here](#what-belongs-here)
- [Design constraints](#design-constraints)
- [Using shared modules in a sample](#using-shared-modules-in-a-sample)
- [KFM-aligned rules (provenance & evidence)](#kfm-aligned-rules-provenance--evidence)
- [Adding a new module](#adding-a-new-module)
- [Module registry](#module-registry)
- [Security & privacy](#security--privacy)
- [Troubleshooting](#troubleshooting)
- [Internal references](#internal-references)

</details>

---

## 🗂️ What belongs here

Use `_shared/js/` when a behavior is:

- ✅ used by **2+** samples (or clearly about to be)
- ✅ **generic** (not tied to one dataset/story)
- ✅ browser-only (works on a static site)
- ✅ safe to share (no sample-specific hacks)

Keep code **inside a sample folder** when it’s:

- 🧪 experimental / spike-only
- 🎯 highly specific to one sample’s narrative or dataset
- 🧱 likely to be rewritten soon

> 🧠 Rule of thumb: if you’d copy/paste it into another sample, it probably belongs here.

---

## 🌐 Design constraints

These constraints keep samples deployable as a **static site**:

- **ES Modules only** (`type="module"`, `import/export`)
- **No bundler required** (avoid Node-only patterns)
- **Relative imports** (so GitHub Pages + local dev both work)
- **No secrets** (anything shipped to the browser is public)
- **No “mystery layers”** — if a sample shows data, it should also show *where it came from* 🔎

---

## 🧪 Using shared modules in a sample

Typical sample layout (illustrative):

```text
web/assets/samples/
├── ♻️ _shared/
│   └── 🧠 js/                     # 👈 you are here 📌 Shared JS helpers used across multiple samples
│      └── 🧠📄 …                   # map bootstrap, layer toggles, timeline binding, URL state, etc.
└── 🧪 <sample-name>/               # One runnable sample (self-contained demo)
    ├── 🧾📄 index.html              # Sample entry page (minimal markup + mounts demo UI)
    ├── 🧠📄 app.js                  # Sample-specific logic (wires shared helpers + sample config)
    └── 📄 README.md                 # How to run the sample + what it demonstrates + data/licensing notes
```

### ✅ Import pattern

From a sample located at `web/assets/samples/<sample-name>/app.js`:

```js
// app.js (inside a sample)
import { somethingUseful } from "../_shared/js/<module>.js";

somethingUseful();
```

### ✅ HTML pattern

```html
<!-- index.html -->
<script type="module" src="./app.js"></script>
```

> ⚠️ Don’t run samples from `file://` URLs. Use a local server (see [Troubleshooting](#troubleshooting)).

---

## 🧾 KFM-aligned rules (provenance & evidence)

KFM’s broader architecture is **contract-first + provenance-first + evidence-first**.  
Even in samples, we keep the *same posture*:

### 🔎 Provenance-first (UI must be traceable)
If a sample loads a dataset/layer/story step:

- show **attribution + license** somewhere visible
- link to **catalog metadata** when available (STAC/DCAT)
- link to **lineage** when available (PROV)
- avoid adding anything that can’t be traced back to a source

### 🧱 API boundary (don’t bypass governance)
If a sample needs structured knowledge:

- fetch it from the **governed API layer** (not direct DB/graph access)
- treat API responses as the contract—validate shape and handle missing fields

### 🧠 Evidence-first narrative
If a sample includes narrative text:

- author it in **Markdown** (when practical)
- include citations/links per claim (or per section)
- label any generated/derived outputs clearly (and keep a trail)

> ✅ The best sample feels like a miniature “Story Node”: map + narrative + evidence links.

---

## 🧰 Adding a new module

### 🧱 Naming & shape
- Prefer **small, single-purpose** files
- Prefer **named exports** (avoid default exports)
- Prefer **pure functions** (or factory functions) over hidden globals
- Add **JSDoc** types for inputs/outputs if the function isn’t obvious

Example skeleton:

```js
/**
 * @param {{ url: string }} opts
 * @returns {Promise<any>}
 */
export async function fetchJson(opts) {
  const res = await fetch(opts.url);
  if (!res.ok) throw new Error(`HTTP ${res.status} for ${opts.url}`);
  return res.json();
}
```

### ✅ Contribution checklist
- [ ] Works in **modern browsers** without a build step
- [ ] No sample-specific constants baked in
- [ ] Errors are actionable (include URLs / layer ids / context)
- [ ] No secrets, tokens, or private endpoints
- [ ] Update the [Module registry](#module-registry)
- [ ] If it affects UX, add a tiny screenshot/gif to the **sample’s** README (not here)

---

## 🧾 Module registry

> 📌 Keep this table up to date as modules are added/renamed.

| 📄 Module | Purpose | Used by | Notes |
|---|---|---:|---|
| *(add entries)* | *(what it does)* | *(# samples)* | *(gotchas / config)* |

---

## 🎛️ Style guidelines (recommended)

- ✅ Prefer `const`/`let` (no `var`)
- ✅ Prefer `async/await` over nested `.then()`
- ✅ Prefer `AbortController` for cancellable fetches (maps + sliders)
- ✅ Keep DOM selectors scoped to a container (avoid global `document.querySelector` when possible)
- ✅ Keep performance in mind (maps + tiles): debounce UI, cache metadata requests, avoid huge GeoJSON blobs

---

## 🔒 Security & privacy

Because samples run in-browser:

- 🚫 **Never** include API keys or tokens in JS
- 🚫 Avoid `eval`, dynamic script injection, and unsafe HTML insertion
- ✅ If rendering Markdown/HTML: **sanitize** first
- ✅ Prefer pinned dependencies (vendored libs or locked versions) if pulling from CDNs
- ✅ Assume anything in `web/` is public

---

## 🧯 Troubleshooting

### “CORS / fetch blocked / nothing loads”
You’re probably opening the HTML via `file://`.

Run a local server from the `web/` folder (example):

```bash
cd web
python -m http.server 8000
```

Then open:

- `http://localhost:8000/assets/samples/<sample-name>/`

### “Imports fail on GitHub Pages”
- Use **relative paths**
- Avoid absolute `/assets/...` unless the site is configured with the correct base path
- Prefer `new URL("./file.json", import.meta.url)` when referencing adjacent assets

### “Map tiles don’t appear”
- Check network tab for 404s
- Verify the layer URL is correct under the GitHub Pages base path
- Confirm the dataset is actually published and reachable

---

## 📚 Internal references

These docs define the “why” behind the constraints above:

- 📄 `docs/MASTER_GUIDE_v13.md` (pipeline invariants & repo structure)
- 📄 `docs/standards/` (STAC/DCAT/PROV profiles, governance)
- 📄 `docs/reports/story_nodes/` (governed narrative patterns)

> 🔗 From this folder, repo-root relative links typically start with:  
> `../../../../../`

---

<p align="right"><a href="#-sharedjs--shared-javascript-helpers-for-samples">⬆️ Back to top</a></p>
