# Markdown Structure Build Notes (2026-04-08)

Summary of repository scaffolding added to align with markdown-linked structure.

## Added directory scaffolding

- `apps/api/`, `apps/api/src/api/`, `apps/api/tests/`, `apps/ui/`
- `contracts/vocab/`, `data/specs/`
- `docs/analyses/archaeology/results/notebooks/{spatial,temporal,environmental,cultural-landscapes,artifacts,geophysics,predictive}/`
- `docs/analyses/archaeology/results/paleoenvironment/{climate,paleohydrology,vegetation,seasonality,drought-cycles,predictive,uncertainty,metadata,provenance,stac}/`
- `docs/analyses/remote-sensing/change-detection/{methods,results,reports}/`
- `docs/analyses/remote-sensing/validation/{methods,results}/`
- `docs/analyses/remote-sensing/sar-lidar-fusion/`
- `docs/domains/{agriculture,archives-heritage,atmosphere,ecology,hazards,history-mobility,land-tenure,settlement-services,transport}/`
- `docs/research/drafts/{assets,literature}/`
- `docs/research/source_summaries/{_attachments,by_domain}/`
- `infra/monitoring/{dashboards,otel}/`
- `policy/bundles/runtime/`, `web/`

## Added placeholders

- README placeholders for all newly created directories.
- Placeholder docs where markdown links referenced missing files:
  - `docs/analyses/_templates/analysis_readme.md`
  - `docs/analyses/ecology/ecosystem-services.md`
  - `docs/analyses/ecology/landcover-analysis.md`
  - `docs/analyses/remote-sensing/change-detection/governance.md`
  - `docs/analyses/remote-sensing/validation/governance.md`
  - `docs/runbooks/{correction.md,publication.md,rollback.md,stale_projection.md}`
  - `docs/standards/governance/ROOT-GOVERNANCE.md`
  - `pipelines/ssurgo_to_catchment.md`
