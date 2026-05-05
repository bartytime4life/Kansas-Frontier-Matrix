<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/TODO-uuid-domain-lane-template
title: ADR-0008 — Domain Lane Template
type: standard
version: v1
status: draft
owners: TODO: documentation steward + domain lane stewards
created: 2026-04-27
updated: 2026-05-02
policy_label: TODO: public|restricted after policy review
related: [NEEDS_VERIFICATION: docs/adr/ADR-0001-schema-home.md, NEEDS_VERIFICATION: docs/registers/AUTHORITY_LADDER.md, NEEDS_VERIFICATION: docs/registers/CANONICAL_LINEAGE_EXPLORATORY.md, NEEDS_VERIFICATION: docs/sources/SOURCE_DESCRIPTOR_STANDARD.md, NEEDS_VERIFICATION: schemas/contracts/v1/, NEEDS_VERIFICATION: contracts/]
tags: [kfm, adr, domain-lane, documentation-control-plane, evidence, publication-governance]
notes: [Revision of attached draft Markdown. doc_id, owners, policy_label, ADR numbering, schema-home authority, and related paths require repo verification before merge.]
[/KFM_META_BLOCK_V2] -->

# ADR-0008 — Domain Lane Template

A standard decision record for making every KFM domain lane evidence-bound, source-ledgered, policy-aware, map-ready, testable, reversible, and safe to promote only through governed release controls.

| Field | Value |
|---|---|
| **Proposed target path** | `docs/adr/ADR-0008-domain-lane-template.md` |
| **Numbering status** | `CONFLICTED / NEEDS VERIFICATION`: the attached draft uses `ADR-0008`, while the visible pipeline ADR index lists `ADR-0007-domain-lane-template` and `ADR-0008-sensitive-location-policy`. |
| **Status** | Draft — proposed standard |
| **Decision type** | Documentation, architecture, contracts, source registry, validation, publication governance, and rollback discipline |
| **Applies to** | Hydrology, habitat, fauna, flora, soil, agriculture, geology/natural resources, atmosphere/air, roads/rail/trade routes, settlements/infrastructure, archaeology, hazards, people/genealogy/DNA/land ownership, and future KFM lanes |
| **Does not do** | Does not create live connectors, publish data, decide schema-home authority, assign owners, or claim implementation maturity |
| **Rollback** | Revert this ADR before adoption; after adoption, supersede with a new ADR and retain this file as lineage |

> [!IMPORTANT]
> **NEEDS VERIFICATION — ADR numbering.** Do not merge this file under `ADR-0008` until the ADR register is checked. If the register already assigns `ADR-0007-domain-lane-template`, rename this file and update all inbound links. If maintainers intentionally keep `ADR-0008`, record the exception in the ADR register.

> [!NOTE]
> **Evidence boundary.** This ADR states KFM doctrine and a proposed lane template. Current implementation depth remains **UNKNOWN** where the mounted repo, tests, schemas, workflows, dashboards, runtime logs, or emitted proof objects have not been inspected in this session.

## Quick jumps

- [Status](#status)
- [Evidence basis and verification boundary](#evidence-basis-and-verification-boundary)
- [Context](#context)
- [Decision](#decision)
- [Domain lane contract](#domain-lane-contract)
- [Minimum lane package](#minimum-lane-package)
- [Required file families](#required-file-families)
- [Lifecycle and trust flow](#lifecycle-and-trust-flow)
- [Lane burden tiers](#lane-burden-tiers)
- [Growth and retention rules](#growth-and-retention-rules)
- [Validation gates](#validation-gates)
- [Alternatives considered](#alternatives-considered)
- [Consequences](#consequences)
- [Adoption plan](#adoption-plan)
- [Open verification backlog](#open-verification-backlog)
- [Appendix A — Copy/paste lane README skeleton](#appendix-a--copypaste-lane-readme-skeleton)
- [Appendix B — ADR maintenance checklist](#appendix-b--adr-maintenance-checklist)

## Status

| Status item | Value |
|---|---|
| **ADR state** | `draft / PROPOSED` |
| **Merge posture** | `HOLD` until ADR number, owners, policy label, related links, and repo conventions are verified |
| **Truth posture** | `CONFIRMED` doctrine / `PROPOSED` template / `UNKNOWN` repo implementation depth |
| **Release posture** | Documentation-only; no source activation, public publication, or runtime behavior implied |
| **Review burden** | Documentation steward, domain lane stewards, schema/contract steward, policy/release reviewer |
| **Primary risk** | A generic lane template could flatten sensitive domain burden unless burden tiers, policy gates, and exceptions remain explicit. |

## Evidence basis and verification boundary

| Source | Status | Supports | Limits |
|---|---|---|---|
| Attached draft `Pasted markdown.md` | `CONFIRMED` revision baseline | Existing ADR text, metadata, lifecycle diagram, file-family inventory, validation gates, and README skeleton | Does not prove repo paths, owners, ADR number, CI, schemas, or implementation behavior |
| Pipeline Living Implementation Manual v0.3 | `LINEAGE / CONFIRMED source text` | KFM lifecycle law, proof-bearing implementation sequence, recurring object families, and the visible ADR-numbering conflict | Does not prove the mounted repo contains those ADR files |
| Documentation Architecture passes | `CONFIRMED doctrine / LINEAGE` | ADR structure, source authority, canon/lineage/exploratory separation, schema-home ambiguity handling | Does not prove current repo state without mounted source inspection |
| Domain lane PDFs | `LINEAGE` | Repeated cross-domain pressure for source registries, validators, fixtures, policies, proof packs, and rollback paths | Prior scaffold/report repetition is continuity, not implementation proof |
| Current workspace inspection | `CONFIRMED` for this session | `/mnt/data` is not a mounted Git repository; no source tree was available for direct verification | Does not describe the state of any external or later-mounted repository |

**Verification rule:** when this ADR conflicts with a mounted repo convention, the mounted repo convention wins for implementation paths, and this ADR must be updated or superseded rather than used to create parallel authority.

## Context

KFM domain reports repeat the same implementation pressure: each lane needs a human control plane, source registry, source-role discipline, machine contracts, validation fixtures, fail-closed policy gates, lifecycle folders, catalog/proof/release separation, rollback paths, and trust-visible public surfaces.

Without a shared template, each domain risks inventing its own structure. That weakens source authority, makes review harder, creates duplicate schema homes, and lets exploratory packet material appear more authoritative than it is.

A shared template must not flatten domain nuance. Hydrology, soil, fauna, archaeology, hazards, land ownership, governed AI, and 3D story lanes do not carry identical public-risk burdens. The template sets the minimum control plane; lane burden tiers add the additional gates needed for sensitive, temporal, regulatory, runtime, 3D, and release-bearing work.

Current implementation evidence is bounded. This authoring workspace did not expose a mounted KFM checkout, tests, workflows, schema registry, dashboards, runtime logs, branch protections, or emitted proof objects. Therefore this ADR standardizes a **proposed lane template**, not current implementation behavior.

## Decision

Adopt a standard **Domain Lane Template** for all new or materially revised KFM domain lanes.

A domain lane is a bounded KFM subject area that turns source evidence into inspectable, policy-aware, time-aware, map-ready claims without collapsing canonical evidence, derived artifacts, UI rendering, AI synthesis, publication state, review state, and correction lineage into one surface.

Every lane MUST:

1. preserve the KFM lifecycle:
   `RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED`;
2. keep public clients and normal UI surfaces behind governed APIs or released artifacts;
3. resolve consequential claims through `EvidenceRef -> EvidenceBundle`;
4. record source role, rights, sensitivity, spatial scope, temporal scope, review state, release state, and correction lineage;
5. fail closed when source terms, precision, sensitivity, ownership, review, or release state is unresolved;
6. keep AI interpretive and evidence-subordinate;
7. distinguish canonical records from derived tiles, search indexes, graph projections, summaries, scenes, dashboards, exports, screenshots, and rendered pixels;
8. define validation, policy, fixtures, acceptance gates, rollback, correction, and supersession before live source activation.

This ADR also establishes a **minimum lane package**. A lane may omit API, UI, graph, 3D, AI, or public-delivery surfaces only by explicitly marking them `OUT_OF_SCOPE`, `DEFERRED`, or `NEEDS VERIFICATION`.

[Back to top](#adr-0008--domain-lane-template)

## Domain lane contract

Each lane MUST declare the following contract before it accepts live source data or public release candidates.

| Contract area | Required answer | Default truth posture |
|---|---|---|
| **Scope and exclusions** | What belongs in this lane, what does not, and which neighboring lanes may reference it. | `PROPOSED` until steward-reviewed |
| **Source roles** | Which sources are authoritative, contextual, modeled, observational, regulatory, archival, aggregator, or exploratory. | `NEEDS VERIFICATION` until source descriptor review |
| **Canonical object families** | The lane’s record, assertion, observation, event, geometry, layer, catalog, proof, release, correction, and rollback objects. | `PROPOSED` until schema/fixture evidence exists |
| **Identity and hashing** | Deterministic identifiers, version keys, geometry fingerprints, `spec_hash` or equivalent, and collision/ambiguity behavior. | `PROPOSED` |
| **Temporal model** | Observation time, source time, valid time, transaction/ingest time, review time, release time, and correction time. | `PROPOSED` |
| **Sensitivity posture** | Exact-location, living-person, DNA, archaeology, rare species, critical infrastructure, private land, cultural/sovereignty, and rights handling. | `DENY` or `HOLD` until reviewed |
| **Publication model** | What can become public, what must be generalized, what remains restricted, and what proof pack is required. | `PROPOSED` |
| **Map/UI model** | Layer IDs, Evidence Drawer payloads, trust badges, negative states, time controls, export behavior, and stale/correction indicators. | `PROPOSED` until UI fixtures exist |
| **Governed AI model** | What Focus Mode may answer, when it must abstain, and what EvidenceBundle it may consume. | `PROPOSED`; default deny direct model access |
| **Validation model** | Valid/invalid fixtures, source descriptor checks, schema validation, policy checks, no-network tests, and promotion dry-runs. | `PROPOSED` until tests pass |
| **Rollback and correction model** | How to withdraw, correct, regenerate, supersede, or generalize artifacts without erasing lineage. | `PROPOSED` until release fixtures exist |
| **Ownership and review model** | Steward roles, CODEOWNERS/review path, release approver, and policy reviewer. | `UNKNOWN` until repo evidence exists |

## Minimum lane package

A lane is not ready for live source activation or public release candidates until these package layers exist, or are explicitly deferred with a reason.

| Package layer | Minimum required surfaces | Why it exists |
|---|---|---|
| **Human control plane** | Lane README, architecture note, runbook, verification backlog, ADRs for consequential decisions | Keeps scope, ownership, assumptions, and review burden inspectable |
| **Source control plane** | Source registry, dataset registry, source-role matrix, rights/sensitivity notes | Prevents connectors and external feeds from becoming unreviewed authority |
| **Contract plane** | Human object cards plus machine schemas or repo-confirmed equivalent | Keeps semantic meaning and executable validation aligned |
| **Lifecycle plane** | Raw/work/quarantine/processed/catalog/triplet/published families or repo equivalent | Preserves the KFM trust membrane |
| **Verification plane** | Fixtures, validators, policy tests, no-network checks, promotion dry-run | Turns doctrine into mergeable gates |
| **Release plane** | ReleaseManifest, ProofPack, rollback card, correction path, catalog closure | Makes publication a governed state transition |
| **Delivery plane** | Governed API contract, layer manifest, Evidence Drawer payload, Focus Mode envelope when in scope | Keeps UI, map, export, and AI surfaces downstream of evidence |

## Required file families

All paths below are **template paths**. Use the repo-equivalent canonical location when a stronger checked-in convention is verified. Do not create duplicate homes to satisfy the template.

### Human control-plane files

| File family | Proposed path pattern | Purpose | Update trigger |
|---|---|---|---|
| Lane landing doc | `docs/domains/<domain>/README.md` | Scope, owners, status, repo fit, accepted inputs, exclusions, quick links, and current evidence boundary. | New lane, scope change, owner change, release posture change |
| Lane architecture | `docs/architecture/<domain>_architecture.md` or `docs/domains/<domain>/ARCHITECTURE.md` | End-to-end lane structure, object families, trust seams, public surfaces, dependency map. | New object family, API/UI surface, lifecycle change, major source change |
| Operations runbook | `docs/runbooks/<domain>_operations.md` | How to run validators, refresh registries, inspect fixtures, and perform dry-runs. | Tooling, source refresh, CI, or validator change |
| Rollback runbook | `docs/runbooks/<domain>_rollback.md` | Withdrawal, correction, rollback target, artifact regeneration, and release-state repair. | Release, correction, or promotion-gate change |
| Lane ADRs | `docs/adr/ADR-<number>-<domain>-*.md` | Decisions that change lane burden, schema homes, source role, policy, or publication model. | Any consequential architectural choice |
| Verification backlog | `docs/backlog/<domain>_verification_backlog.md` | Concrete `UNKNOWN` / `NEEDS VERIFICATION` items and evidence required to retire them. | Any unresolved source, policy, rights, runtime, or repo question |
| Expansion backlog | `docs/backlog/<domain>_expansion_backlog.md` | Deferred sublanes, connectors, UI features, analysis products, and proof slices. | New idea intake, steward request, source opportunity |

### Registries and source-control files

| File family | Proposed path pattern | Purpose | Update trigger |
|---|---|---|---|
| Source registry | `data/registry/<domain>/sources.yaml` | SourceDescriptor instances and source-role assignments. | New source, source role change, rights/cadence change |
| Dataset registry | `data/registry/<domain>/datasets.yaml` | Dataset families, versions, source links, status, and lifecycle mapping. | New dataset, new version, deprecation |
| Layer registry | `data/registry/<domain>/layers.yaml` | Released layer IDs, display meaning, delivery class, evidence route, and trust badges. | New layer, style meaning change, time or policy change |
| Sensitivity registry | `data/registry/<domain>/sensitivity_policies.yaml` | Domain-specific sensitivity classes, transforms, public-safe rules, and review obligations. | New sensitivity class, steward rule, law/source-term change |
| Registry backlog | `data/registry/<domain>/verification_backlog.yaml` | Machine-friendly registry-level unknowns. | Registry entry with missing proof |

### Contracts and schemas

| File family | Proposed path pattern | Purpose | Update trigger |
|---|---|---|---|
| Machine schemas | `schemas/contracts/v1/<domain>/*.schema.json` or repo-confirmed equivalent | Executable shape for lane objects, fixtures, and contracts. | Schema version, object family, validator change |
| Human contracts | `contracts/<domain>/README.md` and/or object cards | Meaning, invariants, semantic field intent, lifecycle expectations. | Object model or field meaning change |
| Shared governance schemas | `schemas/contracts/v1/governance/*.schema.json` or repo-confirmed equivalent | Shared objects such as `EvidenceBundle`, `DecisionEnvelope`, `RuntimeResponseEnvelope`, `ReleaseManifest`, and `ValidationReport`. | Shared object wave or cross-lane change |

> [!WARNING]
> **Schema-home authority remains unresolved.** Do not maintain divergent definitions in both `contracts/` and `schemas/`. If both homes exist, resolve authority through the schema-home ADR and mark the non-authoritative home as explanatory, adapter-facing, or deprecated.

### Lifecycle, catalog, proof, and release object families

| File family | Proposed path pattern | Purpose | Update trigger |
|---|---|---|---|
| Lifecycle storage | `data/raw/<domain>/`, `data/work/<domain>/`, `data/quarantine/<domain>/`, `data/processed/<domain>/` | Segregated lifecycle zones. | Source activation, processing, quarantine, promotion |
| Catalog closure | `data/catalog/stac/<domain>/`, `data/catalog/dcat/<domain>/`, `data/catalog/prov/<domain>/` | Catalog and provenance artifacts for released or candidate data. | Promotion, catalog change, provenance change |
| Receipts | `data/receipts/<domain>/` | Process-memory records such as ingest, validation, run, AI, or transform receipts. | Pipeline run or governed runtime run |
| Proofs | `data/proofs/<domain>/` | Release-significant proof packs, validation reports, policy decisions, signatures, and promotion evidence. | Promotion, release, correction, withdrawal |
| Published artifacts | `data/published/<domain>/` | Public-safe released artifacts only. | Promotion or rollback |
| Triplets/graph | `data/triplets/<domain>/` | Derived graph/triplet projection when in scope. | Graph projection or relation model change |
| Release lane | `release/<domain>/` or repo-equivalent | Release manifest, rollback card, correction notice, publication bundle. | Promotion, withdrawal, correction, supersession |

### Policy, validation, and tests

| File family | Proposed path pattern | Purpose | Update trigger |
|---|---|---|---|
| Policy rules | `policy/<domain>/*.rego` or repo-confirmed equivalent | Rights, sensitivity, source-role, publication, AI, and promotion decisions. | Source role, sensitivity, publication, or runtime rule change |
| Policy tests | `policy/<domain>/tests/*.rego` or repo-confirmed equivalent | Positive and negative policy cases. | Rule change or new reason/obligation code |
| Validators | `tools/validators/<domain>/*` | Schema, source, lifecycle, catalog, proof, geoprivacy, and promotion validators. | Schema, fixture, source, or gate change |
| Diff tools | `tools/diff/<domain>/*` | Source refresh, backfill, and version comparison helpers. | Watcher/backfill/change-detection adoption |
| CI workflow | `.github/workflows/<domain>-*.yml` | Optional lane-specific CI if repo convention supports it. | Validator/test suite becomes merge-blocking |
| Fixtures | `tests/fixtures/<domain>/valid/*`, `tests/fixtures/<domain>/invalid/*`, `tests/fixtures/<domain>/policy/*` | Valid, invalid, and policy-focused examples. | Schema, policy, validator, or object change |
| Lane tests | `tests/<domain>/*` | Unit, integration, no-network, and regression tests. | Validator, policy, pipeline, API/UI contract change |

### Runtime and delivery surfaces

| File family | Proposed path pattern | Purpose | Update trigger |
|---|---|---|---|
| API contract | `apps/governed_api/openapi/<domain>.openapi.yaml` or repo-equivalent | Governed API surface definition when runtime/public access is in scope. | New route, response, envelope, or public query |
| API route | `apps/governed_api/routes/<domain>.*` or repo-equivalent | Runtime implementation surface when verified. | Framework-confirmed route work |
| UI layer descriptors | `ui/<domain>/` or `web/<domain>/` repo-equivalent | Layer descriptors, Evidence Drawer payload fixtures, trust-visible UI notes. | Public layer, drawer, Focus Mode, story, or export change |

> [!NOTE]
> Runtime path spelling is intentionally provisional. Prior KFM materials use both underscore and hyphen path forms for governed API homes. Use the mounted repo convention after inspection and record any migration or alias in an ADR.

[Back to top](#adr-0008--domain-lane-template)

## Lifecycle and trust flow

```mermaid
flowchart LR
  S[Source candidate] --> SD[SourceDescriptor<br/>role + rights + cadence + sensitivity]
  SD --> R[RAW]
  R --> T{Triage checks}
  T -->|usable for work| W[WORK]
  T -->|rights / shape / sensitivity unresolved| Q[QUARANTINE]
  W --> V[ValidationReport<br/>schema + source + policy + fixture checks]
  V -->|fail / hold| Q
  V -->|pass| P[PROCESSED]
  P --> C[CATALOG / TRIPLET<br/>STAC + DCAT + PROV + relation projection]
  C --> EB[EvidenceBundle<br/>claim support + provenance]
  EB --> D[DecisionEnvelope<br/>policy + review + release decision]
  D -->|HOLD / DENY| Q
  D -->|PROMOTE| PR[ProofPack + ReleaseManifest<br/>rollback target + correction path]
  PR --> PUB[PUBLISHED<br/>released artifact]
  PUB --> API[Governed API<br/>EvidenceRef resolution]
  API --> UI[Map/UI<br/>Evidence Drawer]
  API --> AI[Focus Mode<br/>ANSWER / ABSTAIN / DENY / ERROR]
  PR --> CR[CorrectionNotice / Withdrawal / Rollback]
```

### Flow rules

- `RAW`, `WORK`, and `QUARANTINE` are never normal public surfaces.
- Public artifacts are released outputs, not canonical truth.
- Tiles, scenes, indexes, summaries, graph projections, dashboards, screenshots, and AI responses are rebuildable derivatives or interpretive surfaces.
- A rendered feature, popup, export, story, or Focus Mode answer is consequential only when it resolves to an admissible `EvidenceBundle` and passes policy/review checks.
- Promotion is a governed state transition, not a file move.
- Rollback and correction paths are part of publication readiness, not afterthoughts.

## Lane burden tiers

Not every lane carries the same risk. The template is constant, but the burden tier changes how much proof is required before publication. Burdens accumulate: a sensitive runtime lane must satisfy the sensitive-location, runtime/AI, and release-bearing gates that apply to it.

| Tier | Typical lane examples | Required extra burden |
|---|---|---|
| **Baseline evidence lane** | Hydrology fixture, public reference layers, synthetic proof slice | SourceDescriptor, no-network fixtures, schema validation, EvidenceBundle, ReleaseManifest |
| **Public map lane** | Road layer, soil unit layer, public-safe habitat layer | Layer registry, style/layer manifest, Evidence Drawer payload, no-raw-public-path tests |
| **Sensitive location lane** | Rare species, archaeology, cultural sites, critical infrastructure | Geoprivacy transform receipt, steward review, exact-location denial tests, generalized public geometry |
| **Temporal assertion lane** | People/land ownership, historical route status, hazard events | Valid-time/transaction-time handling, assertion status, overlap checks, correction lineage |
| **Regulatory/context lane** | Flood hazard, critical habitat, official designations | Source-role policy proving regulatory source vs observation/model distinction |
| **Runtime/AI lane** | Focus Mode over released evidence | RuntimeResponseEnvelope, citation validation, ABSTAIN/DENY tests, no-direct-model-client checks |
| **3D/story lane** | Terrain, viewshed, archaeological 3D, Cesium scene | 3D admission checklist, scene manifest, same EvidenceBundle/policy/release controls as 2D |
| **Release-bearing lane** | Any public or semi-public promoted product | ProofPack, ReleaseManifest, rollback card, correction path, catalog closure |

## Growth and retention rules

### New sources

A new source MUST NOT enter a lane as a connector first. It enters as a source descriptor and review item.

Required updates:

1. `data/registry/<domain>/sources.yaml` or repo-equivalent;
2. source rights and sensitivity review;
3. source-role policy matrix;
4. source descriptor fixtures;
5. verification backlog entry for unresolved terms, cadence, quota, schema behavior, or attribution;
6. lane README and source registry docs.

### Schema and contract versions

A schema version is additive or explicitly superseding. Silent field meaning changes are prohibited.

Required updates:

1. object card or human contract;
2. schema file and `$id` / version metadata;
3. valid and invalid fixtures;
4. validators;
5. API/UI payload contracts if exposed;
6. compatibility and migration notes;
7. ADR when semantics or authority changes materially.

### Backfills and refreshes

Backfills are governed runs, not invisible data repairs.

Required records:

- backfill request or reason;
- input source version;
- previous artifact/version affected;
- transform or diff summary;
- `run_receipt`;
- validation report;
- proof or release update when public artifacts change;
- correction notice if public claims are affected.

### Corrections

A correction repairs public truth without erasing lineage.

Required records:

- affected claim/artifact/release IDs;
- corrected evidence bundle or source state;
- reason and reviewer;
- superseded release pointer;
- rollback or replacement target;
- updated Evidence Drawer / API / export behavior;
- visible correction state for downstream users.

### Deprecation and supersession

Deprecated files remain queryable or discoverable until a documented retention rule says otherwise.

Each deprecation MUST include:

- replacement pointer;
- compatibility note;
- reason;
- date;
- affected consumers;
- migration or regeneration instructions;
- rollback implications.

### Generated artifacts

Generated artifacts MUST be reproducible from canonical inputs, source descriptors, schemas, validators, and manifests.

Required behavior:

- generated outputs record `spec_hash` or equivalent deterministic identity;
- generated outputs link to input manifests and run receipts;
- generated outputs do not become normative contracts;
- regeneration instructions live in runbooks or tool READMEs;
- old receipts/proofs/releases remain queryable after newer releases land.

### Rollback references

Rollback targets must be explicit before publication.

A lane release MUST NOT promote without:

- rollback target;
- rollback reason codes;
- withdrawal/correction path;
- artifact retention rule;
- reviewer or steward role;
- public-state propagation plan.

[Back to top](#adr-0008--domain-lane-template)

## Validation gates

The first implementation of this ADR is not complete until the following gates pass or are explicitly marked `NEEDS VERIFICATION`.

| Gate | Acceptance condition |
|---|---|
| **ADR numbering gate** | ADR index confirms this file number/title or records a renumbering decision. |
| **Repo convention gate** | Actual `docs/`, `contracts/`, `schemas/`, `policy/`, `data/`, `tests/`, `apps/`, and UI paths are inspected before machine files are added. |
| **Schema-home gate** | Schema-home ADR or existing repo convention decides whether `schemas/contracts/v1/`, `contracts/`, or another path owns machine schemas. |
| **Documentation gate** | Lane README/architecture/runbook/backlog files exist or are intentionally deferred with reason. |
| **Source registry gate** | Sources are descriptor-first; no live connector runs without source review. |
| **Fixture gate** | Valid, invalid, and policy fixtures exist before broad implementation. |
| **No-network gate** | Initial tests run without external network dependency. |
| **Policy gate** | Unknown rights, unresolved sensitivity, exact sensitive location, and unsupported source roles fail closed. |
| **Public path gate** | No UI/API/delivery surface reads `RAW`, `WORK`, `QUARANTINE`, canonical stores, proof-pack stores, or model runtime stores directly. |
| **Evidence closure gate** | Consequential claims resolve `EvidenceRef -> EvidenceBundle`; otherwise runtime returns `ABSTAIN`, `DENY`, or `ERROR`. |
| **Release gate** | Published artifacts have ReleaseManifest, catalog closure, proof/receipt separation, rollback target, and correction path. |
| **AI gate** | Focus Mode consumes governed evidence only and emits finite outcomes. |
| **Lineage gate** | Superseded, deprecated, or migrated files retain successor/predecessor metadata. |
| **Sensitive-burden gate** | Sensitive location, living-person, DNA, cultural, ecological, archaeological, title, or security-relevant claims fail closed unless the lane-specific burden is satisfied. |

## Alternatives considered

| Alternative | Why rejected |
|---|---|
| **One bespoke architecture per domain** | Preserves nuance but increases drift, makes review uneven, and lets each lane invent its own trust seams. |
| **One generic domain README only** | Easier to adopt but too weak for KFM’s source, policy, proof, release, and rollback obligations. |
| **Machine schemas first, docs later** | Creates executable shapes before source authority, object meaning, rights, sensitivity, and review posture are settled. |
| **Live source connector first** | Makes external source behavior, rights, quota, sensitivity, and attribution failures appear late, after implementation inertia exists. |
| **UI/map proof first** | Risks treating rendered layers as truth before EvidenceBundle, policy, and release controls are proven. |
| **AI/runtime proof first** | Risks making generated language the first public value surface rather than a downstream interpretation of released evidence. |

## Consequences

### Positive

- Domain lanes become easier to compare, review, test, and migrate.
- Source roles, rights, sensitivity, and review state are visible before implementation.
- Machine contracts and human semantics remain separate but linked.
- Public-facing UI, API, Focus Mode, and export behavior stay downstream of governed evidence.
- Corrections and rollback become designed surfaces rather than emergency repairs.
- Exploratory packet pressure has a promotion path without becoming accidental authority.

### Costs

- New lanes carry more upfront documentation and fixture burden.
- Some fast demos will be delayed until source descriptors and no-network proof slices exist.
- The schema-home conflict must be resolved instead of worked around.
- Existing domain reports may require migration maps rather than direct replacement.
- Lane stewards must maintain registries and verification backlogs as living control surfaces.

### Tradeoff

This ADR deliberately favors slower, more inspectable first slices over broad domain coverage. That is acceptable because KFM’s value is the inspectable claim, not the speed with which a layer appears on a map.

## Adoption plan

1. **Verify the ADR index.** Reconcile the `ADR-0008` numbering issue before merge.
2. **Verify repo conventions.** Inspect the mounted repo for existing ADR, docs, schema, policy, registry, test, API, and UI patterns.
3. **Resolve schema-home linkage.** Link this ADR to the schema-home ADR or update this ADR after the schema-home decision is accepted.
4. **Fill owners and policy label.** Merge only after owners and policy label are filled or intentionally left as reviewable TODOs.
5. **Adopt as draft standard.** Treat this ADR as a template standard only after the above gates are visible.
6. **Pilot on one low-risk lane.** Prefer a no-network hydrology or similarly public-safe fixture lane.
7. **Run a proof slice.** SourceDescriptor -> fixture -> validator -> EvidenceBundle -> ReleaseManifest -> Evidence Drawer payload.
8. **Record deviations.** Any lane-specific exception gets an ADR, not an undocumented template fork.
9. **Promote or supersede.** After one proof-bearing lane passes, move this ADR from draft to review/published or supersede it with the field-tested version.

## Open verification backlog

| Item | Why it matters | Status |
|---|---|---|
| Confirm whether `ADR-0008` is available for this topic | Visible corpus suggests a numbering conflict. | `NEEDS VERIFICATION` |
| Confirm owners | Owners cannot be inferred from attached PDFs. | `TODO(owner): documentation steward + domain lane stewards` |
| Confirm policy label | Public/restricted status depends on repo policy. | `TODO(policy): public|restricted after policy review` |
| Confirm ADR format convention | Existing repo ADR style was not inspectable in this session. | `UNKNOWN` |
| Confirm schema-home authority | `contracts/` vs `schemas/contracts/v1/` remains a recurring conflict. | `CONFLICTED` |
| Confirm CODEOWNERS / review path | Required for lane steward and contract/policy review. | `UNKNOWN` |
| Confirm validator language and CI runner | Tooling should follow repo-native conventions. | `UNKNOWN` |
| Confirm existing lane docs | Avoid overwriting stronger existing docs. | `UNKNOWN` |
| Confirm generated artifact retention paths | Receipts, proofs, releases, and catalogs need actual repo homes. | `UNKNOWN` |
| Confirm UI/API path names | Do not invent route/component paths before repo inspection. | `UNKNOWN` |
| Confirm governed API spelling convention | Prior materials use underscore/hyphen variants. | `NEEDS VERIFICATION` |
| Confirm public repo vs mounted repo divergence | Attached reports may describe public repo surfaces that were not mounted in this session. | `NEEDS VERIFICATION` |

[Back to top](#adr-0008--domain-lane-template)

## Appendix A — Copy/paste lane README skeleton

Use this skeleton for `docs/domains/<domain>/README.md` or the repo-equivalent lane landing page. Fill placeholders from repo evidence, steward review, or explicit `UNKNOWN` / `NEEDS VERIFICATION` labels.

```markdown
<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/TODO-uuid-<domain>-lane
title: <Domain> Lane
type: standard
version: v1
status: draft
owners: TODO(owner): domain steward + documentation steward
created: YYYY-MM-DD
updated: YYYY-MM-DD
policy_label: TODO(policy): public|restricted after policy review
related: [NEEDS_VERIFICATION: docs/adr/ADR-0008-domain-lane-template.md]
tags: [kfm, domain-lane, <domain>]
notes: [Replace TODO values after repo and steward verification.]
[/KFM_META_BLOCK_V2] -->

# <Domain> Lane

One-line purpose for this KFM domain lane.

![Status](https://img.shields.io/badge/status-draft-lightgrey)
![Truth posture](https://img.shields.io/badge/truth-CONFIRMED%20%2F%20PROPOSED%20%2F%20UNKNOWN-blue)
![Policy](https://img.shields.io/badge/policy-TODO-orange)

> [!IMPORTANT]
> **Status:** draft / PROPOSED  
> **Owner:** TODO(owner): domain steward + documentation steward  
> **Path:** `docs/domains/<domain>/README.md`  
> **Truth posture:** CONFIRMED doctrine / PROPOSED implementation / UNKNOWN repo depth

## Quick jumps

- [Scope](#scope)
- [Repo fit](#repo-fit)
- [Accepted inputs](#accepted-inputs)
- [Exclusions](#exclusions)
- [Source registry](#source-registry)
- [Lifecycle](#lifecycle)
- [Validation](#validation)
- [Release and rollback](#release-and-rollback)
- [Open verification](#open-verification)

## Scope

Define what the lane governs.

## Repo fit

| Direction | Link or object | Status |
|---|---|---|
| Upstream | TODO: doctrine, source registry, adjacent lanes | `NEEDS VERIFICATION` |
| Downstream | TODO: schemas, validators, policy, API/UI, release | `NEEDS VERIFICATION` |
| Related ADRs | TODO: schema-home, source-role, publication, sensitivity | `NEEDS VERIFICATION` |

## Accepted inputs

List source families, fixtures, registries, schemas, review records, or candidate artifacts that belong here.

## Exclusions

List what does not belong here and where it goes instead.

## Source registry

Link to `data/registry/<domain>/sources.yaml` or repo-equivalent.

## Lifecycle

Show how lane data moves through `RAW -> WORK/QUARANTINE -> PROCESSED -> CATALOG/TRIPLET -> PUBLISHED`.

Diagram omitted — NEEDS VERIFICATION until this lane's concrete source families, proof objects, and release surfaces are confirmed.

## Validation

- [ ] SourceDescriptor fixtures exist.
- [ ] Valid and invalid object fixtures exist.
- [ ] Policy fixtures cover allow, hold, deny, abstain, and error conditions where relevant.
- [ ] No-network tests pass.
- [ ] No public path reads RAW, WORK, QUARANTINE, canonical stores, or model stores directly.

## Release and rollback

Define release artifacts, proof packs, correction notices, rollback cards, and withdrawal behavior.

## Open verification

Track concrete evidence still needed before stronger claims are allowed.
```

## Appendix B — ADR maintenance checklist

- [ ] ADR number reconciled with ADR index.
- [ ] Owners filled or intentionally marked `TODO(owner): <reason>`.
- [ ] Policy label filled or intentionally marked `TODO(policy): <reason>`.
- [ ] Related paths verified or marked `NEEDS VERIFICATION`.
- [ ] Schema-home conflict linked to the appropriate ADR.
- [ ] Lane README skeleton reviewed by documentation steward.
- [ ] Template tested against at least one domain lane.
- [ ] No section claims implementation behavior without evidence.
- [ ] No live connector, public publication, or model runtime behavior implied.
- [ ] Rollback path remains doc-only until implementation files are created.
- [ ] All repo path assumptions are rechecked against a mounted checkout before merge.

[Back to top](#adr-0008--domain-lane-template)
