# DRIFT REGISTER
- 2026-05-09: PROPOSED shift: common/evidence/runtime schema placeholders replaced with first typed shapes.
- 2026-05-09: NEEDS VERIFICATION PR-001 `$id` URL-to-file-path inspection found zero mismatches under `schemas/contracts/v1/**/*.schema.json`.

- 2026-05-12: CONFIRMED blocking drift: required doctrine artifacts for evidence-first comparison are not present in mounted repo snapshot (`KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf`, `Master_MapLibre_Components-Functions-Features.pdf`, `Kansas_Frontier_Matrix_Definitive_Greenfield_Building_Plan_v1_1.pdf`); impact: doctrine-vs-implementation gap analysis cannot be completed from primary sources; resolution path: add canonical artifacts (or approved canonical links with provenance) and re-run extraction.

- 2026-05-12: CONFIRMED remediation staged: added governance gate scaffolding for required doctrine artifacts (`control_plane/document_registry_doctrine_required.yaml`, `policy/source/doctrine_artifact_required.rego`, schema+fixtures+tests+validator script). Blocking status remains until artifacts themselves are admitted.
- 2026-05-13: CONFIRMED blocker resolved: required doctrine artifact filenames now exist under `docs/doctrine/artifacts/` and `control_plane/document_registry_doctrine_required.yaml` statuses have been updated to `present`; doctrine prerequisite gate can now be executed in pass mode.
- 2026-05-13: CONFIRMED integrity drift: admitted doctrine artifacts currently fail minimum-integrity checks (tiny files and duplicate hashes), so doctrine extraction remains blocked until canonical artifacts or canonical linked provenance records are supplied.
- 2026-05-13: CONFIRMED correction: placeholder doctrine PDFs were removed and registry statuses reset to `missing`; doctrine gate remains blocked pending canonical artifact admission or approved canonical-link provenance records.
- 2026-05-13: CONFIRMED provenance drift: current doctrine provenance registry uses placeholder `example.org` source URLs; canonical-link admission path remains blocked until real authoritative source URLs are recorded.
- 2026-05-15: CONFIRMED naming drift surfaced in Wave 1 discovery: Directory Rules references `docs/registers/AUTHORITY_LADDER.md` and `docs/registers/OBJECT_FAMILY_MAP.md`, while repository prior state used `docs/registers/OBJECT_FAMILY.md` plus only YAML authority ladder in `control_plane/authority_ladder.yaml`; Wave 1 added PROPOSED Markdown scaffolds for naming parity pending steward confirmation.
- 2026-05-15: CONFIRMED artifact-path drift for required inputs in this run: doctrine filenames used spaces/case variants (`docs/DomainDriven Design Reference.pdf`, `docs/New Ideas 5-8-26.pdf`) and one atlas delivered as Markdown (`docs/KFM_Domains_Culmination_Atlas_v1_1.md`) instead of the exact required PDF path names; run proceeded using explicitly approved substitutes.

- 2026-05-15: CONFIRMED evidence-claim drift: `control_plane/normalized_summary_consumer_readiness.yaml` previously marked consumer checks as `validated` with specific evidence labels; this run demoted those entries to `needs_verification`/`UNKNOWN` pending executable proof in current branch context.

- 2026-05-15: CONFIRMED provenance-placeholder drift remediated: `control_plane/doctrine_artifact_provenance_sources.yaml` no longer carries synthetic `example.org` links; `source_url` values set to `NEEDS_VERIFICATION` until steward-approved authoritative URLs are admitted.

- 2026-05-15: CONFIRMED status-normalization drift remediated: `control_plane/document_registry_doctrine_required.yaml` artifact states changed from `missing` to `needs_verification` to distinguish absent evidence from unresolved canonical-path/provenance validation.

- 2026-05-15: CONFIRMED execution drift: in-branch run of `pytest -q tests/policy/test_preflight_summary_consistency.py` failed (2 failed / 3 passed) with `render_returncode: 2` and `render_stderr: skipped_due_to_check_error`; readiness state for the mapped consumer remains non-validated.

- 2026-05-15: CONFIRMED readiness-state reconciliation: `control_plane/normalized_summary_consumer_readiness.yaml` now reflects branch-local outcomes (`passing` for doctrine artifact suite, `failing` for policy preflight consistency) instead of blanket `needs_verification` placeholders.
