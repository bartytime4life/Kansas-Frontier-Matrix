# Friday natural-systems pulse fixtures

**Status:** `PROPOSED_INACTIVE` · synthetic · fixture-only · no-network · no-schedule · no-publication.

This lane proves deterministic aggregation of already-validated `MaterialChangeAssessment` records for exactly five scopes:

1. `atmosphere`
2. `fauna_habitat`
3. `hydrology`
4. `soil`
5. `vegetation`

## Layout

- `upstream/` contains eight synthetic shared assessments used to compose the four finite pulse states.
- `valid/` contains exact `NO_EVENT`, `PULSE_CANDIDATE`, `HOLD`, and `ERROR` candidates.
- `invalid/` contains one true schema-negative case and ten schema-valid semantic negatives. `expected_findings_manifest.json` records the exact reviewed finding-code set for every negative fixture.

## State matrix

| Fixture | Bound assessment mix | Pulse result | Emits a review candidate? |
|---|---|---|---:|
| `valid_no_event.json` | five `NON_EVENT` | `NO_EVENT` | no |
| `valid_pulse_candidate.json` | four `NON_EVENT`, one `PROMOTION_CANDIDATE` | `PULSE_CANDIDATE` | yes, human review only |
| `valid_hold.json` | three `NON_EVENT`, one `HOLD`, one `PROMOTION_CANDIDATE` | `HOLD` | no |
| `valid_error.json` | three `NON_EVENT`, one `ERROR`, one `PROMOTION_CANDIDATE` | `ERROR` | no |

## Trust boundary

The fixtures contain no live source locators, source credentials, source bytes, precise sensitive coordinates, policy approval, authenticated review, lifecycle mutation, release record, deployment state, or publication permission. `PULSE_CANDIDATE` is review process memory only. It cannot execute `REBUILD`, create an issue or pull request, promote, release, deploy, publish, or permit public use.
