<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-domains-people-dna-land-readme
title: tools/validators/domains/people-dna-land README
type: README
version: v0.2
status: draft
owner: TODO-tooling-qa-owner-plus-people-dna-land-steward-plus-consent-steward-plus-sensitivity-reviewer-plus-rights-holder-representative-plus-policy-steward-plus-release-steward
created: 2026-07-07
updated: 2026-09-01
policy_label: repository-facing; per-domain-validator-index; people-dna-land; living-person; DNA; consent; revocation; land-ownership; fail-closed; non-authoritative
owning_root: tools/
responsibility: proposed per-domain People/DNA/Land validator index for person assertions, genealogy relationships, restricted DNA evidence, consent grants, revocations, land instruments, ownership intervals, assessor/tax records, parcels, title/geometry anti-collapse, source-role separation, T4 deny-by-default posture, evidence, policy, release, correction, rollback, and public-surface denial checks while deferring domain meaning, consent decisions, policy decisions, proof records, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../../README.md
  - ../../_common/README.md
  - ../README.md
  - ../../cross-domain-joins/README.md
  - ../../cross-lane/README.md
  - ../../../../docs/domains/people-dna-land/README.md
  - ../../../../docs/domains/people-dna-land/SCOPE_AND_BOUNDARY.md
  - ../../../../docs/domains/people-dna-land/SENSITIVITY.md
  - ../../../../docs/domains/people-dna-land/PEOPLE_DOMAIN_MODEL.md
  - ../../../../docs/domains/people-dna-land/API_CONTRACTS.md
  - ../../../../docs/domains/people-dna-land/DATA_LIFECYCLE.md
  - ../../../../docs/domains/people-dna-land/MAP_UI_CONTRACTS.md
  - ../../../../docs/domains/people-dna-land/VERIFICATION_BACKLOG.md
  - ../../../../docs/domains/people-dna-land/sublanes/dna.md
  - ../../../../contracts/domains/people-dna-land/
  - ../../../../schemas/contracts/v1/domains/people-dna-land/
  - ../../../../policy/domains/people-dna-land/
  - ../../../../policy/sensitivity/people-dna-land/
  - ../../../../policy/consent/people-dna-land/
  - ../../../../data/registry/sources/people-dna-land/
  - ../../../../data/proofs/
  - ../../../../data/receipts/
  - ../../../../release/
notes:
  - "This index records the bounded executable validators present at the reviewed branch checkpoint; presence is not policy activation, semantic completeness, source admission, or release authority."
  - "No broad tools/validators/people-dna-land/README.md was found during this task, so this path currently serves as the inspected per-domain People/DNA/Land validator index."
  - "This is KFM's strictest sensitivity lane. Living-person fields, raw DNA, private person-parcel joins, and DNA-derived hypotheses are deny-by-default unless scoped consent, review, policy, evidence, release, correction, rollback, and public-safe transform support authorize a derivative."
  - "Consent is revocable. Revocation must propagate to downstream cleanup, tombstone/embargo behavior, cache invalidation, graph/search/vector/AI withdrawal where applicable, correction records, and rollback targets."
  - "Validators enforce declared contracts, schemas, and policy. They do not define person identity, consent validity, title truth, parcel boundary truth, EvidenceBundle content, policy decisions, release decisions, or public outputs."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/domains/people-dna-land

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-people--dna--land--validators-informational)
![sensitivity](https://img.shields.io/badge/sensitivity-T4%20default-critical)
![authority](https://img.shields.io/badge/authority-index--only-lightgrey)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/domains/people-dna-land/` is the proposed per-domain People/DNA/Land validator index for person assertions, genealogy relationships, restricted DNA evidence, consent grants, revocations, land instruments, ownership intervals, assessor/tax records, parcels, title/geometry anti-collapse, source-role separation, deny-by-default sensitivity, evidence, policy, release, correction, rollback, and public-surface denial checks.

---

## Purpose

`tools/validators/domains/people-dna-land/` exists to organize People/DNA/Land validators under the durable `tools/validators/` surface.

The durable KFM question for this index is:

> Do People/DNA/Land candidates preserve assertion-first identity, consent scope, revocation state, source-role posture, title/parcel boundary distinctions, living-person and DNA sensitivity, neighboring-domain ownership, evidence closure, review state, policy decisions, release readiness, correction paths, rollback support, and public-surface denial boundaries before they reach any governed output?

The answer should be a navigable validator index and deterministic validation outputs from configured child lanes. This folder should not create person truth, relationship truth, DNA truth, consent validity, title truth, parcel-boundary truth, EvidenceBundles, PolicyDecisions, release decisions, public map layers, API payloads, or AI answers.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/domains/people-dna-land/README.md` | **CONFIRMED** | This README replaces the previous greenfield stub. |
| Parent per-domain validators README | **CONFIRMED stub** | `tools/validators/domains/README.md` currently says only `# Per-domain validators`; this file keeps its own boundary explicit. |
| Broad `tools/validators/people-dna-land/README.md` | **NOT FOUND in this task** | This path currently serves as the inspected People/DNA/Land validator index. |
| People/DNA/Land domain doctrine | **CONFIRMED in repo evidence / draft** | `docs/domains/people-dna-land/README.md` defines the lane as assertion-first person evidence, genealogy, restricted DNA evidence, land instruments, ownership intervals, consent, policy, review, correction, graph projection, EvidenceBundle views, and rollback. |
| Boundary and sensitivity doctrine | **CONFIRMED in repo evidence / draft** | `docs/domains/people-dna-land/SCOPE_AND_BOUNDARY.md` and `SENSITIVITY.md` define this as a T4/deny-by-default sensitive bounded context with consent, revocation, DNA, living-person, and private land controls. |
| Segment naming | **CONFLICTED / NEEDS ADR** | Domain docs record the open `people` vs `people-dna-land` segment conflict for some schema/contract/policy roots. This README follows the requested path and Directory Rules-style `people-dna-land` segment while marking implementation homes as needs verification. |
| Child README lanes | **NONE** | This directory currently keeps its executable validators flat; distinct subdirectories remain proposal-only. |
| Executable validator set | **CONFIRMED / BOUNDED** | Eight local Python entrypoints are present. They perform structural, fixture-scoped, or delegated fail-closed checks; none grants semantic, consent, source-admission, policy, release, or publication authority. |
| Pipeline and CI binding | **CONFIRMED / BOUNDED** | The People/DNA/Land dispatcher and workflow invoke the reviewed validator/test set with deterministic no-network settings. Proof production and release remain explicit holds. |

[Back to top](#top)

---

## Executable checkpoint

The reviewed branch contains these local validator entrypoints:

| Entrypoint | Bounded role |
|---|---|
| `validate_schema.py` | Strict JSON and Draft 2020-12 structural preflight for the canonical domain schema inventory. |
| `validate_evidence_bundle.py` | Fail-closed adapter to the shared People/DNA/Land EvidenceBundle projection validator. |
| `validate_source_descriptor.py` | Fail-closed adapter to the shared SourceDescriptor validator; it does not admit or activate a source. |
| `validate_catalog_matrix.py` | Fail-closed adapter to shared CatalogMatrix closure checks; catalog authority remains external. |
| `validate_domain_layer_descriptor.py` | Structural schema and synthetic fixture-polarity check for the proposed downstream layer carrier. |
| `validate_domain_feature_identity.py` | Structural schema and synthetic fixture-polarity check for the proposed deterministic identity carrier; identity remains distinct from truth. |
| `validate_consent_overlay.py` | Synthetic, fixture-only consent-overlay safety validation with explicit living-person and raw-genomic denial. |
| `validate_consent_revocation_propagation_assessment.py` | Synthetic assessment of declared revocation propagation; it does not execute cleanup or rollback. |

The stable dispatcher at `pipelines/domains/people-dna-land/validate.py` also routes
the governed living-person screen, historical-resolution validator, and shared
CorrectionNotice validator. The assessment-only rollback seam is
`pipelines/domains/people-dna-land/rollback.py`.

These executable seams validate caller-provided schemas or deterministic
synthetic fixtures without network access. They do not resolve identity,
kinship, consent legal sufficiency, residence, migration, ownership, title,
rights, public safety, policy approval, release, correction execution,
withdrawal execution, or publication.

[Back to top](#top)

---

## Child lanes

No child README lanes were confirmed during this edit.

Future child lanes should be added only when they represent a distinct People/DNA/Land validator specialty, fixture family, edge, or public-surface invariant with accepted contracts, schemas, policy posture, consent posture, fixtures, receipts, and report semantics.

Possible future children remain **PROPOSED** until verified:

- `consent/` for consent scope, duration, revocation, delegation, evidence, and downstream cleanup checks;
- `dna/` for raw DNA denial, token handling, segment/triangulation restrictions, aggregate/k-anonymized derivative checks, and DNA-derived hypothesis posture;
- `living-person/` for living-person field denial, masking, public-safe derivatives, and consent-gated release checks;
- `genealogy/` for assertion-first person identity, relationship assertions, relationship hypotheses, source-role separation, and review posture;
- `land-ownership/` for land instruments, ownership intervals, chain-of-title reasoning, assessor/tax records, parcel versions, and title/geometry anti-collapse;
- `person-parcel-join/` for private person-parcel joins, most-restrictive-policy propagation, public-surface denial, and rollback behavior;
- `revocation-cascade/` for tombstone/embargo cleanup, downstream invalidation, graph/search/vector/AI withdrawal, correction, and rollback target checks.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Per-domain People/DNA/Land validator index | `tools/validators/domains/people-dna-land/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Cross-domain invariant validators | `tools/validators/cross-domain-joins/` |
| People/DNA/Land domain meaning | `docs/domains/people-dna-land/`, `contracts/domains/people-dna-land/` or ADR-selected contract home |
| Consent and sensitivity doctrine | `docs/domains/people-dna-land/`, `policy/consent/...`, `policy/sensitivity/...`, or accepted policy homes |
| Machine schemas | `schemas/contracts/v1/...` or ADR-selected schema home after segment conflict resolution |
| Policy rules | `policy/domains/people-dna-land/`, `policy/sensitivity/...`, `policy/consent/...`, or accepted policy homes |
| Source descriptors | `data/registry/sources/people-dna-land/` or accepted source registry home |
| Evidence/proof support | `data/proofs/` |
| Receipts | `data/receipts/` |
| Release decisions, manifests, rollback, corrections | `release/` |
| Tests and fixtures | `tests/validators/domains/people-dna-land/`, `tests/domains/people-dna-land/`, `fixtures/domains/people-dna-land/`, or accepted conventions |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live below this folder when it checks declared People/DNA/Land invariants and delegates meaning, consent, sensitivity, policy, evidence, and release authority to owning roots.
- **NEEDS VERIFICATION:** exact executable names, schema homes, policy bundle digests, consent bundle behavior, source descriptors, fixtures, report destinations, receipts, runtime behavior, and CI wiring.
- **DENY:** using this folder as person-identity authority, consent authority, DNA authority, title authority, parcel-boundary authority, contract home, schema home, policy home, source registry, evidence store, lifecycle data store, receipt store, release record store, public map product surface, or domain-meaning authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/domains/people-dna-land/` include:

- this parent/index README;
- child README lanes for narrow People/DNA/Land validator families;
- optional parent runner code that delegates to child validators without redefining their rules;
- validators that check assertion-first person identity, relationship claims, consent scope, revocation state, restricted DNA evidence, aggregate/k-anonymized derivative posture, land instruments, ownership intervals, title/parcel anti-collapse, assessor/tax administrative posture, public-safe geometry, evidence closure, review state, policy decisions, release references, correction cascade, and rollback support;
- validators that check cross-lane joins preserve Settlements, Roads/Rail/Trade, Archaeology, Agriculture, Frontier Matrix, Spatial Foundation, and other neighboring-domain authority boundaries;
- synthetic fixture references and test-surface guidance;
- docs or reports that explain validator scope without becoming authoritative People/DNA/Land doctrine.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/domains/people-dna-land/` | Correct home |
|---|---|
| Shared validator plumbing | `tools/validators/_common/` |
| People/DNA/Land domain docs | `docs/domains/people-dna-land/` |
| Domain contracts | `contracts/domains/people-dna-land/` or ADR-selected home |
| Schemas | `schemas/contracts/v1/...` |
| Policy, sensitivity, or consent rules | `policy/...` |
| Source descriptors | `data/registry/sources/...` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| EvidenceBundles, proofs, receipts, consent receipts, revocation receipts, RedactionReceipts, AggregationReceipts | `data/proofs/`, `data/receipts/` |
| Release manifests, decisions, rollback, corrections | `release/` |
| Generated QA reports that are not source code | `artifacts/qa/` or accepted report lane |
| Tests and fixtures | `tests/` and fixture conventions |
| Public API, UI, map, tile, export, search, graph, Focus Mode, identity service, consent service, legal/title determination, or AI runtime code | governed application/runtime roots |

[Back to top](#top)

---

## People/DNA/Land validator posture

People/DNA/Land validators must fail closed, deny, abstain, or route to steward review when a candidate:

- lacks EvidenceRef, EvidenceBundle, source descriptor, source-role, rights, consent, review, time, or object-family support;
- collapses person assertion, person identity candidate, canonical person view, name assertion, life/residence/migration event, genealogy relationship, relationship hypothesis, family group, DNA match evidence, kit token, DNA segment, consent grant, revocation receipt, land ownership assertion, ownership interval, land instrument, assessor record, tax record, parcel, legal description, or parcel version into another role;
- treats an assessor/tax record, parcel geometry, or administrative record as title truth or boundary proof;
- treats DNA-derived hints, genealogy hypotheses, or relationship assertions as confirmed identity or relationship truth without review and evidence closure;
- exposes living-person fields, restricted DNA material, private person-parcel joins, or reverse-engineerable derivatives without consent, policy, review, public-safe transform, release, correction, and rollback support;
- ignores consent scope, consent expiry, revocation, delegated authority limits, embargo state, or downstream cleanup obligations;
- fails to invalidate graph/search/vector indexes, map products, story outputs, API payloads, Focus Mode outputs, and AI context after revocation or correction where applicable;
- joins People/DNA/Land records to archaeology, settlements, roads, agriculture, parcels, infrastructure, frontier routes, or other sensitive contexts without preserving the most restrictive policy and ownership posture;
- lacks a named redaction/generalization/aggregation transform, RedactionReceipt, AggregationReceipt, ConsentReceipt, RevocationReceipt, ReviewRecord, PolicyDecision, ReleaseManifest, correction path, or rollback target where required;
- maps, tiles, exports, searches, embeds, graphs, summarizes, or answers with People/DNA/Land content beyond the approved public-safe derivative;
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
| `PDL_DOMAIN_VALIDATORS_PASS` | Configured People/DNA/Land validators passed. |
| `PDL_DOMAIN_VALIDATORS_FAIL` | One or more configured validators failed. |
| `CHILD_VALIDATOR_MISSING` | Expected People/DNA/Land child validator lane or runner is absent. |
| `CHILD_VALIDATOR_FAILED` | Child validator reported one or more findings. |
| `EVIDENCE_REF_MISSING` | Required EvidenceRef or EvidenceBundle pointer is absent. |
| `CONSENT_REQUIRED` | Candidate requires scoped consent before use. |
| `CONSENT_MISSING_OR_EXPIRED` | Required consent is missing, expired, out of scope, or unverified. |
| `REVOCATION_ACTIVE` | Revocation blocks the candidate or requires downstream cleanup. |
| `SOURCE_ROLE_COLLAPSE` | Candidate collapses source-role or object-family posture. |
| `LIVING_PERSON_DENIED` | Living-person detail is unsafe for public output as shaped. |
| `DNA_PUBLICATION_DENIED` | Restricted DNA material or derivative is unsafe for public output as shaped. |
| `TITLE_PARCEL_AUTHORITY_COLLAPSE` | Administrative, assessor, tax, or parcel geometry record is treated as title/boundary truth. |
| `PERSON_PARCEL_JOIN_DENIED` | Person-parcel join is unsafe without consent, review, policy, and release controls. |
| `PUBLIC_SAFE_DERIVATIVE_MISSING` | Required public-safe transform or derivative profile is absent. |
| `REDACTION_OR_AGGREGATION_RECEIPT_MISSING` | Required transform receipt is absent. |
| `REVIEW_OR_POLICY_GAP` | Required review state or PolicyDecision is absent. |
| `RELEASE_REFERENCE_MISSING` | Required ReleaseManifest, correction path, or rollback target is absent. |
| `REVOCATION_CASCADE_GAP` | Downstream cleanup, tombstone, embargo, cache/index invalidation, correction, or rollback support is incomplete. |
| `CROSS_DOMAIN_AUTHORITY_COLLAPSE` | Candidate absorbs another domain's truth without preserving boundaries. |
| `PUBLIC_SURFACE_LEAK_RISK` | Candidate is unsafe for public/governed output as shaped. |
| `REPORT_DESTINATION_INVALID` | QA report or receipt destination is outside an accepted root. |
| `IGNORED_WITH_REASON` | Finding was ignored under an explicit, reviewable rule. |
| `IGNORE_RULE_EXPIRED` | Ignore rule is stale and must be reviewed. |
| `ABSTAIN` | Validator cannot decide safely with available context. |
| `ERROR` | Validator could not safely complete. |

[Back to top](#top)

---

## Validation

The bounded executable checkpoint is covered by focused tests under
`tests/validators/domains/people-dna-land/`,
`tests/validators/test_screen_living_persons.py`, and
`tests/pipelines/domains/people-dna-land/`. The domain workflow invokes those
tests plus deterministic consent-overlay and consent-revocation fixture replay.

A focused local command is:

```bash
KFM_NO_NETWORK=1 python -m pytest -q \
  tests/validators/domains/people-dna-land \
  tests/validators/test_screen_living_persons.py \
  tests/pipelines/domains/people-dna-land
```

The stable dispatcher can replay specific governed lanes, for example:

```bash
KFM_NO_NETWORK=1 python pipelines/domains/people-dna-land/validate.py domain-layer-descriptor --fixtures
KFM_NO_NETWORK=1 python pipelines/domains/people-dna-land/validate.py domain-feature-identity --fixtures
KFM_NO_NETWORK=1 python pipelines/domains/people-dna-land/validate.py correction-notice --fixtures
KFM_NO_NETWORK=1 python pipelines/domains/people-dna-land/rollback.py --fixtures
```

These commands are validation and assessment only. They do not activate policy,
mutate lifecycle data, perform correction or withdrawal, release, or publish.

[Back to top](#top)

---

## Review checklist

- [ ] Parent runner delegates to child validators instead of redefining their rules.
- [ ] Validator reads declared People/DNA/Land contracts, schemas, consent rules, and policy rather than defining meaning locally.
- [ ] Assertion-first identity, genealogy relationship, DNA evidence, consent, land instrument, ownership interval, assessor/tax record, and parcel-version object families remain distinct.
- [ ] Living-person, DNA, private person-parcel, and DNA-derived outputs fail closed unless approved consent, review, policy, and public-safe transform support exists.
- [ ] Consent scope, expiry, delegation, revocation, tombstone, embargo, correction, and rollback support are checked where required.
- [ ] Assessor/tax records and parcel geometry are not treated as title truth or boundary proof.
- [ ] Cross-domain joins preserve ownership, source role, sensitivity, and EvidenceBundle support.
- [ ] Map, tile, search, graph, export, Focus Mode, and AI surfaces do not reveal restricted details or reverse-engineerable derivatives.
- [ ] Reports and receipts are written only to accepted roots.
- [ ] Validator output is not described as truth, policy, consent approval, release, publication, title determination, or Directory Rules approval.
- [ ] Tests use public-safe or synthetic fixtures.
- [ ] Executable claims are backed by current repo evidence.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-09-01 |
| Review state | Bounded executable validator index; synthetic/no-network checks confirmed, broader authority held. |
| Next smallest safe change | Add or expand only dependency-ready fail-closed validators with synthetic fixture polarity and explicit non-authority boundaries; keep unresolved semantic, policy, consent, release, correction-execution, and publication work held. |
