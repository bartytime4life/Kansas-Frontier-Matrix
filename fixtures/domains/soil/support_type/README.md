# Soil support-type fixtures

Synthetic, no-network candidates for the inactive Soil support-type profile.

- `valid/` contains one persisted positive control for each of the eight declared
  support types.
- `invalid/station_as_satellite_grid.json` is the persisted anti-collapse
  control.
- The focused test suite requires exact positive-fixture parity with the profile
  and also exercises negative binding, public-use, and reference-order cases.

The valid fixtures intentionally select one allowed source family, source role,
spatial support, and claim kind from each profile rule. They are examples for
validation and review only; they do not assert source activation or real-world
observations.

These fixtures create no source, evidence, policy, release, or publication
authority. They use invented identifiers and contain no operational or sensitive
locations.
