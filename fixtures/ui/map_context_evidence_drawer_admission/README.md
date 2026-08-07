# MapContextEnvelope → EvidenceDrawerPayload admission fixtures

This no-network fixture lane exercises the cross-object adapter without creating a new
contract or authority object. Inputs use the existing renderer-neutral
`MapContextEnvelope` and public-safe `EvidenceDrawerPayload` profiles; outputs are
candidate `DecisionEnvelope` objects.

The cases prove aligned ANSWER and ABSTAIN propagation, safe DENY and ERROR
propagation without support leakage, selection-scoped evidence binding, context expiry,
fixture-role admission, and missing-selection abstention.

A passing fixture suite does not resolve evidence, evaluate policy, authenticate a caller
or reviewer, establish release state, authorize public use, or publish anything.
