<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/threshold-policy-registry-source-map
title: Threshold Policy Registry Candidate — Source Map
type: exploratory-source-map
version: v0.1.0
status: exploratory; implementation-mapped; non-authoritative
owners: OWNER_TBD — Docs steward · Policy steward · Domain stewards
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; exploratory-intake; threshold-policy; pass20
owning_root: docs/
responsibility: Preserve source-to-repository reasoning and the Directory Rules path decision for the inactive ThresholdPolicyRegistry candidate.
truth_posture: CONFIRMED proposal pressure and repository duplicate assay / PROPOSED inactive registry packet / UNKNOWN accepted values, owners, bindings, evaluation, and release effects
related:
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../contracts/policy/threshold_policy_registry.md
  - ../../../policy/thresholds/README.md
notes:
  - "Exploratory lineage cannot adopt threshold values or policy authority."
[/KFM_META_BLOCK_V2] -->

# Threshold policy registry candidate — source map

## Goal

Map Pass 20 `EXP-008` and corroborating Drive material into the smallest
repository-native packet that makes unresolved threshold questions inspectable
without adopting source examples as policy.

## Source and collision review

| Evidence | Observation | Disposition |
|---|---|---|
| Attached `KFM_Pass_20_Part_2_Idea_Index_Category_Atlas_and_Expansion_Dossier.md` (`sha256:57e4b74255b52863f2a489595077741d7f45c2968a9740fe4837bac73778f780`) | `EXP-008` proposes a registry covering materiality, persistence, AOD/FRP, soil moisture, ozone, and CDL drift. It explicitly says values are policy choices requiring steward review. | `PROPOSAL LINEAGE`; record stable unresolved slots, not values. |
| Google Drive `New Ideas 5-15-26` (`gdrive://1boJrrqtqk9DcnzU8zymxFBv83r2-jvbep2kecj7WRCQ`) | Supplies illustrative watcher materiality rules and a governed non-publisher posture. | `PROPOSAL LINEAGE`; examples are not accepted thresholds, current endpoint facts, or placement authority. |
| `docs/domains/flora/EXPANSION_BACKLOG.md`, Hydrology and Hazards backlogs, Atmosphere verification backlog, and watcher READMEs | Repeatedly call a global threshold registry `PROPOSED`, warn that thresholds need fixture/steward review, or keep values local and inactive. | `CONFIRMED REPOSITORY PRESSURE`; no canonical registry found. |
| Existing domain materiality profiles and validators | Prove bounded domain-specific comparisons, often with synthetic fixture values. | `PRESERVE`; do not aggregate them into cross-domain policy. |
| `policy/README.md` | Permits inactive reviewed candidate registries under singular `policy/`; semantics, schema, fixtures, validators, and tests remain in their owning roots. | `CONFIRMED PATH OWNER`. |

## Path decision

| Responsibility | Selected path | Reason |
|---|---|---|
| Semantic meaning | `contracts/policy/threshold_policy_registry.md` | The object explains policy-registry meaning without becoming rule source. |
| Machine shape | `schemas/contracts/v1/policy/threshold_policy_registry.schema.json` | Existing canonical policy-schema family. |
| Inactive candidate rule source | `policy/thresholds/registry.v1.json` | Singular policy root explicitly permits inactive registries. |
| Child-lane boundary | `policy/thresholds/README.md` | A substantive README prevents the new child from becoming an unlabeled policy dump. |
| Synthetic examples | `fixtures/contracts/v1/policy/threshold_policy_registry/` | Existing shared fixture family. |
| Validator and tests | `tools/validators/policy/` and `tests/validators/` | Existing executable proof roots. |
| CI | `.github/workflows/threshold-policy-registry.yml` | Read-only orchestration only. |

No new root, parallel registry authority, control-plane mutation, domain-policy
override, source store, lifecycle lane, release record, or publication path is
created.

## Bounded implementation

The candidate registry names six unresolved slots and fixes every authority
field false. Its schema makes numeric or categorical values impossible in this
version. The validator checks deterministic identity, order, exact reason
posture, safe existing pressure references, no-network behavior, and parser
limits. Fixtures and tests prove positive and negative polarity.

## Non-effects and rollback

The packet does not approve a value, bind a consumer, execute policy, activate a
source, or authorize promotion, release, publication, notification, or public
use. Revert the isolated commit; no active system or public artifact requires
cleanup.
