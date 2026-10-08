<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/cards/readme
title: Documentation intake cards
type: lane-readme
version: v1.0
status: draft; repository-grounded; review-required
owners:
  - OWNER_TBD - Documentation intake steward
  - OWNER_TBD - Documentation steward
created: 2026-10-08
updated: 2026-10-08
policy_label: public
owning_root: docs/
responsibility: Documentation intake cards; human guidance subordinate to owning contracts, schemas, policy, evidence, and release decisions
truth_posture: CONFIRMED inspected repository paths and bounded implementation; PROPOSED review procedure; UNKNOWN external source and operational acceptance
related:
  - docs/intake/README.md
  - docs/intake/triage-rules.md
  - docs/intake/promotions/README.md
evidence_snapshot: ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe
[/KFM_META_BLOCK_V2] -->

# Cards

This lane holds small, non-authoritative documentation intake cards: one idea,
claim, evidence gap or proposed change that needs classification before a larger
promotion packet. A card preserves context and routing; it does not establish
an accepted decision, source admission or implementation.

## When to use a card

Use a card when a proposal can be explained as one observable outcome but its
source support, ownership or destination still needs review. Link an existing
card or packet when the topic is already covered. Substantial source analysis
belongs in the existing [exploratory lane](../exploratory/README.md); a complete
review handoff belongs in [promotion packets](../promotions/README.md).

Do not store raw payloads, screenshots containing private data, binaries,
credentials, consent records, protected locations or rights-uncertain excerpts
here. Capture a permitted reference and a minimized summary instead.

## Minimum useful card

The following is an authoring template, not a machine-enforced schema:

```text
Card identity: stable descriptive identifier
Title: one proposed outcome
Status: triaged / candidate-for-promotion / exploratory-retained / lineage-only / rejected
Problem: observable gap and affected reader or workflow
Evidence: exact source/path/version or an explicit unknown
Claim posture: confirmed / proposed / inferred / needs verification
Existing overlap: related document, issue, packet or implementation
Proposed owner and destination: role and verified path, or unresolved
Direct dependencies: contracts, schemas, policy, code, tests and documents affected
Constraints: rights, sensitivity, public precision, access and resource limits
Next action: one bounded investigation or implementation step
Validation: what would demonstrate that step succeeded
Correction/rollback: how an incorrect recommendation is withdrawn or superseded
Lineage: prior card, source map and later packet links
```

Do not invent a person's name, source version or approval to fill a blank.
Unknown ownership should name the required reviewer role and remain unresolved.
Use stable lowercase filenames consistent with existing lane conventions; keep
state in the card rather than renaming it every time a review changes.

## Card workflow

1. Search the existing intake indexes, domain documentation and current work for
   overlap before making a new card.
2. Read the cited source; separate its recommendation from verified repository
   behavior. Record the exact revision for implementation claims.
3. Apply [triage rules](../triage-rules.md), including rights/sensitivity and
   authority-placement checks.
4. Record a finite disposition and the next action or retention reason.
5. When ready, link to a promotion packet with a verified owning destination and
   direct dependencies. Keep the card as lineage rather than a second authority.
6. On supersession, retain the old identity and link the replacement and reason.

## Example classification

A note that “Soil moisture needs a date label” begins as a claim needing a check
against current Site source and tests. If the label already exists, retain the
card as lineage or link the existing work. If a real gap is found, identify the
exact component and acceptance check before proposing implementation. Neither
outcome is a source-admission or publication decision.

## Acceptance and maintenance

A useful card has one coherent claim, traceable evidence or an explicit gap,
clear uncertainty, no duplicated authority and a concrete next step. Check
relative links, metadata when present, headings and the full diff. No live source
access or domain tests are needed merely to classify prose unless the card makes
new behavior claims that require them.

The lane's broader canonical classification remains the question recorded in
[the intake index](../README.md). Filling this README does not settle that
architecture question or create a card executor, registry or review authority.
