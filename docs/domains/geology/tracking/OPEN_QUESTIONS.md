# Geology & Natural Resources Open Questions

Focused decision log for unresolved lane-shaping questions.

| Question | Decision driver | Decision due when | Current state |
| --- | --- | --- | --- |
| Which lane slug is canonical and which (if any) is compatibility-only? | Documentation and schema authority must be singular. | Before adding machine contracts. | Open |
| Should geology contracts live under `schemas/contracts/v1/geology/` or a repo-native alternative? | Determines validator and fixture routing. | Before first contract PR. | Open |
| Which agencies/sources are authoritative per claim class? | Source-role model and policy gates depend on this. | Before connector activation. | Open |
| What coordinate precision rules apply to public borehole/sample/resource displays? | Impacts layer publication and Evidence Drawer payloads. | Before public layer release. | Open |
| What runtime endpoints are the official geology API surfaces? | Required for accurate docs and integration tests. | Before API docs are marked verified. | Open |
| Which release/proof toolchain is authoritative in this repo? | Needed for truthful quickstart and release guidance. | Before operational runbook promotion. | Open |

## Usage

- Move resolved questions to `EVOLUTION_LOG.md` with closure reference.
- Keep this file short; move deep discussion to ADRs or design docs.
