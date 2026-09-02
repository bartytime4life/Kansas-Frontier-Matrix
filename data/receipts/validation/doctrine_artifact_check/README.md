<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/data-receipts-validation-doctrine-artifact-check-readme
title: Doctrine artifact check validation receipts README
type: readme
version: v0.2
status: draft
owner: docs steward
last_reviewed: 2026-06-28
policy_label: internal
path: data/receipts/validation/doctrine_artifact_check/README.md
lifecycle_root: data/receipts
receipt_class: validation
tags:
  - kfm
  - receipts
  - validation
  - doctrine
  - artifacts
  - fail-closed
  - governance
related:
  - control_plane/document_registry_doctrine_required.yaml
  - policy/source/doctrine_artifact_required.rego
  - scripts/maintenance/check_required_doctrine_artifacts.py
  - tests/policy/test_doctrine_artifact_required.py
  - docs/doctrine/directory-rules.md
notes:
  - "Receipts record validation process memory; they do not become source authority, proof packs, release manifests, or promotion decisions."
  - "This README documents the existing doctrine-artifact prerequisite check and its receipt lane."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Doctrine artifact check validation receipts

![status](https://img.shields.io/badge/status-draft-yellow?style=flat-square)
![lifecycle](https://img.shields.io/badge/lifecycle-data%2Freceipts-orange?style=flat-square)
![receipt](https://img.shields.io/badge/receipt-validation-blue?style=flat-square)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-critical?style=flat-square)
![promotion](https://img.shields.io/badge/promotion-no--side--effects-lightgrey?style=flat-square)

> **Purpose.** Store JSON receipts emitted by the required doctrine artifact check. These receipts show what the validator observed about required doctrine artifacts at a particular run boundary; they do **not** prove the doctrine is correct, admit artifacts by themselves, publish artifacts, or promote anything.

---

## Scope

This folder belongs to the `data/receipts/validation/` lifecycle branch. It is a narrow receipt lane for the maintenance check implemented at:

```text
scripts/maintenance/check_required_doctrine_artifacts.py
```

The check reads the required doctrine-artifact registry by default from:

```text
control_plane/document_registry_doctrine_required.yaml
```

It checks the doctrine artifact directory by default at:

```text
docs/doctrine/artifacts
```

The related policy source is:

```text
policy/source/doctrine_artifact_required.rego
```

The related tests are:

```text
tests/policy/test_doctrine_artifact_required.py
```

---

## What belongs here

| Item | Belongs here? | Notes |
|---|---:|---|
| Local smoke receipts such as `run-local-smoke.json` | Yes | Useful for a maintainer-visible dry run. |
| CI validation receipts keyed by workflow run id | Yes | Use stable names that do not hide prior results. |
| Failed validation receipts | Yes | Negative outcomes are process memory and should remain inspectable. |
| JSON output from `--output <path>` | Yes | This is the canonical receipt shape for this lane. |
| Doctrine PDF artifacts | No | Keep doctrine artifacts in the doctrine artifact home, not in receipts. |
| Proof bundles or signatures | No | Use `data/proofs/` or the appropriate proof lane. |
| Release manifests or promotion decisions | No | Use `release/` for release decisions and manifests. |
| Catalog records | No | Use `data/catalog/`; receipt presence is not catalog closure. |
| Policy source | No | Policy lives under `policy/`. |

---

## Receipt meaning

A receipt in this folder records that the check ran and emitted an observed result. It answers questions like:

- Which registry was checked?
- Which artifact directory was checked?
- Which required artifacts were present or missing?
- Did declared status and observed presence disagree?
- Were any present artifacts too small for the configured threshold?
- Did any required artifacts share duplicate hashes?
- Did the check return `pass` or `fail`?

It does **not** answer these questions by itself:

- Are the doctrine artifacts authoritative?
- Are the artifacts rights-cleared for publication?
- Has a steward reviewed the artifacts?
- Has policy approved public release?
- Has catalog closure happened?
- Has a promotion decision been recorded?

Those stronger conclusions require the appropriate evidence, policy, review, proof, catalog, and release objects.

---

## Current implementation boundary

| Claim | Status | Basis |
|---|---:|---|
| The maintenance check can write a JSON receipt when called with `--output`. | CONFIRMED | Implemented in `scripts/maintenance/check_required_doctrine_artifacts.py`. |
| The check returns `0` for `pass` and `1` for `fail`. | CONFIRMED | Implemented by the script return path. |
| The check fails closed when required artifacts are missing, status mismatches exist, artifacts are too small, or duplicate required-artifact hashes are detected. | CONFIRMED | Implemented by the script's `result` calculation. |
| Tests currently expect the check to fail until canonical artifacts are admitted. | CONFIRMED | Covered by `tests/policy/test_doctrine_artifact_required.py`. |
| CI emits date-scoped receipts into this folder. | UNKNOWN | No workflow evidence is asserted here. |
| The doctrine artifact admission workflow is fully enforced for publication. | NEEDS VERIFICATION | Requires policy, CI, review, and release evidence. |

---

## Receipt schema outline

The emitted JSON is intentionally small and reviewable. Current fields include:

| Field | Meaning |
|---|---|
| `check` | Stable check name, currently `required_doctrine_artifacts`. |
| `registry` | Registry path used for required artifact definitions. |
| `artifacts_dir` | Directory inspected for required doctrine artifacts. |
| `required_count` | Number of required artifacts from the registry. |
| `missing_count` | Number of required artifacts not found. |
| `missing` | List of missing artifact filenames. |
| `present` | Map of required filename to observed presence boolean. |
| `status_mismatches` | Required artifacts whose registry status disagrees with observed presence. |
| `integrity.min_bytes_required` | Minimum byte threshold used for present artifacts. |
| `integrity.too_small` | Present artifacts below the byte threshold. |
| `integrity.duplicate_hash_groups` | Required artifacts that hash to the same digest. |
| `result` | `pass` or `fail`. |

Illustrative receipt shape:

```json
{
  "check": "required_doctrine_artifacts",
  "registry": "control_plane/document_registry_doctrine_required.yaml",
  "artifacts_dir": "docs/doctrine/artifacts",
  "required_count": 3,
  "missing_count": 1,
  "missing": [
    "Master_MapLibre_Components-Functions-Features.pdf"
  ],
  "present": {
    "Kansas_Frontier_Matrix_Definitive_Greenfield_Building_Plan_v1_1.pdf": true,
    "KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf": true,
    "Master_MapLibre_Components-Functions-Features.pdf": false
  },
  "status_mismatches": [],
  "integrity": {
    "min_bytes_required": 10000,
    "too_small": {},
    "duplicate_hash_groups": {}
  },
  "result": "fail"
}
```

> [!NOTE]
> The example is illustrative. Do not treat it as a real run receipt unless it is emitted by the script and committed with an appropriate review note.

---

## How to emit a local smoke receipt

Run from the repository root:

```bash
python scripts/maintenance/check_required_doctrine_artifacts.py \
  --output data/receipts/validation/doctrine_artifact_check/run-local-smoke.json
```

The command prints the same JSON payload to stdout and writes the receipt to the requested path.

A `fail` result is still a valid receipt when it accurately records missing or nonconforming prerequisites. Do not delete failed receipts merely because they are failures; use them to drive the next correction.

---

## Naming guidance

Prefer stable, reviewable names:

```text
run-local-smoke.json
ci-<workflow-name>-<run-id>.json
YYYY-MM-DD/<run-id>-required-doctrine-artifacts.json
```

Guidance:

- Keep one intentionally named local smoke receipt when useful.
- Prefer date-scoped folders if CI produces repeated receipts.
- Avoid overwriting historical CI receipts unless the file is clearly disposable.
- Use a follow-up receipt or a Git revert instead of silently editing a committed run receipt.

---

## Review checklist

Before relying on a receipt from this lane, verify:

- [ ] The receipt was produced by `scripts/maintenance/check_required_doctrine_artifacts.py` or a documented wrapper.
- [ ] `check` equals `required_doctrine_artifacts`.
- [ ] `registry` points to the intended registry for the run.
- [ ] `artifacts_dir` points to the intended doctrine artifact directory for the run.
- [ ] `missing`, `status_mismatches`, `too_small`, and `duplicate_hash_groups` were reviewed.
- [ ] A `pass` result is not treated as promotion, publication, or catalog closure.
- [ ] A `fail` result is retained long enough to support correction and audit.

---

## Validation commands

Run the policy/script tests:

```bash
pytest tests/policy/test_doctrine_artifact_required.py
```

Run the check directly:

```bash
python scripts/maintenance/check_required_doctrine_artifacts.py
```

Run the check and write this lane's receipt:

```bash
python scripts/maintenance/check_required_doctrine_artifacts.py \
  --output data/receipts/validation/doctrine_artifact_check/run-local-smoke.json
```

---

## Promotion and publication boundary

This folder is downstream process memory. It does not publish doctrine artifacts and it does not authorize public use.

A healthy later workflow may use these receipts as inputs to review, policy, catalog, proof, release, or correction processes. That workflow must keep each object family separate:

```text
receipt -> review input -> policy/release decision -> catalog/proof linkage -> published surface
```

Never collapse the chain into:

```text
receipt -> public truth
```

---

## Correction and rollback

If a receipt is wrong because the command was run with the wrong registry or artifact directory, prefer one of these actions:

1. Emit a corrected receipt with a clearer filename.
2. Add a review note in the PR explaining which receipt supersedes the bad one.
3. Revert the commit if the receipt should not have been committed.

Do not rewrite history or quietly edit a committed receipt in a way that hides what happened.

---

## Open questions

| Question | Status |
|---|---:|
| Should CI emit doctrine-artifact receipts into date-scoped folders by default? | NEEDS VERIFICATION |
| Should the Rego policy consume this script output directly or remain a separate policy assertion? | NEEDS VERIFICATION |
| Which doctrine-artifact receipts should be public, steward-only, or internal? | NEEDS VERIFICATION |
| Should this receipt shape be formalized under `schemas/contracts/v1/receipts/` or another accepted schema home? | NEEDS VERIFICATION / ADR-class if it creates a new receipt schema layout |

---

## Maintainer note

This README intentionally keeps receipts separate from doctrine artifacts, proofs, catalog records, and release decisions. That separation preserves KFM's trust membrane: process memory is inspectable, but it is not sovereign truth.
