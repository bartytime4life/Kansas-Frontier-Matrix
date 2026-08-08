# Representation fitness assessment source adaptation

Status: PROPOSED implementation candidate.

KFM Components Pass 18 identifies representation and fitness-for-use acceptance criteria as an implementation gap. Current repository reconciliation found a mature fixture-first `RepresentationReceipt` family that records transformation fidelity, information loss, evidence binding, represented time, reality-boundary linkage, and correction lineage, but no cross-domain fitness assessment for one declared use.

This slice therefore adds only a read-only compatibility assessment over declared representation metadata. It does not modify `RepresentationReceipt`, decide evidence truth, execute policy, determine professional fitness, authorize a source, write lifecycle state, promote, release, deploy, publish, or authorize public use.

The fixture profile checks bounded combinations of intended use, source role, fidelity, geometry character, scale range, temporal coverage, EvidenceRef presence, and synthetic reality-boundary linkage. `FIT` means only internal compatibility with this proposed profile; `HOLD` preserves an unsupported use without silently upgrading it.

Directory Rules basis: meaning under `contracts/map/`; shape under `schemas/contracts/v1/map/`; synthetic replay under `fixtures/contracts/v1/map/`; validation under `tools/validators/map/`; tests under `tests/validators/map/`; CI under `.github/workflows/`.
