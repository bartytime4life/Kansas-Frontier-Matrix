## Layer 12: Audit Evidence Crate + Provenance Graph Compiler

This layer compiles **evidence only** and **never mutates source artifacts**.

### Metadata-only
```bash
python soilgrids_evidence_crate.py \
  --release-manifest published/releases/<release_id>/release_manifest.json \
  --publish-receipt published/releases/<release_id>/publish_receipt.json \
  --crate-root evidence_crates \
  --crate-mode metadata-only \
  --dataset-id soilgrids-v2 \
  --crate-title "SoilGrids Evidence Crate"
```

### Local evidence crate
```bash
python soilgrids_evidence_crate.py --crate-root evidence_crates --crate-mode local-evidence-crate --dataset-id soilgrids-v2 --crate-title "SoilGrids Evidence Crate" --run-receipt raw/wcs/run_receipt.json
```

### Full copy
```bash
python soilgrids_evidence_crate.py --crate-root evidence_crates --crate-mode full-copy --dataset-id soilgrids-v2 --crate-title "SoilGrids Evidence Crate"
```

### Exit codes
- 0 success
- 5 dry-run success
- 10 warning
- 20 chain validation failure
- 30 malformed input
- 90 internal error
