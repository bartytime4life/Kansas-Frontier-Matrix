# MRTS-05 trust-spine fixture slice

This directory contains one synthetic, public-safe, no-network fixture chain. `flow.json` pins eleven existing KFM object-family candidates and their SHA-256 digests; `cases.json` defines thirteen exact fail-closed mutations; `artifacts/` contains the candidate-specific fixture objects.

The slice preserves every conflict recorded in `control_plane/object_family_register.yaml`. A candidate schema used here is a fixture binding, not a canonical-family decision.

Run `make trust-spine-fixture-slice`. A pass means deterministic fixture closure and offline dry-run readiness only. It does not activate a source, approve policy or review, mutate lifecycle state, release, deploy, promote, publish, or create a public route.
