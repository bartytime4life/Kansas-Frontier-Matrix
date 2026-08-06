# MapManifestIntegrityAssessment Validator

Deterministic, no-network validation for the fixture profile described by:

- `contracts/map/map_manifest_integrity_assessment.md`
- `schemas/contracts/v1/map/map_manifest_integrity_assessment.schema.json`

It checks canonical manifest and assessment hashes, asset ordering/identity, precomputed signature-verdict consistency, EvidenceBundle/proof resolution, optional selected-asset byte/hash results, exact finite reasons, and outcome precedence.

It does not fetch assets, verify a real signature, approve a release, publish a map, or turn a rendered layer into evidence.
