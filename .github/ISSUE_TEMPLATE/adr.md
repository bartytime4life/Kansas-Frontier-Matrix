---
name: ADR — Architecture Decision Record
about: Propose a decision that changes authority, placement, lifecycle, policy, or contract version.
title: "ADR-XXXX — <short decision title>"
labels: ["adr", "adr-proposed"]
assignees: []
---

<!--
KFM ADR Template
Per ai-build-operating-contract.md §28 and directory-rules.md §10 (decisions of record).

When to file an ADR (§28):
- Adding/removing/renaming canonical roots
- Changing schema-home authority
- Creating parallel homes (schemas/contracts/policy/registry/release/proof/canonical-truth)
- Changing lifecycle phase boundaries
- Approving direct public access paths
- Adopting a model runtime envelope
- Changing promotion gates
- Changing sensitive-location posture
- Changing source-ledger authority
- Changing release/proof/receipt separation
- Introducing or retiring a domain steward role
- Changing CONTRACT_VERSION pinning convention (§37)

When this ADR is accepted, move it to docs/adr/ADR-XXXX-<slug>.md and set status to Accepted.
-->

## Status

<!-- One of: Proposed | Accepted | Superseded by ADR-YYYY | Withdrawn -->

Proposed

## Context

<!-- What is the situation forcing a decision? What invariants or doctrine sections are in play?
     Reference §§ from ai-build-operating-contract.md and directory-rules.md where relevant. -->

## Decision

<!-- The decision in plain language. State it as a directive ("We will…"). -->

## Evidence basis

<!-- §5 authority order. What evidence supports the decision?
     CONFIRMED items go first; PROPOSED items get a status label and a verification plan. -->

- `CONFIRMED`:
- `PROPOSED`:
- `NEEDS VERIFICATION`:

## Directory Rules basis

<!-- Which directory-rules.md sections apply, and how does this decision align with §11 of the
     operating contract? If this creates or relocates a responsibility root, cite the rule of thumb
     in §11.1 and explain why this is not a parallel-home violation (§11.3). -->

## Consequences

<!-- What becomes easier, harder, riskier, or more expensive? Name the trade-offs honestly.
     §1.6: "If a proposal bends an invariant, state the tradeoff clearly." -->

**Positive:**

-

**Negative / costs:**

-

**Neutral / accepted trade-offs:**

-

## Alternatives considered

<!-- Name at least two genuine alternatives and why they were not chosen.
     "Status quo" is a valid alternative; argue against it explicitly if you reject it. -->

1. **Alternative A —**
2. **Alternative B —**
3. **Status quo —**

## Validation

<!-- §24. How will we know this decision worked? What gates fire if it didn't?
     Fixture-only, no-network proofs come first where feasible (§24.2). -->

- Acceptance signal:
- Failure signal:
- Validator(s) affected:
- Policy test(s) affected:

## Rollback

<!-- §10.11. If this turns out to be wrong, how do we reverse it?
     If it cannot be cheaply reversed, say so and justify the irreversibility. -->

- Rollback target:
- Rollback cost estimate:
- Drift register entry on revert:

## Sensitive domains affected

<!-- §23. If any sensitive domain is touched, name the required additional reviewer(s). -->

- [ ] None
- [ ] Archaeology / cultural / Indigenous records
- [ ] Burial / sacred sites
- [ ] Rare species
- [ ] Critical infrastructure
- [ ] Living-person data
- [ ] Genealogy / DNA
- [ ] Private land
- [ ] Hazards / emergency
- [ ] Restricted source terms
- [ ] Exact-harm coordinates

Required additional reviewer(s):

## Companion artifacts affected

<!-- §47. Does this ADR require updates to: -->

- [ ] `schemas/contracts/v1/receipts/generated_receipt.schema.json`
- [ ] `policy/ai_builder/operating_contract.rego`
- [ ] `.github/PULL_REQUEST_TEMPLATE.md`
- [ ] `docs/runbooks/FIRST_GOVERNED_PR_RUNBOOK.md`
- [ ] `docs/prompts/ai-builder-system-prompts.md`
- [ ] None

If yes, list the changes needed:

## CONTRACT_VERSION implications

<!-- §37. Does this ADR require a MAJOR/MINOR/PATCH bump of the contract? -->

- [ ] PATCH — typo/link/clarification only
- [ ] MINOR — new elaborated section, new companion, new gate
- [ ] MAJOR — Operating Law change or receipt-field rename
- [ ] No bump

## Open questions

<!-- §49. Surface what this ADR does not yet resolve. -->

-

## References

<!-- Doctrine sections, prior ADRs, corpus PDFs, related issues/PRs. -->

- `docs/doctrine/ai-build-operating-contract.md` §
- `docs/doctrine/directory-rules.md` §
- Prior ADR(s):
- Related PR(s) / issue(s):

---

<sub>This ADR follows §28 of the operating contract. After acceptance, the file moves to `docs/adr/` and the status is updated. Drift between this decision and current implementation MUST be logged in `docs/registers/DRIFT_REGISTER.md` (§37.3).</sub>
