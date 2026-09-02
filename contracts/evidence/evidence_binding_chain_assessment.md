<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/evidence-binding-chain-assessment
title: Evidence Binding Chain Assessment Contract
type: semantic-contract
version: v0.1.0
status: proposed; inactive; synthetic-fixture-only; no-evidence-closure-or-release-authority
owners: OWNER_TBD — Evidence steward · Source steward · Contracts steward · Schema steward · Validation steward
created: 2026-08-11
updated: 2026-08-11
policy_label: internal; evidence; reference-closure; fail-closed; non-authoritative
owning_root: contracts/
responsibility: Define a bounded synthetic assessment of reference closure from one immutable SourceArtifact through ParseResult and EvidenceRef to one ClaimFieldBinding without creating EvidenceBundle, policy, release, or publication authority.
truth_posture: proposed; cite-or-abstain
related:
  - ../source/source_artifact.md
  - ../source/source_adapter.md
  - ./evidence_ref.md
  - ./claim_field_binding.md
  - ../../schemas/contracts/v1/evidence/evidence_binding_chain_assessment.schema.json
  - ../../fixtures/contracts/v1/evidence/evidence_binding_chain_assessment/
  - ../../tools/validators/validate_evidence_binding_chain_assessment.py
  - ../../tests/validators/test_validate_evidence_binding_chain_assessment.py
  - ../../docs/intake/exploratory/briefing-evidence-binding-chain-source-map.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, evidence, source-artifact, parse-result, evidence-ref, claim-field-binding, reference-closure, fixture-first]
notes:
  - "Implements the first next sourced idea in briefing-claim-field-binding-source-map.md."
  - "PASS means only synthetic reference closure; EvidenceBundle and every authority-bearing gate remain absent."
[/KFM_META_BLOCK_V2] -->

# Evidence Binding Chain Assessment

`EvidenceBindingChainAssessment` is an inactive, synthetic conformance profile for one narrow question:

> Can one field binding be traced without ambiguity to one EvidenceRef, one parsed record, one executable `ParseResult`, and one immutable `SourceArtifact`?

The assessment embeds existing SourceArtifact, EvidenceRef, and ClaimFieldBinding schema shapes, plus the source-adapter `ParseResult` field surface. It adds only the reference links necessary to test the chain. It does not resolve claim-scope evidence, create an `EvidenceBundle`, evaluate policy, or authorize release.

## Chain

```text
SourceArtifact
  -> ParseResult.source_artifact_ref
  -> ParseResult.records[].record_ref
  -> EvidenceRef + EvidenceResolution
  -> ClaimFieldBinding.evidence_ref
  -> ClaimFieldBinding.source_artifact_ref + native locator + value digest
```

`EvidenceResolution` is assessment-local linkage, not a new evidence object family or resolver authority. It says which synthetic parsed record a pre-closure EvidenceRef points to for this test.

## Required closure

1. The SourceArtifact has a non-placeholder byte digest, derived artifact identity and content-addressed storage reference, `FETCHED` outcome, and all-false governance effects.
2. The ParseResult references that exact artifact and repeats the artifact's parser identity, version, and spec digest.
3. The ParseResult is accepted by the executable source-adapter value object and has outcome `PARSED` with canonically ordered, unique record references.
4. The EvidenceRef has kind `record`, carries no `bundle_ref`, and has an identity derived from its assessment-local resolution subject.
5. The resolution references one exact parsed record, its digest and native locator, and the same SourceArtifact and ParseResult.
6. The ClaimFieldBinding passes its existing validator and references the same SourceArtifact, EvidenceRef, native locator, and supported native-value digest.
7. With transform kind `NONE`, native and normalized value digests are equal. A non-trivial transform requires the existing transform reference, receipt reference, and deterministic posture.
8. The assessment and nested ClaimFieldBinding identities are recomputed with the existing RFC 8785 JCS plus SHA-256 `spec_hash` implementation.
9. `evidence_bundle_ref`, `release_ref`, and public use are fixed to null/null/false, and every authority effect is false.

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | The synthetic chain is closed and all embedded shapes and identities conform. |
| `ABSTAIN` | Captured-byte or parsed-record support is unavailable, unsupported, or unresolved. |
| `DENY` | References, parser identity, locator/digest bindings, transform requirements, or authority boundaries conflict. |
| `ERROR` | Input shape, JSON safety, executable model, or deterministic identity is invalid. |

No outcome establishes truth, source authority, rights, sensitivity, EvidenceBundle sufficiency, policy approval, review, release, or public safety.

## Deliberate holds

- No source is discovered, fetched, admitted, activated, or written.
- No raw source statement or normalized field value is stored; fixtures use digests and synthetic references.
- No EvidenceRef is resolved outside the in-memory synthetic packet.
- No EvidenceBundle, policy decision, review record, ReleaseEvidenceIndex, release manifest, DTO, API, AI answer, map layer, export, or publication surface is created.
- TransformReceipt presence is checked as a reference requirement only; this profile does not authenticate a receipt.

## Directory Rules basis

Accepted ADR-0029 places meaning in `contracts/evidence/`, shape in `schemas/contracts/v1/evidence/`, synthetic proof input in `fixtures/contracts/v1/evidence/`, deterministic checking in `tools/validators/`, executable proof in `tests/validators/`, CI in `.github/workflows/`, source mapping in `docs/intake/exploratory/`, and authoring accountability in `data/receipts/generated/`.

No new root, source registry, evidence resolver, proof store, policy home, review lane, release lane, or publication authority is created.

## Rollback

Before merge, close the draft pull request and delete only its branch. After an authorized merge, revert the additive implementation commit. No live source, evidence, lifecycle, policy, release, API, cache, map, or public state requires restoration.
