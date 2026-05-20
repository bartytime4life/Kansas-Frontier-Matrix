# Invalid PMTiles Attestation Fixtures

Add negative fixtures here to exercise fail-closed behavior.

Recommended cases:

- `missing_spec_hash.pmtiles`
- `altered_header.pmtiles`
- `wrong_merkle_root.pmtiles.pmidx`
- `expired_signature.pmtiles.pmsig`
- `forged_signer.pmtiles.pmsig`
- `mismatched_receipt.runreceipt.json`
- `unpublished_source_receipt.runreceipt.json`
- `tampered_tile_range.pmtiles`

Do not include sensitive, unreleased, or production-derived tile payloads unless repository policy explicitly permits it.
