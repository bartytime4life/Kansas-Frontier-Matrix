# ProofPack contract fixtures

Synthetic, public-safe fixtures for `kfm.proof-pack.release-support.v1`.

- `artifacts/` contains small local support records used only to exercise path and digest closure.
- `candidates/` contains an assembler input with no computed digest fields.
- `valid/` contains schema-valid and semantically closed manifests.
- `invalid/invalid_*.json` contains schema-negative fixtures for repository-wide schema polarity tests.
- `invalid/semantic_invalid_*.json` remains schema-valid but fails the dedicated checker with the code in the paired `.expected_code.txt` file.

No fixture is source evidence, a release decision, a signature, or publication authority.
