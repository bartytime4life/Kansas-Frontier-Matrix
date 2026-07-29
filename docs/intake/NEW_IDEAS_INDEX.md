<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS-VERIFICATION
title: New Ideas Index
type: standard
version: v1.4
status: draft; repository-grounded; intake-only
owners: OWNER_TBD
created: 2026-05-16
updated: 2026-07-29
policy_label: public
related: [docs/doctrine/directory-rules.md, docs/intake/README.md, docs/intake/new-ideas-register.md, docs/intake/exploratory/new-ideas-4-16-source-map.md, docs/intake/exploratory/new-ideas-4-30-source-map.md, docs/intake/exploratory/new-ideas-5-source-map.md, docs/registers/DRIFT_REGISTER.md, docs/registers/VERIFICATION_BACKLOG.md]
tags: [kfm, intake, new-ideas, documentation-control, governance]
notes: [Repository presence and sibling register verified at remote main 3a9ebaf842e4dfe65deda95be0d15d6af62723eb; New Ideas 4-16-26, New Ideas 4-30-26, and New Ideas 5 source identities and bounded triage maps added; source packets remain EXPLORATORY until triaged and promoted; no packet is promoted by this file.]
[/KFM_META_BLOCK_V2] -->

# New Ideas Index

A governed intake index for dated KFM “New Ideas” packets, preserving useful design pressure without turning exploratory notes into canon or implementation proof.

> [!IMPORTANT]
> **Status:** draft / repository-grounded / intake-only
> **Path:** `docs/intake/NEW_IDEAS_INDEX.md`  
> **Owner:** `OWNER_TBD`  
> **Truth posture:** CONFIRMED repository path and sibling intake surfaces at remote `main@3a9ebaf842e4dfe65deda95be0d15d6af62723eb` / EXPLORATORY packet content / no promotion authority

> [!NOTE]
> This file is an intake control surface. It records packet presence, themes, routing pressure, blockers, and next verification moves. It does **not** prove that proposed paths, tools, schemas, policies, workflows, or services exist in the repository.

## Quick navigation

- [Purpose](#purpose)
- [Repo fit](#repo-fit)
- [Operating law](#operating-law)
- [Intake record requirements](#intake-record-requirements)
- [Current packet register](#current-packet-register)
- [Intake taxonomy](#intake-taxonomy)
- [Intake statuses](#intake-statuses)
- [Promotion criteria](#promotion-criteria)
- [Maintenance workflow](#maintenance-workflow)
- [Verification checklist](#verification-checklist)
- [Rollback](#rollback)
- [Appendix: triage record template](#appendix-triage-record-template)
- [Appendix: packet cards](#appendix-packet-cards)

## Purpose

The “New Ideas” stream is a high-value source of implementation pressure, source-refresh signals, policy sketches, object-family proposals, and UI/runtime hardening ideas. It is also easy to overread.

This index keeps that stream useful by recording each packet as intake material first, then routing specific ideas toward a governed destination only after evidence, ownership, rights, sensitivity, validation, and rollback requirements are clear.

This file does **not** make any packet authoritative. It does **not** prove that proposed paths, tools, policies, schemas, workflows, or services exist in the repository. It is an intake control surface.

## Repo fit

| Field | Value |
| --- | --- |
| Intended home | `docs/intake/NEW_IDEAS_INDEX.md` |
| Placement status | CONFIRMED present at `main@3a9ebaf842e4dfe65deda95be0d15d6af62723eb`; content remains draft and non-authoritative. |
| Responsibility root | `docs/` — documentation control, human-readable intake navigation, and governance orientation. |
| Directory Rules basis | A human-readable intake index belongs under `docs/`; downstream implementation artifacts stay under their owning roots. Domain names appear as segments inside responsibility roots, not as new repo roots. |
| Intake lane role | Capture and classify exploratory packets before promotion. |
| Upstream doctrine | Directory Rules, documentation architecture passes, KFM truth posture, trust membrane, lifecycle law. |
| Index/register relationship | Both this file and `docs/intake/new-ideas-register.md` are CONFIRMED present. This file is the packet landing index; the sibling register carries detailed triage records. Neither may evolve into packet authority. |

### Candidate downstream homes

Use destination roots by responsibility, not by topic convenience.

| Candidate output | Owning root | Placement rule |
| --- | --- | --- |
| Doctrine or governance wording | `docs/doctrine/` | Human-readable doctrine; path remains PROPOSED until repo inspection. |
| Source notes and source authority summaries | `docs/sources/` and `data/registry/` | Docs explain source posture; registry records source identity, rights, roles, and access constraints. |
| Domain narrative and lane architecture | `docs/domains/<domain>/` | Domain belongs as a segment inside `docs/`, not as a new root. |
| Object meaning | `contracts/` | Use for semantic contract language when verified. |
| Machine shape | `schemas/contracts/v1/` | Use for JSON Schema / machine-readable shape after schema-home verification. |
| Allow / deny / restrict / abstain logic | `policy/` | Policy rules must not live in this index. |
| Pipeline logic and watcher flow | `pipelines/` or `pipeline_specs/` | Executable logic and declarative specs remain separate. |
| Validators, probes, generators, builders | `tools/` | Repo-wide tooling belongs under tools after convention checks. |
| Tests and fixtures | `tests/`, `fixtures/` | Proof of enforceability and sample data are not intake notes. |
| Release decisions, manifests, rollback, corrections | `release/` | Publication remains a governed state transition. |

### Accepted inputs

This index accepts:

- dated “New Ideas” packets, notes, PDFs, docs, or text files;
- packet summaries and one-sentence intake notes;
- source IDs, hashes, dates, owners, and status labels;
- triage category assignments;
- links to candidate canonical destinations;
- verification backlog items that prevent promotion.

### Exclusions

This index must not store:

- canonical policy rules — use `policy/` and policy docs;
- schema definitions — use the repo’s accepted schema home, defaulting to `schemas/contracts/v1/` only after verification;
- contract semantics — use `contracts/` or accepted contract docs;
- source registry records — use `data/registry/` and source descriptors;
- emitted receipts, proofs, manifests, or release objects — use the appropriate lifecycle/proof homes;
- sensitive exact locations, private source credentials, raw data, unpublished EvidenceBundle contents, or unreviewed public-release claims.

## Operating law

New Ideas packets are **EXPLORATORY** until a governed decision changes their status. Duplicates and repeated suggestions can corroborate direction, but they do not become independent authority votes.

```mermaid
flowchart LR
    A[Captured packet] --> B[Triage]
    B --> C{Disposition}
    C --> D[Candidate canonical]
    C --> E[Corroborative]
    C --> F[Deferred]
    C --> G[Archived exploratory]
    C --> H[Rejected]
    D --> I[Owner + destination + validation]
    I --> J[Promotion decision]
    J --> K[Canonical doc / schema / policy / tool path]
    J --> L[ABSTAIN / DENY / rollback]
```

A packet may sharpen a future build, but it must not bypass KFM’s trust membrane:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Publication remains a governed state transition. Map tiles, PMTiles, COGs, graph projections, vector indexes, generated summaries, Focus Mode answers, screenshots, and Story Nodes remain downstream carriers, not sovereign truth.

### Non-authority rule

A row in this file means:

```text
packet observed -> theme captured -> routing pressure recorded -> blockers named
```

It does **not** mean:

```text
implementation exists -> policy is active -> schema is canonical -> public release is allowed
```

## Intake record requirements

Each packet should be tracked with enough information to support later review without forcing a promotion decision.

| Required field | Why it matters | Placeholder when unknown |
| --- | --- | --- |
| Intake ID | Keeps packet identity stable across triage passes. | `NIP-YYYY-MM-DD[-suffix]` |
| Source packet | Allows retrieval of the original packet. | `SOURCE_PACKET_TBD` |
| Date signal | Distinguishes filename dates, creation dates, and content dates. | `DATE_SIGNAL_TBD` |
| Source ID / hash | Supports deduplication and source ledger linkage. | `SOURCE_ID_TBD`; `HASH_TBD` |
| Current status | Prevents exploratory content from masquerading as canon. | `CAPTURED / EXPLORATORY` |
| Main themes | Preserves design pressure without copying full packet contents. | `THEMES_TBD` |
| Candidate destinations | Identifies routing pressure while keeping paths PROPOSED. | `PATH_TBD_AFTER_REPO_INSPECTION` |
| Blocking checks | Makes rights, sensitivity, source-role, owner, and repo gaps visible. | `NEEDS VERIFICATION: <specific check>` |
| Decision record | Links later promotion, rejection, or archive action. | `DECISION_RECORD_TBD` |

## Current packet register

This table records only the packet sources visible or directly retrieved in this session. It is not a complete historical inventory.

| Intake ID | Source packet | Date signal | Current status | Main themes | Candidate destinations | Blocking checks |
| --- | --- | --- | --- | --- | --- | --- |
| `NIP-2026-05-08` | `New Ideas 5-8-26.pdf` | Filename date | CAPTURED / EXPLORATORY | Ecology tile gating; MAIAC AOD, FIRMS, SMAP, AirNow, Mesonet; watcher `DecisionEnvelope`; `RunReceipt`; PMTiles sidecars; MapLibre/Cesium verification; no-network proof slice; DSSE/cosign; policy hooks. | `docs/domains/ecology/`, `docs/sources/`, `policy/ecology/`, `schemas/contracts/v1/governance/`, `tools/ci/probes/`, `tools/smoke/`, `release/` after verification. | Verify source rights, API/key requirements, external product facts, Mesonet consent posture, thresholds as policy not science absolutes, and repo path conventions. |
| `NIP-2026-05-10` | `New Ideas 5-10-26.pdf` | Filename date | CAPTURED / EXPLORATORY | PMTiles operational hardening; versioned artifacts; sidecar + Bao/BLAKE3 proofs; DSSE/cosign/Rekor; OCI/ORAS publication; fail-closed CI gate; MapLibre performance testing; automation starter pack; promotion/rollback rehearsal. | `tools/attest/`, `tools/validators/`, `schemas/contracts/v1/artifacts/`, `.github/workflows/`, `release/`, `docs/architecture/map/`, `docs/runbooks/` after repo verification. | Verify current tool versions and licenses, package availability, OCI/referrer support, schema-home authority, workflow conventions, public-safe artifact exposure, and rollback evidence. |
| `NIP-2026-04-16-governed-baselines` | `New Ideas 4-16-26(1).pdf` | Source date confirmed by filename and PDF title | TRIAGED / EXPLORATORY | Fauna/soil governed ingest; vegetation/hydrology baselines; air-quality anomaly lifecycle; consent/revocation; MapLibre time buckets; PMTiles verification; STAC conformance; historical post-office/trail networks. | Detailed routing in [`exploratory/new-ideas-4-16-source-map.md`](exploratory/new-ideas-4-16-source-map.md); ten gap-fill triads in [`../kfm_full_atlas_seed_cards.md`](../kfm_full_atlas_seed_cards.md); downstream artifacts remain candidate-only. | Do not copy packet paths or code. Reuse existing domain lanes; resolve canonical hash profiles, materiality, baseline/event semantics, consent placement, STAC profile, source authority/rights, and exact bounded authorization per candidate. |
| `NIP-2026-04-30-retrieval-offline-trust` | `New Ideas 4-30-26.pdf` | Source date confirmed by filename and PDF title | TRIAGED / EXPLORATORY | USDA PLANTS, eBird, GBIF, soil/air fusion, source terms, query provenance, sampling/non-detection, PMTiles/offline delivery, verified rendering, STAC/validators, vegetation confounders, and source cadence/latency. | Detailed routing in [`exploratory/new-ideas-4-30-source-map.md`](exploratory/new-ideas-4-30-source-map.md); eleven gap-fill triads in [`../kfm_full_atlas_seed_cards.md`](../kfm_full_atlas_seed_cards.md); downstream artifacts remain candidate-only. | Do not copy packet code, paths, credentials, thresholds, cloud examples, or dated external claims. Resolve retrieval, rights, distribution, support, latency, transfer, offline-trust, and renderer-budget semantics before implementation. |
| `NIP-2026-07-29-new-ideas-5` | `New Ideas 5.pdf` | Capture date only; source date `NEEDS VERIFICATION` | TRIAGED / EXPLORATORY | Dual-renderer Story Node; STAC/catalog QA; signing and provenance; NWIS watcher; pipeline resilience; atmosphere fusion; soil/geology conversion; reproducible models; graph/AI retrieval; license automation. | Detailed routing in [`exploratory/new-ideas-5-source-map.md`](exploratory/new-ideas-5-source-map.md); downstream candidates remain under existing ADR, contract, schema, policy, tool, pipeline, source, domain, data, and release roots. | Do not copy packet paths or code. Resolve renderer ADR, catalog profile/placeholder, external source facts, rights, dependency approval, contract/policy/test consequences, and exact bounded authorization per candidate. |

### Known lineage backlog to inventory

Prior source ledgers and documentation architecture passes refer to earlier New Ideas packets from February, March, and April 2026. Those packets should be inventoried in a separate pass before this file is treated as complete.

| Family | Status | Why it is not fully indexed here | Required next step |
| --- | --- | --- | --- |
| February 2026 New Ideas docs | NEEDS VERIFICATION | Some related files were discoverable as prior uploads, but not all are present in the visible `/mnt/data` workspace. | Confirm packet filenames, hashes, dates, duplicates, source IDs, and promotion status. |
| March 2026 New Ideas packets | NEEDS VERIFICATION | Prior reports list multiple March packets as EXPLORATORY lineage. | Inventory packets and add one row per dated source. |
| April 2026 New Ideas packets | PARTIAL | `New Ideas 4-16-26(1).pdf` and `New Ideas 4-30-26.pdf` are identity-pinned and triaged; other April packets and Part 2 variants remain outside these rows. | Inventory the remaining April packets, de-duplicate them against both April source maps, and preserve one row per distinct source. |

## Intake taxonomy

Use the narrowest truthful category. A packet can produce multiple extracted ideas, each with its own category.

| Intake category | Definition | Typical examples | Default destination after triage |
| --- | --- | --- | --- |
| Doctrine candidate | Refines governing law, terminology, or truth posture. | Better cite-or-abstain wording; authority rule refinement. | `docs/doctrine/` |
| Source refresh | Adds or updates current source/service knowledge. | New official source endpoint; API behavior; licensing change. | `docs/sources/` + source registry |
| Schema / contract proposal | Crystallizes an object family or lifecycle seam. | `RunReceipt`, `EvidenceBundle`, `DecisionEnvelope`, PMTiles sidecar. | `contracts/` for meaning + `schemas/contracts/v1/` for shape after ADR and repo checks. |
| Policy / gate proposal | Refines allow/deny/abstain or release logic. | Promotion gate; AI citation rule; sensitive geometry deny rule. | `policy/` + runbook + tests |
| Workflow / automation proposal | Proposes a governed process change. | Watcher flow; CI gate; artifact signing lane; packaging flow. | `pipelines/`, `pipeline_specs/`, `tools/`, runbooks |
| UI / shell proposal | Refines Evidence Drawer, shell state, Focus Mode, or map interaction. | Drawer payloads; trust badges; route grouping; preview renderer. | `docs/architecture/`, UI docs, component README after repo verification. |
| Data / domain expansion | Expands a lane or sequencing burden. | Hydrology watcher; soils lane; biodiversity extension; hazards context. | `docs/domains/` + source descriptors |
| Implementation note | Narrow operational detail. | Normalization rule; naming rule; sharding convention. | Local package README or runbook |
| Duplicate / corroborative | Repeats accepted direction without a new destination. | Repeated PMTiles attestation note. | Register cross-reference only |
| Lineage-only | Historically useful, no active action. | Older pass variant; superseded sketch. | Archive / lineage location |
| Repo-verification candidate | Claims that need direct repo proof. | “Workflow YAML exists”; “validator already enforced.” | Verification backlog |

## Intake statuses

| Status | Meaning | Next allowed move |
| --- | --- | --- |
| CAPTURED | Stored with date, family, short summary, and source reference. | TRIAGED |
| TRIAGED | Classified and linked to one or more categories. | Candidate canonical, corroborative, deferred, archived, or rejected. |
| CANDIDATE CANONICAL | Fits doctrine and has one clear destination. | Promote only with owner, validation, and rollback target. |
| CORROBORATIVE | Adds support but no new canonical destination. | Cross-reference only. |
| DEFERRED | Useful later, but depends on upstream proof. | Keep on backlog. |
| ARCHIVED EXPLORATORY | Preserved but not active. | Archive and link forward. |
| REJECTED | Contradicts doctrine, exposes unacceptable risk, or overclaims without value. | Archive with rationale. |

### Status transition guardrails

- Do not move directly from `CAPTURED` to `CANDIDATE CANONICAL` without triage.
- Do not mark a packet `CANDIDATE CANONICAL` unless it has one clear owning destination or an ADR-backed split.
- Do not mark a packet `REJECTED` without a rationale that can be reviewed later.
- Do not treat `CORROBORATIVE` duplicates as independent authority votes.
- Do not treat `ARCHIVED EXPLORATORY` as deletion; keep lineage visible enough to audit.

## Promotion criteria

An idea may be promoted only when all of the following are true:

- [ ] It fits KFM’s inspectable-claim, evidence-first, map-first, time-aware, policy-aware doctrine.
- [ ] It has exactly one proposed canonical destination, or an ADR explains why the destination is split.
- [ ] It has an owner or steward for review.
- [ ] It does not create parallel schema, contract, policy, release, proof, receipt, source, or registry authority.
- [ ] Rights, terms, source role, sensitivity, cadence, and access constraints are verified where relevant.
- [ ] Implementation claims are verified against repo files, tests, workflows, logs, emitted artifacts, or runtime evidence.
- [ ] Any public or semi-public exposure has EvidenceBundle support, policy decision, review state, release state, correction path, and rollback target appropriate to significance.
- [ ] Negative outcomes remain available: `ABSTAIN`, `DENY`, or `ERROR` instead of forced publication.

## Maintenance workflow

1. **Capture** the packet with filename, date signal, source ID, hash if available, and short summary.
2. **Classify** each extractable idea using the intake taxonomy.
3. **De-duplicate** against previous packets and mark corroborative repeats.
4. **Assign candidate destinations** without creating parallel authority.
5. **Verify blockers**: repo path, owner, source rights, sensitivity, current external facts, schema-home authority, tests, and rollback.
6. **Promote or abstain** through a visible decision record.
7. **Archive** lineage material after canonical deltas are absorbed or rejected.
8. **Update this index** whenever packet status, destination, or verification state changes.

## Verification checklist

- [ ] Confirm the real repository contains or should create `docs/intake/`.
- [ ] Confirm whether repo naming prefers `NEW_IDEAS_INDEX.md`, `new-ideas-index.md`, or `new-ideas-register.md`.
- [ ] Check for an existing `docs/intake/new-ideas-register.md` before creating a sibling register.
- [ ] Decide whether this file is the landing page, the register, or a companion to `docs/intake/new-ideas-register.md`.
- [ ] Assign `OWNER_TBD` to a real docs steward or intake owner.
- [ ] Add stable source IDs and hashes for every packet.
- [ ] Verify whether earlier February–April packets are present, duplicated, superseded, or already promoted.
- [ ] Recheck all version-sensitive external claims before source activation or implementation.
- [ ] Confirm no sensitive exact locations, credentials, unpublished policy state, or restricted EvidenceBundle contents are copied into public docs.
- [ ] Confirm candidate paths against Directory Rules and mounted repo evidence before using them in PRs.
- [ ] Add tests or lint checks if this index becomes machine-read or CI-gated.

## Rollback

Rollback is required if this index:

- upgrades an EXPLORATORY packet into authority without promotion;
- creates a path or naming conflict with mounted repo convention;
- leaks sensitive, restricted, rights-uncertain, or unpublished material;
- creates parallel schema, contract, policy, source, release, proof, receipt, or registry homes;
- claims implementation depth that was not verified.

Rollback target: restore the previous committed version of `docs/intake/NEW_IDEAS_INDEX.md`, then add a drift or correction entry explaining the reverted claim.

## Appendix: triage record template

Use this template when a packet is ready for more detailed triage. Keep examples illustrative; do not fill unknown fields by guessing.

```markdown
### NIP-YYYY-MM-DD[-slug]

| Field | Value |
| --- | --- |
| Intake ID | `NIP-YYYY-MM-DD[-slug]` |
| Source packet | `SOURCE_PACKET_TBD` |
| Source ID / hash | `SOURCE_ID_TBD`; `HASH_TBD` |
| Date signal | `DATE_SIGNAL_TBD` |
| Current status | `CAPTURED / EXPLORATORY` |
| Owner / steward | `OWNER_TBD` |
| Candidate destination | `PATH_TBD_AFTER_REPO_INSPECTION` |
| Decision record | `DECISION_RECORD_TBD` |

#### Captured themes

- Theme 1.
- Theme 2.

#### Blocking checks

- NEEDS VERIFICATION: source rights and access terms.
- NEEDS VERIFICATION: repo path convention and adjacent docs.
- NEEDS VERIFICATION: schema-home, policy-home, and test-home authority.

#### Proposed disposition

`TRIAGED | CANDIDATE CANONICAL | CORROBORATIVE | DEFERRED | ARCHIVED EXPLORATORY | REJECTED`

#### Review note

Explain why the disposition is safe, reversible, and bounded.
```

## Appendix: packet cards

<details>
<summary><strong>NIP-2026-04-16-governed-baselines - governed baselines, correction seams, and time-aware carriers</strong></summary>

### Source

`New Ideas 4-16-26(1).pdf`

- SHA-256: `73e10e3c75c1f3cbbd49641b33bddfde93895b85c7562af3dbe161cf2d4c6c16`
- Pages: `110`
- Bytes: `1,224,493`
- Source date: `2026-04-16`
- Capture and triage date: `2026-07-29`
- Detailed review: [`exploratory/new-ideas-4-16-source-map.md`](exploratory/new-ideas-4-16-source-map.md)

### Captured themes

- Governed fauna and soil intake with source identifiers, sensitivity, receipts, finite outcomes, and release proof.
- Versioned vegetation, hydrology, and air-quality baselines with explicit change and correction pressure.
- AQS historical authority separated from provisional AirNow signal, HMS interpretation, and HRRR forecast context.
- Consent-first GEDCOM/DNA import, purpose-bound permission, pseudonymization, revocation, and cache cleanup.
- MapLibre time filtering, epoch-bucket manifests, worker preparation, and visible temporal context.
- PMTiles structural verification and signed bytes kept separate from evidence and release authority.
- STAC profile, link-closure, and deterministic API behavior.
- Historical post-office and trail overlays with location precision and valid-time caveats.

### Triage notes

Most paste-ready fauna, soil, receipt, PMTiles, consent, and catalog material overlaps existing repository surfaces and should not be copied. The useful delta is connective: material-change decisions, baseline cohorts, source-role corroboration, correction states, purpose-bound revocation propagation, governed time buckets, STAC link closure, historical proximity semantics, and declared canonical hash profiles.

The packet's Cesium implementation is not carried forward. Only renderer-neutral time-availability ideas survive, pending accepted renderer authority.

### Candidate next extraction

Implement the repository's already-recorded deterministic `stable_diff.py` slice with synthetic same/changed/malformed fixtures. Keep it non-authoritative; use a later contract to decide materiality.

</details>

<details>
<summary><strong>NIP-2026-04-30-retrieval-offline-trust - retrieval meaning, environmental support, and offline trust</strong></summary>

### Source

`New Ideas 4-30-26.pdf`

- SHA-256: `3d7585dd43009c14fa7ae9cec864bb0ecc84340d6fa920b67bc53cd1e7adda0b`
- Pages: `289`
- Bytes: `3,246,311`
- Source date: `2026-04-30`
- Capture and triage date: `2026-07-29`
- Detailed review: [`exploratory/new-ideas-4-30-source-map.md`](exploratory/new-ideas-4-30-source-map.md)

### Captured themes

- USDA PLANTS distribution, eBird EBD/SED effort, GBIF asynchronous downloads, source terms, and query predicates.
- Soil-moisture and air-quality fusion across grids, stations, units, cadences, and knowledge characters.
- PMTiles deltas, signed digest batches, mobile resource budgets, offline-first packaging, and verify-before-render behavior.
- HUC12/COMID crosswalks, promotion gates, decision logs, obligations, STAC validation, and canonical hashing.
- County biodiversity work prioritization, sampling bias, vegetation-change confounders, and source delivery latency.

### Triage notes

Most packet code and path trees duplicate stronger repository surfaces. The durable additions are connective: retrieval intent, terms drift, sampling support, distribution-state meaning, exploration-bias controls, measurement reconciliation, availability latency, asynchronous transfer state, offline trust freshness, verified-rendering budgets, and correctable observation fitness.

Cesium/MapLibre overlays, live source activation, hard-coded thresholds, wildcard hosting examples, credentials, and fail-open workflow fragments are not carried forward.

### Candidate next extraction

Define a contract-only `DistributionAssertion` and `CoverageAssessment` slice with synthetic states for `present`, `explicitly_absent`, `not_assessed`, `unknown`, `suppressed`, `stale`, and `missing_row`. No network access, source activation, or publication.

</details>

<details>
<summary><strong>NIP-2026-05-08 — ecology watchers, tile gating, and no-network proof slice</strong></summary>

### Source

`New Ideas 5-8-26.pdf`

### Captured themes

- Ecology and environmental watcher gating using MAIAC AOD, FIRMS, SMAP, AirNow, and Kansas Mesonet concepts.
- Deterministic thresholds and persistence windows for tile state changes.
- `DecisionEnvelope`, `RunReceipt`, and signed provenance expectations.
- PMTiles sidecar verification and public-client fail-closed behavior.
- MapLibre/Cesium verification workflows and no-network proof slice direction.

### Triage notes

This packet has several high-value candidates, but the source facts, licenses, API/key requirements, and operational thresholds need verification before any source activation or public map behavior. Treat thresholds as proposed policy gates, not as scientific absolutes.

### Candidate next extraction

Create a future issue or triage record for: “Ecology watcher gating specification and offline proof slice.”

</details>

<details>
<summary><strong>NIP-2026-05-10 — PMTiles attestation, OCI publication, and fail-closed CI</strong></summary>

### Source

`New Ideas 5-10-26.pdf`

### Captured themes

- PMTiles operational quirks: HTTP Range behavior, cache invalidation, versioned filenames, partitioned artifacts, and client parity.
- Signed sidecar schema using BLAKE3/Bao concepts, DSSE/cosign/Rekor, OCI/ORAS publication, and run receipts.
- Fail-closed CI gates for artifact root integrity, range integrity, publisher attestation, and policy denial.
- MapLibre performance probes and visual regression direction.
- Automation starter pack ideas for watcher-to-promotion flow.

### Triage notes

This packet is strong implementation pressure for an artifact-verification lane, but tool versions, package availability, licensing, registry behavior, and repo workflow paths remain NEEDS VERIFICATION.

### Candidate next extraction

Create a future issue or triage record for: “PMTiles publication attestation verifier and negative-path CI tests.”

</details>

<details>
<summary><strong>NIP-2026-07-29-new-ideas-5 — multi-cluster implementation pressure</strong></summary>

### Source

`New Ideas 5.pdf`

- SHA-256: `094200ad69f3843d856fce782806f4090c31263567d533d0b425468730d1c91d`
- Pages: `944`
- Bytes: `10,558,510`
- Source authoring date: `NEEDS VERIFICATION`
- Capture and triage date: `2026-07-29`
- Detailed review: [`exploratory/new-ideas-5-source-map.md`](exploratory/new-ideas-5-source-map.md)

### Captured themes

- 3D Story Node and dual-renderer proposal.
- Projection extension mapping and catalog QA.
- Sigstore/cosign, SLSA, SBOM, attestations, and release lineage.
- Hydrology/NWIS watchers and resilient pipeline patterns.
- Atmosphere fusion and sensor/source-role modeling.
- Soil/geology GeoParquet, COG, PMTiles, and deterministic identity.
- Reproducible experiments, graph summaries, and AI retrieval.
- License and dependency checks.

### Triage notes

The packet is broad, internally heterogeneous, and contains implementation-looking paths and code. Current repository evidence shows that several themes are corroborative, several require external verification, and two early proposals are immediately blocked as written:

- the Cesium + MapLibre peer-renderer path requires an ADR-scoped decision and dependency/release burden; and
- the networked catalog quick gate must not bypass unresolved STAC profile, placeholder-record, no-network, and record-versus-closure boundaries.

### Candidate next extraction

Create a separately authorized decision packet for deterministic, record-local STAC readiness after resolving profile ownership and the placeholder `collection.json` disposition. Do not copy the PDF's networked workflow directly.

</details>

---

Back to top: [New Ideas Index](#new-ideas-index)
