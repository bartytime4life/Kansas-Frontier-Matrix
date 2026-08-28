# KFM STAC trust-extension fixtures

These fixtures exercise the proposed `kfm-stac-profile-v1` machine profile without network access or live-source data.

- `valid/` contains three synthetic projections that must return `PASS`.
- `invalid/` contains six synthetic semantic negatives.
- `fixture_manifest.json` is the exact reviewed outcome and reason-code manifest.
- Every valid fixture uses `kfm:source_role: synthetic`.
- The release-linked valid fixture remains `NOT_PUBLISHED`.

The fixtures do not prove external STAC conformance, authenticate referenced objects, admit a source, close evidence, approve policy or review, release data, or publish anything.
