# PR-007 Repo Inspection

CONFIRMED: Phase 0 commands were run before edits.
CONFIRMED: branch is `work`; repo root is `/workspace/Kansas-Frontier-Matrix`; dirty state was clean at inspection time.
CONFIRMED: PR-002..PR-006 baseline docs and fixtures are present.
CONFIRMED: PR-006 WORK candidate exists at `fixtures/domains/hydrology/work_candidates/usgs_water_data.synthetic_streamflow.work_candidate.json`.
CONFIRMED: ingest drill files exist under `fixtures/domains/hydrology/ingest_plans`, `raw_capture`, `quarantine`, and `work_receipts`.
CONFIRMED: processed/catalog/triplet fixtures for PR-007 were not present before this PR.
CONFIRMED: existing evidence bundle fixtures exist (`evidence_bundle.synthetic.valid.json`, `evidence_bundle.synthetic.invalid.json`).
CONFIRMED: existing release dry-run fixtures exist (`promotion_dry_runs/*`, `release_candidate.synthetic.*`).
CONFIRMED: existing validators/tests exist under `tools/validators` and `tests/domains/hydrology`.
CONFIRMED: stack evidence is Python with `pyproject.toml`.
CONFIRMED: no compatibility roots (`ui/`, `web/`, `jsonschema/`, `policies/`, `styles/`, `viewer_templates/`) are canonical roots in current tree.
UNKNOWN: mounted source PDFs were not directly inspectable in this run.
NEEDS VERIFICATION: production deployment posture and live API contracts beyond synthetic fixtures.
PROPOSED: PR-008 synthetic release review/public artifact drill with manual review + release manifest closure.
