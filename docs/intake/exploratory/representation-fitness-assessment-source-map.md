# Representation fitness assessment source adaptation

Status: IMPLEMENTED as a bounded `PROPOSED_INACTIVE` / `FIXTURE_ONLY` profile.

Reconciled against `main@2d0c9a8e4072ce14cb71404585e85fbc86339e12` on 2026-08-25. The proposal lineage is *KFM Pass 18 — Idea Index, Category Atlas, and Expansion Dossier*, Pass 18, §8.6.49, printed p. 302 (`KFM-P9-IDEA-0003`). That downstream carrier proposes purpose-bound fitness assessment; it does not establish repository authority or implementation status.

The earlier absence statement is superseded by current executable repository evidence. The bounded profile now exists as:

- semantic contract: [`contracts/map/representation_fitness_assessment.md`](../../../contracts/map/representation_fitness_assessment.md);
- machine shape: [`schemas/contracts/v1/map/representation_fitness_assessment.schema.json`](../../../schemas/contracts/v1/map/representation_fitness_assessment.schema.json);
- synthetic cases: [`fixtures/contracts/v1/map/representation_fitness_assessment/cases.json`](../../../fixtures/contracts/v1/map/representation_fitness_assessment/cases.json);
- deterministic validator: [`tools/validators/map/validate_representation_fitness_assessment.py`](../../../tools/validators/map/validate_representation_fitness_assessment.py);
- focused proof: [`tests/validators/map/test_representation_fitness_assessment.py`](../../../tests/validators/map/test_representation_fitness_assessment.py); and
- read-only workflow: [`.github/workflows/representation-fitness-assessment.yml`](../../../.github/workflows/representation-fitness-assessment.yml).

The validator returns finite `FIT`, `HOLD`, or `ERROR` outcomes over declared representation metadata. `FIT` means only internal compatibility with this fixture profile. The packet does not modify `RepresentationReceipt`, decide evidence truth, execute policy, determine professional fitness, authorize a source, write lifecycle state, promote, release, deploy, publish, or authorize public use.

Accepted ADR-0029 and the adopted Directory Rules support the existing placement: meaning under `contracts/map/`, shape under `schemas/contracts/v1/map/`, synthetic replay under `fixtures/`, validation under `tools/validators/map/`, proof under `tests/validators/map/`, and orchestration under `.github/workflows/`. This reconciliation changes only the source map; no packet file, registry, manifest, compatibility surface, or authority home changes.
