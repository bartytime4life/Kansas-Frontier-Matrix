# KFM Policy Input Schemas (OPA/Rego)

> [!IMPORTANT]
> This directory is part of KFM’s **trust membrane**: the governed API validates/normalizes inputs and then evaluates **OPA/Rego policy**.  
> **Policy must fail closed** (default deny) and Focus Mode must **cite or abstain**.

This folder contains **JSON Schema contracts** for documents used as **OPA `input`** (and closely-related validator inputs) so policy decisions remain:
- **Contract-first** (schema drift is caught early)
- **Evidence-first** (citations required for factual outputs)
- **Sensitivity-aware** (public vs restricted vs sensitive-location vs aggregate-only)
- **CI-ready** (policy regression suite can treat test fixtures as governed artifacts)

---

## What belongs here

### ✅ In scope
- JSON Schemas for **OPA input shapes** (e.g., `input.actor`, `input.request`, `input.resource`, `input.answer`, derived flags used by policy)
- JSON Schemas for **validator input shapes** that must align with the policy layer (e.g., FocusAnswer-like payloads that policy validates)

### ❌ Out of scope
- Rego policy modules (`*.rego`) — those belong in `policy/policies/` (or the repo’s chosen policy module directory)
- CI test fixtures — those belong in `policy/tests/` (or the repo’s chosen test directory)
- Runtime code — lives in the governed API service (and must not bypass repository interfaces)

---

## Directory responsibilities (recommended layout)

```text
policy/
  policies/                 # Rego packages (default deny; explicit allow)
  schemas/
    inputs/                 # ✅ this directory (OPA + validator input schemas)
      README.md             # ✅ this file
      (recommended) *.schema.json
    outputs/                # Policy decision outputs / normalized responses (recommended)
  tests/                    # Policy regression fixtures (redacted/synthetic)
```

> [!NOTE]
> The exact folder names (`policies/`, `tests/`, `outputs/`) can vary by repo, but the contract boundary remains:
> **schemas define what policy expects; policy denies when input is missing/invalid.**

---

## KFM policy input envelope

KFM’s blueprint shows an illustrative OPA input shape with:
- `actor` (role + attributes)
- `request` (endpoint + context)
- `answer` (fields used by cite-or-abstain policy)
- optional `resource` (for data access policy)

**Recommended approach:** treat this as a single *envelope* schema, with smaller `$ref`-able sub-schemas.

### Canonical top-level keys (recommended)

| Key | Required? | Used for | Notes |
|---|---:|---|---|
| `actor` | ✅ | who is asking / acting | includes `role` and optional attributes/claims |
| `request` | ✅ | what is being requested | often includes endpoint + context |
| `resource` | ↔ | data access / redaction / aggregation decisions | required for dataset/version access policies |
| `answer` | ↔ | Focus Mode output validation | required for cite-or-abstain checks |
| `derived` | ↔ | convenience booleans used by policy | e.g., `has_citations`, `sensitivity_ok` |

> [!TIP]
> Keep `derived` deterministic and computed by the API validator layer, not by the model. Policies may depend on it, but it should be reproducible.

---

## Controlled vocabularies (governed)

### `actor.role` (baseline)
Recommended enum aligned to the blueprint’s illustrative roles:
- `public`
- `reviewer`
- `admin`

### `resource.sensitivity` (baseline)
Sensitivity labels aligned to the integration blueprint:
- `public`
- `restricted`
- `sensitive-location`
- `aggregate-only`

> [!WARNING]
> Do **not** invent new sensitivity labels ad hoc. Add new values only via governance review and update:
> schema → policy → tests → documentation together.

---

## Focus Mode: cite-or-abstain expectations (schema alignment)

Focus Mode output validation is defined as **schema + policy**:
- Schema expects a FocusAnswer-like shape (e.g., `answer_markdown`, `citations[]`, `audit_ref`)
- Policy requires citations and sensitivity_ok; abstain if evidence is insufficient

**Implementation note:** OPA input can embed the raw response object under `answer`, and/or include derived booleans used by policy (e.g., `answer.has_citations`, `answer.sensitivity_ok`).

### Citation object minimum
When your OPA input includes `citations[]`, the Citation objects should minimally support:
- `id` (string)
- `kind` (enum like `dcat`, `stac`, `prov`, `doc`, `graph`)
- `ref` (string resolver reference)

(If additional fields exist in your API contract such as `locator` / `note`, they should be modeled as optional in schema.)

---

## Sensitive data handling

> [!IMPORTANT]
> **Never** put restricted content, precise sensitive locations, personal identifying information, or culturally restricted details into:
> - JSON Schema examples
> - CI fixtures
> - README snippets
>
> Use **synthetic** or **redacted** examples only.

Recommended pattern for fixtures used with these schemas:
- Replace coordinates with coarse bounding boxes
- Replace IDs with placeholders (e.g., `dataset_example`)
- Omit or hash sensitive fields

---

## Versioning rules (schema governance)

1. Every schema file in this folder should include:
   - `$schema` (JSON Schema draft)
   - `$id` (stable identifier)
   - `title` + `description`
2. Breaking changes require:
   - bumping the schema version (file name + `$id`)
   - updating the policy modules that depend on those fields
   - adding/adjusting regression fixtures and tests

> [!NOTE]
> The blueprint shows Draft 2020‑12 usage for at least one schema example; prefer a single draft across this folder for consistency.

---

## CI expectations (policy regression readiness)

This folder exists to make the following checks deterministic and automatable:

- **Schema validation** of policy inputs (fixtures and/or runtime validator contracts)
- **OPA unit tests** for default-deny and cite-or-abstain behavior
- **Regression coverage** for:
  - sensitivity handling
  - field-level redaction (when applicable)
  - aggregation thresholds (when applicable)
  - audit requirements (e.g., audit references / evidence bundle identifiers when required)

> [!CHECKLIST]
> Minimum “done” for any new schema added here:
> - [ ] JSON Schema validates (`$schema`, `$id`, required keys correct)
> - [ ] At least one **positive** fixture (allowed) and one **negative** fixture (denied/abstain) exists in `policy/tests/`
> - [ ] Rego tests cover the new/changed keys (deny on missing/invalid)
> - [ ] No fixture contains sensitive or private raw values
> - [ ] Any new controlled vocabulary value is documented + enforced (schema + policy)

---

## How to add a new input schema

1. **Identify the policy decision** the schema supports (data access, redaction, Focus Mode validation, promotion gating, etc.).
2. **Define the minimal contract**:
   - required fields (what policy must see)
   - optional fields (nice-to-have metadata)
   - controlled vocabularies (enums)
3. Create schema file:
   - `snake_or_kebab_case_name_vX.schema.json` (team preference)
4. Add/extend policy tests:
   - deny when required fields missing
   - allow only when invariants are satisfied
5. Update documentation:
   - add the schema to the “Schema inventory” table below

---

## Schema inventory (fill as implemented)

> Add rows as schema files are created. Keep descriptions terse and test-oriented.

| Schema file | Primary purpose | Key required fields |
|---|---|---|
| *(recommended)* `opa_input_envelope_v1.schema.json` | Common OPA input envelope shared across policies | `actor`, `request`; plus `resource` or `answer` depending on use |
| *(recommended)* `focus_mode_policy_input_v1.schema.json` | Input shape for cite‑or‑abstain evaluation | `actor.role`, `answer.citations`, `answer.audit_ref` (or derived booleans used by policy) |
| *(recommended)* `data_access_policy_input_v1.schema.json` | Input shape for dataset/version access decisions | `actor.role`, `resource.kind`, `resource.sensitivity` |

---

## Verification step (repo alignment)

If the repo already contains canonical schema names/paths or existing API contracts, **treat those as source of truth** and align this folder accordingly:
- reconcile field names (`answer_markdown` vs `text`, etc.)
- reconcile required keys for FocusAnswer and Citation objects
- ensure policy modules and validators agree on the final contract

