# Contract Test Fixtures 📦🧪

![Contracts](https://img.shields.io/badge/contracts-golden%20fixtures-brightgreen)
![Governance](https://img.shields.io/badge/governance-FAIR%20%2B%20CARE-7b2cbf)
![API](https://img.shields.io/badge/API-OpenAPI%20%2B%20GraphQL-2b9348)

> **Goal:** Keep KFM “contract-first” ✅ and “evidence-first” 🧾 — these fixtures are the canonical, versioned payloads used to prove our API + metadata contracts are stable, auditable, and policy-compliant.

---

## What this folder is (and why it exists) 🧭

This directory contains **test fixtures** (a.k.a. “golden files”) for **contract tests** in `api/contracts/tests/`.

In the Kansas Frontier Matrix (KFM) architecture, contracts aren’t a “nice to have” — they’re how we enforce:

- **Contract-first data & API design** (no “mystery layers” 🕵️‍♂️)  
- **Evidence triplet publishing**: **DCAT + STAC + PROV** required for anything that’s “official” ✅  
- **Provenance + policy enforcement** (OPA/Conftest expectations; AI outputs must be citable, etc.) 🛡️  
- **API boundary rule**: UI and other clients never bypass the API layer 🔒  
- **Interoperability**: stable schemas for cross-region federation + standard IDs (e.g., FIPS for counties) 🌎

Fixtures are the smallest possible **representative payloads** that prove these rules.

---

## Quick navigation 🔎

- [Fixture types](#fixture-types-)
- [Recommended layout](#recommended-layout-)
- [Naming conventions](#naming-conventions-)
- [Quality checklist](#quality-checklist-)
- [How to add / update fixtures](#how-to-add--update-fixtures-)
- [Gotchas (common causes of flaky contracts)](#gotchas-common-causes-of-flaky-contracts-)
- [Related docs](#related-docs-)

---

## Fixture types 🧩

### 1) API Interface Contracts 🌐
Used to ensure **clients won’t break** when we refactor internals.

- **OpenAPI** 📜  
  Snapshots of `/openapi.json` (FastAPI-generated) and/or hand-curated overlays.
- **GraphQL** 🧬  
  Exported schema snapshots and selected query/response examples.

✅ These fixtures should cover **core public surfaces** and stable internal contracts between services.

---

### 2) Evidence Triplet Payloads 🧾🗺️🧬
KFM requires the “evidence triplet” for published data:

- **DCAT** (catalog/discovery metadata) 🧾  
- **STAC** (spatiotemporal asset metadata) 🗺️  
- **PROV** (lineage, processing steps, agents) 🧬  

Fixtures here should also reflect KFM’s profile constraints (examples):
- STAC profile fields like `kfm:dataset_id` and `kfm:classification`
- DCAT profile fields for licensing, sovereignty/sensitivity flags
- PROV profile fields that preserve derivation links and agent identities (including software/automation agents)

---

### 3) Policy / Governance Scenarios 🛡️
Fixtures that intentionally test **fail-closed** behavior:

- Missing or invalid provenance
- Missing required license/attribution fields
- Classification/sovereignty mismatches (e.g., confidential input → public output ❌)
- AI output without citations ❌
- Orphan graph entities / missing links between DCAT ↔ STAC ↔ PROV

These are typically stored as:
- `*.invalid.<reason>.json`
- `*.redacted.json`
- `*.policy_deny.json`

---

### 4) “Golden” Endpoint Responses 🧪✨
Small, stable example responses for high-value endpoints (e.g., dataset lookup, search results, map-layer metadata, knowledge-graph entity retrieval, Focus Mode answers).

> ⚠️ Avoid binary fixtures here unless we have deterministic encodings and stable hash checks.
> Prefer JSON for most contract tests.

---

## Recommended layout 🌳

This folder can evolve, but we try to keep fixtures grouped by *contract domain*:

```text
api/contracts/tests/fixtures/
├── README.md                           # 📘 you are here
├── openapi/                            # 📜 OpenAPI snapshots
│   ├── openapi.snapshot.json
│   └── openapi.snapshot.min.json
├── graphql/                            # 🧬 GraphQL contracts
│   ├── schema.graphql
│   ├── queries/
│   │   └── dataset_by_id.graphql
│   └── responses/
│       └── dataset_by_id.200.json
├── evidence/                           # 🧾🗺️🧬 Evidence triplet
│   ├── dcat/
│   │   └── dataset.valid.jsonld
│   ├── stac/
│   │   ├── collection.valid.json
│   │   └── item.valid.json
│   └── prov/
│       ├── run.valid.json
│       └── run.invalid.missing_used.json
├── api/                                # 📦 Golden request/response pairs
│   ├── requests/
│   │   └── search_datasets.json
│   ├── responses/
│   │   └── search_datasets.200.json
│   └── errors/
│       └── forbidden.403.json
└── policy/                             # 🛡️ Explicit governance tests
    ├── ai_answer.invalid.no_citations.json
    └── classification.invalid.downgrade.json
```

> ✅ If your real folder structure differs, keep this README updated (fixtures are only valuable if discoverable).

---

## Naming conventions 🏷️

### File names
Use a consistent pattern that makes fixtures self-explanatory:

- `*.valid.json` — minimal valid example  
- `*.invalid.<reason>.json` — invalid example, reason included  
- `*.redacted.json` — expected redaction behavior  
- `*.snapshot.*` — generated “contract snapshots” (OpenAPI / GraphQL schema)

Examples:
- `item.valid.json`
- `item.invalid.missing_dataset_id.json`
- `dataset.valid.jsonld`
- `answer.invalid.no_citations.json`
- `openapi.snapshot.json`

### IDs & determinism
Fixtures must be stable and reusable:

- Prefer **deterministic IDs** and timestamps  
  - ✅ `kfm:dataset_id: "kfm.ks.example.dataset.v1"` (example pattern)  
  - ✅ `prov:startedAtTime: "2025-01-01T00:00:00Z"`  
  - ❌ “today”, random UUIDs, ephemeral hashes
- Prefer **globally meaningful identifiers** when available (e.g., FIPS for counties, URNs for doc UUIDs) 🌎

---

## Quality checklist ✅

Before adding/modifying a fixture, verify:

- [ ] **Minimal**: contains only what the contract needs (no noise)
- [ ] **Deterministic**: stable ordering, stable timestamps, stable IDs
- [ ] **Sanitized**: no secrets, tokens, internal URLs, private coordinates, PII
- [ ] **Evidence-aligned**: DCAT ↔ STAC ↔ PROV link cleanly (no orphan records)
- [ ] **Policy-aware**: classification + licensing behave as expected
- [ ] **AI-safe** (when applicable): AI outputs include **at least one citation** and can be mapped back to cataloged sources 🧾
- [ ] **Pretty**: formatted JSON (2 spaces) unless a minified snapshot is intentional

---

## How to add / update fixtures 🛠️

### Add a new fixture (recommended flow)
1. **Pick the contract surface** you’re testing 🎯  
   Example: `GET /datasets/{id}`, GraphQL `dataset(id: ...)`, STAC item requirements, etc.
2. **Start from a real payload** (local API run or pipeline output), then minimize ✂️  
3. Ensure **cross-links** are consistent:
   - DCAT dataset references distribution links (STAC/PROV)
   - STAC items reference `kfm:dataset_id`
   - PROV references input/output entities + activity + agent
4. Add the fixture file under the right folder 📁
5. Add/extend the contract test to load the fixture and assert:
   - schema validity ✅
   - stable fields ✅
   - policy behavior ✅
6. Run the contract tests locally (example):
   ```bash
   pytest -q api/contracts/tests
   ```

### Update fixtures when…
- OpenAPI/GraphQL contract changes (new field, renamed field, response shape change)
- Evidence schema profile changes (e.g., new required STAC/PROV/DCAT fields)
- Governance rules change (OPA policy pack updates affecting validation/redaction/citations)

> 🧠 Rule of thumb: if a change breaks a client or breaks provenance, it **must** be represented in fixtures and tested.

---

## Gotchas (common causes of flaky contracts) 🧨

- **Timestamps and “now”**: never use dynamic times in fixtures
- **Order-dependent JSON**: tests should avoid relying on object key order; arrays should be sorted where stability matters
- **Floating precision**: coordinates and computed metrics should be rounded consistently
- **Environment-specific URLs**: don’t bake in local hostnames, ports, or dev-only paths
- **Leaking restricted data**: fixtures must represent **redaction rules**, not bypass them 🔒
- **Orphan metadata**: a STAC item without matching DCAT/PROV expectations is a contract smell (“no mystery nodes/layers”)

---

## Related docs 📚

These fixtures are tightly coupled to our broader KFM “contracts + governance” system:

- 🧾 Data contracts & examples: `/docs/data/contracts/examples/README.md`
- 🛡️ Policy pack & rules: `/api/scripts/policy/README.md`
- 🧠 Master guide / architecture rules: `/docs/MASTER_GUIDE_v13.md`
- 🧱 API contract extensions template: `/docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`

> If you add a new fixture category, also add a short blurb here so future contributors don’t hunt for it. 🔍
