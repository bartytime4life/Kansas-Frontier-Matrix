# Habitat thin-slice fixtures

`fixtures/domains/habitat/thin_slice/`

Status: draft / fixture lane, first payload added.

Small synthetic examples for a bounded Habitat thin-slice proof (a minimal
end-to-end dry-run touching identity, evidence, and public-safe rendering
for one object family). Not evidence, source truth, or release state.

| File | Scenario | Expected outcome |
|---|---|---|
| `valid_1_thin_slice_case.json` | Minimal synthetic dry-run case: one `HabitatPatch` identity plus a closed fixture-only evidence reference. | Passes the bounded thin-slice check; not released. |

See also: [`../habitat_fauna_thin_slice/README.md`](../habitat_fauna_thin_slice/README.md)
