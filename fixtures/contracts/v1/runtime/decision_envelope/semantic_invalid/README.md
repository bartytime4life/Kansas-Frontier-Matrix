# DecisionEnvelope semantic-negative fixtures

These records are valid against the current Draft 2020-12 schema but violate one reviewed
cross-field or trust-boundary invariant enforced by
`tools/validators/validate_decision_envelope.py`.

The authoritative expected result set is the sibling
`../expected_findings_manifest.json`. Every record is synthetic, no-network, and contains no
real evidence, policy decision, credential, sensitive location, person, or release authority.
