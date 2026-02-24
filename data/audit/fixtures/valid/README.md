<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/3af9fe89-1d8b-4650-9cd1-c8cf3821f3f9
title: Audit fixtures (valid)
type: standard
version: v1
status: draft
owners: TBD
created: 2026-02-24
updated: 2026-02-24
policy_label: restricted
related: []
tags: [kfm, audit, fixtures]
notes:
  - This directory contains *valid* audit-record fixtures used for tests and examples.
  - Update owners/policy_label once governance is confirmed.
[/KFM_META_BLOCK_V2] -->

# `data/audit/fixtures/valid`

**Purpose:** canonical *valid* fixtures for the Audit system (schema + policy boundary) — used to prove “this should pass” in tests, examples, and regression suites.

![Status](https://img.shields.io/badge/status-draft-yellow)
![Policy](https://img.shields.io/badge/policy-restricted-orange)
![Kind](https://img.shields.io/badge/fixtures-valid-success)

---

## Quick navigation

- [Purpose](#purpose)
- [Where this fits](#where-this-fits)
- [Directory contract](#directory-contract)
- [Fixture expectations](#fixture-expectations)
- [Naming conventions](#naming-conventions)
- [Example fixture](#example-fixture)
- [How to add a fixture](#how-to-add-a-fixture)
- [Definition of done](#definition-of-done)
- [Troubleshooting](#troubleshooting)
- [Appendix](#appendix)

---

## Purpose

This folder exists to hold **fixtures that MUST validate successfully** under the audit schema / validator and any applicable audit policy rules.

Use these fixtures to:

- ✅ Lock in the “happy path” for schema + policy evaluation
- ✅ Prevent accidental breaking changes to audit record structure
- ✅ Provide readable examples for developers and reviewers

> WARNING  
> Fixtures must be **synthetic**. Do **not** store real credentials, secrets, PII, or production identifiers here. If you’re unsure whether a field is sensitive, treat it as sensitive and redact or replace with clearly fake data.

[Back to top](#dataauditfixturesvalid)

---

## Where this fits

This directory is part of the governed audit data area:

```text
data/
  audit/
    fixtures/
      valid/        # ✅ fixtures that should pass validation (this folder)
```

Common siblings (if present elsewhere in the repo):

- `data/audit/fixtures/invalid/` — fixtures that **must fail** validation (negative tests)
- `data/audit/schema/` — schema definitions (JSON Schema, Zod, OpenAPI fragments, etc.)
- `data/audit/` — audit domain docs, loader/validator code, and test harnesses

[Back to top](#dataauditfixturesvalid)

---

## Directory contract

### Acceptable inputs

Put **only** self-contained fixture artifacts here.

| Category | Allowed (typical) | Notes |
|---|---|---|
| Audit record fixtures | `*.json`, `*.jsonl`, `*.yaml`, `*.yml` | Use the file format expected by your validator/test harness. |
| Supporting blobs | `*.txt` | Only when referenced by a fixture (e.g., embedded payload samples). |
| Local documentation | `README.md` | This file. Keep it current. |

### Exclusions

Do **not** commit the following into this directory:

- Real user data, secrets, tokens, passwords, API keys
- Environment-specific configuration (e.g., `.env`, kubeconfigs)
- Large binary files (unless the audit system explicitly requires them and they’re synthetic)
- “Invalid” fixtures (those belong in the corresponding invalid-fixtures location, if used)

[Back to top](#dataauditfixturesvalid)

---

## Fixture expectations

The exact audit schema is **repo-defined**, but valid fixtures should generally satisfy these invariants:

### Structural invariants (recommended)

- **Stable identity:** a deterministic `audit_id` (or equivalent) that does not change across runs
- **Time clarity:** timestamps are explicit and parseable (prefer ISO-8601 with timezone, e.g. `2026-02-24T18:05:12Z`)
- **Actor + action + subject:** an audit record clearly states *who did what to what*
- **Evidence/provenance ready:** links to inputs/outputs are represented as references (paths, content hashes, dataset IDs, etc.)
- **Policy label present:** classification label such as `public`/`restricted`/`internal` (match your governance model)
- **No “magic”:** avoid relying on default values that might change; be explicit in fixtures

### Behavioral invariants (required)

- Fixtures in this folder should be **accepted** by the validator.
- Any tests that iterate `fixtures/valid` should treat a validation failure as a **hard failure** (fail closed).

[Back to top](#dataauditfixturesvalid)

---

## Naming conventions

Use a name that makes the scenario obvious and stays stable over time.

**Recommended pattern (proposed):**

```text
<domain>__<scenario>__v<schema_version>.<ext>
```

Examples:

- `audit__minimal__v1.json`
- `audit__with_provenance__v1.json`
- `audit__policy_restricted__v1.json`

**Guidance:**

- Keep names **lowercase** and use `__` to separate segments.
- Include a `v<schema_version>` to make schema migrations explicit.
- Prefer small, focused fixtures (one scenario per file).

[Back to top](#dataauditfixturesvalid)

---

## Example fixture

Below is a **synthetic example** (shape only). Update keys/structure to match the actual audit schema used in this repo.

```json
{
  "audit_id": "audit_00000000_0000_0000_0000_000000000000",
  "schema_version": "1",
  "occurred_at": "2026-02-24T18:05:12Z",
  "recorded_at": "2026-02-24T18:05:12Z",

  "actor": {
    "type": "service",
    "id": "svc_example",
    "display": "Example Service"
  },

  "action": {
    "type": "dataset.promote",
    "result": "success",
    "reason": "Fixture example for schema validation"
  },

  "subject": {
    "type": "dataset",
    "id": "kfm://dataset/example",
    "version": "2026-02-24"
  },

  "policy": {
    "policy_label": "restricted",
    "decision": "allow",
    "ruleset_id": "kfm://policy/ruleset/TODO"
  },

  "provenance": {
    "inputs": [
      { "ref": "kfm://dataset/source/TODO", "sha256": "TODO" }
    ],
    "outputs": [
      { "ref": "kfm://dataset/published/TODO", "sha256": "TODO" }
    ],
    "tooling": {
      "runner": "ci",
      "pipeline": "audit-validator",
      "version": "TODO"
    }
  },

  "notes": [
    "All values are synthetic.",
    "Replace TODOs with deterministic placeholders."
  ]
}
```

[Back to top](#dataauditfixturesvalid)

---

## How to add a fixture

1. **Copy an existing valid fixture** (if one exists) that is closest to your scenario.
2. Modify **one dimension at a time** (e.g., add provenance fields, add a policy decision, add a new action type).
3. Keep it **minimal**: only include the fields needed to express the scenario.
4. Ensure identifiers are **obviously fake** and do not resemble production values.
5. Run the audit validation/test harness and confirm the fixture passes.

> TIP  
> If you can’t find the validator entrypoint quickly, search the repo for: `fixtures/valid`, `audit schema`, `validate_audit`, or `audit fixture`.

[Back to top](#dataauditfixturesvalid)

---

## Definition of done

A new valid fixture is “done” when:

- [ ] It validates successfully with the current schema/validator
- [ ] It is deterministic (no random IDs, no “now()” timestamps unless explicitly part of the test)
- [ ] It contains **no** secrets, PII, or production identifiers
- [ ] It has a clear scenario name following the naming convention
- [ ] Any associated tests/docs are updated (if the fixture is used as a golden example)

[Back to top](#dataauditfixturesvalid)

---

## Troubleshooting

### “Fixture validates locally but fails in CI”

- Check for **timezone/locale** differences (always prefer `Z` timestamps in fixtures).
- Ensure the fixture does not depend on environment variables or runtime defaults.
- Confirm the schema version in the fixture matches what CI expects.

### “Schema changed — what now?”

- Do not edit old fixtures in-place if they represent an older contract that must remain supported.
- Add a new fixture version (e.g., `__v2`) and update tests accordingly.
- If the change is a breaking change, ensure migration strategy and promotion gates are updated.

[Back to top](#dataauditfixturesvalid)

---

## Appendix

<details>
<summary><strong>Audit record field glossary (suggested)</strong></summary>

- **audit_id**: deterministic identifier for an audit record.
- **occurred_at**: when the underlying event happened.
- **recorded_at**: when the audit system recorded the event.
- **actor**: the principal performing the action (user, service, job).
- **action**: the operation performed and its outcome.
- **subject**: the entity being acted upon (dataset, pipeline, API key, etc.).
- **policy**: classification + allow/deny decision details.
- **provenance**: evidence chain (inputs/outputs, hashes, tool versions).

</details>
