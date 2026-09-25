# KFM repository orchestration surface.
#
# Implemented targets below invoke repository-owned commands. Bounded readiness
# targets delegate to the reviewed readiness registry. A named HOLD exits 3 and
# must not be cited as validation, release, deployment, or publication evidence.

.DEFAULT_GOAL := help

KFM_VALIDATION_ENV := KFM_NO_NETWORK=1 PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 TZ=UTC
VALIDATOR_ORCHESTRATOR := python tools/validate_all.py

.PHONY: normalized-summary-check

.PHONY: local-data-check local-data-doctor

.PHONY: offline-pipeline-check native-explorer-check

# Existing synthetic pipeline implementations only. The injected guard covers
# named Python egress APIs; PROJ disables native grid retrieval separately.
offline-pipeline-check:
	$(KFM_VALIDATION_ENV) PROJ_NETWORK=OFF PYTHONPATH="$(CURDIR)/tools/ci/kfm_no_network:$(CURDIR)" python -m pytest -q -p no:cacheprovider --strict-config --strict-markers tests/pipelines tests/domains/hydrology/test_no_network_proof.py

# Retired repository mirror. Keep a fail-closed compatibility target so a
# request for the old app check cannot report a passing result.
native-explorer-check:
	@echo "WORKFLOW_HOLD: the legacy monorepo Explorer app was retired; use the separate live Site source branch"; exit 3

local-data-check:
	$(KFM_VALIDATION_ENV) PYTHONPATH="$(CURDIR)/tools/ci/kfm_no_network:$(CURDIR)" python -m pytest -q -p no:cacheprovider --strict-config --strict-markers tests/local_data

local-data-doctor:
	python3 tools/local_data/doctor.py

# Bounded doctrine summary regressions; no cutover or readiness authority.
normalized-summary-check:
	$(KFM_VALIDATION_ENV) python tools/validators/source/validate_doctrine_artifact_preflight_summary.py --fixtures
	$(KFM_VALIDATION_ENV) python -m pytest -q -p no:cacheprovider --strict-config --strict-markers tests/policy/test_preflight_summary_consistency.py tests/policy/test_normalized_summary_consumer_readiness.py tests/policy/test_run_doctrine_artifact_preflight.py tests/policy/test_preflight_summary_schema_contract.py tests/source/test_doctrine_artifact_preflight_summary_schema.py tests/ci/test_normalized_summary_workflow.py

.PHONY: help validate test schemas validators validator-list validator-full validator-focused validator-release-profile validator-changed-area validator-registry-check docs-critical-structure workflow-security repository-topology repository-governance-parity repository-guardrails trust-spine-baseline program-baseline control-plane-registry-packet trust-spine-fixture-slice ci-conformance-report policy fixtures release-dry-run proof-slice catalog publish-check evidence-resolver evidence-resolver-deny hazards-validate deny-test ui-build api-run governed-api-dev governed-api-smoke governed-api-verify boundary-guards boundary-guards-ci maplibre-perf maplibre-govern maplibre-proof maplibre-clean

help:
	@echo "KFM repository targets"
	@echo
	@echo "Implemented validation and test targets:"
	@echo "  validate              Run aggregate schema validators and schema/contract tests"
	@echo "  schemas               Run configured aggregate validators against fixtures"
	@echo "  test                  Run repository schema and contract tests"
	@echo "  normalized-summary-check Test summary structure, compatibility and CI failure propagation"
	@echo "  local-data-doctor     Inspect local-PC prerequisites without installing or starting services"
	@echo "  local-data-check      Test offline local-data capture, safety, and recovery"
	@echo "  offline-pipeline-check Test synthetic ingestion, normalization, replay and rollback boundaries"
	@echo "  native-explorer-check Retired app check (explicit HOLD)"
	@echo "  docs-critical-structure Test and run the critical-document structure sentinel"
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
	@echo "  ui-build              Retired workbench check (explicit HOLD)"
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
	@echo "Bounded readiness lanes (HOLD exits 3):"
	@echo "  policy                Run only the accepted Pass 12 Rego source/test pair"
	@echo "  fixtures              Report fixture-regeneration implementation HOLD"
	@echo "  proof-slice           Report Hydrology proof-producer implementation HOLD"
	@echo "  catalog               Report catalog-builder implementation HOLD"
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

docs-critical-structure:
	$(KFM_VALIDATION_ENV) python -m unittest discover --start-directory tests/validators/docs/critical-structure --pattern 'test_*.py' --verbose
	$(KFM_VALIDATION_ENV) python tools/validators/docs/critical-structure/check_critical_structure.py --repo-root . --format text CONTRIBUTING.md

workflow-security:
	KFM_NO_NETWORK=1 PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 TZ=UTC python -m unittest discover --start-directory tests/validators/governance --pattern 'test_validate_workflow_security.py' --verbose
	KFM_NO_NETWORK=1 PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 TZ=UTC python tools/validators/governance/validate_workflow_security.py --format text

# Independent collection, shared fail-closed outcome. A failing live-index test
# must not prevent the contextualized ratchet from explaining that same drift.
# Record every command status; none is waived. The original test assertions,
# diagnostic implementation and baseline remain unchanged. Cancellation may
# still terminate the process. Revert this target and its focused test together.
repository-topology:
	@set -u; \
	contract_status=0; tests_status=0; register_status=0; diagnostics_status=0; \
	if [ -f tests/ci/test_repository_topology_make_target.py ] && $(KFM_VALIDATION_ENV) python -m unittest discover --start-directory tests/ci --pattern 'test_repository_topology_make_target.py' --verbose; then :; else contract_status=$$?; fi; \
	if $(KFM_VALIDATION_ENV) python -m unittest discover --start-directory tests/validators/directory_governance --pattern 'test_validate_*topology*.py' --verbose; then :; else tests_status=$$?; fi; \
	if $(KFM_VALIDATION_ENV) python -m pytest -q -p no:cacheprovider tests/validators/directory_governance/test_validate_repository_topology_correction_register.py; then :; else register_status=$$?; fi; \
	if $(KFM_VALIDATION_ENV) python tools/validators/directory_governance/render_repository_topology_diagnostics.py; then :; else diagnostics_status=$$?; fi; \
	printf 'repository-topology statuses: contract=%s tests=%s register=%s diagnostics=%s\n' "$$contract_status" "$$tests_status" "$$register_status" "$$diagnostics_status"; \
	if [ "$$contract_status" -ne 0 ] || [ "$$tests_status" -ne 0 ] || [ "$$register_status" -ne 0 ] || [ "$$diagnostics_status" -ne 0 ]; then exit 1; fi

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
	$(KFM_VALIDATION_ENV) python tools/validators/validate_generated_receipt.py data/receipts/generated/genrec-program-baseline-m01-20260822.json --repo-root . --artifact-git-ref d0c4e9a5108c7b0d82372a43f785ae10eeed6895

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
	KFM_NO_NETWORK=1 PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 TZ=UTC python -m unittest discover --start-directory tests/domains/hazards --top-level-directory . --pattern 'test_validate_drought_families.py' --verbose
	KFM_NO_NETWORK=1 PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 TZ=UTC python tools/validators/hazards/validate_drought_families.py --fixtures

# Bounded readiness lanes. Policy executes only the accepted Pass 12 pair.
# Unimplemented producers return a named HOLD with exit status 3.
policy:
	$(KFM_VALIDATION_ENV) python tools/readiness/run_lane.py policy

fixtures:
	$(KFM_VALIDATION_ENV) python tools/readiness/run_lane.py fixtures

proof-slice:
	$(KFM_VALIDATION_ENV) python tools/readiness/run_lane.py proof-slice

catalog:
	$(KFM_VALIDATION_ENV) python tools/readiness/run_lane.py catalog

release-dry-run:
	KFM_NO_NETWORK=1 PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 TZ=UTC python tools/release/release_dry_run.py
	KFM_NO_NETWORK=1 PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 TZ=UTC python -m unittest -q tests.release.test_publication_deny_dry_run
	KFM_NO_NETWORK=1 PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 TZ=UTC python -m pytest -q tests/release/test_synthetic_release_closure.py

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
	@echo "WORKFLOW_HOLD: the legacy Explorer Web workbench was retired; use the separate live Site source branch"; exit 3

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
	python -m pytest -q tests/policy/test_control_plane_register_meta_contract.py tests/policy/test_pipeline_connector_non_publisher.py apps/governed-api/tests/test_boundary_guards.py

boundary-guards-ci:
	mkdir -p artifacts/qa
	python -m pytest -q --junitxml=artifacts/qa/policy-boundary-guards.xml tests/policy/test_control_plane_register_meta_contract.py tests/policy/test_pipeline_connector_non_publisher.py apps/governed-api/tests/test_boundary_guards.py

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
