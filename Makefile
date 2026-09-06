# KFM repository orchestration surface.
#
# Implemented targets below invoke repository-owned commands. Readiness-marker
# targets print TODO output and are intentionally non-enforcing; their zero exit
# status is not validation evidence. Several CI workflows inspect those marker
# bodies to detect when an implementation has landed and must be wired through
# a separately reviewed change.

.DEFAULT_GOAL := help

KFM_VALIDATION_ENV := KFM_NO_NETWORK=1 PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 TZ=UTC
VALIDATOR_ORCHESTRATOR := python tools/validate_all.py

.PHONY: help validate test schemas validators validator-list validator-full validator-focused validator-release-profile validator-changed-area validator-registry-check workflow-security repository-topology repository-governance-parity repository-guardrails trust-spine-baseline program-baseline control-plane-registry-packet trust-spine-fixture-slice ci-conformance-report policy fixtures release-dry-run proof-slice catalog publish-check evidence-resolver evidence-resolver-deny hazards-validate deny-test ui-build api-run governed-api-dev governed-api-smoke governed-api-verify boundary-guards boundary-guards-ci maplibre-perf maplibre-govern maplibre-proof maplibre-clean

help:
	@echo "KFM repository targets"
	@echo
	@echo "Implemented validation and test targets:"
	@echo "  validate              Run aggregate schema validators and schema/contract tests"
	@echo "  schemas               Run configured aggregate validators against fixtures"
	@echo "  test                  Run repository schema and contract tests"
	@echo "  workflow-security     Test and run the 20-rule workflow-security ratchet"
	@echo "  repository-topology  Test and run the 20-rule directory-topology ratchet"
	@echo "  repository-governance-parity Validate the MRTS-04 parity and inherited-drift profile"
	@echo "  repository-guardrails Run registry, workflow, and topology guardrails"
	@echo "  trust-spine-baseline Validate the pinned MRTS-01 authority baseline packet"
	@echo "  program-baseline     Validate the pinned M01 program baseline packet"
	@echo "  control-plane-registry-packet Validate the seven MRTS-02 registry projections"
	@echo "  trust-spine-fixture-slice Validate the synthetic MRTS-05 cross-family flow"
	@echo "  ci-conformance-report Validate the deterministic blocked MRTS-06 handoff"
	@echo "  hazards-validate      Run bounded synthetic USDM materiality validation"
	@echo "  governed-api-smoke    Run governed API tests"
	@echo "  governed-api-verify   Run governed API tests and enforce its import boundary"
	@echo "  boundary-guards       Run policy/API boundary tests"
	@echo "  boundary-guards-ci    Run boundary tests with JUnit output"
	@echo "  deny-test             Run bounded public route, store, and runtime-import guards"
	@echo "  ui-build              Build the Explorer Web baseline"
	@echo "  maplibre-perf         Run MapLibre performance smoke and build artifacts"
	@echo "  maplibre-govern       Validate MapLibre performance governance"
	@echo "  maplibre-proof        Build and validate the MapLibre performance ProofPack"
	@echo "  publish-check         Run bounded promotion-gate fixtures and tests"
	@echo "  release-dry-run       Prove five synthetic publication-denial paths"
	@echo "  evidence-resolver     Run the bounded internal evidence candidate profile"
	@echo "  evidence-resolver-deny Run its fail-closed negative fixture suite"
	@echo
	@echo "Registry-driven validator profiles (finite checker outcomes only):"
	@echo "  validators            Alias of validator-full"
	@echo "  validator-list        List profiles and registered validator IDs"
	@echo "  validator-full        Run every registered validator once"
	@echo "  validator-focused     Run the focused trust-spine profile"
	@echo "  validator-release-profile Run the release-adjacent fixture profile; no release effect"
	@echo "  validator-changed-area Select validators from CHANGED_PATH_FILE; fail when none match"
	@echo "  validator-registry-check Validate the registry without running validators"
	@echo
	@echo "Implemented local runtime targets:"
	@echo "  api-run               Start the governed API locally (alias of governed-api-dev)"
	@echo "  governed-api-dev      Start the governed API module directly"
	@echo
	@echo "Readiness markers (print TODO; do not enforce readiness):"
	@echo "  policy                Policy-engine test lane"
	@echo "  fixtures              Deterministic fixture regeneration"
	@echo "  proof-slice           Hydrology proof-slice pipeline"
	@echo "  catalog               Catalog record builder"
	@echo
	@echo "Cleanup targets:"
	@echo "  maplibre-clean        Remove artifacts/perf"

validate:
	$(MAKE) schemas test

schemas:
	python tools/validators/_common/run_all.py

test:
	python -m pytest tests/schemas tests/contracts -q

# Canonical registry-driven validator profiles. The historical `schemas` target
# remains a workflow-compatible surface and delegates through its compatibility
# wrapper; new operator-facing profile targets use tools/validate_all.py.
validators: validator-full

validator-list:
	$(KFM_VALIDATION_ENV) $(VALIDATOR_ORCHESTRATOR) --list

validator-full:
	$(KFM_VALIDATION_ENV) $(VALIDATOR_ORCHESTRATOR) --profile full

validator-focused:
	$(KFM_VALIDATION_ENV) $(VALIDATOR_ORCHESTRATOR) --profile focused

validator-release-profile:
	$(KFM_VALIDATION_ENV) $(VALIDATOR_ORCHESTRATOR) --profile release-dry-run

validator-changed-area:
	@if [ -z "$(CHANGED_PATH_FILE)" ]; then \
		echo "ERROR: set CHANGED_PATH_FILE to a newline-delimited repository path list" >&2; \
		exit 2; \
	fi
	$(KFM_VALIDATION_ENV) $(VALIDATOR_ORCHESTRATOR) --profile changed-area --changed-path-file "$(CHANGED_PATH_FILE)" --require-match

validator-registry-check:
	$(KFM_VALIDATION_ENV) $(VALIDATOR_ORCHESTRATOR) --validate-registry

workflow-security:
	KFM_NO_NETWORK=1 PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 TZ=UTC python -m unittest discover --start-directory tests/validators/governance --pattern 'test_validate_workflow_security.py' --verbose
	KFM_NO_NETWORK=1 PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 TZ=UTC python tools/validators/governance/validate_workflow_security.py --format text

repository-topology:
	KFM_NO_NETWORK=1 PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 TZ=UTC python -m unittest discover --start-directory tests/validators/directory_governance --pattern 'test_validate_*topology.py' --verbose
	KFM_NO_NETWORK=1 PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 TZ=UTC python tools/validators/directory_governance/render_repository_topology_diagnostics.py

repository-governance-parity:
	$(KFM_VALIDATION_ENV) python -m unittest tests.validators.directory_governance.test_validate_repository_governance_parity --verbose
	$(KFM_VALIDATION_ENV) python tools/validators/directory_governance/validate_repository_governance_parity.py --fixtures
	$(KFM_VALIDATION_ENV) python tools/validators/directory_governance/validate_repository_governance_parity.py
	$(KFM_VALIDATION_ENV) python tools/validators/validate_generated_receipt.py data/receipts/generated/genrec-repository-governance-parity-mrts-04-20260822.json --repo-root . --artifact-git-ref f7c6ba4c73227858c2d7c8931adae37b57092ce1

repository-guardrails: validator-registry-check workflow-security repository-topology

trust-spine-baseline:
	$(KFM_VALIDATION_ENV) python -m unittest discover --start-directory tests/validators --pattern 'test_validate_trust_spine_baseline.py' --verbose
	$(KFM_VALIDATION_ENV) python tools/validators/control_plane/validate_trust_spine_baseline.py --fixtures
	$(KFM_VALIDATION_ENV) python tools/validators/control_plane/validate_trust_spine_baseline.py
	$(KFM_VALIDATION_ENV) python tools/validators/validate_generated_receipt.py data/receipts/generated/genrec-trust-spine-baseline-control-plane-successor-20260822.json --repo-root . --artifact-git-ref 236bdaf81b001d434726bd9ec7b0664c8ec0be83

program-baseline:
	$(KFM_VALIDATION_ENV) python -m unittest discover --start-directory tests/validators --pattern 'test_validate_program_baseline.py' --verbose
	$(KFM_VALIDATION_ENV) python tools/validators/control_plane/validate_program_baseline.py --fixtures
	$(KFM_VALIDATION_ENV) python tools/validators/control_plane/validate_program_baseline.py
	$(KFM_VALIDATION_ENV) python tools/validators/validate_generated_receipt.py data/receipts/generated/genrec-program-baseline-m01-20260822.json --repo-root .

control-plane-registry-packet:
	$(KFM_VALIDATION_ENV) python -m unittest discover --start-directory tests/validators --pattern 'test_validate_control_plane_registry_packet.py' --verbose
	$(KFM_VALIDATION_ENV) python tools/validators/control_plane/validate_control_plane_registry_packet.py --fixtures
	$(KFM_VALIDATION_ENV) python tools/validators/control_plane/validate_control_plane_registry_packet.py
	$(KFM_VALIDATION_ENV) python tools/validators/validate_generated_receipt.py data/receipts/generated/genrec-control-plane-registry-packet-rebased-20260822.json --repo-root . --artifact-git-ref 236bdaf81b001d434726bd9ec7b0664c8ec0be83

trust-spine-fixture-slice:
	$(KFM_VALIDATION_ENV) python -m unittest tests.validators.governance.test_validate_trust_spine_fixture_slice --verbose
	$(KFM_VALIDATION_ENV) python tools/validators/governance/validate_trust_spine_fixture_slice.py --fixtures
	$(KFM_VALIDATION_ENV) python tools/validators/governance/validate_trust_spine_fixture_slice.py
	$(KFM_VALIDATION_ENV) python tools/validators/validate_generated_receipt.py data/receipts/generated/genrec-trust-spine-fixture-slice-mrts-05-20260822.json --repo-root . --artifact-git-ref f2d5ec5f34c97beaedca96f1ea7cce84b3643b67

ci-conformance-report:
	$(KFM_VALIDATION_ENV) python -m unittest tests.validators.test_validate_generated_receipt --verbose
	$(KFM_VALIDATION_ENV) python -m unittest tests.validators.governance.test_validate_ci_conformance_report --verbose
	$(KFM_VALIDATION_ENV) python tools/validators/governance/validate_ci_conformance_report.py --fixtures
	$(KFM_VALIDATION_ENV) python tools/validators/governance/validate_ci_conformance_report.py
	$(KFM_VALIDATION_ENV) python tools/validators/validate_generated_receipt.py data/receipts/generated/genrec-ci-conformance-report-mrts-06-20260822.json --repo-root . --artifact-git-ref 7a6433c931de91f605450aa6ca59b833061f3984

hazards-validate:
	KFM_NO_NETWORK=1 PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 TZ=UTC python -m unittest discover --start-directory tests/domains/hazards --pattern 'test_validate_usdm_materiality.py' --verbose
	KFM_NO_NETWORK=1 PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 TZ=UTC python tools/validators/domains/hazards/validate_usdm_materiality.py --fixtures

# Readiness markers preserve exact TODO bodies consumed by repository workflows.
# They are discovery surfaces only and must not be cited as executable proof.
policy:
	@echo "TODO: opa test policy/ -v"

fixtures:
	@echo "TODO: regenerate deterministic fixtures"

proof-slice:
	@echo "TODO: pipelines/hydrology proof slice"

catalog:
	@echo "TODO: tools/catalog_builders build catalog records from validated processed outputs"

release-dry-run:
	KFM_NO_NETWORK=1 PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 TZ=UTC python tools/release/release_dry_run.py
	KFM_NO_NETWORK=1 PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 TZ=UTC python -m unittest -q tests.release.test_publication_deny_dry_run

publish-check:
	KFM_NO_NETWORK=1 PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 TZ=UTC python tools/validators/validate_review_record.py --fixtures
	KFM_NO_NETWORK=1 PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 TZ=UTC python tools/validators/validate_promotion_gate.py --fixtures
	KFM_NO_NETWORK=1 PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 TZ=UTC python -m unittest -q tests.release.test_review_record
	KFM_NO_NETWORK=1 PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 TZ=UTC python -m unittest -q tests.release.test_promotion_gate

evidence-resolver:
	KFM_NO_NETWORK=1 PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 TZ=UTC python tools/validators/evidence_resolver/validate_candidate.py --fixtures fixtures/packages/evidence_resolver/v1alpha1
	KFM_NO_NETWORK=1 PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 TZ=UTC python -m unittest discover -s tests/packages/evidence_resolver -p 'test_*.py' -q

evidence-resolver-deny:
	KFM_NO_NETWORK=1 PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 TZ=UTC python tools/validators/evidence_resolver/validate_candidate.py --fixtures fixtures/packages/evidence_resolver/v1alpha1 --negative-only
	KFM_NO_NETWORK=1 PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 TZ=UTC python -m unittest discover -s tests/packages/evidence_resolver -p 'test_*.py' -q

deny-test:
	PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 TZ=UTC PYTHONPATH=apps/governed-api/src python -m pytest -q --strict-config --strict-markers apps/governed-api/tests/test_boundary_guards.py

ui-build:
	pnpm --filter explorer-web build

api-run: governed-api-dev

governed-api-dev:
	PYTHONPATH=apps/governed-api/src python -m governed_api.main

governed-api-smoke:
	python -m pytest apps/governed-api/tests -q

governed-api-verify:
	python -m pytest apps/governed-api/tests -q
	@if git grep -nE "^(import|from) (maplibre|cesium|ollama)" apps/governed-api/; then \
		echo "DENY: governed API imports a forbidden renderer or model client" >&2; \
		exit 1; \
	else \
		status=$$?; \
		if [ "$$status" -ne 1 ]; then exit "$$status"; fi; \
		echo "PASS: governed API import boundary is intact"; \
	fi

boundary-guards:
	python -m pytest -q tests/policy/test_control_plane_register_meta_contract.py tests/policy/test_explorer_web_adapter_boundary.py tests/policy/test_pipeline_connector_non_publisher.py apps/governed-api/tests/test_boundary_guards.py

boundary-guards-ci:
	mkdir -p artifacts/qa
	python -m pytest -q --junitxml=artifacts/qa/policy-boundary-guards.xml tests/policy/test_control_plane_register_meta_contract.py tests/policy/test_explorer_web_adapter_boundary.py tests/policy/test_pipeline_connector_non_publisher.py apps/governed-api/tests/test_boundary_guards.py

maplibre-perf:
	node scripts/maplibre-smoke-perf.mjs
	node scripts/build-maplibre-render-diff.mjs
	node scripts/attest-maplibre-perf.mjs
	node scripts/build-maplibre-perf-release-manifest.mjs

maplibre-govern:
	python3 tools/validators/maplibre/validate_perf_governance.py

maplibre-proof:
	node scripts/build-maplibre-perf-proof-pack.mjs
	python3 tools/validators/maplibre/validate_perf_proof_pack.py \
		artifacts/perf/proof-pack.maplibre-perf.json
	node scripts/build-maplibre-perf-release-manifest.mjs
	python3 tools/validators/maplibre/validate_perf_governance.py

maplibre-clean:
	rm -rf -- artifacts/perf
