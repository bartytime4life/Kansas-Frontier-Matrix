# Foundation Strategy — Highest-Impact Base Building (2026-04-25)

This strategy turns the current repository baseline into a reliable, enforceable foundation for feature work.

## Current baseline reality

- Baseline runner is green and executes syntax checks, schema/policy fixture checks, renderer fixture checks, and test slices.
- Core CI (`tests/ci`) is stable.
- Ecology API/UI boundary tests are now in baseline but may skip when optional dependencies are unavailable.
- Placeholder debt remains high and should be converted from observability-only into managed reduction gates.

## Strategy goal

Move from **"baseline checks exist"** to **"baseline checks enforce production-shaping quality"** in 3 steps:

1. **Deterministic execution** (remove dependency and environment ambiguity).
2. **Contract enforcement at boundaries** (API/UI/runtime payload breakage fails fast).
3. **Documentation authority hardening** (high-marker docs stop drifting from implementation).

---

## Priority workstreams (impact-ordered)

## 1) Deterministic CI environment (P0)

### Why this is most impactful
Without deterministic dependencies, test results vary by environment. That blocks confidence in every other gate.

### Actions

- Introduce a pinned Python dependency lock for baseline + boundary tests.
- Replace best-effort dependency installation with deterministic installation in CI.
- Keep local docs-first fallback, but separate it from "required CI" behavior.

### Definition of done

- CI boundary tests run with dependencies installed from a pinned set.
- No proxy/network retries in required CI paths.
- Local runner supports two explicit modes:
  - `strict` (mirrors CI exactly)
  - `docs-first` (current fallback behavior)

## 2) Boundary contract fail-fast gates (P1)

### Why this is next
Most expensive regressions happen at API/UI boundaries.

### Actions

- Add mandatory negative-path tests for malformed, incomplete, and wrong-type payloads at:
  - `apps/governed_api/ecology/routes`
  - `apps/ui/ecology/evidence_drawer_mapper`
- Add contract snapshots for representative successful and abstain responses.
- Ensure deterministic error codes/messages for each boundary failure class.

### Definition of done

- Contract-breaking payload changes fail CI before merge.
- Boundary tests cover both positive and negative paths with explicit expected outcomes.

## 3) Placeholder debt burn-down with thresholds (P2)

### Why this matters
Documentation ambiguity is currently large enough to mask implementation drift.

### Actions

- Use `tools/ci/report_placeholder_markers.py` threshold mode in non-blocking monitor first.
- Set rolling thresholds for top 10 high-marker docs (not repo-wide hard-fail on day one).
- Reduce `NEEDS VERIFICATION` in root/docs architecture surfaces first.
- Execute file-by-file prioritization from `docs/runbooks/markdown-remediation-plan.md`.

### Definition of done

- Top 10 docs show a sustained downward marker trend across 3 consecutive updates.
- At least one threshold transitions from monitor-only to required CI gate.

## 4) First governed end-to-end artifact path (P3)

### Why this closes the loop
A strong base needs one reproducible path from input to governed output artifact.

### Actions

- Promote one deterministic fixture path:
  - runtime fixture -> policy decision -> rendered summary -> uploaded CI artifact.
- Add artifact integrity assertion (hash/content checks) in CI.

### Definition of done

- A single command reproduces the governed artifact exactly.
- CI validates both generation and integrity of that artifact.

---

## Two-week execution plan (recommended)

### Week 1

1. Establish pinned dependency install path for CI-required boundary tests.
2. Add/expand negative-path boundary tests for ecology routes + UI mapper.
3. Add monitor-mode marker thresholds for top 10 docs.

### Week 2

1. Convert one marker threshold to required gate.
2. Implement and validate one deterministic governed E2E artifact path.
3. Publish progress in `docs/runbooks/repository-next-steps.md` with:
   - pass/fail status,
   - marker trend,
   - remaining blockers.

## Progress scorecard fields

Use these in weekly updates:

- Strict CI reproducibility status (`PASS/FAIL`)
- Boundary contract negative-path coverage status (`PASS/FAIL`)
- Top-10 marker trend (`UP/DOWN/FLAT`)
- Enforced marker thresholds count
- Governed E2E artifact reproducibility status (`PASS/FAIL`)
