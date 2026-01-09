<div align="center">

# 🧩 **API Contracts**
### Kansas Frontier Matrix (KFM) — Contract-first interfaces for catalogs, graphs, analysis & Focus Mode

![Contract-first](https://img.shields.io/badge/Contract--first-Required-2ea44f)
![OpenAPI](https://img.shields.io/badge/OpenAPI-3.1-blue)
![GraphQL](https://img.shields.io/badge/GraphQL-SDL-purple)
![JSON%20Schema](https://img.shields.io/badge/JSON%20Schema-Validated-0aa)
![STAC/DCAT/PROV](https://img.shields.io/badge/STAC%20%2F%20DCAT%20%2F%20PROV-Aligned-orange)
![FAIR%2BCARE](https://img.shields.io/badge/FAIR%2BCARE-Governed-ff8c00)

</div>

> ✅ **Rule (KFM v13):** If it’s used across a boundary (UI ↔ API, API ↔ ETL, workers ↔ catalogs, partners ↔ KFM), it must have a **versioned, machine-validated contract** — and implementations must honor it.

---

## 🧭 What this folder is for

This directory is the **single source of truth** for KFM interface contracts *served by the API boundary*:

- 🌐 **REST contracts** (OpenAPI) for public and internal endpoints  
- 🧠 **Graph contracts** (GraphQL SDL + query limits) for graph-shaped reads  
- 🧾 **Schema contracts** (JSON Schema) for:
  - 🗂️ **Catalogs & discovery** (STAC / DCAT)
  - 🧬 **Lineage** (PROV-style bundles, run records, activity/entity links)
  - 🧪 **Analytics outputs** (stats/regression/Bayes; diagnostics + uncertainty)
  - 📖 **Story Nodes / Focus Mode bundles** (citations, evidence pointers, redaction)
  - 📈 **Telemetry & audit payloads** (request, job, provenance, UI events)
- 🧰 **Examples + golden fixtures** to support contract tests & CI

> [!IMPORTANT]
> **Catalog gate is non-negotiable:** outputs become “real” only after they are registered as **STAC/DCAT** and lineage-linked via **PROV**, then consumed downstream (graph → API → UI → Story Nodes → Focus Mode).  
> The API must not serve “mystery data” that isn’t cataloged + provenance-linked + policy-checked.

---

## 🧱 What counts as a “contract” in KFM

A **contract artifact** is a machine-validated schema/spec that defines an interface:

- OpenAPI bundle(s) ✅  
- GraphQL SDL ✅  
- JSON Schemas ✅  
- Evidence bundle shapes (Story Node/Focus Mode payload contracts) ✅  
- Job lifecycle contracts ✅  
- UI config payload contracts (when they cross the API boundary) ✅  

**Breaking changes require explicit version bumps + migration notes.**

Also sacred “pipeline contracts” KFM treats as part of the same governance surface:
- 🧾 **Evidence artifacts must be catalog-registered** (STAC/DCAT) and lineage-linked (PROV) before UI / narratives consume them.
- 🧠 **Focus Mode must not display unsourced material**: it must bind claims to evidence pointers + citations.

---

## 🗂️ Canonical locations (v13 target)

KFM v13 separates **API surface contracts** from **cross-cutting payload schemas**:

- **API boundary home:** `src/server/`  
- **Contracts home (this folder):** inside the API boundary (recommended `src/server/contracts/`)  
- **Machine-validated payload schemas:** `schemas/` at repo root (STAC/DCAT/PROV/storynodes/ui/telemetry)

> [!NOTE]
> If your repo is service-split (e.g., `api/` as its own project), keep the **same internal shape** — but still maintain **one canonical home** for contracts inside that service.

### Suggested directory layout (v13)

```text
📁 src/
└─ 📁 server/                              # 🚪 API boundary (governed)
   ├─ 📁 contracts/                        # 🧩 API surface contracts (this README)
   │  ├─ 📄 README.md
   │  ├─ 📁 openapi/                       # 🌐 REST contracts
   │  │  ├─ 📄 public.v1.yaml
   │  │  ├─ 📄 internal.v1.yaml
   │  │  └─ 📁 components/
   │  ├─ 📁 graphql/                       # 🧠 Graph contracts
   │  │  ├─ 📄 schema.graphql
   │  │  └─ 📄 directives.graphql
   │  ├─ 📁 examples/                      # 🧰 fixtures (redaction-safe)
   │  │  ├─ 📁 requests/
   │  │  └─ 📁 responses/
   │  └─ 📁 changelog/
   │     └─ 📄 CONTRACTS_CHANGELOG.md
   └─ 📁 tests/                            # 🧪 API tests (incl. contract test harness)

📁 schemas/                                # 📦 Cross-boundary JSON Schemas (machine validated)
├─ 📁 stac/                                # 🗂️ STAC profiles + extensions
├─ 📁 dcat/                                # 🏷️ DCAT profiles
├─ 📁 prov/                                # 🧬 PROV bundles + run records
├─ 📁 storynodes/                          # 📖 Story Node + evidence bundle shapes
├─ 📁 ui/                                  # 🌐 UI config payloads that cross boundaries
└─ 📁 telemetry/                           # 📈 Audit & telemetry events