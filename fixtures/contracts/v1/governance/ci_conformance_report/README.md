# CIConformanceReport fixtures

This directory contains deterministic negative mutations for the MRTS-06
milestone report. The canonical blocked report in
`artifacts/qa/validation/milestone-1/ci_conformance_report.json` is the valid
fixture. `cases.json` mutates it in memory and pins exact finding codes.

The fixtures use repository-local bytes only. They do not create hosted-run,
review, merge, release, deployment, promotion, publication, public-route, or
milestone-closure evidence.
