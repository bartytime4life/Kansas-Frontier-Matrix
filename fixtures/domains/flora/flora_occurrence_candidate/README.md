# `FloraOccurrenceCandidate` synthetic fixtures

This fixture family contains no live connector call, no real protected locality, no source credential, and no source-admission or publication decision.

Valid profile cases cover:

- a synthetic GBIF-style human observation with an internal exact point;
- a synthetic iDigBio-style preserved specimen with source generalization and withholding hints; and
- a synthetic GBIF-style occurrence with no coordinates.

Negative cases cover missing source-record identity, missing scientific name, partial coordinates, out-of-range coordinates, and negative uncertainty. `expected_outcomes.json` binds every input to its source profile, source ID, finite outcome, exact finding-code set, and expected candidate where one is produced.

A passing replay proves only deterministic normalization to a WORK-stage candidate.
