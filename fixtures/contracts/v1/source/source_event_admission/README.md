# Source Event Admission fixtures

These fixtures extend the existing `SourceEventEnvelopeCandidate` profile with deterministic prefilter and fixture-only run-receipt candidates.

## Layout

```text
source_event_admission/
├── README.md
├── fixture_manifest.json
├── valid/
└── invalid/
```

The manifest binds every case to one existing valid event fixture under:

```text
fixtures/contracts/v1/source/source_event_envelope/valid/
```

Receipt cases also identify the companion prefilter fixture.

## Coverage

- valid material-change prefilter;
- valid rights-unknown quarantine prefilter;
- valid duplicate-replay no-action prefilter;
- valid `ALLOW`, `QUARANTINE`, and `NO_ACTION` receipt candidates;
- out-of-range score;
- nondeterministic model configuration;
- classification/destination mismatch;
- missing signature;
- decision/target mismatch;
- fixture-signature mismatch; and
- prefilter-reference mismatch.

All data is synthetic. The fixture signature is deterministic test evidence only and is not production cryptographic attestation. A fixture `PASS` creates no source activation, lifecycle write, evidence, policy, review, promotion, release, publication, or public-use authority.
