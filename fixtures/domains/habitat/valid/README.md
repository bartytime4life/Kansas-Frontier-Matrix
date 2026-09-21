# Habitat valid fixtures

`fixtures/domains/habitat/valid/`

Status: draft / fixture lane, first payload added. `PLACEHOLDER.md` is
retained alongside this README in case another consumer checks for its
presence.

| File | Object family | Scenario | Expected outcome |
|---|---|---|---|
| `valid_1_habitat_patch.json` | `HabitatPatch` | Synthetic generalized patch with toy ecoregion, area, and connectivity references. | Passes shape check against the current PROPOSED `habitat_patch.schema.json` stub; matches the field shape implied by `contracts/domains/habitat/habitat_patch.md` and sibling `land_cover/materiality` fixtures. |

Shared posture: all identifiers, digests, and geometry references are
synthetic. A passing check proves only the declared shape expectation, not
habitat truth, evidence closure, or release readiness.

See also: [`../golden/README.md`](../golden/README.md) · [`../invalid/README.md`](../invalid/README.md) · [`../land_cover/materiality/README.md`](../land_cover/materiality/README.md)
