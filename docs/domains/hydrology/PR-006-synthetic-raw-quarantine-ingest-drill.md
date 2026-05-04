# PR-006 Synthetic RAW/QUARANTINE Ingest Drill

CONFIRMED: synthetic mock fetch output can flow to RAW, malformed input routes to QUARANTINE, and valid RAW can normalize to WORK.
CONFIRMED: RAW/WORK/QUARANTINE and associated receipts are internal-only and not EvidenceBundle support.
CONFIRMED: promotion dry run is denied before evidence closure.
PROPOSED: PR-007 synthetic PROCESSED/CATALOG closure drill.
