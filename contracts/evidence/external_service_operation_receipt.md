<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/external-service-operation-receipt
title: ExternalServiceOperationReceiptCandidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Evidence steward · Workflow steward · Source steward · Validation steward
created: 2026-08-11
updated: 2026-08-11
owning_root: contracts/
policy_label: internal; evidence; provenance; external-service; cost; reproducibility
responsibility: Define a fixture-only process-memory candidate that records one external-service operation, provider dependency, service version, declared consumption, cost caveat, and replay posture without executing the operation or creating evidence, policy, review, release, deployment, or publication authority.
truth_posture: "CONFIRMED supplied-card traceability and bounded repository gap; PROPOSED inactive contract; UNKNOWN consumer adoption and provider equivalence; NEEDS VERIFICATION human review and hosted exact-head CI"
related:
  - ./analytic_output_disclosure_assessment.md
  - ../governance/query_run_record.md
  - ../source/source_interface_evolution_assessment.md
  - ../../schemas/contracts/v1/evidence/external_service_operation_receipt.schema.json
  - ../../fixtures/contracts/v1/evidence/external_service_operation_receipt/cases.json
  - ../../tools/validators/evidence/validate_external_service_operation_receipt.py
  - ../../tests/validators/evidence/test_validate_external_service_operation_receipt.py
  - ../../docs/intake/exploratory/pass-18-external-service-operation-receipt-source-map.md
tags: [kfm, evidence, provenance, external-service, credits, cost, replay, fixture-only, no-network]
notes:
  - "Implements the smallest dependency-closed portion of supplied Pass 18 card KFM-P18-INV-419."
  - "A PASS proves bounded declaration coherence only; it does not authenticate provider use, service behavior, consumption, pricing, billing, evidence, review, release, or publication."
[/KFM_META_BLOCK_V2] -->

# ExternalServiceOperationReceiptCandidate

ExternalServiceOperationReceiptCandidate is a bounded, fixture-only process-memory declaration for one workflow step that depends on a hosted or credit-consuming external GIS service. It makes the provider dependency, service version, declared consumption, cost caveat, and replay posture visible without calling the provider or carrying credentials, request payloads, response payloads, source rows, or billing records.

The candidate implements the narrow requirement in supplied Pass 18 card KFM-P18-INV-419: external GIS operations should record cost, dependency, and reproducibility caveats because otherwise a valid hosted analysis may be impossible to reproduce without the same platform access, credentials, credits, or service version.

## Boundary

A validator PASS proves only that:

- the closed candidate shape, profile hash, and receipt identity replay;
- the platform, operation specification, input snapshot, output artifact, and service version are explicitly declared;
- measured, estimated, not-charged, and unresolved consumption states do not contradict their references or amount fields;
- cost minor units and currency remain paired;
- replay posture has a bounded policy reference or explicitly abstains;
- dependency and replay limitations are visible;
- a public-support candidate carries a cost caveat plus evidence and review references; and
- every authority claim remains false.

The validator does not execute an operation, contact a provider, inspect an input or output, authenticate a usage measurement, verify a price, convert currency, prove numerical equivalence, resolve evidence, decide policy or review, promote, release, deploy, publish, or authorize public use.

## Consumption states

| State | Required declaration | Meaning |
|---|---|---|
| MEASURED | At least one credit or cost value and a measurement reference | The candidate records a usage claim; it does not authenticate it. |
| ESTIMATED | At least one credit or cost value and a pricing reference | The candidate records an estimate; it does not guarantee a bill or future price. |
| NOT_CHARGED | No credit, cost, currency, measurement, or pricing fields | No charge is declared for this operation candidate. |
| UNRESOLVED | No consumption values or references | Validation ABSTAINS until consumption posture is declared. |

Credit quantity is a bounded canonical decimal string. Monetary cost is represented only as non-negative minor units paired with a three-letter currency code. Neither field is a financial record or proof of payment.

## Replay and disclosure

Replay posture is one of EXACT_PROVIDER, GOVERNED_REPLACEMENT, REFERENCE_ONLY, or UNRESOLVED. Every resolved posture carries an opaque replay-policy reference and canonically ordered limitations. A governed replacement cannot simultaneously claim that the operation is vendor locked.

An external_service_cost_caveat is required whenever consumption is measured, estimated, or unresolved. Public-claim support additionally requires opaque EvidenceBundle and review-record references. The release-manifest field is fixed to null, and all release, deployment, publication, and public-use authority remains false.

## Finite validator outcomes

| Outcome | Meaning |
|---|---|
| PASS | Identity, operation, consumption, dependency, replay, disclosure, and no-authority declarations are locally coherent. |
| ABSTAIN | The operation, a required reference, service version, consumption posture, or replay policy remains explicitly unresolved. |
| DENY | Consumption, cost/currency, replay, disclosure, ordering, deterministic identity, or authority declarations are contradictory. |
| ERROR | The candidate cannot be parsed or evaluated safely, or declares operation error. |

These outcomes are validation results only. They are not provider, billing, evidence, policy, review, release, deployment, or publication decisions.

## Directory Rules basis

The object is process memory for an evidence-affecting external workflow step, so semantic meaning belongs under contracts/evidence/. Machine shape, synthetic replay, repository validation, executable conformance evidence, CI orchestration, source reconciliation, and authoring accountability remain under schemas/, fixtures/, tools/, tests/, .github/workflows/, docs/intake/exploratory/, and data/receipts/generated/ respectively.

No provider adapter, billing store, credential store, source registry, workflow engine, evidence store, policy lane, release record, deployment path, public API, or new root is created.

## Validation

    python -m unittest tests.validators.evidence.test_validate_external_service_operation_receipt -v
    python tools/validators/evidence/validate_external_service_operation_receipt.py --fixtures

## Rollback

Revert the additive packet. It has no runtime consumer and mutates no provider account, credential, source, input, output, evidence, policy, lifecycle record, review, release, deployment, or public artifact.
