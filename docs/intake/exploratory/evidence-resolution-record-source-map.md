# EvidenceResolutionRecord source adaptation

Status: PROPOSED implementation candidate.

The KFM Pipeline Living Implementation Manual v0.3 names `EvidenceResolutionRecord` as a distinct control-loop artifact between query/retrieval and candidate compilation. Current repository reconciliation confirmed `QueryRunRecord` and `RecompileManifest` executable profiles but found no executable `EvidenceResolutionRecord` contract/schema/validator family.

This slice implements only the missing deterministic, fixture-only record. It does not create a live resolver, source fetcher, policy engine, EvidenceBundle, lifecycle writer, promotion path, release, deployment, or publication surface.

Directory Rules basis: semantic meaning is under `contracts/governance/`; machine shape under `schemas/contracts/v1/governance/`; synthetic examples under `fixtures/contracts/v1/governance/`; operational validation under `tools/validators/governance/`; executable proof under `tests/validators/governance/`; hosted orchestration under `.github/workflows/`.
