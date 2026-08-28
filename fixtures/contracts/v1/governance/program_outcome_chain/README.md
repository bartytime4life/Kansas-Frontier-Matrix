# ProgramOutcomeChain fixtures

This fixture suite exercises the inactive, no-network
`kfm.governance.program-outcome-chain.v1` profile.

It proves only deterministic schema/semantic behavior:

- partial and full chains may pass when their dependencies are explicit;
- later stages cannot appear without required predecessors;
- fixed claim codes prevent eligibility, application, review, award, payment,
  completion, observation, and evaluation from collapsing into one meaning;
- amount, geometry, method, and uncertainty fields remain stage-specific;
- release, public-use, source, evidence, policy, review, causation, promotion,
  and publication effects remain false; and
- malformed fixture input returns `ERROR`.

Synthetic references, amounts, times, geometry identities, methods, and
uncertainty identities are not real program facts, evidence, policy decisions,
reviews, releases, or public claims.
