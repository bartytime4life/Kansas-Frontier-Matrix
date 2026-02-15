<!--
KFM — Governed Policy Artifact Schemas
Path: policy/schemas/artifacts/README.md
-->

# KFM Policy Schemas — Artifact Contracts

![Governed](https://img.shields.io/badge/governed-artifact-blue)
![Fail-closed](https://img.shields.io/badge/fail--closed-default%20deny-critical)
![JSON Schema](https://img.shields.io/badge/JSON%20Schema-draft%202020--12-informational)
![Policy](https://img.shields.io/badge/policy-OPA%2FRego-7d64ff)
![Validation](https://img.shields.io/badge/validation-schema%20%2B%20conftest-success)

Contract-first JSON Schemas for KFM’s **promotion-gated artifacts** (manifests, run receipts, audit records, Story Node front matter, etc.).

> [!IMPORTANT]
> This directory sits on the *governance boundary*: **if an artifact is not schema-valid, it is not promotable**.
> Prefer **strict** schemas and **fail-closed** validation. When in doubt, deny promotion.

## Table of contents

- [What lives here](#what-lives-here)
- [How these schemas are used](#how-these-schemas-are-used)
- [Artifact schema registry](#artifact-schema-registry)
- [Schema conventions](#schema-conventions)
- [Validation (local + CI)](#validation-local--ci)
- [Change control](#change-control)
- [Troubleshooting](#troubleshooting)

## What lives here

```text
policy/schemas/artifacts/
├─ README.md
├─ *.schema.json
└─ examples/
   ├─ *.valid.json
   └─ *.invalid.json
```

- **`*.schema.json`**: Governed JSON Schema contracts for KFM artifacts.
- **`examples/`**: Minimal valid/invalid fixtures used for CI and reviewer sanity checks.

> [!NOTE]
> Keep **real data** out of this folder. This is for *contracts* and *fixtures*, not production datasets.

## How these schemas are used

These schemas exist to make KFM’s governance enforceable in tooling:

```mermaid
flowchart LR
  A[Artifact JSON] --> B[Schema validation]
  B -->|valid| C[Policy tests (OPA/Conftest)]
  C -->|allow| D[Promote / Publish]
  C -->|deny| E[Block merge / Block publish]
  B -->|invalid| E
```

Typical enforcement points:

- **CI (PR gates):**
  - Validate artifact instances against these schemas.
  - Run **Conftest** policy packs that assume schema-valid inputs.
- **Runtime (trust membrane):**
  - Gate API requests and promotions with **default-deny** policy.
  - Validate policy inputs and produced artifacts before returning them to any client.

## Artifact schema registry

This folder is for **artifact contracts** (things that are created, signed, promoted, published, audited, or cited).

| Artifact | Schema (expected filename) | Purpose (why it’s governed) | Typical gates |
|---|---|---|---|
| Dataset manifest (raw/source metadata) | `dataset_manifest.v1.schema.json` | Minimum metadata to ingest safely (source, license/rights, sensitivity/classification) | ingest → validate |
| Run manifest / run receipt | `run_manifest.v1.schema.json` | Reproducibility + provenance anchor (spec_hash, inputs/outputs, attestations/signature refs) | promote → validate + attest |
| Story Node front matter (v3) | `story_front_matter.v3.schema.json` | Ensures Story Nodes are reviewable and citeable | story PR → validate |
| Audit record | `audit_record.v1.schema.json` | Append-only audit/log record validation (event type, subject, evidence refs, hash chain) | runtime → log + validate |
| Watcher entry (registry record) | `watcher.v1.schema.json` | Makes watchers discoverable + attestable (endpoint, schedule, outputs, signature ref) | watcher PR → validate + sign |

> [!TIP]
> If you add a new artifact type, add **(1)** a schema, **(2)** at least one `*.valid.json` and `*.invalid.json`,
> and **(3)** a policy/unit test that proves a broken artifact is rejected.

## Schema conventions

### JSON Schema draft + metadata

- Use **JSON Schema draft 2020-12**.
- Every schema must define:
  - `"$schema"` (metaschema URL)
  - `"$id"` (stable canonical identifier for tooling/audit logs)
  - `title`, `description`
  - `type`, and explicit `required` fields

Recommended baseline:

- `additionalProperties: false` at top-level (unless you explicitly document why it must be open-ended).
- Prefer `oneOf` / `anyOf` only when you also provide **examples** for every branch.

### Versioning rules

- Treat schemas as **governed artifacts**.
- **Breaking change = new major version** (new filename and new `$id`).
- Deprecate old versions, but do not delete them unless a governance decision explicitly allows removal.

A pragmatic filename pattern that works well in Git:

- `NAME.vMAJOR.schema.json` (e.g., `run_manifest.v1.schema.json`)
- If the artifact already has a domain version (e.g., Story template `v3`), keep that as the version token.

### IDs, hashes, and receipts

When a schema includes a reproducibility hash (e.g., `spec_hash`), include enough fields to make hashes comparable:

- `spec_schema_id` (points to the schema `$id` the hash was computed over)
- `spec_recipe_version` (how canonicalization/hashing was performed)
- `spec_hash` (digest of the canonicalized spec)

> [!IMPORTANT]
> Hashes without a schema ID and recipe version become ambiguous over time.

## Validation (local + CI)

### 1) Validate schemas (metaschema)

Pick a validator (examples below). Run this whenever you edit a `*.schema.json`.

```bash
# Option A: Python (simple + CI-friendly)
python -m pip install --upgrade check-jsonschema
check-jsonschema --check-metaschema policy/schemas/artifacts/*.schema.json
```

```bash
# Option B: Node (fast local feedback)
npm install -g ajv-cli
ajv validate -m 2020 -s policy/schemas/artifacts/run_manifest.v1.schema.json -d policy/schemas/artifacts/examples/run_manifest.valid.json
```

### 2) Validate example instances

```bash
check-jsonschema \
  --schemafile policy/schemas/artifacts/run_manifest.v1.schema.json \
  policy/schemas/artifacts/examples/run_manifest.valid.json
```

### 3) Run policy/unit tests (OPA/Conftest)

Exact commands depend on where policy packs live in this repo, but the pattern is:

```bash
# Example shape:
conftest test <artifact-or-bundle-path> -p <rego-policy-dir> -d <policy-data-dir>
```

> [!NOTE]
> Policy packs should assume schema-valid inputs and **fail closed** if required keys are missing.

## Change control

All changes to this folder should be treated like production changes.

### Definition of done

- [ ] Schema change is reviewed (governance + engineering).
- [ ] Metaschema validation passes (`--check-metaschema`).
- [ ] Example fixtures added/updated (`examples/*.valid.json` + `examples/*.invalid.json`).
- [ ] Policy/unit tests updated (Conftest/OPA) so invalid artifacts are rejected.
- [ ] Breaking changes are versioned (new major, migration notes added somewhere discoverable).

### Suggested review routing

- Add `CODEOWNERS` entries for:
  - governance reviewers (policy + sensitivity)
  - security reviewers (signatures/attestations)
  - domain stewards (schema semantics)

## Troubleshooting

<details>
<summary><strong>“Schema passes, but policy fails”</strong></summary>

Common causes:

- Policy expects a field name that differs from the schema (rename drift).
- Schema allows optional fields, but policy treats them as required (tighten schema or loosen policy).
- Examples are out-of-date (update fixtures and pin schema versions in CI).

Fix approach:

1. Make the schema/policy contract explicit (align names).
2. Add a failing fixture in `examples/*.invalid.json`.
3. Add/adjust a Conftest unit test proving the denial case.

</details>

<details>
<summary><strong>“We need additionalProperties=true”</strong></summary>

Allowing arbitrary fields increases audit ambiguity.

If you must permit extension fields:

- scope them under a single namespace object (e.g., `extensions: { ... }`)
- document the extension policy and add tests that prevent abuse (e.g., disallow overriding governed keys)

</details>
