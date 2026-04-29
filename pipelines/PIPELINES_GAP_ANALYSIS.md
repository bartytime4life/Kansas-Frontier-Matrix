# Pipelines Gap Analysis (as of 2026-04-29)

This document summarizes what appears missing or outdated in `pipelines/` based on a direct repository scan.

## High-level findings

1. **Documentation maturity is ahead of implementation maturity** in several pipeline lanes.
   - Multiple pipeline folders only contain `README.md` and no runnable code.
2. **Metadata placeholders are still unresolved** across many docs.
   - Frequent placeholders include `TODO`, `TBD`, `NEEDS VERIFICATION`, and ownership/policy/date placeholders.
3. **Some lanes are implemented and testable**, especially:
   - `pipelines/kansas_biodiversity_etl/catalog/*`
   - `pipelines/kansas_biodiversity_etl/validate/promotion_gate_full.py`
   - `pipelines/watchers/hydrology_huc12_admin_crosswalk_watch/*`
4. **Cross-doc consistency debt exists**: many READMEs still describe “proposed” commands/paths rather than verified repo-native commands.

## Missing or incomplete items by area

### 1) Directory-level implementation gaps

The following directories currently contain only a `README.md` (no scripts/tests/assets), indicating likely missing runnable components:

- `pipelines/habitat_layer_build/`
- `pipelines/kansas_biodiversity_etl/dedupe/`
- `pipelines/kansas_biodiversity_etl/normalize/`
- `pipelines/usgs-gage-watch/`
- `pipelines/watchers/kansas_flora_watch/`
- `pipelines/watchers/soil_air_quality/`

**What likely needs update**
- Add minimal runnable entrypoints (`runner.py`, Make targets, or equivalent) and fixture/test paths that match each README.
- If a lane is intentionally documentation-only, explicitly mark it as roadmap-only and add acceptance criteria for “implementation complete”.

### 2) Unresolved governance metadata in READMEs

Common unresolved fields are still present in top-level and leaf docs:

- `doc_id`
- `owners`
- `created`
- `policy_label`
- `related`

**What likely needs update**
- Resolve these fields in all production READMEs, or formally mark specific docs as draft with a tracked issue reference.

### 3) Highest-placeholder documents (priority)

By quick placeholder-density scan, prioritize these files first:

1. `pipelines/watchers/hydrology_huc12_admin_crosswalk_watch/sql/README.md`
2. `pipelines/kansas_biodiversity_etl/catalog/README.md`
3. `pipelines/kansas_biodiversity_etl/dedupe/README.md`
4. `pipelines/kansas_biodiversity_etl/publish/README.md`
5. `pipelines/watchers/hydrology_huc12_admin_crosswalk_watch/README.md`
6. `pipelines/kansas_biodiversity_etl/harvest/README.md`
7. `pipelines/README.md`
8. `pipelines/kansas_biodiversity_etl/validate/README.md`

**What likely needs update**
- Replace placeholder commands with verified commands that run in this repo.
- Replace placeholder paths with canonical paths in this repo.
- Remove “NEEDS VERIFICATION” where verification can now be done locally.

### 4) Test/fixture parity gaps

Some READMEs describe negative fixtures and failure modes that do not yet have matching concrete fixture files in adjacent directories.

**What likely needs update**
- For each README checklist item, either:
  - add the fixture/test artifact, or
  - remove/reword the claim and link to a tracking issue.

### 5) Consistency between contracts and validators

Where scripts do exist, there are explicit fail-closed checks and reason codes. Documentation should be tightened to reflect the exact implemented reason codes and CLI flags.

**What likely needs update**
- Generate documentation snippets directly from implemented validators where possible (or add a CI doc drift check).

## Suggested update order

1. **Stabilize ownership/policy metadata** in `pipelines/README.md` and each leaf README.
2. **Pick one watcher lane and one ETL lane** and make their docs + commands executable end-to-end.
3. **Add missing runners/tests** for doc-only lanes or explicitly mark them roadmap-only.
4. **Add CI checks** for:
   - unresolved placeholder tokens in non-draft docs
   - referenced command/path existence
   - fixture checklist drift

## Evidence collection commands used

```bash
rg --files pipelines
rg -n "TODO|TBD|FIXME|coming soon|placeholder|stub|missing|not implemented" pipelines
python - <<'PY'
# placeholder-density scan
...
PY
python - <<'PY'
# detect directories that only contain README.md
...
PY
```
