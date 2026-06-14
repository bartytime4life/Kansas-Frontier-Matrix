<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-readme
title: Pipeline Specs Root README
type: readme
version: v0.2
status: draft
owners:
  - <pipeline-spec-steward>
  - <pipeline-owner>
  - <domain-stewards>
  - <source-steward>
  - <evidence-steward>
  - <policy-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipeline_specs/README.md
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - docs/doctrine/trust-membrane.md
  - docs/doctrine/truth-posture.md
  - docs/architecture/release-discipline.md
  - pipelines/README.md
  - pipelines/ingest/README.md
  - pipelines/normalize/README.md
  - pipelines/validate/README.md
  - pipelines/catalog/README.md
  - pipelines/triplets/README.md
  - pipelines/publish/README.md
  - pipelines/rollback/README.md
  - pipelines/watchers/README.md
  - pipelines/domains/README.md
  - data/registry/sources/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - tests/pipeline_specs/
  - fixtures/pipeline_specs/
tags: [kfm, pipeline-specs, declarative-config, pipeline-profiles, lifecycle, evidence, receipts, release-gates, governance]
notes:
  - "This README upgrades the previous short pipeline_specs root stub into a governed root contract."
  - "pipeline_specs/ is declarative pipeline configuration — the what. pipelines/ is executable logic — the how."
  - "Specs configure intent, source scope, lifecycle gates, policy/evidence/review requirements, receipt expectations, fixtures, and release-readiness checks. They do not execute pipeline logic or store lifecycle outputs."
  - "Specs are not source admission, RAW capture, validation pass, EvidenceBundle closure, catalog truth, public truth, release approval, or UI/API authority."
  - "Concrete schema validation, CI coverage, source activation, and run behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Pipeline Specs

> Canonical declarative configuration root for KFM pipeline profiles: source scopes, schedules, lifecycle gates, source-role boundaries, evidence requirements, fixtures, receipt expectations, policy/review blockers, release-readiness checks, and rollback/correction posture — separate from executable pipeline logic.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipeline__specs%2F-0a7ea4)
![authority](https://img.shields.io/badge/authority-declarative%20config-0a7ea4)
![implementation](https://img.shields.io/badge/implementation-pipelines%2F-d62728)
![release](https://img.shields.io/badge/release-governed-d62728)

**Status:** Draft  
**Path:** `pipeline_specs/README.md`  
**Responsibility root:** `pipeline_specs/` — declarative pipeline configuration, the **what**  
**Companion root:** `pipelines/` — executable pipeline logic, the **how**  
**Data root:** `data/` — lifecycle state, source registries, receipts, proofs, catalog/triplets, and published artifacts  
**Release root:** `release/` — release decisions, manifests, correction notices, and rollback cards  
**Truth posture:** spec existence does not prove implementation, activation, runtime behavior, validation, publication, or release maturity.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Root authority](#2-root-authority)
- [3. What a spec may configure](#3-what-a-spec-may-configure)
- [4. Anti-collapse rules](#4-anti-collapse-rules)
- [5. What belongs here](#5-what-belongs-here)
- [6. What does not belong here](#6-what-does-not-belong-here)
- [7. Lifecycle posture](#7-lifecycle-posture)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Domain and shared spec lanes](#10-domain-and-shared-spec-lanes)
- [11. Inputs and outputs](#11-inputs-and-outputs)
- [12. Minimal pipeline spec profile shape](#12-minimal-pipeline-spec-profile-shape)
- [13. Tests, fixtures, and validation](#13-tests-fixtures-and-validation)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`pipeline_specs/` owns declarative configuration for KFM pipelines.

A pipeline spec may define:

- profile identity, version, owner, status, and target lane;
- source descriptor references and source roles;
- schedule, cadence, freshness, and source-vintage expectations;
- lifecycle input and output states;
- policy, rights, sensitivity, review, and public-safe representation gates;
- EvidenceBundle and EvidenceRef requirements;
- receipt requirements;
- fixture expectations;
- dry-run behavior;
- release-readiness checks;
- rollback and correction posture.

A pipeline spec does **not** implement the pipeline. Executable behavior belongs under `pipelines/`.

Short rule:

```text
pipeline_specs/  = declarative pipeline configuration, the WHAT
pipelines/       = executable pipeline logic, the HOW
data/            = lifecycle state, source registries, receipts, proofs, catalog/triplets, and artifacts
release/         = release decisions, release manifests, correction notices, and rollback control
```

[⬆ Back to top](#top)

---

## 2. Root authority

| Question | Answer | Status |
|---|---|---|
| What does `pipeline_specs/` own? | Declarative profiles, scopes, schedules, source refs, gates, receipt expectations, and run contracts. | CONFIRMED root contract |
| What does `pipelines/` own? | Executable pipeline logic. | CONFIRMED companion-root contract |
| Does `pipeline_specs/` own source connectors? | No. Source access and connector logic belongs under `connectors/` or accepted connector homes. | CONFIRMED separation |
| Does `pipeline_specs/` own lifecycle data? | No. Lifecycle outputs belong under `data/`. | CONFIRMED lifecycle posture |
| Does `pipeline_specs/` own schemas, contracts, or policy? | No. These live under their responsibility roots. | CONFIRMED authority separation |
| Does `pipeline_specs/` approve release? | No. Release decisions and manifests belong under `release/`. | CONFIRMED release separation |
| Can public clients use specs directly? | No. Public clients use governed APIs and released artifacts. | CONFIRMED trust-membrane posture |

> [!IMPORTANT]
> A spec can require a gate; it cannot satisfy that gate merely by existing. Validation, evidence, review, receipts, release, correction, and rollback must remain separately auditable.

[⬆ Back to top](#top)

---

## 3. What a spec may configure

Pipeline specs may declare:

- target executable lane;
- source descriptor refs;
- admitted source family and source role expectations;
- lifecycle stage inputs and outputs;
- cadence, issue time, valid time, source vintage, and stale-source behavior;
- data-quality, geometry, topology, class-map, temporal, or support-type checks;
- domain-specific anti-collapse gates;
- sensitivity and rights gates;
- review requirements;
- expected outputs and their responsibility roots;
- required receipts and proof refs;
- release-readiness and rollback-readiness criteria;
- no-op behavior when no material change exists;
- quarantine routing when unresolved risk exists.

Specs should be deterministic, reviewable, fixture-testable, and reversible. They should avoid hidden defaults for risk-bearing behavior.

[⬆ Back to top](#top)

---

## 4. Anti-collapse rules

Disallowed collapses:

```text
pipeline spec -> executable pipeline
pipeline spec -> source admission
source list -> source authority
schedule -> freshness proof
successful spec validation -> data validation pass
watcher spec -> RAW capture
material-change report -> EvidenceBundle
catalog spec -> catalog truth
triplet spec -> graph truth
publish-readiness spec -> ReleaseManifest
release-ready flag -> release approval
rollback spec -> rollback execution
spec summary -> evidence
public profile -> public publication
```

Required separations:

- declarative specs stay in `pipeline_specs/`;
- executable code stays in `pipelines/`;
- upstream access logic stays in `connectors/` or accepted connector homes;
- source descriptors stay in `data/registry/sources/` or accepted registry homes;
- lifecycle outputs stay in `data/` lifecycle homes;
- receipts stay in receipt homes;
- EvidenceBundles stay in proof homes;
- schemas, contracts, and policy stay in their roots;
- release decisions stay in `release/`;
- public clients use governed APIs and released artifacts, not specs directly.

[⬆ Back to top](#top)

---

## 5. What belongs here

Appropriate contents include declarative specs and README contracts for:

- ingest/source-intake profiles;
- normalization profiles;
- validation profiles;
- catalog closure profiles;
- triplet/graph projection profiles;
- publish-readiness profiles;
- rollback-readiness profiles;
- watcher/source-change profiles;
- proof or dry-run profiles;
- domain-specific run profiles;
- shared profile templates;
- source-family profile variants;
- fixture-facing spec examples that do not contain lifecycle data.

A good placement test:

> If the file answers “what should run, against which source descriptors, under which gates, and with which receipts?”, it may belong in `pipeline_specs/`. If it answers “how does the pipeline run?”, it belongs in `pipelines/`.

[⬆ Back to top](#top)

---

## 6. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Executable pipeline code | `pipelines/` |
| Source access clients/connectors | `connectors/` or accepted connector home |
| Source descriptors | `data/registry/sources/` or accepted registry home |
| Runtime output | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/triplets`, `data/published` |
| Receipts emitted by execution | `data/receipts/pipeline/` or accepted receipt home |
| EvidenceBundles | `data/proofs/evidence_bundle/` |
| Object meaning | `contracts/` |
| Machine schemas | `schemas/` |
| Policy decisions | `policy/` |
| Release decisions, manifests, corrections, rollback cards | `release/` |
| Tests | `tests/pipeline_specs/` or accepted test home |
| Fixtures | `fixtures/pipeline_specs/` or accepted fixture home |
| Public API/UI code | `apps/governed-api/`, `apps/explorer-web/`, packages |
| Secrets or credentials | never in repo; use approved secret management |

[⬆ Back to top](#top)

---

## 7. Lifecycle posture

Specs may target lifecycle stages, but do not create lifecycle transitions themselves:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A spec may declare:

- accepted input state;
- intended output state;
- quarantine routing;
- promotion prerequisites;
- EvidenceBundle requirements;
- receipt requirements;
- release blockers;
- rollback target expectations;
- correction support.

Only governed pipeline execution and release authority can perform transitions.

[⬆ Back to top](#top)

---

## 8. Required gates

Every non-trivial pipeline spec should declare or explicitly mark not applicable:

1. **Profile identity gate** — stable `spec_id`, owner, lane, version, and status.
2. **Implementation gate** — target executable lane under `pipelines/`.
3. **Source gate** — source descriptor refs and source roles.
4. **Lifecycle gate** — allowed input and output lifecycle states.
5. **Evidence gate** — EvidenceRef/EvidenceBundle requirements.
6. **Receipt gate** — required run, transform, validation, review, policy, source-vintage, release-readiness, or rollback-readiness receipts.
7. **Policy gate** — rights, sensitivity, admissibility, review, and public-safe representation posture.
8. **Domain anti-collapse gate** — domain-specific proof boundaries and source-role distinctions.
9. **Fixture gate** — no-network fixture profile for validation where feasible.
10. **Release gate** — ReleaseManifest input requirements, correction path, and rollback target where output can publish.
11. **Failure gate** — fail-closed, quarantine, abstain, or no-op behavior for unresolved risk.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended root shape:

```text
pipeline_specs/
├── README.md
├── watchers/
├── agriculture/
├── air/
├── archaeology/
├── atmosphere/
├── fauna/
├── flora/
├── geology/
├── habitat/
├── hazards/
├── hydrology/
├── people-dna-land/
├── people/                         # alias / compatibility lane
├── roads-rail-trade/
├── settlement/                     # alias / compatibility lane
├── settlements-infrastructure/
└── soil/
```

Additional domain or shared spec lanes should be added only when they match a responsibility-rooted domain segment, have an implementation target, have source/fixture/test posture, and do not create a parallel authority home.

[⬆ Back to top](#top)

---

## 10. Domain and shared spec lanes

| Lane | Purpose | Notes |
|---|---|---|
| `watchers/` | Shared source-change watcher profiles. | Shared, no source admission. |
| `agriculture/` | Agriculture run profiles. | Crop/yield/field claims need source-role care. |
| `air/` | Air-quality-oriented profile alias/lane. | Keep air/atmosphere posture explicit. |
| `archaeology/` | Archaeology profiles. | Exact locations and cultural sensitivity fail closed. |
| `atmosphere/` | Weather/climate/atmospheric profiles. | Not life-safety/advisory authority. |
| `fauna/` | Fauna profiles. | Sensitive species and exact locations fail closed. |
| `flora/` | Flora profiles. | Sensitive plants and exact locations fail closed. |
| `geology/` | Geology/resource profiles. | Occurrence, deposit, reserve, permit, production, title, and extraction remain distinct. |
| `habitat/` | Habitat/context profiles. | Habitat context is not species or plant occurrence truth. |
| `hazards/` | Hazards profiles. | Not emergency alerting or life-safety instruction. |
| `hydrology/` | Hydrology profiles. | NFHL/regulatory context is not observed inundation. |
| `people-dna-land/` | People/Genealogy/DNA/Land profiles. | Living-person/DNA/title/privacy gates are strict. |
| `people/` | Alias-gated People sublane profiles. | No parallel authority. |
| `roads-rail-trade/` | Roads/Rail/Trade profiles. | Schemas/contracts use `transport/` segment. |
| `settlements-infrastructure/` | Settlements/Infrastructure profiles. | Whole-domain lane. |
| `settlement/` | Alias-gated Settlement sublane profiles. | No parallel authority. |
| `soil/` | Soil profiles. | Support-type separation is mandatory. |

[⬆ Back to top](#top)

---

## 11. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Spec file | `pipeline_specs/<lane>/` | Declarative config only. |
| Executable target | `pipelines/<lane>/` or `pipelines/domains/<domain>/` | The spec references it; it does not implement it. |
| Source descriptor | `data/registry/sources/<domain>/` | Stable source ref. |
| Fixture | `fixtures/pipeline_specs/<lane>/` or accepted fixture home | Supports no-network validation. |
| Spec validation test | `tests/pipeline_specs/<lane>/` | Verifies shape and root boundaries. |
| Runtime output | `data/` lifecycle homes | Never beside the spec. |
| Receipts | `data/receipts/pipeline/<domain-or-lane>/` | Emitted by execution, not by the spec file alone. |
| Evidence proof | `data/proofs/evidence_bundle/` | Referenced by spec; not created here. |
| Release material | `release/candidates/<domain>/`, `release/manifests/<domain>/` | Release authority owns final state. |

[⬆ Back to top](#top)

---

## 12. Minimal pipeline spec profile shape

```yaml
schema_version: kfm.pipeline_spec.v1
spec_id: <lane>.<profile>
version: 0.1.0
status: draft
owner: <pipeline-spec-steward>
implementation:
  target_pipeline: pipelines/<accepted-target>
  execution_mode: dry_run_first
applicability:
  domains: []
sources:
  source_descriptor_refs: []
lifecycle:
  input_state: WORK
  output_state: PROCESSED
requirements:
  evidence_bundle_required: true
  source_role_required: true
  policy_check_required: true
  receipts_required: []
  fixture_required: true
  release_ready: false
anti_collapse:
  spec_is_executable: false
  spec_is_source_admission: false
  spec_is_validation_pass: false
  spec_is_evidence_bundle: false
  spec_is_catalog_truth: false
  spec_is_release_approval: false
failure_posture:
  unresolved_source: quarantine
  unresolved_rights: quarantine
  unresolved_sensitivity: quarantine
  unsupported_shape: fail_closed
```

[⬆ Back to top](#top)

---

## 13. Tests, fixtures, and validation

Recommended validation coverage:

```text
tests/pipeline_specs/
├── test_spec_shape.py                  # PROPOSED
├── test_no_executable_code.py           # PROPOSED
├── test_implementation_refs.py          # PROPOSED
├── test_source_descriptor_refs.py       # PROPOSED
├── test_lifecycle_states.py             # PROPOSED
├── test_policy_and_evidence_gates.py    # PROPOSED
├── test_required_receipts.py            # PROPOSED
├── test_alias_boundaries.py             # PROPOSED
├── test_release_not_approved_by_spec.py # PROPOSED
└── test_root_boundary.py                # PROPOSED
```

A spec is not ready for execution until it has schema validation, fixture coverage, owner review, source descriptor refs, lifecycle-state assertions, policy/evidence gates, receipt requirements, and explicit release/correction/rollback posture where applicable.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- replaces the short `pipeline_specs/README.md` stub;
- identifies `pipeline_specs/` as the canonical declarative configuration root;
- preserves the `pipeline_specs/` versus `pipelines/` split;
- blocks specs from becoming executable logic, source admission, lifecycle storage, proof storage, catalog truth, release approval, or public API/UI authority;
- defines root placement, anti-collapse rules, domain/shared lanes, lifecycle posture, inputs/outputs, minimal spec shape, tests, and open questions.

Future spec files are done only when they validate, point to executable lanes, use stable source descriptors, declare lifecycle states, require receipts, preserve evidence/policy/anti-collapse posture, and document release/correction/rollback expectations.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `PIPE-SPECS-ROOT-001` | Which shared pipeline spec schema is canonical? | NEEDS VERIFICATION |
| `PIPE-SPECS-ROOT-002` | Which CI workflow validates all pipeline specs? | UNKNOWN |
| `PIPE-SPECS-ROOT-003` | Which receipt vocabulary is canonical across ingest, normalize, validate, catalog, triplets, publish-readiness, rollback, and watchers? | NEEDS VERIFICATION |
| `PIPE-SPECS-ROOT-004` | Which aliases should remain compatibility lanes versus migrate to canonical paths? | NEEDS VERIFICATION / ADR |
| `PIPE-SPECS-ROOT-005` | Should shared profile templates live directly under this root or under a dedicated `_templates/` segment? | NEEDS VERIFICATION / ADR |
| `PIPE-SPECS-ROOT-006` | Which validators should run before a spec can be used by executable pipelines? | NEEDS VERIFICATION |

---

## Maintainer note

Keep this root declarative. Do not add executable code, source clients, source descriptors, schemas, contracts, policy decisions, lifecycle outputs, receipts, EvidenceBundles, release decisions, public API code, UI code, secrets, credentials, or generated summaries here. Add those to their responsibility roots and reference them from specs by stable path or identifier.
