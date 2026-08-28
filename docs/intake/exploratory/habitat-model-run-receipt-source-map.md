<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/habitat-model-run-receipt-source-map
title: Habitat ModelRunReceipt Fixture Profile Source Map
type: intake-source-map
version: v1.0
status: proposed; fixture-only; repository-grounded
owner: OWNER_TBD
created: 2026-08-10
updated: 2026-08-10
policy_label: public
owning_root: docs/
responsibility: Map a bounded Habitat ModelRunReceipt scaffold completion to repository-resident evidence without granting model, evidence, policy, review, release, or publication authority.
truth_posture: CONFIRMED repository gap and local fixture evidence / PROPOSED contract and schema profile / NEEDS VERIFICATION human review and hosted CI
related: [contracts/domains/habitat/model_run_receipt.md, schemas/contracts/v1/domains/habitat/model_run_receipt.schema.json, contracts/evidence/analytic_output_disclosure_assessment.md, docs/doctrine/directory-rules.md, docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md]
tags: [kfm, intake, habitat, model-run, receipt, fixture, provenance, analytics]
notes: [Private research was used only for candidate discovery. Public provenance intentionally excludes private document identifiers and copied private content.]
[/KFM_META_BLOCK_V2] -->

# Habitat ModelRunReceipt fixture profile source map

## Status

This map records why the existing Habitat `ModelRunReceipt` scaffold is being
completed as a closed, fixture-only profile. It is not an adoption decision,
model runtime, EvidenceBundle, policy decision, review record, release
manifest, or publication record.

## Repository evidence

| Evidence | Confirmed observation | Bounded implementation response |
|---|---|---|
| `contracts/domains/habitat/model_run_receipt.md` | The semantic contract defines a receipt as process memory and identifies run identity, model identity, input/config closure, output inventory, source-role preservation, time, uncertainty, validation, and non-publication boundaries. | Enforce a small closed subset suitable for deterministic fixtures. |
| `schemas/contracts/v1/domains/habitat/model_run_receipt.schema.json` at the implementation base | The schema was a permissive empty-object scaffold with no required fields. | Replace only that scaffold with a closed v1 fixture profile. |
| `tools/validators/domains/habitat/validate_model_run_receipt.py` at the implementation base | The validator was a one-line placeholder. | Add deterministic shape, identity, chronology, role, inventory, and non-authority checks. |
| `contracts/evidence/analytic_output_disclosure_assessment.md` | Model and model-interpretation outputs declare a `ModelRunReceipt` dependency. | Preserve the receipt as an inspectable dependency without resolving or publishing an analytic output. |
| `docs/kfm_full_atlas_seed_cards.md` | The public repository atlas calls for model-run receipts, feature manifests, indicator definitions, validation reports, and model-output controls. | Implement only the already-declared Habitat receipt seam. |
| `docs/doctrine/directory-rules.md` and accepted ADR-0029 | Meaning, machine shape, fixtures, validator, tests, CI integration, intake mapping, and authoring provenance have separate responsibility roots. | Keep each artifact in its owning root and create no parallel authority home. |

## Adapted semantics

- `ModelRunReceipt` remains process memory, never proof or truth.
- `COMPLETED` and `FAILED` runs remain distinct and internally consistent.
- Deterministic identity binds model, inputs, effective configuration, outputs,
  timestamps, evidence references, limitations, and governance declarations.
- Completed outputs remain `MODELED` and require uncertainty and validation
  references.
- Inputs retain their declared source role and SourceDescriptor reference.
- The fixture profile carries no raw data, geometry, model weights, executable
  code, credentials, or sensitive payloads.

## Explicit non-effects

Validation does not:

- execute a model, transform, container, pipeline, or external command;
- fetch sources or resolve EvidenceRefs/EvidenceBundles;
- authenticate model cards, validation reports, reviewers, or policy records;
- activate a source, write lifecycle state, create catalog/proof objects, or
  assemble a release;
- authorize a map, API, UI, AI answer, export, deployment, or publication.

## Deferred work

- Accepted cross-domain versus Habitat-specific receipt hierarchy.
- Real receipt emission and durable instance storage.
- Model-card, evidence, policy, review, release, correction, and rollback
  resolvers.
- Sensitive-input redaction and public receipt projection.
- Runtime, pipeline, API, UI, graph, or public-map consumption.

Those changes require separate dependency-closed review and are not implied by
a passing fixture workflow.
