# GovernanceEvent fixture profile

This directory contains one reusable governance-event base plus isolated
mutations for the inactive `kfm.governance.governance-event.v1` profile.

Positive fixtures keep `ANNOUNCED`, `SCHEDULED`, `HELD`, `CANCELLED`,
explicit downstream links, and conflicted source lineage distinct. Negative
fixtures prove that held state requires participation evidence, cancellation
cannot also claim held state, schedule intervals fail closed, implementation
requires a decision, outcomes require implementation, and release/public/effect
overclaims are denied.

All names, references, times, and digests are synthetic. No calendar, public
participation system, source adapter, evidence resolver, policy engine,
lifecycle store, release system, or public product is invoked.
