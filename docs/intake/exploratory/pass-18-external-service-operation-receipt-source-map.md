<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-18-external-service-operation-receipt-source-map
title: Pass 18 External-Service Operation Receipt Source Map
type: source-map
version: v1.0.0
status: exploratory; implementation-mapped; non-authoritative
owners: OWNER_TBD — Intake steward · Evidence steward · Workflow steward · Source steward
created: 2026-08-11
updated: 2026-08-11
owning_root: docs/
policy_label: internal; exploratory; source-reconciliation; external-service; cost; reproducibility
responsibility: Reconcile one supplied external-service cost and reproducibility idea with current repository evidence while withholding private discovery-source identifiers from public provenance.
truth_posture: "CONFIRMED supplied-card, current-main inspection, and bounded gap; PROPOSED inactive implementation profile; UNKNOWN provider equivalence and consumer adoption; NEEDS VERIFICATION human review and hosted exact-head CI"
related:
  - ../../../contracts/evidence/external_service_operation_receipt.md
  - ../../../contracts/evidence/analytic_output_disclosure_assessment.md
  - ../../../contracts/governance/query_run_record.md
  - ../../../contracts/source/source_interface_evolution_assessment.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, intake, pass-18, external-service, credits, cost, replay]
[/KFM_META_BLOCK_V2] -->

# Pass 18 External-Service Operation Receipt Source Map

This map records source adaptation only; it creates no provider or cost authority.

## Source and gap

| Evidence | Observation | Status |
|---|---|---|
| Supplied and connected-Drive Pass 18 card KFM-P18-INV-419 | Workflows using hosted or credit-consuming external GIS operations should record cost, provider dependency, service version, and reproducibility caveats. | CONFIRMED source statement |
| contracts/evidence/analytic_output_disclosure_assessment.md | The existing profile discloses analytic-output role and limitations, not provider usage, credit consumption, pricing posture, or replay dependency. | CONFIRMED adjacent contract |
| contracts/governance/query_run_record.md | The existing record binds one governed query iteration and evidence-resolution projection, but carries no external-service usage or cost declaration. | CONFIRMED adjacent contract |
| contracts/source/source_interface_evolution_assessment.md | The existing assessment records upstream interface evolution, not the consumption and replay posture of one completed workflow operation. | CONFIRMED adjacent contract |
| Starting main@aaf508425818749d5c5d2b9f1cf5808f018d2535 search | No exact card ID, external-service operation cost receipt packet, matching branch, or matching pull request was found before implementation. | CONFIRMED bounded gap |
| Connected private research corpus | Used for candidate discovery and corroboration only. Private file identifiers, URLs, and copied prose are intentionally excluded. | CONFIRMED provenance boundary |

## Adaptation

The implementation is a closed synthetic receipt candidate under the existing evidence family. It records a digest-bound platform descriptor, service version, operation specification, input snapshot, output artifact, measured or estimated consumption, dependency caveat, replay posture, and public-facing cost caveat.

The source card names an external platform descriptor, cost or credit receipt, service version, and replay policy as dependencies. This packet represents each only by bounded metadata or an opaque reference. It does not create a provider adapter, authenticate billing, retain credentials, execute a hosted operation, or claim that a governed replacement is numerically equivalent.

## Directory Rules basis

The packet uses established responsibility roots: semantic meaning in contracts/evidence/, shape in schemas/contracts/v1/evidence/, synthetic replay in fixtures/contracts/v1/evidence/, repository validation in tools/validators/evidence/, conformance evidence in tests/validators/evidence/, orchestration in .github/workflows/, source reconciliation in docs/intake/exploratory/, and authoring accountability in data/receipts/generated/.

No credential root, billing root, provider root, source registry, workflow engine, evidence authority, policy authority, release path, deployment surface, or public route is introduced.

## Non-effects and rollback

A local PASS authenticates no operation, platform, version, input, output, consumption, price, bill, replay equivalence, evidence, policy, review, release, deployment, publication, or public-use state. Rollback is one additive revert with no provider or external-state cleanup.
