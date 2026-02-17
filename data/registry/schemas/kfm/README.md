# KFM Schema Registry (`data/registry/schemas/kfm/`)

**Status:** ✅ Governed • ✅ Contract-first • ✅ Evidence-first • ✅ Fail-closed • ✅ FAIR+CARE aware

> [!IMPORTANT]
> Schemas in this folder are **normative contracts** for KFM.  
> If an artifact does **not** validate, it must **not** be promoted, served, or rendered as “trusted” in any UI.

---

## What this folder is

This directory is the **schema registry** for Kansas Frontier Matrix (KFM). It contains the **versioned** schemas/shapes that define what “valid” means for KFM’s governed artifacts, including (but not limited to):

- **Pipeline receipts** (per-run provenance + checks)
- **Signed registries / allow-lists** used by automation and promotion logic
- **Catalog boundary artifacts** (STAC/DCAT/PROV and KFM profiles for those artifacts)
- **Narrative + UI configuration artifacts** that must remain machine-ingestible (e.g., Story/Focus-mode metadata)

> [!NOTE]
> This folder is intentionally “boring”: stable names, explicit versioning, strict validation.  
> Its value is preventing silent drift in governance.

---

## Architecture boundary

Schemas sit on KFM’s **trust membrane** — the boundary where artifacts move between layers:

- **Pipelines → catalogs/provenance → APIs → UI / Focus Mode**
- **External inputs → governed ingestion → internal storage/graph/search**
- **Runtime requests → governed API responses → front-end renderers**

**Rule of thumb:**  
Domain models stay pure. Validation happens at ports/adapters and at promotion gates.

---

## Directory layout

Below is the *recommended* layout. Keep this README updated if you add new schema families.

```text
data/registry/schemas/kfm/
├─ README.md
├─ common/                 # shared $defs / reusable shapes
├─ receipts/               # run receipts, manifests, validation reports
├─ registries/             # signed allow-lists (watchers, providers, jobs)
├─ catalogs/               # KFM STAC/DCAT/PROV profiles & constraints
├─ story/                  # Story Node / Focus Mode machine-ingestible contracts
├─ ui/                     # legends, symbols, layer-style registries (if governed here)
└─ examples/
   ├─ valid/               # fixtures that MUST validate
   └─ invalid/             # fixtures that MUST fail (regression harness)
```

---

## How schemas are used in the KFM “truth path”

```mermaid
flowchart LR
  A[Raw Sources] --> B[ETL / Watchers]
  B --> C[Artifacts produced<br/>data + catalogs + receipts]
  C --> D[Schema validation<br/>(JSON Schema / shapes)]
  D --> E[Signature / attestation checks<br/>(where required)]
  E --> F[Policy gate<br/>(OPA/Conftest)]
  F --> G[Promotion / publish]
  G --> H[Governed APIs]
  H --> I[UI / Focus Mode]
```

> [!IMPORTANT]
> **Schema validation is a gate, not a hint.**  
> If the artifact fails validation, downstream steps must treat it as untrusted.

---

## Common KFM contract types

The exact inventory of schemas evolves; the table below describes *common* contract families and typical naming.

| Contract family | Intent | Typical filename pattern | Typical gate(s) |
|---|---|---|---|
| Run receipt | Provenance for a single pipeline run (inputs, outputs, checks, timestamps, spec hash) | `receipts/<name>.v1.schema.json` | Schema validation + policy |
| Run manifest | Promotion-oriented rollup (digests, rights, attestations, pointers to catalogs) | `receipts/<name>.v1.schema.json` | Schema validation + policy |
| Registry entry (signed) | “Allow-list” inputs for automation (what may run, where, under what constraints) | `registries/<name>.v1.schema.json` | Schema validation + signature verify + policy |
| Catalog profile | Enforce KFM minimum metadata + governance fields on STAC/DCAT/PROV boundary artifacts | `catalogs/<profile>.vN.schema.json` (and/or shapes) | Schema validation + link checks + policy |
| Story / narrative contract | Make narrative artifacts machine-ingestible and provenance-linked | `story/<name>.vN.schema.json` | Schema validation + governed-doc checks |

---

## Versioning policy

### File naming

- Schemas MUST carry **major version** in the filename:  
  `something.v1.schema.json`, `something.v2.schema.json`, …

### When to bump major

Bump the major version if you:

- remove or rename a field
- change the meaning/semantics of a field
- tighten validation such that previously valid artifacts now fail
- change defaults in a way that affects interpretation downstream

> [!WARNING]
> Treat schema changes as **production changes**. A schema diff can block ingestion, promotion, and rendering.

### Old majors are immutable

- Do **not** “silently fix” old major schemas to change behavior.
- If you must correct a validation bug that changes acceptance semantics, publish a new major.

### Migrations

For each major bump, provide:

- a deterministic transformer/migration path (script or documented procedure)
- dual-read support in consumers for at least one release cycle *when feasible*
- CI coverage proving the migration preserves meaning

---

## Authoring rules (KFM conventions)

### JSON Schema baseline

Unless a shape language is more appropriate (e.g., RDF-heavy constraints), schemas SHOULD:

- declare `$schema` (dialect)
- declare `$id` (stable identifier)
- use `additionalProperties: false` for objects **by default**
- specify `required` explicitly
- centralize shared structures under `$defs` (or `common/` via `$ref`)
- document intended usage in `description` and (optionally) `$comment`

### Governance-aware fields

Any contract that can influence publication, access, or narrative MUST make governance machine-checkable. At minimum, consider fields for:

| Field concept | Examples | Why it matters |
|---|---|---|
| Rights & licensing | `license`, `rights`, `attribution` | prevents improper distribution/use |
| Sensitivity | `sensitivity`, `redaction`, `access_tier` | enables safe defaults + CARE |
| Provenance pointers | `prov_ref`, `stac_ref`, `dcat_ref`, `source_ids` | enables cite-or-abstain behavior |
| Determinism | `spec_hash`, `inputs_digest`, `outputs_digest` | reproducible builds + audit |

> [!CAUTION]
> If a schema permits precise locations for culturally restricted or sensitive resources, it MUST trigger governance review before promotion.

---

## Validation harness

Minimum expectation for this registry:

1) `examples/valid/**` fixtures **must** validate.  
2) `examples/invalid/**` fixtures **must** fail.  
3) Any policy gate that relies on schema-required fields must be covered by tests.

<details>
<summary>Example validation commands (adapt to repo tooling)</summary>

```bash
# Option A: AJV (Node)
ajv validate \
  -s data/registry/schemas/kfm/receipts/run_receipt.v1.schema.json \
  -d data/registry/schemas/kfm/examples/valid/run_receipt.json

# Option B: python-jsonschema
python -m jsonschema \
  -i data/registry/schemas/kfm/examples/valid/run_receipt.json \
  data/registry/schemas/kfm/receipts/run_receipt.v1.schema.json
```

</details>

---

## CI expectations

Schema changes SHOULD cause CI to:

- validate impacted fixtures
- run policy tests (OPA/Conftest or equivalent)
- block merge on validation failures (fail-closed)

<details>
<summary>Recommended CI “definition of done” for schema changes</summary>

- [ ] Schema passes validation/lint checks
- [ ] Fixtures updated (valid + invalid)
- [ ] Consumer impact assessed (API/pipeline/UI)
- [ ] Version bumped if breaking
- [ ] Migration path documented if breaking
- [ ] Governance review requested if sensitivity/rights fields changed
- [ ] README updated (this file)

</details>

---

## Governance rules for contributions

- **Do not** embed secrets, API keys, or private identifiers in schemas or examples.
- Treat any schema affecting **publication, access, sensitivity, or narrative rendering** as requiring governance review.
- Prefer **explicitness over convenience** (strict `required`, strict object shapes, explicit enums).

---

## Glossary

- **Contract artifact:** A machine-validated schema/spec that defines an interface contract (schemas, OpenAPI, GraphQL SDL, UI registries).
- **Evidence artifact:** A derived dataset/output registered in catalogs with provenance before being used in narratives or UI.
- **Fail-closed:** Missing required governance requirements results in denial/blocking by default.
- **Boundary artifact:** The catalog/provenance objects (e.g., STAC/DCAT/PROV) that form the interface between pipeline outputs and runtime services.