<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-domains-hazards-readme
title: tools/validators/domains/hazards/ — Hazards Validator Index
type: readme
version: v0.3
status: draft; repository-grounded; mixed-maturity; non-semantic; non-policy; non-release; non-publication
owner: NEEDS VERIFICATION — CODEOWNERS routes /tools/validators/ to @bartytime4life; no independently verified Hazards validation steward or required-review control was established
created: 2026-07-07
updated: 2026-08-28
policy_label: repository-facing; validators; hazards; deterministic; no-network; cite-or-abstain; not-for-life-safety; release-gated
current_path: tools/validators/domains/hazards/README.md
owning_root: tools/
responsibility: index current Hazards validator implementations and placeholders without defining Hazards meaning, policy, evidence, lifecycle, release, or publication authority
truth_posture: cite-or-abstain; executable claims require current code plus paired deterministic proof; file presence or a green held workflow never establishes source admission, evidence closure, current hazard conditions, life-safety authority, release, or publication
evidence_repository: bartytime4life/Kansas-Frontier-Matrix
evidence_base_ref: main
evidence_base_commit: 2fb5f2c140af2d369d644c754fab0c4caf641465
codeowners_route: /tools/validators/ @bartytime4life
directory_rules_adoption_adr: docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
related:
  - ../../README.md
  - ../../_common/README.md
  - ../README.md
  - ../../../../docs/domains/hazards/README.md
  - ../../../../contracts/domains/hazards/README.md
  - ../../../../schemas/contracts/v1/domains/hazards/README.md
  - ../../../../fixtures/domains/hazards/README.md
  - ../../../../tests/domains/hazards/README.md
  - ../../../../policy/domains/hazards/README.md
  - ../../../../data/registry/sources/hazards/README.md
  - ../../../../release/candidates/hazards/README.md
  - ../../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../../docs/doctrine/directory-rules.md
notes:
  - "v0.3 retires the unused domain-local EvidenceBundle placeholder after confirming the Hazards schema names the substantive repository-root projection validator."
  - "Three scripts have substantive implementations and paired deterministic tests; three scripts remain explicit NotImplementedError placeholders and are not validation evidence."
  - "The EvidenceBundle convergence test enforces the single declared validator path and shared-fixture polarity."
  - "The domain-hazards workflow executes only the bounded smoke and USDM materiality lane; its proof and release jobs remain explicit holds."
  - "This correction removes one unreferenced placeholder and changes no schema, contract, fixture, workflow, policy, source, evidence, lifecycle object, release, deployment, or public surface."
[/KFM_META_BLOCK_V2] -->

# `tools/validators/domains/hazards/` — Hazards Validator Index

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#status)
[![Inventory: 6 scripts](https://img.shields.io/badge/inventory-6%20scripts-2da44e?style=flat-square)](#current-validator-inventory)
[![Executable: 3](https://img.shields.io/badge/executable-3-1f6feb?style=flat-square)](#substantive-implementations)
[![Publisher: no](https://img.shields.io/badge/publisher-no-6e7781?style=flat-square)](#authority-boundary)

> [!IMPORTANT]
> **Validator success is bounded evidence, not Hazards truth.** These tools check declared synthetic or repository-local profiles. They do not admit sources, validate current hazard conditions, issue warnings, create EvidenceBundles, apply policy, promote lifecycle state, approve release, deploy, or publish.

## Purpose

This directory is the Hazards validation implementation lane under the `tools/` responsibility root. It owns repository validator code and this local inventory. Hazards meaning remains under [`contracts/`](../../../../contracts/domains/hazards/README.md); machine shape remains under [`schemas/`](../../../../schemas/contracts/v1/domains/hazards/README.md); fixtures and tests remain under their own roots.

The index reports the exact tree at `main@2fb5f2c140af2d369d644c754fab0c4caf641465`. It distinguishes substantive implementations from tracked placeholders so a file name or a green held job cannot be cited as validation that did not run.

## Status

| Field | Repository-grounded value |
|---|---|
| Owning responsibility root | `tools/` — repository tooling and validators |
| Local scope | Hazards validator implementations and inventory |
| Python scripts | 6 |
| Substantive implementations | 3 |
| Explicit `NotImplementedError` placeholders | 3 |
| Child directories | None |
| CODEOWNERS route | `/tools/validators/ @bartytime4life` |
| Steward assignment | **NEEDS VERIFICATION** beyond the repository route |
| Source admission, policy, release, deployment, publication | Not granted by this lane |

## Authority boundary

[Accepted ADR-0029](../../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts the Directory Rules placement boundary. Validator implementation belongs under `tools/`; tests and fixtures remain separate. A validator reads declared contracts, schemas, fixtures, and policy inputs. It does not define their meaning or mutate their authority.

The Hazards boundary remains fail-closed:

- EvidenceBundle outranks generated language; unresolved evidence requires abstention.
- Observed, regulatory, modeled, aggregate, administrative, candidate, and synthetic roles must not collapse.
- Current-sensitive hazard context requires source-specific time, freshness, expiry, correction, and official-source referral.
- KFM is not an emergency-alert issuer, life-safety instruction surface, or regulatory determination authority.
- Validation, proof construction, policy evaluation, lifecycle promotion, release, deployment, and publication are separate states.

## Current validator inventory

### Substantive implementations

| Validator | Confirmed bounded behavior | Paired executable evidence | Workflow posture |
|---|---|---|---|
| [`validate_drinking_water_advisory.py`](./validate_drinking_water_advisory.py) | Closed proposed advisory profile with deterministic structural and semantic findings | [`test_drinking_water_advisory.py`](../../../../tests/domains/hazards/test_drinking_water_advisory.py) and the [`drinking_water_advisory/`](../../../../fixtures/domains/hazards/drinking_water_advisory/README.md) fixture family | Not part of the two commands executed by `domain-hazards`; covered by separate repository checks where configured |
| [`validate_nfhl_nld_nid_source_role_profile.py`](./validate_nfhl_nld_nid_source_role_profile.py) | Fail-closed NFHL/NLD/NID source-role separation profile | [`test_validate_nfhl_nld_nid_source_role_profile.py`](../../../../tests/validators/domains/hazards/test_validate_nfhl_nld_nid_source_role_profile.py) | Not part of the two commands executed by `domain-hazards`; covered by separate repository checks where configured |
| [`validate_usdm_materiality.py`](./validate_usdm_materiality.py) | Deterministic, no-network USDM material-change evaluation over committed synthetic cases | [`test_validate_usdm_materiality.py`](../../../../tests/domains/hazards/test_validate_usdm_materiality.py) and [`usdm_materiality/cases.json`](../../../../fixtures/domains/hazards/usdm_materiality/cases.json) | Executed by `make hazards-validate`, which is invoked by [`domain-hazards.yml`](../../../../.github/workflows/domain-hazards.yml) |

These relationships prove only their tested profiles and fixture polarity. They do not prove live retrieval, source admission, rights, sensitivity, currentness, complete EvidenceRef resolution, policy activation, release, or public safety.

### Explicit placeholders

The following tracked scripts contain only a placeholder comment, `main()`, and `raise NotImplementedError`:

| Placeholder | Current disposition |
|---|---|
| [`validate_catalog_matrix.py`](./validate_catalog_matrix.py) | **PROPOSED / NOT EXECUTABLE**; the paired Hazards-local contract and fixture family are absent at the pinned tree |
| [`validate_schema.py`](./validate_schema.py) | **PROPOSED / NOT EXECUTABLE**; not a generic validation runner |
| [`validate_source_descriptor.py`](./validate_source_descriptor.py) | **PROPOSED / NOT EXECUTABLE**; source admission and registry validation remain separate |

Placeholder presence is **CONFIRMED**. Behavior, fixture polarity, registry wiring, consumers, and activation are absent or **NEEDS VERIFICATION**. Do not invoke these scripts as successful validators or add them to CI merely to make the inventory look complete.

## Current test and fixture map

The direct Hazards test surface is mixed maturity:

- [`tests/domains/hazards/`](../../../../tests/domains/hazards/README.md) contains the bounded smoke, drinking-water advisory, USDM materiality, and synthetic rollback suites plus additional small boundary tests and child lanes.
- `tests/validators/domains/hazards/` contains the NFHL/NLD/NID source-role test and an EvidenceBundle schema-convergence test. It has no README at the pinned tree.
- [`fixtures/domains/hazards/`](../../../../fixtures/domains/hazards/README.md) contains committed drought, advisory, USDM, rollback, and supporting fixture families. A folder name is not proof that every contained object family has complete valid/invalid/golden coverage.

The EvidenceBundle convergence test checks schema relationships directly, enforces the schema-declared repository-root projection validator, and confirms shared-fixture polarity. No domain-local EvidenceBundle validator alias remains.

## Workflow wiring

The [`domain-hazards`](../../../../.github/workflows/domain-hazards.yml) workflow is executable for pull requests and `main` pushes. Its validation job requires the current Hazards boundary files, runs:

```text
python -m unittest -v tests.domains.hazards.test_hazards_smoke
make hazards-validate
```

The Make target runs the USDM materiality unit tests and `validate_usdm_materiality.py --fixtures` with deterministic no-network environment controls.

The workflow's proof and release-dry-run jobs intentionally emit explicit hold markers. A successful held job confirms that the absence conditions remain as expected; it does not prove that a Hazards ProofPack producer, EvidenceBundle resolver, candidate manifest, release command, or publication path exists.

## Outcomes and interpretation

| Outcome | Meaning |
|---|---|
| `PASS` | The invoked validator completed and reported no finding within its declared profile. |
| `FAIL` | The invoked validator reported a contract, schema, fixture, or invariant violation. |
| `ABSTAIN` / `HOLD` | Available authority or evidence cannot safely support the requested conclusion. |
| `ERROR` | The validator could not safely complete. |
| `NotImplementedError` | Placeholder invoked; **not** a validation result and **not** a pass. |
| `WORKFLOW_SKIPPED_EXPLICIT` | A readiness lane is intentionally held; **not** proof of implementation. |

Individual validators own their finite result grammar. This index does not normalize materially different findings into a shared approval state.

## Inputs and outputs

Permitted inputs are repository contracts, schemas, policy definitions, source descriptors, deterministic public-safe or synthetic fixtures, and explicit configuration within the validator's declared scope.

Permitted outputs are process exit status and deterministic diagnostics or QA artifacts written to an accepted report location. Validator output is not an EvidenceBundle, PolicyDecision, ReviewRecord, ReleaseManifest, warning, alert, regulatory decision, or published object.

## Validation

Current narrow commands include:

```bash
python -m unittest -v tests.domains.hazards.test_hazards_smoke
make hazards-validate
python -m unittest -v tests.domains.hazards.test_drinking_water_advisory
python -m unittest -v tests.validators.domains.hazards.test_validate_nfhl_nld_nid_source_role_profile
python -m unittest -v tests.validators.domains.hazards.test_evidence_bundle_schema_convergence
```

Run only commands whose dependencies are present. Passing these commands remains head-specific evidence for the named surface; it does not activate live sources or advance evidence, policy, lifecycle, release, deployment, or publication state.

## Review burden

Changes route through the repository's `tools/validators/` CODEOWNERS entry. A substantive validator change also requires review of the affected contract, schema, fixture, test, policy, evidence, and release boundaries. Named steward assignments, enforced code-owner review, and independent author/approver separation remain **NEEDS VERIFICATION**.

## Open verification

- Decide whether each placeholder should be implemented, delegated to a shared validator, or retired; do not infer a Hazards-local contract from a shared filename.
- Add or verify complete valid, invalid, edge, and golden fixture polarity for each substantive validator.
- Register validators only after their executable, dependency, result-grammar, and consumer boundaries are closed.
- Verify source-descriptor admission, rights, sensitivity, freshness, EvidenceRef closure, policy, proof, correction, withdrawal, rollback, and release dependencies before operational use.
- Verify every workflow claim against the exact tested head; `SKIPPED`, held, and `NOT_RUN` are not passes.

## Rollback

This README is repository-facing documentation. Rollback is a reviewed revert of its commit. Reverting the index does not change validator code, source state, evidence, policy, lifecycle, release, deployment, or publication state.

## Last reviewed

| Field | Value |
|---|---|
| Evidence date | 2026-08-28 |
| Pinned repository commit | `2fb5f2c140af2d369d644c754fab0c4caf641465` |
| Review result | Six scripts confirmed: three substantive implementations and three explicit `NotImplementedError` placeholders; the unused EvidenceBundle placeholder is retired in favor of the schema-declared repository-root projection validator |
| Next trigger | Validator add/remove/rename, placeholder implementation, fixture/test/workflow change, validator-registry change, source-admission change, or consumer adoption |
