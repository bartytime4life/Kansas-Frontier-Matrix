# 📐 Shared Schemas — `dev_prov` Examples

[![JSON Schema](https://img.shields.io/badge/JSON%20Schema-Draft%202020--12-blue)](https://json-schema.org/)
[![Contract First](https://img.shields.io/badge/Contract--First-%E2%9C%85-brightgreen)](#-design-principles)
[![Provenance First](https://img.shields.io/badge/Provenance--First-%F0%9F%94%8D-important)](#-cross-layer-linking-rules)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-%F0%9F%9B%A1%EF%B8%8F-purple)](#-governance--policy-gates)

> **Goal:** keep *every* artifact in the `mcp/dev_prov` examples **machine-validatable**, **diff-friendly**, and **traceable** — from data catalogs (STAC/DCAT), to lineage (PROV), to Story Nodes, to Focus Mode outputs, to CI/WPE audit trails.

---

## 📘 Overview

This folder contains **shared JSON Schemas** used by the `mcp/dev_prov` example suite (and any other examples that opt-in). These schemas are designed around the KFM philosophy:

- **Contract-first:** artifacts must match an explicit schema (no “mystery fields”, no silent drift).
- **Provenance-first:** if it appears in UI / APIs / Focus Mode, it must be traceable to cataloged sources and logged lineage.
- **Governance-by-default:** fields exist for license, classification, sensitivity, and sovereignty-aware controls (enforced by CI policy gates).
- **Composable narratives:** Story Nodes + Evidence Manifests + PROV bundles link “the story” to “the data” in a way that is auditable and explorable.

> 🧠 Tip: JSON Schema is the *structural* gate. “Deep” rules (e.g., link resolution, forbidden secrets, license allowlists, “fail closed” governance) are typically enforced by **Policy-as-Code** (OPA/Rego + Conftest) and custom checkers.

---

## 🗂️ Directory layout

```text
📁 mcp/dev_prov/examples/_shared/
└── 📁 schemas/
    ├── 📄 README.md  👈 you are here
    ├── 📄 *.schema.json
    └── 📁 _defs/     (optional) shared $defs / vocab enums / reusable fragments
```

### What belongs here ✅
- Schemas that are **shared across multiple examples** (avoid duplication).
- Schemas that represent **stable contracts** for common artifacts:
  - Catalog records (STAC/DCAT profiles)
  - Provenance bundles (PROV + KFM extensions)
  - Evidence manifests (citations + asset refs)
  - Run manifests (audit trail + canonical hash)
  - WPE events (Watcher/Planner/Executor records)
  - Story configs (Story Nodes / Pulse Threads / narrative segments)
  - Telemetry reports (CI traces, energy/carbon, health checks)

### What does *not* belong here ❌
- One-off experiment schemas that only a single example needs (keep local).
- Deprecated schemas (move to an archive folder with clear labels).

---

## 🧬 Schema families

> This is a **recommended index** of schema families for `dev_prov`-style examples.  
> If the folder contents diverge, update this table to reflect the actual files present.

| Family | Typical schema(s) | What it validates | Why it exists |
|---|---|---|---|
| 🗺️ Catalog | `stac_item.kfm.schema.json`, `stac_collection.kfm.schema.json` | STAC Items/Collections with KFM-required extensions (`kfm:*`) | Make map layers “the map behind the map” (traceable, discoverable) |
| 🧾 Dataset Registry | `dcat_dataset.kfm.schema.json` | DCAT Dataset records w/ sovereignty/sensitivity flags | A governance-aware dataset registry (license, access, provenance links) |
| 🔗 Provenance | `prov_bundle.kfm.schema.json` | PROV(-O) JSON-LD bundles + KFM agent roles | “No output without lineage” across pipelines + AI outputs |
| 🧪 Runs / Audits | `run_manifest.schema.json` | Deterministic run manifests (inputs/outputs/versions + canonical digest) | Idempotent, reproducible pipelines; PR diffs that are reviewable |
| 🧾 Evidence | `evidence_manifest.schema.json` | Evidence packs: citations + artifact refs + checksums | Story Nodes / Focus Mode can cite exact sources & assets |
| 🧵 Narrative | `story_node.schema.json`, `pulse_thread.schema.json`, `concept_attention_node.schema.json` | Structured stories + micro-threads linked to evidence | Turn narrative into auditable data (no floating claims) |
| 🤖 AI Outputs | `focus_mode_response.schema.json` | Answer + citations + entities used + refusal modes | Explainable, cite-first AI (“show your work”) |
| 🛡️ Governance / Policy | `policy_result.schema.json`, `governance_card.schema.json` | Policy checks & allowlists (licenses, required fields, sensitivity) | CI gates that “fail closed” & encode FAIR/CARE rules |
| 📡 Telemetry | `telemetry_event.schema.json`, `telemetry_health.schema.json` | NDJSON events, CI traces, energy/carbon reports | QA at the meta-level (runs are measurable & accountable) |
| 🧰 Design Packs | `sample_unit_spec.schema.json`, `preprocess_spec.schema.json`, `metric_spec.schema.json` | Domain-specific specs referenced by provenance | Make niche domain assumptions explicit + versioned |

---

## 🧷 Cross-layer linking rules

These rules prevent “drift” between catalogs, provenance, the graph, and the UI.

### 1) One **Dataset ID** to rule them all 🔑
A dataset’s canonical identifier should be present (or derivable) across:
- **DCAT** record (dataset registry)
- **STAC** Items/Collections (spatial assets)
- **PROV** bundles (lineage)
- **Graph** entities (Neo4j nodes/edges)
- **UI** layer panels + exports

**Rule of thumb:** if you can’t link it across layers, it’s not “publishable”.

### 2) Classification & sensitivity are first-class 🛡️
Every artifact that can be surfaced should carry:
- `classification` (public / restricted / embargoed / etc.)
- `sensitivity` flags (PII, cultural protocols, site-protection, etc.)
- (optional) sovereignty-aware controls (CARE-aligned)

**Why:** The UI and API can enforce RBAC/ABAC and apply obfuscation or redaction rules without guessing.

### 3) Evidence is structured (no orphan citations) 🧾
A **claim** should be backed by an Evidence Manifest entry that includes:
- stable `id`
- `uri` (catalog ID, URL, or artifact reference)
- `checksum` (or digest)
- `cite_as` / `label`
- optional `excerpt` / `query` / `page_span` (for precise traceability)

### 4) Runs are deterministic (hashable) 🔁
Run manifests should be **canonicalized** (e.g., RFC 8785 JSON Canonicalization) before hashing so:
- the same run content produces the same digest,
- CI can be idempotent,
- provenance can point to an immutable activity identifier.

---

## ✅ Validation & tooling

### Fast local validation (pick your stack)

#### Node / TypeScript (Ajv)
```bash
# Install once (repo root)
npm i -D ajv ajv-formats ajv-cli

# Validate a JSON artifact against a schema
npx ajv validate \
  -s mcp/dev_prov/examples/_shared/schemas/run_manifest.schema.json \
  -d path/to/run_manifest.json \
  --spec=draft2020 \
  --all-errors
```

#### Python (jsonschema)
```bash
python -m pip install jsonschema referencing

python -m jsonschema \
  -i path/to/run_manifest.json \
  mcp/dev_prov/examples/_shared/schemas/run_manifest.schema.json
```

### YAML support 🧩
If an artifact is authored as YAML (common for manifests/config), validate by:
1) parsing YAML → JSON (no transformations), then  
2) validating the resulting JSON against the schema.

> ✅ Pro-tip: Keep YAML keys identical to the JSON contract. Don’t “simplify away” required keys — use `"TBD"` / `"n/a"` defaults so tooling stays stable.

---

## 🔐 Governance & policy gates

Schemas define **shape**; policy gates enforce **rules**. Typical gates include:

- ✅ **License required** (and matches an allowlist, e.g., SPDX strings)
- ✅ **Required provenance** exists before publication (no bypass)
- ✅ **No secrets** in JSON/YAML (regex scanning + allowlists)
- ✅ **Sensitive data handling** (classification required; obfuscation rules)
- ✅ **Supply-chain attestations** for artifacts (e.g., signature refs)

**Design stance:** “fail closed” by default.  
If the system can’t verify compliance, it refuses to publish.

---

## 🧠 `dev_prov` patterns: WPE (Watcher → Planner → Executor)

Many examples model changes as **auditable events**:

- **Watcher** creates an immutable alert (what was observed, with evidence).
- **Planner** proposes a patch/PR (what should change, why, with constraints).
- **Executor** applies change via PR/CI (what changed, proof it passed gates).

If you maintain schemas for WPE events, keep them:
- append-only friendly (NDJSON compatible),
- signed/verifiable (optional signature refs),
- linkable to `run_id`, `dataset_id`, and evidence.

---

## 🧪 Example artifacts

> Examples below are **illustrative** (use your exact schema filenames/fields).  
> Keep them tiny, deterministic, and reviewable.

### 1) Evidence Manifest (YAML-friendly)
```yaml
id: kfm.ev.2026-01-21.ks-river-topeka
title: "Kansas River @ Topeka — Evidence Pack"
classification: public
created_at: "2026-01-21T00:00:00Z"
created_by: "planner.agent"

items:
  - id: kfm.ds.usgs.nwis@2026-01-21
    kind: dcat_dataset
    uri: "dcat://kfm.ds.usgs.nwis@2026-01-21"
    cite_as: "USGS NWIS — Real-time Water Data"
    checksum:
      algo: sha256
      value: "0000000000000000000000000000000000000000000000000000000000000000"

  - id: kfm.asset.pmtiles.ks-hydro@sha256:deadbeef
    kind: stac_asset
    uri: "oci://registry.example/kfm/pmtiles/ks-hydro@sha256:deadbeef"
    media_type: "application/vnd.pmtiles"
    signature:
      cosign_ref: "oci://registry.example/kfm/pmtiles/ks-hydro:cosign.sig"
```

### 2) Run Manifest (deterministic + self-fingerprinting)
```json
{
  "run_id": "kfm.run.2026-01-21T000000Z.1a2b3c",
  "run_time": "2026-01-21T00:00:00Z",
  "idempotency_key": "sha256:.................................................................",
  "canonical_digest": "sha256:.................................................................",
  "source_urls": ["https://example.org/source.csv"],
  "tool_versions": {
    "pipeline": "kfm-pipelines@1.2.3",
    "python": "3.12.x"
  },
  "summary_counts": {
    "records_in": 1234,
    "records_out": 1200,
    "errors": 0
  },
  "outputs": [
    {
      "kind": "stac_item",
      "id": "kfm.stac.item.ks-hydro@2026-01-21",
      "path": "data/catalog/stac/items/ks-hydro/2026-01-21.json"
    }
  ]
}
```

### 3) Focus Mode response (answer + citations + trace)
```json
{
  "question": "What’s the current water level of the Kansas River at Topeka?",
  "answer": "As of 2026-01-21T00:00:00Z, the latest reading is X (units).",
  "classification": "public",
  "citations": [
    {
      "evidence_id": "kfm.ev.2026-01-21.ks-river-topeka",
      "item_id": "kfm.ds.usgs.nwis@2026-01-21",
      "cite_as": "USGS NWIS — Real-time Water Data"
    }
  ],
  "used_entities": [
    { "kind": "place", "id": "kfm.place.topeka-ks" },
    { "kind": "station", "id": "kfm.sensor.usgs.topeka-gauge" }
  ],
  "prov_ref": "prov://kfm.run.2026-01-21T000000Z.1a2b3c"
}
```

### 4) Story Node front matter (schema-validated narrative)
```markdown
---
id: kfm.story.santa-fe-trail.001
title: "Santa Fe Trail — A Day in 1850"
classification: public
evidence_manifest: ../evidence/kfm.ev.santa-fe-trail.yaml

timeline:
  start: "1846-01-01"
  end: "1855-12-31"

map_state:
  mode: "2d"
  center: [-96.5, 38.5]
  zoom: 6

pulse_threads:
  - id: kfm.pulse.sft.railroad-shift
    concept_attention_nodes:
      - id: kfm.can.transport-rail
        claim: "Rail expansion shifted trade routes."
        evidence_item_ids: ["kfm.ds.rail.lines@1850"]
---

# Santa Fe Trail — A Day in 1850

(Story content…)
```

---

## 🧱 Extending & versioning

### Versioning rules (SemVer) 🧷
- **MAJOR**: breaking changes (required fields changed/removed, semantics changed)
- **MINOR**: backward-compatible additions (new optional fields)
- **PATCH**: clarifications / tighter validation that doesn’t break valid existing data

### Extension strategy 🧩
- Prefer **namespaced fields** for custom extensions (`kfm:*`, or `x_kfm_*` depending on your layer).
- Keep schemas **strict** where possible:
  - `additionalProperties: false` (or `unevaluatedProperties: false` for 2019-09/2020-12)
- Push “complex” constraints into:
  - policy pack rules (OPA/Rego),
  - link checkers,
  - graph integrity checks.

### Definition of Done ✅
When adding/updating a schema:
- [ ] Schema has a stable `$id` and targets one JSON Schema draft.
- [ ] At least **one minimal fixture** passes.
- [ ] At least **one negative fixture** fails (proves the gate works).
- [ ] CI validation is wired (Ajv/jsonschema + policy pack if applicable).
- [ ] README table/index updated (so humans can find it).
- [ ] Any related vocab/enum updates are PR-reviewed (no “silent” widenings).

---

## 🧰 Troubleshooting

**“It validates locally but fails in CI.”**
- CI may be using a different JSON Schema draft or validator config.
- CI may be enforcing policy rules beyond schema (licenses, secrets, link resolution).

**“We need cross-file constraints (e.g., dataset_id must exist).”**
- JSON Schema won’t reliably enforce repository-wide joins.  
  Use a link checker or policy pack rule (fail closed).

**“YAML vs JSON differences broke validation.”**
- Ensure YAML parses to the exact JSON structure (no implicit typing surprises).
- Avoid key omission; prefer `"TBD"`/`"n/a"` placeholders over deleting required fields.

---

## 📚 References & further reading

<details>
<summary><strong>📌 KFM-aligned concepts these schemas support</strong> (click to expand)</summary>

- **STAC / DCAT / PROV profiles** for catalogs + lineage (plus KFM-required extension fields).
- **Story Nodes** as structured narratives linked to evidence.
- **Pulse Threads / Conceptual Attention Nodes** to turn narrative into auditable micro-claims.
- **OCI artifact distribution + signatures** (treat data artifacts like versioned, verifiable releases).
- **Policy-as-code** gates that fail closed (licenses, sensitivity, secrets, provenance required).
- **WPE automation** (Watcher/Planner/Executor) with immutable, reviewable records.
- **UI transparency** (“map behind the map”) and explainable AI outputs with citations.
- **Offline packs & future AR/4D extensions** (schemas keep packaging sane as features expand).
</details>
