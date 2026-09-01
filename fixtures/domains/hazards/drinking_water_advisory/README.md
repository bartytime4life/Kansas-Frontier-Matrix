# DrinkingWaterAdvisory fixtures

This fixture family contains synthetic public-water-system identifiers,
authority references, source outcomes, service-area references, and advisory
times only. It contains no real advisory, address, person, health claim,
credential, source locator, restricted payload, or public guidance.

The semantic validator also rejects RFC 3339 `-00:00` unknown-offset markers
for source-check, issue, effective, expiry, and rescission timestamps. Such
values are never treated as exact UTC evidence for derived temporal findings.

`PASS` proves local profile coherence only. It does not establish a current
advisory, safe drinking water, source admission, evidence closure, policy or
health review, alert authority, release, publication, or public use.
