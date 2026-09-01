# DrinkingWaterAdvisory fixtures

This fixture family contains synthetic public-water-system identifiers,
authority references, source outcomes, service-area references, and advisory
times only. It contains no real advisory, address, person, health claim,
credential, source locator, restricted payload, or public guidance.

The semantic validator also rejects RFC 3339 `-00:00` unknown-offset markers
for source-check, issue, effective, expiry, and rescission timestamps. Such
values are never treated as exact UTC evidence for derived temporal findings.
The marker is recognized only on a schema-valid aware date-time; a malformed
string that merely ends in `-00:00` cannot satisfy rescission requirements.
Semantic ordering accepts the same RFC 3339 date-time grammar and aware-offset
suffix as the schema, including lowercase `t`, and does not derive ordering
claims from schema-invalid timestamp syntax.

`PASS` proves local profile coherence only. It does not establish a current
advisory, safe drinking water, source admission, evidence closure, policy or
health review, alert authority, release, publication, or public use.
