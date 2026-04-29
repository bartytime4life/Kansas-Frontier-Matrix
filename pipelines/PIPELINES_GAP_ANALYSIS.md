# Pipelines Gap Analysis (as of 2026-04-29)

This document summarizes missing or outdated items in `pipelines/` from a direct repository scan in this checkout.

## High-level findings

1. **Documentation maturity is ahead of implementation maturity** in several lanes.
2. **Governance placeholders are still widespread** (`TODO`, `TBD`, `NEEDS VERIFICATION`, and metadata placeholders).
3. **Some lanes are implemented and testable**, especially:
   - `pipelines/kansas_biodiversity_etl/catalog/*`
   - `pipelines/kansas_biodiversity_etl/validate/promotion_gate_full.py`
   - `pipelines/watchers/hydrology_huc12_admin_crosswalk_watch/*`
4. **Cross-doc drift exists**: multiple READMEs still describe proposed paths/commands rather than verified repo-native commands.

## 1) Directory-level implementation gaps

The following directories currently contain only `README.md` (no scripts/tests/assets at the same level), which indicates likely missing runnable components:

- `pipelines/habitat_layer_build/`
- `pipelines/kansas_biodiversity_etl/dedupe/`
- `pipelines/kansas_biodiversity_etl/normalize/`
- `pipelines/usgs-gage-watch/`
- `pipelines/watchers/kansas_flora_watch/`
- `pipelines/watchers/soil_air_quality/`

**Required updates**
- Add minimal runnable entrypoints (for example `runner.py` or repo-native shell targets).
- Add lane-local fixtures/tests or wire to existing validators.
- If intentionally doc-only, mark lane as `roadmap-only` and link a tracked implementation issue.

## 2) Unresolved metadata fields in READMEs

Common unresolved fields still present:

- `doc_id`
- `owners`
- `created`
- `policy_label`
- `related`

**Required updates**
- Resolve metadata for stable lanes.
- Keep placeholders only in explicitly draft docs and include issue references.

## 3) Highest-placeholder files to prioritize

Placeholder-density scan (README files under `pipelines/`):

1. `pipelines/watchers/hydrology_huc12_admin_crosswalk_watch/sql/README.md` (50)
2. `pipelines/kansas_biodiversity_etl/publish/README.md` (45)
3. `pipelines/kansas_biodiversity_etl/catalog/README.md` (41)
4. `pipelines/kansas_biodiversity_etl/README.md` (41)
5. `pipelines/kansas_biodiversity_etl/dedupe/README.md` (33)
6. `pipelines/kansas_biodiversity_etl/normalize/README.md` (31)
7. `pipelines/README.md` (31)
8. `pipelines/watchers/kansas_flora_watch/README.md` (28)
9. `pipelines/kansas_biodiversity_etl/harvest/README.md` (25)
10. `pipelines/watchers/hydrology_huc12_admin_crosswalk_watch/fixtures/README.md` (24)
11. `pipelines/watchers/hydrology_huc12_admin_crosswalk_watch/README.md` (24)
12. `pipelines/kansas_biodiversity_etl/validate/README.md` (23)

**Required updates**
- Replace placeholder commands with verified commands that run in this repo.
- Replace placeholder paths with canonical repo paths.
- Remove `NEEDS VERIFICATION` markers once locally verified.

## 4) Test/fixture parity gaps

Some READMEs describe failure modes and fixture expectations that are not represented by adjacent concrete fixture files.

**Required updates**
- For each checklist claim, either:
  - add matching fixtures/tests, or
  - reword/remove the claim and link a tracking issue.

## 5) Contract/validator consistency gaps

Where scripts are implemented, behavior is fail-closed with explicit reason codes; docs should mirror actual CLI flags and reason-code vocabulary.

**Required updates**
- Generate doc snippets from implemented validators where possible.
- Add a CI doc-drift check for reason-code and CLI-flag mismatches.

## Suggested execution order

1. **Metadata closure**: stabilize ownership/policy/date metadata in `pipelines/README.md` and lane READMEs.
2. **Executable closure**: make one watcher lane and one ETL lane fully runnable end-to-end.
3. **Doc-only lane decision**: implement or explicitly mark roadmap-only with issue links.
4. **CI enforcement**:
   - unresolved placeholders in non-draft docs,
   - referenced command/path existence,
   - fixture checklist parity.

## Evidence commands run

```bash
rg --files pipelines
rg -n "TODO|TBD|NEEDS VERIFICATION|NEEDS_VERIFICATION|placeholder" pipelines
python - <<'PY'
from pathlib import Path
import re
root=Path('pipelines')
pat=re.compile(r'TODO|TBD|NEEDS VERIFICATION|NEEDS_VERIFICATION|placeholder',re.I)
rows=[]
for p in root.rglob('README.md'):
    txt=p.read_text(errors='ignore')
    c=len(pat.findall(txt))
    if c: rows.append((c,p.as_posix()))
rows.sort(reverse=True)
for c,p in rows[:12]:
    print(c,p)
PY
python - <<'PY'
from pathlib import Path
root=Path('pipelines')
for d in sorted([x for x in root.rglob('*') if x.is_dir()]):
    kids=[k for k in d.iterdir() if not k.name.startswith('.')]
    files=[k for k in kids if k.is_file()]
    dirs=[k for k in kids if k.is_dir()]
    if files and all(f.name=='README.md' for f in files) and not dirs:
        print(d.as_posix())
PY
```
