# Evidence-binding chain assessment fixtures

These fixtures exercise one synthetic `SourceArtifact -> ParseResult -> EvidenceRef -> ClaimFieldBinding` chain without network access, raw source values, EvidenceBundle creation, policy evaluation, lifecycle writes, release, or publication.

- `valid_assessment.json` embeds existing SourceArtifact, EvidenceRef, and ClaimFieldBinding shapes and a serialized projection of the executable source-adapter ParseResult model.
- `cases.json` checks exact `PASS`, `ABSTAIN`, `DENY`, and `ERROR` behavior for unavailable bytes, parser and artifact mismatches, unsupported parse results, unresolved records, evidence-reference drift, locator and digest drift, transform-receipt absence, forbidden EvidenceBundle fields, authority overreach, and identity corruption.

Fixture `PASS` proves only synthetic reference closure. It does not establish source truth, evidence sufficiency, rights, sensitivity, policy approval, review, release, public safety, or publication authority.
