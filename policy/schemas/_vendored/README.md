# `_vendored/` — Third‑Party JSON Schemas (Pinned & Offline)

> **Path:** `policy/schemas/_vendored/`
>
> This directory contains **vendored (third‑party) JSON Schemas** that KFM depends on for policy input validation, contract validation, and CI gates—**pinned and stored locally** to keep builds deterministic and to avoid network-based `$ref` resolution.

> [!IMPORTANT]
> **Do not “casually edit” vendored schemas.** Treat them like external dependencies:
> - **Pinned** to a specific upstream version/commit/release
> - **Integrity-checked** (hashes)
> - **License-preserved**
> - **Reviewed** like a security-sensitive change

---

## Why this exists

KFM governance is **deny-by-default / fail-closed**, with policy checks and schema validation expected to run in CI and at the governed boundary.:contentReference[oaicite:3]{index=3}:contentReference[oaicite:4]{index=4}

Vendoring schemas in-repo ensures:

- **Deterministic builds**: no surprise upstream changes.
- **Offline validation**: CI and local workflows do not require reaching the internet to resolve `$ref`s.
- **Supply-chain safety**: pin + hash the exact bytes.
- **Auditability**: schema provenance becomes part of the governed artifact chain.

---

## What belongs here

Vendored schemas are **external** to KFM and needed for validation, interoperability, or policy evaluation.

Typical examples (non-exhaustive):

- JSON Schema metaschemas / vocabularies (e.g., specific drafts)
- Upstream schemas for formats KFM consumes/produces (e.g., standard catalogs, interchange formats)
- Third-party contract schemas used by tools (e.g., OpenAPI JSON Schema fragments, CloudEvents, etc.)
- Any external schema referenced by KFM schemas via `$ref`

> [!NOTE]
> The *actual* set of vendored schemas varies by repo needs. This README defines the governance + workflow, not a fixed inventory.

---

## What does **not** belong here

Keep these **out** of `_vendored/`:

- **KFM-authored schemas** (these belong in `policy/schemas/…` outside `_vendored/`)
- Generated artifacts that can be reproduced from source (unless they are required for offline `$ref` resolution and are pinned + hashed)
- Experimental/temporary files
- Anything containing secrets or sensitive data (schemas should be public artifacts)

---

## Directory layout expectations

This folder is intentionally “boring”: it should be easy to audit and hard to accidentally break.

A recommended structure:

```
policy/
└─ schemas/
   └─ _vendored/                                   # Pinned upstream schema snapshots (reproducible validation)
      ├─ README.md                                  # What’s vendored, why, and the update/review procedure
      ├─ SOURCES.lock.yml                           # REQUIRED: registry of vendored schemas (url/ref, hash, license, notes)
      ├─ LICENSES/                                  # Upstream license/notice texts (when required by source terms)
      │
      └─ <vendor_or_standard>/                      # Source namespace (e.g., stac, w3c, schema-org, opengis, etc.)
         └─ <name>/                                 # Schema family/project name
            └─ <version_or_commit>/                 # Immutable version tag or commit SHA (no “latest”)
               ├─ schema.json                        # Primary entry schema (the root contract used by validators)
               └─ …                                  # Any referenced/dependent schemas (kept alongside for offline use)
```

> [!TIP]
> If the repository already uses a different layout, keep it—**but** ensure you still meet the invariants:
> pinned version, integrity hashes, license preservation, offline `$ref` resolution, CI validation.

---

## The lock/registry file: `SOURCES.lock.yml`

Every vendored schema **MUST** have an entry in `SOURCES.lock.yml` (or an equivalent lock file). This enables review and automation.

### Required fields

| Field | Required | Meaning |
|---|---:|---|
| `id` | ✅ | Stable internal identifier (e.g., `json-schema.draft2020-12.core`) |
| `local_path` | ✅ | Repo path to the vendored schema file |
| `upstream` | ✅ | Source URL/repo + tag/commit/release reference |
| `version` | ✅ | Version/tag or commit SHA (whatever upstream uses) |
| `retrieved_at` | ✅ | Date fetched (ISO 8601) |
| `sha256` | ✅ | SHA-256 of the exact file bytes stored in repo |
| `license` | ✅ | SPDX id if known (or `UNKNOWN` with follow-up required) |
| `notes` | ⛔ | Why it is needed / any caveats |
| `dependencies` | ⛔ | Other vendored schema IDs it `$ref`s |

### Example `SOURCES.lock.yml`

```yaml
vendored_schemas:
  - id: json-schema.draft2020-12.meta
    local_path: policy/schemas/_vendored/json-schema/draft2020-12/schema.json
    upstream:
      source: https://example.org/upstream/json-schema
      ref: "draft/2020-12"
    version: "2020-12"
    retrieved_at: "2026-02-15"
    sha256: "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    license: "MIT"
    notes: "Used as metaschema for KFM-owned JSON Schemas."
    dependencies: []

  - id: stac.1.0.0.collection
    local_path: policy/schemas/_vendored/stac/1.0.0/collection.json
    upstream:
      source: https://example.org/upstream/stac-spec
      ref: "v1.0.0"
    version: "1.0.0"
    retrieved_at: "2026-02-15"
    sha256: "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
    license: "Apache-2.0"
    notes: "Validates STAC Collections emitted by pipelines."
    dependencies:
      - stac.1.0.0.common
```

> [!IMPORTANT]
> If `SOURCES.lock.yml` does not exist yet, create it as part of the first vendoring PR.
> The review expectation is that future updates are **diffable** and **hash-verified**.

---

## Rules for vendoring (hard invariants)

### 1) Preserve upstream content (byte-for-byte) unless documented

- Prefer **exact copies** from upstream.
- Do not “fix formatting” or rewrap lines unless upstream uses stable formatting and your change is proven non-semantic.
- If a change is unavoidable, do it via the **patch workflow** below.

### 2) All `$ref`s must resolve offline

- If a vendored schema references others, vendor those dependencies too.
- CI must validate with **network disabled** (or validator configured to disallow remote resolution).

### 3) Licenses and notices must be preserved

- If upstream includes LICENSE/NOTICE requirements, copy them into `policy/schemas/_vendored/LICENSES/`.
- Record `license` in `SOURCES.lock.yml`.

### 4) Treat vendored schemas as governed artifacts

Changes to vendored schemas can alter validation outcomes and therefore policy behavior. That means:
- PR review is mandatory
- CI validation gates are mandatory
- Changes are subject to security review expectations (supply chain hygiene)

This aligns with KFM’s broader “validators + policy tests in CI” posture.:contentReference[oaicite:5]{index=5}:contentReference[oaicite:6]{index=6}

---

## Patch workflow (when you must deviate from upstream)

If you must change a vendored schema to work in KFM (e.g., upstream bug, broken `$ref`, non-portable `$id`), do **not** silently edit.

Instead:

1. Keep the **original** file under `_vendored/…`
2. Add a patch file under a sibling patch area (recommended):
   - `policy/schemas/_vendored/_patches/<schema-id>.patch`
3. In `SOURCES.lock.yml`, add:
   - `patched: true`
   - `patch_ref: policy/schemas/_vendored/_patches/<schema-id>.patch`
   - `patch_reason: ...`
4. Link to an upstream issue/PR in `notes` (if applicable)

> [!WARNING]
> Patches should be **minimal**, **justified**, and **reviewed** as if they were production policy changes.

---

## How KFM code/policy should reference vendored schemas

General rules:

- Prefer **relative `$ref` paths** within the repository.
- Avoid remote `$id` URLs as runtime dependencies.
- Validators should load schemas from disk and resolve `$ref`s locally.

### Example (KFM-owned schema referencing vendored metaschema)

```json
{
  "$schema": "./_vendored/json-schema/draft2020-12/schema.json",
  "$id": "https://kfm.example.org/policy/schema/example.json",
  "type": "object",
  "properties": { "hello": { "type": "string" } }
}
```

> [!NOTE]
> The `$id` can remain the canonical KFM identifier while `$schema` points locally. The key requirement is that validation is reproducible and offline.

---

## Validation & CI expectations

KFM’s integration approach expects **validators** and **policy tests** to run in CI, and emphasizes deny-by-default governance patterns.:contentReference[oaicite:7]{index=7}:contentReference[oaicite:8]{index=8}

### Minimum required checks for PRs touching `_vendored/`

- [ ] `SOURCES.lock.yml` updated (new/changed schema entries, hashes, versions)
- [ ] Hashes verified (recomputed in CI)
- [ ] Schema validation pass with **offline `$ref` resolution**
- [ ] OPA/Conftest policy tests pass (if schemas influence policy input validation)
- [ ] License/notice requirements preserved
- [ ] Review completed by:
  - [ ] Maintainer (schema/policy owner)
  - [ ] Security/governance reviewer (when changing validation semantics)

> [!TIP]
> If your repo has an “acceptance harness” workflow that runs validators + conftest, ensure `_vendored/` changes are included in the harness scope.:contentReference[oaicite:9]{index=9}

---

## Security considerations

Vendored schemas are “data,” but they are still a **supply-chain input**:

- A malicious schema can cause:
  - validation bypasses (too-permissive constraints)
  - denial-of-service in validators (pathological recursion)
  - unexpected remote resolution attempts
- Therefore:
  - **Pin + hash** everything
  - **Disable remote ref resolution** in CI validators
  - Prefer schemas from authoritative upstream projects
  - Add regression tests for any schema that gates sensitive promotion or access

---

## Troubleshooting

### `$ref` resolution fails
**Symptoms:** validator complains “cannot resolve reference …”.

**Fix checklist:**
- [ ] Vendor the referenced schema file(s)
- [ ] Confirm the on-disk path matches the `$ref`
- [ ] If `$ref` uses URLs, either:
  - vendor under a resolver mapping that supports that URL, or
  - apply patch workflow to rewrite `$ref` to a local path

### Draft mismatch
**Symptoms:** keywords not recognized, metaschema mismatch.

**Fix checklist:**
- [ ] Ensure the correct metaschema draft is vendored and referenced
- [ ] Do not mix drafts unless you have explicit tooling support

### `$id` collisions
**Symptoms:** validator registers wrong schema for an `$id`.

**Fix checklist:**
- [ ] Keep schemas in distinct directories by version/commit
- [ ] Avoid editing upstream `$id` unless patch workflow is used and justified

---

## Ownership & change control

This folder is part of **policy/schema governance**.

Recommended ownership model:

- **CODEOWNERS** entry for `policy/schemas/_vendored/**`
- Required review from:
  - Policy/schema maintainers
  - Security/governance reviewer for material changes

> [!NOTE]
> “Material change” includes updates that loosen validation, change required fields, or alter schema behavior in ways that could affect access/promotion decisions.

---

## Quick checklist for adding a new vendored schema

- [ ] Identify authoritative upstream + version/commit
- [ ] Download schema + all transitive `$ref` dependencies
- [ ] Store under `_vendored/<name>/<version>/…`
- [ ] Compute `sha256` for each file (bytes on disk)
- [ ] Update `SOURCES.lock.yml`
- [ ] Add required license/notice text
- [ ] Run offline schema validation locally
- [ ] Open PR with rationale + review notes

---

## Glossary

- **Vendored**: copied into the repo from upstream and pinned.
- **Pinned**: tied to a specific version/tag/commit, not “latest”.
- **Offline validation**: validation that does not need network access to resolve `$ref`s.
- **Fail-closed**: when inputs are missing/invalid, the system denies or blocks rather than guessing.

---

