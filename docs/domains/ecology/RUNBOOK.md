# Ecology Operator Runbook

## 1. Purpose

This runbook defines the manual operator path for ecology validations now that gate scripts exist. Use it to run fixture checks, release checks, and Focus Mode checks in a deterministic, fail-closed order before promotion or publication.

## 2. When to run

Run this sequence when any of the following happens:

- A change lands in ecology validators, ecology fixtures, or governed ecology runtime code.
- A candidate ecology release is being prepared or re-validated.
- A CI failure needs local reproduction and failure decoding.
- A policy/sensitivity-related ecology incident requires a confidence rebuild before re-release.

## 3. Prerequisites

- Run from repository root.
- Python runtime available on `python`.
- Ecology validator present:
  - `tools/validators/ecology/validate_ecology_bundle.py`
- Required directories/files exist for each gate:
  - Fixture gate: `tests/fixtures/ecology/valid`, `tests/fixtures/ecology/invalid`
  - Release gate: `data/processed/ecology`, `data/triplets/ecology`, `data/published/ecology`
  - Focus Mode gate: `apps/governed_api/ecology/focus_mode.py`, `tests/fixtures/ecology/focus_mode/*.json`

## 4. Validation sequence

Run gates in this order to narrow blast radius and speed triage:

1. **Fixture baseline**
   ```bash
   tools/validators/ecology/run_ecology_fixture_checks.sh
   ```
2. **Release artifact integrity**
   ```bash
   tools/validators/ecology/run_ecology_release_checks.sh
   ```
3. **Focus Mode runtime behavior**
   ```bash
   tools/validators/ecology/run_ecology_focus_mode_checks.sh
   ```

Operator rule: do not continue to the next step when the current step fails.

## 5. Expected outputs

- Fixture gate should end with:
  - `✓ All ecology fixture checks passed`
- Release gate should end with:
  - `✓ All ecology release checks passed`
- Focus Mode gate should end with:
  - `✓ Ecology Focus Mode checks completed`
- Focus Mode execution should print three response paths for:
  - valid request,
  - deny-sensitive request,
  - abstain-missing-evidence request.

## 6. Common failures and fixes

- **`ERROR: validator not found ... validate_ecology_bundle.py`**
  - Fix: restore validator path, confirm branch includes ecology validator assets, and rerun from repo root.
- **Fixture directory missing (valid/invalid)**
  - Fix: restore `tests/fixtures/ecology/valid` and `tests/fixtures/ecology/invalid`; verify fixture filenames and extension are `.json`.
- **Release directory glob resolves to no files**
  - Fix: ensure release candidate artifacts are staged in `data/processed/ecology`, `data/triplets/ecology`, and `data/published/ecology`.
- **`ERROR: Focus Mode runtime not found ... focus_mode.py`**
  - Fix: restore runtime module path or align script path to the runtime location used by the lane.
- **Validator reports expectation mismatch (`--expect pass` or `--expect fail`)**
  - Fix: inspect changed bundle(s), schema/policy fields, and sensitivity markers; either repair artifact content or update fixture intent explicitly.
- **Focus Mode deny/abstain behavior regresses**
  - Fix: review decision-envelope/evidence resolution logic and re-run fixture + release gates before re-running Focus Mode.

## 7. Release checklist

Before ecology release promotion:

- [ ] Fixture gate is green.
- [ ] Release gate is green.
- [ ] Focus Mode gate is green.
- [ ] Any deny/abstain outcomes are expected and documented.
- [ ] Evidence and release artifacts in ecology directories match the intended candidate set.
- [ ] Gate outputs/logs are attached to change review or release record.

## 8. Rollback / correction path

If any gate fails after a candidate was prepared:

1. Stop promotion/publication for ecology artifacts.
2. Record the exact failing gate, command, and first failing bundle/runtime request.
3. Revert or patch offending validator/runtime/artifact changes.
4. Re-run full sequence from fixture gate onward.
5. Publish corrected candidate only after all three gates pass.
6. If a bad artifact was already published, withdraw it, restore last known-good release set, and rerun release + Focus Mode checks to confirm recovery.
