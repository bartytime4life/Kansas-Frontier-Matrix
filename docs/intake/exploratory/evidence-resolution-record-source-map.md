# EvidenceResolutionRecord source adaptation

Status: IMPLEMENTED as a bounded `PROPOSED_INACTIVE` / `FIXTURE_ONLY` profile.

Reconciled against `main@2d0c9a8e4072ce14cb71404585e85fbc86339e12` on 2026-08-25. The proposal lineage is *Kansas Frontier Matrix Pipeline Living Implementation Manual*, v0.3 (2026-04-30), §8 “Canonical object families,” PDF and printed p. 7. The manual names `EvidenceResolutionRecord` as a proposed control-loop artifact and explicitly reports repository implementation as unknown in that source session.

The earlier absence statement is superseded by current executable repository evidence. The bounded profile now exists as:

- semantic contract: [`contracts/governance/evidence_resolution_record.md`](../../../contracts/governance/evidence_resolution_record.md);
- machine shape: [`schemas/contracts/v1/governance/evidence_resolution_record.schema.json`](../../../schemas/contracts/v1/governance/evidence_resolution_record.schema.json);
- synthetic cases: [`fixtures/contracts/v1/governance/evidence_resolution_record/cases.json`](../../../fixtures/contracts/v1/governance/evidence_resolution_record/cases.json);
- deterministic validator: [`tools/validators/governance/validate_evidence_resolution_record.py`](../../../tools/validators/governance/validate_evidence_resolution_record.py);
- focused proof: [`tests/validators/governance/test_evidence_resolution_record.py`](../../../tests/validators/governance/test_evidence_resolution_record.py); and
- read-only workflow: [`.github/workflows/evidence-resolution-record.yml`](../../../.github/workflows/evidence-resolution-record.yml).

The record preserves finite `COMPLETE`, `PARTIAL`, `UNRESOLVED`, `DENIED`, and `ERROR` outcomes and fixes every authority-effect flag to `false`. It does not create a live resolver, source fetcher, policy engine, EvidenceBundle, lifecycle writer, promotion path, release, deployment, or publication surface.

Accepted ADR-0029 and the adopted Directory Rules support the existing placement: meaning under `contracts/governance/`, shape under `schemas/contracts/v1/governance/`, synthetic replay under `fixtures/`, operational validation under `tools/validators/governance/`, proof under `tests/validators/governance/`, and orchestration under `.github/workflows/`. This reconciliation changes only the source map; no packet file, registry, manifest, compatibility surface, or authority home changes.
