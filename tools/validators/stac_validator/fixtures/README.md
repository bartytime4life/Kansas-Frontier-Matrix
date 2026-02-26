<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/2b6d48db-72ef-4c90-9a2c-ef1f1d0a6c2f
title: STAC Validator Fixtures
type: standard
version: v1
status: draft
owners: Tools/Validators (stac_validator)
created: 2026-02-26
updated: 2026-02-26
policy_label: internal
related:
  - kfm://doc/kfm-governance-guide (see KFM_Source_Snapshots_Bundle_from_vNext1_tables_fixed.pdf)
  - tools/validators/stac_validator/README.md (if present)
tags: [kfm, stac, validation, fixtures, testing]
notes:
  - This README documents *fixtures* used by the STAC validator test suite.
  - Replace TODO placeholders after confirming the actual fixture tree and test runner.
[/KFM_META_BLOCK_V2] -->

# STAC Validator Fixtures

Reference STAC JSON fixtures used by the `stac_validator` test suite and related tooling.

**Status:** draft • **Owners:** Tools/Validators • **Policy:** internal (non-production data)

![Status](https://img.shields.io/badge/status-draft-yellow) <!-- TODO: switch to repo-driven badge -->
![Scope](https://img.shields.io/badge/scope-fixtures-blue)
![STAC](https://img.shields.io/badge/STAC-1.x-lightgrey) <!-- TODO: pin actual supported versions -->
![Governance](https://img.shields.io/badge/governed-evidence--first-brightgreen)

---

## Navigation

- [Purpose](#purpose)
- [Where this fits](#where-this-fits)
- [What belongs here](#what-belongs-here)
- [What must not go here](#what-must-not-go-here)
- [Fixture layout](#fixture-layout)
- [Fixture conventions](#fixture-conventions)
- [Adding a new fixture](#adding-a-new-fixture)
- [Maintenance checklist](#maintenance-checklist)
- [Appendix: Fixture templates](#appendix-fixture-templates)

---

## Purpose

This directory contains **STAC documents** used as *fixtures* for:

- ✅ **Positive validation** (known-good STAC that must pass)
- ❌ **Negative validation** (known-bad STAC that must fail, with expected error signatures)
- 🧪 **Regression tests** for previously fixed bugs
- 📚 **Documentation examples** (only when explicitly marked and kept small)

These fixtures are part of the project’s trust membrane: test results should be reproducible, deterministic, and traceable to inputs.

---

## Where this fits

Path (repo-relative):

- `tools/validators/stac_validator/fixtures/`

Typical consumers (names may vary by language/framework):

- unit tests for `stac_validator`
- CLI smoke tests
- CI gates that prevent schema/behavior regressions

---

## What belongs here

Acceptable inputs:

- **STAC JSON** (Catalog / Collection / Item / ItemCollection), stored as `.json`
- Small companion files that make the fixture self-describing, e.g.
  - `fixture.yaml` / `fixture.json` metadata (recommended)
  - `expected_errors.json` (for negative cases)
  - a short `README.md` *inside a fixture folder* when the scenario is non-obvious
- **Tiny** local asset files only when required to test asset-handling logic (keep them minimal)

Recommended per-fixture metadata (PROPOSED):

- a stable `fixture_id`
- declared intent: `valid` / `invalid`
- target entity: `catalog` / `collection` / `item` / `item_collection`
- expected outcome summary (pass/fail + error codes or message fragments)
- provenance notes (synthetic vs derived; license if derived)

---

## What must not go here

Exclusions (fail-closed):

- **Any sensitive or restricted real-world coordinates** (use synthetic geometry or coarse bounding boxes)
- **PII / secrets / credentials** of any form
- Large binaries (imagery, point clouds, etc.) unless explicitly approved and size-capped
- Data with unclear licensing or redistribution rights
- Anything that requires network access at test time (fixtures must be self-contained)

> NOTE: If you *must* include real-world geometry for a regression test, prefer coarse generalization and document the rationale in the fixture’s metadata.

---

## Fixture layout

The exact tree may evolve. Keep the structure **predictable** and **discoverable**.

### Current tree

> TODO (required): Replace this block with the actual output of:
> `tree tools/validators/stac_validator/fixtures -L 3`

```text
fixtures/
  README.md
  (TODO: add actual subdirectories/files here)
```

### Suggested layout

If the directory does not already enforce a layout, the following is a good default (PROPOSED):

```text
fixtures/
  valid/
    catalog__minimal/
      input.json
      fixture.yaml
    collection__minimal/
      input.json
      fixture.yaml
    item__minimal/
      input.json
      fixture.yaml
  invalid/
    item__missing_geometry/
      input.json
      expected_errors.json
      fixture.yaml
    collection__bad_extent/
      input.json
      expected_errors.json
      fixture.yaml
  regression/
    2026-02-26__bug-<slug>/
      input.json
      expected_errors.json
      fixture.yaml
```

---

## Fixture conventions

### Naming

Use names that optimize grep-ability and long-term maintenance:

- `type__scenario` (double underscore)
  - examples: `item__missing_bbox`, `collection__extent_swap`, `catalog__bad_link_rel`

For regression fixtures, prefix with date:

- `YYYY-MM-DD__bug-<ticket-or-slug>`

### JSON determinism

- Format JSON in a stable way (consistent indentation, sorted keys if your formatter supports it)
- Avoid timestamps like “now”, random UUIDs, or non-deterministic ordering
- Prefer minimal examples that isolate the behavior under test

### Expected errors

For invalid fixtures:

- Store the **minimum stable assertion surface**:
  - error *codes* / *types* when available
  - otherwise, stable message fragments (avoid full message equality when upstream libraries change wording)

### Fixture metadata

If you adopt `fixture.yaml` (recommended), keep it compact:

```yaml
fixture_id: item__missing_bbox
intent: invalid
entity: item
notes: Missing bbox should be rejected.
expects:
  valid: false
  errors:
    - contains: "bbox"
    - contains: "required"
```

> TODO: Align the schema above with whatever your validator actually returns.

---

## Adding a new fixture

Checklist (copy/paste):

- [ ] Pick the smallest STAC document that reproduces the behavior.
- [ ] Place it under the correct category (`valid/`, `invalid/`, `regression/` — or the project’s existing equivalents).
- [ ] Add `fixture.yaml` (or the project’s existing metadata format).
- [ ] For invalid fixtures: add `expected_errors.json` (or a minimal matcher spec).
- [ ] Ensure the fixture is **self-contained** (no network calls, no hidden dependencies).
- [ ] Run the validator test suite locally and confirm the new fixture is exercised.
- [ ] If the fixture encodes geographic geometry, confirm it is **synthetic or safe-to-share**.

---

## Maintenance checklist

Use this when:

- bumping STAC version support
- updating schema libraries
- adding/removing validator rules

- [ ] Re-run the full validator test suite.
- [ ] Verify all `valid/` fixtures still pass.
- [ ] Verify all `invalid/` fixtures still fail *for the intended reason*.
- [ ] If error messages changed upstream, prefer updating matchers rather than weakening assertions.
- [ ] Keep fixtures small and minimize duplication.

---

## Appendix: Fixture templates

<details>
<summary>Minimal STAC Item skeleton (template)</summary>

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "example-item",
  "geometry": null,
  "bbox": null,
  "properties": {
    "datetime": "2020-01-01T00:00:00Z"
  },
  "links": [],
  "assets": {}
}
```

> NOTE: This skeleton is intentionally incomplete. Use it as a starting point and then make it valid/invalid on purpose.

</details>

<details>
<summary>fixture.yaml skeleton (template)</summary>

```yaml
fixture_id: <type__scenario>
intent: valid|invalid
entity: catalog|collection|item|item_collection
notes: <short description>
expects:
  valid: true|false
  # Optional; prefer stable matchers over full message equality
  errors:
    - contains: "..."
```

</details>

---

### Back to top

[↑ Back to top](#stac-validator-fixtures)
