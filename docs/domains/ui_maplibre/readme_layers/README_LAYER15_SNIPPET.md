## Layer 15: Governed Pipeline Orchestrator

This layer orchestrates existing Layers 1-14 and does not reimplement their domain logic.

### CLI examples
- plan-only: `python soilgrids_pipeline_orchestrator.py --pipeline-spec pipeline_specs/soilgrids_pipeline_example.json --run-root pipeline_runs --mode plan-only`
- dry-run: `python soilgrids_pipeline_orchestrator.py --pipeline-spec pipeline_specs/soilgrids_pipeline_example.json --run-root pipeline_runs --mode dry-run`
- execute-local: `python soilgrids_pipeline_orchestrator.py --pipeline-spec pipeline_specs/soilgrids_pipeline_example.json --run-root pipeline_runs --mode execute-local`
- replay: `python soilgrids_pipeline_orchestrator.py --pipeline-spec pipeline_specs/soilgrids_pipeline_example.json --run-root pipeline_runs --mode replay`
- certify: `python soilgrids_pipeline_orchestrator.py --pipeline-run-manifest pipeline_runs/<run_id>/pipeline_run_manifest.json --run-root pipeline_runs --mode certify`

### Key artifacts
- PipelineSpec.v1, PipelinePlan.v1, PipelineRunManifest.v1, PipelineRunReceipt.v1
- ReproducibilityReport.v1, PipelineCertificationEnvelope.v1
- checksums.sha256 and append-only ledger entries

### Run directory layout
See `pipeline_runs/<run_id>/` for plan, manifest, receipts, stage logs, exports, and checksum file.

### Exit codes
- `0` success/planned
- `5` dry-run success
- `40` stage failure
- `80` certification failure
- `120` internal error
