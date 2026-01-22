# 🧱 `input/raw/` — Immutable Evidence (Minimal Triplet Quickstart)

![Provenance-First](https://img.shields.io/badge/provenance-first-✅-informational?style=for-the-badge)
![Immutable Raw](https://img.shields.io/badge/raw%20data-immutable-important?style=for-the-badge)
![Triplet](https://img.shields.io/badge/STAC%20%2B%20DCAT%20%2B%20PROV-required-blue?style=for-the-badge)
![Policy Gates](https://img.shields.io/badge/OPA%20%2B%20Conftest-policy%20gates-critical?style=for-the-badge)
![FAIR+CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-governed-success?style=for-the-badge)

> **This folder is the trust anchor.**  
> Everything downstream (ETL → catalogs → graph → API → UI/Focus Mode) must be reproducible from the bytes stored here — **no “mystery layers,” no ad‑hoc sources, no silent edits**. 🧾🔍

---

## 📌 What this folder is for

This `input/raw/` directory is the **minimal example** version of KFM’s staged data lifecycle:

- **Raw** (`input/raw/`) → immutable source files ✅  
- **Work** (`input/work/`) → intermediate transforms 🧪  
- **Processed** (`input/processed/` or `output/`) → publishable outputs 📦  
- **Boundary artifacts** → **STAC + DCAT + PROV** (the “minimal triplet”) 🧬

KFM’s architecture treats **catalog + provenance artifacts as required interface boundaries** before anything is considered “published” (i.e., safe to load into graph/UI).[^boundary_artifacts]

---

## 🗂️ Expected contents

At minimum, keep these alongside the raw files:

- 📄 `README.md` (this file) — what the dataset is + how to treat it
- 🧾 `source.json` — “data contract” / acquisition + provenance metadata for each raw file
- 🔐 `checksums.sha256` — SHA‑256 checksums for **every** file in this folder

KFM’s intake design explicitly calls out **raw sources + checksums + source metadata** and expects validation + deterministic processing after this step.[^raw_contract]

### 🧰 Folder layout (recommended)

```text
📦 examples/00_quickstart_minimal_triplet/
└─ 📥 input/
   └─ 🧱 raw/
      ├─ 📄 README.md
      ├─ 🧾 source.json
      ├─ 🔐 checksums.sha256
      ├─ 🗺️ example_layer.geojson
      └─ 📊 example_table.csv
```

> 💡 **Rule of thumb:** if a file is needed to reproduce the run, it belongs here (or it must be referenced immutably, e.g., by digest in an artifact store).

---

## 🚫 Non‑negotiables (raw ≠ workspace)

### ✅ Do
- ✅ **Store the original bytes** as acquired (“downloaded, received, exported, scanned…”).[^raw_contract]
- ✅ Track **checksums** (`checksums.sha256`) so byte‑level integrity is verifiable.[^raw_contract]
- ✅ Describe the source in a **contract-first** way (`source.json`) so it can be validated and attributed.[^contract_first]
- ✅ Add a new file for revisions (e.g., `v2`, new date, new digest), rather than editing in place.

### ❌ Don’t
- ❌ Don’t “clean” raw data in place (missing values, outliers, normalization, etc. belong in `work/`).[^data_cleaning]
- ❌ Don’t rename files after checksums are published (that breaks reproducibility).
- ❌ Don’t include secrets, private keys, credentials, or non‑cleared sensitive content.

> 🧯 **Fail‑closed mindset:** if provenance/safety can’t be established, ingestion should stop rather than “best‑effort publish.”[^fail_closed]

---

## 🧬 The “Minimal Triplet” promise (STAC + DCAT + PROV)

This quickstart exists to prove the smallest publishable unit in KFM:

- **STAC**: spatiotemporal asset records (items/collections)
- **DCAT**: dataset discovery + catalog metadata (JSON‑LD)
- **PROV**: lineage bundle (inputs → activities → outputs → agents)

In KFM’s documentation, these are treated as **required boundary artifacts** before downstream use (graph/API/UI).[^boundary_artifacts]

### 🔁 Why it matters (UI + AI depend on it)

KFM’s UI and Focus Mode are designed so that **every visualization and AI answer is traceable to sources** (“the map behind the map”), and the assistant should refuse or show uncertainty if it can’t cite real sources.[^ui_map_behind_map][^ai_citations]

---

## 🛠️ Add a new raw source (minimal workflow)

### 1) Drop the file(s) in this folder 🧱
Use stable, readable names:
- `domain__topic__YYYY-MM-DD__source__vN.ext`

Examples:
- `hydro__gages__2026-01-21__usgs__v1.csv`
- `geo__surficial_geology__2026-01-21__ksgs__v1.geojson`

### 2) Update `source.json` 🧾
Track: where it came from, when/how obtained, licensing, and any handling notes.

<details>
<summary>🧾 Example <code>source.json</code> (minimal, tweak as needed)</summary>

```json
{
  "dataset_id": "00_quickstart_minimal_triplet",
  "title": "Quickstart Minimal Triplet (Example)",
  "sources": [
    {
      "path": "geo__surficial_geology__2026-01-21__ksgs__v1.geojson",
      "source_url": "https://example.org/datasets/surficial-geology",
      "retrieved_at": "2026-01-21T00:00:00Z",
      "license": "CC-BY-4.0",
      "sha256": "<fill_from_checksums.sha256>",
      "notes": "Raw file stored as acquired; transforms occur in work/."
    }
  ]
}
```
</details>

> KFM emphasizes **contract-first** metadata so validators and downstream systems can rely on consistent provenance and attribution.[^contract_first]

### 3) Recompute `checksums.sha256` 🔐
Generate SHA‑256 for every file in this folder (including `source.json`).

<details>
<summary>🔐 Example commands</summary>

```bash
# Linux / WSL
sha256sum * > checksums.sha256

# macOS
shasum -a 256 * > checksums.sha256

# PowerShell (Windows)
Get-FileHash * -Algorithm SHA256 | Format-Table -HideTableHeaders > checksums.sha256
```
</details>

KFM’s raw-stage design explicitly includes maintaining checksums for integrity and auditability.[^raw_contract]

### 4) Validate + build the triplet ✅🧬
Run the example’s validation/build step (whatever the quickstart script provides in your repo).

> 🧪 In the full KFM intake model, validation includes schema checks, CRS/geo sanity, license presence, sensitivity classification, and provenance completeness — enforced as policy gates.[^policy_gates]

---

## 🌍 Geospatial sanity checks (tiny, high‑value)

If you’re adding **GeoJSON**:

- Coordinates are `[longitude, latitude]` (X, Y), not `[lat, lon]`.[^geojson_order]
- Validate geometry (no self‑intersections / invalid rings) before you build derived assets.[^geojson_order]

<details>
<summary>🧭 Quick checks (conceptual)</summary>

```text
✅ CRS known (prefer EPSG:4326 for published derivatives)
✅ Geometry valid (e.g., PostGIS ST_IsValid or equivalent)
✅ Bounds make sense (Kansas-ish, not flipped)
✅ Attributes have consistent types (no mixed strings/ints)
```
</details>

> 📌 Keep the raw file as-is; do fixes in `work/` and publish corrected/standardized outputs downstream.

---

## 🔐 Governance: FAIR+CARE + sensitive data

KFM’s roadmap and governance notes emphasize codifying **FAIR + CARE** rules into the tooling:
- flag culturally sensitive / PII content,
- require approvals/redaction,
- prevent unsafe publication through automated gates.[^fair_care]

If this quickstart is public/open-source:
- ✅ only include public or safely-sanitized example data
- ❌ do **not** commit restricted datasets here

---

## ⚖️ Policy gates (OPA/Rego) + CI behavior

KFM describes a **Policy Pack** using **Open Policy Agent (OPA)** + **Conftest** to enforce rules like:
- “every dataset must have a license”
- “AI outputs must include at least one citation”
- “nothing merges if governance rules are violated”[^opa_pack]

This is consistent with KFM’s “detect → validate → promote” CI pipeline approach and fail-closed behavior.[^opa_pack]

---

## 🤖 `dev_prov` angle: provenance for *code changes*, too

In the “Latest Ideas” proposals, KFM extends provenance into devops by mapping:
- GitHub PRs → **PROV Activities**
- Commits → **PROV Entities**
- Authors/reviewers → **PROV Agents**  
…and ingesting those JSON‑LD records into Neo4j so “which code version produced this dataset?” is queryable.[^pr_to_prov]

This quickstart folder is intentionally designed to play well with that idea:
- raw bytes are immutable,
- inputs are checksummed,
- runs can be linked to a PR/commit provenance trail.

---

## 📦 Optional power move: package raw/outputs as OCI artifacts (content-addressable)

For larger binaries or distribution outside Git:
- package artifacts (PMTiles, GeoParquet, COGs) into an OCI registry using **ORAS**
- sign with **Cosign**
- reference by **digest** for reproducibility and integrity.[^oci_oras_cosign]

This aligns with the KFM “treat data with the same rigor as code” concept — versioned, reviewable, and verifiable.[^oci_oras_cosign]

---

## 🧵 Storytelling + updates: Pulse Threads (optional but awesome)

When turning evidence into narratives, KFM notes “Pulse Threads” as an update stream that:
- always references sources,
- preserves provenance,
- ties interpretations back to evidence.[^pulse_threads]

Raw evidence here is what those story layers ultimately point back to.

---

## 📚 Reference shelf (project files used to shape this folder contract)

> These docs inform why this folder is strict, reproducible, and policy-gated. 📖✨

- 🧾 Data intake staging, raw immutability, checksums/source manifests, and policy philosophy[^raw_contract]
- 🧬 Boundary artifacts: STAC + DCAT + PROV as required publish interfaces[^boundary_artifacts]
- 🗺️ UI transparency (“map behind the map”), provenance surfaced in layers + Focus Mode[^ui_map_behind_map]
- 🤖 AI Focus Mode must cite sources; refuses/flags uncertainty without evidence[^ai_citations]
- ⚖️ OPA policy pack + CI enforcement model[^opa_pack]
- 🧑‍⚖️ FAIR+CARE governance and sensitive-data handling in tooling[^fair_care]
- 🧪 Geospatial validation tips (GeoJSON order + geometry validity)[^geojson_order]
- 🧹 Data preprocessing belongs downstream (raw stays raw)[^data_cleaning]
- 🧵 Narrative update mechanics (Pulse Threads)[^pulse_threads]
- 📦 OCI artifact packaging + signing idea for data integrity/distribution[^oci_oras_cosign]

### 📦 “Library packs” (PDF portfolios)
These are bundled reference collections (open locally for full contents):

- 🧠 AI reading pack (portfolio): `AI Concepts & more.pdf`[^ai_portfolio]
- 🗺️ Mapping/WebGL/virtual worlds pack (portfolio): `Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf`[^maps_portfolio]
- 🧰 Programming resources pack (portfolio): `Various programming langurages & resources 1.pdf`[^langs_portfolio]
- 🗃️ Data management/data science pack (portfolio): `Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf`[^data_mgmt_portfolio]

---

## 🧾 Sources (footnotes)

[^raw_contract]: Raw stage expectations (immutable sources + `checksums.sha256` + `source.json` + validation + deterministic transforms). 

[^boundary_artifacts]: Boundary artifacts + staged lifecycle (raw → work → processed; STAC/DCAT/PROV required before publish). :contentReference[oaicite:1]{index=1}

[^contract_first]: Contract-first metadata + “no mystery layers” trust model. :contentReference[oaicite:2]{index=2}

[^ui_map_behind_map]: UI design principle: provenance-linked visualizations (“map behind the map”) + trust/credits. :contentReference[oaicite:3]{index=3}:contentReference[oaicite:4]{index=4}

[^ai_citations]: Focus Mode requirement: always cite sources; refuse/indicate uncertainty if not supported. :contentReference[oaicite:5]{index=5}

[^fail_closed]: Fail-closed posture + missing provenance triggers CI failure (illustrated in governance/policy discussion). :contentReference[oaicite:6]{index=6}

[^data_cleaning]: Data preprocessing/cleaning steps (missing values, noise, outliers) are part of preparation — not raw mutation. 

[^geojson_order]: GeoJSON coordinate order (lon,lat) + geometry validation concept (e.g., ST_IsValid). 

[^policy_gates]: Automated policy gates checklist (schema validation, STAC/DCAT/PROV completeness, license, sensitivity, provenance; fail-closed). :contentReference[oaicite:9]{index=9}

[^opa_pack]: OPA/Conftest Policy Pack concept + CI enforcement examples. :contentReference[oaicite:10]{index=10}

[^pr_to_prov]: GitHub PR → PROV graph integration concept (PR activity, commits entities, authors agents). :contentReference[oaicite:11]{index=11}

[^fair_care]: FAIR+CARE rules codified; WPE checks to prevent exposing sensitive locations/PII. :contentReference[oaicite:12]{index=12}

[^oci_oras_cosign]: OCI + ORAS + Cosign idea: content-addressable storage and signatures; digests as identifiers; provenance tie-in. :contentReference[oaicite:13]{index=13}:contentReference[oaicite:14]{index=14}

[^pulse_threads]: Pulse Threads concept: concise updates tied to sources/provenance. :contentReference[oaicite:15]{index=15}

[^ai_portfolio]: AI portfolio notice (bundle). 

[^maps_portfolio]: Mapping/WebGL portfolio notice (bundle). 

[^langs_portfolio]: Programming resources portfolio notice (bundle). 

[^data_mgmt_portfolio]: Data management/data science portfolio notice (bundle). 

