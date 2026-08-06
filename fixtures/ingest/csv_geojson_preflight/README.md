# CSV-to-GeoJSON preflight fixtures

These files are synthetic, public-safe, no-network test inputs. Coordinates and labels are invented solely to exercise deterministic parsing and geometry validation. They are not source observations, admitted source data, evidence, or public map content.

- `profile.json` — exact fixture-only mapping and source-reference profile.
- `valid.csv` — three valid rows intentionally out of identifier order.
- `invalid_duplicate_id.csv` — duplicate row identity.
- `invalid_coordinate.csv` — latitude outside the admitted range.
- `invalid_formula.csv` — formula-like property value.

The focused tests create all output candidates under temporary directories. No fixture is written into a KFM lifecycle lane.
