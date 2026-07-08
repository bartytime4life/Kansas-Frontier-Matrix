<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-domains-geology-readme
title: tools/validators/domains/geology README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-geology-steward-plus-natural-resources-steward-plus-policy-steward-plus-evidence-steward-plus-release-steward
created: 2026-07-07
updated: 2026-07-07
policy_label: repository-facing; per-domain-validator-index; geology; natural-resources; subsurface; resource-sensitivity; fail-closed; non-authoritative
owning_root: tools/
responsibility: proposed per-domain Geology validator index for geologic maps, stratigraphy, lithology, structures, subsurface observations, boreholes, well logs, cores, geophysics, geochemistry, mineral occurrence/deposit/estimate/permit/production/reserve anti-collapse, hydrostratigraphy joins, sensitivity, evidence, policy, release, correction, rollback, and public-surface denial checks while deferring Geology meaning, policy decisions, proof records, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../../README.md
  - ../../_common/README.md
  - ../README.md
  - ../../cross-domain-joins/README.md
  - ../../cross-lane/README.md
  - ../../../../../docs/domains/geology/README.md
  - ../../../../../docs/domains/geology/POLICY.md
  - ../../../../../docs/domains/geology/PRESERVATION_MATRIX.md
  - ../../../../../docs/domains/geology/SOURCE_REGISTRY.md
  - ../../../../../docs/domains/geology/IDENTITY_MODEL.md
  - ../../../../../docs/domains/geology/sublanes/natural_resources.md
  - ../../../../../docs/runbooks/geology/SOURCE_REFRESH_RUNBOOK.md
  - ../../../../../contracts/domains/geology/
  - ../../../../../schemas/contracts/v1/domains/geology/
  - ../../../../../policy/domains/geology/
  - ../../../../../policy/sensitivity/geology/
  - ../../../../../data/registry/sources/geology/
  - ../../../../../data/proofs/
  - ../../../../../data/receipts/
  - ../../../../../release/
notes:
  - "This README replaces a greenfield stub. It does not confirm executable files."
  - "No broad tools/validators/geology/README.md was found during this task, so this path currently serves as the inspected per-domain Geology validator index."
  - "Geology validators must preserve the distinction between occurrence, deposit, estimate, permit, production, and reserve claims, and must not treat generalized map polygons or AI summaries as sourced observations."
  - "Exact borehole, core, well-log, private-well, sample, and extraction-targetable resource locations are sensitive by default and require public-safe transforms, review, evidence, policy, release, correction, and rollback support before public exposure."
  - "Validators enforce declared contracts, schemas, and policy. They do not define Geology meaning, create EvidenceBundles, approve release, or publish public outputs."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/domains/geology

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-geology--validators-informational)
![sensitivity](https://img.shields.io/badge/sensitivity-fail--closed-red)
![authority](https://img.shields.io/badge/authority-index--only-lightgrey)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/domains/geology/` is the proposed per-domain Geology validator index for geologic maps, stratigraphy, lithology, structures, subsurface observations, boreholes, well logs, cores, geophysics, geochemistry, mineral/resource anti-collapse, hydrostratigraphy joins, sensitivity, evidence, policy, release, correction, rollback, and public-surface denial checks.

---

## Purpose

`tools/validators/domains/geology/` exists to organize Geology and Natural Resources validators under the durable `tools/validators/` surface.

The durable KFM question for this index is:

> Do Geology candidates preserve geologic identity, source-role posture, occurrence/deposit/estimate/permit/production/reserve distinctions, subsurface and resource-location sensitivity, evidence closure, review state, policy decisions, release readiness, correction paths, rollback support, and public-surface denial boundaries before they reach any governed output?

The answer should be a navigable validator index and deterministic validation outputs from configured child lanes. This folder should not create Geology truth, resource truth, reserve estimates, permit truth, extraction guidance, EvidenceBundles, PolicyDecisions, release decisions, public map layers, API payloads, or AI answers.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/domains/geology/README.md` | **CONFIRMED** | This README replaces the previous greenfield stub. |
| Parent per-domain validators README | **CONFIRMED stub** | `tools/validators/domains/README.md` currently says only `# Per-domain validators`; this file keeps its own boundary explicit. |
| Broad `tools/validators/geology/README.md` | **NOT FOUND in this task** | This path currently serves as the inspected Geology validator index. |
| Geology domain doctrine | **CONFIRMED in repo evidence / draft** | `docs/domains/geology/README.md` defines scope, anti-collapse posture, lifecycle, public trust path, deny-by-default exact subsurface/private-well posture, and responsibility-root split. |
| Geology policy posture | **CONFIRMED in repo evidence / draft** | `docs/domains/geology/POLICY.md` states mixed-tier posture, exact borehole/well/resource sensitivity, claim-distinction rules, and fail-closed public promotion conditions. |
| Child README lanes | **NONE CONFIRMED IN THIS TASK** | No child Geology validator README was verified while writing this index. |
| Executables, schemas, fixtures, policy bundles, and CI wiring | **NEEDS VERIFICATION** | No script names, test paths, schema maturity, policy bundles, receipts, runtime behavior, or CI behavior are claimed as implemented here. |

[Back to top](#top)

---

## Child lanes

No child README lanes were confirmed during this edit.

Future child lanes should be added only when they represent a distinct Geology validator specialty, fixture family, edge, or public-surface invariant with accepted contracts, schemas, policy posture, fixtures, receipts, and report semantics.

Possible future children remain **PROPOSED** until verified:

- `subsurface-location/` for boreholes, cores, samples, well logs, private wells, and exact subsurface point sensitivity;
- `resource-claim/` for occurrence, deposit, estimate, permit, production, reserve, reclamation, and extraction-context anti-collapse;
- `stratigraphy/` for stratigraphic unit identity, correlation, geologic age, and cross-section evidence posture;
- `geologic-map/` for bedrock/surficial map polygons, structure/fault layers, and public-safe cartographic release;
- `hydrostratigraphy/` for Geology ↔ Hydrology joins without re-owning water observation or regulatory flood truth;
- `rights-source-role/` for KGS, USGS, KCC, licensed well-log, and rights-restricted source posture.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Per-domain Geology validator index | `tools/validators/domains/geology/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Cross-domain invariant validators | `tools/validators/cross-domain-joins/` |
| Geology domain meaning | `docs/domains/geology/`, `contracts/domains/geology/` |
| Natural Resources sublane doctrine | `docs/domains/geology/sublanes/natural_resources.md` |
| Geology schemas | `schemas/contracts/v1/domains/geology/` or ADR-selected homes |
| Geology policy rules | `policy/domains/geology/`, `policy/sensitivity/geology/`, or accepted policy homes |
| Source descriptors | `data/registry/sources/geology/`, `data/registry/geology/sources/`, or accepted source registry home |
| Evidence/proof support | `data/proofs/` |
| Receipts | `data/receipts/` |
| Release decisions, manifests, rollback, corrections | `release/` |
| Tests and fixtures | `tests/validators/domains/geology/`, `tests/domains/geology/`, `fixtures/domains/geology/`, or accepted conventions |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live below this folder when it checks declared Geology invariants and delegates meaning, sensitivity, policy, evidence, and release authority to owning roots.
- **NEEDS VERIFICATION:** exact executable names, schema homes, policy bundle digests, source descriptors, fixtures, report destinations, receipts, runtime behavior, and CI wiring.
- **DENY:** using this folder as geology doctrine, resource authority, contract home, schema home, policy home, source registry, evidence store, lifecycle data store, receipt store, release record store, public map product surface, extraction guidance surface, or domain-meaning authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/domains/geology/` include:

- this parent/index README;
- child README lanes for narrow Geology validator families;
- optional parent runner code that delegates to child validators without redefining their rules;
- validators that check source-role discipline, map/product lineage, subsurface point sensitivity, resource-claim anti-collapse, public-safe geometry, evidence closure, review state, policy decisions, release references, correction cascade, and rollback support;
- validators that check cross-lane joins preserve Hydrology, Soil, Hazards, Agriculture, Roads/Rail/Trade, Settlements/Infrastructure, People/Land, and other neighboring-domain authority boundaries;
- synthetic fixture references and test-surface guidance;
- docs or reports that explain validator scope without becoming authoritative Geology doctrine.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/domains/geology/` | Correct home |
|---|---|
| Shared validator plumbing | `tools/validators/_common/` |
| Geology domain docs | `docs/domains/geology/` |
| Geology contracts | `contracts/domains/geology/` |
| Schemas | `schemas/contracts/v1/...` |
| Policy and sensitivity rules | `policy/...` |
| Source descriptors | `data/registry/sources/...` or accepted registry home |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| EvidenceBundles, proofs, receipts, RedactionReceipts, AggregationReceipts | `data/proofs/`, `data/receipts/` |
| Release manifests, decisions, rollback, corrections | `release/` |
| Generated QA reports that are not source code | `artifacts/qa/` or accepted report lane |
| Tests and fixtures | `tests/` and fixture conventions |
| Public API, UI, map, tile, export, search, graph, Focus Mode, extraction guidance, or AI runtime code | governed application/runtime roots |

[Back to top](#top)

---

## Geology validator posture

Geology validators must fail closed, deny, abstain, or route to steward review when a candidate:

- lacks EvidenceRef, EvidenceBundle, source descriptor, source-role, rights, time, or object-family support;
- collapses occurrence, deposit, estimate, permit, production, reserve, reclamation, map polygon, borehole, well log, core, sample, geophysics, geochemistry, or hydrostratigraphic context;
- presents a generalized geologic map polygon, modeled interpretation, or AI summary as a sourced observation;
- exposes exact borehole, core, sample, private well, well-log, sensitive-resource, or extraction-targetable location without public-safe geometry and review support;
- joins geology records to People/Land, parcel, infrastructure, lease, title, permit, hydrology, or hazard contexts without preserving the most restrictive policy and ownership posture;
- lacks a named generalization/redaction/aggregation transform, RedactionReceipt, AggregationReceipt, ReviewRecord, PolicyDecision, ReleaseManifest, correction path, or rollback target where required;
- maps, tiles, exports, searches, embeds, graphs, summarizes, or answers with Geology content beyond the approved public-safe derivative;
- offers extraction, investment, legal, regulatory, emergency, safety, or operational guidance outside an accepted governed authority path;
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
| `GEOLOGY_DOMAIN_VALIDATORS_PASS` | Configured Geology validators passed. |
| `GEOLOGY_DOMAIN_VALIDATORS_FAIL` | One or more configured validators failed. |
| `CHILD_VALIDATOR_MISSING` | Expected Geology child validator lane or runner is absent. |
| `CHILD_VALIDATOR_FAILED` | Child validator reported one or more findings. |
| `EVIDENCE_REF_MISSING` | Required EvidenceRef or EvidenceBundle pointer is absent. |
| `SOURCE_ROLE_COLLAPSE` | Candidate collapses source-role or object-family posture. |
| `RESOURCE_CLAIM_COLLAPSE` | Occurrence, deposit, estimate, permit, production, or reserve claim is conflated. |
| `SUBSURFACE_LOCATION_DENIED` | Exact or identifying subsurface/private-well/resource location is unsafe for public output. |
| `PUBLIC_SAFE_GEOMETRY_MISSING` | Required generalized/redacted/aggregated geometry or profile is absent. |
| `REDACTION_OR_AGGREGATION_RECEIPT_MISSING` | Required transform receipt is absent. |
| `REVIEW_OR_POLICY_GAP` | Required review state or PolicyDecision is absent. |
| `RELEASE_REFERENCE_MISSING` | Required ReleaseManifest, correction path, or rollback target is absent. |
| `CROSS_DOMAIN_AUTHORITY_COLLAPSE` | Candidate absorbs another domain's truth into Geology without preserving boundaries. |
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
tests/validators/domains/geology/
├── README.md
├── test_geology_domain_validator_parent.py
└── fixtures/
    ├── valid_public_safe_geologic_map/
    ├── missing_evidence_ref/
    ├── source_role_collapse/
    ├── resource_claim_collapse/
    ├── subsurface_location_denied/
    ├── public_safe_geometry_missing/
    ├── redaction_receipt_missing/
    ├── review_or_policy_gap/
    ├── cross_domain_authority_collapse/
    └── ignored_with_reason/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/domains/geology
```

```bash
python tools/validators/domains/geology/run_geology_domain_validators.py --repo-root . --format json
```

> [!NOTE]
> This is a proposed interface, not proof that `run_geology_domain_validators.py` or the test path exists.

[Back to top](#top)

---

## Review checklist

- [ ] Parent runner delegates to child validators instead of redefining their rules.
- [ ] Validator reads declared Geology contracts, schemas, and policy rather than defining meaning locally.
- [ ] Occurrence, deposit, estimate, permit, production, reserve, reclamation, map polygon, borehole, well-log, core, sample, geophysics, geochemistry, and hydrostratigraphy object families remain distinct.
- [ ] Exact subsurface, private-well, and extraction-targetable resource details fail closed unless approved public-safe transform support exists.
- [ ] EvidenceBundle, public-safe geometry, review, policy, release, rollback, and correction support are checked where required.
- [ ] Cross-domain joins preserve ownership, source role, sensitivity, and EvidenceBundle support.
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
| Review state | Draft README replacement for greenfield stub and current parent index for Geology validators. |
| Next smallest safe change | Verify child validator scripts, accepted profiles, schemas, source descriptors, policy bundles, fixtures, report destinations, receipts, public-safe geometry behavior, release linkage, cross-domain join behavior, and CI/runtime wiring before promoting this lane beyond draft. |
