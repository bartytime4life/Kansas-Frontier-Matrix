<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://adr/ADR-0031
title: Shared watcher ownership and placement
type: adr
version: v1
status: proposed
owners: ["Architecture steward", "Pipeline steward", "Source steward", "Domain stewards"]
created: 2026-08-08
updated: 2026-08-08
policy_label: public
related:
  - "docs/doctrine/directory-rules.md"
  - "docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md"
  - "pipelines/watchers/README.md"
  - "pipelines/domains/flora/watchers/README.md"
  - "pipeline_specs/watchers/README.md"
  - "pipeline_specs/flora/watchers/README.md"
  - "tools/watchers/README.md"
  - "tools/watchers/plants_watch/README.md"
  - "contracts/runtime/run_receipt.md"
tags: [adr, kfm, pipelines, watchers, source-change, material-change, governance]
supersedes: []
superseded_by: []
notes:
  - "PROPOSED: this ADR does not activate a watcher, choose a source, authorize network access, or move files until accepted and a reviewed migration is supplied."
[/KFM_META_BLOCK_V2] -->

# ADR-0031: Shared watcher ownership and placement

KFM should use `pipelines/watchers/` as the home for executable watcher orchestration that is genuinely reusable across multiple admitted sources or domains, keep domain-specific watcher semantics under `pipelines/domains/<domain>/watchers/`, keep declarative activation intent in the matching `pipeline_specs/` lane, and restrict `tools/watchers/` to side-effect-bounded reusable helpers. This proposal resolves the currently documented placement conflict without giving watchers source-admission, evidence, lifecycle, release, or publication authority.

| Field | Value |
|---|---|
| **ID** | ADR-0031 |
| **Status** | proposed |
| **Date** | 2026-08-08 |
| **Deciders** | Architecture steward · Pipeline steward · Source steward · affected domain stewards |
| **Consulted** | Contracts · schema · policy · evidence · release · correction/rollback reviewers |
| **Informed** | Connector, pipeline-spec, tooling, domain, CI, docs maintainers |
| **Supersedes** | — |
| **Superseded by** | — |
| **Directory Rules trigger** | §2.4 parallel-authority prevention and §14.2 structural migration discipline |
| **Primary responsibility root** | `pipelines/` |
| **Migration required** | yes, only after acceptance |
| **Rollback required** | yes |
| **Truth posture** | CONFIRMED current placement conflict / PROPOSED decision and migration |

---

## 1. Context

Current repository evidence documents several overlapping watcher surfaces:

- `pipelines/watchers/` describes a candidate shared executable-orchestration boundary;
- `pipelines/domains/flora/watchers/` describes domain-owned watcher behavior;
- `pipeline_specs/watchers/` and `pipeline_specs/flora/watchers/` contain duplicated plants-drift specification placeholders;
- `tools/watchers/` and `tools/watchers/plants_watch/` describe reusable watcher tooling.

The parent watcher README explicitly classifies shared-versus-domain-versus-tool ownership as **CONFLICTED**, says the shared watcher runtime is unverified, and warns against resolving the conflict by copying code or specifications into multiple roots. It also confirms a non-publisher boundary: watcher output is candidate evidence-development material and cannot itself become source admission, EvidenceBundle closure, release, or publication.

Pass 20 implementation ideas add pressure for material-change monitoring across PLANTS, CDL, SSURGO, air-quality, and other sources. Implementing those watchers before selecting a responsibility owner would multiply the current ambiguity.

ADR-0029 is the accepted directory-governance decision. This proposed ADR applies that responsibility-root discipline to watcher orchestration; it does not amend ADR-0029.

## 2. Decision

If accepted, KFM will use the following ownership rules.

### 2.1 Shared executable orchestration

`pipelines/watchers/` owns long-lived executable orchestration only when the same watcher mechanics are consumed by two or more accepted source/domain lanes without embedding domain-specific interpretation.

Shared orchestration may:

- compare an approved current signal with pinned prior state;
- apply a versioned materiality rule supplied by the owning source/domain configuration;
- create deterministic process memory and a bounded candidate handoff;
- route a candidate to WORK or QUARANTINE review surfaces through governed interfaces.

Shared orchestration may not:

- retrieve an upstream source unless a connector explicitly owns that access;
- activate or admit a source;
- interpret domain meaning that belongs to a domain pipeline;
- create EvidenceBundle closure or PolicyDecision authority;
- write CATALOG/TRIPLET/PUBLISHED state;
- approve promotion, release, correction, rollback, deployment, or publication.

### 2.2 Domain-specific watcher behavior

`pipelines/domains/<domain>/watchers/` owns executable watcher behavior when materiality, sensitivity, cultural authority, interpretation, or review requirements are domain-specific. Domain watchers may reuse bounded helpers from `tools/watchers/` but must not duplicate shared orchestration code.

### 2.3 Declarative intent

`pipeline_specs/watchers/` is the shared declarative home for accepted shared watcher specifications. `pipeline_specs/<domain>/watchers/` is the declarative home for domain-owned watchers. A specification states what may run; it does not activate itself or grant source/network authority.

A watcher specification must identify its executable owner unambiguously. The same active watcher specification must not be maintained in both shared and domain lanes.

### 2.4 Reusable tools

`tools/watchers/` is limited to side-effect-bounded helpers such as parsers, canonicalizers, materiality comparators, local validators, and deterministic fixture utilities. It must not become a scheduler or long-lived orchestration authority.

### 2.5 Candidate output law

Watcher outputs remain pre-publication candidate/process-memory objects. A material-change result may route to WORK or QUARANTINE review, but it is not RAW capture, source truth, ValidationReport, EvidenceBundle, PolicyDecision, ReleaseManifest, or publication.

## 3. Consequences

### Positive

- One responsibility root owns each executable watcher behavior.
- Shared mechanics can be reused without collapsing domain interpretation.
- Pass 20 material-change ideas gain a governed implementation path.
- `tools/` remains side-effect limited.
- Watcher automation remains subordinate to source admission, evidence, policy, lifecycle, and release governance.

### Costs

- Existing duplicate plants-drift placeholders require an explicit migration decision after this ADR is accepted.
- Some current READMEs and paths may need compatibility notes or retirement plans.
- Shared watcher implementations must demonstrate at least two real consumers before being treated as genuinely shared.

### Risks

- Prematurely moving files could break consumers or silently change authority.
- A generic materiality vocabulary could flatten domain meaning if shared too aggressively.
- A watcher could become an accidental publisher if outputs are allowed to bypass lifecycle and release gates.

The migration plan below is therefore mandatory and remains inactive while this ADR is proposed.

## 4. Alternatives considered

### Keep all watchers domain-owned

Rejected as the default because common polling/comparison/receipt mechanics would be duplicated across source/domain lanes. It remains appropriate for behavior whose meaning or sensitivity is genuinely domain-specific.

### Put all watcher behavior in `tools/watchers/`

Rejected because long-lived orchestration is a pipeline responsibility under current directory doctrine; turning `tools/` into a scheduler would blur side-effect and authority boundaries.

### Keep both shared and domain watcher implementations indefinitely

Rejected because parallel executable/specification homes create ambiguous authority, drift, and inconsistent corrections.

### Resolve ad hoc per source without a repository-wide rule

Rejected because Pass 20 calls for several watcher families and the repository already documents the conflict. Repeating the placement decision source-by-source would accumulate design debt.

## 5. Evidence and references

Current-session repository evidence supporting this proposal includes:

- `pipelines/watchers/README.md` — placement conflict, non-publisher law, responsibility split, duplicated plants-drift placeholders;
- `tools/watchers/README.md` and `tools/watchers/plants_watch/README.md` — reusable helper surface;
- `pipeline_specs/watchers/README.md` and `pipeline_specs/flora/watchers/README.md` — declarative shared/domain lanes;
- `contracts/runtime/run_receipt.md` — generic execution process-memory surface;
- `docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md` — accepted directory governance.

The attached Pass 20 dossier supplies implementation pressure for material-change monitoring, but does not establish current repository runtime behavior.

## 6. Migration plan

**HOLD while status is `proposed`.** No file move or runtime activation is authorized by this ADR draft.

After acceptance, perform migration in a separate reviewed PR:

1. inventory every watcher implementation, specification, fixture, workflow, consumer, and generated receipt;
2. classify each watcher as `SHARED_ORCHESTRATION`, `DOMAIN_OWNED`, or `TOOL_HELPER` using the rules above;
3. select one canonical plants-drift specification and mark the other path compatibility-only or retire it with an explicit migration note;
4. update all consumers atomically;
5. add deterministic no-network fixtures for no-change, material-change, malformed-source, stale-state, sensitivity hold, and rights hold;
6. prove watcher output cannot target `data/catalog`, `data/published`, or `release/` directly;
7. bind process memory to the existing RunReceipt family or a separately reviewed watcher-specific profile without creating a competing receipt root;
8. update affected READMEs and registers;
9. run focused and repository-wide validation;
10. only then consider one fixture-first watcher implementation.

No live source activation, credential use, scheduler enablement, or public notification belongs in that migration PR.

## 7. Rollback plan

Before acceptance, close the ADR PR; no runtime behavior changes.

After acceptance but before implementation migration, supersede or reject this ADR through normal ADR governance.

After a later migration, rollback means restoring the prior executable/specification routing through a reviewed revert or migration reversal while preserving historical receipts and records. Rollback must not delete evidence, correction history, or relied-on process memory.

## 8. Open questions

- Which first two watcher consumers are sufficient to prove the shared lane is genuinely shared?
- Should materiality reason codes be a small shared vocabulary with domain extensions, or remain entirely domain-owned?
- Does an accepted watcher-specific RunReceipt profile add value beyond the generic RunReceipt contract?
- What scheduler, if any, is appropriate after fixture-first behavior is proven?
- Which source rights/sensitivity checks must block network activation before the first live watcher?

## 9. Change history

| Date | Change |
|---|---|
| 2026-08-08 | Initial proposed ADR based on current watcher placement conflict and Pass 20 material-change implementation pressure. |
