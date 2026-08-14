<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://adr/ADR-0031
title: "ADR-0031 — Shared Watcher Ownership and Placement"
type: adr
adr_id: ADR-0031
version: v1.1
status: proposed
effective_decision_status: proposed
owners:
  - "OWNER_TBD — architecture decision owner"
  - "OWNER_TBD — pipeline and watcher steward"
  - "OWNER_TBD — source and evidence steward"
  - "OWNER_TBD — affected domain stewards"
owner_status: "CODEOWNERS routes docs/adr/ and the affected implementation and governance roots to @bartytime4life; accepted stewardship, decision quorum, independent review, source-activation authority, and release authority remain unverified"
reviewers_required:
  - Architecture steward
  - Docs steward
  - Pipeline and watcher steward
  - Pipeline-spec steward
  - Source and evidence steward
  - Affected domain steward
  - Contract and schema steward
  - Policy and sensitivity reviewer
  - Validation steward
  - Release and rollback steward
created: 2026-08-08
updated: 2026-08-14
policy_label: public
truth_posture: cite-or-abstain
responsibility_root: docs/
owning_root: docs/
responsibility: "Records the proposed ownership split for watcher registries, declarative specs, shared executable orchestration, domain watcher behavior, connectors, helpers, candidate outputs, migration, and rollback without granting source activation, execution, lifecycle-write, release, deployment, notification, publication, or settings authority."
current_path: docs/adr/ADR-0031-shared-watcher-ownership-and-placement.md
supersedes: []
superseded_by: []
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: b7352aba93f7298bdd5a6ee6fd8de475b05c9e42
  target_prior_blob: 8cffe2917e9d9646ef1ddd62d5cdda3331b50ac0
  adr_index_blob: 938c5894c36b99e14810918e2c550ab0e92d53b1
  adr_readme_blob: 793015c38f4066c2c23753d4e3dd26bcc890279d
  adr_0029_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  shared_watcher_readme_blob: 42680e55b6e736f7f447f17cec7e5f71e8f67c08
  flora_watcher_readme_blob: ca41b4fc94582eae81fba4b91f397cf9c63004c7
  tools_watchers_readme_blob: 9711995283cbccd80b89189c08002088c28d9b07
  shared_plants_placeholder_blob: fa8ab22f84d2ac41a3a49b9633509c196d989925
  flora_plants_placeholder_blob: efc75e02896e99451fbd103d4a858c55c83784c1
  watcher_gate_profile_blob: fcb4fa6313428b36223b94e2b003dc6ad2430b04
  soil_watcher_spec_blob: e592a06765ce9f2a61aef50ae8f20b2f5d9d6209
  watcher_registry_contract_blob: 8e92b67a47161689f54952a14745c1efd443e540
  watcher_registry_schema_blob: 9f144b42be72917fd16c127fcec35b3900453706
  watcher_registry_projection_blob: 03eaa309c5aac01f7755e7f1df4f04073bf1ad0f
  watcher_registry_validator_blob: 448a5bc5631e91bb3f6ddfda30f09d62c8b2c164
  watcher_registry_tests_blob: 19a5d9d6654f48a5c7963c59e914858d08574fc1
  watcher_registry_workflow_blob: 2da9c6b343b45b2bee33c559dd5fab84a7ba7eb4
  watcher_registry_extension_receipt_blob: 09cba6e791b634b735e2d603bf37250a19d2939b
  last_green_watcher_registry_run: 31263074530
  latest_watcher_registry_run: 31654972163
related:
  - docs/adr/README.md
  - docs/adr/INDEX.md
  - docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - docs/adr/ADR-0012-connector-outputs-to-data-raw-or-data-quarantine-only.md
  - docs/adr/ADR-0017-source-descriptor-admission-process.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/doctrine/directory-rules.md
  - pipelines/watchers/README.md
  - pipelines/domains/flora/watchers/README.md
  - pipeline_specs/watchers/README.md
  - pipeline_specs/watchers/plants_drift.yaml
  - pipeline_specs/watchers/soil_ssurgo_gnatsgo.json
  - pipeline_specs/watchers/watcher_gate_profile.v1.json
  - pipeline_specs/flora/plants_drift_watcher.yaml
  - tools/watchers/README.md
  - contracts/source/watcher_registry.md
  - contracts/domains/soil/soil_watcher_spec.md
  - schemas/contracts/v1/source/watcher_registry.schema.json
  - schemas/contracts/v1/domains/soil/soil_watcher_spec.schema.json
  - control_plane/watcher_registry.json
  - policy/domains/soil/watcher_spec.rego
  - tools/validators/validate_watcher_registry.py
  - tools/validators/domains/soil/watcher_spec/validate_soil_watcher_spec.py
  - tests/validators/test_validate_watcher_registry.py
  - tests/validators/domains/soil/watcher_spec/test_validate_soil_watcher_spec.py
  - .github/workflows/watcher-registry.yml
  - .github/workflows/soil-watcher-spec.yml
  - .github/workflows/policy-boundary-guards.yml
  - data/receipts/generated/genrec-watcher-registry-soil-extension-20260808.json
  - docs/registers/DRIFT_REGISTER.md
  - docs/registers/VERIFICATION_BACKLOG.md
tags: [adr, kfm, pipelines, watchers, watcher-registry, source-change, material-change, governance, non-publisher, fixture-first, placement]
notes:
  - "v1.1 is a same-path documentation-only reconciliation. It preserves proposed status and does not accept ADR-0031 or authorize migration."
  - "ADR-0029 separately accepted the exact Directory Rules v2 bytes; that confirms this ADR lane but does not accept this decision."
  - "A fixture-first WatcherRegistry packet and an inactive Soil watcher extension now exist; neither creates execution or publication authority."
  - "No executable shared watcher runtime is present under pipelines/watchers/ at the evidence checkpoint."
  - "The Soil spec is domain-specific by contract, policy, sources, and outputs but currently sits in the shared watcher-spec lane; migration remains HOLD."
  - "The latest observed watcher-registry run passed focused logic and fixture checks, then failed generated-receipt validation with ARTIFACT_DIGEST_MISMATCH."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ADR-0031 — Shared Watcher Ownership and Placement

> **Proposed decision.** KFM separates watcher responsibilities by ownership: `control_plane/` indexes watcher identities and non-authority state; `pipeline_specs/` declares intent; `pipelines/` owns executable orchestration; domain lanes own domain meaning; `connectors/` own approved upstream access; and `tools/` owns bounded helpers and validators. Shared executable placement requires proven reuse. Watchers remain candidate producers and non-publishers.

[![Decision: proposed](https://img.shields.io/badge/decision-proposed-d4a72c?style=flat-square)](#status)
[![Registry: partial](https://img.shields.io/badge/registry-PARTIAL-0969da?style=flat-square)](#current-repository-evidence)
[![Shared runtime: absent](https://img.shields.io/badge/shared%20runtime-ABSENT-6e7781?style=flat-square)](#current-repository-evidence)
[![Receipt closure: hold](https://img.shields.io/badge/receipt%20closure-HOLD-b42318?style=flat-square)](#hosted-workflow-evidence)
[![Publication: none](https://img.shields.io/badge/publication-none-6e7781?style=flat-square)](#watcher-non-authority-law)

> [!IMPORTANT]
> **Decision status, placement authority, registry implementation, and watcher execution are separate facts.** The ADR index keeps this record `proposed`. ADR-0029 separately accepted Directory Rules v2. The repository has a bounded watcher registry and inactive Soil specification, but neither accepts this ADR, establishes a shared runtime, activates a source, or grants lifecycle, release, notification, or publication authority.

> [!CAUTION]
> **Current placement is not fully aligned with the proposed decision.** `pipeline_specs/watchers/soil_ssurgo_gnatsgo.json` is Soil-specific through its contract, policy, source families, and outputs. Its shared-lane path is therefore migration evidence, not authority to move it in this docs-only update.

> [!NOTE]
> Watcher-registry run `31654972163` passed all five focused tests, current registry validation, and four fixture-polarity cases, then failed generated-receipt validation with `ARTIFACT_DIGEST_MISMATCH`. The last observed green run remains `31263074530`. Current classification: **logic PASS / receipt HOLD**.

**Quick navigation:** [Status](#status) · [Evidence](#evidence-boundary) · [Repository evidence](#current-repository-evidence) · [Decision](#decision) · [Admission](#shared-orchestration-admission-test) · [Non-authority](#watcher-non-authority-law) · [Graduation](#graduation-gates) · [Migration](#migration-plan) · [Validation](#validation-plan) · [Risks](#risk-ledger) · [Open work](#open-questions) · [References](#references) · [No-loss](#no-loss-reconciliation)

---

<a id="status"></a>

## Status

| Field | Current value |
|---|---|
| ADR