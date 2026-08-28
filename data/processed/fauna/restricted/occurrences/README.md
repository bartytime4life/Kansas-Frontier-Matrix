<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/data-processed-fauna-restricted-occurrences-readme
title: data/processed/fauna/restricted/occurrences/README.md — Fauna Restricted Occurrences Processed Data README
version: v0.1
type: readme; data-lifecycle-sublane; processed-stage-guide; fauna-domain-lane; restricted-access-lane; restricted-occurrence-lane; geoprivacy-gated
status: draft; PROPOSED; data-root; processed-stage; fauna; restricted; occurrences; reviewer-only; named-agreement; sensitive-occurrence; deny-by-default; access-controlled; release-gated
owners: OWNER_TBD — Fauna steward · Occurrence steward · Sensitivity reviewer · Rights-holder representative · Access-control steward · Data steward · Pipeline steward · Evidence steward · Policy steward · Release steward · Docs steward
created: NEEDS VERIFICATION — one-character placeholder existed before v0.1 expansion
updated: 2026-06-25
policy_label: public-doc; data; processed; fauna; restricted; occurrences; geoprivacy; access-controlled; deny-by-default
tags: [kfm, data, processed, fauna, restricted, occurrences, occurrence-record, sensitive-occurrence, exact-geometry, reviewer-only, named-agreement, T2, T3, T4, steward-controlled, geoprivacy, rare-species, RedactionReceipt, ReviewRecord, PolicyDecision, CorrectionNotice, RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, PUBLISHED, EvidenceBundle, SourceDescriptor]
related:
  - ../README.md
  - ../../public/README.md
  - ../../public/occurrences_generalized/README.md
  - ../../README.md
  - ../../../README.md
  - ../../../../README.md
  - ../../../../../docs/domains/fauna/README.md
  - ../../../../../docs/domains/fauna/SENSITIVITY.md
  - ../../../../../docs/adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md
  - ../../../../../policy/domains/fauna/
  - ../../../../../policy/sensitivity/fauna/
  - ../../../../../contracts/domains/fauna/
  - ../../../../../schemas/contracts/v1/domains/fauna/
  - ../../../../raw/fauna/
  - ../../../../work/fauna/
  - ../../../../quarantine/fauna/
  - ../../../../catalog/domain/fauna/
  - ../../../../catalog/stac/fauna/
  - ../../../../catalog/dcat/fauna/
  - ../../../../catalog/prov/fauna/
  - ../../../../triplets/
  - ../../../../published/
  - ../../../../proofs/
  - ../../../../receipts/
  - ../../../../registry/sources/fauna/
  - ../../../../../release/candidates/fauna/
  - ../../../../../release/
  - ../../../../../pipelines/domains/fauna/
  - ../../../../../tools/validators/
notes:
  - "This file replaces a one-character placeholder at `data/processed/fauna/restricted/occurrences/README.md`."
  - "This is a child PROCESSED-stage lane under `data/processed/fauna/restricted/` for restricted occurrence artifacts. It is not a public-candidate lane, PUBLISHED lane, direct public API/UI output, source registry, proof store, receipt store, policy authority, release authority, or permission to expose occurrence data."
  - "Restricted occurrence artifacts must preserve source role, rights, sensitivity tier/rank, exact-geometry posture, access basis, reviewer/rights-holder agreement linkage, evidence linkage, policy decision, correction path, and rollback target."
  - "Exact sensitive occurrence geometry, sensitive-taxon coordinates, steward-controlled occurrence records, and re-identifying joins must remain fail-closed unless policy/review/agreement explicitly permits restricted handling."
  - "Any public representation requires a separate governed transition to generalized, aggregated, redacted, or suppressed public-candidate artifacts with receipts and release controls."
  - "This README is a lane guide only. Policy decides admissibility; contracts define object meaning; schemas define machine shape; release/access records decide disclosure."
  - "Rollback target for this expansion is previous placeholder blob SHA `e25f1814e51579d5f55c0f1fe0135ddb28a47f4a`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# data/processed/fauna/restricted/occurrences

> Fauna PROCESSED-stage child lane for restricted occurrence artifacts: exact, sensitive, steward-controlled, rights-limited, reviewer-only, named-agreement, or otherwise non-public occurrence records that have moved beyond RAW/WORK/QUARANTINE but remain inside the trust membrane.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: data/processed/fauna/restricted/occurrences" src="https://img.shields.io/badge/root-data%2Fprocessed%2Ffauna%2Frestricted%2Foccurrences-blue">
  <img alt="Domain: fauna" src="https://img.shields.io/badge/domain-fauna-2ea44f">
  <img alt="Lifecycle: PROCESSED" src="https://img.shields.io/badge/lifecycle-PROCESSED-purple">
  <img alt="Access: restricted" src="https://img.shields.io/badge/access-restricted-critical">
  <img alt="Posture: deny by default" src="https://img.shields.io/badge/posture-deny__by__default-critical">
</p>

**Status:** draft / PROPOSED  
**Owners:** OWNER_TBD — Fauna steward · Occurrence steward · Sensitivity reviewer · Rights-holder representative · Access-control steward · Data steward · Pipeline steward · Evidence steward · Policy steward · Release steward · Docs steward  
**Path:** `data/processed/fauna/restricted/occurrences/README.md`  
**Owning root:** `data/processed/`  
**Domain segment:** `fauna`  
**Parent lane:** `data/processed/fauna/restricted/`  
**Sublane:** `occurrences` / restricted occurrence processed fauna  
**Lifecycle stage:** `PROCESSED`  
**Exposure posture:** not public; access requires governed policy, role, reviewer, rights-holder, named-agreement, or steward authorization. Any public representation requires a separate governed transition to generalized, aggregated, redacted, withheld, or suppressed artifacts with catalog, release, correction, and rollback controls.  
**Truth posture:** CONFIRMED target was a one-character placeholder · CONFIRMED restricted parent lane is non-public and access-controlled · CONFIRMED Fauna doctrine has T2 reviewer-only, T3 named-agreement, and T4 denied tiers · PROPOSED restricted occurrence child-lane details · NEEDS VERIFICATION for actual child inventory, object contracts, schemas, access-control enforcement, validators, fixtures, receipts, policy enforcement, release linkage, and governed route behavior.

**Quick jumps:** [Purpose](#purpose) · [Lifecycle boundary](#lifecycle-boundary) · [Repo fit](#repo-fit) · [Accepted contents](#accepted-contents) · [Exclusions](#exclusions) · [Restricted-occurrence requirements](#restricted-occurrence-requirements) · [Occurrence guardrails](#occurrence-guardrails) · [Directory map](#directory-map) · [Evidence ledger](#evidence-ledger) · [Validation checklist](#validation-checklist) · [Rollback](#rollback)

---

## Purpose

`data/processed/fauna/restricted/occurrences/` holds processed fauna occurrence artifacts that are not public-safe because of sensitivity, exact geometry, taxa status, rights, steward control, named agreement, reviewer-only access, source terms, re-identification risk, or other policy constraints.

This lane is for restricted processed occurrence records that may support authenticated review, stewardship, rights-holder review, correction, audit, redaction/generalization planning, or restricted collaboration. It is not a public-candidate lane, not a publication lane, and not a public access surface.

A restricted occurrence may later support a public-safe derivative only by a governed transition that creates the required RedactionReceipt, AggregationReceipt where applicable, ReviewRecord, PolicyDecision, ReleaseManifest, correction path, and rollback target. The restricted source occurrence remains restricted unless policy explicitly changes its status.

## Lifecycle boundary

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

```mermaid
flowchart LR
  RAW[data/raw/fauna] --> WORK[data/work/fauna]
  WORK --> QUAR[data/quarantine/fauna]
  WORK --> OCC[data/processed/fauna/restricted/occurrences]
  QUAR --> OCC
  OCC --> RES[data/processed/fauna/restricted]
  OCC -. transform request .-> GEN[data/processed/fauna/public/occurrences_generalized]
  OCC -. restricted catalog only if policy allows .-> CAT[data/catalog/domain/fauna]
  OCC -. supports .-> PROOF[data/proofs]
  OCC -. emits / references .-> RECEIPT[data/receipts]
  CAT -. released safe representation only .-> PUBLISHED[data/published/.../fauna]
  GEN -. after catalog and release only .-> PUBLISHED
  PUBLISHED --> REL[release]
```

`data/processed/fauna/restricted/occurrences/` is upstream of any catalog, public-candidate, published, or release surface. It must not be used as a normal public map/API/UI/AI source.

## Repo fit

| Responsibility | Correct home | Rule |
|---|---|---|
| Raw occurrence records, source-native downloads, original exact geometry, steward originals, camera/acoustic source payloads, source logs, source identifiers, or media | `data/raw/fauna/` | Not this lane. |
| In-process occurrence joins, matching, geoprivacy work, QA, reconciliation, redaction trials, transform experiments, or scratch products | `data/work/fauna/` | Not this lane. |
| Unresolved sensitive, rights-unclear, source-role-unclear, malformed, disputed, unsafe, or not-yet-reviewed occurrence material | `data/quarantine/fauna/` | Not this lane until minimally reviewed and admitted as restricted processed material. |
| Restricted occurrence processed artifacts | `data/processed/fauna/restricted/occurrences/` | This lane. |
| Parent restricted fauna lane | `data/processed/fauna/restricted/` | Parent lane; still not public. |
| Public-candidate generalized occurrences | `data/processed/fauna/public/occurrences_generalized/` | Only transformed, reviewed, policy-approved candidates move there. |
| Other processed fauna object/family lanes | `data/processed/fauna/<object-or-family>/` | Use when restricted-occurrence posture is not the primary organizing concern. |
| Fauna catalog records | `data/catalog/domain/fauna/` | Downstream; restricted catalog exposure only if policy allows and route is role-gated. |
| Fauna STAC/DCAT/PROV records | `data/catalog/{stac,dcat,prov}/fauna/` | Downstream catalog projections if accepted and policy-admitted. |
| Fauna triplet/graph records | `data/triplets/.../fauna/` | Downstream graph stage; must not expose restricted geometry or joins. |
| Published public-safe fauna products | `data/published/.../fauna/` | Only release-approved safe derivatives, not restricted originals. |
| EvidenceBundle/proof records | `data/proofs/` | Separate proof family. |
| Source, run, transform, redaction, validation, policy, correction, access, and release receipts | `data/receipts/` | Separate receipt family. |
| Fauna source registry records | `data/registry/sources/fauna/` | Separate source authority. |
| Release candidates and release manifests | `release/candidates/fauna/`, `release/` | Separate publication authority. |
| Fauna contracts | `contracts/domains/fauna/` | Object meaning; not data. |
| Fauna schemas | `schemas/contracts/v1/domains/fauna/` | Machine shape; not data. |
| Fauna policy and sensitivity rules | `policy/domains/fauna/`, `policy/sensitivity/fauna/` | Admissibility authority; not data. |
| Validators, tests, fixtures, pipelines, apps, packages | `tools/validators/`, `tests/`, `fixtures/`, `pipelines/`, `apps/`, `packages/` | Separate roots. |

## Accepted contents

Restricted occurrence artifacts may include:

- processed occurrence records requiring T2 reviewer-only or steward-limited access;
- processed occurrence records requiring T3 named-agreement, rights-holder, agency, tribal, landowner, research, or partner access restrictions;
- T4 denied occurrence records admitted only for internal steward review, correction, or redaction planning when policy allows their processed handling;
- sensitive-taxon occurrence records whose exact geometry or identifying attributes remain restricted;
- occurrence records with exact location, time, method, observer, media, source, or habitat joins that create re-identification risk;
- re-identifying occurrence joins preserved for review, correction, audit, or transformation planning but not for public use;
- restricted sidecars for sensitivity tier/rank, source role, rights, agreement reference, review state, access basis, policy decision, evidence references, validation status, correction path, and rollback target;
- README and manifest notes that explain local boundaries without becoming release manifests, proof bundles, source registry records, schemas, policy rules, validators, or public routes.

## Exclusions

Do not store these under `data/processed/fauna/restricted/occurrences/`:

- RAW occurrence records, source downloads, source-native geometries, steward originals, logs, screenshots, media payloads, or source exports.
- WORK/scratch redaction trials, unresolved geoprivacy experiments, intermediate joins, or transform-debug outputs.
- Quarantined material whose rights, sensitivity, source role, safety, or review state is too unresolved to admit even as restricted processed data.
- Public-candidate generalized or aggregated occurrence products after release-oriented transform review; those belong under `data/processed/fauna/public/occurrences_generalized/` until published.
- Published public-safe occurrence products; those belong under `data/published/.../fauna/` after release.
- RedactionReceipt, AggregationReceipt, ReviewRecord, PolicyDecision, ValidationReport, ReleaseManifest, EvidenceBundle, proof records, catalog records, STAC/DCAT/PROV records, triplets/graph records, source registry records, schemas, policy rules, validators, tests, fixtures, pipelines, app/UI/API code, or packages.
- Public API/UI/tile payloads, direct downloads, Focus Mode answers, public map layers, enforcement aids, landowner/parcel targeting aids, hunting/fishing/legal advice, operational wildlife guidance, emergency alerts, or life-safety guidance.
- Redaction parameters, fuzzing radii, seeds, exact transform offsets, access credentials, secrets, private agreement terms, or implementation details that could aid exposure or unauthorized access.

## Restricted-occurrence requirements

PROPOSED until concrete validators and access-control enforcement are verified:

| Requirement | Meaning |
|---|---|
| Source trace | Each restricted occurrence artifact should trace to SourceDescriptor or fauna source registry context. |
| Evidence linkage | Claims about species, occurrence, site, observation method, record status, access basis, transform, review, or correction should resolve downstream to EvidenceBundle/proof context where appropriate. |
| Occurrence identity | Taxon, observation, location, time, source, observer/media/method where allowed, and occurrence status should remain auditable without increasing exposure. |
| Sensitivity posture | Each artifact should carry sensitivity tier/rank, denied/reviewer/restricted posture, exact-geometry posture, and unresolved-sensitivity behavior. |
| Access basis | T2 reviewer, T3 named-agreement, T4 denied/internal-review, or equivalent access posture should be explicit. |
| Rights posture | Steward, agency, license, landowner, sovereignty, research, consent, observer, media, and reuse rights should be resolved or held closed. |
| Review state | Sensitivity reviewer, fauna steward, rights-holder representative, and access-control review should be recorded where required. |
| Policy decision | Restricted processed status requires PolicyDecision/admissibility posture before non-quarantine handling where policy requires it. |
| Re-identification check | Joins with habitat, parcel, infrastructure, people, time, media, method, rare taxa, or small cells must be checked before any transition. |
| Audit trail | Access, correction, review, transform, demotion, withdrawal, and release-transition actions should be receipt-linked. |
| Public transition | Any public representation requires separate redaction/generalization/aggregation, ReviewRecord, PolicyDecision, ReleaseManifest, correction path, and rollback target. |

## Occurrence guardrails

- Restricted occurrence does not mean public-candidate occurrence.
- Exact sensitive occurrence geometry must stay inside governed restricted/quarantine handling and must not be copied to public-candidate or published lanes.
- T2 reviewer-only occurrence material must stay role-gated and correction-path active.
- T3 named-agreement occurrence material must stay limited to named authorized parties under recorded agreement.
- T4 denied occurrence material must not be released to any audience unless a governed transition permits a safer representation.
- Sensitive taxa, steward-controlled occurrence records, exact sensitive occurrence geometry, observer/source/media identifiers, and re-identifying joins fail closed by default.
- Existence may be releasable without exact geometry only when steward review permits.
- Missing rights, unresolved sensitivity, absent review, missing agreement, or missing policy decision blocks public promotion.
- Source quality never overrides sensitivity, rights, or review state.
- Do not publish transform parameters, radii, seeds, offsets, secrets, credentials, private agreement terms, or source details that could assist re-identification.
- Habitat, hydrology, infrastructure, parcel, people, source, media, method, and time joins can make occurrence records more sensitive.
- Public clients and Focus Mode must not read this lane directly.

> [!CAUTION]
> Do not expose `data/processed/fauna/restricted/occurrences/` directly as a public map, tile service, API, UI, download, Focus Mode answer, AI answer source, species-location service, landowner/parcel targeting aid, enforcement surface, or operational wildlife guidance. Restricted occurrence data remains inside the trust membrane.

## Directory map

Actual child inventory remains **NEEDS VERIFICATION**. Use this as a proposed local organization pattern only after confirming current repo convention and validators.

```text
data/processed/fauna/restricted/occurrences/
├── README.md
├── records/                  # PROPOSED — restricted processed occurrence records
├── exact_geometry/           # PROPOSED — exact/sensitive geometry derivatives if policy allows processed handling
├── reviewer_only/            # PROPOSED — T2 reviewer/steward-limited occurrence artifacts
├── named_agreement/          # PROPOSED — T3 named-party/rights-agreement occurrence artifacts
├── denied_internal_review/   # PROPOSED — T4 occurrence material for internal review/correction where policy allows
├── steward_controlled/       # PROPOSED — agency/tribal/landowner/research restricted occurrences
├── reidentifying_joins/      # PROPOSED — restricted occurrence joins pending sensitivity review
├── access_links/             # PROPOSED — links to access decisions/agreements, not credential storage
├── reviews/                  # PROPOSED — review-link sidecars, not review authority
├── corrections/              # PROPOSED — correction-link sidecars, not receipt authority
├── _manifests/               # PROPOSED — lane-local non-release manifests only
└── _README_TODO.md           # PROPOSED — remove after actual child inventory is documented
```

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous file | CONFIRMED | Target existed as a one-character placeholder. | Did not define restricted occurrence boundaries. |
| `data/processed/fauna/restricted/README.md` | CONFIRMED parent README | Restricted parent lane is non-public, access-controlled, and requires governed transition for any public-safe derivative. | Does not prove child inventory or access-control enforcement. |
| `docs/domains/fauna/SENSITIVITY.md` | CONFIRMED doctrine / PROPOSED implementation | Sensitive species default to DENY/ABSTAIN; T2 is reviewer-only, T3 named-agreement, T4 denied; transitions require ReviewRecord, PolicyDecision, agreements, and reversibility. | Binding decisions live in `policy/sensitivity/fauna/`; concrete parameters are deliberately not in docs. |
| `docs/domains/fauna/README.md` | CONFIRMED doctrine / PROPOSED implementation | Fauna owns taxonomy, occurrences, ranges, monitoring, sensitive sites, invasive species, geoprivacy, public-safe derivatives, and governed API surfaces. | Implementation maturity remains NEEDS VERIFICATION. |
| `data/processed/fauna/public/occurrences_generalized/README.md` | CONFIRMED sibling README | Generalized occurrence public-candidates are separate from restricted source occurrences and still not published by default. | Does not authorize public release. |
| `policy/sensitivity/fauna/` | NEEDS VERIFICATION | Binding admissibility home named by Fauna docs. | Current policy files and enforcement were not verified in this task. |
| `contracts/domains/fauna/` and `schemas/contracts/v1/domains/fauna/` | NEEDS VERIFICATION | Expected occurrence contract/schema homes. | Specific occurrence object files and validators were not verified in this task. |

## Validation checklist

- [ ] Confirm actual child directories under `data/processed/fauna/restricted/occurrences/`.
- [ ] Confirm whether `occurrences/` is the accepted restricted occurrence lane name or needs reconciliation with object-family naming.
- [ ] Confirm parent `data/processed/fauna/README.md` is expanded beyond stub.
- [ ] Confirm occurrence object contracts and schemas for restricted occurrence artifacts.
- [ ] Confirm sensitivity tier/rank representation and canonical vocabulary.
- [ ] Confirm validators, fixtures, CI checks, and access-control enforcement for restricted occurrence artifacts.
- [ ] Confirm SourceDescriptor/source registry linkage for every source-derived occurrence artifact.
- [ ] Confirm ReviewRecord, PolicyDecision, agreement reference, RedactionReceipt/AggregationReceipt where applicable, ValidationReport, CorrectionNotice, ReleaseManifest where transitioning, correction path, and rollback target.
- [ ] Confirm exact sensitive occurrence coordinates, source-native geometry, observer/source/media identifiers, nests, dens, roosts, hibernacula, spawning sites, steward-controlled records, re-identifying joins, private agreement terms, credentials, secrets, redaction parameters, transform secrets, and rights-unclear material cannot enter public routes.
- [ ] Confirm public-candidate transition from restricted occurrence material is governed, evidence-backed, sensitivity-safe, rights-safe, review-backed, release-linked, and reversible.
- [ ] Confirm public clients and Focus Mode cannot read this lane directly as public truth, public location service, public map, public tile, public API, public UI, or AI-answer source.

## Rollback

Rollback is required if this lane becomes a public output root, `data/published/` substitute, public-candidate shortcut, exact sensitive-location exposure path, transform-secret exposure path, agreement/credential exposure path, quarantine bypass, source-data root, proof store, receipt store, catalog root, triplet root, source-registry root, release-decision root, schema root, policy root, validator root, implementation root, public API shortcut, public UI shortcut, public tile shortcut, public exposure shortcut, enforcement aid, landowner/parcel targeting aid, operational wildlife guidance source, or life-safety guidance source.

Rollback target for this expansion: previous placeholder blob SHA `e25f1814e51579d5f55c0f1fe0135ddb28a47f4a`.

<p align="right"><a href="#top">Back to top</a></p>
