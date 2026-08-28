<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/examples/settlements-infrastructure/readme
title: Settlements / Infrastructure Examples README
type: standard
version: v0.2.0
status: draft
owners: NEEDS VERIFICATION - examples, settlements/infrastructure, settlement identity, infrastructure sensitivity, evidence, policy, release, and docs stewardship; default GitHub review route is @bartytime4life
created: NEEDS VERIFICATION - one-character placeholder existed before 2026-06-30 expansion
updated: 2026-07-24
prepared_under_prompt: KFM Markdown Modernization & GitHub Documentation Implementation Agent v4.0.0
review_packet_id: kfm-md-examples-settlements-infrastructure-20260724
truth_posture: >
  CONFIRMED current target path, examples-root contract, runtime finite-outcome enum,
  default CODEOWNERS route, and bounded related README/workflow evidence /
  PROPOSED example authoring and graduation contract / UNKNOWN exhaustive child inventory,
  executable examples, consumers, runtime parity, and public effects /
  NEEDS VERIFICATION accountable stewards, accepted example schema, examples validator,
  link checker, accessibility execution, fixture/test graduation, and host rendering
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: f6b45f14dce46a74f72a0a5ba69d9375dd6a3412
  prior_blob: d9e27f6c2c806587c374e809d608891f8cb418d7
  method: complete target read, current parent/domain/contract/test/fixture/workflow reads, bounded exact-path search, and open-PR overlap check
policy_label: public-review
related: [../README.md, ../evidence_bundles/README.md, ../focus_flows/README.md, ../../docs/domains/settlements-infrastructure/README.md, ../../docs/domains/settlements-infrastructure/CANONICAL_PATHS.md, ../../docs/domains/settlements-infrastructure/DATA_LIFECYCLE.md, ../../data/raw/settlements-infrastructure/README.md, ../../data/work/settlements-infrastructure/README.md, ../../data/processed/settlements-infrastructure/README.md, ../../data/catalog/domain/settlements-infrastructure/README.md, ../../data/proofs/settlement/README.md, ../../data/receipts/settlement/README.md, ../../data/published/layers/settlements-infrastructure/README.md, ../../docs/doctrine/directory-rules.md]
tags: [kfm, examples, settlements-infrastructure, settlement, infrastructure, municipality, census-place, townsite, ghost-town, fort, mission, reservation-community, facility, service-area, operator, condition-observation, dependency, source-role, public-safe, geoprivacy, critical-infrastructure, finite-outcomes, non-authoritative, cite-or-abstain]
notes:
  - "v0.1.0 replaced a one-character placeholder at `examples/settlements-infrastructure/README.md`; v0.2.0 preserves that lineage and modernizes the full baseline."
  - "Settlements/Infrastructure examples are illustrative and review aids only; operational data belongs under `data/<phase>/settlements-infrastructure/` or an ADR-resolved compatibility lane."
  - "The `settlements-infrastructure` versus `settlement` segment conflict is preserved; examples do not resolve ADR-class path variance."
  - "Examples must not become settlement truth, municipal-status certification, infrastructure condition truth, operator/dependency disclosure, proof authority, receipt authority, catalog closure, policy authority, release authority, public artifact authority, or direct AI output authority by placement."
  - "Public runtime outcomes are ANSWER, ABSTAIN, DENY, or ERROR; HOLD and QUARANTINE remain separate review or lifecycle states."
  - "README presence does not prove example files, schemas, validators, fixtures, CI checks, source descriptors, proof objects, receipts, governed API route behavior, public layer payloads, or release readiness."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Settlements / Infrastructure Examples

Illustrative examples for teaching how KFM reviewers should handle settlement identity, municipality/census-place context, historic place context, public-safe infrastructure context, source-role separation, sensitive joins, EvidenceBundle support, and finite public outcomes without creating operational authority.

[![Document status: draft](https://img.shields.io/badge/document-draft-d4a72c?style=flat-square)](#status-notes)
[![Maturity: README only](https://img.shields.io/badge/maturity-README--only-0969da?style=flat-square)](#current-maturity)
[![Authority: non-authoritative](https://img.shields.io/badge/authority-non--authoritative-b42318?style=flat-square)](#path-posture)
[![Truth posture: cite or abstain](https://img.shields.io/badge/truth-cite--or--abstain-1f883d?style=flat-square)](../../docs/doctrine/truth-posture.md)
[![Sensitivity: fail closed](https://img.shields.io/badge/sensitivity-fail--closed-b42318?style=flat-square)](#guardrails)

**Status:** draft / `README_ONLY` / example-lane guidance  
**Stewardship:** `NEEDS VERIFICATION` - examples, settlements/infrastructure, identity, sensitivity, evidence, policy, release, and docs responsibilities  
**GitHub review route:** default [CODEOWNERS](../../.github/CODEOWNERS) route `@bartytime4life`; routing is not stewardship, approval, release authority, or proof of review  
**Path:** `examples/settlements-infrastructure/README.md`  
**Navigate:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Authoring workflow](#authoring-workflow) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Example contract](#example-contract)  
[Current maturity](#current-maturity) · [Guardrails](#guardrails) · [Lifecycle](#lifecycle-relationship) · [Suggested layout](#suggested-layout) · [Validation](#validation-checklist) · [Review](#review-and-maintenance) · [Status](#status-notes) · [History](#change-history) · [Evidence](#evidence-ledger)

> [!IMPORTANT]
> Files under `examples/settlements-infrastructure/` are examples. They are not source captures, working candidates, processed objects, catalog records, triplets, EvidenceBundles, ProofPacks, receipts, policy decisions, release decisions, published layers, governed API responses, Focus Mode answers, Evidence Drawer payloads, fixtures, validators, or tests.

> [!CAUTION]
> Examples must not expose exact critical-infrastructure detail, operator-sensitive detail, dependency graphs, condition/vulnerability detail, private land or person-parcel joins, archaeology/burial/sacred-site clues, cultural/sovereignty-sensitive detail, restricted facility geometry, credentials, secrets, or reconstructive redaction clues. Use synthetic, generalized, redacted, aggregated, delayed, restricted, or denied examples by default.

---

## Scope

`examples/settlements-infrastructure/` is a documentation and review aid for the Settlements/Infrastructure domain.

Use this lane to demonstrate:

- how settlement/place examples should keep legal, census, historic, military, religious, reservation-community, and administrative identities distinct;
- how source roles should stay explicit for source families such as Census/TIGER, GNIS, municipal records, historical maps, local GIS, operator inventories, bridge/facility records, and cross-lane hazard/hydrology/roads/people-land context;
- how example object families may reference `Settlement`, `Municipality`, `CensusPlace`, `Townsite`, `GhostTown`, `Fort`, `Mission`, `ReservationCommunity`, `InfrastructureAsset`, `NetworkNode`, `NetworkSegment`, `Facility`, `ServiceArea`, `Operator`, `ConditionObservation`, and `Dependency` without becoming operational records;
- how public-safe examples should generalize, suppress, aggregate, redact, or deny sensitive infrastructure, cultural, archaeology, person/land, or exact-location detail;
- how `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` public outcomes may be illustrated with synthetic payloads;
- how examples should avoid direct public reads from RAW, WORK, QUARANTINE, PROCESSED, unpublished CATALOG/TRIPLET, proof stores, receipt stores, source registries, model runtimes, graph/vector stores, or canonical/internal stores.

This folder should make reviewers faster. It should not become a shortcut around lifecycle data lanes, source descriptors, schemas, contracts, validators, proof lanes, policy review, release gates, or governed API behavior.

---

## Path posture

Repository lineage records that v0.1.0 replaced a one-character placeholder at this path. The baseline for this revision is the complete v0.1.0 README, not that historical placeholder.

| Baseline fact | Verified result |
|---|---|
| Repository | `bartytime4life/Kansas-Frontier-Matrix` |
| Pinned base | `main@f6b45f14dce46a74f72a0a5ba69d9375dd6a3412` |
| Prior target blob | `d9e27f6c2c806587c374e809d608891f8cb418d7` |
| Canonical relationship | Nested domain lane inside the canonical `examples/` responsibility root |
| Document authority | Non-authoritative example guidance |
| Overlapping open PR | None found for this exact path in the bounded open-PR check |

Current placement evidence:

- `examples/README.md` describes `examples/` as walkthroughs and example assemblies.
- `examples/habitat/README.md` provides the current example-lane pattern: examples are illustrative and non-authoritative by placement.
- `docs/domains/settlements-infrastructure/README.md` defines the domain scope and object families.
- `docs/domains/settlements-infrastructure/CANONICAL_PATHS.md` identifies `settlements-infrastructure` as the working domain slug while preserving an ADR-class conflict with `settlement`.
- `docs/domains/settlements-infrastructure/DATA_LIFECYCLE.md` applies the KFM lifecycle invariant and marks the segment conflict as unresolved.
- `data/raw/settlements-infrastructure/`, `data/work/settlements-infrastructure/`, `data/processed/settlements-infrastructure/`, `data/catalog/domain/settlements-infrastructure/`, `data/published/layers/settlements-infrastructure/`, `data/proofs/settlement/`, and `data/receipts/settlement/` each define operational homes that this examples lane must not replace.

Therefore this README treats `examples/settlements-infrastructure/` as **CONFIRMED path presence / DRAFT example-lane guidance / NON-AUTHORITATIVE by placement**.

### Segment conflict

The long segment is used here because the requested path and current domain/lifecycle evidence use:

```text
settlements-infrastructure
```

The singular segment also appears in compatibility or sublane contexts such as `data/proofs/settlement/` and `data/receipts/settlement/`.

This README does **not** resolve that conflict. Until an ADR or migration note settles the topology, examples must avoid creating parallel authority or implying that one example path can decide schema, contract, policy, proof, receipt, release, or public route placement.

---

## Repo fit

| Responsibility | Correct home | Boundary |
|---|---|---|
| Settlements/Infrastructure example snippets, synthetic payloads, and walkthroughs | `examples/settlements-infrastructure/` | This lane. Illustrative only. |
| Example EvidenceBundle snippets used beside settlement/infrastructure examples | [`../evidence_bundles/`](../evidence_bundles/README.md) | Example lane only; not proof authority. |
| Focus Mode or governed-answer examples involving settlement/infrastructure context | [`../focus_flows/`](../focus_flows/README.md) | Example lane only; not runtime or API behavior. |
| Domain doctrine | [`../../docs/domains/settlements-infrastructure/`](../../docs/domains/settlements-infrastructure/README.md) | Human-facing doctrine. |
| Canonical-path / slug-conflict guidance | [`../../docs/domains/settlements-infrastructure/CANONICAL_PATHS.md`](../../docs/domains/settlements-infrastructure/CANONICAL_PATHS.md) | Path registry guidance; not examples. |
| Lifecycle doctrine | [`../../docs/domains/settlements-infrastructure/DATA_LIFECYCLE.md`](../../docs/domains/settlements-infrastructure/DATA_LIFECYCLE.md) | Lifecycle gates and failure-closed posture. |
| RAW source captures | [`../../data/raw/settlements-infrastructure/`](../../data/raw/settlements-infrastructure/README.md) | Immutable source-capture lane; no public path. |
| WORK candidates and intermediates | [`../../data/work/settlements-infrastructure/`](../../data/work/settlements-infrastructure/README.md) | Working normalization lane; no public path. |
| PROCESSED artifacts | [`../../data/processed/settlements-infrastructure/`](../../data/processed/settlements-infrastructure/README.md) | Validated upstream data; not public by default. |
| CATALOG-stage records | [`../../data/catalog/domain/settlements-infrastructure/`](../../data/catalog/domain/settlements-infrastructure/README.md) | Catalog carriers; release-gated. |
| Settlement-sublane proof support | [`../../data/proofs/settlement/`](../../data/proofs/settlement/README.md) | Proof support; examples do not prove claims. |
| Settlement-sublane receipt support | [`../../data/receipts/settlement/`](../../data/receipts/settlement/README.md) | Process memory; examples do not record runs. |
| Published public-safe layers | [`../../data/published/layers/settlements-infrastructure/`](../../data/published/layers/settlements-infrastructure/README.md) | Released delivery artifacts only. |
| Release decisions | `release/` | ReleaseManifest, PromotionDecision, correction, withdrawal, rollback, signatures. |
| Schemas, contracts, policy, validators, tests, fixtures, apps, packages, pipelines | `schemas/`, `contracts/`, `policy/`, `tools/validators/`, `tests/`, `fixtures/`, `apps/`, `packages/`, `pipelines/` | Separate responsibility roots. Examples must not define or enforce them. |

---

## Authoring workflow

Use this lane as a reviewable teaching surface:

1. **Choose one bounded scenario.** Prefer a synthetic settlement, place, service-area, facility-summary, denial, abstention, or cross-lane reference case.
2. **Declare maturity and authority.** Start at `README_ONLY` or `STATIC_WALKTHROUGH`; do not claim validation, local execution, fixture parity, or runtime parity without observed evidence.
3. **Separate vocabularies.** Public runtime examples use the contract enum `ANSWER | ABSTAIN | DENY | ERROR`. Use `HOLD` or `QUARANTINE` only as clearly labeled review or lifecycle states.
4. **Expose support and limits.** Identify source role, temporal scope, EvidenceRef/EvidenceBundle posture, sensitivity, review, release, correction, and rollback expectations where material.
5. **Keep examples public-safe.** Use synthetic identifiers and generalized or omitted geometry; exclude operational, restricted, reconstructive, person-land, cultural, archaeology, and critical-infrastructure detail.
6. **Validate to the claimed maturity.** Check this README and any example internally; graduate reusable enforcement material into the governed fixture/test strategy rather than treating example placement as proof.

A reviewer should be able to tell what the example teaches, what it cannot prove, which authority owns each referenced rule, and why the expected negative state is safe.

---

## Accepted material

Accepted files should be small, synthetic, reviewable, and visibly marked as examples.

| Accepted item | Use | Required markings |
|---|---|---|
| Settlement identity example | Teach how legal, census, historic, and name-variant identity should stay separated. | `example: true`, synthetic IDs, source-role labels, no legal-status claim. |
| Municipality / CensusPlace comparison | Show how municipal status and census geography differ. | Synthetic or generalized boundaries; cite-or-abstain posture. |
| Historic townsite, ghost town, fort, or mission walkthrough | Show temporal status, uncertainty, rights, and cultural/archaeology review posture. | Generalized geometry; no sensitive site clues. |
| ReservationCommunity context example | Teach sovereignty/cultural review boundaries. | No sensitive detail; review and policy placeholders visible. |
| Public-safe facility or service-area summary | Show aggregation/generalization and field allowlist behavior. | No operator-sensitive or dependency detail. |
| Critical-infrastructure negative example | Show a public `DENY` or `ABSTAIN` outcome, or a separately labeled pre-runtime `HOLD`/restricted review posture. | No exact facility geometry, vulnerability, dependency graph, or operational detail. |
| Cross-lane relation example | Show Roads/Rail, Hydrology, Hazards, People/Land, or Archaeology references without absorbing ownership. | Owning-lane truth and EvidenceRef support remain explicit. |
| Evidence Drawer / Focus example note | Show how governed UI might explain support and limitations. | Must state public UI consumes governed projections, not this folder. |

Examples may use Markdown, JSON, YAML, or tiny tabular snippets. Keep examples deterministic and easy to diff.

---

## Exclusions

| Do not place here | Correct home or action |
|---|---|
| Real source payloads, agency exports, municipal records, operator files, GIS layers, scans, OCR inputs, or source-system mirrors | `data/raw/settlements-infrastructure/` or restricted storage as applicable |
| WORK transforms, identity matching outputs, geometry repair, dependency analysis, QA outputs, notebooks, or review drafts | `data/work/settlements-infrastructure/` |
| Quarantined rights/source-role/sensitivity/release-unclear material | `data/quarantine/settlements-infrastructure/` |
| Validated processed settlement or infrastructure artifacts | `data/processed/settlements-infrastructure/` or ADR-resolved lane |
| Catalog records, triplets, graph exports, or release candidates | `data/catalog/`, `data/triplets/`, or `release/candidates/` as appropriate |
| EvidenceBundles, ProofPacks, citation-validation records, validation reports, or proof indexes | `data/proofs/` |
| Run, transform, validation, redaction, aggregation, policy, AI, telemetry, release, correction, or rollback receipts | `data/receipts/` |
| Published PMTiles, GeoParquet, GeoJSON, COGs, reports, stories, API payloads, screenshots, or public downloads | `data/published/` after release gates |
| ReleaseManifest, PromotionDecision, RollbackCard, CorrectionNotice, WithdrawalNotice, signatures, or changelog entries | `release/` |
| Contracts, schemas, policy bundles, validators, tests, fixtures, apps, packages, pipelines, connectors, or workflows | Their canonical responsibility roots |
| Exact critical infrastructure, operator-sensitive, condition/vulnerability, dependency, cultural/sovereignty, archaeology, sacred-site, private parcel, living-person, credential, or secret detail | Quarantine, restrict, redact, generalize, synthesize, or deny |
| Generated summaries presented as evidence | Governed AI surfaces may cite evidence; generated text is not evidence |

---

## Example contract

Every example in this lane should answer nine questions without claiming operational maturity:

| Question | Expected answer |
|---|---|
| What scenario is illustrated? | A bounded synthetic settlement, place, facility, service-area, condition, dependency, or cross-lane relation scenario. |
| Which object family is involved? | One of the owned object families, or an explicitly synthetic teaching object. |
| What source role applies? | Observed, regulatory, modeled, aggregate, administrative, candidate, authority, context, or synthetic, without role collapse. |
| What evidence support is implied? | Synthetic or clearly marked sample EvidenceRef/EvidenceBundle-like refs, with cite-or-abstain posture. |
| What sensitivity posture applies? | Public-safe, restricted, hold, deny, generalized, redacted, or needs-review. |
| What release posture applies? | Example release reference or `not_released`; examples do not publish. |
| What public outcome should render? | Exactly one of `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR` when public behavior is illustrated, per the [DecisionEnvelope contract](../../contracts/runtime/decision_envelope.md). |
| What pre-runtime state applies? | If review or lifecycle handling uses `HOLD` or `QUARANTINE`, label it separately; never place it in the public outcome field. |
| What must not happen? | No legal-status certification, ownership proof, infrastructure disclosure, emergency guidance, proof, receipt, catalog closure, release, or policy decision by example placement. |

Illustrative JSON should include a visible marker like this:

```json
{
  "example": true,
  "authority": "non_authoritative_example",
  "do_not_publish": true,
  "domain": "settlements-infrastructure",
  "example_id": "kfm://example/settlements-infrastructure/NEEDS-VERIFICATION",
  "object_family": "Settlement",
  "source_role": "synthetic",
  "expected_outcome": "ABSTAIN",
  "reason": "illustrative example only; evidence, policy, release, schema, route, and validator behavior NEEDS VERIFICATION"
}
```

> [!WARNING]
> Do not copy example IDs, example coordinates, example source roles, example evidence refs, example policy decisions, example release refs, example geometry, or example generated text into operational data. Examples teach shape and failure behavior; they do not certify facts.

---

## Current maturity

At the pinned base, this README is the only lane content directly inspected. A bounded exact-path GitHub search surfaced this README and a generated receipt reference, but did not establish child example payloads or an executable entrypoint. The lane is therefore `README_ONLY`, not runnable or structure-validated.

The parent [`examples/` contract](../README.md) defines the maturity vocabulary used here:

| Maturity state | Current result | Evidence boundary |
|---|---:|---|
| `README_ONLY` | `CONFIRMED` | This complete README exists at the pinned target blob. |
| `STATIC_WALKTHROUGH` | `UNKNOWN` | No child walkthrough was directly read; bounded search is not an exhaustive tree proof. |
| `STRUCTURE_VALIDATED` | `NEEDS VERIFICATION` | No accepted examples schema, validator result, or examples-specific check was verified. |
| `RUNNABLE_LOCAL` | `UNKNOWN` | No accepted entrypoint, dependency closure, deterministic run, or smoke result was verified. |
| `FIXTURE_MIRRORED` | `NEEDS VERIFICATION` | Test and fixture README lanes exist, but example-to-fixture parity and drift checks were not verified. |

A badge, README, generated receipt, test-lane README, or fixture stub does not raise this maturity.

---

## Guardrails

| Risk | Guardrail |
|---|---|
| Example becomes settlement truth | Examples can illustrate identity patterns but cannot certify settlement, municipal, census-place, townsite, ghost-town, fort, mission, or reservation-community status. |
| CensusPlace becomes Municipality | Census geography and legal municipal status remain separate unless evidence supports the relation. |
| Historic context exposes sensitive places | Fort, mission, townsite, ghost-town, cultural, sovereignty, archaeology, sacred-site, and burial-adjacent examples use generalized or denied detail. |
| Infrastructure context becomes operational disclosure | Facility, service-area, operator, condition, dependency, vulnerability, and network examples fail closed unless explicitly public-safe and released. |
| Cross-lane truth collapses | Roads/Rail owns routes; Hydrology owns water evidence; Hazards owns events/warnings; People/Land owns parcels/living-person joins; Archaeology owns sensitive site truth. |
| Example becomes proof | This directory is outside the lifecycle/proof/release spine and cannot prove, publish, or release claims. |
| AI becomes authority | AI-generated settlement or infrastructure summaries are downstream carriers; EvidenceBundle, policy, review, and release state outrank generated language. |
| Slug conflict gets hidden | `settlements-infrastructure` and `settlement` variance remains visible until ADR or migration resolves it. |

---

## Lifecycle relationship

```mermaid
flowchart LR
    EX["examples/settlements-infrastructure<br/>illustrative only"]
    DOC["docs/domains/settlements-infrastructure<br/>domain doctrine"]
    EBEX["examples/evidence_bundles<br/>illustrative proof shapes"]
    FOCUS["examples/focus_flows<br/>illustrative finite outcomes"]

    RAW["data/raw/settlements-infrastructure"]
    WQ["WORK / QUARANTINE<br/>candidate or held material"]
    PROC["data/processed/settlements-infrastructure"]
    CT["CATALOG / TRIPLET<br/>governed lifecycle stage"]
    REL["release/<br/>review and decision"]
    PUB["data/published/layers/settlements-infrastructure"]
    PROOF["data/proofs/settlement<br/>sublane proof support"]
    RECEIPT["data/receipts/settlement<br/>process memory"]

    EX -. "teaches" .-> DOC
    EX -. "pairs with" .-> EBEX
    EX -. "pairs with" .-> FOCUS

    RAW --> WQ --> PROC --> CT --> REL --> PUB
    PROOF -. "supports review" .-> REL
    RECEIPT -. "records process" .-> REL

    EX -. "must not replace" .-> RAW
    EX -. "must not prove" .-> PROOF
    EX -. "must not record run" .-> RECEIPT
    EX -. "must not decide" .-> REL
    EX -. "must not publish" .-> PUB

    classDef example fill:#f3e5f5,stroke:#6f42c1,color:#202124;
    classDef doc fill:#e7f1ff,stroke:#2b6cb0,color:#202124;
    classDef data fill:#fff3cd,stroke:#8a6d3b,color:#202124;
    classDef gate fill:#d1e7dd,stroke:#0f5132,color:#202124;
    class EX,EBEX,FOCUS example;
    class DOC doc;
    class RAW,WQ,PROC,CT,PUB,PROOF,RECEIPT data;
    class REL gate;
```

The diagram is a doctrinal relationship, not proof of implemented edges or released artifacts. The examples lane is outside the lifecycle spine. It can illustrate lifecycle behavior, but it cannot become RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, PUBLISHED, proof, receipt, registry, or release authority. Release review and decision gate publication; publication does not create its own release authority.

---

## Suggested layout

This tree is **PROPOSED**. Confirm actual examples, schema paths, fixture strategy, validator expectations, and slug-governance decisions before adding files.

```text
examples/settlements-infrastructure/
├── README.md
├── settlement-identity/
│   ├── census-place-not-municipality.example.json
│   ├── legal-status-timeline.example.json
│   └── name-variant-abstain.example.json
├── historic-places/
│   ├── ghost-town-context.example.json
│   ├── fort-generalized-context.example.json
│   └── mission-sensitive-context-deny.example.json
├── infrastructure/
│   ├── public-safe-facility-summary.example.json
│   ├── service-area-generalized.example.json
│   └── dependency-detail-deny.example.json
├── cross-lane/
│   ├── hydrology-reference-not-water-truth.walkthrough.md
│   ├── roads-reference-not-route-truth.walkthrough.md
│   └── people-land-join-deny.example.json
└── walkthroughs/
    └── settlement-context-to-evidence-drawer.walkthrough.md
```

Recommended file naming:

| Pattern | Use |
|---|---|
| `*.example.json` | Non-authoritative JSON example. |
| `*.example.yaml` | Non-authoritative YAML example. |
| `*.walkthrough.md` | Narrative walkthrough, not operational proof. |
| `README.md` | Local explanation and boundaries. |

---

## Validation checklist

Validation must match the maturity claimed. At the pinned base, repository-native documentation workflows expose readiness holds rather than completed render, link, or accessibility checks.

| Validation surface | Verified state | What it does not prove |
|---|---|---|
| [`docs-build`](../../.github/workflows/docs-build.yml) | `WORKFLOW_HOLD` | No accepted docs generator, preview artifact, or publication handoff. |
| [`link-check`](../../.github/workflows/link-check.yml) | `WORKFLOW_HOLD` | No repository links, anchors, images, or external URLs are checked by that workflow. |
| [`accessibility`](../../.github/workflows/accessibility.yml) | `WORKFLOW_HOLD` | No axe or keyboard-navigation execution occurs. |
| [Domain test parent](../../tests/domains/settlements-infrastructure/README.md) | `CONFIRMED README` | Executable domain tests, validators, CI coverage, and pass rates remain `NEEDS VERIFICATION`. |
| [Domain fixture lane](../../fixtures/domains/settlements-infrastructure/README.md) | `CONFIRMED greenfield stub` | Accepted example-to-fixture structure, payloads, validation, and parity are not established. |
| Examples-specific validator | `NEEDS VERIFICATION` | No accepted validator, deterministic fixture suite, or repository-native command was verified. |

Before adding or changing examples here, verify:

- [ ] The file is marked as an example and non-authoritative.
- [ ] The file contains no exact critical infrastructure detail, operator-sensitive detail, dependency graph, condition/vulnerability detail, archaeology/burial/sacred-site clue, private parcel join, living-person data, credential, secret, or reconstruction clue.
- [ ] The example does not create schema, contract, policy, proof, receipt, release, source-registry, route, model-runtime, fixture, validator, or test authority.
- [ ] Any IDs are synthetic or clearly marked `NEEDS VERIFICATION`.
- [ ] Source role, temporal scope, evidence support, sensitivity posture, review state, release state, correction path, and rollback posture are visible where material.
- [ ] Any public runtime illustration with missing, stale, conflicting, citation-failed, role-unclear, rights-unclear, sensitivity-unclear, or release-missing support renders `ABSTAIN`, `DENY`, or `ERROR` as appropriate; any `HOLD` or `QUARANTINE` is labeled separately as a review or lifecycle state.
- [ ] Any infrastructure, facility, service-area, operator, condition, dependency, or network example is public-safe, generalized, aggregated, redacted, or denied.
- [ ] Any cross-domain example preserves owning-lane truth for Roads/Rail, Hydrology, Hazards, People/Land, Archaeology, Agriculture, and other referenced lanes.
- [ ] Relative links from this README still resolve.
- [ ] Operational fixtures, if needed, are placed under the accepted test/fixture strategy rather than silently becoming examples.

---

## Review and maintenance

The current [CODEOWNERS](../../.github/CODEOWNERS) file routes this path through the repository default owner, `@bartytime4life`. That is a GitHub review route only; it does not prove assigned stewardship, independent review, policy approval, release authorization, or publication.

| Change type | Review burden |
|---|---|
| README-only clarification | Docs, examples, and Settlements/Infrastructure domain review. |
| Identity or legal-status example | Domain identity review plus evidence/source-role review. |
| Facility, service-area, operator, condition, dependency, or exact-location example | Infrastructure sensitivity and policy review; fail closed when uncertain. |
| Cultural, sovereignty, archaeology, sacred-site, burial-adjacent, person-land, or parcel relation | Relevant domain and sensitivity review before inclusion; prefer generalized or denied examples. |
| Example proposed as fixture or test | Fixture/test and validator review in the owning roots; example placement alone is insufficient. |
| Public API, UI, map, story, AI, release, correction, withdrawal, or rollback behavior | Review by the owning implementation, policy, evidence, release, correction, and rollback surfaces. |

### Correction, graduation, and rollback

- Correct misleading examples in place and preserve a clear history when readers may have relied on them.
- Deprecate or remove stale examples when they no longer teach the governed behavior; update inbound links and any mirrored fixture/test lineage.
- Graduate reusable enforcement material through a reviewed fixture/test change with synthetic no-network inputs, deterministic expected outcomes, negative cases, and drift checks.
- If an example exposes sensitive or operational detail, remove public access, preserve the minimum safe audit record, assess downstream copies, and follow governed correction or withdrawal procedures.
- A Git revert can restore documentation bytes; it does not by itself correct copied payloads, public artifacts, caches, or relied-on claims.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target path and baseline | CONFIRMED | The full v0.1.0 README was read at `main@f6b45f14dce46a74f72a0a5ba69d9375dd6a3412`; blob `d9e27f6c2c806587c374e809d608891f8cb418d7`. Earlier placeholder lineage is retained as history. |
| Examples root | CONFIRMED README | `examples/README.md` describes walkthroughs and example assemblies. |
| Example-lane pattern | CONFIRMED README | `examples/habitat/README.md` defines a non-authoritative domain example-lane pattern. |
| Domain doctrine | CONFIRMED README | `docs/domains/settlements-infrastructure/README.md` defines object families, source families, cross-lane boundaries, and sensitivity posture. |
| Canonical path registry | CONFIRMED README | `CANONICAL_PATHS.md` marks `settlements-infrastructure` as the working slug and preserves `settlement` as conflicted. |
| Data lifecycle doctrine | CONFIRMED README | `DATA_LIFECYCLE.md` applies the KFM lifecycle invariant and preserves the segment conflict. |
| RAW lane | CONFIRMED README | `data/raw/settlements-infrastructure/README.md` defines RAW as no-public-path source capture. |
| WORK lane | CONFIRMED README | `data/work/settlements-infrastructure/README.md` defines WORK as no-public-path candidate/intermediate material. |
| PROCESSED lane | CONFIRMED README | `data/processed/settlements-infrastructure/README.md` defines processed artifacts as upstream of catalog, triplet, publication, and release. |
| Catalog lane | CONFIRMED README | `data/catalog/domain/settlements-infrastructure/README.md` defines CATALOG-stage records as release-gated and not truth/public by placement. |
| Settlement proof/receipt sublanes | CONFIRMED README | `data/proofs/settlement/` and `data/receipts/settlement/` exist as singular settlement sublane support while naming remains unresolved. |
| Published layer lane | CONFIRMED README | `data/published/layers/settlements-infrastructure/README.md` defines released public-safe layer artifacts and preserves slug variance. |
| Directly inspected lane content | CONFIRMED | The complete README was read; no child example payload was directly read. |
| Exhaustive child payload inventory | UNKNOWN | Bounded search is not a recursive tree, LFS, generated, hosted, or consumer inventory. |
| Current lane maturity | CONFIRMED | `README_ONLY`; no higher maturity was established. |
| Runtime outcome vocabulary | CONFIRMED | The current DecisionEnvelope contract uses `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR`; `HOLD` and `QUARANTINE` are separate states. |
| GitHub review route | CONFIRMED | Default CODEOWNERS route is `@bartytime4life`; stewardship and independent review remain `NEEDS VERIFICATION`. |
| Documentation workflow checks | CONFIRMED | Docs build, link check, and accessibility are explicit readiness holds, not validation passes. |
| Schemas, validators, fixtures, CI checks, policy enforcement, governed route behavior, release linkage | NEEDS VERIFICATION | No runtime or validation enforcement was proven by this README. |
| Release/publication authority | CONFIRMED | None. Examples cannot publish, prove, release, or answer claims by placement. |

---

## Change history

### v0.2.0 - 2026-07-24

- preserved the same path, `doc_id`, created-date uncertainty, non-authority boundary, slug conflict, sensitivity posture, examples, caveats, links, and stable headings;
- linked every admitted badge to inspectable evidence and added a `README_ONLY` maturity badge;
- separated public runtime outcomes from pre-runtime `HOLD` and lifecycle `QUARANTINE` states;
- repaired the lifecycle diagram so release review and decision gate publication;
- added an authoring workflow, current-maturity matrix, repository validation holds, review burden, maintenance, correction, graduation, and rollback guidance;
- refreshed the evidence ledger against the pinned repository baseline without changing data, code, schema, policy, workflow, release, or publication state.

### v0.1.0 - 2026-06-30

- replaced the historical one-character placeholder with the governed Settlements/Infrastructure example-lane README.

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Current target baseline at `main@f6b45f14dce46a74f72a0a5ba69d9375dd6a3412` | CONFIRMED | Full v0.1.0 README and prior blob `d9e27f6c2c806587c374e809d608891f8cb418d7`; earlier placeholder lineage is preserved in metadata. | Does not prove child examples, execution, validation, review, release, or public effects. |
| [`../README.md`](../README.md) | CONFIRMED README | `examples/` is the canonical examples responsibility root and defines non-authority plus `README_ONLY`, `STATIC_WALKTHROUGH`, `STRUCTURE_VALIDATED`, `RUNNABLE_LOCAL`, and `FIXTURE_MIRRORED` maturity states. | Root guidance does not prove child payloads, execution, validation, or public effects. |
| [`../evidence_bundles/README.md`](../evidence_bundles/README.md) | CONFIRMED README | Establishes non-authoritative example-lane behavior and proof separation. | Covers EvidenceBundle examples, not Settlements/Infrastructure examples directly. |
| [`../habitat/README.md`](../habitat/README.md) | CONFIRMED README | Current domain example-lane pattern: non-authoritative examples, accepted material, exclusions, guardrails, and status notes. | Habitat-specific content does not define Settlements/Infrastructure behavior. |
| [`../../docs/domains/settlements-infrastructure/README.md`](../../docs/domains/settlements-infrastructure/README.md) | CONFIRMED doctrine / PROPOSED implementation | Domain scope, object families, source families, cross-lane boundaries, and sensitivity defaults. | Implementation maturity remains NEEDS VERIFICATION. |
| [`../../docs/domains/settlements-infrastructure/CANONICAL_PATHS.md`](../../docs/domains/settlements-infrastructure/CANONICAL_PATHS.md) | CONFIRMED doctrine / conflict register | Working slug `settlements-infrastructure` and unresolved `settlement` variance. | Does not prove final ADR resolution or runtime adoption. |
| [`../../docs/domains/settlements-infrastructure/DATA_LIFECYCLE.md`](../../docs/domains/settlements-infrastructure/DATA_LIFECYCLE.md) | CONFIRMED doctrine / PROPOSED implementation | Lifecycle invariant, object-family ownership, cross-lane boundaries, failure-closed gates, and segment conflict. | Does not prove implementation paths, validators, schemas, routes, or CI. |
| [`../../data/raw/settlements-infrastructure/README.md`](../../data/raw/settlements-infrastructure/README.md) | CONFIRMED README | RAW source-capture lane and no-public-path posture. | Does not prove payloads, SourceDescriptors, connectors, or release readiness. |
| [`../../data/work/settlements-infrastructure/README.md`](../../data/work/settlements-infrastructure/README.md) | CONFIRMED README | WORK candidate/intermediate lane, no public path, and slug compatibility warning. | Does not prove validators, payloads, or policy enforcement. |
| [`../../data/processed/settlements-infrastructure/README.md`](../../data/processed/settlements-infrastructure/README.md) | CONFIRMED README | Processed artifacts remain upstream of catalog/triplet/publication/release and are not normal public sources. | Actual child inventory and runtime enforcement remain NEEDS VERIFICATION. |
| [`../../data/catalog/domain/settlements-infrastructure/README.md`](../../data/catalog/domain/settlements-infrastructure/README.md) | CONFIRMED README | Domain catalog records are CATALOG-stage carriers, release-gated, and not truth/public by placement. | Catalog inventory, schemas, validators, access controls, and route behavior remain NEEDS VERIFICATION. |
| [`../../data/proofs/settlement/README.md`](../../data/proofs/settlement/README.md) | CONFIRMED README | Settlement-sublane proof support exists inside broader Settlements/Infrastructure doctrine. | It does not resolve the broader proof-path segment conflict. |
| [`../../data/receipts/settlement/README.md`](../../data/receipts/settlement/README.md) | CONFIRMED README | Settlement-sublane process-memory receipts exist as support, not proof or release authority. | It does not prove emitted receipts or final naming governance. |
| [`../../data/published/layers/settlements-infrastructure/README.md`](../../data/published/layers/settlements-infrastructure/README.md) | CONFIRMED README | Published layer lane is for released public-safe artifacts and preserves slug variance. | Concrete released payloads and route behavior remain NEEDS VERIFICATION. |
| [`../../contracts/runtime/decision_envelope.md`](../../contracts/runtime/decision_envelope.md) | CONFIRMED current contract text | Finite runtime outcomes are `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR`. | Does not make this examples lane runtime authority or prove implementation wiring. |
| [`../../tests/domains/settlements-infrastructure/README.md`](../../tests/domains/settlements-infrastructure/README.md) | CONFIRMED README | A domain test parent and documented identity sublane exist. | Executable tests, validators, CI coverage, and pass rates remain `NEEDS VERIFICATION`. |
| [`../../fixtures/domains/settlements-infrastructure/README.md`](../../fixtures/domains/settlements-infrastructure/README.md) | CONFIRMED greenfield stub | The working domain fixture path is present. | Accepted fixture structure, payloads, validation, and example parity are not established. |
| [`../../.github/CODEOWNERS`](../../.github/CODEOWNERS) | CONFIRMED repository evidence | Default GitHub review route is `@bartytime4life`. | Routing is not stewardship, review completion, policy approval, or release authorization. |
| [`../../.github/workflows/docs-build.yml`](../../.github/workflows/docs-build.yml), [`link-check.yml`](../../.github/workflows/link-check.yml), and [`accessibility.yml`](../../.github/workflows/accessibility.yml) | CONFIRMED workflow text | The repository exposes docs-build, link-check, and accessibility readiness holds. | They do not establish rendering, link validity, accessibility, release, or publication. |
| [`../../docs/doctrine/directory-rules.md`](../../docs/doctrine/directory-rules.md) | CONFIRMED doctrine | `examples/` owns worked examples; domain names remain lane segments; lifecycle, proof, receipt, release, and publication responsibilities stay separate. | Some implementation path claims remain PROPOSED / NEEDS VERIFICATION per doctrine notes. |

[Back to top](#top)
