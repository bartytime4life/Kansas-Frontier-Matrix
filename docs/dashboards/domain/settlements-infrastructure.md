<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/dashboards-domain-settlements-infrastructure
title: Settlements / Infrastructure Dashboard Specification
type: standard
version: v0.2.0
status: draft
owners: "@bartytime4life (CODEOWNERS review route); Settlements / Infrastructure, sensitivity, evidence, metric, UI, and release stewards NEEDS VERIFICATION"
created: 2026-05-26
updated: 2026-08-21
policy_label: public
owning_root: docs/
responsibility: "Review-facing Settlements / Infrastructure dashboard specification and repository-state reporting only; not source, evidence, policy, runtime, emergency, utility, release, or publication authority."
truth_posture: "CONFIRMED current repository evidence / PROPOSED indicators and presentation states / UNKNOWN routed dashboard, telemetry, deployment, and publication"
related:
  - ../DASHBOARD_CATALOG.md
  - README.md
  - ../../domains/settlements-infrastructure/README.md
  - ../../domains/settlements-infrastructure/DENY_BY_DEFAULT.md
  - ../../../apps/explorer-web/src/features/domains/settlements_infrastructure/README.md
  - ../../../contracts/domains/settlements-infrastructure/README.md
  - ../../../schemas/contracts/v1/domains/settlements-infrastructure/README.md
  - ../../../policy/domains/settlements-infrastructure/README.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../doctrine/directory-rules.md
tags: [kfm, dashboards, domain, settlements, infrastructure, critical-infrastructure, evidence, sensitivity, correction, rollback, specification]
notes:
  - "v0.2.0 reconciles this specification with current contracts, schemas, bounded EvidenceBundle convergence proof, placeholder Explorer files, policy/validator/test scaffolds, source-registry posture, and explicit proof/release holds."
  - "The document omits exposure-aiding facility detail, dependency topology, operational condition detail, and unadopted public-safety thresholds."
  - "A dashboard, metric producer, telemetry binding, release candidate, deployment, or publication is not established by this document."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Settlements / Infrastructure Dashboard Specification

**Repository-grounded review specification for place identity, infrastructure exposure posture, evidence closure, public-safe transformation, correction, and rollback.**

![status](https://img.shields.io/badge/status-draft-blue)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)
![runtime](https://img.shields.io/badge/runtime-UNKNOWN-lightgrey)
![sensitivity](https://img.shields.io/badge/sensitivity-fail--closed-critical)

[Scope](#1-domain-scope) · [Indicators](#2-indicator-contracts) · [Measurement](#3-measurement-envelope-and-finite-states) · [Evidence](#4-current-repository-evidence) · [Ownership](#5-ownership-and-review) · [Implementation](#6-implementation-and-acceptance-boundary) · [Validation](#9-validation) · [Rollback](#10-maintenance-correction-and-rollback)

> [!IMPORTANT]
> **Current checkpoint.** Current repository evidence confirms domain documentation, semantic contracts, schema families, a shared `EvidenceBundle` projection with focused no-network validation, an Explorer feature directory, domain policy/test/validator lanes, and bounded readiness workflows. The inspected Explorer `EvidenceDrawer.tsx` and `layers.ts` files remain placeholders. Domain-local policy, validator, and representative test files remain scaffolds. The domain workflow explicitly holds semantic validation, proof production, and release dry-run readiness. No routed dashboard, production metric producer, telemetry binding, live-source admission, release, deployment, or publication is confirmed.

> [!CAUTION]
> **Public-safe reporting only.** This specification must not expose exact or reverse-engineerable critical-infrastructure geometry, interiors, dependency topology, condition or vulnerability detail, operator-sensitive attributes, live service availability, emergency-readiness state, private-property joins, or person/parcel/facility compositions. A dashboard may report aggregate governance posture and finite outcomes; it may not become infrastructure-security disclosure, municipal legal authority, utility or operator truth, emergency guidance, or a shortcut around policy and release review.

> [!NOTE]
> `@bartytime4life` is the verified repository review route through `CODEOWNERS`. Routing is not proof of domain, sensitivity, security, policy, or release approval. Accountable reviewer identities remain `NEEDS VERIFICATION`.

---

## 1. Domain scope

This file specifies a **review-facing governance-health projection** for the Settlements / Infrastructure lane. It may summarize posture for:

- settlement, municipality, census-place, historic-townsite, and other place-identity separation;
- infrastructure asset, facility, service-area, operator, condition-observation, and dependency records without collapsing their meanings;
- source role, source vintage, temporal support, rights, sensitivity, evidence, review, release, and correction state;
- public-safe transformation and representation coverage;
- EvidenceRef-to-EvidenceBundle closure for eligible claim-bearing payloads;
- proof, candidate-release, correction, derivative-invalidation, withdrawal, and rollback readiness;
- implementation maturity across documentation, contracts, schemas, policy, validators, tests, workflows, and Explorer surfaces.

It must not decide municipal incorporation, boundary, ownership, facility, service-area, operator, condition, dependency, utility, availability, emergency, or security truth. It must not treat a map feature, tile, popup, test, workflow result, dashboard card, screenshot, or generated explanation as sovereign evidence. It must not read RAW, WORK, QUARANTINE, candidate, or other canonical/internal stores as the normal public path.

```text
released public-safe artifact or governed API envelope
  -> validated object and source-role semantics
  -> EvidenceRef -> EvidenceBundle resolution
  -> rights / sensitivity / policy / review / release checks
  -> aggregate dashboard measurement
  -> restricted, abstaining, or error state when closure fails
```

[↑ back to top](#top)

---

## 2. Indicator contracts

The following are **PROPOSED metric contracts**, not implemented telemetry. Numeric thresholds are intentionally not invented. Every future producer must define its eligible population, numerator, denominator, time window, evidence inputs, sensitivity profile, and safe failure behavior before displaying a percentage or trend.

| ID | Indicator | Proposed healthy posture | Required support | Current state |
|---|---|---|---|---|
| `SI-DB-01` | **Restricted public-path protection** | Zero confirmed restricted-detail exposures; an unknown or unmeasured population is `INCOMPLETE`, never an implied 100%. | Public-safe field/geometry profiles, policy and review results, release manifests, representation checks, incident/correction records. | **PROPOSED.** Domain policy files are inactive greenfield stubs and no exposure-audit producer is confirmed. |
| `SI-DB-02` | **Place-role and vintage separation** | Legal, statistical, historical, and interpretive place roles remain explicit with source role, geography version, and temporal support. | Domain contracts/schemas, identity and crosswalk reports, source/valid/retrieval/release times. | **PARTIAL surface.** Contract/schema families exist; substantive domain semantic validation remains held. |
| `SI-DB-03` | **EvidenceBundle closure** | Every eligible claim-bearing payload either resolves to a schema-valid EvidenceBundle or returns `ABSTAIN`/`HOLD`. | Shared EvidenceBundle shape and fixtures, domain projection, resolver output, citations, spec hash. | **CONFIRMED bounded shape proof.** Runtime resolution and dashboard binding remain `UNKNOWN`. |
| `SI-DB-04` | **Public-safe transform provenance** | Every public derivative of restricted material carries the applicable transform/representation receipt, policy result, review state, released identity, correction path, and rollback target. | Receipt, PolicyDecision, ReviewRecord, ValidationReport, ReleaseManifest, CorrectionNotice/RollbackCard. | **PROPOSED.** No accepted domain proof or release producer is confirmed. |
| `SI-DB-05` | **Condition and dependency exposure control** | Condition, vulnerability, dependency, operator, and live-service implications remain restricted unless an accepted profile explicitly permits a safe aggregate. | Field classification, join-purpose and audience profile, anti-reidentification tests, policy and review decisions. | **HOLD.** Domain-local validators/tests are placeholders and policy enforcement is not established. |
| `SI-DB-06` | **Correction and derivative invalidation** | Every corrected or withdrawn release identifies affected derivatives and reaches a bounded corrected, withdrawn, or rolled-back state. | Deterministic lineage, Correction/WithdrawalNotice, cache/index/tile invalidation records, rollback target. | **PROPOSED.** No domain candidate or rollback drill is confirmed. |
| `SI-DB-07` | **Implementation and release readiness** | Maturity is reported by evidence-backed components and explicit holds, never by file counts or a green placeholder workflow alone. | Contracts, schemas, fixtures, validators, tests, policy, workflows, proofs, candidates, review, release and rollback evidence. | **CONFIRMED mixed maturity / HOLD.** Structural readiness and one focused schema packet exist; semantic validation, proof, and release remain held. |

### Candidate drill-downs

These remain `PROPOSED` until a metric contract and safe producer are accepted:

- unresolved place-role/vintage conflicts by non-sensitive object family;
- EvidenceBundle closure by claim family and immutable snapshot;
- transform/representation receipt coverage by approved public-safe profile;
- correction-to-derivative-invalidation state by release identity;
- scaffolding-to-substantive-validation maturity by responsibility root;
- source-admission/currentness posture without exposing restricted source or facility detail.

[↑ back to top](#top)

---

## 3. Measurement envelope and finite states

Every emitted measurement should bind:

| Dimension | Required content |
|---|---|
| Identity | Stable indicator ID, metric-contract version, producer identity, computation/spec hash. |
| Snapshot | Immutable run/artifact ID and content digest; never an unqualified “latest” value. |
| Time | Valid, observed where applicable, source, retrieval, measurement-window, release, correction, and stale state. |
| Population | Eligibility rule, exclusions, numerator, denominator, units, aggregation, and null/unknown semantics. |
| Evidence and authority | SourceDescriptor/source head, EvidenceRefs and resolved bundles, contracts/schemas, PolicyDecision, ReviewRecord, ReleaseManifest, validation reports. |
| Domain semantics | Object family, source role, knowledge character, place/asset role, geography/vintage, and cross-lane seam identity. |
| Sensitivity and audience | Access label, public-safe profile, authorized audience, and minimum necessary aggregate disclosure. |
| Correction | Superseded measurement, correction/withdrawal reference, invalidation state, rollback target, current disposition. |

Presentation state is separate from policy and runtime outcome:

| Presentation state | Meaning |
|---|---|
| `AVAILABLE` | A public-safe released aggregate is supported for the audience. |
| `NO_DATA` | The eligible snapshot contains no reportable measurement; this does not prove real-world absence. |
| `STALE` | Prior measurement identity and age remain visible; it is not presented as current. |
| `INCOMPLETE` | Population, evidence, or producer coverage is insufficient for a complete result. |
| `RESTRICTED` | The value is withheld without disclosing protected reasons or payloads. |
| `ERROR` | Resolver, validator, policy, producer, telemetry, or delivery failed; never fall back to `AVAILABLE`. |

Governed outcomes converge on `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`. `HOLD` is a repository review/readiness disposition and must not be rendered as `ANSWER`, `AVAILABLE`, or release-ready.

[↑ back to top](#top)

---

## 4. Current repository evidence

| Surface | Status at the pinned checkpoint | What it proves | What it does not prove |
|---|---|---|---|
| [`docs/domains/settlements-infrastructure/README.md`](../../domains/settlements-infrastructure/README.md) and [`DENY_BY_DEFAULT.md`](../../domains/settlements-infrastructure/DENY_BY_DEFAULT.md) | **CONFIRMED docs** | Scope, object-family separation, sensitivity, public-safe, correction, and release boundaries are documented. | Executable enforcement, admitted sources, current real-world claims, or release state. |
| [`apps/explorer-web/src/features/domains/settlements_infrastructure/`](../../../apps/explorer-web/src/features/domains/settlements_infrastructure/README.md) | **CONFIRMED directory** | App-local boundary exists. [`EvidenceDrawer.tsx`](../../../apps/explorer-web/src/features/domains/settlements_infrastructure/EvidenceDrawer.tsx) and [`layers.ts`](../../../apps/explorer-web/src/features/domains/settlements_infrastructure/layers.ts) are present. | Both inspected files export only greenfield placeholders; no route, panel, map binding, producer, or telemetry is established. |
| [`contracts/domains/settlements-infrastructure/`](../../../contracts/domains/settlements-infrastructure/README.md) | **CONFIRMED semantic family** | Domain object meanings and delivery/evidence concepts have documented homes. | Adoption, producer/consumer conformance, policy approval, or runtime use. |
| [`schemas/contracts/v1/domains/settlements-infrastructure/`](../../../schemas/contracts/v1/domains/settlements-infrastructure/README.md) | **CONFIRMED schema lane** | Machine-shape family exists. The [`EvidenceBundle` projection](../../../schemas/contracts/v1/domains/settlements-infrastructure/evidence_bundle.schema.json) delegates to the shared closed shape and grants no exposure or release authority. | Evidence authenticity, source truth, policy approval, public use, or full domain-schema maturity. |
| [`schemas/contracts/v1/settlements-infrastructure/README.md`](../../../schemas/contracts/v1/settlements-infrastructure/README.md) | **CONFIRMED compatibility index** | The flat path identifies itself as compatibility-only and points to the domain lane. | A second canonical schema home or an authorized migration. |
| Focused EvidenceBundle packet | **CONFIRMED bounded executable proof** | The [validator](../../../tools/validators/validate_settlements_infrastructure_evidence_bundle_projection.py), [test](../../../tests/validators/domains/settlements-infrastructure/test_evidence_bundle_schema_convergence.py), and read-only no-network [workflow](../../../.github/workflows/settlements-infrastructure-evidence-bundle-convergence.yml) validate delegation and fixture polarity. | Live EvidenceRef resolution, claim truth, sensitivity review, policy enforcement, release, or dashboard telemetry. |
| Domain-local validator/test lanes | **CONFIRMED scaffolds / HOLD** | [`validate_schema.py`](../../../tools/validators/domains/settlements-infrastructure/validate_schema.py) raises `NotImplementedError`; [`test_restricted_geometry_no_leak.py`](../../../tests/domains/settlements-infrastructure/test_restricted_geometry_no_leak.py) is docstring-only. | Substantive semantic, geometry, public-boundary, or sensitivity validation. |
| [`policy/domains/settlements-infrastructure/`](../../../policy/domains/settlements-infrastructure/README.md) | **CONFIRMED lane / inactive stubs** | Intended policy boundary is documented. Inspected Rego files declare no real rules. | Fail-closed runtime enforcement. A default-allow scaffold is not protection. |
| [`domain-settlements-infrastructure.yml`](../../../.github/workflows/domain-settlements-infrastructure.yml) | **CONFIRMED readiness workflow** | Checks boundaries, parses schemas/fixtures, and records semantic-validation, proof, and release-dry-run holds. | Domain truth, EvidenceBundle creation, proof, policy, candidate release, deployment, or publication. |
| [`data/registry/sources/settlements-infrastructure/README.md`](../../../data/registry/sources/settlements-infrastructure/README.md) | **CONFIRMED registry docs / topology NEEDS VERIFICATION** | Source-registry responsibilities and no-public-path boundary are documented. | Admitted live sources, resolved rights/currentness, one canonical topology, or source truth. |
| Proof and candidate lanes | **CONFIRMED docs/hold surfaces** | [`data/proofs/settlements-infrastructure/README.md`](../../../data/proofs/settlements-infrastructure/README.md) and [`release/candidates/settlements-infrastructure/README.md`](../../../release/candidates/settlements-infrastructure/README.md) exist and are checked by the domain workflow. | Emitted proof, accepted candidate manifest, release decision, rollback drill, or publication. |

The dashboard implementation remains **PROPOSED** until repository evidence confirms a route, producer, schema-validated payload, governed delivery, policy/review/release binding, snapshot lineage, negative tests, access controls, correction behavior, and rollback path.

[↑ back to top](#top)

---

## 5. Ownership and review

| Responsibility | Current status | Boundary |
|---|---|---|
| Repository review route | **CONFIRMED:** `@bartytime4life` through [`CODEOWNERS`](../../../.github/CODEOWNERS). | Routing only; not approval or independent review. |
| Domain steward | **NEEDS VERIFICATION** | Owns domain meaning; cannot self-approve sensitivity or release. |
| Sensitivity / infrastructure-security reviewer | **NEEDS VERIFICATION** | Reviews exposure, aggregation, re-identification, and cross-lane composition. |
| Evidence / source steward | **NEEDS VERIFICATION** | Owns source admission, evidence closure, rights/currentness, and correction support. |
| Metric / observability steward | **NEEDS VERIFICATION** | Owns metric contracts, snapshots, telemetry lineage, and null/stale behavior. |
| Explorer / governed-API owner | **NEEDS VERIFICATION** | Owns implementation and governed delivery; cannot redefine evidence or policy. |
| Release / correction reviewer | **NEEDS VERIFICATION** | Owns release, correction, withdrawal, invalidation, and rollback separately from authorship. |

No placeholder role may be treated as author, approver, sensitivity reviewer, and release authority for the same policy-significant change.

[↑ back to top](#top)

---

## 6. Implementation and acceptance boundary

A future dashboard should consume an immutable aggregate envelope through the governed API or a released public-safe artifact. It must not compute trust decisions in the browser or query internal lifecycle stores.

```text
source and domain records
  -> accepted validators and policy
  -> EvidenceBundle / review / release / correction closure
  -> immutable aggregate metric envelope
  -> governed API or released public-safe artifact
  -> Explorer or review presentation
```

Before any runtime indicator graduates, tests should cover at least:

- unresolved or malformed EvidenceRef/EvidenceBundle support;
- undefined population, zero denominator, null, stale, corrected, withdrawn, and conflicting snapshots;
- legal/statistical/historical place-role or vintage mismatch;
- restricted facility, dependency, condition, operator, service-area, private-property, or cross-lane composition;
- transform/receipt missing, mismatched, stale, or bound to different bytes;
- policy, review, release, correction, or rollback reference absent or invalid;
- geometry, labels, styles, popups, exports, aggregates, timing, or differencing that reconstruct restricted detail;
- resolver, validator, policy engine, producer, telemetry, cache invalidation, or governed-API failure.

No fixture should contain real restricted infrastructure detail or harmful precision.

[↑ back to top](#top)

---

## 7. Review triggers

No steward-approved calendar cadence is confirmed. Review this specification when domain semantics, source roles, sensitivity/public-safe policy, evidence/release/correction objects, validators/tests/workflows, registry topology, Explorer routes, telemetry, or aggregate producers change. A suspected exposure or stale operational implication triggers immediate governed review; public documentation records only the safe correction outcome, not restricted incident detail.

[↑ back to top](#top)

---

## 8. Open questions

- [ ] **OPEN-DASH-SI-01 — Metric authority.** Which accepted contract/schema defines identity, population, time kinds, null semantics, sensitivity, and correction lineage?
- [ ] **OPEN-DASH-SI-02 — Verified reviewers.** Which identities hold domain, sensitivity/security, evidence/source, metric, UI/API, and release/correction responsibilities?
- [ ] **OPEN-DASH-SI-03 — Transform proof.** Which receipt/proof family is canonical for redaction, aggregation, representation, and anti-re-identification checks?
- [ ] **OPEN-DASH-SI-04 — Routed surface.** Which route, producer, snapshot store, governed envelope, telemetry signal, and access profile implement this dashboard?
- [ ] **OPEN-DASH-SI-05 — Compatibility convergence.** How do flat/singular schema and source-registry paths converge without parallel authority or consumer breakage?
- [ ] **OPEN-DASH-SI-06 — Correction cascade.** Which deterministic registry enumerates affected tiles, caches, indexes, exports, search, graph, and AI derivatives?
- [ ] **OPEN-DASH-SI-07 — Hold graduation.** Which validators, negative fixtures, policy tests, proof producer, candidate manifest, reviewers, and rollback drill retire each workflow hold?
- [ ] **OPEN-DASH-SI-08 — Safe aggregation.** Which approved minimum-disclosure and anti-differencing rules permit aggregate posture reporting? Keep operational thresholds out of public docs until approved.

[↑ back to top](#top)

---

## 9. Validation

From a mounted checkout, run the repository-native link check:

```bash
python tools/validators/docs/link-check/check_links.py \
  --repo-root . \
  --format text \
  docs/dashboards/domain/settlements-infrastructure.md
```

Also verify one H1, intact metadata, ordered headings, anchors, alert syntax, tables, balanced fences, no trailing whitespace, final newline, catalog-row alignment, generated-receipt hash closure, and absence of restricted payloads or exposure-aiding detail.

The focused EvidenceBundle packet may be exercised with:

```bash
python -m unittest discover \
  --start-directory tests/validators/domains/settlements-infrastructure \
  --pattern 'test_evidence_bundle_schema_convergence.py' \
  --verbose

python tools/validators/validate_settlements_infrastructure_evidence_bundle_projection.py \
  --fixtures
```

Passing those checks proves shared-schema projection and fixture polarity only. Do not run the domain-local placeholder validator as semantic proof, and do not treat the held domain workflow as a proof or release producer.

[↑ back to top](#top)

---

## 10. Maintenance, correction, and rollback

Update this specification and its [`Dashboard Catalog`](../DASHBOARD_CATALOG.md) row when a material repository fact changes: placeholders become substantive, metric or telemetry surfaces are admitted, a compatibility path migrates, source/evidence/policy maturity changes, a candidate or proof appears, reviewer identities are verified, or correction/rollback requirements change.

Do not rewrite historical receipts or retroactively claim approval. Add a successor record or forward correction that binds new bytes and preserves lineage.

Before merge, rollback is to close or abandon the draft pull request and leave `main` unchanged. After an authorized merge, revert the actual documentation/catalog/receipt commit or submit a forward correction against then-current bytes. No source, domain data, policy, app, release, deployment, or public-state rollback is required for this documentation-only change.

A future public-dashboard correction is broader than a Git revert. It must address the measurement snapshot, release manifest, map/search/export/AI derivatives, caches, correction notice, withdrawal/supersession state, and rollback target without exposing the protected reason or payload.

### Evidence and placement basis

- Current dashboard target, parent [`README.md`](README.md), and catalog: existing identity and inventory relationship; no runtime proof.
- Current domain docs, contracts, schemas, Explorer placeholders, focused validator/test/workflow, scaffolds, registry, proof, and candidate lanes: current maturity evidence bounded as above.
- [`ADR-0029`](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) and [`directory-rules.md`](../../doctrine/directory-rules.md): accepted responsibility-root placement and same-path documentation basis.
- [`CODEOWNERS`](../../../.github/CODEOWNERS): repository review routing only.

[↑ back to top](#top)

---

<sub>This file is a dashboard **specification and repository-state report**. It does not establish a metric producer, protected-data transform, policy decision, review approval, runtime route, release, deployment, or publication.</sub>
