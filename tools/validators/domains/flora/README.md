<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-domains-flora-readme
title: tools/validators/domains/flora README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-flora-steward-plus-rare-plant-reviewer-plus-geoprivacy-reviewer-plus-policy-steward-plus-evidence-steward
created: 2026-07-07
updated: 2026-08-03
policy_label: repository-facing; per-domain-validator-index; flora; rare-plants; geoprivacy; fail-closed; non-authoritative
owning_root: tools/
responsibility: proposed per-domain Flora validator index for plant taxon identity, occurrence/specimen evidence, rare/protected/culturally sensitive flora controls, geoprivacy, vegetation/community products, invasive plants, phenology, restoration plantings, evidence, policy, release, correction, rollback, and public-surface denial checks while deferring Flora meaning, policy decisions, proof records, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../../README.md
  - ../../_common/README.md
  - ../README.md
  - ../../biodiversity/README.md
  - ../../cross-domain-joins/README.md
  - ../../cross-lane/README.md
  - ../../../../../docs/domains/flora/README.md
  - ../../../../../docs/domains/flora/CANONICAL_PATHS.md
  - ../../../../../docs/domains/flora/CONTINUITY_INVENTORY.md
  - ../../../../../docs/domains/flora/PUBLICATION_AND_ROLLBACK.md
  - ../../../../../docs/domains/flora/EXPANSION_PLAN.md
  - ../../../../../docs/adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md
  - ../../../../../contracts/domains/flora/
  - ../../../../../schemas/contracts/v1/domains/flora/
  - ../../../../../policy/domains/flora/
  - ../../../../../policy/sensitivity/flora/
  - ../../../../../data/registry/sources/flora/
  - ../../../../../data/proofs/
  - ../../../../../data/receipts/
  - ../../../../../release/
notes:
  - "This index confirms one bounded synthetic fixture-safety executable; broader Flora validation remains unverified."
  - "Flora rare, protected, culturally sensitive, steward-reviewed, and exact-location plant records are fail-closed unless a public-safe geoprivacy transform, review, policy, evidence, release, correction, and rollback path authorizes disclosure."
  - "Flora may reference Habitat, Fauna, Soil, Hydrology, Agriculture, Hazards, and other domains through governed joins, but it does not own their truth. Validators must preserve ownership, source role, sensitivity, and EvidenceBundle support."
  - "Validators enforce declared contracts, schemas, and policy. They do not define Flora meaning, create EvidenceBundles, make stewardship decisions, approve release, or publish public outputs."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/domains/flora

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-flora--validators-informational)
![sensitivity](https://img.shields.io/badge/sensitivity-fail--closed-red)
![authority](https://img.shields.io/badge/authority-bounded--fixture--validation-lightgrey)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/domains/flora/` is the proposed per-domain Flora validator index for plant taxon identity, occurrence/specimen evidence, rare/protected/culturally sensitive plant controls, geoprivacy, vegetation/community products, invasive plants, phenology, restoration plantings, evidence, policy, release, correction, rollback, and public-surface denial checks.

---

## Purpose

`tools/validators/domains/flora/` exists to organize Flora validators under the durable `tools/validators/` surface.

The durable KFM question for this index is:

> Do Flora candidates preserve plant taxonomic identity, occurrence/specimen source-role posture, rare/protected/culturally sensitive location controls, geoprivacy, evidence closure, review state, policy decisions, release readiness, correction paths, rollback support, and public-surface denial boundaries before they reach any governed output?

The answer should be a navigable validator index and deterministic validation outputs from configured child lanes. This folder should not create Flora truth, botanical authority, stewardship decisions, EvidenceBundles, geoprivacy transforms, PolicyDecisions, release decisions, public map layers, API payloads, or AI answers.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/domains/flora/README.md` | **CONFIRMED** | This README replaces the previous greenfield stub. |
| Parent per-domain validators README | **CONFIRMED stub** | `tools/validators/domains/README.md` currently says only `# Per-domain validators`; this file keeps its own boundary explicit. |
| Flora domain doctrine | **CONFIRMED in repo evidence / draft** | `docs/domains/flora/README.md` defines scope, lifecycle, fail-closed rare-plant sensitivity posture, responsibility-root split, and cross-lane ownership constraints. |
| Deny-by-default sensitivity ADR | **CONFIRMED in repo evidence / draft** | ADR-0010 draft states rare-species exact locations default to deny and public products require public-safe transform, review, receipt, policy, and rollback support. |
| Bounded executable profile | **CONFIRMED** | `validate_public_safe_fixture.py` checks only the closed synthetic, fixture-only, withheld-location profile documented below. |
| Executable test and CI wiring | **CONFIRMED for one profile** | `tests/domains/flora/test_flora_smoke.py` and `.github/workflows/domain-flora.yml` execute the bounded profile without network access. |
| Schemas, policy bundles, geoprivacy transforms, proof, and release | **NEEDS VERIFICATION** | The fixture profile does not validate Flora schemas, accept policy, perform transformation, close evidence, or approve release. |

[Back to top](#top)

---

## Accepted bounded executable

`validate_public_safe_fixture.py` validates one repository-local safety envelope:

- every accepted string, including identifiers, labels, evidence references, and caveats, must match the exact synthetic profile vocabulary;
- `source_role` must remain `synthetic` and the reality boundary must remain explicit;
- spatial support must be `withheld`; coordinate/location fields, numeric location values, URL-shaped clues, and coordinate-shaped text fail closed;
- rights, evidence, review, correction, and rollback state remain fixture-only;
- policy is not evaluated, geoprivacy is not applied because no location is present, release is held, and promotion is ineligible;
- unknown key paths are sanitized, and the bounded, duplicate-free parser and CLI are deterministic, offline, and non-echoing.

Run the accepted profile from the repository root:

```bash
KFM_NO_NETWORK=1 python tests/domains/flora/test_flora_smoke.py --verbose
python tools/validators/domains/flora/validate_public_safe_fixture.py \
  fixtures/domains/flora/valid/non_sensitive_occurrence.json
```

A pass proves conformance only to this synthetic fixture profile. It does not establish occurrence truth, taxonomic identity, source admission, rights or sensitivity clearance, policy approval, a geoprivacy transform, an EvidenceBundle, public safety, or release readiness. County, grid, generalized-area, and exact-geometry rules remain outside this executable.

[Back to top](#top)

---

## Child lanes

No child README lanes were confirmed during this edit.

Future child lanes should be added only when they represent a distinct Flora validator specialty, fixture family, edge, or public-surface invariant with accepted contracts, schemas, policy posture, fixtures, receipts, and report semantics.

Possible future children remain **PROPOSED** until verified:

- `occurrence/` for flora occurrence evidence, specimen support, and public-safe occurrence derivatives;
- `geoprivacy/` for redaction/generalization/buffering/gridding/aggregation checks;
- `rare-plant/` for rare, protected, culturally sensitive, steward-reviewed, or restricted plant records;
- `taxon-status/` for plant taxon identity, synonym/crosswalk, conservation/legal status, and source-role posture;
- `vegetation-community/` for vegetation/community surfaces, habitat associations, and ownership-preserving joins;
- `invasive-phenology/` for invasive plant and phenology observations without operational or regulatory overclaim.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Per-domain Flora validator index | `tools/validators/domains/flora/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Cross-domain ecology/biodiversity validator context | `tools/validators/biodiversity/`, `tools/validators/cross-domain-joins/` |
| Flora domain meaning | `docs/domains/flora/`, `contracts/domains/flora/` |
| Flora schemas | `schemas/contracts/v1/domains/flora/` or ADR-selected homes |
| Flora policy rules | `policy/domains/flora/`, `policy/sensitivity/flora/`, or accepted policy homes |
| Source descriptors | `data/registry/sources/flora/` or accepted source registry home |
| Evidence/proof support | `data/proofs/` |
| Receipts | `data/receipts/` |
| Release decisions, manifests, rollback, corrections | `release/` |
| Tests and fixtures | `tests/validators/domains/flora/`, `tests/domains/flora/`, `fixtures/domains/flora/`, or accepted conventions |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live below this folder when it checks declared Flora invariants and delegates meaning, sensitivity, policy, evidence, and release authority to owning roots.
- **CONFIRMED:** the one bounded executable, fixture corpus, focused test, and CI command named above.
- **NEEDS VERIFICATION:** every broader executable, schema home, policy bundle digest, production source descriptor, report destination, geoprivacy transform, proof path, and release path.
- **DENY:** using this folder as botanical authority, stewardship authority, Flora contract home, schema home, policy home, source registry, evidence store, lifecycle data store, receipt store, release record store, public occurrence surface, public map product surface, or domain-meaning authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/domains/flora/` include:

- this parent/index README;
- child README lanes for narrow Flora validator families;
- optional parent runner code that delegates to child validators without redefining their rules;
- validators that check occurrence/specimen source-role separation, plant taxon/status posture, rare-plant geoprivacy, public-safe derivatives, evidence closure, review state, policy decisions, release references, correction cascade, and rollback support;
- validators that check cross-lane joins preserve Habitat, Fauna, Soil, Hydrology, Agriculture, Hazards, Archaeology, and People/Land ownership boundaries;
- synthetic fixture references and test-surface guidance;
- docs or reports that explain validator scope without becoming authoritative Flora doctrine.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/domains/flora/` | Correct home |
|---|---|
| Shared validator plumbing | `tools/validators/_common/` |
| Flora domain docs | `docs/domains/flora/` |
| Flora contracts | `contracts/domains/flora/` |
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

## Flora validator posture

Flora validators must fail closed, deny, abstain, or route to steward review when a candidate:

- lacks EvidenceRef, EvidenceBundle, source descriptor, source-role, taxon/status, or specimen/occurrence support;
- collapses occurrence evidence, specimen evidence, restricted occurrence, public occurrence derivative, rare-plant location, vegetation-community surface, invasive-plant record, phenology observation, or restoration planting record;
- exposes rare, protected, culturally sensitive, steward-reviewed, exact occurrence geometry, or reverse-engineerable derivatives;
- lacks a named geoprivacy transform, RedactionReceipt, AggregationReceipt, ReviewRecord, PolicyDecision, ReleaseManifest, correction path, or rollback target where required;
- maps, tiles, exports, searches, embeds, graphs, summarizes, or answers with Flora content beyond the approved public-safe derivative;
- imports another domain's truth into a Flora artifact without preserving ownership, source role, sensitivity, and EvidenceBundle support;
- offers collection, disturbance, regulatory, legal, emergency, or operational botanical guidance outside an accepted governed authority path;
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
| `FLORA_DOMAIN_VALIDATORS_PASS` | Configured Flora validators passed. |
| `FLORA_DOMAIN_VALIDATORS_FAIL` | One or more configured validators failed. |
| `CHILD_VALIDATOR_MISSING` | Expected Flora child validator lane or runner is absent. |
| `CHILD_VALIDATOR_FAILED` | Child validator reported one or more findings. |
| `EVIDENCE_REF_MISSING` | Required EvidenceRef or EvidenceBundle pointer is absent. |
| `SOURCE_ROLE_COLLAPSE` | Candidate collapses occurrence/specimen/source-role/object-family posture. |
| `TAXON_STATUS_UNVERIFIED` | Plant taxon identity, synonym/crosswalk, or conservation/legal status lacks support. |
| `SENSITIVE_FLORA_LOCATION_DENIED` | Exact or identifying sensitive flora location is unsafe for public output. |
| `GEOPRIVACY_TRANSFORM_MISSING` | Required public-safe transform or profile is absent. |
| `REDACTION_OR_AGGREGATION_RECEIPT_MISSING` | Required transform receipt is absent. |
| `REVIEW_OR_POLICY_GAP` | Required review state or PolicyDecision is absent. |
| `RELEASE_REFERENCE_MISSING` | Required ReleaseManifest, correction path, or rollback target is absent. |
| `CROSS_DOMAIN_AUTHORITY_COLLAPSE` | Candidate absorbs another domain's truth into Flora without preserving boundaries. |
| `PUBLIC_SURFACE_LEAK_RISK` | Candidate is unsafe for public/governed output as shaped. |
| `REPORT_DESTINATION_INVALID` | QA report or receipt destination is outside an accepted root. |
| `IGNORED_WITH_REASON` | Finding was ignored under an explicit, reviewable rule. |
| `IGNORE_RULE_EXPIRED` | Ignore rule is stale and must be reviewed. |
| `ABSTAIN` | Validator cannot decide safely with available context. |
| `ERROR` | Validator could not safely complete. |

[Back to top](#top)

---

## Validation

Current accepted command:

```bash
KFM_NO_NETWORK=1 python tests/domains/flora/test_flora_smoke.py --verbose
```

All broader test and parent-runner surfaces below remain suggested future work.

Suggested future test surface:

```text
tests/validators/domains/flora/
├── README.md
├── test_flora_domain_validator_parent.py
└── fixtures/
    ├── valid_public_safe_occurrence_derivative/
    ├── missing_evidence_ref/
    ├── source_role_collapse/
    ├── taxon_status_unverified/
    ├── sensitive_flora_location_denied/
    ├── geoprivacy_transform_missing/
    ├── redaction_receipt_missing/
    ├── review_or_policy_gap/
    ├── cross_domain_authority_collapse/
    └── ignored_with_reason/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/domains/flora
```

```bash
python tools/validators/domains/flora/run_flora_domain_validators.py --repo-root . --format json
```

> [!NOTE]
> This is a proposed interface, not proof that `run_flora_domain_validators.py` or the test path exists.

[Back to top](#top)

---

## Review checklist

- [ ] Parent runner delegates to child validators instead of redefining their rules.
- [ ] Validator reads declared Flora contracts, schemas, and policy rather than defining meaning locally.
- [ ] Sensitive Flora details fail closed unless approved public-safe transform support exists.
- [ ] Occurrence, specimen, restricted occurrence, public derivative, rare-location, vegetation-community, invasive, phenology, and restoration object families remain distinct.
- [ ] EvidenceBundle, geoprivacy transform, review, policy, release, rollback, and correction support are checked where required.
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
| Last reviewed | 2026-08-03 |
| Review state | One fixture-only, no-location safety profile is executable; broader Flora validation remains draft. |
| Next smallest safe change | Review the bounded profile and its receipt, then separately resolve schema, policy, geoprivacy-transform, proof, and release authority before widening it. |
