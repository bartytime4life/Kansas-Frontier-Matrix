# Repository Next Steps (2026-04-25)

This runbook captures the most important next actions after a fresh repository scan and baseline verification run on **2026-04-25**.

## Evidence snapshot

- Baseline local verification is green via `tools/ci/run_repo_baseline_local.sh`, including schema checks, runtime policy fixture checks, renderer fixture checks, and CI tests (`95 passed`).
- The baseline GitHub workflow (`.github/workflows/verification-baseline.yml`) already executes thin-slice checks for baseline integrity, script validation, policy fixture validation, renderer fixture validation, and `tests/ci`.
- Baseline now also runs ecology API/UI boundary tests (`apps/governed-api/ecology/tests` and `apps/ui/ecology/tests`), with dependency-aware skips when optional packages are not installed.
- Baseline workflow installs optional boundary-test dependencies via `tools/ci/install_boundary_test_deps.sh` before running ecology boundary tests.
- Python syntax checks are now enforced in baseline for repository Python files via `tools/ci/check_python_syntax.sh` (with optional manifest mode via `tools/ci/python_syntax_targets.txt`).
- Placeholder marker reporting is now automated via `tools/ci/report_placeholder_markers.py` and is included in the local baseline runner and baseline workflow for observability.
- The repo remains documentation-heavy (190 Markdown files out of 361 files), which means governance quality is currently constrained more by documentation clarity than by missing baseline test scaffolding.
- Placeholder and uncertainty markers are still high:
  - `TODO`: 491
  - `UNKNOWN`: 475
  - `NEEDS VERIFICATION`: 1,852

## Why the priorities changed

Earlier next-step guidance focused on adding baseline and smoke checks. That work is now in place. The highest-value work has shifted to **reducing ambiguity in authoritative docs**, **turning thin-slice checks into enforceable contract tests at additional boundaries**, and **proving one governed end-to-end runtime path beyond fixture-level smoke validation**.

## Priority plan

### P0 — Reduce trust-surface ambiguity in top-level docs (1–2 days)

1. Rewrite the root `README.md` from “unknown/doctrine-first” language to “repo-evidenced” language.
2. Keep the doctrine framing, but move speculative/legacy claims into a clearly labeled appendix.
3. Set a target to reduce root-README `NEEDS VERIFICATION` markers by at least **50%**.

**Definition of done:**
- Root README claims only behaviors that are directly backed by existing paths, scripts, tests, or workflow jobs.
- Remaining uncertain claims are isolated and explicitly labeled as future work.

### P1 — Add mandatory contract gate coverage beyond current fixtures (2–4 days)

1. Extend CI from fixture validity checks to explicit **contract boundary checks**:
   - API route payload contracts (`apps/governed-api/ecology/*`)
   - UI payload mapping contracts (`apps/ui/ecology/evidence_drawer_mapper.py`)
2. Add at least one negative test per boundary for malformed payloads and missing required fields.
3. Ensure failure messages are deterministic and actionable.

**Definition of done:**
- CI fails when contract-breaking payload changes are introduced at API or UI adapter boundaries.
- New tests document expected failure behavior for malformed evidence/claim payloads.

### P2 — Build one governed E2E proof path in CI artifacts (3–5 days)

1. Promote one deterministic end-to-end path from fixture input to rendered output artifact:
   - runtime fixture → policy decision → renderer summary artifact
2. Publish the output as a CI artifact and validate checksum/structure in tests.
3. Document the path in a short operator runbook.

**Definition of done:**
- One command path can reproducibly generate a governed output artifact from fixed fixtures.
- CI verifies both semantic content and structural stability of that artifact.

### P3 — Systematically burn down placeholder debt in high-impact docs (ongoing)

1. Rank files by marker density and start with root/architecture/runbook docs.
2. For each file, resolve markers by either:
   - replacing with verified facts,
   - moving to a planned-work section, or
   - deleting stale claims.
3. Track weekly marker counts in this runbook.

**Definition of done:**
- Marker count trend is consistently down week-over-week.
- Documentation uncertainty no longer blocks implementation or review decisions.

## 7-day execution packet (recommended)

1. **Day 1:** Root README truth pass (P0) ✅ completed.
2. **Day 2–3:** Add API/UI negative boundary tests (P1).
3. **Day 4–5:** Add one deterministic E2E governed artifact test + CI artifact publish (P2).
4. **Day 6:** Run placeholder triage on top 10 docs (P3).
5. **Day 7:** Publish progress update in this file with new metrics and remaining blockers.

## Weekly scorecard template

Update this section each week.

- Baseline run status: `PASS/FAIL`
- `tests/ci` pass count:
- Marker counts:
  - `TODO`: (from `tools/ci/report_placeholder_markers.py`)
  - `UNKNOWN`: (from `tools/ci/report_placeholder_markers.py`)
  - `NEEDS VERIFICATION`: (from `tools/ci/report_placeholder_markers.py`)
- Root README verification marker count:
- New boundary tests added this week:
- E2E governed artifact status:
- Top blocker:

## Commands used for this analysis

```bash
tools/ci/run_repo_baseline_local.sh
python3 tools/ci/report_placeholder_markers.py --root . --top 10
python3 tools/ci/report_placeholder_markers.py --root . --max-overall 5000 --max-marker "NEEDS VERIFICATION=2500"
python - <<'PY'
from pathlib import Path
root=Path('.')
files=[p for p in root.rglob('*') if p.is_file() and '.git' not in p.parts]
print('files',len(files))
print('markdown',sum(1 for p in files if p.suffix.lower()=='.md'))
PY
python - <<'PY'
import subprocess
for pat in ['TODO','UNKNOWN','NEEDS VERIFICATION']:
    out=subprocess.run(['rg','-n',pat,'.'],capture_output=True,text=True)
    count=0 if out.returncode==1 else len(out.stdout.strip().splitlines())
    print(pat,count)
PY
```
