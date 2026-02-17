<!--
KFM Governed Artifact
Path: data/registry/datasets/schemas/README.md
Status: DRAFT (until first CI gate + fixtures are wired)
-->

# 🧾 Dataset Schemas (Registry + Contracts)

![Governed](https://img.shields.io/badge/governance-governed-blue)
![Fail--Closed](https://img.shields.io/badge/policy-fail--closed-critical)
![JSON%20Schema](https://img.shields.io/badge/json--schema-draft_2020--12-informational)
![Contracts](https://img.shields.io/badge/contracts-registry%20%2B%20dataset%20outputs-brightgreen)

This directory contains **machine-validatable dataset contracts** that back KFM’s “registry-driven” integration approach:

- the **dataset registry** is the driver of ingestion work and promotion gates
- schemas make that registry **enforceable** in CI, not “policy-by-document” only

> [!IMPORTANT]
> **Fail‑closed rule:** If a payload (registry entry, processed output, or governed API slice) does **not** validate against the applicable schema, treat it as **untrusted** and **block promotion**.

---

## 📌 What lives here

### 1) Dataset registry schemas
Schemas that define the **shape and required fields** for dataset registry entries (metadata, policy labels, cadences, schema refs, etc.).

### 2) Dataset output schemas
Schemas that define the **canonical processed output contract** for a dataset (required fields, types, geometry expectations, and “what’s allowed to exist” at the structural level).

### 3) Fixtures (required)
Small example payloads used by CI to prove the schema works:

- `fixtures/valid/*.json` MUST pass
- `fixtures/invalid/*.json` MUST fail

> [!NOTE]
> Repo-wide, cross-cutting schemas (STAC/DCAT/PROV, Story Nodes, UI/telemetry contracts, run receipts/manifests, watcher registry) are expected to live under the top-level `schemas/` directory per the global directory layout. This folder is specifically **dataset registry + dataset contracts**.  
> If your repo consolidates everything under `/schemas`, treat this directory as an “onboarding kit” mirror and keep **one source of truth**.  

---

## 🗂️ Directory layout

```text
data/registry/datasets/
└── schemas/
    ├── README.md
    ├── dataset_registry_entry.v1.schema.json        # (recommended) contract for registry entries
    ├── dataset_contract_index.v1.schema.json        # (optional) references per-dataset schema files
    ├── fixtures/                                    # (recommended) shared fixtures for registry schema(s)
    │   ├── valid/
    │   └── invalid/
    ├── <dataset_id>.processed.v1.schema.json        # single-table datasets
    └── <dataset_id>/                                # multi-table / multi-layer datasets (optional)
        ├── processed.v1.schema.json
        ├── api_payload.v1.schema.json               # optional: governed API response “slice”
        └── fixtures/
            ├── valid/
            └── invalid/
```

> [!TIP]
> If a dataset produces multiple layers/tables, prefer a `<dataset_id>/` folder so contracts + fixtures stay together.

---

## 🔁 Contract flow (how schemas gate promotion)

```mermaid
flowchart LR
  R[Dataset registry entry] -->|declares schema refs| P[Pipeline run]
  P --> O[Processed outputs]
  O --> V[Schema validation]
  V -->|pass| G[Policy gates (deny-by-default)]
  V -->|fail| X[BLOCK: untrusted]
  G -->|pass| C[Write catalogs (DCAT/STAC/PROV)]
  G -->|deny| X
  C --> S[Serve via governed API boundary]
```

---

## 🧱 Naming & versioning rules

### File naming

Use **major-versioned** filenames:

- lowercase
- `snake_case` (or `kebab-case`, but be consistent)
- `v<MAJOR>` in the filename
- `.schema.json` suffix

Examples:

- `dataset_registry_entry.v1.schema.json`
- `soils.ssurgo.processed.v1.schema.json`
- `historical.kansas_memory.processed.v2.schema.json`

### Versioning policy

- **Breaking change** ⇒ add a new major file (`v1` → `v2`), keep the old file.
- **Non-breaking extensions** (new optional fields) may stay in the same major version, but:
  - fixtures MUST be updated
  - CI MUST prove both “typical” and “minimal” payloads still validate

> [!WARNING]
> Do not “quietly” break old payloads. In a governed system, backwards compatibility is a trust issue.

---

## 📐 Schema style guide

### JSON Schema baseline

- JSON Schema **Draft 2020-12**
- Prefer `"additionalProperties": false` on objects (fail closed)
- Require `title` + `description`
- Prefer explicit `required` lists
- Avoid overly broad regexes for IDs

### Deterministic identity (`spec_hash`) and reproducibility

When KFM hashes a governed “spec” (schema, registry entry, pipeline config):

- **canonicalize** the JSON first (JCS / RFC 8785 style canonicalization)
- hash with **SHA‑256**
- store the result as `spec_hash` in evidence (run receipts/manifests)

This prevents false diffs from key ordering/whitespace and makes signatures/attestations stable.

<details>
<summary>Suggested (proposed) `$id` / `$schema` conventions</summary>

- `$schema`: `https://json-schema.org/draft/2020-12/schema`
- `$id`: `https://kfm.dev/schemas/<name>.v1.json` **(domain placeholder; not confirmed in repo)**

If the repo already has a canonical domain, align to that.

</details>

---

## ✅ CI expectations (minimum)

At minimum, CI should:

- validate every schema file is itself valid JSON Schema
- validate fixtures (valid MUST pass, invalid MUST fail)
- validate catalogs and provenance outputs where relevant (STAC/DCAT/PROV)
- run deny-by-default policy checks as part of promotion gating

> [!IMPORTANT]
> A schema without fixtures is effectively “documentation only.” Fixtures make it enforceable.

### Suggested fixture conventions

```text
fixtures/
  valid/
    minimal.json
    typical.json
  invalid/
    missing_required_field.json
    wrong_type.json
    extra_field.json
```

---

## ➕ Adding a new dataset schema

### Step 1 — Create the contract file

- pick a stable `dataset_id` (canonical registry id)
- add `schemas/<dataset_id>.processed.v1.schema.json`
- define required fields, types, and (if spatial) CRS/geometry expectations

### Step 2 — Add fixtures

- at least:
  - `valid/minimal.json`
  - `valid/typical.json`
  - 3 invalid fixtures (missing required field, wrong type, unexpected extra field)

### Step 3 — Wire it to the dataset registry

Update the dataset registry entry to reference:

- schema file path + major version
- expected cadence/freshness SLO (if applicable)
- policy label (see next section)

### Step 4 — Prove it in CI

Schemas must be part of the “schema registry and validation tests” that run before additional datasets are integrated.

#### Definition of Done ✅

- [ ] Schema file exists + validates
- [ ] Fixtures exist (valid + invalid)
- [ ] Dataset registry references schema + version
- [ ] CI fails on invalid fixtures and passes on valid fixtures
- [ ] Policy label + sensitivity expectations are documented

---

## 🔐 Sensitive data & policy labels

Every dataset must carry a **policy label** and schemas should support enforcement by preventing “public” outputs from structurally containing prohibited fields.

Recommended policy labels (align to governance docs):

- `public`
- `restricted`
- `sensitive-location`
- `aggregate-only`

> [!CAUTION]
> **Redaction is a first-class transformation.** Raw datasets remain immutable; redacted derivatives are separate governed versions (often a separate dataset_id) with explicit policy labels and provenance.

---

## 🔗 Related (repo paths)

- `../../../../schemas/` — cross-cutting system contracts (STAC/DCAT/PROV, receipts/manifests, story node schemas, UI/telemetry) *(if present)*
- `../README.md` — dataset registry overview *(if present)*
- `../../../../docs/` — governance + architecture + onboarding runbooks *(if present)*

---

## 🧠 Why this folder exists (context)

KFM’s roadmap explicitly calls for a **dataset onboarding kit** (templates + scripts + validators + examples) whose dependencies include the **registry + schemas**. This directory is one of those kit components.

---