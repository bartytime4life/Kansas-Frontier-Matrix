# RedactionReceipt v1 source and adaptation map

## Status

**PROPOSED_INACTIVE.** This packet replaces the existing permissive schema scaffold with a closed fixture-only machine profile. The existing semantic contract at `contracts/shared/redaction_receipt.md` remains the meaning authority.

## Source basis

- the existing shared RedactionReceipt contract and receipt catalog;
- KFM sensitivity tiers and domain transition rules requiring a `RedactionReceipt` for public-safe transformations;
- the AI Build Operating Contract's fail-closed sensitive-domain matrix;
- accepted Directory Rules v2 through ADR-0029.

## Adaptation boundary

The profile validates declarations only. It does not:

- open or transform restricted source material;
- execute policy;
- authenticate a reviewer or rights holder;
- prove a transform is sufficient;
- reveal protected values or reversal-enabling parameters;
- promote lifecycle state; or
- release or publish a derivative.

Domain-specific Flora, Fauna, Archaeology, People/Land, Infrastructure, and other constraints continue to apply. This shared profile does not erase them.

## Closure supplied by this packet

- a closed Draft 2020-12 schema paired to the existing semantic contract;
- deterministic receipt identity;
- exact positive and negative fixtures;
- leak-guard, public-tier, policy/review/validation, output, rollback, and non-effect checks;
- read-only CI and generated authoring provenance.

## Follow-on queue

1. Ratify shared versus domain-extension compatibility rules.
2. Bind a policy-selected transform profile in separate policy work.
3. Add geometry/content executors only after safe test data and steward review exist.
4. Integrate release-gate references without allowing this receipt to self-authorize publication.
