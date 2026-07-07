<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-policy-readme
title: Policy Tests README
type: test-readme
version: v0.2
status: draft; expanded-from-boundary-suite; policy-test-lane; PROPOSED / NEEDS VERIFICATION
owners:
  - OWNER_TBD - Test steward
  - OWNER_TBD - Policy steward
  - OWNER_TBD - Governance steward
  - OWNER_TBD - QA steward
  - OWNER_TBD - Release steward
created: 2026-07-06
updated: 2026-07-06
policy_label: public-doc; tests; policy; governance-guardrails; boundary-tests; fail-closed; no-network; evidence-aware; release-gated; trust-membrane
tags: [kfm, tests, policy, governance, boundary-guards, fail-closed, deny, restrict, abstain, redaction, public-release, promotion, sensitivity, no-network, ABSTAIN, DENY, ERROR]
related:
  - ../README.md
  - ../fixtures/README.md
  - ../../policy/README.md
  - ../../schemas/contracts/v1/policy/
  - ../../contracts/policy/
  - ../../apps/governed-api/tests/test_boundary_guards.py
  - ../../.github/workflows/policy-boundary-guards.yml
  - ../../artifacts/qa/
notes:
  - "This README expands the existing tests/policy/README.md boundary-suite stub without dropping its concrete test names, command, workflow, or report artifact note."
  - "This lane documents policy and governance guardrail tests. It is not policy authority; policy rules belong under policy/."
  - "Existing README content named test_control_plane_register_meta_contract.py, test_explorer_web_adapter_boundary.py, test_pipeline_connector_non_publisher.py, boundary_constants.py, apps/governed-api/tests/test_boundary_guards.py, policy-boundary-guards.yml, make boundary-guards-ci, and artifacts/qa/policy-boundary-guards.xml. Presence of those referenced files beyond this README remains NEEDS VERIFICATION unless separately inspected."
  - "Executable test inventory, runner wiring, policy bundles, schema bindings, CI pass rates, and report generation remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Policy tests

> Test-lane README for policy and governance guardrail tests under `tests/policy/`. This lane proves policy boundaries, fail-closed behavior, and trust-membrane rules without becoming policy authority, schema authority, release approval, or production runtime code.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Lane: policy tests" src="https://img.shields.io/badge/lane-policy__tests-purple">
  <img alt="Posture: fail closed" src="https://img.shields.io/badge/posture-fail__closed-critical">
  <img alt="CI: needs verification" src="https://img.shields.io/badge/CI-NEEDS__VERIFICATION-lightgrey">
</p>

**Path:** `tests/policy/README.md`  
**Status:** draft / expanded from existing boundary-suite README / PROPOSED until executable inventory and CI are verified  
**Owning root:** `tests/`  
**Lane family:** `policy`  
**Policy authority root:** `policy/`  
**Default posture:** deterministic, no-network, fixture-backed, fail-closed policy tests only  
**Truth posture:** CONFIRMED this README previously named three boundary tests, a shared constants file, a pytest command, a CI workflow name, and a CI report artifact path; CONFIRMED `tests/` is the canonical enforceability root; CONFIRMED `policy/` is the canonical policy-as-code and policy-documentation root; NEEDS VERIFICATION for referenced file existence, policy bundle coverage, runtime wiring, CI pass rates, and generated report parity.

---

## Scope

Use `tests/policy/` for executable policy and governance guardrail tests.

In scope:

- allow / deny / restrict / abstain / redaction / sensitivity / public-release / promotion policy tests;
- boundary tests for control-plane registers, governed API adapters, explorer-web adapter behavior, and connector or pipeline non-publisher posture;
- negative tests for unknown rights, unresolved sensitivity, missing review, stale source, missing release state, and forbidden public paths;
- tests that prove policy decisions remain finite and fail closed;
- tests that consume synthetic fixtures from `tests/fixtures/`, root `fixtures/`, or policy fixture lanes after verification;
- local parity commands and CI report-output notes.

Out of scope:

- policy rule definitions;
- schema, contract, or release definitions;
- production application code;
- lifecycle data, source exports, EvidenceBundles, receipts, proofs, or release records;
- real sensitive material, source credentials, production logs, generated CI outputs, or public artifacts.

[Back to top](#top)

---

## Repo fit

| Responsibility | Correct home | Relationship |
|---|---|---|
| Policy and governance guardrail tests | `tests/policy/` | This lane. |
| Policy rules and policy documentation | `policy/` | Authority root; tests verify behavior. |
| Policy schemas | `schemas/contracts/v1/policy/` or accepted schema home | Shape authority; tests reference. |
| Policy contracts | `contracts/policy/` | Semantic authority; tests verify. |
| Governed API boundary tests | `apps/governed-api/tests/` where app-owned | App test companion referenced by this lane. |
| Unit-test fixtures | `tests/fixtures/` | Test-local inputs. |
| Cross-cutting fixtures | `fixtures/` | Shared synthetic/golden inputs. |
| Release decisions | `release/` | Publication authority; tests can block, not approve. |
| CI report artifacts | `artifacts/qa/` or CI artifact storage | Output/report location, not policy authority. |

> [!IMPORTANT]
> `tests/policy/` must not become a second policy root, schema home, contract home, source registry, release store, fixture archive, or generated-artifact authority. Tests assert expected policy behavior; they do not define policy.

---

## Existing boundary suite

The previous README named this boundary suite:

| Test or support file | Purpose | Status |
|---|---|---|
| `test_control_plane_register_meta_contract.py` | Control-plane register metadata contract guardrail. | Referenced by existing README; file presence NEEDS VERIFICATION. |
| `test_explorer_web_adapter_boundary.py` | Explorer Web adapter boundary guardrail. | Referenced by existing README; file presence NEEDS VERIFICATION. |
| `test_pipeline_connector_non_publisher.py` | Pipeline/connector non-publisher guardrail. | Referenced by existing README; file presence NEEDS VERIFICATION. |
| `boundary_constants.py` | Shared constants for boundary tests. | Referenced by existing README; file presence NEEDS VERIFICATION. |
| `apps/governed-api/tests/test_boundary_guards.py` | Governed API boundary guard companion. | Referenced by existing README; file presence NEEDS VERIFICATION. |

Preserve these names unless the executable files are renamed and the command below is updated with the same commit.

---

## Policy-test rule

Policy tests prove that policy gates are enforceable and fail closed. A passing policy test should never imply that a source is authoritative, evidence is complete, release is approved, or public display is allowed unless those states are explicitly modeled and allowed by the policy under test.

Core expectations:

| Expectation | Required posture |
|---|---|
| Fail-closed default | Unknown rights, unresolved sensitivity, missing review, stale source, missing evidence, or missing release blocks. |
| Finite outcomes | Expected outcomes remain explicit: `ALLOW`, `DENY`, `RESTRICT`, `ABSTAIN`, `REDACT`, `ERROR`, or validation failure. |
| No-network default | Default tests use synthetic fixtures and do not call live sources, APIs, models, tiles, vendors, or public services. |
| Evidence-subordinate | Policy tests do not fabricate EvidenceBundles or upgrade unsupported claims. |
| Release-aware | Public-release or promotion tests do not turn a policy pass into release approval. |
| Boundary-aware | Frontend, connector, pipeline, and control-plane paths must not bypass governed policy gates. |
| Sensitive-safe | Sensitive-lane examples use public-safe transformed fixtures only. |

---

## Expected test families

| Family | What it proves | Expected outcome |
|---|---|---|
| `rights_unknown_denies` | Unknown or unresolved rights fail closed. | `DENY` / `ABSTAIN`. |
| `sensitivity_unverified_denies` | Unverified sensitivity blocks public display or release. | `DENY`. |
| `review_missing_denies` | Missing required review blocks promotion or publication. | `DENY`. |
| `stale_source_abstains` | Stale source support does not become current truth. | `ABSTAIN`. |
| `redaction_required` | Restricted content is redacted, generalized, delayed, denied, or withheld. | `REDACT` / `DENY`. |
| `public_release_gate` | Release policy requires evidence, rights, sensitivity, validation, review, correction, and rollback posture. | `DENY` / `ALLOW` when modeled. |
| `control_plane_boundary` | Control-plane registers do not become runtime/public truth authority. | validation failure / `DENY`. |
| `adapter_boundary` | Web/API adapters do not bypass policy or read internal stores directly. | validation failure / `DENY`. |
| `pipeline_connector_non_publisher` | Connectors and pipelines do not publish or approve release. | `DENY` / validation failure. |
| `finite_policy_outcome` | Policy runtime returns bounded outcomes rather than ambiguous success. | `ALLOW` / `DENY` / `RESTRICT` / `ABSTAIN` / `ERROR`. |

---

## Run locally

The existing README provided this local command:

```bash
pytest -q \
  tests/policy/test_control_plane_register_meta_contract.py \
  tests/policy/test_explorer_web_adapter_boundary.py \
  tests/policy/test_pipeline_connector_non_publisher.py \
  apps/governed-api/tests/test_boundary_guards.py
```

> [!NOTE]
> Command presence is CONFIRMED from the prior README. Current file existence, runner behavior, dependency setup, and pass/fail status remain NEEDS VERIFICATION because tests were not run during this documentation update.

---

## CI report artifact

The prior README also named this local parity command:

```bash
make boundary-guards-ci
```

Expected report output from the prior README:

```text
artifacts/qa/policy-boundary-guards.xml
```

The artifact path is described as ignored by `.gitignore` for report consumption. This report is a QA artifact, not policy authority, not a release decision, and not evidence closure by itself.

---

## Accepted inputs

Accepted material is limited to executable policy tests, small lane-local helper notes, and minimal synthetic inline values where a separate fixture file would be excessive.

Preferred fixture inputs should be referenced from:

- `tests/fixtures/` for test-local fixtures;
- `fixtures/` for cross-cutting shared fixtures;
- `fixtures/policy/` if accepted for shared policy examples;
- domain fixture lanes when the policy condition is domain-owned.

---

## Exclusions

Do not place these materials in this lane:

| Excluded material | Correct destination |
|---|---|
| policy rules, policy bundles, or policy documentation | `policy/` |
| schema definitions | `schemas/` |
| contract definitions | `contracts/` |
| fixture payload collections | `tests/fixtures/` or `fixtures/` |
| release manifests, correction notices, rollback cards | `release/` roots |
| lifecycle data, source exports, EvidenceBundles, proofs, receipts | governed `data/` roots |
| app implementation, connectors, pipeline implementation | `apps/`, `connectors/`, `pipelines/`, or accepted package roots |
| generated CI reports | `artifacts/qa/` or CI artifact storage, not this test lane |
| secrets, private endpoints, production logs, real sensitive material, direct model output | not allowed in repository tests |

---

## Suggested layout

```text
tests/policy/
|-- README.md
|-- boundary_constants.py
|-- test_control_plane_register_meta_contract.py
|-- test_explorer_web_adapter_boundary.py
|-- test_pipeline_connector_non_publisher.py
|-- rights_unknown_denies.test.PROPOSED
|-- sensitivity_unverified_denies.test.PROPOSED
|-- review_missing_denies.test.PROPOSED
|-- stale_source_abstains.test.PROPOSED
`-- public_release_gate.test.PROPOSED
```

The three named boundary tests and `boundary_constants.py` are carried forward from the previous README. Additional `.test.PROPOSED` entries are schematic until actual filenames, runner, and framework conventions are verified.

---

## Maintenance checklist

- [ ] Preserve or update the existing boundary-suite command when test files are renamed.
- [ ] Keep policy rules in `policy/`, not `tests/policy/`.
- [ ] Keep fixtures in `tests/fixtures/` or `fixtures/`, then reference them from tests.
- [ ] Assert fail-closed behavior for unknown rights, unresolved sensitivity, missing review, stale source, missing evidence, missing release, and unsupported public display.
- [ ] Assert connectors, pipelines, adapters, and control-plane registers do not publish or bypass governed policy.
- [ ] Keep QA reports under governed artifact/report paths, not as policy authority.
- [ ] Do not store real source data, sensitive detail, production logs, public artifacts, schemas, contracts, policy rules, release records, secrets, or direct model output here.

---

## Verification status

| Item | Status |
|---|---|
| Target README path | CONFIRMED; existing README expanded. |
| Existing boundary test names | CONFIRMED from prior README content. |
| Existing local pytest command | CONFIRMED from prior README content. |
| Existing CI workflow name | CONFIRMED from prior README content; workflow file existence NEEDS VERIFICATION. |
| Existing report command and output path | CONFIRMED from prior README content; command execution NEEDS VERIFICATION. |
| `tests/` authority | CONFIRMED as canonical enforceability root. |
| `policy/` authority | CONFIRMED as canonical policy root in `policy/README.md`. |
| Executable test inventory | NEEDS VERIFICATION. |
| Policy bundle coverage | NEEDS VERIFICATION. |
| Runner and CI wiring | NEEDS VERIFICATION. |
| Tests and validators | NOT RUN. |
