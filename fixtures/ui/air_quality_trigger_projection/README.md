# Air-quality trigger projection fixtures

These synthetic packets exercise the app-local
`kfm.explorer.air-quality-trigger.fixture.v1` display boundary.

- `valid/proposed-trigger.json` requires both categorical comparisons and two
  distinct digest-bound evidence references.
- `valid/no-trigger.json` proves an at-or-below relation remains distinct from
  a proposed candidate.
- `valid/held.json`, `valid/denied.json`, and `valid/error.json` carry no
  candidate or reference detail.
- `invalid/extra-raw-field.json` proves raw concentration and internal detail
  fail closed without reflection.
- `invalid/relation-mismatch.json` proves candidate labels cannot contradict
  their categorical relations.

The fixtures contain no real observation, station, coordinate, PM2.5
concentration, threshold, AQI, health category, source payload, resolved
EvidenceBundle, policy decision, event, or released claim.
