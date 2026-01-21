# 04 — Pulse Thread Evidence Schemas 🧾⚡️

![JSON Schema](https://img.shields.io/badge/JSON%20Schema-2020--12-blue)
![PROV](https://img.shields.io/badge/PROV-JSON--LD%20ready-7b2cbf)
![STAC](https://img.shields.io/badge/STAC-aligned-2a9d8f)
![DCAT](https://img.shields.io/badge/DCAT-aligned-264653)
![Policy](https://img.shields.io/badge/Policy-OPA%20%2B%20Conftest-orange)

**Folder:** `mcp/dev_prov/examples/04_pulse_thread_evidence/schemas/` 📁  
**Purpose:** Define the *contract* for “Pulse Threads” + “Evidence Manifests” so every update is **auditable**, **reproducible**, and **UI-ready** (evidence-first, provenance-first) 🧭✅

---

<details>
<summary><strong>📌 Table of contents</strong></summary>

- [What this example is](#what-this-example-is)
- [What lives in this folder](#what-lives-in-this-folder)
- [Core objects](#core-objects)
  - [PulseThread](#pulsethread)
  - [EvidenceManifest](#evidencemanifest)
  - [EvidenceItem](#evidenceitem)
  - [ProvBundle](#provbundle)
  - [PolicyResult](#policyresult)
- [How this maps to KFM’s evidence stack](#how-this-maps-to-kfms-evidence-stack)
- [Validation](#validation)
- [Schema rules & conventions](#schema-rules--conventions)
- [Examples](#examples)
- [Extension hooks](#extension-hooks)
- [Related docs & references](#related-docs--references)

</details>

---

## What this example is

A **Pulse Thread** is a geotagged, time-aware micro-update (a “pulse”) tied to one or more geographic / historical nodes. This example demonstrates how Pulse Threads **must** carry structured evidence so that:

- the UI can show a **View Evidence** panel 🧾
- Focus/AI can answer with **citations** (and fail closed when it can’t) 🤖🧯
- the provenance graph can link *claims → evidence → sources → transformations* 🔗

> [!IMPORTANT]
> These schemas are for the **example** (`04_pulse_thread_evidence`).  
> Keep them **small + strict**, but align with the broader KFM patterns (STAC/DCAT/PROV, provenance-first, policy-as-code).

---

## What lives in this folder

You’ll usually see **JSON Schema** files like:

```text
schemas/ 🧩
├─ README.md 📘
├─ pulse_thread.schema.json ⚡️
├─ evidence_manifest.schema.json 🧾
├─ evidence_item.schema.json 🧷
├─ citation.schema.json 🔖
├─ prov_bundle.schema.json 🧬
├─ policy_result.schema.json 🛡️
└─ common/
   ├─ agent.schema.json 🧑‍🤝‍🧑
   ├─ geo.schema.json 🗺️
   └─ time.schema.json ⏱️
```

> If your filenames differ, keep the **object model** consistent and update links below.

---

## Core objects

### PulseThread

A **PulseThread** is the top-level object the system can render and index:

- **identity:** stable `id`, human `title`
- **geo/time anchoring:** `geo` (bbox/geometry/place refs), `time` (observed range/instant)
- **content:** `summary` (+ optionally `body_md`)
- **evidence binding:** a pointer to an **EvidenceManifest** + optional PROV bundle reference
- **authorship:** human/agent attribution (human-in-the-loop friendly)

Recommended minimal shape:

- `type`: `"PulseThread"`
- `id`: stable URI-ish identifier (e.g., `kfm:pulse:...`)
- `created_at`, `updated_at`
- `geo`: `{ bbox, geometry?, place_refs[] }`
- `time`: `{ observed_at? | start/end? }`
- `summary`
- `evidence`: `{ manifest_ref, citations[], prov_ref? }`

✅ **Design intent:** Everything the UI shows should be traceable back to **cataloged sources** and **provable processing**.

---

### EvidenceManifest

A structured “receipt” for the pulse:

- *what sources were used* (datasets/docs)
- *how they were queried* (params)
- *what time they were fetched* (timestamps)
- *what transformations were applied* (ETL steps)
- *how integrity is ensured* (checksums / digests)

Recommended minimal shape:

- `schema_version` (SemVer)
- `manifest_id` (hash-friendly, stable)
- `thread_id` (back-link to PulseThread)
- `generated_at`
- `items[]`: list of EvidenceItem
- `transformations[]`: optional list of pipeline steps
- `signing[]`: optional signatures / attestations

✅ **Tip:** Even if you store manifests as **YAML**, keep the schema in JSON Schema and validate by parsing YAML → JSON.

---

### EvidenceItem

The smallest *citable* unit.

Supports:
- dataset references (DCAT / STAC)
- document excerpts
- query results (API pulls)
- derived assets (tiles, rasters, normalized extracts)
- AI outputs (as *inputs* only when allowed & labeled)

Recommended minimal shape:

- `evidence_id` (stable, unique)
- `kind` (enum: `dataset|document|query_result|derived_asset|model_output|web_capture`)
- `source` (typed pointer: `dcat_dataset|stac_item|url|file|graph_ref`)
- `retrieved_at`
- `checksums` (`sha256` at minimum when bytes exist)
- `query` (optional; params + endpoint)
- `extracts[]` (optional; citeable fragments / ranges)
- `license` (optional but strongly recommended)
- `classification` / `sensitivity` (optional but recommended)

✅ **Fail-closed rule:** If you can’t prove what it is, where it came from, and how it was produced → it doesn’t ship.

---

### ProvBundle

A provenance bundle that can be stored as **PROV JSON-LD** (or referenced by file/path).

Recommended minimal shape:

- `@context` (JSON-LD context)
- `entities[]`
- `activities[]`
- `agents[]`
- `relations[]` (used/wasGeneratedBy/wasAttributedTo/wasDerivedFrom)

✅ **Goal:** Support “Show me how this pulse was created” in one click 🧭

---

### PolicyResult

OPA/Conftest (or other policy engines) can output structured results that attach to the pulse or manifest:

- `policy_pack_version`
- `evaluated_at`
- `status` (`pass|fail|warn`)
- `violations[]` (rule id, message, path)
- `artifacts[]` (links to reports)

✅ **Goal:** “Policy checks are part of the evidence” 🛡️

---

## How this maps to KFM’s evidence stack

KFM’s “evidence triplet” concept can be represented like this:

- **STAC** → *spatiotemporal assets + footprints + checksums* 🛰️  
- **DCAT** → *dataset discovery + licensing + distributions* 📦  
- **PROV** → *lineage: inputs → transforms → outputs (agents + time)* 🧬  

This example’s schemas should encourage:

- Evidence items that **reference** STAC/DCAT/PROV records (instead of duplicating them)
- A manifest that captures **queries + transformations** needed for reproducibility
- A PulseThread that stays “lightweight” and points to the manifest & provenance bundle

---

## Validation

### ✅ Node (AJV)

```bash
npm i -D ajv ajv-formats
npx ajv validate \
  -s ./pulse_thread.schema.json \
  -d ../examples/pulse.thread.json \
  --all-errors
```

### ✅ Python (jsonschema)

```bash
python -m pip install jsonschema
python -m jsonschema \
  -i ../examples/pulse.thread.json \
  ./pulse_thread.schema.json
```

### ✅ CI idea (recommended)

- Validate all `*.schema.json` (meta-validation)
- Validate example data against schemas
- Run OPA/Conftest policies on manifest outputs

---

## Schema rules & conventions

**🧱 JSON Schema draft**
- Prefer **Draft 2020-12**
- Use `$id` and `$schema`
- Centralize reusable bits in `$defs/` (or `common/`)

**🔒 Strictness**
- Default to `additionalProperties: false` on core objects
- Use `unevaluatedProperties: false` when composing schemas

**🆔 IDs**
- All IDs should be **stable** and **globally unique** (URI-ish strings)
- Prefer hash-friendly identifiers for manifests/items (works great with signing)

**🔐 Integrity**
- If bytes exist: include `sha256`
- For JSON manifests: consider a canonical digest (RFC 8785 style) for idempotency

**🧭 Provenance-first**
- Don’t allow “anonymous” evidence items  
- Don’t allow derived outputs without a transformation chain

**🧠 AI transparency**
- If `kind=model_output`, require:
  - model identifier/version
  - prompt or prompt hash (if sensitive)
  - citations to *input* evidence items
  - human review status (optional but ideal)

**🧨 Privacy & sensitivity**
- Provide optional fields for:
  - `classification` / `sensitivity`
  - `access` (who can see it)
  - `redactions` (what was removed)
- Avoid storing PII in manifests; store pointers and hashes instead.

---

## Examples

### PulseThread (JSON)

```json
{
  "type": "PulseThread",
  "id": "kfm:pulse:2026-01-10:smoky-hill-river:water-level-spike",
  "title": "Water levels spike near Salina after heavy rainfall",
  "status": "draft",
  "created_at": "2026-01-10T03:14:15Z",
  "updated_at": "2026-01-10T03:20:00Z",
  "geo": {
    "bbox": [-97.70, 38.80, -97.40, 39.00],
    "place_refs": ["kfm:place:salina-ks", "kfm:hydro:smoky-hill-river"]
  },
  "time": { "observed_at": "2026-01-10T02:50:00Z" },
  "summary": "Gauge readings show a rapid rise over ~3 hours.",
  "evidence": {
    "manifest_ref": "../evidence/EM-84.yaml",
    "prov_ref": "../prov/PR-84.jsonld",
    "citations": ["ev:usgs-nwis:station-06869500:reading:2026-01-10T02:50:00Z"]
  },
  "authorship": {
    "created_by": { "agent_type": "watcher", "agent_id": "kfm:agent:wpe-watcher" },
    "reviewed_by": [{ "agent_type": "human", "agent_id": "kfm:agent:curator:jdoe" }]
  },
  "tags": ["hydrology", "weather"]
}
```

### EvidenceManifest (YAML)

```yaml
schema_version: 0.1.0
manifest_id: "sha256:1f0b...cafe"
thread_id: "kfm:pulse:2026-01-10:smoky-hill-river:water-level-spike"
generated_at: "2026-01-10T03:14:16Z"

items:
  - evidence_id: "ev:usgs-nwis:station-06869500:reading:2026-01-10T02:50:00Z"
    kind: "query_result"
    retrieved_at: "2026-01-10T03:10:00Z"
    source:
      type: "dcat_dataset"
      id: "kfm:dcat:usgs-nwis"
    query:
      endpoint: "https://waterservices.usgs.gov/nwis/iv/"
      params:
        sites: "06869500"
        parameterCd: "00065"
        format: "json"
    extracts:
      - type: "jsonpath"
        path: "$.value.timeSeries[0].values[0].value[0]"
    checksums:
      sha256: "3b2a...deadbeef"

transformations:
  - step: "normalize_units"
    tool: "kfm-etl"
    tool_version: "11.0.0"
    input_evidence_ids:
      - "ev:usgs-nwis:station-06869500:reading:2026-01-10T02:50:00Z"
```

---

## Extension hooks

If you want to go “full audit mode” 🚀:

- 🧾 **Supply chain / signatures:** add `cosign` signatures, in-toto attestations, SBOM pointers
- 📦 **OCI artifact references:** store large artifacts in an OCI registry; link them from evidence items
- 🧠 **Uncertainty:** attach `confidence`, `error_bars`, ensembles, assumptions
- 🔐 **Sensitive knowledge protocols:** embed `sensitivity_reason`, `authority`, `ethics_notes`

---

## Related docs & references

In the wider KFM project, these concepts connect to:

- 📥 **Data Intake** (provenance-first ETL, immutability, STAC/DCAT/PROV)
- 🧭 **AI / Focus Mode** (citations + governance rules)
- 🖥️ **UI system** (evidence panels, provenance surfacing)
- 🧪 **MCP / Dev Provenance** (reproducible research + experiment contracts)

> Search the repo for: `STAC`, `DCAT`, `PROV`, `evidence_manifest`, `PulseThread`, `OPA`, `Conftest`, `MCP`.
