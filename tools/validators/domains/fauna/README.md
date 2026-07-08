<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-domains-fauna-readme
title: tools/validators/domains/fauna README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-fauna-steward-plus-sensitive-species-reviewer-plus-geoprivacy-reviewer-plus-policy-steward-plus-evidence-steward
created: 2026-07-07
updated: 2026-07-07
policy_label: repository-facing; per-domain-validator-index; fauna; sensitive-species; geoprivacy; fail-closed; non-authoritative
owning_root: tools/
responsibility: proposed per-domain Fauna validator index for occurrence, sensitive-site, geoprivacy, taxon/status, range, migration, mortality, disease, invasive-species, evidence, policy, release, correction, rollback, and public-surface denial checks while deferring Fauna meaning, proof records, policy decisions, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../../README.md
  - ../../_common/README.md
  - ../README.md
  - ../../biodiversity/README.md
  - ../../cross-domain-joins/README.md
  - ../../cross-lane/README.md
  - ../../../../../docs/domains/fauna/README.md
  - ../../../../../docs/domains/fauna/IDENTITY_MODEL.md
  - ../../../../../docs/domains/fauna/FILE_SYSTEM_PLAN.md
  - ../../../../../docs/runbooks/fauna/PROMOTION_RUNBOOK.md
  - ../../../../../docs/runbooks/fauna/SOURCE_REFRESH_RUNBOOK.md
  - ../../../../../docs/adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md
  - ../../../../../contracts/domains/fauna/
  - ../../../../../schemas/contracts/v1/domains/fauna/
  - ../../../../../policy/domains/fauna/
  - ../../../../../policy/sensitivity/fauna/
  - ../../../../../data/registry/sources/fauna/
  - ../../../../../data/proofs/fauna/
  - ../../../../../data/receipts/
  - ../../../../../release/
notes:
  - "This README replaces a greenfield stub. It does not confirm executable files."
  - "No broad tools/validators/fauna/README.md was found during this task, so this path currently serves as the per-domain Fauna validator index."
  - "Fauna sensitive taxa, exact occurrences, nests, dens, roosts, hibernacula, spawning sites, breeding/aggregation sites, steward-controlled records, and reverse-engineerable derivatives are deny-by-default unless geoprivacy, review, policy, evidence, release, correction, and rollback support authorize a public-safe derivative."
  - "Validators enforce declared contracts, schemas, and policy. They do not define Fauna meaning, create EvidenceBundles, make stewardship decisions, approve release, or publish public outputs."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/domains/fauna

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-fauna--validators-informational)
![sensitivity](https://img.shields.io/badge/sensitivity-deny--by--default-red)
![authority](https://img.shields.io/badge/authority-index--only-lightgrey)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/domains/fauna/` is the proposed per-domain Fauna validator index for occurrence, sensitive-site, geoprivacy, taxon/status, range, migration, mortality, disease, invasive-species, evidence, policy, release, correction, rollback, and public-surface denial checks.

---

## Purpose

`tools/validators/domains/fauna/` exists to organize Fauna validators under the durable `tools/validators/` surface.

The durable KFM question for this index is:

> Do Fauna candidates preserve taxonomic identity, occurrence/source-role posture, sensitive-species geoprivacy, evidence closure, review state, policy decisions, release readiness, correction paths, rollback support, and public-surface denial boundaries before they reach any governed output?

The answer should be a navigable validator index and deterministic validation outputs from configured child lanes. This folder should not create Fauna truth, taxonomic authority, stewardship decisions, EvidenceBundles, geoprivacy transforms, PolicyDecisions, release decisions, public map layers, API payloads, or AI answers.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/domains/fauna/README.md` | **CONFIRMED** | This README replaces the previous greenfield stub. |
| Parent per-domain validators README | **CONFIRMED stub** | `tools/validators/domains/README.md` currently says only `# Per-domain validators`; this file keeps its own boundary explicit. |
| Broad `tools/validators/fauna/README.md` | **NOT FOUND in this task** | This path currently serves as the inspected Fauna validator index. |
| Fauna domain doctrine | **CONFIRMED in repo evidence / draft** | `docs/domains/fauna/README.md` defines scope, deny-by-default sensitive occurrence posture, geoprivacy requirements, and responsibility-root split. |
| Deny-by-default sensitivity ADR | **CONFIRMED in repo evidence / draft** | ADR-0010 draft states rare-species exact locations default to deny and public products require public-safe transform, review, receipt, policy, and rollback support. |
| Fauna proof lane | **CONFIRMED in repo evidence / draft** | `data/proofs/fauna/README.md` defines Fauna proof support and says sensitive proof material is deny-by-default. |
| Child README lanes | **NONE CONFIRMED IN THIS TASK** | No child Fauna validator README was verified while writing this index. |
| Executables, schemas, fixtures, policy bundles, and CI wiring | **NEEDS VERIFICATION** | No script names, test paths, schema maturity, policy bundles, receipts, runtime behavior, or CI behavior are claimed as implemented here. |

[Back to top](#top)

---

## Child lanes

No child README lanes were confirmed during this edit.

Future child lanes should be added only when they represent a distinct Fauna validator specialty, fixture family, edge, or public-surface invariant with accepted contracts, schemas, policy posture, fixtures, receipts, and report semantics.

Possible future children remain **PROPOSED** until verified:

- `occurrence/` for occurrence evidence, occurrence restriction, and public-safe occurrence derivatives;
- `geoprivacy/` for redaction/generalization/buffering/gridding/aggregation checks;
- `sensitive-site/` for nest, den, roost, hibernacula, spawning, breeding/aggregation, and steward-controlled records;
- `taxon-status/` for taxon identity, crosswalk, conservation/legal status, and source-role posture;
- `range-migration/` for range polygons, seasonal ranges, and migration-route claims;
- `disease-mortality/` for mortality and disease observation boundaries.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Per-domain Fauna validator index | `tools/validators/domains/fauna/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Cross-domain ecology/biodiversity validator context | `tools/validators/biodiversity/`, `tools/validators/cross-domain-joins/` |
| Fauna domain meaning | `docs/domains/fauna/`, `contracts/domains/fauna/` |
| Fauna schemas | `schemas/contracts/v1/domains/fauna/` or ADR-selected homes |
| Fauna policy rules | `policy/domains/fauna/`, `policy/sensitivity/fauna/`, or accepted policy homes |
| Source descriptors | `data/registry/sources/fauna/` or accepted source registry home |
| Evidence/proof support | `data/proofs/fauna/`, `data/proofs/` |
| Receipts | `data/receipts/` |
| Release decisions, manifests, rollback, corrections | `release/` |
| Tests and fixtures | `tests/validators/domains/fauna/`, `tests/domains/fauna/`, `fixtures/domains/fauna/`, or accepted conventions |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live below this folder when it checks declared Fauna invariants and delegates meaning, sensitivity, policy, evidence, and release authority to owning roots.
- **NEEDS VERIFICATION:** exact executable names, schema homes, policy bundle digests, source descriptors, fixtures, report destinations, receipts, runtime behavior, and CI wiring.
- **DENY:** using this folder as taxonomic authority, stewardship authority, Fauna contract home, schema home, policy home, source registry, evidence store, lifecycle data store, receipt store, release record store, public occurrence surface, public map product surface, or domain-meaning authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/domains/fauna/` include:

- this parent/index README;
- child README lanes for narrow Fauna validator families;
- optional parent runner code that delegates to child validators without redefining their rules;
- validators that check occurrence/source-role separation, taxon/status posture, geoprivacy transforms, public-safe derivatives, evidence closure, review state, policy decisions, release references, correction cascade, and rollback support;
- synthetic fixture references and test-surface guidance;
- docs or reports that explain validator scope without becoming authoritative Fauna doctrine.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/domains/fauna/` | Correct home |
|---|---|
| Shared validator plumbing | `tools/validators/_common/` |
| Fauna domain docs | `docs/domains/fauna/` |
| Fauna contracts | `contracts/domains/fauna/` |
| Schemas | `schemas/contracts/v1/...` |
| Policy and sensitivity rules | `policy/...` |
| Source descriptors | `data/registry/sources/...` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| EvidenceBundles, proofs, receipts, RedactionReceipts, AggregationReceipts | `data/proofs/`, `data/receipts/` |
| Release manifests, decisions, rollback, corrections | `release/` |
| Generated QA reports that are not source code | `artifacts/qa/` or accepted report lane |
| Tests and fixtures | `tests/` and fixture conventions |
| Public API, UI, map, tile, export, search, graph, Focus Mode, or AI runtime code | governed application/runtime roots |

[Back to top](#top)

---

## Fauna validator posture

Fauna validators must fail closed, deny, abstain, or route to steward review when a candidate:

- lacks EvidenceRef, EvidenceBundle, source descriptor, source-role, or taxon/status support;
- collapses occurrence evidence, restricted occurrence, public occurrence derivative, sensitive site, range polygon, seasonal range, migration route, mortality observation, disease observation, or invasive-species record;
- exposes sensitive taxa, exact occurrence geometry, nests, dens, roosts, hibernacula, spawning sites, breeding/aggregation sites, steward-controlled records, or reverse-engineerable derivatives;
- lacks a named geoprivacy transform, RedactionReceipt, AggregationReceipt, ReviewRecord, PolicyDecision, ReleaseManifest, correction path, or rollback target where required;
- maps, tiles, exports, searches, embeds, graphs, summarizes, or answers with Fauna content beyond the approved public-safe derivative;
- offers hunting, collection, disturbance, legal, health, emergency, or operational wildlife guidance outside an accepted governed authority path;
- bypasses lifecycle gates or treats validator output as release approval.

The validator lane must preserve the KFM lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

[Back to top](#top)

---

## Standard parent outcomes

| Outcome | Meaning |
|---|---|
| `FAUNA_DOMAIN_VALIDATORS_PASS` | Configured Fauna validators passed. |
| `FAUNA_DOMAIN_VALIDATORS_FAIL` | One or more configured validators failed. |
| `CHILD_VALIDATOR_MISSING` | Expected Fauna child validator lane or runner is absent. |
| `CHILD_VALIDATOR_FAILED` | Child validator reported one or more findings. |
| `EVIDENCE_REF_MISSING` | Required EvidenceRef or EvidenceBundle pointer is absent. |
| `SOURCE_ROLE_COLLAPSE` | Candidate collapses occurrence/source-role/object-family posture. |
| `TAXON_STATUS_UNVERIFIED` | Taxon identity, crosswalk, or conservation/legal status lacks support. |
| `SENSITIVE_OCCURRENCE_DENIED` | Exact or identifying sensitive occurrence is unsafe for public output. |
| `GEOPRIVACY_TRANSFORM_MISSING` | Required public-safe transform or profile is absent. |
| `REDACTION_OR_AGGREGATION_RECEIPT_MISSING` | Required transform receipt is absent. |
| `REVIEW_OR_POLICY_GAP` | Required review state or PolicyDecision is absent. |
| `RELEASE_REFERENCE_MISSING` | Required ReleaseManifest, correction path, or rollback target is absent. |
| `PUBLIC_SURFACE_LEAK_RISK` | Candidate is unsafe for public/governed output as shaped. |
| `REPORT_DESTINATION_INVALID` | QA report or receipt destination is outside an accepted root. |
| `IGNORED_WITH_REASON` | Finding was ignored under an explicit, reviewable rule. |
| `IGNORE_RULE_EXPIRED` | Ignore rule is stale and must be reviewed. |
| `ABSTAIN` | Validator cannot decide safely with available context. |
| `ERROR` | Validator could not safely complete. |

[Back to top](#top)

---

## Validation

Suggested future test surface:

```text
tests/validators/domains/fauna/
├── README.md
├── test_fauna_domain_validator_parent.py
└── fixtures/
    ├── valid_public_safe_occurrence_derivative/
    ├── missing_evidence_ref/
    ├── source_role_collapse/
    ├── taxon_status_unverified/
    ├── sensitive_occurrence_denied/
    ├── geoprivacy_transform_missing/
    ├── redaction_receipt_missing/
    ├── review_or_policy_gap/
    ├── public_surface_leak_risk/
    └── ignored_with_reason/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/domains/fauna
```

```bash
python tools/validators/domains/fauna/run_fauna_domain_validators.py --repo-root . --format json
```

> [!NOTE]
> This is a proposed interface, not proof that `run_fauna_domain_validators.py` or the test path exists.

[Back to top](#top)

---

## Review checklist

- [ ] Parent runner delegates to child validators instead of redefining their rules.
- [ ] Validator reads declared Fauna contracts, schemas, and policy rather than defining meaning locally.
- [ ] Sensitive taxa and exact occurrence details fail closed unless approved public-safe transform support exists.
- [ ] Occurrence evidence, restricted occurrence, public derivative, sensitive site, range, migration, mortality, disease, and invasive-species object families remain distinct.
- [ ] EvidenceBundle, geoprivacy transform, review, policy, release, rollback, and correction support are checked where required.
- [ ] Map, tile, search, graph, export, Focus Mode, and AI surfaces do not reveal restricted details or reverse-engineerable derivatives.
- [ ] Reports and receipts are written only to accepted roots.
- [ ] Validator output is not described as truth, policy, release, publication, or Directory Rules approval.
- [ ] Tests use public-safe or synthetic fixtures.
- [ ] Executable claims are backed by current repo evidence.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft README replacement for greenfield stub and current parent index for Fauna validators. |
| Next smallest safe change | Verify child validator scripts, accepted profiles, schemas, source descriptors, policy bundles, fixtures, report destinations, receipts, geoprivacy behavior, release linkage, and CI/runtime wiring before promoting this lane beyond draft. |
