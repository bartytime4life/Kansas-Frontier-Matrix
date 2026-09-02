<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/briefing-claim-field-binding-source-map
title: Briefing ClaimFieldBinding Source Map
type: exploratory-source-map
version: v0.1.0
status: draft; PROPOSED adaptation; non-authoritative
owners: ["@bartytime4life"]
created: 2026-08-08
updated: 2026-08-08
policy_label: internal; exploratory; evidence; no-authority
owning_root: docs/
responsibility: Record the source-to-repository adaptation for field-level evidence binding and preserve the next bounded evidence backlog.
truth_posture: "CONFIRMED current repository overlap check; PROPOSED adaptation; NEEDS VERIFICATION human review and hosted CI"
related:
  - ../../../contracts/evidence/claim_field_binding.md
  - ../../../contracts/evidence/evidence_ref.md
  - ../../../contracts/evidence/evidence_bundle.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, intake, exploratory, briefing, evidence, field-binding]
[/KFM_META_BLOCK_V2] -->

# Briefing ClaimFieldBinding Source Map

## Source requirement

The briefing-to-system evidence-binding table requires a field-level carrier
containing the object field, native statement, normalized value, EvidenceRef,
transform, and confidence. Its failure posture is omission, null, quarantine, or
explicit uncertainty when field support is inadequate.

The source also keeps `SourceArtifact`, `ParseResult`, `EvidenceRef`,
`EvidenceBundle`, `ClaimFieldBinding`, and `ReleaseEvidenceIndex` separate.
This packet implements only the field-binding carrier.

## Repository reconciliation

CONFIRMED against the implementation base:

- `contracts/evidence/evidence_ref.md` and
  `contracts/evidence/evidence_bundle.md` already own reference and bundle
  semantics;
- the repository contains the RFC 8785 JCS plus SHA-256 hashing package;
- ADR-0029 accepts Directory Governance Standard v2;
- bounded searches found no existing `claim_field_binding` contract, schema,
  validator, fixture packet, or open pull request for the exact family.

## Adaptation

```text
field-level evidence requirement
  -> evidence semantic contract
  -> closed Draft 2020-12 schema
  -> synthetic base-plus-mutation fixtures
  -> deterministic no-network validator
  -> focused tests
  -> read-only workflow
  -> byte-bound generated authoring receipt
```

The candidate stores digests rather than raw statements or values, requires a
TransformReceipt reference for every non-trivial transform, and leaves
EvidenceRef resolution outside the profile.

## Next sourced ideas

1. **Evidence-binding chain test:** prove
   `SourceArtifact -> ParseResult -> EvidenceRef -> ClaimFieldBinding` reference
   closure without creating an EvidenceBundle.
2. **Conflict-preserving field projection:** define how conflicting field
   bindings become null, withheld, or explicitly uncertain in a candidate DTO.
3. **ReleaseEvidenceIndex:** HOLD until accepted release, policy/review,
   correction, and rollback reference families are verified.
4. **Evidence Drawer field provenance view:** HOLD until released,
   public-safe field bindings and a governed projection contract exist.

## Deliberate holds

No live source, source rights decision, EvidenceBundle resolution, public DTO,
map layer, AI answer, release object, or publication path is introduced.

## Rollback

Discard the branch before merge or revert the additive packet afterward. No
live or public state is affected.
