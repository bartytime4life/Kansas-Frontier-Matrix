<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/flora-source-refresh
title: Flora source refresh review
type: runbook
version: v1.0
status: draft; repository-grounded; review-required
owners:
  - OWNER_TBD - Flora and source stewards
  - OWNER_TBD - Documentation steward
created: 2026-10-08
updated: 2026-10-08
policy_label: public
owning_root: docs/
responsibility: Flora source refresh review; human guidance subordinate to owning contracts, schemas, policy, evidence, and release decisions
truth_posture: CONFIRMED inspected repository paths and bounded implementation; PROPOSED review procedure; UNKNOWN external source and operational acceptance
related:
  - docs/domains/flora/ARCHITECTURE.md
  - contracts/domains/flora/source_readiness/materiality_profile.md
  - .github/workflows/domain-flora.yml
evidence_snapshot: ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe
[/KFM_META_BLOCK_V2] -->

# Flora SOURCE REFRESH

Use this runbook when a Flora source changes edition, records, rights, taxonomy,
quality, availability or sensitivity. It prepares a bounded review packet; it
contains no live source refresh or publication command.

## Current capability and prerequisites

The [Flora workflow](../../.github/workflows/domain-flora.yml) executes a
synthetic public-safe fixture suite and retains explicit proof and release holds.
The [USDA PLANTS registry declaration](../../data/registry/sources/flora/usda_plants.yaml)
is proposed. The [publish declaration](../../pipeline_specs/flora/flora_publish_dryrun.yaml)
is `PROPOSED_INACTIVE`, `NOT_IMPLEMENTED`, with execution disabled.

The [source-readiness materiality profile](../../contracts/domains/flora/source_readiness/materiality_profile.md)
compares synthetic, already-normalized occurrence-dataset metrics. It performs
no fetch or source activation. Do not apply its fixture thresholds to conservation
lists, checklists or modeled ranges as if they were adopted provider policy.

Before review, obtain the exact repository revision, source/product identity,
baseline and proposed edition/digests, permitted local comparison inputs, current
rights and sensitivity records, and correction/rollback references. Source,
Flora, rights and sensitivity steward assignments remain `OWNER_TBD` here.

## Refresh procedure

1. **Pin identity.** Record source-native dataset and record identifiers,
   source role, edition/backbone version and capture/retrieval clocks.
2. **Bound acquisition separately.** If a live capture is needed, establish
   extent, history, expected volume, caching and permission through the source
   admission process. The commands below require only fixtures.
3. **Compare meaning.** Separate byte-only changes from taxonomy, location
   precision, occurrence status, license, access, freshness and sensitivity changes.
4. **Review role.** An occurrence, herbarium specimen, aggregate list, regulatory
   status and modeled range support different claims. Keep source names and IDs.
5. **Assess quality.** Preserve georeference completeness, specimen backing,
   coordinate uncertainty and missing metrics independently. Do not hide a rights
   failure inside an averaged readiness score.
6. **Evaluate the bounded profile** when the input fits its occurrence-dataset
   scope. Record its finite classification and exact profile digest.
7. **Prepare downstream impact.** List affected crosswalks, occurrences, public
   labels, sensitive-location handling, evidence, exports and correction targets.
8. **Route review.** Material change produces a candidate for review; unresolved
   rights, taxonomy or sensitivity remains held. Source admission, geoprivacy
   transformation, evidence closure and release each need their own evidence.

## Local validation

```bash
python -m unittest discover --start-directory tests/validators/domains/flora --pattern 'test_source_readiness_materiality.py' --verbose
python tools/validators/domains/flora/validate_source_readiness_materiality.py --fixtures
python -m unittest discover --start-directory tests/domains/flora --pattern 'test_flora_smoke.py' --verbose
```

Fixture mode proves expected classification, deterministic behavior and bounded
validation. It does not contact a provider or approve a refresh.

## Outcome handling

| Classification | Next action |
|---|---|
| `UNCHANGED / NON_EVENT` | Retain comparison evidence; do not manufacture a new product |
| `BYTE_ONLY / NON_EVENT` | Preserve capture identity and explain non-semantic byte change |
| `SEMANTIC_NON_MATERIAL / NON_EVENT` | Record exact profile and remaining limitations |
| `MATERIAL / PROMOTION_CANDIDATE` | Route the changed dimensions for independent review |
| `UNDETERMINED / HOLD` | Resolve missing metric, semantic state or profile binding |
| Invalid input | Correct the bounded input/profile error; do not weaken validation |

## Troubleshooting, rollback and completion

A successful source request does not settle license or sensitive-location reuse.
A changed taxon label may need [backbone rotation review](flora_BACKBONE_ROTATION.md).
An ambiguous mapping or restricted coordinate cannot be fixed by relabeling it
public-safe. Preserve the prior candidate and lineage while reviewers resolve it.

The refresh review is complete when exact compared identities, classification,
changed dimensions, test results, impact inventory, reviewers and remaining gates
are recorded. Revert a faulty documentation/profile patch through review. Any
actual data withdrawal or release rollback requires the owning runtime process;
this runbook cannot execute it.
