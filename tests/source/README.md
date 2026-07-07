<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-source-readme
title: Source Tests README
type: test-readme
version: v0.1
status: draft; blank-placeholder-replaced; source-test-lane; PROPOSED / NEEDS VERIFICATION
owners:
  - OWNER_TBD - Test steward
  - OWNER_TBD - Source steward
  - OWNER_TBD - Registry steward
  - OWNER_TBD - Policy steward
  - OWNER_TBD - Evidence steward
created: 2026-07-07
updated: 2026-07-07
policy_label: public-doc; tests; source; source-admission; source-role; rights; sensitivity; no-network; synthetic-only; fail-closed; evidence-aware; policy-aware
tags: [kfm, tests, source, source-admission, SourceDescriptor, source-role, rights, sensitivity, cadence, citation, source-registry, anti-collapse, fail-closed, ABSTAIN, DENY, ERROR]
related:
  - ../README.md
  - ../fixtures/README.md
  - ../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../docs/sources/ADMISSION_PROCESS.md
  - ../../docs/sources/README.md
  - ../../contracts/source/README.md
  - ../../contracts/source/SOURCE_DESCRIPTOR.md
  - ../../schemas/contracts/v1/source/
  - ../../policy/source/
  - ../../policy/rights/
  - ../../policy/sensitivity/
  - ../../data/registry/sources/
  - ../../packages/source-registry/README.md
  - ../../tools/validators/
notes:
  - "This README replaces blank placeholder content at tests/source/README.md."
  - "This lane documents executable source-admission and source-role tests. It is not a source registry, SourceDescriptor store, source contract home, schema home, policy home, connector implementation, lifecycle data root, proof store, or release authority."
  - "The root tests/README.md does not currently list tests/source/ in its proposed directory tree; this path is therefore treated as a repo-confirmed placeholder and PROPOSED / NEEDS VERIFICATION lane unless maintainers adopt tests/source/ or redirect it to tests/contracts/source/, tests/schemas/source/, tests/policy/source/, or tests/domains/<domain>/source/."
  - "Executable test inventory, actual runner/framework, fixture consumption, schema bindings, policy/runtime wiring, CI jobs, and pass rates remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Source tests

> Test-lane README for source-admission, source-role, rights, sensitivity, cadence, access, citation, and anti-collapse checks under `tests/source/`. This lane proves source-governance behavior without becoming source authority, source data, registry state, policy, schema, contract, connector code, or release approval.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Lane: source tests" src="https://img.shields.io/badge/lane-source__tests-purple">
  <img alt="Posture: fail closed" src="https://img.shields.io/badge/posture-fail__closed-critical">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
</p>

**Path:** `tests/source/README.md`  
**Status:** draft / blank placeholder replaced / source test lane / PROPOSED until placement and executable tests are verified  
**Owning root:** `tests/`  
**Lane family:** `source`  
**Source authority roots:** `data/registry/sources/`, source authority registers, and accepted source registry homes  
**Default posture:** deterministic, synthetic, no-network, fail-closed source tests only  
**Truth posture:** CONFIRMED target file existed as blank placeholder content before replacement; CONFIRMED `tests/` is the canonical enforceability root; CONFIRMED root test doctrine begins the trust spine with source admission; CONFIRMED source descriptor doctrine fixes role, rights, sensitivity, cadence, access, and citation posture at admission; NEEDS VERIFICATION for accepted placement of `tests/source/`, executable test inventory, fixtures, schema bindings, policy wiring, CI coverage, and pass rates.

---

## Scope

Use `tests/source/` for tests that verify source-admission and source-role guardrails.

In scope:

- `SourceDescriptor` admission precondition tests;
- source-role anti-collapse tests;
- rights, terms, sovereignty, sensitivity, access, cadence, freshness, and citation posture tests;
- source registry lookup and source authority register behavior tests using synthetic inputs;
- negative tests for unknown rights, stale terms, unresolved sensitivity, missing citation template, candidate misuse, synthetic reality-boundary gaps, and role-upgrade attempts;
- tests proving connectors, watchers, loaders, pipelines, API/UI surfaces, and AI adapters cannot use a source outside its admitted role or access posture.

Out of scope:

- source registry records or source descriptors as data;
- source contract definitions;
- source schema definitions;
- source policy rules;
- connector, watcher, loader, or source-registry implementation code;
- lifecycle source data, live credentials, source exports, EvidenceBundles, receipts, proofs, release records, public artifacts, or generated model output.

[Back to top](#top)

---

## Repo fit

| Responsibility | Correct home | Relationship |
|---|---|---|
| Source-admission and source-role tests | `tests/source/` | This PROPOSED lane; placement NEEDS VERIFICATION. |
| General source-descriptor contract tests | `tests/contracts/source/` if adopted | May own contract-semantics tests. |
| Source schema tests | `tests/schemas/` or accepted schema-test lane | Shape checks; not this README unless source-specific. |
| Source policy tests | `tests/policy/` or source policy test sublane | Allow/deny/restrict/abstain checks; not source authority. |
| Domain-specific source tests | `tests/domains/<domain>/` | Prefer when domain owns the source behavior. |
| Source descriptor meaning | `contracts/source/` | Semantic contract authority. |
| Source descriptor shape | `schemas/contracts/v1/source/` or accepted schema home | Machine-shape authority. |
| Source policy | `policy/source/`, `policy/rights/`, `policy/sensitivity/` | Admissibility authority. |
| Source registry records | `data/registry/sources/` and accepted registry homes | Registry authority; not owned here. |
| Source helpers | `packages/source-registry/`, connectors, watchers, pipelines | Implementation under test; not owned here. |
| Receipts, proofs, release | `data/receipts/`, `data/proofs/`, `release/` | Audit and publication authority. |

> [!IMPORTANT]
> `tests/source/` must not become a source registry, source descriptor store, source data lane, connector implementation, schema home, contract home, policy home, fixture archive, proof/receipt store, release store, public artifact root, or direct model-output surface.

---

## Placement note

`tests/README.md` names source admission as the first gate in the trust spine, but the proposed directory tree shown there does not currently list `tests/source/`. Because this requested path exists in the repository as a blank placeholder, this README treats it as a repo-confirmed placeholder and PROPOSED test lane.

If maintainers decide source tests should live elsewhere, this README should become a compatibility pointer to one or more accepted homes:

```text
tests/contracts/source/        # source semantic-contract tests
tests/schemas/                 # source schema shape tests
tests/policy/                  # source rights/sensitivity/admission policy tests
tests/domains/<domain>/        # domain-owned source behavior
tests/source/                  # accepted source test lane, if retained
```

---

## Source-test rule

Source tests prove that source material cannot enter or move through KFM without explicit admitted role, rights, sensitivity, cadence, access, and citation posture.

Core expectations:

| Expectation | Required posture |
|---|---|
| Admission first | Source identity, role, rights, sensitivity, cadence, access, and citation posture are checked before downstream use. |
| Role fixed at admission | Promotion never upgrades `modeled` to `observed`, `aggregate` to per-place truth, `candidate` to verified, or `synthetic` to observed reality. |
| Rights fail closed | Unknown, stale, restricted, or unresolved rights block public derivatives. |
| Sensitivity fail closed | Unresolved or denied sensitivity blocks public exposure or requires transform/review. |
| Citation required | Public downstream use requires citation template and role qualifier where material. |
| No-network default | Default tests use synthetic fixtures and do not call live sources, APIs, vendors, tiles, or model services. |
| Source is not truth alone | Passing source admission does not prove a claim, evidence closure, policy approval, release, or publication. |

---

## Expected test families

| Family | What it proves | Expected outcome |
|---|---|---|
| `source_descriptor_required_fields` | Required identity, role, steward, domain, rights, sensitivity, cadence, access, and citation fields are present. | `PASS` / validation failure. |
| `source_role_anti_collapse` | Source role cannot be silently upgraded or reframed downstream. | validation failure / `DENY`. |
| `candidate_not_published` | Candidate sources cannot back public `PUBLISHED` output without governed promotion. | `DENY`. |
| `synthetic_requires_boundary_note` | Synthetic source lacks reality-boundary note or basis. | validation failure / `DENY`. |
| `unknown_rights_fail_closed` | Unknown or stale rights prevent public derivative use. | `DENY` / `ABSTAIN`. |
| `sensitivity_unresolved_denies` | Missing sensitivity tier/classes/review/transform blocks public surface. | `DENY`. |
| `cadence_stale_marks_or_abstains` | Stale source support is surfaced as stale or causes abstention. | `ABSTAIN` / validation failure. |
| `citation_template_required` | Downstream public use cannot proceed without citation and role qualifier. | validation failure / `ABSTAIN`. |
| `connector_non_publisher` | Connector/watcher/source loader can propose or admit but not publish. | `PASS` / `DENY`. |
| `ai_cannot_infer_source_role` | AI/runtime output cannot mint or upgrade source authority. | validation failure / `ABSTAIN`. |

---

## Accepted inputs

Accepted material is limited to executable source tests, lane-local notes, and tiny synthetic inline values when they are too small to justify fixture files.

Preferred input sources:

- `tests/fixtures/` for unit-test-scoped source fixtures;
- `fixtures/` and `fixtures/contracts/v1/source/` for shared valid/invalid source examples;
- `docs/sources/SOURCE_DESCRIPTOR_STANDARD.md` for source descriptor doctrine;
- `contracts/source/` for source semantic meaning;
- `schemas/contracts/v1/source/` for source descriptor shape;
- `policy/source/`, `policy/rights/`, and `policy/sensitivity/` for admissibility checks;
- `data/registry/sources/` only through synthetic/test-safe refs, not live records.

---

## Exclusions

Do not place these materials in this lane:

| Excluded material | Correct destination |
|---|---|
| source descriptor records or source registry entries | `data/registry/sources/` or accepted registry homes |
| source contract prose | `contracts/source/` |
| source schema definitions | `schemas/contracts/v1/source/` |
| source, rights, or sensitivity policy rules | `policy/source/`, `policy/rights/`, `policy/sensitivity/` |
| fixture payload collections | `tests/fixtures/` or `fixtures/` |
| connector, watcher, loader, package, API, or pipeline implementation | accepted implementation roots such as connectors, watchers, packages, apps, or pipelines |
| lifecycle data, source exports, EvidenceBundles, receipts, proofs, release records | governed `data/` and `release/` roots |
| live credentials, production logs, public artifacts, dashboards, screenshots, secrets, direct model output | not allowed in source tests |

---

## Suggested layout

```text
tests/source/
|-- README.md
|-- source_descriptor_required_fields.test.PROPOSED
|-- source_role_anti_collapse.test.PROPOSED
|-- candidate_not_published.test.PROPOSED
|-- synthetic_requires_boundary_note.test.PROPOSED
|-- unknown_rights_fail_closed.test.PROPOSED
|-- sensitivity_unresolved_denies.test.PROPOSED
|-- cadence_stale_marks_or_abstains.test.PROPOSED
|-- citation_template_required.test.PROPOSED
|-- connector_non_publisher.test.PROPOSED
`-- ai_cannot_infer_source_role.test.PROPOSED
```

The layout is schematic. Actual test filenames, extensions, package manager, runner, and framework remain NEEDS VERIFICATION.

---

## Run posture

No executable runner was verified while authoring this README.

```bash
: "PROPOSED / NEEDS VERIFICATION"
pytest tests/source
```

Default runs should be deterministic, local, no-network, public-safe, and finite-outcome only. Replace the command once the repo's actual test runner and naming convention are verified.

---

## Maintenance checklist

- [ ] Confirm whether `tests/source/` is the accepted source test lane or a compatibility pointer.
- [ ] Keep source registry records in `data/registry/sources/`, not this test lane.
- [ ] Keep source schemas, contracts, policies, fixtures, implementation, receipts, proofs, and releases in their owning roots.
- [ ] Assert source role, rights, sensitivity, cadence, access, citation, and anti-collapse behavior before downstream use.
- [ ] Assert candidate, synthetic, modeled, aggregate, regulatory, administrative, and observed roles remain distinct.
- [ ] Assert unknown rights, unresolved sensitivity, stale terms, and missing citations fail closed.
- [ ] Assert connectors, watchers, loaders, pipelines, API/UI, and AI do not publish or infer authority from source convenience fields.
- [ ] Link tests to fixtures, source standards, contracts, schemas, policies, registries, and validators after verification.

---

## Verification status

| Item | Status |
|---|---|
| Target README path | CONFIRMED; blank placeholder replaced. |
| `tests/` authority | CONFIRMED as canonical enforceability root. |
| Source admission in trust spine | CONFIRMED in `tests/README.md`. |
| SourceDescriptor doctrine | CONFIRMED in source descriptor standard. |
| Source contract boundary | CONFIRMED in `contracts/source/README.md`. |
| `tests/source/` placement | NEEDS VERIFICATION; not listed in the proposed `tests/README.md` directory tree. |
| Executable test inventory | NEEDS VERIFICATION. |
| Fixture payload inventory | NEEDS VERIFICATION. |
| Actual runner/framework | NEEDS VERIFICATION. |
| Schema and policy bindings | NEEDS VERIFICATION. |
| CI wiring and pass rates | NEEDS VERIFICATION. |
| Tests and validators | NOT RUN. |
