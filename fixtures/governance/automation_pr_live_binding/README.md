# Automation PR live-binding fixtures

**Status:** PROPOSED_INACTIVE · synthetic-only · no repository mutation

The live-binding validator is tested with temporary Git repositories created by `tests/validators/test_validate_automation_pr_live_binding.py`. This README exists so the fixture responsibility is explicit without checking in mutable Git-object fixtures or duplicating the canonical `AutomationPrProposal` JSON fixtures.

The test harness creates a synthetic `main` branch, an `automation/` candidate branch, and bounded candidate bytes under `data/work/automation/`. It covers a valid binding plus digest drift, undeclared live paths, paths outside the WORK automation lane, base drift, non-PASS policy outcome, and unsafe executable blob mode.

No real repository branch, pull request, receipt, release, deployment, promotion, publication, or public artifact is created by these tests.
