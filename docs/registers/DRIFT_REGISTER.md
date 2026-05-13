# DRIFT REGISTER
- 2026-05-09: PROPOSED shift: common/evidence/runtime schema placeholders replaced with first typed shapes.
- 2026-05-09: NEEDS VERIFICATION PR-001 `$id` URL-to-file-path inspection found zero mismatches under `schemas/contracts/v1/**/*.schema.json`.

- 2026-05-12: CONFIRMED blocking drift: required doctrine artifacts for evidence-first comparison are not present in mounted repo snapshot (`KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf`, `Master_MapLibre_Components-Functions-Features.pdf`, `Kansas_Frontier_Matrix_Definitive_Greenfield_Building_Plan_v1_1.pdf`); impact: doctrine-vs-implementation gap analysis cannot be completed from primary sources; resolution path: add canonical artifacts (or approved canonical links with provenance) and re-run extraction.

- 2026-05-12: CONFIRMED remediation staged: added governance gate scaffolding for required doctrine artifacts (`control_plane/document_registry_doctrine_required.yaml`, `policy/source/doctrine_artifact_required.rego`, schema+fixtures+tests+validator script). Blocking status remains until artifacts themselves are admitted.
- 2026-05-13: CONFIRMED blocker resolved: required doctrine artifact filenames now exist under `docs/doctrine/artifacts/` and `control_plane/document_registry_doctrine_required.yaml` statuses have been updated to `present`; doctrine prerequisite gate can now be executed in pass mode.
