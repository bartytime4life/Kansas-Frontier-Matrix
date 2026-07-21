<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/domains/archaeology/synthetic-source-descriptor/readme
title: Archaeology synthetic SourceDescriptor fixtures
type: fixture-readme
version: v0.1.0
status: draft
owners: OWNER_TBD - archaeology domain steward; source steward; fixture steward; sensitivity reviewer
created: NEEDS VERIFICATION - a blank misspelled READAME.md predated this correction
updated: 2026-07-21
policy_label: restricted-review
related:
  - ../README.md
  - ../../../../docs/domains/archaeology/MISSING_OR_PLANNED_FILES.md
  - ../../../../contracts/source/source_descriptor.md
  - ../../../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../../../docs/adr/ADR-0017-source-descriptor-admission-process.md
  - ../../../../docs/architecture/directory-rules.md
tags: [kfm, fixtures, archaeology, source-descriptor, synthetic, source-admission, fail-closed]
notes:
  - "This README replaces a one-byte misspelled file named READAME.md."
  - "The existing shpo_like.json is an inventory-created PROPOSED placeholder, not a schema-valid SourceDescriptor or an admitted source."
  - "No real archaeology record, source export, sensitive geometry, rights grant, activation decision, or release authority belongs in this lane."
[/KFM_META_BLOCK_V2] -->

# Archaeology synthetic SourceDescriptor fixtures

`fixtures/domains/archaeology/synthetic_source_descriptor/` is the intended bounded fixture lane for synthetic, public-safe archaeology examples that exercise SourceDescriptor shape and source-admission failure behavior. It is currently placeholder-only.

**Authority:** fixture support only

**Current maturity:** placeholder documentation and one inventory record

**Truth posture:** cite-or-abstain; fail closed on unresolved source identity, role, rights, sensitivity, review, or activation state

> [!IMPORTANT]
> Nothing in this directory admits or activates a source. A file here is not a source record, SourceActivationDecision, rights grant, PolicyDecision, EvidenceBundle, release approval, or publication artifact.

> [!CAUTION]
> Use synthetic metadata only. Do not include real archaeological site coordinates, burial or sacred-place details, collection-security information, living-person data, private-owner details, source credentials, or material whose redistribution rights are unclear.

## Purpose

This lane may support deterministic, no-network tests for archaeology source-descriptor behavior. Appropriate cases include:

- a synthetic descriptor that satisfies the selected canonical SourceDescriptor schema;
- invalid descriptors with missing source identity, source role, rights, sensitivity, review, or lifecycle fields;
- source-role anti-collapse cases;
- rights-unknown or exact-location-risk cases that must fail closed;
- expected error or reason-code sidecars paired with invalid fixtures.

The lane does not define SourceDescriptor meaning or machine shape. Those responsibilities remain under `contracts/` and `schemas/`.

## Placement basis

Directory Rules place deterministic valid, invalid, and golden examples under `fixtures/`, with domain-specific material under `fixtures/domains/<domain>/`. This directory therefore belongs to the `fixtures/` responsibility root and the Archaeology domain segment.

It is outside the lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Copying a fixture into a lifecycle directory would not admit, promote, or publish it. Source admission remains a governed transition.

## Current inventory

| Path | Current state | Interpretation |
|---|---|---|
| `README.md` | **CONFIRMED** | This lane boundary and maintenance contract. |
| `shpo_like.json` | **CONFIRMED file / PROPOSED placeholder** | Inventory metadata created from a planned-files document. It is not SourceDescriptor-shaped and is not a valid or admitted source record. |

At the inspected base, `shpo_like.json` contains only `status`, `source_doc`, `path`, and `notes`. The currently wired detailed SourceDescriptor schema requires 21 fields, rejects additional properties, and recognizes none of those four placeholder keys. The placeholder must therefore remain excluded from valid-fixture claims.

## Authority boundaries

| Concern | Owning path | This lane's role |
|---|---|---|
| SourceDescriptor meaning | `contracts/source/source_descriptor.md` | May illustrate; does not define. |
| SourceDescriptor machine shape | `schemas/contracts/v1/source/source_descriptor.schema.json` or an accepted successor | May be validated against the selected schema; does not choose schema authority. |
| Source admission process | `docs/adr/ADR-0017-source-descriptor-admission-process.md` and accepted governance records | May exercise failure cases; does not approve the proposed ADR or admit a source. |
| Source, rights, and sensitivity decisions | `data/registry/`, `policy/source/`, `policy/rights/`, and `policy/sensitivity/` | Synthetic inputs only; no decisions are issued here. |
| Archaeology validation | `tools/validators/` and `tests/domains/archaeology/` | Expected consumers when implemented; no consumer is established by this README. |
| Lifecycle data and release | `data/<phase>/` and `release/` | Out of scope. |

The repository currently contains conflicting SourceDescriptor schema and validator path declarations. This README does not resolve that authority drift or create another schema, contract, registry, policy, or validator home.

## Fixture admission rules

A new payload may enter this directory only when all of the following are true:

1. The payload is synthetic and contains no sensitive or restricted source material.
2. Its intended status is explicit: valid, invalid, negative, or expected output.
3. The exact schema, validator, or test consumer is named.
4. The expected result is explicit and deterministic.
5. Invalid fixtures include an expected error or reason-code sidecar when the harness supports one.
6. Rights-unknown, role-ambiguous, sensitivity-unclear, or review-missing cases fail closed.
7. The fixture cannot be mistaken for an admitted registry record or an activation decision.

## What does not belong here

- real source-system exports or provider payloads;
- actual archaeology site, survey, collection, or inventory records;
- exact or reconstructable sensitive location data;
- credentials, tokens, private endpoints, or access instructions;
- canonical SourceDescriptor contracts or JSON Schemas;
- executable policy, validator, connector, pipeline, or application code;
- source registry entries or authority-register records;
- SourceActivationDecisions, receipts, proofs, EvidenceBundles, release manifests, correction notices, or rollback cards;
- public API, map, tile, search, export, or AI-response material.

## Validation posture

| Check | Current result | Evidence boundary |
|---|---|---|
| `shpo_like.json` parses as JSON | **PASS when run for this change** | Syntax only; not SourceDescriptor validity. |
| Detailed SourceDescriptor schema shape | **FAIL by inspection** | The placeholder omits all 21 required fields; its four inventory keys are not allowed by the schema, which sets `additionalProperties` to `false`. |
| Archaeology domain validator | **NOT IMPLEMENTED at the inspected base** | `tools/validators/domains/archaeology/validate_source_descriptor.py` raises `NotImplementedError`. |
| Archaeology source-descriptor test | **NOT IMPLEMENTED at the inspected base** | `tests/domains/archaeology/test_source_descriptor.py` contains placeholder documentation only. |
| Source admission, rights, sensitivity, or activation review | **NOT RUN / NOT APPLICABLE** | This change does not propose or activate a source. |

Do not relabel `shpo_like.json` as valid merely because it parses. Replace or relocate it only in a separate evidence-backed change that identifies the canonical schema and consumer, supplies deterministic expectations, and preserves history.

## Expected future layout

Only add these paths when a real consumer is verified:

```text
synthetic_source_descriptor/
  README.md
  valid/
    <case>.json
  invalid/
    <case>.json
    <case>.expected_error.txt
```

This tree is a conditional maintenance pattern, not a claim that those child directories exist or should be created now.

## Maintenance and rollback

- Update this README and the parent Archaeology fixture index when payloads, consumers, expected outcomes, or schema authority change.
- Keep fixtures small, deterministic, no-network, and reviewable.
- Preserve source role, rights, sensitivity, review state, and lifecycle posture as separate dimensions.
- Keep human review separate from fixture generation and validation.
- If sensitive or real source material is discovered, stop using the fixture and follow the governed quarantine or private incident path.
- Roll back this documentation correction with a normal revert; do not restore the misspelled filename as a second compatibility path.

## Related repository evidence

- [`../README.md`](../README.md) - parent Archaeology fixture index.
- [`../../../../docs/domains/archaeology/MISSING_OR_PLANNED_FILES.md`](../../../../docs/domains/archaeology/MISSING_OR_PLANNED_FILES.md) - planning source that named `shpo_like.json`; planning is not implementation proof.
- [`../../../../contracts/source/source_descriptor.md`](../../../../contracts/source/source_descriptor.md) - inspected semantic contract candidate.
- [`../../../../schemas/contracts/v1/source/source_descriptor.schema.json`](../../../../schemas/contracts/v1/source/source_descriptor.schema.json) - currently wired detailed schema.
- [`../../../../docs/adr/ADR-0017-source-descriptor-admission-process.md`](../../../../docs/adr/ADR-0017-source-descriptor-admission-process.md) - proposed source-admission decision record.
- [`../../../../docs/architecture/directory-rules.md`](../../../../docs/architecture/directory-rules.md) - current contribution-preflight placement document; its canonical placement remains conflicted.

## Definition of done for this lane

This lane becomes behaviorally verified only when:

- canonical SourceDescriptor schema and validator paths are resolved;
- synthetic valid and invalid cases replace inventory-only placeholders;
- a named no-network validator or test consumes every case;
- expected failures are asserted;
- rights, sensitivity, role, review, and activation-negative cases fail closed;
- CI runs the same repository-native checks;
- human review is recorded separately from generated-work provenance.

Until then, this directory remains a documented placeholder fixture lane.
