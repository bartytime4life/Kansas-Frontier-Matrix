# 🧩 KFM API Shared Contracts (`api/src/contracts/_shared`)

![contracts](https://img.shields.io/badge/contracts-_shared-blue)
![contract--first](https://img.shields.io/badge/contract--first-enforced-success)
![evidence](https://img.shields.io/badge/evidence-STAC%20%2B%20DCAT%20%2B%20PROV-brightgreen)
![policy](https://img.shields.io/badge/policy-OPA%20%2B%20Conftest-purple)

> [!IMPORTANT]
> **Anything exposed via the API (and therefore the UI + Focus Mode) must be contract-valid, policy-allowed, and provenance-linked.**  
> If it can’t be traced to cataloged evidence, it doesn’t ship. 🚫🕵️‍♂️

## 🎯 Why this folder exists

`_shared/` is the **single source of truth** for cross-cutting API contract primitives used by **every** endpoint and domain contract.

This includes (but isn’t limited to):

- 🧾 **API envelopes** (success/error shape + request metadata)
- 🧨 **Error codes** (policy denies, validation errors, not found, etc.)
- 🆔 **IDs & URNs** (dataset IDs, document UUID URNs, run IDs)
- 🗺️ **Geospatial primitives** (GeoJSON geometry, bbox, CRS hints)
- ⏱️ **Time primitives** (ISO datetimes, intervals)
- 🔗 **Links & references** (evidence refs + hypermedia links)
- 📚 **Evidence & provenance** (STAC/DCAT/PROV triplet, run manifests, artifact distribution)
- 🛡️ **Access + sensitivity + licensing** (FAIR/CARE fields, classification, restrictions)

If you’re authoring a new contract under `api/src/contracts/**`, you **should be importing from here** (not redefining your own versions).

---

## 🧭 Contract philosophy baked into `_shared`

KFM is built around a few non-negotiables:

### 1) 📦 Contract-first
Every dataset (and many other artifacts) must have a **metadata contract** (schema + validators) before it’s accepted or published. That makes downstream systems reliable and automatable (attribution, citations, story references, etc.). ✅

### 2) 🧾 Evidence-first publishing
“Published” means: you have **the evidence triplet** available and cross-linked:

- **STAC** (spatiotemporal assets)
- **DCAT** (data catalog entry)
- **PROV** (lineage/provenance)

These three are treated as **auditable boundary artifacts** (versioned and reviewable like code). 🔍🧬

### 3) 🛡️ Policy-as-code gatekeeping
Access control, sensitivity controls, licensing requirements, and promotion rules are enforced via policy gates (OPA/Conftest).  
Contracts must expose enough metadata for these gates to operate deterministically. ⚖️

---

## 🗂️ Expected layout

This folder is intentionally small and foundational. Keep it **generic** and **domain-agnostic**.

```text
api/src/contracts/_shared/
├─ README.md 📘
├─ envelope.* 📦        # response wrappers + request metadata
├─ errors.* 💥          # error codes + error details
├─ ids.* 🆔             # dataset ids, urns, opaque ids
├─ time.* ⏱️            # iso datetimes + intervals
├─ geo.* 🗺️             # geojson + bbox + crs
├─ links.* 🔗           # hypermedia + evidence refs
├─ pagination.* 📄      # cursor/page primitives
├─ provenance.* 🧾      # STAC/DCAT/PROV + manifests + artifact refs
├─ access.* 🛡️          # classification, license, restrictions
└─ index.* 🧩           # re-exports (recommended)
```

> [!NOTE]
> `*` indicates “whatever your contract layer uses” (TypeScript, Pydantic/Python, JSON Schema, etc.).  
> Keep exports stable; treat changes like API changes. 🧯

---

## 🧱 Import rules

✅ Allowed:
- `contracts/<domain>/*` → imports from `_shared/*`
- `_shared/*` → imports from other `_shared/*`

🚫 Not allowed:
- `_shared/*` → importing any domain-specific contract
- Cross-domain imports (`contracts/maps/*` importing from `contracts/story/*`, etc.) unless mediated through `_shared`

This prevents circular coupling and keeps contracts reusable. 🔄❌

---

## 🧬 Core primitives

<details>
<summary><strong>🆔 IDs & URNs</strong></summary>

### Dataset IDs
Dataset IDs are **stable**, **human-readable**, and **versioned**.

Example:
- `kfm.ks.landcover.2000_2020.v1`

**Guidelines:**
- Prefer dot-separated segments: `<org>.<region>.<theme>.<timespan>.v<major>`
- Never recycle an ID for a meaningfully different dataset
- Consider using separate fields for:
  - `dataset_id` (semantic ID)
  - `dataset_version` (semantic version)
  - `dataset_revision` (content hash / digest, optional)

### Document UUID URNs
Documents and internal references should use URN-style UUIDs.

Example:
- `urn:kfm:doc:guides:data-ingestion:v1.2.0`

### Run IDs / Job IDs
Pipeline runs, agent actions, and derived artifacts should include a stable `run_id` (UUID-like) to support deterministic replay and auditing.

</details>

<details>
<summary><strong>⏱️ Time</strong></summary>

Preferred time representations:
- `IsoDate` → `YYYY-MM-DD`
- `IsoDateTime` → ISO-8601 UTC timestamp (e.g., `2026-01-23T18:07:12Z`)
- `TimeInterval` → `{ start, end }` (inclusive start, inclusive end unless explicitly stated)

> [!TIP]
> If you’re carrying temporal metadata for a dataset or story node, prefer explicit intervals over ambiguous “date” fields.

</details>

<details>
<summary><strong>🗺️ Geo</strong></summary>

### GeoJSON
Use GeoJSON geometries for map-facing contracts wherever possible.

**Conventions:**
- Default coordinates in **WGS84 / EPSG:4326** (lat/long) for interoperability 🌍
- `bbox` is `[minLon, minLat, maxLon, maxLat]`

### CRS handling
If you ingest in another CRS, capture the original CRS in metadata but normalize outputs for distribution unless a specific endpoint requires otherwise.

> [!WARNING]
> If classification/sensitivity requires it, geometry may be **generalized**, **masked**, or omitted entirely. That decision is policy-driven, not contract-driven — but contracts must support it.

</details>

<details>
<summary><strong>📦 Response envelope</strong></summary>

All JSON endpoints should return a consistent envelope for:
- request tracing 🧵
- safe evolution over time 🧬
- warnings + partial results ⚠️
- policy diagnostics (when allowed) 🛡️

Recommended shape:

```json
{
  "ok": true,
  "meta": {
    "request_id": "req_01H...",
    "trace_id": "trace_01H...",
    "generated_at": "2026-01-23T18:07:12Z",
    "warnings": []
  },
  "data": { }
}
```

Failure shape:

```json
{
  "ok": false,
  "meta": {
    "request_id": "req_01H...",
    "trace_id": "trace_01H...",
    "generated_at": "2026-01-23T18:07:12Z"
  },
  "error": {
    "code": "POLICY_DENY",
    "message": "Access denied by policy.",
    "details": { "policy_id": "KFM-POLICY-..." }
  }
}
```

> [!NOTE]
> If you already implement RFC7807 “Problem Details”, keep it — but still wrap or normalize in a predictable `_shared` envelope so clients don’t need one-off handling.

</details>

<details>
<summary><strong>💥 Errors</strong></summary>

Prefer stable **error codes** over fragile message parsing.

Suggested structure:
- `code` (string enum)
- `message` (human-readable)
- `details` (structured info safe to expose)
- `fields` (optional: validation errors)
- `retryable` (optional: boolean)

Common KFM-flavored codes:
- `VALIDATION_ERROR`
- `NOT_FOUND`
- `CONFLICT`
- `POLICY_DENY` 🛡️
- `RATE_LIMITED`
- `UPSTREAM_ERROR`
- `INTERNAL`

</details>

<details>
<summary><strong>📄 Pagination</strong></summary>

Prefer cursor-based pagination for catalogs and graph queries:

```json
{
  "items": [],
  "page": {
    "cursor": "cur_...",
    "next_cursor": "cur_...",
    "limit": 50
  }
}
```

Optional fields (only if feasible and not expensive):
- `total_estimate`
- `has_more`

</details>

<details>
<summary><strong>🔗 Links & references</strong></summary>

Use a consistent link shape so clients can traverse related artifacts:

```json
{
  "rel": "stac",
  "href": "/data/stac/collections/kfm.ks.landcover.2000_2020.v1.json",
  "type": "application/json",
  "title": "STAC Collection"
}
```

Recommended `rel` values:
- `self`
- `stac`
- `dcat`
- `prov`
- `license`
- `download`
- `thumbnail`

</details>

<details>
<summary><strong>🧾 Provenance & evidence</strong></summary>

### The evidence triplet
Expose evidence references in a consistent way:

```json
{
  "evidence": {
    "stac": { "href": "...", "type": "application/json" },
    "dcat": { "href": "...", "type": "application/ld+json" },
    "prov": { "href": "...", "type": "application/json" }
  }
}
```

### Run manifests & deterministic replay
When an output is derived (pipelines, analytics, AI summaries), include:
- `run_manifest` (inputs, params, environment, outputs)
- `evidence_manifest` (ties derived result back to STAC/DCAT/PROV)

If you generate digests/hashes, prefer canonical JSON (RFC 8785 style canonicalization) before hashing so the digest is stable across serialization differences.

### Artifact distribution
When artifacts are promoted/distributed:
- allow `oci` distribution metadata (repo/tag/digest/mediaType)
- allow `http` distribution metadata (url/sha256/size/contentType)
- allow optional signature metadata (e.g., cosign)

</details>

<details>
<summary><strong>🛡️ Access, classification, licensing</strong></summary>

Contracts must provide enough metadata for governed access and attribution:

**Common fields:**
- `license` (required for public-ish datasets)
- `attribution` / `credits`
- `classification` (e.g., `public`, `sensitive`, `restricted`, `confidential`)
- `restrictions` (array of structured constraints)
- `care_label` / `ethics_notes` (for CARE-aligned handling)

> [!IMPORTANT]
> If policy denies access or requires redaction/generalization, clients should still receive a *stable shape*:
> - either a policy error (`POLICY_DENY`)
> - or a redacted payload with explicit flags (e.g., `redacted: true` + reason category)

</details>

<details>
<summary><strong>🤖 Agent actions & AI transparency</strong></summary>

If an AI agent proposes or contributes transformations:
- log it as an `AgentAction` artifact in provenance
- require labeling + citations for AI-generated narrative
- ensure humans review changes (PR-based workflows)

Suggested fields:
- `agent_id`
- `agent_version`
- `action_type`
- `inputs` / `outputs`
- `rationale`
- `citations[]` (each referencing evidence by URN/link)

</details>

---

## 🧠 Contract boundary diagram

```mermaid
flowchart LR
  Client[🧑‍💻 Client / UI / External Integrators] -->|REST / GraphQL| API[🧱 API Boundary]
  API -->|validate| Contracts[🧩 Contracts (_shared + domains)]
  API -->|policy| Policy[🛡️ OPA / Conftest]
  API -->|read| Catalogs[📚 Evidence Triplet]
  Catalogs --> STAC[🛰️ STAC]
  Catalogs --> DCAT[🏷️ DCAT]
  Catalogs --> PROV[🧾 PROV]
  API -->|serve| Response[📦 Stable Envelopes + Evidence Links]
```

---

## 🧪 Example payloads

### ✅ Dataset summary with evidence triplet

```json
{
  "ok": true,
  "meta": {
    "request_id": "req_01H...",
    "trace_id": "trace_01H...",
    "generated_at": "2026-01-23T18:07:12Z",
    "warnings": []
  },
  "data": {
    "dataset_id": "kfm.ks.landcover.2000_2020.v1",
    "title": "Kansas Landcover 2000–2020",
    "classification": "public",
    "extent": {
      "spatial": { "bbox": [-102.05, 36.99, -94.59, 40.00] },
      "temporal": { "start": "2000-01-01", "end": "2020-12-31" }
    },
    "evidence": {
      "stac": { "rel": "stac", "href": "/data/stac/collections/kfm.ks.landcover.2000_2020.v1.json", "type": "application/json" },
      "dcat": { "rel": "dcat", "href": "/data/catalog/dcat/kfm.ks.landcover.2000_2020.v1.jsonld", "type": "application/ld+json" },
      "prov": { "rel": "prov", "href": "/data/prov/kfm.ks.landcover.2000_2020.v1.json", "type": "application/json" }
    }
  }
}
```

### ❌ Policy-denied response

```json
{
  "ok": false,
  "meta": {
    "request_id": "req_01H...",
    "trace_id": "trace_01H...",
    "generated_at": "2026-01-23T18:07:12Z"
  },
  "error": {
    "code": "POLICY_DENY",
    "message": "Access denied by policy.",
    "details": {
      "category": "sensitivity",
      "hint": "Request a redacted/generalized variant or request access."
    }
  }
}
```

---

## ✅ Checklist for contract changes

Before you merge anything that modifies `_shared`:

- [ ] 🧩 Reuse existing primitives instead of redefining
- [ ] 🧯 Treat changes as **potentially breaking** (review carefully)
- [ ] 🧪 Add/adjust contract tests and fixtures (golden examples)
- [ ] 🛡️ Run policy checks (OPA/Conftest) locally and in CI
- [ ] 🧾 Ensure evidence linkability (STAC/DCAT/PROV) where relevant
- [ ] 🔏 Ensure licensing + attribution metadata is present where required
- [ ] 🧠 For AI-facing outputs, ensure labeling + citations support exists
- [ ] 📚 Update any docs/templates impacted by the contract shape

---

## 🔗 Related docs

> These are the “north star” references for how contracts + governance fit together.

- 📘 Master Guide: `/docs/MASTER_GUIDE_v13.md`
- 🧾 Data contracts & examples: `/docs/data/contracts/examples/`
- 🛡️ Policy Pack: `/api/scripts/policy/`
- 🗃️ Evidence triplet roots:
  - `/data/stac/`
  - `/data/catalog/dcat/`
  - `/data/prov/`
- 🧰 Templates:
  - `/docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`

---

## 🧠 Keep it boring on purpose

Shared contracts are where “boring” becomes a superpower:
- fewer one-off client bugs 🐛⬇️
- easier governance enforcement ⚖️
- safer public release flows 🚦
- durable interoperability with external tools 🌐

When in doubt: **add it to `_shared`, test it, document it, and keep it stable.** ✅

