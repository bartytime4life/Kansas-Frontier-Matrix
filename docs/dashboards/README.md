<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/dashboards-readme
title: Dashboards — Human-facing dashboard specifications and indicator catalogs
type: documentation-lane-readme
version: v1.0
status: "repository-grounded; active-path; placement-hold; runtime-needs-verification"
owners:
  - "@bartytime4life"
owner_status: "CONFIRMED GitHub review route through the repository default CODEOWNERS rule; dashboard, observability, domain, and independent-review stewardship assignments remain NEEDS VERIFICATION"
created: 2026-05-20
updated: 2026-08-14
policy_label: repository-facing
truth_posture: cite-or-abstain
owning_root: docs/
responsibility: "Define the human-readable dashboard-specification lane, its current repository inventory, trust boundaries, authoring contract, validation expectations, placement hold, and relationships to runtime, evidence, policy, and release authorities."
current_path: docs/dashboards/README.md
placement_status: "CONFIRMED existing path under canonical docs/ root; HOLD as an unadmitted direct-child lane in the adopted Directory Rules v2 canonical docs map"
runtime_status: "NEEDS VERIFICATION — specification presence is not running-dashboard evidence"
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: dc30e1d38f9a4ecf45fd589d388886fc872dd189
  target_prior_blob: 3749fc0099443c3c8b024357e0f1694253ff735e
  docs_root_readme_blob: 1f8bac189dac1d01c1185e8b4fb8e25efd11d09f
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  adr_0029_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  root_registry_blob: 024f668b5f0a9239bafa4f8b09e2afd86300ff8c
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  dashboard_catalog_blob: 30b9d35ede3410a8d2f946279891ae5ec2482a62
  indicator_catalog_blob: 4fe3d6be5b0b6ba6359a301942c01d713c8e970f
  governance_tree: 448e5614c90534266064dee9a218519876ca8b1c
  operational_tree: c24b6e74e62d0c895282a2e1d9defbe62750f62c
  domain_tree: f27f67d3d13b1082a8edd06d464a36c116130805
  observability_tree: d330bc33e5f94dd54f4d5487fe3ed30ac088f7c7
related:
  - docs/README.md
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/dashboards/DASHBOARD_CATALOG.md
  - docs/dashboards/INDICATOR_CATALOG.md
  - docs/dashboards/governance/README.md
  - docs/dashboards/operational/README.md
  - docs/dashboards/domain/README.md
  - docs/dashboards/observability/README.md
  - docs/atlases/KFM_Domains_Culmination_Atlas_v1_1.md
  - docs/registers/DRIFT_REGISTER.md
  - docs/registers/VERIFICATION_BACKLOG.md
  - apps/review-console/README.md
  - control_plane/root_registry.yaml
  - data/receipts/generated/README.md
tags: [kfm, docs, dashboards, specifications, governance-health, operational-health, domain-health, observability, cite-or-abstain]
notes:
  - "v1.0 is a same-path repository reconciliation. It replaces the 2026-05 evidence boundary with a pinned current-tree inventory and adopted Directory Rules v2 posture."
  - "The current dashboards subtree contains 34 specification files and seven lane/catalog navigation files, for 41 Markdown files total at the pinned base."
  - "Specification-file presence is CONFIRMED; running dashboards, telemetry production, query execution, metric computation, alerting, and deployed review-console integration remain NEEDS VERIFICATION."
  - "The dashboards lane reports posture. It does not create evidence, policy, review, release, correction, rollback, or publication authority."
  - "This documentation-only update does not settle the placement hold, migrate the lane, resolve duplicate observability filenames, or alter runtime behavior."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Dashboards · `docs/dashboards/`

> Human-facing specifications, catalogs, ownership expectations, and trust-boundary guidance for KFM dashboard surfaces. **This lane specifies and indexes; it does not run dashboards or create truth.**

<p>
  <img alt="Path: confirmed" src="https://img.shields.io/badge/path-CONFIRMED-1f6feb">
  <img alt="Placement: hold" src="https://img.shields.io/badge/placement-HOLD-b42318">
  <img alt="Specifications: 34 confirmed" src="https://img.shields.io/badge/specifications-34%20CONFIRMED-1a7f37">
  <img alt="Runtime: needs verification" src="https://img.shields.io/badge/runtime-NEEDS%20VERIFICATION-d4a72c">
  <img alt="Truth posture: cite or abstain" src="https://img.shields.io/badge/truth-cite--or--abstain-8250df">
  <img alt="Publication: none" src="https://img.shields.io/badge/publication-none-6e7781">
</p>

> [!IMPORTANT]
> **Existence, placement, specification, implementation, and publication are separate states.** The path and its current file inventory are **CONFIRMED** at the pinned repository snapshot. The parent `docs/` responsibility root is canonical under accepted [ADR-0029](../adr/ADR-0029-adopt-directory-governance-standard-v2.md). The nested `docs/dashboards/` lane is not listed in the adopted Directory Rules v2 canonical direct-child map, so its long-term placement remains **HOLD** rather than silently canonicalized.

> [!CAUTION]
> **A dashboard is a downstream carrier.** A green panel, trend line, SLO, trace, metric, log, report, badge, or screenshot does not substitute for an `EvidenceBundle`, validator result, `PolicyDecision`, `ReviewRecord`, `ReleaseManifest`, correction path, rollback target, or an authorized release decision.

> [!NOTE]
> This same-path documentation update preserves the existing lane while its disposition is reviewed. It does not authorize a new documentation root, move files, create runtime code, activate telemetry, release data, deploy a dashboard, or publish KFM knowledge.

## Quick jump

- [1. Scope](#1-scope)
- [2. Repo fit](#2-repo-fit)
- [3. Inputs](#3-inputs)
- [4. Exclusions](#4-exclusions-what-does-not-belong-here)
- [5. README contract](#5-readme-contract-directory-rules-15)
- [6. Current directory map](#6-directory-tree-proposed)
- [7. Architecture diagram](#7-architecture-diagram)
- [8. Dashboard catalog](#8-dashboard-catalog)
- [9. Indicator catalog](#9-indicator-catalog-atlas-v11-ch-2411)
- [10. Quickstart](#10-quickstart--authoring-a-dashboard-spec)
- [Validation and acceptance](#validation-and-acceptance)
- [11. Task list and open questions](#11-task-list--open-questions)
- [12. FAQ](#12-faq)
- [13. Related docs](#13-related-docs)
- [14. Appendix](#14-appendix)

---

## 1. Scope

`docs/dashboards/` is an existing human-documentation lane for four related specification classes:

1. **Governance-health specifications** — how stewards should inspect evidence integrity, release/correction/rollback posture, sensitivity and rights, AI surfaces, and documentation drift.
2. **Operational specifications** — how maintainers should inspect feed freshness, SLOs, geospatial quality, and artifact reproducibility.
3. **Domain specifications** — domain-facing roll-ups that preserve the owning domain's evidence, sensitivity, source-role, release, and correction boundaries.
4. **Observability specifications** — telemetry substrate and internal system-health views, including traces, metrics, logs, lineage signals, service health, and validator-orchestrator health.

The lane also contains two indexes:

- [`DASHBOARD_CATALOG.md`](DASHBOARD_CATALOG.md) — current repository inventory and cross-lane spec index.
- [`INDICATOR_CATALOG.md`](INDICATOR_CATALOG.md) — human-readable governance-health indicator mirror and dashboard mapping.

### Current inventory

The inventory below is **CONFIRMED** from the four complete subtree listings at the pinned base. Counts exclude category READMEs and the two catalogs unless stated otherwise.

| Category | Current child lane | Specification files | Current evidence posture |
|---|---|---:|---|
| Governance | [`governance/`](governance/) | 5 | File presence **CONFIRMED**; runtime **NEEDS VERIFICATION** |
| Operational | [`operational/`](operational/) | 4 | File presence **CONFIRMED**; runtime **NEEDS VERIFICATION** |
| Domain | [`domain/`](domain/) | 14 | Thirteen top-level domain specs plus one air sub-spec; runtime **NEEDS VERIFICATION** |
| Observability | [`observability/`](observability/) | 11 | File presence **CONFIRMED**; naming conflict and runtime remain unresolved |
| **Total** | Four child lanes | **34** | Specification presence only |

Together with this README, two catalogs, and four category READMEs, the subtree contains **41 Markdown files** at the evidence snapshot.

[↑ Back to top](#top)

---

## 2. Repo fit

### 2.1 Authority and placement

| Surface | Current role | Status | Consequence |
|---|---|---|---|
| [`docs/`](../README.md) | Canonical human-readable governance and explanation root | **CONFIRMED** under accepted ADR-0029 | Dashboard specifications inherit the `docs/` trust and exposure boundary. |
| [`docs/dashboards/`](./) | Existing nested lane for dashboard specifications and catalogs | **CONFIRMED path / HOLD placement** | Preserve the existing path; do not treat presence as admission to the canonical direct-child map. |
| [`control_plane/`](../../control_plane/README.md) | Machine-readable governance projections and indexes | **CONFIRMED root** | A future machine dashboard registry belongs there only if governed and derived; this README cannot create it. |
| [`apps/review-console/`](../../apps/review-console/README.md) | Proposed role-gated steward review application boundary | **CONFIRMED README / runtime NEEDS VERIFICATION** | Specs may point to this app, but they must not claim routes, panels, or deployed behavior without evidence. |
| External observability tooling | Collectors, stores, panels, queries, and alerts | **UNKNOWN / implementation-specific** | Runtime artifacts do not belong in `docs/`; credentials and private endpoints are never documented here. |

Accepted [ADR-0029](../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts the exact Directory Rules v2 bytes at [`docs/doctrine/directory-rules.md`](../doctrine/directory-rules.md). Those rules define `docs/` as the human explanation surface and require a `BOUNDARY_COMPACT` README where a nested lane changes ownership, exposure, mutation, or authority. They do **not** automatically admit every current direct child as canonical.

### 2.2 Current maturity model

| Level | Meaning | Dashboard-lane posture |
|---|---|---|
| **Tracked** | Path, indexes, category lanes, and spec files exist | **CONFIRMED** |
| **Documented** | Lane boundaries and spec intent are written | **CONFIRMED**, with stale and conflicting statements being reconciled here |
| **Indexed** | Specs are represented in the current dashboard catalog | **CONFIRMED for 34 rows as stated by the catalog; machine parity check NEEDS VERIFICATION** |
| **Implemented** | Queries, panels, adapters, access controls, and stores exist | **NEEDS VERIFICATION** |
| **Observed** | Current telemetry or records feed a running surface | **UNKNOWN / NEEDS VERIFICATION** |
| **Enforced** | Validators or policy fail closed on dashboard contracts | **NEEDS VERIFICATION** |
| **Released** | A governed public or steward release exists with correction and rollback support | **UNKNOWN; no release is asserted by this README** |

[↑ Back to top](#top)

---

## 3. Inputs

A dashboard specification may describe how a running surface consumes or summarizes:

- `ValidationReport`, `ReviewRecord`, `PolicyDecision`, `ReleaseManifest`, `CorrectionNotice`, `WithdrawalNotice`, `RollbackCard`, `AIReceipt`, `RedactionReceipt`, `RepresentationReceipt`, and related governed records **when those families and instances are verified**;
- source identity, role, cadence, freshness, and stale-state metadata from governed registries;
- bounded telemetry signals such as trace coverage, run duration, exit-code distribution, service latency, and contract-health outcomes;
- finite negative states such as `MISSING_EVIDENCE`, `SOURCE_STALE`, `DENIED_BY_POLICY`, `RELEASE_WITHDRAWN`, `RUNTIME_ERROR`, and `REVIEW_PENDING` when defined by the owning runtime or contract;
- current repository and CI signals when the spec clearly distinguishes repository health from KFM truth or release state.

Inputs remain owned by their source families. This lane records presentation and review intent; it does not store, rewrite, approve, or promote the underlying records.

[↑ Back to top](#top)

---

## 4. Exclusions — what does not belong here

| Prohibited content or responsibility | Owning home or disposition | Why |
|---|---|---|
| Running dashboard code, panel JSON, queries, adapters, or UI state | `apps/`, `packages/`, `runtime/`, `infra/`, or an externally governed observability repository selected by execution role | Implementation is not documentation. |
| Telemetry series, traces, logs, profiles, or alert history | Governed runtime/observability storage | `docs/` is public repository-facing and not an operational datastore. |
| Generated review or release reports | The verified report lane or external generated artifact store | Reports are outputs; specs describe recurring surfaces. |
| Machine-readable governance registers | `control_plane/` | A prose catalog is not a machine authority. |
| Semantic contracts, machine schemas, or policy rule source | `contracts/`, `schemas/`, `policy/` | Meaning, shape, and admissibility remain separate. |
| Receipts, proofs, EvidenceBundles, catalog records, or lifecycle data | The correct `data/` accountability or lifecycle lane | Dashboards report on trust objects; they do not host them. |
| Promotion, release, correction, withdrawal, rollback, or signature decisions | `release/` | A dashboard cannot authorize the transition it visualizes. |
| Secrets, credentials, private endpoints, signed URLs, or protected payloads | Never committed; use governed secret and access systems | Public documentation is an exposure boundary. |
| Exact sensitive locations, living-person private data, genomic material, restricted archaeology, rare-species locations, or critical-infrastructure detail | Redact, generalize, quarantine, stage, delay, abstain, or deny according to policy | A chart, tooltip, label, log line, or metric dimension can create a side channel. |

> [!WARNING]
> Client-side hiding, aggregation labels, dashboard permissions, or a private-looking panel are not substitutes for upstream policy and public-safe transformation.

[↑ Back to top](#top)

---

<a id="5-readme-contract-directory-rules-15"></a>

## 5. README contract (Directory Rules v2 §16)

This lane uses the adopted `BOUNDARY_COMPACT` profile.

| Required field | Current contract |
|---|---|
| **Purpose and inherited parent** | Human-readable dashboard specifications and indexes under the canonical `docs/` explanation root. |
| **Local owner and scope** | GitHub review currently routes to `@bartytime4life`; dashboard, observability, domain, release, policy, and independent-review stewardship remain **NEEDS VERIFICATION**. Scope is `docs/dashboards/` only. |
| **Belongs / prohibited** | Sections [1](#1-scope) and [4](#4-exclusions-what-does-not-belong-here) are normative for this README's documentation boundary. |
| **Inputs / outputs** | Inputs are references to governed records and telemetry contracts. Outputs are Markdown specifications, two human indexes, and ownership/review guidance. |
| **Exposure** | Repository-facing; no secrets, restricted payloads, unsafe precision, or private operational details. |
| **Mutation and retention** | Reviewed, versioned Git history. Current files remain editable documents; generated or mirrored derivatives must declare their source and edit policy. |
| **Validation** | Metadata, one-H1, heading/anchor, link, inventory/catalog parity, sensitive-content, generated-receipt, and diff-hygiene checks. Runtime checks are separate. |
| **Related authorities** | `docs/`, contracts, schemas, policy, tests, data accountability lanes, release, runtime/app surfaces, and category READMEs. |
| **Status and open verification** | Existing path and inventory **CONFIRMED**; placement **HOLD**; runtime, telemetry, enforcement, and release **NEEDS VERIFICATION** or **UNKNOWN**. |

A child category README owns deeper lane detail. This parent shows only direct children, as required by Directory Rules v2.

[↑ Back to top](#top)

---

<a id="6-directory-tree-proposed"></a>

## 6. Current directory map

The direct-child map below is **CONFIRMED** from the pinned repository tree. Counts summarize deeper specs without duplicating child-README inventories.

```text
docs/dashboards/
├── README.md                    # this boundary contract
├── DASHBOARD_CATALOG.md         # current cross-lane specification index
├── INDICATOR_CATALOG.md         # governance-health indicator mirror
├── governance/                  # README + 5 governance-health specs
├── operational/                 # README + 4 feed/artifact/QC specs
├── domain/                      # README + 14 domain and air specs
└── observability/               # README + 11 telemetry/system-health specs
```

### Current conflict to preserve

`observability/` contains both `OPENTELEMETRY_STACK.md` and `opentelemetry-stack.md`. Their simultaneous presence is **CONFIRMED**; their identity, precedence, consumer set, and migration disposition are **NEEDS VERIFICATION**. Do not delete, merge, rename, or declare either canonical from this README.

[↑ Back to top](#top)

---

## 7. Architecture diagram

Solid arrows show current documentation relationships. Dashed arrows show implementation relationships that require separate evidence.

```mermaid
flowchart LR
  ATLAS["Atlas and source lineage"] --> IC["INDICATOR_CATALOG.md\n23 indicator mirror"]
  TREE["Current repository tree"] --> DC["DASHBOARD_CATALOG.md\n34 spec index"]
  IC --> ROOT["docs/dashboards/README.md\nboundary contract"]
  DC --> ROOT
  ROOT --> GOV["governance/ specs"]
  ROOT --> OPS["operational/ specs"]
  ROOT --> DOM["domain/ specs"]
  ROOT --> OBS["observability/ specs"]

  RECORDS["Evidence · receipts · policy · review · release records"] -. "reported by" .-> RUNTIME["running dashboard surface\nNEEDS VERIFICATION"]
  TELEMETRY["traces · metrics · logs · lineage signals"] -. "carried by" .-> RUNTIME
  ROOT -. "documents intent and links" .-> RUNTIME
  RUNTIME -. "does not authorize" .-> RELEASE["governed release / correction / rollback"]

  classDef docs fill:#ddf4ff,stroke:#0969da,color:#24292f;
  classDef runtime fill:#fff8c5,stroke:#9a6700,color:#24292f;
  classDef trust fill:#ffebe9,stroke:#cf222e,color:#24292f;
  class ROOT,IC,DC,GOV,OPS,DOM,OBS docs;
  class RUNTIME,TELEMETRY runtime;
  class RECORDS,RELEASE trust;
```

A specification can define the intended panel, indicator, source record, negative state, owner, and response path. Only implementation evidence can establish that those behaviors run.

[↑ Back to top](#top)

---

## 8. Dashboard catalog

[`DASHBOARD_CATALOG.md`](DASHBOARD_CATALOG.md) is the current repository index for specification files in this lane. It records 34 specs and keeps file presence separate from running-surface status.

| Category | Category contract | Current specs | Inventory posture |
|---|---|---:|---|
| Governance | [`governance/README.md`](governance/README.md) | 5 | **CONFIRMED** files |
| Operational | [`operational/README.md`](operational/README.md) | 4 | **CONFIRMED** files |
| Domain | [`domain/README.md`](domain/README.md) | 14 | **CONFIRMED** files |
| Observability | [`observability/README.md`](observability/README.md) | 11 | **CONFIRMED** files; duplicate-name conflict open |

### Catalog rules

- Every dashboard spec should appear in the catalog and its nearest category README.
- A catalog row confirms an indexed specification, not a running panel or released capability.
- `implementation_status` may become `CONFIRMED` only with pinned implementation plus representative test, workflow, emitted telemetry, dashboard artifact, or runtime evidence appropriate to the claim.
- Missing or extra rows are catalog drift; do not silently delete files to make the count match.
- The catalog cannot resolve the parent lane's placement hold or the observability filename conflict by declaration.

[↑ Back to top](#top)

---

<a id="9-indicator-catalog-atlas-v11-ch-2411"></a>

## 9. Indicator catalog

[`INDICATOR_CATALOG.md`](INDICATOR_CATALOG.md) mirrors **23 governance-health indicators** in five categories. It is an authoring and review aid, not doctrine, policy, metric storage, or enforcement.

| Indicator family | Rows | Example focus |
|---|---:|---|
| Evidence and source integrity | 5 | EvidenceRef resolution, cite-or-abstain compliance, source-role and stale-source posture |
| Release, correction, and rollback | 5 | Rollback-target coverage, correction timing, derivative invalidation, supersession lineage |
| Sensitivity and rights | 5 | Fail-closed behavior, redaction coverage, rights-change response, side-channel review |
| AI surface health | 4 | AIReceipt presence, ABSTAIN/DENY distributions, synthetic-claim audit |
| Documentation and drift | 4 | ADR completeness, drift backlog, README coverage, lineage clarity |
| **Total** | **23** | Reported posture only |

> [!TIP]
> **Non-collapse rule:** the dashboard reports; the owning validator or policy enforces; the governing records and EvidenceBundles carry support; the authorized release process decides publication.

If the indicator mirror disagrees with its upstream atlas or another accepted authority, record the discrepancy and reconcile through the owning documentation/governance process. Do not let a mirror silently amend doctrine.

[↑ Back to top](#top)

---

<a id="10-quickstart--authoring-a-dashboard-spec"></a>

## 10. Quickstart — authoring a dashboard spec

1. **Pin the repository state.** Record the base commit, target lane, current catalog row set, and any overlapping pull request.
2. **Read the boundary.** Read this README, the category README, [`docs/README.md`](../README.md), accepted [ADR-0029](../adr/ADR-0029-adopt-directory-governance-standard-v2.md), and the adopted [Directory Rules](../doctrine/directory-rules.md).
3. **Use an existing category.** Add to `governance/`, `operational/`, `domain/`, or `observability/` only when its category contract fits. A new category or direct child requires placement review before creation.
4. **Name the source and limits.** Identify the indicator, source card, contract, runtime anchor, or repository tool that motivates the spec. Mark unsupported implementation claims `NEEDS VERIFICATION` or `UNKNOWN`.
5. **Keep one responsibility.** Describe the human-facing dashboard contract. Put code, schema, policy, telemetry storage, trust objects, and release decisions in their owning roots.
6. **Define finite states.** Include normal, stale, missing, denied, withdrawn, review-pending, and runtime-error behavior where relevant. Do not convert absence into a healthy zero.
7. **Protect sensitive dimensions.** Prohibit raw labels, exact coordinates, identifiers, log content, or query dimensions that can reconstruct restricted information.
8. **Update the indexes.** Add or reconcile the row in [`DASHBOARD_CATALOG.md`](DASHBOARD_CATALOG.md), the nearest category README, and [`INDICATOR_CATALOG.md`](INDICATOR_CATALOG.md) only when indicator coverage changes.
9. **Validate the documentation packet.** Check metadata, one H1, anchors, links, tree/catalog parity, sensitive content, diff hygiene, and the generated receipt.
10. **Stop at reviewable repository state.** A specification pull request does not deploy, release, publish, or approve a dashboard.

[↑ Back to top](#top)

---

## Validation and acceptance

### Documentation checks

For this lane, a focused change should verify:

- one `KFM_META_BLOCK_V2` and one H1 per changed document;
- balanced Markdown fences, HTML blocks, tables, and Mermaid fences;
- valid heading hierarchy and preserved legacy anchors where headings changed;
- all added repository-relative links and case-sensitive paths;
- direct-child tree counts against the pinned repository tree;
- catalog and category-README coverage for added or removed specs;
- no placeholder claims presented as current runtime behavior;
- no secrets, restricted payloads, unsafe precision, or sensitive side channels;
- final newline and diff hygiene;
- generated-receipt schema and artifact-hash integrity.

Useful repository checks include:

```bash
python tools/validators/validate_generated_receipt.py \
  data/receipts/generated/<receipt>.json --repo-root .

git diff --check
```

Run broader repository-native validation when dependencies are available and the changed-area workflow requires it. Report hosted checks separately from local authoring checks.

### Acceptance interpretation

| Criterion | Passing evidence |
|---|---|
| Same-path modernization | Only this README and its generated receipt change unless a direct dependency is explicitly admitted. |
| Accurate current inventory | Four subtree counts reconcile to 34 specs and seven navigation/catalog Markdown files. |
| Placement truth | Existing path is confirmed; canonical nested-lane status remains `HOLD`. |
| Trust boundary | No runtime, evidence, policy, release, or publication authority is transferred into docs. |
| Runtime claims | No running-dashboard claim is upgraded without implementation evidence. |
| Reversibility | Previous README blob and a focused revert remain sufficient rollback targets. |

[↑ Back to top](#top)

---

<a id="11-task-list--open-questions"></a>

## 11. Task list & open questions

- [ ] **DASH-OQ-01 — Placement disposition.** Decide whether `docs/dashboards/` should become an admitted canonical docs lane, remain a bounded current-path exception, migrate into an existing canonical lane, or be split by responsibility. This README records `HOLD`; it does not decide.
- [ ] **DASH-OQ-02 — Observability duplicate identity.** Reconcile `observability/OPENTELEMETRY_STACK.md` and `observability/opentelemetry-stack.md` only after comparing content, IDs, inbound links, writers, consumers, and migration requirements.
- [ ] **DASH-OQ-03 — Steward assignments.** Establish dashboard, observability, category, domain, policy, release, and independent-review roles beyond the confirmed GitHub routing identity.
- [ ] **DASH-OQ-04 — Runtime mapping.** Verify which specifications correspond to code, queries, panels, telemetry stores, alert rules, review-console features, or deployed surfaces.
- [ ] **DASH-OQ-05 — Catalog parity enforcement.** Add or identify a repository-owned check that compares the complete subtree with `DASHBOARD_CATALOG.md` and rejects missing, duplicate, or unclassified specs without treating the catalog as runtime authority.
- [ ] **DASH-OQ-06 — Indicator lineage.** Verify the operative atlas/source identity for the 23-row mirror and establish a bounded mirror-synchronization process.
- [ ] **DASH-OQ-07 — Negative-state vocabulary.** Reconcile reason codes and UI labels with the owning contracts, schemas, policy, Explorer, Review Console, and runtime envelopes.
- [ ] **DASH-OQ-08 — Sensitive telemetry profile.** Define and test cardinality, label, coordinate, identifier, prompt, and log-redaction rules before production telemetry can feed dashboards.
- [ ] **DASH-OQ-09 — Review and correction workflow.** Define who investigates a bad signal, how false positives are corrected, how dashboard definitions are versioned, and how withdrawn releases propagate to panels and caches.

[↑ Back to top](#top)

---

## 12. FAQ

### Why keep dashboard specifications separate from generated reports?

The current lane describes recurring surfaces, inputs, owners, finite states, and healthy posture. Generated reports are point-in-time outputs. Their final placement and relationship remain subject to the dashboard lane's placement disposition; this README does not create a new report authority.

### Are running dashboards stored here?

No. Running code, queries, dashboards-as-code, collector configuration, telemetry stores, and alerting belong in execution or infrastructure surfaces selected by responsibility. This lane may link to them after verification.

### Does a green dashboard prove KFM truth or release readiness?

No. It is one review signal. Evidence, policy, validation, review, release, correction, and rollback remain independently governed.

### Is `docs/dashboards/` canonical?

The path is **CONFIRMED** and the parent `docs/` root is canonical. The nested lane is omitted from the adopted canonical direct-child map, so this README records placement as **HOLD**. Presence alone does not settle admission.

### Who owns this lane?

`@bartytime4life` is the confirmed GitHub review route through the default CODEOWNERS rule. A complete dashboard and observability stewardship assignment, including independent review where risk warrants it, remains **NEEDS VERIFICATION**.

### May a new domain or category be invented here?

No. Use registered domain and category identities already recognized by the repository. A new category, scope, or authority boundary requires evidence and placement review; it is not created by adding a Markdown file.

[↑ Back to top](#top)

---

## 13. Related docs

| Surface | Relationship |
|---|---|
| [`docs/README.md`](../README.md) | Parent human-documentation authority and exposure contract |
| [`Directory Rules v2`](../doctrine/directory-rules.md) | Adopted placement and README-profile law through ADR-0029 |
| [`ADR-0029`](../adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Accepted adoption decision and migration boundary |
| [`Dashboard Catalog`](DASHBOARD_CATALOG.md) | Current cross-lane specification index |
| [`Indicator Catalog`](INDICATOR_CATALOG.md) | Current 23-row governance-health mirror |
| [`Governance lane`](governance/README.md) | Governance-health specification contract |
| [`Operational lane`](operational/README.md) | Feed, artifact, and geospatial-QC specification contract |
| [`Domain lane`](domain/README.md) | Per-domain dashboard specification contract |
| [`Observability lane`](observability/README.md) | Telemetry substrate and system-health specification contract |
| [`Domains Culmination Atlas v1.1`](../atlases/KFM_Domains_Culmination_Atlas_v1_1.md) | Current repository atlas path referenced by the indicator lineage; authority and mirror sync still require verification |
| [`Drift Register`](../registers/DRIFT_REGISTER.md) | Human-readable placement and authority drift tracking |
| [`Verification Backlog`](../registers/VERIFICATION_BACKLOG.md) | Concrete unresolved checks |
| [`Review Console README`](../../apps/review-console/README.md) | Proposed role-gated review application boundary; runtime remains bounded |
| [`Root Registry`](../../control_plane/root_registry.yaml) | Machine projection of adopted top-level root classes; does not admit nested dashboard placement |
| [`Generated receipts`](../../data/receipts/generated/README.md) | AI-authored work provenance and validation guidance |

[↑ Back to top](#top)

---

## 14. Appendix

### A. Evidence ledger

| Evidence | What it establishes | What it does not establish |
|---|---|---|
| Target README prior blob | Stable prior bytes and rollback target | Current correctness or canonical placement |
| Four dashboard subtree SHAs | Exact current paths and spec counts at the base | Runtime behavior, telemetry emission, or catalog parity after the base |
| `DASHBOARD_CATALOG.md` | Current repository inventory claim and spec metadata | Running dashboards or release status |
| `INDICATOR_CATALOG.md` | Current 23-row human mirror | Enforcement or adopted threshold policy |
| Accepted ADR-0029 and Directory Rules blob | Current placement authority and README profiles | Automatic admission of `docs/dashboards/` |
| `docs/README.md` | Parent root contract and current/noncanonical lane posture | A nested-lane disposition |
| CODEOWNERS | GitHub review routing to `@bartytime4life` | Stewardship assignment, approval, independent review, or release authority |

### B. No-loss reconciliation

This modernization preserves the prior document's substantive duties:

- dashboard specifications remain separate from running implementations;
- indicator catalogs remain separate from enforcement;
- governance, operational, domain, and observability categories remain visible;
- evidence, receipts, policy, review, release, correction, and rollback stay outside docs authority;
- sensitive material remains fail closed;
- the authoring workflow, validation burden, open questions, FAQ, and related-doc navigation remain present;
- stable legacy section anchors are retained for the README-contract, directory-tree, indicator-catalog, and open-question sections.

It removes or corrects stale claims that the repository was not mounted, that the directory tree was merely proposed, that only 24 specs existed, that Directory Rules v1 governed placement, and that the old atlas filename was current.

### C. Rollback

Before merge, close the draft pull request and delete its scoped branch through normal repository controls. After an authorized merge, revert the focused documentation and generated-receipt commit, restore prior README blob `3749fc0099443c3c8b024357e0f1694253ff735e`, and rerun the same documentation and receipt checks. No runtime, telemetry store, policy, lifecycle data, release, deployment, cache, or public artifact requires reversal because this change alters documentation and provenance only.

---

**Current edition:** v1.0 · **Evidence review:** 2026-08-14 · **GitHub review route:** `@bartytime4life` · **Placement:** `HOLD` · **Runtime:** `NEEDS VERIFICATION`

[↑ Back to top](#top)
