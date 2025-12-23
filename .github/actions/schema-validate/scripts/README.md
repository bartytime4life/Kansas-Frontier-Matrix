# schema-validate — scripts

This directory contains helper scripts used by the local GitHub Action at:

- `.github/actions/schema-validate/`

Its job is to enforce the **Schema validation** CI gate (e.g., STAC/DCAT/PROV and other schema-governed artifacts), with deterministic behavior:

- **validate if present; fail if invalid; skip if not applicable**

> Repo lint note: this README intentionally contains **no YAML front-matter** because it lives under `.github/` (a “code files” area).

## What this action may validate

Depending on how the workflow wires inputs, scripts in this folder may validate:

### 1) Schema definitions (contracts)
- JSON Schemas under `schemas/**` (examples include: STAC, DCAT, PROV, Story Nodes, UI registries, telemetry).

### 2) Generated artifacts (evidence outputs)
Artifacts produced by pipeline stages and stored under canonical roots, for example:
- `data/stac/**`
- `data/catalog/dcat/**`
- `data/prov/**`

## Deterministic behavior contract (required)

All scripts in this folder should follow the same semantics:

1. **If target root(s) do not exist** (optional in early phases):
   - Exit `0`
   - Print a clear “SKIP” message (and which root was missing)

2. **If target root(s) exist**:
   - Validate all matching files
   - If **any** file is invalid:
     - Exit non-zero
     - Print file path(s) and an actionable error summary
   - If **all** files are valid:
     - Exit `0`

## Local usage

From the repository root:

~~~bash
# List scripts
ls .github/actions/schema-validate/scripts

# Run a script directly (example)
bash .github/actions/schema-validate/scripts/<script-name> --help
~~~

Notes:
- The authoritative entrypoint is the parent action definition under `.github/actions/schema-validate/`.
- Prefer running scripts from repo root so relative paths resolve consistently.

## Extending validations (new schema family or new target root)

When adding a new schema family and/or validating a new artifact root:

1. Add schema files under `schemas/<family>/...`.
2. Update the relevant validator script(s) in this folder to include:
   - the new schema family path(s)
   - the new output root(s) to scan/validate
3. Keep behavior deterministic:
   - skip if optional root absent
   - fail if present but invalid
4. If the repo has test fixtures, add/adjust them under `tests/` and ensure CI calls these scripts.

## Troubleshooting

- **“Root not found”**  
  The workflow is referencing a root that is not present in the repo checkout. Decide whether the root is:
  - optional → script should SKIP
  - required → create/populate it, or make the CI job fail explicitly

- **“Schema reference not resolved”**  
  Check `$ref` targets and ensure referenced schema files exist and are reachable from the validator’s working directory.

- **“Invalid JSON”**  
  Validate the file format first (no trailing commas, valid JSON).

## Related KFM docs

- `docs/MASTER_GUIDE_v12.md` (canonical pipeline ordering and canonical homes)
- `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` (CI gate mapping + deterministic validation rule)
- `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` (validation checklist conventions)
