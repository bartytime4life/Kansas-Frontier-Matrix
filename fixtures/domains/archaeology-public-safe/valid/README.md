# Archaeology public-safe — valid fixtures

`fixtures/domains/archaeology-public-safe/valid/`

Status: draft / fixture lane, first payloads added per the parent README's
[Expected layout](../README.md#expected-layout).

These are small, wholly synthetic, positive-case examples for the public-safe
Archaeology fixture lane. They exercise renderer, candidate-state, and
generalization-shape checks only. They are not evidence, a confirmed site, a
policy decision, or a release artifact.

| File | Scenario | Consumer (intended) | Expected outcome |
|---|---|---|---|
| `valid_1_generalized_feature.json` | Synthetic generalized-grid feature, coarse cell only, no exact geometry. | Renderer / public-safe layer smoke check. | Passes shape check; renders as generalized, non-authoritative. |
| `valid_2_candidate_state.json` | Candidate (not confirmed-site) archaeology feature with withheld spatial precision. | Candidate-state / no-leak helper. | Passes; `truth_state` remains `CANDIDATE`, precision remains `WITHHELD`. |

Shared posture:

- All identifiers, references, and coordinates are synthetic placeholders and must not be read as real locations.
- Coordinates use a coarse, clearly-fictional grid cell (`generalization_method: "SYNTHETIC_GRID_CELL"`), never a real Kansas location.
- A passing check here proves only the declared shape/state expectation. It does not prove a site exists, a cultural review occurred, or a layer is release-approved.

See also: [`../README.md`](../README.md) · [`../invalid/README.md`](../invalid/README.md) · [`../../archaeology/synthetic_candidate_feature/README.md`](../../archaeology/synthetic_candidate_feature/README.md)
