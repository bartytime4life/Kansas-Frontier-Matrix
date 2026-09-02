<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/full-atlas-semantic-disposition-crosswalk
title: Full Atlas Semantic Disposition Crosswalk
type: exploratory-source-map
version: v0.1.0
status: proposed; inventory-reconciled; human-review-hold
owners: OWNER_TBD — Atlas steward · Intake steward · Architecture steward
created: 2026-08-26
updated: 2026-08-26
policy_label: repository-facing; exploratory; non-authoritative
owning_root: docs/
responsibility: Classify the 78 non-exact subjects in the supplied-source versus repository-carrier Atlas inventory without merging, importing, adopting, or assigning stable card identities.
truth_posture: CONFIRMED inventory and pinned repository evidence / PROPOSED semantic relation / HUMAN_REVIEW required for every merge or equivalence decision
related:
  - ../../kfm_full_atlas_seed_cards.md
  - ../new-ideas-register.md
  - ../../doctrine/directory-rules.md
  - ../../doctrine/truth-posture.md
tags: [kfm, atlas, intake, crosswalk, semantic-disposition, implementation-maturity, human-review]
[/KFM_META_BLOCK_V2] -->

# Full Atlas semantic disposition crosswalk

## Outcome and authority boundary

This document classifies every non-exact subject preserved by the existing
Full Atlas inventory crosswalk: one title delta, 39 supplied-source-only
subjects, and 38 repository-carrier-only subjects. It does **not** change the
31 exact-title matches, the source or carrier counts, or the carrier itself.

The supplied source is the read-only `KFM_Full_Atlas_seed_cards.md` attachment:

| Source control | Verified value |
|---|---|
| SHA-256 | `9a95ab510bd984c257a8c578f8646993c7fe55d76f7d3c5f60d8bb9ad04ec3a2` |
| Lines | `8,248` |
| Card headings | `213` in 71 positional idea/feature/programming triplets |
| Repository carrier | [`docs/kfm_full_atlas_seed_cards.md`](../../kfm_full_atlas_seed_cards.md), unchanged by this packet |
| Repository evidence base | `main@93a66dbcd7a7a924f3e52e071459c775bb2b1422` |
| Inventory carried forward | 31 exact matches + 1 title delta + 39 source-only + 38 carrier-only |

Only topic titles are carried into the tables below. No source-card prose,
placeholder IDs, normalized statements, source IDs, or proposed paths are
imported. A semantic relation is a review hypothesis, not an identity, merge,
supersession, adoption, or implementation decision.

All linked repository paths were inspected at the pinned base above. A path
proves only that the cited repository surface existed at that commit. It does
not prove production use, hosted enforcement, release, deployment, or Atlas
adoption.

## Controlled axes

### Semantic relation

The relation is directional: the subject in the row is compared with the
listed subject or subjects from the other unmatched inventory.

| Value | Meaning |
|---|---|
| `NEAR_EQUIVALENT` | The subjects appear to express the same central concern, but wording or normalized statements differ. |
| `BROADER_THAN` | The row subject appears to contain the listed subject and additional concerns. |
| `NARROWER_THAN` | The row subject appears to specialize part of the listed subject. |
| `PARTIAL_OVERLAP` | The subjects share a bounded concern, but neither safely contains the other. |
| `NO_CONFIDENT_COUNTERPART` | Current title and repository evidence do not support a safe cross-inventory counterpart. |

### Implementation maturity

| Value | Meaning |
|---|---|
| `EXECUTABLE_FIXTURE_PROFILE` | A bounded contract/schema/validator/test or equivalent local proof exists. It is not production or release evidence. |
| `EXECUTABLE_LOCAL_COMPONENT` | Local application or tool code and tests exist, with no claim of deployment or publication. |
| `DOCUMENTED_GOVERNANCE` | Doctrine, ADR, standard, or register evidence exists; executable enforcement is not claimed. |
| `PARTIAL_REPO_SURFACE` | Related repository surfaces exist, but they do not close the full subject. |
| `NO_DIRECT_REPO_SURFACE` | No direct repository surface was verified in the bounded search. |

Every row remains `HUMAN_REVIEW/HOLD`. The hold prevents these semantic
hypotheses from changing the Atlas inventory, allocating stable IDs, importing
source prose, or asserting adoption.

## Title delta disposition

| Supplied subject | Carrier subject | Relation | Maturity | Pinned evidence | Review state |
|---|---|---|---|---|---|
| Source ordinal `028` — Field and MapLibre 3D integration Capture Governance | `KFM-TRIAD-028` — Field and 3D Capture Governance | `NEAR_EQUIVALENT` | `PARTIAL_REPO_SURFACE` | [carrier inventory](../../kfm_full_atlas_seed_cards.md); [field-capture handoff](../../../contracts/evidence/field_capture_evidence_handoff.md) | `HUMAN_REVIEW/HOLD` — the three normalized statements differ; editorial equivalence is not inferred. |

## Supplied-source-only dispositions

For each row, the subject is the supplied-source title and the comparison is to
one or more repository-carrier-only triads. Executable evidence may show that a
concept has a bounded repository realization even though no same-title carrier
triad exists.

| Source ordinal and subject | Closest carrier-only subject(s) | Relation | Maturity | Pinned repository evidence | Review state |
|---|---|---|---|---|---|
| `033` — Source-Role Anti-Collapse Register | `KFM-TRIAD-037` Corroboration Role Graph; `065` Source-Conflict Topology and Influence Accounting | `BROADER_THAN` | `EXECUTABLE_FIXTURE_PROFILE` | [source-role validator](../../../tools/validators/source_role/validate_source_role.py); [tests](../../../tests/validators/test_validate_source_role.py) | `HUMAN_REVIEW/HOLD` |
| `034` — Master Receipt Catalog and Lifecycle Mapping | `KFM-TRIAD-069` Generated Runtime-Proof Artifact Lifecycle; `057` Replay-Safe Event Identity and Side-Effect Ledger | `BROADER_THAN` | `EXECUTABLE_FIXTURE_PROFILE` | [receipt catalog assessment](../../../contracts/governance/receipt_catalog_assessment.md); [tests](../../../tests/validators/governance/test_receipt_catalog_assessment.py) | `HUMAN_REVIEW/HOLD` |
| `035` — Finite Decision Outcome Envelope | `KFM-TRIAD-066` Cross-Layer Outcome Projection and Parity; `058` Conditional Decision Obligations and Closure | `BROADER_THAN` | `EXECUTABLE_FIXTURE_PROFILE` | [decision envelope](../../../contracts/runtime/decision_envelope.md); [tests](../../../tests/validators/test_validate_decision_envelope.py) | `HUMAN_REVIEW/HOLD` |
| `036` — Sensitivity Tier Scheme T0-T4 and Transitions | No confident carrier-only counterpart | `NO_CONFIDENT_COUNTERPART` | `PARTIAL_REPO_SURFACE` | [sensitivity tiers](../../architecture/sensitivity-tiers.md); [sensitivity label contract](../../../contracts/policy/sensitivity_label.md) | `HUMAN_REVIEW/HOLD` |
| `037` — Universal Pipeline Gate Reference (RAW to PUBLISHED) | `KFM-TRIAD-033` Material Change Classification and Non-Event Receipts; `035` Correctable Environmental Event Lifecycle; `049` Product Cadence, Delivery Latency, and Availability | `BROADER_THAN` | `DOCUMENTED_GOVERNANCE` | [lifecycle law](../../doctrine/lifecycle-law.md); [pipeline gate reference](../../atlases/pipeline-gate-reference.md) | `HUMAN_REVIEW/HOLD` |
| `038` — Reviewer Role and Separation-of-Duties Matrix | `KFM-TRIAD-058` Conditional Decision Obligations and Closure | `BROADER_THAN` | `EXECUTABLE_FIXTURE_PROFILE` | [reviewer-role vocabulary](../../../contracts/policy/policy_reviewer_role_vocabulary.md); [tests](../../../tests/validators/test_validate_policy_reviewer_role_vocabulary.py) | `HUMAN_REVIEW/HOLD` |
| `039` — Stale-State and Supersession Lineage | `KFM-TRIAD-036` Baseline Cohort and Drift Governance; `070` Observed Interface Evolution and Compatibility Window | `BROADER_THAN` | `EXECUTABLE_FIXTURE_PROFILE` | [stale-state assessment](../../../contracts/common/stale_state_supersession_assessment.md); [tests](../../../tests/validators/governance/test_validate_stale_state_supersession_assessment.py) | `HUMAN_REVIEW/HOLD` |
| `040` — Failure-Mode and Anti-Pattern Register (Trust-Membrane Discipline) | `KFM-TRIAD-063` Adversarial Validator Assurance and Mutation Adequacy | `BROADER_THAN` | `DOCUMENTED_GOVERNANCE` | [Directory Rules anti-pattern authority](../../doctrine/directory-rules.md); [security threat model](../../security/THREAT_MODEL.md) | `HUMAN_REVIEW/HOLD` |
| `041` — Risk Register and Threat Posture | `KFM-TRIAD-063` Adversarial Validator Assurance and Mutation Adequacy; `053` Confounder Exclusion and Observation Fitness | `BROADER_THAN` | `DOCUMENTED_GOVERNANCE` | [security threat model](../../security/THREAT_MODEL.md); [API threat model](../../architecture/governed-api/THREAT_MODEL.md) | `HUMAN_REVIEW/HOLD` |
| `042` — Governance Health Indicators | No confident carrier-only counterpart | `NO_CONFIDENT_COUNTERPART` | `EXECUTABLE_FIXTURE_PROFILE` | [governance health projection](../../../contracts/governance/governance_health_projection.md); [tests](../../../tests/generators/governance_health/test_compile_governance_health_projection.py) | `HUMAN_REVIEW/HOLD` |
| `043` — Open-ADR Backlog Discipline | No confident carrier-only counterpart | `NO_CONFIDENT_COUNTERPART` | `EXECUTABLE_FIXTURE_PROFILE` | [open-ADR assessment](../../../contracts/governance/open_adr_backlog_discipline_assessment.md); [tests](../../../tests/validators/governance/test_validate_open_adr_backlog_discipline_assessment.py) | `HUMAN_REVIEW/HOLD` |
| `044` — Object Family x Domain Reference Matrix | `KFM-TRIAD-054` Cross-Boundary Evidence Custody and Reconciliation; `066` Cross-Layer Outcome Projection and Parity | `BROADER_THAN` | `EXECUTABLE_FIXTURE_PROFILE` | [object-family profile](../../../contracts/governance/object_family_domain_reference_profile.md); [tests](../../../tests/validators/governance/test_object_family_domain_reference_profile.py) | `HUMAN_REVIEW/HOLD` |
| `045` — Frontier Demography Economy Settlement Land Time Matrix Lane | `KFM-TRIAD-041` Historical Network Uncertainty and Temporal Joins; `061` Place-Name Authority and Temporal Alias Graph | `BROADER_THAN` | `PARTIAL_REPO_SURFACE` | [county-year panel](../../../contracts/data/county_year_panel.md); [place-name graph](../../../contracts/domains/settlements-infrastructure/place_name_authority_graph.md) | `HUMAN_REVIEW/HOLD` |
| `046` — Planetary MapLibre 3D integration Digital-Twin and Synthetic Spatial Governance Lane | `KFM-TRIAD-039` Governed Time-Bucket Map Playback; `052` Verified Rendering Resource Envelope | `BROADER_THAN` | `PARTIAL_REPO_SURFACE` | [planetary 3D architecture](../../architecture/planetary-3d.md); [domain README](../../domains/planetary-3d/README.md) | `HUMAN_REVIEW/HOLD` |
| `047` — Sigstore Keyless Attestation as Promotion Floor | `KFM-TRIAD-056` Trust-Root Lifecycle and Historical Signature Verification; `051` Offline Release Capsule and Trust Freshness | `NARROWER_THAN` | `EXECUTABLE_FIXTURE_PROFILE` | [Cosign verification plan](../../../contracts/release/cosign_attestation_verification_plan.md); [tests](../../../tests/release/test_cosign_attestation_verification_plan.py) | `HUMAN_REVIEW/HOLD` — no live signing or promotion authority is inferred. |
| `048` — Bao Outboard Range-Proof for PMTiles Verification | `KFM-TRIAD-051` Offline Release Capsule and Trust Freshness; `052` Verified Rendering Resource Envelope | `NARROWER_THAN` | `PARTIAL_REPO_SURFACE` | [PMTiles attestation standard](../../standards/pmtiles/PMTILES_ATTESTATION_STANDARD.md); [integrity source map](pmtiles-attestation-integrity-source-map.md) | `HUMAN_REVIEW/HOLD` — cryptographic range-proof closure is not claimed. |
| `049` — STAC DCAT PROV Distribution Cross-Mapping | `KFM-TRIAD-040` STAC Profile and Link-Closure Conformance; `046` Distribution Assertion and Coverage Semantics | `BROADER_THAN` | `EXECUTABLE_FIXTURE_PROFILE` | [catalog mapping profile](../../../contracts/data/catalog_distribution_mapping_profile.md); [tests](../../../tests/validators/catalog_closure/test_catalog_distribution_mapping_profile.py) | `HUMAN_REVIEW/HOLD` |
| `050` — OCI ORAS Artifact Publication Lane | `KFM-TRIAD-050` Asynchronous Transfer and Partial-State Provenance; `051` Offline Release Capsule and Trust Freshness | `NARROWER_THAN` | `EXECUTABLE_LOCAL_COMPONENT` | [OCI artifact browser](../../../apps/explorer-web/src/features/oci_artifact_browser/index.ts); [tests](../../../apps/explorer-web/tests/oci-artifact-browser.test.ts) | `HUMAN_REVIEW/HOLD` — the browser is not publication authority. |
| `051` — Environmental Indicator Gate (NDVI and Air Quality) | `KFM-TRIAD-048` Measurement Support and Scale Reconciliation; `053` Confounder Exclusion and Observation Fitness | `PARTIAL_OVERLAP` | `EXECUTABLE_FIXTURE_PROFILE` | [indicator bundle profile](../../../contracts/evidence/environmental_indicator_evidence_bundle_profile.md); [tests](../../../tests/validators/test_validate_environmental_indicator_evidence_bundle_profile.py) | `HUMAN_REVIEW/HOLD` |
| `052` — SSURGO and gNATSGO Yearly Diff Pipeline | `KFM-TRIAD-033` Material Change Classification and Non-Event Receipts; `036` Baseline Cohort and Drift Governance | `NARROWER_THAN` | `EXECUTABLE_FIXTURE_PROFILE` | [SSURGO yearly diff](../../../contracts/domains/soil/ssurgo_yearly_diff_profile.md); [tests](../../../tests/validators/domains/soil/test_validate_ssurgo_yearly_diff_profile.py) | `HUMAN_REVIEW/HOLD` |
| `053` — Connector and Watcher as Anti-Corruption Layer | `KFM-TRIAD-043` Retrieval Intent and Query Snapshot; `044` Source Terms Snapshot and Rights Drift; `070` Observed Interface Evolution and Compatibility Window | `BROADER_THAN` | `PARTIAL_REPO_SURFACE` | [connector boundary](../../../connectors/README.md); [source-event envelope](../../../contracts/source/source_event_envelope.md) | `HUMAN_REVIEW/HOLD` |
| `054` — Consent and Egress Policy Pack | `KFM-TRIAD-038` Purpose-Bound Consent and Revocation Propagation; `054` Cross-Boundary Evidence Custody and Reconciliation; `058` Conditional Decision Obligations and Closure | `BROADER_THAN` | `EXECUTABLE_FIXTURE_PROFILE` | [consent revocation assessment](../../../contracts/domains/people-dna-land/consent_revocation_propagation_assessment.md); [tests](../../../tests/domains/people-dna-land/consent/revocation/test_consent_revocation_propagation_assessment.py) | `HUMAN_REVIEW/HOLD` |
| `055` — GA4GH-Style Token Gatehouse for DNA and Genomic Material | `KFM-TRIAD-038` Purpose-Bound Consent and Revocation Propagation | `NARROWER_THAN` | `PARTIAL_REPO_SURFACE` | [DNA public-deny policy](../../../policy/sensitivity/dna_segment_public_deny.rego); [consent policy](../../../policy/domains/people-dna-land/consent/dna_consent_revocation.rego) | `HUMAN_REVIEW/HOLD` — no GA4GH token service is claimed. |
| `056` — Headless Render Gate CI | `KFM-TRIAD-052` Verified Rendering Resource Envelope | `PARTIAL_OVERLAP` | `EXECUTABLE_LOCAL_COMPONENT` | [headless review packet](../../../apps/explorer-web/src/features/map_runtime/headless_render_review_packet.ts); [tests](../../../tests/validators/test_headless_render_review_packet.py) | `HUMAN_REVIEW/HOLD` |
| `057` — JCS Plus SHA-256 Spec-Hash Identity | `KFM-TRIAD-034` Identifier and Precision Lineage; `042` Purpose-Specific Hash Profiles | `NARROWER_THAN` | `EXECUTABLE_LOCAL_COMPONENT` | [JCS validator](../../../tools/validators/identity/jcs_spec_hash.py); [tests](../../../tests/validators/test_validate_spec_hash.py) | `HUMAN_REVIEW/HOLD` |
| `058` — OPA Promotion Gate for Derived Indicators | `KFM-TRIAD-053` Confounder Exclusion and Observation Fitness; `058` Conditional Decision Obligations and Closure | `NARROWER_THAN` | `PARTIAL_REPO_SURFACE` | [OPA boundary](../../../policy/opa/README.md); [indicator definition](../../../contracts/evidence/indicator_definition.md) | `HUMAN_REVIEW/HOLD` — no derived-indicator promotion decision is inferred. |
| `059` — apps/explorer-web Canonical Map-First Shell | `KFM-TRIAD-039` Governed Time-Bucket Map Playback; `052` Verified Rendering Resource Envelope | `BROADER_THAN` | `EXECUTABLE_LOCAL_COMPONENT` | [shell](../../../apps/explorer-web/src/features/shell/index.tsx); [tests](../../../apps/explorer-web/tests/shell-baseline.test.ts) | `HUMAN_REVIEW/HOLD` |
| `060` — Focus Mode as Cross-Cutting Compositional Unit | `KFM-TRIAD-055` Composed Claim Dependency Closure; `039` Governed Time-Bucket Map Playback | `PARTIAL_OVERLAP` | `EXECUTABLE_LOCAL_COMPONENT` | [Focus panel](../../../apps/explorer-web/src/features/focus_panel/index.tsx); [tests](../../../apps/explorer-web/tests/focus-composed-claim.test.ts) | `HUMAN_REVIEW/HOLD` |
| `061` — Renderer as Pluggable Component Framework | `KFM-TRIAD-052` Verified Rendering Resource Envelope; `067` Verifier Profile and Capability Portability | `BROADER_THAN` | `EXECUTABLE_FIXTURE_PROFILE` | [renderer admission](../../../contracts/map/renderer_plugin_admission_assessment.md); [tests](../../../tests/validators/map/test_validate_renderer_plugin_admission_assessment.py) | `HUMAN_REVIEW/HOLD` |
| `062` — KFM Domains as DDD Bounded Contexts with Context Map | `KFM-TRIAD-054` Cross-Boundary Evidence Custody and Reconciliation; `066` Cross-Layer Outcome Projection and Parity | `BROADER_THAN` | `EXECUTABLE_FIXTURE_PROFILE` | [context-map assessment](../../../contracts/governance/domain_context_map_assessment.md); [tests](../../../tests/validators/governance/test_validate_domain_context_map_assessment.py) | `HUMAN_REVIEW/HOLD` |
| `063` — Manifests as DDD Entities with spec_hash Identity | `KFM-TRIAD-042` Purpose-Specific Hash Profiles; `069` Generated Runtime-Proof Artifact Lifecycle | `BROADER_THAN` | `PARTIAL_REPO_SURFACE` | [identity architecture](../../architecture/identity-and-spec-hash.md); [spec-hash contract](../../../contracts/common/spec_hash.md) | `HUMAN_REVIEW/HOLD` |
| `064` — Two-Person Rule for T3/T4 Release | `KFM-TRIAD-058` Conditional Decision Obligations and Closure; `054` Cross-Boundary Evidence Custody and Reconciliation | `NARROWER_THAN` | `DOCUMENTED_GOVERNANCE` | [ADR-0024](../../adr/ADR-0024-steward-separation-of-duties-for-release.md); [separation of duties](../../governance/SEPARATION_OF_DUTIES.md) | `HUMAN_REVIEW/HOLD` — reviewer identity and release execution are not inferred. |
| `065` — Pre-RAW Watcher Signal Stage | `KFM-TRIAD-043` Retrieval Intent and Query Snapshot; `049` Product Cadence, Delivery Latency, and Availability | `BROADER_THAN` | `EXECUTABLE_FIXTURE_PROFILE` | [source-event envelope](../../../contracts/source/source_event_envelope.md); [tests](../../../tests/validators/test_validate_source_event_envelope.py) | `HUMAN_REVIEW/HOLD` — no live watcher activation is claimed. |
| `066` — Replay Verification of Pipelines and Receipts | `KFM-TRIAD-057` Replay-Safe Event Identity and Side-Effect Ledger; `064` Bitemporal Verification-State Replay; `069` Generated Runtime-Proof Artifact Lifecycle | `BROADER_THAN` | `EXECUTABLE_FIXTURE_PROFILE` | [pipeline replay assessment](../../../contracts/validation/pipeline_replay_assessment.md); [tests](../../../tests/validators/test_validate_pipeline_replay_assessment.py) | `HUMAN_REVIEW/HOLD` |
| `067` — Drift Register Triage Discipline | `KFM-TRIAD-036` Baseline Cohort and Drift Governance; `044` Source Terms Snapshot and Rights Drift; `070` Observed Interface Evolution and Compatibility Window | `BROADER_THAN` | `EXECUTABLE_FIXTURE_PROFILE` | [drift triage assessment](../../../contracts/governance/drift_register_triage_assessment.md); [tests](../../../tests/validators/governance/test_validate_drift_register_triage_assessment.py) | `HUMAN_REVIEW/HOLD` |
| `068` — Crosswalk Validator Lane (SQL-First Non-Publisher) | `KFM-TRIAD-059` Reversible Entity Reconciliation and Conflict-Preserving Dedupe; `060` Taxonomic Concept and Name-Usage Lineage; `063` Adversarial Validator Assurance and Mutation Adequacy | `NARROWER_THAN` | `EXECUTABLE_LOCAL_COMPONENT` | [join assessment](../../../contracts/joins/cross_lane_join_assessment.md); [tool](../../../tools/joins/join_candidates.py); [tests](../../../tests/joins/test_join_candidates.py) | `HUMAN_REVIEW/HOLD` |
| `069` — Authority Ladder Doctrine | `KFM-TRIAD-037` Corroboration Role Graph; `065` Source-Conflict Topology and Influence Accounting | `BROADER_THAN` | `DOCUMENTED_GOVERNANCE` | [authority ladder](../../doctrine/authority-ladder.md); [register projection](../../registers/AUTHORITY_LADDER.md) | `HUMAN_REVIEW/HOLD` |
| `070` — County Proof-Slice (Focus-Mode-First Releases) | `KFM-TRIAD-039` Governed Time-Bucket Map Playback; `047` Coverage-Aware Prioritization and Exploration-Bias Control; `051` Offline Release Capsule and Trust Freshness | `BROADER_THAN` | `PARTIAL_REPO_SURFACE` | [ADR-0027](../../adr/ADR-0027-county-focus-mode-control-plane.md); [Focus boundary tests](../../../apps/explorer-web/tests/focus-workspace-boundary.test.ts) | `HUMAN_REVIEW/HOLD` — no county release is asserted. |
| `071` — LiDAR Lineage Manifest | `KFM-TRIAD-062` Survey-Control and Boundary Derivation Provenance; `051` Offline Release Capsule and Trust Freshness | `NARROWER_THAN` | `EXECUTABLE_FIXTURE_PROFILE` | [LiDAR lineage candidate](../../../contracts/data/lidar_lineage_manifest_candidate.md); [tests](../../../tests/validators/data/test_lidar_lineage_manifest_candidate.py) | `HUMAN_REVIEW/HOLD` |

## Repository-carrier-only dispositions

For each row, the subject is the repository-carrier title and the comparison is
to one or more supplied-source-only titles. These rows do not imply that the
carrier subject was derived from, replaces, or should merge with the supplied
subject.

| Carrier triad and subject | Closest supplied-source-only subject(s) | Relation | Maturity | Pinned repository evidence | Review state |
|---|---|---|---|---|---|
| `KFM-TRIAD-033` — Material Change Classification and Non-Event Receipts | Source `052` SSURGO and gNATSGO Yearly Diff Pipeline | `BROADER_THAN` | `EXECUTABLE_FIXTURE_PROFILE` | [material-change assessment](../../../contracts/data/material_change_assessment.md); [tests](../../../tests/validators/test_validate_material_change_assessment.py) | `HUMAN_REVIEW/HOLD` |
| `KFM-TRIAD-034` — Identifier and Precision Lineage | Source `057` JCS Plus SHA-256 Spec-Hash Identity | `BROADER_THAN` | `EXECUTABLE_FIXTURE_PROFILE` | [identifier/precision assessment](../../../contracts/common/identifier_precision_lineage_assessment.md); [tests](../../../tests/validators/test_validate_identifier_precision_lineage_assessment.py) | `HUMAN_REVIEW/HOLD` |
| `KFM-TRIAD-035` — Correctable Environmental Event Lifecycle | Source `051` Environmental Indicator Gate (NDVI and Air Quality) | `PARTIAL_OVERLAP` | `EXECUTABLE_FIXTURE_PROFILE` | [event assessment](../../../contracts/domains/atmosphere/correctable_environmental_event_assessment.md); [tests](../../../tests/domains/atmosphere/test_correctable_environmental_event_assessment.py) | `HUMAN_REVIEW/HOLD` |
| `KFM-TRIAD-036` — Baseline Cohort and Drift Governance | Source `039` Stale-State and Supersession Lineage; `052` SSURGO and gNATSGO Yearly Diff Pipeline; `067` Drift Register Triage Discipline | `PARTIAL_OVERLAP` | `EXECUTABLE_FIXTURE_PROFILE` | [baseline assessment](../../../contracts/data/baseline_cohort_assessment.md); [tests](../../../tests/data/test_baseline_cohort_assessment.py) | `HUMAN_REVIEW/HOLD` |
| `KFM-TRIAD-037` — Corroboration Role Graph | Source `033` Source-Role Anti-Collapse Register | `NARROWER_THAN` | `EXECUTABLE_FIXTURE_PROFILE` | [corroboration assessment](../../../contracts/evidence/corroboration_role_assessment.md); [tests](../../../tests/validators/test_validate_corroboration_role_assessment.py) | `HUMAN_REVIEW/HOLD` |
| `KFM-TRIAD-038` — Purpose-Bound Consent and Revocation Propagation | Source `054` Consent and Egress Policy Pack; `055` GA4GH-Style Token Gatehouse for DNA and Genomic Material | `NARROWER_THAN` | `EXECUTABLE_FIXTURE_PROFILE` | [consent revocation assessment](../../../contracts/domains/people-dna-land/consent_revocation_propagation_assessment.md); [tests](../../../tests/domains/people-dna-land/consent/revocation/test_consent_revocation_propagation_assessment.py) | `HUMAN_REVIEW/HOLD` |
| `KFM-TRIAD-039` — Governed Time-Bucket Map Playback | Source `046` Planetary MapLibre 3D integration Digital-Twin and Synthetic Spatial Governance Lane; `070` County Proof-Slice (Focus-Mode-First Releases) | `NARROWER_THAN` | `EXECUTABLE_FIXTURE_PROFILE` | [playback manifest](../../../contracts/ui/time_bucket_playback_manifest.md); [tests](../../../tests/validators/ui/test_time_bucket_playback_manifest.py) | `HUMAN_REVIEW/HOLD` |
| `KFM-TRIAD-040` — STAC Profile and Link-Closure Conformance | Source `049` STAC DCAT PROV Distribution Cross-Mapping | `NARROWER_THAN` | `EXECUTABLE_FIXTURE_PROFILE` | [STAC link closure](../../../contracts/data/stac_link_closure_assessment.md); [tests](../../../tests/validators/test_validate_stac_link_closure_assessment.py) | `HUMAN_REVIEW/HOLD` |
| `KFM-TRIAD-041` — Historical Network Uncertainty and Temporal Joins | Source `045` Frontier Demography Economy Settlement Land Time Matrix Lane | `NARROWER_THAN` | `EXECUTABLE_FIXTURE_PROFILE` | [historical-network assessment](../../../contracts/joins/historical_network_proximity_assessment.md); [tests](../../../tests/joins/test_historical_network_proximity.py) | `HUMAN_REVIEW/HOLD` |
| `KFM-TRIAD-042` — Purpose-Specific Hash Profiles | Source `057` JCS Plus SHA-256 Spec-Hash Identity; `063` Manifests as DDD Entities with spec_hash Identity | `BROADER_THAN` | `EXECUTABLE_FIXTURE_PROFILE` | [hash-profile matrix](../../../contracts/common/hash_profile_readiness_matrix.md); [tests](../../../tests/validators/test_validate_hash_profile_readiness_matrix.py) | `HUMAN_REVIEW/HOLD` |
| `KFM-TRIAD-043` — Retrieval Intent and Query Snapshot | Source `053` Connector and Watcher as Anti-Corruption Layer; `065` Pre-RAW Watcher Signal Stage | `NARROWER_THAN` | `EXECUTABLE_FIXTURE_PROFILE` | [retrieval-intent assessment](../../../contracts/source/retrieval_intent_query_snapshot_assessment.md); [tests](../../../tests/source/test_retrieval_intent_query_snapshot_assessment.py) | `HUMAN_REVIEW/HOLD` |
| `KFM-TRIAD-044` — Source Terms Snapshot and Rights Drift | Source `033` Source-Role Anti-Collapse Register; `053` Connector and Watcher as Anti-Corruption Layer; `054` Consent and Egress Policy Pack | `PARTIAL_OVERLAP` | `EXECUTABLE_FIXTURE_PROFILE` | [rights-drift disposition](../../../contracts/source/source_terms_drift_disposition.md); [tests](../../../tests/validators/test_validate_source_terms_drift_disposition.py) | `HUMAN_REVIEW/HOLD` |
| `KFM-TRIAD-045` — Sampling Effort and Non-Detection Support | Source `051` Environmental Indicator Gate (NDVI and Air Quality) | `NARROWER_THAN` | `EXECUTABLE_FIXTURE_PROFILE` | [non-detection assessment](../../../contracts/evidence/non_detection_support_assessment.md); [tests](../../../tests/evidence/test_non_detection_support_assessment.py) | `HUMAN_REVIEW/HOLD` |
| `KFM-TRIAD-046` — Distribution Assertion and Coverage Semantics | Source `049` STAC DCAT PROV Distribution Cross-Mapping; `051` Environmental Indicator Gate (NDVI and Air Quality) | `PARTIAL_OVERLAP` | `EXECUTABLE_FIXTURE_PROFILE` | [distribution/coverage assessment](../../../contracts/evidence/distribution_coverage_assessment.md); [tests](../../../tests/evidence/test_distribution_coverage_assessment.py) | `HUMAN_REVIEW/HOLD` |
| `KFM-TRIAD-047` — Coverage-Aware Prioritization and Exploration-Bias Control | Source `051` Environmental Indicator Gate (NDVI and Air Quality); `070` County Proof-Slice (Focus-Mode-First Releases) | `PARTIAL_OVERLAP` | `EXECUTABLE_FIXTURE_PROFILE` | [coverage scorecard](../../../contracts/governance/coverage_priority_scorecard.md); [tests](../../../tests/validators/governance/test_coverage_priority_scorecard.py) | `HUMAN_REVIEW/HOLD` |
| `KFM-TRIAD-048` — Measurement Support and Scale Reconciliation | Source `051` Environmental Indicator Gate (NDVI and Air Quality) | `NARROWER_THAN` | `EXECUTABLE_FIXTURE_PROFILE` | [measurement reconciliation](../../../contracts/common/measurement_support_reconciliation.md); [tests](../../../tests/validators/test_validate_measurement_support_reconciliation.py) | `HUMAN_REVIEW/HOLD` |
| `KFM-TRIAD-049` — Product Cadence, Delivery Latency, and Availability | Source `052` SSURGO and gNATSGO Yearly Diff Pipeline; `053` Connector and Watcher as Anti-Corruption Layer; `065` Pre-RAW Watcher Signal Stage | `PARTIAL_OVERLAP` | `EXECUTABLE_FIXTURE_PROFILE` | [delivery assessment](../../../contracts/source/delivery_availability_assessment.md); [tests](../../../tests/validators/test_validate_delivery_availability_assessment.py) | `HUMAN_REVIEW/HOLD` |
| `KFM-TRIAD-050` — Asynchronous Transfer and Partial-State Provenance | Source `050` OCI ORAS Artifact Publication Lane; `053` Connector and Watcher as Anti-Corruption Layer | `BROADER_THAN` | `EXECUTABLE_FIXTURE_PROFILE` | [transfer assessment](../../../contracts/source/asynchronous_transfer_assessment.md); [tests](../../../tests/validators/test_validate_asynchronous_transfer_assessment.py) | `HUMAN_REVIEW/HOLD` |
| `KFM-TRIAD-051` — Offline Release Capsule and Trust Freshness | Source `047` Sigstore Keyless Attestation as Promotion Floor; `048` Bao Outboard Range-Proof for PMTiles Verification; `050` OCI ORAS Artifact Publication Lane; `070` County Proof-Slice (Focus-Mode-First Releases) | `BROADER_THAN` | `EXECUTABLE_FIXTURE_PROFILE` | [offline capsule assessment](../../../contracts/runtime/offline_release_capsule_assessment.md); [tests](../../../tests/validators/test_validate_offline_release_capsule_assessment.py) | `HUMAN_REVIEW/HOLD` |
| `KFM-TRIAD-052` — Verified Rendering Resource Envelope | Source `046` Planetary MapLibre 3D integration Digital-Twin and Synthetic Spatial Governance Lane; `056` Headless Render Gate CI; `059` apps/explorer-web Canonical Map-First Shell; `061` Renderer as Pluggable Component Framework | `PARTIAL_OVERLAP` | `EXECUTABLE_FIXTURE_PROFILE` | [rendering envelope](../../../contracts/runtime/verified_rendering_resource_envelope.md); [tests](../../../tests/validators/test_validate_verified_rendering_resource_envelope.py) | `HUMAN_REVIEW/HOLD` |
| `KFM-TRIAD-053` — Confounder Exclusion and Observation Fitness | Source `051` Environmental Indicator Gate (NDVI and Air Quality); `058` OPA Promotion Gate for Derived Indicators | `BROADER_THAN` | `EXECUTABLE_FIXTURE_PROFILE` | [observation fitness](../../../contracts/evidence/observation_fitness_assessment.md); [tests](../../../tests/evidence/test_observation_fitness_assessment.py) | `HUMAN_REVIEW/HOLD` |
| `KFM-TRIAD-054` — Cross-Boundary Evidence Custody and Reconciliation | Source `054` Consent and Egress Policy Pack; `062` KFM Domains as DDD Bounded Contexts with Context Map | `PARTIAL_OVERLAP` | `EXECUTABLE_FIXTURE_PROFILE` | [custody handoff](../../../contracts/evidence/evidence_custody_handoff.md); [tests](../../../tests/validators/test_validate_evidence_custody_handoff.py) | `HUMAN_REVIEW/HOLD` |
| `KFM-TRIAD-055` — Composed Claim Dependency Closure | Source `035` Finite Decision Outcome Envelope; `060` Focus Mode as Cross-Cutting Compositional Unit | `PARTIAL_OVERLAP` | `EXECUTABLE_FIXTURE_PROFILE` | [composed-claim closure](../../../contracts/evidence/composed_claim_dependency_closure.md); [tests](../../../tests/validators/test_validate_composed_claim_dependency_closure.py) | `HUMAN_REVIEW/HOLD` |
| `KFM-TRIAD-056` — Trust-Root Lifecycle and Historical Signature Verification | Source `047` Sigstore Keyless Attestation as Promotion Floor | `BROADER_THAN` | `EXECUTABLE_FIXTURE_PROFILE` | [signature assessment](../../../contracts/release/historical_signature_verification_assessment.md); [tests](../../../tests/validators/test_validate_historical_signature_verification_assessment.py) | `HUMAN_REVIEW/HOLD` |
| `KFM-TRIAD-057` — Replay-Safe Event Identity and Side-Effect Ledger | Source `066` Replay Verification of Pipelines and Receipts | `NARROWER_THAN` | `EXECUTABLE_FIXTURE_PROFILE` | [effect ledger](../../../contracts/runtime/replay_safe_effect_ledger.md); [tests](../../../tests/validators/test_validate_replay_safe_effect_ledger.py) | `HUMAN_REVIEW/HOLD` |
| `KFM-TRIAD-058` — Conditional Decision Obligations and Closure | Source `035` Finite Decision Outcome Envelope; `038` Reviewer Role and Separation-of-Duties Matrix; `054` Consent and Egress Policy Pack; `064` Two-Person Rule for T3/T4 Release | `PARTIAL_OVERLAP` | `EXECUTABLE_FIXTURE_PROFILE` | [conditional closure](../../../contracts/policy/conditional_decision_closure.md); [tests](../../../tests/validators/test_validate_conditional_decision_closure.py) | `HUMAN_REVIEW/HOLD` |
| `KFM-TRIAD-059` — Reversible Entity Reconciliation and Conflict-Preserving Dedupe | Source `062` KFM Domains as DDD Bounded Contexts with Context Map; `068` Crosswalk Validator Lane (SQL-First Non-Publisher) | `PARTIAL_OVERLAP` | `EXECUTABLE_FIXTURE_PROFILE` | [entity reconciliation](../../../contracts/common/reversible_entity_reconciliation.md); [tests](../../../tests/validators/test_validate_reversible_entity_reconciliation.py) | `HUMAN_REVIEW/HOLD` |
| `KFM-TRIAD-060` — Taxonomic Concept and Name-Usage Lineage | Source `068` Crosswalk Validator Lane (SQL-First Non-Publisher) | `NARROWER_THAN` | `EXECUTABLE_FIXTURE_PROFILE` | [taxonomy lineage](../../../contracts/crosswalks/taxonomy/taxonomic_concept_lineage.md); [tests](../../../tests/validators/test_validate_taxonomic_concept_lineage.py) | `HUMAN_REVIEW/HOLD` |
| `KFM-TRIAD-061` — Place-Name Authority and Temporal Alias Graph | Source `045` Frontier Demography Economy Settlement Land Time Matrix Lane | `NARROWER_THAN` | `EXECUTABLE_FIXTURE_PROFILE` | [place-name graph](../../../contracts/domains/settlements-infrastructure/place_name_authority_graph.md); [tests](../../../tests/validators/test_validate_place_name_authority_graph.py) | `HUMAN_REVIEW/HOLD` |
| `KFM-TRIAD-062` — Survey-Control and Boundary Derivation Provenance | Source `071` LiDAR Lineage Manifest | `BROADER_THAN` | `EXECUTABLE_FIXTURE_PROFILE` | [boundary derivation](../../../contracts/spatial-foundation/boundary_derivation_record.md); [tests](../../../tests/validators/test_validate_boundary_derivation_record.py) | `HUMAN_REVIEW/HOLD` |
| `KFM-TRIAD-063` — Adversarial Validator Assurance and Mutation Adequacy | Source `040` Failure-Mode and Anti-Pattern Register (Trust-Membrane Discipline); `041` Risk Register and Threat Posture; `056` Headless Render Gate CI; `068` Crosswalk Validator Lane (SQL-First Non-Publisher) | `PARTIAL_OVERLAP` | `EXECUTABLE_FIXTURE_PROFILE` | [validator assurance](../../../contracts/validation/validator_assurance_report.md); [tests](../../../tests/validators/test_validate_validator_assurance_report.py) | `HUMAN_REVIEW/HOLD` |
| `KFM-TRIAD-064` — Bitemporal Verification-State Replay | Source `039` Stale-State and Supersession Lineage; `066` Replay Verification of Pipelines and Receipts | `PARTIAL_OVERLAP` | `EXECUTABLE_FIXTURE_PROFILE` | [verification history](../../../contracts/evidence/verification_state_history.md); [tests](../../../tests/schemas/test_verification_state_history.py) | `HUMAN_REVIEW/HOLD` |
| `KFM-TRIAD-065` — Source-Conflict Topology and Influence Accounting | Source `033` Source-Role Anti-Collapse Register; `069` Authority Ladder Doctrine | `NARROWER_THAN` | `EXECUTABLE_FIXTURE_PROFILE` | [conflict influence assessment](../../../contracts/evidence/source_conflict_influence_assessment.md); [tests](../../../tests/validators/test_validate_source_conflict_influence_assessment.py) | `HUMAN_REVIEW/HOLD` |
| `KFM-TRIAD-066` — Cross-Layer Outcome Projection and Parity | Source `035` Finite Decision Outcome Envelope | `NARROWER_THAN` | `EXECUTABLE_FIXTURE_PROFILE` | [outcome parity](../../../contracts/common/outcome_projection_parity.md); [tests](../../../tests/validators/test_validate_outcome_projection_parity.py) | `HUMAN_REVIEW/HOLD` |
| `KFM-TRIAD-067` — Verifier Profile and Capability Portability | Source `056` Headless Render Gate CI; `061` Renderer as Pluggable Component Framework; `068` Crosswalk Validator Lane (SQL-First Non-Publisher) | `BROADER_THAN` | `EXECUTABLE_FIXTURE_PROFILE` | [verifier portability](../../../contracts/evidence/verifier_capability_portability.md); [tests](../../../tests/validators/test_validate_verifier_capability_portability.py) | `HUMAN_REVIEW/HOLD` |
| `KFM-TRIAD-068` — Source-Native Quality Translation and Health Separation | Source `051` Environmental Indicator Gate (NDVI and Air Quality); `052` SSURGO and gNATSGO Yearly Diff Pipeline; `053` Connector and Watcher as Anti-Corruption Layer | `PARTIAL_OVERLAP` | `EXECUTABLE_FIXTURE_PROFILE` | [quality translation](../../../contracts/common/source_native_quality_translation.md); [tests](../../../tests/validators/test_validate_source_native_quality_translation.py) | `HUMAN_REVIEW/HOLD` |
| `KFM-TRIAD-069` — Generated Runtime-Proof Artifact Lifecycle | Source `034` Master Receipt Catalog and Lifecycle Mapping; `047` Sigstore Keyless Attestation as Promotion Floor; `063` Manifests as DDD Entities with spec_hash Identity; `066` Replay Verification of Pipelines and Receipts | `PARTIAL_OVERLAP` | `EXECUTABLE_FIXTURE_PROFILE` | [runtime-proof artifact](../../../contracts/runtime/generated_runtime_proof_artifact.md); [tests](../../../tests/validators/test_validate_generated_runtime_proof_artifact.py) | `HUMAN_REVIEW/HOLD` |
| `KFM-TRIAD-070` — Observed Interface Evolution and Compatibility Window | Source `039` Stale-State and Supersession Lineage; `053` Connector and Watcher as Anti-Corruption Layer; `061` Renderer as Pluggable Component Framework; `067` Drift Register Triage Discipline | `PARTIAL_OVERLAP` | `EXECUTABLE_FIXTURE_PROFILE` | [interface evolution](../../../contracts/source/source_interface_evolution_assessment.md); [tests](../../../tests/validators/test_validate_source_interface_evolution_assessment.py) | `HUMAN_REVIEW/HOLD` |

## Count control and next review

| Control | Result |
|---|---:|
| Title-delta disposition rows | 1 |
| Supplied-source-only disposition rows | 39 |
| Repository-carrier-only disposition rows | 38 |
| Total non-exact subjects covered | 78 |
| Exact-title subjects reclassified | 0 |
| Stable card IDs allocated | 0 |
| Source prose imported | 0 |
| Adoption, merge, rejection, or supersession decisions | 0 |

Human review should decide one subject at a time whether a relation is strong
enough to justify a separate carrier edit. Review must compare the three
normalized statements and source attribution on both sides, not titles alone.
Until that review occurs, every row stays on hold and both inventories remain
intact.
