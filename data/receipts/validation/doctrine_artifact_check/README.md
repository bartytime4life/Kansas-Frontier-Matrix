# doctrine_artifact_check receipts

This folder stores local and CI smoke receipts for the doctrine artifact admission prerequisite gate.

- `run-local-smoke.json` captures the expected fail-closed result while required doctrine PDFs are still missing.
- Downstream CI runs can emit additional receipts keyed by workflow run id.
