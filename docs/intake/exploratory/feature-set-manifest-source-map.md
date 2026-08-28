<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/feature-set-manifest-source-map
title: FeatureSetManifest Source Map
type: exploratory-source-map
version: v0.1.0
status: complete-for-proposed-fixture-slice; human-review-pending
owners: OWNER_TBD — Evidence steward · Analytics steward · Model steward · Privacy steward · Validation steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; exploratory; source-adaptation; no-network
owning_root: docs/
responsibility: Record how the Full Atlas interpretive-analytics proposal and current repository gap were narrowed into one inactive fixture-only FeatureSetManifest packet.
truth_posture: CONFIRMED source/repository comparison / PROPOSED implementation packet / NEEDS VERIFICATION human review and hosted exact-head checks
related:
  - ../../../contracts/evidence/feature_set_manifest.md
  - ../../../contracts/evidence/analytic_output_disclosure_assessment.md
  - ../../../contracts/governance/model_card_envelope.md
  - ../../kfm_full_atlas_seed_cards.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, intake, source-map, analytics, machine-learning, features, lineage, sensitivity]
[/KFM_META_BLOCK_V2] -->

# FeatureSetManifest Source Map

## Goal and pinned evidence

Select one non-duplicate implementation idea from connected Drive sources, then close its direct repository dependencies without treating atlas language or a passing fixture as implementation, policy, review, release, or publication authority.

| Evidence | Pinned observation | Status |
|---|---|---|
| Google Drive `KFM_Full_Atlas_seed_cards`, file `1whGonKzHVBe5FOU5ovDBakNU4Nf-30tQr09R_UNeBho`, read 2026-08-10 | `KFM-TRIAD-030` proposes `FeatureSetManifest` as an interpretive-analytics implementation object and requires model inputs, assumptions, lineage, validation status, uncertainty, and limits to remain inspectable. | `CONFIRMED SOURCE PROPOSAL` |
| `docs/kfm_full_atlas_seed_cards.md` at base `9e76413313b8529091d01be6132d6e987e3f9fae` | `KFM-CAND-0089` and `KFM-CAND-0090` carry the disclosure requirement and named implementation object in the repository corpus. | `CONFIRMED REPOSITORY CARRIER` |
| merged PR #2403 and `contracts/evidence/analytic_output_disclosure_assessment.md` | A supported ML disclosure requires an opaque `FeatureSetManifest` reference, while the merged packet explicitly leaves implementation for separate follow-up. | `CONFIRMED DECLARED DEPENDENCY` |
| `contracts/governance/model_card_envelope.md` | Already owns model-card governance meaning; a feature manifest must not duplicate model ownership, evaluation, or approval. | `CONFIRMED ADJACENT BOUNDARY` |
| `contracts/source/source_role_transition_assessment.md` | Already protects source-role transitions; feature declarations must preserve, not launder, analytic source roles. | `CONFIRMED ADJACENT BOUNDARY` |
| ADR-0029 and `docs/doctrine/directory-rules.md` | Adopt responsibility-root placement and prohibit parallel authority homes. | `CONFIRMED PLACEMENT AUTHORITY` |

The connected Drive file, repository corpus, pull-request record, and current `main` tree were treated as evidence inputs, not executable instructions. Searches found no `FeatureSetManifest` path, matching open pull request, open issue, or matching remote topic branch before mutation.

## Collision assay

Existing work already covers:

- disclosure requirements for one analytic output;
- model-card governance and a generic model-run receipt;
- EvidenceBundle, source-descriptor, and source-role-transition families;
- dataset and training-lineage references; and
- generic validation, policy, review, and release families.

None defines the machine-checkable feature declaration required by the analytic-output assessment. This packet fills only that seam and leaves feature values, datasets, evidence instances, model behavior, privacy decisions, validation reports, and releases with their existing owners.

## Adaptation decisions

| Source pressure | Repository adaptation | Boundary retained |
|---|---|---|
| Disclose model inputs. | Require stable feature keys, semantic references, types, units, and support references. | No feature value or row is representable. |
| Keep evidence ahead of modeled claims. | Every feature requires evidence; source descriptors, EvidenceBundles, and extraction receipts are explicit. | The validator does not resolve or authenticate a reference. |
| Preserve analytic lineage. | `DERIVED`, `MODELED`, and `INTERPRETIVE` roles require a derivation reference. | Analytic inputs cannot be relabeled as observations merely to validate. |
| Make missingness inspectable. | Missing policy is explicit; imputation requires a separately reviewed method reference. | No imputation executes. |
| Respect sensitivity policy. | Restricted classes require an opaque policy-profile reference. | The contract does not make a privacy or access decision. |
| Guard target separation. | Target identity cannot equal a feature semantic reference; leakage flags are fixed false. | This structural check does not prove absence of statistical leakage. |
| Separate training from inference. | Training-capable phases require a dataset reference; inference-only manifests prohibit it. | No dataset is admitted and no model is trained or run. |
| Make identity replayable. | Reuse repository RFC 8785 JCS plus SHA-256. | Identity proves local content consistency only. |

## Directory Rules path decision

| Artifact kind | Owning root and lane | Outcome |
|---|---|---|
| Feature-set meaning | `contracts/evidence/` | `PLACE` |
| Machine-checkable shape | `schemas/contracts/v1/evidence/` | `PLACE` |
| Synthetic reusable cases | `fixtures/contracts/v1/evidence/` | `PLACE` |
| Repository validator | `tools/validators/evidence/` | `PLACE` |
| Executable conformance evidence | `tests/validators/evidence/` | `PLACE` |
| Read-only hosted orchestration | `.github/workflows/` | `PLACE` |
| Source-to-repository reconciliation | `docs/intake/exploratory/` | `PLACE` |
| AI authoring accountability | `data/receipts/generated/` | `PLACE` |

No new root, parallel model/evidence/policy/privacy/receipt/release home, compatibility alias, migration, or ADR-class authority change is introduced.

## Acceptance and non-goals

The packet is acceptable when all use phases, source roles, and feature data types have positive fixtures; feature and lineage ordering, derivation, missingness, sensitivity-policy coupling, target separation, training-dataset coupling, mandatory limits, deterministic identity, hostile-input handling, no-network behavior, and no-authority fields fail closed when violated.

It does not add a feature store, extraction engine, data payload, imputer, dataset, model trainer, inference runner, EvidenceBundle resolver, privacy decision, validation report, review flow, public API, release action, deployment, or publication.

## Rollback

Revert the additive packet. The source carriers and all existing model, analytics, evidence, dataset, policy, review, release, and runtime objects remain unchanged; no operational state requires restoration.
