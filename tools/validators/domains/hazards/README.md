<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-domains-hazards-readme
title: tools/validators/domains/hazards/ — Hazards Validator Index
type: readme
version: v0.19
status: draft; repository-grounded; mixed-maturity; non-semantic; non-policy; non-release; non-publication
owner: NEEDS VERIFICATION — CODEOWNERS routes /tools/validators/ to @bartytime4life; no independently verified Hazards validation steward or required-review control was established
created: 2026-07-07
updated: 2026-09-01
policy_label: repository-facing; validators; hazards; deterministic; no-network; cite-or-abstain; not-for-life-safety; release-gated
current_path: tools/validators/domains/hazards/README.md
owning_root: tools/
responsibility: index current Hazards validator implementations and placeholders without defining Hazards meaning, policy, evidence, lifecycle, release, or publication authority
truth_posture: cite-or-abstain; executable claims require current code plus paired deterministic proof; file presence or a green held workflow never establishes source admission, evidence closure, current hazard conditions, life-safety authority, release, or publication
evidence_repository: bartytime4life/Kansas-Frontier-Matrix
evidence_base_ref: main
evidence_base_commit: 7e5bfa8e178940876f90d096613661a72c0ae66b
evidence_base_role: pre-change evidence base; the inventory below includes this proposed branch change and is exact only at the branch head reported by GitHub
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
  - "v0.19 denies every repository-local symlink path component before resolving or reading a snapshot, preventing an ancestor alias from bypassing the declared input path."
  - "v0.18 converts ancestor symlink-resolution loops into the finite symlink-denied error instead of allowing a RuntimeError to escape the validator."
  - "v0.17 reports repository-relative targets and redacts external host paths, preventing local usernames or mount structure from leaking through the result envelope."
  - "v0.16 enforces the declared repository-local file boundary before reading a snapshot, preventing arbitrary external paths from becoming validator inputs."
  - "v0.15 binds first-after-last and last-after-retrieval ordering findings to the exact timestamp field that violates its boundary."
  - "v0.14 prevents timestamps with unknown local offsets from participating in derived ordering, freshness, or expiration findings after they are denied."
  - "v0.13 denies RFC3339's unknown-local-offset marker on snapshot timestamps so ordering and freshness checks cannot silently treat unknown local time as exact UTC."
  - "v0.12 rejects subsecond programmatic evaluation instants so semantic evaluation and the canonical whole-second result envelope cannot disagree about the evaluated instant."
  - "v0.11 keeps explicit-time findings temporally coherent: an evaluation before retrieval is denied as pre-retrieval and cannot also claim that the not-yet-retrieved carrier was expired at that evaluation instant."
  - "v0.10 makes the explicit evaluation interface canonical and replay-safe by accepting only timezone-aware RFC3339 whole-second instants with a known, valid offset before normalizing them to UTC in the result envelope."
  - "v0.9 binds each file-validation result to retrieval-relative or explicit-as-of evaluation and emits a canonical UTC evaluation time when supplied, so downstream consumers can distinguish the meaning of PASS without inspecting source values."
  - "v0.8 adds an optional caller-supplied evaluation instant so current snapshots can be deterministically denied after expiry without consulting a clock or network."
  - "v0.7 adds deterministic, no-network temporal ordering and freshness-budget validation for the existing inactive KDHE HAB advisory snapshot profile; it does not activate the source or authorize alerts, release, deployment, or publication."
  - "v0.6 corrects the hosted-workflow inventory: drinking-water advisory and NFHL/NLD/NID already have dedicated hosted workflows on the pinned base, while domain-hazards remains the bounded smoke and USDM materiality lane."
  - "v0.5 incorrectly classified the drinking-water advisory and NFHL/NLD/NID test families as not run in hosted workflows; that statement is superseded by current workflow evidence."
  - "v0.4 retires the unused domain-local generic-schema placeholder after confirming that no Hazards schema or consumer names it and repository-wide schema validation is already established."
  - "Four scripts have substantive implementations and paired deterministic tests; two scripts remain explicit NotImplementedError placeholders and are not validation evidence."
  - "The EvidenceBundle convergence test enforces the single declared validator path and shared-fixture polarity."
  - "The domain-hazards workflow executes the bounded smoke and USDM materiality lane; dedicated profile workflows execute the drinking-water advisory and NFHL/NLD/NID suites; proof and release jobs remain explicit holds."
  - "The v0.6 workflow-inventory correction changed documentation only; it changed no validator implementation, schema, contract, fixture, test, workflow, policy, source, evidence, lifecycle object, release, deployment, or public surface."
[/KFM_META_BLOCK_V2] -->

# `tools/validators/domains/hazards/` — Hazards Validator Index

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#status)
[![Inventory: 6 scripts](https://img.shields.io/badge/inventory-6%20scripts-2da44e?style=flat-square)](#current-validator-inventory)
[![Executable: 4](https://img.shields.io/badge/executable-4-1f6feb?style=flat-square)](#substantive-implementations)
[![Publisher: no](https://img.shields.io/badge/publisher-no-6e7781?style=flat-square)](#authority-boundary)

> [!IMPORTANT]
> **Validator success is bounded evidence, not Hazards truth.** These tools check declared synthetic or repository-local profiles. They do not admit sources, validate current hazard conditions, issue warnings, create EvidenceBundles, apply policy, promote lifecycle state, approve release, deploy, or publish.

## Purpose

This directory is the Hazards validation implementation lane under the `tools/` responsibility root. It owns repository validator code and this local inventory. Hazards meaning remains under [`contracts/`](../../../../contracts/domains/hazards/README.md); machine shape remains under [`schemas/`](../../../../schemas/contracts/v1/domains/hazards/README.md); fixtures and tests remain under their own roots.

The pre-change evidence base is `main@7e5bfa8e178940876f90d096613661a72c0ae66b`. The inventory below additionally includes the KDHE HAB temporal validator proposed on this branch and is exact only at the branch head reported by GitHub. It distinguishes substantive implementations from tracked placeholders and distinguishes the aggregate Hazards workflow from dedicated profile workflows so hosted evidence is not understated or overstated.

## Status

| Field | Repository-grounded value |
|---|---|
| Owning responsibility root | `tools/` — repository tooling and validators |
| Local scope | Hazards validator implementations and inventory |
| Python scripts | 6 |
| Substantive implementations | 4 |
| Explicit `NotImplementedError` placeholders | 2 |
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
| [`validate_drinking_water_advisory.py`](./validate_drinking_water_advisory.py) | Closed proposed advisory profile with deterministic structural and semantic findings | [`test_drinking_water_advisory.py`](../../../../tests/domains/hazards/test_drinking_water_advisory.py) and the [`drinking_water_advisory/`](../../../../fixtures/domains/hazards/drinking_water_advisory/README.md) fixture family | Hosted by dedicated [`drinking-water-advisory.yml`](../../../../.github/workflows/drinking-water-advisory.yml), which runs the focused unit suite and exact fixture replay; exact-head hosted result is required before claiming PASS |
| [`validate_kdhe_hab_temporal.py`](./validate_kdhe_hab_temporal.py) | Repository-local file admission, deterministic cross-field observation ordering, source-time ordering, active-state currentness, retrieval-relative freshness enforcement, canonical RFC3339-second explicit-time expiry evaluation, and evaluation-basis binding for the inactive KDHE HAB advisory snapshot profile | [`test_validate_kdhe_hab_temporal.py`](../../../../tests/validators/domains/hazards/test_validate_kdhe_hab_temporal.py) and the existing [`kdhe_hab_advisory_snapshot/`](../../../../fixtures/domains/hazards/kdhe_hab_advisory_snapshot/) valid/invalid families | Not separately hosted at this boundary; local focused proof and exact fixture replay are required, and hosted checks must not be described as profile execution unless a workflow actually invokes it |
| [`validate_nfhl_nld_nid_source_role_profile.py`](./validate_nfhl_nld_nid_source_role_profile.py) | Fail-closed NFHL/NLD/NID source-role separation profile | [`test_validate_nfhl_nld_nid_source_role_profile.py`](../../../../tests/validators/domains/hazards/test_validate_nfhl_nld_nid_source_role_profile.py) | Hosted by dedicated [`nfhl-nld-nid-source-role-profile.yml`](../../../../.github/workflows/nfhl-nld-nid-source-role-profile.yml), which runs the focused deterministic no-network suite and exact fixture replay; exact-head hosted result is required before claiming PASS |
| [`validate_usdm_materiality.py`](./validate_usdm_materiality.py) | Deterministic, no-network USDM material-change evaluation over committed synthetic cases | [`test_validate_usdm_materiality.py`](../../../../tests/domains/hazards/test_validate_usdm_materiality.py) and [`usdm_materiality/cases.json`](../../../../fixtures/domains/hazards/usdm_materiality/cases.json) | Executed by `make hazards-validate`, which is invoked by [`domain-hazards.yml`](../../../../.github/workflows/domain-hazards.yml) |

These relationships prove only their tested profiles and fixture polarity. They do not prove live retrieval, source admission, rights, sensitivity, currentness, complete EvidenceRef resolution, policy activation, release, or public safety.

### Explicit placeholders

The following tracked scripts contain only a placeholder comment, `main()`, and `raise NotImplementedError`:

| Placeholder | Current disposition |
|---|---|
| [`validate_catalog_matrix.py`](./validate_catalog_matrix.py) | **PROPOSED / NOT EXECUTABLE**; the paired Hazards-local contract and fixture family are absent at the pinned tree |
| [`validate_source_descriptor.py`](./validate_source_descriptor.py) | **PROPOSED / NOT EXECUTABLE**; source admission and registry validation remain separate |

Placeholder presence is **CONFIRMED**. Behavior, fixture polarity, registry wiring, consumers, and activation are absent or **NEEDS VERIFICATION**. Do not invoke these scripts as successful validators or add them to CI merely to make the inventory look complete.

## Current test and fixture map

The direct Hazards test surface is mixed maturity:

- [`tests/domains/hazards/`](../../../../tests/domains/hazards/README.md) contains the bounded smoke, drinking-water advisory, USDM materiality, and synthetic rollback suites plus additional small boundary tests and child lanes.
- `tests/validators/domains/hazards/` contains the NFHL/NLD/NID source-role test, the KDHE HAB temporal-validator test, and an EvidenceBundle schema-convergence test. It has no README at the pinned tree.
- [`fixtures/domains/hazards/`](../../../../fixtures/domains/hazards/README.md) contains committed drought, advisory, USDM, rollback, and supporting fixture families. A folder name is not proof that every contained object family has complete valid/invalid/golden coverage.

The EvidenceBundle convergence test checks schema relationships directly, enforces the schema-declared repository-root projection validator, and confirms shared-fixture polarity. No domain-local EvidenceBundle validator alias remains.

Repository-wide schema validation remains owned by [`schema-validation.yml`](../../../../.github/workflows/schema-validation.yml), `make schemas`, and the shared [`jsonschema_runner.py`](../../_common/jsonschema_runner.py). Every canonical Hazards schema is included by that all-schema inventory. No Hazards schema, contract, fixture, test, workflow, registry entry, or consumer named the removed generic-schema placeholder, and accepted Directory Rules prohibit empty symmetry scaffolding.

## Workflow wiring

The [`domain-hazards`](../../../../.github/workflows/domain-hazards.yml) workflow is executable for pull requests and `main` pushes. Its validation job requires the bounded Hazards materiality boundary and runs:

```text
python -m unittest -v tests.domains.hazards.test_hazards_smoke
make hazards-validate
```

The Make target runs the USDM materiality unit tests and `validate_usdm_materiality.py --fixtures` with deterministic no-network environment controls.

Two additional substantive profiles are already hosted through dedicated workflows rather than through `domain-hazards`:

```text
.github/workflows/drinking-water-advisory.yml
  -> python -m unittest tests.domains.hazards.test_drinking_water_advisory --verbose
  -> python tools/validators/domains/hazards/validate_drinking_water_advisory.py --fixtures

.github/workflows/nfhl-nld-nid-source-role-profile.yml
  -> focused unittest discovery for test_validate_nfhl_nld_nid_source_role_profile.py
  -> python tools/validators/domains/hazards/validate_nfhl_nld_nid_source_role_profile.py --fixtures
```

That dedicated coverage is hosted evidence only when an exact-head run actually executes and succeeds. It does not imply that the aggregate `domain-hazards` workflow owns those profile triggers, and duplicating the suites into that aggregate lane is not required to establish that they are hosted.

The `domain-hazards` proof and release-dry-run jobs intentionally emit explicit hold markers. A successful held job confirms that the absence conditions remain as expected; it does not prove that a Hazards ProofPack producer, EvidenceBundle resolver, candidate manifest, release command, or publication path exists.

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

KDHE HAB file validation admits only paths that resolve within the repository root and denies every repository-local symlink path component before resolving or reading the snapshot. This prevents a repository-local ancestor alias from redirecting the caller's declared input path. External paths return a finite error before reading. Result envelopes report admitted inputs as repository-relative paths and replace external or unresolvable host paths with `<outside-repository>`, so local usernames and mount structure are not exposed. Output identifies whether validation was retrieval-relative or used an explicit caller-supplied evaluation instant. Snapshot timestamps and the CLI evaluation instant must carry a known offset; RFC3339's unknown-local-offset marker (`-00:00`) is denied rather than collapsed to UTC or used for derived ordering, freshness, or expiration findings. Observation-order findings bind first-after-last to `/first_observed_at` and last-after-retrieval to `/last_observed_at`, preserving an actionable field path without assigning causal authority. The CLI otherwise accepts only timezone-aware RFC3339 whole-second instants with a valid offset, and the programmatic interface rejects evaluation instants whose normalized UTC value has subsecond precision. Accepted instants are normalized to UTC in the result, while retrieval-relative output uses a null evaluation time. An instant before retrieval yields the pre-retrieval finding and does not also assert explicit-time expiration for a carrier that did not yet exist. This canonical binding supports deterministic replay but does not create a runtime DecisionEnvelope, EvidenceBundle, approval, alert, or current-condition claim.

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
python -m unittest -v tests.validators.domains.hazards.test_validate_kdhe_hab_temporal
python tools/validators/domains/hazards/validate_kdhe_hab_temporal.py --fixtures
python tools/validators/domains/hazards/validate_kdhe_hab_temporal.py --as-of 2026-07-25T15:00:01Z path/to/repository-local-snapshot.json
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
| Evidence date | 2026-09-01 |
| Pre-change repository commit | `7e5bfa8e178940876f90d096613661a72c0ae66b` |
| Review result | Six scripts confirmed: four substantive implementations and two explicit `NotImplementedError` placeholders; the KDHE HAB temporal profile has focused deterministic local proof but no dedicated hosted workflow at this boundary |
| Next trigger | Validator add/remove/rename, placeholder implementation, fixture/test/workflow change, validator-registry change, source-admission change, or consumer adoption |
