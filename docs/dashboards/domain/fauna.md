<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/dashboards-domain-fauna
title: Fauna Dashboard Specification
type: standard
version: v0.2.0
status: draft
owners: "@bartytime4life (CODEOWNERS review route); fauna, sensitivity, and governance-health stewards NEEDS VERIFICATION"
created: 2026-05-26
updated: 2026-08-21
policy_label: public
related:
  - kfm://doc/dashboards-domain-readme
  - kfm://doc/domains-fauna-dossier
  - ../../domains/fauna/README.md
  - ../../../apps/explorer-web/src/features/domains/fauna/README.md
  - ../../../contracts/domains/fauna/occurrence_evidence.md
  - ../../../policy/domains/fauna/README.md
  - ../../../policy/sensitivity/fauna/README.md
tags: [kfm, dashboards, domain, fauna, sensitivity, geoprivacy, evidence, governance-health, specification]
notes:
  - Same-path modernization of the per-domain dashboard specification; no dashboard route, release, or publication is created.
  - Dashboard indicators report derived posture. Contracts define meaning, schemas define shape, policy decides, review records disposition, and release artifacts authorize public use.
  - Sensitive Fauna occurrence and site information remains deny-by-default; this document contains no exact locations or exposure-aiding thresholds.
[/KFM_META_BLOCK_V2] -->

# Fauna Dashboard Specification

<!-- [doc: kfm://doc/dashboards-domain-fauna] -->
<a id="top"></a>

This draft specifies a review-facing Fauna dashboard that reports evidence,
sensitivity, validation, and release posture without becoming an authority for
Fauna truth, policy, review, or publication.

> [!IMPORTANT]
> **Current status.** Repository evidence confirms a bounded Fauna feature
> directory, an Evidence Drawer adapter, draft occurrence-evidence machinery,
> deterministic fixture checks, and fail-closed CI holds. It does **not** confirm
> a routed dashboard, production telemetry, accepted indicator thresholds, live
> source admission, release readiness, deployment, or publication.

> [!CAUTION]
> **Sensitive information stays closed.** Exact sensitive occurrences, nests,
> dens, roosts, hibernacula, spawning sites, steward-controlled records, and
> re-identifying joins must not appear in a public dashboard. An unresolved
> rights, sensitivity, geoprivacy, evidence, review, policy, correction, or
> release dependency produces a safe hold, restriction, abstention, denial, or
> error—not a guessed value or an exposure hint.

## Contents

1. [Domain scope](#1-domain-scope)
2. [Indicator subset](#2-indicator-subset)
3. [Domain-specific indicators](#3-domain-specific-indicators-proposed)
4. [Ownership](#4-ownership)
5. [Implementation pointer](#5-implementation-pointer)
6. [Review cadence](#6-review-cadence)
7. [Open questions](#7-open-questions)
8. [Evidence basis and citations](#8-evidence-basis--citations)

---

## 1. Domain scope

The dashboard covers aggregate operational posture for Fauna taxonomy,
occurrence evidence, generalized public representations, sensitivity controls,
evidence resolution, and correction readiness.

It may report:

- finite validator outcomes and safe reason-code families;
- completeness of source, rights, sensitivity, evidence, policy, and review
  dependencies;
- coverage of public-safe transformation records;
- EvidenceRef-to-EvidenceBundle resolution for claim-bearing UI payloads;
- public-safe field-allowlist and presentation-state coverage; and
- explicit proof, release, correction, and rollback holds.

It must not:

- expose exact or reverse-engineerable sensitive locations, small-cell counts,
  transformation parameters, source-restricted attributes, or private review
  material;
- turn an observation, model, map layer, tile, fixture, validator result, badge,
  or AI response into Fauna truth;
- redefine contracts, schemas, source roles, sensitivity tiers, policy outcomes,
  review authority, or release eligibility;
- read RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLETS, or internal registry
  stores directly from a public client; or
- treat a green workflow, pull request, merge, or rendered chart as promotion or
  publication.

Public clients consume governed API envelopes or release-approved public-safe
artifacts. Claim-bearing UI details resolve EvidenceRefs to EvidenceBundles
before presentation as authoritative. The dashboard is an interpretive surface
over those governed inputs.

[↑ Back to top](#top)

---

## 2. Indicator subset

These are bounded Fauna instances of the parent dashboard categories. They do
not replace a master indicator catalog or create executable policy.

| ID | Indicator | Computation and healthy posture | Governed input | Current state |
|:---|:---|:---|:---|:---|
| `FAUNA-DB-01` | Sensitive public-path protection | Count public render or export candidates rejected for disallowed exact, restricted, or re-identifying fields. Any confirmed public exposure is a critical defect; `NO_DATA` must never render as 100% safe. | Policy and validation outcomes, release-approved field profiles, incident/correction records | **PROPOSED metric**; fixture-only field-allowlist checks are CONFIRMED, production telemetry is UNKNOWN. |
| `FAUNA-DB-02` | Occurrence-evidence disposition | Report `pass`, `quarantine`, `deny`, and `error` counts by safe reason-code family. No record may claim `pass` while required source, rights, taxonomy, evidence, sensitivity, policy, or review support is unresolved. | `OccurrenceEvidence` validator output and validation reports | **PARTIAL:** draft schema, validator, fixtures, tests, and CI are CONFIRMED; live-source and runtime use remain held. |
| `FAUNA-DB-03` | Evidence resolution | Numerator: eligible claim-bearing UI payloads whose EvidenceRefs resolve to an audience-appropriate EvidenceBundle. Denominator: all eligible claim-bearing payloads in the same snapshot. Unresolved support blocks an authoritative answer. | EvidenceBundle resolver results and Evidence Drawer payloads | **PARTIAL:** Fauna Evidence Drawer adapter and schema-convergence checks are CONFIRMED; a routed dashboard and production observations are UNKNOWN. |
| `FAUNA-DB-04` | Public-safe transform provenance | Numerator: sensitive-derived public candidates with the required transform, receipt, review, policy, and release references. Denominator: all sensitive-derived public candidates in scope. Missing support yields `HOLD` or `DENY`. | Redaction or aggregation receipt, ReviewRecord, PolicyDecision, ReleaseManifest | **HOLD:** the Fauna RedactionReceipt contract records a placement/schema conflict and does not yet prove executable coverage. |
| `FAUNA-DB-05` | Source-role and taxonomy closure | Report unresolved source-role mappings, role/basis mismatches, unresolved taxonomy, and correction-required records without collapsing aggregator identity into source authority. | Source descriptors, occurrence validation findings, taxonomy lineage | **PARTIAL:** deterministic source-role and occurrence checks exist; accepted taxonomy authority and live source admission remain NEEDS VERIFICATION. |
| `FAUNA-DB-06` | Public tile field posture | Compare a candidate LayerManifest field set with the reviewed allowlist. Any denied or undeclared field fails closed; a style-only check does not count as field safety. | Tile-field allowlist policy, validator findings, LayerManifest | **PARTIAL:** inactive synthetic profile, validator, tests, and workflow are CONFIRMED; production tile bytes and public approval are not. |
| `FAUNA-DB-07` | Proof and release readiness | Show the explicit proof and release-dry-run hold until accepted producers, candidate identity, EvidenceBundle closure, review, correction, and rollback artifacts exist. Never infer readiness from absence of failures. | Fauna domain workflow, proof inventory, release candidates and manifests | **CONFIRMED HOLD** at the inspected snapshot. |

### Measurement envelope

Every displayed measurement should carry, or resolve to, the following fields:

| Field | Requirement |
|:---|:---|
| Metric identity | Stable indicator ID plus specification version. |
| Snapshot identity | Immutable run, report, or artifact reference; not “latest” without a resolved object. |
| Time | UTC observation window, calculation time, and source-valid time where applicable. |
| Population | Explicit numerator, denominator, exclusions, and completeness state. |
| Presentation state | `AVAILABLE`, `NO_DATA`, `STALE`, `INCOMPLETE`, or `ERROR` as **PROPOSED UI states**, separate from policy and validator outcomes. |
| Authority references | SourceDescriptor, EvidenceRef/EvidenceBundle, schema/spec hash, policy version, and review/release references as required. |
| Sensitivity | Audience and aggregation/generalization posture; suppress or restrict unsafe small cells and re-identifying combinations. No threshold is invented here. |
| Correction | Supersession, withdrawal, correction notice, and rollback target when the source snapshot changes. |

If the denominator is unknown or incomplete, the dashboard must disclose that
state and withhold a percentage. If a safe aggregation threshold is unresolved,
the dashboard must deny or restrict the view rather than guess.

[↑ Back to top](#top)

---

## 3. Domain-specific indicators (PROPOSED)

The following extensions require an accepted metric contract before runtime use:

| Candidate | Purpose | Minimum dependency | Safe failure behavior |
|:---|:---|:---|:---|
| Taxonomy-correction backlog | Surface records affected by misidentification, synonym, split, merge, or authority changes. | Stable taxon concept lineage, correction reason codes, and supersession references. | `INCOMPLETE` or `HOLD`; never silently rewrite historical claims. |
| Listing-change response | Measure time from an admitted conservation-status change to reviewed sensitivity and public-safe disposition. | Admitted authority source, valid-time semantics, PolicyDecision, ReviewRecord, and correction path. | `NO_DATA` or `HOLD`; never scrape or infer current legal status from dashboard prose. |
| Geoprivacy transform drift | Detect public derivatives whose current policy/spec version no longer matches the transform evidence used to create them. | Resolved transform/receipt identity, policy version, source snapshot, and release manifest. | `DENY` public detail and open correction review without revealing transformation parameters. |
| Re-identification risk review | Count combinations of otherwise generalized attributes that require additional restriction. | Reviewed risk profile and public-safe fixture coverage. | Restrict the combined view; expose only a non-reconstructive reason code. |

Exact locality thresholds, taxon-specific generalization rules, reviewer identities,
and source terms belong to their governing policy, registry, and review records;
they are intentionally absent from this public specification.

[↑ Back to top](#top)

---

## 4. Ownership

| Responsibility | Current disposition |
|:---|:---|
| Repository review route | **CONFIRMED:** `@bartytime4life` is the default CODEOWNERS route. CODEOWNERS routing does not prove review, stewardship, or approval. |
| Fauna domain steward | **NEEDS VERIFICATION:** no verified identity is assigned by this document. |
| Sensitivity reviewer | **NEEDS VERIFICATION:** the parent dashboard register keeps stricter sensitive-domain review as `OPEN-DASH-08`. |
| Governance-health / metric steward | **NEEDS VERIFICATION:** required to approve indicator semantics, windows, completeness, and correction behavior. |
| Application owner | **NEEDS VERIFICATION:** the current implementation evidence is under Explorer Web; no dashboard owner or route is confirmed. |

The author or generator is not the sole approver for a policy-significant change.
Merge review, sensitivity review, release approval, and publication authority
remain separate transitions.

[↑ Back to top](#top)

---

## 5. Implementation pointer

### Current repository evidence

| Surface | Verified state | Boundary |
|:---|:---|:---|
| [`docs/domains/fauna/README.md`](../../domains/fauna/README.md) | Draft Fauna domain lane with deny-by-default sensitive-occurrence posture. | Doctrine and domain context, not runtime enforcement. |
| [`contracts/domains/fauna/occurrence_evidence.md`](../../../contracts/domains/fauna/occurrence_evidence.md), [schema](../../../schemas/contracts/v1/domains/fauna/occurrence_evidence.schema.json), [validator](../../../tools/validators/domains/fauna/occurrence/validate_occurrence_evidence.py), and [tests](../../../tests/domains/fauna/test_occurrence_evidence.py) | Fixture-first draft profile with deterministic identity, finite outcomes, and fail-closed checks. | Does not admit live sources, resolve EvidenceBundles, authorize public derivatives, or release data. |
| [`apps/explorer-web/src/features/domains/fauna/EvidenceDrawer.tsx`](../../../apps/explorer-web/src/features/domains/fauna/EvidenceDrawer.tsx) | Re-exports the shared Evidence Drawer controller and view model. | Confirms an adapter surface, not a routed Fauna dashboard or runtime data. |
| [`fauna-evidence-drawer-convergence.yml`](../../../.github/workflows/fauna-evidence-drawer-convergence.yml) | Read-only, no-network schema/convergence test definition. | A workflow definition or passing run is not evidence truth or release authority. |
| [`FocusFlow.tsx`](../../../apps/explorer-web/src/features/domains/fauna/FocusFlow.tsx) and [`layers.ts`](../../../apps/explorer-web/src/features/domains/fauna/layers.ts) | Greenfield placeholders. | Must not be described as implemented Focus Mode or map-layer behavior. |
| [`fauna-tile-field-allowlist.yml`](../../../.github/workflows/fauna-tile-field-allowlist.yml) | Deterministic inactive, fixture-only allowlist validation. | Does not inspect production tile bytes or approve a public field set. |
| [`domain-fauna.yml`](../../../.github/workflows/domain-fauna.yml) | Runs the accepted synthetic smoke slice and preserves explicit proof and release-dry-run holds. | Performs no source access, transform, promotion, release, deployment, or publication. |
| [`data/registry/sources/fauna/`](../../../data/registry/sources/fauna/README.md) | Source-registry boundary exists. | Current rights, terms, cadence, field mapping, and source activation remain individually governed. |
| [`contracts/domains/fauna/redaction_receipt.md`](../../../contracts/domains/fauna/redaction_receipt.md) | Draft Fauna semantics with a disclosed cross-domain placement/schema conflict. | Not an accepted executable receipt contract; cannot substantiate coverage alone. |

### Proposed read path

```text
governed API or release-approved public-safe artifact
  -> runtime-validated finite envelope
  -> evidence / policy / review / release references
  -> aggregate metric calculation with sensitivity controls
  -> Fauna dashboard presentation
```

No dashboard route, telemetry adapter, metric store, or release binding was
confirmed at the inspected snapshot. Those remain implementation work, not
documentation facts.

[↑ Back to top](#top)

---

## 6. Review cadence

Review this specification when any of the following occurs:

- the Fauna domain lane changes its sensitivity, evidence, source-role,
  taxonomy, correction, or rollback posture;
- an occurrence, EvidenceBundle, Evidence Drawer, tile-field, receipt, policy,
  review, release, or runtime contract changes;
- a dashboard route, telemetry source, metric window, aggregation rule, or
  public export is introduced;
- a source-rights or conservation-status change affects admissibility;
- an incident, correction, withdrawal, or rollback reveals an unsafe or stale
  metric; or
- the parent dashboard catalog or `OPEN-DASH-08` reviewer disposition changes.

### Changed-document checks

The repository workflows apply changed-file metadata, document-graph, and
no-network local-link checks. A focused local link check is:

```bash
python tools/validators/docs/link-check/check_links.py \
  --repo-root . \
  --format text \
  docs/dashboards/domain/fauna.md
```

The accepted synthetic Fauna smoke slice is:

```bash
KFM_NO_NETWORK=1 PYTHONDONTWRITEBYTECODE=1 \
  python -m unittest discover \
  --start-directory tests/domains/fauna \
  --pattern 'test_fauna_smoke.py' \
  --verbose
```

Passing these checks proves only their bounded document and fixture contracts.
It does not establish source truth, current rights, taxonomic authority,
EvidenceBundle closure, sensitivity review, safe public use, release readiness,
deployment, or publication.

[↑ Back to top](#top)

---

## 7. Open questions

- [ ] **OPEN-DASH-FAUNA-01** — Which reviewed metric contract defines safe
  aggregation and suppression without recording exposure-aiding thresholds in
  this public document?
- [ ] **OPEN-DASH-FAUNA-02** — Which shared receipt family is canonical for
  geoprivacy/redaction evidence, and how will the current Fauna placement/schema
  conflict be resolved without parallel authority?
- [ ] **OPEN-DASH-FAUNA-03** — Which verified identity serves as sensitivity
  reviewer, and which repository control—if any—enforces that review?
- [ ] **OPEN-DASH-FAUNA-04** — What accepted route, telemetry contract, and
  immutable snapshot identity will supply the dashboard?
- [ ] **OPEN-DASH-FAUNA-05** — Which correction and withdrawal events invalidate
  a historical metric snapshot and its downstream caches or exports?

[↑ Back to top](#top)

---

## 8. Evidence basis & citations

Evidence was inspected against
[`main@51d45e45a56d19961a3014009b80c2c94b1107ee`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/commit/51d45e45a56d19961a3014009b80c2c94b1107ee)
on 2026-08-21.

| Source | Status | Supports | Does not prove |
|:---|:---|:---|:---|
| [Parent dashboard specification](./README.md) | **CONFIRMED file / PROPOSED lane** | Per-domain scope, indicator-instance boundary, anti-collapse rule, and open sensitive-domain review question. | Accepted dashboard authority, implementation, or reviewer assignment. |
| [Fauna domain lane](../../domains/fauna/README.md) and [sensitivity posture](../../domains/fauna/SENSITIVITY.md) | **CONFIRMED draft documentation** | T4 deny-by-default posture, geoprivacy boundary, finite public outcomes, and governed API path. | Executable policy, reviewed release, or current source truth. |
| [Occurrence Evidence contract](../../../contracts/domains/fauna/occurrence_evidence.md) and [focused workflow](../../../.github/workflows/fauna-occurrence-evidence.yml) | **CONFIRMED draft machinery** | Finite disposition states, deterministic validation, source-role separation, synthetic fixture coverage, and explicit holds. | Live-source admission, EvidenceBundle closure, public derivative, or publication. |
| [Explorer Web Fauna feature boundary](../../../apps/explorer-web/src/features/domains/fauna/README.md) and current TypeScript files | **CONFIRMED repository surfaces** | Evidence Drawer adapter exists; FocusFlow and layers are placeholders. | A dashboard route, complete feature, runtime behavior, deployment, or public availability. |
| [Fauna domain workflow](../../../.github/workflows/domain-fauna.yml) | **CONFIRMED read-only workflow definition** | Synthetic smoke validation and explicit proof/release holds. | Hosted pass at an arbitrary head, proof, release readiness, or publication. |
| [Directory Rules](../../doctrine/directory-rules.md) and [accepted ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) | **CONFIRMED adopted placement authority** | Documentation may reference every responsibility root but gains no executable authority through prose; public clients use governed APIs or released carriers. | That the separately proposed `docs/dashboards/` lane has been independently adopted as canonical. |
| [CODEOWNERS](../../../.github/CODEOWNERS) | **CONFIRMED review routing** | `@bartytime4life` is the verified default repository review route. | Human review, domain stewardship, sensitivity approval, or branch-protection enforcement. |

### Material change ledger

- **KEEP:** document ID, path, created date, draft status, T4 deny-by-default
  posture, specification-only boundary, numbered section anchors, and open
  reviewer/receipt questions.
- **CLARIFY:** dashboards report derived posture; contracts, schemas, policy,
  reviews, and release artifacts retain their separate authority.
- **REPAIR:** replace obsolete `apps/review-console/` and unverified telemetry
  pointers with current Explorer Web, contract, validator, fixture, and workflow
  evidence.
- **REMOVE WITH EVIDENCE:** arbitrary health percentages, decorative external
  badges, and source-currentness implications not supported by current runtime
  evidence.
- **ENRICH:** add measurement envelopes, finite missing/stale/error states,
  sensitivity-safe computation rules, validation commands, correction triggers,
  and explicit implementation holds.

This document is a specification and review aid. It is not a PolicyDecision,
ReviewRecord, EvidenceBundle, RedactionReceipt, ValidationReport,
ReleaseManifest, correction notice, rollback card, deployment record, or
publication artifact.

[↑ Back to top](#top)
