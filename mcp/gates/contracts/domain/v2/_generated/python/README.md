<!-- @generated: This README lives in a generated folder. Manual edits may be overwritten. -->

# KFM Domain Contracts v2 (Generated Python) 🐍🧾

![Generated](https://img.shields.io/badge/generated-do%20not%20edit-blue)
![Contracts](https://img.shields.io/badge/contracts-domain%20v2-informational)
![Python](https://img.shields.io/badge/python-typed%20models-success)
![Governance](https://img.shields.io/badge/governance-policy%20gates%20enabled-important)
![Evidence](https://img.shields.io/badge/evidence-STAC%20%2B%20DCAT%20%2B%20PROV-purple)

> **What is this?**  
> This directory contains the **auto-generated Python bindings** for **Kansas Frontier Matrix (KFM)** **Domain Contracts v2** — the shared “language” used across ingestion pipelines, the knowledge graph, the governed API, the web UI, and Focus Mode (AI) to keep everything **typed, validated, traceable, and policy-compliant**.

---

## 🔎 Table of Contents

- [Why these contracts exist](#-why-these-contracts-exist)
- [What’s inside this folder](#-whats-inside-this-folder)
- [How it fits into KFM](#-how-it-fits-into-kfm)
- [Install & import](#-install--import)
- [Quickstart examples](#-quickstart-examples)
- [Governance & policy gates](#-governance--policy-gates)
- [Versioning & compatibility](#-versioning--compatibility)
- [Regenerating this package](#-regenerating-this-package)
- [Security & reproducibility notes](#-security--reproducibility-notes)
- [Related project docs](#-related-project-docs)

---

## 🧠 Why these contracts exist

KFM is explicitly designed around **contract-first + provenance-first + evidence-first** principles:

- **Contract-first**: data structures (and cross-service interfaces) are defined as contracts and validated continuously.
- **Provenance-first**: nothing enters “official” runtime use without lineage metadata.
- **Evidence-first**: published data is supported by the “evidence triplet” (**STAC + DCAT + PROV**) and enforced via validation gates.

These Python bindings exist so every KFM component can:
- validate inputs/outputs consistently ✅
- share stable types across services ✅
- enforce governance rules at CI + runtime ✅
- keep the “no mystery nodes / no black-box data” promise ✅

---

## 📦 What’s inside this folder

This folder is generated from **Domain Contracts v2** and typically includes:

- **Typed models** for core domain entities (examples):
  - 🗺️ `Place`
  - 🧭 `Event`
  - 📦 `Dataset`
  - 🔬 `Observation` / assets
  - 📖 `StoryNode` (narrative + map state)
  - 🧬 PROV-style lineage objects (`Entity`, `Activity`, `Agent`) and link structures
  - 🏷️ governance metadata (classification/sensitivity, licensing, review flags)
- **Serialization helpers** (JSON in/out)
- **Validation behavior** aligned with KFM gates (fail closed, strictness, required fields, etc.)

> ⚠️ **Do not edit generated code.**  
> If you need changes, update the contract sources and regenerate (see [Regenerating this package](#-regenerating-this-package)).

---

## 🧩 How it fits into KFM

KFM’s pipeline is intentionally linear and auditable:

```
📥 Raw → 🧪 ETL/Work → 📦 Processed → 🛰 Catalogs (STAC/DCAT/PROV) → 🕸 Graph → 🔌 API → 🗺 UI → 🤖 Focus Mode
```

Where these models are used:

- **Pipelines**: validate outputs + metadata artifacts before they’re promotable.
- **Graph ingestion**: ensures nodes/edges match governed ontology + required provenance.
- **API (FastAPI + GraphQL)**: request/response schemas, validation, and policy checks.
- **UI (React + MapLibre + Cesium)**: consumes only governed API outputs; provenance is surfaced to users.
- **Focus Mode (AI)**: answers must be grounded in data and include citations; non-grounded responses are rejected.

---

## 🧰 Install & import

### Option A — editable install from this directory (common in monorepos)
From **this** folder:

```bash
python -m pip install -e .
```

### Option B — install via repo-relative path (if supported by your repo tooling)
From repo root:

```bash
python -m pip install -e mcp/gates/contracts/domain/v2/_generated/python
```

> If you hit import issues, check how your repo defines Python package roots (e.g., `pyproject.toml` / workspace tooling).

---

## 🚀 Quickstart examples

> **Note:** the exact package/module names depend on generation settings.  
> Search within this folder for the top-level import (often `*_domain_v2`, `contracts_domain_v2`, or similar).

### 1) Validate a payload (Pydantic-style)

```python
import json

from YOUR_PACKAGE.models import Dataset  # 👈 replace with actual import

payload = json.loads(open("dataset.json", "r", encoding="utf-8").read())

# Pydantic v2-style
dataset = Dataset.model_validate(payload)

# (If generated for Pydantic v1, it may look like:)
# dataset = Dataset.parse_obj(payload)

print(dataset)
```

### 2) Serialize back to JSON

```python
# Pydantic v2-style
as_dict = dataset.model_dump(mode="json", exclude_none=True)

# (If v1:)
# as_dict = dataset.dict(exclude_none=True)

print(as_dict)
```

### 3) FastAPI boundary (request/response validation)

```python
from fastapi import FastAPI
from YOUR_PACKAGE.models import Dataset  # 👈 replace with actual import

app = FastAPI()

@app.post("/datasets", response_model=Dataset)
def create_dataset(ds: Dataset) -> Dataset:
    # ✅ ds is validated at the boundary
    return ds
```

### 4) Deterministic IDs / hashing (for run manifests, evidence manifests, etc.)

KFM emphasizes reproducibility and auditability. If your workflow needs stable digests:

```python
import hashlib, json

def stable_sha256(obj) -> str:
    # For strict canonicalization, prefer RFC 8785 tooling.
    canonical = json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()
```

---

## 🛡️ Governance & policy gates

KFM treats governance as **code**, enforced by **policy gates** at multiple checkpoints (CI and runtime). Common enforced rules include:

- ✅ schema validation (contracts must match)
- ✅ metadata completeness (STAC/DCAT/PROV expectations)
- ✅ license presence (no “unknown license” data)
- ✅ sensitivity/classification labeling and handling
- ✅ provenance completeness (inputs + processing declared)
- ✅ pipeline ordering (no skipping required stages)
- ✅ API boundary (UI must not talk directly to databases/graph)
- ✅ AI output rules (citations required; refusal if none)

If a rule is violated, changes should **fail closed** (CI blocks, runtime refuses, or promotion is denied).

---

## 🧬 Versioning & compatibility

KFM versioning is multi-layered:

- **Dataset versioning** (content changes over time)
- **System/API versioning** (interface evolution)
- **Contract versioning** (schema + model evolution)

Guidelines you should follow when changing **Domain Contracts v2**:

- 🟢 **Backward-compatible**: adding optional fields; adding new entity types without breaking existing ones.
- 🟡 **Potentially breaking**: adding required fields; narrowing allowed values; changing meaning/units.
- 🔴 **Breaking**: removing/renaming fields; changing field types; removing enum values relied on by clients.

> Breaking changes should typically result in a new **major contract version** (e.g., `v3/`), not silent mutations of `v2/`.

---

## ♻️ Regenerating this package

Because this folder is generated:

1. **Edit the contract sources** (the JSON Schema / contract definitions for `domain/v2`)
2. Run the repo’s **contract generation** workflow (Makefile/task runner/script)
3. Run validation gates (schema checks, policy checks, tests)
4. Commit the regenerated Python output

> Tip: search the repo for “codegen”, “generate contracts”, or “_generated/” to find the exact command for this project.

---

## 🔐 Security & reproducibility notes

A few project-wide practices that matter when working with contracts & generated code:

- 🧪 Prefer deterministic ETL and avoid ad-hoc manual edits to processed outputs.
- 🧾 Treat metadata as code (validate it in CI).
- 🔏 Favor signed artifacts + provenance attestations where applicable (SBOM/provenance concepts show up across the project).
- 🧨 Avoid dangerous subprocess patterns (`shell=True`) in automation scripts unless carefully controlled.

---

## 📚 Related project docs

These contracts are shaped by the KFM architecture + governance documentation and the project’s embedded reference libraries.

### Core KFM design docs
- 📘 **Comprehensive Technical Documentation** (system + repo structure, tooling, validation patterns)
- 🏗️ **Comprehensive Architecture, Features, and Design** (policy gates, API/UI split, security posture)
- 📥 **Data Intake – Technical & Design Guide** (evidence triplet, pipeline ordering, provenance requirements)
- 🧭 **AI System Overview** (Focus Mode governance, citation enforcement, provenance logging)
- 🗺️ **UI System Overview** (Story Nodes, provenance-first UX, API decoupling)
- 💡 **Latest Ideas & Future Proposals** (ops maturity: rollback, runbooks, policy packs, telemetry)
- 🧪 **Additional Project Ideas** (run manifests, evidence manifests, OCI artifacts & signing concepts)
- 🌱 **Innovative Concepts to Evolve KFM** (future-forward extensions)

### Embedded reference libraries (PDF Portfolios)
- 🤖 **AI Concepts & more** (portfolio)
- 🛰️ **Maps / WebGL / Virtual Worlds / Geospatial** (portfolio)
- 🗃️ **Data Management / Architectures / Data Science / Bayesian Methods** (portfolio)
- 🧰 **Various Programming Languages & Resources** (portfolio)

---

### ✅ Reminder

If you’re trying to change the contract:
- **Edit the source contracts**
- **Regenerate**
- **Let the gates do their job** 🛡️✨

