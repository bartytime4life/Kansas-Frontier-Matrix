# KFM Tooling Libraries (`tools/lib`) 🧰

![governed](https://img.shields.io/badge/governed-yes-blue)
![evidence-first](https://img.shields.io/badge/evidence--first-required-brightgreen)
![fail-closed](https://img.shields.io/badge/policy-fail--closed-critical)
![ci-ready](https://img.shields.io/badge/CI-acceptance%20harness%20ready-success)
![semver](https://img.shields.io/badge/versioning-semver-informational)

Shared, **reusable**, **reviewable**, and **testable** libraries used by KFM’s tooling layer (watchers, validators, catalog generators, promotion/acceptance checks, provenance packaging, and evidence/citation utilities).

> [!IMPORTANT]
> This directory is **governed** because it can directly impact:
> - promotion gates (what becomes publishable),
> - provenance integrity (what can be cited/audited),
> - policy enforcement behavior (what is blocked/allowed),
> - trust UI signals (what gets a “trusted” badge).

---

## Table of contents

- [Why this exists](#why-this-exists)
- [Scope](#scope)
- [Non-negotiables](#non-negotiables)
- [Truth path alignment](#truth-path-alignment)
- [Directory layout](#directory-layout)
- [Core library responsibilities](#core-library-responsibilities)
- [Normative contracts](#normative-contracts)
  - [`spec_hash`](#spec_hash)
  - [`run_manifest` / `run_receipt`](#run_manifest--run_receipt)
  - [Evidence locators & resolvers](#evidence-locators--resolvers)
  - [Policy evaluation](#policy-evaluation)
  - [Signature verification helpers](#signature-verification-helpers)
- [Testing & determinism](#testing--determinism)
- [CI / acceptance harness integration](#ci--acceptance-harness-integration)
- [Security & supply chain](#security--supply-chain)
- [Versioning & compatibility](#versioning--compatibility)
- [Contributing](#contributing)
- [Glossary](#glossary)
- [References](#references)

---

## Why this exists

KFM tooling is intentionally *evidence-first* and *policy-enforced*. Many tools need the **same** primitives:

- deterministic hashing (`spec_hash`) for stable IDs and reproducible diffs
- schema validation (STAC/DCAT/PROV, receipts/manifests)
- policy “deny-by-default” gates
- evidence packaging and resolution
- signature/attestation verification hooks for CI gates

`tools/lib` is where those primitives live so they are:
- consistent across all pipelines
- easier to test
- easier to review (governance)
- harder to accidentally bypass

---

## Scope

### In scope ✅

- Canonicalization and hashing utilities (e.g., `spec_hash`)
- Schema definitions + validators (JSON Schema; STAC/DCAT/PROV validation wrappers)
- “Run” artifact types (manifest/receipt models + helpers)
- Policy utilities (OPA/Rego invocation helpers, Conftest harness glue)
- Evidence/citation resolver helpers (stable locator parsing, URL normalization)
- Test fixtures + golden files for determinism
- Library glue for acceptance harness checks (but **not** the entire CI system itself)

### Out of scope ❌

- Application/runtime business logic (belongs in services)
- Frontend UI components
- Direct database access from UI-facing tooling (violates trust membrane)
- Secrets, credentials, or environment-specific values
- One-off scripts with no tests/validation

---

## Non-negotiables

> [!IMPORTANT]
> These rules are **MUST** requirements for anything added to `tools/lib`.

### 1) Trust membrane (no direct DB/UI shortcuts)

- Tooling **MUST NOT** enable any path where a UI/external client can “reach around” governed APIs.
- Any integration intended for UI consumption must flow through the governed gateway and policy boundary.

### 2) Fail-closed by default

- If required fields, required provenance, required signatures, or required policy decisions are missing/invalid:
  - **fail the check**
  - **block promotion**
  - **produce a machine-readable error report**

### 3) Only publish from “processed” outputs

- Library behavior must assume: **raw** and **work** zones are not publishable.
- Anything that generates artifacts intended for publication must target **processed** outputs and produce catalogs/provenance required by policy.

### 4) “No Source, No Answer” supports cite-or-abstain UX

- Evidence references must remain resolvable and stable.
- Citation/Evidence locators must be machine-checkable so QA can measure “citation resolvable” rates.

---

## Truth path alignment

The libraries here support KFM’s governed “truth path” from acquisition → validation → publication:

```mermaid
flowchart LR
  A[Acquire / Watch] --> B[Raw Zone]
  B --> C[Work Zone]
  C --> D[Processed Zone]
  D --> E[Catalogs: STAC / DCAT + PROV links]
  E --> F[Stores: object/registry/search]
  F --> G[Governed API boundary + policy checks]
  G --> H[UI / Story Nodes]
  H --> I[Focus Mode (cite-or-abstain)]
```

> [!NOTE]
> Tools in this folder should make it *easy* to follow this path and *hard* to bypass it.

---

## Directory layout

This repo may be polyglot; the layout below is the **recommended** stable shape for `tools/lib`.
If your repo differs, keep the same *conceptual separation* (schemas vs policy vs code vs fixtures).

```text
tools/
└─ lib/
   ├─ README.md                # this file
   ├─ schemas/                 # JSON Schemas (run_manifest, watcher schema, etc.)
   ├─ policy/                  # OPA/Rego bundles + conftest scaffolding
   ├─ fixtures/                # small deterministic test fixtures + golden outputs
   ├─ canonical/               # canonicalization + hashing utilities (spec_hash)
   ├─ receipts/                # run_manifest/run_receipt helpers (models + IO)
   ├─ catalogs/                # STAC/DCAT/PROV helpers (generation + validation glue)
   ├─ evidence/                # evidence locators, resolver contracts, URL normalization
   ├─ signing/                 # signature/attestation verification wrappers (tool-agnostic)
   └─ _shared/                 # shared helpers (logging, errors, I/O), if needed
```

**Rule:** Every subfolder that exposes reusable code must have:
- its own small `README.md` (scope + API + tests)
- tests (unit + contract/golden where relevant)
- a minimal changelog/notes (or reference root changelog)

---

## Core library responsibilities

| Responsibility | Why it exists | Typical outputs |
|---|---|---|
| Deterministic hashing (`spec_hash`) | Stable IDs, reproducibility, audit equivalence | `sha256:<digest>` |
| Receipt/manifest helpers | Provenance anchored to an execution/run | `run_manifest.json` / `run_receipt.json` |
| Catalog helpers | Publishable discovery + interoperability | STAC Item/Collection, DCAT dataset, PROV links |
| Policy gate glue | Deny-by-default enforcement in CI + local verify | pass/fail + reasons |
| Evidence utilities | “No Source, No Answer” + cite panel support | resolvable evidence refs |
| Signature verification wrappers | Supply-chain trust gates | verification results + metadata |

---

## Normative contracts

This section is **normative**: libraries implementing these concerns must honor these contracts.

### `spec_hash`

**Definition (normative):**

- `spec_hash` is a **sha256** hash of a **canonicalized** spec object.
- Canonicalization must be deterministic so two equivalent specs hash identically.

**Required metadata alongside a spec_hash:**
- `spec_schema_id` (what schema defines the object)
- `spec_recipe_version` (what canonicalization recipe version was used)

> [!IMPORTANT]
> Any change to canonicalization rules is a **breaking change** (see [Versioning & compatibility](#versioning--compatibility)).

**Implementation guidance:**
- Prefer JSON canonicalization via **RFC 8785 (JCS)** when the spec is JSON.
- If authoring is YAML, convert to a schema-defined object then canonicalize deterministically.

**Example pseudo-code (language-agnostic):**

```text
spec_hash(spec):
  assert spec is validated against schema(spec_schema_id)
  canonical = JCS(spec)                # RFC 8785 canonical JSON serialization
  digest = SHA256(canonical)
  return "sha256:" + digest
```

---

### `run_manifest` / `run_receipt`

**Purpose:** A run receipt is the minimal portable provenance artifact that lets KFM prove:
- what was fetched/produced,
- under what spec,
- with what tool versions,
- with what policy outcomes,
- and where evidence artifacts live.

**Required minimum fields (normative baseline):**
- `run_id`
- `fetched_at` (timestamp)
- `source_url` (or equivalent anchor/ref)
- `spec_hash`
- `artifact_digest` (digest of the produced publishable artifact/bundle)
- `tool_versions` (at least the pipeline/tool)
- `policy_gate.status` and a list of checks evaluated

**Optional but recommended:**
- HTTP caching metadata (ETag, Last-Modified)
- links to generated catalogs (STAC/DCAT) and lineage references (PROV pointers)
- signatures/attestations references (e.g., Rekor UUIDs)

> [!NOTE]
> The concrete schema should live under `tools/lib/schemas/` and be enforced by validators in CI and local verify.

---

### Evidence locators & resolvers

Evidence references **must** be:
- stable,
- resolvable by automated checks,
- safe to expose (respecting sensitivity policies),
- and compatible with UI “Cite” affordances.

**Resolver contract (normative expectations):**
- inputs: an evidence locator (e.g., digest address, gateway address)
- outputs:
  - canonical resolved URL (UI-safe)
  - content-type metadata
  - integrity metadata (digest) if available
  - access class (public/generalized/restricted)

> [!IMPORTANT]
> Evidence resolvers MUST support QA measurement: “does this locator resolve?” and MUST NOT silently fall back to ambiguous sources.

---

### Policy evaluation

Policy evaluation is designed to be **deny-by-default**.

**Normative behavior:**
- missing required fields → deny
- missing required provenance → deny
- missing required signatures/attestations when required → deny
- policy engine errors → deny (fail-closed)

**Deliverable expectations:**
- machine-readable decision output (JSON)
- human-readable summary for logs/PR checks

---

### Signature verification helpers

This folder may include wrappers around verification steps (e.g., signature verification, attestation verification) **but not** hard-coded infrastructure endpoints or secrets.

**Normative behavior:**
- verification failure → deny (fail-closed)
- verification output must be captured in CI logs and (when required) in receipt metadata

---

## Testing & determinism

Everything in `tools/lib` must be testable locally and in CI.

### Required test types

- **Unit tests:** basic correctness
- **Golden (snapshot) tests:** canonicalization/hashing outputs are stable over time
- **Schema contract tests:** validate fixtures against schemas
- **Policy contract tests:** Conftest/OPA policies produce expected decisions for fixtures

### Fixture guidance

Keep fixtures:
- small
- synthetic (when possible)
- deterministic
- committed under `tools/lib/fixtures/`

Example fixture types:
- minimal run_receipt JSON
- minimal STAC item/collection examples
- minimal DCAT dataset examples
- minimal PROV link objects
- policy “should pass” and “should fail” cases

---

## CI / acceptance harness integration

`tools/lib` should make it easy to implement an “acceptance harness” that:

- validates **STAC/DCAT/PROV**
- runs **OPA/Rego + Conftest** policy tests
- verifies signatures/attestations (e.g., cosign verify)
- checks deterministic `spec_hash` reproducibility

### Expectations for CI wiring

A repo using these libs should be able to implement:

- a local `make verify` (or equivalent) that runs the same checks CI runs
- a CI workflow/job that:
  1. installs/pins validator & policy tooling
  2. runs schema validations
  3. runs policy tests
  4. runs signature verification
  5. fails the job on any unmet requirement (fail-closed)

> [!NOTE]
> CI implementation details live outside `tools/lib`, but `tools/lib` should supply:
> - stable commands or wrappers,
> - stable output formats (JSON),
> - consistent exit codes,
> - and documentation for how to run checks.

---

## Security & supply chain

Because these libs support promotion gates:

- Dependencies should be pinned.
- Tool versions used in CI should be pinned and reviewable.
- Avoid shelling out without sanitizing inputs.
- Avoid network calls in core logic unless explicitly required and tested.

### Secrets policy

- **Never** commit secrets here.
- **Never** write code that prints secrets (including tokens, signed URLs) to logs.
- Use environment variables only at the *tooling entrypoint* layer, not inside reusable libs.

---

## Versioning & compatibility

### SemVer policy

Libraries in `tools/lib` should follow **SemVer**:

- **MAJOR**: breaking changes to:
  - canonicalization rules (JCS recipe changes)
  - schema required fields
  - policy decision semantics
  - evidence locator formats
- **MINOR**: additive changes (new optional fields, new helpers)
- **PATCH**: bug fixes that do not change external behavior

### Compatibility promise

- Receipts/manifests should remain forward-readable where possible.
- Policy changes must be explicitly versioned and tested against fixtures.

---

## Contributing

### Adding a new library (Definition of Done)

- [ ] New code lives in a clearly named subfolder under `tools/lib/`
- [ ] Subfolder includes a `README.md` (scope, API, how to test)
- [ ] Unit tests exist and run locally
- [ ] Deterministic/golden tests exist if output must be stable (hashing, canonicalization, generated catalogs)
- [ ] Fixtures exist (pass + fail cases)
- [ ] CI can run the checks (or a documented local verify command exists)
- [ ] No secrets, no environment-specific endpoints
- [ ] Changes that affect promotion/policy/schemas are flagged for governance review

### Changing “governed” behavior

If your change affects any of these:
- `spec_hash` rules
- required receipt fields
- policy pack behavior
- evidence locator formats
- signature verification rules

…treat it as a **governed artifact change**:
- document the change
- add/adjust fixtures
- add/adjust contract tests
- require review by security + data governance stakeholders

---

## Glossary

- **Acceptance harness**: A standardized set of validations + policy checks + signature verification used in CI/local verify.
- **Fail-closed**: If anything required is missing or invalid, the system denies promotion and blocks merge/publish.
- **Promotion gate**: The enforceable checks required before something becomes publishable/served.
- **Receipt / manifest**: The portable provenance record for a tool run (what happened, when, with what spec and outputs).
- **spec_hash**: Deterministic canonical hash of a schema-defined spec, used for stable IDs and reproducibility.
- **Trust membrane**: The enforced boundary preventing UI/external clients from bypassing governed APIs/policy checks.

---

## References

### Internal KFM governance sources (primary for this repo)

- *KFM NextGen Blueprint and Primary Guide* (v1.x; prepared 2026-02-12)
- *Integrating “New Ideas Feb-2026” Into Knowledge-First Management* (promotion contract, policy pack, acceptance harness)
- *KFM Integration Report for KFM New Ideas 2-8-26* (gaps + normalization recommendations)

### External standards referenced by KFM concepts

- RFC 8785 — JSON Canonicalization Scheme (JCS)
- W3C DCAT v3 — dataset catalog vocabulary
- W3C PROV — provenance data model
- STAC — SpatioTemporal Asset Catalog specification
- Open Policy Agent (OPA) + Conftest
- SPDX (SBOM) + SLSA (supply chain provenance expectations)

