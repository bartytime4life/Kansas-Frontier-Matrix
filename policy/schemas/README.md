<!--
File: policy/schemas/README.md
KFM: Kansas Frontier Matrix — Governed Policy Schemas

This README is a *contract* for what belongs in policy/schemas/, how it is used, and how it is governed.
-->

# Policy Schemas (KFM)

✅ **Governed artifact** · 🔒 **Fail-closed** · 🧾 **Provenance-first** · 🧪 **CI enforced** · 🧩 **JSON Schema (Draft 2020-12)**

This directory contains **JSON Schemas that define the shapes used by KFM policy enforcement**, including:

- **OPA/Rego policy inputs** (request + actor + candidate answer) used for deny-by-default enforcement.
- **Policy-gated governed artifacts** (receipts/manifests, audit records, story claims/citations structures) that must validate **before** promotion/publish.
- **Policy-adjacent contracts** that are referenced by CI “acceptance harness” checks (schema validation, policy tests, signature verification, `spec_hash` reproducibility).

> [!IMPORTANT]
> **Validate first, then evaluate policy.**
> If an object does not validate against its schema, treat it as **invalid input** and **deny / block promotion** (“fail-closed” behavior).

---

## Related directories

- **`policy/`** — OPA/Rego policies + unit tests (deny-by-default)  
  ↳ see: `../README.md` (if present)
- **`schemas/` (repo root)** — Canonical platform schemas (STAC/DCAT/PROV/story nodes/UI/telemetry)  
  ↳ see: `../../schemas/` (repo standard)

> [!NOTE]
> **Canonical** schemas usually live under the repo-root `schemas/`.  
> `policy/schemas/` is for *policy-boundary schemas* (OPA inputs, promotion receipts/manifests, policy-gated “contract objects”), and for *vendored snapshots* when CI/policy tooling needs local references.

---

## Directory layout (expected)

```text
policy/
  schemas/
    README.md                      # you are here
    inputs/                        # OPA input contracts
      policy_input.v1.schema.json
      focus_answer.v1.schema.json  # optional: validate AI output contract pre-policy
    artifacts/                     # things policies/gates validate before publish
      dataset_manifest.v1.schema.json
      run_record.v1.schema.json
      audit_record.v1.schema.json
      story_front_matter.v3.schema.json
      run_manifest.v1.schema.json  # aka run_receipt
      watcher.v1.schema.json
    _vendored/                     # optional: pinned external schema snapshots
      README.md
```

---

## Schema inventory

Update this table **whenever** a schema is added/removed or a major version changes.

| Category | Schema ID (logical) | File (relative) | Validates | Primary consumer(s) | Status |
|---|---|---|---|---|---|
| OPA input | `kfm.schema.policy_input.v1` | `inputs/policy_input.v1.schema.json` | Actor/request/answer envelope to OPA | API gateway → PDP; Conftest fixtures | **Required** |
| Focus output | `kfm.schema.focus_answer.v1` | `inputs/focus_answer.v1.schema.json` | Focus Mode response shape (answer + citations + audit_ref) | Output validator; “cite-or-abstain” policy | **Required** |
| Dataset manifest | `kfm.schema.dataset_manifest.v1` | `artifacts/dataset_manifest.v1.schema.json` | Raw dataset manifest (license, sensitivity, etc.) | Ingest validators; promotion gates; policy checks | **Required** |
| Pipeline run record | `kfm.schema.run_record.v1` | `artifacts/run_record.v1.schema.json` | Run inputs/outputs + validation refs | Pipelines; provenance graph ingest; audit | **Required** |
| Story front matter | `kfm.schema.story_front_matter.v3` | `artifacts/story_front_matter.v3.schema.json` | Story metadata + evidence bundle refs + claims/citations | Story validator; publish gate | **Required** |
| Audit record | `kfm.schema.audit_record.v1` | `artifacts/audit_record.v1.schema.json` | Append-only audit events | Audit ledger writer; reviewers | **Required** |
| Run manifest / receipt | `kfm.schema.run_manifest.v1` | `artifacts/run_manifest.v1.schema.json` | Promotion/publish receipt (spec_hash, rights, digests, attestations) | “Promotion Contract”; provenance guard policy pack | **Required** |
| Watcher | `kfm.schema.watcher.v1` | `artifacts/watcher.v1.schema.json` | Watcher definitions (endpoint/poll/policy/outputs/spec_hash/signature_ref) | Watchers registry + CI gating | **Required** |
| (Optional) Materiality profile | `kfm.schema.materiality_profile.v1` | `inputs/materiality_profile.v1.schema.json` | Provider thresholds / materiality rules input | Materiality policy pack | Planned |
| (Optional) Sensitive record | `kfm.schema.sensitive_record.v1` | `artifacts/sensitive_record.v1.schema.json` | Rights + generalized geometry + grants model | Sensitive-access policies | Planned |

> [!TIP]
> If you’re unsure whether a schema belongs in `policy/schemas/` or `schemas/` (root):  
> - Put it in **`schemas/`** if it is a platform-wide data contract.  
> - Put it in **`policy/schemas/`** if it is a **policy boundary** contract (OPA input, receipt/manifest required for promotion, or a contract used *directly* by policy tests).

---

## Schema conventions (KFM)

### JSON Schema dialect
- Use **JSON Schema Draft 2020-12**.
- Every schema file MUST include:
  - `"$schema"` (draft URI)
  - `"$id"` (stable, absolute identifier)
  - `title`, `description`
  - `type`, and a strict `required[]` set for the gate-critical keys

### Strictness defaults
- Prefer **fail-closed** shapes:
  - `additionalProperties: false` for top-level objects unless there is a strong reason.
  - Use `unevaluatedProperties: false` where appropriate for composed schemas.
- Prefer explicit enums/controlled vocabularies for policy-critical fields (e.g., roles, classification levels).

### Stable identifiers
- Treat `"$id"` as **public API**.
- Prefer a stable base, e.g.:
  - `"$id": "https://<kfm-domain>/schema/<name>.v1.schema.json"`

> [!CAUTION]
> Do not rename keys casually. Changing key names breaks policy evaluation and provenance comparability.

---

## How schemas are used (runtime + CI)

### Fail-closed request path (conceptual)
```mermaid
flowchart LR
  UI[UI / client] --> API[API Gateway]
  API --> SV[Schema validate (request / artifacts)]
  SV -->|fail| DENY[Deny / Block promotion]
  SV -->|pass| PDP[OPA/Rego PDP]
  PDP -->|deny| DENY
  PDP -->|allow| APP[Application / pipeline]
  APP --> OUTSV[Schema validate (outputs / receipts)]
  OUTSV -->|fail| DENY
  OUTSV -->|pass| AUDIT[Append audit record]
  AUDIT --> RESP[Response / publish]
```

### CI acceptance harness (what MUST be checked)
A PR that adds or changes governed artifacts MUST pass:

1. **Schema validation**
   - Story nodes / manifests / receipts validate against the correct schema versions.
2. **Policy tests**
   - Conftest runs the deny-by-default policy packs against fixtures and changed files.
3. **Catalog and provenance validation**
   - STAC / DCAT / PROV artifacts validate (as applicable).
4. **Supply-chain verification (when publishing/promoting)**
   - Receipt/manifests include required digests.
   - Signatures / attestations are verified.
5. **`spec_hash` reproducibility**
   - `spec_hash` recomputation matches the committed value.

---

## OPA/Rego input contract (recommended)

Schemas in `inputs/` should model the envelope passed into OPA, typically:

- `actor` (role + attributes)
- `request` (endpoint + context)
- `answer` (content + citations + sensitivity flags)

Keep OPA inputs **stable** and **explicitly versioned**, because changes here can silently break deny-by-default policies.

---

## `spec_hash` (deterministic identity) rules

### Required fields
Any schema used for deterministic addressing MUST include:
- `spec_hash`
- `spec_schema_id`
- `spec_recipe_version`

### Canonicalization requirements
- Preferred: **RFC 8785 JSON Canonicalization Scheme** applied to the schema-defined object (“spec”)
- Fallback: YAML canonicalization must be deterministic and documented (do not invent ad-hoc sorting rules)

> [!IMPORTANT]
> `spec_hash` is only meaningful if it is computed over a **schema-defined object** with a **declared recipe version**.

---

## Adding or changing a schema (contribution workflow)

### Add a new schema
- [ ] Create `inputs/` or `artifacts/` file with semver suffix (e.g., `*.v1.schema.json`)
- [ ] Include `$schema`, `$id`, `title`, `description`
- [ ] Define required keys and enums for policy-critical fields
- [ ] Add/extend test fixtures under `policy/testdata/` (or equivalent)
- [ ] Update the **Schema inventory table** in this README
- [ ] Add/adjust Conftest rules to deny on missing required fields (fail-closed)
- [ ] Ensure CI acceptance harness validates the new schema + fixtures

### Changing an existing schema
- **Non-breaking** (add optional fields, widen enums safely):
  - [ ] Bump **minor** version (or keep v1 and document additive change—project standard)
- **Breaking** (remove/rename required fields, tighten constraints):
  - [ ] Create **new major** schema file (e.g., `v2`)
  - [ ] Provide migration notes + scripts (where practical)
  - [ ] Keep old major available for a deprecation window

---

## Security, CARE/FAIR, and sensitivity

Policy and schema design MUST reflect:
- **Classification & access controls** (deny-by-default)
- **Sensitive-location controls** (generalize/redact; avoid releasing precise geometry without a grant)
- **CARE/FAIR posture** (controlled vocabulary; enforceable policy mapping)

> [!CAUTION]
> If a schema includes location geometry and a dataset can be sensitive, design for **dual assets**:
> public/generalized vs restricted/precise, with policy deciding which one can be served.

---

## Definition of Done (boss-checklist)

A PR touching anything validated by policy MUST satisfy:

- [ ] Schema added/updated under `policy/schemas/` (and/or canonical `schemas/`)
- [ ] Schema inventory table updated
- [ ] CI runs schema validation + policy tests (deny-by-default)
- [ ] Promotion/publish artifacts include receipts/manifests and required provenance
- [ ] `spec_hash` is reproducible and recipe-versioned
- [ ] Audit record emission is possible for the change path
- [ ] Sensitive data rules are encoded (classification + access + redaction/generalization if needed)

---

## FAQ

**Why keep schemas near policy?**  
Because these objects sit on the **trust membrane** boundary: policies can only be correct if inputs are well-defined and validated.

**Why deny-by-default?**  
Because missing metadata/provenance must block promotion and prevent unverifiable narratives.

**Can we vendor external schemas here?**  
Yes, but pin them in `_vendored/` with versions and document how updates are reviewed.

