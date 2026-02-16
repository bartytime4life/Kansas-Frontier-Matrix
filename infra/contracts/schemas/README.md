# Schema contracts

![Contract First](https://img.shields.io/badge/contract--first-required-brightgreen)
![Fail Closed](https://img.shields.io/badge/fail--closed-enforced-critical)
![JSON Schema](https://img.shields.io/badge/json--schema-2020--12-blue)
![Governed](https://img.shields.io/badge/governed-artifact-orange)

This directory contains **machine-validated schema contracts** that act as hard boundaries between KFM stages (pipeline → catalogs → graph → API → UI → narrative). If an artifact does **not** validate, it is **not trusted** and must be treated as **untrusted** across the platform.

> [!IMPORTANT]
> **Fail-closed rule:** invalid or unsigned artifacts must not be promoted, must not be treated as verified evidence, and must not receive “trusted/green” UI affordances.

---

## What belongs here

This folder is the canonical home for **cross-cutting, infrastructure-grade schema contracts**, especially contracts that:

- are produced by automated runs (watchers, ETL jobs, validators)
- are consumed by **policy gates** (OPA/Rego + CI checks)
- are displayed in evidence UX (e.g., receipt viewers, trust badges)
- must remain stable and versioned because many subsystems depend on them

Typical contracts include (examples; adjust to repo reality):

- **Run receipt**: per-run evidence record (inputs/outputs/checks/timestamps)
- **Run manifest**: promotion-focused rollup for release/publish lanes
- **Watcher registry**: signed allow-list for automation agents (“watchers”)

---

## Directory layout

```text
repo-root/
└─ infra/
   └─ contracts/
      └─ schemas/
         ├─ README.md
         ├─ run_receipt.v1.schema.json
         ├─ run_manifest.v1.schema.json
         ├─ watcher.v1.schema.json
         └─ examples/
            ├─ run_receipt.valid.json
            ├─ run_receipt.invalid.missing_spec_hash.json
            ├─ run_manifest.valid.json
            ├─ watcher.valid.json
            └─ watcher.invalid.unsigned.json
```

> [!NOTE]
> The `examples/` fixtures are not “nice-to-have” — they are intended to be **CI gates**. At minimum: one **valid** and one **invalid** example per schema.

---

## Schema index

| Contract | File | Primary producers | Primary consumers | Notes |
|---|---|---|---|---|
| Run receipt | `run_receipt.v1.schema.json` | pipelines, watchers | CI policy gates, provenance resolver, evidence UX | One per run; includes deterministic identifiers and checks |
| Run manifest | `run_manifest.v1.schema.json` | promotion lanes, release workflows | PR gates, publishing automation, audit tooling | Rollup for promotion; includes publish-candidate metadata |
| Watcher registry | `watcher.v1.schema.json` | governance maintainers | watcher orchestrator, CI allow/deny, Focus Mode | Signed allow-list to prevent automation drift |

---

## Non-negotiable contract rules

### 1) Strict validation

- Prefer **JSON Schema draft 2020-12**
- Use strict shapes:
  - `additionalProperties: false` (or `unevaluatedProperties: false` when appropriate)
  - explicit `required` fields
  - explicit formats (e.g., `uri`, RFC3339 timestamps)

### 2) Deterministic identity fields

Contracts that describe a run or publish candidate should include deterministic identifiers (examples):

- `spec_hash`: hash of canonicalized inputs + contract IDs + code blocks
- `subject`: content address (digest), not a mutable tag/label

> [!CAUTION]
> Hashes must be computed from **canonicalized bytes** (avoid “false drift” caused by whitespace/order differences).

### 3) Fail-closed checks

If the schema includes a `checks` or similar structure:

- any failure MUST block promotion/publishing
- missing checks MUST be treated as failure

### 4) Signed automation contracts

Watcher/automation contracts should embed fields that enable verification:

- a `signature_ref` (or equivalent) that can be resolved and verified
- a `spec_hash` so CI can detect drift

---

## Validation workflow

### Local validation

Below are example commands (adapt to your repo tooling):

```bash
# Example: validate examples against JSON Schemas (tooling not confirmed in repo)
ajv validate \
  --spec=draft2020 \
  -s infra/contracts/schemas/run_receipt.v1.schema.json \
  -d infra/contracts/schemas/examples/run_receipt.valid.json

# Example: run policy checks (OPA/Rego via conftest) on the same artifact
conftest test infra/contracts/schemas/examples/run_receipt.valid.json -p infra/contracts/policy/opa
```

### CI expectations

Minimum expected CI gates for this folder:

- ✅ schema compilation / load check (no broken refs)
- ✅ all `examples/*.valid.json` must pass
- ✅ all `examples/*.invalid*.json` must fail (negative testing)
- ✅ policy checks must fail-closed when required fields are missing

---

## Versioning policy

These schemas are **contract artifacts** and must be versioned explicitly.

### File naming

- `name.v1.schema.json` = **major version 1**
- breaking changes ⇒ new major file:
  - keep old majors in place until deprecation window ends
  - consumers must migrate intentionally

### Compatibility rules

- Additive changes (new optional fields) can stay in the same major.
- Removing or renaming required fields is breaking ⇒ bump major.

---

## How to add a new schema

Checklist for a PR that introduces or changes a schema:

- [ ] Add schema file `*.vN.schema.json`
- [ ] Add at least:
  - [ ] one valid fixture
  - [ ] one invalid fixture
- [ ] Update the **Schema index** table in this README
- [ ] Add/adjust CI validation so invalid fixtures fail as expected
- [ ] If schema affects promotion, add/adjust policy gate tests (OPA/Rego)
- [ ] Document any sensitivity impact (see next section)

Definition of Done for a schema PR:

- CI fails on invalid examples
- schema validation is a required status check
- README documents the contract fields and invariants

---

## Governance and sensitivity

Some contracts may carry sensitive elements (e.g., exact locations, restricted identifiers, private attributes). When a schema could expose sensitive data:

- include a `policy_label` / classification field (if your governance model uses one)
- ensure API/policy layers enforce redaction and access control
- prefer generalized coordinates for sensitive sites and protect the original precision

> [!IMPORTANT]
> Do not “solve” sensitivity in the UI. Enforcement belongs in the governed API + policy boundary.

---

## Design anchors

These schema patterns are aligned with the broader KFM contract-first and evidence-first approach. When implementing or revising these contracts, ensure they still support:

- deterministic pipelines
- provenance-first publication
- governed API surfaces (redaction, classification, and auditability)
- fail-closed promotion workflows
