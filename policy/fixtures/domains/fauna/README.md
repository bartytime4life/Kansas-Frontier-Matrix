# Fauna policy-fixture compatibility boundary

Status: empty compatibility scaffold; no policy fixture is active from this directory.

`policy/fixtures/domains/fauna/` currently contains only this README and `.gitkeep`. The previous empty file did not distinguish this path from KFM's established policy and reusable-fixture homes.

## Current routing

- Fauna policy semantics and their current maturity are documented at [`../../../domains/fauna/README.md`](../../../domains/fauna/README.md).
- Reusable synthetic Fauna fixtures are documented at [`../../../../fixtures/domains/fauna/README.md`](../../../../fixtures/domains/fauna/README.md).

This directory does not duplicate either responsibility. Add a policy-local fixture here only when a reviewed policy evaluator or native policy-test convention requires co-location and the same change identifies the consumer, finite expected decision, fail-closed negative case, public-safe synthetic data boundary, and rollback. Otherwise, place reusable fixtures in the established `fixtures/` root.

## Safety and authority boundary

Do not place real animal occurrences, rare-species locations, nests, dens, roosts, telemetry, steward-controlled records, private-land details, restricted source payloads, credentials, concrete geoprivacy parameters, EvidenceBundles, receipts, proofs, lifecycle data, or release records here. A synthetic fixture may test policy behavior; it cannot establish source authority, rights, sensitivity clearance, evidence sufficiency, review, release, deployment, promotion, or publication.

## Validation and rollback

For this documentation-only repair, verify both relative links, confirm the directory still contains no fixture payloads or executable policy, and check the Markdown for one H1, a final newline, and no trailing whitespace.

Rollback by reverting this README. No policy rule, fixture payload, evaluator, source, data, release, or public state changes.
